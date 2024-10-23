# G4F - Async client API Guide
The G4F async client API is a powerful asynchronous interface for interacting with various AI models. This guide provides comprehensive information on how to use the API effectively, including setup, usage examples, best practices, and important considerations for optimal performance.


## Compatibility Note
The G4F async client API is designed to be compatible with the OpenAI API, making it easy for developers familiar with OpenAI's interface to transition to G4F.

## Table of Contents
   - [Introduction](#introduction)
   - [Key Features](#key-features)
   - [Getting Started](#getting-started)
   - [Initializing the Client](#initializing-the-client)
   - [Configuration](#configuration)
   - [Usage Examples](#usage-examples)
   - [Text Completions](#text-completions)
   - [Streaming Completions](#streaming-completions)
   - [Using a Vision Model](#using-a-vision-model)
   - [Image Generation](#image-generation)
   - [Concurrent Tasks](#concurrent-tasks-with-asynciogather)
   - [Available Models and Providers](#available-models-and-providers)
   - [Error Handling and Best Practices](#error-handling-and-best-practices)
   - [Rate Limiting and API Usage](#rate-limiting-and-api-usage)
   - [Conclusion](#conclusion)

  

## Introduction
The G4F async client API is an asynchronous version of the standard G4F Client API. It offers the same functionality as the synchronous API but with improved performance due to its asynchronous nature. This guide will walk you through the key features and usage of the G4F async client API.
  

## Key Features
   - **Custom Providers**: Use custom providers for enhanced flexibility.
   - **ChatCompletion Interface**: Interact with chat models through the ChatCompletion class.
   - **Streaming Responses**: Get responses iteratively as they are received.
   - **Non-Streaming Responses**: Generate complete responses in a single call.
   - **Image Generation and Vision Models**: Support for image-related tasks.

  

## Getting Started
### Initializing the Client
**To use the G4F `Client`, create a new instance:**
```python
from g4f.client import Client
from g4f.Provider import OpenaiChat, Gemini

client = Client(
    provider=OpenaiChat,
    image_provider=Gemini,
    # Add other parameters as needed
)
```

  

### Configuration
**Configure the `Client` with additional settings:**
```python
client = Client(
    api_key="your_api_key_here",
    proxies="http://user:pass@host",
    # Add other parameters as needed
)
```

  

## Usage Examples
### Text Completions
**Generate text completions using the ChatCompletions endpoint:**
```python
import asyncio
from g4f.client import Client

async def main():
    client = Client()
    
    response = await client.chat.completions.async_create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test"
            }
        ]
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())
```

  

### Streaming Completions
**Process responses incrementally as they are generated:**
```python
import asyncio
from g4f.client import Client

async def main():
    client = Client()
    
    stream = await client.chat.completions.async_create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test"
            }
        ],
        stream=True,
    )
    
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

asyncio.run(main())
```

  

### Using a Vision Model
**Analyze an image and generate a description:**
```python
import g4f
import requests
import asyncio
from g4f.client import Client

async def main():
    client = Client()
    
    image = requests.get("https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/cat.jpeg", stream=True).raw
    
    response = await client.chat.completions.async_create(
        model=g4f.models.default,
        provider=g4f.Provider.Bing,
        messages=[
            {
                "role": "user",
                "content": "What's in this image?"
            }
        ],
        image=image
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())
```

  

### Image Generation
**Generate images using a specified prompt:**
```python
import asyncio
from g4f.client import Client

async def main():
    client = Client()
    
    response = await client.images.async_generate(
        prompt="a white siamese cat",
        model="dall-e-3"
    )
    
    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

asyncio.run(main())
```

  

#### Base64 Response Format
```python
import asyncio
from g4f.client import Client

async def main():
    client = Client()
    
    response = await client.images.async_generate(
        prompt="a white siamese cat",
        model="dall-e-3",
        response_format="b64_json"
    )
    
    base64_text = response.data[0].b64_json
    print(base64_text)

asyncio.run(main())
```

  

### Concurrent Tasks with asyncio.gather
**Execute multiple tasks concurrently:**
```python
import asyncio
from g4f.client import Client

async def main():
    client = Client()
    
    task1 = client.chat.completions.async_create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test"
            }
        ]
    )
    
    task2 = client.images.async_generate(
        model="dall-e-3",
        prompt="a white siamese cat"
    )
    
    chat_response, image_response = await asyncio.gather(task1, task2)
    
    print("Chat Response:")
    print(chat_response.choices[0].message.content)
    
    print("Image Response:")
    print(image_response.data[0].url)

asyncio.run(main())
```

  

## Available Models and Providers
The G4F AsyncClient supports a wide range of AI models and providers, allowing you to choose the best option for your specific use case. **Here's a brief overview of the available models and providers:**

### Models
   - GPT-3.5-Turbo
   - GPT-4
   - DALL-E 3
   - Gemini
   - Claude (Anthropic)
   - And more...

  

### Providers
   - OpenAI
   - Google (for Gemini)
   - Anthropic
   - Bing
   - Custom providers

  

**To use a specific model or provider, specify it when creating the client or in the API call:**
```python
client = AsyncClient(provider=g4f.Provider.OpenaiChat)

# or

response = await client.chat.completions.async_create(
    model="gpt-4",
    provider=g4f.Provider.Bing,
    messages=[
        {
            "role": "user",
            "content": "Hello, world!"
        }
    ]
)
```

  

## Error Handling and Best Practices
Implementing proper error handling and following best practices is crucial when working with the G4F AsyncClient API. This ensures your application remains robust and can gracefully handle various scenarios. **Here are some key practices to follow:**

1. **Use try-except blocks to catch and handle exceptions:**
```python
try:
    response = await client.chat.completions.async_create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Hello, world!"
            }
        ]
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

2. **Check the response status and handle different scenarios:**
```python
if response.choices:
    print(response.choices[0].message.content)
else:
    print("No response generated")
```

3. **Implement retries for transient errors:**
```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
async def make_api_call():
    # Your API call here
    pass
```

  

## Rate Limiting and API Usage
When working with the G4F AsyncClient API, it's important to implement rate limiting and monitor your API usage. This helps ensure fair usage, prevents overloading the service, and optimizes your application's performance. Here are some key strategies to consider:
  

1. **Implement rate limiting in your application:**
```python
import asyncio
from aiolimiter import AsyncLimiter

rate_limit = AsyncLimiter(max_rate=10, time_period=1)  # 10 requests per second

async def make_api_call():
    async with rate_limit:
        # Your API call here
        pass
```

  

2. **Monitor your API usage and implement logging:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def make_api_call():
    try:
        response = await client.chat.completions.async_create(...)
        logger.info(f"API call successful. Tokens used: {response.usage.total_tokens}")
    except Exception as e:
        logger.error(f"API call failed: {e}")
```

  

3. **Use caching to reduce API calls for repeated queries:**
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_response(query):
    # Your API call here
    pass
```

## Conclusion
The G4F async client API provides a powerful and flexible way to interact with various AI models asynchronously. By leveraging its features and following best practices, you can build efficient and responsive applications that harness the power of AI for text generation, image analysis, and image creation.

Remember to handle errors gracefully, implement rate limiting, and monitor your API usage to ensure optimal performance and reliability in your applications.

---

[Return to Home](/)
