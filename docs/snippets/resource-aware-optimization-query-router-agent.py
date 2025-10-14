---
name: "ADK Query Router Agent"
objective: "Illustrates a conceptual ADK QueryRouterAgent that routes queries based on complexity to different LLM agents (Gemini Pro or Flash)."
how_to_run: "This is a conceptual code block demonstrating agent routing logic within the Google ADK framework. It is not directly runnable as a standalone script without a full ADK environment setup and the 'gemini_pro_agent' and 'gemini_flash_agent' instances."
from_note: "../patterns/resource-aware-optimization.md"
---
from google.adk.agents import Agent, BaseAgent
from google.adk.events import Event
from google.adk.agents.invocation_context import InvocationContext
import asyncio

class QueryRouterAgent(BaseAgent):
    name: str = "QueryRouter"
    description: str = "Routes user queries to the appropriate LLM agent based on complexity."

    async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
        user_query = context.current_message.text # Assuming text input
        query_length = len(user_query.split()) # Simple metric: number of words

        if query_length < 20: # Example threshold for simplicity vs. complexity
            print(f"Routing to Gemini Flash Agent for short query (length: {query_length})")
            # In a real ADK setup, you would 'transfer_to_agent' or directly invoke
            # For demonstration, we'll simulate a call and yield its response
            response = await gemini_flash_agent.run_async(context.current_message)
            yield Event(author=self.name, content=f"Flash Agent processed: {response}")
        else:
            print(f"Routing to Gemini Pro Agent for long query (length: {query_length})")
            response = await gemini_pro_agent.run_async(context.current_message)
            yield Event(author=self.name, content=f"Pro Agent processed: {response}")