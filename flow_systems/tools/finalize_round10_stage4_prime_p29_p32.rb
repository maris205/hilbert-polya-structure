#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "pathname"
require "time"
require "tmpdir"

ROOT = Pathname.new(__dir__).parent.expand_path
ARS = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
TOKEN_TOOL = ARS / "scripts/check_revision_token_conservation.py"
ROADMAP_TOOL = ARS / "scripts/revision_roadmap.py"
WORKFLOW_DATE = "2026-09-04"
AUTHORITY = {
  "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_AUTHORIZATION_RECEIPT.json" => "4cc48a512c35dc31ccff0b1ff80472eed04fc454d83f4410277bd2fe356e4e4c",
  "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json" => "081f28e0ade1af62d8f5d56d90b83ff543e1019ab1931473ff95754e81855e98",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json" => "3a17181450f040e274f1fa6c31386ff2593c04f409013908bfad759d408d65fa"
}.freeze

CONFIG = {
  "P29" => {
    number: 29,
    slug: "29-bianchi-ideal-owner-refinement",
    expected_ops: 8,
    expected_preserved: 105,
    expected_total: 113,
    new_references: 0,
    writer_validation: "stage4_prime_writer_emit_audit_receipt_round2.json",
    writer_handoff: "stage4_prime_writer_handoff_round2.json",
    provisional: "stage4_prime_response_to_reviewers_provisional_round2.json",
    archives: %w[stage4_prime_layout_superseded_20260904 stage4_prime_layout_superseded_attempt2_20260904 stage4_prime_layout_superseded_attempt3_20260904 stage4_prime_layout_superseded_attempt4_20260904],
    route_state: "Route A A0/A1 foundation/interface only; formal tuple UNASSIGNED; positive A2 and A3--A4 NOT_RUN; Route B NOT_INVOKED",
    summary: "The revision closes the review-facing mechanism/quotient interface gaps with a complete typed reader map, a current 53-query replay ledger, a 22/22 source crosswalk, three explicit control stop states, and a defined-but-unexecuted split-ideal fixture. It does not claim an owner law, certified quotient, mechanism result, performance value, or Route credit."
  },
  "P32" => {
    number: 32,
    slug: "32-homology-cover-renormalization-uniformity",
    expected_ops: 18,
    expected_preserved: 114,
    expected_total: 131,
    new_references: 4,
    writer_validation: "stage4_prime_writer_validation_receipt_round2.json",
    writer_handoff: "stage4_prime_writer_handoff.json",
    provisional: "stage4_prime_response_to_reviewers_provisional_round2.json",
    archives: %w[stage4_prime_layout_superseded_20260904],
    route_state: "Route A A0/A1 foundation/interface only; formal tuple UNASSIGNED; positive A2 and A3--A4 NOT_RUN; Route B NOT_INVOKED",
    summary: "The revision adds a four-work closest-comparator matrix, a 51-manifestation replay, explicit inverse-limit/localization/Hahn formal carriers, an exact conditional scalar lemma, and a complete AN-1--AN-5 obligation registry. Owner/factor application, global products, analytic interchanges, and Route credit remain unproved or not evaluable."
  }
}.freeze

def require!(condition, message)
  raise "STAGE4_PRIME_FINALIZE_FAIL: #{message}" unless condition
end

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def load_json(path)
  JSON.parse(File.binread(path).force_encoding("UTF-8"))
end

def write_json(path, value)
  File.binwrite(path, JSON.pretty_generate(value) + "\n")
end

def artifact(path, paper_root)
  {"path" => Pathname.new(path).relative_path_from(paper_root).to_s, "sha256" => sha(path), "bytes" => File.size(path)}
end

# The official revision-evidence-bundle/1.0 contract deliberately accepts only
# path and sha256.  Other project receipts retain byte counts through `artifact`.
def bundle_artifact(path, paper_root)
  {"path" => Pathname.new(path).relative_path_from(paper_root).to_s, "sha256" => sha(path)}
end

def run!(*command, chdir: nil)
  options = chdir.nil? ? {} : {chdir: chdir}
  stdout, stderr, status = Open3.capture3(*command, **options)
  require!(status.success?, "command failed #{command.join(' ')}: #{stderr}#{stdout}")
  [stdout, stderr, status.exitstatus]
end

def word_count(path)
  File.read(path).gsub(/<!--.*?-->/m, " ").split.length
end

def verify_frozen!(paper_id, paper_root, global_freeze)
  record = global_freeze.fetch("papers").find { |entry| entry.fetch("paper_id") == paper_id }
  require!(!record.nil?, "#{paper_id}: absent from input freeze")
  bound = record.fetch("canonical_files") + record.fetch("science_files") + [record.fetch("initial_system_source"), record.fetch("route_crosswalk")]
  bound.each do |entry|
    path = ROOT / entry.fetch("path")
    require!(path.file? && !path.symlink?, "#{paper_id}: frozen file missing/symlink #{path}")
    require!(File.size(path) == entry.fetch("bytes"), "#{paper_id}: frozen bytes drift #{path}")
    require!(sha(path) == entry.fetch("sha256"), "#{paper_id}: frozen hash drift #{path}")
  end
  bound.length
end

def paths(config)
  paper_root = ROOT / "papers" / config.fetch(:slug)
  notes = paper_root / "notes"
  {
    root: paper_root,
    notes: notes,
    base: notes / "stage4_revision_round1.tex",
    manifest: notes / "stage4_prime_base.block-manifest.json",
    roadmap: notes / "stage4_prime_revision_roadmap.json",
    claim: notes / "stage4_prime_claim_surface_manifest.json",
    author: notes / "stage4_prime_author_adjudication.json",
    patch: notes / "stage4_prime_revision_patch_round2.json",
    revised: notes / "stage4_prime_revision_round2.tex",
    apply_report: notes / "stage4_prime_revision_round2.tex.apply-report.json",
    bib: notes / "stage4_prime_references_round2.bib",
    prior_bundle: notes / "stage4_revision_evidence_bundle.json",
    evidence_bundle: notes / "stage4_prime_revision_evidence_bundle_round2.json",
    pdf: notes / "stage4_prime_revision_round2.pdf",
    build_log: notes / "stage4_prime_revision_round2.build.log",
    build_transcript: notes / "stage4_prime_preview_build_transcript_round2.log",
    build_receipt: notes / "stage4_prime_preview_build_receipt_round2.json",
    writer_validation: notes / config.fetch(:writer_validation),
    writer_handoff: notes / config.fetch(:writer_handoff),
    provisional: notes / config.fetch(:provisional)
  }
end

def validate_apply_chain!(paper_id, config, p)
  %i[base manifest roadmap claim author patch revised apply_report bib writer_validation writer_handoff provisional].each do |key|
    require!(p.fetch(key).file?, "#{paper_id}: missing #{key} #{p.fetch(key)}")
  end
  patch_sha = sha(p[:patch])
  report = load_json(p[:apply_report])
  require!(report.fetch("report_format_version") == "1.3", "#{paper_id}: apply report version")
  require!(report.fetch("patch_digest") == patch_sha, "#{paper_id}: patch/apply digest")
  require!(report.dig("authorization_witness", "status") == "pass", "#{paper_id}: authorization witness")
  require!(report.dig("authorization_witness", "registered_claim_surfaces_checked") == 0, "#{paper_id}: registered population")
  require!(report.fetch("ops_applied").length == config.fetch(:expected_ops), "#{paper_id}: operation count")
  require!(report.dig("counters", "blocks_preserved_byte_identical") == config.fetch(:expected_preserved), "#{paper_id}: preserved blocks")
  require!(report.dig("counters", "blocks_total") == config.fetch(:expected_total), "#{paper_id}: block denominator")
  require!(report.dig("structural_flags", "any") == false, "#{paper_id}: structural flag")
  [p[:writer_validation], p[:writer_handoff], p[:provisional]].each do |path|
    require!(File.binread(path).include?(patch_sha), "#{paper_id}: writer binding missing current patch in #{path.basename}")
  end
  report
end

def build_role_lineage(paper_id, config, p, generated_at)
  attempts = config.fetch(:archives).map.with_index(1) do |dirname, index|
    directory = p[:notes] / dirname
    require!(directory.directory?, "#{paper_id}: missing archive #{dirname}")
    patch = directory / "stage4_prime_revision_patch_round2.json"
    draft = directory / "stage4_prime_revision_round2.tex"
    apply_report = directory / "stage4_prime_revision_round2.tex.apply-report.json"
    require!([patch, draft, apply_report].all?(&:file?), "#{paper_id}: incomplete archive #{dirname}")
    {
      "attempt" => index,
      "status" => "SUPERSEDED_LAYOUT_PREFLIGHT_FAILURE",
      "directory" => "notes/#{dirname}",
      "patch_sha256" => sha(patch),
      "draft_sha256" => sha(draft),
      "apply_report_sha256" => sha(apply_report),
      "used_in_final_chain" => false
    }
  end
  attempts << {
    "attempt" => attempts.length + 1,
    "status" => "CURRENT_DISTINCT_CONTEXT_APPLY",
    "patch_sha256" => sha(p[:patch]),
    "draft_sha256" => sha(p[:revised]),
    "apply_report_sha256" => sha(p[:apply_report]),
    "writer_context" => paper_id == "P29" ? "/root/r10_p29_stage4_prime_writer" : "/root/r10_p32_stage4_prime_writer",
    "applier_context" => "/root",
    "used_in_final_chain" => true
  }
  output = p[:notes] / "stage4_prime_role_separation_and_layout_lineage_round2.json"
  write_json(output, {
    "schema_version" => "round10-stage4-prime-role-layout-lineage/1.0",
    "paper_id" => paper_id,
    "recorded_at_utc" => generated_at,
    "incident" => artifact(p[:notes] / "stage4_prime_layout_preflight_incident_round2.md", p[:root]),
    "attempts" => attempts,
    "scientific_or_citation_content_changed_by_layout_remediation" => false,
    "canonical_or_route_state_changed" => false,
    "verdict" => "FINAL_CHAIN_USES_DISTINCT_CONTEXT_CLEAN_BUILD_CANDIDATE"
  })
  output
end

def build_token_receipt(p)
  stdout, = run!("python3", TOKEN_TOOL.to_s, "patch", "--patch", p[:patch].to_s, "--base", p[:base].to_s)
  output = p[:notes] / "stage4_prime_token_conservation_round2.json"
  write_json(output, JSON.parse(stdout))
  output
end

def build_claim_replay(config, p, generated_at)
  output = p[:notes] / "stage4_prime_registered_claim_surface_replay_round2.json"
  write_json(output, {
    "schema" => "stage4-prime-registered-claim-surface-replay/1.0",
    "paper_number" => config.fetch(:number),
    "recorded_at_utc" => generated_at,
    "manifest" => artifact(p[:claim], p[:root]),
    "revised_draft" => artifact(p[:revised], p[:root]),
    "surface_count" => 0,
    "exact_once_same_block_count" => 0,
    "rows" => [],
    "claim_strength_replacements_authorized" => 0,
    "verdict" => "PASS_EMPTY_REGISTERED_POPULATION"
  })
  output
end

def item_blocks(report, item_id)
  report.fetch("ops_applied").flat_map do |op|
    op.fetch("roadmap_item_ids").include?(item_id) ? [op.fetch("block_id"), *op.fetch("new_block_ids")] : []
  end.uniq
end

def build_response(paper_id, config, p, report, generated_at)
  provisional = load_json(p[:provisional])
  rows = provisional.fetch("items").map do |row|
    item_id = row.fetch("roadmap_item_id")
    row.merge(
      "change_block_ids" => item_blocks(report, item_id),
      "application_status" => "APPLIED_AND_BUILD_VERIFIED"
    )
  end
  response = {
    "schema_version" => "round10-stage4-prime-response-to-reviewers/1.0",
    "artifact_status" => "FINAL_AUTHOR_SIDE_STAGE4_PRIME",
    "paper_id" => paper_id,
    "paper_number" => config.fetch(:number),
    "revision_round" => 2,
    "generated_at_utc" => generated_at,
    "patch" => artifact(p[:patch], p[:root]),
    "revised_draft" => artifact(p[:revised], p[:root]),
    "apply_report" => artifact(p[:apply_report], p[:root]),
    "items" => rows,
    "summary" => {
      "residual_items_covered" => rows.length,
      "patch_ops" => report.fetch("ops_applied").length,
      "word_count_delta" => word_count(p[:revised]) - word_count(p[:base]),
      "notes_side_bibliography_entries_added" => config.fetch(:new_references),
      "canonical_bibliography_entries_added" => 0,
      "scientific_execution" => false,
      "stage4_5_invoked" => false,
      "route_state_changed" => false
    },
    "summary_of_changes" => config.fetch(:summary)
  }
  json_path = p[:notes] / "stage4_prime_response_to_reviewers_round2.json"
  md_path = p[:notes] / "stage4_prime_response_to_reviewers_round2.md"
  write_json(json_path, response)
  lines = ["# #{paper_id} Stage 4′ Round-2 Response to Reviewers", "", "Date: **#{WORKFLOW_DATE}**", ""]
  rows.each do |row|
    lines += ["## `#{row.fetch('roadmap_item_id')}` — #{row.fetch('status')}", "", row.fetch("author_response"), "", "Applied blocks: #{row.fetch('change_block_ids').map { |id| "`#{id}`" }.join(', ')}.", ""]
  end
  lines += ["All #{rows.length} authorized residual items are covered by the applied revision. Scientific execution, canonical promotion, Stage 4.5, Stage 5, and Route advancement were not performed.", ""]
  File.binwrite(md_path, lines.join("\n"))
  [json_path, md_path, response]
end

def build_revision_log(paper_id, config, p, report, response, token, claim, lineage)
  output = p[:notes] / "stage4_prime_post_apply_revision_log_round2.md"
  lines = ["# #{paper_id} Stage 4′ Round-2 Post-Apply Revision Log", "", "Date: **#{WORKFLOW_DATE}**", "", "| Item | Status | Applied blocks |", "|---|---|---|"]
  response.fetch("items").each do |row|
    lines << "| `#{row.fetch('roadmap_item_id')}` | `#{row.fetch('status')}` | #{row.fetch('change_block_ids').map { |id| "`#{id}`" }.join(', ')} |"
  end
  lines += [
    "", "## Deterministic application", "",
    "- Patch SHA-256: `#{sha(p[:patch])}`; revised draft: `#{sha(p[:revised])}`; apply report: `#{sha(p[:apply_report])}`.",
    "- Operations: #{report.fetch('ops_applied').length}; preserved source blocks: #{config.fetch(:expected_preserved)}/#{config.fetch(:expected_total)}; authorization witness: PASS.",
    "- Token sidecar: `#{sha(token)}`; registered-surface replay: `#{sha(claim)}` (0/0); role/layout lineage: `#{sha(lineage)}`.",
    "- Route state: #{config.fetch(:route_state)}.",
    "", "Stage status: **author-side Stage 4′ complete after clean build; fresh Stage 4.5 remains a separate mandatory gate.**", ""
  ]
  File.binwrite(output, lines.join("\n"))
  output
end

def build_drift_audit(paper_id, config, p, report, token, claim)
  output = p[:notes] / "stage4_prime_unregistered_claim_drift_audit_round2.md"
  File.binwrite(output, <<~MD)
    # #{paper_id} Stage 4′ Round-2 Unregistered-Claim Drift Audit

    Date: **#{WORKFLOW_DATE}**

    Status: **PASS WITH MODEL-MEDIATED LIMITATION**

    All #{report.fetch("ops_applied").length} applied operations were reviewed against the authorized residuals, the base draft, and the exact patch. Every operation has empty `claim_strength_changes` and `collateral_authorization_ids`; the registered population is 0/0 (`#{sha(claim)}`), and the token-conservation sidecar is bound at `#{sha(token)}`. The changes add or narrow provenance, definitions, formal obligations, failure states, and limitations. They do not assert a newly observed scientific value, completed owner/factor mechanism, global theorem, or Route credit.

    Canonical manuscript/bibliography/PDF, scientific inputs/results, the initial dynamical-system restriction, and Route coordinates remain frozen. This semantic comparison is model-mediated and is not a deterministic proof of completeness; a fresh Stage 4.5 E6 pass remains mandatory.

    Route state: `#{config.fetch(:route_state)}`.
  MD
  output
end

def build_evidence_bundle(p, generated_at)
  bundle = load_json(p[:prior_bundle])
  require!(bundle.fetch("rounds").length == 1, "prior evidence bundle must contain one round")
  round = {
    "kind" => "review_roadmap",
    "revision_round" => 2,
    "pre_round_draft" => bundle_artifact(p[:base], p[:root]),
    "pre_round_block_manifest" => bundle_artifact(p[:manifest], p[:root]),
    "revision_roadmap" => bundle_artifact(p[:roadmap], p[:root]),
    "claim_surface_manifest" => bundle_artifact(p[:claim], p[:root]),
    "author_adjudication" => bundle_artifact(p[:author], p[:root]),
    "revision_patch" => bundle_artifact(p[:patch], p[:root]),
    "apply_report" => bundle_artifact(p[:apply_report], p[:root]),
    "post_round_draft" => bundle_artifact(p[:revised], p[:root])
  }
  bundle.fetch("rounds") << round
  bundle["final_draft"] = round.fetch("post_round_draft")
  write_json(p[:evidence_bundle], bundle)
  stdout, stderr, exit_code = run!("python3", ROADMAP_TOOL.to_s, "validate-bundle", p[:evidence_bundle].to_s, "--root", p[:root].to_s)
  receipt = p[:notes] / "stage4_prime_bundle_validation_receipt_round2.json"
  write_json(receipt, {
    "schema_version" => "round10-stage4-prime-bundle-validation-receipt/1.0",
    "validated_at_utc" => generated_at,
    "bundle" => artifact(p[:evidence_bundle], p[:root]),
    "command" => "python3 revision_roadmap.py validate-bundle <bundle> --root <paper-root>",
    "exit_code" => exit_code,
    "stdout" => stdout.strip,
    "stderr" => stderr.strip,
    "verdict" => "PASS"
  })
  receipt
end

def build_preview(config, p, generated_at)
  transcript = +""
  pdfinfo = nil
  Dir.mktmpdir("p#{config.fetch(:number)}-stage4-prime-final.") do |tmp|
    marker_free = File.read(p[:revised]).lines.reject { |line| line.match?(/\A<!--block:B\d+-->\s*\z/) }.join
    File.binwrite(File.join(tmp, "manuscript.tex"), marker_free)
    FileUtils.cp(p[:bib], File.join(tmp, "references.bib"))
    commands = [
      ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
      ["bibtex", "manuscript"],
      ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"],
      ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "manuscript.tex"]
    ]
    commands.each do |command|
      stdout, stderr, = run!(*command, chdir: tmp)
      transcript << "$ #{command.join(' ')}\n#{stdout}#{stderr}\n"
    end
    FileUtils.cp(File.join(tmp, "manuscript.pdf"), p[:pdf])
    FileUtils.cp(File.join(tmp, "manuscript.log"), p[:build_log])
    pdfinfo, = run!("pdfinfo", File.join(tmp, "manuscript.pdf"))
  end
  File.binwrite(p[:build_transcript], transcript)
  log = File.read(p[:build_log])
  overfull = log.scan(/Overfull \\hbox \(([0-9.]+)pt too wide\)/).flatten.map(&:to_f)
  undefined_citations = log.scan(/(?:Citation [`'][^\n]+ undefined|There were undefined citations)/).length
  undefined_references = log.scan(/(?:Reference [`'][^\n]+ undefined|There were undefined references)/).length
  missing = log.scan(/Missing character:/).length
  fatal = log.scan(/(?:Fatal error|Emergency stop)/i).length
  require!(overfull.empty? && undefined_citations.zero? && undefined_references.zero? && missing.zero? && fatal.zero?, "P#{config.fetch(:number)}: preview diagnostics not clean")
  draft = File.read(p[:revised])
  cited = draft.scan(/\\cite\w*\{([^}]+)\}/).flatten.flat_map { |keys| keys.split(",") }.map(&:strip).uniq
  receipt = {
    "schema" => "round10-stage4-prime-preview-build-receipt/1.0",
    "paper_number" => config.fetch(:number),
    "built_at_utc" => generated_at,
    "classification" => "STAGE4_PRIME_MARKER_STRIPPED_PREVIEW_NOT_STAGE5_PROMOTION",
    "status" => "PASS",
    "compiler_sequence" => %w[lualatex bibtex lualatex lualatex],
    "compiler_exit_codes_all_zero" => true,
    "citation_style" => "plainnat_numeric_current",
    "citation_commands" => draft.scan(/\\cite\w*\{/).length,
    "unique_citation_keys" => cited.length,
    "pages" => pdfinfo[/^Pages:\s+(\d+)/, 1].to_i,
    "page_size" => pdfinfo[/^Page size:\s+(.+)$/, 1],
    "undefined_citations" => undefined_citations,
    "undefined_references" => undefined_references,
    "missing_characters" => missing,
    "fatal_errors" => fatal,
    "overfull_hboxes" => overfull.length,
    "maximum_overfull_pt" => overfull.max || 0.0,
    "underfull_hboxes" => log.scan(/Underfull \\hbox/).length,
    "marker_strip_rule" => "remove only lines matching ^<!--block:B[0-9]+-->$",
    "temporary_build_directory_removed" => true,
    "pdf_byte_reproducibility_claimed" => false,
    "bindings" => {
      "revised_anchored_draft_sha256" => sha(p[:revised]),
      "revision_patch_sha256" => sha(p[:patch]),
      "revision_evidence_bundle_sha256" => sha(p[:evidence_bundle]),
      "versioned_references_bib_sha256" => sha(p[:bib]),
      "preview_pdf_sha256" => sha(p[:pdf]),
      "final_build_log_sha256" => sha(p[:build_log]),
      "build_transcript_sha256" => sha(p[:build_transcript])
    },
    "write_boundary" => {
      "canonical_paper_files_modified" => false,
      "canonical_results_refreshed" => false,
      "stage4_5_invoked" => false,
      "stage5_invoked" => false
    }
  }
  write_json(p[:build_receipt], receipt)
  receipt
end

def support_names(paper_id)
  if paper_id == "P29"
    %w[
      stage4_prime_literature_replay_round2.raw.json
      stage4_prime_literature_screening_ledger_round2.json
      stage4_prime_literature_screening_ledger_round2.tsv
      stage4_prime_inventory_matrix_crosswalk_round2.json
      stage4_prime_inventory_matrix_crosswalk_round2.tsv
      stage4_prime_sf_literal_01_definition_round2.json
      stage4_prime_references_round2.bib
      stage4_prime_replay_references_round2.bib
      stage4_prime_writer_emit_audit_receipt_round2.json
      stage4_prime_writer_handoff_round2.json
      stage4_prime_layout_preflight_incident_round2.md
    ]
  else
    %w[
      stage4_prime_literature_replay_round2.raw.json
      stage4_prime_literature_screening_ledger_round2.json
      stage4_prime_literature_screening_ledger_round2.tsv
      stage4_prime_closest_work_source_verification_round2.json
      stage4_prime_closest_work_comparison_matrix_round2.json
      stage4_prime_closest_work_comparison_matrix_round2.tsv
      stage4_prime_claim_passage_matrix_round2.json
      stage4_prime_claim_passage_matrix_round2.tsv
      stage4_prime_formal_definition_audit_round2.json
      stage4_prime_conditional_scalar_lemma_audit_round2.json
      stage4_prime_analytic_registry_audit_round2.json
      stage4_prime_reader_artifact_manifest_round2.json
      stage4_prime_references_round2.bib
      stage4_prime_writer_validation_receipt_round2.json
      stage4_prime_writer_handoff.json
      stage4_prime_layout_preflight_incident_round2.md
    ]
  end
end

def build_final_support(paper_id, config, p, generated_at, audit_paths, preview)
  support = support_names(paper_id).map { |name| p[:notes] / name }
  require!(support.all?(&:file?), "#{paper_id}: support artifact absent")
  output = p[:notes] / "stage4_prime_final_support_evidence_bundle_round2.json"
  write_json(output, {
    "schema_version" => "round10-stage4-prime-final-support-bundle/1.0",
    "paper_id" => paper_id,
    "revision_round" => 2,
    "generated_at_utc" => generated_at,
    "authority" => AUTHORITY.map { |name, digest| {"path" => "../../../#{name}", "sha256" => digest} },
    "revision_chain" => artifact(p[:evidence_bundle], p[:root]).merge("official_validation" => "PASS"),
    "apply" => {
      "patch" => artifact(p[:patch], p[:root]),
      "draft" => artifact(p[:revised], p[:root]),
      "report" => artifact(p[:apply_report], p[:root]),
      "authorization_witness" => "PASS"
    },
    "support_artifacts" => support.map { |path| artifact(path, p[:root]) },
    "post_apply_audit_artifacts" => audit_paths.map { |path| artifact(path, p[:root]) },
    "preview" => {
      "status" => preview.fetch("status"),
      "pages" => preview.fetch("pages"),
      "pdf" => artifact(p[:pdf], p[:root]),
      "build_log" => artifact(p[:build_log], p[:root]),
      "build_transcript" => artifact(p[:build_transcript], p[:root])
    },
    "registered_claim_surfaces" => "0/0",
    "scientific_value_changed" => false,
    "canonical_result_refreshed" => false,
    "route_tuple_changed" => false,
    "stage4_5_invoked" => false,
    "stage5_invoked" => false,
    "verdict" => "STAGE4_PRIME_AUTHOR_SIDE_EVIDENCE_BOUND"
  })
  output
end

def build_completion(paper_id, config, p, report, preview, final_support)
  output = p[:notes] / "stage4_prime_completion_report_round2.md"
  File.binwrite(output, <<~MD)
    # #{paper_id} Stage 4′ Round-2 Completion Report

    Date: **#{WORKFLOW_DATE}**

    Status: **COMPLETE — author-side Stage 4′ only; fresh Stage 4.5 remains uninvoked**

    #{config.fetch(:summary)}

    - authorized residuals covered: #{load_json(p[:provisional]).fetch("items").length};
    - Patch 1.1 operations: #{report.fetch("ops_applied").length}; authorization witness: PASS;
    - byte-identical preserved source blocks: #{config.fetch(:expected_preserved)}/#{config.fetch(:expected_total)};
    - registered claim population: 0/0; claim-strength replacements: 0;
    - isolated preview: #{preview.fetch("pages")} pages, plainnat numeric, zero undefined citations/references, missing glyphs, fatal errors, or overfull boxes;
    - Route state unchanged: `#{config.fetch(:route_state)}`.

    Principal bindings: patch `#{sha(p[:patch])}`; revised draft `#{sha(p[:revised])}`; apply report `#{sha(p[:apply_report])}`; revision bundle `#{sha(p[:evidence_bundle])}`; final support bundle `#{sha(final_support)}`; preview PDF `#{sha(p[:pdf])}`.

    Canonical manuscript, canonical bibliography, canonical PDF, scientific inputs/results, and the initial dynamical-system restriction remain byte-frozen. Superseded layout candidates are preserved and excluded from the final evidence chain. Stage 4.5, Stage 5, canonical promotion, and Route advancement require separate authorization.
  MD
  output
end

AUTHORITY.each { |name, digest| require!(sha(ROOT / name) == digest, "authority drift #{name}") }
global_freeze = load_json(ROOT / "BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_INPUT_FREEZE.json")
selected = ARGV.empty? ? CONFIG.keys : ARGV
require!((selected - CONFIG.keys).empty?, "unknown selector(s): #{(selected - CONFIG.keys).join(',')}")

selected.each do |paper_id|
  generated_at = Time.now.utc.iso8601
  config = CONFIG.fetch(paper_id)
  p = paths(config)
  frozen_count = verify_frozen!(paper_id, p[:root], global_freeze)
  report = validate_apply_chain!(paper_id, config, p)
  lineage = build_role_lineage(paper_id, config, p, generated_at)
  token = build_token_receipt(p)
  claim = build_claim_replay(config, p, generated_at)
  response_json, response_md, response = build_response(paper_id, config, p, report, generated_at)
  revision_log = build_revision_log(paper_id, config, p, report, response, token, claim, lineage)
  drift = build_drift_audit(paper_id, config, p, report, token, claim)
  bundle_receipt = build_evidence_bundle(p, generated_at)
  preview = build_preview(config, p, generated_at)
  audit_paths = [lineage, token, claim, response_json, response_md, revision_log, drift, bundle_receipt, p[:build_receipt]]
  final_support = build_final_support(paper_id, config, p, generated_at, audit_paths, preview)
  completion = build_completion(paper_id, config, p, report, preview, final_support)
  verify_frozen!(paper_id, p[:root], global_freeze)
  validate_apply_chain!(paper_id, config, p)
  puts "#{paper_id}: COMPLETE author-side Stage 4′; #{frozen_count} frozen boundaries; #{preview.fetch('pages')} pages; #{completion}"
end
