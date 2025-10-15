---
title: "Pattern: Memory Management"
slug: "memory-management"
tags: ["memory", "context", "retention", "long-term", "short-term", "agentic-pattern"]
themes: ["knowledge/context", "architecture/state"]
source:
  origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1asVTObtzIye0I9ypAztaeeI_sr_Hx2TORE02uUuqH_c/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Gerencia memória de curto e longo prazo em agentes para manter contexto, aprender com experiência e personalizar interações."
relationships:
  snippets: []
  examples: []
  resources: []
---

### Problem

Agentes precisam reter informações entre sessões, recordar preferências, rastrear progresso e aprender com interações passadas, mas LLMs têm apenas janelas de contexto limitadas e efêmeras.

### Pattern

Implementar sistema de memória em duas camadas:

1. **Short-Term Memory (Memória Contextual)**
   - Mantém informações recentes dentro da janela de contexto do LLM.
   - Inclui mensagens, uso de ferramentas, reflexões temporárias.
   - Capacidade limitada; persiste apenas durante a sessão.

2. **Long-Term Memory (Memória Persistente)**
   - Repositório externo (banco de dados, vector stores, grafos de conhecimento).
   - Permite busca semântica e recuperação entre sessões.
   - Armazena preferências, aprendizados, históricos.

Frameworks como ADK e LangGraph fornecem:
- **Session/State**: contexto temporário de chat.
- **MemoryService/BaseStore**: busca persistente de conhecimento.

### Trade_offs

- **Pró:** personalização, rastreamento de tarefas complexas, aprendizado contínuo.
- **Pró:** suporta conversações longas e múltiplas sessões.
- **Contra:** aumenta complexidade (infra de armazenamento, sincronização).
- **Contra:** requer políticas de privacidade e retenção de dados.

### When_to_use

- Chatbots que mantêm contexto de sessões anteriores.
- Agentes de tarefas que rastreiam progresso multi-etapa.
- Aplicações personalizadas que aprendem preferências do usuário.
- Sistemas autônomos que evoluem com experiência acumulada.

### Minimal_example

(Snippets a serem criados: ADK SessionService, LangGraph Memory Store, Vertex Memory Bank)

### Further_reading

- [Agentic Design Patterns — Capítulo 8](https://docs.google.com/document/d/1asVTObtzIye0I9ypAztaeeI_sr_Hx2TORE02uUuqH_c/edit?tab=t.0)
- [LangGraph Memory Management](https://langchain-ai.github.io/langgraph/concepts/memory/)
- [Vertex Memory Bank](https://cloud.google.com/vertex-ai/docs/agent-engine/memory-bank)
