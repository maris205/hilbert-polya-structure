# Paper 12 Phase-1 source, scope, and nonredundancy feasibility review

Review date: **2026-08-15 (Asia/Shanghai)**  
Review mode: **independent source/domain feasibility on initial bytes only**  
Verdict: **REVISE — C0 / M4 / m2**  
Phase-2 release: **BLOCKED pending an amended exact-byte re-lock and a fresh independent review**

## 1. Exact-byte boundary and independence statement

This review is bound only to the following initial Paper-12 bytes:

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/research_protocol.md` | `1ea7e67825d5f543f472e1f4e0b3ea57a986269b24ec8dad1bf533475cc860eb` | exact lock matched |
| `notes/candidate_lock.md` | `6a03983a76d34937f01ff03da4d074d1111b0722afff417a4532c5d7744f2975` | exact lock matched |
| `notes/pipeline_state.md` | `4fe89540fb743e757e45ce71569261659a0d780db0c79ee5867792fe8ac936c0` | exact lock matched |

I did **not** read either other Paper-12 Phase-1 review. I did not edit any
lock, proof target, Route record, source artifact, prior-paper artifact, or
pipeline state. I did not run a Phase-2 literature or novelty search. The
external check was limited to identifying whether plausible primary sources
exist for the proposed definitions and to detecting source-domain mismatch.

The inherited local evidence hashes also match the candidate lock:

| Locked prior artifact | SHA-256 | Feasibility role |
|---|---|---|
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | actual packet/orbit indiscreteness and exact topology owner |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | Deninger action, packet, stabilizer, and topology-credit ceiling |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | separated observable and standard-quotient comparison boundary |
| Paper 11 `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | actual transformation-groupoid owner and arrow-time factorization |
| Paper 11 `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | source-credit, public-PDF, and nonpromotion boundary |

The source chain is therefore not blocked by a missing inherited theorem.
It is blocked by four repairable definition, owner, morphism, and standalone
scope defects in the initial Paper-12 lock.

## 2. Finding summary

| ID | Severity | Finding | Gate effect |
|---|---|---|---|
| M1 | Major | The proposed complex is not yet entitled to the unqualified name “continuous topological-groupoid cohomology”; the constant coefficient bundle/action and unnormalized nerve convention are underspecified. | amend convention and source-credit lock |
| M2 | Major | “Deninger action groupoid” conflates four owners, and the packet groupoid/common-stabilizer specialization is not explicitly frozen. | split generic/orbit/packet/global owners |
| M3 | Major | “Preserved precisely by strict morphisms but lost under scaled or unmarked equivalence” is logically too strong, and the claimed period-quotient functor has no defined source/target categories or arrow map. | weaken invariant claim and define categories |
| M4 | Major | The standalone/nonredundancy and bounded novelty gates are qualitative rather than executable; they do not force comparison with the nearest cohomology theories or a release decision if the package is formal from Papers 9/11 plus Deninger. | add exact search and merge/note decision rules |
| m1 | Minor | `Per_x([b])` is used before the restriction/image assignment has been proved representative-independent and its base-unit transport has been typed. | repair notation order |
| m2 | Minor | The public manuscript-PDF and source-PDF/internal-audit citation boundary is incomplete. | add release manifest and bibliography rules |

No Critical finding is assigned because the initial bytes call the package a
proposal and preserve Phase-2/Phase-3 blocks; no false theorem has yet been
released. All six findings must close for a Phase-1 `PASS`.

## 3. Major findings

### M1 — The cochain convention is feasible but not yet standard at the claimed scope

**Anchor:** `research_protocol.md` §§3--4, especially the coefficient sentence,
the displayed differential, and the “standard continuous groupoid-cohomology
convention or author-defined” fork; `candidate_lock.md` §§1, 3--4.

The formulas define a coherent **Paper-12 continuous unnormalized nerve
cochain complex**. They do not yet identify one unambiguous standard
topological-groupoid cohomology theory on this non-Hausdorff owner.

The coefficient datum must be frozen as the constant bundle

```text
underline(A)_X = X x A -> X,
gamma . (s(gamma),a) = (r(gamma),a),
```

with the continuity of this action checked. Cochains should then be described
either as continuous sections of the appropriate pullback bundle over
`G^(n)` or, **after the displayed trivialization**, as continuous maps
`G^(n)->A`. Merely saying that a many-unit groupoid acts trivially on the
topological group `A` suppresses the anchor bundle needed by standard module
conventions.

The lock must also say that “unnormalized” means all continuous cochains are
retained, including values on degenerate simplices; no condition requiring a
cochain to vanish when some `t_i=0` is imposed. The comparison complex for
`R` must use the same unnormalized convention. If a source uses normalized
cochains, Phase 2 must prove the normalization comparison rather than silently
identify the complexes.

The bounded feasibility check found three useful but noninterchangeable
primary comparators:

1. K. A. Mackenzie, “Rigid cohomology of topological groupoids,” *J. Austral.
   Math. Soc. (Series A)* 26 (1978), 277--301,
   DOI `10.1017/S1446788700011794`, defines continuous groupoid modules as
   bundles and uses nonhomogeneous cocycles. Its main theory assumes locally
   trivial, locally compact groupoids. Those hypotheses may not cover the
   actual inherited owner and must not be imported without proof.
2. J. Blanco, B. Uribe, and K. Waldorf, “Pontrjagin duality on
   multiplicative gerbes,” *J. Noncommut. Geom.* 17 (2023), 1469--1520,
   DOI `10.4171/JNCG/528`, §2.3 defines continuous cochains on a simplicial
   space and §2.4 displays the unnormalized inhomogeneous differential for a
   topological group. Its Segal--Mitchison comparison has paracompactness and
   coefficient hypotheses; it is a convention source, not automatic proof
   that the Paper-12 complex equals that derived theory for every named `T0`
   coefficient.
3. C. Farsi, L. Huang, A. Kumjian, and J. Packer, “Cocycles on groupoids
   arising from `N^k`-actions,” *Ergodic Theory Dynam. Systems* 42 (2022),
   3325--3356, DOI `10.1017/etds.2021.69`, Definition 3.7 supports the
   standard degree-one language: a continuous abelian-valued groupoid
   1-cocycle is a continuous groupoid homomorphism. Its later theorems have
   étale/local-homeomorphism hypotheses and do not source the proposed
   all-degree result on the actual owner.

These sources make the project feasible, but they also show why an
unqualified “the continuous groupoid cohomology” claim would be unsafe. The
amendment must freeze the Paper-12 complex by formula and give it a distinct
symbol, for example `H^*_{cnv}(G;underline(A))`, until Phase 2 proves exact
equivalence with a named published theory at matching hypotheses. If no such
source is found, the manuscript must call it author-defined continuous nerve
cohomology throughout.

**Mandatory amendment M1:** add the constant-bundle/action diagram, pullback
section interpretation, degeneracy/unnormalized clause, exact face maps, and
a fail-closed naming rule. Phase 3 must prove `d^2=0` directly and must not use
a standard-theory label to replace that proof.

### M2 — Generic, actual-orbit, packet, and global ownership must be split

**Anchor:** `candidate_lock.md` §§1--3; `research_protocol.md` §§1, 5, 9--11.

The phrase “inherited-indiscrete Deninger action groupoid” assigns too much to
one source. The locked chain actually has four different credits:

- Deninger owns the fixed-prime suspension action, packet membership, exact
  multiplicative stabilizer `p^Z`, and logarithmic clock conversion;
- Paper 9 owns the actual inherited indiscrete orbit/packet topology;
- Paper 11 owns the explicit range-first transformation-groupoid construction
  `G_{p,a}^act=X_{p,a} rtimes R` and arrow-time factorization;
- Paper 12 proposes the nerve complex, marked cohomology class, isotropy image,
  marked morphism categories, and standard period quotient.

Paper 9's source audit gives a feasible packet chain: Deninger physical
pp. 38--39, §6 and Theorem 6.1 provide the packet action and common
stabilizer `p^Z`; Paper 9 then owns actual packet indiscreteness. But the
initial Paper-12 bytes do not freeze the packet transformation groupoid.
They jump from a fixed-orbit owner indexed by `p,a` to `x in Gamma_p`.

**Mandatory amendment M2:** freeze these three positive owners and one
exclusion separately:

```text
G(X,alpha)                     generic arbitrary indiscrete R-action;
G_{p,a}^orb=X_{p,a} rtimes R  one actual fixed orbit, every p,a;
G_p^pkt=Gamma_p rtimes R      optional packet owner, every fixed p;
G^global                      excluded full Deninger suspension owner.
```

For `G_p^pkt`, state the additive action obtained from Deninger's positive
multiplicative flow, show explicitly that `p^Z` becomes `(log p)Z`, and bind
the common stabilizer for **every packet unit**. If any of those three arrows
cannot be source-verified, the packet statement is `NOT_TESTABLE` and must be
omitted rather than borrowed orbitwise. “Globally continuous” must always
mean a cochain defined on the full nerve of the one named owner; it must never
be read as a full-suspension or all-prime theorem.

The manuscript source-credit sentence must say “the Paper-11 transformation
groupoid built from Deninger's action,” not “Deninger's groupoid,” unless an
exact Deninger locator actually defines that topological groupoid.

### M3 — Weaker morphisms show non-invariance, not universal loss

**Anchor:** `research_protocol.md` primary question and §§6--7;
`candidate_lock.md` §§1, 3--4.

The intended direct statements are feasible:

```text
c' o F = c           => Per_{F_0(x)}(c') = Per_x(c),
c' o F = alpha c     => Per_{F_0(x)}(c') = alpha Per_x(c).
```

The explicit control with `alpha=M/L` is also algebraically plausible. But
the phrases “preserved precisely by strict marked morphisms,” “lost under
scaled or unmarked equivalence,” and “rigid only in the strictly marked
category” overstate what those formulas can prove:

- the unmarked category contains strict morphisms, so not every unmarked
  isomorphism loses the scale;
- positive-scaled morphisms with `alpha=1` are strict;
- for trivial, free, or scale-invariant dense period subgroups, a nonunit
  scaling may leave the subgroup unchanged; and
- one counterisomorphism between unequal lattices proves failure of
  **categorical invariance** in the weaker category, not pointwise loss under
  every weaker morphism.

The safe result is:

> Strict marked isomorphisms guarantee exact preservation. Positive-scaled
> isomorphisms obey the displayed covariance law. Period scale is not an
> invariant of the unmarked or positive-scaled category because explicit
> objects with unequal lattice generators are isomorphic there.

The protocol also calls `S(G,c)=R/Per(c)` functorial without defining a
category. A functor claim requires, before proof:

1. objects and admissible period subgroups;
2. morphisms, their unit maps, and the strict/scaled parameter law;
3. a target category of unbased homogeneous `R`-spaces;
4. the induced arrow on quotients and proofs of well-definedness,
   continuity, identity, and composition; and
5. a separate statement of how a chosen base unit changes `theta_x` by a
   rotation.

If only the isomorphism class `R/P` is established, call it an invariant
assignment, not a functor. The ordinary quotient topology and the one-sided
map to an indiscrete orbit are elementary Paper-12 direct proofs; they need no
borrowed inherited-topology credit.

**Mandatory amendment M3:** replace universal-loss language with the
covariance/non-invariance statement above; define the marked categories and
unit transport; either specify the quotient functor completely or lower the
target to an object-level standard quotient assignment.

### M4 — Standalone novelty and nonredundancy need an executable decision rule

**Anchor:** `research_protocol.md` §§1, 9, 11; `candidate_lock.md` §2.

The initial design recognizes the overlap risk but does not operationalize
it. Paper 11 already proves all continuous `T0`-valued arrow maps factor
through time, and Deninger/Paper 9 already own the stabilizer. The all-degree
nerve theorem may be a worthwhile extension, but “substantive” is not a test.

Phase 2 must compare the exact package against at least these nearest classes:

- continuous cochains on nerves/simplicial spaces;
- continuous cohomology of topological groups;
- topological-groupoid module and rigid/derived cohomology;
- continuous groupoid 1-cocycles and coboundaries;
- cocycle-preserving or graded groupoid isomorphisms;
- restriction to isotropy/vertex groups;
- homogeneous quotient reconstruction from an isotropy subgroup; and
- Deninger rational-Witt flow/stabilizer literature plus Papers 9--11.

The standalone decision must be fail-closed:

```text
STANDALONE only if the exact all-degree chain is not merely a cited standard
bar-complex fact after Paper 11, and the marked morphism/quotient package adds
a proved categorical result beyond re-reporting Deninger's stabilizer.

NOTE_OR_MERGE if the source audit reduces the contribution to Paper-11 arrow
factorization + a formal nerve corollary + Deninger's p^Z statement.
```

The packet corollary alone cannot rescue standalone status because the common
stabilizer is source-owned. Nor can elementary continuous Cauchy linearity or
the ordinary quotient topology carry novelty.

**Mandatory amendment M4:** add the bounded search protocol in §5 below,
name the nearest prior works before searching, and freeze the binary
`STANDALONE` versus `NOTE_OR_MERGE` test. Any novelty sentence remains
`SUPPORTED_WITHIN_SEARCH`; there is no absolute priority language.

## 4. Minor findings

### m1 — Introduce the cohomology-class period only after well-definedness

The lock defines `Per_x(b)=b(G_x^x)` and then writes `Per_x([b])` inside the
list of facts to be proved. Phase 3 should first define the restriction
homomorphism

```text
res_x:Z^1_cont(G;R) -> Hom_cont(G_x^x,R),
```

prove that every degree-one coboundary restricts to zero, and only then define
`Per_x([b])=image(res_x(b))`. Under a groupoid isomorphism the comparison is
between `x` and `F_0(x)`, not two untyped copies of the same unit.

**Mandatory amendment m1:** reorder the definition and include the unit-map
subscript in every preservation/covariance formula.

### m2 — Freeze the release-PDF boundary

The protocol excludes retained source PDFs from public synchronization, but
it does not yet distinguish the final manuscript PDF from local evidence or
say how unpublished internal dependencies appear in the bibliography.

**Mandatory amendment m2:** freeze the release bundle as follows:

- the generated Paper-12 manuscript PDF and declared textual/code supplement
  may be released only after manuscript, citation, declaration, and release
  gates pass;
- no `notes/sources/*.pdf` is a public supplement or is embedded/attached in
  the manuscript PDF;
- bibliography entries use canonical DOI, journal, publisher, arXiv, or
  author endpoints, never local paths or audit hashes;
- hashes remain audit locators in a reproducibility appendix, not substitutes
  for scholarly citations;
- if Papers 9 or 11 lack a public citable manifestation at release time,
  Paper 12 must either provide a citable companion-preprint record or restate
  the exact dependency needed for self-containment; and
- the public-sync dry run must list every released file and mechanically show
  that retained source PDFs are absent.

## 5. Mandatory Phase-2 source plan

This is a plan, not a completed Phase-2 search.

### 5.1 Exact local inheritance ledger

1. Reverify the five prior hashes in §1.
2. Bind Paper 9's exact theorem and source locators separately:
   actual inherited topology from its proof; Deninger action, packet, `p^Z`,
   and clock from the primary source.
3. Bind Paper 11 only for the range-first transformation groupoid, nerve
   degree-one arrow topology, and `T0` time factorization. Do not inherit its
   global-QC support, fibre, convolution, or completion objects into the
   Paper-12 cochain owner.
4. Record Paper 10's standard-circle direction as a comparison only. The
   standard quotient receives no actual-topology credit.

### 5.2 Framework/source matrix to acquire and preflight

At minimum, Phase 2 should retain or canonical-link exact manifestations for:

| Source class | Candidate source | Permitted use | Required ceiling |
|---|---|---|---|
| Deninger owner | *Dynamical systems for arithmetic schemes*, arXiv `1807.06400v4` | action, packet, stabilizer, log-time normalization | no topology/cohomology/groupoid credit beyond exact wording |
| topological-groupoid module/cochains | Mackenzie 1978, DOI `10.1017/S1446788700011794` | coefficient-bundle and nonhomogeneous-cocycle comparator | locally trivial/locally compact domain must be audited |
| simplicial continuous cochains | Blanco--Uribe--Waldorf 2023, DOI `10.4171/JNCG/528`, §§2.3--2.4 | nerve/unnormalized differential comparator | paracompactness/coefficient hypotheses; no automatic equality with derived theory |
| continuous groupoid degree one | Farsi--Huang--Kumjian--Packer 2022, DOI `10.1017/etds.2021.69`, Def. 3.7 | continuous 1-cocycle terminology | later étale/local-homeomorphism theorems not applicable automatically |
| continuous topological-group cochains | Fuchssteiner--Wockel, arXiv `1110.2977` and its published manifestation if available | naive continuous group cochain comparator | distinguish continuous-cochain theory from other topological group cohomologies |

Each retained PDF must receive the repository read-integrity preflight,
manifest entry, exact checksum, canonical endpoint, license note, and printed
versus physical page locators. A failed or unavailable PDF is an explicit
advisory or source substitution, never a silent locator `PASS`.

### 5.3 Claim-to-source/direct-proof allocation

| Proposed claim | Source/direct-proof owner |
|---|---|
| exact rational-Witt action, `p^Z`, and `log p` | Deninger primary source, with Paper-9 audit locator |
| actual inherited orbit/packet indiscreteness | Paper 9 theorem, not Deninger |
| actual range-first transformation groupoid and arrow factorization | Paper 11 direct theorem |
| constant coefficient bundle and published convention comparison | named primary cohomology sources, at exact hypotheses |
| `Psi_n` homeomorphism and every nerve open `X x U` | Paper 12 direct all-degree proof |
| `d^2=0` and `T_bullet d=d T_bullet` | Paper 12 direct simplicial/coordinate proof |
| continuous Cauchy equation implies `f(t)=lambda t` | Paper 12 direct elementary proof; cite as standard only if an exact source is retained |
| coboundaries vanish on isotropy and period is class-dependent | Paper 12 direct degree-one proof, with published cocycle convention comparator |
| strict/scaled covariance and `F_alpha` counterisomorphism | Paper 12 author-defined marked-category theorem |
| standard `R/P`, one-sided `theta_x`, and basepoint rotation | Paper 12 direct quotient/homogeneous-space proof |
| packet period corollary | Deninger common stabilizer + Paper-9 packet topology + explicit Paper-12 packet groupoid |
| exact-package absence/novelty | bounded search only; never sourced as a global absence fact |

### 5.4 Bounded exact-package novelty search

Freeze before searching:

- cutoff date and `last_searched_at` timestamp;
- databases/endpoints: MathSciNet or zbMATH where available, Crossref,
  arXiv, Google Scholar, Project Euclid, EMS, Cambridge Core, SpringerLink,
  and the relevant authors' publication lists;
- English search vocabulary plus symbol/notation variants;
- backward citation chaining from the five comparator classes above and
  forward citation chaining for Mackenzie, Deninger, and the continuous
  groupoid-cocycle sources;
- inclusion rule: a result counts as a direct precedent only if the same
  owner/domain, full unnormalized nerve complex, marked isotropy image, and
  strict/scaled/unmarked boundary are actually present;
- exclusion ledger with a reason for every nearest but inapplicable result.

Minimum query families:

```text
"continuous cohomology" AND groupoid AND (nerve OR composable tuples)
"continuous cochains" AND "action groupoid" AND indiscrete
"trivial coefficient bundle" AND groupoid cohomology
groupoid cocycle AND isotropy AND (restriction OR period group)
"cocycle-preserving" AND "groupoid isomorphism"
graded groupoid AND cocycle AND scaling
"R/LZ" AND action groupoid AND cohomology
Deninger AND (cocycle OR cohomology OR isotropy OR marked period)
"rational Witt" AND (groupoid cohomology OR cocycle)
```

The output must name the nearest prior work even when no direct precedent is
found. Allowed classification:

```text
SUPPORTED_WITHIN_SEARCH
```

with the databases, query families, date range, timestamp, and nearest prior
work attached. Forbidden classifications include `GLOBALLY_NEW`, `FIRST`,
`UNPRECEDENTED`, and any claim that absence was verified outside the search.

## 6. Feasibility adjudication by requested component

| Component | Feasibility | Exact condition |
|---|---|---|
| continuous topological-groupoid cohomology convention | **FEASIBLE AFTER M1** | freeze an author complex unless an exact published theory matches all hypotheses |
| trivial constant bundle | **FEASIBLE AFTER M1** | define `X x A -> X`, action, pullbacks, and trivialization |
| unnormalized nerve | **FEASIBLE AFTER M1** | retain degeneracies and use the identical `R` convention |
| isotropy restriction | **FEASIBLE** | direct proof first; then class/image notation |
| marked cocycle morphisms | **FEASIBLE AFTER M3** | covariance plus weaker-category non-invariance, not universal loss |
| fixed-orbit owner | **FEASIBLE** | Deninger action/stabilizer + Paper-9 topology + Paper-11 groupoid, with split credit |
| packet owner/common stabilizer | **FEASIBLE AFTER M2** | explicitly define `G_p^pkt` and rebind the common stabilizer on every packet unit |
| standard quotient | **FEASIBLE AFTER M3** | direct Paper-12 construction; functor only if categories/arrows are fully defined |
| continuous Cauchy fact | **FEASIBLE / DIRECT** | prove by rationals plus continuity; no novelty credit |
| bounded exact-package novelty search | **FEASIBLE AFTER M4** | run the preregistered limited search, not an absolute literature claim |
| standalone release PDF | **CONDITIONAL** | all findings, sources, proofs, search, citation, declarations, and release manifest must close |

## 7. Final decision

The exact source chain is feasible, including a packet-level common-period
corollary, but the initial bytes are not ready for Phase 2. The current lock
could misname an author continuous nerve complex as a standard cohomology
theory, over-credit Deninger with the transformation groupoid, promote a
fixed-orbit statement to an undefined packet owner, and state categorical
loss/functoriality more strongly than the proposed proofs support.

Required disposition:

```text
REVISE
C0 / M4 / m2
Phase 2 remains blocked.
```

After a versioned amendment closes M1--M4 and m1--m2, a fresh independent
source/domain re-lock may return `PASS` only with **C0/M0/m0** on the amended
exact bytes. This review itself does not authorize proof execution,
manuscript drafting, Route serialization, or public release.

---

## 8. Amended-v1 exact-byte source/scope re-lock addendum

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Review mode: **independent source/domain feasibility re-lock on amended-v1
bytes only**  
Verdict: **PASS — C0 / M0 / m0**  
Phase-2 disposition: **this reviewer's source/scope gate passes; the aggregate
Phase-1 gate and all downstream authorization remain governed by
`pipeline_state.md`**

### 8.1 Exact-byte boundary and independence

This addendum is bound to, and only to, the following amended-v1 tuple:

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/research_protocol.md` | `a923bfcf5fbae2d3136632794f0eb68ce4b7e48f217f0a071295e9fe4a85dda5` | exact lock matched |
| `notes/candidate_lock.md` | `0932d8a388ce732a3ad0702f3703cc91088d2fa73cc02f0a8063d240d70f5a42` | exact lock matched |
| `notes/pipeline_state.md` | `9cb7c51c534fd26f68fb66853312b022202c1d58b0ff2d74910c4deb3b32059b` | exact lock matched |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | exact lock matched |

I re-audited the amended protocol, candidate, pipeline, and versioned
amendment against this review's original M1--M4 and m1--m2. I did **not** read
either sibling Paper-12 Phase-1 review. I did not edit an active lock, proof
target, source artifact, Route record, or pipeline state; run a Phase-2
discovery or novelty search; prove a `P12-*` target; or treat an amendment
summary as evidence for a theorem. The initial review above remains the
unchanged historical review of its original tuple.

### 8.2 Disposition of the original findings

| ID | Amended-v1 disposition | Exact closure |
|---|---|---|
| M1 | **CLOSED** | The lock defines `underline(A)_X=X x A -> X` and the identity arrow action, gives the pullback-section interpretation after trivialization, retains degenerate simplices in an explicitly unnormalized complex, freezes every face and differential, requires a direct `d^2=0` proof, and caps naming at author-defined `C_cnv/H_cnv` until an exact matching published theory is proved. |
| M2 | **CLOSED** | The generic action groupoid, actual fixed orbit, actual fixed-prime packet, and excluded global suspension are separately typed. Source credit is split among Deninger's flow/packet/stabilizer/clock, Paper 9's actual inherited topology, Papers 11--12's transformation-groupoid definition, and Paper 12's proposed cohomology/category constructions. The packet result checks the same action, normalization, and stabilizer at every unit or returns `ORBIT_ONLY`. |
| M3 | **CLOSED** | The amended theorem states transported-unit covariance, strict preservation as the `alpha=1` sufficient case, and only existential non-descent in weaker categories. `C_str`, `C_scale`, and `C_un` have typed objects, arrows, unit maps, identities, composition, and inverses. The normalized strict functor has a typed pointed homogeneous-space target and explicit object/arrow maps, well-definedness, identity, composition, naturality, and basepoint-rotation obligations; scaled dilation is kept outside that target category. |
| M4 | **CLOSED** | `STANDALONE_PASS` and mandatory `NOTE_OR_MERGE` conditions are executable. The Phase-2 plan freezes a comparator set, domain ceilings, cutoff, endpoints, query families, backward/forward chaining, include/exclude rule, nearest-precedent requirement, unavailable-endpoint handling, and the sole negative-search ceiling `SUPPORTED_WITHIN_SEARCH`. |
| m1 | **CLOSED** | `res_x` is defined first, coboundary vanishing is a prior obligation, and only then is `Per_x([b])` defined; covariance consistently compares `x` with `F_0(x)`. |
| m2 | **CLOSED** | The release boundary distinguishes the releasable manuscript PDF and declared supplements from internal source PDFs, requires canonical scholarly endpoints rather than local paths or hashes, handles unpublished Paper-9/11 dependencies honestly, and requires an enumerated public-sync dry run proving zero retained source PDFs in the public payload. |

No residual source, domain, scope, nonredundancy, or release finding remains
at Phase-1 design level. In particular, the continuous Cauchy step remains a
direct elementary proof obligation with no novelty credit; the packet/common-
stabilizer result remains source-gated; and the ordinary standard quotient
remains distinct from the actual inherited orbit topology and from arbitrary
class-dependent value-space quotients.

### 8.3 Source-plan and claim-ceiling adjudication

The exact source chain is feasible on the amended design. Phase 2 now has an
executable plan for separately auditing the author-defined complex against
continuous nerve, topological-group, topological-groupoid-module, and
degree-one cocycle conventions; binding Deninger/Papers 9--11 at same-object
strength; deciding the packet gate; locating the nearest period-quotient and
marked-morphism precedents; and performing the bounded exact-package search.
Comparator hypotheses remain ceilings rather than imported assumptions.

This feasibility pass does **not** certify that `C_cnv/H_cnv` equals any named
published theory, that the packet checks succeed, that a direct precedent is
absent, that the package is standalone, or that any theorem, Route coordinate,
manuscript, citation set, or release artifact passes a later gate. Those
questions remain assigned to Phases 2 and 3 and to the final review/release
workflow.

### 8.4 Final amended-v1 decision

```text
PASS
C0 / M0 / m0
No further Phase-1 source/scope amendment is required on the locked bytes.
The aggregate pipeline remains blocked until every independent amended-byte
re-lock and the Phase-1 final gate pass.
```

---

## 9. Amended-v2 narrow source/scope regression re-lock addendum

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Review mode: **independent narrow source/scope regression re-lock on amended-v2
bytes only**  
Verdict: **PASS — C0 / M0 / m0**  
Phase-2 disposition: **this reviewer's v2 source/scope gate passes; the
aggregate Phase-1 gate and every downstream authorization remain controlled by
`pipeline_state.md`**

### 9.1 Exact-byte boundary and independence

This v2 addendum is bound to, and only to, the following tuple:

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/research_protocol.md` | `9c4947880f894dabb0648e9434fdf6e3a28cf2d9bf6434f86579370d8da80087` | exact lock matched |
| `notes/candidate_lock.md` | `1893cb74a5fc1a004873d5d027faf58bb384c3419699675dd37f33ee7b13c14f` | exact lock matched |
| `notes/pipeline_state.md` | `971489c1208ef32082bf936bf6c8b45661740d9b867857250a02798e02fafb62` | exact lock matched |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | exact v1 ledger matched |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` | exact v2 amendment matched |

I inspected only the amended-v2 packet/standalone branch, Route intake and
provenance records, their interaction with the already-passed owner/source
ceilings, and the retained release boundary. I did **not** read either sibling
Paper-12 review, run a Phase-2 literature or novelty search, prove a `P12-*`
target, inspect or create a Route YAML, or edit any active lock. The initial
review and v1 addendum above remain the immutable adjudications of their own
tuples.

### 9.2 Narrow regression checks

| Check | Verdict | Source/scope adjudication |
|---|---|---|
| Packet standalone branch | **PASS** | `PACKET_COROLLARY` is mandatory in the standalone eligibility list, executable decision rule, candidate decision lock, and final handoff. Failure of the same-action, same-clock, or every-unit common-stabilizer check yields `ORBIT_ONLY`, omits the packet claim, and forces `NOTE_OR_MERGE`. No packet theorem or source strength is silently assumed. |
| Owner and source-credit split | **PASS** | The generic, fixed-orbit, fixed-prime packet, and excluded global owners remain nonconflated. Deninger remains limited to the source flow, packet membership/common stabilizer, and logarithmic conversion; Paper 9 owns the actual inherited topology; Paper 11 owns the range-first groupoid construction; and Paper 12 owns its author-defined complex, categories, isotropy image, and standard quotient. Packet and orbit arithmetic fields remain conditional on the same-object source audit. |
| Complete Route metadata | **PASS** | Seven distinct candidate IDs now carry all seventeen required fields through candidate-specific and shared records. These fields describe later evaluator intake and proposed provenance; they neither certify a source, novelty, theorem, nor Route coordinate. Generic and unmarked controls retain `arithmetic_origin: NONE`, while the standard quotient explicitly receives only the copied period relation and no actual-topology credit. |
| No-Git provenance | **PASS** | The workspace has no Git repository or resolvable `HEAD`. The identical resolved value `unavailable-no-git-content-sha256-lock-required` appears in the protocol, candidate, and v2 ledger; it is not a pending commit placeholder. `P12-10` remains blocked until every named artifact exists and final implementation/content SHA-256 values are serialized in the YAML and route audit. |
| Release and citation boundary | **PASS** | Protocol §10.1 and candidate §8 retain the v1 separation between the releasable manuscript/supplement and internal `notes/sources/*.pdf`, canonical scholarly citations and audit hashes, unpublished internal dependencies and citable/self-contained replacements, and an enumerated public-sync dry run showing zero retained source PDFs. Route metadata does not weaken this boundary. |

The v2 changes do not reopen M1--M4 or m1--m2. The author-defined
constant-bundle unnormalized complex and naming ceiling, period-class ordering,
transported-unit covariance, typed strict quotient functor, bounded
nearest-precedent plan, and public-PDF/citation rules remain intact. No new
Critical, Major, or Minor source/scope finding is present.

### 9.3 Final amended-v2 decision

```text
PASS
C0 / M0 / m0
No further Phase-1 source/scope amendment is required on the locked v2 bytes.
The aggregate pipeline remains blocked until all three independent v2 re-locks
and the Phase-1 final gate pass.
```
