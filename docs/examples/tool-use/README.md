---
title: "Example: Building a Research Agent with Google Search and Code Execution"
slug: "tool-use"
summary: "Agente que combina Google Search e execução de código Python para responder perguntas complexas que exigem cálculos e dados atualizados."
status: "draft"
last_update: "2025-10-14"
origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
objective: "Construir agente capaz de buscar informações na web e executar código para análise de dados"
estimated_time: "15-20 min"
related_patterns:
  - "docs/patterns/tool-use.md"
---

### Overview

Este exemplo demonstra como equipar um agente com múltiplas ferramentas (Google Search + Code Executor) usando Google ADK. O agente decide autonomamente quando buscar informações atualizadas na web e quando executar código Python para realizar cálculos, ilustrando o padrão fundamental de tool use em sistemas agentic.

### Prerequisites

- Python 3.9+
- Google API key (Gemini) configurada em `GOOGLE_API_KEY`
- Google Search API key (opcional, para produção)
- Dependências: `google-adk`, `google-genai`

Instalação:
```bash
pip install google-adk google-genai python-dotenv
```

### Steps

1. **Setup do ambiente ADK**
   - Configurar `GOOGLE_API_KEY` no `.env`
   - Importar `LlmAgent`, `BuiltInCodeExecutor`, `google_search`

2. **Configurar agente com múltiplas tools**
   - Adicionar `google_search` para buscar informações atualizadas
   - Adicionar `BuiltInCodeExecutor()` para executar código Python
   - Definir instructions claras sobre quando usar cada ferramenta

3. **Testar com queries que exigem ambas tools**
   - Exemplo 1: "Qual o preço atual do Bitcoin em USD e quantos satoshis equivalem a $100?"
     - Usa Google Search para preço atual
     - Usa Code Executor para cálculo de satoshis
   - Exemplo 2: "Qual a população atual do Brasil e quantos % da população mundial isso representa?"

4. **Observar decisão autônoma do agente**
   - Agent escolhe search quando precisa de dados atuais
   - Agent escolhe code execution quando precisa de cálculos precisos
   - Agent pode combinar ambas ferramentas em sequência

5. **Experimentar variações**
   - Adicionar mais tools (web scraping, APIs externas)
   - Ajustar instructions para guiar seleção de tools

### Related_snippets

- [`snippets/tool-use-google-adk-google-search.md`](../../snippets/tool-use-google-adk-google-search.md) — Agent com Google Search
- [`snippets/tool-use-google-adk-code-execution.md`](../../snippets/tool-use-google-adk-code-execution.md) — Agent com Code Executor
