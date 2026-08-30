---
title: "DeepSeek Harness (dsh) — Everything is a Plugin 에이전트 런타임"
researched_date: "2026-08-20"
published_date: "2026-08-30"
category: "agents"
status: "research-complete"
summary: "plugin 조합과 세션 로그를 중심으로 에이전트 실행 환경을 분해하는 Developer Preview 런타임이다."
direct_execution: "실행하지 않음"
direct_measurement: "직접 측정하지 않음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/deepseek-harness-dsh-everything-is-a-plugin"
promoted_asset_url: null
date_basis: "원문 조사 상세에 기록된 공식 소스 확인일을 사용"
---

## 조사 배경

DeepSeek Harness 공식 저장소·소개 페이지와 추가 분석 문서를 대조해 모델과 harness, plugin, sandbox, 세션 로그의 경계를 확인했다.

## 확인한 내용

- 모델·도구·스킬·세션·sandbox·storage·agent loop·UI를 교체 가능한 plugin으로 조합하는 agent harness로 설명된다.
- Cordis와 profile·bundle·patch layer를 통해 실행 구성을 조합한다.
- 모델에게 보인 context와 tool result를 session log에서 재구성하려는 원칙이 있다.
- Node.js·pnpm 기반이며 공식 실행 경로로 `npx @deepseek-ai/dsh web`이 제시되어 있다.

## 확인하지 못한 내용

- dsh의 직접 설치·benchmark 결과
- DGX Spark GB10 ARM64의 완전한 호환성
- 추가 분석 문서에 있던 context·cache·비용 절감 수치의 재현성
- Developer Preview의 변경과 plugin 공급망 위험

## 직접 실행 여부

실행하지 않음

## 직접 측정 여부

직접 측정하지 않음

## 다음 실험/검증 계획

1. 고정 commit에서 source·package lock을 확인한다.
2. profile의 plugin tree와 dump-config를 기록한다.
3. read-only 또는 workspace-write에서 최소 작업과 session replay를 확인한다.
4. custom plugin은 하나씩 추가하며 권한·네트워크·로그를 검증한다.

## Sources

- [Original DevSnack Research 원문](https://devsnack-blog.vercel.app/research/deepseek-harness-dsh-everything-is-a-plugin)
- 원문에 수록된 주요 출처:
  - [DeepSeek Harness repository](https://github.com/deepseek-ai/deepseek-harness)
  - [DeepSeek Harness 소개](https://www.deepseek.com/harness/en)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/deepseek-harness-dsh-everything-is-a-plugin

## Promotion

- 이 Note는 조사 단계 기록이다. 직접 실행·측정·적용 결과가 별도 자산으로 검증되기 전까지 `promoted_asset_url`은 `null`이다.
