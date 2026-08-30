---
title: "ACE-Step 리페인트 (Repaint)"
researched_date: "2026-07-02"
published_date: "2026-08-30"
category: "media"
status: "experiment-candidate"
summary: "기존 오디오 일부만 다시 생성하는 가이드이며, 원본 prompt·가사 재투입 조건을 실제로 검증해야 한다."
direct_execution: "가이드 확인만; 실제 repaint 적용 안 함"
direct_measurement: "직접 음질 측정 안 함"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/ace-step-repaint"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

ACE-Step 1.5의 특정 구간 재생성 원리와 API payload, 기존 곡의 결말·도입부 수정 사용 사례를 조사했다.

## 확인한 내용

- 마스크 구간만 다시 생성하고 앞뒤 오디오 맥락을 사용한다.
- 원본 prompt와 전체 가사를 다시 넣어야 일관성이 유지된다고 기록되어 있다.
- `conservative` mode와 0.4~0.6 strength를 우선하는 가이드가 있다.
- 서버 최초 요청 lazy-load와 결과 파일 직접 확인 등 운영 주의점이 기록되어 있다.

## 확인하지 못한 내용

- DevSnack 곡에 실제 repaint 적용
- 구간 경계·음질의 청취 검증
- API polling과 output file 보존의 안정성
- 다양한 BPM·key·언어 재현성

## 직접 실행 여부

가이드 확인만; 실제 repaint 적용 안 함

## 직접 측정 여부

직접 음질 측정 안 함

## 다음 실험/검증 계획

1. 보존 가능한 테스트 오디오와 원본 prompt·가사를 고정한다.
2. 10초 구간 한 건을 conservative 설정으로 실행한다.
3. 경계·음질·파일 보존을 확인한 뒤 실제 곡 적용 여부를 판단한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/ace-step-repaint)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/ace-step-repaint

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
