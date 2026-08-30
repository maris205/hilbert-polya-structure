#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
PAPERS = {
  "24" => "24-bianchi-holonomy-flow",
  "25" => "25-three-disk-scattering-flow",
  "26" => "26-level11-newform-time-change",
  "27" => "27-congruence-inverse-limit-no-go",
  "28" => "28-bolza-magnetic-flow"
}.freeze

def load_json(path)
  JSON.parse(File.binread(path))
rescue JSON::ParserError => e
  raise "invalid JSON at #{path}: #{e.message}"
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def assert(condition, message)
  raise message unless condition
end

def audit_paper(number, directory)
  paper_root = File.join(ROOT, "papers", directory)
  notes = File.join(paper_root, "notes")
  handoff_path = File.join(notes, "stage4_writer_handoff.json")
  adjudication_path = File.join(notes, "stage4_author_adjudication.json")
  claims_path = File.join(notes, "stage4_claim_surface_manifest.json")
  manifest_path = File.join(notes, "stage3_revision_base.block-manifest.json")
  roadmap_path = File.join(notes, "stage3_revision_roadmap.json")
  base_path = File.join(notes, "stage3_revision_base.tex")
  patch_path = File.join(notes, "stage4_revision_patch_round1.json")

  [handoff_path, adjudication_path, claims_path, manifest_path, roadmap_path,
   base_path, patch_path].each { |path| assert(File.file?(path), "P#{number}: missing #{path}") }

  handoff = load_json(handoff_path)
  adjudication = load_json(adjudication_path)
  claims = load_json(claims_path)
  manifest = load_json(manifest_path)
  patch = load_json(patch_path)
  base_text = File.binread(base_path).force_encoding("UTF-8")
  base_blocks = base_text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m).to_h

  assert(sha256(base_path) == handoff.fetch("base_draft_sha256"), "P#{number}: base SHA drift")
  assert(sha256(manifest_path) == handoff.fetch("block_manifest_sha256"), "P#{number}: block-manifest SHA drift")
  assert(sha256(roadmap_path) == handoff.fetch("roadmap_sha256"), "P#{number}: roadmap SHA drift")
  assert(sha256(adjudication_path) == handoff.fetch("author_adjudication_sha256"), "P#{number}: adjudication SHA drift")
  assert(sha256(claims_path) == handoff.fetch("claim_surface_manifest_sha256"), "P#{number}: claim-surface SHA drift")

  assert(patch.fetch("patch_format_version") == "1.1", "P#{number}: patch format is not 1.1")
  assert(patch.fetch("authorization_context") == "review_roadmap", "P#{number}: wrong authorization context")
  assert(patch.fetch("revision_round") == 1, "P#{number}: wrong revision round")
  assert(patch.fetch("base_draft_hash") == handoff.fetch("base_draft_hash"), "P#{number}: base hash mismatch")
  assert(patch.fetch("roadmap_sha256") == handoff.fetch("roadmap_sha256"), "P#{number}: roadmap binding mismatch")
  assert(patch.fetch("author_adjudication_sha256") == handoff.fetch("author_adjudication_sha256"), "P#{number}: adjudication binding mismatch")
  assert(patch.fetch("author_decision_digest") == handoff.fetch("author_decision_digest"), "P#{number}: decision digest mismatch")
  assert(patch.fetch("claim_surface_manifest_sha256") == handoff.fetch("claim_surface_manifest_sha256"), "P#{number}: claim binding mismatch")
  assert(patch.fetch("emitted_by") == "draft_writer_agent", "P#{number}: emitter role mismatch")

  blocks = manifest.fetch("blocks").to_h { |row| [row.fetch("block_id"), row] }
  decisions = adjudication.fetch("author_adjudications").to_h { |row| [row.fetch("item_id"), row] }
  surfaces_by_block = claims.fetch("surfaces").group_by { |surface| surface.fetch("block_id") }
  seen_blocks = {}
  covered_items = []

  patch.fetch("ops").each_with_index do |op, index|
    block_id = op.fetch("block_id")
    operation = op.fetch("op")
    label = "P#{number} op #{index} #{block_id}/#{operation}"
    assert(!seen_blocks.key?(block_id), "#{label}: block already has op #{seen_blocks[block_id]}")
    seen_blocks[block_id] = index
    assert(blocks.key?(block_id), "#{label}: unknown block")
    assert(op.fetch("old_hash") == blocks.fetch(block_id).fetch("old_hash"), "#{label}: old hash mismatch")
    assert(op.fetch("claim_strength_changes") == [], "#{label}: claim-strength change is not authorized")
    assert(op.fetch("collateral_authorization_ids") == [], "#{label}: collateral authorization is not authorized")

    item_ids = op.fetch("roadmap_item_ids")
    assert(item_ids.is_a?(Array) && !item_ids.empty?, "#{label}: no roadmap item")
    item_ids.each do |item_id|
      decision = decisions[item_id]
      assert(decision, "#{label}: unknown roadmap item #{item_id}")
      assert(decision.fetch("author_triage") == "will_address", "#{label}: #{item_id} not will_address")
      allowed = decision.fetch("authorized_targets").any? do |target|
        target.fetch("block_id") == block_id && target.fetch("allowed_operations").include?(operation)
      end
      assert(allowed, "#{label}: #{item_id} does not authorize this target/operation")
      covered_items << item_id
    end

    if %w[replace_block insert_before insert_after].include?(operation)
      new_text = op.fetch("new_text")
      assert(new_text.is_a?(String) && !new_text.empty?, "#{label}: missing new text")
      heading_pattern = /\\(?:sub)*section\*?\s*\{[^}]*\}/
      new_headings = new_text.scan(heading_pattern)
      old_headings = base_blocks.fetch(block_id).scan(heading_pattern)
      if operation == "replace_block"
        assert(new_headings == old_headings, "#{label}: section-heading signature changed")
      else
        assert(new_headings.empty?, "#{label}: inserted section heading requires structural checkpoint")
      end
    end

    next unless operation == "replace_block"

    surfaces_by_block.fetch(block_id, []).each do |surface|
      original = surface.fetch("original_text")
      occurrences = op.fetch("new_text").scan(Regexp.new(Regexp.escape(original))).length
      assert(occurrences == 1,
             "#{label}: registered #{surface.fetch('surface_id')} occurs #{occurrences} times instead of once")
    end
  end

  missing = decisions.keys - covered_items.uniq
  puts "P#{number}: PASS — #{patch.fetch('ops').length} ops; " \
       "#{covered_items.uniq.length}/#{decisions.length} roadmap items represented; " \
       "#{claims.fetch('surfaces').length} registered surfaces guarded" \
       "#{missing.empty? ? '' : "; no-op/unrepresented: #{missing.join(', ')}"}"
end

requested = ARGV.empty? ? PAPERS.keys : ARGV
unknown = requested - PAPERS.keys
abort("unknown paper numbers: #{unknown.join(', ')}") unless unknown.empty?

begin
  requested.each { |number| audit_paper(number, PAPERS.fetch(number)) }
rescue KeyError, RuntimeError => e
  warn "FAIL: #{e.message}"
  exit 1
end
