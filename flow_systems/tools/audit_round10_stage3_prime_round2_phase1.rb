#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_VALIDATION.json")
PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

LETTER_SECTION = /^### Required Item Details\s*$/
LETTER_BLOCK = /^\*\*(R[1-9][0-9]*): .*\*\*\s*$/
LETTER_CRITERION = /^- \*\*Acceptance criteria\*\*: (.*)$/

def assert!(condition, message)
  raise message unless condition
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
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

def normalize_reviewer_labels(raw)
  stripped = raw.gsub(/\([^()]*\)/, "").sub(/ — .*/, "")
  tokens = stripped.split(/,|\/|;| and |&/)
  labels = []
  tokens.each do |token|
    normalized = token.strip.downcase
    label = case normalized
            when "eic", "editor", "editor-in-chief" then "EIC"
            when "da", "devil's advocate", "devils advocate" then "DA"
            when /\Ar([1-3])\z/ then "R#{Regexp.last_match(1)}"
            when /\Areviewer ([1-3])\z/ then "R#{Regexp.last_match(1)}"
            when /\Apeer reviewer ([1-3])\z/ then "R#{Regexp.last_match(1)}"
            end
    labels << label if label && !labels.include?(label)
  end
  labels
end

def parse_letter(path)
  blocks = []
  in_section = false
  current = nil
  File.read(path, encoding: "UTF-8").split("\n", -1).each do |line|
    if LETTER_SECTION.match?(line)
      in_section = true
      next
    end
    next unless in_section
    break if line.start_with?("## ")

    if (header = LETTER_BLOCK.match(line))
      current = [header[1], nil]
      blocks << current
      next
    end
    next unless current && current[1].nil?

    criterion = LETTER_CRITERION.match(line)
    current[1] = criterion[1] if criterion
  end
  blocks
end

papers = []
total_checks = 0
total_items = 0

PAPERS.each do |paper_id, slug|
  notes = File.join(ROOT, "papers", slug, "notes")
  manifest_path = File.join(notes, "stage3_prime_round2_input_manifest.json")
  roadmap_path = File.join(notes, "stage3_revision_roadmap.json")
  precommitment_path = File.join(notes, "stage3_prime_round2_precommitment.json")
  letter_path = File.join(notes, "stage3_editorial_synthesis.md")
  receipt_path = File.join(notes, "stage3_prime_round2_phase1_receipt.md")

  manifest = load_json(manifest_path)
  roadmap = load_json(roadmap_path)
  precommitment = load_json(precommitment_path)
  roadmap_items = roadmap.fetch("items").select { |item| %w[must_fix should_fix].include?(item.fetch("obligation_class")) }
  records = precommitment.fetch("items")
  checks = []
  check = lambda do |condition, label|
    assert!(condition, "#{paper_id}: #{label}")
    checks << label
  end

  check.call(precommitment.fetch("contract_version") == "1.1", "contract_version")
  check.call(precommitment.fetch("round_id") == manifest.fetch("round_id"), "round_id_binding")
  check.call(precommitment.fetch("input_manifest_hash") == jcs_sha256(manifest), "manifest_jcs_binding")
  check.call(precommitment.fetch("new_standards") == [], "new_standards_empty")
  check.call(records.map { |record| record.fetch("item_id") } == roadmap_items.map { |item| item.fetch("id") }, "coverage_and_order")

  records.zip(roadmap_items).each do |record, item|
    item_id = item.fetch("id")
    check.call(record.fetch("obligation_class") == item.fetch("obligation_class"), "#{item_id}:obligation_class")
    check.call(record.dig("inherited_criterion", "roadmap_text") == item.fetch("verification_criteria"), "#{item_id}:roadmap_text")
    check.call(record.fetch("source_reviewer") == item.fetch("reviewer"), "#{item_id}:source_reviewer")
    check.call(record.fetch("source_reviewer_labels") == normalize_reviewer_labels(item.fetch("reviewer")), "#{item_id}:source_reviewer_labels")
    check.call(record.fetch("equivalence_policy") == "allowed", "#{item_id}:equivalence_policy")
    operational_keys = record.fetch("operationalization").keys.sort
    expected_keys = item.fetch("obligation_class") == "must_fix" ? %w[fully_addressed made_worse_discriminator partially_addressed] : %w[fully_addressed]
    check.call(operational_keys == expected_keys.sort, "#{item_id}:operationalization_shape")
    surface = record.fetch("expected_change_surface")
    item.fetch("proposed_targets", []).each do |target|
      check.call(surface.include?(target.fetch("block_id")), "#{item_id}:surface_block_#{target.fetch('block_id')}")
    end
    check.call(!surface.strip.empty?, "#{item_id}:surface_nonempty")
  end

  blocks = parse_letter(letter_path)
  must_fix = roadmap_items.select { |item| item.fetch("obligation_class") == "must_fix" }
  check.call(blocks.each_with_index.all? { |(rid, _), index| rid == "R#{index + 1}" }, "letter_ordinal_contiguity")
  check.call(blocks.length <= must_fix.length, "letter_count_bound")
  block_by_id = blocks.to_h
  must_fix.each_with_index do |item, index|
    record = records.find { |candidate| candidate.fetch("item_id") == item.fetch("id") }
    criterion = record.fetch("inherited_criterion")
    ref = "R#{index + 1}"
    if block_by_id[ref]
      check.call(criterion["letter_item_ref"] == ref, "#{item.fetch('id')}:letter_ref")
      check.call(criterion["letter_text"] == block_by_id.fetch(ref), "#{item.fetch('id')}:letter_text")
    else
      check.call(!criterion.key?("letter_item_ref") && !criterion.key?("letter_text"), "#{item.fetch('id')}:letter_fields_absent")
    end
  end
  records.select { |record| record.fetch("obligation_class") == "should_fix" }.each do |record|
    criterion = record.fetch("inherited_criterion")
    check.call(!criterion.key?("letter_item_ref") && !criterion.key?("letter_text"), "#{record.fetch('item_id')}:should_fix_letter_fields_absent")
  end

  receipt_tail = File.readlines(receipt_path, chomp: true).last
  check.call(receipt_tail == "[CONTRACT-ACKNOWLEDGED]", "phase1_receipt_acknowledgement")

  papers << {
    "paper_id" => paper_id,
    "paper_slug" => slug,
    "round_id" => manifest.fetch("round_id"),
    "manifest_sha256" => sha256(manifest_path),
    "manifest_jcs_sha256" => jcs_sha256(manifest),
    "precommitment_sha256" => sha256(precommitment_path),
    "precommitment_jcs_sha256" => jcs_sha256(precommitment),
    "phase1_receipt_sha256" => sha256(receipt_path),
    "roadmap_items_precommitted" => records.length,
    "must_fix" => records.count { |record| record.fetch("obligation_class") == "must_fix" },
    "should_fix" => records.count { |record| record.fetch("obligation_class") == "should_fix" },
    "strict_letter_blocks" => blocks.length,
    "validation_checks" => checks.length,
    "status" => "PASS"
  }
  total_checks += checks.length
  total_items += records.length
end

payload = {
  "schema_version" => "round10-stage3-prime-round2-phase1-validation/1.0",
  "generated_at" => "2026-09-03T09:30:00Z",
  "contract_version" => "1.1",
  "review_mode" => "three-gate-evidence-before-persuasion",
  "phase" => "phase1_revision_blind_precommitment",
  "papers" => papers,
  "totals" => {
    "papers" => papers.length,
    "precommitted_items" => total_items,
    "validation_checks" => total_checks,
    "schema_validation" => "PASS",
    "phase1_validation" => "PASS"
  },
  "boundary" => {
    "phase2a_started" => false,
    "revision_evidence_exposed_during_phase1" => false,
    "phase2b_response_material_exposed" => false,
    "manuscripts_modified" => false,
    "science_artifacts_modified" => false,
    "route_credit_changed" => false
  }
}

File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS — Round 10 Stage 3′ Round 2 Phase 1: #{total_checks} checks; #{total_items} precommitments across #{papers.length} papers"
