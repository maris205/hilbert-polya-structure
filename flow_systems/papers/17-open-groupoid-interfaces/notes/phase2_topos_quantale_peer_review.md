# Paper 17 Phase-2 independent topos--quantale proof review

Review date: **2026-08-16 (Asia/Shanghai)**  
Review role: **independent ARS mathematical / methodology / domain / devil proof reviewer**  
Review mode: **read-only exact-byte re-derivation**  
Verdict: **PASS — C0 / M0 / m0**  
Proof disposition: **the Phase-2 symbolic ledger survives independent review**  
Publication ceiling: **TECHNICAL_NOTE_CANDIDATE**  
Standalone disposition: **FALSE / not adjudicated by this review**

Controls, Route A/B, manuscript work, release, Git, and public synchronization
remain **false / unauthorized**.  This report is the only file written by the
review.

## 1. Independence, method, and exact-byte receipts

I read the complete bound tuple and the complete proof ledger, then re-derived
the registered results from the definitions.  The proof author's conversation
was neither available nor consulted.  The earlier source, methodology, and
mathematical reviews were treated as claims to test, not as proof authority.
The ARS theoretical-methodology, domain, and devil lenses used here were:
owner/type validity, premise-to-conclusion validity, convention and
handedness checks, explicit counterexample search, primary-source domain
checking, reproducibility of the symbolic constructions, and P9--P11 novelty
subtraction.  Empirical sampling and statistical criteria are inapplicable.

The following inputs were re-hashed before reading and again after complete
reading:

| Bound artifact | SHA-256 | Receipt |
|---|---|---|
| `notes/research_protocol.md` | `5ca581cff6f2fe088744a522646466ef2f5ce124ad3cdf50367cc5ed33347cea` | exact match |
| `notes/candidate_lock.md` | `2db53e92961cdfa7e43e4e06b7cdd81a2d87d97d15957d793b720bd86c71a604` | exact match |
| `notes/phase1_amendment_v1.md` | `3ada0e70a0d3f53bd68e1a44e63c24870215987176d538c513400dc99ef95f3d` | exact match |
| `notes/phase1_amendment_v2.md` | `2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957` | exact match |
| `notes/phase1_framework_source_precheck.md` | `9991dc5e27ea8577d4236d38feeb63bfc110e3a3b242b3c17be8607da01f9e64` | exact match |
| `notes/phase1_methodology_devils_review.md` | `811e51fc96baedf81a3e4185fa49519ff6c15bad37d866d8186054a24c25653e` | exact match |
| `notes/phase1_independent_math_review.md` | `bdf89476d49ab8a5b3bb7deff9f8738079bd185fd38a00bc1c9ba175677ad6d4` | exact match |
| `notes/phase1_final_gate.md` | `025ee0404484bfa906094adc940528fc6c2c564c39783e1f1658ed9666f645df` | exact match |
| `notes/phase2_topos_quantale_proofs.md` | `f6c7475b854b3d00b37d3e7f2edca8e8f2f15d92d67ae8bbcdcd71be127b3bb1` | exact match |

The candidate hash is also the exact value in the active pipeline tuple at
`notes/pipeline_state.md:20-31`.  The same tuple keeps Controls/Route/manuscript/
release blocked and Route B/Git/public synchronization false at
`notes/pipeline_state.md:16-18`.  The historical batch-lock file itself hashes
to `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8`,
and the batch amendment hashes to
`afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802`.
Thus the proof file is the authorized target and no downstream gate is opened
by this review.

The upstream owner receipts asserted by the proof were independently re-hashed:

| Owner artifact | SHA-256 | Receipt |
|---|---|---|
| Paper-9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | exact match |
| Paper-9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | exact match |
| Paper-10 manuscript | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | exact match |
| Paper-10 proof audit | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | exact match |
| Paper-11 manuscript | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | exact match |
| Paper-11 proof audit | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | exact match |

## 2. Framework-domain cross-check

The selected source convention is correctly typed.  Forssell, Section 2.1,
physical pp. 2--3, defines an open topological groupoid by open domain and
codomain maps, defines equivariant sheaves as local homeomorphisms with a
continuous groupoid action, and states that their category is a Grothendieck
topos.  No Hausdorff hypothesis appears in that definition
([arXiv:1111.2952v2](https://arxiv.org/pdf/1111.2952)).

The Protin--Resende boundary was checked against the primary source rather
than inherited from the prior reviews.  Theorem 2.41 and Theorem 2.45 give the
open-localic-groupoid / multiplicative-open-quantal-frame correspondence at
printed pp. 214--215.  Printed pp. 245--246 state that the canonical
composable-pair frame quotient need not be an isomorphism in general and that
local compactness of the arrow space is sufficient; Definition 5.26 requires
openness and local compactness of the arrow space, not an additional
Hausdorff or second-countability axiom
([DOI 10.4171/JNCG/90](https://doi.org/10.4171/JNCG/90)).
The proof uses exactly this localic result and does not invoke the etale-only
inverse-quantal-frame/sheaf bridge.

## 3. Independent re-derivation matrix

### 3.1 Open and non-etale type

Every nonempty product-basic open in `X_ind x H` has the form `X x U`, and
nonemptiness of `X` makes `U` unique.  The composable-pair parametrization

```text
(x,h,k) |-> ((x,h),(x.h,k))
```

is a homeomorphism because its inverse reads off `x,h,k`, while the forward
map uses only the continuous action.  For nonempty `U`, range maps `X x U`
onto `X`, and source does too because any fixed right translation of `X` is
bijective.  In the real-time case, every arrow neighbourhood contains two
arrows `(x,u)` and `(x.(u-v),v)` with the same source and distinct time
coordinates.  Hence source is nowhere locally injective; `X x {0}` is also
not open.  The open/non-etale split is correct.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (3.1), lines 97-120`; `text: phase2_topos_quantale_proofs.md "G(X,H) is an open topological groupoid." and "For H=R with addition and its usual topology, G(X,R) is not etale.", lines 122-155`.

### 3.2 Whole-`X` sheets and the generic topos

For a local homeomorphism `p:E->X_ind`, every point has an open chart onto
the only nonempty base open, namely all of `X`.  Each chart is therefore the
image of a global section.  Two global sections that meet have a nonempty
open equalizer and hence agree everywhere; their images are equal or
disjoint and partition `E`.  Evaluation consequently yields the explicit
homeomorphism

```text
X x Gamma(X,E) -> E.
```

For an equivariant sheet object `X x S`, continuity of the sheet-label map
`X x H x S -> S_discrete` makes the label independent of `x`.  Unit and
composition leave exactly a continuous action of `H` on the discrete sheet
set.  Morphisms over `X` are exactly `id_X x f`, and groupoid equivariance is
ordinary `H`-equivariance.  The constructed functors satisfy `FE=id` and
`EF~=id`; therefore the proof establishes the category/topos equivalence,
not merely an object-level correspondence:

```text
B(G(X,H)) ~= B_cont(H).
```

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (4.1)-(4.2), lines 159-186`; `equation: phase2_topos_quantale_proofs.md (4.3)-(4.6), lines 188-244`.

### 3.3 Left-action handedness

With the frozen range-first convention, `(x,h)` goes from `x.h` to `x`.
Starting in the fibre over `x.hk`, one first applies `(x.h,k)` and then
`(x,h)`.  Thus the sheet labels obey

```text
h.(k.a)=(hk).a,
```

which is a left `H`-action, not an unrecorded opposite action.  Conversely,
`(x,h).(x.h,a)=(x,h.a)` has the correct source and range.  The proof's
handedness is therefore internally consistent and agrees with Forssell's
left action of an arrow from its domain fibre to its codomain fibre.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (2.1)-(2.2), lines 57-80`; `equation: phase2_topos_quantale_proofs.md (4.4)-(4.6), lines 202-241`.

### 3.4 Connected `R` and disconnected `Z`

For a continuous action of connected `R` on a discrete `S`, every orbit map
has connected image and is constant; the identity forces that constant to be
the starting point.  Hence `B_cont(R)=Set`.  For discrete `Z`, every abstract
action is continuous and the regular translation action is nontrivial.  Its
transitive regular object is connected and nonterminal, whereas a nonempty
connected object of `Set` is terminal.  Therefore `BZ` is not `Set`, and
connectedness is used only in the real-time corollary.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (4.7) and the displayed B(G(X,Z)) ~= BZ, lines 246-273`.

### 3.5 Bare quantale, base frame, and real-time nonunit

The frame isomorphism `Phi(U)=X x U` preserves arbitrary joins and finite
meets.  Direct arrow composition and inversion give

```text
Phi(U)Phi(V)=Phi(UV),        Phi(U)^*=Phi(U^(-1)).
```

Thus the bare involutive quantale is `O(H)`, independently of the carrier and
action.  Right-sidedness is `UH subseteq U`; a nonempty `U` contains `u`, so
`uH=H` and the condition forces `U=H`.  The right-sided/base frame is exactly
`2`.  For `H=R`, a hypothetical open multiplicative unit `E` would satisfy
`E+U=U` for every bounded interval, forcing every `e in E` to be zero, while
`{0}` is not open.  The nonunital conclusion is correct and remains confined
to nondiscrete real time.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (5.1)-(5.3), the Proposition 5.2 base display, and Proposition 5.3, lines 277-340`.

### 3.6 The `q_H` local-compactness gate

Because the unit frame is `2`, the localic composable-pair frame is
`O(H) tensor O(H)`, while the point-set composable-pair frame is
`O(H x H)`.  The rectangle bimorphism is exactly

```text
q_H:O(H) tensor O(H) -> O(H x H).
```

This comparison is not inferred from the bare quantale computation.  If `H`
is locally compact in the registered convention, then `X_ind x H` is locally
compact: a compact neighbourhood `C` in `H` lifts to `X x C`, and every open
cover of the latter is precisely an open cover of `C` under the frame
identification.  The checked Protin--Resende locator then makes `q_H` an
isomorphism.  Only after that step does multiplication live on the correct
localic pullback, permitting Theorems 2.41 and 2.45 to reconstruct the
one-object open localic group.  Outside this domain the proof claims only the
direct topos and bare-quantale calculations.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (6.1), lines 344-362`; `text: phase2_topos_quantale_proofs.md "If H is locally compact in the registered Protin--Resende convention, then q_H is an isomorphism", lines 364-386`; `text: phase2_topos_quantale_proofs.md "They are not lost through failure of the Protin--Resende reconstruction theorem", lines 388-403`.

### 3.7 Standard circle: `BZ` and `O(S_L)`

At `[0]`, isotropy is `LZ`.  For a left `LZ`-set `A`, the relation

```text
(r+nL,a) ~ (r,(-nL).a)
```

is the correct associated-bundle sign for the range-first convention.  In
particular `[0,a]=[nL,(nL).a]`; applying the isotropy arrow `(o,nL)` returns
`[0,(nL).a]`, so restriction recovers the stipulated left action.  Local
sections of `R->S_L` establish the etale bundle, and orbit transport gives
the quasi-inverse.  Hence `B(G_L)~=B(LZ)~=BZ`, not `Set`.

For the quantale, right multiplication saturates the entire time fibre while
preserving range, so the right-sided opens are exactly `A x R` with
`A in O(S_L)`.  The base frame is `O(S_L)`, not `2`; local compactness of
`S_L x R` licenses the same localic comparison.  This proves the requested
standard asymmetry.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (7.1)-(7.2), lines 417-450`; `equation: phase2_topos_quantale_proofs.md (7.3), lines 455-475`; `table: phase2_topos_quantale_proofs.md Section 8 comparison table, lines 477-500`.

### 3.8 Unmarked dilation and strict marking

For `c=L'/L`, simultaneous object and time dilation sends `LZ` onto `L'Z`,
intertwines source, range, product, inverse, and units, and has inverse scale
`c^(-1)`.  Thus unmarked groupoids, topoi, and quantales do not determine the
positive numerical period.  A strict marker fixes the time coordinate; any
marker-preserving isomorphism carries a point's stabilizer-time set `LZ` to
`L'Z` without rescaling.  Equality of those subgroups gives equality of their
positive primitive generators.  The numerical period is therefore retained
only by the separately registered strict marker, not by either plain output.

**Exact proof anchors**: `equation: phase2_topos_quantale_proofs.md (9.1), lines 510-533`; `equation: phase2_topos_quantale_proofs.md (9.2), lines 535-556`.

## 4. P9--P11 owner firewall

| Owner | Independent source check | Paper-17 use | Verdict |
|---|---|---|---|
| Paper 9 | `papers/9-packet-separation/paper/manuscript.tex:409-426` proves actual packet/orbit indiscreteness and records the set stabilizer / primitive logarithmic period. | Section 10 substitutes those facts only after the generic theorems. | PASS |
| Paper 10 | `papers/10-separated-reflection/paper/manuscript.tex:94-120` confines its results to separated, observable, Borel, measurable, and positive-finite-measure interfaces and distinguishes the standard proxy. | Section 10 expressly refuses to relabel those collapses as a topos theorem. | PASS |
| Paper 11 | `papers/11-indiscrete-convolution/paper/manuscript.tex:255-277,337-405` owns the range-first formulas, arrow topology, and composable-pair chart; `:313-324` types the standard proxy; `:1079-1087` forbids owner splicing. | Paper 17 inherits these as lemmas and claims only the new equivariant-sheaf, open-quantal/base/localic, standard-asymmetry, and marked/unmarked calculations. | PASS |

The fixed-prime conclusions at `phase2_topos_quantale_proofs.md:558-591`
stay inside this firewall.  In particular, no standard topology, C*-algebra,
measure, Haar system, trace, determinant, or Route-B object is manufactured.
The proof's same-carrier action-blindness statement at lines 502--506 is a
formal consequence of the generic theorems and is not represented as an
executed control suite.

## 5. Devil's-advocate stress test

### Strongest counter-argument

The strongest attack is that the ledger could obtain its desired collapse by
silently replacing three different owners: first treating `Sh(X_ind)=Set` as
if it erased equivariance, then treating the point-set composable-pair space
as a localic pullback for arbitrary `H`, and finally importing the standard
circle or strict time marker when interpreting the fixed-prime period.  That
splice would make `B(G)=Set`, localic reconstruction, and numerical-scale
claims look mutually compatible while none followed on one registered
owner.  A second version of the attack is convention-sensitive: reversing
the groupoid-action handedness would turn the standard associated bundle into
an opposite-action construction and break the claimed explicit equivalence.

The attack fails against the submitted ledger.  Equivariance is classified
before connectedness is used; the generic output is `B_cont(H)`, with `Z` as
an explicit falsifier.  The bare `O(H)` computation is separated from the
`q_H` gate, and localic reconstruction is asserted only after the locally
compact comparison.  The standard circle is computed as `BZ/O(S_L)`, not
collapsed to the actual `Set/2`, and the associated-bundle sign recovers the
declared left action.  Simultaneous dilation is used only for the unmarked
record, while a strict marker is explicitly extra structure.  Finally,
Section 10 performs the P9--P11 substitution and subtraction only after all
generic and standard theorems are complete.

### Adversarial attack matrix

| Attack | Independent resolution | Exact anchor | Result |
|---|---|---|---|
| Hidden nonconstant etale objects survive on `X_ind`. | Rejected by the global-section partition and evaluation homeomorphism. | `equation: proof (4.1)-(4.2), lines 159-186` | PASS |
| The action on `X` survives in sheet labels. | Rejected because every discrete-label fibre is `X x U`; only the continuous `H`-action on sheets remains. | `equation: proof (4.4)-(4.6), lines 202-244` | PASS |
| The real collapse leaks to disconnected time. | Rejected by the regular discrete `Z`-set. | `equation: proof (4.7) and displayed B(G(X,Z)) ~= BZ, lines 246-273` | PASS |
| Open implies etale or a unital inverse quantal frame. | Rejected by source non-local-injectivity and the no-open-unit argument. | `text: proof "G(X,R) is not etale." and "The quantale O(G(X,R))~=O(R) is nonunital.", lines 138-155 and 327-340` | PASS |
| Bare `O(H)` automatically licenses localic reconstruction. | Rejected; `q_H` is separately derived and installed only on the locally compact domain. | `equation: proof (6.1), lines 344-386` | PASS |
| The quantale theorem itself forgets the nonsober point set. | Rejected; the loss is assigned to `Top -> Loc`, while Theorem 2.45 reconstructs its localic input. | `text: proof "They are not lost through failure of the Protin--Resende reconstruction theorem", lines 388-403` | PASS |
| Standard and actual periodic owners have the same outputs. | Rejected by `Set/2` versus `BZ/O(S_L)`. | `table: proof Section 8, lines 477-500` | PASS |
| Plain outputs recover numerical `L`. | Rejected by unmarked dilation; strict recovery uses an extra marker. | `equation: proof (9.1)-(9.2), lines 508-556` | PASS |
| P9--P11 are repackaged as new Paper-17 results. | Rejected by the exact provenance table and delayed substitution. | `table: proof lines 579-587` | PASS |

## 6. Evidence-backed strengths

### S1: Convention closure is explicit rather than implicit

The proof fixes range-first arrows, fibre direction, residual left action,
and the associated-bundle sign, eliminating the main opposite-group failure
mode.

**Evidence Anchor**: `equation: phase2_topos_quantale_proofs.md (2.1)-(2.2), (4.4)-(4.6), and (7.2)`

### S2: The direct quantale and localic claims are cleanly separated

The ledger proves `O(G)~=O(H)` directly, names the precise `q_H` comparison,
and invokes reconstruction only after its domain condition is met.

**Evidence Anchor**: `equation: phase2_topos_quantale_proofs.md (5.1)-(5.3) and (6.1)`

### S3: The actual/standard/marked owners remain typed

The proof varies topology on one periodic action set, distinguishes
`Set/2` from `BZ/O(S_L)`, and then treats strict time as extra registered
structure.

**Evidence Anchor**: `table: phase2_topos_quantale_proofs.md Section 8, lines 477-500; equations (9.1)-(9.2)`

## 7. Findings by severity

### Critical findings

None.

### Major findings

None.

### Minor findings

None.

The proof is concise at several standard steps, especially orbit transport in
Theorem 7.1, but the associated bundle, representative check, recovered
isotropy action, and inverse-on-arrows statement are all present.  This does
not rise to a clarity defect, and it does not mask a missing mathematical
step.

## 8. Zero-weakness coverage receipt

**Covers**: Weaknesses

| Dimension examined | What was checked | Basis for no residual weakness |
|---|---|---|
| open/non-etale type | topology, structure maps, openness, source local injectivity, unit image | each claim follows directly from `X x U` opens and right-translation bijectivity |
| etale-object classification | global charts, section equalizers, partition, evaluation map | the construction gives a genuine homeomorphism and covers all local homeomorphisms |
| generic topos | object map, morphisms, continuity, quasi-inverses | both functors and natural inverse are explicit |
| handedness | arrow direction, composition order, associated-bundle relation | all three checks produce the same left action |
| `R/Z` split | connected orbit maps and discrete regular action | connectedness is isolated and the falsifier is valid |
| quantale/base/nonunit | joins, product, involution, right-sided frame, real unit | algebraic formulas are exact and action-independent |
| localic domain | relative tensor, `q_H`, local compactness, source locator | the proof does not infer reconstruction from the bare quantale |
| standard circle | isotropy restriction, associated bundle, base frame | `BZ` and `O(S_L)` are independently derived |
| strict/unmarked scale | groupoid dilation and marker-preserving stabilizers | the two record types are not conflated |
| fixed-prime/P9--P11 firewall | hashes, upstream anchors, substitution order, forbidden promotions | inherited facts and Paper-17 deltas remain separate |
| standalone/publication boundary | ledger status and authorization footer | standalone remains false and no downstream action is opened |

## 9. Final proof gate

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0

INDEPENDENT_MATHEMATICS=PASS
METHODOLOGY=PASS
DOMAIN_AND_SOURCE_BOUNDARY=PASS
DEVIL_AND_COUNTEREXAMPLES=PASS
OPEN_NONETALE_TYPE=PASS
TOPOS_EQUIVALENCE_AND_HANDEDNESS=PASS
CONNECTED_R_DISCONNECTED_Z=PASS
BARE_QUANTALE_AND_BASE=PASS
Q_H_LOCALLY_COMPACT_GATE=PASS
STANDARD_CIRCLE_BZ_O_SL=PASS
UNMARKED_STRICT_SCALE=PASS
P9_P11_OWNER_FIREWALL=PASS
FINAL_EXACT_BYTE_PROOF_REVIEW=PASS_C0_M0_m0

TECHNICAL_NOTE_CANDIDATE=true
STANDALONE_PASS=false
STANDALONE_ADJUDICATED_BY_THIS_REVIEW=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

This verdict closes only the independent symbolic-proof review requested
here.  It does not decide standalone eligibility and does not authorize a
control, Route, manuscript, release, Git, or public action.
