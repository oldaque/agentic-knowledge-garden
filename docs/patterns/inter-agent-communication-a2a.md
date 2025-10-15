---
title: "Pattern: Inter-Agent Communication (A2A)"
slug: "inter-agent-communication-a2a"
tags: ["inter-agent", "communication", "a2a", "protocol", "collaboration", "agentic-pattern"]
themes: ["architecture/integration", "execution/coordination"]
source:
  origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1H6HmUYcy5kugt5gt7Kh2Zzb8C62d5pu36RsgMNDCX24/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Protocolo aberto baseado em HTTP que padroniza comunicação e coordenação entre agentes de diferentes frameworks, permitindo delegação de tarefas e colaboração multi-agente."
relationships:
  snippets:
    - "snippets/inter-agent-communication/inter-agent-communication-a2a-adk-agent-creation.md"
    - "snippets/inter-agent-communication/inter-agent-communication-a2a-adk-server-setup.md"
  examples: []
  resources: []
---

### Problem

Agentes individuais têm limitações ao enfrentar problemas complexos. Quando construídos em frameworks diferentes (ADK, LangGraph, CrewAI), falta linguagem comum para coordenação, delegação de tarefas e troca de informações. Integração custosa e não escalável.

### Pattern

Agent2Agent (A2A) é protocolo aberto HTTP/JSON-RPC 2.0 que padroniza comunicação inter-agente:

1. **Agent Card**: identidade digital (JSON) que descreve capacidades, skills, endpoint URL, métodos de autenticação e modos de I/O do agente.

2. **Agent Discovery**: mecanismos para encontrar agentes disponíveis (well-known URI, registros curados, configuração direta).

3. **Interaction Modes**:
   - Synchronous request/response (rápido, imediato).
   - Asynchronous polling (tarefas longas com task ID).
   - Streaming (SSE) para atualizações incrementais em tempo real.
   - Webhooks para notificações push em tarefas muito longas.

4. **Task-Based Communication**: comunicação estruturada em torno de tasks assíncronos com estados (submitted, working, completed), suportando processamento paralelo.

5. **Security**: mTLS, audit logs, autenticação declarada no Agent Card (OAuth 2.0, API keys via HTTP headers).

**A2A vs. MCP**: A2A foca em coordenação/delegação entre agentes; MCP foca em estruturar contexto LLM + integração com ferramentas externas. Protocolos complementares.

### Trade_offs

- **Pró:** interoperabilidade universal, modularidade, escalabilidade, ecossistema multi-framework.
- **Pró:** permite sistemas distribuídos com agentes especializados em portas/hosts diferentes.
- **Contra:** overhead adicional de rede (HTTP) comparado a comunicação em-memória.
- **Contra:** requer adesão ao padrão; curva de aprendizado inicial.

### When_to_use

- Orquestrar colaboração entre 2+ agentes de frameworks diferentes.
- Aplicações modulares onde agentes especializados cuidam de partes específicas do workflow.
- Descoberta dinâmica de capacidades de outros agentes.
- Workflows complexos com delegação de tarefas (ex.: agente A coleta dados → agente B analisa → agente C gera relatório).

### Minimal_example

- [`snippets/inter-agent-communication/inter-agent-communication-a2a-adk-agent-creation.md`](../snippets/inter-agent-communication-a2a-adk-agent-creation.md) — Criação de ADK agent A2A.
- [`snippets/inter-agent-communication/inter-agent-communication-a2a-adk-server-setup.md`](../snippets/inter-agent-communication-a2a-adk-server-setup.md) — Setup de A2A server com AgentCard.

### Further_reading

- [Agentic Design Patterns — Capítulo 15](https://docs.google.com/document/d/1H6HmUYcy5kugt5gt7Kh2Zzb8C62d5pu36RsgMNDCX24/edit?usp=sharing)
- [A2A Protocol Spec](https://a2a-protocol.org/latest/)
- [A2A GitHub Samples](https://github.com/google-a2a/a2a-samples)
- [Trickle A2A Tutorial](https://www.trickle.so/blog/how-to-build-google-a2a-project)
- [O'Reilly: Designing Collaborative Multi-Agent Systems with A2A](https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/)
