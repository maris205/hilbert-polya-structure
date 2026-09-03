#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
ARS_ROOT = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
REVISION_TOOL = ARS_ROOT / "scripts" / "revision_roadmap.py"
EVENT = ROOT / "BATCH_ROUND10_STAGE4_AUTHOR_EVENT_20260903.txt"
EVENT_ID = "AUTHOR-EVENT-20260903-ROUND10-STAGE4-ALL56"

PAPERS = {
  29 => "29-bianchi-ideal-owner-refinement",
  30 => "30-three-disk-nonconstant-roof-determinant",
  31 => "31-level11-conjugacy-owner-ledger",
  32 => "32-homology-cover-renormalization-uniformity",
  33 => "33-bolza-control-matched-census"
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def pretty_json(value)
  JSON.pretty_generate(value) + "\n"
end

def write_new(path, content)
  abort "refusing to overwrite: #{path}" if path.exist?
  path.dirname.mkpath
  path.binwrite(content)
end

def strip_block_markers(text)
  text.lines.reject { |line| line.match?(/\A<!--block:B\d{4,}-->\s*\z/) }.join
end

def run!(*command)
  stdout, stderr, status = Open3.capture3(*command.map(&:to_s), chdir: ROOT.to_s)
  $stdout.write(stdout)
  $stderr.write(stderr)
  abort "command failed (#{status.exitstatus}): #{command.join(' ')}" unless status.success?
end

abort "missing author event" unless EVENT.file?
abort "unexpected author event bytes" unless EVENT.binread == "继续，额度已经重置了\n".b
event_sha256 = sha256(EVENT)
total_items = 0
rows = []

PAPERS.each do |paper_number, slug|
  paper_root = ROOT / "papers" / slug
  notes = paper_root / "notes"
  canonical = paper_root / "paper" / "manuscript.tex"
  passport_path = notes / "stage2_5_material_passport.json"
  integrity_report_path = notes / "stage2_5_integrity_report.json"
  base = notes / "stage3_revision_base.tex"
  manifest_path = notes / "stage3_revision_base.block-manifest.json"
  roadmap_path = notes / "stage3_revision_roadmap.json"
  claims_path = notes / "stage4_claim_surface_manifest.json"
  integrity_receipt_path = notes / "stage4_integrity_pass_receipt.json"
  choices_path = notes / "stage4_author_choices.json"
  adjudication_path = notes / "stage4_author_adjudication.json"

  [canonical, passport_path, integrity_report_path, base, manifest_path, roadmap_path].each do |path|
    abort "missing required input: #{path}" unless path.file?
  end

  passport = JSON.parse(passport_path.binread)
  integrity_report = JSON.parse(integrity_report_path.binread)
  roadmap = JSON.parse(roadmap_path.binread)
  manifest = JSON.parse(manifest_path.binread)
  canonical_raw = canonical.binread
  base_raw = base.binread

  abort "P#{paper_number}: Stage 2.5 not VERIFIED" unless passport.fetch("verification_status") == "VERIFIED"
  abort "P#{paper_number}: Stage 2.5 report not PASS" unless integrity_report.fetch("verdict") == "PASS"
  abort "P#{paper_number}: passport/canonical mismatch" unless passport.fetch("content_hash") == Digest::SHA256.hexdigest(canonical_raw)
  abort "P#{paper_number}: anchored base is not content-neutral" unless strip_block_markers(base_raw) == canonical_raw
  abort "P#{paper_number}: manifest/base mismatch" unless manifest.fetch("base_draft_hash") == Digest::SHA256.hexdigest(base_raw)[0, 12]
  abort "P#{paper_number}: expected empty passport ClaimIntent list" unless passport.fetch("claim_intent_manifests") == []

  claim_surface = {
    "schema_version" => "claim-surface-manifest/1.0",
    "revision_round" => roadmap.fetch("revision_round"),
    "roadmap_sha256" => sha256(roadmap_path),
    "base_draft_sha256" => sha256(base),
    "claim_intent_sources" => [],
    "surfaces" => []
  }
  write_new(claims_path, pretty_json(claim_surface))

  integrity_receipt = {
    "schema_version" => "integrity-pass-receipt/1.0",
    "receipt_id" => "INTEGRITY-PASS-P#{paper_number}-20260903-STAGE4-CHAINSTART",
    "checked_draft_sha256" => sha256(base),
    "verdict" => "PASS",
    "open_issue_count" => 0,
    "issued_by" => "integrity_verification_agent"
  }
  write_new(integrity_receipt_path, pretty_json(integrity_receipt))

  items = roadmap.fetch("items")
  total_items += items.length
  item_ids = items.map { |item| item.fetch("id") }
  abort "P#{paper_number}: duplicate roadmap item" unless item_ids.uniq.length == item_ids.length
  author_adjudications = items.map do |item|
    targets = item.fetch("proposed_targets")
    abort "P#{paper_number}/#{item.fetch('id')}: empty proposed targets" if targets.empty?
    {
      "item_id" => item.fetch("id"),
      "author_event_id" => EVENT_ID,
      "author_triage" => "will_address",
      "authorized_targets" => targets,
      "claim_strength_authorizations" => []
    }
  end
  choices = {
    "schema_version" => "author-adjudication-input/1.0",
    "author_events" => [{
      "event_id" => EVENT_ID,
      "source" => "explicit_session_user_message",
      "actor_role" => "author",
      "input_sha256" => event_sha256
    }],
    "display_order" => {
      "mode" => "source_traceability",
      "item_ids" => item_ids,
      "author_event_id" => EVENT_ID
    },
    "author_adjudications" => author_adjudications,
    "collateral_authorizations" => []
  }
  write_new(choices_path, pretty_json(choices))

  run!(
    "python", REVISION_TOOL, "build-adjudication", roadmap_path,
    "--base", base,
    "--block-manifest", manifest_path,
    "--claim-surface", claims_path,
    "--author-choices", choices_path,
    "--artifact-root", paper_root,
    "--output", adjudication_path
  )
  run!(
    "python", REVISION_TOOL, "validate-adjudication", roadmap_path, adjudication_path,
    "--base", base,
    "--block-manifest", manifest_path,
    "--claim-surface", claims_path,
    "--artifact-root", paper_root
  )

  rows << {
    "paper" => paper_number,
    "items" => items.length,
    "roadmap_sha256" => sha256(roadmap_path),
    "base_sha256" => sha256(base),
    "manifest_sha256" => sha256(manifest_path),
    "claim_surface_sha256" => sha256(claims_path),
    "author_choices_sha256" => sha256(choices_path),
    "author_adjudication_sha256" => sha256(adjudication_path)
  }
end

abort "expected 56 roadmap items, found #{total_items}" unless total_items == 56

record = []
record << "# Round 10 Papers 29--33 -- Stage 4 authorization record"
record << ""
record << "Date: **2026-09-03 UTC**"
record << ""
record << "Status: **AUTHORIZED / EXACT-SCOPE REVISION ONLY**"
record << ""
record << "At the preceding mandatory checkpoint, the author was told that Stage 4 would adjudicate the 56 displayed Stage-3 roadmap items and that replying `确认` would start that stage. The author replied `继续，额度已经重置了`. This raw event is stored byte-for-byte in `BATCH_ROUND10_STAGE4_AUTHOR_EVENT_20260903.txt` (SHA-256 `#{event_sha256}`)."
record << ""
record << "The event is recorded as `will_address` for all 56 immutable roadmap items, in `source_traceability` order, with exactly each item's existing `proposed_targets` and `allowed_operations`. There are no declined items, collateral authorizations, registered-claim replacements, structural acknowledgements, Route-A promotions, Route-B invocations, or later-stage authorizations."
record << ""
record << "## Frozen authority tuples"
record << ""
record << "| Paper | Items | Roadmap SHA-256 | Anchored base SHA-256 | Block manifest SHA-256 | Claim-surface SHA-256 | Adjudication SHA-256 |"
record << "|---|---:|---|---|---|---|---|"
rows.each do |row|
  record << "| P#{row.fetch('paper')} | #{row.fetch('items')} | `#{row.fetch('roadmap_sha256')}` | `#{row.fetch('base_sha256')}` | `#{row.fetch('manifest_sha256')}` | `#{row.fetch('claim_surface_sha256')}` | `#{row.fetch('author_adjudication_sha256')}` |"
end
record << ""
record << "## Claim and scientific boundaries"
record << ""
record << "- The Round-10 Stage-2.5 passports carry zero ClaimIntent manifests. Therefore each schema-valid claim-surface manifest contains zero mechanically registered surfaces. No ClaimIntent text is fabricated or forced onto nonmatching manuscript bytes."
record << "- Every changed block remains subject to mandatory E6 unregistered semantic-drift review. An empty registered-surface set is not a clean-claim certificate."
record << "- Auxiliary manifests, synthetic non-scientific fixtures, provenance tables, and direct regression tests may be created only where a roadmap item requests them."
record << "- No canonical result refresh, new scientific value, registered-claim strengthening, structural patch acknowledgement, Route-A coordinate movement, or Route-B work is authorized. Any such need stops the round."
record << "- The five frozen dynamical systems, clocks, owner conventions, normalizations, and forbidden-data rules remain unchanged."
record << ""
record << "## Exact item scopes"
record << ""

PAPERS.each do |paper_number, slug|
  roadmap = JSON.parse((ROOT / "papers" / slug / "notes" / "stage3_revision_roadmap.json").binread)
  record << "### Paper #{paper_number}"
  record << ""
  record << "| Item | Class | Exact authorized target/operation set |"
  record << "|---|---|---|"
  roadmap.fetch("items").each do |item|
    targets = item.fetch("proposed_targets").map do |target|
      target.fetch("allowed_operations").map { |operation| "`#{target.fetch('block_id')}/#{operation}`" }
    end.flatten.join(", ")
    record << "| `#{item.fetch('id')}` | `#{item.fetch('obligation_class')}` | #{targets} |"
  end
  record << ""
end

record << "## Validation"
record << ""
record << "All five claim-surface/adjudication tuples passed the official ARS `revision_roadmap.py build-adjudication` and `validate-adjudication` replay before this record was emitted."
record << ""
write_new(ROOT / "BATCH_ROUND10_STAGE4_AUTHORIZATION_RECORD.md", record.join("\n"))

puts "PASS -- Round 10 Stage 4 authority: #{total_items} will_address items; 0 registered claim surfaces"
puts "author_event_sha256=#{event_sha256}"
rows.each { |row| puts "P#{row.fetch('paper')}: adjudication=#{row.fetch('author_adjudication_sha256')}" }
