#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
STAMP = "2026-09-03T15:48:00Z"
OUT_JSON = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json")
OUT_MD = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md")

AUTHORITY_PATHS = [
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_AUDIT.json",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_RECEIPT.json",
  "skills/route-a-evaluator.md",
  "skills/route-b-evaluator.md"
].freeze

PAPERS = {
  "P29" => {
    slug: "29-bianchi-ideal-owner-refinement",
    items: {
      "REV-R1-1" => {
        targets: {
          "B0048" => %w[replace_block insert_after],
          "B0080" => %w[replace_block],
          "B0089" => %w[replace_block],
          "B0107" => %w[replace_block]
        },
        branch: "Run a dated, bounded replay of the frozen interfaces and exact query strings; publish a row-level retrieval/deduplication/screening ledger for the replay and a deterministic P29-S01--P29-S22 inventory-to-matrix row crosswalk. Keep the missing original-session rejected rows explicitly unavailable, label replay rows as new observations, and bind every new ledger/crosswalk artifact by path, schema, and SHA-256."
      },
      "REV-R3-1" => {
        targets: {"B0112" => %w[replace_block]},
        branch: "Replace the reader map with one complete dependency/stop map: ObjectLedger input validation; Gate Q to oriented classes and owners or a named quotient-not-certified stop; Gate M to MECHANISM_ADMISSIBLE, SPLIT_IDEAL_CODOMAIN_OBSTRUCTION, or FORMAL_MAP_REFUTED; PerformanceLedger to a valid empty/result skeleton or its named hash/freeze/reconciliation stops; and replay to pass or first-mismatch stop. Every edge remains prospective."
      },
      "REV-R3-2" => {
        targets: {"B0113" => %w[replace_block]},
        branch: "Assign a fail-closed output to each unexecuted control: owner-label permutation failure -> CONTROL_LABEL_DEPENDENCE_STOP; inversion-paired failure -> CONTROL_REPRESENTATIVE_INVARIANCE_STOP; broadened-codomain noncomparability -> CONTROL_CODOMAIN_COMPARABILITY_STOP. Retain the diagnostic/non-diagnostic interpretation and state that no control or stop has been observed."
      },
      "REV-DA-2" => {
        targets: {"B0084" => %w[replace_block insert_after]},
        branch: "Replace the scientific-usefulness wording with prospective organizational stress-test value pending implementation. Define, but do not run, one labeled synthetic fixture SF-LITERAL-01 with a frozen owner input, unordered-conjugate-pair baseline, literal-branch candidate, expected codomain-specific typed stop, and a prohibition on treating the expected disposition as performance or an all-codomain obstruction."
      }
    },
    new_issues: {
      "NEW-1" => {
        targets: {"B0049" => %w[replace_block]},
        branch: "Replace 'independently assessed' with 'assessed from procedurally role-separated, same-model-family perspectives'; state that role separation does not remove correlated-error risk and make no independence claim. No review result or scientific disposition changes."
      }
    }
  },
  "P32" => {
    slug: "32-homology-cover-renormalization-uniformity",
    items: {
      "REV-P32-EIC-W1" => {
        targets: {"B0018" => %w[replace_block insert_after]},
        branch: "Run a bounded, dated closest-work search across owner algorithms, homology-cover factors, formal coefficient objects, and compact-uniform limit programs. Name the closest works individually and add a four-component overlap/difference matrix. Source-verify every retained record; add at most four verified bibliography records under deterministic keys P32-CW01--P32-CW04; retain the bounded-search and no-priority boundary."
      },
      "REV-P32-EIC-W2" => {
        targets: {
          "B0098" => %w[replace_block insert_after],
          "B0125" => %w[replace_block]
        },
        branch: "Use a commit-pinned public repository base as the stable resolving locator. Enumerate every artifact claimed current in Section 6, not only four examples, and give each repository-relative path, full SHA-256, byte count, schema/version or explicit non-schema media type, access state, and bounded evidentiary role. Make no persistent-archive or DOI claim."
      },
      "REV-P32-EIC-W4" => {
        targets: {
          "B0049" => %w[replace_block],
          "B0128" => %w[insert_after]
        },
        branch: "Keep the main executed-method block limited to corpus capture, deduplication, screening, effect coding, synthesis, and nonexecution boundaries. Move the four role labels, same-family limitation, MAJOR_REVISION code, and author-adjudication history into a separately labeled development-provenance paragraph in the declarations; do not represent the roles as independent validation."
      },
      "REV-P32-R1-W1" => {
        targets: {
          "B0081" => %w[replace_block insert_after],
          "B0082" => %w[replace_block],
          "B0083" => %w[replace_block insert_after],
          "B0084" => %w[replace_block],
          "B0131" => %w[replace_block]
        },
        branch: "Use a self-contained formalization rather than an analogy: declare coefficient rings, exponent/owner monoids, support conditions, topology/filtration, equality, localization domains, transition maps, R_+, the separately typed R_0, scalar specialization, and singleton projections with complete domains and codomains. Add a labeled well-definedness/compatibility lemma and proof for the operations actually used. If any definition or proof does not close, retain UNDEFINED/NOT_EVALUABLE and stop; assert no global-product or recovery theorem."
      },
      "REV-P32-R1-W2" => {
        targets: {
          "B0090" => %w[replace_block insert_after],
          "B0091" => %w[replace_block]
        },
        branch: "Replace the prose registry with one complete AN-1--AN-5 table. Each row must identify the exact logarithmic summand and branch convention, owner and modulus indices, schedule/coupling, K(delta,T,R), quantified limit order, the explicit majorant obligation, the precise sum/limit or limit/limit interchange claimed, prerequisites, and current status. Preserve finite prefixes as nonconvergent diagnostics and do not assert a tail theorem."
      },
      "REV-P32-R1-W4" => {
        targets: {
          "B0044" => %w[replace_block insert_after],
          "B0047" => %w[replace_block insert_after],
          "B0109" => %w[replace_block]
        },
        branch: "Run a dated replay of the frozen search strings and publish a complete current 51-manifestation retrieval/deduplication/screening/retention ledger, explicitly distinct from unavailable historical row decisions. For every decision-bearing source use, publish a source-to-claim table with exact passage locator, hypotheses, correction state, applicability statement, and prohibited stronger transfer; unresolved or inaccessible passages remain INCONCLUSIVE."
      },
      "REV-P32-DA-M1" => {
        targets: {
          "B0060" => %w[replace_block insert_after],
          "B0066" => %w[replace_block],
          "B0072" => %w[replace_block]
        },
        branch: "Add the exact conditional scalar lemma: for ell>0, real s>0, and integer m>=2, Phi_m(s)>B(s). Prove it by x=exp(-s ell/m) in (0,1), so (1-x)^m < 1-x < 1-x^m. Apply it only conditionally to m=d after a valid higher-content factor derivation and to m=N after a valid zero-content derivation. It supplies no factor derivation, ownerwise observation, global obstruction, recovery result, or Route credit."
      }
    },
    new_issues: {}
  }
}.freeze

SUPPORTING_OPERATIONS = [
  {
    "operation_id" => "P29-DATED-LITERATURE-REPLAY",
    "paper_id" => "P29",
    "allowed_operations" => %w[read_frozen_queries run_dated_literature_retrieval create_current_row_ledger create_inventory_matrix_crosswalk create_hash_receipts],
    "forbidden" => %w[fabricate_historical_rows overwrite_frozen_source_artifacts change_scientific_results refresh_canonical_results]
  },
  {
    "operation_id" => "P32-CLOSEST-WORK",
    "paper_id" => "P32",
    "allowed_operations" => %w[run_bounded_closest_work_search create_source_verification_receipt append_source_verified_bibliography_entries create_four_component_comparison_matrix],
    "bibliography_path" => "papers/32-homology-cover-renormalization-uniformity/paper/references.bib",
    "allowed_key_prefix" => "P32-CW",
    "maximum_new_entries" => 4,
    "forbidden" => %w[priority_claim unverified_bibliography_entry overwrite_existing_entry]
  },
  {
    "operation_id" => "P32-ARTIFACT-INVENTORY",
    "paper_id" => "P32",
    "allowed_operations" => %w[resolve_commit_pinned_repository_base enumerate_claimed_current_artifacts record_schema_or_media_type record_sha256_and_bytes create_access_manifest],
    "forbidden" => %w[claim_uncreated_archive claim_unminted_persistent_identifier modify_canonical_artifact]
  },
  {
    "operation_id" => "P32-DATED-LITERATURE-REPLAY",
    "paper_id" => "P32",
    "allowed_operations" => %w[read_frozen_queries run_dated_literature_retrieval create_current_51_row_ledger adjudicate_decision_bearing_passages create_claim_passage_matrix create_hash_receipts],
    "forbidden" => %w[fabricate_historical_rows silently_upgrade_inconclusive_passage overwrite_frozen_source_artifacts]
  },
  {
    "operation_id" => "P32-FORMAL-DEFINITION-AUDIT",
    "paper_id" => "P32",
    "allowed_operations" => %w[derive_self_contained_definitions check_domain_codomain_and_topology check_transition_and_projection_compatibility create_proof_audit_receipt],
    "forbidden" => %w[import_undefined_object_by_analogy claim_global_product_theorem claim_route_credit]
  },
  {
    "operation_id" => "P32-CONDITIONAL-SCALAR-LEMMA-AUDIT",
    "paper_id" => "P32",
    "allowed_operations" => %w[verify_elementary_inequality verify_hypothesis_scope create_proof_audit_receipt],
    "forbidden" => %w[claim_factor_derivation claim_executed_owner_observation claim_global_obstruction claim_route_credit]
  }
].freeze

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
  targets.flat_map do |target|
    target.fetch("allowed_operations").map { |op| "`#{target.fetch('block_id')}/#{op}`" }
  end.join(", ")
end

payload = {
  "schema_version" => "round10-stage4-prime-authorization-request/1.1",
  "generated_at_utc" => STAMP,
  "status" => "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION",
  "authority_bindings" => AUTHORITY_PATHS.map { |path| artifact(File.join(ROOT, path)) },
  "proposed_display_order" => "source_traceability",
  "proposed_author_triage" => "will_address",
  "proposed_revision_round" => 2,
  "papers" => [],
  "supporting_operations" => SUPPORTING_OPERATIONS,
  "exact_conditional_claim_requested" => {
    "paper_id" => "P32",
    "item_id" => "REV-P32-DA-M1",
    "claim" => "For ell>0, real s>0, and integer m>=2, Phi_m(s)=(1-exp(-s ell/m))^(-m) is strictly greater than B(s)=(1-exp(-s ell))^(-1).",
    "proof_scope" => "Set x=exp(-s ell/m) in (0,1); then (1-x)^m < 1-x < 1-x^m, and take positive reciprocals.",
    "boundary" => "Conditional scalar lemma only; candidate-factor derivation, formal projection, ownerwise observation, global obstruction, recovery, and Route credit remain outside the claim."
  },
  "structural_acknowledgment_requested" => [],
  "boundaries" => {
    "request_only_no_current_manuscript_or_bibliography_write" => true,
    "revision_patch_emitted" => false,
    "manuscripts_modified" => false,
    "bibliographies_modified" => false,
    "pdfs_built_or_modified" => false,
    "registered_claim_surfaces" => 0,
    "claim_strength_replacements_authorized" => false,
    "collateral_authorizations" => [],
    "scientific_execution_performed" => false,
    "canonical_result_refresh_performed" => false,
    "route_a_change_performed" => false,
    "route_b_invoked" => false,
    "later_pipeline_stages_authorized" => false,
    "execution_requires_later_exact_confirmation" => true
  },
  "stop_conditions_for_later_execution" => [
    "a target or operation outside this request is required",
    "a registered ClaimIntent surface must change",
    "a source or passage cannot be verified but the prose would require VERIFIED support",
    "a formal definition, compatibility proof, or scalar-lemma scope does not close exactly as requested",
    "a canonical result, initial dynamical system, Route-A coordinate, or scientific value would change",
    "an apply, build, or integrity check fails beyond the contract's allowed retry",
    "Stage 4.5 or any later stage would begin"
  ]
}

PAPERS.each do |paper_id, spec|
  root = File.join(ROOT, "papers", spec.fetch(:slug))
  notes = File.join(root, "notes")
  verdict_path = File.join(notes, "stage3_prime_round3_verdict_record.json")
  trace_path = File.join(notes, "stage3_prime_round3_traceability.json")
  checker_path = File.join(notes, "stage3_prime_round3_checker_receipt.json")
  draft_path = File.join(notes, "stage4_revision_round1.tex")
  manifest_path = File.join(notes, "stage4_prime_base.block-manifest.json")
  bib_path = File.join(root, "paper", "references.bib")
  claim_path = File.join(notes, "stage4_claim_surface_manifest.json")
  response_path = File.join(notes, "stage4_response_to_reviewers_round1.json")
  evidence_path = File.join(notes, "stage4_revision_evidence_bundle.json")

  verdict = load_json(verdict_path)
  trace = load_json(trace_path)
  checker = load_json(checker_path)
  manifest = load_json(manifest_path)
  claim = load_json(claim_path)
  blocks = manifest.fetch("blocks").to_h { |row| [row.fetch("block_id"), row] }
  partials = verdict.fetch("items").select { |row| row.fetch("verdict") == "PARTIALLY_ADDRESSED" }
  partial_trace = trace.fetch("rows").select { |row| row.fetch("phase2a_verdict") == "PARTIALLY_ADDRESSED" }

  assert!(checker.fetch("checker_status") == "PASS", "#{paper_id}: checker not PASS")
  assert!(checker.fetch("decision_state") == "Major Revision", "#{paper_id}: not Major Revision")
  assert!(checker.fetch("decision_rule") == "B4", "#{paper_id}: not B4")
  assert!(partials.map { |row| row.fetch("item_id") } == spec.fetch(:items).keys, "#{paper_id}: item order mismatch")
  assert!(partial_trace.map { |row| row.fetch("item_id") } == spec.fetch(:items).keys, "#{paper_id}: traceability order mismatch")
  assert!(sha(draft_path).start_with?(manifest.fetch("base_draft_hash")), "#{paper_id}: block manifest/base drift")
  assert!(claim.fetch("surfaces").empty?, "#{paper_id}: registered claims unexpectedly present")

  items = partials.map do |row|
    id = row.fetch("item_id")
    source_trace = partial_trace.find { |candidate| candidate.fetch("item_id") == id }
    plan = spec.fetch(:items).fetch(id)
    targets = plan.fetch(:targets).map do |block_id, operations|
      assert!(blocks.key?(block_id), "#{paper_id}/#{id}: unknown target #{block_id}")
      {
        "block_id" => block_id,
        "expected_old_hash" => blocks.fetch(block_id).fetch("old_hash"),
        "first_line_excerpt" => blocks.fetch(block_id).fetch("first_line_excerpt"),
        "allowed_operations" => operations
      }
    end
    {
      "item_id" => id,
      "item_kind" => "residual_roadmap_item",
      "source_concern_id" => source_trace.fetch("concern_id"),
      "source_obligation_class" => source_trace.fetch("obligation_class"),
      "phase2a_verdict" => row.fetch("verdict"),
      "residual_obligation_class" => row.dig("residual_gap", "residual_obligation_class"),
      "residual_gap" => row.dig("residual_gap", "text"),
      "proposed_author_triage" => "will_address",
      "proposed_targets" => targets,
      "implementation_branch" => plan.fetch(:branch)
    }
  end

  new_issue_actions = spec.fetch(:new_issues).map do |id, plan|
    issue = verdict.fetch("new_issues").find { |candidate| candidate.fetch("new_issue_id") == id }
    assert!(!issue.nil?, "#{paper_id}: missing new issue #{id}")
    targets = plan.fetch(:targets).map do |block_id, operations|
      assert!(blocks.key?(block_id), "#{paper_id}/#{id}: unknown target #{block_id}")
      {
        "block_id" => block_id,
        "expected_old_hash" => blocks.fetch(block_id).fetch("old_hash"),
        "first_line_excerpt" => blocks.fetch(block_id).fetch("first_line_excerpt"),
        "allowed_operations" => operations
      }
    end
    {
      "item_id" => id,
      "item_kind" => "round3_regression_new_issue",
      "severity" => issue.fetch("severity"),
      "attribution" => issue.fetch("attribution"),
      "description" => issue.fetch("description"),
      "location_anchor" => issue.fetch("location_anchor"),
      "nearest_roadmap_item" => issue.fetch("nearest_roadmap_item"),
      "proposed_author_triage" => "will_address",
      "proposed_targets" => targets,
      "implementation_branch" => plan.fetch(:branch)
    }
  end

  assert!(verdict.fetch("new_issues").map { |row| row.fetch("new_issue_id") } == spec.fetch(:new_issues).keys,
          "#{paper_id}: new issue coverage mismatch")

  payload["papers"] << {
    "paper_id" => paper_id,
    "paper_slug" => spec.fetch(:slug),
    "controlling_decision" => {"state" => checker.fetch("decision_state"), "rule" => checker.fetch("decision_rule")},
    "stage3_prime_round3_verdict_record" => artifact(verdict_path),
    "stage3_prime_round3_traceability" => artifact(trace_path),
    "stage3_prime_round3_checker_receipt" => artifact(checker_path),
    "stage4_round1_response" => artifact(response_path),
    "stage4_round1_evidence_bundle" => artifact(evidence_path),
    "stage4_prime_base_draft" => artifact(draft_path),
    "stage4_prime_block_manifest" => artifact(manifest_path),
    "bibliography" => artifact(bib_path),
    "claim_surface_manifest" => artifact(claim_path),
    "proposed_patch_path" => "papers/#{spec.fetch(:slug)}/notes/stage4_prime_revision_patch_round2.json",
    "proposed_output_draft_path" => "papers/#{spec.fetch(:slug)}/notes/stage4_prime_revision_round2.tex",
    "partial_items" => items.length,
    "new_issue_actions" => new_issue_actions.length,
    "items" => items,
    "round3_new_issue_actions" => new_issue_actions
  }
end

assert!(!File.exist?(OUT_JSON), "refusing to overwrite #{OUT_JSON}")
assert!(!File.exist?(OUT_MD), "refusing to overwrite #{OUT_MD}")
File.write(OUT_JSON, JSON.pretty_generate(payload) + "\n")

residual_count = payload.fetch("papers").sum { |paper| paper.fetch("items").length }
new_issue_count = payload.fetch("papers").sum { |paper| paper.fetch("round3_new_issue_actions").length }
target_count = payload.fetch("papers").sum do |paper|
  (paper.fetch("items") + paper.fetch("round3_new_issue_actions")).sum { |item| item.fetch("proposed_targets").length }
end
operation_pair_count = payload.fetch("papers").sum do |paper|
  (paper.fetch("items") + paper.fetch("round3_new_issue_actions")).sum do |item|
    item.fetch("proposed_targets").sum { |target| target.fetch("allowed_operations").length }
  end
end

lines = []
lines << "# Round 10 Papers 29 and 32 -- Stage 4′ Exact Authorization Request"
lines << ""
lines << "Date: **2026-09-03 UTC**"
lines << ""
lines << "Status: `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION`"
lines << ""
lines << "This artifact is preparation-only. It changed no manuscript, bibliography, PDF, experiment, result, registered claim, initial dynamical system, or Route state. A later exact confirmation is required before any listed revision, source, proof-audit, or bibliography operation is executed."
lines << ""
lines << "Machine-readable request: `#{File.basename(OUT_JSON)}` (SHA-256 `#{sha(OUT_JSON)}`)."
lines << ""
lines << "The request contains **#{residual_count} residual roadmap items**, **#{new_issue_count} Round-3 regression issue**, **#{target_count} exact target entries**, and **#{operation_pair_count} block/operation pairs**."
lines << ""
lines << "## Frozen authority bindings"
lines << ""
lines << "| Artifact | SHA-256 |"
lines << "|---|---|"
payload.fetch("authority_bindings").each { |row| lines << "| `#{row.fetch('path')}` | `#{row.fetch('sha256')}` |" }
lines << ""
lines << "## Frozen paper inputs"
lines << ""
lines << "| Paper | Round-3 verdict | Traceability | Checker | Stage-4′ base | Block manifest | Bibliography | Claim surfaces |"
lines << "|---|---|---|---|---|---|---|---|"
payload.fetch("papers").each do |paper|
  lines << "| #{paper.fetch('paper_id')} | `#{paper.dig('stage3_prime_round3_verdict_record', 'sha256')}` | `#{paper.dig('stage3_prime_round3_traceability', 'sha256')}` | `#{paper.dig('stage3_prime_round3_checker_receipt', 'sha256')}` | `#{paper.dig('stage4_prime_base_draft', 'sha256')}` | `#{paper.dig('stage4_prime_block_manifest', 'sha256')}` | `#{paper.dig('bibliography', 'sha256')}` | 0 |"
end
lines << ""

payload.fetch("papers").each do |paper|
  actions = paper.fetch("items") + paper.fetch("round3_new_issue_actions")
  lines << "## #{paper.fetch('paper_id')} -- #{paper.fetch('partial_items')} residual items, #{paper.fetch('new_issue_actions')} new-issue action"
  lines << ""
  lines << "| Item | Kind | Residual/severity | Exact proposed target/operation set |"
  lines << "|---|---|---|---|"
  actions.each do |item|
    residual = item["residual_obligation_class"] || item["severity"]
    lines << "| `#{item.fetch('item_id')}` | `#{item.fetch('item_kind')}` | `#{residual}` | #{target_text(item.fetch('proposed_targets'))} |"
  end
  lines << ""
  lines << "Implementation branches:"
  lines << ""
  actions.each { |item| lines << "- `#{item.fetch('item_id')}`: #{item.fetch('implementation_branch')}" }
  lines << ""
end

lines << "## Supporting scopes requested for later execution"
lines << ""
lines << "- P29: dated replay ledger plus an admitted-ID/evidence-row crosswalk; historical missing rows remain missing."
lines << "- P32: bounded closest-work search, with zero to four source-verified `P32-CWxx` bibliography additions only if required."
lines << "- P32: commit-pinned, schema-bearing inventory of every artifact claimed current in Section 6; no uncreated archive or DOI claim."
lines << "- P32: dated 51-manifestation replay ledger and exact claim-to-passage matrix; inaccessible rows remain `INCONCLUSIVE`."
lines << "- P32: self-contained formal-definition/compatibility audit and the exact conditional scalar lemma stated in the JSON request."
lines << ""
lines << "## Boundaries"
lines << ""
lines << "- Every action is proposed as `will_address` and displayed in `source_traceability` order. A later patch may use a subset of an approved target/operation set but may not broaden it."
lines << "- The two claim-surface manifests contain zero registered surfaces. No registered-claim replacement and no collateral authorization is requested."
lines << "- There is no current revision patch, manuscript or bibliography write, PDF build, scientific execution, or result refresh."
lines << "- The scalar lemma is conditional and elementary; it does not derive either candidate factor or produce an ownerwise observation, global obstruction, recovery result, or Route credit."
lines << "- Route-A coordinates, the five initial systems, and canonical manuscript/bibliography/PDF triples remain frozen. Route B and Stages 4.5--6 remain unauthorized."
lines << "- Any target expansion, registered-claim change, verification failure, failed definition/proof, scientific-value change beyond the exact conditional lemma, build failure, Route change, or later-stage transition stops for a new checkpoint."
lines << ""
lines << "## Short confirmation"
lines << ""
lines << "Reply `确认` to approve this exact JSON request and its SHA-256. Any byte change to the request requires a new confirmation."

File.write(OUT_MD, lines.join("\n") + "\n")
puts "PASS -- emitted P29/P32 Stage 4-prime request: #{residual_count} residual + #{new_issue_count} regression; #{target_count} targets; #{operation_pair_count} operation pairs; markdown sha256=#{sha(OUT_MD)}"
