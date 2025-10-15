---
title: "Pattern: Model Context Protocol (MCP)"
slug: "model-context-protocol-mcp"
tags: ["mcp", "protocol", "model-context", "interoperability", "anthropic", "agentic-pattern"]
themes: ["execution/tooling", "architecture/integration"]
source:
  origin_note: "docs/notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1e6XimYczKmhX9zpqEyxLFWPQgGuG0brp7Hic2sFl_qw/edit?usp=sharing"
status: "stable"
last_update: "2025-10-14"
summary: "Protocolo aberto que padroniza comunicação entre LLMs e ferramentas externas, promovendo interoperabilidade e reutilização de componentes."
relationships:
  snippets: []
  examples: []
  resources: []
---

### Problem

LLMs precisam integrar com múltiplas fontes de dados e ferramentas, mas cada provedor usa interfaces proprietárias. Isso dificulta interoperabilidade, reusabilidade e composição de componentes agentic.

### Pattern

Model Context Protocol (MCP) define um padrão aberto cliente-servidor onde:

1. **MCP Servers** expõem:
   - **Resources**: dados estáticos (PDFs, registros de banco).
   - **Tools**: funções executáveis (enviar emails, consultar APIs).
   - **Prompts**: templates que guiam interações.

2. **MCP Clients** (hosts LLM ou agentes) descobrem dinamicamente capacidades disponíveis via JSON-RPC sobre STDIO (local) ou HTTP/SSE (remoto).

3. Benefícios:
   - Substituir interfaces proprietárias por padrão universal.
   - Reuso de servidores MCP entre diferentes agentes/frameworks.
   - Descoberta dinâmica de novas ferramentas sem redeploy.

### Trade_offs

- **Pró:** interoperabilidade, composição, ecossistema de componentes reutilizáveis.
- **Pró:** desacoplamento entre host LLM e ferramentas.
- **Contra:** curva de aprendizado inicial para implementar servidores.
- **Contra:** overhead adicional de transporte (comparado a chamadas diretas).

### When_to_use

- Agentes que precisam integrar múltiplas ferramentas de terceiros.
- Desenvolvimento de componentes reutilizáveis para ecossistema multi-framework.
- Aplicações que exigem descoberta dinâmica de capacidades.
- Substituição de integrações proprietárias para maior portabilidade.

### Minimal_example

(Snippets a serem criados: ADK MCPToolset, FastMCP Server, MCP client com descoberta dinâmica)

### Further_reading

- [Agentic Design Patterns — Capítulo 10](https://docs.google.com/document/d/1e6XimYczKmhX9zpqEyxLFWPQgGuG0brp7Hic2sFl_qw/edit?usp=sharing)
- [MCP Specification (Anthropic)](https://spec.modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
