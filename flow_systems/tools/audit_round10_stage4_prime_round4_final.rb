#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "pathname"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_FINAL_AUDIT.json")
MARKER = "<!-- ROUND10_STAGE4_PRIME_ROUND4_STATUS_SYNC_20260904 -->"
OLD_MARKER = "<!-- ROUND10_STAGE3_PRIME_ROUND3_STATUS_SYNC_20260903 -->"

class Audit
  attr_reader :categories, :failures

  def initialize
    @categories = Hash.new { |hash, key| hash[key] = { "checks" => 0, "passed" => 0, "failed" => 0 } }
    @failures = []
  end

  def check(category, id, actual, expected = true)
    row = @categories[category]
    row["checks"] += 1
    if actual == expected
      row["passed"] += 1
    else
      row["failed"] += 1
      @failures << { "category" => category, "id" => id, "expected" => expected, "actual" => actual }
    end
  end

  def total
    @categories.values.sum { |row| row.fetch("checks") }
  end

  def passed
    @categories.values.sum { |row| row.fetch("passed") }
  end
end

def load_json(path)
  JSON.parse(File.binread(File.join(ROOT, path)))
end

def sha(path)
  Digest::SHA256.file(File.join(ROOT, path)).hexdigest
end

def read_text(path)
  File.binread(File.join(ROOT, path)).force_encoding("UTF-8")
end

def collect_artifact_records(object, result = [])
  case object
  when Hash
    if object["path"].is_a?(String) && object["sha256"].is_a?(String)
      result << object
    end
    object.each_value { |value| collect_artifact_records(value, result) }
  when Array
    object.each { |value| collect_artifact_records(value, result) }
  end
  result
end

audit = Audit.new

report_path = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md"
receipt_path = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json"
checkpoint_path = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md"
freeze_path = "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json"

receipt = load_json(receipt_path)
report_sha = sha(report_path)
receipt_sha = sha(receipt_path)
checkpoint = read_text(checkpoint_path)

audit.check("terminal", "receipt schema", receipt.fetch("schema_version"), "round10-stage4-prime-and-round4-completion-receipt/1.0")
audit.check("terminal", "receipt status", receipt.fetch("status"), "THREE_TRACKS_CLOSED_AWAITING_MANDATORY_AUTHOR_CHECKPOINT")
audit.check("terminal", "receipt report hash", receipt.dig("completion_report", "sha256"), report_sha)
audit.check("terminal", "checkpoint report hash", checkpoint.include?(report_sha))
audit.check("terminal", "checkpoint receipt hash", checkpoint.include?(receipt_sha))
audit.check("terminal", "checkpoint short confirmation", checkpoint.include?("**`确认`**"))
audit.check("terminal", "checkpoint P29/P32", checkpoint.include?("P29/P32 — execute Stage 4′"))
audit.check("terminal", "checkpoint P30/P31", checkpoint.include?("P30/P31 — start fresh Stage 4.5"))
audit.check("terminal", "checkpoint P33", checkpoint.include?("P33 — start a wholly fresh Stage 3′ Round 5"))

# Replay every hash-and-byte witness carried by the completion receipt.
receipt_records = collect_artifact_records(receipt).uniq { |row| [row["path"], row["sha256"], row["bytes"]] }
receipt_records.each do |record|
  path = record.fetch("path")
  absolute = File.join(ROOT, path)
  audit.check("receipt_artifacts", "#{path} exists", File.file?(absolute))
  next unless File.file?(absolute)

  audit.check("receipt_artifacts", "#{path} hash", Digest::SHA256.file(absolute).hexdigest, record.fetch("sha256"))
  audit.check("receipt_artifacts", "#{path} bytes", File.size(absolute), record.fetch("bytes")) if record.key?("bytes")
end

# Independently replay all 92 frozen paths without rewriting the earlier receipt.
freeze = load_json(freeze_path)
frozen_records = collect_artifact_records(freeze).uniq { |row| row.fetch("path") }
audit.check("frozen_boundary", "unique frozen paths", frozen_records.length, 92)
frozen_records.each do |record|
  path = record.fetch("path")
  absolute = File.join(ROOT, path)
  audit.check("frozen_boundary", "#{path} exists", File.file?(absolute))
  next unless File.file?(absolute)

  audit.check("frozen_boundary", "#{path} hash", Digest::SHA256.file(absolute).hexdigest, record.fetch("sha256"))
  audit.check("frozen_boundary", "#{path} bytes", File.size(absolute), record.fetch("bytes"))
end
canonical_count = freeze.fetch("papers").sum { |paper| paper.fetch("canonical_files").length }
audit.check("frozen_boundary", "canonical file count", canonical_count, 15)
audit.check("frozen_boundary", "Route A hash", sha("skills/route-a-evaluator.md"), "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c")
audit.check("frozen_boundary", "Route B hash", sha("skills/route-b-evaluator.md"), "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595")

# P29/P32 remains request-only.
request = load_json("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json")
request_validation = load_json("BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json")
audit.check("p29_p32_request", "request status", request.fetch("status"), "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION")
audit.check("p29_p32_request", "validation status", request_validation.fetch("status"), "PASS")
{
  "residual_roadmap_items" => 11,
  "round3_regression_issues" => 1,
  "exact_target_entries" => 26,
  "block_operation_pairs" => 36,
  "supporting_operations" => 6,
  "registered_claim_surfaces" => 0,
  "validation_checks" => 377,
  "current_manuscript_writes" => 0,
  "current_bibliography_writes" => 0,
  "current_pdf_builds" => 0,
  "current_scientific_executions" => 0,
  "route_changes" => 0
}.each do |key, expected|
  audit.check("p29_p32_request", key, request_validation.fetch(key), expected)
end
request.fetch("papers").each do |paper|
  %w[proposed_patch_path proposed_output_draft_path].each do |key|
    path = paper.fetch(key)
    audit.check("p29_p32_request", "#{paper.fetch('paper_id')} #{key} absent", File.exist?(File.join(ROOT, path)), false)
  end
end

# P30/P31 final patch, apply, audit, and build semantics.
paper_specs = {
  30 => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    operations: 14,
    audit_checks: 86,
    blocks_total: 127,
    blocks_preserved: 113,
    pages: 16,
    queries: 54,
    matrix_file: "stage4_prime_claim_passage_matrix_round2.json",
    matrix_rows: 28
  },
  31 => {
    slug: "31-level11-conjugacy-owner-ledger",
    operations: 20,
    audit_checks: 85,
    blocks_total: 111,
    blocks_preserved: 93,
    pages: 13,
    queries: 20,
    matrix_file: "stage4_prime_method_passage_matrix_round2.json",
    matrix_rows: 24
  }
}

paper_specs.each do |number, spec|
  prefix = "papers/#{spec.fetch(:slug)}/notes"
  patch = load_json("#{prefix}/stage4_prime_revision_patch_round2.json")
  apply = load_json("#{prefix}/stage4_prime_revision_round2.tex.apply-report.json")
  final_audit = load_json("#{prefix}/stage4_prime_final_audit_round2.json")
  build = load_json("#{prefix}/stage4_prime_preview_build_receipt_round2.json")
  ledger = load_json("#{prefix}/stage4_prime_literature_screening_ledger_round2.json")
  matrix = load_json("#{prefix}/#{spec.fetch(:matrix_file)}")

  audit.check("p#{number}", "patch operations", patch.fetch("ops").length, spec.fetch(:operations))
  audit.check("p#{number}", "apply operations", apply.fetch("ops_applied").length, spec.fetch(:operations))
  audit.check("p#{number}", "apply witness", apply.dig("authorization_witness", "status"), "pass")
  audit.check("p#{number}", "blocks total", apply.dig("counters", "blocks_total"), spec.fetch(:blocks_total))
  audit.check("p#{number}", "blocks preserved", apply.dig("counters", "blocks_preserved_byte_identical"), spec.fetch(:blocks_preserved))
  audit.check("p#{number}", "final audit", final_audit.fetch("verdict"), "PASS")
  audit.check("p#{number}", "final audit total", final_audit.fetch("checks_total"), spec.fetch(:audit_checks))
  audit.check("p#{number}", "final audit passed", final_audit.fetch("checks_passed"), spec.fetch(:audit_checks))
  audit.check("p#{number}", "final audit failed", final_audit.fetch("checks_failed"), 0)
  audit.check("p#{number}", "build status", build.fetch("status"), "PASS")
  audit.check("p#{number}", "preview pages", build.fetch("pages"), spec.fetch(:pages))
  %w[undefined_citations undefined_references missing_characters fatal_errors overfull_hboxes].each do |key|
    audit.check("p#{number}", "build #{key}", build.fetch(key), 0)
  end
  audit.check("p#{number}", "citation style", build.fetch("citation_style"), "plainnat_numeric_current")
  audit.check("p#{number}", "ledger queries", ledger.fetch("rows").length, spec.fetch(:queries))
  audit.check("p#{number}", "ledger all HTTP 200", ledger.fetch("rows").all? { |row| row.fetch("http_status") == 200 })
  matrix_rows = matrix["rows"] || matrix["entries"] || matrix["matrix"]
  audit.check("p#{number}", "matrix rows", matrix_rows.length, spec.fetch(:matrix_rows))
  audit.check("p#{number}", "no claim-strength changes", patch.fetch("ops").all? { |op| op.fetch("claim_strength_changes").empty? })
  audit.check("p#{number}", "no collateral changes", patch.fetch("ops").all? { |op| op.fetch("collateral_authorization_ids").empty? })

  support = load_json("#{prefix}/stage4_prime_support_evidence_bundle_round2.json")
  support_records = collect_artifact_records(support).uniq { |row| [row.fetch("path"), row.fetch("sha256")] }
  audit.check("p#{number}_support", "support witness count", support_records.length, 29)
  paper_root = File.join(ROOT, "papers", spec.fetch(:slug))
  notes_root = File.join(paper_root, "notes")
  support_records.each do |record|
    record_path = record.fetch("path")
    # Bundle-local authority links use ../../../ from notes/, while the
    # revision/support records use paper-root-relative notes/... paths.
    resolution_root = record_path.start_with?("../") ? notes_root : paper_root
    absolute = File.expand_path(record_path, resolution_root)
    audit.check("p#{number}_support", "#{record.fetch('path')} exists", File.file?(absolute))
    next unless File.file?(absolute)
    audit.check("p#{number}_support", "#{record.fetch('path')} hash", Digest::SHA256.file(absolute).hexdigest, record.fetch("sha256"))
    audit.check("p#{number}_support", "#{record.fetch('path')} bytes", File.size(absolute), record.fetch("bytes")) if record.key?("bytes")
  end
end

# Official ARS authority validators are rerun read-only.
ars_script = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/scripts/revision_roadmap.py"
paper_specs.each do |number, spec|
  paper_root = File.join(ROOT, "papers", spec.fetch(:slug))
  stdout, stderr, status = Open3.capture3("python", ars_script, "validate-bundle", "--root", ".", "notes/stage4_prime_revision_evidence_bundle_round2.json", chdir: paper_root)
  audit.check("ars_official", "P#{number} bundle exit", status.exitstatus, 0)
  audit.check("ars_official", "P#{number} bundle output", "#{stdout}#{stderr}".include?("revision evidence bundle ok"))

  args = [
    "python", ars_script, "validate-adjudication",
    "--base", "notes/stage4_revision_round1.tex",
    "--block-manifest", "notes/stage4_prime_base.block-manifest.json",
    "--claim-surface", "notes/stage4_prime_claim_surface_manifest.json",
    "--artifact-root", ".",
    "notes/stage4_prime_revision_roadmap.json",
    "notes/stage4_prime_author_adjudication.json"
  ]
  stdout, stderr, status = Open3.capture3(*args, chdir: paper_root)
  audit.check("ars_official", "P#{number} adjudication exit", status.exitstatus, 0)
  audit.check("ars_official", "P#{number} adjudication output", "#{stdout}#{stderr}".include?("author adjudication ok"))
end

# P33's first immutable Phase-2A record must remain invalid and noncontrolling.
p33_validation = load_json("papers/33-bolza-control-matched-census/notes/stage3_prime_round4_phase2a_validation.json")
p33_completion = load_json("papers/33-bolza-control-matched-census/notes/stage3_prime_round4_completion_receipt.json")
audit.check("p33", "Phase-2A status", p33_validation.fetch("status"), "FAIL")
audit.check("p33", "schema errors", p33_validation.dig("schema_validation", "error_count"), 35)
audit.check("p33", "immutable verdict", p33_validation.dig("phase2a_record", "immutable_after_first_emission"), true)
audit.check("p33", "retry unused", p33_validation.dig("phase2a_record", "retry_used"), false)
audit.check("p33", "FULL noncontrolling", p33_validation.dig("phase2a_record", "semantic_counts_noncontrolling", "FULLY_ADDRESSED"), 5)
audit.check("p33", "PARTIAL noncontrolling", p33_validation.dig("phase2a_record", "semantic_counts_noncontrolling", "PARTIALLY_ADDRESSED"), 8)
audit.check("p33", "completion status", p33_completion.fetch("status"), "ABORTED")
audit.check("p33", "terminal token", p33_completion.fetch("terminal_marker"), "[RE-REVIEW-ABORT: phase2a_lint_failed]")
audit.check("p33", "official checker", p33_completion.fetch("official_checker_status"), "NOT_RUN")
audit.check("p33", "decision not emitted", p33_completion.fetch("decision_emitted"), false)
audit.check("p33", "Round-3 files rehashed", p33_completion.fetch("round3_files_rehashed"), 37)

schema_path = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars/shared/contracts/re_review/verdict_record.schema.json"
verdict_path = File.join(ROOT, "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_verdict_record.json")
python = <<~PY
  import json, sys
  from jsonschema import Draft202012Validator
  schema = json.load(open(sys.argv[1], "r", encoding="utf-8"))
  instance = json.load(open(sys.argv[2], "r", encoding="utf-8"))
  print(len(list(Draft202012Validator(schema).iter_errors(instance))))
PY
stdout, stderr, status = Open3.capture3("python", "-c", python, schema_path, verdict_path)
audit.check("p33", "independent schema recount exit", status.exitstatus, 0)
audit.check("p33", "independent schema recount", stdout.strip.to_i, 35)
audit.check("p33", "independent schema stderr", stderr, "")

p33_forbidden = Dir.glob(File.join(ROOT, "papers/33-bolza-control-matched-census/notes/stage3_prime_round4_*"))
  .select { |path| File.basename(path).match?(/response|phase2b|traceability|decision/) }
audit.check("p33", "forbidden downstream artifacts", p33_forbidden, [])

# Fresh independent marker-stripped builds.
independent_builds = {}
Dir.mktmpdir("round10-stage4-prime-final-audit-") do |temporary_root|
  paper_specs.each do |number, spec|
    prefix = File.join(ROOT, "papers", spec.fetch(:slug), "notes")
    build_dir = File.join(temporary_root, "p#{number}")
    Dir.mkdir(build_dir)
    source = File.binread(File.join(prefix, "stage4_prime_revision_round2.tex"))
    stripped = source.lines.reject { |line| line.match?(/^<!--block:B[0-9]+-->\s*$/) }.join
    File.binwrite(File.join(build_dir, "main.tex"), stripped)
    FileUtils.cp(File.join(prefix, "stage4_prime_references_round2.bib"), File.join(build_dir, "references.bib"))

    commands = [
      %w[lualatex -interaction=nonstopmode -halt-on-error main.tex],
      %w[bibtex main],
      %w[lualatex -interaction=nonstopmode -halt-on-error main.tex],
      %w[lualatex -interaction=nonstopmode -halt-on-error main.tex]
    ]
    exits = commands.map do |command|
      _stdout, _stderr, status = Open3.capture3(*command, chdir: build_dir)
      status.exitstatus
    end
    log = File.file?(File.join(build_dir, "main.log")) ? File.binread(File.join(build_dir, "main.log")) : ""
    pdfinfo, _pdferr, pdfstatus = Open3.capture3("pdfinfo", "main.pdf", chdir: build_dir)
    pages = pdfinfo[/^Pages:\s+(\d+)/, 1]&.to_i
    counters = {
      "undefined_citations" => log.scan(/Citation.*undefined|There were undefined citations/).length,
      "undefined_references" => log.scan(/Reference.*undefined|There were undefined references/).length,
      "missing_characters" => log.scan(/Missing character/).length,
      "fatal_errors" => log.scan(/Fatal error occurred|Emergency stop/).length,
      "overfull_hboxes" => log.scan(/Overfull \\hbox/).length,
      "underfull_hboxes" => log.scan(/Underfull \\hbox/).length
    }
    independent_builds["P#{number}"] = {
      "compiler_sequence" => %w[lualatex bibtex lualatex lualatex],
      "exit_codes" => exits,
      "pdfinfo_exit" => pdfstatus.exitstatus,
      "pages" => pages,
      "counters" => counters,
      "pdf_sha256" => File.file?(File.join(build_dir, "main.pdf")) ? Digest::SHA256.file(File.join(build_dir, "main.pdf")).hexdigest : nil,
      "pdf_byte_reproducibility_claimed" => false
    }
    audit.check("independent_build", "P#{number} compiler exits", exits, [0, 0, 0, 0])
    audit.check("independent_build", "P#{number} pdfinfo exit", pdfstatus.exitstatus, 0)
    audit.check("independent_build", "P#{number} pages", pages, spec.fetch(:pages))
    %w[undefined_citations undefined_references missing_characters fatal_errors overfull_hboxes].each do |key|
      audit.check("independent_build", "P#{number} #{key}", counters.fetch(key), 0)
    end
  end
end

# Current status surfaces and all local Markdown links.
status_files = ["README.md"] + paper_specs.values.map { |spec| spec.fetch(:slug) }
  .concat(%w[29-bianchi-ideal-owner-refinement 32-homology-cover-renormalization-uniformity 33-bolza-control-matched-census])
  .uniq
  .flat_map do |slug|
    ["papers/#{slug}/README.md", "papers/#{slug}/notes/pipeline_state.md", "papers/#{slug}/paper/README.md"]
  end
audit.check("status_sync", "status file count", status_files.length, 16)
states = {
  "29-bianchi-ideal-owner-refinement" => "stage4_prime_request_prepared_awaiting_exact_authorization",
  "30-three-disk-nonconstant-roof-determinant" => "stage4_prime_author_side_complete_awaiting_stage4_5_authorization",
  "31-level11-conjugacy-owner-ledger" => "stage4_prime_author_side_complete_awaiting_stage4_5_authorization",
  "32-homology-cover-renormalization-uniformity" => "stage4_prime_request_prepared_awaiting_exact_authorization",
  "33-bolza-control-matched-census" => "stage3_prime_round4_aborted_phase2a_lint_failed_awaiting_fresh_round5_authorization"
}
status_files.each do |path|
  text = read_text(path)
  audit.check("status_sync", "#{path} current marker", text.scan(Regexp.new(Regexp.escape(MARKER))).length, 1)
  audit.check("status_sync", "#{path} no stale marker", text.include?(OLD_MARKER), false)
  unless path == "README.md"
    slug = path.split("/")[1]
    audit.check("status_sync", "#{path} current state", text.include?(states.fetch(slug)))
    audit.check("status_sync", "#{path} Route boundary", text.include?("Route"))
    audit.check("status_sync", "#{path} citation style", text.include?("plainnat"))
    audit.check("status_sync", "#{path} conclusion summary", text.include?("结论概要")) unless path.end_with?("notes/pipeline_state.md")
  end
end

current_hashes = [report_sha, receipt_sha, sha(checkpoint_path)]
states.each_key do |slug|
  paths = ["papers/#{slug}/README.md", "papers/#{slug}/notes/pipeline_state.md", "papers/#{slug}/paper/README.md"]
  paths.each do |path|
    text = read_text(path)
    current_hashes.each do |digest|
      audit.check("status_bindings", "#{path} binds #{digest[0, 12]}", text.include?(digest))
    end
  end
end

link_count = 0
status_files.each do |path|
  text = read_text(path)
  text.scan(/\[[^\]]*\]\(([^)]+)\)/).flatten.each do |target|
    next if target.match?(/\A(?:https?:|mailto:|#)/)
    target = target.sub(/\A</, "").sub(/>\z/, "").split("#", 2).first
    next if target.empty?
    link_count += 1
    resolved = File.expand_path(target, File.dirname(File.join(ROOT, path)))
    audit.check("markdown_links", "#{path} -> #{target}", File.exist?(resolved))
  end
end

later_stage_files = states.keys.flat_map do |slug|
  Dir.glob(File.join(ROOT, "papers", slug, "notes", "*"))
    .select { |path| File.basename(path).match?(/stage4_5|stage5|stage6/i) }
end
audit.check("scope", "later-stage files absent", later_stage_files, [])
audit.check("scope", "Route-A tuple remains 0/5", receipt.dig("route", "formal_route_a_tuples"), "0/5")
audit.check("scope", "positive arithmetic A2 remains 0/5", receipt.dig("route", "positive_arithmetic_a2"), "0/5")
audit.check("scope", "Route B remains 0/5", receipt.dig("route", "route_b_invocations"), "0/5")
audit.check("scope", "canonical 15/15 unchanged", receipt.dig("write_boundary", "canonical_manuscript_bibliography_pdf_files_unchanged"), "15/15")
audit.check("scope", "no new scientific execution", receipt.dig("write_boundary", "new_scientific_execution"), false)
audit.check("scope", "no result refresh", receipt.dig("write_boundary", "result_refresh"), false)

result = {
  "schema_version" => "round10-stage4-prime-and-round4-final-audit/1.0",
  "generated_date_utc" => "2026-09-04",
  "status" => audit.failures.empty? ? "PASS" : "FAIL",
  "checks_total" => audit.total,
  "checks_passed" => audit.passed,
  "checks_failed" => audit.failures.length,
  "categories" => audit.categories.sort.to_h,
  "failures" => audit.failures,
  "frozen_paths_replayed" => frozen_records.length,
  "completion_receipt_artifact_witnesses" => receipt_records.length,
  "support_bundle_witnesses" => { "P30" => 29, "P31" => 29 },
  "status_documents" => status_files.length,
  "local_markdown_links_checked" => link_count,
  "independent_builds" => independent_builds,
  "p33_independent_schema_error_recount" => stdout.strip.to_i,
  "official_ars_validators" => {
    "P30_bundle" => "PASS",
    "P30_adjudication" => "PASS",
    "P31_bundle" => "PASS",
    "P31_adjudication" => "PASS"
  },
  "route_state" => {
    "formal_route_a_tuples" => "0/5",
    "positive_arithmetic_a2" => "0/5",
    "a3" => "0/5",
    "a4" => "0/5",
    "route_b" => "0/5"
  },
  "next_checkpoint" => {
    "path" => checkpoint_path,
    "sha256" => sha(checkpoint_path),
    "confirmation_token" => "确认"
  }
}

File.binwrite(OUTPUT, "#{JSON.pretty_generate(result)}\n")
puts "#{result.fetch('status')} -- #{result.fetch('checks_passed')}/#{result.fetch('checks_total')} checks; #{link_count} local Markdown links; #{frozen_records.length} frozen paths"
exit 1 unless audit.failures.empty?
