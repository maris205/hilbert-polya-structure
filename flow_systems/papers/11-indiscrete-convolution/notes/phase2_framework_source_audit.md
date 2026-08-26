# Paper 11 Phase-2 framework / source audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Verdict: **PASS — framework source coverage and applicability are locked;
no standard actual-groupoid `C*` framework applies**  
Open findings: **C0 / M0 / m0**  
Closed documentation correction: **Williams Example 1.80 is physical PDF
p. 38 / printed p. 26 in draft 3.1, not printed p. 29**

This is a Phase-2 source-verification deliverable only. It proves no
`P11-*` target, performs no Route evaluation, writes no manuscript text, and
does not authorize Phase 3 globally. Its only source-retention corpus is the
five-file `fw-*` tuple in `notes/sources/framework_source_manifest.md`.

## 1. Exact gate and object binding

The Phase-1 final gate authorizes this audit and nothing downstream. The
active status bytes read for the audit are:

| Active artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` |
| `notes/pipeline_state.md` | `d4801ffbe0785e3023c55245c21e7ab9c2ea08bf78d524ea86dfe7d54305bff1` |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` |
| `notes/phase1_final_gate.md` | `ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f` |

The exact owners remain separate:

```text
ACTUAL:
  G_act = X_{p,a} rtimes R
  X_{p,a} nontrivial indiscrete
  globally continuous C_qc^glob
  author GLOB-FIBRE-FAMILY and Ind_x

DIAGNOSTIC:
  raw Hausdorff-open zero-extension span C_c^HOp

PROXY:
  G_std = (R/L_p Z)_std rtimes R
  ordinary compact Hausdorff circle topology
  alpha_t(h)([r])=h([r+t])

TRANSPORT TARGET:
  ordinary group convolution C_c(R), C^*(R), C_r^*(R)
```

No source theorem is allowed to cross one of these owner boundaries without
an explicit map and hypothesis check.

## 2. Retrieval, integrity, and source-quality result

Five sources were reviewed, retained, and verified; none was rejected. The
manifest gives exact titles, versions, URLs, page counts, PDF hashes,
preflight hashes, and redistribution classes. ARS preflight returned `PASS`
for all five exact PDFs under `pypdf 6.15.0`, with three agreeing page counts
and no warnings.

Semantic Scholar Tier-0 metadata matched Tu by DOI
(`f64a9d39b8b172597899723332606786363f2789`) and Buss--Holkar--Meyer by DOI
(`f69645a5d05660c2cadff00664c0e7ddf811543c`). The public endpoint then
returned HTTP 429 for the remaining three lookups. Those three were therefore
verified through their official arXiv, NYJM, and author/AMS records rather
than treating an unavailable Tier-0 response as a failure.

The ARS empirical I--VII hierarchy has no proof-theoretic category. Each row
is recorded as Level VII by that mandatory vocabulary, with a separate
mathematical-authority grade controlling use here.

| Source | ARS level | Existence / venue | Mathematical authority | Currency | COI / predatory screen | Overall |
|---|---|---|---|---|---|---|
| Tu 2004 | VII | DOI resolves to EMS/*Documenta Mathematica*; exact journal PDF | primary peer-reviewed framework source | foundational/current for its named convention | normal authorial intellectual interest; no relevant financial conflict or predatory signal | A |
| Muhly--Williams 2008 | VII | official NYJM Monographs record and full text | primary/authoritative full treatment with explicit assumptions | foundational/current for the named locally Hausdorff framework | normal authorial intellectual interest; legitimate journal monograph, no predatory signal | A |
| Exel v3 | VII | official arXiv v3 and exact title/author/year | primary preprint, used only as an independent étale-definition boundary | current manifestation; not used as sole completion authority | preprint/peer-review caveat disclosed; no predatory venue claim | B+ for narrow role |
| Buss--Holkar--Meyer v2 | VII | DOI/arXiv metadata match PLMS publication; v2 marked final accepted | primary peer-reviewed theorem source | foundational/current for Theorem 7.1 | disclosed academic support only; no relevant COI or predatory signal | A |
| Williams draft 3.1 | VII | author endpoint, published AMS monograph metadata, exact Paper-8 byte match | authoritative author draft of published monograph; current errata screened | foundational; no relevant load-bearing erratum through 2025-10-10 | normal authorial intellectual interest; AMS is a recognized scholarly publisher | A- |

Framework claims are cross-checked at more than the required 30% rate: the
actual-object exclusion converges across Tu, Muhly--Williams, Exel, and
Buss--Holkar--Meyer; the proxy groupoid/crossed-product step is checked by
Buss--Holkar--Meyer and Williams; and the Williams group/completion claims
match the independently locked Paper-8 Williams bytes.

## 3. Applicability matrix

| Record / proposed use | Exact source gate | Result | What is licensed | What remains forbidden or direct |
|---|---|---|---|---|
| Tu `C_c(G)` / Haar framework on `G_act` | Tu requires ambient local compactness in the compact-Hausdorff-neighborhood sense; his later groupoid use also imposes the stated fibre and unit hypotheses | **NOT_APPLICABLE** | Tu supplies terminology and a comparison convention only | no Tu `C_c(G_act)`, Haar system, regular algebra, or completion theorem |
| Muhly--Williams patch algebra on `G_act` | G2 requires Hausdorff units; G3 requires a compact Hausdorff neighborhood of every arrow; the treatment is second countable and assumes a full Haar system | **NOT_APPLICABLE** | confirms that the Hausdorff-open raw span is genuine accepted practice | no published convolution/completion credit for the actual object |
| Exel étale framework on `G_act` | unit must be locally compact Hausdorff and range/source local homeomorphisms | **NOT_APPLICABLE** | independent boundary corroboration | neither the indiscrete unit nor continuous `R`-fibres are étale |
| Buss--Holkar--Meyer universal property on `G_act` | the paper works throughout with locally compact Hausdorff groupoids with Haar systems | **NOT_APPLICABLE** | sharp Hausdorff applicability boundary | no actual groupoid universal property or transformation-crossed-product theorem |
| Frozen `C_c^HOp(G_act)` | author diagnostic copies the raw zero-extension owner without importing ambient hypotheses | **DIAGNOSTIC_ONLY** | `HOPEN-SPAN-VALUE=0` is the registered direct value once `P11-1/P11-6` prove there is no nonempty Hausdorff open arrow patch | value zero is not “the standard groupoid algebra is zero”; this audit supplies no proof of the value |
| `GLOB-FIBRE-FAMILY` and `Ind_x` on `G_act` | no retained standard framework reaches this non-locally-Hausdorff owner | **AUTHOR_DEFINED_DIRECT** | ordinary fibre facts about copies of `R` may be used inside direct proofs | do not call the family a published Haar system or `Ind_x` a standard actual-groupoid regular representation |
| `C^full_glob` and `C^red_glob` | require a proved `Phi` and, for the reduced norm, the separately proved `U_x Ind_x U_x^-1=lambda_R` formula | **APPLICABLE_AFTER_TRANSPORT** | Williams's group `R` theorems may identify the transported completions | no notation `C^*(G_act)` or `C_r^*(G_act)` |
| Muhly--Williams framework on `G_std` | ordinary circle and arrow space are second-countable locally compact Hausdorff; the canonical fibre measures give a full Haar system | **APPLICABLE_PROXY_ONLY** | standard Hausdorff proxy dense convolution framework | no actual-topology credit |
| Buss--Holkar--Meyer Theorem 7.1 on `G_std` | exact right-to-left convention map below; proxy is Hausdorff with canonical Haar system | **APPLICABLE_PROXY_ONLY** | full proxy groupoid algebra equals the corresponding full crossed product | theorem is full, not reduced; no actual completion map |
| Williams Theorem 4.30 / 7.13 on proxy | closed `H=L_p Z`, explicit sign conjugacy, quotient-measure equation (4.63), and amenable `R` | **APPLICABLE_PROXY_ONLY** | source-gates the full homogeneous-space tensor-product theorem and then full/reduced equality | Morita, stable, full, reduced, and actual-isomorphism records remain distinct |
| Exel framework on `G_std` | the acting group `R` is nondiscrete, so the transformation groupoid is not étale | **NOT_APPLICABLE** | no proxy role needed | do not cite Exel for the standard proxy algebra |

The required four-way split is therefore exact:

```text
HOPEN-SPAN-VALUE                         = 0
  owner                                 = direct diagnostic
  proof status in this source audit      = withheld; P11-1/P11-6 obligation

PUBLISHED-FRAMEWORK-APPLICABILITY(actual)= NOT_APPLICABLE

GLOBAL FIBRE / UNIT REGULAR RECORD       = author-defined direct construction

C^*(R), C_r^*(R), Fourier                = group-R source, transport only after Phi
```

## 4. Framework findings

### 4.1 Tu: local compactness already blocks the actual arrow space

In the retained EMS journal manifestation, Definition 1.1 is physical p. 3 /
printed p. 567. Tu distinguishes open-cover quasi-compactness from compactness
and reserves compactness for quasi-compact Hausdorff spaces. His local
compactness means a compact neighborhood at each point and therefore implies
local Hausdorffness. Section 4.1, physical p. 17 / printed p. 581, then builds
`C_c(X)` as a span of zero-extensions from open Hausdorff patches; Definition
4.6, physical p. 19 / printed p. 583, tests that function space in the Haar
system axioms.

The actual arrow space has the frozen indiscrete-unit product topology and is
not locally Hausdorff. Hausdorff individual fibres do not cure the failed
ambient domain. Thus Tu's convention is an exact comparator for the HOpen
diagnostic and an exact reason not to call the author global family a Tu Haar
system.

### 4.2 Muhly--Williams: HOpen is real practice, but G2/G3 fail

Physical/printed pp. 4--5 explicitly distinguish their raw span `C(X)` from
globally continuous ambient functions. Their assumptions on p. 6 require a
Hausdorff unit space and compact Hausdorff arrow neighborhoods. Their p. 7
Haar system and Proposition 4.4 on pp. 21--23 operate only after those
assumptions are in force.

This verifies both halves of the required statement:

- the Paper-11 raw Hausdorff-open span has a faithful literature analogue;
- the actual indiscrete object is outside the published framework before
  convolution or completion is reached.

The direct value `0`, if proved, arises because the frozen actual topology has
no legal nonempty patch. It is not a Muhly--Williams theorem and does not
compute any standard completion.

### 4.3 Exel: “non-Hausdorff groupoid” does not mean non-Hausdorff unit

Exel's physical/printed p. 1 defines the paper's étale groupoids with locally
compact Hausdorff units and local-homeomorphism range/source maps. The arrow
space may be non-Hausdorff, but that relaxation does not cover the actual
indiscrete unit or a nondiscrete-time transformation groupoid. Exel is retained
only because it independently closes a common terminology escape route.

### 4.4 Buss--Holkar--Meyer: actual no, proxy yes

Physical/printed pp. 1--2 state the Hausdorff groupoid standing hypothesis and
explain that the displayed universal property only works as written in that
case. It is therefore unavailable for `G_act`.

For the proxy, convert the frozen right action to a left action by

```text
t circle [r] := [r] dot (-t) = [r-t].
```

Then the BHM left-action transformation groupoid receives the explicit
topological groupoid isomorphism

```text
([r],t)_right |-> (t,[r+t])_left,
```

because the left arrow has source `[r+t]` and range
`t circle [r+t]=[r]`. Theorem 7.1, physical/printed p. 23, therefore applies
to the ordinary Hausdorff proxy and identifies its **full** groupoid algebra
with the full crossed product for the associated coefficient action. This map
does not involve the actual indiscrete topology.

## 5. Williams source transport and proxy convention

### 5.1 Frozen `+t` coefficient sign

Williams equations (2.4)--(2.5), physical p. 54 / printed p. 42, associate to
a left action the automorphism

```text
alpha_t(h)(x)=h((-t) circle x).
```

For `t circle [r]=[r-t]`, this is exactly

```text
alpha_t(h)([r])=h([r+t]),
```

so the protocol sign is not silently reversed. The coordinate inversion
`kappa([r])=[-r]` conjugates `circle` to Williams's ordinary left translation
`t+[r]`; hence Theorem 4.30 may be used after naming this conjugacy.

### 5.2 Normalized proxy Haar probability satisfies (4.63)

Set `G=R`, `H=L_p Z`, give `G` Lebesgue Haar measure and `H` counting Haar
measure, and put `rho(t)=1/L_p`. With `mu_p` the normalized Haar probability
on `R/L_p Z`, equation (4.63) becomes

```text
integral_R f(t) dt/L_p
  = integral_{R/L_p Z} sum_{n in Z} f(r+nL_p) dmu_p([r]).
```

Thus the exact `mu_p` frozen in the protocol is an admissible quotient measure
for Williams Theorem 4.30, physical p. 150 / printed p. 138. The source then
licenses the full-proxy candidate

```text
C(S_p^std) rtimes_alpha,full R
  ~= C^*(L_p Z) tensor K(L^2(S_p^std,mu_p)),
```

after the explicit action conjugacy. This is a proxy theorem only. It does not
make the pullback of `C_qc^glob(G_act)` dense or isometric and supplies no
completion extension of `I`.

### 5.3 Transported group `C^*(R)` facts

The retained Williams draft supplies the exact chain:

- Example 1.80, physical p. 38 / printed p. 26, fixes the character and
  Fourier sign `exp(-it xi)`;
- Proposition 3.1, physical p. 94 / printed p. 82, gives
  `C^*(R) ~= C_0(Rhat) ~= C_0(R)`;
- Definition 7.7 and Example 7.9, physical p. 210 / printed p. 198, identify
  the reduced group norm with the left-regular norm;
- the discussion and Theorem 7.13, physical p. 211 / printed p. 199, apply
  because `R` is abelian and hence amenable, yielding
  `C^*(R)=C_r^*(R)` and full/reduced equality for the proxy crossed product.

For the actual owner this chain activates only after Phase 3 proves both
`Phi` as an algebraic `*`-isomorphism and the displayed unitary reduction of
every `Ind_x`. It licenses transported author-defined norms, never a standard
actual-groupoid completion.

## 6. Safe downstream source language

Safe, subject to the named Phase-3 proofs:

> The frozen HOpen raw span is a diagnostic analogue of published
> locally-Hausdorff conventions; those published frameworks do not apply to
> the actual indiscrete orbit groupoid. The global fibre family and unit
> operators are author-defined. After the global algebra is proved to be
> `C_c(R)`, its completions may be transported from the ordinary group
> `C^*(R)=C_r^*(R)`. Separately, the ordinary Hausdorff-circle proxy has the
> standard full transformation-groupoid crossed product and Williams's
> homogeneous-space model after the explicit sign and measure translation.

Unsafe:

- “`C_c^HOp=0`, therefore the groupoid `C*`-algebra is zero.”
- “The actual fibre family is a Haar system in Tu/Muhly--Williams.”
- “BHM identifies `C^*(G_act)` with a crossed product.”
- “Williams Theorem 4.30 applies directly without converting the frozen
  right action and `+t` coefficient convention.”
- “Morita equivalence, stable isomorphism, full/reduced equality, and the
  concrete tensor-product isomorphism are the same claim.”
- “The dense actual-to-proxy pullback automatically extends to completions.”

## 7. Final framework gate

```text
phase2_framework_source_audit: PASS
critical_open: 0
major_open: 0
minor_open: 0
retained_full_texts: 5
preflight_pass: 5
preflight_fail_or_unavailable: 0
hopen_span_value: 0 (direct P11-1/P11-6 proof obligation; not source-owned)
published_actual_framework_applicability: NOT_APPLICABLE
global_fibre_record_owner: AUTHOR_DEFINED
group_completion_owner: C*(R), transport only after Phi
proxy_bhm_applicability: APPLICABLE_AFTER_EXPLICIT_RIGHT_TO_LEFT_MAP
proxy_williams_applicability: APPLICABLE_AFTER_SIGN_AND_MEASURE_CHECK
actual_groupoid_cstar_notation_authorized: false
active_lock_edited: false
phase3_clearance_from_this_framework_audit: true
global_phase2_clearance: requires the remaining independent Phase-2 audits
```

The sole historical locator discrepancy is closed by the exact locator in
this audit and manifest. It changes no theorem, convention, applicability
classification, or active byte.
