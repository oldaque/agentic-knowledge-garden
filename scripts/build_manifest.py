#!/usr/bin/env python3
"""
Builds the content manifest for the Agentic Knowledge Garden and regenerates
the landing pages (home, Brain Dump, section indexes) with dynamic cards.

The script is intentionally data-first: every Markdown page is described in the
manifest so that navigation components can stay in sync without manual edits.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - handled at runtime
    yaml = None  # Fallback handled in `_load_yaml`


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPOSITORY_ROOT / "docs"
MANIFEST_PATH = REPOSITORY_ROOT / "data" / "content_manifest.json"


def _simple_yaml_scalar(token: str) -> Any:
    token = token.strip()
    if not token:
        return ""
    if token in {"null", "Null", "NULL", "~"}:
        return None
    if token in {"true", "True", "TRUE"}:
        return True
    if token in {"false", "False", "FALSE"}:
        return False
    if token.startswith('"') and token.endswith('"'):
        return token[1:-1]
    if token.startswith("'") and token.endswith("'"):
        return token[1:-1]
    if token.startswith("[") and token.endswith("]"):
        try:
            return json.loads(token)
        except json.JSONDecodeError:
            return [item.strip() for item in token[1:-1].split(",") if item.strip()]
    try:
        if "." in token:
            return float(token)
        return int(token)
    except ValueError:
        return token


def _simple_yaml_load(raw: str) -> Any:
    lines = raw.splitlines()
    index = 0

    def parse_block(expected_indent: int) -> Dict[str, Any]:
        nonlocal index
        data: Dict[str, Any] = {}
        while index < len(lines):
            line = lines[index]
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                index += 1
                continue
            indent = len(line) - len(line.lstrip(" "))
            if indent < expected_indent:
                break
            if indent > expected_indent:
                raise ValueError(f"Unexpected indent at line {index + 1}: {line}")
            if ":" not in stripped:
                raise ValueError(f"Expected key:value at line {index + 1}: {line}")
            key, remainder = stripped.split(":", 1)
            key = key.strip()
            remainder = remainder.strip()
            index += 1
            if remainder:
                data[key] = _simple_yaml_scalar(remainder)
                continue

            # Peek next meaningful line to decide dict vs list.
            values: Any
            if index < len(lines):
                next_line = lines[index]
                while index < len(lines) and not next_line.strip():
                    index += 1
                    if index < len(lines):
                        next_line = lines[index]
                if index < len(lines):
                    next_indent = len(next_line) - len(next_line.lstrip(" "))
                    next_stripped = next_line.strip()
                    if next_stripped.startswith("- "):
                        values = parse_list(next_indent)
                    else:
                        values = parse_block(next_indent)
                else:
                    values = {}
            else:
                values = {}
            data[key] = values
        return data

    def parse_list(expected_indent: int) -> List[Any]:
        nonlocal index
        items: List[Any] = []
        while index < len(lines):
            line = lines[index]
            stripped = line.strip()
            if not stripped:
                index += 1
                continue
            indent = len(line) - len(line.lstrip(" "))
            if indent < expected_indent:
                break
            if not stripped.startswith("- "):
                break
            payload = stripped[2:].strip()
            index += 1

            # Check if payload is key:value (inline dict item)
            if payload and ":" in payload:
                # This could be an inline dict item like "- key: value"
                # or start of a nested block like "- title: value"
                # Check if next line is indented more (nested block)
                if index < len(lines):
                    next_line = lines[index]
                    if next_line.strip() and not next_line.strip().startswith("- "):
                        next_indent = len(next_line) - len(next_line.lstrip(" "))
                        if next_indent > indent:
                            # Nested block - parse the first key:value inline, then the rest as block
                            key, value = payload.split(":", 1)
                            block_data = {key.strip(): _simple_yaml_scalar(value)}
                            block_data.update(parse_block(next_indent))
                            items.append(block_data)
                            continue
                # Simple inline key:value
                items.append(_simple_yaml_scalar(payload))
            elif payload:
                items.append(_simple_yaml_scalar(payload))
            else:
                # Nested structure with empty payload
                if index >= len(lines):
                    items.append({})
                    break
                next_line = lines[index]
                next_indent = len(next_line) - len(next_line.lstrip(" "))
                if next_line.strip().startswith("- "):
                    items.append(parse_list(next_indent))
                else:
                    items.append(parse_block(next_indent))
        return items

    # Decide if root is list or dict
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and lines[index].lstrip().startswith("- "):
        return parse_list(len(lines[index]) - len(lines[index].lstrip(" ")))
    index = 0
    return parse_block(0)


def _load_yaml_any(raw: str) -> Any:
    if not raw.strip():
        return {}
    if yaml is not None:
        return yaml.safe_load(raw)
    return _simple_yaml_load(raw)


def _load_yaml(raw: str) -> Dict[str, Any]:
    """Loads YAML mapping using PyYAML when available, otherwise a minimal parser."""
    if not raw.strip():
        return {}
    loaded = _load_yaml_any(raw)
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError("Front matter must be a mapping at the top level.")
    return loaded


def _parse_markdown(path: Path) -> Tuple[Dict[str, Any], str]:
    """Returns (front_matter, body) for a Markdown file."""
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}, content
    # Split on the first two occurrences of `---`
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    _, fm_raw, rest = parts
    front_matter = _load_yaml(fm_raw)
    body = rest.lstrip("\n")
    return front_matter, body


def _ensure_date(value: Optional[str], fallback: Optional[str] = None) -> str:
    """Validates/normalises ISO dates."""
    candidate = value or fallback
    if not candidate:
        return dt.date.today().isoformat()
    try:
        # Accept both date and datetime strings.
        return dt.datetime.fromisoformat(candidate).date().isoformat()
    except ValueError:
        raise ValueError(f"Expected ISO date, got '{candidate}'")


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def _as_list(value: Optional[Any]) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def _escape_html(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def _relative_item_link(item: Dict[str, Any], *, context_path: str) -> str:
    context_dir = Path(context_path).parent
    target_path = Path(item["path"])
    relative = os.path.relpath(target_path, context_dir).replace("\\", "/")
    if relative.endswith("README.md"):
        relative = relative[: -len("README.md")]
    elif relative.endswith(".md"):
        relative = relative[: -3]
    if not relative.endswith("/"):
        relative = relative + "/"
    if not relative.startswith("."):
        return f"./{relative}"
    return relative


def _card_grid(items: List[Dict[str, Any]], *, context_path: str) -> str:
    if not items:
        return "_No entries yet._"
    lines = ['<div class="kg-grid">']
    for item in items:
        tags = item.get("tags", [])[:3]
        tag_html = "".join(
            f'<span class="kg-badge">{_escape_html(tag)}</span>' for tag in tags
        )
        link = _relative_item_link(item, context_path=context_path)
        lines.extend(
            [
                '  <div class="kg-card">',
                f'    <div class="kg-card__type">{item["type"].title()}</div>',
                f'    <h3><a href="{link}">{_escape_html(item["title"])}</a></h3>',
                f'    <p class="kg-card__summary">{_escape_html(item.get("summary", ""))}</p>',
                "    <div class=\"kg-card__meta\">",
                f'      <span class="kg-badge kg-badge--status">{_escape_html(item.get("status", "draft").title())}</span>',
                f'      <span class="kg-badge kg-badge--date">{_escape_html(item.get("updated_at", ""))}</span>',
                f"      {tag_html}",
                "    </div>",
                "  </div>",
            ]
        )
    lines.append("</div>")
    return "\n".join(lines)


@dataclass
class ManifestItem:
    id: str
    type: str
    title: str
    slug: str
    summary: str
    status: str
    tags: List[str]
    themes: List[str]
    created_at: str
    updated_at: str
    path: str
    origin_note: Optional[str]
    promotions: List[str] = field(default_factory=list)
    relationships: Dict[str, List[str]] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "slug": self.slug,
            "summary": self.summary,
            "status": self.status,
            "tags": self.tags,
            "themes": self.themes,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "path": self.path,
            "origin_note": self.origin_note,
            "promotions": self.promotions,
            "relationships": self.relationships,
        }


def _collect_markdown_items() -> List[ManifestItem]:
    items: List[ManifestItem] = []
    section_map = {
        "notes": ("note", DOCS_ROOT / "notes"),
        "patterns": ("pattern", DOCS_ROOT / "patterns"),
        "guide": ("guide", DOCS_ROOT / "guide"),
        "snippets": ("snippet", DOCS_ROOT / "snippets"),
        "examples": ("example", DOCS_ROOT / "examples"),
    }

    for section, (content_type, base_path) in section_map.items():
        for path in sorted(base_path.rglob("*.md")):
            if path.name.lower() in {"readme.md", "index.md"}:
                continue
            if path.name == "section_file_schema.yml":
                continue
            front_matter, _ = _parse_markdown(path)
            if not front_matter:
                continue

            title = front_matter.get("title") or path.stem.replace("-", " ").title()
            slug = front_matter.get("slug") or _slugify(title)
            summary = front_matter.get("summary") or ""
            tags = _as_list(front_matter.get("tags"))
            themes = _as_list(front_matter.get("themes") or front_matter.get("theme"))
            relationships = front_matter.get("relationships") or {}

            created_at = _ensure_date(front_matter.get("created_at"))
            updated_at = _ensure_date(front_matter.get("updated_at"), fallback=created_at)

            origin_note: Optional[str] = None
            if content_type == "note":
                origin_note = f"notes/{path.name}"
            else:
                origin_note = front_matter.get("origin_note") or (
                    front_matter.get("source", {}) if isinstance(front_matter.get("source"), dict) else None
                )
                if isinstance(origin_note, dict):
                    origin_note = origin_note.get("origin_note") or origin_note.get("note")

            promotes_to = []
            if content_type == "note":
                rel = front_matter.get("relationships") or {}
                promotes_to = rel.get("promotes_to") or []

            manifest_path = path.relative_to(DOCS_ROOT).as_posix()

            item = ManifestItem(
                id=f"{content_type}:{slug}",
                type=content_type,
                title=title,
                slug=slug,
                summary=summary,
                status=front_matter.get("status", "draft"),
                tags=tags,
                themes=themes or ["core/unsorted"],
                created_at=created_at,
                updated_at=updated_at,
                path=manifest_path,
                origin_note=origin_note,
                promotions=_as_list(promotes_to),
                relationships={
                    key: _as_list(value) for key, value in (relationships or {}).items()
                },
            )
            items.append(item)
    return items


def _collect_resources(items: List[ManifestItem]) -> None:
    links_path = DOCS_ROOT / "resources" / "links.md"
    if not links_path.exists():
        return
    raw = links_path.read_text(encoding="utf-8")
    raw = raw.strip()
    if not raw:
        return
    parsed = _load_yaml_any(raw)
    if not isinstance(parsed, list):
        raise ValueError("resources/links.md must contain a YAML list.")
    for entry in parsed:
        if not isinstance(entry, dict):
            continue
        title = entry.get("title")
        url = entry.get("url")
        if not title or not url:
            continue
        slug = _slugify(title)
        created_at = entry.get("added_at") or dt.date.today().isoformat()
        item = ManifestItem(
            id=f"resource:{slug}",
            type="resource",
            title=title,
            slug=slug,
            summary=entry.get("summary") or entry.get("insight") or "",
            status="curated",
            tags=_as_list(entry.get("tags")),
            themes=_as_list(entry.get("type")),
            created_at=_ensure_date(created_at),
            updated_at=_ensure_date(entry.get("added_at"), fallback=created_at),
            path="resources/links.md",
            origin_note=entry.get("origin_note") or entry.get("from_note"),
            promotions=[],
            relationships={},
        )
        items.append(item)


def build_manifest() -> Dict[str, Any]:
    items = _collect_markdown_items()
    _collect_resources(items)
    items_sorted = sorted(items, key=lambda item: (item.type, item.slug))
    manifest = {
        "version": 1,
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "items": [item.as_dict() for item in items_sorted],
    }
    return manifest


def _select(items: Iterable[Dict[str, Any]], *, item_type: Optional[str] = None) -> List[Dict[str, Any]]:
    data = [item for item in items if item_type is None or item["type"] == item_type]
    return sorted(data, key=lambda x: x.get("updated_at", ""), reverse=True)


def _format_theme(theme: str) -> str:
    cleaned = theme.replace("_", " ").replace("-", " ").replace("/", " / ")
    parts = [part.capitalize() for part in cleaned.split()]
    return " ".join(parts)


def _render_home(manifest: Dict[str, Any]) -> str:
    items = manifest["items"]
    notes = _select(items, item_type="note")[:6]
    promos = [
        item
        for item in manifest["items"]
        if item["type"] in {"pattern", "guide", "snippet", "example"}
    ]
    promos = sorted(promos, key=lambda x: x.get("updated_at", ""), reverse=True)[:6]

    overview = (
        "**Agentic Knowledge Garden** é um brain dump evolutivo sobre agentes de IA. "
        "Cada nota nasce no Brain Dump, cria conexões e promove conteúdo reutilizável."
    )

    sections = [
        "# Agentic Knowledge Garden",
        overview,
        "",
        "## Brain Dump Highlights",
        _card_grid(notes, context_path="index.md"),
        "",
        "## Freshly Promoted",
        _card_grid(promos, context_path="index.md"),
        "",
        "## Explore Pillars",
        "- Brain Dump → ideias brutas e sinais.",
        "- Patterns → soluções recorrentes comentadas.",
        "- Guides → fundamentos organizados por tema.",
        "- Resources → referências externas curadas.",
        "- Snippets → blocos de código mínimos.",
        "- Examples → fluxos reprodutíveis.",
        "",
        "> Tudo nasce de uma nota. Explore, combine, promova.",
    ]
    return "\n".join(sections) + "\n"


def _render_notes_index(manifest: Dict[str, Any]) -> str:
    notes = _select(manifest["items"], item_type="note")
    latest = notes[:8]

    sections = [
        "---",
        'title: "Brain Dump"',
        'summary: "Notas brutas que alimentam todo o jardim."',
        "---",
        "",
        "# Brain Dump",
        "Notas recentes e sinais que evoluem em padrões, guias e recursos.",
        "",
        "## Last Updates",
        _card_grid(latest, context_path="notes/README.md"),
    ]
    return "\n".join(sections) + "\n"


def _render_section_index(manifest: Dict[str, Any], *, item_type: str, heading: str, folder: str) -> str:
    items = _select(manifest["items"], item_type=item_type)
    latest = items[:8]
    sections = [
        f"# {heading}",
        "",
        "## Latest",
        _card_grid(latest, context_path=f"{folder}/README.md"),
    ]
    return "\n".join(sections) + "\n"


def regenerate_pages(manifest: Dict[str, Any]) -> None:
    _write_if_changed(MANIFEST_PATH, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    _write_if_changed(DOCS_ROOT / "index.md", _render_home(manifest))
    _write_if_changed(DOCS_ROOT / "notes" / "README.md", _render_notes_index(manifest))
    _write_if_changed(
        DOCS_ROOT / "patterns" / "README.md",
        _render_section_index(manifest, item_type="pattern", heading="Patterns", folder="patterns"),
    )
    _write_if_changed(
        DOCS_ROOT / "snippets" / "README.md",
        _render_section_index(manifest, item_type="snippet", heading="Snippets", folder="snippets"),
    )
    _write_if_changed(
        DOCS_ROOT / "examples" / "README.md",
        _render_section_index(manifest, item_type="example", heading="Examples", folder="examples"),
    )
    _write_if_changed(
        DOCS_ROOT / "guide" / "README.md",
        _render_section_index(manifest, item_type="guide", heading="Guides", folder="guide"),
    )
    _write_if_changed(
        DOCS_ROOT / "resources" / "README.md",
        _render_section_index(manifest, item_type="resource", heading="Resources", folder="resources"),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build content manifest and landing pages.")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress console output.",
    )
    args = parser.parse_args()

    manifest = build_manifest()
    regenerate_pages(manifest)

    if not args.quiet:
        print(f"Manifest generated with {len(manifest['items'])} items.")
        print(f"Wrote manifest to {MANIFEST_PATH.relative_to(REPOSITORY_ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover
        print(f"[build_manifest] error: {exc}", file=sys.stderr)
        sys.exit(1)
