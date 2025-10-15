---
title: "Pattern: Reflection"
slug: "reflection"
tags: ["reflection", "self-critique", "iterative-improvement", "agentic-pattern"]
themes: ["reasoning/metacognition", "quality-assurance"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1HXXJOQIMWowtLw4WMiSR360caDAlZPtl5dPPgvq9IT4/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Adiciona loop de autoavaliação (ou crítico dedicado) para revisar e refinir a saída antes de expor ao usuário."
relationships:
  snippets:
    - "snippets/reflection/reflection-google-adk-generator-critic.md"
    - "snippets/reflection/reflection-langchain-iterative-code-refinement.md"
  examples: []
  resources: []
---

### Problem

Mesmo com cadeias bem projetadas, a primeira resposta do agente pode conter erros, inconsistências ou estilo inadequado. Sem feedback interno, o usuário recebe resultado ruim e precisa refazer a solicitação.

### Pattern

Reflection introduz uma etapa de crítica que avalia a resposta antes da entrega. Pode ser o próprio agente (self-reflection) ou um par produtor/crítico. O crítico compara a saída com critérios (requisitos, fatos, estilo) e gera feedback estruturado; o produtor usa o feedback para gerar uma nova versão. O ciclo termina ao atingir qualidade desejada ou limite de iterações.

### Trade_offs

- **Pró:** melhora consistência e reduz erros recorrentes; útil para conteúdo sensível.  
- **Pró:** registra racionalidade explícita, útil para auditoria.  
- **Contra:** aumenta latência e custo (chamadas extras).  
- **Contra:** se crítica for pobre, pode gerar loops inúteis; requer critérios bem definidos.

### When_to_use

- Geração de código/documentos com requisitos estritos.  
- Respostas que precisam de validação factual (RAG, relatórios).  
- Qualquer fluxo onde um reviewer humano avaliaria antes de publicar.

### Minimal_example

- [`snippets/reflection-langchain-iterative-code-refinement.md`](../snippets/reflection-langchain-iterative-code-refinement.md) — ciclo produtor/crítico para código.  
- [`snippets/reflection-google-adk-generator-critic.md`](../snippets/reflection-google-adk-generator-critic.md) — implementação usando Google ADK.

### Further_reading

- [Agentic Design Patterns — Capítulo 4](https://docs.google.com/document/d/1HXXJOQIMWowtLw4WMiSR360caDAlZPtl5dPPgvq9IT4/edit?tab=t.0)
- [Self-Refine paper](https://arxiv.org/abs/2303.17651)
