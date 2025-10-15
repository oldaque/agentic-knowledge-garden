---
title: "Pattern: Evaluation and Monitoring"
slug: "evaluation-and-monitoring"
tags: ["evaluation", "monitoring", "telemetry", "metrics", "agentic-pattern"]
themes: ["governance/measurement", "operations/reliability"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Instrumenta agentes com métricas, alertas e laços de feedback contínuos para garantir qualidade, eficiência e conformidade."
relationships:
  snippets:
    - "snippets/evaluation-and-monitoring/evaluation-and-monitoring-llm-judge.md"
    - "snippets/evaluation-and-monitoring/evaluation-and-monitoring-response-accuracy.md"
    - "snippets/evaluation-and-monitoring/evaluation-and-monitoring-token-usage.md"
  examples: []
  resources: []
---

### Problem

Agentes evoluem depois de entrar em produção. Sem telemetria contínua, você não detecta degradação de qualidade, violações de política ou desperdício de recursos.

### Pattern

Construir um ciclo fechado:
1. **Definir métricas** (qualidade, latência, custo, compliance).  
2. **Instrumentar captura** em cada estágio (entrada, tool use, saída).  
3. **Avaliar** com pipelines automáticos (LLM-as-a-judge, testes sintéticos, comparativos).  
4. **Monitorar & alertar** com thresholds, dashboards e playbooks de resposta.  
5. **Aprender** alimentando melhorias nos prompts, ferramentas e políticas.

### Trade_offs

- **Pró:** visibilidade contínua e capacidade de reação rápida.  
- **Pró:** gera dados históricos para calibração e regressão controlada.  
- **Contra:** aumenta custo operacional (infra, labeling).  
- **Contra:** métricas ruins induzem otimização míope.

### When_to_use

- Agentes com impacto direto no negócio (suporte, vendas, operações críticas).  
- Ambientes regulados que exigem trilhas de auditoria.  
- Times que fazem deploy frequente de prompts/modelos.

### Minimal_example

- [`snippets/evaluation-and-monitoring/evaluation-and-monitoring-llm-judge.md`](../snippets/evaluation-and-monitoring-llm-judge.md) — uso de LLM como juiz.  
- [`snippets/evaluation-and-monitoring/evaluation-and-monitoring-response-accuracy.md`](../snippets/evaluation-and-monitoring-response-accuracy.md) — baseline de acurácia.  
- [`snippets/evaluation-and-monitoring/evaluation-and-monitoring-token-usage.md`](../snippets/evaluation-and-monitoring-token-usage.md) — monitor de custo/latência.

### Further_reading

- [Agentic Design Patterns — Capítulo 19](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0)
- [LLM Evaluation Guide (OpenAI)](https://platform.openai.com/docs/guides/evals)
