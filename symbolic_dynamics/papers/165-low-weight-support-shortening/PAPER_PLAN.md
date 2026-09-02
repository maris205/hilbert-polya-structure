# P165 paper plan — low-weight support shortening

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## One-sentence contribution

After assigning zero credit to one-step low-weight hitting-set shortening,
the note gives the exact dyadic clock, every-time image boundary for every
nonzero target, and the classified simultaneous dimension/support-minimal
slice of each such target fibre for the autonomous padded-shortening map.

## Claim architecture

1. Define the literal map before using any distance consequence; retain the
   deleted coordinates as zero coordinates so the update is a self-map.
2. Subtract Jibril et al.'s entire one-step hitting-set shortening principle,
   including distance increase, rather than presenting it as a contribution.
3. Derive pairwise-disjoint purge sets and a geometric support budget; use
   it to prove the unique zero recurrent state and sharp height.
4. Reverse the dynamics for an arbitrary prescribed nonzero target using
   dyadic full-support lines on target-zero coordinates.
5. Prove lower bounds for every source in every nonzero target fibre.
6. Classify and count only the sources simultaneously attaining both lower
   bounds; never present the formula as a full-fibre count.
7. Isolate `D=0`, `t=0`, `n=0`, full-support targets, exhausted coordinate
   capacity, the strict threshold, labelled coordinates, and nonprime fields.

## Page architecture

- Abstract and literal/owner boundary: 1 page.
- Main theorem and temporal clock: 1.5 pages.
- Every-time image theorem: 0.75 page.
- Extremal inverse layer: 1 page.
- Boundaries, exact controls, declarations, references: 0.75 page.

Target: anonymous `amsart`, A4, 4--6 pages, no figures or appendices.

## Evidence plan

All-parameter proofs appear in the manuscript and `PROOF_PACKAGE.md`.
`code/verify.py` is an independent finite falsifier, not a proof and not an
ownership test.  `SOURCE_VERIFICATION.md` records the bounded source audit.
