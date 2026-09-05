# Independent delta-comb manuscript review

Review date: 2026-09-05 UTC.

Disposition: **No blocking mathematical, translation, numerical-reporting, or citation-context issue found in the reviewed snapshot. One minor editorial clarification is recommended.** This is a bounded independent source/manuscript audit, not journal acceptance, a global-priority certificate, an interval-certified computation, or a formal ARS runtime result.

## 1. Scope and actual inspection

The reviewer read the actual complete `delta_comb/PROOF_PACKAGE.md`, `PAPER_PLAN.md`, `paper/main.tex`, `paper/math_commands.tex`, all eight section files, and the five-entry bibliography. The complete `SOURCE_AUDIT.md`, `CHECK_REPORT.md`, existing independent `boole/REVIEW_OF_DELTA_COMB.md`, and `reviews/DELTA_BROADER_SOURCE_CHECK.md` were inspected as supporting records, not accepted as substitutes for checking proofs or primary sources.

For the finite-check section, the reviewer additionally read the complete `sanity.py` and the actual `SANITY_OUTPUT.json`. All nine table rows and the prose's numerical quantities were reconciled against that JSON, not merely against the author's report. The author code was **not rerun**. There was no manuscript/source edit, PDF compilation or visual inspection, or Git operation in this review. Its only repository output is this report.

The proof-writer and ARS academic-paper-reviewer instructions informed the proof-obligation and claim/evidence checks. A separate current-team agent independently checked the comparator/phase and asymptotic-transfer arguments and reported no defect. That bounded corroboration is not represented as a multi-person external referee panel. The main reviewer also independently accessed the cited DLMF formulas. No ARS machine registry, route result, or literal pipeline execution is claimed.

The assessment below covers the finite positive-coupling theorem, the infinite-coupling endpoint, actual citation uses, and the finite numerical reporting. It does not establish global novelty or any arithmetic realization.

## 2. Findings requiring attention

### D-MINOR-1: sharpen one abstract sentence

Location: `paper/sections/0_abstract.tex`, lines 12–13, the statement that shrinking gaps make a direct interval-decoupling approximation unsuitable.

The proved conclusion is specific: replacing all finite delta interactions by Dirichlet walls changes the high-energy leading coefficient from two to one. The current sentence can be read more broadly as ruling out useful interval methods in general. The manuscript itself validly uses a finite-head/tail split in Section 6, so the broadest reading is unnecessary.

Suggested clarification: “Replacing the finite interactions by Dirichlet walls changes the leading high-energy coefficient, so the fixed-coupling count requires a different comparison.” This is an editorial precision request, not a gap in a theorem or proof. The surrounding introduction and discussion already make the distinction correctly. No other correction is required by this review.

### Boundaries that must remain explicit

- The logarithmic remainder is proved for each fixed finite positive coupling. It is not an estimate uniform as the coupling tends to infinity, and the finite data do not improve it to a bounded remainder.
- The source-zeta continuation obtained here stops at the open half-plane `Re s > 0`. No value or derivative at zero, and hence no zeta-regularized determinant of the finite comb, is obtained by this argument.
- The ordinary Fredholm determinant from trace-class inverse is legitimate. The comparator's Bessel function is not identified with the comb's spectral determinant.
- Inclusive fixed-energy counts are addressed, including endpoint eigenvalues. An analogous assertion for strict counts at those thresholds is not made.
- The cited passages do not contain the stated finite-coupling formula. That bounded observation is not a global-priority claim.

These qualifications are present in the actual TeX and should be retained during final production.

## 3. Proof/translation audit

### 3.1 Forms, all-positive-coupling domain, and operator realization

The compression from the proof package preserves the essential non-circular order of argument. The finite-prefix sampling inequality is proved before asserting finiteness of either infinite nonnegative expression. Its error is bounded by `2 kappa ||f||_2 ||f'||_2` without an inverse-gap factor. Monotone passage through finite prefixes therefore establishes equivalence of the vertex square-sum and the cell-average integral for every `f` in the underlying half-line Dirichlet Sobolev space.

The harmonic estimates apply on every cell, including the first one, and give

`|V_kappa(x) - C exp(x/pi)| <= B`, with `C = kappa exp(-gamma)/pi` and `B = kappa/pi`.

Consequently the common domain really is

`{f in H_0^1(0,infinity): integral exp(x/pi)|f(x)|^2 dx < infinity}`

for **all** `kappa > 0`, not merely an inclusion or a large-coupling statement. Young's inequality yields the common-domain brackets

`Q_(1-epsilon),C - d_epsilon ||f||^2 <= q_kappa[f] <= Q_(1+epsilon),C + d_epsilon ||f||^2`,

where `d_epsilon = kappa^2/epsilon + B`. The square-root form norms, with a sufficiently large positive shift, are equivalent to the weighted Sobolev norm. Closedness, density, and self-adjoint realization consequently do not assume the result they are used to prove.

The compactness proof combines compact restriction to a bounded interval with the exponentially small tail bound. The operator-domain description retains global square-integrability of the piecewise second derivative, continuity, the initial Dirichlet condition, and the positive-sign derivative jump `f'(x_n+) - f'(x_n-) = kappa f(x_n)`. The cutoff/core argument rules out an unstated extra boundary condition at infinity. Strict positivity follows from compact resolvent and the trivial zero-energy kernel; simplicity follows from the one-dimensional Cauchy data and the jump propagation. No sign, domain, or all-coupling gap was found.

### 3.2 Comparator: scale, phase, common threshold, and integer offset

The scaling is correct:

`A_(a,C) ~= a/(4 pi^2) B_b`, `B_b = -d^2/dy^2 + b^2 exp(2y)`,

`b = 2 pi sqrt(C/a)`, and `K = 2 pi r/sqrt(a)`.

The use of imaginary **order** in `K_(iK)(b exp(y))` is correctly distinguished from imaginary spatial argument. Fixed-order large-argument asymptotics select the unique square-integrable solution at infinity. The connection identity has the correct sign:

`K_(iK)(b) = pi Im I_(-iK)(b)/sinh(pi K)`.

The argument does not merely quote a pointwise large-order estimate. It explicitly controls both `S_b(K)-1` and its derivative uniformly for `b` in a fixed compact positive interval. One common `K_0` places the series in a disk with a single logarithm; increasing that same threshold gives a uniformly increasing unwrapped phase. The Gamma logarithm convention is specified. The phase constant is `+pi/4`, and the real digamma error has order `K^(-2)`, as used.

The low-energy integer offset is not omitted: `B_b >= B_(b_-)` bounds the number of roots at or below the common threshold, while the phase at that threshold is bounded on the same compact parameter interval. Equivalently, for `K >= K_0`, the inclusive count can be written as the count at `K_0` plus the difference of the two phase floors. This supplies the uniform bounded error needed when `a` later moves with energy. Endpoint floor conventions affect at most a bounded quantity and do not invalidate that estimate.

The final comparator count is

`N_A(r^2) = (2r/sqrt(a)) [log(2r/sqrt(C)) - 1] + O_C(1)`,

uniform in the stated kinetic-coefficient interval. No missing uniformity or counting-offset assumption was found.

### 3.3 Min–max transfer and fixed-coupling remainder

The inequality directions are correct. Writing `A_+ = A_(1+epsilon),C` and `A_- = A_(1-epsilon),C`, form order gives

`N_(A_+)(k^2-d_epsilon) <= N_kappa(k^2) <= N_(A_-)(k^2+d_epsilon)`.

With `epsilon = 1/k`, the shifted frequencies are `k + O_kappa(1)`, while `a-1 = O(1/k)`. The manuscript explicitly controls both derivatives of the smooth comparator main term: its frequency derivative is logarithmic and its kinetic-coefficient derivative has size `k log k`. Each change therefore costs at most `O_kappa(log k)`. In particular, the proof does **not** illegitimately transfer the comparator's bounded error to the actual comb.

Insertion of `C = kappa exp(-gamma)/pi` gives

`N_kappa(k^2) = 2k log k + [log(4pi/kappa)+gamma-2] k + O_kappa(log k)`.

The energy-variable restatement has leading term `sqrt(E) log(E)`, not half that term. The proof and both displayed theorem statements agree.

### 3.4 Heat trace, source zeta, and Schatten endpoint

Stieltjes integration is justified by the positive ground energy and the count growth. The change of variables in the heat integral gives the leading factor `Gamma(3/2)/sqrt(t)`, and

`psi(3/2) + C_kappa = log(pi/kappa)`.

Thus the theorem's heat expression

`sqrt(pi)/(2sqrt(t)) [log(1/t)+log(pi/kappa)] + O_kappa(log(1/t))`

has the correct coefficient and constant. The logarithmic error estimate is uniform over the integration variable in the stated small-time range.

For the zeta function, the finite-energy contribution is entire because the count vanishes below the strictly positive ground energy. The remainder integral and its complex derivatives are locally dominated only on `Re s > 0`, exactly as claimed. Expanding

`s/(s-1/2)^2 + s C_kappa/(s-1/2)`

gives a double-pole coefficient `1/2` and a simple-pole coefficient `1+C_kappa/2`. The pole is genuine and is the only pole in that open half-plane. No continuation through its boundary is inferred.

The positive Stieltjes identity for `sum E_j^(-p)` is valid even when divergent. It proves both sides of the sharp criterion `p > 1/2`, including failure at `p = 1/2`. The same threshold applies to the shifted resolvent. Trace-class inverse permits the ordinary Fredholm determinant; its interpretation is kept separate from both the exponential comparator and a regularized determinant. No endpoint or determinant overclaim was found.

### 3.5 Infinite coupling and inclusive fixed-energy counts

The increasing forms have the stated dense limit domain: functions vanish at every vertex and on each interval belong to the Dirichlet Sobolev space with square-summable derivative norms. The limit is the direct sum of Dirichlet interval Laplacians. This supports strong-resolvent convergence by monotone forms.

The strengthening to norm-resolvent convergence is justified rather than assumed. At the negative spectral parameter used in the proof,

`0 <= R_kappa - R_infinity <= R_(kappa_0)`

for `kappa >= kappa_0`, with a fixed compact upper bound and strong convergence of the left-hand side to zero. The finite-head/tail projection argument, including control of off-diagonal blocks by positivity, proves operator-norm convergence.

Eigenvalues then increase to the endpoint eigenvalues, with multiplicities. For fixed `E`, let `J = N_infinity(E)`. The first `J` finite-coupling eigenvalues stay at or below `E`, even when `E` is an endpoint eigenvalue; convergence of the next eigenvalue, whose limit exceeds `E`, eventually excludes all later indices. This proves eventual equality of the **inclusive** counts at every fixed finite energy, not merely continuity points. The proof properly avoids making a strict-threshold assertion at a limiting eigenvalue.

The direct-sum spectrum is `(mn)^2`, counted with pair multiplicity. The hyperbola identity gives the divisor count and the elementary `O(sqrt(k))` remainder. This endpoint has leading coefficient one. The two iterated limits of the count normalized by `k log k` are therefore two and one in the stated order. No uniform-in-coupling inference is hidden in that conclusion.

## 4. Primary-source and bibliography checks

All five actual bibliography entries are used. Every one of the nine actual citation contexts was checked against the corresponding primary passage or formula. Access below was performed by this reviewer on 2026-09-05; prior audit summaries were not the sole basis.

### 4.1 Bibliographic identity and access receipts

1. **`egger2011infinite`.** The [arXiv metadata](https://arxiv.org/abs/1104.1364) verifies the title, two authors, 2011 date, journal volume 44, article 185202, and DOI `10.1088/1751-8113/44/18/185202`. The [actual arXiv v1 PDF](https://arxiv.org/pdf/1104.1364v1) displays Egger's longer surname form used in the bibliography. Its Section 2 and start of Section 3 were read for the citation uses. The accessed preprint has 50 pages; the journal reference describes a 44-page version. Publisher full-text access is not claimed.

2. **`egger2011thesis`.** The [official OPARU item JSON](https://oparu.uni-ulm.de/server/api/core/items/85bfa3c7-67a9-46f4-81b6-1ddefe00f428) confirms author, title, institution, DOI, legacy handle, creation year 2011, 2016 accession/availability, and the legacy 2012 availability field. The [repository's extracted full text](https://oparu.uni-ulm.de/server/api/core/bitstreams/444820b4-8f1a-4e70-a22b-b6884cd41c6d/content) independently supplies the title-page year and doctorate date 16 February 2012, together with the cited introduction and Chapter 2 scope. A browser rendering attempt failed, but direct HTTPS text access succeeded. The 2016 repository date is not substituted for the dissertation year. An unrelated locally cached PDF was encountered; its filename is **not** used to authenticate the source. The conclusion rests on the official text and metadata just described.

3. **`bifulco2024infinite`.** The [arXiv record](https://arxiv.org/abs/2308.16869) verifies authors, title, the 2023 preprint, the 2024 journal publication link, and DOI. DOI content negotiation and [publisher-deposited Crossref metadata](https://api.crossref.org/works/10.1063/5.0178226) verify journal, volume 65, issue 7, and article number 073502. The [actual arXiv v1 PDF](https://arxiv.org/pdf/2308.16869v1), Section 5 and Theorem 11, was read. The manuscript explicitly identifies that theorem numbering as belonging to the arXiv version. Publisher full-text verification is not claimed.

4. **`bifulco2025thesis`.** The [actual DNB-hosted dissertation](https://d-nb.info/1388406829/34) was retrieved directly. Its front matter verifies Patrizio Bifulco, the complete title/subtitle used in the bibliography, FernUniversität in Hagen, and submission on 25 June 2025. The cited subsections and theorems were inspected in the text. The directly retrieved PDF has SHA-256 `468fa3abb4502020163501361b494e7ff8dae78dd917719990ceee1649bdd335`, matching the PDF used for local text inspection. This establishes provenance by content, not by filename. No visual PDF inspection is claimed.

5. **`nist2026dlmf`.** The [actual DLMF homepage](https://dlmf.nist.gov/) explicitly reports **Version 1.2.7, release date 2026-06-15**. This was read directly, not inferred from a prior audit or the manuscript. The specified Bessel and Gamma formula pages were also opened and read. The bibliography's year, version, release date, and access date agree.

### 4.2 Complete actual-citation context register

| Context in reviewed TeX | Claim supported, and exact primary locator | Assessment |
| --- | --- | --- |
| Introduction, line 50; `egger2011infinite` | Original chain, positive-coupling discreteness/positivity, strong-resolvent limit, and nearby historical scope. [Preprint Section 2](https://arxiv.org/pdf/1104.1364v1): model (4), Theorems 2.1–2.2, (28)–(30), and final paragraph before Section 3; Section 3 begins the divisor endpoint. | Supported. The final paragraph defers the finite-coupling asymptotic in that paper; it is not evidence of present-day global priority. |
| Introduction, line 59; `egger2011thesis` | Infinite-chain work is outside the thesis; its subsequent treatment uses finitely many edges. [Official extracted text](https://oparu.uni-ulm.de/server/api/core/bitstreams/444820b4-8f1a-4e70-a22b-b6884cd41c6d/content), Introduction printed pp. 3–4 and Chapter 2 p. 17. | Supported by explicit scope statements, not merely absence of a keyword. |
| Introduction, line 63; `bifulco2024infinite` | Modified local Weyl law concerns infinite coupling. [ArXiv v1 Section 5, Theorem 11](https://arxiv.org/pdf/2308.16869v1), printed pp. 6–7. | Supported: the theorem explicitly assumes `sigma = infinity`. The version-specific locator is correctly qualified. |
| Introduction, line 65; `bifulco2025thesis` | Later dissertation retains the Dirichlet endpoint, also with a bounded potential. [Dissertation Sections 6.3.3 and 6.3.5](https://d-nb.info/1388406829/34): (6.3.28), Theorem 6.3.14, (6.3.48), and Theorem 6.3.19, printed pp. 221–223 and 229–230. | Supported. The local theorem uses bounded potentials; the comparison subsection further restricts to an integrable bounded potential. Neither is used as the present finite-coupling count. |
| Forms, line 76; `egger2011infinite` | Compactness itself is classical for the chain. [Theorems 2.1–2.2](https://arxiv.org/pdf/1104.1364v1), printed pp. 8–9. | Supported; the manuscript separately proves its weighted-domain realization. |
| Comparator, line 49; `nist2026dlmf` | Fixed-order decaying and growing solutions at large positive spatial argument. [DLMF 10.25.3](https://dlmf.nist.gov/10.25#E3) and [10.40.1](https://dlmf.nist.gov/10.40#E1). | Supported. Used for the endpoint solution, not as a substitute for uniform imaginary-order counting. |
| Comparator, line 61; `nist2026dlmf` | Modified-Bessel series and connection identity. [DLMF 10.25.2](https://dlmf.nist.gov/10.25#E2) and [10.27.4](https://dlmf.nist.gov/10.27#E4). | Supported; substitution at order `iK` gives the displayed sign and series. Uniform remainder/derivative estimates are proved locally. |
| Comparator, line 95; `nist2026dlmf` | Sectorial log-Gamma and digamma expansions. [DLMF 5.11.1–2](https://dlmf.nist.gov/5.11). | Supported with the manuscript's analytic logarithm convention and fixed sector. |
| Strong coupling, line 7; `egger2011infinite` | Strong-resolvent Dirichlet limit and divisor endpoint are classical. [Section 2, (28)–(30), and Section 3](https://arxiv.org/pdf/1104.1364v1). | Supported. Norm-resolvent convergence and inclusive threshold conclusions are proved in the manuscript, not attributed to those passages. |

No missing bibliography key, unused listed entry, source-title mismatch, version-number mismatch, or unsupported use of the nine cited contexts was found. The bounded reading does not establish an exhaustive literature result. In particular, the global-priority disclaimer is necessary and appropriate.

## 5. Actual finite-output reconciliation

The following cells, counts, predictions, and residuals match the actual JSON and the six-decimal table rendering. “Count” means the common shooting and two-finest-grid finite-head count, not a certified infinite-spectrum count.

| Coupling | Frequency | Cells | Count | Analytic prediction | Count minus prediction |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0.5 | 10 | 2545 | 64 | 64.065573 | -0.065573 |
| 0.5 | 20 | 10085 | 156 | 155.857033 | 0.142967 |
| 0.5 | 40 | 40244 | 367 | 367.165840 | -0.165840 |
| 1 | 10 | 1282 | 57 | 57.134101 | -0.134101 |
| 1 | 20 | 5052 | 142 | 141.994089 | 0.005911 |
| 1 | 40 | 20132 | 339 | 339.439953 | -0.439953 |
| 2 | 10 | 660 | 50 | 50.202629 | -0.202629 |
| 2 | 20 | 2545 | 128 | 128.131146 | -0.131146 |
| 2 | 40 | 10085 | 312 | 311.714066 | 0.285934 |

The actual saved output also supports all of these narrower observations:

- Three symbolic remainders are exactly recorded as zero. The script constructs the analytic identities rather than fitting the coefficients to eigenvalue data.
- The high-precision configuration is 70 decimal digits. The first 1,000 endpoint pairs give maximum deviation `0.5262051115958638804748887`. The single sampling test uses 1,200 cells and reports difference `0.2534272797325425665304724` against bound `4.6875`. Reading the script confirms the stated function, coupling, and explicit antiderivative implementation.
- Exact divisor tests at integer frequencies `1, 2, 10, 100, 1000` give `1, 3, 27, 482, 7069`, respectively.
- The reported cutoffs agree with `ceil(4 pi (k^2+kappa^2+1)/kappa)`. The tail lower bound is an analytic form argument. Its saved lower-bound/energy ratios range from `4.002931678` to `4.128056695`, agreeing with the rounded manuscript range.
- For all nine cases, the original and doubled shooting cutoffs give matching Dirichlet and Robin counts. The two finest finite-element grids, maximum free phases `0.02` and `0.01`, match those counts.
- At coupling two and frequency forty, **both** coarser grids, maximum free phases `0.08` and `0.04`, return **311**, while shooting and the two finer grids return **312**. The JSON explicitly records `coarse_levels_agree: false` for this case. The prose correctly says eight, not nine, cases agree at all four levels.
- The minimum relative LDL pivot among finest-grid cases is `7.844349e-6`, at coupling two and frequency twenty. The manuscript properly calls it a diagnostic, not a roundoff or spectral-gap certificate.
- The script uses genuinely different finite-head descriptions: rounded phase propagation versus linear finite-element stiffness/mass inertia. The finite-element computation uses strict negative-pivot counts. It is not an independently interval-certified evaluation of the inclusive infinite count, and the manuscript explicitly says so.

The code/output dependency versions SymPy 1.14.0 and mpmath 1.3.0 agree. Python 3.12.3 and Linux x86_64 are historical execution metadata stated in `CHECK_REPORT.md`, not independently established by this non-rerun review. No evidence was found contradicting those declarations, but they are not upgraded here into fresh execution receipts.

The reported finite data therefore survive a source-code/output/prose consistency audit. They do not establish all-cell sampling bounds, the asymptotic remainder, a uniform coupling estimate, or any target-zero claim. The analytic proofs supply the first three mathematical statements within their stated scopes; no target-zero data are used.

## 6. Seven named AI-research failure-mode checks

These are the exact seven failure-mode names from the ARS checklist, applied to this mathematical manuscript and its finite sanity-check code. No empirical-efficacy evaluation or literal seven-reviewer execution is claimed.

| Named failure mode | Scope-specific evidence and conclusion |
| --- | --- |
| Implementation bug passing AI self-review | There is finite-check code, so this is not marked “no implementation.” The reviewer read the actual code and reconciled its saved output; analytic proof obligations were checked independently. No relevant bug was identified, but absence of rerun/interval certification remains an explicit limitation. |
| Hallucinated citation | All five bibliography entries and all nine actual citation contexts were checked against primary metadata/text/formulas. No fabricated entry or unsupported citation-context use was found. |
| Hallucinated experimental result | Every table row and reported scalar was checked against the actual saved JSON. The coarse-grid discrepancy remains visible. Numerical claims are finite sanity checks, not asserted empirical efficacy or proof. No invented result was found. |
| Shortcut reliance | The theorem is not inferred from nine favorable points, a formal WKB integral, fixed-parameter Bessel asymptotics, or an arithmetic target fit. The manuscript retains the form-domain, uniform phase-offset, min–max, and endpoint arguments needed to exclude those shortcuts. |
| Implementation bug reframed as novel insight | The 311/312 mesh discrepancy is identified as a coarse-discretization issue and retained, not advertised as new spectral behavior. The two-versus-one limiting coefficient is analytically proved and not extracted from that discrepancy. |
| Methodology fabrication | The finite-method descriptions match the inspected script: phase propagation, finite elements with consistent mass and LDL inertia, doubled cutoffs, and the specified mesh levels. No interval certification, fresh reviewer rerun, global-priority certificate, or unperformed PDF inspection is claimed here. |
| Frame-lock at early pipeline stage | The manuscript expressly credits classical ownership, distinguishes later infinite-coupling results, and retains negative boundaries on global novelty, zeta regularization, arithmetic realization, and uniform coupling. This bounded audit found no contradiction concealed to preserve a preferred arithmetic narrative. It does not certify exhaustive alternative-model search. |

## 7. Reviewed input hashes

SHA-256 values were measured from the actual files after the read-through. Paths below are relative to `henon_dynamics/research_c399_c403/`. The review attaches to this snapshot; any later theorem/proof/citation change requires a delta check.

```text
7a63727caee39ba2926e2fe93dd249df17ea9ec4ba5ddf7b760432f02898b0af  delta_comb/PROOF_PACKAGE.md
1a4724fa0dfff16d47370376ab70ad45b688e8d188d8eee9bed79c0d533452bb  delta_comb/PAPER_PLAN.md
e85f39d3ab773794bc768335b6a5719648180648ef3cde6cac1a158b786fdf69  delta_comb/paper/main.tex
0877c2538604b06108164619fff7d5ddad90db431b78dd34d1ae99880053c300  delta_comb/paper/math_commands.tex
01bc361cf7ed4fedccae43d92a8a556cbcb4cca65d5dade59c35d9ce89712433  delta_comb/paper/sections/0_abstract.tex
1643c128d4c8822236e8f599c7809b4eda78ae6ecda0240bfc49f6720588afae  delta_comb/paper/sections/1_introduction.tex
205bb36168a5391193c9337e99d3be3a26cae04bbd826a7bfb2da9c4947eb52a  delta_comb/paper/sections/2_forms.tex
3f9b699040d7a26eae1430461d41d2c2d02706a6d635b68a6f2135e65c410982  delta_comb/paper/sections/3_comparator.tex
404e95e350d5d3ab5c36076c50ee0546e6f13eef7ec045ccc75657b0c223ff83  delta_comb/paper/sections/4_asymptotics.tex
9e28f66ceb97ba250d9774cfa141d7d03bb5117b8093ce85f3d8516d90b54771  delta_comb/paper/sections/5_strong_coupling.tex
a6f92368734cc4b39b767c4ea9516030e2041b2f898e3d27087a43b46dfcd22f  delta_comb/paper/sections/6_checks.tex
dfb8ef3137bd1b3f85145f1b7de7a282a5596a34aca91ed33a122521466d36a9  delta_comb/paper/sections/7_discussion.tex
a99f9fe25a836b0c3c64957df4057eff7424680e0802c686af26d53de61d3853  delta_comb/paper/references.bib
8a5c31e6d89c1180e989549480a05d8a5a268ac537ab90a328f725a5fcda655b  delta_comb/SOURCE_AUDIT.md
0e354ea7ff30664703c8b665789b4bef08f0c63337f657d069cf97b85ca6830d  delta_comb/CHECK_REPORT.md
0796b98534e6d9976608524dbb9df217208b1d501c649e7c2b32e3397b2070c5  delta_comb/sanity.py
68b7338ce7fbc867430bd0b513f1fb57bb5a21861d7a1a8e651d8dfa04f43641  delta_comb/SANITY_OUTPUT.json
ce6da9327d1b270774e961feb1d61ee37c71573e8723b738b5eb64064abe4ca8  boole/REVIEW_OF_DELTA_COMB.md
04d84a7707d96f3f0b88cf69612d918d8d9851739e2c61dddf7b1f3cc9556750  reviews/DELTA_BROADER_SOURCE_CHECK.md
```

## 8. Handoff conclusion

The actual TeX is a faithful, sufficiently explicit compression of the reviewed proof package on the requested mathematical points. The finite-coupling coefficient, its logarithmic error, heat/zeta constants and boundaries, sharp Schatten threshold, norm-resolvent limit, and inclusive endpoint counts survive this audit. The bibliographic ownership and arithmetic nonclaims are appropriately bounded. Finite-check reporting matches the retained raw output, including the adverse coarse-grid case.

Proceed to the main agent's final build and PDF inspection, optionally after D-MINOR-1. Those production checks are outside this review and are not pre-certified by it. If only production metadata or the recommended abstract wording changes, a targeted receipt can identify the new hashes without implying that a different mathematical source was reviewed in full.

## 9. Targeted post-review receipt — 2026-09-05 12:02 UTC

The main agent subsequently changed exactly two of the 19 reviewed inputs. This addendum records a targeted source check, not a fresh mathematical review or build verification. The preceding full-review report, before this addition, had SHA-256 `46b90653dac89498ea12adee1470054330daad8ab4b16fbc56ae7f7835816f10`.

- **Abstract:** the broad interval-decoupling sentence is replaced by the recommended statement that replacing finite interactions by Dirichlet walls changes the leading high-energy coefficient and therefore requires a different fixed-coupling comparison. The reviewer read the complete changed abstract and confirmed that this resolves **D-MINOR-1** without altering its formulas or claim boundaries. Reversing only those three replacement lines in a read-only output stream reproduces the original abstract hash `01bc361cf7ed4fedccae43d92a8a556cbcb4cca65d5dade59c35d9ce89712433`, confirming that there is no additional abstract change.
- **Main TeX file:** immediately after `documentclass`, the only additions are `\pdfinfoomitdate=1` and `\pdftrailerid{}`. The complete file was read. Omitting only those two lines in a read-only output stream reproduces the original main-file hash `e85f39d3ab773794bc768335b6a5719648180648ef3cde6cac1a158b786fdf69`. These are production-metadata settings; no mathematical content or section inclusion changed. Their behavior in the final compiled PDF remains a main-agent build check, not a result certified here.
- **Remaining inputs:** all other 17 entries were checked against the original Section 7 SHA-256 values with `sha256sum -c`; every entry passed, including every proof-bearing section, bibliography, proof package, numerical code/output, and supporting audit.

The two replacement snapshot hashes are:

```text
ad78a74abfc5f9d7a62a8b5ed8c7db094a453f55da85f398a4f4af84113e2b5f  delta_comb/paper/main.tex
95c63f61da43d369b99a6f2f98d1604d723135e85ec86cb20b34aff89c3e9f69  delta_comb/paper/sections/0_abstract.tex
```

**Targeted disposition:** D-MINOR-1 is closed. The no-blocking-issue conclusion of the full review applies to this updated source snapshot with the two substitutions above and the other 17 original hashes unchanged. No outstanding correction is required by this review. No author-code rerun, mathematical rerun, PDF compilation/visual inspection, further citation search, source edit, or Git operation was performed for this addendum; only this review report was updated.
