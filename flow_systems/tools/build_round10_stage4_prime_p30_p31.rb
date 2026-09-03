#!/usr/bin/env ruby
# frozen_string_literal: true

require "csv"
require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent.expand_path
ARS_ROOT = Pathname.new("/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/skills/academic-research-suite/ars")
ROADMAP_CLI = ARS_ROOT / "scripts/revision_roadmap.py"
DATE = "2026-09-04"
TIMESTAMP = "2026-09-04T00:30:00Z"

AUTHORITY_HASHES = {
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json" => "a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688",
  "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md" => "4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt" => "111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md" => "67ad4ce8bfb34676b46ffb96e8c9833c1204ada3ffde1e0dc542ea43c46acca5",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json" => "c94137879092d7d475b22c8985a8f09073c29027f77a89b8ccb8749acfdac48b",
  "BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json" => "82dbf52120f120ffea6ba82b4614c69d4022a32bc01305a892eadde92b8248b7"
}.freeze

PAPERS = {
  "P30" => {
    number: 30,
    slug: "30-three-disk-nonconstant-roof-determinant",
    base_sha: "9d8c7201420d182154796ed714e34de466cc683a7910f9830825ec4ea8efd3e7",
    manifest_sha: "a3eaa92d60149c9f4facf43be4b5357ea64608188a44e9768c3a472566b86dab",
    canonical_bib_sha: "1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f",
    canonical_tex_sha: "af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506",
    canonical_pdf_sha: "c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e"
  },
  "P31" => {
    number: 31,
    slug: "31-level11-conjugacy-owner-ledger",
    base_sha: "03304330e06f2af77a9311908ab0bbc4d350dd9e5b54a47744cd1e3367a6f6d5",
    manifest_sha: "8bd7801b604aedd1227185730b370f01d279aece6b83c7777d9db3bc685f0fb5",
    canonical_bib_sha: "b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958",
    canonical_tex_sha: "f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a",
    canonical_pdf_sha: "f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722"
  }
}.freeze

def sha(path)
  Digest::SHA256.file(path).hexdigest
end

def bytes(path)
  File.size(path)
end

def write_json(path, object)
  File.write(path, JSON.pretty_generate(object) + "\n")
end

def deep_sort(value)
  case value
  when Hash
    value.keys.sort.each_with_object({}) { |key, out| out[key] = deep_sort(value[key]) }
  when Array
    value.map { |entry| deep_sort(entry) }
  else
    value
  end
end

def canonical_hash(value)
  Digest::SHA256.hexdigest(JSON.generate(deep_sort(value)))
end

def author_decision_digest(adjudication)
  canonical_hash({
    "author_events" => adjudication["author_events"],
    "display_order" => adjudication["display_order"],
    "author_adjudications" => adjudication["author_adjudications"],
    "collateral_authorizations" => adjudication["collateral_authorizations"]
  })
end

def paper_paths(config)
  root = ROOT / "papers" / config[:slug]
  {
    root: root,
    notes: root / "notes",
    base: root / "notes/stage4_revision_round1.tex",
    manifest: root / "notes/stage4_prime_base.block-manifest.json",
    canonical_bib: root / "paper/references.bib",
    canonical_tex: root / "paper/manuscript.tex",
    canonical_pdf: root / "paper/paper.pdf",
    old_roadmap: root / "notes/stage3_revision_roadmap.json",
    raw_replay: root / "notes/stage4_prime_literature_replay_round2.raw.json",
    roadmap: root / "notes/stage4_prime_revision_roadmap.json",
    claim_manifest: root / "notes/stage4_prime_claim_surface_manifest.json",
    choices: root / "notes/stage4_prime_author_choices.json",
    adjudication: root / "notes/stage4_prime_author_adjudication.json",
    patch: root / "notes/stage4_prime_revision_patch_round2.json",
    versioned_bib: root / "notes/stage4_prime_references_round2.bib",
    reader_manifest: root / "notes/stage4_prime_reader_artifact_manifest_round2.json"
  }
end

def verify_frozen_inputs!
  AUTHORITY_HASHES.each do |rel, expected|
    actual = sha(ROOT / rel)
    raise "authority hash mismatch #{rel}: #{actual}" unless actual == expected
  end
  PAPERS.each_value do |config|
    p = paper_paths(config)
    {
      p[:base] => config[:base_sha],
      p[:manifest] => config[:manifest_sha],
      p[:canonical_bib] => config[:canonical_bib_sha],
      p[:canonical_tex] => config[:canonical_tex_sha],
      p[:canonical_pdf] => config[:canonical_pdf_sha]
    }.each do |path, expected|
      actual = sha(path)
      raise "frozen input hash mismatch #{path}: #{actual}" unless actual == expected
    end
  end
end

def read_tsv(path)
  CSV.read(path, headers: true, col_sep: "\t").map(&:to_h)
end

def normalized_title(text)
  text.to_s.downcase.gsub(/[^a-z0-9]+/, " ").strip
end

def build_replay_ledger(paper_id, paths)
  raw = JSON.parse(File.read(paths[:raw_replay]))
  inventory = read_tsv(paths[:root] / "notes/stage1_phase2_source_inventory.tsv")
  doi_index = inventory.reject { |r| r["doi"].to_s.empty? }.to_h { |r| [r["doi"].downcase, r] }
  title_index = inventory.to_h { |r| [normalized_title(r["title"]), r] }
  rows = raw.fetch("rows").map do |row|
    record = row.dig("crossref", "top_record") || {}
    match = doi_index[record["doi"].to_s.downcase] || title_index[normalized_title(record["title"])]
    decision = match ? "RETAIN_EXISTING_INVENTORY_RECORD" : "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE"
    {
      "query_id" => row["query_id"],
      "exact_frozen_query" => row["query"],
      "retrieved_at_utc" => row["retrieved_at_utc"],
      "interface" => "Crossref REST query.bibliographic; rows=1",
      "http_status" => row.dig("crossref", "http_status"),
      "candidate_doi" => record["doi"],
      "candidate_title" => record["title"],
      "candidate_year" => record["year"],
      "decision" => decision,
      "matched_source_id" => match && match["source_id"],
      "decision_reason" => if match
        "Top-ranked metadata record is already present in the frozen admitted inventory; no new scientific record is created."
      else
        "Top-ranked metadata record does not match the frozen admitted inventory by DOI or normalized title; it is not adopted by this bounded replay."
      end
    }
  end
  ledger = {
    "schema_version" => "round10-stage4-prime-literature-screening-ledger/1.0",
    "paper_id" => paper_id,
    "generated_at_utc" => TIMESTAMP,
    "source_raw_replay" => {
      "path" => "notes/#{paths[:raw_replay].basename}",
      "sha256" => sha(paths[:raw_replay]),
      "rows" => raw.fetch("rows").length
    },
    "method" => {
      "retrieval_bound" => raw["retrieval_bound"],
      "match_rule" => "case-insensitive DOI equality, then normalized-title equality, against the frozen admitted inventory",
      "decision_vocabulary" => ["RETAIN_EXISTING_INVENTORY_RECORD", "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE"],
      "historical_reconstruction_boundary" => raw["historical_reconstruction_boundary"]
    },
    "row_count" => rows.length,
    "retained_existing" => rows.count { |r| r["decision"] == "RETAIN_EXISTING_INVENTORY_RECORD" },
    "screened_out" => rows.count { |r| r["decision"] == "SCREEN_OUT_OUTSIDE_FROZEN_SCOPE" },
    "rows" => rows,
    "scientific_result_changed" => false,
    "canonical_result_refreshed" => false
  }
  json_path = paths[:notes] / "stage4_prime_literature_screening_ledger_round2.json"
  tsv_path = paths[:notes] / "stage4_prime_literature_screening_ledger_round2.tsv"
  write_json(json_path, ledger)
  CSV.open(tsv_path, "w", col_sep: "\t") do |csv|
    keys = rows.first.keys
    csv << keys
    rows.each { |row| csv << keys.map { |key| row[key] } }
  end
  [json_path, tsv_path, ledger]
end

def build_passage_matrix(paper_id, paths, additions)
  matrix = read_tsv(paths[:root] / "notes/stage1_phase3_literature_matrix.tsv")
  rows = matrix.map do |row|
    {
      "source_id" => row["source_id"],
      "component_or_claim_role" => row["admissible_contribution"],
      "exact_passage_locator" => nil,
      "passage_status" => "INCONCLUSIVE",
      "hypothesis_or_scope" => row["compatibility_role"],
      "transfer_boundary" => row["excluded_stronger_claim"],
      "evidence_note" => row["locator_or_verification_limit"]
    }
  end
  additions.each { |addition| rows << addition }
  object = {
    "schema_version" => "round10-stage4-prime-claim-passage-matrix/1.0",
    "paper_id" => paper_id,
    "generated_at_utc" => TIMESTAMP,
    "source_matrix" => {
      "path" => "notes/stage1_phase3_literature_matrix.tsv",
      "sha256" => sha(paths[:root] / "notes/stage1_phase3_literature_matrix.tsv")
    },
    "row_count" => rows.length,
    "passage_finalized_count" => rows.count { |r| r["passage_status"] == "FINALIZED" },
    "passage_inconclusive_count" => rows.count { |r| r["passage_status"] == "INCONCLUSIVE" },
    "rows" => rows,
    "boundary" => "Record identity and role coding do not establish theorem-to-claim transfer. Null locators remain unresolved and were not reconstructed."
  }
  stem = paper_id == "P30" ? "claim" : "method"
  json_path = paths[:notes] / "stage4_prime_#{stem}_passage_matrix_round2.json"
  tsv_path = paths[:notes] / "stage4_prime_#{stem}_passage_matrix_round2.tsv"
  write_json(json_path, object)
  CSV.open(tsv_path, "w", col_sep: "\t") do |csv|
    keys = rows.first.keys
    csv << keys
    rows.each { |row| csv << keys.map { |key| row[key] } }
  end
  [json_path, tsv_path, object]
end

def append_versioned_bibliographies(paths30, paths31)
  p30_add = <<~'BIB'

    @article{P30-C01,
      author  = {Gaspard, Pierre and Rice, Stuart A.},
      title   = {Erratum: Scattering from a Classically Chaotic Repellor},
      journal = {The Journal of Chemical Physics},
      year    = {1989},
      volume  = {91},
      number  = {5},
      pages   = {3279--3279},
      doi     = {10.1063/1.457669},
      url     = {https://doi.org/10.1063/1.457669}
    }

    @article{P30-C02,
      author  = {Gaspard, Pierre and Rice, Stuart A.},
      title   = {Erratum: Exact Quantization of the Scattering from a Classically Chaotic Repellor},
      journal = {The Journal of Chemical Physics},
      year    = {1989},
      volume  = {91},
      number  = {5},
      pages   = {3280--3280},
      doi     = {10.1063/1.457670},
      url     = {https://doi.org/10.1063/1.457670}
    }
  BIB
  p31_add = <<~'BIB'

    @inproceedings{P31-S23,
      author    = {Necula, George C.},
      title     = {Proof-Carrying Code},
      booktitle = {Proceedings of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages},
      year      = {1997},
      pages     = {106--119},
      publisher = {ACM Press},
      doi       = {10.1145/263699.263712},
      url       = {https://doi.org/10.1145/263699.263712}
    }

    @inproceedings{P31-S24,
      author    = {Crosby, Scott A. and Wallach, Dan S.},
      title     = {Efficient Data Structures for Tamper-Evident Logging},
      booktitle = {18th USENIX Security Symposium (USENIX Security 09)},
      year      = {2009},
      publisher = {USENIX Association},
      address   = {Montreal, Quebec},
      url       = {https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/efficient-data-structures-tamper-evident}
    }
  BIB
  File.write(paths30[:versioned_bib], File.binread(paths30[:canonical_bib]) + p30_add)
  File.write(paths31[:versioned_bib], File.binread(paths31[:canonical_bib]) + p31_add)
end

def build_source_verification_receipts(paths30, paths31)
  p30 = {
    "schema_version" => "round10-stage4-prime-correction-source-verification/1.0",
    "paper_id" => "P30",
    "verified_at_utc" => TIMESTAMP,
    "verification_interface" => "Crossref DOI REST metadata plus DOI resolution to AIP Publishing",
    "records" => [
      {
        "key" => "P30-C01", "doi" => "10.1063/1.457669",
        "authors" => ["Pierre Gaspard", "Stuart A. Rice"],
        "title" => "Erratum: Scattering from a classically chaotic repellor",
        "container_title" => "The Journal of Chemical Physics", "year" => 1989,
        "volume" => "91", "issue" => "5", "pages" => "3279--3279",
        "crossref_url" => "https://api.crossref.org/works/10.1063/1.457669",
        "publisher_url" => "https://doi.org/10.1063/1.457669",
        "binds_source_ids" => ["P30-S01", "P30-S02"], "verdict" => "VERIFIED"
      },
      {
        "key" => "P30-C02", "doi" => "10.1063/1.457670",
        "authors" => ["Pierre Gaspard", "Stuart A. Rice"],
        "title" => "Erratum: Exact quantization of the scattering from a classically chaotic repellor",
        "container_title" => "The Journal of Chemical Physics", "year" => 1989,
        "volume" => "91", "issue" => "5", "pages" => "3280--3280",
        "crossref_url" => "https://api.crossref.org/works/10.1063/1.457670",
        "publisher_url" => "https://doi.org/10.1063/1.457670",
        "binds_source_ids" => ["P30-S03"], "verdict" => "VERIFIED"
      }
    ],
    "bibliography_mode" => "notes-side versioned build input; canonical paper/references.bib remains frozen",
    "versioned_bibliography" => {
      "path" => "notes/#{paths30[:versioned_bib].basename}", "sha256" => sha(paths30[:versioned_bib])
    },
    "new_entries" => 2, "maximum_authorized_new_entries" => 2, "verdict" => "PASS"
  }
  p30_path = paths30[:notes] / "stage4_prime_correction_source_verification_round2.json"
  write_json(p30_path, p30)

  p31 = {
    "schema_version" => "round10-stage4-prime-closest-work-source-verification/1.0",
    "paper_id" => "P31",
    "verified_at_utc" => TIMESTAMP,
    "search_scope" => "bounded closest-work search for proof-carrying-data and ledger-verification method families",
    "records" => [
      {
        "key" => "P31-S23", "method_family" => "proof-carrying code/data",
        "authors" => ["George C. Necula"], "year" => 1997,
        "title" => "Proof-carrying code",
        "venue" => "Proceedings of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages",
        "pages" => "106--119", "doi" => "10.1145/263699.263712",
        "authoritative_metadata" => "https://api.crossref.org/works/10.1145/263699.263712",
        "publisher_locator" => "https://doi.org/10.1145/263699.263712",
        "admissible_transfer" => "producer-supplied evidence checked by a comparatively simple consumer",
        "prohibited_transfer" => "does not prove the P31 group-theoretic owner map or certificate completeness",
        "verdict" => "VERIFIED"
      },
      {
        "key" => "P31-S24", "method_family" => "tamper-evident ledger verification",
        "authors" => ["Scott A. Crosby", "Dan S. Wallach"], "year" => 2009,
        "title" => "Efficient Data Structures for Tamper-Evident Logging",
        "venue" => "18th USENIX Security Symposium (USENIX Security 09)",
        "authoritative_metadata" => "https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/efficient-data-structures-tamper-evident",
        "publisher" => "USENIX Association",
        "admissible_transfer" => "history-tree membership and consistency proof patterns for append-only evidence",
        "prohibited_transfer" => "does not establish mathematical owner identity or substitute for an independent semantic adjudicator",
        "verdict" => "VERIFIED"
      }
    ],
    "new_entries" => 2, "maximum_authorized_new_entries" => 4,
    "novelty_boundary" => "No priority or exhaustive novelty claim is made; the sources position method components only.",
    "bibliography_mode" => "notes-side versioned build input; canonical paper/references.bib remains frozen",
    "versioned_bibliography" => {
      "path" => "notes/#{paths31[:versioned_bib].basename}", "sha256" => sha(paths31[:versioned_bib])
    },
    "verdict" => "PASS"
  }
  p31_path = paths31[:notes] / "stage4_prime_closest_work_source_verification_round2.json"
  write_json(p31_path, p31)
  [p30_path, p31_path]
end

def build_reader_manifest(paper_id, paths, artifacts)
  rows = artifacts.map do |path, schema, access_state|
    {
      "path" => path.relative_path_from(paths[:root]).to_s,
      "schema_or_format" => schema,
      "sha256" => sha(path),
      "bytes" => bytes(path),
      "repository_relative_access_state" => access_state
    }
  end
  object = {
    "schema_version" => "round10-stage4-prime-reader-artifact-manifest/1.0",
    "paper_id" => paper_id,
    "generated_at_utc" => TIMESTAMP,
    "repository_locator" => "https://github.com/maris205/hilbert-polya-structure/tree/main/flow_systems/papers/#{paths[:root].basename}",
    "locator_state" => "branch-relative locator; not content-addressed and not a persistent archive",
    "entry_count" => rows.length,
    "entries" => rows,
    "boundary" => {
      "persistent_archive_claimed" => false,
      "canonical_results_refreshed" => false,
      "scientific_artifacts_claimed" => false,
      "reader_recoverability_limited_to_listed_entries" => true
    }
  }
  write_json(paths[:reader_manifest], object)
  object
end

def request_paper(request, paper_id)
  request.fetch("papers").find { |paper| paper.fetch("paper_id") == paper_id } || raise("missing request paper #{paper_id}")
end

def build_residual_roadmap(request, paper_id, config, paths)
  requested = request_paper(request, paper_id)
  old = JSON.parse(File.read(paths[:old_roadmap]))
  old_by_id = old.fetch("items").to_h { |item| [item.fetch("id"), item] }
  items = requested.fetch("items").map do |residual|
    source = Marshal.load(Marshal.dump(old_by_id.fetch(residual.fetch("item_id"))))
    source["description"] = residual.fetch("residual_gap")
    source["obligation_class"] = residual.fetch("residual_obligation_class")
    source["evidence_anchor"] = {
      "anchor_type" => "absence",
      "locator" => "notes/stage3_prime_round2_verification_report.md, #{residual.fetch("item_id")}",
      "absence_scope" => residual.fetch("residual_gap"),
      "check_performed" => "Checked the frozen Stage-3-prime Round-2 verdict, traceability, current Stage-4 draft, block manifest, and authorized target surface."
    }
    source["confidence"] = 5
    source["competence_basis"] = "Stage-3-prime residual verification bound to the exact current Stage-4 draft and content-neutral block manifest"
    source["cost_scope"] = {
      "kind" => "section",
      "locator" => residual.fetch("proposed_targets").map { |target| target.fetch("block_id") }.join(", ")
    }
    source["consequence_if_unaddressed"] = {
      "code" => "evidence_gap_remains",
      "target" => {"kind" => "claim", "locator" => residual.fetch("residual_gap")[0, 400]}
    }
    source["target_section"] = residual.fetch("proposed_targets").map { |target| target.fetch("block_id") }.join(", ")
    source["suggested_action"] = residual.fetch("implementation_branch")
    source["verification_criteria"] = "Every authorized target used by the patch stays within the exact operation scope, the named residual evidence is explicit, and no scientific value, registered claim byte, canonical file, or Route state changes."
    source["proposed_targets"] = residual.fetch("proposed_targets")
    source
  end
  counts = %w[must_fix should_fix consider].to_h { |kind| [kind, items.count { |item| item["obligation_class"] == kind }] }
  roadmap = {
    "schema_version" => "revision-roadmap/1.0",
    "revision_round" => 2,
    "base_draft_sha256" => config[:base_sha],
    "block_manifest_sha256" => config[:manifest_sha],
    "items" => items,
    "total_items" => items.length,
    "obligation_counts" => counts,
    "editorial_decision" => "Major Revision",
    "consensus_summary" => "This non-ranking Stage-4-prime roadmap contains only the #{items.length} explicitly authorized residual items from the frozen Stage-3-prime Round-2 verification. It creates no authority beyond the separately bound author adjudication.",
    "dissenting_opinions" => []
  }
  write_json(paths[:roadmap], roadmap)
  roadmap
end

def build_claim_manifest(paths, roadmap)
  object = {
    "schema_version" => "claim-surface-manifest/1.0",
    "revision_round" => 2,
    "roadmap_sha256" => sha(paths[:roadmap]),
    "base_draft_sha256" => roadmap.fetch("base_draft_sha256"),
    "claim_intent_sources" => [],
    "surfaces" => []
  }
  write_json(paths[:claim_manifest], object)
  object
end

def build_author_choices(request, paper_id, paths)
  items = request_paper(request, paper_id).fetch("items")
  event_id = "AUTHOR-EVENT-20260903-ROUND10-STAGE4-PRIME-P30-P31"
  object = {
    "schema_version" => "author-adjudication-input/1.0",
    "author_events" => [{
      "event_id" => event_id,
      "source" => "explicit_session_user_message",
      "actor_role" => "author",
      "input_sha256" => AUTHORITY_HASHES.fetch("BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt")
    }],
    "display_order" => {
      "mode" => "source_traceability",
      "item_ids" => items.map { |item| item.fetch("item_id") },
      "author_event_id" => event_id
    },
    "author_adjudications" => items.map do |item|
      {
        "item_id" => item.fetch("item_id"),
        "author_event_id" => event_id,
        "author_triage" => "will_address",
        "authorized_targets" => item.fetch("proposed_targets"),
        "claim_strength_authorizations" => []
      }
    end,
    "collateral_authorizations" => []
  }
  write_json(paths[:choices], object)
  object
end

def p30_texts(reader_manifest_sha)
  replacements = {
    "B0059" => <<~'TEX',
      The executed evidence synthesis remains bounded to the frozen 68 captured
      manifestations, 52 unique screened records, 26 admitted records, and 24
      peer-reviewed-journal records.  A dated replay on 3 September 2026 ran all
      54 exact frozen query strings through the Crossref REST
      \texttt{query.bibliographic} interface with one top-ranked metadata record
      returned per query.  The row-level ledger records the query, retrieval time,
      interface, HTTP status, candidate DOI and title, inventory match, screening
      decision, and reason for every replay row.  It retained only candidates that
      matched the frozen admitted inventory by DOI or normalized title; every other
      top record was screened out as outside the frozen scope.  This replay is a new,
      fully enumerated retrieval event.  The unavailable excluded rows from the
      original synthesis session remain unavailable and are not reconstructed as
      historical observations.
    TEX
    "B0060" => <<~'TEX',
      Correction provenance is independently citable in the versioned Stage-4-prime
      bibliography.  P30-S01 and P30-S02 are bound to the published correction
      DOI \url{https://doi.org/10.1063/1.457669} \citep{P30-C01}; P30-S03 is bound
      to DOI \url{https://doi.org/10.1063/1.457670} \citep{P30-C02}.  The existing
      P30-S17/P30-S18 pairing remains unchanged for its affected Section-7 boundary.
      These record-level bindings correct publication provenance only; they do not
      finalize a theorem passage or license any project-specific physical-roof or
      determinant claim.  The canonical bibliography is frozen, and the two entries
      occur only in the notes-side versioned bibliography used for this revision preview.
    TEX
    "B0061" => <<~'TEX',
      Each admitted source was encoded in a source-effect matrix with thematic role,
      claim fitness, admissible use, prohibited transfer, correction applicability,
      and locator limitation.  Four role-separated assessments---editorial, domain,
      methodology, and adversarial---were performed in fresh contexts within the same
      model family before author adjudication.  They are therefore distinct
      fresh-context checks, not independent replications.  This reader-facing method
      classifies and synthesizes evidence only; it creates no scientific artifact,
      experiment, determinant, enclosure, or result.
    TEX
    "B0062" => <<~'TEX',
      The claim-to-passage matrix has 28 rows: one for each of P30-S01--P30-S26 and
      one record-level row for each correction P30-C01 and P30-C02.  All 26
      paper-specific source rows retain \texttt{anchor:none} and
      \texttt{INCONCLUSIVE} passage support; source identity, DOI resolution, metadata
      checks, and role coding do not establish theorem-to-claim transfer.  The two
      correction rows are finalized only at publication-record level and bind the
      affected source IDs; they add no formula or theorem locator.  No direct quotation
      is used.  Retraction status remains \texttt{NOT_CHECKED}, and source-level
      conflict-of-interest status remains \texttt{UNKNOWN_NOT_AUDITED}.
    TEX
    "B0064" => <<~'TEX',
      The evidence transformation follows the registered claim plan rather than
      searching for a stronger narrative.  Each claim carries a frozen source set
      and a negative constraint.  Physical-scattering sources can motivate geometry
      and coding only within their correction bindings.  Symbolic-flow and operator
      sources supply conditional components only under their own hypotheses.
      Determinant and numerical-analysis sources describe what an eligible
      approximation would require but cannot establish eligibility for an undefined
      operator.  Cohomology sources license only directional reasoning after an exact
      theorem-to-object map.  These roles remain separate rather than being merged
      into a synthetic theorem.
    TEX
    "B0067" => <<~'TEX',
      \section{Certificate Method Architecture}
    TEX
    "B0084" => <<~'TEX',
      Gate~5 freezes one primary roof and three deterministic controls on a single
      callable interface.  Scale is fixed by (a=1), so the primary geometry is
      (d=6) and (\rho_{\rm phys}=\tau_6).  The unit control is
      (\rho_{\rm unit}=1).  Let (phi) be the order-three cyclic disk-label map
      (1\mapsto2\mapsto3\mapsto1); it preserves the no-repeat adjacency rule and,
      for the equilateral geometry, defines the symmetry control
      (\rho_{\rm sym}=\rho_{\rm phys}\circ\phi).  The neighboring control uses
      the exact rational perturbation (delta=1/10), hence
      (d=6+\delta=61/10) and (\rho_{\rm near}=\tau_{61/10}).  Its geometry must
      independently satisfy the no-eclipse precondition.  Comparisons are restricted to
      [
        \Omega=\{s:1/2\leq\operatorname{Re}s\leq2,
        \ |\operatorname{Im}s|\leq50\},\qquad \eta_c=1/100.
      ]
      For each control (c), a future Gate-4 joint enclosure
      ([L_c,U_c]) for
      (Delta_c=\sup_{s\in\Omega}|D_{\rm phys}(s)-D_c(s)|) yields
      \path{SEPARATED} when (L_c>\eta_c), \path{NOT_SEPARATED} when
      (U_c\leq\eta_c), and \path{INDETERMINATE} otherwise.

      \begin{center}
      \small
      \begin{tabularx}{\linewidth}{@{}lXXX@{}}
      \toprule
      Surface & Preserved & Broken or changed & Admissible interpretation \\
      \midrule
      Primary (d=6) & geometry, coding, owners, physical timing & none & registered baseline only \\
      Unit (c_0=1) & coding and owner policy & pointwise flight-time variation and geometry-derived timing & tests dependence on a nonconstant roof, not geometric fidelity \\
      Cyclic (phi) & equilateral geometry, adjacency, owner relation, roof values up to relabeling & no physical property; labels are permuted & symmetry/invariance control for label equivariance \\
      Neighbor (d=61/10) & disk type, symbolic adjacency when no-eclipse holds, owner policy & exact primary geometry and flight times & local geometry-sensitivity control, not an extrapolation theorem \\
      \bottomrule
      \end{tabularx}
      \end{center}
      No control comparison or numerical enclosure has been executed.
    TEX
    "B0088" => <<~'TEX',
      The certificate is a directed acyclic graph with the following complete
      reader-facing gate map.  A hash field always binds both the typed inputs and the
      emitted output; a missing permission or prerequisite stops the gate and every
      listed downstream consumer.

      \begin{center}
      \scriptsize
      \begin{tabularx}{\linewidth}{@{}l p{.19\linewidth} p{.27\linewidth} X@{}}
      \toprule
      Gate & Inputs & Output, receipt, and hash & Uncertainty, consumer, permission/stop \\
      \midrule
      1 & frozen geometry and owner policy & pointwise-roof and orbit-owner ledger; G1 receipt; input/output SHA-256 & geometry/roof-input; G2--G5; construct only from frozen geometry, otherwise stop \\
      2 & G1 output and function-space specification & operator specification and theorem-hypothesis map; G2 receipt; input/output SHA-256 & hypothesis/applicability; G3--G5; require exact theorem map, otherwise stop \\
      3 & G1--G2 outputs and normalization & common coefficient-correspondence ledger; G3 receipt; input/output SHA-256 & coefficient/repetition convention; G4--G5; require one typed coefficient theorem, otherwise stop \\
      4 & G1--G3 plus five channel records & domain-specific joint enclosure; G4 receipt; input/output SHA-256 & geometry/roof, orbit tail, projection, evaluation, roundoff; G5; require common norm, propagation, dependence, and conditioning, otherwise stop \\
      5 & G1--G4 plus frozen controls and thresholds & physical-versus-control comparison; G5 receipt; input/output SHA-256 & propagated joint enclosure; registered physical interpretation; require all controls evaluable, otherwise stop \\
      6 & separately registered roof pair and theorem map & typed directional nontransfer decision; G6 receipt; input/output SHA-256 & theorem applicability and witness; nontransfer consumer only; require separate activation, otherwise \texttt{NOT_ACTIVATED} \\
      \bottomrule
      \end{tabularx}
      \end{center}
      The closed state vocabulary is \texttt{NOT_STARTED},
      \texttt{PREREQUISITE_BLOCKED}, \texttt{EVALUABLE}, \texttt{PASSED},
      \texttt{FAILED}, and \texttt{NOT_EVALUABLE}; Gate~6 additionally admits
      \texttt{NOT_ACTIVATED}.  Prose cannot promote a state.
    TEX
    "B0090" => <<~'TEX',
      Gates~1--5 are currently \texttt{NOT_STARTED}; none is
      \texttt{EVALUABLE}, \texttt{PASSED}, or \texttt{FAILED}.  Gate~6 is
      \texttt{NOT_ACTIVATED}, because no separate roof-pair registration and theorem
      map exists.  After execution begins, an unmet predecessor yields
      \texttt{PREREQUISITE_BLOCKED}; complete typed inputs yield
      \texttt{EVALUABLE}; validation then yields \texttt{PASSED},
      \texttt{FAILED}, or \texttt{NOT_EVALUABLE} according to the gate contract.
      The first nonpassing mandatory gate prohibits every downstream
      physical-determinant claim.  This status report is architectural and promotes
      no gate.
    TEX
    "B0098" => <<~'TEX',
      Reader-auditable Stage-4-prime materials are enumerated in
      \path{notes/stage4_prime_reader_artifact_manifest_round2.json} (SHA-256
      \texttt{__READER_SHA__}).  Every retained entry carries a schema or format,
      byte length, full SHA-256 digest, and repository-relative access state.  The
      branch-relative locator is
      \url{https://github.com/maris205/hilbert-polya-structure/tree/main/flow_systems/papers/30-three-disk-nonconstant-roof-determinant}.
      It is not a content-addressed or persistent archival release.  The manifest
      supports only the bounded search replay, screening decisions, correction
      metadata, and source-role matrix; it lists no scientific result package.
    TEX
    "B0100" => <<~'TEX',
      A fresh verifier would check hashes, types, completeness, precision ladders,
      and stop states under prospectively frozen rules.  Role-separated evidence
      synthesis and the dated literature replay check provenance and declared
      boundaries only.  No serializer, proof object, scientific implementation,
      determinant, or replay receipt for Gates~1--6 is claimed to exist.
    TEX
    "B0103" => <<~'TEX',
      The frozen controls have distinct interpretations.  The unit roof preserves
      coding and owner policy while removing pointwise temporal variation; it can
      diagnose dependence on a nonconstant roof but not geometric fidelity.  The
      order-three cyclic label map is a symmetry/invariance control: it preserves
      equilateral geometry, adjacency, and roof information up to relabeling, so it
      tests label equivariance rather than placement sensitivity.  The neighboring
      (d=61/10) roof changes the exact geometry while preserving the registered
      symbolic interface only if no-eclipse is separately certified; it can test local
      geometry sensitivity but cannot alter or extrapolate from the primary (d=6)
      system.  All use the fixed (Omega), (eta_c=1/100), joint enclosure, and
      three-way decision rule stated above.  No comparison or enclosure has been
      executed, and the controls create no Route-A or Route-B credit.
    TEX
    "B0106" => <<~'TEX',
      The 28-row matrix retains \texttt{INCONCLUSIVE} theorem-passage support for
      P30-S01--P30-S26 and finalizes only the publication records for P30-C01 and
      P30-C02.  P30-S01/P30-S02 are bound to \citep{P30-C01}, P30-S03 is bound to
      \citep{P30-C02}, and P30-S17/P30-S18 remain paired for affected use.  The two
      new bibliography records therefore close the publication-level correction
      citation gap, but no formula, theorem, section, paragraph, or quotation is
      cleared for project-specific transfer.  Retraction status remains unchecked,
      and source-level conflicts remain unaudited.
    TEX
    "B0123" => <<~'TEX'
      \section*{Data and Materials Availability}
      The bounded Stage-4-prime evidence files, their schema or format versions,
      byte lengths, full SHA-256 digests, and repository-relative access states are
      listed in \path{notes/stage4_prime_reader_artifact_manifest_round2.json}
      (SHA-256 \texttt{__READER_SHA__}).  The listed branch-relative repository path
      is not a persistent archive.  The notes-side versioned bibliography contains
      independently citable P30-C01 and P30-C02 correction records; the canonical
      bibliography remains frozen.  Original-session excluded rows and theorem-level
      passage adjudications remain unavailable.  No collision data, owner ledger,
      pointwise roof, operator artifact, determinant value, error bound, control
      comparison, cohomological witness, or experiment was generated in this revision.
    TEX
  }
  # Reassert the two mathematical control blocks through a neutral placeholder.
  # This makes every intended TeX backslash explicit and prevents host-language
  # escape processing from turning \rho into a carriage return or stripping math
  # delimiters during source transport.
  replacements["B0084"] = <<~'TEX'.tr("§", 92.chr)
    Gate~5 freezes one primary roof and three deterministic controls on a single
    callable interface.  Scale is fixed by §(a=1§), so the primary geometry is
    §(d=6§) and §(§rho_{§rm phys}=§tau_6§).  The unit control is
    §(§rho_{§rm unit}=1§).  Let §(§phi§) be the order-three cyclic disk-label map
    §(1§mapsto2§mapsto3§mapsto1§); it preserves the no-repeat adjacency rule and,
    for the equilateral geometry, defines the symmetry control
    §(§rho_{§rm sym}=§rho_{§rm phys}§circ§phi§).  The neighboring control uses
    the exact rational perturbation §(§delta=1/10§), hence
    §(d=6+§delta=61/10§) and §(§rho_{§rm near}=§tau_{61/10}§).  Its geometry must
    independently satisfy the no-eclipse precondition.  Comparisons are restricted to
    §[
      §Omega=§{s:1/2§leq§operatorname{Re}s§leq2,
      § |§operatorname{Im}s|§leq50§},§qquad §eta_c=1/100.
    §]
    For each control §(c§), a future Gate-4 joint enclosure
    §([L_c,U_c]§) for
    §(§Delta_c=§sup_{s§in§Omega}|D_{§rm phys}(s)-D_c(s)|§) yields
    §path{SEPARATED} when §(L_c>§eta_c§), §path{NOT_SEPARATED} when
    §(U_c§leq§eta_c§), and §path{INDETERMINATE} otherwise.

    §begin{center}
    §small
    §begin{tabularx}{§linewidth}{@{}lXXX@{}}
    §toprule
    Surface & Preserved & Broken or changed & Admissible interpretation §§
    §midrule
    Primary §(d=6§) & geometry, coding, owners, physical timing & none & registered baseline only §§
    Unit §(c_0=1§) & coding and owner policy & pointwise flight-time variation and geometry-derived timing & tests dependence on a nonconstant roof, not geometric fidelity §§
    Cyclic §(§phi§) & equilateral geometry, adjacency, owner relation, roof values up to relabeling & no physical property; labels are permuted & symmetry/invariance control for label equivariance §§
    Neighbor §(d=61/10§) & disk type, symbolic adjacency when no-eclipse holds, owner policy & exact primary geometry and flight times & local geometry-sensitivity control, not an extrapolation theorem §§
    §bottomrule
    §end{tabularx}
    §end{center}
    No control comparison or numerical enclosure has been executed.
  TEX
  replacements["B0103"] = <<~'TEX'.tr("§", 92.chr)
    The frozen controls have distinct interpretations.  The unit roof preserves
    coding and owner policy while removing pointwise temporal variation; it can
    diagnose dependence on a nonconstant roof but not geometric fidelity.  The
    order-three cyclic label map is a symmetry/invariance control: it preserves
    equilateral geometry, adjacency, and roof information up to relabeling, so it
    tests label equivariance rather than placement sensitivity.  The neighboring
    §(d=61/10§) roof changes the exact geometry while preserving the registered
    symbolic interface only if no-eclipse is separately certified; it can test local
    geometry sensitivity but cannot alter or extrapolate from the primary §(d=6§)
    system.  All use the fixed §(§Omega§), §(§eta_c=1/100§), joint enclosure, and
    three-way decision rule stated above.  No comparison or enclosure has been
    executed, and the controls create no Route-A or Route-B credit.
  TEX

  texttt_open = 92.chr + "texttt{"
  texttt_pattern = Regexp.new(Regexp.escape(texttt_open) + "([^}]*)}")
  # Keep literal identifiers and digests byte-readable while giving TeX legal
  # discretionary breakpoints.  The printed identifier/hash bytes are unchanged.
  # This is confined to the already-authorized replacement blocks.
  allowbreak = 92.chr + "allowbreak "
  escaped_underscore = 92.chr + "_"
  readable_reader_sha = reader_manifest_sha.scan(/.{1,16}/).join(allowbreak)
  replacements.transform_values do |text|
    rebound = text.gsub("__READER_SHA__", readable_reader_sha)
    rebound.gsub(texttt_pattern) do
      inner = Regexp.last_match(1)
      escaped = +""
      previous = nil
      inner.each_char do |character|
        escaped << 92.chr if character == "_" && previous != 92.chr
        escaped << character
        previous = character
      end
      escaped = escaped.gsub(escaped_underscore, escaped_underscore + allowbreak)
      texttt_open + escaped + "}"
    end
  end
end

def p31_texts(reader_manifest_sha)
  replacements = {
    "B0012" => <<~'TEX',
      The finite input is unchanged: 138 instances are distributed over 55
      source-word/prime groups.  The inherited \texttt{2/2/134} split and the three
      55-group summaries remain instance- or group-level controls, not owner counts.
      The proposed owner is an oriented primitive conjugacy class in
      \texttt{Gamma\_0(11)} represented by a positive-trace determinant-one lift.  The
      inverse policy has three typed branches.  A certified self-reciprocal owner keeps
      one \texttt{owner\_bytes} value and records
      \texttt{inverse\_relation=self\_reciprocal} with its subgroup witness.  A
      certified non-self-reciprocal pair keeps two oriented owner values linked by
      \texttt{inverse\_relation=inverse\_separated}.  If neither proposition is
      certified, \texttt{delta} returns an unresolved inverse disposition.  Trace,
      length, homology, or another filter cannot choose among these branches by itself.
    TEX
    "B0015" => <<~'TEX',
      The primary target is a canonicalization biconditional, not 9,453 independently
      foundational negative certificates.  The all-pairs expansion is derived from the
      prospective byte partition and can replay sorting, collision, binding,
      inverse-label, traversal-metadata, and other bookkeeping consequences.  It is not
      an independent semantic truth source.  Reflexivity belongs to self fixtures,
      direction sensitivity to ordered reversal fixtures, and transitivity to explicit
      triples.  Detecting a semantic false merge or split requires a separately bound,
      target-blind adjudicator; no such route was executed or recorded here.
    TEX
    "B0016" => <<~'TEX',
      The closest-work comparison now separates four method families.  Finite-index
      subgroup descriptions and computable Fuchsian domains provide representation and
      reduction ingredients (P31-S01--P31-S06).  Ambient, arithmetic, and hyperbolic
      conjugacy methods provide decision ingredients that still require an exact
      \texttt{Gamma\_0(11)} specialization (P31-S07--P31-S20).  Proof-carrying code
      supplies the general producer-evidence/simple-checker pattern \citep{P31-S23},
      while tamper-evident logging supplies append-only membership and consistency
      proof patterns \citep{P31-S24}.  Aggregate class-counting neighbors remain
      post-closure controls (P31-S21--P31-S22).  The project synthesis combines these
      inherited components into a resolved-domain canonicalizer specification, a total
      disposition, a derived regression audit, and distinct \texttt{G/I/C}
      projections.  It is not a new conjugacy theorem, an implemented solver, a
      priority claim, or an exhaustive novelty claim.
    TEX
    "B0033" => <<~'TEX',
      Proof-carrying code places a proof next to untrusted producer output so that a
      simpler consumer can check an explicit safety policy \citep{P31-S23}; P31 borrows
      only that evidence-carrying separation.  Tamper-evident history trees support
      compact membership and append-only consistency checks \citep{P31-S24}; P31
      borrows only the ledger-verification pattern.  Neither source supplies the
      subgroup-conjugacy theorem, canonical owner bytes, inverse policy, or complete
      negative certificate needed here.  Their role is component positioning, not
      evidence of priority or of a completed P31 method.
    TEX
    "B0036" => <<~'TEX',
      The executed research method remains literature synthesis over frozen artifacts.
      The upstream corpus captured 44 manifestations, removed nine duplicates, screened
      35 unique records, excluded 13, and retained 22 sources.  A dated replay on
      3 September 2026 submitted all 20 exact frozen query strings to Crossref
      \texttt{query.bibliographic}, bounded to one top-ranked metadata record per query.
      The row-level supplement records each query, timestamp, interface, HTTP status,
      candidate identity, inventory match, decision, and reason.  It is a new replay,
      not a reconstruction of the unavailable original-session exclusion rows.  A
      separate bounded closest-work search verified exactly two method records and
      added them only to the notes-side versioned bibliography.
    TEX
    "B0037" => <<~'TEX',
      The method-component matrix has 24 rows: P31-S01--P31-S22 retain
      \texttt{anchor:none} and \texttt{INCONCLUSIVE} theorem-passage transfer, while
      P31-S23 and P31-S24 have finalized publisher-level method locators for the narrow
      proof-carrying and tamper-evident patterns cited here.  Every row states the
      component or claim role, passage status, applicable hypothesis or scope, and a
      prohibited transfer.  Metadata closure does not promote the 22 unresolved rows,
      and the two new method rows do not establish any P31 owner theorem, implementation,
      or semantic adjudicator.  No direct quotation is used.
    TEX
    "B0038" => <<~'TEX',
      The synthesis uses source-effect discipline rather than vote counting.  A source
      may support subgroup representation, ambient reduction, proof-carrying checking,
      or append-only ledger verification while being explicitly excluded from proving
      the composite P31 owner contract.  Venue recognition and algorithmic proximity do
      not erase hypothesis, object, or output-type boundaries.  The method-passage
      matrix records those permitted components and forbidden transfers row by row;
      missing theorem-to-certificate links remain visible obligations.
    TEX
    "B0039" => <<~'TEX',
      Citation closure is checked against the notes-side versioned bibliography: all
      24 cited source identifiers resolve to one entry, including source-verified
      P31-S23 and P31-S24.  The canonical bibliography is unchanged.  This structural
      check does not validate a theorem passage.  P31-S01--P31-S22 retain
      \texttt{anchor:none} and \texttt{INCONCLUSIVE} claim-to-passage status; only the
      narrow method descriptions for P31-S23/P31-S24 use their finalized publisher-level
      locators.  The wording remains limited to inherited components, prospective use,
      and explicit exclusions.
    TEX
    "B0046" => <<~'TEX',
      \begin{verbatim}
      OwnerDisposition = Resolved(owner_bytes, witnesses)
                       | Unresolved(code, evidence)
      delta: X -> OwnerDisposition
      X_res = {x in X: delta(x) is Resolved}
      kappa: X_res -> OwnerBytes
      Closed = (X_res = X)
      \end{verbatim}
      Thus \texttt{delta} is total even when it returns a typed unresolved disposition;
      \texttt{kappa} is defined only on the resolved domain.  A total owner map on all
      of \texttt{X} exists only after the separately checked condition
      \texttt{Closed} holds.
    TEX
    "B0049" => <<~'TEX',
      The inverse rule is branch-complete but remains prospective.  If an exact
      \texttt{Gamma\_0(11)} witness certifies that an oriented primitive owner is
      conjugate to its inverse, one canonical value is retained and the certificate
      records \texttt{inverse\_relation=self\_reciprocal}, the conjugator, presentation
      version, and replay trace.  If a lawful obstruction certifies nonconjugacy, two
      oriented values are retained and linked as \texttt{inverse\_separated}.  If
      neither witness exists, \texttt{delta} returns
      \path{UNRESOLVED_INVERSE_RELATION}; it must not choose two owners merely from a
      convention.  This typed branch does not assert an exclusion lemma or report that
      any frozen instance is self-reciprocal.
    TEX
    "B0050" => <<~'TEX',
      On the resolved domain, the certificate invariant is
      \[
        \forall x,y\in X_{\rm res},\qquad
        \kappa(x)=\kappa(y)\ \Longleftrightarrow\
        x\text{ and }y\text{ represent the same oriented primitive owner}.
      \]
      Soundness, completeness, and determinism are therefore claims about
      \texttt{kappa:X\_res->OwnerBytes}.  They become a total-owner theorem for the
      frozen population only after the independent closure condition
      \texttt{X\_res=X}.  Before closure, byte equality can induce a partition of the
      resolved subset but cannot certify a complete partition of \texttt{X}.
    TEX
    "B0051" => <<~'TEX',
      The branches have distinct failure modes.  Soundness fails if distinct resolved
      oriented owners share bytes; completeness fails if one resolved owner receives
      different bytes; and determinism fails if a resolved input can receive different
      bytes under permitted executions.  \texttt{delta} itself remains total because
      it may emit a typed \texttt{Unresolved} value.  Global owner-map closure fails
      whenever \texttt{X\_res} is a proper subset of \texttt{X}; in that state
      \texttt{kappa} is not total on \texttt{X}, the all-population biconditional is not
      available, and complete \texttt{G/I/C} materialization is prohibited.
    TEX
    "B0054" => <<~'TEX',
      Each future per-instance certificate binds the immutable input identifier and
      hash; subgroup presentation and theorem version; exact membership evidence;
      normalized matrix or word; maximal primitive root and traversal exponent;
      orientation convention; canonical owner bytes; and the proof or reduction trace
      for a read-only verifier.  It also carries
      \texttt{inverse\_relation} in
      \{\texttt{self\_reciprocal}, \texttt{inverse\_separated},
      \texttt{unresolved}\}, with the matching subgroup conjugator, obstruction, or
      unresolved evidence.  A failure record identifies the exact failed precondition
      or theorem obligation; a timeout never becomes nonconjugacy.
    TEX
    "B0061" => <<~'TEX',
      For \texttt{|X|=138}, the 9,453 unordered distinct-pair rows are generated from
      the same prospective canonical-byte partition.  They can replay byte equality,
      sorting, binding, inverse labels, traversal metadata, and bookkeeping
      consequences.  They cannot test reflexivity, ordered reversal, or three-input
      closure, and they cannot detect semantic false merges, false splits, or
      nontransitivity without expected dispositions from a separately bound,
      target-blind adjudicator.  No such independent semantic route exists in the
      recorded project, so the optional direct-solver field remains \texttt{ABSENT}
      and the all-pairs surface is not a truth source.
    TEX
    "B0062" => <<~'TEX',
      Prospective coverage is separated by fixture type.  Self fixtures
      \texttt{F\_self=\{(x,x)\}} test reflexive handling; ordered reversal pairs test
      direction-sensitive serialization; triples \texttt{(x,y,z)} test closure and
      transitivity consequences; and separately sourced disagreement rows would
      compare canonical bytes with a target-blind semantic adjudicator.  The 9,453
      unordered distinct pairs cover none of the first three fixture shapes by
      construction and have no independent expected semantic labels.  They are limited
      to byte and bookkeeping checks.  No fixture set or direct route was executed.
    TEX
    "B0067" => <<~'TEX',
      The downstream relations are conditional on the total disposition
      \texttt{delta}.  Complete \texttt{G/I/C} materialization requires
      \texttt{X\_res=X}.  Until then, unresolved rows enter only
      \texttt{I\_diag}, contribute to no estimand, and prevent \texttt{G},
      \texttt{I}, or \texttt{C} from being published as complete.  Once closure holds,
      \texttt{I} contains exactly 138 provenance-preserving input rows;
      \texttt{G} is its distinct owner projection; and \texttt{C} is its distinct
      cell-owner projection.  The consolidated schema below is the checkable contract;
      the surrounding prose supplies interpretation only.
    TEX
    "B0072" => <<~'TEX',
      \begin{center}
      \scriptsize
      \begin{tabular}{@{}p{.10\linewidth}p{.20\linewidth}p{.10\linewidth}p{.18\linewidth}p{.30\linewidth}@{}}
      \toprule
      Relation & Key & Closed cardinality & Materialization gate & Provenance and allowed direction \\
      \midrule
      \texttt{G} & \texttt{owner\_bytes} & distinct resolved owners & \texttt{X\_res=X} & derived from complete \texttt{I}; cannot reconstruct input occurrences \\
      \texttt{I} & \texttt{input\_id}, foreign key to \texttt{G} & 138 & \texttt{X\_res=X} & retains input, cell, traversal, Hecke, hash, and disposition provenance; may project to \texttt{G} and \texttt{C} \\
      \texttt{C} & \texttt{(cell\_key,owner\_bytes)} & distinct complete-\texttt{I} cell-owner pairs & \texttt{X\_res=X} & derived from complete \texttt{I}; cannot reconstruct input occurrences \\
      \texttt{I\_diag} & \texttt{input\_id} & all unresolved diagnostics & any unresolved row & diagnostic only; no projection into complete estimands \\
      \bottomrule
      \end{tabular}
      \end{center}
      Therefore the only allowed construction direction is complete
      \texttt{I -> G,C}; neither \texttt{G} nor \texttt{C}, separately or jointly,
      may be used to reconstruct \texttt{I}.  The three published estimands retain
      separate schemas and validation rules.
    TEX
    "B0079" => <<~'TEX',
      \begingroup\sloppy
      Reader-accessible Stage-4-prime materials are exactly the entries listed in
      \path{notes/stage4_prime_reader_artifact_manifest_round2.json} (SHA-256
      \texttt{__READER_SHA__}).  Each row names its schema or format version, byte
      length, full SHA-256 digest, and repository-relative access state.  The
      branch-relative locator is
      \url{https://github.com/maris205/hilbert-polya-structure/tree/main/flow_systems/papers/31-level11-conjugacy-owner-ledger};
      it is not a content-addressed or persistent archive.  Recovery claims are made
      only for listed entries.  Generative prose is not promised byte-reproducible,
      and no owner ledger or scientific result package is listed.
      \par\endgroup
    TEX
    "B0089" => <<~'TEX',
      The dated supplement exposes one screening decision for each of the 20 frozen
      query strings, but it is a new bounded Crossref replay and not a reconstruction
      of the unavailable original-session excluded rows.  The 24-row method-passage
      matrix preserves \texttt{INCONCLUSIVE} theorem transfer for P31-S01--P31-S22
      and finalizes only the narrow publisher-level method locators for P31-S23 and
      P31-S24.  Those two records position proof-carrying and tamper-evident components;
      they do not provide a \texttt{Gamma\_0(11)} owner theorem, solver, inverse witness,
      or semantic adjudicator.  Retraction and source-conflict screening were not
      expanded by this revision.
    TEX
    "B0105" => <<~'TEX'
      \paragraph{Data and materials availability.}\begingroup\sloppy
      The bounded reader-accessible files
      are enumerated in
      \path{notes/stage4_prime_reader_artifact_manifest_round2.json} (SHA-256
      \texttt{__READER_SHA__}), with a schema or format, byte length, full digest, and
      repository-relative access state for every entry.  The notes-side versioned
      bibliography includes source-verified P31-S23 and P31-S24; the canonical
      bibliography remains frozen.  The branch-relative repository locator is not a
      persistent archival identifier, and materials outside the manifest are not
      described as reader-recoverable.  No owner ledger, scientific dataset, solver
      output, pair-decision table, or \texttt{G/I/C} result was generated.
      \par\endgroup
    TEX
  }
  allowbreak = 92.chr + "allowbreak{}"
  readable_reader_sha = reader_manifest_sha.scan(/.{1,16}/).join(allowbreak)
  replacements.transform_values { |text| text.gsub("__READER_SHA__", readable_reader_sha) }
end

def run!(*command)
  puts "+ #{command.join(" ")}"
  success = system(*command)
  raise "command failed: #{command.join(" ")}" unless success
end

def build_adjudication!(paths)
  run!(
    "python", ROADMAP_CLI.to_s, "validate-roadmap", paths[:roadmap].to_s,
    "--base", paths[:base].to_s,
    "--block-manifest", paths[:manifest].to_s
  )
  unless File.file?(paths[:adjudication])
    run!(
      "python", ROADMAP_CLI.to_s, "build-adjudication", paths[:roadmap].to_s,
      "--base", paths[:base].to_s,
      "--block-manifest", paths[:manifest].to_s,
      "--claim-surface", paths[:claim_manifest].to_s,
      "--author-choices", paths[:choices].to_s,
      "--artifact-root", paths[:root].to_s,
      "--output", paths[:adjudication].to_s
    )
  end
  run!(
    "python", ROADMAP_CLI.to_s, "validate-adjudication", paths[:roadmap].to_s, paths[:adjudication].to_s,
    "--base", paths[:base].to_s,
    "--block-manifest", paths[:manifest].to_s,
    "--claim-surface", paths[:claim_manifest].to_s,
    "--artifact-root", paths[:root].to_s
  )
end

def build_patch(request, paper_id, config, paths, texts, insert_blocks)
  manifest = JSON.parse(File.read(paths[:manifest]))
  old_hashes = manifest.fetch("blocks").to_h { |block| [block.fetch("block_id"), block.fetch("old_hash")] }
  requested_items = request_paper(request, paper_id).fetch("items")
  item_by_id = requested_items.to_h { |item| [item.fetch("item_id"), item] }
  adjudication = JSON.parse(File.read(paths[:adjudication]))
  operations = texts.keys.sort_by { |id| id.delete_prefix("B").to_i }.map do |block_id|
    operation = insert_blocks.include?(block_id) ? "insert_after" : "replace_block"
    item_ids = item_by_id.values.filter_map do |item|
      target = item.fetch("proposed_targets").find { |entry| entry.fetch("block_id") == block_id }
      item.fetch("item_id") if target && target.fetch("allowed_operations").include?(operation)
    end
    raise "no exact authority for #{paper_id} #{operation} #{block_id}" if item_ids.empty?
    {
      "op" => operation,
      "block_id" => block_id,
      "old_hash" => old_hashes.fetch(block_id),
      "new_text" => texts.fetch(block_id).rstrip,
      "roadmap_item_ids" => item_ids,
      "claim_strength_changes" => [],
      "collateral_authorization_ids" => []
    }
  end
  covered_items = operations.flat_map { |op| op.fetch("roadmap_item_ids") }.uniq
  missing = item_by_id.keys - covered_items
  raise "patch fails to cover items #{missing.join(",")}" unless missing.empty?
  patch = {
    "patch_format_version" => "1.1",
    "authorization_context" => "review_roadmap",
    "revision_round" => 2,
    "base_draft_hash" => config[:base_sha][0, 12],
    "roadmap_sha256" => sha(paths[:roadmap]),
    "author_adjudication_sha256" => sha(paths[:adjudication]),
    "author_decision_digest" => author_decision_digest(adjudication),
    "claim_surface_manifest_sha256" => sha(paths[:claim_manifest]),
    "ops" => operations,
    "emitted_by" => "draft_writer_agent"
  }
  write_json(paths[:patch], patch)
  patch
end

def build_writer_handoff(paper_id, paths, patch)
  object = {
    "schema_version" => "round10-stage4-prime-writer-handoff/1.0",
    "paper_id" => paper_id,
    "revision_round" => 2,
    "generated_at_utc" => TIMESTAMP,
    "authority" => AUTHORITY_HASHES.map { |path, digest| {"path" => "../../../#{path}", "sha256" => digest} },
    "base_draft" => {"path" => "notes/#{paths[:base].basename}", "sha256" => sha(paths[:base])},
    "block_manifest" => {"path" => "notes/#{paths[:manifest].basename}", "sha256" => sha(paths[:manifest])},
    "roadmap" => {"path" => "notes/#{paths[:roadmap].basename}", "sha256" => sha(paths[:roadmap])},
    "claim_surface_manifest" => {"path" => "notes/#{paths[:claim_manifest].basename}", "sha256" => sha(paths[:claim_manifest]), "surfaces" => 0},
    "author_adjudication" => {"path" => "notes/#{paths[:adjudication].basename}", "sha256" => sha(paths[:adjudication])},
    "reader_artifact_manifest" => {"path" => "notes/#{paths[:reader_manifest].basename}", "sha256" => sha(paths[:reader_manifest])},
    "patch" => {"path" => "notes/#{paths[:patch].basename}", "sha256" => sha(paths[:patch]), "ops" => patch.fetch("ops").length},
    "boundaries" => {
      "canonical_manuscript_bibliography_pdf_frozen" => true,
      "versioned_notes_bibliography_only" => true,
      "scientific_execution" => false,
      "canonical_result_refresh" => false,
      "registered_claim_replacements" => 0,
      "stage4_5_or_later" => false,
      "route_state_change" => false
    }
  }
  write_json(paths[:notes] / "stage4_prime_writer_handoff.json", object)
end

verify_frozen_inputs!
request = JSON.parse(File.read(ROOT / "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json"))
paths30 = paper_paths(PAPERS.fetch("P30"))
paths31 = paper_paths(PAPERS.fetch("P31"))

append_versioned_bibliographies(paths30, paths31)
p30_verification, p31_verification = build_source_verification_receipts(paths30, paths31)
p30_ledger_json, p30_ledger_tsv, p30_ledger = build_replay_ledger("P30", paths30)
p31_ledger_json, p31_ledger_tsv, p31_ledger = build_replay_ledger("P31", paths31)

p30_passage_additions = [
  {
    "source_id" => "P30-C01", "component_or_claim_role" => "published correction record for P30-S01/P30-S02",
    "exact_passage_locator" => "DOI 10.1063/1.457669; Journal of Chemical Physics 91(5), 3279",
    "passage_status" => "FINALIZED", "hypothesis_or_scope" => "publication-level correction provenance only",
    "transfer_boundary" => "does not finalize a theorem or project-specific formula passage",
    "evidence_note" => "Crossref DOI metadata and AIP DOI resolution verified on 2026-09-04"
  },
  {
    "source_id" => "P30-C02", "component_or_claim_role" => "published correction record for P30-S03",
    "exact_passage_locator" => "DOI 10.1063/1.457670; Journal of Chemical Physics 91(5), 3280",
    "passage_status" => "FINALIZED", "hypothesis_or_scope" => "publication-level correction provenance only",
    "transfer_boundary" => "does not finalize a theorem or project-specific formula passage",
    "evidence_note" => "Crossref DOI metadata and AIP DOI resolution verified on 2026-09-04"
  }
]
p31_passage_additions = [
  {
    "source_id" => "P31-S23", "component_or_claim_role" => "producer-supplied proof checked by a simple consumer",
    "exact_passage_locator" => "ACM publisher abstract; DOI 10.1145/263699.263712",
    "passage_status" => "FINALIZED", "hypothesis_or_scope" => "proof-carrying code method pattern",
    "transfer_boundary" => "does not prove the P31 owner theorem or certificate completeness",
    "evidence_note" => "ACM/Crossref publication record verified on 2026-09-04"
  },
  {
    "source_id" => "P31-S24", "component_or_claim_role" => "tamper-evident membership and consistency proof pattern",
    "exact_passage_locator" => "USENIX Security 2009 official paper page and paper Sections 2--4",
    "passage_status" => "FINALIZED", "hypothesis_or_scope" => "append-only ledger verification pattern",
    "transfer_boundary" => "does not decide subgroup conjugacy or supply semantic owner labels",
    "evidence_note" => "USENIX official metadata and open paper verified on 2026-09-04"
  }
]
p30_matrix_json, p30_matrix_tsv, p30_matrix = build_passage_matrix("P30", paths30, p30_passage_additions)
p31_matrix_json, p31_matrix_tsv, p31_matrix = build_passage_matrix("P31", paths31, p31_passage_additions)

existing_artifacts = lambda do |paths|
  [
    [paths[:root] / "notes/stage1_phase2_annotated_bibliography.md", "Markdown/source synthesis note", "present_in_local_worktree; repository-relative locator declared"],
    [paths[:root] / "notes/stage1_phase2_source_inventory.tsv", "TSV/source inventory", "present_in_local_worktree; repository-relative locator declared"],
    [paths[:root] / "notes/stage1_phase2_source_verification.tsv", "TSV/source verification", "present_in_local_worktree; repository-relative locator declared"],
    [paths[:root] / "notes/stage1_phase3_literature_matrix.tsv", "TSV/source-effect matrix", "present_in_local_worktree; repository-relative locator declared"]
  ]
end
p30_manifest = build_reader_manifest("P30", paths30, existing_artifacts.call(paths30) + [
  [paths30[:raw_replay], "round10-stage4-prime-literature-replay-raw/1.0", "present_in_local_worktree; pending batch synchronization"],
  [p30_ledger_json, "round10-stage4-prime-literature-screening-ledger/1.0", "present_in_local_worktree; pending batch synchronization"],
  [p30_ledger_tsv, "TSV/row-level replay ledger", "present_in_local_worktree; pending batch synchronization"],
  [p30_matrix_json, "round10-stage4-prime-claim-passage-matrix/1.0", "present_in_local_worktree; pending batch synchronization"],
  [p30_matrix_tsv, "TSV/claim-passage matrix", "present_in_local_worktree; pending batch synchronization"],
  [p30_verification, "round10-stage4-prime-correction-source-verification/1.0", "present_in_local_worktree; pending batch synchronization"],
  [paths30[:versioned_bib], "BibTeX/notes-side Stage-4-prime build input", "present_in_local_worktree; pending batch synchronization"]
])
p31_manifest = build_reader_manifest("P31", paths31, existing_artifacts.call(paths31) + [
  [paths31[:raw_replay], "round10-stage4-prime-literature-replay-raw/1.0", "present_in_local_worktree; pending batch synchronization"],
  [p31_ledger_json, "round10-stage4-prime-literature-screening-ledger/1.0", "present_in_local_worktree; pending batch synchronization"],
  [p31_ledger_tsv, "TSV/row-level replay ledger", "present_in_local_worktree; pending batch synchronization"],
  [p31_matrix_json, "round10-stage4-prime-method-passage-matrix/1.0", "present_in_local_worktree; pending batch synchronization"],
  [p31_matrix_tsv, "TSV/method-passage matrix", "present_in_local_worktree; pending batch synchronization"],
  [p31_verification, "round10-stage4-prime-closest-work-source-verification/1.0", "present_in_local_worktree; pending batch synchronization"],
  [paths31[:versioned_bib], "BibTeX/notes-side Stage-4-prime build input", "present_in_local_worktree; pending batch synchronization"]
])

[["P30", paths30], ["P31", paths31]].each do |paper_id, paths|
  config = PAPERS.fetch(paper_id)
  roadmap = build_residual_roadmap(request, paper_id, config, paths)
  build_claim_manifest(paths, roadmap)
  build_author_choices(request, paper_id, paths)
  build_adjudication!(paths)
end

p30_patch = build_patch(request, "P30", PAPERS.fetch("P30"), paths30, p30_texts(sha(paths30[:reader_manifest])), [])
p31_patch = build_patch(request, "P31", PAPERS.fetch("P31"), paths31, p31_texts(sha(paths31[:reader_manifest])), %w[B0033 B0072])
build_writer_handoff("P30", paths30, p30_patch)
build_writer_handoff("P31", paths31, p31_patch)

verify_frozen_inputs!
summary = {
  "P30" => {"queries" => p30_ledger["row_count"], "passage_rows" => p30_matrix["row_count"], "patch_ops" => p30_patch["ops"].length},
  "P31" => {"queries" => p31_ledger["row_count"], "passage_rows" => p31_matrix["row_count"], "patch_ops" => p31_patch["ops"].length}
}
puts JSON.pretty_generate(summary)
