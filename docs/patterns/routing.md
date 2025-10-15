---
title: "Pattern: Routing"
slug: "routing"
tags: ["routing", "coordinator", "intent-classification", "agentic-pattern"]
themes: ["workflow/orchestration", "reasoning/selection"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1ux_n8n3T4bYndOjs1DKW5ccpC802KISdy2IWnlvYbas/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Dirige cada requisição ao agente, ferramenta ou modelo mais adequado com base em intenção e contexto, mantendo decisões adaptativas controladas."
relationships:
  snippets:
    - "snippets/routing/routing-langchain-coordinator-router.md"
    - "snippets/routing/routing-google-adk-coordinator-subagents.md"
  examples: []
  resources: []
---

### Problem

Fluxos lineares tratam todos os pedidos igualmente, desperdiçando recursos e entregando respostas fracas quando o contexto exige caminhos diferentes. Sem um roteador, o agente fica preso a heurísticas fixas e perde a chance de combinar especializações.

### Pattern

Routing adiciona uma camada de coordenação que inspeciona intenção, estado e restrições (latência, custo, compliance) para decidir qual subagente, ferramenta ou modelo deve atuar.  
Implementações comuns:
- **Classificador de intenção** com LLM ou embeddings que retorna o destino (`"knowledge"`, `"calculator"`, `"support"`).  
- **Árvores de decisão** com regras explícitas para cenários críticos (ex.: bloquear ações sensíveis).  
- **Roteamento em cascata**: começa em modelo barato e sobe para especialistas quando confiança for baixa.  
- **Feedback loop**: logs e métricas alimentam re-treino do roteador e thresholds de confiança.

### Trade_offs

- **Pró:** Usa cada recurso no contexto certo, reduzindo custo e aumentando precisão.  
- **Pró:** Escala facilmente — adicionar uma capability nova é só registrar no roteador.  
- **Contra:** Ponto adicional de falha; roteadores precisam de monitoramento e auditoria.  
- **Contra:** Requer dados etiquetados ou heurísticas claras; decisões erradas afetam UX.

### When_to_use

- Produtos com múltiplos agentes especializados (pesquisa, cálculo, suporte crítico).  
- Camadas de ferramentas heterogêneas (APIs externas, automações internas) que precisam de delegação confiável.  
- Sistemas que equilibram custo/latência vs. qualidade (ex.: fallback para LLM premium).

### Minimal_example

- [`snippets/routing-langchain-coordinator-router.md`](../snippets/routing-langchain-coordinator-router.md): coordenação com LangChain.
- [`snippets/routing-google-adk-coordinator-subagents.md`](../snippets/routing-google-adk-coordinator-subagents.md): roteamento com Google ADK.

### Further_reading

- [Agentic Design Patterns — Capítulo 2](https://docs.google.com/document/d/1ux_n8n3T4bYndOjs1DKW5ccpC802KISdy2IWnlvYbas/edit?tab=t.0)
- [LangChain Router Chains](https://python.langchain.com/docs/modules/chains/router/)
- [Google ADK Routing](https://google.github.io/adk-docs/)
