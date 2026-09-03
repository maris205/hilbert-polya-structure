#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
REQUEST_JSON = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json")
REQUEST_MD = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md")
INPUT_FREEZE = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json")

EXPECTED_AUTHORITY = {
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt" => "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md" => "67ad4ce8bfb34676b46ffb96e8c9833c1204ada3ffde1e0dc542ea43c46acca5",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json" => "c94137879092d7d475b22c8985a8f09073c29027f77a89b8ccb8749acfdac48b",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json" => "82dbf52120f120ffea6ba82b4614c69d4022a32bc01305a892eadde92b8248b7",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md" => "dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_AUDIT.json" => "b61f44535bd83b84da163391f30225de1b6afba5aa1434babb0bcca808c5b692",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_RECEIPT.json" => "f6eb05b19724b868b5aacb3dfbfb28ec56995675effd5984176bd9aea202f53e",
  "skills/route-a-evaluator.md" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
  "skills/route-b-evaluator.md" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
}.freeze

EXPECTED_TARGETS = {
  "P29" => {
    "REV-R1-1" => {"B0048" => %w[replace_block insert_after], "B0080" => %w[replace_block], "B0089" => %w[replace_block], "B0107" => %w[replace_block]},
    "REV-R3-1" => {"B0112" => %w[replace_block]},
    "REV-R3-2" => {"B0113" => %w[replace_block]},
    "REV-DA-2" => {"B0084" => %w[replace_block insert_after]},
    "NEW-1" => {"B0049" => %w[replace_block]}
  },
  "P32" => {
    "REV-P32-EIC-W1" => {"B0018" => %w[replace_block insert_after]},
    "REV-P32-EIC-W2" => {"B0098" => %w[replace_block insert_after], "B0125" => %w[replace_block]},
    "REV-P32-EIC-W4" => {"B0049" => %w[replace_block], "B0128" => %w[insert_after]},
    "REV-P32-R1-W1" => {"B0081" => %w[replace_block insert_after], "B0082" => %w[replace_block], "B0083" => %w[replace_block insert_after], "B0084" => %w[replace_block], "B0131" => %w[replace_block]},
    "REV-P32-R1-W2" => {"B0090" => %w[replace_block insert_after], "B0091" => %w[replace_block]},
    "REV-P32-R1-W4" => {"B0044" => %w[replace_block insert_after], "B0047" => %w[replace_block insert_after], "B0109" => %w[replace_block]},
    "REV-P32-DA-M1" => {"B0060" => %w[replace_block insert_after], "B0066" => %w[replace_block], "B0072" => %w[replace_block]}
  }
}.freeze

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
freeze = load_json(INPUT_FREEZE)
checks = []
check = lambda do |condition, label|
  assert!(condition, label)
  checks << label
end

check.call(request.fetch("schema_version") == "round10-stage4-prime-authorization-request/1.1", "request_schema")
check.call(request.fetch("status") == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION", "awaiting_confirmation")
check.call(request.fetch("proposed_display_order") == "source_traceability", "source_traceability_order")
check.call(request.fetch("proposed_author_triage") == "will_address", "proposed_will_address")
check.call(request.fetch("proposed_revision_round") == 2, "revision_round_2")
check.call(request.fetch("papers").map { |row| row.fetch("paper_id") } == %w[P29 P32], "paper_scope")

authority = request.fetch("authority_bindings").to_h { |row| [row.fetch("path"), row] }
check.call(authority.keys == EXPECTED_AUTHORITY.keys, "authority_path_set")
EXPECTED_AUTHORITY.each do |path, expected_sha|
  full = File.join(ROOT, path)
  row = authority.fetch(path)
  check.call(File.file?(full), "authority:#{path}:exists")
  check.call(sha(full) == expected_sha, "authority:#{path}:frozen_sha")
  check.call(row.fetch("sha256") == expected_sha, "authority:#{path}:request_sha")
  check.call(row.fetch("bytes") == File.size(full), "authority:#{path}:bytes")
end

freeze_papers = freeze.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }
total_residual = 0
total_new_issue = 0
total_targets = 0
total_operation_pairs = 0
unique_target_pairs = []

request.fetch("papers").each do |paper|
  paper_id = paper.fetch("paper_id")
  frozen = freeze_papers.fetch(paper_id)
  check.call(paper.fetch("paper_slug") == frozen.fetch("paper_slug"), "#{paper_id}:slug")
  check.call(paper.fetch("controlling_decision") == {"state" => "Major Revision", "rule" => "B4"}, "#{paper_id}:controlling_decision")

  artifact_keys = %w[
    stage3_prime_round3_verdict_record stage3_prime_round3_traceability
    stage3_prime_round3_checker_receipt stage4_round1_response
    stage4_round1_evidence_bundle stage4_prime_base_draft
    stage4_prime_block_manifest bibliography claim_surface_manifest
  ]
  artifact_keys.each do |key|
    row = paper.fetch(key)
    full = File.join(ROOT, row.fetch("path"))
    check.call(File.file?(full), "#{paper_id}:#{key}:exists")
    check.call(sha(full) == row.fetch("sha256"), "#{paper_id}:#{key}:sha")
    check.call(File.size(full) == row.fetch("bytes"), "#{paper_id}:#{key}:bytes")
  end

  verdict = load_json(File.join(ROOT, paper.dig("stage3_prime_round3_verdict_record", "path")))
  trace = load_json(File.join(ROOT, paper.dig("stage3_prime_round3_traceability", "path")))
  checker = load_json(File.join(ROOT, paper.dig("stage3_prime_round3_checker_receipt", "path")))
  manifest = load_json(File.join(ROOT, paper.dig("stage4_prime_block_manifest", "path")))
  claims = load_json(File.join(ROOT, paper.dig("claim_surface_manifest", "path")))
  draft_path = File.join(ROOT, paper.dig("stage4_prime_base_draft", "path"))
  blocks = manifest.fetch("blocks").to_h { |row| [row.fetch("block_id"), row] }
  draft_markers = File.read(draft_path, encoding: "UTF-8").scan(/<!--block:(B\d{4})-->/).flatten

  check.call(checker.fetch("checker_status") == "PASS", "#{paper_id}:checker_pass")
  check.call(checker.fetch("decision_state") == "Major Revision", "#{paper_id}:major_revision")
  check.call(checker.fetch("decision_rule") == "B4", "#{paper_id}:B4")
  check.call(checker.fetch("apply_chain_witness") == "pass", "#{paper_id}:apply_chain")
  check.call(sha(draft_path).start_with?(manifest.fetch("base_draft_hash")), "#{paper_id}:manifest_base")
  check.call(draft_markers == manifest.fetch("blocks").map { |row| row.fetch("block_id") }, "#{paper_id}:manifest_marker_order")
  check.call(draft_markers.uniq.length == draft_markers.length, "#{paper_id}:unique_block_ids")
  check.call(claims.fetch("surfaces") == [], "#{paper_id}:zero_registered_surfaces")

  partials = verdict.fetch("items").select { |row| row.fetch("verdict") == "PARTIALLY_ADDRESSED" }
  partial_trace = trace.fetch("rows").select { |row| row.fetch("phase2a_verdict") == "PARTIALLY_ADDRESSED" }
  items = paper.fetch("items")
  issue_actions = paper.fetch("round3_new_issue_actions")
  check.call(items.map { |row| row.fetch("item_id") } == partials.map { |row| row.fetch("item_id") }, "#{paper_id}:partial_coverage_order")
  check.call(items.map { |row| row.fetch("item_id") } == partial_trace.map { |row| row.fetch("item_id") }, "#{paper_id}:traceability_coverage_order")
  check.call(paper.fetch("partial_items") == items.length, "#{paper_id}:partial_count")
  check.call(paper.fetch("new_issue_actions") == issue_actions.length, "#{paper_id}:new_issue_count")
  check.call(issue_actions.map { |row| row.fetch("item_id") } == verdict.fetch("new_issues").map { |row| row.fetch("new_issue_id") }, "#{paper_id}:new_issue_coverage")

  actions = items + issue_actions
  check.call(actions.map { |row| row.fetch("item_id") } == EXPECTED_TARGETS.fetch(paper_id).keys, "#{paper_id}:action_order")
  actions.each do |item|
    item_id = item.fetch("item_id")
    expected_targets = EXPECTED_TARGETS.fetch(paper_id).fetch(item_id)
    actual_targets = item.fetch("proposed_targets").to_h { |target| [target.fetch("block_id"), target.fetch("allowed_operations")] }
    check.call(actual_targets == expected_targets, "#{paper_id}/#{item_id}:exact_target_operation_set")
    check.call(item.fetch("proposed_author_triage") == "will_address", "#{paper_id}/#{item_id}:triage")
    check.call(!item.fetch("implementation_branch").strip.empty?, "#{paper_id}/#{item_id}:implementation_branch")
    item.fetch("proposed_targets").each do |target|
      block_id = target.fetch("block_id")
      row = blocks.fetch(block_id)
      check.call(target.fetch("expected_old_hash") == row.fetch("old_hash"), "#{paper_id}/#{item_id}/#{block_id}:old_hash")
      check.call(target.fetch("first_line_excerpt") == row.fetch("first_line_excerpt"), "#{paper_id}/#{item_id}/#{block_id}:excerpt")
      check.call((target.fetch("allowed_operations") - %w[replace_block insert_after delete_block move_block]).empty?, "#{paper_id}/#{item_id}/#{block_id}:operation_vocabulary")
      target.fetch("allowed_operations").each { |op| unique_target_pairs << [paper_id, item_id, block_id, op] }
      total_targets += 1
      total_operation_pairs += target.fetch("allowed_operations").length
    end
  end

  items.each do |item|
    source = partials.find { |row| row.fetch("item_id") == item.fetch("item_id") }
    trace_row = partial_trace.find { |row| row.fetch("item_id") == item.fetch("item_id") }
    check.call(item.fetch("item_kind") == "residual_roadmap_item", "#{paper_id}/#{item.fetch('item_id')}:item_kind")
    check.call(item.fetch("phase2a_verdict") == "PARTIALLY_ADDRESSED", "#{paper_id}/#{item.fetch('item_id')}:source_verdict")
    check.call(item.fetch("residual_gap") == source.dig("residual_gap", "text"), "#{paper_id}/#{item.fetch('item_id')}:gap_binding")
    check.call(item.fetch("residual_obligation_class") == source.dig("residual_gap", "residual_obligation_class"), "#{paper_id}/#{item.fetch('item_id')}:residual_class")
    check.call(item.fetch("source_concern_id") == trace_row.fetch("concern_id"), "#{paper_id}/#{item.fetch('item_id')}:concern_binding")
    check.call(item.fetch("source_obligation_class") == trace_row.fetch("obligation_class"), "#{paper_id}/#{item.fetch('item_id')}:obligation_binding")
  end

  issue_actions.each do |item|
    source = verdict.fetch("new_issues").find { |row| row.fetch("new_issue_id") == item.fetch("item_id") }
    check.call(item.fetch("item_kind") == "round3_regression_new_issue", "#{paper_id}/#{item.fetch('item_id')}:issue_kind")
    check.call(item.fetch("severity") == source.fetch("severity"), "#{paper_id}/#{item.fetch('item_id')}:issue_severity")
    check.call(item.fetch("attribution") == "regression", "#{paper_id}/#{item.fetch('item_id')}:regression_attribution")
    check.call(item.fetch("location_anchor") == source.fetch("location_anchor"), "#{paper_id}/#{item.fetch('item_id')}:issue_location")
  end

  frozen_track = frozen.fetch("track_inputs").to_h { |row| [row.fetch("path"), row.fetch("sha256")] }
  %w[stage3_prime_round3_verdict_record stage3_prime_round3_traceability stage3_prime_round3_checker_receipt stage4_round1_response stage4_round1_evidence_bundle stage4_prime_base_draft claim_surface_manifest].each do |key|
    row = paper.fetch(key)
    check.call(frozen_track.fetch(row.fetch("path")) == row.fetch("sha256"), "#{paper_id}:freeze_binding:#{key}")
  end

  frozen_canonical = frozen.fetch("canonical_files").to_h { |row| [row.fetch("path"), row.fetch("sha256")] }
  frozen.fetch("canonical_files").each do |row|
    full = File.join(ROOT, row.fetch("path"))
    check.call(sha(full) == frozen_canonical.fetch(row.fetch("path")), "#{paper_id}:canonical_frozen:#{File.basename(full)}")
  end
  frozen.fetch("science_files").each do |row|
    full = File.join(ROOT, row.fetch("path"))
    check.call(sha(full) == row.fetch("sha256"), "#{paper_id}:science_frozen:#{row.fetch('path')}")
  end

  check.call(!File.exist?(File.join(ROOT, paper.fetch("proposed_patch_path"))), "#{paper_id}:no_stage4_prime_patch")
  check.call(!File.exist?(File.join(ROOT, paper.fetch("proposed_output_draft_path"))), "#{paper_id}:no_stage4_prime_output_draft")
  total_residual += items.length
  total_new_issue += issue_actions.length
end

check.call(unique_target_pairs.uniq.length == unique_target_pairs.length, "unique_item_target_operation_pairs")
check.call(total_residual == 11, "total_residual_items")
check.call(total_new_issue == 1, "total_regression_issues")
check.call(total_targets == 26, "total_target_entries")
check.call(total_operation_pairs == 36, "total_operation_pairs")
check.call(request.fetch("supporting_operations").length == 6, "supporting_operation_count")
check.call(request.fetch("structural_acknowledgment_requested") == [], "no_structural_acknowledgment")

closest = request.fetch("supporting_operations").find { |row| row.fetch("operation_id") == "P32-CLOSEST-WORK" }
check.call(closest.fetch("maximum_new_entries") == 4, "closest_work_max_four_entries")
check.call(closest.fetch("allowed_key_prefix") == "P32-CW", "closest_work_key_prefix")
check.call(closest.fetch("bibliography_path") == "papers/32-homology-cover-renormalization-uniformity/paper/references.bib", "closest_work_bibliography_scope")

claim = request.fetch("exact_conditional_claim_requested")
check.call(claim.fetch("paper_id") == "P32" && claim.fetch("item_id") == "REV-P32-DA-M1", "conditional_claim_item_scope")
check.call(claim.fetch("claim").include?("strictly greater than"), "conditional_claim_direction")
check.call(claim.fetch("proof_scope").include?("(1-x)^m < 1-x < 1-x^m"), "conditional_claim_proof_scope")
check.call(claim.fetch("boundary").include?("Route credit remain outside"), "conditional_claim_boundary")

boundaries = request.fetch("boundaries")
%w[request_only_no_current_manuscript_or_bibliography_write execution_requires_later_exact_confirmation].each do |key|
  check.call(boundaries.fetch(key) == true, "boundary:#{key}")
end
%w[revision_patch_emitted manuscripts_modified bibliographies_modified pdfs_built_or_modified claim_strength_replacements_authorized scientific_execution_performed canonical_result_refresh_performed route_a_change_performed route_b_invoked later_pipeline_stages_authorized].each do |key|
  check.call(boundaries.fetch(key) == false, "boundary:#{key}")
end
check.call(boundaries.fetch("registered_claim_surfaces") == 0, "boundary:registered_claim_surfaces")
check.call(boundaries.fetch("collateral_authorizations") == [], "boundary:collateral_authorizations")

md = File.read(REQUEST_MD, encoding: "UTF-8")
check.call(md.include?(sha(REQUEST_JSON)), "markdown_json_binding")
check.call(md.include?("11 residual roadmap items"), "markdown_residual_count")
check.call(md.include?("1 Round-3 regression issue"), "markdown_regression_count")
check.call(md.include?("26 exact target entries"), "markdown_target_count")
check.call(md.include?("36 block/operation pairs"), "markdown_operation_pair_count")
check.call(md.include?("Reply `确认`"), "markdown_short_confirmation")

payload = {
  "schema_version" => "round10-stage4-prime-authorization-request-validation/1.1",
  "generated_at_utc" => "2026-09-03T15:52:00Z",
  "request_json" => {"path" => File.basename(REQUEST_JSON), "sha256" => sha(REQUEST_JSON), "bytes" => File.size(REQUEST_JSON)},
  "request_markdown" => {"path" => File.basename(REQUEST_MD), "sha256" => sha(REQUEST_MD), "bytes" => File.size(REQUEST_MD)},
  "authority_record" => {"path" => "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md", "sha256" => EXPECTED_AUTHORITY.fetch("BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md")},
  "input_freeze" => {"path" => File.basename(INPUT_FREEZE), "sha256" => sha(INPUT_FREEZE)},
  "papers" => 2,
  "residual_roadmap_items" => total_residual,
  "round3_regression_issues" => total_new_issue,
  "exact_target_entries" => total_targets,
  "block_operation_pairs" => total_operation_pairs,
  "supporting_operations" => request.fetch("supporting_operations").length,
  "registered_claim_surfaces" => 0,
  "validation_checks" => checks.length,
  "current_manuscript_writes" => 0,
  "current_bibliography_writes" => 0,
  "current_pdf_builds" => 0,
  "current_scientific_executions" => 0,
  "route_changes" => 0,
  "status" => "PASS"
}
File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS -- P29/P32 Stage 4-prime request: #{checks.length} checks; #{total_residual} residual + #{total_new_issue} regression; #{total_targets} targets; #{total_operation_pairs} operation pairs"
