---
title: "Download-only Models Triage — Ternary-Bonsai-27B · Qwopus 3.6-27B"
researched_date: "2026-07-30"
published_date: "2026-08-30"
category: "models"
status: "archived"
summary: "다운로드·백업 보관은 확인됐지만 benchmark·실사용 결과가 없어 개별 Note 대신 triage로 통합 보존한다."
direct_execution: "다운로드·백업 보관 기록만; 실제 모델 실행 안 함"
direct_measurement: "직접 benchmark·실측 없음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/ternary-bonsai-27b"
promoted_asset_url: null
date_basis: "통합 대상 원문 중 최신 게시일을 사용"
---

## 조사 배경

중복되는 download-only 모델 페이지를 합쳐, 실제 설치·실행·측정과 단순 파일 보관을 구분했다.

## 확인한 내용

- Ternary-Bonsai-27B는 ternary 약 1.71bpw·약 7.2GB·262K context로 조사됐다.
- Qwopus 3.6-27B는 여러 GGUF·NVFP4·MTP 변형과 약 100GB 규모가 기록되어 있다.
- 두 원문 모두 백업·다운로드 보관 중심이며 주력 모델 대비 실사용 결과는 없다.

## 확인하지 못한 내용

- 현재 파일의 무결성과 실제 로드
- coding·tool call 품질
- 양자화 변형 간 직접 비교
- 주력 모델로 쓸 실질적 가치

## 직접 실행 여부

다운로드·백업 보관 기록만; 실제 모델 실행 안 함

## 직접 측정 여부

직접 benchmark·실측 없음

## 다음 실험/검증 계획

1. 파일 보관 상태와 checksum을 확인하되 자동으로 주력 모델로 채택하지 않는다.
2. 실험 가치가 다시 생길 때 특정 변형 하나만 고정해 별도 모델 테스트를 만든다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/ternary-bonsai-27b)
- 원문에 수록된 주요 출처:
  - [Ternary-Bonsai-27B](https://devsnack-blog.vercel.app/research/ternary-bonsai-27b)
  - [Qwopus 3.6-27B](https://devsnack-blog.vercel.app/research/qwopus-3-6-27b)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/ternary-bonsai-27b

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
