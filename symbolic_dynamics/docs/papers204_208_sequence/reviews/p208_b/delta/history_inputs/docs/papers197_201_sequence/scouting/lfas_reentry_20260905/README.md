# LFAS reserve re-entry, 2026-09-05

**THEOREM_SPIKE / STAGE1_GATE_PENDING / HOLD_EXTERNAL**.
This is the same LFAS literal previously reserved, with deductive progress;
it adds zero new literal systems to the breadth denominator.

The closed package is `THEOREM_CONTRACT_AND_PROOF.md`: the earliest pivot
row is invariant, each partner is visited at most twice before recurrence,
and `tau<=2r-3` is sharp for every `s>=r+1`. The new inverse formula is an
explicit first-difference column interval plus row-comparability test. It
gives maximum fibre `(r-1)(s-1)` and exactly two maximizing targets, except
the bijective `2x2` boundary where all 16 maximize. Fixed and two-cycle
states have a complete row-support criterion.

This package deliberately leaves the exact maximum tail for `s<=r` open.
The guessed symmetric formula is not used. Transpose image counts differ,
so transposition cannot justify a symmetric theorem.

`SOURCE_AND_COLLISION.md` records actual primary-source retrieval, including
Ryser's original interchange theorem, Brewbaker's lonesum paper, and the
August 2026 Baggett--Yan interchange-graph paper. These are mandatory
subtractions. An independent candidate gate is still needed; no paper
number or external novelty status is assigned by this re-entry.

Run the deterministic exact verifier:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers197_201_sequence/scouting/lfas_reentry_20260905/verify_lfas_reentry.py
```

It enumerates the complete carrier in 11 boxes, compares an independent
literal rectangle scan against row-support theory, checks exact inverse
source sets and all maximizing targets, and checks 38 wide witnesses.
`CANONICAL.txt` reports 1,076,738 assertions. Two fresh-process replays are
recorded separately. This is the re-entry verifier, not manuscript Review A
or B and not the earlier author's multi-system verifier count.

`probe_lfas.cpp` is exploratory only. Its exhaustive mode was used for
`4x5` (all 1,048,576 matrices, maximum tail 5); heuristic mutation walks
found witnesses for larger boxes. These samples do not certify maxima.
The safe tested probe dimensions have at most 12 rows and 10 columns;
its integer bit-mask syntax is not advertised for arbitrary dimensions.
The Python theorem verifier has no such fixed-width representation limit.

All old reserve and author files are preserved. `INPUT_PINS.sha256` is
relative to the workspace root; package `SHA256SUMS` excludes itself.
