---
title: "Inter-Agent Communication - ADK Server Setup"
slug: "inter-agent-communication-a2a-adk-server-setup"
summary: "Demonstrates setting up an A2A server using Google ADK for agent-to-agent communication with OAuth authentication support."
tags: ["google-adk", "a2a", "server-setup", "starlette", "uvicorn", "oauth"]
status: "stable"
last_update: "2025-10-14"
origin_note: "docs/patterns/inter-agent-communication-a2a.md"
languages: ["python"]
how_to_run: "Requires Google ADK and appropriate credentials. Run: python inter-agent-communication-a2a-adk-server-setup.py"
related_patterns: ["docs/patterns/inter-agent-communication-a2a.md"]
---

## Context

This snippet demonstrates setting up a complete A2A (Agent-to-Agent) server using Google ADK. It creates an HTTP server that exposes ADK agents through the A2A protocol, enabling other agents to discover capabilities and communicate via standardized endpoints. The setup includes agent card definition, OAuth authentication handling, and Starlette web framework integration.

## Snippet

```python
import os
import asyncio
from typing import List, Dict, Any, TypedDict
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.requests import Request
import uvicorn

from google.adk.a2a.agent_card import AgentCard, AgentCapabilities, AgentSkill
from google.adk.a2a.runner import Runner
from google.adk.a2a.server import DefaultRequestHandler, A2AStarletteApplication
from google.adk.a2a.server.executors import ADKAgentExecutor
from google.adk.a2a.server.services import InMemoryArtifactService, InMemorySessionService, InMemoryMemoryService

# Assuming create_agent is defined elsewhere or imported
# from .adk_agent import create_agent # This would be the actual import

def main(host: str, port: int):
    # Verify an API key is set.
    # Not required if using Vertex AI APIs.
    if os.getenv('GOOGLE_GENAI_USE_VERTEXAI') != 'TRUE' and not os.getenv(
            'GOOGLE_API_KEY' ):
        raise ValueError(
            'GOOGLE_API_KEY environment variable not set and '
            'GOOGLE_GENAI_USE_VERTEXAI is not TRUE.'
        )

    skill = AgentSkill(
        id='check_availability',
        name='Check Availability',
        description="Checks a user's availability for a time using their Google Calendar",
        tags=['calendar'],
        examples=['Am I free from 10am to 11am tomorrow?'],
    )

    agent_card = AgentCard(
        name='Calendar Agent',
        description="An agent that can manage a user's calendar",
        url=f'http://{host}:{port}/',
        version='1.0.0',
        defaultInputModes=['text'],
        defaultOutputModes=['text'],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill],
    )

    adk_agent = asyncio.run(create_agent(
        client_id=os.getenv('GOOGLE_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    ))

    runner = Runner(
        app_name=agent_card.name,
        agent=adk_agent,
        artifact_service=InMemoryArtifactService(),
        session_service=InMemorySessionService(),
        memory_service=InMemoryMemoryService(),
    )

    agent_executor = ADKAgentExecutor(runner, agent_card)

    async def handle_auth(request: Request) -> PlainTextResponse:
        await agent_executor.on_auth_callback(
            str(request.query_params.get('state')),
            str(request.url)
        )
        return PlainTextResponse('Authentication successful.')

    request_handler = DefaultRequestHandler(
        agent_executor=agent_executor,
        task_store=InMemoryTaskStore()
    )

    a2a_app = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler
    )

    routes = a2a_app.routes()
    routes.append(
        Route(
            path='/authenticate',
            methods=['GET'],
            endpoint=handle_auth,
        )
    )
    app = Starlette(routes=routes)
    uvicorn.run(app, host=host, port=port)

if __name__ == '__main__':
    main()
```

## Notes

Key implementation details:

- **Agent Card**: Defines agent capabilities, skills, and I/O modes for discovery
- **ADKAgentExecutor**: Wraps ADK agent to handle A2A protocol requests
- **In-Memory Services**: Uses stateless services for artifacts, sessions, and memory
- **OAuth Handler**: Custom endpoint for OAuth callback authentication flow
- **Starlette Integration**: Creates HTTP server with A2A-compatible routes
- **Uvicorn Server**: Runs async web application on specified host and port
- **Streaming Support**: Agent card declares streaming capabilities for real-time responses
