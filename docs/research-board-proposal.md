# Research Board row proposal

이 문서는 DevSnack production에 구현하지 않은 구조 제안이다. DB migration, API 변경, UI 변경, 기존 URL 변경은 포함하지 않는다.

## Minimal row

```json
{
  "date": "YYYY-MM-DD",
  "category": "models|tools|agents|media|infra|misc",
  "title": "Research Note title",
  "summary": "One-line summary",
  "status": "research-complete|experiment-candidate|awaiting-test|archived",
  "external_url": "https://gdevsnack-ai-labs.github.io/devsnack-research-notes/notes/example.html",
  "promoted_asset_url": null
}
```

## Field meaning

- `date`: Research Note가 DevSnack에 공개된 기준 날짜. ISO `YYYY-MM-DD` 형식.
- `category`: Note 분류. `models`, `tools`, `agents`, `media`, `infra`, `misc` 중 하나.
- `title`: Note 제목.
- `summary`: Board에 표시할 한 줄 요약. 상세 조사 내용을 복제하지 않는다.
- `status`: 조사·실험 상태. `research-complete`는 조사 완료이지 실험 완료를 뜻하지 않는다.
- `external_url`: 원문 상세를 담은 GitHub Pages Note URL.
- `promoted_asset_url`: 후속 실험 결과가 별도의 DevSnack Lab·Benchmark·Knowledge 자산으로 승격된 경우에만 채운다. 아직은 `null`.

## URL relationship

- 기존 DevSnack Research URL은 삭제·redirect하지 않는다.
- GitHub Pages `external_url`은 공개 Notebook으로 연결한다.
- 기존 원문 URL은 각 Note의 `Original DevSnack URL`에서 계속 보존한다.
- 실험 결과가 생기기 전에는 `promoted_asset_url`을 추정하거나 임의로 만들지 않는다.

## Pilot mapping

| title | category | status | external_url |
|---|---|---|---|
| DeepSeek Harness (dsh) | agents | research-complete | `/notes/deepseek-harness-dsh.html` |
| Oh My Hermes (OMH) | agents | experiment-candidate | `/notes/oh-my-hermes-omh.html` |
| DFlash 2 + Qwen3.8-27B | models | experiment-candidate | `/notes/dflash-2-qwen3-8-27b.html` |
| FLUX 3 | media | research-complete | `/notes/flux-3.html` |
