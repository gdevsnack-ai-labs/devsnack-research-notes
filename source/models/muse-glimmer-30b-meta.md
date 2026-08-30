---
title: "Muse Glimmer 30B (Meta 오픈 에이전트 모델)"
researched_date: "2026-08-12"
published_date: "2026-08-30"
category: "models"
status: "experiment-candidate"
summary: "툴콜링·비전 보조 모델 후보로 GB10 fit 가능성이 조사됐지만, 직접 실행과 주력 모델 비교는 남아 있다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음; 외부·커뮤니티 수치만 기록"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/muse-glimmer-30b-meta"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

Meta의 오픈웨이트 에이전트 모델을 툴콜링·비전·GB10 메모리 관점에서 검토했다.

## 확인한 내용

- Apache 2.0 오픈웨이트 30B dense 모델과 비전 인코더로 소개되어 있다.
- 원문은 MCP Atlas·τ3-Banking·MMMU-Pro·TerminalBench 등 외부 또는 모델 카드 수치를 구분한다.
- Q4 메모리 fit과 Hermes Agent 하네스 보조 모델 가능성을 후보 판단으로 기록했다.
- 지식 작업과 속도는 주력 교체보다 비전·툴콜링 보조 관점에서 신중히 보도록 결론냈다.

## 확인하지 못한 내용

- GB10에서의 직접 실행 속도·품질
- Hermes tool call 실사용
- Qwen3.8-27B와 동일 조건 비교
- Muse Spark 1.2 공개 및 영향

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음; 외부·커뮤니티 수치만 기록

## 다음 실험/검증 계획

1. GB10에서 비전 입력과 툴콜링을 분리한 작은 테스트를 실행한다.
2. Qwen3.8-27B와 동일 prompt·provider·검증 조건으로 비교한다.
3. 속도·메모리·툴콜링 실패를 함께 기록해 보조 모델 가치만 판단한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/muse-glimmer-30b-meta)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/muse-glimmer-30b-meta

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
