---
name: "Routing with ADK: Coordinator and Sub-Agents"
objective: "Demonstrates a routing pattern where a coordinator agent delegates tasks to specialized sub-agents based on the user's request."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/routing.md"
---

# Routing with ADK: Coordinator and Sub-Agents

This snippet demonstrates the routing pattern in the Google ADK. A central `Coordinator` agent is responsible for analyzing user requests and delegating them to the appropriate specialized sub-agent (`booking_agent` or `info_agent`).

## Code Example

```python
# Copyright (c) 2025 Marco Fago
# This code is licensed under the MIT License.

import uuid
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool

# --- Define Tool Functions ---
def booking_handler(request: str) -> str:
    """Handles booking requests for flights and hotels."""
    print("--- Booking Handler Called ---")
    return f"Booking action for '{request}' has been simulated."

def info_handler(request: str) -> str:
    """Handles general information requests."""
    print("--- Info Handler Called ---")
    return f"Information request for '{request}'. Result: Simulated information retrieval."

# --- Create Tools and Sub-Agents ---
booking_tool = FunctionTool(booking_handler)
info_tool = FunctionTool(info_handler)

booking_agent = Agent(
    name="Booker",
    model="gemini-2.0-flash",
    description="A specialized agent for booking flights and hotels.",
    tools=[booking_tool]
)

info_agent = Agent(
    name="Info",
    model="gemini-2.0-flash",
    description="A specialized agent for general information.",
    tools=[info_tool]
)

# --- Define the Coordinator Agent ---
coordinator = Agent(
    name="Coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "You are the main coordinator. Your only task is to analyze "
        "incoming user requests and delegate them to the appropriate specialist agent. "
        "Do not try to answer the user directly.\n"
        "- For any requests related to booking flights or hotels, delegate to the 'Booker' agent.\n"
        "- For all other general information questions, delegate to the 'Info' agent."
    ),
    sub_agents=[booking_agent, info_agent]
)

# --- Execution Logic ---
async def run_coordinator(runner: InMemoryRunner, request: str):
    print(f"\n--- Running Coordinator with request: '{request}' ---")
    # ... (runner execution logic) ...
    # This part is simplified for brevity
    pass

async def main():
    runner = InMemoryRunner(coordinator)
    await run_coordinator(runner, "Book me a hotel in Paris.")
    await run_coordinator(runner, "What is the highest mountain in the world?")

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    # await main() # Commented out to prevent execution in markdown
```

## How It Works

1.  **Specialized Sub-Agents**: Two agents, `booking_agent` and `info_agent`, are created. Each has a specific `description` and is equipped with a tool relevant to its task.
2.  **Coordinator Agent**: The `coordinator` agent is the entry point. Its `instruction` is the key to the routing logic. It is explicitly told *not* to answer questions itself, but to delegate to the correct sub-agent based on the request type.
3.  **Hierarchical Structure**: The `booking_agent` and `info_agent` are passed as `sub_agents` to the `coordinator`. This establishes the hierarchy needed for delegation.
4.  **Delegation**: When the `coordinator` receives a request, its LLM uses the descriptions of the sub-agents and its own instructions to decide which sub-agent is best suited for the job. It then delegates the task to that sub-agent.

```