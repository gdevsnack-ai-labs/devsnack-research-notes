# Research Board row proposal

이 문서는 DevSnack production에 적용하지 않은 정적 Board 구조 제안이다. DB migration·API 변경·production UI 변경을 포함하지 않는다.

## Row schema

```json
{
  "researched_date": "YYYY-MM-DD",
  "published_date": "YYYY-MM-DD",
  "category": "agents",
  "title": "Oh My Hermes (OMH)",
  "summary": "Hermes 운영 레이어를 격리 profile에서 검증할 후보.",
  "status": "experiment-candidate",
  "external_url": "https://gdevsnack-ai-labs.github.io/devsnack-research-notes/notes/oh-my-hermes-omh-hermes-agent.html",
  "promoted_asset_url": null
}
```

## Field meaning

- `researched_date`: 실제 조사 기준 날짜. 원문에 별도 조사일이 없으면 원문 게시일을 사용하고 Note의 `date_basis`로 식별한다.
- `published_date`: Research Notebook 공개 날짜.
- `category`: `models`, `tools`, `agents`, `media`, `infra`, `misc` 중 하나.
- `title`: Board 표시 제목.
- `summary`: 상세 내용을 복제하지 않는 한 줄 요약.
- `status`: 조사·실험 상태. `research-complete`는 실험 완료가 아니다.
- `external_url`: GitHub Pages 상세 Note.
- `promoted_asset_url`: 독립 DevSnack 자산으로 승격된 경우에만 입력하며, 그 전에는 `null`.

## Static snapshot implementation

- GitHub Pages의 `data/research-notes.json`을 공개 manifest로 생성한다.
- DevSnack에는 필요한 필드만 정적 TypeScript snapshot으로 복사한다.
- snapshot 갱신은 source manifest와 row count·title·URL을 대조한 뒤 별도 커밋으로 수행한다.
- DB schema, Supabase row, API write는 사용하지 않는다.

## URL relationship

- 기존 DevSnack Research URL은 원문 provenance로 유지한다.
- Board `external_url`은 GitHub Pages로 연결한다.
- `promoted_asset_url`은 실제 자산이 존재하고 독립적인 가치가 검증된 뒤에만 채운다.
- 기존 URL redirect는 Note·Board·UI·sitemap 검증 이후 별도 변경으로 적용한다.

## Pilot-to-main mapping

| title | category | status | external_url |
|---|---|---|---|
| DeepSeek Harness (dsh) | agents | research-complete | `/notes/deepseek-harness-dsh.html` |
| Oh My Hermes (OMH) | agents | experiment-candidate | `/notes/oh-my-hermes-omh.html` |
| DFlash 2 + Qwen3.8-27B | models | experiment-candidate | `/notes/dflash-2-qwen3-8-27b.html` |
| FLUX 3 | media | research-complete | `/notes/flux-3.html` |
