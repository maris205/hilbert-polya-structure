#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUT = File.join(
  ROOT,
  "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_INPUT_FREEZE.json"
)

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
  raise "symlink input: #{relative}" if File.symlink?(absolute)

  {
    "path" => relative,
    "sha256" => Digest::SHA256.file(absolute).hexdigest,
    "bytes" => File.size(absolute)
  }
end

def artifacts(paths)
  paths.uniq.sort.map { |path| artifact(path) }
end

def top_level_note_glob(notes, prefixes)
  prefixes.flat_map do |prefix|
    Dir.glob(File.join(ROOT, notes, "#{prefix}*"))
      .select { |path| File.file?(path) && !File.symlink?(path) }
      .map { |path| path.delete_prefix("#{ROOT}/") }
  end
end

authority_paths = %w[
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_MANDATORY_CHECKPOINT.md
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_COMPLETION_REPORT.md
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_COMPLETION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_FINAL_AUDIT.json
  BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_AUTHOR_EVENT_20260904.txt
  BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_AUTHORIZATION_RECORD.md
  BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_AUTHORIZATION_RECEIPT.json
  skills/route-a-evaluator.md
  skills/route-b-evaluator.md
]

paper_rows = PAPERS.map do |paper_id, slug|
  base = "papers/#{slug}"
  notes = "#{base}/notes"

  science_paths = %w[code experiments results].flat_map do |directory|
    Dir.glob(File.join(ROOT, base, directory, "**", "*"), File::FNM_DOTMATCH)
      .select { |path| File.file?(path) && !File.symlink?(path) }
      .map { |path| path.delete_prefix("#{ROOT}/") }
  end

  prefixes = case paper_id
             when "P29", "P32"
               %w[stage2_5_ stage3_prime_round3_ stage4_]
             when "P30", "P31"
               %w[stage2_5_ stage4_prime_ stage4_5_round1_]
             when "P33"
               %w[stage2_5_ stage3_prime_round5_ stage4_]
             end

  dedicated_paths = %W[
    #{notes}/stage1_prestart_brief.md
    #{notes}/stage4_route_crosswalk.md
  ]

  track_inputs = (top_level_note_glob(notes, prefixes) - dedicated_paths) + %W[
    #{base}/README.md
    #{notes}/pipeline_state.md
  ]

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
  "schema_version" => "round10-stage4.5-and-stage4-prime-request-prep-input-freeze/1.0",
  "generated_at_utc" => "2026-09-03T20:03:19Z",
  "workflow_date" => "2026-09-04",
  "scope" => {
    "P29" => "fresh Stage 4.5 Mode-2 audit-only",
    "P30" => "bounded source-finalization and exact Stage-4-prime correction-request preparation",
    "P31" => "bounded source-finalization and exact Stage-4-prime correction-request preparation",
    "P32" => "fresh Stage 4.5 Mode-2 audit-only",
    "P33" => "read-only source/inventory analysis and exact Stage-4-prime request preparation"
  },
  "authority_and_roadmap_bindings" => artifacts(authority_paths),
  "papers" => paper_rows,
  "boundaries" => {
    "canonical_files_frozen" => 15,
    "science_and_results_frozen" => true,
    "initial_systems_frozen" => 5,
    "route_evaluators_frozen" => 2,
    "route_crosswalks_frozen" => 5,
    "route_a_credit_authorized" => false,
    "route_b_invocation_authorized" => false,
    "p29_p32_audit_only" => true,
    "p30_p31_patch_application_authorized" => false,
    "p30_p31_stage4_5_rerun_authorized" => false,
    "p33_patch_or_scientific_execution_authorized" => false,
    "stage5_or_stage6_authorized" => false,
    "citation_style" => "plainnat numeric"
  }
}

File.write(OUT, JSON.pretty_generate(payload) + "\n")
puts OUT
