#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
DATE = "2026-09-03"
STAMP = "2026-09-03T09:10:00Z"
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

def assert!(condition, message)
  raise message unless condition
end

def digest(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def canonical(value)
  case value
  when Hash
    "{" + value.keys.sort.map { |key| "#{JSON.generate(key)}:#{canonical(value.fetch(key))}" }.join(",") + "}"
  when Array
    "[" + value.map { |child| canonical(child) }.join(",") + "]"
  else
    JSON.generate(value)
  end
end

def jcs_sha256(value)
  Digest::SHA256.hexdigest(canonical(value).encode("UTF-8"))
end

def artifact(notes, filename, version)
  path = File.join(notes, filename)
  assert!(File.file?(path), "missing #{path}")
  {
    "present" => true,
    "path_or_passport_ref" => "path:notes/#{filename}",
    "sha256" => digest(path),
    "version_label" => version,
    "origin_date" => DATE
  }
end

def array_artifact(notes, filename, version)
  entry = artifact(notes, filename, version)
  entry.delete("present")
  {"present" => true, "items" => [entry]}
end

def relative(path)
  path.delete_prefix("#{ROOT}/")
end

def frozen_file(path)
  assert!(File.file?(path), "missing frozen file #{path}")
  {"path" => relative(path), "sha256" => digest(path), "bytes" => File.size(path)}
end

author_event = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_AUTHOR_EVENT_20260903.txt")
authorization = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_AUTHORIZATION_RECORD.md")

receipt = {
  "schema_version" => "round10-stage3-prime-round2-input-manifests/1.0",
  "generated_at" => STAMP,
  "authorization" => {
    "author_event" => frozen_file(author_event),
    "authorization_record" => frozen_file(authorization)
  },
  "contract_version" => "1.1",
  "cross_model_active" => false,
  "papers" => []
}

freeze = {
  "schema_version" => "round10-stage3-prime-round2-input-freeze/1.0",
  "generated_at" => STAMP,
  "scope" => "P29-P33 Stage 3 prime Round 2 review-side additions only",
  "round1_terminal_bindings" => %w[
    BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json
    BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md
    BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json
    BATCH_ROUND10_STAGE3_PRIME_MANDATORY_CHECKPOINT.md
    BATCH_ROUND10_STAGE3_PRIME_FINAL_AUDIT.json
  ].map { |name| frozen_file(File.join(ROOT, name)) },
  "route_evaluator_bindings" => %w[
    skills/route-a-evaluator.md
    skills/route-b-evaluator.md
  ].map { |name| frozen_file(File.join(ROOT, name)) },
  "papers" => []
}

PAPERS.each do |paper_id, slug|
  paper = File.join(ROOT, "papers", slug)
  notes = File.join(paper, "notes")
  roadmap_path = File.join(notes, "stage3_revision_roadmap.json")
  author_path = File.join(notes, "stage4_author_adjudication.json")
  bundle_path = File.join(notes, "stage4_revision_evidence_bundle.json")
  patch_path = File.join(notes, "stage4_revision_patch_round1.json")
  apply_path = File.join(notes, "stage4_revision_round1.tex.apply-report.json")
  base_path = File.join(notes, "stage3_revision_base.tex")
  revised_path = File.join(notes, "stage4_revision_round1.tex")

  roadmap = load_json(roadmap_path)
  author = load_json(author_path)
  bundle = load_json(bundle_path)
  apply_report = load_json(apply_path)

  assert!(roadmap.fetch("schema_version") == "revision-roadmap/1.0", "#{paper_id}: roadmap schema")
  assert!(author.fetch("schema_version") == "author-adjudication/1.0", "#{paper_id}: author schema")
  assert!(bundle.fetch("schema_version") == "revision-evidence-bundle/1.0", "#{paper_id}: bundle schema")
  assert!(apply_report.fetch("report_format_version") == "1.3", "#{paper_id}: apply-report schema")
  assert!(author.fetch("adjudication_status") == "complete", "#{paper_id}: incomplete author adjudication")
  assert!(author.fetch("roadmap_sha256") == digest(roadmap_path), "#{paper_id}: author/roadmap binding")
  assert!(author.fetch("base_draft_sha256") == digest(base_path), "#{paper_id}: author/base binding")
  assert!(bundle.dig("chain_start", "draft", "sha256") == digest(base_path), "#{paper_id}: bundle/base binding")
  assert!(bundle.dig("final_draft", "sha256") == digest(revised_path), "#{paper_id}: bundle/revised binding")
  assert!(bundle.dig("rounds", 0, "revision_roadmap", "sha256") == digest(roadmap_path), "#{paper_id}: bundle/roadmap binding")
  assert!(bundle.dig("rounds", 0, "author_adjudication", "sha256") == digest(author_path), "#{paper_id}: bundle/author binding")
  assert!(bundle.dig("rounds", 0, "revision_patch", "sha256") == digest(patch_path), "#{paper_id}: bundle/patch binding")
  assert!(bundle.dig("rounds", 0, "apply_report", "sha256") == digest(apply_path), "#{paper_id}: bundle/apply binding")
  assert!(apply_report.fetch("patch_digest") == digest(patch_path), "#{paper_id}: apply/patch binding")
  assert!(roadmap.fetch("items").length == author.fetch("author_adjudications").length, "#{paper_id}: item-count binding")

  round_id = "#{paper_id.downcase}-stage3-prime-round2-2026-09-03"
  manifest = {
    "contract_version" => "1.1",
    "round_id" => round_id,
    "cross_model_active" => false,
    "artifacts" => {
      "original_manuscript" => artifact(notes, "stage3_revision_base.tex", "round10-stage3-prime-input-v1"),
      "revised_manuscript" => artifact(notes, "stage4_revision_round1.tex", "round10-stage4-round1"),
      "revision_roadmap" => artifact(notes, "stage3_revision_roadmap.json", "revision-roadmap/1.0"),
      "author_adjudication" => artifact(notes, "stage4_author_adjudication.json", "author-adjudication/1.0"),
      "revision_evidence_bundle" => artifact(notes, "stage4_revision_evidence_bundle.json", "revision-evidence-bundle/1.0"),
      "editorial_decision_letter" => artifact(notes, "stage3_editorial_synthesis.md", "round10-stage3-editorial-synthesis"),
      "response_to_reviewers" => artifact(notes, "stage4_response_to_reviewers_round1.json", "round10-stage4-round1"),
      "revision_patches" => array_artifact(notes, "stage4_revision_patch_round1.json", "revision-patch/1.1"),
      "apply_reports" => array_artifact(notes, "stage4_revision_round1.tex.apply-report.json", "apply-report/1.3"),
      "round1_findings" => artifact(notes, "stage3_review_package.json", nil),
      "round1_config_cards" => artifact(notes, "stage3_phase0_field_analysis.md", "round10-stage3-frozen-cards")
    }
  }

  output = File.join(notes, "stage3_prime_round2_input_manifest.json")
  File.write(output, JSON.pretty_generate(manifest) + "\n")

  round1_files = Dir[File.join(notes, "stage3_prime_round1_*")].sort.map { |path| frozen_file(path) }
  canonical_files = %w[paper/manuscript.tex paper/references.bib paper/paper.pdf].map { |name| frozen_file(File.join(paper, name)) }
  science_files = %w[code experiments results].flat_map do |dir|
    Dir.glob(File.join(paper, dir, "**", "*"), File::FNM_DOTMATCH)
       .select { |path| File.file?(path) }
       .sort
       .map { |path| frozen_file(path) }
  end
  review_evidence_files = Dir[File.join(notes, "stage4_*")].flat_map do |path|
    File.directory?(path) ? Dir[File.join(path, "**", "*")] : [path]
  end.select { |path| File.file?(path) }.uniq.sort.map { |path| frozen_file(path) }
  freeze["papers"] << {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "round1_artifacts" => round1_files,
    "canonical_files" => canonical_files,
    "science_files" => science_files,
    "review_evidence_files" => review_evidence_files,
    "initial_system_source" => frozen_file(File.join(paper, "notes", "stage1_prestart_brief.md")),
    "route_crosswalk" => frozen_file(File.join(paper, "notes", "stage4_route_crosswalk.md"))
  }

  receipt["papers"] << {
    "paper_id" => paper_id,
    "round_id" => round_id,
    "manifest_path" => relative(output),
    "manifest_sha256" => digest(output),
    "manifest_jcs_sha256" => jcs_sha256(manifest),
    "roadmap_items" => roadmap.fetch("items").length,
    "required_artifacts_present" => true,
    "apply_chain_witness_expected" => "pass",
    "phase1_revision_content_exposed" => false
  }
end

freeze_path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_INPUT_FREEZE.json")
File.write(freeze_path, JSON.pretty_generate(freeze) + "\n")
receipt["input_freeze"] = frozen_file(freeze_path)
receipt_path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_INPUT_MANIFEST_RECEIPT.json")
File.write(receipt_path, JSON.pretty_generate(receipt) + "\n")

puts "PASS — emitted #{PAPERS.length} Round-2 manifests and froze Round-1/canonical boundaries"
