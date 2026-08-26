# Paper 14 Phase-2 independent global-topology proof review

Status: **COMPLETE — READ-ONLY MATHEMATICAL PEER REVIEW**  
Role: **independent domain / devil's-advocate proof reviewer**  
Date: 2026-08-16 (Asia/Shanghai)  
Proof verdict: **PASS — C0 / M0 / m0**  
Standalone disposition: **NOT ASSESSED BY THIS REPORT**  
Controls, Route A/B, manuscript, release, Git, and public synchronization:
**not authorized / not performed**

## 1. Exact-byte review basis

The Phase-1 gate, every input bound by that gate, the submitted proof, the
two inherited exact proof audits, and the retained primary source were
rehashed immediately before substantive review.

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/phase1_final_gate.md` | `fb645cfbb21e299d78f698699ccb2abe1c5b68b4c64e7c3efc32521fe7dc297c` | exact match |
| `notes/papers14_18_batch_design_lock.md` | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | exact match |
| `notes/research_protocol.md` | `a3ee049f27d29bb276553edcee8fbb019125b96c3e90b82f800a9706a106d7ab` | exact match |
| `notes/candidate_lock.md` | `8cbbd9e63f53c8f821f940405c6f5a41f34a5242ab9ea24be1fb87b47ae9b096` | exact match |
| `notes/phase1_amendment_v1.md` | `931d0c83528d1e05b467cf8f378b8798d2e14170c9505bcaeb5566de0a8cae16` | exact match |
| `notes/phase1_source_topology_precheck.md` | `05fb9f622c348839514d4d69760e491e7d2afdf4eb9f14687d5e0ce05d1229cb` | exact match |
| `notes/phase1_methodology_review.md` | `581e2ad01156d80f6b91febaa431d81352c47431de8a0fd865d9c71993861bf4` | exact match |
| `notes/phase1_devils_source_review.md` | `5f2e85b211b159b0333cf28ce64c83cb76eb9abb4ac7f8f00cfcacf258462b86` | exact match |
| `notes/phase2_global_topology_proofs.md` | `3d03722c866a6ec9998673ff404cd05208106d4953e8d4461429c6fd303371fe` | exact submitted proof |
| Paper-9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | exact match |
| Paper-10 proof audit | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | exact match |
| retained Deninger arXiv-v4 PDF | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | exact primary-source bytes |
| local Deninger source audit | `a4785e0fd56cb4e24211ea4d8f0e78a83ccdd6c942dc6572c87b2c1230ae521a` | exact locator cross-check only |

The load-bearing Deninger text was read directly at physical pp. 27, 31--39,
40--52.  In particular, this review checked Definition 4.1, Proposition 4.2,
Theorems 5.2 and 6.1, Lemma 7.1, Lemma 7.3, Proposition 7.4, the admissible-
`E` paragraph following Theorem 7.10, Claim 8.1, Theorem 8.2, and Lemma 8.3.
The local source audit was not substituted for the primary text.

The review re-derived the proof rather than inheriting the proof ledger's
`PASS` label.  No proof, protocol, control, Route, or manuscript file was
modified.

## 2. Executive mathematical verdict

The frozen proof is correct on its declared owner and within its declared
source ceiling.

1. The descended map `pi` and the full-fibre formula
   `Gamma_p=pi^{-1}((p))` are correctly obtained from Deninger's base map,
   invariance, full finite-field fibre, and quotient topology.
2. The finite packet theorem and ambient singleton closure use only ambient
   closedness plus Paper 9's exact inherited indiscreteness; no proxy topology
   enters.
3. The source evaluation `P |-> P(p)` gives a genuine all-stage open
   isolator.  Its zero/unit-modulus dichotomy survives the raw-to-Galois,
   Galois-to-colimit, rational saturation, and suspension passages.
4. Consequently every packet is relatively open in the actual all-prime
   locus, so arbitrary packet unions are clopen.  This proves G1 and every
   branch of G2, including the infinite-coinfinite branch, without inference
   from finite restrictions.
5. The ambient closure reduction is exact.  Empty, finite, all-prime, and
   cofinite subfamilies are classified correctly.  The arbitrary-`S`
   incidence formula has the right neighborhood quantifiers, and the
   infinite-coinfinite classification stops at the precise missing
   `S`-relative incidence theorem rather than inserting an assumption.
6. The quotient topology and `T0` universal property follow in the correct
   order after G1--G2.

No Critical, Major, or Minor correction is required.

## 3. General quotient and closure lemmas

### 3.1 Open-quotient closure identity

For an open continuous surjection `q:E->B`, the ledger's identity

```text
q^{-1}(closure_B(A)) = closure_E(q^{-1}(A))
```

is correct.  Continuity gives the inclusion from right to left.  If an open
neighborhood `V` of `e` misses `q^{-1}(A)`, then the open neighborhood
`q(V)` of `q(e)` misses `A`, because any `a=q(v)` in `A` would put
`v` in `q^{-1}(A)`.  Thus the reverse inclusion is valid without a
separation or countability hypothesis.

This applies to:

- the Galois orbit maps, since the action is by homeomorphisms and the image
  of an open set has open saturation; and
- the suspension orbit map `rho`, by Paper 9's exact open-quotient proof.

### 3.2 Product and saturation reduction

For `C_S=union_{p in S} C_p`, base invariance makes
`C_S x R_{>0}` saturated.  The product identity

```text
closure(C_S x R_{>0}) = closure(C_S) x R_{>0}
```

is valid because the second factor is the whole nonempty space.  Applying
the open-quotient identity and then surjectivity of `rho` gives equations
(3.2)--(3.3) exactly.  No closed-map property of `rho` is assumed.

## 4. Independent review of `P14-0`

Deninger Proposition 4.2 makes the admissible `E_f` subsystem invariant and
extends the base map equivariantly with trivial rational action on the base.
Section 7 supplies continuity through the pointwise stage, Galois quotient,
and Frobenius colimit.  Hence

```text
(P,u) |-> pr(P)
```

is continuous and constant on every diagonal `Q_{>0}` orbit, so the quotient
universal property gives the unique continuous `pi`.

The full-fibre assertion is also correctly typed.  In Section 5, for a
finite-residue-field point `x_0`, Deninger's `C_{x_0}` is the
`Q_{>0}`-extension of the entire base fibre.  Theorem 5.2 states that when
`E` contains `E_f`, the full `C_{x_0}` remains; taking `E=E_f` therefore
gives

```text
pr^{-1}((p)) = C_p.
```

This invariant equality commutes with the suspension quotient, yielding
`Gamma_p=pi^{-1}((p))`.  Since `(p)` is closed in `Spec Z`, each
`Gamma_p` is ambient closed.  Distinct base fibres are disjoint.

Verdict: **P14-0 PASS**.

## 5. Independent review of the finite theorem

For finite nonempty `F`, each `Gamma_p` is closed in `X_susp`.  Its
complement in `U_F` is a finite union of the other closed packets, so it is
also relatively open.  Paper 9 proves the exact inherited topology of each
packet is nonempty indiscrete.  Therefore the opens in `U_F` are exactly
the packet unions `U_S`, `S subset F`, and the canonical finite component
map is a homeomorphism.

For `x in Gamma_p`, ambient closedness gives

```text
closure_X_susp({x}) subset Gamma_p,
```

while Paper 9's indiscreteness gives
`closure_Gamma_p({x})=Gamma_p`.  The ordinary subspace-closure identity
gives the reverse inclusion.  Hence the ambient singleton closure, absence
of cross-prime specialization, finite discrete `T0` quotient, and four-open
two-prime case all follow.

This uses a closure identity, not a claim that sequences characterize every
ambient closure.

Verdict: **finite theorem PASS**.

## 6. Stage-by-stage attack on the all-prime isolator

The main hostile question is whether the proposed open condition really
survives every topology-changing stage.  It does.

### 6.1 Raw pointwise stage

At the affine pointwise stage a point is a multiplicative map extended by
zero.  Evaluation at the fixed ring element `p` is a coordinate projection
in the ambient product topology.  Therefore

```text
V_p = {P: |P(p)| < 1/2}
```

is open after restriction to the exact `E_f` subspace.

On a raw point above `(p)`, the image of the integer `p` is zero, so
`P(p)=0`.  On a raw point above `(q)`, `q!=p`, its image is a nonzero element
of `overline(F_q)^times`.  That group is torsion; every multiplicative
character sends a finite-order element to a root of unity.  Thus
`|P(p)|=1`.  The condition cuts out exactly the `p`-fibre among all
finite-field fibres.

This calculation uses neither injectivity nor a coordinate model for the
packet; finite-kernel membership is sufficient and, in fact, not needed for
the modulus of an individual torsion image.

### 6.2 Galois quotient

The global Galois group fixes the rational integer `p`, so `V_p` is
Galois-invariant.  The Galois action is by homeomorphisms, hence its orbit
projection is open.  The image `V_{p,0}` is therefore open and retains the
same exact finite-fibre intersection.

No representative-dependent value is used after quotienting: invariance is
proved before the image is taken.

### 6.3 Frobenius colimit and rational saturation

Proposition 7.4 proves that the initial pointwise/Galois stage is an open
subspace of the Frobenius colimit, not merely continuously embedded.  Thus
`V_{p,0}` is genuinely open in the colimit.  Every rational Frobenius map is
a homeomorphism.  Consequently

```text
W_p = union_{r in Q_{>0}} F_r(V_{p,0})
```

is open and `Q_{>0}`-invariant.

Every `C_p` point can be moved by an integral Frobenius map into the initial
stage; its base remains `(p)` and it lies in `V_{p,0}`, so `C_p subset W_p`.
Conversely, if a `C_q` point lies in `F_r(V_{p,0})`, applying `F_r^{-1}`
preserves the base `q` and produces a `V_{p,0}` point above `(q)`.  The raw
zero/unit calculation forces `q=p`.  Hence

```text
W_p intersection union_q C_q = C_p.
```

This proves the full raw-to-Galois-to-colimit firewall; it does not assume
that the value inequality itself is rational-Frobenius invariant.  The union
of all rational translates supplies the needed invariant saturation.

### 6.4 Suspension quotient

`W_p x R_{>0}` is open and saturated for the diagonal action.  The open
suspension quotient therefore sends it to an open `O_p`.  Since the rational
action preserves the base prime, the finite-fibre intersection descends to

```text
O_p intersection Per = Gamma_p.
```

The proof correctly permits `O_p` to contain generic points.  It claims only
relative isolation inside `Per`; this is why the argument does not falsely
make `Gamma_p` ambient open.

Verdict: **Lemma 6.1 PASS through all four stages**.

## 7. Review of G1 and G2

The isolator makes every `Gamma_p` open in the actual subspace `Per`.
Together with Paper 9's component indiscreteness, this proves that an open
set in the coproduct domain is a union of whole components and that its image
is open in `Per`.  The canonical continuous bijection `J` is therefore open
and a homeomorphism.

This proof uses the all-prime family of source opens and not the finite
packet theorem.  It genuinely distinguishes the discrete index topology
from the cofinite control.

For arbitrary `S subset P`, both

```text
U_S = union_{p in S} Gamma_p
U_{P\S} = Per \ U_S
```

are arbitrary unions of relatively open packets.  Thus every `U_S` is
clopen and `closure_Per(U_S)=U_S`.  The empty, finite nonempty, cofinite,
infinite-coinfinite, and all-prime branches all satisfy the same formula for
the same proved reason.  No countability restriction on the union is needed,
because a topology is closed under arbitrary unions.

The derived identity

```text
closure_X_susp(U_S) intersection Per = U_S
```

is the standard subspace-closure identity.  The ledger does not promote it
to an ambient classification.

Verdicts: **P14-G1 PASS; P14-G2 PASS for every `S`**.

## 8. Review of G3 ambient closure

### 8.1 Unitary ceiling and all-prime endpoint

Deninger Theorem 8.2 proves, for `Spec Z` without the conditional higher-
dimensional hypothesis, that the raw finite-field finite-kernel locus is
dense in the raw unitary locus.  The periodic set is already contained in
`E_f`.  Therefore the subspace closure formula gives, on the exact `E_f`
owner,

```text
closure_{E_f}(periodic points) = E_f intersection unitary locus.
```

The Galois and suspension orbit maps are open and the relevant subsets are
saturated, so the open-quotient closure identity transports this equality.
The Frobenius-colimit form is already part of Theorem 8.2.  This verifies

```text
closure_X_susp(Per) = Unit_{E_f}.
```

The unitary locus is closed at each pointwise stage.  The inductive-limit
closed-set criterion retains closedness, intersection with `E_f` gives a
closed subspace set, and the saturated suspension preimage is closed.
Because the suspension topology is a quotient topology, a saturated set
whose full preimage is closed has closed image.  The ledger therefore does
not need the quotient map itself to be closed.

The proof explicitly credits this all-prime equality to Deninger rather than
to Paper 14.

### 8.2 Sharp universal bounds

Monotonicity gives the unitary upper bound.  For every excluded prime
`q in P\S`, the ambient open `O_q` contains `Gamma_q` and is disjoint from
`U_S`, so no point of `Gamma_q` is in the ambient closure.  This verifies

```text
U_S subset closure_X_susp(U_S)
    subset Unit_{E_f} \ U_{P\S}.
```

The full-fibre theorem also shows that all finite-base points of the frozen
`E_f` owner lie in the corresponding `C_p`; hence every new point permitted
by the bound lies over the generic base point.  No finite-base stratum is
silently omitted.

### 8.3 Empty, finite, and cofinite branches

The empty branch is tautological.  A finite `U_S` is a finite union of the
ambient closed fibres from `P14-0` and is therefore closed.

For cofinite `S`, let `F=P\S` be finite.  The upper inclusion is the universal
bound.  To prove the reverse inclusion at a generic unitary point, Deninger's
Lemma 8.3 reduces a basic finite-evaluation neighborhood to a maximal ideal
in the set furnished by Claim 8.1.  For the number-ring stratum arising in
the `Spec Z` proof, the primary source states that this eligible set is
infinite, indeed of positive Dirichlet density.  A fixed rational prime has
only finitely many maximal ideals in the finite number field/order used for
the finite constraints.  Hence only finitely many eligible maximal ideals
can lie over the finite set `F`; one can choose an eligible ideal over a
rational prime in `S`.

The resulting finite-field character has finite kernel, lies in the
prescribed basic neighborhood, and belongs to an `S` packet.  Directing the
basic neighborhoods by reverse inclusion gives a net converging to the raw
generic point.  The open Galois and suspension quotient identities and the
Frobenius homeomorphisms transport membership in closure to the exact owner.
Thus

```text
closure_X_susp(U_S) = Unit_{E_f} \ U_F
```

for every cofinite `S`.  This is not inferred merely from the fact that the
eligible set is nonempty; the infinitude statement is exactly what permits
finite prime exclusion.

Verdict: **G3 empty/finite/all/cofinite branches PASS**.

### 8.4 Arbitrary-`S` incidence formula

The incidence formula's quantifiers are exact.

- Finite-coordinate neighborhoods with one common positive tolerance form
  a cofinal neighborhood basis: from finitely many coordinate neighborhoods
  choose a positive radius below their finite minimum.
- After a Frobenius homeomorphism moves a colimit point into the open initial
  stage, closure may be tested using neighborhoods contained in that stage.
- The Galois and suspension open-quotient identities say that a quotient
  point is in closure exactly when any, equivalently every, lift is in the
  closure of the saturated full preimage.
- Galois conjugation and rational Frobenius preserve the base rational prime,
  so the property `S intersection Elig(a;T,epsilon) != empty` is independent
  of the chosen lift and stage in the precise sense required by the proof.
- The unrestricted time factor contributes no extra incidence condition.

It follows that a generic unitary suspended point belongs to
`closure_X_susp(U_S)` exactly when every basic finite-evaluation neighborhood
has an eligible finite-field approximant whose rational base prime lies in
`S`.  Formula (9.10) is therefore an exact closure criterion, not merely a
one-sided bound.

### 8.5 Infinite-coinfinite stopping rule

Claim 8.1 and Lemma 8.3 supply an infinite eligible set for each finite
approximation problem.  Their quantifiers do not assert intersection with
an arbitrary prescribed infinite coinfinite subset of rational primes.
Infinitude on both sides does not force intersection, and the eligible set
may encode splitting, order, and congruence restrictions.

The proof therefore stops at the exact missing assertion

```text
for every generic a and every basic finite-evaluation neighborhood,
S intersects Elig(a;T,epsilon).
```

The label `SOURCE_UNDERDETERMINED_FOR_CLASSIFICATION` is used narrowly: the
topology is already uniquely defined, and the source does not provide the
additional arithmetic incidence theorem needed to simplify the exact
criterion for every prescribed infinite coinfinite `S`.  The ledger states
this distinction explicitly.  It neither treats a bounded search failure as
a theorem nor inserts a Chebotarev hypothesis.

Verdict: **G3 arbitrary-`S` formula and typed stop PASS**.

## 9. Review of G4 and the use of nets

Because `kappa^{-1}(S)=U_S` is open for every `S subset P`, the quotient
topology induced by `kappa` is discrete.  Paper 9 makes all points within a
packet topologically indistinguishable; the relatively clopen packet
isolators distinguish points in different packets.  Thus the packet fibres
are exactly the Kolmogorov equivalence classes.

For a continuous map `f:Per->T` to a `T0` space, the restriction to an
indiscrete packet is constant.  The induced set map on `P` is unique by
surjectivity of `kappa` and is continuous because `P` has the computed
discrete topology.  This proves the universal property only after the
quotient topology is known.  The final comparison with the cofinite prime
subspace of `Spec Z` has the correct direction: the identity from discrete
primes to cofinite primes is continuous.

All non-first-countable closure steps use neighborhoods or nets.  The only
sequence inherited from Paper 9 proves the within-packet lower inclusion in
an ambient singleton closure, for which existence of that particular
convergent sequence is sufficient.  It is not used as a characterization of
arbitrary closure.  The cofinite proof explicitly constructs a neighborhood-
directed net.

Verdicts: **P14-G4 PASS; net/closure discipline PASS**.

## 10. Adversarial falsifier record

| Attack | Result | Reason |
|---|---|---|
| `Gamma_p` might be only a periodic subset, not the full base fibre | **REFUTED** | Section 5 defines the full finite-field fibre and Theorem 5.2 retains it for `E_f`. |
| evaluation at `p` might fail on another prime fibre | **REFUTED** | zero at characteristic `p`; a root of unity of modulus one in every other finite characteristic. |
| the evaluation open might be lost at the Galois quotient | **REFUTED** | it is invariant and the orbit projection is open. |
| an initial-stage open might not be colimit-open | **REFUTED** | Proposition 7.4 makes the initial stage an open subspace. |
| rational saturation might add other prime fibres | **REFUTED** | every `F_r` preserves the base point. |
| the suspension image might not be open | **REFUTED** | the global orbit quotient is open by Paper 9. |
| finite clopen components might be promoted to an all-prime theorem | **REFUTED / NOT USED** | the all-prime source isolator is proved independently. |
| arbitrary unions might fail to be closed | **REFUTED** | their complements are also arbitrary unions of relatively open packets. |
| relative closure might be promoted to ambient closure | **REFUTED / NOT USED** | G3 uses the pre-suspension closure reduction and unitary ceiling. |
| Deninger 8.2 might be cited for every prescribed `S` | **REFUTED / NOT USED** | the ledger exposes the missing `S`-incidence quantifier. |
| positive density might imply intersection with every infinite `S` | **REFUTED / NOT USED** | it is used only to remove finitely many rational primes. |
| the incidence formula might depend on a lift | **REFUTED** | saturated preimages plus Galois/Frobenius base-prime invariance give lift independence. |
| `P_discrete` might be confused with the cofinite base subspace | **REFUTED** | the comparison map and topology direction are stated explicitly. |

## 11. Severity and final verdict

### Critical findings

None.

### Major findings

None.

### Minor findings

None.  In particular, the phrase
`SOURCE_UNDERDETERMINED_FOR_CLASSIFICATION` is already qualified so that it
cannot be read as nonuniqueness of the frozen topology.

### Machine-readable review verdict

```text
P14_PHASE2_INDEPENDENT_MATH_REVIEW=COMPLETE
REVIEWED_PROOF_SHA256=3d03722c866a6ec9998673ff404cd05208106d4953e8d4461429c6fd303371fe
PHASE1_GATE_SHA256=fb645cfbb21e299d78f698699ccb2abe1c5b68b4c64e7c3efc32521fe7dc297c
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
P14_0_REVIEW=PASS
FINITE_PACKET_REVIEW=PASS
ZERO_UNIT_ALL_STAGE_FIREWALL=PASS
P14_G1_REVIEW=PASS
P14_G2_REVIEW=PASS
P14_G3_EMPTY_FINITE_ALL_COFINITE_REVIEW=PASS
P14_G3_ARBITRARY_S_INCIDENCE_REVIEW=PASS
P14_G3_INFINITE_COINFINITE_STOP_REVIEW=PASS
P14_G4_REVIEW=PASS
NET_AND_T0_UNIVERSAL_PROPERTY_REVIEW=PASS
OVERALL_MATHEMATICAL_VERDICT=PASS
STANDALONE_REVIEW_PERFORMED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

Final verdict on the exact frozen proof:
**PASS — C0 / M0 / m0**.  This report confirms mathematical correctness and
the typed G3 stopping boundary only.  It deliberately makes no standalone,
novelty, or publication-weight decision.
