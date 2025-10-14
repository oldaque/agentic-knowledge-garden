---
name: "Knowledge Retrieval (RAG) with ADK and Google Search"
objective: "Demonstrates how to use the Google Search tool within the ADK framework for knowledge retrieval."
how_to_run: "Requires Google ADK. Run as part of an ADK agent."
from_note: "../patterns/knowledge-retrieval-rag.md"
---

# Knowledge Retrieval with ADK and Google Search

This snippet shows how to create a simple agent that uses the `google_search` tool for research tasks.

## Code Example

```python
from google.adk.tools import google_search
from google.adk.agents import Agent

search_agent = Agent(
    name="research_assistant",
    model="gemini-2.0-flash-exp",
    instruction="You help users research topics. When asked, use the Google Search tool",
    tools=[google_search]
)
```

## How It Works

- The `google_search` tool is imported from the ADK library.
- An `Agent` is created with an instruction to use the search tool.
- The `google_search` tool is passed to the agent's `tools` list, making it available for the agent to use.
