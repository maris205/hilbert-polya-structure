#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path
CLONE = Pathname.new("/root/autodl-tmp/round10-stage3-prime-publish").expand_path
DESTINATION = CLONE / "flow_systems"
OUTPUT = ROOT / "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_SYNC_MANIFEST.json"
EXPECTED_BASE = "9f71f27b544884325120ce63a6cffbe1becb39c3"

def require!(condition, message)
  raise "ROUND10_REQUEST_PREP_SYNC_MANIFEST_FAIL: #{message}" unless condition
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def binding(path)
  {
    "path" => path.relative_path_from(ROOT).to_s,
    "sha256" => sha256(path),
    "bytes" => path.size
  }
end

def git_output(*args)
  stdout, stderr, status = Open3.capture3("git", "-C", CLONE.to_s, *args)
  require!(status.success?, "git #{args.join(' ')} failed: #{stderr.strip}")
  stdout.strip
end

require!(!OUTPUT.exist?, "refusing to overwrite #{OUTPUT}")
require!(ROOT.directory?, "source root missing")
require!(DESTINATION.directory?, "publish destination missing")
require!(git_output("status", "--short").empty?, "publish clone is not clean")

local_head = git_output("rev-parse", "HEAD")
local_origin_main = git_output("rev-parse", "origin/main")
require!(local_head == EXPECTED_BASE, "unexpected publish-clone HEAD #{local_head}")
require!(local_origin_main == EXPECTED_BASE, "unexpected local origin/main #{local_origin_main}")

paths = []
paths << ROOT / "README.md"
paths.concat(ROOT.glob("BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_*"))
paths.concat(ROOT.glob("BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32*"))
paths.concat(ROOT.glob("BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P30_P31*"))
paths.concat(ROOT.glob("BATCH_ROUND10_STAGE4_5_EXECUTION_INCIDENT_*"))
paths.concat(ROOT.glob("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33*"))

%w[
  29-bianchi-ideal-owner-refinement
  32-homology-cover-renormalization-uniformity
].each do |slug|
  paper = ROOT / "papers" / slug
  paths << paper / "README.md"
  paths.concat((paper / "notes").glob("stage4_5_round1_*"))
end

%w[
  30-three-disk-nonconstant-roof-determinant
  31-level11-conjugacy-owner-ledger
].each do |slug|
  paper = ROOT / "papers" / slug
  paths << paper / "README.md"
  paths.concat((paper / "notes").glob("stage4_5_round1_source_finalization_proposal.*"))
  paths << paper / "notes/stage4_5_round1_stage4_prime_correction_authorization_proposal.json"
end

p33 = ROOT / "papers/33-bolza-control-matched-census"
paths << p33 / "README.md"
paths.concat((p33 / "notes").glob("stage4_prime_round5_*"))

%w[
  tools/build_round10_p29_p32_stage45_correction_request.py
  tools/build_round10_p29_p32_stage4_5_audits.py
  tools/build_round10_stage4_5_and_stage4_prime_request_prep_input_freeze.rb
  tools/build_round10_stage4_5_and_stage4_prime_request_prep_sync_manifest.rb
].each { |relative| paths << ROOT / relative }

paths = paths.select(&:file?).reject(&:symlink?).reject do |path|
  path == OUTPUT || path.to_s.include?("__pycache__") || path.extname == ".pyc" ||
    path.basename.to_s.include?("private")
end.uniq.sort_by { |path| path.relative_path_from(ROOT).to_s }

require!(paths.length == 112, "expected 112 allowlisted files, found #{paths.length}")
require!(paths.none? { |path| path.to_s.include?("/.git/") }, "nested git path selected")
require!(paths.none? { |path| path.basename.to_s.include?("private") }, "private path selected")

unchanged = paths.filter_map do |path|
  relative = path.relative_path_from(ROOT)
  destination = DESTINATION / relative
  relative.to_s if destination.file? && sha256(path) == sha256(destination)
end
require!(unchanged.empty?, "allowlist includes files unchanged from publish base: #{unchanged.join(', ')}")

files = paths.map { |path| binding(path) }
manifest = {
  "schema_version" => "round10-stage4-5-and-stage4-prime-request-prep-sync-manifest/1.0",
  "generated_at_utc" => Time.now.utc.iso8601,
  "workflow_date" => "2026-09-04",
  "status" => "READY_FOR_EXPLICIT_ALLOWLIST_SYNC",
  "source_root" => ROOT.to_s,
  "destination" => {
    "repository" => "git@github.com:maris205/hilbert-polya-structure.git",
    "subdirectory" => "flow_systems/",
    "publish_clone" => CLONE.to_s,
    "pre_sync_local_head" => local_head,
    "pre_sync_local_origin_main" => local_origin_main,
    "verified_remote_main_before_manifest" => EXPECTED_BASE
  },
  "selection" => {
    "files_in_manifest" => files.length,
    "manifest_self_is_out_of_band_and_must_also_be_synced" => true,
    "all_manifest_files_differ_from_publish_base" => true,
    "explicit_allowlist_only" => true,
    "deletions_requested" => 0,
    "symlinks_selected" => 0,
    "excluded_cache_patterns" => ["__pycache__/", "*.pyc"],
    "private_payloads_selected" => 0,
    "unrelated_legacy_or_nested_git_content_selected" => false
  },
  "category_counts" => {
    "root_checkpoint_request_and_audit_artifacts" => 25,
    "paper_29_status_and_stage4_5_artifacts" => 34,
    "paper_30_status_and_source_finalization_artifacts" => 4,
    "paper_31_status_and_source_finalization_artifacts" => 4,
    "paper_32_status_and_stage4_5_artifacts" => 34,
    "paper_33_status_and_stage4_prime_request_sidecars" => 7,
    "workflow_builders" => 4
  },
  "files" => files,
  "boundaries" => {
    "canonical_paper_files_selected" => 0,
    "manuscript_or_bibliography_files_selected" => 0,
    "science_or_canonical_result_files_selected" => 0,
    "initial_system_sources_selected" => 0,
    "route_evaluator_or_route_crosswalk_files_selected" => 0,
    "registered_claim_surface_files_selected" => 0,
    "root_readme_selected" => 1,
    "per_paper_status_readmes_selected" => 5,
    "stage4_5_preview_pdfs_selected" => 2,
    "publication_is_exact_hash_bound_and_additive" => true
  }
}

require!(manifest["category_counts"].values.sum == paths.length,
         "category counts do not sum to selected file count")

File.binwrite(OUTPUT, JSON.pretty_generate(manifest) + "\n")
puts "sync manifest: #{paths.length} files"
puts "manifest sha256: #{sha256(OUTPUT)}"
