#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND9_STAGE5_COMPLETION_RECEIPT.json")
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars"
VERIFIER = File.join(ARS_ROOT, "scripts", "verify_submission_package.py")
SOURCE_DATE_EPOCH = "1788220800"

PAPERS = {
  24 => {
    dir: "24-bianchi-holonomy-flow",
    tex_sha: "153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e",
    bib_sha: "11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87",
    proof_sha: "7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea",
    text_sha: "f72efc209a139b7eb586b4db5b5b2ab9f8850d4728931c6c9f0882359c073931",
    pages: 15, citation_commands: 9, citation_keys: 7, bib_entries: 7
  },
  25 => {
    dir: "25-three-disk-scattering-flow",
    tex_sha: "9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1",
    bib_sha: "a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab",
    proof_sha: "34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65",
    text_sha: "60aedb5e593ad6971ed37cda6206e2eab0aefc5653064f10f516f9208408b185",
    pages: 13, citation_commands: 13, citation_keys: 8, bib_entries: 8
  },
  26 => {
    dir: "26-level11-newform-time-change",
    tex_sha: "fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3",
    bib_sha: "dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f",
    proof_sha: "402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da",
    text_sha: "67805a2b582713a79755b5c8074dac91e793754f2bb7fd179d8e4bfcd8b74444",
    pages: 16, citation_commands: 9, citation_keys: 7, bib_entries: 7
  },
  27 => {
    dir: "27-congruence-inverse-limit-no-go",
    tex_sha: "bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48",
    bib_sha: "32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981",
    proof_sha: "087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208",
    text_sha: "5f02152c13d9f36fd9163cbe2906572ae52aa9bc282d5ea979165ea536bb114b",
    pages: 13, citation_commands: 5, citation_keys: 5, bib_entries: 5
  },
  28 => {
    dir: "28-bolza-magnetic-flow",
    tex_sha: "14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22",
    bib_sha: "95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e",
    proof_sha: "253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382",
    text_sha: "2e7c021043d9d5e00e561bcc134a047df00f957d39b91bf48fd856f74861f1ff",
    pages: 14, citation_commands: 9, citation_keys: 6, bib_entries: 6
  }
}.freeze

ROUTE_HASHES = {
  "skills/route-a-evaluator.md" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
  "skills/route-b-evaluator.md" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
}.freeze

PREFLIGHT_RECEIPT_SHA = "87b99ed793690c245304e1e117bb09e3890152c4da2648801549f62fd1a8a952"
INPUT_LOCK_SHA = "bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30"
FINAL_REQUIRED = %w[
  notes/stage5_content_confirmation_20260901.md
  notes/stage5_finalization_report.md
  notes/stage5_final_manifest.json
  notes/stage5_completion_checkpoint.md
  notes/stage5_collaboration_depth_advisory.md
  stage5_finalization/README.md
  stage5_finalization/manuscript.tex
  stage5_finalization/references.bib
  stage5_finalization/content_proof.pdf
  stage5_finalization/paper.pdf
  stage5_finalization/provenance_summary.md
  stage5_finalization/submission_verification_report.json
].freeze

BUILD_ARTIFACT_CANDIDATES = {
  "pass1" => %w[pass1.stdout pass1.stdout.txt run1_pass1.stdout],
  "bibtex" => %w[bib.stdout bibtex.stdout bibtex.stdout.txt run1_bibtex.stdout],
  "pass2" => %w[pass2.stdout pass2.stdout.txt run1_pass2.stdout],
  "pass3" => %w[pass3.stdout pass3.stdout.txt run1_pass3.stdout],
  "aux" => %w[paper.aux run1_paper.aux],
  "bbl" => %w[paper.bbl run1_paper.bbl],
  "blg" => %w[paper.blg run1_paper.blg],
  "log" => %w[paper.log run1_paper.log]
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def relative(path)
  path.delete_prefix("#{ROOT}/")
end

def tree_sha256(relative_dir)
  absolute = File.join(ROOT, relative_dir)
  files = Dir.glob(File.join(absolute, "**", "*"), File::FNM_DOTMATCH)
             .select { |path| File.file?(path) }
             .sort
  ledger = files.map { |path| "#{sha256(path)}  #{relative(path)}\n" }.join
  Digest::SHA256.hexdigest(ledger)
end

def run(*argv, cwd: ROOT, env: {})
  Open3.capture3(env, *argv, chdir: cwd)
end

def citation_keys(tex)
  tex.scan(/\\cite(?:t|p|alt|alp|author|year|yearpar|num)?\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}/m)
     .flatten
     .flat_map { |group| group.split(",") }
     .map(&:strip)
     .reject(&:empty?)
end

def bib_keys(bib)
  bib.scan(/^\s*@\w+\s*\{\s*([^,\s]+)/).flatten
end

def deterministic_build(tex, bib)
  result = nil
  Dir.mktmpdir("round9-stage5-completion-build.") do |tmp|
    FileUtils.cp(tex, File.join(tmp, "manuscript.tex"))
    FileUtils.cp(bib, File.join(tmp, "references.bib"))
    env = {
      "SOURCE_DATE_EPOCH" => SOURCE_DATE_EPOCH,
      "FORCE_SOURCE_DATE" => "1",
      "TZ" => "UTC",
      "LC_ALL" => "C"
    }
    latex = [
      "lualatex", "-jobname=paper", "-interaction=nonstopmode",
      "-halt-on-error", "\\pdfvariable suppressoptionalinfo 512\\relax\\input{manuscript.tex}"
    ]
    sequence = [latex, ["bibtex", "paper"], latex, latex]
    statuses = sequence.map do |argv|
      stdout, stderr, status = run(*argv, cwd: tmp, env: env)
      raise "deterministic build failed: #{argv.first}: #{(stdout + stderr).lines.last(12).join}" unless status.success?
      status.exitstatus
    end
    pdf = File.join(tmp, "paper.pdf")
    log = File.read(File.join(tmp, "paper.log"))
    blg = File.read(File.join(tmp, "paper.blg"))
    info, _stderr, status = run("pdfinfo", pdf)
    raise "pdfinfo failed" unless status.success?
    text, _stderr, status = run("pdftotext", "-layout", pdf, "-")
    raise "pdftotext failed" unless status.success?
    result = {
      "sha256" => sha256(pdf),
      "text_sha256" => Digest::SHA256.hexdigest(text),
      "pages" => info[/^Pages:\s+(\d+)/, 1].to_i,
      "page_size" => info[/^Page size:\s+(.+)$/, 1],
      "statuses" => statuses,
      "undefined_citations" => log.scan(/Citation [`'][^\n]+ undefined|There were undefined citations/).length,
      "undefined_references" => log.scan(/Reference [`'][^\n]+ undefined|There were undefined references/).length,
      "overfull_boxes" => log.scan(/Overfull \\hbox/).length,
      "missing_glyphs" => log.scan(/Missing character:/).length,
      "fatal_errors" => log.scan(/Fatal error|Emergency stop/i).length,
      "bibtex_warnings" => blg.scan(/Warning--/).length
    }
  end
  result
end

checks = []
failures = []
paper_results = {}

record = lambda do |id, condition, detail = nil|
  row = { "id" => id, "status" => condition ? "PASS" : "FAIL" }
  row["detail"] = detail unless detail.nil?
  checks << row
  failures << row unless condition
  condition
end

ROUTE_HASHES.each do |path, expected|
  full = File.join(ROOT, path)
  record.call("route-lock:#{path}", File.file?(full) && sha256(full) == expected,
              File.file?(full) ? sha256(full) : "missing")
end

preflight = File.join(ROOT, "BATCH_ROUND9_STAGE5_PREFLIGHT_RECEIPT.json")
record.call("preflight-receipt-lock", File.file?(preflight) && sha256(preflight) == PREFLIGHT_RECEIPT_SHA,
            File.file?(preflight) ? sha256(preflight) : "missing")
input_lock_path = File.join(ROOT, "BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json")
record.call("stage4.5-input-lock", File.file?(input_lock_path) && sha256(input_lock_path) == INPUT_LOCK_SHA,
            File.file?(input_lock_path) ? sha256(input_lock_path) : "missing")

if File.file?(input_lock_path)
  lock = JSON.parse(File.read(input_lock_path))
  lock.fetch("papers").each do |entry|
    number = entry.fetch("paper_id")
    record.call("P#{number}:canonical-tree-frozen",
                tree_sha256(entry.fetch("canonical_tree_path")) == entry.fetch("canonical_tree_sha256"),
                entry.fetch("canonical_tree_sha256"))
    record.call("P#{number}:results-tree-frozen",
                tree_sha256(entry.fetch("results_tree_path")) == entry.fetch("results_tree_sha256"),
                entry.fetch("results_tree_sha256"))
  end
end

PAPERS.each do |number, config|
  paper = File.join(ROOT, "papers", config.fetch(:dir))
  package = File.join(paper, "stage5_finalization")
  paths = FINAL_REQUIRED.to_h { |rel| [rel, File.join(paper, rel)] }
  paths.each do |rel, path|
    record.call("P#{number}:exists:#{rel}", File.file?(path))
  end
  next unless paths.values.all? { |path| File.file?(path) }

  build_dir = File.join(paper, "notes", "stage5_build_artifacts")
  build_paths = BUILD_ARTIFACT_CANDIDATES.to_h do |role, candidates|
    found = candidates.map { |name| File.join(build_dir, name) }.find { |path| File.file?(path) }
    record.call("P#{number}:exists:build-artifact-#{role}", !found.nil?, found ? relative(found) : candidates)
    [role, found]
  end
  next if build_paths.values.any?(&:nil?)

  tex = paths.fetch("stage5_finalization/manuscript.tex")
  bib = paths.fetch("stage5_finalization/references.bib")
  proof = paths.fetch("stage5_finalization/content_proof.pdf")
  final_pdf = paths.fetch("stage5_finalization/paper.pdf")
  record.call("P#{number}:stage5-source-lock", sha256(tex) == config.fetch(:tex_sha), sha256(tex))
  record.call("P#{number}:stage5-bibliography-lock", sha256(bib) == config.fetch(:bib_sha), sha256(bib))
  record.call("P#{number}:content-proof-lock", sha256(proof) == config.fetch(:proof_sha), sha256(proof))

  confirmation = File.read(paths.fetch("notes/stage5_content_confirmation_20260901.md"))
  record.call("P#{number}:exact-content-confirmation", confirmation.include?("确认"))
  record.call("P#{number}:confirmation-date", confirmation.include?("2026-09-01"))
  record.call(
    "P#{number}:confirmation-no-science-edit",
    confirmation.match?(/scientific-content|scientific content|manuscript science|科学内容/i) &&
      confirmation.match?(/does not|not authorize|不.*授权|未.*授权/i)
  )

  tex_text = File.read(tex)
  bib_text = File.read(bib)
  cited = citation_keys(tex_text)
  entries = bib_keys(bib_text)
  record.call("P#{number}:citation-command-count", cited.length == config.fetch(:citation_commands), cited.length)
  record.call("P#{number}:citation-key-count", cited.uniq.length == config.fetch(:citation_keys), cited.uniq.length)
  record.call("P#{number}:bib-entry-count", entries.length == config.fetch(:bib_entries), entries.length)
  record.call("P#{number}:zero-missing-citation-keys", (cited.uniq - entries.uniq).empty?, (cited.uniq - entries.uniq).sort)
  record.call("P#{number}:zero-orphan-bib-entries", (entries.uniq - cited.uniq).empty?, (entries.uniq - cited.uniq).sort)
  record.call("P#{number}:numeric-natbib-lock", tex_text.include?("\\usepackage[numbers,sort&compress]{natbib}"))
  record.call("P#{number}:plainnat-lock", tex_text.include?("\\bibliographystyle{plainnat}"))

  info, _stderr, info_status = run("pdfinfo", final_pdf)
  final_pages = info[/^Pages:\s+(\d+)/, 1].to_i
  page_size = info[/^Page size:\s+(.+)$/, 1]
  record.call("P#{number}:final-pdf-info", info_status.success?)
  record.call("P#{number}:final-page-count", final_pages == config.fetch(:pages), final_pages)
  record.call("P#{number}:final-page-size-a4", page_size.to_s.include?("A4"), page_size)
  final_text, _stderr, text_status = run("pdftotext", "-layout", final_pdf, "-")
  proof_text, _stderr, proof_status = run("pdftotext", "-layout", proof, "-")
  final_text_sha = Digest::SHA256.hexdigest(final_text)
  proof_text_sha = Digest::SHA256.hexdigest(proof_text)
  record.call("P#{number}:final-pdftotext-success", text_status.success? && proof_status.success?)
  record.call("P#{number}:proof-text-lock", proof_text_sha == config.fetch(:text_sha), proof_text_sha)
  record.call("P#{number}:final-proof-text-equivalence", final_text_sha == proof_text_sha, final_text_sha)

  fonts, _stderr, fonts_status = run("pdffonts", final_pdf)
  font_rows = fonts.lines.drop(2).reject { |line| line.strip.empty? }
  embedded = font_rows.count { |line| line.split[-5] == "yes" }
  unicode = font_rows.count { |line| line.split[-3] == "yes" }
  record.call("P#{number}:pdffonts-success", fonts_status.success?)
  record.call("P#{number}:all-fonts-embedded", !font_rows.empty? && embedded == font_rows.length,
              "#{embedded}/#{font_rows.length}")
  record.call("P#{number}:unicode-font-maps-present", unicode.positive?, "#{unicode}/#{font_rows.length}")

  log = File.read(build_paths.fetch("log"))
  blg = File.read(build_paths.fetch("blg"))
  diagnostics = {
    "undefined_citations" => log.scan(/Citation [`'][^\n]+ undefined|There were undefined citations/).length,
    "undefined_references" => log.scan(/Reference [`'][^\n]+ undefined|There were undefined references/).length,
    "overfull_boxes" => log.scan(/Overfull \\hbox/).length,
    "missing_glyphs" => log.scan(/Missing character:/).length,
    "fatal_errors" => log.scan(/Fatal error|Emergency stop/i).length,
    "bibtex_warnings" => blg.scan(/Warning--/).length
  }
  diagnostics.each do |name, value|
    record.call("P#{number}:final-build-zero-#{name.tr('_', '-')}", value.zero?, value)
  end

  replay_a = deterministic_build(tex, bib)
  replay_b = deterministic_build(tex, bib)
  final_sha = sha256(final_pdf)
  record.call("P#{number}:independent-build-a-success", replay_a.fetch("statuses").all?(&:zero?))
  record.call("P#{number}:independent-build-b-success", replay_b.fetch("statuses").all?(&:zero?))
  record.call("P#{number}:independent-builds-byte-identical",
              replay_a.fetch("sha256") == replay_b.fetch("sha256"), replay_a.fetch("sha256"))
  record.call("P#{number}:promoted-final-matches-independent-build",
              final_sha == replay_a.fetch("sha256"), final_sha)
  record.call("P#{number}:independent-build-text-equivalence",
              replay_a.fetch("text_sha256") == config.fetch(:text_sha), replay_a.fetch("text_sha256"))
  record.call("P#{number}:independent-build-page-count", replay_a.fetch("pages") == config.fetch(:pages), replay_a.fetch("pages"))
  %w[undefined_citations undefined_references overfull_boxes missing_glyphs fatal_errors bibtex_warnings].each do |name|
    record.call("P#{number}:independent-build-zero-#{name.tr('_', '-')}", replay_a.fetch(name).zero?, replay_a.fetch(name))
  end

  report_path = paths.fetch("stage5_finalization/submission_verification_report.json")
  verifier_report = JSON.parse(File.read(report_path))
  report_checks = verifier_report.fetch("checks")
  statuses = report_checks.group_by { |row| row.fetch("status") }.transform_values(&:length)
  record.call("P#{number}:package-policy-advisory", verifier_report.dig("header", "policy_slug") == "advisory")
  record.call("P#{number}:package-report-roster", report_checks.length == 14, report_checks.length)
  record.call("P#{number}:package-c1-pass", report_checks.any? { |row| row["id"] == "C1" && row["status"] == "pass" })
  record.call("P#{number}:package-c2-pass", report_checks.any? { |row| row["id"] == "C2" && row["status"] == "pass" })
  record.call("P#{number}:package-no-fail", statuses.fetch("fail", 0).zero?, statuses)
  record.call("P#{number}:package-five-not-checked", statuses.fetch("not_checked", 0) == 5, statuses)
  freshness_stdout, freshness_stderr, _freshness_status = run(
    "python", VERIFIER, package, "--policy", "advisory", "--check-freshness"
  )
  freshness = freshness_stdout + freshness_stderr
  record.call("P#{number}:package-report-fresh", freshness.match?(/report fresh/i), freshness.lines.first(3).join.strip)
  %w[TERMINAL-BLOCK VERIFICATION-INCOMPLETE STALE-REPORT].each do |token|
    record.call("P#{number}:package-no-#{token.downcase}", !freshness.include?(token))
  end

  provenance = File.read(paths.fetch("stage5_finalization/provenance_summary.md"))
  record.call("P#{number}:provenance-advisory-heading", provenance.include?("## Submission Package Advisories"))
  nonpassing = report_checks.select { |row| %w[fail warn not_checked].include?(row.fetch("status")) }
  nonpassing.each do |row|
    record.call("P#{number}:provenance-transcribes-#{row.fetch('id')}", provenance.include?(row.fetch("id")))
  end

  manifest = JSON.parse(File.read(paths.fetch("notes/stage5_final_manifest.json")))
  record.call("P#{number}:final-manifest-completed", manifest.to_s.match?(/complete/i))
  record.call("P#{number}:final-manifest-binds-pdf", manifest.to_s.include?(final_sha))
  record.call("P#{number}:final-manifest-binds-source", manifest.to_s.include?(config.fetch(:tex_sha)))
  record.call("P#{number}:final-manifest-binds-proof", manifest.to_s.include?(config.fetch(:proof_sha)))

  checkpoint = File.read(paths.fetch("notes/stage5_completion_checkpoint.md"))
  collab = File.read(paths.fetch("notes/stage5_collaboration_depth_advisory.md"))
  state = File.read(File.join(paper, "notes", "pipeline_state.md"))
  readme = File.read(File.join(paper, "README.md"))
  workspace_readme = File.read(paths.fetch("stage5_finalization/README.md"))
  record.call("P#{number}:full-checkpoint", checkpoint.match?(/FULL/i))
  record.call("P#{number}:stage6-pending", (checkpoint + state).match?(/Stage 6.*(?:pending|not entered|未进入|等待)/i))
  record.call("P#{number}:collaboration-insufficient-evidence", collab.include?("insufficient_evidence"))
  record.call("P#{number}:paper-readme-stage5-complete", readme.match?(/Stage.?5.*(?:complete|完成)/i))
  record.call("P#{number}:workspace-readme-final", workspace_readme.match?(/final paper|final PDF|最终 PDF|Stage 5.*complete/i))
  record.call("P#{number}:route-boundary-recorded", (checkpoint + state + readme).include?("0/5") && (checkpoint + state + readme).match?(/Route B/i))

  paper_results[number.to_s] = {
    "source_sha256" => sha256(tex),
    "bibliography_sha256" => sha256(bib),
    "content_proof_sha256" => sha256(proof),
    "final_pdf_sha256" => final_sha,
    "pages" => final_pages,
    "pdftotext_layout_sha256" => final_text_sha,
    "font_rows" => font_rows.length,
    "embedded_fonts" => embedded,
    "unicode_mapped_fonts" => unicode,
    "citation_command_instances" => cited.length,
    "unique_citation_keys" => cited.uniq.length,
    "bibliography_entries" => entries.length,
    "build_diagnostics" => diagnostics,
    "independent_build_sha256" => replay_a.fetch("sha256"),
    "independent_double_build_byte_identical" => replay_a.fetch("sha256") == replay_b.fetch("sha256"),
    "package_verifier_status_counts" => statuses,
    "package_fingerprint" => verifier_report.dig("header", "package_fingerprint"),
    "package_freshness_stdout" => freshness_stdout.strip,
    "state" => "stage5_completed_awaiting_stage6_decision"
  }
end

receipt = {
  "schema_version" => "round9-stage5-completion-validation/1.0",
  "batch_id" => "round9-papers24-28-stage5-completion",
  "validated_at" => "2026-09-01T00:00:00Z",
  "status" => failures.empty? ? "PASS" : "FAIL",
  "scope" => {
    "papers" => PAPERS.keys,
    "format_only" => true,
    "citation_profile" => "natbib[numbers,sort&compress]+plainnat",
    "content_confirmation" => "确认",
    "final_pdf_emitted" => true,
    "canonical_promotion" => false,
    "route_advancement" => false,
    "submission_or_external_contact" => false,
    "stage6_entered" => false
  },
  "reproducibility_envelope" => {
    "source_date_epoch" => SOURCE_DATE_EPOCH,
    "force_source_date" => "1",
    "tz" => "UTC",
    "compiler_sequence" => ["lualatex", "bibtex", "lualatex", "lualatex"],
    "lualatex_optional_info_suppression" => 512
  },
  "route_state" => {
    "layer" => "early A0-A1 / A1-A2 evidence",
    "positive_arithmetic_A2" => "0/5",
    "route_b_invocations" => "0/5",
    "model_instances" => 19,
    "independent_statistical_samples_claimed" => false
  },
  "tool" => {
    "path" => relative(__FILE__),
    "sha256" => sha256(__FILE__)
  },
  "summary" => {
    "checks_total" => checks.length,
    "checks_passed" => checks.count { |row| row.fetch("status") == "PASS" },
    "checks_failed" => failures.length,
    "papers_passed" => paper_results.length,
    "pages_total" => paper_results.values.sum { |row| row.fetch("pages") },
    "final_pdfs" => paper_results.length,
    "independent_builds_executed" => paper_results.length * 2,
    "citation_command_instances" => paper_results.values.sum { |row| row.fetch("citation_command_instances") },
    "unique_citation_keys" => paper_results.values.sum { |row| row.fetch("unique_citation_keys") },
    "bibliography_entries" => paper_results.values.sum { |row| row.fetch("bibliography_entries") }
  },
  "papers" => paper_results,
  "checks" => checks
}

File.write(OUTPUT, JSON.pretty_generate(receipt) + "\n")
puts "Round 9 Stage 5 completion: #{receipt['status']} " \
     "(#{receipt.dig('summary', 'checks_passed')}/#{receipt.dig('summary', 'checks_total')} checks; " \
     "#{receipt.dig('summary', 'papers_passed')}/5 papers; #{receipt.dig('summary', 'pages_total')} pages)"
failures.each { |row| warn "FAIL #{row['id']}: #{row['detail']}" }
exit(failures.empty? ? 0 : 1)
