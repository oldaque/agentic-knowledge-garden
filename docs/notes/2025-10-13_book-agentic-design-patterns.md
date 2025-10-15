title: "Livro: Agentic Design Patterns"
slug: "book-agentic-design-patterns"
tags: ["book", "agentic-patterns", "design-patterns", "google", "reference"]
themes: ["curriculum", "agentic-patterns", "reading-list"]
source:
  type: "book"
  title: "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0"
status: "draft"
created_at: "2025-10-13"
updated_at: "2025-10-13"
summary: "Sumário e estrutura do livro 'Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems', um guia abrangente sobre a construção de sistemas de IA agenticos."
relationships:
  promotes_to:
    - "resources/links.md"
    - "patterns/README.md"
  related_notes: []
---

### Overview
Livro de 424 páginas que serve como catálogo prático de padrões agenticos, cobrindo desde estruturas de indução de prompt até governança e monitoramento. Excelente trilha para transformar notas em capítulos temáticos.

### Brain Dump
- Estrutura em quatro partes: fundamentos de padrões, memória/aprendizado, resiliência/segurança e otimização avançada.
- Cada capítulo mapeia diretamente para uma entrada em `docs/patterns`, facilitando promoção e atualização incremental.
- Apêndices trazem repertório hands-on (frameworks, CLI agents, raciocínio interno) útil para exemplos/snippets.
- O capítulo “What makes an AI system an agent?” ancora conceitos para o guia base.

### Highlights
- Parte I (Ch. 1–7): padrões core (Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent).
- Parte II (Ch. 8–11): operações de memória, adaptação, MCP e definição/monitoramento de objetivos.
- Parte III (Ch. 12–14): resiliência, humanos no loop, RAG — todos já mapeados para o garden.
- Parte IV (Ch. 15–19): comunicação entre agentes, otimização de recursos, raciocínio, guardrails e evaluation loops.
- Apêndices conectam frameworks, construção de agentes e ferramentas complementares.

### Test Ideas
- Criar uma planilha de leitura cruzando capítulos com gaps no garden para priorizar promoções.
- Extrair para cada capítulo as principais heurísticas e comparar com implementações existentes.
- Validar consistência entre os padrões do livro e os padrões internos (identificar divergências).

### Destilado
O livro funciona como backbone para a taxonomia do Agentic Knowledge Garden. Cada capítulo especifica problema, forças e trade-offs — exatamente o que precisamos nas páginas de padrão. Os apêndices sugerem exemplos executáveis e frameworks que podem alimentar `docs/examples` e `docs/snippets`. Excelente referência para manter o garden alinhado com o estado da arte.

### Next Steps
- Garantir que todos os capítulos citados estão promovidos em `docs/patterns` com link de volta.
- Criar uma visão “Leitura Guiada” em Guides usando a estrutura do sumário.
- Adicionar recursos complementares (Amazon, artigos de Gulli) em `resources/links.md`.
