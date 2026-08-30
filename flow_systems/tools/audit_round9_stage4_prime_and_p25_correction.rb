#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)

REQUEST_SHA = "d2e94cd10b1ca12204c8747b5bc0895f6c642e3a3ff7c08194016ed62fd461ec"
EVENT_SHA = "fc4de4ab870bcb6ff3f1c0c9fc6eb9f389edbfbb2d6b01a79a063d21f80365dd"
ROUTE_A_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE_B_SHA = "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"

PAPERS = {
  24 => {
    dir: "24-bianchi-holonomy-flow",
    draft: "stage4_prime_revision_round2.tex",
    patch: "stage4_prime_revision_patch_round2.json",
    bundle: "stage4_revision_evidence_bundle.json",
    preview: "stage4_prime_preview_build_receipt_round2.json",
    support_bundle: "stage4_prime_support_evidence_bundle_round2.json",
    completion: "stage4_prime_completion_report_round2.md",
    pages: 15,
    base_sha: "b098630fdf8db94b6ae892e86eabafe1832b45ff72122ea722100d3541e46d16",
    roadmap_sha: "bd30b424da60ee104346e54dce5117efff754d062a0f4f4f771ea94a29becf0e",
    surfaces: 10,
    ops: [%w[REV-001 B0015], %w[REV-001 B0032], %w[REV-001 B0034], %w[REV-001 B0104],
          %w[REV-003 B0056], %w[REV-003 B0065], %w[REV-003 B0067], %w[REV-003 B0068],
          %w[REV-003 B0075], %w[REV-003 B0084]],
    canonical_manuscript: "e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11",
    canonical_pdf: "e8dcfa74b967054a956521daa138a4cb397292c13674c19e1c03e218438759f1"
  },
  26 => {
    dir: "26-level11-newform-time-change",
    draft: "stage4_prime_revision_round2.tex",
    patch: "stage4_prime_revision_patch_round2.json",
    bundle: "stage4_revision_evidence_bundle.json",
    preview: "stage4_prime_preview_build_receipt_round2.json",
    support_bundle: "stage4_prime_support_evidence_bundle_round2.json",
    completion: "stage4_prime_completion_report_round2.md",
    pages: 16,
    base_sha: "dea8f3af92bde625008f2987922b3b69d2856abe3b796fdd2af319bf6db3bf37",
    roadmap_sha: "65590089ab2eca9b227047620a484c2fbc70a56c8b9b50d8c00aea404f236f1f",
    surfaces: 17,
    ops: [%w[REV-02 B0029], %w[REV-02 B0030], %w[REV-02 B0031], %w[REV-02 B0092],
          %w[REV-04 B0080], %w[REV-04 B0081], %w[REV-04 B0082], %w[REV-04 B0083],
          %w[REV-04 B0093]],
    canonical_manuscript: "00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe",
    canonical_pdf: "b2911495fff88a1e351c4b7cc65989f998df47822b3a2bae0db60b543c34d5aa"
  },
  27 => {
    dir: "27-congruence-inverse-limit-no-go",
    draft: "stage4_prime_revision_round1.tex",
    patch: "stage4_prime_revision_patch_round1.json",
    bundle: "stage4_prime_revision_evidence_bundle.json",
    preview: "stage4_prime_preview_build_receipt.json",
    support_bundle: "stage4_prime_evidence_bundle.json",
    completion: "stage4_prime_completion_report.md",
    pages: 13,
    base_sha: "b445b5c8350439e97f6be415c2ea99c948114cb241c3ccb084e5f8263e61be8f",
    roadmap_sha: "a31b0557a42bcc31c20864ef0cdc7318661e0d02cbe525ae9bf3816506328451",
    surfaces: 10,
    ops: [%w[REV-03 B0040], %w[REV-03 B0041], %w[REV-03 B0042]],
    canonical_manuscript: "c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9",
    canonical_pdf: "540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a"
  },
  28 => {
    dir: "28-bolza-magnetic-flow",
    draft: "stage4_prime_revision_round1.tex",
    patch: "stage4_prime_revision_patch_round1.json",
    bundle: "stage4_prime_revision_evidence_bundle.json",
    preview: "stage4_prime_preview_build_receipt.json",
    support_bundle: "stage4_prime_evidence_bundle.json",
    completion: "stage4_prime_completion_report.md",
    pages: 14,
    base_sha: "884ca28dacf24cabe6f5473c67cb55bdfd1491e87eb6bd763aab7646cfce1bb2",
    roadmap_sha: "59378ac5cdf61a547fa543cb97f665da49b2769109b523ad71117e2cc0e98fd7",
    surfaces: 14,
    ops: [%w[REV-02 B0048]],
    canonical_manuscript: "864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7",
    canonical_pdf: "f78ddd1f8676b24c4937ab94c4ad491b52892fd563c5a27facc77d523ff0c192"
  }
}.freeze

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.read(path, encoding: "UTF-8"))
end

failures = []
check = ->(condition, message) { failures << message unless condition }

check.call(sha256(File.join(ROOT, "BATCH_ROUND9_STAGE4_PRIME_AUTHORIZATION_REQUEST.md")) == REQUEST_SHA,
           "batch authorization request SHA")
check.call(sha256(File.join(ROOT, "BATCH_ROUND9_STAGE4_PRIME_AND_P25_AUTHOR_EVENT_20260830.txt")) == EVENT_SHA,
           "unified author-event SHA")
check.call(sha256(File.join(ROOT, "skills/route-a-evaluator.md")) == ROUTE_A_SHA, "Route-A evaluator SHA")
check.call(sha256(File.join(ROOT, "skills/route-b-evaluator.md")) == ROUTE_B_SHA, "Route-B evaluator SHA")

total_ops = 0
total_surfaces = 0

PAPERS.each do |number, expected|
  paper = File.join(ROOT, "papers", expected.fetch(:dir))
  notes = File.join(paper, "notes")
  prefix = "P#{number}"

  base = File.join(notes, "stage4_revision_round1.tex")
  roadmap_path = File.join(notes, "stage4_prime_revision_roadmap.json")
  surface_path = File.join(notes, "stage4_prime_claim_surface_manifest.json")
  choices_path = File.join(notes, "stage4_prime_author_choices.json")
  adjudication_path = File.join(notes, "stage4_prime_author_adjudication.json")
  patch_path = File.join(notes, expected.fetch(:patch))
  draft_path = File.join(notes, expected.fetch(:draft))
  report_path = "#{draft_path}.apply-report.json"
  bundle_path = File.join(notes, expected.fetch(:bundle))
  preview_path = File.join(notes, expected.fetch(:preview))
  support_bundle_path = File.join(notes, expected.fetch(:support_bundle))
  completion_path = File.join(notes, expected.fetch(:completion))

  [base, roadmap_path, surface_path, choices_path, adjudication_path, patch_path, draft_path, report_path,
   bundle_path, preview_path, support_bundle_path, completion_path].each do |path|
    check.call(File.file?(path), "#{prefix}: missing #{path.delete_prefix("#{paper}/")}")
  end
  next unless [base, roadmap_path, surface_path, choices_path, adjudication_path, patch_path, draft_path, report_path,
               bundle_path, preview_path, support_bundle_path, completion_path].all? { |path| File.file?(path) }

  check.call(sha256(base) == expected.fetch(:base_sha), "#{prefix}: base draft drift")
  check.call(sha256(roadmap_path) == expected.fetch(:roadmap_sha), "#{prefix}: roadmap drift")

  choices = load_json(choices_path)
  adjudication = load_json(adjudication_path)
  patch = load_json(patch_path)
  report = load_json(report_path)
  surfaces = load_json(surface_path).fetch("surfaces")
  revised = File.binread(draft_path)

  [choices, adjudication].each do |artifact|
    events = artifact.fetch("author_events")
    check.call(events.length == 1 && events.first.fetch("input_sha256") == EVENT_SHA,
               "#{prefix}: author-event binding")
    check.call(artifact.fetch("collateral_authorizations") == [], "#{prefix}: collateral authority")
    check.call(artifact.fetch("author_adjudications").all? do |row|
      row.fetch("author_triage") == "will_address" && row.fetch("claim_strength_authorizations") == []
    end, "#{prefix}: author triage or claim-strength authority")
  end

  check.call(adjudication.fetch("adjudication_status") == "complete", "#{prefix}: adjudication status")
  check.call(adjudication.fetch("roadmap_sha256") == expected.fetch(:roadmap_sha), "#{prefix}: adjudication roadmap binding")
  check.call(patch.fetch("patch_format_version") == "1.1", "#{prefix}: patch format")
  check.call(patch.fetch("authorization_context") == "review_roadmap", "#{prefix}: patch authority context")

  actual_ops = patch.fetch("ops").map do |op|
    [op.fetch("roadmap_item_ids").fetch(0), op.fetch("block_id")]
  end
  check.call(actual_ops == expected.fetch(:ops), "#{prefix}: exact target/order set")
  check.call(patch.fetch("ops").all? do |op|
    op.fetch("op") == "replace_block" && op.fetch("roadmap_item_ids").length == 1 &&
      op.fetch("claim_strength_changes") == [] && op.fetch("collateral_authorization_ids") == []
  end, "#{prefix}: operation boundary")

  check.call(report.dig("authorization_witness", "status") == "pass", "#{prefix}: apply authority witness")
  check.call(report.fetch("ops_applied").length == expected.fetch(:ops).length, "#{prefix}: applied op count")
  check.call(report.dig("structural_flags", "any") == false, "#{prefix}: structural flag")
  check.call(report.dig("structural_flags", "acknowledged") == false, "#{prefix}: structural acknowledgement")
  check.call(report.fetch("base_draft_hash") == expected.fetch(:base_sha)[0, 12], "#{prefix}: apply base binding")
  check.call(report.fetch("output_draft_hash") == sha256(draft_path)[0, 12], "#{prefix}: apply output binding")
  check.call(report.fetch("patch_digest") == sha256(patch_path), "#{prefix}: apply patch binding")

  check.call(surfaces.length == expected.fetch(:surfaces), "#{prefix}: registered surface count")
  surfaces.each do |surface|
    text = surface.fetch("original_text").b
    check.call(revised.scan(Regexp.new(Regexp.escape(text))).length == 1,
               "#{prefix}: #{surface.fetch("surface_id")} not byte-exact-once")
  end

  bundle = load_json(bundle_path)
  check.call(bundle.fetch("rounds").length == 2, "#{prefix}: evidence bundle round count")
  check.call(bundle.fetch("final_draft").fetch("path") == "notes/#{expected.fetch(:draft)}",
             "#{prefix}: evidence bundle final path")
  check.call(bundle.fetch("final_draft").fetch("sha256") == sha256(draft_path),
             "#{prefix}: evidence bundle final hash")
  first, second = bundle.fetch("rounds")
  check.call(first.fetch("post_round_draft").fetch("sha256") == second.fetch("pre_round_draft").fetch("sha256"),
             "#{prefix}: evidence bundle draft continuity")

  preview = load_json(preview_path)
  check.call(preview.fetch("status") == "PASS", "#{prefix}: preview status")
  check.call(preview.fetch("pages") == expected.fetch(:pages), "#{prefix}: preview page count")
  %w[undefined_citations undefined_references fatal_errors overfull_hboxes].each do |field|
    check.call(preview.fetch(field) == 0, "#{prefix}: preview #{field}")
  end
  glyph_field = preview.key?("missing_glyphs") ? "missing_glyphs" : "missing_characters"
  check.call(preview.fetch(glyph_field) == 0, "#{prefix}: preview #{glyph_field}")
  bindings = preview.fetch("bindings")
  check.call(bindings.fetch("revised_anchored_draft_sha256") == sha256(draft_path), "#{prefix}: preview draft binding")
  check.call(bindings.fetch("revision_patch_sha256") == sha256(patch_path), "#{prefix}: preview patch binding")
  check.call(bindings.fetch("revision_evidence_bundle_sha256") == sha256(bundle_path), "#{prefix}: preview bundle binding")
  pdf_path = draft_path.sub(/\.tex\z/, ".pdf")
  log_path = draft_path.sub(/\.tex\z/, ".build.log")
  check.call(bindings.fetch("preview_pdf_sha256") == sha256(pdf_path), "#{prefix}: preview PDF binding")
  # Raw compiler logs are intentionally covered by the repository-wide
  # **/*.log ignore rule. Verify their receipt binding when a local build log
  # is present, while keeping a fresh clone auditable without ignored files.
  if File.file?(log_path)
    check.call(bindings.fetch("final_build_log_sha256") == sha256(log_path), "#{prefix}: preview log binding")
  end
  boundaries = preview.fetch("write_boundary")
  check.call(boundaries.fetch("paper_manuscript_modified") == false, "#{prefix}: canonical manuscript boundary")
  pdf_boundary = boundaries.key?("paper_pdf_modified") ? "paper_pdf_modified" : "canonical_paper_pdf_modified"
  check.call(boundaries.fetch(pdf_boundary) == false, "#{prefix}: canonical PDF boundary")
  check.call(boundaries.fetch("canonical_results_refreshed") == false, "#{prefix}: canonical result boundary")
  check.call(boundaries.fetch("stage4_5_invoked") == false, "#{prefix}: Stage 4.5 boundary")
  check.call(boundaries.fetch("stage5_invoked") == false, "#{prefix}: Stage 5 boundary")

  support_bundle = load_json(support_bundle_path)
  check.call(support_bundle.dig("authority", "request_sha256") == REQUEST_SHA ||
             support_bundle.dig("authorization", "request_sha256") == REQUEST_SHA,
             "#{prefix}: support-package request binding")
  check.call(support_bundle.dig("authority", "author_event_sha256") == EVENT_SHA ||
             support_bundle.dig("authorization", "author_event_sha256") == EVENT_SHA,
             "#{prefix}: support-package author-event binding")

  check.call(sha256(File.join(paper, "paper/manuscript.tex")) == expected.fetch(:canonical_manuscript),
             "#{prefix}: canonical manuscript drift")
  check.call(sha256(File.join(paper, "paper/paper.pdf")) == expected.fetch(:canonical_pdf),
             "#{prefix}: canonical PDF drift")

  total_ops += patch.fetch("ops").length
  total_surfaces += surfaces.length
end

check.call(total_ops == 23, "Stage 4-prime op total #{total_ops}")
check.call(total_surfaces == 51, "Stage 4-prime surface total #{total_surfaces}")

# P26 bibliography is the sole authorized canonical bibliography write in Stage 4-prime.
p26_bib = File.join(ROOT, "papers/26-level11-newform-time-change/paper/references.bib")
p26_audit = File.join(ROOT, "papers/26-level11-newform-time-change/notes/stage4_prime_bibliography_append_audit.json")
if File.file?(p26_bib) && File.file?(p26_audit)
  audit = load_json(p26_audit)
  check.call(audit.fetch("pre_append_sha256") == "9b061c02006f07f1c93df68d8577d44906122f55db71e6f529f43cf3f6483ed8",
             "P26: bibliography preimage")
  check.call(audit.fetch("post_append_sha256") == sha256(p26_bib), "P26: bibliography postimage")
  check.call(audit.fetch("verdict") == "PASS_EXACT_APPEND_ONLY", "P26: bibliography append verdict")
  check.call(audit.fetch("field_by_field_exact_match") == true && audit.fetch("existing_entry_modified") == false &&
             audit.fetch("unauthorized_entry_added") == false, "P26: bibliography append boundary")
  check.call(audit.dig("authorized_entries", "Katok1985", "number") == "3", "P26: Katok issue number")
else
  failures << "P26: bibliography or append audit missing"
end

# P25 repair is a derived-bibliography correction only; it is not a fresh Stage 4.5 verdict or promotion.
p25 = File.join(ROOT, "papers/25-three-disk-scattering-flow")
p25_notes = File.join(p25, "notes")
p25_expected = {
  "stage4_5_integrity_patch_round1.json" => "c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc",
  "stage4_5_integrity_authorization_input_round1.json" => "50324cbe040a0b6e96a0ee96ed790910159c9811b6159f74d46b796463648abf",
  "stage4_5_integrity_authorization_round1.json" => "7c9fad9e525e8a352ee95007bfbd02b8497d905b698f8eb40598d66ef82fc966",
  "stage4_5_references_corrected_round1.bib" => "a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab",
  "stage4_5_references_corrected_round1.bib.apply-report.json" => "d7f6eea3c77837ac902258f079ee54e7fbf182c4cbe0a0f25a274ced51b6be9b",
  "stage4_5_references_working.bib" => "24381ded0d5d9d91fc4a3ad5250e3ccd8039c96a5f9131a8a987eb56d85bb8d6",
  "stage4_5_evidence_rows.json" => "752504e737d4162dff1e189c878f4c1492054207cbd36752dfc6ff86cacce146",
  "stage4_revision_round1.tex" => "39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835"
}.freeze
p25_expected.each do |name, expected_sha|
  path = File.join(p25_notes, name)
  check.call(File.file?(path), "P25: missing #{name}")
  check.call(sha256(path) == expected_sha, "P25: #{name} SHA") if File.file?(path)
end
check.call(sha256(File.join(p25, "paper/manuscript.tex")) == "283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb",
           "P25: canonical manuscript drift")
check.call(sha256(File.join(p25, "paper/references.bib")) == "de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b",
           "P25: canonical bibliography drift")

if failures.empty?
  puts "PASS — P25 exact four-item derived-bibliography repair; P24/P26/P27/P28 Stage 4-prime 6 items, 23 ops, 51/51 registered surfaces; canonical manuscripts/PDFs/results and Route evaluators preserved"
  exit 0
end

warn "FAIL — Round 9 Stage 4-prime / P25 correction audit"
failures.each { |failure| warn "  - #{failure}" }
exit 1
