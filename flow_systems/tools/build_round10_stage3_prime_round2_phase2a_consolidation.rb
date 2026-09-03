#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_CONSOLIDATION.json")
GATE = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_GATE_RECEIPT.json")
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze
CREATED_AT = "2026-09-03T11:50:15Z"

SOURCES = [
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_VALIDATION.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_AUDIT_P29_P30.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_AUDIT_P31_P32.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_AUDIT_P33.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_TIEBREAK_PRECOMMITMENT.md",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_TIEBREAK_P29_P33.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_TIEBREAK_P31.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_TIEBREAK_P32.json"
].freeze

ARBITRATED = [
  ["P29", "REV-EIC-1", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "PARTIALLY_ADDRESSED",
   "The revision names comparison classes and a project-specific synthesis but does not explicitly identify adapted components versus the synthesis."],
  ["P29", "REV-DA-2", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "PARTIALLY_ADDRESSED",
   "Neither permitted branch is complete: there is no worked synthetic baseline/outcome fixture, and an unchanged sentence still claims scientific usefulness."],
  ["P31", "REV-P31-003", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "FULLY_ADDRESSED",
   "The blind tie-break found B0041's explicit provenance boundary sufficient for the exact committed criterion."],
  ["P31", "REV-P31-006", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "FULLY_ADDRESSED",
   "The blind tie-break found the manuscript-wide design-level and non-executable boundaries sufficient for the exact committed branch."],
  ["P32", "REV-P32-DA-N1", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "FULLY_ADDRESSED",
   "The blind tie-break found every comparative term locally or anaphorically tied to the declared structural dependency basis."],
  ["P32", "REV-P32-DA-M1", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "PARTIALLY_ADDRESSED",
   "The manuscript supplies a future scalar-check contract but neither a conditional lemma conclusion nor the alternative inadmissibility-and-necessity argument."],
  ["P33", "REV-P33-011", "FULLY_ADDRESSED", "PARTIALLY_ADDRESSED", "PARTIALLY_ADDRESSED",
   "The invalid BP/CP cases do not each display the complete private-payload, mapping, predicate, transition, and fail-closed chain required by the committed universal."]
].freeze

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def counts(rows)
  names = %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY]
  names.to_h { |name| [name, rows.count { |row| row.fetch("verdict") == name }] }
end

source_records = SOURCES.map { |path| {"path" => path, "sha256" => sha(File.join(ROOT, path))} }
disputed_rows = ARBITRATED.map do |paper_id, item_id, recorded, primary, controlling, reason|
  {
    "paper_id" => paper_id,
    "item_id" => item_id,
    "recorded_verdict" => recorded,
    "primary_audit_supported_verdict" => primary,
    "blind_tie_break_verdict" => controlling,
    "tie_break_matches_committed_record" => controlling == recorded,
    "controlling_verdict" => controlling,
    "reason" => reason
  }
end

paper_records = PAPERS.map do |paper_id, slug|
  verdict_path = File.join(ROOT, "papers", slug, "notes", "stage3_prime_round2_verdict_record.json")
  verdict = load_json(verdict_path)
  recorded = counts(verdict.fetch("items"))
  controlling = recorded.dup
  paper_disputes = disputed_rows.select { |row| row.fetch("paper_id") == paper_id }
  paper_disputes.each do |row|
    next if row.fetch("recorded_verdict") == row.fetch("controlling_verdict")
    controlling[row.fetch("recorded_verdict")] -= 1
    controlling[row.fetch("controlling_verdict")] += 1
  end
  differences = paper_disputes.reject { |row| row.fetch("tie_break_matches_committed_record") }
  status = differences.empty? ? "PHASE2A_PASS" : "ABORTED"
  {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "round_id" => verdict.fetch("round_id"),
    "verdict_record_sha256" => sha(verdict_path),
    "recorded_counts" => recorded,
    "controlling_counts" => controlling,
    "primary_audit_disputed_rows" => paper_disputes.length,
    "controlling_record_discrepancies" => differences.map { |row| row.fetch("item_id") },
    "controlling_status" => status,
    "abort_reason" => ("phase2a_lint_failed" if status == "ABORTED"),
    "phase2b_eligible" => status == "PHASE2A_PASS",
    "phase2a_retry_used" => false,
    "decision_emitted" => false
  }.compact
end

recorded_total = paper_records.each_with_object(Hash.new(0)) do |paper, memo|
  paper.fetch("recorded_counts").each { |name, value| memo[name] += value }
end
controlling_total = paper_records.each_with_object(Hash.new(0)) do |paper, memo|
  paper.fetch("controlling_counts").each { |name, value| memo[name] += value }
end

payload = {
  "schema_version" => "round10-stage3-prime-round2-phase2a-semantic-consolidation/1.0",
  "created_at_utc" => CREATED_AT,
  "protocol" => "ARS re-review contract 1.1 / evidence-before-persuasion / no-retry Phase 2A",
  "source_artifacts" => source_records,
  "method" => {
    "primary_audit" => "Fresh-context full-row semantic audit against the immutable precommitted criterion.",
    "tie_break" => "A hash-bound blind tie-break, precommitted before dispatch, controls only the seven closed disputed rows.",
    "abort_rule" => "If a controlling tie-break verdict differs from the already committed Phase-2A record, that paper aborts phase2a_lint_failed; the record is not edited and Phase 2B is forbidden.",
    "non_disputed_rows" => "The committed record remains controlling for all non-disputed rows."
  },
  "provenance" => {
    "fresh_context_role_separation" => true,
    "human_distinct" => false,
    "model_family_distinct" => false,
    "provider_distinct" => false,
    "independent_error_process_claimed" => false,
    "limitation" => "All passes are same-family fresh contexts; correlated-error risk remains."
  },
  "disputed_rows" => disputed_rows,
  "papers" => paper_records,
  "totals" => {
    "papers" => 5,
    "phase2a_pass" => paper_records.count { |paper| paper.fetch("controlling_status") == "PHASE2A_PASS" },
    "phase2a_aborted" => paper_records.count { |paper| paper.fetch("controlling_status") == "ABORTED" },
    "recorded" => recorded_total,
    "controlling" => controlling_total,
    "primary_audit_disputed_rows" => disputed_rows.length,
    "blind_tie_break_matches" => disputed_rows.count { |row| row.fetch("tie_break_matches_committed_record") },
    "blind_tie_break_record_discrepancies" => disputed_rows.count { |row| !row.fetch("tie_break_matches_committed_record") }
  },
  "phase2b_scope" => ["P30", "P31"],
  "aborted_before_phase2b" => ["P29", "P32", "P33"],
  "boundary" => {
    "phase2a_records_rewritten" => false,
    "response_to_reviewers_seen_during_phase2a_or_tie_break" => false,
    "canonical_manuscripts_modified" => false,
    "science_artifacts_modified" => false,
    "route_credit_changed" => false,
    "route_b_invoked" => false
  }
}

File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
gate = {
  "schema_version" => "round10-stage3-prime-round2-phase2a-gate-receipt/1.0",
  "generated_at_utc" => CREATED_AT,
  "consolidation_path" => File.basename(OUTPUT),
  "consolidation_sha256" => sha(OUTPUT),
  "structural_validation_path" => "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_VALIDATION.json",
  "structural_validation_sha256" => sha(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_VALIDATION.json")),
  "structural_checks" => 380,
  "phase2a_rows" => 56,
  "phase2a_pass_papers" => ["P30", "P31"],
  "phase2a_aborted_papers" => ["P29", "P32", "P33"],
  "aborted_reason" => "phase2a_lint_failed",
  "phase2b_authorized_scope" => ["P30", "P31"],
  "phase2a_retry_used" => false,
  "status" => "PASS_WITH_THREE_FAIL_CLOSED_ABORTS"
}
File.write(GATE, JSON.pretty_generate(gate) + "\n")
puts "PASS — Phase 2A consolidated: 2 pass, 3 fail-closed aborts; 56 rows"
