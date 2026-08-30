---
title: "tool-eval-bench (툴콜링 평가)"
researched_date: "2026-07-05"
published_date: "2026-08-30"
category: "tools"
status: "experiment-candidate"
summary: "결정론적 84개 툴콜링 시나리오를 기존 속도·품질 벤치에 통합하는 후보 조사다."
direct_execution: "호환성 확인만; benchmark 실행 안 함"
direct_measurement: "직접 점수 측정 없음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/tool-eval-bench"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

기존 벤치가 PP/TG와 품질은 측정하지만 툴콜링 능력은 측정하지 않는다는 문제에서 출발했다.

## 확인한 내용

- 표준 69개와 Hard Mode 15개, Pass·Partial·Fail 점수 구조가 기록되어 있다.
- vLLM·LiteLLM·llama.cpp와 `--perf`, `--trials` 실행 옵션이 언급되어 있다.
- 원문은 llama-server의 OpenAI 호환성과 tools 파라미터 확인만 기록하고 실제 벤치 실행은 하지 않았다.
- subprocess 실행·JSON 저장·profile 옵션 통합 방안이 제안되어 있다.

## 확인하지 못한 내용

- 84개 시나리오 실제 실행
- 모델별 Pass@k·품질
- 기존 benchmark pipeline 통합 결과
- 도구 호출 실패·복구의 재현성

## 직접 실행 여부

호환성 확인만; benchmark 실행 안 함

## 직접 측정 여부

직접 점수 측정 없음

## 다음 실험/검증 계획

1. 고정 llama-server에서 `--short` smoke test를 실행한다.
2. 동일 모델·시나리오를 여러 번 실행해 Pass·Partial·Fail을 저장한다.
3. 기존 benchmark와 통합할 때 결과 schema와 비용을 검증한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/tool-eval-bench)
- 원문에 수록된 주요 출처:
  - [tool-eval-bench repository](https://github.com/SeraphimSerapis/tool-eval-bench)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/tool-eval-bench

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
