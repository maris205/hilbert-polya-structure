#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "json"

ROOT = File.expand_path("..", __dir__)
PAPERS = {
  29 => {dir: "29-bianchi-ideal-owner-refinement", items: 11, ops: 40, resolved: 7, limitations: 4, affected_e1: 38, delta: 651, pages: 14},
  30 => {dir: "30-three-disk-nonconstant-roof-determinant", items: 9, ops: 21, resolved: 7, limitations: 2, affected_e1: 21, delta: 635, pages: 15},
  31 => {dir: "31-level11-conjugacy-owner-ledger", items: 11, ops: 11, resolved: 6, limitations: 5, affected_e1: 8, delta: 440, pages: 13},
  32 => {dir: "32-homology-cover-renormalization-uniformity", items: 12, ops: 12, resolved: 8, limitations: 4, affected_e1: 9, delta: 437, pages: 14},
  33 => {dir: "33-bolza-control-matched-census", items: 13, ops: 13, resolved: 8, limitations: 5, affected_e1: 12, delta: 1400, pages: 17}
}.freeze
AUTH_RECORD_SHA = "44f5b2cc73c424a2c3b07da7308b0cbbcc71a50546c456bd4c1c6e1b2610f22e"
AUTHOR_EVENT_SHA = "37ec1eff9228a996f835a975b59a04f88c2aad3b2f2ab47b6c512d3299ff0c86"
ROUTE_A_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ROUTE_B_SHA = "170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595"

def load_json(path)
  JSON.parse(File.binread(path))
end

def sha256(path)
  Digest::SHA256.file(path).hexdigest
end

def tree_hash(paths)
  rows = paths.select { |path| File.file?(path) }.sort_by { |path| path.delete_prefix(ROOT + "/") }.map do |path|
    "#{sha256(path)}  #{path.delete_prefix(ROOT + '/')}\n"
  end
  Digest::SHA256.hexdigest(rows.join)
end

def marker_free_blocks(path)
  source = File.binread(path).force_encoding("UTF-8")
  blocks = []
  current = nil
  offset = 0
  source.lines.each do |line|
    marker = line.match(/\A<!--block:(B\d{4})-->\s*\z/)
    if marker
      current = {id: marker[1], start: offset, text: +""}
      blocks << current
    else
      raise "content before first block marker" unless current
      current.fetch(:text) << line
      offset += line.bytesize
    end
  end
  blocks.each { |block| block[:finish] = block.fetch(:start) + block.fetch(:text).bytesize }
  blocks
end

failures = []
checks = 0
check = lambda do |condition, message|
  checks += 1
  failures << message unless condition
end

auth_record = File.join(ROOT, "BATCH_ROUND10_STAGE4_AUTHORIZATION_RECORD.md")
author_event = File.join(ROOT, "BATCH_ROUND10_STAGE4_AUTHOR_EVENT_20260903.txt")
check.call(File.file?(auth_record) && sha256(auth_record) == AUTH_RECORD_SHA, "batch authorization record SHA mismatch")
check.call(File.file?(author_event) && sha256(author_event) == AUTHOR_EVENT_SHA, "author event SHA mismatch")
check.call(sha256(File.join(ROOT, "skills/route-a-evaluator.md")) == ROUTE_A_SHA, "Route-A evaluator drift")
check.call(sha256(File.join(ROOT, "skills/route-b-evaluator.md")) == ROUTE_B_SHA, "Route-B evaluator drift")

science_freeze = load_json(File.join(ROOT, "BATCH_ROUND10_STAGE2_INPUT_FREEZE.json"))
science_by_code = science_freeze.fetch("papers").to_h { |row| [row.fetch("paper"), row] }

totals = {items: 0, ops: 0, resolved: 0, limitations: 0, affected_e1: 0, registry_e1: 0, unaffected_exact_once: 0, unaffected_duplicate_valued: 0, delta: 0, pages: 0, blocks: 0, preserved: 0}
receipt_expectations = {}

PAPERS.each do |number, expected|
  code = "P#{number}"
  paper_root = File.join(ROOT, "papers", expected.fetch(:dir))
  notes = File.join(paper_root, "notes")
  baseline_path = File.join(notes, "stage3_review_baseline.json")
  baseline = load_json(baseline_path)
  paths = {
    manuscript: File.join(paper_root, "paper/manuscript.tex"),
    bibliography: File.join(paper_root, "paper/references.bib"),
    canonical_pdf: File.join(paper_root, "paper/paper.pdf"),
    base: File.join(notes, "stage3_revision_base.tex"),
    manifest: File.join(notes, "stage3_revision_base.block-manifest.json"),
    roadmap: File.join(notes, "stage3_revision_roadmap.json"),
    adjudication: File.join(notes, "stage4_author_adjudication.json"),
    claims: File.join(notes, "stage4_claim_surface_manifest.json"),
    patch: File.join(notes, "stage4_revision_patch_round1.json"),
    revised: File.join(notes, "stage4_revision_round1.tex"),
    apply_report: File.join(notes, "stage4_revision_round1.tex.apply-report.json"),
    response: File.join(notes, "stage4_response_to_reviewers_round1.json"),
    bundle: File.join(notes, "stage4_revision_evidence_bundle.json"),
    bundle_receipt: File.join(notes, "stage4_bundle_validation_receipt.json"),
    token: File.join(notes, "stage4_token_conservation_round1.json"),
    replay: File.join(notes, "stage4_registered_claim_surface_replay.json"),
    packet: File.join(notes, "stage4_unregistered_claim_drift_review_packet.json"),
    semantic_audit: File.join(notes, "stage4_unregistered_claim_drift_audit.md"),
    route: File.join(notes, "stage4_route_crosswalk.md"),
    completion: File.join(notes, "stage4_completion_report.md"),
    preview: File.join(notes, "stage4_preview_build_receipt.json"),
    preview_pdf: File.join(notes, "stage4_revision_round1.pdf"),
    archive: File.join(notes, "stage4_attempt1_superseded_20260903/ATTEMPT_MANIFEST.json"),
    registry: File.join(notes, "stage2_5_claim_registry.json")
  }
  paths.each { |key, path| check.call(File.file?(path), "#{code}: missing #{key} at #{path}") }
  next unless paths.values.all? { |path| File.file?(path) }

  check.call(sha256(paths.fetch(:manuscript)) == baseline.dig("manuscript", "sha256"), "#{code}: canonical manuscript drift")
  check.call(sha256(paths.fetch(:bibliography)) == baseline.dig("bibliography", "sha256"), "#{code}: canonical bibliography drift")
  check.call(sha256(paths.fetch(:canonical_pdf)) == baseline.dig("rendered_pdf", "sha256"), "#{code}: canonical PDF drift")
  marker_free_base = File.binread(paths.fetch(:base)).force_encoding("UTF-8").lines.reject { |line| line.match?(/\A<!--block:B\d{4}-->\s*\z/) }.join
  check.call(marker_free_base == File.binread(paths.fetch(:manuscript)).force_encoding("UTF-8"), "#{code}: Stage-3 base no longer strips to canonical manuscript")

  science_paths = %w[code experiments results].flat_map { |dir| Dir.glob(File.join(paper_root, dir, "**/*"), File::FNM_DOTMATCH) }
  check.call(tree_hash(science_paths) == science_by_code.fetch(code).fetch("science_tree_sha256"), "#{code}: frozen code/experiments/results tree drift")

  roadmap = load_json(paths.fetch(:roadmap))
  adjudication = load_json(paths.fetch(:adjudication))
  claims = load_json(paths.fetch(:claims))
  patch = load_json(paths.fetch(:patch))
  report = load_json(paths.fetch(:apply_report))
  response = load_json(paths.fetch(:response))
  replay = load_json(paths.fetch(:replay))
  packet = load_json(paths.fetch(:packet))
  preview = load_json(paths.fetch(:preview))
  archive = load_json(paths.fetch(:archive))
  registry = load_json(paths.fetch(:registry)).fetch("claims")
  base_text = File.binread(paths.fetch(:base)).force_encoding("UTF-8")
  revised_text = File.binread(paths.fetch(:revised)).force_encoding("UTF-8")

  item_ids = roadmap.fetch("items").map { |item| item.fetch("id") }
  display_order = adjudication.dig("display_order", "item_ids")
  check.call(item_ids.length == expected.fetch(:items), "#{code}: roadmap item count")
  check.call(display_order == item_ids, "#{code}: adjudication display order differs from roadmap")
  check.call(adjudication.fetch("author_adjudications").all? { |row| row.fetch("author_triage") == "will_address" }, "#{code}: non-will_address adjudication")
  check.call(patch.fetch("ops").length == expected.fetch(:ops), "#{code}: patch op count")
  check.call(patch.fetch("ops").flat_map { |op| op.fetch("roadmap_item_ids") }.uniq.sort == item_ids.sort, "#{code}: roadmap coverage")
  check.call(patch.fetch("ops").all? { |op| op.fetch("claim_strength_changes") == [] && op.fetch("collateral_authorization_ids") == [] }, "#{code}: unauthorized claim/collateral entry")
  check.call(report.fetch("ops_applied").length == expected.fetch(:ops), "#{code}: applied op count")
  check.call(report.dig("authorization_witness", "status") == "pass", "#{code}: authorization witness")
  check.call(report.dig("structural_flags", "any") == false && report.dig("structural_flags", "acknowledged") == false, "#{code}: structural flag/acknowledgement")
  check.call(report.fetch("patch_digest") == sha256(paths.fetch(:patch)), "#{code}: apply patch binding")
  check.call(report.fetch("output_draft_hash") == sha256(paths.fetch(:revised))[0, 12], "#{code}: apply output binding")

  summary = response.fetch("summary")
  check.call(response.fetch("items").map { |item| item.fetch("roadmap_item_id") } == item_ids, "#{code}: response order")
  check.call(summary.fetch("resolved") == expected.fetch(:resolved), "#{code}: resolved count")
  check.call(summary.fetch("limitations") == expected.fetch(:limitations), "#{code}: limitation count")
  check.call(summary.fetch("unresolvable") == 0 && summary.fetch("disagreed") == 0, "#{code}: unexpected disposition")
  check.call(response.fetch("items").all? { |item| item.fetch("status") == "RESOLVED" || !item.fetch("decline_justification", "").strip.empty? }, "#{code}: limitation without justification")
  check.call(response.fetch("word_count_delta") == expected.fetch(:delta), "#{code}: word-count delta")
  check.call(response.fetch("new_references_added") == 0, "#{code}: bibliography mutation declared")
  check.call(!File.binread(paths.fetch(:response)).match?(/pending deterministic apply|applicator assigns its fresh block ID/i), "#{code}: stale pre-apply response wording")

  check.call(claims.fetch("surfaces") == [], "#{code}: unexpected ClaimIntent surfaces")
  check.call(replay.fetch("registered_surface_count") == 0 && replay.fetch("all_byte_exact_once") == true, "#{code}: ClaimIntent vacuous replay")
  check.call(replay.fetch("vacuous_replay") == true && replay.fetch("clean_claim_certificate") == false, "#{code}: vacuous replay misrepresented")
  check.call(replay.fetch("unregistered_claim_drift_review_required") == true, "#{code}: semantic review flag")
  check.call(packet.dig("coverage", "operation_count") == expected.fetch(:ops), "#{code}: semantic packet op coverage")
  check.call(packet.dig("coverage", "affected_registry_claim_count") == expected.fetch(:affected_e1), "#{code}: semantic packet E1 coverage")
  check.call(packet.dig("coverage", "all_operations_included") == true, "#{code}: semantic packet incomplete-operation flag")
  check.call(packet.dig("bindings", "patch_sha256") == sha256(paths.fetch(:patch)), "#{code}: semantic packet patch binding")
  check.call(packet.dig("bindings", "revised_draft_sha256") == sha256(paths.fetch(:revised)), "#{code}: semantic packet revised binding")

  blocks = marker_free_blocks(paths.fetch(:base))
  revised_blocks = marker_free_blocks(paths.fetch(:revised))
  block_by_id = blocks.to_h { |block| [block.fetch(:id), block] }
  revised_by_id = revised_blocks.to_h { |block| [block.fetch(:id), block] }
  packet_ops = packet.fetch("operations")
  check.call(packet_ops.length == patch.fetch("ops").length, "#{code}: semantic packet operation cardinality")
  patch.fetch("ops").each_with_index do |op, index|
    packet_op = packet_ops[index]
    next unless packet_op
    check.call(packet_op.fetch("op_index") == index, "#{code}: packet op #{index} index")
    check.call(packet_op.fetch("op") == op.fetch("op"), "#{code}: packet op #{index} operation")
    check.call(packet_op.fetch("block_id") == op.fetch("block_id"), "#{code}: packet op #{index} block")
    check.call(packet_op.fetch("roadmap_item_ids") == op.fetch("roadmap_item_ids"), "#{code}: packet op #{index} roadmap IDs")
    check.call(packet_op.fetch("new_text") == op.fetch("new_text"), "#{code}: packet op #{index} new text")
    source_block = block_by_id[op.fetch("block_id")]
    check.call(!source_block.nil? && packet_op.fetch("old_text") == source_block&.fetch(:text), "#{code}: packet op #{index} old text")
    if op.fetch("op") == "replace_block"
      emitted_text = revised_by_id.dig(op.fetch("block_id"), :text)
      check.call(!emitted_text.nil? && emitted_text.rstrip == op.fetch("new_text").rstrip && emitted_text.end_with?("\n\n"), "#{code}: revised op #{index} replacement text")
    end
  end
  replaced = patch.fetch("ops").select { |op| %w[replace_block delete_block].include?(op.fetch("op")) }.map { |op| op.fetch("block_id") }.to_h { |id| [id, true] }
  affected = 0
  affected_claim_ids = []
  unaffected_exact_once = 0
  unaffected_duplicate_valued = 0
  registry.each do |claim|
    span = claim.fetch("draft_span")
    owner = blocks.find { |block| span.fetch("start_byte") >= block.fetch(:start) && span.fetch("end_byte") <= block.fetch(:finish) }
    if owner && replaced[owner.fetch(:id)]
      affected += 1
      affected_claim_ids << claim.fetch("claim_id")
    else
      matcher = Regexp.new(Regexp.escape(claim.fetch("claim_text")))
      base_count = base_text.scan(matcher).length
      revised_count = revised_text.scan(matcher).length
      check.call(base_count.positive? && revised_count == base_count, "#{code}: unaffected #{claim.fetch('claim_id')} occurrence multiplicity #{base_count} -> #{revised_count}")
      if base_count == 1
        unaffected_exact_once += 1
      else
        unaffected_duplicate_valued += 1
      end
    end
  end
  check.call(affected == expected.fetch(:affected_e1), "#{code}: independently mapped affected E1 count")
  packet_claim_rows = packet_ops.flat_map { |row| row.fetch("affected_registered_e1_claims") }
  packet_claim_ids = packet_claim_rows.map { |row| row.fetch("claim_id") }
  check.call(packet_claim_ids.sort == affected_claim_ids.sort, "#{code}: semantic packet affected E1 ID mapping")
  registry_by_id = registry.to_h { |claim| [claim.fetch("claim_id"), claim] }
  packet_claim_rows.each do |row|
    claim = registry_by_id[row.fetch("claim_id")]
    check.call(!claim.nil?, "#{code}: packet unknown affected claim #{row.fetch('claim_id')}")
    next unless claim
    check.call(row.fetch("original_claim_text") == claim.fetch("claim_text"), "#{code}: packet affected #{row.fetch('claim_id')} original text")
    check.call(row.fetch("original_text_sha256") == Digest::SHA256.hexdigest(claim.fetch("claim_text")), "#{code}: packet affected #{row.fetch('claim_id')} text SHA")
    actual_occurrences = revised_text.scan(Regexp.new(Regexp.escape(claim.fetch("claim_text")))).length
    check.call(row.fetch("occurrences_byte_exact_in_revised") == actual_occurrences, "#{code}: packet affected #{row.fetch('claim_id')} revised occurrence count")
  end

  check.call(preview.fetch("status") == "PASS", "#{code}: preview status")
  check.call(preview.fetch("pages") == expected.fetch(:pages), "#{code}: preview pages")
  %w[undefined_citations undefined_references missing_glyphs fatal_errors overfull_hboxes].each do |field|
    check.call(preview.fetch(field) == 0, "#{code}: preview #{field}")
  end
  check.call(preview.fetch("maximum_overfull_pt") == 0.0, "#{code}: preview maximum overfull")
  check.call(preview.fetch("layout_advisory") == "NONE", "#{code}: preview layout advisory")
  check.call(preview.fetch("citation_style") == "plainnat_numeric_current", "#{code}: preview citation style")
  check.call(preview.dig("bindings", "references_bib_sha256") == sha256(paths.fetch(:bibliography)), "#{code}: preview bibliography binding")
  build_log = File.join(notes, "stage4_revision_round1.build.log")
  check.call(File.file?(build_log) && preview.dig("bindings", "final_build_log_sha256") == sha256(build_log), "#{code}: preview final-build-log binding")
  %w[paper_manuscript_modified paper_pdf_modified canonical_results_refreshed stage3_prime_invoked stage4_5_invoked stage5_invoked].each do |field|
    check.call(preview.dig("write_boundary", field) == false, "#{code}: preview write boundary #{field}")
  end
  check.call(preview.dig("bindings", "revision_patch_sha256") == sha256(paths.fetch(:patch)), "#{code}: preview patch binding")
  check.call(preview.dig("bindings", "revised_anchored_draft_sha256") == sha256(paths.fetch(:revised)), "#{code}: preview revised binding")
  check.call(preview.dig("bindings", "revision_evidence_bundle_sha256") == sha256(paths.fetch(:bundle)), "#{code}: preview bundle binding")
  check.call(preview.dig("bindings", "preview_pdf_sha256") == sha256(paths.fetch(:preview_pdf)), "#{code}: preview PDF binding")

  check.call(load_json(paths.fetch(:bundle_receipt)).fetch("status") == "PASS", "#{code}: evidence bundle validation")
  check.call(load_json(paths.fetch(:bundle_receipt)).fetch("bundle_sha256") == sha256(paths.fetch(:bundle)), "#{code}: evidence bundle receipt binding")
  check.call(archive.fetch("status") == "SUPERSEDED_FAIL_CLOSED_NOT_CANONICAL", "#{code}: attempt-1 archive status")
  check.call(archive.dig("boundaries", "canonical_results_refreshed") == false, "#{code}: archive canonical-results boundary")

  semantic_text = File.binread(paths.fetch(:semantic_audit)).force_encoding("UTF-8")
  route_text = File.binread(paths.fetch(:route)).force_encoding("UTF-8")
  completion_text = File.binread(paths.fetch(:completion)).force_encoding("UTF-8")
  check.call(semantic_text.include?("Status: **PASS") && semantic_text.include?("not Stage 4.5"), "#{code}: bounded semantic audit status/scope")
  check.call(route_text.include?("FORMAL_ROUTE_A_TUPLE=UNASSIGNED") && route_text.include?("STAGE4_ROUTE_PROMOTION=NONE") && route_text.include?("ROUTE_B_INVOKED=false"), "#{code}: route crosswalk boundary")
  check.call(completion_text.include?("Stage 3 prime") && completion_text.include?("not"), "#{code}: completion checkpoint boundary")
  [paths.fetch(:patch), paths.fetch(:revised), paths.fetch(:apply_report), paths.fetch(:response), paths.fetch(:bundle), paths.fetch(:packet), paths.fetch(:preview), paths.fetch(:preview_pdf)].each do |bound_path|
    check.call(semantic_text.include?(sha256(bound_path)), "#{code}: semantic audit omits binding #{File.basename(bound_path)}")
    check.call(completion_text.include?(sha256(bound_path)), "#{code}: completion report omits binding #{File.basename(bound_path)}")
  end
  check.call(route_text.include?(ROUTE_A_SHA) && route_text.include?(ROUTE_B_SHA), "#{code}: route evaluator bindings absent")

  totals[:items] += expected.fetch(:items)
  totals[:ops] += expected.fetch(:ops)
  totals[:resolved] += expected.fetch(:resolved)
  totals[:limitations] += expected.fetch(:limitations)
  totals[:affected_e1] += expected.fetch(:affected_e1)
  totals[:registry_e1] += registry.length
  totals[:unaffected_exact_once] += unaffected_exact_once
  totals[:unaffected_duplicate_valued] += unaffected_duplicate_valued
  totals[:delta] += expected.fetch(:delta)
  totals[:pages] += expected.fetch(:pages)
  totals[:blocks] += report.dig("counters", "blocks_total")
  totals[:preserved] += report.dig("counters", "blocks_preserved_byte_identical")
  receipt_expectations[code] = {
    "directory" => "papers/#{expected.fetch(:dir)}",
    "roadmap" => {"items" => expected.fetch(:items), "resolved" => expected.fetch(:resolved), "deliberate_limitations" => expected.fetch(:limitations)},
    "patch" => {
      "operations" => expected.fetch(:ops), "affected_e1" => expected.fetch(:affected_e1),
      "registry_e1" => registry.length,
      "unaffected_e1_baseline_multiplicity_preserved" => registry.length - expected.fetch(:affected_e1),
      "unaffected_e1_exact_once" => unaffected_exact_once,
      "unaffected_e1_duplicate_valued" => unaffected_duplicate_valued
    },
    "word_count" => {"before" => response.fetch("word_count_delta") + (expected.fetch(:delta) == 0 ? 0 : 0), "delta" => response.fetch("word_count_delta")},
    "anchored_blocks" => {"original" => report.dig("counters", "blocks_total"), "preserved_byte_identical" => report.dig("counters", "blocks_preserved_byte_identical")},
    "pages" => expected.fetch(:pages),
    "semantic_audit_sha256" => sha256(paths.fetch(:semantic_audit)),
    "route_crosswalk_sha256" => sha256(paths.fetch(:route)),
    "completion_report_sha256" => sha256(paths.fetch(:completion)),
    "preview_pdf_sha256" => sha256(paths.fetch(:preview_pdf)),
    "artifacts" => {
      "patch" => sha256(paths.fetch(:patch)), "revised" => sha256(paths.fetch(:revised)),
      "apply" => sha256(paths.fetch(:apply_report)), "response" => sha256(paths.fetch(:response)),
      "bundle" => sha256(paths.fetch(:bundle)), "bundle_receipt" => sha256(paths.fetch(:bundle_receipt)),
      "token" => sha256(paths.fetch(:token)), "replay" => sha256(paths.fetch(:replay)),
      "packet" => sha256(paths.fetch(:packet)), "preview" => sha256(paths.fetch(:preview)),
      "preview_pdf" => sha256(paths.fetch(:preview_pdf)), "archive" => sha256(paths.fetch(:archive)),
      "completion_report" => sha256(paths.fetch(:completion))
    }
  }
end

expected_totals = {items: 56, ops: 97, resolved: 36, limitations: 20, affected_e1: 88, registry_e1: 480, unaffected_exact_once: 375, unaffected_duplicate_valued: 17, delta: 3563, pages: 73, blocks: 604, preserved: 513}
check.call(totals == expected_totals, "batch totals #{totals.inspect} != #{expected_totals.inspect}")
check.call(File.file?(File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md")), "missing batch Stage-4 completion report")
check.call(File.file?(File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json")), "missing batch Stage-4 completion receipt")

batch_report_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md")
batch_receipt_path = File.join(ROOT, "BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json")
if File.file?(batch_report_path) && File.file?(batch_receipt_path)
  receipt = load_json(batch_receipt_path)
  check.call(receipt.fetch("schema") == "round10-stage4-completion-receipt/1.0", "batch receipt schema")
  check.call(receipt.fetch("status") == "PASS", "batch receipt status")
  check.call(receipt.fetch("pipeline_state") == "STAGE4_COMPLETE_AWAITING_SCHOLAR_CONFIRMATION_FOR_STAGE3_PRIME", "batch receipt pipeline state")
  check.call(receipt.dig("authorization", "author_event_sha256") == AUTHOR_EVENT_SHA, "batch receipt author-event binding")
  check.call(receipt.dig("authorization", "authorization_record_sha256") == AUTH_RECORD_SHA, "batch receipt authorization binding")
  check.call(receipt.dig("authorization", "roadmap_items_authorized") == 56 && receipt.dig("authorization", "adjudication") == "will_address", "batch receipt authorization scope")
  check.call(receipt.dig("evaluator_bindings", "route_a_sha256") == ROUTE_A_SHA, "batch receipt Route-A binding")
  check.call(receipt.dig("evaluator_bindings", "route_b_sha256") == ROUTE_B_SHA, "batch receipt Route-B binding")
  receipt_totals = receipt.fetch("totals")
  expected_receipt_totals = {
    "papers" => 5, "roadmap_items" => 56, "resolved" => 36,
    "deliberate_limitations" => 20, "operations" => 97,
    "registry_e1" => 480, "affected_e1_semantically_reviewed" => 88,
    "unaffected_e1_baseline_multiplicity_preserved" => 392,
    "unaffected_e1_exact_once" => 375, "unaffected_e1_duplicate_valued" => 17,
    "word_count_before" => 26_638, "word_count_after" => 30_201,
    "word_count_delta" => 3563, "original_anchored_blocks" => 604,
    "preserved_byte_identical_blocks" => 513, "preview_pages" => 73
  }
  check.call(receipt_totals == expected_receipt_totals, "batch receipt totals")
  expected_boundaries = {
    "canonical_manuscripts_changed" => false, "canonical_bibliographies_changed" => false,
    "canonical_pdfs_changed" => false, "science_trees_changed" => false,
    "initial_dynamical_systems_changed" => false, "formal_route_a_tuples_assigned" => 0,
    "positive_arithmetic_a2" => 0, "route_b_invocations" => 0,
    "stage3_prime_started" => false, "stage4_5_started" => false, "stage5_started" => false
  }
  check.call(receipt.fetch("boundaries") == expected_boundaries, "batch receipt boundaries")
  check.call(receipt.dig("batch_report", "path") == "BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md" && receipt.dig("batch_report", "sha256") == sha256(batch_report_path), "batch receipt report binding")
  receipt_rows = receipt.fetch("papers")
  check.call(receipt_rows.length == PAPERS.length, "batch receipt paper cardinality")
  receipt_expectations.each do |code, expected_row|
    row = receipt_rows.find { |candidate| candidate.fetch("paper") == code }
    check.call(!row.nil? && row.fetch("status") == "PASS", "#{code}: batch receipt paper status")
    next unless row
    check.call(row.fetch("directory") == expected_row.fetch("directory"), "#{code}: batch receipt directory")
    check.call(row.fetch("roadmap") == expected_row.fetch("roadmap"), "#{code}: batch receipt roadmap")
    check.call(row.fetch("patch") == expected_row.fetch("patch"), "#{code}: batch receipt patch/E1 counts")
    check.call(row.dig("word_count", "delta") == expected_row.dig("word_count", "delta"), "#{code}: batch receipt word delta")
    check.call(row.fetch("anchored_blocks") == expected_row.fetch("anchored_blocks"), "#{code}: batch receipt block conservation")
    check.call(row.dig("preview", "status") == "PASS" && row.dig("preview", "pages") == expected_row.fetch("pages") && row.dig("preview", "citation_style") == "plainnat numeric" && row.dig("preview", "pdf_sha256") == expected_row.fetch("preview_pdf_sha256"), "#{code}: batch receipt preview")
    check.call(row.dig("semantic_audit", "status") == "PASS" && row.dig("semantic_audit", "clean_claim_certificate") == false && row.dig("semantic_audit", "sha256") == expected_row.fetch("semantic_audit_sha256"), "#{code}: batch receipt semantic audit")
    check.call(row.dig("route", "formal_route_a_tuple") == "UNASSIGNED" && row.dig("route", "positive_arithmetic_a2") == 0 && row.dig("route", "stage4_promotion") == "NONE" && row.dig("route", "route_b_invoked") == false && row.dig("route", "crosswalk_sha256") == expected_row.fetch("route_crosswalk_sha256"), "#{code}: batch receipt route")
    check.call(row.fetch("artifacts") == expected_row.fetch("artifacts"), "#{code}: batch receipt artifact hashes")
  end
end
check.call(Dir.glob(File.join(ROOT, "BATCH_ROUND10_STAGE3_PRIME*")).empty?, "Stage 3 prime batch artifacts already exist")
check.call(Dir.glob(File.join(ROOT, "BATCH_ROUND10_STAGE4_5*")).empty?, "Stage 4.5 batch artifacts already exist")

if failures.empty?
  puts "PASS — Round 10 Stage 4 completion: #{checks} checks; 56/56 items (36 RESOLVED, 20 DELIBERATE_LIMITATION); 97 ops; 88/480 E1 claims changed and bounded-semantically reviewed; all 392 unaffected claims retain baseline multiplicity (375 exact-once, 17 duplicate-valued); 73 clean preview pages; +3,563 words; canonical/science/Route boundaries unchanged"
  exit 0
end

warn "FAIL — Round 10 Stage 4 completion audit (#{failures.length} failures / #{checks} checks)"
failures.each { |failure| warn "  - #{failure}" }
exit 1
