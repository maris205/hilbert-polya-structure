#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
PAPER_ROOT = File.join(ROOT, "papers", "33-bolza-control-matched-census")
NOTES = File.join(PAPER_ROOT, "notes")
OUTPUT = File.join(NOTES, "stage3_prime_round4_phase1_validation.json")
ROUND_ID = "p33-stage3-prime-round4-2026-09-03"

def assert!(condition, message)
  raise "P33_ROUND4_PHASE1_FAIL: #{message}" unless condition
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

def normalize_labels(raw)
  stripped = raw.gsub(/\([^()]*\)/, "").sub(/ — .*/, "")
  labels = []
  stripped.split(/,|\/|;| and |&/).each do |token|
    value = token.strip.downcase
    label = case value
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

def verify_frozen!(root, node, checks, prefix)
  case node
  when Hash
    if node.keys.sort == %w[bytes path sha256]
      path = File.join(root, node.fetch("path"))
      assert!(File.file?(path) && !File.symlink?(path), "#{prefix}: missing or symlinked #{node.fetch('path')}")
      assert!(File.size(path) == node.fetch("bytes"), "#{prefix}: byte-size drift #{node.fetch('path')}")
      assert!(sha256(path) == node.fetch("sha256"), "#{prefix}: hash drift #{node.fetch('path')}")
      checks << "#{prefix}:#{node.fetch('path')}"
    else
      node.each { |key, value| verify_frozen!(root, value, checks, "#{prefix}.#{key}") }
    end
  when Array
    node.each_with_index { |value, index| verify_frozen!(root, value, checks, "#{prefix}[#{index}]") }
  end
end

manifest_path = File.join(NOTES, "stage3_prime_round4_input_manifest.json")
freeze_path = File.join(NOTES, "stage3_prime_round4_input_freeze.json")
receipt_path = File.join(NOTES, "stage3_prime_round4_input_manifest_receipt.json")
pre_path = File.join(NOTES, "stage3_prime_round4_precommitment.json")
context_path = File.join(NOTES, "stage3_prime_round4_phase1_receipt.md")
roadmap_path = File.join(NOTES, "stage3_revision_roadmap.json")

[manifest_path, freeze_path, receipt_path, pre_path, context_path, roadmap_path].each do |path|
  assert!(File.file?(path), "missing #{path.delete_prefix("#{ROOT}/")}")
end
assert!(!File.exist?(OUTPUT), "refusing to overwrite #{OUTPUT}")

manifest = load_json(manifest_path)
freeze = load_json(freeze_path)
input_receipt = load_json(receipt_path)
pre = load_json(pre_path)
roadmap = load_json(roadmap_path)
checks = []

assert!(manifest.fetch("contract_version") == "1.1", "manifest contract version")
checks << "manifest_contract_version"
assert!(manifest.fetch("round_id") == ROUND_ID, "manifest round id")
checks << "manifest_round_id"
assert!(manifest.fetch("artifacts").keys.length == 11, "manifest must contain eleven artifact keys")
checks << "manifest_eleven_keys"
assert!(input_receipt.dig("input_manifest", "sha256") == sha256(manifest_path), "manifest raw receipt binding")
checks << "manifest_raw_receipt_binding"
assert!(input_receipt.dig("input_manifest", "jcs_sha256") == jcs_sha256(manifest), "manifest JCS receipt binding")
checks << "manifest_jcs_receipt_binding"
verify_frozen!(ROOT, freeze.fetch("round3_preservation"), checks, "round3_preservation")
verify_frozen!(ROOT, freeze.fetch("immutable_boundaries"), checks, "immutable_boundaries")

assert!(pre.fetch("contract_version") == "1.1", "precommitment contract version")
checks << "precommitment_contract_version"
assert!(pre.fetch("round_id") == ROUND_ID, "precommitment round id")
checks << "precommitment_round_id"
assert!(pre.fetch("input_manifest_hash") == jcs_sha256(manifest), "precommitment manifest JCS binding")
checks << "precommitment_manifest_binding"
assert!(pre.fetch("new_standards") == [], "unexpected new standard")
checks << "new_standards_empty"

expected = roadmap.fetch("items").select { |item| %w[must_fix should_fix].include?(item.fetch("obligation_class")) }
rows = pre.fetch("items")
assert!(rows.map { |row| row.fetch("item_id") } == expected.map { |item| item.fetch("id") }, "coverage/order mismatch")
checks << "coverage_and_order"

rows.zip(expected).each do |row, item|
  id = item.fetch("id")
  assert!(row.fetch("obligation_class") == item.fetch("obligation_class"), "#{id}: obligation class")
  checks << "#{id}:obligation_class"
  assert!(row.dig("inherited_criterion", "roadmap_text") == item.fetch("verification_criteria"), "#{id}: criterion not verbatim")
  checks << "#{id}:roadmap_text"
  assert!(row.fetch("source_reviewer") == item.fetch("reviewer"), "#{id}: reviewer not verbatim")
  checks << "#{id}:source_reviewer"
  assert!(row.fetch("source_reviewer_labels") == normalize_labels(item.fetch("reviewer")), "#{id}: normalized labels")
  checks << "#{id}:source_reviewer_labels"
  assert!(row.fetch("equivalence_policy") == "allowed", "#{id}: equivalence policy")
  checks << "#{id}:equivalence_policy"
  expected_keys = item.fetch("obligation_class") == "must_fix" ? %w[fully_addressed made_worse_discriminator partially_addressed] : %w[fully_addressed]
  assert!(row.fetch("operationalization").keys.sort == expected_keys.sort, "#{id}: operationalization shape")
  checks << "#{id}:operationalization_shape"
  assert!(row.fetch("operationalization").values.all? { |text| !text.strip.empty? }, "#{id}: empty operationalization")
  checks << "#{id}:operationalization_nonempty"
  surface = row.fetch("expected_change_surface")
  assert!(!surface.strip.empty?, "#{id}: empty expected surface")
  checks << "#{id}:surface_nonempty"
  item.fetch("proposed_targets", []).each do |target|
    assert!(surface.include?(target.fetch("block_id")), "#{id}: missing target #{target.fetch('block_id')}")
    checks << "#{id}:surface_#{target.fetch('block_id')}"
  end
end

context = File.read(context_path, encoding: "UTF-8")
assert!(context.include?("fork_turns=none"), "fresh-context fork marker absent")
checks << "fresh_context_fork_none"
assert!(context.include?("revision_blind=true"), "revision-blind marker absent")
checks << "revision_blind_declared"
assert!(context.include?("prohibited_material_inspected=false"), "withholding declaration absent")
checks << "withholding_declared"
assert!(context.lines.reverse.find { |line| !line.strip.empty? }&.strip == "[CONTRACT-ACKNOWLEDGED]", "missing terminal marker")
checks << "contract_acknowledged"

payload = {
  "schema_version" => "p33-stage3-prime-round4-phase1-validation/1.0",
  "generated_at" => "2026-09-03T16:00:00Z",
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "phase" => "phase1_revision_blind_precommitment",
  "status" => "PASS",
  "inputs" => {
    "manifest_raw_sha256" => sha256(manifest_path),
    "manifest_jcs_sha256" => jcs_sha256(manifest),
    "input_freeze_sha256" => sha256(freeze_path),
    "roadmap_sha256" => sha256(roadmap_path)
  },
  "outputs" => {
    "precommitment_raw_sha256" => sha256(pre_path),
    "precommitment_jcs_sha256" => jcs_sha256(pre),
    "phase1_receipt_sha256" => sha256(context_path)
  },
  "counts" => {
    "roadmap_items" => roadmap.fetch("items").length,
    "precommitted_items" => rows.length,
    "must_fix" => rows.count { |row| row.fetch("obligation_class") == "must_fix" },
    "should_fix" => rows.count { |row| row.fetch("obligation_class") == "should_fix" },
    "new_standards" => pre.fetch("new_standards").length,
    "validation_checks" => checks.length
  },
  "freshness" => {
    "fresh_context" => true,
    "fork_turns" => "none",
    "revision_blind" => true,
    "round3_context_reused" => false,
    "phase2a_started" => false
  },
  "checks" => checks
}
File.write(OUTPUT, JSON.pretty_generate(payload) + "\n")
puts "PASS -- P33 Round-4 Phase 1: #{checks.length} checks, #{rows.length} precommitments"
