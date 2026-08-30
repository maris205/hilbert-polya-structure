#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

def abort_with(message)
  warn("ERROR: #{message}")
  exit(2)
end

paper_root = Pathname.new(ARGV.fetch(0) do
  abort_with("usage: build_stage4_claim_surface_manifest.rb PAPER_ROOT [OUTPUT]")
end).expand_path

passport_path = paper_root.join("notes/stage2_5_material_passport.json")
base_path = paper_root.join("notes/stage3_revision_base.tex")
roadmap_path = paper_root.join("notes/stage3_revision_roadmap.json")
output_path = if ARGV[1]
                Pathname.new(ARGV[1]).expand_path
              else
                paper_root.join("notes/stage4_claim_surface_manifest.json")
              end

[passport_path, base_path, roadmap_path].each do |path|
  abort_with("missing required input: #{path}") unless path.file?
end

passport_raw = passport_path.binread
base_raw = base_path.binread
roadmap_raw = roadmap_path.binread
passport = JSON.parse(passport_raw)
roadmap = JSON.parse(roadmap_raw)

manifests = passport.fetch("claim_intent_manifests", [])
abort_with("material passport has no claim_intent_manifests") if manifests.empty?

block_markers = []
base_raw.to_enum(:scan, /<!--block:(B[0-9]{4,})-->/).each do
  match = Regexp.last_match
  block_markers << { "start" => match.begin(0), "id" => match[1] }
end
abort_with("anchored base contains no block markers") if block_markers.empty?

claim_intent_dir = paper_root.join("notes/stage4_revision_authority/claim_intents")
claim_intent_dir.mkpath
manifest_artifacts = {}
manifests.each do |manifest|
  manifest_id = manifest.fetch("manifest_id")
  safe_id = manifest_id.gsub(/[^A-Za-z0-9._-]+/, "_")
  artifact_path = claim_intent_dir.join("#{safe_id}.json")
  artifact_path.binwrite(JSON.pretty_generate(manifest) + "\n")
  manifest_artifacts[manifest_id] = {
    "path" => artifact_path.relative_path_from(paper_root).to_s,
    "sha256" => Digest::SHA256.file(artifact_path).hexdigest
  }
end

candidates = []
manifests.each do |manifest|
  manifest_id = manifest.fetch("manifest_id")
  manifest.fetch("claims", []).each do |claim|
    text = claim.fetch("claim_text").encode(Encoding::UTF_8).b
    offsets = []
    cursor = 0
    while (offset = base_raw.index(text, cursor))
      offsets << offset
      cursor = offset + 1
    end
    abort_with("#{manifest_id}/#{claim.fetch('claim_id')} occurs #{offsets.length} times in anchored base") unless offsets.length == 1

    start_byte = offsets.first
    end_byte = start_byte + text.bytesize
    marker_index = block_markers.rindex { |marker| marker.fetch("start") < start_byte }
    abort_with("claim begins before first block: #{manifest_id}/#{claim.fetch('claim_id')}") unless marker_index
    block = block_markers.fetch(marker_index)
    next_marker = block_markers[marker_index + 1]
    if next_marker && end_byte > next_marker.fetch("start")
      abort_with("claim crosses block boundary: #{manifest_id}/#{claim.fetch('claim_id')}")
    end

    candidates << {
      "manifest_id" => manifest_id,
      "claim_id" => claim.fetch("claim_id"),
      "evidence_kind" => claim.fetch("intended_evidence_kind", "unspecified"),
      "block_id" => block.fetch("id"),
      "start" => start_byte,
      "end" => end_byte,
      "text" => text
    }
  end
end

# Claim Intent may contain nested formulations of the same claim. The current
# claim-surface contract rejects overlapping UTF-8 spans, so register the
# longest exact surface in every overlap component. Shorter nested claims stay
# explicitly unregistered and remain part of the mandatory E6 semantic audit.
selected = []
excluded = []
candidates.sort_by { |row| [-(row.fetch("end") - row.fetch("start")), row.fetch("start"), row.fetch("claim_id")] }.each do |row|
  overlap = selected.any? do |kept|
    row.fetch("start") < kept.fetch("end") && kept.fetch("start") < row.fetch("end")
  end
  (overlap ? excluded : selected) << row
end
selected.sort_by! { |row| [row.fetch("start"), row.fetch("claim_id")] }

paper_number = paper_root.basename.to_s[/\A([0-9]+)/, 1] || "X"
surfaces = selected.map do |row|
  original_text = row.fetch("text").dup.force_encoding(Encoding::UTF_8)
  evidence_kind = row.fetch("evidence_kind").to_s.gsub(/[^A-Za-z0-9._-]+/, "_")
  {
    "surface_id" => "CLAIM-SURFACE-P#{paper_number}-#{row.fetch('claim_id')}",
    "scoped_manifest_id" => row.fetch("manifest_id"),
    "claim_id" => row.fetch("claim_id"),
    "block_id" => row.fetch("block_id"),
    "utf8_start" => row.fetch("start"),
    "utf8_end" => row.fetch("end"),
    "original_text" => original_text,
    "original_text_sha256" => Digest::SHA256.hexdigest(row.fetch("text")),
    "intent_claim_text_sha256" => Digest::SHA256.hexdigest(row.fetch("text")),
    "current_rung" => "registered_#{evidence_kind}_claim_exactly_preserved"
  }
end

claim_intent_sources = manifests.map do |manifest|
  {
    "scoped_manifest_id" => manifest.fetch("manifest_id"),
    "artifact" => manifest_artifacts.fetch(manifest.fetch("manifest_id"))
  }
end

output = {
  "schema_version" => "claim-surface-manifest/1.0",
  "revision_round" => roadmap.fetch("revision_round"),
  "roadmap_sha256" => Digest::SHA256.hexdigest(roadmap_raw),
  "base_draft_sha256" => Digest::SHA256.hexdigest(base_raw),
  "claim_intent_sources" => claim_intent_sources,
  "surfaces" => surfaces
}

output_path.dirname.mkpath
output_path.binwrite(JSON.pretty_generate(output) + "\n")

puts JSON.generate(
  "paper_root" => paper_root.to_s,
  "output" => output_path.to_s,
  "source_claims" => candidates.length,
  "registered_surfaces" => selected.length,
  "nested_overlap_exclusions" => excluded.map { |row| row.fetch("claim_id") },
  "passport_sha256" => Digest::SHA256.hexdigest(passport_raw),
  "claim_intent_artifacts" => manifest_artifacts.values,
  "sha256" => Digest::SHA256.file(output_path).hexdigest
)
