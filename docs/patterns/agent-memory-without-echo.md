title: "Padrão: Memória de Agente Sem Eco"
slug: "agent-memory-without-echo"
tags: ["memory", "agent", "deduplication", "idempotency", "langgraph", "redis", "celery", "duckdb", "guardrails"]
themes: ["memory", "conversation-quality", "operations"]
source:
  origin_note: "notes/2025-10-13_agent-memory-without-echo.md"
  author: "Oldaque Rios"
  org: "Agentic Knowledge Garden"
  url: null
status: "draft"
last_update: "2025-10-13"
summary: "Este padrão descreve um conjunto de técnicas para prevenir que agentes de IA repitam respostas, garantindo conversas mais naturais e eficientes. Ele aborda o problema do 'eco' através de uma arquitetura que combina memória validada, grafos de estados, armazenamento distribuído, e processamento assíncrono."
relationships:
  snippets: []
  examples: []
  resources:
    - "resources/links.md"
---

### Problem

Agentes de IA, especialmente em interações contínuas, tendem a gerar respostas repetitivas ou ficar presos em um "eco", onde o mesmo conteúdo é reenviado a cada turno. Isso geralmente ocorre devido a três causas principais:
1.  **Reenvio do Histórico Bruto:** O histórico completo da conversa é enviado ao LLM a cada nova interação, causando redundância.
2.  **Escrita Concorrente na Memória:** Múltiplos processos ou threads tentam atualizar o estado da memória do agente simultaneamente, levando a condições de corrida e estados inconsistentes.
3.  **Ausência de Controles de Idempotência:** A mesma operação (como uma chamada de API ou atualização de memória) é executada várias vezes sem um mecanismo para garantir que o resultado seja o mesmo após a primeira execução.

### Pattern

Para resolver o problema do "eco", aplicamos uma arquitetura de sistema que separa o fluxo de resposta síncrono do gerenciamento de memória assíncrono, utilizando um conjunto de ferramentas e técnicas para garantir a consistência e a eficiência dos dados.

O padrão consiste nos seguintes componentes:

1.  **Memória Tipada e Validada (PydanticAI):** Em vez de usar strings soltas, a memória do agente (episódica, resumo, variáveis) é estruturada com tipos definidos e validações para garantir a integridade.

2.  **Grafo de Estados (LangGraph):** A lógica da conversa é modelada como um grafo de estados, onde cada nó representa uma etapa do processamento. O `MemorySaver()` e os checkpoints garantem que apenas o estado essencial seja passado adiante, reduzindo a carga de informação.

3.  **Armazenamento de Sessão com Locks (Redis):** Um armazenamento rápido como o Redis é usado para gerenciar sessões de usuário e implementar locks distribuídos (`SET NX` com TTL), garantindo que apenas uma operação de escrita na memória ocorra por turno de conversa.

4.  **Contexto Estruturado (DuckDB):** Documentos e dados de contexto são armazenados em um formato estruturado e de baixo custo, evitando o reprocessamento a cada interação.

5.  **Guardrails de Saída:** Antes de enviar a resposta final ao usuário, aplicam-se validações como:
    *   Deduplicação por hash do conteúdo.
    *   Filtros para barrar repetições óbvias.
    *   Políticas de estilo e formatação.

6.  **Orquestração Assíncrona (Celery):** Tarefas que não precisam estar no caminho crítico da resposta são delegadas a um sistema de filas assíncrono:
    *   **Write-behind:** A atualização da memória de longo prazo (resumos, embeddings) ocorre em background.
    *   **Idempotência:** Chaves de idempotência (ex: `session_id:turn_id`) previnem a execução de jobs duplicados.
    *   **Controle de Taxa e Retentativas:** Gerenciamento de chamadas a serviços externos (LLMs, bancos de vetores) com políticas de `rate limit` e `retry`.
    - **Debounce:** Agrupamento de eventos rápidos (ex: múltiplas edições do usuário) em uma única tarefa de atualização.

**Fluxo recomendado**
1. Usuário envia mensagem → LangGraph processa o mínimo necessário de contexto.
2. Resposta é entregue ao usuário sem aguardar tarefas caras.
3. Celery enfileira write-behind (resumos, embeddings, métricas) com chave de idempotência.
4. Redis garante exclusão mútua do turno e protege contra duplicidade.
5. DuckDB/índices são atualizados uma única vez por turno.
6. Guardrails avaliam a próxima saída antes de ser emitida.

### Trade_offs

- **Pró:** Latência percebida baixa porque a resposta ao usuário não espera persistência de memória.
- **Pró:** Locks + idempotência deixam o estado consistente mesmo com múltiplos workers.
- **Contra:** Arquitetura adiciona componentes (Redis, filas, checkpoints) que precisam de observabilidade dedicada.
- **Contra:** Requer engenharia cuidadosa de reprocessamento para lidar com falhas nas tarefas assíncronas.

### When_to_use

- Agents orientados a diálogo que precisam manter contexto confiável em sessões longas.
- Ambientes multiusuário com alta concorrência de escrita e risco de duplicação de respostas.
- Plataformas que diferenciam strictamente o SLA de resposta do SLA de persistência de memória.

### Minimal_example

```python
turn_id = f"{session_id}:{message_id}"

with redis.lock(name=turn_id, timeout=5):
    state = memory_saver.checkpoint(session_id)
    response = langgraph_executor.run(state, message)

if not guardrails.is_duplicate(response.text):
    send_to_user(response.text)
    celery_app.send_task(
        "memory.write_behind",
        kwargs={
            "turn_id": turn_id,
            "summary": response.summary,
            "embeddings": response.embeddings,
        },
        task_id=turn_id,  # idempotência
    )
```

### Further_reading

- [LinkedIn: Memória do agente sem “eco”](https://www.linkedin.com/feed/update/urn:li:activity:7383532727225987072)
- [LangGraph MemorySaver](https://python.langchain.com/docs/langgraph/concepts/memory/)
- [Celery Best Practices](https://docs.celeryq.dev/en/stable/userguide/tasks.html#chord-and-chain-shortcuts)
