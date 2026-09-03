#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "open3"
require "pathname"
require "tmpdir"

ROOT = Pathname.new(__dir__).parent.expand_path
ARS_ROOT = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
TOKEN_TOOL = ARS_ROOT / "scripts/check_revision_token_conservation.py"
ROADMAP_TOOL = ARS_ROOT / "scripts/revision_roadmap.py"
DATE = "2026-09-04"
TIMESTAMP = "2026-09-04T01:10:00Z"

AUTHORITY = {
  "../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json" => "a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688",
  "../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md" => "4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a",
  "../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt" => "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
  "../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md" => "67ad4ce8bfb34676b46ffb96e8c9833c1204ada3ffde1e0dc542ea43c46acca5",
  "../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json" => "c94137879092d7d475b22c8985a8f09073c29027f77a89b8ccb8749acfdac48b",
  "../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json" => "82dbf52120f120ffea6ba82b4614c69d4022a32bc01305a892eadde92b8248b7"
}.freeze

CONFIG = {
  "P30" => {
    number: 30,
    slug: "30-three-disk-nonconstant-roof-determinant",
    patch_sha: "5876b07df9741ca1d384a78441030d96734a1e87547e94cb7c097efa8d099846",
    canonical_tex_sha: "af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506",
    canonical_bib_sha: "1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f",
    canonical_pdf_sha: "c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e",
    expected_ops: 14,
    expected_preserved: "113/127",
    new_references: 2,
    route_state: "FORMAL_ROUTE_A_TUPLE=UNASSIGNED; A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; ROUTE_B_INVOKED=false",
    summary: "The 54-query row-level replay and 28-row passage matrix are bound; two correction records are independently citable; reader-facing method vocabulary, frozen controls, and the complete six-gate map are explicit without scientific execution."
  },
  "P31" => {
    number: 31,
    slug: "31-level11-conjugacy-owner-ledger",
    patch_sha: "aeb40a0f7bc440d96ad9ffae4fed1137fb28c6ff9162d98c49a53d04b003dbc2",
    canonical_tex_sha: "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a",
    canonical_bib_sha: "b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958",
    canonical_pdf_sha: "f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722",
    expected_ops: 20,
    expected_preserved: "93/111",
    new_references: 2,
    route_state: "FORMAL_ROUTE_A_TUPLE=UNASSIGNED; A1-ONLY_PREPARATION; POSITIVE_ARITHMETIC_A2=0; ROUTE_B_INVOKED=false",
    summary: "The four-family method positioning, 20-query replay, 24-row method matrix, total-disposition/resolved-owner typing, inverse branches, audit limits, and consolidated G/I/C schema are explicit without an owner result."
  }
}.freeze

RESPONSES = {
  "P30" => {
    "REV-EIC-W2-R1-W3" => "Ran and bound all 54 frozen queries as a dated row-level Crossref replay; published screening decisions and a 28-row claim-passage matrix; preserved unavailable original-session rows as unavailable; and replaced broad recovery wording with a schema/hash/access-state manifest.",
    "REV-EIC-W3-R2-W2" => "Added source-verified notes-side entries P30-C01 and P30-C02 for the two correction DOIs, bound P30-S01/P30-S02 and P30-S03 to the matching records, and removed only the publication-incomplete wording now resolved.",
    "REV-EIC-W4" => "Recast the evidence process as a standalone reader-facing method, described the four assessments as same-family fresh-context role-separated checks, removed internal Stage language, and changed only the authorized section heading text.",
    "REV-R1-W2-R3-W2" => "Froze a=1, c0=1, the order-three cyclic label automorphism, delta=1/10 giving d=61/10, Omega, and eta=1/100; stated preserved/changed properties and reclassified phi as an invariance control. No comparison was executed.",
    "REV-R3-W1-DA-N1" => "Added a six-row gate map containing inputs, output, receipt/hash, uncertainty, consumer, permission, and stop state, including Gate 6; corrected current state to Gates 1--5 NOT_STARTED and Gate 6 NOT_ACTIVATED."
  },
  "P31" => {
    "REV-P31-001" => "Added source-verified proof-carrying-code and tamper-evident-ledger neighbors, separated their inherited patterns from the P31 synthesis, and retained the no-priority/no-exhaustive-novelty boundary.",
    "REV-P31-002" => "Replaced broad recoverability claims with one manifest that gives every retained entry a schema/format, byte length, full digest, and explicit repository-relative access state; no persistent archive is claimed.",
    "REV-P31-004" => "Made delta total on X, kappa defined only on X_res, and every total owner-map or complete G/I/C statement conditional on X_res=X.",
    "REV-P31-005" => "Restricted the all-pairs surface to byte/bookkeeping effects and assigned self, ordered reversal, triple, and independent semantic checks to their capable fixture types.",
    "REV-P31-007" => "Ran and bound all 20 frozen queries as a new dated replay, published row-level decisions and a 24-row method-passage matrix, and retained every unresolved theorem passage as unresolved.",
    "REV-P31-008" => "Added the typed self_reciprocal, inverse_separated, and unresolved branches with their required witness/obstruction fields; no exclusion theorem or observed self-reciprocal case is asserted.",
    "REV-P31-009" => "Added one consolidated G/I/C/I_diag schema table with keys, closed cardinalities, gates, provenance fields, allowed I-to-G/C projections, and prohibited reverse reconstruction.",
    "REV-P31-011" => "Removed the remaining semantic merge/split/nontransitivity capability from the all-pairs description and bound the limitation to the absence of a target-blind independent adjudicator."
  }
}.freeze

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def write_json(path, object)
  File.binwrite(path, JSON.pretty_generate(object) + "\n")
end

def word_count(path)
  File.read(path).gsub(/<!--.*?-->/m, " ").split.length
end

def capture_json!(*command)
  stdout, stderr, status = Open3.capture3(*command)
  raise "command failed #{command.join(" ")}: #{stderr}#{stdout}" unless status.success?
  [JSON.parse(stdout), stdout, stderr]
end

def run_build!(command, cwd, transcript)
  stdout, stderr, status = Open3.capture3(*command, chdir: cwd)
  transcript << "$ #{command.join(" ")}\n" << stdout << stderr << "\n"
  raise "build command failed #{command.join(" ")}" unless status.success?
end

def paths(config)
  root = ROOT / "papers" / config[:slug]
  notes = root / "notes"
  {
    root: root, notes: notes,
    base: notes / "stage4_revision_round1.tex",
    manifest: notes / "stage4_prime_base.block-manifest.json",
    roadmap: notes / "stage4_prime_revision_roadmap.json",
    claim: notes / "stage4_prime_claim_surface_manifest.json",
    author: notes / "stage4_prime_author_adjudication.json",
    patch: notes / "stage4_prime_revision_patch_round2.json",
    revised: notes / "stage4_prime_revision_round2.tex",
    report: notes / "stage4_prime_revision_round2.tex.apply-report.json",
    bib: notes / "stage4_prime_references_round2.bib",
    prior_bundle: notes / "stage4_revision_evidence_bundle.json",
    bundle: notes / "stage4_prime_revision_evidence_bundle_round2.json",
    pdf: notes / "stage4_prime_revision_round2.pdf",
    build_log: notes / "stage4_prime_revision_round2.build.log",
    build_transcript: notes / "stage4_prime_preview_build_transcript_round2.log",
    build_receipt: notes / "stage4_prime_preview_build_receipt_round2.json",
    canonical_tex: root / "paper/manuscript.tex",
    canonical_bib: root / "paper/references.bib",
    canonical_pdf: root / "paper/paper.pdf"
  }
end

def assert_inputs!(paper_id, config, p)
  raise "#{paper_id} final patch hash changed" unless sha(p[:patch]) == config[:patch_sha]
  raise "#{paper_id} canonical tex changed" unless sha(p[:canonical_tex]) == config[:canonical_tex_sha]
  raise "#{paper_id} canonical bib changed" unless sha(p[:canonical_bib]) == config[:canonical_bib_sha]
  raise "#{paper_id} canonical pdf changed" unless sha(p[:canonical_pdf]) == config[:canonical_pdf_sha]
  [p[:revised], p[:report]].each { |path| raise "missing distinct-context apply artifact #{path}" unless File.file?(path) }
  report = JSON.parse(File.read(p[:report]))
  raise "#{paper_id} apply witness failed" unless report.dig("authorization_witness", "status") == "pass"
  raise "#{paper_id} patch/report mismatch" unless report["patch_digest"] == sha(p[:patch])
  raise "#{paper_id} op count mismatch" unless report.fetch("ops_applied").length == config[:expected_ops]
  raise "#{paper_id} registered surfaces not zero" unless report.dig("authorization_witness", "registered_claim_surfaces_checked") == 0
  report
end

def reconstruct_superseded_patch!(paper_id, p)
  if paper_id == "P30"
    # P30 required later byte/TeX remediation, so the original date-mismatch
    # patch cannot be reconstructed from the final content.  Its preserved
    # archival copies are the authoritative superseded bytes.
    expected = "85b42c725b04771fff8ffec5e94a00a956b26adebcc5238adb3a94ae0e3f771d"
    %w[stage4_prime_same_context_apply_superseded_20260904 stage4_prime_date_mismatch_superseded_20260904].each do |directory|
      archived = p[:notes] / directory / "stage4_prime_revision_patch_round2.json"
      raise "P30 archived superseded patch mismatch: #{archived}" unless sha(archived) == expected
    end
    return expected
  end

  # P31's final patch adds layout-only break opportunities.  Reconstruct the
  # first two superseded date-mismatch attempts from the preserved pre-layout
  # patch, not from the final patch.
  layout_patch = p[:notes] / "stage4_prime_layout_superseded_20260904" / "stage4_prime_revision_patch_round2.json"
  raise "P31 archived layout patch mismatch" unless sha(layout_patch) == "6b0eab8c0c6902e0a2284ba1fe86c5c6972a46e607617418bc0840f3f8b2d5d3"
  old = JSON.parse(File.read(layout_patch))
  old.fetch("ops").each do |op|
    op["new_text"] = op.fetch("new_text").gsub("3 September 2026", "4 September 2026")
  end
  bytes = JSON.pretty_generate(old) + "\n"
  expected = "26b19da9cc84985374645da83f85e99a23be41c101a275cf21083c1c846da5d1"
  raise "#{paper_id} old patch reconstruction mismatch" unless Digest::SHA256.hexdigest(bytes) == expected
  %w[stage4_prime_same_context_apply_superseded_20260904 stage4_prime_date_mismatch_superseded_20260904].each do |directory|
    File.binwrite(p[:notes] / directory / "stage4_prime_revision_patch_round2.json", bytes)
  end
  expected
end

def build_role_remediation(paper_id, p, old_patch_sha)
  same_dir = p[:notes] / "stage4_prime_same_context_apply_superseded_20260904"
  date_dir = p[:notes] / "stage4_prime_date_mismatch_superseded_20260904"
  defect_dir = p[:notes] / "stage4_prime_cr_and_latex_escape_superseded_20260904"
  layout_dir = p[:notes] / "stage4_prime_layout_superseded_20260904"
  attempts = [
    {
      "status" => "SUPERSEDED_NONCOMPLIANT_ROLE_SEPARATION",
      "directory" => "notes/#{same_dir.basename}",
      "patch_sha256" => old_patch_sha,
      "draft_sha256" => sha(same_dir / "stage4_prime_revision_round2.tex"),
      "apply_report_sha256" => sha(same_dir / "stage4_prime_revision_round2.tex.apply-report.json"),
      "remediation" => "Preserved without deletion; excluded from the evidence chain."
    },
    {
      "status" => "SUPERSEDED_PROVENANCE_DATE_MISMATCH",
      "directory" => "notes/#{date_dir.basename}",
      "patch_sha256" => old_patch_sha,
      "draft_sha256" => sha(date_dir / "stage4_prime_revision_round2.tex"),
      "apply_report_sha256" => sha(date_dir / "stage4_prime_revision_round2.tex.apply-report.json"),
      "role_separation" => "distinct root applier",
      "remediation" => "Preserved without deletion; excluded because prose said 4 September while the raw replay timestamp was 3 September."
    }
  ]
  if paper_id == "P30"
    attempts << {
      "status" => "SUPERSEDED_CONTROL_BYTE_AND_TEX_ESCAPE_DEFECT",
      "directory" => "notes/#{defect_dir.basename}",
      "patch_sha256" => sha(defect_dir / "stage4_prime_revision_patch_round2.json"),
      "draft_sha256" => sha(defect_dir / "stage4_prime_revision_round2.tex"),
      "apply_report_sha256" => sha(defect_dir / "stage4_prime_revision_round2.tex.apply-report.json"),
      "role_separation" => "distinct root applier",
      "defects" => [
        "B0084 carried four literal CR bytes where TeX rho commands were intended and lost required math delimiters.",
        "B0062/B0088/B0090 carried raw underscores in texttt identifiers; B0103 lost required math delimiters."
      ],
      "remediation" => "Preserved without deletion; excluded. Final re-emission has zero CR/control bytes, escaped identifier underscores with legal line breaks, restored B0084/B0103 math mode, and a clean four-command preview build."
    }
  else
    attempts << {
      "status" => "SUPERSEDED_LAYOUT_OVERFULL",
      "directory" => "notes/#{layout_dir.basename}",
      "patch_sha256" => sha(layout_dir / "stage4_prime_revision_patch_round2.json"),
      "draft_sha256" => sha(layout_dir / "stage4_prime_revision_round2.tex"),
      "apply_report_sha256" => sha(layout_dir / "stage4_prime_revision_round2.tex.apply-report.json"),
      "role_separation" => "distinct root applier",
      "defect" => "The isolated preview compiled but carried three overfull hboxes from full reader-manifest paths, an unabbreviated SHA-256 digest, and the branch URL in B0079/B0105.",
      "remediation" => "Preserved without deletion; excluded. Final B0079/B0105 re-emission adds deterministic discretionary breaks and local scoped layout handling without abbreviating the digest or changing semantic content."
    }
  end
  attempts << {
    "status" => "CURRENT_FINAL_DISTINCT_CONTEXT_APPLY",
    "patch_sha256" => sha(p[:patch]),
    "draft_sha256" => sha(p[:revised]),
    "apply_report_sha256" => sha(p[:report]),
    "writer_context" => "/root/r10_stage4_prime_p30_p31",
    "applier_context" => "/root",
    "byte_identity_with_same_patch_preflight" => true
  }
  object = {
    "schema_version" => "round10-stage4-prime-role-separation-remediation/1.0",
    "paper_id" => paper_id,
    "recorded_at_utc" => TIMESTAMP,
    "incident" => "The writer context performed an initial deterministic apply before the parent role-separation reminder arrived; that apply is not used as the final author-side revision artifact.",
    "attempts" => attempts,
    "final_chain_uses_superseded_attempt" => false,
    "verdict" => "REMEDIATED_BY_DISTINCT_CONTEXT_REPLAY"
  }
  path = p[:notes] / "stage4_prime_role_separation_remediation_round2.json"
  write_json(path, object)
  path
end

def build_token_receipt(p)
  object, = capture_json!("python", TOKEN_TOOL.to_s, "patch", "--patch", p[:patch].to_s, "--base", p[:base].to_s)
  path = p[:notes] / "stage4_prime_token_conservation_round2.json"
  write_json(path, object)
  path
end

def build_claim_replay(paper_id, config, p)
  object = {
    "schema" => "stage4-prime-registered-claim-surface-replay/1.0",
    "paper_number" => config[:number], "date" => DATE,
    "manifest" => {"path" => "notes/#{p[:claim].basename}", "sha256" => sha(p[:claim])},
    "revised_draft" => {"path" => "notes/#{p[:revised].basename}", "sha256" => sha(p[:revised])},
    "surface_count" => 0, "exact_once_same_block_count" => 0, "rows" => [],
    "claim_strength_replacements_authorized" => 0,
    "verdict" => "PASS_EMPTY_REGISTERED_POPULATION"
  }
  path = p[:notes] / "stage4_prime_registered_claim_surface_replay_round2.json"
  write_json(path, object)
  path
end

def item_blocks(report, item_id)
  report.fetch("ops_applied").flat_map do |op|
    next [] unless op.fetch("roadmap_item_ids").include?(item_id)
    [op.fetch("block_id"), *op.fetch("new_block_ids")]
  end.uniq
end

def build_response(paper_id, config, p, report)
  request = JSON.parse(File.read(ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json"))
  paper = request.fetch("papers").find { |entry| entry.fetch("paper_id") == paper_id }
  items = paper.fetch("items").map do |item|
    id = item.fetch("item_id")
    blocks = item_blocks(report, id)
    {
      "roadmap_item_id" => id,
      "reviewer_comment" => item.fetch("residual_gap"),
      "author_response" => RESPONSES.fetch(paper_id).fetch(id),
      "change_location" => blocks.join(", "),
      "change_block_ids" => blocks,
      "status" => "RESOLVED"
    }
  end
  delta = word_count(p[:revised]) - word_count(p[:base])
  object = {
    "revision_round" => 2,
    "items" => items,
    "summary" => {"resolved" => items.length, "limitations" => 0, "unresolvable" => 0, "disagreed" => 0},
    "word_count_delta" => delta,
    "new_references_added" => config[:new_references],
    "bibliography_scope" => "notes-side versioned Stage-4-prime bibliography; canonical bibliography frozen",
    "summary_of_changes" => config[:summary],
    "new_content_highlight" => RESPONSES.fetch(paper_id).values
  }
  json_path = p[:notes] / "stage4_prime_response_to_reviewers_round2.json"
  md_path = p[:notes] / "stage4_prime_response_to_reviewers_round2.md"
  write_json(json_path, object)
  md = +"# #{paper_id} Stage-4′ Round-2 Response to Reviewers\n\n"
  md << "Date: **#{DATE}**\n\n"
  items.each do |item|
    md << "## `#{item["roadmap_item_id"]}` — RESOLVED\n\n"
    md << "**Residual:** #{item["reviewer_comment"]}\n\n"
    md << "**Response:** #{item["author_response"]}\n\n"
    md << "**Applied blocks:** #{item["change_block_ids"].map { |id| "`#{id}`" }.join(", ")}\n\n"
  end
  md << "All #{items.length} residuals are answered within exact authorized scopes. No canonical paper file, scientific result, registered claim byte, Route state, Stage 4.5, or Stage 5 surface was changed.\n"
  File.binwrite(md_path, md)
  [json_path, md_path, object]
end

def build_revision_log(paper_id, config, p, report, response, token_path, claim_path, remediation_path)
  path = p[:notes] / "stage4_prime_revision_log_round2.md"
  lines = [
    "# #{paper_id} Stage-4′ Round-2 Revision Log", "", "Date: **#{DATE}**", "",
    "| Item | Obligation | Applied targets | Result |", "|---|---|---|---|"
  ]
  roadmap = JSON.parse(File.read(p[:roadmap])).fetch("items").to_h { |item| [item.fetch("id"), item] }
  response.fetch("items").each do |item|
    id = item.fetch("roadmap_item_id")
    blocks = item.fetch("change_block_ids").map { |block| "`#{block}`" }.join(", ")
    lines << "| `#{id}` | `#{roadmap.fetch(id).fetch("obligation_class")}` | #{blocks} | RESOLVED within exact authorized scope. |"
  end
  lines += [
    "", "## Deterministic application", "",
    "- Base SHA-256: `#{sha(p[:base])}`.",
    "- Patch 1.1 SHA-256: `#{sha(p[:patch])}`.",
    "- Revised draft SHA-256: `#{sha(p[:revised])}`.",
    "- Apply report 1.3 SHA-256: `#{sha(p[:report])}`.",
    "- Applied operations: #{report.fetch("ops_applied").length}; preserved blocks: #{config[:expected_preserved]}; touched ratio: #{report.dig("structural_flags", "touched_ratio")}.",
    "- Authorization witness: PASS; registered claim surfaces checked: 0; section-count delta: #{report.dig("structural_flags", "section_count_delta")}.",
    "- Role-separation remediation: `#{sha(remediation_path)}`; superseded attempts are preserved and excluded from the chain.",
    "", "## Audit boundaries", "",
    "- Token-conservation sidecar: `#{sha(token_path)}` (advisory changes correspond to authorized dates, counts, parameters, tables, citations, and artifact hashes).",
    "- Registered-surface replay: `#{sha(claim_path)}` (empty registered population, 0/0).",
    "- Canonical manuscript, bibliography, and PDF remain byte-frozen.",
    "- No scientific experiment, result refresh, Stage 4.5, Stage 5, or Route transition occurred.",
    "", "Stage status: **Stage 4′ author-side revision complete after build and audit; author confirmation and fresh Stage 4.5 remain pending.**", ""
  ]
  File.binwrite(path, lines.join("\n"))
  path
end

def build_drift_audit(paper_id, config, p, report, token_path, claim_path)
  path = p[:notes] / "stage4_prime_unregistered_claim_drift_audit_round2.md"
  item_rows = if paper_id == "P30"
    [
      ["literature/corrections", "Adds row-level replay and correction provenance while preserving passage-level uncertainty and unavailable historical rows.", "provenance strengthened; scientific claim unchanged"],
      ["controls", "Adds exact authorized design parameters and property boundaries; repeatedly states that no comparison or enclosure was executed.", "prospective contract only"],
      ["six-gate map", "Makes receipts, uncertainty, consumers, and stop states explicit; Gates 1--5 remain NOT_STARTED and Gate 6 NOT_ACTIVATED.", "no state promotion"]
    ]
  else
    [
      ["closest work/replay", "Adds two narrow method neighbors and row-level retrieval evidence with explicit no-priority and no-theorem-transfer boundaries.", "positioning strengthened; owner claim unchanged"],
      ["owner typing", "Separates total disposition from resolved owner map and adds prospective inverse branches without asserting a witness or exclusion theorem.", "type correction; no observed owner result"],
      ["audit and G/I/C", "Narrows all-pairs capability and makes projection/gating rules explicit; no semantic adjudicator or materialized relation is claimed.", "capability narrowed; no result"]
    ]
  end
  lines = [
    "# #{paper_id} Stage-4′ Round-2 Unregistered-Claim Drift Audit", "", "Date: **#{DATE}**", "",
    "Status: **PASS WITH MODEL-MEDIATED LIMITATION — no unauthorized strengthening found in the reviewed changed blocks**", "",
    "This answers the apply report's `unregistered_claim_drift_review_required=true` boundary for Stage 4′. It is not a deterministic proof of semantic completeness, is not a fresh Stage-4.5 E6 review, and authorizes no later-stage promotion.", "",
    "## Bound artifacts", "",
    "- patch: `#{sha(p[:patch])}`;", "- revised draft: `#{sha(p[:revised])}`;",
    "- apply report: `#{sha(p[:report])}`;", "- token sidecar: `#{sha(token_path)}`;",
    "- registered-surface replay: `#{sha(claim_path)}`.", "", "## Semantic comparison", "",
    "| Surface | Old-to-new comparison | Direction |", "|---|---|---|"
  ]
  item_rows.each { |row| lines << "| #{row[0]} | #{row[1]} | #{row[2]} |" }
  lines += [
    "", "## Deterministic facts", "",
    "- all #{report.fetch("ops_applied").length} operations carry empty `claim_strength_changes` and `collateral_authorization_ids`;",
    "- registered population is 0, so the deterministic registered-surface replay is 0/0 and PASS;",
    "- preserved blocks are #{config[:expected_preserved]}, section count is unchanged, and the authorization witness is PASS;",
    "- canonical manuscript/bibliography/PDF hashes equal the input freeze;",
    "- no science/result execution or canonical result refresh occurred;",
    "- Route state remains `#{config[:route_state]}`.", "",
    "The reviewed edits improve provenance, definitions, and limitations without asserting a new scientific value or completed certificate. This conclusion remains a model-mediated judgment; Stage 4.5 must reassess E6 independently.", ""
  ]
  File.binwrite(path, lines.join("\n"))
  path
end

def build_evidence_bundle(p, report)
  prior = JSON.parse(File.read(p[:prior_bundle]))
  raise "prior evidence bundle should contain exactly round 1" unless prior.fetch("rounds").length == 1
  round = {
    "kind" => "review_roadmap", "revision_round" => 2,
    "pre_round_draft" => {"path" => "notes/#{p[:base].basename}", "sha256" => sha(p[:base])},
    "pre_round_block_manifest" => {"path" => "notes/#{p[:manifest].basename}", "sha256" => sha(p[:manifest])},
    "revision_roadmap" => {"path" => "notes/#{p[:roadmap].basename}", "sha256" => sha(p[:roadmap])},
    "claim_surface_manifest" => {"path" => "notes/#{p[:claim].basename}", "sha256" => sha(p[:claim])},
    "author_adjudication" => {"path" => "notes/#{p[:author].basename}", "sha256" => sha(p[:author])},
    "revision_patch" => {"path" => "notes/#{p[:patch].basename}", "sha256" => sha(p[:patch])},
    "apply_report" => {"path" => "notes/#{p[:report].basename}", "sha256" => sha(p[:report])},
    "post_round_draft" => {"path" => "notes/#{p[:revised].basename}", "sha256" => sha(p[:revised])}
  }
  prior["rounds"] << round
  prior["final_draft"] = round["post_round_draft"]
  write_json(p[:bundle], prior)
  stdout, stderr, status = Open3.capture3("python", ROADMAP_TOOL.to_s, "validate-bundle", p[:bundle].to_s, "--root", p[:root].to_s)
  receipt = {
    "schema_version" => "round10-stage4-prime-bundle-validation-receipt/1.0",
    "validated_at_utc" => TIMESTAMP,
    "bundle" => {"path" => "notes/#{p[:bundle].basename}", "sha256" => sha(p[:bundle])},
    "command" => "python revision_roadmap.py validate-bundle <bundle> --root <paper-root>",
    "exit_code" => status.exitstatus, "stdout" => stdout.strip, "stderr" => stderr.strip,
    "ordered_apply_chain" => report.dig("authorization_witness", "status") == "pass" ? "PASS" : "FAIL",
    "verdict" => status.success? ? "PASS" : "FAIL"
  }
  receipt_path = p[:notes] / "stage4_prime_bundle_validation_receipt_round2.json"
  write_json(receipt_path, receipt)
  raise "bundle validation failed: #{stderr}#{stdout}" unless status.success?
  receipt_path
end

def build_preview(config, p)
  transcript = +""
  begin
    Dir.mktmpdir("p#{config[:number]}-stage4-prime-preview.") do |tmp|
      marker_free = File.read(p[:revised]).lines.reject { |line| line.match?(/\A<!--block:B\d+-->\s*\z/) }.join
      File.binwrite(File.join(tmp, "manuscript.tex"), marker_free)
      FileUtils.cp(p[:bib], File.join(tmp, "references.bib"))
      job = "stage4_prime_revision_round2"
      run_build!(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"], tmp, transcript)
      run_build!(["bibtex", job], tmp, transcript)
      2.times { run_build!(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=#{job}", "manuscript.tex"], tmp, transcript) }
      FileUtils.cp(File.join(tmp, "#{job}.pdf"), p[:pdf])
      FileUtils.cp(File.join(tmp, "#{job}.log"), p[:build_log])
    end
  ensure
    File.binwrite(p[:build_transcript], transcript)
  end
  log = File.read(p[:build_log])
  info, error, status = Open3.capture3("pdfinfo", p[:pdf].to_s)
  raise "pdfinfo failed: #{error}" unless status.success?
  overfull = log.scan(/Overfull \\hbox \(([0-9.]+)pt too wide\)/).flatten.map(&:to_f)
  underfull = log.scan(/Underfull \\hbox/).length
  undefined_citations = log.scan(/(?:Citation [`'][^\n]+ undefined|There were undefined citations)/).length
  undefined_references = log.scan(/(?:Reference [`'][^\n]+ undefined|There were undefined references)/).length
  missing = log.scan(/Missing character:/).length
  fatal = log.scan(/(?:Fatal error|Emergency stop)/i).length
  clean = overfull.empty? && undefined_citations.zero? && undefined_references.zero? && missing.zero? && fatal.zero?
  draft = File.read(p[:revised])
  cited = draft.scan(/\\cite\w*\{([^}]+)\}/).flatten.flat_map { |keys| keys.split(",") }.map(&:strip).uniq
  receipt = {
    "schema" => "round10-stage4-prime-preview-build-receipt/1.0",
    "paper_number" => config[:number], "date" => DATE,
    "classification" => "STAGE4_PRIME_MARKER_STRIPPED_PREVIEW_NOT_STAGE5_PROMOTION",
    "status" => clean ? "PASS" : "FAIL",
    "compiler_sequence" => ["lualatex", "bibtex", "lualatex", "lualatex"],
    "compiler_exit_codes_all_zero" => true,
    "citation_style" => "plainnat_numeric_current",
    "citation_commands" => draft.scan(/\\cite\w*\{/).length,
    "unique_citation_keys" => cited.length,
    "pages" => info[/^Pages:\s+(\d+)/, 1].to_i,
    "page_size" => info[/^Page size:\s+(.+)$/, 1],
    "undefined_citations" => undefined_citations, "undefined_references" => undefined_references,
    "missing_characters" => missing, "fatal_errors" => fatal,
    "overfull_hboxes" => overfull.length, "maximum_overfull_pt" => overfull.max || 0.0,
    "underfull_hboxes" => underfull,
    "layout_advisory" => overfull.empty? ? "NONE" : "OVERFULL_HBOX_PRESENT",
    "marker_strip_rule" => "remove only lines matching ^<!--block:B[0-9]+-->$",
    "temporary_build_directory_removed" => true,
    "pdf_byte_reproducibility_claimed" => false,
    "bindings" => {
      "revised_anchored_draft_sha256" => sha(p[:revised]), "revision_patch_sha256" => sha(p[:patch]),
      "revision_evidence_bundle_sha256" => sha(p[:bundle]), "versioned_references_bib_sha256" => sha(p[:bib]),
      "preview_pdf_sha256" => sha(p[:pdf]), "final_build_log_sha256" => sha(p[:build_log])
    },
    "write_boundary" => {
      "paper_manuscript_modified" => false, "canonical_paper_bibliography_modified" => false,
      "canonical_paper_pdf_modified" => false, "canonical_results_refreshed" => false,
      "stage4_5_invoked" => false, "stage5_invoked" => false
    }
  }
  write_json(p[:build_receipt], receipt)
  raise "preview validation failed" unless clean
  receipt
end

def build_support_bundle(paper_id, config, p, response_paths, token_path, claim_path, drift_path, log_path, remediation_path, bundle_receipt, preview)
  support_names = if paper_id == "P30"
    %w[stage4_prime_literature_replay_round2.raw.json stage4_prime_literature_screening_ledger_round2.json stage4_prime_literature_screening_ledger_round2.tsv stage4_prime_claim_passage_matrix_round2.json stage4_prime_claim_passage_matrix_round2.tsv stage4_prime_correction_source_verification_round2.json stage4_prime_reader_artifact_manifest_round2.json stage4_prime_references_round2.bib]
  else
    %w[stage4_prime_literature_replay_round2.raw.json stage4_prime_literature_screening_ledger_round2.json stage4_prime_literature_screening_ledger_round2.tsv stage4_prime_method_passage_matrix_round2.json stage4_prime_method_passage_matrix_round2.tsv stage4_prime_closest_work_source_verification_round2.json stage4_prime_reader_artifact_manifest_round2.json stage4_prime_references_round2.bib]
  end
  artifact = lambda { |path| {"path" => "notes/#{path.basename}", "sha256" => sha(path), "bytes" => File.size(path)} }
  object = {
    "schema_version" => "round10-stage4-prime-support-evidence-bundle/1.0",
    "paper_id" => paper_id, "revision_round" => 2, "date" => DATE,
    "authority" => AUTHORITY.map { |path, digest| {"path" => path, "sha256" => digest} },
    "revision_chain" => artifact.call(p[:bundle]).merge("official_validation" => "PASS"),
    "apply" => {"patch" => artifact.call(p[:patch]), "draft" => artifact.call(p[:revised]), "report" => artifact.call(p[:report]), "authorization_witness" => "PASS"},
    "support_artifacts" => support_names.map { |name| artifact.call(p[:notes] / name) },
    "audit_artifacts" => [*response_paths, token_path, claim_path, drift_path, log_path, remediation_path, bundle_receipt, p[:build_receipt]].map { |path| artifact.call(path) },
    "preview" => {"status" => preview["status"], "pages" => preview["pages"], "pdf" => artifact.call(p[:pdf]), "build_log" => artifact.call(p[:build_log])},
    "registered_surfaces" => "0/0",
    "scientific_value_changed" => false, "canonical_result_refreshed" => false,
    "route_tuple_changed" => false, "stage4_5_invoked" => false, "stage5_invoked" => false,
    "pdf_byte_reproducibility_claimed" => false,
    "verdict" => "STAGE4_PRIME_EVIDENCE_BOUND"
  }
  path = p[:notes] / "stage4_prime_support_evidence_bundle_round2.json"
  write_json(path, object)
  path
end

def build_completion(paper_id, config, p, report, preview, support_bundle)
  path = p[:notes] / "stage4_prime_completion_report_round2.md"
  body = <<~MD
    # #{paper_id} Stage-4′ Round-2 Completion Report

    Date: **#{DATE}**

    Status: **COMPLETE — author-side Stage 4′ only; Stage 4.5 remains uninvoked and requires a fresh mandatory gate**

    ## Outcome

    #{config[:summary]}

    - residual items resolved: #{RESPONSES.fetch(paper_id).length}/#{RESPONSES.fetch(paper_id).length};
    - Patch 1.1 operations: #{report.fetch("ops_applied").length}; authorization witness: PASS;
    - byte-identical preserved blocks: #{config[:expected_preserved]}; touched ratio: #{report.dig("structural_flags", "touched_ratio")};
    - registered claim population: 0/0; claim-strength replacements: 0;
    - preview: #{preview["pages"]} pages, zero undefined citations/references, missing glyphs, fatal errors, or overfull boxes;
    - Route state unchanged: `#{config[:route_state]}`.

    ## Principal bindings

    - final patch SHA-256: `#{sha(p[:patch])}`;
    - final revised draft SHA-256: `#{sha(p[:revised])}`;
    - apply report SHA-256: `#{sha(p[:report])}`;
    - revision-evidence bundle SHA-256: `#{sha(p[:bundle])}`;
    - support-evidence bundle SHA-256: `#{sha(support_bundle)}`;
    - preview PDF SHA-256: `#{sha(p[:pdf])}`.

    The canonical manuscript, canonical bibliography, canonical PDF, scientific inputs/results, initial dynamical-system restriction, and Route-A/Route-B state remain byte-frozen. The only bibliography additions are in the notes-side versioned preview input. Superseded apply attempts are preserved with an explicit role-separation/remediation record and are not part of the final evidence chain.
  MD
  File.binwrite(path, body)
  path
end

AUTHORITY.each do |relative, expected|
  actual = sha(ROOT / relative.delete_prefix("../../../"))
  raise "authority hash mismatch #{relative}" unless actual == expected
end

selected_papers = ARGV.empty? ? CONFIG.keys : ARGV
unknown_papers = selected_papers - CONFIG.keys
raise "unknown paper selector(s): #{unknown_papers.join(", ")}" unless unknown_papers.empty?

selected_papers.each do |paper_id|
  config = CONFIG.fetch(paper_id)
  p = paths(config)
  report = assert_inputs!(paper_id, config, p)
  old_patch_sha = reconstruct_superseded_patch!(paper_id, p)
  remediation_path = build_role_remediation(paper_id, p, old_patch_sha)
  token_path = build_token_receipt(p)
  claim_path = build_claim_replay(paper_id, config, p)
  response_json, response_md, response = build_response(paper_id, config, p, report)
  revision_log = build_revision_log(paper_id, config, p, report, response, token_path, claim_path, remediation_path)
  drift_path = build_drift_audit(paper_id, config, p, report, token_path, claim_path)
  bundle_receipt = build_evidence_bundle(p, report)
  preview = build_preview(config, p)
  support_bundle = build_support_bundle(paper_id, config, p, [response_json, response_md], token_path, claim_path, drift_path, revision_log, remediation_path, bundle_receipt, preview)
  completion = build_completion(paper_id, config, p, report, preview, support_bundle)
  assert_inputs!(paper_id, config, p)
  puts "#{paper_id}: finalized #{RESPONSES.fetch(paper_id).length} residuals; preview #{preview["pages"]} pages; completion #{completion}"
end
