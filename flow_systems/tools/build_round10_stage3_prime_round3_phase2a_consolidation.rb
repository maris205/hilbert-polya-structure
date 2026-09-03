#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
VALIDATION_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_VALIDATION.json")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_SEMANTIC_CONSOLIDATION.json")
GATE = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_GATE_RECEIPT.json")
TIEBREAK_PLAN = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_TIEBREAK_PRECOMMITMENT.md")
TIEBREAK = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_TIEBREAK_P33.json")
INVALID_ATTEMPT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_SEMANTIC_AUDIT_P33_INVALID_ATTEMPT1.json")
INVALID_INCIDENT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_SEMANTIC_AUDIT_P33_INVALID_ATTEMPT1_INCIDENT.md")
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze
VERDICTS = %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].freeze

def assert!(condition, message)
  raise "ROUND3_PHASE2A_CONSOLIDATION_FAIL_CLOSED: #{message}" unless condition
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def verdict_counts(rows, key)
  VERDICTS.to_h { |name| [name, rows.count { |row| row.fetch(key) == name }] }
end

validation = load_json(VALIDATION_PATH)
assert!(validation.dig("totals", "phase2a_validation") == "PASS", "structural validation")
assert!(validation.dig("totals", "papers") == 3 && validation.dig("totals", "verdict_rows") == 36, "structural totals")
validation_by_id = validation.fetch("papers").to_h { |paper| [paper.fetch("paper_id"), paper] }

audits = PAPERS.to_h do |paper_id, _slug|
  path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_SEMANTIC_AUDIT_#{paper_id}.json")
  [paper_id, {"path" => path, "value" => load_json(path)}]
end
tiebreak = load_json(TIEBREAK)
assert!(tiebreak.fetch("paper_id") == "P33" && tiebreak.fetch("item_id") == "REV-P33-011", "tie-break scope")
assert!(VERDICTS.include?(tiebreak.fetch("tie_break_verdict")), "tie-break verdict vocabulary")
assert!(tiebreak.fetch("status") == "COMMITTED", "tie-break not committed")
assert!(File.read(TIEBREAK_PLAN, encoding: "UTF-8").include?("Sole disputed row: `REV-P33-011`"), "tie-break plan scope")
assert!(sha256(INVALID_ATTEMPT) == "5610fc9d4ee43a2a6c45cd2105c97823c4d56684994b4a8bb0fb151a8b322ec9", "invalid-attempt preservation")
assert!(File.read(INVALID_INCIDENT, encoding: "UTF-8").include?("INVALID_BOUNDARY_TAINTED"), "invalid-attempt incident disposition")

paper_records = PAPERS.map do |paper_id, slug|
  notes = File.join(ROOT, "papers", slug, "notes")
  verdict_path = File.join(notes, "stage3_prime_round3_verdict_record.json")
  verdict = load_json(verdict_path)
  recorded_rows = verdict.fetch("items")
  audit_path = audits.fetch(paper_id).fetch("path")
  audit = audits.fetch(paper_id).fetch("value")
  phase2a_record = validation_by_id.fetch(paper_id)
  assert!(sha256(verdict_path) == phase2a_record.fetch("verdict_record_sha256"), "#{paper_id} verdict raw drift")
  assert!(audit.fetch("paper_id") == paper_id && audit.fetch("round_id") == verdict.fetch("round_id"), "#{paper_id} audit identity")
  audit_rows = audit.fetch("item_results")
  assert!(audit_rows.map { |row| row.fetch("item_id") } == recorded_rows.map { |row| row.fetch("item_id") }, "#{paper_id} audit order")
  audit_rows.zip(recorded_rows).each do |row, recorded|
    assert!(row.fetch("committed_verdict") == recorded.fetch("verdict"), "#{paper_id}/#{row.fetch('item_id')} committed binding")
    assert!(VERDICTS.include?(row.fetch("independently_supported_verdict")), "#{paper_id}/#{row.fetch('item_id')} supported vocabulary")
    assert!(row.fetch("agree") == (row.fetch("committed_verdict") == row.fetch("independently_supported_verdict")), "#{paper_id}/#{row.fetch('item_id')} agreement logic")
  end
  disputes = audit_rows.reject { |row| row.fetch("agree") }
  assert!(audit.fetch("disputed_item_ids") == disputes.map { |row| row.fetch("item_id") }, "#{paper_id} dispute list")
  if paper_id == "P33"
    assert!(disputes.map { |row| row.fetch("item_id") } == ["REV-P33-011"], "P33 closed dispute set")
  else
    assert!(disputes.empty? && audit.fetch("status") == "PASS", "#{paper_id} semantic audit did not pass")
  end
  if paper_id == "P29"
    assert!(Array(audit["disputed_new_issue_ids"]).empty?, "P29 new-issue dispute")
  end

  controlling_rows = recorded_rows.map do |row|
    value = if paper_id == "P33" && row.fetch("item_id") == "REV-P33-011"
              tiebreak.fetch("tie_break_verdict")
            else
              row.fetch("verdict")
            end
    {"item_id" => row.fetch("item_id"), "verdict" => value}
  end
  record_differences = controlling_rows.zip(recorded_rows).filter_map do |control, recorded|
    next if control.fetch("verdict") == recorded.fetch("verdict")
    {"item_id" => control.fetch("item_id"), "recorded_verdict" => recorded.fetch("verdict"), "controlling_verdict" => control.fetch("verdict")}
  end
  controlling_status = record_differences.empty? ? "PHASE2A_PASS" : "ABORTED"
  {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "round_id" => verdict.fetch("round_id"),
    "verdict_record_sha256" => sha256(verdict_path),
    "semantic_audit_path" => audit_path.delete_prefix("#{ROOT}/"),
    "semantic_audit_sha256" => sha256(audit_path),
    "recorded_counts" => verdict_counts(recorded_rows, "verdict"),
    "controlling_counts" => verdict_counts(controlling_rows, "verdict"),
    "primary_audit_disputed_rows" => disputes.length,
    "controlling_record_discrepancies" => record_differences,
    "controlling_status" => controlling_status,
    "abort_reason" => ("phase2a_lint_failed" if controlling_status == "ABORTED"),
    "phase2b_eligible" => controlling_status == "PHASE2A_PASS",
    "phase2a_retry_used" => false,
    "decision_emitted" => false
  }.compact
end

recorded_total = VERDICTS.to_h { |name| [name, paper_records.sum { |paper| paper.fetch("recorded_counts").fetch(name) }] }
controlling_total = VERDICTS.to_h { |name| [name, paper_records.sum { |paper| paper.fetch("controlling_counts").fetch(name) }] }
phase2b_scope = paper_records.select { |paper| paper.fetch("phase2b_eligible") }.map { |paper| paper.fetch("paper_id") }
aborted = paper_records.reject { |paper| paper.fetch("phase2b_eligible") }.map { |paper| paper.fetch("paper_id") }
dispute_row = audits.fetch("P33").fetch("value").fetch("item_results").find { |row| row.fetch("item_id") == "REV-P33-011" }

payload = {
  "schema_version" => "round10-stage3-prime-round3-phase2a-semantic-consolidation/1.0",
  "created_at_utc" => "2026-09-03T14:55:00Z",
  "protocol" => "ARS re-review contract 1.1 / evidence-before-persuasion / no-retry Phase 2A",
  "source_artifacts" => ([VALIDATION_PATH, *audits.values.map { |entry| entry.fetch("path") }, TIEBREAK_PLAN, TIEBREAK, INVALID_ATTEMPT, INVALID_INCIDENT].map do |path|
    {"path" => path.delete_prefix("#{ROOT}/"), "sha256" => sha256(path)}
  end),
  "invalid_attempts" => [{
    "paper_id" => "P33",
    "path" => INVALID_ATTEMPT.delete_prefix("#{ROOT}/"),
    "sha256" => sha256(INVALID_ATTEMPT),
    "disposition" => "INVALID_BOUNDARY_TAINTED",
    "used_for_gate" => false,
    "replacement_audit_sha256" => sha256(audits.fetch("P33").fetch("path"))
  }],
  "method" => {
    "primary_audit" => "One valid fresh-context full-row semantic audit per paper against immutable criteria; the tainted P33 attempt is excluded.",
    "tie_break" => "One result-blind, hash-bound fresh-context tie-break controls only P33 REV-P33-011.",
    "abort_rule" => "A tie-break verdict differing from the committed Phase-2A verdict aborts that paper as phase2a_lint_failed; the verdict record is not edited and Phase 2B is forbidden.",
    "non_disputed_rows" => "The immutable committed record remains controlling."
  },
  "provenance" => {"fresh_context_role_separation" => true, "human_distinct" => false, "model_family_distinct" => false, "provider_distinct" => false, "independent_error_process_claimed" => false},
  "disputed_rows" => [{
    "paper_id" => "P33",
    "item_id" => "REV-P33-011",
    "recorded_verdict" => dispute_row.fetch("committed_verdict"),
    "primary_audit_supported_verdict" => dispute_row.fetch("independently_supported_verdict"),
    "blind_tie_break_verdict" => tiebreak.fetch("tie_break_verdict"),
    "tie_break_matches_committed_record" => tiebreak.fetch("tie_break_verdict") == dispute_row.fetch("committed_verdict"),
    "controlling_verdict" => tiebreak.fetch("tie_break_verdict"),
    "reason" => tiebreak.fetch("rationale")
  }],
  "papers" => paper_records,
  "totals" => {
    "papers" => 3,
    "phase2a_pass" => phase2b_scope.length,
    "phase2a_aborted" => aborted.length,
    "recorded" => recorded_total,
    "controlling" => controlling_total,
    "primary_audit_disputed_rows" => 1,
    "blind_tie_break_matches" => aborted.empty? ? 1 : 0,
    "blind_tie_break_record_discrepancies" => aborted.length
  },
  "phase2b_scope" => phase2b_scope,
  "aborted_before_phase2b" => aborted,
  "boundary" => {"phase2a_records_rewritten" => false, "response_to_reviewers_seen_during_phase2a_or_tie_break" => false, "canonical_manuscripts_modified" => false, "science_artifacts_modified" => false, "route_credit_changed" => false, "route_b_invoked" => false}
}
File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")

status = aborted.empty? ? "PASS" : "PASS_WITH_#{aborted.length}_FAIL_CLOSED_ABORT"
gate = {
  "schema_version" => "round10-stage3-prime-round3-phase2a-gate-receipt/1.0",
  "generated_at_utc" => "2026-09-03T14:55:00Z",
  "consolidation_path" => File.basename(OUTPUT),
  "consolidation_sha256" => sha256(OUTPUT),
  "structural_validation_path" => File.basename(VALIDATION_PATH),
  "structural_validation_sha256" => sha256(VALIDATION_PATH),
  "structural_checks" => validation.dig("totals", "validation_checks"),
  "phase2a_rows" => validation.dig("totals", "verdict_rows"),
  "phase2a_pass_papers" => phase2b_scope,
  "phase2a_aborted_papers" => aborted,
  "aborted_reason" => ("phase2a_lint_failed" unless aborted.empty?),
  "phase2b_authorized_scope" => phase2b_scope,
  "phase2a_retry_used" => false,
  "invalid_primary_audit_replacements" => 1,
  "status" => status
}.compact
File.write(GATE, JSON.pretty_generate(gate) + "\n")
puts "PASS — Phase 2A consolidated: #{phase2b_scope.length} pass, #{aborted.length} fail-closed abort; 36 rows"
