---
title: "Pattern: Guardrails and Safety"
slug: "guardrails-safety"
tags: ["guardrails", "safety", "moderation", "policy", "agentic-pattern"]
themes: ["governance/safety", "operations/reliability"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1DdukF8iTrpxLKHx-H-Jp8g8jzM4GNAE2Y12xD2fEmGg/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Aplica controles multi-camada para manter agentes dentro das políticas, proteger dados sensíveis e evitar ações perigosas."
relationships:
  snippets:
    - "snippets/guardrails/guardrails-safety-patterns-crewai.md"
    - "snippets/guardrails/guardrails-safety-patterns-vertex-ai.md"
  examples: []
  resources: []
---

### Problem

Agentes têm acesso crescente a dados e ações. Sem salvaguardas, podem violar políticas, expor PII ou executar comandos destrutivos.

### Pattern

Implementar guardrails em quatro camadas:
- **Entrada:** moderação, validação de schema, verificação de permissões.
- **Raciocínio/planejamento:** limites por papel, aprovação humana, filtros de intenção.
- **Execução:** whitelists de ferramentas, sandbox, simulação antes de aplicar mudanças reais.
- **Saída:** moderação, redatores de PII, citers de fontes, detecção de alucinação.
Tudo respaldado por telemetria, auditoria e processos de revisão.

### Trade_offs

- **Pró:** reduz risco regulatório e incidente grave.  
- **Pró:** aumenta confiança do usuário/stakeholder.  
- **Contra:** adiciona latência e complexidade de manutenção.  
- **Contra:** controles excessivamente rígidos podem bloquear uso legítimo.

### When_to_use

- Produtos orientados a compliance (finanças, saúde, jurídico).  
- Aplicações com automação de tool-use/integração profunda.  
- Plataformas abertas a usuários externos (risco de abuso).

### Minimal_example

- [`snippets/guardrails/guardrails-safety-patterns-crewai.md`](../snippets/guardrails-safety-patterns-crewai.md)  
- [`snippets/guardrails/guardrails-safety-patterns-vertex-ai.md`](../snippets/guardrails-safety-patterns-vertex-ai.md)

### Further_reading

- [Agentic Design Patterns — Capítulo 18](https://docs.google.com/document/d/1DdukF8iTrpxLKHx-H-Jp8g8jzM4GNAE2Y12xD2fEmGg/edit?tab=t.0)
- [Anthropic Constitutional AI](https://www.anthropic.com/index/constitutional-ai)
