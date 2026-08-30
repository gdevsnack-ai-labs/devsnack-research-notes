---
title: "Airy Studio (에어리 스튜디오) — 무료 웹 TTS"
researched_date: "2026-08-18"
published_date: "2026-08-30"
category: "media"
status: "research-complete"
summary: "무료 웹 TTS와 공개 voice 목록 API를 조사했지만 API·SDK와 음질은 확인 전이다."
direct_execution: "웹/API 구조 확인만; 생성 파이프라인 실행 안 함"
direct_measurement: "직접 품질 측정 안 함"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/airy-studio-tts"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

웹 기반 다중 보이스 TTS가 기존 로컬 TTS와 보완 관계인지, 자동화 연결이 가능한지 조사했다.

## 확인한 내용

- 브라우저에서 음성 생성·다운로드를 제공하는 웹 TTS로 소개되어 있다.
- 원문은 100종 한·영 보이스, 최대 50줄 대화, WAV 다운로드와 0.2초 TTFB를 서비스 설명으로 기록한다.
- voice 목록 API는 확인됐지만 개발자 API·SDK는 계획 단계로 분류했다.
- 대량 자동화는 로컬 TTS를 유지하고 소량 다중 보이스 생성만 후보로 판단했다.

## 확인하지 못한 내용

- 음질·자연스러움의 직접 청취
- 공식 API·SDK 공개 여부
- 대량 자동화와 사용량 제한
- GB10 자원 사용 여부 외의 운영 안정성

## 직접 실행 여부

웹/API 구조 확인만; 생성 파이프라인 실행 안 함

## 직접 측정 여부

직접 품질 측정 안 함

## 다음 실험/검증 계획

1. 공식 API·SDK 공개 여부를 다시 확인한다.
2. 접근 가능한 경우 짧은 한국어·영어·다중 보이스 샘플만 비교한다.
3. 자동화 연결은 API·약관·사용량 제한이 확인된 뒤 검토한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/airy-studio-tts)
- 원문에 수록된 주요 출처:
  - [Airy Studio](https://airy.so/studio)
  - [Voice list API](https://api.outofset.com/v1/studio/voices)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/airy-studio-tts

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
