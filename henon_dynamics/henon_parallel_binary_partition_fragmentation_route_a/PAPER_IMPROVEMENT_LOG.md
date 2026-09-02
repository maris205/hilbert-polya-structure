# Two-round paper improvement log

## Baseline — `main_round0_original.pdf`

The original draft found the decisive binary-word coupling and stated the
complete all-parameter theorem.  It proved the full kernel, occupancy laws,
absorption CDF/mass/mean, and handled `n=1`.  Its main weakness was that the
spectral and critical-window parts were stated without the full guardrail
discussion expected of a release artifact.

## Improvement round 1 — `main_round1.pdf`

Hostile question: does triangularity actually prove diagonalizability?

Implemented changes:

- inserted the invariant rank flag `V_1 subset ... subset V_n`;
- proved `(K-lambda_k I)V_k subset V_{k-1}`;
- derived the squarefree annihilator by descending-rank lowering;
- separated algebraic multiplicity from geometric closure;
- added the logarithmic birthday expansion and its vanishing error;
- refused a global shifted limit unless the dyadic phase converges.

This round closes the largest mathematical gap and is substantively longer
than the baseline.

## Improvement round 2 — `main_round2.pdf`

Hostile question: is the package confusing a classical breaking mechanism or a
finite determinant with a new arithmetic bridge?

Implemented changes:

- added exact certificate sizes and the independent/SymPy validation split;
- named the nearest primary owner (Diaconis–Pang–Ram) and disclaimed priority;
- distinguished C194, C215, C276, and the unlabelled block-size quotient;
- spelled out all five failed Route-A rungs and the locked Route B;
- added shared-bit, biased-bit, persistent-bit, and quotient model boundaries;
- added the fixed scope literal and an AI-use statement.

The final `main.pdf` is byte-identical to this round.  No reviewer-requested
change weakened or broadened the theorem.
