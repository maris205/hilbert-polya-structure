# Paper 12 standalone-strength amendment v4

Date: **2026-08-15 (Asia/Shanghai)**

Status: **SUBMITTED FOR EXACT-BYTE METHODOLOGY / DEVIL / SOURCE RE-LOCK**

## 1. Trigger and supersession boundary

This amendment supersedes v3 only as the proposed standalone repair.  It
does not alter any proved v2 statement or any frozen v2/v3 review.  The v3
single-orbit construction is retained as the one-orbit special case of the
new common-stabilizer construction.

The new centre is not the standard `R/H` quotient by itself.  It is the
comparison between the actual indiscrete packet groupoid and a canonical
orbitwise standardization, including the exact change in degree-one
continuous cohomology and its symmetry-invariant diagonal.

## 2. Common-stabilizer source category

Define `C_common` to have objects

```text
(G_actual=X_indisc rtimes R,c),
X nonempty with the single global indiscrete topology,
x dot t a jointly continuous right R-action,
c(x,t)=t,
Stab_R(x)=H=LZ for every x in X, with L>0.
```

No transitivity or orbit count is assumed.  Put `Q=X/R` as a bare set.  A
morphism is a topological groupoid isomorphism `F` satisfying `c' o F=c`.
It must be proved, not assumed, that every such arrow is uniquely

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t,
```

and that it maps orbits bijectively and preserves the common subgroup `H`.

Mixed-stabilizer actions, including the existing `NONTRANS-1-2` control, are
outside `C_common`.  They remain valid controls for the generic v2 complex.
Write `C_common(H)` for the full component at one fixed lattice and
`C_common=disjoint-union_(L>0) C_common(LZ)`.  Strict morphisms cannot cross
these components because they preserve isotropy exactly.

## 3. Section-free orbitwise standardization

For an orbit `O` and any `x in O`, write

```text
q_x:R->O,       q_x(t)=x dot t.
```

Give `O` the quotient topology transported by `q_x`.  The identity
`q_(x dot u)=q_x o T_u`, with `T_u(t)=u+t`, must prove independence of the
chosen unit.  On the same underlying set `X`, define

```text
U open in Std_coprod(X)
iff U intersect O is open in O for every orbit O.
```

Thus `Std_coprod(X)` is the topological coproduct of the standard torsors
`R/H`.  The construction uses no orbit section and no topology on `Q`.

The proof obligations are:

1. every orbit is open and carries the usual compact Hausdorff `R/H`
   topology;
2. the coproduct is Hausdorff and the right `R`-action is jointly continuous;
3. it is the unique Hausdorff topology on the same `R`-set for which the
   action is jointly continuous and every orbit is open; the proof must use
   compactness of `R/H` and may not be generalized to noncocompact `H`;
4. the identity `Std_coprod(X)->X_actual` is continuous, while the reverse is
   noncontinuous whenever `X` has more than one point; and
5. no source, quotient, separated-reflection, or inherited topology is
   transported to the orbit index `Q`.

For fixed `H`, let `Tor_R^coprod(H)` be the category of nonempty topological coproducts of standard
right `R/H` torsors, all with the same lattice `H`, and continuous strictly
`R`-equivariant homeomorphisms, and put
`Tor_R^coprod=disjoint-union_(L>0) Tor_R^coprod(LZ)`. `Std_coprod` must be proved full and faithful.
The inverse `Indisc` replaces the entire unit topology by one global
indiscrete topology and forms the range-first marked action groupoid.  It
does not merely indiscretize each component separately.  The two functors
must be proved inverse under the frozen concrete convention, or equivalent
via displayed natural isomorphisms.

## 4. Automorphisms

Work in the ambient ZFC convention. For the nonempty set `Q=X/R`, freeze the canonical
abstract-group exact sequence

```text
1 -> Map(Q,R/H) -> Aut_R(Std_coprod(X)) -> Sym(Q) -> 1,
```

where `Map(Q,R/H)=(R/H)^Q` is the full Cartesian product.  The kernel consists
of independent orbit rotations, and the quotient records the permutation of
orbit components. Surjectivity onto every permutation uses the existence of
one equivariant identification for each moved torsor; this is an explicit
choice step, not extra topology.

After choosing one origin in every torsor, the sequence splits and gives a
noncanonical abstract-group isomorphism

```text
Aut_R(Std_coprod(X)) ~= (R/H)^Q semidirect Sym(Q).
```

The permutation convention is

```text
(sigma dot a)(q)=a(sigma^(-1)q).
```

No topology is placed on any automorphism group.  The splitting and wreath
coordinates are section-dependent; the topology, exact sequence, and
cohomological slope invariant below are section-free.

## 5. Standardized versus actual degree-one cohomology

Use exactly the author-defined, globally continuous, unnormalized nerve
complex `C_cnv` with the trivial real coefficient bundle, no support or
boundedness condition, and no topology on cohomology.

Put

```text
G_std    = Std_coprod(X) rtimes R,
G_actual = X_indisc rtimes R.
```

The identity on units and arrows is a continuous marked functor

```text
J:G_std -> G_actual.
```

The reverse identity is not continuous for a nontrivial owner.  Therefore
pullback has the fixed direction

```text
J^*:H_cnv^1(G_actual;R) -> H_cnv^1(G_std;R).
```

For `q in Q`, choose any `x in q` only to evaluate a representative and set

```text
rho([b])(q)=b(x,L)/L.
```

The proof must show that this value is independent of the chosen unit and
representative and defines a canonical algebraic isomorphism

```text
rho:H_cnv^1(G_std;R) ~= R^Q.
```

Surjectivity must use the globally continuous cocycle

```text
b_lambda(x,t)=lambda([x]) t
```

for an arbitrary function `lambda:Q->R`, where `Q` is discrete only as the
component index of the constructed coproduct.  Injectivity must show that a
cocycle with zero isotropy slope on every orbit is a coboundary: after a
ZFC choice of one unit `x_q` per orbit,

```text
h(x_q dot t)=b_0(x_q,t)
```

is well-defined by zero isotropy, continuous by the quotient and coproduct
topologies, and satisfies `d h=b_0` in the frozen sign convention.

It is mandatory to state

```text
B_cnv^1(G_std;R) is generally nonzero,
Z_cnv^1(G_std;R) is generally larger than {b_lambda}.
```

Only cohomology, not the full cocycle space, is identified with `R^Q`.  No
higher-degree standardized cohomology, product topology, named standard
groupoid cohomology, or Morita-invariance statement is authorized.

The already proved actual result gives

```text
H_cnv^1(G_actual;R)=R[c],
B_cnv^1(G_actual;R)=0.
```

Under `rho`, the pullback is the constant diagonal

```text
rho(J^*(lambda[c]))=(q |-> lambda).
```

Strict equivariant automorphisms act on slopes only by their permutation of
`Q`; component rotations act trivially.  V4 must prove the intrinsic equality

```text
image(J^*)
 = (R^Q)^(Aut_R(G_std))
 = {constant functions Q->R}.
```

`Aut_R` here means strict time-preserving equivariant automorphisms, not the
scaled, unmarked, or all abstract groupoid automorphisms.

## 6. Rational-Witt packet application

Deninger owns the fixed-prime packet action, clock, and common stabilizer
`H=(log p)Z` at every unit.  Paper 9 owns the actual global indiscrete packet
topology and the orbit quotient.  Those exact gates make `G_p^pkt` an object
of `C_common`.

The bare orbit set `Q=Gamma_p/R` may be identified set-theoretically with the
underlying set of Paper-9 `Q_p`.  Four records remain distinct:

```text
Gamma_p_actual       global indiscrete unit topology;
Gamma_p_std          coproduct of standard circles;
Q_p_actual           Paper-9 indiscrete orbit-quotient topology;
Q_p_disc             discrete component index induced by the coproduct.
```

No cardinality, enumeration, measure, local triviality, inherited transverse
topology, or arithmetic selectivity is inferred from `Q_p`.  The v3
single-orbit standardization is recovered on each component; the whole
packet theorem is not called transitive.

## 7. Frozen deterministic controls

Add exactly

```text
results/orbitwise_standardization_h1_controls.csv
```

using finite exact analogues: `Z` acts on `m` disjoint cycles of common order
`n`, with

```text
n in {3,5,7},      m in {1,2,3}.
```

The actual carrier has one global indiscrete topology; the standardized
carrier has the discrete topology obtained as the coproduct of the finite
cycle quotients.  The CSV has exactly these columns, in this order:

```text
record_type,n,m,orbit,basepoint,permutation,translation_vector,
open_count_actual,open_count_standard,h1_dim_actual,h1_dim_standard,
j_rank,aut_expected,aut_enumerated,basepoint_independent,joint_action_ok,
lift_descend_ok,group_inverse_ok,diagonal_ok,nonzero_coboundary_ok,
zero_isotropy_potential_ok,invariant_dim,mixed_length_rejected,
packet_schematic_only,replaces_source_proof,status
```

Rows are emitted deterministically in this order:

1. one `MODEL` row for each lexicographic `(n,m)` pair: `9` rows;
2. one `BASEPOINT` row for each `(n,m,orbit,basepoint)`: `90` rows;
3. one `AUT` row for every permutation of `m` components and every vector in
   `(Z/nZ)^m`, lexicographically: `3151` rows; and
4. two `NEGATIVE` rows, in order: mixed cycle lengths and wrong pullback
   direction.

The file therefore has exactly `3252` body rows.  For each model the expected
strict automorphism count is `n^m m!`; the actual and standardized first
cohomology dimensions are respectively `1` and `m`; the diagonal matrix has
rank `1`; and the invariant dimension is `1`.  Controls must include a
nonzero coboundary with zero cycle sums and explicit recovery of a potential
from a zero-isotropy cocycle.  Mixed cycle lengths must be rejected from
`C_common`.

The complete package after this amendment has exactly `11` CSV files and
`3486` body rows.  At least `96` meaningful unit tests are required.  The
existing strict verify-only, implementation/lock/gate/manifest drift,
extra/missing/tamper, two-fresh byte identity, recursive-entry, and no-cache
contracts remain mandatory.  Finite controls do not prove the real,
infinite-`Q`, choice, source, or topology theorems.  Packet rows remain
`packet_schematic_only=true` and `replaces_source_proof=false`.

## 8. Source, novelty, Route, and standalone gates

A new exact-byte source audit must bind authoritative records for topological
coproducts, standard `R/H` quotients, action groupoids over `B R`, orbitwise
automorphisms/wreath products, and the nearest transitive groupoid
cohomology comparator.  Gepner--Meier Proposition 2.15 is a mandatory nearest
precedent for the formal lift/descent step, with its compactly generated weak
Hausdorff domain mismatch stated.  Guillou--May, Alp--Wensley, and Mackenzie
must be used only at their exact finite/transitive/comparator ceilings.  The
only negative wording is `SUPPORTED_WITHIN_SEARCH`; no priority claim is
allowed.

Keep `DEN-EF-STANDARD-PERIOD-QUOTIENT-P` as the one-orbit standard
isomorphism-class proxy and pointed shadow only.  Add the separate Route
owner

```text
DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P
```

for the comparison `J_p:G_p^std->G_p^actual`, with parameters `p`, the bare
orbit set `Q_p`, and `H=(log p)Z`.  It receives no topology, cardinality,
enumeration, trace, completion, determinant, or separated-reflection credit.
All existing A-coordinate ceilings and `Route_B_invocation=false` remain.

`STANDALONE_PASS` requires the proved v2 package, the v4 orbitwise
standardization/equivalence and automorphism exact sequence, the exact
standardized `H^1` computation, the diagonal/invariant theorem, updated
controls, the targeted source audit, and independent closure of the prior
routine-reduction Major.  Topology plus a wreath-product formula without the
cohomological comparison is insufficient and leaves `NOTE_OR_MERGE` binding.

## 9. Phase boundary

This amendment authorizes no proof, code, Route YAML, manuscript, or release
work until three independent exact-byte re-locks and the targeted source gate
return zero findings on the same final tuple.
