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
