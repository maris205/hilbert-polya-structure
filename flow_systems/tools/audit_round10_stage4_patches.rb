#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
PAPERS = {
  "29" => "29-bianchi-ideal-owner-refinement",
  "30" => "30-three-disk-nonconstant-roof-determinant",
  "31" => "31-level11-conjugacy-owner-ledger",
  "32" => "32-homology-cover-renormalization-uniformity",
  "33" => "33-bolza-control-matched-census"
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
  provisional_path = File.join(notes, "stage4_response_to_reviewers_provisional.json")

  [handoff_path, adjudication_path, claims_path, manifest_path, roadmap_path,
   base_path, patch_path, provisional_path].each do |path|
    assert(File.file?(path), "P#{number}: missing #{path}")
  end

  handoff = load_json(handoff_path)
  adjudication = load_json(adjudication_path)
  claims = load_json(claims_path)
  manifest = load_json(manifest_path)
  roadmap = load_json(roadmap_path)
  patch = load_json(patch_path)
  provisional = load_json(provisional_path)
  base_text = File.binread(base_path).force_encoding("UTF-8")
  base_blocks = base_text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m).to_h

  assert(sha256(base_path) == handoff.fetch("base_draft_sha256"), "P#{number}: base SHA drift")
  assert(sha256(manifest_path) == handoff.fetch("block_manifest_sha256"), "P#{number}: block-manifest SHA drift")
  assert(sha256(roadmap_path) == handoff.fetch("roadmap_sha256"), "P#{number}: roadmap SHA drift")
  assert(sha256(adjudication_path) == handoff.fetch("author_adjudication_sha256"), "P#{number}: adjudication SHA drift")
  assert(sha256(claims_path) == handoff.fetch("claim_surface_manifest_sha256"), "P#{number}: claim-surface SHA drift")
  assert(claims.fetch("surfaces") == [], "P#{number}: unexpected registered claim surface")

  assert(patch.fetch("patch_format_version") == "1.1", "P#{number}: patch format is not 1.1")
  assert(patch.fetch("authorization_context") == "review_roadmap", "P#{number}: wrong authorization context")
  assert(patch.fetch("revision_round") == 1, "P#{number}: wrong revision round")
  assert(patch.fetch("base_draft_hash") == handoff.fetch("base_draft_hash"), "P#{number}: base hash mismatch")
  assert(patch.fetch("roadmap_sha256") == handoff.fetch("roadmap_sha256"), "P#{number}: roadmap binding mismatch")
  assert(patch.fetch("author_adjudication_sha256") == handoff.fetch("author_adjudication_sha256"), "P#{number}: adjudication binding mismatch")
  assert(patch.fetch("author_decision_digest") == handoff.fetch("author_decision_digest"), "P#{number}: decision digest mismatch")
  assert(patch.fetch("claim_surface_manifest_sha256") == handoff.fetch("claim_surface_manifest_sha256"), "P#{number}: claim binding mismatch")
  assert(patch.fetch("emitted_by") == "draft_writer_agent", "P#{number}: emitter role mismatch")

  assert(provisional.fetch("schema_version") == "response-to-reviewers-provisional/1.0",
         "P#{number}: provisional response schema mismatch")
  assert(provisional.fetch("artifact_status") == "PROVISIONAL_PENDING_APPLICATION_AND_POST_APPLY_AUDIT",
         "P#{number}: provisional response status mismatch")
  assert(provisional.fetch("paper_number") == number.to_i, "P#{number}: provisional paper number mismatch")
  assert(provisional.fetch("revision_round") == 1, "P#{number}: provisional revision round mismatch")
  assert(provisional.dig("patch_binding", "path") == "notes/stage4_revision_patch_round1.json",
         "P#{number}: provisional patch path mismatch")
  assert(provisional.dig("patch_binding", "sha256") == sha256(patch_path),
         "P#{number}: provisional patch SHA mismatch")
  assert(provisional.dig("patch_binding", "apply_status") == "NOT_APPLIED",
         "P#{number}: writer crossed the apply boundary")
  {
    "roadmap_sha256" => handoff.fetch("roadmap_sha256"),
    "author_adjudication_sha256" => handoff.fetch("author_adjudication_sha256"),
    "author_decision_digest" => handoff.fetch("author_decision_digest"),
    "claim_surface_manifest_sha256" => handoff.fetch("claim_surface_manifest_sha256")
  }.each do |key, expected|
    assert(provisional.dig("authority_bindings", key) == expected,
           "P#{number}: provisional authority binding #{key} mismatch")
  end
  assert(provisional.fetch("new_references_added") == 0,
         "P#{number}: bibliography mutation was not authorized")

  blocks = manifest.fetch("blocks").to_h { |row| [row.fetch("block_id"), row] }
  decisions = adjudication.fetch("author_adjudications").to_h { |row| [row.fetch("item_id"), row] }
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

    next if operation == "delete_block"
    new_text = op.fetch("new_text")
    assert(new_text.is_a?(String) && !new_text.empty?, "#{label}: missing new text")
    assert(!new_text.include?("<!--block:"), "#{label}: writer attempted block-id allocation")
    heading_pattern = /\\(?:sub)*section\*?\s*\{[^}]*\}/
    new_headings = new_text.scan(heading_pattern)
    old_headings = base_blocks.fetch(block_id).scan(heading_pattern)
    if operation == "replace_block"
      assert(new_headings == old_headings, "#{label}: section-heading signature changed")
    else
      assert(new_headings.empty?, "#{label}: inserted section heading requires structural checkpoint")
    end
  end

  missing = decisions.keys - covered_items.uniq
  assert(missing.empty?, "P#{number}: roadmap items unrepresented in patch: #{missing.join(', ')}")
  expected_order = adjudication.fetch("display_order").fetch("item_ids")
  items = provisional.fetch("items")
  assert(items.map { |row| row.fetch("roadmap_item_id") } == expected_order,
         "P#{number}: provisional response order mismatch")
  status_to_summary = {
    "RESOLVED" => "resolved",
    "DELIBERATE_LIMITATION" => "limitations",
    "UNRESOLVABLE" => "unresolvable",
    "REVIEWER_DISAGREE" => "disagreed"
  }
  assert(items.all? { |row| status_to_summary.key?(row.fetch("status")) },
         "P#{number}: invalid provisional response status")
  items.each do |row|
    next if row.fetch("status") == "RESOLVED"
    assert(row.fetch("decline_justification", "").strip.length.positive?,
           "P#{number}: #{row.fetch('roadmap_item_id')} lacks decline_justification")
  end
  summary = provisional.fetch("summary")
  assert(%w[resolved limitations unresolvable disagreed].sum { |key| summary.fetch(key) } == expected_order.length,
         "P#{number}: response summary total mismatch")
  observed = items.group_by { |row| status_to_summary.fetch(row.fetch("status")) }.transform_values(&:length)
  %w[resolved limitations unresolvable disagreed].each do |key|
    assert(summary.fetch(key) == observed.fetch(key, 0), "P#{number}: summary #{key} mismatch")
  end

  puts "P#{number}: PASS -- #{patch.fetch('ops').length} ops; #{covered_items.uniq.length}/#{decisions.length} items; " \
       "response #{summary.map { |key, value| "#{key}=#{value}" }.join(', ')}; 0 registered surfaces"
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
