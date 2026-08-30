---
title: "DFlash 2 + Qwen3.8-27B — 블록 디퓨전 병렬 드래프팅 vs MTP 비교"
researched_date: "2026-08-18"
published_date: "2026-08-30"
category: "models"
status: "experiment-candidate"
summary: "DFlash 2가 MTP 대비 높은 수락률·처리량을 보인다는 원문을 바탕으로, GB10 로컬과 H200 서버 후속 비교가 필요한 후보로 남긴다."
direct_execution: "DFlash 2는 실행하지 않음; MTP 참고 기록만 존재"
direct_measurement: "DFlash 2 직접 측정 없음; 원문 외부·기존 MTP 수치만 기록"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/dflash-2-qwen3-8-27b-vs-mtp"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

Inco AI DFlash 2와 Qwen3.8-27B MTP의 구조·수치·엔진 지원을 비교하고 로컬 적용 판단을 정리했다.

## 확인한 내용

- DFlash 2는 별도 경량 드래프터, 블록 병렬 생성, Top-16 후보 Path Selector, Two-Tap Dynamic Convolution 구조로 기록되어 있다.
- 원문에 수록된 H200 배치 1 결과는 autoregressive 대비 약 2.7~3.4배, MTP 대비 약 27~47% 추가 처리량으로 보고된다.
- Qwen3.8-27B MTP의 GB10 17~19.5 tok/s 실측이 기존 참고값으로 기록되어 있다.
- 원문 조사 시점에는 llama.cpp 지원이 PR #27342 단계였고 GB10에서는 MTP 우선으로 판단했다.

## 확인하지 못한 내용

- DFlash 2 자체의 GB10 실행
- GB10 CUDA·엔진 조합
- llama.cpp PR의 현재 merge 상태
- H200·RTX 5090 수치의 동일 조건 재현

## 직접 실행 여부

DFlash 2는 실행하지 않음; MTP 참고 기록만 존재

## 직접 측정 여부

DFlash 2 직접 측정 없음; 원문 외부·기존 MTP 수치만 기록

## 다음 실험/검증 계획

1. 지원 엔진 또는 llama.cpp 경로의 현재 상태를 확인한다.
2. 동일 모델·프롬프트 조건에서 GB10 MTP와 DFlash 2의 메모리·처리량·수락률을 비교한다.
3. 서버에서는 원문과 같은 batch·benchmark 조건을 고정한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/dflash-2-qwen3-8-27b-vs-mtp)
- 원문에 수록된 주요 출처:
  - [Inco AI DFlash 2](https://inco.ai/blog/dflash2/)
  - [DFlash 2 model](https://huggingface.co/incoai/Qwen3.8-27B-DFlash2)
  - [DFlash paper](https://arxiv.org/abs/2602.06036)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/dflash-2-qwen3-8-27b-vs-mtp

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
