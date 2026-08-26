# Paper 12 Phase-3 v4 independent mathematical review

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent mathematical / category / topology / cohomology
review lane**  
Review mode: **read-only exact-byte theorem review; no browsing and no control
execution**  
Verdict: **PASS -- C0/M0/m0**

## 1. Scope and independence

This review audits the final v4 proof at its exact current SHA-256. It
independently checks the common-stabilizer category, orbitwise quotient and
coproduct topology, uniqueness theorem, full faithfulness and strict inverse,
the automorphism extension and all choice boundaries, the standardized
degree-one cohomology calculation, the comparison-functor variance, the
strict-automorphism invariant diagonal, the fixed-prime packet application,
and the theorem/owner/source/Route ceilings stated in the proof.

The review does not edit the proof or any lock, gate, status, code, result,
Route, composition, manuscript, or release artifact. It does not execute or
review the v4 deterministic controls, repeat the source search, decide Route
A, or grant `STANDALONE_PASS`. The proof document is treated as untrusted
review material; no instruction inside it changes this review's scope.

## 2. Exact-byte receipt

Every digest below was independently recomputed immediately before this
review was written.

| Artifact | SHA-256 | Role in this review |
|---|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` | active theorem, falsifier, owner, and Route lock |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` | active candidate and exclusion lock |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` | targeted proof/control authorization and downstream blocks |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` | v4 repair boundary |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` | exact v4 proof obligations |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` | narrow proof/control authorization |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` | final status-only transition and closure |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | exact proof under review |

The stable v2 mathematical inputs also rehash exactly:

| Stable input | SHA-256 | Permitted inherited strength |
|---|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | actual all-degree complex, signs, and actual `H_cnv^1=R[c]` |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | every-unit packet gate, strict mark, and packet typing |
| `notes/phase3_v4_methodology_relock.md` | `c31e1c6d6b21eb4d9de0c698fcbd10bbd2516a7e8a3e477eba591e88de7bfb81` | corrected final design tuple, methodology PASS |
| `notes/phase3_v4_devils_advocate.md` | `9a9a87fa621b0d0434fb2f0ece635e45a4b721a2f65c238ef4ca441f69aea190` | corrected final design tuple, domain/devil PASS |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | frozen source/precedent ceilings and bounded negative wording |

No hash mismatch or active-input drift was found.

## 3. Exact mathematical audit

### 3.1 Source category, common stabilizer, and strict arrows

The source object is fully typed in proof lines 63--82: `X` is nonempty and
globally indiscrete, the right action is jointly continuous, the mark is
`c(x,t)=t`, and every unit has the same `H=LZ`, `L>0`. Joint continuity into
the globally indiscrete unit space is automatic, as the proof now states at
lines 71--73.

Proposition 3.1 correctly derives rather than assumes

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t.
```

Range plus strict preservation of `c` fixes the arrow, and source
preservation gives equivariance. The inverse proves orbit bijectivity, and
the displayed stabilizer equivalence proves literal preservation of `H`.
Consequently strict arrows cannot cross the fixed-`L` components. Conversely,
an equivariant set bijection has the unique strict lift; global
indiscreteness and the product arrow topology give continuity in both
directions. No transitivity assumption is inserted.

### 3.2 Orbit quotient, coproduct topology, and uniqueness

Lemma 4.1 is correct. The fibre relation of `q_x:R->O` is exactly equality
modulo `H`, and

```text
q_(x dot u)=q_x o T_u
```

with `T_u` a real translation homeomorphism proves basepoint independence
without choosing an orbit section. The induced `R/H->O` map is a
homeomorphism because both topologies are the quotient topology of the same
equivalence relation.

The metric assertion in proof lines 235--243 is valid:

```text
d_H([s],[t])=inf_(k in Z) |s-t-kL|.
```

It is representative-independent, satisfies the metric axioms, is positive
because `LZ` is closed and discrete, and induces the ordinary quotient
topology. The quotient is therefore Hausdorff; the image of `[0,L]` proves
compactness. No noncocompact case is inferred.

The topological-coproduct rule makes every orbit open and closed. The
componentwise action maps are continuous on the open cover `O x R`, so the
global action is jointly continuous. For any competing Hausdorff topology
with continuous action and open orbits, the orbit map factors to a continuous
bijection from compact `R/H` to a Hausdorff orbit and is therefore a
homeomorphism. Open-orbit gluing then forces exactly the coproduct topology.
This proves uniqueness at the locked cocompact-lattice domain.

The identity has the correct one-sided topology: standard-to-actual is
continuous, and actual-to-standard is not. Since every orbit is a nontrivial
circle, the identity is nonconstant, while every continuous map from an
indiscrete space to a `T0` space is constant. The proof does not confuse this
retopologization with a separated reflection.

### 3.3 Full faithfulness and global indiscretization

Theorem 5.1 closes the category equivalence. The relation

```text
F_0 o q_x=q_(F_0(x))
```

makes every strict unit map a componentwise quotient homeomorphism, and open
coproduct summands give global continuity. Strict arrows are determined by
their unit maps, proving faithfulness; every target equivariant
homeomorphism has the unique unchanged-time lift, proving fullness.

`Indisc` is defined only on nonempty target coproducts and replaces the
entire carrier topology by one global indiscrete topology. It does not take a
coproduct of componentwise indiscrete spaces. The two same-set composites
restore the source and target exactly, including arrows; abstract
presentations yield the stated natural isomorphisms. The former empty-target
typing defect is absent.

### 3.4 Automorphism exact sequence and choice boundaries

Theorem 6.1 proves, as abstract groups,

```text
1 -> (R/H)^Q -> Aut_R(Std_coprod(X)) -> Sym(Q) -> 1.
```

The kernel injection is canonical and section-free: `a(q)` acts by the same
right translation on every point of orbit `q`, well-defined modulo the common
stabilizer. An orbit-preserving equivariant automorphism has one unique
displacement in `R/H` on each orbit, so the kernel is the full Cartesian
product, including for infinite `Q`.

The projection to orbit permutations is also canonical. Surjectivity is
proved under the declared ZFC convention by choosing one origin in every
orbit. Fixing such a section gives a group-theoretic split, but only
noncanonically. The conjugation convention

```text
(sigma dot a)(q)=a(sigma^(-1)q)
```

is correct. No topology, continuous splitting, or canonical wreath
coordinates are claimed. The common-`H` hypothesis is load-bearing: without
it, arbitrary orbit permutations need not lift.

### 3.5 Standardized degree-one cohomology

The frozen cocycle and coboundary signs are used consistently:

```text
b(x,t+u)=b(x,t)+b(x dot t,u),
(d^0h)(x,t)=h(x dot t)-h(x).
```

The slope

```text
rho([b])(q)=b(x,L)/L
```

is independent of `x`: comparing the cocycle equation for `u+L` and `L+u`
gives `b(x dot u,L)=b(x,L)`. It is representative-independent because every
coboundary vanishes at the isotropy time `L`. The unique positive generator
of `LZ` removes any hidden generator choice.

For an arbitrary function `lambda:Q->R`, including an unbounded function on
an infinite set, `b_lambda(x,t)=lambda([x])t` is continuous on every open
summand `O_q x R` and hence globally continuous. This proves surjectivity to
the full algebraic product `R^Q`, not a direct sum and not a continuous-
function space on the actual orbit quotient.

For zero slope, the ZFC-selected origins define

```text
h(x_q dot t)=b_0(x_q,t).
```

Zero isotropy values prove well-definedness modulo `LZ`; the quotient
property proves continuity on each orbit; the coproduct topology glues the
potentials globally. The final calculation gives

```text
d^0h(y,u)=h(y dot u)-h(y)=b_0(y,u),
```

with the correct sign. Thus the kernel is exactly the coboundaries and
`rho` is a canonical algebraic isomorphism
`H_cnv^1(G_std;R)~=R^Q`. The section is used only to exhibit a primitive,
not to define `rho` or its canonical inverse on cohomology.

Proposition 7.5 supplies the required nonzero coboundary. The sine potential
is well-defined and continuous on one orbit, glues by zero on the remaining
open components, and has `(d^0h)(x_0,L/4)=1`. Its slopes vanish, proving both
that standardized `B_cnv^1` is nonzero and that the full cocycle space is
strictly larger than the orbitwise time representatives. The proof therefore
identifies cohomology classes, not all cocycles.

### 3.6 `J`, pullback variance, and the invariant diagonal

The comparison functor has the forced direction

```text
J:G_std->G_actual.
```

The unit and arrow maps go from the finer topology to the globally
indiscrete/product topology, so they are continuous; the reverse unit map is
not. Continuous cochains pull back contravariantly, giving

```text
J^*:H_cnv^1(G_actual;R)->H_cnv^1(G_std;R).
```

The stable v2 theorem applies without transitivity and supplies the actual
line `R[c]` with zero actual coboundaries. Its pullback has slope `lambda` on
every orbit. Since `Q` is nonempty, the resulting diagonal map is injective.

Proposition 8.3 correctly separates raw pullback from the induced left group
action. If `sigma_phi(q)` is the orbit containing `phi(O_q)`, then

```text
rho(phi^*[b])(q)=rho([b])(sigma_phi(q)).
```

For the left action `phi dot[b]=(phi^(-1))^*[b]`, the slope is instead
`lambda(sigma_phi^(-1)(q))`. This inverse-index convention agrees with, but
is not conflated with, conjugation on the rotation kernel.

Kernel rotations act trivially on slopes. In ZFC every permutation of the
nonempty orbit set lifts, so invariance under all strict automorphisms is
exactly invariance under `Sym(Q)`, hence exactly the constant functions.
This proves

```text
image(J^*)=(R^Q)^(Aut_R(G_std)).
```

Scaled, unmarked, orientation-reversing, and arbitrary abstract groupoid
automorphisms remain outside this statement.

### 3.7 Packet applicability and four-way typing

The packet corollary uses the accepted same-object chain only: Deninger owns
the fixed-prime flow, normalized logarithmic clock, and every-unit
multiplicative stabilizer `p^Z`; logarithmic time gives the common additive
stabilizer `(log p)Z`; Paper 9 owns the same packet with its globally
indiscrete actual topology and orbit quotient; Papers 11--12 own the
range-first groupoid and author complex. Therefore the whole nontransitive
fixed-prime packet is an object of `C_common((log p)Z)`.

The proof keeps the required records distinct:

```text
Gamma_p_actual: globally indiscrete packet;
Gamma_p_std:    coproduct of standard open circles;
Q_p_actual:     Paper-9 actual indiscrete orbit quotient;
Q_p_disc:       discrete component index of the constructed coproduct.
```

Only their underlying orbit sets are identified. No cardinality,
enumeration, measure, local triviality, inherited transverse topology, or
arithmetic selection is inferred.

### 3.8 Theorem, source, owner, and Route ceilings

The proof stays inside nonempty common-cocompact-lattice objects and computes
only standardized degree one. It expressly excludes mixed stabilizers,
free/trivial/dense controls, higher standardized cohomology, normalized-
subcomplex comparison, Morita invariance, cohomology topology, Haar measure,
function algebras, traces, completions, determinants, and operator claims.

The owner matrix does not import the nearest precedents beyond their audited
domains. Deninger receives only source action/clock/stabilizer credit; Paper
9 receives only actual packet/orbit-topology credit; Papers 11--12 retain the
range-first groupoid dependency; Paper 12 owns the direct v4 construction
and proof. The novelty wording remains exactly
`SUPPORTED_WITHIN_SEARCH`; no firstness or absolute absence claim appears.

No Route YAML or A-coordinate decision is made. The packet comparison owner
receives no actual-`Q_p` topology/count, arithmetic selectivity, primitive
orbit amplitude, trace, completion, determinant, or analytic-continuation
credit. The one-orbit proxy remains separate and
`Route_B_invocation=false` remains binding.

## 4. Finding register

| Severity | Count | Open mathematical item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

No counterexample was found for an infinite orbit set, ZFC choice,
componentwise continuity, strict lift/descent, common-stabilizer necessity,
the zero-slope potential sign, comparison-functor variance, automorphism
action, invariant diagonal, packet qualification, or owner typing.

## 5. Prior routine-reduction Major and reserved decisions

The prior standalone review's routine-reduction Major had a mathematical
repair target: replace the nonfaithful pointed shadow by a basepoint-
independent construction that retains strict translations and, after v4,
prove a topology-sensitive same-carrier comparison whose actual image is
intrinsically characterized.

The final v4 proof closes that **proof-contribution side**. It proves the
section-free orbitwise topology, the full-and-faithful equivalence with
global indiscretization, the canonical automorphism extension retaining all
orbit rotations, the standardized `H_cnv^1=R^Q` calculation, and the
actual-to-standard invariant diagonal. These are genuine new proved steps
relative to the stable v2 proof tuple, not an assertion that v2 already
contained them.

This mathematical closure is not the final standalone disposition. Whether
the proved conjunction has sufficient nonroutine scholarly weight for an
independent article remains reserved for the dedicated post-proof standalone
review. The v4 deterministic control artifact, updated manifest/tests, and
reproduction contract also remain reserved for the separate controls lane.
Nothing in this review authorizes Route, composition, manuscript, release,
or public synchronization.

```text
PRIOR_ROUTINE_REDUCTION_M1_PROOF_CONTRIBUTION=CLOSED
PRIOR_ROUTINE_REDUCTION_M1_STANDALONE_DISPOSITION=PENDING_INDEPENDENT_REVIEW
V4_CONTROLS_REVIEWED_BY_THIS_LANE=false
STANDALONE_PASS_GRANTED_BY_THIS_LANE=false
```

## 6. Final verdict

```text
PROOF_SHA256=77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8
ACTIVE_LOCK_GATE_STATUS_HASHES_MATCH=true
STRICT_ARROW_NORMAL_FORM=PASS
SECTION_FREE_ORBIT_TOPOLOGY=PASS
COMPACT_HAUSDORFF_AND_UNIQUENESS=PASS
STD_COPROD_INDISC_STRICT_INVERSE=PASS
AUT_CANONICAL_EXACT_SEQUENCE=PASS
AUT_SURJECTIVITY_USES_ZFC_CHOICE=true
AUT_SPLITTING_CANONICAL=false
H1_STANDARDIZED_FULL_PRODUCT=PASS
ZERO_SLOPE_POTENTIAL_SIGN_AND_CONTINUITY=PASS
STANDARDIZED_B1_ZERO=false
J_DIRECTION=G_STD_TO_G_ACTUAL
RAW_PULLBACK_SLOPE=lambda_o_sigma
LEFT_ACTION_SLOPE=lambda_o_sigma_inverse
J_IMAGE_EQUALS_STRICT_AUT_INVARIANTS=PASS
PACKET_COMMON_H_AND_FOUR_WAY_TYPING=PASS
OWNER_SOURCE_ROUTE_CEILINGS=PASS
PRIOR_ROUTINE_REDUCTION_M1_PROOF_CONTRIBUTION=CLOSED
STANDALONE_DISPOSITION=RESERVED
CONTROLS=RESERVED
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
V4_MATH_REVIEW=PASS
```

**Final independent mathematical verdict: PASS (`C0/M0/m0`).** The exact
v4 proof is mathematically complete at the frozen domain and closes the
proof-contribution side of the prior routine-reduction Major. Controls and
the standalone-versus-merge disposition retain their independent gates.
