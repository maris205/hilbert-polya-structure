# Paper 12 Phase-2 integrated independent final review

Review date: **2026-08-15 (Asia/Shanghai)**  
Decision: **PASS — PHASE 3 PROOFS AND CONTROLS MAY START**  
Findings: **C0 / M0 / m0**

This is the independent final gate for the Phase-2 source, convention,
category/owner, packet, and bounded-novelty work. It proves no `P12-*`
target, grants no Route coordinate, and authorizes neither manuscript drafting
nor release. The clearance below is limited to direct Phase-3 proofs and the
preregistered deterministic controls on the exact active lock tuple.

## 1. Exact-byte review binding

The active Phase-1 authorities and every final Phase-2 artifact were read in
full and independently rehashed at these bytes:

| Artifact | SHA-256 | Review result |
|---|---|---|
| `notes/phase1_final_gate.md` | `fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c` | exact final Phase-1 gate |
| `notes/phase1_status_relock.md` | `a7a9875c810ea98f5a5563c8f243612b006c20f397aaa8ebae533d8b8c6c61d6` | exact status-only inverse-reconstruction lock |
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` | active protocol; read in full |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` | active owner/category lock; read in full |
| `notes/pipeline_state.md` | `9a3c2dbf85a4f2f9a8ebe82a6b8ad82b79379bb7bd5245bbe03e9a39a2200e05` | Phase-2-only authorization confirmed |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` | final frozen source audit; read in full |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` | final frozen manifestation/locator manifest; read in full |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` | final ten-object checksum ledger; rerun |
| `notes/phase2_category_owner_audit.md` | `8fad79f121439145e0ac3cac7ca67e82f3e2ad6af86da5b0f001e92da30e1d62` | category, owner, packet, and applicability audit; read in full |
| `notes/phase2_novelty_search.md` | `c4584862824dbaadec9945fb85defd6d11ee7822849471b075ff4d90d57ca1bd` | bounded novelty search; read in full |

The inherited local dependencies named by the Phase-2 reports were also
rehashed and matched:

| Dependency | SHA-256 |
|---|---|
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` |
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| Paper 11 `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` |
| Paper 11 `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` |

A pre-final source tuple was not accepted: its five PDF entries matched but
its five sidecar entries did not. The source lane regenerated and explicitly
froze the three final bytes listed above. This review binds only that final
tuple; the resolved transient mismatch is not an open finding.

## 2. Checksum and ARS PDF-read preflight rerun

Running `sha256sum -c coh-sources.sha256` in `notes/sources/` returned `OK`
for all five retained PDFs and all five same-stem sidecars:

```text
checksum entries checked: 10
checksum entries OK:      10
checksum failures:         0
```

The unmodified ARS `pdf_read_preflight/1.0.0` script was then rerun from the
five local PDFs in an independent isolated `pypdf` environment, without
overwriting the frozen sidecars. PDF hashes, all three page counts, verdicts,
and warning arrays matched the manifest:

| Source | PDF SHA-256 | Declared / enumerated / reader | Independent rerun |
|---|---|---:|---|
| Blanco--Uribe--Waldorf 2023 | `3d46127491c66f3ec0568fccb8df60b9e4465c4f4719b712fc3e23ca48f9e143` | 52 / 52 / 52 | `PASS`, warnings `[]` |
| Deninger arXiv v4 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | 119 / 119 / 119 | `PASS`, warnings `[]` |
| Farsi--Huang--Kumjian--Packer 2022 | `194583c289d3c08463a32221a8e6561292d48d5357021db370237c71de697083` | 32 / 32 / 32 | `PASS`, warnings `[]` |
| Fuchssteiner--Wockel arXiv v2 | `194483f7c90cb752b95f86b2557572bb8deb135032b749503347d7592d752f42` | 13 / 13 / 13 | `PASS`, warnings `[]` |
| Mackenzie 1978 | `b94ed23e24a13047037dbffc5c84513df1cd8931c4391670e05c1f5904f66f83` | 25 / 25 / 25 | `PASS`, warnings `[]` |

The local source PDFs remain evidence caches only. This gate does not grant
permission to stage, publish, or attach them.

## 3. Independent locator and applicability check

The load-bearing passages were read directly from the retained PDFs rather
than inferred from the three Phase-2 reports.

| Exact local locator | Independently verified content | Licensed Paper-12 use and ceiling |
|---|---|---|
| Deninger physical/printed pp. 32--33, Eqs. (35), (38), (39) | finite-kernel exponent parametrization and `Q_{>0}`-equivariant **set** bijections; exact multiplicative stabilizer calculation | source set/stabilizer input only; no topology transport |
| Deninger physical/printed p. 38, Section 6 | suspension, right `Q_{>0}` action, right `R_{>0}` flow, additive `phi^t([P,u])=[P,ue^t]`, packet definition, and `Gamma^E=Gamma` when `E_f subset E` | exact action/clock/packet input; taking the Paper-9 owner `E=E_f` closes the same-owner packet step |
| Deninger physical/printed p. 39, Theorem 6.1 | **every point** in `Gamma^E_{x_0}` has isotropy `N(x_0)^Z`; packets correspond to finite-residue-field points and orbit length is `log N(x_0)` | every-unit packet gate only; no groupoid, topology, or cohomology theorem |
| Mackenzie physical pp. 1, 3--4, 6, 9, 14--15, 25 / printed pp. 277, 279--280, 282, 285, 290--291, 301 | Hausdorff/transitive/locally trivial/locally compact domain, locally convex vector-bundle modules, trivial real product module, full continuous nonhomogeneous composable-tuple cochains, and normalized-cochain postponement | full/unnormalized formula and module comparator; rigid theory is `NOT_APPLICABLE` to the nontrivial inherited-indiscrete owner and arbitrary `T0` coefficients |
| Blanco--Uribe--Waldorf physical pp. 4--7 / printed pp. 1472--1475, Sections 2.3--2.4 | `Topab` is compactly generated, locally contractible, Hausdorff; a simplicial-paracompact full `Map(X_*,A)` complex is called continuous-cochain cohomology; the one-object group nerve has the displayed full inhomogeneous differential; Lemma 2.5 identifies degree one with continuous homomorphisms | exact `(R,R)` comparison and conditional simplicial-space formula match; no citation-based extension to arbitrary `T0` coefficients or an unqualified actual-groupoid theory |
| Farsi--Huang--Kumjian--Packer physical p. 12 / printed p. 3336, Definition 3.7 | a continuous `H`-valued groupoid 1-cocycle is a continuous groupoid homomorphism; coboundaries have range-minus-source form | exact degree-one terminology for `H=R`; sign-opposite coboundary formula has the same image after negating the unit function; no all-degree precedent |
| Fuchssteiner--Wockel physical/author pp. 2--3 and p. 7, Corollary II.8 | globally continuous homogeneous group cochains and their comparison with locally continuous cochains for loop-contractible coefficients | comparison one-object group only; no actual action-groupoid theorem |

The reports therefore make the necessary distinction between an exact
formula comparator and a theorem whose hypotheses cover the frozen owner.
The generic family must retain the author-defined `C_cnv/H_cnv` notation.
Any later reference to Blanco--Uribe--Waldorf on the actual nerve remains
conditional on an explicit source-convention and nerve-level hypothesis
check; it cannot replace the direct `P12-1`--`P12-3` proofs.

## 4. Fixed-prime packet and owner-chain gate

The required same-object chain is complete and non-spliced:

```text
Deninger p. 38:
  the exact E_f packet and restricted right flow with additive +t clock

Deninger p. 39, Theorem 6.1:
  every packet unit has multiplicative stabilizer N((p))^Z = p^Z

the source exponential time coordinate:
  exp^{-1}(p^Z) = (log p)Z

Paper 9 exact E_f owner:
  Gamma_p is the same packet, with its actual inherited indiscrete topology
```

Thus all three preregistered source checks pass:

| Packet check | Verdict |
|---|---|
| same restricted Deninger action | `PASS` |
| same normalized additive clock `c(x,t)=t` | `PASS` |
| every packet unit has stabilizer `(log p)Z` | `PASS` |

The Phase-2 source branch is therefore exactly:

```text
source_gate: PACKET_COROLLARY_ELIGIBLE
ORBIT_ONLY: false
packet_claim_proved: false
global_or_cross_prime_promotion: forbidden
```

Eligibility is not the corollary's proof. Phase 3 must still prove that the
Paper-12 cohomology-class restriction is representative-independent and has
the stated image on the author-defined groupoid.

The owner split is intact: Deninger owns only the source suspension,
fixed-prime packet, flow, stabilizer, and logarithmic clock; Paper 9 owns the
actual inherited topology; Papers 11--12 own the range-first transformation
groupoid allocation; and Paper 12 alone attempts the nerve complex, marked
restriction, morphism categories, and quotient functor. `G^global` remains
excluded.

## 5. Category, period, and quotient terminology

The three morphism types are correctly separated:

```text
C_str:    c' o F = c                    strict preservation
C_scale:  c' o F = alpha c, alpha > 0  positive scaled covariance
C_un:     no equation involving c       unmarked isomorphism
```

The only correctly directed covariance statement is

```text
Per_(F_0(x))([c']) = alpha Per_x([c]).
```

Strict preservation is the `alpha=1` case. The weaker-category statement is
existential non-descent, not universal loss. The unequal-period dilation
controls show that `C_scale` and `C_un` can connect different generators;
the orientation-reversing control preserves `LZ` while sending `c` to `-c`,
so subgroup equality does not characterize strictness.

The restriction map is correctly typed first on cocycles. Only after direct
proof that coboundaries vanish on isotropy may `Per_x([b])` be treated as a
cohomology-class image. No audited source supplies that marked package as a
theorem.

The standard object `(R/H,[0])` uses the usual Hausdorff quotient topology
and remains a proxy. The proposed `S` is a normalized strict functor only.
For scaling, `[t]_H |-> [alpha t]_(alpha H)` is semilinear relative to the
value-group automorphism and is not a strict `R`-equivariant target morphism
unless `alpha=1`. For a nontrivial actual inherited-indiscrete orbit, the
chart is continuous only from the standard quotient to the actual space; its
inverse is not continuous. No actual/proxy topology identification remains.

## 6. Bounded novelty and standalone conjunction

The novelty report records the exact nine query families, cutoff
`2026-08-15`, `last_searched_at=2026-08-15T03:48:00+08:00`, required
endpoint attempts, parser translations, degradation states, include/exclude
reasons, seeded comparators, and one-hop backward/forward chaining. It
screened 134 displayed result slots across the interfaces that returned
records and did not convert the OpenAlex, Semantic Scholar, MathSciNet, or
later Google-Scholar failures into zero results.

Its direct-precedent test is the preregistered conjunction:

```text
D1 same owner/domain
AND D2 full locked unnormalized nerve complex
AND D3 marked isotropy image
AND D4 strict/scaled/unmarked boundary and normalized quotient package.
```

No included source passed all four conditions. The nearest sources supply
separate ingredients: Mackenzie supplies a stricter-domain groupoid theory;
Blanco--Uribe--Waldorf the nearest continuous-nerve convention; Farsi et al.
the exact degree-one terminology; graded-groupoid reconstruction literature
a strict-preservation analogue; and Deninger the arithmetic owner only.

The defensible novelty verdict is therefore exactly
`SUPPORTED_WITHIN_SEARCH`, with `DIRECT_PRECEDENT_FOUND=false`. It is not a
global absence, priority, or “first” claim. The bounded search leg does not
force `NOTE_OR_MERGE`, but it also does not grant `STANDALONE_PASS`.
Standalone status remains conjunctive: if Phase 3 yields only Paper-11
factorization plus routine nerve formalism and Deninger's already-owned
stabilizer, or if the packet proof fails and produces `ORBIT_ONLY`, the
frozen result is `NOTE_OR_MERGE`.

## 7. Public-source boundary and final authorization

`notes/sources/.gitignore` excludes `*.pdf` while retaining sidecars. This
workspace has no Git metadata, so neither the source reports nor this review
claim an index/staging pass. A later public-sync dry run must enumerate the
payload and mechanically show zero retained source PDFs. Scholarly citations
must use canonical DOI, publisher, journal, arXiv, or author endpoints, never
local paths or audit hashes.

No contradiction remains among the exact source, category/owner, packet,
novelty, and active-lock records. No source locator, applicability label,
owner assignment, category equation, quotient direction, bounded novelty
classification, or standalone condition requires amendment.

```text
phase2_integrated_final_review: PASS
critical_open: 0
major_open: 0
minor_open: 0
source_checksum: 10/10 OK
ars_pdf_preflight_rerun: 5/5 PASS; 0 warnings
packet_source_gate: PACKET_COROLLARY_ELIGIBLE
orbit_only: false
generic_named_theory_status: AUTHOR_DEFINED_C_CNV_H_CNV
mackenzie_actual_applicability: NOT_APPLICABLE
buw_actual_applicability: CONDITIONAL_COMPARATOR_ONLY
fhkp_actual_applicability: DEGREE_ONE_R_ONLY
strict_scaled_unmarked_split: LOCKED_NO_DRIFT
standard_quotient_status: HAUSDORFF_PROXY_ONLY
novelty_ceiling: SUPPORTED_WITHIN_SEARCH
direct_precedent_found: false
standalone_release_status: PENDING_PHASE3_AND_DOWNSTREAM_GATES
phase3_proofs_and_controls_may_start: YES
route_evaluation_authorized: false
route_b_yaml_authorized: false
manuscript_or_release_authorized: false
active_lock_edited: false
```

**Final verdict: PASS (`C0/M0/m0`).** Phase 3 may begin only with direct
proofs of `P12-1`--`P12-8` and the frozen `P12-9` controls. The packet
corollary remains an eligible target rather than an established theorem;
Route, manuscript, and release work remain blocked.
