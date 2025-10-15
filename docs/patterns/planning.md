---
title: "Pattern: Planning"
slug: "planning"
tags: ["planning", "strategy", "workflow", "agentic-pattern", "crewai", "openai"]
themes: ["reasoning/sequencing", "workflow/orchestration"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/18vvNESEwHnVUREzIipuaDNCnNAREGqEfy9MQYC9wb4o/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Faz o agente descobrir e revisitar a sequência de passos necessária para atingir um objetivo aberto antes de executar."
relationships:
  snippets:
    - "snippets/planning/planning-crewai-planner-writer-agent.md"
    - "snippets/planning/planning-openai-deep-research-api.md"
  examples: []
  resources: []
---

### Problem

Algumas demandas não têm workflow conhecido. Se o agente executar imediatamente, ele improvisa e se perde; se seguir script fixo, perde flexibilidade.

### Pattern

Planning introduz um módulo planejador que recebe objetivo, restrições e contexto, gera um plano estruturado (etapas, responsáveis, outputs esperados) e itera conforme novos sinais. Execução só começa após o plano estar claro; durante a execução, telemetria realimenta o planejador para ajustar próximos passos.

### Trade_offs

- **Pró:** clareza sobre o caminho; reduz desperdício e repetições.  
- **Pró:** fácil apresentar plano ao humano (aprovação/edição).  
- **Contra:** aumenta tempo de resposta inicial; risco de planos grandes demais.  
- **Contra:** precisa de heurística para replanejar quando contexto muda.

### When_to_use

- Objetivos abertos (pesquisa, estratégia, troubleshooting).  
- Missões multi-agente onde papéis dependem do plano.  
- Situações que exigem transparência: o usuário quer ver como o agente vai agir.

### Minimal_example

- [`snippets/planning-crewai-planner-writer-agent.md`](../snippets/planning-crewai-planner-writer-agent.md) — planner + executor no CrewAI.  
- [`snippets/planning-openai-deep-research-api.md`](../snippets/planning-openai-deep-research-api.md) — planejamento com Deep Research API.

### Further_reading

- [Agentic Design Patterns — Capítulo 6](https://docs.google.com/document/d/18vvNESEwHnVUREzIipuaDNCnNAREGqEfy9MQYC9wb4o/edit?usp=sharing)
- [CrewAI Planner Docs](https://docs.crewai.com/)
