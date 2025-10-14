---
name: "Inter-Agent Communication - ADK Agent Creation"
objective: "Demonstrates creating A2A-compliant agents using Google ADK for calendar management."
how_to_run: "Requires Google ADK and calendar API credentials. Run: python inter-agent-communication-a2a-adk-agent-creation.py"
from_note: "../patterns/inter-agent-communication-a2a.md"
---

# A2A Agent Creation for Calendar Management

This example shows how to create A2A-compliant agents using Google ADK for calendar management functionality.

## Code Example

```python
import datetime
from google.adk.agents import LlmAgent # type: ignore[import-untyped]
from google.adk.tools.google_api_tool import CalendarToolset # type: ignore[import-untyped]

async def create_agent(client_id, client_secret) -> LlmAgent:
    """Constructs the ADK agent."""
    toolset = CalendarToolset(client_id=client_id, client_secret=client_secret)
    return LlmAgent(
        model='gemini-2.0-flash-001',
        name='calendar_agent',
        description="An agent that can help manage a user's calendar",
        instruction=f"""
You are an agent that can help manage a user's calendar. Users will request information about the state of their calendar or to make changes to their calendar. Use the provided tools for interacting with the calendar API. If not specified, assume the calendar the user wants is the 'primary' calendar. When using the Calendar API tools, use well-formed RFC3339 timestamps. Today is {datetime.datetime.now()}.
        """,
        tools=await toolset.get_tools(),
    )
```

## Explanation

This example demonstrates how to create A2A-compliant agents using Google ADK:

1. **CalendarToolset**: Initializes calendar API tools with OAuth credentials
2. **LlmAgent Configuration**: Creates an agent with calendar management capabilities
3. **A2A Compliance**: Uses standard ADK agent structure compatible with A2A protocol
4. **Tool Integration**: Loads Google Calendar API tools for event management

The agent can handle calendar queries and modifications through the A2A protocol interface.</content>
