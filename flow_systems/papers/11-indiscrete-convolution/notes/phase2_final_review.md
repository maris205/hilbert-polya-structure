# Paper 11 Phase-2 integrated independent final review

Review date: **2026-08-15 (Asia/Shanghai)**  
Decision: **PASS — PHASE 3 PROOFS AND CONTROLS MAY START**  
Findings: **C0 / M0 / m0**

This is the independent final gate for the Phase-2 source, convention,
owner/proxy, and bounded-novelty work. It proves no `P11-*` target, supplies
no Route verdict, writes no manuscript claim, and grants no standard
actual-groupoid `C*` notation. Phase-3 clearance below is limited to proofs
and deterministic controls under the exact active Phase-1 tuple.

## 1. Exact-byte review binding

The complete framework audit, framework manifest, checksum ledger,
owner/proxy audit, novelty search, active Phase-1 tuple, and final Phase-1
gate were read and cross-checked at these bytes:

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` | exact requested byte; read in full |
| `notes/sources/framework_source_manifest.md` | `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f` | exact requested byte; read in full |
| `notes/sources/framework_sources.sha256` | `057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f` | exact requested byte; ledger rerun |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` | exact requested byte; read in full |
| `notes/phase2_novelty_search.md` | `024398a3575cf41a7f33c6950dc1c8de8a8d5f4ec81675f8760ce7c7a87ac24e` | exact requested byte; read in full |
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` | active status byte; read in full |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` | active status byte; read in full |
| `notes/pipeline_state.md` | `d4801ffbe0785e3023c55245c21e7ab9c2ea08bf78d524ea86dfe7d54305bff1` | active status byte; read in full |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | active amendment byte; read in full |
| `notes/phase1_final_gate.md` | `ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f` | exact final-gate byte; read in full |

The active status tuple agrees with Section 3 of the Phase-1 final gate. The
pre-status tuple recorded in that gate is historical evidence only and was
not substituted for the active bytes.

The inherited audit hashes named by the owner/proxy report were also
recomputed and matched, including Paper 8's groupoid source audit
`39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42`,
Paper 9's source/proof audits
`20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` /
`c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8`,
and Paper 10's domain/proof audits
`8dbc4e6487d342bcf352a4b0161bc1c4f17800d07556a3d11b49ce900b3aa582` /
`efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a`.
No owner was silently changed by the integration.

## 2. Checksum and ARS preflight rerun

Running `sha256sum -c framework_sources.sha256` in `notes/sources/`
returned `OK` for all five PDFs and all five same-stem preflight sidecars:

```text
checksum entries checked: 10
checksum entries OK:      10
checksum failures:         0
```

ARS `pdf_read_preflight/1.0.0` was then rerun from the retained local PDFs,
without replacing the frozen sidecars. The recomputed hashes, declared page
counts, recursively enumerated page counts, reader page counts, verdicts, and
warning arrays match the frozen records:

| Source | PDF SHA-256 | Page counts (declared/enumerated/reader) | Rerun |
|---|---|---:|---|
| BHM v2 | `8be7896ed1aab1138b8ccf067ebfbba0f8b7d8a1dc8713fbf6c2f173ffe647e6` | 30 / 30 / 30 | `PASS`, warnings `[]` |
| Exel v3 | `01b1ac9a6f98444438c654b2e4d8b69ff6058e15c02ae6704e6d254f457c3a99` | 12 / 12 / 12 | `PASS`, warnings `[]` |
| Muhly--Williams 2008 | `7a7c16f132f1df35f8bf304206e998796834cd23a31836dd4e15108f91806f20` | 87 / 87 / 87 | `PASS`, warnings `[]` |
| Tu 2004 | `ff88e322eee65d2d6dd083697c82febb3759268f9b36083264a3e20b6e586897` | 34 / 34 / 34 | `PASS`, warnings `[]` |
| Williams draft 3.1 | `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | 540 / 540 / 540 | `PASS`, warnings `[]` |

The Williams bytes remain identical to Paper 8's independently retained
copy. The `*.pdf` local-only retention boundary remains intact; no source PDF
is authorized for public synchronization by this review.

## 3. Exact source locators, terminology, and applicability

The retained locator index agrees with the exact local manifestations:

| Source locator | Verified content | Integrated use |
|---|---|---|
| Tu physical p. 3 / printed p. 567, Definition 1.1 | `quasi-compact` is the open-cover property; `compact` adds Hausdorffness; Tu-local compactness implies local Hausdorffness | terminology comparator; actual framework `NOT_APPLICABLE` |
| Tu physical p. 17 / printed p. 581, Section 4.1; physical p. 19 / printed p. 583, Definition 4.6 | raw zero-extension span from Hausdorff opens, followed by the locally compact groupoid/Haar-system domain | HOpen convention analogue only; no actual Haar/completion credit |
| Muhly--Williams physical/printed pp. 3--7 and 21--23 | locally Hausdorff/locally compact standing domain, Hausdorff units, compact Hausdorff arrow neighborhoods, raw patch span, Haar system, and patch convolution | accepted HOpen practice; actual framework `NOT_APPLICABLE` |
| Exel physical/printed p. 1 | the non-Hausdorff-arrow étale setting still requires a locally compact Hausdorff unit and local-homeomorphism range/source | actual and continuous-`R` proxy use `NOT_APPLICABLE` |
| BHM physical/printed pp. 1--2 and p. 23, Theorem 7.1 | Hausdorff groupoid standing hypothesis and the full transformation-groupoid/full crossed-product bridge | `NOT_APPLICABLE` actual; `APPLICABLE_PROXY_ONLY` after the explicit convention map |
| Williams physical p. 38 / printed p. 26, Example 1.80 | character/Fourier sign `exp(-it xi)` | transported group-`R` Fourier convention only |
| Williams physical p. 54 / printed p. 42, (2.4)--(2.5) | a left point action induces the inverse-pullback coefficient action | exact proxy sign dictionary |
| Williams physical p. 94 / printed p. 82, Proposition 3.1 | `C^*(G) ~= C_0(Ghat)` for LCA groups | `C^*(R) ~= C_0(R)` after transport only |
| Williams physical p. 150 / printed p. 138, (4.63) and Theorem 4.30 | quotient-measure normalization and the full homogeneous-space tensor-product isomorphism | concrete unstabilized full proxy theorem |
| Williams physical p. 210 / printed p. 198 and physical p. 211 / printed p. 199 | reduced group norm/left regular representation; abelian and amenable full--reduced equalities | group `R` and proxy crossed-product results, not actual groupoid results |

The historical Williams “printed p. 29” locator is correctly superseded by
physical p. 38 / printed p. 26. No locator correction changes a theorem
strength or owner.

The terminology/applicability split is internally exact:

```text
C_c^HOp(G_act):
  source relation = diagnostic analogue of a published raw patch convention
  source-framework applicability = NOT_APPLICABLE
  value 0 = direct P11-1/P11-6 proof obligation, not a source theorem

GLOB-FIBRE-FAMILY and Ind_x:
  owner = AUTHOR_DEFINED_DIRECT
  published Haar/regular terminology = forbidden on the present evidence

C^full_glob and C^red_glob:
  owner = author-defined transported completions
  activation = only after Phi and the exact U_x Ind_x U_x^{-1} calculation
  notation C^*(G_act), C_r^*(G_act) = unauthorized

G_std:
  owner = ordinary Hausdorff-circle proxy
  BHM/Williams applicability = proxy only
  actual-topology or actual-completion credit = forbidden
```

Thus `HOPEN-SPAN-VALUE=0` must never be paraphrased as “the standard
groupoid algebra is zero.” The source audits correctly keep the direct value,
published-framework non-applicability, author fibre record, and transported
group completion as four different records.

## 4. Right-to-left sign and `mu_p` regression

The frozen right action and range-first arrows are

```text
[r] dot t=[r+t],   r([r],t)=[r],   s([r],t)=[r+t].
```

Converting to the BHM left action by `ell_t([r])=[r-t]` gives the exact arrow
map

```text
K([r],t)=(t,[r+t]).
```

The BHM arrow has source `[r+t]` and range
`ell_t([r+t])=[r]`, so the direction is correct. Williams's coefficient
formula for a left point action is inverse pullback; hence

```text
a_t(h)([r])=h(ell_{-t}([r]))=h([r+t])=alpha_t(h)([r]).
```

There is no hidden sign reversal. To reach Williams's ordinary left
translation `m_t([r])=[r+t]`, coordinate inversion
`kappa([r])=[-r]` gives `Q alpha_t Q^{-1}=lt_t`, where
`Q(h)=h o kappa` and `lt_t(h)([r])=h([r-t])`. This is an explicit proxy
conjugacy, not a change to the frozen actual right action.

For `G=R`, `H=L_p Z`, Lebesgue Haar on `G`, counting Haar on `H`, and
`rho=1/L_p`, Williams (4.63) becomes

```text
integral_R f(t) dt/L_p
  = integral_(R/L_p Z) sum_(n in Z) f(r+nL_p) dmu_p([r]).
```

This is exactly normalized Haar probability
`dmu_p=dr/L_p` on a fundamental interval. Therefore the frozen
`L^2(S_p^std,mu_p)` is admissible for Williams 4.30. The audit does not
silently substitute length Haar, and no modular correction appears because
the groups in this dictionary are unimodular.

## 5. Theorem-strength ledger

The integrated strength ladder has no inflation or cross-owner drift:

| Result | Exact licensed strength | Explicit non-credit |
|---|---|---|
| Green Proposition 3; Williams 4.22; MRW 2.8 | strong Morita equivalence at the full level | not an algebra isomorphism or tensor model |
| Brown--Green--Rieffel 1.2 | stable isomorphism under its strictly-positive-element hypotheses | no cancellation of `K`; no unstabilized conclusion |
| Williams 4.30 | direct **unstabilized** full-level isomorphism `C(S) rtimes R ~= C^*(L_p Z) tensor K(L^2(S,mu_p))` | not merely Morita/stable; no actual-topology theorem |
| MRW 3.1 | independent unstabilized full-groupoid tensor route for a positive unit-space measure | does not select the frozen `mu_p` |
| BHM 7.1 | natural **full** transformation-groupoid/full crossed-product isomorphism | no reduced theorem, Morita theorem, or tensor conclusion by itself |
| Williams 7.13 | full equals reduced crossed product because the acting `R` is amenable | not a consequence of transitivity, isotropy, BHM, Green, or MRW |
| Williams Example 7.11 / Proposition 3.1 | `C^*(R)=C_r^*(R) ~= C_0(R)` with the frozen Fourier sign | group owner only; transport requires the Phase-3 `Phi` and regular-norm proofs |

In particular, the licensed proxy chain is full-level:

```text
C^*(G_p^std)
  ~= C(S_p^std) rtimes_alpha,full R
  ~= C(S_p^std) rtimes_lt,full R
  ~= C^*(L_p Z) tensor K(L^2(S_p^std,mu_p)).
```

Williams 7.13 separately identifies the full and reduced **proxy crossed
products**. The retained BHM/Green/MRW sources do not supply an exact reduced
groupoid/crossed-product bridge, so this review does not promote that equality
to a reduced proxy groupoid-algebra statement. None of the proxy statements
extends `I` from the actual global algebra to a completion without a separate
boundedness/isometry proof.

## 6. Novelty ceiling and standalone gate

The novelty artifact records a reproducible search from database inception
through **2026-08-15**, with
`last_searched_at=2026-08-15T00:37:14+08:00`. Its inclusion unit is the exact
six-part rational-Witt actual-orbit/convolution/HOpen/transport/proxy package,
not any generic indiscrete-space lemma, standard groupoid framework,
Deninger Section-11 convolution, Paper-9 topology theorem, Paper-10 unit
collapse, or standard circle crossed product.

The search ledger reports:

```text
exact-package precedents included: 0
classification: SUPPORTED_WITHIN_SEARCH
new retained PDFs: 0
```

The disclosed OpenAlex and Semantic Scholar HTTP-429 failures, unavailable
reproducible zbMATH/MathSciNet corpus totals, and non-exposed general-web hit
total prevent any global absence or priority claim. Those limitations are
correctly retained rather than converted into zero hits. The only safe
novelty language is the bounded conclusion already printed in the novelty
report. Absolute terms such as “first,” “only,” “unprecedented,” and “no
prior work” remain forbidden.

The **Phase-2 search leg** of the standalone gate passes: the bounded ledger
is documented and contains no included exact-package precedent. Standalone
publication status itself is **not yet granted**. It remains conditional on
Phase 3 proving the exact convention split and strict proxy boundary,
especially `P11-6`--`P11-7`, and on the later proof/control, Route,
composition, manuscript, citation, peer, and release gates. Failure of that
later package gate still routes the correct mathematics to a technical note
or merge, exactly as the active protocol requires.

## 7. Final gate and Phase-3 clearance

No contradiction was found among the framework, owner/proxy, novelty, and
active-lock artifacts. No source locator, terminology, applicability label,
action sign, quotient measure, theorem strength, novelty ceiling, or
standalone condition requires amendment.

```text
phase2_integrated_final_review: PASS
critical_open: 0
major_open: 0
minor_open: 0
framework_checksum: 10/10 OK
framework_preflight_rerun: 5/5 PASS; 0 warnings
published_actual_framework_applicability: NOT_APPLICABLE
hopen_value_owner: DIRECT_P11_PROOF_OBLIGATION
global_fibre_and_regular_owner: AUTHOR_DEFINED_DIRECT
transported_completion_owner: GROUP_R_AFTER_REGISTERED_PROOFS
proxy_sign_and_mu_p: LOCKED_NO_DRIFT
proxy_strength_ladder: LOCKED_NO_INFLATION
novelty_ceiling: SUPPORTED_WITHIN_SEARCH
standalone_search_leg: PASS
standalone_release_status: PENDING_PHASE3_AND_DOWNSTREAM_GATES
phase3_proofs_and_controls_may_start: YES
actual_groupoid_cstar_notation_authorized: false
route_or_manuscript_authorized: false
active_lock_edited: false
```

Phase 3 may therefore start on the frozen `P11-1`--`P11-10` proof and
deterministic-control obligations. This clearance does not pre-certify any
target, completion map, arithmetic relevance, Route-A verdict, Route B, or
standalone paper.
