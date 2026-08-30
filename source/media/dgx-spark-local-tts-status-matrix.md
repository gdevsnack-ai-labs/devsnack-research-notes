---
title: "DGX Spark Local TTS Status Matrix"
researched_date: "2026-07-27"
published_date: "2026-08-30"
category: "media"
status: "awaiting-test"
summary: "여러 TTS 조사 페이지를 하나의 설치·실행·사양 matrix로 통합한다. 설치됨과 생성 검증됨을 구분한다."
direct_execution: "일부 설치·로드 확인 기록은 있으나 matrix 전체 생성 테스트는 안 함"
direct_measurement: "개별 사양·일부 원문 수치는 있으나 동일 protocol 비교 측정 없음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/moss-tts-gguf"
promoted_asset_url: null
date_basis: "통합 대상 원문 페이지의 게시일 범위를 사용"
---

## 조사 배경

동일한 DGX Spark TTS 현황이 여러 Research 페이지에 반복되어 M 그룹을 하나의 provenance-preserving matrix로 압축했다.

## 확인한 내용

- 원문 기준 Qwen3-TTS는 운영 중이며, Supertone·OmniVoice·MagpieTTS·MOSS 계열은 설치·weights·생성 테스트 상태가 서로 다르다.
- MOSS-TTS Family는 8B·1.7B·Realtime 2B·TTSD 8B의 용도와 사양을 설명한다.
- MOSS-TTS-GGUF는 gated 승인 필요로 미설치 상태로 기록되어 있다.
- 원문은 일부 모델의 로드 검증·크기·언어·용도와 생성 테스트 미실시를 구분한다.

## 확인하지 못한 내용

- 각 모델의 실제 생성 테스트와 품질 비교
- 한국어·zero-shot cloning·실시간 latency의 동일 조건 비교
- 현재 파일 경로·가중치의 지속성
- MOSS-TTS-GGUF 접근 승인과 실행

## 직접 실행 여부

일부 설치·로드 확인 기록은 있으나 matrix 전체 생성 테스트는 안 함

## 직접 측정 여부

개별 사양·일부 원문 수치는 있으나 동일 protocol 비교 측정 없음

## 다음 실험/검증 계획

1. 각 모델의 설치 여부를 현재 환경에서 다시 inventory한다.
2. 동일 한국어 문장·참조 음성·출력 형식으로 생성 smoke test를 한다.
3. 생성 시간·음질·메모리·장문 안정성을 분리 기록한 뒤 DevSnack 자산 승격 여부를 판단한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/moss-tts-gguf)
- 원문에 수록된 주요 출처:
  - [MOSS-TTS-GGUF](https://devsnack-blog.vercel.app/research/moss-tts-gguf)
  - [Higgs TTS 3 4B](https://devsnack-blog.vercel.app/research/higgs-tts-3-4b)
  - [NVIDIA MagpieTTS 357M](https://devsnack-blog.vercel.app/research/nvidia-magpietts-357m)
  - [OmniVoice 0.6B](https://devsnack-blog.vercel.app/research/omnivoice-0-6b)
  - [Supertone 3](https://devsnack-blog.vercel.app/research/supertone-3)
  - [MOSS-TTS Family](https://devsnack-blog.vercel.app/research/moss-tts-family-8b-1-7b-realtime-2b-ttsd-8b)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/moss-tts-gguf

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
