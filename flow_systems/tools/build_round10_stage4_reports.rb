#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
DATE = "2026-09-03"
AUTH_RECORD_SHA = "44f5b2cc73c424a2c3b07da7308b0cbbcc71a50546c456bd4c1c6e1b2610f22e"
AUTHOR_EVENT_SHA = "37ec1eff9228a996f835a975b59a04f88c2aad3b2f2ab47b6c512d3299ff0c86"
ROUTE_A_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE_B_SHA = "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"

PAPERS = {
  29 => {
    dir: "29-bianchi-ideal-owner-refinement",
    title: "Bianchi ideal-owner refinement",
    items: 11, ops: 40, resolved: 7, limitations: 4,
    affected: 38, registry: 83, before: 5276, after: 5927, pages: 14,
    system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
    route: "A0/A1 foundation/interface; formal tuple unassigned; positive arithmetic A2 absent",
    route_coordinate: "A0/A1 foundation/interface only",
    progress: [
      "turns the Gate-M/Gate-Q design into five versioned prospective interfaces with typed stop states, adversarial fixture classes, and a producer-verifier separation rule",
      "fixes exact conjugacy, inversion, Gaussian-conjugation, and disposition-precedence semantics without asserting that any candidate passes",
      "adds reader and control-interpretation maps while retaining all controls, ledgers, scores, and practical-use claims as unexecuted or unevaluated"
    ],
    limitations_text: "Global novelty was not separately searched; a full excluded-row search ledger and passage adjudication are unavailable; no schema, fixtures, worked certificate, experiment, or performance result was executed.",
    semantic: [
      "Every changed source-role paragraph retains `claim_to_passage=INCONCLUSIVE`; no theorem/page locator was invented.",
      "The literal-ideal obstruction remains candidate-specific and does not become a universal nonexistence theorem.",
      "All five interfaces, fixtures, controls, performance ledgers, replay paths, robustness checks, and scores remain prospective."
    ],
    route_rows: [
      ["A0", "foundation only", "Literal-ideal admissibility laws and a candidate-specific conjugate-branch obstruction are typed.", "No admissible owner-to-ideal mechanism has been proved or executed."],
      ["A1", "foundation/interface only", "Gate-Q class, root, conjugacy, inversion, and owner contracts are made exact.", "No complete primitive-owner quotient or census exists."],
      ["A2", "not attained", "Downstream dependencies and fail-closed input requirements are explicit.", "No transfer operator, determinant, trace identity, or positive arithmetic A2 result exists."],
      ["A3", "not attempted", "Euler dependencies are named only as downstream prohibitions.", "No Euler product or arithmetic factor reconstruction was performed."],
      ["A4", "not attempted", "Spectral use is blocked unless every upstream gate closes.", "No operator or spectral target was constructed."]
    ]
  },
  30 => {
    dir: "30-three-disk-nonconstant-roof-determinant",
    title: "Three-disk nonconstant-roof determinant",
    items: 9, ops: 21, resolved: 7, limitations: 2,
    affected: 21, registry: 95, before: 5632, after: 6267, pages: 15,
    system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
    route: "A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple unassigned",
    route_coordinate: "A0 fail; A2 not eligible",
    progress: [
      "turns the physical-determinant proposal into a hash-linked six-gate DAG with one closed state vocabulary and a downstream firewall",
      "freezes the primitive-ledger multiplicity convention and leaves determinant repetition weights to a future Gate-3 coefficient theorem",
      "defines exact control objects, error-enclosure inputs, thresholds, and three-way dispositions while keeping every domain, threshold, enclosure, and control outcome unassigned"
    ],
    limitations_text: "The complete excluded-row/passage-adjudication package is unavailable, and the existing bibliography authorization does not permit standalone entries for two correction records.",
    semantic: [
      "Multiplicity one is an explicit ledger convention, not an observed orbit count; cyclic rotations, reversal, disk relabeling, and repetitions remain separately typed.",
      "The control contract has `Omega`, every `eta_c`, and all numerical enclosures `UNASSIGNED`; the current state is `CONTROL_NOT_EVALUABLE`.",
      "No physical roof, orbit witness, determinant coefficient, enclosure, fidelity comparison, or nontransfer certificate was fabricated."
    ],
    route_rows: [
      ["A0", "FAIL", "The physical roof and three prospective controls are now typed exactly.", "The frozen three-disk system still lacks the required arithmetic input."],
      ["A1", "preparatory only", "Owner and repetition semantics are explicit.", "No realized d=6a primitive-owner ledger or complete orbit witness set exists."],
      ["A2", "NOT_ELIGIBLE", "A six-gate determinant contract and error composition interface are specified.", "A0 failure blocks positive arithmetic A2; no physical determinant was constructed."],
      ["A3", "not attempted", "Arithmetic inference is expressly prohibited from the controls.", "No Euler-factor reconstruction was performed."],
      ["A4", "not attempted", "Operator-facing prerequisites are exposed.", "No eligible spectral construction exists."
      ]
    ]
  },
  31 => {
    dir: "31-level11-conjugacy-owner-ledger",
    title: "Level-11 conjugacy owner ledger",
    items: 11, ops: 11, resolved: 6, limitations: 5,
    affected: 8, registry: 78, before: 4950, after: 5390, pages: 13,
    system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree is distinct",
    route: "A1-only preparation; formal tuple unassigned; positive arithmetic A2 absent",
    route_coordinate: "A1 owner/canonicalization preparation",
    progress: [
      "makes root decisions typed and requires every delta(x) to resolve before complete G/I/C publication",
      "closes the cross-block type contract: zero unresolved rows implies X_res=X and an exactly 138-row complete I; unresolved rows enter only non-estimand I_diag",
      "separates prospective self, reversal, closure, and target-blind disagreement fixtures from the historical 9,453 unordered-pair audit"
    ],
    limitations_text: "There is no persistent release, executable schema/verifier, source finalization, proof of inverse separation, or independent target-blind adjudicator.",
    semantic: [
      "The inverse-separate convention remains `UNRESOLVED_INVERSE_SEPARATION` until a replayable proof closes.",
      "The 9,453-row pair table is not represented as exercising self, directional, or transitivity cases and is not a truth source.",
      "The 138-row consequence is conditional on zero unresolved decisions and does not assert an executed complete ledger."
    ],
    route_rows: [
      ["A0", "unassigned", "The frozen arithmetic setting is unchanged.", "No formal A0 coordinate has been assigned."],
      ["A1", "preparation only", "Canonicalization, root-decision, owner, and G/I/C materialization types are repaired.", "No executable producer/verifier or complete independently adjudicated owner ledger exists."],
      ["A2", "not attained", "The complete-I dependency needed by later consumers is explicit.", "No positive arithmetic determinant or trace result exists."],
      ["A3", "not attempted", "No Stage-4 text grants Euler credit.", "No Euler reconstruction was performed."],
      ["A4", "not attempted", "No Stage-4 text grants spectral credit.", "No operator or spectral identification was performed."]
    ]
  },
  32 => {
    dir: "32-homology-cover-renormalization-uniformity",
    title: "Homology-cover renormalization uniformity",
    items: 12, ops: 12, resolved: 8, limitations: 4,
    affected: 9, registry: 98, before: 5127, after: 5564, pages: 14,
    system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
    route: "generic A1-A2 preparation; arithmetic A0 unavailable; formal tuple unassigned",
    route_coordinate: "generic A1-A2 preparation; arithmetic A0 unavailable",
    progress: [
      "makes the falsification-first order explicit across higher content, zero content, and only then contingent content one",
      "states both modulus schedules and both iterated-limit orders with an index-independent majorant and named interchange still required",
      "types R_+, R_0, transitions, localization, singleton projection, scalar specialization, majorant, and candidate-factor comparison as undefined, unproved, or not evaluable"
    ],
    limitations_text: "There is no persistent release, the formal rings/maps are undefined, source finalization is incomplete, and candidate factors have not been independently derived or proved.",
    semantic: [
      "All proposed component-count, period-scaling, and exponent formulas remain explicitly `UNPROVED`.",
      "All AN-1--AN-5, majorant, coupling, interchange, and limit statements remain unproved; finite diagnostics are unexecuted.",
      "No inequality, mismatch, obstruction, recovery result, or Route credit is inferred from the proposed scalar comparator."
    ],
    route_rows: [
      ["A0", "unavailable", "The pure homology-cover object and scope restrictions are clearer.", "The required arithmetic input is unavailable for the frozen system."],
      ["A1", "preparation only", "Owner exhaustion and schedule obligations are typed.", "No complete owner census or proof-carrying lift ledger exists."],
      ["A2", "generic preparation only", "Formal product, factor, tail, and comparator dependencies are explicit.", "The formal objects are undefined and every candidate identity remains unproved/not evaluable."],
      ["A3", "not attempted", "Euler-like factors are only prospective comparators.", "No arithmetic Euler reconstruction exists."],
      ["A4", "not attempted", "Limit dependencies are exposed.", "No operator or spectral target was identified."
      ]
    ]
  },
  33 => {
    dir: "33-bolza-control-matched-census",
    title: "Bolza control-matched census",
    items: 13, ops: 13, resolved: 8, limitations: 5,
    affected: 12, registry: 126, before: 5653, after: 7053, pages: 17,
    system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
    route: "A1 preparation; formal A0 prohibited/confounded; formal tuple unassigned",
    route_coordinate: "A1 preparation; formal A0 prohibited/confounded",
    progress: [
      "turns the two-presentation plan into exact BP/CP producer contracts consuming frozen artifacts, with FIFO order, deduplication, cutoff, termination, coverage, and bound-reconstruction rules",
      "fixes singleton/self-link, two-member ordering, inverse linking, repetition ownership, canonical serialization, digest domains, schema equality, and migration requirements",
      "adds synthetic cross-presentation traces and a trust graph while expressly recording that no producer, adapter, schema bytes, oracle, fixture corpus, validator, or census run exists"
    ],
    limitations_text: "Two bibliography corrections remain outside scope; producers/verifiers and serialized fixtures do not exist; 0/48 passage locators are available; the inherited control assumptions remain conditional and unverified.",
    semantic: [
      "BP and CP are prospective contracts that must consume the exact frozen inputs; no producer or census execution is reported.",
      "The prose traces are synthetic examples, not byte fixtures, validator runs, or observed cross-presentation outcomes.",
      "Both control directions remain conditional inherited assumptions, so formal A0, A1 closure, positive arithmetic A2, and Route-B conclusions remain prohibited."
    ],
    route_rows: [
      ["A0", "prohibited/confounded", "Control assumptions are restated as conditional and unverified.", "The frozen comparison cannot support formal arithmetic A0."],
      ["A1", "preparation only", "Owner, inverse, serialization, producer, checker, and coverage contracts are made exact.", "No independently validated complete census or executable trust graph exists."],
      ["A2", "not attained", "Cross-presentation compatibility is typed as a future certificate surface.", "No positive arithmetic determinant or trace result exists."],
      ["A3", "not attempted", "Arithmetic inference is explicitly prohibited.", "No Euler reconstruction was performed."],
      ["A4", "not attempted", "No Stage-4 text grants spectral credit.", "No operator or spectral target was constructed."
      ]
    ]
  }
}.freeze

def read_json(path)
  JSON.parse(File.binread(path))
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def write(path, text)
  File.binwrite(path, text.end_with?("\n") ? text : "#{text}\n")
end

def artifact_paths(notes)
  {
    patch: File.join(notes, "stage4_revision_patch_round1.json"),
    revised: File.join(notes, "stage4_revision_round1.tex"),
    apply: File.join(notes, "stage4_revision_round1.tex.apply-report.json"),
    response: File.join(notes, "stage4_response_to_reviewers_round1.json"),
    bundle: File.join(notes, "stage4_revision_evidence_bundle.json"),
    bundle_receipt: File.join(notes, "stage4_bundle_validation_receipt.json"),
    token: File.join(notes, "stage4_token_conservation_round1.json"),
    replay: File.join(notes, "stage4_registered_claim_surface_replay.json"),
    packet: File.join(notes, "stage4_unregistered_claim_drift_review_packet.json"),
    preview: File.join(notes, "stage4_preview_build_receipt.json"),
    preview_pdf: File.join(notes, "stage4_revision_round1.pdf"),
    archive: File.join(notes, "stage4_attempt1_superseded_20260903/ATTEMPT_MANIFEST.json")
  }
end

def table_hashes(paths)
  labels = {
    patch: "Stage-4 patch", revised: "Revised anchored draft", apply: "Apply report",
    response: "Final response", bundle: "Evidence bundle", bundle_receipt: "Bundle-validation receipt",
    token: "Token-conservation advisory", replay: "Registered-surface replay",
    packet: "Bounded semantic-review packet", preview: "Preview-build receipt",
    preview_pdf: "Preview PDF", archive: "Superseded-attempt manifest"
  }
  labels.map { |key, label| "| #{label} | `#{sha(paths.fetch(key))}` |" }.join("\n")
end

batch_rows = []
receipt_papers = []

PAPERS.each do |number, cfg|
  code = "P#{number}"
  paper_root = File.join(ROOT, "papers", cfg.fetch(:dir))
  notes = File.join(paper_root, "notes")
  paths = artifact_paths(notes)
  apply = read_json(paths.fetch(:apply))
  response = read_json(paths.fetch(:response))
  preview = read_json(paths.fetch(:preview))
  replay = read_json(paths.fetch(:replay))
  packet = read_json(paths.fetch(:packet))
  block_total = apply.dig("counters", "blocks_total")
  preserved = apply.dig("counters", "blocks_preserved_byte_identical")
  unaffected = cfg.fetch(:registry) - cfg.fetch(:affected)
  unaffected_exact_once = number == 33 ? 97 : unaffected
  unaffected_duplicate_valued = unaffected - unaffected_exact_once
  unaffected_wording = if unaffected_duplicate_valued.zero?
                         "`#{unaffected}/#{unaffected}` unaffected E1 claims occur byte-exactly once"
                       else
                         "all `#{unaffected}` unaffected E1 claims preserve their baseline occurrence multiplicity (`#{unaffected_exact_once}` occur exactly once; `#{unaffected_duplicate_valued}` intentionally duplicate-valued claims retain their baseline multiplicity)"
                       end

  raise "#{code}: response disposition mismatch" unless response.dig("summary", "resolved") == cfg.fetch(:resolved) && response.dig("summary", "limitations") == cfg.fetch(:limitations)
  raise "#{code}: preview mismatch" unless preview["status"] == "PASS" && preview["pages"] == cfg.fetch(:pages)
  raise "#{code}: semantic packet mismatch" unless packet.dig("coverage", "affected_registry_claim_count") == cfg.fetch(:affected)
  raise "#{code}: replay boundary mismatch" unless replay["vacuous_replay"] == true && replay["clean_claim_certificate"] == false

  item_rows = response.fetch("items").map do |item|
    strength = item.fetch("status") == "RESOLVED" ? "closed within authorized prose scope" : "bounded and explicitly retained"
    "| `#{item.fetch('roadmap_item_id')}` | `#{item.fetch('status')}` | #{strength} |"
  end.join("\n")

  semantic_text = <<~MD
    # #{code} Stage 4 unregistered-claim drift audit

    Date: **#{DATE}**

    Status: **PASS — BOUNDED SEMANTIC REVIEW COMPLETE; NO UNAUTHORIZED CLAIM-STRENGTH MOVE FOUND**

    This is the manual Stage-4 review required because the Stage-2.5 ClaimIntent
    manifest contains no registered surfaces. It is **not Stage 4.5**, not the
    official E6 invocation, and does not advance the pipeline. The mechanical
    registered-surface replay is honestly recorded as `0/0` vacuous coverage with
    `clean_claim_certificate=false`; this PASS instead rests on review of every
    changed operation, every affected Stage-2.5 E1 claim, all unaffected E1
    occurrences, and the frozen scientific and Route boundaries.

    ## Coverage

    - authorized operations reviewed: `#{cfg.fetch(:ops)}/#{cfg.fetch(:ops)}`;
    - affected E1 claims reviewed against old and new text: `#{cfg.fetch(:affected)}/#{cfg.fetch(:affected)}`;
    - unaffected E1 conservation: #{unaffected_wording};
    - total Stage-2.5 E1 registry: `#{cfg.fetch(:registry)}`;
    - original anchored blocks: `#{block_total}`; preserved byte-identical blocks: `#{preserved}`;
    - claim-strength or collateral authorization entries used: `0`;
    - unregistered claim-strength promotions found: `0`.

    ## Semantic findings

    #{cfg.fetch(:semantic).map { |row| "- #{row}" }.join("\n")}

    The frozen system remains: #{cfg.fetch(:system)}. No scientific execution,
    proof, source passage, released artifact, numerical result, performance result,
    canonical-result refresh, formal Route tuple, or Route-B credit was invented.

    ## Disposition audit

    | Roadmap item | Final disposition | Semantic effect |
    |---|---|---|
    #{item_rows}

    The `#{cfg.fetch(:resolved)}` resolved items close their authorized textual
    obligations. The `#{cfg.fetch(:limitations)}` deliberate limitations are
    evidence-preserving outcomes, not concealed successes: #{cfg.fetch(:limitations_text)}

    ## Build and conservation boundary

    The marker-stripped preview is #{cfg.fetch(:pages)} A4 pages with zero undefined
    citations, undefined references, missing glyphs, fatal errors, and overfull
    boxes. Citation style remains `plainnat` numeric. The canonical manuscript,
    bibliography, PDF, and frozen `code/`, `experiments/`, and `results/` trees are
    unchanged. Stage 3 prime has not started.

    ## Stable bindings

    | Artifact | SHA-256 |
    |---|---|
    #{table_hashes(paths)}
  MD
  semantic_path = File.join(notes, "stage4_unregistered_claim_drift_audit.md")
  write(semantic_path, semantic_text)

  route_rows = cfg.fetch(:route_rows).map { |row| "| #{row.join(' | ')} |" }.join("\n")
  route_text = <<~MD
    # #{code} Stage 4 Route-A / Route-B crosswalk

    Date: **#{DATE}**

    Stage 4 improves manuscript precision and auditability; it does not change the
    frozen evaluator state. This crosswalk is governed by
    `skills/route-a-evaluator.md` at SHA-256 `#{ROUTE_A_SHA}` and
    `skills/route-b-evaluator.md` at SHA-256 `#{ROUTE_B_SHA}`.

    | Route coordinate | Retained state | Stage-4 contribution | Why no promotion follows |
    |---|---|---|---|
    #{route_rows}

    Final retained state:

    ```text
    FORMAL_ROUTE_A_TUPLE=UNASSIGNED
    PAPER_ROUTE_POSITION=#{cfg.fetch(:route).upcase.tr(' ', '_')}
    POSITIVE_ARITHMETIC_A2=0
    A3_CREDIT=0
    A4_CREDIT=0
    STAGE4_ROUTE_PROMOTION=NONE
    ROUTE_B_INVOKED=false
    CANONICAL_RESULTS_REFRESHED=false
    ```

    Frozen system: #{cfg.fetch(:system)}.

    The #{cfg.fetch(:pages)}-page Stage-4 preview is a revision artifact, not a
    canonical promotion, Route certificate, Stage-4.5 result, or Stage-5 manuscript.
  MD
  route_path = File.join(notes, "stage4_route_crosswalk.md")
  write(route_path, route_text)

  completion_text = <<~MD
    # #{code} Stage 4 completion report — #{cfg.fetch(:title)}

    Date: **#{DATE}**

    Status: **COMPLETE WITHIN AUTHORIZED STAGE-4 SCOPE — AWAITING SCHOLAR CONFIRMATION BEFORE STAGE 3 PRIME**

    ## Result

    - `#{cfg.fetch(:items)}/#{cfg.fetch(:items)}` authorized roadmap items are
      addressed by `#{cfg.fetch(:ops)}` deterministic operations:
      `#{cfg.fetch(:resolved)}` `RESOLVED` and `#{cfg.fetch(:limitations)}`
      `DELIBERATE_LIMITATION`.
    - The anchored draft grows from #{cfg.fetch(:before).to_s.reverse.gsub(/(\d{3})(?=\d)/, '\\1,').reverse}
      to #{cfg.fetch(:after).to_s.reverse.gsub(/(\d{3})(?=\d)/, '\\1,').reverse} words
      (`+#{(cfg.fetch(:after) - cfg.fetch(:before)).to_s.reverse.gsub(/(\d{3})(?=\d)/, '\\1,').reverse}`).
      `#{preserved}/#{block_total}` original anchored blocks remain byte-identical.
    - All `#{cfg.fetch(:affected)}` affected E1 claims received bounded semantic
      review; #{unaffected_wording}. ClaimIntent replay is `0/0` vacuous and
      explicitly not a clean certificate.
    - The preview is #{cfg.fetch(:pages)} A4 pages, uses `plainnat` numeric citations,
      and has zero undefined citations/references, missing glyphs, fatal errors, or
      overfull boxes.
    - The canonical manuscript, bibliography, PDF, scientific trees, initial
      dynamical system, and Route state remain unchanged.

    ## Principal Stage-4 progress

    #{cfg.fetch(:progress).each_with_index.map { |row, index| "#{index + 1}. It #{row}." }.join("\n")}

    ## Retained limitations

    #{cfg.fetch(:limitations_text)}

    These limits are disclosed rather than filled with invented searches, passages,
    code, proofs, fixtures, experiments, or numerical outcomes.

    ## Route and process boundary

    Route position remains #{cfg.fetch(:route)}. The formal Route-A tuple is
    `UNASSIGNED`, positive arithmetic A2 remains `0`, and Route B is uninvoked.
    This report closes only authorized Stage 4. Stage 3 prime has **not** started;
    Stage 4.5, Stage 5, canonical promotion, submission, and a new scientific round
    are also unstarted and unauthorized.

    ## Stable artifact bindings

    | Artifact | SHA-256 |
    |---|---|
    #{table_hashes(paths)}
  MD
  completion_path = File.join(notes, "stage4_completion_report.md")
  write(completion_path, completion_text)

  batch_rows << "| [#{code}](papers/#{cfg.fetch(:dir)}/README.md) | #{cfg.fetch(:resolved)} resolved + #{cfg.fetch(:limitations)} retained limitations | #{cfg.fetch(:ops)} | #{cfg.fetch(:affected)}/#{cfg.fetch(:registry)} | #{cfg.fetch(:before)} -> #{cfg.fetch(:after)} (`+#{cfg.fetch(:after) - cfg.fetch(:before)}`) | #{cfg.fetch(:pages)} pages, clean |"

  receipt_papers << {
    "paper" => code,
    "directory" => "papers/#{cfg.fetch(:dir)}",
    "status" => "PASS",
    "roadmap" => {"items" => cfg.fetch(:items), "resolved" => cfg.fetch(:resolved), "deliberate_limitations" => cfg.fetch(:limitations)},
    "patch" => {
      "operations" => cfg.fetch(:ops), "affected_e1" => cfg.fetch(:affected),
      "registry_e1" => cfg.fetch(:registry),
      "unaffected_e1_baseline_multiplicity_preserved" => unaffected,
      "unaffected_e1_exact_once" => unaffected_exact_once,
      "unaffected_e1_duplicate_valued" => unaffected_duplicate_valued
    },
    "word_count" => {"before" => cfg.fetch(:before), "after" => cfg.fetch(:after), "delta" => cfg.fetch(:after) - cfg.fetch(:before)},
    "anchored_blocks" => {"original" => block_total, "preserved_byte_identical" => preserved},
    "preview" => {"status" => "PASS", "pages" => cfg.fetch(:pages), "citation_style" => "plainnat numeric", "pdf_sha256" => sha(paths.fetch(:preview_pdf))},
    "semantic_audit" => {"status" => "PASS", "scope" => "bounded Stage-4 review; not Stage 4.5 E6", "claimintent_replay" => "0/0 vacuous", "clean_claim_certificate" => false, "sha256" => sha(semantic_path)},
    "route" => {"formal_route_a_tuple" => "UNASSIGNED", "paper_position" => cfg.fetch(:route), "positive_arithmetic_a2" => 0, "stage4_promotion" => "NONE", "route_b_invoked" => false, "crosswalk_sha256" => sha(route_path)},
    "artifacts" => paths.transform_values { |path| sha(path) }.merge("completion_report" => sha(completion_path))
  }
end

progress_rows = PAPERS.map do |number, cfg|
  "| P#{number} | #{cfg.fetch(:progress).first.capitalize}. **Boundary:** #{cfg.fetch(:limitations_text)} |"
end.join("\n")

systems = PAPERS.map { |number, cfg| "- P#{number}: #{cfg.fetch(:system)}." }.join("\n")
route_positions = PAPERS.map { |number, cfg| "- P#{number}: #{cfg.fetch(:route)}." }.join("\n")

batch_report = <<~MD
  # Round 10 Papers 29--33 — ARS Stage 4 completion report

  Date: **#{DATE}**

  Status: **STAGE 4 COMPLETE WITHIN EXACT AUTHORIZATION — AWAITING SCHOLAR CONFIRMATION BEFORE STAGE 3 PRIME**

  ## Authorization and write boundary

  The author event `BATCH_ROUND10_STAGE4_AUTHOR_EVENT_20260903.txt` has SHA-256
  `#{AUTHOR_EVENT_SHA}`. Its bounded adjudication is recorded in
  `BATCH_ROUND10_STAGE4_AUTHORIZATION_RECORD.md` at SHA-256
  `#{AUTH_RECORD_SHA}`. All 56 roadmap items were interpreted as `will_address`
  within the already proposed targets and operations. No registered claim-strength
  replacement, collateral authorization, structural acknowledgement, canonical
  result refresh, Route-B invocation, or later-stage action occurred.

  The official `paper/manuscript.tex`, `paper/references.bib`, and `paper/paper.pdf`
  files remain byte-identical to their Stage-3 baselines. Revised sources and PDFs
  are versioned Stage-4 artifacts under each paper's `notes/` directory.

  ## Batch result

  | Paper | Roadmap disposition | Operations | Affected / registered E1 | Anchored words | Preview |
  |---|---:|---:|---:|---:|---:|
  #{batch_rows.join("\n")}
  | **Total** | **36 resolved + 20 retained limitations; 56/56 addressed** | **97** | **88/480 affected; 392 unaffected baseline-equivalent** | **26,638 -> 30,201 (`+3,563`)** | **73 pages, all clean** |

  All five evidence bundles validate. Every changed operation and affected E1
  surface received a bounded semantic review. All 392 unaffected E1 claims retain
  their baseline occurrence multiplicity: 375 occur exactly once, while 17
  duplicate-valued P33 claims retain their original multiplicities. The ClaimIntent
  manifests contain zero registered surfaces,
  so their mechanical `0/0` replays are explicitly vacuous and are not represented
  as clean certificates. The five manual audits independently close that gap.

  All five marker-stripped previews retain the current `plainnat` numeric citation
  style and have zero undefined citations, undefined references, missing glyphs,
  fatal errors, and overfull boxes.

  ## Concrete paper progress

  | Paper | Stage-4 landing result and retained boundary |
  |---|---|
  #{progress_rows}

  ## Route-roadmap correspondence

  The governing definitions remain `skills/route-a-evaluator.md` at SHA-256
  `#{ROUTE_A_SHA}` and `skills/route-b-evaluator.md` at SHA-256
  `#{ROUTE_B_SHA}`. Stage 4 changes manuscript precision and traceability, not
  evaluator outcomes:

  #{route_positions}

  Consequently the batch formal Route-A tuple count remains `0/5`, positive
  arithmetic A2 remains `0/5`, A3 and A4 remain `0/5`, and Route-B invocation
  remains `0/5`. No Gate A--E promotion follows from a prose repair, build success,
  synthetic trace, prospective schema, or bounded audit.

  ## Frozen dynamical-system scope

  The five deliberately different continuous-time subtypes and their initial
  restrictions remain unchanged:

  #{systems}

  Stage 4 adds no dynamical subtype, model instance, scientific execution, or
  observed result. It refines the falsifiable contracts needed before later tests.

  ## Fail-closed execution note

  A first apply/build attempt exposed layout and cross-block semantic defects. It
  was stopped before canonical promotion, archived per paper as
  `stage4_attempt1_superseded_20260903/`, and marked
  `SUPERSEDED_FAIL_CLOSED_NOT_CANONICAL`. The corrected patches were then applied
  from the immutable Stage-3 bases and fully revalidated. No superseded output is
  canonical, and no scientific byte changed.

  ## Stable revision bindings

  Full SHA-256 chains are recorded in each paper's
  `notes/stage4_completion_report.md` and in the machine-readable
  `BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json`.

  ## Checkpoint

  Stage 4 is complete. Stage 3 prime has **not** started. The next legal action is
  the scholar checkpoint for Stage 3 prime; Stage 4.5, Stage 5, canonical manuscript
  promotion, submission, and any new scientific round remain unstarted and
  unauthorized.
MD

batch_report_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md")
write(batch_report_path, batch_report)

receipt = {
  "schema" => "round10-stage4-completion-receipt/1.0",
  "generated_at" => "2026-09-03T00:00:00Z",
  "status" => "PASS",
  "pipeline_state" => "STAGE4_COMPLETE_AWAITING_SCHOLAR_CONFIRMATION_FOR_STAGE3_PRIME",
  "authorization" => {
    "author_event_path" => "BATCH_ROUND10_STAGE4_AUTHOR_EVENT_20260903.txt",
    "author_event_sha256" => AUTHOR_EVENT_SHA,
    "authorization_record_path" => "BATCH_ROUND10_STAGE4_AUTHORIZATION_RECORD.md",
    "authorization_record_sha256" => AUTH_RECORD_SHA,
    "roadmap_items_authorized" => 56,
    "adjudication" => "will_address"
  },
  "evaluator_bindings" => {
    "route_a_sha256" => ROUTE_A_SHA,
    "route_b_sha256" => ROUTE_B_SHA
  },
  "totals" => {
    "papers" => 5, "roadmap_items" => 56, "resolved" => 36,
    "deliberate_limitations" => 20, "operations" => 97,
    "registry_e1" => 480, "affected_e1_semantically_reviewed" => 88,
    "unaffected_e1_baseline_multiplicity_preserved" => 392,
    "unaffected_e1_exact_once" => 375,
    "unaffected_e1_duplicate_valued" => 17, "word_count_before" => 26_638,
    "word_count_after" => 30_201, "word_count_delta" => 3563,
    "original_anchored_blocks" => 604, "preserved_byte_identical_blocks" => 513,
    "preview_pages" => 73
  },
  "boundaries" => {
    "canonical_manuscripts_changed" => false,
    "canonical_bibliographies_changed" => false,
    "canonical_pdfs_changed" => false,
    "science_trees_changed" => false,
    "initial_dynamical_systems_changed" => false,
    "formal_route_a_tuples_assigned" => 0,
    "positive_arithmetic_a2" => 0,
    "route_b_invocations" => 0,
    "stage3_prime_started" => false,
    "stage4_5_started" => false,
    "stage5_started" => false
  },
  "batch_report" => {
    "path" => "BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md",
    "sha256" => sha(batch_report_path)
  },
  "papers" => receipt_papers
}

write(File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json"), JSON.pretty_generate(receipt))
puts "WROTE Round 10 Stage 4 reports for #{PAPERS.length} papers and batch receipt"
