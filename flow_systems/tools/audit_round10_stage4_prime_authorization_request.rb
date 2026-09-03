#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
REQUEST_JSON = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json")
REQUEST_MD = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json")

def assert!(condition, message)
  raise message unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

request = load_json(REQUEST_JSON)
checks = []
check = lambda do |condition, label|
  assert!(condition, label)
  checks << label
end

check.call(request.fetch("schema_version") == "round10-stage4-prime-authorization-request/1.0", "request_schema")
check.call(request.fetch("status") == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION", "awaiting_confirmation")
check.call(request.fetch("proposed_display_order") == "source_traceability", "source_traceability_order")
check.call(request.fetch("proposed_author_triage") == "will_address", "proposed_will_address")
check.call(request.fetch("papers").map { |row| row.fetch("paper_id") } == %w[P30 P31], "paper_scope")

total_items = 0
total_targets = 0
request.fetch("papers").each do |paper|
  paper_id = paper.fetch("paper_id")
  verdict_path = File.join(ROOT, paper.dig("stage3_prime_round2_verdict_record", "path"))
  trace_path = File.join(ROOT, paper.dig("stage3_prime_round2_traceability", "path"))
  checker_path = File.join(ROOT, paper.dig("stage3_prime_round2_checker_receipt", "path"))
  draft_path = File.join(ROOT, paper.dig("stage4_prime_base_draft", "path"))
  manifest_path = File.join(ROOT, paper.dig("stage4_prime_block_manifest", "path"))
  bib_path = File.join(ROOT, paper.dig("bibliography", "path"))
  claim_path = File.join(ROOT, paper.dig("claim_surface_manifest", "path"))
  {
    "verdict" => [verdict_path, paper.dig("stage3_prime_round2_verdict_record", "sha256")],
    "trace" => [trace_path, paper.dig("stage3_prime_round2_traceability", "sha256")],
    "checker" => [checker_path, paper.dig("stage3_prime_round2_checker_receipt", "sha256")],
    "draft" => [draft_path, paper.dig("stage4_prime_base_draft", "sha256")],
    "manifest" => [manifest_path, paper.dig("stage4_prime_block_manifest", "sha256")],
    "bibliography" => [bib_path, paper.dig("bibliography", "sha256")],
    "claim_surface" => [claim_path, paper.dig("claim_surface_manifest", "sha256")]
  }.each do |label, (path, expected)|
    check.call(File.file?(path) && sha(path) == expected, "#{paper_id}:#{label}_binding")
  end
  verdict = load_json(verdict_path)
  manifest = load_json(manifest_path)
  claim = load_json(claim_path)
  partials = verdict.fetch("items").select { |row| row.fetch("verdict") == "PARTIALLY_ADDRESSED" }
  items = paper.fetch("items")
  check.call(items.map { |row| row.fetch("item_id") } == partials.map { |row| row.fetch("item_id") }, "#{paper_id}:partial_coverage_order")
  check.call(paper.fetch("partial_items") == items.length, "#{paper_id}:item_count")
  block_ids = manifest.fetch("blocks").map { |row| row.fetch("block_id") }
  check.call(sha(draft_path).start_with?(manifest.fetch("base_draft_hash")), "#{paper_id}:manifest_base")
  check.call(claim.fetch("surfaces").empty?, "#{paper_id}:zero_registered_surfaces")
  items.each do |item|
    check.call(item.fetch("phase2a_verdict") == "PARTIALLY_ADDRESSED", "#{paper_id}/#{item.fetch('item_id')}:source_verdict")
    check.call(%w[must_fix should_fix consider].include?(item.fetch("residual_obligation_class")), "#{paper_id}/#{item.fetch('item_id')}:residual_class")
    check.call(item.fetch("proposed_author_triage") == "will_address", "#{paper_id}/#{item.fetch('item_id')}:triage")
    item.fetch("proposed_targets").each do |target|
      check.call(block_ids.include?(target.fetch("block_id")), "#{paper_id}/#{item.fetch('item_id')}:target_#{target.fetch('block_id')}")
      check.call(!target.fetch("allowed_operations").empty? && (target.fetch("allowed_operations") - %w[replace_block insert_after delete_block move_block]).empty?, "#{paper_id}/#{item.fetch('item_id')}:operations_#{target.fetch('block_id')}")
      total_targets += 1
    end
    total_items += 1
  end
end

boundaries = request.fetch("boundaries")
%w[request_only_no_write].each { |key| check.call(boundaries.fetch(key) == true, "boundary:#{key}") }
%w[revision_patch_emitted manuscripts_modified bibliographies_modified claim_strength_replacements_authorized scientific_execution_authorized canonical_result_refresh_authorized route_a_change_authorized route_b_authorized later_pipeline_stages_authorized].each do |key|
  check.call(boundaries.fetch(key) == false, "boundary:#{key}")
end
check.call(boundaries.fetch("registered_claim_surfaces") == 0, "boundary:registered_claim_surfaces")
check.call(boundaries.fetch("collateral_authorizations") == [], "boundary:collateral_authorizations")
check.call(total_items == 13, "total_items")
check.call(request.fetch("supporting_operations").length == 4, "supporting_operation_count")
check.call(request.fetch("structural_acknowledgment_requested").length == 1, "structural_acknowledgment_count")
check.call(File.read(REQUEST_MD, encoding: "UTF-8").include?(sha(REQUEST_JSON)), "markdown_json_binding")

payload = {
  "schema_version" => "round10-stage4-prime-authorization-request-validation/1.0",
  "generated_at_utc" => "2026-09-03T13:10:00Z",
  "request_json" => {"path" => File.basename(REQUEST_JSON), "sha256" => sha(REQUEST_JSON)},
  "request_markdown" => {"path" => File.basename(REQUEST_MD), "sha256" => sha(REQUEST_MD)},
  "papers" => 2,
  "residual_items" => total_items,
  "manuscript_target_blocks" => total_targets,
  "validation_checks" => checks.length,
  "manuscript_writes" => 0,
  "bibliography_writes" => 0,
  "route_changes" => 0,
  "status" => "PASS"
}
File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS -- P30/P31 Stage 4-prime request: #{checks.length} checks, #{total_items} items, #{total_targets} targets"
