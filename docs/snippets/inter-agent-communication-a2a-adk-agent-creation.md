---
title: "Inter-Agent Communication - ADK Agent Creation"
slug: "inter-agent-communication-a2a-adk-agent-creation"
summary: "Demonstrates creating A2A-compliant agents using Google ADK for calendar management functionality with OAuth integration."
tags: ["google-adk", "a2a", "inter-agent-communication", "calendar", "oauth"]
status: "stable"
last_update: "2025-10-14"
origin_note: "docs/patterns/inter-agent-communication-a2a.md"
languages: ["python"]
how_to_run: "Requires Google ADK and calendar API credentials. Run: python inter-agent-communication-a2a-adk-agent-creation.py"
related_patterns: ["docs/patterns/inter-agent-communication-a2a.md"]
---

## Context

This snippet demonstrates how to create A2A (Agent-to-Agent) compliant agents using Google ADK. The agent uses CalendarToolset to integrate with Google Calendar API, enabling calendar management capabilities through the A2A protocol. This pattern allows agents from different systems to communicate and collaborate using a standardized interface.

## Snippet

```python
import datetime
from google.adk.agents import LlmAgent
from google.adk.tools.google_api_tool import CalendarToolset

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

## Notes

Key implementation details:

- **CalendarToolset Integration**: Initializes OAuth-based calendar API tools
- **A2A Compliance**: Standard ADK agent structure compatible with A2A protocol
- **Dynamic Instruction**: Includes current date for context-aware calendar operations
- **Primary Calendar Default**: Assumes 'primary' calendar when not specified by user
- **RFC3339 Timestamps**: Explicitly instructs agent to use proper datetime format
- **Async Tool Loading**: Uses await to load calendar API tools asynchronously
