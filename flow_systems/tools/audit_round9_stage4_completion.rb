#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)

PAPERS = {
  24 => {
    dir: "24-bianchi-holonomy-flow", items: 8, resolved: 8, limitations: 0,
    ops: 23, surfaces: 10, delta: 1160, pages: 14,
    manuscript: "e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11",
    pdf: "e8dcfa74b967054a956521daa138a4cb397292c13674c19e1c03e218438759f1"
  },
  25 => {
    dir: "25-three-disk-scattering-flow", items: 6, resolved: 6, limitations: 0,
    ops: 14, surfaces: 6, delta: 666, pages: 13,
    manuscript: "283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb",
    pdf: "2bff30f417741922bb2b28e3208dd08993f0a83a9511421283143ace22177c9e"
  },
  26 => {
    dir: "26-level11-newform-time-change", items: 9, resolved: 8, limitations: 1,
    ops: 25, surfaces: 17, delta: 1731, pages: 15,
    manuscript: "00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe",
    pdf: "b2911495fff88a1e351c4b7cc65989f998df47822b3a2bae0db60b543c34d5aa"
  },
  27 => {
    dir: "27-congruence-inverse-limit-no-go", items: 6, resolved: 6, limitations: 0,
    ops: 15, surfaces: 10, delta: 835, pages: 13,
    manuscript: "c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9",
    pdf: "540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a"
  },
  28 => {
    dir: "28-bolza-magnetic-flow", items: 4, resolved: 4, limitations: 0,
    ops: 4, surfaces: 14, delta: 386, pages: 14,
    manuscript: "864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7",
    pdf: "f78ddd1f8676b24c4937ab94c4ad491b52892fd563c5a27facc77d523ff0c192"
  }
}.freeze

AUTHORIZATION_SHA = "174cf1b035c55f72cdc06f1df6eb5e39138cbc9982ed1fb97457189a964ecd63"

def load_json(path)
  JSON.parse(File.read(path, encoding: "UTF-8"))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

failures = []

authorization = File.join(ROOT, "BATCH_ROUND9_STAGE4_AUTHORIZATION_REQUEST.md")
failures << "authorization SHA mismatch" unless sha256(authorization) == AUTHORIZATION_SHA

totals = {items: 0, ops: 0, surfaces: 0, pages: 0, delta: 0}

PAPERS.each do |number, expected|
  paper = File.join(ROOT, "papers", expected.fetch(:dir))
  notes = File.join(paper, "notes")
  patch = load_json(File.join(notes, "stage4_revision_patch_round1.json"))
  report = load_json(File.join(notes, "stage4_revision_round1.tex.apply-report.json"))
  response = load_json(File.join(notes, "stage4_response_to_reviewers_round1.json"))
  replay = load_json(File.join(notes, "stage4_registered_claim_surface_replay.json"))
  preview = load_json(File.join(notes, "stage4_preview_build_receipt.json"))
  patch_path = File.join(notes, "stage4_revision_patch_round1.json")
  revised_path = File.join(notes, "stage4_revision_round1.tex")
  bundle_path = File.join(notes, "stage4_revision_evidence_bundle.json")
  preview_pdf_path = File.join(notes, "stage4_revision_round1.pdf")

  prefix = "P#{number}"
  summary = response.fetch("summary")
  addressed = %w[resolved limitations unresolvable disagreed].sum { |key| summary.fetch(key, 0) }

  failures << "#{prefix}: item count" unless response.fetch("items").length == expected.fetch(:items)
  failures << "#{prefix}: addressed count" unless addressed == expected.fetch(:items)
  failures << "#{prefix}: resolved count" unless summary.fetch("resolved") == expected.fetch(:resolved)
  failures << "#{prefix}: limitation count" unless summary.fetch("limitations") == expected.fetch(:limitations)
  failures << "#{prefix}: op count" unless patch.fetch("ops").length == expected.fetch(:ops)
  failures << "#{prefix}: applied op count" unless report.fetch("ops_applied").length == expected.fetch(:ops)
  failures << "#{prefix}: structural flag" unless report.dig("structural_flags", "any") == false
  failures << "#{prefix}: structural acknowledgement" unless report.dig("structural_flags", "acknowledged") == false
  failures << "#{prefix}: surface count" unless replay.fetch("registered_surface_count") == expected.fetch(:surfaces)
  failures << "#{prefix}: surface replay" unless replay.fetch("all_byte_exact_once") == true
  failures << "#{prefix}: individual surface replay" unless replay.fetch("surfaces").all? { |row| row.fetch("occurrences_in_revised_draft") == 1 && row.fetch("status") == "BYTE_EXACT_ONCE" }
  failures << "#{prefix}: word delta" unless response.fetch("word_count_delta") == expected.fetch(:delta)
  failures << "#{prefix}: preview status" unless preview.fetch("status") == "PASS"
  failures << "#{prefix}: preview page count" unless preview.fetch("pages") == expected.fetch(:pages)
  failures << "#{prefix}: preview patch binding" unless preview.dig("bindings", "revision_patch_sha256") == sha256(patch_path)
  failures << "#{prefix}: preview draft binding" unless preview.dig("bindings", "revised_anchored_draft_sha256") == sha256(revised_path)
  failures << "#{prefix}: preview bundle binding" unless preview.dig("bindings", "revision_evidence_bundle_sha256") == sha256(bundle_path)
  failures << "#{prefix}: preview PDF binding" unless preview.dig("bindings", "preview_pdf_sha256") == sha256(preview_pdf_path)
  failures << "#{prefix}: preview canonical manuscript boundary" unless preview.dig("write_boundary", "paper_manuscript_modified") == false
  failures << "#{prefix}: preview canonical PDF boundary" unless preview.dig("write_boundary", "paper_pdf_modified") == false
  failures << "#{prefix}: preview canonical-result boundary" unless preview.dig("write_boundary", "canonical_results_refreshed") == false
  failures << "#{prefix}: Stage-5 boundary" unless preview.dig("write_boundary", "stage5_invoked") == false

  %w[undefined_citations undefined_references missing_glyphs fatal_errors overfull_hboxes].each do |field|
    failures << "#{prefix}: preview #{field}" unless preview.fetch(field) == 0
  end

  failures << "#{prefix}: canonical manuscript drift" unless sha256(File.join(paper, "paper", "manuscript.tex")) == expected.fetch(:manuscript)
  failures << "#{prefix}: canonical PDF drift" unless sha256(File.join(paper, "paper", "paper.pdf")) == expected.fetch(:pdf)

  %w[
    stage4_revision_round1.tex
    stage4_revision_evidence_bundle.json
    stage4_unregistered_claim_drift_audit.md
    stage4_route_crosswalk.md
    stage4_completion_report.md
  ].each do |name|
    failures << "#{prefix}: missing #{name}" unless File.file?(File.join(notes, name))
  end

  totals[:items] += expected.fetch(:items)
  totals[:ops] += expected.fetch(:ops)
  totals[:surfaces] += expected.fetch(:surfaces)
  totals[:pages] += expected.fetch(:pages)
  totals[:delta] += expected.fetch(:delta)
end

expected_totals = {items: 33, ops: 81, surfaces: 57, pages: 69, delta: 4778}
failures << "batch totals #{totals.inspect}" unless totals == expected_totals

if failures.empty?
  puts "PASS — Round 9 Stage 4 completion: 33 items; 81 ops; 57 surfaces; 69 clean preview pages; +4,778 words; canonical manuscripts/PDFs unchanged"
  exit 0
end

warn "FAIL — Round 9 Stage 4 completion audit"
failures.each { |failure| warn "  - #{failure}" }
exit 1
