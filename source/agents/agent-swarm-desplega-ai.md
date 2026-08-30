---
title: "agent-swarm (desplega-ai)"
researched_date: "2026-07-31"
published_date: "2026-08-30"
category: "agents"
status: "research-complete"
summary: "Company Agentic OS 형태의 멀티 에이전트 오케스트레이션 구조를 Hermes Kanban과 비교한 조사다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/agent-swarm-desplega-ai"
promoted_asset_url: null
date_basis: "원문 조사 상세에 기록된 2026-07-31 확인일을 사용"
---

## 조사 배경

작업 분해·worker 격리·공유 메모리·HITL gate 패턴이 기존 Hermes 운영에 참고가 되는지 비교했다.

## 확인한 내용

- 작업을 Worker Agent에 위임하고 Docker 격리 환경에서 실행하는 구조가 설명되어 있다.
- 실행 결과와 학습 내용을 공유 메모리에 기록하는 방향이 있다.
- HITL gate로 되돌릴 수 없는 단계에서 인간 승인을 기다리는 패턴을 제시한다.
- 원문 결론은 Hermes Kanban과의 구조 비교 및 참고 패턴 확인이다.

## 확인하지 못한 내용

- agent-swarm 자체 설치·실행
- 제안된 공유 메모리의 품질
- 실제 Hermes와의 통합 결과
- 멀티 에이전트 벤치마크 수치

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. Hermes Kanban의 현재 소유권·승인 경계와 패턴을 비교한다.
2. 필요할 때만 작은 HITL handoff 시나리오를 별도 실험한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/agent-swarm-desplega-ai)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/agent-swarm-desplega-ai

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
