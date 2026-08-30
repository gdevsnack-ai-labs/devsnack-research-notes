---
title: "Herdr — 에이전트 런타임/멀티플렉서 (YC F26)"
researched_date: "2026-08-12"
published_date: "2026-08-30"
category: "agents"
status: "awaiting-test"
summary: "여러 AI 에이전트의 상태와 pane을 관리하는 Rust 기반 런타임으로, Hermes와 보완 관계인지 확인이 필요한 조사 후보다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/herdr-yc-f26"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

멀티 에이전트 터미널 런타임의 기능과 Hermes와의 레이어 차이, ARM64 적용성을 조사했다.

## 확인한 내용

- working·blocked·idle·done 상태 감지와 CLI·Socket API 기반 조율 구조가 기록되어 있다.
- Hermes Agent를 감지 가능한 에이전트로 문서에 등재한 사례가 원문에 있다.
- Hermes는 도구·메모리·크론·스킬·위임을 담당하고 Herdr은 에이전트가 실행되는 런타임으로 구분했다.

## 확인하지 못한 내용

- GB10 ARM64 네이티브 지원
- 실제 Hermes 세션을 Herdr에서 호스팅한 결과
- herdr.org 및 herdr.dev와의 관계
- 사이트 티저 페이지의 실제 내용

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. 공식 저장소와 고정 release의 ARM64 빌드 가능성을 확인한다.
2. 작은 Hermes 세션을 attach하고 상태 감지·Socket API를 확인한다.
3. 로컬 Unix socket과 SSH 원격 attach의 권한·복구 동작을 검증한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/herdr-yc-f26)
- 원문에 수록된 주요 출처:
  - [Herdr repository](https://github.com/ogulcantuna/herdr)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/herdr-yc-f26

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
