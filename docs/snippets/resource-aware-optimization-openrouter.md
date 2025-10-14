---
name: "OpenRouter API Example"
objective: "Demonstrates how to interact with the OpenRouter API for chat completions, showcasing its unified interface for various AI models."
how_to_run: "This script requires an OpenRouter API key. Replace 'YOUR_OPENROUTER_API_KEY' with your actual key. Install dependencies: `pip install requests`. Then run the script."
from_note: "../patterns/resource-aware-optimization.md"
---

## Explanation

This code demonstrates the **OpenRouter API**, a unified gateway that provides access to multiple LLM providers (OpenAI, Anthropic, Google, Meta, Mistral, etc.) through a single, OpenAI-compatible API interface. OpenRouter is particularly valuable for resource-aware optimization as it enables:

**Key Features:**
1. **Provider Abstraction**: Access dozens of models through one API, eliminating the need to integrate multiple SDKs
2. **Model Routing**: Specify models like `openai/gpt-4o`, `anthropic/claude-3-opus`, `google/gemini-pro`, etc.
3. **Fallback Handling**: OpenRouter can automatically fallback to alternative models if primary choices are unavailable
4. **Cost Optimization**: Compare pricing across providers and switch models dynamically
5. **Load Balancing**: OpenRouter handles rate limits and load distribution across providers

**Resource Optimization Use Cases:**
- **Dynamic Model Selection**: Route complex queries to GPT-4o, simple ones to GPT-3.5-turbo or Gemini Flash
- **Cost Management**: Track spending across different model tiers and providers
- **Provider Diversity**: Avoid vendor lock-in by easily switching between OpenAI, Anthropic, Google
- **Availability Resilience**: Automatic fallback if a provider experiences downtime

**API Structure:**
- **Authorization Header**: Bearer token with your OpenRouter API key
- **HTTP-Referer** (optional): Your site URL for usage analytics on openrouter.ai
- **X-Title** (optional): Your app name for identification
- **model**: Specify the model in format `provider/model-name`
- **messages**: Standard OpenAI chat format with roles (system, user, assistant)

The example shows a basic chat completion request asking "What is the meaning of life?" using OpenAI's GPT-4o through OpenRouter. In production, you would implement logic to select different models based on query complexity, cost constraints, or latency requirements.

## Code

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer ",
        "HTTP-Referer": "", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "openai/gpt-4o", # Optional
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ]
    })
)
```
