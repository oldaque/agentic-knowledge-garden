---
name: "ADK PALMs Example"
objective: "Demonstrates the use of external tools within Google's ADK for generating code, illustrating Program-Aided Language Models (PALMs)."
how_to_run: "This is a conceptual code block demonstrating agent definition within the Google ADK framework. It is not directly runnable as a standalone script without a full ADK environment setup."
from_note: "../patterns/reasoning-techniques.md"
---
from google.adk.tools import agent_tool
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor

search_agent = Agent(
    model='gemini-2.0-flash',
    name='SearchAgent',
    instruction="""
You're a specialist in Google Search
""",
    tools=[google_search],
)

coding_agent = Agent(
    model='gemini-2.0-flash',
    name='CodeAgent',
    instruction="""
You're a specialist in Code Execution
""",
    code_executor=[BuiltInCodeExecutor],
)

root_agent = Agent(
    name="RootAgent",
    model="gemini-2.0-flash",
    description="Root Agent",
    tools=[agent_tool.AgentTool(agent=search_agent), agent_tool.AgentTool(agent=coding_agent)],
)
