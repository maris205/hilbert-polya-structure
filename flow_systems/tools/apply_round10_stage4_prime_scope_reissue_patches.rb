#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
ARS_ROOT = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars").freeze
ROADMAP_CLI = ARS_ROOT / "scripts/revision_roadmap.py"
APPLY_CLI = ARS_ROOT / "scripts/ars_apply_revision_patch.py"

EXACT_AUTHORITY_PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
EXACT_AUTHOR_EVENT = "#{EXACT_AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt"
EXACT_AUTHORIZATION_RECORD = "#{EXACT_AUTHORITY_PREFIX}_AUTHORIZATION_RECORD.md"
EXACT_INPUT_FREEZE = "#{EXACT_AUTHORITY_PREFIX}_INPUT_FREEZE.json"
EXACT_AUTHORIZATION_RECEIPT = "#{EXACT_AUTHORITY_PREFIX}_AUTHORIZATION_RECEIPT.json"
EXACT_AUTHORITY_AUDIT = "#{EXACT_AUTHORITY_PREFIX}_AUTHORITY_AUDIT.json"
CONTROLLING_CHECKPOINT = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_MANDATORY_CHECKPOINT.md"
FINAL_EMISSION_MANIFEST = "#{EXACT_AUTHORITY_PREFIX}_FINAL_EMISSION_MANIFEST.json"
FINAL_EMISSION_SCHEMA = "round10-stage4-prime-scope-reissue-exact-confirmation-final-emission-manifest/1.0"
FINAL_EMISSION_STATUS = "PASS_EXACT_CONFIRMATION_FINAL_EMISSION_READY_FOR_DETERMINISTIC_APPLY"
EXACT_FREEZE_STATUS = "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION"
EXACT_RECEIPT_STATUS = "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION"
EXACT_AUDIT_STATUS = "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY"
NON_AUTHORIZING_PREPARATION_ROLE = "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"

# This is intentionally fail-closed until the final exact-confirmation emission
# manifest has been produced and its independently audited SHA-256 is supplied.
FINAL_EMISSION_MANIFEST_SHA256 = "db98aa8ace700196044b7bb1903251a90782e709d65f6c0712da041c36421091"

TRACK_PATHS = {
  "P29_P32" => "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json",
  "P30_P31" => "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json",
  "P33" => "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json"
}.freeze

EXACT_CROSS_AUDIT_PATHS = %w[
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P29_P32.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P33.json
].freeze

CONFIGS = {
  "P29" => {
    slug: "29-bianchi-ideal-owner-refinement",
    base: "stage4_prime_revision_round2.tex",
    manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    author_choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    output: "stage4_prime_revision_round3.tex",
    expected_ops: 31,
    request_track: "P29_P32"
  },
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    base: "stage4_prime_revision_round2.tex",
    manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    author_choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    output: "stage4_prime_revision_round3.tex",
    expected_ops: 34,
    request_track: "P30_P31"
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    base: "stage4_prime_revision_round2.tex",
    manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    author_choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    output: "stage4_prime_revision_round3.tex",
    expected_ops: 13,
    request_track: "P30_P31"
  },
  "P32" => {
    slug: "32-homology-cover-renormalization-uniformity",
    base: "stage4_prime_revision_round2.tex",
    manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json",
    claims: "stage4_prime_correction_round3_claim_surface_manifest.json",
    author_choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    output: "stage4_prime_revision_round3.tex",
    expected_ops: 15,
    request_track: "P29_P32"
  },
  "P33" => {
    slug: "33-bolza-control-matched-census",
    base: "stage4_revision_round1.tex",
    manifest: "stage4_prime_round5_base.block-manifest.json",
    roadmap: "stage4_prime_round6_revision_roadmap.json",
    claims: "stage4_prime_round6_claim_surface_manifest.json",
    author_choices: "stage4_prime_round6_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_round6_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round6_exact_confirmation.json",
    handoff: "stage4_prime_round6_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_round6_exact_confirmation_writer_validation_receipt.json",
    output: "stage4_prime_revision_round2.tex",
    expected_ops: 37,
    request_track: "P33"
  }
}.freeze

def require!(condition, message)
  raise "ROUND10_SCOPE_REISSUE_APPLY_FAIL: #{message}" unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(path.read)
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

def author_decision_digest(adjudication)
  projection = {
    "author_events" => adjudication.fetch("author_events"),
    "display_order" => adjudication.fetch("display_order"),
    "author_adjudications" => adjudication.fetch("author_adjudications"),
    "collateral_authorizations" => adjudication.fetch("collateral_authorizations")
  }
  Digest::SHA256.hexdigest(JSON.generate(deep_sort(projection)))
end

def parse_blocks(text)
  text.scan(/<!--block:(B\d{4})-->\n(.*?)(?=\n<!--block:B\d{4}-->|\z)/m).to_h
end

def normalized_block_text(text)
  lines = text.gsub("\r\n", "\n").split("\n", -1)
  lines.shift while !lines.empty? && lines.first.strip.empty?
  lines.pop while !lines.empty? && lines.last.strip.empty?
  lines.join("\n")
end

def heading_signature(text)
  text.scan(/\\(?:sub)*section\*?\s*\{[^}]*\}/)
end

def run!(*command)
  stdout, stderr, status = Open3.capture3(*command.map(&:to_s), chdir: ROOT.to_s)
  $stdout.write(stdout)
  $stderr.write(stderr)
  require!(status.success?, "command failed #{status.exitstatus}: #{command.join(' ')}")
end

def capture_created_artifact!(path, label)
  stat = path.lstat
  require!(stat.file?, "#{label} is not a regular file created by this apply")
  {
    path: path,
    device: stat.dev,
    inode: stat.ino,
    sha256: sha(path)
  }
rescue Errno::ENOENT
  require!(false, "#{label} is absent after apply")
end

def rollback_created_artifacts(created)
  # Exception rollback only: this cannot recover from SIGKILL/process death,
  # and the lstat/hash/unlink sequence is not a kernel-level compare-and-delete.
  # Official execution therefore requires one process and no concurrent writer
  # in any output directory.
  errors = []
  created.reverse_each do |row|
    path = row.fetch(:path)
    begin
      stat = path.lstat
      matches = stat.file? && stat.dev == row.fetch(:device) && stat.ino == row.fetch(:inode) &&
        sha(path) == row.fetch(:sha256)
      unless matches
        errors << "preserved nonmatching path #{path.relative_path_from(ROOT)}"
        next
      end
      File.unlink(path)
    rescue Errno::ENOENT
      errors << "created path disappeared before rollback #{path.relative_path_from(ROOT)}"
    rescue StandardError => error
      errors << "rollback #{path.relative_path_from(ROOT)}: #{error.message}"
    end
  end
  errors
end

def verify_artifact!(row, label, expected_path: nil, require_bytes: false)
  require!(row.is_a?(Hash), "#{label} binding is not an object")
  relative = row.fetch("path")
  require!(relative.is_a?(String) && !relative.empty?, "#{label} path is not a nonempty string")
  relative_path = Pathname.new(relative)
  require!(!relative_path.absolute?, "#{label} path is absolute: #{relative}")
  require!(relative_path.cleanpath.to_s == relative && !relative.start_with?("../"), "#{label} path escapes root: #{relative}")
  require!(relative == expected_path, "#{label} path #{relative} != #{expected_path}") if expected_path
  path = ROOT / relative
  require!(path.file?, "#{label} missing #{relative}")
  expected_sha = row.fetch("sha256")
  require!(expected_sha.match?(/\A[0-9a-f]{64}\z/), "#{label} SHA-256 is not 64 lowercase hex")
  require!(sha(path) == expected_sha, "#{label} SHA-256 drift #{relative}")
  require!(row.key?("bytes"), "#{label} byte count absent #{relative}") if require_bytes
  require!(path.size == row.fetch("bytes"), "#{label} byte-count drift #{relative}") if row.key?("bytes")
  path
end

def verify_binding_rows!(rows, label, expected_count: nil)
  require!(rows.is_a?(Array), "#{label} bindings are not an array")
  require!(rows.length == expected_count, "#{label} count #{rows.length} != #{expected_count}") if expected_count
  rows.each { |row| verify_artifact!(row, label) }
end

def require_same_binding!(actual, expected, label)
  %w[path sha256 bytes].each do |key|
    require!(actual.fetch(key) == expected.fetch(key), "#{label} #{key} does not match exact authority")
  end
end

def verify_internal_exact_authority!(document, authority, label)
  internal = document.fetch("authority")
  %w[author_event authorization_record input_freeze authorization_receipt authority_audit].each do |key|
    require_same_binding!(internal.fetch(key), authority.fetch(key), "#{label}/authority/#{key}")
  end
end

def verify_exact_author_events!(document, event_binding, label)
  events = document.fetch("author_events")
  require!(events.is_a?(Array) && events.length == 1, "#{label} must contain one exact author event")
  event = events.first
  require!(event.fetch("actor_role") == "author", "#{label} event actor is not author")
  require!(event.fetch("source") == "explicit_session_user_message", "#{label} event source is not explicit session input")
  require!(event.fetch("input_sha256") == event_binding.fetch("sha256"), "#{label} does not bind exact 确认 event")
end

def load_exact_authority!
  receipt_path = ROOT / EXACT_AUTHORIZATION_RECEIPT
  require!(receipt_path.file?, "missing exact-confirmation receipt #{EXACT_AUTHORIZATION_RECEIPT}")
  receipt = load_json(receipt_path)
  require!(receipt.fetch("status") == EXACT_RECEIPT_STATUS, "exact-confirmation receipt status")
  require!(receipt.fetch("prepared_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
           "old prepared evidence is not explicitly non-authorizing")

  event_path = verify_artifact!(receipt.fetch("author_event"), "exact author event", expected_path: EXACT_AUTHOR_EVENT, require_bytes: true)
  require!(event_path.binread == "确认\n".b, "exact author event bytes are not 确认\\n")
  require!(receipt.dig("author_event", "exact_text") == "确认\n", "exact author event receipt text mismatch")
  verify_artifact!(receipt.fetch("authorization_record"), "exact authorization record",
                   expected_path: EXACT_AUTHORIZATION_RECORD, require_bytes: true)
  freeze_path = verify_artifact!(receipt.fetch("input_freeze"), "exact input freeze",
                                 expected_path: EXACT_INPUT_FREEZE, require_bytes: true)
  verify_artifact!(receipt.fetch("controlling_checkpoint"), "controlling checkpoint",
                   expected_path: CONTROLLING_CHECKPOINT, require_bytes: true)

  tracks = receipt.fetch("tracks")
  TRACK_PATHS.each do |track, relative|
    verify_artifact!(tracks.fetch(track), "#{track} request", expected_path: relative, require_bytes: true)
  end
  require!(receipt.dig("aggregate", "papers") == 5, "exact receipt paper count")
  require!(receipt.dig("aggregate", "unique_replace_block_pairs") == 130, "exact receipt operation count")
  require!(receipt.dig("aggregate", "matrix_regenerations") == 2, "exact receipt matrix count")
  require!(receipt.dig("aggregate", "p33_bibliography_appends") == 2, "exact receipt P33 bibliography count")

  audit_path = ROOT / EXACT_AUTHORITY_AUDIT
  require!(audit_path.file?, "missing exact-confirmation authority audit #{EXACT_AUTHORITY_AUDIT}")
  audit = load_json(audit_path)
  require!(audit.fetch("status") == EXACT_AUDIT_STATUS, "exact-confirmation authority audit status")
  checks = audit.fetch("checks")
  require!(checks.all? { |row| row.fetch("status") == "PASS" }, "exact-confirmation authority audit has a non-PASS check")
  require!(audit.fetch("checks_failed", 0) == 0, "exact-confirmation authority audit failure count")
  [EXACT_AUTHOR_EVENT, EXACT_AUTHORIZATION_RECORD, EXACT_INPUT_FREEZE, EXACT_AUTHORIZATION_RECEIPT,
   CONTROLLING_CHECKPOINT, *TRACK_PATHS.values].each do |relative|
    binding = checks.find { |row| row.fetch("check_id") == "binding:#{relative}" }
    require!(binding, "authority audit missing binding #{relative}")
    require!(binding.dig("detail", "actual") == sha(ROOT / relative), "authority audit stale binding #{relative}")
    require!(binding.dig("detail", "expected") == sha(ROOT / relative), "authority audit expected binding mismatch #{relative}")
  end

  freeze = load_json(freeze_path)
  require!(freeze.fetch("status") == EXACT_FREEZE_STATUS, "exact-confirmation freeze status")
  require!(freeze.fetch("prepared_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
           "freeze does not mark old prepared evidence non-authorizing")
  authority = {
    "author_event" => receipt.fetch("author_event"),
    "authorization_record" => receipt.fetch("authorization_record"),
    "input_freeze" => receipt.fetch("input_freeze"),
    "authorization_receipt" => {
      "path" => EXACT_AUTHORIZATION_RECEIPT,
      "sha256" => sha(receipt_path),
      "bytes" => receipt_path.size
    },
    "authority_audit" => {
      "path" => EXACT_AUTHORITY_AUDIT,
      "sha256" => sha(audit_path),
      "bytes" => audit_path.size
    }
  }
  [receipt, freeze, authority]
end

def replay_complete_freeze!(freeze, phase)
  require!(freeze.fetch("status") == EXACT_FREEZE_STATUS, "#{phase}: freeze status")
  require!(freeze.fetch("papers").map { |paper| paper.fetch("paper_id") } == CONFIGS.keys, "#{phase}: freeze paper order")
  freeze.fetch("papers").each do |paper|
    paper_id = paper.fetch("paper_id")
    config = CONFIGS.fetch(paper_id)
    paper_prefix = "papers/#{config.fetch(:slug)}/"
    require!(paper.fetch("paper_slug") == config.fetch(:slug), "#{phase}/#{paper_id} freeze slug")
    require!(paper.fetch("authorized_unique_replace_block_pairs") == config.fetch(:expected_ops), "#{phase}/#{paper_id} frozen operation count")
    require!(paper.dig("current_working_draft", "path") == "#{paper_prefix}notes/#{config.fetch(:base)}", "#{phase}/#{paper_id} frozen draft path")
    require!(paper.dig("block_manifest", "path") == "#{paper_prefix}notes/#{config.fetch(:manifest)}", "#{phase}/#{paper_id} frozen manifest path")
    has_matrix_exception = paper.key?("authorized_in_place_matrix_regeneration")
    require!(has_matrix_exception == %w[P30 P31].include?(paper_id), "#{phase}/#{paper_id} matrix exception set")
    rows = [
      paper.fetch("current_working_draft"),
      paper.fetch("current_working_bibliography"),
      paper.fetch("block_manifest"),
      *paper.fetch("canonical_files"),
      *paper.fetch("science_files"),
      paper.fetch("initial_system_source"),
      paper.fetch("route_crosswalk")
    ]
    rows << paper.fetch("authorized_in_place_matrix_regeneration") if paper.key?("authorized_in_place_matrix_regeneration")
    require!(rows.all? { |row| row.fetch("path").start_with?(paper_prefix) }, "#{phase}/#{paper_id} cross-paper freeze path")
    verify_binding_rows!(rows, "#{phase}/#{paper_id} freeze")
  end
  verify_binding_rows!(freeze.dig("superseded_freeze_replay", "bindings"), "#{phase}/94-row prior freeze replay", expected_count: 94)
  verify_binding_rows!(freeze.dig("expanded_request_referenced_artifact_replay", "bindings"), "#{phase}/85-row request replay", expected_count: 85)
  verify_binding_rows!(freeze.fetch("route_evaluators"), "#{phase}/route evaluators", expected_count: 2)
end

def verify_emission_evidence!(receipt, authority, targets_by_paper)
  require!(FINAL_EMISSION_MANIFEST_SHA256.is_a?(String) &&
           FINAL_EMISSION_MANIFEST_SHA256.match?(/\A[0-9a-f]{64}\z/),
           "final exact-confirmation emission manifest SHA-256 pin has not been supplied")
  manifest_path = ROOT / FINAL_EMISSION_MANIFEST
  require!(manifest_path.file?, "missing final exact-confirmation emission manifest #{FINAL_EMISSION_MANIFEST}")
  require!(sha(manifest_path) == FINAL_EMISSION_MANIFEST_SHA256, "final exact-confirmation emission manifest SHA-256 drift")
  final_manifest = load_json(manifest_path)
  require!(final_manifest.fetch("schema_version") == FINAL_EMISSION_SCHEMA, "final emission manifest schema")
  require!(final_manifest.fetch("status") == FINAL_EMISSION_STATUS, "final emission manifest status")
  require!(final_manifest.fetch("preparation_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
           "final manifest does not mark old prepared evidence non-authorizing")
  verify_internal_exact_authority!(final_manifest, authority, "final emission manifest")
  require!(final_manifest.dig("authority", "author_event", "exact_text") == "确认\n",
           "final manifest exact author text mismatch")
  require!(final_manifest.dig("aggregate", "papers") == 5, "final manifest paper count")
  require!(final_manifest.dig("aggregate", "unique_replace_block_pairs") == 130,
           "final manifest operation count")

  papers = final_manifest.fetch("papers")
  require!(papers.is_a?(Array), "final manifest papers are not an array")
  require!(papers.map { |paper| paper.fetch("paper_id") } == CONFIGS.keys, "final manifest paper order")
  paper_emissions = {}
  required_artifacts = %w[
    revision_roadmap author_choices author_adjudication claim_surface_manifest
    patch writer_handoff writer_validation
  ].freeze

  papers.each do |paper|
    paper_id = paper.fetch("paper_id")
    config = CONFIGS.fetch(paper_id)
    request_scope = targets_by_paper.fetch(paper_id)
    require!(paper.fetch("paper_slug") == config.fetch(:slug), "#{paper_id} final manifest slug")
    require!(paper.fetch("request_track") == config.fetch(:request_track), "#{paper_id} final manifest request track")
    require!(paper.fetch("authorized_replace_block_pairs") == config.fetch(:expected_ops),
             "#{paper_id} final manifest operation count")
    request_binding = paper.fetch("request")
    require_same_binding!(request_binding, receipt.dig("tracks", config.fetch(:request_track)),
                          "#{paper_id} final manifest request")
    verify_artifact!(request_binding, "#{paper_id} final manifest request",
                     expected_path: TRACK_PATHS.fetch(config.fetch(:request_track)), require_bytes: true)

    trace = paper.fetch("source_traceability")
    item_ids = trace.fetch("item_ids")
    require!(trace.fetch("mode") == "source_traceability", "#{paper_id} source_traceability mode")
    require!(item_ids == request_scope.fetch("item_order"), "#{paper_id} source_traceability item order")
    require!(trace.fetch("count") == item_ids.length, "#{paper_id} source_traceability count")
    require!(trace.fetch("canonicalization") == "JSON.generate(item_ids) UTF-8",
             "#{paper_id} source_traceability canonicalization")
    canonical_trace = JSON.generate(item_ids).encode(Encoding::UTF_8)
    require!(trace.fetch("sha256") == Digest::SHA256.hexdigest(canonical_trace),
             "#{paper_id} source_traceability digest")

    base_path = ROOT / "papers" / config.fetch(:slug) / "notes" / config.fetch(:base)
    base_blocks = parse_blocks(base_path.read)
    expected_full_hash_order = if paper_id == "P33"
                                 base_blocks.keys.select { |block_id| request_scope.fetch("blocks").key?(block_id) }
                               else
                                 request_scope.fetch("block_order")
                               end
    full_old_hashes = paper.fetch("full_old_hashes")
    require!(full_old_hashes.is_a?(Array) && full_old_hashes.length == config.fetch(:expected_ops),
             "#{paper_id} final manifest full old-hash count")
    require!(full_old_hashes.map { |row| row.fetch("block_id") } == expected_full_hash_order,
             "#{paper_id} final manifest full old-hash order")
    full_old_hashes.each do |row|
      block_id = row.fetch("block_id")
      expected_full = Digest::SHA256.hexdigest(normalized_block_text(base_blocks.fetch(block_id)))
      require!(row.fetch("sha256").match?(/\A[0-9a-f]{64}\z/),
               "#{paper_id}/#{block_id} final manifest old hash is not 64 lowercase hex")
      require!(row.fetch("sha256") == expected_full, "#{paper_id}/#{block_id} final manifest full old-hash mismatch")
      request_scope.fetch("blocks").fetch(block_id)["authorized_full_old_hash"] = expected_full
    end

    rows = paper.fetch("artifacts")
    require!(rows.is_a?(Hash), "#{paper_id} final artifacts are not an object")
    require!((required_artifacts - rows.keys).empty?, "#{paper_id} final manifest missing required artifacts")
    notes_prefix = "papers/#{config.fetch(:slug)}/notes/"
    expected_paths = {
      "revision_roadmap" => "#{notes_prefix}#{config.fetch(:roadmap)}",
      "author_choices" => "#{notes_prefix}#{config.fetch(:author_choices)}",
      "author_adjudication" => "#{notes_prefix}#{config.fetch(:adjudication)}",
      "claim_surface_manifest" => "#{notes_prefix}#{config.fetch(:claims)}",
      "patch" => "#{notes_prefix}#{config.fetch(:patch)}",
      "writer_handoff" => "#{notes_prefix}#{config.fetch(:handoff)}",
      "writer_validation" => "#{notes_prefix}#{config.fetch(:writer_validation)}"
    }
    artifact_paths = expected_paths.to_h do |key, relative|
      [key, verify_artifact!(rows.fetch(key), "#{paper_id}/#{key}", expected_path: relative, require_bytes: true)]
    end
    paper.fetch("supporting_artifacts", {}).each do |key, row|
      verify_artifact!(row, "#{paper_id}/supporting_artifacts/#{key}", require_bytes: true)
    end

    choices = load_json(artifact_paths.fetch("author_choices"))
    adjudication = load_json(artifact_paths.fetch("author_adjudication"))
    patch = load_json(artifact_paths.fetch("patch"))
    handoff = load_json(artifact_paths.fetch("writer_handoff"))
    validation = load_json(artifact_paths.fetch("writer_validation"))
    verify_exact_author_events!(choices, authority.fetch("author_event"), "#{paper_id} exact author choices")
    verify_exact_author_events!(adjudication, authority.fetch("author_event"), "#{paper_id} exact adjudication")
    require!(choices.fetch("author_events") == adjudication.fetch("author_events"),
             "#{paper_id} choices/adjudication author-event divergence")
    require!(choices.fetch("display_order") == adjudication.fetch("display_order"),
             "#{paper_id} choices/adjudication display-order divergence")
    require!(choices.fetch("author_adjudications") == adjudication.fetch("author_adjudications"),
             "#{paper_id} choices/adjudication decision divergence")
    require!(choices.fetch("collateral_authorizations") == adjudication.fetch("collateral_authorizations"),
             "#{paper_id} choices/adjudication collateral divergence")
    require!(patch.fetch("roadmap_sha256") == rows.dig("revision_roadmap", "sha256"),
             "#{paper_id} final patch/roadmap manifest binding")
    require!(patch.fetch("author_adjudication_sha256") == rows.dig("author_adjudication", "sha256"),
             "#{paper_id} final patch/adjudication manifest binding")
    require!(patch.fetch("claim_surface_manifest_sha256") == rows.dig("claim_surface_manifest", "sha256"),
             "#{paper_id} final patch/claim manifest binding")
    verify_internal_exact_authority!(handoff, authority, "#{paper_id} writer handoff")
    verify_internal_exact_authority!(validation, authority, "#{paper_id} writer validation")
    [handoff, validation].each do |document|
      serialized = JSON.generate(document)
      %w[patch author_choices author_adjudication].each do |key|
        require!(serialized.include?(rows.dig(key, "sha256")), "#{paper_id} writer evidence does not bind #{key}")
      end
    end
    validation_verdict = validation["status"] || validation["verdict"]
    require!(validation_verdict.to_s.start_with?("PASS"), "#{paper_id} writer validation status")
    handoff_status = handoff["status"] || handoff["handoff_status"]
    require!(handoff_status.to_s.match?(/EMITTED|READY/), "#{paper_id} writer handoff status")

    paper_emissions[paper_id] = {
      "patch_sha256" => rows.dig("patch", "sha256"),
      "source_traceability_sha256" => trace.fetch("sha256")
    }
  end

  audit_rows = final_manifest.fetch("root_cross_audits")
  require!(audit_rows.is_a?(Array) && audit_rows.length == EXACT_CROSS_AUDIT_PATHS.length,
           "final manifest exact cross-audit count")
  require!(audit_rows.map { |row| row.fetch("path") } == EXACT_CROSS_AUDIT_PATHS,
           "final manifest exact cross-audit order/path")
  audited_papers = []
  audit_rows.each do |row|
    audit_path = verify_artifact!(row, "exact-confirmation root cross-audit", require_bytes: true)
    audit = load_json(audit_path)
    require!(audit.fetch("status").start_with?("PASS"), "exact-confirmation cross-audit status #{row.fetch('path')}")
    verify_internal_exact_authority!(audit, authority, "exact-confirmation cross-audit #{row.fetch('path')}")
    audit.fetch("papers").each do |paper|
      paper_id = paper.fetch("paper_id")
      require!(paper_emissions.key?(paper_id), "cross-audit has unknown paper #{paper_id}")
      require!(!audited_papers.include?(paper_id), "duplicate exact-confirmation cross-audit paper #{paper_id}")
      require!(paper.fetch("patch_sha256") == paper_emissions.dig(paper_id, "patch_sha256"),
               "#{paper_id} exact-confirmation cross-audit patch binding")
      require!(paper.fetch("source_traceability_sha256") == paper_emissions.dig(paper_id, "source_traceability_sha256"),
               "#{paper_id} exact-confirmation cross-audit source_traceability binding")
      if paper_id == "P33"
        require!(paper.dig("checks", "physical_block_order") == "PASS",
                 "P33 exact-confirmation cross-audit physical block order")
        require!(paper.dig("checks", "all_required_checks_passed") == true,
                 "P33 exact-confirmation cross-audit required checks")
      end
      audited_papers << paper_id
    end
  end
  require!(audited_papers.sort == CONFIGS.keys.sort, "exact-confirmation cross-audits do not cover each paper once")
end

def request_targets
  p29_p32 = load_json(ROOT / TRACK_PATHS.fetch("P29_P32"))
  p30_p31 = load_json(ROOT / TRACK_PATHS.fetch("P30_P31"))
  p33 = load_json(ROOT / TRACK_PATHS.fetch("P33"))
  out = Hash.new do |hash, key|
    hash[key] = {"item_order" => [], "block_order" => [], "blocks" => {}}
  end
  roadmap_id = ->(source_id) { source_id.start_with?("REV-") ? source_id : "REV-#{source_id}" }
  add = lambda do |paper_id, item_id, target|
    paper = out[paper_id]
    paper.fetch("item_order") << item_id unless paper.fetch("item_order").include?(item_id)
    block_id = target.fetch("block_id")
    unless paper.fetch("blocks").key?(block_id)
      paper.fetch("block_order") << block_id
      paper.fetch("blocks")[block_id] = {"item_ids" => [], "expected_old_hash" => target.fetch("expected_old_hash")}
    end
    row = paper.fetch("blocks").fetch(block_id)
    require!(row.fetch("expected_old_hash") == target.fetch("expected_old_hash"), "#{paper_id}/#{block_id} conflicting request old hashes")
    require!(target.fetch("allowed_operations") == ["replace_block"], "#{paper_id}/#{block_id} request operation is not exact replace_block")
    row.fetch("item_ids") << item_id unless row.fetch("item_ids").include?(item_id)
  end
  p29_p32.fetch("papers").each do |paper|
    paper.fetch("issues").each do |issue|
      item_id = roadmap_id.call(issue.fetch("issue_id"))
      issue.fetch("proposed_targets").each { |target| add.call(paper.fetch("paper_id"), item_id, target) }
    end
  end
  p30_p31.fetch("papers").each do |paper|
    paper.fetch("all_requested_targets").each do |target|
      add.call(paper.fetch("paper_id"), roadmap_id.call(target.fetch("issue_id")), target)
    end
  end
  p33.dig("carried_forward_exact_request", "items").each do |item|
    item.fetch("proposed_targets").each { |target| add.call("P33", item.fetch("item_id"), target) }
  end
  p33.fetch("new_issue_actions").each do |action|
    action.fetch("proposed_targets").each { |target| add.call("P33", action.fetch("action_id"), target) }
  end
  out
end

preflight_only = ARGV.delete("--preflight-only")
require!(ARGV.empty?, "unknown arguments: #{ARGV.join(' ')}")
receipt, freeze, authority = load_exact_authority!
replay_complete_freeze!(freeze, "pre-apply")
targets_by_paper = request_targets
require!(targets_by_paper.sum { |_, paper| paper.fetch("blocks").length } == 130, "request target union is not 130")
verify_emission_evidence!(receipt, authority, targets_by_paper)
preflight = {}

CONFIGS.each do |paper_id, config|
  paper_root = ROOT / "papers" / config.fetch(:slug)
  notes = paper_root / "notes"
  paths = %i[base manifest roadmap claims adjudication patch].to_h { |key| [key, notes / config.fetch(key)] }
  paths.each { |key, path| require!(path.file?, "#{paper_id} missing #{key}: #{path}") }
  output = notes / config.fetch(:output)
  report = Pathname.new(output.to_s + ".apply-report.json")
  require!(!output.exist? && !output.symlink?, "#{paper_id} refusing to overwrite output #{output}")
  require!(!report.exist? && !report.symlink?, "#{paper_id} refusing to overwrite report #{report}")

  manifest = load_json(paths.fetch(:manifest))
  roadmap = load_json(paths.fetch(:roadmap))
  claims = load_json(paths.fetch(:claims))
  adjudication = load_json(paths.fetch(:adjudication))
  patch = load_json(paths.fetch(:patch))
  base_blocks = parse_blocks(paths.fetch(:base).read)
  manifest_blocks = manifest.fetch("blocks").to_h { |row| [row.fetch("block_id"), row.fetch("old_hash")] }
  request_scope = targets_by_paper.fetch(paper_id)
  expected_targets = request_scope.fetch("blocks")

  require!(manifest.fetch("base_draft_hash") == sha(paths.fetch(:base))[0, 12], "#{paper_id} manifest/base mismatch")
  require!(roadmap.fetch("base_draft_sha256") == sha(paths.fetch(:base)), "#{paper_id} roadmap/base mismatch")
  require!(roadmap.fetch("block_manifest_sha256") == sha(paths.fetch(:manifest)), "#{paper_id} roadmap/manifest mismatch")
  require!(roadmap.fetch("items").map { |item| item.fetch("id") } == request_scope.fetch("item_order"), "#{paper_id} roadmap source_traceability order mismatch")
  require!(adjudication.dig("display_order", "mode") == "source_traceability", "#{paper_id} adjudication display mode")
  require!(adjudication.dig("display_order", "item_ids") == request_scope.fetch("item_order"), "#{paper_id} adjudication source_traceability order mismatch")
  require!(claims.fetch("surfaces") == [], "#{paper_id} has registered claim surfaces but no claim authority")
  require!(patch.fetch("patch_format_version") == "1.1", "#{paper_id} patch is not 1.1")
  require!(patch.fetch("authorization_context") == "review_roadmap", "#{paper_id} wrong patch authority context")
  require!(patch.fetch("emitted_by") == "draft_writer_agent", "#{paper_id} wrong patch emitter")
  require!(patch.fetch("revision_round") == roadmap.fetch("revision_round"), "#{paper_id} round mismatch")
  require!(patch.fetch("base_draft_hash") == manifest.fetch("base_draft_hash"), "#{paper_id} patch/base mismatch")
  require!(patch.fetch("roadmap_sha256") == sha(paths.fetch(:roadmap)), "#{paper_id} patch/roadmap mismatch")
  require!(patch.fetch("author_adjudication_sha256") == sha(paths.fetch(:adjudication)), "#{paper_id} patch/adjudication mismatch")
  require!(patch.fetch("claim_surface_manifest_sha256") == sha(paths.fetch(:claims)), "#{paper_id} patch/claims mismatch")
  require!(patch.fetch("author_decision_digest") == author_decision_digest(adjudication), "#{paper_id} author decision digest mismatch")
  require!(adjudication.fetch("author_adjudications").all? { |row| row.fetch("author_triage") == "will_address" }, "#{paper_id} non-will_address decision")
  require!(adjudication.fetch("collateral_authorizations") == [], "#{paper_id} collateral authority is nonempty")

  ops = patch.fetch("ops")
  require!(ops.length == config.fetch(:expected_ops), "#{paper_id} op count #{ops.length} != #{config.fetch(:expected_ops)}")
  require!(ops.map { |op| op.fetch("block_id") }.uniq.length == ops.length, "#{paper_id} duplicate patch block")
  require!(ops.map { |op| op.fetch("block_id") }.sort == expected_targets.keys.sort, "#{paper_id} patch target set mismatch")
  if paper_id != "P33"
    require!(ops.map { |op| op.fetch("block_id") } == request_scope.fetch("block_order"), "#{paper_id} patch request order mismatch")
  else
    physical_target_order = base_blocks.keys.select { |block_id| expected_targets.key?(block_id) }
    require!(ops.map { |op| op.fetch("block_id") } == physical_target_order, "P33 patch physical block order mismatch")
  end
  ops.each do |op|
    block_id = op.fetch("block_id")
    target = expected_targets.fetch(block_id)
    actual_full_hash = Digest::SHA256.hexdigest(normalized_block_text(base_blocks.fetch(block_id)))
    requested_hash = target.fetch("expected_old_hash")
    authorized_full_hash = target.fetch("authorized_full_old_hash")
    require!(authorized_full_hash == actual_full_hash, "#{paper_id}/#{block_id} final emission full old hash mismatch")
    require!(requested_hash.match?(/\A(?:[0-9a-f]{12}|[0-9a-f]{64})\z/),
             "#{paper_id}/#{block_id} invalid request old hash")
    if requested_hash.length == 64
      require!(requested_hash == actual_full_hash, "#{paper_id}/#{block_id} full 64-hex request old hash mismatch")
    else
      require!(requested_hash == actual_full_hash[0, 12], "#{paper_id}/#{block_id} request old hash mismatch")
    end
    require!(op.fetch("op") == "replace_block", "#{paper_id}/#{block_id} non-replace operation")
    require!(manifest_blocks.fetch(block_id) == actual_full_hash[0, 12], "#{paper_id}/#{block_id} manifest old hash mismatch")
    require!(op.fetch("old_hash") == actual_full_hash[0, 12], "#{paper_id}/#{block_id} patch old hash mismatch")
    require!(op.fetch("roadmap_item_ids") == target.fetch("item_ids"), "#{paper_id}/#{block_id} source_traceability provenance mismatch")
    require!(op.fetch("claim_strength_changes") == [], "#{paper_id}/#{block_id} claim-strength change")
    require!(op.fetch("collateral_authorization_ids") == [], "#{paper_id}/#{block_id} collateral authority")
    new_text = op.fetch("new_text")
    require!(!new_text.empty?, "#{paper_id}/#{block_id} empty replacement")
    require!(!new_text.include?("<!--block:"), "#{paper_id}/#{block_id} writer allocated marker")
    require!(heading_signature(new_text) == heading_signature(base_blocks.fetch(block_id)), "#{paper_id}/#{block_id} heading signature changed")
  end
  touched_ratio = ops.length.fdiv(manifest.fetch("blocks").length)
  require!(touched_ratio <= 0.6, "#{paper_id} structural touched ratio #{touched_ratio}")

  relative = lambda { |path| path.relative_path_from(ROOT) }
  run!("python", ROADMAP_CLI, "validate-adjudication", relative.call(paths.fetch(:roadmap)),
       relative.call(paths.fetch(:adjudication)), "--base", relative.call(paths.fetch(:base)),
       "--block-manifest", relative.call(paths.fetch(:manifest)),
       "--claim-surface", relative.call(paths.fetch(:claims)),
       "--artifact-root", relative.call(paper_root))
  preflight[paper_id] = {
    paper_root: paper_root,
    paths: paths,
    output: output,
    report: report,
    base_sha256: sha(paths.fetch(:base)),
    patch_sha256: sha(paths.fetch(:patch)),
    ops: ops.length,
    total_blocks: manifest.fetch("blocks").length,
    touched_ratio: touched_ratio
  }
  puts "#{paper_id}: preflight PASS #{ops.length} exact ops; touched_ratio=#{format('%.6f', touched_ratio)}"
end

if preflight_only
  puts "ROUND10_SCOPE_REISSUE_APPLY_PREFLIGHT_PASS: 130/130 exact operations; no output written"
  exit 0
end

created_artifacts = []
begin
  preflight.each do |paper_id, row|
    paths = row.fetch(:paths)
    relative = lambda { |path| path.relative_path_from(ROOT) }
    run!("python", APPLY_CLI, relative.call(paths.fetch(:base)), relative.call(paths.fetch(:patch)),
         "--block-manifest", relative.call(paths.fetch(:manifest)), "--roadmap", relative.call(paths.fetch(:roadmap)),
         "--author-adjudication", relative.call(paths.fetch(:adjudication)),
         "--claim-surface-manifest", relative.call(paths.fetch(:claims)),
         "--artifact-root", relative.call(row.fetch(:paper_root)), "--output", relative.call(row.fetch(:output)))
    created_artifacts << capture_created_artifact!(row.fetch(:output), "#{paper_id} output")
    created_artifacts << capture_created_artifact!(row.fetch(:report), "#{paper_id} report")
    report = load_json(row.fetch(:report))
    require!(report.fetch("mode") == "patch", "#{paper_id} apply report is not patch mode")
    require!(report.dig("authorization_witness", "status") == "pass", "#{paper_id} authorization witness is not pass")
    require!(report.fetch("base_draft_hash") == row.fetch(:base_sha256)[0, 12], "#{paper_id} report base mismatch")
    require!(report.fetch("output_draft_hash") == sha(row.fetch(:output))[0, 12], "#{paper_id} report output mismatch")
    require!(report.fetch("ops_applied").length == row.fetch(:ops), "#{paper_id} report op count mismatch")
    require!(report.dig("structural_flags", "any") == false, "#{paper_id} unexpected structural flags")
    require!(report.dig("authorization_witness", "unregistered_claim_drift_review_required") == true, "#{paper_id} E6 boundary missing")
    puts "#{paper_id}: official deterministic apply PASS -> #{row.fetch(:output).relative_path_from(ROOT)}"
  end

  replay_complete_freeze!(freeze, "post-apply")
rescue StandardError => error
  rollback_errors = rollback_created_artifacts(created_artifacts)
  if rollback_errors.empty?
    raise
  else
    raise error, "#{error.message}; ROLLBACK ERRORS: #{rollback_errors.join('; ')}", error.backtrace
  end
end

puts "ROUND10_SCOPE_REISSUE_OFFICIAL_APPLY_PASS: 130/130 exact replace_block operations"
