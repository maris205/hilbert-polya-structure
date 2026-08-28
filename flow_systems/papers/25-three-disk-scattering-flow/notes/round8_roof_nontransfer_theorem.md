# P25 Round-8 theorem — the unit roof cannot be transferred to the physical clock

Date: **2026-08-28**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow position: ARS Stage 1 research, Route-A ownership audit
- Symbolic owner: the unit-roof three-symbol no-repeat suspension
- Physical owner: the unit-speed equilateral three-disk exterior billiard
- Frozen geometry panel: `d/a=29/5,6,31/5`
- Freeze SHA-256:
  `43393de457d985009883ab31a023c7dcf6444f9640e86d9aa969cc3993cf49a4`
- Core-output SHA-256:
  `9a29d8894b1ac81f9588fe221375bddc671898b9b08b409b0fa5a1d5a42a9014`
- Target prime/zero/resonance data: none

## Setting

Three disks of radius `a>0` have centers at the vertices of an equilateral
triangle of side `d`.  The physical flow has unit speed, so the period of an
orbit is its Euclidean flight length.  In the no-eclipse regime the trapped
collision dynamics has the no-repeat symbolic coding used in Rounds 2--7, but
the suspension roof is the physical free-flight function `tau`, not the
constant function one.

The Round-7 determinant

```text
det(I-u z A_3) = (1-2u z)(1+u z)^2
```

belongs to the collision-count clock.  A scalar substitution
`z=exp(-c s)` could transfer it owner by owner to physical time only if every
primitive word of topological period `n` had physical period `n c`.

## Theorem 1 — two exact periodic averages

`[PROVED]` The symmetric period-two owner alternating between two disks has

```text
T_2 = 2(d-2a),             T_2/2 = d-2a.
```

The symmetric period-three owner visiting all three disks has

```text
T_3 = 3(d-sqrt(3)a),       T_3/3 = d-sqrt(3)a.
```

Consequently

```text
T_3/3 - T_2/2 = (2-sqrt(3))a > 0.
```

### Proof

For the two-disk bounce, each reflection point lies on the line of centers and
the free segment is the center separation minus two radii, `d-2a`.  The closed
orbit contains two such segments.

For the three-disk orbit, symmetry places each collision point on the radius
toward the center of the center triangle.  The three collision points form an
equilateral triangle.  The difference of two adjacent inward unit-radius
vectors has length `sqrt(3)a` in the direction of the corresponding center
edge, so each free segment has length `d-sqrt(3)a`.  There are three segments.
At each collision, the inward radius is the angle bisector exchanged by the
reflection that maps the incoming edge direction to the outgoing edge
direction; because the boundary tangent is perpendicular to that radius, the
equal-angle specular reflection law is satisfied.
Finally, `2>sqrt(3)` because both sides are positive and `4>3`.  QED.

## Theorem 2 — constant-roof cohomology obstruction

`[PROVED]` The physical roof is not cohomologous to a constant on the trapped
collision shift.

### Proof

If, for some function `u` and constant `c`,

```text
tau = c + u - u o sigma,
```

then summing around any period-`n` point telescopes and gives

```text
S_n tau = n c.
```

Thus every periodic orbit would have the same mean flight length `c`.  The two
exact owners in Theorem 1 have distinct means, a contradiction.  This uses
only the necessary telescoping direction of the periodic-orbit cohomology
criterion; no numerical Livsic inference is made.  QED.

## Corollary 3 — no global scalar determinant transfer

`[PROVED]` No owner- and traversal-power-preserving scalar substitution
`z=exp(-c s)` turns the unit-roof determinant into the physical three-disk
orbit determinant.  The obstruction holds for every `d` for which the two
symmetric trapped owners exist, including all three frozen geometries.

Indeed, period two would force `c=d-2a`, while period three would force
`c=d-sqrt(3)a`.  These requirements are incompatible.  Repetitions also rule
out repairing the substitution by an owner-independent additive period
offset: physical traversal powers satisfy `T(g^r)=rT(g)`.

This result does **not** rule out a transfer operator with the genuine
nonconstant roof.  It rules out only importing the finite-dimensional
unit-roof formula by a one-parameter change of variable.

## Corollary 4 — quantitative minimax error

`[PROVED]` For every real scalar `c`,

```text
max(|c-(d-2a)|, |c-(d-sqrt(3)a)|)
    >= (2-sqrt(3))a/2.
```

This is the elementary two-point minimax bound.  Equality is attained at the
midpoint of the two exact periodic averages.  The obstruction is independent
of `d`, so changing the neighboring geometry cannot tune it away.

## Locked full-ledger replay

The theorem is proved above, not estimated from the orbit file.  The
deterministic replay nevertheless checks the exact witnesses against the
source-locked Round-2 ledger and retains all 2,241 certified physical rows.

| `d/a` | frozen owners | match `c=d-2a` | disagree | exact witness gap |
|---:|---:|---:|---:|---:|
| `29/5` | 747 | 3 | 744 | `2-sqrt(3)` |
| `6` | 747 | 3 | 744 | `2-sqrt(3)` |
| `31/5` | 747 | 3 | 744 | `2-sqrt(3)` |

The three matching rows at each geometry are exactly the three oriented
two-disk bounce owners `01`, `02`, and `12`.  The finite disagreement count is
a bounded diagnostic, not a completeness theorem beyond word length 12.

## Route-A consequence

The Round-7 tuple remains

```text
(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)
overall = ROUTE_A_REJECTED.
```

It remains owned exclusively by the unit-roof symbolic calibrator.  The new
theorem makes the ownership firewall exact: the physical flight-length flow
cannot inherit the symbolic A2 determinant through a scalar clock change.
The physical tuple remains `UNASSIGNED`; no physical root count, global
determinant, target-divisor comparison, or Route-B evaluation has run.

## Source and disclosure boundary

The no-repeat coding and the separation between semiclassical orbit products
and exact multiple-scattering determinants retain the verified source scope in
the Stage-1 brief: Gaspard--Rice
([DOI 10.1063/1.456018](https://doi.org/10.1063/1.456018),
[DOI 10.1063/1.456019](https://doi.org/10.1063/1.456019)) and Wirzba
([DOI 10.1016/S0370-1573(98)00036-2](https://doi.org/10.1016/S0370-1573(98)00036-2)).
The two length formulas, cohomology obstruction, and minimax bound are proved
in this note.  AI-assisted research and code generation were used; all machine
claims are tied to the freeze, tests, deterministic output, and receipt.
