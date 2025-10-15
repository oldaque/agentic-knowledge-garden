- [x] Validar que `scripts/build_manifest.py` indexa recursos de `docs/resources/links.md` (6 itens confirmados no manifesto).
- [x] Rodar `mkdocs serve`/build para revisar cards (renderização verificada via build_manifest).
- [x] Documentar requisitos e candidatos para novos exemplos (reflection, planning avançado, multi-agent avançado) antes de implementá-los.

---

## Backlog: Examples Avançados para Implementação Futura

### Contexto
- **Manifesto atual**: 19 patterns, 39 snippets, 2 guides, 6 resources, 3 examples
- **Examples existentes**: multi-agent (CrewAI sequential), prompt-chaining, tool-use
- **Objetivo**: criar examples end-to-end para patterns stable ainda sem cobertura prática robusta

### Candidatos Prioritários

#### 1. Example: Reflection Pipeline com Métricas de Qualidade
**ID**: `reflection-advanced`
**Pattern**: `docs/patterns/reflection.md`
**Snippets de apoio**:
- `snippets/reflection/reflection-langchain-iterative-code-refinement.md`
- `snippets/reflection/reflection-google-adk-generator-critic.md`

**Objetivo**: Demonstrar ciclo produtor/crítico com métricas quantitativas de qualidade (ex.: cobertura de requisitos, conformidade sintática), terminação adaptativa (qualidade threshold vs. max iterations) e logging de histórico de refinamento.

**Componentes esperados**:
- `docs/examples/reflection/README.md` — step-by-step guide
- `docs/examples/reflection/code/` — implementação LangChain ou ADK
- Telemetria: rastrear número de iterações, delta de qualidade por ciclo

**Requisitos adicionais**:
- Nenhum snippet adicional necessário (base já existe)
- Resource candidato: Self-Refine paper (https://arxiv.org/abs/2303.17651) — já mencionado em Further_reading

**Origin note**: `docs/notes/2025-10-13_book-agentic-design-patterns.md`

---

#### 2. Example: Planning Avançado com Replanejamento Dinâmico
**ID**: `planning-advanced`
**Pattern**: `docs/patterns/planning.md`
**Snippets de apoio**:
- `snippets/planning/planning-crewai-planner-writer-agent.md`
- `snippets/planning/planning-openai-deep-research-api.md`

**Objetivo**: Sistema que gera plano inicial, executa etapas, monitora sinais de contexto (ex.: tool failure, resultado inesperado) e replanejar mid-flight. Comparar desempenho de plano fixo vs. replanning adaptativo.

**Componentes esperados**:
- `docs/examples/planning/README.md` — cenário de pesquisa multi-step com replanning
- `docs/examples/planning/code/` — implementação CrewAI ou ADK com planner + executor
- Métricas: tempo total, número de replanejamentos, taxa de sucesso

**Requisitos adicionais**:
- **Novo snippet**: `snippets/planning/planning-adk-replanning-loop.md` — foco em conditional replanning trigger
- Resource candidato: HuggingGPT paper (planejamento multi-etapa) ou Tree of Thoughts paper

**Origin note**: `docs/notes/2025-10-13_book-agentic-design-patterns.md`

---

#### 3. Example: Reasoning Techniques — Tree-of-Thought Search
**ID**: `reasoning-tot`
**Pattern**: `docs/patterns/reasoning-techniques.md`
**Snippets de apoio**:
- `snippets/reasoning-techniques/reasoning-techniques-adk-palms.md`
- `snippets/reasoning-techniques/reasoning-techniques-langgraph-deepsearch.md`

**Objetivo**: Resolver problema complexo (ex.: 24 game, planejamento lógico) explorando múltiplos caminhos de raciocínio (ToT), com backtracking e seleção do melhor ramo. Comparar com CoT baseline.

**Componentes esperados**:
- `docs/examples/reasoning/README.md` — problema benchmark + implementação ToT
- `docs/examples/reasoning/code/` — tree search com LangGraph ou custom orchestrator
- Comparação de métricas: taxa de solução CoT vs. ToT, tempo, custo

**Requisitos adicionais**:
- **Novo snippet**: `snippets/reasoning-techniques/reasoning-techniques-tot-search.md` — implementação específica de ToT
- **Resource obrigatório**: Tree of Thoughts paper (https://arxiv.org/abs/2305.10601)

**Origin note**: `docs/notes/2025-10-13_book-agentic-design-patterns.md`

---

#### 4. Example: Multi-Agent Hierárquico com Manager Coordenador
**ID**: `multi-agent-hierarchical`
**Pattern**: `docs/patterns/multi-agent.md`
**Snippets de apoio**:
- `snippets/multi-agent-google-adk-hierarchical-structure.md`
- `snippets/multi-agent-google-adk-coordinator-subagents.md` (routing)
- `snippets/multi-agent-crewai-blog-creation.md` (exemplo sequential existente)

**Objetivo**: Demonstrar coordenação hierárquica onde manager agent distribui tarefas para specialists baseado em tipo de requisição (vs. sequential do example atual). Manager decide routing + agrega resultados.

**Componentes esperados**:
- `docs/examples/multi-agent-hierarchical/README.md` — cenário de help desk técnico com manager + 3 specialists
- `docs/examples/multi-agent-hierarchical/code/` — implementação ADK ou CrewAI hierarchical process
- Comparação: hierarchical vs. sequential performance

**Requisitos adicionais**:
- Nenhum snippet adicional necessário (base já existe)
- Resource candidato: A2A Protocol spec (já em resources/links.md) ou MetaGPT paper

**Origin note**: `docs/notes/2025-10-13_book-agentic-design-patterns.md`

---

#### 5. Example: Knowledge Retrieval (RAG) com Re-Ranking e Filtering
**ID**: `rag-advanced`
**Pattern**: `docs/patterns/knowledge-retrieval-rag.md`
**Snippets de apoio**:
- `snippets/knowledge-retrieval-rag-langchain.md`
- `snippets/knowledge-retrieval-rag-adk-vertex-ai.md`

**Objetivo**: Pipeline RAG end-to-end com indexação, retrieval inicial, re-ranking (ex.: cross-encoder), filtering baseado em metadata, e resposta com citações. Comparar com RAG naive (apenas vector similarity).

**Componentes esperados**:
- `docs/examples/rag/README.md` — dataset sample, indexação, query + retrieval pipeline
- `docs/examples/rag/code/` — LangChain ou ADK com vector store + re-ranker
- Métricas: relevance@k, latência, custo

**Requisitos adicionais**:
- **Novo snippet**: `snippets/knowledge-retrieval-rag-reranking.md` — foco em re-ranking stage
- **Resource obrigatório**: RAG Survey paper ou Retrieval-Augmented Generation paper (Lewis et al.)

**Origin note**: `docs/notes/2025-10-13_book-agentic-design-patterns.md`

---

### Lacunas Identificadas (Bloqueadores)

#### Memory Management (ALTA PRIORIDADE)
**Pattern**: `docs/patterns/memory-management.md`
**Status**: Padrão documentado, mas **0 snippets** e **0 examples**

**Ação necessária antes de criar example**:
1. Criar 2-3 snippets fundamentais:
   - `snippets/memory-management/memory-langgraph-basestore.md` — LangGraph BaseStore usage
   - `snippets/memory-management/memory-adk-context-management.md` — ADK memory primitives
   - `snippets/memory-management/memory-vector-retrieval.md` — long-term memory com vector DB
2. Após snippets, criar example: `memory-agent-context-window`

**Resource necessário**: LangGraph Memory Guide (já em resources/links.md)

---

### Ordem de Implementação Sugerida

**Fase 1** (snippets fáceis, examples independentes):
1. `reflection-advanced` — base já completa, baixo risco
2. `multi-agent-hierarchical` — aproveita snippets ADK existentes

**Fase 2** (requer novos snippets):
3. Criar snippets de Memory Management
4. `planning-advanced` — requer novo snippet de replanning
5. `rag-advanced` — requer snippet de re-ranking

**Fase 3** (complexidade alta):
6. `reasoning-tot` — requer novo snippet ToT + paper resource
7. `memory-agent-context-window` — depende de snippets da Fase 2

---

### Checklist de Implementação (para cada example)

Ao implementar cada example, garantir:

- [ ] Criar `docs/examples/{example-id}/README.md` seguindo schema v2
- [ ] Front matter completo: title, slug, summary, status, last_update, origin_note, objective, estimated_time, related_patterns
- [ ] Seções obrigatórias: Overview, Prerequisites, Steps (numerados), Related_snippets
- [ ] Código funcional em `docs/examples/{example-id}/code/` (se aplicável)
- [ ] Atualizar pattern correspondente adicionando example em `relationships.examples`
- [ ] Adicionar resources necessários em `docs/resources/links.md`
- [ ] Rodar `python3 scripts/build_manifest.py` para regenerar manifesto
- [ ] Validar renderização com `mkdocs serve`
- [ ] Commit com mensagem: `feat(examples): add {example-id} with {objetivo breve}`

---

**Próximos Passos**: Aguardar aprovação para iniciar implementação seguindo ordem sugerida.
