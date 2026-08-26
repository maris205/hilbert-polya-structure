# Paper 12 Phase-1 devil's-advocate mathematical/domain audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Audit scope: **INITIAL LOCKED BYTES ONLY**  
Verdict: **REVISE**

## Exact-byte lock receipt

| Audited artifact | SHA-256 | Status |
|---|---|---|
| `notes/research_protocol.md` | `1ea7e67825d5f543f472e1f4e0b3ea57a986269b24ec8dad1bf533475cc860eb` | exact match |
| `notes/candidate_lock.md` | `6a03983a76d34937f01ff03da4d074d1111b0722afff417a4532c5d7744f2975` | exact match |
| `notes/pipeline_state.md` | `4fe89540fb743e757e45ce71569261659a0d780db0c79ee5867792fe8ac936c0` | exact match |

The methodology review was not opened or used. No browsing, source discovery,
lock mutation, or Phase-3 proof/result inspection was performed. The Route-A
and Route-B repository skills were used only as evaluation-boundary contracts.

## Finding count and gate

```text
Critical: 1
Major:    5
Minor:    3
Total:    9
```

Phase 1 requires zero unresolved Critical, Major, or Minor findings. Therefore
this exact-byte package is **REVISE**, not PASS.

## Strongest counter-argument

The proposed complex-collapse theorem is mathematically plausible, but almost
all of its content follows from a simple topology fact: in the nerve
coordinates, points with the same time coordinates and different unit
coordinates are topologically indistinguishable, so a continuous map to a
`T0` coefficient cannot distinguish them. The marked-period statement then
evaluates the already chosen coordinate cocycle on an already supplied
stabilizer. Neither step selects an arithmetic scale. That makes categorical
precision decisive. As written, the primary claim overstates the morphism
boundary: strict marking guarantees exact preservation, but exact preservation
is not exclusive to strict morphisms, and scaled or unmarked morphisms do not
always lose a period subgroup. The quotient is also only an object assignment,
not yet a functor in a specified category. Unless the iff-like wording,
functor, packet gate, algebraic cohomology convention, deterministic controls,
and Route status are repaired, the paper's claimed standalone boundary is
formally stronger than the definitions support.

## Findings

### C1 — The core “precisely strict / lost when scaled or unmarked” claim is false

**Locators:** `notes/research_protocol.md:L23-L28`,
`notes/research_protocol.md:L216-L246`,
`notes/research_protocol.md:L279-L294`,
`notes/candidate_lock.md:L93-L95`,
`notes/candidate_lock.md:L143-L147`.

Strict marking is sufficient for exact preservation, but it is not necessary.
The morphism classes are nested at the level relevant here: a strict morphism
is also an `alpha=1` scaled morphism and can be regarded as an unmarked
morphism. Thus an unmarked morphism can preserve the period exactly.

More strongly, even a genuinely nontrivial scale can preserve the subgroup in
the protocol's own controls. For the one-unit trivial action, `P=R` and the
automorphism `F_alpha(*,t)=(*,alpha t)` has `c o F_alpha=alpha c` while
`alpha P=P=R` for every `alpha>0`. For the free translation action on an
indiscrete copy of `R`, `P={0}` and dilation likewise has
`alpha P=P`. For the dense-period control, `P=Q`, every positive rational
`alpha` satisfies `alpha Q=Q`. Hence “lost under scaled” is not a universal
claim either.

The valid theorem is the covariance statement

```text
Per_{F_0(x)}(c') = alpha Per_x(c)
```

for an `alpha`-scaled isomorphism, with strict preservation as the special case
`alpha=1`. What fails in the scaled/unmarked categories is *categorical
invariance of a nonzero lattice generator in general*, witnessed by the
`LZ -> MZ` counterisomorphisms; it is not preservation by an individual
morphism iff that morphism is strict.

**Decision impact:** Critical. The false iff/scale-loss wording occurs in the
primary research question and the claimed primary boundary.

### M1 — The morphism categories and period-quotient “functor” are not defined

**Locators:** `notes/research_protocol.md:L216-L271`,
`notes/candidate_lock.md:L53-L65`,
`notes/candidate_lock.md:L93-L97`.

The lock gives three equations on an arrow map `F`, but it does not freeze the
objects, require that `F` be a topological groupoid functor/homeomorphism, name
the induced unit map `F_0`, or define composition of scaled morphisms and their
scale labels. Section 7 then defines only the object
`S(G,c)=R/Per(c)`. It gives no codomain category and no arrow map `S(F)`, so no
functoriality, identity law, or composition law is presently a testable claim.

This omission matters: for a strict morphism the natural candidate is
`S(F)([t]_P)=[t]_{P'}` after proving `P=P'`; for an `alpha`-scaled morphism the
equally natural candidate is `[t]_P -> [alpha t]_{P'}` after proving
`P'=alpha P`. Whether the latter is a morphism depends on whether the codomain
uses strictly `R`-equivariant maps or permits semilinear time rescaling. The
claimed “functorial ceiling” cannot be decided until that category is frozen.

**Decision impact:** Major. Period-quotient functoriality is a standalone gate,
but the locked bytes do not yet state a functor.

### M2 — Packet scope is undefined behind a circular phase gate

**Locators:** `notes/research_protocol.md:L206-L214`,
`notes/research_protocol.md:L315-L345`,
`notes/candidate_lock.md:L16-L19`,
`notes/candidate_lock.md:L57-L58`,
`notes/candidate_lock.md:L154-L159`,
`notes/pipeline_state.md:L7-L10`.

`Gamma_p`, the packet object, its point set, its action, and the relation of the
normalized label `a` to its units are not defined in the locked bytes. The
protocol says the packet claim is `NOT_TESTABLE` until Phase 2 binds those
data, while Phase 2 is blocked until Phase 1 passes; Phase 1 in turn says packet
ambiguity must already be closed. This is a gate deadlock, not merely a pending
source citation.

**Decision impact:** Major. The packet decision is both a standalone-eligibility
condition and an explicit Phase-1 closure condition.

### M3 — `Z`, `B`, and `H` are not frozen as algebraic cohomology objects

**Locators:** `notes/research_protocol.md:L84-L130`,
`notes/research_protocol.md:L145-L160`,
`notes/candidate_lock.md:L75-L92`.

The cochain groups and differentials are specified, but the lock never defines
`Z_cont^n=ker d^n`, `B_cont^n=im d^{n-1}`, or
`H_cont^n=Z_cont^n/B_cont^n`, nor does it state whether the quotient is purely
algebraic. No topology on a cochain space or quotient is specified. Therefore
`H_cont^1(G;R)=R[c]` is sound only if read as an algebraic real vector-space
statement; it is not presently a theorem about a topological cohomology group.

**Decision impact:** Major. The paper title and primary result use cohomology,
so the category of the asserted `H^1` object cannot remain implicit.

### M4 — P12-9 is called deterministic/reproducible but its controls are not frozen

**Locators:** `notes/research_protocol.md:L277-L314`,
`notes/research_protocol.md:L317-L330`,
`notes/candidate_lock.md:L64-L69`.

The list names “random integer,” “random” clock, arbitrary labels, an explicit
non-`T0` cochain, and a nontransitive action, but fixes no witness values,
seed/generator, finite test matrix, expected outputs, executable command, or
artifact/hash schema. Several controls can and should be theorem-level exact
witnesses, but those witnesses are not present in the design. As a result,
different Phase-3 implementations could satisfy different tests while all
claiming P12-9.

**Decision impact:** Major. Deterministic adversarial controls and reproduction
are an active target and a standalone gate.

### M5 — A formal Route-A evaluation is `NOT_TESTABLE` on the frozen inputs

**Locators:** `notes/research_protocol.md:L317-L330`,
`notes/research_protocol.md:L351-L371`,
`notes/candidate_lock.md:L122-L141`,
`notes/candidate_lock.md:L143-L152`,
`notes/pipeline_state.md:L11-L12`,
`skills/route-a-evaluator.md:L49-L72`,
`skills/route-a-evaluator.md:L185-L222`.

The Route-A contract rejects an evaluation as `NOT_TESTABLE` when the
determinant convention or data split is missing. Those inputs are deliberately
excluded here, along with a dynamical zeta/determinant target. Consequently
P12-10 cannot be a formal Route-A evaluation that assigns `A2_FAIL`, `A3_FAIL`,
and `A4_FAIL`; on these bytes it is a route-boundary or stop-scope record.
Likewise, a period/repetition subgroup does not by itself meet A1's primitive
orbit, phase, multiplicity, stability, enumeration, and completeness checks.
The lock may state design ceilings, but it must not serialize absent layers as
evaluated failures.

`Route B invocation false` is correct and should remain. No Route-B YAML is
authorized.

**Decision impact:** Major. The current P12-10 target conflicts with the
repository evaluator's mandatory-input semantics.

### m1 — The explicit `G_L` control omits its action

**Locators:** `notes/research_protocol.md:L229-L240`.

`G(X,alpha)` depends on an action, but `X_L=R/LZ` is followed directly by
`G_L=X_L rtimes R` without freezing `[r]_L dot t=[r+t]_L`. The proposed
`F_alpha` is correct for that translation action, but not for an unspecified
action on the same set.

**Decision impact:** Minor. One line closes the owner and makes every functor
check unambiguous.

### m2 — The non-`T0` negative control needs a nontrivial unit space

**Locators:** `notes/research_protocol.md:L53-L66`,
`notes/research_protocol.md:L130`,
`notes/research_protocol.md:L288-L294`.

The generic theorem permits singleton `X`. Removing `T0` does not force
factorization failure for a singleton unit space. The negative witness must
instead freeze `|X|>=2`, a concrete non-`T0` topological abelian group (for
example a nontrivial abelian group with the indiscrete topology), and a
continuous cochain taking topologically indistinguishable coefficient values
on two unit fibers.

**Decision impact:** Minor. The intended existential counterexample is valid,
but its quantifier and witness are not locked.

### m3 — The scale-blind lattice statement is placed under a generic stabilizer claim

**Locators:** `notes/research_protocol.md:L163-L188`.

Items 1--4 apply to arbitrary stabilizers, including the protocol's `R`,
`{0}`, and `Q` controls. Item 5 speaks specifically of “scaled discrete
lattices” and an “original positive generator,” which exists only after adding
`H_x=LZ` with `L>0`. The statement is correct under that hypothesis:
`{lambda LZ:lambda!=0}` is the collection of all nonzero rank-one lattices,
independent of `L`.

**Decision impact:** Minor. Add the missing discrete nonzero-lattice
hypothesis; do not present item 5 as a generic stabilizer theorem.

## Claims that survived direct attack

These are not Phase-3 proofs or pre-certifications; they record that no
counterexample was found in the locked definitions after checking the stated
universal quantifiers.

1. **All-degree nerve topology:** for every finite `n>=1`, `G^n` has the form
   `X^n x R^n` with `X^n` indiscrete. Intersecting its opens with the composable
   nerve yields exactly `X x U` in `Psi_n` coordinates. The inverse reads the
   first range unit and the `n` time coordinates, so the proposed
   homeomorphism is coherent for arbitrary actions.
2. **`T0` factorization:** points `(x,t_vector)` and `(y,t_vector)` are
   topologically indistinguishable. A continuous map to a `T0` space identifies
   them, and a fixed-unit section proves the resulting time function is
   continuous. This supports degreewise bijectivity of `T_n`, including the
   constant degree-zero case.
3. **Differential:** the frozen range-first formula gives
   `d^1 f(t,u)=f(u)-f(t+u)+f(t)` after time factorization and is consistent with
   `d^0h=h(s)-h(r)`. No sign counterexample was found; an all-degree cosimplicial
   or direct cancellation proof remains a Phase-3 obligation.
4. **Real degree one:** algebraically, the cocycle equation makes the factored
   function continuous additive, hence `f(t)=lambda t`; real-valued continuous
   zero-cochains on nonempty indiscrete `X` are constant, hence `B^1=0`.
   M3 governs the meaning of `H^1`.
5. **Isotropy restriction:** a trivial-coefficient 1-cocycle restricts to a
   homomorphism on `H_x`; coboundaries vanish on isotropy; and
   `Per_x(lambda c)=lambda H_x`. Stabilizers at points of a transitive abelian
   action agree. The source-specific equality `H_x=(log p)Z` was not checked
   and remains source-gated.
6. **Explicit lattice dilation:** after freezing the translation action as in
   m1, `F_alpha([r]_L,t)=([alpha r]_M,alpha t)` with `alpha=M/L` is a
   topological groupoid isomorphism and satisfies `c_M o F_alpha=alpha c_L`.
7. **One-sided topology:** for `P=LZ`, `L>0`, the based equivariant bijection
   from usual Hausdorff `R/P` to a nontrivial indiscrete orbit is continuous;
   its inverse is not. This gives no transport of the actual inherited
   topology.
8. **Arithmetic specificity:** the trivial, free, arbitrary-period, dense, and
   label controls correctly show that the generic complex and marked-period
   mechanisms do not select primes or `log p`. Any arithmetic credit must come
   only from a same-object source relation.

## Mandatory repair checklist

- [ ] Replace every iff-like “precisely strict” / “lost under scaled or
      unmarked” statement with the exact covariance formula; state only that
      strict morphisms guarantee equality and that scaled/unmarked categories
      admit counterexamples to lattice-generator invariance.
- [ ] Define the strict, scaled, and unmarked categories completely: objects,
      topological functors/isomorphisms, unit maps, scale labels, identities,
      composition, and inverses.
- [ ] Define the period-quotient functor's codomain and arrow map. Decide
      explicitly whether scaled dilation is admitted or excluded by the
      codomain's morphism notion, and prove identities/composition.
- [ ] Break the packet gate deadlock: either freeze the exact `Gamma_p` owner,
      action, topology, unit/label quantifiers, and Phase-2 verification input,
      or record `ORBIT_ONLY` and remove packet closure from the Phase-1 and
      standalone gates until a versioned relock.
- [ ] State that `Z_cont^n`, `B_cont^n`, and `H_cont^n` are kernels, images, and
      algebraic quotients in abelian groups (and real vector spaces for
      `A=R`); disclaim any topological quotient claim unless cochain-space
      topologies are separately defined and proved.
- [ ] Freeze deterministic controls: exact `L` values (prime/composite/random/
      nonarithmetic), an explicit nontransitive action, an explicit non-`T0`
      coefficient/cochain witness, fixed label permutations, exact expected
      outputs, and the reproduction artifact/command/hash schema. Eliminate
      unfrozen uses of “random” or supply a seed and generator.
- [ ] Replace P12-10's formal Route-A evaluation with a
      `NOT_TESTABLE`/`STOP_SCOPED` route-boundary record unless all mandatory
      Route-A inputs are introduced. Do not award A1 from a period subgroup
      without the primitive-orbit obligations. Keep Route B false and emit no
      Route-B YAML.
- [ ] Freeze the translation action `[r]_L dot t=[r+t]_L` in the `G_L` control.
- [ ] Scope the non-`T0` control to a unit space with at least two points and
      provide the explicit coefficient group and cochain.
- [ ] Condition the scale-blind lattice statement on `H_x=LZ`, `L>0`, and write
      period preservation at the corresponding unit `F_0(x)`.
- [ ] After repairs, create versioned amended locks, recompute all three SHA-256
      values, and obtain fresh independent exact-byte Phase-1 reviews. Do not
      status-edit these initial locks in place.

---

# Amended-v1 independent exact-byte re-lock

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **amended-v1 design bytes only**  
Verdict: **REVISE**

## Amended tuple receipt

| Audited artifact | SHA-256 | Status |
|---|---|---|
| `notes/research_protocol.md` | `a923bfcf5fbae2d3136632794f0eb68ce4b7e48f217f0a071295e9fe4a85dda5` | exact match |
| `notes/candidate_lock.md` | `0932d8a388ce732a3ad0702f3703cc91088d2fa73cc02f0a8063d240d70f5a42` | exact match |
| `notes/pipeline_state.md` | `9cb7c51c534fd26f68fb66853312b022202c1d58b0ff2d74910c4deb3b32059b` | exact match |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | exact match |

The pre-append historical report hash was
`f861957d59ff63ccc1aa3328c3bcb2c8a293d2115f69f845f0ae4f77e3ab11cf`,
matching the amendment ledger. No sibling review, Phase-2 artifact, Phase-3
proof/result, or external source was read. No browsing was performed.

## Amended finding count

```text
Critical: 0
Major:    1
Minor:    0
Total:    1
```

The amended lock requires `C0/M0/m0`. One Route-input defect remains, so the
exact amended tuple is **REVISE**, not PASS.

## Initial-finding re-attack ledger

| Initial finding | Amended-v1 result | Exact amended locator and attack result |
|---|---|---|
| `C1` false iff/universal scale loss | **CLOSED** | `research_protocol.md:L23-L30,L349-L387`; covariance is exact, strictness is only sufficient, unequal-period maps prove existential non-descent, and `F_-`, `R`, `{0}`, and `Q` explicitly defeat any converse/universal-loss wording. |
| `M1` untyped categories/quotient functor | **CLOSED** | `research_protocol.md:L322-L434`; objects, unit maps, topological isomorphisms, scale composition/inverses, target category, `S(F)`, identities, composition, naturality, basepoint rotation, and the scaled semilinear stop are all frozen coherently. |
| `M2` packet deadlock/undefined owner | **CLOSED** | `research_protocol.md:L274-L320` and `candidate_lock.md:L19-L24,L59-L75`; orbit, packet, and excluded global owners are separated, exact Phase-2 inputs are named, every packet unit is quantified, and failure deterministically returns `ORBIT_ONLY`. |
| `M3` undefined algebraic `H` | **CLOSED** | `research_protocol.md:L108-L206` and `candidate_lock.md:L103-L114`; the author-defined unnormalized constant-bundle complex, faces, `Z`, `B`, and algebraic `H` are explicit, with no cochain or quotient topology claimed. |
| `M4` nondeterministic controls | **CLOSED** | `research_protocol.md:L440-L479` and `candidate_lock.md:L148-L168`; exact carriers/actions/witnesses, fixed constants, tolerance boundary, paths, manifest, two-generation identity, tamper checks, and test floor replace every post-hoc random choice. |
| `M5` Route intake/status | **REOPENED IN PART AS A-M1** | The determinant absence and A1/Route-B ceilings are repaired, but the purported complete mandatory intake still omits required Route-A fields; see A-M1. |
| `m1` missing `X_L` action | **CLOSED** | `research_protocol.md:L363-L375`; `[r]_L dot t=[r+t]_L` and every `F_alpha` obligation are frozen. |
| `m2` unscoped non-`T0` witness | **CLOSED** | `research_protocol.md:L445-L455`; `NON-T0-A2` fixes a two-point indiscrete unit space, indiscrete `Z/2Z`, and an explicit nonconstant continuous degree-zero cochain. |
| `m3` generic/discrete lattice conflation | **CLOSED** | `research_protocol.md:L255-L272`; scale-blindness is expressly conditional on `H_x=LZ`, `L>0`, and covariance uses `F_0(x)`. |

## Remaining finding

### A-M1 — The claimed complete Route-A intake omits six mandatory fields

**Severity:** Major  
**Confidence:** 5/5 — direct schema comparison  
**Evidence anchor:** `text: research_protocol.md:L584-L607 and candidate_lock.md:L218-L240, compared with skills/route-a-evaluator.md:L34-L72`

The amendment says the later Route-A evaluation “has every mandatory input
field,” and the protocol calls its block the common Route input record. The
repository Route-A contract requires these seventeen keys:

```text
candidate_id, candidate_definition, family, phase_space, dynamics,
parameters, parameter_provenance, arithmetic_origin, clock, normalization,
determinant_convention, orbit_cutoff, precision, training_data,
forbidden_data, code_commit, artifact_paths.
```

The amended record serializes only eleven of them. It omits the literal fields
`candidate_id`, `family`, `phase_space`, `dynamics`, `parameters`, and
`parameter_provenance`. Related prose elsewhere does not close an exact-schema
intake, especially because the “common” record ranges over generic, actual,
standard-quotient, scaled, and unmarked owners with different dynamics,
parameters, clocks, and arithmetic provenance. In addition,
`code_commit: LOCAL_CONTENT_HASH_LOCK_PENDING_BATCH_SYNC` is a pending
placeholder, not the required immutable value; the exact gate for replacing it
before evaluation is not stated in the Route block.

The negative determinant value
`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT` is an adequate explicit negative
convention for a fail-closed boundary record; it supplies no determinant and
earns no A2 credit. The A1 obligation list, arbitrary-period controls, Route-B
false flag, and no-Route-B-YAML rule are coherent. The remaining defect is the
false completeness claim and non-serialized per-owner intake, not the use of a
negative determinant sentinel.

**Decision impact:** P12-10 is an active target, and Phase 1 expressly requires
every Route ambiguity to close on exact bytes. A formal evaluator cannot consume
the promised mandatory schema as written.

## Mandatory amended-v1 repair

- [ ] Replace the “common Route input record” with a per-evaluated-owner Route-A
      intake containing every required literal key: add `candidate_id`,
      `family`, `phase_space`, `dynamics`, `parameters`, and
      `parameter_provenance` alongside the eleven present keys.
- [ ] Give each owner one unambiguous value rather than conditional prose such
      as “where applicable”; an unmarked/control owner with no clock or
      arithmetic origin must carry the explicit negative value and accept the
      evaluator's resulting `NOT_TESTABLE`/failure classification.
- [ ] Add an exact pre-evaluation gate replacing
      `LOCAL_CONTENT_HASH_LOCK_PENDING_BATCH_SYNC` with the immutable synced
      commit/content identifier and binding concrete artifact paths. Until
      replacement, Route evaluation remains blocked.
- [ ] Preserve `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`, the no-A2-credit
      boundary, evaluator ownership of A0/A1, Route B false, and the prohibition
      on Route-B YAML.
- [ ] Version and rehash the repaired protocol/candidate/amendment tuple, then
      obtain a fresh independent devil/domain exact-byte re-lock. Do not advance
      Phase 2 from this `C0/M1/m0` result.

## Repaired-logic coverage receipt

No additional Critical, Major, or Minor defect was found after independently
attacking the following amended surfaces:

1. every finite-degree nerve topology claim and the `T0` factorization inverse;
2. constant-bundle continuity, unnormalized face differential, and algebraic
   `Z/B/H` typing;
3. real `H_cnv^1`, isotropy restriction, representative independence, and the
   discrete-lattice-only scale-blindness statement;
4. covariance versus iff, unequal-lattice non-descent, orientation reversal,
   and the scale-invariant `R`, `{0}`, and rational-`Q` cases;
5. strict/scaled/unmarked identity, composition, inverse, and transported-unit
   laws;
6. normalized coordinate-clock orbit quotient versus arbitrary-class
   value-space quotient, strict functor laws, one-sided topology, and scaled
   semilinear exclusion;
7. fixed-orbit, fixed-prime packet, and excluded global ownership, including
   the `ORBIT_ONLY` fail path;
8. every exact control witness, including `NON-T0-A2`, test/manifest contract,
   and proves-too-much interpretation;
9. executable standalone/note-or-merge and bounded Phase-2 novelty gates; and
10. downstream blocking, source-PDF exclusion, canonical citation endpoints,
    companion-dependency handling, and public-sync release gates.

---

# Amended-v2 narrow independent exact-byte re-lock

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **amended-v2 Route correction plus specified regressions only**  
Verdict: **PASS**

## Amended-v2 tuple receipt

| Audited artifact | SHA-256 | Status |
|---|---|---|
| `notes/research_protocol.md` | `9c4947880f894dabb0648e9434fdf6e3a28cf2d9bf6434f86579370d8da80087` | exact match |
| `notes/candidate_lock.md` | `1893cb74a5fc1a004873d5d027faf58bb384c3419699675dd37f33ee7b13c14f` | exact match |
| `notes/pipeline_state.md` | `971489c1208ef32082bf936bf6c8b45661740d9b867857250a02798e02fafb62` | exact match |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | exact unchanged v1 ledger |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` | exact match |

The pre-append report hash was
`8dce153cb25760729237d264fbe74f5cbf3403e553627526f47f78d9d70413c7`,
matching the immutable v1 history. No sibling report, Phase-2 material,
Phase-3 proof/result, or external source was read; no browsing was performed.

## Finding count

```text
Critical: 0
Major:    0
Minor:    0
Total:    0
```

The narrow amended-v2 devil/domain gate is **PASS C0/M0/m0**.

## Closure of amended-v1 A-M1

**Status: CLOSED.**

The seven Route owners are nonconflated and each now carries the first ten
mandatory Route-A fields at `research_protocol.md:L585-L671`:

```text
candidate_id
candidate_definition
family
phase_space
dynamics
parameters
parameter_provenance
arithmetic_origin
clock
normalization
```

The shared tail at `research_protocol.md:L673-L689` applies the remaining seven
mandatory fields to every owner:

```text
determinant_convention
orbit_cutoff
precision
training_data
forbidden_data
code_commit
artifact_paths
```

A direct count over the seven owner records found exactly seven occurrences of
each owner-specific key. The candidate lock independently tabulates the same
seven IDs, their six formerly missing fields, and seven distinct exact YAML
paths at `candidate_lock.md:L219-L245`.

The required records are:

1. `GEN-INDISC-R-ACTION-CNV`;
2. `DEN-EF-ACTUAL-ORBIT-CNV-P-A`;
3. `DEN-EF-ACTUAL-PACKET-CNV-P`;
4. `DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A`;
5. `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P`;
6. `DEN-EF-STANDARD-PERIOD-QUOTIENT-P`; and
7. `UNMARKED-PERIOD-SCALING-CONTROL`.

Each row has the exact YAML path
`evaluations/route_a/<candidate_id>/2026-08-15-stage12.yaml`; the candidate
table expands the placeholder to a literal path for every ID. The common
artifact list fixes `proof_audit.md`, `results/manifest.json`,
`phase3_peer_review.md`, and `route_audit.md`. Section 8 separately freezes the
implementation paths `code/generate_controls.py`, `code/test_controls.py`, and
`experiments/reproduce.sh`.

`P12-10` is explicitly blocked until every required artifact exists and the
final implementation/artifact SHA-256 values are serialized in the YAML and
route audit. The workspace diagnostic `git rev-parse --is-inside-work-tree`
returns exit 128 (“not a git repository”), so
`unavailable-no-git-content-sha256-lock-required` is a resolved provenance
state rather than a disguised pending commit. Mandatory content hashes are the
mechanical substitute; no Route execution is authorized before they exist.

`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT` remains an explicit negative convention,
not determinant evidence. It gives no A2 credit and cannot be upgraded without
a fresh owner/protocol. The formal evaluator retains A0/A1 authority, a period
subgroup alone does not pass A1, and Route B invocation remains false with no
Route-B YAML.

## Regression coverage receipt

No regression was found in the required surfaces:

- **Covariance/non-descent:** `research_protocol.md:L323-L388` retains
  transported-unit covariance, strict sufficiency without an iff converse,
  unequal-period existential non-descent, orientation reversal, and the
  scale-invariant `R`, `{0}`, and rational-`Q` controls.
- **Algebraic domains:** `research_protocol.md:L108-L237` retains the
  author-defined unnormalized constant-bundle complex and purely algebraic
  `Z/B/H`, with no cochain-space or quotient-topology claim.
- **Packet and standalone branch:** `research_protocol.md:L39-L65,L274-L321`
  and `candidate_lock.md:L191-L196` now agree exactly:
  `PACKET_COROLLARY` is mandatory for `STANDALONE_PASS`, while any packet-gate
  failure produces `ORBIT_ONLY` and forces `NOTE_OR_MERGE`.
- **Controls:** `research_protocol.md:L441-L480` retains all exact witnesses,
  the explicit non-`T0` counterexample, tolerance boundary, two-generation
  identity, tamper/drift rejection, test floor, and the rule that finite
  controls do not prove universal theorems.
- **Route and release stop:** `research_protocol.md:L691-L730` and
  `pipeline_state.md:L9-L21` retain artifact/hash preconditions, negative
  A2/A3/A4 ceilings, Route B false, no Route-B YAML, Phase-2/3 blocking, and no
  premature manuscript or source-PDF release.

## Mandatory repair checklist

None. This narrow review found zero unresolved Critical, Major, or Minor
finding on the exact amended-v2 tuple.
