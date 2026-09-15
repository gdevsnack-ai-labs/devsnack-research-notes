---
title: "tool-eval-bench (툴콜링 평가)"
researched_date: "2026-07-05"
published_date: "2026-08-30"
category: "tools"
status: "experiment-candidate"
summary: "LLM이 도구를 고르고, 인자를 채우고, 여러 호출을 이어가는 능력을 재현 가능한 방식으로 확인하는 69개 표준 시나리오 기반 평가 도구다."
direct_execution: "호환성과 공식 문서만 확인; benchmark 실행 안 함"
direct_measurement: "직접 점수 측정 없음"
original_devsnack_url: "https://devsnack-blog.vercel.app/research/tool-eval-bench"
promoted_asset_url: null
date_basis: "원문 게시일을 researched_date로 사용"
---

## 이 도구를 찾아본 이유

기존에 쓰던 벤치마크는 prompt를 얼마나 빨리 읽고 답을 얼마나 빨리 생성하는지, 그리고 지식·코딩 문제를 얼마나 잘 푸는지는 보여줬다. 그런데 실제 에이전트 작업에서는 그 앞에 다른 문제가 하나 더 있다. 모델이 **도구를 호출해야 하는지 판단하고, 맞는 도구를 고르고, 인자를 정확히 채우고, 앞선 결과를 다음 호출에 연결하는가** 하는 문제다.

tool-eval-bench는 이 부분을 따로 확인하기 위한 도구다. 단순히 함수 호출 JSON이 문법적으로 맞는지만 보는 게 아니라, 여러 번의 대화와 mock tool 응답을 따라가면서 도구 선택, 인자, 순서, 복구, 안전 경계를 함께 본다.

다만 이 도구가 측정하는 범위는 분명하다. 한 assistant와 mock tool 사이의 대화 흐름을 평가하는 것이지, 여러 독립 agent의 위임·handoff·조직 운영 전체를 평가하는 도구는 아니다. localization 시나리오도 현재는 독일어 중심이고, 난이도 tier는 모델 간 순위를 실측해 보정한 값이 아니라 작성자가 정한 분류다.

## 현재 공식 저장소에서 확인한 범위

처음 이 도구를 조사했을 때 원문에는 표준 69개와 Hard Mode 15개를 합쳐 84개라고 기록돼 있었다. 이후 공식 저장소의 현재 `main` 문서를 다시 확인해보니 Hard Mode가 19개로 늘어났다. 현재 기준으로는 **표준 69개 + 선택형 Hard Mode 19개 = 최대 88개 시나리오**다. Hard Mode는 기본 실행에 포함되지 않고 `--hardmode`를 붙였을 때 들어간다.

표준 시나리오는 A부터 O까지 15개 범주로 나뉜다.

- **A Tool Selection** — 요청에 맞는 도구 고르기
- **B Parameter Precision** — 타입·단위·날짜·다중값을 정확히 채우기
- **C Multi-Step Chains** — 앞선 도구 결과를 다음 호출에 연결하기
- **D Restraint & Refusal** — 도구를 쓰지 않아야 할 때 멈추기
- **E Error Recovery** — 실패한 도구 호출에서 복구하기
- **F Localization** — 언어와 시간대가 섞인 요청 처리하기
- **G Structured Reasoning** — 라우팅·추출·제약 검증하기
- **H Instruction Following** — 출력 형식과 여러 조건을 지키기
- **I Context & State** — 여러 턴의 상태와 조건을 유지하기
- **J Code Patterns** — 읽기 전 쓰기, 실행과 설명의 구분
- **K Safety & Boundaries** — 모호성, 프롬프트 인젝션, 권한 경계 확인하기
- **L Toolset Scale** — 52개 도구가 있는 큰 namespace에서 고르기
- **M Autonomous Planning** — 목표를 나누고 조건부 workflow 만들기
- **N Creative Composition** — 여러 도구와 데이터 흐름을 합성하기
- **O Structured Output** — JSON schema, enum, 중첩 구조 지키기

Hard Mode인 P는 이미 표준 시나리오에서 높은 점수를 낸 모델의 빈틈을 찾기 위한 선택 영역이다. 단순히 더 긴 질문을 주는 방식이 아니라, 상태 유지·병렬 호출·트랜잭션·페이지네이션·모호한 승인·prompt injection·복구 같은 상황을 더 강하게 만든다. 현재 문서의 예시에는 `TC-85`의 exactly-once provisioning, `TC-86`의 동시성 충돌 복구, `TC-87`의 cursor 기반 페이지네이션, `TC-88`의 후속 질문 사이 reasoning 보존이 포함돼 있다.

## 무엇을 실제로 평가하나

각 시나리오는 모델에 system prompt, 고정된 날짜가 들어간 context, 사용자 요청, 그리고 mock tool 목록을 전달한다. 도구가 반환하는 값도 일부러 깨끗하게 만들지 않는다. timestamp, ID, nested object, 불필요한 metadata 같은 잡음을 섞어서 실제 API 응답에서 필요한 값을 찾아야 하도록 만든다.

모델이 도구를 요청하면 benchmark orchestrator가 결정론적인 mock handler를 실행하고 결과를 다시 대화에 넣는다. 이 과정을 시나리오가 정한 turn limit까지 반복한 다음, 전체 trace를 evaluator가 읽는다. 그래서 최종 답변만 맞았는지보다 다음을 함께 볼 수 있다.

- 맞는 도구를 골랐는가
- 필수 인자와 단위를 정확히 전달했는가
- 앞선 결과가 필요한 호출을 올바른 순서로 했는가
- 실패나 오류 응답을 보고 안전하게 복구했는가
- 필요 없는 도구 호출이나 중복 side effect를 만들지 않았는가
- prompt injection이나 권한 상승 요청을 그대로 따르지 않았는가
- 최종 출력 schema와 형식을 지켰는가

이 구조의 장점은 실제 외부 API에 의존하지 않는다는 점이다. API 상태나 네트워크 변동 때문에 점수가 흔들리는 대신, 같은 scenario와 mock response를 반복해서 비교할 수 있다. 반대로 실제 서비스의 rate limit, 인증, 데이터 품질, 운영자 승인 같은 문제까지 재현하는 테스트는 아니다.

## 점수는 어떻게 읽어야 하나

각 시나리오는 세 단계로 채점한다.

- **PASS = 2점** — 도구·인자·흐름·최종 답변이 요구사항에 맞음
- **PARTIAL = 1점** — 일부는 맞지만 조건을 놓치거나 불필요한 호출이 있음
- **FAIL = 0점** — 잘못된 도구, 잘못된 값, hallucination, unsafe behavior 등

최종 점수는 선택된 시나리오의 총점으로 계산한다. 범주별 평균을 먼저 낸 뒤 다시 평균내는 방식이 아니라, 각 시나리오가 같은 비중을 갖는다. 따라서 시나리오가 10개인 Context & State 범주는 3개인 Tool Selection보다 전체 점수에 더 크게 반영된다.

- **90–100**: Excellent
- **75–89**: Good
- **60–74**: Adequate
- **40–59**: Weak
- **0–39**: Poor

점수 하나만 보면 놓치는 것도 있다. 실행 중 timeout, connection error, endpoint가 요청을 거부한 경우처럼 모델이 답을 만들 기회조차 얻지 못한 infrastructure failure는 일반 tool-call 점수의 0점으로 세지 않고 분모에서 제외한다. 그래서 `completion_rate`와 `excluded_scenarios`를 먼저 봐야 한다. 69개 중 60개만 실제 채점된 결과를 69개 모두 채점된 결과와 바로 비교하면 안 된다.

안전 경고도 별도로 남는다. 실제 unsafe action이나 disclosure가 관찰되고 safety group 점수가 50% 아래로 내려가면, 종합 점수가 높더라도 rating이 3 stars를 넘지 못하는 safety gate가 적용된다. 단순히 lookup을 못 했거나 답이 덜 완성됐다는 것만으로 safety violation이라고 하지는 않는다.

원하면 `--weight-by-difficulty`로 난이도 가중 점수도 함께 볼 수 있다. 다만 난이도 tier 자체가 작성자의 추정이므로, 기본 점수는 그대로 두고 가중 점수는 보조 지표로 보는 편이 맞다.

## llama.cpp에서 어떻게 연결하나

이 도구는 OpenAI 호환 `POST /v1/chat/completions` endpoint를 기준으로 한다. Tool-call 시나리오를 돌리려면 `tools`와 `tool_choice` 요청 필드를 처리할 수 있어야 한다. 공식 문서에는 vLLM, SGLang, LiteLLM, llama.cpp, NInfer와 hosted Gemini가 지원 대상으로 적혀 있다.

백엔드마다 차이는 있다. 예를 들어 llama.cpp는 버전에 따라 `tool_choice: "required"` 지원 여부가 달라질 수 있고, parallel tool calls와 streaming usage 통계는 지원되지 않는다. 52개 도구를 한꺼번에 주는 시나리오는 backend의 context window에 부담이 될 수 있다. 이런 차이는 모델 점수와 섞어 해석하지 말고, report의 capability와 completion 정보에서 따로 확인해야 한다.

설치는 `uv` 기준으로 간단하다.

- 기본 설치: `uv tool install git+https://github.com/SeraphimSerapis/tool-eval-bench.git`
- throughput 기능 포함: `uv tool install 'tool-eval-bench[perf] @ git+https://github.com/SeraphimSerapis/tool-eval-bench.git'`

처음에는 endpoint를 명시하는 편이 안전하다.

아래 명령의 `$TOOL_EVAL_BASE_URL`에는 실제로 확인할 OpenAI 호환 server endpoint를 넣는다.

- 서버 확인: `tool-eval-bench probe --base-url "$TOOL_EVAL_BASE_URL"`
- 짧은 smoke test: `tool-eval-bench run --short --base-url "$TOOL_EVAL_BASE_URL"`
- 재현 가능한 표준 실행: `tool-eval-bench run --seed 42 --base-url "$TOOL_EVAL_BASE_URL"`
- Hard Mode 포함: `tool-eval-bench run --hardmode --seed 42 --base-url "$TOOL_EVAL_BASE_URL"`
- 특정 시나리오만: `tool-eval-bench run --scenarios TC-01 TC-02 TC-03 --base-url "$TOOL_EVAL_BASE_URL"`

`--base-url`을 생략하면 common localhost port를 자동으로 찾는다. 현재 CLI 문서에는 8000, 8080, 8081, 8082, 30000, 4000, 3000, 11434, 5000 순으로 probe한다고 적혀 있다. 자동 발견에 기대기보다 실제 사용 중인 server endpoint를 지정하는 것이 나중에 결과를 재현하기 쉽다.

CI나 기존 benchmark pipeline에 붙일 때는 `--json` 또는 `--json-file results.json`을 쓰는 것이 좋다. JSON mode에서는 stdout에 result envelope가 나오고, 진행 이벤트는 stderr의 JSONL로 분리된다. `run` 명령 외에도 throughput·speculative decoding·context pressure를 다루는 `bench`, 정확도 plugin을 다루는 `plugin`, 저장 결과를 비교하는 `compare`, 중단된 실행을 잇는 `resume` 명령이 있다.

환경변수도 사용할 수 있다. 우선순위는 CLI flag, 실행 프로세스의 environment, `.env`, 자동 발견 순서다. `TOOL_EVAL_BASE_URL`, `TOOL_EVAL_MODEL`, `TOOL_EVAL_API_KEY` 등을 둘 수 있지만, API key는 공개 글이나 report에 남기면 안 된다.

## 실행 결과는 무엇으로 남나

완료된 실행은 실행 위치 기준으로 두 가지 결과를 남긴다.

- `runs/YYYY/MM/<run_id>.md` — 시나리오별 verdict와 전체 conversation trace
- `data/benchmarks.sqlite` — 다시 조회할 수 있는 SQLite 기록과 trace

각 시나리오가 끝날 때마다 SQLite에 checkpoint를 남기는 점도 괜찮았다. 중간에 Ctrl-C가 나거나 연결이 끊겨도 이미 끝난 시나리오까지 버릴 필요 없이 `resume RUN_ID`로 이어갈 수 있다. 다시 실행할 때는 run ID, label, model, backend, seed를 함께 관리해야 서로 다른 조건의 결과를 섞지 않게 된다.

비교할 때 특히 중요한 값은 `config_fingerprint`다. 이 fingerprint에는 CLI 옵션뿐 아니라 tool-eval-bench 코드의 version과 git SHA도 포함된다. server engine version, quantization, GPU 수, slot 수, speculative decoding mode 같은 deployment metadata도 비교 조건에 들어간다. 같은 모델 이름이라도 quantization이나 실행 코드가 다르면 leaderboard의 같은 cohort로 묶지 않는 이유다.

## 우리 GB10 벤치마크와는 어떻게 다른가

tool-eval-bench 자체는 아직 실행하지 않았다. 따라서 이 글에는 특정 모델의 tool-eval-bench 점수를 넣지 않는다.

대신 다른 방식으로 측정한 결과가 궁금하다면, 우리가 별도로 진행한 [DGX Spark GB10 로컬 LLM Benchmark](https://devsnack-blog.vercel.app/benchmarks)를 먼저 참고할 만하다. 그 페이지는 같은 GB10과 llama.cpp 조건에서 여러 GGUF·quantization·MTP variant를 돌리고, 속도뿐 아니라 Knowledge, Coding, Tool-call, Agent-single, Agent-multi를 나눠 비교한 기록이다.

두 결과는 같은 benchmark가 아니다. 우리 페이지의 Tool-call과 Agent 항목은 고정된 별도 evaluator와 protocol을 사용하고, tool-eval-bench는 자체 mock tool·scenario·trace·safety evaluator를 사용한다. 따라서 숫자를 합쳐서 하나의 종합 점수로 만들거나, 한쪽 결과를 다른 쪽 결과로 바꿔 읽을 수는 없다. 그래도 같은 모델을 두 방식으로 보았을 때 어떤 부분이 일치하고 어떤 부분이 달라지는지 확인하는 참고 자료로는 의미가 있다.

다음에는 GB10에서 사용했던 모델과 variant 중 일부를 같은 조건으로 tool-eval-bench에도 넣어볼 생각이다. 그때는 단순히 점수를 하나 더 추가하는 것이 아니라, 우리 기존 Tool-call·Agent 결과와 tool-eval-bench의 category·completion·safety 결과가 어디서 맞물리는지 비교해보려 한다. 이 교차 검증이 쌓이면 GB10 benchmark의 tool-use 평가 신뢰도도 지금보다 높일 수 있을 것 같다.

## 지금 단계에서의 결론

이 도구는 “모델이 tool calling을 지원한다”는 문장을 확인하는 수준에서 한 단계 더 나아간다. 올바른 도구 선택, 인자 정확도, 다중 호출, 오류 복구, 안전 경계를 같은 mock 환경에서 반복해볼 수 있다는 점이 가장 큰 장점이다. 특히 `completion_rate`, safety warning, `config_fingerprint`를 함께 남기는 구조는 단일 점수만 보여주는 간단한 테스트보다 비교에 유리하다.

반면 tool-eval-bench가 곧 실제 agent 전체의 능력을 뜻하는 것은 아니다. 한 assistant와 mock tools의 protocol이고, 독일어 중심 localization과 작성자 추정 난이도라는 한계도 있다. 실제 개발 환경에서의 파일 수정, 긴 repository 작업, 여러 agent의 역할 분담까지 판단하려면 별도 평가가 필요하다.

그래서 현재는 기존 GB10 벤치마크를 대체할 도구라기보다 **tool-call 평가를 더 촘촘하게 만들 수 있는 다음 측정 후보**로 보는 것이 맞다. 실행하지 않은 것을 실행한 것처럼 쓰지 않고, 우선 공식 구조와 한계를 정리해 둔 뒤 실제 측정 결과가 생기면 이 글에서 별도 결과 자산으로 연결할 예정이다.

## Sources

- [tool-eval-bench 공식 저장소 README](https://github.com/SeraphimSerapis/tool-eval-bench)
- [Scoring Methodology](https://github.com/SeraphimSerapis/tool-eval-bench/blob/main/docs/methodology.md)
- [Backend compatibility](https://github.com/SeraphimSerapis/tool-eval-bench/blob/main/docs/backends.md)
- [CLI reference](https://github.com/SeraphimSerapis/tool-eval-bench/blob/main/docs/cli-reference.md)
- [Run IDs, artifacts, and labels](https://github.com/SeraphimSerapis/tool-eval-bench/blob/main/docs/artifacts.md)
- [Related work](https://github.com/SeraphimSerapis/tool-eval-bench/blob/main/docs/related-work.md)
- [DGX Spark GB10 로컬 LLM Benchmark — DevSnack](https://devsnack-blog.vercel.app/benchmarks)
- [GB10 benchmark public source repository](https://github.com/gdevsnack-ai-labs/gb10-local-llm-benchmark)

## Original DevSnack URL

- https://devsnack-blog.vercel.app/research/tool-eval-bench

## Promotion

- 이 Note는 조사 단계 기록이다. tool-eval-bench 직접 실행·측정·적용·반복 검증이 별도 자산으로 확인되기 전까지 `promoted_asset_url`은 `null`이다.
