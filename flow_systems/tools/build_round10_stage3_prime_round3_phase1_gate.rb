#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_GATE_RECEIPT.json")
VALIDATION = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_VALIDATION.json")
AUDITS = {
  "P29-initial" => "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_SEMANTIC_AUDIT_P29.json",
  "P29-retry1" => "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_SEMANTIC_AUDIT_P29_RETRY1.json",
  "P32" => "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_SEMANTIC_AUDIT_P32.json",
  "P33" => "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_SEMANTIC_AUDIT_P33.json"
}.freeze

def assert!(condition, message)
  raise message unless condition
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def audit_status(audit)
  audit["closed_status"] || audit["status"] || audit.dig("final", "status") || audit["overall_status"]
end

def row_status(row)
  return row["status"] if row["status"]
  return row["result"] if row["result"].is_a?(String)
  return row["result"]["status"] if row["result"].is_a?(Hash)
  return row["final"] if row["final"].is_a?(String)
  return row["final"]["status"] if row["final"].is_a?(Hash)

  nil
end

validation = load_json(VALIDATION)
audits = AUDITS.transform_values { |name| load_json(File.join(ROOT, name)) }
assert!(validation.dig("totals", "papers") == 3, "paper count")
assert!(validation.dig("totals", "precommitted_items") == 36, "row count")
assert!(validation.dig("totals", "validation_checks") == 423, "structural check count")
assert!(validation.dig("totals", "phase1_validation") == "PASS", "structural validation")
assert!(audit_status(audits.fetch("P29-initial")) == "FAIL", "P29 initial audit must retain failure")
assert!(audits.fetch("P29-initial").fetch("item_results").count { |row| row_status(row) == "FAIL" } == 1, "P29 initial defect count")

{"P29-retry1" => 11, "P32" => 12, "P33" => 13}.each do |label, expected|
  audit = audits.fetch(label)
  rows = audit.fetch("item_results")
  assert!(audit_status(audit) == "PASS", "#{label} audit status")
  assert!(rows.length == expected, "#{label} audit row count")
  assert!(rows.all? { |row| row_status(row) == "PASS" }, "#{label} semantic row failure")
end

papers = validation.fetch("papers").map do |paper|
  receipt_path = File.join(ROOT, "papers", paper.fetch("paper_slug"), "notes", "stage3_prime_round3_phase1_receipt.md")
  receipt = File.read(receipt_path, encoding: "UTF-8")
  retry_used = paper.fetch("paper_id") == "P29"
  if retry_used
    assert!(receipt.match?(/retry/i) && receipt.match?(/1\s*\/\s*1|1\s+of\s+1/i), "P29 retry marker missing")
  end
  {
    "paper_id" => paper.fetch("paper_id"),
    "round_id" => paper.fetch("round_id"),
    "precommitment_sha256" => paper.fetch("precommitment_sha256"),
    "precommitment_jcs_sha256" => paper.fetch("precommitment_jcs_sha256"),
    "phase1_receipt_sha256" => paper.fetch("phase1_receipt_sha256"),
    "rows" => paper.fetch("roadmap_items_precommitted"),
    "lint_retry_used" => retry_used,
    "lint_retry_count" => retry_used ? 1 : 0,
    "terminal_marker" => "[CONTRACT-ACKNOWLEDGED]",
    "structural_status" => "PASS",
    "semantic_status" => "PASS"
  }
end

payload = {
  "schema_version" => "round10-stage3-prime-round3-phase1-gate/1.0",
  "closed_at" => "2026-09-03T13:45:00Z",
  "status" => "PASS",
  "gate" => "phase1_revision_blind_precommitment",
  "contract_version" => "1.1",
  "papers" => papers,
  "totals" => {"papers" => 3, "rows" => 36, "structural_checks" => 423, "semantic_rows_passed" => 36, "semantic_defects_after_retry" => 0, "pre_evidence_lint_retries" => 1},
  "bindings" => {
    "structural_validation" => {"path" => File.basename(VALIDATION), "sha256" => sha(VALIDATION)},
    "semantic_audits" => AUDITS.map { |label, name| {"label" => label, "path" => name, "sha256" => sha(File.join(ROOT, name))} }
  },
  "provenance" => {"fresh_context" => true, "revision_blind" => true, "same_model_family" => true, "human_distinct" => false, "provider_distinct" => false, "independent_error_process_claimed" => false},
  "boundary" => {"revision_evidence_seen_during_phase1" => false, "response_letter_seen_during_phase1" => false, "author_sidecar_used_as_criterion" => false, "phase1_artifacts_now_immutable" => true, "phase2a_may_start" => true}
}
File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS -- Phase 1 gate closed after one permitted blind retry: 36/36 rows"
