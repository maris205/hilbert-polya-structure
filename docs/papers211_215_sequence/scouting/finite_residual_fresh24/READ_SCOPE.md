# Fresh24 read scope and failures

The exact command/request and the entire native returned value for every
listed key are in EVIDENCE_CAPTURE.json. 31 records: 24 shell read/navigation
returns and 7 Web search/open/find returns. None is a scientific execution.

## Selected local originals

- Project skill and workflow: complete bounded reads reaching EOF,
  keys `f24_skill`, `f24_workflow`, and complete re-reads
  `f24_reread_skill`, `f24_reread_workflow`.
- Active recovery entries only: `f24_state`, `f24_batch`,
  `f24_reread_state`, `f24_reread_batch`. These are partial index ranges,
  not proofs or full-history reads.
- Current batch PROBLEM_ANCHOR: complete reads `f24_anchor` and
  `f24_reread_correct_anchor`.
- Historical C12 definition, C13/C18/C19 comparisons:
  `f24_old_C12_definition`, lines 54–78, partial original scout;
  `f24_old_C12_range`, lines 150–198, partial old owner notes.
  Old pilot summaries are DATA only; no pilot source was run or validated.
- Whole original group hostile gate: `f24_oldgate_full`, command
  lines 1–460 reaches EOF (411 lines).
- Whole original group proof spike: `f24_oldproof_full`, command
  lines 1–260 reaches EOF (197 lines; retain original typo and
  overbroad “full functional graph” language as historical evidence).
- TWC: `f24_old_TWC_range` is only lines 84–117 and is not the full proof.
  `f24_old_TWC_complete_section`, lines 58–109, subsequently covers the
  complete selected subsection at lines 64–108, with a few surrounding
  rows. Not the entire containing scout.
- `f24_old_shallow_word_rows`, lines 41–53, is a partial original table.
- `f24_prior_literal_navigation`, `f24_oldgate_paths` and
  `f24_oldgate_navigation` are targeted path/text navigation, not a full
  corpus read or a proof of absence. Broad regex matches include unrelated
  words; no conclusion depends on those false positives.
- New output path checks: `f24_owned_path_navigation` returns exit 1/no
  matches; because its glob alone is not an absence proof,
  `f24_new_directory_absence` explicitly tests the exact owned new path
  and returns exit 0 before creation.
- `f24_original_line_count` checks the exact two whole original file line
  counts using wc; the initial draft's guessed counts were corrected before
  sealing. No contents of either historical original changed.

## All original Web calls, without discarded failures

1. `f24_primary_search`: three exact initial queries. Full search return,
   including secondary/unselected/unrelated hits; only navigation value
   is assigned to those hits.
2. `f24_primary_open`: author-page timeout; WIAS PDF indexed-text opening
   returns lines 0–319 out of 778 indexed lines. Excerpt, not full paper.
3. `f24_owner_locator`: three Almeida queries and a WIAS “2. The
   Thue-Morse” find. Complete search return and exact find no-match.
4. `f24_direct_cim_and_wias_locator`: direct CIM article opening returns
   lines 0–377 out of 981 indexed lines; WIAS “This time” find has no match.
   Excerpt, not full paper.
5. `f24_primary_target_excerpts`: targeted URL+line openings for CIM and
   WIAS both time out. No body read credited.
6. `f24_primary_cached_excerpts`: targeted reference+line openings also
   both time out. No body read credited.
7. `f24_primary_target_search`: three primary-domain exact queries return
   the complete requested result set. CIM printed page 12 explicitly
   contains the map and finite-group dynamics; WIAS printed page 19
   contains equations (4.5)–(4.6). The unrelated CIM Lie-algebra result is
   retained but unused.

No screenshots or PDF files were created. A Web-provided textual
“visual_element” description is not a page view. Returned body snippets,
even long ones, are selected original-source excerpts, not full-paper reads.

## Preserved errors and limits

- One initial combined display exceeded the orchestration display budget;
  complete component result objects had already been retained. The full
  initial Web return was displayed separately before being used. The
  preserved native shell returns themselves do not report truncation.
- Failed path `docs/research_state/CURRENT_CLAIM_ANCHOR.md`:
  `f24_reread_anchor`, native afe07e, exit 2, exact “No such file or
  directory” output retained. The correct linked batch PROBLEM_ANCHOR was
  read under `f24_reread_correct_anchor`.
- One no-match path query and two WIAS find no-match returns are not owner
  no-hit claims.
- Author-page timeout plus four targeted PDF-opening timeouts are retained.
  Successful primary-domain search excerpts supply only their displayed
  passages, not the inaccessible full papers.
- Historical source/proof wording is not silently repaired; current
  report explicitly limits “full graph”, carrier embeddings and output
  transform/conjugacy assertions.
- The attempted documentation census with jq failed (exit 127, command
  not found). Its complete native return is in VALIDATION_CAPTURE.json.
  Fallback: sed reads only EVIDENCE_CAPTURE.json; the orchestration layer
  parses that returned JSON and compares every complete record with its
  original captured value. All 31 match. No host script or import runs.
- The first combined prose read is a 260-line range across concatenated
  files, so its HANDOFF tail is incomplete. A separate whole HANDOFF read
  supplies that tail. A malformed backtick and initially guessed whole-file
  line counts were repaired before sealing; pre-fix returns are retained.
- No filesystem raw-byte replay of old outputs, review PASS, imported
  verifier execution, host runtime evidence or root acceptance is claimed.

The report's claim footprint is checked by direct reading and this exact
documentation inventory. A manifest hashes the physical new payloads only.
