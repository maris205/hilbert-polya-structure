#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"
require "open3"
require "pathname"
require "time"

ROOT = Pathname.new(__dir__).parent.expand_path
FREEZE_PATH = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json"
REQUEST_PATH = ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json"
ROADMAP_TOOL = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/scripts/revision_roadmap.py")

CONFIG = {
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    patch_sha: "5876b07df9741ca1d384a78441030d96734a1e87547e94cb7c097efa8d099846",
    draft_sha: "6c09fa99b17a1f0d47a1c186f0fe48072a3f7d7e45b036a0b237460cd51ae39a",
    report_sha: "b633ca6116992ee8ad97e825a05ffef53eff2127cd2d611d965c3fa275e482d9",
    ops: 14, blocks_total: 127, blocks_preserved: 113, response_items: 5,
    replay_rows: 54, matrix_rows: 28, canonical_bib_entries: 26,
    versioned_bib_entries: 28, pages: 16,
    matrix_file: "stage4_prime_claim_passage_matrix_round2.json",
    verification_file: "stage4_prime_correction_source_verification_round2.json",
    new_keys: %w[P30-C01 P30-C02]
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    patch_sha: "aeb40a0f7bc440d96ad9ffae4fed1137fb28c6ff9162d98c49a53d04b003dbc2",
    draft_sha: "2f71faeb4f7306f2475cd7cdb4f4fd692166f4a363eb1dfea3d11fd836eee9ea",
    report_sha: "7e70373d0104a2c8a8b6252418b7478ed2324bcd9003f2c16ddcb120e329fa0c",
    ops: 20, blocks_total: 111, blocks_preserved: 93, response_items: 8,
    replay_rows: 20, matrix_rows: 24, canonical_bib_entries: 22,
    versioned_bib_entries: 24, pages: 13,
    matrix_file: "stage4_prime_method_passage_matrix_round2.json",
    verification_file: "stage4_prime_closest_work_source_verification_round2.json",
    new_keys: %w[P31-S23 P31-S24]
  }
}.freeze

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def json(path)
  JSON.parse(File.read(path))
end

def control_byte_count(bytes)
  bytes.bytes.count { |byte| byte < 32 && ![9, 10, 13].include?(byte) }
end

def bib_entry_count(path)
  File.read(path).lines.count { |line| line.start_with?("@") }
end

def semantic_layout_normalize(text)
  text.gsub("\\allowbreak{}", "")
      .gsub("\\begingroup\\sloppy", "")
      .gsub("\\par\\endgroup", "")
      .gsub(/\s+/, " ").strip
end

freeze = json(FREEZE_PATH)
request = json(REQUEST_PATH)
all_failures = []

CONFIG.each do |paper_id, config|
  paper_root = ROOT / "papers" / config[:slug]
  notes = paper_root / "notes"
  checks = []
  check = lambda do |name, pass, detail = nil|
    row = {"name" => name, "status" => pass ? "PASS" : "FAIL"}
    row["detail"] = detail unless detail.nil?
    checks << row
  end

  freeze.fetch("authority_and_roadmap_bindings").each do |binding|
    path = ROOT / binding.fetch("path")
    actual = File.file?(path) ? sha(path) : "MISSING"
    check.call("authority freeze: #{binding.fetch("path")}", actual == binding.fetch("sha256"), {"expected" => binding.fetch("sha256"), "actual" => actual})
  end

  frozen_paper = freeze.fetch("papers").find { |entry| entry.fetch("paper_id") == paper_id }
  protected = frozen_paper.fetch("canonical_files") + frozen_paper.fetch("science_files") +
              [frozen_paper.fetch("initial_system_source"), frozen_paper.fetch("route_crosswalk")] +
              frozen_paper.fetch("track_inputs")
  protected.each do |binding|
    path = ROOT / binding.fetch("path")
    actual = File.file?(path) ? sha(path) : "MISSING"
    check.call("protected input: #{binding.fetch("path")}", actual == binding.fetch("sha256"), {"expected" => binding.fetch("sha256"), "actual" => actual})
  end

  paths = {
    patch: notes / "stage4_prime_revision_patch_round2.json",
    draft: notes / "stage4_prime_revision_round2.tex",
    report: notes / "stage4_prime_revision_round2.tex.apply-report.json",
    handoff: notes / "stage4_prime_writer_handoff.json",
    bundle: notes / "stage4_prime_revision_evidence_bundle_round2.json",
    support: notes / "stage4_prime_support_evidence_bundle_round2.json",
    build_receipt: notes / "stage4_prime_preview_build_receipt_round2.json",
    build_log: notes / "stage4_prime_revision_round2.build.log",
    pdf: notes / "stage4_prime_revision_round2.pdf",
    response: notes / "stage4_prime_response_to_reviewers_round2.json",
    claim_replay: notes / "stage4_prime_registered_claim_surface_replay_round2.json",
    token: notes / "stage4_prime_token_conservation_round2.json",
    remediation: notes / "stage4_prime_role_separation_remediation_round2.json",
    completion: notes / "stage4_prime_completion_report_round2.md",
    raw_replay: notes / "stage4_prime_literature_replay_round2.raw.json",
    screening: notes / "stage4_prime_literature_screening_ledger_round2.json",
    matrix: notes / config[:matrix_file],
    verification: notes / config[:verification_file],
    versioned_bib: notes / "stage4_prime_references_round2.bib",
    canonical_bib: paper_root / "paper/references.bib"
  }
  paths.each { |name, path| check.call("artifact exists: #{name}", File.file?(path), path.relative_path_from(ROOT).to_s) }

  patch_raw = File.binread(paths[:patch])
  patch = JSON.parse(patch_raw)
  draft_raw = File.binread(paths[:draft])
  report = json(paths[:report])
  check.call("final patch SHA-256", sha(paths[:patch]) == config[:patch_sha], sha(paths[:patch]))
  check.call("final draft SHA-256", sha(paths[:draft]) == config[:draft_sha], sha(paths[:draft]))
  check.call("final apply-report SHA-256", sha(paths[:report]) == config[:report_sha], sha(paths[:report]))
  check.call("patch byte hygiene", patch_raw.bytes.count(13).zero? && control_byte_count(patch_raw).zero?, {"cr" => patch_raw.bytes.count(13), "other_control" => control_byte_count(patch_raw)})
  check.call("draft byte hygiene", draft_raw.bytes.count(13).zero? && control_byte_count(draft_raw).zero?, {"cr" => draft_raw.bytes.count(13), "other_control" => control_byte_count(draft_raw)})
  check.call("patch operation count", patch.fetch("ops").length == config[:ops], patch.fetch("ops").length)

  request_paper = request.fetch("papers").find { |entry| entry.fetch("paper_id") == paper_id }
  allowed = Hash.new { |hash, key| hash[key] = {} }
  request_paper.fetch("items").each do |item|
    item.fetch("proposed_targets").each do |target|
      target.fetch("allowed_operations").each do |operation|
        (allowed[target.fetch("block_id")][operation] ||= []) << item.fetch("item_id")
      end
    end
  end
  exact_scope = patch.fetch("ops").all? do |operation|
    item_ids = allowed.dig(operation.fetch("block_id"), operation.fetch("op")) || []
    !item_ids.empty? && operation.fetch("roadmap_item_ids").all? { |item_id| item_ids.include?(item_id) }
  end
  covered_items = patch.fetch("ops").flat_map { |operation| operation.fetch("roadmap_item_ids") }.uniq.sort
  expected_items = request_paper.fetch("items").map { |item| item.fetch("item_id") }.sort
  check.call("exact authorized target/operation scope", exact_scope)
  check.call("all authorized roadmap items covered", covered_items == expected_items, {"expected" => expected_items, "actual" => covered_items})
  empty_claim_changes = patch.fetch("ops").all? { |operation| operation.fetch("claim_strength_changes").empty? && operation.fetch("collateral_authorization_ids").empty? }
  check.call("no claim-strength or collateral mutation", empty_claim_changes)

  handoff = json(paths[:handoff])
  check.call("writer handoff binds final patch", handoff.dig("patch", "sha256") == config[:patch_sha] && handoff.dig("patch", "ops") == config[:ops])
  check.call("writer boundary forbids later stages", handoff.dig("boundaries", "stage4_5_or_later") == false && handoff.dig("boundaries", "route_state_change") == false)
  check.call("root apply patch binding", report.fetch("patch_digest") == config[:patch_sha])
  check.call("root apply output binding", report.fetch("output_draft_hash") == config[:draft_sha][0, 12])
  check.call("authorization witness", report.dig("authorization_witness", "status") == "pass" && report.dig("authorization_witness", "registered_claim_surfaces_checked").zero?)
  counters = report.fetch("counters")
  check.call("apply preservation counters", counters.fetch("blocks_total") == config[:blocks_total] && counters.fetch("blocks_preserved_byte_identical") == config[:blocks_preserved], counters)
  check.call("apply op count", report.fetch("ops_applied").length == config[:ops])

  remediation = json(paths[:remediation])
  final_attempt = remediation.fetch("attempts").last
  check.call("writer/apply role separation", final_attempt.fetch("writer_context") == "/root/r10_stage4_prime_p30_p31" && final_attempt.fetch("applier_context") == "/root")
  check.call("remediation final chain bindings", final_attempt.fetch("patch_sha256") == config[:patch_sha] && final_attempt.fetch("draft_sha256") == config[:draft_sha] && final_attempt.fetch("apply_report_sha256") == config[:report_sha])
  check.call("superseded attempts excluded", remediation.fetch("final_chain_uses_superseded_attempt") == false)

  replay = json(paths[:raw_replay])
  screening = json(paths[:screening])
  matrix = json(paths[:matrix])
  check.call("literature replay row count", replay.fetch("rows").length == config[:replay_rows], replay.fetch("rows").length)
  check.call("literature replay HTTP completion", replay.fetch("rows").all? { |row| row.dig("crossref", "http_status") == 200 })
  check.call("screening ledger row count", screening.fetch("row_count") == config[:replay_rows] && screening.fetch("rows").length == config[:replay_rows])
  check.call("screening changed no science/results", screening.fetch("scientific_result_changed") == false && screening.fetch("canonical_result_refreshed") == false)
  check.call("passage matrix row count", matrix.fetch("row_count") == config[:matrix_rows] && matrix.fetch("rows").length == config[:matrix_rows])
  verification = json(paths[:verification])
  check.call("source verification", verification.fetch("verdict") == "PASS" && verification.fetch("records").all? { |record| record.fetch("verdict") == "VERIFIED" })

  check.call("canonical bibliography entry count", bib_entry_count(paths[:canonical_bib]) == config[:canonical_bib_entries])
  check.call("versioned bibliography adds exactly two", bib_entry_count(paths[:versioned_bib]) == config[:versioned_bib_entries])
  bib_text = File.read(paths[:versioned_bib])
  check.call("authorized new bibliography keys present", config[:new_keys].all? { |key| bib_text.match?(/^@\w+\{#{Regexp.escape(key)},/) })

  response = json(paths[:response])
  check.call("Schema-8 response completion", response.fetch("items").length == config[:response_items] && response.fetch("items").all? { |item| item.fetch("status") == "RESOLVED" })
  claim = json(paths[:claim_replay])
  check.call("registered claim replay 0/0", claim.fetch("surface_count").zero? && claim.fetch("exact_once_same_block_count").zero? && claim.fetch("verdict") == "PASS_EMPTY_REGISTERED_POPULATION")
  token = json(paths[:token])
  token_safe = token.fetch("op_reports").length == config[:ops] && token.fetch("op_reports").all? do |row|
    row.dig("delta", "citations_delta", "removed").empty? && row.dig("delta", "citations_delta", "added").empty? &&
      row.dig("delta", "protected_terms_delta", "removed").empty? && row.dig("delta", "protected_terms_delta", "added").empty?
  end
  check.call("token advisory has no citation/protected-term drift", token_safe)

  stdout, stderr, status = Open3.capture3("python", ROADMAP_TOOL.to_s, "validate-bundle", paths[:bundle].to_s, "--root", paper_root.to_s)
  check.call("official evidence-bundle validation", status.success? && stdout.include?("revision evidence bundle ok"), {"exit_code" => status.exitstatus, "stdout" => stdout.strip, "stderr" => stderr.strip})
  support = json(paths[:support])
  check.call("support bundle boundary", support.fetch("verdict") == "STAGE4_PRIME_EVIDENCE_BOUND" && support.fetch("scientific_value_changed") == false && support.fetch("canonical_result_refreshed") == false && support.fetch("route_tuple_changed") == false && support.fetch("stage4_5_invoked") == false && support.fetch("stage5_invoked") == false)

  build = json(paths[:build_receipt])
  build_clean = build.fetch("status") == "PASS" && build.fetch("pages") == config[:pages] &&
                build.fetch("compiler_exit_codes_all_zero") == true &&
                %w[undefined_citations undefined_references missing_characters fatal_errors overfull_hboxes].all? { |key| build.fetch(key).zero? }
  check.call("isolated four-command preview build", build_clean, build.slice("status", "pages", "undefined_citations", "undefined_references", "missing_characters", "fatal_errors", "overfull_hboxes"))
  log_text = File.read(paths[:build_log])
  check.call("build-log lint", !log_text.match?(/Overfull \\hbox|Fatal error|Emergency stop|Missing character:/i))
  _pdf_stdout, pdf_stderr, pdf_status = Open3.capture3("pdfinfo", paths[:pdf].to_s)
  check.call("preview PDF parse", pdf_status.success?, pdf_stderr.strip)
  completion = File.read(paths[:completion])
  check.call("completion report binds patch and stage boundary", completion.include?(config[:patch_sha]) && completion.include?("Stage 4.5 remains uninvoked"))

  if paper_id == "P30"
    all_new_text = patch.fetch("ops").map { |operation| operation.fetch("new_text", "") }.join("\n")
    raw_texttt_underscores = all_new_text.scan(/\\texttt\{([^}]*)\}/m).flatten.sum { |inner| inner.scan(/(?<!\\)_/).length }
    block84 = patch.fetch("ops").find { |operation| operation.fetch("block_id") == "B0084" }.fetch("new_text")
    block103 = patch.fetch("ops").find { |operation| operation.fetch("block_id") == "B0103" }.fetch("new_text")
    check.call("P30 texttt underscore lint", raw_texttt_underscores.zero?, raw_texttt_underscores)
    check.call("P30 B0084 math-mode restoration", %w[\\rho \\( \\) \\[ \\] \\Omega \\leq \\sup].all? { |token_value| block84.include?(token_value) })
    check.call("P30 B0103 math-mode restoration", block103.include?("\\(\\Omega\\)") && block103.include?("\\(\\eta_c=1/100\\)"))
  else
    archived = json(notes / "stage4_prime_layout_superseded_20260904/stage4_prime_revision_patch_round2.json")
    old_ops = archived.fetch("ops").to_h { |operation| [operation.fetch("block_id"), operation.fetch("new_text")] }
    new_ops = patch.fetch("ops").to_h { |operation| [operation.fetch("block_id"), operation.fetch("new_text")] }
    changed = new_ops.keys.select { |block_id| new_ops.fetch(block_id) != old_ops.fetch(block_id) }
    check.call("P31 layout repair exact blocks", changed == %w[B0079 B0105], changed)
    semantics_equal = changed.all? { |block_id| semantic_layout_normalize(new_ops.fetch(block_id)) == semantic_layout_normalize(old_ops.fetch(block_id)) }
    check.call("P31 layout repair semantic preservation", semantics_equal)
  end

  failures = checks.reject { |row| row.fetch("status") == "PASS" }
  receipt = {
    "schema_version" => "round10-stage4-prime-final-audit/1.0",
    "paper_id" => paper_id,
    "audited_at_utc" => Time.now.utc.iso8601,
    "scope" => "final Track-A Stage 4-prime chain only; no Stage 4.5/5 or Route mutation",
    "checks_total" => checks.length,
    "checks_passed" => checks.length - failures.length,
    "checks_failed" => failures.length,
    "checks" => checks,
    "verdict" => failures.empty? ? "PASS" : "FAIL"
  }
  output = notes / "stage4_prime_final_audit_round2.json"
  File.binwrite(output, JSON.pretty_generate(receipt) + "\n")
  puts "#{paper_id}: #{receipt.fetch("verdict")} #{receipt.fetch("checks_passed")}/#{receipt.fetch("checks_total")} -> #{output}"
  all_failures.concat(failures.map { |failure| failure.merge("paper_id" => paper_id) })
end

unless all_failures.empty?
  warn JSON.pretty_generate(all_failures)
  exit 1
end
