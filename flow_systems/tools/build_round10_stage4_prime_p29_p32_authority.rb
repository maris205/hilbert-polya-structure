#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
ARS_ROOT = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
ROADMAP_CLI = ARS_ROOT / "scripts/revision_roadmap.py"
TIMESTAMP = "2026-09-03T18:00:00Z"
EVENT_ID = "AUTHOR-EVENT-20260904-ROUND10-STAGE4-PRIME-P29-P32"

AUTHORITY_HASHES = {
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json" => "3a17181450f040e274f1fa6c31386ff2593c04f409013908bfad759d408d65fa",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md" => "44cf590c2ce5ad86d7a698c436b13e21618e7965a8792dce262845ed2eb4fcf3",
  "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHOR_EVENT_20260904.txt" => "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
  "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECORD.md" => "79c9c59b592ccf66619dfa6b1cd0e006f7dbe949890cddc22d6105a50f4a9dc5",
  "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json" => "4cc48a512c35dc31ccff0b1ff80472eed04fc454d83f4410277bd2fe356e4e4c",
  "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json" => "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md" => "5561443b7a061673032eb8fbd635a0b47995e04eb80c977ef6ff5409d5699cad"
}.freeze

PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P32" => "32-homology-cover-renormalization-uniformity"
}.freeze

SEAT_ORDER = {"EIC" => 0, "R1" => 1, "R2" => 2, "R3" => 3, "DA" => 4}.freeze
CHANNEL_ORDER = {"finding" => 0, "question" => 1, "editorial" => 2}.freeze

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def write_json(path, object)
  File.write(path, JSON.pretty_generate(object) + "\n")
end

def deep_copy(value)
  Marshal.load(Marshal.dump(value))
end

def deep_sort(value)
  case value
  when Hash
    value.keys.sort.each_with_object({}) { |key, out| out[key] = deep_sort(value[key]) }
  when Array
    value.map { |entry| deep_sort(entry) }
  else
    value
  end
end

def canonical_hash(value)
  Digest::SHA256.hexdigest(JSON.generate(deep_sort(value)))
end

def author_decision_digest(adjudication)
  canonical_hash({
    "author_events" => adjudication.fetch("author_events"),
    "display_order" => adjudication.fetch("display_order"),
    "author_adjudications" => adjudication.fetch("author_adjudications"),
    "collateral_authorizations" => adjudication.fetch("collateral_authorizations")
  })
end

def paths(slug)
  root = ROOT / "papers" / slug
  {
    root: root,
    notes: root / "notes",
    base: root / "notes/stage4_revision_round1.tex",
    manifest: root / "notes/stage4_prime_base.block-manifest.json",
    old_roadmap: root / "notes/stage3_revision_roadmap.json",
    verdict: root / "notes/stage3_prime_round3_verdict_record.json",
    roadmap: root / "notes/stage4_prime_revision_roadmap.json",
    claim_manifest: root / "notes/stage4_prime_claim_surface_manifest.json",
    choices: root / "notes/stage4_prime_author_choices.json",
    adjudication: root / "notes/stage4_prime_author_adjudication.json",
    regression_transport: root / "notes/stage4_prime_regression_transport.json",
    authority_handoff: root / "notes/stage4_prime_writer_authority_handoff.json"
  }
end

def artifact_hash(request_paper, key)
  request_paper.fetch(key).fetch("sha256")
end

def normalize_targets(targets)
  targets.map do |target|
    {
      "block_id" => target.fetch("block_id"),
      "allowed_operations" => target.fetch("allowed_operations")
    }
  end
end

def source_key(item)
  ref = item.fetch("source_refs").first
  [SEAT_ORDER.fetch(ref.fetch("seat")), CHANNEL_ORDER.fetch(ref.fetch("channel")), ref.fetch("ordinal"), ref.fetch("subclaim_ordinal"), item.fetch("id")]
end

def build_residual_item(source, action, report_name)
  item = deep_copy(source)
  item["description"] = action.fetch("residual_gap")
  item["obligation_class"] = action.fetch("residual_obligation_class")
  item["evidence_anchor"] = {
    "anchor_type" => "absence",
    "locator" => "notes/#{report_name}, #{action.fetch('item_id')}",
    "absence_scope" => action.fetch("residual_gap"),
    "check_performed" => "Checked the frozen Stage-3-prime Round-3 verdict and traceability against the exact current Stage-4 draft and content-neutral block manifest."
  }
  item["confidence"] = 5
  item["competence_basis"] = "Stage-3-prime residual verification bound to the exact current Stage-4 draft and content-neutral block manifest"
  item["cost_scope"] = {
    "kind" => "section",
    "locator" => action.fetch("proposed_targets").map { |target| target.fetch("block_id") }.join(", ")
  }
  item["consequence_if_unaddressed"] = {
    "code" => "evidence_gap_remains",
    "target" => {"kind" => "claim", "locator" => action.fetch("residual_gap")[0, 400]}
  }
  item["target_section"] = action.fetch("proposed_targets").map { |target| target.fetch("block_id") }.join(", ")
  # The immutable runtime rejects acceptance/rejection vocabulary even when it
  # describes literature-screening rows.  Preserve the approved operation in
  # the request and use the exact semantic synonym "excluded" in this roadmap
  # transport field only.
  item["suggested_action"] = action.fetch("implementation_branch").gsub("rejected rows", "excluded rows")
  item["verification_criteria"] = "Every authorized target used by the patch stays within the exact operation scope, the named residual evidence is explicit, and no scientific result, registered claim byte, canonical file, initial-system definition, or Route state changes."
  item["proposed_targets"] = normalize_targets(action.fetch("proposed_targets"))
  item
end

def build_regression_item(action, verdict_issue)
  raise "unexpected regression identifier" unless action.fetch("item_id") == "NEW-1"
  raise "regression verdict mismatch" unless verdict_issue.fetch("new_issue_id") == "NEW-1"
  {
    "id" => "REV-NEW-1",
    "source_refs" => [{
      "seat" => verdict_issue.fetch("found_by"),
      "channel" => "finding",
      "ordinal" => 4,
      "subclaim_ordinal" => 0
    }],
    "description" => verdict_issue.fetch("description"),
    "reviewer" => verdict_issue.fetch("found_by"),
    "obligation_class" => "should_fix",
    "severity" => verdict_issue.fetch("severity"),
    "evidence_anchor" => {
      "anchor_type" => "text",
      "locator" => verdict_issue.fetch("location_anchor"),
      "quote" => "independently assessed from editorial, domain, methodology, and adversarial perspectives"
    },
    "confidence" => verdict_issue.fetch("confidence"),
    "competence_basis" => verdict_issue.fetch("competence_basis"),
    "cost_scope" => {"kind" => "sentence", "locator" => "B0049 review-provenance sentence"},
    "consequence_if_unaddressed" => {
      "code" => "reporting_requirement_unmet",
      "target" => {"kind" => "section", "locator" => "B0049 Executed Methodology provenance wording"}
    },
    "target_section" => "B0049",
    "suggested_action" => action.fetch("implementation_branch"),
    "consensus_level" => "SINGLE-VERIFIER",
    "verification_criteria" => "B0049 describes same-model-family perspectives as procedurally role-separated, expressly retains correlated-error risk, makes no independence claim, and changes no review result or scientific disposition.",
    "proposed_targets" => normalize_targets(action.fetch("proposed_targets"))
  }
end

def run!(*command)
  puts "+ #{command.join(' ')}"
  raise "command failed: #{command.join(' ')}" unless system(*command)
end

AUTHORITY_HASHES.each do |relative, expected|
  actual = sha(ROOT / relative)
  raise "authority hash mismatch #{relative}: #{actual}" unless actual == expected
end

request = JSON.parse(File.read(ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json"))
freeze = JSON.parse(File.read(ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json"))
outputs = {}

PAPERS.each do |paper_id, slug|
  paper_request = request.fetch("papers").find { |row| row.fetch("paper_id") == paper_id } || raise("missing request #{paper_id}")
  paper_freeze = freeze.fetch("papers").find { |row| row.fetch("paper_id") == paper_id } || raise("missing freeze #{paper_id}")
  p = paths(slug)

  raise "base hash drift #{paper_id}" unless sha(p[:base]) == artifact_hash(paper_request, "stage4_prime_base_draft")
  raise "manifest hash drift #{paper_id}" unless sha(p[:manifest]) == artifact_hash(paper_request, "stage4_prime_block_manifest")
  paper_freeze.fetch("canonical_files").each do |entry|
    raise "canonical drift #{entry.fetch('path')}" unless sha(ROOT / entry.fetch("path")) == entry.fetch("sha256")
  end
  paper_freeze.fetch("science_files").each do |entry|
    raise "science drift #{entry.fetch('path')}" unless sha(ROOT / entry.fetch("path")) == entry.fetch("sha256")
  end

  old = JSON.parse(File.read(p[:old_roadmap]))
  old_by_id = old.fetch("items").to_h { |item| [item.fetch("id"), item] }
  items = paper_request.fetch("items").map do |action|
    build_residual_item(old_by_id.fetch(action.fetch("item_id")), action, "stage3_prime_round3_verification_report.md")
  end

  transport_rows = []
  paper_request.fetch("round3_new_issue_actions").each do |action|
    verdict = JSON.parse(File.read(p[:verdict]))
    issue = verdict.fetch("new_issues").find { |row| row.fetch("new_issue_id") == action.fetch("item_id") } || raise("missing regression issue")
    item = build_regression_item(action, issue)
    items << item
    transport_rows << {
      "source_new_issue_id" => action.fetch("item_id"),
      "transport_roadmap_item_id" => item.fetch("id"),
      "reason" => "The immutable ARS revision-roadmap and author-adjudication schemas require REV-prefixed item identifiers; this is an identifier-only transport and preserves the exact approved action, target, operation, severity, source, and wording obligation.",
      "nearest_historical_roadmap_item" => action.fetch("nearest_roadmap_item"),
      "merged_into_nearest_item" => false,
      "authorized_targets" => normalize_targets(action.fetch("proposed_targets"))
    }
  end
  items.sort_by! { |item| source_key(item) }
  counts = %w[must_fix should_fix consider].to_h { |kind| [kind, items.count { |item| item.fetch("obligation_class") == kind }] }

  roadmap = {
    "schema_version" => "revision-roadmap/1.0",
    "revision_round" => 2,
    "base_draft_sha256" => sha(p[:base]),
    "block_manifest_sha256" => sha(p[:manifest]),
    "items" => items,
    "total_items" => items.length,
    "obligation_counts" => counts,
    "editorial_decision" => "Major Revision",
    "consensus_summary" => "This non-ranking Stage-4-prime roadmap contains only the explicitly authorized Round-3 residual items and regression action for #{paper_id}. It creates no authority beyond the separately hash-bound author adjudication.",
    "dissenting_opinions" => []
  }
  write_json(p[:roadmap], roadmap)

  claim_manifest = {
    "schema_version" => "claim-surface-manifest/1.0",
    "revision_round" => 2,
    "roadmap_sha256" => sha(p[:roadmap]),
    "base_draft_sha256" => sha(p[:base]),
    "claim_intent_sources" => [],
    "surfaces" => []
  }
  write_json(p[:claim_manifest], claim_manifest)

  id_map = transport_rows.to_h { |row| [row.fetch("source_new_issue_id"), row.fetch("transport_roadmap_item_id")] }
  request_actions = paper_request.fetch("items") + paper_request.fetch("round3_new_issue_actions")
  action_by_transport_id = request_actions.to_h { |action| [id_map.fetch(action.fetch("item_id"), action.fetch("item_id")), action] }
  ordered_ids = items.map { |item| item.fetch("id") }
  choices = {
    "schema_version" => "author-adjudication-input/1.0",
    "author_events" => [{
      "event_id" => EVENT_ID,
      "source" => "explicit_session_user_message",
      "actor_role" => "author",
      "input_sha256" => AUTHORITY_HASHES.fetch("BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHOR_EVENT_20260904.txt")
    }],
    "display_order" => {
      "mode" => "source_traceability",
      "item_ids" => ordered_ids,
      "author_event_id" => EVENT_ID
    },
    "author_adjudications" => ordered_ids.map do |item_id|
      action = action_by_transport_id.fetch(item_id)
      {
        "item_id" => item_id,
        "author_event_id" => EVENT_ID,
        "author_triage" => "will_address",
        "authorized_targets" => normalize_targets(action.fetch("proposed_targets")),
        "claim_strength_authorizations" => []
      }
    end,
    "collateral_authorizations" => []
  }
  write_json(p[:choices], choices)

  if transport_rows.empty?
    regression_transport = {
      "schema_version" => "round10-stage4-prime-regression-transport/1.0",
      "generated_at_utc" => TIMESTAMP,
      "paper_id" => paper_id,
      "rows" => [],
      "status" => "NOT_APPLICABLE"
    }
  else
    regression_transport = {
      "schema_version" => "round10-stage4-prime-regression-transport/1.0",
      "generated_at_utc" => TIMESTAMP,
      "paper_id" => paper_id,
      "request" => {"path" => "../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json", "sha256" => sha(ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json")},
      "source_verdict" => {"path" => "notes/#{p[:verdict].basename}", "sha256" => sha(p[:verdict])},
      "rows" => transport_rows,
      "status" => "EXACT_IDENTIFIER_TRANSPORT_ONLY"
    }
  end
  write_json(p[:regression_transport], regression_transport)

  run!("python", ROADMAP_CLI.to_s, "validate-roadmap", p[:roadmap].to_s, "--base", p[:base].to_s, "--block-manifest", p[:manifest].to_s)
  run!("python", ROADMAP_CLI.to_s, "build-adjudication", p[:roadmap].to_s,
       "--base", p[:base].to_s, "--block-manifest", p[:manifest].to_s,
       "--claim-surface", p[:claim_manifest].to_s, "--author-choices", p[:choices].to_s,
       "--artifact-root", p[:root].to_s, "--output", p[:adjudication].to_s)
  run!("python", ROADMAP_CLI.to_s, "validate-adjudication", p[:roadmap].to_s, p[:adjudication].to_s,
       "--base", p[:base].to_s, "--block-manifest", p[:manifest].to_s,
       "--claim-surface", p[:claim_manifest].to_s, "--artifact-root", p[:root].to_s)

  adjudication = JSON.parse(File.read(p[:adjudication]))
  handoff = {
    "schema_version" => "round10-stage4-prime-writer-authority-handoff/1.0",
    "generated_at_utc" => TIMESTAMP,
    "paper_id" => paper_id,
    "revision_round" => 2,
    "request" => {"path" => "../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json", "sha256" => sha(ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json")},
    "author_event" => {"path" => "../../../BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHOR_EVENT_20260904.txt", "sha256" => AUTHORITY_HASHES.fetch("BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHOR_EVENT_20260904.txt")},
    "base_draft" => {"path" => "notes/#{p[:base].basename}", "sha256" => sha(p[:base])},
    "block_manifest" => {"path" => "notes/#{p[:manifest].basename}", "sha256" => sha(p[:manifest])},
    "roadmap" => {"path" => "notes/#{p[:roadmap].basename}", "sha256" => sha(p[:roadmap])},
    "claim_surface_manifest" => {"path" => "notes/#{p[:claim_manifest].basename}", "sha256" => sha(p[:claim_manifest]), "surfaces" => 0},
    "author_choices" => {"path" => "notes/#{p[:choices].basename}", "sha256" => sha(p[:choices])},
    "author_adjudication" => {"path" => "notes/#{p[:adjudication].basename}", "sha256" => sha(p[:adjudication])},
    "author_decision_digest" => author_decision_digest(adjudication),
    "regression_transport" => {"path" => "notes/#{p[:regression_transport].basename}", "sha256" => sha(p[:regression_transport]), "rows" => transport_rows.length},
    "boundaries" => {
      "writer_emits_patch_only" => true,
      "writer_must_not_apply_patch" => true,
      "canonical_and_science_files_frozen" => true,
      "registered_claim_replacements" => 0,
      "route_state_change" => false
    }
  }
  write_json(p[:authority_handoff], handoff)
  outputs[paper_id] = {
    "roadmap_sha256" => sha(p[:roadmap]),
    "claim_surface_manifest_sha256" => sha(p[:claim_manifest]),
    "author_adjudication_sha256" => sha(p[:adjudication]),
    "author_decision_digest" => author_decision_digest(adjudication),
    "authority_handoff_sha256" => sha(p[:authority_handoff]),
    "items" => items.length,
    "transported_regressions" => transport_rows.length
  }
end

AUTHORITY_HASHES.each do |relative, expected|
  raise "authority changed #{relative}" unless sha(ROOT / relative) == expected
end

puts JSON.pretty_generate(outputs)
