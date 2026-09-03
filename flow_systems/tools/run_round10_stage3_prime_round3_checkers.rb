#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "optparse"

ROOT = File.expand_path("..", __dir__)
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite"
CHECKER = File.join(ARS_ROOT, "ars/scripts/check_re_review_synthesis.py")
EXPECTED_CHECKER_SHA256 = "8347ec3766857366cc0c6ffd30021afcebf8d0528a83927fabfce9ecb66a59ab"
CHECKED_AT = "2026-09-03T15:30:00Z"
DISCLOSURE = "This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2)."
PAPER_SLUGS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze
VERDICTS = %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].freeze

options = { paper_ids: PAPER_SLUGS.keys, candidate_dir: nil }
OptionParser.new do |parser|
  parser.on("--papers IDS", "Comma-separated eligible paper IDs") { |ids| options[:paper_ids] = ids.split(",") }
  parser.on("--candidate-dir DIR", "Write checker receipts to a comparison directory") { |dir| options[:candidate_dir] = File.expand_path(dir) }
end.parse!
FileUtils.mkdir_p(options[:candidate_dir]) if options[:candidate_dir]

def assert!(condition, message)
  raise "ROUND3_CHECKER_FAIL_CLOSED: #{message}" unless condition
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

def artifact_path(paper_root, entry, label)
  assert!(entry.fetch("present"), "#{label} absent")
  ref = entry.fetch("path_or_passport_ref")
  assert!(ref.start_with?("path:"), "#{label} is not a path ref")
  relative = ref.delete_prefix("path:")
  assert!(!relative.start_with?("/") && !relative.split("/").include?(".."), "unsafe #{label} path")
  path = File.expand_path(relative, paper_root)
  assert!(path.start_with?("#{paper_root}/") && File.file?(path) && !File.symlink?(path), "unsafe or missing #{label}")
  assert!(sha256(path) == entry.fetch("sha256"), "#{label} hash drift")
  path
end

def binding(path, json: false)
  row = {"path" => path.delete_prefix("#{ROOT}/"), "raw_sha256" => sha256(path)}
  row["jcs_sha256"] = jcs_sha256(load_json(path)) if json
  row
end

def decision_rule(trace, roadmap)
  by_id = roadmap.fetch("items").to_h { |item| [item.fetch("id"), item] }
  rows = trace.fetch("rows")
  must = rows.select { |row| by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == "must_fix" }
  should = rows.select { |row| by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == "should_fix" }
  issues = trace.fetch("new_issues")
  critical_worse = must.any? { |row| row.fetch("final_verdict") == "MADE_WORSE" && by_id.fetch(row.fetch("item_id"))["severity"] == "critical" }
  critical_regression = issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "critical" }
  negative_count = must.count { |row| %w[NOT_ADDRESSED MADE_WORSE].include?(row.fetch("final_verdict")) }
  half_negative = !must.empty? && negative_count * 2 >= must.length
  must_negative = must.any? { |row| %w[NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].include?(row.fetch("final_verdict")) }
  major_regression = issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "major" }
  must_residual = trace.dig("decision_inputs", "per_item").any? do |row|
    row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && row["residual_obligation_class"] == "must_fix"
  end
  lower_residual = trace.dig("decision_inputs", "per_item").any? do |row|
    row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && %w[should_fix consider].include?(row["residual_obligation_class"])
  end
  rate = trace.dig("decision_inputs", "should_fix_addressed_rate")
  under_eighty = rate.fetch("denominator").positive? && rate.fetch("numerator") * 5 < rate.fetch("denominator") * 4
  should_worse = should.any? { |row| row.fetch("final_verdict") == "MADE_WORSE" }
  minor_regression = issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "minor" }
  return "B1" if critical_worse || critical_regression
  return "B2" if half_negative
  return "B3" if must_negative || major_regression
  return "B4" if must_residual
  return "B5" if lower_residual || under_eighty || should_worse || minor_regression

  "B6"
end

assert!(sha256(CHECKER) == EXPECTED_CHECKER_SHA256, "checker hash drift")
assert!(options[:paper_ids].uniq == options[:paper_ids], "duplicate paper id")
unknown = options[:paper_ids] - PAPER_SLUGS.keys
assert!(unknown.empty?, "unknown paper id(s): #{unknown.join(',')}")

options[:paper_ids].each do |paper_id|
  slug = PAPER_SLUGS.fetch(paper_id)
  paper_root = File.join(ROOT, "papers", slug)
  notes = File.join(paper_root, "notes")
  manifest_path = File.join(notes, "stage3_prime_round3_input_manifest.json")
  precommitment_path = File.join(notes, "stage3_prime_round3_precommitment.json")
  verdict_path = File.join(notes, "stage3_prime_round3_verdict_record.json")
  integration_path = File.join(notes, "stage3_prime_round3_phase2b_integration.json")
  traceability_path = File.join(notes, "stage3_prime_round3_traceability.json")
  manifest = load_json(manifest_path)
  verdict = load_json(verdict_path)
  integration = load_json(integration_path)
  traceability = load_json(traceability_path)
  artifacts = manifest.fetch("artifacts")
  roadmap_path = artifact_path(paper_root, artifacts.fetch("revision_roadmap"), "roadmap")
  author_path = artifact_path(paper_root, artifacts.fetch("author_adjudication"), "author adjudication")
  bundle_path = artifact_path(paper_root, artifacts.fetch("revision_evidence_bundle"), "revision evidence bundle")
  letter_path = artifact_path(paper_root, artifacts.fetch("editorial_decision_letter"), "editorial decision letter")
  apply_paths = artifacts.fetch("apply_reports").fetch("items").each_with_index.map do |entry, index|
    artifact_path(paper_root, entry.merge("present" => true), "apply report #{index}")
  end

  command = ["python", CHECKER,
             "--manifest", manifest_path,
             "--precommitment", precommitment_path,
             "--verdict-record", verdict_path,
             "--traceability", traceability_path,
             "--roadmap", roadmap_path,
             "--author-adjudication", author_path,
             "--revision-evidence-bundle", bundle_path,
             "--revision-evidence-root", paper_root,
             "--letter", letter_path]
  apply_paths.each { |path| command.concat(["--apply-report", path]) }
  stdout, stderr, status = Open3.capture3(*command)
  assert!(status.success?, "#{paper_id} checker failed: #{stderr}#{stdout}")
  decision = traceability.fetch("decision_state")
  assert!(stdout.include?("decision_state '#{decision}'"), "#{paper_id} checker/traceability decision mismatch")
  assert!(integration.fetch("verdict_record_hash") == jcs_sha256(verdict), "#{paper_id} integration hash binding")
  counts = VERDICTS.to_h { |name| [name, traceability.fetch("rows").count { |row| row.fetch("final_verdict") == name }] }
  rule = decision_rule(traceability, load_json(roadmap_path))
  expected_decision = {"B1" => "Major Revision", "B2" => "Major Revision", "B3" => "Major Revision", "B4" => "Major Revision", "B5" => "Minor Revision", "B6" => "Accept"}.fetch(rule)
  assert!(decision == expected_decision, "#{paper_id} decision-rule mismatch")

  receipt = {
    "schema_version" => "round10-stage3-prime-round3-checker-receipt/1.0",
    "paper_id" => paper_id,
    "round_id" => manifest.fetch("round_id"),
    "checked_at" => CHECKED_AT,
    "checker" => "ARS-Codex 0.1.26 scripts/check_re_review_synthesis.py",
    "checker_sha256" => EXPECTED_CHECKER_SHA256,
    "checker_status" => "PASS",
    "checker_exit_code" => status.exitstatus,
    "checker_stdout" => stdout,
    "checker_stderr" => stderr,
    "checker_message" => stdout.strip,
    "decision_emitted" => true,
    "decision_state" => decision,
    "decision_rule" => rule,
    "reject_recommended" => traceability.dig("decision_inputs", "reject_recommended"),
    "apply_chain_witness" => traceability.dig("decision_inputs", "apply_chain_witness"),
    "cross_model_status" => "not_configured",
    "phase_counts" => counts,
    "adjustments" => integration.fetch("adjustments").length,
    "new_issues" => verdict.fetch("new_issues").length,
    "dissents" => verdict.fetch("dissents").length,
    "escalation_exceptions" => verdict.fetch("escalation_exceptions").length,
    "artifacts" => {
      "input_manifest" => binding(manifest_path, json: true),
      "precommitment" => binding(precommitment_path, json: true),
      "verdict_record" => binding(verdict_path, json: true),
      "phase2b_integration" => binding(integration_path, json: true),
      "traceability" => binding(traceability_path, json: true),
      "revision_roadmap" => binding(roadmap_path, json: true),
      "author_adjudication" => binding(author_path, json: true),
      "revision_evidence_bundle" => binding(bundle_path, json: true),
      "editorial_decision_letter" => {"path" => letter_path.delete_prefix("#{ROOT}/"), "sha256" => sha256(letter_path)},
      "apply_reports" => apply_paths.map { |path| binding(path, json: true) }
    },
    "same_family_disclosure" => DISCLOSURE,
    "boundaries" => {
      "canonical_manuscript_pdf_bibliography_changed" => false,
      "science_results_changed" => false,
      "initial_dynamical_system_changed" => false,
      "route_credit_changed" => false,
      "route_b_invoked" => false,
      "successor_stage_authorized" => false
    }
  }
  destination = if options[:candidate_dir]
                  File.join(options[:candidate_dir], "#{paper_id.downcase}_stage3_prime_round3_checker_receipt.json")
                else
                  File.join(notes, "stage3_prime_round3_checker_receipt.json")
                end
  bytes = JSON.pretty_generate(receipt) + "\n"
  if File.exist?(destination)
    assert!(File.binread(destination) == bytes.b, "#{paper_id} differing checker receipt already exists")
  else
    File.write(destination, bytes)
  end
  puts "#{paper_id} checker PASS — #{decision} / #{rule} -> #{destination}"
end
