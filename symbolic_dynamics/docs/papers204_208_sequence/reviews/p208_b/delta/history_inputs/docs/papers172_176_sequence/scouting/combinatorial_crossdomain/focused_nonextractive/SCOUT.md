# Focused non-extractive scout: outcome

**Date:** 2026-09-03 UTC  
**External lifecycle:** `HOLD_EXTERNAL`  
**Paper allocation:** none in this directory

## Outcome first

Eighteen genuinely different fixed-size autonomous dynamics were implemented
across permutations, words, and labelled perfect matchings.  All 45 pairs
within a common carrier family are separated by explicit exact witnesses.
The breadth verifier executes `751,158` assertions.

One system has a complete theorem package: first-frequency rotation (`FCR`)
on binary words.  Its independent verifier exhausts every word through
length 18 with `2,828,503` assertions and checks:

1. exact reduction of every pointed necklace to disjoint `+/-k` generator
   cycles;
2. pointwise transient and recurrent classification on every component;
3. complete possible-period set
   `{1,2} union {proper divisors of n at least 3}`;
4. sharp maximum tail `n-2` and exactly two deepest states for `n>=3`;
5. the complete two-branch inverse of every labelled target and fibre sizes
   `0/1/2`, including the closed fibre histogram; and
6. a primitive fixed-density Möbius formula for the fixed census.

This is not green.  P166 reduces a different literal map to the same cyclic
phase architecture and has its own `n-2` clock and target-indicator theorem.
Those shared features are zero credit.  Only FCR's constrained `+/-k`
component theorem, multiple recurrent components, proper-divisor period
inventory, two-branch fibres, and fixed census remain.  The status is exactly

```text
AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL
```

and the kill switch remains live.

## Two useful negative results

- Value-index stable reranking has strict inversion-set descent to the unique
  identity and exact identity fibre `2^(n-1)`, but its apparent short clock
  and general target fibres are unresolved.  It is killed rather than
  promoted from finite data.
- Minimum-ordered matching cross has exceptionally clean `m`-cycles and an
  `m-1` clock, but RGF encoding identifies it as the reverse-direction pair-
  partition slice of P169.  It is permanently killed.

The other fifteen controls are retractions, occupied run/sort/rerank
mechanisms, or exact spectra without a stable parameter theorem.  No green
candidate was manufactured to fill a quota.

## Reproduction

Run from the repository root:

```bash
PYTHONHASHSEED=0 python \
  docs/papers172_176_sequence/scouting/combinatorial_crossdomain/\
focused_nonextractive/breadth2.py

PYTHONHASHSEED=0 python \
  docs/papers172_176_sequence/scouting/combinatorial_crossdomain/\
focused_nonextractive/verify_fcr.py
```

The expected byte transcripts are `BREADTH2_CANONICAL.txt` and
`FCR_CANONICAL.txt`.  Combined author-side exact pressure is `3,579,661`
assertions.  Enumeration supports regression and falsification only; the
all-parameter arguments are written in `FCR_DERIVATION.md`.

## Terminal gate

No exact external owner for the literal FCR update was found in the bounded
search.  This is not a novelty claim.  A direct owner, literal P166
conjugacy, transferred mass-exhaustion proof, or verifier failure changes the
amber entry immediately to `KILL`.  No external posting, contact,
circulation, or submission is authorized.
