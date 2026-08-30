# Research Note template

> Research Note는 완성된 Knowledge 글이 아니라 조사 단계의 공개 기록이다.

```yaml
title: ""
researched_date: "YYYY-MM-DD"
published_date: "YYYY-MM-DD"
category: "models | tools | agents | media | infra | misc"
status: "research-complete | experiment-candidate | awaiting-test | archived"
summary: "한 줄 요약"
direct_execution: "실행 여부를 명시"
direct_measurement: "측정 여부를 명시"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/..."
promoted_asset_url: null
date_basis: "조사일의 근거 또는 원문 게시일 대체 사용 사유"
```

## 조사 배경

원문에서 정의한 조사 목적과 범위를 적는다.

## 확인한 내용

원문과 원문에 수록된 출처에서 확인한 사실·관찰을 적는다. 외부·벤더·커뮤니티 수치는 출처의 성격을 표시한다.

## 확인하지 못한 내용

직접 설치·실행·측정하지 않은 항목, 호환성·재현성·접근 권한 등 불확실성을 적는다.

## 직접 실행 여부

실행했다면 범위와 한계를, 실행하지 않았다면 그 사실을 적는다.

## 직접 측정 여부

자체 측정인지, 원문에 수록된 외부·기존 기록인지 구분한다.

## 다음 실험/검증 계획

계획을 완료된 결과처럼 쓰지 않는다. 환경·조건·측정 항목을 적는다.

## Sources

원문에 수록된 출처와 provenance 링크를 적는다. 새 조사를 추가하지 않았다면 Original DevSnack URL을 1차 원천으로 명시한다.

## Original DevSnack URL

기존 원문 route를 삭제·대체하지 않고 그대로 보존한다.

## Promotion

직접 실행 성공·실패, 직접 측정 수치, 실제 적용, 비교 실험, 재현 가능한 방법, 반복 검증, DevSnack 환경 고유 판단, 독립 페이지 가치가 함께 확인될 때만 별도 DevSnack 자산을 검토한다. 단 한 번의 테스트만으로 자동 승격하지 않는다. 승격 전 `promoted_asset_url`은 `null`이다.
