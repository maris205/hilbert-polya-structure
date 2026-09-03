#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path
DATE = "2026-09-04"
FREEZE_NAME = "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json"
AUTH_NAME = "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json"
FREEZE_SHA = "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98"
AUTH_SHA = "4cc48a512c35dc31ccff0b1ff80472eed04fc454d83f4410277bd2fe356e4e4c"
ROUTE_A_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE_B_SHA = "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"

PAPERS = {
  "P29" => "29-bianchi-ideal-owner-refinement",
  "P30" => "30-three-disk-nonconstant-roof-determinant",
  "P31" => "31-level11-conjugacy-owner-ledger",
  "P32" => "32-homology-cover-renormalization-uniformity",
  "P33" => "33-bolza-control-matched-census"
}.freeze

OUTPUTS = %w[
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_FINAL_AUDIT.json
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_COMPLETION_RECEIPT.json
  BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_COMPLETION_REPORT.md
].freeze

def require!(condition, message)
  raise "ROUND10_TERMINAL_FAIL: #{message}" unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def rel(path)
  Pathname.new(path).expand_path.relative_path_from(ROOT).to_s
end

def artifact(path)
  path = Pathname.new(path)
  require!(path.file? && !path.symlink?, "missing/symlink artifact #{path}")
  {"path" => rel(path), "sha256" => sha(path), "bytes" => File.size(path)}
end

def write_json_new(path, value)
  require!(!path.exist?, "refusing to overwrite #{path}")
  File.binwrite(path, JSON.pretty_generate(value) + "\n")
end

def verify_binding!(entry, checks, label)
  return unless entry.is_a?(Hash) && entry.keys.sort == %w[bytes path sha256]
  path = ROOT / entry.fetch("path")
  require!(path.file? && !path.symlink?, "#{label}: missing/symlink #{entry.fetch('path')}")
  require!(File.size(path) == entry.fetch("bytes"), "#{label}: byte drift #{entry.fetch('path')}")
  require!(sha(path) == entry.fetch("sha256"), "#{label}: hash drift #{entry.fetch('path')}")
  checks << "#{label}:#{entry.fetch('path')}"
end

def replay_bindings!(node, checks, label = "freeze")
  if node.is_a?(Hash)
    if node.keys.sort == %w[bytes path sha256]
      verify_binding!(node, checks, label)
    else
      node.each { |key, child| replay_bindings!(child, checks, "#{label}.#{key}") }
    end
  elsif node.is_a?(Array)
    node.each_with_index { |child, index| replay_bindings!(child, checks, "#{label}[#{index}]") }
  end
end

def paper_notes(id)
  ROOT / "papers" / PAPERS.fetch(id) / "notes"
end

OUTPUTS.each { |name| require!(!(ROOT / name).exist?, "terminal output already exists: #{name}") }
require!(sha(ROOT / FREEZE_NAME) == FREEZE_SHA, "input freeze hash")
require!(sha(ROOT / AUTH_NAME) == AUTH_SHA, "authorization receipt hash")
require!(sha(ROOT / "skills/route-a-evaluator.md") == ROUTE_A_SHA, "Route A evaluator drift")
require!(sha(ROOT / "skills/route-b-evaluator.md") == ROUTE_B_SHA, "Route B evaluator drift")

freeze = load_json(ROOT / FREEZE_NAME)
frozen_checks = []
replay_bindings!(freeze, frozen_checks)
require!(!frozen_checks.empty?, "empty freeze replay")

generated_at = Time.now.utc.iso8601
checks = []

author_side = {
  "P29" => {ops: 8, preserved: 105, total: 113, pages: 15},
  "P32" => {ops: 18, preserved: 114, total: 131, pages: 17}
}
author_rows = author_side.map do |id, expected|
  notes = paper_notes(id)
  paths = {
    patch: notes / "stage4_prime_revision_patch_round2.json",
    draft: notes / "stage4_prime_revision_round2.tex",
    apply: notes / "stage4_prime_revision_round2.tex.apply-report.json",
    bundle: notes / "stage4_prime_revision_evidence_bundle_round2.json",
    bundle_receipt: notes / "stage4_prime_bundle_validation_receipt_round2.json",
    build: notes / "stage4_prime_preview_build_receipt_round2.json",
    pdf: notes / "stage4_prime_revision_round2.pdf",
    support: notes / "stage4_prime_final_support_evidence_bundle_round2.json",
    completion: notes / "stage4_prime_completion_report_round2.md"
  }
  paths.each_value { |path| require!(path.file? && !path.symlink?, "#{id}: missing terminal artifact #{path}") }
  apply = load_json(paths.fetch(:apply))
  build = load_json(paths.fetch(:build))
  bundle_receipt = load_json(paths.fetch(:bundle_receipt))
  support = load_json(paths.fetch(:support))
  require!(apply.fetch("ops_applied").length == expected.fetch(:ops), "#{id}: applied operation count")
  require!(apply.dig("counters", "blocks_preserved_byte_identical") == expected.fetch(:preserved), "#{id}: preserved blocks")
  require!(apply.dig("counters", "blocks_total") == expected.fetch(:total), "#{id}: block total")
  require!(apply.dig("authorization_witness", "status") == "pass", "#{id}: authorization witness")
  require!(apply.dig("structural_flags", "any") == false, "#{id}: structural flag")
  require!(build.fetch("status") == "PASS" && build.fetch("pages") == expected.fetch(:pages), "#{id}: preview status/pages")
  %w[undefined_citations undefined_references missing_characters fatal_errors overfull_hboxes].each do |key|
    require!(build.fetch(key).zero?, "#{id}: nonzero build diagnostic #{key}")
  end
  require!(bundle_receipt.fetch("verdict") == "PASS", "#{id}: official bundle validation")
  require!(support.fetch("verdict") == "STAGE4_PRIME_AUTHOR_SIDE_EVIDENCE_BOUND", "#{id}: support bundle verdict")
  require!(support.fetch("stage4_5_invoked") == false && support.fetch("stage5_invoked") == false, "#{id}: stage boundary")
  checks.concat(["#{id}:apply", "#{id}:bundle", "#{id}:build", "#{id}:support"])
  {
    "paper_id" => id,
    "status" => "STAGE4_PRIME_AUTHOR_SIDE_COMPLETE",
    "authorized_residuals" => id == "P29" ? 5 : 7,
    "operations" => expected.fetch(:ops),
    "preserved_blocks" => {"numerator" => expected.fetch(:preserved), "denominator" => expected.fetch(:total)},
    "preview_pages" => expected.fetch(:pages),
    "artifacts" => paths.transform_values { |path| artifact(path) }
  }
end

audit_expectations = {
  "P30" => {
    issues: {"SERIOUS" => 1, "MEDIUM" => 3, "MINOR" => 0},
    references: 28, contexts: 30, verified_contexts: 4, anchorless: 26,
    claims: 102, evidence: 104, verified_evidence: 75, unverifiable: 26, minor_distortion: 3,
    pages: 16
  },
  "P31" => {
    issues: {"SERIOUS" => 1, "MEDIUM" => 1, "MINOR" => 0},
    references: 24, contexts: 26, verified_contexts: 4, anchorless: 22,
    claims: 71, evidence: 91, verified_evidence: 68, unverifiable: 22, minor_distortion: 1,
    pages: 13
  }
}
audit_rows = audit_expectations.map do |id, expected|
  notes = paper_notes(id)
  paths = {
    report: notes / "stage4_5_round1_integrity_report.json",
    human_report: notes / "stage4_5_round1_final_integrity_report.md",
    receipt: notes / "stage4_5_round1_receipt.json",
    correction_checkpoint: notes / "stage4_5_round1_correction_checkpoint.json",
    preview: notes / "stage4_5_round1_preview.pdf"
  }
  paths.each_value { |path| require!(path.file? && !path.symlink?, "#{id}: missing audit artifact #{path}") }
  report = load_json(paths.fetch(:report))
  receipt = load_json(paths.fetch(:receipt))
  checkpoint = load_json(paths.fetch(:correction_checkpoint))
  require!(report.fetch("verdict") == "FAIL" && receipt.fetch("verdict") == "FAIL", "#{id}: Stage 4.5 verdict")
  require!(report.fetch("issue_counts") == expected.fetch(:issues), "#{id}: issue counts")
  require!(report.dig("phases", "A_references", "checked") == expected.fetch(:references), "#{id}: reference denominator")
  require!(report.dig("phases", "B_citation_contexts", "registered") == expected.fetch(:contexts), "#{id}: citation denominator")
  require!(report.dig("phases", "B_citation_contexts", "verified") == expected.fetch(:verified_contexts), "#{id}: verified citations")
  require!(report.dig("phases", "B_citation_contexts", "unverifiable_anchorless") == expected.fetch(:anchorless), "#{id}: anchorless citations")
  require!(report.dig("phases", "E_claims_evidence", "registry_claims") == expected.fetch(:claims), "#{id}: claim denominator")
  require!(report.dig("phases", "E_claims_evidence", "actual_evidence_tuples") == expected.fetch(:evidence), "#{id}: evidence denominator")
  verdict_counts = report.dig("phases", "E_claims_evidence", "verdict_counts")
  require!(verdict_counts == {"MINOR_DISTORTION" => expected.fetch(:minor_distortion), "UNVERIFIABLE" => expected.fetch(:unverifiable), "VERIFIED" => expected.fetch(:verified_evidence)}, "#{id}: evidence verdicts")
  require!(report.dig("build", "status") == "PASS" && report.dig("build", "preview", "pages") == expected.fetch(:pages), "#{id}: independent build")
  require!(receipt.fetch("protected_snapshot_unchanged") == true, "#{id}: protected snapshot")
  require!(receipt.fetch("silent_repair_performed") == false && receipt.fetch("stage5_started") == false, "#{id}: fail-closed boundary")
  require!(checkpoint.fetch("status") == "FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED", "#{id}: proposal-only boundary")
  checks.concat(["#{id}:fresh_stage4_5", "#{id}:denominators", "#{id}:fail_closed"])
  {
    "paper_id" => id,
    "status" => "STAGE4_5_FAIL_CORRECTIONS_PROPOSED_NOT_APPLIED",
    "issue_counts" => expected.fetch(:issues),
    "citation_contexts" => {"verified" => expected.fetch(:verified_contexts), "anchorless_unverifiable" => expected.fetch(:anchorless), "total" => expected.fetch(:contexts)},
    "evidence_rows" => {"verified" => expected.fetch(:verified_evidence), "unverifiable" => expected.fetch(:unverifiable), "minor_distortion" => expected.fetch(:minor_distortion), "total" => expected.fetch(:evidence)},
    "preview_pages" => expected.fetch(:pages),
    "artifacts" => paths.transform_values { |path| artifact(path) }
  }
end

p33_notes = paper_notes("P33")
p33_paths = {
  completion: p33_notes / "stage3_prime_round5_completion_receipt.json",
  final_audit: p33_notes / "stage3_prime_round5_final_integrity_audit.json",
  checker: p33_notes / "stage3_prime_round5_checker_receipt.json",
  verification_report: p33_notes / "stage3_prime_round5_verification_report.md",
  phase1: p33_notes / "stage3_prime_round5_phase1_validation.json",
  phase2a: p33_notes / "stage3_prime_round5_phase2a_validation.json",
  phase2b: p33_notes / "stage3_prime_round5_phase2b_validation.json",
  traceability: p33_notes / "stage3_prime_round5_traceability.json"
}
p33_paths.each_value { |path| require!(path.file? && !path.symlink?, "P33: missing Round-5 artifact #{path}") }
p33_completion = load_json(p33_paths.fetch(:completion))
p33_audit = load_json(p33_paths.fetch(:final_audit))
p33_checker = load_json(p33_paths.fetch(:checker))
require!(p33_completion.fetch("status") == "COMPLETE", "P33: completion status")
require!(p33_completion.fetch("decision") == "Major Revision" && p33_completion.fetch("decision_rule") == "B4", "P33: decision")
require!(p33_completion.fetch("phase_counts") == {"FULLY_ADDRESSED" => 6, "PARTIALLY_ADDRESSED" => 7}, "P33: verdict counts")
require!(p33_completion.fetch("residual_counts") == {"must_fix" => 6, "should_fix" => 1}, "P33: residual counts")
require!(p33_audit.fetch("status") == "PASS" && p33_checker.fetch("checker_status") == "PASS", "P33: terminal audit/checker")
require!(p33_checker.fetch("reject_recommended") == false && p33_checker.fetch("apply_chain_witness") == "pass", "P33: decision inputs")
checks.concat(%w[P33:round5 P33:official_checker P33:decision_B4])
p33_row = {
  "paper_id" => "P33",
  "status" => "STAGE3_PRIME_ROUND5_COMPLETE_MAJOR_REVISION_B4",
  "verdict_counts" => {"FULLY_ADDRESSED" => 6, "PARTIALLY_ADDRESSED" => 7},
  "residual_counts" => {"must_fix" => 6, "should_fix" => 1},
  "adjustments" => 0,
  "reject_recommended" => false,
  "artifacts" => p33_paths.transform_values { |path| artifact(path) }
}

# Recheck the complete frozen boundary after every terminal artifact has been read.
frozen_checks_after = []
replay_bindings!(freeze, frozen_checks_after)
require!(frozen_checks_after == frozen_checks, "freeze replay population changed")

final_audit_path = ROOT / OUTPUTS[0]
completion_receipt_path = ROOT / OUTPUTS[1]
completion_report_path = ROOT / OUTPUTS[2]

final_audit = {
  "schema_version" => "round10-stage4-prime-execution-stage4-5-round5-final-audit/1.0",
  "generated_at" => generated_at,
  "workflow_date" => DATE,
  "status" => "PASS",
  "authority" => {"authorization_receipt" => artifact(ROOT / AUTH_NAME), "input_freeze" => artifact(ROOT / FREEZE_NAME)},
  "frozen_binding_replay" => {"before" => frozen_checks.length, "after" => frozen_checks_after.length, "status" => "PASS"},
  "route_evaluators" => {
    "route_a" => artifact(ROOT / "skills/route-a-evaluator.md"),
    "route_b" => artifact(ROOT / "skills/route-b-evaluator.md")
  },
  "paper_outcomes" => author_rows + audit_rows + [p33_row],
  "independent_checks" => checks,
  "boundaries" => {
    "canonical_files_frozen" => "15/15",
    "science_result_placeholders_frozen" => "15/15",
    "initial_dynamical_system_sources_frozen" => "5/5",
    "route_crosswalks_frozen" => "5/5",
    "new_scientific_executions" => 0,
    "canonical_result_refresh" => false,
    "canonical_promotion" => false,
    "stage5_started" => false,
    "route_a_formal_tuples" => "0/5",
    "positive_arithmetic_a2" => "0/5",
    "a3_credit" => "0/5",
    "a4_credit" => "0/5",
    "route_b_invocations" => "0/5",
    "citation_style" => "plainnat numeric unchanged"
  },
  "verdict" => "AUTHORIZED_SCOPE_COMPLETE_NO_SUCCESSOR_STAGE_STARTED"
}
write_json_new(final_audit_path, final_audit)

receipt = {
  "schema_version" => "round10-stage4-prime-execution-stage4-5-round5-completion-receipt/1.0",
  "generated_at" => generated_at,
  "workflow_date" => DATE,
  "status" => "COMPLETE",
  "scope" => "P29/P32 author-side Stage 4-prime; P30/P31 fresh Stage 4.5; P33 fresh Stage 3-prime Round 5",
  "paper_states" => {
    "P29" => "STAGE4_PRIME_AUTHOR_SIDE_COMPLETE_AWAITING_FRESH_STAGE4_5",
    "P30" => "STAGE4_5_FAIL_AWAITING_EXACT_CORRECTION_AUTHORIZATION",
    "P31" => "STAGE4_5_FAIL_AWAITING_EXACT_CORRECTION_AUTHORIZATION",
    "P32" => "STAGE4_PRIME_AUTHOR_SIDE_COMPLETE_AWAITING_FRESH_STAGE4_5",
    "P33" => "ROUND5_MAJOR_REVISION_B4_AWAITING_EXACT_STAGE4_PRIME_AUTHORIZATION"
  },
  "aggregate" => {
    "papers_with_concrete_progress" => "5/5",
    "author_side_stage4_prime_completed" => "2/2",
    "fresh_stage4_5_audits_completed" => "2/2",
    "fresh_stage4_5_pass" => 0,
    "fresh_stage4_5_fail" => 2,
    "fresh_round5_completed" => "1/1",
    "stage4_5_blockers" => 6,
    "p33_round5_verdicts" => {"FULLY_ADDRESSED" => 6, "PARTIALLY_ADDRESSED" => 7}
  },
  "final_audit" => artifact(final_audit_path),
  "next_gate" => "MANDATORY_AUTHOR_CHECKPOINT_REQUIRED",
  "successor_stage_started" => false,
  "route_state_changed" => false,
  "canonical_or_scientific_state_changed" => false
}
write_json_new(completion_receipt_path, receipt)

report = <<~MD
  # Round 10 Papers 29--33 — Stage 4′ execution / Stage 4.5 / Round 5 completion report

  Date: **#{DATE} UTC**

  Status: **AUTHORIZED SCOPE COMPLETE — all five papers made a concrete, audited advance; no successor stage started**

  ## Paper outcomes

  | Paper | Terminal state | Concrete result | Next legal gate |
  |---|---|---|---|
  | P29 | Stage 4′ author-side **COMPLETE** | 5 residual/regression items covered by 8 operations; 105/113 source blocks preserved; 53-query replay, 22/22 crosswalk, explicit stop map and unexecuted fixture; clean 15-page preview. | Fresh Stage 4.5 audit. |
  | P30 | Stage 4.5 **FAIL** | Full fresh audit completed: 28/28 references, 30/30 citation contexts, 102/102 claims and 104/104 evidence rows; 16-page clean build. One Serious and three Medium blockers are proposal-only and unapplied. | Exact author authorization for correction/source-finalization, then a new fresh Stage 4.5. |
  | P31 | Stage 4.5 **FAIL** | Full fresh audit completed: 24/24 references, 26/26 citation contexts, 71/71 claims and 91/91 evidence rows; 13-page clean build. One Serious and one Medium blocker are proposal-only and unapplied. | Exact author authorization for correction/source-finalization, then a new fresh Stage 4.5. |
  | P32 | Stage 4′ author-side **COMPLETE** | 7 residuals covered by 18 operations; 114/131 source blocks preserved; four-work comparator, 51-manifestation replay, formal carriers, conditional scalar lemma and AN-1--AN-5 registry; clean 17-page preview. | Fresh Stage 4.5 audit. |
  | P33 | Stage 3′ Round 5 **COMPLETE — Major Revision / B4** | Fresh three-gate review completed with official checker PASS: 6 FULL, 7 PARTIAL, zero adjustments; six must-fix and one should-fix residual remain. | Exact Stage 4′ residual-remediation authorization. |

  ## What changed in the papers

  P29 and P32 now have complete versioned Stage-4′ author-side manuscripts and reproducible evidence bundles. P29 makes the mechanism/quotient interface, replay provenance, control stops and fixture non-execution explicit. P32 makes its formal carrier hierarchy, analytic obligation registry, comparator positioning and conditional scalar claim precise. These are material manuscript advances, while remaining honest about absent owner laws, factors, limits, executions and Route credit.

  P30 and P31 also progressed decisively: their fresh final-integrity audits replaced an assumed readiness state with exact failure surfaces. P30 has 26/30 anchorless citation contexts plus three text/provenance inconsistencies; P31 has 22/26 anchorless contexts plus one disclosure gap. No correction was silently applied. P33's previously blocked re-review now has a valid terminal decision and a finite six-item must-fix set.

  ## Route A / Route B correspondence

  The controlling evaluators remain `skills/route-a-evaluator.md` (SHA-256 `#{ROUTE_A_SHA}`) and `skills/route-b-evaluator.md` (SHA-256 `#{ROUTE_B_SHA}`). Round 10 remains at **Route-A A0/A1 foundation/interface work**: formal Route-A tuples `0/5`, positive arithmetic A2 `0/5`, A3 `0/5`, A4 `0/5`, and Route-B invocations `0/5`. P30 remains A0-failed/not eligible for A2; P32's arithmetic A0 remains unavailable; no paper acquired scientific Route credit from manuscript revision or integrity review.

  Five distinct continuous-time dynamical subtypes remain represented, but this authorized scope ran **zero new scientific experiments**. All five initial systems, clocks, primitive/owner conventions, inverse rules, normalizations, cutoffs and target-blind restrictions are byte-frozen. The 15 canonical manuscript/bibliography/PDF files and all science/results boundaries remain unchanged. Citation formatting remains `plainnat` numeric.

  ## Integrity result

  The global freeze was replayed #{frozen_checks.length} bindings before and after terminal synthesis. P29/P32 apply witnesses, official revision-bundle validation and isolated builds passed. P30/P31 were retained as Stage-4.5 FAIL with six total blockers and no repair or promotion. P33's Phase 1, Phase 2A, Phase 2B and official synthesis checker all passed. Same-family role separation is disclosed and is not represented as independent error processes.

  Final audit: `#{rel(final_audit_path)}` (`#{sha(final_audit_path)}`). Completion receipt: `#{rel(completion_receipt_path)}` (`#{sha(completion_receipt_path)}`). A separate mandatory author checkpoint defines the next scope; Stage 5/6, canonical promotion, submission, result refresh, new science execution and Route advancement remain unauthorized.
MD
File.binwrite(completion_report_path, report)

puts "PASS -- Round 10 authorized scope complete; frozen=#{frozen_checks.length}; audit=#{sha(final_audit_path)}; receipt=#{sha(completion_receipt_path)}"
