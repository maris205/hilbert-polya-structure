# Paper 11 Phase-1 source / terminology feasibility review

Review date: **2026-08-14 (Asia/Shanghai)**  
Review type: independent ARS source-verification, integrity, and bounded-prior-art audit  
Verdict: **REVISE — mathematically feasible; C=0, M=3, m=1**  
Phase gate: **BLOCKED pending a versioned terminology/domain amendment and independent exact-byte re-lock**  
Novelty status: **SUPPORTED_WITHIN_SEARCH** only

This report is source and design feasibility work only. It proves no `P11-*`
target, starts no Phase-3 proof, evaluates no Route, edits no active lock, and
retains no new full text.

## 1. Exact review binding

The review is bound to the following active bytes:

| Active input | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `f1575e6d605a5dc442deb5889415f10166d0a6f0e11e8395733dad77a6f2a66f` |
| `notes/candidate_lock.md` | `6815e1d4e09159be9dbb8b0df0d7098e3cafae0e06f7da85a143c9e6c33caea7` |
| `notes/pipeline_state.md` | `406fcc08459b2093aaf52d187d4d9f2f928a40269951681c91c628168e75c95d` |

The inherited topology and operator/source ledgers were read rather than
silently re-created. In particular:

| Inherited ledger | SHA-256 / role |
|---|---|
| Paper 8 `notes/phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42`; standard transitive-circle crossed product |
| Paper 8 `notes/sources/phase2_topology_source_manifest.md` | `ca9c7f7527bd1b523fb8dc98bf541d157601bd97b9458fb9d50b712bd5a4c58b`; Deninger/Morishita manifestations |
| Paper 8 `notes/sources/trace_source_manifest.md` | `517a498d78526467696a539cc8a481084fa7acdccaa5367e7cfa1866ceefbe5e`; Fourier/dual-Haar boundary |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20`; actual rational-Witt topology ownership |
| Paper 9 `notes/sources/paper9_source_manifest.md` | `8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906`; exact primary-source corpus |
| Paper 10 `notes/sources/scope_source_manifest.md` | `38fd6557eba364eff748b35a62ac28bf768b75a259e1e7631099149f67118140`; separated-observable boundary |
| Paper 10 `notes/sources/dom-source-manifest.md` | `49e20c34eff26915780f43b5df7d5b6635fa35d6225b63ea476cbeab1c14af21`; operator/measure/domain conventions |

The inherited release and proof hashes in `candidate_lock.md` were also
rechecked. The Paper-9 proof/PDF hashes are respectively `c38c2429...` and
`c55e4f45...`; the Paper-10 proof/PDF hashes are respectively `efda522e...`
and `30c22eb8...`. No stale-source or stale-release mismatch was found.

## 2. Executive source finding

The proposed convention split is real and researchable, but the standard
non-Hausdorff groupoid literature does **not** license standard groupoid
terminology for the actual object.

For a nontrivial indiscrete `X=X_{p,a}`, the product arrow topology on
`X x R` has opens exactly `X x U`, with `U` open in `R`. Hence it has no
nonempty Hausdorff open subset and is not locally Hausdorff. Its unit space is
also non-Hausdorff. These facts put it outside every retained standard
groupoid-`C*` framework below. They do not prevent a direct, author-defined
calculation on the globally continuous functions: the same topology strongly
indicates

```text
f(x,t)=g(t),
support(f)=X x support(g),
```

and the proposed fibrewise Lebesgue formulas then reduce to the group
convolution formulas on `R`. Those conclusions remain Phase-3 proof
obligations, not source-owned theorems.

The decisive distinction is therefore:

```text
HOPEN-SPAN-VALUE = 0                         direct diagnostic computation
STANDARD-FRAMEWORK-APPLICABILITY = NOT_APPLICABLE
GLOBAL-QC-SUPPORT ALGEBRA ~= C_c(R)          author-defined, if proved
```

The first line must never be serialized as “the standard groupoid
`C*`-algebra is zero,” and the third line must never be serialized as
`C^*(G_{p,a}^{act})`.

## 3. Primary/authoritative framework audit

### 3.1 Jean-Louis Tu: locally Hausdorff is built into “locally compact”

Jean-Louis Tu, “Non-Hausdorff groupoids, proper actions and K-theory,”
*Documenta Mathematica* **9** (2004), 565--597,
[DOI 10.4171/DM/178](https://doi.org/10.4171/DM/178),
[official article page](https://ems.press/journals/dm/articles/8965109),
[arXiv v2 full text](https://arxiv.org/pdf/math/0403071v2).

- Definition 1.1, physical/printed p. 3: “compact” means quasi-compact **and
  Hausdorff**; “locally compact” means that every point has a compact
  neighborhood. Tu immediately notes that such a space is locally Hausdorff.
- Section 4.1, physical/printed p. 17: for a locally compact space `Y`, Tu
  defines `C_c(Y)_0` from `C_c(V)` on open Hausdorff `V`, extended by zero,
  and defines `C_c(Y)` as their linear span. The resulting functions need not
  be globally continuous.
- Definition 4.6, physical/printed p. 18: a Haar system is defined for a
  locally compact groupoid whose range fibres are Hausdorff; its tests use
  that `C_c(G)`, full fibre support, continuity/compact support of the
  fibre-integral function, and left invariance.

**Applicability:** `NOT_APPLICABLE` to `G_{p,a}^{act}`. The actual arrow space
has no compact Hausdorff neighborhood at any point. Its individual range
fibres are copies of `R`, but fibre Hausdorffness alone does not repair the
failed ambient hypothesis. The Hausdorff-open span in Paper 11 is a faithful
diagnostic analogue of Tu's convention, not an invocation of Tu's groupoid
algebra.

### 3.2 Muhly--Williams: the Hausdorff-open span is accepted practice, under strict standing assumptions

Paul S. Muhly and Dana P. Williams, “Renault's Equivalence Theorem for
Groupoid Crossed Products,” *NYJM Monographs* **3** (2008),
[official record](https://nyjm.albany.edu/m/2008/3.html),
[official full text](https://nyjm.albany.edu/m/2008/3v.pdf),
[arXiv record](https://arxiv.org/abs/0707.3566).

- Physical/printed pp. 3--4: the authors call it “accepted practice” to replace
  `C_c(X)` by the vector space `C(X)` spanned by zero-extensions of `C_c(U)`
  over all Hausdorff open subsets `U`. They explicitly warn that the
  zero-extensions need not be globally continuous or compactly supported in
  the ambient non-Hausdorff space.
- Physical/printed pp. 6--7, assumptions G1--G4: the groupoid operations are
  continuous, `G^(0)` is Hausdorff, every arrow has a compact Hausdorff
  neighborhood, and range/source are open; the overall treatment is also
  second countable.
- Physical/printed p. 7: their Haar-system axioms are formulated on the
  Hausdorff range fibres and the above `C(G)`, with invariance and continuity
  into `C_c(G^(0))`; the paper assumes full Haar systems.
- Proposition 4.4, physical/printed pp. 21--23: convolution and involution on
  the span of compactly supported sections over Hausdorff open patches are
  well-defined under those locally Hausdorff/locally compact/Hausdorff-unit
  assumptions.

**Applicability:** `NOT_APPLICABLE` to the actual object and `APPLICABLE` in
the ordinary Hausdorff-circle proxy after the action convention is matched.
This source gives a positive answer to the narrow question “is
Hausdorff-open-span an actual literature convention?” It gives a negative
answer to “may Paper 11 call its actual diagnostic the standard algebra?”

### 3.3 Independent boundary checks

Ruy Exel, “Non-Hausdorff groupoids,”
[arXiv:0812.4087v3](https://arxiv.org/pdf/0812.4087v3), physical/printed p. 1,
defines an étale groupoid with locally compact Hausdorff unit space and local
homeomorphism range/source maps, while allowing the arrow space itself to be
non-Hausdorff. The actual Paper-11 unit is not Hausdorff and its continuous
`R`-fibres are not étale. **Status: `NOT_APPLICABLE`.**

Alcides Buss, Rohit Holkar, and Ralf Meyer, “A universal property for groupoid
C*-algebras. I,” *Proceedings of the London Mathematical Society* **117**(2)
(2018), 345--375, [DOI 10.1112/plms.12131](https://doi.org/10.1112/plms.12131),
[arXiv:1612.04963](https://arxiv.org/pdf/1612.04963). Physical/printed pp. 1--2
state that the paper works throughout with locally compact Hausdorff groupoids
with Haar systems and that its universal property, as written, only works for
Hausdorff groupoids. Section 7.1 and Theorem 7.1, printed p. 23, identify the
groupoid `C*`-algebra of a transformation groupoid with the corresponding
crossed product for a locally compact group acting on a locally compact
Hausdorff space. **Status: `NOT_APPLICABLE` to the actual object;
`APPLICABLE` to the standard-circle proxy.**

No primary/authoritative source found in this bounded audit supplies a
standard full or reduced groupoid `C*` construction for the exact combination

```text
non-Hausdorff indiscrete unit
+ arrow space not locally Hausdorff
+ no nonempty Hausdorff open arrow patch.
```

This is a framework non-hit, not a theorem that no conceivable construction
can ever be made.

## 4. Load-bearing compactness fork

The word “compact” in `research_protocol.md:80-82` is presently unsafe. It
changes the answer to the main feasibility question.

- In the open-cover sense, `X x K` is quasi-compact whenever `K` is compact
  in `R`; more generally, a subset of `X x R` is quasi-compact exactly when
  its time projection is compact. Under that chosen convention, a nonzero
  `g in C_c(R)` has quasi-compact global support `X x supp(g)`.
- In Tu's convention, compact means quasi-compact and Hausdorff. For nonempty
  `K`, `X x K` is not Hausdorff. Under that convention the proposed nonzero
  global function does **not** have compact support, and the claimed
  `C_c^glob ~= C_c(R)` identification fails at the domain definition.

Muhly--Williams also separate local Hausdorffness from the open-cover
compactness issue by requiring compact Hausdorff neighborhoods. Their
Hausdorff-patch `C` space is not the globally continuous space in Paper 11.

Therefore Paper 11 must freeze the intended support predicate before any
source comparison. The safest owner name is
`C_qc^glob(G_{p,a}^{act})`, meaning global continuity plus open-cover
quasi-compact topological support. If the notation `C_c^glob` is retained, it
must explicitly declare that its superscripted author convention uses
open-cover quasi-compactness and is not Tu/Muhly--Williams `C_c`.

## 5. Author-defined fibre measure and completion feasibility

### 5.1 What can be tested directly

Each range fibre is homeomorphic to ordinary `R`, so Lebesgue measure is a
positive Radon measure **on that fibre**, has full fibre support, and is
translation invariant. If the global-function collapse is proved, the three
proposed tests reduce to ordinary facts for `g in C_c(R)`:

```text
x |-> integral_R g(t) dt                         is constant,
integral f(gamma eta) d lambda^{s(gamma)}(eta)
  = integral f(eta) d lambda^{r(gamma)}(eta),    by translation,
Phi(g)*Phi(h)=Phi(g*h),  Phi(g)^*=Phi(g^*).
```

That makes the construction feasible. It does not make the family a Haar
system in any retained published framework because those frameworks fail
before the fibre axioms are reached.

### 5.2 Exact group results available after `Phi` is proved

Dana P. Williams, *Crossed Products of C*-Algebras*, author draft v3.1
(6 September 2006), published as AMS Mathematical Surveys and Monographs 134
(2007), [authoritative author PDF](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf).
The exact retained local manifestation is
`papers/8-isotropy-trace/notes/sources/grp-williams-crossed-products-draft3.1.pdf`,
SHA-256
`3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2`.

- Example 1.80, printed p. 29 / PDF page 38: every character of `R` is
  `x |-> exp(-i x y)` for a unique `y in R`, and the dual topology is the
  ordinary topology.
- Proposition 3.1, printed p. 82 / PDF page 94: Fourier transform extends to
  an isomorphism `C^*(G) ~= C_0(Ghat)` for every locally compact abelian
  group.
- The discussion immediately before Theorem 7.13, printed pp. 198--199 / PDF
  pages 210--211, records that abelian groups are amenable; Theorem 7.13,
  printed p. 199 / PDF page 211, identifies universal and reduced norms for
  every action of an amenable group.

With the frozen Lebesgue measure and character convention, these source
results license the **group** statements

```text
Fourier(g)(xi) = integral_R g(t) exp(-i t xi) dt,
C^*(R) = C_r^*(R) ~= C_0(Rhat) ~= C_0(R).
```

They license Paper 11 only after a direct `*`-isomorphism
`Phi:C_c(R)->C_qc^glob(G_act)` is proved. The completion norms should be
defined by transport:

```text
||f||_{full,glob} := ||Phi^{-1}(f)||_{C^*(R)},
||f||_{red,glob}  := ||lambda_R(Phi^{-1}(f))||.
```

The equality is due to amenability of the **group `R`**, not to an unproved
amenability theorem for `G_{p,a}^{act}`.

## 6. Standard-circle proxy: exact theorem and ceiling

Put `G=R`, `H=L_p Z`, and `S=G/H` with its standard compact Hausdorff
topology. Williams, Theorem 4.30, printed p. 138 / PDF page 150, gives for the
left-translation homogeneous-space action and a suitable quasi-invariant
measure `mu`:

```text
C_0(G/H) rtimes G
  ~= C^*(H) tensor K(L^2(G/H,mu)).
```

Theorem 7.13 gives full/reduced equality because `R` is amenable. Since
`H=L_p Z` is discrete abelian,

```text
C^*(H) ~= C(Hhat) ~= C(T),
C(S_p^std) rtimes R
  ~= C(T) tensor K(L^2(S_p^std,mu)).
```

Buss--Holkar--Meyer Theorem 7.1, printed p. 23, independently licenses the
transformation-groupoid/crossed-product identification in this Hausdorff
proxy. Paper 8's exact groupoid audit additionally records Green's and the
Muhly--Renault--Williams transitive-groupoid routes.

This theorem is `APPLICABLE` only after Paper 11 freezes an equivariant
identification and matches its right-action sign to the cited left-translation
convention. The bare `K` in the protocol should be expanded to
`K(L^2(S_p^std,mu))`; full and reduced crossed products should be named before
using their equality. The pullback of the actual global algebra may be
computed as a unit-coordinate-constant `*`-subalgebra of the proxy
test-function algebra (and is expected to be proper), but continuity of the
set map alone proves neither density nor a norm-isometric embedding of
completions.

## 7. Bounded exact-precedent search

Search date/cutoff: **2026-08-14**. The bounded search used official arXiv,
publisher/monograph pages, author-hosted primary texts, and the exact Paper
8--10 manifests. Query families included:

```text
"rational Witt" groupoid convolution C*-algebra
"Rational Witt vectors" transformation groupoid convolution
Deninger E_f orbit groupoid C* algebra convolution
"finite-kernel" Deninger orbit convolution groupoid
"finite-kernel Deninger" convolution
"Deninger" "rational-Witt" groupoid
"prime packet" Deninger C*-algebra
"E_f" Deninger "groupoid"
```

No direct primary-source precedent was found for the exact conjunction

```text
rational-Witt finite-kernel actual orbit
+ inherited indiscrete topology
+ actual transformation-groupoid arrow topology
+ global-continuous versus Hausdorff-open-span convolution split
+ transported C^*(R) completion versus standard-circle crossed product.
```

The nearest arithmetic convolution precedent is Christopher Deninger,
“Dynamical systems for arithmetic schemes,”
[arXiv:1807.06400v4](https://arxiv.org/pdf/1807.06400v4), Section 11,
physical pp. 66--67, equations (104)--(110) and Lemma 11.1. Deninger constructs
a locally compact pro-discrete topological group `inverse-limit K^times`,
chooses Haar measure, and defines convolution on its globally continuous
compactly supported functions. The exact retained bytes are
`papers/8-isotropy-trace/notes/sources/topo-deninger-dynamical-systems-arithmetic-schemes-v4.pdf`,
SHA-256
`edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`.

That construction is load-bearing nearest prior art, but it is a convolution
algebra of a different locally compact topological **group**. It neither
defines the Paper-11 time-orbit transformation groupoid nor computes an
indiscrete arrow topology, a zero Hausdorff-open span, or either transported
completion. Generic “indiscrete groupoid” search hits that use “indiscrete”
for the codiscrete/pair groupoid rather than for the topology were excluded as
different objects.

Accordingly the only licensed novelty wording is:

> No direct precedent for the exact rational-Witt actual-orbit
> convention-split package was found within the bounded search completed on
> 2026-08-14.

This is `SUPPORTED_WITHIN_SEARCH`, not “first,” “unprecedented,” or proof of
global nonexistence. Deninger's Section 11 and the generic indiscrete-space,
group-convolution, and homogeneous-space crossed-product facts must be cited
as prior art.

## 8. Findings and mandatory amendments

### M1 — freeze quasi-compact support; “compact” currently changes the algebra

**Required amendment:** replace the unqualified support predicate by
open-cover quasi-compact support and preferably rename the owner
`C_qc^glob`. Record separately that the actual arrow space is locally
quasi-compact in that chosen sense but is not locally compact in Tu's sense
and has no compact Hausdorff neighborhood. State the time-projection criterion
for quasi-compact subsets. Never cite a locally compact groupoid theorem from
this property.

### M2 — rename the actual measure family and its operators

**Required amendment:** replace “Haar system in the explicitly frozen sense”
by a unique author record such as
`ACT-GLOB-FIBRE-MEASURE-FAMILY`. Freeze its complete fields: positive Radon
measure on each usual Hausdorff range fibre, full fibre support, the exact
left-invariance equation, and continuity/selected support of the integral map
tested only on `C_qc^glob`. Require direct well-definedness and closure of
convolution. The separate literature ledger must continue to say
`PUBLISHED-HAAR-SYSTEM-APPLICABILITY = NOT_APPLICABLE`.

Likewise replace unqualified “regular representation at every unit” by
`ACT-GLOB-FIBRE-CONVOLUTION-OPERATOR`. Freeze

```text
G_x=s^{-1}(x)={(x dot (-t),t):t in R},
lambda_x=(inversion)_*lambda^x,
H_x=L^2(G_x,lambda_x),
[Lambda_x^glob(f)xi](gamma)
  = integral_{G_x} f(gamma eta^{-1})xi(eta)d lambda_x(eta).
```

Only after the explicit unitary to `L^2(R)` is proved may this operator supply
the author-defined reduced norm.

### M3 — make full/reduced ownership syntactic, not contextual

**Required amendment:** insert the two transported norm equations in Section
3.3 and state that full/reduced equality is a theorem about the amenable group
`R`. Forbid “groupoid amenability,” “the regular representation of the actual
groupoid,” and `C^*(G_act)` unless a later exact framework is separately
found. In P11-6 store both
`HOPEN-SPAN-VALUE=0` and
`STANDARD-FRAMEWORK-APPLICABILITY=NOT_APPLICABLE`; do not identify them.

### m1 — fully type the proxy theorem

Before Phase 2/3, freeze the signed equivariant parameter used to compare
right and left actions, write `K(L^2(S_p^std,mu))`, and name full and reduced
proxy crossed products separately. State that the dense-algebra pullback does
not itself transport completion norms.

### Mandatory novelty/source carry-forward

The amendment and eventual manuscript must acknowledge Deninger Section 11 as
the nearest arithmetic convolution prior, cite Tu and Muhly--Williams for the
genuine Hausdorff-open convention, and use only the dated
`SUPPORTED_WITHIN_SEARCH` wording for the exact package.

## 9. Retention and integrity result

No new PDF was retained. Tu, Muhly--Williams, Exel, and
Buss--Holkar--Meyer were screened through their official/arXiv full-text
endpoints and are recorded here with exact physical/printed locators. The two
load-bearing long texts already present in the repository were reused with
their existing hashes:

| Reused local source | SHA-256 | Result |
|---|---|---|
| Deninger arXiv v4 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | exact bytes match inherited manifest |
| Williams draft v3.1 | `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | exact bytes match inherited groupoid audit |

No streamed source supplies public-sync permission merely by being
downloadable. If any is retained later, it must receive the ARS preflight,
exact SHA-256, manifestation, physical-page locator, and redistribution
classification required by the protocol.

## 10. Final gate

**REVISE, but not for mathematical infeasibility.** The direct global
quasi-compact-support construction and the standard-circle contrast have a
sound source path. The active bytes are unsafe because “compact,” “Haar
system,” “regular representation,” and “full/reduced” can presently be read
as terms from frameworks whose hypotheses the actual object violates. Close
M1--M3 and m1 in a versioned amendment, independently re-lock the exact bytes,
and only then begin the source-retention or proof phases.

## 11. Amended-v1 exact-byte source / terminology re-lock

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Re-lock scope: **narrow closure audit of M1--M3 and m1; no new search, source,
PDF, proof, or Route work**  
Verdict: **PASS — C=0, M=0, m=0**

### 11.1 Exact amended tuple

The four files read for this re-lock match the tuple submitted by the
versioned amendment exactly:

| Amended-v1 input | SHA-256 | Match |
|---|---|---|
| `notes/research_protocol.md` | `bc40e307746c1d05808d8288dba0b0a315c30e60d7983989ca42ebe913ecb922` | exact |
| `notes/candidate_lock.md` | `a82a96957f5d58b0925e96395ea2994acb9dece9e24f60f286b7ea714cdb7c3e` | exact |
| `notes/pipeline_state.md` | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` | exact |
| `notes/phase1_design_amendment.md` | `7d2c2c7eb041a530ff4da6f7090d85053b067243d7a2ab445b4b4cba9cc2dc64` | exact |

The pre-amendment source-feasibility report immediately above had SHA-256
`8dd0b3cae55a94b7f9140d6ee5bf49dacbc735a92743c02608815493ed562e37`.
This section appends a re-lock decision; it does not erase or retrospectively
rewrite the initial `REVISE` findings.

### 11.2 Closure matrix

| Initial finding | Exact amended evidence | Re-lock result |
|---|---|---|
| `M1`: unqualified compact support could change the global algebra | Protocol lines 104--124 define open-cover quasi-compactness, ambient closure support, and `C_qc^glob`; lines 126--129 split the local predicates and forbid unqualified `locally compact`; lines 279--283 register the time-projection criterion and both quasi-compact/Hausdorff-open tests. Candidate lines 45--47 and 81--85 serialize the same owner and raw HOpen distinction. | **CLOSED** |
| `M2`: actual fibre family and unit operators could be mistaken for published Haar/regular records | Protocol lines 137--155 register the uniquely named author-owned `GLOB-FIBRE-FAMILY`, its range-fibre Radon/full-support domain, exact test algebra, integral continuity, left-invariance equation, and a separate standard-framework applicability gate. Lines 198--216 freeze `G_x`, inversion-pushed `lambda_x`, `H_x`, `Ind_x`, and the exact unitary reduction obligation. Candidate lines 49--54 explicitly classify both records as author-defined. The integral-map support issue no longer imports a standard Haar axiom: on the frozen quasi-compact indiscrete unit, the registered continuity condition forces a constant scalar map and hence empty or whole-unit quasi-compact support; this remains a direct verification consequence, not source credit. | **CLOSED** |
| `M3`: full/reduced ownership and HOpen applicability were only contextual | Protocol lines 190--228 define the source-fibre reduced norm and the transported group-full norm syntactically, freeze the Fourier sign, and attribute equality only to amenability of the group `R`; lines 230--233 forbid actual standard groupoid-completion notation. Lines 165--186 place the HOpen span in a raw-function diagnostic owner, while lines 335--342 separately require per-framework `APPLICABLE` / `NOT_APPLICABLE` / `DIAGNOSTIC_ONLY` decisions. Hypothesis H3 registers the zero-value claim as a falsifiable theorem target rather than equating it with framework applicability. Candidate lines 56--64 and 89--96 preserve the same owner split. | **CLOSED** |
| `m1`: proxy action, theorem strength, and completion map were under-typed | Protocol lines 244--255 freeze the `+t` signed right action, set-groupoid map `J`, both continuity directions, contravariant map `I`, and preconditions for a `*`-monomorphism. Lines 257--270 type only a source-gated full-proxy candidate with `K(L^2(S_p^std,mu))` and separate dense/full/reduced/Morita/stable/actual-isomorphism claims. Lines 344--351 require an independent boundedness/isometry theorem before any completion extension. Candidate lines 99--109 repeat the sign/map owner and explicitly include no completion map. | **CLOSED** |

### 11.3 Source-ceiling conservation

The amended tuple preserves every load-bearing ceiling of the initial source
review:

1. `C_qc^glob` is author-defined and is not Tu/Muhly--Williams `C_c(G)`.
2. `GLOB-FIBRE-FAMILY` and the named `Ind_x` record do not claim that a
   retained published Haar/regular-representation framework applies to the
   actual non-locally-Hausdorff object.
3. The HOpen diagnostic value and standard-framework applicability are two
   independently tested fields. A zero diagnostic cannot become “the standard
   groupoid `C*`-algebra is zero.”
4. The actual completion names remain transported author objects; only the
   group `R` may own the amenability and Fourier theorems.
5. The standard-circle display remains marked `?~=` and source-gated. It is
   not promoted to the actual object, and the dense-algebra pullback does not
   automatically extend to completions.
6. Novelty remains capped at dated `SUPPORTED_WITHIN_SEARCH`; the amendment
   neither reruns nor enlarges the bounded search recorded above.

The remaining occurrences of “Haar system,” “regular representation,”
“locally compact,” and actual `C^*(G)` notation are all negative rules,
source-audit subjects, explicitly author-qualified records, ordinary
Hausdorff-fibre/group/proxy terms, or forbidden-notation examples. No residual
terminology splice was found on the exact amended tuple.

### 11.4 Re-lock decision

```text
phase1_source_terminology_relock: PASS
critical: 0
major: 0
minor: 0
tuple_match: true
new_source_search: false
active_lock_edited: false
phase2_clearance_from_this_reviewer: true
global_phase2_clearance: requires the other two independent amended-byte PASS re-locks
```

This PASS certifies only that amended v1 closes the initial source/terminology
findings at the design level. It proves no `P11-*` theorem, does not itself
certify `C_c^HOp=0`, does not turn `GLOB-FIBRE-FAMILY` into a published Haar
system, and does not authorize any actual-groupoid `C*` notation.

## 12. Final mechanical-v1.1 terminology / source regression re-lock

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Re-lock scope: **exact-byte regression limited to the added definitions of
`U_x`, `mu_p`, and `alpha_t`; no new search, retained source, proof, or Route
work**  
Verdict: **PASS — C=0, M=0, m=0**

### 12.1 Exact reviewed bundle

The files match the final mechanical-v1.1 bundle submitted for this review:

| Reviewed file | SHA-256 | Match |
|---|---|---|
| `notes/research_protocol.md` | `0f500ca7e10596024a883a027e63203f7f21ffade3d5de59eb367eb2090fb7d5` | exact |
| `notes/candidate_lock.md` | `6ddbea5f4e104ac3bd3ab99fa561b9f6c632e8cd4e86d34371628ecb591526ed` | exact |
| `notes/pipeline_state.md` | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` | exact |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | exact |

The source-feasibility report, including the preceding amended-v1 re-lock but
before this section was appended, had SHA-256
`c29376bfde9ebcdf2cb82617f5f9aa625fec0ca39b28aef5988f613ff089f720`.
This regression appends a new decision without modifying either prior review.

### 12.2 Three-definition regression

| Mechanical definition | Exact-byte terminology / source check | Result |
|---|---|---|
| `(U_x xi)(t)=xi(vartheta_x(t))` | Protocol lines 201--208 now type `G_x`, `lambda_x`, `vartheta_x`, `H_x`, `U_x`, `Ind_x`, and the reduced norm in one author-owned record. Lines 211--216 still require `P11-5` to prove that `vartheta_x` is measure preserving, that the operators are bounded `*`-representations, and that conjugation by `U_x` gives group convolution. Thus the formula closes the missing signature but imports no published regular-representation theorem and does not pre-prove unitarity. Candidate lines 89--95 preserve the author-defined/transported-norm boundary. | **NO DRIFT** |
| `mu_p` is normalized Haar probability on `S_p^std` | Protocol lines 241--246 place `mu_p` solely on the ordinary compact Hausdorff circle `R/L_p Z`; line 271 uses it only to type `K(L^2(S_p^std,mu_p))`. Candidate lines 102--112 preserve the same proxy owner. “Haar probability” is therefore ordinary compact-group proxy terminology, not a renaming of `GLOB-FIBRE-FAMILY` and not a Haar-system claim for the actual indiscrete groupoid. | **NO DRIFT** |
| `alpha_t(h)([r])=h([r+t])` | Protocol lines 245--254 place this formula under the already frozen signed right action `[r] dot t=[r+t]` and expressly require any retained source using inverse pullback to be translated rather than silently changing sign. The display at lines 267--277 remains a `?~=` Phase-2 source-gated proxy candidate, with full/reduced, Morita, stable, and actual-isomorphism claims still separated. Candidate lines 102--112 repeat the same convention and prohibit an unsourced completion map. | **NO DRIFT** |

Calling the coordinate map “unitary” in the candidate lock is read together
with the protocol's explicit `P11-5` proof obligation; it is a theorem target,
not a source-backed or completed proof claim. Likewise, naming `mu_p` and
`alpha_t` makes the proxy expression well typed but does not activate the
retained crossed-product theorem. Exact comparison with the retained source's
action convention remains Phase-2 work.

### 12.3 Source-ceiling conservation

No source was added, removed, or reinterpreted in v1.1. The exact primary
locators and applicability classifications in Sections 3--6 above remain the
source ledger: Tu and Muhly--Williams license a Hausdorff-open-span convention
only under their stated locally Hausdorff/local-compactness hypotheses;
Buss--Holkar--Meyer and the Williams/Green records concern the ordinary
Hausdorff proxy; the group amenability and Fourier results belong to `R`; and
none licenses a standard full or reduced groupoid completion for the actual
non-locally-Hausdorff owner.

Consequently all prior ceilings are conserved:

1. `GLOB-FIBRE-FAMILY`, `Ind_x`, and both global completions remain
   author-defined records.
2. `HOPEN-SPAN-VALUE` and `STANDARD-FRAMEWORK-APPLICABILITY` remain separate;
   neither new definition touches them.
3. `mu_p`, `alpha_t`, the crossed-product candidate, and its compact-operator
   Hilbert space remain proxy-only and convey no actual-topology credit.
4. The proxy display is still conjectural/source-gated, and the dense
   pullback still carries no automatic boundedness, isometry, or completion
   extension.
5. Novelty remains limited to the dated `SUPPORTED_WITHIN_SEARCH` result in
   Section 7; this regression neither refreshes nor broadens that search.

### 12.4 Final regression decision

```text
phase1_source_terminology_regression_relock: PASS
critical: 0
major: 0
minor: 0
tuple_match: true
regression_scope: U_x/mu_p/alpha_t only
proxy_source_convention_drift: false
new_source_search: false
retained_source_change: false
active_lock_edited: false
phase2_clearance_from_this_reviewer: true
global_phase2_clearance: requires the other final amended-byte PASS re-locks
```

This PASS is a source/terminology regression result only. It proves no
`P11-*` target, certifies no proxy isomorphism, and does not authorize standard
actual-groupoid `C_c` or `C*` notation.
