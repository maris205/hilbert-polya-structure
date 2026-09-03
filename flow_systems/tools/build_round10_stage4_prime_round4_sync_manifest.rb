#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = File.expand_path("..", __dir__)
PUBLISH = "/root/autodl-tmp/round10-stage3-prime-publish/flow_systems"
OUTPUT = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_SYNC_MANIFEST.json"

paper_slugs = %w[
  29-bianchi-ideal-owner-refinement
  30-three-disk-nonconstant-roof-determinant
  31-level11-conjugacy-owner-ledger
  32-homology-cover-renormalization-uniformity
  33-bolza-control-matched-census
]

status_files = ["README.md"] + paper_slugs.flat_map do |slug|
  [
    "papers/#{slug}/README.md",
    "papers/#{slug}/notes/pipeline_state.md",
    "papers/#{slug}/paper/README.md"
  ]
end

batch_files = Dir.glob(File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME*"), File::FNM_DOTMATCH)
  .select { |path| File.file?(path) }
  .map { |path| Pathname(path).relative_path_from(Pathname(ROOT)).to_s }
  .reject { |path| path == OUTPUT }

paper_files = []
paper_files.concat(%w[
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_base.block-manifest.json
  papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_base.block-manifest.json
])
%w[30-three-disk-nonconstant-roof-determinant 31-level11-conjugacy-owner-ledger].each do |slug|
  paper_files.concat(
    Dir.glob(File.join(ROOT, "papers", slug, "notes", "stage4_prime_*"), File::FNM_DOTMATCH)
      .flat_map { |path| File.directory?(path) ? Dir.glob(File.join(path, "**", "*"), File::FNM_DOTMATCH) : [path] }
      .select { |path| File.file?(path) }
      .map { |path| Pathname(path).relative_path_from(Pathname(ROOT)).to_s }
  )
end
paper_files.concat(
  Dir.glob(File.join(ROOT, "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_*"), File::FNM_DOTMATCH)
    .select { |path| File.file?(path) }
    .map { |path| Pathname(path).relative_path_from(Pathname(ROOT)).to_s }
)

tool_files = %w[
  tools/audit_p33_stage3_prime_round4_phase1.rb
  tools/audit_round10_stage4_prime_authorization_request_p29_p32.rb
  tools/audit_round10_stage4_prime_p30_p31.rb
  tools/audit_round10_stage4_prime_round4_boundaries.rb
  tools/audit_round10_stage4_prime_round4_final.rb
  tools/build_p33_stage3_prime_round4_inputs.rb
  tools/build_round10_stage4_prime_authorization_request_p29_p32.rb
  tools/build_round10_stage4_prime_p30_p31.rb
  tools/build_round10_stage4_prime_round4_input_freeze.rb
  tools/build_round10_stage4_prime_round4_sync_manifest.rb
  tools/build_round10_stage4_prime_round4_terminal_artifacts.rb
  tools/finalize_p33_stage3_prime_round4_abort.rb
  tools/finalize_round10_stage4_prime_p30_p31.rb
  tools/replay_round10_stage4_prime_literature.rb
  tools/update_round10_stage4_prime_round4_status_docs.rb
]

candidates = (batch_files + status_files + paper_files + tool_files).uniq.sort
raise "unsafe candidate path" if candidates.any? { |path| Pathname(path).absolute? || path.split("/").include?("..") }
missing = candidates.reject { |path| File.file?(File.join(ROOT, path)) }
raise "missing candidate files: #{missing.join(', ')}" unless missing.empty?

changed = candidates.select do |path|
  source = File.join(ROOT, path)
  target = File.join(PUBLISH, path)
  !File.file?(target) || Digest::SHA256.file(source).hexdigest != Digest::SHA256.file(target).hexdigest
end

records = changed.map do |path|
  source = File.join(ROOT, path)
  {
    "path" => path,
    "sha256" => Digest::SHA256.file(source).hexdigest,
    "bytes" => File.size(source),
    "publish_state_before_sync" => File.file?(File.join(PUBLISH, path)) ? "MODIFIED" : "NEW"
  }
end

manifest = {
  "schema_version" => "round10-stage4-prime-and-round4-sync-manifest/1.0",
  "generated_date_utc" => "2026-09-04",
  "source_root" => ROOT,
  "publish_clone_root" => PUBLISH,
  "copy_policy" => "EXPLICIT_FILE_LIST_ONLY_NO_DELETE",
  "payload_file_count" => records.length,
  "payload_files" => records,
  "manifest_self" => {
    "path" => OUTPUT,
    "excluded_from_payload_to_avoid_self_hash_cycle" => true,
    "must_be_copied_and_committed_with_payload" => true
  },
  "scope_guards" => {
    "canonical_manuscript_bibliography_pdf_files_in_payload" => records.count { |row| row.fetch("path").match?(%r{/paper/(?:manuscript\.tex|references\.bib|paper\.pdf)$}) },
    "science_code_experiment_result_files_in_payload" => records.count { |row| row.fetch("path").match?(%r{/code/|/experiments/|/results/}) },
    "route_definition_files_in_payload" => records.count { |row| row.fetch("path").start_with?("skills/route-") },
    "unrelated_full-tree_differences_intentionally_excluded" => true,
    "excluded_examples" => ["root scratch/build files", ".ipynb_checkpoints", "__pycache__", "legacy logs/PDF caches", "unrelated older tools"]
  }
}

raise "canonical payload violation" unless manifest.dig("scope_guards", "canonical_manuscript_bibliography_pdf_files_in_payload").zero?
raise "science payload violation" unless manifest.dig("scope_guards", "science_code_experiment_result_files_in_payload").zero?
raise "Route payload violation" unless manifest.dig("scope_guards", "route_definition_files_in_payload").zero?

File.binwrite(File.join(ROOT, OUTPUT), "#{JSON.pretty_generate(manifest)}\n")
puts "payload_files=#{records.length} manifest=#{OUTPUT} sha256=#{Digest::SHA256.file(File.join(ROOT, OUTPUT)).hexdigest}"
