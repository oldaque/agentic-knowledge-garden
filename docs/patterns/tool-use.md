---
title: "Chapter 5: Tool Use"
slug: "tool-use"
tags: ["tool-use", "function-calling", "functionality", "agentic-pattern", "langchain", "google-adk"]
source:
  type: "book"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1bE4iMljhppqGY1p48gQWtZvk6MfRuJRCiba1yRykGNE/edit?usp=sharing"
status: "stable"
last_update: "2025-10-13"
summary: "Pattern for enabling agents to interact with external APIs, services and tools to extend their capabilities beyond training data."
---

# Chapter 5: Tool Use (Function Calling)

## TOOL USE PATTERN OVERVIEW

The Tool Use pattern, often implemented through a mechanism called Function Calling, enables an agent to interact with external APIs, databases, services, or even execute code. It allows the LLM at the core of the agent to decide when and how to use a specific external function based on the user's request or the current state of the task.

**The process typically involves:**
1.  **Tool Definition:** External functions are described to the LLM.
2.  **LLM Decision:** The LLM decides if calling one or more tools is necessary.
3.  **Function Call Generation:** The LLM generates a structured output (e.g., JSON) for the tool call.
4.  **Tool Execution:** The agentic framework executes the actual external function.
5.  **Observation/Result:** The tool's output is returned to the agent.
6.  **LLM Processing:** The LLM uses the tool's output as context to formulate a final response or decide on the next step.

This pattern is fundamental because it breaks the limitations of the LLM's training data and allows it to access up-to-date information, perform calculations, interact with user-specific data, or trigger real-world actions.

While "function calling" describes invoking specific code functions, "tool calling" is a broader term that includes complex API endpoints, database requests, or instructions to other specialized agents.

Frameworks like LangChain, LangGraph, and Google Agent Developer Kit (ADK) provide robust support for defining tools and integrating them into agent workflows.


## PRACTICAL APPLICATIONS & USE CASES

-   **Information Retrieval from External Sources:** Accessing real-time data (e.g., weather, stock prices).
-   **Interacting with Databases and APIs:** Performing queries, updates, or operations on structured data (e.g., e-commerce inventory).
-   **Performing Calculations and Data Analysis:** Using external calculators or data analysis libraries (e.g., financial analysis).
-   **Sending Communications:** Sending emails, messages, or making API calls to external communication services.
-   **Executing Code:** Running code snippets in a safe environment to perform specific tasks.
-   **Controlling Other Systems or Devices:** Interacting with smart home devices or IoT platforms.

## HANDS-ON CODE EXAMPLE (LANGCHAIN)

This example demonstrates a tool-calling agent using LangChain and the Google Gemini model, with a simulated `search_information` tool.

[Code Example: LangChain Tool-Calling Agent](../snippets/tool-use-langchain-search-information.md)

## HANDS-ON CODE EXAMPLE (CREWAI)

This example shows how to implement function calling (Tools) within the CrewAI framework to fetch a simulated stock price.

[Code Example: CrewAI Stock Price Lookup Tool](../snippets/tool-use-crewai-stock-price-lookup.md)

## HANDS-ON CODE EXAMPLE (GOOGLE ADK)

This section demonstrates two examples using Google ADK: one for Google Search and another for Code Execution.

### Google Search Tool

[Code Example: Google ADK Google Search Tool](../snippets/tool-use-google-adk-google-search.md)

### Code Execution Tool

[Code Example: Google ADK Code Execution Tool](../snippets/tool-use-google-adk-code-execution.md)

## AT A GLANCE

**What:** LLMs are limited by their static training data and inability to perform actions or retrieve real-time information.

**Why:** The Tool Use pattern (function calling) provides a standardized solution by describing external functions to the LLM. The LLM decides when to use a tool, generates a structured call, and an orchestration layer executes it, feeding the result back to the LLM.

**Rule of thumb:** Use the Tool Use pattern whenever an agent needs to break out of the LLM's internal knowledge and interact with the outside world (real-time data, private info, calculations, code execution, external actions).

## VISUAL SUMMARY


## KEY TAKEAWAYS

*   Tool Use (Function Calling) allows agents to interact with external systems and access dynamic information.
*   It involves defining tools with clear descriptions and parameters that the LLM can understand.
*   The LLM decides when to use a tool and generates structured function calls.
*   Agentic frameworks execute the actual tool calls and return the results to the LLM.
*   Tool Use is essential for building agents that can perform real-world actions and provide up-to-date information.
*   LangChain simplifies tool definition using the `@tool` decorator and provides `create_tool_calling_agent` and `AgentExecutor`.
*   Google ADK has useful pre-built tools like Google Search, Code Execution, and Vertex AI Search Tool.

## CONCLUSION

The Tool Use pattern is a critical architectural principle for extending the functional scope of large language models beyond their intrinsic text generation capabilities. By equipping a model with the ability to interface with external software and data sources, this paradigm allows an agent to perform actions, execute computations, and retrieve information from other systems. Frameworks such as LangChain, Google ADK, and Crew AI offer structured abstractions and components that facilitate the integration of these external tools.

## REFERENCES

1.  [LangChain Documentation (Tools)](https://python.langchain.com/docs/integrations/tools/)
2.  [Google Agent Developer Kit (ADK) Documentation (Tools)](https://google.github.io/adk-docs/tools/)
3.  [OpenAI Function Calling Documentation](https://platform.openai.com/docs/guides/function-calling)
4.  [CrewAI Documentation (Tools)](https://docs.crewai.com/concepts/tools)
