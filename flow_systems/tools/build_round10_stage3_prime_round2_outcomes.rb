#!/usr/bin/env ruby
# frozen_string_literal: true

# Finalize Round 10 / Stage 3-prime / Round 2 from already committed review
# artifacts.  This program is intentionally a terminal, fail-closed publisher:
#
# * P29/P32/P33 ended at the no-retry Phase-2A semantic gate.  Their checker is
#   not run and no decision is emitted.
# * P30/P31 must have a schema-valid Phase-2B integration and traceability
#   sidecar.  The official ARS checker is run here; no result is published
#   unless both invocations exit zero and agree with the traceability decision.
# * the Round-1, canonical, science, initial-system, and Route-A/B bytes frozen
#   by the Round-2 input freeze are replayed before and after composition.
# * only the explicitly enumerated Round-2 terminal review artifacts are ever
#   created.  Manuscripts, bibliographies, PDFs, Stage-4 evidence, route files,
#   science trees, README/state files, and successor-stage files are read-only.
#
# Publication is create-only and transactional with respect to files created by
# this invocation.  A rerun accepts byte-identical outputs, but refuses to
# replace a differing terminal artifact.

require "digest"
require "fileutils"
require "find"
require "json"
require "open3"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
FINALIZED_AT = "2026-09-03T12:06:19Z"
DISCLOSURE = "This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2)."

ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite"
CHECKER = File.join(ARS_ROOT, "ars/scripts/check_re_review_synthesis.py")
EXPECTED_CHECKER_SHA256 = "8347ec3766857366cc0c6ffd30021afcebf8d0528a83927fabfce9ecb66a59ab"
PROTOCOL = File.join(ARS_ROOT, "ars/academic-paper-reviewer/references/re_review_mode_protocol.md")
WORKFLOW = File.join(ARS_ROOT, "ars/academic-paper-reviewer/WORKFLOW.md")
CONTRACT_ROOT = File.join(ARS_ROOT, "ars/shared/contracts/re_review")
RUBRIC_PATHS = [
  WORKFLOW,
  PROTOCOL,
  File.join(CONTRACT_ROOT, "input_manifest.schema.json"),
  File.join(CONTRACT_ROOT, "precommitment.schema.json"),
  File.join(CONTRACT_ROOT, "verdict_record.schema.json"),
  File.join(CONTRACT_ROOT, "traceability.schema.json"),
  CHECKER
].freeze

FREEZE_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_INPUT_FREEZE.json"
BOUNDARY_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_BOUNDARY_VALIDATION.json"
PHASE1_GATE_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE1_GATE_RECEIPT.json"
PHASE2A_GATE_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_GATE_RECEIPT.json"
PHASE2A_CONSOLIDATION_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_CONSOLIDATION.json"
PHASE2B_VALIDATION_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2B_INTEGRATION_VALIDATION.json"
AUTHORIZATION_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_AUTHORIZATION_RECORD.md"
AUTHOR_EVENT_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_AUTHOR_EVENT_20260903.txt"

BATCH_REPORT_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_REPORT.md"
BATCH_CHECKPOINT_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_MANDATORY_CHECKPOINT.md"
FINAL_AUDIT_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_FINAL_INTEGRITY_AUDIT.json"
FINAL_AUDIT_RECEIPT_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_FINAL_INTEGRITY_RECEIPT.json"
BATCH_RECEIPT_FILE = "BATCH_ROUND10_STAGE3_PRIME_ROUND2_RECEIPT.json"

VERDICTS = %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].freeze
ABORTED = %w[P29 P32 P33].freeze
ELIGIBLE = %w[P30 P31].freeze
ROUTE_TOKENS = %w[
  FORMAL_ROUTE_A_TUPLE=UNASSIGNED
  POSITIVE_ARITHMETIC_A2=0
  STAGE4_ROUTE_PROMOTION=NONE
  ROUTE_B_INVOKED=false
  CANONICAL_RESULTS_REFRESHED=false
].freeze

PAPERS = {
  "P29" => {
    slug: "29-bianchi-ideal-owner-refinement",
    title: "Bianchi ideal-owner refinement",
    route: "A0/A1 foundation/interface preparation; formal tuple UNASSIGNED; positive arithmetic A2 = 0; Route B uninvoked",
    system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
    progress: "Gate M/Q, inversion/conjugation semantics, the literal ideal-owner convention, and fail-closed interfaces remain concrete manuscript advances. Round 2 nevertheless overcredited two committed criteria and therefore terminates before claim matching."
  },
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    title: "Three-disk nonconstant-roof determinant",
    route: "A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; Route B uninvoked",
    system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
    progress: "The physical-roof six-gate architecture, common-norm uncertainty channels, owner witness, and typed control surfaces survive a clean Round-2 three-gate review. Residual must-fix obligations still require another scoped revision."
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    title: "Level-11 conjugacy owner ledger",
    route: "A1-only preparation; formal tuple UNASSIGNED; positive arithmetic A2 = 0; Route B uninvoked",
    system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree is distinct",
    progress: "Owner canonicalization, G/I/C materializations, and the 9,453-pair adversarial-audit architecture survive the fresh Round-2 criteria and evidence gates. Residual must-fix obligations still prevent acceptance."
  },
  "P32" => {
    slug: "32-homology-cover-renormalization-uniformity",
    title: "Homology-cover renormalization uniformity",
    route: "generic A1-A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; Route B uninvoked",
    system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
    progress: "Higher/zero-content falsification order, the two modulus schedules, and the dependency table remain explicit manuscript advances. The scalar-lemma/inadmissibility row was overcredited, so Round 2 terminates at Phase 2A without a decision."
  },
  "P33" => {
    slug: "33-bolza-control-matched-census",
    title: "Bolza control-matched census",
    route: "A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; Route B uninvoked",
    system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
    progress: "BP/CP producer contracts, owner/inverse/repetition rules, canonical serialization, migration, and the trust graph remain concrete manuscript advances. One universal invalid-case criterion was overcredited, forcing a Phase-2A abort."
  }
}.freeze

OUTPUTS = {}

def fail_closed!(message)
  raise "ROUND10_STAGE3_PRIME_ROUND2_FAIL_CLOSED: #{message}"
end

def assert!(condition, message)
  fail_closed!(message) unless condition
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

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
rescue JSON::ParserError => error
  fail_closed!("invalid JSON #{path}: #{error.message}")
end

def relative(path)
  expanded = File.expand_path(path)
  prefix = "#{ROOT}/"
  assert!(expanded.start_with?(prefix), "repository path escape: #{path}")
  expanded.delete_prefix(prefix)
end

def safe_repo_file!(relative_path)
  assert!(!relative_path.start_with?("/"), "absolute repository path: #{relative_path}")
  assert!(!relative_path.split("/").include?(".."), "repository path traversal: #{relative_path}")
  expanded = File.expand_path(relative_path, ROOT)
  assert!(expanded.start_with?("#{ROOT}/"), "repository path escape: #{relative_path}")

  cursor = ROOT
  relative_path.split("/")[0...-1].each do |part|
    cursor = File.join(cursor, part)
    stat = File.lstat(cursor)
    assert!(stat.directory? && !stat.symlink?, "unsafe ancestor #{relative(cursor)}")
  end
  stat = File.lstat(expanded)
  assert!(stat.file? && !stat.symlink?, "not a regular non-symlink file: #{relative_path}")
  expanded
rescue Errno::ENOENT
  fail_closed!("missing required file: #{relative_path}")
end

def safe_external_file!(path)
  expanded = File.expand_path(path)
  stat = File.lstat(expanded)
  assert!(stat.file? && !stat.symlink?, "unsafe or missing external file: #{expanded}")
  expanded
rescue Errno::ENOENT
  fail_closed!("missing external file: #{expanded}")
end

def binding(path, jcs: false)
  expanded = File.expand_path(path)
  bytes = OUTPUTS[expanded]
  raw = bytes ? Digest::SHA256.hexdigest(bytes) : sha256(expanded)
  result = {"path" => expanded.start_with?("#{ROOT}/") ? relative(expanded) : expanded, "sha256" => raw}
  result["jcs_sha256"] = jcs_sha256(bytes ? JSON.parse(bytes) : load_json(expanded)) if jcs
  result
end

def verify_binding!(entry, label)
  path = safe_repo_file!(entry.fetch("path"))
  assert!(File.size(path) == entry.fetch("bytes"), "#{label}: byte drift #{entry.fetch('path')}") if entry.key?("bytes")
  assert!(sha256(path) == entry.fetch("sha256"), "#{label}: hash drift #{entry.fetch('path')}")
  path
end

def bind_json(path)
  value = load_json(path)
  {"path" => relative(path), "raw_sha256" => sha256(path), "jcs_sha256" => jcs_sha256(value)}
end

def output_paths
  roots = [BATCH_REPORT_FILE, BATCH_CHECKPOINT_FILE, FINAL_AUDIT_FILE,
           FINAL_AUDIT_RECEIPT_FILE, BATCH_RECEIPT_FILE]
  PAPERS.each do |paper_id, spec|
    base = File.join("papers", spec.fetch(:slug), "notes")
    roots << File.join(base, "stage3_prime_round2_checker_receipt.json")
    roots << File.join(base, "stage3_prime_round2_verification_report.md")
    roots << File.join(base, "stage3_prime_round2_abort_record.json") if ABORTED.include?(paper_id)
  end
  roots.sort.freeze
end

def queue_output!(relative_path, content)
  assert!(output_paths.include?(relative_path), "undeclared output #{relative_path}")
  destination = File.expand_path(relative_path, ROOT)
  assert!(destination.start_with?("#{ROOT}/"), "output path escape #{relative_path}")
  assert!(!OUTPUTS.key?(destination), "duplicate output #{relative_path}")

  cursor = ROOT
  relative_path.split("/")[0...-1].each do |part|
    cursor = File.join(cursor, part)
    stat = File.lstat(cursor)
    assert!(stat.directory? && !stat.symlink?, "unsafe output ancestor #{relative(cursor)}")
  end
  if File.exist?(destination) || File.symlink?(destination)
    stat = File.lstat(destination)
    assert!(stat.file? && !stat.symlink?, "unsafe existing output #{relative_path}")
  end
  OUTPUTS[destination] = content.encode(Encoding::UTF_8).b
end

def verify_manifest_artifacts!(paper_root, manifest)
  assert!(manifest.fetch("contract_version") == "1.1", "manifest contract is not 1.1")
  artifacts = manifest.fetch("artifacts")
  assert!(artifacts.keys.sort == %w[apply_reports author_adjudication editorial_decision_letter original_manuscript response_to_reviewers revised_manuscript revision_evidence_bundle revision_patches revision_roadmap round1_config_cards round1_findings].sort,
          "manifest does not contain exactly eleven artifact keys")

  artifacts.each do |key, entry|
    next unless entry.fetch("present")
    records = entry.key?("items") ? entry.fetch("items") : [entry]
    records.each do |record|
      ref = record.fetch("path_or_passport_ref")
      assert!(ref.start_with?("path:"), "#{key}: only local path refs are allowed")
      relative_path = ref.delete_prefix("path:")
      assert!(!relative_path.start_with?("/") && !relative_path.split("/").include?(".."), "#{key}: unsafe manifest path")
      path = File.expand_path(relative_path, paper_root)
      assert!(path.start_with?("#{paper_root}/"), "#{key}: manifest path escape")
      stat = File.lstat(path)
      assert!(stat.file? && !stat.symlink?, "#{key}: manifest target is not a regular file")
      assert!(sha256(path) == record.fetch("sha256"), "#{key}: manifest hash drift")
    end
  end
end

def replay_frozen_boundaries!
  freeze_path = safe_repo_file!(FREEZE_FILE)
  freeze = load_json(freeze_path)
  assert!(freeze.fetch("schema_version") == "round10-stage3-prime-round2-input-freeze/1.0", "input-freeze schema")

  totals = Hash.new(0)
  freeze.fetch("round1_terminal_bindings").each do |entry|
    verify_binding!(entry, "Round-1 terminal")
    totals["round1_artifacts_unchanged"] += 1
  end
  freeze.fetch("route_evaluator_bindings").each do |entry|
    verify_binding!(entry, "route evaluator")
    totals["route_evaluators_unchanged"] += 1
  end

  paper_rows = freeze.fetch("papers").map do |paper|
    paper_id = paper.fetch("paper_id")
    spec = PAPERS.fetch(paper_id)
    assert!(paper.fetch("paper_slug") == spec.fetch(:slug), "#{paper_id}: freeze slug")
    groups = {
      "round1_artifacts_unchanged" => paper.fetch("round1_artifacts"),
      "canonical_files_unchanged" => paper.fetch("canonical_files"),
      "science_files_unchanged" => paper.fetch("science_files"),
      "review_evidence_files_unchanged" => paper.fetch("review_evidence_files"),
      "initial_system_sources_unchanged" => [paper.fetch("initial_system_source")],
      "route_crosswalks_unchanged" => [paper.fetch("route_crosswalk")]
    }
    row = {"paper_id" => paper_id}
    groups.each do |name, entries|
      entries.each { |entry| verify_binding!(entry, "#{paper_id} #{name}") }
      row[name] = entries.length
      totals[name] += entries.length
    end

    notes = File.join(ROOT, "papers", spec.fetch(:slug), "notes")
    round1_now = Dir[File.join(notes, "stage3_prime_round1_*")].sort.map { |path| relative(path) }
    round1_frozen = paper.fetch("round1_artifacts").map { |entry| entry.fetch("path") }.sort
    assert!(round1_now == round1_frozen, "#{paper_id}: Round-1 inventory drift")

    paper_root = File.join(ROOT, "papers", spec.fetch(:slug))
    science_now = %w[code experiments results].flat_map do |directory|
      Dir.glob(File.join(paper_root, directory, "**", "*"), File::FNM_DOTMATCH)
         .select { |path| File.file?(path) }
         .map { |path| relative(path) }
    end.sort
    science_frozen = paper.fetch("science_files").map { |entry| entry.fetch("path") }.sort
    assert!(science_now == science_frozen, "#{paper_id}: science inventory drift")

    review_now = Dir[File.join(notes, "stage4_*")].flat_map do |path|
      File.directory?(path) ? Dir[File.join(path, "**", "*")] : [path]
    end.select { |path| File.file?(path) }.uniq.sort.map { |path| relative(path) }
    review_frozen = paper.fetch("review_evidence_files").map { |entry| entry.fetch("path") }.sort
    assert!(review_now == review_frozen, "#{paper_id}: Stage-4 evidence inventory drift")

    route_path = safe_repo_file!(paper.fetch("route_crosswalk").fetch("path"))
    route_text = File.binread(route_path).force_encoding("UTF-8")
    ROUTE_TOKENS.each { |token| assert!(route_text.include?(token), "#{paper_id}: missing frozen route token #{token}") }

    successor_hits = Find.find(paper_root).select do |path|
      next false unless File.file?(path)
      relative_path = path.delete_prefix("#{paper_root}/")
      /(?:stage4[_.-]?(?:prime|p)|stage4[_.-]?5|stage45|stage5|submission)/i.match?(relative_path)
    end.map { |path| relative(path) }
    # Stage-4 evidence predates this re-review and is explicitly hash-bound by
    # the freeze.  Only successor-looking paths outside that closed inventory
    # are unauthorized.  In particular, `stage4_preview_*` must not be
    # mistaken for `stage4_prime` merely because "preview" begins with "p".
    unexpected_successors = successor_hits - review_frozen
    assert!(unexpected_successors.empty?, "#{paper_id}: unauthorized successor-stage artifacts: #{unexpected_successors.join(', ')}")
    row["status"] = "PASS"
    row
  end

  assert!(paper_rows.map { |row| row.fetch("paper_id") } == PAPERS.keys, "input-freeze paper order")
  assert!(totals.fetch("round1_artifacts_unchanged") == 55, "Round-1 binding total")
  assert!(totals.fetch("canonical_files_unchanged") == 15, "canonical binding total")
  assert!(totals.fetch("science_files_unchanged") == 15, "science binding total")
  assert!(totals.fetch("review_evidence_files_unchanged") == 212, "review-evidence binding total")
  assert!(totals.fetch("initial_system_sources_unchanged") == 5, "initial-system binding total")
  assert!(totals.fetch("route_crosswalks_unchanged") == 5, "route-crosswalk binding total")
  assert!(totals.fetch("route_evaluators_unchanged") == 2, "route-evaluator binding total")
  assert!(totals.values.sum == 309, "frozen binding grand total")

  boundary_path = safe_repo_file!(BOUNDARY_FILE)
  boundary = load_json(boundary_path)
  assert!(boundary.fetch("status") == "PASS", "boundary validation status")
  assert!(boundary.fetch("input_freeze_sha256") == sha256(freeze_path), "boundary validation freeze binding")
  expected_totals = totals.dup
  assert!(boundary.fetch("totals") == expected_totals, "boundary validation totals disagree with replay")
  expected_zero = {
    "manuscript_bibliography_pdf_writes" => 0,
    "science_writes" => 0,
    "initial_system_changes" => 0,
    "formal_route_a_tuples_assigned" => 0,
    "positive_arithmetic_a2_results" => 0,
    "route_b_invocations" => 0,
    "successor_stage_authorized" => false
  }
  assert!(boundary.fetch("boundaries") == expected_zero, "boundary validation flags")

  {
    "input_freeze" => binding(freeze_path),
    "prior_boundary_validation" => binding(boundary_path),
    "papers" => paper_rows,
    "totals" => totals,
    "verified_bindings" => totals.values.sum,
    "status" => "PASS"
  }
end

def validate_root_gates!
  authorization = File.binread(safe_repo_file!(AUTHORIZATION_FILE)).force_encoding("UTF-8")
  author_event = File.binread(safe_repo_file!(AUTHOR_EVENT_FILE)).force_encoding("UTF-8")
  assert!(author_event == "确认，下一轮\n" || author_event == "确认，下一轮", "author event bytes")
  assert!(authorization.include?("Stage 3′ Round 2"), "authorization scope")
  assert!(authorization.include?("does not authorize Stage 4′"), "authorization successor-stage exclusion")

  phase1 = load_json(safe_repo_file!(PHASE1_GATE_FILE))
  assert!(phase1.fetch("status") == "PASS", "Phase-1 gate")
  assert!(phase1.dig("totals", "papers") == 5 && phase1.dig("totals", "rows") == 56, "Phase-1 totals")
  assert!(phase1.dig("totals", "semantic_defects") == 0, "Phase-1 semantic defects")

  phase2a = load_json(safe_repo_file!(PHASE2A_GATE_FILE))
  assert!(phase2a.fetch("status") == "PASS_WITH_THREE_FAIL_CLOSED_ABORTS", "Phase-2A gate")
  assert!(phase2a.fetch("phase2a_pass_papers") == ELIGIBLE, "Phase-2A eligible set")
  assert!(phase2a.fetch("phase2a_aborted_papers") == ABORTED, "Phase-2A aborted set")
  assert!(phase2a.fetch("phase2b_authorized_scope") == ELIGIBLE, "Phase-2B scope")
  assert!(phase2a.fetch("aborted_reason") == "phase2a_lint_failed", "Phase-2A abort reason")

  consolidation_path = safe_repo_file!(PHASE2A_CONSOLIDATION_FILE)
  consolidation = load_json(consolidation_path)
  assert!(phase2a.fetch("consolidation_sha256") == sha256(consolidation_path), "Phase-2A consolidation binding")
  assert!(consolidation.fetch("phase2b_scope") == ELIGIBLE, "consolidation Phase-2B scope")
  assert!(consolidation.fetch("aborted_before_phase2b") == ABORTED, "consolidation aborted set")
  assert!(consolidation.dig("totals", "papers") == 5, "consolidation paper total")
  assert!(consolidation.dig("totals", "phase2a_pass") == 2, "consolidation pass total")
  assert!(consolidation.dig("totals", "phase2a_aborted") == 3, "consolidation abort total")
  assert!(consolidation.dig("totals", "blind_tie_break_record_discrepancies") == 4, "consolidation discrepancy total")

  consolidation.fetch("source_artifacts").each do |entry|
    path = safe_repo_file!(entry.fetch("path"))
    assert!(sha256(path) == entry.fetch("sha256"), "consolidation source drift #{entry.fetch('path')}")
  end

  phase2b_path = safe_repo_file!(PHASE2B_VALIDATION_FILE)
  phase2b = load_json(phase2b_path)
  assert!(phase2b.dig("totals", "phase2b_integration_validation") == "PASS", "Phase-2B integration validation")
  assert!(phase2b.fetch("papers").map { |row| row.fetch("paper_id") } == ELIGIBLE, "Phase-2B validated set")
  assert!(phase2b.dig("totals", "papers") == 2, "Phase-2B paper total")
  assert!(phase2b.dig("totals", "response_rows") == 20, "Phase-2B row total")
  assert!(phase2b.dig("totals", "verdict_changes") == 0, "Phase-2B unexpected verdict changes")

  {
    "authorization" => binding(File.join(ROOT, AUTHORIZATION_FILE)),
    "author_event" => binding(File.join(ROOT, AUTHOR_EVENT_FILE)),
    "phase1_gate" => binding(File.join(ROOT, PHASE1_GATE_FILE), jcs: true),
    "phase2a_gate" => binding(File.join(ROOT, PHASE2A_GATE_FILE), jcs: true),
    "phase2a_consolidation" => binding(consolidation_path, jcs: true),
    "phase2b_validation" => binding(phase2b_path, jcs: true),
    "phase1" => phase1,
    "phase2a" => phase2a,
    "consolidation" => consolidation,
    "phase2b" => phase2b
  }
end

def paper_paths(spec)
  root = File.join(ROOT, "papers", spec.fetch(:slug))
  notes = File.join(root, "notes")
  {
    root: root,
    notes: notes,
    manifest: File.join(notes, "stage3_prime_round2_input_manifest.json"),
    precommitment: File.join(notes, "stage3_prime_round2_precommitment.json"),
    verdict: File.join(notes, "stage3_prime_round2_verdict_record.json"),
    phase1_receipt: File.join(notes, "stage3_prime_round2_phase1_receipt.md"),
    phase2a_receipt: File.join(notes, "stage3_prime_round2_phase2a_receipt.md"),
    integration: File.join(notes, "stage3_prime_round2_phase2b_integration.json"),
    trace: File.join(notes, "stage3_prime_round2_traceability.json"),
    roadmap: File.join(notes, "stage3_revision_roadmap.json"),
    author: File.join(notes, "stage4_author_adjudication.json"),
    bundle: File.join(notes, "stage4_revision_evidence_bundle.json"),
    letter: File.join(notes, "stage3_editorial_synthesis.md"),
    apply_report: File.join(notes, "stage4_revision_round1.tex.apply-report.json")
  }
end

def count_verdicts(rows, key)
  VERDICTS.to_h { |verdict| [verdict, rows.count { |row| row.fetch(key) == verdict }] }
end

def validate_paper_inputs!(paper_id, spec, gates)
  paths = paper_paths(spec)
  %i[manifest precommitment verdict phase1_receipt phase2a_receipt roadmap author bundle letter apply_report].each do |key|
    safe_repo_file!(relative(paths.fetch(key)))
  end
  manifest = load_json(paths.fetch(:manifest))
  precommitment = load_json(paths.fetch(:precommitment))
  verdict = load_json(paths.fetch(:verdict))
  roadmap = load_json(paths.fetch(:roadmap))
  verify_manifest_artifacts!(paths.fetch(:root), manifest)

  round_id = "#{paper_id.downcase}-stage3-prime-round2-2026-09-03"
  assert!(manifest.fetch("round_id") == round_id, "#{paper_id}: manifest round id")
  assert!(precommitment.fetch("round_id") == round_id, "#{paper_id}: precommitment round id")
  assert!(verdict.fetch("round_id") == round_id, "#{paper_id}: verdict round id")
  assert!(manifest.fetch("cross_model_active") == false, "#{paper_id}: unauthorized cross-model route")
  assert!(verdict.fetch("dissents").empty?, "#{paper_id}: unexpected dissent")
  assert!(verdict.fetch("escalation_exceptions").empty?, "#{paper_id}: unexpected escalation")

  phase1_gate = gates.fetch("phase1").fetch("papers").find { |row| row.fetch("paper_id") == paper_id }
  phase2a_record = gates.fetch("consolidation").fetch("papers").find { |row| row.fetch("paper_id") == paper_id }
  assert!(!phase1_gate.nil? && !phase2a_record.nil?, "#{paper_id}: absent from root gates")
  assert!(sha256(paths.fetch(:precommitment)) == phase1_gate.fetch("precommitment_sha256"), "#{paper_id}: frozen precommitment drift")
  assert!(sha256(paths.fetch(:phase1_receipt)) == phase1_gate.fetch("phase1_receipt_sha256"), "#{paper_id}: Phase-1 receipt drift")
  assert!(File.binread(paths.fetch(:phase1_receipt)).include?("[CONTRACT-ACKNOWLEDGED]"), "#{paper_id}: Phase-1 terminal marker")
  assert!(sha256(paths.fetch(:verdict)) == phase2a_record.fetch("verdict_record_sha256"), "#{paper_id}: frozen verdict drift")
  assert!(File.binread(paths.fetch(:phase2a_receipt)).include?("[EVIDENCE-COMMITTED]"), "#{paper_id}: Phase-2A terminal marker")
  assert!(roadmap.fetch("items").map { |item| item.fetch("id") } == verdict.fetch("items").map { |item| item.fetch("item_id") }, "#{paper_id}: roadmap/verdict row order")

  if ABORTED.include?(paper_id)
    assert!(phase2a_record.fetch("controlling_status") == "ABORTED", "#{paper_id}: expected Phase-2A abort")
    assert!(phase2a_record.fetch("abort_reason") == "phase2a_lint_failed", "#{paper_id}: abort reason")
    assert!(phase2a_record.fetch("phase2b_eligible") == false, "#{paper_id}: Phase-2B must be forbidden")
    assert!(!File.exist?(paths.fetch(:integration)) && !File.symlink?(paths.fetch(:integration)), "#{paper_id}: forbidden Phase-2B integration exists")
    assert!(!File.exist?(paths.fetch(:trace)) && !File.symlink?(paths.fetch(:trace)), "#{paper_id}: forbidden traceability exists")
  else
    assert!(phase2a_record.fetch("controlling_status") == "PHASE2A_PASS", "#{paper_id}: expected Phase-2A pass")
    assert!(phase2a_record.fetch("phase2b_eligible") == true, "#{paper_id}: Phase-2B eligibility")
    safe_repo_file!(relative(paths.fetch(:integration)))
    safe_repo_file!(relative(paths.fetch(:trace)))
  end

  {
    paper_id: paper_id,
    spec: spec,
    paths: paths,
    round_id: round_id,
    manifest: manifest,
    precommitment: precommitment,
    verdict: verdict,
    roadmap: roadmap,
    phase1_gate: phase1_gate,
    phase2a_record: phase2a_record
  }
end

def derive_decision(data, trace)
  roadmap_by_id = data.fetch(:roadmap).fetch("items").to_h { |item| [item.fetch("id"), item] }
  verdict_by_id = data.fetch(:verdict).fetch("items").to_h { |item| [item.fetch("item_id"), item] }
  rows = trace.fetch("rows")
  must = rows.select { |row| roadmap_by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == "must_fix" }
  should = rows.select { |row| roadmap_by_id.fetch(row.fetch("item_id")).fetch("obligation_class") == "should_fix" }
  new_issues = trace.fetch("new_issues")

  critical_made_worse = must.any? do |row|
    row.fetch("final_verdict") == "MADE_WORSE" && roadmap_by_id.fetch(row.fetch("item_id"))["severity"] == "critical"
  end
  critical_regression = new_issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "critical" }
  negative = must.count { |row| %w[NOT_ADDRESSED MADE_WORSE].include?(row.fetch("final_verdict")) }
  half_negative = !must.empty? && negative * 2 >= must.length
  must_negative = must.any? { |row| %w[NOT_ADDRESSED MADE_WORSE CANNOT_VERIFY].include?(row.fetch("final_verdict")) }
  major_regression = new_issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "major" }
  must_residual = rows.any? do |row|
    verdict_row = verdict_by_id.fetch(row.fetch("item_id"))
    row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && verdict_row.dig("residual_gap", "residual_obligation_class") == "must_fix"
  end
  lower_residual = must.any? do |row|
    verdict_row = verdict_by_id.fetch(row.fetch("item_id"))
    row.fetch("final_verdict") == "PARTIALLY_ADDRESSED" && %w[should_fix consider].include?(verdict_row.dig("residual_gap", "residual_obligation_class"))
  end
  should_numerator = should.count { |row| %w[FULLY_ADDRESSED PARTIALLY_ADDRESSED].include?(row.fetch("final_verdict")) }
  under_eighty = !should.empty? && should_numerator * 5 < should.length * 4
  should_worse = should.any? { |row| row.fetch("final_verdict") == "MADE_WORSE" }
  minor_regression = new_issues.any? { |issue| issue.fetch("attribution") == "regression" && issue.fetch("severity") == "minor" }

  result = if critical_made_worse || critical_regression
             ["Major Revision", "B1", true]
           elsif half_negative
             ["Major Revision", "B2", true]
           elsif must_negative || major_regression
             ["Major Revision", "B3", false]
           elsif must_residual
             ["Major Revision", "B4", false]
           elsif lower_residual || under_eighty || should_worse || minor_regression
             ["Minor Revision", "B5", false]
           else
             ["Accept", "B6", false]
           end
  [*result, should_numerator, should.length]
end

def validate_eligible_trace!(data, gates)
  paper_id = data.fetch(:paper_id)
  paths = data.fetch(:paths)
  integration = load_json(paths.fetch(:integration))
  trace = load_json(paths.fetch(:trace))
  verdict = data.fetch(:verdict)
  roadmap = data.fetch(:roadmap)

  phase2b_row = gates.fetch("phase2b").fetch("papers").find { |row| row.fetch("paper_id") == paper_id }
  assert!(!phase2b_row.nil?, "#{paper_id}: absent from Phase-2B validation")
  assert!(sha256(paths.fetch(:integration)) == phase2b_row.fetch("integration_sha256"), "#{paper_id}: integration drift")
  assert!(jcs_sha256(integration) == phase2b_row.fetch("integration_jcs_sha256"), "#{paper_id}: integration JCS drift")
  assert!(integration.fetch("round_id") == data.fetch(:round_id), "#{paper_id}: integration round id")
  assert!(integration.fetch("verdict_record_hash") == jcs_sha256(verdict), "#{paper_id}: integration/verdict binding")
  assert!(integration.fetch("adjustments").empty?, "#{paper_id}: unexpected Phase-2B adjustment")
  assert!(integration.fetch("post_letter_observations").empty?, "#{paper_id}: unexpected post-letter observation")

  assert!(trace.fetch("contract_version") == "1.1", "#{paper_id}: trace contract")
  assert!(trace.fetch("round_id") == data.fetch(:round_id), "#{paper_id}: trace round id")
  assert!(trace.fetch("revision") == 1, "#{paper_id}: trace revision")
  assert!(trace.fetch("verdict_record_hash") == jcs_sha256(verdict), "#{paper_id}: trace/verdict binding")
  %w[adjustments dissent_adjudications resolution_intents cross_model_resolutions rebuttal_adjudications g2d_acceptances pending_rebuttal_upgrades escalation_approvals reapplications].each do |key|
    assert!(trace.fetch(key).empty?, "#{paper_id}: unsupported nonempty trace channel #{key}")
  end
  assert!(trace.fetch("new_issues") == verdict.fetch("new_issues"), "#{paper_id}: new-issue freeze")
  assert!(trace.fetch("post_letter_observations") == integration.fetch("post_letter_observations"), "#{paper_id}: post-letter observation binding")

  roadmap_ids = roadmap.fetch("items").map { |item| item.fetch("id") }
  verdict_by_id = verdict.fetch("items").to_h { |row| [row.fetch("item_id"), row] }
  integration_by_id = integration.fetch("rows").to_h { |row| [row.fetch("item_id"), row] }
  assert!(trace.fetch("rows").map { |row| row.fetch("item_id") } == roadmap_ids, "#{paper_id}: trace order")
  trace.fetch("rows").each do |row|
    item_id = row.fetch("item_id")
    assert!(VERDICTS.include?(row.fetch("final_verdict")), "#{paper_id}/#{item_id}: invalid verdict")
    assert!(row.fetch("phase2a_verdict") == verdict_by_id.fetch(item_id).fetch("verdict"), "#{paper_id}/#{item_id}: Phase-2A binding")
    assert!(row.fetch("final_verdict") == row.fetch("phase2a_verdict"), "#{paper_id}/#{item_id}: silent verdict change")
    integration_row = integration_by_id.fetch(item_id)
    %w[concern_id original_comment authors_claim revision_location phase2a_verdict final_verdict quality_assessment].each do |key|
      assert!(row.fetch(key) == integration_row.fetch(key), "#{paper_id}/#{item_id}: integration mismatch #{key}")
    end
  end

  decision, rule, reject, should_num, should_den = derive_decision(data, trace)
  assert!(trace.fetch("decision_state") == decision, "#{paper_id}: trace decision derivation")
  assert!(decision == "Major Revision" && rule == "B4", "#{paper_id}: expected Major Revision/B4, got #{decision}/#{rule}")
  assert!(trace.dig("decision_inputs", "apply_chain_witness") == "pass", "#{paper_id}: apply-chain witness")

  data.merge(
    integration: integration,
    trace: trace,
    decision: decision,
    rule: rule,
    reject_recommended: reject,
    should_numerator: should_num,
    should_denominator: should_den,
    counts: count_verdicts(trace.fetch("rows"), "final_verdict")
  )
end

def checker_command(data)
  paths = data.fetch(:paths)
  [
    "python3", "-B", CHECKER,
    "--manifest", paths.fetch(:manifest),
    "--precommitment", paths.fetch(:precommitment),
    "--verdict-record", paths.fetch(:verdict),
    "--traceability", paths.fetch(:trace),
    "--roadmap", paths.fetch(:roadmap),
    "--author-adjudication", paths.fetch(:author),
    "--revision-evidence-bundle", paths.fetch(:bundle),
    "--revision-evidence-root", paths.fetch(:root),
    "--letter", paths.fetch(:letter),
    "--apply-report", paths.fetch(:apply_report)
  ]
end

def run_checker!(data)
  assert!(sha256(safe_external_file!(CHECKER)) == EXPECTED_CHECKER_SHA256, "official checker hash drift")
  stdout, stderr, status = Open3.capture3({"PYTHONDONTWRITEBYTECODE" => "1"}, *checker_command(data), chdir: ROOT)
  assert!(status.exited?, "#{data.fetch(:paper_id)}: checker did not exit normally")
  assert!(status.exitstatus == 0, "#{data.fetch(:paper_id)}: checker exit #{status.exitstatus}: #{[stdout, stderr].join(' ').byteslice(0, 3000)}")
  message = stdout.lines.map(&:strip).find { |line| line.include?("re-review synthesis ok:") }
  assert!(!message.nil?, "#{data.fetch(:paper_id)}: checker success marker missing")
  decision_match = message.match(/decision_state '([^']+)'/)
  apply_match = message.match(/apply_chain_witness '([^']+)'/)
  round_match = message.match(/round '([^']+)'/)
  assert!(decision_match && decision_match[1] == data.fetch(:decision), "#{data.fetch(:paper_id)}: checker decision mismatch")
  assert!(apply_match && apply_match[1] == "pass", "#{data.fetch(:paper_id)}: checker apply-chain mismatch")
  assert!(round_match && round_match[1] == data.fetch(:round_id), "#{data.fetch(:paper_id)}: checker round mismatch")

  paths = data.fetch(:paths)
  {
    "schema_version" => "round10-stage3-prime-round2-checker-receipt/1.0",
    "paper_id" => data.fetch(:paper_id),
    "round_id" => data.fetch(:round_id),
    "checked_at" => FINALIZED_AT,
    "checker" => "ARS-Codex 0.1.26 scripts/check_re_review_synthesis.py",
    "checker_sha256" => EXPECTED_CHECKER_SHA256,
    "checker_status" => "PASS",
    "checker_exit_code" => status.exitstatus,
    "checker_stdout" => stdout,
    "checker_stderr" => stderr,
    "checker_message" => message,
    "decision_emitted" => true,
    "decision_state" => data.fetch(:decision),
    "decision_rule" => data.fetch(:rule),
    "reject_recommended" => data.fetch(:reject_recommended),
    "apply_chain_witness" => "pass",
    "cross_model_status" => "not_configured",
    "phase_counts" => data.fetch(:counts),
    "adjustments" => data.fetch(:trace).fetch("adjustments").length,
    "new_issues" => data.fetch(:trace).fetch("new_issues").length,
    "dissents" => data.fetch(:verdict).fetch("dissents").length,
    "escalation_exceptions" => data.fetch(:verdict).fetch("escalation_exceptions").length,
    "artifacts" => {
      "input_manifest" => bind_json(paths.fetch(:manifest)),
      "precommitment" => bind_json(paths.fetch(:precommitment)),
      "verdict_record" => bind_json(paths.fetch(:verdict)),
      "phase2b_integration" => bind_json(paths.fetch(:integration)),
      "traceability" => bind_json(paths.fetch(:trace)),
      "revision_roadmap" => bind_json(paths.fetch(:roadmap)),
      "author_adjudication" => bind_json(paths.fetch(:author)),
      "revision_evidence_bundle" => bind_json(paths.fetch(:bundle)),
      "editorial_decision_letter" => binding(paths.fetch(:letter)),
      "apply_report" => bind_json(paths.fetch(:apply_report))
    },
    "same_family_disclosure" => DISCLOSURE,
    "boundaries" => {
      "canonical_manuscript_pdf_bibliography_changed" => false,
      "science_results_changed" => false,
      "initial_dynamical_system_changed" => false,
      "route_credit_changed" => false,
      "route_b_invoked" => false,
      "successor_stage_authorized" => false
    }
  }
end

def aborted_checker_receipt(data, gates)
  paths = data.fetch(:paths)
  {
    "schema_version" => "round10-stage3-prime-round2-checker-receipt/1.0",
    "paper_id" => data.fetch(:paper_id),
    "round_id" => data.fetch(:round_id),
    "checked_at" => FINALIZED_AT,
    "checker" => "ARS-Codex 0.1.26 scripts/check_re_review_synthesis.py",
    "checker_sha256" => EXPECTED_CHECKER_SHA256,
    "checker_status" => "NOT_RUN",
    "checker_not_run_reason" => "checker_not_run_due_to_phase2a_abort",
    "checker_exit_code" => nil,
    "checker_stdout" => nil,
    "checker_stderr" => nil,
    "decision_emitted" => false,
    "decision_state" => nil,
    "suppressed_mechanical_candidate" => nil,
    "controlling_status" => "ABORTED",
    "abort_reason" => "phase2a_lint_failed",
    "phase2b_emitted" => false,
    "traceability_emitted" => false,
    "phase2a_retry_used" => false,
    "artifacts" => {
      "input_manifest" => bind_json(paths.fetch(:manifest)),
      "precommitment" => bind_json(paths.fetch(:precommitment)),
      "verdict_record" => bind_json(paths.fetch(:verdict)),
      "phase2a_consolidation" => gates.fetch("phase2a_consolidation"),
      "phase2a_gate" => gates.fetch("phase2a_gate")
    },
    "same_family_disclosure" => DISCLOSURE,
    "boundaries" => {
      "committed_phase2a_record_rewritten" => false,
      "response_to_reviewers_seen" => false,
      "canonical_manuscript_pdf_bibliography_changed" => false,
      "science_results_changed" => false,
      "initial_dynamical_system_changed" => false,
      "route_credit_changed" => false,
      "route_b_invoked" => false,
      "successor_stage_authorized" => false
    }
  }
end

def abort_record(data, gates)
  discrepancies = gates.fetch("consolidation").fetch("disputed_rows").select do |row|
    row.fetch("paper_id") == data.fetch(:paper_id) && !row.fetch("tie_break_matches_committed_record")
  end
  assert!(!discrepancies.empty?, "#{data.fetch(:paper_id)}: abort without controlling discrepancy")
  {
    "schema_version" => "round10-stage3-prime-round2-abort-record/1.0",
    "paper_id" => data.fetch(:paper_id),
    "round_id" => data.fetch(:round_id),
    "status" => "aborted",
    "abort_reason" => "phase2a_lint_failed",
    "detected_at" => FINALIZED_AT,
    "detected_by" => "fresh-context full-row semantic audit plus precommitted blind same-family tie-break",
    "independent_error_process_claimed" => false,
    "phase1_gate_passed" => true,
    "phase2a_structural_gate_passed" => true,
    "phase2a_semantic_gate_passed" => false,
    "phase2a_retry_used" => false,
    "phase2b_emitted" => false,
    "checker_run" => false,
    "decision_emitted" => false,
    "suppressed_mechanical_candidate" => nil,
    "frozen_phase_artifacts_preserved" => true,
    "controlling_discrepancies" => discrepancies,
    "recorded_counts" => data.fetch(:phase2a_record).fetch("recorded_counts"),
    "audit_supported_counts" => data.fetch(:phase2a_record).fetch("controlling_counts"),
    "semantic_evidence" => [gates.fetch("phase2a_consolidation"), gates.fetch("phase2a_gate")],
    "next_round_requirement" => {
      "explicit_scholar_authorization" => true,
      "new_round_id" => true,
      "new_manifest" => true,
      "fresh_phase1_context" => true,
      "fresh_phase2a_context" => true,
      "no_overwrite_of_round1_or_round2" => true
    },
    "boundaries" => {
      "phase_artifacts_rewritten_after_commit" => false,
      "canonical_manuscript_pdf_bibliography_changed" => false,
      "science_results_changed" => false,
      "initial_dynamical_system_changed" => false,
      "route_credit_changed" => false,
      "route_b_invoked" => false,
      "successor_stage_authorized" => false
    }
  }
end

def escape_table(text)
  text.to_s.gsub("|", "\\|").gsub("\n", " ")
end

def compact(text, limit = 220)
  normalized = text.to_s.gsub(/\s+/, " ").strip
  normalized.length > limit ? "#{normalized[0, limit - 1]}…" : normalized
end

def rubric_bindings
  RUBRIC_PATHS.map do |path|
    safe_external_file!(path)
    {"path" => path, "sha256" => sha256(path)}
  end
end

def panel_provenance(data)
  round1 = load_json(File.join(data.fetch(:paths).fetch(:notes), "stage3_prime_round1_checker_receipt.json"))
  record = round1.dig("judge_record", "round1_panel_provenance")
  assert!(record.is_a?(Hash) && record.fetch("status") == "valid", "#{data.fetch(:paper_id)}: invalid frozen Round-1 panel provenance")
  record
end

def eligible_report(data, receipt)
  trace = data.fetch(:trace)
  verdict_by_id = data.fetch(:verdict).fetch("items").to_h { |row| [row.fetch("item_id"), row] }
  provenance = panel_provenance(data)
  checklist = trace.fetch("rows").map do |row|
    [
      row.fetch("concern_id"), row.fetch("item_id"), row.fetch("obligation_class"),
      row.fetch("final_verdict"), row.fetch("verified_by"),
      compact(row.fetch("original_comment")), compact(row.fetch("authors_claim")), compact(row.fetch("revision_location"))
    ]
  end.map { |cells| "| #{cells.map { |cell| escape_table(cell) }.join(' | ')} |" }.join("\n")

  residuals = trace.fetch("rows").filter_map do |row|
    next unless row.fetch("final_verdict") == "PARTIALLY_ADDRESSED"
    residual = verdict_by_id.fetch(row.fetch("item_id")).fetch("residual_gap")
    "- **#{row.fetch('item_id')} — PARTIALLY_ADDRESSED** (`#{residual.fetch('residual_obligation_class')}` residual): #{residual.fetch('text')}"
  end.join("\n")
  residuals = "- None." if residuals.empty?
  counts = data.fetch(:counts)
  axes = provenance.fetch("axes")

  <<~MARKDOWN
    # #{data.fetch(:paper_id)} Stage 3′ Round 2 Verification Review Report

    - **Round id:** `#{data.fetch(:round_id)}`
    - **Decision:** **#{data.fetch(:decision)}**
    - **Mechanical rule:** `#{data.fetch(:rule)}`
    - **Official checker:** PASS (exit 0)
    - **Apply-report chain:** `pass`
    - **Checked at:** `#{FINALIZED_AT}`
    - **Round 1:** preserved byte-for-byte as frozen abort evidence and excluded from the fresh review contexts.

    ## Judge Record (#539)

    - **Verification judge:** OpenAI GPT-5 family through Codex; the exact service model id is not exposed to this artifact layer.
    - **Round-1 panel provenance:** `valid`; artifact `#{provenance.fetch('artifact_path')}`; raw SHA-256 `#{provenance.fetch('artifact_sha256')}`; normalized-manifest SHA-256 `#{provenance.fetch('normalized_manifest_sha256')}`; execution-topology SHA-256 `#{provenance.fetch('execution_topology_sha256')}`.
    - **Six provenance axes:** role-separated=`#{axes.fetch('role_separated')}`; fresh-context=`#{axes.fetch('fresh_context')}` (`#{provenance.fetch('fresh_context_scope')}`); blind-to-peer-outputs=`#{axes.fetch('blind_to_peer_outputs')}`; model-family-distinct=`#{axes.fetch('model_family_distinct')}`; provider-distinct=`#{axes.fetch('provider_distinct')}`; human-distinct=`#{axes.fetch('human_distinct')}`.
    - **Blind cross-model pass:** `not_configured`; no independent-error-process claim is made.
    - **Pre-committed criteria:** JCS SHA-256 `#{jcs_sha256(data.fetch(:precommitment))}`.
    - **Prompt/rubric surfaces:** ARS re-review three-gate protocol and contract family `1.1`; exact hashes are recorded in the checker receipt.
    - **Reviewer configuration:** `round1_cards_reused`.
    - **Routing:** `card_mapped`; the DA seat is not a verification persona.
    - **Evidence seen:** Phase 1 used only frozen Round-1 yardsticks; Phase 2A added original/revised manuscripts and bound patch/apply/bundle evidence while withholding the response; Phase 2B added the response. Author adjudication remained checker-only.
    - **Judging budget:** three gated review calls plus this deterministic checker invocation; exact token telemetry was not retained.

    #{DISCLOSURE}

    ## Decision

    **#{data.fetch(:decision)}** under `#{data.fetch(:rule)}`. The official checker recomputed this decision from the committed artifacts. It is a mandatory Stage 3′ checkpoint, not authorization for Stage 4′.

    ## Revision Response Checklist

    | Ref | Item | Class | Final status | Verified by | Original concern | Author claim | Revision location |
    |---|---|---|---|---|---|---|---|
    #{checklist}

    ## Frozen evidence summary

    - `FULLY_ADDRESSED`: #{counts.fetch('FULLY_ADDRESSED')}
    - `PARTIALLY_ADDRESSED`: #{counts.fetch('PARTIALLY_ADDRESSED')}
    - `NOT_ADDRESSED`: #{counts.fetch('NOT_ADDRESSED')}
    - `MADE_WORSE`: #{counts.fetch('MADE_WORSE')}
    - `CANNOT_VERIFY`: #{counts.fetch('CANNOT_VERIFY')}
    - Phase-2B adjustments: #{trace.fetch('adjustments').length}
    - New issues / dissents / escalation exceptions: #{trace.fetch('new_issues').length} / #{data.fetch(:verdict).fetch('dissents').length} / #{data.fetch(:verdict).fetch('escalation_exceptions').length}
    - Should-fix addressed rate: #{data.fetch(:should_numerator)}/#{data.fetch(:should_denominator)}

    ## Residual issues

    #{residuals}

    ## Concrete paper progress

    #{data.fetch(:spec).fetch(:progress)}

    ## Route-map and initial-system boundary

    - **Frozen system:** #{data.fetch(:spec).fetch(:system)}.
    - **Route position:** #{data.fetch(:spec).fetch(:route)}.
    - This review changed no Route-A tuple, A2 result, Route-B state, system clock/owner/normalization, canonical manuscript, bibliography, PDF, or scientific result.

    ## Checker record

    The official ARS checker exited zero, agreed with `#{data.fetch(:decision)}` / `#{data.fetch(:rule)}`, and replayed the apply chain as `pass`. Exact stdout, stderr, command-input hashes, and checker hash are preserved in `stage3_prime_round2_checker_receipt.json`.

    ## Boundary and next checkpoint

    The next legal transition is **Stage 4′**, only after explicit user authorization. No Stage 4′ work has begun.
  MARKDOWN
end

def aborted_report(data, gates)
  discrepancies = gates.fetch("consolidation").fetch("disputed_rows").select do |row|
    row.fetch("paper_id") == data.fetch(:paper_id) && !row.fetch("tie_break_matches_committed_record")
  end
  rows = discrepancies.map do |row|
    "| #{row.fetch('item_id')} | #{row.fetch('recorded_verdict')} | #{row.fetch('controlling_verdict')} | #{escape_table(row.fetch('reason'))} |"
  end.join("\n")
  recorded = data.fetch(:phase2a_record).fetch("recorded_counts")
  controlling = data.fetch(:phase2a_record).fetch("controlling_counts")

  <<~MARKDOWN
    # #{data.fetch(:paper_id)} Stage 3′ Round 2 Verification Review Report

    - **Round id:** `#{data.fetch(:round_id)}`
    - **Terminal status:** `[RE-REVIEW-ABORT: phase2a_lint_failed]`
    - **Decision emitted:** no
    - **Phase 2B / traceability:** not emitted
    - **Official checker:** not run (`checker_not_run_due_to_phase2a_abort`)
    - **Finalized at:** `#{FINALIZED_AT}`

    ## Why the round stopped

    Phase 1 passed its revision-blind structural and semantic gate. Phase 2A then committed its persuasion-blind evidence record, but a fresh full-row semantic audit and precommitted blind same-family tie-break found the discrepancies below. Because Phase 2A has no retry after evidence exposure, the committed record remains immutable and this paper aborts before the response letter, Phase 2B, traceability, checker, or decision.

    | Item | Committed verdict | Audit-supported verdict | Controlling reason |
    |---|---|---|---|
    #{rows}

    No suppressed Round-2 mechanical candidate is reported: the checker was never legally reachable.

    ## Evidence counts

    - Committed record: #{recorded.fetch('FULLY_ADDRESSED')} fully / #{recorded.fetch('PARTIALLY_ADDRESSED')} partially / #{recorded.fetch('NOT_ADDRESSED')} not addressed / #{recorded.fetch('MADE_WORSE')} made worse / #{recorded.fetch('CANNOT_VERIFY')} cannot verify.
    - Audit-supported controlling read: #{controlling.fetch('FULLY_ADDRESSED')} fully / #{controlling.fetch('PARTIALLY_ADDRESSED')} partially / #{controlling.fetch('NOT_ADDRESSED')} not addressed / #{controlling.fetch('MADE_WORSE')} made worse / #{controlling.fetch('CANNOT_VERIFY')} cannot verify.

    ## Concrete paper progress

    #{data.fetch(:spec).fetch(:progress)}

    ## Provenance limitation

    The semantic audit and tie-break used fresh role-separated contexts but the same model family/provider and the same accountable human. They are not described as independent error processes.

    #{DISCLOSURE}

    ## Route-map and initial-system boundary

    - **Frozen system:** #{data.fetch(:spec).fetch(:system)}.
    - **Route position:** #{data.fetch(:spec).fetch(:route)}.
    - This review changed no Route-A tuple, A2 result, Route-B state, system clock/owner/normalization, canonical manuscript, bibliography, PDF, or scientific result.

    ## Boundary and next checkpoint

    A fresh **Stage 3′ Round 3** requires explicit scholar authorization, a new round id and manifest, and new Phase-1/2A contexts. Round 1 and Round 2 must remain immutable. No successor stage has begun.
  MARKDOWN
end

def build_batch_report(results, gates, checker_receipts)
  rows = PAPERS.keys.map do |paper_id|
    data = results.fetch(paper_id)
    if ABORTED.include?(paper_id)
      counts = data.fetch(:phase2a_record).fetch("controlling_counts")
      outcome = "ABORT `phase2a_lint_failed`"
      next_step = "authorize fresh Stage 3′ Round 3"
      checker = "not run"
    else
      counts = data.fetch(:counts)
      outcome = "#{data.fetch(:decision)} (#{data.fetch(:rule)})"
      next_step = "authorize scoped Stage 4′"
      checker = "PASS"
    end
    report = "papers/#{data.fetch(:spec).fetch(:slug)}/notes/stage3_prime_round2_verification_report.md"
    "| #{paper_id} | #{counts.fetch('FULLY_ADDRESSED')} | #{counts.fetch('PARTIALLY_ADDRESSED')} | #{counts.fetch('NOT_ADDRESSED')} | #{outcome} | #{checker} | #{next_step} | [report](#{report}) |"
  end.join("\n")

  discrepancy_rows = gates.fetch("consolidation").fetch("disputed_rows").select { |row| !row.fetch("tie_break_matches_committed_record") }.map do |row|
    "| #{row.fetch('paper_id')} | #{row.fetch('item_id')} | #{row.fetch('recorded_verdict')} | #{row.fetch('controlling_verdict')} | #{escape_table(row.fetch('reason'))} |"
  end.join("\n")

  <<~MARKDOWN
    # Round 10 Papers 29–33 — Stage 3′ Round 2 Terminal Report

    ## Outcome

    Round 2 is terminally accounted for all five papers. P30 and P31 completed all three evidence-before-persuasion gates and passed the official ARS checker as **Major Revision / B4**. P29, P32 and P33 failed closed at the no-retry Phase-2A semantic gate; for those papers Phase 2B, traceability, checker execution, and editorial decision were correctly not emitted.

    - Phase-1 precommitment rows: **56**; structural and fresh semantic gate PASS for all five.
    - Phase-2A rows: **56**; two paper gates PASS and three paper gates ABORT.
    - Phase-2B/checker scope: **20 rows across P30/P31 only**; checker **2/2 PASS**.
    - Eligible-paper final verdicts: **7 `FULLY_ADDRESSED` + 13 `PARTIALLY_ADDRESSED`**; all other verdict classes 0.
    - Whole-batch audit-supported Phase-2A read: **23 fully + 33 partially**; all other verdict classes 0.
    - Phase-2B adjustments / new issues / dissents / escalations: **0 / 0 / 0 / 0**.
    - Decisions emitted: **2 Major Revision**; decisions suppressed or fabricated for aborted papers: **0**.
    - Canonical manuscript/bibliography/PDF changes: **0 of 15 frozen files**.
    - Science-result changes / new science execution: **0 / 0**.
    - Initial-system changes / Route-A tuple assignments / Route-B invocations: **0 / 0 / 0**.

    ## Per-paper results and concrete progress

    | Paper | Fully | Partially | Not addressed | Outcome | Checker | Next legal action | Report |
    |---|---:|---:|---:|---|---|---|---|
    #{rows}

    #{PAPERS.map { |paper_id, spec| "- **#{paper_id}:** #{spec.fetch(:progress)}" }.join("\n")}

    ## Controlling Phase-2A discrepancies

    | Paper | Item | Committed | Audit-supported | Reason |
    |---|---|---|---|---|
    #{discrepancy_rows}

    These four discrepancies are not patched in place. They are the terminal reason P29/P32/P33 require a newly authorized review round.

    ## Route-map correspondence and frozen systems

    This batch remains on **Route A foundations/interfaces**. A1/A2 preparation is not a formal evaluator pass; P30 remains A0-failed/A2-ineligible, and no paper receives a formal Route-A tuple or positive arithmetic A2 credit. Route B is not invoked.

    #{PAPERS.map { |paper_id, spec| "- **#{paper_id}:** #{spec.fetch(:system)} — #{spec.fetch(:route)}." }.join("\n")}

    This Stage 3′ round performed review verification, not a new dynamical experiment. It re-reviewed five already frozen dynamical-system forms and produced no new scientific result artifact.

    ## Integrity and provenance

    The final integrity audit replayed all **309** frozen bindings: Round-1 terminal artifacts, 15 canonical files, 15 science placeholders with exact inventories, 212 Stage-4 evidence files, five initial-system sources, five route crosswalks, and both route-evaluator definitions. All remained unchanged.

    #{DISCLOSURE}

    ## Mandatory user checkpoint

    This report does not authorize a successor stage.

    - P30 and P31 may enter **Stage 4′** only after explicit confirmation and exact scoped authorization.
    - P29, P32 and P33 may enter a fresh **Stage 3′ Round 3** only after explicit confirmation; the new round must use new ids/manifests and fresh Phase-1/2A contexts.
    - No Stage 4′, Stage 4.5, Stage 5, canonical promotion, submission, Route advancement, or new science round has begun.

    Finalized at `#{FINALIZED_AT}`.
  MARKDOWN
end

def build_checkpoint
  <<~MARKDOWN
    # Round 10 Papers 29–33 — Stage 3′ Round 2 Mandatory Checkpoint

    Round 2 is closed. P30/P31 completed the official checker with **Major Revision / B4**. P29/P32/P33 aborted at `phase2a_lint_failed` before Phase 2B and have no decision.

    No successor-stage authority is implied by this checkpoint.

    - A confirmation may authorize scoped **Stage 4′** preparation for P30/P31.
    - A confirmation may authorize a fresh **Stage 3′ Round 3** for P29/P32/P33.
    - The exact scope must preserve canonical/science/initial-system/Route freezes unless separately and explicitly authorized.
    - Stage 4.5, Stage 5, submission, Route advancement, and new science remain unauthorized.

    Awaiting explicit scholar confirmation.
  MARKDOWN
end

def build_final_audit(results, gates, boundary_replay, terminal_bindings)
  per_paper = PAPERS.keys.map do |paper_id|
    data = results.fetch(paper_id)
    base = {
      "paper_id" => paper_id,
      "round_id" => data.fetch(:round_id),
      "manifest" => bind_json(data.fetch(:paths).fetch(:manifest)),
      "precommitment" => bind_json(data.fetch(:paths).fetch(:precommitment)),
      "verdict_record" => bind_json(data.fetch(:paths).fetch(:verdict)),
      "checker_receipt" => terminal_bindings.fetch(paper_id).fetch("checker_receipt"),
      "verification_report" => terminal_bindings.fetch(paper_id).fetch("verification_report")
    }
    if ABORTED.include?(paper_id)
      base.merge!(
        "terminal_status" => "ABORTED",
        "abort_reason" => "phase2a_lint_failed",
        "phase2b_emitted" => false,
        "checker_run" => false,
        "decision_emitted" => false,
        "abort_record" => terminal_bindings.fetch(paper_id).fetch("abort_record")
      )
    else
      base.merge!(
        "terminal_status" => "COMPLETE",
        "phase2b_emitted" => true,
        "checker_run" => true,
        "decision_emitted" => true,
        "decision_state" => data.fetch(:decision),
        "decision_rule" => data.fetch(:rule),
        "phase2b_integration" => bind_json(data.fetch(:paths).fetch(:integration)),
        "traceability" => bind_json(data.fetch(:paths).fetch(:trace))
      )
    end
    base
  end

  {
    "schema_version" => "round10-stage3-prime-round2-final-integrity-audit/1.0",
    "audited_at" => FINALIZED_AT,
    "status" => "PASS",
    "scope" => "P29-P33 Stage 3-prime Round 2 terminal review artifacts only",
    "builder" => binding(__FILE__),
    "protocol_surfaces" => rubric_bindings,
    "gate_bindings" => gates.slice("authorization", "author_event", "phase1_gate", "phase2a_gate", "phase2a_consolidation", "phase2b_validation"),
    "frozen_boundary_replay" => boundary_replay,
    "papers" => per_paper,
    "batch_report" => binding(File.join(ROOT, BATCH_REPORT_FILE)),
    "mandatory_checkpoint" => binding(File.join(ROOT, BATCH_CHECKPOINT_FILE)),
    "totals" => {
      "frozen_file_bindings_verified" => 309,
      "round1_artifacts_unchanged" => 55,
      "canonical_files_unchanged" => 15,
      "science_files_unchanged" => 15,
      "review_evidence_files_unchanged" => 212,
      "initial_system_sources_unchanged" => 5,
      "route_crosswalks_unchanged" => 5,
      "route_evaluators_unchanged" => 2,
      "phase2a_aborts" => 3,
      "eligible_checker_passes" => 2,
      "decisions_emitted" => 2
    },
    "boundaries" => {
      "canonical_15_of_15_unchanged" => true,
      "science_artifacts_unchanged" => true,
      "science_artifacts_created_or_refreshed" => 0,
      "initial_dynamical_systems_5_of_5_unchanged" => true,
      "route_a_evaluator_unchanged" => true,
      "route_b_evaluator_unchanged" => true,
      "route_crosswalks_5_of_5_unchanged" => true,
      "round1_preserved" => true,
      "round2_committed_phase_artifacts_rewritten" => false,
      "formal_route_a_tuples_assigned" => 0,
      "positive_arithmetic_a2_results" => 0,
      "route_b_invocations" => 0,
      "stage4_prime_authorized" => false,
      "stage4_5_authorized" => false,
      "stage5_authorized" => false,
      "manuscripts_modified" => false,
      "readme_or_state_docs_modified_by_builder" => false
    }
  }
end

def publish_outputs!
  expected = output_paths
  actual = OUTPUTS.keys.map { |path| relative(path) }.sort
  assert!(actual == expected, "terminal output set mismatch: expected #{expected.length}, composed #{actual.length}")

  existing_identical = []
  expected.each do |relative_path|
    destination = File.join(ROOT, relative_path)
    next unless File.exist?(destination) || File.symlink?(destination)
    stat = File.lstat(destination)
    assert!(stat.file? && !stat.symlink?, "unsafe existing output #{relative_path}")
    expected_sha = Digest::SHA256.hexdigest(OUTPUTS.fetch(destination))
    assert!(sha256(destination) == expected_sha, "refusing to overwrite differing terminal output #{relative_path}")
    existing_identical << relative_path
  end

  staging = Dir.mktmpdir("round10-stage3-prime-round2-outcomes-", File.dirname(ROOT))
  created = []
  begin
    expected.each do |relative_path|
      staged = File.join(staging, relative_path)
      FileUtils.mkdir_p(File.dirname(staged), mode: 0o700)
      File.open(staged, File::WRONLY | File::CREAT | File::EXCL, 0o644) do |stream|
        stream.binmode
        stream.write(OUTPUTS.fetch(File.join(ROOT, relative_path)))
        stream.flush
        stream.fsync
      end
    end

    # Batch receipt is the terminal commit marker and is published last.
    order = expected.reject { |path| path == BATCH_RECEIPT_FILE } + [BATCH_RECEIPT_FILE]
    order.each do |relative_path|
      next if existing_identical.include?(relative_path)
      destination = File.join(ROOT, relative_path)
      File.rename(File.join(staging, relative_path), destination)
      created << destination
    end
  rescue Exception # rubocop:disable Lint/RescueException
    created.reverse_each do |path|
      File.unlink(path) if File.file?(path) && !File.symlink?(path)
    rescue StandardError
      # The caller receives the original failure.  A retained newly-created file
      # is visibly outside the commit marker and will fail the next create-only
      # run instead of being overwritten.
    end
    raise
  ensure
    FileUtils.remove_entry_secure(staging) if staging && File.exist?(staging)
  end

  expected.each do |relative_path|
    destination = safe_repo_file!(relative_path)
    assert!(sha256(destination) == Digest::SHA256.hexdigest(OUTPUTS.fetch(destination)), "published hash mismatch #{relative_path}")
  end
  {"created" => created.map { |path| relative(path) }, "already_identical" => existing_identical}
end

def main
  assert!(File.expand_path(__FILE__) == File.join(ROOT, "tools/build_round10_stage3_prime_round2_outcomes.rb"), "unexpected builder location")
  assert!(sha256(safe_external_file!(CHECKER)) == EXPECTED_CHECKER_SHA256, "official checker hash drift")
  pre_boundary = replay_frozen_boundaries!
  gates = validate_root_gates!

  results = PAPERS.to_h do |paper_id, spec|
    data = validate_paper_inputs!(paper_id, spec, gates)
    data = validate_eligible_trace!(data, gates) if ELIGIBLE.include?(paper_id)
    [paper_id, data]
  end

  checker_receipts = {}
  results.each do |paper_id, data|
    receipt = ELIGIBLE.include?(paper_id) ? run_checker!(data) : aborted_checker_receipt(data, gates)
    checker_receipts[paper_id] = receipt
    notes_rel = "papers/#{data.fetch(:spec).fetch(:slug)}/notes"
    queue_output!(File.join(notes_rel, "stage3_prime_round2_checker_receipt.json"), JSON.pretty_generate(receipt) + "\n")
    if ABORTED.include?(paper_id)
      queue_output!(File.join(notes_rel, "stage3_prime_round2_abort_record.json"), JSON.pretty_generate(abort_record(data, gates)) + "\n")
      report = aborted_report(data, gates)
    else
      report = eligible_report(data, receipt)
    end
    queue_output!(File.join(notes_rel, "stage3_prime_round2_verification_report.md"), report)
  end

  queue_output!(BATCH_REPORT_FILE, build_batch_report(results, gates, checker_receipts))
  queue_output!(BATCH_CHECKPOINT_FILE, build_checkpoint)

  # Re-run every frozen binding after checker execution and report composition.
  post_boundary = replay_frozen_boundaries!
  assert!(pre_boundary == post_boundary, "frozen boundary changed during finalization")

  terminal_bindings = PAPERS.to_h do |paper_id, spec|
    base = "papers/#{spec.fetch(:slug)}/notes"
    row = {
      "checker_receipt" => binding(File.join(ROOT, base, "stage3_prime_round2_checker_receipt.json")),
      "verification_report" => binding(File.join(ROOT, base, "stage3_prime_round2_verification_report.md"))
    }
    row["abort_record"] = binding(File.join(ROOT, base, "stage3_prime_round2_abort_record.json")) if ABORTED.include?(paper_id)
    [paper_id, row]
  end
  audit = build_final_audit(results, gates, post_boundary, terminal_bindings)
  queue_output!(FINAL_AUDIT_FILE, JSON.pretty_generate(audit) + "\n")

  audit_receipt = {
    "schema_version" => "round10-stage3-prime-round2-final-integrity-receipt/1.0",
    "issued_at" => FINALIZED_AT,
    "status" => "PASS",
    "final_integrity_audit" => binding(File.join(ROOT, FINAL_AUDIT_FILE), jcs: true),
    "frozen_file_bindings_verified" => 309,
    "eligible_checker_passes" => 2,
    "phase2a_fail_closed_aborts" => 3,
    "canonical_files_unchanged" => 15,
    "science_artifacts_created_or_refreshed" => 0,
    "route_or_initial_system_changes" => 0,
    "successor_stage_authorized" => false
  }
  queue_output!(FINAL_AUDIT_RECEIPT_FILE, JSON.pretty_generate(audit_receipt) + "\n")

  receipt_bindings = output_paths.reject { |path| path == BATCH_RECEIPT_FILE }.to_h do |path|
    [path, binding(File.join(ROOT, path))]
  end
  batch_receipt = {
    "schema_version" => "round10-stage3-prime-round2-terminal-receipt/1.0",
    "committed_at" => FINALIZED_AT,
    "status" => "PASS_WITH_THREE_FAIL_CLOSED_ABORTS",
    "papers" => PAPERS.keys.map do |paper_id|
      data = results.fetch(paper_id)
      if ABORTED.include?(paper_id)
        {
          "paper_id" => paper_id, "terminal_status" => "ABORTED",
          "abort_reason" => "phase2a_lint_failed", "checker_run" => false,
          "decision_emitted" => false, "next_checkpoint" => "authorize fresh Stage 3-prime Round 3"
        }
      else
        {
          "paper_id" => paper_id, "terminal_status" => "COMPLETE",
          "checker_run" => true, "checker_status" => "PASS",
          "decision_emitted" => true, "decision_state" => data.fetch(:decision),
          "decision_rule" => data.fetch(:rule), "next_checkpoint" => "authorize scoped Stage 4-prime"
        }
      end
    end,
    "terminal_artifacts" => receipt_bindings,
    "final_integrity_receipt" => binding(File.join(ROOT, FINAL_AUDIT_RECEIPT_FILE), jcs: true),
    "boundaries" => {
      "round1_preserved" => true,
      "canonical_15_of_15_unchanged" => true,
      "science_changes" => 0,
      "initial_system_changes" => 0,
      "route_a_or_b_changes" => 0,
      "stage4_prime_authorized" => false,
      "stage4_5_authorized" => false,
      "stage5_authorized" => false
    }
  }
  queue_output!(BATCH_RECEIPT_FILE, JSON.pretty_generate(batch_receipt) + "\n")

  # Final boundary replay occurs after every byte is composed and before any
  # publication.  The checker and generator therefore cannot silently alter a
  # frozen input and still reach the commit marker.
  assert!(replay_frozen_boundaries! == pre_boundary, "final pre-publication boundary drift")
  publication = publish_outputs!
  puts JSON.pretty_generate({
    "status" => "PASS_WITH_THREE_FAIL_CLOSED_ABORTS",
    "created_outputs" => publication.fetch("created"),
    "already_identical_outputs" => publication.fetch("already_identical"),
    "eligible_decisions" => {"P30" => "Major Revision/B4", "P31" => "Major Revision/B4"},
    "aborted_before_checker" => ABORTED,
    "frozen_bindings_verified" => 309,
    "commit_marker" => BATCH_RECEIPT_FILE
  })
end

main if $PROGRAM_NAME == __FILE__
