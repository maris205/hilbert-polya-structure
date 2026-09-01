#!/usr/bin/env ruby
# frozen_string_literal: true

# Read-only audit for the Round-10 Papers 29--33 Pre-Stage-1 boundary.

ROOT = File.expand_path("..", __dir__)
PROJECTS = {
  29 => "29-bianchi-ideal-owner-refinement",
  30 => "30-three-disk-nonconstant-roof-determinant",
  31 => "31-level11-conjugacy-owner-ledger",
  32 => "32-homology-cover-renormalization-uniformity",
  33 => "33-bolza-control-matched-census"
}.freeze

EXPECTED = [
  "README.md",
  "code/.gitkeep",
  "experiments/.gitkeep",
  "notes/pipeline_state.md",
  "notes/stage1_prestart_brief.md",
  "paper/figures/.gitkeep",
  "paper/manuscript.tex",
  "paper/references.bib",
  "results/.gitkeep"
].freeze

checks = 0
failures = []

check = lambda do |condition, label|
  checks += 1
  failures << label unless condition
end

batch_path = File.join(ROOT, "BATCH_ROUND10_PAPERS_29_33_PRESTART.md")
batch = File.exist?(batch_path) ? File.read(batch_path, encoding: "UTF-8") : ""
check.call(File.file?(batch_path), "missing batch pre-start record")
[
  "PRE-STAGE-1 / BUDGET CONFIRMATION PENDING",
  "400k–700k tokens",
  "80k–140k tokens",
  "20 document round-trips",
  "Stage 1 has not started",
  "Route B is closed",
  "“确认”"
].each { |token| check.call(batch.include?(token), "batch token missing: #{token}") }

PROJECTS.each do |number, slug|
  base = File.join(ROOT, "papers", slug)
  actual = Dir.glob(File.join(base, "**", "*"), File::FNM_DOTMATCH)
              .select { |path| File.file?(path) }
              .map { |path| path.delete_prefix("#{base}/") }
              .sort
  check.call(actual == EXPECTED.sort,
             "P#{number} file inventory mismatch: #{actual.inspect}")

  state = File.read(File.join(base, "notes/pipeline_state.md"), encoding: "UTF-8")
  brief = File.read(File.join(base, "notes/stage1_prestart_brief.md"), encoding: "UTF-8")
  readme = File.read(File.join(base, "README.md"), encoding: "UTF-8")
  tex = File.read(File.join(base, "paper/manuscript.tex"), encoding: "UTF-8")
  bib = File.read(File.join(base, "paper/references.bib"), encoding: "UTF-8")

  check.call(state.include?("PRE-STAGE-1 / BUDGET CONFIRMATION PENDING"),
             "P#{number} controlling state mismatch")
  check.call(state.include?("`NOT_STARTED`"), "P#{number} Stage-1 state missing")
  check.call(state.include?("`HUMAN_CONFIRMATION_PENDING`"),
             "P#{number} budget gate missing")
  check.call(state.include?("`CLOSED`"), "P#{number} Route-B closure missing")
  check.call(brief.match?(/not (?:a )?Stage-?1 (?:output|result)/i) ||
             brief.match?(/This is intake, not Stage 1/i) ||
             brief.start_with?("# P#{number} Stage-1 pre-start brief\n\nThis intake"),
             "P#{number} pre-start evidence boundary missing")
  check.call(readme.match?(/Stage 1 has not started|Stage 1.*?have not\s+started|are all unstarted|No Stage-1 work/im),
             "P#{number} README Stage-1 boundary missing")
  check.call(tex.include?("Liang Wang") &&
             tex.include?("Huazhong University of Science and Technology") &&
             tex.include?("wangliang.f@gmail.com"),
             "P#{number} author block incomplete")
  check.call(tex.match?(/\\section\*\{Funding\}/) &&
             tex.match?(/\\section\*\{Competing interests\}/) &&
             (tex.match?(/No funding was received/i) || tex.match?(/Funding\}None\./)) &&
             (tex.match?(/no competing interests/i) || tex.match?(/None declared/i)),
             "P#{number} declarations incomplete")
  check.call(!bib.match?(/^\s*@/), "P#{number} has a pre-screen bibliography entry")
  check.call(!File.exist?(File.join(base, "paper/paper.pdf")),
             "P#{number} has a premature PDF")
end

if failures.empty?
  puts "PASS #{checks}/#{checks} checks; 5/5 projects PRE-STAGE-1; Stage 1 started 0/5; Route B closed 5/5"
  exit 0
end

warn "FAIL #{failures.length}/#{checks} checks"
failures.each { |failure| warn "- #{failure}" }
exit 1
