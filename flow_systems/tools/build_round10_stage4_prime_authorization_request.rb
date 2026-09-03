#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
STAMP = "2026-09-03T13:00:00Z"
OUT_JSON = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json")
OUT_MD = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md")

PAPERS = {
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    items: {
      "REV-EIC-W2-R1-W3" => {
        targets: {
          "B0059" => ["replace_block"], "B0062" => ["replace_block"],
          "B0098" => ["replace_block", "insert_after"], "B0123" => ["replace_block"]
        },
        branch: "Run a dated, bounded replay of the already frozen search strings; publish a row-level retrieval/screening ledger and a claim-to-passage matrix. Preserve unavailable original-session rows as unavailable and never backfill them as historical observations."
      },
      "REV-EIC-W3-R2-W2" => {
        targets: {"B0060" => ["replace_block"], "B0106" => ["replace_block"], "B0123" => ["replace_block"]},
        branch: "Add exactly two independently citable correction records, keys P30-C01 and P30-C02, for DOI 10.1063/1.457669 and 10.1063/1.457670, then bind P30-S01/P30-S02 and P30-S03 to the matching keys and remove only the now-resolved publication-incomplete wording."
      },
      "REV-EIC-W4" => {
        targets: {
          "B0061" => ["replace_block"], "B0064" => ["replace_block"],
          "B0067" => ["replace_block"], "B0100" => ["replace_block"]
        },
        branch: "Replace internal Stage/review vocabulary with a standalone evidence-method description. Rename the B0067 heading only; keep section order and section count unchanged. Describe same-family fresh-context assessments as role-separated, not independent."
      },
      "REV-R1-W2-R3-W2" => {
        targets: {"B0084" => ["replace_block", "insert_after"], "B0103" => ["replace_block"]},
        branch: "Freeze a=1 scale, c0=1, the order-three cyclic disk-label automorphism phi, delta=1/10 giving d=61a/10, Omega={1/2<=Re(s)<=2, |Im(s)|<=50}, and eta_c=1/100. Reclassify phi as a symmetry/invariance control and state preserved/broken properties for every control. Do not execute a comparison."
      },
      "REV-R3-W1-DA-N1" => {
        targets: {"B0088" => ["replace_block", "insert_after"], "B0090" => ["replace_block"]},
        branch: "Insert one six-row gate table that explicitly lists each gate's inputs, output, receipt, hash, uncertainty channel, downstream consumer, permission and stop state, including the Gate-6 output. No gate state is promoted."
      }
    }
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    items: {
      "REV-P31-001" => {
        targets: {"B0016" => ["replace_block"], "B0033" => ["insert_after"]},
        branch: "Run a bounded closest-work search for proof-carrying-data and ledger-verification methods, add only source-verified records, distinguish inherited components from the project synthesis, and retain the no-priority/no-exhaustive-novelty boundary."
      },
      "REV-P31-002" => {
        targets: {"B0079" => ["replace_block"], "B0105" => ["replace_block"]},
        branch: "Use the conservative branch: remove reader-recovery claims for materials not listed, and give every retained entry its schema/version, digest and explicit repository-relative access state; make no persistent-archive claim."
      },
      "REV-P31-004" => {
        targets: {"B0046" => ["replace_block"], "B0050" => ["replace_block"], "B0051" => ["replace_block"]},
        branch: "Reserve totality for delta:X->OwnerDisposition; define kappa only on X_res and make every owner-map theorem require X_res=X. Keep the biconditional and G/I/C materialization under the same zero-unresolved stop condition."
      },
      "REV-P31-005" => {
        targets: {"B0015" => ["replace_block"], "B0062" => ["replace_block"]},
        branch: "Restrict the all-pairs surface to byte-level and bookkeeping consequences. Assign reflexivity to self fixtures, direction sensitivity to ordered reversals, transitivity to triples, and semantic merge/split detection only to an independent target-blind route."
      },
      "REV-P31-007" => {
        targets: {
          "B0036" => ["replace_block"], "B0037" => ["replace_block"],
          "B0038" => ["replace_block"], "B0039" => ["replace_block"],
          "B0079" => ["insert_after"], "B0089" => ["replace_block"]
        },
        branch: "Run and publish a dated row-level retrieval/screening ledger from frozen queries plus a method-component passage/hypothesis/transfer-boundary table. Preserve every unresolved passage as unresolved; do not fabricate historical screening rows."
      },
      "REV-P31-008" => {
        targets: {"B0012" => ["replace_block"], "B0049" => ["replace_block"], "B0054" => ["replace_block"]},
        branch: "Add the typed self-reciprocal branch: if subgroup self-reciprocity is certified, retain one owner_bytes value and emit inverse_relation=self_reciprocal with the witness; otherwise retain inverse-separated or unresolved dispositions. Do not assert an exclusion theorem."
      },
      "REV-P31-009" => {
        targets: {"B0067" => ["replace_block"], "B0072" => ["insert_after"]},
        branch: "Add one consolidated G/I/C relational-schema table with keys, cardinalities, materialization gate, allowed I-to-G/C projections and prohibited G/C-to-I reconstruction; retain the prose only as interpretation."
      },
      "REV-P31-011" => {
        targets: {"B0015" => ["replace_block"], "B0061" => ["replace_block"]},
        branch: "Remove the remaining semantic false-merge/false-split and nontransitivity capability claim from the introduction and bind the limitation to the absence of an independent target-blind adjudicator."
      }
    }
  }
}.freeze

def assert!(condition, message)
  raise message unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def rel(path)
  path.delete_prefix("#{ROOT}/")
end

def artifact(path)
  assert!(File.file?(path), "missing #{path}")
  {"path" => rel(path), "sha256" => sha(path), "bytes" => File.size(path)}
end

def target_text(targets)
  targets.flat_map { |block, ops| ops.map { |op| "`#{block}/#{op}`" } }.join(", ")
end

payload = {
  "schema_version" => "round10-stage4-prime-authorization-request/1.0",
  "generated_at_utc" => STAMP,
  "status" => "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION",
  "authorization_source" => artifact(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_AUTHORIZATION_RECORD.md")),
  "proposed_display_order" => "source_traceability",
  "proposed_author_triage" => "will_address",
  "papers" => [],
  "supporting_operations" => [
    {
      "operation_id" => "P30-LIT-REPLAY",
      "paper_id" => "P30",
      "allowed_operations" => ["read_frozen_queries", "run_dated_literature_retrieval", "create_screening_ledger", "create_claim_passage_matrix", "validate_hashes"],
      "forbidden" => ["fabricate_historical_rows", "change_scientific_results", "refresh_canonical_results"]
    },
    {
      "operation_id" => "P30-BIB-CORRECTIONS",
      "paper_id" => "P30",
      "path" => "papers/30-three-disk-nonconstant-roof-determinant/paper/references.bib",
      "base_sha256" => sha(File.join(ROOT, "papers/30-three-disk-nonconstant-roof-determinant/paper/references.bib")),
      "allowed_operations" => ["append_verified_entry:P30-C01:10.1063/1.457669", "append_verified_entry:P30-C02:10.1063/1.457670"],
      "maximum_new_entries" => 2
    },
    {
      "operation_id" => "P31-CLOSEST-WORK",
      "paper_id" => "P31",
      "allowed_operations" => ["run_bounded_closest_work_search", "create_source_verification_receipt", "append_source_verified_bibliography_entries"],
      "maximum_new_entries" => 4,
      "forbidden" => ["uncited_novelty_claim", "unverified_bibliography_entry", "priority_claim"]
    },
    {
      "operation_id" => "P31-LIT-REPLAY",
      "paper_id" => "P31",
      "allowed_operations" => ["read_frozen_queries", "run_dated_literature_retrieval", "create_screening_ledger", "create_method_passage_matrix", "validate_hashes"],
      "forbidden" => ["fabricate_historical_rows", "change_scientific_results", "refresh_canonical_results"]
    }
  ],
  "structural_acknowledgment_requested" => [
    {
      "paper_id" => "P30", "block_id" => "B0067", "operation" => "replace_block",
      "scope" => "heading text only; section order and section count unchanged"
    }
  ],
  "boundaries" => {
    "request_only_no_write" => true,
    "revision_patch_emitted" => false,
    "manuscripts_modified" => false,
    "bibliographies_modified" => false,
    "registered_claim_surfaces" => 0,
    "claim_strength_replacements_authorized" => false,
    "collateral_authorizations" => [],
    "scientific_execution_authorized" => false,
    "canonical_result_refresh_authorized" => false,
    "route_a_change_authorized" => false,
    "route_b_authorized" => false,
    "later_pipeline_stages_authorized" => false
  }
}

PAPERS.each do |paper_id, spec|
  paper_root = File.join(ROOT, "papers", spec.fetch(:slug))
  notes = File.join(paper_root, "notes")
  verdict_path = File.join(notes, "stage3_prime_round2_verdict_record.json")
  trace_path = File.join(notes, "stage3_prime_round2_traceability.json")
  checker_path = File.join(notes, "stage3_prime_round2_checker_receipt.json")
  draft_path = File.join(notes, "stage4_revision_round1.tex")
  manifest_path = File.join(notes, "stage4_prime_base.block-manifest.json")
  bib_path = File.join(paper_root, "paper", "references.bib")
  claim_path = File.join(notes, "stage4_claim_surface_manifest.json")
  verdict = load_json(verdict_path)
  block_manifest = load_json(manifest_path)
  block_ids = block_manifest.fetch("blocks").map { |row| row.fetch("block_id") }
  partials = verdict.fetch("items").select { |row| row.fetch("verdict") == "PARTIALLY_ADDRESSED" }

  assert!(partials.map { |row| row.fetch("item_id") } == spec.fetch(:items).keys,
          "#{paper_id}: proposed item order does not match partial rows")
  assert!(sha(draft_path).start_with?(block_manifest.fetch("base_draft_hash")), "#{paper_id}: block manifest/base drift")
  assert!(load_json(claim_path).fetch("surfaces").empty?, "#{paper_id}: registered claims unexpectedly present")

  items = partials.map do |row|
    item_id = row.fetch("item_id")
    plan = spec.fetch(:items).fetch(item_id)
    plan.fetch(:targets).each_key { |block| assert!(block_ids.include?(block), "#{paper_id}: unknown target #{block}") }
    {
      "item_id" => item_id,
      "phase2a_verdict" => row.fetch("verdict"),
      "residual_obligation_class" => row.dig("residual_gap", "residual_obligation_class"),
      "residual_gap" => row.dig("residual_gap", "text"),
      "proposed_author_triage" => "will_address",
      "proposed_targets" => plan.fetch(:targets).map { |block, ops| {"block_id" => block, "allowed_operations" => ops} },
      "implementation_branch" => plan.fetch(:branch)
    }
  end

  payload["papers"] << {
    "paper_id" => paper_id,
    "paper_slug" => spec.fetch(:slug),
    "stage3_prime_round2_verdict_record" => artifact(verdict_path),
    "stage3_prime_round2_traceability" => artifact(trace_path),
    "stage3_prime_round2_checker_receipt" => artifact(checker_path),
    "stage4_prime_base_draft" => artifact(draft_path),
    "stage4_prime_block_manifest" => artifact(manifest_path),
    "bibliography" => artifact(bib_path),
    "claim_surface_manifest" => artifact(claim_path),
    "partial_items" => items.length,
    "items" => items
  }
end

assert!(!File.exist?(OUT_JSON), "refusing to overwrite #{OUT_JSON}")
assert!(!File.exist?(OUT_MD), "refusing to overwrite #{OUT_MD}")
File.write(OUT_JSON, JSON.pretty_generate(payload) + "\n")

lines = []
lines << "# Round 10 Papers 30--31 -- Stage 4′ Exact Authorization Request"
lines << ""
lines << "Date: **2026-09-03 UTC**"
lines << ""
lines << "Status: `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION`"
lines << ""
lines << "This request is preparation-only. Its creation changed no manuscript, bibliography, PDF, result, experiment, registered claim, initial system, or Route state. A later exact confirmation is required before any listed operation is executed."
lines << ""
lines << "Machine-readable request: `#{File.basename(OUT_JSON)}` (SHA-256 `#{sha(OUT_JSON)}`)."
lines << ""
lines << "## Frozen authority bindings"
lines << ""
lines << "| Paper | Stage 3′ verdict | Traceability | Checker | Stage 4′ base draft | Block manifest | Bibliography |"
lines << "|---|---|---|---|---|---|---|"
payload.fetch("papers").each do |paper|
  lines << "| #{paper.fetch('paper_id')} | `#{paper.dig('stage3_prime_round2_verdict_record', 'sha256')}` | `#{paper.dig('stage3_prime_round2_traceability', 'sha256')}` | `#{paper.dig('stage3_prime_round2_checker_receipt', 'sha256')}` | `#{paper.dig('stage4_prime_base_draft', 'sha256')}` | `#{paper.dig('stage4_prime_block_manifest', 'sha256')}` | `#{paper.dig('bibliography', 'sha256')}` |"
end
lines << ""
payload.fetch("papers").each do |paper|
  lines << "## #{paper.fetch('paper_id')} -- #{paper.fetch('partial_items')} residual items"
  lines << ""
  lines << "| Item | Residual class | Exact proposed target/operation set |"
  lines << "|---|---|---|"
  paper.fetch("items").each do |item|
    targets = item.fetch("proposed_targets").to_h { |target| [target.fetch("block_id"), target.fetch("allowed_operations")] }
    lines << "| `#{item.fetch('item_id')}` | `#{item.fetch('residual_obligation_class')}` | #{target_text(targets)} |"
  end
  lines << ""
  lines << "Implementation branches:"
  lines << ""
  paper.fetch("items").each do |item|
    lines << "- `#{item.fetch('item_id')}`: #{item.fetch('implementation_branch')}"
  end
  lines << ""
end
lines << "## Supporting and exceptional scopes requested"
lines << ""
lines << "- P30 literature replay: dated retrieval/screening ledger plus claim-to-passage matrix; historical gaps remain visibly unavailable."
lines << "- P30 bibliography: append only `P30-C01` / DOI `10.1063/1.457669` and `P30-C02` / DOI `10.1063/1.457670`, after metadata verification."
lines << "- P31 closest-work search: at most four source-verified bibliography additions for the two missing method families; no priority claim."
lines << "- P31 literature replay: dated row-level ledger and passage/hypothesis/transfer matrix; no fabricated historical rows."
lines << "- P30 structural acknowledgment: `B0067/replace_block` is limited to heading text; section order and section count must remain unchanged."
lines << ""
lines << "## Boundaries"
lines << ""
lines << "- Proposed disposition is `will_address` for all 13 residual items, in `source_traceability` order."
lines << "- No declined item, no collateral authorization, and no registered-claim replacement; both claim-surface manifests contain zero registered surfaces."
lines << "- The later patch may use a subset of an authorized target/operation set but may not broaden it."
lines << "- No scientific execution or canonical-result refresh. P30's control values are frozen modeling choices only; no comparison result is produced."
lines << "- Any source-verification failure, test failure, scientific-value change, unregistered semantic drift requiring disposition, extra bibliography record, target expansion, broader structural change, Route change, or later-stage transition stops for a new checkpoint."
lines << "- Route-A tuples and the five initial dynamical systems stay unchanged; Route B and Stages 4.5--6 remain unauthorized."
lines << ""
lines << "## Short confirmation"
lines << ""
lines << "Reply `确认` to approve this exact request and its SHA-256; any change to the request bytes requires a new confirmation."

File.write(OUT_MD, lines.join("\n") + "\n")
puts "PASS -- emitted P30/P31 Stage 4-prime request: 13 residual items; markdown sha256=#{sha(OUT_MD)}"
