# Paper 12 Phase-3 v4 exact-byte methodology re-lock

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent methodology / category / cohomology / reproducibility lane**  
Review mode: **read-only exact-byte re-lock; no browsing**  
Verdict: **PASS — C0/M0/m0**

## 1. Scope and independence

This review audits the final v4 design tuple only. It tests the exact object
and morphism domains, topology and choice boundaries, automorphism statement,
degree-one cohomology comparison, packet ownership, deterministic-control
freeze, Route metadata, and status/gate consistency. It does not prove a v4
target, execute or edit controls, perform the required source/novelty audit,
evaluate Route A, draft a manuscript, or authorize release.

The stable v2 mathematics and the superseded v3 reviews are immutable history.
They were used only to check that v4 neither withdraws a proved claim nor
silently treats a failed proposal as established. No active lock was edited.
The only file written by this lane is this report.

## 2. Exact-byte input receipt

The following five hashes were independently recomputed before the audit and
again immediately before this report was written.

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `dfe676ddf2532bddb4fd0613752370d3bd6c30655a6cf6621fddcfbb423babe2` |
| `notes/candidate_lock.md` | `331703b5bb68467b1a4a29bc77008782a13e8083c67d5dde1f89674731b4688d` |
| `notes/pipeline_state.md` | `be98619a4e116dc35eb90c77962798a298099ac2740b8f28fa013517bf273107` |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` |
| `notes/phase3_standalone_amendment_v4.md` | `42dee6bf70373c0d74e40264ab9f6c9d510b124e37108902fdaf5feae7befb82` |

These are the reviewed bytes. A later content or status edit requires a new
hash tuple and a fresh re-lock.

## 3. Category, topology, and equivalence audit

### 3.1 `C_common` and its fixed-stabilizer components

The object domain is exact: one nonempty set with a single global indiscrete
topology, a jointly continuous right `R`-action, normalized mark `c(x,t)=t`,
and the same stabilizer `H=LZ`, `L>0`, at every unit. Transitivity and an orbit
count are not assumed. Mixed-stabilizer actions are explicitly outside the
category while remaining valid generic-v2 controls.

The decomposition

```text
C_common=disjoint-union_(L>0) C_common(LZ)
```

has the correct quantifier. A strict marked groupoid isomorphism fixes the
time coordinate and therefore transports isotropy at the same real times;
it cannot cross two distinct lattice components. The required formula

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t
```

is a proof obligation rather than an assumption, and is sufficient to recover
the orbit bijection and the common subgroup.

### 3.2 Section-free coproduct topology

For each orbit, `q_(x dot u)=q_x o T_u` has the correct order for the frozen
right action. Precomposition by the real translation homeomorphism makes the
quotient topology independent of the unit. The global rule

```text
U is open iff U intersect O is open for every orbit O
```

then defines the topological coproduct on the same underlying set without
choosing an orbit section or topologizing the bare orbit set `Q=X/R`.

The registered proof obligations are sufficient and sharp. Each orbit is the
compact Hausdorff quotient `R/H`; the coproduct is Hausdorff; the action is
jointly continuous componentwise; and every orbit is open. Conversely, in
any Hausdorff topology on the same `R`-set with jointly continuous action and
open orbits, the induced continuous bijection `R/H -> O` is a homeomorphism
by compact-to-Hausdorff rigidity, after which the open-orbit partition forces
the coproduct topology. The lock expressly forbids a noncocompact or
non-open-orbit generalization.

The identity direction is correct: constructed standard coproduct to actual
global indiscrete is continuous, while the reverse is noncontinuous for the
nontrivial lattice owner. No inherited, quotient-index, separated-reflection,
or actual-`Q_p` topology is smuggled into the construction.

### 3.3 `Std_coprod` and `Indisc`

For fixed `H`, the target contains exactly topological coproducts of standard
right `R/H` torsors and strict equivariant homeomorphisms. Every strict source
arrow descends to such a homeomorphism, and every target arrow uniquely lifts
with the unchanged time coordinate. This closes fullness, faithfulness, and
the morphism domain.

`Indisc` is correctly frozen to replace the entire unit topology by one
global indiscrete topology, not by a coproduct of componentwise indiscrete
topologies. Retaining the same set and action makes both composites exact
under the concrete convention, or naturally isomorphic under a presentation-
independent convention. No continuity or inverse-construction gap remains in
the design.

## 4. Choice and automorphism audit

The canonical statement is the abstract-group exact sequence

```text
1 -> Map(Q,R/H) -> Aut_R(Std_coprod(X)) -> Sym(Q) -> 1,
Map(Q,R/H)=(R/H)^Q.
```

The kernel is correctly the full Cartesian product: a strict automorphism may
rotate every orbit independently, including when `Q` is infinite. The
projection to component permutations is canonical. Under the explicit ZFC
convention, surjectivity uses a family of equivariant identifications between
moved torsors.

The lock does not call the splitting canonical. Only after choosing one
origin in every orbit does it assert the noncanonical semidirect/wreath
description, and it freezes the permutation action

```text
(sigma dot a)(q)=a(sigma^(-1)q).
```

Different section choices may change the coordinates without changing the
canonical exact sequence. No topology on the automorphism group is claimed.
The same ZFC choice boundary is recorded for the family of zero-slope
potentials used in the cohomology proof.

## 5. Standardized degree-one cohomology audit

### 5.1 Domain and slope map

The theorem uses the same Paper-12 author-defined full globally continuous,
unnormalized nerve complex with trivial real coefficients. It adds no support,
boundedness, normalization, or cohomology topology. The result is restricted
to degree one.

The proposed map

```text
rho([b])(q)=b(x,L)/L
```

has the correct type. The cocycle law and conjugation within an orbit make the
value independent of `x`; coboundaries vanish on isotropy, so it is also
representative-independent. Division by the frozen positive generator `L`
normalizes the coordinate class to slope one.

For an arbitrary function `lambda:Q->R`, the cochain

```text
b_lambda(x,t)=lambda([x]) t
```

is globally continuous on the constructed coproduct because it is continuous
on every open component, with no cross-component uniformity requirement. This
correctly yields every element of the full algebraic product `R^Q`, including
unbounded functions when `Q` is infinite.

For zero slope, choosing one `x_q` per orbit and setting

```text
h(x_q dot t)=b_0(x_q,t)
```

is well-defined because the isotropy values vanish, continuous by quotient
descent on each orbit and coproduct gluing globally, and satisfies
`d h=b_0` with the frozen sign. Thus the design correctly distinguishes the
canonical cohomology isomorphism from its noncanonical primitive witnesses.

The locks explicitly prevent the two common errors: standardized
`B_cnv^1` is generally nonzero, and a general standardized cocycle need only
be cohomologous to an orbitwise time cocycle. No equality for the full
cocycle space is claimed.

### 5.2 `J`, pullback variance, and the invariant diagonal

The topology forces the registered direction

```text
J:G_std -> G_actual.
```

It is the identity algebraically from the finer coproduct topology to the
coarser actual topology. Continuous cochains are contravariant, so the fixed
map

```text
J^*:H_cnv^1(G_actual;R) -> H_cnv^1(G_std;R)
```

has the correct variance. The inherited actual calculation is one global
line even for a nontransitive globally indiscrete unit space. Under `rho`, its
class `lambda[c]` maps to the constant function `q |-> lambda`.

Strict component rotations preserve every slope, and a strict automorphism
acts on slopes through its permutation of `Q`. The common stabilizer makes
all orbit permutations available under the stated ZFC boundary. Because `Q`
is nonempty, the invariants under the full strict time-preserving equivariant
automorphism group are exactly the constant functions. Therefore the proposed
identity

```text
image(J^*)=(R^Q)^(Aut_R(G_std))=the constant diagonal
```

is correctly typed. Scaled, unmarked, or arbitrary unmarked groupoid
automorphisms are explicitly excluded. No higher-degree, Morita-invariance,
named-theory, direct-sum, or product-topology claim is licensed.

## 6. Packet and owner audit

The packet application is conditional on the exact every-unit source gate:
Deninger supplies the fixed-prime action, clock, and common stabilizer
`(log p)Z`; Paper 9 supplies the actual global indiscrete packet and its bare
orbit quotient. Only after that same-object gate does the whole packet enter
`C_common`.

The four records

```text
Gamma_p_actual, Gamma_p_std, Q_p_actual, Q_p_disc
```

remain nonconflated. The v4 bytes infer no cardinality, enumeration, measure,
local triviality, inherited transverse topology, or arithmetic selectivity
from `Q_p`. The one-orbit v3 construction survives only componentwise; the
packet is never called transitive.

## 7. Deterministic-control freeze audit

The previous underfrozen-control finding is closed. The carrier orders,
component counts, artifact name, 26-column schema, record blocks, row counts,
negative rows, package totals, and minimum test count are all frozen before
implementation:

```text
n in {3,5,7}, m in {1,2,3};
artifact: results/orbitwise_standardization_h1_controls.csv;
MODEL rows:      3*3 = 9;
BASEPOINT rows:  (3+5+7)*(1+2+3) = 90;
AUT rows:        sum_(n,m) n^m m! = 3151;
NEGATIVE rows:   2;
new body rows:   9+90+3151+2 = 3252;
package:         11 CSV files, 234+3252 = 3486 body rows;
tests:           at least 96 meaningful tests.
```

The automorphism expectation `n^m m!`, actual/standardized dimensions `1/m`,
rank-one diagonal, one-dimensional invariant space, nonzero coboundary,
zero-isotropy potential, mixed-stabilizer rejection, and wrong-variance
negative are mutually consistent. The lock also states that finite controls
do not prove the real, infinite-`Q`, choice, source, or topology theorems.
Strict verification, two-fresh byte identity, lock/gate/implementation drift,
tamper, extra/missing-file, recursion, and no-cache checks remain mandatory.

## 8. Route and gate audit

Exactly eight nonconflated Route owners are frozen:

1. generic indiscrete continuous complex;
2. actual orbit complex;
3. actual packet complex;
4. actual orbit marked period;
5. actual packet marked period;
6. one-orbit standard period proxy;
7. standardized-packet `H^1` comparison; and
8. unmarked/scaled control.

The new packet comparison owner has the correct phase-space pair
`(G_p^std,G_p^actual,J_p)` and parameters `p`, bare `Q_p`, and
`H=(log p)Z`. It is separate from the singular one-orbit proxy and receives
no `Q_p` topology/count, actual-topology transport, trace, completion,
determinant, or arithmetic-selectivity credit. The shared mandatory fields,
future artifact hashes, A-coordinate ceilings, and false Route-B invocation
remain explicit.

The stale-gate finding is also closed. `phase1_final_gate.md` is described
only as the historical v2 gate; every active v4 file says the current tuple is
pending and blocks proof, code, Route, manuscript, release, and public sync.
The v4 design gate preserves the superseded v3 findings as history without
treating them as current proof authority.

## 9. Finding register and disposition

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
V4_METHODOLOGY_RELOCK=PASS
EXACT_TUPLE_MATCH=true
CATEGORY_AND_QUANTIFIERS=PASS
SECTION_FREE_TOPOLOGY_AND_UNIQUENESS=PASS
STD_COPROD_INDISC_EQUIVALENCE=PASS_DESIGN
CHOICE_BOUNDARIES=PASS
AUTOMORPHISM_EXACT_SEQUENCE=PASS_DESIGN
NONCANONICAL_SPLITTING_BOUNDARY=PASS
STANDARDIZED_H1_PRODUCT=PASS_DESIGN
J_VARIANCE_AND_INVARIANT_DIAGONAL=PASS_DESIGN
PACKET_OWNER_GATE=PASS_DESIGN
CONTROL_FREEZE_3252_11_3486=PASS
ROUTE_OWNER_COUNT=8
STALE_GATE_FINDING=CLOSED
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
PROOF_OR_ROUTE_AUTHORIZED_BY_THIS_REPORT=false
TARGETED_SOURCE_NOVELTY_AUDIT=STILL_REQUIRED
```

**Final verdict: PASS (`C0/M0/m0`).** The current v4 bytes are methodology-
locked for the separately gated source/novelty, proof, control, and later
standalone-review lanes. This report does not itself prove a theorem or open
Route/manuscript/release work.

## Addendum — nonempty-domain exact-byte re-lock

Addendum date: **2026-08-15 (Asia/Shanghai)**  
Verdict: **PASS — C0/M0/m0**

The narrow final tuple is:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `e72aa3b82f916a3687ef2366df535599db5ab26e28e2bce66f4a54110b9850f7` |
| `notes/candidate_lock.md` | `7b6b6e97ced6e5b3f39e7da44f852fb1aeea06826fc0a79f807eaf16579b4700` |
| `notes/pipeline_state.md` | `be98619a4e116dc35eb90c77962798a298099ac2740b8f28fa013517bf273107` |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` |

Relative to the tuple reviewed above, the sole semantic change is explicit
closure under the already-frozen nonempty source domain: target coproducts
are nonempty and `Q=X/R` is nonempty. This removes the empty target object
that `Indisc` could not send into `C_common`, and it excludes the empty-`Q`
case in which the diagonal `R -> R^Q` would not be injective. Pipeline and
design-gate bytes are unchanged. All prior category, topology, choice,
automorphism, `H^1`, `J^*`, packet, control-count, Route, and stale-gate PASS
checks regress unchanged.

```text
NONEMPTY_DOMAIN_ISSUE=CLOSED
SEMANTIC_DELTA=NONEMPTY_TARGET_COPRODUCT_AND_Q_ONLY
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
V4_METHODOLOGY_RELOCK=PASS
```
