# C401 independent internal manuscript review

Date: 5 September 2026. Reviewer: current-team agent assigned to the nonlinear-return lane, not the C401 manuscript author. This is an AI-assisted internal mathematical and integrity review, not human or external peer review.

## Verdict and scope

**MANUSCRIPT_PASS_MINOR_CLOSED — zero blocking findings, zero open minor findings.** The manuscript proves the stated nonresonant Hénon--Frobenius equalizer law and its stated consequences. The coordinator's known wording issue M1 was justified and has been closed by an affected-line check. No additional mathematical gap was found in the 14 registered claims.

The reviewed scientific increment is the all-coefficient, nonresonant exact count and its two explicit local intersection lengths. General eventual Frobenius trace agreement, affine-space cohomology, and fixed-variety zeta rationality remain prior-owned. This verdict does not grant global priority, a target-route promotion, or a publication recommendation.

Review calibration: **NOT_CALIBRATED — criteria_binding_unavailable**. No venue-specific acceptance criteria were supplied. The research-review workflow and the ARS domain/integrity checks, including all seven AI-research failure modes, were applied within this delegated internal review. This was not a full ARS multi-seat run, an external-model evaluation, or a human-read attestation. The prior proof review and the coordinator's preliminary observation were visible; in particular M1 is not presented as a blind discovery.

I read the complete manuscript build inputs: main file, command file, eight section files (881 section lines in the initial snapshot), and bibliography; the complete source-verification note and initial-build receipt; the two source/provenance manifests; the complete 456-line upstream contract and prior proof review; the complete bounded-check producer; and all saved JSON output, including all 47 nonresonant rows and the separate resonant control. Source manifests were checked read-only. I reasoned through the proofs independently of the recorded numerical equalities. No mathematical producer, compiler, or experiment was run, and no author file was edited by this reviewer.

This report covers the frozen initial manuscript plus the single source-only M1 correction described below. It does not certify a regenerated final PDF, all-page visual QA, or the coordinator's two fresh-directory builds. The initial-build receipt openly records its two failed preliminary builds and later successful builds; this review does not replace those records with a fresh execution claim.

## Artifact binding

Paths in the first table are relative to `henon_arithmetic/paper/`; upstream paths in the second are relative to the continuation directory. The initial source manifest contains all 11 individual build-input hashes. All 11 archived inputs checked against it. Its unchanged hash therefore binds the complete reviewed initial source, not merely the files selected for quotation here.

| Reviewed artifact | SHA256 |
| --- | --- |
| `SOURCE_INPUTS.sha256` | `1f7307204aa183613eb9898a5a32c5ba03ddb6deddce9f2970ac474562f83485` |
| `SOURCE_VERIFICATION.md` | `9587ca2db384fcb3a199cc1f3bf305c9d65b0048544285d9b9105cad468faabe` |
| `INITIAL_BUILD_RECEIPT.md` | `37c3de706d4d7426e1fdbf4b7e44d2758a28ed8e7425a7f39e146a19222cd988` |
| `FROZEN_UPSTREAM.sha256` | `9f5971f7fae7f83026b28e220c45532e8cccb8ff1b15552124fbd832995fcda4` |
| Initial 13-page PDF, preserved at `initial_build/initial.pdf` | `fcd14059ed2504dae82188c585d8bc2a05f040fc27775251728d72c5408e891a` |
| Initial `sections/1_introduction.tex`, preserved under `initial_build/source/` | `88162d13ea48b94b6053d5ac1d8b28850fe184730d31b79506140129a516d980` |
| M1-corrected `sections/1_introduction.tex` | `b8a7f05bd2fbbfd6c5af28f3845854975d62e7c2ea709aa3093b9897a724af93` |

| Frozen upstream artifact | SHA256 |
| --- | --- |
| `henon_arithmetic/CONTRACT_SCOUT.md` | `a891beca49be4b1cc2a460a4320596097a22c13a39056e20727db5058b982378` |
| `henon_arithmetic/bounded_check.py` | `330440c3883aeaabb53944c9e3e2101ecdccdc92dfb3d775fdbf8811121668cf` |
| `henon_arithmetic/bounded_results.json` | `9d821a7b787ad0fdbf8fca5b25a5724d7f3d46d792888e17256600136653e79b` |
| `reviews/HENON_ARITHMETIC_PROOF_REVIEW.md` | `1db696829223f9ac76f93bdfea607a169890c61d3535afac72af6dae3819627e` |

The coordinator preserved the original inputs and PDF before changing M1. A read-only recursive comparison of the initial and current section directories showed exactly that one changed line. The historical `SOURCE_INPUTS.sha256` and initial-build receipt correctly remain initial-snapshot records; they must not be represented as the final corrected-source manifest.

## Mathematical review: all 14 registered claims

Throughout, the source map is the actual polynomial automorphism
`H(x,y)=(y,f(y)-a x)` over `F_q`, with arbitrary degree-`d` polynomial `f`, `d>=2`, and `a!=0`. Write `D=d^n` and `Q=q^r`. The affine equalizer is counted over the algebraic closure. It is not an enumeration of points in one selected finite extension. Line references below are relative to `paper/` and remain unchanged by M1.

| Claim and statement locator | Proof locator | Independent check and disposition |
| --- | --- | --- |
| Theorem 1.1, `sections/1_introduction.tex:44` | `sections/4_boundary_count.tex:150` | **PASS, M1 closed.** Finiteness and reducedness hold for every positive pair of clocks. When `D!=Q`, the total graph intersection is `1+DQ+Q^2`; removing lengths `Q min(D,Q)` and `1` gives `max(DQ,Q^2)`. Boundary properness is established before using intersection multiplicities as lengths. |
| Corollary 1.2, `sections/1_introduction.tex:59` | `sections/4_boundary_count.tex:179` | **PASS.** If `d^n=p^{er}`, unique factorization forces `d` to be a power of `p`. Thus the non-`p`-power hypothesis excludes resonance for all positive `n,r`, not just the checked examples. |
| Lemma 3.1, `sections/3_projective_geometry.tex:11` | Same file, line 27 | **PASS.** Forward coordinate degrees are `d^(n-1),d^n`, with pure leading powers in `y`; strict degree separation prevents cancellation even with nonmonic `f` or positive characteristic. The inverse has the corresponding pure leading power in `x`. These give the stated opposite regular and indeterminate infinity points. |
| Lemma 3.2, `sections/3_projective_geometry.tex:76` | Same file, line 85 | **PASS.** At the forward regular infinity point the graph is the ordinary graph in the source chart. At the other point the inverse is regular, so the second-projection chart is valid. This avoids treating the original rational map as regular at its indeterminacy point. |
| Lemma 3.3, `sections/3_projective_geometry.tex:110` | Same file, line 124 | **PASS.** With the manuscript's projection convention, graph classes are `h1^2+D h1 h2+h2^2` and `Q^2 h1^2+Q h1 h2+h2^2`. Both Hénon projections are birational; a generic source line avoids the base point and a generic target line avoids the contracted image, giving mixed coefficient `D`. Frobenius has scheme degree `Q^2`, not `Q^2` distinct points in a geometric fiber. Multiplication gives `1+DQ+Q^2`. |
| Lemma 4.1, `sections/4_boundary_count.tex:3` | Same file, line 9 | **PASS.** The Frobenius terms have zero differential and the equalizer Jacobian is `DH^n`, determinant `a^n`. The local rings at all geometric affine solutions are reduced and zero-dimensional. Finite type then gives a finite reduced affine scheme. This argument does not assume the eventual count. |
| Lemma 4.2, `sections/4_boundary_count.tex:32` | Same file, line 37 | **PASS.** A pair on the Frobenius graph is finite in both factors or infinite in both. The forward contraction off its unique indeterminacy point, together with the opposite inverse chart and the geometric injectivity of Frobenius, leaves exactly `(I_-,I_-)` and `(I_+,I_+)` on the boundary. |
| Lemma 4.3, `sections/4_boundary_count.tex:52` | Same file, line 57 | **PASS.** The completed quotient is `k[[u,v]]/(A-u^Q C, v^D-v^Q C)` with `C` a unit and `(A-u^Q C) mod v` a nonzero multiple of `u^Q`. Nonresonance makes the second equation a unit times `v^min(D,Q)`. Reduction modulo `v` and cancellation in `k[[u,v]]` prove that `v` is a non-zero-divisor modulo the first equation. Each of the `min(D,Q)` filtration quotients has length `Q`, giving the claimed product. |
| Lemma 4.4, `sections/4_boundary_count.tex:123` | Same file, line 128 | **PASS.** In the inverse-regular chart the equation is `Y=Phi_r(g^{-1}(Y))`. Its linear part is the identity because the right-hand side has no linear terms. Nakayama, or the formal local inverse argument, gives length one. This does not require separability of Frobenius. |
| Proposition 5.1, `sections/5_threshold_slices.tex:37` | Same file, line 56 | **PASS.** Section 5 retains the non-`p`-power degree hypothesis. With `R=floor(log_q D)`, the defects are `Q(D-Q)>0` exactly for `1<=r<=R`; agreement first occurs at `r=R+1`. There is no hidden equality case. The compactly supported comparison is `Q^2`, since only top affine-space cohomology survives. |
| Proposition 5.3, `sections/5_threshold_slices.tex:88` | Same file, line 99 | **PASS.** Splitting off the tail gives `exp(P_n(t))/(1-q^2 t)` with the stated finite defect polynomial. For `D>q`, the polynomial is nonconstant with positive leading coefficient. The proof rules out an algebraic relation by comparing its largest exponential term along the positive real axis; rational denominators are first cleared. For zero defect the slice can coincide numerically with the zeta of affine two-space. |
| Proposition 5.4, `sections/5_threshold_slices.tex:149` | Same file, line 162 | **PASS.** Finite-dimensional characteristic-zero traces with invertible `F_i` obey a recurrence whose constant coefficient is nonzero. Subtracting the `q^(2r)` term and propagating the zero tail backwards forces every positive-index defect to vanish, contradicting the first defect when `D>q`. The proof does not assume that `A_i` commutes with `F_i`, and does require the explicitly stated invertibility and all-clock equality. It makes no infinite-dimensional exclusion. |
| Proposition 6.1, `sections/6_diagonal_resonance.tex:13` | Same file, line 32 | **PASS.** Coefficients in `F_q` imply commutation with `Phi_s`, so the actual map `S=H^{-b}Phi_s` satisfies `S^m=H^{-bm}Phi_{sm}`. The nonresonant max-law gives `#Fix(S^m)=Lambda^m` and hence `1/(1-Lambda t)`. This is a new diagonal clock and a genuine iterated map, not the fixed-`n` slice or ordinary Hénon periodic zeta. The separately discussed top cohomological determinant need not agree in the short-twist regime. |
| Proposition 6.2, `sections/6_diagonal_resonance.tex:86` | Same file, line 97 | **PASS.** For `H(x,y)=(y,y^3+y^2-x)` in characteristic three and `n=r=1`, the first equation gives `y=x^3`; substitution in the second gives `x^6-x=0`. Its derivative is `-1`, so there are six distinct geometric points, not nine. This directly reconstructed elimination invalidates an unconditional extension to `D=Q`. |

Definition 5.2 introduces notation only and is not counted as a fifteenth theorem. All proofs are in the main text. In particular, neither the 47 finite examples nor the prior proof-review verdict is used to fill a missing quantified argument.

The delicate global-to-local step is sound: all affine intersections are isolated; the two boundary computations are finite-length local intersections; and the relevant Hénon graph charts and Frobenius graph are smooth at every intersection point. Thus their proper Cohen--Macaulay intersections in the smooth ambient product have local intersection numbers equal to the calculated scheme lengths. There is no omitted boundary component or interchange of scheme degree with geometric cardinality.

## Finding M1 and affected-only closure

**M1 — minor conditional-scope ambiguity, supplied by the coordinator before this review.** In Theorem 1.1, the first assertion of finite reducedness applies to all clocks, while the following count and explicit boundary lengths require `D!=Q`. The initial transition, “More precisely, the closures ...”, could be read as expanding the unqualified first assertion. The proof itself already imposed nonresonance correctly, so this was not a proof gap.

The coordinator changed only `sections/1_introduction.tex:51` to:

> Under the same nonresonance condition, the closures of the graphs of $H^n$ and $\Phi_r$ in

I inspected that exact delta and the adjacent theorem. It resolves the scope ambiguity without changing the theorem proved or the examples. Status: **CLOSED**. No mathematical rerun is warranted. The final corrected PDF must still be built and inspected by the coordinator; the initial PDF hash above deliberately continues to describe the old wording.

The earlier proof review's two author-facing items are also satisfied in the manuscript: Frobenius's `Q^2` coefficient is described using finite-morphism/scheme degree, and the Shuddhodan threshold paragraph is located immediately after Example 3.6 rather than assigned an unverified “Remark 3.7” label.

## Independent bibliography and ownership check

All six actual bibliography records were checked against primary publisher, author, institutional, or project sources during this review. All seven actual citation commands were read in context. This is bounded identity and content-support verification, not an exhaustive retraction scan or global novelty clearance. No unavailable original was silently upgraded to full-text access.

| Reference | Independently checked identity and primary content | Result and limitation |
| --- | --- | --- |
| Fujiwara, *Rigid geometry, Lefschetz--Verdier trace formula and Deligne's conjecture*, Invent. Math. 127(3) (1997), 489--533, DOI `10.1007/s002220050129` | [Publisher record](https://link.springer.com/article/10.1007/s002220050129) matches the entry. Original ownership of sufficiently high Frobenius twisting is supported by Proposition 2.10 and its attribution in [Shuddhodan author v2](https://arxiv.org/html/1803.06461v2), and the discussion accompanying Theorem 2.3.2 in [Varshavsky author v2](https://arxiv.org/html/math/0505564v2). | **PASS, mediated content attribution.** The full original 1997 article was not read; neither manuscript nor this review claims otherwise. |
| Varshavsky, *Lefschetz--Verdier Trace Formula and a Generalization of a Theorem of Fujiwara*, GAFA 17(1) (2007), 271--319, DOI `10.1007/s00039-007-0596-9` | [Author institution record](https://cris.huji.ac.il/en/publications/lefschetz-verdier-trace-formula-and-a-generalization-of-a-theorem/) confirms identity. The actual [author v2](https://arxiv.org/html/math/0505564v2), Section 2.2, Lemma 2.2.3, Corollary 2.2.4 and Theorem 2.3.2 were inspected for contraction thresholds and the hypotheses of the trace statement. | **PASS.** The manuscript treats these as classical context, not as a theorem automatically giving the short-twist Hénon count. Numbering is explicitly version-bound. |
| Shuddhodan, *Constraints on the cohomological correspondence associated to a self map*, Compos. Math. 155(6) (2019), 1047--1056, DOI `10.1112/S0010437X19007188` | [Publisher article](https://www.cambridge.org/core/journals/compositio-mathematica/article/constraints-on-the-cohomological-correspondence-associated-to-a-self-map/1540B4808FA0FDC8A2CF17B75A02DC51) confirms metadata. In [author v2](https://arxiv.org/html/1803.06461v2), Lemma 2.6, Proposition 2.10, Definition 2.12, Lemma 2.14, Example 3.6 and its following threshold paragraph were read. | **PASS.** Twisted étaleness, eventual agreement, the cohomologically defined rational zeta, torus discrepancy and growing-threshold motivation are prior-owned. No claim of a new general principle remains. |
| Stacks Project, tags 0B01 and 0FEZ, accessed 5 September 2026 | Actual [Lemma 43.16.1, tag 0B01](https://stacks.math.columbia.edu/tag/0B01), including its proper Cohen--Macaulay hypotheses and length formula, and the [lci/Gysin framework, tag 0FEZ](https://stacks.math.columbia.edu/tag/0FEZ), were inspected. | **PASS.** These provide the classical intersection rule. The manuscript itself supplies the Hénon chart regularity, properness and local lengths needed to apply it. |
| Milne, *Lectures on Étale Cohomology*, version 2.21, 22 March 2013 | The actual [author PDF](https://www.jmilne.org/math/CourseNotes/LEC.pdf) confirms version metadata. Example 16.3, compact supports in Section 18, the compact-support Künneth discussion in Section 22, Theorem 24.1 and finite-degree pullback Remark 24.2 were read. | **PASS.** These support the elementary affine-space cohomological comparison. More precisely, the cited Section 22 supplies the relevant Künneth extension; it is not the first definition of compact support. The manuscript's cited locations adequately support the stated use. |
| Dwork, *On the Rationality of the Zeta Function of an Algebraic Variety*, Amer. J. Math. 82(3) (1960), 631--648, DOI `10.2307/2372974` | The DOI BibTeX response confirms author, title, journal, volume, issue, year, DOI and first page. Dwork's own [1967 publisher chapter abstract and bibliography, reference 1](https://link.springer.com/chapter/10.1007/978-3-642-87942-5_5) independently confirm the terminal page and the fixed-variety rational-point-zeta setting. | **PASS, bounded original access.** The full 1960 article was not read. Only ownership and scope of the classical rationality theorem are used, not a fine-grained theorem or quoted passage from that original. |

The inspected closest-source material does not itself supply the two Hénon local lengths or the all-coefficient short-twist max-law. That observation bounds the ownership subtraction within these sources; it does not prove that no other publication contains the result.

### Every actual citation context

| TeX locator, relative to `paper/` | Actual key | Context-specific decision |
| --- | --- | --- |
| `sections/2_context.tex:5` | `fujiwara1997rigid` | **PASS.** Original eventual-trace ownership is expressly mediated through the inspected accounts. |
| `sections/2_context.tex:8` | `varshavsky2007trace` | **PASS.** Contracting correspondences and the author-v2 theorem are described with their eventual-twist role. |
| `sections/2_context.tex:19` | `shuddhodan2019constraints` | **PASS.** All named distinctions and the post-Example-3.6 threshold discussion agree with the inspected v2. |
| `sections/2_context.tex:37` | `stacks2026intersection` | **PASS.** Classical local-length/lci input is separated from the new graph calculations. |
| `sections/2_context.tex:41` | `milne2013etale` | **PASS.** Affine cohomology, compact-support Künneth and duality support the later comparison, not the independent point-count proof. |
| `sections/4_boundary_count.tex:164` | `stacks2026intersection` | **PASS.** At this use site the manuscript has established properness and smooth local graph charts, so the lemma's hypotheses hold. |
| `sections/5_threshold_slices.tex:138` | `dwork1960rationality` | **PASS.** Fixed-variety Hasse--Weil rationality does not imply rationality of the changing-equation fixed-time slice. The text explicitly permits accidental equality with the affine-two-space zeta in the zero-defect case. |

There are no uncited bibliography entries or unsupported “full original read” assertions in these six entries/seven contexts. This check did not use an automated semantic-database certification and does not claim one.

## All recorded exact examples: evidence surface, not proof

The producer and all 1,354 lines of the saved JSON were read. The producer constructs the literal iterates of `H(x,y)=(y,f(y)-a x)`, subtracts coordinate `Q`-powers, computes a Gröbner basis over the prime field, counts standard monomials in the exact bounding rectangle, and separately asserts the Jacobian determinant `a^n`. This is an affine quotient-length calculation, not an enumeration of one finite field's orbit points. Reducedness is justified by the proof and the nonzero Jacobian. The formula being tested does not enter construction of the ideal or its standard-monomial count.

The first 36 stored rows exhaust `c0,c1 in F_3`, `c2,a in {1,2}`, with `f=c0+c1 y+c2 y^2` and `(n,r)=(2,1)`. Each has `D=4`, `Q=3`, and stored affine length/prediction `12`. I inspected all 36 parameter rows and their leading monomials; the one- or two-step staircases have the recorded lengths. This is a complete test of that bounded 36-element parameter grid, not all quadratic maps over all fields or clocks.

The remaining eleven nonresonant rows are all listed here. Coefficients are in ascending powers and belong to the prime subfield, including the nonprime-base-field cases.

| `p,q` | Coefficients; `a` | `n,r` | `D,Q` | Stored affine length = prediction |
| --- | --- | --- | --- | --- |
| `3,3` | `[1,0,1]`; `1` | `1,1` | `2,3` | `9` |
| `3,3` | `[1,0,1]`; `1` | `3,1` | `8,3` | `24` |
| `3,3` | `[1,0,1]`; `1` | `4,1` | `16,3` | `48` |
| `3,3` | `[1,0,1]`; `1` | `3,2` | `8,9` | `81` |
| `3,3` | `[1,0,1]`; `1` | `4,2` | `16,9` | `144` |
| `3,9` | `[1,0,1]`; `2` | `2,1` | `4,9` | `81` |
| `5,5` | `[1,2,3]`; `2` | `2,1` | `4,5` | `25` |
| `5,5` | `[1,2,3]`; `2` | `3,1` | `8,5` | `40` |
| `2,2` | `[1,1,0,1]`; `1` | `1,1` | `3,2` | `6` |
| `2,2` | `[1,1,0,1]`; `1` | `2,1` | `9,2` | `18` |
| `2,4` | `[1,1,0,1]`; `1` | `2,1` | `9,4` | `36` |

The separate resonant control is not counted among the 47 nonresonant checks: `p=q=3`, coefficients `[0,0,1,1]`, `a=n=r=1`, stored length `6`, naive max-law `9`. The direct hand elimination in the proof independently explains this number and its distinctness. The saved environment fields are Python 3.12.3 and SymPy 1.14.0.

Section 7's computational description matches these artifacts, including the prime-subfield restriction, bounded-example status, no additional manuscript computation, and warning that the producer normally overwrites the adjacent results file. I did not replay the historical execution or independently attest its process exit code or warning stream. This is a read-only source/saved-output consistency review, not a fresh reproducibility run or a universal bug-freedom claim.

## Seven-mode ARS integrity audit

The statuses below mean **CLEAR within the inspected theoretical-manuscript and saved-evidence scope**, not unconditional certification of software, external publication, or historical runtime. No mode is suspected on the inspected evidence. ML-specific seeds, baselines and effect-size tests are not invented for this pure-mathematics paper.

| Mode | Status | Actual evidence and boundary |
| --- | --- | --- |
| 1. Implementation bug passing AI self-review | **CLEAR within scope** | The complete literal-map producer was read, its construction is independent of the tested max formula, all saved rows and monomial-length surfaces agree, and the general proof does not rely on the program. The adversarial control is independently derived by hand. No fresh run or blanket code-correctness certificate is claimed. |
| 2. Hallucinated citation | **CLEAR within scope** | All six identities and all seven contexts have primary-source support at the access level recorded above. Original Fujiwara/Dwork full-text access is explicitly withheld. No global database or retraction certification is claimed. |
| 3. Hallucinated experimental result | **CLEAR within scope** | Every quantitative check mentioned in Section 7 is present in the hashed saved output: 47 nonresonant examples and one separate resonant control. The manuscript makes no new run, statistical improvement, seed, or benchmark claim. Historical process execution was not replayed. |
| 4. Shortcut reliance | **CLEAR within scope** | Finite examples are not promoted to an all-parameter argument. The theorem follows from degree induction and local algebra for arbitrary allowed coefficients. The examples independently construct the ideal before comparing its length to the formula. |
| 5. Implementation bug reframed as insight | **CLEAR within scope** | The short-twist discrepancy is explained by the proved boundary length, and the resonant failure by explicit elimination with derivative `-1`. Neither is inferred only from surprising numerical output; general short-twist discrepancies are also credited to prior work. |
| 6. Methodology fabrication | **CLEAR within scope** | The described Gröbner procedure, parameter coverage, version fields and overwrite behavior match the supplied code/output. No claim of newly executed computations, all-page inspection, final double builds, human review or external review is substituted for the actual record. |
| 7. Early frame-lock | **CLEAR within scope** | The text distinguishes source arithmetic from target arithmetic, fixed-time slices from fixed-variety zeta functions and genuine diagonal dynamics, and nonresonance from the explicit failing resonant case. It expressly withholds ordinary Hénon zeta, target Euler factors, root numbers, automorphy, zero correspondence and a Hilbert--Pólya realization. A source-side theorem is not used to force target success. |

## Handoff

The corrected source is suitable to proceed to the coordinator's remaining final-source manifest, two fresh-directory builds and complete final-PDF QA. Those gates remain separate from this mathematical review. Author identities, contributions, funding and conflicts are correctly left as author-owned information to be completed before any submission, not fabricated declarations or blockers to an internal anonymous draft.

No author files, frozen contract, saved mathematical code/output, central indexes, evaluation records, Git state, or external services were changed by this review. Its only written deliverable is this report. Any further mathematical or citation change requires an affected-scope follow-up; purely reproducible rebuilding of the M1-corrected source does not by itself reopen the 14 proved claims.
