#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
FREEZE_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_INPUT_FREEZE.json")
REQUEST_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json")
REQUEST_VALIDATION_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_BOUNDARY_VALIDATION.json")

def assert!(condition, message)
  raise "ROUND3_BOUNDARY_FAIL_CLOSED: #{message}" unless condition
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def safe_file!(relative)
  assert!(!relative.start_with?("/") && !relative.split("/").include?(".."), "unsafe path #{relative}")
  path = File.expand_path(relative, ROOT)
  assert!(path.start_with?("#{ROOT}/"), "path escape #{relative}")
  stat = File.lstat(path)
  assert!(stat.file? && !stat.symlink?, "not a regular non-symlink file #{relative}")
  path
rescue Errno::ENOENT
  raise "ROUND3_BOUNDARY_FAIL_CLOSED: missing #{relative}"
end

def verify_bindings!(rows, label)
  rows.map do |row|
    path = safe_file!(row.fetch("path"))
    assert!(File.size(path) == row.fetch("bytes"), "#{label} byte drift #{row.fetch('path')}") if row.key?("bytes")
    assert!(sha256(path) == row.fetch("sha256"), "#{label} hash drift #{row.fetch('path')}")
    row.fetch("path")
  end
end

freeze = load_json(FREEZE_PATH)
assert!(freeze.fetch("schema_version") == "round10-stage3-prime-round3-input-freeze/1.0", "freeze schema")
root_round2 = verify_bindings!(freeze.fetch("round2_terminal_bindings"), "Round-2 terminal")
route_evaluators = verify_bindings!(freeze.fetch("route_evaluator_bindings"), "Route evaluator")

paper_rows = freeze.fetch("papers").map do |paper|
  paper_id = paper.fetch("paper_id")
  slug = paper.fetch("paper_slug")
  paper_root = File.join(ROOT, "papers", slug)
  notes = File.join(paper_root, "notes")
  round2 = verify_bindings!(paper.fetch("round2_artifacts"), "#{paper_id} Round-2")
  canonical = verify_bindings!(paper.fetch("canonical_files"), "#{paper_id} canonical")
  science = verify_bindings!(paper.fetch("science_files"), "#{paper_id} science")
  review = verify_bindings!(paper.fetch("review_evidence_files"), "#{paper_id} Stage-4 evidence")
  initial = verify_bindings!([paper.fetch("initial_system_source")], "#{paper_id} initial system")
  route = verify_bindings!([paper.fetch("route_crosswalk")], "#{paper_id} Route crosswalk")

  current_round2 = Dir[File.join(notes, "stage3_prime_round2_*")].select { |path| File.file?(path) }.sort.map { |path| path.delete_prefix("#{ROOT}/") }
  assert!(current_round2 == round2.sort, "#{paper_id} Round-2 inventory drift")
  current_science = %w[code experiments results].flat_map do |directory|
    Dir.glob(File.join(paper_root, directory, "**", "*"), File::FNM_DOTMATCH)
       .select { |path| File.file?(path) }
       .map { |path| path.delete_prefix("#{ROOT}/") }
  end.sort
  assert!(current_science == science.sort, "#{paper_id} science inventory drift")
  current_review = Dir[File.join(notes, "stage4_*")].flat_map do |path|
    File.directory?(path) ? Dir[File.join(path, "**", "*")] : [path]
  end.select { |path| File.file?(path) }.uniq.sort.map { |path| path.delete_prefix("#{ROOT}/") }
  assert!(current_review == review.sort, "#{paper_id} Stage-4 evidence inventory drift")

  route_text = File.read(safe_file!(paper.fetch("route_crosswalk").fetch("path")), encoding: "UTF-8")
  %w[FORMAL_ROUTE_A_TUPLE=UNASSIGNED POSITIVE_ARITHMETIC_A2=0 STAGE4_ROUTE_PROMOTION=NONE ROUTE_B_INVOKED=false CANONICAL_RESULTS_REFRESHED=false].each do |token|
    assert!(route_text.include?(token), "#{paper_id} missing frozen Route token #{token}")
  end
  {
    "paper_id" => paper_id,
    "round2_artifacts_unchanged" => round2.length,
    "canonical_files_unchanged" => canonical.length,
    "science_files_unchanged" => science.length,
    "review_evidence_files_unchanged" => review.length,
    "initial_system_sources_unchanged" => initial.length,
    "route_crosswalks_unchanged" => route.length,
    "status" => "PASS"
  }
end

request_validation = load_json(REQUEST_VALIDATION_PATH)
assert!(request_validation.fetch("status") == "PASS", "P30/P31 request validation")
assert!(request_validation.fetch("request_json").fetch("sha256") == sha256(REQUEST_PATH), "request JSON drift")
assert!(request_validation.fetch("request_markdown").fetch("sha256") == sha256(File.join(ROOT, request_validation.fetch("request_markdown").fetch("path"))), "request Markdown drift")
request = load_json(REQUEST_PATH)
request.fetch("papers").each do |paper|
  %w[stage3_prime_round2_verdict_record stage3_prime_round2_traceability stage3_prime_round2_checker_receipt stage4_prime_base_draft stage4_prime_block_manifest bibliography claim_surface_manifest].each do |key|
    verify_bindings!([paper.fetch(key)], "#{paper.fetch('paper_id')} request #{key}")
  end
end

totals = {
  "round2_terminal_bindings_unchanged" => root_round2.length + paper_rows.sum { |row| row.fetch("round2_artifacts_unchanged") },
  "canonical_files_unchanged" => paper_rows.sum { |row| row.fetch("canonical_files_unchanged") },
  "science_files_unchanged" => paper_rows.sum { |row| row.fetch("science_files_unchanged") },
  "review_evidence_files_unchanged" => paper_rows.sum { |row| row.fetch("review_evidence_files_unchanged") },
  "initial_system_sources_unchanged" => paper_rows.sum { |row| row.fetch("initial_system_sources_unchanged") },
  "route_crosswalks_unchanged" => paper_rows.sum { |row| row.fetch("route_crosswalks_unchanged") },
  "route_evaluators_unchanged" => route_evaluators.length,
  "p30_p31_request_checks_replayed" => request_validation.fetch("validation_checks")
}

payload = {
  "schema_version" => "round10-stage3-prime-round3-boundary-validation/1.0",
  "checked_at" => "2026-09-03T16:00:00Z",
  "status" => "PASS",
  "input_freeze_sha256" => sha256(FREEZE_PATH),
  "papers" => paper_rows,
  "totals" => totals,
  "p30_p31_stage4_prime_request" => {
    "request_sha256" => sha256(REQUEST_PATH),
    "validation_sha256" => sha256(REQUEST_VALIDATION_PATH),
    "residual_items" => request_validation.fetch("residual_items"),
    "target_blocks" => request_validation.fetch("manuscript_target_blocks"),
    "checks" => request_validation.fetch("validation_checks"),
    "status" => "PASS_AWAITING_EXPLICIT_AUTHOR_CONFIRMATION"
  },
  "boundaries" => {
    "manuscript_bibliography_pdf_writes" => 0,
    "science_writes" => 0,
    "initial_system_changes" => 0,
    "formal_route_a_tuples_assigned" => 0,
    "positive_arithmetic_a2_results" => 0,
    "route_b_invocations" => 0,
    "stage4_prime_manuscript_patch_authorized" => false,
    "stage4_5_or_stage5_authorized" => false
  }
}
File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS — Round-3/P30-P31 boundaries: #{totals.values.sum} checks or bindings"
