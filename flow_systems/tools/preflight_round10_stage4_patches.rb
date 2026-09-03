#!/usr/bin/env ruby
# frozen_string_literal: true

require "fileutils"
require "open3"
require "tmpdir"

ROOT = File.expand_path("..", __dir__)
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars"
PAPERS = {
  "29" => "29-bianchi-ideal-owner-refinement",
  "30" => "30-three-disk-nonconstant-roof-determinant",
  "31" => "31-level11-conjugacy-owner-ledger",
  "32" => "32-homology-cover-renormalization-uniformity",
  "33" => "33-bolza-control-matched-census"
}.freeze

def run!(command, cwd: ROOT)
  stdout, stderr, status = Open3.capture3(*command, chdir: cwd)
  raise "command failed (#{status.exitstatus}): #{command.join(' ')}\n#{stdout}\n#{stderr}" unless status.success?
  [stdout, stderr]
end

def preflight(number, directory)
  paper_root = File.join(ROOT, "papers", directory)
  notes = File.join(paper_root, "notes")
  base = File.join(notes, "stage3_revision_base.tex")
  patch = File.join(notes, "stage4_revision_patch_round1.json")
  manifest = File.join(notes, "stage3_revision_base.block-manifest.json")
  roadmap = File.join(notes, "stage3_revision_roadmap.json")
  adjudication = File.join(notes, "stage4_author_adjudication.json")
  claims = File.join(notes, "stage4_claim_surface_manifest.json")
  bibliography = File.join(paper_root, "paper", "references.bib")

  Dir.mktmpdir("round10-p#{number}-stage4-preflight.") do |tmp|
    revised = File.join(tmp, "anchored.tex")
    run!([
      "python", File.join(ARS_ROOT, "scripts/ars_apply_revision_patch.py"),
      base, patch,
      "--block-manifest", manifest,
      "--roadmap", roadmap,
      "--author-adjudication", adjudication,
      "--claim-surface-manifest", claims,
      "--artifact-root", paper_root,
      "--output", revised
    ])
    marker_free = File.binread(revised).force_encoding("UTF-8").lines.reject do |line|
      line.match?(/\A<!--block:B\d{4}-->\s*\z/)
    end.join
    File.binwrite(File.join(tmp, "manuscript.tex"), marker_free)
    FileUtils.cp(bibliography, File.join(tmp, "references.bib"))
    job = "preflight"
    run!(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"], cwd: tmp)
    run!(["bibtex", job], cwd: tmp)
    2.times { run!(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"], cwd: tmp) }
    log = File.binread(File.join(tmp, "#{job}.log")).force_encoding("UTF-8")
    overfull = log.scan(/Overfull \\hbox \(([0-9.]+)pt too wide\)/).flatten.map(&:to_f)
    undefined_citations = log.scan(/(?:Citation [`'][^\n]+ undefined|There were undefined citations)/).length
    undefined_references = log.scan(/(?:Reference [`'][^\n]+ undefined|There were undefined references)/).length
    missing_glyphs = log.scan(/Missing character:/).length
    fatal_errors = log.scan(/(?:Fatal error|Emergency stop)/i).length
    unless overfull.empty? && undefined_citations.zero? && undefined_references.zero? && missing_glyphs.zero? && fatal_errors.zero?
      log_lines = log.lines
      overfull_context = log_lines.each_index.filter_map do |index|
        next unless log_lines[index].include?("Overfull \\hbox")
        log_lines[index, 7].join.strip
      end.join("\n---\n")
      raise "P#{number}: preflight not clean: overfull=#{overfull.length} max=#{overfull.max || 0.0}; " \
            "undefined citations=#{undefined_citations}; references=#{undefined_references}; glyphs=#{missing_glyphs}; fatal=#{fatal_errors}\n" \
            "#{overfull_context}"
    end
    info, = run!(["pdfinfo", File.join(tmp, "#{job}.pdf")], cwd: tmp)
    pages = info[/^Pages:\s+(\d+)/, 1].to_i
    puts "P#{number}: clean dry-apply/full-build preflight PASS; #{pages} pages; overfull=0"
  end
end

requested = ARGV.empty? ? PAPERS.keys : ARGV
unknown = requested - PAPERS.keys
abort("unknown paper numbers: #{unknown.join(', ')}") unless unknown.empty?

begin
  run!(["ruby", File.join(ROOT, "tools/audit_round10_stage4_patches.rb"), *requested])
  requested.each { |number| preflight(number, PAPERS.fetch(number)) }
rescue RuntimeError => e
  warn "FAIL: #{e.message}"
  exit 1
end
