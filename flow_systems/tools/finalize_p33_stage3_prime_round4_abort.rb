#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"

ROOT = File.expand_path("..", __dir__)
PAPER_ROOT = File.join(ROOT, "papers", "33-bolza-control-matched-census")
NOTES = File.join(PAPER_ROOT, "notes")
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite"
VERDICT_SCHEMA = File.join(ARS_ROOT, "ars/shared/contracts/re_review/verdict_record.schema.json")
OFFICIAL_CHECKER = File.join(ARS_ROOT, "ars/scripts/check_re_review_synthesis.py")
ROUND_ID = "p33-stage3-prime-round4-2026-09-03"
MARKER = "[RE-REVIEW-ABORT: phase2a_lint_failed]"
DISCLOSURE = "This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2)."

def assert!(condition, message)
  raise "P33_ROUND4_ABORT_FINALIZATION_FAIL: #{message}" unless condition
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def canonical(value)
  case value
  when Hash
    "{" + value.keys.sort.map { |key| "#{JSON.generate(key)}:#{canonical(value.fetch(key))}" }.join(",") + "}"
  when Array
    "[" + value.map { |child| canonical(child) }.join(",") + "]"
  else
    JSON.generate(value)
  end
end

def jcs_sha256(value)
  Digest::SHA256.hexdigest(canonical(value).encode("UTF-8"))
end

def relative(path)
  path.delete_prefix("#{ROOT}/")
end

def binding(path, json: false)
  row = {"path" => relative(path), "raw_sha256" => sha256(path), "bytes" => File.size(path)}
  row["jcs_sha256"] = jcs_sha256(load_json(path)) if json
  row
end

def verify_frozen!(root, node, checks, prefix)
  case node
  when Hash
    if node.keys.sort == %w[bytes path sha256]
      path = File.join(root, node.fetch("path"))
      assert!(File.file?(path) && !File.symlink?(path), "#{prefix}: missing/symlink #{node.fetch('path')}")
      assert!(File.size(path) == node.fetch("bytes"), "#{prefix}: byte drift #{node.fetch('path')}")
      assert!(sha256(path) == node.fetch("sha256"), "#{prefix}: hash drift #{node.fetch('path')}")
      checks << "#{prefix}:#{node.fetch('path')}"
    else
      node.each { |key, value| verify_frozen!(root, value, checks, "#{prefix}.#{key}") }
    end
  when Array
    node.each_with_index { |value, index| verify_frozen!(root, value, checks, "#{prefix}[#{index}]") }
  end
end

def schema_errors(schema_path, instance_path)
  python = <<~'PY'
    import json, sys
    from jsonschema import Draft202012Validator
    schema = json.load(open(sys.argv[1], encoding="utf-8"))
    instance = json.load(open(sys.argv[2], encoding="utf-8"))
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda e: (list(e.absolute_path), e.message),
    )
    payload = []
    for error in errors:
        path = "/" + "/".join(map(str, error.absolute_path)) if error.absolute_path else "/"
        payload.append({"path": path, "message": error.message})
    print(json.dumps(payload, ensure_ascii=False))
  PY
  stdout, stderr, status = Open3.capture3("python3", "-c", python, schema_path, instance_path)
  assert!(status.success?, "schema validator execution failed: #{stderr}")
  JSON.parse(stdout)
end

paths = {
  "input_freeze" => File.join(NOTES, "stage3_prime_round4_input_freeze.json"),
  "input_manifest" => File.join(NOTES, "stage3_prime_round4_input_manifest.json"),
  "input_manifest_receipt" => File.join(NOTES, "stage3_prime_round4_input_manifest_receipt.json"),
  "precommitment" => File.join(NOTES, "stage3_prime_round4_precommitment.json"),
  "phase1_receipt" => File.join(NOTES, "stage3_prime_round4_phase1_receipt.md"),
  "phase1_validation" => File.join(NOTES, "stage3_prime_round4_phase1_validation.json"),
  "verdict_record" => File.join(NOTES, "stage3_prime_round4_verdict_record.json"),
  "phase2a_semantic_audit" => File.join(NOTES, "stage3_prime_round4_phase2a_semantic_audit.json"),
  "phase2a_receipt" => File.join(NOTES, "stage3_prime_round4_phase2a_receipt.md")
}
paths.each { |name, path| assert!(File.file?(path), "missing #{name}: #{relative(path)}") }

forbidden_downstream = %w[
  stage3_prime_round4_phase2b_integration.json
  stage3_prime_round4_phase2b_validation.json
  stage3_prime_round4_traceability.json
].map { |name| File.join(NOTES, name) }
forbidden_downstream.each { |path| assert!(!File.exist?(path), "downstream artifact exists after failed gate: #{relative(path)}") }

output_paths = {
  "phase2a_validation" => File.join(NOTES, "stage3_prime_round4_phase2a_validation.json"),
  "checker_receipt" => File.join(NOTES, "stage3_prime_round4_checker_receipt.json"),
  "abort_record" => File.join(NOTES, "stage3_prime_round4_abort_record.json"),
  "boundary_validation" => File.join(NOTES, "stage3_prime_round4_boundary_validation.json"),
  "verification_report" => File.join(NOTES, "stage3_prime_round4_verification_report.md"),
  "completion_receipt" => File.join(NOTES, "stage3_prime_round4_completion_receipt.json")
}
output_paths.each { |name, path| assert!(!File.exist?(path), "refusing to overwrite #{name}: #{path}") }

freeze = load_json(paths.fetch("input_freeze"))
manifest = load_json(paths.fetch("input_manifest"))
pre = load_json(paths.fetch("precommitment"))
phase1 = load_json(paths.fetch("phase1_validation"))
verdict = load_json(paths.fetch("verdict_record"))
semantic = load_json(paths.fetch("phase2a_semantic_audit"))
errors = schema_errors(VERDICT_SCHEMA, paths.fetch("verdict_record"))
assert!(!errors.empty?, "verdict unexpectedly schema-valid; abort path is inapplicable")
assert!(errors.length == 35, "unexpected schema error count #{errors.length}")

categories = {
  "top_level_additional_properties" => errors.count { |error| error.fetch("path") == "/" && error.fetch("message").include?("Additional properties") },
  "row_additional_properties" => errors.count { |error| %r{\A/items/[0-9]+\z}.match?(error.fetch("path")) && error.fetch("message").include?("Additional properties") },
  "evidence_anchor_not_array" => errors.count { |error| error.fetch("path").end_with?("/evidence_anchor") && error.fetch("message").include?("not of type 'array'") },
  "residual_gap_not_object" => errors.count { |error| error.fetch("path").end_with?("/residual_gap") && error.fetch("message").include?("not of type 'object'") }
}
assert!(categories == {
  "top_level_additional_properties" => 1,
  "row_additional_properties" => 13,
  "evidence_anchor_not_array" => 13,
  "residual_gap_not_object" => 8
}, "unexpected schema error categories #{categories}")

checks = []
assert!(sha256(VERDICT_SCHEMA) == "b23d1dae82ef383fae9ccbc269d2aa68ed73dd61a47c2a544c1d12e59c39c3f5", "verdict schema hash drift")
checks << "verdict_schema_binding"
assert!(sha256(OFFICIAL_CHECKER) == "8347ec3766857366cc0c6ffd30021afcebf8d0528a83927fabfce9ecb66a59ab", "checker hash drift")
checks << "official_checker_binding"
assert!(phase1.fetch("status") == "PASS", "Phase 1 not PASS")
checks << "phase1_gate_pass"
assert!(manifest.fetch("round_id") == ROUND_ID && pre.fetch("round_id") == ROUND_ID && verdict.fetch("round_id") == ROUND_ID, "round-id chain")
checks << "round_id_chain"
assert!(semantic.fetch("verdict_record_raw_sha256") == sha256(paths.fetch("verdict_record")), "semantic raw binding")
checks << "semantic_raw_binding"
assert!(semantic.fetch("verdict_record_jcs_sha256") == jcs_sha256(verdict), "semantic JCS binding")
checks << "semantic_jcs_binding"
assert!(semantic.dig("withholding", "response_to_reviewers_inspected") == false, "response exposure")
checks << "response_withheld"
assert!(semantic.dig("withholding", "prior_re_review_artifacts_inspected") == false, "prior-round exposure")
checks << "prior_round_withheld"
assert!(File.readlines(paths.fetch("phase2a_receipt"), chomp: true).reverse.find { |line| !line.strip.empty? } == "[EVIDENCE-COMMITTED]", "Phase 2A marker")
checks << "evidence_committed_marker"
verify_frozen!(ROOT, freeze.fetch("round3_preservation"), checks, "round3_preservation")
verify_frozen!(ROOT, freeze.fetch("immutable_boundaries"), checks, "immutable_boundaries")
assert!(freeze.dig("authority", "author_event", "sha256") == "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812", "author event")
checks << "author_event_binding"
assert!(freeze.dig("authority", "authorization_record", "sha256") == "67ad4ce8bfb34676b46ffb96e8c9833c1204ada3ffde1e0dc542ea43c46acca5", "authorization record")
checks << "authorization_record_binding"
assert!(sha256(File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json")) == "c94137879092d7d475b22c8985a8f09073c29027f77a89b8ccb8749acfdac48b", "authorization receipt")
checks << "authorization_receipt_binding"

counts = semantic.dig("counts", "verdicts")
phase2a_validation = {
  "schema_version" => "p33-stage3-prime-round4-phase2a-validation/1.0",
  "generated_at" => "2026-09-03T16:25:00Z",
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "phase" => "phase2a_persuasion_blind_evidence_verdict",
  "status" => "FAIL",
  "terminal_marker" => MARKER,
  "abort_reason" => "phase2a_lint_failed",
  "phase2a_record" => {
    "raw_sha256" => sha256(paths.fetch("verdict_record")),
    "jcs_sha256" => jcs_sha256(verdict),
    "immutable_after_first_emission" => true,
    "retry_used" => false,
    "semantic_counts_noncontrolling" => counts
  },
  "schema_validation" => {
    "schema_path" => VERDICT_SCHEMA,
    "schema_sha256" => sha256(VERDICT_SCHEMA),
    "validator" => "python jsonschema Draft202012Validator",
    "error_count" => errors.length,
    "category_counts" => categories,
    "errors" => errors
  },
  "semantic_self_audit" => {
    "artifact" => binding(paths.fetch("phase2a_semantic_audit"), json: true),
    "reported_status" => semantic.fetch("status"),
    "authority" => "advisory_only; cannot override schema failure"
  },
  "freshness" => {
    "fresh_context" => true,
    "fork_turns" => "none",
    "persuasion_blind" => true,
    "response_to_reviewers_inspected" => false,
    "prior_re_review_artifacts_inspected" => false,
    "phase2a_retry_used" => false
  },
  "downstream" => {
    "phase2b_started" => false,
    "traceability_emitted" => false,
    "official_checker_run" => false,
    "decision_emitted" => false
  }
}
File.write(output_paths.fetch("phase2a_validation"), JSON.pretty_generate(phase2a_validation) + "\n")

checker_receipt = {
  "schema_version" => "p33-stage3-prime-round4-checker-receipt/1.0",
  "paper_id" => "P33",
  "paper_slug" => "33-bolza-control-matched-census",
  "round_id" => ROUND_ID,
  "checked_at" => "2026-09-03T16:26:00Z",
  "checker" => "ARS-Codex 0.1.26 scripts/check_re_review_synthesis.py",
  "checker_sha256" => sha256(OFFICIAL_CHECKER),
  "checker_status" => "NOT_RUN",
  "reason" => "checker_not_run_due_to_phase2a_abort",
  "checker_exit_code" => nil,
  "checker_stdout" => nil,
  "checker_stderr" => nil,
  "decision" => nil,
  "decision_state" => nil,
  "decision_emitted" => false,
  "controlling_status" => "ABORTED",
  "terminal_marker" => MARKER,
  "abort_reason" => "phase2a_lint_failed",
  "phase2b_emitted" => false,
  "traceability_emitted" => false,
  "phase2a_retry_used" => false,
  "response_to_reviewers_exposed" => false,
  "same_family_disclosure" => DISCLOSURE
}
File.write(output_paths.fetch("checker_receipt"), JSON.pretty_generate(checker_receipt) + "\n")

abort_record = {
  "schema_version" => "p33-stage3-prime-round4-abort-record/1.0",
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "recorded_at" => "2026-09-03T16:27:00Z",
  "controlling_status" => "ABORTED",
  "terminal_marker" => MARKER,
  "abort_reason" => "phase2a_lint_failed",
  "phase1" => {
    "status" => "PASS",
    "precommitment_items" => phase1.dig("counts", "precommitted_items"),
    "validation_checks" => phase1.dig("counts", "validation_checks"),
    "fresh_revision_blind_context" => true
  },
  "phase2a" => {
    "record_emitted" => true,
    "record_schema_valid" => false,
    "schema_error_count" => errors.length,
    "schema_error_categories" => categories,
    "committed_semantic_counts_noncontrolling" => counts,
    "retry_used" => false,
    "record_modified_after_emission" => false,
    "fresh_persuasion_blind_context" => true
  },
  "phase2b" => {"started" => false, "response_exposed" => false, "artifact_emitted" => false},
  "official_checker" => {"status" => "NOT_RUN", "reason" => "checker_not_run_due_to_phase2a_abort"},
  "decision" => {"emitted" => false, "decision_state" => nil, "suppressed_candidate" => nil},
  "artifacts" => {
    "input_manifest" => binding(paths.fetch("input_manifest"), json: true),
    "precommitment" => binding(paths.fetch("precommitment"), json: true),
    "phase1_validation" => binding(paths.fetch("phase1_validation"), json: true),
    "verdict_record_invalid_immutable" => binding(paths.fetch("verdict_record"), json: true),
    "phase2a_semantic_audit_advisory" => binding(paths.fetch("phase2a_semantic_audit"), json: true),
    "phase2a_receipt" => binding(paths.fetch("phase2a_receipt")),
    "phase2a_validation" => binding(output_paths.fetch("phase2a_validation"), json: true),
    "checker_not_run_receipt" => binding(output_paths.fetch("checker_receipt"), json: true)
  },
  "same_family_role_separated" => true,
  "independence_claim_made" => false,
  "same_family_disclosure" => DISCLOSURE,
  "next_stage_authorized" => false
}
File.write(output_paths.fetch("abort_record"), JSON.pretty_generate(abort_record) + "\n")

boundary = {
  "schema_version" => "p33-stage3-prime-round4-boundary-validation/1.0",
  "generated_at" => "2026-09-03T16:28:00Z",
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "status" => "PASS",
  "controlling_round_status" => "ABORTED",
  "terminal_marker" => MARKER,
  "round3_preservation" => {
    "frozen_file_count" => freeze.dig("round3_preservation", "file_count"),
    "rehash_status" => "PASS",
    "abort_record_preserved" => true,
    "invalid_attempt_incident_preserved" => true
  },
  "freshness" => {
    "phase1_context" => "fresh fork_turns=none, revision-blind",
    "phase2a_context" => "distinct fresh fork_turns=none, persuasion-blind",
    "same_family_role_separation_only" => true,
    "independence_claim_made" => false
  },
  "protected_surfaces" => {
    "canonical_manuscript_bibliography_pdf" => "UNCHANGED",
    "science_code_experiments_results" => "UNCHANGED",
    "registered_claims" => "UNCHANGED",
    "initial_system" => "UNCHANGED",
    "route_state" => "UNCHANGED"
  },
  "downstream_absence" => {
    "phase2b" => true,
    "traceability" => true,
    "official_checker_execution" => true,
    "decision" => true
  },
  "validation_checks" => checks.length,
  "checks" => checks
}
File.write(output_paths.fetch("boundary_validation"), JSON.pretty_generate(boundary) + "\n")

full_ids = semantic.fetch("item_results").select { |row| row.fetch("verdict") == "FULLY_ADDRESSED" }.map { |row| "`#{row.fetch('item_id')}`" }.join(", ")
partial_ids = semantic.fetch("item_results").select { |row| row.fetch("verdict") == "PARTIALLY_ADDRESSED" }.map { |row| "`#{row.fetch('item_id')}`" }.join(", ")
report = <<~MARKDOWN
  # P33 Round 10 Stage 3′ Round 4 Verification Review Report

  **Controlling outcome: `#{MARKER}`.** Phase 1 passed, but the first and immutable persuasion-blind Phase-2A verdict record failed the contract-1.1 JSON Schema. The no-retry rule therefore terminates this round before Response exposure, Phase 2B, traceability, the official checker, or any decision.

  - **Round ID:** `#{ROUND_ID}`
  - **Phase 1:** PASS — 13 precommitments (7 must-fix, 6 should-fix), #{phase1.dig('counts', 'validation_checks')} validation checks, no retry
  - **Phase 2A first emission:** semantic self-audit reported #{counts.fetch('FULLY_ADDRESSED')} fully addressed / #{counts.fetch('PARTIALLY_ADDRESSED')} partially addressed / #{counts.fetch('NOT_ADDRESSED')} not addressed / #{counts.fetch('MADE_WORSE')} made worse / #{counts.fetch('CANNOT_VERIFY')} cannot verify
  - **Controlling Phase 2A gate:** FAIL — #{errors.length} schema errors
  - **Phase 2A retry/edit/regeneration:** none; the invalid artifact remains preserved at raw SHA-256 `#{sha256(paths.fetch('verdict_record'))}`
  - **Phase 2B / Response exposure:** not started / not exposed
  - **Official checker:** NOT RUN (`checker_not_run_due_to_phase2a_abort`)
  - **Decision:** none; the 5/8 semantic counts are non-controlling and are not a Stage 3′ decision

  ## Exact lint failure

  | Error class | Count | Contract mismatch |
  |---|---:|---|
  | Top-level additional property | #{categories.fetch('top_level_additional_properties')} | `input_manifest_hash` is not allowed on a verdict-record/1.1 object |
  | Per-row additional properties | #{categories.fetch('row_additional_properties')} | `obligation_class`, and on partial rows the flat `residual_obligation_class`, are not allowed row properties |
  | Evidence-anchor shape | #{categories.fetch('evidence_anchor_not_array')} | Each row emitted one anchor object; the schema requires a nonempty array of typed-anchor strings |
  | Residual-gap shape | #{categories.fetch('residual_gap_not_object')} | Each partial row emitted a string plus a flat class; the schema requires one `{text, residual_obligation_class}` object |

  The semantic self-audit cannot override a structural contract failure. Editing these fields into the expected shapes would be a forbidden Phase-2A retry after evidence exposure.

  ## Non-controlling evidence signal

  The fresh evidence reader classified #{full_ids} as fully addressed and #{partial_ids} as genuine but incomplete. These labels are retained only as provenance of the failed first emission. They do not enter decision arithmetic, do not authorize revision work, and do not advance the pipeline.

  ## Freshness and preservation evidence

  Phase 1 ran in a new `fork_turns=none` revision-blind context. Phase 2A ran in a different `fork_turns=none` persuasion-blind context and did not inspect the Response, author-adjudication surface, or any earlier re-review artifact. This is same-family procedural role separation only; no independent-error, cross-model, cross-provider, or human-review claim is made.

  All #{freeze.dig('round3_preservation', 'file_count')} frozen Round-3 artifacts rehashed byte-for-byte, including the prior abort and invalid-attempt incident. The canonical manuscript, bibliography, PDF, code, experiments, results, registered claims, initial-system definition, Route-A state, and Route-B entry state also rehashed unchanged.

  #{DISCLOSURE}

  ## Next legal checkpoint

  Round 4 grants no authority to repair or re-emit Phase 2A. Continuing P33 requires a new explicit author authorization for a wholly fresh Stage 3′ round with a new round ID and new manifest, or a separately scoped hash-bound Stage 4′ authorization request. No Stage 4.5, Stage 5, Stage 6, canonical promotion, submission, scientific execution, result refresh, or Route change occurred.

  ## Controlling hashes

  | Artifact | Raw SHA-256 | JCS SHA-256 |
  |---|---|---|
  | Input manifest | `#{sha256(paths.fetch('input_manifest'))}` | `#{jcs_sha256(manifest)}` |
  | Precommitment | `#{sha256(paths.fetch('precommitment'))}` | `#{jcs_sha256(pre)}` |
  | Immutable invalid verdict | `#{sha256(paths.fetch('verdict_record'))}` | `#{jcs_sha256(verdict)}` |
  | Phase-2A lint failure | `#{sha256(output_paths.fetch('phase2a_validation'))}` | `#{jcs_sha256(phase2a_validation)}` |
  | Checker-not-run receipt | `#{sha256(output_paths.fetch('checker_receipt'))}` | `#{jcs_sha256(checker_receipt)}` |
  | Abort record | `#{sha256(output_paths.fetch('abort_record'))}` | `#{jcs_sha256(abort_record)}` |
  | Boundary validation | `#{sha256(output_paths.fetch('boundary_validation'))}` | `#{jcs_sha256(boundary)}` |
MARKDOWN
File.write(output_paths.fetch("verification_report"), report)

completion_artifacts = paths.merge(output_paths.reject { |name, _| name == "completion_receipt" }).map do |name, path|
  [name, binding(path, json: path.end_with?(".json"))]
end.to_h
completion = {
  "schema_version" => "p33-stage3-prime-round4-completion-receipt/1.0",
  "generated_at" => "2026-09-03T16:29:00Z",
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "status" => "ABORTED",
  "terminal_marker" => MARKER,
  "abort_reason" => "phase2a_lint_failed",
  "decision_emitted" => false,
  "official_checker_status" => "NOT_RUN",
  "phase2a_semantic_counts_noncontrolling" => counts,
  "phase2a_schema_error_count" => errors.length,
  "round3_files_rehashed" => freeze.dig("round3_preservation", "file_count"),
  "protected_surfaces_status" => "UNCHANGED",
  "same_family_role_separated" => true,
  "independence_claim_made" => false,
  "artifacts" => completion_artifacts,
  "next_stage_authorized" => false
}
File.write(output_paths.fetch("completion_receipt"), JSON.pretty_generate(completion) + "\n")

puts "PASS -- finalized P33 Round-4 fail-closed abort"
puts "terminal_marker=#{MARKER}"
puts "schema_errors=#{errors.length}; categories=#{categories}"
puts "boundary_checks=#{checks.length}; round3_rehashed=#{freeze.dig('round3_preservation', 'file_count')}"
puts "abort_record_sha256=#{sha256(output_paths.fetch('abort_record'))}"
puts "report_sha256=#{sha256(output_paths.fetch('verification_report'))}"
puts "completion_receipt_sha256=#{sha256(output_paths.fetch('completion_receipt'))}"
