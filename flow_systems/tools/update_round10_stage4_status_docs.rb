#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
RECEIPT = JSON.parse(File.binread(File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json")))
REPORT_SHA = Digest::SHA256.file(File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md")).hexdigest
RECEIPT_SHA = Digest::SHA256.file(File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json")).hexdigest

PAPERS = {
  29 => {
    dir: "29-bianchi-ideal-owner-refinement",
    counts: "11/11 items; 40 operations; 7 RESOLVED + 4 DELIBERATE_LIMITATION; 38/83 affected E1; +651 words; 14-page clean preview",
    progress: "Stage 4 makes the five prospective Gate-M/Gate-Q interfaces, exact inversion/conjugation laws, failure precedence, reader map, and three control interpretations explicit. No owner law, complete quotient, executed fixture, score, or practical-performance result is claimed.",
    route: "Route A A0/A1 foundation/interface; formal tuple `UNASSIGNED`; positive arithmetic A2 `0`; Route B uninvoked",
    bundle: "27b2d57da72eb475fa4fc01bac1dc98c5e59b4095496cff8c65517d9a8018634"
  },
  30 => {
    dir: "30-three-disk-nonconstant-roof-determinant",
    counts: "9/9 items; 21 operations; 7 RESOLVED + 2 DELIBERATE_LIMITATION; 21/95 affected E1; +635 words; 15-page clean preview",
    progress: "Stage 4 turns the proposal into a hash-linked six-gate DAG, fixes primitive-ledger multiplicity semantics, and defines four prospective controls with exact three-way dispositions. Every domain, threshold, enclosure, orbit witness, determinant, and control outcome remains unassigned or unexecuted.",
    route: "`A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`; formal tuple `UNASSIGNED`; Route B uninvoked",
    bundle: "e6ff8927bd88d3d6c08c74f366c84f7704f84bbb67b5a9f178a12ee7a62f31e2"
  },
  31 => {
    dir: "31-level11-conjugacy-owner-ledger",
    counts: "11/11 items; 11 operations; 6 RESOLVED + 5 DELIBERATE_LIMITATION; 8/78 affected E1; +440 words; 13-page clean preview",
    progress: "Stage 4 closes the G/I/C type contract: complete publication requires every root decision resolved, hence `X_res=X` and an exactly 138-row `I`; unresolved rows enter only non-estimand `I_diag`. The inverse proof, executable producer/verifier, and independent adjudicator remain absent.",
    route: "Route A A1 owner/canonicalization preparation; formal tuple `UNASSIGNED`; positive arithmetic A2 `0`; Route B uninvoked",
    bundle: "463c00cf2975c945ef5f9c180bb4ba0040ebddf13731da5f0e16bc12ac43f612"
  },
  32 => {
    dir: "32-homology-cover-renormalization-uniformity",
    counts: "12/12 items; 12 operations; 8 RESOLVED + 4 DELIBERATE_LIMITATION; 9/98 affected E1; +437 words; 14-page clean preview",
    progress: "Stage 4 gives the two modulus schedules, both iterated-limit orders, majorant/interchange obligations, and a typed R+/R0/factor comparator table. Every formal object or candidate identity remains `UNDEFINED`, `UNPROVED`, or `NOT_EVALUABLE`; no obstruction or factor result is claimed.",
    route: "generic Route-A A1-A2 preparation with arithmetic A0 unavailable; formal tuple `UNASSIGNED`; Route B uninvoked",
    bundle: "b527625c90cff83468df0ca40b066b79f47b8deaa22c8f62324d297ae4275269"
  },
  33 => {
    dir: "33-bolza-control-matched-census",
    counts: "13/13 items; 13 operations; 8 RESOLVED + 5 DELIBERATE_LIMITATION; 12/126 affected E1; +1,400 words; 17-page clean preview",
    progress: "Stage 4 fixes BP/CP producer contracts, exact owner/inverse/repetition semantics, canonical serialization and migration rules, and a trust graph with synthetic cross-presentation traces. No producer, fixture bytes, validator, passage audit, or census exists; both control directions remain conditional and unverified.",
    route: "Route A A1 preparation with formal A0 prohibited/confounded; formal tuple `UNASSIGNED`; Route B uninvoked",
    bundle: "3c8fb5ae0bbe9b597579d41657a312da1f081068ac9e977c6df38f80337265a9"
  }
}.freeze

def checked_sub!(text, pattern, replacement, label)
  raise "missing status-doc target: #{label}" unless text.sub!(pattern, replacement)
end

def write(path, text)
  File.binwrite(path, text.end_with?("\n") ? text : "#{text}\n")
end

root_path = File.join(ROOT, "README.md")
root = File.binread(root_path).force_encoding("UTF-8")

checked_sub!(
  root,
  /^\| `29--33`[^\n]*$/,
  "| `29--33` — 五个同源但不同检验面的连续时间子型 | **Round 10 / Stage 4 精确授权修订完成；等待 Stage 3 prime 作者确认** | 56/56 roadmap items 由 97 个定点操作落地：36 `RESOLVED`、20 `DELIBERATE_LIMITATION`；88/480 E1 逐项语义复核，392 条未受影响 E1 保持基线等重数；五份 evidence bundle、73 页 clean preview 与 2,018 项统一验收全部通过。Canonical manuscript/bib/PDF/results、初始动力学限定和 Route 坐标均未改。见 [Stage-4 批次报告](BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md)与[完成收据](BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json)。 |",
  "root progress-index row"
)

overview = <<~MD.chomp
  ## Papers 29--33 Round 10 当前概要

  Round 10 的 ARS **Stage 4 author-side revision 已在精确授权内完成**，当前严格停在
  **STAGE4_COMPLETE / AWAITING_SCHOLAR_CONFIRMATION_BEFORE_STAGE3_PRIME**。
  五篇合计 **56/56 roadmap items、97 operations、36 RESOLVED + 20
  DELIBERATE_LIMITATION**；正文由 26,638 增至 30,201 词（`+3,563`），五份
  marker-stripped preview 共 73 页。统一只读验收 **2,018/2,018 PASS**。

  | Paper | Stage-4 明确落地进展 | 结果与保留边界 |
  |---|---|---|
  | [P29](papers/29-bianchi-ideal-owner-refinement/README.md) | 五个 Gate-M/Gate-Q 接口、精确 inversion/conjugation 法则、失败优先级及控制解释图已落成。 | 11/11；40 ops；7 resolved + 4 limitations；无 owner law、完整 quotient、执行 fixture 或性能结果。 |
  | [P30](papers/30-three-disk-nonconstant-roof-determinant/README.md) | 六门 DAG、primitive multiplicity 约定、四类 control 与三态判据已精确定义。 | 9/9；21 ops；7 + 2；`Omega`、阈值、enclosure、determinant 与控制结果仍未赋值／未执行。 |
  | [P31](papers/31-level11-conjugacy-owner-ledger/README.md) | 完整 G/I/C 现在必须先有全体 resolved root decisions；零未决时 `I` 精确为 138 行。 | 11/11；11 ops；6 + 5；inverse theorem、executable verifier 与独立 adjudicator 仍缺。 |
  | [P32](papers/32-homology-cover-renormalization-uniformity/README.md) | 两套 modulus schedule、两种迭代极限、majorant/interchange 与 typed comparator 全部显式化。 | 12/12；12 ops；8 + 4；形式对象和因子仍 `UNDEFINED/UNPROVED/NOT_EVALUABLE`。 |
  | [P33](papers/33-bolza-control-matched-census/README.md) | BP/CP 契约、owner/inverse/repetition、canonical serialization、migration 与 trust graph 已具体化。 | 13/13；13 ops；8 + 5；无 producer、fixture bytes、validator、passage audit 或 census。 |

  ClaimIntent 表面为 0，因此机械 replay 是诚实的 `0/0 vacuous`，不是 clean claim
  certificate；本轮结论来自全部 changed operations、88 条 affected E1 与 392 条
  unaffected E1 的有界语义复核。后者中 375 条在全稿恰好一次；P33 的 17 条短文本
  保持原有重复重数，没有被误报为“全稿一次”。五篇最终构建均为 0 undefined
  citation/reference、0 missing glyph、0 fatal、0 overfull，引用仍为 `plainnat` 数字制。

  路线对应仍由 [`Route A`](skills/route-a-evaluator.md) 与
  [`Route B`](skills/route-b-evaluator.md) 控制：Stage 4 是论文语义与证据修订，不产生
  A0--A4 或 B1--B5 credit。P29 仍在 A0/A1 foundation/interface；P30 仍为
  `A0_FAIL / A2_NOT_ELIGIBLE`；P31 为 A1 owner/canonicalization preparation；P32
  仅 generic A1--A2 preparation 且 arithmetic A0 unavailable；P33 为 A1
  preparation 且 formal A0 prohibited/confounded。Formal Route-A tuples、正向算术
  A2、A3、A4 与 Route-B invocation 仍各为 `0/5`，五个初始系统、clock、owner、
  normalization 与 cutoff 原样冻结。

  首次 apply/build 发现的排版和跨块语义问题已 fail closed，并逐篇归档为
  `stage4_attempt1_superseded_20260903/`；修正版均从不可变 Stage-3 base 重放。
  Canonical manuscript/bib/PDF、`code/experiments/results` 与科学数值没有变化。
  详见 [Stage-4 批次完成报告](BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md)、
  [机器收据](BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json)与
  [统一验收脚本](tools/audit_round10_stage4_completion.rb)。Stage 3 prime 尚未开始；
  下一合法动作只需作者确认进入 Stage 3 prime，Stage 4.5 与 Stage 5 均未授权。
MD

checked_sub!(
  root,
  /## Papers 29--33 Round 10 当前概要\n.*?(?=\n### 历史：Stage 2\.5 与 Stage 3 Phase 0 基线)/m,
  overview,
  "root current Round-10 overview"
)

root.gsub!("以下记录是已被本节上方 Stage-3 完成态取代的历史基线。", "以下记录是已被本节上方 Stage-4 完成态取代的历史基线。")
root.gsub!("。当前严格停在\n**HISTORICAL_STAGE3_PHASE0_COMPLETE", "。当时严格停在\n**HISTORICAL_STAGE3_PHASE0_COMPLETE")
root.gsub!("上述历史 Phase-0 配置随后已由 25/25 Phase-1、25/25 Phase-2 和 5/5\n机械综合完整执行并取代；当前合法下一步已变为作者 Stage-3 决策与 Stage-4\n精确授权。", "上述历史 Phase-0 配置随后已由 25/25 Phase-1、25/25 Phase-2 和 5/5\n机械综合完整执行并取代；该历史检查点当时的合法下一步是作者 Stage-3 决策与\nStage-4 精确授权。")
root.gsub!("29--33-round10-stage3 - ARS Stage 3 `REVIEW` complete（2026-09-03，当前）", "29--33-round10-stage3 - ARS Stage 3 `REVIEW` complete（2026-09-03，历史检查点）")

stage4_ledger = <<~MD.chomp

  29--33-round10-stage4 - ARS Stage 4 `REVISE` complete（2026-09-03，当前） - 作者事件 `继续，额度已经重置了` 经有界解释批准全部 56 项 proposal-only 路线图；五篇以 97 个授权定点操作完成 36 `RESOLVED` + 20 `DELIBERATE_LIMITATION`，正文共新增 3,563 词。88/480 affected E1 全量有界语义复核，392 unaffected E1 保持基线等重数（375 exact-once；P33 17 duplicate-valued）；五份 evidence bundle、73 页 clean preview 与统一验收 2,018/2,018 通过。首次 apply/build 暴露的问题 fail closed 并归档为 `SUPERSEDED_FAIL_CLOSED_NOT_CANONICAL`，最终补丁全部从 Stage-3 immutable base 重放。Canonical manuscript/bib/PDF、科学树、五个初始动力系统与 Route 坐标均未变；formal tuples、正向算术 A2、A3、A4、Route B 仍 `0/5`。当前停在 Stage 3 prime 作者确认门，Stage 3 prime、Stage 4.5 与 Stage 5 均未开始。详见 [批次完成报告](BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md)与[机器收据](BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json)。
MD

raise "root already contains Stage-4 ledger" if root.include?("29--33-round10-stage4 -")
root << stage4_ledger
write(root_path, root)

PAPERS.each do |number, cfg|
  code = "P#{number}"
  paper_root = File.join(ROOT, "papers", cfg.fetch(:dir))
  readme_path = File.join(paper_root, "README.md")
  readme = File.binread(readme_path).force_encoding("UTF-8")
  receipt_row = RECEIPT.fetch("papers").find { |row| row.fetch("paper") == code }
  completion_sha = receipt_row.dig("artifacts", "completion_report")
  audit_sha = receipt_row.dig("semantic_audit", "sha256")
  crosswalk_sha = receipt_row.dig("route", "crosswalk_sha256")

  status = <<~MD.chomp
    ## Current status

    **ARS STAGE 4 AUTHOR-SIDE REVISION COMPLETE / AWAITING SCHOLAR CONFIRMATION BEFORE STAGE 3 PRIME.**

    #{cfg.fetch(:counts)}. The final bounded semantic audit and clean preview pass.
    Canonical manuscript, bibliography, PDF, scientific results, initial dynamical
    system, and Route coordinates remain frozen. Stage 3 prime and Stage 4.5 have
    not started.

  MD
  checked_sub!(readme, /## Current status\n.*?(?=\n## )/m, status, "#{code} current status")

  package_heading = number <= 31 ? "## Current paper package" : "## Current paper and revision package"
  next_heading = number <= 31 ? "## 明确科学进展与边界" : "## 结论概要"
  stage4_package = <<~MD
    - [Stage-4 completion report](notes/stage4_completion_report.md)
    - [Stage-4 revised anchored draft](notes/stage4_revision_round1.tex) and [clean preview PDF](notes/stage4_revision_round1.pdf)
    - [Authorized patch](notes/stage4_revision_patch_round1.json) and [apply report](notes/stage4_revision_round1.tex.apply-report.json)
    - [Response to reviewers](notes/stage4_response_to_reviewers_round1.md)
    - [Revision-Evidence Bundle](notes/stage4_revision_evidence_bundle.json) and [bundle validation](notes/stage4_bundle_validation_receipt.json)
    - [Bounded semantic audit](notes/stage4_unregistered_claim_drift_audit.md) and [Route crosswalk](notes/stage4_route_crosswalk.md)
    - [Pipeline state](notes/pipeline_state.md)
  MD
  package_pattern = /(#{Regexp.escape(package_heading)}\n.*?)(?=\n#{Regexp.escape(next_heading)})/m
  match = readme.match(package_pattern)
  raise "missing #{code} package section" unless match
  package_body = match[1].gsub(/^- \[Pipeline state\].*\n?/, "")
  checked_sub!(readme, package_pattern, "#{package_body}#{stage4_package.rstrip}\n", "#{code} package links")

  progress_insert = <<~MD

    **Stage-4 landing result.** #{cfg.fetch(:progress)} The disposition is
    `#{cfg.fetch(:counts)}`. This is explicit manuscript/certificate progress,
    not a scientific execution or Route promotion.
  MD
  checked_sub!(readme, /(#{Regexp.escape(next_heading)}\n)/, "\\1#{progress_insert}", "#{code} progress insertion")

  readme.gsub!(/- Official ARS E6:.*\n/, "- Official ARS E6: a schema-compatible Revision-Evidence Bundle now exists at SHA-256 `#{cfg.fetch(:bundle)}`, but Stage-4.5 E6 has **not** been invoked. The Stage-4 bounded semantic PASS is not an official E6 verdict.\n")
  readme.gsub!(/- Stage-3 review:.*\n/, "- Stage 4: `COMPLETE WITHIN EXACT AUTHORIZATION`; #{cfg.fetch(:counts)}; next checkpoint is scholar confirmation before Stage 3 prime.\n")
  readme.gsub!("`STAGE3_EDITORIAL_DECISION=MAJOR_REVISION`, and `STAGE4_AUTHORIZED=false`.", "`STAGE3_EDITORIAL_DECISION=MAJOR_REVISION`, `STAGE4_AUTHORIZED=true`,\n`STAGE4_COMPLETE=true`, and `STAGE3_PRIME_STARTED=false`.")
  readme.gsub!(/Official E6 remains `skipped_no_revision_evidence`.*?(?=\n(?:Bundle\.|The next legal transition))/m, "A schema-compatible Stage-4 Revision-Evidence Bundle now exists, but official\nStage-4.5 E6 has not been invoked. The bounded Stage-4 semantic audit is not an\nofficial E6 verdict. ")
  readme.gsub!(/The next legal transition is explicit scholar adjudication and Stage-4\nauthorization; the roadmap itself grants no write authority\./, "The next legal transition is scholar confirmation before Stage 3 prime; Stage\n4.5 and Stage 5 remain unstarted and unauthorized.")

  trace_heading = number <= 31 ? "## Batch traceability" : "## Traceability"
  trace_insert = <<~MD

    ### Current Stage-4 bindings

    - [Per-paper completion report](notes/stage4_completion_report.md): SHA-256 `#{completion_sha}`
    - [Bounded semantic audit](notes/stage4_unregistered_claim_drift_audit.md): SHA-256 `#{audit_sha}`
    - [Route crosswalk](notes/stage4_route_crosswalk.md): SHA-256 `#{crosswalk_sha}`
    - [Batch Stage-4 report](../../BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md): SHA-256 `#{REPORT_SHA}`
    - [Batch Stage-4 receipt](../../BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json): SHA-256 `#{RECEIPT_SHA}`
  MD
  checked_sub!(readme, /(#{Regexp.escape(trace_heading)}\n)/, "\\1#{trace_insert}", "#{code} trace insertion")
  write(readme_path, readme)

  state_path = File.join(paper_root, "notes", "pipeline_state.md")
  state = File.binread(state_path).force_encoding("UTF-8")
  checked_sub!(state, /Current controlling state: \*\*.*?\*\*\./, "Current controlling state: **ARS STAGE 4 AUTHOR-SIDE REVISION COMPLETE / AWAITING SCHOLAR CONFIRMATION BEFORE STAGE 3 PRIME**.", "#{code} state header")
  checked_sub!(state, /\| Pipeline global state \| `[^`]+` \|/, "| Pipeline global state | `stage4_complete_awaiting_scholar_confirmation_before_stage3_prime` |", "#{code} global state")
  checked_sub!(state, /\| Official E6 \|.*$/, "| Official E6 | Stage-4 Revision-Evidence Bundle present at SHA-256 `#{cfg.fetch(:bundle)}`; Stage-4.5 E6 `NOT_INVOKED`; bounded semantic audit `PASS` is not official E6 |", "#{code} E6 row")
  checked_sub!(state, /\| Stage 4 \|.*$/, "| Stage 4 | `COMPLETE WITHIN EXACT AUTHORIZATION`; #{cfg.fetch(:counts)} |", "#{code} Stage-4 row")
  checked_sub!(state, /\| Stage-3 mutation\/Route boundary \|.*$/, "| Stage-4 write boundary | only versioned `notes/` revision artifacts changed; canonical manuscript/bibliography/PDF and science trees unchanged; Route advancement `NONE` |", "#{code} write boundary")
  checked_sub!(state, /\| (?:Next legal transition|Next state) \|.*$/, "| Next legal transition | `AWAITING_SCHOLAR_CONFIRMATION_BEFORE_STAGE3_PRIME`; Stage 3 prime, Stage 4.5, and Stage 5 not started |", "#{code} next transition")
  state.gsub!("| Route advancement from Stage 3 | `NONE` |", "| Route advancement from Stage 4 | `NONE` |")
  state.gsub!(/Official E6 remains skipped because no official ARS Revision-Evidence Bundle\nexists\..*?\n\n/m, "A schema-compatible Revision-Evidence Bundle now exists for this Stage-4 revision.\nOfficial Stage-4.5 E6 has not been invoked; the bounded Stage-4 semantic audit\nmust not be represented as the official E6 verdict.\n\n")

  state_append = <<~MD

    ## Current Stage-4 completion bindings

    | Artifact | SHA-256 |
    |---|---|
    | [Per-paper completion report](stage4_completion_report.md) | `#{completion_sha}` |
    | [Bounded semantic audit](stage4_unregistered_claim_drift_audit.md) | `#{audit_sha}` |
    | [Route crosswalk](stage4_route_crosswalk.md) | `#{crosswalk_sha}` |
    | [Revision-Evidence Bundle](stage4_revision_evidence_bundle.json) | `#{cfg.fetch(:bundle)}` |
    | [Batch completion report](../../../BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md) | `#{REPORT_SHA}` |
    | [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json) | `#{RECEIPT_SHA}` |

    The ClaimIntent replay is `0/0` vacuous and not a clean certificate. Completion
    rests on the bounded changed-operation/E1 semantic audit. #{cfg.fetch(:route)}.
    Canonical bytes and scientific trees are unchanged. Stage 3 prime has not
    started.
  MD
  raise "#{code} state already has Stage-4 bindings" if state.include?("## Current Stage-4 completion bindings")
  state << state_append
  write(state_path, state)
end

puts "UPDATED root README, five paper READMEs, and five pipeline-state files"
