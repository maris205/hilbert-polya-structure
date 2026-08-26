# Papers 14--18 replacement screen v4

Date: **2026-08-16 (Asia/Shanghai)**  
Status: **INTEGRATED SCREEN COMPLETE / NO PRECHECK AUTHORIZED**  
Authority: **P14-18-BATCH-AMENDMENT-v4.0**  
Screen findings: **C0/M3/m0**

## 1. Result in one page

This report screened fourteen distinct research questions across the three
stopped slots:

```text
Slot 14 candidates: 4
Slot 16 candidates: 5
Slot 18 candidates: 5
Total candidates:   14

GO count:            0
HOLD count:          3
NO-GO count:        11
```

At most one candidate is retained in each stopped slot, and each retained
candidate is retained only in the source-wait queue:

| Slot | Unique retained candidate | Slot disposition | Blocking finding |
|---|---|---|---|
| 14 | `S14-R4`, stronger-descent rational-Witt replacement with a nonnormal comparison test | `HOLD_FOR_SOURCE` | `M1`: no source-defined stronger-descent functor, comparison map, or packet-topology realization |
| 16 | `S16-R4`, fp/fppf Verschiebung-lift obstruction | `HOLD_FOR_SOURCE` | `M2`: the sheaf-level lifting question is source-authored, but no source map connects a solution to the arithmetic packet or actual/standard comparison |
| 18 | `S18-R4`, `K(C_{Y/X})`-to-cycle comparison | `HOLD_FOR_SOURCE` | `M3`: the proposed comparison has no locked category/degree/target beyond the source sketch and no same-owner packet representation |

`HOLD_FOR_SOURCE` is not a weak form of authorization.  None of these three
questions may proceed to a protocol, lock, proof, controls, Route record, or
manuscript.  In particular, this screen retains **zero** candidates for an
immediate separate precheck.  A later exact-byte batch amendment would have
to adjudicate this report and close the stated source blocker before any
further work.

The eleven rejections are theorem-level.  They are not requests for better
exposition.  They fail the v4 mandatory rejection rules through one or more
of: P9/P10 reflection retelling, P15/Slot-14 Smith--Ulm repackaging, P16
independent-lift destruction, P17-style formal topos/quantale translation,
arbitrary probability-base or time-tensor blindness, an unsourced chosen
kernel, or an asserted rather than constructed same-owner operator.

## 2. Exact authority, read boundary, and hash binding

The authorized target did not exist when this screen began.  Immediately
before creation, the absence check was repeated and passed.  The active v4
amendment was read completely and rehashed twice at the final bytes:

```text
papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v4.md
sha256:6660dd17ff52ad80509358d6f3cd18119c068374383edb5ad6fc9d8bb7e6d76e
lines:264
bytes:11141
```

The following load-bearing v4 receipts were also read completely at the
bound bytes:

| Receipt | SHA-256 | Screen use |
|---|---|---|
| Slot-14 final rank-two precheck, `papers/14-global-periodic-topology/notes/papers14_18_slot14_c2_ranktwo_precheck.md` | `63dcace23ac620b7cc5d41ac78f4c6adbdafecd77f3cec11d0a6f66401634332` | exact common-quotient, Ulm, and Smith maximum; `MERGE_P15R / STOP_SLOT14` |
| replacement-P15 proof ledger, `papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_proofs.md` | `7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355` | complete `B_p`/`kappa_r(p)` theorem and open universal prime-recovery boundary |
| replacement-P15 peer review, `papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_peer_review.md` | `2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7` | `PASS C0/M0/m0`, standalone/full-paper ceiling |
| replacement-P15 stable control-design gate, `papers/15-wieferich-ulm-packet-bases/notes/phase2_control_design_gate.md` | `0380ae8a924ed8cbbf3de1229e7d53a9f51b3da50d053cc700527ca8267660a3` | stable downstream boundary only; no changing design file was read |
| Paper-16 shared-iota fail-fast, `papers/16-arveson-prime-recovery/notes/phase1_shared_iota_factorization_precheck.md` | `60986c5a13488250b45f078d55adb7e26eda8896b0e40f054f2f21d7b49efdc6` | independent-lift product theorem and frozen-lift reduction |
| Paper-18 measured/operator fail-fast, `papers/18-packet-haar-trace/notes/phase1_measured_operator_coupling_precheck.md` | `b0f073af15ce7c6133cdb70e56ea660ab46135635c74ced678aa029247b7fea7` | arbitrary-probability tensor and scalar-transverse-multiplier theorem |

The changing P15 control-design document was not read or bound.  No P17
implementation, result, reproduction, or changing artifact was read or
bound.  P17 appears below only where the active v4 amendment itself imposes
the mandatory “no source-sensitive owner, no topos/quantale retelling” rule.

The relevant maximum-prior owner reports for Papers 2 and 7--13 were read at
these bytes:

| Prior owner report | SHA-256 | Lines |
|---|---|---:|
| P2 `papers/2-flow-zeta/notes/phase3_trace_no_go_audit.md` | `b4930e919bdaf6cf4a30667e3a2a0013603b8afe5492ced1cc0b3f3077968f18` | 264 |
| P7 `papers/7-packet-groupoid/notes/proof_audit.md` | `febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5` | 964 |
| P8 `papers/8-isotropy-trace/notes/proof_audit.md` | `1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990` | 510 |
| P9 `papers/9-packet-separation/notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | 751 |
| P10 `papers/10-separated-reflection/notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | 591 |
| P11 `papers/11-indiscrete-convolution/notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | 581 |
| P12 `papers/12-marked-time-cohomology/notes/phase3_v4_standalone_review.md` | `639dc289c024588777a05d46ff9e5cd47b6e50ceeb807ef7571776d0301e6895` | 453 |
| P13 `papers/13-circle-twists/notes/phase3_v2_note_disposition_gate.md` | `b60c88a33bb3bb5c4f87448aaaf8f2d4020fa945bc9f204fd81d07ea85d7d03e` | 305 |

## 3. Maximum-prior subtraction ledger

Every candidate below applies this complete ledger, not only the nearest
row.  Candidate-specific effects are repeated in each entry so that no
subtraction is implicit.

| Owner | Maximum result that cannot be renamed as a replacement |
|---|---|
| P2 | The fixed-prime packet has an uncountable equal-period bare-set lower bound, but no ordinary orbitwise Ruelle product; a packet measure/disintegration and same-owner trace map are missing, and an arbitrary base can reproduce the formal scalar ledger. |
| P7 | On the proxy `B_p x S_{log p}`, the decomposable semifinite trace, arbitrary central masses, positive-time scalar ledger, and zero-mode principal trace-log are complete; both branches are probability-base blind, and the zero mode is an arbitrary-clock Euler-product compiler. |
| P8 | The actual one-orbit character trace and its no-normal-extension theorem are local; the packet branch is not testable, the regular trace erases nonzero returns, and the all-prime positive-time object is only a scalar Radon measure, not a global operator or determinant. |
| P9 | The actual fixed-prime packet, each actual orbit, and the intrinsic orbit quotient are nontrivial indiscrete spaces with trivial Borel structure.  The set quotient is `U_p/H_p`, but not with its compact proxy topology, and the full global suspension is not classified. |
| P10 | The `T0`, Hausdorff, and completely-regular-Hausdorff images of each actual fixed-prime owner are singletons; separated observables collapse.  A tagged coproduct retains only its externally declared discrete labels and arbitrary `ell^1` masses. |
| P11 | The author global-QC actual convolution algebra collapses to `C_c(R)` and its transported completions to the time group; the raw Hausdorff-open diagnostic is zero.  The result is action-, period-, label-, and arithmetic-blind, and the proxy map has no completion extension. |
| P12 | On the same carrier, the standardized marked action groupoid has `H^1 = R^Q`, the actual complex has `H^1 = R`, and the comparison image is exactly the constant diagonal, equal to strict-automorphism invariants. |
| P13 | Continuous twists and the maximal/reduced diagonal-corona package are correct but reduce to generic gauge and constant-diagonal `c0`/multiplier/corona facts after component isometries; the binding ceiling is a Technical Note, not a new owner-sensitive obstruction. |
| P15 | The bare compact group `B_p` is completely classified by its Ulm tails `kappa_r(p)`, including the exceptional local branch, torsion closure, global isomorphism criterion, and `B_2 != B_3`.  Marked sequences, measure, flow, trace, and universal recovery of `p` are distinct owners; universal recovery remains open. |
| Slot 14 | The source common quotient `C_{pq}` is correct and complete.  Rank two gives `h_r=min(kappa_r(p),kappa_r(q))`; finite assemblies give ordinary incidence Smith factors.  This is P15 content after maximum subtraction and is stopped/merged. |
| P16 | The complete choice groupoid permits independent lift changes, which realize all of `B_p x B_q`.  A proper common-iota subdirect product exists only after artificial freezing and then reduces to Slot 14/P15; the generic minimal-ideal/Arveson foundation supplies no replacement centre. |
| P18 | The only typed measured operator in the audited owner is `L^infinity(B_p) bar-tensor M_{log p}^{reg}` with `1 bar-tensor lambda`; normalized transverse integration is the scalar one, arbitrary probability spaces substitute unchanged, and no source-induced mixed packet/time operator exists. |

## 4. Primary/official source corpus and bounded-search ceiling

Only primary author records and official mathematical documentation were
admitted.  No new PDF was downloaded or retained.  Existing local primary
bytes were read only where already present.

| Source | Exact admitted role |
|---|---|
| [Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4](https://arxiv.org/abs/1807.06400) | rational-Witt arithmetic suspension, source flow, periodic-orbit and stabilizer ownership; not a source for the later author groupoids, traces, kernels, or replacements |
| [Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1](https://arxiv.org/html/2508.05329v1) | stronger-descent motivation in the introduction; sheaf results; the explicit fp/fppf Verschiebung-lift question in Section 4; `W_rat`/finite-correspondence Theorem 5.1, F/V Proposition 5.2, nonnormal extension question, and `K(C_{Y/X})`/cycle research direction in Section 5 |
| [Kucharczyk--Scholze, *Topological realisations of absolute Galois groups*](https://arxiv.org/abs/1609.04717) | primary comparator for rational-Witt-based functorial compact Hausdorff Galois realizations and Frobenius-type descent; not the Deninger suspension or any proposed stronger-descent replacement |
| [Stacks Project, fppf/etale comparison, Tag 0DDK](https://stacks.math.columbia.edu/tag/0DDK) | official site/sheaf framework only; no rational-Witt Verschiebung lift |
| [Stacks Project, quotient sheaves, Tag 044H](https://stacks.math.columbia.edu/tag/044H) | official quotient-sheaf/coequalizer framework only; no packet quotient or source arithmetic invariant |
| [Stacks Project, normalization and finite-etale criterion, Tag 0BTF](https://stacks.math.columbia.edu/tag/0BTF) | official normalization framework only; no extension of Deninger's Theorem 5.1 to nonnormal schemes |
| [Blumberg--Gepner--Tabuada, *K-theory of endomorphisms via noncommutative motives*](https://arxiv.org/abs/1302.1214) | strong primary prior for `KEnd`, natural transformations, and recovery of rational Witt vectors from noncommutative motives |
| [Campbell--Lind--Malkiewich--Ponto--Zakharevich, *K-theory of endomorphisms, the TR-trace, and zeta functions*](https://arxiv.org/abs/2005.04334) | strong primary prior for endomorphism K-theory, TR traces, characteristic polynomials, and Lefschetz zeta functions |
| [Agarwal--Campbell--Manco--Ponto--Sun, *Frobenius and Verschiebung for K-theory of endomorphisms*](https://arxiv.org/abs/2507.05956) | primary nearby prior for lifting F/V to reduced K-theory of endomorphisms; a different owner from Deninger's sheafified reduced monoid algebra |
| [Connes--Consani--Marcolli, *Noncommutative geometry and motives: the thermodynamics of endomotives*](https://arxiv.org/abs/math/0512138) and [Connes--Consani, *BC-system, absolute cyclotomy and the quantized calculus*](https://arxiv.org/abs/2112.08820) | strong primary prior against rebranding power maps, Witt/KEnd operations, or a semigroup action as a new arithmetic packet operator |

Four bounded arXiv-only query clusters were run on 2026-08-16: rational-Witt
topology/stronger descent/common quotient/cohomology; shared-iota/lift
obstruction/Arveson/Verschiebung; F/V Hecke/Haar tensor/mixed kernel/power-map
operator; and `K(C_{Y/X})`/cycles/KEnd/TR/endomotive comparisons.  Exact-phrase
queries for the Section-4 Verschiebung lift, the stronger-descent replacement,
the nonnormal correspondence extension, and the `C_{Y/X}` comparison returned
Deninger's 2025 paper as the only direct admitted hit.  The K-theory queries
also returned the substantial nearby priors listed above.  Search-engine
silence and indexing are incomplete evidence, so the maximum negative wording
throughout this report is:

```text
NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH
```

It is never upgraded to a universal absence or priority claim.

## 5. Firewall semantics

The candidate entries use five separate firewalls:

1. **same owner** asks whether the source domain, codomain, and map remain on
   one functorial object, rather than being spliced from a packet, proxy,
   correspondence, trace, or Hilbert representation owned elsewhere;
2. **arbitrary probability** asks whether replacing `B_p` by an arbitrary
   probability space leaves the claimed invariant unchanged;
3. **independent lift** applies the full P16 choice groupoid rather than a
   frozen common-iota slice;
4. **time tensor** asks whether the operator or trace factors as identity on
   the transverse base tensor a time-only construction; and
5. **forget owner** removes the rational-Witt/Deninger owner and checks
   whether a generic topological, compact-group, Smith, sheaf, cohomological,
   or operator lemma proves the same theorem.

`PASS` means the candidate is not destroyed by that particular falsifier; it
does not imply the other v4 promotion conditions.  `N/A` is a type barrier,
not positive evidence.  `PENDING` is a fail-closed source/proof obligation.

## 6. Slot 14 candidates

### S14-R1 — global-suspension `T0`/sober reflection retaining arithmetic incidence

**Research question.**  Does the full Deninger suspension, rather than one
fixed-prime packet, have a source-canonical `T0` or sober image whose
specialization preorder retains a nontrivial cross-prime incidence relation?

**Owner, domain, codomain, map, law.**  The proposed domain is the actual
global rational-Witt suspension `X_Den` with its source flow.  The codomain is
the generic Kolmogorov quotient `K0(X_Den)` or sobrification
`Sob(K0(X_Den))`; the map is the canonical unit `eta_X`.  These units are
functorial for continuous maps, but no source proves the topology or
specialization order of the full `X_Den`, and no source map from that image
to an arithmetic incidence object is available.

**Primary/official locator or proof obligation.**  [Deninger 2018](https://arxiv.org/abs/1807.06400)
owns the suspension and flow, not this reflection.  The author obligation
would be to derive the full global topology from the source quotient, compute
its specialization preorder without importing fixed-prime coproduct topology,
and prove functorial arithmetic content of `eta_X`.

**Strongest generic retelling/attack.**  Every topological space has a `T0`
quotient, and sobrification is a generic reflection.  P9/P10 already show
that each fixed-prime actual owner is indiscrete and its separated reflection
is a singleton; tagging components merely leaves externally declared labels.
Thus “take the reflection” is exactly the mandatory generic retelling unless
a new full-suspension specialization relation is proved first.

**Maximum subtraction.**  P2 removes the bare-set multiplicity as topology;
P7/P8 remove trace or return information from a reflection; P9/P10 own the
indiscrete and singleton-reflection theorems; P11 removes action-sensitive
information from globally continuous separated observables; P12 owns the
actual/standard cohomology diagonal; P13 removes generic topos/twist/corona
packaging; P15 and Slot 14 remove `kappa`/common-quotient arithmetic; P16
removes frozen shared-lift incidence; P18 removes any probability/time trace
promotion.  What remains is only an unproved full-global topology theorem.

**Firewalls.**  Same owner: `PENDING`, because the full topology is not yet
classified.  Arbitrary probability: `N/A`; no measure is typed.  Independent
lift: `PENDING`; no global choice law is computed.  Time tensor: `FAIL`; the
reflection ignores the flow unless extra source structure is proved.
Forget owner: `FAIL`; the reflector exists for every space.

**Smallest publication-weight theorem signature.**  An explicit source-derived
specialization preorder on the full suspension, a proof that its canonical
reflection is neither a singleton nor a tagged discrete label set, and a
functorial theorem recovering a source arithmetic relation from that order.
Anything weaker is P9/P10 retelling.

**Bounded precedent ceiling.**  The arXiv-only topology query returned
[Deninger 2018](https://arxiv.org/abs/1807.06400),
[Deninger 2025](https://arxiv.org/html/2508.05329v1), and the distinct compact
Hausdorff construction of [Kucharczyk--Scholze](https://arxiv.org/abs/1609.04717),
but no exact full-suspension reflection package.  The search does not compute
the missing topology and cannot defeat the internal P9/P10 subtraction.

**Disposition:** `NO_GO`

### S14-R2 — higher-rank source common quotient and multi-prime Ulm incidence

**Research question.**  For a finite prime set `S` with `|S|>=3`, can the
source common quotient `C_S` and its Ulm invariants yield a new multi-prime
topology or incidence theorem beyond pairwise minima and Smith normal form?

**Owner, domain, codomain, map, law.**  Let `A` denote the exact compact
abelian ambient owner of the Slot-14 receipt and let `K_p` be its source
kernels.  The proposed map is the formal quotient
`q_S:A -> C_S=A/(product_{p in S}K_p)`, equivalently the corresponding
`U_S/H_S` quotient where licensed.  Inclusion of finite prime sets induces
the formal quotient maps `C_S -> C_T` for `T subset S`.  No nonformal
relative functor beyond this quotient lattice has been identified.

**Primary/official locator or proof obligation.**  The exact source and proof
owner is the hash-bound Slot-14 receipt together with the P15 proof ledger.
No extra external locator is needed for the formal quotient.  A replacement
would have to author-prove a relative invariant not determined by the
individual `kappa_r(p)` and ordinary incidence matrices.

**Strongest generic retelling/attack.**  Finite families of subgroups produce
an ordinary quotient lattice.  On each `r`-primary component the available
height is an extremum of already classified tails; finite relation maps are
integer incidence matrices and reduce to Smith normal form.  Raising the rank
does not change that generic algebra.

**Maximum subtraction.**  P2 contributes no relative topology; P7/P8 remove
measure/trace/determinant promotion; P9/P10 remove compact topology imported
through a set quotient; P11 removes action information from generic
convolution; P12/P13 remove formal cohomology/twist or diagonal-corona
repackaging; P15 owns every `kappa_r(p)` and the full `B_p` classification;
Slot 14 owns pairwise minima and incidence Smith factors; P16 proves that the
only proper common-iota form is the artificially frozen version of this same
package; P18 removes tensor-trace coupling.  No independent remainder is
visible.

**Firewalls.**  Same owner: `PASS` for the formal quotient only.  Arbitrary
probability: `N/A`.  Independent lift: `FAIL` if interpreted as a shared-lift
invariant; full lift changes restore the product.  Time tensor: `N/A`.
Forget owner: `FAIL`; quotient lattices, minima, and Smith form are generic.

**Smallest publication-weight theorem signature.**  A functorial relative
tail or extension class that is not reconstructible from all individual
P15 tails, pairwise minima, and the integral incidence matrix, together with
two nonisomorphic source examples having identical maximum-prior data.  No
candidate construction of that signature exists.

**Bounded precedent ceiling.**  Exact arXiv queries combining rational Witt,
common quotient, Ulm, and Smith returned no direct external package.  That
bounded non-hit is immaterial because the exact internal Slot-14/P15 theorem
already supplies the maximum reduction.

**Disposition:** `NO_GO`

### S14-R3 — actual/standard mapping-cone, topos, or quantale cohomology

**Research question.**  Can the same-carrier comparison
`J:G_std -> G_actual` be promoted to a mapping-cone, topos, or quantale
invariant that becomes a new global-periodic-topology centre?

**Owner, domain, codomain, map, law.**  The exact existing map is P12's
unchanged-time groupoid map `J:G_std -> G_actual`; contravariance gives
`J^*:C^*(G_actual;R)->C^*(G_std;R)`.  The proposed owner is the author-derived
cone `Cone(J^*)`, or a geometric morphism/quantale homomorphism constructed
from the same map.  Functoriality is the generic functoriality of cones,
topoi, or quantales; Deninger supplies no such object.

**Primary/official locator or proof obligation.**  The source ceiling is the
hash-bound P12 actual/standard theorem.  [Deninger 2018](https://arxiv.org/abs/1807.06400)
does not define this comparison.  The author would have to prove a new
source-sensitive coefficient system or operation before applying formal
derived/topos machinery.

**Strongest generic retelling/attack.**  Forming a cone from a cochain map is
formal.  P12 already computes the publication-weight degree-one delta:
`R -> R^Q` with constant-diagonal image and strict-symmetry invariants.
Rephrasing the same exact sequence as a topos or quantale statement adds no
new owner-sensitive theorem and triggers the v4 P17-style rejection rule.

**Maximum subtraction.**  P2/P7/P8 remove any inferred measure, trace, or
determinant; P9/P10 own the topology/reflection collapse; P11 owns the
time-factorization consequence; P12 owns the full current cohomological
comparison; P13 owns generic twist and diagonal-corona formalism; P15/Slot14
remove arithmetic tail or Smith labels; P16 removes shared-choice
cohomology destroyed by independent lifts; P18 removes tensor-operator
promotion.  The remaining cone/topos/quantale operation is formal packaging.

**Firewalls.**  Same owner: `PASS` only at the author-derived cochain level,
not as a source object.  Arbitrary probability: `PASS` vacuously because no
measure enters.  Independent lift: `PENDING` for any cross-prime variant.
Time tensor: `PASS` only by type separation.  Forget owner: `FAIL`; the cone
and categorical reformulations work for every marked groupoid map.

**Smallest publication-weight theorem signature.**  A source-defined
coefficient sheaf or operation for which the cone has a computed nonzero
class outside P12's `R^Q/diagonal`, is functorial under the actual source
choice law, and distinguishes a rational-Witt packet from a generic marked
action.  No such coefficient owner or map is available.

**Bounded precedent ceiling.**  The bounded action-groupoid/cohomology query
found no exact rational-Witt cone package.  Search silence cannot convert a
formal mapping-cone or topos translation into a new source theorem.

**Disposition:** `NO_GO`

### S14-R4 — stronger-descent rational-Witt replacement with a nonnormal comparison test

**Research question.**  Can one define a stronger-than-Galois descent functor
that retains more additive structure than `W_rat`, use it to replace the
defective Deninger/Kucharczyk--Scholze spaces, and test the improvement by an
extension of the `W_rat`--finite-correspondence comparison across nonnormal
schemes?

**Owner, domain, codomain, map, law.**  [Deninger 2025, introduction](https://arxiv.org/html/2508.05329v1)
gives, for normal domains in the stated setting, the descent identity
`W_rat(A)=(underline Z overline A)^G` and its natural map to functions on
`X_A`, then explicitly suggests stronger descent replacements.  Section 5
gives the functorial isomorphism
`chi_X:W_rat(O(X))->underline Corr(X,A^1)` for normal Noetherian affine `X`
and asks about nonnormal extension.  The candidate would require a precisely
defined site/descent datum `D_sd`, a functor `W_sd`, natural comparison maps
whose directions cannot yet be asserted, a functorial space `X_A^sd`, and a
nonnormal defect comparison.  None of those new domain/codomain/map data is
currently source-defined.

**Primary/official locator or proof obligation.**  The suggestion and the
nonnormal question are source-authored in
[Deninger 2025, introduction and Section 5](https://arxiv.org/html/2508.05329v1#S5).
[Kucharczyk--Scholze](https://arxiv.org/abs/1609.04717) is the primary
compact-Hausdorff rational-Witt comparator.  The author obligation is not to
guess a topology: it is first to define the descent category, prove a
representability/sheaf theorem, construct every natural comparison, and only
then derive a packet or actual/standard topology.

**Strongest generic retelling/attack.**  “Choose a finer topology and
sheafify,” “normalize and take a conductor,” or “impose a stronger descent
condition” are generic moves.  Unless `W_sd` is characterized by a universal
property and yields an invariant that differs on explicit arithmetic rings
with the same generic normalization data, the proposal is a generic descent
or normalization exercise.  The nonnormal question alone is an algebraic
extension problem, not yet a global-periodic-topology replacement.

**Maximum subtraction.**  P2/P7/P8 remove any automatic measure, trace,
return, or determinant from a new space; P9/P10 require the actual topology
and forbid reflection relabeling; P11 requires any analytic structure to
survive action-blindness; P12/P13 remove formal comparison/cohomology/twist
packaging; P15 and Slot 14 remove all old `B_p` tail/common-quotient content;
P16 requires naturality under independent choices; P18 requires a non-product
same-owner operator before analytic promotion.  Thus only a genuinely new
descent functor plus topology comparison can remain.

**Firewalls.**  Same owner: `PENDING`; the new owner and maps do not yet
exist.  Arbitrary probability: `PASS` at the algebraic stage, but supplies no
measure.  Independent lift: `PENDING`; descent naturality must quantify all
permitted changes.  Time tensor: `PASS` at the algebraic stage, but supplies
no time representation.  Forget owner: `FAIL` unless the proposed defect is
proved to use rational-Witt addition rather than generic normalization.

**Smallest publication-weight theorem signature.**  Define `W_sd` by a
universal descent law; prove functorial sheaf/representability and comparison
theorems; compute it on at least one singular arithmetic family where
`W_rat` and normalization/conductor data do not already determine the answer;
construct the induced source space; and prove a nontrivial actual/standard or
separation invariant that disappears for a generic sheafification.  This is
a multi-lemma program, not a one-line corollary.

**Bounded precedent ceiling.**  Exact stronger-descent and nonnormal queries
returned [Deninger 2025](https://arxiv.org/html/2508.05329v1) as the only
direct admitted formulation, with
[Kucharczyk--Scholze](https://arxiv.org/abs/1609.04717) as strong nearby
topological prior.  No defined `W_sd` package was found within the bounded
search, but the missing definition makes this source silence a blocker, not
novelty evidence.

**Disposition:** `HOLD_FOR_SOURCE`

## 7. Slot 16 candidates

### S16-R1 — shared-iota fibre product as a proper arithmetic subdirect product

**Research question.**  Does fixing a global root-of-unity injection `iota`
force the two fixed-prime coordinates into a proper source-canonical
subdirect product of `B_p x B_q`?

**Owner, domain, codomain, map, law.**  The exact domain is the P16 source
choice groupoid with objects `(iota,x_p,x_q)` and independently permitted
transporters in the two lift coordinates.  The map sends a choice to its
two classes in `B_p x B_q`.  The functorial choice law is the full independent
action, not the frozen diagonal slice.

**Primary/official locator or proof obligation.**  The primary source ceiling
is [Deninger 2018](https://arxiv.org/abs/1807.06400) for the underlying
rational-Witt construction; the complete map and choice-law proof is the
hash-bound P16 fail-fast receipt.  No further author obligation can change
the already computed image without changing the source choice groupoid.

**Strongest generic retelling/attack.**  A fibre product over a shared datum
is a proper subdirect product only if the allowed changes remain correlated.
Here independent translation actions are surjective in each factor, so the
orbit image is the full product.  Freezing both translations manufactures
the desired fibre product and is not source invariance.

**Maximum subtraction.**  P2/P7/P8 remove trace or determinant consequences;
P9/P10 remove topology imported from compact quotient charts; P11 removes
action-sensitive analytic claims; P12/P13 remove diagonal/cohomology/twist
rephrasings; P15/Slot14 own the only frozen common quotient and its full
Smith--Ulm data; P16 itself proves the full-product image under independent
lifts; P18 removes any later tensor-trace rescue.  Nothing remains.

**Firewalls.**  Same owner: `PASS` for the complete choice map.  Arbitrary
probability: `N/A`.  Independent lift: `FAIL` decisively; the image is all of
`B_p x B_q`.  Time tensor: `N/A`.  Forget owner: `FAIL`; a frozen fibre
product is a generic compact-group construction.

**Smallest publication-weight theorem signature.**  A source theorem showing
that the permitted transport group is genuinely smaller than the product,
with a nontrivial invariant constant on every allowed transporter.  The P16
receipt proves the negation for the current owner.

**Bounded precedent ceiling.**  The exact shared-iota arXiv query produced no
direct external package.  This cannot overcome the complete internal
surjectivity proof.

**Disposition:** `NO_GO`

### S16-R2 — cohomological obstruction class for independently varying lifts

**Research question.**  Can a cocycle or torsor class record failure to choose
the two prime lifts compatibly even though the underlying image is the full
product?

**Owner, domain, codomain, map, law.**  The proposed domain is the same P16
choice groupoid.  A candidate cocycle would map its arrows to an abelian
coefficient group `M`, hence define a class in groupoid `H^1` or a connecting
set attached to a chosen extension.  Neither `M` nor an extension is
source-defined.  The required law is invariance under both independent
transporter actions.

**Primary/official locator or proof obligation.**  [Deninger 2018](https://arxiv.org/abs/1807.06400)
does not define this cohomology.  The author would have to construct a
source-natural coefficient object and prove the cocycle descends under the
complete choice groupoid.  A class built only after selecting origins is not
admissible.

**Strongest generic retelling/attack.**  On a product torsor with independent
surjective translations, an origin-dependent compatibility cocycle is a
coboundary or a coordinate artifact.  A shared-iota class that changes under
one permitted lift is not an invariant.  This is the cohomological restatement
of the P16 fail-fast, not a repair.

**Maximum subtraction.**  P2/P7/P8 remove analytic promotion; P9/P10 remove
topological separated information; P11 removes generic action-groupoid
analytic content; P12 already supplies the relevant actual/standard
cohomological comparison and constant-diagonal invariant; P13 removes formal
twist/corona variants; P15/Slot14 own the frozen quotient arithmetic; P16
forces independent changes; P18 removes a later probability/time coupling.
No source-sensitive coefficient system remains.

**Firewalls.**  Same owner: `FAIL` until a coefficient object is sourced.
Arbitrary probability: `N/A`.  Independent lift: `FAIL`; the proposed class
is precisely what the independent action destroys.  Time tensor: `N/A`.
Forget owner: `FAIL`; torsor cocycles and coboundaries are generic.

**Smallest publication-weight theorem signature.**  A source-defined
extension/coefficient system, a nonzero class invariant under the full
independent transporter group, and two arithmetic owners distinguished after
all P15 tails and P12 diagonal data agree.  No candidate meets the first
condition.

**Bounded precedent ceiling.**  The bounded rational-Witt/Galois-cohomology
lift-obstruction query found only the general rational-Witt topological and
sheaf sources, not this exact class.  Missing coefficients and P16's direct
countertheorem control the decision.

**Disposition:** `NO_GO`

### S16-R3 — minimal ideal, boundary representation, or Arveson envelope of the lift action

**Research question.**  Can the independent-lift action be encoded by an
operator system whose Shilov boundary, minimal ideal, or C*-envelope retains
prime-pair arithmetic?

**Owner, domain, codomain, map, law.**  A putative domain would be an operator
system generated from translation functions on `B_p x B_q`; the codomain
would be its C*-envelope or primitive/minimal-ideal lattice, with the canonical
inclusion map.  No such operator system or representation is source-defined.
The only invariant law available is the generic product-translation action.

**Primary/official locator or proof obligation.**  There is no Deninger
operator-system locator.  [Deninger 2018](https://arxiv.org/abs/1807.06400)
owns only the arithmetic space/flow input.  An author would have to construct
a faithful same-owner representation before any boundary theorem; choosing
coordinate functions from compact proxy charts is forbidden.

**Strongest generic retelling/attack.**  Translation algebras on a compact
product and their minimal ideals/boundaries are generic harmonic or operator
algebra.  The P16 receipt already identifies this as the generic
minimal-ideal/Arveson foundation, with no proper shared arithmetic subobject.

**Maximum subtraction.**  P2/P7/P8 remove inherited traces and determinants;
P9/P10 forbid compact-proxy topology transfer; P11 shows generic convolution
erases action/period/arithmetic; P12/P13 remove formal boundary/twist/diagonal
repackaging; P15/Slot14 remove tail/Smith labels; P16 removes the supposed
proper subdirect owner and explicitly owns the generic Arveson foundation;
P18 removes product-tensor operator promotion.  The centre is wholly prior or
generic.

**Firewalls.**  Same owner: `FAIL`; the representation is chosen.  Arbitrary
probability: `FAIL` for any normalized translation representation with the
same support.  Independent lift: `FAIL`; the full product action remains.
Time tensor: `PENDING`, but cannot rescue the missing owner.  Forget owner:
`FAIL`; the construction is a generic operator-system envelope.

**Smallest publication-weight theorem signature.**  A source-induced
operator system and a boundary invariant proved not to occur for a generic
compact product translation action.  No source map supplies the first object.

**Bounded precedent ceiling.**  The exact rational-Witt/Arveson query found no
direct admitted package.  The v4 mandatory P16-Arveson rejection and missing
source representation are independently decisive.

**Disposition:** `NO_GO`

### S16-R4 — fp/fppf Verschiebung-lift obstruction on the sheafified reduced monoid algebra

**Research question.**  For the fp or fppf topology, does the sheafified
Verschiebung `V_N` on `W_rat(O)^#` lift functorially to an additive
endomorphism of `underline Z(O)^#`, and if not, what exact obstruction in the
kernel of `omega` prevents it?

**Owner, domain, codomain, map, law.**  On the fp/fppf site of affine schemes,
the source-defined epimorphism is
`omega:underline Z(O)^# ->> W_rat(O)^#`.  The desired map is an additive
endomorphism `tilde V_N` of `underline Z(O)^#` satisfying
`omega o tilde V_N = V_N o omega`, functorial in schemes and compatible with
the indexed Witt operation.  On topologies finer than the `f`-topology the
source proves an isomorphism and an explicit lift; fp/fppf is the stated open
case.

**Primary/official locator or proof obligation.**  The question is explicit
in [Deninger 2025, Section 4, immediately after Proposition 4.8](https://arxiv.org/html/2508.05329v1#S4).
The [Stacks fppf/etale comparison](https://stacks.math.columbia.edu/tag/0DDK)
supplies site framework only.  The proof obligation is to identify whether
`V_N` preserves the exact sheaf kernel of `omega`, construct the lift or an
explicit counterexample, and prove descent/naturality rather than objectwise
choice.

**Strongest generic retelling/attack.**  Lifting an endomorphism through an
epimorphism is generically equivalent to preserving its kernel, with possible
extension obstructions.  Publication weight therefore cannot come from that
formal lemma; it must compute the rational-Witt kernel in the fp/fppf site,
exhibit an arithmetic obstruction or canonical lift, and control the Witt
relations.  Nearby KEnd F/V lifts are substantial prior but use a different
owner.

**Maximum subtraction.**  P2/P7/P8 remove any automatic packet trace,
operator, or determinant; P9/P10 require an actual topology map before a
topological replacement; P11 removes generic action/convolution promotion;
P12/P13 remove formal cohomology/twist repackaging; P15 and Slot14 remove all
`B_p`/Ulm/common-quotient content; P16 removes shared-lift arithmetic but does
not answer this sheaf question; P18 removes any probability/time tensor
operator.  The sheaf obstruction itself survives, but no bridge to the
stopped arithmetic packet slot survives yet.

**Firewalls.**  Same owner: `PASS` at the sheaf level; all displayed maps are
on the `omega` owner.  Arbitrary probability: `PASS` by type separation.
Independent lift: `PASS` only if the constructed map is genuinely natural,
which is part of the obligation.  Time tensor: `PASS` by type separation.
Forget owner: `PASS` only for a computed `V_N`/kernel obstruction; the generic
lifting lemma alone fails.  The separate v4 packet/actual-standard
load-bearing gate is `FAIL` at present.

**Smallest publication-weight theorem signature.**  For a locked fp or fppf
site and every `N`, give a necessary-and-sufficient kernel criterion; prove a
canonical natural lift satisfying the relevant F/V identities or give a
minimal explicit arithmetic counterexample; distinguish fp from fppf if they
differ; and then supply a source-defined functorial map explaining how the
result changes the Deninger packet or actual/standard comparison.  The first
three clauses are a credible multi-lemma algebraic program; the final bridge
is presently absent.

**Bounded precedent ceiling.**  The exact Verschiebung/reduced-monoid/fppf
query returned [Deninger 2025](https://arxiv.org/html/2508.05329v1#S4) as the
only direct admitted formulation.  [Agarwal et al. 2025](https://arxiv.org/abs/2507.05956)
lifts F/V on reduced K-theory of endomorphisms and is a mandatory nearby
subtraction, not a solution on this sheaf owner.  No direct exact solution was
found within the bounded search.  The missing packet bridge, not presumed
novelty, prevents promotion.

**Disposition:** `HOLD_FOR_SOURCE`

### S16-R5 — F/V power correspondences as a new Hecke algebra

**Research question.**  Do the push-pull maps generated by the power maps
`pi_N:A^1->A^1` form a new rational-Witt Hecke algebra capable of replacing
the stopped shared-iota centre?

**Owner, domain, codomain, map, law.**  For normal Noetherian affine `X`, the
source owner is `underline Corr(X,A^1)`, functorially isomorphic to
`W_rat(O(X))`.  The maps are `pi_{N*}` and `pi_N^*`, corresponding exactly to
`F_N` and `V_N`.  Composition and projection laws come from finite
correspondence/power-map calculus.  No packet representation is part of this
owner.

**Primary/official locator or proof obligation.**  [Deninger 2025, Theorem
5.1 and Proposition 5.2](https://arxiv.org/html/2508.05329v1#S5) already owns
the isomorphism and F/V push-pull identification.  Any proposed “Hecke
algebra” must therefore prove a new representation or relation not formal
from the semigroup of power maps.

**Strongest generic retelling/attack.**  An algebra generated by push-pull
operators of finite power maps is a generic correspondence/semigroup algebra.
Renaming `F_N,V_N` as Hecke generators adds no theorem; their source
identification is already Proposition 5.2.

**Maximum subtraction.**  P2/P7/P8 remove trace/determinant inference;
P9/P10 remove topology inference; P11 removes action-sensitive analytic
promotion; P12/P13 remove cohomology/twist/corona repackaging; P15/Slot14
remove prime-tail and common-quotient content; P16 removes shared-lift
selectivity; P18 removes a represented coupled operator.  The source theorem
itself is prior and the added algebra is generic.

**Firewalls.**  Same owner: `PASS` algebraically.  Arbitrary probability:
`PASS` by type separation.  Independent lift: `PASS` by naturality of source
correspondences, but no shared-lift invariant is produced.  Time tensor:
`PASS` by type separation.  Forget owner: `FAIL`; finite power-map semigroup
algebras are generic, and the F/V identification is already source-owned.

**Smallest publication-weight theorem signature.**  A new relation or
faithful representation specific to the rational-Witt correspondence owner,
proved to fail for generic power correspondences and shown to act
load-bearingly on the actual arithmetic packet.  No such map is present.

**Bounded precedent ceiling.**  The exact F/V/Hecke query returned Deninger's
source theorem and strong KEnd/endomotive neighbors.  The direct source
theorem and generic semigroup reduction make a replacement claim untenable
regardless of bounded search silence for the word “Hecke.”

**Disposition:** `NO_GO`

## 8. Slot 18 candidates

### S18-R1 — normalized-Haar packet/time tensor trace

**Research question.**  Can normalized Haar integration over `B_p`, tensored
with the Paper-8 literal-time representation, produce a source-sensitive
packet trace or coupled determinant?

**Owner, domain, codomain, map, law.**  The exact typed algebra is
`M_p=L^infinity(B_p,mu_p) bar-tensor M_{log p}^{reg}` and the represented
time map is `1 bar-tensor lambda_{log p}`.  The trace is
`Tau_p=integral_{B_p} Tau_{log p} dmu_p`, mapping its positive/`L1` domain to
extended scalars.  Translation invariance forces any admissible transverse
multiplier to be scalar.

**Primary/official locator or proof obligation.**  Deninger supplies no such
operator.  The exact author-derived owner and its complete failure theorem
are in the hash-bound P18 receipt, with P7/P8 as the local proxy and time
owners.  There is no remaining proof obligation that can make normalized
Haar detect a constant transverse field.

**Strongest generic retelling/attack.**  Replace `(B_p,mu_p)` by any
probability space `(Omega,nu)`.  A constant decomposable field has the same
trace because `nu(Omega)=1`.  The construction is exactly an arbitrary
probability base tensor a time-only trace.

**Maximum subtraction.**  P2 removes packet measure/disintegration
provenance; P7 proves probability-base and arbitrary-clock blindness; P8 owns
the literal-time traces and their packet boundary; P9/P10 remove nontrivial
Borel/separated packet observables; P11 removes action information; P12/P13
remove formal cohomology/twist/corona repairs; P15/Slot14 remove compact-group
tail arithmetic; P16 removes cross-prime shared-lift coupling; P18 proves the
tensor reduction and scalar multiplier.  There is no delta.

**Firewalls.**  Same owner: `PASS` for the displayed tensor algebra only.
Arbitrary probability: `FAIL` decisively.  Independent lift: `FAIL` for any
claimed transverse choice sensitivity.  Time tensor: `FAIL` by construction.
Forget owner: `FAIL`; the formula is unchanged for every probability base.

**Smallest publication-weight theorem signature.**  A nonconstant
source-induced transverse observable in the same represented algebra, a
canonical disintegration, and a trace formula whose value changes under
probability-base substitution while remaining invariant under every source
choice.  P18 proves no such observable is present.

**Bounded precedent ceiling.**  The exact rational-Witt/Haar/time-tensor query
returned Deninger's arithmetic flow records but no source packet trace.  The
internal arbitrary-probability theorem is already conclusive.

**Disposition:** `NO_GO`

### S18-R2 — chosen mixed kernel or crossed product coupling packet and time

**Research question.**  Can one select a non-product integral kernel or
crossed-product cocycle on `B_p x S_{log p}` whose trace retains both packet
and return-time information?

**Owner, domain, codomain, map, law.**  A proposed kernel would define an
operator
`T_K:L^2(B_p x S_{log p})->L^2(B_p x S_{log p})` by integration against
`K(b,u;b',u')`; a crossed-product version would require a source action and
cocycle on the same owner.  The source supplies neither `K`, a transverse
relation, a cocycle, nor a representation.  No functorial transformation law
under translations or lift choices is available.

**Primary/official locator or proof obligation.**  [Deninger 2018](https://arxiv.org/abs/1807.06400)
does not define this analytic kernel.  The P18 receipt proves that the
source-typed transitions found in the bounded corpus are translation times
identity time and yield only the product owner.  An author-chosen weight,
chart, or kernel is explicitly forbidden by v4.

**Strongest generic retelling/attack.**  Any Hilbert spaces admit mixed
kernels, and any chosen measurable cocycle can manufacture a crossed product.
Without a source relation, the construction proves only a generic operator
theorem; changing the kernel changes the answer and defeats canonicity.

**Maximum subtraction.**  P2 removes a canonical packet measure; P7/P8 own
all current time trace and determinant formulas; P9/P10 remove separated
packet observables; P11 removes action-sensitive global-QC analytic content;
P12/P13 remove formal cocycle/twist/corona choices; P15/Slot14 remove compact
tail/common-quotient labels; P16 removes shared-choice coupling; P18 proves
the only typed representation factors.  The proposed kernel is the missing
data, not a theorem.

**Firewalls.**  Same owner: `FAIL`; the kernel/cocycle is chosen.  Arbitrary
probability: `FAIL` unless an unsourced density is inserted.  Independent
lift: `FAIL`; no covariance law is defined.  Time tensor: `PENDING` by design,
but breaking a tensor with an arbitrary kernel has no source credit.  Forget
owner: `FAIL`; the same construction works on arbitrary product spaces.

**Smallest publication-weight theorem signature.**  A source-derived
non-product correspondence on the actual packet, a canonical represented
algebra and measure, boundedness/trace-domain theorems, and an invariant trace
that fails on arbitrary products.  The first datum is absent.

**Bounded precedent ceiling.**  Exact mixed-kernel/crossed-product queries
found no source-defined rational-Witt packet operator.  This is an explicit
author-proof obligation, not evidence that one may choose a kernel.

**Disposition:** `NO_GO`

### S18-R3 — F/V power correspondence reinterpreted as a packet operator

**Research question.**  Can the algebraic power-map correspondences
`pi_{N*},pi_N^*` be represented as a coupled global packet operator with a
new determinant?

**Owner, domain, codomain, map, law.**  The actual source maps act on
`underline Corr(X,A^1) ~= W_rat(O(X))` for normal Noetherian affine `X`.
The proposed codomain would be operators on a packet Hilbert space, but no
functor from the correspondence category to the P18 represented algebra is
defined.  Push-pull functoriality on correspondences does not supply bounded
operator, trace, or determinant functoriality.

**Primary/official locator or proof obligation.**  [Deninger 2025, Proposition
5.2](https://arxiv.org/html/2508.05329v1#S5) identifies F/V with power-map
push-pull.  [Connes--Consani--Marcolli](https://arxiv.org/abs/math/0512138)
and [Connes--Consani](https://arxiv.org/abs/2112.08820) are strong primary
endomotive/BC precedents.  The author obligation would be a new exact
same-owner representation functor, not the declaration that a correspondence
“acts.”

**Strongest generic retelling/attack.**  Power maps generate generic
semigroup and endomotive representations.  An algebraic correspondence is
not automatically a bounded operator on the packet, and a represented
endomorphism is not automatically trace class or determinant class.

**Maximum subtraction.**  P2 removes the packet trace map; P7/P8 remove
Euler-product and local-trace promotion; P9/P10 remove compact topology and
measurable fields on the actual packet; P11 removes generic action
convolution; P12/P13 remove formal correspondence/twist packaging; P15 and
Slot14 remove arithmetic tail labels; P16 removes shared-choice coupling;
P18 explicitly rejects Deninger 2025 F/V correspondences as the wrong owner
without a bridge.  The same-owner map remains absent.

**Firewalls.**  Same owner: `FAIL`; algebraic and Hilbert owners are spliced.
Arbitrary probability: `FAIL` for any constant-field representation.
Independent lift: `PENDING`; no representation covariance exists.  Time
tensor: `FAIL` if represented through the current P18 tensor.  Forget owner:
`FAIL`; semigroup power-map operators are generic and heavily precedented.

**Smallest publication-weight theorem signature.**  A faithful functor from
the exact rational-Witt correspondence owner to a canonically represented
packet algebra, compatibility with actual source choices and F/V, a
non-product trace-domain theorem, and a determinant invariant not reducible
to an endomotive or arbitrary-clock construction.  No first map exists.

**Bounded precedent ceiling.**  The bounded power-map/operator query found
Deninger's algebraic theorem and substantial endomotive/KEnd prior, but no
same-owner packet representation.  The non-hit cannot license an asserted
operator.

**Disposition:** `NO_GO`

### S18-R4 — `K(C_{Y/X})`-to-cycle comparison and its higher extension

**Research question.**  Can Almkvist's theorem be generalized to a functorial
comparison between the K-theory of the exact/perfect category attached to
`Y->X` and universally integral relative cycles, including a nonaffine and
higher-degree version compatible with rational Witt F/V?

**Owner, domain, codomain, map, law.**  For affine `pi:Y->X`, Deninger defines
the exact category `C_{Y/X}` of quasicoherent `M` for which `pi_*M` is a
vector bundle and the object-level cycle
`cycle(M)=sum length(M_eta_i)[Z_i]` in relative proper cycles.  The desired
degree-zero map is
`K_0(C_{Y/X})->c_equi(Y/X,0)` after exact additivity is locked.  The proposed
nonaffine domain is a still-unspecified category of perfect complexes; the
higher codomains and functorial push/pull laws are also not fixed by the
source sketch.

**Primary/official locator or proof obligation.**  [Deninger 2025, closing
paragraph of Section 5](https://arxiv.org/html/2508.05329v1#S5) explicitly
proposes the `K_0(C_{Y/X})`/cycle comparison, removal of affineness via perfect
complexes, and higher K/higher cycle extension.  The author must first lock
the exact category, equivalence relation, degree, target cycle theory, and
functoriality; the source expresses a program, not a theorem.

**Strongest generic retelling/attack.**  Devissage, support-cycle maps,
determinants of endomorphisms, and K-to-trace/cycle transformations are major
existing theories.  The exact rational-Witt delta must be more than the
generic fact that a finite-support coherent object has a cycle.  It must
recover Deninger's Theorem 5.1/Almkvist comparison and prove new compatibility
or a sharply identified kernel/cokernel.

**Maximum subtraction.**  P2/P7/P8 remove direct promotion to packet trace,
zeta, or determinant; P9/P10 remove actual-packet topological inference; P11
removes generic action convolution; P12/P13 remove formal cohomology/twist or
constant-diagonal packaging; P15/Slot14 remove `B_p`/Ulm/Smith arithmetic;
P16 removes shared-lift coupling; P18 removes any current represented
operator.  The algebraic K/cycle question survives those theorems, but it is
not yet a Slot-18 operator replacement and has heavy external KEnd/trace
prior.

**Firewalls.**  Same owner: `PENDING`; the object-level cycle is sourced, but
the higher/nonaffine comparison owner is not locked.  Arbitrary probability:
`PASS` by type separation.  Independent lift: `PASS` only if the eventual map
is functorial.  Time tensor: `PASS` by type separation.  Forget owner: `FAIL`
for a generic support-cycle map; only a proved rational-Witt/F/V comparison
could pass.  The v4 packet/actual-standard and represented-operator gates are
currently `FAIL`.

**Smallest publication-weight theorem signature.**  Fix a nontrivial class of
arithmetic morphisms `Y->X`; construct the exact or stable category and a
well-defined comparison on K-groups; prove a kernel/cokernel theorem or
isomorphism beyond generic devissage; recover the affine Almkvist/rational-
Witt diagram; prove F/V push-pull compatibility; and, before any Slot-18
operator claim, construct a source-defined functor to the same packet
represented algebra.  This is a credible multi-lemma program, but its last
owner and its higher domain are absent.

**Bounded precedent ceiling.**  The exact `C_{Y/X}`/`c_equi` query returned
[Deninger 2025](https://arxiv.org/html/2508.05329v1#S5) as the direct
formulation.  Strong nearby priors include
[Blumberg--Gepner--Tabuada](https://arxiv.org/abs/1302.1214),
[Campbell et al.](https://arxiv.org/abs/2005.04334), and
[Agarwal et al.](https://arxiv.org/abs/2507.05956).  No direct exact
comparison package was found within the bounded search, but the unsettled
domain and missing packet representation control the hold.

**Disposition:** `HOLD_FOR_SOURCE`

### S18-R5 — KEnd/TR trace composed with a packet determinant

**Research question.**  Can the trace from K-theory of endomorphisms to TR,
or its characteristic-polynomial/zeta shadow, be composed with the
rational-Witt packet to obtain a new global determinant/operator?

**Owner, domain, codomain, map, law.**  The primary generic owner is a
K-theory spectrum/category of endomorphisms with a natural trace to `TR`; its
shadows include characteristic polynomials and Lefschetz zeta functions.  A
packet determinant would require a further natural map from that target to a
specific represented von Neumann or C*-algebra on the Deninger packet.  No
such map, representation, trace domain, or coupling law is defined.

**Primary/official locator or proof obligation.**  [Campbell et al.](https://arxiv.org/abs/2005.04334)
already own the KEnd-to-TR trace/zeta mechanism;
[Blumberg--Gepner--Tabuada](https://arxiv.org/abs/1302.1214) own a strong
motivic KEnd/rational-Witt framework; [Agarwal et al.](https://arxiv.org/abs/2507.05956)
own nearby F/V lifts.  Deninger supplies no packet representation of these
targets.  An author would need a genuinely new natural transformation into
the exact P18 packet algebra.

**Strongest generic retelling/attack.**  The central trace/zeta construction
is direct prior.  Composing it with a chosen representation or evaluating a
known characteristic polynomial is generic.  Calling the result a packet
determinant without a same-owner representation is an owner splice.

**Maximum subtraction.**  P2 removes an actual packet trace map; P7 owns the
proxy principal trace-log and arbitrary-clock compiler; P8 owns local traces
and refutes packet promotion; P9/P10 remove standard measurable packet
fields; P11 removes generic action convolution; P12/P13 remove formal
cohomology/twist/corona repackaging; P15/Slot14 remove old arithmetic labels;
P16 removes shared-lift coupling; P18 removes the only available
probability/time tensor.  External KEnd/TR prior removes the remaining generic
trace centre.

**Firewalls.**  Same owner: `FAIL`; the packet representation is absent.
Arbitrary probability: `FAIL` if the current constant-field tensor is used.
Independent lift: `PENDING`; no covariance map exists.  Time tensor: `FAIL`
on the current P18 owner.  Forget owner: `FAIL`; the KEnd/TR trace and zeta
mechanism are already generic and source-independent.

**Smallest publication-weight theorem signature.**  A natural same-owner map
from a rational-Witt KEnd/cycle object into a canonically represented actual
packet algebra, proof of non-product coupling and trace-class domain,
compatibility with F/V and source choices, and a determinant theorem not
implied by the existing TR trace or P7 arbitrary-clock compiler.  The first
map is absent.

**Bounded precedent ceiling.**  The KEnd/TR query directly found the three
primary prior programs above and related BC/endomotive work.  This is not a
search-silence case: direct generic precedent plus the missing packet map
requires rejection.

**Disposition:** `NO_GO`

## 9. Integrated adversarial adjudication

### 9.1 Why no candidate advances now

The screen was attacked from both ends of the v4 chain.

From the carrier end, every immediately constructible topology, reflector,
cochain cone, compact quotient, or shared-lift object reduces to P9/P10,
P12/P13, or P15/Slot14/P16.  The only source suggestion that could change the
carrier is stronger descent, but the source deliberately leaves the
replacement functor undefined.

From the operator end, every immediately constructible trace or determinant
either factors through an arbitrary probability base tensor a time-only
operator, uses an unsourced kernel/representation, or lands in strong generic
KEnd/TR/endomotive precedent.  The source K/cycle direction is mathematically
substantial, but it is not yet a represented packet owner.

The fp/fppf Verschiebung question is the sharpest exact source-authored map in
the screen.  It passes the algebraic same-owner tests, but v4 additionally
requires load-bearing use of the arithmetic packet or actual/standard
comparison.  Inventing that bridge would violate the source-map rejection
rule.  It is therefore held, not advanced.

### 9.2 Finding register

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none; the screen itself has no owner contradiction or unauthorized positive verdict |
| Major (`M`) | 3 | `M1` Slot-14 stronger-descent owner/map undefined; `M2` Slot-16 V-lift has no packet/actual-standard bridge; `M3` Slot-18 K/cycle higher owner and packet representation undefined |
| Minor (`m`) | 0 | none; search incompleteness is a declared ceiling, not a curable copy-edit finding |

These counts belong only to this replacement screen.  They do not alter the
binding historical counts of Slot 14, P15, P16, P18, or any prior paper.

## 10. Authorization and machine-readable receipt

```text
SCREEN_VERSION=P14-18-REPLACEMENT-SCREEN-v4.0
SCREEN_DATE=2026-08-16
BATCH_V4_SHA256=6660dd17ff52ad80509358d6f3cd18119c068374383edb5ad6fc9d8bb7e6d76e
BATCH_V4_HASH_MATCH=true
TARGET_ABSENT_AT_START=true

STOPPED_SLOT_COUNT=3
CANDIDATE_COUNT=14
SLOT14_CANDIDATE_COUNT=4
SLOT16_CANDIDATE_COUNT=5
SLOT18_CANDIDATE_COUNT=5

SLOT14_RETAINED_COUNT=1
SLOT14_RETAINED_ID=S14-R4
SLOT14_DISPOSITION=HOLD_FOR_SOURCE

SLOT16_RETAINED_COUNT=1
SLOT16_RETAINED_ID=S16-R4
SLOT16_DISPOSITION=HOLD_FOR_SOURCE

SLOT18_RETAINED_COUNT=1
SLOT18_RETAINED_ID=S18-R4
SLOT18_DISPOSITION=HOLD_FOR_SOURCE

IMMEDIATE_SEPARATE_PRECHECK_COUNT=0
HOLD_FOR_SOURCE_COUNT=3
NO_GO_COUNT=11

CRITICAL_OPEN=0
MAJOR_OPEN=3
MINOR_OPEN=0
FINDINGS=C0/M3/m0

NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH=true
UNIVERSAL_NOVELTY_CLAIM_ALLOWED=false
NEW_SOURCE_PDF_RETAINED=false

SEPARATE_PRECHECK_AUTHORIZED=false
NEW_PROTOCOL_AUTHORIZED=false
NEW_CANDIDATE_LOCK_AUTHORIZED=false
NEW_PROOF_AUTHORIZED=false
CONTROL_DESIGN_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
FIGURE_WORK_AUTHORIZED=false
RELEASE_AUTHORIZED=false
ARCHIVE_AUTHORIZED=false
GIT_ACTION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false

P15_CHANGING_CONTROL_DESIGN_READ=false
P17_IMPLEMENTATION_OR_RESULTS_READ=false
SELF_HASH_EMBEDDED=false
```

**Binding screen conclusion:** fourteen questions were tested; exactly one
source-wait candidate is retained per stopped slot; zero candidates are ready
for a separate precheck; and the integrated result is `C0/M3/m0`.  No
downstream work is authorized by this report.
