#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
PAPER_SLUG = "33-bolza-control-matched-census"
PAPER_ROOT = File.join(ROOT, "papers", PAPER_SLUG)
NOTES = File.join(PAPER_ROOT, "notes")
DATE = "2026-09-03"
STAMP = "2026-09-03T15:46:00Z"
ROUND_ID = "p33-stage3-prime-round4-2026-09-03"

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

event_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt")
authorization_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md")
batch_freeze_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json")
assert!(sha256(event_path) == "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812", "author event hash drift")
assert!(sha256(authorization_path) == "67ad4ce8bfb34676b46ffb96e8c9833c1204ada3ffde1e0dc542ea43c46acca5", "authorization record hash drift")
assert!(sha256(batch_freeze_path) == "82dbf52120f120ffea6ba82b4614c69d4022a32bc01305a892eadde92b8248b7", "batch input freeze hash drift")

round3_files = unique_files([
  Dir[File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_*")],
  Dir[File.join(NOTES, "stage3_prime_round3_*")]
])
assert!(!round3_files.empty?, "no Round-3 artifacts found")
assert!(round3_files.any? { |path| path.end_with?("stage3_prime_round3_abort_record.json") }, "Round-3 abort record missing")
assert!(round3_files.any? { |path| path.end_with?("PHASE2A_SEMANTIC_AUDIT_P33_INVALID_ATTEMPT1_INCIDENT.md") }, "invalid-attempt incident missing")

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
  "schema_version" => "p33-stage3-prime-round4-input-freeze/1.0",
  "generated_at" => STAMP,
  "paper_id" => "P33",
  "paper_slug" => PAPER_SLUG,
  "round_id" => ROUND_ID,
  "authority" => {
    "author_event" => frozen_file(event_path),
    "authorization_record" => frozen_file(authorization_path),
    "batch_input_freeze" => frozen_file(batch_freeze_path),
    "authorized_scope" => "P33 wholly fresh Stage 3 prime Round 4, review-side artifacts only"
  },
  "fresh_context_contract" => {
    "phase1" => "new revision-blind context; manifest verification result, roadmap, decision letter, Round-1 findings, and frozen cards only",
    "phase2a" => "separate new persuasion-blind context; Response to Reviewers and every earlier re-review result/audit withheld",
    "phase2b" => "permitted only after Phase-2A structural and semantic PASS",
    "cross_model_active" => false,
    "independence_claim" => "none; same-family role separation only"
  },
  "round3_preservation" => {
    "file_count" => round3_files.length,
    "files" => round3_files.map { |path| frozen_file(path) }
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

freeze_path = File.join(NOTES, "stage3_prime_round4_input_freeze.json")
manifest_path = File.join(NOTES, "stage3_prime_round4_input_manifest.json")
receipt_path = File.join(NOTES, "stage3_prime_round4_input_manifest_receipt.json")
[freeze_path, manifest_path, receipt_path].each do |path|
  assert!(!File.exist?(path), "refusing to overwrite #{path}")
end

File.write(freeze_path, JSON.pretty_generate(freeze) + "\n")
File.write(manifest_path, JSON.pretty_generate(manifest) + "\n")

receipt = {
  "schema_version" => "p33-stage3-prime-round4-input-manifest-receipt/1.0",
  "generated_at" => STAMP,
  "paper_id" => "P33",
  "round_id" => ROUND_ID,
  "authority" => {
    "author_event_sha256" => sha256(event_path),
    "authorization_record_sha256" => sha256(authorization_path),
    "batch_input_freeze_sha256" => sha256(batch_freeze_path)
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
    "round3_context_reused" => false,
    "phase1_revision_content_exposed" => false,
    "phase2a_response_content_exposed" => false
  }
}
File.write(receipt_path, JSON.pretty_generate(receipt) + "\n")

puts "PASS -- emitted P33 Round-4 input freeze, manifest, and receipt"
puts "round_id=#{ROUND_ID}"
puts "manifest_raw_sha256=#{sha256(manifest_path)}"
puts "manifest_jcs_sha256=#{jcs_sha256(manifest)}"
puts "round3_files_frozen=#{round3_files.length}"
