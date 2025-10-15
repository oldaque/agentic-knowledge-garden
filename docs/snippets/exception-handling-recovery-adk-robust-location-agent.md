---
title: "Exception Handling - ADK Robust Location Agent"
slug: "exception-handling-recovery-adk-robust-location-agent"
summary: "Demonstrates robust exception handling in ADK agents using SequentialAgent with multiple sub-agents that include fallback mechanisms for location retrieval."
tags: ["google-adk", "exception-handling", "fallback", "sequential-agent", "error-recovery"]
status: "stable"
last_update: "2025-10-14"
origin_note: "docs/patterns/exception-handling-recovery.md"
languages: ["python"]
how_to_run: "Requires Google ADK. Run: python exception-handling-recovery-adk-robust-location-agent.py"
related_patterns: ["docs/patterns/exception-handling-recovery.md"]
---

## Context

This snippet demonstrates the Exception Handling and Recovery pattern using Google ADK's SequentialAgent. It implements a robust error handling strategy with multiple sub-agents that work together: a primary agent attempts precise location lookup, a fallback agent handles errors gracefully by providing alternative lookups, and a response agent presents the final result. The pattern uses state management to track failures and coordinate the fallback logic.

## Snippet

```python
from google.adk.agents import Agent, SequentialAgent

# Agent 1: Tries the primary tool. Its focus is narrow and clear.
primary_handler = Agent(
    name="primary_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
Your job is to get precise location information.
Use the get_precise_location_info tool with the user's provided address.
    """,
    tools=[get_precise_location_info]
)

# Agent 2: Acts as the fallback handler, checking state to decide its action.
fallback_handler = Agent(
    name="fallback_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
Check if the primary location lookup failed by looking at state["primary_location_failed"].
- If it is True, extract the city from the user's original query and use the get_general_area_info tool.
- If it is False, do nothing.
    """,
    tools=[get_general_area_info]
)

# Agent 3: Presents the final result from the state.
response_agent = Agent(
    name="response_agent",
    model="gemini-2.0-flash-exp",
    instruction="""
Review the location information stored in state["location_result"].
Present this information clearly and concisely to the user.
If state["location_result"] does not exist or is empty, apologize that you could not retrieve the location.
    """,
    tools=[] # This agent only reasons over the final state.
)

# The SequentialAgent ensures the handlers run in a guaranteed order.
robust_location_agent = SequentialAgent(
    name="robust_location_agent",
    sub_agents=[primary_handler, fallback_handler, response_agent]
)
```

## Notes

Key implementation details:

- **Primary Handler**: Attempts precise location lookup first with specialized tool
- **Fallback Handler**: Checks state for failure flag and provides alternative lookup if needed
- **Response Agent**: Presents final results with appropriate error messages when necessary
- **State Management**: Uses session state to track failures and coordinate between agents
- **Sequential Orchestration**: SequentialAgent guarantees execution order for proper error handling flow
- **Graceful Degradation**: System provides increasingly general information rather than complete failure
