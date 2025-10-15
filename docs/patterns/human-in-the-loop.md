---
title: "Pattern: Human-in-the-Loop (HITL)"
slug: "human-in-the-loop"
tags: ["human-in-the-loop", "hitl", "supervision", "collaboration", "safety", "agentic-pattern"]
themes: ["governance/oversight", "architecture/collaboration"]
source:
  origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1ImOZcw6yeb7a-uRBMNP1VdovYfyip4IdsAcLu9yue-0/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Integra supervisão e colaboração humana em sistemas agentic para garantir qualidade, segurança e decisões éticas em contextos complexos ou de alto risco."
relationships:
  snippets:
    - "snippets/human-in-the-loop/human-in-the-loop-adk-technical-support-agent.md"
  examples: []
  resources: []
---

### Problem

AI totalmente autônoma pode cometer erros críticos em domínios ambíguos, complexos ou de alto risco (saúde, finanças, jurídico). Falta julgamento nuançado, raciocínio ético e senso comum que humanos possuem. Necessidade de garantir alinhamento com valores humanos e conformidade regulatória.

### Pattern

Integrar deliberadamente supervisão humana em workflows agentic:

1. **Human Oversight**: monitorar performance do agente via dashboards, logs ou alertas em tempo real.

2. **Intervention & Correction**: agente pode solicitar intervenção humana quando encontra ambiguidade ou erro; humano corrige, fornece dados faltantes ou guia ação.

3. **Human Feedback for Learning**: coletar preferências humanas para refinar modelos (RLHF - Reinforcement Learning from Human Feedback).

4. **Decision Augmentation**: agente fornece análises/recomendações; humano toma decisão final.

5. **Human-Agent Collaboration**: trabalho cooperativo onde agente processa dados rotineiros e humano faz raciocínio criativo/complexo.

6. **Escalation Policies**: protocolos claros que ditam quando agente deve escalar para humano (ex.: transações acima de threshold, conteúdo ambíguo).

**Variante Human-on-the-loop**: humano define políticas de alto nível; AI executa ações imediatas dentro dessas políticas (ex.: trading automatizado com regras definidas por especialista).

### Trade_offs

- **Pró:** segurança, conformidade ética/regulatória, melhoria contínua via feedback.
- **Pró:** permite deploy de AI em domínios críticos onde autonomia total seria imprudente.
- **Contra:** falta de escalabilidade (humanos não conseguem revisar milhões de tarefas).
- **Contra:** depende de expertise dos operadores humanos; requer treinamento.
- **Contra:** preocupações de privacidade (dados sensíveis precisam ser anonimizados).

### When_to_use

- Domínios onde erros têm consequências severas (saúde, finanças, autônomo).
- Tarefas com ambiguidade ou nuance que LLMs não resolvem confiavelmente (moderação de conteúdo, suporte complexo).
- Melhoria contínua de modelos com dados rotulados por humanos.
- Requisitos regulatórios que exigem supervisão humana.

### Minimal_example

- [`snippets/human-in-the-loop/human-in-the-loop-adk-technical-support-agent.md`](../snippets/human-in-the-loop-adk-technical-support-agent.md) — ADK agent com escalação humana.

### Further_reading

- [Agentic Design Patterns — Capítulo 13](https://docs.google.com/document/d/1ImOZcw6yeb7a-uRBMNP1VdovYfyip4IdsAcLu9yue-0/edit?usp=sharing)
- [A Survey of Human-in-the-loop for ML (Wu et al.)](https://arxiv.org/abs/2108.00941)
