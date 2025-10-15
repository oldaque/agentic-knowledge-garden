---
title: "Pattern: Parallelization"
slug: "parallelization"
tags: ["parallelization", "concurrency", "performance", "agentic-pattern"]
themes: ["execution/performance", "workflow/orchestration"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1XVMp4RcRkoUJTVbrP2foWZX703CUJpWkrhyFU2cfUOA/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Dispara chamadas e subagentes independentes ao mesmo tempo para reduzir latência e entregar respostas mais completas em menos ciclos."
relationships:
  snippets:
    - "snippets/parallelization/parallelization-langchain-map-synthesis-chain.md"
    - "snippets/parallelization/parallelization-google-adk-research-synthesis.md"
  examples: []
  resources: []
---

### Problem

Execuções sequenciais desperdiçam tempo quando o agente depende de múltiplas tarefas independentes (consultar APIs, resumir documentos, gerar variações). As chamadas ficam aguardando filas longas e o usuário percebe latência desnecessária.

### Pattern

Parallelization divide o fluxo em ramos independentes que rodam simultaneamente. Cada ramo resolve parte da demanda (busca de dados, análise, geração) e um nó agregador sintetiza tudo no final.  
Estratégias úteis:
- fan-out + fan-in com LangGraph/LangChain LCEL;  
- enfileirar jobs assíncronos (Celery, GCP Tasks) para workloads pesados;  
- usar timeouts e retries por ramo;  
- coletar telemetria para medir ganhos de latência.

### Trade_offs

- **Pró:** menor tempo de resposta em tarefas com I/O pesado; maior cobertura (mais hipóteses avaliadas).  
- **Pró:** permite repartir carga entre múltiplas instâncias/modelos.  
- **Contra:** complexidade adicional para controlar erros e juntar resultados.  
- **Contra:** consumo de recursos cresce; precisa de limites por ramo para evitar saturação.

### When_to_use

- Pesquisa/monitoramento com múltiplas fontes simultâneas.  
- Geração de conteúdo multi-parte (títulos, corpo, CTAs).  
- Execução de agentes paralelos especializados (ex.: brainstorm vs. crítica).

### Minimal_example

- [`snippets/parallelization-langchain-map-synthesis-chain.md`](../snippets/parallelization-langchain-map-synthesis-chain.md) — fan-out/fan-in com LangChain.  
- [`snippets/parallelization-google-adk-research-synthesis.md`](../snippets/parallelization-google-adk-research-synthesis.md) — paralelismo no Google ADK.

### Further_reading

- [Agentic Design Patterns — Capítulo 3](https://docs.google.com/document/d/1XVMp4RcRkoUJTVbrP2foWZX703CUJpWkrhyFU2cfUOA/edit?tab=t.0)
- [LangChain LCEL Map-Reduce](https://python.langchain.com/docs/expression_language/how_to/parallel/)
