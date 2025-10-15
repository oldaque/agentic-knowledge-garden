---
title: "Pattern: Knowledge Retrieval (RAG)"
slug: "knowledge-retrieval-rag"
tags: ["rag", "retrieval", "knowledge", "vector", "search", "agentic-pattern"]
themes: ["knowledge/context", "execution/tooling"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1v96Oobio6xDOqbK8ejsXjmOc4Dp2uoLMo5_gfJgi-NE/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Conecta agentes a bases externas via busca semântica para fornecer contexto atualizado e citável antes da geração."
relationships:
  snippets:
    - "snippets/knowledge-retrieval/knowledge-retrieval-rag-langchain.md"
    - "snippets/knowledge-retrieval/knowledge-retrieval-rag-adk-vertex-ai.md"
    - "snippets/knowledge-retrieval/knowledge-retrieval-rag-adk-google-search.md"
  examples: []
  resources: []
---

### Problem

LLMs sozinhos não acessam dados recentes nem conhecimento interno. Resultado: respostas desatualizadas, alucinações e falta de confiança.

### Pattern

Retrieval-Augmented Generation cria um pipeline em dois passos:
1. **Retriever** localiza passagens relevantes (vetores, BM25, híbrido) com filtros de segurança.  
2. **Generator** recebe a consulta + contexto recuperado, produzindo resposta citável.

Pontos críticos:
- chunking + embeddings corretos para cada domínio;  
- política de fusão (rerank, top‑k, baseada em score);  
- feedback loop (atualizar índice, remover conteúdo vencido).

### Trade_offs

- **Pró:** respostas fundamentadas e atualizadas.  
- **Pró:** dá transparência (citations).  
- **Contra:** arquitetura mais complexa (pipelines, infra de busca).  
- **Contra:** indexação custosa e manutenção contínua.

### When_to_use

- Suporte que depende de KB dinâmico.  
- Aplicações reguladas que exigem referências.  
- Agentes que combinam várias fontes internas/externas.

### Minimal_example

- [`snippets/knowledge-retrieval/knowledge-retrieval-rag-langchain.md`](../snippets/knowledge-retrieval-rag-langchain.md)  
- [`snippets/knowledge-retrieval/knowledge-retrieval-rag-adk-vertex-ai.md`](../snippets/knowledge-retrieval-rag-adk-vertex-ai.md)  
- [`snippets/knowledge-retrieval/knowledge-retrieval-rag-adk-google-search.md`](../snippets/knowledge-retrieval-rag-adk-google-search.md)

### Further_reading

- [Agentic Design Patterns — Capítulo 14](https://docs.google.com/document/d/1v96Oobio6xDOqbK8ejsXjmOc4Dp2uoLMo5_gfJgi-NE/edit?usp=sharing)
- [RAG Architecture Guide (IBM)](https://www.ibm.com/blog/rag/)
