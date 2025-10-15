---
title: "Example: Building a Data Extraction Pipeline with Prompt Chaining"
slug: "prompt-chaining"
summary: "Demonstra pipeline completo de extração e transformação de dados usando prompt chaining com LangChain LCEL."
status: "draft"
last_update: "2025-10-14"
origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
objective: "Construir pipeline que extrai especificações técnicas de texto e converte para JSON estruturado"
estimated_time: "10-15 min"
related_patterns:
  - "docs/patterns/prompt-chaining.md"
---

### Overview

Este exemplo demonstra como usar prompt chaining para processar informação sequencialmente através de múltiplos passos. O pipeline extrai especificações técnicas de descrições em linguagem natural e as transforma em formato JSON estruturado, ilustrando o padrão fundamental de encadear outputs de um prompt como inputs do próximo.

### Prerequisites

- Python 3.8+
- OpenAI API key configurada em `OPENAI_API_KEY`
- Dependências: `langchain-openai`, `langchain-core`

Instalação:
```bash
pip install langchain-openai langchain-core python-dotenv
```

### Steps

1. **Setup do ambiente**
   - Criar arquivo `.env` com `OPENAI_API_KEY=your-key`
   - Importar módulos LangChain necessários

2. **Definir prompts sequenciais**
   - Prompt 1: Extrai especificações técnicas de texto não estruturado
   - Prompt 2: Transforma especificações em objeto JSON com chaves padronizadas

3. **Construir chain usando LCEL**
   - Usar operador `|` para encadear extraction → transformation
   - Adicionar `StrOutputParser()` para converter saídas LLM

4. **Executar pipeline**
   - Invocar chain com texto de entrada
   - Observar output JSON estruturado final

5. **Testar variações**
   - Experimentar diferentes textos de entrada (laptops, smartphones, servers)
   - Ajustar estrutura JSON (adicionar campos como 'gpu', 'display')

### Related_snippets

- [`snippets/prompt-chaining-langchain-extraction-transformation.md`](../../snippets/prompt-chaining-langchain-extraction-transformation.md) — Implementação completa do pipeline
