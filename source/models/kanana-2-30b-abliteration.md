---
title: "Kanana-2-30B Abliteration + 파인튜닝"
researched_date: "2026-07-24"
published_date: "2026-08-30"
category: "models"
status: "experiment-candidate"
summary: "Kanana-2-30B에 OBLITERATUS와 Unsloth LoRA를 적용하는 가이드 조사이며 실제 실행은 아직 없다."
direct_execution: "가이드만 확인; 실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/kanana-2-30b-abliteration"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

한국어 특화 Kanana-2-30B-A3B에 abliteration·fine-tuning을 적용하는 절차와 GB10 메모리 가능성을 검토했다.

## 확인한 내용

- OBLITERATUS nuclear 방법과 Unsloth LoRA 절차가 원문에 정리되어 있다.
- 원문은 128GB unified memory 환경을 전제로 실행 순서를 제안한다.
- quantization 전 abliteration, recommend 단계와 검증 순서를 강조한다.

## 확인하지 못한 내용

- OBLITERATUS 설치 여부
- abliteration 실행 결과
- LoRA 학습 결과·품질 변화
- 최적 파라미터의 재현성

## 직접 실행 여부

가이드만 확인; 실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. 먼저 `obliteratus recommend`와 설치 조건을 별도 환경에서 확인한다.
2. 작은 검증 모델로 abliteration 전후를 비교한 뒤 LoRA 확대 여부를 판단한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/kanana-2-30b-abliteration)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/kanana-2-30b-abliteration

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
