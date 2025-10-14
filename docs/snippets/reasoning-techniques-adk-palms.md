---
name: "ADK PALMs Example"
objective: "Demonstrates the use of external tools within Google's ADK for generating code, illustrating Program-Aided Language Models (PALMs)."
how_to_run: "This is a conceptual code block demonstrating agent definition within the Google ADK framework. It is not directly runnable as a standalone script without a full ADK environment setup."
from_note: "../patterns/reasoning-techniques.md"
---

## Explanation

This code demonstrates the **Program-Aided Language Models (PALMs)** reasoning technique using Google's ADK. PALMs enhance LLM capabilities by allowing them to generate and execute code for tasks requiring precise computation, data manipulation, or logical operations that are difficult to perform through natural language alone.

The implementation creates a hierarchical agent structure with three components:

1. **SearchAgent**: Specializes in web search using Google Search tool, enabling the agent to retrieve up-to-date information from the internet.

2. **CodeAgent**: Specializes in code generation and execution using the BuiltInCodeExecutor, allowing the agent to write Python code, execute it in a sandboxed environment, and return results.

3. **RootAgent**: Orchestrates the specialized agents by exposing them as tools via `AgentTool`. This coordinator pattern allows the root agent to route tasks to the appropriate specialist.

The PALMs pattern is particularly powerful for:
- Complex mathematical calculations
- Data analysis and transformation
- Algorithm implementation
- Iterative problem-solving requiring both reasoning and computation
- Tasks where natural language explanations need to be backed by executable code

By separating search capabilities from code execution, the system achieves modularity and allows each agent to focus on its specialized domain while the root agent handles task decomposition and coordination.

## Code

```python
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
```
