---
title: "MiniMax H3 Turbo LoRA — 4-Step 가속 3종 비교 + 2-Stage 샘플링"
researched_date: "2026-08-13"
published_date: "2026-08-30"
category: "media"
status: "experiment-candidate"
summary: "구세대 4-step 실패 기록과 새 LoRA·2-stage 조합을 분리해, GB10 재테스트 후보로 남긴다."
direct_execution: "기존·구세대 결과 일부만 존재; 권장 조합은 실행하지 않음"
direct_measurement: "기존 기록은 있으나 새 조합 직접 측정 없음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/minimax-h3-turbo-lora-4-step-3-2-stage"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

MiniMax H3 I2V·FL2VA Turbo LoRA 조합과 2-stage sampling이 영상 품질·생성 시간에 미치는 영향을 원문 기록으로 검토했다.

## 확인한 내용

- RTX 4090 기준 5초 영상 생성 시간이 8분 29초에서 1분 38초로 줄었다는 원문 수치가 있다.
- DRBF와 larryvrh 계열의 step·weight·품질 차이를 비교했다.
- 기존 GB10 4-step 테스트는 blur·화면 깨짐으로 LTX 2.3 유지 결론이었다.
- v4 step600 EMA·6~8 step·2-stage 조합은 후속 재테스트 가치로만 제안됐다.

## 확인하지 못한 내용

- 새 권장 조합의 GB10 실행
- 현재 LoRA와 scheduler의 호환성
- 2-stage가 품질·시간을 동시에 개선하는지
- 오디오·립싱크·모션의 반복 재현성

## 직접 실행 여부

기존·구세대 결과 일부만 존재; 권장 조합은 실행하지 않음

## 직접 측정 여부

기존 기록은 있으나 새 조합 직접 측정 없음

## 다음 실험/검증 계획

1. v4 step600 EMA와 권장 6~8 step 조합을 고정한다.
2. 5초·10초 동일 입력으로 기존 LTX baseline과 시간·품질·실패를 비교한다.
3. 재현 결과가 반복될 때만 pipeline 적용을 검토한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/minimax-h3-turbo-lora-4-step-3-2-stage)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/minimax-h3-turbo-lora-4-step-3-2-stage

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
