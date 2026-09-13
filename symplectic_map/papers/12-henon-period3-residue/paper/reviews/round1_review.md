# Consolidated Round 1 Manuscript Review

## Signed decision

**Verdict: MINOR REVISION**

**Release state: `DO_NOT_FINALIZE` until the single typesetting defect M1 is corrected, the manuscript is rebuilt, and the corrected PDF is visually rechecked.**

The mathematical contribution, including its proof-only all-degree certificate, survives independent line-by-line and adversarial review. I found no Critical or Major issue. I found one Minor production issue: seven bare `quad` tokens are printed literally in two equations on page 12. This defect does not change the proof, but it should be repaired before archival or submission release.

| Severity | Count | Disposition |
|---|---:|---|
| Critical | 0 | None found |
| Major | 0 | None found |
| Minor | 1 | M1 must be fixed before finalization |

## Review identity, scope, and limitations

This is the sole fresh consolidated Round 1 review. It combines the ARS journal/criteria, methodology, domain, perspective, devil's-advocate, and editorial-synthesis views in one signed report. The review was conducted from the frozen manuscript, PDF, proof package, claim manifest, bibliography, and declared integrity/provenance documents.

`criteria_binding_unavailable`: no target venue and no author-confirmed venue criteria were supplied. I therefore make no claim of fit to a particular journal, conference, page limit, house style, or acceptance threshold. My editorial decision uses general standards for a rigorous specialist mathematics manuscript.

There was no cross-model review. The five ARS views were synthesized by one model-family reviewer, and the later QA shadow is from the same broad model family. Correlated blind spots are therefore possible even though the audits were operationally independent. The QA shadow was received only after my substantive mathematical and production review was substantially complete; it independently agreed with the package checks and the sole Minor finding.

The scientific audit was proof-only. I did not run or import a candidate, recover scientific computations, or inspect `code`, `preexecution`, `results`, or `runtime` as scientific evidence. Registered-run failure material was treated only as non-evidentiary provenance. No high-index \(m=8,9\) observation, no \(Q/R\) agreement, and no failed registered computation was used to certify any theorem.

## Frozen-object binding

All seven supplied bindings were independently recomputed and matched byte for byte.

| Object | Recomputed SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617` | MATCH |
| `paper/manuscript.pdf` | `bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949` | MATCH |
| `paper/INTEGRITY_PRE_REVIEW.md` | `b5ba58d5f0c55ada0be179a1a8eea5516abcf79465f71f5603ae013735c53945` | MATCH |
| `PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | MATCH |
| proof-only manuscript lock | `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb` | MATCH |
| independent proof-only handoff review | `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711` | MATCH |
| asset review R2 | `7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404` | MATCH |

I also recomputed the complete integrity-root digests for the source support files and locked build artifacts. They matched the integrity record, including `math_commands.tex`, `references.bib`, `paper_pre_review.pdf`, `manuscript.{log,blg,bbl,aux,out}`, `PAPER_CONFIGURATION.md`, `CLAIM_MANIFEST.json`, `PROOF_ONLY_PASSPORT.json`, `FIGURE_PACKAGE.json`, `PLAGIARISM_MANIFEST.json`, `PIPELINE_STATE.json`, and `AUTHOR_PRE_REVIEW_AUDIT.md`. The pre-review PDF is byte-identical to the manuscript PDF, and no `paper_final.pdf` was present.

## Finding inventory

### M1 — Literal `quad` text appears inside Eqs. (44)–(45)

- **Severity:** Minor
- **Typed evidence anchor:** equation — PDF p. 12, Eqs. (44)–(45); source — `manuscript.tex` lines 867, 869, and 882–884.
- **Direct evidence:** seven instances use bare `quad` rather than `\quad`. The PDF consequently prints such strings as `s_d=j,quad T_d=0` and prints further `quad` tokens in the incoming-flow assignments.
- **Impact:** the intended equalities remain unambiguous and the transfer-flow proof is not altered, but literal command text degrades mathematical typography and readability at a central proof step.
- **Minimum repair:** replace precisely those seven bare instances by `\quad`; do not change the surrounding mathematics. Then run the complete bibliography build, check that no literal `quad` remains in PDF text, visually inspect p. 12, and refresh affected artifact hashes.
- **Confidence:** 5/5 — direct source and rendered-PDF inspection, independently corroborated by the QA shadow.

No other finding met the threshold for a Critical, Major, or Minor item. In particular, stylistic preferences, intentionally bounded claims, and already-disclosed open problems were not converted into artificial findings.

## ARS multi-perspective review

### 1. Journal and criteria view

Because `criteria_binding_unavailable`, venue-specific fit is not assessable. Against general specialist-mathematics criteria, the manuscript has a sharply scoped question, a nontrivial exact theorem, a self-contained proof, clear category restrictions, and unusually explicit nonclaims. The contribution is appropriately presented as a proof-only separation result rather than as a computational discovery or universal classification. The bounded historical-originality language is responsible: it does not claim a certified priority search.

The manuscript is technically publishable after M1. No venue-specific acceptance claim is made.

### 2. Methodology view

The proof architecture is coherent from formal fixed-point algebras through cyclic residues, weight elimination, Laurent coefficient extraction, transfer configurations, the quartic base case, and the local-length conversion. The hypotheses used by the residue identities and quotient-algebra arguments are stated. The separation between raw trace, exact-period subtraction, and cyclewise normalization is maintained.

The central all-degree result is a two-term structural law with odd \(C_m=0\) and an explicit integer certificate \(D_m\). The paper does **not** infer universal \(D_m\ne0\): that assertion remains explicitly OPEN. This is the correct logical boundary. The quartic computation proves only the nonzero base case needed for the stated minimality result.

There are no empirical statistics to reproduce; all evidentiary claims are exact symbolic statements. The independently checked arithmetic and combinatorics are recorded below.

### 3. Domain view

The manuscript correctly distinguishes a nilpotent trace correction from the zero function and distinguishes the formal fixed-point spectrum from a reduced-point evaluation. It also restricts the conjugacy statement to normalized Hénon form and handles the centered translation obstruction, avoiding an overclaim about arbitrary polynomial conjugacies.

The bibliography contains 11 entries, of which 10 are cited. The citations have identifiable roles: polynomial-automorphism normal form, residue/trace machinery, and the lower-period background for the selected family. The one unused entry is harmless. The paper's novelty statement is narrow and explicitly bounded rather than a certified global priority claim.

### 4. Perspective, clarity, and standalone-evidence view

The paper is standalone: the definitions, theorem statements, coefficient formula, base-case calculation, local multiplicity lemma, and scope limitations needed to assess the result are all in the manuscript. The proof does not ask the reader to trust external code or an opaque computed output. Figures 1–3 are legible and support the evidence-firewall, period-sensitivity, and proof-flow narratives without functioning as substitutes for proof.

The presentation is generally clear for a specialist reader. The sole actionable clarity defect is M1. The manuscript's explicit record of a failed registered route is appropriately quarantined as provenance and is never promoted to proof evidence.

### 5. Devil's-advocate view and adjudication

The strongest plausible attack is that the compressed Step 9 transfer-flow classification may omit admissible tuples, especially the \(j=0\) boundary, and that finite \(Q/R\) or high-index checks might have silently filled that gap. I reconstructed the recurrence from its base cases, the Laurent coefficient extraction, admissible tuple constraints, Eq. (9.14), the distinguished-coordinate bijection, and the separate \(j=0\) enumeration. The cases close symbolically; neither finite diagnostics nor registered computation is needed.

A second strong attack is category drift: treating a nilpotent class as zero, or turning normalized-form conjugacy into unrestricted conjugacy. The manuscript avoids both. A third is overclaiming the certificate as universal nonvanishing. The manuscript explicitly leaves \(D_m\ne0\) OPEN and uses only \(D_2\ne0\) for the quartic conclusion.

`da_critical_adjudications: []`

No devil's-advocate challenge survived as a Critical or Major finding. M1 survives only as a production-level Minor item.

### 6. Editorial synthesis

All substantive views converge: the theorem is scoped correctly, the symbolic proof chain closes, the quartic base case is independently reproducible, and the evidence firewall is respected. The absence of a target venue prevents a venue-fit judgment, and the same-model-family caveat limits claims of review independence. Neither limitation creates a manuscript defect. The only required revision is the exact typography repair M1, so the proportionate decision is MINOR REVISION.

## Claim-by-claim mathematical coverage receipt

The full 1,419-line manuscript and the full 1,639-line proof package were read. Every claim in the claim manifest was independently checked.

| ID | Manuscript evidence anchor | Independent check | Result |
|---|---|---|---|
| C1 | pp. 3–4, Sec. 3; source lines 216–229 | Field, characteristic-zero, and algebraic-closure conventions are explicit and sufficient for the later divisions and multiplicity arguments. | PASS |
| C2 | p. 5, Eq. (9); lines 334–355 | \(B_1=k[x]/((x^m-a)^2)\), \(q^2=0\), and multiplication by \(q\) has formal spectrum \(0^{\times 2m}\); this does not assert \(q=0\). | PASS |
| C3 | p. 5, Eq. (10); lines 357–375 | On the period-two quotient, the trace is \(2+q(x)q(y)\); the correction is nilpotent, hence the fixed exact-period formal spectrum follows. | PASS |
| C4 | pp. 5–6, Eq. (11); lines 377–401 | Normalized-form conjugacy is equivalent to equality of \(a^{2m-1}\); the diagonal action, gcd converse, and centered-translation removal close the “iff.” | PASS |
| C5 | p. 6, Eqs. (12)–(13); lines 406–432 | The cyclic period-three equations, Jacobian convention, and trace polynomial \(t\) are consistent. | PASS |
| C6 | p. 6, Eq. (14); lines 434–449 | The monic leading terms give a free quotient of rank \((2m)^3\); the projective leading equations exclude points at infinity. | PASS |
| C7 | p. 6, Eqs. (15)–(17); lines 451–469 | Euler–Jacobi/global residue and the top normal-form coefficient recover the raw moment with the claimed sign and degree. | PASS |
| C8 | p. 7, Eq. (18); lines 474–497 | Weight and exponent constraints leave exactly the displayed four raw monomial candidates. | PASS |
| C9 | p. 7 after Eq. (18); lines 499–518 | At \(\varepsilon=0\), the moment vanishes, eliminating the constant candidate without computational evidence. | PASS |
| C10 | pp. 7–8, Eqs. (19)–(21); lines 520–574 | Puiseux valuation analysis eliminates the \(a^{2\nu}\varepsilon^m\) term in the three root-collision patterns; the fixed diagonal is treated separately. | PASS |
| C11 | pp. 7–8, Eqs. (4), (18)–(21); lines 488–574 | Reversal symmetry forces evenness in \(\varepsilon\), and the weight system gives the two-term law with odd \(C_m=0\). | PASS |
| C12 | p. 8, final paragraph of Sec. 6; lines 576–579 | Exact-period subtraction leaves only the fixed contribution because the formal period-two contribution is zero. | PASS |
| C13 | pp. 8–13, Sec. 7, Eqs. (22)–(55) | Recurrence/base cases, Laurent extraction, admissible tuples, Eq. (9.14), transfer flow, signs, factorials, and independent \(j=0\) cases yield the stated integer certificate. M1 affects typography only. | PASS |
| C14 | p. 16, Lemma 9.1 | At fixed points \(t=q^3+3\varepsilon^2q\), and its \(m\)-th power vanishes in the fixed algebra for \(m\ge2\). | PASS |
| C15 | p. 14, Sec. 8 | The quartic full-fiber condition forces multiple-root partitions \(4\) or \(2+2\), hence uniquely \(p=(x^2-L)^2\). | PASS |
| C16 | pp. 14–16, Eqs. (56)–(63) | Independent evaluation gives \(H(2,1)=2\), \(A_{2,2}=-2\), \(A_{2,1}=0\), so \(D_2=-1572864\); the constant term is \(-1296000\). | PASS |
| C17 | p. 17, Lemma 9.2 and Eqs. (64)–(66) | Local formal elimination gives length \(r\) at a root of multiplicity \(r\); total period-three length is \(64-4=60\), with division by 3 for cyclewise moments. | PASS |
| C18 | p. 17, Sec. 9 and Eq. (66) | In normalized quartic coordinates, lower periods are blind to \(L^3\) while the period-three cyclewise moment has nonzero slope \(-1572864\). | PASS |
| PC1 | Theorem 3.1, pp. 4–5; proof in Secs. 8–9 | The normalized quartic minimality/separation statement follows from C4 and C14–C18, including length 60 and the cyclewise normalization. | PASS |
| PC2 | Theorem 3.2, p. 4; proof in Secs. 6–7 | The all-degree two-term law and explicit integer certificate are proved. Universal nonvanishing \(D_m\ne0\) remains OPEN and is not claimed. | PASS |

## High-risk proof-step receipt

### Step 7 — Puiseux elimination

I checked all boundary patterns used to exclude the \(a^{2\nu}\varepsilon^m\) coefficient: three distinct limiting roots give \(q\)-valuation \(1/2\); the exactly-two-equal pattern gives the claimed stronger valuation; the all-equal nontrivial branch has \(r\ge1\) and \(t\ge3\). The fixed diagonal is separated from the Puiseux branches. No hidden inference from a reduced fiber is made.

### Step 9 — recurrence to certificate

The recurrence terminates by total degree from the stated base cases. Laurent coefficient extraction makes the expansion order independent. The admissible tuple constraints reproduce the coefficient ranges and signs. The local coefficient identity corresponding to Eq. (9.14) was checked directly. For \(j\ge1\), the congruence and \(z\)-sum give one distinguished coordinate and a bijective incoming-transfer parametrization. The \(j=0\) cases \((0,m,m)\) and \((0,0,2m)\) were enumerated independently; the exceptional factor vanishes as stated. These cases collapse to the displayed \(D_m\) certificate without \(Q/R\) agreement or finite-index supplementation.

### Step 10 — exact-period subtraction

The fixed-point contribution vanishes in the nonreduced fixed algebra because the trace representative is \(q^3+3\varepsilon^2q\) with \(q^2=0\). The period-two contribution is formally zero. Therefore the raw and exact period-three moments agree for the stated power.

### Step 12 — quartic base case

The independent finite sum gives \(D_2=-1572864\), and the constant ledger gives \(-1296000\). Thus
\[
M_{3,2}^{\mathrm{ex}}=-1296000-1572864L^3.
\]
This is an exact paper-and-pencil reconstruction, not recovery of a candidate or run output.

### Step 13 — local lengths and cyclewise conversion

The formal implicit elimination at a root of multiplicity \(r\) produces local length \(r\). The full quartic cyclic fiber has length 64, the fixed diagonal contributes length 4, and the exact period-three part has length 60. Each exact period-three orbit appears at its three marked points, so the cyclewise moment is the pointwise moment divided by 3.

## Adversarial boundary-stress receipt

| Stress case | Question tested | Outcome |
|---|---|---|
| Nilpotent versus zero | Does the proof ever identify a nonzero nilpotent trace class with the zero function? | No; only its formal spectrum/power consequences are used. |
| \(a=0\) and \(a\ne0\) | Are degenerate and generic parameter fibers conflated? | No; the formal quotient and Puiseux cases cover the relevant boundaries. |
| Odd versus even \(m\) | Is the parity cancellation stated too strongly? | No; reversal symmetry gives odd \(C_m=0\), while the two-term law remains valid. |
| Minimal degree \(m=2\) | Do factorial ranges or exceptional cases break at the endpoint? | No; the ranges specialize consistently and give the checked quartic constants. |
| \(j=0\) | Is the transfer argument illegitimately reused when there is no distinguished coordinate? | No; the two \(j=0\) patterns are treated separately. |
| Raw/exact/cyclewise | Are the three normalizations mixed? | No; fixed/period-two subtraction and the final factor of 3 are explicit. |
| Conjugacy category | Is an unrestricted polynomial-conjugacy conclusion claimed? | No; the theorem is explicitly for normalized Hénon form, with an iff in that category. |
| Certificate boundary | Is the observed quartic nonvanishing generalized to all \(m\)? | No; universal \(D_m\ne0\) is explicitly OPEN. |

## Build, PDF, bibliography, and asset QA receipt

Two isolated builds were run from clean copied source trees using the explicit sequence

`pdflatex -> bibtex -> pdflatex -> pdflatex`

with a fixed `SOURCE_DATE_EPOCH`. Their PDF, log, BLG, BBL, AUX, and OUT files were pairwise byte-identical. The rebuilt PDF hash was exactly the frozen PDF hash. The BBL, BLG, AUX, and OUT matched their locked counterparts. The only locked-log byte difference was a non-substantive engine/header setting in the historical log; the isolated logs agreed with each other and contained no warning-state difference.

| Check | Independent result |
|---|---|
| Page count and geometry | 19 pages, letter size; PASS |
| Visual inspection | All 19 pages inspected; no clipping, overlap, missing glyphs, or broken cross-references; M1 was the sole visual defect |
| Figures | Three figures, visibly checked on pp. 3, 7, and 9; legible and properly placed |
| Bibliography | 11 BibTeX records, 10 cited and 10 emitted in the BBL; no undefined citations |
| Labels/references | 91 labels and 43 reference commands; no undefined references |
| Fonts | 38 reported font rows; all embedded, subset, and Unicode-mapped; no Type 3 fonts |
| Raster content | None reported by PDF image inspection |
| Compile diagnostics | No LaTeX warnings, overfull/underfull boxes, undefined references/citations, or BibTeX warnings |
| PDF metadata | Unencrypted; blank author/title/subject/keywords; anonymous production metadata |
| Source anonymity | `Anonymous` author; no identifying author metadata found |
| Standalone evidence | PASS; theorem proof does not depend on code, candidate runs, or inaccessible results |
| Originality posture | PASS for the manuscript's deliberately bounded novelty statement; no global priority certification is claimed |

The QA shadow independently reported the same package/build/PDF/bibliography/label/font/figure/anonymity/standalone/provenance results and the same sole Minor `quad` defect. Its imprecise phrase suggesting “all-degree nonvanishing” is expressly rejected here: the manuscript correctly leaves universal \(D_m\ne0\) OPEN.

## Required revision and closure condition

1. Replace the seven bare `quad` instances at `manuscript.tex` lines 867, 869, and 882–884 with `\quad`, without altering the equations.
2. Rebuild with the full `pdflatex -> bibtex -> pdflatex -> pdflatex` sequence.
3. Confirm by source search, PDF text extraction, and visual inspection of p. 12 that no literal `quad` remains.
4. Re-run warning, font, bibliography, label/reference, and deterministic-build checks, then refresh all affected hashes and locks according to the project's integrity procedure.

Once those mechanical checks pass, this Round 1 decision can close as an accepted minor revision without reopening the scientific proof, provided the diff is confined to the seven command corrections and expected regenerated artifacts. Until then, the signed state remains **MINOR REVISION — `DO_NOT_FINALIZE`**.
