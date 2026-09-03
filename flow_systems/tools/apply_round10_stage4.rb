#!/usr/bin/env ruby
# frozen_string_literal: true

require "open3"

ROOT = File.expand_path("..", __dir__)
ARS_ROOT = "/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars"
PAPERS = {
  "29" => "29-bianchi-ideal-owner-refinement",
  "30" => "30-three-disk-nonconstant-roof-determinant",
  "31" => "31-level11-conjugacy-owner-ledger",
  "32" => "32-homology-cover-renormalization-uniformity",
  "33" => "33-bolza-control-matched-census"
}.freeze

def run!(command)
  stdout, stderr, status = Open3.capture3(*command, chdir: ROOT)
  $stdout.write(stdout)
  $stderr.write(stderr)
  raise "command failed (#{status.exitstatus}): #{command.join(' ')}" unless status.success?
end

requested = ARGV.empty? ? PAPERS.keys : ARGV
unknown = requested - PAPERS.keys
abort("unknown paper numbers: #{unknown.join(', ')}") unless unknown.empty?

begin
  # The writer cannot apply. This root/orchestrator entry point first replays the
  # complete authority and writer-boundary audit, then invokes the official
  # two-phase fail-closed applicator without structural acknowledgement.
  run!(["ruby", File.join(ROOT, "tools/audit_round10_stage4_patches.rb"), *requested])

  requested.each do |number|
    paper_root = File.join(ROOT, "papers", PAPERS.fetch(number))
    notes = File.join(paper_root, "notes")
    base = File.join(notes, "stage3_revision_base.tex")
    patch = File.join(notes, "stage4_revision_patch_round1.json")
    manifest = File.join(notes, "stage3_revision_base.block-manifest.json")
    roadmap = File.join(notes, "stage3_revision_roadmap.json")
    adjudication = File.join(notes, "stage4_author_adjudication.json")
    claims = File.join(notes, "stage4_claim_surface_manifest.json")
    output = File.join(notes, "stage4_revision_round1.tex")
    report = output + ".apply-report.json"
    output_manifest = output + ".block-manifest.json"
    [output, report, output_manifest].each do |path|
      raise "P#{number}: refusing to overwrite existing Stage-4 apply artifact #{path}" if File.exist?(path)
    end

    run!([
      "python", File.join(ARS_ROOT, "scripts/revision_roadmap.py"), "validate-adjudication",
      roadmap, adjudication,
      "--base", base,
      "--block-manifest", manifest,
      "--claim-surface", claims,
      "--artifact-root", paper_root
    ])
    run!([
      "python", File.join(ARS_ROOT, "scripts/ars_apply_revision_patch.py"),
      base, patch,
      "--block-manifest", manifest,
      "--roadmap", roadmap,
      "--author-adjudication", adjudication,
      "--claim-surface-manifest", claims,
      "--artifact-root", paper_root,
      "--output", output
    ])
    puts "P#{number}: official Stage-4 apply PASS"
  end
rescue RuntimeError => e
  warn "FAIL: #{e.message}"
  exit 1
end
