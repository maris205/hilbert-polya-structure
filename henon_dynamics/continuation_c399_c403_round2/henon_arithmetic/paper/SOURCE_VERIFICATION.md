# C401 source and citation verification

Verified on 5 September 2026. This is a bounded citation/ownership check, not an exhaustive novelty search, retraction audit, venue endorsement, or certification of the manuscript's mathematical correctness. The six bibliography entries are all cited. There are seven actual citation commands because the Stacks Project is cited twice. Locators below refer to the frozen initial-build TeX recorded in `SOURCE_INPUTS.sha256` and the 13-page initial PDF.

## Bibliographic and content checks

| Citation key | Verified bibliographic record | Content inspected and exact locator | Access limitation |
| --- | --- | --- | --- |
| `fujiwara1997rigid` | Kazuhiro Fujiwara, *Rigid geometry, Lefschetz–Verdier trace formula and Deligne's conjecture*, Inventiones Mathematicae 127(3) (1997), 489–533; [publisher DOI](https://doi.org/10.1007/s002220050129). Publisher page and DOI metadata checked. | Attribution of the original sufficiently-high-Frobenius result is checked through the proof of Proposition 2.10 in [Shuddhodan's author v2](https://arxiv.org/html/1803.06461v2), together with the discussion surrounding Theorem 2.3.2 in [Varshavsky's author v2](https://arxiv.org/html/math/0505564v2). The manuscript explicitly identifies this mediated attribution. | The full original Fujiwara article was not inspected. No precise theorem statement is quoted from that inaccessible original. |
| `varshavsky2007trace` | Yakov Varshavsky, *Lefschetz–Verdier Trace Formula and a Generalization of a Theorem of Fujiwara*, Geometric and Functional Analysis 17(1) (2007), 271–319; [publisher DOI](https://doi.org/10.1007/s00039-007-0596-9). Publisher and author's institutional metadata checked. | [Author manuscript arXiv:math/0505564v2](https://arxiv.org/html/math/0505564v2), Section 2.2 and Theorem 2.3.2: contraction after sufficiently large Frobenius twist and the corresponding trace statement. | The content locators are explicitly tied to the 2005 author v2, not silently asserted to have the same numbering in the published version. |
| `shuddhodan2019constraints` | K. V. Shuddhodan, *Constraints on the cohomological correspondence associated to a self map*, Compositio Mathematica 155(6) (2019), 1047–1056; [publisher DOI](https://doi.org/10.1112/S0010437X19007188). DOI metadata and arXiv identity checked. | [Author manuscript arXiv:1803.06461v2](https://arxiv.org/html/1803.06461v2), Lemma 2.6, Proposition 2.10, Definition 2.12, Lemma 2.14, Example 3.6, and the paragraph immediately after Example 3.6. These locate, respectively, twisted étaleness, eventual trace agreement, the cohomologically defined rational zeta, the torus example, and discussion of threshold growth under iteration. | All numbered content locators refer to the 2018 author v2. The threshold paragraph is **not** labeled Remark 3.7 in that inspected version. |
| `stacks2026intersection` | The Stacks Project Authors, *The Stacks Project*, 2026, tags 0B01 and 0FEZ, accessed 5 September 2026. Project citation metadata checked. | [Tag 0B01, Lemma 43.16.1](https://stacks.math.columbia.edu/tag/0B01): proper Cohen–Macaulay intersections and their local lengths. [Tag 0FEZ](https://stacks.math.columbia.edu/tag/0FEZ): the local-complete-intersection framework. | This reference supplies the classical local intersection rule; the Hénon-specific properness, graph charts, and local lengths are proved in the manuscript. |
| `milne2013etale` | James S. Milne, *Lectures on Étale Cohomology*, version 2.21, 22 March 2013; [author course page](https://www.jmilne.org/math/CourseNotes/lec.html) and [author PDF](https://www.jmilne.org/math/CourseNotes/LEC.pdf). Version and author-supplied citation checked. | Author PDF, Example 16.3 (affine-space cohomology), Section 22 (compact support), Theorem 24.1 (Poincaré duality), and the following finite-degree pullback discussion in Remark 24.2. | Used only for the classical cohomological comparison in Section 5, not for the geometric equalizer count. |
| `dwork1960rationality` | Bernard Dwork, *On the Rationality of the Zeta Function of an Algebraic Variety*, American Journal of Mathematics 82(3) (1960), 631–648; [DOI record](https://doi.org/10.2307/2372974). DOI metadata checked. The terminal page and the fixed-variety setting were independently checked in the author's [1967 publisher chapter abstract and bibliography, reference 1](https://link.springer.com/chapter/10.1007/978-3-642-87942-5_5). | Dwork's 1967 author chapter describes the rational-point zeta of a variety over a finite field and cites the 1960 article. This verifies the ownership and scope of the rationality result used for the manuscript's contrast. | The full 1960 article was not inspected. The manuscript does not quote it or invoke a fine-grained theorem locator from it. |

## Every actual citation context

All file paths in this table are relative to `paper/`. The summaries identify the actual claims next to each citation, not merely a list of background topics.

| Actual TeX location | Citation | Claim supported in that context | Ownership boundary retained |
| --- | --- | --- | --- |
| `sections/2_context.tex:5` | Fujiwara | Original source of the general eventual Frobenius trace principle, as attributed in the inspected Shuddhodan and Varshavsky accounts. | The general principle is classical, not a C401 contribution. |
| `sections/2_context.tex:8` | Varshavsky | Algebraic-geometric generalization via contracting correspondences; author-v2 Section 2.2 and Theorem 2.3.2 are named. | C401 does not claim a new general trace or local-term theorem. |
| `sections/2_context.tex:19` | Shuddhodan | Twisted étaleness, eventual trace agreement, rational cohomological zeta, torus nonproperness example, and iteration-dependent threshold discussion at the explicit v2 locators above. | Neither nonuniform thresholds nor short-twist discrepancies are claimed as conceptually new. |
| `sections/2_context.tex:37` | Stacks Project | The classical intersection-multiplicity-as-length rule, and the local-complete-intersection setting. | Only the Hénon graph coefficients and two local lengths are calculated here. |
| `sections/2_context.tex:41` | Milne | Classical affine-space cohomology, compact support, and Poincaré duality used later to obtain the top cohomological trace. | These are not inputs to the geometric count and are not original results. |
| `sections/4_boundary_count.tex:164` | Stacks Project | At the already verified smooth graph-intersection points, the proper local intersection number equals the local length just computed. | The manuscript checks the hypotheses before this use; it does not infer local lengths merely from total graph degree. |
| `sections/5_threshold_slices.tex:138` | Dwork | Fixed-variety Hasse–Weil rationality does not impose rationality on a two-clock slice whose defining equations vary with the extension clock. | The text explicitly allows accidental equality with the zeta of affine two-space when the defect polynomial is zero. |

## Claim-to-proof locators

All important mathematical statements have full proofs in the main text. There is no proof appendix and no claim is justified by the recorded numerical examples.

| Claim | Statement locator | Full proof locator | Initial PDF page(s) |
| --- | --- | --- | --- |
| Theorem 1.1: finite reduced nonresonant equalizer, count `max(DQ,Q^2)` | `sections/1_introduction.tex:44` | `sections/4_boundary_count.tex:150`, using Lemmas 3.1–4.4 | Statement 2; proof 7 |
| Corollary 1.2: all positive clocks when `d` is not a power of the characteristic | `sections/1_introduction.tex:59` | `sections/4_boundary_count.tex:179` | 2, 7 |
| Lemma 3.1: iterate degrees and the two infinity points | `sections/3_projective_geometry.tex:11` | `sections/3_projective_geometry.tex:27` | 3–4 |
| Lemma 3.2: forward and inverse graph charts | `sections/3_projective_geometry.tex:76` | `sections/3_projective_geometry.tex:85` | 4 |
| Lemma 3.3: graph classes and total intersection `1+DQ+Q^2` | `sections/3_projective_geometry.tex:110` | `sections/3_projective_geometry.tex:124` | 4–5 |
| Lemma 4.1: affine equalizer is zero-dimensional and reduced | `sections/4_boundary_count.tex:3` | `sections/4_boundary_count.tex:9` | 5 |
| Lemma 4.2: only two boundary intersection points | `sections/4_boundary_count.tex:32` | `sections/4_boundary_count.tex:37` | 5–6 |
| Lemma 4.3: regular infinity length `Q min(D,Q)` | `sections/4_boundary_count.tex:52` | `sections/4_boundary_count.tex:57` | 6 |
| Lemma 4.4: inverse-regular infinity length one | `sections/4_boundary_count.tex:123` | `sections/4_boundary_count.tex:128` | 7 |
| Proposition 5.1: exact trace threshold and all finite defects | `sections/5_threshold_slices.tex:37` | `sections/5_threshold_slices.tex:56` | 8 |
| Proposition 5.3: slice formula and transcendence for nonzero defect | `sections/5_threshold_slices.tex:88` | `sections/5_threshold_slices.tex:99` | 8–9 |
| Proposition 5.4: obstruction to an invertible finite-dimensional weighted trace | `sections/5_threshold_slices.tex:149` | `sections/5_threshold_slices.tex:162` | 9–10 |
| Proposition 6.1: genuine diagonal map, fixed-point count, rational dynamical zeta | `sections/6_diagonal_resonance.tex:13` | `sections/6_diagonal_resonance.tex:32` | 10–11 |
| Proposition 6.2: explicit degree-resonant counterexample, six points rather than nine | `sections/6_diagonal_resonance.tex:86` | `sections/6_diagonal_resonance.tex:97` | 11 |

Definition 5.2 merely defines the fixed-time slice and does not assert a theorem. The resonant counterexample and diagonal comparison were already part of the frozen mathematical contract, not newly invented additions during manuscript drafting. The bibliography check verifies cited source identities and bounded support; final independent review remains the coordinator's responsibility.
