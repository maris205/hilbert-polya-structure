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
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def marker_free_blocks(path)
  source = File.binread(path).force_encoding("UTF-8")
  blocks = []
  current = nil
  offset = 0
  source.lines.each do |line|
    marker = line.match(/\A<!--block:(B\d{4})-->\s*\z/)
    if marker
      current = {"block_id" => marker[1], "start_byte" => offset, "text" => +""}
      blocks << current
    else
      raise "content before first marker in #{path}" unless current
      current.fetch("text") << line
      offset += line.bytesize
    end
  end
  blocks.each { |block| block["end_byte"] = block.fetch("start_byte") + block.fetch("text").bytesize }
  blocks
end

def numeric_tokens(text)
  text.scan(/(?<![A-Za-z])(?:\d+(?:[.,]\d+)*(?:e[+-]?\d+)?|\d+\/\d+)(?![A-Za-z])/i).uniq.sort
end

def build(number, directory)
  notes = File.join(ROOT, "papers", directory, "notes")
  base_path = File.join(notes, "stage3_revision_base.tex")
  patch_path = File.join(notes, "stage4_revision_patch_round1.json")
  registry_path = File.join(notes, "stage2_5_claim_registry.json")
  revised_path = File.join(notes, "stage4_revision_round1.tex")
  [base_path, patch_path, registry_path].each { |path| raise "P#{number}: missing #{path}" unless File.file?(path) }

  blocks = marker_free_blocks(base_path)
  block_by_id = blocks.to_h { |block| [block.fetch("block_id"), block] }
  patch = load_json(patch_path)
  registry = load_json(registry_path).fetch("claims")
  revised = File.file?(revised_path) ? File.binread(revised_path).force_encoding("UTF-8") : nil
  touched = patch.fetch("ops").map { |op| op.fetch("block_id") }.uniq

  claims_by_block = Hash.new { |hash, key| hash[key] = [] }
  registry.each do |claim|
    span = claim.fetch("draft_span")
    start_byte = span.fetch("start_byte")
    end_byte = span.fetch("end_byte")
    owner = blocks.find do |block|
      start_byte >= block.fetch("start_byte") && end_byte <= block.fetch("end_byte")
    end
    raise "P#{number}: cannot map #{claim.fetch('claim_id')} span to one block" unless owner
    claim_text = claim.fetch("claim_text")
    local_start = start_byte - owner.fetch("start_byte")
    unless owner.fetch("text").byteslice(local_start, end_byte - start_byte) == claim_text.force_encoding("UTF-8")
      raise "P#{number}: #{claim.fetch('claim_id')} span text mismatch"
    end
    claims_by_block[owner.fetch("block_id")] << claim
  end

  operation_rows = patch.fetch("ops").map.with_index do |op, index|
    block_id = op.fetch("block_id")
    old_text = block_by_id.fetch(block_id).fetch("text")
    new_text = op["new_text"]
    affected = op.fetch("op") == "replace_block" || op.fetch("op") == "delete_block" ? claims_by_block[block_id] : []
    {
      "op_index" => index,
      "op" => op.fetch("op"),
      "block_id" => block_id,
      "roadmap_item_ids" => op.fetch("roadmap_item_ids"),
      "old_text" => old_text,
      "new_text" => new_text,
      "old_numeric_tokens" => numeric_tokens(old_text),
      "new_numeric_tokens" => numeric_tokens(new_text.to_s),
      "affected_registered_e1_claims" => affected.map do |claim|
        {
          "claim_id" => claim.fetch("claim_id"),
          "claim_kinds" => claim.fetch("claim_kinds", []),
          "selection_tier" => claim.fetch("selection_tier", "UNSPECIFIED"),
          "high_impact_basis" => claim.fetch("high_impact_basis", []),
          "writer_anchors" => claim.fetch("writer_anchors", []),
          "original_claim_text" => claim.fetch("claim_text"),
          "original_text_sha256" => Digest::SHA256.hexdigest(claim.fetch("claim_text")),
          "occurrences_byte_exact_in_revised" => revised ? revised.scan(Regexp.new(Regexp.escape(claim.fetch("claim_text")))).length : nil
        }
      end
    }
  end

  affected_ids = operation_rows.flat_map { |row| row.fetch("affected_registered_e1_claims").map { |claim| claim.fetch("claim_id") } }.uniq
  packet = {
    "schema" => "round10-stage4-bounded-semantic-review-packet/1.0",
    "paper_number" => number.to_i,
    "purpose" => "Manual review aid for every authorized changed operation; not an automatic E6 verdict and not Stage 4.5.",
    "bindings" => {
      "base_draft_sha256" => sha256(base_path),
      "patch_sha256" => sha256(patch_path),
      "stage2_5_claim_registry_sha256" => sha256(registry_path),
      "revised_draft_sha256" => File.file?(revised_path) ? sha256(revised_path) : nil
    },
    "coverage" => {
      "operation_count" => operation_rows.length,
      "unique_target_block_count" => touched.length,
      "registry_claim_count" => registry.length,
      "affected_registry_claim_count" => affected_ids.length,
      "all_operations_included" => operation_rows.length == patch.fetch("ops").length
    },
    "mandatory_review_questions" => [
      "Does each replacement preserve or narrow the scientific strength of every affected E1 claim?",
      "Does each inserted or replaced passage avoid inventing executed experiments, proofs, released artifacts, source passage anchors, or route credit?",
      "Are all new numeric tokens either inherited frozen values, identifiers/version syntax, or explicitly prospective/synthetic?",
      "Do the frozen dynamical system, clock, owner convention, normalization, cutoff, Route-A tuple, and Route-B state remain unchanged?",
      "Are deliberately unclosed bibliography, source-finalization, independent-verifier, producer, proof, or census obligations disclosed rather than represented as complete?"
    ],
    "operations" => operation_rows
  }
  output = File.join(notes, "stage4_unregistered_claim_drift_review_packet.json")
  File.binwrite(output, JSON.pretty_generate(packet) + "\n")
  puts "P#{number}: packet built; #{operation_rows.length} ops; #{affected_ids.length}/#{registry.length} E1 claims affected"
end

requested = ARGV.empty? ? PAPERS.keys : ARGV
unknown = requested - PAPERS.keys
abort("unknown paper numbers: #{unknown.join(', ')}") unless unknown.empty?

begin
  requested.each { |number| build(number, PAPERS.fetch(number)) }
rescue KeyError, JSON::ParserError, RuntimeError => e
  warn "FAIL: #{e.message}"
  exit 1
end
