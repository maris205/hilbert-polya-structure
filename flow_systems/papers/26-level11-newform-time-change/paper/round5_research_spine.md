# P26 Round-5 paper-facing research spine

## Candidate paper contribution

The strongest defensible paper is now an owner-to-obstruction theorem chain
for a level-11 newform time change:

1. the time variation of a closed orbit is the period of a globally descended
   real newform 1-form;
2. that period is owned by an oriented `Gamma_0(11)` conjugacy class and is
   linear under traversal repetition;
3. the prime-to-11 Hecke correspondence sends one source cycle to a finite
   sum of explicitly owned closed geodesics whose periods sum to `a_p` times
   the source period;
4. the Hecke permutation-cycle degree is not the zeta repetition index, even
   when an output owner has length `d` times the source length;
5. the log-zeta first variation is an owner-length weighted sum in which the
   repetition factor cancels the `1/r` logarithmic coefficient;
6. the canonical oriented product has exact zero first variation because
   inverse primitive orbits have equal length and opposite 1-form period; and
7. a noncanonical one-sided orientation choice still does not inherit an
   Euler recurrence from the Hecke period sum: it additionally requires
   degree-wise period moments that are absent from the correspondence theorem.

This result is stronger and cleaner than a numerical mismatch.  It identifies
two independent obstructions: orientation pairing kills the canonical first
variation, while length-kernel weights block the proposed Hecke lift on an
orientation half-ledger.

## Proposed result order, after Stage-2 authorization

1. Freeze the positive time change and prove the orbit-period formula.
2. Prove conjugacy, inverse-orientation, and repetition ownership.
3. State the Ruelle reciprocal-product convention and the frozen-stability
   Selberg-type convention.
4. Derive both log-zeta first-variation formulas.
5. Prove the inverse-orientation exact-zero theorem.
6. Freeze the prime-to-level Hecke normalization and prove the cycle-sum
   eigenperiod theorem.
7. Separate Hecke cycle degree `d` from zeta repetition `r`.
8. Prove the degree-moment criterion by `q` expansion and Mobius inversion.
9. Present the Round-4/5 exact and numerical ledgers and reproducibility
   receipts.
10. Close with the genus-one control theorem and the no-Euler scope verdict.

## Claim ladder

```text
[PROVED]
  time-change period law;
  conjugacy/orientation/repetition owner;
  Hecke cycle-pushforward period relation;
  Ruelle and frozen-Selberg log-zeta first-variation formulas on finite or
    absolutely convergent owner families;
  exact inverse-pair cancellation;
  degree-moment necessary-and-sufficient criterion;
  genus-one same-owner control relation.

[NUMERICALLY_CERTIFIED]
  138 finite Hecke cycle-owner instances primitive in the exact root search,
  without claiming full cross-instance `Gamma_0(11)` conjugacy deduplication;
  1,104 orientation/repetition bookkeeping rows;
  110 degree-moment rows and 165 frozen one-sided zeta rows generated
    deterministically.

[NUMERICAL_OBSERVATION]
  Round-4 period quadratures and the resulting weighted Round-5 residuals;
  51/55 alpha groups and 53/55 control groups violate the all-s moment
    conditions at the frozen tolerance.

[STOP_SCOPED]
  using the cohomological Hecke relation as discriminative evidence for a
  primitive dynamical Euler product;
  using a positive-word orientation half-ledger as a canonical global zeta.

[OPEN / NOT_ESTABLISHED]
  complete primitive Gamma_0(11) conjugacy enumeration;
  an intrinsic orientation-even twist with a nonzero first variation;
  global time-changed zeta convergence/continuation;
  primitive Euler factorization or automorphic-L determinant identity;
  Route-A A2 and Route B.
```

## Manuscript gate

ARS remains at Stage 1.  This is a research spine, not a manuscript draft.
Round 5 supplies a paper-worthy central theorem and a sharp negative result,
but it does not authorize Stage 2 or a formal Route tuple.
