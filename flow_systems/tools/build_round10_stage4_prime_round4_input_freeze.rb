#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUT = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json")

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
  paths.sort.map { |path| artifact(path) }
end

authority_paths = %w[
  BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt
  BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md
  BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md
  BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_AUDIT.json
  BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md
  BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json
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

  review_inputs = case paper_id
                  when "P30", "P31"
                    %W[
                      #{notes}/stage3_prime_round2_verdict_record.json
                      #{notes}/stage3_prime_round2_traceability.json
                      #{notes}/stage3_prime_round2_checker_receipt.json
                      #{notes}/stage4_revision_round1.tex
                      #{notes}/stage4_prime_base.block-manifest.json
                      #{notes}/stage4_claim_surface_manifest.json
                      #{notes}/stage4_response_to_reviewers_round1.json
                      #{notes}/stage4_revision_evidence_bundle.json
                    ]
                  when "P29", "P32"
                    %W[
                      #{notes}/stage3_prime_round3_verdict_record.json
                      #{notes}/stage3_prime_round3_traceability.json
                      #{notes}/stage3_prime_round3_checker_receipt.json
                      #{notes}/stage4_revision_round1.tex
                      #{notes}/stage4_claim_surface_manifest.json
                      #{notes}/stage4_response_to_reviewers_round1.json
                      #{notes}/stage4_revision_evidence_bundle.json
                    ]
                  when "P33"
                    Dir.glob(File.join(ROOT, notes, "stage3_prime_round3*"))
                      .select { |path| File.file?(path) }
                      .map { |path| path.delete_prefix("#{ROOT}/") } + %W[
                        #{notes}/stage4_revision_round1.tex
                        #{notes}/stage4_claim_surface_manifest.json
                        #{notes}/stage4_response_to_reviewers_round1.json
                        #{notes}/stage4_revision_evidence_bundle.json
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
    "track_inputs" => artifacts(review_inputs)
  }
end

payload = {
  "schema_version" => "round10-stage4-prime-and-round4-input-freeze/1.0",
  "generated_at" => "2026-09-03T15:42:00Z",
  "scope" => "P30/P31 exact Stage 4-prime execution; P29/P32 request preparation only; P33 fresh Stage 3-prime Round 4",
  "authority_and_roadmap_bindings" => artifacts(authority_paths),
  "papers" => paper_rows,
  "boundaries" => {
    "canonical_files_frozen" => 15,
    "science_results_frozen" => true,
    "initial_systems_frozen" => 5,
    "route_a_coordinates_frozen" => true,
    "route_b_invocation_authorized" => false,
    "p29_p32_patch_or_apply_authorized" => false,
    "p33_round3_artifacts_frozen" => true,
    "stage4_5_or_later_authorized" => false
  }
}

File.write(OUT, JSON.pretty_generate(payload) + "\n")
puts OUT
