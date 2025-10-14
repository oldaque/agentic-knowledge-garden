---
name: "Tool Use with LangChain: Search Information"
objective: "Demonstrates how to create a tool-calling agent with LangChain, including defining a custom tool and using an AgentExecutor."
how_to_run: "Requires LangChain and a Google API key. Run with `python your_script_name.py`."
from_note: "../patterns/tool-use.md"
---

# Tool Use with LangChain: Search Information

This snippet demonstrates how to build a tool-calling agent using LangChain. It defines a custom `search_information` tool and uses `create_tool_calling_agent` and `AgentExecutor` to create an agent that can decide when to use the tool to answer questions.

## Code Example

```python
import os, getpass
import asyncio
import nest_asyncio
from typing import List
from dotenv import load_dotenv
import logging

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool as langchain_tool
from langchain.agents import create_tool_calling_agent, AgentExecutor

# UNCOMMENT
# Prompt the user securely and set API keys as an environment variables
# os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")
# os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

try:
    # A model with function/tool calling capabilities is required.
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    print(f"✅ Language model initialized: {llm.model}")
except Exception as e:
    print(f"🛑 Error initializing language model: {e}")
    llm = None

# --- Define a Tool ---
@langchain_tool
def search_information(query: str) -> str:
    """
    Provides factual information on a given topic. Use this tool to find answers to phrases
    like 'capital of France' or 'weather in London?'.
    """
    print(f"\n--- 🛠️ Tool Called: search_information with query: '{query}' ---")
    # Simulate a search tool with a dictionary of predefined results.
    simulated_results = {
        "weather in london": "The weather in London is currently cloudy with a temperature of 15°C.",
        "capital of france": "The capital of France is Paris.",
        "population of earth": "The estimated population of Earth is around 8 billion people.",
        "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
        "default": f"Simulated search result for '{query}': No specific information found, but the topic seems interesting."
    }
    result = simulated_results.get(query.lower(), simulated_results["default"])
    print(f"--- TOOL RESULT: {result} ---")
    return result

tools = [search_information]

# --- Create a Tool-Calling Agent ---
if llm:
    # This prompt template requires an `agent_scratchpad` placeholder for the agent's internal steps.
    agent_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    # Create the agent, binding the LLM, tools, and prompt together.
    agent = create_tool_calling_agent(llm, tools, agent_prompt)

    # AgentExecutor is the runtime that invokes the agent and executes the chosen tools.
    # The 'tools' argument is not needed here as they are already bound to the agent.
    agent_executor = AgentExecutor(agent=agent, verbose=True, tools=tools)

async def run_agent_with_tool(query: str):
    """Invokes the agent executor with a query and prints the final response."""
    print(f"\n--- 🏃 Running Agent with Query: '{query}' ---")
    try:
        response = await agent_executor.ainvoke({"input": query})
        print("\n--- ✅ Final Agent Response ---")
        print(response["output"])
    except Exception as e:
        print(f"\n🛑 An error occurred during agent execution: {e}")

async def main():
    """Runs all agent queries concurrently."""
    tasks = [
        run_agent_with_tool("What is the capital of France?"),
        run_agent_with_tool("What's the weather like in London?"),
        run_agent_with_tool("Tell me something about dogs.") # Should trigger the default tool response
    ]
    await asyncio.gather(*tasks)

nest_asyncio.apply()
asyncio.run(main())
```

## How It Works

1.  **Tool Definition**: The `@langchain_tool` decorator is used to easily define a Python function as a LangChain tool. The function's docstring serves as the description for the tool, which the agent uses to decide when to call it.
2.  **Agent Creation**: `create_tool_calling_agent` is a high-level function that binds the LLM to the provided tools and a prompt. The prompt must include a placeholder for `{agent_scratchpad}`, which is where the agent's intermediate steps are managed.
3.  **AgentExecutor**: The `AgentExecutor` is the runtime environment for the agent. It takes the agent and the list of tools, and it's responsible for invoking the agent, parsing its output, executing the chosen tool, and passing the tool's output back to the agent to formulate a final response.
4.  **Asynchronous Invocation**: The example uses `ainvoke` to run the agent asynchronously, which is efficient for I/O-bound tasks like making API calls to an LLM.

```