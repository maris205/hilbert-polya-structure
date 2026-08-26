# Paper 12 integrated pre-Route proof, ownership, and standalone audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Integrated mathematical verdict: **`CONFIRM_COMPLEX_COLLAPSE`,
`CONFIRM_MARKED_PERIOD_RECOVERY`, and `CONFIRM_STRICT_VS_SCALED_SPLIT`**  
Packet verdict: **`PACKET_COROLLARY`; `ORBIT_ONLY=false`**  
Standalone disposition: **`STANDALONE_PASS`**  
Mathematical targets: **`P12-1`--`P12-8` proved**  
Deterministic controls: **`P12-9` PASS -- 122/122 tests, 11 CSVs,
3486 rows, 14/14 explicit negatives detected**  
Route status: **pre-Route evidence complete; `P12-10` not evaluated here**  
Integrated findings: **0 Critical / 0 Major / 0 Minor**  
Manuscript and release status: **not authorized by this audit**

## 1. Scope and acyclic boundary

This report integrates the unchanged active lock and gate tuple, the stable
v2 actual-topology proofs, the final v4 orbitwise-standardization proof, the
independent exact mathematical review, the final deterministic-control
manifest and controls review, the source/design gates, and the independent
binding standalone review. It creates no new mathematical object and does
not strengthen any theorem beyond its proved owner, topology, coefficient,
or category.

This is deliberately a **pre-Route** audit. It binds no Route audit and no
Route-A or Route-B YAML. Those artifacts are downstream consumers that may
bind the detached SHA-256 of this report; this report cannot bind them without
creating a provenance cycle. It likewise does not bind a composition,
manuscript, citation, declaration, release, or public-sync artifact.

The exact central comparison is

```text
H_cnv^1(G_actual;R)=R[c]
  --J^*--> H_cnv^1(G_std;R)=R^Q,

image(J^*)=(R^Q)^(Aut_R(G_std))
           ={constant functions Q->R}.
```

Here `C_cnv/H_cnv` is the Paper-12 author-defined globally continuous
unnormalized nerve complex, `Q` is a nonempty bare orbit set, and `R^Q` is
the full algebraic Cartesian product. No topology is placed on either
cohomology group, on `R^Q`, or on an automorphism group.

## 2. Exact-byte evidence lock

Every digest in this section was independently recomputed immediately before
this audit was written.

### 2.1 Active protocol, candidate, state, and v4 gates

| Artifact | SHA-256 | Status bound here |
|---|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` | active targets, owners, falsifiers, and ceilings |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` | active candidate, conventions, exclusions, and decision vocabulary |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` | targeted proof/control authorization and downstream blocks |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` | v4 repair and nontransitive common-`H` boundary |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` | exact v4 theorem and control obligations |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` | exact-byte design/source PASS and narrow proof/control authorization |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` | final status-only transition, including candidate closure |

The status re-lock's exact inverse reconstruction establishes that the
active protocol, candidate, and pipeline differ from the independently
reviewed v4 content tuple only in gate/status provenance. No mathematical,
owner, control-freeze, or Route-schema drift is imported here.

### 2.2 Source, category, and novelty gates

| Artifact | SHA-256 | Exact retained strength |
|---|---|---|
| `notes/phase2_category_owner_audit.md` | `8fad79f121439145e0ac3cac7ca67e82f3e2ad6af86da5b0f001e92da30e1d62` | author complex, coefficient, category, and owner boundaries |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` | exact framework hypotheses and same-object source chain |
| `notes/phase2_novelty_search.md` | `c4584862824dbaadec9945fb85defd6d11ee7822849471b075ff4d90d57ca1bd` | bounded v2 search result only |
| `notes/phase2_final_review.md` | `032d558fecdccc492ce59733e20dd9322f573d033355aee3c74563680cea2ea7` | independent Phase-2 `PASS C0/M0/m0` |
| `notes/phase2_final_gate.md` | `1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab` | stable v2 source/proof authorization |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | targeted v4 nearest-precedent and source-domain ceilings |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` | local source manifestations and exact locators |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` | source/preflight checksum ledger |

The only negative novelty wording licensed by these gates is
`SUPPORTED_WITHIN_SEARCH` through the frozen cutoff **2026-08-15**. The v4
audit records `DIRECT_EXACT_PACKAGE_PRECEDENT_FOUND=false` only at that
bounded strength. This is not a firstness, priority, or global-absence claim.

### 2.3 Stable v2 proofs and final v4 proof

| Artifact | SHA-256 | Role in the integrated theorem |
|---|---|---|
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | direct `P12-1`--`P12-5`: actual nerve, complex, chain reduction, actual `H^1`, and isotropy image |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | direct `P12-6`--`P12-8` v2: packet, covariance/non-descent, and pointed shadow |
| `notes/phase3_orbitwise_standardization_h1_proofs.md` | `77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8` | final v4 common-`H` standardization, automorphisms, standardized `H^1`, `J`, and invariant diagonal |
| `notes/phase3_v4_math_review.md` | `97dbd63fae6d35ae627520203db98d7c497a927a505599c0855231ac3f3b4e07` | independent exact-proof `PASS C0/M0/m0` |

V4 extends rather than supersedes the stable v2 mathematics. The all-degree
actual-complex theorem, actual `H_cnv^1=R[c]`, representative-independent
period image, packet recovery, strict/scaled/unmarked boundary, and pointed
one-orbit shadow remain valid at their original exact owners. V4 supplies the
additional nontransitive same-carrier topology and comparison theorem; it
does not reinterpret a failed v3 proposal as prior proof.

### 2.4 Final deterministic controls

| Artifact | SHA-256 | Role |
|---|---|---|
| `results/manifest.json` | `7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95` | final 11-CSV/3486-row control manifest |
| `notes/phase3_v4_controls_review.md` | `886a2648473035bb4d3600a03474680d3f692b1bdca08034096c6e7eebd664e6` | independent reproduction and controls `PASS C0/M0/m0` |

The manifest was frozen concurrently with the v4 proof and therefore
honestly records

```text
proof_binding.concurrent_v4_proof_hash_included=false.
```

This is not an unresolved proof/control gap. The controls review separately
binds the now-stable proof SHA-256
`77258319c1e1cbcc08501e33e3c60a03acd71a62342898f3535375e6159f77e8`
to the manifest and confirms there was no proof-hash race. This audit binds
the stable proof, manifest, and controls review together without modifying
the manifest retrospectively.

The reviewed package completed `122/122` tests and contains exactly eleven
CSV files and `3486` body rows. The new v4 ledger has `3252` rows in the
frozen blocks

```text
MODEL / BASEPOINT / AUT / NEGATIVE = 9 / 90 / 3151 / 2.
```

All `3151` finite strict automorphisms were enumerated; the actual and
standardized finite-model `H^1` dimensions are `1` and `m`; the comparison
rank and full-permutation invariant dimension are `1`; nonzero coboundaries
and zero-isotropy potentials were checked; mixed lengths and the reversed
`J` direction were rejected. The complete package detects all `14` explicit
negatives with zero negative-control failures and passes checked-in/fresh-one/
fresh-two byte identity, strict verify-only, drift/tamper, recursive-entry,
and no-cache gates.

The shared-workspace extra-run incident is retained in the controls review.
It produced no accepted evidence, surviving process, temporary directory,
cache, result mutation, or proof/manifest drift. The one authorized controls
run remains the reproducibility receipt.

### 2.5 Binding standalone review

| Artifact | SHA-256 | Binding result |
|---|---|---|
| `notes/phase3_v4_standalone_review.md` | `639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895` | `STANDALONE_PASS C0/M0/m0`; prior routine-reduction Major closed |

The standalone reviewer independently reconstructed the final theorem,
controls, owner split, and nearest-precedent ceiling. The pass is not based
on a vote or on failure to find one exact-title source. It is based on the
proved interaction between two continuity structures on the same marked
carrier, the full standardized cohomology, and the intrinsic characterization
of the classes descending from the actual topology.

The pass is conditional on keeping that comparison theorem central. A later
manuscript that foregrounds only the inherited actual collapse, ordinary
quotient/coproduct facts, a wreath formula, or the source-owned period must
undergo its own manuscript-level adverse review; this audit does not pre-pass
such a presentation.

## 3. Frozen objects, topologies, and coefficient convention

### 3.1 Generic actual owner

Let `X` be a nonempty globally indiscrete space with any right action of the
additive group `R`. The action is jointly continuous because its codomain is
indiscrete. Define the range-first action groupoid

```text
G(X,alpha)=X rtimes R,
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u),
(x,t)^(-1)=(x dot t,-t).
```

The arrow topology is the product of the global indiscrete topology on `X`
and the usual topology on `R`. The generic actual theorem assumes no
transitivity, stabilizer, lattice, prime, packet, or arithmetic label.

### 3.2 Author-defined cochain complex

For a named `T0` topological abelian group `A`, the coefficient object is the
constant bundle with identity arrow action. The Paper-12 complex is

```text
C_cnv^0(G;A)=C(X,A),
C_cnv^n(G;A)=C(G^(n),A), n>=1,
```

with the frozen globally continuous **unnormalized** nerve differential.
There is no support, boundedness, decay, integrability, smoothness, Borel-
only, or compactness requirement. Cohomology is algebraic. Until a source
matches these exact hypotheses and conventions, the result is not renamed
unqualified “continuous topological-groupoid cohomology.”

### 3.3 Common-stabilizer standardized owner

V4 additionally fixes a common cocompact lattice

```text
H=LZ, L>0,
Stab_R(x)=H for every x in X,
Q=X/R != emptyset.
```

It gives each orbit the quotient topology of `R/H` and takes their
topological coproduct on the same underlying set. This constructed standard
topology is not the actual inherited topology, not a separated reflection,
and not a topology transported to the actual orbit quotient. Its component
index is discrete only by construction.

## 4. Integrated target matrix

| Target | Exact integrated result | Direct proof owner | Deterministic witness | Nonpromotion ceiling |
|---|---|---|---|---|
| `P12-1` | for every finite `n`, `Psi_n:X x R^n->G^(n)` is a homeomorphism; exact faces and degeneracies are continuous | v2 core proof §3 | nerve-face ledger | actual globally indiscrete owner; no infinite-degree topological product claim |
| `P12-2` | constant coefficient action is continuous; frozen unnormalized differential is typed and satisfies `d^(n+1)d^n=0` | v2 core proof §4 | face and `d^2` checks | author complex only; no named-theory upgrade |
| `P12-3` | time projection is an all-degree cochain-complex isomorphism for every named `T0` coefficient; evaluation is its unit-independent inverse | v2 core proof §5 | factorization and non-`T0` negatives | `T0` is load-bearing; non-`T0` removal is refuted |
| `P12-4` | on the actual globally indiscrete groupoid, `Z_cnv^1=R c`, `B_cnv^1=0`, `H_cnv^1=R[c]` | v2 core proof §6 | degree-one profiles | real coefficients; no preferred arithmetic scale without the source mark |
| `P12-5` | isotropy restriction kills coboundaries and descends; `Per_x([lambda c])=lambda H_x`; transitive units transport | v2 core proof §7 | period and boundary controls | no universal lattice claim; arbitrary classes do not parametrize orbits |
| `P12-6` | every fixed orbit and every unit of the exact fixed-prime packet has `Per_x([c])=(log p)Z` | v2 marked proof §3 plus exact source gate | packet schema, source-gated only | `PACKET_COROLLARY`; no global/cross-prime suspension promotion |
| `P12-7` | strict preservation, positive scaled covariance, explicit unequal-period non-descent, and orientation-reversal nonconverse | v2 marked proof §4 | morphism and wrong-scale ledgers | covariance is not an iff; weaker-category loss is existential |
| `P12-8a` | pointed standard period quotient, chart/naturality/basepoint law, and one-sided topology | v2 marked proof §5 | quotient-topology controls | deliberately lossy shadow; no actual-topology transport |
| `P12-8b` | section-free orbitwise coproduct, topology uniqueness, full-and-faithful `Std_coprod` with strict inverse `Indisc` | v4 proof §§3--5 | finite basepoint, topology, lift/descent controls | nonempty common cocompact lattice only; not a separated reflection |
| `P12-8c` | canonical abstract-group exact sequence `1->(R/H)^Q->Aut_R(G_std)->Sym(Q)->1` | v4 proof §6 | all `3151` finite automorphisms | surjectivity/split use ZFC choice; split noncanonical; no automorphism topology |
| `P12-8d` | `H_cnv^1(G_std;R)=R^Q`, actual line maps to the constant diagonal, equal to strict-automorphism invariants | v4 proof §§7--8 | finite dimensions, potentials, coboundaries, diagonal, invariants | full algebraic product; degree one only; strict automorphisms only |
| `P12-8e` | fixed-prime packet instantiates the v4 theorem with common `H=(log p)Z` | v4 proof §9 | schematic packet rows plus exact source proof | bare `Q_p` only; four-way topology typing mandatory |
| `P12-9` | deterministic controls reproduce all frozen finite witnesses, negatives, counts, and byte-integrity gates | manifest and v4 controls review | `122/122`; `11/3486`; `14/14` | controls do not prove real, infinite-`Q`, choice, topology, source, or arithmetic claims |
| `P12-10` | formal typed Route-A evaluation | not executed in this audit | none bound here | downstream only; no Route/YAML dependency; Route B remains false by design |

## 5. Proof dependency and conservation ledger

The proof graph is one-directional:

```text
Paper-9 actual orbit/packet topology
  + Deninger fixed-prime flow, clock, and every-unit stabilizer
  + Papers-11/12 range-first groupoid
    -> v2 all-degree actual nerve and author complex
    -> actual all-degree time-projection collapse
    -> actual H_cnv^1=R[c] and representative-independent isotropy image
    -> fixed-orbit and fixed-prime PACKET_COROLLARY
    -> strict/scaled/unmarked covariance and non-descent
    -> pointed standard quotient shadow

common every-unit H=LZ on the same nonempty action
    -> section-free orbit quotient topologies
    -> open Hausdorff coproduct and topology uniqueness
    -> full-and-faithful Std_coprod / global-Indisc equivalence
    -> canonical automorphism exact sequence
    -> standardized H_cnv^1=R^Q with nonzero B_cnv^1
    -> continuous identity J:G_std->G_actual
    -> J^*:R->R^Q as the constant diagonal
    -> diagonal = strict-automorphism invariant subspace
    -> exact fixed-prime packet application.

finite controls
    -> deterministic witnesses and falsifiers only
    -/> universal real/infinite-Q/source proof.

this pre-Route proof audit
    -> possible downstream Route audit/YAML binding
    <-/ no Route artifact is an input here.
```

No standard quotient theorem, finite wreath comparator, or transitive
cohomology source is used to prove the whole actual/standard comparison. No
proxy topology proves an actual-topology statement, and no arithmetic label
is used to prove a generic theorem.

## 6. Stable v2 actual-complex audit

### 6.1 All finite nerve degrees and the frozen differential

For each finite `n`, a composable tuple is uniquely determined by its first
range and `n` time increments. Finite powers of an indiscrete space are
indiscrete, so the nerve opens are exactly `X x U` in the `Psi_n` chart.
The exact first, interior, and last faces project respectively by dropping
the first time, adding adjacent times, and dropping the last time; the first
face alone changes the unit. The direct simplicial face identity pairs every
term in `d^(n+1)d^n` with the identical composite and opposite sign.

This proves the author complex at all finite degrees. Degenerate cochains are
retained; no normalized-subcomplex comparison is inferred.

### 6.2 `T0` factorization and chain reduction

Points `(x,t)` and `(y,t)` have identical open neighborhoods. A continuous
map to a `T0` target therefore cannot distinguish their unit coordinates.
This gives degreewise factorization through time and makes evaluation at any
unit the same inverse. Exact projected-face identities prove that time
pullback commutes with `d` in every degree.

The `T0` boundary is sharp: the frozen indiscrete `Z/2Z` coefficient admits
a nonconstant continuous degree-zero map. The theorem is not promoted to
non-`T0` coefficients.

### 6.3 Actual real degree one and marked period

For real coefficients, actual one-cochains factor as `b(x,t)=f(t)`. The
cocycle law is the continuous Cauchy equation, hence `f(t)=lambda t`.
Continuous degree-zero cochains on the actual globally indiscrete unit space
are constant, so

```text
Z_cnv^1(G_actual;R)=R c,
B_cnv^1(G_actual;R)=0,
H_cnv^1(G_actual;R)=R[c].
```

The abstract line does not select a preferred nonzero class. Only the
Deninger-normalized clock marks `[c]`. Its isotropy restriction is the
identity on the stabilizer; all coboundaries vanish on isotropy before the
image is defined, so

```text
Per_x([lambda c])=lambda H_x
```

is representative-independent.

### 6.4 Packet gate and category boundary

At the exact fixed-prime packet, Deninger supplies multiplicative
stabilizer `p^Z` at **every** unit. The same normalized logarithmic clock
converts it to `(log p)Z`; Paper 9 separately supplies the actual global
indiscrete packet topology. Thus

```text
Per_x([c])=(log p)Z for every x in Gamma_p,
PACKET_COROLLARY=true,
ORBIT_ONLY=false.
```

Strict marked isomorphisms preserve the subgroup. Positive scaled morphisms
obey `H'=alpha H`; explicit dilations connect unequal lattice generators,
so the unscaled subgroup is not a scaled or unmarked invariant. Orientation
reversal preserves the subgroup while reversing the clock, refuting the
converse from subgroup equality to strictness. These are exact category
claims, not universal statements that every weak morphism changes a period.

The pointed standard quotient remains valid as a one-orbit isomorphism-class
proxy and based shadow. It is deliberately nonfaithful and is not identified
with the actual inherited topology.

## 7. V4 orbitwise topology and category audit

### 7.1 Section-free standardization

For an orbit `O` and `x in O`, let `q_x(t)=x dot t`. Its fibres are the
`H=LZ` cosets. If `x'=x dot u`, then

```text
q_(x')=q_x o T_u,
```

and real translation `T_u` is a homeomorphism. The quotient topology on the
same orbit set is therefore basepoint-independent. The standard metric

```text
d_H([s],[t])=inf_(k in Z)|s-t-kL|
```

gives the ordinary compact Hausdorff `R/H` topology. Taking the nonempty
topological coproduct of those orbits gives a Hausdorff space with open
orbits and jointly continuous action.

Any competing Hausdorff action topology with open orbits receives a
continuous bijection from compact `R/H` on each orbit and is therefore the
same orbit topology; open-orbit gluing forces the same coproduct globally.
This proves uniqueness only at the frozen cocompact-lattice domain.

The identity from the finer standardized carrier to the actual global
indiscrete carrier is continuous. The reverse identity is not. The
construction retains the action set and is neither an inherited topology nor
a Kolmogorov, Hausdorff, or completely regular reflection.

### 7.2 Full faithfulness and strict inverse

Strict preservation of `c=t` forces

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t.
```

Thus every strict arrow descends to an equivariant homeomorphism of the
standardized coproduct, and every such target homeomorphism has one unique
unchanged-time lift. `Std_coprod` is full and faithful.

`Indisc` replaces the **whole** target carrier topology by one global
indiscrete topology. On the explicitly nonempty target, both same-set
composites are strict identities; abstract presentations yield the displayed
natural isomorphisms. A coproduct of componentwise indiscrete topologies is
not used.

### 7.3 Canonical automorphism extension and choice

Every strict equivariant automorphism permutes the nonempty orbit set `Q`.
The section-free kernel consists of independent right rotations, one in
`R/H` on every orbit. Hence, canonically as abstract groups in ZFC,

```text
1 -> (R/H)^Q -> Aut_R(G_std) -> Sym(Q) -> 1.
```

The kernel is the full Cartesian product even for infinite `Q`. The maps and
kernel identification use no origin. Surjectivity uses a ZFC choice of one
origin in each orbit. Fixing such origins splits the sequence
noncanonically, with conjugation action

```text
(sigma dot a)(q)=a(sigma^(-1)q).
```

No canonical split, topology, or continuous-splitting claim is made. The
common-`H` condition is load-bearing: mixed-stabilizer orbits cannot in
general be permuted arbitrarily.

## 8. Standardized `H^1`, comparison variance, and invariants

### 8.1 Full algebraic product and nonzero coboundaries

The frozen standardized cocycle equation and degree-zero sign are

```text
b(x,t+u)=b(x,t)+b(x dot t,u),
(d^0h)(x,t)=h(x dot t)-h(x).
```

The canonical slope

```text
rho([b])(q)=b(x,L)/L
```

is basepoint-independent by comparing `u+L` and `L+u`, and is
representative-independent because coboundaries vanish on isotropy.

Every function `lambda:Q->R`, including an arbitrary unbounded function on
an infinite set, defines

```text
b_lambda(x,t)=lambda([x])t.
```

It is globally continuous because every component `O_q x R` is open. Thus
surjectivity is onto the full algebraic Cartesian product `R^Q`, not a direct
sum and not a continuous-function space on the actual `Q_p`.

For zero slopes, choose one origin `x_q` per orbit and define

```text
h(x_q dot t)=b_0(x_q,t).
```

Zero isotropy makes it well-defined, quotient descent makes it continuous on
each orbit, and coproduct gluing makes it globally continuous. The exact
sign calculation gives `d^0h=b_0`. Therefore

```text
H_cnv^1(G_std;R)=R^Q.
```

Standardized degree-zero cochains need not be constant. The explicit sine
potential has a nonzero coboundary with zero slopes, so

```text
B_cnv^1(G_std;R) != 0,
Z_cnv^1(G_std;R) != {b_lambda:lambda in R^Q}.
```

Only cohomology classes reduce to orbitwise time representatives. No higher
standardized degree is computed.

### 8.2 `J`, raw pullback, left action, and invariant diagonal

The same-set identity has the forced continuous direction

```text
J:G_std -> G_actual.
```

Continuous cochains pull back contravariantly:

```text
J^*:H_cnv^1(G_actual;R) -> H_cnv^1(G_std;R).
```

Under `rho`, `J^*(lambda[c])` is the constant function with value `lambda`.
The diagonal is injective because `Q` is nonempty.

If a strict automorphism `phi` induces `sigma_phi in Sym(Q)`, raw pullback
has the exact slope formula

```text
rho(phi^*[b])(q)=rho([b])(sigma_phi(q)).
```

For the declared left action

```text
phi dot[b]=(phi^(-1))^*[b],
```

the slope is instead

```text
(phi dot lambda)(q)=lambda(sigma_phi^(-1)(q)).
```

Raw contravariant pullback is therefore not conflated with the inverse-index
left action. The latter shares an inverse-index convention with conjugation
on the rotation kernel, but the two actions are distinct.

Kernel rotations act trivially on slopes. All orbit permutations lift in ZFC,
so the invariant functions are exactly the constants. Consequently

```text
image(J^*)=(R^Q)^(Aut_R(G_std))
           ={constant functions Q->R}.
```

`Aut_R` means strict time-preserving equivariant automorphisms. Scaled,
unmarked, orientation-reversing, and arbitrary abstract groupoid
automorphisms are outside this theorem.

## 9. Fixed-prime packet application and four-way typing

The exact packet application instantiates the common-stabilizer theorem with

```text
H=(log p)Z at every packet unit.
```

Deninger owns the fixed-prime flow, normalized clock, and stabilizer. Paper 9
owns the actual packet and orbit quotient topology. Papers 11--12 own the
range-first groupoid and author complex. Paper 12 owns the constructed
standardization and comparison.

Four records remain distinct:

| Record | Exact type/topology | Forbidden conflation |
|---|---|---|
| `Gamma_p_actual` | same packet unit set with one global indiscrete topology | no standard-circle topology on the actual packet |
| `Gamma_p_std` | same set with the coproduct of open standard circles | not inherited and not a separated reflection |
| `Q_p_actual` | Paper-9 orbit quotient with its actual indiscrete quotient topology | no discreteness, count, enumeration, measure, or local triviality |
| `Q_p_disc` | same bare orbit set as the discrete component index of `Gamma_p_std` | not the topology of `Q_p_actual` |

No packet theorem requires transitivity. The v3 one-orbit result survives
only componentwise. The packet result supplies no cardinality, enumeration,
measure, transverse topology, or arithmetic selectivity.

## 10. Owner and source-credit conservation

| Claim surface | Exact owner | Retained input/source role | Forbidden promotion |
|---|---|---|---|
| generic actual `G(X,alpha)` and `C_cnv/H_cnv` | Paper 12 author construction | Paper 11 supplies only arrow/time-factorization background | no arithmetic, packet, Deninger, or named-theory credit |
| fixed orbit `G_(p,a)^orb` | Papers 11--12 groupoid on Paper-9 actual orbit | Deninger action/clock/stabilizer; Paper 9 topology | no “Deninger groupoid/cohomology” wording |
| fixed-prime packet `G_p^pkt` | Papers 11--12 groupoid on Paper-9 actual packet | Deninger every-unit packet stabilizer and normalized clock | no global suspension or cross-prime theorem |
| one-orbit standard period quotient | Paper-12 proxy/shadow | source-marked `H` only | no actual topology, reflection, or packet-standardization credit |
| `Std_coprod(X)` and `G_std` | Paper-12 constructed same-set topology/groupoid | standard quotient/coproduct background only | not inherited; no source theorem for the full comparison |
| automorphism extension | Paper-12 direct arbitrary-`Q` proof | finite component/wreath sources are nearest comparators | no finite-to-arbitrary transfer or canonical split |
| standardized `H_cnv^1=R^Q` | Paper-12 author complex/direct proof | transitive cohomology source is a different-theory comparator | no rigid/Morita/named-theory identification |
| `J` and invariant diagonal | Paper-12 same-carrier comparison | no direct exact-package precedent within the bounded search | no priority or global absence claim |
| `Q_p_actual` | Paper 9 | actual quotient topology only | no constructed discrete topology/count |
| `Q_p_disc` | Paper 12 | component index of the constructed coproduct | no arithmetic or inherited-transverse meaning |
| `G^global` / cross-prime suspension | excluded | none | every Paper-12 theorem on this owner |

Local source PDFs and their hashes are internal verification artifacts, not
public scholarly identities or supplements. Bibliographic use must cite
canonical publisher, journal, DOI, arXiv, or author endpoints. This audit
does not authorize release of a source PDF.

## 11. Standalone/nonredundancy disposition

The v2 reviewer correctly held the earlier package because its mathematical
centre could be reduced to Paper-11 factorization, routine bar/Cauchy
formalism, Deninger's source-owned stabilizer, and a deliberately
nonfaithful pointed shadow. That finding is retained as history rather than
overridden by a vote.

V4 closes its two load-bearing unresolved parts:

1. `Std_coprod`/`Indisc` is full and faithful and retains strict orbit
   translations through the canonical automorphism kernel; and
2. the topology change produces a proved cohomological enlargement
   `R -> R^Q` whose actual image is intrinsically equal to all strict-
   automorphism invariants.

These claims require the constructed topology, nonzero standardized
coboundaries, zero-isotropy potential descent, arbitrary-orbit
automorphisms, and exact comparison variance. They are not supplied by the
stable v2 proof or by a single nearest component source.

The independent standalone review therefore returns

```text
PRIOR_ROUTINE_REDUCTION_M1=CLOSED,
ROUTINE_REDUCTION_TRIGGER_FOR_FINAL_V4=false,
STANDALONE_DECISION=STANDALONE_PASS,
CRITICAL_OPEN=0,
MAJOR_OPEN=0,
MINOR_OPEN=0.
```

This is a theorem-package disposition only. It is not a Route score, journal
acceptance decision, manuscript/citation-integrity clearance, declaration
gate, or release authorization.

## 12. Pre-Route boundary

The proof, source, controls, mathematical-review, and standalone preconditions
are now stable and mutually bound. This makes the exact theorem package
eligible for its separately authorized formal Route evaluation. It does not
prejudge that evaluation.

The eight nonconflated candidate owners remain those frozen by the active
protocol and candidate. Their design ceilings remain:

```text
generic complex: action-blind, no arithmetic credit;
marked source-period owners: source relation only;
standard quotient: one-orbit proxy/shadow only;
standardized packet comparison: derived topology/cohomology comparison,
                                no Q_p topology/count or arithmetic selection;
all owners: no pre-certified A coordinate;
A2/A3/A4 fail or NOT_TESTABLE absent a fresh same-owner theorem;
Route_B_invocation=false.
```

The downstream evaluator retains authority over every A0/A1 result. A period
subgroup alone is not a primitive-orbit amplitude, enumeration, trace, or
determinant. Nothing may be imported from Paper 8 traces, Paper 11
completions, a positive-time scalar ledger, target-zero data, or fitted
normalizations.

No Route artifact path or digest appears in this evidence lock. The detached
SHA-256 of this report is the acyclic upstream proof receipt to be consumed
later.

## 13. Finding register and final integrated verdict

| Severity | Count | Open integrated item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
P12_1_THROUGH_P12_8=PROVED
P12_9_CONTROLS=PASS
P12_10_ROUTE=NOT_EVALUATED_HERE
ACTUAL_H1=R[c]
ACTUAL_B1_ZERO=true
STANDARDIZED_H1=R^Q_FULL_ALGEBRAIC_PRODUCT
STANDARDIZED_B1_ZERO=false
J_DIRECTION=G_STD_TO_G_ACTUAL
J_PULLBACK_DIRECTION=H1_ACTUAL_TO_H1_STANDARDIZED
RAW_PULLBACK_SLOPE=lambda_o_sigma
LEFT_ACTION_SLOPE=lambda_o_sigma_inverse
J_IMAGE=CONSTANT_DIAGONAL
STRICT_AUT_INVARIANTS=CONSTANT_DIAGONAL
PACKET_RESULT=PACKET_COROLLARY
ORBIT_ONLY=false
PACKET_COMMON_H=(log p)Z_EVERY_UNIT
Q_P_FOUR_WAY_TYPING=EXACT
NOVELTY_CEILING=SUPPORTED_WITHIN_SEARCH
GENERIC_ARITHMETIC_SELECTIVITY=false
CONTROL_MANIFEST_SHA256=7cbce9303393fcd755dda785312e26165656301e5dfbcab53b611e71c6204e95
CONTROLS_REVIEW_SHA256=886a2648473035bb4d3600a03474680d3f692b1bdca08034096c6e7eebd664e6
STANDALONE_REVIEW_SHA256=639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895
STANDALONE_DECISION=STANDALONE_PASS
PRIOR_ROUTINE_REDUCTION_M1=CLOSED
ROUTE_ARTIFACTS_BOUND=false
ROUTE_B_INVOCATION_ALLOWED=false
MANUSCRIPT_OR_RELEASE_AUTHORIZED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
PRE_ROUTE_PROOF_AUDIT=PASS
```

**Final integrated pre-Route verdict: PASS (`C0/M0/m0`).** `P12-1` through
`P12-8` are proved at the frozen domains, `P12-9` controls pass independently,
the exact fixed-prime result is `PACKET_COROLLARY`, and the binding
standalone disposition is `STANDALONE_PASS`. `P12-10`, composition,
manuscript, citation, declaration, release, and public synchronization retain
their separate downstream gates.
