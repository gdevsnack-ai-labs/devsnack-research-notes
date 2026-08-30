---
title: "TencentDB Agent Memory — 텐센트 에이전트 메모리 시스템"
researched_date: "2026-08-11"
published_date: "2026-08-30"
category: "agents"
status: "experiment-candidate"
summary: "Mermaid 기반 단기 메모리 오프로딩과 L0~L3 계층 기억을 결합한 로컬 우선 에이전트 메모리 조사다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/tencentdb-agent-memory"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

TencentDB의 에이전트 메모리 구조와 Hermes 기본 메모리와의 역할 중복 가능성을 검토했다.

## 확인한 내용

- Task Canvas/Mermaid 기반 단기 메모리와 L0~L3 계층 장기 기억을 제안한다.
- SQLite와 sqlite-vec를 기본 backend로 하며 완전 로컬 실행을 지향한다.
- 원문은 WideSearch·PersonaMem 수치와 토큰 절감 수치를 공식 발표로 구분한다.
- Hermes와 연결할 gateway 경로가 언급되지만 별도 시스템으로 역할 분담이 필요하다.

## 확인하지 못한 내용

- GB10 ARM64에서의 실제 설치
- Hermes gateway 연결과 첫 요청
- 공식 benchmark의 독립 재현
- v2.0 팀 기능의 실제 운영성

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. SQLite/sqlite-vec와 ARM64 조건을 별도로 확인한다.
2. Hermes 메모리와 중복되지 않는 격리 profile에서 gateway 경로를 시험한다.
3. 장시간 세션에서 Mermaid canvas와 계층 기억의 비용·회수 품질을 비교한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/tencentdb-agent-memory)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/tencentdb-agent-memory

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
