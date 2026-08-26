# Paper 10 Phase-3 rigorous proof audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Primary verdict: **CONFIRM_COLLAPSE on every registered actual owner**  
Proof findings: **0 Critical / 0 Major / 0 Minor**  
Deterministic-control execution: **not run in this proof-only phase**  
Route-B invocation: **false**

## 1. Exact lock and evidence binding

This audit is bound to the final Phase-1 tuple:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `4fe51d7dc9514dea101178995dec73e120ab7032b11c06ecd4bc0efadf9cbc58` |
| `notes/candidate_lock.md` | `4cc6cae36630e13623d638a5eac7daaab084eef9549f4ca3bd44b026a32d26cf` |
| `notes/phase1_design_amendment.md` | `e0e3fb42c2285b8c5da521f05588581e7981de8957e33aa3cf237f653d1c432f` |
| `notes/pipeline_state.md` | `75cec92ff33ef52a456304361d6df5c26c055164adecbffb7f603b63e195e5ce` |
| `notes/phase1_final_gate.md` | `bdc5e3698110695a84f392c47bb907b7cf8ddc8807ea9af04654791090e4ab68` |

The final Phase-2 evidence tuple is:

| Artifact | SHA-256 |
|---|---|
| `notes/phase2_source_novelty_audit.md` | `8b4a2ff1ed911765faa294c43cfbfb9f4986624e972ee4bcb509b12321e658fa` |
| `notes/sources/scope_source_manifest.md` | `38fd6557eba364eff748b35a62ac28bf768b75a259e1e7631099149f67118140` |
| `notes/sources/scope_sources.sha256` | `222c1a6d9552c82890bcc3846245fb4c636eef981a5937b7355d45f5626497aa` |
| `notes/phase2_domain_source_audit.md` | `8dbc4e6487d342bcf352a4b0161bc1c4f17800d07556a3d11b49ce900b3aa582` |
| `notes/sources/dom-source-manifest.md` | `49e20c34eff26915780f43b5df7d5b6635fa35d6225b63ea476cbeab1c14af21` |
| `notes/sources/dom-sources.sha256` | `34ed23b73f01f5027deaa5084bce250d5f77c1dbcd02c38627c950e5803d13ce` |
| `notes/phase2_precedent_search.md` | `68aef453788251edb0e7aad631ea58ca1794fc23e255d5c96b3d8c39030d5719` |
| `notes/phase2_final_gate.md` | `1421ada08a7192e14e7edf4ab9982523c275063dee0c23c1d2f076ac4bf13ffb` |

The only arithmetic-topology theorem imported is Paper 9's result that, for
every rational prime `p`, each of

```text
ACT-PACKET-p,
ACT-ORBIT-p-a for every a in U_p/H_p,
ACT-Q-p
```

is a nonempty, nontrivial indiscrete space. Its exact proof and source audits
remain unchanged:

| Paper-9 artifact | SHA-256 |
|---|---|
| `papers/9-packet-separation/notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` |
| `papers/9-packet-separation/notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` |
| `papers/9-packet-separation/results/packet_separation_manifest.json` | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` |

No topology is imported through the set bijections `phi_p` or `beta_{p,a}`.

## 2. Standard reduction: one nonempty indiscrete space

This section is a standard general lemma, not a new arithmetic theorem. Let
`X` be a nonempty indiscrete space, so `tau_X={emptyset,X}`.

### Lemma 2.1 — maps into separated topological targets

If `Y` is `T0`, every continuous `f:X->Y` is constant.

**Proof.** If `f(x)!=f(y)`, the `T0` property supplies an open set of `Y`
containing exactly one of these two values. Its inverse image is a nonempty
proper open subset of `X`, a contradiction. QED.

The target assumption is sharp. If `Y` is a two-point indiscrete space, every
set map `X->Y` is continuous, including nonconstant maps when `|X|>1`.

### Lemma 2.2 — topological indistinguishability and direct UMPs

All points of `X` have the same open-neighbourhood filter. Hence the relation
`~_0` has one class and

```text
K0(X)=X/~_0={*}
```

with the one-point quotient topology. Let `q_0:X->{*}` be the quotient map.
For every continuous `f:X->Y` with `Y` `T0`, Lemma 2.1 makes `f` constant,
so there is exactly one map `f_bar:{*}->Y` with `f=f_bar o q_0`; every map
from a one-point space is continuous. This proves existence, continuity, and
uniqueness, not merely the cardinality of the quotient.

The same one-point space and the same unit give the direct universal property
against all Hausdorff targets and, separately, all completely regular and
Hausdorff targets. Those targets are `T0`, and the one-point space belongs to
both full subcategories. Thus, for this exact `X`,

```text
K0(X)=Sep_H(X)=Sep_CRH(X)={*}
```

as directly verified universal images. No assertion that an arbitrary
subcategory is reflective for every topological space is needed.

### Lemma 2.3 — scalar observables

Since `C` is Hausdorff, every member of `C(X)` is constant. The map

```text
C -> C(X),        c |-> c 1_X
```

is a unital `*`-algebra isomorphism. Every constant function is bounded, so
only now may one conclude

```text
C(X)=C_b(X)={c 1_X:c in C}.
```

Because `X` is nonempty, `||c 1_X||_infinity=|c|`; hence the displayed
isomorphism is isometric after the supremum norm is attached. If `X` has more
than one point, neither algebra separates points, and for all `x,y in X`,

```text
ev_x=ev_y:C(X)->C.
```

This is not a Gelfand-duality or compact-Hausdorff representation theorem.

### Lemma 2.4 — Borel and measurable collapse

The topology is already a sigma-algebra, so

```text
B(X)={emptyset,X}.
```

Let `(Y,Sigma_Y)` be countably separated, with a countable measurable family
`(E_n)` separating points. If `f:(X,B(X))->(Y,Sigma_Y)` is measurable, then
each `f^{-1}(E_n)` is either `emptyset` or `X`. Thus any two values in the
image have identical membership in every `E_n`, and separation forces them
to be equal. Hence every such measurable map is constant. In particular this
holds for every standard Borel target.

If `X` is nontrivial, `(X,B(X))` is itself not countably separated: neither
of its two measurable sets separates two distinct points. It is therefore not
a standard Borel space. The negative control is again exact: every map from
`X` to a two-point space with the trivial sigma-algebra is measurable, so
nonconstant measurable maps exist when target separation is removed.

### Lemma 2.5 — positive finite measures and Dirac collapse

For `mu in Mfin+(X)`, put `m=mu(X)`. Then `m in [0,infinity)` and the entire
measure is

```text
mu(emptyset)=0,       mu(X)=m.
```

Conversely every `m>=0` defines a positive countably additive finite measure
by these equations. Therefore total mass is a cone bijection

```text
Mfin+(X) <-> [0,infinity).
```

For `x in X`, define `delta_x` only on measurable `A` by
`delta_x(A)=1` if `x in A` and `0` otherwise. Since the only measurable sets
are `emptyset` and `X`, every `delta_x` is the same mass-one measure. When `X`
is nontrivial, a proper singleton `{x}` is not measurable; the proof never
evaluates `delta_x({x})` and makes no support claim.

No signed/complex-measure, regularity, Radon, Haar, state, disintegration, or
trace conclusion follows from this classification.

### Lemma 2.6 — fixed bounded-operator targets

Fix `H_0=ell^2(N)`. The norm topology on `B(H_0)` is Hausdorff. The SOT is
Hausdorff because, for `A!=B`, some vector `xi` has `(A-B)xi!=0`, and the
evaluation seminorm at `xi` separates them. The WOT is Hausdorff because one
may additionally choose `eta` with `< (A-B)xi,eta > !=0`. Consequently each
of

```text
B(H_0)_norm,       B(H_0)_SOT,       B(H_0)_WOT
```

is a `T0` target, and every continuous map from `X` to each named target is
constant. These are three separate map classifications on one fixed carrier;
they say nothing about measurable fields, group representations, unbounded
operators, domains, or traces.

## 3. P10-1--P10-5 on the actual rational-Witt owners

Fix an arbitrary rational prime `p`; where relevant fix arbitrary
`a in U_p/H_p`. Apply Section 2 separately to each exact Paper-9 owner
`ACT-PACKET-p`, `ACT-ORBIT-p-a`, and `ACT-Q-p`. Nonemptiness and
nontriviality are the only Paper-9 inputs used by the standard reduction.

### P10-1 — separated reflections: PROVED / SINGLETON

For every registered actual object, topological indistinguishability is the
universal relation. Its `K0`, Hausdorff universal image, and completely
regular and Hausdorff universal image are one-point spaces. The three units
are the unique maps from the actual object to `{*}`, and each satisfies the
exact factorization, continuity, and uniqueness property proved in Lemma 2.2.

`K0(ACT-Q-p)` is not the time-orbit quotient named `ACT-Q-p`; it is the
one-point quotient of that already formed nontrivial indiscrete object.

### P10-2 — continuous scalar observables: PROVED

For each actual object `X`,

```text
C(X)=C_b(X)=C 1_X isometrically,
```

all algebraic point evaluations coincide, and the algebra does not separate
the distinct points of `X`. Equality is established before the supremum norm
is used.

### P10-3 — Borel and measurable observables: PROVED

For each actual object `X`,

```text
B(X)={emptyset,X}.
```

Every measurable map from this exact measurable source to a countably
separated target, hence to a standard Borel target, is constant. The
nontrivial source itself is neither countably separated nor standard Borel.
Non-separated targets remain the licensed negative control and admit
nonconstant maps.

The trivial-Borel computation and constant-`T0`-map fact are already recorded
by Paper 9; Paper 10's new proof-owned content is their placement inside the
exact UMP/function/measure/operator package, not a priority claim for those
two consequences.

### P10-4 — positive finite measures: PROVED

For every actual object, total mass gives

```text
Mfin+(X) = {mu_m:m in [0,infinity)},
mu_m(emptyset)=0,  mu_m(X)=m.
```

All Dirac measures coincide with `mu_1`. Proper point singletons are not in
`B(X)`. This theorem has no regularity adjective.

### P10-5a — the transported actual `Q_p` topological group: PROVED

Use exactly the frozen set bijection

```text
phi_p:ACT-Q-p -> U_p/H_p
```

and transport the quotient-group law:

```text
x *_p y = phi_p^{-1}(phi_p(x)phi_p(y)),
e_p       = phi_p^{-1}(H_p),
x^{-1,*}  = phi_p^{-1}(phi_p(x)^{-1}).
```

The group axioms, including commutativity, follow by transport through this
bijection. The product of two indiscrete spaces is indiscrete, and every map
into an indiscrete space is continuous. Hence

```text
*_p:ACT-Q-p x ACT-Q-p -> ACT-Q-p
```

and the transported inverse are continuous for the actual topology. Thus the
specified transported law makes the actual object a non-Hausdorff topological
group under conventions that do not build Hausdorffness into that term.

This is a Paper-10 derived group structure tied to the chosen `phi_p`; it is
not asserted to be source-canonical, it does not make `phi_p` a homeomorphism,
and it imports no natural/profinite quotient topology from `U_p/H_p`.

### P10-5b — continuous characters and operator fields: PROVED

The ordinary unit circle `T` is Hausdorff. A continuous group homomorphism

```text
chi:(ACT-Q-p,*_p)->T
```

is constant by Lemma 2.1, and the homomorphism identity forces that constant
to be `1`. Therefore

```text
Hom_cont((ACT-Q-p,*_p),T)={1}.
```

This does not classify abstract algebraic characters or characters after a
different topology is placed on the same set.

For each of the three actual objects separately, every continuous map into
`B(ell^2(N))` with norm, SOT, or WOT is constant by Lemma 2.6. No additional
operator-theoretic structure is inferred.

## 4. P10-6: standard-circle comparison direction

Fix `p` and `a`, choose the registered basepoint, and use the noncanonical set
bijection

```text
beta_{p,a}:|ACT-ORBIT-p-a| -> |STD-CIRCLE-p|.
```

Both sets are nontrivial. The domain of `beta_{p,a}` has its actual
indiscrete topology, while its codomain has the ordinary Hausdorff circle
topology. Since the bijection is nonconstant, Lemma 2.1 gives

```text
beta_{p,a} is not continuous.
```

The reverse map has an indiscrete codomain, so

```text
beta_{p,a}^{-1}:STD-CIRCLE-p -> ACT-ORBIT-p-a
```

is continuous. Under the set identification, the standard-circle topology is
therefore strictly finer than the actual topology.

No nonconstant continuous map from the actual orbit onto a nontrivial `T0`
space exists. Thus the standard circle is neither a continuous factor nor a
`T0`, Hausdorff, or completely-regular-Hausdorff reflection of the actual
orbit. The actual reflection is the singleton of P10-1. The proxy retains
only modeling-choice topology and the chosen set/action parametrization.

## 5. P10-7 and P10-8: tagged copied components

The next results concern a declared model, not the global Deninger
suspension. First prove the abstract countable-label theorem.

### Theorem 5.1 — coproduct topology and `K0`

Let `I` be a nonempty countable label set and let every `X_i` be a nonempty
indiscrete space. Put

```text
X_I = coproduct_{i in I} ({i} x X_i)
```

with the tagged coproduct topology, and write

```text
X_S = coproduct_{i in S} ({i} x X_i)   for S subset I.
```

By definition a set is open in the coproduct exactly when its intersection
with every component is open in that component. Those intersections are only
empty or the whole component, so

```text
tau(X_I)={X_S:S subset I}.
```

Two points are topologically indistinguishable exactly when they have the
same label. Points in one component see the same component-union opens;
points with different labels are separated by a clopen component. Hence the
label projection

```text
q_I:X_I->I,        (i,x)|->i
```

is the `K0` unit. Its quotient topology is discrete because
`q_I^{-1}(S)=X_S` is open for every `S subset I`.

If `Y` is `T0` and `f:X_I->Y` is continuous, each restriction to `X_i` is
constant. Therefore `f` factors uniquely as `f=f_bar o q_I`. Conversely
every `f_bar:I_discrete->Y` is continuous. Thus

```text
Cont(X_I,Y) <-> Map(I,Y)
```

naturally for `T0` targets: all within-component coordinates are erased and
the label is retained exactly.

### Theorem 5.2 — Borel algebra and positive finite measures

The topology in Theorem 5.1 is closed under complement and countable union,
so it is already a sigma-algebra:

```text
B(X_I)={X_S:S subset I}.
```

For `mu in Mfin+(X_I)`, set `m_i=mu(X_{ {i} })`. Countable additivity over
the disjoint components gives, for every `S subset I`,

```text
mu(X_S)=sum_{i in S} m_i,
sum_{i in I}m_i=mu(X_I)<infinity.
```

Thus `(m_i)` lies in `ell^1_+(I)`. Conversely, for every nonnegative summable
family `(m_i)`, the same formula defines a positive countably additive finite
measure. These constructions are inverse, including zero components:

```text
Mfin+(X_I) <-> ell^1_+(I).
```

Point Dirac measures inside one component coincide; Dirac measures in two
different components are distinguished by their clopen components. Hence
the measure interface retains exactly label-level, not within-component,
point information.

The whole cone is admissible with the same topology. In particular the
topology supplies no distinguished nonzero finite measure or probability.
The zero measure is the universally canonical zero element. More invariantly,
on the bare countably infinite discrete quotient, a finite measure invariant
under every permutation must give equal mass to every point and is therefore
zero; any nonzero choice requires extra, non-topological data.

### P10-7 — copied-prime reflection: PROVED ON MODELING CHOICE

Apply Theorem 5.1 with `I=P`, the countable set of rational primes, and
`X_p=ACT-PACKET-p`. Then

```text
K0(COPROD-PACKETS)=P_discrete.
```

Every continuous map from the copied coproduct to a `T0` target is exactly an
arbitrary prime-indexed family of target points, constant inside each copied
packet. Distinct prime components remain distinguishable; no orbit or packet
coordinate survives within one component.

This is not a theorem about the topology inherited by any global rational-
Witt or Deninger suspension.

### P10-8 — copied-prime mass and scalar ledger: PROVED ON MODELING CHOICE

Apply Theorem 5.2 with `I=P`. Every positive finite Borel measure is uniquely
specified by

```text
(m_p) in ell^1_+(P),
mu(coproduct_{p in S} ACT-PACKET-p)=sum_{p in S}m_p.
```

Zeros are allowed, and no nonzero vector is selected by topology. Replacing
`P` by the composite integers, or by any other nonempty countable label set,
gives the identical abstract `K0`, Borel, continuous-map, and `ell^1_+`
classification. The construction therefore contains no intrinsic primality
test or arithmetic weight selection.

On the discrete quotient `P_discrete`, every scalar function is continuous.
The externally attached function

```text
lambda(p)=log p
```

is unbounded because the primes are unbounded, so `lambda` is not in
`C_b(P_discrete)`. It also does not vanish at infinity: for a fixed positive
threshold, infinitely many primes satisfy `log p` above that threshold.
Hence it is not in the ordinary discrete `C_0(P_discrete)` either.

The arithmetic label permits this external scalar, but neither the discrete
topology nor the measure cone selects it. It is not a return time, primitive-
orbit weight, multiplicity, stability, phase, trace, or `A1` datum of the
separated/copied owner. The existing `Theta_+` record is not reissued.

## 6. Registered falsifiers and negative controls

| Hypothesis | Audit result | Exact falsifier test |
|---|---|---|
| H1 complete separated collapse | **CONFIRMED** | A nonconstant continuous map from an actual owner to a named `T0` target would falsify it; Lemma 2.1 rules one out. |
| H2 observable and measure collapse | **CONFIRMED on the frozen domains** | A nontrivial actual open/Borel set, a licensed nonconstant separated map, or equal-total unequal positive finite measures would falsify it; Sections 2--3 exclude all three. |
| H3 proxy is not a separated reflection | **CONFIRMED** | A nonconstant actual-to-circle continuous factor would falsify it; `beta_{p,a}` is not continuous, while its inverse is. |
| H4 copied components retain only labels | **CONFIRMED on the explicit coproduct** | A surviving within-component point, merged distinct labels, or a topology-selected nonzero mass would falsify it; Theorems 5.1--5.2 give the opposite classification. |

The assumptions are not cosmetic: indiscrete topological and measurable
targets admit nonconstant maps; algebraic characters are outside the
continuous-character conclusion; alternative topologies on `U_p/H_p` may
have different characters; and arbitrary `ell^1_+` masses give the same
coproduct topology.

## 7. P10-9 control contract: typed, not executed here

This proof-only task creates no code or result files. A later deterministic
control phase must test, without being treated as proof, at least these exact
oracles:

1. for indiscrete sets of sizes `1,2,3,5`, `K0` has one class; for size
   `n>0`, maps to a two-point discrete or Sierpinski `T0` target are continuous
   exactly when constant, while all `2^n` maps to a two-point indiscrete
   target are continuous;
2. the topology-generated Borel algebra has two sets; measurable maps to a
   finite discrete target are constant; all point Dirac ledgers agree;
3. for finite indiscrete topological groups, continuous characters into
   finite cyclic/Hausdorff circle targets are trivial;
4. on one finite carrier with a nontrivial discrete proxy, the map from the
   finer discrete topology to the coarser indiscrete topology is continuous,
   and the reverse identity is not;
5. coproducts of `2,3,5,8` nonempty indiscrete components have respectively
   `2,3,5,8` `K0` classes and `2^k` component-union opens;
6. arbitrary nonnegative finite component vectors, including zeros, produce
   distinct measure ledgers without changing the topology;
7. prime, composite, and arbitrary labels give the same abstract answers; and
8. implementation hashes plus two fresh generations satisfy the registered
   byte-reproducibility gate.

Accordingly `P10-9` is **SPECIFIED / NOT YET EXECUTED**, not `PASS`.

## 8. T0--T7 same-object certificate

| Gate | Actual fixed-prime owners | Standard-circle proxy | Copied-prime owner |
|---|---|---|---|
| `T0` identity | **PASS:** exact Paper-9 `ACT-PACKET-p`, `ACT-ORBIT-p-a`, `ACT-Q-p`; reflections are derived interfaces | **PASS only as proxy:** `STD-CIRCLE-p` is separately declared | **PASS only as model:** exact tagged coproduct and discrete label quotient |
| `T1` topology | **PASS:** inherited nontrivial indiscrete topology; no `U_p/H_p` topology imported | ordinary Hausdorff circle by modeling choice | component-union coproduct topology; `K0=P_discrete` |
| `T2` map | `q_0`, Hausdorff/CRH units, transported group operations, and all factorization maps typed; `beta` direction split | `beta^{-1}` is continuous toward actual; `beta` is not | label projection `q_P` is the exact quotient/UMP unit |
| `T3` sigma-algebra | **PASS:** exact topology-generated `{emptyset,X}` | no measure credit transported | **PASS:** all and only component unions |
| `T4` measure | **PASS:** `[0,infinity)` total-mass cone, no regularity; all Diracs coincide | no actual-source measure transported | **PASS:** `ell^1_+(P)`, including zeros; no selected nonzero weight |
| `T5` observable/operator | scalar algebra is constant; norm/SOT/WOT maps constant; actual continuous `Q_p` character trivial | no actual observable/operator credit | continuous separated observables factor through labels; `log p` is external and unbounded |
| `T6` global aggregation | fixed-prime theorem only; no global conclusion | none | **PASS as modeling choice / FAIL as source-global claim** |
| `T7` arithmetic promotion | Paper-9 prime provenance and set/action clock survive only at `A0`/topology level; separated interfaces erase nontrivial coordinates | copied label/clock only; no source-topology promotion | prime tag permits external arithmetic decoration but no primitive-orbit, trace, or determinant promotion |

Every failed or inapplicable downstream gate leaves the Paper-9 topology
theorem unchanged.

## 9. P10-10 Route ceiling

This is a proof-audit ceiling, not a formal Route audit and not a Route YAML.

- The exact actual packet/orbit/`Q_p` topology owners retain arithmetic origin
  and at most topology-level `A1_WEAK`; their standard LCH-Hausdorff route was
  already refuted by Paper 9.
- The singleton separated reflections, constant scalar/operator interfaces,
  trivial measurable interface, total-mass-only measure cone, and trivial
  continuous-character owner are `A1_FAIL` for any nontrivial return/trace
  mechanism: the required internal coordinates have been erased.
- The standard circle is a retopologized proxy. This audit grants it no new
  actual-source `A1` credit and imports none of Paper 8's proxy calculations.
- The copied-prime quotient is a declared aggregation model. Its surviving
  discrete label and external `log p` scalar receive no source-global topology,
  clock, measure, or trace credit.
- No owner here defines an exact determinant, analytic continuation,
  functional equation, completed divisor, self-adjoint quantization, or
  Hilbert--Polya realization. Thus all remain `A2_FAIL`, `A3_FAIL`, and
  `A4_FAIL` under the existing Route rubric.
- Route B remains Boolean `false`; no target data, fit, zero table, or Route-B
  object entered the proof.

## 10. Integrated target adjudication

| Target | Verdict | Exact result |
|---|---|---|
| P10-1 | **PROVED / SINGLETON** | Direct `K0`, Hausdorff, and completely-regular-Hausdorff units and UMPs for every actual owner |
| P10-2 | **PROVED** | `C(X)=C_b(X)=C1_X` isometrically after equality; evaluations coincide; no point separation |
| P10-3 | **PROVED** | Actual Borel algebra is trivial; separated measurable targets force constant maps; source is not countably separated or standard Borel |
| P10-4 | **PROVED** | `Mfin+(X)<->[0,infinity)` by total mass; all Dirac measures agree; no singleton/Radon promotion |
| P10-5 | **PROVED ON EXACT TRANSPORTED OWNER** | `*_p` and inverse are continuous; continuous circle character is trivial; fixed norm/SOT/WOT fields are constant |
| P10-6 | **PROVED WITH DIRECTION** | `beta_{p,a}` is not continuous; `beta_{p,a}^{-1}` is continuous; standard circle is only a finer proxy |
| P10-7 | **PROVED ON MODELING CHOICE** | Coproduct `K0` is the discrete prime set; all `T0` maps factor exactly through the label |
| P10-8 | **PROVED ON MODELING CHOICE** | Borel sets are component unions; finite positive measures are `ell^1_+(P)`; arbitrary labels behave identically; `log p` is external/unbounded |
| P10-9 | **SPECIFIED / NOT EXECUTED** | Exact finite regression oracles are frozen; controls remain witnesses, not proofs |
| P10-10 | **CEILING ADJUDICATED** | Same-object gates and Route ceilings fixed; formal Route audit remains separate; Route B false |

The primary candidate verdict is therefore **CONFIRM_COLLAPSE**, with the
surviving prime label confined to the separately declared copied coproduct.
There is no owner-level `SPLIT` among the licensed actual separated,
measurable, measure, character, scalar, or operator targets.

## 11. Novelty and integrity boundary

The general lemmas in Section 2 are standard topology and measure theory.
Paper 9 owns actual indiscreteness plus its immediate trivial-Borel and
constant-`T0` consequences. The Phase-2 result supports only this wording:

> No direct precedent for the exact rational-Witt packet package was found
> within the bounded Phase-2 search as of 2026-08-14.

The proof-owned Paper-10 result is the exact typed assembly on the hash-locked
rational-Witt owners: direct separated UMPs, scalar/evaluation and positive-
finite-measure classifications, the transported-law continuity and character
boundary, three fixed operator targets, the two circle-map directions, and
the tagged-coproduct/global boundary. It is not new generic topology and is
not an absolute priority claim.

AI-assisted proof disclosure: this audit used AI-assisted symbolic proof
construction, exact-byte binding, and adversarial owner/domain checking. It
used no target zero data, parameter fitting, random search, external-model
upload, source modification, lock edit, manuscript edit, Route file, or code
artifact.
