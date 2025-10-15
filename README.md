# Agentic Knowledge Garden

Brain dump evolutivo sobre agentes de IA transformado em um jardim navegável de padrões, guias, recursos e exemplos.

- 🌐 Site: https://oldaque.github.io/agentic-knowledge-garden/
- 🧪 Tudo nasce em notas (`docs/notes`) e promove conhecimento reutilizável.
- 🎴 A navegação é dinâmica: cards minimalistas destacam os últimos updates e promoções.

## Organização da Navegação
- **Brain Dump** → notas raiz, acessíveis pela lateral (`notes/README.md` e subitens).
- **Patterns** → agrupados por tema (Memory & Context, Reasoning & Planning, etc.).
- **Guides / Examples / Snippets / Resources** → cada seção tem overview + itens listados individualmente no menu lateral.
- Landing page traz destaques recentes, mas toda navegação é possível pelo sidebar sem depender de cards.

## Fluxo de Atualização
1. Crie/edite a nota em `docs/notes/<data>_<slug>.md` seguindo o schema (`Overview`, `Brain Dump`, `Highlights`, `Test Ideas`, `Destilado`, `Next Steps`, `relationships`).
2. Promova o conteúdo (patterns, guides, snippets, resources, examples) mantendo o campo `origin_note`.
3. Rode o sincronizador para atualizar manifesto e cards:
   ```bash
   python3 scripts/build_manifest.py
   ```
4. Visualize localmente com MkDocs (a navegação lateral é atualizada via `mkdocs.yml`):
   ```bash
   mkdocs serve
   ```

## Estrutura rápida
- `docs/index.md`: landing page gerada a partir do manifesto com pílulas recentes.
- `docs/notes/`: Brain Dump (fonte de verdade).
- `docs/patterns/`, `docs/guide/`, `docs/resources/`, `docs/snippets/`, `docs/examples/`: conteúdo promovido.
- `data/content_manifest.json`: snapshot utilizado para navegação dinâmica.
- `scripts/build_manifest.py`: gera manifesto, home e índices com cards.
- `mkdocs.yml`: define o agrupamento exibido na navegação lateral.

## Boas práticas
- Sempre valide schemas (`section_file_schema.yml`) antes de criar novos arquivos.
- Utilize `TODO.md` para registrar planos de exemplos/atravessamento antes de implementar.
- Execute `python3 scripts/build_manifest.py --quiet` antes de fazer commit para garantir que o manifesto e os cards estejam sincronizados.

Sinta-se à vontade para explorar, abrir PRs ou sugerir novos padrões. Fixe a nota raiz e o jardim se reorganiza sozinho. 🌱
