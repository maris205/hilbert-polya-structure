# Final public-Web originality screen — P182–P186

**Run date:** 2026-09-03 UTC.  **Result:**
`61/116 DISTINCT PROSE BLOCKS SCREENED / 64 QUERY EXECUTIONS / 0 QUALIFYING CLOSE MATCH / 0 VERBATIM MATCH`.

This is a heuristic public-Web search, not professional plagiarism-detection
software.  It cannot inspect closed databases, translated reuse, paraphrase
reuse outside surfaced results, or the unsampled 55 blocks.  `NO MATCH` below
means only that no qualifying exact or close textual match appeared in the
public search results inspected for the recorded query.  It is not an
authorship, novelty, priority, or ownership determination.

The denominator uses the same deterministic blank-line block split as the
initial screen: manuscript-body prose blocks with at least 18 alphabetic
tokens.  Review-A source changes did not alter the denominator.  The final
sample exceeds 50% in every manuscript and includes every paragraph modified
after Round 0.

| paper | body blocks | distinct screened IDs | rate | result |
|---:|---:|---|---:|---|
| P182 | 28 | 1, 2, 3, 4, 6, 8, 12, 13, 14, 15, 18, 21, 23, 27 | 50.0% | 14 NO MATCH |
| P183 | 25 | 1, 3, 4, 5, 6, 7, 9, 11, 12, 13, 17, 18, 19, 21 | 56.0% | 14 NO MATCH |
| P184 | 23 | 1, 3, 4, 5, 6, 7, 9, 11, 13, 14, 16, 20 | 52.2% | 12 NO MATCH |
| P185 | 20 | 1, 2, 3, 6, 7, 9, 10, 12, 13, 15, 16 | 55.0% | 11 NO MATCH |
| P186 | 20 | 1, 2, 3, 6, 7, 8, 10, 11, 12, 16 | 50.0% | 10 NO MATCH |
| **total** | **116** | **61 distinct blocks** | **52.6%** | **61 NO MATCH** |

Across the batch, 64 searches cover 61 distinct blocks.  Three repeat queries
were deliberate: P183 block 13 received a second history-count phrasing, and
P185 block 1 and P186 block 1 were searched again after their Round-1 wording
repairs.

## Initial query population

The 36 pre-review queries, their 36/116 block sample, and their inspected
results are preserved verbatim in `ORIGINALITY_AUDIT_INITIAL.md`.  None
surfaced a qualifying close or verbatim match.  The following queries extend
that population and re-open every revised paragraph.

## Final-extension query audit trail

### P182 — additional blocks

- `"depth of a state is its distance to the recurrent set"`
- `"The image consists exactly of triples" "M" "J" subspaces`
- `"A state outside the recurrent set has depth one exactly when"`
- `"The universal predicates reduce every population to a finite-geometry count"`
- `"The first image" "is recurrent if and only if" "A" "B" "C" lattice comparator`

### P183 — additional blocks

- `"Associate to" "the simple conflict graph" directed graph`
- `"exact conflict deletion" "conflict graph" vertex`
- `"vertex history" "missing set" conflict graph`
- `"all-time absorption CDF" independent sets`
- `"labelled actions versus distinct sources"`

Two extra phrasings (`"Selecting a vertex removes all incident conflicts"`
and `"histories with exact support" "prescribed labels" surjections`) also
produced no qualifying match.  The first adds block 11 to the denominator;
the second rechecks already sampled block 13.

### P184 — additional blocks

- `"the tail" "least" "for which" "is periodic" finite map`
- `"all valuation strata" finite dynamics prime power`
- `"complete functional-graph census" prime power valuation`
- `"double-target set" valuation prime power dynamics`
- `"a target other than" "is double precisely when" valuation`

Generic search hits about tails, valuation records, and unrelated double
targets did not reproduce the manuscript's characteristic wording or
mathematical sequence and were rejected.

### P185 — additional and revised blocks

- `"prefix-diversity self-map" word`
- `"pointwise all-time iterate" "prefix" diversity`
- `"binary-rise paths with an identity prefix"`
- `"positive depth population is the difference of consecutive values"`
- `"The product" "is empty when" "n-1" fibre prefix diversity`
- revised abstract recheck: `"Every transient target fibre is a local product"`

The last query rechecks the Round-1 abstract.  The product query covers the
new explicit `t=n-1` empty-product sentence; the same paragraph also states
the repaired `t=0` and stabilized fibres.

### P186 — additional and revised blocks

- `"rank-compression support" subset map`
- `"all-time gap normal form" subset dynamics`
- `"The recurrent states are precisely" "singletons" subset map`
- `"complete time-t inverse atlas" gap`
- revised abstract recheck: `"each original consecutive gap" "contributes" "exactly when"`

The last query reaches the repaired `g>t` survival wording; the same revised
abstract block contains the restored `n>=2` qualifier for the unique deepest
state.

## Residual limitation

All manuscripts are anonymous and no author publication list was supplied.
Author-specific self-plagiarism comparison therefore remains `NOT_CHECKED`,
not a clean result.  The screen supports only an internal disclosure gate and
does not alter `OWNER_AMBER / HOLD_EXTERNAL`.
