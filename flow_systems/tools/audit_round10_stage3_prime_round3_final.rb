#!/usr/bin/env ruby
# frozen_string_literal: true

# Terminal, fail-closed integrity audit for Round 10 / Stage 3-prime Round 3.
# It replays the deterministic validators, runs the official ARS checker in a
# temporary comparison directory, validates the eleven applicable contracts,
# and binds the post-round README/status surfaces without editing science or
# canonical paper files.

require "digest"
require "fileutils"
require "json"
require "open3"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite"
CONTRACTS = File.join(ARS_ROOT, "ars/shared/contracts/re_review")
OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_AUDIT.json")
RECEIPT_OUTPUT = File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_RECEIPT.json")
MARKER = "<!-- ROUND10_STAGE3_PRIME_ROUND3_STATUS_SYNC_20260903 -->"

EXPECTED = {
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md" => "c122ca7f070a20568e47fab8999d6a3bf106b29da21f1dc8bca056b2c1ce5432",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md" => "dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json" => "ad20c4331936d2d8e1fb55613f72c3cf6bb5d07852775a47071ac427a9107172",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_VALIDATION.json" => "319751760fdd36c8152bc56581ee9ff2c5dce173de503e651f09e05860a6b4a9",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_VALIDATION.json" => "6ad085540923a5758728196ff0088e631520d8a482a0c4cc7b9aef362e508248",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2B_INTEGRATION_VALIDATION.json" => "3e3abde9875b01259177ed9877b57cad2abb17e9002f17b127bcd1105442dd40",
  "BATCH_ROUND10_STAGE3_PRIME_ROUND3_BOUNDARY_VALIDATION.json" => "885e2ef06473601b6a4999e0e3e347f1bd2164f74576b465c97a3b8843728275",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json" => "a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md" => "4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json" => "52739c5ef1cb2a8142feadb73945fbcbe06a551f43d37fc2e0022b497c6a645c",
  "skills/route-a-evaluator.md" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
  "skills/route-b-evaluator.md" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
}.freeze

PAPERS = {
  "P29" => {
    slug: "29-bianchi-ideal-owner-refinement",
    state: "stage3_prime_round3_major_revision_awaiting_stage4_prime_request_preparation_authorization",
    canonical: {
      "paper/manuscript.tex" => "5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034",
      "paper/references.bib" => "c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555",
      "paper/paper.pdf" => "14dd360e0152da9c976c88bfe3ca197449017d49e09ea75279d4099457f1044e"
    },
    outcome: [7, 4, 0], decision: "Major Revision", rule: "B4"
  },
  "P30" => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    state: "stage3_prime_round2_major_revision_stage4_prime_request_prepared_awaiting_exact_authorization",
    canonical: {
      "paper/manuscript.tex" => "af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506",
      "paper/references.bib" => "1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f",
      "paper/paper.pdf" => "c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e"
    },
    outcome: [4, 5, 0], decision: "Major Revision", rule: "B4"
  },
  "P31" => {
    slug: "31-level11-conjugacy-owner-ledger",
    state: "stage3_prime_round2_major_revision_stage4_prime_request_prepared_awaiting_exact_authorization",
    canonical: {
      "paper/manuscript.tex" => "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a",
      "paper/references.bib" => "b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958",
      "paper/paper.pdf" => "f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722"
    },
    outcome: [3, 8, 0], decision: "Major Revision", rule: "B4"
  },
  "P32" => {
    slug: "32-homology-cover-renormalization-uniformity",
    state: "stage3_prime_round3_major_revision_awaiting_stage4_prime_request_preparation_authorization",
    canonical: {
      "paper/manuscript.tex" => "4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a",
      "paper/references.bib" => "e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9",
      "paper/paper.pdf" => "66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93"
    },
    outcome: [5, 7, 0], decision: "Major Revision", rule: "B4"
  },
  "P33" => {
    slug: "33-bolza-control-matched-census",
    state: "stage3_prime_round3_aborted_awaiting_fresh_round4_authorization",
    canonical: {
      "paper/manuscript.tex" => "b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3",
      "paper/references.bib" => "12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0",
      "paper/paper.pdf" => "487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031"
    },
    outcome: [6, 6, 1], decision: nil, rule: nil
  }
}.freeze

REPLAY = [
  ["Phase-1 validator", "tools/audit_round10_stage3_prime_round3_phase1.rb", "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE1_VALIDATION.json"],
  ["Phase-2A validator", "tools/audit_round10_stage3_prime_round3_phase2a.rb", "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_VALIDATION.json"],
  ["Phase-2B validator", "tools/audit_round10_stage3_prime_round3_phase2b_integration.rb", "BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2B_INTEGRATION_VALIDATION.json"],
  ["boundary validator", "tools/audit_round10_stage3_prime_round3_boundaries.rb", "BATCH_ROUND10_STAGE3_PRIME_ROUND3_BOUNDARY_VALIDATION.json"],
  ["P30/P31 request validator", "tools/audit_round10_stage4_prime_authorization_request.rb", "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json"]
].freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
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

def resolve_path(reference)
  path = reference.start_with?("/") ? File.expand_path(reference) : File.expand_path(reference, ROOT)
  allowed = [ROOT, ARS_ROOT].any? { |base| path == base || path.start_with?("#{base}/") }
  raise "unsafe binding path #{reference}" unless allowed
  raise "missing or non-file binding #{reference}" unless File.file?(path) && !File.symlink?(path)
  path
end

def collect_bindings(value, trail = [], rows = [])
  case value
  when Hash
    if value["path"].is_a?(String)
      if value["sha256"].is_a?(String)
        rows << [trail.join("."), value.fetch("path"), "raw", value.fetch("sha256")]
      elsif value["raw_sha256"].is_a?(String)
        rows << [trail.join("."), value.fetch("path"), "raw", value.fetch("raw_sha256")]
      end
      if value["jcs_sha256"].is_a?(String)
        rows << [trail.join("."), value.fetch("path"), "jcs", value.fetch("jcs_sha256")]
      end
    end
    value.each { |key, child| collect_bindings(child, trail + [key], rows) }
  when Array
    value.each_with_index { |child, index| collect_bindings(child, trail + [index.to_s], rows) }
  end
  rows
end

def atomic_json(path, payload)
  temporary = "#{path}.tmp"
  raise "temporary output exists: #{temporary}" if File.exist?(temporary)
  File.binwrite(temporary, JSON.pretty_generate(payload) + "\n")
  File.rename(temporary, path)
end

failures = []
checks = []
check = lambda do |condition, label|
  condition ? checks << label : failures << label
end

EXPECTED.each do |relative, expected|
  path = File.join(ROOT, relative)
  check.call(File.file?(path) && !File.symlink?(path), "real frozen file: #{relative}")
  check.call(sha256(path) == expected, "frozen hash: #{relative}") if File.file?(path)
end

terminal = load_json(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json"))
check.call(terminal.fetch("status") == "PASS_WITH_ONE_FAIL_CLOSED_ABORT", "terminal receipt status")
check.call(terminal.dig("round3_aggregate", "papers_complete") == 2 && terminal.dig("round3_aggregate", "papers_aborted") == 1, "terminal 2 complete / 1 abort")
check.call(terminal.dig("round3_aggregate", "controlling_counts") == {
  "FULLY_ADDRESSED" => 18, "PARTIALLY_ADDRESSED" => 17, "NOT_ADDRESSED" => 1,
  "MADE_WORSE" => 0, "CANNOT_VERIFY" => 0
}, "terminal controlling aggregate 18/17/1")
check.call(terminal.dig("route_credit", "formal_route_a_tuples_assigned") == "0/5" &&
           terminal.dig("route_credit", "positive_arithmetic_a2") == "0/5" &&
           terminal.dig("route_credit", "route_b_invoked") == "0/5", "terminal Route boundary")

binding_rows = collect_bindings(terminal)
binding_rows.each do |label, reference, kind, expected|
  begin
    path = resolve_path(reference)
    actual = kind == "jcs" ? jcs_sha256(load_json(path)) : sha256(path)
    check.call(actual == expected, "receipt binding #{kind}: #{label}")
  rescue StandardError => error
    failures << "receipt binding #{kind}: #{label}: #{error.message}"
  end
end

replay_results = REPLAY.map do |label, script, output|
  stdout, stderr, status = Open3.capture3("ruby", File.join(ROOT, script), chdir: ROOT)
  expected = EXPECTED.fetch(output)
  unchanged = File.file?(File.join(ROOT, output)) && sha256(File.join(ROOT, output)) == expected
  check.call(status.success?, "#{label} replay exit")
  check.call(unchanged, "#{label} replay preserves frozen bytes")
  {"label" => label, "exit_code" => status.exitstatus, "stdout" => stdout.strip, "stderr" => stderr.strip, "frozen_output_sha256" => sha256(File.join(ROOT, output))}
end

schema_code = <<~'PY'
  import json, sys
  from pathlib import Path
  from jsonschema import Draft202012Validator
  root, contracts = map(Path, sys.argv[1:3])
  papers = {
      "P29": "29-bianchi-ideal-owner-refinement",
      "P32": "32-homology-cover-renormalization-uniformity",
      "P33": "33-bolza-control-matched-census",
  }
  names = {
      "input_manifest": "input_manifest.schema.json",
      "precommitment": "precommitment.schema.json",
      "verdict_record": "verdict_record.schema.json",
      "traceability": "traceability.schema.json",
  }
  passed, errors = 0, []
  for pid, slug in papers.items():
      kinds = ["input_manifest", "precommitment", "verdict_record"]
      if pid != "P33": kinds.append("traceability")
      for kind in kinds:
          value = json.loads((root / "papers" / slug / "notes" / f"stage3_prime_round3_{kind}.json").read_text())
          schema = json.loads((contracts / names[kind]).read_text())
          found = list(Draft202012Validator(schema).iter_errors(value))
          if found: errors.append(f"{pid}:{kind}:{found[0].message}")
          else: passed += 1
  print(json.dumps({"passed": passed, "total": 11, "errors": errors}))
  sys.exit(0 if passed == 11 and not errors else 1)
PY
schema_stdout, schema_stderr, schema_status = Open3.capture3("python", "-c", schema_code, ROOT, CONTRACTS)
schema_result = JSON.parse(schema_stdout) rescue {"passed" => 0, "total" => 11, "errors" => [schema_stderr]}
check.call(schema_status.success? && schema_result["passed"] == 11, "official contracts 11/11")

checker_results = []
Dir.mktmpdir("round3-final-checkers-") do |directory|
  stdout, stderr, status = Open3.capture3(
    "ruby", File.join(ROOT, "tools/run_round10_stage3_prime_round3_checkers.rb"),
    "--papers", "P29,P32", "--candidate-dir", directory, chdir: ROOT
  )
  check.call(status.success?, "official checker replay 2/2 exit")
  {"P29" => "29-bianchi-ideal-owner-refinement", "P32" => "32-homology-cover-renormalization-uniformity"}.each do |paper_id, slug|
    candidate = File.join(directory, "#{paper_id.downcase}_stage3_prime_round3_checker_receipt.json")
    frozen = File.join(ROOT, "papers", slug, "notes/stage3_prime_round3_checker_receipt.json")
    same = File.file?(candidate) && File.binread(candidate) == File.binread(frozen)
    check.call(same, "#{paper_id} official checker candidate equals frozen receipt")
    checker_results << {"paper_id" => paper_id, "candidate_equals_frozen" => same, "frozen_sha256" => sha256(frozen)}
  end
  checker_results << {
    "combined_exit_code" => status.exitstatus,
    "stdout" => stdout.gsub(directory, "<temporary-checker-dir>").strip,
    "stderr" => stderr.gsub(directory, "<temporary-checker-dir>").strip
  }
end

status_paths = ["README.md"] + PAPERS.values.flat_map do |paper|
  base = File.join("papers", paper.fetch(:slug))
  [File.join(base, "README.md"), File.join(base, "notes/pipeline_state.md"), File.join(base, "paper/README.md")]
end
check.call(status_paths.length == 16 && status_paths.uniq.length == 16, "exactly 16 status surfaces")
status_bindings = status_paths.map do |relative|
  path = File.join(ROOT, relative)
  text = File.binread(path).force_encoding("UTF-8")
  check.call(text.scan(MARKER).length == 1, "single Round-3 sync marker: #{relative}")
  check.call(text.include?("plainnat") || relative == "README.md", "citation style visible: #{relative}")
  {"path" => relative, "sha256" => sha256(path)}
end

root_readme = File.read(File.join(ROOT, "README.md"), encoding: "UTF-8")
check.call(root_readme.include?("18 FULL / 17 PARTIAL / 1 NOT"), "root README controlling aggregate")
check.call(root_readme.include?("formal Route-A") && root_readme.include?("0/5"), "root README Route-A location")
check.call(root_readme.include?("建议的下一组五篇动作"), "root README next-bundle summary")

canonical_bindings = []
PAPERS.each do |paper_id, paper|
  base = File.join(ROOT, "papers", paper.fetch(:slug))
  docs = [File.join(base, "README.md"), File.join(base, "notes/pipeline_state.md"), File.join(base, "paper/README.md")]
  check.call(docs.all? { |path| File.read(path, encoding: "UTF-8").include?(paper.fetch(:state)) }, "#{paper_id} status surfaces agree")
  check.call(File.read(File.join(base, "paper/README.md"), encoding: "UTF-8").include?("## 结论概要"), "#{paper_id} conclusion summary present")
  paper.fetch(:canonical).each do |relative, expected|
    path = File.join(base, relative)
    actual = sha256(path)
    check.call(actual == expected, "#{paper_id} canonical unchanged: #{relative}")
    canonical_bindings << {"paper_id" => paper_id, "path" => path.delete_prefix("#{ROOT}/"), "sha256" => actual}
  end
end

p33_notes = File.join(ROOT, "papers/33-bolza-control-matched-census/notes")
%w[phase2b_integration traceability].each do |suffix|
  check.call(!File.exist?(File.join(p33_notes, "stage3_prime_round3_#{suffix}.json")), "P33 forbidden successor absent: #{suffix}")
end
p33_checker = load_json(File.join(p33_notes, "stage3_prime_round3_checker_receipt.json"))
check.call(p33_checker["checker_status"] == "NOT_RUN" && p33_checker["decision_emitted"] == false, "P33 checker NOT_RUN and no decision")

request = load_json(File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json"))
request_validation = load_json(File.join(ROOT, "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json"))
check.call(request_validation["status"] == "PASS" && request_validation["residual_items"] == 13 && request_validation["manuscript_target_blocks"] == 37 && request_validation["validation_checks"] == 156, "P30/P31 request 13/37/156 PASS")
check.call(request_validation["manuscript_writes"] == 0 && request_validation["bibliography_writes"] == 0 && request_validation["route_changes"] == 0, "P30/P31 request has zero writes")
check.call(request["status"] == "AWAITING_EXPLICIT_AUTHOR_CONFIRMATION", "P30/P31 request awaits exact authorization")

audit = {
  "schema_version" => "round10-stage3-prime-round3-final-integrity-audit/1.0",
  "audited_at" => "2026-09-03T16:30:00Z",
  "status" => failures.empty? ? "PASS" : "FAIL",
  "scope" => "Round 10 Papers 29--33 Stage 3-prime Round 3 terminal state, P30/P31 request preparation, status synchronization, and frozen science/Route boundary",
  "checks_passed" => checks.length,
  "failures" => failures,
  "terminal_artifacts" => EXPECTED.map { |path, expected| {"path" => path, "sha256" => expected} },
  "terminal_receipt_bindings" => {"verified" => binding_rows.length, "failed" => failures.count { |item| item.start_with?("receipt binding") }},
  "validator_replays" => replay_results,
  "official_schema_validation" => schema_result.merge("status" => schema_status.success? ? "PASS" : "FAIL"),
  "official_checker_replay" => checker_results,
  "status_surfaces" => status_bindings,
  "canonical_files" => canonical_bindings,
  "papers" => PAPERS.map { |paper_id, paper| {"paper_id" => paper_id, "control_state" => paper.fetch(:state), "controlling_counts" => paper.fetch(:outcome), "decision" => paper.fetch(:decision), "rule" => paper.fetch(:rule)} },
  "totals" => {
    "papers" => 5,
    "round3_complete" => 2,
    "round3_aborted" => 1,
    "controlling_full" => 18,
    "controlling_partial" => 17,
    "controlling_not" => 1,
    "official_schema_passes" => schema_result["passed"],
    "official_checker_passes" => 2,
    "status_files_synchronized" => status_bindings.length,
    "canonical_files_unchanged" => canonical_bindings.length,
    "new_science_executions" => 0
  },
  "route_position" => {
    "roadmap" => "Route A",
    "formal_route_a_tuples" => "0/5",
    "positive_arithmetic_a2" => "0/5",
    "a3" => "0/5",
    "a4" => "0/5",
    "route_b" => "0/5"
  },
  "boundaries" => {
    "canonical_manuscript_bibliography_pdf_mutations" => failures.any? { |item| item.include?("canonical unchanged") } ? nil : 0,
    "science_or_result_mutations" => 0,
    "initial_system_mutations" => 0,
    "route_advancement" => "NONE",
    "p30_p31_stage4_prime_patch_authorized" => false,
    "p29_p32_stage4_prime_request_preparation_authorized" => false,
    "p33_round4_authorized" => false,
    "stage4_5_or_stage5_authorized" => false
  }
}
atomic_json(OUTPUT, audit)

receipt = {
  "schema_version" => "round10-stage3-prime-round3-final-integrity-receipt/1.0",
  "issued_at" => "2026-09-03T16:30:00Z",
  "status" => audit.fetch("status"),
  "final_integrity_audit" => {
    "path" => File.basename(OUTPUT),
    "sha256" => sha256(OUTPUT),
    "jcs_sha256" => jcs_sha256(load_json(OUTPUT))
  },
  "checks_passed" => checks.length,
  "failures" => failures,
  "terminal_receipt_bindings_verified" => binding_rows.length,
  "official_schema_passes" => schema_result["passed"],
  "eligible_checker_passes" => 2,
  "status_files_synchronized" => status_bindings.length,
  "canonical_files_unchanged" => canonical_bindings.length,
  "science_artifacts_created_or_refreshed" => 0,
  "route_or_initial_system_changes" => 0,
  "successor_bundle_authorized" => false,
  "closure_note" => "This receipt cannot bind its own hash; the publishing Git commit provides the external terminal binding."
}
atomic_json(RECEIPT_OUTPUT, receipt)

if failures.empty?
  puts "PASS -- Round 10 Stage 3-prime Round 3 final integrity: #{checks.length} checks; #{binding_rows.length} receipt bindings; 16 status files; 15 canonical files"
  exit 0
end

warn "FAIL -- Round 10 Stage 3-prime Round 3 final integrity: #{failures.join('; ')}"
exit 1
