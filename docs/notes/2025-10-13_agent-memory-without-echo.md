---
title: "Memória do agente sem eco: como evitar respostas duplicadas"
slug: "agent-memory-without-echo"
tags: ["memory", "agent", "deduplication", "idempotency", "langgraph", "redis", "celery", "duckdb", "guardrails"]
source:
  type: "linkedin"
  author: "Anderson Amaral"
  org: null
  url: "https://www.linkedin.com/feed/update/urn:li:activity:7383532727225987072"
status: "draft"
created_at: "2025-10-13"
summary: "Técnicas e ferramentas para evitar que agentes de IA gerem respostas repetitivas, abordando desde o armazenamento de memória até o processamento assíncrono de tarefas."
---

### Conteúdo Bruto

🧠 Memória do agente sem “eco”: como evitar respostas duplicadas

Repetição a cada turno costuma vir de 3 problemas: (1) reenvio do histórico bruto, (2) escrita concorrente da memória, (3) ausência de controles de idempotência. Na Scoras Stack, resolvemos assim:

1. PydanticAI: memória tipada e validada (episódica, resumo conversacional e variáveis de sessão). Nada de string solta.

2. LangGraph: grafo de estados com MemorySaver() e checkpoints; só o essencial segue para o próximo nó.

3. Redis: armazenamento de sessão e locks distribuídos (garantimos um único write por turno via SET NX com TTL).

4. DuckDB: contexto estruturado e barato para consultas; evita reprocessar documentos a cada interação.

5. Guardrails: dedupe de saída (hash do conteúdo), filtros de repetição e políticas de estilo antes de responder.

6. Celery: o maestro assíncrono.
   - Write-behind da memória (resumo e embeddings) fora do request principal.
   - Idempotência por chave de turno (ex: session_id:turn_id) evitando jobs duplicados.
   - Rate limit e retry com backoff para chamadas a LLMs e vetores.
   - Debounce de eventos rápidos (consolida múltiplas edições do usuário em um único resumo).
   - Orquestração com groups/chords para batch de ferramentas e atualização de memória ao final.
   - Outbox/Saga (opcional) para confirmar persistência antes de “promover” o estado do agente.

💡 Fluxo prático:
Usuário fala → LangGraph processa → resposta sai rápido → Celery enfileira tarefas de “memória” (resumo, indexação, métricas) → Redis bloqueia writes concorrentes → DuckDB/índices são atualizados uma vez por turno → Guardrails checa duplicação antes de enviar a próxima saída.

Checklist anti-eco:
- Não reenviar todo o histórico; use resumo incremental.
- Lock + idempotency key em qualquer escrita de memória.
- Deduplicação por hash no pós-processamento.
- Jobs Celery para tudo que não precisa estar no caminho síncrono.

Resultado: conversa natural, sem repetições, barata e estável!
