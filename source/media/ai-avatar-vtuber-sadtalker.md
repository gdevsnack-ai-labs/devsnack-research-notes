---
title: "AI Avatar / VTuber (SadTalker 등)"
researched_date: "2026-07-04"
published_date: "2026-08-30"
category: "media"
status: "awaiting-test"
summary: "TTS+아바타 영상 자동화 후보를 조사했지만 ARM64 로컬 의존성과 실제 생성은 확인 전이다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 품질 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/ai-avatar-vtuber-sadtalker"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 조사 배경

페이스리스 YouTube 정보 영상에 TTS와 아바타 영상을 결합하는 후보를 클라우드·로컬·ARM64 관점에서 조사했다.

## 확인한 내용

- Opentown Studio 같은 웹 기반 옵션과 SadTalker·Wav2Lip·MuseTalk·LivePortrait를 비교했다.
- Hugging Face SadTalker Spaces 등 설치 없는 클라우드 옵션과 로컬 의존성 복잡성을 구분했다.
- 원문은 Qwen3.6-35B→Qwen3-TTS→SadTalker 흐름을 현실적인 후보로 제안한다.
- SadTalker의 오래된 의존성과 dlib·face_alignment 컴파일 문제가 위험 요소로 기록되어 있다.

## 확인하지 못한 내용

- 실제 아바타 영상 생성
- 최신 PyTorch와 GB10 ARM64의 재현성
- 클라우드 무료 옵션의 사용 제한·품질
- 자동화 파이프라인 운영 안정성

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 품질 측정하지 않음

## 다음 실험/검증 계획

1. 먼저 웹 기반 단일 샘플을 실행해 입력·출력·라이선스를 확인한다.
2. 로컬 검토가 필요할 때만 작은 이미지+오디오 테스트로 ARM64 의존성을 확인한다.
3. 대량 자동화는 품질·사용 제한과 개인정보 처리를 검토한 뒤 결정한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/ai-avatar-vtuber-sadtalker)
- 원문에 수록된 주요 출처:
  - [SadTalker repository](https://github.com/OpenTalker/SadTalker)
  - [SadTalker HF Space](https://huggingface.co/spaces/vinthony/SadTalker)
  - [Opentown Studio](https://studio.opentown.ai/)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/ai-avatar-vtuber-sadtalker

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
