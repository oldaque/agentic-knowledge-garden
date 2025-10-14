---
name: "OpenRouter API Example"
objective: "Demonstrates how to interact with the OpenRouter API for chat completions, showcasing its unified interface for various AI models."
how_to_run: "This script requires an OpenRouter API key. Replace 'YOUR_OPENROUTER_API_KEY' with your actual key. Install dependencies: `pip install requests`. Then run the script."
from_note: "../patterns/resource-aware-optimization.md"
---
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