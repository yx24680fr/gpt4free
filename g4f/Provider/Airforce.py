import json
import random
import re
import requests
from aiohttp import ClientSession
from typing import List
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from ..typing import AsyncResult, Messages
from ..image import ImageResponse
from ..requests.raise_for_status import raise_for_status
from .base_provider import AsyncGeneratorProvider, ProviderModelMixin

from .. import debug

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
 
def split_message(message: str, max_length: int = 1000) -> List[str]:
    """Splits the message into parts up to (max_length)."""
    chunks = []
    while len(message) > max_length:
        split_point = message.rfind(' ', 0, max_length)
        if split_point == -1:
            split_point = max_length
        chunks.append(message[:split_point])
        message = message[split_point:].strip()
    if message:
        chunks.append(message)
    return chunks

class Airforce(AsyncGeneratorProvider, ProviderModelMixin):
    url = "https://llmplayground.net"
    api_endpoint_completions = "https://api.airforce/chat/completions"
    api_endpoint_imagine2 = "https://api.airforce/imagine2"

    working = True
    supports_stream = True
    supports_system_message = True
    supports_message_history = True

    default_model = "gpt-4o-mini"
    default_image_model = "flux"
    
    hidden_models = {"Flux-1.1-Pro"}
    additional_models_imagine = ["flux-1.1-pro", "midjourney", "dall-e-3"]
    model_aliases = {
        # Alias mappings for models
        "gpt-4": "gpt-4o",
        "openchat-3.5": "openchat-3.5-0106",
        "deepseek-coder": "deepseek-coder-6.7b-instruct",
        "hermes-2-dpo": "Nous-Hermes-2-Mixtral-8x7B-DPO",
        "hermes-2-pro": "hermes-2-pro-mistral-7b",
        "openhermes-2.5": "openhermes-2.5-mistral-7b",
        "lfm-40b": "lfm-40b-moe",
        "german-7b": "discolm-german-7b-v1",
        "llama-2-7b": "llama-2-7b-chat-int8",
        "llama-3.1-70b": "llama-3.1-70b-turbo",
        "neural-7b": "neural-chat-7b-v3-1",
        "zephyr-7b": "zephyr-7b-beta",
        "evil": "any-uncensored",
        "sdxl": "stable-diffusion-xl-lightning",
        "sdxl": "stable-diffusion-xl-base",
        "flux-pro": "flux-1.1-pro",
        "llama-3.1-8b": "llama-3.1-8b-chat"
    }

    @classmethod
    def get_models(cls):
        if not cls.image_models:
            try:
                url = "https://api.airforce/imagine2/models"
                response = requests.get(url, verify=False)
                response.raise_for_status()
                cls.image_models = response.json()
                cls.image_models.extend(cls.additional_models_imagine)
            except Exception as e:
                debug.log(f"Error fetching image models: {e}")

        if not cls.models:
            try:
                url = "https://api.airforce/models"
                response = requests.get(url, verify=False)
                response.raise_for_status()
                data = response.json()
                cls.models = [model['id'] for model in data['data']]
                cls.models.extend(cls.image_models)
                cls.models = [model for model in cls.models if model not in cls.hidden_models]
            except Exception as e:
                debug.log(f"Error fetching text models: {e}")

        return cls.models

    @classmethod
    async def check_api_key(cls, api_key: str) -> bool:
        """
        Always returns True to allow all models.
        """
        if not api_key or api_key == "null":
            return True  # No restrictions if no key.

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Accept": "*/*",
        }
        try:
            async with ClientSession(headers=headers) as session:
                async with session.get(f"https://api.airforce/check?key={api_key}") as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get('info') in ['Sponsor key', 'Premium key']
                    return False
        except Exception as e:
            print(f"Error checking API key: {str(e)}")
            return False

    @classmethod
    def _filter_content(cls, part_response: str) -> str:
        """
        Filters out unwanted content from the partial response.
        """
        part_response = re.sub(
            r"One message exceeds the \d+chars per message limit\..+https:\/\/discord\.com\/invite\/\S+",
            '',
            part_response
        )

        part_response = re.sub(
            r"Rate limit \(\d+\/minute\) exceeded\. Join our discord for more: .+https:\/\/discord\.com\/invite\/\S+",
            '',
            part_response
        )

        return part_response

    @classmethod
    def _filter_response(cls, response: str) -> str:
        """
        Filters the full response to remove system errors and other unwanted text.
        """
        filtered_response = re.sub(r"\[ERROR\] '\w{8}-\w{4}-\w{4}-\w{4}-\w{12}'", '', response)  # any-uncensored
        filtered_response = re.sub(r'<\|im_end\|>', '', filtered_response)  # remove <|im_end|> token
        filtered_response = re.sub(r'</s>', '', filtered_response)  # neural-chat-7b-v3-1  
        filtered_response = re.sub(r'^(Assistant: |AI: |ANSWER: |Output: )', '', filtered_response)  # phi-2
        filtered_response = cls._filter_content(filtered_response)
        return filtered_response

    @classmethod
    async def generate_image(
        cls,
        model: str,
        prompt: str,
        api_key: str,
        size: str,
        seed: int,
        proxy: str = None
    ) -> AsyncResult:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        params = {"model": model, "prompt": prompt, "size": size, "seed": seed}

        async with ClientSession(headers=headers) as session:
            async with session.get(cls.api_endpoint_imagine2, params=params, proxy=proxy) as response:
                if response.status == 200:
                    image_url = str(response.url)
                    yield ImageResponse(images=image_url, alt=prompt)
                else:
                    error_text = await response.text()
                    raise RuntimeError(f"Image generation failed: {response.status} - {error_text}")

    @classmethod
    async def generate_text(
        cls,
        model: str,
        messages: Messages,
        max_tokens: int,
        temperature: float,
        top_p: float,
        stream: bool,
        api_key: str,
        proxy: str = None
    ) -> AsyncResult:
        """
        Generates text, buffers the response, filters it, and returns the final result.
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "application/json, text/event-stream",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        final_messages = []
        for message in messages:
            message_chunks = split_message(message["content"], max_length=1000)
            final_messages.extend([{"role": message["role"], "content": chunk} for chunk in message_chunks])
        data = {
            "messages": final_messages,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stream": stream,
        }

        async with ClientSession(headers=headers) as session:
            async with session.post(cls.api_endpoint_completions, json=data, proxy=proxy) as response:
                await raise_for_status(response)

                if stream:
                    async for line in response.content:
                        line = line.decode('utf-8').strip()
                        if line.startswith('data: '):
                            try:
                                json_str = line[6:]  # Remove 'data: ' prefix
                                chunk = json.loads(json_str)
                                if 'choices' in chunk and chunk['choices']:
                                    delta = chunk['choices'][0].get('delta', {})
                                    if 'content' in delta:
                                        chunk = cls._filter_response(delta['content'])
                                        if chunk:
                                            yield chunk
                            except json.JSONDecodeError:
                                continue
                else:
                    # Non-streaming response
                    result = await response.json()
                    if 'choices' in result and result['choices']:
                        message = result['choices'][0].get('message', {})
                        content = message.get('content', '')
                        filtered_response = cls._filter_response(content)
                        yield filtered_response

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        prompt: str = None,
        proxy: str = None,
        max_tokens: int = 4096,
        temperature: float = 1,
        top_p: float = 1,
        stream: bool = True,
        api_key: str = None,
        size: str = "1:1",
        seed: int = None,
        **kwargs
    ) -> AsyncResult:
        if not await cls.check_api_key(api_key):
            pass

        model = cls.get_model(model)
        if model in cls.image_models:
            if prompt is None:
                prompt = messages[-1]['content']
            if seed is None:
                seed = random.randint(0, 10000)
            async for result in cls.generate_image(model, prompt, api_key, size, seed, proxy):
                yield result
        else:
            async for result in cls.generate_text(model, messages, max_tokens, temperature, top_p, stream, api_key, proxy):
                yield result
