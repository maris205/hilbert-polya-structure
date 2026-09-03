#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"

ROOT = File.expand_path("..", __dir__)
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars"
DATE = "2026-09-03"
PAPERS = {
  "29" => "29-bianchi-ideal-owner-refinement",
  "30" => "30-three-disk-nonconstant-roof-determinant",
  "31" => "31-level11-conjugacy-owner-ledger",
  "32" => "32-homology-cover-renormalization-uniformity",
  "33" => "33-bolza-control-matched-census"
}.freeze

STATUS_TO_SUMMARY = {
  "RESOLVED" => "resolved",
  "DELIBERATE_LIMITATION" => "limitations",
  "UNRESOLVABLE" => "unresolvable",
  "REVIEWER_DISAGREE" => "disagreed"
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

def marker_free_word_count(text)
  text.gsub(/<!--.*?-->/m, " ").split.length
end

def response_markdown(number, response)
  summary = response.fetch("summary")
  lines = [
    "# Paper #{number} Stage 4 response to reviewers — Round 1",
    "",
    "Date: **#{DATE}**",
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
    if item.key?("decline_justification")
      lines.concat(["**Residual limitation.** #{item.fetch('decline_justification')}", ""])
    end
  end
  lines.concat([
    "## Round summary",
    "",
    "- Resolved: #{summary.fetch('resolved')}",
    "- Deliberate limitations: #{summary.fetch('limitations')}",
    "- Unresolvable: #{summary.fetch('unresolvable')}",
    "- Reviewer disagreements: #{summary.fetch('disagreed')}",
    "- Marker-stripped word-count delta: #{format('%+d', response.fetch('word_count_delta'))}",
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
  paths = {
    base: File.join(notes, "stage3_revision_base.tex"),
    manifest: File.join(notes, "stage3_revision_base.block-manifest.json"),
    roadmap: File.join(notes, "stage3_revision_roadmap.json"),
    claims: File.join(notes, "stage4_claim_surface_manifest.json"),
    adjudication: File.join(notes, "stage4_author_adjudication.json"),
    integrity: File.join(notes, "stage4_integrity_pass_receipt.json"),
    patch: File.join(notes, "stage4_revision_patch_round1.json"),
    provisional: File.join(notes, "stage4_response_to_reviewers_provisional.json"),
    revised: File.join(notes, "stage4_revision_round1.tex")
  }
  paths[:report] = paths.fetch(:revised) + ".apply-report.json"
  paths.each_value { |path| assert(File.file?(path), "P#{number}: missing #{path}") }

  roadmap = load_json(paths.fetch(:roadmap))
  adjudication = load_json(paths.fetch(:adjudication))
  claims = load_json(paths.fetch(:claims))
  provisional = load_json(paths.fetch(:provisional))
  report = load_json(paths.fetch(:report))
  base_text = File.binread(paths.fetch(:base)).force_encoding("UTF-8")
  revised_text = File.binread(paths.fetch(:revised)).force_encoding("UTF-8")

  assert(report.dig("authorization_witness", "status") == "pass", "P#{number}: apply authorization did not pass")
  assert(report.dig("structural_flags", "any") == false, "P#{number}: structural checkpoint required")
  assert(report.dig("structural_flags", "acknowledged") == false, "P#{number}: structural acknowledgement must remain false")
  assert(report.fetch("patch_digest") == sha256(paths.fetch(:patch)), "P#{number}: apply report/patch mismatch")
  assert(report.fetch("base_draft_hash") == sha256(paths.fetch(:base))[0, 12], "P#{number}: report/base mismatch")
  assert(report.fetch("output_draft_hash") == sha256(paths.fetch(:revised))[0, 12], "P#{number}: report/output mismatch")
  assert(claims.fetch("surfaces") == [], "P#{number}: Round 10 expected zero registered ClaimIntent surfaces")

  replay = {
    "schema" => "round10-stage4-registered-claim-surface-replay/1.0",
    "paper_number" => number.to_i,
    "revision_round" => 1,
    "claim_surface_manifest_sha256" => sha256(paths.fetch(:claims)),
    "revised_draft_sha256" => sha256(paths.fetch(:revised)),
    "registered_surface_count" => 0,
    "all_byte_exact_once" => true,
    "vacuous_replay" => true,
    "clean_claim_certificate" => false,
    "unregistered_claim_drift_review_required" => true,
    "interpretation" => "No ClaimIntent surfaces were registered in the verified passport. This vacuous replay is not evidence that the manuscript has no claims; all changed prose remains subject to bounded semantic review.",
    "surfaces" => []
  }
  replay_path = File.join(notes, "stage4_registered_claim_surface_replay.json")
  write_text(replay_path, pretty_json(replay))

  changes = Hash.new { |hash, key| hash[key] = [] }
  fresh_changes = Hash.new { |hash, key| hash[key] = [] }
  report.fetch("ops_applied").each do |op|
    block_ids = [op.fetch("block_id"), *op.fetch("new_block_ids")]
    op.fetch("roadmap_item_ids").each do |item_id|
      block_ids.each { |block_id| changes[item_id] << block_id unless changes[item_id].include?(block_id) }
      op.fetch("new_block_ids").each do |block_id|
        fresh_changes[item_id] << block_id unless fresh_changes[item_id].include?(block_id)
      end
    end
  end
  expected_order = adjudication.fetch("display_order").fetch("item_ids")
  provisional_items = provisional.fetch("items")
  assert(provisional_items.map { |item| item.fetch("roadmap_item_id") } == expected_order,
         "P#{number}: provisional response item order mismatch")

  final_items = provisional_items.map do |item|
    status = item.fetch("status")
    assert(STATUS_TO_SUMMARY.key?(status), "P#{number}: invalid response status #{status}")
    assert(!item.fetch("author_response").match?(/\bwould\b/i),
           "P#{number}: response is not finalization-ready for #{item.fetch('roadmap_item_id')}")
    location = item.fetch("change_location")
    if location.include?("fresh block ID remains pending deterministic apply")
      assigned = fresh_changes.fetch(item.fetch("roadmap_item_id"))
      assert(!assigned.empty?, "P#{number}: pending fresh-block location has no applied fresh block")
      location = location.sub(
        /one insert_after operation has been emitted and the fresh block ID remains pending deterministic apply\.?/,
        "the authorized insert_after operation was applied as fresh #{assigned.length == 1 ? 'block' : 'blocks'} #{assigned.join(', ')}."
      )
    end
    if location.include?("the applicator assigns its fresh block ID")
      assigned = fresh_changes.fetch(item.fetch("roadmap_item_id"))
      assert(!assigned.empty?, "P#{number}: generic fresh-block location has no applied fresh block")
      location = location.sub(
        "the applicator assigns its fresh block ID",
        "the authorized insert_after operation was applied as fresh #{assigned.length == 1 ? 'block' : 'blocks'} #{assigned.join(', ')}"
      )
    end
    assert(!location.match?(/pending deterministic apply|NOT_APPLIED/i),
           "P#{number}: stale pre-apply wording remains for #{item.fetch('roadmap_item_id')}")
    finalized = {
      "roadmap_item_id" => item.fetch("roadmap_item_id"),
      "reviewer_comment" => item.fetch("reviewer_comment"),
      "author_response" => item.fetch("author_response"),
      "change_location" => location,
      "change_block_ids" => changes[item.fetch("roadmap_item_id")],
      "status" => status
    }
    if status != "RESOLVED"
      justification = item.fetch("decline_justification", "").strip
      assert(!justification.empty?, "P#{number}: #{item.fetch('roadmap_item_id')} lacks residual-limitation justification")
      finalized["decline_justification"] = justification
    end
    finalized
  end

  observed_summary = Hash.new(0)
  final_items.each { |item| observed_summary[STATUS_TO_SUMMARY.fetch(item.fetch("status"))] += 1 }
  summary = provisional.fetch("summary")
  %w[resolved limitations unresolvable disagreed].each do |key|
    assert(summary.fetch(key) == observed_summary[key], "P#{number}: response summary #{key} mismatch")
  end
  assert(summary.values.sum == expected_order.length, "P#{number}: response disposition total mismatch")
  delta = marker_free_word_count(revised_text) - marker_free_word_count(base_text)
  response = {
    "revision_round" => 1,
    "items" => final_items,
    "summary" => summary,
    "word_count_delta" => delta,
    "new_references_added" => provisional.fetch("new_references_added"),
    "summary_of_changes" => provisional.fetch("summary_of_changes"),
    "new_content_highlight" => provisional["new_content_highlight"] || final_items.map do |item|
      "#{item.fetch('roadmap_item_id')}: #{item.fetch('change_location')}"
    end
  }
  assert(response.fetch("new_references_added") == 0, "P#{number}: bibliography mutation was not authorized")
  response_json_path = File.join(notes, "stage4_response_to_reviewers_round1.json")
  response_md_path = File.join(notes, "stage4_response_to_reviewers_round1.md")
  write_text(response_json_path, pretty_json(response))
  write_text(response_md_path, response_markdown(number, response))

  bundle = {
    "schema_version" => "revision-evidence-bundle/1.0",
    "chain_start" => {
      "first_revision_round" => 1,
      "draft" => {"path" => "notes/stage3_revision_base.tex", "sha256" => sha256(paths.fetch(:base))},
      "block_manifest" => {"path" => "notes/stage3_revision_base.block-manifest.json", "sha256" => sha256(paths.fetch(:manifest))},
      "integrity_pass_receipt" => {"path" => "notes/stage4_integrity_pass_receipt.json", "sha256" => sha256(paths.fetch(:integrity))}
    },
    "rounds" => [
      {
        "kind" => "review_roadmap",
        "revision_round" => 1,
        "pre_round_draft" => {"path" => "notes/stage3_revision_base.tex", "sha256" => sha256(paths.fetch(:base))},
        "pre_round_block_manifest" => {"path" => "notes/stage3_revision_base.block-manifest.json", "sha256" => sha256(paths.fetch(:manifest))},
        "revision_roadmap" => {"path" => "notes/stage3_revision_roadmap.json", "sha256" => sha256(paths.fetch(:roadmap))},
        "claim_surface_manifest" => {"path" => "notes/stage4_claim_surface_manifest.json", "sha256" => sha256(paths.fetch(:claims))},
        "author_adjudication" => {"path" => "notes/stage4_author_adjudication.json", "sha256" => sha256(paths.fetch(:adjudication))},
        "revision_patch" => {"path" => "notes/stage4_revision_patch_round1.json", "sha256" => sha256(paths.fetch(:patch))},
        "apply_report" => {"path" => "notes/stage4_revision_round1.tex.apply-report.json", "sha256" => sha256(paths.fetch(:report))},
        "post_round_draft" => {"path" => "notes/stage4_revision_round1.tex", "sha256" => sha256(paths.fetch(:revised))}
      }
    ],
    "final_draft" => {"path" => "notes/stage4_revision_round1.tex", "sha256" => sha256(paths.fetch(:revised))}
  }
  bundle_path = File.join(notes, "stage4_revision_evidence_bundle.json")
  write_text(bundle_path, pretty_json(bundle))

  token_command = [
    "python", File.join(ARS_ROOT, "scripts/check_revision_token_conservation.py"), "patch",
    "--patch", paths.fetch(:patch), "--base", paths.fetch(:base)
  ]
  token_stdout, token_stderr, token_status = Open3.capture3(*token_command)
  assert(token_status.success?, "P#{number}: token audit failed: #{token_stderr}")
  token_object = JSON.parse(token_stdout)
  token_path = File.join(notes, "stage4_token_conservation_round1.json")
  write_text(token_path, pretty_json(token_object))

  bundle_command = [
    "python", File.join(ARS_ROOT, "scripts/revision_roadmap.py"),
    "validate-bundle", bundle_path, "--root", paper_root
  ]
  bundle_stdout, bundle_stderr, bundle_status = Open3.capture3(*bundle_command)
  assert(bundle_status.success?, "P#{number}: evidence-bundle validation failed: #{bundle_stderr}#{bundle_stdout}")
  bundle_receipt = {
    "schema" => "round10-stage4-bundle-validation-receipt/1.0",
    "paper_number" => number.to_i,
    "date" => DATE,
    "status" => "PASS",
    "bundle_sha256" => sha256(bundle_path),
    "command" => bundle_command,
    "stdout" => bundle_stdout,
    "stderr" => bundle_stderr
  }
  bundle_receipt_path = File.join(notes, "stage4_bundle_validation_receipt.json")
  write_text(bundle_receipt_path, pretty_json(bundle_receipt))

  roadmap_by_id = roadmap.fetch("items").to_h { |item| [item.fetch("id"), item] }
  final_by_id = final_items.to_h { |item| [item.fetch("roadmap_item_id"), item] }
  log = [
    "# Paper #{number} Stage 4 revision log — Round 1",
    "",
    "Date: **#{DATE}**",
    "",
    "| Item | Severity | Obligation | Author triage | Stage-4 disposition | Landed anchored blocks |",
    "|---|---|---|---|---|---|"
  ]
  expected_order.each do |item_id|
    item = roadmap_by_id.fetch(item_id)
    landed = changes[item_id].empty? ? "No manuscript operation required" : changes[item_id].map { |id| "`#{id}`" }.join(", ")
    log << "| `#{item_id}` | #{item.fetch('severity')} | `#{item.fetch('obligation_class')}` | `will_address` | `#{final_by_id.fetch(item_id).fetch('status')}` | #{landed} |"
  end
  log.concat([
    "",
    "## Mechanical receipt",
    "",
    "- Patch SHA-256: `#{sha256(paths.fetch(:patch))}`",
    "- Revised anchored draft SHA-256: `#{sha256(paths.fetch(:revised))}`",
    "- Apply-report SHA-256: `#{sha256(paths.fetch(:report))}`",
    "- Final response SHA-256: `#{sha256(response_json_path)}`",
    "- Evidence-bundle SHA-256: `#{sha256(bundle_path)}`",
    "- Bundle-validation receipt SHA-256: `#{sha256(bundle_receipt_path)}`",
    "- Token-conservation advisory SHA-256: `#{sha256(token_path)}`",
    "- Marker-stripped word-count delta: `#{format('%+d', delta)}`",
    "- New bibliography entries: `0`",
    "- Registered ClaimIntent surfaces replayed: `0/0` (vacuous; not a clean claim certificate)",
    "- Unregistered-claim semantic review required: `true`",
    "- Structural flags: `false`",
    "- Route-A tuple changed: `false`",
    "- Route B invoked: `false`",
    "- Canonical results refreshed: `false`",
    ""
  ])
  write_text(File.join(notes, "stage4_revision_log_round1.md"), log.join("\n"))

  puts "P#{number}: post-apply PASS; #{report.fetch('ops_applied').length} ops; " \
       "words #{marker_free_word_count(base_text)} -> #{marker_free_word_count(revised_text)} " \
       "(#{format('%+d', delta)}); response #{summary.map { |key, value| "#{key}=#{value}" }.join(', ')}; " \
       "ClaimIntent replay 0/0 (E6 required)"
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
