# DevSnack Research Notebook

DevSnack Research 원문을 공개 Notebook으로 보존하는 저장소다. Note는 완성된 Knowledge 글이 아니라 조사 단계·불확실성·후속 검증을 기록한다.

## Canonical structure

```text
.
├── README.md
├── index.html                 # generated catalog
├── data/
│   └── research-notes.json    # generated public manifest
├── docs/
│   ├── migration-log-2026-08-30.md
│   ├── research-note-template.md
│   └── research-board-proposal.md
├── scripts/
│   ├── build_notebook.py      # Markdown → manifest/index/HTML
│   └── test_build_notebook.py
├── source/                    # canonical Markdown source
│   ├── agents/
│   ├── models/
│   ├── tools/
│   └── media/
└── notes/                     # generated Pages HTML; do not hand-edit
```

`source/<category>/*.md`가 canonical source이고, `notes/*.html`, `index.html`, `data/research-notes.json`은 다음 명령으로 재생성한다.

```bash
python3 scripts/build_notebook.py
python3 scripts/test_build_notebook.py -v
```

## Current migration scope

- public R1: 10건
- public R2: 11건
- M 통합 Note: 3건
- 공개 Note 합계: 24건
- draft 5건: 제외
- X `Unsloth → GGUF 변환 파이프라인`: 제외
- StockPulse·AITech output: 제외
- K1/K2: DevSnack 내부 유지

## Note metadata

각 Markdown Note는 다음 frontmatter를 가진다.

```yaml
title: "..."
researched_date: "YYYY-MM-DD"
published_date: "YYYY-MM-DD"
updated_date: "YYYY-MM-DD" # 선택 사항
category: "models | tools | agents | media | infra | misc"
status: "research-complete | experiment-candidate | awaiting-test | archived"
summary: "..."
direct_execution: "..."
direct_measurement: "..."
original_devsnack_url: "https://devsnack-blog.vercel.app/research/..."
promoted_asset_url: null
show_promotion: true # 선택 사항; 별도 승격 자산 메타를 숨길 때 false
date_basis: "..."
```

- `researched_date`: 원문에 명시된 조사일이 있으면 그 날짜. 없으면 원문 게시일을 사용하고 `date_basis`에 표시한다.
- `published_date`: 이 Notebook에 공개한 날짜.
- `updated_date`: 직접 실행·측정 결과나 중요한 내용 변경이 있었던 날짜. 변경 전 Note에는 생략할 수 있다.
- `promoted_asset_url`: 실제 DevSnack 자산으로 승격되기 전에는 `null`이며, Benchmark·Lab·Knowledge 자산으로 연결되면 해당 HTTPS URL을 기록한다.

## Category

- `models`: 모델·추론 가속·모델 비교
- `tools`: 독립 도구·유틸리티
- `agents`: 에이전트·하네스·운영 레이어
- `media`: 이미지·영상·음악·음성
- `infra`: 런타임·배포·인프라
- `misc`: 기타

## Status

- `research-complete`: 해당 조사 단계가 끝났음. 직접 실행·측정 여부는 `direct_execution`과 `direct_measurement`에서 별도로 확인한다.
- `experiment-candidate`: 후속 실행·비교 계획이 있는 후보
- `awaiting-test`: 환경·지원·권한·호환성 때문에 테스트 대기
- `archived`: 현재 우선순위가 낮고 provenance 보존만 하는 항목

R1/R2는 원본 분류이며 Status에 기계적으로 1:1 매핑하지 않는다.

## DevSnack relationship

DevSnack의 기존 Research URL은 원문 provenance로 보존한다. Board의 `external_url`은 이 저장소의 공개 Note를 가리키고, 실제 실행·측정·적용·반복 검증을 거쳐 독립 자산 가치가 생긴 경우에만 DevSnack Lab·Benchmark·Knowledge 자산을 별도로 만들고 `promoted_asset_url`을 채운다.

이번 migration은 기존 DevSnack DB·production route·redirect를 변경하지 않는다. redirect는 별도 검증 게이트 이후에만 적용한다.

## Public URL

<https://gdevsnack-ai-labs.github.io/devsnack-research-notes/>
