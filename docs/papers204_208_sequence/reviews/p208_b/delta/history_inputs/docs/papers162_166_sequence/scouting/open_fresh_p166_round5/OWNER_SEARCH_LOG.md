# P166 Round-5 owner and internal-collision log

Search frozen: 2026-09-03  
Outcome: **KILL_ALL / HOLD_EXTERNAL**.

This was a bounded owner gate, not a novelty certification.  Search misses
are recorded only as misses.  The exact map, its temporal theorem, its inverse
axis, and its proof engine were searched separately where a candidate had a
credible spine.

## XCT

Literal/dynamical queries included:

```text
"xor centroid" subset translation dynamics
map subset A to A + sum A finite vector space dynamics
Boolean function support sum translation self map finite field
"sum of all elements" subset "F_2^n" translation
zero-sum subsets elementary abelian 2 group fixed translation enumeration
Boolean functions translation orbit support XOR sum
```

No direct source for the literal self-map was returned.  This is only a
bounded non-hit.  Its static refined census is directly inside:

- J. Li and D. Wan, “Counting subset sums of finite abelian groups,” Journal
  of Combinatorial Theory A 119 (2012), 170--182,
  <https://doi.org/10.1016/j.jcta.2011.07.003>.  The paper gives explicit
  fixed-cardinality subset-sum counts in finite abelian groups; author copy:
  <https://www.math.uci.edu/~dwan/liwan4.pdf>.
- M. Shi, D. S. Krotov, X. Li, and P. Solé, “Zero sum sets in abelian groups,”
  <https://arxiv.org/abs/2102.00011>.  It states that the cardinality
  distribution of zero-sum sets is completely determined and notes the
  elementary-abelian cases.

Thus the character-extraction formula in XCT is zero-credit background.
Internally, P162 is decisive.  Its headline inverse result is an
arbitrary-target translation-stabilizer polynomial, followed by stabilizer
recovery.  XCT's `2^n` odd-target fibre uses triviality of an odd set's
translation stabilizer; its extra nonzero-centroid fixed states are counted as
translation-invariant pair unions.  The deterministic forward action differs
from P162's random intersection, but the only plausible independent inverse
axis is the occupied P162 engine.

Decision: `KILL_INTERNAL_P162_TRANSLATION_STABILIZER_FIBRE_ENGINE`.

## BND

Queries included:

```text
topological boundary operator iteration boundary boundary fixed
Kuratowski boundary operator monoid
boundary operator powers topological space
topological boundary satisfies boundary cubed boundary squared
```

Primary/current operator sources:

- S. Plewik and M. Walczyńska, “The monoid consisting of Kuratowski
  operations,” Journal of Mathematics (2013),
  <https://doi.org/10.1155/2013/289854>.
- M. Bowron, “Boundary-Border Extensions of the Kuratowski Monoid,”
  <https://arxiv.org/abs/2210.10928>.  It explicitly adds the boundary
  operator and studies the resulting operator monoid and its collapses.

The identities that a boundary is closed and that iterated boundaries
stabilize after the second boundary are definition-level topology.  Round 2's
CGP and the geometry/topology BPD kill also bar a finite-topology carrier from
being used to disguise a standard set operator.  The small-box fibres do not
have a uniform target formula.

Decision: `KILL_DIRECT_OPERATOR_PLUS_NO_TARGET_ATLAS`.

## ZAT

Queries included `pointed quiver representation vector dynamics zero
trigger`, `quiver representation marked vector update along arrow`, and
`finite field guarded linear assignment dynamics`.  No literal source was
returned.  The non-hit is immaterial: for each fixed arrow, the map is simply

```text
if v=0 then v:=Au else hold,
```

and becomes idempotent after one evaluation.  Rank decorates counts but does
not drive the dynamics.  P99's shear and the portfolio's generic one-step
projection firewall are sufficient internal controls.

Decision: `KILL_GUARDED_ONE_STEP_PROJECTION`.

## EOD

Queries included `exactly one threshold Boolean network incidence matrix`,
`complement singleton symmetric design`, and `2-(v,v-1,v-2) design`.  Design
complementation and incidence parameters are standard; for example the
standard relation that a symmetric design's complement has parameters
`(v,v-k,v-2k+lambda)` is summarized in the design literature.  One accessible
design reference located by the search is:

- T. Nilson, *Design Theory* notes, including incidence matrices and
  complements of symmetric designs:
  <https://apachepersonal.miun.se/~tomnil/designs/designsShortC.pdf>.

For this degenerate design, the update reduces exactly to the three
cardinality cases in `SCOUT.md`.  It is therefore a totalistic exact-one
threshold network, not a design-dynamical theorem.  P80 (majority on the
cocktail-party graph), P106 (synchronous polarity network), and P118 (mex
network) are internal Boolean-network controls.

Decision: `KILL_TRIVIAL_DESIGN_PLUS_THRESHOLD_NETWORK_COLLISION`.

## NIM

Queries included `Bouton Nim two piles equal heaps winning strategy`,
`canonical winning move two-pile Nim`, and `Nim original 1901 paper`.

- C. L. Bouton, “Nim, a game with a complete mathematical theory,” Annals of
  Mathematics 3 (1901--1902), 35--39.  A transcription of the original is at
  <https://en.wikisource.org/wiki/Nim%2C_A_Game_with_a_Complete_Mathematical_Theory>.

For two heaps, reducing the larger heap to the smaller is exactly the
classical move to nim-sum zero.  Treating this optimal policy as an endomap
adds only an idempotent projection and a box-boundary fibre count.

Decision: `KILL_DIRECT_BOUTON_STRATEGY_PLUS_IDEMPOTENT_PROJECTION`.

## GSR

Queries included:

```text
oriented matroid covectors sign reversal reorientation
global sign reversal signed covectors
state dependent reorientation oriented matroid dynamics
covector central symmetry oriented matroid
```

- J. Folkman and J. Lawrence, “Oriented matroids,” Journal of Combinatorial
  Theory B 25 (1978), 199--236,
  <https://doi.org/10.1016/0095-8956(78)90039-4>, is foundational primary
  ownership of the sign-vector/covector setting.
- Reorientation is standard enough to support specialized work such as
  Goddyn--Hliněný--Hochstättler, “Balanced signings and the chromatic number
  of oriented matroids,” <https://doi.org/10.1017/S096354830500742X>.

The literal feedback map was not located, but it either fixes a sign vector or
applies the single central involution `s -> -s`.  All functional-graph and
fibre formulas are the same two-element orbit calculation.  Earlier OZP used
the same full signed-cube carrier with a different update, and P102/RTCD
occupy involution-driven algebraic functional graphs more broadly.

Decision: `KILL_THIN_STATE_DEPENDENT_CENTRAL_INVOLUTION`.

## DLR

Queries included:

```text
Latin square diagonal permutation row permutation dynamics
Latin square state dependent isotopism diagonal
cycle structure autotopisms quasigroups Latin squares
row isotopism diagonal Latin square
```

- D. S. Stones et al., “Cycle structure of autotopisms of quasigroups and
  Latin squares,” <https://arxiv.org/abs/1509.05655>, studies cycle structure
  of row/column/symbol permutation symmetries.
- Stones et al., work on reduced Latin squares and autotopisms uses the same
  row-permutation/isotopism action language; author copy located at
  <https://users.cecs.anu.edu.au/~bdm/papers/ls_final.pdf>.

No exact diagonal-feedback owner was returned.  Exhaustion already kills it:
orders three and four have qualitatively different functional graphs, and the
order-four fibre spectrum is `1,3,5` with an isolated 3-cycle.  There is no
all-parameter temporal or target theorem to take to a deeper owner gate.
Prior LPS and Latin intercalate-walk scouts reinforce the action-density risk.

Decision: `KILL_NO_ALL_PARAMETER_SPINE_PLUS_LATIN_ACTION_OWNER_DENSITY`.

## Aggregate ruling

| candidate | direct/static source subtraction | internal collision | ruling |
|---|---|---|---|
| XCT | fixed-weight subset sums | P162 translation/stabilizer inverse axis | KILL |
| BND | boundary/Kuratowski monoid | topology/closure firewalls | KILL |
| ZAT | no search needed after thinness | guarded projection; P99 neighbor | KILL |
| EOD | trivial complement design | P80/P106/P118 threshold networks | KILL |
| NIM | Bouton | generic optimal-policy projection | KILL |
| GSR | oriented-matroid reorientation | action/involution silhouettes | KILL |
| DLR | Latin isotopism/autotopism | no spine; prior Latin scouts | KILL |

No candidate is owner-thin with two independent surviving axes.  The correct
outcome is `KILL_ALL`, not a forced P166.

