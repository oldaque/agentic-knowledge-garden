---
title: "Pattern: Goal Setting and Monitoring"
slug: "goal-setting-and-monitoring"
tags: ["goal-setting", "monitoring", "metrics", "progress-tracking", "agentic-pattern"]
themes: ["governance/measurement", "workflow/orchestration"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/10ndlCB39BWjyFRWKpcoKib4vuPD1ojD-x0-ynMaf5uw/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Define objetivos claros, conecte-os a métricas acionáveis e use feedback contínuo para evitar deriva de comportamento."
relationships:
  snippets:
    - "snippets/goal-setting/goal-setting-monitoring-langchain-code-generation-agent.md"
  examples: []
  resources: []
---

### Problem

Sem metas explícitas, agentes trabalham no escuro: interpretam mal solicitações, priorizam errado e não sabem quando parar ou escalar.

### Pattern

1. Registrar objetivos estruturados (SMART, OKR, JTBD) com dono, prazo e critérios de sucesso.  
2. Instrumentar estado e métricas que reflitam progresso (ex.: itens entregues, score de qualidade).  
3. Estabelecer cadências de revisão (por turno, sessão, diário).  
4. Acionar correções automáticas (ajuste de prompt, fallback, handoff humano) quando desvios ocorrerem.

### Trade_offs

- **Pró:** garante alinhamento a outcomes de negócio.  
- **Pró:** facilita auditoria e melhoria contínua.  
- **Contra:** overhead para definir/atualizar objetivos e métricas.  
- **Contra:** metas mal especificadas induzem comportamento distorcido.

### When_to_use

- Copilots corporativos com KPIs definidos.  
- Serviços que exigem acompanhamento de pipeline (suporte, vendas, onboarding).  
- Agentes que gerenciam projetos ou planos longos.

### Minimal_example

- [`snippets/goal-setting/goal-setting-monitoring-langchain-code-generation-agent.md`](../snippets/goal-setting-monitoring-langchain-code-generation-agent.md) — aplica objetivos + monitoramento num agente de geração de código.

### Further_reading

- [Agentic Design Patterns — Capítulo 11](https://docs.google.com/document/d/10ndlCB39BWjyFRWKpcoKib4vuPD1ojD-x0-ynMaf5uw/edit?tab=t.0)
- [SMART Goals Framework](https://en.wikipedia.org/wiki/SMART_criteria)
