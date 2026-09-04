#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
AUTHORITY_PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
OUTPUT = ROOT / "#{AUTHORITY_PREFIX}_AUTHORITY_AUDIT.json"

EXPECTED = {
  "#{AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt" => "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe",
  "#{AUTHORITY_PREFIX}_AUTHORIZATION_RECORD.md" => "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79",
  "#{AUTHORITY_PREFIX}_INPUT_FREEZE.json" => "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1",
  "#{AUTHORITY_PREFIX}_AUTHORIZATION_RECEIPT.json" => "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21",
  "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_MANDATORY_CHECKPOINT.md" => "0fb41c724ee484335190b823d904d199b11b69528ea890d15119530eb26507d2",
  "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json" => "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b",
  "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json" => "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json" => "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65"
}.freeze

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def collect_bindings(node, rows = [])
  case node
  when Hash
    if node["path"].is_a?(String) && node["sha256"].is_a?(String) && node["sha256"].match?(/\A[0-9a-f]{64}\z/)
      rows << [node.fetch("path"), node.fetch("sha256")]
    end
    node.each_value { |value| collect_bindings(value, rows) }
  when Array
    node.each { |value| collect_bindings(value, rows) }
  end
  rows
end

checks = []
check = lambda do |id, condition, detail = nil|
  checks << { "check_id" => id, "status" => condition ? "PASS" : "FAIL", "detail" => detail }.compact
end

EXPECTED.each do |relative, expected|
  path = ROOT / relative
  actual = path.file? ? sha(path) : nil
  check.call("binding:#{relative}", actual == expected, { "expected" => expected, "actual" => actual })
end

event = ROOT / "#{AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt"
check.call("author-event:exact-bytes", event.file? && event.binread == "确认\n".b)

freeze_path = ROOT / "#{AUTHORITY_PREFIX}_INPUT_FREEZE.json"
receipt_path = ROOT / "#{AUTHORITY_PREFIX}_AUTHORIZATION_RECEIPT.json"
freeze = JSON.parse(freeze_path.read)
receipt = JSON.parse(receipt_path.read)
check.call("freeze:status", freeze["status"] == "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION")
check.call("receipt:status", receipt["status"] == "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION")
check.call("scope:aggregate", freeze.dig("authorized_scope", "unique_replace_block_pairs") == 130 && receipt.dig("aggregate", "unique_replace_block_pairs") == 130)
check.call("scope:per-paper", freeze.dig("authorized_scope", "per_paper") == {"P29" => 31, "P30" => 34, "P31" => 13, "P32" => 15, "P33" => 37})
check.call("scope:matrix", freeze.dig("authorized_scope", "p30_p31_in_place_matrix_regenerations") == 2)
check.call("scope:p33-bib", freeze.dig("authorized_scope", "p33_bibliography_append_keys") == ["P33-S03-CORR", "P33-S16-CORR"])
check.call("scope:p33-uses", freeze.dig("authorized_scope", "p33_use_bindings") == ["P33-U08", "P33-U22", "P33-U27", "P33-U28", "P33-U37"])
check.call("scope:p33-fresh-chain", freeze.dig("authorized_scope", "p33_fresh_successor_authority_chain") == true)

false_boundaries = %w[
  fresh_stage4_5_authorized
  p33_re_review_authorized
  stage5_or_stage6_authorized
  canonical_promotion_authorized
  scientific_producer_enumeration_census_or_result_refresh_authorized
  route_a_or_route_b_credit_authorized
  route_or_initial_system_mutation_authorized
  structural_edit_authorized
]
check.call("boundaries:all-retained", false_boundaries.all? { |key| freeze.dig("boundaries", key) == false }, freeze.fetch("boundaries"))
check.call("citation-style:plainnat-numeric", freeze.dig("boundaries", "citation_style") == "natbib numbers sort&compress with plainnat")

{
  "prior-freeze" => [freeze.dig("superseded_freeze_replay", "bindings"), 94],
  "request-artifacts" => [freeze.dig("expanded_request_referenced_artifact_replay", "bindings"), 85],
  "prepared-execution-evidence" => [collect_bindings(freeze.fetch("prepared_execution_evidence")), 38],
  "prepared-cross-audits" => [collect_bindings(freeze.fetch("prepared_cross_audits")), 3]
}.each do |label, (rows, expected_count)|
  unique = rows.to_h { |row| row.is_a?(Array) ? row : [row.fetch("path"), row.fetch("sha256")] }
  check.call("#{label}:count", unique.length == expected_count, { "expected" => expected_count, "actual" => unique.length })
  failures = unique.filter_map do |relative, expected|
    path = ROOT / relative
    actual = path.file? ? sha(path) : nil
    { "path" => relative, "expected" => expected, "actual" => actual } unless actual == expected
  end
  check.call("#{label}:replay", failures.empty?, failures)
end

freeze.fetch("papers").each do |paper|
  paper_id = paper.fetch("paper_id")
  draft = ROOT / paper.dig("current_working_draft", "path")
  manifest_path = ROOT / paper.dig("block_manifest", "path")
  manifest = JSON.parse(manifest_path.read)
  check.call("#{paper_id}:draft-binding", sha(draft) == paper.dig("current_working_draft", "sha256"))
  check.call("#{paper_id}:manifest-binding", sha(manifest_path) == paper.dig("block_manifest", "sha256"))
  bibliography = ROOT / paper.dig("current_working_bibliography", "path")
  check.call("#{paper_id}:bibliography-binding", sha(bibliography) == paper.dig("current_working_bibliography", "sha256"))
  check.call("#{paper_id}:manifest-base", sha(draft).start_with?(manifest.fetch("base_draft_hash")), { "draft" => sha(draft), "manifest_base" => manifest.fetch("base_draft_hash") })
  paper.fetch("canonical_files").each do |row|
    check.call("#{paper_id}:canonical:#{row.fetch('path')}", sha(ROOT / row.fetch("path")) == row.fetch("sha256"))
  end
  paper.fetch("science_files").each do |row|
    check.call("#{paper_id}:science:#{row.fetch('path')}", sha(ROOT / row.fetch("path")) == row.fetch("sha256"))
  end
  check.call("#{paper_id}:initial-system", sha(ROOT / paper.dig("initial_system_source", "path")) == paper.dig("initial_system_source", "sha256"))
  check.call("#{paper_id}:route", sha(ROOT / paper.dig("route_crosswalk", "path")) == paper.dig("route_crosswalk", "sha256"))
  if paper.key?("authorized_in_place_matrix_regeneration")
    row = paper.fetch("authorized_in_place_matrix_regeneration")
    check.call("#{paper_id}:matrix", sha(ROOT / row.fetch("path")) == row.fetch("sha256"))
  end
end

freeze.fetch("route_evaluators").each do |row|
  check.call("route-evaluator:#{row.fetch('path')}", sha(ROOT / row.fetch("path")) == row.fetch("sha256"))
end

check.call("receipt:record-binding", receipt.dig("authorization_record", "sha256") == EXPECTED.fetch("#{AUTHORITY_PREFIX}_AUTHORIZATION_RECORD.md"))
check.call("receipt:freeze-binding", receipt.dig("input_freeze", "sha256") == EXPECTED.fetch("#{AUTHORITY_PREFIX}_INPUT_FREEZE.json"))
check.call("receipt:author-binding", receipt.dig("author_event", "sha256") == EXPECTED.fetch("#{AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt"))
check.call("receipt:prepared-evidence-binding", receipt.fetch("prepared_execution_evidence") == freeze.fetch("prepared_execution_evidence"))
check.call("receipt:cross-audit-binding", receipt.fetch("prepared_cross_audits") == freeze.fetch("prepared_cross_audits"))

failed = checks.count { |row| row.fetch("status") == "FAIL" }
audit = {
  "schema_version" => "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authority-audit/1.0",
  "generated_at_utc" => Time.now.utc.iso8601,
  "workflow_date" => "2026-09-04",
  "status" => failed.zero? ? "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY" : "FAIL_CLOSED",
  "checks_run" => checks.length,
  "checks_passed" => checks.length - failed,
  "checks_failed" => failed,
  "checks" => checks,
  "next_legal_action" => failed.zero? ? "A distinct applicator may replay the exact requests and prepared patch evidence before deterministic apply." : "Stop before apply and repair the named binding failure."
}
abort("refusing to overwrite #{OUTPUT.basename}") if OUTPUT.exist?
File.binwrite(OUTPUT, JSON.pretty_generate(audit) + "\n")
abort("authority audit failed closed") unless failed.zero?
puts "authority audit PASS #{checks.length}/#{checks.length}: #{sha(OUTPUT)}"
