#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
TIMESTAMP = "2026-09-03T21:40:49Z"
WORKFLOW_DATE = "2026-09-04"

EVENT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHOR_EVENT_20260904.txt"
RECORD = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECORD.md"
RECEIPT = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_AUTHORIZATION_RECEIPT.json"
FREEZE = ROOT / "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_EXECUTION_INPUT_FREEZE.json"

CHECKPOINT = "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_MANDATORY_CHECKPOINT.md"
REQUESTS = {
  "P29_P32" => "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32.json",
  "P30_P31" => "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json",
  "P33" => "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33.json"
}.freeze
EXPECTED = {
  CHECKPOINT => "d2f1a0c2bf98910948c2131f503bd36c479e9f565f4151231a77a6c819132bf3",
  REQUESTS.fetch("P29_P32") => "2b8a1c5d57cc01589ca6c926dc5590be0cbe58cae187a0b70d0b4c6c9a6bf3b3",
  REQUESTS.fetch("P30_P31") => "0c44b40fb5cdea77ccc277dd85b2b713d14f7e5d2d18de4636e7b09e046b3a9c",
  REQUESTS.fetch("P33") => "ff160416cd8316326d2ef15b806f41479e63e299e0523899dbe93dc2e0da1650"
}.freeze
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

def require!(condition, message)
  raise "ROUND10_CORRECTION_EXECUTION_AUTHORITY_FAIL: #{message}" unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def binding(path)
  {
    "path" => path.relative_path_from(ROOT).to_s,
    "sha256" => sha(path),
    "bytes" => path.size
  }
end

def write_json(path, object)
  File.binwrite(path, JSON.pretty_generate(object) + "\n")
end

def nested_bindings(value, rows = [])
  case value
  when Hash
    if value["path"].is_a?(String) && value["sha256"].is_a?(String)
      candidate = ROOT / value["path"]
      rows << binding(candidate) if candidate.file?
    end
    value.each_value { |child| nested_bindings(child, rows) }
  when Array
    value.each { |child| nested_bindings(child, rows) }
  end
  rows
end

require!(EVENT.file?, "author event missing")
require!(EVENT.binread == "确认，下一轮\n".b, "author event bytes differ")
[RECORD, RECEIPT, FREEZE].each { |path| require!(!path.exist?, "refusing to overwrite #{path}") }

EXPECTED.each do |relative, expected|
  path = ROOT / relative
  require!(path.file?, "missing authority input #{relative}")
  require!(sha(path) == expected, "authority hash mismatch #{relative}")
end

requests = REQUESTS.transform_values { |relative| JSON.parse((ROOT / relative).read) }
require!(requests.fetch("P29_P32").fetch("papers").sum { |p| p.fetch("block_operation_pairs") } == 36,
         "P29/P32 pair count mismatch")
require!(requests.fetch("P30_P31").fetch("papers").sum { |p| p.fetch("block_operation_pairs") } == 34,
         "P30/P31 pair count mismatch")
p33 = requests.fetch("P33")
p33_targets = p33.fetch("papers").first.fetch("items").flat_map { |item| item.fetch("proposed_targets") }
require!(p33_targets.length == 39, "P33 mapped pair count mismatch")
require!(p33_targets.map { |target| target.fetch("block_id") }.uniq.length == 35,
         "P33 unique pair count mismatch")
require!(p33.fetch("supporting_operations").length == 7, "P33 support operation count mismatch")

request_input_bindings = REQUESTS.values.flat_map do |relative|
  nested_bindings(JSON.parse((ROOT / relative).read))
end

paper_rows = PAPERS.map do |paper_id, slug|
  paper_root = ROOT / "papers" / slug
  current_draft = if paper_id == "P33"
    paper_root / "notes/stage4_revision_round1.tex"
  else
    paper_root / "notes/stage4_prime_revision_round2.tex"
  end
  current_bib = if paper_id == "P33"
    paper_root / "paper/references.bib"
  else
    paper_root / "notes/stage4_prime_references_round2.bib"
  end
  block_manifest = if paper_id == "P33"
    paper_root / "notes/stage4_prime_round5_base.block-manifest.json"
  else
    paper_root / "notes/stage4_prime_base.block-manifest.json"
  end
  science = %w[code experiments results].flat_map do |directory|
    (paper_root / directory).glob("**/*").select(&:file?).reject(&:symlink?)
  end.sort_by(&:to_s)
  {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "current_working_draft" => binding(current_draft),
    "current_working_bibliography" => binding(current_bib),
    "available_block_manifest" => binding(block_manifest),
    "canonical_files" => %w[paper/manuscript.tex paper/references.bib paper/paper.pdf].map { |r| binding(paper_root / r) },
    "science_files" => science.map { |path| binding(path) },
    "initial_system_source" => binding(paper_root / "notes/stage1_prestart_brief.md"),
    "route_crosswalk" => binding(paper_root / "notes/stage4_route_crosswalk.md")
  }
end

root_bindings = [
  CHECKPOINT,
  "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_COMPLETION_REPORT.md",
  "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_COMPLETION_RECEIPT.json",
  "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_FINAL_AUDIT.json",
  "BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_INPUT_FREEZE.json",
  *REQUESTS.values,
  "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json",
  "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_VALIDATION.json"
].map { |relative| binding(ROOT / relative) }

unique_request_inputs = request_input_bindings.each_with_object({}) do |row, out|
  out[row.fetch("path")] ||= row
end.values.sort_by { |row| row.fetch("path") }

freeze = {
  "schema_version" => "round10-stage4-prime-correction-execution-input-freeze/1.0",
  "generated_at_utc" => TIMESTAMP,
  "workflow_date" => WORKFLOW_DATE,
  "status" => "FROZEN_FOR_EXACT_AUTHORIZED_EXECUTION",
  "scope" => {
    "papers" => PAPERS.keys,
    "revision_stage" => "Stage 4-prime exact correction execution",
    "authorized_unique_replace_block_pairs" => 105,
    "authorized_p33_support_operations" => 7,
    "authorized_p30_p31_matrix_regenerations" => 2
  },
  "root_authority_bindings" => root_bindings,
  "request_referenced_existing_artifacts" => unique_request_inputs,
  "papers" => paper_rows,
  "route_evaluators" => %w[skills/route-a-evaluator.md skills/route-b-evaluator.md].map { |r| binding(ROOT / r) },
  "boundaries" => {
    "canonical_manuscript_or_pdf_promotion_authorized" => false,
    "p29_p32_p30_p31_bibliography_mutation_authorized" => false,
    "p33_bibliography_append_authorized_only_for" => ["P33-S03-CORR", "P33-S16-CORR"],
    "scientific_producer_census_or_result_refresh_authorized" => false,
    "route_or_initial_system_mutation_authorized" => false,
    "fresh_stage4_5_or_re_review_authorized" => false,
    "stage5_or_stage6_authorized" => false,
    "citation_style" => "plainnat numeric"
  }
}
write_json(FREEZE, freeze)

record = <<~MD
  # Round 10 Papers 29--33 — exact Stage 4′ correction-execution authorization

  - Workflow date: `#{WORKFLOW_DATE} UTC`
  - Confirmation observed at: `#{TIMESTAMP}`
  - Exact author instruction: `确认，下一轮`
  - Author event: `#{EVENT.basename}`, SHA-256 `#{sha(EVENT)}`
  - Controlling checkpoint: `#{CHECKPOINT}`, SHA-256 `#{EXPECTED.fetch(CHECKPOINT)}`

  ## Authorized tracks

  1. P29/P32: execute request `#{REQUESTS.fetch("P29_P32")}` at SHA-256 `#{EXPECTED.fetch(REQUESTS.fetch("P29_P32"))}`; 36 exact `replace_block` pairs plus its named source-finalization, provenance, response, validation, and isolated-build artifacts.
  2. P30/P31: execute request `#{REQUESTS.fetch("P30_P31")}` at SHA-256 `#{EXPECTED.fetch(REQUESTS.fetch("P30_P31"))}`; 34 exact `replace_block` pairs plus exactly two named passage-matrix regenerations and isolated builds.
  3. P33: execute request `#{REQUESTS.fetch("P33")}` at SHA-256 `#{EXPECTED.fetch(REQUESTS.fetch("P33"))}`; 39 item-target mappings over 35 unique `replace_block` pairs plus the seven named support operations.

  Author triage is `will_address` in `source_traceability` order. The confirmation authorizes this exact execution package only. It does not authorize target expansion, registered-claim strengthening, collateral edits, fresh Stage 4.5 or re-review, canonical promotion, scientific producer/census execution, result refresh, Route advancement, Route B, initial-system changes, Stage 5/6, or a citation-style change.

  P33 bibliography authority is limited to appending exactly `P33-S03-CORR` and `P33-S16-CORR`; no existing entry may be overwritten. Synthetic fixture execution is conformance-only and may not be represented as a scientific experiment or census result.

  Any old-hash mismatch, unsupported locator that cannot be safely narrowed within its listed block, missing component/provenance fact, scientific-value change, registered-claim change, out-of-scope target, apply failure, build failure, or validation failure stops fail-closed.
MD
File.binwrite(RECORD, record)

receipt = {
  "schema_version" => "round10-stage4-prime-correction-execution-authorization-receipt/1.0",
  "recorded_at_utc" => TIMESTAMP,
  "workflow_date" => WORKFLOW_DATE,
  "status" => "AUTHORIZED_WITH_EXACT_BOUNDARIES",
  "author_event" => binding(EVENT).merge("exact_text" => "确认，下一轮\n"),
  "authorization_record" => binding(RECORD),
  "input_freeze" => binding(FREEZE),
  "controlling_checkpoint" => binding(ROOT / CHECKPOINT),
  "tracks" => [
    {"track_id" => "P29_P32", "request" => binding(ROOT / REQUESTS.fetch("P29_P32")), "replace_block_pairs" => 36},
    {"track_id" => "P30_P31", "request" => binding(ROOT / REQUESTS.fetch("P30_P31")), "replace_block_pairs" => 34, "matrix_regenerations" => 2},
    {"track_id" => "P33", "request" => binding(ROOT / REQUESTS.fetch("P33")), "item_target_mappings" => 39, "unique_replace_block_pairs" => 35, "supporting_operations" => 7}
  ],
  "aggregate" => {
    "papers" => 5,
    "unique_replace_block_pairs" => 105,
    "p33_supporting_operations" => 7,
    "p30_p31_matrix_regenerations" => 2
  },
  "boundaries" => freeze.fetch("boundaries")
}
write_json(RECEIPT, receipt)

puts "authorization record: #{sha(RECORD)}"
puts "input freeze: #{sha(FREEZE)}"
puts "authorization receipt: #{sha(RECEIPT)}"
puts "request-referenced existing artifacts: #{unique_request_inputs.length}"
