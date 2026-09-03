#!/usr/bin/env ruby
# frozen_string_literal: true

# Rebuild the terminal Round-10 Stage-3-prime outcome from frozen protocol
# artifacts plus the persisted, fresh-context semantic audits.  This script
# emits review/audit records only.  It never edits a manuscript, bibliography,
# PDF, result tree, Route record, or successor-stage authorization.

require "digest"
require "fileutils"
require "find"
require "json"
require "open3"
require "tmpdir"
require "time"

ROOT = File.expand_path("..", __dir__)
FROZEN_REPOSITORY_ROOT = "/root/autodl-tmp/flow_systems"
CHECKED_AT = "2026-09-03T08:41:00Z"
CHECKER_SHA = "8347ec3766857366cc0c6ffd30021afcebf8d0528a83927fabfce9ecb66a59ab"
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite"
PROTOCOL_PATH = "#{ARS_ROOT}/ars/academic-paper-reviewer/references/re_review_mode_protocol.md"
WORKFLOW_PATH = "#{ARS_ROOT}/ars/academic-paper-reviewer/WORKFLOW.md"
CONTRACT_ROOT = "#{ARS_ROOT}/ars/shared/contracts/re_review"
RUBRIC_PATHS = [
  WORKFLOW_PATH,
  PROTOCOL_PATH,
  "#{CONTRACT_ROOT}/input_manifest.schema.json",
  "#{CONTRACT_ROOT}/precommitment.schema.json",
  "#{CONTRACT_ROOT}/verdict_record.schema.json",
  "#{CONTRACT_ROOT}/traceability.schema.json",
  "#{ARS_ROOT}/ars/scripts/check_re_review_synthesis.py"
].freeze
DISCLOSURE = "This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2)."

SEMANTIC_FILES = [
  "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P29_P30.json",
  "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P31_P32.json",
  "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_TIEBREAK_P33.json",
  "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P33_CRITERION_CONFIRMATION.json"
].freeze
CONSOLIDATION_FILE = "BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_CONSOLIDATION.json"
FINAL_AUDIT_FILE = "BATCH_ROUND10_STAGE3_PRIME_FINAL_AUDIT.json"
FINAL_AUDIT_TOOL = File.join(ROOT, "tools", "audit_round10_stage3_prime_final.py")
BUILDER_REENTRY_ENV = "ROUND10_STAGE3_PRIME_BUILDER_RUNNING"
PAPER_TOP_LEVEL = %w[README.md code experiments notes paper results].freeze
SCIENCE_ROOTS = %w[code experiments results paper/figures].freeze
PER_PAPER_GENERATED_PATHS = %w[
  notes/stage3_prime_round1_checker_receipt.json
  notes/stage3_prime_round1_abort_record.json
  notes/stage3_prime_round1_verification_report.md
].freeze
SUCCESSOR_PATTERN = /(?:round[\s_.-]*2|stage[\s_.-]*4(?:[\s_.-]*(?:prime|′))|stage[\s_.-]*4[\s_.-]*5|stage[\s_.-]*5|submission[\s_.-]*receipt)/i
ROUND10_PATTERN = /round[\s_.-]*10/i
OUTPUT_BUFFER = {}

class PublicationError < StandardError
  attr_reader :rollback_complete, :recovery_backup_path

  def initialize(message, rollback_complete:, recovery_backup_path: nil)
    super(message)
    @rollback_complete = rollback_complete
    @recovery_backup_path = recovery_backup_path
  end
end

TIE_ROWS = {
  "P29" => %w[REV-EIC-1],
  "P30" => %w[REV-EIC-W4 REV-R2-W1 REV-R3-W1-DA-N1],
  "P31" => %w[REV-P31-005 REV-P31-009 REV-P31-010],
  "P32" => %w[REV-P32-R1-W1 REV-P32-R1-W2 REV-P32-R3-W1 REV-P32-DA-M1]
}.freeze

PAPERS = {
  "P29" => {
    slug: "29-bianchi-ideal-owner-refinement",
    title: "Bianchi ideal-owner refinement",
    recorded: [7, 4, 0], audited: [6, 5, 0],
    mechanical_rule: "B4", abort_reason: "phase2a_lint_failed",
    state: "stage3_prime_round1_aborted_awaiting_round2_authorization",
    route: "A0/A1 foundation/interface preparation; formal tuple UNASSIGNED; positive arithmetic A2 = 0; Route B uninvoked",
    route_sha256: "3946edf4f1f2ffc52343f9e9471b81bef590c59bd084ad5db049b6cb89da9445",
    system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
    inventory_sha256: "67127ecade13770b8c5a05903a5db42c8fdac031c34865f12ec9f1d8c601e368",
    protected_tree_sha256: "18336c3a465351e2f27f09a1d9e1859576631d11205449c3e1033a61b55e1965",
    canonical_sha256: {
      "paper/manuscript.tex" => "5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034",
      "paper/references.bib" => "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
      "paper/paper.pdf" => "14dd360e0152da9c976c88bfe3ca197449017d49e09ea75279d4099457f1044e"
    },
    progress: "Gate M/Q, inversion/conjugation semantics, and fail-closed interfaces remain concrete manuscript advances; the review round overcredited the adaptation-versus-synthesis labeling and therefore emits no decision.",
    overrides: {"REV-EIC-1" => "PARTIALLY_ADDRESSED"},
    defects: [
      {
        "item_id" => "REV-EIC-1", "recorded" => "FULLY_ADDRESSED",
        "audit_supported" => "PARTIALLY_ADDRESSED", "kind" => "phase2a_overcredit",
        "reason" => "The comparison classes, contribution unit, and novelty limitation are present, but the text does not explicitly identify which elements are adaptations versus the synthesized contribution."
      }
    ],
    criterion_defects: [],
    advisory: "B0049's same-family role-separation wording should be changed from ‘independently assessed’ to procedurally separated/same-family wording within the already-PARTIAL REV-EIC-2 residual."
  },
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    title: "Three-disk nonconstant-roof determinant",
    recorded: [4, 5, 0], audited: [4, 5, 0],
    mechanical_rule: "B4", abort_reason: "phase1_lint_failed",
    state: "stage3_prime_round1_aborted_awaiting_round2_authorization",
    route: "A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; Route B uninvoked",
    route_sha256: "d1af9901e66450ca88d01419a9fe02d6606bac2f7e7e0999a14a9213bb9ce166",
    system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
    inventory_sha256: "67127ecade13770b8c5a05903a5db42c8fdac031c34865f12ec9f1d8c601e368",
    protected_tree_sha256: "3546ea8f98d61eeb8493936e03b388ef3f6bf0a324eae47e0ee8e5610a32a0ab",
    canonical_sha256: {
      "paper/manuscript.tex" => "af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506",
      "paper/references.bib" => "1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f",
      "paper/paper.pdf" => "c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e"
    },
    progress: "The physical-roof six-gate architecture, common-norm uncertainty channels, owner witness, and typed control surfaces remain substantive manuscript progress; the review round, not the manuscript bytes, failed its Phase-1 yardstick contract.",
    overrides: {"REV-EIC-W4" => "FULLY_ADDRESSED", "REV-R3-W1-DA-N1" => "PARTIALLY_ADDRESSED"},
    defects: [
      {
        "item_id" => "REV-EIC-W4", "recorded" => "PARTIALLY_ADDRESSED",
        "audit_supported" => "FULLY_ADDRESSED", "kind" => "phase2a_undercredit_from_criterion_extension",
        "reason" => "The exact criterion asks for reader-facing method language. Phase 1 added a retained-history-as-provenance condition, and that added condition became the sole residual."
      },
      {
        "item_id" => "REV-R3-W1-DA-N1", "recorded" => "FULLY_ADDRESSED",
        "audit_supported" => "PARTIALLY_ADDRESSED", "kind" => "phase2a_overcredit",
        "reason" => "The six gates and closed state vocabulary are present, but the consolidated surface prescribes rather than populates every required per-gate input/output/hash/uncertainty/receipt/consumer/permission field."
      }
    ],
    criterion_defects: [
      {
        "item_id" => "REV-EIC-W4", "kind" => "unrecorded_semantic_extension_decision_relevant",
        "reason" => "Phase 1 added ‘any retained internal history is separated as provenance,’ which is absent from the immutable roadmap criterion and changed the row verdict."
      },
      {
        "item_id" => "REV-R3-W1-DA-N1", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 expanded the required current-state vocabulary beyond the exact not-started versus prerequisite-blocked distinction; the revision happens to satisfy the addition, so it does not cause the audited PARTIAL."
      }
    ],
    advisory: "B0061's same-family role-separation wording should be handled inside a future valid review/revision scope; it is not an independently authorized new issue here."
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    title: "Level-11 conjugacy owner ledger",
    recorded: [4, 6, 1], audited: [3, 7, 1],
    mechanical_rule: "B3", abort_reason: "phase1_lint_failed",
    state: "stage3_prime_round1_aborted_awaiting_round2_authorization",
    route: "A1-only preparation; formal tuple UNASSIGNED; positive arithmetic A2 = 0; Route B uninvoked",
    route_sha256: "e851c2ee493414fe26321740aac277e95cd196372a11bc2618eb089b8ad1eff2",
    system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree is distinct",
    inventory_sha256: "43a5f544c1dce282b1977fe10ebf0d408e9c029fb9e839ea2b5dbf5368fc77e5",
    protected_tree_sha256: "0678fd9cb5faa73cb8dcae77604d5eadd3a5f4125de1fccfc9c1d13d07b5c2f8",
    canonical_sha256: {
      "paper/manuscript.tex" => "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a",
      "paper/references.bib" => "b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958",
      "paper/paper.pdf" => "f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722"
    },
    progress: "Owner canonicalization, G/I/C materializations, and the 9,453-pair adversarial audit architecture remain concrete manuscript advances; one frozen row overcredits the missing consolidated table, and two Phase-1 operationalizations changed the frozen yardstick.",
    overrides: {"REV-P31-009" => "PARTIALLY_ADDRESSED"},
    defects: [
      {
        "item_id" => "REV-P31-009", "recorded" => "FULLY_ADDRESSED",
        "audit_supported" => "PARTIALLY_ADDRESSED", "kind" => "phase2a_overcredit_from_criterion_weakening",
        "reason" => "The exact criterion requires one consolidated table; the revision distributes the schema and projection constraints across prose blocks."
      }
    ],
    criterion_defects: [
      {
        "item_id" => "REV-P31-005", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 added an independent direct-solver route and separately identified byte-expansion checks beyond the exact observable-equivalence criterion; no row-verdict effect."
      },
      {
        "item_id" => "REV-P31-009", "kind" => "unrecorded_semantic_extension_and_weakening_decision_relevant",
        "reason" => "Phase 1 weakened ‘one consolidated table’ to a generic relational-schema surface while adding extra schema fields; the weakening allowed distributed prose to receive FULL credit."
      }
    ],
    advisory: nil
  },
  "P32" => {
    slug: "32-homology-cover-renormalization-uniformity",
    title: "Homology-cover renormalization uniformity",
    recorded: [6, 5, 1], audited: [6, 5, 1],
    mechanical_rule: "B3", abort_reason: "phase1_lint_failed",
    state: "stage3_prime_round1_aborted_awaiting_round2_authorization",
    route: "generic A1–A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; Route B uninvoked",
    route_sha256: "570b8d7307913495053c69560ccd04e0d37ab6dbcd99fbe53248b81db296fcda",
    system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
    inventory_sha256: "d046915a133bfb0b561220d10bb9099fb280dcb4f3cee463a061821dc8729c89",
    protected_tree_sha256: "62ce28c55c794f375fb1123b834fcfe175024e59d4505e4202a126dba5aa203f",
    canonical_sha256: {
      "paper/manuscript.tex" => "4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a",
      "paper/references.bib" => "e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9",
      "paper/paper.pdf" => "66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93"
    },
    progress: "Higher/zero-content falsification order, the two modulus schedules, and the dependency table remain explicit manuscript advances. Row-level overcredit and undercredit cancel only in the aggregate count, while Phase-1 yardstick drift invalidates this review round.",
    overrides: {"REV-P32-R1-W2" => "PARTIALLY_ADDRESSED", "REV-P32-R3-W1" => "FULLY_ADDRESSED"},
    defects: [
      {
        "item_id" => "REV-P32-R1-W2", "recorded" => "FULLY_ADDRESSED",
        "audit_supported" => "PARTIALLY_ADDRESSED", "kind" => "phase2a_overcredit",
        "reason" => "The analytic registry names AN-1–AN-5 and generic future requirements, but it does not populate every current row with explicit indices, coupling, compact domain, limit order, majorant, and interchange statement."
      },
      {
        "item_id" => "REV-P32-R3-W1", "recorded" => "PARTIALLY_ADDRESSED",
        "audit_supported" => "FULLY_ADDRESSED", "kind" => "phase2a_undercredit_from_criterion_extension",
        "reason" => "B0131 covers every named surface with status and dependency edges; the residual enforced extra per-row fields absent from the immutable criterion."
      }
    ],
    criterion_defects: [
      {
        "item_id" => "REV-P32-R3-W1", "kind" => "unrecorded_semantic_extension_decision_relevant",
        "reason" => "Phase 1 added per-row domain, codomain, equality, topology, and local-survival fields and used them to undergrade the row."
      },
      {
        "item_id" => "REV-P32-DA-M1", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 added a downstream-order condition for richer formal products beyond the exact scalar-lemma-or-inadmissibility criterion; no row-verdict effect."
      }
    ],
    advisory: "B0018's wording should be clarified only through a future authorized scope tied to the existing REV-P32-EIC-W1 residual."
  },
  "P33" => {
    slug: "33-bolza-control-matched-census",
    title: "Bolza control-matched census",
    recorded: [6, 7, 0], audited: [6, 7, 0],
    mechanical_rule: "B4", abort_reason: "phase1_lint_failed",
    state: "stage3_prime_round1_aborted_awaiting_round2_authorization",
    route: "A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; Route B uninvoked",
    route_sha256: "0434982b38bf658bfd808469671431f089140850ceb2c01875539ef997f942cf",
    system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
    inventory_sha256: "85c40122dde748aa643a9a3c5e404239553e7312962e522e464ed1acfef64430",
    protected_tree_sha256: "4bb0015c97ec7f9e31fdef3f43d2dfbb2bf136a138db8ed0579c0206d2e63b90",
    canonical_sha256: {
      "paper/manuscript.tex" => "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
      "paper/references.bib" => "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
      "paper/paper.pdf" => "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031"
    },
    progress: "BP/CP producer contracts, owner/inverse/repetition rules, canonical serialization, migration, and the trust graph remain concrete manuscript advances; the 6/7/0 B4 row result is semantically stable, but seven Phase-1 rows carry unregistered yardstick drift and therefore no decision can issue.",
    overrides: {},
    defects: [],
    criterion_defects: [
      {
        "item_id" => "REV-P33-001", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 added priority claims and comparison-exclusive documentary support to an exact criterion that binds originality statements to documented support."
      },
      {
        "item_id" => "REV-P33-003", "kind" => "unrecorded_semantic_weakening",
        "reason" => "Phase 1 relaxed the exact references.bib carrier to an undefined broader references surface."
      },
      {
        "item_id" => "REV-P33-004", "kind" => "unrecorded_semantic_extension_and_weakening",
        "reason" => "Phase 1 promoted a four-part suggested-action decomposition into the pass test while narrowing all retained phase history to numbered-phase history."
      },
      {
        "item_id" => "REV-P33-006", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 added a versioned-schema condition to the exact byte/schema/registry/validator/fixture criterion."
      },
      {
        "item_id" => "REV-P33-007", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 added theorem-bounded enumeration and a separate exact-comparison-method condition."
      },
      {
        "item_id" => "REV-P33-009", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 strengthened exact generator data to proof-bearing generator data."
      },
      {
        "item_id" => "REV-P33-012", "kind" => "unrecorded_semantic_extension",
        "reason" => "Phase 1 added a mandatory transformation contract to the exact schema/registry digest, migration version/digest, and full-revalidation criterion."
      }
    ],
    advisory: nil
  }
}.freeze

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
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

def escape_table(text)
  text.to_s.gsub("|", "\\|").gsub("\n", " ")
end

def ensure_semantic!(condition, message)
  raise "semantic-source validation failed: #{message}" unless condition
end

def ensure_boundary!(condition, message)
  raise "boundary validation failed: #{message}" unless condition
end

def relative_to_root(path)
  expanded = File.expand_path(path)
  prefix = ROOT.end_with?(File::SEPARATOR) ? ROOT : "#{ROOT}#{File::SEPARATOR}"
  ensure_boundary!(expanded.start_with?(prefix), "path escapes repository root: #{path}")
  expanded.delete_prefix(prefix)
end

def declared_path(path)
  if path.start_with?(File::SEPARATOR)
    expanded = File.expand_path(path)
    current_prefix = "#{ROOT}#{File::SEPARATOR}"
    frozen_prefix = "#{FROZEN_REPOSITORY_ROOT}#{File::SEPARATOR}"
    ars_prefix = "#{ARS_ROOT}#{File::SEPARATOR}"

    if expanded.start_with?(current_prefix)
      relative_to_root(expanded)
      return expanded
    end
    if expanded.start_with?(frozen_prefix)
      relative = expanded.delete_prefix(frozen_prefix)
      remapped = File.expand_path(relative, ROOT)
      relative_to_root(remapped)
      return remapped
    end
    return expanded if expanded == ARS_ROOT || expanded.start_with?(ars_prefix)

    raise "semantic-source validation failed: undeclared absolute path #{path}"
  end

  expanded = File.expand_path(path, ROOT)
  relative_to_root(expanded)
  expanded
end

def expected_output_paths
  paths = [
    CONSOLIDATION_FILE,
    "BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md",
    "BATCH_ROUND10_STAGE3_PRIME_MANDATORY_CHECKPOINT.md",
    "BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json"
  ]
  PAPERS.each_value do |spec|
    PER_PAPER_GENERATED_PATHS.each do |relative|
      paths << File.join("papers", spec.fetch(:slug), relative)
    end
  end
  paths.sort.freeze
end

def assert_regular_no_symlink!(path, label)
  expanded = File.expand_path(path)
  relative = relative_to_root(expanded)
  cursor = ROOT
  relative.split(File::SEPARATOR)[0...-1].each do |part|
    cursor = File.join(cursor, part)
    stat = File.lstat(cursor)
    ensure_boundary!(!stat.symlink?, "#{label}: symlink ancestor #{relative_to_root(cursor)}")
    ensure_boundary!(stat.directory?, "#{label}: non-directory ancestor #{relative_to_root(cursor)}")
  end
  stat = File.lstat(expanded)
  ensure_boundary!(!stat.symlink?, "#{label}: symlink target #{relative}")
  ensure_boundary!(stat.file?, "#{label}: target is not a regular file #{relative}")
  ensure_boundary!(stat.nlink == 1, "#{label}: hard-linked target #{relative} (nlink=#{stat.nlink})")
  expanded
rescue Errno::ENOENT
  raise "boundary validation failed: #{label}: missing path #{relative || path}"
end

def assert_safe_output!(path)
  expanded = assert_regular_no_symlink!(path, "output")
  relative = relative_to_root(expanded)
  ensure_boundary!(expected_output_paths.include?(relative), "undeclared output target #{relative}")
  expanded
end

def binding(path)
  expanded = File.expand_path(path)
  relative = relative_to_root(expanded)
  bytes = OUTPUT_BUFFER[expanded]
  digest = bytes ? Digest::SHA256.hexdigest(bytes) : sha256(expanded)
  {"path" => relative, "sha256" => digest}
end

def queue_output!(path, content)
  expanded = assert_safe_output!(path)
  ensure_boundary!(!OUTPUT_BUFFER.key?(expanded), "duplicate output target #{relative_to_root(expanded)}")
  OUTPUT_BUFFER[expanded] = content.encode(Encoding::UTF_8).b
end

def tree_digest(root, content:, excluded_paths: [])
  root = File.expand_path(root)
  excluded = excluded_paths.to_h { |path| [path, true] }
  rows = []
  Find.find(root) do |path|
    next if path == root

    relative = path.delete_prefix("#{root}#{File::SEPARATOR}")
    stat = File.lstat(path)
    if stat.symlink?
      kind = "symlink:#{File.readlink(path)}"
      Find.prune
    elsif stat.directory?
      kind = "directory"
    elsif stat.file?
      kind = content ? "file:#{sha256(path)}" : "file"
    else
      kind = "other:#{stat.ftype}"
    end
    rows << "#{kind}\0#{relative}" unless excluded.key?(relative)
  end
  Digest::SHA256.hexdigest(rows.sort.join("\n").b)
end

def tree_symlinks(root)
  hits = []
  Find.find(root) do |path|
    next if path == root

    stat = File.lstat(path)
    next unless stat.symlink?

    hits << relative_to_root(path)
    Find.prune
  end
  hits.sort
end

def successor_hits
  paper_prefixes = PAPERS.values.map { |spec| "papers/#{spec.fetch(:slug)}/" }
  hits = []
  Find.find(ROOT) do |path|
    next if path == ROOT

    relative = relative_to_root(path)
    in_target_paper = paper_prefixes.any? { |prefix| relative.start_with?(prefix) }
    next unless in_target_paper || ROUND10_PATTERN.match?(relative)

    hits << relative if SUCCESSOR_PATTERN.match?(relative)
  end
  hits.sort
end

def evaluation_hits
  root = File.join(ROOT, "evaluations")
  return [] unless File.exist?(root) || File.symlink?(root)

  stat = File.lstat(root)
  ensure_boundary!(stat.directory? && !stat.symlink?, "evaluations root type/symlink boundary")
  symlinks = tree_symlinks(root)
  ensure_boundary!(symlinks.empty?, "evaluation-tree symlinks present: #{symlinks.join(', ')}")

  labels = PAPERS.keys
  hits = []
  Find.find(root) do |path|
    next unless File.file?(path)

    bytes = File.binread(path)
    hits << relative_to_root(path) if labels.any? { |label| bytes.include?(label) }
  end
  hits.sort
end

def verify_boundaries!
  declared_root_files = (
    expected_output_paths + SEMANTIC_FILES + [
      FINAL_AUDIT_FILE,
      "tools/build_round10_stage3_prime_outcomes.rb",
      "tools/audit_round10_stage3_prime_final.py",
      "BATCH_ROUND10_STAGE3_PRIME_AUTHOR_EVENT_20260903.txt",
      "BATCH_ROUND10_STAGE3_PRIME_AUTHORIZATION_RECORD.md",
      "BATCH_ROUND10_STAGE3_PRIME_PHASE1_VALIDATION.json",
      "BATCH_ROUND10_STAGE3_PRIME_PHASE2A_VALIDATION.json",
      "BATCH_ROUND10_STAGE3_PRIME_PHASE2B_INTEGRATION_VALIDATION.json"
    ]
  ).uniq
  declared_root_files.each do |relative|
    assert_regular_no_symlink!(File.join(ROOT, relative), "declared Round-10 root input/output")
  end

  paper_snapshots = {}
  PAPERS.each do |paper_id, spec|
    paper = File.join(ROOT, "papers", spec.fetch(:slug))
    symlinks = tree_symlinks(paper)
    ensure_boundary!(symlinks.empty?, "#{paper_id}: symlinks present: #{symlinks.join(', ')}")
    top_level = Dir.children(paper).sort
    ensure_boundary!(top_level == PAPER_TOP_LEVEL.sort,
                     "#{paper_id}: exact top-level inventory")
    PAPER_TOP_LEVEL.each do |name|
      path = File.join(paper, name)
      stat = File.lstat(path)
      expected_type = name == "README.md" ? :file? : :directory?
      ensure_boundary!(stat.public_send(expected_type),
                       "#{paper_id}: top-level type #{name}")
    end

    inventory = tree_digest(paper, content: false)
    ensure_boundary!(inventory == spec.fetch(:inventory_sha256),
                     "#{paper_id}: full path/type inventory mismatch: #{inventory}")
    protected = tree_digest(
      paper,
      content: true,
      excluded_paths: PER_PAPER_GENERATED_PATHS
    )
    ensure_boundary!(protected == spec.fetch(:protected_tree_sha256),
                     "#{paper_id}: protected tree content mismatch: #{protected}")

    spec.fetch(:canonical_sha256).each do |relative, expected|
      path = assert_regular_no_symlink!(File.join(paper, relative), "#{paper_id} canonical")
      ensure_boundary!(sha256(path) == expected, "#{paper_id}: canonical hash #{relative}")
    end

    SCIENCE_ROOTS.each do |relative|
      science_root = File.join(paper, relative)
      stat = File.lstat(science_root)
      ensure_boundary!(stat.directory? && !stat.symlink?,
                       "#{paper_id}: science root type #{relative}")
      ensure_boundary!(Dir.children(science_root).sort == [".gitkeep"],
                       "#{paper_id}: science root exact inventory #{relative}")
      assert_regular_no_symlink!(File.join(science_root, ".gitkeep"),
                                 "#{paper_id} science placeholder")
    end

    route_path = assert_regular_no_symlink!(File.join(paper, "notes", "stage4_route_crosswalk.md"),
                                           "#{paper_id} Route crosswalk")
    route_text = File.binread(route_path).force_encoding(Encoding::UTF_8)
    ensure_boundary!(sha256(route_path) == spec.fetch(:route_sha256),
                     "#{paper_id}: Route crosswalk hash")
    ensure_boundary!(route_text.include?(spec.fetch(:system)),
                     "#{paper_id}: frozen dynamical-system text")
    %w[
      FORMAL_ROUTE_A_TUPLE=UNASSIGNED
      POSITIVE_ARITHMETIC_A2=0
      STAGE4_ROUTE_PROMOTION=NONE
      ROUTE_B_INVOKED=false
      CANONICAL_RESULTS_REFRESHED=false
    ].each do |token|
      ensure_boundary!(route_text.include?(token), "#{paper_id}: Route boundary token #{token}")
    end

    paper_snapshots[paper_id] = {
      "inventory_sha256" => inventory,
      "protected_tree_sha256" => protected
    }
  end

  successors = successor_hits
  ensure_boundary!(successors.empty?, "successor-stage paths present: #{successors.join(', ')}")
  evaluations = evaluation_hits
  ensure_boundary!(evaluations.empty?, "P29-P33 Route evaluation artifacts present: #{evaluations.join(', ')}")

  {
    "papers" => paper_snapshots,
    "canonical_or_science_writes" => 0,
    "route_changes" => 0,
    "successor_stage_authorized" => false,
    "phase_artifacts_rewritten_after_commit" => false,
    "canonical_manuscript_pdf_bibliography_changed" => false,
    "science_results_changed" => false,
    "initial_dynamical_system_changed" => false,
    "route_credit_changed" => false,
    "route_b_invoked" => false,
    "formal_route_a_tuples_assigned" => 0,
    "positive_arithmetic_a2_results" => 0,
    "route_b_invocations" => 0,
    "initial_dynamical_systems_changed" => 0,
    "canonical_manuscripts_changed" => 0,
    "canonical_bibliographies_changed" => 0,
    "canonical_pdfs_changed" => 0,
    "scientific_result_artifacts_changed" => 0
  }
end

def write_staged_file(path, bytes, mode)
  FileUtils.mkdir_p(File.dirname(path), mode: 0o700)
  File.open(path, File::WRONLY | File::CREAT | File::EXCL, mode) do |stream|
    stream.binmode
    stream.write(bytes)
    stream.flush
    stream.fsync
  end
end

def restore_files!(builder_backups, final_audit_backup)
  errors = []
  builder_backups.reverse_each do |destination, backup|
    begin
      File.rename(backup, destination)
    rescue Exception => error # rubocop:disable Lint/RescueException
      errors << "#{relative_to_root(destination)}: #{error.class}: #{error.message}"
    end
  end
  if final_audit_backup
    destination, backup = final_audit_backup
    begin
      File.rename(backup, destination)
    rescue Exception => error # rubocop:disable Lint/RescueException
      errors << "#{relative_to_root(destination)}: #{error.class}: #{error.message}"
    end
  end
  errors
end

def run_final_audit!
  audit_path = assert_regular_no_symlink!(File.join(ROOT, FINAL_AUDIT_FILE), "final audit output")
  tool_path = assert_regular_no_symlink!(FINAL_AUDIT_TOOL, "final audit tool")
  environment = {
    BUILDER_REENTRY_ENV => "1",
    "PYTHONDONTWRITEBYTECODE" => "1"
  }
  stdout, stderr, status = Open3.capture3(
    environment,
    "python3", "-B", tool_path,
    chdir: ROOT
  )
  unless status.success?
    detail = [stdout, stderr].reject(&:empty?).join("\n").byteslice(0, 4000)
    raise "final audit failed with exit #{status.exitstatus}: #{detail}"
  end

  audit = load_json(audit_path)
  ensure_boundary!(audit["status"] == "PASS", "final audit did not emit status PASS")
  {
    "path" => FINAL_AUDIT_FILE,
    "sha256" => sha256(audit_path),
    "checks_passed" => audit["checks_passed"]
  }
end

def publish_outputs_transactionally!(preflight_snapshot)
  expected = expected_output_paths
  buffered = OUTPUT_BUFFER.keys.map { |path| relative_to_root(path) }.sort
  ensure_boundary!(buffered == expected, "output set mismatch: expected #{expected.length}, got #{buffered.length}")
  ensure_boundary!(verify_boundaries! == preflight_snapshot,
                   "protected tree changed while outputs were being composed")

  staging_root = Dir.mktmpdir("round10-stage3-prime-staging-", File.dirname(ROOT))
  backup_root = Dir.mktmpdir("round10-stage3-prime-backup-", File.dirname(ROOT))
  builder_backups = []
  final_audit_backup = nil
  retain_backup = false
  changed = []
  begin
    expected.each do |relative|
      destination = assert_safe_output!(File.join(ROOT, relative))
      bytes = OUTPUT_BUFFER.fetch(destination)
      staged = File.join(staging_root, relative)
      mode = File.stat(destination).mode & 0o777
      write_staged_file(staged, bytes, mode)
      ensure_boundary!(sha256(staged) == Digest::SHA256.hexdigest(bytes),
                       "staging hash mismatch #{relative}")

      backup = File.join(backup_root, "builder", relative)
      FileUtils.mkdir_p(File.dirname(backup), mode: 0o700)
      FileUtils.copy_file(destination, backup, true)
      builder_backups << [destination, backup]
    end

    final_audit_path = assert_regular_no_symlink!(File.join(ROOT, FINAL_AUDIT_FILE),
                                                  "final audit output")
    final_audit_backup_path = File.join(backup_root, "final-audit", FINAL_AUDIT_FILE)
    FileUtils.mkdir_p(File.dirname(final_audit_backup_path), mode: 0o700)
    FileUtils.copy_file(final_audit_path, final_audit_backup_path, true)
    final_audit_backup = [final_audit_path, final_audit_backup_path]

    # The outcome receipt is the commit marker and is always published last.
    receipt_relative = "BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json"
    publish_order = expected.reject { |relative| relative == receipt_relative } + [receipt_relative]
    publish_order.each do |relative|
      destination = assert_safe_output!(File.join(ROOT, relative))
      staged = File.join(staging_root, relative)
      next if sha256(destination) == sha256(staged)

      backup = File.join(backup_root, "builder", relative)
      File.rename(staged, destination)
      changed << relative
    end

    ensure_boundary!(verify_boundaries! == preflight_snapshot,
                     "protected tree changed during atomic publication")
    expected.each do |relative|
      destination = File.join(ROOT, relative)
      expected_sha = Digest::SHA256.hexdigest(OUTPUT_BUFFER.fetch(destination))
      ensure_boundary!(sha256(destination) == expected_sha,
                       "published output hash mismatch #{relative}")
    end

    final_audit = run_final_audit!
    ensure_boundary!(verify_boundaries! == preflight_snapshot,
                     "protected tree changed during final audit")
    expected.each do |relative|
      destination = File.join(ROOT, relative)
      expected_sha = Digest::SHA256.hexdigest(OUTPUT_BUFFER.fetch(destination))
      ensure_boundary!(sha256(destination) == expected_sha,
                       "final audit changed builder output #{relative}")
    end

    {
      "changed_outputs" => changed,
      "final_audit" => final_audit
    }
  # Publication is the one place where Interrupt/SystemExit must also roll back.
  rescue Exception => error # rubocop:disable Lint/RescueException
    # Preserve recoverable copies even if a second signal interrupts rollback.
    retain_backup = true
    rollback_errors = begin
      restore_files!(builder_backups, final_audit_backup)
    rescue Exception => rollback_error # rubocop:disable Lint/RescueException
      ["rollback interrupted: #{rollback_error.class}: #{rollback_error.message}"]
    end
    retain_backup = !rollback_errors.empty?
    message = "#{error.class}: #{error.message}"
    message += "; rollback failures: #{rollback_errors.join(' | ')}" unless rollback_errors.empty?
    raise PublicationError.new(
      message,
      rollback_complete: rollback_errors.empty?,
      recovery_backup_path: (backup_root if retain_backup)
    )
  ensure
    begin
      FileUtils.remove_entry_secure(staging_root) if staging_root && File.exist?(staging_root)
      FileUtils.remove_entry_secure(backup_root) if backup_root && File.exist?(backup_root) && !retain_backup
    rescue StandardError => cleanup_error
      warn JSON.generate({"status" => "WARNING", "temporary_cleanup_error" => cleanup_error.message})
    end
  end
end

def normalize_primary_29_30(row)
  {
    "item_id" => row.fetch("item_id"),
    "obligation_class" => row.fetch("obligation_class"),
    "immutable_criterion" => row.dig("immutable_criterion", "text"),
    "recorded_verdict" => row.dig("phase2a", "recorded_verdict"),
    "audited_verdict" => row.dig("phase2a", "audit_supported_verdict"),
    "criterion_inheritance_status" => row.dig("phase1", "semantic_inheritance"),
    "criterion_inheritance_reason" => row.dig("phase1", "reason")
  }
end

def normalize_primary_31_32(row)
  {
    "item_id" => row.fetch("item_id"),
    "obligation_class" => row.fetch("obligation_class"),
    "immutable_criterion" => row.fetch("immutable_criterion"),
    "recorded_verdict" => row.fetch("recorded_verdict"),
    "audited_verdict" => row.fetch("audit_supported_verdict"),
    "criterion_inheritance_status" => row.fetch("criterion_inheritance_status"),
    "criterion_inheritance_reason" => row["audit_reason"]
  }
end

def normalize_tiebreak(row)
  inheritance = row.fetch("phase1_criterion_inheritance")
  {
    "item_id" => row.fetch("item_id"),
    "obligation_class" => row.fetch("obligation_class"),
    "severity" => row.fetch("severity"),
    "immutable_criterion" => row.fetch("immutable_roadmap_criterion"),
    "recorded_verdict" => row.fetch("recorded_verdict"),
    "audited_verdict" => row.fetch("audited_verdict"),
    "criterion_inheritance_status" => inheritance.fetch("status"),
    "criterion_inheritance_reason" => inheritance.fetch("reason"),
    "criterion_inheritance_decision_relevant" => inheritance.fetch("decision_relevant")
  }
end

def validate_hash_tree!(tree, label)
  checked = 0
  tree.each do |key, value|
    if value.is_a?(Hash)
      checked += validate_hash_tree!(value, "#{label}/#{key}")
    elsif value.is_a?(String) && value.match?(/\A[0-9a-f]{64}\z/)
      path = declared_path(key)
      ensure_semantic!(File.file?(path), "#{label}: input exists #{key}")
      ensure_semantic!(sha256(path) == value, "#{label}: input hash #{key}")
      checked += 1
    end
  end
  checked
end

def main
  raise "recursive builder invocation refused" if ENV[BUILDER_REENTRY_ENV] == "1"

  OUTPUT_BUFFER.clear
  boundary_snapshot = verify_boundaries!
  semantic_documents = {}
semantic_bindings = SEMANTIC_FILES.map do |rel|
  path = File.join(ROOT, rel)
  raise "missing semantic audit: #{rel}" unless File.file?(path)
  semantic_documents[rel] = load_json(path)
  binding(path)
end

primary_29_30 = semantic_documents.fetch("BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P29_P30.json")
primary_31_32 = semantic_documents.fetch("BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P31_P32.json")
tiebreak = semantic_documents.fetch("BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_TIEBREAK_P33.json")
criterion_confirmation = semantic_documents.fetch("BATCH_ROUND10_STAGE3_PRIME_SEMANTIC_AUDIT_P33_CRITERION_CONFIRMATION.json")

ensure_semantic!(primary_29_30["schema_version"] == "stage3-prime-semantic-audit/1.0", "P29/P30 audit schema")
ensure_semantic!(primary_29_30.dig("auditor_provenance", "fresh_context") == true, "P29/P30 fresh context")
ensure_semantic!(primary_31_32["schema_version"] == "stage3-prime-semantic-audit/1.0", "P31/P32 audit schema")
ensure_semantic!(primary_31_32.dig("auditor_provenance", "fresh_context") == true, "P31/P32 fresh context")
ensure_semantic!(tiebreak["fresh_context"] == true, "tie-break fresh context")
ensure_semantic!(tiebreak.dig("role_separation", "independent_error_claimed") == false, "tie-break same-family limitation")
ensure_semantic!(criterion_confirmation.dig("fresh_context", "confirmed") == true, "P33 criterion confirmation fresh context")
ensure_semantic!(criterion_confirmation.dig("pipeline_gate_implication", "constitutes_phase1_lint_failure") == true, "P33 criterion confirmation gate failure")
ensure_semantic!(validate_hash_tree!(primary_29_30.fetch("input_raw_sha256"), "P29/P30 primary") == 21, "P29/P30 exact 21 input hashes replayed")
ensure_semantic!(validate_hash_tree!(primary_31_32.fetch("governing_sources_raw_sha256"), "P31/P32 governing") == 3, "P31/P32 exact three governing hashes replayed")
ensure_semantic!(validate_hash_tree!(primary_31_32.fetch("input_raw_sha256"), "P31/P32 primary") == 18, "P31/P32 exact 18 paper-input hashes replayed")
tie_hash_checks = tiebreak.fetch("allowed_inputs").count do |entry|
  path = entry.fetch("path")
  full_path = declared_path(path)
  ensure_semantic!(File.file?(full_path), "tie-break input exists #{path}")
  ensure_semantic!(sha256(full_path) == entry.fetch("sha256"), "tie-break input hash #{path}")
  true
end
ensure_semantic!(tie_hash_checks == 60, "tie-break 60 input hashes replayed")
ensure_semantic!(tiebreak.fetch("allowed_inputs").map { |entry| entry.fetch("path") }.uniq.length == 60,
                 "tie-break input paths are unique")
confirmation_hash_checks = criterion_confirmation.dig("input_inventory", "allowed").count do |entry|
  path = entry.fetch("path")
  full_path = declared_path(path)
  ensure_semantic!(File.file?(full_path), "P33 criterion-confirmation input exists #{path}")
  ensure_semantic!(sha256(full_path) == entry.fetch("sha256"), "P33 criterion-confirmation input hash #{path}")
  true
end
ensure_semantic!(confirmation_hash_checks == 7, "P33 criterion-confirmation seven input hashes replayed")
ensure_semantic!(criterion_confirmation.dig("input_inventory", "allowed").map { |entry| entry.fetch("path") }.uniq.length == 7,
                 "P33 criterion-confirmation input paths are unique")

source_rows = {}
primary_29_30.fetch("papers").each do |paper|
  paper_id = "P#{paper.fetch('paper_id')}"
  source_rows[paper_id] = paper.fetch("row_audits").to_h do |row|
    normalized = normalize_primary_29_30(row)
    [normalized.fetch("item_id"), normalized]
  end
end
primary_31_32.fetch("papers").each do |paper_id, paper|
  source_rows[paper_id] = paper.fetch("row_audits").to_h do |row|
    normalized = normalize_primary_31_32(row)
    [normalized.fetch("item_id"), normalized]
  end
end
primary_source_rows = source_rows.to_h do |paper_id, rows|
  [paper_id, rows.transform_values(&:dup)]
end

tie_rows_by_paper = tiebreak.fetch("disputed_rows").group_by { |row| "P#{row.fetch('paper_id')}" }
ensure_semantic!(tie_rows_by_paper.values.sum(&:length) == 11, "exact 11 disputed tie-break rows")
tiebreak_source_rows = {}
TIE_ROWS.each do |paper_id, item_ids|
  rows = tie_rows_by_paper.fetch(paper_id).to_h { |row| [row.fetch("item_id"), normalize_tiebreak(row)] }
  ensure_semantic!(rows.keys.sort == item_ids.sort, "#{paper_id} disputed item set")
  tiebreak_source_rows[paper_id] = rows
  rows.each { |item_id, row| source_rows.fetch(paper_id)[item_id] = row }
end
source_rows["P33"] = tiebreak.fetch("paper33_all_rows").to_h do |row|
  normalized = normalize_tiebreak(row)
  [normalized.fetch("item_id"), normalized]
end
confirmation_rows = criterion_confirmation.fetch("item_comparisons")
ensure_semantic!(confirmation_rows.length == 13, "P33 criterion-confirmation 13 rows")
confirmation_rows.each do |row|
  item_id = row.fetch("item_id")
  inherited = source_rows.fetch("P33").fetch(item_id)
  ensure_semantic!(row.fetch("roadmap_exact_criterion") == inherited.fetch("immutable_criterion"), "P33 #{item_id} confirmation exact criterion")
  ensure_semantic!(row.fetch("obligation_class") == inherited.fetch("obligation_class"), "P33 #{item_id} confirmation obligation class")
  extension = row.dig("material_extension", "present")
  weakening = row.dig("material_weakening", "present")
  status = if row.fetch("faithful")
             "faithful"
           elsif extension && weakening
             "material_extension_and_weakening"
           elsif extension
             "material_extension"
           elsif weakening
             "material_weakening"
           else
             raise "semantic-source validation failed: P33 #{item_id} non-faithful row lacks drift type"
           end
  reasons = [row.dig("material_extension", "detail"), row.dig("material_weakening", "detail")].compact
  inherited["criterion_inheritance_status"] = status
  inherited["criterion_inheritance_reason"] = reasons.join(" ")
end

semantic_replay = {}
PAPERS.each do |paper_id, spec|
  notes = File.join(ROOT, "papers", spec.fetch(:slug), "notes")
  roadmap = load_json(File.join(notes, "stage3_revision_roadmap.json"))
  verdict = load_json(File.join(notes, "stage3_prime_round1_verdict_record.json"))
  roadmap_by_id = roadmap.fetch("items").to_h { |row| [row.fetch("id"), row] }
  verdict_by_id = verdict.fetch("items").to_h { |row| [row.fetch("item_id"), row] }
  rows = source_rows.fetch(paper_id)
  ensure_semantic!(rows.keys.sort == roadmap_by_id.keys.sort, "#{paper_id} complete semantic row coverage")
  rows.each do |item_id, row|
    roadmap_row = roadmap_by_id.fetch(item_id)
    ensure_semantic!(row.fetch("immutable_criterion") == roadmap_row.fetch("verification_criteria"), "#{paper_id} #{item_id} exact criterion")
    ensure_semantic!(row.fetch("obligation_class") == roadmap_row.fetch("obligation_class"), "#{paper_id} #{item_id} obligation class")
    ensure_semantic!(row.fetch("recorded_verdict") == verdict_by_id.fetch(item_id).fetch("verdict"), "#{paper_id} #{item_id} recorded verdict")
    if row.key?("severity")
      ensure_semantic!(row.fetch("severity") == roadmap_row.fetch("severity"), "#{paper_id} #{item_id} severity")
    end
  end
  audited_histogram = rows.values.map { |row| row.fetch("audited_verdict") }.tally
  audited_counts = [audited_histogram.fetch("FULLY_ADDRESSED", 0), audited_histogram.fetch("PARTIALLY_ADDRESSED", 0), audited_histogram.fetch("NOT_ADDRESSED", 0)]
  overrides = rows.values.select { |row| row.fetch("recorded_verdict") != row.fetch("audited_verdict") }.to_h { |row| [row.fetch("item_id"), row.fetch("audited_verdict")] }
  drift_ids = rows.values.reject { |row| ["faithful", "no_material_extension_or_weakening"].include?(row.fetch("criterion_inheritance_status")) }.map { |row| row.fetch("item_id") }.sort
  ensure_semantic!(audited_counts == spec.fetch(:audited), "#{paper_id} audited counts")
  ensure_semantic!(overrides == spec.fetch(:overrides), "#{paper_id} verdict override set")
  ensure_semantic!(drift_ids == spec.fetch(:criterion_defects).map { |row| row.fetch("item_id") }.sort, "#{paper_id} criterion-drift set")
  semantic_replay[paper_id] = {
    "row_count" => rows.length,
    "audited_counts" => audited_counts,
    "verdict_overrides" => overrides,
    "criterion_inheritance_item_ids" => drift_ids
  }
end

# The consolidation is deliberately explicit: same-family fresh contexts are
# useful role separation, but they are not an independence certificate.
disputed_rows = []
PAPERS.each do |paper_id, spec|
  notes = File.join(ROOT, "papers", spec.fetch(:slug), "notes")
  verdict = load_json(File.join(notes, "stage3_prime_round1_verdict_record.json"))
  verdict_by_id = verdict.fetch("items").to_h { |row| [row.fetch("item_id"), row] }
  TIE_ROWS.fetch(paper_id, []).each do |item_id|
    recorded = verdict_by_id.fetch(item_id).fetch("verdict")
    primary_verdict = primary_source_rows.fetch(paper_id).fetch(item_id).fetch("audited_verdict")
    tie_verdict = tiebreak_source_rows.fetch(paper_id).fetch(item_id).fetch("audited_verdict")
    disputed_rows << {
      "paper_id" => paper_id,
      "item_id" => item_id,
      "recorded_verdict" => recorded,
      "primary_audit_supported_verdict" => primary_verdict,
      "tie_break_audit_supported_verdict" => tie_verdict,
      "primary_tie_agree" => primary_verdict == tie_verdict,
      "consolidated_audit_supported_verdict" => tie_verdict,
      "criterion_inheritance_finding" => spec.fetch(:criterion_defects).any? { |row| row.fetch("item_id") == item_id }
    }
  end
end

consolidation = {
  "schema_version" => "stage3-prime-semantic-audit-consolidation/1.0",
  "audit_id" => "round10-stage3-prime-semantic-audit-consolidation-2026-09-03",
  "created_at_utc" => CHECKED_AT,
  "source_artifacts" => semantic_bindings,
  "method" => {
    "criterion" => "Each verdict is judged against the immutable exact roadmap criterion; Phase-1 operationalization may not add or weaken an acceptance condition.",
    "arbitration" => "The fresh-context tie-break controls the listed disputed rows; full-coverage primary audits control all other P29-P32 rows; the tie-break supplies full P33 verdict coverage; a separate roadmap-versus-precommitment-only P33 audit confirms the Phase-1 inheritance result.",
    "earliest_gate_rule" => "Any unrecorded Phase-1 criterion extension or weakening aborts at phase1_lint_failed even when the mechanical decision direction is unchanged; frozen artifacts are not rewritten in place."
  },
  "auditor_provenance" => {
    "fresh_context_role_separation" => true,
    "human_distinct" => false,
    "model_family_distinct" => false,
    "provider_distinct" => false,
    "independent_error_process_claimed" => false,
    "limitation" => "All semantic passes used role-separated fresh contexts in the same model family/provider. Correlated-error risk remains."
  },
  "disputed_rows" => disputed_rows,
  "papers" => PAPERS.map do |paper_id, spec|
    {
      "paper_id" => paper_id,
      "recorded_counts" => spec.fetch(:recorded),
      "consolidated_audit_supported_counts" => spec.fetch(:audited),
      "verdict_discrepancies" => spec.fetch(:defects),
      "criterion_inheritance_findings" => spec.fetch(:criterion_defects),
      "mechanical_direction" => "Major Revision",
      "mechanical_rule" => spec.fetch(:mechanical_rule),
      "controlling_status" => spec[:abort_reason] ? "ABORTED" : "COMPLETE",
      "abort_reason" => spec[:abort_reason]
    }.compact
  end,
  "aggregate" => {
    "recorded_counts" => [27, 27, 2],
    "consolidated_audit_supported_counts" => [25, 29, 2],
    "verdict_discrepancies" => 6,
    "false_full_rows" => 4,
    "false_partial_rows" => 2,
    "criterion_inheritance_affected_rows" => 13,
    "complete_papers" => 0,
    "aborted_papers" => 5
  },
  "boundary_attestation" => {
    "semantic_audit_only" => true,
    "canonical_or_science_writes" => boundary_snapshot.fetch("canonical_or_science_writes"),
    "route_changes" => boundary_snapshot.fetch("route_changes"),
    "successor_stage_authorized" => boundary_snapshot.fetch("successor_stage_authorized")
  }
}
consolidation_path = File.join(ROOT, CONSOLIDATION_FILE)
queue_output!(consolidation_path, JSON.pretty_generate(consolidation) + "\n")
consolidation_binding = binding(consolidation_path)

phase_validation_bindings = {
  "phase1" => binding(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_PHASE1_VALIDATION.json")),
  "phase2a" => binding(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_PHASE2A_VALIDATION.json")),
  "phase2b" => binding(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_PHASE2B_INTEGRATION_VALIDATION.json"))
}

batch_papers = []
terminal_checker_receipts = []
terminal_verification_reports = []
terminal_abort_records = []

PAPERS.each do |paper_id, spec|
  notes = File.join(ROOT, "papers", spec.fetch(:slug), "notes")
  manifest_path = File.join(notes, "stage3_prime_round1_input_manifest.json")
  precommitment_path = File.join(notes, "stage3_prime_round1_precommitment.json")
  verdict_path = File.join(notes, "stage3_prime_round1_verdict_record.json")
  integration_path = File.join(notes, "stage3_prime_round1_phase2b_integration.json")
  trace_path = File.join(notes, "stage3_prime_round1_traceability.json")
  roadmap_path = File.join(notes, "stage3_revision_roadmap.json")
  bundle_path = File.join(notes, "stage4_revision_evidence_bundle.json")
  author_path = File.join(notes, "stage4_author_adjudication.json")
  panel_path = File.join(notes, "stage3_review_package.json")

  manifest = load_json(manifest_path)
  precommitment = load_json(precommitment_path)
  verdict = load_json(verdict_path)
  integration = load_json(integration_path)
  trace = load_json(trace_path)
  roadmap = load_json(roadmap_path)
  bundle = load_json(bundle_path)
  author = load_json(author_path)
  panel = load_json(panel_path).fetch("review_panel_provenance")
  roadmap_by_id = roadmap.fetch("items").to_h { |row| [row.fetch("id"), row] }

  recorded_full, recorded_partial, recorded_not = spec.fetch(:recorded)
  audited_full, audited_partial, audited_not = spec.fetch(:audited)
  controlling = spec[:abort_reason] ? "ABORTED" : "COMPLETE"
  warning = paper_id == "P31" ? [] : ["Editorial decision letter present but no Required Item Details blocks parsed; the level-2 criteria layer is empty and the registered roadmap remains controlling."]

  artifacts = {
    "input_manifest" => {"raw_sha256" => sha256(manifest_path), "jcs_sha256" => jcs_sha256(manifest)},
    "precommitment" => {"raw_sha256" => sha256(precommitment_path), "jcs_sha256" => jcs_sha256(precommitment)},
    "verdict_record" => {"raw_sha256" => sha256(verdict_path), "jcs_sha256" => jcs_sha256(verdict)},
    "phase2b_integration" => {"raw_sha256" => sha256(integration_path), "jcs_sha256" => jcs_sha256(integration)},
    "traceability" => {"raw_sha256" => sha256(trace_path), "jcs_sha256" => jcs_sha256(trace)},
    "revision_roadmap" => {"raw_sha256" => sha256(roadmap_path), "jcs_sha256" => jcs_sha256(roadmap)},
    "revision_evidence_bundle" => {"raw_sha256" => sha256(bundle_path), "jcs_sha256" => jcs_sha256(bundle)},
    "author_adjudication" => {"raw_sha256" => sha256(author_path), "jcs_sha256" => jcs_sha256(author)}
  }

  judge_record = {
    "verification_judge" => {
      "model_family" => "OpenAI GPT-5 family",
      "interface" => "Codex",
      "service_model_id" => "unavailable_to_workspace",
      "same_family_as_revision_workflow" => true,
      "independent_error_process_claimed" => false
    },
    "round1_panel_provenance" => panel,
    "cross_model_pass" => "not_configured",
    "prompt_rubric_surfaces" => RUBRIC_PATHS.map do |path|
      surface = {"path" => path, "sha256" => sha256(path)}
      if path == PROTOCOL_PATH
        surface["sections"] = ["Three-Gate Orchestration (#576 Spec B)", "Criterion Inheritance", "Decision Derivation (verdict -> decision)", "Judge Record (#539)"]
      end
      surface
    end,
    "reviewer_configuration" => "round1_cards_reused",
    "evidence_seen" => {
      "phase1" => {
        "allowed" => ["revision roadmap", "editorial decision surface", "Round-1 findings/configuration cards", "Phase-0 field analysis", "manifest verification binding"],
        "withheld" => ["manifest body", "original manuscript", "revised manuscript", "evidence bundle", "patch/apply reports", "Response to Reviewers", "author adjudication"]
      },
      "phase2a" => {
        "allowed" => ["frozen precommitment", "manifest path/hash bindings", "roadmap/decision/findings/cards", "original manuscript", "revised manuscript", "patch/apply reports", "evidence bundle"],
        "withheld" => ["Response to Reviewers", "author adjudication"]
      },
      "phase2b" => {
        "protocol_allowed" => ["frozen Phase-2A verdict", "roadmap/manuscript evidence", "Response to Reviewers"],
        "withheld" => ["author adjudication (checker-only)"],
        "call_level_input_receipt" => "not retained; protocol fencing and integration output are recorded, but the exact realized call input cannot be independently replayed"
      },
      "checker" => "read the exact author-adjudication sidecar only to verify row-level triage/target/claim-authorization carriage; the sidecar did not become a judging criterion",
      "untrusted_data_boundary" => ["revised manuscript", "Response to Reviewers"],
      "post_checker_semantic_audit" => "hash-bound audit allowlists; the fresh tie-break withheld outcome reports, README status surfaces, and prior semantic-audit conclusions"
    },
    "judging_budget_note" => "Actual API-call and token telemetry was not retained. Contract topology was a Phase-1 initial call with at most one pre-evidence lint retry, one Phase-2A evidence-exposed call with no retry, one Phase-2B integration call with no retry, zero Phase-2B-prime reapplication calls, and zero cross-model calls. Exact realized calls/tokens must not be inferred; post-checker semantic audits are separate provenance; generation work is excluded.",
    "precommitment_hash" => artifacts.dig("precommitment", "jcs_sha256"),
    "routing_status" => "card_mapped",
    "apply_chain_witness" => "pass",
    "precommitment_raw_sha256" => artifacts.dig("precommitment", "raw_sha256")
  }

  next_authorization = if spec[:abort_reason]
                         "explicit scholar authorization to restart Stage 3′ as Round 2 with a new round id/manifest and fresh Phase-1/2A contexts"
                       else
                         partial_count = spec.fetch(:audited)[1]
                         "explicit scholar authorization to prepare a hash-bound Stage 4′ item/target/operation request for all #{partial_count} PARTIAL residuals; manuscript writes require a later exact approval"
                       end

  receipt = {
    "schema_version" => "stage3-prime-round1-checker-semantic-receipt/1.1",
    "round_id" => manifest.fetch("round_id"),
    "checked_at" => CHECKED_AT,
    "checker" => "ARS 0.1.26 scripts/check_re_review_synthesis.py",
    "checker_sha256" => CHECKER_SHA,
    "checker_exit_code" => 0,
    "checker_message" => "re-review synthesis ok: round '#{manifest.fetch('round_id')}', revision 1, decision_state 'Major Revision', apply_chain_witness 'pass'",
    "checker_warnings" => warning,
    "mechanical_status" => "PASS",
    "mechanical_decision_state" => "Major Revision",
    "mechanical_decision_rule" => spec.fetch(:mechanical_rule),
    "semantic_audit_status" => spec[:abort_reason] ? "FAIL_CLOSED" : "PASS",
    "controlling_status" => controlling,
    "abort_reason" => spec[:abort_reason],
    "decision_emitted" => spec[:abort_reason].nil?,
    "emitted_decision" => spec[:abort_reason] ? nil : "Major Revision",
    "suppressed_candidate_decision" => spec[:abort_reason] ? "Major Revision" : nil,
    "recorded_counts" => {"FULLY_ADDRESSED" => recorded_full, "PARTIALLY_ADDRESSED" => recorded_partial, "NOT_ADDRESSED" => recorded_not, "MADE_WORSE" => 0, "CANNOT_VERIFY" => 0},
    "audit_supported_counts" => {"FULLY_ADDRESSED" => audited_full, "PARTIALLY_ADDRESSED" => audited_partial, "NOT_ADDRESSED" => audited_not, "MADE_WORSE" => 0, "CANNOT_VERIFY" => 0},
    "semantic_findings" => spec.fetch(:defects),
    "criterion_inheritance_findings" => spec.fetch(:criterion_defects),
    "apply_chain_witness" => "pass",
    "cross_model_status" => "not_configured",
    "judge_record" => judge_record,
    "artifacts" => artifacts,
    "semantic_evidence" => semantic_bindings + [consolidation_binding],
    "validation_receipts" => phase_validation_bindings,
    "boundaries" => {
      "phase_artifacts_rewritten_after_commit" => boundary_snapshot.fetch("phase_artifacts_rewritten_after_commit"),
      "canonical_manuscript_pdf_bibliography_changed" => boundary_snapshot.fetch("canonical_manuscript_pdf_bibliography_changed"),
      "science_results_changed" => boundary_snapshot.fetch("science_results_changed"),
      "initial_dynamical_system_changed" => boundary_snapshot.fetch("initial_dynamical_system_changed"),
      "route_credit_changed" => boundary_snapshot.fetch("route_credit_changed"),
      "route_b_invoked" => boundary_snapshot.fetch("route_b_invoked"),
      "successor_stage_authorized" => boundary_snapshot.fetch("successor_stage_authorized")
    },
    "next_authorization" => next_authorization,
    "same_family_disclosure" => DISCLOSURE
  }.compact

  checker_receipt_path = File.join(notes, "stage3_prime_round1_checker_receipt.json")
  queue_output!(checker_receipt_path, JSON.pretty_generate(receipt) + "\n")

  if spec[:abort_reason]
    abort_record = {
      "schema_version" => "round10-stage3-prime-abort-record/1.1",
      "paper_id" => paper_id,
      "round_id" => manifest.fetch("round_id"),
      "status" => "aborted",
      "abort_reason" => spec.fetch(:abort_reason),
      "detected_at" => CHECKED_AT,
      "detected_by" => "persisted fresh-context, role-separated same-family semantic audit with hash-bound tie-break",
      "independent_error_process_claimed" => false,
      "mechanical_checker_passed" => true,
      "decision_suppressed" => true,
      "suppressed_candidate_decision" => "Major Revision",
      "no_retry_rule_applied" => true,
      "retry_handling" => if spec.fetch(:abort_reason) == "phase1_lint_failed"
                            {
                              "protocol_rule" => "one manuscript-blind Phase-1 lint retry is permitted only before Phase 2A consumes manuscript evidence",
                              "detection_timing" => "post_commit_after_phase2a_and_phase2b",
                              "in_place_retry_eligible" => false,
                              "reason" => "The semantic defect was discovered only after frozen Phase-2A and Phase-2B artifacts existed. Re-entering Phase 1 in the same round would overwrite committed evidence and violate evidence-before-persuasion; the fail-closed remedy is a fresh authorized Round 2."
                            }
                          else
                            {
                              "protocol_rule" => "Phase 2A is no-retry within the frozen round",
                              "detection_timing" => "post_commit_phase2a_semantic_audit",
                              "in_place_retry_eligible" => false,
                              "reason" => "The frozen Phase-2A verdict record contains semantic overcredit. It cannot be rewritten in place; the fail-closed remedy is a fresh authorized Round 2."
                            }
                          end,
      "frozen_phase_artifacts_preserved" => true,
      "semantic_findings" => receipt.fetch("semantic_findings"),
      "criterion_inheritance_findings" => receipt.fetch("criterion_inheritance_findings"),
      "semantic_evidence" => receipt.fetch("semantic_evidence"),
      "next_round_requirement" => {
        "explicit_scholar_authorization" => true,
        "new_round_id" => manifest.fetch("round_id").sub("round1", "round2"),
        "new_manifest" => true,
        "fresh_phase1_context" => true,
        "fresh_phase2a_context" => true,
        "no_overwrite_of_round1" => true
      },
      "boundaries" => receipt.fetch("boundaries")
    }
    abort_path = File.join(notes, "stage3_prime_round1_abort_record.json")
    queue_output!(abort_path, JSON.pretty_generate(abort_record) + "\n")
    terminal_abort_records << binding(abort_path)
  end

  audit_supported_by_id = verdict.fetch("items").to_h do |row|
    [row.fetch("item_id"), spec.fetch(:overrides).fetch(row.fetch("item_id"), row.fetch("verdict"))]
  end
  row_table = verdict.fetch("items").map do |row|
    item_id = row.fetch("item_id")
    roadmap_row = roadmap_by_id.fetch(item_id)
    residual = row.dig("residual_gap", "text") || row["cannot_verify_reason"] || "—"
    anchors = Array(row["evidence_anchor"]).join("; ")
    supported = audit_supported_by_id.fetch(item_id)
    verified = case supported
               when "FULLY_ADDRESSED" then "FULL"
               when "PARTIALLY_ADDRESSED" then "PARTIAL"
               else "NO"
               end
    "| #{item_id} | `#{roadmap_row.fetch('obligation_class')}` | `#{row.fetch('verdict')}` | `#{supported}` | #{verified} | #{escape_table(anchors)} | #{escape_table(residual)} |"
  end.join("\n")

  finding_rows = spec.fetch(:defects).map do |row|
    "| #{row.fetch('item_id')} | `#{row.fetch('recorded')}` | `#{row.fetch('audit_supported')}` | #{escape_table(row.fetch('reason'))} |"
  end.join("\n")
  criterion_rows = spec.fetch(:criterion_defects).map do |row|
    "| #{row.fetch('item_id')} | #{escape_table(row.fetch('kind'))} | #{escape_table(row.fetch('reason'))} |"
  end.join("\n")
  provenance_axes = panel.fetch("axes").map { |key, value| "`#{key}=#{value}`" }.join(", ")

  outcome_intro = if spec[:abort_reason]
                    retry_note = if spec.fetch(:abort_reason) == "phase1_lint_failed"
                                   "The Phase-1 drift was discovered only after Phase 2A/2B had consumed and frozen manuscript evidence, so the pre-evidence retry window cannot be reopened in place."
                                 else
                                   "Phase 2A is no-retry within this frozen round."
                                 end
                    "`[RE-REVIEW-ABORT: #{spec.fetch(:abort_reason)}]`\n\nThe official checker passed artifact grammar and recomputed a candidate `Major Revision`, but the persisted fresh-context semantic audit found a frozen gate violation. #{retry_note} The candidate is suppressed and no decision is emitted."
                  else
                    "**Decision: Major Revision (#{spec.fetch(:mechanical_rule)}); semantic and mechanical verification PASS.**\n\nThe decision is valid for this frozen revision package. It authorizes no manuscript write or successor stage."
                  end

  checkpoint_text = if spec[:abort_reason]
                      "A fresh Stage 3′ Round 2 requires explicit scholar authorization, a new round id and manifest, fresh Phase-1/2A contexts, and byte-preservation of Round 1."
                    else
                      "The next confirmation may authorize only preparation of a hash-bound Stage 4′ request covering all #{audited_partial} PARTIAL rows. Actual manuscript edits require a later exact approval of item ids, target blocks, and operations."
                    end

  report = <<~MD
    # #{paper_id} Round 10 Stage 3′ Round 1 Verification Report

    ## Controlling outcome

    #{outcome_intro}

    | Count view | Fully | Partially | Not addressed | Made worse | Cannot verify |
    |---|---:|---:|---:|---:|---:|
    | Frozen emitted record | #{recorded_full} | #{recorded_partial} | #{recorded_not} | 0 | 0 |
    | Consolidated semantic audit | #{audited_full} | #{audited_partial} | #{audited_not} | 0 | 0 |

    Explicit paper progress: #{spec.fetch(:progress)}

    ## Semantic and criterion findings

    #{finding_rows.empty? ? "No row-verdict discrepancy was found." : "| Item | Frozen verdict | Audit-supported verdict | Reason |\n|---|---|---|---|\n#{finding_rows}"}

    #{criterion_rows.empty? ? "No criterion-inheritance defect was found." : "### Criterion-inheritance defects\n\n| Item | Kind | Reason |\n|---|---|---|\n#{criterion_rows}"}

    #{spec[:advisory] ? "Traceable wording advisory within an existing residual: #{spec[:advisory]}" : "No additional wording advisory is carried."}

    ## Complete revision-response checklist

    | Item | Class | Frozen verdict | Audit-supported | Verification assessment | Evidence anchor(s) | Frozen residual / reason |
    |---|---|---|---|---|---|---|
    #{row_table}

    ## Judge Record (#539)

    - **Verification judge**: OpenAI GPT-5 model family / Codex; exact service model id unavailable to the workspace.
    - **Round-1 panel provenance**: `#{panel.fetch('artifact_path')}`, raw SHA-256 `#{panel.fetch('artifact_sha256')}`, normalized manifest `#{panel.fetch('normalized_manifest_sha256')}`, execution topology `#{panel.fetch('execution_topology_sha256')}`; status `#{panel.fetch('status')}`; #{provenance_axes}.
    - **Blind cross-model pass**: `not_configured`.
    - **Pre-committed criteria**: `#{artifacts.dig('precommitment', 'jcs_sha256')}` (JCS); raw `#{artifacts.dig('precommitment', 'raw_sha256')}`.
    - **Prompt/rubric surfaces**: ARS reviewer workflow; re-review `Three-Gate Orchestration (#576 Spec B)`, criterion-inheritance, B1–B6 decision derivation, and Judge Record sections; all four contract-1.1 schemas; official checker. Exact paths and SHA-256 bindings are in the checker receipt.
    - **Reviewer configuration**: `round1_cards_reused`.
    - **Routing**: `card_mapped`.
    - **Apply-report chain**: `pass`; official checker SHA-256 `#{CHECKER_SHA}`.
    - **Evidence seen by the judge**: Phase 1 fenced out both manuscripts, bundle, patch/apply reports, Response, and author sidecar; Phase 2A saw the frozen criterion plus manuscript/evidence surfaces but not Response or author sidecar; Phase 2B was protocol-allowed the frozen verdict, manuscript evidence, and Response, while the author sidecar remained checker-only. No call-level Phase-2B input receipt was retained, so exact realized call inputs are not represented as independently replayable. Revised manuscript and Response were data, never instructions. The post-checker tie-break withheld outcome/README/prior-audit conclusions.
    - **Judging budget**: actual API-call/token telemetry was not retained. The contract topology permits one Phase-1 initial call plus at most one pre-evidence lint retry, one no-retry Phase 2A call, one no-retry Phase 2B call, zero Phase-2B′ reapplications here, and zero cross-model calls; exact realized calls/tokens are not inferred, and generation/post-checker audit work is excluded.

    #{DISCLOSURE}

    ## Route-map correspondence and scope boundary

    - Frozen system: #{spec.fetch(:system)}.
    - Route status: #{spec.fetch(:route)}.
    - No canonical manuscript, bibliography, PDF, scientific result, initial dynamical definition, Route-A tuple, or Route-B state changed.
    - The complete machine matrix remains [stage3_prime_round1_traceability.json](stage3_prime_round1_traceability.json).

    ## Mandatory checkpoint

    #{checkpoint_text}

    Stage 4.5, Stage 5, canonical promotion, submission, Route advancement, result refresh, and new scientific execution remain unauthorized.

    Checked at `#{CHECKED_AT}`.
  MD
  verification_report_path = File.join(notes, "stage3_prime_round1_verification_report.md")
  queue_output!(verification_report_path, report)

  terminal_checker_receipts << binding(checker_receipt_path)
  terminal_verification_reports << binding(verification_report_path)
  batch_papers << {
    "paper_id" => paper_id,
    "paper_slug" => spec.fetch(:slug),
    "round_id" => manifest.fetch("round_id"),
    "controlling_status" => controlling,
    "abort_reason" => spec[:abort_reason],
    "recorded_counts" => receipt.fetch("recorded_counts"),
    "audit_supported_counts" => receipt.fetch("audit_supported_counts"),
    "mechanical_candidate_decision" => "Major Revision",
    "mechanical_rule" => spec.fetch(:mechanical_rule),
    "decision_emitted" => spec[:abort_reason].nil?,
    "semantic_findings" => spec.fetch(:defects).length,
    "criterion_inheritance_findings" => spec.fetch(:criterion_defects).length,
    "traceability_sha256" => artifacts.dig("traceability", "raw_sha256"),
    "checker_receipt_path" => binding(checker_receipt_path).fetch("path"),
    "verification_report_path" => binding(verification_report_path).fetch("path"),
    "next_authorization" => next_authorization
  }.compact
end

recorded_totals = {"FULLY_ADDRESSED" => 27, "PARTIALLY_ADDRESSED" => 27, "NOT_ADDRESSED" => 2, "MADE_WORSE" => 0, "CANNOT_VERIFY" => 0}
audited_totals = {"FULLY_ADDRESSED" => 25, "PARTIALLY_ADDRESSED" => 29, "NOT_ADDRESSED" => 2, "MADE_WORSE" => 0, "CANNOT_VERIFY" => 0}

paper_rows = PAPERS.map do |paper_id, spec|
  outcome = spec[:abort_reason] ? "ABORT `#{spec.fetch(:abort_reason)}`" : "Major Revision (#{spec.fetch(:mechanical_rule)})"
  next_step = spec[:abort_reason] ? "authorize fresh Round 2" : "authorize exact Stage 4′ request preparation"
  "| #{paper_id} | #{spec.fetch(:recorded).join('/')} | #{spec.fetch(:audited).join('/')} | #{outcome} | #{next_step} | [report](papers/#{spec.fetch(:slug)}/notes/stage3_prime_round1_verification_report.md) |"
end.join("\n")

finding_rows = PAPERS.flat_map do |paper_id, spec|
  spec.fetch(:defects).map do |row|
    "| #{paper_id} | #{row.fetch('item_id')} | `#{row.fetch('recorded')}` | `#{row.fetch('audit_supported')}` | #{escape_table(row.fetch('reason'))} |"
  end
end.join("\n")

criterion_rows = PAPERS.flat_map do |paper_id, spec|
  spec.fetch(:criterion_defects).map do |row|
    "| #{paper_id} | #{row.fetch('item_id')} | #{escape_table(row.fetch('kind'))} | #{escape_table(row.fetch('reason'))} |"
  end
end.join("\n")

system_rows = PAPERS.map do |paper_id, spec|
  "| #{paper_id} | #{escape_table(spec.fetch(:system))} | #{escape_table(spec.fetch(:route))} |"
end.join("\n")

progress_rows = PAPERS.map do |paper_id, spec|
  "| #{paper_id} | #{escape_table(spec.fetch(:progress))} |"
end.join("\n")

report = <<~MD
  # Round 10 Papers 29–33 — Stage 3′ Round 1 Outcome Report

  ## Outcome first

  Round 1 is **fail-closed for all five papers; no Stage 3′ decision is emitted**. All five official ARS checker runs passed mechanically and recomputed `Major Revision`, but persisted fresh-context, role-separated semantic audits found six row-verdict discrepancies and 13 rows with unrecorded Phase-1 criterion drift. The contexts are same-family and are not represented as statistically independent error processes.

  - P29: `[RE-REVIEW-ABORT: phase2a_lint_failed]`; exact-criterion count 6/5/0; one false FULL.
  - P30: `[RE-REVIEW-ABORT: phase1_lint_failed]`; exact-criterion count remains 4/5/0; one false FULL and one false PARTIAL offset.
  - P31: `[RE-REVIEW-ABORT: phase1_lint_failed]`; exact-criterion count 3/7/1; one false FULL.
  - P32: `[RE-REVIEW-ABORT: phase1_lint_failed]`; aggregate count remains 6/5/1; one false FULL and one false PARTIAL offset.
  - P33: `[RE-REVIEW-ABORT: phase1_lint_failed]`; its 6/7/0 row judgments remain semantically supported and would point to B4, but seven Phase-1 rows carry undeclared extension/weakening drift and invalidate the gate before a decision can issue.

  No frozen Phase-1/2A artifact is repaired in place.

  ## Per-paper result

  Counts are `FULL/PARTIAL/NOT`; both views have zero `MADE_WORSE` and zero `CANNOT_VERIFY`.

  | Paper | Frozen count | Audit-supported count | Controlling outcome | Next authorization | Detail |
  |---|---:|---:|---|---|---|
  #{paper_rows}

  Aggregate frozen count: **27/27/2**. Aggregate audit-supported count: **25/29/2**. Phase 2B made **0 adjustments** and **0 verdict changes**; no new issue, dissent, escalation exception, or post-letter observation was emitted.

  ## Explicit manuscript progress

  | Paper | Progress that remains true after re-review |
  |---|---|
  #{progress_rows}

  ## Row-verdict discrepancies

  | Paper | Item | Frozen verdict | Audit-supported verdict | Reason |
  |---|---|---|---|---|
  #{finding_rows}

  ## Phase-1 criterion-inheritance findings

  | Paper | Item | Kind | Reason |
  |---|---|---|---|
  #{criterion_rows}

  The B-rule direction remains Major for all five. Gate integrity nevertheless controls: P30–P33 abort at the earliest invalid Phase-1 gate; P29 aborts at Phase 2A. All require a new round rather than an in-place correction.

  ## What passed

  - Phase 1 structural validation: 56 precommitments; 679 binding checks; schema PASS.
  - Phase 2A structural validation: 56 immutable verdict records; 380 checks; schema PASS.
  - Phase 2B integration: 56 response rows; 482 checks; zero silent change.
  - Official synthesis checker: 5/5 exit 0; apply-chain witness 5/5 `pass`.
  - Manifest surfaces: exact eleven keys per paper; all raw/JCS chains bind.
  - Author carriage: 56/56 exact triage/target/claim-authorization copies.
  - Full semantic coverage: primary audits cover all P29–P32 rows; the fresh tie-break covers disputed rows and all 13 P33 rows; a separate blind P33 criterion-only audit confirms its Phase-1 inheritance status; consolidation is hash-bound.

  ## Route-map correspondence

  This run was checked against [`skills/route-a-evaluator.md`](skills/route-a-evaluator.md) and [`skills/route-b-evaluator.md`](skills/route-b-evaluator.md). Stage 3′ is a manuscript-revision verification gate, not Route evidence.

  | Paper | Frozen initial system | Unchanged Route coordinate |
  |---|---|---|
  #{system_rows}

  Formal Route-A tuples remain **0/5 assigned**, positive arithmetic A2 results remain **0/5**, A3/A4 were not advanced, and Route B remains **0/5 invoked**. No prime/zero data redefined or tuned a candidate.

  ## Provenance and limitations

  P31's decision letter has a valid contiguous R1–R11 criterion layer. P29/P30/P32/P33 retain a non-blocking template-drift advisory because their decision letters contain no strictly parseable `Required Item Details` blocks; their registered roadmap criteria remain controlling.

  No cross-model pass was configured. #{DISCLOSURE}

  Canonical manuscripts, bibliographies, PDFs, scientific result trees, initial system restrictions, and Route records are unchanged. Frozen Round-1 Phase artifacts and mechanically valid trace matrices are retained byte-for-byte.

  ## Mandatory user checkpoint

  No further stage is authorized by this report. A later plain **“确认”** authorizes exactly:

  1. P29–P33: start **Stage 3′ Round 2** with new round ids/manifests, freshly fenced Phase-1/2A contexts, and byte-preservation of every Round-1 artifact.

  That confirmation does **not** authorize manuscript or bibliography edits, a Stage 4′ request, Stage 4.5, Stage 5, canonical promotion, submission, Route advancement, result refresh, or new scientific execution.

  Checked at `#{CHECKED_AT}`.
MD
report_path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md")
queue_output!(report_path, report)

checkpoint = <<~MD
  # Round 10 Stage 3′ Round 1 — Mandatory Checkpoint

  All five papers failed closed in Stage 3′ Round 1; no decision was emitted. P29 aborted at `phase2a_lint_failed`; P30–P33 aborted at `phase1_lint_failed`. Their mechanically recomputed Major directions and all frozen artifacts remain auditable but cannot be promoted.

  Reply **“确认”** to authorize exactly these next actions:

  - P29–P33: start fresh Stage 3′ Round-2 records with new round ids/manifests and fresh fenced Phase-1/2A contexts; preserve every Round-1 artifact byte-for-byte.

  This checkpoint does **not** authorize manuscript/bibliography edits, Stage 4′ request preparation, Stage 4.5, Stage 5, canonical promotion, submission, Route advancement, result refresh, or new scientific execution.
MD
checkpoint_path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_MANDATORY_CHECKPOINT.md")
queue_output!(checkpoint_path, checkpoint)

totals = {
  "papers" => 5,
  "complete" => 0,
  "aborted" => 5,
  "mechanical_checker_pass" => 5,
  "semantic_audit_pass" => 0,
  "semantic_audit_fail" => 5,
  "recorded" => recorded_totals,
  "audit_supported" => audited_totals,
  "verdict_discrepancies" => 6,
  "false_full_rows" => 4,
  "false_partial_rows" => 2,
  "criterion_inheritance_affected_rows" => 13,
  "phase2b_adjustments" => 0,
  "new_issues" => 0,
  "dissents" => 0,
  "escalation_exceptions" => 0,
  "apply_chain_pass" => 5
}

receipt = {
  "schema_version" => "round10-stage3-prime-round1-outcome/1.1",
  "generated_at" => CHECKED_AT,
  "status" => "ALL_FIVE_ABORTED_FAIL_CLOSED",
  "protocol" => "ARS re-review contract 1.1 / three-gate evidence-before-persuasion",
  "authorization" => {
    "event_path" => "BATCH_ROUND10_STAGE3_PRIME_AUTHOR_EVENT_20260903.txt",
    "event_sha256" => sha256(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_AUTHOR_EVENT_20260903.txt")),
    "authorization_record_path" => "BATCH_ROUND10_STAGE3_PRIME_AUTHORIZATION_RECORD.md",
    "authorization_record_sha256" => sha256(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_AUTHORIZATION_RECORD.md"))
  },
  "validation_receipts" => phase_validation_bindings,
  "semantic_audit" => {
    "fresh_contexts" => "role-separated; exact service call count not instrumented",
    "cross_model" => false,
    "independent_error_process_claimed" => false,
    "sources" => semantic_bindings,
    "consolidation" => consolidation_binding,
    "status" => "FAIL_CLOSED_ALL_FIVE"
  },
  "papers" => batch_papers,
  "totals" => totals,
  "route_boundary" => {
    "formal_route_a_tuples_assigned" => boundary_snapshot.fetch("formal_route_a_tuples_assigned"),
    "positive_arithmetic_a2_results" => boundary_snapshot.fetch("positive_arithmetic_a2_results"),
    "route_b_invocations" => boundary_snapshot.fetch("route_b_invocations"),
    "initial_dynamical_systems_changed" => boundary_snapshot.fetch("initial_dynamical_systems_changed"),
    "canonical_manuscripts_changed" => boundary_snapshot.fetch("canonical_manuscripts_changed"),
    "canonical_bibliographies_changed" => boundary_snapshot.fetch("canonical_bibliographies_changed"),
    "canonical_pdfs_changed" => boundary_snapshot.fetch("canonical_pdfs_changed"),
    "scientific_result_artifacts_changed" => boundary_snapshot.fetch("scientific_result_artifacts_changed")
  },
  "mandatory_checkpoint" => {
    "required" => true,
    "authorization_granted" => false,
    "round2_authorized" => false,
    "stage4_prime_authorization_request_preparation_authorized" => false,
    "p29_revision_authorized" => false,
    "p33_revision_authorized" => false,
    "recommended_combined_action" => "restart P29-P33 Stage 3′ as fresh Round 2 with new manifests and fenced contexts",
    "stage4_5_authorized" => false,
    "stage5_authorized" => false,
    "new_science_authorized" => false
  },
  "terminal_artifacts" => {
    "semantic_audits" => semantic_bindings,
    "semantic_consolidation" => consolidation_binding,
    "checker_receipts" => terminal_checker_receipts,
    "verification_reports" => terminal_verification_reports,
    "abort_records" => terminal_abort_records,
    "batch_report" => binding(report_path),
    "mandatory_checkpoint" => binding(checkpoint_path)
  },
  "same_family_disclosure" => DISCLOSURE
}
receipt_path = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json")
queue_output!(receipt_path, JSON.pretty_generate(receipt) + "\n")

  publication = publish_outputs_transactionally!(boundary_snapshot)
  puts "PASS — emitted Round 10 Stage 3′ terminal outcome: all five fail-closed; final audit #{publication.fetch('final_audit').fetch('sha256')}; fresh Round 2 awaits authorization"
  0
end

if __FILE__ == $PROGRAM_NAME
  begin
    exit_code = main
  # Emit a structured fail-closed record even for an interrupted direct run.
  rescue Exception => error # rubocop:disable Lint/RescueException
    publication_error = error.is_a?(PublicationError)
    rollback_complete = error.rollback_complete if publication_error
    failure = {
      "schema_version" => "round10-stage3-prime-builder-failure/1.0",
      "generated_at" => Time.now.utc.iso8601,
      "status" => "FAIL",
      "error_class" => error.class.name,
      "error" => error.message,
      "outputs_published" => rollback_complete == true ? false : nil,
      "rollback_complete" => rollback_complete,
      "recovery_backup_path" => (error.recovery_backup_path if publication_error),
      "successor_authorized" => false,
      "manuscript_or_science_write_authorized" => false
    }
    warn JSON.pretty_generate(failure)
    exit_code = 1
  end
  exit(exit_code)
end
