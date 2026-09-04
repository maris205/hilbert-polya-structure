#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "securerandom"
require "tempfile"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
AUTHORITY_PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
AUTHORITY = {
  "author_event" => ["#{AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt", "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe"],
  "authorization_record" => ["#{AUTHORITY_PREFIX}_AUTHORIZATION_RECORD.md", "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79"],
  "input_freeze" => ["#{AUTHORITY_PREFIX}_INPUT_FREEZE.json", "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1"],
  "authorization_receipt" => ["#{AUTHORITY_PREFIX}_AUTHORIZATION_RECEIPT.json", "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21"],
  "authority_audit" => ["#{AUTHORITY_PREFIX}_AUTHORITY_AUDIT.json", "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2"]
}.freeze
EXACT_EVENT_BYTES = "确认\n".b.freeze
EXACT_EVENT_SHA = AUTHORITY.fetch("author_event").last
FINAL_MANIFEST = (ROOT / "#{AUTHORITY_PREFIX}_FINAL_EMISSION_MANIFEST.json").freeze
# Filled only after the immutable final-emission manifest is independently
# audited. A nil value intentionally disables every official write.
FINAL_MANIFEST_SHA256 = "db98aa8ace700196044b7bb1903251a90782e709d65f6c0712da041c36421091"

REQUEST = (ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json").freeze
REQUEST_SHA = "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135"
EXACT_CROSS_AUDIT_PATHS = %w[
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P29_P32.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P33.json
].freeze
OLD_AUTHOR_EVENT_SHA = "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812"

PLAN_PRECONDITIONS = [
  "The independent applier has applied every authorized manuscript replacement successfully.",
  "The successor draft and apply report replay the exact patch and authority hashes.",
  "No scientific value, registered claim, structure, bibliography, Route state, or initial system changed."
].freeze
PLAN_WRITER_STATEMENT = "No matrix bytes were modified or regenerated in writer emission."
REQUEST_MATRIX_CONSTRAINTS = [
  "regenerate this exact existing Round-2 matrix path in place only after every authorized manuscript block replacement succeeds",
  "preserve row count, source IDs, registered roles, hypotheses/scopes, and transfer boundaries",
  "record exact locator for each available row and explicit bounded unavailability for every unavailable row",
  "do not guess locators and do not strengthen claims"
].freeze

CONFIG = {
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    base: "stage4_prime_revision_round2.tex",
    matrix: "stage4_prime_claim_passage_matrix_round2.json",
    matrix_kind: "claim-passage",
    matrix_sha: "583ce6edb27860ca77967af7c2cb1afb64214fa8f84c30cf7ede9f6578343dc0",
    matrix_bytes: 15_820,
    source: "stage4_5_round1_source_finalization_proposal.json",
    source_sha: "6337d2c0240982bef5221d346b5e61851cbdc1f154cf92e16dd39234b2900566",
    plan: "stage4_prime_correction_round3_matrix_regeneration_plan.json",
    plan_sha: "949c3ac3bd629c67c4d3605a4b4b173603b1c000d0ef8bae5c47a5b4c7e9b553",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    prepared_patch_sha: "8d8c209bec0c639878b63b7faffcbafafcb1dfe46967cf69b790217e6b1a365b",
    revised: "stage4_prime_revision_round3.tex",
    expected_ops: 34,
    expected: {located: 18, unavailable: 8, retained: 2, rows: 28}
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    base: "stage4_prime_revision_round2.tex",
    matrix: "stage4_prime_method_passage_matrix_round2.json",
    matrix_kind: "method-passage",
    matrix_sha: "e18e78cd31f85858184d01ef1e2a36ae80f80830c80b6b3a2977d0f00206f06b",
    matrix_bytes: 12_020,
    source: "stage4_5_round1_source_finalization_proposal.json",
    source_sha: "37526ac1b63329b06dae9174417ee200483a1c90905a55d3b27a859fba26913a",
    plan: "stage4_prime_correction_round3_matrix_regeneration_plan.json",
    plan_sha: "ce7063c0fe7f24bced010076062acf60ce63716b42eac082ff9b6ed995f0ebe8",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    prepared_patch_sha: "778b35df262cc28fc7aec2bb2d8a1f1c51f62fd6556ece02a5fd88c0266056b5",
    revised: "stage4_prime_revision_round3.tex",
    expected_ops: 13,
    expected: {located: 7, unavailable: 15, retained: 2, rows: 24}
  }
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

def require!(condition, message)
  raise "ROUND10_MATRIX_REGEN_FAIL: #{message}" unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def bytes_sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end

def load_json(path)
  JSON.parse(path.binread)
rescue JSON::ParserError => e
  raise "ROUND10_MATRIX_REGEN_FAIL: invalid JSON #{path}: #{e.message}"
end

def json_bytes(object)
  JSON.pretty_generate(object) + "\n"
end

def root_relative(path)
  path.relative_path_from(ROOT).to_s
end

def binding(path)
  {"path" => root_relative(path), "sha256" => sha(path), "bytes" => path.size}
end

def verify_binding!(row, label, expected_path: nil, expected_sha: nil)
  require!(row.is_a?(Hash), "#{label}: binding is not an object")
  relative = row.fetch("path")
  require!(relative == expected_path, "#{label}: path #{relative} != #{expected_path}") if expected_path
  require!(!Pathname.new(relative).absolute?, "#{label}: absolute path is forbidden")
  path = ROOT / relative
  require!(path.file? && !path.symlink?, "#{label}: missing regular file #{relative}")
  actual = sha(path)
  require!(actual == row.fetch("sha256"), "#{label}: SHA-256 drift #{relative}")
  require!(actual == expected_sha, "#{label}: fixed SHA-256 drift #{relative}") if expected_sha
  require!(path.size == row.fetch("bytes"), "#{label}: byte-count drift #{relative}") if row.key?("bytes")
  path
end

def collect_bindings(node, out = [])
  case node
  when Hash
    if node["path"].is_a?(String) && node["sha256"].is_a?(String)
      out << node
    end
    node.each_value { |value| collect_bindings(value, out) }
  when Array
    node.each { |value| collect_bindings(value, out) }
  end
  out
end

def find_unique_binding!(node, relative, label)
  rows = collect_bindings(node).select { |row| row.fetch("path") == relative }
  require!(rows.length == 1, "#{label}: expected one binding for #{relative}, found #{rows.length}")
  rows.first
end

def verify_internal_exact_authority!(document, label)
  internal = document.fetch("authority")
  require!(internal.keys.sort == AUTHORITY.keys.sort, "#{label}: exact-confirmation authority key set")
  AUTHORITY.each do |role, (relative, expected)|
    verify_binding!(internal.fetch(role), "#{label}: authority #{role}",
                    expected_path: relative, expected_sha: expected)
  end
end

def verify_authority!
  paths = AUTHORITY.transform_values do |relative, expected|
    path = ROOT / relative
    require!(path.file? && !path.symlink? && sha(path) == expected, "exact-confirmation authority drift #{relative}")
    path
  end
  require!(paths.fetch("author_event").binread == EXACT_EVENT_BYTES, "author event is not exact 确认\\n")
  receipt = load_json(paths.fetch("authorization_receipt"))
  freeze = load_json(paths.fetch("input_freeze"))
  audit = load_json(paths.fetch("authority_audit"))
  require!(receipt.fetch("schema_version") ==
           "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authorization-receipt/1.0" &&
           receipt.fetch("status") == "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION",
           "exact-confirmation receipt schema/status")
  require!(freeze.fetch("schema_version") ==
           "round10-stage4-prime-correction-scope-reissue-exact-confirmation-input-freeze/1.0" &&
           freeze.fetch("status") == "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION",
           "exact-confirmation freeze schema/status")
  require!(audit.fetch("schema_version") ==
           "round10-stage4-prime-correction-scope-reissue-exact-confirmation-authority-audit/1.0" &&
           audit.fetch("status") == "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY",
           "exact-confirmation authority-audit schema/status")
  require!(receipt.fetch("author_event") == binding(paths.fetch("author_event")).merge("exact_text" => "确认\n") &&
           freeze.fetch("author_event") == receipt.fetch("author_event"), "authority author-event binding")
  %w[authorization_record input_freeze].each do |role|
    require!(receipt.fetch(role) == binding(paths.fetch(role)), "receipt #{role} binding")
  end
  require!(receipt.fetch("aggregate") == {
    "papers" => 5, "unique_replace_block_pairs" => 130, "matrix_regenerations" => 2,
    "p33_bibliography_appends" => 2
  }, "receipt aggregate scope")
  require!(receipt.fetch("boundaries") == EXPECTED_BOUNDARIES && freeze.fetch("boundaries") == EXPECTED_BOUNDARIES,
           "exact-confirmation boundaries")
  require!(freeze.fetch("prepared_evidence_authority_role") ==
           "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY" &&
           receipt.fetch("prepared_evidence_authority_role") == freeze.fetch("prepared_evidence_authority_role"),
           "prepared evidence was not explicitly non-authorizing")
  require!(freeze.dig("authorized_scope", "per_paper") ==
           {"P29" => 31, "P30" => 34, "P31" => 13, "P32" => 15, "P33" => 37} &&
           freeze.dig("authorized_scope", "p30_p31_in_place_matrix_regenerations") == 2,
           "freeze paper/matrix scope")
  checks = audit.fetch("checks")
  require!(checks.length == 81 && audit.fetch("checks_run") == 81 && audit.fetch("checks_passed") == 81 &&
           audit.fetch("checks_failed") == 0 && checks.all? { |row| row.fetch("status") == "PASS" },
           "authority audit is not 81/81 PASS")
  AUTHORITY.reject { |role, _| role == "authority_audit" }.each_value do |relative, expected|
    row = checks.find { |candidate| candidate.fetch("check_id") == "binding:#{relative}" }
    require!(!row.nil? && row.dig("detail", "expected") == expected && row.dig("detail", "actual") == expected,
             "authority audit binding #{relative}")
  end
  {paths: paths, receipt: receipt, freeze: freeze, audit: audit}
end

def verify_final_manifest!(authority)
  require!(FINAL_MANIFEST_SHA256.is_a?(String) && FINAL_MANIFEST_SHA256.match?(/\A[0-9a-f]{64}\z/),
           "final exact-confirmation emission manifest SHA-256 pin has not been supplied")
  require!(FINAL_MANIFEST.file? && !FINAL_MANIFEST.symlink?, "final exact-confirmation emission manifest is missing")
  require!(sha(FINAL_MANIFEST) == FINAL_MANIFEST_SHA256, "final exact-confirmation emission manifest SHA-256 drift")
  manifest = load_json(FINAL_MANIFEST)
  require!(manifest.fetch("schema_version") ==
           "round10-stage4-prime-scope-reissue-exact-confirmation-final-emission-manifest/1.0" &&
           manifest.fetch("status") == "PASS_EXACT_CONFIRMATION_FINAL_EMISSION_READY_FOR_DETERMINISTIC_APPLY",
           "final emission manifest schema/status")
  require!(manifest.fetch("preparation_evidence_authority_role") ==
           "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY",
           "final manifest preparation-evidence role")
  require!(manifest.fetch("aggregate") == {"papers" => 5, "unique_replace_block_pairs" => 130},
           "final manifest aggregate")
  AUTHORITY.each do |role, (relative, expected)|
    row = manifest.fetch("authority").fetch(role)
    verify_binding!(row, "final manifest authority #{role}", expected_path: relative, expected_sha: expected)
  end
  papers = manifest.fetch("papers")
  require!(papers.map { |row| row.fetch("paper_id") } == %w[P29 P30 P31 P32 P33],
           "final manifest paper order")
  audits = manifest.fetch("root_cross_audits")
  require!(audits.map { |row| row.fetch("path") } == EXACT_CROSS_AUDIT_PATHS,
           "final manifest exact cross-audit set/order")
  covered = []
  audits.each do |row|
    path = verify_binding!(row, "final exact-confirmation cross-audit")
    audit = load_json(path)
    require!(audit.fetch("status") == "PASS", "exact-confirmation cross-audit status #{path.basename}")
    verify_internal_exact_authority!(audit, "exact-confirmation cross-audit #{path.basename}")
    audit.fetch("papers").each do |paper|
      require!(paper.fetch("findings") == [], "#{paper.fetch('paper_id')}: exact-confirmation cross-audit findings")
      covered << paper.fetch("paper_id")
    end
  end
  require!(covered.sort == %w[P29 P30 P31 P32 P33], "exact-confirmation cross-audits do not cover each paper once")
  {object: manifest, sha256: sha(FINAL_MANIFEST), bytes: FINAL_MANIFEST.size}
end

def roadmap_id(source_id)
  source_id.start_with?("REV-") ? source_id : "REV-#{source_id}"
end

def request_scope(paper)
  order = []
  targets = Hash.new { |hash, key| hash[key] = [] }
  paper.fetch("all_requested_targets").each do |target|
    item_id = roadmap_id(target.fetch("issue_id"))
    order << item_id unless order.include?(item_id)
    targets[item_id] << {
      "block_id" => target.fetch("block_id"),
      "allowed_operations" => target.fetch("allowed_operations")
    }
  end
  {"item_ids" => order, "targets" => targets}
end

def deep_sort(value)
  case value
  when Hash
    value.keys.sort.to_h { |key| [key, deep_sort(value.fetch(key))] }
  when Array
    value.map { |entry| deep_sort(entry) }
  else
    value
  end
end

def author_decision_digest(adjudication)
  projection = %w[author_events display_order author_adjudications collateral_authorizations].to_h do |key|
    [key, adjudication.fetch(key)]
  end
  bytes_sha(JSON.generate(deep_sort(projection)))
end

def result_counts(config)
  expected = config.fetch(:expected)
  {
    "bounded_substantive_locator_rows" => expected.fetch(:located),
    "explicit_bounded_unavailability_rows" => expected.fetch(:unavailable),
    "inconclusive_unadjudicated_rows" => 0,
    "preexisting_narrow_record_or_method_locator_rows" => expected.fetch(:retained),
    "row_count" => expected.fetch(:rows)
  }
end

def verify_manifest_paper!(manifest, request_paper, paper_id, config)
  row = manifest.fetch(:object).fetch("papers").find { |candidate| candidate.fetch("paper_id") == paper_id }
  require!(!row.nil? && row.fetch("paper_slug") == config.fetch(:slug) && row.fetch("request_track") == "P30_P31" &&
           row.fetch("authorized_replace_block_pairs") == config.fetch(:expected_ops),
           "#{paper_id}: final manifest identity/scope")
  verify_binding!(row.fetch("request"), "#{paper_id} final manifest request",
                  expected_path: root_relative(REQUEST), expected_sha: REQUEST_SHA)
  scope = request_scope(request_paper)
  trace = row.fetch("source_traceability")
  require!(trace == {
    "mode" => "source_traceability",
    "item_ids" => scope.fetch("item_ids"),
    "count" => scope.fetch("item_ids").length,
    "canonicalization" => "JSON.generate(item_ids) UTF-8",
    "sha256" => bytes_sha(JSON.generate(scope.fetch("item_ids")))
  }, "#{paper_id}: final manifest source traceability")

  notes_prefix = "papers/#{config.fetch(:slug)}/notes/"
  expected_paths = {
    "revision_roadmap" => notes_prefix + config.fetch(:roadmap),
    "author_choices" => notes_prefix + config.fetch(:choices),
    "author_adjudication" => notes_prefix + config.fetch(:adjudication),
    "claim_surface_manifest" => notes_prefix + config.fetch(:claims),
    "patch" => notes_prefix + config.fetch(:patch),
    "writer_handoff" => notes_prefix + config.fetch(:handoff),
    "writer_validation" => notes_prefix + config.fetch(:writer_validation)
  }
  artifacts = row.fetch("artifacts")
  require!(artifacts.keys.sort == expected_paths.keys.sort, "#{paper_id}: final manifest artifact roles")
  expected_paths.each { |role, relative| verify_binding!(artifacts.fetch(role), "#{paper_id} #{role}", expected_path: relative) }

  plan_relative = notes_prefix + config.fetch(:plan)
  plan_binding = find_unique_binding!(row.fetch("supporting_artifacts"), plan_relative,
                                      "#{paper_id} matrix plan support")
  verify_binding!(plan_binding, "#{paper_id} matrix plan support", expected_sha: config.fetch(:plan_sha))
  [row, scope]
end

def verify_resigned_emission!(paper_id, config, row, scope)
  artifacts = row.fetch("artifacts")
  roadmap = load_json(ROOT / artifacts.dig("revision_roadmap", "path"))
  choices = load_json(ROOT / artifacts.dig("author_choices", "path"))
  adjudication = load_json(ROOT / artifacts.dig("author_adjudication", "path"))
  claims = load_json(ROOT / artifacts.dig("claim_surface_manifest", "path"))
  patch = load_json(ROOT / artifacts.dig("patch", "path"))
  handoff = load_json(ROOT / artifacts.dig("writer_handoff", "path"))
  validation = load_json(ROOT / artifacts.dig("writer_validation", "path"))
  prepared_path = ROOT / "papers" / config.fetch(:slug) / "notes" / config.fetch(:prepared_patch)
  require!(prepared_path.file? && sha(prepared_path) == config.fetch(:prepared_patch_sha),
           "#{paper_id}: non-authorizing semantic template drift")
  prepared = load_json(prepared_path)

  require!(roadmap.fetch("items").map { |item| item.fetch("id") } == scope.fetch("item_ids"),
           "#{paper_id}: roadmap source order")
  require!(claims.fetch("surfaces") == [], "#{paper_id}: registered claim surfaces appeared")
  [choices, adjudication].each do |document|
    require!(document.fetch("author_events").length == 1 &&
             document.dig("author_events", 0, "input_sha256") == EXACT_EVENT_SHA,
             "#{paper_id}: re-signed author event")
    require!(document.dig("display_order", "mode") == "source_traceability" &&
             document.dig("display_order", "item_ids") == scope.fetch("item_ids"),
             "#{paper_id}: re-signed display order")
    decisions = document.fetch("author_adjudications")
    require!(decisions.map { |decision| decision.fetch("item_id") } == scope.fetch("item_ids"),
             "#{paper_id}: re-signed decision order")
    decisions.each do |decision|
      item_id = decision.fetch("item_id")
      require!(decision.fetch("author_triage") == "will_address" &&
               decision.fetch("authorized_targets") == scope.fetch("targets").fetch(item_id) &&
               decision.fetch("claim_strength_authorizations") == [],
               "#{paper_id}/#{item_id}: re-signed scope differs")
    end
    require!(document.fetch("collateral_authorizations") == [], "#{paper_id}: collateral authority appeared")
  end
  require!(patch.fetch("patch_format_version") == "1.1" && patch.fetch("authorization_context") == "review_roadmap" &&
           patch.fetch("emitted_by") == "draft_writer_agent" && patch.fetch("revision_round") == 3,
           "#{paper_id}: exact-confirmation patch header")
  require!(patch.fetch("ops") == prepared.fetch("ops"),
           "#{paper_id}: re-sign changed prepared semantic operations")
  require!(patch.fetch("roadmap_sha256") == artifacts.dig("revision_roadmap", "sha256") &&
           patch.fetch("author_adjudication_sha256") == artifacts.dig("author_adjudication", "sha256") &&
           patch.fetch("claim_surface_manifest_sha256") == artifacts.dig("claim_surface_manifest", "sha256") &&
           patch.fetch("author_decision_digest") == author_decision_digest(adjudication),
           "#{paper_id}: exact-confirmation patch authority bindings")
  require!(patch.fetch("ops").length == config.fetch(:expected_ops) &&
           patch.fetch("ops").all? { |op| op.fetch("op") == "replace_block" && op.fetch("claim_strength_changes") == [] &&
             op.fetch("collateral_authorization_ids") == [] }, "#{paper_id}: exact-confirmation patch scope")
  [handoff, validation].each do |document|
    encoded = JSON.generate(document)
    [EXACT_EVENT_SHA, AUTHORITY.fetch("authorization_receipt").last, artifacts.dig("patch", "sha256"),
     artifacts.dig("author_choices", "sha256"), artifacts.dig("author_adjudication", "sha256")].each do |digest|
      require!(encoded.include?(digest), "#{paper_id}: re-signed writer artifact omits #{digest}")
    end
  end
  verdict = validation["status"] || validation["verdict"]
  require!(verdict.to_s.start_with?("PASS"), "#{paper_id}: exact-confirmation writer validation status")
  require!(JSON.generate(validation).include?("NON_AUTHORIZING") || !JSON.generate(validation).include?(OLD_AUTHOR_EVENT_SHA),
           "#{paper_id}: old author event is not demoted in writer validation")
  [artifacts, patch]
end

def expected_plan(paper_id, config, matrix_relative)
  {
    "schema_version" => "round10-stage4-prime-round3-matrix-regeneration-plan/1.0",
    "paper_id" => paper_id,
    "revision_round" => 3,
    "status" => "NOT_RUN_WRITER_ROLE_FORBIDDEN",
    "matrix_kind" => config.fetch(:matrix_kind),
    "matrix" => {
      "path" => matrix_relative,
      "current_sha256" => config.fetch(:matrix_sha),
      "authorized_operation" => "regenerate_file_from_authorized_block_results",
      "in_place_explicit_exception" => true,
      "expected_result_counts" => result_counts(config)
    },
    "preconditions" => PLAN_PRECONDITIONS,
    "writer_statement" => PLAN_WRITER_STATEMENT
  }
end

def verify_request_and_plan!(request_row, plan, paper_id, config, matrix_relative)
  require!(request_row.fetch("matrix_regeneration") == {
    "constraints" => REQUEST_MATRIX_CONSTRAINTS,
    "expected_current_sha256" => config.fetch(:matrix_sha),
    "expected_result_counts" => result_counts(config),
    "in_place_explicit_exception" => true,
    "operation" => "regenerate_file_from_authorized_block_results",
    "path" => matrix_relative
  }, "#{paper_id}: complete request matrix contract")
  require!(plan == expected_plan(paper_id, config, matrix_relative), "#{paper_id}: complete matrix plan")
end

def verify_apply_report!(paper_id, config, artifacts, patch)
  notes = ROOT / "papers" / config.fetch(:slug) / "notes"
  base = notes / config.fetch(:base)
  revised = notes / config.fetch(:revised)
  report_path = Pathname.new(revised.to_s + ".apply-report.json")
  require!(base.file? && revised.file? && report_path.file?, "#{paper_id}: official successor/apply report missing")
  report = load_json(report_path)
  require!(report.fetch("report_format_version") == "1.3" && report.fetch("mode") == "patch" &&
           report.fetch("base_path") == root_relative(base) && report.fetch("output_path") == root_relative(revised),
           "#{paper_id}: apply report format/paths")
  require!(report.fetch("base_draft_hash") == sha(base)[0, 12] &&
           report.fetch("output_draft_hash") == sha(revised)[0, 12] &&
           report.fetch("patch_digest") == artifacts.dig("patch", "sha256") &&
           report.fetch("revision_round") == 3 && report.fetch("authorization_context") == "review_roadmap",
           "#{paper_id}: apply report hashes/authority")
  witness = report.fetch("authorization_witness")
  require!(witness.fetch("status") == "pass" &&
           witness.fetch("roadmap_sha256") == artifacts.dig("revision_roadmap", "sha256") &&
           witness.fetch("author_adjudication_sha256") == artifacts.dig("author_adjudication", "sha256") &&
           witness.fetch("author_decision_digest") == patch.fetch("author_decision_digest") &&
           witness.fetch("claim_surface_manifest_sha256") == artifacts.dig("claim_surface_manifest", "sha256") &&
           witness.fetch("registered_claim_surfaces_checked") == 0 &&
           witness.fetch("unregistered_claim_drift_review_required") == true,
           "#{paper_id}: apply authorization witness")
  applied = report.fetch("ops_applied")
  require!(applied.length == config.fetch(:expected_ops), "#{paper_id}: apply op count")
  applied.each_with_index do |row, index|
    op = patch.fetch("ops").fetch(index)
    require!(row == {
      "op_index" => index, "op" => "replace_block", "block_id" => op.fetch("block_id"),
      "roadmap_item_ids" => op.fetch("roadmap_item_ids"), "claim_strength_changes" => [],
      "collateral_authorization_ids" => [], "new_block_ids" => []
    }, "#{paper_id}: apply op #{index} does not exactly replay the final patch")
  end
  require!(report.fetch("fresh_block_ids") == [] && report.fetch("pure_move_pairs") == [] &&
           report.dig("structural_flags", "heading_op_indexes") == [] &&
           report.dig("structural_flags", "section_count_delta") == 0 &&
           report.dig("structural_flags", "touched_ratio_exceeded") == false &&
           report.dig("structural_flags", "any") == false,
           "#{paper_id}: apply structural/fresh-block boundary")
  require!(report.dig("counters", "blocks_touched") == config.fetch(:expected_ops) &&
           report.dig("counters", "blocks_preserved_byte_identical") + config.fetch(:expected_ops) ==
             report.dig("counters", "blocks_total"), "#{paper_id}: apply counters")
  [revised, report_path]
end

def verify_source!(paper_id, source, expected)
  rows = source.fetch("rows")
  require!(source.fetch("paper_id") == paper_id &&
           rows.length == expected.fetch(:located) + expected.fetch(:unavailable) &&
           rows.map { |row| row.fetch("source_id") }.uniq.length == rows.length,
           "#{paper_id}: source-finalization identity/count/uniqueness")
  rows.each do |row|
    require!(row.fetch("claim_strength_increase_allowed") == false,
             "#{paper_id}/#{row.fetch('source_id')}: source allows claim strengthening")
    case row.fetch("finalization_status")
    when "EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT"
      require!(!row.fetch("exact_passage_locator").to_s.empty? && !row.fetch("support_excerpt").to_s.empty? &&
               bytes_sha(row.fetch("support_excerpt")) == row.fetch("support_excerpt_sha256"),
               "#{paper_id}/#{row.fetch('source_id')}: locator/excerpt binding")
    when "EXPLICIT_BOUNDED_PASSAGE_UNAVAILABILITY"
      require!(row.fetch("exact_passage_locator").nil? && row.fetch("support_excerpt").nil? &&
               row.dig("unavailability", "locator_guessing_permitted") == false,
               "#{paper_id}/#{row.fetch('source_id')}: unavailable-source boundary")
    else
      require!(false, "#{paper_id}/#{row.fetch('source_id')}: unknown source-finalization status")
    end
  end
  require!(rows.count { |row| row.fetch("finalization_status").start_with?("EXACT_LOCATOR") } == expected.fetch(:located) &&
           rows.count { |row| row.fetch("finalization_status").start_with?("EXPLICIT_BOUNDED") } == expected.fetch(:unavailable),
           "#{paper_id}: source-finalization partition")
end

def regenerate_matrix!(paper_id, config, matrix, source, authority_rows, final_manifest, revised, apply_report, patch_sha, timestamp)
  expected = config.fetch(:expected)
  require!(matrix.fetch("rows").length == expected.fetch(:rows) &&
           matrix.fetch("rows").map { |row| row.fetch("source_id") }.uniq.length == expected.fetch(:rows),
           "#{paper_id}: matrix row count/uniqueness")
  source_by_id = source.fetch("rows").to_h { |row| [row.fetch("source_id"), row] }
  located = unavailable = retained = 0
  matrix.fetch("rows").each do |row|
    source_row = source_by_id[row.fetch("source_id")]
    if source_row.nil?
      require!(row.fetch("passage_status") == "FINALIZED" && !row.fetch("exact_passage_locator").to_s.empty?,
               "#{paper_id}/#{row.fetch('source_id')}: retained narrow row")
      row["passage_status"] = "RETAINED_PRIOR_NARROW_LOCATOR"
      row["evidence_note"] = row.fetch("evidence_note") +
        "; retained unchanged by the authorized Round-3 regeneration"
      retained += 1
      next
    end
    require!(row.fetch("component_or_claim_role") == source_row.fetch("registered_role") &&
             row.fetch("hypothesis_or_scope") == source_row.fetch("hypothesis_or_scope") &&
             row.fetch("transfer_boundary") == source_row.fetch("transfer_boundary_preserved"),
             "#{paper_id}/#{row.fetch('source_id')}: registered matrix fields drift")
    if source_row.fetch("finalization_status") == "EXACT_LOCATOR_AVAILABLE_FOR_AUTHORIZED_LATER_REPLACEMENT"
      row["exact_passage_locator"] = source_row.fetch("exact_passage_locator")
      row["passage_status"] = "FINALIZED_BOUNDED_LOCATOR"
      row["evidence_note"] = "Authorized source-finalization row #{source_row.fetch('context_id')}; " \
        "support excerpt SHA-256 #{source_row.fetch('support_excerpt_sha256')}; the retained excerpt provides bounded " \
        "context for the registered use and is not proof of the role in full."
      located += 1
    else
      unavailable_row = source_row.fetch("unavailability")
      row["exact_passage_locator"] = nil
      row["passage_status"] = "EXPLICIT_BOUNDED_UNAVAILABILITY"
      row["evidence_note"] = "Authorized source-finalization row #{source_row.fetch('context_id')}; " \
        "#{unavailable_row.fetch('code')}: #{unavailable_row.fetch('detail')} Locator guessing remains prohibited."
      unavailable += 1
    end
  end
  counts = {
    "bounded_substantive_locator_rows" => located,
    "explicit_bounded_unavailability_rows" => unavailable,
    "preexisting_narrow_record_or_method_locator_rows" => retained,
    "inconclusive_unadjudicated_rows" => 0,
    "row_count" => matrix.fetch("rows").length
  }
  require!(counts == result_counts(config), "#{paper_id}: regenerated result counts")
  matrix["generated_at_utc"] = timestamp
  matrix["authorization"] = {
    "path" => root_relative(REQUEST), "sha256" => REQUEST_SHA,
    "operation" => "regenerate_file_from_authorized_block_results", "in_place_explicit_exception" => true,
    "exact_confirmation" => authority_rows,
    "final_emission_manifest" => {
      "path" => root_relative(FINAL_MANIFEST), "sha256" => final_manifest.fetch(:sha256),
      "bytes" => final_manifest.fetch(:bytes)
    }
  }
  matrix["source_finalization"] = {"path" => "notes/#{config.fetch(:source)}", "sha256" => config.fetch(:source_sha)}
  matrix["successor_draft"] = {
    "path" => "notes/#{config.fetch(:revised)}", "sha256" => sha(revised), "bytes" => revised.size,
    "patch_path" => "notes/#{config.fetch(:patch)}", "patch_sha256" => patch_sha,
    "applied_operation_count" => config.fetch(:expected_ops), "apply_report_path" => root_relative(apply_report),
    "apply_report_sha256" => sha(apply_report), "apply_report_bytes" => apply_report.size
  }
  matrix["row_count"] = expected.fetch(:rows)
  matrix["passage_finalized_count"] = located + retained
  matrix["passage_unavailable_count"] = unavailable
  matrix["passage_inconclusive_count"] = 0
  matrix["terminal_disposition_count"] = expected.fetch(:rows)
  matrix["result_counts"] = counts
  matrix["boundary"] = "Every row has a terminal bounded disposition. Exact locators provide bounded context for the preserved registered use and are not proof of the role in full; explicit unavailability is not passage support; no project theorem, scientific result, or Route credit follows."
  counts
end

def stage_bytes(path, bytes, mode: 0o644)
  temporary = Tempfile.new([".#{path.basename}.", ".stage"], path.dirname.to_s)
  temporary.binmode
  temporary.write(bytes)
  temporary.flush
  temporary.fsync
  File.chmod(mode, temporary.path)
  temporary.close
  staged = Pathname.new(temporary.path)
  require!(staged.size == bytes.bytesize && sha(staged) == bytes_sha(bytes), "staged bytes differ for #{path}")
  {target: path, temporary: temporary, staged: staged, sha256: bytes_sha(bytes), bytes: bytes.bytesize}
rescue StandardError
  temporary&.close!
  raise
end

def cleanup_stage(row)
  File.unlink(row.fetch(:staged)) if row.fetch(:staged).exist?
rescue Errno::ENOENT
  nil
end

def fsync_directories(paths)
  paths.map(&:dirname).uniq.each { |directory| File.open(directory.to_s, File::RDONLY) { |handle| handle.fsync } }
end

def promote_batch!(replacements, creations)
  require!(creations.all? { |row| !row.fetch(:target).exist? }, "receipt collision before staging promotion")
  token = "round10-matrix-#{Process.pid}-#{SecureRandom.hex(12)}"
  backups = {}
  installed = []
  created = []
  committed = false
  begin
    replacements.each do |row|
      target = row.fetch(:target)
      require!(target.file? && sha(target) == row.fetch(:before_sha256), "late matrix base drift #{target}")
      backup = target.dirname / ".#{target.basename}.#{token}.backup"
      require!(!backup.exist?, "backup collision #{backup}")
      File.link(target, backup)
      backups[target] = backup
    end
    creations.each { |row| require!(!row.fetch(:target).exist?, "late receipt collision #{row.fetch(:target)}") }
    replacements.each do |row|
      File.rename(row.fetch(:staged), row.fetch(:target))
      installed << row.fetch(:target)
    end
    creations.each do |row|
      # Atomic no-clobber creation: a receipt that appears after preflight
      # raises EEXIST instead of being overwritten.
      File.link(row.fetch(:staged), row.fetch(:target))
      created << row.fetch(:target)
      File.unlink(row.fetch(:staged))
    end
    fsync_directories((replacements + creations).map { |row| row.fetch(:target) })
    yield
    committed = true
  rescue StandardError => error
    rollback_errors = []
    created.reverse_each do |path|
      File.unlink(path) if path.exist?
    rescue StandardError => rollback_error
      rollback_errors << "remove #{path}: #{rollback_error.message}"
    end
    installed.reverse_each do |target|
      backup = backups[target]
      File.rename(backup, target) if backup&.exist?
    rescue StandardError => rollback_error
      rollback_errors << "restore #{target}: #{rollback_error.message}"
    end
    backups.each_value do |backup|
      File.unlink(backup) if backup.exist?
    rescue StandardError => rollback_error
      rollback_errors << "cleanup #{backup}: #{rollback_error.message}"
    end
    fsync_directories((replacements + creations).map { |row| row.fetch(:target) }) rescue nil
    suffix = rollback_errors.empty? ? "" : "; ROLLBACK ERRORS: #{rollback_errors.join('; ')}"
    raise "ROUND10_MATRIX_REGEN_FAIL: batch promotion failed: #{error.message}#{suffix}"
  ensure
    if committed
      backups.each_value do |backup|
        File.unlink(backup) if backup.exist?
      rescue StandardError => cleanup_error
        warn "ROUND10_MATRIX_REGEN_WARNING: committed backup cleanup failed #{backup}: #{cleanup_error.message}"
      end
      fsync_directories(replacements.map { |row| row.fetch(:target) }) rescue nil
    end
    (replacements + creations).each { |row| cleanup_stage(row) }
  end
end

authority = verify_authority!
final_manifest = verify_final_manifest!(authority)
request = load_json(REQUEST)
require!(request.fetch("schema_version") ==
         "round10-stage4-prime-expanded-correction-authorization-request-p30-p31/1.0" &&
         request.fetch("status") == "AWAITING_NEW_EXPLICIT_AUTHOR_CONFIRMATION" &&
         request.dig("totals", "expanded_block_operation_pairs") == 47 &&
         request.dig("totals", "derived_matrix_regenerations") == 2,
         "expanded request schema/status/counts")
request_by_paper = request.fetch("papers").to_h { |row| [row.fetch("paper_id"), row] }
require!(request_by_paper.keys == %w[P30 P31], "expanded request paper order")
timestamp = Time.now.utc.iso8601
transactions = []

# Validate and compute both complete matrix successors and both receipts before
# staging anything. Prepared artifacts are used only as byte-identity semantic
# templates; execution authority comes exclusively from the final manifest.
CONFIG.each do |paper_id, config|
  paper_root = ROOT / "papers" / config.fetch(:slug)
  notes = paper_root / "notes"
  matrix_path = notes / config.fetch(:matrix)
  source_path = notes / config.fetch(:source)
  plan_path = notes / config.fetch(:plan)
  receipt_path = notes / "stage4_prime_correction_round3_matrix_regeneration_receipt.json"
  require!(!receipt_path.exist?, "#{paper_id}: refusing to overwrite matrix receipt")
  require!(matrix_path.file? && !matrix_path.symlink? && sha(matrix_path) == config.fetch(:matrix_sha) &&
           matrix_path.size == config.fetch(:matrix_bytes), "#{paper_id}: matrix base drift")
  require!(source_path.file? && !source_path.symlink? && sha(source_path) == config.fetch(:source_sha),
           "#{paper_id}: source-finalization drift")
  require!(plan_path.file? && sha(plan_path) == config.fetch(:plan_sha), "#{paper_id}: matrix plan drift")
  freeze_paper = authority.fetch(:freeze).fetch("papers").find { |row| row.fetch("paper_id") == paper_id }
  require!(!freeze_paper.nil?, "#{paper_id}: absent from exact-confirmation freeze")
  verify_binding!(freeze_paper.fetch("authorized_in_place_matrix_regeneration"), "#{paper_id} frozen matrix",
                  expected_path: root_relative(matrix_path), expected_sha: config.fetch(:matrix_sha))

  manifest_row, scope = verify_manifest_paper!(final_manifest, request_by_paper.fetch(paper_id), paper_id, config)
  artifacts, patch = verify_resigned_emission!(paper_id, config, manifest_row, scope)
  matrix_relative = root_relative(matrix_path)
  verify_request_and_plan!(request_by_paper.fetch(paper_id), load_json(plan_path), paper_id, config, matrix_relative)
  revised, apply_report = verify_apply_report!(paper_id, config, artifacts, patch)
  exact_audit = final_manifest.fetch(:object).fetch("root_cross_audits").map { |row| load_json(ROOT / row.fetch("path")) }
    .flat_map { |audit| audit.fetch("papers") }.find { |row| row.fetch("paper_id") == paper_id }
  require!(!exact_audit.nil? && exact_audit.fetch("patch_sha256") == artifacts.dig("patch", "sha256") &&
           exact_audit.fetch("op_count") == config.fetch(:expected_ops) && exact_audit.fetch("findings") == [],
           "#{paper_id}: exact-confirmation cross-audit/apply patch binding")

  source = load_json(source_path)
  verify_source!(paper_id, source, config.fetch(:expected))
  matrix = load_json(matrix_path)
  authority_rows = AUTHORITY.transform_values { |relative, _| binding(ROOT / relative) }
  authority_rows.fetch("author_event")["exact_text"] = "确认\n"
  counts = regenerate_matrix!(paper_id, config, matrix, source, authority_rows, final_manifest, revised,
                              apply_report, artifacts.dig("patch", "sha256"), timestamp)
  matrix_bytes = json_bytes(matrix)
  after_sha = bytes_sha(matrix_bytes)
  require!(after_sha != config.fetch(:matrix_sha), "#{paper_id}: regeneration would be a no-op")
  receipt = {
    "schema_version" => "round10-stage4-prime-round3-matrix-regeneration-receipt/1.0",
    "paper_id" => paper_id,
    "generated_at_utc" => timestamp,
    "status" => "PASS_AUTHORIZED_IN_PLACE_REGENERATION",
    "exact_confirmation_authority" => authority_rows,
    "final_emission_manifest" => {
      "path" => root_relative(FINAL_MANIFEST), "sha256" => final_manifest.fetch(:sha256),
      "bytes" => final_manifest.fetch(:bytes)
    },
    "matrix_path" => matrix_relative,
    "before_sha256" => config.fetch(:matrix_sha),
    "before_bytes" => config.fetch(:matrix_bytes),
    "after_sha256" => after_sha,
    "after_bytes" => matrix_bytes.bytesize,
    "source_finalization_path" => root_relative(source_path),
    "source_finalization_sha256" => sha(source_path),
    "plan_path" => root_relative(plan_path),
    "plan_sha256" => sha(plan_path),
    "patch_path" => artifacts.dig("patch", "path"),
    "patch_sha256" => artifacts.dig("patch", "sha256"),
    "successor_draft_path" => root_relative(revised),
    "successor_draft_sha256" => sha(revised),
    "successor_draft_bytes" => revised.size,
    "apply_report_path" => root_relative(apply_report),
    "apply_report_sha256" => sha(apply_report),
    "apply_report_bytes" => apply_report.size,
    "applied_operation_count" => config.fetch(:expected_ops),
    "result_counts" => counts,
    "preserved_fields" => ["source_id", "component_or_claim_role", "hypothesis_or_scope", "transfer_boundary"],
    "boundaries" => {
      "locator_guessing" => false, "claim_strengthening" => false, "scientific_result_change" => false,
      "route_change" => false, "other_matrix_or_tsv_changed" => false
    }
  }
  receipt_bytes = json_bytes(receipt)
  transactions << {
    paper_id: paper_id, matrix_path: matrix_path, receipt_path: receipt_path,
    before_sha: config.fetch(:matrix_sha), matrix_bytes: matrix_bytes, matrix_sha: after_sha,
    receipt_bytes: receipt_bytes, receipt_sha: bytes_sha(receipt_bytes), counts: counts
  }
end

replacement_stages = transactions.map do |row|
  stage_bytes(row.fetch(:matrix_path), row.fetch(:matrix_bytes), mode: row.fetch(:matrix_path).stat.mode & 0o777)
    .merge(before_sha256: row.fetch(:before_sha))
end
creation_stages = transactions.map { |row| stage_bytes(row.fetch(:receipt_path), row.fetch(:receipt_bytes)) }
promote_batch!(replacement_stages, creation_stages) do
  transactions.each do |row|
    require!(sha(row.fetch(:matrix_path)) == row.fetch(:matrix_sha) &&
             row.fetch(:matrix_path).size == row.fetch(:matrix_bytes).bytesize,
             "#{row.fetch(:paper_id)}: promoted matrix mismatch")
    require!(sha(row.fetch(:receipt_path)) == row.fetch(:receipt_sha) &&
             row.fetch(:receipt_path).size == row.fetch(:receipt_bytes).bytesize,
             "#{row.fetch(:paper_id)}: promoted receipt mismatch")
  end
end

transactions.each do |row|
  counts = row.fetch(:counts)
  puts "#{row.fetch(:paper_id)}: matrix regeneration PASS " \
       "#{counts.fetch('bounded_substantive_locator_rows')} located + " \
       "#{counts.fetch('explicit_bounded_unavailability_rows')} unavailable + " \
       "#{counts.fetch('preexisting_narrow_record_or_method_locator_rows')} retained = " \
       "#{counts.fetch('row_count')}; matrix SHA-256 #{row.fetch(:matrix_sha)}"
end
puts "ROUND10_MATRIX_REGEN_BATCH_PASS: 2/2 matrices and 2/2 receipts promoted in one rollback-safe batch"
