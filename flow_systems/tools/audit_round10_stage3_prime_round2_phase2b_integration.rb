#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "optparse"

ROOT = File.expand_path("..", __dir__)
PAPER_SLUGS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

options = { round: "round2", paper_ids: %w[P30 P31], generated_at: "2026-09-03T11:00:00Z" }
OptionParser.new do |parser|
  parser.on("--round ROUND", /\Around[1-9][0-9]*\z/, "Artifact round token (default: round2)") { |round| options[:round] = round }
  parser.on("--papers IDS", "Comma-separated paper IDs (default: P30,P31)") { |ids| options[:paper_ids] = ids.split(",") }
  parser.on("--generated-at TIME", "Receipt timestamp") { |time| options[:generated_at] = time }
end.parse!
raise "duplicate paper id" unless options[:paper_ids].uniq == options[:paper_ids]
unknown_papers = options[:paper_ids] - PAPER_SLUGS.keys
raise "unknown paper id(s): #{unknown_papers.join(',')}" unless unknown_papers.empty?
papers_to_audit = options[:paper_ids].to_h { |paper_id| [paper_id, PAPER_SLUGS.fetch(paper_id)] }
round_upper = options[:round].upcase
output = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_#{round_upper}_PHASE2B_INTEGRATION_VALIDATION.json")
phase2a_validation = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_#{round_upper}_PHASE2A_VALIDATION.json")

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

phase2a = load_json(phase2a_validation)
phase2a_by_paper = phase2a.fetch("papers").to_h { |paper| [paper.fetch("paper_id"), paper] }
papers = []
total_checks = 0
total_rows = 0

papers_to_audit.each do |paper_id, slug|
  notes = File.join(ROOT, "papers", slug, "notes")
  manifest = load_json(File.join(notes, "stage3_prime_#{options[:round]}_input_manifest.json"))
  roadmap = load_json(File.join(notes, "stage3_revision_roadmap.json"))
  response = load_json(File.join(notes, "stage4_response_to_reviewers_round1.json"))
  verdict_path = File.join(notes, "stage3_prime_#{options[:round]}_verdict_record.json")
  integration_path = File.join(notes, "stage3_prime_#{options[:round]}_phase2b_integration.json")
  verdict = load_json(verdict_path)
  integration = load_json(integration_path)
  checks = []
  check = lambda do |condition, label|
    assert!(condition, "#{paper_id}: #{label}")
    checks << label
  end

  frozen_2a = phase2a_by_paper.fetch(paper_id)
  check.call(sha256(verdict_path) == frozen_2a.fetch("verdict_record_sha256"), "phase2a_raw_immutability")
  check.call(jcs_sha256(verdict) == frozen_2a.fetch("verdict_record_jcs_sha256"), "phase2a_jcs_immutability")
  response_manifest = manifest.dig("artifacts", "response_to_reviewers")
  check.call(response_manifest.fetch("present"), "response_manifest_present")
  check.call(sha256(File.join(ROOT, "papers", slug, response_manifest.fetch("path_or_passport_ref").delete_prefix("path:"))) == response_manifest.fetch("sha256"), "response_raw_hash_binding")
  check.call(integration.keys.sort == %w[adjustments contract_version post_letter_observations round_id rows verdict_record_hash].sort,
             "closed_integration_shape")
  check.call(integration.fetch("contract_version") == "1.1", "contract_version")
  check.call(integration.fetch("round_id") == manifest.fetch("round_id"), "round_id_binding")
  check.call(integration.fetch("verdict_record_hash") == jcs_sha256(verdict), "verdict_record_jcs_binding")

  roadmap_items = roadmap.fetch("items")
  verdict_by_item = verdict.fetch("items").to_h { |row| [row.fetch("item_id"), row] }
  response_items = response.fetch("items")
  response_by_item = response_items.to_h { |row| [row.fetch("roadmap_item_id"), row] }
  rows = integration.fetch("rows")
  check.call(response_items.map { |row| row.fetch("roadmap_item_id") } == roadmap_items.map { |item| item.fetch("id") }, "response_coverage_and_order")
  check.call(rows.map { |row| row.fetch("item_id") } == roadmap_items.map { |item| item.fetch("id") }, "integration_coverage_and_order")

  counters = Hash.new(0)
  expected_concerns = roadmap_items.map do |item|
    prefix = {"must_fix" => "R", "should_fix" => "S", "consider" => "N"}.fetch(item.fetch("obligation_class"))
    counters[prefix] += 1
    "#{prefix}#{counters[prefix]}"
  end
  check.call(rows.map { |row| row.fetch("concern_id") } == expected_concerns, "concern_id_derivation")

  adjustment_ids = integration.fetch("adjustments").map { |record| record.fetch("adjustment_id") }
  check.call(adjustment_ids.uniq.length == adjustment_ids.length, "adjustment_id_uniqueness")
  adjustments_by_item = integration.fetch("adjustments").group_by { |record| record.fetch("item_id") }
  rows.zip(roadmap_items).each do |row, item|
    item_id = item.fetch("id")
    response_row = response_by_item.fetch(item_id)
    phase2a_row = verdict_by_item.fetch(item_id)
    check.call(row.keys.sort == %w[authors_claim concern_id final_verdict item_id original_comment phase2a_verdict quality_assessment revision_location].sort,
               "#{item_id}:closed_row_shape")
    check.call(!response_row.fetch("reviewer_comment").strip.empty?, "#{item_id}:response_comment_present")
    check.call(row.fetch("original_comment") == item.fetch("description"), "#{item_id}:original_comment_binding")
    check.call(row.fetch("authors_claim") == response_row.fetch("author_response"), "#{item_id}:authors_claim_binding")
    check.call(row.fetch("revision_location") == response_row.fetch("change_location"), "#{item_id}:revision_location_binding")
    check.call(!row.fetch("quality_assessment").strip.empty?, "#{item_id}:quality_assessment_nonempty")
    check.call(row.fetch("phase2a_verdict") == phase2a_row.fetch("verdict"), "#{item_id}:phase2a_verdict_binding")
    chain = adjustments_by_item.fetch(item_id, [])
    if chain.empty?
      check.call(row.fetch("final_verdict") == row.fetch("phase2a_verdict"), "#{item_id}:no_silent_change")
    else
      check.call(chain.first.fetch("from_verdict") == row.fetch("phase2a_verdict"), "#{item_id}:adjustment_head")
      check.call(chain.last.fetch("to_verdict") == row.fetch("final_verdict"), "#{item_id}:adjustment_tail")
    end
  end

  forbidden_keys = %w[author_triage author_reason authorized_targets claim_strength_authorizations decision_inputs decision_state]
  serialized = JSON.generate(integration)
  forbidden_keys.each do |key|
    check.call(!serialized.include?(%Q["#{key}"]), "checker_only_field_absent:#{key}")
  end

  changed = rows.count { |row| row.fetch("phase2a_verdict") != row.fetch("final_verdict") }
  papers << {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "round_id" => integration.fetch("round_id"),
    "integration_sha256" => sha256(integration_path),
    "integration_jcs_sha256" => jcs_sha256(integration),
    "rows" => rows.length,
    "adjustments" => integration.fetch("adjustments").length,
    "verdict_changes" => changed,
    "post_letter_observations" => integration.fetch("post_letter_observations").length,
    "validation_checks" => checks.length,
    "status" => "PASS"
  }
  total_checks += checks.length
  total_rows += rows.length
end

payload = {
  "schema_version" => "round10-stage3-prime-#{options[:round]}-phase2b-integration-validation/1.0",
  "generated_at" => options[:generated_at],
  "contract_version" => "1.1",
  "phase" => "phase2b_response_matching",
  "papers" => papers,
  "totals" => {
    "papers" => papers.length,
    "response_rows" => total_rows,
    "validation_checks" => total_checks,
    "adjustments" => papers.sum { |paper| paper.fetch("adjustments") },
    "verdict_changes" => papers.sum { |paper| paper.fetch("verdict_changes") },
    "post_letter_observations" => papers.sum { |paper| paper.fetch("post_letter_observations") },
    "phase2b_integration_validation" => "PASS"
  },
  "boundary" => {
    "author_adjudication_used_as_criterion_input" => false,
    "phase2b_retry_used" => false,
    "traceability_emitted" => false,
    "manuscripts_modified" => false,
    "science_artifacts_modified" => false,
    "route_credit_changed" => false
  }
}

File.write(output, JSON.pretty_generate(payload) + "\n")
puts "PASS — Round 10 Stage 3′ #{options[:round]} Phase 2B integration: #{total_checks} checks; #{total_rows} response rows"
