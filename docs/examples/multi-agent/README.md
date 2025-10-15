---
title: "Example: Building a Content Creation Crew with Researcher and Writer Agents"
slug: "multi-agent"
summary: "Sistema multi-agente usando CrewAI onde pesquisador coleta tendências de IA e escritor produz blog post baseado nos achados."
status: "draft"
last_update: "2025-10-14"
origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
objective: "Demonstrar colaboração entre agentes especializados através de dependências de tarefas e compartilhamento de contexto"
estimated_time: "15-20 min"
related_patterns:
  - "docs/patterns/multi-agent.md"
---

### Overview

Este exemplo demonstra colaboração multi-agente usando CrewAI com dois agentes especializados: um pesquisador que identifica tendências de IA e um escritor que cria conteúdo baseado na pesquisa. Ilustra como diferentes agentes com papéis distintos podem trabalhar sequencialmente, onde o output de um agente serve de contexto para o próximo, seguindo o padrão fundamental de sistemas multi-agente.

### Prerequisites

- Python 3.9+
- Google API key (Gemini) configurada em `GOOGLE_API_KEY`
- Dependências: `crewai`, `langchain-google-genai`, `python-dotenv`

Instalação:
```bash
pip install crewai langchain-google-genai python-dotenv
```

### Steps

1. **Setup do ambiente CrewAI**
   - Configurar `GOOGLE_API_KEY` no `.env`
   - Importar `Agent`, `Task`, `Crew`, `Process` do CrewAI
   - Inicializar `ChatGoogleGenerativeAI` com modelo Gemini

2. **Definir agentes especializados**
   - **Researcher Agent**: role="Senior Research Analyst", goal="Find and summarize AI trends"
   - **Writer Agent**: role="Technical Content Writer", goal="Write engaging blog post"
   - Cada agente com backstory específico para guiar comportamento

3. **Criar tarefas com dependências**
   - `research_task`: assigned to researcher, busca top 3 trends em IA 2024-2025
   - `writing_task`: assigned to writer, **context=[research_task]** (depende do output do pesquisador)
   - Expected output definido para cada task

4. **Formar e executar Crew**
   - Criar `Crew` com agents=[researcher, writer], tasks=[research_task, writing_task]
   - Definir `process=Process.sequential` (writer só executa após researcher)
   - Executar `crew.kickoff()` e observar colaboração

5. **Experimentar variações**
   - Adicionar 3º agente (editor) para revisar blog post
   - Testar `process=Process.hierarchical` (manager coordena agentes)
   - Adicionar ferramentas externas (web search, APIs)

### Related_snippets

- [`snippets/multi-agent-crewai-blog-creation.md`](../../snippets/multi-agent-crewai-blog-creation.md) — Implementação completa com CrewAI
- [`snippets/multi-agent-google-adk-sequential-agent.md`](../../snippets/multi-agent-google-adk-sequential-agent.md) — Alternativa usando ADK SequentialAgent
