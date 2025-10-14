---
name: "ADK Agents for Resource-Aware Optimization"
objective: "Demonstrates defining ADK agents with different models (Gemini Pro and Flash) for resource-aware optimization."
how_to_run: "This is a conceptual code block demonstrating agent definition within the Google ADK framework. It is not directly runnable as a standalone script without a full ADK environment setup."
from_note: "../patterns/resource-aware-optimization.md"
---
from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLlm # If using models not directly supported by ADK's default Agent

# Agent using the more expensive Gemini Pro 2.5
gemini_pro_agent = Agent(
    name="GeminiProAgent",
    model="gemini-2.5-pro", # Placeholder for actual model name if different
    description="A highly capable agent for complex queries.",
    instruction="You are an expert assistant for complex problem-solving."
)

# Agent using the less expensive Gemini Flash 2.5
gemini_flash_agent = Agent(
    name="GeminiFlashAgent",
    model="gemini-2.5-flash", # Placeholder for actual model name if different
    description="A fast and efficient agent for simple queries.",
    instruction="You are a quick assistant for straightforward questions."
)