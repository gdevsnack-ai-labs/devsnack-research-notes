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
        if metadata.get("updated_date") is not None:
            date.fromisoformat(str(metadata["updated_date"]))
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
    if metadata.get("updated_date") is not None and (not isinstance(metadata["updated_date"], str) or not metadata["updated_date"].strip()):
        raise ValueError(f"{path}: updated_date must be a non-empty string when present")


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


STATUS_LABELS = {
    "research-complete": "조사 완료",
    "experiment-candidate": "실험 후보",
    "awaiting-test": "테스트 대기",
    "archived": "보관됨",
}
CATEGORY_LABELS = {
    "models": "Models",
    "tools": "Tools",
    "agents": "Agents",
    "media": "Media",
    "infra": "Infra",
    "misc": "Misc",
}
STATUS_CLASSES = {
    "research-complete": "status-research-complete",
    "experiment-candidate": "status-experiment-candidate",
    "awaiting-test": "status-awaiting-test",
    "archived": "status-archived",
}


def status_label(status: str) -> str:
    return STATUS_LABELS.get(status, status)


def metadata_html(record: dict[str, Any]) -> str:
    fields = [
        ("조사일", record["researched_date"]),
        ("게시일", record["published_date"]),
        ("분류", CATEGORY_LABELS.get(record["category"], record["category"])),
        ("상태", record["status"]),
        ("직접 실행", record["direct_execution"]),
        ("직접 측정", record["direct_measurement"]),
        ("날짜 기준", record["date_basis"]),
        ("승격 자산", record["promoted_asset_url"] or "아직 없음 (별도 자산 미생성)"),
    ]
    if record.get("updated_date"):
        fields.insert(2, ("업데이트", record["updated_date"]))
    rows: list[str] = []
    for label, value in fields:
        if label == "상태":
            value_html = (
                f'<span class="status-chip {STATUS_CLASSES.get(str(value), "status-archived")}"'
                f'>{html.escape(status_label(str(value)))}</span>'
            )
        elif label == "승격 자산" and record["promoted_asset_url"]:
            href = html.escape(str(record["promoted_asset_url"]), quote=True)
            value_html = f'<a href="{href}">별도 자산 열기 ↗</a>'
        else:
            value_html = html.escape(str(value))
        rows.append(f'<div class="meta-item"><dt>{html.escape(label)}</dt><dd>{value_html}</dd></div>')
    return f'<dl class="meta-list">{"".join(rows)}</dl>'


def render_note(record: dict[str, Any]) -> str:
    body_html = markdown_to_html(record["body"])
    title = html.escape(record["title"], quote=True)
    summary = html.escape(record["summary"], quote=True)
    canonical = html.escape(record["external_url"], quote=True)
    category = html.escape(str(CATEGORY_LABELS.get(record["category"], record["category"])))
    status = record["status"]
    status_class = STATUS_CLASSES.get(status, "status-archived")
    status_text = html.escape(status_label(status))
    original_url = html.escape(record["original_devsnack_url"], quote=True)
    scope_text = "실제 실행·측정 결과와 아직 확인하지 못한 부분을 함께 기록했다." if record.get("promoted_asset_url") else "조사한 내용과 아직 확인하지 못한 부분을 함께 기록했다."
    plan_text = "추가 측정 계획은 다음 variant 검증을 위한 메모로 남겼다." if record.get("promoted_asset_url") else "계획은 완료된 결과가 아니라 다음 검증을 위한 메모로 남겼다."
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="index,follow">
  <meta name="description" content="{summary}">
  <meta name="author" content="DevSnack Research">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title} — DevSnack Research Notebook">
  <meta property="og:description" content="{summary}">
  <meta property="og:url" content="{canonical}">
  <title>{title} — DevSnack Research Notebook</title>
  <link rel="stylesheet" href="../assets/notebook.css">
</head>
<body>
  <div class="site-shell">
    <header class="site-header">
      <div class="topbar">
        <a class="back-link" href="../index.html">← Research Notebook</a>
        <a class="brand-link" href="https://devsnack-blog.vercel.app/research">DevSnack Research ↗</a>
      </div>
      <p class="eyebrow">Research Note / {category}</p>
      <div class="title-row">
        <div class="title-block">
          <h1>{title}</h1>
          <p class="lede">{summary}</p>
        </div>
        <span class="status-chip {status_class}">{status_text}</span>
      </div>
    </header>

    <main class="note-layout">
      <aside class="meta-card" aria-label="Research note metadata">
        <div class="meta-card-inner">
          <p class="card-kicker">At a glance</p>
          {metadata_html(record)}
          <div class="scope-note">
            <strong>Research-stage Note</strong>
            직접 실행·측정 여부를 확인하고 읽어주세요.
          </div>
        </div>
      </aside>

      <article class="note-content">
        <div class="content-intro">
          <p class="section-kicker">Notebook entry</p>
          <p>{scope_text} {plan_text}</p>
        </div>
        {body_html}
      </article>
    </main>

    <footer class="site-footer">
      <p><a href="{original_url}">Original DevSnack URL ↗</a></p>
      <p>DevSnack Research Notebook · {html.escape(str(record["published_date"]))}</p>
    </footer>
  </div>
</body>
</html>
'''


def render_index(records: list[dict[str, Any]]) -> str:
    items = []
    for record in records:
        output_path = html.escape(record["output_path"], quote=True)
        title = inline_markdown(record["title"])
        summary = inline_markdown(record["summary"])
        category = html.escape(str(CATEGORY_LABELS.get(record["category"], record["category"])))
        status = record["status"]
        status_class = STATUS_CLASSES.get(status, "status-archived")
        status_text = html.escape(status_label(status))
        items.append(
            f'<li class="note-card">'
            f'<div class="note-card-top"><span class="note-category">{category}</span>'
            f'<span class="status-chip {status_class}">{status_text}</span></div>'
            f'<a class="note-card-title" href="{output_path}">{title}</a>'
            f'<p class="note-card-summary">{summary}</p>'
            f'<span class="read-link">Read note →</span>'
            f'</li>'
        )
    joined_items = "\n      ".join(items)
    return f'''<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="index,follow">
  <meta name="description" content="조사 단계의 기술 메모와 후속 검증 계획을 공개하는 DevSnack Research Notebook">
  <link rel="stylesheet" href="assets/notebook.css">
  <title>DevSnack Research Notebook</title>
</head>
<body>
  <div class="site-shell index-page">
    <header class="site-header">
      <div class="topbar">
        <a class="back-link" href="https://devsnack-blog.vercel.app/research">← DevSnack Research</a>
        <a class="brand-link" href="data/research-notes.json">JSON manifest ↗</a>
      </div>
      <p class="eyebrow">Public research archive</p>
      <h1>Research Notebook</h1>
      <p class="lede">조사 단계의 기술 메모와 후속 검증 계획을 공개한다. 완성된 Knowledge 글과는 다른 속도로 움직이는 기록이다.</p>
    </header>

    <main>
      <div class="index-actions">
        <p class="index-intro">공식 문서에서 확인한 사실, 아직 실행하지 않은 가설, 다음에 검증할 질문을 한곳에 모았다.</p>
        <span class="stats-line">총 {len(records)}개 Note · <a href="https://github.com/gdevsnack-ai-labs/devsnack-research-notes">source repository ↗</a></span>
      </div>
      <ul class="note-grid" aria-label="Research Notes">
      {joined_items}
      </ul>
    </main>

    <footer class="site-footer">
      <p>DevSnack Research Notebook</p>
      <p>공개 Note는 조사 상태와 한계를 함께 표시한다.</p>
    </footer>
  </div>
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
