---
name: "Exception Handling - ADK Robust Location Agent"
objective: "Demonstrates robust exception handling in ADK agents with fallback mechanisms for location retrieval."
how_to_run: "Requires Google ADK. Run: python exception-handling-recovery-adk-robust-location-agent.py"
from_note: "../patterns/exception-handling-recovery.md"
---

# Exception Handling with Fallback Agents in Google ADK

This example demonstrates robust exception handling using a SequentialAgent with multiple sub-agents that include fallback mechanisms. The primary agent attempts precise location lookup, with a fallback agent that handles errors gracefully.

## Code Example

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

## How It Works

1. **Primary Handler**: Attempts to get precise location information using a specific tool
2. **Fallback Handler**: Checks if the primary lookup failed and provides alternative location lookup if needed
3. **Response Agent**: Presents the final location information to the user, with error handling for cases where location couldn't be retrieved

This pattern ensures the agent can handle tool failures gracefully and still provide useful responses.
