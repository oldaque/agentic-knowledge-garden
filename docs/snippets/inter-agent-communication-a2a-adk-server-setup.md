---
name: "Inter-Agent Communication - ADK Server Setup"
objective: "Demonstrates setting up an A2A server using Google ADK for agent communication."
how_to_run: "Requires Google ADK and appropriate credentials. Run: python inter-agent-communication-a2a-adk-server-setup.py"
from_note: "../patterns/inter-agent-communication-a2a.md"
---

# A2A Server Setup with Google ADK

This example shows how to set up an A2A (Agent-to-Agent) server using Google ADK for inter-agent communication.

## Code Example

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

## Explanation

This example demonstrates setting up an A2A (Agent-to-Agent) server using Google ADK:

1. **Agent Card Creation**: Defines agent capabilities (skills, input/output modes, streaming support)
2. **ADK Agent Executor**: Wraps the ADK agent to handle A2A protocol requests
3. **In-Memory Services**: Uses InMemoryArtifactService, InMemorySessionService, and InMemoryMemoryService for stateless operation
4. **Starlette Web Application**: Creates HTTP server with A2A routes and authentication endpoint
5. **Uvicorn Server**: Runs the application on specified host and port

The setup provides a complete A2A-compliant server that other agents can communicate with using the defined skills.</content>
