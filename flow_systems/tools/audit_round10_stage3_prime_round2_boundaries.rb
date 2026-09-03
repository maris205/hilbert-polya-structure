#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
FREEZE_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_INPUT_FREEZE.json")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_BOUNDARY_VALIDATION.json")
STAMP = "2026-09-03T12:30:00Z"

def assert!(condition, message)
  raise message unless condition
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def safe_file!(relative)
  assert!(!relative.start_with?("/"), "absolute frozen path: #{relative}")
  assert!(!relative.split("/").include?(".."), "traversal frozen path: #{relative}")
  path = File.expand_path(relative, ROOT)
  assert!(path.start_with?("#{ROOT}/"), "path escapes root: #{relative}")
  stat = File.lstat(path)
  assert!(stat.file? && !stat.symlink?, "not a regular non-symlink file: #{relative}")
  path
end

def verify_bindings!(bindings, label)
  bindings.map do |entry|
    path = safe_file!(entry.fetch("path"))
    assert!(File.size(path) == entry.fetch("bytes"), "#{label}: byte drift #{entry.fetch('path')}")
    assert!(sha256(path) == entry.fetch("sha256"), "#{label}: hash drift #{entry.fetch('path')}")
    entry.fetch("path")
  end
end

freeze = load_json(FREEZE_PATH)
assert!(freeze.fetch("schema_version") == "round10-stage3-prime-round2-input-freeze/1.0", "freeze schema")

counts = {}
counts["round1_terminal"] = verify_bindings!(freeze.fetch("round1_terminal_bindings"), "round1 terminal").length
counts["route_evaluators"] = verify_bindings!(freeze.fetch("route_evaluator_bindings"), "route evaluator").length

paper_rows = freeze.fetch("papers").map do |paper|
  paper_id = paper.fetch("paper_id")
  round1 = verify_bindings!(paper.fetch("round1_artifacts"), "#{paper_id} round1")
  canonical = verify_bindings!(paper.fetch("canonical_files"), "#{paper_id} canonical")
  science = verify_bindings!(paper.fetch("science_files"), "#{paper_id} science")
  review = verify_bindings!(paper.fetch("review_evidence_files"), "#{paper_id} review evidence")
  initial = verify_bindings!([paper.fetch("initial_system_source")], "#{paper_id} initial system")
  route = verify_bindings!([paper.fetch("route_crosswalk")], "#{paper_id} route")

  notes = File.join(ROOT, "papers", paper.fetch("paper_slug"), "notes")
  current_round1 = Dir[File.join(notes, "stage3_prime_round1_*")].sort.map { |path| path.delete_prefix("#{ROOT}/") }
  assert!(current_round1 == round1.sort, "#{paper_id}: Round-1 inventory drift")

  paper_root = File.join(ROOT, "papers", paper.fetch("paper_slug"))
  current_science = %w[code experiments results].flat_map do |dir|
    Dir.glob(File.join(paper_root, dir, "**", "*"), File::FNM_DOTMATCH)
       .select { |path| File.file?(path) }
       .map { |path| path.delete_prefix("#{ROOT}/") }
  end.sort
  assert!(current_science == science.sort, "#{paper_id}: science inventory drift")

  current_review = Dir[File.join(notes, "stage4_*")].flat_map do |path|
    File.directory?(path) ? Dir[File.join(path, "**", "*")] : [path]
  end.select { |path| File.file?(path) }.uniq.sort.map { |path| path.delete_prefix("#{ROOT}/") }
  assert!(current_review == review.sort, "#{paper_id}: Stage-4 evidence inventory drift")

  route_text = File.read(safe_file!(paper.fetch("route_crosswalk").fetch("path")), encoding: "UTF-8")
  %w[
    FORMAL_ROUTE_A_TUPLE=UNASSIGNED
    POSITIVE_ARITHMETIC_A2=0
    STAGE4_ROUTE_PROMOTION=NONE
    ROUTE_B_INVOKED=false
    CANONICAL_RESULTS_REFRESHED=false
  ].each { |token| assert!(route_text.include?(token), "#{paper_id}: missing route token #{token}") }

  {
    "paper_id" => paper_id,
    "round1_artifacts_unchanged" => round1.length,
    "canonical_files_unchanged" => canonical.length,
    "science_files_unchanged" => science.length,
    "review_evidence_files_unchanged" => review.length,
    "initial_system_sources_unchanged" => initial.length,
    "route_crosswalks_unchanged" => route.length,
    "status" => "PASS"
  }
end

payload = {
  "schema_version" => "round10-stage3-prime-round2-boundary-validation/1.0",
  "checked_at" => STAMP,
  "status" => "PASS",
  "input_freeze_sha256" => sha256(FREEZE_PATH),
  "papers" => paper_rows,
  "totals" => {
    "round1_artifacts_unchanged" => paper_rows.sum { |row| row.fetch("round1_artifacts_unchanged") } + counts.fetch("round1_terminal"),
    "canonical_files_unchanged" => paper_rows.sum { |row| row.fetch("canonical_files_unchanged") },
    "science_files_unchanged" => paper_rows.sum { |row| row.fetch("science_files_unchanged") },
    "review_evidence_files_unchanged" => paper_rows.sum { |row| row.fetch("review_evidence_files_unchanged") },
    "initial_system_sources_unchanged" => paper_rows.sum { |row| row.fetch("initial_system_sources_unchanged") },
    "route_crosswalks_unchanged" => paper_rows.sum { |row| row.fetch("route_crosswalks_unchanged") },
    "route_evaluators_unchanged" => counts.fetch("route_evaluators")
  },
  "boundaries" => {
    "manuscript_bibliography_pdf_writes" => 0,
    "science_writes" => 0,
    "initial_system_changes" => 0,
    "formal_route_a_tuples_assigned" => 0,
    "positive_arithmetic_a2_results" => 0,
    "route_b_invocations" => 0,
    "successor_stage_authorized" => false
  }
}

File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS — Round-2 frozen boundaries: #{payload.fetch('totals').values.sum} file bindings verified"
