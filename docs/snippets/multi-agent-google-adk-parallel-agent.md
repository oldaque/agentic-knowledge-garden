---
name: "Multi-Agent with ADK: Parallel Agent"
objective: "Demonstrates how to use the ADK ParallelAgent to run multiple sub-agents concurrently."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/multi-agent.md"
---

# Multi-Agent with ADK: Parallel Agent

This snippet shows how to use the `ParallelAgent` in the Google ADK to execute multiple agents simultaneously. This is useful for tasks that can be broken down into independent sub-tasks, such as fetching different types of data at the same time.

## Code Example

```python
from google.adk.agents import Agent, ParallelAgent


# It's better to define the fetching logic as tools for the agents
# For simplicity in this example, we'll embed the logic in the agent's instruction.
# In a real-world scenario, you would use tools.


# Define the individual agents that will run in parallel
weather_fetcher = Agent(
    name="weather_fetcher",
    model="gemini-2.0-flash-exp",
    instruction="Fetch the weather for the given location and return only the weather report.",
    output_key="weather_data" # The result will be stored in session.state["weather_data"]
)


news_fetcher = Agent(
    name="news_fetcher",
    model="gemini-2.0-flash-exp",
    instruction="Fetch the top news story for the given topic and return only that story.",
    output_key="news_data" # The result will be stored in session.state["news_data"]
)


# Create the ParallelAgent to orchestrate the sub-agents
data_gatherer = ParallelAgent(
    name="data_gatherer",
    sub_agents=[
        weather_fetcher,
        news_fetcher
    ]
)
```

## How It Works

1.  **Sub-Agents**: Two individual `Agent` instances, `weather_fetcher` and `news_fetcher`, are defined. Each has a specific instruction and an `output_key`. The `output_key` specifies where the agent's final result will be stored in the session state.
2.  **ParallelAgent**: A `ParallelAgent` named `data_gatherer` is created, and the `weather_fetcher` and `news_fetcher` are passed to its `sub_agents` list.
3.  **Concurrent Execution**: When the `data_gatherer` agent is run, it will execute both `weather_fetcher` and `news_fetcher` concurrently.
4.  **Results**: The results of each sub-agent will be collected and stored in the session state under their respective `output_key`s (`weather_data` and `news_data`).