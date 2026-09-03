#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_GATE_RECEIPT.json")
VALIDATION_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_VALIDATION.json")
AUDIT_A_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_SEMANTIC_AUDIT_P29_P31.json")
AUDIT_B_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_SEMANTIC_AUDIT_P32_P33.json")
BOUNDARY_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_BOUNDARY_VALIDATION.json")

def assert!(condition, message)
  raise message unless condition
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

validation = load_json(VALIDATION_PATH)
audit_a = load_json(AUDIT_A_PATH)
audit_b = load_json(AUDIT_B_PATH)
boundary = load_json(BOUNDARY_PATH)

assert!(validation.dig("totals", "papers") == 5, "phase1 paper count")
assert!(validation.dig("totals", "precommitted_items") == 56, "phase1 row count")
assert!(validation.dig("totals", "validation_checks") == 679, "phase1 structural checks")
assert!(validation.dig("totals", "phase1_validation") == "PASS", "phase1 validation")
assert!(audit_a.dig("aggregate", "row_count") == 31, "audit A row count")
assert!(audit_a.dig("aggregate", "pass_count") == 31, "audit A pass count")
assert!(audit_a.dig("aggregate", "defect_count") == 0, "audit A defects")
assert!(audit_a.dig("aggregate", "overall_status") == "PASS_WITH_REPORTED_NONROW_ADVISORIES", "audit A status")
assert!(audit_b.dig("aggregate_counts", "rows_total") == 25, "audit B row count")
assert!(audit_b.dig("aggregate_counts", "pass_rows") == 25, "audit B pass count")
assert!(audit_b.dig("aggregate_counts", "defect_rows") == 0, "audit B defects")
assert!(audit_b.fetch("overall_status") == "PASS", "audit B status")
assert!(boundary.fetch("status") == "PASS", "frozen boundaries")

papers = validation.fetch("papers").map do |paper|
  receipt_path = File.join(ROOT, "papers", paper.fetch("paper_slug"), "notes", "stage3_prime_round2_phase1_receipt.md")
  receipt = File.read(receipt_path, encoding: "UTF-8")
  retries = receipt.scan(/retry[^\n]*1(?: of 1|\/1)/i).length
  {
    "paper_id" => paper.fetch("paper_id"),
    "round_id" => paper.fetch("round_id"),
    "precommitment_sha256" => paper.fetch("precommitment_sha256"),
    "precommitment_jcs_sha256" => paper.fetch("precommitment_jcs_sha256"),
    "phase1_receipt_sha256" => paper.fetch("phase1_receipt_sha256"),
    "rows" => paper.fetch("roadmap_items_precommitted"),
    "lint_retry_used" => retries.positive?,
    "terminal_marker" => "[CONTRACT-ACKNOWLEDGED]",
    "structural_status" => "PASS",
    "semantic_status" => "PASS"
  }
end

payload = {
  "schema_version" => "round10-stage3-prime-round2-phase1-gate/1.0",
  "closed_at" => "2026-09-03T09:55:00Z",
  "status" => "PASS",
  "gate" => "phase1_revision_blind_precommitment",
  "contract_version" => "1.1",
  "papers" => papers,
  "totals" => {
    "papers" => 5,
    "rows" => 56,
    "structural_checks" => 679,
    "semantic_rows_passed" => 56,
    "semantic_defects" => 0,
    "pre_evidence_lint_retries" => papers.count { |paper| paper.fetch("lint_retry_used") }
  },
  "bindings" => {
    "structural_validation" => {"path" => File.basename(VALIDATION_PATH), "sha256" => sha256(VALIDATION_PATH)},
    "semantic_audit_p29_p31" => {"path" => File.basename(AUDIT_A_PATH), "sha256" => sha256(AUDIT_A_PATH)},
    "semantic_audit_p32_p33" => {"path" => File.basename(AUDIT_B_PATH), "sha256" => sha256(AUDIT_B_PATH)},
    "frozen_boundary_validation" => {"path" => File.basename(BOUNDARY_PATH), "sha256" => sha256(BOUNDARY_PATH)}
  },
  "provenance" => {
    "fresh_context" => true,
    "revision_blind" => true,
    "same_model_family" => true,
    "human_distinct" => false,
    "provider_distinct" => false,
    "independent_error_process_claimed" => false
  },
  "letter_layer" => {
    "P29" => "absent_strict_blocks_with_advisory",
    "P30" => "absent_strict_blocks_with_advisory",
    "P31" => "present_contiguous_R1_R11",
    "P32" => "absent_noncanonical_template_with_advisory",
    "P33" => "absent_strict_blocks_with_advisory"
  },
  "boundary" => {
    "revision_evidence_seen_during_phase1" => false,
    "response_letter_seen_during_phase1" => false,
    "author_sidecar_used_as_criterion" => false,
    "phase1_artifacts_now_immutable" => true,
    "phase2a_may_start_under_existing_round2_authorization" => true
  }
}

File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS — Phase 1 gate closed: 56/56 semantic rows, 679 structural checks"
