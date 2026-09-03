#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
DATE = "2026-09-03"

PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

def digest(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.read(path, encoding: "UTF-8"))
end

def assert!(condition, message)
  raise message unless condition
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

receipt = {
  "schema_version" => "round10-stage3-prime-input-manifests/1.0",
  "generated_at" => "2026-09-03T05:00:00Z",
  "cross_model_active" => false,
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
  apply = load_json(apply_path)

  assert!(roadmap.fetch("schema_version") == "revision-roadmap/1.0", "#{paper_id}: roadmap schema")
  assert!(author.fetch("schema_version") == "author-adjudication/1.0", "#{paper_id}: author schema")
  assert!(bundle.fetch("schema_version") == "revision-evidence-bundle/1.0", "#{paper_id}: bundle schema")
  assert!(apply.fetch("report_format_version") == "1.3", "#{paper_id}: apply-report schema")
  assert!(author.fetch("adjudication_status") == "complete", "#{paper_id}: incomplete author adjudication")
  assert!(author.fetch("roadmap_sha256") == digest(roadmap_path), "#{paper_id}: author/roadmap binding")
  assert!(author.fetch("base_draft_sha256") == digest(base_path), "#{paper_id}: author/base binding")
  assert!(bundle.dig("chain_start", "draft", "sha256") == digest(base_path), "#{paper_id}: bundle/base binding")
  assert!(bundle.dig("final_draft", "sha256") == digest(revised_path), "#{paper_id}: bundle/revised binding")
  assert!(bundle.dig("rounds", 0, "revision_roadmap", "sha256") == digest(roadmap_path), "#{paper_id}: bundle/roadmap binding")
  assert!(bundle.dig("rounds", 0, "author_adjudication", "sha256") == digest(author_path), "#{paper_id}: bundle/author binding")
  assert!(bundle.dig("rounds", 0, "revision_patch", "sha256") == digest(patch_path), "#{paper_id}: bundle/patch binding")
  assert!(bundle.dig("rounds", 0, "apply_report", "sha256") == digest(apply_path), "#{paper_id}: bundle/apply binding")
  assert!(apply.fetch("patch_digest") == digest(patch_path), "#{paper_id}: apply/patch binding")
  assert!(roadmap.fetch("items").length == author.fetch("author_adjudications").length, "#{paper_id}: item-count binding")

  round_id = "#{paper_id.downcase}-stage3-prime-round1-2026-09-03"
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

  output = File.join(notes, "stage3_prime_round1_input_manifest.json")
  File.write(output, JSON.pretty_generate(manifest) + "\n")
  receipt["papers"] << {
    "paper_id" => paper_id,
    "round_id" => round_id,
    "manifest_path" => output.delete_prefix("#{ROOT}/"),
    "manifest_sha256" => digest(output),
    "roadmap_items" => roadmap.fetch("items").length,
    "required_artifacts_present" => true,
    "apply_chain_witness_expected" => "pass"
  }
end

receipt_path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_INPUT_MANIFEST_RECEIPT.json")
File.write(receipt_path, JSON.pretty_generate(receipt) + "\n")
puts "PASS — emitted #{PAPERS.length} current-contract Stage 3′ input manifests"
