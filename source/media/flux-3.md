---
title: "FLUX 3 (Black Forest Labs 멀티모달)"
researched_date: "2026-08-12"
published_date: "2026-08-30"
category: "media"
status: "research-complete"
summary: "이미지·비디오·오디오·액션을 통합하고 최대 20초 영상을 내세우지만, 조사 시점에는 오픈웨이트가 없어 API 보조 후보였다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음; 원문 수치는 벤더·외부 자료"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/flux-3-black-forest-labs"
promoted_asset_url: null
date_basis: "원문 조사 상세의 2026-08-12 조사일을 사용"
---

## 조사 배경

Black Forest Labs Early Access 모델의 기능·API 비용·오픈웨이트·GB10 적용성을 기존 LTX-2.5 워크플로우와 비교했다.

## 확인한 내용

- Self-Flow 기반 이미지·비디오·오디오·액션 통합 멀티모달 모델로 소개되어 있다.
- 최대 20초 영상, 네이티브 오디오, 멀티샷·키프레임·다국어 대화·립싱크·타이포그래피·Draft 모드가 기록되어 있다.
- 가격과 benchmark는 원문에 수록된 API·BFL 자체 보고 자료로 표시되어 있다.
- 오픈웨이트·HF 웨이트가 없어 GB10 로컬은 불가하고 LTX-2.5 우선·FLUX 3 API 보조로 판단했다.

## 확인하지 못한 내용

- 직접 API 호출 및 품질·비용·latency 측정
- 한국 지역 API 접근성
- 오픈웨이트 공개 시점과 GB10 실행 조건
- 서드파티 무료 크레딧 서비스

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음; 원문 수치는 벤더·외부 자료

## 다음 실험/검증 계획

1. 공식 Early Access/API 접근과 지역 조건을 확인한다.
2. 접근 가능할 때 짧은 T2V·V2V smoke test를 비용·시간·오디오와 함께 기록한다.
3. 오픈웨이트가 공개되면 그때 GB10 로컬을 검증한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/flux-3-black-forest-labs)
- 원문에 수록된 주요 출처:
  - [BFL official blog](https://bfl.ai/blog/flux-3)
  - [BFL model page](https://bfl.ai/models/flux-3)
  - [BFL pricing](https://bfl.ai/pricing)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/flux-3-black-forest-labs

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
