# P26 Round-4 paper-facing research spine

## Candidate paper contribution

The strongest defensible paper is now a theorem-and-obstruction study of a
level-11 newform time change:

1. the period variation is owned by an oriented `Gamma_0(11)` conjugacy class;
2. the correctly normalized Hecke correspondence sends that owner to a finite
   sum of explicitly owned closed geodesics;
3. the sum of their newform periods is exactly `a_p` times the original period;
4. the finite Round-4 sample certifies all 138 resulting cycle-owner instances
   as primitive in `Gamma_0(11)`, without full cross-instance conjugacy
   deduplication; and
5. the genus-one cohomology control proves that this Hecke identity alone is
   not selective enough to imply a primitive dynamical Euler factorization.

This is a clear advance over a numerical period pattern: it states precisely
what Hecke owns, what is summed, and why the natural control also passes.

## Proposed result order, after Stage-2 authorization

1. Define the positive time change and prove its first-variation formula.
2. Prove conjugacy, orientation, and repetition ownership.
3. Freeze the prime-to-level Hecke normalization.
4. Prove the cycle-pushforward eigenperiod theorem.
5. Give the right-action permutation and closed-owner construction.
6. Present the finite exact/numerical ledger and reproducibility receipt.
7. Prove the genus-one same-owner control theorem.
8. State the obstruction to reading the sum-valued identity as primitive
   Euler factors.

## Claim ladder

```text
[PROVED]
  conjugacy/orientation/repetition owner;
  Hecke cycle-pushforward period relation;
  genus-one same-owner control relation.

[NUMERICALLY_CERTIFIED]
  385 exact branch-gluing rows;
  320 exact coefficient rows;
  138 finite cycle-owner/primitivity certificates.

[NUMERICAL_OBSERVATION]
  55 direct complex period checks at two configurations.

[STOP_SCOPED]
  treating the cohomological Hecke relation as discriminative evidence for
  a primitive dynamical Euler product.

[OPEN / NOT_ESTABLISHED]
  single primitive-orbit recurrence;
  global primitive-class decomposition;
  first-variation dynamical-zeta Hecke identity;
  Euler product or automorphic-L determinant;
  Route-A A2 and Route B.
```

## Manuscript gate

ARS remains at Stage 1, so this file is a research spine rather than a draft.
Round-5 disposition: the smallest zeta-variation algebra has now been carried
out.  It proves exact inverse-orientation cancellation for the canonical
product and a separate degree-moment obstruction for a one-sided audit.  The
current paper-facing structure is in `round5_research_spine.md`.
