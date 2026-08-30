---
title: "Wan-Dancer-14B (Music-to-Dance)"
researched_date: "2026-08-07"
published_date: "2026-08-30"
category: "media"
status: "awaiting-test"
summary: "사진과 음악으로 댄스 영상을 만드는 워크플로우는 준비됐지만 서브그래프 flatten 문제로 실행 대기 중이다."
direct_execution: "파일·워크플로우 준비만 완료; 웹 UI 실행 대기"
direct_measurement: "직접 생성 측정 없음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/wan-dancer-14b-music-to-dance"
promoted_asset_url: null
date_basis: "원문 조사 상세의 2026-08-07 조사일을 사용"
---

## 조사 배경

Wan-Dancer의 모델·워크플로우·GB10 메모리 가능성과 ComfyUI 실행 경계를 조사했다.

## 확인한 내용

- 사진+음악→댄스 영상 모델이며 Apache-2.0으로 기록되어 있다.
- FP8 모델·워크플로우·관련 파일 준비가 완료된 상태로 기록되어 있다.
- GB10 통합 메모리에는 적재 가능성이 있지만 스텝 수 때문에 실사용 적합성은 별도 판단이다.
- 웹 UI의 서브그래프 인스턴스화와 widgets_values flatten 문제가 API 제출을 막고 있다.

## 확인하지 못한 내용

- 서브그래프 flatten 위젯 매핑 해결
- 실제 queue 제출과 영상 생성
- 4-step distill의 호환성과 시간 단축
- 생성 품질·음악-동작 정합성

## 직접 실행 여부

파일·워크플로우 준비만 완료; 웹 UI 실행 대기

## 직접 측정 여부

직접 생성 측정 없음

## 다음 실험/검증 계획

1. 웹 UI에서 워크플로우를 로드해 queue까지 도달하는지 확인한다.
2. 실행 후 global/local 단계·스텝·메모리·생성 시간을 기록한다.
3. distill 조합은 기본 실행이 재현된 뒤에만 비교한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/wan-dancer-14b-music-to-dance)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/wan-dancer-14b-music-to-dance

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
