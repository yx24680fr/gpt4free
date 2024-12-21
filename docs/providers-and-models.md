


# G4F - Providers and Models

This document provides an overview of various AI providers and models, including text generation, image generation, and vision capabilities. It aims to help users navigate the diverse landscape of AI services and choose the most suitable option for their needs.

## Table of Contents
  - [Providers](#providers)
    - [Free](#providers-free)
    - [Needs Auth](#providers-needs-auth)
  - [Models](#models)
    - [Text Models](#text-models)
    - [Image Models](#image-models)
  - [Conclusion and Usage Tips](#conclusion-and-usage-tips)

---
## Providers

### Providers Free
| Website | Provider | Text Models | Image Models | Vision Models | Stream | Status | Auth |
|----------|-------------|--------------|---------------|--------|--------|------|------|
|[api.airforce](https://api.airforce)|`g4f.Provider.Airforce`|`phi-2, gpt-4, gpt-4o-mini, gpt-4o, gpt-4-turbo, o1-mini, openchat-3.5, deepseek-coder, hermes-2-dpo, hermes-2-pro, openhermes-2.5, lfm-40b, german-7b, llama-2-7b, llama-3.1-70b, neural-7b, zephyr-7b, evil,`|`sdxl, flux-pro, flux, flux-realism, flux-anime, flux-3d, flux-disney, flux-pixel, flux-4o, any-dark, midjourney, dall-e-3`|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌+✔|
|[amigochat.io](https://amigochat.io/chat/)|`g4f.Provider.AmigoChat`|✔|✔|❌|✔|![Error](https://img.shields.io/badge/RateLimit-f48d37)|❌|
|[blackbox.ai](https://www.blackbox.ai)|`g4f.Provider.Blackbox`|`blackboxai, gpt-4, gpt-4o, gemini-pro, claude-3.5-sonnet, blackboxai-pro, llama-3.1-8b, llama-3.1-70b, llama-3.1-405b, llama-3.3-70b, mixtral-7b, deepseek-chat, dbrx-instruct, qwq-32b, hermes-2-dpo`|`flux`|`blackboxai, gpt-4o, gemini-pro, gemini-flash, llama-3.1-8b, llama-3.1-70b, llama-3.1-405b`|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[blackbox.ai](https://www.blackbox.ai)|`g4f.Provider.Blackbox2`|`llama-3.1-70b`|`flux`|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[chatgpt.com](https://chatgpt.com)|`g4f.Provider.ChatGpt`|✔|❌|❌|✔|![Error](https://img.shields.io/badge/HTTPError-f48d37)|❌|
|[chatgpt.es](https://chatgpt.es)|`g4f.Provider.ChatGptEs`|`gpt-4, gpt-4o, gpt-4o-mini`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[playground.ai.cloudflare.com](https://playground.ai.cloudflare.com)|`g4f.Provider.Cloudflare`|`llama-2-7b, llama-3-8b, llama-3.1-8b, llama-3.2-1b, qwen-1.5-7b`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[copilot.microsoft.com](https://copilot.microsoft.com)|`g4f.Provider.Copilot`|`gpt-4`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[darkai.foundation](https://darkai.foundation)|`g4f.Provider.DarkAI`|`gpt-3.5-turbo, gpt-4o, llama-3.1-70b`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[duckduckgo.com/aichat](https://duckduckgo.com/aichat)|`g4f.Provider.DDG`|`gpt-4, gpt-4o-mini, claude-3-haiku, llama-3.1-70b, mixtral-8x7b`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[deepinfra.com/chat](https://deepinfra.com/chat)|`g4f.Provider.DeepInfraChat`|`llama-3.1-8b, llama-3.1-70b, qwq-32b, wizardlm-2-8x22b, qwen-2-72b, qwen-2.5-coder-32b, nemotron-70b`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[black-forest-labs-flux-1-dev.hf.space](https://black-forest-labs-flux-1-dev.hf.space)|`g4f.Provider.Flux`|❌|`flux-dev`|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[chat10.free2gpt.xyz](https://chat10.free2gpt.xyz)|`g4f.Provider.Free2GPT`|`mistral-7b`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[freegptsnav.aifree.site](https://freegptsnav.aifree.site)|`g4f.Provider.FreeGpt`|`gemini-pro`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[app.giz.ai/assistant](https://app.giz.ai/assistant)|`g4f.Provider.GizAI`|`gemini-flash`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[liaobots.work](https://liaobots.work)|`g4f.Provider.Liaobots`|`grok-beta, gpt-4o-mini, gpt-4o, gpt-4, o1-preview, o1-mini, claude-3-opus, claude-3.5-sonnet, claude-3-sonnet, gemini-flash, gemini-pro`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[mhystical.cc](https://mhystical.cc)|`g4f.Provider.Mhystical`|`gpt-4`|❌|❌|✔|![Error](https://img.shields.io/badge/Active-brightgreen)|❌|
|[labs.perplexity.ai](https://labs.perplexity.ai)|`g4f.Provider.PerplexityLabs`|`sonar-online, sonar-chat, llama-3.3-70b, llama-3.1-8b, llama-3.1-70b, lfm-40b`|❌|❌|✔|![Error](https://img.shields.io/badge/Active-brightgreen)|❌|
|[pi.ai/talk](https://pi.ai/talk)|`g4f.Provider.Pi`|`pi`|❌|❌|✔|![Error](https://img.shields.io/badge/Active-brightgreen)|❌|
|[pizzagpt.it](https://www.pizzagpt.it)|`g4f.Provider.Pizzagpt`|`gpt-4o-mini`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[pollinations.ai](https://pollinations.ai)|`g4f.Provider.PollinationsAI`|`gpt-4o, mistral-large, mistral-nemo, llama-3.1-70b, gpt-4, qwen-2.5-coder-32b, claude-3.5-sonnet, command-r, evil, p1,turbo, unity, midijourney, rtist`|`flux, flux-realism, flux-cablyai, flux-anime, flux-3d, any-dark, flux-pro, midjourney, dall-e-3`|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[app.prodia.com](https://app.prodia.com)|`g4f.Provider.Prodia`|❌|✔|❌|❌|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[replicate.com](https://replicate.com)|`g4f.Provider.ReplicateHome`|`gemma-2b`|`sd-3, sdxl, playground-v2.5`|❌|❌|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[rubiks.ai](https://rubiks.ai)|`g4f.Provider.RubiksAI`|`gpt-4o-mini, llama-3.1-70b`|❌|❌|✔|![Error](https://img.shields.io/badge/Active-brightgreen)|❌|
|[teach-anything.com](https://www.teach-anything.com)|`g4f.Provider.TeachAnything`|`llama-3.1-70b`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[you.com](https://you.com)|`g4f.Provider.You`|✔|✔|✔|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|


---
### Providers Needs Auth
| Provider | Text Models | Image Models | Vision Models | Stream | Status | Auth |
|----------|-------------|--------------|---------------|--------|--------|------|
|[bing.com/images/create](https://www.bing.com/images/create)|`g4f.Provider.BingCreateImages`|❌|`dall-e-3`|❌|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[inference.cerebras.ai](https://inference.cerebras.ai/)|`g4f.Provider.Cerebras`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|❌|
|[deepinfra.com](https://deepinfra.com)|`g4f.Provider.DeepInfra`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[deepinfra.com](https://deepinfra.com)|`g4f.Provider.DeepInfraImage`|❌|✔|❌|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[gemini.google.com](https://gemini.google.com)|`g4f.Provider.Gemini`|`gemini`|`gemini`|`gemini`|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[ai.google.dev](https://ai.google.dev)|`g4f.Provider.GeminiPro`|`gemini-pro`|❌|`gemini-pro`|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[github.com/copilot](https://github.com/copilot)|`g4f.Provider.GithubCopilot`|✔|❌|❌|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[console.groq.com/playground](https://console.groq.com/playground)|`g4f.Provider.Groq`|✔|❌|✔|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[huggingface.co/chat](https://huggingface.co/chat)|`g4f.Provider.HuggingChat`|`qwen-2.5-72b, llama-3.3-70b, command-r-plus, qwq-32b, nemotron-70b, nemotron-70b, llama-3.2-11b, hermes-3, mistral-nemo, phi-3.5-mini`|`flux-dev`|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[huggingface.co/chat](https://huggingface.co/chat)|`g4f.Provider.HuggingFace`|✔|✔|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[api-inference.huggingface.co](https://api-inference.huggingface.co)|`g4f.Provider.HuggingFaceAPI`|✔|❌|✔|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[meta.ai](https://www.meta.ai)|`g4f.Provider.MetaAI`|`meta-ai`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[designer.microsoft.com](https://designer.microsoft.com)|`g4f.Provider.MicrosoftDesigner`|❌|`dall-e-3`|❌|❌|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[platform.openai.com](https://platform.openai.com)|`g4f.Provider.OpenaiAPI`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[chatgpt.com](https://chatgpt.com)|`g4f.Provider.OpenaiChat`|`gpt-4o, gpt-4o-mini, gpt-4, ...`|❌|✔|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[perplexity.ai](https://www.perplexity.ai)|`g4f.Provider.PerplexityApi`|`gpt-4o, gpt-4o-mini, gpt-4, ...`|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[poe.com](https://poe.com)|`g4f.Provider.Poe`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[raycast.com](https://raycast.com)|`g4f.Provider.Raycast`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[chat.reka.ai](https://chat.reka.ai)|`g4f.Provider.Reka`|`reka-core`|❌|✔|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[replicate.com](https://replicate.com)|`g4f.Provider.Replicate`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[beta.theb.ai](https://beta.theb.ai)|`g4f.Provider.Theb`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[beta.theb.ai](https://beta.theb.ai)|`g4f.Provider.WhiteRabbitNeo`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|
|[whiterabbitneo.com](https://www.whiterabbitneo.com)|`g4f.Provider.WhiteRabbitNeo`|✔|❌|❌|✔|![](https://img.shields.io/badge/Active-brightgreen)|✔|

---

## Models

### Text Models
| Model | Base Provider | Providers | Website |
|-------|---------------|-----------|---------|
|gpt_35_turbo|OpenAI|2+ Providers|[platform.openai.com](https://platform.openai.com/docs/models/gpt-3-5-turbo)|
|gpt-4|OpenAI|8+ Providers|[platform.openai.com](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4)|
|gpt-4-turbo|OpenAI|1+ Providers|[platform.openai.com](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4)|
|gpt-4o|OpenAI|8+ Providers|[platform.openai.com](https://platform.openai.com/docs/models/gpt-4o)|
|gpt-4o-mini|OpenAI|8+ Providers|[platform.openai.com](https://platform.openai.com/docs/models/gpt-4o-mini)|
|o1-preview|OpenAI|1+ Providers|[platform.openai.com](https://openai.com/index/introducing-openai-o1-preview/)|
|o1-mini|OpenAI|2+ Providers|[platform.openai.com](https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/)|
|gigachat||1+ Providers|[]( )|
|llama-2-7b|Meta Llama|2+ Providers|[huggingface.co](https://huggingface.co/meta-llama/Llama-2-7b)|
|llama-3-8b|Meta Llama|1+ Providers|[ai.meta.com](https://ai.meta.com/blog/meta-llama-3/)|
|llama-3.1-8b|Meta Llama|5+ Providers|[ai.meta.com](https://ai.meta.com/blog/meta-llama-3-1/)|
|llama-3.1-70b|Meta Llama|12+ Providers|[ai.meta.com](https://ai.meta.com/blog/meta-llama-3-1/)|
|llama-3.1-405b|Meta Llama|1+ Providers|[ai.meta.com](https://ai.meta.com/blog/meta-llama-3-1/)|
|llama-3.2-11b|Meta Llama|2+ Providers|[ai.meta.com](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)|
|llama-3.3-70b|Meta Llama|4+ Providers|[llama.com/]()|
|mixtral-7b|Mistral AI|1+ Providers|[mistral.ai](https://mistral.ai/news/mixtral-of-experts/)|
|mixtral-8x7b|Mistral AI|1+ Providers|[mistral.ai](https://mistral.ai/news/mixtral-of-experts/)|
|mistral-nemo|Mistral AI|3+ Providers|[huggingface.co](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)|
|mistral-large|Mistral AI|1+ Providers|[mistral.ai](https://mistral.ai/news/mistral-large-2407/)|
|hermes-2-dpo|NousResearch|1+ Providers|[huggingface.co](https://huggingface.co/NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO)|
|hermes-2-pro|NousResearch|1+ Providers|[huggingface.co](https://huggingface.co/NousResearch/Hermes-2-Pro-Mistral-7B)|
|hermes-3|NousResearch|1+ Providers|[nousresearch.com](https://nousresearch.com/hermes3/)|
|gemini|Google DeepMind|1+ Providers|[deepmind.google](http://deepmind.google/technologies/gemini/)|
|gemini-flash|Google DeepMind|4+ Providers|[deepmind.google](https://deepmind.google/technologies/gemini/flash/)|
|gemini-pro|Google DeepMind|5+ Providers|[deepmind.google](https://deepmind.google/technologies/gemini/pro/)|
|gemma-2b|Google|1+ Providers|[huggingface.co](https://huggingface.co/google/gemma-2b)|
|claude-3-haiku|Anthropic|1+ Providers|[anthropic.com](https://www.anthropic.com/news/claude-3-haiku)|
|claude-3-sonnet|Anthropic|1+ Providers|[anthropic.com](https://www.anthropic.com/news/claude-3-family)|
|claude-3-opus|Anthropic|1+ Providers|[anthropic.com](https://www.anthropic.com/news/claude-3-family)|
|claude-3.5-sonnet|Anthropic|3+ Providers|[anthropic.com](https://www.anthropic.com/news/claude-3-5-sonnet)|
|reka-core|Reka AI|1+ Providers|[reka.ai](https://www.reka.ai/ourmodels)|
|blackboxai|Blackbox AI|1+ Providers|[docs.blackbox.chat](https://docs.blackbox.chat/blackbox-ai-1)|
|blackboxai-pro|Blackbox AI|1+ Providers|[docs.blackbox.chat](https://docs.blackbox.chat/blackbox-ai-1)|
|command-r-plus|CohereForAI|1+ Providers|[docs.cohere.com](https://docs.cohere.com/docs/command-r-plus)|
|command-r|CohereForAI|1+ Providers|[docs.cohere.com](https://docs.cohere.com/docs/command-r-plus)|
|qwen|Qwen|1+ Providers|[huggingface.co](https://huggingface.co/Qwen)|
|qwen-1.5-7b|Qwen|2+ Providers|[huggingface.co](https://huggingface.co/Qwen/Qwen1.5-7B)|
|qwen-2-72b|Qwen|1+ Providers|[huggingface.co](https://huggingface.co/Qwen/Qwen2-72B)|
|qwen-2.5-72b|Qwen|2+ Providers|[huggingface.co](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)|
|qwen-2.5-coder-32b|Qwen|4+ Providers|[huggingface.co](https://huggingface.co/Qwen/Qwen2.5-Coder-32B)|
|qwq-32b|Qwen|4+ Providers|[qwen2.org](https://qwen2.org/qwq-32b-preview/)|
|pi|Inflection|1+ Providers|[inflection.ai](https://inflection.ai/blog/inflection-2-5)|
|deepseek-chat|DeepSeek|1+ Providers|[huggingface.co](https://huggingface.co/deepseek-ai/deepseek-llm-67b-chat)|
|deepseek-coder|DeepSeek|1+ Providers|[huggingface.co](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct)|
|wizardlm-2-8x22b|WizardLM|1+ Providers|[huggingface.co](https://huggingface.co/alpindale/WizardLM-2-8x22B)|
|openchat-3.5|OpenChat|1+ Providers|[huggingface.co](https://huggingface.co/openchat/openchat_3.5)|
|grok-beta|x.ai|1+ Providers|[x.ai](https://x.ai/blog/grok-2)|
|sonar-online|Perplexity AI|2+ Providers|[docs.perplexity.ai](https://docs.perplexity.ai/)|
|sonar-chat|Perplexity AI|1+ Providers|[docs.perplexity.ai](https://docs.perplexity.ai/)|
|nemotron-70b|Nvidia|3+ Providers|[build.nvidia.com](https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct)|
|openhermes-2.5|Teknium|1+ Providers|[huggingface.co](https://huggingface.co/datasets/teknium/OpenHermes-2.5)|
|lfm-40b|Liquid|2+ Providers|[liquid.ai](https://www.liquid.ai/liquid-foundation-models)|
|german-7b|TheBloke|1+ Providers|[huggingface.co](https://huggingface.co/TheBloke/DiscoLM_German_7b_v1-GGUF)|
|zephyr-7b|HuggingFaceH4|1+ Providers|[huggingface.co](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)|
|neural-7b|Inferless|1+ Providers|[huggingface.co](https://huggingface.co/Intel/neural-chat-7b-v3-1)|
|p1|PollinationsAI|1+ Providers|[]( )|
|dbrx-instruct|Databricks|1+ Providers|[huggingface.co](https://huggingface.co/databricks/dbrx-instruct)|
|evil|Evil Mode - Experimental|2+ Providers|[]( )|
|midijourney||1+ Providers|[]( )|
|turbo||1+ Providers|[]( )|
|unity||1+ Providers|[]( )|
|rtist||1+ Providers|[]( )|



### Image Models
| Model | Base Provider | Providers | Website |
|-------|---------------|-----------|---------|
|sdxl|Stability AI|2+ Providers|[huggingface.co](https://huggingface.co/docs/diffusers/en/using-diffusers/sdxl)|
|sdxl-lora|Stability AI|1+ Providers|[huggingface.co](https://huggingface.co/blog/lcm_lora)|
|sd-3|Stability AI|1+ Providers|[huggingface.co](https://huggingface.co/docs/diffusers/main/en/api/pipelines/stable_diffusion/stable_diffusion_3)|
|playground-v2.5|Playground AI|1+ Providers|[huggingface.co](https://huggingface.co/playgroundai/playground-v2.5-1024px-aesthetic)|
|flux|Black Forest Labs|4+ Providers|[github.com/black-forest-labs/flux](https://github.com/black-forest-labs/flux)|
|flux-pro|Black Forest Labs|2+ Providers|[github.com/black-forest-labs/flux](https://github.com/black-forest-labs/flux)|
|flux-dev|Black Forest Labs|3+ Providers|[huggingface.co](https://huggingface.co/black-forest-labs/FLUX.1-dev)|
|flux-realism|Flux AI|2+ Providers|[]( )|
|flux-cablyai|Flux AI|1+ Providers|[]( )|
|flux-anime|Flux AI|2+ Providers|[]( )|
|flux-3d|Flux AI|2+ Providers|[]( )|
|flux-disney|Flux AI|1+ Providers|[]( )|
|flux-pixel|Flux AI|1+ Providers|[]( )|
|flux-4o|Flux AI|1+ Providers|[]( )|
|flux-schnell|Black Forest Labs|2+ Providers|[huggingface.co](https://huggingface.co/black-forest-labs/FLUX.1-schnell)|
|dall-e-3|OpenAI|5+ Providers|[openai.com](https://openai.com/index/dall-e/)|
|midjourney|Midjourney|2+ Providers|[docs.midjourney.com](https://docs.midjourney.com/docs/model-versions)|
|any-dark||2+ Providers|[]( )|

## Conclusion and Usage Tips
This document provides a comprehensive overview of various AI providers and models available for text generation, image generation, and vision tasks. **When choosing a provider or model, consider the following factors:**
   1. **Availability**: Check the status of the provider to ensure it's currently active and accessible.
   2. **Model Capabilities**: Different models excel at different tasks. Choose a model that best fits your specific needs, whether it's text generation, image creation, or vision-related tasks.
   3. **Authentication**: Some providers require authentication, while others don't. Consider this when selecting a provider for your project.
   4. **Streaming Support**: If real-time responses are important for your application, prioritize providers that offer streaming capabilities.
   5. **Vision Models**: For tasks requiring image understanding or multimodal interactions, look for providers offering vision models.

Remember to stay updated with the latest developments in the AI field, as new models and providers are constantly emerging and evolving.

---

[Return to Home](/)
