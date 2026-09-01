#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND9_STAGE6_SKIP_RECEIPT.json")
RAW_EVENT = File.join(ROOT, "BATCH_ROUND9_STAGE6_SKIP_AUTHOR_EVENT_20260901.txt")
STAGE5_RECEIPT = File.join(ROOT, "BATCH_ROUND9_STAGE5_COMPLETION_RECEIPT.json")
EXPECTED_RAW_EVENT = "跳过，继续下一批\n".b
EXPECTED_RAW_EVENT_SHA256 = "eb65f3fe7e4fc530db88e71600b88c57c0174ca330b563b899031f9d20aa93da"
EXPECTED_STAGE5_RECEIPT_SHA256 = "53ad11010b8a9fa5064644c0ce9fea22666370b6d9f89ab623a5cf70f7b73018"

PAPERS = {
  24 => "24-bianchi-holonomy-flow",
  25 => "25-three-disk-scattering-flow",
  26 => "26-level11-newform-time-change",
  27 => "27-congruence-inverse-limit-no-go",
  28 => "28-bolza-magnetic-flow"
}.freeze

ROUTE_HASHES = {
  "skills/route-a-evaluator.md" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
  "skills/route-b-evaluator.md" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
}.freeze

# The Stage-5 receipt froze the hydrated local canonical trees, which include
# ignored LaTeX scratch files.  A fresh Git clone intentionally lacks those
# files.  Both byte-exact profiles are frozen here so the terminal audit is
# strict and reproducible in either environment without treating scratch files
# as scientific content.
CLEAN_REPOSITORY_CANONICAL_HASHES = {
  24 => "3b1fa5e278ed2b7dc2ac7b0e5ea7bb6b0733bb7a4bbf5c504feb69d5e281c63a",
  25 => "05d34059972e2d0dcaaea300e1f36f04a9441043fe4745cdca85c86fc2a1a49f",
  26 => "72c14f0257c985f01a921f7e223f2219cdf9093b5246a6523b399c6b3ba2cc74",
  27 => "664745a0073b2ef60cd33cb2a64d45295503a9f6540e3bbd29cf18ac8570593b",
  28 => "d9aa4a4a257d222e156d026f60b29fe8cc5dc1556bdf045b83303a63eec67f4f"
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def tree_sha256(relative_dir)
  absolute = File.join(ROOT, relative_dir)
  files = Dir.glob(File.join(absolute, "**", "*"), File::FNM_DOTMATCH)
             .select { |path| File.file?(path) }
             .sort
  ledger = files.map do |path|
    relative = path.delete_prefix("#{ROOT}/")
    "#{sha256(path)}  #{relative}\n"
  end.join
  Digest::SHA256.hexdigest(ledger)
end

checks = []
failures = []
record = lambda do |id, passed, detail = nil|
  row = {"id" => id, "status" => passed ? "PASS" : "FAIL"}
  row["detail"] = detail unless detail.nil? || detail.to_s.empty?
  checks << row
  failures << row unless passed
end

record.call("authority:raw-event-exists", File.file?(RAW_EVENT))
raw = File.binread(RAW_EVENT)
record.call("authority:raw-event-exact-bytes", raw == EXPECTED_RAW_EVENT,
            "bytes=#{raw.bytesize}")
record.call("authority:raw-event-sha256", sha256(RAW_EVENT) == EXPECTED_RAW_EVENT_SHA256,
            sha256(RAW_EVENT))
record.call("authority:stage5-receipt-sha256",
            sha256(STAGE5_RECEIPT) == EXPECTED_STAGE5_RECEIPT_SHA256,
            sha256(STAGE5_RECEIPT))

stage5 = JSON.parse(File.read(STAGE5_RECEIPT, encoding: "UTF-8"))
record.call("authority:stage5-receipt-pass", stage5.fetch("status") == "PASS")
record.call("authority:stage5-was-checkpoint-state",
            stage5.fetch("papers").values.all? do |paper|
              paper.fetch("state") == "stage5_completed_awaiting_stage6_decision"
            end)

old_checks = stage5.fetch("checks").to_h { |row| [row.fetch("id"), row] }
ROUTE_HASHES.each do |path, expected|
  actual = sha256(File.join(ROOT, path))
  record.call("route-lock:#{path}", actual == expected, actual)
end

root_readme = File.read(File.join(ROOT, "README.md"), encoding: "UTF-8")
batch_report = File.read(File.join(ROOT, "BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md"),
                         encoding: "UTF-8")
record.call("root-readme:terminal-state", root_readme.include?("Stage 6 skipped") &&
            root_readme.include?("pipeline global state") &&
            root_readme.include?("BATCH_ROUND9_STAGE6_SKIP_RECEIPT.json"))
record.call("batch-report:terminal-state", batch_report.include?("all five pipelines completed") &&
            batch_report.include?("reason `user declined Stage 6`") &&
            batch_report.include?("no Process Record was generated"))
record.call("batch-report:exact-author-event", batch_report.include?("> 跳过，继续下一批"))

paper_receipts = {}
PAPERS.each do |number, dir|
  paper_root = File.join(ROOT, "papers", dir)
  state_path = File.join(paper_root, "notes", "pipeline_state.md")
  checkpoint_path = File.join(paper_root, "notes", "stage5_completion_checkpoint.md")
  readme_path = File.join(paper_root, "README.md")
  state = File.read(state_path, encoding: "UTF-8")
  checkpoint = File.read(checkpoint_path, encoding: "UTF-8")
  readme = File.read(readme_path, encoding: "UTF-8")
  current_readme = readme.split(/\n- Previous/, 2).first
  current_state = state.split("\n| Item |", 2).first

  record.call("P#{number}:pipeline-global-completed",
              current_state.include?("PIPELINE COMPLETED") &&
              current_state.match?(/pipeline global state is\s+`completed`/))
  record.call("P#{number}:stage6-skipped",
              state.include?("| ARS Stage 6 | **SKIPPED / PIPELINE COMPLETED**"))
  record.call("P#{number}:no-current-pending-state",
              !current_state.match?(/STAGE 6\s+PENDING/i))
  record.call("P#{number}:checkpoint-historical-boundary",
              checkpoint.match?(/state at checkpoint issuance/i))
  record.call("P#{number}:checkpoint-current-terminal-state",
              checkpoint.match?(/Current terminal state:.*Stage 6 skipped.*pipeline completed/i))
  record.call("P#{number}:checkpoint-exact-event",
              checkpoint.include?("> 跳过，继续下一批"))
  record.call("P#{number}:checkpoint-reason",
              checkpoint.include?("reason `user declined Stage 6`"))
  record.call("P#{number}:checkpoint-no-process-record",
              checkpoint.include?("no Process Record was generated"))
  record.call("P#{number}:checkpoint-terminal-diagram",
              checkpoint.include?("[-]SUMMARY (skipped) -> [v]COMPLETED"))
  record.call("P#{number}:readme-current-terminal-state",
              current_readme.include?("PIPELINE COMPLETED") &&
              current_readme.match?(/STAGE 6\s+SKIPPED/) &&
              current_readme.include?("跳过，继续下一批"))
  record.call("P#{number}:readme-terminal-receipt-link",
              current_readme.include?("BATCH_ROUND9_STAGE6_SKIP_RECEIPT.json"))

  process_record_paths = [
    File.join(paper_root, "notes", "stage6_process_record"),
    File.join(paper_root, "stage6_process_record")
  ]
  record.call("P#{number}:no-stage6-process-record",
              process_record_paths.none? { |path| File.exist?(path) })

  old_paper = stage5.fetch("papers").fetch(number.to_s)
  immutable = {
    "manuscript.tex" => ["source_sha256", "stage5_finalization/manuscript.tex"],
    "references.bib" => ["bibliography_sha256", "stage5_finalization/references.bib"],
    "content_proof.pdf" => ["content_proof_sha256", "stage5_finalization/content_proof.pdf"],
    "paper.pdf" => ["final_pdf_sha256", "stage5_finalization/paper.pdf"]
  }
  immutable_hashes = {}
  immutable.each do |label, (key, rel)|
    path = File.join(paper_root, rel)
    actual = sha256(path)
    immutable_hashes[label] = actual
    record.call("P#{number}:immutable:#{label}", actual == old_paper.fetch(key), actual)
  end

  canonical_expected = old_checks.fetch("P#{number}:canonical-tree-frozen").fetch("detail")
  canonical_clean_expected = CLEAN_REPOSITORY_CANONICAL_HASHES.fetch(number)
  results_expected = old_checks.fetch("P#{number}:results-tree-frozen").fetch("detail")
  canonical_actual = tree_sha256("papers/#{dir}/paper")
  results_actual = tree_sha256("papers/#{dir}/results")
  canonical_profiles = [canonical_expected, canonical_clean_expected]
  record.call("P#{number}:canonical-tree-frozen", canonical_profiles.include?(canonical_actual),
              "full-local=#{canonical_expected}; clean-repository=#{canonical_clean_expected}")
  record.call("P#{number}:results-tree-frozen", results_actual == results_expected,
              results_actual)

  if [24, 25].include?(number)
    manifest_path = File.join(paper_root, "notes", "stage5_final_manifest.json")
    manifest = JSON.parse(File.read(manifest_path, encoding: "UTF-8"))
    manifest.fetch("audit_deliverables").each do |row|
      path = File.join(ROOT, row.fetch("path"))
      record.call("P#{number}:manifest-replay:#{row.fetch('role')}",
                  File.file?(path) && sha256(path) == row.fetch("sha256"))
    end
    record.call("P#{number}:checkpoint-binds-current-manifest",
                checkpoint.include?(sha256(manifest_path)), sha256(manifest_path))
  end

  if number == 28
    inventory_path = File.join(paper_root, "notes", "stage5_artifact_inventory.sha256")
    inventory_rows = File.readlines(inventory_path, chomp: true).reject(&:empty?)
    inventory_rows.each_with_index do |line, index|
      expected, rel = line.split(/\s+/, 2)
      path = File.join(ROOT, rel)
      record.call("P28:inventory-replay:#{index + 1}",
                  File.file?(path) && sha256(path) == expected, rel)
    end
  end

  paper_receipts[number.to_s] = {
    "stage5" => "completed",
    "stage6" => "skipped",
    "stage6_reason" => "user declined Stage 6",
    "pipeline_global_state" => "completed",
    "process_record_generated" => false,
    "next_required_event" => nil,
    "state_artifacts" => {
      "readme_sha256" => sha256(readme_path),
      "pipeline_state_sha256" => sha256(state_path),
      "stage5_completion_checkpoint_sha256" => sha256(checkpoint_path)
    },
    "immutable_stage5_artifacts" => immutable_hashes,
    "canonical_full_local_tree_sha256" => canonical_expected,
    "canonical_clean_repository_tree_sha256" => canonical_clean_expected,
    "results_tree_sha256" => results_actual
  }
end

record.call("batch:positive-arithmetic-a2", root_readme.include?("A2 `0/5`"))
record.call("batch:route-b-zero", root_readme.include?("Route B `0/5`"))
record.call("batch:instances-not-independent",
            root_readme.include?("19 个 bookkeeping instances") &&
            root_readme.include?("不解释为统计独立样本"))

receipt = {
  "schema_version" => "round9-stage6-skip-terminal/1.0",
  "batch_id" => "round9-papers24-28-stage6-skipped",
  "recorded_date_utc" => "2026-09-01",
  "status" => failures.empty? ? "PASS" : "FAIL",
  "authority" => {
    "raw_event_path" => "BATCH_ROUND9_STAGE6_SKIP_AUTHOR_EVENT_20260901.txt",
    "raw_event_sha256" => sha256(RAW_EVENT),
    "exact_response" => "跳过，继续下一批"
  },
  "legal_transition" => {
    "from" => "checkpoint",
    "to" => "completed",
    "stage5_status" => "completed",
    "stage6_status" => "skipped",
    "stage6_reason" => "user declined Stage 6",
    "process_record_generated" => false,
    "terminal_acknowledgement_required" => false,
    "next_required_event" => nil
  },
  "stage5_completion_authority" => {
    "path" => "BATCH_ROUND9_STAGE5_COMPLETION_RECEIPT.json",
    "sha256" => sha256(STAGE5_RECEIPT),
    "historical_state" => "stage5_completed_awaiting_stage6_decision"
  },
  "scope" => {
    "papers" => PAPERS.keys,
    "scientific_content_changed" => false,
    "final_pdf_changed" => false,
    "canonical_or_results_changed" => false,
    "route_changed" => false,
    "submission_or_external_contact" => false
  },
  "route_state" => {
    "layer" => "early A0-A1 / A1-A2 evidence",
    "positive_arithmetic_A2" => "0/5",
    "route_b_invocations" => "0/5",
    "model_instances" => 19,
    "independent_statistical_samples_claimed" => false
  },
  "tool" => {
    "path" => "tools/audit_round9_stage6_skip.rb",
    "sha256" => sha256(__FILE__)
  },
  "root_artifacts" => {
    "README.md" => sha256(File.join(ROOT, "README.md")),
    "BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md" =>
      sha256(File.join(ROOT, "BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md"))
  },
  "papers" => paper_receipts,
  "summary" => {
    "papers_completed" => paper_receipts.count,
    "stage6_skipped" => paper_receipts.count { |_id, row| row["stage6"] == "skipped" },
    "process_records_generated" => 0,
    "checks_total" => checks.count,
    "checks_passed" => checks.count { |row| row["status"] == "PASS" },
    "checks_failed" => failures.count
  },
  "checks" => checks
}

File.write(OUTPUT, JSON.pretty_generate(receipt) + "\n")
puts "#{receipt.fetch('status')} #{receipt.dig('summary', 'checks_passed')}/#{checks.count} checks; " \
     "#{paper_receipts.count}/5 pipelines completed; Stage 6 skipped 5/5; Process Records 0"
exit(failures.empty? ? 0 : 1)
