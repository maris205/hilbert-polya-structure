#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
OUTPUT = File.join(ROOT, "BATCH_ROUND9_STAGE5_PREFLIGHT_RECEIPT.json")

PAPERS = {
  24 => {
    dir: "24-bianchi-holonomy-flow",
    draft: "notes/stage4_prime_revision_round2.tex",
    draft_sha: "79735d058d965a35de10cc0b3655e0b1db5217bde00e02d2d48b7564cd841afc",
    bib: "paper/references.bib",
    bib_sha: "11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87",
    preview_sha: "7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea",
    pages: 15
  },
  25 => {
    dir: "25-three-disk-scattering-flow",
    draft: "notes/stage4_revision_round1.tex",
    draft_sha: "39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835",
    bib: "notes/stage4_5_references_corrected_round1.bib",
    bib_sha: "a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab",
    preview_sha: "34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65",
    pages: 13
  },
  26 => {
    dir: "26-level11-newform-time-change",
    draft: "notes/stage4_prime_revision_round2.tex",
    draft_sha: "345c258b5a1097c67d4f7777167b90eee208d6b2d36b23655990269a4de42203",
    bib: "paper/references.bib",
    bib_sha: "dbb54b090c63904964e27d9c63e67c6f907a9b9a2788e7fdb91f2c7f9820ad0f",
    preview_sha: "402f2fa4adb0a197799539a97ff15122d3056f4a3ebc153ccc9b82423438b7da",
    pages: 16
  },
  27 => {
    dir: "27-congruence-inverse-limit-no-go",
    draft: "notes/stage4_prime_revision_round1.tex",
    draft_sha: "803d9e7d69c233363d912b4fee25f5915b7f07d48937b794ee11c807ca182ef7",
    bib: "paper/references.bib",
    bib_sha: "32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981",
    preview_sha: "087ae69c0b70a1d2a3bd6b9607ac71ca33a7adb2eff3545858b5f71b40fb3208",
    pages: 13
  },
  28 => {
    dir: "28-bolza-magnetic-flow",
    draft: "notes/stage4_prime_revision_round1.tex",
    draft_sha: "126783db66949396f7b3b494e06f55e4deedcc9f443f29e6477e6254676d472e",
    bib: "paper/references.bib",
    bib_sha: "95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e",
    preview_sha: "253d10080331076a14d658afc423a72b2f687eadcfb68c6e482cec03aabae382",
    pages: 14
  }
}.freeze

ROUTE_HASHES = {
  "skills/route-a-evaluator.md" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
  "skills/route-b-evaluator.md" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
}.freeze

INPUT_LOCK_SHA = "bcfc097598a062fa91176aebb76be41a28eda7699c4a39ccaaaf2426194b8b30"
FORBIDDEN = /UNVERIFIED CITATION|anchor:none|HIGH-WARN|severity=HIGH-BLOCK|TERMINAL-BLOCK|READ-LEDGER-INVALID|\bTODO\b|\bTBD\b|\bFIXME\b/i
ARS_MARKER = /<!--(?:ref|anchor|block):?[^>]*-->/

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

def marker_clean(source)
  source.force_encoding("UTF-8").lines.reject do |line|
    line.match?(/\A<!--block:B\d{4}-->\s*\z/)
  end.join.gsub(ARS_MARKER, "")
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

def command!(*argv, cwd:)
  stdout, stderr, status = Open3.capture3(*argv, chdir: cwd)
  raise "#{argv.join(' ')} exited #{status.exitstatus}: #{stderr.lines.last(8).join.strip}" unless status.success?

  [stdout, stderr]
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
  record.call("route-lock:#{path}", File.file?(full) && sha256(full) == expected, expected)
end
record.call(
  "stage4.5-input-lock",
  sha256(File.join(ROOT, "BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json")) == INPUT_LOCK_SHA,
  INPUT_LOCK_SHA
)

lock = JSON.parse(File.read(File.join(ROOT, "BATCH_ROUND9_STAGE4_5_ROUND2_INPUT_LOCK.json")))
lock.fetch("papers").each do |entry|
  record.call(
    "P#{entry.fetch('paper_id')}:canonical-tree-frozen",
    tree_sha256(entry.fetch("canonical_tree_path")) == entry.fetch("canonical_tree_sha256"),
    entry.fetch("canonical_tree_sha256")
  )
  record.call(
    "P#{entry.fetch('paper_id')}:results-tree-frozen",
    tree_sha256(entry.fetch("results_tree_path")) == entry.fetch("results_tree_sha256"),
    entry.fetch("results_tree_sha256")
  )
end

PAPERS.each do |number, config|
  paper = File.join(ROOT, "papers", config.fetch(:dir))
  draft = File.join(paper, config.fetch(:draft))
  bibliography = File.join(paper, config.fetch(:bib))
  preview = File.join(paper, "notes", "stage4_5_round2_preview.pdf")
  final_dir = File.join(paper, "stage5_finalization")
  final_tex = File.join(final_dir, "manuscript.tex")
  final_bib = File.join(final_dir, "references.bib")
  proof = File.join(final_dir, "content_proof.pdf")
  entry_decision = File.join(paper, "notes", "stage5_entry_decision_20260831.md")
  preflight = File.join(paper, "notes", "stage5_content_preflight.md")
  manifest = File.join(paper, "notes", "stage5_input_manifest.json")
  build_receipt = File.join(paper, "notes", "stage5_preflight_build_receipt.json")
  tortured = File.join(paper, "notes", "stage5_entry_tortured_phrase_advisory.json")
  cross_doc = File.join(paper, "notes", "stage5_entry_cross_document_advisory_unavailable.txt")
  workspace_readme = File.join(final_dir, "README.md")

  required = [draft, bibliography, preview, final_tex, final_bib, proof, entry_decision,
              preflight, manifest, build_receipt, tortured, cross_doc, workspace_readme]
  required.each do |path|
    record.call("P#{number}:exists:#{relative(path)}", File.file?(path))
  end
  next unless required.all? { |path| File.file?(path) }

  record.call("P#{number}:accepted-draft-lock", sha256(draft) == config.fetch(:draft_sha), config.fetch(:draft_sha))
  record.call("P#{number}:accepted-bib-lock", sha256(bibliography) == config.fetch(:bib_sha), config.fetch(:bib_sha))
  record.call("P#{number}:preview-lock", sha256(preview) == config.fetch(:preview_sha), config.fetch(:preview_sha))
  record.call("P#{number}:final-bib-byte-copy", File.binread(final_bib) == File.binread(bibliography), sha256(final_bib))

  accepted = File.binread(draft)
  clean = File.binread(final_tex)
  expected_clean = marker_clean(accepted.dup)
  record.call("P#{number}:mechanical-marker-removal-only", clean.b == expected_clean.b, sha256(final_tex))
  record.call("P#{number}:zero-ars-markers", clean.scan(ARS_MARKER).empty?)
  record.call("P#{number}:zero-hard-block-tokens", clean.match?(FORBIDDEN) == false)
  record.call("P#{number}:natbib-numeric-lock", clean.include?("\\usepackage[numbers,sort&compress]{natbib}"))
  record.call("P#{number}:plainnat-lock", clean.include?("\\bibliographystyle{plainnat}"))

  cited = citation_keys(clean)
  entries = bib_keys(File.read(final_bib))
  record.call("P#{number}:zero-missing-citations", (cited.uniq - entries.uniq).empty?, (cited.uniq - entries.uniq).sort)
  record.call("P#{number}:zero-bibliography-orphans", (entries.uniq - cited.uniq).empty?, (entries.uniq - cited.uniq).sort)
  record.call("P#{number}:zero-duplicate-bib-keys", entries.length == entries.uniq.length)

  declarations = {
    "author" => /Liang Wang/,
    "affiliation" => /Huazhong University of Science and Technology/,
    "contact" => /wangliang\.f@gmail\.com/,
    "funding" => /Funding/i,
    "conflict" => /Conflict of Interest|Conflict of interest|Competing interests/i,
    "contributions" => /Author contributions|CRediT author statement/i,
    "availability" => /Data and (?:code|Code) availability/i,
    "ethics" => /Ethics (?:statement|Declaration)/i,
    "ai-disclosure" => /AI-Assisted Research Disclosure/i,
    "limitations" => /Limitations/i
  }
  declarations.each do |name, pattern|
    record.call("P#{number}:declaration:#{name}", clean.match?(pattern))
  end

  record.call("P#{number}:proof-byte-copy", File.binread(proof) == File.binread(preview), sha256(proof))
  info, = command!("pdfinfo", proof, cwd: ROOT)
  pages = info[/^Pages:\s+(\d+)/, 1].to_i
  record.call("P#{number}:proof-page-count", pages == config.fetch(:pages), pages)
  record.call("P#{number}:no-premature-final-pdf", !File.exist?(File.join(final_dir, "paper.pdf")))

  advisory = JSON.parse(File.read(tortured))
  record.call("P#{number}:660-schema", advisory["schema_version"] == "tortured-phrase-advisory/1.0")
  record.call("P#{number}:660-bound-to-accepted-draft", advisory.dig("input_binding", "artifact", "artifact_sha256") == config.fetch(:draft_sha))
  record.call("P#{number}:660-explicit-not-checked", advisory["check_status"] == "not_checked" && advisory["reason_code"] == "SNAPSHOT_NOT_PROVIDED")
  record.call("P#{number}:660-not-clean-certificate", advisory.dig("boundary", "absence_is_clean_certificate") == false)
  cross_text = File.read(cross_doc)
  record.call("P#{number}:672-explicit-unavailable", cross_text.include?("ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE"))
  record.call("P#{number}:672-no-fabricated-carrier", !File.exist?(File.join(paper, "notes", "stage5_entry_cross_document_advisory.json")))

  decision_text = File.read(entry_decision)
  preflight_text = File.read(preflight)
  record.call("P#{number}:entry-confirmation-recorded", decision_text.include?("确认"))
  record.call("P#{number}:citation-decision-recorded", decision_text.match?(/plainnat/i))
  record.call("P#{number}:awaiting-content-confirmation", (decision_text + preflight_text).match?(/await|pending|confirm|等待|确认/i))

  replay = {}
  Dir.mktmpdir("round9-p#{number}-stage5-preflight.") do |tmp|
    FileUtils.cp(final_tex, File.join(tmp, "manuscript.tex"))
    FileUtils.cp(final_bib, File.join(tmp, "references.bib"))
    env = { "TZ" => "UTC" }
    sequence = [
      ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
      ["bibtex", "manuscript"],
      ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
      ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"]
    ]
    sequence.each do |argv|
      stdout, stderr, status = Open3.capture3(env, *argv, chdir: tmp)
      raise "P#{number} build failed: #{argv.first}: #{(stdout + stderr).lines.last(12).join}" unless status.success?
    end
    built_pdf = File.join(tmp, "manuscript.pdf")
    log = File.read(File.join(tmp, "manuscript.log"))
    built_info, = command!("pdfinfo", built_pdf, cwd: ROOT)
    proof_text, = command!("pdftotext", "-layout", proof, "-", cwd: ROOT)
    built_text, = command!("pdftotext", "-layout", built_pdf, "-", cwd: ROOT)
    replay = {
      "compiler_sequence" => ["lualatex", "bibtex", "lualatex", "lualatex"],
      "pages" => built_info[/^Pages:\s+(\d+)/, 1].to_i,
      "built_pdf_sha256" => sha256(built_pdf),
      "proof_text_sha256" => Digest::SHA256.hexdigest(proof_text),
      "built_text_sha256" => Digest::SHA256.hexdigest(built_text),
      "undefined_citations" => log.scan(/Citation [`'][^\n]+ undefined|There were undefined citations/).length,
      "undefined_references" => log.scan(/Reference [`'][^\n]+ undefined|There were undefined references/).length,
      "missing_glyphs" => log.scan(/Missing character:/).length,
      "fatal_errors" => log.scan(/Fatal error|Emergency stop/i).length,
      "overfull_hboxes" => log.scan(/Overfull \\hbox/).length
    }
    record.call("P#{number}:isolated-build-pages", replay.fetch("pages") == config.fetch(:pages), replay.fetch("pages"))
    record.call("P#{number}:isolated-build-zero-undefined-citations", replay.fetch("undefined_citations").zero?)
    record.call("P#{number}:isolated-build-zero-undefined-references", replay.fetch("undefined_references").zero?)
    record.call("P#{number}:isolated-build-zero-missing-glyphs", replay.fetch("missing_glyphs").zero?)
    record.call("P#{number}:isolated-build-zero-fatal-errors", replay.fetch("fatal_errors").zero?)
    record.call("P#{number}:isolated-build-zero-overfull-hboxes", replay.fetch("overfull_hboxes").zero?)
    record.call("P#{number}:proof-replay-text-equivalence", replay.fetch("proof_text_sha256") == replay.fetch("built_text_sha256"), replay.fetch("built_text_sha256"))
  end

  paper_results[number.to_s] = {
    "accepted_draft_sha256" => sha256(draft),
    "finalization_source_sha256" => sha256(final_tex),
    "bibliography_sha256" => sha256(final_bib),
    "content_proof_sha256" => sha256(proof),
    "pages" => pages,
    "citation_command_instances" => cited.length,
    "unique_citation_keys" => cited.uniq.length,
    "bibliography_entries" => entries.length,
    "tortured_phrase_advisory_sha256" => sha256(tortured),
    "cross_document_diagnostic_sha256" => sha256(cross_doc),
    "isolated_replay" => replay,
    "state" => "stage5_in_progress_awaiting_scholar_content_confirmation"
  }
end

receipt = {
  "schema_version" => "round9-stage5-preflight-validation/1.0",
  "batch_id" => "round9-papers24-28-stage5-preflight",
  "validated_at" => "2026-08-31T09:30:00Z",
  "status" => failures.empty? ? "PASS" : "FAIL",
  "scope" => {
    "papers" => PAPERS.keys,
    "format_only" => true,
    "citation_profile" => "natbib[numbers,sort&compress]+plainnat",
    "final_pdf_emitted" => false,
    "content_confirmation_pending" => true,
    "canonical_promotion" => false,
    "route_advancement" => false,
    "submission_or_external_contact" => false
  },
  "route_state" => {
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
    "checks_passed" => checks.count { |row| row["status"] == "PASS" },
    "checks_failed" => failures.length,
    "papers_passed" => paper_results.length,
    "pages_total" => paper_results.values.sum { |row| row.fetch("pages") }
  },
  "papers" => paper_results,
  "checks" => checks
}

File.write(OUTPUT, JSON.pretty_generate(receipt) + "\n")
puts "Round 9 Stage 5 preflight: #{receipt['status']} " \
     "(#{receipt.dig('summary', 'checks_passed')}/#{receipt.dig('summary', 'checks_total')} checks; " \
     "#{receipt.dig('summary', 'papers_passed')}/5 papers; #{receipt.dig('summary', 'pages_total')} pages)"
failures.each { |row| warn "FAIL #{row['id']}: #{row['detail']}" }
exit(failures.empty? ? 0 : 1)
