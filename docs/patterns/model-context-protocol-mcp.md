---
title: "Chapter 10: Model Context Protocol (MCP)"
slug: "model-context-protocol-mcp"
tags: ["mcp", "protocol", "model-context", "agentic-pattern", "anthropic"]
source:
  type: "book"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1e6XimYczKmhX9zpqEyxLFWPQgGuG0brp7Hic2sFl_qw/edit?usp=sharing"
status: "stable"
last_update: "2025-10-13"
summary: "Pattern for enabling secure communication and data sharing between AI models and external tools through standardized protocols."
source: "https://docs.google.com/document/d/1e6XimYczKmhX9zpqEyxLFWPQgGuG0brp7Hic2sFl_qw/edit?usp=sharing"
---

# The Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard designed to standardize how Large Language Models (LLMs) communicate with external applications, data sources, and tools. It acts as a universal adapter, enabling LLMs to access current data, utilize external software, and execute specific operational tasks.

**Key Aspects of MCP:**
*   **Client-Server Architecture:** MCP operates on a client-server model where MCP servers expose data (resources), interactive templates (prompts), and actionable functions (tools) to MCP clients (LLM host applications or AI agents).
*   **Standardization:** Unlike proprietary tool function calling, MCP provides a standardized interface, promoting interoperability, composability, and reusability across different LLMs and tools.
*   **Dynamic Discovery:** MCP clients can dynamically query a server to discover available tools and resources, allowing agents to adapt to new capabilities without redeployment.
*   **Components:** It distinguishes between:
    *   **Resources:** Static data (e.g., PDF files, database records).
    *   **Tools:** Executable functions that perform actions (e.g., sending emails, querying APIs).
    *   **Prompts:** Templates guiding the LLM's interaction with resources or tools.
*   **Transportation Mechanisms:** Uses JSON-RPC over STDIO for local interactions and web-friendly protocols like Streamable HTTP and Server-Sent Events (SSE) for remote connections.

**MCP vs. Tool Function Calling:**
*   **Tool Function Calling:** A direct, proprietary, and vendor-specific request from an LLM to a predefined tool, often tightly coupled with the specific application and LLM.
*   **MCP:** An open, standardized protocol that enables dynamic discovery and communication with a wide range of external capabilities, fostering an ecosystem of reusable components.

**Practical Applications:**
MCP significantly broadens LLM capabilities, enabling:
*   Database integration (e.g., querying Google BigQuery).
*   Generative media orchestration (e.g., integrating with Imagen, Veo).
*   External API interaction (e.g., fetching weather data, sending emails).
*   Reasoning-based information extraction.
*   Custom tool development and exposure.
*   Complex workflow orchestration.
*   IoT device control.
*   Financial services automation.

**Integration with ADK and FastMCP:**
*   **ADK (Agent Development Kit):** Supports connecting ADK agents to MCP servers using `MCPToolset` and `StdioServerParameters` (for local servers) or `HttpServerParameters` (for remote servers).
*   **FastMCP:** A Python framework that simplifies the development of MCP servers, automatically generating schema from Python function signatures, type hints, and docstrings, making it easy to expose Python functions as MCP tools.

_Code examples for this chapter are available in the Google Drive folder: [https://drive.google.com/drive/u/0/folders/1Y3U3IrYCiJ3E45Z8okR5eCg7OPnWQtPV](https://drive.google.com/drive/u/0/folders/1Y3U3IrYCiJ3E45Z8okR5eCg7OPnWQtPV)_
