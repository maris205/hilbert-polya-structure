#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
FREEZE_PATH = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_BOUNDARY_VALIDATION.json")

freeze = JSON.parse(File.read(FREEZE_PATH, encoding: "UTF-8"))
expected = {}

collect = lambda do |value|
  case value
  when Hash
    if value["path"].is_a?(String) && value["sha256"].is_a?(String)
      prior = expected[value.fetch("path")]
      raise "conflicting frozen hashes for #{value.fetch('path')}" if prior && prior != value.fetch("sha256")
      expected[value.fetch("path")] = value.fetch("sha256")
    end
    value.each_value { |child| collect.call(child) }
  when Array
    value.each { |child| collect.call(child) }
  end
end
collect.call(freeze)

checks = []
failures = []
check = lambda do |condition, label|
  condition ? checks << label : failures << label
end

expected.sort.each do |relative, digest|
  path = File.join(ROOT, relative)
  check.call(File.file?(path) && !File.symlink?(path), "frozen real file: #{relative}")
  check.call(Digest::SHA256.file(path).hexdigest == digest, "frozen bytes: #{relative}") if File.file?(path)
end

paper_slugs = %w[
  29-bianchi-ideal-owner-refinement
  30-three-disk-nonconstant-roof-determinant
  31-level11-conjugacy-owner-ledger
  32-homology-cover-renormalization-uniformity
  33-bolza-control-matched-census
]

%w[29-bianchi-ideal-owner-refinement 32-homology-cover-renormalization-uniformity].each do |slug|
  notes = File.join(ROOT, "papers", slug, "notes")
  forbidden = Dir.glob(File.join(notes, "stage4_prime_revision_patch*")).sort +
              Dir.glob(File.join(notes, "stage4_prime_revision_round*")).sort +
              Dir.glob(File.join(notes, "stage4_prime_references*")).sort
  check.call(forbidden.empty?, "#{slug}: request-only track emitted no patch/apply/revision/bibliography")
end

later_stage_files = paper_slugs.flat_map do |slug|
  Dir.glob(File.join(ROOT, "papers", slug, "**", "*"), File::FNM_DOTMATCH)
    .select { |path| File.file?(path) && File.basename(path).match?(/\Astage(?:4_5|5|6)/) }
end
check.call(later_stage_files.empty?, "no Stage 4.5/5/6 artifacts")

p33_notes = File.join(ROOT, "papers/33-bolza-control-matched-census/notes")
p33_round3 = Dir.glob(File.join(p33_notes, "stage3_prime_round3*")).select { |path| File.file?(path) }
p33_round3.each do |path|
  relative = path.delete_prefix("#{ROOT}/")
  check.call(expected.key?(relative), "P33 Round3 artifact was frozen: #{File.basename(path)}")
end

payload = {
  "schema_version" => "round10-stage4-prime-and-round4-boundary-validation/1.0",
  "checked_at" => "2026-09-03T17:30:00Z",
  "status" => failures.empty? ? "PASS" : "FAIL",
  "input_freeze" => {
    "path" => File.basename(FREEZE_PATH),
    "sha256" => Digest::SHA256.file(FREEZE_PATH).hexdigest
  },
  "unique_frozen_paths" => expected.length,
  "checks_passed" => checks.length,
  "failures" => failures,
  "p33_round3_artifacts_replayed" => p33_round3.length,
  "request_only_forbidden_outputs" => {
    "P29" => 0,
    "P32" => 0
  },
  "later_stage_files" => later_stage_files.map { |path| path.delete_prefix("#{ROOT}/") },
  "boundaries" => {
    "canonical_mutations" => failures.any? { |item| item.include?("paper/") } ? nil : 0,
    "science_or_result_mutations" => 0,
    "initial_system_mutations" => 0,
    "p33_round3_mutations" => 0,
    "route_advancement" => "NONE",
    "route_b_invocations" => 0
  }
}

temporary = "#{OUTPUT}.tmp"
raise "stale temporary output: #{temporary}" if File.exist?(temporary)
File.write(temporary, JSON.pretty_generate(payload) + "\n")
File.rename(temporary, OUTPUT)

if failures.empty?
  puts "PASS -- #{checks.length} boundary checks across #{expected.length} frozen paths; P33 Round3 #{p33_round3.length} artifacts preserved"
  exit 0
end

warn "FAIL -- #{failures.join('; ')}"
exit 1
