---
name: "Multi-Agent with ADK: Hierarchical Structure"
objective: "Demonstrates how to create a hierarchical agent structure in ADK by assigning sub-agents to a parent agent."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/multi-agent.md"
---

# Multi-Agent with ADK: Hierarchical Structure

This snippet demonstrates how to create a hierarchical multi-agent system in the Google ADK. A `Coordinator` agent is set up to delegate tasks to its `sub_agents`, a `Greeter` and a `TaskExecutor`.

## Code Example

```python
from google.adk.agents import LlmAgent, BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator


# Correctly implement a custom agent by extending BaseAgent
class TaskExecutor(BaseAgent):
    """A specialized agent with custom, non-LLM behavior."""
    name: str = "TaskExecutor"
    description: str = "Executes a predefined task."

    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        """Custom implementation logic for the task."""
        # This is where your custom logic would go.
        # For this example, we'll just yield a simple event.
        yield Event(author=self.name, content="Task finished successfully.")


# Define individual agents with proper initialization
# LlmAgent requires a model to be specified.
greeter = LlmAgent(
    name="Greeter",
    model="gemini-2.0-flash-exp",
    instruction="You are a friendly greeter."
)
task_doer = TaskExecutor() # Instantiate our concrete custom agent

# Create a parent agent and assign its sub-agents
# The parent agent's description and instructions should guide its delegation logic.
coordinator = LlmAgent(
    name="Coordinator",
    model="gemini-2.0-flash-exp",
    description="A coordinator that can greet users and execute tasks.",
    instruction="When asked to greet, delegate to the Greeter. When asked to perform a task, delegate to the TaskExecutor.",
    sub_agents=[
        greeter,
        task_doer
    ]
)

# The ADK framework automatically establishes the parent-child relationships.
# These assertions will pass if checked after initialization.
assert greeter.parent_agent == coordinator
assert task_doer.parent_agent == coordinator

print("Agent hierarchy created successfully.")
```

## How It Works

1.  **Custom Agent**: A `TaskExecutor` agent is defined by inheriting from `BaseAgent`. This allows for custom, non-LLM-based logic to be implemented in the `_run_async_impl` method.
2.  **Sub-Agents**: A standard `LlmAgent` (`greeter`) and an instance of our custom `TaskExecutor` (`task_doer`) are created.
3.  **Parent Agent**: A `Coordinator` agent is created. The `greeter` and `task_doer` are passed to its `sub_agents` parameter.
4.  **Hierarchy**: The ADK framework automatically sets the `parent_agent` attribute on the sub-agents, establishing the hierarchical relationship. The `Coordinator` can now delegate tasks to its sub-agents based on its instructions.