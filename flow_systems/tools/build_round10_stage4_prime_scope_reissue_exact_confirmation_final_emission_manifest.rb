#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
OUTPUT = (ROOT / "#{PREFIX}_FINAL_EMISSION_MANIFEST.json").freeze
SCHEMA = "round10-stage4-prime-scope-reissue-exact-confirmation-final-emission-manifest/1.0"
STATUS = "PASS_EXACT_CONFIRMATION_FINAL_EMISSION_READY_FOR_DETERMINISTIC_APPLY"
PREPARATION_ROLE = "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"

AUTHORITY_PATHS = {
  "author_event" => "#{PREFIX}_AUTHOR_EVENT_20260904.txt",
  "authorization_record" => "#{PREFIX}_AUTHORIZATION_RECORD.md",
  "input_freeze" => "#{PREFIX}_INPUT_FREEZE.json",
  "authorization_receipt" => "#{PREFIX}_AUTHORIZATION_RECEIPT.json",
  "authority_audit" => "#{PREFIX}_AUTHORITY_AUDIT.json"
}.freeze

AUTHORITY_SHA256 = {
  "author_event" => "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe",
  "authorization_record" => "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79",
  "input_freeze" => "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1",
  "authorization_receipt" => "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21",
  "authority_audit" => "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2"
}.freeze

TRACK_PATHS = {
  "P29_P32" => "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json",
  "P30_P31" => "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json",
  "P33" => "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json"
}.freeze

CROSS_AUDITS = %w[
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P29_P32.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P33.json
].freeze

CONFIG = {
  "P29" => {
    slug: "29-bianchi-ideal-owner-refinement", request_track: "P29_P32", expected_ops: 31,
    base: "stage4_prime_revision_round2.tex",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    supporting: {}
  },
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant", request_track: "P30_P31", expected_ops: 34,
    base: "stage4_prime_revision_round2.tex",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    supporting: {
      "matrix_regeneration_plan" => "stage4_prime_correction_round3_matrix_regeneration_plan.json"
    }
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger", request_track: "P30_P31", expected_ops: 13,
    base: "stage4_prime_revision_round2.tex",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    supporting: {
      "matrix_regeneration_plan" => "stage4_prime_correction_round3_matrix_regeneration_plan.json"
    }
  },
  "P32" => {
    slug: "32-homology-cover-renormalization-uniformity", request_track: "P29_P32", expected_ops: 15,
    base: "stage4_prime_revision_round2.tex",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    supporting: {}
  },
  "P33" => {
    slug: "33-bolza-control-matched-census", request_track: "P33", expected_ops: 37,
    base: "stage4_revision_round1.tex",
    roadmap: "stage4_prime_round6_revision_roadmap.json",
    choices: "stage4_prime_round6_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_round6_exact_confirmation_author_adjudication.json",
    claims: "stage4_prime_round6_claim_surface_manifest.json",
    patch: "stage4_prime_revision_patch_round6_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round6.json",
    handoff: "stage4_prime_round6_exact_confirmation_writer_handoff.json",
    validation: "stage4_prime_round6_exact_confirmation_writer_validation_receipt.json",
    supporting: {
      "bibliography_append_plan" => "stage4_prime_round6_bibliography_append_plan.json",
      "prospective_bibliography_contract" => "stage4_prime_round5_correction_bibliography_prospective.json"
    }
  }
}.freeze

def require!(condition, message)
  raise "ROUND10_EXACT_EMISSION_MANIFEST_FAIL: #{message}" unless condition
end

def load_json(path)
  JSON.parse(path.read)
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def bind(relative)
  path = ROOT / relative
  require!(path.file?, "missing bound artifact #{relative}")
  {"path" => relative, "sha256" => sha(path), "bytes" => path.size}
end

def parse_blocks(text)
  text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m).to_h
end

def normalized_block_text(text)
  lines = text.gsub("\r\n", "\n").split("\n", -1)
  lines.shift while !lines.empty? && lines.first.strip.empty?
  lines.pop while !lines.empty? && lines.last.strip.empty?
  lines.join("\n")
end

def request_targets
  requests = TRACK_PATHS.transform_values { |relative| load_json(ROOT / relative) }
  out = Hash.new { |hash, key| hash[key] = {"item_order" => [], "block_order" => [], "blocks" => {}} }
  roadmap_id = ->(source_id) { source_id.start_with?("REV-") ? source_id : "REV-#{source_id}" }
  add = lambda do |paper_id, item_id, target|
    paper = out[paper_id]
    paper.fetch("item_order") << item_id unless paper.fetch("item_order").include?(item_id)
    block_id = target.fetch("block_id")
    unless paper.fetch("blocks").key?(block_id)
      paper.fetch("block_order") << block_id
      paper.fetch("blocks")[block_id] = target.fetch("expected_old_hash")
    end
    require!(paper.fetch("blocks").fetch(block_id) == target.fetch("expected_old_hash"),
             "conflicting requested old hash #{paper_id}/#{block_id}")
    require!(target.fetch("allowed_operations") == ["replace_block"],
             "non-exact requested operation #{paper_id}/#{block_id}")
  end
  requests.fetch("P29_P32").fetch("papers").each do |paper|
    paper.fetch("issues").each do |issue|
      issue.fetch("proposed_targets").each do |target|
        add.call(paper.fetch("paper_id"), roadmap_id.call(issue.fetch("issue_id")), target)
      end
    end
  end
  requests.fetch("P30_P31").fetch("papers").each do |paper|
    paper.fetch("all_requested_targets").each do |target|
      add.call(paper.fetch("paper_id"), roadmap_id.call(target.fetch("issue_id")), target)
    end
  end
  requests.fetch("P33").dig("carried_forward_exact_request", "items").each do |item|
    item.fetch("proposed_targets").each { |target| add.call("P33", item.fetch("item_id"), target) }
  end
  requests.fetch("P33").fetch("new_issue_actions").each do |action|
    action.fetch("proposed_targets").each { |target| add.call("P33", action.fetch("action_id"), target) }
  end
  out
end

require!(!OUTPUT.exist?, "refusing to overwrite #{OUTPUT.basename}")

receipt = load_json(ROOT / AUTHORITY_PATHS.fetch("authorization_receipt"))
require!(receipt.fetch("status") == "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION",
         "authorization receipt status")
require!(receipt.dig("aggregate", "papers") == 5, "authorization receipt paper count")
require!(receipt.dig("aggregate", "unique_replace_block_pairs") == 130,
         "authorization receipt operation count")
TRACK_PATHS.each do |track, relative|
  expected = bind(relative)
  actual = receipt.fetch("tracks").fetch(track)
  %w[path sha256 bytes].each do |key|
    require!(actual.fetch(key) == expected.fetch(key), "authorization receipt track drift #{track}/#{key}")
  end
end
authority = AUTHORITY_PATHS.to_h do |key, relative|
  binding = bind(relative)
  require!(binding.fetch("sha256") == AUTHORITY_SHA256.fetch(key), "authority drift #{key}")
  binding["exact_text"] = "确认\n" if key == "author_event"
  [key, binding]
end
require!((ROOT / AUTHORITY_PATHS.fetch("author_event")).binread == "确认\n".b, "author event bytes")

targets = request_targets
require!(targets.keys.sort == CONFIG.keys.sort, "request paper coverage")
require!(targets.sum { |_, row| row.fetch("blocks").length } == 130, "request target union is not 130")

papers = CONFIG.map do |paper_id, config|
  notes_relative = "papers/#{config.fetch(:slug)}/notes"
  notes = ROOT / notes_relative
  scope = targets.fetch(paper_id)
  require!(scope.fetch("blocks").length == config.fetch(:expected_ops), "#{paper_id} requested operation count")

  base_path = notes / config.fetch(:base)
  blocks = parse_blocks(base_path.read)
  expected_hash_order = if paper_id == "P33"
                          blocks.keys.select { |block_id| scope.fetch("blocks").key?(block_id) }
                        else
                          scope.fetch("block_order")
                        end
  full_old_hashes = expected_hash_order.map do |block_id|
    full = Digest::SHA256.hexdigest(normalized_block_text(blocks.fetch(block_id)))
    requested = scope.fetch("blocks").fetch(block_id)
    require!(requested == full || requested == full[0, 12], "#{paper_id}/#{block_id} request/base hash mismatch")
    {"block_id" => block_id, "sha256" => full}
  end

  artifact_names = {
    "revision_roadmap" => config.fetch(:roadmap),
    "author_choices" => config.fetch(:choices),
    "author_adjudication" => config.fetch(:adjudication),
    "claim_surface_manifest" => config.fetch(:claims),
    "patch" => config.fetch(:patch),
    "writer_handoff" => config.fetch(:handoff),
    "writer_validation" => config.fetch(:validation)
  }
  artifacts = artifact_names.transform_values { |name| bind("#{notes_relative}/#{name}") }
  prepared_patch = load_json(notes / config.fetch(:prepared_patch))
  fresh_patch = load_json(notes / config.fetch(:patch))
  require!(fresh_patch.fetch("ops") == prepared_patch.fetch("ops"), "#{paper_id} fresh ops differ from prepared ops")
  require!(fresh_patch.fetch("ops").length == config.fetch(:expected_ops), "#{paper_id} patch operation count")
  require!(fresh_patch.fetch("ops").map { |op| op.fetch("block_id") } == expected_hash_order,
           "#{paper_id} patch order differs from authorized order")

  adjudication = load_json(notes / config.fetch(:adjudication))
  item_ids = adjudication.dig("display_order", "item_ids")
  require!(item_ids == scope.fetch("item_order"), "#{paper_id} source-traceability order")
  trace_canonical = JSON.generate(item_ids).encode(Encoding::UTF_8)
  supporting = config.fetch(:supporting).transform_values { |name| bind("#{notes_relative}/#{name}") }

  {
    "paper_id" => paper_id,
    "paper_slug" => config.fetch(:slug),
    "request_track" => config.fetch(:request_track),
    "authorized_replace_block_pairs" => config.fetch(:expected_ops),
    "request" => bind(TRACK_PATHS.fetch(config.fetch(:request_track))),
    "source_traceability" => {
      "mode" => "source_traceability",
      "item_ids" => item_ids,
      "count" => item_ids.length,
      "canonicalization" => "JSON.generate(item_ids) UTF-8",
      "sha256" => Digest::SHA256.hexdigest(trace_canonical)
    },
    "full_old_hashes" => full_old_hashes,
    "artifacts" => artifacts,
    "supporting_artifacts" => supporting
  }
end

root_cross_audits = CROSS_AUDITS.map { |relative| bind(relative) }
manifest = {
  "schema_version" => SCHEMA,
  "status" => STATUS,
  "preparation_evidence_authority_role" => PREPARATION_ROLE,
  "authority" => authority,
  "aggregate" => {
    "papers" => papers.length,
    "unique_replace_block_pairs" => papers.sum { |row| row.fetch("authorized_replace_block_pairs") }
  },
  "papers" => papers,
  "root_cross_audits" => root_cross_audits
}

payload = JSON.pretty_generate(manifest) + "\n"
temporary = Pathname.new("#{OUTPUT}.tmp.#{$$}")
begin
  File.open(temporary, "wbx", 0o644) do |file|
    file.write(payload)
    file.flush
    file.fsync
  end
  begin
    File.link(temporary, OUTPUT)
  rescue Errno::EEXIST
    raise "ROUND10_EXACT_EMISSION_MANIFEST_FAIL: refusing to overwrite #{OUTPUT.basename}"
  end
  temporary.delete
ensure
  temporary.delete if temporary.exist?
end

puts "ROUND10_EXACT_EMISSION_MANIFEST_PASS: #{OUTPUT.basename} sha256=#{sha(OUTPUT)} bytes=#{OUTPUT.size} papers=5 ops=130"
