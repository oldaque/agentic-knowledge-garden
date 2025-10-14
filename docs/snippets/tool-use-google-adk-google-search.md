---
name: "Tool Use with ADK: Google Search"
objective: "Demonstrates how to use the pre-built Google Search tool with an ADK agent."
how_to_run: "Requires Google ADK. Run with `python your_script_name.py`."
from_note: "../patterns/tool-use.md"
---

# Tool Use with ADK: Google Search

This snippet shows how to use the pre-built `google_search` tool in the Google ADK. An agent is created and given the search tool to answer user questions.

## Code Example

```python
from google.adk.agents import Agent as ADKAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import nest_asyncio
import asyncio

APP_NAME="Google_Search_agent"
USER_ID="user1234"
SESSION_ID="1234"

root_agent = ADKAgent(
    name="basic_search_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    tools=[google_search] # Google Search is a pre-built tool to perform Google searches.
)

# Agent Interaction
async def call_agent(query):
    """
    Helper function to call the agent with a query.
    """

    # Session and Runner
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)

nest_asyncio.apply()

asyncio.run(call_agent("what's the latest ai news?"))
```

## How It Works

1.  **Import Tool**: The `google_search` tool is imported directly from `google.adk.tools`.
2.  **Agent with Tool**: An `ADKAgent` is created, and the `google_search` tool is passed into its `tools` list.
3.  **Instruction**: The agent's `instruction` tells it that it can search the internet to answer questions. This, combined with the tool's own description, helps the LLM decide when to use the tool.
4.  **Execution**: When the agent is run with a query, it recognizes that it needs external information, calls the `google_search` tool, and then uses the search results to formulate a final answer.