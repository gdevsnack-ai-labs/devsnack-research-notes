# Research migration log — 2026-08-30

## Scope

Source of truth: `outputs/devsnack-content-role-inventory-2026-08-30.md` and the existing DevSnack Research pages named by that inventory. No new external research was added. `published_date` for this migration is `2026-08-30`.

`researched_date` uses the explicit investigation date in the original where available. When the original did not expose a separate investigation date, the original DevSnack publication date was used and recorded in Note frontmatter as `date_basis`.

## Migrated public R1 — 10

1. DeepSeek Harness (dsh) → `agents/deepseek-harness-dsh.md`
2. Airy Studio → `media/airy-studio-tts.md`
3. Herdr → `agents/herdr-yc-f26.md`
4. TencentDB Agent Memory → `agents/tencentdb-agent-memory.md`
5. agent-swarm → `agents/agent-swarm-desplega-ai.md`
6. TokenChaser Lab Note pattern → `tools/tokenchaser-lab-note.md`
7. DeepSeek V4 Pro 0813 → `models/deepseek-v4-pro-0813-1-6t-ga.md`
8. Qwen3.8-2.4T-A95B → `models/qwen3-8-2-4t-a95b-qwen3-8-max.md`
9. FLUX 3 → `media/flux-3.md`
10. AI Avatar / VTuber → `media/ai-avatar-vtuber-sadtalker.md`

## Migrated public R2 — 11

1. Oh My Hermes (OMH) → `agents/oh-my-hermes-omh.md`
2. DFlash 2 + Qwen3.8-27B → `models/dflash-2-qwen3-8-27b.md`
3. TokenChaser Self Bench Pack → `tools/tokenchaser-self-bench-pack-gb10-llm.md`
4. Karakeep → `tools/karakeep-hoarder.md`
5. MiniMax H3 Turbo LoRA → `media/minimax-h3-turbo-lora-4-step-3-2-stage.md`
6. Muse Glimmer 30B → `models/muse-glimmer-30b-meta.md`
7. Wan-Dancer-14B → `media/wan-dancer-14b-music-to-dance.md`
8. Kanana-2-30B Abliteration → `models/kanana-2-30b-abliteration.md`
9. tool-eval-bench → `tools/tool-eval-bench.md`
10. PixelGPT → `media/pixelgpt-24-24-lora.md`
11. ACE-Step Repaint → `media/ace-step-repaint.md`

## Migrated M — 3 integrated Notes

- DGX Spark Local TTS Status Matrix → `media/dgx-spark-local-tts-status-matrix.md`
  - MOSS-TTS-GGUF
  - Higgs TTS 3 4B
  - NVIDIA MagpieTTS 357M
  - OmniVoice 0.6B
  - Supertone 3
  - MOSS-TTS Family
- Download-only Models Triage → `models/download-only-models-triage.md`
  - Ternary-Bonsai-27B
  - Qwopus 3.6-27B
- Media Automation Tools Comparison → `media/media-automation-tools-comparison.md`
  - HyperFrames
  - VoiceBox

Each M Note lists every source page as provenance. The underlying pages are not silently discarded.

## Excluded

- Research draft 5건: public migration excluded; remain review-queue candidates.
- X `Unsloth → GGUF 변환 파이프라인`: not migrated. Existing references were checked; the original note only records an unbuilt pipeline and no completed conversion result. Keep as delete/archive/noindex decision candidate; do not delete in this migration.
- K1/K2: retained inside DevSnack. This migration does not relocate them.
- StockPulse, AITech, and 253 external output candidates: out of scope.

## Promotion rule

A Research Note is a source-preserving research record. Create a separate DevSnack asset only when the evidence supports independent value through execution success/failure, direct measurement, actual application, comparison experiment, reproducible method, repeated validation, a DevSnack-specific finding, and a conclusion worth a separate page. A single test does not automatically promote an item. Until then `promoted_asset_url: null`; after promotion, retain the Note and connect the new asset to preserve the provenance chain.

## URL / redirect gate

This migration log records intended relationship only. Existing `/research/[slug]` routes are not redirected until:

1. every Note and source link is HTTP 200;
2. `data/research-notes.json` and DevSnack Board snapshot reconcile;
3. Knowledge UI and responsive Board pass build/runtime checks;
4. sitemap/search policy tests confirm old details are excluded only with the intended permanent redirect;
5. redirect target read-back returns HTTP 200 and no loop.

Until that gate is complete, old DevSnack URLs remain unchanged.

## Final result

The gate passed after the GitHub Pages manifest, Board snapshot, production Knowledge UI, sitemap, and link audits were verified.

- 30 migrated legacy Research slugs now return HTTP 308 with their mapped GitHub Pages `Location`.
- 24 unique GitHub Pages targets return HTTP 200.
- The production Research Board exposes 24 unique external Note links; `promoted_asset_url` remains `null` for all rows.
- The 30 legacy details are excluded from the DevSnack sitemap and the migrated details resolve to `noindex` before redirect handling.
- K1/K2 retained assets remain reachable and K2 representative URLs remain sitemap-indexable.
- Draft 5건 and X `Unsloth → GGUF 변환 파이프라인` remain outside the redirect map.
- Existing Research source rows were not deleted and are retained as redirect provenance.
