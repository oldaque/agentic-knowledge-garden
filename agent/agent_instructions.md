# Agent Instructions

Objetivo: transformar brain dumps em objetos navegáveis sem perder a nota raiz como fonte de verdade. Cada operação deve atualizar o manifesto (`data/content_manifest.json`) para manter Home, Brain Dump e seções sincronizadas.

## Entrada Aceita
- Texto livre com título, fonte e resumo dos insights.
- Payload YAML no padrão:
  ```yaml
  nota: "texto livre obrigatório"
  titulo: "Multi Agent Framework"   # obrigatório
  fonte:
    tipo: linkedin|paper|...        # obrigatório
    autor: "Nome"                   # obrigatório se externo
    org: "IA Overflow"
    url: "https://..."              # obrigatório se externo
  tags: [memory, dedup]
  temas: [reasoning/core]
  status: draft|in-review|stable
  pedir_snippet: false
  ```

## Workflow Determinístico
1. **Validar schemas**  
   - Conferir `$schema` com `head` (`head -n 1 docs/notes/2025-*.md`).  
   - Garantir que front matter contém `summary`, `themes`, `updated_at`, `relationships` conforme `docs/<section>/section_file_schema.yml`.

2. **Criar ou atualizar nota (Brain Dump)**  
   - Usar seções padrão: `Overview`, `Brain Dump`, `Highlights`, `Test Ideas`, `Destilado`, `Next Steps`.  
   - `relationships.promotes_to` aponta para caminhos relativos (ex.: `patterns/memory/...md`).

3. **Checar duplicidade antes de promover**  
   - `rg --files docs/notes | xargs -I{} head -n 5 {}` para procurar `slug`/`url`.  
   - Revisar `data/content_manifest.json` (ou executar o script com `--quiet` e validar diff seco).

4. **Promover conforme classificação**  
   - `patterns/`: preencher `Problem`, `Pattern`, `Trade_offs`, `When_to_use`, `Minimal_example`, `Further_reading`.  
   - `guide/`: construir narrativa com `Objective`, `Core_concepts`, `Content`, `Further_reading`.  
  - `resources/links.md`: cada item precisa de `summary`, `type`, `origin_note`, `added_at`.  
  - `snippets/`: manter `origin_note`, `languages`, `how_to_run`.  
  - `examples/`: arquivos em `examples/<slug>/README.md` com front matter completo.

5. **Sincronizar manifesto e páginas dinâmicas**  
   - Executar `python3 scripts/build_manifest.py --quiet`.  
   - Confirmar que `docs/index.md` e os `README.md` de cada seção foram regenerados com os cards.

6. **Verificações finais**  
   - `rg "$schema" docs -g"*.md"` para garantir que nenhum arquivo ficou sem schema atualizado.  
   - Revisar cards gerados no Brain Dump e em Patterns para assegurar links válidos.

## Regras Essenciais
- Nada de códigos extensos: apenas snippets curtos e contextualizados.  
- Preserve a nota raiz; derivados sempre carregam `origin_note`.  
- Nunca sobrescreva conteúdo existente sem checar o manifesto e o schema correspondente.  
- Utilize caminhos relativos (`notes/...`, `patterns/...`) nos relacionamentos para compatibilidade com o manifesto.

## Comandos Úteis
- `rg --files docs/notes | xargs head -n 1` → inspeção rápida de schemas.  
- `python3 scripts/build_manifest.py` → recalcula manifesto e UI dinâmica.  
- `rg "origin_note" docs/patterns -g"*.md"` → valida backlinks.  
- `jq '.items[] | select(.type=="note") | .title' data/content_manifest.json` → revisar notas indexadas.
