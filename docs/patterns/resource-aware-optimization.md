---
title: "Pattern: Resource-Aware Optimization"
slug: "resource-aware-optimization"
tags: ["resource", "optimization", "efficiency", "cost", "performance", "agentic-pattern"]
themes: ["operations/efficiency", "governance/cost"]
source:
  origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1nAN58l6JjqEJHk43126uh7xgdEblCpcbsNUHXgtBmJQ/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Otimiza uso de recursos computacionais, temporais e financeiros através de seleção dinâmica de modelos, caching e estratégias de eficiência."
relationships:
  snippets:
    - "snippets/resource-aware-optimization/resource-aware-optimization-adk-agents.md"
    - "snippets/resource-aware-optimization/resource-aware-optimization-query-router-agent.md"
    - "snippets/resource-aware-optimization/resource-aware-optimization-openai.md"
    - "snippets/resource-aware-optimization/resource-aware-optimization-openrouter.md"
  examples: []
  resources: []
---

### Problem

Aplicações agentic podem ser caras e lentas se sempre usarem modelos top-tier. Sem gestão dinâmica de recursos, sistema opera ineficientemente, desperdiçando budget em tarefas simples ou falhando por indisponibilidade de modelos.

### Pattern

Implementar arquitetura multi-agente com otimização consciente de recursos:

1. **Router Agent**: classifica complexidade da requisição e direciona para modelo apropriado (ex.: Gemini Flash para queries simples, Gemini Pro para raciocínio complexo).

2. **Fallback Mechanism**: quando modelo preferencial está indisponível (throttled, overload), sistema automaticamente usa modelo backup (graceful degradation).

3. **Critique Agent**: avalia qualidade das respostas e refina lógica de roteamento ao longo do tempo (feedback loop).

4. **Técnicas adicionais**:
   - Adaptive tool selection (escolher ferramenta mais eficiente por custo/latência).
   - Contextual pruning/summarization (reduzir tokens de prompt).
   - Caching de respostas frequentes.
   - Parallelization e computação distribuída.

### Trade_offs

- **Pró:** reduz custo operacional significativamente, mantém latência aceitável, aumenta confiabilidade (fallback).
- **Pró:** permite escalar sistemas agentic sem explosão de custos.
- **Contra:** aumenta complexidade de arquitetura (múltiplos agentes, lógica de roteamento).
- **Contra:** Router Agent pode adicionar latência; precisa ser otimizado.

### When_to_use

- Orçamento limitado para APIs de LLM ou infra computacional.
- Aplicações latency-sensitive que exigem resposta rápida.
- Deploy em hardware limitado (edge devices, mobile).
- Workflows multi-etapa onde diferentes tarefas têm requisitos variados.
- Necessidade de alta disponibilidade (fallback para garantir continuidade).

### Minimal_example

- [`snippets/resource-aware-optimization/resource-aware-optimization-adk-agents.md`](../snippets/resource-aware-optimization-adk-agents.md) — ADK multi-agent com Gemini Flash/Pro.
- [`snippets/resource-aware-optimization/resource-aware-optimization-query-router-agent.md`](../snippets/resource-aware-optimization-query-router-agent.md) — Router Agent com LLM.
- [`snippets/resource-aware-optimization/resource-aware-optimization-openrouter.md`](../snippets/resource-aware-optimization-openrouter.md) — OpenRouter com fallback automático.

### Further_reading

- [Agentic Design Patterns — Capítulo 16](https://docs.google.com/document/d/1nAN58l6JjqEJHk43126uh7xgdEblCpcbsNUHXgtBmJQ/edit?usp=sharing)
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [OpenRouter API](https://openrouter.ai/docs)
