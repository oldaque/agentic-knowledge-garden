---
name: "Parallelization with ADK: Research and Synthesis"
objective: "Demonstrates a parallel research and synthesis pipeline using ADK's ParallelAgent and SequentialAgent."
how_to_run: "Requires Google ADK and google-search tool. Run as part of an ADK application."
from_note: "../patterns/parallelization.md"
---

# Parallelization with ADK: Research and Synthesis

This snippet demonstrates a common and powerful pattern: performing parallel research and then synthesizing the results. It uses a `ParallelAgent` to run multiple researchers concurrently and a `SequentialAgent` to orchestrate the overall workflow, feeding the parallel results into a final `SynthesisAgent`.

## Code Example

```python
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

GEMINI_MODEL="gemini-2.0-flash"

# --- 1. Define Researcher Sub-Agents (to run in parallel) ---
researcher_agent_1 = LlmAgent(
    name="RenewableEnergyResearcher",
    model=GEMINI_MODEL,
    instruction="Research 'renewable energy sources' and summarize findings.",
    tools=[google_search],
    output_key="renewable_energy_result"
)

researcher_agent_2 = LlmAgent(
    name="EVResearcher",
    model=GEMINI_MODEL,
    instruction="Research 'electric vehicle technology' and summarize findings.",
    tools=[google_search],
    output_key="ev_technology_result"
)

# --- 2. Create the ParallelAgent ---
parallel_research_agent = ParallelAgent(
    name="ParallelWebResearchAgent",
    sub_agents=[researcher_agent_1, researcher_agent_2]
)

# --- 3. Define the Merger Agent ---
merger_agent = LlmAgent(
    name="SynthesisAgent",
    model=GEMINI_MODEL,
    instruction="""Synthesize the following research summaries into a structured report.

    **Input Summaries:**
    *   **Renewable Energy:** {renewable_energy_result}
    *   **Electric Vehicles:** {ev_technology_result}
    """
)

# --- 4. Create the SequentialAgent (Orchestrates the flow) ---
sequential_pipeline_agent = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    sub_agents=[parallel_research_agent, merger_agent]
)

root_agent = sequential_pipeline_agent
```

## How It Works

1.  **Researcher Agents**: Two `LlmAgent` instances are created to research different topics. Each is equipped with the `google_search` tool and has a unique `output_key` to store its findings in the session state.
2.  **Parallel Execution**: A `ParallelAgent` is created to run the two researcher agents concurrently. This significantly speeds up the data gathering phase.
3.  **Synthesis Agent**: A `merger_agent` is defined. Its instruction is a prompt template that explicitly references the `output_key`s from the parallel researchers. This allows it to access and synthesize their results.
4.  **Sequential Orchestration**: A `SequentialAgent` orchestrates the entire process. It first runs the `parallel_research_agent`. Once the parallel research is complete and the results are in the session state, it runs the `merger_agent`, which then has the data it needs to create the final report.