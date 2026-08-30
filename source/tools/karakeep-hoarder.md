---
title: "Karakeep — 북마크-에브리씽 셀프호스팅 앱 (구 Hoarder)"
researched_date: "2026-08-13"
published_date: "2026-08-30"
category: "tools"
status: "experiment-candidate"
summary: "링크·노트·이미지·PDF를 저장하고 로컬 LLM으로 태깅·검색하는 셀프호스팅 수집 도구 후보다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/karakeep-hoarder"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

Research 자료와 블로그 소재를 모으는 개인 수집 파이프라인에 Karakeep을 적용할 가능성을 조사했다.

## 확인한 내용

- 북마크·노트·이미지·PDF 저장, AI 태깅·요약, 전문·의미 검색, RSS·OCR·아카이브 기능이 기록되어 있다.
- OpenAI와 Ollama 등 로컬 LLM backend를 선택할 수 있다고 원문은 정리한다.
- Docker 셀프호스팅과 CLI·REST API·웹훅 통합 표면이 있다.
- Hermes 친화성과 GB10 로컬 LLM 태깅 가능성을 후보 가치로 판단했다.

## 확인하지 못한 내용

- 실제 self-host 운영
- Ollama·로컬 LLM 태깅 품질
- Hermes 공식 skill의 현재 동작
- 저장·검색·아카이브의 장기 비용

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. Docker Compose로 격리 설치하고 데이터 저장 경계를 확인한다.
2. 소량의 공개 Research URL을 넣어 태깅·검색·아카이브를 확인한다.
3. 운영 가치와 백업·업데이트 비용을 비교한 뒤 도입 여부를 판단한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/karakeep-hoarder)
- 원문에 수록된 주요 출처:
  - [Karakeep](https://karakeep.app)
  - [Karakeep agentic skills](https://docs.karakeep.app/integrations/agentic-skills)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/karakeep-hoarder

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
