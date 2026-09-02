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
    synthesis_seat: "SYNTH-SEAT-A",
    da_seat: "DA-SEAT-C",
    phase1_checkpoint_sha256: "1365f31ce44ebc45510700a1a1db2d9079c71408cbc41f8e390ee7753f477435",
    phase2_checkpoint_sha256: "a9847cd300102f05927923dc3f7ac67d95987656413afc27ffc9bf172bb0e2dc",
    route_markers: ["unit-speed", "arclength", "primitive loxodromic", "Gaussian prime ideals", "UNASSIGNED"]
  },
  "P30" => {
    directory: "papers/30-three-disk-nonconstant-roof-determinant",
    sources: 26,
    synthesis_seat: "SYNTH-SEAT-A",
    da_seat: "DA-SEAT-C",
    phase1_checkpoint_sha256: "adb1d4dab9b270f9a40b4fb7eb0923fc2d6ce1d50de07d2441e12a8e091d0b5e",
    phase2_checkpoint_sha256: "4a8bfd6ee234f752b607c62fa9582139e17f8a0be9dc9dd478c7e381aaaed3d0",
    route_markers: ["d=6a", "physical Euclidean flight length", "A0_FAIL", "A2_NOT_ELIGIBLE", "NO_ROUTE_PROMOTION"]
  },
  "P31" => {
    directory: "papers/31-level11-conjugacy-owner-ledger",
    sources: 22,
    synthesis_seat: "SYNTH-SEAT-B",
    da_seat: "DA-SEAT-A",
    phase1_checkpoint_sha256: "a81744824bc900a29c95edba3af0ef9c071f70e912927153477a8add35855ec1",
    phase2_checkpoint_sha256: "e79049403dae8aca8607f59413731a570638f20c2160ce2bb7f40037341560e7",
    route_markers: ["Gamma_0(11)", "oriented", "9,453", "A1", "UNASSIGNED"]
  },
  "P32" => {
    directory: "papers/32-homology-cover-renormalization-uniformity",
    sources: 26,
    synthesis_seat: "SYNTH-SEAT-B",
    da_seat: "DA-SEAT-A",
    phase1_checkpoint_sha256: "6d5fb1b44fb2a15d98390381a59e4178655b459475a020e3b1d242929b75610f",
    phase2_checkpoint_sha256: "688a7048f5cabc0f4ff64bf8fcb78a6692dfd775219382d18fdbdbf2c4bcc534",
    route_markers: ["1/N", "1/N^3", "content-one", "A0", "UNASSIGNED"]
  },
  "P33" => {
    directory: "papers/33-bolza-control-matched-census",
    sources: 20,
    synthesis_seat: "SYNTH-SEAT-C",
    da_seat: "DA-SEAT-B",
    phase1_checkpoint_sha256: "a22657b85d0f2613d9c32f12ec1e92d835a0653cc8bfef48b01ff4f40dee5285",
    phase2_checkpoint_sha256: "19cc93b6055f0a657de62bb28bcd4cc0556296658c68722d42b8d1c3c91b2d39",
    route_markers: ["b=1/2", "Lambda=21/10", "A0_INCONCLUSIVE_SYSTOLE_CONFOUNDED", "A0_CONTROL_PANEL_INCOMPLETE", "P33-RC-1"]
  }
}.freeze

MATRIX_HEADERS = %w[
  source_id
  authors_year
  theme
  existence_outcome
  claim_fitness_grade
  support_class
  admissible_contribution
  excluded_stronger_claim
  compatibility_role
  locator_or_verification_limit
].freeze

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

PHASE2_INPUTS = %w[
  stage1_phase2_annotated_bibliography.md
  stage1_phase2_source_inventory.tsv
  stage1_phase2_source_verification.md
  stage1_phase2_source_verification.tsv
].freeze

PHASE3_CORE = %w[
  stage1_phase3_claim_intent_manifest.json
  stage1_phase3_literature_matrix.tsv
  stage1_phase3_synthesis.md
].freeze

SKELETON_HASHES = {
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

AUTHORIZATION_SHA256 = "f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe"
CONTRACT_SHA256 = "2607c63b04c48584827825312f14f36fe852c358191d4abcb4cd882c54a75e1f"
START_SHA256 = "6e67b347e6cfecbac7dcdfc7debb78f19e43a54d5f937efe7e7d42d2005df554"
PHASE2_RECEIPT_SHA256 = "8e0b8660f303256df8a11840c094d520112fbf8bff1d29db16a29a513d8ec521"

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

def table_hash(text, basename)
  matches = text.scan(/^\| `#{Regexp.escape(basename)}` \| `([0-9a-f]{64})` \|$/).flatten
  matches.length == 1 ? matches.first : nil
end

authorization = "BATCH_ROUND10_STAGE1_PHASE3_AUTHORIZATION_20260902.txt"
check("Phase-3 authorization exists", File.file?(path(authorization)))
if File.file?(path(authorization))
  check("Phase-3 authorization exact bytes", read(authorization).bytes == "确认\n".bytes)
  check("Phase-3 authorization SHA-256", digest(authorization) == AUTHORIZATION_SHA256)
end

{
  "BATCH_ROUND10_STAGE1_PHASE3_SYNTHESIS_CONTRACT.md" => CONTRACT_SHA256,
  "BATCH_ROUND10_STAGE1_PHASE3_START.md" => START_SHA256,
  "BATCH_ROUND10_STAGE1_PHASE2_AUDIT_RECEIPT.json" => PHASE2_RECEIPT_SHA256
}.each do |relative, expected|
  check("#{relative} exists", File.file?(path(relative)))
  check("#{relative} frozen SHA-256", File.file?(path(relative)) && digest(relative) == expected)
end

manifest_ids = []
total_matrix_rows = 0
total_refs = 0

PAPERS.each do |paper_id, config|
  directory = config.fetch(:directory)
  notes = "#{directory}/notes"
  phase1_checkpoint = "#{notes}/stage1_phase1_checkpoint.md"
  phase2_checkpoint = "#{notes}/stage1_phase2_checkpoint.md"

  check("#{paper_id} Phase-1 checkpoint frozen", File.file?(path(phase1_checkpoint)) && digest(phase1_checkpoint) == config.fetch(:phase1_checkpoint_sha256))
  check("#{paper_id} Phase-2 checkpoint frozen", File.file?(path(phase2_checkpoint)) && digest(phase2_checkpoint) == config.fetch(:phase2_checkpoint_sha256))

  checkpoint_text = File.file?(path(phase2_checkpoint)) ? read(phase2_checkpoint) : ""
  PHASE2_INPUTS.each do |basename|
    relative = "#{notes}/#{basename}"
    expected = table_hash(checkpoint_text, basename)
    check("#{paper_id} #{basename} has unique Phase-2 hash binding", !expected.nil?)
    check("#{paper_id} #{basename} matches Phase-2 hash binding", !expected.nil? && File.file?(path(relative)) && digest(relative) == expected)
  end

  PHASE3_CORE.each do |basename|
    check("#{paper_id} #{basename} exists", File.file?(path("#{notes}/#{basename}")))
  end

  inventory_relative = "#{notes}/stage1_phase2_source_inventory.tsv"
  verification_relative = "#{notes}/stage1_phase2_source_verification.tsv"
  matrix_relative = "#{notes}/stage1_phase3_literature_matrix.tsv"
  manifest_relative = "#{notes}/stage1_phase3_claim_intent_manifest.json"
  synthesis_relative = "#{notes}/stage1_phase3_synthesis.md"

  inventory = CSV.read(path(inventory_relative), headers: true, col_sep: "\t", liberal_parsing: true)
  verification = CSV.read(path(verification_relative), headers: true, col_sep: "\t", liberal_parsing: true)
  source_ids = inventory.map { |row| row["source_id"] }
  verification_by_id = verification.to_h { |row| [row["source_id"], row] }
  check("#{paper_id} upstream source count", source_ids.length == config.fetch(:sources))
  check("#{paper_id} upstream source IDs unique", source_ids.uniq.length == source_ids.length)

  begin
    manifest = JSON.parse(read(manifest_relative))
    check("#{paper_id} manifest only allowed top keys", (manifest.keys - MANIFEST_TOP_KEYS).empty?)
    check("#{paper_id} manifest required top keys", (MANIFEST_REQUIRED_KEYS - manifest.keys).empty?)
    check("#{paper_id} manifest version", manifest["manifest_version"] == "1.0")
    check("#{paper_id} manifest emitted by synthesis agent", manifest["emitted_by"] == "synthesis_agent")
    check("#{paper_id} manifest ID syntax", manifest["manifest_id"].is_a?(String) && manifest["manifest_id"].match?(/\AM-\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z-[0-9a-f]{4}\z/))
    manifest_ids << manifest["manifest_id"]
    time_valid = begin
      Time.iso8601(manifest.fetch("emitted_at"))
      true
    rescue ArgumentError, KeyError
      false
    end
    check("#{paper_id} manifest emitted_at", time_valid)
    claims = manifest["claims"]
    check("#{paper_id} manifest claims nonempty", claims.is_a?(Array) && !claims.empty?)
    claim_ids = claims.is_a?(Array) ? claims.map { |claim| claim["claim_id"] } : []
    check("#{paper_id} manifest claim IDs unique", claim_ids.uniq.length == claim_ids.length)
    claims.to_a.each do |claim|
      claim_id = claim["claim_id"] || "missing"
      check("#{paper_id} #{claim_id} allowed claim keys", (claim.keys - CLAIM_ALLOWED_KEYS).empty?)
      check("#{paper_id} #{claim_id} required claim keys", (CLAIM_REQUIRED_KEYS - claim.keys).empty?)
      check("#{paper_id} #{claim_id} ID syntax", claim_id.match?(/\AC-\d{3,}\z/))
      check("#{paper_id} #{claim_id} text nonblank", nonblank?(claim["claim_text"]))
      check("#{paper_id} #{claim_id} evidence kind", EVIDENCE_KINDS.include?(claim["intended_evidence_kind"]))
      planned_refs = claim["planned_refs"]
      check("#{paper_id} #{claim_id} planned refs array", planned_refs.is_a?(Array))
      check("#{paper_id} #{claim_id} planned refs resolve", planned_refs.is_a?(Array) && (planned_refs - source_ids).empty?)
      check("#{paper_id} #{claim_id} no experiment IDs", !claim.key?("planned_experiment_ids"))
      claim.fetch("negative_constraints", []).each do |constraint|
        expected_digits = claim_id.delete_prefix("C-")
        check("#{paper_id} #{claim_id} claim constraint ID", constraint["constraint_id"].to_s.match?(/\ANC-C#{Regexp.escape(expected_digits)}-\d+\z/))
        check("#{paper_id} #{claim_id} claim constraint rule", nonblank?(constraint["rule"]))
      end
    end
    global_constraints = manifest["manifest_negative_constraints"]
    check("#{paper_id} global constraints nonempty", global_constraints.is_a?(Array) && !global_constraints.empty?)
    global_constraints.to_a.each do |constraint|
      check("#{paper_id} global constraint ID", constraint["constraint_id"].to_s.match?(/\AMNC-\d+\z/))
      check("#{paper_id} global constraint rule", nonblank?(constraint["rule"]))
    end
  rescue JSON::ParserError => error
    check("#{paper_id} manifest parses: #{error.message}", false)
  end

  matrix = CSV.read(path(matrix_relative), headers: true, col_sep: "\t", liberal_parsing: true)
  check("#{paper_id} matrix exact header", matrix.headers == MATRIX_HEADERS)
  check("#{paper_id} matrix row count", matrix.length == config.fetch(:sources))
  matrix_ids = matrix.map { |row| row["source_id"] }
  check("#{paper_id} matrix IDs exact", matrix_ids.sort == source_ids.sort)
  check("#{paper_id} matrix IDs unique", matrix_ids.uniq.length == matrix_ids.length)
  matrix.each do |row|
    source_id = row["source_id"] || "missing"
    check("#{paper_id} matrix #{source_id} fields nonblank", MATRIX_HEADERS.all? { |header| nonblank?(row[header]) })
    verification_row = verification_by_id[source_id]
    check("#{paper_id} matrix #{source_id} verification row resolves", !verification_row.nil?)
    if verification_row
      check("#{paper_id} matrix #{source_id} existence outcome", row["existence_outcome"] == verification_row["existence_outcome"])
      check("#{paper_id} matrix #{source_id} claim fitness", row["claim_fitness_grade"] == verification_row["claim_fitness_grade"])
      check("#{paper_id} matrix #{source_id} support class", row["support_class"] == verification_row["support_class"])
    end
  end
  total_matrix_rows += matrix.length

  synthesis = read(synthesis_relative)
  check("#{paper_id} synthesis seat", synthesis.include?(config.fetch(:synthesis_seat)))
  theme_count = synthesis.scan(/^(?:##|###|####) Theme \d+/).length
  check("#{paper_id} synthesis has 3-7 themes", theme_count.between?(3, 7))
  {
    "consensus" => /^## .*Consensus/i,
    "debates" => /^## .*Debates/i,
    "contradictions" => /^## .*Contradictions/i,
    "research gaps" => /^## .*Research gaps/i,
    "methodology recommendations" => /^## .*Methodology recommendations/i,
    "theoretical implications" => /^## .*Theoretical implications/i,
    "concrete advance" => /Concrete Phase-3 advance/i
  }.each do |name, pattern|
    check("#{paper_id} synthesis section #{name}", synthesis.match?(pattern))
  end

  ref_count = synthesis.scan(/<!--ref:/).length
  anchor_count = synthesis.scan(/<!--anchor:/).length
  pairs = synthesis.scan(/<!--ref:([^>]+)--><!--anchor:([^>]+)-->/)
  check("#{paper_id} citation comments paired", ref_count == anchor_count && ref_count == pairs.length && ref_count.positive?)
  cited_ids = pairs.map(&:first)
  check("#{paper_id} citation IDs resolve", (cited_ids - source_ids).empty?)
  check("#{paper_id} citations use disclosed no-locator state", pairs.all? { |_source_id, anchor| anchor == "none" })
  total_refs += pairs.length
  pending_count = synthesis.scan(/scholar_confirmation:\s*["']?pending["']?/).length
  check("#{paper_id} bounded tension inventory present", pending_count >= 3)
  plain_synthesis = synthesis.delete("*`")
  check("#{paper_id} tension inventory explicitly non-exhaustive", plain_synthesis.match?(/not (?:an )?exhaustive|not complete pairwise|not exhaustive pairwise/i))
  check("#{paper_id} no partial passport masquerade", !synthesis.match?(/^(?:##|###|####) Material Passport\s*$/))
  check("#{paper_id} search absence not novelty", synthesis.match?(/not.{0,80}novelty|novelty.{0,80}(?:not|neither)|do not establish novelty/i))
  check("#{paper_id} scientific computation remains not run", synthesis.match?(/SCIENTIFIC_COMPUTATION=NOT_RUN|Scientific computation:\s*`?NOT_RUN/i))
  check("#{paper_id} formal claim registration remains zero", synthesis.match?(/FORMAL_PROJECT_CLAIM_REGISTRATION=0|Formal project claim registration:\s*`?0/i))
  check("#{paper_id} Route B remains closed", synthesis.match?(/ROUTE_B_(?:INVOCATIONS=0\/1|INVOCATION=false)|Route B is closed/i))
  config.fetch(:route_markers).each do |marker|
    check("#{paper_id} synthesis preserves route marker #{marker}", synthesis.downcase.include?(marker.downcase))
  end

  da_relative = "#{notes}/stage1_phase3_devils_advocate.md"
  check("#{paper_id} independent DA report exists", File.file?(path(da_relative)))
  if File.file?(path(da_relative))
    da = read(da_relative)
    check("#{paper_id} DA seat", da.include?(config.fetch(:da_seat)))
    check("#{paper_id} DA distinct from synthesis seat", config.fetch(:da_seat) != config.fetch(:synthesis_seat))
    pass_in_initial = da.match?(/(?:Final |Checkpoint-2 |DA )?verdict:\s*\*\*`?PASS`?\*\*|FINAL_VERDICT=PASS|^\*\*`?PASS`?\*\*$/i)
    revise_in_initial = da.match?(/(?:Final |Checkpoint-2 |DA )?verdict:\s*\*\*`?REVISE`?\*\*|FINAL_VERDICT=REVISE|^\*\*`?REVISE`?\*\*$/i)
    resolution_relative = "#{notes}/stage1_phase3_resolution.md"
    recheck_relative = "#{notes}/stage1_phase3_devils_advocate_recheck.md"
    if revise_in_initial
      %w[stage1_phase3_claim_intent_manifest.json stage1_phase3_literature_matrix.tsv].each do |basename|
        check("#{paper_id} initial DA binds immutable #{basename} hash", da.include?(digest("#{notes}/#{basename}")))
      end
      reviewed_synthesis_sha256 = da[/\| `(?:notes\/)?stage1_phase3_synthesis\.md` \| `([0-9a-f]{64})` \|/, 1]
      check("#{paper_id} initial DA identifies reviewed synthesis hash", !reviewed_synthesis_sha256.nil?)
      check("#{paper_id} DA revision has resolution", File.file?(path(resolution_relative)))
      check("#{paper_id} DA revision has recheck", File.file?(path(recheck_relative)))
      if File.file?(path(resolution_relative))
        resolution = read(resolution_relative)
        check("#{paper_id} resolution binds initial DA", resolution.include?(digest(da_relative)))
        check("#{paper_id} resolution binds reviewed synthesis", !reviewed_synthesis_sha256.nil? && resolution.include?(reviewed_synthesis_sha256))
      end
      if File.file?(path(recheck_relative))
        recheck = read(recheck_relative)
        check("#{paper_id} DA recheck same independent seat", recheck.include?(config.fetch(:da_seat)))
        check("#{paper_id} DA recheck PASS", recheck.match?(/(?:Final |Checkpoint-2 |Recheck )?verdict:\s*\*\*`?PASS`?\*\*|FINAL_VERDICT=PASS|^\*\*`?PASS`?\*\*$/i))
        check("#{paper_id} DA recheck binds corrected synthesis", recheck.include?(digest(synthesis_relative)))
        check("#{paper_id} DA recheck binds resolution", File.file?(path(resolution_relative)) && recheck.include?(digest(resolution_relative)))
      end
    else
      PHASE3_CORE.each do |basename|
        check("#{paper_id} DA binds #{basename} hash", da.include?(digest("#{notes}/#{basename}")))
      end
      check("#{paper_id} DA initial PASS", pass_in_initial)
    end
  end

  checkpoint_relative = "#{notes}/stage1_phase3_checkpoint.md"
  check("#{paper_id} Phase-3 checkpoint exists", File.file?(path(checkpoint_relative)))
  if File.file?(path(checkpoint_relative))
    checkpoint = read(checkpoint_relative)
    check("#{paper_id} checkpoint disposition", checkpoint.lines.grep(/^CURRENT_DISPOSITION=/) == ["CURRENT_DISPOSITION=PHASE3_SYNTHESIS_READY_WITH_WARNINGS\n"])
    check("#{paper_id} checkpoint DA pass", checkpoint.lines.grep(/^DA_CHECKPOINT_2_FINAL_VERDICT=/) == ["DA_CHECKPOINT_2_FINAL_VERDICT=PASS\n"])
    check("#{paper_id} checkpoint state", checkpoint.lines.grep(/^NEXT_STATE=/) == ["NEXT_STATE=AWAITING_PHASE_4_CONFIRMATION\n"])
    check("#{paper_id} checkpoint computation fence", checkpoint.lines.grep(/^SCIENTIFIC_COMPUTATION=/) == ["SCIENTIFIC_COMPUTATION=NOT_RUN\n"])
    PHASE3_CORE.each do |basename|
      check("#{paper_id} checkpoint binds #{basename}", checkpoint.include?(digest("#{notes}/#{basename}")))
    end
    check("#{paper_id} checkpoint binds DA report", File.file?(path(da_relative)) && checkpoint.include?(digest(da_relative)))
    da_text = File.file?(path(da_relative)) ? read(da_relative) : ""
    if da_text.match?(/(?:Final |Checkpoint-2 |DA )?verdict:\s*\*\*`?REVISE`?\*\*|FINAL_VERDICT=REVISE|^\*\*`?REVISE`?\*\*$/i)
      resolution_relative = "#{notes}/stage1_phase3_resolution.md"
      recheck_relative = "#{notes}/stage1_phase3_devils_advocate_recheck.md"
      check("#{paper_id} checkpoint binds synthesis resolution", File.file?(path(resolution_relative)) && checkpoint.include?(digest(resolution_relative)))
      check("#{paper_id} checkpoint binds DA recheck", File.file?(path(recheck_relative)) && checkpoint.include?(digest(recheck_relative)))
    end
  end

  readme_relative = "#{directory}/README.md"
  state_relative = "#{notes}/pipeline_state.md"
  check("#{paper_id} README Phase-3 complete", File.file?(path(readme_relative)) && read(readme_relative).include?("PHASE_3_COMPLETE"))
  check("#{paper_id} state awaits Phase 4", File.file?(path(state_relative)) && read(state_relative).include?("AWAITING_PHASE_4_CONFIRMATION"))

  %w[code experiments results].each do |subdirectory|
    files = Dir.glob(path("#{directory}/#{subdirectory}/**/*"), File::FNM_DOTMATCH).select { |entry| File.file?(entry) }
    relative_files = files.map { |entry| entry.delete_prefix("#{path(directory)}/") }
    check("#{paper_id} #{subdirectory} has no Phase-3 scientific output", relative_files.all? { |entry| entry.end_with?(".gitkeep") })
  end
end

check("manifest IDs unique across five papers", manifest_ids.compact.uniq.length == PAPERS.length)
check("matrix rows total 116", total_matrix_rows == 116)
check("synthesis citation pairs positive", total_refs.positive?)

SKELETON_HASHES.each do |relative, expected|
  check("skeleton frozen #{relative}", File.file?(path(relative)) && digest(relative) == expected)
end

batch_checkpoint = "BATCH_ROUND10_STAGE1_PHASE3_CHECKPOINT.md"
root_readme = "README.md"
candidate_registry = "docs/candidate_registry.md"
audit_receipt = "BATCH_ROUND10_STAGE1_PHASE3_AUDIT_RECEIPT.json"

check("batch Phase-3 checkpoint exists", File.file?(path(batch_checkpoint)))
check("root README records Phase 3", File.file?(path(root_readme)) && read(root_readme).include?("Round 10 / Stage 1 Phase 3 complete"))
check("candidate registry records Phase 3", File.file?(path(candidate_registry)) && PAPERS.keys.all? { |paper_id| read(candidate_registry).match?(/#{paper_id}.*PHASE_3_COMPLETE/) })
check("Phase-3 audit receipt exists", File.file?(path(audit_receipt)))

if File.file?(path(batch_checkpoint))
  batch = read(batch_checkpoint)
  check("batch current state", batch.lines.grep(/^CURRENT_STATE=/) == ["CURRENT_STATE=PHASE_3_COMPLETE_AWAITING_PHASE_4_CONFIRMATION\n"])
  check("batch dispositions 5/5", batch.lines.grep(/^PHASE3_SYNTHESIS_READY_WITH_WARNINGS=/) == ["PHASE3_SYNTHESIS_READY_WITH_WARNINGS=5\/5\n"])
  check("batch scientific computation not run", batch.lines.grep(/^SCIENTIFIC_COMPUTATION=/) == ["SCIENTIFIC_COMPUTATION=NOT_RUN\n"])
  check("batch formal tuples zero", batch.lines.grep(/^FORMAL_ROUTE_A_TUPLES=/) == ["FORMAL_ROUTE_A_TUPLES=0\/5\n"])
  check("batch Route B zero", batch.lines.grep(/^ROUTE_B_INVOCATIONS=/) == ["ROUTE_B_INVOCATIONS=0\/5\n"])
  PAPERS.each do |paper_id, config|
    checkpoint_relative = "#{config.fetch(:directory)}/notes/stage1_phase3_checkpoint.md"
    check("batch binds #{paper_id} checkpoint", File.file?(path(checkpoint_relative)) && batch.include?(digest(checkpoint_relative)))
  end
end

if File.file?(path(audit_receipt))
  begin
    receipt = JSON.parse(read(audit_receipt))
    check("audit receipt schema", receipt["schema"] == "flow-systems-round10-stage1-phase3-audit-receipt-v1")
    check("audit receipt status", receipt["status"] == "PASS")
    locks = receipt.fetch("locks", {})
    {
      "authorization_sha256" => AUTHORIZATION_SHA256,
      "synthesis_contract_sha256" => CONTRACT_SHA256,
      "start_receipt_sha256" => START_SHA256,
      "audit_script_sha256" => digest("tools/audit_round10_stage1_phase3.rb"),
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
  puts "PASS checks=#{@checks} failures=0 papers=5 matrix_rows=#{total_matrix_rows} citation_pairs=#{total_refs}"
  exit 0
end

warn "FAIL checks=#{@checks} failures=#{@failures.length}"
@failures.each { |failure| warn "- #{failure}" }
exit 1
