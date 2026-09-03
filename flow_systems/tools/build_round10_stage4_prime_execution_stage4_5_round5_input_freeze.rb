#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUT = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json")

PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

def artifact(relative)
  absolute = File.join(ROOT, relative)
  raise "missing input: #{relative}" unless File.file?(absolute)

  {
    "path" => relative,
    "sha256" => Digest::SHA256.file(absolute).hexdigest,
    "bytes" => File.size(absolute)
  }
end

def artifacts(paths)
  paths.uniq.sort.map { |path| artifact(path) }
end

authority_paths = %w[
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHOR_EVENT_20260904.txt
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECORD.md
  BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md
  BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md
  BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_FINAL_AUDIT.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json
  skills/route-a-evaluator.md
  skills/route-b-evaluator.md
]

paper_rows = PAPERS.map do |paper_id, slug|
  base = "papers/#{slug}"
  notes = "#{base}/notes"
  science_paths = %w[code experiments results].flat_map do |directory|
    Dir.glob(File.join(ROOT, base, directory, "**", "*"), File::FNM_DOTMATCH)
      .select { |path| File.file?(path) }
      .map { |path| path.delete_prefix("#{ROOT}/") }
  end

  track_inputs = case paper_id
                 when "P29", "P32"
                   %W[
                     #{notes}/stage3_prime_round3_input_manifest.json
                     #{notes}/stage3_prime_round3_precommitment.json
                     #{notes}/stage3_prime_round3_verdict_record.json
                     #{notes}/stage3_prime_round3_traceability.json
                     #{notes}/stage3_prime_round3_checker_receipt.json
                     #{notes}/stage4_revision_round1.tex
                     #{notes}/stage4_prime_base.block-manifest.json
                     #{notes}/stage4_claim_surface_manifest.json
                     #{notes}/stage4_response_to_reviewers_round1.json
                     #{notes}/stage4_revision_evidence_bundle.json
                     #{base}/paper/references.bib
                   ]
                 when "P30", "P31"
                   Dir.glob(File.join(ROOT, notes, "stage4_prime_*"))
                     .select { |path| File.file?(path) }
                     .map { |path| path.delete_prefix("#{ROOT}/") } + %W[
                       #{notes}/stage2_5_integrity_report.json
                       #{notes}/stage2_5_material_passport.json
                       #{notes}/stage4_revision_round1.tex
                       #{notes}/stage4_revision_evidence_bundle.json
                     ]
                 when "P33"
                   Dir.glob(File.join(ROOT, notes, "stage3_prime_round4_*"))
                     .select { |path| File.file?(path) }
                     .map { |path| path.delete_prefix("#{ROOT}/") } + %W[
                       #{notes}/stage3_revision_roadmap.json
                       #{notes}/stage4_author_adjudication.json
                       #{notes}/stage4_revision_evidence_bundle.json
                       #{notes}/stage4_revision_round1.tex
                       #{notes}/stage4_response_to_reviewers_round1.json
                       #{notes}/stage3_review_package.json
                       #{notes}/stage3_review_panel_provenance.json
                     ]
                 end

  {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "canonical_files" => artifacts(%W[
      #{base}/paper/manuscript.tex
      #{base}/paper/references.bib
      #{base}/paper/paper.pdf
    ]),
    "science_files" => artifacts(science_paths),
    "initial_system_source" => artifact("#{notes}/stage1_prestart_brief.md"),
    "route_crosswalk" => artifact("#{notes}/stage4_route_crosswalk.md"),
    "track_inputs" => artifacts(track_inputs)
  }
end

payload = {
  "schema_version" => "round10-stage4-prime-execution-stage4-5-round5-input-freeze/1.0",
  "generated_at" => "2026-09-03T17:48:06Z",
  "workflow_date" => "2026-09-04",
  "scope" => "P29/P32 exact Stage 4-prime execution; P30/P31 fresh Stage 4.5 audit-only; P33 fresh Stage 3-prime Round 5",
  "authority_and_roadmap_bindings" => artifacts(authority_paths),
  "papers" => paper_rows,
  "boundaries" => {
    "canonical_files_frozen" => 15,
    "science_results_frozen" => true,
    "initial_systems_frozen" => 5,
    "route_a_coordinates_frozen" => true,
    "route_a_credit_authorized" => false,
    "route_b_invocation_authorized" => false,
    "p29_p32_exact_stage4_prime_authorized" => true,
    "p30_p31_stage4_5_audit_only_authorized" => true,
    "p33_stage3_prime_round5_authorized" => true,
    "p33_round4_artifacts_frozen" => true,
    "stage5_or_later_authorized" => false
  }
}

File.write(OUT, JSON.pretty_generate(payload) + "\n")
puts OUT
