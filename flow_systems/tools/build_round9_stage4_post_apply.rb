#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"

ROOT = File.expand_path("..", __dir__)
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars"
PAPERS = {
  "24" => "24-bianchi-holonomy-flow",
  "25" => "25-three-disk-scattering-flow",
  "26" => "26-level11-newform-time-change",
  "27" => "27-congruence-inverse-limit-no-go",
  "28" => "28-bolza-magnetic-flow"
}.freeze

def load_json(path)
  JSON.parse(File.binread(path))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def write_text(path, text)
  File.binwrite(path, text)
end

def pretty_json(object)
  JSON.pretty_generate(object) + "\n"
end

def assert(condition, message)
  raise message unless condition
end

def canonical_word_count(text)
  text.gsub(/<!--.*?-->/m, " ").split.length
end

def response_markdown(number, response)
  summary = response.fetch("summary")
  lines = [
    "# Paper #{number} Stage 4 response to reviewers — Round 1",
    "",
    "Date: **2026-08-30**",
    "",
    "Status: **#{summary.fetch('resolved')} RESOLVED; #{summary.fetch('limitations')} DELIBERATE LIMITATION; " \
      "#{summary.fetch('unresolvable')} UNRESOLVABLE; #{summary.fetch('disagreed')} DISAGREED**",
    ""
  ]
  response.fetch("items").each do |item|
    lines.concat([
      "## #{item.fetch('roadmap_item_id')}",
      "",
      "**Reviewer comment.** #{item.fetch('reviewer_comment')}",
      "",
      "**Response.** #{item.fetch('author_response')}",
      "",
      "**Location.** #{item.fetch('change_location')}",
      "",
      "**Anchored blocks.** #{item.fetch('change_block_ids').empty? ? 'No manuscript operation required.' : item.fetch('change_block_ids').map { |id| "`#{id}`" }.join(', ')}",
      "",
      "**Status.** `#{item.fetch('status')}`",
      ""
    ])
  end
  lines.concat([
    "## Round summary",
    "",
    "- Resolved: #{response.fetch('summary').fetch('resolved')}",
    "- Deliberate limitations: #{response.fetch('summary').fetch('limitations')}",
    "- Unresolvable: #{response.fetch('summary').fetch('unresolvable')}",
    "- Reviewer disagreements: #{response.fetch('summary').fetch('disagreed')}",
    "- Canonical word-count delta: #{format('%+d', response.fetch('word_count_delta'))}",
    "- New bibliography entries: #{response.fetch('new_references_added')}",
    "",
    response.fetch("summary_of_changes"),
    "",
    "New-content highlights:",
    ""
  ])
  response.fetch("new_content_highlight").each { |row| lines << "- #{row}" }
  lines.join("\n") + "\n"
end

def build(number, directory)
  paper_root = File.join(ROOT, "papers", directory)
  notes = File.join(paper_root, "notes")
  base_path = File.join(notes, "stage3_revision_base.tex")
  base_manifest_path = File.join(notes, "stage3_revision_base.block-manifest.json")
  roadmap_path = File.join(notes, "stage3_revision_roadmap.json")
  claims_path = File.join(notes, "stage4_claim_surface_manifest.json")
  adjudication_path = File.join(notes, "stage4_author_adjudication.json")
  integrity_path = File.join(notes, "stage4_integrity_pass_receipt.json")
  patch_path = File.join(notes, "stage4_revision_patch_round1.json")
  provisional_path = File.join(notes, "stage4_response_to_reviewers_provisional.json")
  revised_path = File.join(notes, "stage4_revision_round1.tex")
  report_path = revised_path + ".apply-report.json"
  required = [base_path, base_manifest_path, roadmap_path, claims_path,
              adjudication_path, integrity_path, patch_path, provisional_path,
              revised_path, report_path]
  required.each { |path| assert(File.file?(path), "P#{number}: missing #{path}") }

  roadmap = load_json(roadmap_path)
  adjudication = load_json(adjudication_path)
  claims = load_json(claims_path)
  provisional = load_json(provisional_path)
  report = load_json(report_path)
  base_text = File.binread(base_path).force_encoding("UTF-8")
  revised_text = File.binread(revised_path).force_encoding("UTF-8")

  assert(report.dig("authorization_witness", "status") == "pass", "P#{number}: apply authorization did not pass")
  assert(report.dig("structural_flags", "any") == false, "P#{number}: structural checkpoint required")
  assert(report.fetch("patch_digest") == sha256(patch_path), "P#{number}: apply report/patch mismatch")
  assert(report.fetch("base_draft_hash") == sha256(base_path)[0, 12], "P#{number}: report/base mismatch")
  assert(report.fetch("output_draft_hash") == sha256(revised_path)[0, 12], "P#{number}: report/output mismatch")

  claim_rows = claims.fetch("surfaces").map do |surface|
    original = surface.fetch("original_text")
    count = revised_text.scan(Regexp.new(Regexp.escape(original))).length
    assert(count == 1, "P#{number}: #{surface.fetch('surface_id')} occurs #{count} times")
    {
      "surface_id" => surface.fetch("surface_id"),
      "claim_id" => surface.fetch("claim_id"),
      "block_id" => surface.fetch("block_id"),
      "original_text_sha256" => surface.fetch("original_text_sha256"),
      "occurrences_in_revised_draft" => count,
      "status" => "BYTE_EXACT_ONCE"
    }
  end
  claim_replay = {
    "schema" => "round9-stage4-registered-claim-surface-replay/1.0",
    "paper_number" => number.to_i,
    "revision_round" => 1,
    "claim_surface_manifest_sha256" => sha256(claims_path),
    "revised_draft_sha256" => sha256(revised_path),
    "registered_surface_count" => claim_rows.length,
    "all_byte_exact_once" => true,
    "surfaces" => claim_rows
  }
  write_text(File.join(notes, "stage4_registered_claim_surface_replay.json"), pretty_json(claim_replay))

  changes = Hash.new { |hash, key| hash[key] = [] }
  report.fetch("ops_applied").each do |op|
    ids = [op.fetch("block_id"), *op.fetch("new_block_ids")]
    op.fetch("roadmap_item_ids").each do |item_id|
      ids.each { |id| changes[item_id] << id unless changes[item_id].include?(id) }
    end
  end
  expected_order = adjudication.fetch("display_order").fetch("item_ids")
  provisional_items = provisional.fetch("items")
  assert(provisional_items.map { |item| item.fetch("roadmap_item_id") } == expected_order,
         "P#{number}: provisional response item order mismatch")
  final_items = provisional_items.map do |item|
    assert(!item.fetch("author_response").match?(/\bwould\b/i),
           "P#{number}: provisional response is not finalization-ready for #{item.fetch('roadmap_item_id')}")
    {
      "roadmap_item_id" => item.fetch("roadmap_item_id"),
      "reviewer_comment" => item.fetch("reviewer_comment"),
      "author_response" => item.fetch("author_response"),
      "change_location" => item.fetch("change_location"),
      "change_block_ids" => changes[item.fetch("roadmap_item_id")],
      "status" => item.fetch("status")
    }
  end
  delta = canonical_word_count(revised_text) - canonical_word_count(base_text)
  response = {
    "revision_round" => 1,
    "items" => final_items,
    "summary" => provisional.fetch("summary"),
    "word_count_delta" => delta,
    "new_references_added" => provisional.fetch("new_references_added"),
    "summary_of_changes" => provisional.fetch("summary_of_changes"),
    "new_content_highlight" => provisional["new_content_highlight"] || final_items.map do |item|
      "#{item.fetch('roadmap_item_id')}: #{item.fetch('change_location')}"
    end
  }
  disposition_total = %w[resolved limitations unresolvable disagreed].sum do |key|
    response.fetch("summary").fetch(key)
  end
  assert(disposition_total == expected_order.length, "P#{number}: response disposition total mismatch")
  write_text(File.join(notes, "stage4_response_to_reviewers_round1.json"), pretty_json(response))
  write_text(File.join(notes, "stage4_response_to_reviewers_round1.md"), response_markdown(number, response))

  bundle = {
    "schema_version" => "revision-evidence-bundle/1.0",
    "chain_start" => {
      "first_revision_round" => 1,
      "draft" => {"path" => "notes/stage3_revision_base.tex", "sha256" => sha256(base_path)},
      "block_manifest" => {"path" => "notes/stage3_revision_base.block-manifest.json", "sha256" => sha256(base_manifest_path)},
      "integrity_pass_receipt" => {"path" => "notes/stage4_integrity_pass_receipt.json", "sha256" => sha256(integrity_path)}
    },
    "rounds" => [
      {
        "kind" => "review_roadmap",
        "revision_round" => 1,
        "pre_round_draft" => {"path" => "notes/stage3_revision_base.tex", "sha256" => sha256(base_path)},
        "pre_round_block_manifest" => {"path" => "notes/stage3_revision_base.block-manifest.json", "sha256" => sha256(base_manifest_path)},
        "revision_roadmap" => {"path" => "notes/stage3_revision_roadmap.json", "sha256" => sha256(roadmap_path)},
        "claim_surface_manifest" => {"path" => "notes/stage4_claim_surface_manifest.json", "sha256" => sha256(claims_path)},
        "author_adjudication" => {"path" => "notes/stage4_author_adjudication.json", "sha256" => sha256(adjudication_path)},
        "revision_patch" => {"path" => "notes/stage4_revision_patch_round1.json", "sha256" => sha256(patch_path)},
        "apply_report" => {"path" => "notes/stage4_revision_round1.tex.apply-report.json", "sha256" => sha256(report_path)},
        "post_round_draft" => {"path" => "notes/stage4_revision_round1.tex", "sha256" => sha256(revised_path)}
      }
    ],
    "final_draft" => {"path" => "notes/stage4_revision_round1.tex", "sha256" => sha256(revised_path)}
  }
  bundle_path = File.join(notes, "stage4_revision_evidence_bundle.json")
  write_text(bundle_path, pretty_json(bundle))

  token_command = [
    "python", File.join(ARS_ROOT, "scripts/check_revision_token_conservation.py"), "patch",
    "--patch", patch_path, "--base", base_path
  ]
  token_stdout, token_stderr, token_status = Open3.capture3(*token_command)
  assert(token_status.success?, "P#{number}: token audit failed: #{token_stderr}")
  token_object = JSON.parse(token_stdout)
  write_text(File.join(notes, "stage4_token_conservation_round1.json"), pretty_json(token_object))

  roadmap_by_id = roadmap.fetch("items").to_h { |item| [item.fetch("id"), item] }
  log = [
    "# Paper #{number} Stage 4 revision log — Round 1",
    "",
    "Date: **2026-08-30**",
    "",
    "| Item | Severity | Obligation | Author triage | Landed anchored blocks |",
    "|---|---|---|---|---|"
  ]
  expected_order.each do |item_id|
    item = roadmap_by_id.fetch(item_id)
    landed = changes[item_id].empty? ? "No manuscript operation required" : changes[item_id].map { |id| "`#{id}`" }.join(", ")
    log << "| `#{item_id}` | #{item.fetch('severity')} | `#{item.fetch('obligation_class')}` | `will_address` | #{landed} |"
  end
  log.concat([
    "",
    "## Mechanical receipt",
    "",
    "- Patch SHA-256: `#{sha256(patch_path)}`",
    "- Revised anchored draft SHA-256: `#{sha256(revised_path)}`",
    "- Apply-report SHA-256: `#{sha256(report_path)}`",
    "- Evidence-bundle SHA-256: `#{sha256(bundle_path)}`",
    "- Canonical word-count delta: `#{format('%+d', delta)}`",
    "- New bibliography entries: `#{response.fetch('new_references_added')}`",
    "- Registered surfaces replayed byte-exact once: `#{claim_rows.length}/#{claim_rows.length}`",
    "- Structural flags: `false`",
    "- Route-A tuple changed: `false`",
    "- Route B invoked: `false`",
    "- Canonical results refreshed: `false`",
    ""
  ])
  write_text(File.join(notes, "stage4_revision_log_round1.md"), log.join("\n"))

  puts "P#{number}: post-apply artifacts built; words #{canonical_word_count(base_text)} -> #{canonical_word_count(revised_text)} (#{format('%+d', delta)}); claims #{claim_rows.length}/#{claim_rows.length}"
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
