#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "optparse"

ROOT = File.expand_path("..", __dir__)
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze
VERDICTS = %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].freeze
PRIORITIES = %w[must_fix should_fix consider].freeze
RESIDUALS = %w[must_fix should_fix consider].freeze
VERIFIED_MAP = {
  "FULLY_ADDRESSED" => "YES",
  "PARTIALLY_ADDRESSED" => "PARTIAL",
  "NOT_ADDRESSED" => "NO",
  "MADE_WORSE" => "NO",
  "CANNOT_VERIFY" => "CANNOT_VERIFY"
}.freeze

options = { candidate_dir: nil }
OptionParser.new do |parser|
  parser.on("--candidate-dir DIR", "Write flat candidate files under DIR instead of final note paths") do |dir|
    options[:candidate_dir] = File.expand_path(dir)
  end
end.parse!

def assert!(condition, message)
  raise message unless condition
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
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

def derive_decision(rows, roadmap_by_id, residual_by_item, new_issues, escalations)
  must = rows.select { |row| roadmap_by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == "must_fix" }
  should = rows.select { |row| roadmap_by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == "should_fix" }
  critical_made_worse = must.any? do |row|
    row.fetch("final_verdict") == "MADE_WORSE" && roadmap_by_id.fetch(row.fetch("item_id"))["severity"] == "critical"
  end
  critical_regression = new_issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "critical" }
  negative_count = must.count { |row| %w[NOT_ADDRESSED MADE_WORSE].include?(row.fetch("final_verdict")) }
  half_negative = !must.empty? && negative_count * 2 >= must.length
  must_negative = must.any? { |row| %w[NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].include?(row.fetch("final_verdict")) }
  major_regression = new_issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "major" }
  must_residual = rows.any? do |row|
    row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && residual_by_item[row.fetch("item_id")] == "must_fix"
  end
  should_numerator = should.count { |row| %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED].include?(row.fetch("final_verdict")) }
  under_eighty = !should.empty? && should_numerator * 5 < should.length * 4
  lower_residual = must.any? do |row|
    row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && %w[should_fix consider].include?(residual_by_item[row.fetch("item_id")])
  end
  should_worse = should.any? { |row| row.fetch("final_verdict") == "MADE_WORSE" }
  minor_regression = new_issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "minor" }

  if critical_made_worse || critical_regression
    decision = "Major Revision"
    reject = true
    rule = "B1"
  elsif half_negative
    decision = "Major Revision"
    reject = true
    rule = "B2"
  elsif must_negative || major_regression
    decision = "Major Revision"
    reject = false
    rule = "B3"
  elsif must_residual
    decision = "Major Revision"
    reject = false
    rule = "B4"
  elsif lower_residual || under_eighty || should_worse || minor_regression
    decision = "Minor Revision"
    reject = false
    rule = "B5"
  else
    decision = "Accept"
    reject = false
    rule = "B6"
  end

  order = {"Accept" => 0, "Minor Revision" => 1, "Major Revision" => 2}
  escalations.select { |entry| entry.fetch("effective_approval_state") == "approved" }.each do |entry|
    floor = entry.fetch("mechanical_decision_impact")
    decision = floor if order.fetch(floor) > order.fetch(decision)
  end
  [decision, reject, rule]
end

FileUtils.mkdir_p(options[:candidate_dir]) if options[:candidate_dir]
summary = []

PAPERS.each do |paper_id, slug|
  notes = File.join(ROOT, "papers", slug, "notes")
  roadmap = load_json(File.join(notes, "stage3_revision_roadmap.json"))
  author = load_json(File.join(notes, "stage4_author_adjudication.json"))
  verdict = load_json(File.join(notes, "stage3_prime_round1_verdict_record.json"))
  integration = load_json(File.join(notes, "stage3_prime_round1_phase2b_integration.json"))
  roadmap_items = roadmap.fetch("items")
  roadmap_by_id = roadmap_items.to_h { |item| [item.fetch("id"), item] }
  author_by_id = author.fetch("author_adjudications").to_h { |record| [record.fetch("item_id"), record] }
  verdict_by_id = verdict.fetch("items").to_h { |record| [record.fetch("item_id"), record] }
  integration_by_id = integration.fetch("rows").to_h { |record| [record.fetch("item_id"), record] }

  ids = roadmap_items.map { |item| item.fetch("id") }
  assert!(ids == author.fetch("author_adjudications").map { |record| record.fetch("item_id") }, "#{paper_id}: author order")
  assert!(ids == verdict.fetch("items").map { |record| record.fetch("item_id") }, "#{paper_id}: verdict order")
  assert!(ids == integration.fetch("rows").map { |record| record.fetch("item_id") }, "#{paper_id}: integration order")
  assert!(integration.fetch("verdict_record_hash") == jcs_sha256(verdict), "#{paper_id}: verdict hash")
  assert!(integration.fetch("adjustments").empty?, "#{paper_id}: builder currently requires zero adjustments")
  assert!(verdict.fetch("dissents").empty?, "#{paper_id}: builder currently requires zero dissents")
  assert!(verdict.fetch("escalation_exceptions").empty?, "#{paper_id}: builder currently requires zero escalation exceptions")

  rows = roadmap_items.map do |item|
    item_id = item.fetch("id")
    phase2a = verdict_by_id.fetch(item_id)
    phase2b = integration_by_id.fetch(item_id)
    author_record = author_by_id.fetch(item_id)
    assert!(phase2b.fetch("phase2a_verdict") == phase2a.fetch("verdict"), "#{paper_id}/#{item_id}: phase2a verdict")
    assert!(phase2b.fetch("final_verdict") == phase2a.fetch("verdict"), "#{paper_id}/#{item_id}: unexpected change")

    row = {
      "item_id" => item_id,
      "concern_id" => phase2b.fetch("concern_id"),
      "obligation_class" => item.fetch("obligation_class").upcase,
      "original_comment" => phase2b.fetch("original_comment"),
      "authors_claim" => phase2b.fetch("authors_claim"),
      "revision_location" => phase2b.fetch("revision_location"),
      "verified" => VERIFIED_MAP.fetch(phase2b.fetch("final_verdict")),
      "status" => phase2b.fetch("final_verdict"),
      "quality_assessment" => phase2b.fetch("quality_assessment"),
      "final_verdict" => phase2b.fetch("final_verdict"),
      "phase2a_verdict" => phase2b.fetch("phase2a_verdict"),
      "verified_by" => phase2a.fetch("verified_by"),
      "author_triage" => author_record.fetch("author_triage"),
      "authorized_targets" => author_record.fetch("authorized_targets"),
      "claim_strength_authorizations" => author_record.fetch("claim_strength_authorizations")
    }
    row["author_reason"] = author_record.fetch("author_reason") if author_record.key?("author_reason")
    row["cross_model_status"] = "not_configured" if item.fetch("obligation_class") == "must_fix"
    row
  end

  residual_by_item = verdict.fetch("items").to_h do |record|
    [record.fetch("item_id"), record.dig("residual_gap", "residual_obligation_class")]
  end
  verdict_counts = PRIORITIES.to_h do |priority|
    priority_rows = rows.select { |row| roadmap_by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == priority }
    [priority, VERDICTS.to_h { |name| [name, priority_rows.count { |row| row.fetch("final_verdict") == name }] }]
  end
  residual_counts = PRIORITIES.to_h do |priority|
    priority_rows = rows.select { |row| roadmap_by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == priority }
    [priority, RESIDUALS.to_h do |magnitude|
      [magnitude, priority_rows.count do |row|
        row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && residual_by_item[row.fetch("item_id")] == magnitude
      end]
    end]
  end
  must_items = roadmap_items.select { |item| item.fetch("obligation_class") == "must_fix" }
  per_item = must_items.map do |item|
    row = rows.find { |candidate| candidate.fetch("item_id") == item.fetch("id") }
    entry = {
      "item_id" => item.fetch("id"),
      "final_verdict" => row.fetch("final_verdict"),
      "driving_severity" => %w[critical major minor].include?(item["severity"]) ? item["severity"] : nil
    }
    if row.fetch("final_verdict") == "PARTIALLY_ADDRESSED"
      entry["residual_obligation_class"] = residual_by_item.fetch(item.fetch("id"))
    end
    entry
  end
  should_items = roadmap_items.select { |item| item.fetch("obligation_class") == "should_fix" }
  should_numerator = should_items.count do |item|
    %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED].include?(integration_by_id.fetch(item.fetch("id")).fetch("final_verdict"))
  end
  regressions = verdict.fetch("new_issues").select { |issue| issue.fetch("attribution") == "regression" }.map do |issue|
    {"new_issue_id" => issue.fetch("new_issue_id"), "severity" => issue.fetch("severity")}
  end
  non_regressions = verdict.fetch("new_issues").reject { |issue| issue.fetch("attribution") == "regression" }.map { |issue| issue.fetch("new_issue_id") }
  escalations = []
  decision, reject_recommended, rule = derive_decision(rows, roadmap_by_id, residual_by_item, verdict.fetch("new_issues"), escalations)

  trace = {
    "contract_version" => "1.1",
    "round_id" => integration.fetch("round_id"),
    "revision" => 1,
    "verdict_record_hash" => jcs_sha256(verdict),
    "rows" => rows,
    "adjustments" => [],
    "new_issues" => verdict.fetch("new_issues"),
    "post_letter_observations" => integration.fetch("post_letter_observations"),
    "dissent_adjudications" => [],
    "resolution_intents" => [],
    "cross_model_resolutions" => [],
    "rebuttal_adjudications" => [],
    "g2d_acceptances" => [],
    "pending_rebuttal_upgrades" => [],
    "escalation_approvals" => [],
    "reapplications" => [],
    "decision_inputs" => {
      "per_item" => per_item,
      "verdict_counts" => verdict_counts,
      "residual_obligation_class_counts" => residual_counts,
      "should_fix_addressed_rate" => {"numerator" => should_numerator, "denominator" => should_items.length},
      "regressions" => regressions,
      "non_regression_new_issue_ids" => non_regressions,
      "escalations" => escalations,
      "reject_recommended" => reject_recommended,
      "apply_chain_witness" => "pass"
    },
    "decision_state" => decision
  }

  destination = if options[:candidate_dir]
                  File.join(options[:candidate_dir], "#{paper_id.downcase}_stage3_prime_round1_traceability.json")
                else
                  File.join(notes, "stage3_prime_round1_traceability.json")
                end
  File.write(destination, JSON.pretty_generate(trace) + "\n")
  summary << {paper_id: paper_id, path: destination, decision: decision, rule: rule, rows: rows.length}
end

summary.each { |entry| puts "#{entry[:paper_id]} #{entry[:decision]} #{entry[:rule]} #{entry[:rows]} rows -> #{entry[:path]}" }
