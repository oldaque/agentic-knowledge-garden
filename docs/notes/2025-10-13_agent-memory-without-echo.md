title: "Memória do agente sem eco: como evitar respostas duplicadas"
slug: "agent-memory-without-echo"
tags: ["memory", "agent", "deduplication", "idempotency", "langgraph", "redis", "celery", "duckdb", "guardrails"]
themes: ["memory", "conversation-quality", "operations"]
source:
  type: "linkedin"
  title: "Memória do agente sem eco: como evitar respostas duplicadas"
  author: "Anderson Amaral"
  org: null
  url: "https://www.linkedin.com/feed/update/urn:li:activity:7383532727225987072"
status: "draft"
created_at: "2025-10-13"
updated_at: "2025-10-13"
summary: "Técnicas e ferramentas para evitar que agentes de IA gerem respostas repetitivas, abordando desde o armazenamento de memória até o processamento assíncrono de tarefas."
relationships:
  promotes_to:
    - "patterns/agent-memory-without-echo.md"
  related_notes: []
---

### Overview
Evitar “eco” em agentes conversacionais depende de separar a resposta síncrona do tratamento de memória, mantendo consistência em cada turno. A proposta combina grafos de estado, locks distribuídos e filas assíncronas para garantir idempotência ponta a ponta.

### Brain Dump
- Repetição recorrente vem de três causas: histórico bruto demais, escrita concorrente e falta de idempotência.
- PydanticAI estrutura a memória (episódica, resumo e variáveis) para evitar strings soltas.
- LangGraph usa `MemorySaver()` e checkpoints, passando apenas o essencial ao próximo nó.
- Redis mantém o estado de sessão e fornece locks via `SET NX` com TTL por turno.
- DuckDB viabiliza contexto estruturado barato para consultas rápidas.
- Guardrails deduplica saída via hash, aplica filtros de repetição e políticas de estilo.
- Celery orquestra tarefas fora do caminho síncrono com write-behind, idempotência por chave (`session_id:turn_id`), rate limit, retries e debounce de eventos.
- Fluxo resumido: usuário fala → LangGraph responde rápido → Celery cuida da memória → Redis controla concorrência → DuckDB/índices atualizados → Guardrails garante resposta limpa.

### Highlights
- Arquitetura separa conversa síncrona da persistência, reduzindo latência percebida.
- Locks distribuídos + idempotência por turno eliminam escrita duplicada.
- Guardrails atuam como camada final contra repetição antes da resposta sair.

### Test Ideas
- Simular múltiplos workers escrevendo memória para validar locks Redis + idempotência.
- Estressar conversas longas com variações de contexto para medir efetividade do resumo incremental.
- Monitorar hashes de saída para confirmar a eficácia da deduplicação no Guardrails.

### Destilado
O núcleo do padrão é tratar memória como preocupação assíncrona: o usuário recebe a resposta rápida enquanto Celery cuida do write-behind de resumos, embeddings e métricas. LangGraph delimita o escopo de contexto, Redis assegura exclusão mútua, DuckDB evita reprocessamento, e Guardrails garante que respostas revisadas não repetem o turno anterior. Essa combinação mantém a conversa fluida, barata e previsível mesmo com muitas interações simultâneas.

### Next Steps
- Promover a nota para `patterns/agent-memory-without-echo.md` (feito).
- Criar snippet com fluxo Celery + Redis locks em pseudo-código.
- Registrar métricas sugeridas (hashes de resposta, retries) no hub de observabilidade.
