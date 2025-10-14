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
