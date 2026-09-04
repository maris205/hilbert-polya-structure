#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "tempfile"
require "time"

# Fail-closed completion gate for the Round-10 Stage 4-prime exact-confirmation
# scope reissue.  This tool is intentionally independent from the apply and
# post-apply finalizer tools: it consumes their receipts and outputs, but never
# applies a patch, builds a manuscript, edits a bibliography/matrix, or promotes
# a canonical paper.
module Round10Stage4PrimeExactConfirmationCompletion
  module_function

  ROOT = Pathname.new(__dir__).parent.expand_path.freeze
  PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
  AUTHOR_EVENT_BYTES = "确认\n".b.freeze
  NON_AUTHORIZING_PREPARATION_ROLE =
    "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"

  AUTHORITY = {
    "author_event" => ["#{PREFIX}_AUTHOR_EVENT_20260904.txt",
                       "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe"],
    "authorization_record" => ["#{PREFIX}_AUTHORIZATION_RECORD.md",
                                "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79"],
    "input_freeze" => ["#{PREFIX}_INPUT_FREEZE.json",
                        "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1"],
    "authorization_receipt" => ["#{PREFIX}_AUTHORIZATION_RECEIPT.json",
                                 "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21"],
    "authority_audit" => ["#{PREFIX}_AUTHORITY_AUDIT.json",
                           "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2"]
  }.freeze

  FINAL_EMISSION_MANIFEST = "#{PREFIX}_FINAL_EMISSION_MANIFEST.json"
  # Independently verified immutable exact-confirmation emission manifest.
  FINAL_EMISSION_MANIFEST_SHA256 =
    "db98aa8ace700196044b7bb1903251a90782e709d65f6c0712da041c36421091"

  CROSS_AUDITS = [
    "BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P29_P32.json",
    "BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P30_P31.json",
    "BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P33.json"
  ].freeze

  REQUESTS = {
    "P29_P32" => ["BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json",
                   "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b"],
    "P30_P31" => ["BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json",
                   "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135"],
    "P33" => ["BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json",
               "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65"]
  }.freeze

  OUTPUTS = {
    report: "#{PREFIX}_COMPLETION_REPORT.md",
    receipt: "#{PREFIX}_COMPLETION_RECEIPT.json",
    checkpoint: "#{PREFIX}_MANDATORY_CHECKPOINT.md",
    audit: "#{PREFIX}_FINAL_AUDIT.json"
  }.freeze

  EXPECTED_BOUNDARIES = {
    "fresh_stage4_5_authorized" => false,
    "p33_re_review_authorized" => false,
    "stage5_or_stage6_authorized" => false,
    "canonical_promotion_authorized" => false,
    "scientific_producer_enumeration_census_or_result_refresh_authorized" => false,
    "route_a_or_route_b_credit_authorized" => false,
    "route_or_initial_system_mutation_authorized" => false,
    "registered_claim_strength_change_authorized_only_if_explicitly_listed" => true,
    "structural_edit_authorized" => false,
    "citation_style" => "natbib numbers sort&compress with plainnat"
  }.freeze

  P33_BIB_AFTER_SHA256 = "98bba3645e32b96c8321dad6b3b8dc11087e11e35af835432cbbbee7f0853747"
  P33_BIB_AFTER_BYTES = 9_594
  P33_BIB_KEYS = %w[P33-S03-CORR P33-S16-CORR].freeze
  P33_USE_IDS = %w[P33-U08 P33-U22 P33-U27 P33-U28 P33-U37].freeze

  PAPER_CONFIG = {
    "P29" => {
      slug: "29-bianchi-ideal-owner-refinement", revision_round: 3,
      base: "stage4_prime_revision_round2.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      revised: "stage4_prime_revision_round3.tex", request_track: "P29_P32",
      ops: 31, total_blocks: 113, preserved_blocks: 82, bib_scope: :notes,
      bib: "stage4_prime_references_round2.bib",
      route: "A0/A1 preparation only; formal Route-A tuple UNASSIGNED; positive A2=0; A3=0; A4=0; Route B not invoked",
      initial_system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
      progress: "The 31-block exact-confirmation correction closes the registered author-side source-traceability and owner-refinement revision scope; admissibility and obstruction statements are now audit-ready, while no owner mechanism or Route credit is claimed."
    },
    "P30" => {
      slug: "30-three-disk-nonconstant-roof-determinant", revision_round: 3,
      base: "stage4_prime_revision_round2.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      revised: "stage4_prime_revision_round3.tex", request_track: "P30_P31",
      ops: 34, total_blocks: 129, preserved_blocks: 95, bib_scope: :notes,
      bib: "stage4_prime_references_round2.bib",
      route: "A0_FAIL / A2_NOT_ELIGIBLE; formal Route-A tuple UNASSIGNED; A3=0; A4=0; Route B not invoked",
      initial_system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
      progress: "The 34-block correction and authorized claim-passage matrix regeneration make the nonconstant-roof determinant prerequisites and source limits auditable; no physical determinant or arithmetic A0 repair was produced."
    },
    "P31" => {
      slug: "31-level11-conjugacy-owner-ledger", revision_round: 3,
      base: "stage4_prime_revision_round2.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      revised: "stage4_prime_revision_round3.tex", request_track: "P30_P31",
      ops: 13, total_blocks: 113, preserved_blocks: 100, bib_scope: :notes,
      bib: "stage4_prime_references_round2.bib",
      route: "A1-only preparation; formal Route-A tuple UNASSIGNED; positive A2=0; A3=0; A4=0; Route B not invoked",
      initial_system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers are repetitions; Hecke degree is distinct",
      progress: "The 13-block correction and authorized method-passage matrix regeneration make conjugacy, root, and owner-ledger contracts auditable; no complete producer-backed owner ledger or A2 result was produced."
    },
    "P32" => {
      slug: "32-homology-cover-renormalization-uniformity", revision_round: 3,
      base: "stage4_prime_revision_round2.tex",
      patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
      revised: "stage4_prime_revision_round3.tex", request_track: "P29_P32",
      ops: 15, total_blocks: 138, preserved_blocks: 123, bib_scope: :notes,
      bib: "stage4_prime_references_round2.bib",
      route: "generic A1--A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B not invoked",
      initial_system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
      progress: "The 15-block correction makes uniformity dependencies, owner scope, and bounded source limitations explicit; the formal products remain unevaluated and no arithmetic A0/A2 credit was produced."
    },
    "P33" => {
      slug: "33-bolza-control-matched-census", revision_round: 2,
      base: "stage4_revision_round1.tex",
      patch: "stage4_prime_revision_patch_round6_exact_confirmation.json",
      revised: "stage4_prime_revision_round2.tex", request_track: "P33",
      ops: 37, total_blocks: 128, preserved_blocks: 91, bib_scope: :paper,
      bib: "references.bib",
      route: "A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; positive A2=0; A3=0; A4=0; Route B not invoked",
      initial_system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
      progress: "The 37-block correction plus exactly two bibliography corrections bind five affected uses and clarify census trust and coverage contracts; no complete census, fresh re-review, or Route credit was produced."
    }
  }.freeze

  SCIENCE_PLACEHOLDERS = {
    "P29" => {
      "experiments/.gitkeep" => ["dc9d77c6b5ce1ec9414ddadd1371c983ab334a80428d972c0f9927bf10a7fc2e", 59],
      "results/.gitkeep" => ["a9965fa2c516e7f7af7e12209d135d56673438f834d7b3a6313fd5dcd195921c", 46]
    },
    "P30" => {
      "experiments/.gitkeep" => ["dc9d77c6b5ce1ec9414ddadd1371c983ab334a80428d972c0f9927bf10a7fc2e", 59],
      "results/.gitkeep" => ["a9965fa2c516e7f7af7e12209d135d56673438f834d7b3a6313fd5dcd195921c", 46]
    },
    "P31" => {
      "experiments/.gitkeep" => ["6df9d48c988acad5795519a644ebb5d55f52c4e88deb5ed87fd47fd1a193156e", 33],
      "results/.gitkeep" => ["87fa44d1ac4bd48df8288c6389e99aa304351ab6c81879d7177c5c31a4e9a050", 25]
    },
    "P32" => {
      "experiments/.gitkeep" => ["6df9d48c988acad5795519a644ebb5d55f52c4e88deb5ed87fd47fd1a193156e", 33],
      "results/.gitkeep" => ["87fa44d1ac4bd48df8288c6389e99aa304351ab6c81879d7177c5c31a4e9a050", 25]
    },
    "P33" => {
      "experiments/.gitkeep" => ["6df9d48c988acad5795519a644ebb5d55f52c4e88deb5ed87fd47fd1a193156e", 33],
      "results/.gitkeep" => ["87fa44d1ac4bd48df8288c6389e99aa304351ab6c81879d7177c5c31a4e9a050", 25]
    }
  }.freeze

  def fail!(message)
    raise "ROUND10_EXACT_CONFIRMATION_COMPLETION_FAIL: #{message}"
  end

  def require!(condition, message)
    fail!(message) unless condition
  end

  def sha256(path)
    Digest::SHA256.file(path).hexdigest
  end

  def bytes_sha256(bytes)
    Digest::SHA256.hexdigest(bytes)
  end

  def load_json(path)
    JSON.parse(path.read)
  rescue JSON::ParserError => error
    fail!("invalid JSON #{relative(path)}: #{error.message}")
  end

  def json_bytes(object)
    (JSON.pretty_generate(object) + "\n").encode("UTF-8")
  end

  def relative(path)
    Pathname.new(path).expand_path.relative_path_from(ROOT).to_s
  rescue ArgumentError
    path.to_s
  end

  def safe_root_path(relative_string, label)
    value = Pathname.new(relative_string)
    require!(!value.absolute? && value.each_filename.none? { |part| part == ".." },
             "#{label}: unsafe path #{relative_string}")
    ROOT / value
  end

  def artifact(path)
    path = Pathname.new(path)
    require!(path.file? && !path.symlink?, "missing or symlinked artifact #{relative(path)}")
    {"path" => relative(path), "sha256" => sha256(path), "bytes" => path.size}
  end

  def memory_artifact(path, bytes)
    {"path" => relative(path), "sha256" => bytes_sha256(bytes), "bytes" => bytes.bytesize}
  end

  def same_binding!(actual, expected, label)
    %w[path sha256 bytes].each do |key|
      require!(actual.fetch(key) == expected.fetch(key), "#{label}: #{key} drift")
    end
  end

  def validate_bound_artifact!(row, label)
    path = safe_root_path(row.fetch("path"), label)
    require!(path.file? && !path.symlink?, "#{label}: missing or symlinked #{row.fetch('path')}")
    require!(sha256(path) == row.fetch("sha256"), "#{label}: SHA-256 drift #{row.fetch('path')}")
    require!(path.size == row.fetch("bytes"), "#{label}: byte-size drift #{row.fetch('path')}") if row.key?("bytes")
    path
  end

  def deep_sort(value)
    case value
    when Hash
      value.keys.sort.each_with_object({}) { |key, out| out[key] = deep_sort(value.fetch(key)) }
    when Array
      value.map { |entry| deep_sort(entry) }
    else
      value
    end
  end

  def authority_rows
    rows = AUTHORITY.to_h do |role, (name, expected_sha)|
      path = ROOT / name
      require!(path.file? && !path.symlink?, "missing exact-confirmation #{role}")
      require!(sha256(path) == expected_sha, "exact-confirmation #{role} digest drift")
      [role, artifact(path)]
    end
    rows.fetch("author_event")["exact_text"] = AUTHOR_EVENT_BYTES.dup.force_encoding("UTF-8")
    rows
  end

  def verify_authority_container!(container, expected, label)
    require!(container.keys.sort == expected.keys.sort, "#{label}: authority key set")
    expected.each do |role, row|
      same_binding!(container.fetch(role), row, "#{label}/#{role}")
    end
    require!(container.dig("author_event", "exact_text") == AUTHOR_EVENT_BYTES.dup.force_encoding("UTF-8"),
             "#{label}: exact author-event text")
  end

  def verify_authority_chain!
    rows = authority_rows
    event = ROOT / AUTHORITY.fetch("author_event").first
    require!(event.binread == AUTHOR_EVENT_BYTES, "author-event bytes are not exact `确认\\n`")

    receipt_path = ROOT / AUTHORITY.fetch("authorization_receipt").first
    freeze_path = ROOT / AUTHORITY.fetch("input_freeze").first
    audit_path = ROOT / AUTHORITY.fetch("authority_audit").first
    receipt = load_json(receipt_path)
    freeze = load_json(freeze_path)
    audit = load_json(audit_path)

    require!(receipt.fetch("schema_version") ==
             "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authorization-receipt/1.0",
             "authorization receipt schema")
    require!(receipt.fetch("status") ==
             "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION",
             "authorization receipt status")
    require!(freeze.fetch("schema_version") ==
             "round10-stage4-prime-correction-scope-reissue-exact-confirmation-input-freeze/1.0",
             "input-freeze schema")
    require!(freeze.fetch("status") == "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION",
             "input-freeze status")
    require!(audit.fetch("schema_version") ==
             "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authority-audit/1.0",
             "authority-audit schema")
    require!(audit.fetch("status") ==
             "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY",
             "authority-audit status")
    require!(audit.fetch("checks_failed") == 0 && audit.fetch("checks").all? { |row| row.fetch("status") == "PASS" },
             "authority-audit checks")
    require!(receipt.fetch("prepared_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE &&
             freeze.fetch("prepared_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
             "prepared artifacts acquired execution authority")
    same_binding!(receipt.fetch("author_event"), rows.fetch("author_event"), "receipt author event")
    %w[authorization_record input_freeze].each do |role|
      same_binding!(receipt.fetch(role), rows.fetch(role), "receipt #{role}")
    end
    require!(receipt.fetch("aggregate") == {
      "papers" => 5, "unique_replace_block_pairs" => 130,
      "matrix_regenerations" => 2, "p33_bibliography_appends" => 2
    }, "authority aggregate")
    require!(receipt.fetch("boundaries") == EXPECTED_BOUNDARIES && freeze.fetch("boundaries") == EXPECTED_BOUNDARIES,
             "exact-confirmation boundaries")
    require!(freeze.fetch("author_event") == rows.fetch("author_event"), "freeze author-event binding")
    [rows, freeze]
  end

  def paper_paths(config)
    paper_root = ROOT / "papers" / config.fetch(:slug)
    notes = paper_root / "notes"
    round = config.fetch(:revision_round)
    revised = notes / config.fetch(:revised)
    bib = config.fetch(:bib_scope) == :notes ? notes / config.fetch(:bib) : paper_root / "paper" / config.fetch(:bib)
    {
      paper_root: paper_root,
      notes: notes,
      base: notes / config.fetch(:base),
      patch: notes / config.fetch(:patch),
      revised: revised,
      apply_report: Pathname.new("#{revised}.apply-report.json"),
      bib: bib,
      output_manifest: notes / "stage4_prime_revision_round#{round}.block-manifest.json",
      bundle: notes / "stage4_prime_revision_evidence_bundle_round#{round}.json",
      bundle_receipt: notes / "stage4_prime_bundle_validation_receipt_round#{round}.json",
      token: notes / "stage4_prime_token_conservation_round#{round}.json",
      response_json: notes / "stage4_prime_response_to_reviewers_round#{round}.json",
      response_md: notes / "stage4_prime_response_to_reviewers_round#{round}.md",
      post_log: notes / "stage4_prime_post_apply_revision_log_round#{round}.md",
      semantic_audit: notes / "stage4_prime_unregistered_claim_drift_audit_round#{round}.md",
      pdf: notes / "stage4_prime_revision_round#{round}.pdf",
      build_log: notes / "stage4_prime_revision_round#{round}.build.log",
      build_transcript: notes / "stage4_prime_preview_build_transcript_round#{round}.log",
      build_receipt: notes / "stage4_prime_revision_round#{round}_build_receipt.json"
    }
  end

  def finalizer_output_paths(config)
    paths = paper_paths(config)
    %i[output_manifest bundle bundle_receipt token response_json response_md post_log
       semantic_audit pdf build_log build_transcript build_receipt].to_h { |key| [key, paths.fetch(key)] }
  end

  def verify_final_emission_manifest!(authority)
    require!(FINAL_EMISSION_MANIFEST_SHA256.is_a?(String) &&
             FINAL_EMISSION_MANIFEST_SHA256.match?(/\A[0-9a-f]{64}\z/),
             "FINAL_EMISSION_MANIFEST_SHA256 pin is nil or invalid")
    path = ROOT / FINAL_EMISSION_MANIFEST
    require!(path.file? && !path.symlink?, "missing final-emission manifest")
    require!(sha256(path) == FINAL_EMISSION_MANIFEST_SHA256, "final-emission manifest pin mismatch")
    manifest = load_json(path)
    require!(manifest.fetch("schema_version") ==
             "round10-stage4-prime-scope-reissue-exact-confirmation-final-emission-manifest/1.0",
             "final-emission manifest schema")
    require!(manifest.fetch("status") ==
             "PASS_EXACT_CONFIRMATION_FINAL_EMISSION_READY_FOR_DETERMINISTIC_APPLY",
             "final-emission manifest status")
    require!(manifest.fetch("preparation_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
             "final-emission prepared-evidence role")
    require!(manifest.fetch("aggregate").fetch("papers") == 5 &&
             manifest.fetch("aggregate").fetch("unique_replace_block_pairs") == 130,
             "final-emission aggregate")
    verify_authority_container!(manifest.fetch("authority"), authority, "final-emission manifest")

    papers = manifest.fetch("papers")
    require!(papers.map { |row| row.fetch("paper_id") } == PAPER_CONFIG.keys,
             "final-emission paper order")
    papers.each do |row|
      paper_id = row.fetch("paper_id")
      config = PAPER_CONFIG.fetch(paper_id)
      paths = paper_paths(config)
      require!(row.fetch("paper_slug") == config.fetch(:slug), "#{paper_id}: final-emission slug")
      require!(row.fetch("authorized_replace_block_pairs") == config.fetch(:ops),
               "#{paper_id}: final-emission op count")
      require!(row.fetch("request_track") == config.fetch(:request_track),
               "#{paper_id}: final-emission request track")
      request_name, request_sha = REQUESTS.fetch(config.fetch(:request_track))
      request = row.fetch("request")
      require!(request.fetch("path") == request_name && request.fetch("sha256") == request_sha,
               "#{paper_id}: final-emission request binding")
      validate_bound_artifact!(request, "#{paper_id} final-emission request")
      artifacts = row.fetch("artifacts")
      require!(artifacts.keys.sort == %w[
        author_adjudication author_choices claim_surface_manifest patch revision_roadmap
        writer_handoff writer_validation
      ].sort, "#{paper_id}: final-emission artifact key set")
      artifacts.each do |key, binding|
        validate_bound_artifact!(binding, "#{paper_id} final-emission #{key}")
      end
      patch_binding = artifacts.fetch("patch")
      require!(patch_binding.fetch("path") == relative(paths.fetch(:patch)),
               "#{paper_id}: final-emission patch path")
      trace = row.fetch("source_traceability")
      require!(trace.fetch("mode") == "source_traceability" &&
               trace.fetch("canonicalization") == "JSON.generate(item_ids) UTF-8" &&
               trace.fetch("count") == trace.fetch("item_ids").length &&
               trace.fetch("sha256") == Digest::SHA256.hexdigest(JSON.generate(trace.fetch("item_ids"))),
               "#{paper_id}: final-emission source traceability")
      adjudication_path = safe_root_path(artifacts.dig("author_adjudication", "path"),
                                         "#{paper_id} adjudication")
      claim_path = safe_root_path(artifacts.dig("claim_surface_manifest", "path"),
                                  "#{paper_id} claim-surface manifest")
      require!(load_json(adjudication_path).dig("display_order", "item_ids") == trace.fetch("item_ids"),
               "#{paper_id}: adjudication/source-traceability order")
      require!(load_json(claim_path).fetch("surfaces") == [],
               "#{paper_id}: registered claim-surface population changed")
      expected_support = case paper_id
                         when "P30"
                           ["papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_correction_round3_matrix_regeneration_plan.json"]
                         when "P31"
                           ["papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_correction_round3_matrix_regeneration_plan.json"]
                         when "P33"
                           [
                             "papers/33-bolza-control-matched-census/notes/stage4_prime_round6_bibliography_append_plan.json",
                             "papers/33-bolza-control-matched-census/notes/stage4_prime_round5_correction_bibliography_prospective.json"
                           ]
                         else
                           []
                         end
      support = row.fetch("supporting_artifacts", {})
      require!(support.values.map { |binding| binding.fetch("path") }.sort == expected_support.sort,
               "#{paper_id}: final-emission supporting-artifact set")
      support.each_value { |binding| validate_bound_artifact!(binding, "#{paper_id} supporting artifact") }
    end

    audit_rows = manifest.fetch("root_cross_audits")
    require!(audit_rows.map { |row| row.fetch("path") } == CROSS_AUDITS,
             "final-emission cross-audit order")
    audit_rows.each { |row| validate_bound_artifact!(row, "final-emission cross-audit") }
    [manifest, artifact(path)]
  end

  def verify_cross_audits!(manifest, authority)
    emissions = manifest.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }
    rows = {}
    bindings = []
    CROSS_AUDITS.each do |name|
      path = ROOT / name
      audit = load_json(path)
      require!(audit.fetch("status") == "PASS", "#{name}: top status")
      verify_authority_container!(audit.fetch("authority"), authority, name)
      audit.fetch("papers").each do |row|
        paper_id = row.fetch("paper_id")
        require!(PAPER_CONFIG.key?(paper_id) && !rows.key?(paper_id),
                 "#{name}: duplicate or unknown paper #{paper_id}")
        emission = emissions.fetch(paper_id)
        require!(row.fetch("patch_path") == emission.dig("artifacts", "patch", "path") &&
                 row.fetch("patch_sha256") == emission.dig("artifacts", "patch", "sha256"),
                 "#{paper_id}: cross-audit patch binding")
        require!(row.fetch("source_traceability_sha256") == emission.dig("source_traceability", "sha256"),
                 "#{paper_id}: cross-audit trace binding")
        require!(row.fetch("op_count") == PAPER_CONFIG.fetch(paper_id).fetch(:ops) &&
                 row.fetch("request_target_count") == PAPER_CONFIG.fetch(paper_id).fetch(:ops),
                 "#{paper_id}: cross-audit counts")
        require!(row.fetch("findings") == [], "#{paper_id}: cross-audit findings")
        checks = row.fetch("checks")
        require!(checks.values.all? { |value| value == "PASS" || value == true },
                 "#{paper_id}: cross-audit non-PASS check")
        rows[paper_id] = row
      end
      bindings << artifact(path)
    end
    require!(rows.keys.sort == PAPER_CONFIG.keys.sort, "cross-audit five-paper coverage")
    p33 = rows.fetch("P33")
    require!(p33.fetch("provenance_mapping_count") == 41 &&
             p33.fetch("bounded_unavailable_use_count") == 48 &&
             p33.fetch("dual_correction_binding_count") == 5 &&
             p33.dig("checks", "physical_block_order") == "PASS" &&
             p33.dig("checks", "all_required_checks_passed") == true,
             "P33 exact cross-audit count/order contract")
    [rows, bindings]
  end

  def parse_blocks(text)
    text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m).to_h
  end

  def verify_apply_and_patch!(paper_id, config, paths, manifest_row, cross_row)
    %i[base patch revised apply_report].each do |key|
      path = paths.fetch(key)
      require!(path.file? && !path.symlink?, "#{paper_id}: missing or symlinked #{key}")
    end
    patch = load_json(paths.fetch(:patch))
    report = load_json(paths.fetch(:apply_report))
    ops = patch.fetch("ops")
    require!(patch.fetch("patch_format_version") == "1.1" &&
             patch.fetch("authorization_context") == "review_roadmap" &&
             patch.fetch("emitted_by") == "draft_writer_agent" &&
             patch.fetch("revision_round") == config.fetch(:revision_round),
             "#{paper_id}: patch schema/role/round")
    require!(ops.length == config.fetch(:ops) &&
             ops.all? { |op| op.fetch("op") == "replace_block" } &&
             ops.map { |op| op.fetch("block_id") }.uniq.length == config.fetch(:ops),
             "#{paper_id}: exact unique replace-block count")
    require!(ops.all? do |op|
      op.fetch("claim_strength_changes") == [] && op.fetch("collateral_authorization_ids") == []
    end, "#{paper_id}: patch claim/collateral authority")
    same_binding!(manifest_row.fetch("artifacts").fetch("patch"), artifact(paths.fetch(:patch)),
                  "#{paper_id}: manifest/patch")
    require!(cross_row.fetch("patch_sha256") == sha256(paths.fetch(:patch)),
             "#{paper_id}: cross-audit/patch drift")

    require!(report.fetch("mode") == "patch" &&
             report.fetch("patch_digest") == sha256(paths.fetch(:patch)) &&
             report.fetch("base_draft_hash") == sha256(paths.fetch(:base))[0, 12] &&
             report.fetch("output_draft_hash") == sha256(paths.fetch(:revised))[0, 12] &&
             report.fetch("revision_round") == config.fetch(:revision_round),
             "#{paper_id}: apply report chain")
    applied = report.fetch("ops_applied")
    require!(applied.length == config.fetch(:ops), "#{paper_id}: applied operation count")
    require!(applied.map { |op| op.fetch("block_id") } == ops.map { |op| op.fetch("block_id") } &&
             applied.map { |op| op.fetch("roadmap_item_ids") } == ops.map { |op| op.fetch("roadmap_item_ids") },
             "#{paper_id}: apply operation order/provenance")
    require!(applied.all? do |op|
      op.fetch("claim_strength_changes") == [] && op.fetch("collateral_authorization_ids") == []
    end, "#{paper_id}: applied claim/collateral authority")
    witness = report.fetch("authorization_witness")
    require!(witness.fetch("status") == "pass" &&
             witness.fetch("unregistered_claim_drift_review_required") == true,
             "#{paper_id}: apply authorization witness")
    require!(report.dig("structural_flags", "any") == false,
             "#{paper_id}: structural apply flag")
    require!(report.dig("counters", "blocks_total") == config.fetch(:total_blocks) &&
             report.dig("counters", "blocks_preserved_byte_identical") == config.fetch(:preserved_blocks),
             "#{paper_id}: block preservation counters")
    fresh_block_ids = report.fetch("fresh_block_ids")
    require!(fresh_block_ids.uniq.length == fresh_block_ids.length &&
             applied.flat_map { |op| op.fetch("new_block_ids") } == fresh_block_ids,
             "#{paper_id}: fresh-block allocation/order")
    source = paths.fetch(:revised).read
    require!(source.scan(/<!--block:B\d{4}-->/).length == config.fetch(:total_blocks) + fresh_block_ids.length,
             "#{paper_id}: successor marker count")
    require!(source.include?("\\usepackage[numbers,sort&compress]{natbib}") &&
             source.include?("\\bibliographystyle{plainnat}"),
             "#{paper_id}: plainnat numeric citation style")
    require!(!source.match?(/[\x00-\x08\x0b\x0c\x0e-\x1f]/),
             "#{paper_id}: TeX control byte")
    [patch, report]
  end

  def verify_output_manifest!(paper_id, config, paths, report)
    object = load_json(paths.fetch(:output_manifest))
    require!(object.fetch("base_draft_hash") == sha256(paths.fetch(:revised))[0, 12],
             "#{paper_id}: output manifest/successor")
    require!(object.fetch("blocks").length == config.fetch(:total_blocks) + report.fetch("fresh_block_ids").length,
             "#{paper_id}: output manifest block count")
  end

  def paper_relative(path, paper_root)
    Pathname.new(path).relative_path_from(paper_root).to_s
  end

  def verify_bundle!(paper_id, config, paths)
    bundle = load_json(paths.fetch(:bundle))
    require!(bundle.fetch("rounds").length == config.fetch(:revision_round),
             "#{paper_id}: evidence bundle round count")
    last = bundle.fetch("rounds").last
    require!(last.fetch("kind") == "review_roadmap" &&
             last.fetch("revision_round") == config.fetch(:revision_round),
             "#{paper_id}: evidence bundle final round")
    {
      "pre_round_draft" => paths.fetch(:base),
      "revision_patch" => paths.fetch(:patch),
      "apply_report" => paths.fetch(:apply_report),
      "post_round_draft" => paths.fetch(:revised)
    }.each do |key, path|
      row = last.fetch(key)
      require!(row.fetch("path") == paper_relative(path, paths.fetch(:paper_root)) &&
               row.fetch("sha256") == sha256(path),
               "#{paper_id}: bundle #{key} binding")
    end
    require!(bundle.dig("final_draft", "sha256") == sha256(paths.fetch(:revised)),
             "#{paper_id}: bundle final draft")

    receipt = load_json(paths.fetch(:bundle_receipt))
    require!(receipt.fetch("schema_version") ==
             "round10-stage4-prime-scope-reissue-bundle-validation/1.0" &&
             receipt.fetch("paper_id") == paper_id && receipt.fetch("status") == "PASS",
             "#{paper_id}: bundle receipt status")
    expected = artifact(paths.fetch(:bundle))
    expected["path"] = paper_relative(paths.fetch(:bundle), paths.fetch(:paper_root))
    same_binding!(receipt.fetch("bundle"), expected, "#{paper_id}: bundle receipt")
  end

  def verify_build!(paper_id, config, paths)
    receipt = load_json(paths.fetch(:build_receipt))
    require!(receipt.fetch("schema_version") ==
             "round10-stage4-prime-scope-reissue-preview-build/1.0" &&
             receipt.fetch("paper_id") == paper_id && receipt.fetch("status") == "PASS_CLEAN",
             "#{paper_id}: build receipt schema/status")
    require!(receipt.fetch("classification") ==
             "NOTES_SIDE_STAGE4_PRIME_CORRECTION_PREVIEW_NOT_CANONICAL_PROMOTION",
             "#{paper_id}: build classification")
    require!(receipt.fetch("compiler_sequence") == %w[lualatex bibtex lualatex lualatex] &&
             receipt.fetch("citation_style") == "natbib[numbers,sort&compress] + plainnat",
             "#{paper_id}: build compiler/citation style")
    %w[undefined_citations undefined_references missing_glyphs fatal_errors overfull_hboxes].each do |key|
      require!(receipt.fetch(key) == 0, "#{paper_id}: non-clean build #{key}")
    end
    require!(receipt.fetch("pages").is_a?(Integer) && receipt.fetch("pages").positive?,
             "#{paper_id}: invalid clean page count")
    bindings = receipt.fetch("bindings")
    {
      "revised_draft_sha256" => paths.fetch(:revised),
      "patch_sha256" => paths.fetch(:patch),
      "evidence_bundle_sha256" => paths.fetch(:bundle),
      "references_bib_sha256" => paths.fetch(:bib),
      "preview_pdf_sha256" => paths.fetch(:pdf),
      "final_build_log_sha256" => paths.fetch(:build_log),
      "build_transcript_sha256" => paths.fetch(:build_transcript)
    }.each do |key, path|
      require!(bindings.fetch(key) == sha256(path), "#{paper_id}: build binding #{key}")
    end
    boundaries = receipt.fetch("boundaries")
    require!(boundaries.fetch("canonical_manuscript_or_pdf_modified") == false &&
             boundaries.fetch("canonical_results_refreshed") == false &&
             boundaries.fetch("fresh_stage4_5_invoked") == false &&
             boundaries.fetch("stage5_or_stage6_invoked") == false &&
             boundaries.fetch("canonical_bibliography_modified") == (paper_id == "P33") &&
             boundaries.fetch("p33_exact_bibliography_exception") == (paper_id == "P33"),
             "#{paper_id}: build boundaries")
    require!(paths.fetch(:pdf).binread(5) == "%PDF-", "#{paper_id}: preview is not a PDF")
    log = paths.fetch(:build_log).read
    require!(!log.match?(/Fatal error|Emergency stop|There were undefined citations|There were undefined references|Missing character:|Overfull \\hbox/i),
             "#{paper_id}: independent final build-log scan")
    receipt
  end

  def verify_response_and_auxiliary!(paper_id, config, paths)
    response = load_json(paths.fetch(:response_json))
    require!(response.fetch("schema_version") ==
             "round10-stage4-prime-scope-reissue-final-response/1.0" &&
             response.fetch("paper_id") == paper_id &&
             response.fetch("artifact_status") == "FINAL_AUTHOR_SIDE_CORRECTION_AWAITING_FRESH_STAGE4_5",
             "#{paper_id}: final response status")
    require!(response.dig("summary", "applied_operations") == config.fetch(:ops) &&
             response.dig("summary", "fresh_stage4_5_run") == false &&
             response.dig("summary", "scientific_execution") == false &&
             response.dig("summary", "route_state_changed") == false,
             "#{paper_id}: final response boundary")
    {
      "patch" => paths.fetch(:patch),
      "revised_draft" => paths.fetch(:revised),
      "apply_report" => paths.fetch(:apply_report)
    }.each do |key, path|
      expected = artifact(path)
      expected["path"] = paper_relative(path, paths.fetch(:paper_root))
      same_binding!(response.fetch(key), expected, "#{paper_id}: response #{key}")
    end
    require!(paths.fetch(:response_md).read.include?("Fresh Stage 4.5") &&
             paths.fetch(:response_md).read.include?("not performed"),
             "#{paper_id}: response Markdown boundary")
    semantic = paths.fetch(:semantic_audit).read
    require!(semantic.include?(config.fetch(:route)) && semantic.include?("Fresh Stage 4.5 was not run"),
             "#{paper_id}: semantic audit Route/Stage 4.5 boundary")
    post_log = paths.fetch(:post_log).read
    require!(post_log.include?(config.fetch(:route)) &&
             post_log.include?("fresh Stage 4.5 remains a separate mandatory checkpoint") &&
             post_log.include?("#{config.fetch(:ops)} operations"),
             "#{paper_id}: post-apply log boundary")
    token = load_json(paths.fetch(:token)).fetch("advisory_execution")
    require!(%w[PASS UNAVAILABLE].include?(token.fetch("status")) && token.fetch("non_blocking") == true,
             "#{paper_id}: token advisory became blocking")
  end

  def verify_support_authority!(receipt, authority, manifest_binding, label)
    verify_authority_container!(receipt.fetch("exact_confirmation_authority"), authority, label)
    same_binding!(receipt.fetch("final_emission_manifest"), manifest_binding,
                  "#{label}/final-emission manifest")
  end

  def verify_matrix_support!(paper_id, config, paths, freeze_paper, authority, manifest_binding)
    receipt_path = paths.fetch(:notes) / "stage4_prime_correction_round3_matrix_regeneration_receipt.json"
    receipt = load_json(receipt_path)
    require!(receipt.fetch("schema_version") ==
             "round10-stage4-prime-round3-matrix-regeneration-receipt/1.0" &&
             receipt.fetch("paper_id") == paper_id &&
             receipt.fetch("status") == "PASS_AUTHORIZED_IN_PLACE_REGENERATION",
             "#{paper_id}: matrix receipt schema/status")
    verify_support_authority!(receipt, authority, manifest_binding, "#{paper_id} matrix receipt")
    matrix_path = safe_root_path(receipt.fetch("matrix_path"), "#{paper_id} matrix")
    frozen = freeze_paper.fetch("authorized_in_place_matrix_regeneration")
    require!(receipt.fetch("matrix_path") == frozen.fetch("path") &&
             receipt.fetch("before_sha256") == frozen.fetch("sha256") &&
             receipt.fetch("before_bytes") == frozen.fetch("bytes"),
             "#{paper_id}: matrix before/freeze binding")
    require!(receipt.fetch("after_sha256") == sha256(matrix_path) &&
             receipt.fetch("after_bytes") == matrix_path.size,
             "#{paper_id}: matrix after binding")
    require!(receipt.fetch("patch_sha256") == sha256(paths.fetch(:patch)) &&
             receipt.fetch("successor_draft_sha256") == sha256(paths.fetch(:revised)) &&
             receipt.fetch("apply_report_sha256") == sha256(paths.fetch(:apply_report)) &&
             receipt.fetch("applied_operation_count") == config.fetch(:ops),
             "#{paper_id}: matrix execution chain")
    expected = paper_id == "P30" ? {
      "bounded_substantive_locator_rows" => 18,
      "explicit_bounded_unavailability_rows" => 8,
      "preexisting_narrow_record_or_method_locator_rows" => 2,
      "inconclusive_unadjudicated_rows" => 0,
      "row_count" => 28
    } : {
      "bounded_substantive_locator_rows" => 7,
      "explicit_bounded_unavailability_rows" => 15,
      "preexisting_narrow_record_or_method_locator_rows" => 2,
      "inconclusive_unadjudicated_rows" => 0,
      "row_count" => 24
    }
    require!(receipt.fetch("result_counts") == expected, "#{paper_id}: matrix receipt counts")
    matrix = load_json(matrix_path)
    require!(matrix.fetch("result_counts") == expected && matrix.fetch("row_count") == expected.fetch("row_count"),
             "#{paper_id}: after-matrix counts")
    %w[locator_guessing claim_strengthening scientific_result_change route_change other_matrix_or_tsv_changed].each do |key|
      require!(receipt.dig("boundaries", key) == false, "#{paper_id}: matrix boundary #{key}")
    end
    [{
      "path" => receipt.fetch("matrix_path"),
      "before_sha256" => receipt.fetch("before_sha256"),
      "before_bytes" => receipt.fetch("before_bytes"),
      "after_sha256" => receipt.fetch("after_sha256"),
      "after_bytes" => receipt.fetch("after_bytes"),
      "kind" => "authorized_support_matrix_replacement"
    }, artifact(receipt_path)]
  end

  def verify_p33_bibliography_support!(config, paths, freeze_paper, authority, manifest_binding)
    receipt_path = paths.fetch(:notes) / "stage4_prime_round6_bibliography_append_receipt.json"
    receipt = load_json(receipt_path)
    require!(receipt.fetch("schema_version") ==
             "round10-p33-stage4-prime-round6-correction-bibliography-receipt/1.0" &&
             receipt.fetch("paper_id") == "P33" &&
             receipt.fetch("status") == "PASS_EXACT_TWO_ENTRY_APPEND_AND_FIVE_USE_BINDING",
             "P33: bibliography receipt schema/status")
    verify_support_authority!(receipt, authority, manifest_binding, "P33 bibliography receipt")
    frozen = freeze_paper.fetch("current_working_bibliography")
    bibliography = receipt.fetch("bibliography")
    require!(bibliography.fetch("path") == paper_relative(paths.fetch(:bib), paths.fetch(:paper_root)) &&
             bibliography.fetch("before_sha256") == frozen.fetch("sha256") &&
             bibliography.fetch("before_bytes") == frozen.fetch("bytes") &&
             bibliography.fetch("after_sha256") == P33_BIB_AFTER_SHA256 &&
             bibliography.fetch("after_bytes") == P33_BIB_AFTER_BYTES &&
             bibliography.fetch("entries_appended") == P33_BIB_KEYS,
             "P33: exact bibliography before/after contract")
    require!(sha256(paths.fetch(:bib)) == P33_BIB_AFTER_SHA256 &&
             paths.fetch(:bib).size == P33_BIB_AFTER_BYTES,
             "P33: canonical bibliography result")
    require!(receipt.fetch("counts") == {
      "entries_appended" => 2, "affected_uses_dual_bound" => 5,
      "existing_entries_overwritten" => 0
    }, "P33: bibliography receipt counts")
    require!(receipt.dig("manuscript", "patch_sha256") == sha256(paths.fetch(:patch)) &&
             receipt.dig("manuscript", "sha256") == sha256(paths.fetch(:revised)) &&
             receipt.dig("manuscript", "apply_report_sha256") == sha256(paths.fetch(:apply_report)) &&
             receipt.dig("manuscript", "applied_operation_count") == config.fetch(:ops),
             "P33: bibliography manuscript chain")
    uses = receipt.dig("manuscript", "dual_bound_uses")
    require!(uses.map { |row| row.fetch("use_id") } == P33_USE_IDS,
             "P33: five-use order")
    blocks = parse_blocks(paths.fetch(:revised).read)
    uses.each do |row|
      block = blocks.fetch(row.fetch("block_id"))
      require!(block.include?("use_id=#{row.fetch('use_id')}"), "#{row.fetch('use_id')}: use marker")
      keys = block.scan(/\\cite(?:p|t)?\{([^}]*)\}/).flatten.flat_map { |group| group.split(",").map(&:strip) }
      require!(keys.include?(row.fetch("base_key")) && keys.include?(row.fetch("correction_key")),
               "#{row.fetch('use_id')}: dual correction binding")
    end
    bib_keys = paths.fetch(:bib).read.scan(/@[A-Za-z]+\{([^,]+),/).flatten
    P33_BIB_KEYS.each { |key| require!(bib_keys.count(key) == 1, "P33: bibliography key #{key} multiplicity") }
    %w[third_entry_added scientific_claim_strengthened systematic_retraction_or_conflict_audit_claimed
       canonical_manuscript_or_pdf_changed fresh_stage4_5_or_re_review_run].each do |key|
      require!(receipt.dig("boundaries", key) == false, "P33: bibliography boundary #{key}")
    end
    [{
      "path" => relative(paths.fetch(:bib)),
      "before_sha256" => bibliography.fetch("before_sha256"),
      "before_bytes" => bibliography.fetch("before_bytes"),
      "after_sha256" => bibliography.fetch("after_sha256"),
      "after_bytes" => bibliography.fetch("after_bytes"),
      "kind" => "authorized_p33_canonical_bibliography_replacement"
    }, artifact(receipt_path)]
  end

  def collect_artifact_rows(value, rows = [])
    case value
    when Hash
      rows << value if value.key?("path") && value.key?("sha256")
      value.each_value { |child| collect_artifact_rows(child, rows) }
    when Array
      value.each { |child| collect_artifact_rows(child, rows) }
    end
    rows
  end

  def verify_science_placeholders!(paper_id, config)
    paper_root = ROOT / "papers" / config.fetch(:slug)
    actual = %w[experiments results].flat_map do |dirname|
      directory = paper_root / dirname
      require!(directory.directory?, "#{paper_id}: missing #{dirname} directory")
      Dir.children(directory).sort.map { |entry| "#{dirname}/#{entry}" }
    end
    expected = SCIENCE_PLACEHOLDERS.fetch(paper_id)
    require!(actual == expected.keys.sort, "#{paper_id}: experiments/results inventory changed")
    expected.map do |relative_path, (expected_sha, expected_bytes)|
      path = paper_root / relative_path
      require!(path.file? && !path.symlink? && sha256(path) == expected_sha && path.size == expected_bytes,
               "#{paper_id}: science/results placeholder drift #{relative_path}")
      artifact(path)
    end
  end

  def verify_no_fresh_stage4_5!(paper_id, config)
    notes = ROOT / "papers" / config.fetch(:slug) / "notes"
    stage_files = Dir.children(notes).select do |name|
      (notes / name).file? && name.match?(/stage4[_\-.]?5/i)
    end
    unexpected = if paper_id == "P33"
                   stage_files
                 else
                   stage_files.reject { |name| name.start_with?("stage4_5_round1") }
                 end
    require!(unexpected.empty?, "#{paper_id}: fresh Stage 4.5 artifact(s) present: #{unexpected.sort.join(', ')}")
  end

  def verify_freeze_replay!(freeze, replacements)
    require!(replacements.keys.sort == [
      "papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_claim_passage_matrix_round2.json",
      "papers/31-level11-conjugacy-owner-ledger/notes/stage4_prime_method_passage_matrix_round2.json",
      "papers/33-bolza-control-matched-census/paper/references.bib"
    ].sort, "authorized support replacement set is not exactly two matrices plus P33 bibliography")
    rows = collect_artifact_rows(freeze)
    require!(rows.length >= 200, "freeze replay row population unexpectedly incomplete")
    grouped = rows.group_by { |row| row.fetch("path") }
    replay_bindings = []
    grouped.each do |relative_path, path_rows|
      path = safe_root_path(relative_path, "freeze replay")
      require!(path.file? && !path.symlink?, "freeze replay missing or symlinked #{relative_path}")
      expected_sha = path_rows.map { |row| row.fetch("sha256") }.uniq
      require!(expected_sha.length == 1, "freeze replay conflicting digest #{relative_path}")
      expected_bytes = path_rows.filter_map { |row| row["bytes"] }.uniq
      require!(expected_bytes.length <= 1, "freeze replay conflicting byte count #{relative_path}")
      replacement = replacements[relative_path]
      if replacement
        require!(replacement.fetch("before_sha256") == expected_sha.first,
                 "freeze/support before digest mismatch #{relative_path}")
        require!(replacement.fetch("before_bytes") == expected_bytes.first,
                 "freeze/support before bytes mismatch #{relative_path}") unless expected_bytes.empty?
        require!(sha256(path) == replacement.fetch("after_sha256") &&
                 path.size == replacement.fetch("after_bytes"),
                 "authorized support result drift #{relative_path}")
      else
        require!(sha256(path) == expected_sha.first, "frozen artifact drift #{relative_path}")
        require!(path.size == expected_bytes.first, "frozen artifact bytes #{relative_path}") unless expected_bytes.empty?
      end
      replay_bindings << artifact(path)
    end
    require!((replacements.keys - grouped.keys).empty?, "authorized replacement absent from freeze")

    freeze_papers = freeze.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }
    require!(freeze_papers.keys == PAPER_CONFIG.keys, "freeze paper order/coverage")
    canonical_changes = []
    freeze_papers.each do |paper_id, row|
      config = PAPER_CONFIG.fetch(paper_id)
      replay_bindings.concat(verify_science_placeholders!(paper_id, config))
      verify_no_fresh_stage4_5!(paper_id, config)
      require!(row.fetch("science_files") == [], "#{paper_id}: unexpected frozen science-file authorization")
      require!(row.fetch("authorized_unique_replace_block_pairs") == config.fetch(:ops),
               "#{paper_id}: freeze operation count")
      require!(row.fetch("paper_slug") == config.fetch(:slug), "#{paper_id}: freeze slug")
      require!(row.fetch("canonical_files").length == 3, "#{paper_id}: canonical file coverage")
      row.fetch("canonical_files").each do |binding|
        current_sha = sha256(safe_root_path(binding.fetch("path"), "#{paper_id} canonical"))
        canonical_changes << binding.fetch("path") if current_sha != binding.fetch("sha256")
      end
      ["initial_system_source", "route_crosswalk"].each do |key|
        binding = row.fetch(key)
        validate_bound_artifact!(binding, "#{paper_id} #{key}")
      end
      route_text = safe_root_path(row.dig("route_crosswalk", "path"), "#{paper_id} route").read
      require!(route_text.include?("Frozen system: #{config.fetch(:initial_system)}."),
               "#{paper_id}: frozen initial-system summary drift")
      require!(route_text.include?("FORMAL_ROUTE_A_TUPLE=UNASSIGNED") &&
               route_text.include?("ROUTE_B_INVOKED=false") &&
               route_text.include?("STAGE4_ROUTE_PROMOTION=NONE"),
               "#{paper_id}: Route crosswalk boundary")
    end
    require!(canonical_changes == ["papers/33-bolza-control-matched-census/paper/references.bib"],
             "P33 bibliography is not the unique canonical change")
    {
      "rows_replayed" => rows.length,
      "unique_paths_replayed" => grouped.length,
      "authorized_replacements" => replacements.values.sort_by { |row| row.fetch("path") },
      "canonical_changes" => canonical_changes,
      "canonical_manuscript_and_pdf_unchanged" => true,
      "science_and_results_unchanged" => true,
      "route_and_initial_system_unchanged" => true,
      "bound_artifacts" => replay_bindings
    }
  end

  def verify_paper!(paper_id, config, manifest_row, cross_row, freeze_paper, authority, manifest_binding)
    paths = paper_paths(config)
    finalizer_outputs = finalizer_output_paths(config)
    finalizer_outputs.each_value do |path|
      require!(path.file? && !path.symlink?, "#{paper_id}: missing finalizer output #{relative(path)}")
      require!(path.size.positive?, "#{paper_id}: empty finalizer output #{relative(path)}")
    end
    _patch, report = verify_apply_and_patch!(paper_id, config, paths, manifest_row, cross_row)
    verify_output_manifest!(paper_id, config, paths, report)
    verify_bundle!(paper_id, config, paths)
    build = verify_build!(paper_id, config, paths)
    verify_response_and_auxiliary!(paper_id, config, paths)

    support_replacement = nil
    support_receipt = nil
    if %w[P30 P31].include?(paper_id)
      support_replacement, support_receipt = verify_matrix_support!(
        paper_id, config, paths, freeze_paper, authority, manifest_binding
      )
    elsif paper_id == "P33"
      support_replacement, support_receipt = verify_p33_bibliography_support!(
        config, paths, freeze_paper, authority, manifest_binding
      )
    end

    bound = %i[base patch revised apply_report bib].map { |key| artifact(paths.fetch(key)) }
    bound.concat(finalizer_outputs.values.map { |path| artifact(path) })
    bound << support_receipt if support_receipt
    record = {
      "paper_id" => paper_id,
      "paper_slug" => config.fetch(:slug),
      "status" => "STAGE4_PRIME_EXACT_CONFIRMATION_AUTHOR_SIDE_CORRECTION_COMPLETE_AWAITING_FRESH_STAGE4_5",
      "explicit_progress" => config.fetch(:progress),
      "route_position" => config.fetch(:route),
      "initial_system" => config.fetch(:initial_system),
      "operations" => config.fetch(:ops),
      "total_blocks" => config.fetch(:total_blocks),
      "successor_total_blocks" => config.fetch(:total_blocks) + report.fetch("fresh_block_ids").length,
      "preserved_blocks_byte_identical" => config.fetch(:preserved_blocks),
      "clean_preview_pages" => build.fetch("pages"),
      "citation_style" => build.fetch("citation_style"),
      "artifacts" => {
        "patch" => artifact(paths.fetch(:patch)),
        "successor_draft" => artifact(paths.fetch(:revised)),
        "apply_report" => artifact(paths.fetch(:apply_report)),
        "output_block_manifest" => artifact(paths.fetch(:output_manifest)),
        "evidence_bundle" => artifact(paths.fetch(:bundle)),
        "bundle_validation_receipt" => artifact(paths.fetch(:bundle_receipt)),
        "preview_pdf" => artifact(paths.fetch(:pdf)),
        "build_receipt" => artifact(paths.fetch(:build_receipt)),
        "final_response_json" => artifact(paths.fetch(:response_json))
      },
      "support_receipt" => support_receipt,
      "boundaries" => {
        "fresh_stage4_5_run" => false,
        "scientific_execution_or_result_refresh" => false,
        "route_or_initial_system_change" => false,
        "canonical_manuscript_or_pdf_promotion" => false,
        "stage5_or_stage6_run" => false
      }
    }.compact
    [record, support_replacement, bound]
  end

  def ensure_completion_output_collisions_absent!
    paths = OUTPUTS.values.map { |name| ROOT / name }
    require!(paths.map(&:to_s).uniq.length == 4, "completion output path collision")
    paths.each { |path| require!(!path.exist?, "refusing to overwrite #{relative(path)}") }
  end

  def normalize_bound_artifacts(rows)
    grouped = rows.group_by { |row| row.fetch("path") }
    grouped.map do |path, entries|
      signatures = entries.map { |row| [row.fetch("sha256"), row.fetch("bytes")] }.uniq
      require!(signatures.length == 1, "snapshot conflicting binding #{path}")
      entries.first.slice("path", "sha256", "bytes")
    end.sort_by { |row| row.fetch("path") }
  end

  def preflight!
    ensure_completion_output_collisions_absent!
    authority, freeze = verify_authority_chain!
    manifest, manifest_binding = verify_final_emission_manifest!(authority)
    cross_rows, cross_bindings = verify_cross_audits!(manifest, authority)
    manifest_rows = manifest.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }
    freeze_rows = freeze.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }
    papers = []
    replacements = {}
    bound = authority.values.map { |row| row.slice("path", "sha256", "bytes") }
    bound << manifest_binding
    bound.concat(cross_bindings)
    bound.concat(collect_artifact_rows(manifest).select { |row| row.key?("bytes") })
    output_paths = []

    PAPER_CONFIG.each do |paper_id, config|
      record, replacement, paper_bound = verify_paper!(
        paper_id, config, manifest_rows.fetch(paper_id), cross_rows.fetch(paper_id),
        freeze_rows.fetch(paper_id), authority, manifest_binding
      )
      papers << record
      bound.concat(paper_bound)
      output_paths.concat(finalizer_output_paths(config).values.map { |path| relative(path) })
      next unless replacement
      require!(!replacements.key?(replacement.fetch("path")),
               "duplicate support replacement #{replacement.fetch('path')}")
      replacements[replacement.fetch("path")] = replacement
    end
    require!(papers.sum { |row| row.fetch("operations") } == 130, "five-paper operation total")
    require!(output_paths.length == 60 && output_paths.uniq.length == 60,
             "finalizer output coverage is not exactly 60 unique artifacts")
    freeze_replay = verify_freeze_replay!(freeze, replacements)
    bound.concat(freeze_replay.delete("bound_artifacts"))
    snapshot = {
      "authority" => authority,
      "final_emission_manifest" => manifest_binding,
      "cross_audits" => cross_bindings,
      "papers" => papers,
      "finalizer_output_paths" => output_paths,
      "freeze_replay" => freeze_replay,
      "bound_artifacts" => normalize_bound_artifacts(bound)
    }
    snapshot["snapshot_sha256"] = Digest::SHA256.hexdigest(JSON.generate(deep_sort(snapshot)))
    snapshot
  end

  def validate_snapshot!(snapshot)
    snapshot.fetch("bound_artifacts").each do |row|
      validate_bound_artifact!(row, "preflight snapshot")
    end
    PAPER_CONFIG.each { |paper_id, config| verify_no_fresh_stage4_5!(paper_id, config) }
    true
  end

  def report_bytes(snapshot, generated_at)
    paper_sections = snapshot.fetch("papers").map do |paper|
      <<~MD
        ## #{paper.fetch('paper_id')} — #{paper.fetch('paper_slug')}

        - Status: **author-side Stage 4′ exact-confirmation correction complete; fresh Stage 4.5 not run**.
        - Concrete progress: #{paper.fetch('explicit_progress')}
        - Deterministic apply: **#{paper.fetch('operations')}/#{paper.fetch('operations')}** authorized replacements; **#{paper.fetch('preserved_blocks_byte_identical')}/#{paper.fetch('total_blocks')}** blocks preserved byte-identically.
        - Clean notes-side preview: **#{paper.fetch('clean_preview_pages')} pages**; `#{paper.fetch('citation_style')}`.
        - Existing Route position: `#{paper.fetch('route_position')}`.
        - Frozen initial system: #{paper.fetch('initial_system')}.
        - Evidence bundle: `#{paper.dig('artifacts', 'evidence_bundle', 'path')}`; build receipt: `#{paper.dig('artifacts', 'build_receipt', 'path')}`.
      MD
    end.join("\n")
    <<~MD
      # Round 10 Stage 4′ exact-confirmation completion report

      Generated: **#{generated_at}**

      Status: **PASS — FIVE-PAPER AUTHOR-SIDE STAGE 4′ CORRECTION COMPLETE; FRESH STAGE 4.5 REQUIRED**

      The exact-confirmation authority chain, immutable final-emission manifest, three independent cross-audits, five deterministic patch applications, two matrix receipts, the P33 bibliography receipt, and all 60 post-apply finalizer outputs passed the completion preflight. The batch applied **130/130** unique `replace_block` operations and preserved **#{snapshot.fetch('papers').sum { |row| row.fetch('preserved_blocks_byte_identical') }}/#{snapshot.fetch('papers').sum { |row| row.fetch('total_blocks') }}** blocks byte-identically.

      The two P30/P31 notes-side matrices are the only matrix changes. P33's canonical `paper/references.bib` is the only canonical bibliography change: exactly `P33-S03-CORR` and `P33-S16-CORR` were appended and dual-bound at exactly five registered uses, yielding SHA-256 `#{P33_BIB_AFTER_SHA256}` and #{P33_BIB_AFTER_BYTES} bytes. Every canonical manuscript/PDF, experiments/results inventory, Route crosswalk, initial-system source, scientific input, and all other frozen artifacts remain unchanged. Citation formatting remains numeric `natbib[numbers,sort&compress] + plainnat`.

      #{paper_sections}
      ## Gate boundary

      Fresh Stage 4.5 has **not** been run. This completion does not authorize or perform silent repair, Stage 5/6, canonical manuscript/PDF promotion, scientific production/result refresh, claim strengthening, or Route/initial-system change. The next legal action is a separate short author confirmation for the five-paper fresh Stage 4.5 integrity audit only.
    MD
  end

  def receipt_object(snapshot, generated_at, report_binding)
    {
      "schema_version" => "round10-stage4-prime-scope-reissue-exact-confirmation-completion-receipt/1.0",
      "generated_at_utc" => generated_at,
      "status" => "PASS_STAGE4_PRIME_EXACT_CONFIRMATION_COMPLETION_AWAITING_FRESH_STAGE4_5",
      "completion_report" => report_binding,
      "preflight_snapshot_sha256" => snapshot.fetch("snapshot_sha256"),
      "authority" => snapshot.fetch("authority"),
      "final_emission_manifest" => snapshot.fetch("final_emission_manifest"),
      "root_cross_audits" => snapshot.fetch("cross_audits"),
      "aggregate" => {
        "papers" => 5,
        "authorized_replace_block_operations" => 130,
        "applied_replace_block_operations" => snapshot.fetch("papers").sum { |row| row.fetch("operations") },
        "post_apply_finalizer_outputs" => snapshot.fetch("finalizer_output_paths").length,
        "evidence_bundles" => snapshot.fetch("papers").count,
        "clean_build_receipts" => snapshot.fetch("papers").count,
        "matrix_regeneration_receipts" => 2,
        "p33_bibliography_entries_appended" => 2,
        "p33_dual_bound_uses" => 5,
        "preserved_blocks_byte_identical" => snapshot.fetch("papers").sum { |row| row.fetch("preserved_blocks_byte_identical") },
        "total_blocks" => snapshot.fetch("papers").sum { |row| row.fetch("total_blocks") }
      },
      "papers" => snapshot.fetch("papers"),
      "freeze_replay" => snapshot.fetch("freeze_replay"),
      "citation_style" => "natbib[numbers,sort&compress] + plainnat",
      "stage4_5" => {"run" => false, "authorized_by_this_receipt" => false},
      "boundaries" => {
        "silent_repair_authorized" => false,
        "stage5_or_stage6_authorized" => false,
        "canonical_promotion_authorized" => false,
        "scientific_execution_or_result_refresh_authorized" => false,
        "route_or_initial_system_change_authorized" => false
      },
      "next_legal_action" => "One new short `确认` may authorize only a fresh five-paper Stage 4.5 integrity audit."
    }
  end

  def checkpoint_bytes(generated_at, report_binding, receipt_binding)
    <<~MD
      # Round 10 mandatory checkpoint after Stage 4′ exact-confirmation completion

      Generated: **#{generated_at}**

      Status: **STOP — FRESH STAGE 4.5 HAS NOT RUN**

      Completion report: `#{report_binding.fetch('path')}` (`#{report_binding.fetch('sha256')}`).

      Completion receipt: `#{receipt_binding.fetch('path')}` (`#{receipt_binding.fetch('sha256')}`).

      The next short **`确认`** authorizes **only** a fresh Stage 4.5 integrity audit of Papers P29–P33 against the completed exact-confirmation Stage 4′ artifacts.

      It does **not** authorize silent repair, any manuscript/Bib/matrix edit, Stage 5 or Stage 6, canonical manuscript/PDF promotion, scientific execution or result refresh, claim strengthening, or any Route/initial-system change. Any defect found at Stage 4.5 must stop for a separately scoped author decision.
    MD
  end

  def audit_object(snapshot, generated_at, report_binding, receipt_binding, checkpoint_binding)
    checks = {
      "exact_five_artifact_authority_chain" => "PASS",
      "immutable_final_emission_manifest_pin" => "PASS",
      "three_independent_cross_audits" => "PASS",
      "five_exact_patches_and_apply_reports_130_of_130" => "PASS",
      "block_preservation_counters" => "PASS",
      "sixty_post_apply_finalizer_outputs" => "PASS",
      "five_evidence_bundles" => "PASS",
      "five_clean_preview_builds_and_positive_page_counts" => "PASS",
      "p30_p31_matrix_receipts_and_after_matrices" => "PASS",
      "p33_exact_two_entry_five_use_bibliography_receipt" => "PASS",
      "numeric_plainnat_citation_style" => "PASS",
      "full_freeze_replay_with_exactly_three_support_replacements" => "PASS",
      "canonical_manuscripts_and_pdfs_unchanged" => "PASS",
      "p33_bibliography_only_canonical_bibliography_change" => "PASS",
      "science_results_route_and_initial_system_unchanged" => "PASS",
      "fresh_stage4_5_not_run" => "PASS",
      "completion_artifact_bindings" => "PASS",
      "next_confirmation_scope_is_stage4_5_only" => "PASS"
    }
    {
      "schema_version" => "round10-stage4-prime-scope-reissue-exact-confirmation-completion-final-audit/1.0",
      "generated_at_utc" => generated_at,
      "status" => "PASS",
      "preflight_snapshot_sha256" => snapshot.fetch("snapshot_sha256"),
      "authority" => snapshot.fetch("authority"),
      "final_emission_manifest" => snapshot.fetch("final_emission_manifest"),
      "completion_artifacts" => {
        "completion_report" => report_binding,
        "completion_receipt" => receipt_binding,
        "mandatory_checkpoint" => checkpoint_binding
      },
      "checks_run" => checks.length,
      "checks_passed" => checks.length,
      "checks_failed" => 0,
      "checks" => checks,
      "findings" => [],
      "stage4_5_run" => false,
      "next_gate" => "fresh five-paper Stage 4.5 integrity audit requires one separate short `确认`"
    }
  end

  def build_completion_candidates(snapshot, generated_at)
    report_path = ROOT / OUTPUTS.fetch(:report)
    receipt_path = ROOT / OUTPUTS.fetch(:receipt)
    checkpoint_path = ROOT / OUTPUTS.fetch(:checkpoint)
    audit_path = ROOT / OUTPUTS.fetch(:audit)

    report = report_bytes(snapshot, generated_at).encode("UTF-8")
    report_binding = memory_artifact(report_path, report)
    receipt = json_bytes(receipt_object(snapshot, generated_at, report_binding))
    receipt_binding = memory_artifact(receipt_path, receipt)
    checkpoint = checkpoint_bytes(generated_at, report_binding, receipt_binding).encode("UTF-8")
    checkpoint_binding = memory_artifact(checkpoint_path, checkpoint)
    audit = json_bytes(audit_object(snapshot, generated_at, report_binding, receipt_binding, checkpoint_binding))

    [
      {path: report_path, bytes: report},
      {path: receipt_path, bytes: receipt},
      {path: checkpoint_path, bytes: checkpoint},
      {path: audit_path, bytes: audit}
    ]
  end

  def validate_completion_candidates!(candidates)
    require!(candidates.map { |row| relative(row.fetch(:path)) } == OUTPUTS.values,
             "completion candidate order/path set")
    candidates.each do |row|
      require!(row.fetch(:bytes).bytesize.positive?, "empty candidate #{relative(row.fetch(:path))}")
      JSON.parse(row.fetch(:bytes)) if row.fetch(:path).extname == ".json"
    end
    report_binding = memory_artifact(candidates.fetch(0).fetch(:path), candidates.fetch(0).fetch(:bytes))
    receipt_binding = memory_artifact(candidates.fetch(1).fetch(:path), candidates.fetch(1).fetch(:bytes))
    checkpoint_binding = memory_artifact(candidates.fetch(2).fetch(:path), candidates.fetch(2).fetch(:bytes))
    receipt = JSON.parse(candidates.fetch(1).fetch(:bytes))
    audit = JSON.parse(candidates.fetch(3).fetch(:bytes))
    same_binding!(receipt.fetch("completion_report"), report_binding, "candidate receipt/report")
    same_binding!(audit.dig("completion_artifacts", "completion_report"), report_binding,
                  "candidate audit/report")
    same_binding!(audit.dig("completion_artifacts", "completion_receipt"), receipt_binding,
                  "candidate audit/receipt")
    same_binding!(audit.dig("completion_artifacts", "mandatory_checkpoint"), checkpoint_binding,
                  "candidate audit/checkpoint")
    require!(audit.fetch("status") == "PASS" && audit.fetch("checks_failed") == 0 &&
             audit.fetch("checks").values.all? { |status| status == "PASS" },
             "candidate final-audit verdict")
    true
  end

  def fsync_directory(directory)
    File.open(directory.to_s, File::RDONLY) { |handle| handle.fsync }
  end

  # Generalized only to permit isolated rollback tests.  Production callers
  # supply the four fixed root paths above.  All candidate bytes are staged
  # before any destination becomes visible; File.link supplies no-clobber
  # creation and every path created by this invocation is removed on failure.
  def atomic_no_clobber_commit!(candidates, before_check: nil, after_check: nil)
    require!(candidates.map { |row| row.fetch(:path).to_s }.uniq.length == candidates.length,
             "duplicate atomic destination")
    candidates.each { |row| require!(!row.fetch(:path).exist?, "atomic destination collision #{row.fetch(:path)}") }
    staged = []
    created = []
    begin
      candidates.each do |row|
        target = row.fetch(:path)
        require!(target.dirname.directory?, "missing atomic destination directory #{target.dirname}")
        file = Tempfile.new([".#{target.basename}.", ".candidate"], target.dirname.to_s)
        file.binmode
        file.write(row.fetch(:bytes))
        file.flush
        file.fsync
        file.chmod(0o644)
        file.close
        candidate = Pathname.new(file.path)
        require!(candidate.stat.dev == target.dirname.stat.dev, "cross-device completion candidate")
        require!(sha256(candidate) == bytes_sha256(row.fetch(:bytes)) &&
                 candidate.size == row.fetch(:bytes).bytesize,
                 "staged completion candidate drift #{target}")
        staged << {target: target, candidate: candidate, tempfile: file}
      end
      before_check&.call
      staged.each { |row| require!(!row.fetch(:target).exist?, "late completion collision #{row.fetch(:target)}") }
      staged.each do |row|
        begin
          File.link(row.fetch(:candidate), row.fetch(:target))
        rescue Errno::EEXIST
          fail!("late completion collision #{row.fetch(:target)}")
        end
        created << row
      end
      created.each do |row|
        require!(File.identical?(row.fetch(:target), row.fetch(:candidate)),
                 "hard-link promotion identity #{row.fetch(:target)}")
      end
      fsync_directory(candidates.first.fetch(:path).dirname)
      after_check&.call
      true
    rescue StandardError
      created.reverse_each do |row|
        target = row.fetch(:target)
        File.unlink(target) if target.exist? && row.fetch(:candidate).exist? && File.identical?(target, row.fetch(:candidate))
      rescue StandardError => cleanup_error
        warn "ROUND10_EXACT_CONFIRMATION_COMPLETION_ROLLBACK_WARNING: #{cleanup_error.message}"
      end
      fsync_directory(candidates.first.fetch(:path).dirname) rescue nil
      raise
    ensure
      staged.each do |row|
        begin
          row.fetch(:tempfile).close! unless row.fetch(:tempfile).nil?
        rescue Errno::ENOENT
          nil
        end
      end
    end
  end

  def run!(arguments)
    require!(arguments == [] || arguments == ["--preflight-only"],
             "usage: #{File.basename($PROGRAM_NAME)} [--preflight-only]")
    snapshot = preflight!
    if arguments == ["--preflight-only"]
      puts "ROUND10_EXACT_CONFIRMATION_COMPLETION_PREFLIGHT_PASS: 5/5 papers; 130/130 ops; 60/60 finalizer outputs; no writes"
      return true
    end

    generated_at = Time.now.utc.iso8601
    candidates = build_completion_candidates(snapshot, generated_at)
    validate_completion_candidates!(candidates)
    snapshot_digest = snapshot.fetch("snapshot_sha256")
    before_check = lambda do
      current = preflight!
      require!(current.fetch("snapshot_sha256") == snapshot_digest,
               "preflight snapshot drift before atomic promotion")
    end
    after_check = lambda do
      validate_snapshot!(snapshot)
      candidates.each do |row|
        path = row.fetch(:path)
        require!(sha256(path) == bytes_sha256(row.fetch(:bytes)) && path.size == row.fetch(:bytes).bytesize,
                 "post-promotion completion artifact drift #{relative(path)}")
      end
    end
    atomic_no_clobber_commit!(candidates, before_check: before_check, after_check: after_check)
    puts "ROUND10_EXACT_CONFIRMATION_COMPLETION_PASS: four root artifacts hard-link promoted; fresh Stage 4.5 still required"
    true
  end
end

if $PROGRAM_NAME == __FILE__
  begin
    Round10Stage4PrimeExactConfirmationCompletion.run!(ARGV)
  rescue StandardError => error
    warn error.message
    exit 1
  end
end
