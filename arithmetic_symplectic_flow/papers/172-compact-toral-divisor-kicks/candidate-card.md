# Frozen compact-fibre divisor-kick candidate

**Candidate ID:** ASFS-20260915-TDK01  
**Paper ID:** 172-compact-toral-divisor-kicks  
**Version:** 1, frozen 2026-09-15 before the mathematical audit.  
**Status at freeze:** FROZEN — FULL TORAL SOURCE / PERIOD GATE TO AUDIT.

This is lane T of the authorized
[175 scope](../175-six-lane-geometric-source-frontier/candidate-card.md).
It changes the full geometric action, not a roof or parameter of 141 or 152.

## Exact object

For every integer n >= 2 let D_n = {1,...,n-1}, cyclically ordered with
d^+ = d+1 for d < n-1 and d^+ = 1 otherwise. All components are retained:

\[
M=\coprod_{n\geq2}\coprod_{d\in D_n}\mathbb T^2_{n,d},\qquad
\mathbb T^2=\mathbb R^2/\mathbb Z^2,\qquad \omega=dq\wedge dp.
\]

Each torus and each fixed-n finite union is compact. The entire countable
union M is disconnected and noncompact; its dimension is two, not zero.
Set, using only the current n and d,

\[
w(n,d)=\mathbf1_{\{2\leq d<n,\ d\mid n\}},\qquad
Q=q+p\pmod1,
\]
\[
F(n,d,q,p)=\left(n,d^+,Q,
  p+\frac{w(n,d)}{2\pi}\sin(2\pi Q)\pmod1\right).
\tag{C1}
\]

The amplitude, twist coefficient, and phase range above are fixed uniformly.
In particular d=1 is a guarded zero test for every n, including n=2; no
special prime branch is supplied. No aggregate proper-divisor count is an
input to a macrostep. Every iterate executes its current single test.

The roof is exactly tau = 1 on all M. The flow carrier is the endpoint
quotient

\[
S=(M\times[0,1])/((x,1)\sim(Fx,0)),
\]

with translation in height. No logarithmic timing or later roof adjustment
is part of this candidate. Invertibility and bidirectional completeness
must be established in the paper.

## Source, ownership, and controls

| Field | Frozen convention / audit obligation |
| --- | --- |
| Arithmetic and lineage | Prime/composite divisor-exclusion symbols -> one local witness per cyclic phase -> direct two-dimensional conservative shear coupling. The exact zero-witness source is retained from the [prior-work lineage](../../docs/prior_work/README.md), not a claimed conjugacy to a historical Logistic/Hénon map. |
| Allowed inputs | All integers n >= 2, current phase d, elementary divisibility, the displayed fixed sine and linear shear. No prime table, prime-only fibre, completed prime mask, zero data, fitted coefficients or supplied target lengths. |
| Coding | Conserved n and the complete phase d; observation w(n,d) along this same map. It is a finite witness scan, not a Markov conjugacy or chronological all-prime generator. |
| Geometry and measure | Full toral coordinates, normalized Haar area one per torus, counting over components. Total measure is infinite; no finite invariant probability is asserted. Global smooth inverse and symplecticity to check. |
| Primitive convention | Least positive full-state period under F, then oriented cycles modulo cyclic phase. All geometric coordinates and all phase representatives count; no centre, rational-point, or prime-only restriction. Unit suspension times are full-state periods, with repetitions rT. |
| First test | Audit the complete state with q=p=0 for every phase and an actual composite n=4. Any composite primitive orbit refutes the proposed prime-exclusive ledger. |
| Full-fibre test | Check whether prime zero-witness fibres retain continuous periodic families; do not infer their multiplicity from a symbolic phase list. |
| Monodromy | Derivative of this same F along any explicitly proved cycle; global periodic-set classification is OPEN and not required after a decisive counterexample. |
| Arithmetic controls | Suppressed witnesses, an all-one witness comparator, and actual composite input. Preserve the source dependence away from a common invariant point. |
| Geometric / ownership controls | Full torus versus a selected centre; fixed unit roof versus a prohibited post-audit logarithmic replacement; distinguish compact fibres from a compact all-integer carrier. |
| Analytic owner | No operator, trace, zeta or determinant constructed. Ordinary full-ledger product may only be considered after the early source/period gate; no object may be borrowed. |
| Future owner | Hamiltonian/contact/quantum lift DEFERRED. The three-dimensional suspension is not thereby symplectic or Hamiltonian. |
| Formal Route | UNASSIGNED; Route B NOT INVOKED. Only owner-level P0 and decisive A0/period checks are authorized here. |

## Collision boundary and precommitted decision

[140](../140-cyclic-divisor-counter/paper.md) and
[141](../141-divisor-counter-henon-lift/paper.md) use a complete finite
counter and, in 141, a noncompact hyperbolic plane. Equation (C1) has neither
and instead couples each test directly to compact toral coordinates.
[152](../152-coupled-witness-henon-escape/paper.md) aggregates all tests into
each four-dimensional update, unlike this genuine serial scan.
[033](../033-wheel-packet-symplectic-thickening-screen/paper.md) and
[052](../052-hyperbolic-wheel-packet-lift/paper.md) supply full-multiplicity
controls, not theorems for this map. The present carrier is specified before
the periodic audit; it is not a selected finite packet thickened afterwards.

Stop the prime-exclusive / prime-log target at the first owned counterexample.
Retain any proved source and symplectic construction. Do not run large orbit
enumerations, invoke general compact-surface theorems, change the roof, or
claim that all compact conservative lifts are impossible.

## Post-audit disposition (same version-1 object)

**Status:** STOP — OWNED COMPOSITE CYCLES AND CONTINUOUS PRIME FAMILIES.

The [paper](paper.md) proves the full symplectic and complete unit-flow
owner, an actual primitive composite n=4 cycle, and continuous prime
zero-momentum orbit families of time p-1. The exact source coupling is
retained, but this candidate's prime-exclusive / finite-multiplicity /
prime-log target is stopped. No field in (C1), carrier, phase range or roof
changed during the audit. Formal Route coordinates UNASSIGNED; Route B
NOT INVOKED. Global periodic classification and analytic development are
not pursued after the decisive counterexamples.
