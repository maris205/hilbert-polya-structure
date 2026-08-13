# Candidate Registry

## SD-C07 — tensor-prime atom-loop shift, graded enhancement

- Family: **Symbolic Dynamics**, exclusively.
- Base object: the identity-adjacency countable shift on the tensor atoms of
  finite full shifts, with the topological-entropy roof.
- Paper-05 enhancement: tensor-divisor homology and the canonical Koszul
  degree on the same monoidal symbolic skeleton.
- Candidate identity: this is an enhancement of SD-C07, not a new
  candidate. The preregistered G4 gate failed, so SD-C08 is intentionally
  unassigned.
- Frozen tuple:
  (A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC,
  A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL).
- Overall Route A: ROUTE_A_ANALYTIC_CANDIDATE.
- Paper-05 stage verdict: SCOPED THEOREM STOP.
- Route B: locked; route_b_invocation_allowed is false.

### Exact gain

The Koszul generator attached to each tensor atom lies in degree one.
Consequently, on the purely odd one-particle transfer module,

\[
  \operatorname{Ber}(I-L_s)=\zeta(s),\qquad \Re s>1.
\]

The separate exterior-Fock supertrace remains

\[
  \operatorname{Str}_{\Lambda V}\Gamma(L_s)
  =\det(I-L_s)=\zeta(s)^{-1}.
\]

This distinction fixes the internal graded orientation once the
exterior/Koszul functor is frozen; selection of that functor on the bare
tensor monoid remains a modeling choice. It does not extend the determinant
beyond the Euler half-plane.

### Non-promotion facts

1. On the honest Koszul resolution \(A\otimes\Lambda V\), the total-mass
   transfer has supertrace \(1\) in every positive power and
   superdeterminant \(1-z\): exactness cancels all non-vacuum prime data.
2. Natural two-sided symbolic reversal sends \(L_s\) to another \(L_s\),
   not to \(L_{1-s}\).
3. Inversion in the tensor Grothendieck group sends \(s\) to \(-s\), and
   every monoidal \(\mathbb Z/2\)-parity is inversion-even.
4. Even after adversarially granting a centered
   \(s\leftrightarrow(1-s)\) pairing, the first common regularized
   determinant is \(\det_3\) on
   \(1/3<\Re s<2/3\); it is zero-free and its logarithm starts at repetition
   \(r=3\), deleting the \(r=1,2\) traces.

Canonical evaluation:
evaluations/route_a/SD-C07/20260813T230000Z.yaml.
