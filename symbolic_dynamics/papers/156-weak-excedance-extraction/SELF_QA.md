# P156 author-side self-QA

**Date:** 2026-09-02 UTC.  **Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Contract audit

- The image threshold, all-rank section, Ferrers fibre, recurrence, and
  right-inverse tower match the reframed freeze ceiling.
- “Locally minimum” is defined only as one-step minimum source rank.
- The false pointwise clock is displayed as false, not as a conjecture.
- No global maximum clock or global iterated-preimage optimum is claimed.
- The Bell identity-basin aggregate is cited and subtracted at theorem level.

## Proof-interface attacks

1. **Why is `a_j<=h+j`?** Among the first `a_j` values exactly `j` are
   selected, so at most all `h` complement values can precede it.
2. **Can a low-tail value be accidentally selected?** Low value `j` occurs at
   position `m+j>j`, so it is strictly deficient.
3. **Does the fibre product overcount?** No: fixed selected sets force their
   assignment, and increasing complement positions expose disjoint sequential
   choices; every source has one selected-set pair.
   For `n<m` the fibre is empty by rank, while at `n=m` the empty product is
   one and admissibility leaves only the identity target.
4. **Can a nonidentity have `d=0`?** No: `sigma_i>=i` for all `i` plus equal
   coordinate sums forces the identity.
5. **Is the tower drop really `m`?** High entries have nonpositive drop;
   every low-tail entry has drop exactly `m`.
6. **Does local minimality compose globally?** Not necessarily, and the paper
   expressly makes no such claim.
7. **Could the inverse tower imply the global forward clock?** No: it supplies
   witnesses on one backward ray, not an upper bound for arbitrary sources.

## Source and claim audit

All eight bibliography entries are cited.  Weak-excedance, maximum-drop,
tableau/Bruhat, transposition-array, Bell aggregate, and generic Ferrers-board
inputs are zero credit.  The exact-map query result is presented only as a
bounded non-hit.

## Computational audit

`verify_p156.py` performs 3,689,489 exact assertions with no randomness,
floating point, third-party dependency, or runtime network.  It cold-checks
images, fibres, 362,879 explicit rank-boundary cells, the zero-credit Bell
aggregate, six tower levels for 46,225 targets, and the exact rank-11 clock
counterexample.

## Artifact boundary

The anonymous manuscript contains all mandatory declarations, including
External Status.  Hostile Review A is preserved separately; its two Minor
findings closed in Round 1.  Hostile Review B is also preserved separately;
its one Minor finding identified a stale 26-row font count in two author
ledgers.  The corrected count is 27, and every row is embedded, subsetted,
and Unicode-enabled.  No mathematical, source, verifier, transcript, or PDF
change was required.  The current/Round-2 PDF remains 4 A4 pages, 336,311
bytes, at SHA-256
`7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979`.
All findings are closed.  This author-side QA does not authorize external
release.
