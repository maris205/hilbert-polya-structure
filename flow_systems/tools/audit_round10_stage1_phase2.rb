#!/usr/bin/env ruby
# frozen_string_literal: true

require "csv"
require "digest"

ROOT = File.expand_path("..", __dir__)

PAPERS = {
  "P29" => {
    directory: "papers/29-bianchi-ideal-owner-refinement",
    sources: 22,
    peer_reviewed: 17,
    verification_seat: "VERIFY-SEAT-C",
    route_markers: ["unit-speed", "arclength", "primitive loxodromic", "UNASSIGNED", "Route B", "CLOSED"]
  },
  "P30" => {
    directory: "papers/30-three-disk-nonconstant-roof-determinant",
    sources: 26,
    peer_reviewed: 24,
    verification_seat: "VERIFY-SEAT-C",
    route_markers: ["d=6a", "physical Euclidean flight length", "A0_FAIL", "A2_NOT_ELIGIBLE", "NO_ROUTE_PROMOTION"]
  },
  "P31" => {
    directory: "papers/31-level11-conjugacy-owner-ledger",
    sources: 22,
    peer_reviewed: 19,
    verification_seat: "VERIFY-SEAT-A",
    route_markers: ["Gamma_0(11)", "oriented", "powers are repetitions", "UNASSIGNED", "Route B"]
  },
  "P32" => {
    directory: "papers/32-homology-cover-renormalization-uniformity",
    sources: 26,
    peer_reviewed: 22,
    verification_seat: "VERIFY-SEAT-A",
    route_markers: ["1/N", "1/N^3", "primitive content-one", "UNASSIGNED", "Route B"]
  },
  "P33" => {
    directory: "papers/33-bolza-control-matched-census",
    sources: 20,
    peer_reviewed: 18,
    verification_seat: "VERIFY-SEAT-B",
    route_markers: ["b=1/2", "Lambda=21/10", "A0_INCONCLUSIVE_SYSTOLE_CONFOUNDED", "A0_CONTROL_PANEL_INCOMPLETE", "Route B"]
  }
}.freeze

INVENTORY_HEADERS = %w[
  source_id
  authors
  year
  title
  venue
  doi
  stable_url
  document_type
  peer_reviewed
  theme
  metadata_basis
  full_text_status
].freeze

VERIFICATION_HEADERS = %w[
  source_id
  existence_outcome
  metadata_match
  evidence_level
  claim_fitness_grade
  venue_assessment
  currency_assessment
  coi_assessment
  retraction_assessment
  support_class
  verified_locator
  notes
].freeze

ALLOWED_EXISTENCE_OUTCOMES = %w[
  S2_VERIFIED
  VERIFIED
  PLAUSIBLE
  UNVERIFIABLE
  FABRICATED
].freeze

ALLOWED_DISPOSITIONS = %w[
  PHASE2_SOURCE_BASE_READY
  PHASE2_SOURCE_BASE_READY_WITH_WARNINGS
  PHASE2_SOURCE_BASE_INSUFFICIENT
  PHASE2_INTEGRITY_BLOCK
].freeze

PHASE1_CHECKPOINT_HASHES = {
  "P29" => "1365f31ce44ebc45510700a1a1db2d9079c71408cbc41f8e390ee7753f477435",
  "P30" => "adb1d4dab9b270f9a40b4fb7eb0923fc2d6ce1d50de07d2441e12a8e091d0b5e",
  "P31" => "a81744824bc900a29c95edba3af0ef9c071f70e912927153477a8add35855ec1",
  "P32" => "6d5fb1b44fb2a15d98390381a59e4178655b459475a020e3b1d242929b75610f",
  "P33" => "a22657b85d0f2613d9c32f12ec1e92d835a0653cc8bfef48b01ff4f40dee5285"
}.freeze

UPSTREAM_HASHES = {
  "papers/24-bianchi-holonomy-flow/results/round7_trace_discriminant_ledger.csv" => "ac15fe34c25d7d570af48672c17989795c92ce4865ad74f2297fcb3c194bd632",
  "papers/25-three-disk-scattering-flow/results/three_disk_primitive_ledger_round2.csv" => "25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736",
  "papers/25-three-disk-scattering-flow/results/round8_exact_roof_witnesses.csv" => "53acd2d60db18909e36ad0ad7c1ee505874117d5fbb32eeda1fc374d15530ad5",
  "papers/25-three-disk-scattering-flow/results/round8_physical_roof_replay.csv" => "fa82c62ff34b8e674e78e37e800a5f31fdcbe3b986b37344a36719e30fa53e63",
  "papers/25-three-disk-scattering-flow/results/round8_roof_nontransfer_summary.json" => "39bb90334d57eee2e9fa3678cb5079b2d8f087d60c607a052955bb0303cd4295",
  "papers/26-level11-newform-time-change/results/round4_hecke_cycle_ledger.csv" => "f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662",
  "papers/26-level11-newform-time-change/results/round6_quadratic_degree_moment_ledger.csv" => "f95e1435c9293f8e008cebf80084ea2b522b76186dbd684b5e3997c5e588edea",
  "papers/26-level11-newform-time-change/results/round8_exact_instance_taxonomy_ledger.csv" => "beb363e4080b794e33ec6bc729b1f3e4dd7ef322be63fc59755e18fdf6bc889f",
  "papers/26-level11-newform-time-change/results/round8_exact_group_moment_taxonomy_ledger.csv" => "532e799686dd8afefa3a7529717208305fedede3f3e74e14ccf761ab35d74f69",
  "papers/26-level11-newform-time-change/results/round8_summary.json" => "4ba5de801dfd06c8b03bfe5fc07297b8c4e074bcf26c70ec6566de401ae2384d",
  "papers/27-congruence-inverse-limit-no-go/results/round5_cocompact_homology_escape_ledger.csv" => "0c74333b63f6027b16d134f19a320b8148e7fab6f86fa204d213c801106fe825",
  "papers/27-congruence-inverse-limit-no-go/results/round5_cocompact_homology_escape_validation.json" => "afdc51ca7ecfbd8777955c7438f08d4580e6b924419a807191e097b0292d9c10",
  "papers/27-congruence-inverse-limit-no-go/results/round8_renormalization_quadrants.csv" => "879ce8aec4e041e7cbba947706319511d99bb72592421584e76bbe47fad5ae57",
  "papers/27-congruence-inverse-limit-no-go/results/round8_renormalization_prefix_coefficients.csv" => "63f9632a0a715be26545e645a0f1d238e3ff24baec70fd8f478f1eda6c12c132",
  "papers/27-congruence-inverse-limit-no-go/results/round8_homology_renormalization_summary.json" => "c482c0e48fb1036faed37f123fbdec0b1c54f757a75f35e8a24cee27cb242b1a",
  "papers/28-bolza-magnetic-flow/notes/round3_trace_regime_contract.md" => "6fec628b7ec910296a81038d1f66a140b97c16113c29dce261b8e7b22d2ee5e0",
  "papers/28-bolza-magnetic-flow/results/round4_bolza_group_certificate.json" => "e3e6c486c66116dc6fe9fdd054c2fce9d4b1a58318f56d1656f6db168c807eca",
  "papers/28-bolza-magnetic-flow/results/round6_bolza_conjugacy_validation.json" => "ce8c751035b0f367c0f74594f93b0e5ed0bbec140897c8458cf5c9e11b9c8269",
  "papers/28-bolza-magnetic-flow/notes/round7_nonarithmetic_source_package_freeze.md" => "efdbeca3611b92863e1e8b8b1769a7d18c2ac4d839001275afb5b8db09c9255a",
  "papers/28-bolza-magnetic-flow/results/round7_nonarithmetic_control_matrices.json" => "a900749b6905a5f324c2e2670363ec1bc9480481f3f5aa1240ed0ebbee55e6ca",
  "papers/28-bolza-magnetic-flow/notes/round8_control_systole_completeness_freeze.md" => "b2655431dcc27c471e8da3c092435dbe30c6a483e2244f78543adcd2a3141528",
  "papers/28-bolza-magnetic-flow/results/round8_control_finite_ball_certificate.json" => "c1bf68a8a1485665680dba01d0012fb691c7ca1a795e36334639e34bbbdbcb1f",
  "papers/28-bolza-magnetic-flow/results/round8_control_systole_validation.json" => "4bf132b0d53e2cec329b26d0963f0e0f721c4c98fd4c58873b781bb5053e00c4"
}.freeze

PAPER_SKELETON_HASHES = {
  "papers/29-bianchi-ideal-owner-refinement/paper/manuscript.tex" => "7665c11cda3ee12d4310e51e69a9f47226777c85d761a5be0267340305f99fcf",
  "papers/29-bianchi-ideal-owner-refinement/paper/references.bib" => "ef60634ee003420e1b6273c2d11441d4623663597a66dcc75ec3b938c59e8b05",
  "papers/30-three-disk-nonconstant-roof-determinant/paper/manuscript.tex" => "2c50c1b734c54c3a6c4e1b2bd48f87d63de5f2be7cdf80811517e3d449df1ff9",
  "papers/30-three-disk-nonconstant-roof-determinant/paper/references.bib" => "ef60634ee003420e1b6273c2d11441d4623663597a66dcc75ec3b938c59e8b05",
  "papers/31-level11-conjugacy-owner-ledger/paper/manuscript.tex" => "4dc7ff031793aea9fb8d718d6594fde177e147961df0fcdceaea27e16bedba8a",
  "papers/31-level11-conjugacy-owner-ledger/paper/references.bib" => "89e0e523e50d4eb0848092cab77cff5a8e02f506a154e0ac86c64a985d83116b",
  "papers/32-homology-cover-renormalization-uniformity/paper/manuscript.tex" => "5ae25a297d02046f721c0bb6ef2be35534bc8bfe8268c660f767f0c558eb6f29",
  "papers/32-homology-cover-renormalization-uniformity/paper/references.bib" => "89e0e523e50d4eb0848092cab77cff5a8e02f506a154e0ac86c64a985d83116b",
  "papers/33-bolza-control-matched-census/paper/manuscript.tex" => "04afba2461431ae8d0f04f7fa73e6ccc8619cde856f9f06fe6418f692e236e97",
  "papers/33-bolza-control-matched-census/paper/references.bib" => "89e0e523e50d4eb0848092cab77cff5a8e02f506a154e0ac86c64a985d83116b"
}.freeze

VERIFICATION_CONTRACT_SHA256 = "41f3881f0fa428c3ce324a12f12bd514649aff652114cc436d5932fb3cb8b72e"
METADATA_CORRECTION_MANIFEST_SHA256 = "59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c"
METADATA_CORRECTION_RECEIPT_SHA256 = "c0d521739a482b2423a3b5af37e19841d6729fc963e99b089e0498edc1caddcb"
REPRODUCIBILITY_NOTE_SHA256 = "bb186dd95ae4eb54e795d17e128660685724b2929886d375847019d910bca447"

@checks = 0
@failures = []

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
  !value.nil? && !value.strip.empty?
end

def key_values(text, key)
  text.scan(/^#{Regexp.escape(key)}=([^\r\n]+)$/).flatten
end

def authoritative_report_dispositions(text)
  lines = text.lines
  results = []
  lines.each_with_index do |line, index|
    field = line.strip.match(/\A(?:Phase-2 )?Disposition:\s*\*\*`?([A-Z0-9_]+)`?\*\*\z/i)
    results << field[1] if field && ALLOWED_DISPOSITIONS.include?(field[1])
    next unless line.strip == "## Disposition"

    following = lines[(index + 1)..].to_a.map(&:strip).find { |candidate| !candidate.empty? }
    results << following if ALLOWED_DISPOSITIONS.include?(following)
  end
  results
end

def authoritative_checkpoint_dispositions(text)
  text.lines.filter_map do |line|
    stripped = line.strip
    field = stripped.match(/\A(?:Source-base|Phase-2) disposition:\s*\*\*`?([A-Z0-9_]+)`?\*\*\z/i)
    table = stripped.match(/\A\| Source-base disposition \| `?([A-Z0-9_]+)`? \|\z/)
    label = field&.[](1) || table&.[](1)
    label if ALLOWED_DISPOSITIONS.include?(label)
  end
end

authorization = "BATCH_ROUND10_STAGE1_PHASE2_AUTHORIZATION_20260902.txt"
check("Phase-2 authorization exists", File.file?(path(authorization)))
if File.file?(path(authorization))
  check("Phase-2 authorization bytes", read(authorization).bytes == "确认，开始下一轮\n".bytes)
  check(
    "Phase-2 authorization SHA-256",
    digest(authorization) == "b516a3f1c0b362a77ba7b5963375492d7bab73c746cb458086feb48638739a85"
  )
end

%w[
  BATCH_ROUND10_STAGE1_PHASE2_START.md
  BATCH_ROUND10_STAGE1_PHASE2_VERIFICATION_CONTRACT.md
  BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_RECEIPT.md
  BATCH_ROUND10_STAGE1_PHASE2_REPRODUCIBILITY_NOTE.md
  BATCH_ROUND10_STAGE1_PHASE2_CHECKPOINT.md
].each do |relative|
  check("#{relative} exists", File.file?(path(relative)))
end

check(
  "verification contract SHA-256 frozen",
  File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_VERIFICATION_CONTRACT.md")) &&
    digest("BATCH_ROUND10_STAGE1_PHASE2_VERIFICATION_CONTRACT.md") == VERIFICATION_CONTRACT_SHA256
)
check(
  "metadata correction manifest SHA-256 frozen",
  File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_MANIFEST.md")) &&
    digest("BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_MANIFEST.md") == METADATA_CORRECTION_MANIFEST_SHA256
)
check(
  "metadata correction receipt SHA-256 frozen",
  File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_RECEIPT.md")) &&
    digest("BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_RECEIPT.md") == METADATA_CORRECTION_RECEIPT_SHA256
)
check(
  "correction-chain reproducibility note SHA-256 frozen",
  File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_REPRODUCIBILITY_NOTE.md")) &&
    digest("BATCH_ROUND10_STAGE1_PHASE2_REPRODUCIBILITY_NOTE.md") == REPRODUCIBILITY_NOTE_SHA256
)
reproducibility_note = if File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_REPRODUCIBILITY_NOTE.md"))
                         read("BATCH_ROUND10_STAGE1_PHASE2_REPRODUCIBILITY_NOTE.md")
                       else
                         ""
                       end
check(
  "reproducibility note discloses missing complete prepatch bytes",
  key_values(reproducibility_note, "PREPATCH_COMPLETE_BYTES_RETAINED") == ["false"]
)
check(
  "reproducibility note preserves current-byte verification",
  key_values(reproducibility_note, "POSTPATCH_CURRENT_BYTES_VERIFIABLE") == ["true"]
)
check(
  "reproducibility note types historical replay",
  key_values(reproducibility_note, "HISTORICAL_REPLAY") == ["SEAT_ATTESTED"]
)

correction_receipt = if File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_RECEIPT.md"))
                       read("BATCH_ROUND10_STAGE1_PHASE2_METADATA_CORRECTION_RECEIPT.md")
                     else
                       ""
                     end
{
  "MANIFEST_SHA256" => METADATA_CORRECTION_MANIFEST_SHA256,
  "POST_RECHECK_STATUS" => "PASS",
  "SOURCE_ROWS" => "116/116",
  "VERIFICATION_ROWS" => "116/116",
  "PEER_REVIEWED_ROWS" => "100/116",
  "VERIFIED_OR_S2_VERIFIED" => "114/116",
  "PLAUSIBLE" => "2/116",
  "UNVERIFIABLE" => "0/116",
  "FABRICATED" => "0/116"
}.each do |key, expected|
  check("correction receipt #{key} exact once", key_values(correction_receipt, key) == [expected])
end
(1..6).each do |index|
  key = format("R10PH2_C%02d", index)
  check(
    "correction receipt #{key} resolved exact once",
    key_values(correction_receipt, key) == ["RESOLVED_POST_VERIFICATION"]
  )
end

total_sources = 0
total_peer_reviewed = 0
total_verified_rows = 0
total_existence_outcomes = Hash.new(0)

PAPERS.each do |paper, config|
  directory = config.fetch(:directory)
  notes = File.join(directory, "notes")
  bibliography_file = File.join(notes, "stage1_phase2_annotated_bibliography.md")
  inventory_file = File.join(notes, "stage1_phase2_source_inventory.tsv")
  verification_report_file = File.join(notes, "stage1_phase2_source_verification.md")
  verification_tsv_file = File.join(notes, "stage1_phase2_source_verification.tsv")
  checkpoint_file = File.join(notes, "stage1_phase2_checkpoint.md")
  state_file = File.join(notes, "pipeline_state.md")
  project_readme_file = File.join(directory, "README.md")
  phase1_checkpoint_file = File.join(notes, "stage1_phase1_checkpoint.md")

  [bibliography_file, inventory_file, verification_report_file,
   verification_tsv_file, checkpoint_file, state_file,
   project_readme_file, phase1_checkpoint_file].each do |relative|
    check("#{paper} #{File.basename(relative)} exists", File.file?(path(relative)))
  end

  next unless [bibliography_file, inventory_file, verification_report_file,
               verification_tsv_file, checkpoint_file, state_file,
               project_readme_file, phase1_checkpoint_file].all? { |relative| File.file?(path(relative)) }

  bibliography = read(bibliography_file)
  verification_report = read(verification_report_file)
  checkpoint = read(checkpoint_file)
  state = read(state_file)
  project_readme = read(project_readme_file)
  phase1_checkpoint = read(phase1_checkpoint_file)

  {
    "#{paper}_BIBLIOGRAPHY_POST_SHA256" => bibliography_file,
    "#{paper}_INVENTORY_POST_SHA256" => inventory_file,
    "#{paper}_VERIFICATION_MD_SHA256" => verification_report_file,
    "#{paper}_VERIFICATION_TSV_SHA256" => verification_tsv_file
  }.each do |key, relative|
    check("correction receipt binds #{key}", key_values(correction_receipt, key) == [digest(relative)])
  end

  check("#{paper} Phase-1 checkpoint hash frozen", digest(phase1_checkpoint_file) == PHASE1_CHECKPOINT_HASHES.fetch(paper))
  %w[
    stage1_phase1_rq_brief.md
    stage1_phase1_methodology_blueprint.md
    stage1_phase1_devils_advocate.md
    stage1_phase1_resolution.md
    stage1_phase1_devils_advocate_recheck.md
  ].each do |filename|
    relative = File.join(notes, filename)
    check("#{paper} #{filename} exists", File.file?(path(relative)))
    phase1_binding_rows = phase1_checkpoint.lines.select do |line|
      line.match?(/^\| `#{Regexp.escape(filename)}` \| `[0-9a-f]{64}` \|\s*$/)
    end
    check("#{paper} Phase-1 checkpoint has one #{filename} binding", phase1_binding_rows.length == 1)
    check(
      "#{paper} Phase-1 checkpoint still binds #{filename}",
      File.file?(path(relative)) &&
        phase1_binding_rows == ["| `#{filename}` | `#{digest(relative)}` |\n"]
    )
  end

  inventory = CSV.read(path(inventory_file), headers: true, col_sep: "\t")
  check("#{paper} inventory headers exact", inventory.headers == INVENTORY_HEADERS)
  check("#{paper} inventory source count", inventory.length == config.fetch(:sources))
  check("#{paper} inventory minimum source count", inventory.length >= 15)
  inventory_ids = inventory.map { |row| row["source_id"].to_s.strip }
  check("#{paper} inventory IDs nonblank", inventory_ids.all? { |id| nonblank?(id) })
  check("#{paper} inventory IDs unique", inventory_ids.uniq.length == inventory_ids.length)
  %w[authors year title venue stable_url document_type theme metadata_basis full_text_status].each do |field|
    check("#{paper} inventory #{field} complete", inventory.all? { |row| nonblank?(row[field]) })
  end
  peer_count = inventory.count { |row| row["peer_reviewed"].to_s.strip.downcase == "yes" }
  check("#{paper} peer-reviewed count", peer_count == config.fetch(:peer_reviewed))
  check("#{paper} peer-reviewed threshold", inventory.any? && peer_count.fdiv(inventory.length) >= 0.60)
  check("#{paper} peer-review values typed", inventory.all? { |row| %w[yes no].include?(row["peer_reviewed"].to_s.strip.downcase) })
  dois = inventory.map { |row| row["doi"].to_s.strip.downcase }.reject(&:empty?)
  urls = inventory.map { |row| row["stable_url"].to_s.strip }.reject(&:empty?)
  check("#{paper} DOI values unique", dois.uniq.length == dois.length)
  check("#{paper} stable locators unique", urls.uniq.length == urls.length)
  check("#{paper} bibliography records bounded search", bibliography.match?(/search protocol|bounded-search protocol/i))
  check("#{paper} bibliography records inclusion", bibliography.match?(/inclusion/i))
  check("#{paper} bibliography records exclusion", bibliography.match?(/exclusion/i))
  check("#{paper} bibliography records screening counts", bibliography.match?(/screening|screened/i))
  quoted_query_count = bibliography.scan(/^- \".+\"\s*$/).length
  check(
    "#{paper} bibliography records exact query strings",
    bibliography.match?(/queries|query families/i) &&
      (bibliography.include?("```text") || quoted_query_count >= 5)
  )
  check("#{paper} bibliography records search date", bibliography.include?("2026-09-02"))
  check("#{paper} bibliography records deduplication", bibliography.match?(/deduplication/i))
  check("#{paper} bibliography records distribution skew", bibliography.match?(/Distributional-skew advisory/i))
  check("#{paper} bibliography records limitations", bibliography.match?(/limitations/i))
  check("#{paper} bibliography forbids novelty from non-detection", bibliography.match?(/not.*novelty|novelty.*not|not.*evidence.*novelty/i))
  inventory_ids.each do |source_id|
    check("#{paper} bibliography contains #{source_id}", bibliography.include?(source_id))
  end

  verification = CSV.read(path(verification_tsv_file), headers: true, col_sep: "\t")
  check("#{paper} verification headers exact", verification.headers == VERIFICATION_HEADERS)
  check("#{paper} verification row count", verification.length == inventory.length)
  verification_ids = verification.map { |row| row["source_id"].to_s.strip }
  check("#{paper} verification IDs unique", verification_ids.uniq.length == verification_ids.length)
  check("#{paper} verification IDs equal inventory", verification_ids.sort == inventory_ids.sort)
  verification.each do |row|
    source_id = row["source_id"].to_s.strip
    outcome = row["existence_outcome"].to_s.strip
    total_existence_outcomes[outcome] += 1
    check("#{paper} #{source_id} existence outcome allowed", ALLOWED_EXISTENCE_OUTCOMES.include?(outcome))
    check("#{paper} #{source_id} metadata match recorded", nonblank?(row["metadata_match"]))
    if %w[VERIFIED S2_VERIFIED].include?(outcome)
      check(
        "#{paper} #{source_id} verified metadata match is exact/resolved",
        row["metadata_match"].to_s.strip.match?(/\A(?:EXACT(?:_[A-Z0-9]+)*|RESOLVED_POST_VERIFICATION)\z/)
      )
    end
    check("#{paper} #{source_id} evidence level I-VII", %w[I II III IV V VI VII].include?(row["evidence_level"].to_s.strip))
    check("#{paper} #{source_id} claim fitness A-F", row["claim_fitness_grade"].to_s.strip.match?(/\A[A-F]\z/))
    %w[venue_assessment currency_assessment coi_assessment retraction_assessment support_class verified_locator notes].each do |field|
      check("#{paper} #{source_id} #{field} recorded", nonblank?(row[field]))
    end
    if outcome == "S2_VERIFIED"
      row_notes = row["notes"].to_s
      paper_id = row_notes.match(/paperId\s+([0-9a-f]{40})/i)
      similarity = row_notes.match(/(?:normalized-title\s+)?similarity\s+([01](?:\.\d+)?)/i)
      s2_year = row_notes.match(/(?:S2\s+)?year\s+(\d{4})/i)
      inventory_row = inventory.find { |candidate| candidate["source_id"].to_s.strip == source_id }
      check("#{paper} #{source_id} S2 paper ID documented", !paper_id.nil?)
      check("#{paper} #{source_id} S2 similarity documented", similarity && similarity[1].to_f.between?(0.70, 1.0))
      check(
        "#{paper} #{source_id} S2 year within one",
        s2_year && inventory_row && (s2_year[1].to_i - inventory_row["year"].to_i).abs <= 1
      )
    elsif outcome == "PLAUSIBLE"
      inventory_row = inventory.find { |candidate| candidate["source_id"].to_s.strip == source_id }
      combined = [row["metadata_match"], row["venue_assessment"], row["verified_locator"], row["notes"]].join(" ")
      check("#{paper} #{source_id} PLAUSIBLE has no inventory DOI", inventory_row && inventory_row["doi"].to_s.strip.empty?)
      check("#{paper} #{source_id} PLAUSIBLE has authoritative exact-title basis", combined.match?(/authoritative|catalog|journal|archive|institution/i) && combined.match?(/exact/i))
      check("#{paper} #{source_id} PLAUSIBLE has stable locator", row["verified_locator"].to_s.match?(/\Ahttps?:\/\//))
    end
  end
  total_verified_rows += verification.length

  dispositions = authoritative_report_dispositions(verification_report)
  check("#{paper} exactly one authoritative Phase-2 disposition", dispositions.length == 1)
  check(
    "#{paper} disposition permits Phase-2 closeout awaiting Phase 3",
    dispositions.length == 1 &&
      %w[PHASE2_SOURCE_BASE_READY PHASE2_SOURCE_BASE_READY_WITH_WARNINGS].include?(dispositions.first)
  )
  check("#{paper} verification seat exact", verification_report.include?(config.fetch(:verification_seat)))
  check("#{paper} verification binds contract", verification_report.include?(VERIFICATION_CONTRACT_SHA256))
  check("#{paper} verification binds correction manifest", verification_report.include?(METADATA_CORRECTION_MANIFEST_SHA256))
  if verification.any? { |row| row["existence_outcome"].to_s.strip == "FABRICATED" }
    check("#{paper} fabricated source forces integrity block", dispositions == ["PHASE2_INTEGRITY_BLOCK"])
  end
  if verification.any? { |row| row["existence_outcome"].to_s.strip == "UNVERIFIABLE" }
    check("#{paper} unverifiable source cannot receive warning-free READY", dispositions != ["PHASE2_SOURCE_BASE_READY"])
  end
  check("#{paper} verification report has support boundary", verification_report.match?(/support|支持/i) && verification_report.match?(/cannot|does not|不能|不支持/i))
  check(
    "#{paper} verification report has limitations",
    verification_report.match?(/limitation|\blimits\b|NOT_CHECKED|限制/i)
  )
  check(
    "#{paper} verification report denies novelty verdict",
    verification_report.match?(/not.*novelty|novelty.*not|no\b.{0,80}\bnovelty/i)
  )

  checkpoint_dispositions = authoritative_checkpoint_dispositions(checkpoint)
  check("#{paper} checkpoint has one authoritative disposition", checkpoint_dispositions.length == 1)
  check("#{paper} checkpoint disposition matches verifier", checkpoint_dispositions == dispositions)

  [bibliography_file, inventory_file, verification_report_file, verification_tsv_file].each do |relative|
    basename = File.basename(relative)
    phase2_binding_rows = checkpoint.lines.select do |line|
      line.match?(/^\| `#{Regexp.escape(basename)}` \| `[0-9a-f]{64}` \|\s*$/)
    end
    check("#{paper} checkpoint has one #{basename} binding", phase2_binding_rows.length == 1)
    check(
      "#{paper} checkpoint binds #{basename}",
      phase2_binding_rows == ["| `#{basename}` | `#{digest(relative)}` |\n"]
    )
  end
  check("#{paper} checkpoint Phase 2 complete", checkpoint.include?("PHASE_2_COMPLETE"))
  check("#{paper} checkpoint awaits Phase 3", checkpoint.include?("AWAITING_PHASE_3_CONFIRMATION"))
  check("#{paper} checkpoint binds authorization", checkpoint.include?("b516a3f1c0b362a77ba7b5963375492d7bab73c746cb458086feb48638739a85"))
  check("#{paper} checkpoint binds correction receipt", checkpoint.include?(METADATA_CORRECTION_RECEIPT_SHA256))
  check("#{paper} checkpoint records source count", checkpoint.match?(/^\|\s*Included unique sources\s*\|\s*#{config.fetch(:sources)}\s*\|\s*$/))
  check("#{paper} checkpoint records peer count", checkpoint.match?(/^\|\s*Peer-reviewed sources\s*\|\s*#{config.fetch(:peer_reviewed)}\s*\|\s*$/))
  check("#{paper} checkpoint keeps computation stopped", checkpoint.match?(/Scientific computation.*NOT_RUN|SCIENTIFIC_COMPUTATION=NOT_RUN/i))
  check("#{paper} checkpoint keeps novelty open", checkpoint.match?(/Novelty.*NOT_RUN|NOVELTY.*NOT_RUN|no novelty/i))
  check(
    "#{paper} has no Phase-3 authorization promotion",
    !(checkpoint + state + project_readme).match?(/PHASE_3_AUTHORIZED\s*=\s*true/i)
  )
  formal_tuple_rows = state.lines.select { |line| line.start_with?("| Formal Route-A tuple |") }
  check("#{paper} state has exactly one formal tuple row", formal_tuple_rows.length == 1)
  check("#{paper} formal tuple remains unassigned", formal_tuple_rows.first.to_s.include?("UNASSIGNED"))
  closeout_text = checkpoint + state + project_readme
  check(
    "#{paper} has no conflicting Route-B promotion",
    !closeout_text.match?(/ROUTE_B(?:_STATUS)?\s*=\s*OPEN|\| Route B \|[^\n]*\bOPEN\b|Route B is\s+`?OPEN|invocation(?: allowed)?\s+`?true/i)
  )
  check(
    "#{paper} has no conflicting assigned-tuple count",
    !closeout_text.match?(/FORMAL_ROUTE_A_TUPLES\s*=\s*[1-9]/i)
  )
  config.fetch(:route_markers).each do |marker|
    check("#{paper} route marker #{marker}", (checkpoint + state + project_readme).include?(marker))
  end

  controlling_states = state.scan(/^Current controlling state:\s*\*\*(.+?)\*\*\.?\s*$/).flatten
  check("#{paper} state has one controlling state", controlling_states.length == 1)
  check("#{paper} state Phase 2 complete", controlling_states == ["STAGE 1 RESEARCH / PHASE_2_COMPLETE / AWAITING_PHASE_3_CONFIRMATION"])
  check("#{paper} state awaits Phase 3", state.match?(/^\| Phase 3 \| `AWAITING_PHASE_3_CONFIRMATION`; not authorized \|$/))
  check("#{paper} pipeline is awaiting confirmation", state.match?(/^\| Pipeline global state \| `awaiting_confirmation` \|$/))
  check("#{paper} state keeps computation stopped", state.match?(/computation.*NOT_RUN/i))
  check("#{paper} state keeps Route B closed", state.match?(/^\| Route B \| `CLOSED`; evaluation `NOT_RUN`; invocation `false` \|$/))
  check("#{paper} project README records Phase 2", project_readme.match?(/PHASE 2 COMPLETE|Phase-2 source/i))
  check("#{paper} project README links Phase-2 checkpoint", project_readme.include?("stage1_phase2_checkpoint.md"))

  later_phase_files = Dir.glob(path(File.join(directory, "**", "*")), File::FNM_DOTMATCH).select do |candidate|
    basename = File.basename(candidate).downcase
    File.file?(candidate) && basename.match?(/phase[-_]?3|synthesis/)
  end
  check("#{paper} has no Phase-3/synthesis artifact", later_phase_files.empty?)
  allowed_project_files = %w[
    README.md
    code/.gitkeep
    experiments/.gitkeep
    notes/pipeline_state.md
    notes/stage1_phase1_checkpoint.md
    notes/stage1_phase1_devils_advocate.md
    notes/stage1_phase1_devils_advocate_recheck.md
    notes/stage1_phase1_methodology_blueprint.md
    notes/stage1_phase1_resolution.md
    notes/stage1_phase1_rq_brief.md
    notes/stage1_phase2_annotated_bibliography.md
    notes/stage1_phase2_checkpoint.md
    notes/stage1_phase2_source_inventory.tsv
    notes/stage1_phase2_source_verification.md
    notes/stage1_phase2_source_verification.tsv
    notes/stage1_prestart_brief.md
    paper/figures/.gitkeep
    paper/manuscript.tex
    paper/references.bib
    results/.gitkeep
  ].sort
  actual_project_files = Dir.glob(path(File.join(directory, "**", "*")), File::FNM_DOTMATCH)
                            .select { |candidate| File.file?(candidate) }
                            .map { |candidate| candidate.delete_prefix("#{path(directory)}/") }
                            .sort
  check("#{paper} project file set is Phase-2 exact", actual_project_files == allowed_project_files)
  execution_files = %w[code experiments results].flat_map do |subdirectory|
    Dir.glob(path(File.join(directory, subdirectory, "**", "*")), File::FNM_DOTMATCH).select do |candidate|
      File.file?(candidate) && File.basename(candidate) != ".gitkeep"
    end
  end
  check("#{paper} has no computation/experiment output", execution_files.empty?)
  total_sources += inventory.length
  total_peer_reviewed += peer_count
end

PAPER_SKELETON_HASHES.each do |relative, expected|
  check("paper skeleton exists: #{relative}", File.file?(path(relative)))
  check("paper skeleton remains frozen: #{relative}", File.file?(path(relative)) && digest(relative) == expected)
end

UPSTREAM_HASHES.each do |relative, expected|
  check("upstream file exists: #{relative}", File.file?(path(relative)))
  check("upstream hash frozen: #{relative}", File.file?(path(relative)) && digest(relative) == expected)
end

check("total source count", total_sources == 116)
check("total peer-reviewed count", total_peer_reviewed == 100)
check("total verification row count", total_verified_rows == 116)
{
  "VERIFIED" => 105,
  "S2_VERIFIED" => 9,
  "PLAUSIBLE" => 2,
  "UNVERIFIABLE" => 0,
  "FABRICATED" => 0
}.each do |outcome, expected|
  check("total #{outcome} outcome count", total_existence_outcomes[outcome] == expected)
end
check(
  "no unexpected existence outcome aggregate",
  (total_existence_outcomes.keys - ALLOWED_EXISTENCE_OUTCOMES).empty?
)

root_readme = File.file?(path("README.md")) ? read("README.md") : ""
registry = File.file?(path("docs/candidate_registry.md")) ? read("docs/candidate_registry.md") : ""
batch_checkpoint = File.file?(path("BATCH_ROUND10_STAGE1_PHASE2_CHECKPOINT.md")) ? read("BATCH_ROUND10_STAGE1_PHASE2_CHECKPOINT.md") : ""

check("root README references Phase-2 checkpoint", root_readme.include?("BATCH_ROUND10_STAGE1_PHASE2_CHECKPOINT.md"))
check("root README records Round-10 source count", root_readme.include?("ROUND10_PHASE2_SOURCE_ROWS=116/116"))
check("root README records Round-10 peer-reviewed count", root_readme.include?("ROUND10_PHASE2_PEER_REVIEWED=100/116"))
round10_index_rows = root_readme.lines.select { |line| line.start_with?("| `29--33` ") }
check("root README has exactly one Round-10 index row", round10_index_rows.length == 1)
check(
  "root README Round-10 index is current Phase 2",
  round10_index_rows.first.to_s.include?("Stage 1 Phase 2 complete") &&
    round10_index_rows.first.to_s.include?("Phase 3")
)
check("root README has no stale Phase-2 confirmation state", !root_readme.include?("AWAITING_PHASE_2_CONFIRMATION"))
check("root README has no stale wait-to-enter-Phase-2 text", !root_readme.match?(/等待确认进入 Phase 2|才允许进入 Phase 2 文献/))
check("registry references Phase-2 checkpoint", registry.include?("BATCH_ROUND10_STAGE1_PHASE2_CHECKPOINT.md"))
check("batch checkpoint binds correction receipt", batch_checkpoint.include?(METADATA_CORRECTION_RECEIPT_SHA256))
check("batch checkpoint binds reproducibility limitation", batch_checkpoint.include?(REPRODUCIBILITY_NOTE_SHA256))
PAPERS.each do |paper, config|
  paper_checkpoint = File.join(config.fetch(:directory), "notes", "stage1_phase2_checkpoint.md")
  checkpoint_rows = batch_checkpoint.lines.select do |line|
    line.match?(/^\| #{paper} \| `[0-9a-f]{64}` \|/)
  end
  check("batch checkpoint has exactly one #{paper} hash row", checkpoint_rows.length == 1)
  check(
    "batch checkpoint binds #{paper} checkpoint hash",
    File.file?(path(paper_checkpoint)) &&
      checkpoint_rows == ["| #{paper} | `#{digest(paper_checkpoint)}` | `PHASE2_SOURCE_BASE_READY_WITH_WARNINGS` |\n"]
  )
end
%w[
  P29-BIANCHI-IDEAL-OWNER-REFINEMENT
  P30-THREE-DISK-NONCONSTANT-ROOF-DETERMINANT
  P31-LEVEL11-CONJUGACY-OWNER-LEDGER
  P32-HOMOLOGY-COVER-RENORMALIZATION-UNIFORMITY
  P33-BOLZA-CONTROL-MATCHED-CENSUS
].each do |candidate|
  rows = registry.lines.select { |line| line.start_with?("| `#{candidate}` |") }
  check("registry #{candidate} occurs exactly once", rows.length == 1)
  row = rows.first.to_s
  check("registry #{candidate} awaits Phase 3", row.include?("AWAITING_PHASE_3_CONFIRMATION"))
  check("registry #{candidate} binds Phase-2 checkpoint", row.include?("BATCH_ROUND10_STAGE1_PHASE2_CHECKPOINT.md"))
  check(
    "registry #{candidate} has no conflicting later-phase or Route-B promotion",
    !row.match?(/PHASE_3_COMPLETE|PHASE_3_AUTHORIZED\s*=\s*true|Route B[^|]*\bOPEN\b|ROUTE_B[^|]*\bOPEN\b/i)
  )
end
{
  "SOURCE_ROWS" => "116/116",
  "VERIFICATION_ROWS" => "116/116",
  "SCIENTIFIC_COMPUTATION" => "NOT_RUN",
  "NOVELTY_ASSESSMENT" => "NOT_RUN",
  "CLAIM_REGISTRATION" => "0/5",
  "FORMAL_ROUTE_A_TUPLES" => "0/5",
  "POSITIVE_ARITHMETIC_A2" => "0/5",
  "ROUTE_B_INVOCATIONS" => "0/5",
  "PHASE_3_AUTHORIZED" => "false",
  "NEXT_GATE" => "PHASE_3_USER_CONFIRMATION"
}.each do |key, expected|
  values = key_values(batch_checkpoint, key)
  check("batch checkpoint #{key} occurs once", values.length == 1)
  check("batch checkpoint #{key} exact", values == [expected])
end

later_phase_batch_files = Dir.glob(path("BATCH_ROUND10*")).select do |candidate|
  basename = File.basename(candidate).downcase
  basename.match?(/phase[-_]?3.*(?:authorization|start)|(?:authorization|start).*phase[-_]?3/)
end
check("no Round-10 Phase-3 authorization/start artifact", later_phase_batch_files.empty?)

route_files = (
  Dir.glob(path("evaluations/route_a/**/*")) +
  Dir.glob(path("evaluations/route_b/**/*"))
).select { |candidate| File.file?(candidate) }
PAPERS.each do |paper, config|
  candidate_slug = File.basename(config.fetch(:directory)).sub(/^\d+-/, "")
  route_artifacts = route_files.select do |candidate|
    relative = candidate.delete_prefix("#{ROOT}/")
    searchable = relative + "\n" + File.binread(candidate).force_encoding(Encoding::UTF_8).scrub
    searchable.match?(/(?<![A-Z0-9])#{paper}(?![A-Z0-9])/i) || searchable.downcase.include?(candidate_slug.downcase)
  end
  check("#{paper} has no new formal Route artifact by path or content", route_artifacts.empty?)
end

if @failures.empty?
  puts "ROUND10_STAGE1_PHASE2_AUDIT=PASS checks=#{@checks} failures=0 sources=#{total_sources} peer_reviewed=#{total_peer_reviewed} verification_rows=#{total_verified_rows}"
  exit 0
end

warn "ROUND10_STAGE1_PHASE2_AUDIT=FAIL checks=#{@checks} failures=#{@failures.length} sources=#{total_sources} peer_reviewed=#{total_peer_reviewed} verification_rows=#{total_verified_rows}"
@failures.each { |failure| warn "- #{failure}" }
exit 1
