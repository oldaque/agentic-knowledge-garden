---
name: "Vertex AI Guardrail Example"
objective: "Demonstrates a tool argument validation callback for an ADK agent using Vertex AI, ensuring secure tool execution based on user ID matching."
how_to_run: "This is a conceptual code block demonstrating an ADK agent with a `before_tool_callback`. It requires a full ADK environment setup and a defined list of tools. It is not directly runnable as a standalone script."
from_note: "../patterns/guardrails-safety-patterns.md"
---
from google.adk.agents import Agent # Correct import
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from typing import Optional, Dict, Any

def validate_tool_params(
    tool: BaseTool,
    args: Dict[str, Any],
    tool_context: ToolContext # Correct signature, removed CallbackContext
) -> Optional[Dict]:
    """
    Validates tool arguments before execution. For example, checks if the user ID in the arguments
    matches the one in the session state.
    """
    print(f"Callback triggered for tool: {tool.name}, args: {args}")
    # Access state correctly through tool_context
    expected_user_id = tool_context.state.get("session_user_id")
    actual_user_id_in_args = args.get("user_id_param")

    if actual_user_id_in_args and actual_user_id_in_args != expected_user_id:
        print(f"Validation Failed: User ID mismatch for tool '{tool.name}'.")
        # Block tool execution by returning a dictionary
        return {
            "status": "error",
            "error_message": f"Tool call blocked: User ID validation failed for security reasons."
        }
    # Allow tool execution to proceed
    print(f"Callback validation passed for tool '{tool.name}'.")
    return None

# Agent setup using the documented class
root_agent = Agent( # Use the documented Agent class
    model='gemini-2.0-flash-exp', # Using a model name from the guide
    name='root_agent',
    instruction="You are a root agent that validates tool calls.",
    before_tool_callback=validate_tool_params, # Assign the corrected callback
    tools = [ # ... list of tool functions or Tool instances ... ]
)
