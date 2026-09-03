# Hostile Review B — P178 state-selected finite differences

**Reviewer process:** root, preliminary Round-0 review with explicit Round-1
documentation re-entry.  
**Reviewed bytes:** byte-identical Round-1 PDF SHA-256
`b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce`.  
**Reviewed source:** `main.tex`
`d89e740fa45a8ad21a1244c504ec3288cce1e887f7ca2dd14febe4822e7b3603`.  
**Verdict:** `PROVABLE AS STATED / 0 CRITICAL / 0 MAJOR / 0 MINOR /
HOLD_EXTERNAL`.

## Independent reconstruction

I rebuilt the function carrier as base-`p` integers rather than author tuple
states.  Complete functional graphs for `p=2,3,5`, independently generated
unit-difference image sets, direction-word/endpoint keys, Jordan rank
sequences, binomial evaluation columns, and augmented anchor ranks give
**36,899 exact assertions**.  Two fresh processes reproduce the canonical
transcript byte for byte.

This confirms all image sizes and target fibres through the exhaustive boxes,
the sharp depth census and witness, unique nonzero direction-word lifts, the
transition-rank sequence `p^(p-t)-1`, every advertised zero-Jordan count, and
anchor injectivity for all nonzero steps through `p=13`.

## Proof audit

The binomial basis remains valid across the cyclic wrap because Pascal's
polynomial identity holds on `F_p`.  For every nonzero `a`, the factor
`U_a(N)` has nonzero constant coefficient, preserves each ideal layer, and
is invertible; evaluation on the one-dimensional constant kernel is a
bijection.  Backward integration therefore gives one source for each
nonzero direction word, while a forward orbit recovers that word.  This
proves both image surjectivity and the uniform nonzero fibre, with the zero
fibre following by an exhaustive source partition rather than an unproved
uniformity assumption.

The rank-one map `E=P^p` is correctly used: on `im P^t` it still has rank one,
so the nilpotent restriction has rank `p^(p-t)-1`.  Second rank differences
then give the full Jordan inventory.  The theorem is explicitly and correctly
restricted to prime fields; no unsupported extension to `F_(p^e)` occurs.

## Findings

### `P178-B-M1` — Minor — author-control provenance

The docstring says “Independent exact controls,” and `BUILD.md` says the
author program is “independently organized.”  Representational separation
from the scout is useful, but it is still an author-created control and not a
process-independent hostile review.  Rename the heading/docstring language
to `paper-local author-side regression control`, retaining the factual
no-import statement.  Reserve `independent` for the two review processes.

No mathematical repair was required.  The Round-1 package now labels the
program “paper-local author-side” in its docstring and all author surfaces;
the factual no-import statement remains.  The theorem source and PDF bytes
are unchanged, the author verifier replays exactly, and the paper manifest
passes 16/16 entries.  `P178-B-M1` is closed.

## Sources, collision, and release

Both citations have verified publisher/primary records and bounded claim
roles.  Fixed differences, augmentation powers, nilpotent linear systems,
image/kernel flags, and rank-to-Jordan conversion are explicitly zero credit.
The A05/P164 transfer boundary is stated, and only repeated state-selected
directions plus anchored inverse words are retained.  The exact-literal
non-hit is correctly called `OWNER_THIN`, never novelty.  External lifecycle
must remain `HOLD_EXTERNAL`.

## Reopened kill switches

An unanchored inverse line, a non-observable direction word, failure at
`t=p`, a transferred P164 fixed tail, a prime-power overclaim, or a direct
literal owner would kill or shrink the paper.  None fired.  Two fresh
Reviewer-B processes reproduce the 36,899-assertion canonical transcript,
and the deterministic post-repair build preserves the prime-only theorem and
`HOLD_EXTERNAL`.  There are no open Reviewer-B findings.
