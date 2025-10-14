---
name: "Multi-Agent with ADK: Loop Agent"
objective: "Demonstrates how to use the ADK LoopAgent to repeatedly execute a set of sub-agents until a condition is met."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/multi-agent.md"
---

# Multi-Agent with ADK: Loop Agent

This snippet demonstrates the use of a `LoopAgent` in the Google ADK. The `LoopAgent` runs a sequence of sub-agents repeatedly until a condition is met, which is checked by a custom `ConditionChecker` agent.

## Code Example

```python
import asyncio
from typing import AsyncGenerator
from google.adk.agents import LoopAgent, LlmAgent, BaseAgent
from google.adk.events import Event, EventActions
from google.adk.agents.invocation_context import InvocationContext

# Best Practice: Define custom agents as complete, self-describing classes.
class ConditionChecker(BaseAgent):
    """A custom agent that checks for a 'completed' status in the session state."""
    name: str = "ConditionChecker"
    description: str = "Checks if a process is complete and signals the loop to stop."

    async def _run_async_impl(
        self,
        context: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """Checks state and yields an event to either continue or stop the loop."""
        status = context.session.state.get("status", "pending")
        is_done = (status == "completed")

        if is_done:
            # Escalate to terminate the loop when the condition is met.
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            # Yield a simple event to continue the loop.
            yield Event(author=self.name, content="Condition not met, continuing loop.")

# Correction: The LlmAgent must have a model and clear instructions.
process_step = LlmAgent(
    name="ProcessingStep",
    model="gemini-2.0-flash-exp",
    instruction="You are a step in a longer process. Perform your task. If you are the final step, update session state by setting 'status' to 'completed'."
)

# The LoopAgent orchestrates the workflow.
poller = LoopAgent(
    name="StatusPoller",
    max_iterations=10,
    sub_agents=[
        process_step,
        ConditionChecker() # Instantiating the well-defined custom agent.
    ]
)
```

## How It Works

1.  **ConditionChecker Agent**: A custom agent, `ConditionChecker`, is defined to check a `status` value in the session state. If the status is "completed", it yields an event with `actions=EventActions(escalate=True)`, which signals the parent `LoopAgent` to stop.
2.  **Processing Step Agent**: An `LlmAgent` named `process_step` represents the main work to be done in each loop iteration. It's instructed to update the session state to "completed" when its task is finished.
3.  **LoopAgent**: The `poller` is a `LoopAgent` that contains the `process_step` and `ConditionChecker` as sub-agents. It will execute them sequentially in a loop.
4.  **Loop Termination**: The loop will continue for a maximum of `max_iterations`. However, it will terminate early if the `ConditionChecker` escalates, which happens when the `process_step` agent has set the status to "completed".