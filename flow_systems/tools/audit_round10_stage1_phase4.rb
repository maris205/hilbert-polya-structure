#!/usr/bin/env ruby
# frozen_string_literal: true

require "csv"
require "digest"
require "json"
require "time"

ROOT = File.expand_path("..", __dir__)

PAPERS = {
  "P29" => {
    directory: "papers/29-bianchi-ideal-owner-refinement",
    sources: 22,
    manifest_id: "M-2026-09-02T09:25:28Z-29d4",
    phase3_checkpoint_sha256: "491c340bae8433c0a2b87826a2267e6b3f7b193f485976580bb9a38b55f5467f",
    manuscript_sha256: "7665c11cda3ee12d4310e51e69a9f47226777c85d761a5be0267340305f99fcf",
    bibliography_sha256: "ef60634ee003420e1b6273c2d11441d4623663597a66dcc75ec3b938c59e8b05",
    reference_order: %w[P29-S06 P29-S07 P29-S01 P29-S03 P29-S21 P29-S22 P29-S19 P29-S08 P29-S14 P29-S18 P29-S13 P29-S11 P29-S15 P29-S02 P29-S04 P29-S20 P29-S17 P29-S05 P29-S10 P29-S12 P29-S09 P29-S16],
    route_markers: ["unit-speed", "arclength", "primitive loxodromic", "Gaussian prime ideals", "UNASSIGNED"]
  },
  "P30" => {
    directory: "papers/30-three-disk-nonconstant-roof-determinant",
    sources: 26,
    manifest_id: "M-2026-09-02T09:25:28Z-30d4",
    phase3_checkpoint_sha256: "fca6c5143f729b12234ec674c531b4926c117db6210d2b5bf8154e65a63db43c",
    manuscript_sha256: "2c50c1b734c54c3a6c4e1b2bd48f87d63de5f2be7cdf80811517e3d449df1ff9",
    bibliography_sha256: "ef60634ee003420e1b6273c2d11441d4623663597a66dcc75ec3b938c59e8b05",
    reference_order: %w[P30-S19 P30-S20 P30-S22 P30-S07 P30-S08 P30-S04 P30-S05 P30-S24 P30-S16 P30-S03 P30-S01 P30-S02 P30-S17 P30-S18 P30-S09 P30-S10 P30-S25 P30-S23 P30-S15 P30-S13 P30-S14 P30-S26 P30-S11 P30-S12 P30-S06 P30-S21],
    route_markers: ["d=6a", "physical Euclidean flight", "six gate", "A0_FAIL", "A2_NOT_ELIGIBLE", "NO_ROUTE_PROMOTION"]
  },
  "P31" => {
    directory: "papers/31-level11-conjugacy-owner-ledger",
    sources: 22,
    manifest_id: "M-2026-09-02T09:26:20Z-31d4",
    phase3_checkpoint_sha256: "9ea8dc37a7bcd75a29e08ab1d3f7f81f66636d9d53560a7db1bf05373eed7294",
    manuscript_sha256: "4dc7ff031793aea9fb8d718d6594fde177e147961df0fcdceaea27e16bedba8a",
    bibliography_sha256: "89e0e523e50d4eb0848092cab77cff5a8e02f506a154e0ac86c64a985d83116b",
    reference_order: %w[P31-S10 P31-S18 P31-S17 P31-S03 P31-S20 P31-S13 P31-S16 P31-S21 P31-S11 P31-S12 P31-S05 P31-S02 P31-S04 P31-S07 P31-S19 P31-S01 P31-S14 P31-S15 P31-S08 P31-S22 P31-S06 P31-S09],
    route_markers: ["Gamma_0(11)", "oriented", "9,453", "A1", "UNASSIGNED"]
  },
  "P32" => {
    directory: "papers/32-homology-cover-renormalization-uniformity",
    sources: 26,
    manifest_id: "M-2026-09-02T09:26:20Z-32d4",
    phase3_checkpoint_sha256: "b910acfb9f299bd0bb5514cbc86628a0e4531d848a6566c6897bd5a6c4c80dc6",
    manuscript_sha256: "5ae25a297d02046f721c0bb6ef2be35534bc8bfe8268c660f767f0c558eb6f29",
    bibliography_sha256: "89e0e523e50d4eb0848092cab77cff5a8e02f506a154e0ac86c64a985d83116b",
    reference_order: %w[P32-S16 P32-S03 P32-S04 P32-S01 P32-S25 P32-S12 P32-S18 P32-S02 P32-S17 P32-S07 P32-S10 P32-S11 P32-S19 P32-S05 P32-S20 P32-S23 P32-S26 P32-S15 P32-S09 P32-S22 P32-S14 P32-S13 P32-S21 P32-S24 P32-S08 P32-S06],
    route_markers: ["1/N", "1/N^3", "N_k=k!", "m_k=2^k", "N'_k=2*(k!)", "CP-P32-004", "UNASSIGNED"]
  },
  "P33" => {
    directory: "papers/33-bolza-control-matched-census",
    sources: 20,
    manifest_id: "M-2026-09-02T09:24:48Z-33d4",
    phase3_checkpoint_sha256: "4ebeb9342e510579783092eceaec6fd4737136196e51ebc0e8df6b700f11cb38",
    manuscript_sha256: "04afba2461431ae8d0f04f7fa73e6ccc8619cde856f9f06fe6418f692e236e97",
    bibliography_sha256: "89e0e523e50d4eb0848092cab77cff5a8e02f506a154e0ac86c64a985d83116b",
    reference_order: %w[S02 S05 S14 S11 S12 S15 S09 S20 S19 S06 S17 S08 S13 S01 S04 S18 S07 S16 S03 S10],
    route_markers: ["b=1/2", "Lambda=21/10", "P33-RC-1", "A0_INCONCLUSIVE_SYSTOLE_CONFOUNDED", "A0_CONTROL_PANEL_INCOMPLETE"]
  }
}.freeze

LOCKS = {
  "BATCH_ROUND10_STAGE1_PHASE4_AUTHORIZATION_20260902.txt" => "b516a3f1c0b362a77ba7b5963375492d7bab73c746cb458086feb48638739a85",
  "BATCH_ROUND10_STAGE1_PHASE4_COMPOSITION_CONTRACT.md" => "4104135b2318acfc965f48c91213775d31b9924b80215f9d19b63a0506e4cc63",
  "BATCH_ROUND10_STAGE1_PHASE4_START.md" => "68d0aa50830903750a30c24d47b2911b8b5771a7bd9d4b37aed189ce264914bc",
  "BATCH_ROUND10_STAGE1_PHASE3_CHECKPOINT.md" => "5cc6daca4a3d34b7c09a8b7bc0b33e1ec16818a849d89a3755ec623a4688990e",
  "BATCH_ROUND10_STAGE1_PHASE3_AUDIT_RECEIPT.json" => "f224e196d26be6cc1cd8fa1812f792fb1fe0fe59228092c208a2bdb82a251160",
  "BATCH_ROUND10_STAGE1_PHASE4_PROVENANCE_CORRECTION.md" => "f9895d410033e5def2c390b36a841ac6523bdc7b752be5c6094377b3d73c6ec2",
  "skills/route-a-evaluator.md" => "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
  "skills/route-b-evaluator.md" => "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"
}.freeze

MANIFEST_TOP_KEYS = %w[
  manifest_version
  manifest_id
  emitted_by
  emitted_at
  session_id
  claims
  manifest_negative_constraints
].freeze
MANIFEST_REQUIRED_KEYS = %w[
  manifest_version
  manifest_id
  emitted_by
  emitted_at
  claims
  manifest_negative_constraints
].freeze
CLAIM_REQUIRED_KEYS = %w[
  claim_id
  claim_text
  intended_evidence_kind
  planned_refs
].freeze
CLAIM_ALLOWED_KEYS = (CLAIM_REQUIRED_KEYS + %w[planned_experiment_ids negative_constraints]).freeze
EVIDENCE_KINDS = %w[empirical theoretical definitional normative].freeze

@checks = 0
@failures = []
@metrics = {}

def path(relative)
  File.join(ROOT, relative)
end

def read(relative)
  File.binread(path(relative)).force_encoding(Encoding::UTF_8)
end

def digest(relative)
  Digest::SHA256.file(path(relative)).hexdigest
end

def check(label, condition)
  @checks += 1
  @failures << label unless condition
end

def nonblank?(value)
  value.is_a?(String) && !value.strip.empty?
end

def strip_markdown_for_count(text)
  text
    .gsub(/<!--.*?-->/m, " ")
    .gsub(/```.*?```/m) { |block| block.lines.reject { |line| line.start_with?("```") }.join(" ") }
    .gsub(/[#*`>|_\[\]]/, " ")
end

def section(text, heading)
  match = text.match(/^##\s+#{heading}\s*$\n(.*?)(?=^##\s+|\z)/im)
  match && match[1]
end

def report_body_without_ledger(text)
  text.split(/^##\s+(?:Report Metadata and Closed Phase Ledger|Closed machine ledger)\s*$/i, 2).first
end

def line_value(text, key)
  text.lines.grep(/^#{Regexp.escape(key)}=/)
end


LOCKS.each do |relative, expected|
  check("lock exists #{relative}", File.file?(path(relative)))
  check("lock SHA-256 #{relative}", File.file?(path(relative)) && digest(relative) == expected)
end

authorization = "BATCH_ROUND10_STAGE1_PHASE4_AUTHORIZATION_20260902.txt"
check("Phase-4 authorization exact bytes", File.file?(path(authorization)) && read(authorization).bytes == "确认，开始下一轮\n".bytes)

manifest_ids = []
total_words = 0
total_citation_pairs = 0
total_claim_intents = 0

PAPERS.each do |paper_id, config|
  directory = config.fetch(:directory)
  notes = "#{directory}/notes"
  inventory_relative = "#{notes}/stage1_phase2_source_inventory.tsv"
  phase3_checkpoint_relative = "#{notes}/stage1_phase3_checkpoint.md"
  manifest_relative = "#{notes}/stage1_phase4_claim_intent_manifest.json"
  report_relative = "#{notes}/stage1_phase4_research_report.md"
  checkpoint_relative = "#{notes}/stage1_phase4_checkpoint.md"

  check("#{paper_id} frozen Phase-3 checkpoint", File.file?(path(phase3_checkpoint_relative)) && digest(phase3_checkpoint_relative) == config.fetch(:phase3_checkpoint_sha256))
  check("#{paper_id} frozen manuscript", File.file?(path("#{directory}/paper/manuscript.tex")) && digest("#{directory}/paper/manuscript.tex") == config.fetch(:manuscript_sha256))
  check("#{paper_id} frozen bibliography", File.file?(path("#{directory}/paper/references.bib")) && digest("#{directory}/paper/references.bib") == config.fetch(:bibliography_sha256))

  check("#{paper_id} inventory exists", File.file?(path(inventory_relative)))
  inventory = File.file?(path(inventory_relative)) ? CSV.read(path(inventory_relative), headers: true, col_sep: "\t", liberal_parsing: true) : []
  source_ids = inventory.map { |row| row["source_id"] }
  check("#{paper_id} inventory source count", source_ids.length == config.fetch(:sources))
  check("#{paper_id} inventory IDs unique", source_ids.uniq.length == source_ids.length)

  check("#{paper_id} Phase-4 manifest exists", File.file?(path(manifest_relative)))
  manifest = nil
  manifest_emitted_at = nil
  if File.file?(path(manifest_relative))
    begin
      manifest = JSON.parse(read(manifest_relative))
      check("#{paper_id} manifest only allowed top keys", (manifest.keys - MANIFEST_TOP_KEYS).empty?)
      check("#{paper_id} manifest required top keys", (MANIFEST_REQUIRED_KEYS - manifest.keys).empty?)
      check("#{paper_id} manifest version", manifest["manifest_version"] == "1.0")
      check("#{paper_id} manifest emitted by report compiler", manifest["emitted_by"] == "report_compiler_agent")
      check("#{paper_id} fresh manifest ID", manifest["manifest_id"] == config.fetch(:manifest_id))
      manifest_ids << manifest["manifest_id"]
      emitted_at_valid = begin
        manifest_emitted_at = Time.iso8601(manifest.fetch("emitted_at"))
        true
      rescue ArgumentError, KeyError
        false
      end
      check("#{paper_id} manifest emitted_at", emitted_at_valid)
      check("#{paper_id} manifest ID embeds emitted_at", emitted_at_valid && manifest["manifest_id"].start_with?("M-#{manifest["emitted_at"]}-"))
      claims = manifest["claims"]
      check("#{paper_id} manifest claims nonempty", claims.is_a?(Array) && !claims.empty?)
      claim_ids = claims.is_a?(Array) ? claims.map { |claim| claim["claim_id"] } : []
      check("#{paper_id} manifest claim IDs unique", claim_ids.uniq.length == claim_ids.length)
      total_claim_intents += claims.to_a.length
      claims.to_a.each do |claim|
        claim_id = claim["claim_id"] || "missing"
        check("#{paper_id} #{claim_id} allowed claim keys", (claim.keys - CLAIM_ALLOWED_KEYS).empty?)
        check("#{paper_id} #{claim_id} required claim keys", (CLAIM_REQUIRED_KEYS - claim.keys).empty?)
        check("#{paper_id} #{claim_id} ID syntax", claim_id.match?(/\AC-\d{3,}\z/))
        check("#{paper_id} #{claim_id} text", nonblank?(claim["claim_text"]))
        check("#{paper_id} #{claim_id} evidence kind", EVIDENCE_KINDS.include?(claim["intended_evidence_kind"]))
        planned_refs = claim["planned_refs"]
        check("#{paper_id} #{claim_id} refs array", planned_refs.is_a?(Array))
        check("#{paper_id} #{claim_id} refs resolve", planned_refs.is_a?(Array) && (planned_refs - source_ids).empty?)
        check("#{paper_id} #{claim_id} no experiment IDs", !claim.key?("planned_experiment_ids"))
        claim.fetch("negative_constraints", []).each do |constraint|
          digits = claim_id.delete_prefix("C-")
          check("#{paper_id} #{claim_id} constraint ID", constraint["constraint_id"].to_s.match?(/\ANC-C#{Regexp.escape(digits)}-\d+\z/))
          check("#{paper_id} #{claim_id} constraint rule", nonblank?(constraint["rule"]))
        end
      end
      global_constraints = manifest["manifest_negative_constraints"]
      check("#{paper_id} global constraints nonempty", global_constraints.is_a?(Array) && !global_constraints.empty?)
      global_constraints.to_a.each do |constraint|
        check("#{paper_id} global constraint ID", constraint["constraint_id"].to_s.match?(/\AMNC-\d+\z/))
        check("#{paper_id} global constraint rule", nonblank?(constraint["rule"]))
      end
      manifest_text = read(manifest_relative)
      {
        "SCIENTIFIC_COMPUTATION" => /SCIENTIFIC[ _-]COMPUTATION/i,
        "NOVELTY" => /NOVELTY/i,
        "ROUTE" => /ROUTE/i
      }.each do |fence, pattern|
        check("#{paper_id} manifest preserves #{fence} fence", manifest_text.match?(pattern))
      end
    rescue JSON::ParserError => error
      check("#{paper_id} manifest parses: #{error.message}", false)
    end
  end

  check("#{paper_id} Phase-4 report exists", File.file?(path(report_relative)))
  if File.file?(path(report_relative))
    report = read(report_relative)
    report_body = report_body_without_ledger(report)
    word_count = report_body.split.length
    total_words += word_count
    check("#{paper_id} report word count 3000-8000", word_count.between?(3000, 8000))

    abstract = section(report, "Abstract")
    check("#{paper_id} Abstract section", !abstract.nil?)
    abstract_without_keywords = abstract.to_s.lines.reject { |line| line.match?(/Keywords?/i) }.join
    abstract_word_count = abstract_without_keywords.split.length
    check("#{paper_id} abstract 150-250 words", abstract_word_count.between?(150, 250))

    keywords_section = section(report, "Keywords?")
    keyword_line = report.lines.find { |line| line.match?(/^\s*(?:\*\*)?Keywords?(?:\*\*)?\s*:/i) } || keywords_section.to_s.lines.first.to_s
    keyword_text = keyword_line.sub(/.*?keywords?\s*:?/i, "").strip
    keyword_count = keyword_text.split(/\s*[;,]\s*/).reject(&:empty?).length
    check("#{paper_id} has 5-7 keywords", keyword_count.between?(5, 7))

    required_sections = {
      "author declarations" => /^\#{2,4}\s+.*Declarations/i,
      "introduction" => /^\#{2,4}\s+.*Introduction/i,
      "research question" => /research question/i,
      "literature or theory" => /^\#{2,4}\s+.*(?:Literature|Theoretical framework)/i,
      "methodology" => /^\#{2,4}\s+.*Methodology/i,
      "findings" => /^\#{2,4}\s+.*Findings/i,
      "discussion" => /^\#{2,4}\s+.*Discussion/i,
      "theoretical implications" => /^\#{2,4}\s+.*Theoretical.*Implications/i,
      "practical implications" => /^\#{2,4}\s+.*Practical.*Implications/i,
      "limitations" => /^\#{2,4}\s+.*Limitations/i,
      "future work" => /^\#{2,4}\s+.*Future Work/i,
      "conclusion" => /^\#{2,4}\s+.*Conclusion/i,
      "bounded recommendations" => /^\#{2,4}\s+.*Bounded Recommendations/i,
      "references" => /^\#{2,4}\s+References/i,
      "AI disclosure" => /^\#{2,4}\s+AI Disclosure/i,
      "report metadata" => /^\#{2,4}\s+Report Metadata/i,
      "closed ledger" => /^\#{2,4}\s+.*(?:Closed Phase Ledger|Closed machine ledger)/i
    }
    required_sections.each do |name, pattern|
      check("#{paper_id} report section #{name}", report.match?(pattern))
    end

    refs_heading = report.match(/^##\s+References\s*$/i)
    prose = refs_heading ? report[0...refs_heading.begin(0)] : report_body
    ref_count = prose.scan(/<!--ref:/).length
    anchor_count = prose.scan(/<!--anchor:/).length
    citation_pairs = prose.scan(/<!--ref:([^>]+)--><!--anchor:([^>]+)-->/)
    check("#{paper_id} every ref comment has an adjacent anchor", ref_count == citation_pairs.length && ref_count.positive?)
    cited_ids = citation_pairs.map(&:first)
    check("#{paper_id} cited IDs resolve", (cited_ids - source_ids).empty?)
    check("#{paper_id} every frozen source cited", cited_ids.uniq.sort == source_ids.sort)
    check("#{paper_id} all citations carry none locator", citation_pairs.all? { |_id, anchor| anchor == "none:" })
    total_citation_pairs += citation_pairs.length

    citation_visible = true
    cursor = 0
    prose.to_enum(:scan, /<!--ref:[^>]+--><!--anchor:none:-->/).each do
      match = Regexp.last_match
      prefix = prose[[cursor, match.begin(0) - 240].max...match.begin(0)]
      citation_visible &&= prefix.match?(/(?:19|20)\d{2}[a-z]?[^\n]{0,160}\z/i)
      cursor = match.end(0)
    end
    check("#{paper_id} visible author-year precedes every marker", citation_visible)

    author_year_pattern = /(?<![A-Za-z])(?:de la Llave|[\p{Lu}][\p{L}\p{M}’'.-]+(?:\s+(?:[\p{Lu}][\p{L}\p{M}’'.-]+|de|la|van|von|and|&|et|al\.)){0,7})\s+\((?:19|20)\d{2}[^)\n]*\)/u
    author_year_matches = prose.to_enum(:scan, author_year_pattern).map { Regexp.last_match }
    reverse_citation_coverage = author_year_matches.all? do |match|
      prose[match.end(0), 200].to_s.start_with?("<!--ref:")
    end
    check("#{paper_id} every visible author-year has an adjacent marker", reverse_citation_coverage)
    check("#{paper_id} author-year and marker counts agree", author_year_matches.length == citation_pairs.length)

    references = section(report, "References")
    reference_ids = references.to_s.scan(/^-\s+\[([^\]]+)\]/).flatten
    check("#{paper_id} reference IDs unique", reference_ids.uniq.length == reference_ids.length)
    check("#{paper_id} references exactly match citations", reference_ids.sort == cited_ids.uniq.sort)
    check("#{paper_id} references exactly match frozen inventory", reference_ids.sort == source_ids.sort)
    check("#{paper_id} APA first-author reference order", reference_ids == config.fetch(:reference_order))
    reference_lines = references.to_s.lines.grep(/^-\s+\[/)
    author_fields = reference_lines.filter_map do |line|
      line[/^-\s+\[[^\]]+\]\s+(.*?)\s+\((?:19|20)\d{2}[a-z]?\)\./, 1]
    end
    check("#{paper_id} APA author fields parsed", author_fields.length == reference_lines.length)
    check("#{paper_id} APA ampersands replace author-list and", author_fields.none? { |field| field.match?(/\sand\s/i) })

    if paper_id == "P30"
      {
        "P30-S03" => "1989a",
        "P30-S01" => "1989b",
        "P30-S02" => "1989c"
      }.each do |source_id, year|
        check("P30 #{source_id} APA year suffix in citation", prose.match?(/Gaspard and Rice \(#{year}\)<!--ref:#{source_id}--><!--anchor:none:-->/))
        check("P30 #{source_id} APA year suffix in reference", references.to_s.match?(/^- \[#{source_id}\] Gaspard, P\., & Rice, S\. A\. \(#{year}\)\./))
      end
    end

    if paper_id == "P33"
      s20 = reference_lines.find { |line| line.start_with?("- [S20]") }.to_s
      check("P33 S20 APA >20-author ellipsis", s20.include?("Trieu, T. D., … Zumkeller, R.") && !s20.include?("& Zumkeller"))
    end

    blockquotes = prose.lines.grep(/^\s*>/).map { |line| line.sub(/^\s*>\s?/, "").strip }
    check("#{paper_id} no source block quotations", blockquotes.all? { |line| line.end_with?("?") && !line.include?("<!--ref:") })
    quoted_citation_lines = prose.lines.select do |line|
      line.include?("<!--ref:") && line.match?(/“[^”\n]+”|"[^"\n]+"/)
    end
    check("#{paper_id} no inline quoted source excerpts", quoted_citation_lines.empty?)
    check("#{paper_id} no deictic temporal claims", !prose.match?(/\b(?:latest|current|recent)\b/i))
    check("#{paper_id} no positive locator-compliance claim", !report.match?(/(?:has|have|is|are)\s+(?:passed|satisfying|achieving).{0,60}locator(?:-level)? citation compliance/i))
    check("#{paper_id} report states evidence-synthesis findings", report.match?(/evidence[- ]synthesis findings/i))
    check("#{paper_id} bounded absence is not novelty", report.match?(/not.{0,90}novelty|novelty.{0,90}(?:not|neither)|does not establish novelty/i))
    check("#{paper_id} AI disclosure records metadata/abstract limit", report.match?(/AI Disclosure.*metadata.*abstract/im))
    check("#{paper_id} report warning disposition", report.include?("PHASE4_REPORT_DRAFT_READY_WITH_WARNINGS"))

    manifest_bindings = report.lines.grep(/^(?:CLAIM_INTENT_MANIFEST_ID|REPORT_MANIFEST_ID)=/).map { |line| line.split("=", 2).last.strip }
    check("#{paper_id} report uniquely binds corrected manifest ID", manifest_bindings == [config.fetch(:manifest_id)])
    finalized_lines = report.lines.grep(/^REPORT_FINALIZED_AT=/)
    finalized_at = begin
      Time.iso8601(finalized_lines.first.to_s.split("=", 2).last.to_s.strip)
    rescue ArgumentError
      nil
    end
    check("#{paper_id} report has one valid finalized UTC timestamp", finalized_lines.length == 1 && !finalized_at.nil?)
    check("#{paper_id} manifest precedes finalized report", !manifest_emitted_at.nil? && !finalized_at.nil? && manifest_emitted_at < finalized_at)

    %w[
      SOURCE_CORPUS=FROZEN_116_ROWS
      SCIENTIFIC_COMPUTATION=NOT_RUN
      CANONICAL_RESULTS_REFRESH=NOT_RUN
      NOVELTY_ASSESSMENT=NOT_RUN
      FORMAL_PROJECT_CLAIM_REGISTRATION=0/5
      FORMAL_ROUTE_A_TUPLES=0/5
      POSITIVE_ARITHMETIC_A2=0/5
      ROUTE_B_INVOCATIONS=0/5
      CANONICAL_MANUSCRIPTS_MODIFIED=0/5
      CANONICAL_BIBLIOGRAPHIES_MODIFIED=0/5
      MANUSCRIPT_DRAFTING=NOT_AUTHORIZED
      PHASE_5_REVIEW=NOT_AUTHORIZED
    ].each do |ledger_line|
      check("#{paper_id} report ledger #{ledger_line}", report.lines.include?("#{ledger_line}\n") || report.end_with?(ledger_line))
    end

    normalized_report = report.downcase.tr("-–—", "   ").gsub(/\s+/, " ")
    config.fetch(:route_markers).each do |marker|
      normalized_marker = marker.downcase.tr("-–—", "   ").gsub(/\s+/, " ")
      check("#{paper_id} report preserves route marker #{marker}", normalized_report.include?(normalized_marker))
    end

    @metrics[paper_id] = {
      "word_count" => word_count,
      "abstract_word_count" => abstract_word_count,
      "citation_pairs" => citation_pairs.length,
      "unique_sources_cited" => cited_ids.uniq.length,
      "claim_intents" => manifest ? manifest.fetch("claims", []).length : 0,
      "material_gaps" => report.scan(/\[MATERIAL GAP\]/).length
    }
  end

  check("#{paper_id} Phase-4 checkpoint exists", File.file?(path(checkpoint_relative)))
  if File.file?(path(checkpoint_relative))
    checkpoint = read(checkpoint_relative)
    check("#{paper_id} checkpoint disposition", line_value(checkpoint, "CURRENT_DISPOSITION") == ["CURRENT_DISPOSITION=PHASE4_REPORT_DRAFT_READY_WITH_WARNINGS\n"])
    check("#{paper_id} checkpoint state", line_value(checkpoint, "CURRENT_STATE") == ["CURRENT_STATE=PHASE_4_COMPLETE_AWAITING_PHASE_5_CONFIRMATION\n"])
    check("#{paper_id} checkpoint computation fence", line_value(checkpoint, "SCIENTIFIC_COMPUTATION") == ["SCIENTIFIC_COMPUTATION=NOT_RUN\n"])
    check("#{paper_id} checkpoint Phase 5 fence", line_value(checkpoint, "PHASE_5_REVIEW") == ["PHASE_5_REVIEW=NOT_AUTHORIZED\n"])
    check("#{paper_id} checkpoint binds manifest", File.file?(path(manifest_relative)) && checkpoint.include?(digest(manifest_relative)))
    check("#{paper_id} checkpoint binds report", File.file?(path(report_relative)) && checkpoint.include?(digest(report_relative)))
    check("#{paper_id} checkpoint binds Phase 3", checkpoint.include?(config.fetch(:phase3_checkpoint_sha256)))
  end

  readme_relative = "#{directory}/README.md"
  state_relative = "#{notes}/pipeline_state.md"
  check("#{paper_id} README records Phase 4", File.file?(path(readme_relative)) && read(readme_relative).include?("PHASE_4_COMPLETE") && read(readme_relative).include?("AWAITING_PHASE_5_CONFIRMATION"))
  check("#{paper_id} state records Phase 4", File.file?(path(state_relative)) && read(state_relative).include?("PHASE_4_COMPLETE") && read(state_relative).include?("AWAITING_PHASE_5_CONFIRMATION"))

  %w[code experiments results].each do |subdirectory|
    files = Dir.glob(path("#{directory}/#{subdirectory}/**/*"), File::FNM_DOTMATCH).select { |entry| File.file?(entry) }
    relative_files = files.map { |entry| entry.delete_prefix("#{path(directory)}/") }
    check("#{paper_id} #{subdirectory} has no Phase-4 scientific output", relative_files.all? { |entry| entry.end_with?(".gitkeep") })
  end
end

check("manifest IDs unique across five papers", manifest_ids.compact.uniq.length == PAPERS.length)
check("all five reports measured", @metrics.length == PAPERS.length)
check("five reports total at least 15000 words", total_words >= 15_000)
check("citation pairs positive", total_citation_pairs.positive?)
check("claim intents positive", total_claim_intents.positive?)

batch_checkpoint = "BATCH_ROUND10_STAGE1_PHASE4_CHECKPOINT.md"
root_readme = "README.md"
candidate_registry = "docs/candidate_registry.md"
audit_receipt = "BATCH_ROUND10_STAGE1_PHASE4_AUDIT_RECEIPT.json"

check("batch Phase-4 checkpoint exists", File.file?(path(batch_checkpoint)))
check("root README records Phase 4", File.file?(path(root_readme)) && read(root_readme).include?("Round 10 / Stage 1 Phase 4 complete"))
check("candidate registry records Phase 4", File.file?(path(candidate_registry)) && PAPERS.keys.all? { |paper_id| read(candidate_registry).match?(/#{paper_id}.*PHASE_4_COMPLETE/) })
check("Phase-4 audit receipt exists", File.file?(path(audit_receipt)))

if File.file?(path(batch_checkpoint))
  batch = read(batch_checkpoint)
  check("batch current state", line_value(batch, "CURRENT_STATE") == ["CURRENT_STATE=PHASE_4_COMPLETE_AWAITING_PHASE_5_CONFIRMATION\n"])
  check("batch dispositions 5/5", line_value(batch, "PHASE4_REPORT_DRAFT_READY_WITH_WARNINGS") == ["PHASE4_REPORT_DRAFT_READY_WITH_WARNINGS=5/5\n"])
  check("batch reports 5/5", line_value(batch, "FULL_RESEARCH_REPORT_DRAFTS") == ["FULL_RESEARCH_REPORT_DRAFTS=5/5\n"])
  check("batch manifests 5/5", line_value(batch, "PHASE4_CLAIM_INTENT_MANIFESTS") == ["PHASE4_CLAIM_INTENT_MANIFESTS=5/5\n"])
  check("batch computation fence", line_value(batch, "SCIENTIFIC_COMPUTATION") == ["SCIENTIFIC_COMPUTATION=NOT_RUN\n"])
  check("batch Route tuples zero", line_value(batch, "FORMAL_ROUTE_A_TUPLES") == ["FORMAL_ROUTE_A_TUPLES=0/5\n"])
  check("batch Route B zero", line_value(batch, "ROUTE_B_INVOCATIONS") == ["ROUTE_B_INVOCATIONS=0/5\n"])
  check("batch Phase 5 fence", line_value(batch, "PHASE_5_REVIEW") == ["PHASE_5_REVIEW=NOT_AUTHORIZED\n"])
  PAPERS.each do |paper_id, config|
    checkpoint_relative = "#{config.fetch(:directory)}/notes/stage1_phase4_checkpoint.md"
    check("batch binds #{paper_id} checkpoint", File.file?(path(checkpoint_relative)) && batch.include?(digest(checkpoint_relative)))
  end
end

if File.file?(path(audit_receipt))
  begin
    receipt = JSON.parse(read(audit_receipt))
    check("audit receipt schema", receipt["schema"] == "flow-systems-round10-stage1-phase4-audit-receipt-v1")
    check("audit receipt status", receipt["status"] == "PASS")
    check("audit receipt checks recorded", receipt["checks"].is_a?(Integer) && receipt["checks"].positive?)
    check("audit receipt report metrics", receipt["paper_metrics"] == @metrics)
    locks = receipt.fetch("locks", {})
    {
      "authorization_sha256" => LOCKS.fetch("BATCH_ROUND10_STAGE1_PHASE4_AUTHORIZATION_20260902.txt"),
      "composition_contract_sha256" => LOCKS.fetch("BATCH_ROUND10_STAGE1_PHASE4_COMPOSITION_CONTRACT.md"),
      "start_receipt_sha256" => LOCKS.fetch("BATCH_ROUND10_STAGE1_PHASE4_START.md"),
      "provenance_correction_sha256" => LOCKS.fetch("BATCH_ROUND10_STAGE1_PHASE4_PROVENANCE_CORRECTION.md"),
      "phase3_checkpoint_sha256" => LOCKS.fetch("BATCH_ROUND10_STAGE1_PHASE3_CHECKPOINT.md"),
      "phase3_audit_receipt_sha256" => LOCKS.fetch("BATCH_ROUND10_STAGE1_PHASE3_AUDIT_RECEIPT.json"),
      "route_a_evaluator_sha256" => LOCKS.fetch("skills/route-a-evaluator.md"),
      "route_b_evaluator_sha256" => LOCKS.fetch("skills/route-b-evaluator.md"),
      "audit_script_sha256" => digest("tools/audit_round10_stage1_phase4.rb"),
      "batch_checkpoint_sha256" => File.file?(path(batch_checkpoint)) ? digest(batch_checkpoint) : nil,
      "root_readme_sha256" => File.file?(path(root_readme)) ? digest(root_readme) : nil,
      "candidate_registry_sha256" => File.file?(path(candidate_registry)) ? digest(candidate_registry) : nil
    }.each do |key, expected|
      check("audit receipt lock #{key}", !expected.nil? && locks[key] == expected)
    end
  rescue JSON::ParserError => error
    check("audit receipt parses: #{error.message}", false)
  end
end

if @failures.empty?
  puts "PASS checks=#{@checks} failures=0 papers=5 words=#{total_words} citation_pairs=#{total_citation_pairs} claim_intents=#{total_claim_intents}"
  puts JSON.generate(@metrics)
  exit 0
end

warn "FAIL checks=#{@checks} failures=#{@failures.length}"
@failures.each { |failure| warn "- #{failure}" }
warn JSON.generate(@metrics)
exit 1
