#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
CLONE = Pathname.new("/root/autodl-tmp/round10-stage3-prime-publish").expand_path.freeze
DESTINATION = (CLONE / "flow_systems").freeze
OUTPUT = (ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_SYNC_MANIFEST.json").freeze
EXPECTED_BASE = "27da449ec0039b67598d3c01b38aa381536db211".freeze

RELATIVE_PATHS = %w[
  BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_ESCALATION_INCIDENT.json
  BATCH_ROUND10_P29_P32_STAGE4_PRIME_SCOPE_REQUEST_PREP_INCIDENT_001.json
  BATCH_ROUND10_P29_P32_STAGE4_PRIME_SOURCE_FINALIZATION_SCOPE_CHECKPOINT_RECEIPT.json
  BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json
  BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.md
  BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED_VALIDATION.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.md
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION_VALIDATION.json
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORITY_ATTEMPT1_INCIDENT.md
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORITY_ATTEMPT2_INCIDENT.md
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECORD.md
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHOR_EVENT_20260904.txt
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_EXPANSION_FAIL_CLOSED_INCIDENT_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.md
  BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_PREPARATION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json
  papers/29-bianchi-ideal-owner-refinement/README.md
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_claim_passage_matrix_round3.json
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_001.json
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_002.json
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_p29_p32_source_finalization_round3_incident_003.json
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_source_finalization_round3.json
  papers/29-bianchi-ideal-owner-refinement/notes/stage4_prime_source_finalization_round3_validation.json
  papers/30-three-disk-nonconstant-roof-determinant/README.md
  papers/31-level11-conjugacy-owner-ledger/README.md
  papers/32-homology-cover-renormalization-uniformity/README.md
  papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_claim_passage_matrix_round3.json
  papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_source_finalization_round3.json
  papers/32-homology-cover-renormalization-uniformity/notes/stage4_prime_source_finalization_round3_validation.json
  papers/33-bolza-control-matched-census/README.md
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_artifact_inventory_final.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_artifact_inventory_receipt.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_author_adjudication.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_author_choices.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_claim_surface_manifest.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_revision_roadmap.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_scope_stop_incident.md
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_source_identity_replay_receipt.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_source_use_locator_final.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_source_use_locator_receipt.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_coverage_ledger.schema.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/build_scope_expansion_request.py
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/component_build_provenance.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_coverage_ledger.schema.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixture_oracle_manifest.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/altered_digest.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/duplicate_owner.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/false_reciprocity.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/hash_mismatch.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/incomplete_coverage.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/invalid_termination.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/malformed_schema.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/missing_inverse_link.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/primitive_power_conflict.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/unknown_proof_type.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/unresolved_cutoff.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/invalid/unsupported_negative_decision.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/valid/bp_minimal.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/fixtures/valid/cp_minimal.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/generate_authorized_support.py
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/producer_code_exclusion_audit.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/producer_contract_validation_receipt.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/serialized_fixture_validation_receipt.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/synthetic_proof_registry_snapshot.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/trust_graph.json
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/validate_scope_expansion_request.py
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/validate_support_bundle.py
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/validate_synthetic_fixtures.py
  papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support_validation.json
  tools/audit_round10_p29_p32_source_scope_checkpoint.py
  tools/build_round10_p29_p32_scope_escalation_request.py
  tools/build_round10_p29_p32_source_finalization_round3.py
  tools/build_round10_stage4_prime_correction_execution_authority.rb
  README.md
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_COMPLETION_REPORT.md
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_FINAL_AUDIT.json
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_COMPLETION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_MANDATORY_CHECKPOINT.md
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_PROVENANCE_TIMESTAMP_CORRECTION.json
  tools/finalize_round10_stage4_prime_scope_reissue.rb
  tools/resign_round10_stage4_prime_scope_reissue_provenance.rb
  tools/fix_round10_p30_p31_human_request_binding.rb
  tools/build_round10_stage4_prime_scope_reissue_sync_manifest.rb
].freeze

def require!(condition, message)
  raise "ROUND10_SCOPE_REISSUE_SYNC_MANIFEST_FAIL: #{message}" unless condition
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
require!(ROOT.directory? && DESTINATION.directory?, "source root or publish destination missing")
require!(git_output("status", "--short").empty?, "publish clone is not clean")

head = git_output("rev-parse", "HEAD")
origin_main = git_output("rev-parse", "origin/main")
require!(head == EXPECTED_BASE, "unexpected HEAD #{head}")
require!(origin_main == EXPECTED_BASE, "unexpected origin/main #{origin_main}")

require!(RELATIVE_PATHS.length == 90, "expected 90 explicit paths, found #{RELATIVE_PATHS.length}")
require!(RELATIVE_PATHS.uniq.length == RELATIVE_PATHS.length, "duplicate explicit path")
require!(RELATIVE_PATHS.none? { |p| p.start_with?("/") || p.include?("..") }, "non-relative or traversing path")
require!(RELATIVE_PATHS.none? { |p| p.include?("__pycache__") || p.end_with?(".pyc") || p.include?("private") }, "cache/private path selected")

paths = RELATIVE_PATHS.map { |relative| ROOT / relative }
missing = paths.reject(&:file?).map { |p| p.relative_path_from(ROOT).to_s }
require!(missing.empty?, "missing allowlisted paths: #{missing.join(', ')}")
require!(paths.none?(&:symlink?), "symlink selected")

unchanged = paths.filter_map do |source|
  relative = source.relative_path_from(ROOT)
  destination = DESTINATION / relative
  relative.to_s if destination.file? && sha256(source) == sha256(destination)
end
require!(unchanged.empty?, "allowlist includes unchanged paths: #{unchanged.join(', ')}")

terminal_audit = JSON.parse((ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_FINAL_AUDIT.json").read)
require!(terminal_audit["status"] == "PASS_SCOPE_REISSUE_READY_AWAITING_EXPLICIT_CONFIRMATION", "terminal audit is not PASS")
require!(terminal_audit["checks_passed"] == 83 && terminal_audit["checks_failed"] == 0, "terminal audit count mismatch")

files = paths.map { |p| binding(p) }
path_set_text = RELATIVE_PATHS.sort.join("\n") + "\n"
extensions = RELATIVE_PATHS.group_by { |p| File.extname(p).empty? ? "none" : File.extname(p) }.transform_values(&:length)
categories = {
  "root_artifacts_and_readme" => RELATIVE_PATHS.count { |p| !p.include?("/") },
  "paper_29" => RELATIVE_PATHS.count { |p| p.start_with?("papers/29-") },
  "paper_30" => RELATIVE_PATHS.count { |p| p.start_with?("papers/30-") },
  "paper_31" => RELATIVE_PATHS.count { |p| p.start_with?("papers/31-") },
  "paper_32" => RELATIVE_PATHS.count { |p| p.start_with?("papers/32-") },
  "paper_33" => RELATIVE_PATHS.count { |p| p.start_with?("papers/33-") },
  "workflow_tools" => RELATIVE_PATHS.count { |p| p.start_with?("tools/") }
}
require!(categories.values.sum == RELATIVE_PATHS.length, "category count mismatch")

manifest = {
  "schema_version" => "round10-stage4-prime-correction-scope-reissue-sync-manifest/1.0",
  "generated_at_utc" => Time.now.utc.iso8601,
  "workflow_date" => "2026-09-04",
  "status" => "READY_FOR_EXACT_ALLOWLIST_SSH_SYNC",
  "source_root" => ROOT.to_s,
  "destination" => {
    "repository" => "git@github.com:maris205/hilbert-polya-structure.git",
    "subdirectory" => "flow_systems/",
    "publish_clone" => CLONE.to_s,
    "pre_sync_head" => head,
    "pre_sync_origin_main" => origin_main
  },
  "selection" => {
    "files_in_manifest" => files.length,
    "manifest_self_is_out_of_band_and_must_also_be_synced" => true,
    "total_files_to_sync_including_manifest" => files.length + 1,
    "all_manifest_files_differ_from_publish_base" => true,
    "explicit_allowlist_only" => true,
    "deletions_requested" => 0,
    "symlinks_selected" => 0,
    "private_or_cache_files_selected" => 0,
    "path_set_sha256" => Digest::SHA256.hexdigest(path_set_text)
  },
  "category_counts" => categories,
  "extension_counts" => extensions,
  "files" => files,
  "boundaries" => {
    "canonical_manuscript_bibliography_or_pdf_selected" => 0,
    "scientific_code_experiment_or_result_output_selected" => 0,
    "initial_system_or_route_crosswalk_selected" => 0,
    "manuscript_patch_successor_draft_or_build_output_selected" => 0,
    "root_readme_selected" => 1,
    "per_paper_readmes_selected" => 5,
    "p33_synthetic_conformance_support_selected" => true,
    "p33_noncontrolling_superseded_authority_chain_selected_as_provenance_only" => true,
    "publication_is_exact_hash_bound_and_additive" => true
  }
}

OUTPUT.write(JSON.pretty_generate(manifest) + "\n")
puts JSON.pretty_generate(
  "status" => manifest.fetch("status"),
  "files_in_manifest" => files.length,
  "total_files_including_manifest" => files.length + 1,
  "path_set_sha256" => manifest.dig("selection", "path_set_sha256"),
  "manifest_sha256" => sha256(OUTPUT)
)
