# Agent Instructions

Objetivo: a partir de uma **nota** criada pelo usuário, organizar o conteúdo no repositório seguindo o modelo Knowledge Garden com toque de awesome‑list e cookbook. Não gerar código além de **snippets** quando explicitamente solicitado pela nota.

## Input
Entrada aberta em linguagem natural ou YAML. Exemplos:

Texto livre:
"Vi um post no LinkedIn sobre memória sem eco, autor Anderson Amaral, fala sobre deduplicação e janela semântica, link X. Quero nota."

YAML opcional:
```

nota:                   # OBRIGATORIO
titulo: "Multi Agent Framework"
fonte:  # OBRIGATORIO
tipo: linkedin
autor: "Author Name"    # OBRIGATORIO
org: "IA Overflow"
url: "https://..."      # OBRIGATORIO
tags: [memory, dedup]
conteudo_bruto: |
Resumo livre, tópicos de interesse, citações curtas.
pedir_snippet: false

```

## Processo
1. **Criar ou atualizar nota** em `docs/notes/` com o schema da seção.
2. **Verificar duplicidade**
   - Pesquisar por `slug`, `url` de origem e similaridade de título.
   - Se existir item equivalente em `docs/`, anexar como atualização em vez de criar novo.
3. **Classificar** o conteúdo
   - **docs/patterns** quando descrever um padrão recorrente com problema, forças e trade‑offs.
   - **docs/guide** quando explicar um tópico base do conhecimento.
   - **docs/resources** quando a nota é principalmente uma referência de link ou pessoa.
   - **docs/snippets** quando houver demonstração curta de código necessária para fixar a ideia.
   - **docs/examples** quando a nota solicitar um exemplo mínimo funcional.
4. **Promover por cópia** conforme necessário, seguindo os schemas de cada seção.
5. **Atualizar índices** internos de cada seção se os schemas pedirem.

## Regras
- Não criar arquivos redundantes. Conferir antes de escrever.
- Não gerar código completo. Apenas **snippets** quando indicado.
- Manter front‑matter completo, com `status: draft | in-review | stable`.
- Preservar a nota original como fonte de verdade. Promoções referenciam a nota.