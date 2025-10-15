---
title: "Fundamentos de Sistemas Agentic"
slug: "agentic-fundamentals"
tags: ["agents", "fundamentals", "intro", "llm", "tool-use"]
themes: ["foundations", "intro"]
status: "draft"
last_update: "2025-10-14"
summary: "Introdução aos conceitos fundamentais de agentes autônomos: definição, componentes essenciais e ciclos de execução."
level: "intro"
origin_notes:
  - "docs/notes/2025-10-13_book-agentic-design-patterns.md"
relationships:
  patterns:
    - "docs/patterns/tool-use.md"
    - "docs/patterns/prompt-chaining.md"
    - "docs/patterns/routing.md"
  snippets:
    - "docs/snippets/tool-use-google-adk-code-execution.md"
  examples:
    - "docs/examples/tool-use/README.md"
---

## Objective

Estabelecer compreensão sólida sobre o que define um agente autônomo, diferenciando-o de aplicações LLM tradicionais. Ao final, você entenderá os componentes essenciais (reasoning, tools, memory) e os ciclos fundamentais (thought → action → observation).

## Core_concepts

- **Agente vs. LLM simples**: agente decide autonomamente próximos passos; LLM tradicional apenas completa texto
- **Ciclo agentic**: observação → raciocínio → seleção de ação → execução → feedback → repetição
- **Tool use**: capacidade de chamar funções externas (APIs, automações, código)
- **Memory**: manutenção de estado entre execuções (short-term via contexto, long-term via vector stores)
- **Reasoning patterns**: técnicas estruturadas (CoT, ReAct, Planning) para decompor problemas complexos

## Content

### O que é um Agente?

Um **agente agentic** é um sistema que:
1. Observa ambiente/entrada
2. Raciocina sobre próximos passos
3. Escolhe e executa ação (tool call, resposta, busca)
4. Incorpora feedback da ação
5. Repete até atingir objetivo

Diferente de um chatbot que apenas responde queries, o agente **persegue goals** e **adapta estratégia** conforme resultados intermediários.

### Componentes Essenciais

**1. Reasoning Engine (LLM)**
Core do agente. Usa LLM para interpretar estado atual, selecionar ação apropriada e gerar argumentos para ferramentas.

**2. Tool Interface**
Catálogo de funções externas disponíveis ao agente:
- Busca (Google Search, RAG)
- Execução (Python Code Executor, APIs)
- Escrita (enviar emails, criar tickets)

Agente escolhe qual tool chamar baseado em descrição e parâmetros tipados.

**3. Memory System**
- **Short-term**: contexto LLM (últimas N mensagens)
- **Long-term**: armazena conhecimento persistente (vector DB, grafos)

**4. Orchestration Logic**
Frameworks como LangChain, CrewAI, Google ADK proveem estrutura para:
- Definir agentes com instructions
- Registrar ferramentas
- Gerenciar execução multi-step
- Logging e observability

### Ciclos Fundamentais

**ReAct Loop (Reasoning + Acting)**
```
Thought: "Preciso do preço atual do Bitcoin"
Action: google_search("bitcoin price USD")
Observation: "$45,230"
Thought: "Agora posso calcular satoshis"
Action: code_executor("100 / 45230 * 100_000_000")
Observation: "221,048 satoshis"
Answer: "$100 equivale a ~221k satoshis"
```

**Prompt Chaining**
Sequência linear de prompts onde output(step N) → input(step N+1). Útil para transformações determinísticas (extração → análise → geração).

### Quando Usar Agentes?

✅ **Sim**, quando:
- Tarefa requer múltiplos passos com decisões intermediárias
- Necessita integração com ferramentas externas (APIs, DBs)
- Objetivos dinâmicos que mudam conforme contexto

❌ **Não**, quando:
- Tarefa simples de completar texto
- Resposta single-shot suficiente
- Não há necessidade de ações externas

## Further_reading

- [Pattern: Tool Use](../../patterns/tool-use.md)
- [Pattern: Prompt Chaining](../../patterns/prompt-chaining.md)
- [Example: Building a Research Agent](../../examples/tool-use/README.md)
- [Livro: Agentic Design Patterns (Capítulo 1)](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit)
