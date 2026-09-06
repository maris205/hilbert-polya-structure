# C403 independent internal manuscript review

Date: 2026-09-05. Reviewed title: *Regular-variation limits for nonmultiplicative divisibility Gram matrices*.

## Outcome and review provenance

**No blocking mathematical defect and no actionable minor defect found in the frozen manuscript.** Its statements and proofs preserve the original contract's hypotheses, full real-`q` range, and ownership boundaries. This is a bounded internal mathematical and citation review, not an editorial acceptance, target-route evaluation, global novelty certificate, or guarantee of correctness.

This reviewer did not author the C403 manuscript. The reviewer previously reviewed its proof package and has now read that earlier report, the author's claim/citation map, and the coordinator's disclosure that a typographical superscript comma had already been repaired. Thus this is a non-author review, **not a blind or fresh-error-process replication**. It uses the current team's model family; no external model call, paid API, accountable human review, or full ARS panel execution occurred. Calibration: `NOT_CALIBRATED`. Venue/track criteria were not supplied, so venue alignment is not assessed.

The research-review skill's evidence gathering, critical checking, and written handoff were used within the explicitly assigned internal-review scope; its legacy external-model and ML-experiment defaults were not invoked. ARS read-only integrity discipline and all seven AI-research failure modes were applied in the limited form recorded below. No author file, root state, evaluation record, or Git state was modified. No mathematical experiment or compilation was run.

## Exact material read and artifact binding

All twelve local TeX/Bib inputs were read in full: 944 lines, including all 845 lines of the nine section files. This includes the abstract, introduction/comparison table, classical inputs, every proof, examples, scope, and declarations, not just the theorem statements. Also read completely: `PROOF_PACKAGE.md` (260 lines), `SOURCE_AUDIT.md` (95 lines), the previous `SPECTRAL_REGULAR_VARIATION_REVIEW.md` (83 lines), `CITATION_AND_CLAIM_MAP.md` (56 lines), and `BIBLIOGRAPHY_CHECK.md` (86 lines).

The initial PDF identity was checked by hashing, not by recompiling. This report does not certify all-page PDF appearance or final build reproducibility.

| Artifact, relative to the batch directory | SHA256 |
| --- | --- |
| `spectral_regular_variation/paper/main.pdf` | `83ed1a84dffe7696596b31d3752c620e472a959afae4aed8faaee044379501fd` |
| `spectral_regular_variation/paper/SOURCE_SHA256SUMS.txt` | `46dc6bb27d5f7f66bc2d517893fefb1df472a57d64960fa1aba3ea63dc50e9dd` |
| `spectral_regular_variation/PROOF_PACKAGE.md` | `0f8e436657de4207087137502236b2d48f69dae947f368b5d586039b7a282fee` |
| `spectral_regular_variation/SOURCE_AUDIT.md` | `3f21874bdc23d8fe70fb7b0b15708a25782b3564750d8775e01908f0a139c64e` |
| `reviews/SPECTRAL_REGULAR_VARIATION_REVIEW.md` | `3c1de5f3a52d0e0249459343cab00329609fbad72c6a52e4190fb4464f9c0f10` |
| `spectral_regular_variation/paper/CITATION_AND_CLAIM_MAP.md` | `eedd652c2de1a0a463e232d664dc9e28e0a4bc385179240671808a02003027b0` |
| `spectral_regular_variation/paper/BIBLIOGRAPHY_CHECK.md` | `3d385e04e5de77050ca3d5ddf63cb7e30e8d9c117f7822aaf5e077365f83e4c7` |
| `spectral_regular_variation/INITIAL_COMPILE_RECEIPT.md` | `bf49975ed42317381c7298eae603f209a0eb61924324522afda68e5eedcc4efe` |

Full local input manifest, paths relative to `spectral_regular_variation/paper/`:

```text
9a104b081a64dc0d4e514bc34f349aa50b6392aa7469de136a6cf9690822c6a4  main.tex
5cc8edfd8e12b5a947909de79fa0c6a7ee314512c7ad1368b66fcaf37eeb8cde  math_commands.tex
8d2cbd9839f7fb66b62adce2ed5e523a681ebda3f231eba5c3d4acbf8877bfac  references.bib
cf385bf7fd2c474a7be1205d73d94afe46392ea5dce855f4e765c7481bf702b3  sections/0_abstract.tex
4702dcecefea8af8ff485efde577f8d0b2c3d1a718f353e941e20a98fafbf1f0  sections/1_introduction.tex
0f6dc2249ac252a5a4bb2e229d61a48faae47687cfa98f7269e6cf52bbb1aa7a  sections/2_framework.tex
d14b8e8497b196dd0d6d42ccd544eb12f350a74bbab512644ea71ab65b0dd176  sections/3_gram_limit.tex
5831943d8b75cd818b439684fcbc1fbb528857e67d9dc37e13d48d1ecb84ae65  sections/4_uniform_tails.tex
cfbbbe56f353cc1dc845cbc8686aab3fba890de559f019b9c5f733c975c759dc  sections/5_ideal_convergence.tex
f9ca2c254e13adeb254d21a2edb58a44132f3bd5756ca2122ac0085087970269  sections/6_consequences.tex
05aa2f633c4e88d04adb488a4e8bfef9354b9fb96e29262eb761985dfad624d4  sections/7_scope.tex
a8f855cb7b9dd527821fb501f73d14f6ddcac37e7af4dbbdc51cbc2f0b6fbaa5  sections/8_declarations.tex
```

`sha256sum -c SOURCE_SHA256SUMS.txt` returned `OK` for every one of these twelve inputs. The bibliography keys were independently counted from the actual TeX: eleven citation commands, with multiplicities `Hilberdink2017:4`, `HilberdinkPushnitski2023:3`, `BinghamGoldieTeugels1987:2`, and `Simon2005:2`. All four bibliography entries are used; no additional key was found.

## Mathematical claims checked against the actual full text

All locators below are relative to `spectral_regular_variation/paper/`. This covers every key-claim row in the author's map and additionally records the elementary power-sum lemma.

| Claim / risk surface | Evidence anchor | Review finding |
| --- | --- | --- |
| Standing coefficient family and shared Hilbert space | `sections/0_abstract.tex:1`; `sections/1_introduction.tex:12`; equations (1.1)–(1.2) | Positive measurable slow variation, compact upper/lower bounds, `sigma<1/2`, and zero extension are explicit. The abstract retains the local bounds flagged in the prior review; that previous M1 does not survive as a manuscript defect. |
| Main theorem, including the negative statement | `sections/1_introduction.tex:43`; assembled proof `sections/5_ideal_convergence.tex:4` | The three assertions match the frozen contract. The negative range says nonmembership for each finite `N`, not merely lack of convergence. |
| Classical LCM input | `sections/2_framework.tex:51` | Under the source specialization `tau=1`, its conditions become `1-2s>0`, `2-2s>1`, and `1>0`, all implied by `s<1/2`. Injectivity supplies strictly positive ordered eigenvalues; the positive asymptotic constant gives the exact p-series threshold. This is attributed input, not a new theorem of C403. |
| UCT and global Potter hypotheses | `sections/2_framework.tex:6`; equations (2.2)–(2.3) | The measurable positive version of UCT is applied only on fixed compact scaling intervals. The explicit four-case extension of eventual Potter bounds uses the stated local upper/lower bounds. No hypothesis has disappeared in prose. |
| Singular-value sum inequality and ideal linearity | `sections/2_framework.tex:94`, proof at 104 | Ranks less than `j,k` give rank at most `j+k-2`. Taking infima proves the stated singular-value inequality. Pairing indices and the scalar power inequality prove linearity for every `q>0`, including `q<1`. |
| Exact Gram identity | `sections/3_gram_limit.tex:6`, equation (3.1) | Direct multiplication and `r=k lcm(m,n)` give precisely the factors displayed. Positivity of `L` makes the entries nonnegative; positive semidefiniteness separately follows from the Gram representation. No multiplicativity is used. |
| Power sums for either sign of the exponent | `sections/3_gram_limit.tex:26`, proof at 36 | The separate arguments for negative `alpha` and `0<=alpha<1` prove the full bound used later. There is no hidden restriction to positive `sigma`. |
| Uniform entry majorant | `sections/3_gram_limit.tex:45`, proof at 56 | Every Potter argument is in `[1,N]`. With `alpha=2sigma+2epsilon<1`, the powers cancel as `N^{-rho+2epsilon} N^{1-alpha}=1`; the remaining LCM power is exactly minus one. Constants are independent of all matrix indices and `N`. |
| Entrywise convergence and smallest-index tail | `sections/3_gram_limit.tex:87`, proof at 101 | On the fixed upper interval UCT makes both ratios uniformly close to one. For the lower interval, `h^{1-alpha}(delta/h)^{1-alpha}=delta^{rho-2epsilon}` is independent of `N`. Empty tails are handled, and the order of limits is valid. The `(1,1)` entry proves the cumulative energy asymptotic. |
| Positive congruence, avoiding false entrywise order | `sections/4_uniform_tails.tex:6`, proof at 28 | `B_N` is constructed on the finite head. Entry domination is used only after coordinatewise absolute values to obtain a bilinear operator-norm bound against bounded `E_s`. Positivity then gives `B_N<=M I`, hence the genuine order `A_N<=M D_eta^2`. No unbounded inverse-diagonal domain is used. |
| Uniform eigenvalue tails | `sections/4_uniform_tails.tex:74` | Min–max applies to that operator majorant. The limiting majorant is obtained first on finitely supported forms and then by density. Only `eta<rho` is claimed, with no endpoint bound. |
| Operator-norm convergence | `sections/4_uniform_tails.tex:94`, proof at 103 | The factorization controls both coordinate tails uniformly in `N`. The compact limit has vanishing coordinate tails. Finite-head convergence followed by the `K` limit proves the norm limit; entrywise convergence alone is never substituted. |
| All real admissible ideal exponents | `sections/5_ideal_convergence.tex:9` | `1/q<eta<rho` is available exactly in the positive range. Odd-index bounds plus monotonicity at even indices give a fixed summable majorant. Scalar dominated convergence proves the claim unchanged below one; no quasi-norm triangle inequality or Banach interpolation is smuggled in. |
| Exact excluded range | `sections/5_ideal_convergence.tex:44` | Since finite-rank operators belong to every `S_q`, linearity of that ideal would turn membership of the difference into membership of the known nonmember `E_sigma`. The contradiction applies to every finite `N`. |
| Cumulative normalization | `sections/6_consequences.tex:13`, proof at 24 | The scalar ratio is positive, tends to one, and has only finitely many initial values outside a bounded tail. Operator convergence and the same spectral dominated-convergence argument establish the result also for `q<1`. |
| Ordered singular values and moments | `sections/6_consequences.tex:51`, proof at 74 | Min–max's Lipschitz bound yields a uniform **absolute** eigenvalue error. The positivity and moment arguments are valid. The text explicitly excludes uniform relative growing-index asymptotics; the fixed-index consequence does not extend beyond its quantifier. |
| Nonmultiplicative and oscillatory examples | `sections/6_consequences.tex:108` | The logarithmic ratio tends to one for every real beta; beta one violates multiplicativity at coprime 2 and 3. The oscillatory factor stays in `[1,3]`, has a vanishing phase increment under fixed scaling, and attains two different values along divergent sequences. These are analytic examples, not fabricated computations. |
| Nonclaims and target boundary | `sections/7_scope.tex:1` | Pointwise coefficient regular variation is not replaced by arbitrary cumulative-energy regular variation. No universal convergence rate, endpoint tail, joint relative limit, new LCM spectrum, global priority, or target Euler/zero-set identification is claimed. |

The significant proof expansions from the package are legitimate expositions of its existing argument: the elementary power-sum proof, explicit quasi-ideal linearity, global-Potter compact cases, finite-rank compact-tail explanation, and checked examples. They do not add a new theorem or an unlicensed broader coefficient class.

## Complete bibliography and actual citation-context review

All four registered references were checked for identity and bibliographic consistency. All eleven registered contexts were read next to their actual claims; **context coverage does not mean that every cited book was read in full**.

| Key | Identity / primary verification | Content access and limitation |
| --- | --- | --- |
| `Hilberdink2017` | Titus Hilberdink, *Linear and Multilinear Algebra* 65(4) (2017), 813–829, DOI `10.1080/03081087.2016.1204978`; checked against the cover of the [official accepted manuscript](https://centaur.reading.ac.uk/66059/1/finitetoeplitz.pdf). | Read the relevant accepted-manuscript text: Section 1.1, Proposition 2.1, Theorem 2.2/Corollary 2.3, Theorems 3.1/3.2, and the power example in Section 4(a). PDF SHA256 is `d040bf0f3df4da2d72b1f7728b80c6e3fed3d1214ed1e3a895e8dde81f71b518`. No fresh full-paper reading or physical-page-anchor audit is claimed. |
| `HilberdinkPushnitski2023` | Titus Hilberdink and Alexander Pushnitski, *St. Petersburg Mathematical Journal* 34(3) (2023), 463–481; [official publication and DOI record](https://www.mathnet.ru/eng/aa1816), DOI `10.1090/spmj/1764`. | Directly checked [arXiv:2110.14323v1](https://arxiv.org/html/2110.14323v1), Theorems 1.1 and 2.1, adjacent definitions/assumptions, and introductory prime-factor discussion. The manuscript marks this version for the parity comparison; it makes no claim about current open-problem status. |
| `BinghamGoldieTeugels1987` | N. H. Bingham, C. M. Goldie, J. L. Teugels, *Regular Variation*, Cambridge University Press, 1987, DOI `10.1017/CBO9780511721434`; [publisher metadata](https://www.cambridge.org/core/books/abs/regular-variation/contents/92ABC242FEBEDE566EA28EA26351D63B) checked. | The book was **not** read in full, nor were its precise UCT/Potter pages retrieved. The [publisher Chapter 1 record](https://www.cambridge.org/core/books/abs/regular-variation/karamata-theory/3AE606B1554DD31F5211C1FFE0F0B3C7) does not expose the full theorem text. Global Potter is additionally verified in Hilberdink's inspected Section 1.1. UCT is used in its standard explicitly stated measurable-positive form; attribution is conventional, not represented as a page-level book-content audit. |
| `Simon2005` | Barry Simon, *Trace Ideals and Their Applications*, second edition, Mathematical Surveys and Monographs 120, AMS, 2005, DOI `10.1090/surv/120`; [official edition record](https://bookstore.ams.org/SURV/120) checked through its returned publisher search record. | No full monograph or precise book page was read. Direct publisher-page/endmatter retrieval was intermittently unavailable. The book is a general framework citation; the manuscript itself proves the particular singular-value sum and all-positive-q linearity statements it needs. The remaining approximation/min–max facts are standard, not newly claimed. |

The author's bibliography-access disclosures agree with these bounded checks. Metadata-only verification for a book is not upgraded to full-body content verification. No fabricated page or theorem locator is present.

| Actual context | Key | Context judgment |
| --- | --- | --- |
| `sections/1_introduction.tex:76` | `Hilberdink2017` | Supported: complete multiplicativity versus multiplicativity with extra conditions is accurately distinguished. |
| `sections/2_framework.tex:32` | `Hilberdink2017` | Supported directly by its Section 1.1 global Potter statement under local bounds. |
| `sections/3_gram_limit.tex:21` | `Hilberdink2017` | Proposition 2.1 is the correct common-multiple identity; the displayed specialization is directly proved. |
| `sections/7_scope.tex:18` | `Hilberdink2017` | Supported as a difference of coefficient assumptions, without wholesale-containment language. |
| `sections/1_introduction.tex:89` | `HilberdinkPushnitski2023` | Supported by the named v1 result; the even-integer qualification is version-bound. |
| `sections/2_framework.tex:72` | `HilberdinkPushnitski2023` | Correct specialization of Theorem 1.1 and its assumptions; sharp membership follows from the positive asymptotic. |
| `sections/7_scope.tex:27` | `HilberdinkPushnitski2023` | The source owns the LCM asymptotics, constant, and prime analysis. |
| `sections/1_introduction.tex:125` | `BinghamGoldieTeugels1987` | Appropriate classical-tool attribution; limited book-content access remains disclosed above. |
| `sections/2_framework.tex:30` | `BinghamGoldieTeugels1987` | Correct standard statements and explicit hypotheses; no invented source locator. Global Potter independently corroborated as above. |
| `sections/1_introduction.tex:126` | `Simon2005` | General compact-operator framework citation, consistent with the official book scope. |
| `sections/2_framework.tex:91` | `Simon2005` | Appropriate framework citation; the specific subsequent inequality/linearity proof is self-contained. No claim of reading a precise uninspected book theorem. |

Table 1 was also compared with the surrounding source discussion. It summarizes the same qualified settings and does not silently add a new source or an empirical comparison. The manuscript's eleven actual citation commands match the author's inventory exactly.

## Strongest counterargument and scope disposition

The strongest objection is not a demonstrated proof flaw: much of the machinery is classical, the limit spectrum is prior-owned, and the pure-power parity extension alone would be a short increment. The review therefore must not describe C403 as a new LCM spectral law or as settling an open problem still current in 2026. The actual theorem addresses a full nonmultiplicative pointwise regularly varying coefficient family, including oscillatory factors, with all admissible ideal exponents and exact nonmembership outside the range. Those combined quantifiers are present in the proof and the manuscript does not split them into independent contributions. No inspected source passage directly proves that same nonmultiplicative theorem; the bounded check does not rule out all later or uninspected literature.

There is likewise no inference from source divisibility arithmetic to a target Hilbert–Pólya operator. The manuscript expressly refuses that inference. This review gives no A2/A3 evaluation and no positive target-route score.

## Registered numerical/data surfaces and seven failure modes

There are **zero empirical result surfaces** in the reviewed draft: no performance table, sampled matrix experiment, plotted numerical spectrum, seed count, confidence interval, or claimed computational discovery. The displayed examples are checked by algebra and limit arguments. Compilation artifacts are production evidence, not mathematical experiments. The declaration of no new numerical experiments matches the actual text. No test was invented to satisfy a checklist quota.

| ARS failure mode | Scoped status | Evidence / boundary |
| --- | --- | --- |
| 1. Implementation bug passing self-review | CLEAR for applicability to the registered empirical population | That population is empty; the theorem relies on the written analytic proof, which was separately checked above. This is not a claim that arbitrary repository code is bug-free. |
| 2. Hallucinated citation | CLEAR for identity/misstatement on checked surfaces, with access advisory | Four identities and all eleven actual contexts were inspected. The two book-content limitations are explicit; no full-book or retraction-clean certificate is issued. |
| 3. Hallucinated experimental result | CLEAR for the reviewed draft | No empirical result or computational discovery is claimed. |
| 4. Shortcut reliance | CLEAR for the named mathematical risk | The manuscript does not use entrywise convergence as norm convergence or entrywise domination as positive order. The finite congruence and two-sided tail argument close those specific shortcuts. |
| 5. Implementation bug reframed as novelty | CLEAR for the reviewed draft | No implementation-derived surprise is used as evidence. The claimed increment is a quantified proof about the stated coefficient family. |
| 6. Methodology fabrication | CLEAR for the reviewed draft | The methods are the explicit analytic derivation, with no fictitious experiment settings or rerun claims. This reviewer performed no compilation. |
| 7. Early frame lock | No suspected frame-lock defect identified in this scope | The paper retains the distinction between the source theorem and target arithmetic goals, and does not overstate the later literature. Global significance/priority and target identification remain unestablished rather than manufactured. |

These scoped dispositions apply only to this internal review and named populations; they are not a full ARS Stage 2.5/4.5 certificate. No broad plagiarism detector, global originality search, retraction database sweep, or human-read attestation was run. The source-owned theorem, common-multiple identity, and regular-variation tools are expressly attributed. The prose/claim comparison with the frozen package found no substantive claim-strength expansion.

## Handoff

Blocking findings: **0**. Actionable minor findings: **0**. The prior local-bounds caution is resolved in the actual abstract and standing hypotheses. Remaining non-defect advisories are the limited classic-book content access, the boundedness of the novelty search, the pending production checks, and the author/funding/disclosure fields which the draft expressly marks as not supplied.

No manuscript correction is requested by this review. Preserve the frozen input hashes. The coordinator may proceed to final two-directory builds and all-page QA on this reviewed source version. The coordinator remains responsible for those actual production gates, artifact packaging, separate source-admission/target evaluations, and any later affected-only re-review if the author changes these bytes.

The coordinator subsequently supplied the exact initial-receipt path, `spectral_regular_variation/INITIAL_COMPILE_RECEIPT.md`, and it was read completely before this report was finalized. It openly records the fresh initial directory, incremental table/bookmark repairs, the superscript-comma repair, representative-page checks, and the unperformed final two-build/all-page gates. Its PDF and source-manifest hashes match the reviewed artifacts. As read-only consistency checks, this reviewer rehashed the five archived log/auxiliary/text files against the receipt, checked the current PDF metadata (11 pages, 350553 bytes, A4, PDF 1.5), and found no matches for the receipt's warning/error pattern in the final TeX/BibTeX logs. All twelve source hashes still passed. These checks neither reran compilation nor independently witnessed the author's earlier execution; no stronger execution or visual attestation is made. The receipt introduces no new mathematical or bibliographic issue.
