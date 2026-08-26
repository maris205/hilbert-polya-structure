# P70 Stage 2.5 integrity and priority audit

Audit date: **2026-08-26 UTC**  
Manuscript: *Weighted Three-Term Shifts on Finite Heisenberg Quotients*  
Audit posture: author-side integrity and search-bounded priority audit, not independent specialist certification  
External state: **HOLD**

## 1. Executive verdict

**Overall Stage 2.5 release-gate verdict: FAIL.**

This is a source-ownership and declaration failure at the external-release gate, not
a finding that the theorem is false. The quotient reduction, right-convolution
convention, cross-characteristic regular-representation decomposition, character gcd
term, clock--shift determinant, singular-block corank-one lemma, and final nullity
formula form a coherent argument. All five existing bibliography records are real
and field-verified; all ten citation contexts are substantively supported; no ghost,
dangling key, unresolved compiled citation, table discrepancy, or control-output
discrepancy was found. A fresh deterministic replay was byte-identical to the frozen
receipt.

External release is nevertheless blocked because the current ownership discussion
omits two material direct neighbors:

1. Deundyak--Leonov (2016) explicitly develop left/right convolution, irreducible
   Fourier blocks, FFT, and an equation-solving algorithm on the finite Heisenberg
   group over a prime field. They do not state P70's weighted cross-characteristic
   kernel-dimension formula, but they own a direct finite-Heisenberg convolution
   framework that must be cited and subtracted.
2. Grassberger--Hörmann (2001) explicitly classify finite-Heisenberg irreducible
   representations and is a closer owner of the finite-group representation ledger
   than the current quantization reference alone.

Author identity/order, final contributions, funding, competing interests, and a
specific author-approved AI/tool disclosure also remain unresolved. The exact-formula
search found no collision only within the recorded public-Web queries through
2026-08-26. Collision risk is **MEDIUM-HIGH**. No worldwide novelty or priority
certificate is issued.

| Axis | Decision |
|---|---|
| Mathematical/proof consistency | PASS within this audit |
| Existing-reference authenticity | PASS (5/5) |
| Citation-context fidelity | PASS (10/10) |
| Numerical/control integrity | PASS as proof-regression controls |
| Paragraph-overlap screen | PASS_WITH_TOOL_LIMITATIONS |
| Priority framing | FAIL_PENDING_DIRECT_OWNER_SUBTRACTION |
| Declarations | UNRESOLVED |
| Overall Stage 2.5 release gate | **FAIL** |
| External release | **HOLD** |

## 2. Scope, immutability, and protocol coverage

No manuscript source, bibliography, control source, frozen output, or PDF was edited
during this audit. Work was confined to `stage2_5/`; the pre-existing generated
claim-registry artifacts were preserved. Baseline fingerprints were:

| File | SHA-256 |
|---|---|
| `main.tex` | `dee658d7259b0aa69d2255293d87336b54def9c8ed2a47962326e16b3236c984` |
| `references.bib` | `a3e0cfa339eaaa8a20d61b9fe4338f0385ad6c982f8be49c11fb5c2773d3b0cc` |
| `sections/0_abstract.tex` | `a6033f7aa0c5011c908774a7571fe63bcfc797647cb74cb35478d56d18dc023f` |
| `sections/1_introduction.tex` | `1386879d4d4db2516e23894b1767cdd303c5fdd8b21b4db9588d334db8bca9df` |
| `sections/2_setup.tex` | `b8493ccd45ca47c7db60ffc2b51aa4fd75280fe8217c74ac3b8d8d2d3871df3c` |
| `sections/3_regular_decomposition.tex` | `22ef5a3a3752bae4caa84bbf9a970c2528d5b5579a033b6e87e65cf38985ab63` |
| `sections/4_character_blocks.tex` | `c8d61605d29ad8088a4e2e1b810f601baa63dbbd8017fba155a74ea369fc24ca` |
| `sections/5_nonlinear_blocks.tex` | `2f155b982f889596dab9eb534e6f136c2bdb1136a5da04d37060d33e4b01ba3b` |
| `sections/6_phase_diagram_controls.tex` | `2e84e4ccf221ea72513e2df347ab48edd77f2fb5053b560af590f8fc9d8cea4d` |
| `sections/7_scope_declarations.tex` | `90d603174bd3d4b36dc0dd126db6aad56c1937df30b51de2308c06cfbc8d77ef` |
| `sections/8_conclusion.tex` | `c9aafb509c32e860c2229a7b47f5150635cab52efdeddbee0994cff2210a64ed` |

Protocol coverage:

| Phase | Required surface | Audited surface | Status |
|---|---|---|---|
| A | 100% bibliography entries and fields | 5/5 entries; every supplied field | 5 VERIFIED, 0 MISMATCH, 0 NOT_FOUND |
| B | at least 30% citation contexts | 10/10 citation commands, 100%, against abstracts/original texts | PASS |
| C | all tables, numbers, code/enumeration assertions and receipts | both manuscript tables, all formulas used numerically, four block cases, ten full-quotient cases, frozen output | PASS; proof-regression only |
| D | at least 30% body paragraphs and one per major section | 13/41 = 31.71%; Sections 1--8 all represented | PASS_WITH_TOOL_LIMITATIONS |
| E | all HIGH-IMPACT plus at least `min(10,total)` | all 18 semantically identified claim families | PASS_WITH_SOURCE_NOTES |

For Phase E, `semantic completeness=not_machine_detectable`. Semantic claim
extraction cannot certify that no implicit proposition was missed. All 18 identified
claim families were audited rather than only the protocol minimum of ten.

## 3. Phases A and B — source authenticity and citation fidelity

The complete query strings, direct authoritative URLs, field-by-field decisions,
key-set comparison, and all ten context checks are in
[`SOURCE_SEARCH_LEDGER.md`](SOURCE_SEARCH_LEDGER.md).

### A. Bibliography result

All five current entries are **VERIFIED**:

- Lind--Schmidt, [publisher record](https://www.mathnet.ru/eng/rm9658),
  [arXiv](https://arxiv.org/abs/1502.06243),
  [DOI](https://doi.org/10.1070/RM2015v070n04ABEH004957);
- Göll--Schmidt--Verbitskiy,
  [arXiv](https://arxiv.org/abs/1312.2469),
  [DOI](https://doi.org/10.1016/j.indag.2014.04.007);
- Gurevich--Hadani, [arXiv](https://arxiv.org/abs/0708.0669),
  [DOI](https://doi.org/10.1007/978-0-8176-4831-2_8);
- Zaidenberg, [arXiv](https://arxiv.org/abs/math-ph/0606070),
  [original preprint](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2006/67.pdf);
- Ford--Jha, [publisher](https://www.tandfonline.com/doi/abs/10.1080/10586458.1993.10504271),
  [DOI](https://doi.org/10.1080/10586458.1993.10504271).

No item reached `MISMATCH` or `NOT_FOUND`, so the three-query failure rule was not
invoked.

### B. Key and context result

- unique cited keys: 5;
- unique bibliography keys: 5;
- dangling in-text keys: 0;
- uncited bibliography entries: 0;
- ghost works: 0;
- citation commands checked against content: 10/10 (100%);
- substantively unsupported contexts: 0.

Original-text/abstract inspection supports the manuscript's statements about
positive-characteristic lattice convolution and torsion points, Wendt's resultant and
Fermat curves, principal Heisenberg actions and the exact element `1+a+b`, and finite
Stone--von Neumann theory. The source-validity pass does not cure the newly discovered
direct-neighbor omissions described in Sections 7 and 10 below.

## 4. Phase C — proof, table, and proof-regression consistency

### C1. Classification and deterministic replay

P70 reports no empirical experiment, dataset, estimated statistic, fitted parameter,
random sample, or numerical approximation. `code/verify_weighted_heisenberg.py` is a
deterministic exact modular-linear-algebra **proof-regression control**. It evaluates
selected finite cases of a theorem whose general proof is representation-theoretic.

Replay command:

```bash
python3 code/verify_weighted_heisenberg.py
```

Audit-time receipt:

| Artifact | SHA-256 | Comparison |
|---|---|---|
| `code/verify_weighted_heisenberg.py` | `a476ddddca2d9373c1412039e86dac64457354740e530ff3e20ab7ade4e5b1e1` | source fingerprint |
| fresh stdout | `fe26d12a4fd332b87027db685563980b788fb097bd633dc974b091de0bc2f42f` | reference replay |
| `code/verification_output.txt` | `fe26d12a4fd332b87027db685563980b788fb097bd633dc974b091de0bc2f42f` | byte-identical |

The fresh final line was `ALL WEIGHTED HEISENBERG CONTROLS PASS`.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

Here “experiment” in the required C4 sentence has no manuscript referent: P70 reports
only finite exact proof-regression checks.

### C2. Complete code/output/manuscript traceability

| Assertion | Code locator | Frozen/output evidence | Manuscript/package locator | Verdict |
|---|---|---|---|---|
| finite Heisenberg multiplication used to assemble quotient matrices | `code/verify_weighted_heisenberg.py:132-156` | all ten full matrices built from the displayed law | `sections/2_setup.tex:3-34` | PASS |
| clock--shift block `alpha I+beta U+gamma V` | code lines 62-83 | four direct blocks | `sections/3_regular_decomposition.tex:30-66`; `sections/5_nonlinear_blocks.tex:3-12` | PASS |
| determinant equals `alpha^ell+beta^ell+gamma^ell` in the four direct blocks | code lines 86-98 | first receipt line PASS | `sections/5_nonlinear_blocks.tex:12-33` | PASS_WITH_FINITE_SCOPE |
| singular clock--shift block has nullity exactly one | code lines 86-98 | on-locus blocks have nullity one, off-locus zero | `sections/5_nonlinear_blocks.tex:35-54` | PASS_WITH_FINITE_SCOPE |
| character contribution is the cyclotomic gcd degree | code lines 101-129,159-180 | recomputed in every full case | `sections/4_character_blocks.tex:3-42` | PASS_WITH_FINITE_SCOPE |
| nonlinear contribution is `ell(ell-1)` exactly on the Fermat locus | code lines 169-180 | full-case expected formula | `sections/2_setup.tex:48-79`; `sections/6_phase_diagram_controls.tex:3-37` | PASS |
| full right-convolution matrix nullity equals theorem formula | code lines 140-156,183-208 | ten listed PASS rows | `sections/2_setup.tex:17-58`; `CONTROL_RESULTS.md:9-26` | PASS_WITH_FINITE_SCOPE |
| manuscript seven-row control table | cases at code lines 188-198 | exact rows shown below | `sections/6_phase_diagram_controls.tex:49-66` | PASS |
| left/right convention scope | matrix uses `g*step`, code lines 150-155 | same total nullity under inversion/transposition, but no entrywise convention comparison | `sections/3_regular_decomposition.tex:68-112`; `sections/6_phase_diagram_controls.tex:69-76` | PASS_WITH_STATED_LIMIT |
| block ledger dimension | formula, not loop-derived | `ell^2` characters plus `ell-1` types of degree `ell`, regular multiplicity equals degree | `sections/2_setup.tex:65-79`; `sections/3_regular_decomposition.tex:24-102` | PASS |

The seven displayed table rows exactly match the frozen output:

| `ell` | `p` | coefficients | manuscript stratum | observed nullity | Formula/control verdict |
|---:|---:|---|---|---:|---|
| 3 | 2 | `(1,1,1)` | nonsingular | 2 | PASS |
| 3 | 5 | `(1,1,2)` | singular | 6 | PASS |
| 3 | 5 | `(1,2,3)` | nonsingular | 0 | PASS |
| 3 | 7 | `(2,3,4)` | nonsingular | 1 | PASS |
| 5 | 3 | `(1,1,1)` | singular | 21 | PASS |
| 5 | 11 | `(1,1,1)` | nonsingular | 3 | PASS |
| 5 | 11 | `(2,3,5)` | nonsingular | 2 | PASS |

The frozen output additionally checks `(ell,p,weights)=(3,5,(1,1,1))`,
`(5,2,(1,1,1))`, and `(5,7,(1,2,3))`, for ten full-quotient cases total, plus four
direct clock--shift blocks. Every coefficient tuple satisfies the theorem's nonzero
weight requirement.

### C3. Convention boundary

The manuscript correctly derives a right-convolution kernel from the stated left
shift and normal quotient (`sections/2_setup.tex:17-34`). The finite matrix in the
script uses `g*step`, matching that right-convolution convention. The proof also
explains that inversion relates left and right regular actions and preserves total
nullity (`sections/3_regular_decomposition.tex:103-112`).

This has an important evidentiary consequence: a **nullity-only** comparison of the
full matrices with the closed formula cannot by itself detect every left/right
convention error, because left and right convolution have the same total nullity
under inversion/transposition. It can detect many formula, group-law, coefficient,
rank, and implementation errors. Convention correctness here rests on the explicit
entrywise derivation plus inspection of the matrix assembly, not on nullity equality
alone. The current prose acknowledges that boundary, so no new overclaim was found.

### C4. Main proof-chain audit

1. **Finite reduction.** `N_ell`-fixed configurations descend to the normal finite
   quotient and the local relation becomes the displayed right-convolution operator
   (`sections/2_setup.tex:17-34`).
2. **Semisimple transfer.** Since `p != ell`, scalar extension to a splitting field
   preserves kernel dimension and Maschke semisimplicity applies
   (`sections/3_regular_decomposition.tex:3-16`).
3. **Irreducible ledger.** There are `ell^2` characters and `ell-1` nonlinear
   degree-`ell` types, with regular multiplicity equal to degree; the dimension sum
   is `ell^2 + (ell-1)ell^2 = ell^3`
   (`sections/3_regular_decomposition.tex:24-102`).
4. **Character blocks.** Simultaneous evaluation over all torsion characters equals
   the stated polynomial gcd degree (`sections/4_character_blocks.tex:3-31`).
5. **Nonlinear determinant.** The cyclic recurrence gives
   `det(alpha I+beta U+gamma V)=alpha^ell+beta^ell+gamma^ell`
   (`sections/5_nonlinear_blocks.tex:3-33`).
6. **Exact nullity.** Nonzero coefficients make the recurrence first-order, so every
   singular nonlinear block has one-dimensional kernel, not merely zero determinant
   (`sections/5_nonlinear_blocks.tex:35-54`).
7. **Summation.** Multiplicity `ell` across `ell-1` nonlinear types gives the exact
   `ell(ell-1)` jump on the Fermat locus, added to the character gcd degree
   (`sections/2_setup.tex:48-79`; `sections/6_phase_diagram_controls.tex:3-37`).

No theorem step was found to depend on the finite control. This remains an audit
finding, not external specialist refereeing.

## 5. Phase D — paragraph overlap and author-overlap screen

### D1. Sampling rule and coverage

A body paragraph was defined as a blank-line-delimited LaTeX narrative block after
removing comments and command-only lines, with at least 20 alphabetic tokens. Counts
were: Introduction 6, Setup 5, Regular decomposition 9, Character blocks 3,
Nonlinear blocks 4, Phase diagram/controls 7, Scope/declarations 5, Conclusion 2;
total **41**. The sample is **13/41 = 31.71%** and includes at least one paragraph
from each major section. Each query used an exact 8--12-word phrase.

`NO_EXACT_MATCH_IN_INDEXED_WEB` means that the quoted phrase did not appear in an
inspected public indexed result. It is not an originality finding.

| # | Section and locator | Exact 8--12-word query | Search result |
|---:|---|---|---|
| 1 | `sections/1_introduction.tex:3-10` | “Periodic configurations convert an infinite symbolic constraint into a finite linear problem” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 2 | introduction 31-33 | “The answer has two qualitatively different pieces The one-dimensional representations behave” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 3 | `sections/2_setup.tex:17-25` | “This is a closed shift-invariant linear group shift” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 4 | setup 60-63 | “Their different scales are essential the character term is at most” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 5 | `sections/3_regular_decomposition.tex:3-4` | “We first remove a possible field splitting ambiguity” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 6 | regular decomposition 49-57 | “Distinct values give inequivalent modules because the center acts by different scalars” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 7 | `sections/4_character_blocks.tex:3-5` | “The following calculation identifies it over the ground field” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 8 | `sections/5_nonlinear_blocks.tex:3-10` | “Changing the central character only replaces zeta by another primitive root” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 9 | nonlinear blocks 35-36 | “A determinant alone would not determine the fixed-space dimension” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 10 | `sections/6_phase_diagram_controls.tex:3-5` | “The family therefore lives naturally in the projective coefficient plane” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 11 | phase diagram/controls 69-76 | “They can expose many transcription or implementation mistakes including an omitted” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 12 | `sections/7_scope_declarations.tex:12-19` | “Degenerate two-term rules admit separate elementary case splits but are outside” | NO_EXACT_MATCH_IN_INDEXED_WEB |
| 13 | `sections/8_conclusion.tex:11-14` | “The excluded modular case is the next concrete problem” | NO_EXACT_MATCH_IN_INDEXED_WEB |

Representative surfaced pages were unrelated rather than phrase matches, including
an unrelated [machine-learning research post](https://research.iaifi.org/posts/decomposing-the-dark-matter-of-sparse-autoencoders/),
an unrelated [IMRN article](https://academic.oup.com/imrn/article/2022/21/17112/6344682),
and a generic [Project Gutenberg text](https://gutenberg.org/cache/epub/16713/pg16713-images.html).
They are recorded only to make the result classification auditable.

### D2. Author-overlap status

`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`

The manuscript says only “Anonymous,” so no responsible author set exists against
which to run author-publication overlap.

### D3. Tool limitation statement

This screen used general public-Web indexing, not Turnitin, iThenticate, Crossref
Similarity Check, subscription full-text databases, or a complete historical archive.
Exact-string search can miss paywalls, nonindexed works, mathematical/TeX and OCR
normalization, paraphrase, translation, and alternate terminology. Rankings can
change after the freeze date. The 31.71% sample is not exhaustive, and AI-text or
plagiarism detectors have both false positives and false negatives. Phase D cannot
certify originality.

## 6. Phase E — semantic claim registry and evidence decisions

The table treats contiguous formula/proof units as semantic claims. All 18 identified
claims were audited, including every HIGH claim; the protocol floor is
`min(10,total)=10`. `semantic completeness=not_machine_detectable`.

| ID | Impact | Claim and exact locator | Source/provenance checked | Verdict |
|---|---|---|---|---|
| P70-E01 | HIGH | closed shift and `N_ell`-fixed quotient reduction, `sections/2_setup.tex:17-34` | direct left-shift/right-convolution derivation | VERIFIED_INTERNAL |
| P70-E02 | HIGH | exact main fixed-dimension formula, setup 48-58 | E03--E10 proof chain and exact controls | VERIFIED_INTERNAL |
| P70-E03 | HIGH | character/nonlinear scale and block ledger, setup 60-79 | irreducible count and regular multiplicities | VERIFIED_INTERNAL_WITH_MISSING_DIRECT_OWNER |
| P70-E04 | HIGH | scalar extension preserves nullity and supplies a splitting field, `sections/3_regular_decomposition.tex:3-16` | rank invariance and Maschke argument | VERIFIED_INTERNAL |
| P70-E05 | HIGH | `ell^2` characters plus `ell-1` degree-`ell` irreducibles, regular decomposition 24-66 | direct construction; [Gurevich--Hadani](https://arxiv.org/abs/0708.0669); missing [Grassberger--Hörmann](https://dmtcs.episciences.org/284) | VERIFIED_WITH_OWNER_GAP |
| P70-E06 | HIGH | right regular block multiplicity and left/right ledger, regular decomposition 68-112 | regular-module dimension identity and inversion map | VERIFIED_INTERNAL |
| P70-E07 | HIGH | character contribution equals the displayed cyclotomic gcd degree, `sections/4_character_blocks.tex:3-31` | torsion-character evaluation; control gcd implementation | VERIFIED_INTERNAL |
| P70-E08 | NORMAL | lattice torsion-point and Wendt context, character blocks 33-42 | [Zaidenberg](https://arxiv.org/abs/math-ph/0606070), [Ford--Jha](https://doi.org/10.1080/10586458.1993.10504271) | VERIFIED_EXTERNAL |
| P70-E09 | HIGH | clock--shift determinant is `alpha^ell+beta^ell+gamma^ell`, `sections/5_nonlinear_blocks.tex:12-33` | cyclic determinant argument and four finite blocks | VERIFIED_INTERNAL |
| P70-E10 | HIGH | every singular nonlinear block has exact nullity one, nonlinear blocks 35-54 | nonzero-coefficient recurrence | VERIFIED_INTERNAL |
| P70-E11 | HIGH | two-stratum coefficient-space phase diagram, `sections/6_phase_diagram_controls.tex:3-21` | E07, E09, E10 and regular multiplicities | VERIFIED_INTERNAL |
| P70-E12 | NORMAL | unit-weight characteristic-three specialization, phase diagram 23-37 | Fermat term plus character gcd | VERIFIED_INTERNAL |
| P70-E13 | NORMAL | four block and ten full-matrix controls agree with formula, phase diagram 39-76; `CONTROL_RESULTS.md` | byte-identical replay | VERIFIED_CONTROL_DISCLOSURE |
| P70-E14 | HIGH | left/right total nullities agree, but nullity-only controls do not certify convention, regular decomposition 103-112; phase diagram 69-76 | inversion/transposition argument and code inspection | VERIFIED_WITH_EXPLICIT_LIMIT |
| P70-E15 | NORMAL | algebraic Heisenberg-action framework and `1+a+b` predate P70, introduction 22-29; `sections/7_scope_declarations.tex:3-10` | [Göll--Schmidt--Verbitskiy](https://arxiv.org/abs/1312.2469), [Lind--Schmidt](https://www.mathnet.ru/eng/rm9658) | VERIFIED_EXTERNAL |
| P70-E16 | NORMAL | `p=ell`, zero weights, and dynamical invariants lie outside theorem, scope 12-19 | assumptions and semisimplicity boundary | VERIFIED_SCOPE |
| P70-E17 | HIGH | conclusion synthesizes gcd plus Fermat jump and isolates modular next case, `sections/8_conclusion.tex:3-14` | theorem and explicit limitation | VERIFIED_INTERNAL |
| P70-E18 | HIGH | bounded search found no exact weighted nullity collision, scope 8-10 | alternate-term search through 2026-08-26 | SUPPORTED_WITHIN_SEARCH_ONLY |

No mathematical headline claim depends solely on the script. P70-E13 is a receipt
claim. The direct-neighbor gap affects historical framing of E03, E05, E07, and the
method neighborhood; it does not supply a counterexample to E02.

## 7. Search-bounded priority audit and owner subtraction

The full query strings and direct source URLs are in
[`SOURCE_SEARCH_LEDGER.md`](SOURCE_SEARCH_LEDGER.md). At least three alternate-term
queries were run for every core progress family through 2026-08-26.

### 7.1 Nearest-neighbor map

| P70 surface | Nearest owner/source | Exact owner subtraction | Collision risk |
|---|---|---|---|
| principal algebraic actions of the discrete Heisenberg group and `1+a+b` | [Göll--Schmidt--Verbitskiy](https://arxiv.org/abs/1312.2469), [Lind--Schmidt](https://www.mathnet.ru/eng/rm9658) | principal-action, expansiveness/homoclinic, and exact integer-element setting are prior; P70 may claim only its finite weighted mod-`p` congruence-nullity theorem | MEDIUM |
| positive-characteristic abelian convolution/torsion intersections | [Zaidenberg](https://arxiv.org/abs/math-ph/0606070) | lattice Fourier/torsion-point method is prior; P70's residual character term is a finite-Heisenberg specialization and not standalone priority mass | MEDIUM |
| Wendt resultant/Fermat relation | [Ford--Jha](https://doi.org/10.1080/10586458.1993.10504271) | unit-weight resultant and Fermat connection are classical; P70 does not own that determinant family | MEDIUM |
| finite-Heisenberg representation ledger | [Gurevich--Hadani](https://arxiv.org/abs/0708.0669), [Grassberger--Hörmann](https://dmtcs.episciences.org/284) | Stone--von Neumann theory and explicit irreducible classification are prior; residual contribution is the cross-characteristic weighted kernel calculation and its exact summation | MEDIUM-HIGH |
| finite-Heisenberg convolution and Fourier solution | [Deundyak--Leonov publisher](https://vestnik.kubsu.ru/article/view/686), [original PDF](https://vestnik.kubsu.ru/article/download/686/1168/694) | left/right convolution, the character/nonlinear representation ledger, noncommutative FFT, and blockwise equation solving are prior. They do not give P70's `F_p` singular-nullity formula, cyclotomic degree plus Fermat jump, or corank-one theorem | HIGH adjacency |
| weighted clock--shift/Fermat jump | no exact public formula located | residual candidate mass is the exact weighted determinant plus corank-one statement in every nonlinear type and the total `ell(ell-1)` jump combined with the character gcd | MEDIUM-HIGH |

### 7.2 Direct-neighbor original-text findings

The original Deundyak--Leonov PDF, not just its metadata, was inspected. It defines
left and right convolution, lists `p^2` characters and `p-1` degree-`p`
representations of the finite Heisenberg group, builds forward/inverse FFTs, and
solves convolution equations by representation-block inversion. Its base field and
goal differ: it does not analyze P70's cross-characteristic `F_p` kernel dimensions
for quotient order `ell`, singular weighted three-term symbols, the cyclotomic gcd,
the Fermat-locus determinant, or the exact corank-one/full-jump formula. It is
nevertheless too close methodologically to omit.

Grassberger--Hörmann construct all irreducible representations of finite Heisenberg
groups `H(Z_n)` and count their classes. At prime `n=ell`, this specializes directly
to P70's character/nontrivial-central-character strata. The source does not compute
the weighted nullity but is a direct owner of the finite representation ledger.

### 7.3 Search conclusion

No inspected source stated the full conjunction of:

1. distinct primes `p != ell` with `ell` odd;
2. a nondegenerate weighted symbol `alpha + beta a + gamma b`;
3. the character contribution as the displayed cyclotomic gcd degree;
4. determinant `alpha^ell+beta^ell+gamma^ell` uniformly across nonlinear central
   characters;
5. exact singular-block corank one; and
6. the resulting full regular-representation jump `ell(ell-1)`.

The only permissible conclusion is:

`BOUNDED_NO_EXACT_WEIGHTED_NULLITY_COLLISION_LOCATED_AS_OF_2026-08-26`

Collision risk is **MEDIUM-HIGH**, because a general finite-Heisenberg convolution
solver already exists and the remaining matrix arguments are elementary after the
block model is chosen. Non-English, implicit, unpublished, or poorly indexed
derivations remain plausible. This is not a worldwide novelty or priority certificate.

## 8. Seven-mode AI failure checklist

| Failure mode | Evidence checked | Verdict |
|---|---|---|
| 1. Implementation bug | exact modular row reduction/determinant/gcd, finite-group law, case list, fresh replay and stored-output comparison | CLEAR_WITHIN_FINITE_CONTROL_SCOPE; convention needs proof inspection |
| 2. Hallucinated citation | 5/5 records and fields verified, 10/10 contexts checked, key-set comparison | CLEAR_FOR_CURRENT_BIBLIOGRAPHY; material omissions remain |
| 3. Hallucinated experimental result | no empirical experiment exists; all reported values are exact deterministic nullities | NOT_APPLICABLE_NO_EMPIRICAL_EXPERIMENTS |
| 4. Shortcut reliance | base change, representation ledger, determinant, recurrence nullity, and summation are proved independently of code | CLEAR_WITH_DISCLOSED_CONTROL_BOUNDARY |
| 5. Bug reframed as insight | table/output/formula agree; left/right nullity limitation is stated; no discrepancy marketed as discovery | CLEAR_WITHIN_AUDIT |
| 6. Methodology fabrication | definitions, proof chain, code and receipt exist; no statistical or empirical methodology is claimed | CLEAR_THEORETICAL_METHOD |
| 7. Frame-lock | searches included algebraic actions, lattice convolution, noncommutative FFT, finite-Heisenberg representations, Weyl/clock--shift matrices, Fermat resultants, torsion gcds | FAIL_RELEASE_FRAME_PENDING_DIRECT_NEIGHBOR_INTEGRATION |

## 9. Authorship, funding, COI, and AI disclosure

| Field | Current evidence | Audit status | Required action |
|---|---|---|---|
| Author identity/order/affiliations | `main.tex:37` says only “Anonymous” | UNRESOLVED | responsible researchers authorize final names/order/affiliations |
| Contributions / CRediT | `sections/7_scope_declarations.tex:30-34` explicitly says attribution must be replaced | UNRESOLVED | provide and approve final roles |
| Funding | internal sentence says no external funding, but no identified author has attested it | UNRESOLVED | identified authors verify grants/support or approve “none” |
| Competing interests / COI | internal sentence says none, but no identified author has attested it | UNRESOLVED | identified authors verify and approve final declaration |
| AI/tool assistance | generic tool-use paragraph at scope lines 40-43; no final author-approved model/role/extent record | UNRESOLVED | provide venue-compliant specific disclosure and human approval |
| Human/animal/personal data | purely mathematical content; none present | NO_PARTICIPANT_ETHICS_ISSUE_IDENTIFIED | retain accurate declaration if venue requires |
| D2 author-overlap | identities unavailable | `NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE` | rerun after author identification |
| External dissemination | internal HOLD | BLOCKED | no upload, contact, release, submission, or priority statement |

The internal negative funding/COI wording is not treated as independent evidence of
the authors' circumstances. Unknown fields remain unresolved rather than being
fabricated into passes.

## 10. Objective correction list and disposition

### Required before external release

1. Add V. M. Deundyak and D. A. Leonov, “FFT and Solving of Convolution Equations on
   Heisenber Group over Prime Galua Field,” 2016,
   [publisher record](https://vestnik.kubsu.ru/article/view/686) and
   [original PDF](https://vestnik.kubsu.ru/article/download/686/1168/694). Preserve
   the publisher's title spelling in metadata, and explicitly subtract its left/right
   convolution, finite-Heisenberg Fourier, representation-ledger, and block-solving
   ownership.
2. Add or explicitly justify the treatment of Johannes Grassberger and Günther
   Hörmann, “A Note on Representations of the Finite Heisenberg Group and Sums of
   Greatest Common Divisors,” [publisher](https://dmtcs.episciences.org/284),
   [DOI](https://doi.org/10.46298/dmtcs.284). State that explicit finite-Heisenberg
   irreducible classification is prior.
3. Keep the residual claim precise: P70's candidate contribution is the weighted
   cross-characteristic kernel-dimension formula, including the cyclotomic term,
   uniform nonlinear Fermat determinant, exact corank-one lemma, and regular
   `ell(ell-1)` jump. Do not claim the general convolution method, representation
   ledger, Wendt determinant, or algebraic-action setting.
4. Retain the left/right evidentiary boundary: nullity-only full-matrix checks verify
   the formula but cannot alone detect every convention reversal. Do not broaden the
   control claim without entrywise comparison tests.
5. Resolve author identity/order, contributions, funding, COI, and the AI/tool-use
   disclosure; then run D2 author-overlap screening.
6. Obtain specialist review in finite-group harmonic analysis/representation theory,
   algebraic actions, and finite-field convolution. Keep all novelty language bounded.
7. After source/declaration edits, rerun citation compilation, ghost/dangling checks,
   control/output comparison, PDF QA, and this Stage 2.5 audit against the new hashes
   and search-freeze date.

### No correction identified by this audit

- No change to the quotient reduction, main formula, base-change argument,
  irreducible dimension ledger, character gcd derivation, determinant identity,
  corank-one recurrence, or phase-stratum summation is required on the audited
  evidence.
- No current bibliography field requires repair; the bibliography needs augmentation.
- No stored control value or script branch requires correction.

### Final disposition

P70's mathematics is coherent within this audit, but its direct related-work
ownership and author-attested declaration record are not ready for external use.
Overall status remains **FAIL** at the Stage 2.5 release gate and **HOLD** externally
until the objective corrections are integrated and re-audited. No worldwide novelty
or priority certificate is issued.
