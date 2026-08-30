---
title: "Qwen3.8-2.4T-A95B (Qwen3.8-Max 오픈웨이트)"
researched_date: "2026-08-12"
published_date: "2026-08-30"
category: "models"
status: "research-complete"
summary: "대규모 Qwen3.8 오픈웨이트와 클라우드 Max를 구분한 조사이며 GB10 로컬 실행 후보는 아니다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/qwen3-8-2-4t-a95b-qwen3-8-max"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

오픈웨이트와 Qwen3.8-Max의 구조·벤치마크·라이선스·GB10 적용성을 구분해 기록했다.

## 확인한 내용

- 2.4T total/95B active MoE와 262K context로 소개되어 있다.
- 오픈웨이트와 클라우드 Max의 비전·thinking·context 차이를 구분했다.
- 벤치마크 표가 오픈웨이트 자체 실측이 아니라 클라우드 Max 기준일 수 있음을 명시했다.
- GB10 로컬은 불가하고 Qwen3.8-27B가 실질적인 후속 후보로 기록되어 있다.

## 확인하지 못한 내용

- 오픈웨이트 자체의 직접 실행·benchmark
- GB10 실행
- Qwen3.8-27B 출시 후 동일 조건 비교
- 라이선스·가격의 최신 상태

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. 대규모 웨이트는 로컬 실행 대상으로 확대하지 않는다.
2. 비교가 필요하면 Qwen3.8-27B 등 실제 로컬 후보를 별도 실험한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/qwen3-8-2-4t-a95b-qwen3-8-max)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/qwen3-8-2-4t-a95b-qwen3-8-max

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
