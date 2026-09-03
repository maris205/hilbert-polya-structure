#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
DATE = "2026-09-04"

REPORT_PATH = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md"
RECEIPT_PATH = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json"
CHECKPOINT_PATH = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md"

TARGETS = [REPORT_PATH, RECEIPT_PATH, CHECKPOINT_PATH].freeze
existing = TARGETS.select { |path| File.exist?(File.join(ROOT, path)) }
abort "refusing to overwrite terminal artifacts: #{existing.join(', ')}" unless existing.empty?

def artifact(path)
  absolute = File.join(ROOT, path)
  raise "missing artifact: #{path}" unless File.file?(absolute)

  {
    "path" => path,
    "sha256" => Digest::SHA256.file(absolute).hexdigest,
    "bytes" => File.size(absolute)
  }
end

def sha(path)
  artifact(path).fetch("sha256")
end

authority = {
  "author_event" => artifact("BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt"),
  "authorization_record" => artifact("BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md"),
  "authorization_receipt" => artifact("BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json"),
  "input_freeze" => artifact("BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json")
}

p29_p32 = {
  "request_json" => artifact("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json"),
  "request_markdown" => artifact("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md"),
  "validation" => artifact("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json"),
  "track_report" => artifact("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_TRACK_REPORT.md")
}

p30_dir = "papers/30-three-disk-nonconstant-roof-determinant/notes"
p31_dir = "papers/31-level11-conjugacy-owner-ledger/notes"
p33_dir = "papers/33-bolza-control-matched-census/notes"

p30 = {
  "patch" => artifact("#{p30_dir}/stage4_prime_revision_patch_round2.json"),
  "revised_draft" => artifact("#{p30_dir}/stage4_prime_revision_round2.tex"),
  "apply_report" => artifact("#{p30_dir}/stage4_prime_revision_round2.tex.apply-report.json"),
  "revision_evidence_bundle" => artifact("#{p30_dir}/stage4_prime_revision_evidence_bundle_round2.json"),
  "support_evidence_bundle" => artifact("#{p30_dir}/stage4_prime_support_evidence_bundle_round2.json"),
  "build_receipt" => artifact("#{p30_dir}/stage4_prime_preview_build_receipt_round2.json"),
  "preview_pdf" => artifact("#{p30_dir}/stage4_prime_revision_round2.pdf"),
  "completion_report" => artifact("#{p30_dir}/stage4_prime_completion_report_round2.md"),
  "final_audit" => artifact("#{p30_dir}/stage4_prime_final_audit_round2.json")
}

p31 = {
  "patch" => artifact("#{p31_dir}/stage4_prime_revision_patch_round2.json"),
  "revised_draft" => artifact("#{p31_dir}/stage4_prime_revision_round2.tex"),
  "apply_report" => artifact("#{p31_dir}/stage4_prime_revision_round2.tex.apply-report.json"),
  "revision_evidence_bundle" => artifact("#{p31_dir}/stage4_prime_revision_evidence_bundle_round2.json"),
  "support_evidence_bundle" => artifact("#{p31_dir}/stage4_prime_support_evidence_bundle_round2.json"),
  "build_receipt" => artifact("#{p31_dir}/stage4_prime_preview_build_receipt_round2.json"),
  "preview_pdf" => artifact("#{p31_dir}/stage4_prime_revision_round2.pdf"),
  "completion_report" => artifact("#{p31_dir}/stage4_prime_completion_report_round2.md"),
  "final_audit" => artifact("#{p31_dir}/stage4_prime_final_audit_round2.json")
}

p33 = {
  "input_manifest" => artifact("#{p33_dir}/stage3_prime_round4_input_manifest.json"),
  "precommitment" => artifact("#{p33_dir}/stage3_prime_round4_precommitment.json"),
  "immutable_invalid_verdict" => artifact("#{p33_dir}/stage3_prime_round4_verdict_record.json"),
  "phase2a_validation" => artifact("#{p33_dir}/stage3_prime_round4_phase2a_validation.json"),
  "abort_record" => artifact("#{p33_dir}/stage3_prime_round4_abort_record.json"),
  "checker_receipt" => artifact("#{p33_dir}/stage3_prime_round4_checker_receipt.json"),
  "boundary_validation" => artifact("#{p33_dir}/stage3_prime_round4_boundary_validation.json"),
  "verification_report" => artifact("#{p33_dir}/stage3_prime_round4_verification_report.md"),
  "completion_receipt" => artifact("#{p33_dir}/stage3_prime_round4_completion_receipt.json")
}

report = <<~MD
  # Round 10 — Stage 4′ / Stage 3′ Round 4 completion report

  Date: **#{DATE} UTC**

  Status: **THREE TRACKS CLOSED / MANDATORY AUTHOR CHECKPOINT**

  The authorized five-paper round is complete within its exact boundary. P30 and
  P31 completed author-side Stage 4′; P29 and P32 received a hash-bound Stage 4′
  authorization request only; P33 started a fresh Stage 3′ Round 4 and aborted
  fail-closed at its first immutable Phase-2A schema failure. No track entered
  Stage 4.5, Stage 5, Stage 6, canonical promotion, scientific-result refresh, or
  Route advancement.

  ## Paper-level outcome

  | Paper | Controlling outcome | Concrete progress | Next gated action |
  |---|---|---|---|
  | P29 | Stage 4′ request prepared; no revision executed | Four residual roadmap items plus `NEW-1` are mapped to 8 exact targets / 10 block-operation pairs. The request adds a replay/crosswalk, stop map, three control stop states, a labeled unexecuted fixture, and removes the independence overstatement. | Exact author confirmation of the frozen P29/P32 request. |
  | P30 | **Stage 4′ author-side complete** | 5/5 residuals resolved by 14 authorized operations; 113/127 base blocks preserved; 54/54 dated metadata queries logged; 28-row passage matrix; two notes-only correction records; clean 16-page preview. | Fresh Stage 4.5 audit authorization. |
  | P31 | **Stage 4′ author-side complete** | 8/8 residuals resolved by 20 authorized operations; 93/111 base blocks preserved; 20/20 dated metadata queries logged; 24-row method matrix; two notes-only closest-work records; clean 13-page preview. | Fresh Stage 4.5 audit authorization. |
  | P32 | Stage 4′ request prepared; no revision executed | Seven residual roadmap items are mapped to 18 exact targets / 26 block-operation pairs. The request specifies closest-work comparison, commit-pinned artifact inventory, formal definitions, AN-1--AN-5 closure, a 51-row replay/matrix, and a bounded conditional inequality lemma. | Exact author confirmation of the frozen P29/P32 request. |
  | P33 | **Stage 3′ Round 4 aborted fail-closed** | Phase 1 passed with 13 precommitted rows (7 must, 6 should) and 201 checks. The first immutable Phase-2A verdict semantically read 5 FULL / 8 PARTIAL / 0 other, but failed the official schema with exactly 35 errors. | A wholly fresh Round 5 using a schema-correct emitter/template; Round 4 remains immutable. |

  ## Track A — P30/P31 Stage 4′

  The original joint request remained bound to JSON SHA-256
  `a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688`
  and Markdown SHA-256
  `4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a`.
  All 13 residual items were addressed by 34 operations inside the 37 proposed
  targets. There were no registered ClaimIntent surfaces, claim-strength
  replacements, collateral authorizations, or section-count changes.

  P30 final bindings:

  - patch: `#{p30.fetch("patch").fetch("sha256")}`;
  - revised anchored draft: `#{p30.fetch("revised_draft").fetch("sha256")}`;
  - apply report: `#{p30.fetch("apply_report").fetch("sha256")}`;
  - revision-evidence bundle: `#{p30.fetch("revision_evidence_bundle").fetch("sha256")}`;
  - support bundle: `#{p30.fetch("support_evidence_bundle").fetch("sha256")}`;
  - preview PDF: `#{p30.fetch("preview_pdf").fetch("sha256")}`;
  - final audit: **PASS 86/86**, `#{p30.fetch("final_audit").fetch("sha256")}`.

  P31 final bindings:

  - patch: `#{p31.fetch("patch").fetch("sha256")}`;
  - revised anchored draft: `#{p31.fetch("revised_draft").fetch("sha256")}`;
  - apply report: `#{p31.fetch("apply_report").fetch("sha256")}`;
  - revision-evidence bundle: `#{p31.fetch("revision_evidence_bundle").fetch("sha256")}`;
  - support bundle: `#{p31.fetch("support_evidence_bundle").fetch("sha256")}`;
  - preview PDF: `#{p31.fetch("preview_pdf").fetch("sha256")}`;
  - final audit: **PASS 85/85**, `#{p31.fetch("final_audit").fetch("sha256")}`.

  Writer and apply roles were separated. Noncompliant or defective intermediate
  attempts—including P30 control-byte/TeX-escape defects and P31 overfull layout—
  are retained under explicitly superseded directories and excluded from the final
  evidence chains. A fresh root-context replay produced the current drafts. Both
  official bundle validators pass. Independent four-pass LuaLaTeX/BibTeX builds
  reproduce 16 and 13 pages with zero undefined citations, undefined references,
  missing glyphs, fatal errors, or overfull boxes. The nonblocking underfull counts
  are recorded as P30=8 and P31=14.

  ## Track B — P29/P32 request preparation

  The request is frozen at:

  - JSON SHA-256 `#{p29_p32.fetch("request_json").fetch("sha256")}`;
  - reader Markdown SHA-256 `#{p29_p32.fetch("request_markdown").fetch("sha256")}`;
  - validation SHA-256 `#{p29_p32.fetch("validation").fetch("sha256")}`.

  The dedicated replay passes **377 checks** over 11 residual roadmap items plus
  one regression, 26 exact target entries, 36 block-operation pairs, and six
  support scopes. Status remains `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION`.
  Manuscript, bibliography, PDF, patch, scientific execution, result refresh, and
  Route mutations are all zero for P29/P32 in this round.

  ## Track C — P33 Stage 3′ Round 4

  Round id: `p33-stage3-prime-round4-2026-09-03`.

  Phase 1 used a fresh revision-blind role context and passed. Phase 2A used a
  distinct fresh persuasion-blind role context. Its first verdict was frozen
  before validation. The official Draft-2020-12 schema then found exactly 35
  errors: one prohibited top-level property, 13 prohibited row properties, 13
  object-versus-array `evidence_anchor` errors, and eight string-versus-object
  `residual_gap` errors. Under the no-retry rule after evidence exposure, the
  controlling terminal token is:

  `[RE-REVIEW-ABORT: phase2a_lint_failed]`

  The 5 FULL / 8 PARTIAL semantic self-count is noncontrolling. No Response,
  Phase 2B, traceability matrix, official checker execution, or decision was
  created. The checker receipt is `NOT_RUN`; all 37 prior Round-3 files and all
  protected science/Route surfaces remain byte-preserved.

  Key P33 hashes: manifest `#{p33.fetch("input_manifest").fetch("sha256")}`;
  precommitment `#{p33.fetch("precommitment").fetch("sha256")}`; immutable invalid
  verdict `#{p33.fetch("immutable_invalid_verdict").fetch("sha256")}`; Phase-2A
  validation `#{p33.fetch("phase2a_validation").fetch("sha256")}`; abort
  `#{p33.fetch("abort_record").fetch("sha256")}`; completion receipt
  `#{p33.fetch("completion_receipt").fetch("sha256")}`.

  ## Route A and frozen dynamical systems

  The route definitions remain byte-frozen:

  - `skills/route-a-evaluator.md`: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
  - `skills/route-b-evaluator.md`: `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7f9595`.

  This batch is still Route-A foundation/interface work. Formal Route-A tuples are
  **0/5**; positive arithmetic A2 is **0/5**; A3 and A4 are **0/5**; Route B is
  **0/5**. The five initial systems remain the same: level-(3) Gaussian Bianchi
  geodesic flow (P29), no-eclipse equilateral three-disk flow at `d=6a` (P30), a
  fixed positive time-change of the `Gamma_0(11)` geodesic flow (P31), the
  genus-two pure-homology tower (P32), and the unit-speed Bolza flow plus separately
  typed matched control (P33). Clock, primitive, owner, inverse, normalization,
  cutoff, and target-blind restrictions are unchanged.

  ## Validation ledger and write boundary

  - P30 final audit: 86/86 PASS; P31 final audit: 85/85 PASS.
  - P29/P32 exact-request validation: 377/377 PASS.
  - P33 Phase-1 audit: 201/201 PASS; Phase-2A schema: 35 errors and required abort.
  - Batch frozen-boundary replay: 195/195 PASS across 92 paths, including the 15
    canonical manuscript/bibliography/PDF files and eight P33 Round-3 per-paper
    controls.
  - Final independent preview rebuild: P30 16 pages, P31 13 pages; all blocking
    TeX counters and overfull boxes are zero.
  - Citation style remains current `plainnat` numeric.

  The only new files are versioned notes, review/request/provenance artifacts,
  batch records, status documents, and audit tools. Canonical papers, canonical
  bibliographies, canonical PDFs, `code/experiments/results`, scientific values,
  and Route state are unchanged.

  The batch now stops at the mandatory author checkpoint. A short `确认` against
  that checkpoint is sufficient for the precisely listed next actions; it does
  not authorize Stage 5/6, canonical promotion, new science, result refresh, or
  Route advancement.
MD

File.binwrite(File.join(ROOT, REPORT_PATH), report)

receipt = {
  "schema_version" => "round10-stage4-prime-and-round4-completion-receipt/1.0",
  "generated_date_utc" => DATE,
  "batch" => "Round 10 / Papers 29--33",
  "status" => "THREE_TRACKS_CLOSED_AWAITING_MANDATORY_AUTHOR_CHECKPOINT",
  "authority" => authority,
  "completion_report" => artifact(REPORT_PATH),
  "papers" => {
    "P29" => {
      "status" => "STAGE4_PRIME_REQUEST_PREPARED_AWAITING_EXACT_AUTHORIZATION",
      "residual_items" => 4,
      "regressions" => 1,
      "exact_target_entries" => 8,
      "block_operation_pairs" => 10,
      "manuscript_writes" => 0
    },
    "P30" => {
      "status" => "STAGE4_PRIME_AUTHOR_SIDE_COMPLETE_AWAITING_STAGE4_5_AUTHORIZATION",
      "residual_items_resolved" => 5,
      "patch_operations" => 14,
      "preserved_base_blocks" => "113/127",
      "literature_queries_http_200" => "54/54",
      "matrix_rows" => 28,
      "preview_pages" => 16,
      "final_audit_checks" => "86/86",
      "artifacts" => p30
    },
    "P31" => {
      "status" => "STAGE4_PRIME_AUTHOR_SIDE_COMPLETE_AWAITING_STAGE4_5_AUTHORIZATION",
      "residual_items_resolved" => 8,
      "patch_operations" => 20,
      "preserved_base_blocks" => "93/111",
      "literature_queries_http_200" => "20/20",
      "matrix_rows" => 24,
      "preview_pages" => 13,
      "final_audit_checks" => "85/85",
      "artifacts" => p31
    },
    "P32" => {
      "status" => "STAGE4_PRIME_REQUEST_PREPARED_AWAITING_EXACT_AUTHORIZATION",
      "residual_items" => 7,
      "regressions" => 0,
      "exact_target_entries" => 18,
      "block_operation_pairs" => 26,
      "manuscript_writes" => 0
    },
    "P33" => {
      "status" => "STAGE3_PRIME_ROUND4_ABORTED_PHASE2A_LINT_FAILED_AWAITING_FRESH_ROUND5_AUTHORIZATION",
      "round_id" => "p33-stage3-prime-round4-2026-09-03",
      "phase1_checks" => "201/201",
      "phase2a_schema_errors" => 35,
      "semantic_counts_noncontrolling" => {
        "FULLY_ADDRESSED" => 5,
        "PARTIALLY_ADDRESSED" => 8,
        "OTHER" => 0
      },
      "official_checker" => "NOT_RUN",
      "decision_emitted" => false,
      "terminal_marker" => "[RE-REVIEW-ABORT: phase2a_lint_failed]",
      "artifacts" => p33
    }
  },
  "p29_p32_request" => p29_p32.merge(
    "validation_checks" => "377/377",
    "residual_items" => 11,
    "regressions" => 1,
    "exact_target_entries" => 26,
    "block_operation_pairs" => 36,
    "registered_claim_surfaces" => 0,
    "status" => "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION"
  ),
  "validation" => {
    "p30_final_audit" => "PASS_86_OF_86",
    "p31_final_audit" => "PASS_85_OF_85",
    "p29_p32_request" => "PASS_377_OF_377",
    "p33_phase1" => "PASS_201_OF_201",
    "p33_phase2a" => "ABORT_REQUIRED_35_SCHEMA_ERRORS",
    "batch_boundary" => "PASS_195_OF_195_ACROSS_92_FROZEN_PATHS",
    "independent_build" => {
      "P30" => "16_PAGES_ZERO_BLOCKING_TEX_AND_ZERO_OVERFULL",
      "P31" => "13_PAGES_ZERO_BLOCKING_TEX_AND_ZERO_OVERFULL"
    }
  },
  "route" => {
    "route_a_sha256" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
    "route_b_sha256" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7f9595",
    "formal_route_a_tuples" => "0/5",
    "positive_arithmetic_a2" => "0/5",
    "a3" => "0/5",
    "a4" => "0/5",
    "route_b_invocations" => "0/5",
    "changed" => false
  },
  "write_boundary" => {
    "canonical_manuscript_bibliography_pdf_files_unchanged" => "15/15",
    "science_results_unchanged" => true,
    "initial_systems_unchanged" => true,
    "citation_style" => "plainnat_numeric_current",
    "stage4_5_invoked" => false,
    "stage5_invoked" => false,
    "stage6_invoked" => false,
    "canonical_promotion" => false,
    "new_scientific_execution" => false,
    "result_refresh" => false
  },
  "next_checkpoint" => {
    "confirmation_token" => "确认",
    "actions" => [
      "P29_P32_EXECUTE_EXACT_HASH_BOUND_STAGE4_PRIME_REQUEST",
      "P30_P31_START_FRESH_STAGE4_5_AUDIT",
      "P33_START_FRESH_STAGE3_PRIME_ROUND5_WITH_SCHEMA_CORRECT_EMITTER"
    ],
    "later_stages_or_route_authorized" => false
  }
}

File.binwrite(File.join(ROOT, RECEIPT_PATH), "#{JSON.pretty_generate(receipt)}\n")

checkpoint = <<~MD
  # Round 10 — mandatory checkpoint after Stage 4′ / Round 4

  Date: **#{DATE} UTC**

  Status: **STOP / AWAITING EXPLICIT AUTHOR CONFIRMATION**

  Completion report SHA-256: `#{sha(REPORT_PATH)}`  
  Completion receipt SHA-256: `#{sha(RECEIPT_PATH)}`

  A short reply **`确认`** authorizes exactly the following three-track next round:

  1. **P29/P32 — execute Stage 4′** only against
     `BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json`
     SHA-256 `#{p29_p32.fetch("request_json").fetch("sha256")}` and its reader
     Markdown SHA-256 `#{p29_p32.fetch("request_markdown").fetch("sha256")}`.
     Execution is limited to the listed 11 residual items plus one regression,
     26 exact target entries, 36 block-operation pairs, and six support scopes.
     Any science-value change, registered-claim rewrite, structural overrun,
     canonical write, failed test, or out-of-scope requirement stops for review.
  2. **P30/P31 — start fresh Stage 4.5** over the current versioned Stage-4′
     drafts, notes-side bibliographies, evidence bundles, logs, and receipts.
     This authorizes audit/review only: no silent repair, canonical promotion,
     Stage 5, or scientific-result refresh.
  3. **P33 — start a wholly fresh Stage 3′ Round 5** with a new round id,
     new manifest, fresh role-separated Phase-1/Phase-2A contexts, and a
     schema-correct verdict emitter/template validated before evidence exposure.
     All Round-4 artifacts remain immutable. Any first-evidence lint failure again
     aborts fail-closed without retry.

  The confirmation does **not** authorize Stage 5/6, submission, canonical
  manuscript/bibliography/PDF replacement, new scientific computation, result
  refresh, Route-A credit, Route-B invocation, or changes to any frozen initial
  dynamical-system/clock/primitive/owner/normalization/cutoff restriction.

  Until the exact confirmation is received, all three tracks remain stopped.
MD

File.binwrite(File.join(ROOT, CHECKPOINT_PATH), checkpoint)

TARGETS.each do |path|
  puts "#{path} #{sha(path)} #{File.size(File.join(ROOT, path))}"
end
