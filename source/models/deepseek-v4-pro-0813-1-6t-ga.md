---
title: "DeepSeek V4 Pro 0813 (1.6T 플래그십 GA)"
researched_date: "2026-08-12"
published_date: "2026-08-30"
category: "models"
status: "research-complete"
summary: "API 중심의 플래그십 GA와 비용·컨텍스트 조사를 정리했으며 0813 오픈웨이트의 GB10 실행은 대상이 아니다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/deepseek-v4-pro-0813-1-6t-ga"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

DeepSeek V4 Pro 0813의 GA 상태와 API·오픈웨이트·Hermes 사용 가능성을 조사했다.

## 확인한 내용

- 1.6T total/49B active MoE, 하이브리드 attention, 1M context로 소개되어 있다.
- 원문은 공식·커뮤니티 benchmark와 API 가격을 구분해 기록한다.
- 0813 웨이트는 미공개이며 GB10은 API 전용으로 판단했다.
- Hermes가 사용하는 deepseek-v4-flash와의 관계를 API 전환 검토 후보로만 남겼다.

## 확인하지 못한 내용

- 0813 오픈웨이트 공개
- GB10 로컬 실행
- 현재 API 가격·접근성의 재확인
- 실제 Hermes provider 전환 결과

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. 오픈웨이트 또는 API 정책이 바뀔 때만 재검토한다.
2. provider 전환은 별도 승인·비용·품질 비교 없이 진행하지 않는다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/deepseek-v4-pro-0813-1-6t-ga)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/deepseek-v4-pro-0813-1-6t-ga

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
