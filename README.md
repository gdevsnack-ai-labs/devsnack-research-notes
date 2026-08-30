# DevSnack Research Notebook

DevSnack Research 원문 중 파일럿 4개를 공개 Notebook 형식으로 옮긴 공간이다.

이 저장소의 Note는 완성된 Knowledge 글이 아니다. 조사 당시 확인한 사실, 아직 확인하지 않은 부분, 다음 검증 계획을 분리해 기록한다.

## Pilot scope

- DeepSeek Harness (dsh)
- Oh My Hermes (OMH)
- DFlash 2 + Qwen3.8-27B
- FLUX 3

이번 단계에서는 전체 R1/R2를 이전하지 않았다. 기존 DevSnack URL·DB·production·redirect는 변경하지 않았다.

## Structure

```text
.
├── README.md
├── index.html
├── docs/
│   ├── research-note-template.md
│   └── research-board-proposal.md
└── notes/
    ├── deepseek-harness-dsh.html
    ├── oh-my-hermes-omh.html
    ├── dflash-2-qwen3-8-27b.html
    └── flux-3.html
```

- `notes/`: GitHub Pages에서 직접 공개하는 파일럿 Note
- `docs/research-note-template.md`: 다음 Note에 사용할 최소 필드 템플릿
- `docs/research-board-proposal.md`: DevSnack Research Board 행 구조 제안. 구현·DB 변경은 하지 않았다.

## Research Note fields

각 Note는 다음 순서를 따른다.

1. 제목
2. 날짜
3. Category
4. Status
5. 한 줄 요약
6. 조사 배경
7. 확인한 내용
8. 아직 확인하지 않은 내용
9. 다음 실험/검증 계획
10. Sources
11. Original DevSnack URL

## Category rules

- `models`: 모델, 추론 가속, 모델 비교
- `tools`: 독립 도구·유틸리티
- `agents`: 에이전트, 하네스, 운영 레이어
- `media`: 이미지·영상·음악·음성
- `infra`: 런타임·배포·인프라
- `misc`: 위 분류에 속하지 않는 항목

## Status rules

- `research-complete`: 원문 조사는 끝났지만 직접 실행·측정은 없음
- `experiment-candidate`: 후속 실행·비교 계획이 있고 실험 후보로 남김
- `awaiting-test`: 실행 조건이나 환경을 기다리는 상태
- `archived`: 현재 공개·실험 우선순위가 낮아 보존만 하는 상태

## Original DevSnack relationship

각 Note는 기존 DevSnack Research 원문을 삭제하거나 대체하지 않는다. 상세 원문과 기존 route는 `Original DevSnack URL`로 보존하고, GitHub Pages URL은 공개 Notebook의 외부 URL로 사용한다. 실제 결과가 생기면 별도의 DevSnack Lab·Benchmark·Knowledge 자산으로 승격하고 `promoted_asset_url`로 연결하는 방식을 제안한다.

## Public URL

<https://gdevsnack-ai-labs.github.io/devsnack-research-notes/>
