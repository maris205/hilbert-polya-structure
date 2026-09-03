#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.freeze
WORKFLOW_DATE = "2026-09-04"

FILES = {
  author_event: ["BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHOR_EVENT_20260904.txt", "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812"],
  authorization_record: ["BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECORD.md", "ced9a1452d71b0dc119d6e9b2a180fe446f7f6b381f5d7895459c6289642f12b"],
  authorization_receipt: ["BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json", "7fda096bc17ab453ba2defa5301838ebc9e4056e48282f2eef6783aa96381ddf"],
  input_freeze: ["BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json", "87ce645eeccbd3a179d05ee48d7abe8c468e1a8f04e9e84cd1ca4037bf95ccff"],
  p29_p32_request: ["BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json", "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b"],
  p29_p32_request_md: ["BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.md", "74045f2b6758333d6dc1792e5e5a40052a559ed9f983a88b6154e37aa3e6f63d"],
  p29_p32_validation: ["BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED_VALIDATION.json", "947e7203cc22109969831aa0bee066dbc2b0fa5415090c6781aa3b33d8f7dd80"],
  p29_p32_receipt: ["BATCH_ROUND10_P29_P32_STAGE4_PRIME_SOURCE_FINALIZATION_SCOPE_CHECKPOINT_RECEIPT.json", "160e13e777f7545e9fa08c73adc51e5de5c001b0284155482bcbed72ac86a4bb"],
  p30_p31_incident: ["BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_EXPANSION_FAIL_CLOSED_INCIDENT_P30_P31.json", "7833c8e8796ba1fa691dfaad95460406fd8026e8d12a6d6d9665011d41685b6e"],
  p30_p31_request: ["BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json", "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135"],
  p30_p31_request_md: ["BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.md", "858256909b6d30423e22977bfd8bebb7d4b5f46c8406890e17ca65cc5f9a9960"],
  p30_p31_validation: ["BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json", "b2ae5c8e5c6fa542bd004cca6b9dd97451d16ccb7847b05ce25daa4006d33a97"],
  p30_p31_receipt: ["BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_PREPARATION_RECEIPT.json", "460dfda1ed4e443181565fcaab40d87834d2a624117e801a2fd31bdd8cb5235f"],
  p33_request: ["BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json", "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65"],
  p33_request_md: ["BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.md", "b36b65521481d6a8f568b78ac2ba7b2f09c638b5f26fd9fa9b5255ba9af9d6e0"],
  p33_validation: ["BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_VALIDATION.json", "cfec67180ec0f6e8e24909af47f4a62de7402fb3eedd060cb6abcd318bb697b8"],
  p33_receipt: ["BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_RECEIPT.json", "70e24304b48e9d1981273e064e58b41a60de9126169e8971298390d89f783a26"],
  provenance_timestamp_correction: ["BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_PROVENANCE_TIMESTAMP_CORRECTION.json", "0ac6f56ec6b7cafbc30bda57c687b7d560913d36e4989cbd5b083015db586aff"],
  p33_support_validation: ["papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support_validation.json", "25ff420bb5a2f88d245b9c78ffe1ae68cd9108b3e991994e36e73300968be0df"]
}.freeze

OUTPUTS = {
  report: "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_COMPLETION_REPORT.md",
  audit: "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_FINAL_AUDIT.json",
  receipt: "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_COMPLETION_RECEIPT.json",
  checkpoint: "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_MANDATORY_CHECKPOINT.md"
}.freeze

def path(relative)
  ROOT / relative
end

def sha(relative)
  Digest::SHA256.file(path(relative)).hexdigest
end

def binding(relative)
  p = path(relative)
  { "path" => relative, "sha256" => Digest::SHA256.file(p).hexdigest, "bytes" => p.size }
end

def load_json(relative)
  JSON.parse(path(relative).read)
end

def write_json(relative, value)
  path(relative).write(JSON.pretty_generate(value) + "\n")
end

def write_text(relative, value)
  path(relative).write(value.rstrip + "\n")
end

checks = []
check = lambda do |id, condition, detail = nil|
  checks << { "check_id" => id, "status" => condition ? "PASS" : "FAIL", "detail" => detail }.compact
end

FILES.each do |key, (relative, expected)|
  exists = path(relative).file?
  check.call("binding:#{key}:exists", exists, relative)
  check.call("binding:#{key}:sha256", exists && sha(relative) == expected,
             { "path" => relative, "expected" => expected, "actual" => exists ? sha(relative) : nil })
end

p29_p32 = load_json(FILES.fetch(:p29_p32_request).first)
p29_p32_validation = load_json(FILES.fetch(:p29_p32_validation).first)
p29_p32_receipt = load_json(FILES.fetch(:p29_p32_receipt).first)
p30_p31 = load_json(FILES.fetch(:p30_p31_request).first)
p30_p31_validation = load_json(FILES.fetch(:p30_p31_validation).first)
p33 = load_json(FILES.fetch(:p33_request).first)
p33_validation = load_json(FILES.fetch(:p33_validation).first)
p33_support_validation = load_json(FILES.fetch(:p33_support_validation).first)

expected_p29_p32 = {
  "original_authorized_replace_block_pairs" => 36,
  "additional_required_replace_block_pairs" => 10,
  "block_operation_pairs" => 46,
  "registered_citation_contexts" => 52,
  "passage_bounded_total" => 35,
  "explicit_bounded_unavailability" => 17
}
expected_p29_p32.each do |key, expected|
  check.call("p29-p32:count:#{key}", p29_p32.dig("totals", key) == expected,
             { "expected" => expected, "actual" => p29_p32.dig("totals", key) })
end
check.call("p29-p32:request-status", p29_p32["status"] == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION")
check.call("p29-p32:validation", p29_p32_validation["verdict"] == "PASS" && p29_p32_validation["passed"] == 20 && p29_p32_validation["failed"] == 0)
check.call("p29-p32:checkpoint-receipt", p29_p32_receipt["verdict"] == "PASS" && p29_p32_receipt.dig("counts", "checks_passed") == 44 && p29_p32_receipt.dig("counts", "checks_failed") == 0)

expected_p30_p31 = {
  "original_block_operation_pairs" => 34,
  "new_scope_closure_pairs" => 13,
  "expanded_block_operation_pairs" => 47,
  "derived_matrix_regenerations" => 2,
  "source_finalization_rows" => 48,
  "bounded_locator_available" => 25,
  "bounded_explicit_unavailability" => 23,
  "bibliography_operations" => 0
}
expected_p30_p31.each do |key, expected|
  check.call("p30-p31:count:#{key}", p30_p31.dig("totals", key) == expected,
             { "expected" => expected, "actual" => p30_p31.dig("totals", key) })
end
check.call("p30-p31:request-status", p30_p31["status"] == "AWAITING_NEW_EXPLICIT_AUTHOR_CONFIRMATION")
check.call("p30-p31:validation", p30_p31_validation["status"] == "PASS" && p30_p31_validation.dig("counts", "passed") == 84 && p30_p31_validation.dig("counts", "failed") == 0)
check.call("p30-p31:timestamp-corrected", p30_p31.dig("provenance_timestamp_correction", "status") == "REISSUED_BEFORE_AUTHOR_CONFIRMATION")
p30_p31_human = path(FILES.fetch(:p30_p31_request_md).first).read
check.call(
  "p30-p31:human-request-current-machine-binding",
  p30_p31_human.scan(FILES.fetch(:p30_p31_request).last).length == 1 &&
    p30_p31_human.scan(FILES.fetch(:p30_p31_incident).last).length == 1 &&
    !p30_p31_human.include?("bae806e48a240b9a139b84c16aefb32c1199406b43d1cfe9c142c47768d94705"),
  { "human_request" => FILES.fetch(:p30_p31_request_md).first }
)

expected_p33 = {
  "carried_unique_block_operation_pairs" => 35,
  "new_issue_actions" => 2,
  "total_mapped_pairs_with_item_or_action_provenance" => 41,
  "total_unique_block_operation_pairs" => 37,
  "replace_block_pairs" => 37,
  "supporting_operations" => 7,
  "artifact_inventory_rows" => 43,
  "source_use_rows" => 48,
  "exact_passage_locators" => 0,
  "explicit_bounded_unavailability_rows" => 48,
  "valid_synthetic_fixtures" => 2,
  "invalid_synthetic_fixtures" => 12,
  "production_components_available" => 0
}
expected_p33.each do |key, expected|
  check.call("p33:count:#{key}", p33.dig("counts", key) == expected,
             { "expected" => expected, "actual" => p33.dig("counts", key) })
end
check.call("p33:request-status", p33["status"] == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION")
check.call("p33:validation", p33_validation["status"] == "PASS_SCOPE_EXPANSION_REQUEST_READY_AWAITING_CONFIRMATION" && p33_validation["checks_run"] == 701 && p33_validation["failure_count"] == 0)
check.call("p33:support-validation", p33_support_validation["status"] == "PASS_SUPPORT_COMPLETE_SCOPE_STOPPED_REQUEST_REISSUE_REQUIRED" && p33_support_validation["failure_count"] == 0)
check.call("p33:superseded-chain", p33.dig("superseded_scope_attempt1", "status") == "NONCONTROLLING_SUPERSEDED_DUE_TO_UNLISTED_TARGETS" && p33.dig("superseded_scope_attempt1", "may_be_used_for_apply") == false)

# Replay every unique path/hash binding in the execution input freeze.
freeze = load_json(FILES.fetch(:input_freeze).first)
frozen_bindings = []
walk = lambda do |node|
  case node
  when Hash
    if node["path"].is_a?(String) && node["sha256"].is_a?(String) && node["sha256"].match?(/\A[0-9a-f]{64}\z/)
      frozen_bindings << [node["path"], node["sha256"]]
    end
    node.each_value { |value| walk.call(value) }
  when Array
    node.each { |value| walk.call(value) }
  end
end
walk.call(freeze)
frozen_bindings.uniq!
frozen_failures = frozen_bindings.filter_map do |relative, expected|
  actual = path(relative).file? ? sha(relative) : nil
  { "path" => relative, "expected" => expected, "actual" => actual } unless actual == expected
end
check.call("freeze:unique-bindings", frozen_bindings.length == 94, { "actual" => frozen_bindings.length, "expected" => 94 })
check.call("freeze:replay", frozen_failures.empty?, { "passed" => frozen_bindings.length - frozen_failures.length, "failed" => frozen_failures.length })

forbidden_outputs = [
  "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round3.tex",
  "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_round3.pdf",
  "papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_revision_patch_round3.json",
  "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round3.tex",
  "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round3.pdf",
  "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_patch_round3.json",
  "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round3.tex",
  "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_round3.pdf",
  "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_revision_patch_round3.json",
  "papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round3.tex",
  "papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_round3.pdf",
  "papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_revision_patch_round3.json",
  "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round5.tex",
  "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_round5.pdf",
  "papers/33-bolza-control-matched-census/notes/stage4_prime_revision_patch_round5.json"
]
forbidden_present = forbidden_outputs.select { |relative| path(relative).exist? }
check.call("boundary:no-successor-manuscript-output", forbidden_present.empty?, forbidden_present)

mutation_boundary = p33_validation.fetch("mutation_boundary")
expected_false = %w[
  bibliography_appended
  patch_emitted_or_applied
  new_draft_or_pdf_emitted
  build_run
  scientific_producer_or_census_run
  result_refreshed
  canonical_or_route_or_initial_system_changed
]
check.call("boundary:p33-no-mutation", expected_false.all? { |key| mutation_boundary[key] == false }, mutation_boundary)

aggregate = {
  "papers" => 5,
  "old_authorized_replace_block_pairs" => 105,
  "newly_detected_required_pairs" => 25,
  "expanded_replace_block_pairs" => 130,
  "applied_replace_block_pairs" => 0,
  "matrix_regenerations_pending" => 2,
  "p33_bibliography_entries_pending" => 2,
  "p33_support_operations" => 7,
  "source_use_rows_finalized" => 148,
  "passage_or_bounded_locators" => 60,
  "explicit_bounded_unavailability_rows" => 88,
  "scientific_experiments_or_producer_runs" => 0,
  "route_promotions" => 0
}
check.call("aggregate:replace-block-arithmetic", 46 + 47 + 37 == 130)
check.call("aggregate:scope-expansion-arithmetic", 10 + 13 + 2 == 25 && 105 + 25 == 130)
check.call("aggregate:source-arithmetic", 52 + 48 + 48 == 148 && 35 + 25 == 60 && 17 + 23 + 48 == 88)

failed_checks = checks.count { |row| row["status"] == "FAIL" }
status = failed_checks.zero? ? "PASS_SCOPE_REISSUE_READY_AWAITING_EXPLICIT_CONFIRMATION" : "FAIL_CLOSED"
generated_at = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")

audit = {
  "schema_version" => "round10-stage4-prime-correction-scope-reissue-final-audit/1.0",
  "generated_at_utc" => generated_at,
  "workflow_date" => WORKFLOW_DATE,
  "status" => status,
  "checks_run" => checks.length,
  "checks_passed" => checks.length - failed_checks,
  "checks_failed" => failed_checks,
  "checks" => checks,
  "aggregate_counts" => aggregate,
  "freeze_replay" => {
    "unique_bindings" => frozen_bindings.length,
    "passed" => frozen_bindings.length - frozen_failures.length,
    "failed" => frozen_failures.length,
    "failures" => frozen_failures
  },
  "stage_boundaries" => {
    "manuscript_patch_or_apply_executed" => false,
    "successor_draft_pdf_or_build_executed" => false,
    "p30_p31_matrix_regeneration_executed" => false,
    "p33_bibliography_append_executed" => false,
    "fresh_stage4_5_executed" => false,
    "canonical_or_science_or_result_mutation" => false,
    "route_or_initial_system_mutation" => false,
    "citation_style" => "plainnat numeric"
  },
  "next_legal_action" => "Obtain one new explicit author confirmation bound to all three expanded machine requests; then execute only the listed Stage 4-prime corrections and direct validations."
}
write_json(OUTPUTS.fetch(:audit), audit)

abort("final audit failed closed; inspect #{OUTPUTS.fetch(:audit)}") unless failed_checks.zero?

report = <<~MD
  # Round 10 Stage 4′ correction scope-reissue completion report

  Workflow date: #{WORKFLOW_DATE}  
  Status: **PASS — expanded requests ready; awaiting a new explicit author confirmation**

  ## Outcome

  The prior confirmation was bound correctly and all authorized read-only/source/support work completed, but the pre-apply audit found 25 present-tense manuscript surfaces that were not named in the three earlier requests. The stop conditions therefore fired before any patch, bibliography append, matrix regeneration, successor draft, PDF, or build. This is a scope correction, not a scientific-result change.

  | Paper | Concrete progress in this turn | Expanded pending manuscript scope | Current gate |
  |---|---|---:|---|
  | P29 | 22/22 source contexts finalized: 13 exact locators, 9 bounded unavailable | 31 `replace_block` (26 + 5) | awaiting expanded confirmation |
  | P30 | 26/26 source contexts finalized: 18 locators, 8 bounded unavailable | 34 `replace_block` (29 + 5), plus 1 matrix regeneration | awaiting expanded confirmation |
  | P31 | 22/22 source contexts finalized: 7 locators, 15 bounded unavailable | 13 `replace_block` (5 + 8), plus 1 matrix regeneration | awaiting expanded confirmation |
  | P32 | 30/30 source contexts finalized: 18 new exact locators, 4 retained bounded scopes, 8 bounded unavailable | 15 `replace_block` (10 + 5) | awaiting expanded confirmation |
  | P33 | 43/43 commit-pinned artifacts replayed; 48/48 uses bounded; 2 valid + 12 invalid synthetic fixtures pass their oracle; production components remain absent | 37 `replace_block` (35 + 2), exactly 2 Bib appends; 7 support operations are now evidence-bound | awaiting expanded confirmation |

  Aggregate: **105 old + 25 newly required = 130 exact `replace_block` pairs; 0 applied**. Across the five papers, 148 source-use rows are finalized as 60 exact/retained bounded locators and 88 explicit bounded-unavailability rows. P33's synthetic conformance work is not a scientific producer run, census, or result refresh.

  ## Integrity and boundaries

  - The three request-track validations are **805/805 PASS** (`20 + 84 + 701`), including an explicit human-request-to-machine-SHA binding check.
  - The execution-input freeze replay is **94/94 PASS**.
  - P29--P33 working drafts and bibliographies remain at their frozen hashes; both P30/P31 matrices remain unchanged.
  - Canonical manuscript/Bib/PDF, science/results, Route crosswalks, and initial dynamical-system specifications remain unchanged.
  - No fresh Stage 4.5, re-review, Stage 5, or Stage 6 was started.
  - The batch remains at foundation/interface research, with paper-specific Route states retained: notably P30 is `A0_FAIL / A2_NOT_ELIGIBLE`; formal tuples are `UNASSIGNED 5/5`, positive A2 `0/5`, A3 `0/5`, A4 `0/5`, and Route B `0/5`.
  - Scientific experiments/producer/census runs in this turn: `0`. Citation style remains `plainnat` numeric.

  ## Exact successor requests

  - P29/P32: `#{FILES.fetch(:p29_p32_request).last}`
  - P30/P31: `#{FILES.fetch(:p30_p31_request).last}`
  - P33: `#{FILES.fetch(:p33_request).last}`

  The next confirmation authorizes only these expanded Stage 4′ corrections, the two notes-side matrix regenerations, the two exact P33 bibliography appends, a fresh P33 authority chain, and direct isolated build/validation. It does not authorize fresh Stage 4.5 or any scientific/Route/canonical promotion.
MD
write_text(OUTPUTS.fetch(:report), report)

receipt = {
  "schema_version" => "round10-stage4-prime-correction-scope-reissue-completion-receipt/1.0",
  "generated_at_utc" => generated_at,
  "workflow_date" => WORKFLOW_DATE,
  "status" => status,
  "aggregate_counts" => aggregate,
  "authority" => FILES.slice(:author_event, :authorization_record, :authorization_receipt, :input_freeze).transform_values { |relative, _| binding(relative) },
  "expanded_requests" => {
    "P29_P32" => binding(FILES.fetch(:p29_p32_request).first),
    "P30_P31" => binding(FILES.fetch(:p30_p31_request).first),
    "P33" => binding(FILES.fetch(:p33_request).first)
  },
  "track_validations" => {
    "P29_P32" => binding(FILES.fetch(:p29_p32_validation).first),
    "P30_P31" => binding(FILES.fetch(:p30_p31_validation).first),
    "P33" => binding(FILES.fetch(:p33_validation).first)
  },
  "terminal_artifacts" => {
    "report" => binding(OUTPUTS.fetch(:report)),
    "final_audit" => binding(OUTPUTS.fetch(:audit))
  },
  "freeze_replay" => audit.fetch("freeze_replay"),
  "next_gate" => "MANDATORY_EXPLICIT_AUTHOR_CONFIRMATION_OF_THREE_EXPANDED_MACHINE_REQUESTS"
}
write_json(OUTPUTS.fetch(:receipt), receipt)

checkpoint = <<~MD
  # Round 10 mandatory checkpoint — expanded Stage 4′ correction execution

  Workflow date: #{WORKFLOW_DATE}  
  Current status: **scope reissue complete; no manuscript correction applied**

  ## What the next short confirmation means

  The author may reply with exactly **`确认`**. That reply will bind and approve all `will_address` targets and permitted operations in these three machine requests:

  1. `#{FILES.fetch(:p29_p32_request).first}`  
     SHA-256 `#{FILES.fetch(:p29_p32_request).last}` — 46 exact `replace_block` pairs.
  2. `#{FILES.fetch(:p30_p31_request).first}`  
     SHA-256 `#{FILES.fetch(:p30_p31_request).last}` — 47 exact `replace_block` pairs and exactly two in-place notes-matrix regenerations.
  3. `#{FILES.fetch(:p33_request).first}`  
     SHA-256 `#{FILES.fetch(:p33_request).last}` — 37 unique `replace_block` pairs, exactly two verified bibliography appends, seven evidence-bound support operations, and a required fresh successor authority chain.

  In aggregate, the reply authorizes **130 exact manuscript block replacements**, not 105. It also authorizes direct isolated builds and scope-bound validation/receipts after the exact changes.

  ## Boundaries retained

  The confirmation does **not** authorize fresh Stage 4.5, P33 re-review, Stage 5/6, canonical promotion, scientific producer/enumeration/census execution, result refresh, Route A/B credit, or any change to the five frozen initial dynamical systems. A target-hash mismatch, scientific numerical change, registered-claim strength change beyond a listed contract, structural edit, or out-of-scope need must stop for a new request.

  Evidence: `#{OUTPUTS.fetch(:report)}` (`#{sha(OUTPUTS.fetch(:report))}`), `#{OUTPUTS.fetch(:audit)}` (`#{sha(OUTPUTS.fetch(:audit))}`), and `#{OUTPUTS.fetch(:receipt)}` (`#{sha(OUTPUTS.fetch(:receipt))}`).
MD
write_text(OUTPUTS.fetch(:checkpoint), checkpoint)

puts JSON.pretty_generate(
  "status" => status,
  "checks" => { "passed" => checks.length, "failed" => 0 },
  "outputs" => OUTPUTS.transform_values { |relative| binding(relative) },
  "aggregate_counts" => aggregate
)
