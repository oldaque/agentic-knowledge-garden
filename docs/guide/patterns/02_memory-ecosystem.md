---
title: "Ecossistema de Memória em Agentes"
slug: "memory-ecosystem"
tags: ["memory", "state", "context", "rag", "vector-db", "session"]
themes: ["memory", "state-management"]
status: "draft"
last_update: "2025-10-14"
summary: "Arquiteturas de memória short-term e long-term em sistemas agentic, cobrindo context windows, vector stores e técnicas sem echo."
level: "intermediate"
origin_notes:
  - "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  - "docs/notes/2025-10-13_agent-memory-without-echo.md"
relationships:
  patterns:
    - "docs/patterns/memory-management.md"
    - "docs/patterns/knowledge-retrieval-rag.md"
    - "docs/patterns/agent-memory-without-echo.md"
  snippets: []
  examples: []
---

## Objective

Compreender como agentes mantêm contexto conversacional e conhecimento persistente através de múltiplas execuções. Ao final, você será capaz de projetar arquiteturas de memória que equilibram custo (tokens), latência e qualidade de recall.

## Core_concepts

- **Short-term memory**: contexto LLM (janela de últimas N mensagens) - efêmero e limitado
- **Long-term memory**: armazenamento externo persistente (vector DBs, grafos) - recuperável semanticamente
- **Session vs. Global memory**: escopo por usuário/thread vs. compartilhado entre todos
- **Memory without echo**: técnica de comprimir histórico sem reinjetar verbatim no contexto
- **Semantic search**: busca por similaridade (embeddings) em vez de keyword matching

## Content

### Problemática da Memória

Agentes precisam:
1. Recordar preferências do usuário entre sessões
2. Manter contexto conversacional multi-turn
3. Acessar conhecimento acumulado (docs, interações passadas)

Mas LLMs têm:
- Contexto limitado (4k-128k tokens)
- Custo proporcional ao tamanho do contexto
- Não retêm informação além da sessão atual

### Arquitetura em Duas Camadas

**Short-Term (Contextual Memory)**
- Mantém N últimas mensagens no context window
- Frameworks gerenciam com `ConversationBufferMemory` (LangChain) ou `Session.state` (ADK)
- Trade-off: mais contexto = mais custo + melhor coerência

**Long-Term (Persistent Memory)**
- Armazena informações duradouras em vector DB (Pinecone, Chroma, Vertex AI Search)
- Busca semântica quando relevante: `user_query → embedding → top_k_results`
- Tipos de memória long-term:
  - **Semantic**: fatos ("usuário prefere Python")
  - **Episodic**: experiências ("resolvemos bug X assim")
  - **Procedural**: regras aprendidas ("sempre validar JSON antes de parsear")

### Frameworks e Implementação

**Google ADK**
- `Session`: thread individual de chat, gerenciado por `SessionService`
- `session.state`: dicionário temporário (chave-valor) para dados da sessão
- `MemoryService`: busca persistente (`add_session_to_memory`, `search_memory`)

**LangChain/LangGraph**
- `ConversationBufferMemory`: histórico automático injetado no prompt
- `BaseStore` (LangGraph): armazenamento long-term com namespaces (user_id, etc.)

**Vertex Memory Bank**
- Serviço gerenciado do Vertex AI
- Analisa conversações async, extrai fatos/preferências
- Integra com ADK, LangGraph, CrewAI

### Técnica: Memory Without Echo

Problema: reinjetar todo histórico no contexto consome tokens e degrada performance.

Solução: **comprimir** informações essenciais em formato estruturado antes de armazenar:
- Extrair entidades-chave + relacionamentos
- Resumir decisões/ações tomadas
- Armazenar como metadata em vector DB
- Recuperar via busca semântica quando relevante

Exemplo:
```
❌ Echo total (custoso):
User: "Preciso instalar pandas"
Agent: "pip install pandas"
[reinjetar 100% no próximo turn]

✅ Memory without echo:
Armazenar: {user_needs: ["pandas"], resolved: true}
Próximo turn: buscar "pandas" → encontrar resolução prévia
```

### Best Practices

1. **Separar contexto imediato de conhecimento**
   - Short-term: últimas 5-10 mensagens
   - Long-term: buscar apenas quando query menciona tópico relacionado

2. **Definir políticas de retenção**
   - Limpar sessões antigas após N dias
   - Priorizar memórias com maior engagement

3. **Monitorar custo de contexto**
   - Alertar quando context size > threshold
   - Implementar summarization automática

4. **Privacy e compliance**
   - Anonimizar dados sensíveis antes de armazenar
   - Permitir user-initiated forget (GDPR)

## Further_reading

- [Pattern: Memory Management](../../patterns/memory-management.md)
- [Pattern: Knowledge Retrieval (RAG)](../../patterns/knowledge-retrieval-rag.md)
- [Pattern: Agent Memory Without Echo](../../patterns/agent-memory-without-echo.md)
- [Vertex Memory Bank Docs](https://cloud.google.com/vertex-ai/docs/agent-engine/memory-bank)
- [LangGraph Memory Guide](https://langchain-ai.github.io/langgraph/concepts/memory/)
