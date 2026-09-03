#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"

ROOT = File.expand_path("..", __dir__)
DATE = "2026-09-03"
PAPERS = {
  "29" => {
    dir: "29-bianchi-ideal-owner-refinement",
    patch: "da28a98143fd09b0a91fae2195ef713cd0ffcb4f277ed831c9163511ff0bb3ca",
    reason: "Superseded after clean compilation exposed long-token overfull boxes and final-response fresh-block provenance required refresh."
  },
  "30" => {
    dir: "30-three-disk-nonconstant-roof-determinant",
    patch: "bb67926c5f6dc1b7fed71d00c62ff874be67498be5fe4fa469ce45279b350d33",
    reason: "Superseded after build layout diagnostics and bounded semantic review found two RESOLVED contracts underspecified."
  },
  "31" => {
    dir: "31-level11-conjugacy-owner-ledger",
    patch: "2bbfc03621101193f10381a7692c92b2500329b78df126dd0884a01cdb1af237",
    reason: "Superseded after bounded semantic review found an X versus X_res materialization type inconsistency and build layout diagnostics."
  },
  "32" => {
    dir: "32-homology-cover-renormalization-uniformity",
    patch: "cf398eaec0528f42e42fd5acc939616ba4bf19c0e36c0e39aaacca655b20ac94",
    reason: "Superseded after marker-stripped preview failed closed on a math superscript outside math mode."
  },
  "33" => {
    dir: "33-bolza-control-matched-census",
    patch: "0a81a835dc081d98457751741541a1147aa796da45c1e18a2028530973dcd6ea",
    reason: "Superseded after bounded semantic review found one incorrect upstream digest, one dropped prospective hedge, two overstated roadmap dispositions, one schema key-order inconsistency, and build layout diagnostics."
  }
}.freeze

WRITER_FILES = %w[
  stage4_revision_patch_round1.json
  stage4_response_to_reviewers_provisional.json
  stage4_revision_patch_round1_writer_receipt.md
].freeze

GENERATED_FILES = %w[
  stage4_revision_round1.tex
  stage4_revision_round1.tex.apply-report.json
  stage4_revision_round1.tex.block-manifest.json
  stage4_response_to_reviewers_round1.json
  stage4_response_to_reviewers_round1.md
  stage4_registered_claim_surface_replay.json
  stage4_revision_evidence_bundle.json
  stage4_bundle_validation_receipt.json
  stage4_token_conservation_round1.json
  stage4_revision_log_round1.md
  stage4_unregistered_claim_drift_review_packet.json
  stage4_revision_round1.pdf
  stage4_revision_round1.build.log
  stage4_preview_build_receipt.json
  stage4_preview_build_transcript.log
].freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

requested = ARGV.empty? ? PAPERS.keys : ARGV
unknown = requested - PAPERS.keys
abort("unknown paper numbers: #{unknown.join(', ')}") unless unknown.empty?

requested.each do |number|
  config = PAPERS.fetch(number)
  notes = File.join(ROOT, "papers", config.fetch(:dir), "notes")
  patch_path = File.join(notes, "stage4_revision_patch_round1.json")
  abort("P#{number}: writer patch changed before archive; inspect manually") unless sha256(patch_path) == config.fetch(:patch)
  destination = File.join(notes, "stage4_attempt1_superseded_20260903")
  abort("P#{number}: archive destination already exists") if File.exist?(destination)
  FileUtils.mkdir_p(destination)

  copied = []
  (WRITER_FILES + GENERATED_FILES).uniq.each do |name|
    source = File.join(notes, name)
    next unless File.file?(source)
    target = File.join(destination, name)
    FileUtils.cp(source, target, preserve: true)
    copied << {"path" => name, "sha256" => sha256(target), "bytes" => File.size(target)}
  end
  manifest = {
    "schema" => "round10-stage4-superseded-attempt/1.0",
    "paper_number" => number.to_i,
    "date" => DATE,
    "status" => "SUPERSEDED_FAIL_CLOSED_NOT_CANONICAL",
    "reason" => config.fetch(:reason),
    "superseded_patch_sha256" => config.fetch(:patch),
    "files" => copied,
    "boundaries" => {
      "canonical_manuscript_modified" => false,
      "canonical_bibliography_modified" => false,
      "canonical_pdf_modified" => false,
      "canonical_results_refreshed" => false,
      "route_state_changed" => false
    }
  }
  manifest_path = File.join(destination, "ATTEMPT_MANIFEST.json")
  File.binwrite(manifest_path, JSON.pretty_generate(manifest) + "\n")

  # Only generated, fully archived attempt outputs are cleared. Writer sidecars
  # remain in place for a writer-only repair against the immutable Stage-3 base.
  GENERATED_FILES.each do |name|
    path = File.join(notes, name)
    FileUtils.rm_f(path) if File.file?(path)
  end
  puts "P#{number}: archived #{copied.length} files; manifest #{sha256(manifest_path)}; generated attempt outputs cleared"
end
