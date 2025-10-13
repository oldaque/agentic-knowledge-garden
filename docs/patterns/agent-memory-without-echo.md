---
title: "Padrão: Memória de Agente Sem Eco"
slug: "agent-memory-without-echo"
tags: ["memory", "agent", "deduplication", "idempotency", "langgraph", "redis", "celery", "duckdb", "guardrails"]
source:
  note: "/notes/2025-10-13_agent-memory-without-echo.md"
status: "draft"
last_update: "2025-10-13"
summary: "Este padrão descreve um conjunto de técnicas para prevenir que agentes de IA repitam respostas, garantindo conversas mais naturais e eficientes. Ele aborda o problema do 'eco' através de uma arquitetura que combina memória validada, grafos de estados, armazenamento distribuído, e processamento assíncrono."
---

### Problema

Agentes de IA, especialmente em interações contínuas, tendem a gerar respostas repetitivas ou ficar presos em um "eco", onde o mesmo conteúdo é reenviado a cada turno. Isso geralmente ocorre devido a três causas principais:
1.  **Reenvio do Histórico Bruto:** O histórico completo da conversa é enviado ao LLM a cada nova interação, causando redundância.
2.  **Escrita Concorrente na Memória:** Múltiplos processos ou threads tentam atualizar o estado da memória do agente simultaneamente, levando a condições de corrida e estados inconsistentes.
3.  **Ausência de Controles de Idempotência:** A mesma operação (como uma chamada de API ou atualização de memória) é executada várias vezes sem um mecanismo para garantir que o resultado seja o mesmo após a primeira execução.

### Padrão

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

### Exemplo de Fluxo

1.  O usuário envia uma mensagem.
2.  O `LangGraph` processa a entrada e gera uma resposta rápida.
3.  O `Celery` enfileira tarefas de atualização de memória (resumo, indexação).
4.  O `Redis` bloqueia escritas concorrentes para a sessão atual.
5.  Os armazenamentos de dados (`DuckDB`, índices vetoriais) são atualizados de forma segura.
6.  Os `Guardrails` validam a próxima saída para evitar duplicação.

### Quando Usar

Este padrão é ideal para qualquer sistema de agente conversacional que precise manter o contexto por múltiplos turnos e onde a qualidade da interação (fluidez, ausência de repetição) é um requisito fundamental. É especialmente útil em aplicações de alta concorrência, onde múltiplos usuários interagem simultaneamente com os agentes.

### Leituras

- [Post Original no LinkedIn por Anderson Amaral](https://www.linkedin.com/feed/update/urn:li:activity:7383532727225987072)
