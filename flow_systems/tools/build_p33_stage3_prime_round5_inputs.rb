#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
PAPER_SLUG = "33-bolza-control-matched-census"
PAPER_ROOT = File.join(ROOT, "papers", PAPER_SLUG)
NOTES = File.join(PAPER_ROOT, "notes")
DATE = "2026-09-04"
STAMP = "2026-09-03T17:50:00Z"
ROUND_ID = "p33-stage3-prime-round5-2026-09-04"

def assert!(condition, message)
  raise message unless condition
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

def relative(path)
  path.delete_prefix("#{ROOT}/")
end

def frozen_file(path)
  assert!(File.file?(path), "missing frozen file #{path}")
  assert!(!File.symlink?(path), "symlink forbidden in freeze #{path}")
  {"path" => relative(path), "sha256" => sha256(path), "bytes" => File.size(path)}
end

def artifact(filename, version)
  path = File.join(NOTES, filename)
  assert!(File.file?(path), "missing input #{path}")
  {
    "present" => true,
    "path_or_passport_ref" => "path:notes/#{filename}",
    "sha256" => sha256(path),
    "version_label" => version,
    "origin_date" => DATE
  }
end

def array_artifact(filename, version)
  entry = artifact(filename, version)
  entry.delete("present")
  {"present" => true, "items" => [entry]}
end

def unique_files(paths)
  paths.flatten.select { |path| File.file?(path) }.uniq.sort
end

event_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHOR_EVENT_20260904.txt")
authorization_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECORD.md")
authorization_receipt_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json")
batch_freeze_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json")
checkpoint_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md")

assert!(sha256(event_path) == "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812", "author event hash drift")
assert!(sha256(authorization_path) == "79c9c59b592ccf66619dfa6b1cd0e006f7dbe949890cddc22d6105a50f4a9dc5", "authorization record hash drift")
assert!(sha256(batch_freeze_path) == "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98", "batch input freeze hash drift")
assert!(sha256(checkpoint_path) == "5561443b7a061673032eb8fbd635a0b47995e04eb80c977ef6ff5409d5699cad", "checkpoint hash drift")

round4_files = unique_files([
  Dir[File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_*")],
  Dir[File.join(NOTES, "stage3_prime_round4_*")]
])
assert!(!round4_files.empty?, "no Round-4 artifacts found")
assert!(round4_files.any? { |path| path.end_with?("stage3_prime_round4_abort_record.json") }, "Round-4 abort record missing")
assert!(round4_files.any? { |path| path.end_with?("stage3_prime_round4_verdict_record.json") }, "Round-4 immutable invalid verdict missing")

canonical_files = %w[
  paper/manuscript.tex
  paper/references.bib
  paper/paper.pdf
].map { |name| File.join(PAPER_ROOT, name) }
science_files = %w[code experiments results].flat_map do |directory|
  Dir.glob(File.join(PAPER_ROOT, directory, "**", "*"), File::FNM_DOTMATCH)
end.select { |path| File.file?(path) }.sort
claim_files = unique_files([
  Dir[File.join(NOTES, "*claim*")],
  Dir[File.join(NOTES, "stage4_registered_claim_surface_replay.json")]
])

freeze = {
  "schema_version" => "p33-stage3-prime-round5-input-freeze/1.0",
  "generated_at" => STAMP,
  "workflow_date" => DATE,
  "paper_id" => "P33",
  "paper_slug" => PAPER_SLUG,
  "round_id" => ROUND_ID,
  "authority" => {
    "author_event" => frozen_file(event_path),
    "authorization_record" => frozen_file(authorization_path),
    "authorization_receipt" => frozen_file(authorization_receipt_path),
    "batch_input_freeze" => frozen_file(batch_freeze_path),
    "controlling_checkpoint" => frozen_file(checkpoint_path),
    "authorized_scope" => "P33 wholly fresh Stage 3-prime Round 5, review-side artifacts only"
  },
  "fresh_context_contract" => {
    "phase1" => "new revision-blind context; manifest verification result, roadmap, decision letter, Round-1 findings, and frozen cards only",
    "phase2a" => "separate new persuasion-blind context; Response to Reviewers and every earlier re-review result/audit withheld",
    "phase2b" => "separate integration context permitted only after Phase-2A schema and semantic PASS",
    "verdict_emitter" => "schema-correct emitter and test fixture validated before Phase-2A evidence exposure",
    "cross_model_active" => false,
    "independence_claim" => "none; same-family procedural role separation only"
  },
  "round4_preservation" => {
    "file_count" => round4_files.length,
    "files" => round4_files.map { |path| frozen_file(path) }
  },
  "immutable_boundaries" => {
    "canonical_files" => canonical_files.map { |path| frozen_file(path) },
    "science_files" => science_files.map { |path| frozen_file(path) },
    "registered_claim_files" => claim_files.map { |path| frozen_file(path) },
    "initial_system_source" => frozen_file(File.join(NOTES, "stage1_prestart_brief.md")),
    "route_crosswalk" => frozen_file(File.join(NOTES, "stage4_route_crosswalk.md")),
    "route_evaluators" => %w[skills/route-a-evaluator.md skills/route-b-evaluator.md].map do |name|
      frozen_file(File.join(ROOT, name))
    end
  }
}

manifest = {
  "contract_version" => "1.1",
  "round_id" => ROUND_ID,
  "cross_model_active" => false,
  "artifacts" => {
    "original_manuscript" => artifact("stage3_revision_base.tex", "round10-stage3-prime-input-v1"),
    "revised_manuscript" => artifact("stage4_revision_round1.tex", "round10-stage4-round1"),
    "revision_roadmap" => artifact("stage3_revision_roadmap.json", "revision-roadmap/1.0"),
    "author_adjudication" => artifact("stage4_author_adjudication.json", "author-adjudication/1.0"),
    "revision_evidence_bundle" => artifact("stage4_revision_evidence_bundle.json", "revision-evidence-bundle/1.0"),
    "editorial_decision_letter" => artifact("stage3_editorial_synthesis.md", "round10-stage3-editorial-synthesis"),
    "response_to_reviewers" => artifact("stage4_response_to_reviewers_round1.json", "round10-stage4-round1"),
    "revision_patches" => array_artifact("stage4_revision_patch_round1.json", "revision-patch/1.1"),
    "apply_reports" => array_artifact("stage4_revision_round1.tex.apply-report.json", "apply-report/1.3"),
    "round1_findings" => artifact("stage3_review_package.json", nil),
    "round1_config_cards" => artifact("stage3_phase0_field_analysis.md", "round10-stage3-frozen-cards")
  }
}

freeze_path = File.join(NOTES, "stage3_prime_round5_input_freeze.json")
manifest_path = File.join(NOTES, "stage3_prime_round5_input_manifest.json")
receipt_path = File.join(NOTES, "stage3_prime_round5_input_manifest_receipt.json")
[freeze_path, manifest_path, receipt_path].each do |path|
  assert!(!File.exist?(path), "refusing to overwrite #{path}")
end

File.write(freeze_path, JSON.pretty_generate(freeze) + "\n")
File.write(manifest_path, JSON.pretty_generate(manifest) + "\n")

receipt = {
  "schema_version" => "p33-stage3-prime-round5-input-manifest-receipt/1.0",
  "generated_at" => STAMP,
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "authority" => {
    "author_event_sha256" => sha256(event_path),
    "authorization_record_sha256" => sha256(authorization_path),
    "authorization_receipt_sha256" => sha256(authorization_receipt_path),
    "batch_input_freeze_sha256" => sha256(batch_freeze_path),
    "controlling_checkpoint_sha256" => sha256(checkpoint_path)
  },
  "input_freeze" => frozen_file(freeze_path),
  "input_manifest" => frozen_file(manifest_path).merge("jcs_sha256" => jcs_sha256(manifest)),
  "manifest_shape" => {
    "contract_version" => "1.1",
    "artifact_keys" => manifest.fetch("artifacts").keys,
    "artifact_key_count" => manifest.fetch("artifacts").length,
    "required_artifacts_present" => true,
    "apply_chain_witness_expected" => "pass"
  },
  "freshness" => {
    "new_round_id" => true,
    "round4_context_reused" => false,
    "phase1_revision_content_exposed" => false,
    "phase2a_response_content_exposed" => false,
    "phase2a_started" => false
  }
}
File.write(receipt_path, JSON.pretty_generate(receipt) + "\n")

puts "PASS -- emitted P33 Round-5 input freeze, manifest, and receipt"
puts "round_id=#{ROUND_ID}"
puts "manifest_raw_sha256=#{sha256(manifest_path)}"
puts "manifest_jcs_sha256=#{jcs_sha256(manifest)}"
puts "round4_files_frozen=#{round4_files.length}"
