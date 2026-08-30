#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
PAPERS = {
  "24" => "24-bianchi-holonomy-flow",
  "25" => "25-three-disk-scattering-flow",
  "26" => "26-level11-newform-time-change",
  "27" => "27-congruence-inverse-limit-no-go",
  "28" => "28-bolza-magnetic-flow"
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def run!(command, cwd, transcript)
  stdout, stderr, status = Open3.capture3(*command, chdir: cwd)
  transcript << "$ #{command.join(' ')}\n" << stdout << stderr << "\n"
  raise "command failed (#{status.exitstatus}): #{command.join(' ')}" unless status.success?
end

def build(number, directory)
  paper_root = File.join(ROOT, "papers", directory)
  notes = File.join(paper_root, "notes")
  revised = File.join(notes, "stage4_revision_round1.tex")
  bibliography = File.join(paper_root, "paper", "references.bib")
  patch = File.join(notes, "stage4_revision_patch_round1.json")
  bundle = File.join(notes, "stage4_revision_evidence_bundle.json")
  [revised, bibliography, patch, bundle].each { |path| raise "missing #{path}" unless File.file?(path) }

  transcript = +""
  Dir.mktmpdir("p#{number}-stage4-preview.") do |tmp|
    marker_free = File.binread(revised).force_encoding("UTF-8").lines.reject do |line|
      line.match?(/\A<!--block:B\d{4}-->\s*\z/)
    end.join
    File.binwrite(File.join(tmp, "manuscript.tex"), marker_free)
    FileUtils.cp(bibliography, File.join(tmp, "references.bib"))
    job = "stage4_revision_round1"
    run!(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"], tmp, transcript)
    run!(["bibtex", job], tmp, transcript)
    2.times do
      run!(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"], tmp, transcript)
    end
    FileUtils.cp(File.join(tmp, "#{job}.pdf"), File.join(notes, "stage4_revision_round1.pdf"))
    FileUtils.cp(File.join(tmp, "#{job}.log"), File.join(notes, "stage4_revision_round1.build.log"))
  end

  pdf = File.join(notes, "stage4_revision_round1.pdf")
  log_path = File.join(notes, "stage4_revision_round1.build.log")
  log = File.binread(log_path).force_encoding("UTF-8")
  info_stdout, info_stderr, info_status = Open3.capture3("pdfinfo", pdf)
  raise "pdfinfo failed: #{info_stderr}" unless info_status.success?
  pages = info_stdout[/^Pages:\s+(\d+)/, 1].to_i
  page_size = info_stdout[/^Page size:\s+(.+)$/, 1]
  overfull_values = log.scan(/Overfull \\hbox \(([0-9.]+)pt too wide\)/).flatten.map(&:to_f)
  undefined_citations = log.scan(/(?:Citation [`'][^\n]+ undefined|There were undefined citations)/).length
  undefined_references = log.scan(/(?:Reference [`'][^\n]+ undefined|There were undefined references)/).length
  missing_glyphs = log.scan(/Missing character:/).length
  fatal_errors = log.scan(/(?:Fatal error|Emergency stop)/i).length
  scientific_pass = undefined_citations.zero? && undefined_references.zero? && missing_glyphs.zero? && fatal_errors.zero?
  receipt = {
    "schema" => "round9-stage4-preview-build-receipt/1.0",
    "paper_number" => number.to_i,
    "date" => "2026-08-30",
    "classification" => "STAGE4_MARKER_STRIPPED_PREVIEW_NOT_STAGE5_PROMOTION",
    "status" => scientific_pass ? "PASS" : "FAIL",
    "compiler_sequence" => ["lualatex", "bibtex", "lualatex", "lualatex"],
    "citation_style" => "plainnat_numeric_current",
    "pages" => pages,
    "page_size" => page_size,
    "undefined_citations" => undefined_citations,
    "undefined_references" => undefined_references,
    "missing_glyphs" => missing_glyphs,
    "fatal_errors" => fatal_errors,
    "overfull_hboxes" => overfull_values.length,
    "maximum_overfull_pt" => overfull_values.max || 0.0,
    "layout_advisory" => overfull_values.empty? ? "NONE" : "OVERFULL_HBOX_PRESENT",
    "bindings" => {
      "revised_anchored_draft_sha256" => sha256(revised),
      "revision_patch_sha256" => sha256(patch),
      "revision_evidence_bundle_sha256" => sha256(bundle),
      "references_bib_sha256" => sha256(bibliography),
      "preview_pdf_sha256" => sha256(pdf),
      "final_build_log_sha256" => sha256(log_path)
    },
    "write_boundary" => {
      "paper_manuscript_modified" => false,
      "paper_pdf_modified" => false,
      "canonical_results_refreshed" => false,
      "stage5_invoked" => false
    }
  }
  receipt_path = File.join(notes, "stage4_preview_build_receipt.json")
  File.binwrite(receipt_path, JSON.pretty_generate(receipt) + "\n")
  raise "P#{number}: preview validation failed" unless scientific_pass
  puts "P#{number}: preview PASS; #{pages} pages; overfull=#{overfull_values.length}; max=#{receipt['maximum_overfull_pt']}pt"
end

requested = ARGV.empty? ? PAPERS.keys : ARGV
unknown = requested - PAPERS.keys
abort("unknown paper numbers: #{unknown.join(', ')}") unless unknown.empty?

begin
  requested.each { |number| build(number, PAPERS.fetch(number)) }
rescue KeyError, RuntimeError => e
  warn "FAIL: #{e.message}"
  exit 1
end
