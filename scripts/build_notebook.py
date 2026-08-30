#!/usr/bin/env python3
"""Build the public DevSnack Research Notebook from Markdown sources."""

from __future__ import annotations

import html
import json
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Any

PAGES_BASE_URL = "https://gdevsnack-ai-labs.github.io/devsnack-research-notes"
VALID_CATEGORIES = {"models", "tools", "agents", "media", "infra", "misc"}
VALID_STATUSES = {
    "research-complete",
    "experiment-candidate",
    "awaiting-test",
    "archived",
}
REQUIRED_FIELDS = {
    "title",
    "researched_date",
    "published_date",
    "category",
    "status",
    "summary",
    "direct_execution",
    "direct_measurement",
    "original_devsnack_url",
    "promoted_asset_url",
    "date_basis",
}


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "null":
        return None
    if value.startswith('"') and value.endswith('"'):
        return json.loads(value)
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("Markdown source must start with YAML frontmatter")
    closing = text.find("\n---\n", 4)
    if closing < 0:
        raise ValueError("YAML frontmatter closing marker is missing")
    raw_frontmatter = text[4:closing]
    metadata: dict[str, Any] = {}
    for line in raw_frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, raw = line.split(":", 1)
        metadata[key.strip()] = parse_scalar(raw)
    return metadata, text[closing + len("\n---\n") :]


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", text)


def source_links(body: str, original_url: str) -> list[str]:
    section = re.search(r"(?ms)^## Sources\s*\n(.*?)(?=^## |\Z)", body)
    links = markdown_links(section.group(1) if section else "")
    if original_url not in links:
        links.insert(0, original_url)
    return list(dict.fromkeys(links))


def validate_metadata(metadata: dict[str, Any], path: Path) -> None:
    missing = sorted(REQUIRED_FIELDS - metadata.keys())
    if missing:
        raise ValueError(f"{path}: missing fields: {', '.join(missing)}")
    for field in ("title", "summary", "researched_date", "published_date", "category", "status", "original_devsnack_url", "date_basis"):
        if not isinstance(metadata[field], str) or not metadata[field].strip():
            raise ValueError(f"{path}: {field} must be a non-empty string")
    try:
        date.fromisoformat(metadata["researched_date"])
        date.fromisoformat(metadata["published_date"])
    except ValueError as exc:
        raise ValueError(f"{path}: dates must use YYYY-MM-DD") from exc
    if metadata["category"] not in VALID_CATEGORIES:
        raise ValueError(f"{path}: invalid category {metadata['category']!r}")
    if metadata["status"] not in VALID_STATUSES:
        raise ValueError(f"{path}: invalid status {metadata['status']!r}")
    if not metadata["original_devsnack_url"].startswith("https://"):
        raise ValueError(f"{path}: original_devsnack_url must be HTTPS")
    if metadata["promoted_asset_url"] is not None and not str(metadata["promoted_asset_url"]).startswith("https://"):
        raise ValueError(f"{path}: promoted_asset_url must be HTTPS or null")


def collect_notes(source_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(source_dir.rglob("*.md")):
        metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        validate_metadata(metadata, path)
        relative = path.relative_to(source_dir)
        expected_category = relative.parts[0]
        if expected_category != metadata["category"]:
            raise ValueError(f"{path}: directory category does not match metadata category")
        slug = path.stem
        output_path = Path("notes") / f"{slug}.html"
        records.append(
            {
                **metadata,
                "slug": slug,
                "source_path": str(Path("source") / relative),
                "output_path": str(output_path),
                "external_url": f"{PAGES_BASE_URL}/{output_path.as_posix()}",
                "sources": source_links(body, metadata["original_devsnack_url"]),
                "body": body,
            }
        )
    if not records:
        raise ValueError("No Markdown Research Notes found")
    return records


def inline_markdown(value: str) -> str:
    escaped = html.escape(value, quote=False)
    code_tokens: list[str] = []

    def code_repl(match: re.Match[str]) -> str:
        code_tokens.append(f"<code>{match.group(1)}</code>")
        return f"\x00CODE{len(code_tokens) - 1}\x00"

    escaped = re.sub(r"`([^`]+)`", code_repl, escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+|/[^)\s]+)\)",
        lambda match: f'<a href="{html.escape(match.group(2), quote=True)}">{match.group(1)}</a>',
        escaped,
    )
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    for index, token in enumerate(code_tokens):
        escaped = escaped.replace(f"\x00CODE{index}\x00", token)
    return escaped


def markdown_to_html(body: str) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    list_tag: str | None = None

    def close_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_tag
        if list_tag:
            output.append(f"</{list_tag}>")
            list_tag = None

    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            close_paragraph()
            close_list()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            close_paragraph()
            close_list()
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            continue
        bullet = re.match(r"^-\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if bullet or ordered:
            close_paragraph()
            wanted = "ul" if bullet else "ol"
            if list_tag != wanted:
                close_list()
                output.append(f"<{wanted}>")
                list_tag = wanted
            item = bullet.group(1) if bullet else ordered.group(1)
            output.append(f"<li>{inline_markdown(item)}</li>")
            continue
        close_list()
        if line.startswith("> "):
            paragraph.append(line[2:])
        else:
            paragraph.append(line)
    close_paragraph()
    close_list()
    return "\n".join(output)


def metadata_html(record: dict[str, Any]) -> str:
    fields = [
        ("제목", record["title"]),
        ("researched_date", record["researched_date"]),
        ("published_date", record["published_date"]),
        ("Category", record["category"]),
        ("Status", record["status"]),
        ("직접 실행 여부", record["direct_execution"]),
        ("직접 측정 여부", record["direct_measurement"]),
        ("date_basis", record["date_basis"]),
        ("promoted_asset_url", record["promoted_asset_url"] or "null"),
    ]
    rows = "\n".join(f"<dt>{html.escape(label)}</dt><dd>{inline_markdown(str(value))}</dd>" for label, value in fields)
    return f"<dl>\n{rows}\n</dl>"


def render_note(record: dict[str, Any]) -> str:
    body_html = markdown_to_html(record["body"])
    title = html.escape(record["title"], quote=True)
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="index,follow">
  <title>{title} — DevSnack Research Notebook</title>
</head>
<body>
  <main>
    <p><a href="../index.html">Research Notebook</a></p>
    <p><strong>Research-stage Notebook:</strong> 이 문서는 완성된 Knowledge 글이 아니라 조사·불확실성·후속 검증을 기록한 공개 Note다.</p>
    {metadata_html(record)}
    <h2>한 줄 요약</h2>
    <p>{inline_markdown(record["summary"])}</p>
    {body_html}
  </main>
</body>
</html>
'''


def render_index(records: list[dict[str, Any]]) -> str:
    items = []
    for record in records:
        items.append(
            f'<li><a href="{html.escape(record["output_path"], quote=True)}">{inline_markdown(record["title"])}</a> '
            f'— {html.escape(record["category"])} / {html.escape(record["status"])}</li>'
        )
    joined_items = "\n      ".join(items)
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="index,follow">
  <title>DevSnack Research Notebook</title>
</head>
<body>
  <main>
    <h1>DevSnack Research Notebook</h1>
    <p>조사 단계·불확실성·후속 실험을 공개하는 Research Notebook이다. 완성된 Knowledge 글 모음이 아니다.</p>
    <p>총 {len(records)}개 Note · <a href="data/research-notes.json">JSON manifest</a> · <a href="https://github.com/gdevsnack-ai-labs/devsnack-research-notes">source repository</a></p>
    <h2>Research Notes</h2>
    <ul>
      {joined_items}
    </ul>
  </main>
</body>
</html>
'''


def build_notebook(root: Path | None = None) -> list[dict[str, Any]]:
    root = root or Path(__file__).resolve().parents[1]
    source_dir = root / "source"
    notes_dir = root / "notes"
    data_dir = root / "data"
    records = collect_notes(source_dir)

    notes_dir.mkdir(parents=True, exist_ok=True)
    for old in notes_dir.glob("*.html"):
        old.unlink()
    for record in records:
        destination = root / record["output_path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render_note(record), encoding="utf-8")

    public_records = [{key: value for key, value in record.items() if key != "body"} for record in records]
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "research-notes.json").write_text(
        json.dumps(public_records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (root / "index.html").write_text(render_index(records), encoding="utf-8")
    return public_records


if __name__ == "__main__":
    built = build_notebook()
    print(json.dumps({"built": len(built), "categories": sorted({item["category"] for item in built})}, ensure_ascii=False))
