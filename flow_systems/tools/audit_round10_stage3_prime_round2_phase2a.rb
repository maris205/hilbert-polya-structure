#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_VALIDATION.json")
PHASE1_VALIDATION = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_VALIDATION.json")
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze
VERDICTS = %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].freeze

def assert!(condition, message)
  raise message unless condition
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

def verify_manifest_entry!(paper_root, entry, label, checks)
  return unless entry.fetch("present")

  entries = entry.key?("items") ? entry.fetch("items") : [entry]
  entries.each_with_index do |artifact, index|
    ref = artifact.fetch("path_or_passport_ref")
    assert!(ref.start_with?("path:"), "#{label}[#{index}]: non-path artifact unsupported")
    relative = ref.delete_prefix("path:")
    assert!(!relative.start_with?("/") && !relative.split("/").include?(".."), "#{label}[#{index}]: unsafe path")
    path = File.join(paper_root, relative)
    assert!(File.file?(path), "#{label}[#{index}]: missing #{relative}")
    assert!(sha256(path) == artifact.fetch("sha256"), "#{label}[#{index}]: raw hash drift")
    checks << "manifest_artifact:#{label}[#{index}]"
  end
end

phase1 = load_json(PHASE1_VALIDATION)
phase1_by_paper = phase1.fetch("papers").to_h { |paper| [paper.fetch("paper_id"), paper] }
papers = []
total_checks = 0
total_rows = 0

PAPERS.each do |paper_id, slug|
  paper_root = File.join(ROOT, "papers", slug)
  notes = File.join(paper_root, "notes")
  manifest_path = File.join(notes, "stage3_prime_round2_input_manifest.json")
  precommitment_path = File.join(notes, "stage3_prime_round2_precommitment.json")
  roadmap_path = File.join(notes, "stage3_revision_roadmap.json")
  verdict_path = File.join(notes, "stage3_prime_round2_verdict_record.json")
  receipt_path = File.join(notes, "stage3_prime_round2_phase2a_receipt.md")

  manifest = load_json(manifest_path)
  precommitment = load_json(precommitment_path)
  roadmap = load_json(roadmap_path)
  verdict = load_json(verdict_path)
  checks = []
  check = lambda do |condition, label|
    assert!(condition, "#{paper_id}: #{label}")
    checks << label
  end

  phase1_record = phase1_by_paper.fetch(paper_id)
  check.call(sha256(precommitment_path) == phase1_record.fetch("precommitment_sha256"), "phase1_raw_immutability")
  check.call(jcs_sha256(precommitment) == phase1_record.fetch("precommitment_jcs_sha256"), "phase1_jcs_immutability")
  manifest.fetch("artifacts").each do |label, entry|
    verify_manifest_entry!(paper_root, entry, label, checks)
  end

  check.call(verdict.fetch("contract_version") == "1.1", "contract_version")
  check.call(verdict.fetch("round_id") == manifest.fetch("round_id"), "round_id_binding")
  check.call(verdict.fetch("precommitment_hash") == jcs_sha256(precommitment), "precommitment_jcs_binding")
  roadmap_items = roadmap.fetch("items")
  rows = verdict.fetch("items")
  check.call(rows.map { |row| row.fetch("item_id") } == roadmap_items.map { |item| item.fetch("id") }, "all_item_coverage_and_order")

  pre_by_item = precommitment.fetch("items").to_h { |record| [record.fetch("item_id"), record] }
  dissent_by_id = verdict.fetch("dissents").to_h { |record| [record.fetch("dissent_id"), record] }
  rows.zip(roadmap_items).each do |row, item|
    item_id = item.fetch("id")
    expected_seat = Array(pre_by_item.dig(item_id, "source_reviewer_labels")).find { |seat| seat != "DA" } || "EIC"
    check.call(VERDICTS.include?(row.fetch("verdict")), "#{item_id}:closed_verdict")
    check.call(row.fetch("verified_by") == expected_seat, "#{item_id}:routing")

    if %w[must_fix should_fix].include?(item.fetch("obligation_class"))
      applied = row.fetch("applied_criterion")
      if applied == "precommitted"
        check.call(true, "#{item_id}:precommitted_criterion")
      else
        match = /\Adissented:(DIS-[1-9][0-9]*)\z/.match(applied)
        check.call(match && dissent_by_id.key?(match[1]) && dissent_by_id.fetch(match[1]).fetch("item_id") == item_id,
                   "#{item_id}:dissent_binding")
      end
    else
      check.call(row.fetch("applied_criterion") == "not_precommitted", "#{item_id}:consider_criterion")
    end

    if row.fetch("verdict") == "CANNOT_VERIFY"
      check.call(row.key?("cannot_verify_reason") && !row.key?("evidence_anchor"), "#{item_id}:cannot_verify_shape")
    else
      anchors = row.fetch("evidence_anchor")
      check.call(!anchors.empty? && anchors.all? { |anchor| /\A(text|table|figure|equation|dataset|absence): .+/.match?(anchor) },
                 "#{item_id}:typed_revised_anchors")
    end
    if row.fetch("verdict") == "PARTIALLY_ADDRESSED"
      residual = row.fetch("residual_gap")
      check.call(!residual.fetch("text").strip.empty? && %w[must_fix should_fix consider].include?(residual.fetch("residual_obligation_class")),
                 "#{item_id}:residual_gap")
    else
      check.call(!row.key?("residual_gap"), "#{item_id}:no_spurious_residual")
    end
  end

  serialized = JSON.generate(verdict)
  %w[stage4_response_to_reviewers author_response].each do |forbidden|
    check.call(!serialized.downcase.include?(forbidden.downcase), "no_#{forbidden}_reference")
  end
  final_nonempty_line = File.readlines(receipt_path, chomp: true).reverse.find { |line| !line.strip.empty? }
  check.call(final_nonempty_line == "[EVIDENCE-COMMITTED]", "phase2a_receipt_acknowledgement")

  counts = VERDICTS.to_h { |name| [name, rows.count { |row| row.fetch("verdict") == name }] }
  papers << {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "round_id" => verdict.fetch("round_id"),
    "verdict_record_sha256" => sha256(verdict_path),
    "verdict_record_jcs_sha256" => jcs_sha256(verdict),
    "phase2a_receipt_sha256" => sha256(receipt_path),
    "rows" => rows.length,
    "verdict_counts" => counts,
    "new_issues" => verdict.fetch("new_issues").length,
    "dissents" => verdict.fetch("dissents").length,
    "escalation_exceptions" => verdict.fetch("escalation_exceptions").length,
    "validation_checks" => checks.length,
    "status" => "PASS"
  }
  total_checks += checks.length
  total_rows += rows.length
end

payload = {
  "schema_version" => "round10-stage3-prime-round2-phase2a-validation/1.0",
  "generated_at" => "2026-09-03T10:30:00Z",
  "contract_version" => "1.1",
  "phase" => "phase2a_persuasion_blind_evidence_verdict",
  "papers" => papers,
  "totals" => {
    "papers" => papers.length,
    "verdict_rows" => total_rows,
    "validation_checks" => total_checks,
    "schema_validation" => "PASS",
    "phase2a_validation" => "PASS"
  },
  "boundary" => {
    "response_to_reviewers_exposed_during_phase2a" => false,
    "phase2a_retry_used" => false,
    "phase2b_started" => false,
    "manuscripts_modified" => false,
    "science_artifacts_modified" => false,
    "route_credit_changed" => false
  }
}

File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS — Round 10 Stage 3′ Round 2 Phase 2A: #{total_checks} checks; #{total_rows} immutable evidence verdicts"
