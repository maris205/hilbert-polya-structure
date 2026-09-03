#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"

ROOT = File.expand_path("..", __dir__)
SYNC_MARKER = "<!-- ROUND10_STAGE3_PRIME_ROUND3_STATUS_SYNC_20260903 -->"

PAPERS = {
  29 => {
    slug: "29-bianchi-ideal-owner-refinement",
    state: "stage3_prime_round3_major_revision_awaiting_stage4_prime_request_preparation_authorization",
    progress: "Gate M/Gate Q, exact inversion/conjugation laws, five fail-closed prospective interfaces, and deterministic failure precedence are explicit; no owner law, quotient, fixture run, score, or performance result exists.",
    system: "torsion-free level-(3) Gaussian Bianchi unit-speed geodesic flow; hyperbolic-arclength clock; primitive loxodromic inversion-paired owner; one literal nonzero Gaussian prime ideal",
    route: "Route A A0/A1 foundation/interface preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    main_trace_heading: "## Batch traceability",
    paper_route_heading: "## Claim and route boundary",
    paper_route_next_heading: nil,
    paper_current_insert_before: "## 结论概要"
  },
  30 => {
    slug: "30-three-disk-nonconstant-roof-determinant",
    state: "stage3_prime_round2_major_revision_stage4_prime_request_prepared_awaiting_exact_authorization",
    progress: "The physical-roof proposal is a six-gate fail-closed DAG with a common-norm uncertainty contract, four numerical channels, and separately propagated geometry/roof-input uncertainty; no roof, operator, determinant, enclosure, fidelity result, or nontransfer theorem exists.",
    system: "no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control",
    route: "A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    main_trace_heading: "## Batch traceability",
    paper_route_heading: "## Claim and route boundary",
    paper_route_next_heading: nil,
    paper_current_insert_before: "## 结论概要"
  },
  31 => {
    slug: "31-level11-conjugacy-owner-ledger",
    state: "stage3_prime_round2_major_revision_stage4_prime_request_prepared_awaiting_exact_authorization",
    progress: "The deterministic canonicalization biconditional is primary, the 9,453 pair dispositions are a derived audit, and G/I/C are distinct typed estimands; no owner partition, complete ledger, canonicalization theorem, or all-pairs execution exists.",
    system: "fixed positive time change of the Gamma_0(11) geodesic flow; oriented primitive owner; inverse separate; powers repetitions; Hecke degree distinct",
    route: "Route A A1-only owner/canonicalization preparation; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    main_trace_heading: "## Batch traceability",
    paper_route_heading: "## Claim and route boundary",
    paper_route_next_heading: nil,
    paper_current_insert_before: "## 结论概要"
  },
  32 => {
    slug: "32-homology-cover-renormalization-uniformity",
    state: "stage3_prime_round3_major_revision_awaiting_stage4_prime_request_preparation_authorization",
    progress: "Higher-content and zero-content factors remain the first falsification targets; the two modulus schedules, both iterated-limit orders, dependency table, and scalar-comparator interface are explicit, while every scientific object, majorant, limit, factor, or obstruction remains unexecuted or unproved.",
    system: "unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3",
    route: "generic Route A A1-A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    main_trace_heading: "## Traceability",
    paper_route_heading: "## Route position and next gate",
    paper_route_next_heading: "## Batch traceability",
    paper_current_insert_before: "## Stage 2.5 integrity result"
  },
  33 => {
    slug: "33-bolza-control-matched-census",
    state: "stage3_prime_round3_aborted_awaiting_fresh_round4_authorization",
    progress: "BP/CP producer contracts, owner/inverse/repetition semantics, serialization, migration, and trust-graph surfaces are concrete prospective interfaces; no producer, independent fixture/oracle, validator execution, owner computation, or census exists.",
    system: "unit-speed Bolza geodesic flow with a separately typed matched control; presentation-specific owner semantics; frozen generator/cutoff objects; target-blind no-retuning rule",
    route: "Route A A1 preparation with formal A0 prohibited/confounded; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked",
    main_trace_heading: "## Traceability",
    paper_route_heading: "## Route position and next gate",
    paper_route_next_heading: "## Batch traceability",
    paper_current_insert_before: "## Stage 2.5 integrity result"
  }
}.freeze

ARTIFACTS = {
  batch_report: "BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md",
  batch_receipt: "BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json",
  batch_checkpoint: "BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md",
  stage4_request_md: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md",
  stage4_request_json: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json",
  stage4_request_validation: "BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json",
  p29_report: "papers/29-bianchi-ideal-owner-refinement/notes/stage3_prime_round3_verification_report.md",
  p29_checker: "papers/29-bianchi-ideal-owner-refinement/notes/stage3_prime_round3_checker_receipt.json",
  p29_traceability: "papers/29-bianchi-ideal-owner-refinement/notes/stage3_prime_round3_traceability.json",
  p32_report: "papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_verification_report.md",
  p32_checker: "papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_checker_receipt.json",
  p32_traceability: "papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_traceability.json",
  p33_report: "papers/33-bolza-control-matched-census/notes/stage3_prime_round3_verification_report.md",
  p33_checker: "papers/33-bolza-control-matched-census/notes/stage3_prime_round3_checker_receipt.json",
  p33_abort: "papers/33-bolza-control-matched-census/notes/stage3_prime_round3_abort_record.json"
}.freeze

TARGETS = ["README.md"] + PAPERS.values.flat_map do |paper|
  base = File.join("papers", paper.fetch(:slug))
  [File.join(base, "README.md"), File.join(base, "notes", "pipeline_state.md"), File.join(base, "paper", "README.md")]
end
TARGETS.freeze

raise "internal target count changed: #{TARGETS.length}, expected 16" unless TARGETS.length == 16
raise "duplicate status-doc target" unless TARGETS.uniq.length == TARGETS.length
raise "forbidden write target" if TARGETS.any? { |path| path.match?(%r{/(?:manuscript\.tex|references\.bib|paper\.pdf)$|/(?:code|experiments|results)/|stage4_route_crosswalk\.md$}) }

missing_artifacts = ARTIFACTS.values.reject { |path| File.file?(File.join(ROOT, path)) }
unless missing_artifacts.empty?
  raise "required terminal artifacts are missing; no status document was changed: #{missing_artifacts.join(', ')}"
end

missing_targets = TARGETS.reject { |path| File.file?(File.join(ROOT, path)) }
unless missing_targets.empty?
  raise "status-document targets are missing; no status document was changed: #{missing_targets.join(', ')}"
end

HASHES = ARTIFACTS.transform_values { |path| Digest::SHA256.file(File.join(ROOT, path)).hexdigest }.freeze

def occurrence_count(text, needle)
  text.scan(Regexp.new(Regexp.escape(needle))).length
end

def checked_replace!(text, old, replacement, label)
  count = occurrence_count(text, old)
  raise "#{label}: expected exactly one literal target, found #{count}" unless count == 1

  text.sub!(old, replacement)
end

def checked_replace_regex!(text, pattern, replacement, label)
  count = text.scan(pattern).length
  raise "#{label}: expected exactly one regex target, found #{count}" unless count == 1

  text.sub!(pattern, replacement)
end

def replace_section!(text, heading, next_heading, replacement, label)
  start_token = "#{heading}\n"
  start_count = occurrence_count(text, start_token)
  raise "#{label}: expected one start heading, found #{start_count}" unless start_count == 1

  start_at = text.index(start_token)
  if next_heading
    end_token = "\n#{next_heading}\n"
    end_count = occurrence_count(text, end_token)
    raise "#{label}: expected one end heading, found #{end_count}" unless end_count == 1
    end_at = text.index(end_token, start_at + start_token.length)
    raise "#{label}: end heading precedes start heading" unless end_at
  else
    end_at = text.length
  end

  # Keep one newline in the replacement itself. When a following heading exists,
  # its retained leading newline then preserves the Markdown blank line. At EOF,
  # this also preserves the repository's trailing-newline convention.
  text[start_at...end_at] = "#{replacement.rstrip}\n"
end

def insert_after_heading!(text, heading, insertion, label)
  token = "#{heading}\n"
  checked_replace!(text, token, "#{token}\n#{insertion.rstrip}\n", label)
end

def insert_before_heading!(text, heading, insertion, label)
  token = "\n#{heading}\n"
  checked_replace!(text, token, "\n#{insertion.rstrip}\n\n#{heading}\n", label)
end

def replace_table_row!(text, label, replacement, audit_label)
  pattern = /^\| #{Regexp.escape(label)} \|[^\n]*$/
  checked_replace_regex!(text, pattern, replacement, audit_label)
end

def insert_after_table_row!(text, label, insertion, audit_label)
  pattern = /^(\| #{Regexp.escape(label)} \|[^\n]*$)/
  checked_replace_regex!(text, pattern, "\\1\n#{insertion.rstrip}", audit_label)
end

def artifact_rows(number, link_prefix, hashes)
  batch = <<~MD.rstrip
    | [Round-3 batch report](#{link_prefix}BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md) | `#{hashes.fetch(:batch_report)}` |
    | [Round-3 batch receipt](#{link_prefix}BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json) | `#{hashes.fetch(:batch_receipt)}` |
    | [Round-3 mandatory checkpoint](#{link_prefix}BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md) | `#{hashes.fetch(:batch_checkpoint)}` |
  MD

  case number
  when 29
    <<~MD.rstrip
      | [P29 Round-3 verification report](#{link_prefix}papers/29-bianchi-ideal-owner-refinement/notes/stage3_prime_round3_verification_report.md) | `#{hashes.fetch(:p29_report)}` |
      | [P29 Round-3 checker receipt](#{link_prefix}papers/29-bianchi-ideal-owner-refinement/notes/stage3_prime_round3_checker_receipt.json) | `#{hashes.fetch(:p29_checker)}` |
      | [P29 Round-3 traceability](#{link_prefix}papers/29-bianchi-ideal-owner-refinement/notes/stage3_prime_round3_traceability.json) | `#{hashes.fetch(:p29_traceability)}` |
      #{batch}
    MD
  when 32
    <<~MD.rstrip
      | [P32 Round-3 verification report](#{link_prefix}papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_verification_report.md) | `#{hashes.fetch(:p32_report)}` |
      | [P32 Round-3 checker receipt](#{link_prefix}papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_checker_receipt.json) | `#{hashes.fetch(:p32_checker)}` |
      | [P32 Round-3 traceability](#{link_prefix}papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_traceability.json) | `#{hashes.fetch(:p32_traceability)}` |
      #{batch}
    MD
  when 33
    <<~MD.rstrip
      | [P33 Round-3 verification report](#{link_prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round3_verification_report.md) | `#{hashes.fetch(:p33_report)}` |
      | [P33 checker-not-run receipt](#{link_prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round3_checker_receipt.json) | `#{hashes.fetch(:p33_checker)}` |
      | [P33 Round-3 abort record](#{link_prefix}papers/33-bolza-control-matched-census/notes/stage3_prime_round3_abort_record.json) | `#{hashes.fetch(:p33_abort)}` |
      #{batch}
    MD
  when 30, 31
    <<~MD.rstrip
      | [P30/P31 Stage-4′ exact request](#{link_prefix}BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md) | `#{hashes.fetch(:stage4_request_md)}` |
      | [Machine-readable request](#{link_prefix}BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json) | `#{hashes.fetch(:stage4_request_json)}` |
      | [Request validation](#{link_prefix}BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json) | `#{hashes.fetch(:stage4_request_validation)}` |
      #{batch}
    MD
  else
    raise "unsupported paper number: #{number}"
  end
end

def main_status(number, paper)
  shared_boundary = "Citation formatting remains frozen in plainnat numeric style. Canonical manuscript, bibliography, and PDF bytes; science/results; the frozen initial system; and every Route coordinate remain unchanged. Stage 4.5, Stage 5, canonical promotion, submission, Route advancement, result refresh, and new scientific execution remain unauthorized."

  body = case number
         when 29
           "Stage 3′ Round 3 completed all three gates. The official checker returned PASS and emitted Major Revision / ARS B4 at 7 FULL / 4 PARTIAL / 0 other, with zero Phase-2B adjustments. NEW-1 is a separate minor regression in the newly introduced independence wording. The only next legal action is explicit authorization to prepare a hash-bound P29 Stage-4′ item/target/operation request; neither that request nor any revision write is yet authorized."
         when 30
           "The controlling review remains the completed Stage 3′ Round-2 Major Revision / ARS B4 decision at 4 FULL / 5 PARTIAL. A hash-bound P30/P31 Stage-4′ request is now prepared and validated: 13 residual items, 37 manuscript target blocks, and 156 checks across the pair. It has not been authorized or executed, and no manuscript or bibliography edit has occurred. The next legal action is exact author confirmation of that already prepared request."
         when 31
           "The controlling review remains the completed Stage 3′ Round-2 Major Revision / ARS B4 decision at 3 FULL / 8 PARTIAL. A hash-bound P30/P31 Stage-4′ request is now prepared and validated: 13 residual items, 37 manuscript target blocks, and 156 checks across the pair. It has not been authorized or executed, and no manuscript or bibliography edit has occurred. The next legal action is exact author confirmation of that already prepared request."
         when 32
           "Stage 3′ Round 3 completed all three gates. The official checker returned PASS and emitted Major Revision / ARS B4 at 5 FULL / 7 PARTIAL / 0 other, with zero Phase-2B adjustments, new issues, dissents, or escalations. The only next legal action is explicit authorization to prepare a hash-bound P32 Stage-4′ item/target/operation request; neither that request nor any revision write is yet authorized."
         when 33
           "Stage 3′ Round 3 aborted fail-closed at phase2a_lint_failed. The committed 7 FULL / 5 PARTIAL / 1 NOT record is controlled as 6 FULL / 6 PARTIAL / 1 NOT because REV-P33-011 is PARTIALLY_ADDRESSED under both the valid primary audit and blind tie-break. The response, Phase 2B, traceability, checker, and decision were not run or emitted. The next legal action is explicit authorization for a wholly fresh Stage 3′ Round 4 with a new id, manifest, and fresh Phase-1/2A contexts."
         end

  <<~MD.rstrip
    ## Current status

    #{SYNC_MARKER}

    **#{number == 33 ? "ARS STAGE 3′ ROUND 3 ABORTED FAIL-CLOSED — AWAITING EXPLICIT FRESH ROUND-4 AUTHORIZATION." : (number == 30 || number == 31 ? "ARS STAGE 3′ ROUND 2 REMAINS COMPLETE — STAGE-4′ REQUEST PREPARED / AWAITING EXACT AUTHORIZATION." : "ARS STAGE 3′ ROUND 3 COMPLETE — OFFICIAL CHECKER PASS / MAJOR REVISION (B4).")}**

    Control state: `#{paper.fetch(:state)}`. #{body}

    Explicit manuscript progress: #{paper.fetch(:progress)}

    Frozen initial system: #{paper.fetch(:system)}.

    Route mapping: #{paper.fetch(:route)}. Stage 3′ cannot award Route credit.

    #{shared_boundary}
  MD
end

def main_current_trace(number, hashes)
  title = case number
          when 29, 32 then "### Current Stage-3′ Round-3 checker-backed outcome"
          when 33 then "### Current Stage-3′ Round-3 fail-closed outcome"
          else "### Prepared P30/P31 Stage-4′ request (not authorized or executed)"
          end

  summary = case number
            when 29
              "P29 is complete at Major Revision / B4 with checker PASS, 7 FULL / 4 PARTIAL / 0 other, zero Phase-2B adjustments, and the separate minor regression NEW-1. Only request-preparation authorization for a future P29 Stage 4′ is the next legal action."
            when 30
              "P30 remains at its completed Round-2 Major Revision / B4 outcome (4 FULL / 5 PARTIAL). The exact pair request contains 13 residuals and 37 target blocks and passed 156 checks; no listed operation has author approval and no draft/bibliography write occurred."
            when 31
              "P31 remains at its completed Round-2 Major Revision / B4 outcome (3 FULL / 8 PARTIAL). The exact pair request contains 13 residuals and 37 target blocks and passed 156 checks; no listed operation has author approval and no draft/bibliography write occurred."
            when 32
              "P32 is complete at Major Revision / B4 with checker PASS, 5 FULL / 7 PARTIAL / 0 other, and zero Phase-2B adjustments. Only request-preparation authorization for a future P32 Stage 4′ is the next legal action."
            when 33
              "P33 is aborted at phase2a_lint_failed: committed 7/5/1 versus controlling 6/6/1 on REV-P33-011. No response, Phase 2B, traceability, checker, or decision exists; the next action is an explicitly authorized fresh Round 4."
            end

  <<~MD.rstrip
    #{title}

    #{summary}

    | Current artifact | SHA-256 |
    |---|---|
    #{artifact_rows(number, "../../", hashes)}
  MD
end

def pipeline_current_rows(number)
  stage_row = case number
              when 29
                "| Stage 3′ Round 3 | `COMPLETE`; Phase 1/2A/2B PASS; final 7/4/0; adjustments `0`; NEW-1 minor regression; official checker `PASS`; decision `Major Revision / ARS B4` |"
              when 30
                "| Stage 4′ exact request | `PREPARED_NOT_AUTHORIZED_NOT_EXECUTED`; joint P30/P31 scope 13 residuals / 37 target blocks / 156 checks; manuscript and bibliography writes `0` |"
              when 31
                "| Stage 4′ exact request | `PREPARED_NOT_AUTHORIZED_NOT_EXECUTED`; joint P30/P31 scope 13 residuals / 37 target blocks / 156 checks; manuscript and bibliography writes `0` |"
              when 32
                "| Stage 3′ Round 3 | `COMPLETE`; Phase 1/2A/2B PASS; final 5/7/0; adjustments/new issues/dissents/escalations `0`; official checker `PASS`; decision `Major Revision / ARS B4` |"
              when 33
                "| Stage 3′ Round 3 | `ABORTED / phase2a_lint_failed`; Phase 1 and structural Phase 2A PASS; committed 7/5/1, controlling 6/6/1 on REV-P33-011; no response, Phase 2B, traceability, checker, or decision |"
              end

  active_row = case number
               when 29
                 "| Active Stage-3′ findings | four PARTIALLY_ADDRESSED residuals plus NEW-1, a separate minor regression; exact list in `stage3_prime_round3_verification_report.md` |"
               when 30
                 "| Active Stage-3′ findings | five PARTIALLY_ADDRESSED residuals; exact target/operation scope is frozen in the prepared Stage-4′ request |"
               when 31
                 "| Active Stage-3′ findings | eight PARTIALLY_ADDRESSED residuals; exact target/operation scope is frozen in the prepared Stage-4′ request |"
               when 32
                 "| Active Stage-3′ findings | seven PARTIALLY_ADDRESSED residuals, including six must-fix; exact list in `stage3_prime_round3_verification_report.md` |"
               when 33
                 "| Active Stage-3′ finding | REV-P33-011: committed FULL, controlling PARTIAL; fresh Round 4 required |"
               end
  [stage_row, active_row]
end

def pipeline_next_action(number)
  case number
  when 29
    "only explicit authorization to prepare a hash-bound P29 Stage-4′ item/target/operation request; no patch or manuscript write is authorized"
  when 30, 31
    "only exact author confirmation of the already prepared P30/P31 Stage-4′ request before any listed operation may execute"
  when 32
    "only explicit authorization to prepare a hash-bound P32 Stage-4′ item/target/operation request; no patch or manuscript write is authorized"
  when 33
    "only explicit authorization for fresh Stage 3′ Round 4 with a new round id, new manifest, fresh Phase-1/2A contexts, and all prior-round artifacts preserved"
  end
end

def pipeline_current_bindings(number, hashes)
  title = number == 30 || number == 31 ? "## Prepared Stage-4′ request bindings" : "## Current Stage-3′ Round-3 bindings"
  status = case number
           when 29 then "P29 Round 3 is complete: checker PASS; Major Revision / B4; 7/4/0; zero adjustments; NEW-1 minor regression."
           when 30 then "P30 remains complete under Round 2 at Major Revision / B4 (4/5/0). The exact P30/P31 Stage-4′ request is prepared but not authorized or executed."
           when 31 then "P31 remains complete under Round 2 at Major Revision / B4 (3/8/0). The exact P30/P31 Stage-4′ request is prepared but not authorized or executed."
           when 32 then "P32 Round 3 is complete: checker PASS; Major Revision / B4; 5/7/0; zero adjustments."
           when 33 then "P33 Round 3 is aborted at phase2a_lint_failed: committed 7/5/1 versus controlling 6/6/1 on REV-P33-011; no response, Phase 2B, traceability, checker, or decision."
           end

  <<~MD.rstrip
    #{title}

    #{status}

    | Current artifact | SHA-256 |
    |---|---|
    #{artifact_rows(number, "../../../", hashes)}

    Citation style remains plainnat numeric. The canonical manuscript,
    bibliography, PDF, science/results, frozen initial system, and Route
    coordinates are unchanged. New science executions: `0`. Stage 4.5, Stage 5,
    canonical promotion, submission, Route advancement, and result refresh remain
    unauthorized.
  MD
end

def paper_intro(number, paper)
  status = case number
           when 29
             "Stage 3′ Round 3 is complete with checker PASS and Major Revision / ARS B4 at 7 FULL / 4 PARTIAL / 0 other, zero Phase-2B adjustments, and NEW-1 as a separate minor regression. Only explicit authorization to prepare a P29 Stage-4′ request is next; no revision write is authorized."
           when 30
             "The controlling Round-2 outcome remains checker PASS and Major Revision / ARS B4 at 4 FULL / 5 PARTIAL. The exact joint P30/P31 Stage-4′ request (13 residuals, 37 targets, 156 checks) is prepared but not authorized or executed."
           when 31
             "The controlling Round-2 outcome remains checker PASS and Major Revision / ARS B4 at 3 FULL / 8 PARTIAL. The exact joint P30/P31 Stage-4′ request (13 residuals, 37 targets, 156 checks) is prepared but not authorized or executed."
           when 32
             "Stage 3′ Round 3 is complete with checker PASS and Major Revision / ARS B4 at 5 FULL / 7 PARTIAL / 0 other and zero Phase-2B adjustments. Only explicit authorization to prepare a P32 Stage-4′ request is next; no revision write is authorized."
           when 33
             "Stage 3′ Round 3 aborted at phase2a_lint_failed: committed 7 FULL / 5 PARTIAL / 1 NOT versus controlling 6 FULL / 6 PARTIAL / 1 NOT on REV-P33-011. No response, Phase 2B, traceability, checker, or decision exists; only an explicitly authorized fresh Round 4 is next."
           end

  <<~MD.rstrip
    Package note: this directory is the immutable canonical Stage-2.5 manuscript
    package; historical review sections below remain frozen. The authoritative
    current state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md).
    #{SYNC_MARKER}
    Control state: `#{paper.fetch(:state)}`. #{status}
    Canonical manuscript/PDF/bibliography bytes and plainnat numeric citation style
    remain unchanged.
  MD
end

def paper_current_section(number, hashes)
  heading = case number
            when 29, 32 then "## Current Stage 3′ Round-3 checker-backed outcome"
            when 33 then "## Current Stage 3′ Round-3 fail-closed outcome"
            else "## Prepared Stage-4′ request (not yet authorized)"
            end
  summary = case number
            when 29 then "P29 completed Round 3 at Major Revision / B4 with checker PASS, 7/4/0, zero adjustments, and NEW-1 as a minor regression."
            when 30 then "P30 remains at its completed Round-2 Major Revision / B4 outcome (4/5/0); the joint exact request has 13 residuals, 37 targets, and 156 passing checks, with zero manuscript/bibliography writes."
            when 31 then "P31 remains at its completed Round-2 Major Revision / B4 outcome (3/8/0); the joint exact request has 13 residuals, 37 targets, and 156 passing checks, with zero manuscript/bibliography writes."
            when 32 then "P32 completed Round 3 at Major Revision / B4 with checker PASS, 5/7/0, and zero adjustments."
            when 33 then "P33 aborted at phase2a_lint_failed; REV-P33-011 changes the committed 7/5/1 reading to the controlling 6/6/1 reading, and no response, Phase 2B, traceability, checker, or decision was produced."
            end

  <<~MD.rstrip
    #{heading}

    #{summary}

    | Current artifact | SHA-256 |
    |---|---|
    #{artifact_rows(number, "../../../", hashes)}
  MD
end

def paper_route_section(number, paper)
  next_action = pipeline_next_action(number)
  <<~MD.rstrip
    #{paper.fetch(:paper_route_heading)}

    Explicit manuscript progress: #{paper.fetch(:progress)}

    Frozen initial system: #{paper.fetch(:system)}.

    Route mapping: #{paper.fetch(:route)}. Stage 3′ cannot create Route credit.
    Across Papers 29--33 the formal Route-A tuple count remains 0/5, positive
    arithmetic A2 remains 0/5, A3/A4 remain 0/5, and Route B remains 0/5.

    The next legal action for P#{number} is #{next_action}. Canonical manuscript,
    bibliography, PDF, science/results, and the frozen system remain unchanged;
    new science executions are zero. Stage 4.5, Stage 5, canonical promotion,
    submission, Route advancement, and result refresh remain unauthorized.
  MD
end

documents = TARGETS.to_h do |relative_path|
  text = File.binread(File.join(ROOT, relative_path)).force_encoding("UTF-8")
  raise "#{relative_path}: status sync was already applied" if text.include?(SYNC_MARKER)
  [relative_path, text]
end

root = documents.fetch("README.md")
checked_replace_regex!(
  root,
  /^\| `29--33`[^\n]*$/,
  "| `29--33` — 五个同源但不同检验面的连续时间子型 | **Round 10 / Stage 3′ Round 3 closed；P29/P32 complete，P33 aborted；P30/P31 Stage 4′ request prepared** | Round-3 controlling aggregate 为 18 FULL / 17 PARTIAL / 1 NOT；P29/P32 checker `PASS` 且均为 Major Revision / B4，P33 因 `REV-P33-011` 在 `phase2a_lint_failed` 终止。P30/P31 的精确 Stage-4′ 请求已准备但未授权／未执行（13 residuals、37 targets、156 checks）。Canonical 15 files、science/results、初始系统及 Route 坐标均未变。见 [Round-3 报告](BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md)、[收据](BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json)与[检查点](BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md)。 |",
  "root progress-index row"
)

root_overview = <<~MD.rstrip
  ## Papers 29--33 Round 10 当前概要

  #{SYNC_MARKER}

  Round 10 的 ARS **Stage 3′ Round 3 已结账**。P29 与 P32 完成三门复审、官方
  checker 均为 `PASS`，决定分别为 **Major Revision / ARS B4**；P33 在不可原地重试
  的 Phase-2A 语义门以 `phase2a_lint_failed` 中止。Round-3 committed aggregate 为
  **19 FULL / 16 PARTIAL / 1 NOT**，控制读数为 **18 FULL / 17 PARTIAL / 1 NOT**；唯一
  controlling discrepancy 是 P33 `REV-P33-011`。P30/P31 沿用已完成的 Round-2
  Major/B4 结果，其 hash-bound Stage-4′ 精确请求已准备且通过 **156** 项检查，但
  **13 residuals / 37 target blocks** 均未获授权、未执行，draft/bibliography 写入为 0。

  | Paper | 当前复审／请求状态 | 明确论文进展 | 冻结初始系统 | 路线对应与下一合法动作 |
  |---|---|---|---|---|
  | [P29](papers/29-bianchi-ideal-owner-refinement/README.md) | Round 3 COMPLETE；checker PASS；Major/B4；7 FULL / 4 PARTIAL；0 adjustments；`NEW-1` minor regression | Gate M/Q、精确 inversion/conjugation、五个 fail-closed prospective interfaces 与失败优先级均已明确；无 owner law、quotient、fixture run 或 score。 | level-(3) Gaussian Bianchi unit-speed geodesic；hyperbolic-arclength；primitive loxodromic inversion-paired；一个 literal nonzero Gaussian prime ideal。 | A0/A1 foundation/interface；只可在明确授权后**准备** P29 Stage-4′ 精确请求。 |
  | [P30](papers/30-three-disk-nonconstant-roof-determinant/README.md) | Round 2 COMPLETE；checker PASS；Major/B4；4 FULL / 5 PARTIAL；Stage-4′ request prepared, not authorized/executed | physical-roof 六门 DAG、共同范数误差与控制面已型别化；无 roof/operator/determinant/enclosure/result。 | no-eclipse equilateral three-disk `d=6a`；Euclidean free-flight；primitive cyclic word；physical roof 与 unit-roof control 分离。 | `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`；明确确认后仅执行已冻结请求。 |
  | [P31](papers/31-level11-conjugacy-owner-ledger/README.md) | Round 2 COMPLETE；checker PASS；Major/B4；3 FULL / 8 PARTIAL；Stage-4′ request prepared, not authorized/executed | canonicalization biconditional、G/I/C 分型与 9,453-pair 派生审计均明确；无完整 ledger/theorem/execution。 | fixed positive time-change `Gamma_0(11)` geodesic；oriented primitive；inverse separate；powers repetitions；Hecke degree distinct。 | A1-only owner/canonicalization prep；明确确认后仅执行已冻结请求。 |
  | [P32](papers/32-homology-cover-renormalization-uniformity/README.md) | Round 3 COMPLETE；checker PASS；Major/B4；5 FULL / 7 PARTIAL；0 adjustments | higher/zero-content 先证伪、双 modulus schedules、双 limit order、dependency/comparator interfaces 已明确；无已证 factor/limit/obstruction。 | unit-speed genus-two；pure homology tower；oriented primitive inverse-separate；full content；`1/N` clock；`1/N^3` log norm。 | generic A1--A2 prep、arithmetic A0 unavailable；只可在明确授权后**准备** P32 Stage-4′ 精确请求。 |
  | [P33](papers/33-bolza-control-matched-census/README.md) | Round 3 ABORT；committed 7/5/1、controlling 6/6/1；无 Response/2B/checker/decision | BP/CP、owner/inverse/repetition、serialization、migration 与 trust graph 为明确 prospective interfaces；无 producer/validator/census。 | unit-speed Bolza + separately typed matched control；presentation-specific owner；frozen generator/cutoff；target-blind no-retuning。 | A1 prep、formal A0 prohibited/confounded；下一动作仅为明确授权的 fresh Round 4。 |

  Stage 3′ 是复审门，不能产生 A0--A4 或 B1--B5 credit。全批 formal Route-A
  tuples 为 **0/5**，positive arithmetic A2 为 **0/5**，A3/A4 为 **0/5**，Route B
  为 **0/5**。Canonical manuscript/bibliography/PDF 共 **15/15 unchanged**；science
  results unchanged；new scientific executions **0**。引用继续保持 `plainnat` 数字制。

  当前权威 batch artifacts：

  - [Stage-3′ Round-3 report](BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md) — SHA-256 `#{HASHES.fetch(:batch_report)}`
  - [Stage-3′ Round-3 receipt](BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json) — SHA-256 `#{HASHES.fetch(:batch_receipt)}`
  - [Mandatory checkpoint](BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md) — SHA-256 `#{HASHES.fetch(:batch_checkpoint)}`
  - [P30/P31 Stage-4′ exact request](BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md) — SHA-256 `#{HASHES.fetch(:stage4_request_md)}`
  - [P30/P31 request validation](BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json) — SHA-256 `#{HASHES.fetch(:stage4_request_validation)}`

  **建议的下一组五篇动作**：明确确认后执行已经冻结的 P30/P31 Stage-4′ request；
  对 P29/P32 只准备 hash-bound Stage-4′ request；对 P33 启动 new-id/new-manifest/
  fresh-context Round 4。Stage 4.5、Stage 5、canonical promotion、投稿、Route 晋级、
  result refresh 与新科学执行仍未授权。
MD
replace_section!(root, "## Papers 29--33 Round 10 当前概要", "### 历史：Stage 2.5 与 Stage 3 Phase 0 基线", root_overview, "root Round-10 overview")

round3_history = <<~MD.rstrip

  29--33-round10-stage3-prime-round3 - ARS Stage 3′ Round 3 closed（2026-09-03，当前强制检查点） - P29/P32 完成三门复审并通过官方 checker 2/2，决定均为 Major Revision / B4；P29 为 7 FULL / 4 PARTIAL 且有独立记录的 `NEW-1` minor regression，P32 为 5 FULL / 7 PARTIAL，两篇 Phase-2B adjustments 均为 0。P33 的 committed 7/5/1 因 `REV-P33-011` 受控为 6/6/1，并在 no-retry Phase-2A 语义门以 `phase2a_lint_failed` 中止；无 Response、Phase 2B、traceability、checker 或 decision。Round-3 控制总数为 18/17/1。并行准备的 P30/P31 Stage-4′ 精确请求为 13 residuals、37 targets、156/156 checks，尚未授权／执行。Canonical manuscript/bib/PDF 15/15、science/results、五个初始系统与 Route 坐标均未变；new science executions 0，formal Route-A tuples 0/5、positive arithmetic A2 0/5、A3/A4 0/5、Route B 0/5。下一组动作需明确确认：执行冻结的 P30/P31 request；仅准备 P29/P32 request；fresh P33 Round 4。详见 [Round-3 报告](BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md)（SHA-256 `#{HASHES.fetch(:batch_report)}`）、[收据](BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json)（`#{HASHES.fetch(:batch_receipt)}`）与[强制检查点](BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md)（`#{HASHES.fetch(:batch_checkpoint)}`）。
MD
raise "root: Round-3 history ledger already exists" if root.include?("29--33-round10-stage3-prime-round3 -")
raise "root: expected Round-2 ledger entry before append" unless root.include?("29--33-round10-stage3-prime-round2 -")
root << "\n" unless root.end_with?("\n")
root << round3_history
root << "\n"

PAPERS.each do |number, paper|
  slug = paper.fetch(:slug)
  main_key = File.join("papers", slug, "README.md")
  state_key = File.join("papers", slug, "notes", "pipeline_state.md")
  package_key = File.join("papers", slug, "paper", "README.md")

  main = documents.fetch(main_key)
  package_heading = number <= 31 ? "## Current paper package" : "## Current paper and revision package"
  replace_section!(main, "## Current status", package_heading, main_status(number, paper), "P#{number} main status")

  main_links = case number
               when 29
                 <<~MD
                   - [Stage-3′ Round-3 verification report](notes/stage3_prime_round3_verification_report.md), [official checker receipt](notes/stage3_prime_round3_checker_receipt.json), and [traceability matrix](notes/stage3_prime_round3_traceability.json)
                   - [Round-3 batch report](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md), [receipt](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json), and [mandatory checkpoint](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md)
                 MD
               when 32
                 <<~MD
                   - [Stage-3′ Round-3 verification report](notes/stage3_prime_round3_verification_report.md), [official checker receipt](notes/stage3_prime_round3_checker_receipt.json), and [traceability matrix](notes/stage3_prime_round3_traceability.json)
                   - [Round-3 batch report](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md), [receipt](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json), and [mandatory checkpoint](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md)
                 MD
               when 33
                 <<~MD
                   - [Stage-3′ Round-3 verification report](notes/stage3_prime_round3_verification_report.md), [checker-not-run receipt](notes/stage3_prime_round3_checker_receipt.json), and [abort record](notes/stage3_prime_round3_abort_record.json)
                   - [Round-3 batch report](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md), [receipt](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json), and [mandatory checkpoint](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md)
                 MD
               else
                 <<~MD
                   - [Prepared P30/P31 Stage-4′ request](../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md), [machine request](../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json), and [156-check validation](../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json)
                   - [Round-3 batch report](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md), [receipt](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json), and [mandatory checkpoint](../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md)
                 MD
               end
  checked_replace!(main, "- [Pipeline state](notes/pipeline_state.md)\n", "#{main_links}- [Pipeline state](notes/pipeline_state.md)\n", "P#{number} main current-package links")

  if [29, 32, 33].include?(number)
    checked_replace!(main, "### Current Stage-3′ Round-2 outcome", "### Historical Stage-3′ Round-2 outcome", "P#{number} main Round-2 heading")
  end
  insert_after_heading!(main, paper.fetch(:main_trace_heading), main_current_trace(number, HASHES), "P#{number} main current trace")

  if number <= 31
    current_round_pattern = /^- Stage 3′ Round 2:.*$/
    round_lines = case number
                  when 29
                    "- Stage 3′ Round 2: immutable historical fail-closed record.\n- Stage 3′ Round 3: `COMPLETE`; final 7/4/0; Phase-2B adjustments `0`; `NEW-1` minor regression; checker `PASS`; Major Revision / ARS B4. Only explicit authorization to prepare a P29 Stage-4′ request may follow."
                  when 30
                    "- Stage 3′ Round 2: `COMPLETE`; final 4/5/0; Phase-2B adjustments `0`; checker `PASS`; Major Revision / ARS B4.\n- Stage 4′ request: joint P30/P31 request prepared and validated at 13 residuals / 37 targets / 156 checks; not authorized, not executed, and manuscript/bibliography writes remain 0."
                  when 31
                    "- Stage 3′ Round 2: `COMPLETE`; final 3/8/0; Phase-2B adjustments `0`; checker `PASS`; Major Revision / ARS B4.\n- Stage 4′ request: joint P30/P31 request prepared and validated at 13 residuals / 37 targets / 156 checks; not authorized, not executed, and manuscript/bibliography writes remain 0."
                  end
    checked_replace_regex!(main, current_round_pattern, round_lines, "P#{number} main current round/request bullet")
  else
    token_updates = case number
                    when 32
                      ["`STAGE3_PRIME_ROUND2=ABORTED_PHASE2A_LINT_FAILED`,\n`STAGE3_PRIME_DECISION_EMITTED=false`, and\n`STAGE3_PRIME_ROUND3_AUTHORIZED=false`.", "`STAGE3_PRIME_ROUND2=HISTORICAL_ABORT`,\n`STAGE3_PRIME_ROUND3=COMPLETE_MAJOR_REVISION_B4`,\n`STAGE3_PRIME_DECISION_EMITTED=true`, and\n`STAGE4_PRIME_REQUEST_PREPARATION_AUTHORIZED=false`."]
                    when 33
                      ["`STAGE3_PRIME_ROUND2=ABORTED_PHASE2A_LINT_FAILED`,\n`STAGE3_PRIME_DECISION_EMITTED=false`, and\n`STAGE3_PRIME_ROUND3_AUTHORIZED=false`.", "`STAGE3_PRIME_ROUND2=HISTORICAL_ABORT`,\n`STAGE3_PRIME_ROUND3=ABORTED_PHASE2A_LINT_FAILED`,\n`STAGE3_PRIME_DECISION_EMITTED=false`, and\n`STAGE3_PRIME_ROUND4_AUTHORIZED=false`."]
                    end
    checked_replace!(main, token_updates[0], token_updates[1], "P#{number} main control tokens")

    tail_pattern = /All detailed Stage-1 research, source, review, and revision artifacts remain\nfrozen in `notes\/`;.*\z/m
    tail = if number == 32
             <<~MD.rstrip
               All detailed Stage-1 research, source, review, and revision artifacts remain
               frozen in `notes/`; all Round-1/Round-2/Round-3 review artifacts are preserved.
               A schema-compatible Stage-4 Revision-Evidence Bundle exists, but official
               Stage-4.5 E6 has not been invoked. The only next legal action is explicit
               authorization to prepare a hash-bound P32 Stage-4′ request; no patch or
               manuscript write is authorized. Stage 4.5, Stage 5, canonical promotion,
               submission, Route advancement, result refresh, and new scientific execution
               remain unauthorized.
             MD
           else
             <<~MD.rstrip
               All detailed Stage-1 research, source, review, and revision artifacts remain
               frozen in `notes/`; all Round-1/Round-2/Round-3 review artifacts are preserved.
               A schema-compatible Stage-4 Revision-Evidence Bundle exists, but official
               Stage-4.5 E6 has not been invoked. The only next legal action is explicit
               authorization for a new-id/new-manifest/fresh-context Stage 3′ Round 4.
               Stage 4′, Stage 4.5, Stage 5, canonical promotion, submission, Route
               advancement, result refresh, and new scientific execution remain unauthorized.
             MD
           end
    checked_replace_regex!(main, tail_pattern, tail, "P#{number} main next-action tail")
  end

  main << "\n" unless main.end_with?("\n")
  documents[main_key] = main

  state = documents.fetch(state_key)
  checked_replace_regex!(state, /^Current controlling state: .*$/, "Current controlling state: **`#{paper.fetch(:state)}`**.\n\n#{SYNC_MARKER}", "P#{number} pipeline current state")
  replace_table_row!(state, "Pipeline global state", "| Pipeline global state | `#{paper.fetch(:state)}` |", "P#{number} pipeline global state")
  checked_replace_regex!(
    state,
    /^(\| (?:\[Bibliography\]\([^)]+\)|Bibliography) \|[^\n]*$)/,
    "\\1\n| Citation style | `plainnat` numeric; unchanged |",
    "P#{number} pipeline citation style"
  )
  stage_row, active_row = pipeline_current_rows(number)
  insert_after_table_row!(state, "Stage 3′ Round 2", stage_row, "P#{number} pipeline current round/request row")

  next_label = state.include?("| Next legal action |") ? "Next legal action" : "Next legal transition"
  replace_table_row!(state, next_label, "| #{next_label} | #{pipeline_next_action(number)} |", "P#{number} pipeline next action")
  if state.include?("| Active Stage-3′ findings |")
    replace_table_row!(state, "Active Stage-3′ findings", active_row, "P#{number} pipeline active findings")
  else
    insert_after_table_row!(state, next_label, active_row, "P#{number} pipeline active findings insertion")
  end

  if [29, 32, 33].include?(number)
    checked_replace!(state, "## Current Stage-3′ Round-2 bindings", "## Historical Stage-3′ Round-2 bindings", "P#{number} pipeline Round-2 binding heading")
  end
  state << "\n" unless state.end_with?("\n")
  state << "\n#{pipeline_current_bindings(number, HASHES)}\n"
  documents[state_key] = state

  package = documents.fetch(package_key)
  title_end = package.index("\n\n")
  raise "P#{number} package: missing title boundary" unless title_end
  deliverables_at = package.index("\n## Deliverables\n")
  raise "P#{number} package: missing Deliverables heading" unless deliverables_at
  intro_start = title_end + 2
  package[intro_start...deliverables_at] = "#{paper_intro(number, paper)}\n"

  if [32, 33].include?(number)
    checked_replace!(package, "## Current Stage 3′ Round-2 controlling outcome", "## Historical Stage 3′ Round-2 controlling outcome", "P#{number} package Round-2 heading")
  end
  insert_before_heading!(package, paper.fetch(:paper_current_insert_before), paper_current_section(number, HASHES), "P#{number} package current artifacts")
  replace_section!(package, paper.fetch(:paper_route_heading), paper.fetch(:paper_route_next_heading), paper_route_section(number, paper), "P#{number} package Route/next section")
  documents[package_key] = package
end

documents.each do |relative_path, text|
  marker_count = occurrence_count(text, SYNC_MARKER)
  raise "#{relative_path}: expected one status-sync marker, found #{marker_count}" unless marker_count == 1
  raise "#{relative_path}: transformation produced no trailing newline" unless text.end_with?("\n")
end

# All substitutions are validated in memory before the first write. Targets are
# the root README plus exactly three status documents for each of P29--P33.
documents.each do |relative_path, text|
  absolute_path = File.join(ROOT, relative_path)
  temporary_path = "#{absolute_path}.round3-status.tmp"
  raise "temporary path already exists: #{temporary_path}" if File.exist?(temporary_path)
  File.binwrite(temporary_path, text)
  File.chmod(File.stat(absolute_path).mode, temporary_path)
  File.rename(temporary_path, absolute_path)
end

TARGETS.each { |path| puts path }
puts "updated_files=#{TARGETS.length}"
