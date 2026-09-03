# P177 improvement log

## Round 0 → Round 1

Review A found one Major theorem-statement defect: the unique endpoint
coordinate did not by itself imply the existence of a history at `t=0` or
`t=1`.  The repaired theorem now states that existence is equivalent to
`a_t(L)>0` and gives the exact support (`L=0` at zero steps, `L!=0` at one
step, all `L` from two steps).  The proof records positivity explicitly.

The author verifier gained direct sentinels for both zero-count boundaries;
its total increased from 1,095,978 to 1,095,999 exact assertions.  Stale
theorem locations in `PAPER_PLAN.md` were synchronized.  Review B's
provenance wording concern was also repaired by labelling the program an
author-side regression control throughout.

Round-1 PDF SHA-256:
`ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c`.

## Round 1 → Round 2

Reviewer A formally accepted the repaired support statement after two fresh
36,510-assertion replays.  Reviewer B reopened the repaired bytes, closed its
provenance Minor, and reproduced 224,874 independent assertions twice.  No
additional source change was required, so Round 2 deliberately reproduces
the Round-1 PDF byte for byte.  Two source-only cold builds and a four-page
visual audit also pass.  External status remains `HOLD_EXTERNAL`.
