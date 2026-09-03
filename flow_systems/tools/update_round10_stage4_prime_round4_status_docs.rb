#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"

ROOT = File.expand_path("..", __dir__)
OLD_MARKER = "<!-- ROUND10_STAGE3_PRIME_ROUND3_STATUS_SYNC_20260903 -->"
SYNC_MARKER = "<!-- ROUND10_STAGE4_PRIME_ROUND4_STATUS_SYNC_20260904 -->"

PAPERS = {
  29 => {
    slug: "29-bianchi-ideal-owner-refinement",
    state: "stage4_prime_request_prepared_awaiting_exact_authorization",
    status_title: "ARS STAGE 4′ EXACT REQUEST PREPARED — AWAITING AUTHOR CONFIRMATION.",
    progress: "The Stage-4′ request now maps four residual roadmap items plus `NEW-1` to 8 exact targets and 10 block-operation pairs. It specifies the dated replay/crosswalk, complete stop map, three control stop states, a labeled unexecuted fixture, and removal of the same-family independence overstatement. No patch, revised draft, bibliography, or scientific result was created.",
    conclusion: "本轮明确进展是把 P29 的四个剩余评审项和 `NEW-1` 收敛为可逐块执行、可回放的 Stage 4′ 合同：8 个精确目标、10 个 block-operation pairs。正文尚未修改；这是一项可审计的落地准备，不是 owner law、完整 quotient、fixture 结果或 Route credit。",
    system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
    route: "Route A A0/A1 foundation/interface preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    next_action: "exact author confirmation of the frozen joint P29/P32 Stage-4′ request before any listed operation executes",
    main_trace_heading: "## Batch traceability",
    package_route_heading: "## Claim and route boundary",
    package_route_next: nil,
    old_current_heading: "### Current Stage-3′ Round-3 checker-backed outcome",
    old_package_heading: "## Current Stage 3′ Round-3 checker-backed outcome"
  },
  30 => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    state: "stage4_prime_author_side_complete_awaiting_stage4_5_authorization",
    status_title: "ARS STAGE 4′ AUTHOR-SIDE REVISION COMPLETE — AWAITING FRESH STAGE 4.5.",
    progress: "All 5/5 residual items are addressed by 14 authorized operations. The final chain preserves 113/127 base blocks, records 54/54 successful dated metadata queries and a 28-row passage matrix, and appends two verified correction records only to the notes-side bibliography. The clean preview is 16 pages with zero blocking TeX findings or overfull boxes.",
    conclusion: "本轮 P30 已形成实质性的论文修订稿：5/5 剩余项由 14 个授权操作闭合，补入 54 条可回放检索、28 行 passage matrix 与两条 notes-only correction records；16 页预览干净构建。物理 roof、算子、determinant、误差界和 Route 结论仍未被虚构，下一步是 fresh Stage 4.5 审计。",
    system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
    route: "A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    next_action: "fresh Stage 4.5 audit of the current versioned Stage-4′ chain; no silent repair or promotion",
    main_trace_heading: "## Batch traceability",
    package_route_heading: "## Claim and route boundary",
    package_route_next: nil,
    old_current_heading: "### Prepared P30/P31 Stage-4′ request (not authorized or executed)",
    old_package_heading: "## Prepared Stage-4′ request (not yet authorized)"
  },
  31 => {
    slug: "31-level11-conjugacy-owner-ledger",
    state: "stage4_prime_author_side_complete_awaiting_stage4_5_authorization",
    status_title: "ARS STAGE 4′ AUTHOR-SIDE REVISION COMPLETE — AWAITING FRESH STAGE 4.5.",
    progress: "All 8/8 residual items are addressed by 20 authorized operations. The final chain preserves 93/111 base blocks, records 20/20 successful dated metadata queries and a 24-row method matrix, and appends two source-verified closest-work records only to the notes-side bibliography. The clean preview is 13 pages with zero blocking TeX findings or overfull boxes.",
    conclusion: "本轮 P31 已形成实质性的论文修订稿：8/8 剩余项由 20 个授权操作闭合，补入 20 条可回放检索、24 行 method matrix 与两条 notes-only closest-work records；13 页预览干净构建。完整 owner ledger、inverse theorem、可执行 verifier 和 Route 结论仍未被声称，下一步是 fresh Stage 4.5 审计。",
    system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers repetitions; Hecke degree distinct",
    route: "Route A A1-only owner/canonicalization preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    next_action: "fresh Stage 4.5 audit of the current versioned Stage-4′ chain; no silent repair or promotion",
    main_trace_heading: "## Batch traceability",
    package_route_heading: "## Claim and route boundary",
    package_route_next: nil,
    old_current_heading: "### Prepared P30/P31 Stage-4′ request (not authorized or executed)",
    old_package_heading: "## Prepared Stage-4′ request (not yet authorized)"
  },
  32 => {
    slug: "32-homology-cover-renormalization-uniformity",
    state: "stage4_prime_request_prepared_awaiting_exact_authorization",
    status_title: "ARS STAGE 4′ EXACT REQUEST PREPARED — AWAITING AUTHOR CONFIRMATION.",
    progress: "The Stage-4′ request now maps seven residual roadmap items to 18 exact targets and 26 block-operation pairs. It specifies closest-work comparison, a commit-pinned artifact inventory, scholarly/development provenance separation, formal definitions, AN-1--AN-5 closure, a 51-manifestation replay and passage matrix, and a bounded conditional inequality lemma. No patch, revised draft, bibliography, or scientific result was created.",
    conclusion: "本轮明确进展是把 P32 的七个剩余评审项收敛为可逐块执行、可回放的 Stage 4′ 合同：18 个精确目标、26 个 block-operation pairs，并把形式定义、AN-1--AN-5、51 条 replay/matrix 与条件不等式的边界写入请求。正文尚未修改；没有 factor、limit、obstruction 或 Route credit。",
    system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
    route: "generic Route A A1-A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    next_action: "exact author confirmation of the frozen joint P29/P32 Stage-4′ request before any listed operation executes",
    main_trace_heading: "## Traceability",
    package_route_heading: "## Route position and next gate",
    package_route_next: "## Batch traceability",
    old_current_heading: "### Current Stage-3′ Round-3 checker-backed outcome",
    old_package_heading: "## Current Stage 3′ Round-3 checker-backed outcome"
  },
  33 => {
    slug: "33-bolza-control-matched-census",
    state: "stage3_prime_round4_aborted_phase2a_lint_failed_awaiting_fresh_round5_authorization",
    status_title: "ARS STAGE 3′ ROUND 4 ABORTED FAIL-CLOSED — AWAITING FRESH ROUND 5.",
    progress: "Fresh Round 4 Phase 1 passed 201 checks over 13 precommitted rows. The first immutable Phase-2A verdict semantically counted 5 FULL / 8 PARTIAL, but failed the official schema with exactly 35 errors, so the no-retry gate emitted `[RE-REVIEW-ABORT: phase2a_lint_failed]`. No response, Phase 2B, traceability, checker execution, or decision exists.",
    conclusion: "本轮 P33 的可交付结果是一次严格失败封闭的 Round 4：Phase 1 的 13 行预承诺和 201 项检查通过，但首次 Phase-2A verdict 出现 35 个 schema 错误，故 5 FULL / 8 PARTIAL 只作非控制读数，没有签发决定。下一轮必须使用预先校验的 schema-correct emitter/template 开启全新 Round 5；Round 4 不原地修补。",
    system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
    route: "Route A A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    next_action: "a wholly fresh Stage 3′ Round 5 with a new id/manifest, fresh role-separated contexts, and a schema-correct prevalidated emitter/template",
    main_trace_heading: "## Traceability",
    package_route_heading: "## Route position and next gate",
    package_route_next: "## Batch traceability",
    old_current_heading: "### Current Stage-3′ Round-3 fail-closed outcome",
    old_package_heading: "## Current Stage 3′ Round-3 fail-closed outcome"
  }
}.freeze

ARTIFACTS = {
  report: "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md",
  receipt: "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json",
  checkpoint: "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md",
  request_json: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json",
  request_md: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md",
  request_validation: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json",
  p30_draft: "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round2.tex",
  p30_patch: "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_patch_round2.json",
  p30_bundle: "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_evidence_bundle_round2.json",
  p30_build: "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_preview_build_receipt_round2.json",
  p30_audit: "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_final_audit_round2.json",
  p31_draft: "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round2.tex",
  p31_patch: "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_patch_round2.json",
  p31_bundle: "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_evidence_bundle_round2.json",
  p31_build: "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_preview_build_receipt_round2.json",
  p31_audit: "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_final_audit_round2.json",
  p33_report: "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_verification_report.md",
  p33_abort: "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_abort_record.json",
  p33_validation: "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_phase2a_validation.json",
  p33_completion: "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_completion_receipt.json"
}.freeze

TARGETS = ["README.md"] + PAPERS.values.flat_map do |paper|
  base = File.join("papers", paper.fetch(:slug))
  [File.join(base, "README.md"), File.join(base, "notes", "pipeline_state.md"), File.join(base, "paper", "README.md")]
end
TARGETS.freeze

abort "expected 16 status targets" unless TARGETS.length == 16 && TARGETS.uniq.length == 16
abort "forbidden status target" if TARGETS.any? { |path| path.match?(%r{/(?:manuscript\.tex|references\.bib|paper\.pdf)$|/(?:code|experiments|results)/}) }

(ARTIFACTS.values + TARGETS).each do |path|
  abort "missing required path before status sync: #{path}" unless File.file?(File.join(ROOT, path))
end

HASHES = ARTIFACTS.transform_values { |path| Digest::SHA256.file(File.join(ROOT, path)).hexdigest }.freeze

def count(text, needle)
  text.scan(Regexp.new(Regexp.escape(needle))).length
end

def replace_once!(text, old, replacement, label)
  n = count(text, old)
  raise "#{label}: expected one literal target, found #{n}" unless n == 1
  text.sub!(old, replacement)
end

def replace_regex_once!(text, pattern, replacement, label)
  n = text.scan(pattern).length
  raise "#{label}: expected one regex target, found #{n}" unless n == 1
  text.sub!(pattern, replacement)
end

def replace_section!(text, heading, next_heading, replacement, label)
  start_token = "#{heading}\n"
  raise "#{label}: start heading count != 1" unless count(text, start_token) == 1
  start_at = text.index(start_token)
  if next_heading
    end_token = "\n#{next_heading}\n"
    end_at = text.index(end_token, start_at + start_token.length)
    raise "#{label}: missing next heading" unless end_at
  else
    end_at = text.length
  end
  text[start_at...end_at] = "#{replacement.rstrip}\n"
end

def insert_after_heading!(text, heading, insertion, label)
  token = "#{heading}\n"
  replace_once!(text, token, "#{token}\n#{insertion.rstrip}\n", label)
end

def insert_before_heading!(text, heading, insertion, label)
  token = "\n#{heading}\n"
  replace_once!(text, token, "\n#{insertion.rstrip}\n\n#{heading}\n", label)
end

def replace_table_row!(text, label_pattern, replacement, label)
  pattern = /^\| #{label_pattern} \|[^\n]*$/
  replace_regex_once!(text, pattern, replacement, label)
end

def current_rows(number, prefix, hashes)
  common = <<~MD.rstrip
    | [Batch completion report](#{prefix}BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md) | `#{hashes.fetch(:report)}` |
    | [Batch completion receipt](#{prefix}BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json) | `#{hashes.fetch(:receipt)}` |
    | [Mandatory checkpoint](#{prefix}BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md) | `#{hashes.fetch(:checkpoint)}` |
  MD
  case number
  when 29, 32
    <<~MD.rstrip
      | [P29/P32 exact Stage-4′ request](#{prefix}BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md) | `#{hashes.fetch(:request_md)}` |
      | [Machine-readable request](#{prefix}BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json) | `#{hashes.fetch(:request_json)}` |
      | [377-check validation](#{prefix}BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json) | `#{hashes.fetch(:request_validation)}` |
      #{common}
    MD
  when 30
    <<~MD.rstrip
      | [P30 revised anchored draft](#{prefix}papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round2.tex) | `#{hashes.fetch(:p30_draft)}` |
      | [P30 exact patch](#{prefix}papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_patch_round2.json) | `#{hashes.fetch(:p30_patch)}` |
      | [P30 evidence bundle](#{prefix}papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_evidence_bundle_round2.json) | `#{hashes.fetch(:p30_bundle)}` |
      | [P30 build receipt](#{prefix}papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_preview_build_receipt_round2.json) | `#{hashes.fetch(:p30_build)}` |
      | [P30 final audit](#{prefix}papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_final_audit_round2.json) | `#{hashes.fetch(:p30_audit)}` |
      #{common}
    MD
  when 31
    <<~MD.rstrip
      | [P31 revised anchored draft](#{prefix}papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round2.tex) | `#{hashes.fetch(:p31_draft)}` |
      | [P31 exact patch](#{prefix}papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_patch_round2.json) | `#{hashes.fetch(:p31_patch)}` |
      | [P31 evidence bundle](#{prefix}papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_evidence_bundle_round2.json) | `#{hashes.fetch(:p31_bundle)}` |
      | [P31 build receipt](#{prefix}papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_preview_build_receipt_round2.json) | `#{hashes.fetch(:p31_build)}` |
      | [P31 final audit](#{prefix}papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_final_audit_round2.json) | `#{hashes.fetch(:p31_audit)}` |
      #{common}
    MD
  when 33
    <<~MD.rstrip
      | [P33 Round-4 verification report](#{prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round4_verification_report.md) | `#{hashes.fetch(:p33_report)}` |
      | [P33 Round-4 abort record](#{prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round4_abort_record.json) | `#{hashes.fetch(:p33_abort)}` |
      | [P33 Phase-2A validation](#{prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round4_phase2a_validation.json) | `#{hashes.fetch(:p33_validation)}` |
      | [P33 completion receipt](#{prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round4_completion_receipt.json) | `#{hashes.fetch(:p33_completion)}` |
      #{common}
    MD
  end
end

def main_status(number, paper)
  <<~MD.rstrip
    ## Current status

    #{SYNC_MARKER}

    **#{paper.fetch(:status_title)}**

    Control state: `#{paper.fetch(:state)}`. #{paper.fetch(:progress)}

    本轮结论概要：#{paper.fetch(:conclusion)}

    Frozen initial system: #{paper.fetch(:system)}.

    Route mapping: #{paper.fetch(:route)}. This round cannot award Route credit.

    Citation formatting remains `plainnat` numeric. Canonical manuscript,
    bibliography, and PDF bytes; science/results; the frozen initial system; and
    every Route coordinate remain unchanged. Stage 5/6, canonical promotion,
    submission, result refresh, new scientific execution, and Route advancement
    remain unauthorized.
  MD
end

def main_trace(number, paper, hashes)
  title = case number
          when 29, 32 then "### Current Stage-4′ request (prepared, not executed)"
          when 30, 31 then "### Current Stage-4′ author-side completion"
          when 33 then "### Current Stage-3′ Round-4 fail-closed outcome"
          end
  <<~MD.rstrip
    #{title}

    #{paper.fetch(:progress)} Next legal action: #{paper.fetch(:next_action)}.

    | Current artifact | SHA-256 |
    |---|---|
    #{current_rows(number, "../../", hashes)}
  MD
end

def pipeline_binding(number, paper, hashes)
  title = case number
          when 29, 32 then "## Current Stage-4′ request bindings"
          when 30, 31 then "## Current Stage-4′ completion bindings"
          when 33 then "## Current Stage-3′ Round-4 abort bindings"
          end
  <<~MD.rstrip
    #{title}

    Control state: `#{paper.fetch(:state)}`.

    #{paper.fetch(:progress)}

    | Current artifact | SHA-256 |
    |---|---|
    #{current_rows(number, "../../../", hashes)}

    Next legal action: #{paper.fetch(:next_action)}. Citation style remains
    `plainnat` numeric. Canonical manuscript/bibliography/PDF, science/results,
    frozen initial system, and Route coordinates are unchanged. Formal Route-A
    tuples, positive arithmetic A2, A3, A4, and Route B remain `0/5`. Stage 5/6,
    canonical promotion, submission, result refresh, and new scientific execution
    remain unauthorized.
  MD
end

def package_current(number, paper, hashes)
  title = case number
          when 29, 32 then "## Current Stage 4′ request-preparation outcome"
          when 30, 31 then "## Current Stage 4′ author-side revision outcome"
          when 33 then "## Current Stage 3′ Round-4 fail-closed outcome"
          end
  <<~MD.rstrip
    #{title}

    **本轮结论概要。** #{paper.fetch(:conclusion)}

    | Current artifact | SHA-256 |
    |---|---|
    #{current_rows(number, "../../../", hashes)}
  MD
end

def package_route(paper)
  <<~MD.rstrip
    #{paper.fetch(:package_route_heading)}

    Explicit paper progress: #{paper.fetch(:progress)}

    Frozen initial system: #{paper.fetch(:system)}.

    Route mapping: #{paper.fetch(:route)}. Across Papers 29--33, formal Route-A
    tuples, positive arithmetic A2, A3, A4, and Route B remain `0/5`.

    The next legal action is #{paper.fetch(:next_action)}. Canonical manuscript,
    bibliography, PDF, science/results, and the frozen system remain unchanged.
    Stage 5/6, canonical promotion, submission, Route advancement, result refresh,
    and new scientific execution remain unauthorized.
  MD
end

documents = TARGETS.to_h do |relative|
  text = File.binread(File.join(ROOT, relative)).force_encoding("UTF-8")
  raise "#{relative}: old marker count != 1" unless count(text, OLD_MARKER) == 1
  raise "#{relative}: new marker already present" unless count(text, SYNC_MARKER).zero?
  [relative, text]
end

root = documents.fetch("README.md")
replace_regex_once!(
  root,
  /^\| `29--33`[^\n]*$/,
  "| `29--33` — 五个同源但不同检验面的连续时间子型 | **Round 10 / three-track close：P30/P31 Stage 4′ complete；P29/P32 exact request prepared；P33 Round 4 fail-closed** | P30/P31 完成 13/13 residuals、34 个授权操作和 86/86 + 85/85 审计；P29/P32 请求覆盖 11 residuals + 1 regression、26 targets、36 pairs，并通过 377 checks；P33 Phase 1 为 201/201，但首次 Phase-2A 有 35 个 schema 错误，故严格中止。Canonical 15 files、science/results、五个初始系统与 Route 坐标均未变。见 [完成报告](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md)、[收据](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json)与[检查点](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md)。 |",
  "root progress row"
)

root_overview = <<~MD.rstrip
  ## Papers 29--33 Round 10 当前概要

  #{SYNC_MARKER}

  Round 10 本轮三轨已经结账，并且五篇都有明确、可审计的推进。P30/P31 的
  Stage 4′ 作者侧修订完成；P29/P32 的 hash-bound Stage 4′ 精确请求已准备、但尚未
  执行；P33 的 fresh Stage 3′ Round 4 在首次不可变 Phase-2A schema 校验处严格
  fail closed。当前停在统一 mandatory author checkpoint。

  | Paper | 当前状态 | 本轮明确落地结果 | 下一合法动作 |
  |---|---|---|---|
  | [P29](papers/29-bianchi-ideal-owner-refinement/README.md) | Stage 4′ request prepared；未改稿 | 4 residuals + `NEW-1` 映射为 8 targets / 10 pairs；replay、stop map、三 control 状态和未执行 fixture 均已定型。 | 确认执行冻结的 P29/P32 精确请求。 |
  | [P30](papers/30-three-disk-nonconstant-roof-determinant/README.md) | **Stage 4′ author-side COMPLETE** | 5/5 residuals、14 ops、54/54 queries、28-row matrix、16-page clean preview；final audit 86/86。 | fresh Stage 4.5 审计。 |
  | [P31](papers/31-level11-conjugacy-owner-ledger/README.md) | **Stage 4′ author-side COMPLETE** | 8/8 residuals、20 ops、20/20 queries、24-row matrix、13-page clean preview；final audit 85/85。 | fresh Stage 4.5 审计。 |
  | [P32](papers/32-homology-cover-renormalization-uniformity/README.md) | Stage 4′ request prepared；未改稿 | 7 residuals 映射为 18 targets / 26 pairs；formal definitions、AN-1--AN-5、51-row replay/matrix 与条件 lemma 均已定型。 | 确认执行冻结的 P29/P32 精确请求。 |
  | [P33](papers/33-bolza-control-matched-census/README.md) | **Round 4 ABORT / `phase2a_lint_failed`** | Phase 1 为 13 rows、201/201；首次 Phase-2A 的 5 FULL / 8 PARTIAL 为非控制读数，因 35 个 schema errors 未签发 decision。 | 使用预校验 schema emitter 开启全新 Round 5。 |

  P30/P31 合计闭合 **13/13 residuals、34 operations**，两份 evidence bundle 和
  notes-side bibliography 均通过，独立重构建为 16 + 13 页，undefined
  citation/reference、missing glyph、fatal、overfull 全为 0。P29/P32 请求通过
  **377/377**；它不是已执行修订。P33 没有 Response、Phase 2B、traceability、
  checker execution 或 decision；Round 4 工件保持不可变。

  路线仍由 [`Route A`](skills/route-a-evaluator.md) 和
  [`Route B`](skills/route-b-evaluator.md) 控制。本批仍是 **Route-A
  foundation/interface**：formal Route-A tuples `0/5`、positive arithmetic A2
  `0/5`、A3 `0/5`、A4 `0/5`、Route B `0/5`。五个初始动力学系统及 clock、
  primitive、owner、inverse、normalization、cutoff 和 target-blind 限定全部冻结。
  引用继续保持 `plainnat` 数字制；canonical manuscript/bib/PDF 15/15、
  science/results 与 Route 状态均未改。

  当前权威工件：

  - [本轮完成报告](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md) — `#{HASHES.fetch(:report)}`
  - [机器收据](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json) — `#{HASHES.fetch(:receipt)}`
  - [下一轮 mandatory checkpoint](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md) — `#{HASHES.fetch(:checkpoint)}`
  - [P29/P32 exact request](BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md) — `#{HASHES.fetch(:request_md)}`

  下一条简短 **`确认`** 只授权：执行 P29/P32 冻结请求、对 P30/P31 开启 fresh
  Stage 4.5、对 P33 开启 schema-correct fresh Round 5。它不授权 Stage 5/6、
  canonical promotion、新科学计算、result refresh 或 Route 晋级。
MD
replace_section!(root, "## Papers 29--33 Round 10 当前概要", "### 历史：Stage 2.5 与 Stage 3 Phase 0 基线", root_overview, "root overview")
replace_once!(root, "29--33-round10-stage3-prime-round3 - ARS Stage 3′ Round 3 closed（2026-09-03，当前强制检查点）", "29--33-round10-stage3-prime-round3 - ARS Stage 3′ Round 3 closed（2026-09-03，历史检查点；已由本轮取代）", "root Round-3 history label")

ledger = <<~MD.rstrip

  29--33-round10-stage4-prime-and-round4 - ARS three-track close（2026-09-04，当前强制检查点） - P30/P31 在原 hash-bound request 内完成作者侧 Stage 4′：13/13 residuals、34 operations、两份官方 bundle PASS、最终审计 86/86 + 85/85，独立 clean preview 为 16 + 13 页且所有 blocking TeX/overfull counters 为 0。P29/P32 只准备 Stage 4′ 精确请求，覆盖 11 residuals + 1 regression、26 targets、36 pairs、6 support scopes，377/377 checks PASS，manuscript/bib/PDF writes 均为 0。P33 fresh Round 4 的 Phase 1 为 201/201，但首次不可变 Phase-2A verdict 有 35 个 schema errors，因此以 `[RE-REVIEW-ABORT: phase2a_lint_failed]` 终止；5 FULL / 8 PARTIAL 仅为 noncontrolling self-count，无 Response/2B/checker/decision。Canonical 15 files、science/results、初始系统和 Route 均冻结；formal Route-A tuples、positive arithmetic A2、A3/A4、Route B 仍为 0/5。下一条 `确认` 的精确范围见 [完成报告](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md)、[收据](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json)与[强制检查点](BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md)。
MD
raise "root current ledger already exists" if root.include?("29--33-round10-stage4-prime-and-round4 -")
root << "\n" unless root.end_with?("\n")
root << ledger
root << "\n"
root.sub!(OLD_MARKER, SYNC_MARKER)
documents["README.md"] = root

PAPERS.each do |number, paper|
  base = File.join("papers", paper.fetch(:slug))
  main_key = File.join(base, "README.md")
  state_key = File.join(base, "notes", "pipeline_state.md")
  package_key = File.join(base, "paper", "README.md")

  main = documents.fetch(main_key)
  package_heading = number <= 31 ? "## Current paper package" : "## Current paper and revision package"
  replace_section!(main, "## Current status", package_heading, main_status(number, paper), "P#{number} main status")
  links = case number
          when 29, 32
            "- [Current P29/P32 Stage-4′ exact request](../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md) and [377-check validation](../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json)\n"
          when 30
            "- [Current Stage-4′ revised draft](notes/stage4_prime_revision_round2.tex), [evidence bundle](notes/stage4_prime_revision_evidence_bundle_round2.json), [build receipt](notes/stage4_prime_preview_build_receipt_round2.json), and [final audit](notes/stage4_prime_final_audit_round2.json)\n"
          when 31
            "- [Current Stage-4′ revised draft](notes/stage4_prime_revision_round2.tex), [evidence bundle](notes/stage4_prime_revision_evidence_bundle_round2.json), [build receipt](notes/stage4_prime_preview_build_receipt_round2.json), and [final audit](notes/stage4_prime_final_audit_round2.json)\n"
          when 33
            "- [Stage-3′ Round-4 verification report](notes/stage3_prime_round4_verification_report.md), [abort record](notes/stage3_prime_round4_abort_record.json), and [completion receipt](notes/stage3_prime_round4_completion_receipt.json)\n"
          end
  links += "- [Current batch completion report](../../#{ARTIFACTS.fetch(:report)}), [receipt](../../#{ARTIFACTS.fetch(:receipt)}), and [checkpoint](../../#{ARTIFACTS.fetch(:checkpoint)})\n"
  replace_once!(main, "- [Pipeline state](notes/pipeline_state.md)\n", "#{links}- [Pipeline state](notes/pipeline_state.md)\n", "P#{number} main package links")
  replace_once!(main, paper.fetch(:old_current_heading), paper.fetch(:old_current_heading).sub("Current", "Historical").sub("Prepared", "Historical prepared"), "P#{number} old main trace heading")
  if number == 30 || number == 31
    replace_once!(main, "### Current Stage-3′ Round-2 outcome", "### Historical Stage-3′ Round-2 outcome", "P#{number} Round-2 main heading")
  end
  insert_after_heading!(main, paper.fetch(:main_trace_heading), main_trace(number, paper, HASHES), "P#{number} new main trace")

  conclusion_heading = main.include?("## 明确科学进展与边界\n") ? "## 明确科学进展与边界" : "## 结论概要"
  insert_after_heading!(main, conclusion_heading, "**本轮结论概要（#{number}）。** #{paper.fetch(:conclusion)}", "P#{number} main conclusion")

  case number
  when 29
    replace_once!(main, "- Stage 3′ Round 3: `COMPLETE`; final 7/4/0; Phase-2B adjustments `0`; `NEW-1` minor regression; checker `PASS`; Major Revision / ARS B4. Only explicit authorization to prepare a P29 Stage-4′ request may follow.", "- Stage 3′ Round 3: historical `COMPLETE`; final 7/4/0; checker `PASS`; Major Revision / ARS B4.\n- Stage 4′ exact request: `PREPARED_NOT_AUTHORIZED_NOT_EXECUTED`; P29 scope 4 residuals + `NEW-1`, 8 targets, 10 block-operation pairs.", "P29 main stage bullets")
  when 30
    replace_once!(main, "- Stage 4′ request: joint P30/P31 request prepared and validated at 13 residuals / 37 targets / 156 checks; not authorized, not executed, and manuscript/bibliography writes remain 0.", "- Stage 4′ author-side revision: `COMPLETE`; P30 5/5 residuals, 14 operations, final audit 86/86, clean 16-page preview; Stage 4.5 not invoked.", "P30 main stage bullet")
  when 31
    replace_once!(main, "- Stage 4′ request: joint P30/P31 request prepared and validated at 13 residuals / 37 targets / 156 checks; not authorized, not executed, and manuscript/bibliography writes remain 0.", "- Stage 4′ author-side revision: `COMPLETE`; P31 8/8 residuals, 20 operations, final audit 85/85, clean 13-page preview; Stage 4.5 not invoked.", "P31 main stage bullet")
  when 32
    replace_once!(main, "`STAGE4_PRIME_REQUEST_PREPARATION_AUTHORIZED=false`.", "`STAGE4_PRIME_REQUEST_PREPARED=true`, and\n`STAGE4_PRIME_EXECUTION_AUTHORIZED=false`.", "P32 main tokens")
  when 33
    replace_once!(main, "`STAGE3_PRIME_ROUND4_AUTHORIZED=false`.", "`STAGE3_PRIME_ROUND4=ABORTED_PHASE2A_LINT_FAILED`, and\n`STAGE3_PRIME_ROUND5_AUTHORIZED=false`.", "P33 main tokens")
  end
  main.sub!(OLD_MARKER, SYNC_MARKER)
  documents[main_key] = main

  state = documents.fetch(state_key)
  replace_regex_once!(state, /^(?:Synchronized|Date): \*\*[^\n]+$/, "Synchronized: **2026-09-04 UTC**", "P#{number} state date")
  replace_regex_once!(state, /^Current controlling state: .*$/, "Current controlling state: **`#{paper.fetch(:state)}`**.", "P#{number} state control")
  replace_table_row!(state, "Pipeline global state", "| Pipeline global state | `#{paper.fetch(:state)}` |", "P#{number} state global")
  stage_row = case number
              when 29 then "| Stage 4′ exact request | `PREPARED_NOT_AUTHORIZED_NOT_EXECUTED`; P29 scope 4 residuals + NEW-1 / 8 targets / 10 block-operation pairs; request validation belongs to joint 377/377 replay |"
              when 30 then "| Stage 4′ author-side revision | `COMPLETE`; 5/5 residuals; 14 operations; 113/127 preserved blocks; 54/54 queries; 28-row matrix; 16-page clean preview; final audit 86/86; Stage 4.5 `NOT_INVOKED` |"
              when 31 then "| Stage 4′ author-side revision | `COMPLETE`; 8/8 residuals; 20 operations; 93/111 preserved blocks; 20/20 queries; 24-row matrix; 13-page clean preview; final audit 85/85; Stage 4.5 `NOT_INVOKED` |"
              when 32 then "| Stage 4′ exact request | `PREPARED_NOT_AUTHORIZED_NOT_EXECUTED`; P32 scope 7 residuals / 18 targets / 26 block-operation pairs; request validation belongs to joint 377/377 replay |"
              when 33 then "| Stage 3′ Round 4 | `ABORTED / phase2a_lint_failed`; Phase 1 201/201; immutable Phase-2A has 35 schema errors; semantic 5/8/0 noncontrolling; no response/2B/traceability/checker/decision |"
              end
  if number == 30 || number == 31
    replace_table_row!(state, "Stage 4′ exact request", stage_row, "P#{number} stage row")
  else
    anchor_label = "Stage 3′ Round 3"
    pattern = /^(\| #{Regexp.escape(anchor_label)} \|[^\n]*$)/
    replace_regex_once!(state, pattern, "\\1\n#{stage_row}", "P#{number} stage row insertion")
  end
  next_label = state.include?("| Next legal action |") ? "Next legal action" : "Next legal transition"
  replace_table_row!(state, next_label, "| #{next_label} | #{paper.fetch(:next_action)} |", "P#{number} next row")
  replace_regex_once!(state, /^\| Active Stage-3′ (?:finding|findings) \|[^\n]*$/, "| Current gated scope | #{paper.fetch(:progress)} |", "P#{number} current scope row")

  old_binding = case number
                when 29, 32, 33 then "## Current Stage-3′ Round-3 bindings"
                when 30, 31 then "## Prepared Stage-4′ request bindings"
                end
  replace_once!(state, old_binding, old_binding.sub("Current", "Historical").sub("Prepared", "Historical prepared"), "P#{number} old state binding")
  if number == 30 || number == 31
    replace_once!(state, "## Current Stage-3′ Round-2 bindings", "## Historical Stage-3′ Round-2 bindings", "P#{number} Round-2 state heading")
  end
  state << "\n" unless state.end_with?("\n")
  state << "\n#{pipeline_binding(number, paper, HASHES)}\n"
  state.sub!(OLD_MARKER, SYNC_MARKER)
  documents[state_key] = state

  package = documents.fetch(package_key)
  title_end = package.index("\n\n")
  deliverables_at = package.index("\n## Deliverables\n")
  raise "P#{number} package boundaries missing" unless title_end && deliverables_at
  intro = <<~MD.rstrip
    Package note: this directory remains the immutable canonical Stage-2.5 package;
    current revision/review outputs are versioned under `../notes/`. The authoritative
    state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md).
    #{SYNC_MARKER}
    Control state: `#{paper.fetch(:state)}`. #{paper.fetch(:progress)}
    Canonical manuscript/PDF/bibliography bytes and `plainnat` numeric citation style
    remain unchanged.
  MD
  package[(title_end + 2)...deliverables_at] = "#{intro}\n"
  replace_once!(package, paper.fetch(:old_package_heading), paper.fetch(:old_package_heading).sub("Current", "Historical").sub("Prepared", "Historical prepared"), "P#{number} old package heading")
  insert_before_heading!(package, "## 结论概要", package_current(number, paper, HASHES), "P#{number} package current")
  replace_section!(package, paper.fetch(:package_route_heading), paper.fetch(:package_route_next), package_route(paper), "P#{number} package route")
  documents[package_key] = package
end

documents.each do |relative, text|
  raise "#{relative}: new marker count != 1" unless count(text, SYNC_MARKER) == 1
  raise "#{relative}: stale marker remains" unless count(text, OLD_MARKER).zero?
  if relative.end_with?("/README.md") && !relative.end_with?("/notes/pipeline_state.md")
    raise "#{relative}: missing conclusion summary" unless text.include?("结论概要")
  end
  raise "#{relative}: missing trailing newline" unless text.end_with?("\n")
end

documents.each do |relative, text|
  absolute = File.join(ROOT, relative)
  temporary = "#{absolute}.round10-current-status.tmp"
  raise "temporary path exists: #{temporary}" if File.exist?(temporary)
  File.binwrite(temporary, text)
  File.chmod(File.stat(absolute).mode, temporary)
  File.rename(temporary, absolute)
end

TARGETS.each { |path| puts path }
puts "updated_files=#{TARGETS.length}"
