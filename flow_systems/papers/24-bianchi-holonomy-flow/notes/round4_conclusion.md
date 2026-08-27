# P24 Round-4 conclusion — finite-volume cusped non-arithmetic control

## Paper-level result

Round 4 replaces the Round-3 infinite-volume Schottky surrogate with a genuine
finite-volume control in the same coarse geometric class as the Bianchi
candidate.  The frozen object is

```text
Y = S^3 \ 5_2 = m015,
flow = unit-speed geodesic flow on T^1Y,
clock = hyperbolic arclength.
```

The source-bound theorem chain proves that `Y` is an orientable, torsion-free,
finite-volume hyperbolic 3-manifold with one complete torus cusp and that its
lattice is non-arithmetic.  In particular, “finite volume” and
“non-arithmetic” are not inferred from a floating volume or an approximate
trace field.  The full source audit is in
[`round4_source_audit.md`](round4_source_audit.md).

This is a strict improvement in control validity: the shared axes are now

```text
hyperbolic dimension 3;
orientable torsion-free manifold;
finite volume and noncompact cusp geometry;
unit-speed geodesic flow and arclength clock;
primitive loxodromic classes carrying complex length and holonomy.
```

The control deliberately has no Gaussian-prime owner.  It therefore tests
whether a holonomy statistic can survive on a non-arithmetic finite-volume
cusped manifold without an arithmetic substrate.

## Executed invariant and primitive ledger

The pinned executable contract first checks that SnapPy 3.3.2 returns the
rigorous positive isometry identification `5_2 -> m015`, then records the
one-cusp topology, triangulation identifiers, group presentation, peripheral
curves, source receipts, and numerical geometric invariants.

At real-length cutoff `3.05`, the high-precision grouped ledger contains

```text
complex-length groups                    18
primitive geodesic classes by multiplicity 31
shortest real length       0.5623991486459236930...
largest emitted real length 3.0450466184664543005...
```

Every row retains a representative word, multiplicity, real length, holonomy
angle, orientation/parity, and the PSL-invariant value

```text
tr(gamma)^2 = 2 + 2 cosh(L_gamma).
```

A second SnapPy length-spectrum implementation, run independently at 106-bit
precision through real length `2.10`, emits 9 primitive classes in 6
complex-length groups.  Its multiplicity vector agrees exactly with the first
implementation, and the maximum complex-length residual is
`2.2944137070481165e-31`.

These ledger fields remain **`[NUMERICAL_OBSERVATION]`**, not interval
certificates.  SageMath's interval backend was unavailable, and the published
hyperbolicity theorem does not certify this finite length prefix.  The
implementation's primitive de-duplication semantics are pinned and tested, but
the project does not call the 31-row prefix a theorem-level complete primitive
ledger.

## What remains unmatched

The new control matches finite-volume cusp geometry, but it does not match:

- the arithmetic owner (`Y` is intentionally non-arithmetic);
- the exact cusp count or covolume of the level-`(3)` Bianchi quotient;
- generator marking or word cutoff from Rounds 2--3;
- complex-length distribution;
- a full metric primitive spectrum on either side.

Consequently no cross-system arithmetic score is reported in Round 4.  A
comparison now has the right geometric control class, but the Bianchi side is
still only an elementary-generator word ball, whereas the `5_2` rows use a
metric length cutoff.  Comparing them directly would confound enumeration
schemes.

## Route boundary and next smallest result

```text
ARS_STAGE=1_RESEARCH_IN_PROGRESS
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_ONLY
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
A2_A4_EVALUATION=NOT_EVALUATED
CROSS_SYSTEM_ARITHMETIC_VERDICT=OPEN
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

The next smallest scientifically valid step is a **same-enumeration** contract:
either produce a metric-cutoff primitive ledger for a finite quotient of the
Bianchi candidate or reduce both systems to a rigorously identical symbolic
sampling rule.  Only after that freeze may the holonomy statistic be compared.
Round 4 creates no orbit-to-prime-ideal map, no Riemann-`zeta` A0 credit, no
dynamical determinant, and no quantum/operator claim.
