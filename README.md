# Agentic Knowledge Garden

Brain dump evolutivo sobre agentes de IA transformado em um jardim navegável de padrões, guias, recursos e exemplos.

- 🌐 Site: https://oldaque.github.io/agentic-knowledge-garden/
- 🧪 Tudo nasce em notas (`docs/notes`) e promove conhecimento reutilizável.
- 🎴 A navegação é dinâmica: cards minimalistas destacam os últimos updates e promoções.

## Como atualizar o garden
1. Crie/edite a nota em `docs/notes/<data>_<slug>.md` seguindo o schema (`Overview`, `Brain Dump`, `Highlights`, `Test Ideas`, `Destilado`, `Next Steps`).
2. Promova o conteúdo (patterns, guides, snippets, resources, examples) mantendo `origin_note`.
3. Rode o sincronizador para atualizar manifesto e páginas dinâmicas:
   ```bash
   python3 scripts/build_manifest.py
   ```
4. Visualize localmente com MkDocs:
   ```bash
   mkdocs serve
   ```

## Estrutura rápida
- `docs/index.md`: landing page gerada a partir do manifesto com pílulas recentes.
- `docs/notes/`: Brain Dump (fonte de verdade).
- `docs/patterns/`, `docs/guide/`, `docs/resources/`, `docs/snippets/`, `docs/examples/`: conteúdo promovido.
- `data/content_manifest.json`: snapshot utilizado para navegação dinâmica.
- `scripts/build_manifest.py`: gera manifesto, home e índices com cards.

Sinta-se à vontade para explorar, abrir PRs ou sugerir novos padrões. Fixe a nota raiz e o jardim se reorganiza sozinho. 🌱
