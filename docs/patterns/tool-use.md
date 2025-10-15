---
title: "Pattern: Tool Use"
slug: "tool-use"
tags: ["tool-use", "function-calling", "external-apis", "agentic-pattern"]
themes: ["execution/tooling", "reasoning/augmentation"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1bE4iMljhppqGY1p48gQWtZvk6MfRuJRCiba1yRykGNE/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Permite que agentes chamem funções, APIs e automações externas para ir além do que está no modelo."
relationships:
  snippets:
    - "snippets/tool-use/tool-use-langchain-search-information.md"
    - "snippets/tool-use/tool-use-google-adk-google-search.md"
    - "snippets/tool-use/tool-use-crewai-stock-price-lookup.md"
  examples:
    - "examples/tool-use/README.md"
  resources: []
---

### Problem

LLMs têm conhecimento estático. Sem ferramentas, o agente não acessa dados atualizados, não executa ações concretas e não manipula sistemas do usuário.

### Pattern

Tool Use define uma interface de funções externas (http APIs, consultas, automações). O agente decide quando invocá-las, envia argumentos estruturados e usa o retorno para continuar o raciocínio. Elementos chave:
- catálogo de ferramentas com descrições curtas e parâmetros tipados;  
- política de autorização (quem pode chamar o quê, logging);  
- normalização de respostas (JSON, schemas) para evitar parsing frágil;  
- ciclo observação → decisão → ação integrado ao estado do agente.

### Trade_offs

- **Pró:** desbloqueia dados vivos, integrações e ações do mundo real.  
- **Pró:** separa lógica de negócio do prompt e permite reuso.  
- **Contra:** exige engenharia de infraestrutura (timeout, retries, segurança).  
- **Contra:** ferramentas mal definidas geram hallucinations ou chamadas inválidas.

### When_to_use

- Consultas a sistemas legados (CRM, ERP).  
- Ações concretas (enviar e-mail, abrir ticket, executar automações).  
- Enriquecimento de contexto (busca, cálculos, conversões).

### Minimal_example

- [`snippets/tool-use-langchain-search-information.md`](../snippets/tool-use-langchain-search-information.md) — função de busca com LangChain.  
- [`snippets/tool-use-google-adk-google-search.md`](../snippets/tool-use-google-adk-google-search.md) — ferramenta no Google ADK.  
- [`snippets/tool-use-crewai-stock-price-lookup.md`](../snippets/tool-use-crewai-stock-price-lookup.md) — execução com CrewAI.

### Further_reading

- [Agentic Design Patterns — Capítulo 5](https://docs.google.com/document/d/1bE4iMljhppqGY1p48gQWtZvk6MfRuJRCiba1yRykGNE/edit?usp=sharing)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
