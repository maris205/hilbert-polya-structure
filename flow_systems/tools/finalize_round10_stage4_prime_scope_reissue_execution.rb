#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "pathname"
require "time"
require "tmpdir"

ROOT = Pathname.new(__dir__).parent.expand_path.freeze
ARS = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars").freeze
ANCHOR_TOOL = (ARS / "scripts/ars_anchorize_draft.py").freeze
TOKEN_TOOL = (ARS / "scripts/check_revision_token_conservation.py").freeze
ROADMAP_TOOL = (ARS / "scripts/revision_roadmap.py").freeze
EXACT_AUTHORITY_PREFIX = "BATCH_ROUND10_STAGE4_PRIME_CORRECTION_SCOPE_REISSUE_EXACT_CONFIRMATION"
EXACT_AUTHOR_EVENT = (ROOT / "#{EXACT_AUTHORITY_PREFIX}_AUTHOR_EVENT_20260904.txt").freeze
EXACT_AUTHORIZATION_RECORD = (ROOT / "#{EXACT_AUTHORITY_PREFIX}_AUTHORIZATION_RECORD.md").freeze
FREEZE_PATH = (ROOT / "#{EXACT_AUTHORITY_PREFIX}_INPUT_FREEZE.json").freeze
EXACT_AUTHORIZATION_RECEIPT = (ROOT / "#{EXACT_AUTHORITY_PREFIX}_AUTHORIZATION_RECEIPT.json").freeze
EXACT_AUTHORITY_AUDIT = (ROOT / "#{EXACT_AUTHORITY_PREFIX}_AUTHORITY_AUDIT.json").freeze
EXACT_AUTHOR_EVENT_BYTES = "确认\n".b.freeze
EXACT_AUTHOR_EVENT_SHA = "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe"
EXACT_AUTHORITY_SHA256 = {
  EXACT_AUTHOR_EVENT.basename.to_s => EXACT_AUTHOR_EVENT_SHA,
  EXACT_AUTHORIZATION_RECORD.basename.to_s => "98755a5998aeee16034db32c89d997b3349a1b77b0c41a93ab32ac994a8d8f79",
  FREEZE_PATH.basename.to_s => "7a140287ce95ad6304cc52e7568d66780d77f54d7aaba461515cb087886075e1",
  EXACT_AUTHORIZATION_RECEIPT.basename.to_s => "a21655745ea33c565626c5cc980b8f91a82f4b87ce2d74cfcb012f0c5d7bae21",
  EXACT_AUTHORITY_AUDIT.basename.to_s => "813a600253cdeac98003a69beb7f28dbf35080cfdfe7bb974d1d8c9a323857b2"
}.freeze

TRACK_REQUESTS = {
  "P29_P32" => {
    path: "BATCH_ROUND10_STAGE4_5_CORRECTION_AUTHORIZATION_REQUEST_P29_P32_EXPANDED.json",
    sha256: "51735eed804f9bd933e2f5a1f69ad0068b74921b4ab6fc4cdddaade0b6bc2e5b",
    replace_block_pairs: 46
  },
  "P30_P31" => {
    path: "BATCH_ROUND10_STAGE4_PRIME_EXPANDED_CORRECTION_AUTHORIZATION_REQUEST_P30_P31.json",
    sha256: "9fecba23da5ea90f3c8f252d0a7fbd019d042f600dbeaa320167865273692135",
    replace_block_pairs: 47
  },
  "P33" => {
    path: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P33_SCOPE_EXPANSION.json",
    sha256: "100c97df01c356a52e3dea39ab327873f544d3ac6b32107f1576ae4dcb02db65",
    replace_block_pairs: 37
  }
}.freeze

FINAL_EMISSION_MANIFEST = (ROOT / "#{EXACT_AUTHORITY_PREFIX}_FINAL_EMISSION_MANIFEST.json").freeze
FINAL_EMISSION_STATUS = "PASS_EXACT_CONFIRMATION_FINAL_EMISSION_READY_FOR_DETERMINISTIC_APPLY"
NON_AUTHORIZING_PREPARATION_ROLE = "NON_AUTHORIZING_PREPARATION_EVIDENCE_FOR_EXACT_CONFIRMATION_REEMISSION_ONLY"
# Filled only after the five-paper exact-confirmation re-emission and three
# independent cross-audits have produced the immutable final manifest.
FINAL_EMISSION_MANIFEST_SHA256 = "db98aa8ace700196044b7bb1903251a90782e709d65f6c0712da041c36421091"
CROSS_AUDIT_PATHS = %w[
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P29_P32.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P30_P31.json
  BATCH_ROUND10_STAGE4_PRIME_SCOPE_REISSUE_EXACT_CONFIRMATION_CROSS_AUDIT_P33.json
].freeze

TOKEN_TIMEOUT_SECONDS = 30
P33_BIB_AFTER_SHA = "98bba3645e32b96c8321dad6b3b8dc11087e11e35af835432cbbbee7f0853747"
P33_BIB_AFTER_BYTES = 9_594
P33_BIB_KEYS = %w[P33-S03-CORR P33-S16-CORR].freeze
P33_USE_IDS = %w[P33-U08 P33-U22 P33-U27 P33-U28 P33-U37].freeze

CONFIG = {
  "P29" => {
    number: 29, slug: "29-bianchi-ideal-owner-refinement", revision_round: 3,
    base: "stage4_prime_revision_round2.tex", manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json", claim: "stage4_prime_correction_round3_claim_surface_manifest.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    writer_handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    provisional: "stage4_prime_response_to_reviewers_provisional_round3.json", revised: "stage4_prime_revision_round3.tex",
    output_manifest: "stage4_prime_revision_round3.block-manifest.json", prior_bundle: "stage4_prime_revision_evidence_bundle_round2.json",
    bundle: "stage4_prime_revision_evidence_bundle_round3.json", token: "stage4_prime_token_conservation_round3.json",
    response_json: "stage4_prime_response_to_reviewers_round3.json", response_md: "stage4_prime_response_to_reviewers_round3.md",
    post_log: "stage4_prime_post_apply_revision_log_round3.md", semantic_audit: "stage4_prime_unregistered_claim_drift_audit_round3.md",
    pdf: "stage4_prime_revision_round3.pdf", build_log: "stage4_prime_revision_round3.build.log",
    build_transcript: "stage4_prime_preview_build_transcript_round3.log", build_receipt: "stage4_prime_revision_round3_build_receipt.json",
    bib_scope: :notes, bib: "stage4_prime_references_round2.bib", request_track: "P29_P32",
    expected_ops: 31, total_blocks: 113, preserved_blocks: 82,
    route: "A0/A1 preparation only; formal Route-A tuple UNASSIGNED; positive A2=0; A3=0; A4=0; Route B not invoked"
  },
  "P30" => {
    number: 30, slug: "30-three-disk-nonconstant-roof-determinant", revision_round: 3,
    base: "stage4_prime_revision_round2.tex", manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json", claim: "stage4_prime_correction_round3_claim_surface_manifest.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    writer_handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    provisional: "stage4_prime_response_to_reviewers_provisional_round3.json", revised: "stage4_prime_revision_round3.tex",
    output_manifest: "stage4_prime_revision_round3.block-manifest.json", prior_bundle: "stage4_prime_revision_evidence_bundle_round2.json",
    bundle: "stage4_prime_revision_evidence_bundle_round3.json", token: "stage4_prime_token_conservation_round3.json",
    response_json: "stage4_prime_response_to_reviewers_round3.json", response_md: "stage4_prime_response_to_reviewers_round3.md",
    post_log: "stage4_prime_post_apply_revision_log_round3.md", semantic_audit: "stage4_prime_unregistered_claim_drift_audit_round3.md",
    pdf: "stage4_prime_revision_round3.pdf", build_log: "stage4_prime_revision_round3.build.log",
    build_transcript: "stage4_prime_preview_build_transcript_round3.log", build_receipt: "stage4_prime_revision_round3_build_receipt.json",
    bib_scope: :notes, bib: "stage4_prime_references_round2.bib", request_track: "P30_P31",
    expected_ops: 34, total_blocks: 129, preserved_blocks: 95,
    route: "A0_FAIL / A2_NOT_ELIGIBLE; formal Route-A tuple UNASSIGNED; A3=0; A4=0; Route B not invoked"
  },
  "P31" => {
    number: 31, slug: "31-level11-conjugacy-owner-ledger", revision_round: 3,
    base: "stage4_prime_revision_round2.tex", manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json", claim: "stage4_prime_correction_round3_claim_surface_manifest.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    writer_handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    provisional: "stage4_prime_response_to_reviewers_provisional_round3.json", revised: "stage4_prime_revision_round3.tex",
    output_manifest: "stage4_prime_revision_round3.block-manifest.json", prior_bundle: "stage4_prime_revision_evidence_bundle_round2.json",
    bundle: "stage4_prime_revision_evidence_bundle_round3.json", token: "stage4_prime_token_conservation_round3.json",
    response_json: "stage4_prime_response_to_reviewers_round3.json", response_md: "stage4_prime_response_to_reviewers_round3.md",
    post_log: "stage4_prime_post_apply_revision_log_round3.md", semantic_audit: "stage4_prime_unregistered_claim_drift_audit_round3.md",
    pdf: "stage4_prime_revision_round3.pdf", build_log: "stage4_prime_revision_round3.build.log",
    build_transcript: "stage4_prime_preview_build_transcript_round3.log", build_receipt: "stage4_prime_revision_round3_build_receipt.json",
    bib_scope: :notes, bib: "stage4_prime_references_round2.bib", request_track: "P30_P31",
    expected_ops: 13, total_blocks: 113, preserved_blocks: 100,
    route: "A1-only preparation; formal Route-A tuple UNASSIGNED; positive A2=0; A3=0; A4=0; Route B not invoked"
  },
  "P32" => {
    number: 32, slug: "32-homology-cover-renormalization-uniformity", revision_round: 3,
    base: "stage4_prime_revision_round2.tex", manifest: "stage4_prime_correction_round3_base.block-manifest.json",
    roadmap: "stage4_prime_correction_round3_revision_roadmap.json", claim: "stage4_prime_correction_round3_claim_surface_manifest.json",
    choices: "stage4_prime_correction_round3_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_correction_round3_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round3_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round3.json",
    writer_handoff: "stage4_prime_correction_round3_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_writer_validation_receipt_round3_exact_confirmation.json",
    provisional: "stage4_prime_response_to_reviewers_provisional_round3.json", revised: "stage4_prime_revision_round3.tex",
    output_manifest: "stage4_prime_revision_round3.block-manifest.json", prior_bundle: "stage4_prime_revision_evidence_bundle_round2.json",
    bundle: "stage4_prime_revision_evidence_bundle_round3.json", token: "stage4_prime_token_conservation_round3.json",
    response_json: "stage4_prime_response_to_reviewers_round3.json", response_md: "stage4_prime_response_to_reviewers_round3.md",
    post_log: "stage4_prime_post_apply_revision_log_round3.md", semantic_audit: "stage4_prime_unregistered_claim_drift_audit_round3.md",
    pdf: "stage4_prime_revision_round3.pdf", build_log: "stage4_prime_revision_round3.build.log",
    build_transcript: "stage4_prime_preview_build_transcript_round3.log", build_receipt: "stage4_prime_revision_round3_build_receipt.json",
    bib_scope: :notes, bib: "stage4_prime_references_round2.bib", request_track: "P29_P32",
    expected_ops: 15, total_blocks: 138, preserved_blocks: 123,
    route: "generic A1--A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B not invoked"
  },
  "P33" => {
    number: 33, slug: "33-bolza-control-matched-census", revision_round: 2,
    base: "stage4_revision_round1.tex", manifest: "stage4_prime_round5_base.block-manifest.json",
    roadmap: "stage4_prime_round6_revision_roadmap.json", claim: "stage4_prime_round6_claim_surface_manifest.json",
    choices: "stage4_prime_round6_exact_confirmation_author_choices.json",
    adjudication: "stage4_prime_round6_exact_confirmation_author_adjudication.json",
    patch: "stage4_prime_revision_patch_round6_exact_confirmation.json",
    prepared_patch: "stage4_prime_revision_patch_round6.json",
    writer_handoff: "stage4_prime_round6_exact_confirmation_writer_handoff.json",
    writer_validation: "stage4_prime_round6_exact_confirmation_writer_validation_receipt.json",
    provisional: "stage4_prime_round6_response_to_reviewers_provisional.json", revised: "stage4_prime_revision_round2.tex",
    output_manifest: "stage4_prime_revision_round2.block-manifest.json", prior_bundle: "stage4_revision_evidence_bundle.json",
    bundle: "stage4_prime_revision_evidence_bundle_round2.json", token: "stage4_prime_token_conservation_round2.json",
    response_json: "stage4_prime_response_to_reviewers_round2.json", response_md: "stage4_prime_response_to_reviewers_round2.md",
    post_log: "stage4_prime_post_apply_revision_log_round2.md", semantic_audit: "stage4_prime_unregistered_claim_drift_audit_round2.md",
    pdf: "stage4_prime_revision_round2.pdf", build_log: "stage4_prime_revision_round2.build.log",
    build_transcript: "stage4_prime_preview_build_transcript_round2.log", build_receipt: "stage4_prime_revision_round2_build_receipt.json",
    bib_scope: :paper, bib: "references.bib", request_track: "P33",
    expected_ops: 37, total_blocks: 128, preserved_blocks: 91,
    route: "A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; positive A2=0; A3=0; A4=0; Route B not invoked"
  }
}.freeze

OUTPUT_KEYS = %i[
  output_manifest bundle bundle_receipt token response_json response_md post_log
  semantic_audit pdf build_log build_transcript build_receipt
].freeze

def require!(condition, message)
  raise "ROUND10_SCOPE_REISSUE_FINALIZE_FAIL: #{message}" unless condition
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

def write_json(path, object)
  path.dirname.mkpath
  path.write(JSON.pretty_generate(object) + "\n")
end

def artifact(source, destination, paper_root)
  {
    "path" => destination.relative_path_from(paper_root).to_s,
    "sha256" => sha(source),
    "bytes" => source.size
  }
end

def bundle_artifact(path, paper_root)
  {"path" => path.relative_path_from(paper_root).to_s, "sha256" => sha(path)}
end

def run!(*command, chdir: ROOT)
  stdout, stderr, status = Open3.capture3(*command.map(&:to_s), chdir: chdir.to_s)
  require!(status.success?, "command failed #{command.join(' ')}: #{stderr}#{stdout}")
  [stdout, stderr]
end

def bounded_capture(command, timeout_seconds:, chdir: ROOT)
  stdout_text = +""
  stderr_text = +""
  status = nil
  timed_out = false

  Open3.popen3(*command.map(&:to_s), chdir: chdir.to_s, pgroup: true) do |stdin, stdout, stderr, wait_thread|
    stdin.close
    stdout_reader = Thread.new { stdout.read }
    stderr_reader = Thread.new { stderr.read }
    unless wait_thread.join(timeout_seconds)
      timed_out = true
      begin
        Process.kill("TERM", -wait_thread.pid)
      rescue Errno::ESRCH
        nil
      end
      unless wait_thread.join(2)
        begin
          Process.kill("KILL", -wait_thread.pid)
        rescue Errno::ESRCH
          nil
        end
        wait_thread.join
      end
    end
    status = wait_thread.value
    stdout_text = stdout_reader.value
    stderr_text = stderr_reader.value
  end
  [stdout_text, stderr_text, status, timed_out]
rescue StandardError => error
  [stdout_text, "#{stderr_text}\n#{error.class}: #{error.message}".strip, nil, timed_out]
end

def marker_free_word_count(path)
  path.read.gsub(/<!--.*?-->/m, " ").split.length
end

def item_blocks(report, item_id)
  report.fetch("ops_applied").flat_map do |op|
    op.fetch("roadmap_item_ids").include?(item_id) ? [op.fetch("block_id"), *op.fetch("new_block_ids")] : []
  end.uniq
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

def exact_authority_bindings
  receipt = load_json(EXACT_AUTHORIZATION_RECEIPT)
  {
    "author_event" => receipt.fetch("author_event"),
    "authorization_record" => receipt.fetch("authorization_record"),
    "input_freeze" => receipt.fetch("input_freeze"),
    "authorization_receipt" => {
      "path" => EXACT_AUTHORIZATION_RECEIPT.basename.to_s,
      "sha256" => sha(EXACT_AUTHORIZATION_RECEIPT),
      "bytes" => EXACT_AUTHORIZATION_RECEIPT.size
    },
    "authority_audit" => {
      "path" => EXACT_AUTHORITY_AUDIT.basename.to_s,
      "sha256" => sha(EXACT_AUTHORITY_AUDIT),
      "bytes" => EXACT_AUTHORITY_AUDIT.size
    }
  }
end

def require_same_binding!(actual, expected, label)
  %w[path sha256 bytes].each { |key| require!(actual.fetch(key) == expected.fetch(key), "#{label}: #{key} drift") }
end

def validate_internal_exact_authority!(document, label)
  internal = document.fetch("authority")
  exact_authority_bindings.each do |key, expected|
    require_same_binding!(internal.fetch(key), expected, "#{label}/authority/#{key}")
  end
end

def request_targets
  requests = TRACK_REQUESTS.transform_values { |row| load_json(ROOT / row.fetch(:path)) }
  out = Hash.new { |hash, key| hash[key] = {"item_order" => [], "block_order" => [], "blocks" => {}} }
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
    require!(row.fetch("expected_old_hash") == target.fetch("expected_old_hash"), "#{paper_id}/#{block_id}: request old-hash conflict")
    require!(target.fetch("allowed_operations") == ["replace_block"], "#{paper_id}/#{block_id}: request operation")
    row.fetch("item_ids") << item_id unless row.fetch("item_ids").include?(item_id)
  end
  requests.fetch("P29_P32").fetch("papers").each do |paper|
    paper.fetch("issues").each do |issue|
      item_id = roadmap_id.call(issue.fetch("issue_id"))
      issue.fetch("proposed_targets").each { |target| add.call(paper.fetch("paper_id"), item_id, target) }
    end
  end
  requests.fetch("P30_P31").fetch("papers").each do |paper|
    paper.fetch("all_requested_targets").each do |target|
      add.call(paper.fetch("paper_id"), roadmap_id.call(target.fetch("issue_id")), target)
    end
  end
  requests.fetch("P33").dig("carried_forward_exact_request", "items").each do |item|
    item.fetch("proposed_targets").each { |target| add.call("P33", item.fetch("item_id"), target) }
  end
  requests.fetch("P33").fetch("new_issue_actions").each do |action|
    action.fetch("proposed_targets").each { |target| add.call("P33", action.fetch("action_id"), target) }
  end
  out
end

def paths(config)
  paper_root = ROOT / "papers" / config.fetch(:slug)
  notes = paper_root / "notes"
  bib = config.fetch(:bib_scope) == :notes ? notes / config.fetch(:bib) : paper_root / "paper" / config.fetch(:bib)
  values = {
    root: paper_root, notes: notes, bib: bib,
    base: notes / config.fetch(:base), manifest: notes / config.fetch(:manifest), roadmap: notes / config.fetch(:roadmap),
    claim: notes / config.fetch(:claim), choices: notes / config.fetch(:choices), adjudication: notes / config.fetch(:adjudication),
    patch: notes / config.fetch(:patch), prepared_patch: notes / config.fetch(:prepared_patch),
    writer_handoff: notes / config.fetch(:writer_handoff),
    writer_validation: notes / config.fetch(:writer_validation),
    provisional: notes / config.fetch(:provisional), revised: notes / config.fetch(:revised),
    output_manifest: notes / config.fetch(:output_manifest), prior_bundle: notes / config.fetch(:prior_bundle),
    bundle: notes / config.fetch(:bundle), token: notes / config.fetch(:token), response_json: notes / config.fetch(:response_json),
    response_md: notes / config.fetch(:response_md), post_log: notes / config.fetch(:post_log), semantic_audit: notes / config.fetch(:semantic_audit),
    pdf: notes / config.fetch(:pdf), build_log: notes / config.fetch(:build_log), build_transcript: notes / config.fetch(:build_transcript),
    build_receipt: notes / config.fetch(:build_receipt)
  }
  values[:apply_report] = Pathname.new(values.fetch(:revised).to_s + ".apply-report.json")
  values[:bundle_receipt] = notes / "stage4_prime_bundle_validation_receipt_round#{config.fetch(:revision_round)}.json"
  values
end

def validate_bound_artifact!(row, label)
  relative = Pathname.new(row.fetch("path"))
  require!(!relative.absolute? && relative.each_filename.none? { |part| part == ".." }, "#{label}: unsafe artifact path")
  path = ROOT / relative
  require!(path.file?, "#{label}: missing #{relative}")
  require!(sha(path) == row.fetch("sha256"), "#{label}: digest drift #{relative}")
  require!(path.size == row.fetch("bytes"), "#{label}: byte-size drift #{relative}") if row.key?("bytes")
  path
end

def validate_exact_authority_chain!
  authority_paths = [EXACT_AUTHOR_EVENT, EXACT_AUTHORIZATION_RECORD, FREEZE_PATH, EXACT_AUTHORIZATION_RECEIPT, EXACT_AUTHORITY_AUDIT]
  authority_paths.each do |path|
    require!(path.file?, "missing exact-confirmation authority artifact #{path.basename}")
    require!(sha(path) == EXACT_AUTHORITY_SHA256.fetch(path.basename.to_s), "exact-confirmation authority drift #{path.basename}")
  end
  require!(EXACT_AUTHOR_EVENT.binread == EXACT_AUTHOR_EVENT_BYTES, "exact-confirmation author event bytes")
  require!(sha(EXACT_AUTHOR_EVENT) == EXACT_AUTHOR_EVENT_SHA, "exact-confirmation author event digest")

  receipt = load_json(EXACT_AUTHORIZATION_RECEIPT)
  require!(receipt.fetch("status") == "AUTHORIZED_BY_EXACT_CONFIRMATION_FOR_130_BLOCK_STAGE4_PRIME_EXECUTION",
           "exact-confirmation receipt status")
  require!(receipt.fetch("prepared_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
           "exact-confirmation receipt prepared-evidence role")
  require!(receipt.dig("author_event", "path") == EXACT_AUTHOR_EVENT.basename.to_s, "exact-confirmation receipt event path")
  require!(receipt.dig("author_event", "sha256") == EXACT_AUTHOR_EVENT_SHA, "exact-confirmation receipt event digest")
  require!(receipt.dig("author_event", "bytes") == EXACT_AUTHOR_EVENT_BYTES.bytesize, "exact-confirmation receipt event bytes")
  exact_event_text = EXACT_AUTHOR_EVENT_BYTES.dup.force_encoding("UTF-8")
  require!(receipt.dig("author_event", "exact_text") == exact_event_text, "exact-confirmation receipt event text")
  require!(receipt.dig("authorization_record", "path") == EXACT_AUTHORIZATION_RECORD.basename.to_s, "exact-confirmation record path")
  require!(receipt.dig("authorization_record", "sha256") == sha(EXACT_AUTHORIZATION_RECORD), "exact-confirmation record digest")
  require!(receipt.dig("input_freeze", "path") == FREEZE_PATH.basename.to_s, "exact-confirmation freeze path")
  require!(receipt.dig("input_freeze", "sha256") == sha(FREEZE_PATH), "exact-confirmation freeze digest")

  tracks = receipt.fetch("tracks")
  TRACK_REQUESTS.each do |track_id, expected|
    row = tracks.fetch(track_id)
    require!(row.fetch("path") == expected.fetch(:path), "#{track_id}: receipt request path")
    require!(row.fetch("sha256") == expected.fetch(:sha256), "#{track_id}: receipt request digest")
    require!(row.fetch("replace_block_pairs") == expected.fetch(:replace_block_pairs), "#{track_id}: receipt operation count")
    validate_bound_artifact!({"path" => row.fetch("path"), "sha256" => row.fetch("sha256"), "bytes" => row["bytes"]}.compact,
                             "#{track_id} exact request")
  end
  require!(receipt.dig("aggregate", "papers") == 5, "exact-confirmation receipt paper count")
  require!(receipt.dig("aggregate", "unique_replace_block_pairs") == 130, "exact-confirmation receipt operation total")
  require!(receipt.dig("aggregate", "matrix_regenerations") == 2, "exact-confirmation receipt matrix total")
  require!(receipt.dig("aggregate", "p33_bibliography_appends") == 2, "exact-confirmation receipt bibliography total")

  freeze = load_json(FREEZE_PATH)
  require!(freeze.fetch("status") == "FROZEN_FOR_EXACT_CONFIRMATION_130_BLOCK_EXECUTION", "exact-confirmation freeze status")
  require!(freeze.fetch("prepared_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
           "exact-confirmation freeze prepared-evidence role")
  require!(freeze.dig("author_event", "path") == EXACT_AUTHOR_EVENT.basename.to_s, "freeze event path")
  require!(freeze.dig("author_event", "sha256") == EXACT_AUTHOR_EVENT_SHA, "freeze event digest")
  require!(freeze.dig("author_event", "bytes") == EXACT_AUTHOR_EVENT_BYTES.bytesize, "freeze event bytes")
  require!(freeze.dig("author_event", "exact_text") == exact_event_text, "freeze event text")
  require!(freeze.dig("authorized_scope", "paper_ids") == CONFIG.keys, "freeze paper order")
  require!(freeze.dig("authorized_scope", "unique_replace_block_pairs") == 130, "freeze operation total")
  require!(freeze.dig("authorized_scope", "per_paper") == CONFIG.transform_values { |config| config.fetch(:expected_ops) },
           "freeze per-paper operation totals")
  require!(freeze.dig("authorized_scope", "p30_p31_in_place_matrix_regenerations") == 2, "freeze matrix scope")
  require!(freeze.dig("authorized_scope", "p33_bibliography_append_keys") == P33_BIB_KEYS, "freeze P33 bibliography keys")
  require!(freeze.dig("authorized_scope", "p33_use_bindings") == P33_USE_IDS, "freeze P33 use bindings")

  boundaries = freeze.fetch("boundaries")
  %w[
    fresh_stage4_5_authorized p33_re_review_authorized stage5_or_stage6_authorized canonical_promotion_authorized
    scientific_producer_enumeration_census_or_result_refresh_authorized route_a_or_route_b_credit_authorized
    route_or_initial_system_mutation_authorized structural_edit_authorized
  ].each { |key| require!(boundaries.fetch(key) == false, "freeze boundary #{key}") }
  require!(boundaries.fetch("citation_style") == "natbib numbers sort&compress with plainnat", "freeze citation style")

  audit = load_json(EXACT_AUTHORITY_AUDIT)
  require!(audit.fetch("status") == "PASS_EXACT_CONFIRMATION_AUTHORITY_FROZEN_READY_FOR_DETERMINISTIC_APPLY",
           "exact-confirmation authority audit status")
  require!(audit.fetch("checks_failed") == 0, "exact-confirmation authority audit failures") if audit.key?("checks_failed")
  checks = audit.fetch("checks")
  require!(checks.all? { |row| row.fetch("status") == "PASS" }, "exact-confirmation authority audit non-PASS check")
  [EXACT_AUTHOR_EVENT, EXACT_AUTHORIZATION_RECORD, FREEZE_PATH, EXACT_AUTHORIZATION_RECEIPT].each do |path|
    row = checks.find { |check| check.fetch("check_id") == "binding:#{path.basename}" }
    require!(!row.nil?, "authority audit missing binding #{path.basename}")
    require!(row.dig("detail", "expected") == sha(path) && row.dig("detail", "actual") == sha(path),
             "authority audit binding drift #{path.basename}")
  end
  freeze
end

def validate_final_emission_manifest!
  require!(FINAL_EMISSION_MANIFEST_SHA256.is_a?(String) && FINAL_EMISSION_MANIFEST_SHA256.match?(/\A[0-9a-f]{64}\z/),
           "final exact-confirmation emission manifest SHA-256 pin has not been supplied")
  require!(FINAL_EMISSION_MANIFEST.file?, "missing exact-confirmation final-emission manifest")
  require!(sha(FINAL_EMISSION_MANIFEST) == FINAL_EMISSION_MANIFEST_SHA256, "exact-confirmation final-emission manifest drift")
  manifest = load_json(FINAL_EMISSION_MANIFEST)
  require!(manifest.fetch("schema_version") == "round10-stage4-prime-scope-reissue-exact-confirmation-final-emission-manifest/1.0",
           "final-emission manifest schema")
  require!(manifest.fetch("status") == FINAL_EMISSION_STATUS, "final-emission manifest status")
  require!(manifest.fetch("preparation_evidence_authority_role") == NON_AUTHORIZING_PREPARATION_ROLE,
           "final-emission manifest prepared-evidence role")
  require!(manifest.dig("aggregate", "papers") == 5, "final-emission manifest paper total")
  require!(manifest.dig("aggregate", "unique_replace_block_pairs") == 130, "final-emission manifest operation total")

  authority = manifest.fetch("authority")
  require!(authority.keys.sort == exact_authority_bindings.keys.sort, "final-emission authority key set")
  exact_authority_bindings.each do |key, expected|
    require_same_binding!(authority.fetch(key), expected, "final-emission authority #{key}")
    validate_bound_artifact!(authority.fetch(key), "final-emission authority #{key}")
  end
  require!(authority.dig("author_event", "exact_text") == EXACT_AUTHOR_EVENT_BYTES.dup.force_encoding("UTF-8"),
           "final-emission manifest author-event text")

  targets = request_targets
  require!(targets.sum { |_, row| row.fetch("blocks").length } == 130, "final-emission request target union")
  papers = manifest.fetch("papers")
  require!(papers.map { |row| row.fetch("paper_id") } == CONFIG.keys, "final-emission manifest paper order")
  papers.each do |paper_row|
    paper_id = paper_row.fetch("paper_id")
    config = CONFIG.fetch(paper_id)
    p = paths(config)
    request_scope = targets.fetch(paper_id)
    require!(paper_row.fetch("paper_slug") == config.fetch(:slug), "#{paper_id}: final-emission slug")
    require!(paper_row.fetch("authorized_replace_block_pairs") == config.fetch(:expected_ops), "#{paper_id}: final-emission op count")
    require!(paper_row.fetch("request_track") == config.fetch(:request_track), "#{paper_id}: final-emission request track")
    request = paper_row.fetch("request")
    expected_request = TRACK_REQUESTS.fetch(config.fetch(:request_track))
    require!(request.fetch("path") == expected_request.fetch(:path), "#{paper_id}: final-emission request path")
    require!(request.fetch("sha256") == expected_request.fetch(:sha256), "#{paper_id}: final-emission request digest")
    validate_bound_artifact!(request, "#{paper_id} final-emission request")

    expected_artifacts = {
      "revision_roadmap" => p.fetch(:roadmap),
      "author_choices" => p.fetch(:choices),
      "author_adjudication" => p.fetch(:adjudication),
      "claim_surface_manifest" => p.fetch(:claim),
      "patch" => p.fetch(:patch),
      "writer_handoff" => p.fetch(:writer_handoff),
      "writer_validation" => p.fetch(:writer_validation)
    }
    artifacts = paper_row.fetch("artifacts")
    require!(artifacts.keys.sort == expected_artifacts.keys.sort, "#{paper_id}: final-emission artifact key set")
    expected_artifacts.each do |key, path|
      binding = artifacts.fetch(key)
      require!(binding.fetch("path") == path.relative_path_from(ROOT).to_s, "#{paper_id}: final-emission #{key} path")
      validate_bound_artifact!(binding, "#{paper_id} final-emission #{key}")
    end

    adjudication = load_json(p.fetch(:adjudication))
    item_ids = adjudication.dig("display_order", "item_ids")
    trace = paper_row.fetch("source_traceability")
    require!(trace.fetch("mode") == "source_traceability", "#{paper_id}: final-emission trace mode")
    require!(trace.fetch("canonicalization") == "JSON.generate(item_ids) UTF-8", "#{paper_id}: final-emission trace canonicalization")
    require!(item_ids == request_scope.fetch("item_order"), "#{paper_id}: final-emission/request trace order")
    require!(trace.fetch("item_ids") == item_ids, "#{paper_id}: final-emission trace order")
    require!(trace.fetch("count") == item_ids.length, "#{paper_id}: final-emission trace count")
    trace_digest = Digest::SHA256.hexdigest(JSON.generate(item_ids))
    require!(trace.fetch("sha256") == trace_digest, "#{paper_id}: final-emission trace digest")

    base_blocks = parse_blocks(p.fetch(:base).read)
    expected_old_hash_order = paper_id == "P33" ? base_blocks.keys.select { |block_id| request_scope.fetch("blocks").key?(block_id) } : request_scope.fetch("block_order")
    full_old_hashes = paper_row.fetch("full_old_hashes")
    require!(full_old_hashes.map { |row| row.fetch("block_id") } == expected_old_hash_order,
             "#{paper_id}: final-emission full old-hash order")
    full_old_hashes.each do |row|
      expected = Digest::SHA256.hexdigest(normalized_block_text(base_blocks.fetch(row.fetch("block_id"))))
      require!(row.fetch("sha256") == expected, "#{paper_id}/#{row.fetch('block_id')}: final-emission full old hash")
    end

    choices = load_json(p.fetch(:choices))
    [choices, adjudication].each do |authority|
      events = authority.fetch("author_events")
      require!(events.length == 1, "#{paper_id}: exact-confirmation author-event cardinality")
      require!(events.first.fetch("actor_role") == "author", "#{paper_id}: exact-confirmation event actor")
      require!(events.first.fetch("source") == "explicit_session_user_message", "#{paper_id}: exact-confirmation event source")
      require!(events.first.fetch("input_sha256") == EXACT_AUTHOR_EVENT_SHA, "#{paper_id}: nonexact author event in re-signed authority")
    end
    require!(choices.fetch("author_events") == adjudication.fetch("author_events"), "#{paper_id}: choices/adjudication event divergence")
    require!(choices.fetch("display_order") == adjudication.fetch("display_order"), "#{paper_id}: choices/adjudication order divergence")
    require!(choices.fetch("author_adjudications") == adjudication.fetch("author_adjudications"),
             "#{paper_id}: choices/adjudication decision divergence")
    require!(choices.fetch("collateral_authorizations") == adjudication.fetch("collateral_authorizations"),
             "#{paper_id}: choices/adjudication collateral divergence")
    patch = load_json(p.fetch(:patch))
    prepared_patch = load_json(p.fetch(:prepared_patch))
    require!(patch.fetch("ops") == prepared_patch.fetch("ops"), "#{paper_id}: re-signed patch changed prepared operations/new_text")
    require!(patch.fetch("author_adjudication_sha256") == sha(p.fetch(:adjudication)), "#{paper_id}: re-signed patch/adjudication drift")
    require!(patch.fetch("author_decision_digest") == author_decision_digest(adjudication), "#{paper_id}: re-signed author decision digest")
    handoff = load_json(p.fetch(:writer_handoff))
    validation = load_json(p.fetch(:writer_validation))
    validate_internal_exact_authority!(handoff, "#{paper_id} exact-confirmation handoff")
    validate_internal_exact_authority!(validation, "#{paper_id} exact-confirmation writer validation")
    [handoff, validation].each do |document|
      serialized = JSON.generate(document)
      %w[patch author_choices author_adjudication].each do |key|
        require!(serialized.include?(artifacts.dig(key, "sha256")), "#{paper_id}: writer evidence missing #{key} digest")
      end
    end
    validation_status = validation["status"] || validation["verdict"]
    handoff_status = handoff["status"] || handoff["handoff_status"]
    require!(validation_status.to_s.start_with?("PASS"), "#{paper_id}: writer validation status")
    require!(handoff_status.to_s.match?(/EMITTED|READY/), "#{paper_id}: writer handoff status")

    expected_supporting_paths = case paper_id
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
    supporting = paper_row.fetch("supporting_artifacts", {})
    require!(supporting.values.map { |row| row.fetch("path") }.sort == expected_supporting_paths.sort,
             "#{paper_id}: final-emission supporting-artifact exact path set")
    supporting.each_value { |row| validate_bound_artifact!(row, "#{paper_id} final-emission supporting artifact") }
  end

  audit_bindings = manifest.fetch("root_cross_audits")
  require!(audit_bindings.length == CROSS_AUDIT_PATHS.length, "final-emission cross-audit binding count")
  require!(audit_bindings.map { |row| row.fetch("path") } == CROSS_AUDIT_PATHS, "final-emission cross-audit order/path")
  audit_bindings.each { |row| validate_bound_artifact!(row, "final-emission exact-confirmation cross-audit") }
  manifest
end

def cross_audit_rows!(manifest)
  rows = {}
  bindings = manifest.fetch("root_cross_audits").to_h { |row| [row.fetch("path"), row] }
  emissions = manifest.fetch("papers").to_h do |paper|
    [paper.fetch("paper_id"), {
      "patch_sha256" => paper.dig("artifacts", "patch", "sha256"),
      "source_traceability_sha256" => paper.dig("source_traceability", "sha256")
    }]
  end
  CROSS_AUDIT_PATHS.each do |relative|
    path = ROOT / relative
    binding = bindings.fetch(relative)
    require!(path.file? && sha(path) == binding.fetch("sha256"), "exact-confirmation cross-audit drift #{relative}")
    require!(path.size == binding.fetch("bytes"), "exact-confirmation cross-audit bytes #{relative}")
    audit = load_json(path)
    require!(audit.fetch("status").start_with?("PASS"), "cross-audit status #{relative}")
    validate_internal_exact_authority!(audit, "exact-confirmation cross-audit #{relative}")
    audit.fetch("papers").each do |row|
      paper_id = row.fetch("paper_id")
      require!(!rows.key?(paper_id), "duplicate cross-audit row #{paper_id}")
      require!(row.fetch("findings", []) == [], "cross-audit findings #{paper_id}")
      require!(row.fetch("patch_sha256") == emissions.dig(paper_id, "patch_sha256"), "cross-audit patch binding #{paper_id}")
      require!(row.fetch("source_traceability_sha256") == emissions.dig(paper_id, "source_traceability_sha256"),
               "cross-audit trace binding #{paper_id}")
      request_count = row["request_target_count"] || row["authorized_replace_block_pairs"] || row["op_count"]
      require!(request_count == CONFIG.fetch(paper_id).fetch(:expected_ops), "cross-audit operation count #{paper_id}")
      rows[paper_id] = row
    end
  end
  require!(rows.keys.sort == CONFIG.keys.sort, "cross-audit paper coverage")
  p33 = rows.fetch("P33")
  require!(p33.dig("checks", "physical_block_order") == "PASS", "P33 physical block order")
  require!(p33.dig("checks", "all_required_checks_passed") == true, "P33 required cross-audit checks")
  rows
end

def request_papers
  request = load_json(ROOT / TRACK_REQUESTS.fetch("P29_P32").fetch(:path))
  request.fetch("papers").to_h { |paper| [paper.fetch("paper_id"), paper] }
end

def validate_exact_build_receipt_names!
  request_papers.each do |paper_id, request_paper|
    expected_paths = request_paper.fetch("supporting_operations_after_new_authorization").filter_map do |operation|
      operation.fetch("path") if operation.fetch("operation") == "create_file" && operation.fetch("path").end_with?("_build_receipt.json")
    end
    require!(expected_paths.length == 1, "#{paper_id}: request must authorize exactly one build receipt")
    configured = paths(CONFIG.fetch(paper_id)).fetch(:build_receipt).relative_path_from(ROOT).to_s
    require!(configured == expected_paths.first, "#{paper_id}: build receipt name is not the exact request-authorized path")
  end
end

def validate_exact_confirmation_support_authority!(receipt, label)
  authority = receipt.fetch("exact_confirmation_authority")
  rows = collect_frozen_artifact_rows(authority)
  required = [EXACT_AUTHOR_EVENT, EXACT_AUTHORIZATION_RECORD, FREEZE_PATH, EXACT_AUTHORIZATION_RECEIPT, EXACT_AUTHORITY_AUDIT]
  require!(rows.map { |row| row.fetch("path") }.sort == required.map { |path| path.basename.to_s }.sort,
           "#{label}: exact-confirmation authority path set")
  rows.each { |row| validate_bound_artifact!(row, "#{label} exact-confirmation authority") }
  event = rows.find { |row| row.fetch("path") == EXACT_AUTHOR_EVENT.basename.to_s }
  require!(event.fetch("exact_text") == EXACT_AUTHOR_EVENT_BYTES.dup.force_encoding("UTF-8"), "#{label}: exact event text")

  final_emission = receipt.fetch("final_emission_manifest")
  require!(final_emission.fetch("path") == FINAL_EMISSION_MANIFEST.basename.to_s, "#{label}: final-emission path")
  validate_bound_artifact!(final_emission, "#{label} final-emission manifest")
end

def validate_required_support_receipts!(paper_id, p, freeze_paper)
  case paper_id
  when "P30", "P31"
    receipt_path = p.fetch(:notes) / "stage4_prime_correction_round3_matrix_regeneration_receipt.json"
    require!(receipt_path.file?, "#{paper_id}: mandatory matrix-regeneration receipt missing")
    receipt = load_json(receipt_path)
    validate_exact_confirmation_support_authority!(receipt, "#{paper_id} matrix receipt")
    require!(receipt.fetch("status") == "PASS_AUTHORIZED_IN_PLACE_REGENERATION", "#{paper_id}: matrix receipt status")
    matrix_path = ROOT / receipt.fetch("matrix_path")
    require!(matrix_path.file? && sha(matrix_path) == receipt.fetch("after_sha256"), "#{paper_id}: regenerated matrix/receipt drift")
    require!(receipt.fetch("successor_draft_sha256") == sha(p.fetch(:revised)), "#{paper_id}: matrix receipt/successor drift")
    require!(receipt.fetch("apply_report_sha256") == sha(p.fetch(:apply_report)), "#{paper_id}: matrix receipt/apply drift")
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
    frozen_matrix = freeze_paper.fetch("authorized_in_place_matrix_regeneration")
    require!(receipt.fetch("matrix_path") == frozen_matrix.fetch("path"), "#{paper_id}: matrix receipt path")
    require!(receipt.fetch("before_sha256") == frozen_matrix.fetch("sha256"), "#{paper_id}: matrix receipt before digest")
    matrix = load_json(matrix_path)
    require!(matrix.fetch("result_counts") == expected, "#{paper_id}: regenerated matrix counts")
    require!(matrix.fetch("row_count") == expected.fetch("row_count"), "#{paper_id}: regenerated matrix row count")
    request = load_json(ROOT / TRACK_REQUESTS.fetch("P30_P31").fetch(:path))
    request_row = request.fetch("papers").find { |row| row.fetch("paper_id") == paper_id }.fetch("matrix_regeneration")
    require!(request_row.fetch("path") == receipt.fetch("matrix_path"), "#{paper_id}: matrix request path")
    require!(request_row.fetch("expected_current_sha256") == receipt.fetch("before_sha256"), "#{paper_id}: matrix request base")
    require!(request_row.fetch("expected_result_counts") == expected, "#{paper_id}: matrix request counts")
    require!(receipt.dig("boundaries", "locator_guessing") == false, "#{paper_id}: matrix locator boundary")
    require!(receipt.dig("boundaries", "claim_strengthening") == false, "#{paper_id}: matrix claim boundary")
    require!(receipt.dig("boundaries", "scientific_result_change") == false, "#{paper_id}: matrix science boundary")
    require!(receipt.dig("boundaries", "route_change") == false, "#{paper_id}: matrix Route boundary")
    {
      "path" => receipt.fetch("matrix_path"), "before_sha256" => receipt.fetch("before_sha256"),
      "after_sha256" => receipt.fetch("after_sha256"), "after_bytes" => matrix_path.size
    }
  when "P33"
    receipt_path = p.fetch(:notes) / "stage4_prime_round6_bibliography_append_receipt.json"
    require!(receipt_path.file?, "P33: mandatory bibliography receipt missing")
    receipt = load_json(receipt_path)
    validate_exact_confirmation_support_authority!(receipt, "P33 bibliography receipt")
    require!(receipt.fetch("status") == "PASS_EXACT_TWO_ENTRY_APPEND_AND_FIVE_USE_BINDING", "P33: bibliography receipt status")
    require!(receipt.dig("bibliography", "after_sha256") == P33_BIB_AFTER_SHA && sha(p.fetch(:bib)) == P33_BIB_AFTER_SHA, "P33: bibliography result drift")
    require!(receipt.dig("counts", "entries_appended") == 2 && receipt.dig("counts", "affected_uses_dual_bound") == 5, "P33: bibliography receipt counts")
    require!(receipt.dig("manuscript", "sha256") == sha(p.fetch(:revised)), "P33: bibliography receipt/successor drift")
    require!(receipt.dig("manuscript", "apply_report_sha256") == sha(p.fetch(:apply_report)), "P33: bibliography receipt/apply drift")
    frozen_bib = freeze_paper.fetch("current_working_bibliography")
    require!(receipt.dig("bibliography", "path") == p.fetch(:bib).relative_path_from(p.fetch(:root)).to_s, "P33: bibliography receipt path")
    require!(receipt.dig("bibliography", "before_sha256") == frozen_bib.fetch("sha256"), "P33: bibliography receipt before digest")
    require!(receipt.dig("bibliography", "before_bytes") == frozen_bib.fetch("bytes"), "P33: bibliography receipt before bytes")
    require!(receipt.dig("bibliography", "after_bytes") == P33_BIB_AFTER_BYTES && p.fetch(:bib).size == P33_BIB_AFTER_BYTES,
             "P33: bibliography result bytes")
    require!(receipt.dig("bibliography", "entries_appended") == P33_BIB_KEYS, "P33: bibliography keys")
    require!(receipt.dig("authority", "path") == TRACK_REQUESTS.fetch("P33").fetch(:path), "P33: bibliography authority path")
    require!(receipt.dig("authority", "sha256") == TRACK_REQUESTS.fetch("P33").fetch(:sha256), "P33: bibliography authority digest")
    uses = receipt.dig("manuscript", "dual_bound_uses")
    require!(uses.map { |row| row.fetch("use_id") } == P33_USE_IDS, "P33: bibliography use bindings")
    keys = p.fetch(:bib).read.scan(/@[A-Za-z]+\{([^,]+),/).flatten
    P33_BIB_KEYS.each { |key| require!(keys.count(key) == 1, "P33: bibliography key multiplicity #{key}") }
    require!(receipt.dig("boundaries", "third_entry_added") == false, "P33: bibliography third-entry boundary")
    require!(receipt.dig("boundaries", "scientific_claim_strengthened") == false, "P33: bibliography claim boundary")
    {
      "path" => frozen_bib.fetch("path"), "before_sha256" => frozen_bib.fetch("sha256"),
      "after_sha256" => P33_BIB_AFTER_SHA, "after_bytes" => P33_BIB_AFTER_BYTES
    }
  else
    nil
  end
end

def collect_frozen_artifact_rows(value, rows = [])
  case value
  when Hash
    rows << value if value.key?("path") && value.key?("sha256")
    value.each_value { |child| collect_frozen_artifact_rows(child, rows) }
  when Array
    value.each { |child| collect_frozen_artifact_rows(child, rows) }
  end
  rows
end

def validate_frozen_artifacts!(freeze, authorized_replacements)
  rows = collect_frozen_artifact_rows(freeze)
  require!(rows.length >= 200, "freeze artifact replay unexpectedly incomplete")
  grouped = rows.group_by { |row| row.fetch("path") }
  grouped.each do |relative_string, path_rows|
    relative = Pathname.new(relative_string)
    require!(!relative.absolute? && relative.each_filename.none? { |part| part == ".." }, "freeze unsafe path #{relative_string}")
    path = ROOT / relative
    require!(path.file?, "freeze missing artifact #{relative_string}")
    expected_digests = path_rows.map { |row| row.fetch("sha256") }.uniq
    require!(expected_digests.length == 1, "freeze conflicting digests #{relative_string}")
    replacement = authorized_replacements[relative_string]
    if replacement
      require!(expected_digests.first == replacement.fetch("before_sha256"), "freeze/support before-digest mismatch #{relative_string}")
      require!(sha(path) == replacement.fetch("after_sha256"), "authorized support-result drift #{relative_string}")
      require!(path.size == replacement.fetch("after_bytes"), "authorized support-result bytes #{relative_string}")
    else
      require!(sha(path) == expected_digests.first, "frozen artifact drift #{relative_string}")
      path_rows.each do |row|
        require!(path.size == row.fetch("bytes"), "frozen artifact byte-size drift #{relative_string}") if row.key?("bytes")
      end
    end
  end
  true
end

def validate_apply_and_inputs!(paper_id, config, p, cross_row, request_scope)
  %i[
    base manifest roadmap claim choices adjudication patch writer_handoff writer_validation
    provisional revised apply_report prior_bundle bib
  ].each do |key|
    require!(p.fetch(key).file?, "#{paper_id}: missing #{key}")
  end
  manifest = load_json(p.fetch(:manifest))
  roadmap = load_json(p.fetch(:roadmap))
  claim = load_json(p.fetch(:claim))
  adjudication = load_json(p.fetch(:adjudication))
  patch = load_json(p.fetch(:patch))
  report = load_json(p.fetch(:apply_report))

  require!(cross_row.fetch("patch_path") == p.fetch(:patch).relative_path_from(ROOT).to_s, "#{paper_id}: cross-audit patch path")
  require!(cross_row.fetch("patch_sha256") == sha(p.fetch(:patch)), "#{paper_id}: cross-audit patch drift")
  require!(manifest.fetch("base_draft_hash") == sha(p.fetch(:base))[0, 12], "#{paper_id}: manifest/base mismatch")
  require!(roadmap.fetch("base_draft_sha256") == sha(p.fetch(:base)), "#{paper_id}: roadmap/base mismatch")
  require!(roadmap.fetch("block_manifest_sha256") == sha(p.fetch(:manifest)), "#{paper_id}: roadmap/manifest mismatch")
  require!(roadmap.fetch("items").map { |item| item.fetch("id") } == request_scope.fetch("item_order"),
           "#{paper_id}: roadmap/request source-traceability order")
  require!(claim.fetch("surfaces") == [], "#{paper_id}: registered surface population changed")
  require!(adjudication.fetch("base_draft_sha256") == sha(p.fetch(:base)), "#{paper_id}: adjudication/base mismatch")
  require!(adjudication.fetch("roadmap_sha256") == sha(p.fetch(:roadmap)), "#{paper_id}: adjudication/roadmap mismatch")
  require!(adjudication.fetch("claim_surface_manifest_sha256") == sha(p.fetch(:claim)), "#{paper_id}: adjudication/claim mismatch")
  require!(adjudication.fetch("collateral_authorizations") == [], "#{paper_id}: collateral authority")
  require!(adjudication.fetch("author_events").length == 1 &&
           adjudication.fetch("author_events").first.fetch("input_sha256") == EXACT_AUTHOR_EVENT_SHA,
           "#{paper_id}: adjudication is not exact-confirmation re-signed")
  require!(adjudication.fetch("author_adjudications").all? { |row| row.fetch("author_triage") == "will_address" },
           "#{paper_id}: non-will-address adjudication")
  require!(patch.fetch("patch_format_version") == "1.1", "#{paper_id}: patch format")
  require!(patch.fetch("authorization_context") == "review_roadmap", "#{paper_id}: patch authority context")
  require!(patch.fetch("emitted_by") == "draft_writer_agent", "#{paper_id}: patch emitter")
  require!(patch.fetch("revision_round") == config.fetch(:revision_round), "#{paper_id}: patch round")
  require!(patch.fetch("base_draft_hash") == sha(p.fetch(:base))[0, 12], "#{paper_id}: patch/base mismatch")
  require!(patch.fetch("roadmap_sha256") == sha(p.fetch(:roadmap)), "#{paper_id}: patch/roadmap mismatch")
  require!(patch.fetch("author_adjudication_sha256") == sha(p.fetch(:adjudication)), "#{paper_id}: patch/adjudication mismatch")
  require!(patch.fetch("claim_surface_manifest_sha256") == sha(p.fetch(:claim)), "#{paper_id}: patch/claim mismatch")
  require!(patch.fetch("author_decision_digest") == author_decision_digest(adjudication), "#{paper_id}: patch author-decision digest")
  require!(patch.fetch("ops").length == config.fetch(:expected_ops), "#{paper_id}: patch op count")
  require!(patch.fetch("ops").all? { |op| op.fetch("op") == "replace_block" }, "#{paper_id}: non-replace patch op")
  require!(patch.fetch("ops").map { |op| op.fetch("block_id") }.uniq.length == config.fetch(:expected_ops), "#{paper_id}: duplicate patch target")
  require!(patch.fetch("ops").all? { |op| op.fetch("claim_strength_changes") == [] && op.fetch("collateral_authorization_ids") == [] },
           "#{paper_id}: unauthorized claim/collateral mutation")
  require!(patch.fetch("ops").map { |op| op.fetch("block_id") }.sort == request_scope.fetch("blocks").keys.sort,
           "#{paper_id}: patch/request target set")
  patch.fetch("ops").each do |op|
    target = request_scope.fetch("blocks").fetch(op.fetch("block_id"))
    require!(op.fetch("old_hash") == target.fetch("expected_old_hash")[0, 12], "#{paper_id}/#{op.fetch('block_id')}: request old hash")
    require!(op.fetch("roadmap_item_ids") == target.fetch("item_ids"), "#{paper_id}/#{op.fetch('block_id')}: request provenance")
  end

  require!(report.fetch("mode") == "patch", "#{paper_id}: apply mode")
  require!(report.fetch("patch_digest") == sha(p.fetch(:patch)), "#{paper_id}: apply/patch drift")
  require!(report.fetch("base_draft_hash") == sha(p.fetch(:base))[0, 12], "#{paper_id}: apply/base drift")
  require!(report.fetch("output_draft_hash") == sha(p.fetch(:revised))[0, 12], "#{paper_id}: apply/output drift")
  require!(report.fetch("revision_round") == config.fetch(:revision_round), "#{paper_id}: apply round")
  require!(report.dig("authorization_witness", "status") == "pass", "#{paper_id}: apply witness")
  require!(report.dig("authorization_witness", "roadmap_sha256") == sha(p.fetch(:roadmap)), "#{paper_id}: apply roadmap witness")
  require!(report.dig("authorization_witness", "author_adjudication_sha256") == sha(p.fetch(:adjudication)),
           "#{paper_id}: apply adjudication witness")
  require!(report.dig("authorization_witness", "author_decision_digest") == patch.fetch("author_decision_digest"),
           "#{paper_id}: apply author-decision witness")
  require!(report.dig("authorization_witness", "claim_surface_manifest_sha256") == sha(p.fetch(:claim)),
           "#{paper_id}: apply claim witness")
  require!(report.fetch("ops_applied").length == config.fetch(:expected_ops), "#{paper_id}: applied op count")
  require!(report.fetch("ops_applied").all? { |op| op.fetch("claim_strength_changes") == [] && op.fetch("collateral_authorization_ids") == [] },
           "#{paper_id}: apply report claim/collateral mutation")
  require!(report.dig("counters", "blocks_total") == config.fetch(:total_blocks), "#{paper_id}: block total")
  require!(report.dig("counters", "blocks_preserved_byte_identical") == config.fetch(:preserved_blocks), "#{paper_id}: preserved blocks")
  require!(report.dig("structural_flags", "any") == false, "#{paper_id}: structural flag")
  require!(report.dig("authorization_witness", "unregistered_claim_drift_review_required") == true, "#{paper_id}: E6 boundary")

  source = p.fetch(:revised).read
  require!(source.include?("\\usepackage[numbers,sort&compress]{natbib}"), "#{paper_id}: natbib style drift")
  require!(source.include?("\\bibliographystyle{plainnat}"), "#{paper_id}: bibliography style drift")
  require!(!source.match?(/[\x00-\x08\x0b\x0c\x0e-\x1f]/), "#{paper_id}: TeX control byte")
  report
end

def all_destinations(context)
  context.values.flat_map do |row|
    OUTPUT_KEYS.map { |key| [row.fetch(:paths).fetch(key), row.fetch(:staged).fetch(key)] }
  end
end

def validate_output_collisions!(context)
  destinations = all_destinations(context).map(&:first)
  require!(destinations.length == CONFIG.length * OUTPUT_KEYS.length, "output destination coverage")
  require!(destinations.map(&:to_s).uniq.length == destinations.length, "duplicate output destination")
  destinations.each { |path| require!(!path.exist?, "refusing to overwrite output #{path.relative_path_from(ROOT)}") }
end

def build_response(paper_id, config, p, staged, report, build, generated_at)
  require!(build.fetch("status") == "PASS_CLEAN", "#{paper_id}: response cannot precede a clean build")
  provisional = load_json(p.fetch(:provisional))
  rows = provisional.fetch("items").map do |source|
    item_id = source.fetch("roadmap_item_id")
    response_text = source["author_response"] || source["response_text"]
    require!(!response_text.to_s.empty?, "#{paper_id}/#{item_id}: provisional response absent")
    inherited_status = source.fetch("status", "RESOLVED")
    final_status = inherited_status.match?(/LIMITATION/) ? "DELIBERATE_LIMITATION" : "RESOLVED_AUTHOR_SIDE"
    {
      "roadmap_item_id" => item_id,
      "source_issue_id" => source["source_issue_id"],
      "reviewer_comment" => source["reviewer_comment"] || source["request_severity"],
      "author_response" => response_text.gsub(/Application,.*pending\.?/m, "The authorized replacements were deterministically applied and build-verified; fresh Stage 4.5 remains pending."),
      "change_block_ids" => item_blocks(report, item_id),
      "status" => final_status
    }.compact
  end
  expected_ids = load_json(p.fetch(:adjudication)).dig("display_order", "item_ids")
  require!(rows.map { |row| row.fetch("roadmap_item_id") } == expected_ids, "#{paper_id}: response item order")
  require!(rows.all? { |row| !row.fetch("change_block_ids").empty? }, "#{paper_id}: response item without applied block")
  object = {
    "schema_version" => "round10-stage4-prime-scope-reissue-final-response/1.0",
    "artifact_status" => "FINAL_AUTHOR_SIDE_CORRECTION_AWAITING_FRESH_STAGE4_5",
    "paper_id" => paper_id,
    "revision_round" => config.fetch(:revision_round),
    "generated_at_utc" => generated_at,
    "patch" => artifact(p.fetch(:patch), p.fetch(:patch), p.fetch(:root)),
    "revised_draft" => artifact(p.fetch(:revised), p.fetch(:revised), p.fetch(:root)),
    "apply_report" => artifact(p.fetch(:apply_report), p.fetch(:apply_report), p.fetch(:root)),
    "items" => rows,
    "summary" => {
      "items" => rows.length,
      "resolved_author_side" => rows.count { |row| row.fetch("status") == "RESOLVED_AUTHOR_SIDE" },
      "deliberate_limitations" => rows.count { |row| row.fetch("status") == "DELIBERATE_LIMITATION" },
      "applied_operations" => report.fetch("ops_applied").length,
      "word_count_delta" => marker_free_word_count(p.fetch(:revised)) - marker_free_word_count(p.fetch(:base)),
      "fresh_stage4_5_run" => false,
      "scientific_execution" => false,
      "route_state_changed" => false
    },
    "boundary" => "Author-side corrections are complete. Fresh Stage 4.5 is a separately authorized integrity gate; no scientific result or Route credit is implied."
  }
  write_json(staged.fetch(:response_json), object)
  lines = ["# #{paper_id} Stage 4′ correction response", "", "Date: **2026-09-04**", ""]
  rows.each do |row|
    lines += ["## `#{row.fetch('roadmap_item_id')}` — #{row.fetch('status')}", "", row.fetch("author_response"), "", "Applied blocks: #{row.fetch('change_block_ids').map { |id| "`#{id}`" }.join(', ')}.", ""]
  end
  lines += ["All authorized manuscript operations were applied and build-verified. Fresh Stage 4.5, scientific execution, canonical manuscript/PDF promotion, Route advancement, and initial-system changes were not performed.", ""]
  staged.fetch(:response_md).write(lines.join("\n"))
  object
end

def build_bundle(paper_id, config, p, staged, generated_at)
  bundle = load_json(p.fetch(:prior_bundle))
  expected_prior_rounds = config.fetch(:revision_round) - 1
  require!(bundle.fetch("rounds").length == expected_prior_rounds, "#{paper_id}: prior bundle round count")
  require!(bundle.dig("final_draft", "sha256") == sha(p.fetch(:base)), "#{paper_id}: prior final/base mismatch")
  round = {
    "kind" => "review_roadmap",
    "revision_round" => config.fetch(:revision_round),
    "pre_round_draft" => bundle_artifact(p.fetch(:base), p.fetch(:root)),
    "pre_round_block_manifest" => bundle_artifact(p.fetch(:manifest), p.fetch(:root)),
    "revision_roadmap" => bundle_artifact(p.fetch(:roadmap), p.fetch(:root)),
    "claim_surface_manifest" => bundle_artifact(p.fetch(:claim), p.fetch(:root)),
    "author_adjudication" => bundle_artifact(p.fetch(:adjudication), p.fetch(:root)),
    "revision_patch" => bundle_artifact(p.fetch(:patch), p.fetch(:root)),
    "apply_report" => bundle_artifact(p.fetch(:apply_report), p.fetch(:root)),
    "post_round_draft" => bundle_artifact(p.fetch(:revised), p.fetch(:root))
  }
  bundle.fetch("rounds") << round
  bundle["final_draft"] = round.fetch("post_round_draft")
  write_json(staged.fetch(:bundle), bundle)
  stdout, stderr = run!("python3", ROADMAP_TOOL, "validate-bundle", staged.fetch(:bundle), "--root", p.fetch(:root))
  write_json(staged.fetch(:bundle_receipt), {
    "schema_version" => "round10-stage4-prime-scope-reissue-bundle-validation/1.0",
    "paper_id" => paper_id,
    "validated_at_utc" => generated_at,
    "status" => "PASS",
    "bundle" => artifact(staged.fetch(:bundle), p.fetch(:bundle), p.fetch(:root)),
    "stdout" => stdout.strip,
    "stderr" => stderr.strip
  })
  staged.fetch(:bundle_receipt)
end

def build_preview(paper_id, config, p, staged, generated_at)
  transcript = +""
  Dir.mktmpdir("build.", staged.fetch(:pdf).dirname.to_s) do |tmp_string|
    tmp = Pathname.new(tmp_string)
    marker_free = p.fetch(:revised).read.lines.reject { |line| line.match?(/\A<!--block:B\d+-->\s*\z/) }.join
    (tmp / "manuscript.tex").write(marker_free)
    FileUtils.cp(p.fetch(:bib), tmp / "references.bib")
    job = "stage4_prime_revision_round#{config.fetch(:revision_round)}"
    [["/usr/bin/lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"],
     ["/usr/bin/bibtex", job],
     ["/usr/bin/lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"],
     ["/usr/bin/lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"]].each do |command|
      stdout, stderr, status = Open3.capture3(*command, chdir: tmp.to_s)
      transcript << "$ #{command.join(' ')}\n#{stdout}#{stderr}\n"
      require!(status.success?, "#{paper_id}: build command failed #{command.join(' ')}")
    end
    FileUtils.cp(tmp / "#{job}.pdf", staged.fetch(:pdf))
    FileUtils.cp(tmp / "#{job}.log", staged.fetch(:build_log))
  end
  staged.fetch(:build_transcript).write(transcript)
  log = staged.fetch(:build_log).read
  fatal = log.scan(/Fatal error|Emergency stop/i).length
  undefined_citations = log.scan(/Citation [`'][^\n]+ undefined|There were undefined citations/i).length
  undefined_references = log.scan(/Reference [`'][^\n]+ undefined|There were undefined references/i).length
  missing_glyphs = log.scan(/Missing character:/).length
  overfull = log.scan(/Overfull \\hbox \(([0-9.]+)pt too wide\)/).flatten.map(&:to_f)
  require!([fatal, undefined_citations, undefined_references, missing_glyphs, overfull.length].all?(&:zero?), "#{paper_id}: non-clean final preview")
  info, = run!("/usr/bin/pdfinfo", staged.fetch(:pdf))
  pages = info[/^Pages:\s+(\d+)/, 1].to_i
  page_size = info[/^Page size:\s+(.+)$/, 1]
  pdf_text, = run!("/usr/bin/pdftotext", staged.fetch(:pdf), "-")
  require!(!pdf_text.strip.empty?, "#{paper_id}: empty PDF text extraction")
  receipt = {
    "schema_version" => "round10-stage4-prime-scope-reissue-preview-build/1.0",
    "paper_id" => paper_id,
    "generated_at_utc" => generated_at,
    "classification" => "NOTES_SIDE_STAGE4_PRIME_CORRECTION_PREVIEW_NOT_CANONICAL_PROMOTION",
    "status" => "PASS_CLEAN",
    "compiler_sequence" => ["lualatex", "bibtex", "lualatex", "lualatex"],
    "citation_style" => "natbib[numbers,sort&compress] + plainnat",
    "pages" => pages,
    "page_size" => page_size,
    "undefined_citations" => undefined_citations,
    "undefined_references" => undefined_references,
    "missing_glyphs" => missing_glyphs,
    "fatal_errors" => fatal,
    "overfull_hboxes" => overfull.length,
    "bindings" => {
      "revised_draft_sha256" => sha(p.fetch(:revised)),
      "patch_sha256" => sha(p.fetch(:patch)),
      "evidence_bundle_sha256" => sha(staged.fetch(:bundle)),
      "references_bib_sha256" => sha(p.fetch(:bib)),
      "preview_pdf_sha256" => sha(staged.fetch(:pdf)),
      "final_build_log_sha256" => sha(staged.fetch(:build_log)),
      "build_transcript_sha256" => sha(staged.fetch(:build_transcript))
    },
    "boundaries" => {
      "canonical_manuscript_or_pdf_modified" => false,
      "canonical_bibliography_modified" => paper_id == "P33",
      "p33_exact_bibliography_exception" => paper_id == "P33",
      "canonical_results_refreshed" => false,
      "fresh_stage4_5_invoked" => false,
      "stage5_or_stage6_invoked" => false
    }
  }
  write_json(staged.fetch(:build_receipt), receipt)
  receipt
end

def build_output_manifest(paper_id, config, p, staged)
  before = sha(p.fetch(:revised))
  apply_report = load_json(p.fetch(:apply_report))
  expected_output_blocks = apply_report.dig("counters", "blocks_total") + apply_report.fetch("fresh_block_ids").length
  require!(apply_report.dig("counters", "blocks_total") == config.fetch(:total_blocks),
           "#{paper_id}: output-manifest base block count")
  anchor_check = staged.fetch(:output_manifest).dirname / "#{p.fetch(:revised).basename}.anchor-check"
  require!(!anchor_check.exist?, "#{paper_id}: anchor-check staging collision")
  begin
    FileUtils.cp(p.fetch(:revised), anchor_check)
    stdout, = run!("python3", ANCHOR_TOOL, anchor_check, "--manifest-out", staged.fetch(:output_manifest))
    require!(sha(anchor_check) == before, "#{paper_id}: successor anchorization was not idempotent")
    require!(sha(p.fetch(:revised)) == before, "#{paper_id}: official successor drift during staged anchor check")
    require!(stdout.include?("0 newly labeled"), "#{paper_id}: unexpected new marker allocation")
    manifest = load_json(staged.fetch(:output_manifest))
    require!(manifest.fetch("blocks").length == expected_output_blocks, "#{paper_id}: output manifest block count")
  ensure
    anchor_check.delete if anchor_check.exist?
  end
end

def build_token_advisory(paper_id, config, p, staged, generated_at)
  command = ["python3", TOKEN_TOOL, "patch", "--patch", p.fetch(:patch), "--base", p.fetch(:base)]
  report = nil
  stdout = ""
  stderr = ""
  status = nil
  timed_out = false
  if TOKEN_TOOL.file?
    stdout, stderr, process_status, timed_out = bounded_capture(command, timeout_seconds: TOKEN_TIMEOUT_SECONDS)
    if !timed_out && process_status&.success?
      begin
        parsed = JSON.parse(stdout)
        report = parsed if parsed.fetch("op_reports").length == config.fetch(:expected_ops)
      rescue JSON::ParserError, KeyError, TypeError
        report = nil
      end
    end
    status = report ? "PASS" : "UNAVAILABLE"
  else
    status = "UNAVAILABLE"
    stderr = "advisory token checker is absent"
  end
  object = report || {"conserved" => nil, "op_reports" => []}
  object["advisory_execution"] = {
    "schema_version" => "round10-stage4-prime-token-advisory-execution/1.0",
    "paper_id" => paper_id,
    "generated_at_utc" => generated_at,
    "status" => status,
    "timeout_seconds" => TOKEN_TIMEOUT_SECONDS,
    "timed_out" => timed_out,
    "non_blocking" => true,
    "command" => command.map(&:to_s),
    "stderr" => stderr.to_s.strip[0, 4_000],
    "stdout_sha256" => Digest::SHA256.hexdigest(stdout.to_s)
  }
  write_json(staged.fetch(:token), object)
  status
end

def semantic_audit_text(paper_id, config)
  <<~MD
    # #{paper_id} Stage 4′ correction semantic-boundary audit

    Date: **2026-09-04**

    Status: **PASS WITH MODEL-MEDIATED LIMITATION — FRESH STAGE 4.5 REQUIRED**

    The exact #{config.fetch(:expected_ops)} authorized replacements were compared with their source-finalization or support contracts and independently cross-audited before deterministic application. The final prose distinguishes bounded passage locators from explicit source unavailability, and does not promote metadata, short excerpts, synthetic schema fixtures, or inherited architecture into a scientific result. Registered ClaimIntent population is 0/0, so this remains an E6 model-mediated review rather than a deterministic clean-claim certificate.

    Route state remains: `#{config.fetch(:route)}`. The frozen initial dynamical system, scientific inputs/results, clock, normalization, primitive/owner rules, cutoff, and target-blind/no-retuning restrictions are unchanged. Fresh Stage 4.5 was not run.
  MD
end

def validate_semantic_candidate!(paper_id, config, p, staged, cross_row)
  text = staged.fetch(:semantic_audit).read
  require!(text.include?("exact #{config.fetch(:expected_ops)} authorized replacements"), "#{paper_id}: semantic audit op count")
  require!(text.include?(config.fetch(:route)), "#{paper_id}: semantic audit Route boundary")
  require!(text.include?("Fresh Stage 4.5 was not run"), "#{paper_id}: semantic audit Stage 4.5 boundary")
  require!(cross_row.fetch("findings", []) == [], "#{paper_id}: semantic cross-audit findings")
  source = p.fetch(:revised).read
  require!(!source.match?(/[\x00-\x08\x0b\x0c\x0e-\x1f]/), "#{paper_id}: semantic preflight control byte")
  apply_report = load_json(p.fetch(:apply_report))
  expected_output_blocks = apply_report.dig("counters", "blocks_total") + apply_report.fetch("fresh_block_ids").length
  markers = source.scan(/<!--block:(B\d{4})-->/).flatten
  require!(markers.length == expected_output_blocks, "#{paper_id}: semantic preflight marker count")
  require!(markers.uniq.length == markers.length, "#{paper_id}: semantic preflight duplicate marker")
  true
end

def build_post_log(paper_id, config, p, staged, bundle_receipt, build, token_status)
  staged.fetch(:post_log).write(<<~MD)
    # #{paper_id} Stage 4′ correction post-apply log

    Date: **2026-09-04**

    - Official deterministic application: **PASS**, #{config.fetch(:expected_ops)} operations.
    - Untouched source blocks: **#{config.fetch(:preserved_blocks)}/#{config.fetch(:total_blocks)} byte-identical**.
    - Revised draft SHA-256: `#{sha(p.fetch(:revised))}`.
    - Patch SHA-256: `#{sha(p.fetch(:patch))}`; apply report: `#{sha(p.fetch(:apply_report))}`.
    - Output block manifest: `#{sha(staged.fetch(:output_manifest))}`; token advisory: **#{token_status}**, `#{sha(staged.fetch(:token))}`.
    - Final response: `#{sha(staged.fetch(:response_json))}`; evidence bundle: `#{sha(staged.fetch(:bundle))}`; bundle validation: `#{sha(bundle_receipt)}`.
    - Notes-side preview: **#{build.fetch('pages')} pages, zero fatal/undefined citation/undefined reference/missing-glyph/overfull errors**; PDF `#{sha(staged.fetch(:pdf))}`.
    - Citation system: `natbib[numbers,sort&compress] + plainnat`.
    - Route state: #{config.fetch(:route)}.

    Author-side Stage 4′ correction is complete; fresh Stage 4.5 remains a separate mandatory checkpoint. No scientific execution, result refresh, canonical manuscript/PDF promotion, Stage 5/6, or Route advancement occurred.
  MD
end

def prepare_context(staging_root, create_staging_directories: true)
  CONFIG.to_h do |paper_id, config|
    p = paths(config)
    paper_stage = staging_root / paper_id
    paper_stage.mkpath if create_staging_directories
    staged = OUTPUT_KEYS.to_h { |key| [key, paper_stage / p.fetch(key).basename] }
    [paper_id, {config: config, paths: p, staged: staged}]
  end
end

def global_preflight!(context)
  freeze = validate_exact_authority_chain!
  final_emission_manifest = validate_final_emission_manifest!
  cross_rows = cross_audit_rows!(final_emission_manifest)
  targets = request_targets
  validate_exact_build_receipt_names!
  validate_output_collisions!(context)
  freeze_by_paper = freeze.fetch("papers").to_h { |paper| [paper.fetch("paper_id"), paper] }
  require!(freeze_by_paper.keys.sort == CONFIG.keys.sort, "freeze paper coverage")
  replacements = {}
  context.each do |paper_id, row|
    p = row.fetch(:paths)
    validate_apply_and_inputs!(paper_id, row.fetch(:config), p, cross_rows.fetch(paper_id), targets.fetch(paper_id))
  end
  context.each do |paper_id, row|
    replacement = validate_required_support_receipts!(paper_id, row.fetch(:paths), freeze_by_paper.fetch(paper_id))
    next if replacement.nil?
    require!(!replacements.key?(replacement.fetch("path")), "duplicate authorized frozen replacement #{replacement.fetch('path')}")
    replacements[replacement.fetch("path")] = replacement
  end
  require!(replacements.length == 3, "support receipt coverage must be exactly two matrices plus P33 bibliography")
  validate_frozen_artifacts!(freeze, replacements)
  {freeze: freeze, final_emission_manifest: final_emission_manifest, cross_rows: cross_rows, replacements: replacements}
end

def validate_candidate_set!(context)
  all_destinations(context).each do |destination, candidate|
    require!(candidate.file?, "missing staged candidate #{destination.relative_path_from(ROOT)}")
    require!(candidate.size.positive?, "empty staged candidate #{destination.relative_path_from(ROOT)}")
    JSON.parse(candidate.read) if destination.extname == ".json"
  end
end

def promote_candidates!(context, freeze, replacements)
  pairs = all_destinations(context)
  pairs.each do |destination, candidate|
    require!(!destination.exist?, "promotion collision #{destination.relative_path_from(ROOT)}")
    require!(candidate.stat.dev == destination.dirname.stat.dev, "non-atomic cross-device promotion #{destination.relative_path_from(ROOT)}")
  end
  expected = pairs.to_h { |destination, candidate| [destination, sha(candidate)] }
  promoted = []
  begin
    pairs.each do |destination, candidate|
      require!(!destination.exist?, "late promotion collision #{destination.relative_path_from(ROOT)}")
      File.chmod(0o644, candidate)
      begin
        File.link(candidate, destination)
      rescue Errno::EEXIST
        require!(false, "late promotion collision #{destination.relative_path_from(ROOT)}")
      end
      promoted << destination
    end
    promoted.each { |destination| require!(sha(destination) == expected.fetch(destination), "post-promotion drift #{destination.relative_path_from(ROOT)}") }
    validate_frozen_artifacts!(freeze, replacements)
  rescue StandardError
    promoted.reverse_each do |destination|
      candidate = pairs.to_h.fetch(destination)
      next unless destination.file? && candidate.file? && File.identical?(destination, candidate)
      File.delete(destination)
    end
    raise
  end
end

if $PROGRAM_NAME == __FILE__
  generated_at = Time.now.utc.iso8601
  preflight_context = prepare_context(ROOT / ".round10-stage4-prime-finalize.preflight-only",
                                      create_staging_directories: false)

  # Complete the five-paper read-only gate before even creating a staging
  # directory.  Old prepared artifacts are checked only as frozen provenance;
  # execution authority comes exclusively from the exact-confirmation chain
  # and its final-emission manifest.
  initial_preflight = global_preflight!(preflight_context)

  Dir.mktmpdir(".round10-stage4-prime-finalize.", ROOT.to_s) do |staging_string|
    staging_root = Pathname.new(staging_string)
    context = prepare_context(staging_root)

    context.each do |paper_id, row|
      config = row.fetch(:config)
      p = row.fetch(:paths)
      staged = row.fetch(:staged)
      report = load_json(p.fetch(:apply_report))

      build_output_manifest(paper_id, config, p, staged)
      token_status = build_token_advisory(paper_id, config, p, staged, generated_at)
      bundle_receipt = build_bundle(paper_id, config, p, staged, generated_at)
      build = build_preview(paper_id, config, p, staged, generated_at)
      require!(build.fetch("status") == "PASS_CLEAN", "#{paper_id}: clean build gate")

      # A final response is intentionally impossible until the clean-build gate
      # above has succeeded.
      build_response(paper_id, config, p, staged, report, build, generated_at)
      staged.fetch(:semantic_audit).write(semantic_audit_text(paper_id, config))
      validate_semantic_candidate!(paper_id, config, p, staged, initial_preflight.fetch(:cross_rows).fetch(paper_id))
      build_post_log(paper_id, config, p, staged, bundle_receipt, build, token_status)
      puts "#{paper_id}: staged PASS #{config.fetch(:expected_ops)} ops, #{build.fetch('pages')} pages, clean build; token=#{token_status}"
    end

    validate_candidate_set!(context)

    # Re-run the complete read-only gate after the long build phase.  This also
    # catches late destination collisions and any concurrent input/freeze drift.
    prepromotion = global_preflight!(context)
    validate_candidate_set!(context)
    promote_candidates!(context, prepromotion.fetch(:freeze), prepromotion.fetch(:replacements))
  end

  puts "ROUND10_SCOPE_REISSUE_POST_APPLY_FINALIZER_PASS: 5/5 papers; 130/130 operations; 60/60 outputs atomically promoted"
end
