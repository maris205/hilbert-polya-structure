#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "pathname"
require "securerandom"
require "tempfile"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
PAPER_ROOT = (ROOT / "papers/33-bolza-control-matched-census").freeze
NOTES = (PAPER_ROOT / "notes").freeze
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
OLD_AUTHOR_EVENT_SHA = "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812"
FINAL_MANIFEST = (ROOT / "#{AUTHORITY_PREFIX}_FINAL_EMISSION_MANIFEST.json").freeze
# Filled only after the immutable final-emission manifest is independently
# audited. A nil value intentionally disables every official write.
FINAL_MANIFEST_SHA256 = "db98aa8ace700196044b7bb1903251a90782e709d65f6c0712da041c36421091"
EXACT_CROSS_AUDIT_PATHS = %w[
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P29_P32.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P33.json
].freeze

REQUEST = (ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json").freeze
REQUEST_SHA = "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65"
PLAN = (NOTES / "stage4_prime_round6_bibliography_append_plan.json").freeze
PLAN_SHA = "44ac528b952b74f80ba7a223446d672e636831afbd827b5aadbb976c7de7d249"
PROSPECTIVE = (NOTES / "stage4_prime_round5_correction_bibliography_prospective.json").freeze
PROSPECTIVE_SHA = "0d6c0084359e5482246f25dd935d4793ad391aef04b4d78191a15aaa6c21b68b"
BIB = (PAPER_ROOT / "paper/references.bib").freeze
BASE_BIB_SHA = "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0"
BASE_BIB_BYTES = 8_697
EXPECTED_BIB_SHA = "98bba3645e32b96c8321dad6b3b8dc11087e11e35af835432cbbbee7f0853747"
EXPECTED_BIB_BYTES = 9_594
REVISED = (NOTES / "stage4_prime_revision_round2.tex").freeze
APPLY_REPORT = Pathname.new(REVISED.to_s + ".apply-report.json").freeze
RECEIPT = (NOTES / "stage4_prime_round6_bibliography_append_receipt.json").freeze

ARTIFACT_NAMES = {
  "revision_roadmap" => "stage4_prime_round6_revision_roadmap.json",
  "author_choices" => "stage4_prime_round6_exact_confirmation_author_choices.json",
  "author_adjudication" => "stage4_prime_round6_exact_confirmation_author_adjudication.json",
  "claim_surface_manifest" => "stage4_prime_round6_claim_surface_manifest.json",
  "patch" => "stage4_prime_revision_patch_round6_exact_confirmation.json",
  "writer_handoff" => "stage4_prime_round6_exact_confirmation_writer_handoff.json",
  "writer_validation" => "stage4_prime_round6_exact_confirmation_writer_validation_receipt.json"
}.freeze
PREPARED_PATCH = (NOTES / "stage4_prime_revision_patch_round6.json").freeze
PREPARED_PATCH_SHA = "6de8c7d910d22cf2436f11863689de1bc7d2c35e80027fca42815b95d82e6326"
ALLOWED_KEYS = %w[P33-S03-CORR P33-S16-CORR].freeze
USE_IDS = %w[P33-U08 P33-U22 P33-U27 P33-U28 P33-U37].freeze

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
  raise "ROUND10_P33_BIB_APPEND_FAIL: #{message}" unless condition
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
  raise "ROUND10_P33_BIB_APPEND_FAIL: invalid JSON #{path}: #{e.message}"
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
    out << node if node["path"].is_a?(String) && node["sha256"].is_a?(String)
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
  role = "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"
  require!(freeze.fetch("prepared_evidence_authority_role") == role &&
           receipt.fetch("prepared_evidence_authority_role") == role,
           "prepared evidence is not re-emission-only")
  require!(freeze.dig("authorized_scope", "p33_bibliography_append_keys") == ALLOWED_KEYS &&
           freeze.dig("authorized_scope", "p33_use_bindings") == USE_IDS &&
           freeze.dig("authorized_scope", "p33_supporting_operations") == 7,
           "freeze P33 bibliography scope")
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
    verify_binding!(manifest.fetch("authority").fetch(role), "final manifest authority #{role}",
                    expected_path: relative, expected_sha: expected)
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

def request_scope(request)
  order = []
  targets = Hash.new { |hash, key| hash[key] = [] }
  add = lambda do |item_id, target|
    item_id = roadmap_id(item_id)
    order << item_id unless order.include?(item_id)
    targets[item_id] << {
      "block_id" => target.fetch("block_id"),
      "allowed_operations" => target.fetch("allowed_operations")
    }
  end
  request.dig("carried_forward_exact_request", "items").each do |item|
    item.fetch("proposed_targets").each { |target| add.call(item.fetch("item_id"), target) }
  end
  request.fetch("new_issue_actions").each do |action|
    action.fetch("proposed_targets").each { |target| add.call(action.fetch("action_id"), target) }
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

def verify_manifest_p33!(manifest, request)
  row = manifest.fetch(:object).fetch("papers").find { |candidate| candidate.fetch("paper_id") == "P33" }
  require!(!row.nil? && row.fetch("paper_slug") == "33-bolza-control-matched-census" &&
           row.fetch("request_track") == "P33" && row.fetch("authorized_replace_block_pairs") == 37,
           "P33 final manifest identity/scope")
  verify_binding!(row.fetch("request"), "P33 final manifest request",
                  expected_path: root_relative(REQUEST), expected_sha: REQUEST_SHA)
  scope = request_scope(request)
  trace = row.fetch("source_traceability")
  require!(trace == {
    "mode" => "source_traceability", "item_ids" => scope.fetch("item_ids"),
    "count" => scope.fetch("item_ids").length, "canonicalization" => "JSON.generate(item_ids) UTF-8",
    "sha256" => bytes_sha(JSON.generate(scope.fetch("item_ids")))
  }, "P33 final manifest source traceability")
  expected_paths = ARTIFACT_NAMES.transform_values { |name| "papers/33-bolza-control-matched-census/notes/#{name}" }
  artifacts = row.fetch("artifacts")
  require!(artifacts.keys.sort == expected_paths.keys.sort, "P33 final manifest artifact roles")
  expected_paths.each { |role, relative| verify_binding!(artifacts.fetch(role), "P33 #{role}", expected_path: relative) }

  supporting = row.fetch("supporting_artifacts")
  plan_row = find_unique_binding!(supporting, root_relative(PLAN), "P33 bibliography plan support")
  prospective_row = find_unique_binding!(supporting, root_relative(PROSPECTIVE), "P33 prospective contract support")
  verify_binding!(plan_row, "P33 bibliography plan support", expected_sha: PLAN_SHA)
  verify_binding!(prospective_row, "P33 prospective contract support", expected_sha: PROSPECTIVE_SHA)
  [row, scope]
end

def verify_resigned_emission!(row, scope)
  artifacts = row.fetch("artifacts")
  roadmap = load_json(ROOT / artifacts.dig("revision_roadmap", "path"))
  choices = load_json(ROOT / artifacts.dig("author_choices", "path"))
  adjudication = load_json(ROOT / artifacts.dig("author_adjudication", "path"))
  claims = load_json(ROOT / artifacts.dig("claim_surface_manifest", "path"))
  patch = load_json(ROOT / artifacts.dig("patch", "path"))
  handoff = load_json(ROOT / artifacts.dig("writer_handoff", "path"))
  validation = load_json(ROOT / artifacts.dig("writer_validation", "path"))
  require!(PREPARED_PATCH.file? && sha(PREPARED_PATCH) == PREPARED_PATCH_SHA,
           "P33 non-authorizing semantic template drift")
  prepared = load_json(PREPARED_PATCH)

  require!(roadmap.fetch("items").map { |item| item.fetch("id") } == scope.fetch("item_ids"),
           "P33 roadmap source order")
  require!(claims.fetch("surfaces") == [], "P33 registered claim surfaces appeared")
  [choices, adjudication].each do |document|
    require!(document.fetch("author_events").length == 1 &&
             document.dig("author_events", 0, "input_sha256") == EXACT_EVENT_SHA,
             "P33 re-signed author event")
    require!(document.dig("display_order", "mode") == "source_traceability" &&
             document.dig("display_order", "item_ids") == scope.fetch("item_ids"),
             "P33 re-signed display order")
    decisions = document.fetch("author_adjudications")
    require!(decisions.map { |decision| decision.fetch("item_id") } == scope.fetch("item_ids"),
             "P33 re-signed decision order")
    decisions.each do |decision|
      item_id = decision.fetch("item_id")
      require!(decision.fetch("author_triage") == "will_address" &&
               decision.fetch("authorized_targets") == scope.fetch("targets").fetch(item_id) &&
               decision.fetch("claim_strength_authorizations") == [],
               "P33/#{item_id}: re-signed scope differs")
    end
    require!(document.fetch("collateral_authorizations") == [], "P33 collateral authority appeared")
  end
  require!(patch.fetch("patch_format_version") == "1.1" && patch.fetch("authorization_context") == "review_roadmap" &&
           patch.fetch("emitted_by") == "draft_writer_agent" && patch.fetch("revision_round") == 2,
           "P33 exact-confirmation patch header")
  require!(patch.fetch("ops") == prepared.fetch("ops"), "P33 re-sign changed prepared semantic operations")
  require!(patch.fetch("roadmap_sha256") == artifacts.dig("revision_roadmap", "sha256") &&
           patch.fetch("author_adjudication_sha256") == artifacts.dig("author_adjudication", "sha256") &&
           patch.fetch("claim_surface_manifest_sha256") == artifacts.dig("claim_surface_manifest", "sha256") &&
           patch.fetch("author_decision_digest") == author_decision_digest(adjudication),
           "P33 exact-confirmation patch authority bindings")
  require!(patch.fetch("ops").length == 37 &&
           patch.fetch("ops").all? { |op| op.fetch("op") == "replace_block" && op.fetch("claim_strength_changes") == [] &&
             op.fetch("collateral_authorization_ids") == [] }, "P33 exact-confirmation patch scope")
  [handoff, validation].each do |document|
    encoded = JSON.generate(document)
    [EXACT_EVENT_SHA, AUTHORITY.fetch("authorization_receipt").last, artifacts.dig("patch", "sha256"),
     artifacts.dig("author_choices", "sha256"), artifacts.dig("author_adjudication", "sha256"), PLAN_SHA].each do |digest|
      require!(encoded.include?(digest), "P33 re-signed writer artifact omits #{digest}")
    end
  end
  verdict = validation["status"] || validation["verdict"]
  require!(verdict.to_s.start_with?("PASS"), "P33 exact-confirmation writer validation status")
  require!(JSON.generate(validation).include?("NON_AUTHORIZING") || !JSON.generate(validation).include?(OLD_AUTHOR_EVENT_SHA),
           "P33 old author event is not demoted in writer validation")
  [artifacts, patch]
end

def verify_prospective_and_plan!(request)
  require!(PLAN.file? && sha(PLAN) == PLAN_SHA, "bibliography plan drift")
  require!(PROSPECTIVE.file? && sha(PROSPECTIVE) == PROSPECTIVE_SHA, "prospective bibliography contract drift")
  plan = load_json(PLAN)
  prospective = load_json(PROSPECTIVE)
  require!(prospective.fetch("schema_version") ==
           "p33-stage4-prime-round5-correction-bibliography-prospective/1.0" &&
           prospective.fetch("status") == "SOURCE_FINALIZED_PROPOSAL_NOT_APPLIED" &&
           prospective.fetch("paper_id") == "P33", "prospective contract schema/status/identity")
  require!(prospective.fetch("bibliography_base") == {
    "path" => root_relative(BIB), "sha256" => BASE_BIB_SHA, "bytes" => BASE_BIB_BYTES,
    "mutation_state" => "NOT_AUTHORIZED_BY_CURRENT_PREPARATION_SCOPE_AND_NOT_PERFORMED"
  }, "prospective bibliography base")
  entries = prospective.fetch("prospective_entries")
  require!(entries.map { |entry| entry.fetch("key") } == ALLOWED_KEYS &&
           entries.map { |entry| entry.fetch("base_key") } == %w[P33-S03 P33-S16],
           "prospective entry key order")
  require!(prospective.fetch("affected_uses").map { |use| use.fetch("use_id") } == USE_IDS,
           "prospective five-use order")
  require!(prospective.fetch("counts") == {
    "prospective_entries" => 2, "affected_uses" => 5, "base_P33_S03_uses" => 2,
    "base_P33_S16_uses" => 3, "entries_appended" => 0, "uses_rewritten" => 0
  }, "prospective counts")
  require!(prospective.fetch("later_authorization_contract") == {
    "maximum_new_entries" => 2, "allowed_keys" => ALLOWED_KEYS, "append_only" => true,
    "every_affected_use_requires_base_and_correction_binding" => true,
    "claim_boundary_must_remain_unchanged" => true
  }, "prospective later-authorization contract")
  require!(prospective.fetch("boundaries") == {
    "references_bib_modified" => false, "manuscript_modified" => false,
    "scientific_claim_changed" => false, "systematic_retraction_or_conflict_audit_claimed" => false
  }, "prospective boundaries")

  expected_records = entries.map do |entry|
    {"key" => entry.fetch("key"), "base_key" => entry.fetch("base_key"),
     "prospective_bibtex_record" => entry.fetch("prospective_bibtex_record")}
  end
  expected_append = "\n#{expected_records.map { |entry| entry.fetch('prospective_bibtex_record') }.join("\n\n")}\n"
  expected_plan = {
    "schema_version" => "p33-stage4-prime-round6-bibliography-append-plan/1.0",
    "status" => "AUTHORIZED_EXACT_APPEND_PLAN_NOT_APPLIED",
    "paper_id" => "P33",
    "revision_round" => 2,
    "authority" => binding(REQUEST),
    "prospective_contract" => binding(PROSPECTIVE),
    "base" => {"path" => root_relative(BIB), "sha256" => BASE_BIB_SHA, "bytes" => BASE_BIB_BYTES},
    "append_only" => true,
    "allowed_keys" => ALLOWED_KEYS,
    "records" => expected_records,
    "append_text" => expected_append,
    "append_text_sha256" => bytes_sha(expected_append),
    "expected_result_sha256" => EXPECTED_BIB_SHA,
    "expected_result_bytes" => EXPECTED_BIB_BYTES,
    "affected_uses" => prospective.fetch("affected_uses"),
    "counts" => {"entries_to_append" => 2, "uses_to_dual_bind" => 5, "entries_appended_now" => 0},
    "boundaries" => {
      "existing_entry_bytes_may_change" => false, "third_entry_allowed" => false,
      "scientific_claim_strengthening_allowed" => false,
      "systematic_retraction_or_conflict_audit_claimed" => false
    }
  }
  require!(plan == expected_plan, "complete bibliography append plan differs from prospective contract")

  operation = request.fetch("supporting_operations").find do |row|
    row.fetch("operation_id") == "P33-CORRECTION-BIBLIOGRAPHY"
  end
  require!(!operation.nil? && operation.fetch("prospective_contract") == binding(PROSPECTIVE) &&
           operation.fetch("bibliography_path") == root_relative(BIB) &&
           operation.fetch("base_sha256") == BASE_BIB_SHA && operation.fetch("maximum_new_entries") == 2 &&
           operation.fetch("allowed_operations") == [
             "append_exact_verified_entry:P33-S03-CORR",
             "append_exact_verified_entry:P33-S16-CORR",
             "bind_five_affected_uses_to_base_and_correction",
             "create_append_and_binding_receipt"
           ], "scope request bibliography operation")
  [plan, prospective]
end

def parse_blocks(text)
  text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m).to_h
end

def verify_apply_report!(artifacts, patch)
  base = NOTES / "stage4_revision_round1.tex"
  require!(base.file? && REVISED.file? && APPLY_REPORT.file?, "official P33 successor/apply report missing")
  report = load_json(APPLY_REPORT)
  require!(report.fetch("report_format_version") == "1.3" && report.fetch("mode") == "patch" &&
           report.fetch("base_path") == root_relative(base) && report.fetch("output_path") == root_relative(REVISED),
           "P33 apply report format/paths")
  require!(report.fetch("base_draft_hash") == sha(base)[0, 12] &&
           report.fetch("output_draft_hash") == sha(REVISED)[0, 12] &&
           report.fetch("patch_digest") == artifacts.dig("patch", "sha256") &&
           report.fetch("revision_round") == 2 && report.fetch("authorization_context") == "review_roadmap",
           "P33 apply report hashes/authority")
  witness = report.fetch("authorization_witness")
  require!(witness.fetch("status") == "pass" &&
           witness.fetch("roadmap_sha256") == artifacts.dig("revision_roadmap", "sha256") &&
           witness.fetch("author_adjudication_sha256") == artifacts.dig("author_adjudication", "sha256") &&
           witness.fetch("author_decision_digest") == patch.fetch("author_decision_digest") &&
           witness.fetch("claim_surface_manifest_sha256") == artifacts.dig("claim_surface_manifest", "sha256") &&
           witness.fetch("registered_claim_surfaces_checked") == 0 &&
           witness.fetch("unregistered_claim_drift_review_required") == true,
           "P33 apply authorization witness")
  applied = report.fetch("ops_applied")
  require!(applied.length == 37, "P33 apply op count")
  applied.each_with_index do |row, index|
    op = patch.fetch("ops").fetch(index)
    require!(row == {
      "op_index" => index, "op" => "replace_block", "block_id" => op.fetch("block_id"),
      "roadmap_item_ids" => op.fetch("roadmap_item_ids"), "claim_strength_changes" => [],
      "collateral_authorization_ids" => [], "new_block_ids" => []
    }, "P33 apply op #{index} does not exactly replay final patch")
  end
  require!(report.fetch("fresh_block_ids") == [] && report.fetch("pure_move_pairs") == [] &&
           report.dig("structural_flags", "heading_op_indexes") == [] &&
           report.dig("structural_flags", "section_count_delta") == 0 &&
           report.dig("structural_flags", "touched_ratio_exceeded") == false &&
           report.dig("structural_flags", "any") == false,
           "P33 apply structural/fresh-block boundary")
  require!(report.dig("counters", "blocks_touched") == 37 &&
           report.dig("counters", "blocks_preserved_byte_identical") + 37 == report.dig("counters", "blocks_total"),
           "P33 apply counters")
  report
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

def fsync_directory(path)
  File.open(path.dirname.to_s, File::RDONLY) { |handle| handle.fsync }
end

def promote_bibliography_and_receipt!(bibliography_stage, receipt_stage, before_sha)
  require!(!receipt_stage.fetch(:target).exist?, "receipt collision before promotion")
  target = bibliography_stage.fetch(:target)
  backup = target.dirname / ".#{target.basename}.round10-p33-#{Process.pid}-#{SecureRandom.hex(12)}.backup"
  receipt_created = false
  bibliography_installed = false
  committed = false
  begin
    require!(target.file? && sha(target) == before_sha, "late bibliography base drift")
    require!(!backup.exist?, "bibliography backup collision")
    File.link(target, backup)
    require!(!receipt_stage.fetch(:target).exist?, "late receipt collision")
    File.rename(bibliography_stage.fetch(:staged), target)
    bibliography_installed = true
    # Atomic no-clobber receipt creation; EEXIST forces rollback.
    File.link(receipt_stage.fetch(:staged), receipt_stage.fetch(:target))
    receipt_created = true
    File.unlink(receipt_stage.fetch(:staged))
    fsync_directory(target)
    fsync_directory(receipt_stage.fetch(:target))
    yield
    committed = true
  rescue StandardError => error
    rollback_errors = []
    begin
      File.unlink(receipt_stage.fetch(:target)) if receipt_created && receipt_stage.fetch(:target).exist?
    rescue StandardError => rollback_error
      rollback_errors << "remove receipt: #{rollback_error.message}"
    end
    begin
      File.rename(backup, target) if bibliography_installed && backup.exist?
    rescue StandardError => rollback_error
      rollback_errors << "restore bibliography: #{rollback_error.message}"
    end
    begin
      File.unlink(backup) if backup.exist?
    rescue StandardError => rollback_error
      rollback_errors << "cleanup backup: #{rollback_error.message}"
    end
    fsync_directory(target) rescue nil
    suffix = rollback_errors.empty? ? "" : "; ROLLBACK ERRORS: #{rollback_errors.join('; ')}"
    raise "ROUND10_P33_BIB_APPEND_FAIL: promotion failed: #{error.message}#{suffix}"
  ensure
    if committed
      begin
        File.unlink(backup) if backup.exist?
        fsync_directory(target)
      rescue StandardError => cleanup_error
        warn "ROUND10_P33_BIB_APPEND_WARNING: committed backup cleanup failed #{backup}: #{cleanup_error.message}"
      end
    end
    cleanup_stage(bibliography_stage)
    cleanup_stage(receipt_stage)
  end
end

authority = verify_authority!
manifest = verify_final_manifest!(authority)
request = load_json(REQUEST)
require!(request.fetch("schema_version") == "round10-stage4-prime-p33-scope-expansion-authorization-request/1.0" &&
         request.fetch("status") == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION" &&
         request.fetch("paper_id") == "P33" &&
         request.dig("counts", "total_unique_block_operation_pairs") == 37,
         "P33 scope request schema/status/count")
manifest_row, scope = verify_manifest_p33!(manifest, request)
artifacts, patch = verify_resigned_emission!(manifest_row, scope)
plan, prospective = verify_prospective_and_plan!(request)
report = verify_apply_report!(artifacts, patch)

p33_cross_audit = manifest.fetch(:object).fetch("root_cross_audits").map { |row| load_json(ROOT / row.fetch("path")) }
  .flat_map { |audit| audit.fetch("papers") }.find { |row| row.fetch("paper_id") == "P33" }
require!(!p33_cross_audit.nil? && p33_cross_audit.fetch("patch_sha256") == artifacts.dig("patch", "sha256") &&
         p33_cross_audit.fetch("op_count") == 37 && p33_cross_audit.fetch("findings") == [],
         "P33 exact-confirmation cross-audit patch/count/findings")
cross_encoded = JSON.generate(p33_cross_audit)
[PLAN_SHA, PROSPECTIVE_SHA, EXPECTED_BIB_SHA, artifacts.dig("author_choices", "sha256")].each do |digest|
  require!(cross_encoded.include?(digest), "P33 exact-confirmation cross-audit omits #{digest}")
end

require!(!RECEIPT.exist?, "refusing to overwrite bibliography receipt")
require!(BIB.file? && !BIB.symlink? && sha(BIB) == BASE_BIB_SHA && BIB.size == BASE_BIB_BYTES,
         "base bibliography drift")
freeze_p33 = authority.fetch(:freeze).fetch("papers").find { |row| row.fetch("paper_id") == "P33" }
require!(!freeze_p33.nil?, "P33 absent from exact-confirmation freeze")
verify_binding!(freeze_p33.fetch("current_working_bibliography"), "P33 frozen bibliography",
                expected_path: root_relative(BIB), expected_sha: BASE_BIB_SHA)

base_bytes = BIB.binread
ALLOWED_KEYS.each do |key|
  require!(!base_bytes.match?(/@[A-Za-z]+\{#{Regexp.escape(key)},/), "#{key} already exists in base bibliography")
end
expected_bytes = base_bytes + plan.fetch("append_text")
require!(expected_bytes.start_with?(base_bytes) && expected_bytes.bytesize == EXPECTED_BIB_BYTES &&
         bytes_sha(expected_bytes) == EXPECTED_BIB_SHA,
         "computed append-only bibliography result")
keys = expected_bytes.scan(/@[A-Za-z]+\{([^,]+),/).flatten
ALLOWED_KEYS.each { |key| require!(keys.count(key) == 1, "#{key}: expected exactly one prospective entry") }
require!((keys - base_bytes.scan(/@[A-Za-z]+\{([^,]+),/).flatten) == ALLOWED_KEYS,
         "bibliography append introduced a key outside the two-key contract")

blocks = parse_blocks(REVISED.binread.force_encoding("UTF-8"))
uses = plan.fetch("affected_uses")
require!(uses == prospective.fetch("affected_uses") && uses.map { |row| row.fetch("use_id") } == USE_IDS,
         "five-use plan/prospective order")
uses.each do |row|
  text = blocks.fetch(row.fetch("block_id"))
  require!(text.include?("use_id=#{row.fetch('use_id')}"), "#{row.fetch('use_id')}: annotation missing")
  citations = text.scan(/\\cite(?:p|t)?\{([^}]*)\}/).flatten.flat_map { |group| group.split(",").map(&:strip) }
  require!(citations.include?(row.fetch("base_key")) && citations.include?(row.fetch("correction_key")),
           "#{row.fetch('use_id')}: exact dual citation missing")
end

timestamp = Time.now.utc.iso8601
authority_rows = AUTHORITY.transform_values { |relative, _| binding(ROOT / relative) }
authority_rows.fetch("author_event")["exact_text"] = "确认\n"
receipt = {
  "schema_version" => "round10-p33-stage4-prime-round6-correction-bibliography-receipt/1.0",
  "paper_id" => "P33",
  "generated_at_utc" => timestamp,
  "status" => "PASS_EXACT_TWO_ENTRY_APPEND_AND_FIVE_USE_BINDING",
  "authority" => {"path" => root_relative(REQUEST), "sha256" => REQUEST_SHA},
  "exact_confirmation_authority" => authority_rows,
  "final_emission_manifest" => {
    "path" => root_relative(FINAL_MANIFEST), "sha256" => manifest.fetch(:sha256), "bytes" => manifest.fetch(:bytes)
  },
  "plan" => {"path" => PLAN.relative_path_from(PAPER_ROOT).to_s, "sha256" => PLAN_SHA, "bytes" => PLAN.size},
  "prospective_contract" => {
    "path" => PROSPECTIVE.relative_path_from(PAPER_ROOT).to_s,
    "sha256" => PROSPECTIVE_SHA,
    "bytes" => PROSPECTIVE.size
  },
  "bibliography" => {
    "path" => BIB.relative_path_from(PAPER_ROOT).to_s,
    "before_sha256" => BASE_BIB_SHA,
    "after_sha256" => EXPECTED_BIB_SHA,
    "before_bytes" => BASE_BIB_BYTES,
    "after_bytes" => EXPECTED_BIB_BYTES,
    "entries_appended" => ALLOWED_KEYS
  },
  "manuscript" => {
    "path" => REVISED.relative_path_from(PAPER_ROOT).to_s,
    "sha256" => sha(REVISED),
    "bytes" => REVISED.size,
    "patch_path" => artifacts.dig("patch", "path"),
    "patch_sha256" => artifacts.dig("patch", "sha256"),
    "apply_report_path" => root_relative(APPLY_REPORT),
    "apply_report_sha256" => sha(APPLY_REPORT),
    "apply_report_bytes" => APPLY_REPORT.size,
    "applied_operation_count" => report.fetch("ops_applied").length,
    "dual_bound_uses" => uses
  },
  "cross_audit" => {
    "path" => EXACT_CROSS_AUDIT_PATHS.last,
    "sha256" => sha(ROOT / EXACT_CROSS_AUDIT_PATHS.last)
  },
  "counts" => {"entries_appended" => 2, "affected_uses_dual_bound" => 5, "existing_entries_overwritten" => 0},
  "boundaries" => {
    "third_entry_added" => false,
    "scientific_claim_strengthened" => false,
    "systematic_retraction_or_conflict_audit_claimed" => false,
    "canonical_manuscript_or_pdf_changed" => false,
    "fresh_stage4_5_or_re_review_run" => false
  }
}
receipt_bytes = json_bytes(receipt)
bibliography_stage = stage_bytes(BIB, expected_bytes, mode: BIB.stat.mode & 0o777)
receipt_stage = stage_bytes(RECEIPT, receipt_bytes)
promote_bibliography_and_receipt!(bibliography_stage, receipt_stage, BASE_BIB_SHA) do
  require!(sha(BIB) == EXPECTED_BIB_SHA && BIB.size == EXPECTED_BIB_BYTES,
           "promoted bibliography mismatch")
  require!(sha(RECEIPT) == bytes_sha(receipt_bytes) && RECEIPT.size == receipt_bytes.bytesize,
           "promoted bibliography receipt mismatch")
  promoted_keys = BIB.binread.scan(/@[A-Za-z]+\{([^,]+),/).flatten
  ALLOWED_KEYS.each { |key| require!(promoted_keys.count(key) == 1, "#{key}: promoted entry count") }
end

puts "P33 bibliography append PASS: 2 exact entries, 5 dual-bound uses, #{EXPECTED_BIB_BYTES} bytes; " \
     "bibliography SHA-256 #{EXPECTED_BIB_SHA}"
