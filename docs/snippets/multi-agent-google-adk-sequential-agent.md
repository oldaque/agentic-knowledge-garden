---
name: "Multi-Agent with ADK: Sequential Agent"
objective: "Demonstrates how to use the ADK SequentialAgent to run multiple sub-agents in a predefined order."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/multi-agent.md"
---

# Multi-Agent with ADK: Sequential Agent

This snippet shows how to use the `SequentialAgent` in the Google ADK to create a pipeline of agents that execute in a specific order. The output of one agent can be used as the input for the next.

## Code Example

```python
from google.adk.agents import SequentialAgent, Agent


# This agent's output will be saved to session.state["data"]
step1 = Agent(name="Step1_Fetch", output_key="data")


# This agent will use the data from the previous step.
# We instruct it on how to find and use this data.
step2 = Agent(
    name="Step2_Process",
    instruction="Analyze the information found in state['data'] and provide a summary."
)


pipeline = SequentialAgent(
    name="MyPipeline",
    sub_agents=[step1, step2]
)


# When the pipeline is run with an initial input, Step1 will execute,
# its response will be stored in session.state["data"], and then
# Step2 will execute, using the information from the state as instructed.
```

## How It Works

1.  **Step 1 Agent**: The first agent, `step1`, is defined with an `output_key="data"`. This means that whatever this agent outputs will be saved to `session.state["data"]`.
2.  **Step 2 Agent**: The second agent, `step2`, is instructed to use the information from `state['data']`. This creates a dependency on the output of the first agent.
3.  **SequentialAgent**: A `SequentialAgent` named `pipeline` is created with `step1` and `step2` as its sub-agents. The order in the list defines the execution order.
4.  **Execution Flow**: When the `pipeline` is run, it will first execute `step1`. Its output is stored in the session state. Then, `step2` is executed, and because of its instructions, it will access the output of `step1` from the session state to perform its task.