---
title: "TokenChaser 벤치마크 프롬프트 팩 + 자체 설계 Self Bench Pack — GB10 로컬 LLM 테스트"
researched_date: "2026-08-18"
published_date: "2026-08-30"
category: "tools"
status: "experiment-candidate"
summary: "외부 84개 프롬프트를 참고해 자체 24개 팩과 실행·검증기를 준비했지만 전체 실행은 남아 있다."
direct_execution: "실행기 구축과 베타 일부 실행은 있음; 전체 팩 실행 안 함"
direct_measurement: "베타 관찰은 있으나 전체 비교 측정 안 함"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/tokenchaser-self-bench-pack-gb10-llm"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

TokenChaser Lab Note에서 수집한 프롬프트 구조와 DevSnack용 Self Bench Pack 설계·검증 루프를 정리했다.

## 확인한 내용

- 외부 84개 프롬프트를 정제하고 24개 자체 프롬프트로 확장한 기록이 있다.
- KO+EN 이중언어, 한글 폰트, UTF-8, Self-Test & Verification Loop를 공통 요구로 둔다.
- 오픈코드 실행기와 HTML 검사기가 구축되었고 베타 2회에서 루프 동작이 확인됐다고 기록되어 있다.
- 전체 24개 실행과 점수화는 다음 단계로 남아 있다.

## 확인하지 못한 내용

- 전체 24개 프롬프트 실행
- 모델별 점수·반복 재현성
- 실제 품질·창의성 비교
- 전체 결과의 DevSnack Lab 승격 가치

## 직접 실행 여부

실행기 구축과 베타 일부 실행은 있음; 전체 팩 실행 안 함

## 직접 측정 여부

베타 관찰은 있으나 전체 비교 측정 안 함

## 다음 실험/검증 계획

1. 동일 GB10·8080 backend에서 24개를 실행한다.
2. 이중언어·반응형·기능·자기검증 결과를 분리해 점수화한다.
3. 모델 비교 결과가 독립 자산이 될 만큼 재현되는지 확인한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/tokenchaser-self-bench-pack-gb10-llm)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/tokenchaser-self-bench-pack-gb10-llm

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
