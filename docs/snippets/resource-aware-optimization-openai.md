---
name: "OpenAI Resource-Aware Optimization"
objective: "Demonstrates a prompt routing system using OpenAI models and Google Custom Search for resource-aware optimization based on query classification."
how_to_run: "This script requires `OPENAI_API_KEY`, `GOOGLE_CUSTOM_SEARCH_API_KEY`, and `GOOGLE_CSE_ID` to be set in a `.env` file. Install dependencies: `pip install openai requests python-dotenv`. Then run the script."
from_note: "../patterns/resource-aware-optimization.md"
---

## Explanation

This code implements a sophisticated **three-tier resource-aware routing system** that optimizes both cost and performance by matching query complexity with appropriate model capabilities. The system intelligently routes user queries through a classification-first architecture.

The implementation consists of four key components:

1. **Query Classification** (`classify_prompt`):
   - Uses GPT-4o to analyze incoming queries
   - Categorizes queries into: "simple" (factual), "reasoning" (multi-step logic), or "internet_search" (current events)
   - Returns structured JSON for downstream routing decisions

2. **Web Search Integration** (`google_search`):
   - Retrieves real-time information via Google Custom Search API
   - Activates only when queries require current data beyond training cutoff
   - Provides context (title, snippet, link) for LLM synthesis

3. **Model Selection** (`generate_response`):
   - **Simple queries** → GPT-4o-mini: Fast, cost-effective for straightforward Q&A
   - **Reasoning queries** → o4-mini: Optimized for complex logic and multi-step problems
   - **Internet search queries** → GPT-4o: Higher capability for synthesizing web results

4. **Orchestration** (`handle_prompt`):
   - Coordinates classification, optional web search, and response generation
   - Returns classification type, selected model, and final response

**Resource Optimization Benefits:**
- **Cost reduction**: Avoid using expensive models (GPT-4o, o4-mini) for simple queries
- **Latency improvement**: Faster models (4o-mini) respond quicker for basic requests
- **Quality preservation**: Complex tasks still get high-capability models
- **Dynamic retrieval**: Only fetch web data when needed, reducing API costs

The example query "What is the capital of Australia?" would route to gpt-4o-mini (simple classification), while "Explain the impact of quantum computing on cryptography" would route to o4-mini (reasoning classification).

## Code

```python
# MIT License
# Copyright (c) 2025 Mahtab Syed
# https://www.linkedin.com/in/mahtabsyed/
import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_CUSTOM_SEARCH_API_KEY = os.getenv("GOOGLE_CUSTOM_SEARCH_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

if not OPENAI_API_KEY or not GOOGLE_CUSTOM_SEARCH_API_KEY or not GOOGLE_CSE_ID:
    raise ValueError(
        "Please set OPENAI_API_KEY, GOOGLE_CUSTOM_SEARCH_API_KEY, and GOOGLE_CSE_ID in your .env file."
    )

client = OpenAI(api_key=OPENAI_API_KEY)

# --- Step 1: Classify the Prompt ---
def classify_prompt(prompt: str) -> dict:
    system_message = {
        "role": "system",
        "content": (
            "You are a classifier that analyzes user prompts and returns one of three categories ONLY:\n\n"
            "- simple\n"
            "- reasoning\n"
            "- internet_search\n\n"
            "Rules:\n"
            "- Use 'simple' for direct factual questions that need no reasoning or current events.\n"
            "- Use 'reasoning' for logic, math, or multi-step inference questions.\n"
            "- Use 'internet_search' if the prompt refers to current events, recent data, or things not in your training data.\n\n"
            "Respond ONLY with JSON like:\n"
            '{ \"classification\": \"simple\" }'
        ),
    }
    user_message = {"role": "user", "content": prompt}
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[system_message, user_message],
        temperature=1
    )
    reply = response.choices[0].message.content
    return json.loads(reply)

# --- Step 2: Google Search ---
def google_search(query: str, num_results=1) -> list:
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_CUSTOM_SEARCH_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        if "items" in results and results["items"]:
            return [
                {
                    "title": item.get("title"),
                    "snippet": item.get("snippet"),
                    "link": item.get("link"),
                }
                for item in results["items"]
            ]
        else:
            return []
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# --- Step 3: Generate Response ---
def generate_response(prompt: str, classification: str, search_results=None) -> str:
    if classification == "simple":
        model = "gpt-4o-mini"
        full_prompt = prompt
    elif classification == "reasoning":
        model = "o4-mini"
        full_prompt = prompt
    elif classification == "internet_search":
        model = "gpt-4o"
        # Convert each search result dict to a readable string
        if search_results:
            search_context = "\n".join(
                [
                    f"Title: {item.get('title')}\nSnippet: {item.get('snippet')}\nLink: {item.get('link')}"
                    for item in search_results
                ]
            )
        else:
            search_context = "No search results found."
        full_prompt = f"Use the following web results to answer the user query: {search_context} Query: {prompt}"
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=1,
    )
    return response.choices[0].message.content, model

# --- Step 4: Combined Router ---
def handle_prompt(prompt: str) -> dict:
    classification_result = classify_prompt(prompt)
    # Remove or comment out the next line to avoid duplicate printing
    # print("\n🔍 Classification Result:", classification_result)
    classification = classification_result["classification"]
    search_results = None
    if classification == "internet_search":
        search_results = google_search(prompt)
        # print("\n🔍 Search Results:", search_results)
    answer, model = generate_response(prompt, classification, search_results)
    return {"classification": classification, "response": answer, "model": model}

test_prompt = "What is the capital of Australia?"
# test_prompt = "Explain the impact of quantum computing on cryptography."
# test_prompt = "When does the Australian Open 2026 start, give me full date?"
result = handle_prompt(test_prompt)
print("🔍 Classification:", result["classification"])
print("🧠 Model Used:", result["model"])
print("🧠 Response:\n", result["response"])
```
