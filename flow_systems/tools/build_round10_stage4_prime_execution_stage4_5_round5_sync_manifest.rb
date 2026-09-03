#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path
OUTPUT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_SYNC_MANIFEST.json"
PREFIX = "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_"

def require!(condition, message)
  raise "ROUND10_SYNC_MANIFEST_FAIL: #{message}" unless condition
end

def binding(path)
  {
    "path" => path.relative_path_from(ROOT).to_s,
    "sha256" => Digest::SHA256.file(path).hexdigest,
    "bytes" => path.size
  }
end

require!(!OUTPUT.exist?, "refusing to overwrite #{OUTPUT}")

paths = []
paths << ROOT / "README.md"
paths.concat(ROOT.glob("#{PREFIX}*"))

{
  "29-bianchi-ideal-owner-refinement" => "stage4_prime_*",
  "30-three-disk-nonconstant-roof-determinant" => "stage4_5_round1_*",
  "31-level11-conjugacy-owner-ledger" => "stage4_5_round1_*",
  "32-homology-cover-renormalization-uniformity" => "stage4_prime_*",
  "33-bolza-control-matched-census" => "stage3_prime_round5_*"
}.each do |slug, pattern|
  paper = ROOT / "papers" / slug
  paths << paper / "README.md"
  paths << paper / "notes/pipeline_state.md"
  paths.concat((paper / "notes").glob("**/#{pattern}"))
  if slug.start_with?("29-") || slug.start_with?("32-")
    paths.concat((paper / "notes").glob("stage4_prime_layout_superseded*/**/*"))
  end
end

%w[
  tools/audit_p33_stage3_prime_round5_phase1.py
  tools/audit_p33_stage3_prime_round5_phase2a.py
  tools/build_p33_stage3_prime_round5_inputs.rb
  tools/build_round10_stage4_prime_execution_stage4_5_round5_input_freeze.rb
  tools/build_round10_stage4_prime_execution_stage4_5_round5_sync_manifest.rb
  tools/build_round10_stage4_prime_p29_p32_authority.rb
  tools/finalize_p33_stage3_prime_round5.py
  tools/finalize_round10_stage4_prime_execution_stage4_5_round5.rb
  tools/finalize_round10_stage4_prime_p29_p32.rb
  tools/p33_stage3_prime_round5_verdict_emitter.py
].each { |name| paths << ROOT / name }

paths = paths.select(&:file?).reject(&:symlink?).reject do |path|
  path.to_s.include?("__pycache__") || path.extname == ".pyc" || path.basename.to_s.include?("private")
end.uniq.sort_by { |path| path.relative_path_from(ROOT).to_s }
require!(paths.none? { |path| path.basename.to_s.include?("private") }, "private path selected")
require!(paths.none? { |path| path.to_s.include?("__pycache__") || path.extname == ".pyc" }, "cache path selected")
require!(paths.none? { |path| path.to_s.include?("/.git/") }, "nested git path selected")
require!(paths.length >= 250, "unexpectedly small manifest: #{paths.length}")

manifest = {
  "schema_version" => "round10-stage4-prime-execution-stage4-5-round5-sync-manifest/1.0",
  "generated_at" => Time.now.utc.iso8601,
  "workflow_date" => "2026-09-04",
  "source_root" => ROOT.to_s,
  "destination" => {
    "repository" => "git@github.com:maris205/hilbert-polya-structure.git",
    "subdirectory" => "flow_systems/",
    "pre_sync_remote_main" => "d29a829b4acac29ff8429724467409e9820a8fa2"
  },
  "selection" => {
    "files" => paths.length,
    "manifest_self_is_out_of_band" => true,
    "excluded_private_payload" => ".p33_stage3_prime_round5_phase2a_payload.private.json",
    "excluded_root_build_junk" => "stage4_prime_revision_round2.log",
    "excluded_cache_patterns" => ["__pycache__/", "*.pyc"],
    "unrelated_legacy_and_nested_git_content_selected" => false
  },
  "files" => paths.map { |path| binding(path) },
  "boundaries" => {
    "canonical_paper_files_selected" => 0,
    "science_or_result_files_selected" => 0,
    "initial_system_sources_selected" => 0,
    "route_evaluator_or_crosswalk_files_selected" => 0,
    "status_readmes_selected" => 6,
    "pipeline_state_files_selected" => 5,
    "publication_is_explicit_allowlist_only" => true
  }
}

File.binwrite(OUTPUT, JSON.pretty_generate(manifest) + "\n")
puts "sync manifest: #{paths.length} files; #{Digest::SHA256.file(OUTPUT).hexdigest}"
