---
title: "Pattern: Reasoning Techniques"
slug: "reasoning-techniques"
tags: ["reasoning", "cot", "tot", "react", "self-correction", "agentic-pattern"]
themes: ["execution/reasoning", "architecture/cognition"]
source:
  origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1Yt1W_hLaC6ZNgJXfT4W6NrCL4TzNVdKOX50kgpHiIq4/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Técnicas avançadas de raciocínio (CoT, ToT, ReAct, Self-Correction) que tornam explícito o processo de pensamento do agente, permitindo decomposição, exploração multi-caminho e refinamento iterativo."
relationships:
  snippets:
    - "snippets/reasoning-techniques/reasoning-techniques-adk-palms.md"
    - "snippets/reasoning-techniques/reasoning-techniques-langgraph-deepsearch.md"
  examples: []
  resources: []
---

### Problem

Problemas complexos exigem raciocínio multi-etapa, decomposição lógica e exploração de múltiplos caminhos de solução. LLMs em modo "resposta direta" não expõem processo de pensamento, limitando transparência, auditabilidade e capacidade de correção.

### Pattern

Implementar técnicas estruturadas de raciocínio que tornam explícito o "pensamento" do agente:

1. **Chain-of-Thought (CoT)**: gera passos intermediários antes da resposta final, decompondo problemas complexos em sub-problemas menores.

2. **Tree-of-Thought (ToT)**: explora múltiplos caminhos de raciocínio em estrutura de árvore, permitindo backtracking e exploração de alternativas.

3. **Self-Correction**: revisão crítica interna; o agente identifica erros/ambiguidades e refina a resposta iterativamente.

4. **Program-Aided Language Models (PALMs)**: gera e executa código (Python, etc.) para cálculos precisos, integrando raciocínio simbólico determinístico.

5. **ReAct (Reasoning + Acting)**: intercala pensamento, ação (tool use) e observação em loop iterativo, adaptando plano conforme feedback do ambiente.

6. **Collaborative frameworks (CoD, GoD)**: múltiplos modelos debatem e validam argumentos, reduzindo viés individual.

7. **Scaling Inference Law**: aumentar "tempo de pensamento" (mais ciclos de inferência) melhora qualidade, mesmo em modelos menores.

### Trade_offs

- **Pró:** transparência, auditabilidade, capacidade de correção, melhor performance em problemas complexos.
- **Pró:** permite composição de agentes (alguns raciocinam, outros executam).
- **Contra:** aumenta latência e custo (mais tokens, mais chamadas).
- **Contra:** requer prompts cuidadosos para guiar estrutura de raciocínio.

### When_to_use

- Resolução de problemas matemáticos, lógicos ou multi-hop.
- Debugging e geração de código que exige validação iterativa.
- Planejamento estratégico que requer avaliação de opções e consequências.
- Diagnóstico médico/jurídico que demanda raciocínio em etapas auditáveis.
- Tarefas de pesquisa profunda (Deep Research) que exigem múltiplas buscas refinadas.

### Minimal_example

- [`snippets/reasoning-techniques/reasoning-techniques-adk-palms.md`](../snippets/reasoning-techniques-adk-palms.md) — PALMs com geração de código externo.
- [`snippets/reasoning-techniques/reasoning-techniques-langgraph-deepsearch.md`](../snippets/reasoning-techniques-langgraph-deepsearch.md) — Deep Research iterativo com reflexão.

### Further_reading

- [Agentic Design Patterns — Capítulo 17](https://docs.google.com/document/d/1Yt1W_hLaC6ZNgJXfT4W6NrCL4TzNVdKOX50kgpHiIq4/edit?usp=sharing)
- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2201.11903)
- [Tree of Thoughts (Yao et al., 2023)](https://arxiv.org/abs/2305.10601)
- [ReAct: Reasoning and Acting (Yao et al., 2023)](https://arxiv.org/abs/2210.03629)
- [Scaling Inference Law (2024)](https://arxiv.org/abs/2408.00724)
