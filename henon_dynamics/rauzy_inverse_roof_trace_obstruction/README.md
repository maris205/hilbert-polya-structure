# HCS-C30: Rauzy inverse-roof and trace obstruction

## Outcome

This round tests the largest open gate left by HCS-C29: can its formal inverse
arrows and exact identity-holonomy cycles be promoted to a genuine reversible
Rauzy/AGY dynamics with positive time and a dynamical trace formula?

The answer is **no for the proposed promotion**, for three independent
reasons.

1. The exact C25 and C26 words have no orbit in the source positive length
   cone.  Both the genuine \(B^{-\mathsf T}\) length action and the separate
   contravariant \(B^{\mathsf T}\) transfer action fail in every cyclic phase.
2. A real additive groupoid time cocycle changes sign on inverse arrows.  A
   positive symmetric edge length is a valid new graph clock, but it is not
   the AGY roof or the natural extension of that roof.
3. If forward and inverse arrows are represented as bounded inverses on one
   infinite-dimensional space, the finite edge Hashimoto operator cannot be
   compact or nuclear.  Enlarging the branch domain instead turns each raw
   identity word into a full neutral fixed family with
   \(\det(I-Dh_W)=0\), outside the standard isolated-orbit flat-trace formula.

The C29 finite-Weil/group-von-Neumann determinant is **not** invalidated.  It
remains a correct nonconstant determinant germ for a newly declared symmetric
non-backtracking graph suspension.

## Exact chronology gate

The three matrix actions are frozen separately.

| Word | Length action | Transfer action | Raw covariant control |
|---|---:|---:|---|
| C25 \(C_1\), length 6 | 6/6 phases infeasible | 6/6 phases infeasible | positive witness \((1,2,1,1)\) |
| C25 \(C_2\), length 6 | 6/6 phases infeasible | 6/6 phases infeasible | positive witness \((1,1,3,1)\) |
| C26 \(W_{24}\), length 24 | 24/24 phases infeasible | 24/24 phases infeasible | infeasible |

Every failure has a canonical exact integer Farkas descriptor.  For example,
the C26 forward-length phase zero contains the required row

\[
(-11430,-460520,-3353,-456200),
\]

while its transfer phase zero contains

\[
(-984333,-498163,-999116,-479060).
\]

Both are negative on every positive vector.  No floating-point optimizer or
small-prime scan is involved.

## Identity and clock boundary

A reduced word with matrix holonomy \(B_w=I\) need not be the unit arrow of
the path groupoid.  Consequently an arbitrary edge cocycle need not vanish on
C1 or C2.  The projective normalizer does vanish conditionally wherever every
prefix is defined, because it factors through the matrix action:

\[
\sum_k r_{B(e_k)}(x_{k-1})
=\log\frac{\ell(B_wx)}{\ell(x)}=0.
\]

This produces a sharp analytic fork:

- with the intrinsic signed normalizer, repetitions have zero period and the
  flow Euler repetition series diverges;
- with unit graph length, repetitions have lengths \(6m\) or \(24m\) and the
  finite Hashimoto germ is regular, but the dynamics has changed.

## Route-A decision

For the C29-to-AGY dynamical/operator promotion,

```text
(A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FORMAL_HINT)

overall: ROUTE_A_REJECTED_FOR_DYNAMICAL_PROMOTION
```

Route B is not authorized.  The decision is scoped: C29's finite algebraic
result survives.

## What is genuinely new in this round

- raw source-level identity replay, not merely a finite-Weil image;
- complete cyclic-phase cone certificates for two distinct dynamical actions;
- an explicit positive raw-homology control showing why chronology labels
  matter;
- the identity-arrow/identity-holonomy/zero-projective-period trichotomy;
- a same-space compact-ideal theorem and a positive-domain/neutral-family
  flat-trace dichotomy tailored to the C29 witnesses.

The novelty claim is search-bounded.  General Rauzy induction, symbolic
suspensions, flat traces, and stable--unstable pinning operators are prior art.

## Nonduplicative next move

The next round should not rebuild a generic Fried/Rugh operator.  The local
project `henon_pinning_trace_obstruction` already certifies the Hénon \(H_6\)
mixed domains and one-step BPS pinning kernel.  The next large door is one of:

- a quantitative all-word composition and determinant-tail theorem for that
  existing hyperbolic pinning system;
- a genuinely new twist or graded cancellation theorem on the same source
  dynamics;
- a different dynamics whose base return remains hyperbolic while only the
  fibre holonomy is the identity.

Longer formal inverse words and larger prime scans are explicitly not the next
move.

## Project map

- `RESEARCH_QUESTION.md` -- selected question and stop/go rule;
- `METHODOLOGY_BLUEPRINT.md` -- exact design and validity controls;
- `DEVILS_ADVOCATE_CHECKPOINT1.md` -- adversarial scope review;
- `DERIVATION_PACKAGE.md` -- detailed derivations;
- `THEOREM_PACKAGE.md` -- theorem statements and proof boundaries;
- `FINAL_CHECKPOINT.md` -- stop/go decision and next large door;
- `SOURCE_BOUNDARY.md` -- local prior-work and literature boundary;
- `SOURCE_VERIFICATION.md` -- claim-to-primary-source audit;
- `route_a_evaluation.yaml` -- frozen Route-A record;
- `evaluations/route_a/hcs_c30/` -- immutable accumulation copy of that record;
- `code/` -- producer, independent checker, tests, runner, and manifest tool;
- `results/` -- certificate, checker report, results, and validation reports;
- `paper/` -- manuscript source and compiled note.

Reproduce the exact release from any working directory with

```bash
/absolute/path/to/rauzy_inverse_roof_trace_obstruction/code/run_c30.sh
```
