---
title: "Oh My Hermes (OMH) — Hermes Agent 운영 레이어"
researched_date: "2026-08-19"
published_date: "2026-08-30"
category: "agents"
status: "experiment-candidate"
summary: "Hermes를 대체하는 에이전트가 아니라 workflow·routing·handoff·evidence 경계를 보강하는 운영 레이어다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/oh-my-hermes-omh-hermes-agent"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

`rlaope/oh-my-hermes`를 기준으로 공식 README·설치·아키텍처 문서를 대조하고, 기존 Hermes 설정을 보존한 격리 도입 가능성을 검토했다.

## 확인한 내용

- Hermes의 자연어 대화·native delegation을 유지하면서 요청 분류·계획·handoff·상태 구분을 보강한다.
- 원문 기준 102개 skill 디렉터리와 8개 `ulw-` workflow가 기록되어 있으나 이는 카탈로그 규모이지 성능 결과가 아니다.
- `Plan · not run`과 `Test · verified`처럼 준비·실행 보고·검증을 구분한다.
- full profile보다 별도 profile의 core 설치와 `doctor`부터 시작하는 방안을 제안한다.

## 확인하지 못한 내용

- 현재 Hermes v0.20.2 환경에 설치·handoff하지 않았다.
- Hermes v0.20.2와 GB10 ARM64의 호환성
- 문맥 비용·latency·검증 누락률 변화
- OMH model routing이 실제 dispatch를 보장하는지

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. 현재 Hermes 설정·provider·메모리 상태를 기록한다.
2. commit SHA를 고정한 별도 profile에서 `omh setup --core`와 `omh doctor`를 실행한다.
3. 모델 routing을 바꾸지 않고 작은 handoff 1건을 A/B 비교한다.
4. turn·tool call·검증 누락률·문맥 비용을 비교한 뒤 필요한 workflow만 확대한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/oh-my-hermes-omh-hermes-agent)
- 원문에 수록된 주요 출처:
  - [OMH repository](https://github.com/rlaope/oh-my-hermes)
  - [OMH documentation](https://rlaope.github.io/oh-my-hermes/)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/oh-my-hermes-omh-hermes-agent

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
