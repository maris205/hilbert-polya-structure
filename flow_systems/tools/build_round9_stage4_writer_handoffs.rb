#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path

PAPERS = {
  24 => "24-bianchi-holonomy-flow",
  25 => "25-three-disk-scattering-flow",
  26 => "26-level11-newform-time-change",
  27 => "27-congruence-inverse-limit-no-go",
  28 => "28-bolza-magnetic-flow"
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def canonicalize(value)
  case value
  when Hash
    value.keys.sort.to_h { |key| [key, canonicalize(value.fetch(key))] }
  when Array
    value.map { |child| canonicalize(child) }
  else
    value
  end
end

def canonical_sha256(value)
  Digest::SHA256.hexdigest(JSON.generate(canonicalize(value)))
end

PAPERS.each do |paper_number, slug|
  paper_root = ROOT / "papers" / slug
  notes = paper_root / "notes"
  base = notes / "stage3_revision_base.tex"
  manifest_path = notes / "stage3_revision_base.block-manifest.json"
  roadmap_path = notes / "stage3_revision_roadmap.json"
  claims_path = notes / "stage4_claim_surface_manifest.json"
  adjudication_path = notes / "stage4_author_adjudication.json"
  output_path = notes / "stage4_writer_handoff.json"
  abort "refusing to overwrite: #{output_path}" if output_path.exist?

  manifest = JSON.parse(manifest_path.read)
  roadmap = JSON.parse(roadmap_path.read)
  claims = JSON.parse(claims_path.read)
  adjudication = JSON.parse(adjudication_path.read)

  target_ids = roadmap.fetch("items").flat_map do |item|
    item.fetch("proposed_targets").map { |target| target.fetch("block_id") }
  end.uniq
  block_hashes = manifest.fetch("blocks").to_h do |block|
    [block.fetch("block_id"), block.fetch("old_hash")]
  end
  missing = target_ids.reject { |block_id| block_hashes.key?(block_id) }
  abort "manifest missing targets for P#{paper_number}: #{missing.join(', ')}" unless missing.empty?

  decision_projection = {
    "author_events" => adjudication.fetch("author_events"),
    "display_order" => adjudication.fetch("display_order"),
    "author_adjudications" => adjudication.fetch("author_adjudications"),
    "collateral_authorizations" => adjudication.fetch("collateral_authorizations")
  }

  handoff = {
    "handoff_type" => "round9-stage4-writer-bindings/1.0",
    "paper_number" => paper_number,
    "revision_round" => roadmap.fetch("revision_round"),
    "base_draft_path" => "notes/stage3_revision_base.tex",
    "base_draft_hash" => manifest.fetch("base_draft_hash"),
    "base_draft_sha256" => sha256(base),
    "block_manifest_path" => "notes/stage3_revision_base.block-manifest.json",
    "block_manifest_sha256" => sha256(manifest_path),
    "roadmap_path" => "notes/stage3_revision_roadmap.json",
    "roadmap_sha256" => sha256(roadmap_path),
    "author_adjudication_path" => "notes/stage4_author_adjudication.json",
    "author_adjudication_sha256" => sha256(adjudication_path),
    "author_decision_digest" => canonical_sha256(decision_projection),
    "claim_surface_manifest_path" => "notes/stage4_claim_surface_manifest.json",
    "claim_surface_manifest_sha256" => sha256(claims_path),
    "registered_claim_surface_count" => claims.fetch("surfaces").length,
    "unregistered_claim_drift_review_required" => true,
    "authorization_request_sha256" => sha256(ROOT / "BATCH_ROUND9_STAGE4_AUTHORIZATION_REQUEST.md"),
    "author_event_path" => "../../BATCH_ROUND9_STAGE4_AUTHOR_EVENT_20260830.txt",
    "author_event_sha256" => sha256(ROOT / "BATCH_ROUND9_STAGE4_AUTHOR_EVENT_20260830.txt"),
    "target_old_hashes" => target_ids.sort.to_h { |block_id| [block_id, block_hashes.fetch(block_id)] }
  }

  output_path.write(JSON.pretty_generate(handoff) + "\n")
  puts "P#{paper_number}: #{target_ids.length} target hashes -> #{output_path.relative_path_from(ROOT)}"
  puts "  author_decision_digest=#{handoff.fetch('author_decision_digest')}"
end
