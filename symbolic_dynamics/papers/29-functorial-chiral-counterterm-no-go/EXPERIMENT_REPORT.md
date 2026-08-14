# Experiment Report — SD-C31

## Outcome

The exact authority suite supports

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

with `ROUTE_A_REJECTED`, Route B locked, and no target-zero data.  The positive
result is an exact classification of the diagonal divergent germ and its
summable finite-scheme freedom.  The decisive failure is that every retained
mixed or fourth-order pair invariant is reproduced by mutated, composite, and
generic controls.

## Raw exact census

| Artifact | Rows/checks | Result |
|---|---:|---|
| baseline pair ledger | 76 | all mixed and B4 coefficients nonzero |
| control pair ledger | 47 | 18 mixed and 18 B4 coefficients nonzero |
| scheme shift ledger | 15 | all atom-local, relabel-natural, prefix-additive |
| coefficient grid | 49 | zero arithmetic-selective solutions |
| determinant powers | 4 | B2 wholly deleted; B4 first visible |
| route gates | 5 | frozen tuple reproduced |
| comparison table | 7 | three baselines plus four controls |
| independent evaluator | 602 | 602/602 PASS |
| regression tests | 23 | 23/23 PASS |

These are exhaustive finite identities, formal frequency/radical ledgers, or
exact theorem certificates.  Means, standard deviations, confidence
intervals, sampled phases, and target-zero error metrics do not apply.

## Exact finite-part ambiguity

At `eta=2`, with `C_eta` factored out, the source-locked divisibility Gram is

    g_pp = 1 + p^(-4),
    g_pq = 1 / ((p^4+1)(q^4+1)).

At each of the three cutoffs the exact diagonal identity is

    D_N = H_N + S0_N,
    H_N  = 2 sum_(p<=N) 1/p,
    S0_N = 2 sum_(p<=N) p^(-5).

Thus full-diagonal subtraction leaves only the mixed ledger, while leading-
harmonic subtraction leaves `S0+mixed`.  Their difference is positive and
absolutely summable.  Fifteen frozen rational combinations of `S0,S1,S2`
demonstrate additional compatible local finite shifts.  Naturality and cutoff
convergence therefore fix only the divergent germ and do not choose a unique
finite part.

This is a sharp-cutoff/Hadamard-style source finite part, not a zeta trace.
No meromorphic, heat-kernel, Wodzicki, Dixmier, or relative determinant
calculus is imported.

## Local selectivity no-go

Every source-atom pair has the same tested pointed local type: two
incomparable covers sharing the bottom.  For a universal pair-local
counterterm coefficient `beta`, the residual coefficient is `1-beta`.

    preserve divisibility baseline  => beta = 0,
    cancel a nonzero same-type control => beta = 1.

The symbolic constraints are inconsistent.  The preregistered 49-row rational
grid independently contains zero solutions.  The four control classes have
respectively 3, 2, 4, and 9 nonzero mixed pairs, so the contradiction is not a
zero-fixture artifact.

The conclusion is scoped to quadratic, additive, pair-local rules linear in
native Gram contractions.  Arbitrary global/nonlocal invariants of a filtered
tower remain outside the theorem.

## Determinant ownership

The inherited honest analytic object is `det3(I-zB_s)` on
`1/3 < Re(s) < 2/3`.  It deletes powers one and two in full; block parity
makes power three vanish; B4 is the first visible coefficient.  Ordinary
Fredholm determinant and `det2` remain unavailable at the critical object.

After declaring a finite-part scheme one may form

    D_ren = det3(I-zB_s) exp[-z^2 FP Tr(B_s^2)/2].

This is a new scheme-dependent holomorphic functional.  Changing schemes
multiplies it by a nontrivial zero-free entire scalar.  Reflection and
holomorphy survive, but neither determinant ownership nor arithmetic
selectivity improves.

## Observation → interpretation → implication → next step

1. Observation: `D=H+S0` exactly and `S0` is nonzero with a rational vanishing
   tail. Interpretation: full and leading subtraction are equally compatible
   but inequivalent. Implication: the finite part is not canonical. Next step:
   require an independently sourced uniqueness axiom before naming a preferred
   regularization.
2. Observation: every control family retains a mixed/B4 pair ledger.
   Interpretation: the signal is generic oblique-projector Gram geometry.
   Implication: a universal local coefficient cannot separate arithmetic and
   controls. Next step: require a genuinely global higher invariant with exact
   control vanishing.
3. Observation: restoring B2 changes det3 by a scheme-dependent entire
   exponential. Interpretation: analytic symmetry is cheaper than determinant
   ownership. Implication: A2 remains inherited only. Next step: do not promote
   `D_ren` to an ordinary determinant.

## Reproducibility and boundary

The canonical runner clears only this paper-local `results/` directory before
each of two runs, sets deterministic Python environment variables, regenerates
all ledgers, runs the source-separated evaluator and tests, compares artifact
hashes, rejects CRLF/control bytes/caches, audits the strict paired-pending
Route-A provenance, and freezes the code/result SHA ledger.  It performs no
Git operation.

SD-C31 does not claim a universal natural-counterterm no-go, an ordinary B2
trace, `det2`, a fixed Hilbert--Polya operator, target-zero agreement, or any
implication for RH.

## Paper 30 minimum obligation

Construct one globally source-derived higher incidence cumulant or
cohomological invariant, prove uniqueness/canonicity, and show exact vanishing
on mutated-cover, composite-only, seeded generic-DAG, and random-inventory
controls while retaining a nonzero divisibility signal.  Otherwise close the
chiral-incidence/counterterm branch.  Route B remains locked.
