---
name: "Multi-Agent with ADK: Agent as a Tool"
objective: "Demonstrates how to wrap one ADK agent as a tool to be used by another agent, creating a hierarchical multi-agent system."
how_to_run: "Requires Google ADK. Run as part of an ADK application."
from_note: "../patterns/multi-agent.md"
---

# Multi-Agent with ADK: Agent as a Tool

This snippet shows how to create a hierarchical agent structure in the Google ADK by wrapping a specialized agent (`image_generator_agent`) as a tool (`image_tool`) that can be used by another agent (`artist_agent`).

## Code Example

```python
from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from google.genai import types


# 1. A simple function tool for the core capability.
# This follows the best practice of separating actions from reasoning.
def generate_image(prompt: str) -> dict:
    """
    Generates an image based on a textual prompt.

    Args:
        prompt: A detailed description of the image to generate.

    Returns:
        A dictionary with the status and the generated image bytes.

    """
    print(f"TOOL: Generating image for prompt: '{prompt}'")
    # In a real implementation, this would call an image generation API.
    # For this example, we return mock image data.
    mock_image_bytes = b"mock_image_data_for_a_cat_wearing_a_hat"
    return {
        "status": "success",
        # The tool returns the raw bytes, the agent will handle the Part creation.
        "image_bytes": mock_image_bytes,
        "mime_type": "image/png"
    }


# 2. Refactor the ImageGeneratorAgent into an LlmAgent.
# It now correctly uses the input passed to it.
image_generator_agent = LlmAgent(
    name="ImageGen",
    model="gemini-2.0-flash",
    description="Generates an image based on a detailed text prompt.",
    instruction=(
        "You are an image generation specialist. Your task is to take the user's request "
        "and use the `generate_image` tool to create the image. "
        "The user's entire request should be used as the 'prompt' argument for the tool. "
        "After the tool returns the image bytes, you MUST output the image."
    ),
    tools=[generate_image]
)


# 3. Wrap the corrected agent in an AgentTool.
# The description here is what the parent agent sees.
image_tool = agent_tool.AgentTool(
    agent=image_generator_agent,
    description="Use this tool to generate an image. The input should be a descriptive prompt of the desired image."
)


# 4. The parent agent remains unchanged. Its logic was correct.
artist_agent = LlmAgent(
    name="Artist",
    model="gemini-2.0-flash",
    instruction=(
        "You are a creative artist. First, invent a creative and descriptive prompt for an image. "
        "Then, use the `ImageGen` tool to generate the image using your prompt."
    ),
    tools=[image_tool]
)
```

## How It Works

1.  **Core Function Tool**: A basic Python function `generate_image` is defined to perform the final action (image generation).
2.  **Specialized Agent**: An `LlmAgent` named `image_generator_agent` is created. Its sole purpose is to take a prompt and use the `generate_image` tool.
3.  **Agent as Tool**: The `image_generator_agent` is wrapped in an `agent_tool.AgentTool`. This makes the entire agent available as a single tool that other agents can call.
4.  **Parent Agent**: The `artist_agent` is a higher-level agent. It is given the `image_tool` and instructed to first create a prompt and then use the tool to generate the image. This demonstrates a clear separation of concerns and a hierarchical agent structure.