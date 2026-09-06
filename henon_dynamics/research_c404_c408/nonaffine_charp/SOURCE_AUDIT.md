# Source and access audit — nonaffine_charp

Access date: 2026-09-06. This is a bounded five-source primary-text screen supporting three scout decisions, not an exhaustive literature review. Titles/abstracts were used to route retrieval, not to certify theorem coverage. No full-workspace upload, paid model review, automated citation-count score, or unseen-source attribution was used.

## Verified sources and exact use

| ID | Primary source | Body actually inspected | Claim supported; boundary |
|---|---|---|---|
| S1 | Jun Bo Lau, Travis Morrison, Eli Orvis, Gabrielle Scullard, Lukas Zobernig, *Zeta functions of abstract isogeny graphs and modular curves*, arXiv:2509.15214, [accessible HTML](https://arxiv.org/html/2509.15214v1); [PDF](https://arxiv.org/pdf/2509.15214) | Introduction §§1.1–1.3; §2.2; definitions 3.1, 4.1–4.4; lemma 4.11, theorem 4.12 and proof; definitions/proposition 5.1–5.3; theorem 6.9 and proof; corollary 6.10, examples 6.11–6.12, §7.1 through remark 7.7; PDF pp.12–14 checked after cross-audit | Ownership of definitions/framework, including reversal formalism. A real odd-cycle sign error prevents unrestricted reliance on the printed cycle-product theorem; see the explicit caveat below. No new arithmetic theorem for an actual isogeny graph was derived from that error. |
| S2 | Michiel Hazewinkel (2008), *Witt vectors. Part 1*, [arXiv:0804.3888 PDF](https://arxiv.org/pdf/0804.3888) | §5.1–5.2 statement, §5.9–5.15 addition/construction passage; §7.1 truncation and coordinate Frobenius passage, equations (7.3)–(7.4) | Witt group law and truncation explaining hidden group structure. The length-two calculation and counting proof were written explicitly in this lane. Not all 148 pages read. |
| S3 | Jakub Byszewski, Gunther Cornelissen, Marc Houben, *Dynamics of endomorphisms of algebraic groups: Including the general theory of FAD systems*, [arXiv:2209.00085v2](https://arxiv.org/pdf/2209.00085v2) | Front matter/introduction; the §4.4 definitions and Lang–Steinberg theorem 4.4.5 with remark 4.4.6, recovered in a body-text find result | The connected-group Lang-map mechanism is classical and explicitly credited there to earlier work. Our translation is not itself a group endomorphism fixing the identity, so we use conjugacy, not a careless direct application of an endomorphism zeta theorem. Not all 176 pages read. |
| S4 | William M. Goldman and Walter D. Neumann (2005), *Homological action of the modular group on some cubic moduli spaces*, [author PDF](https://www.math.columbia.edu/~neumann/preprints/wmgwdn2.pdf); [published primary PDF](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2005/0012/0004/MRL-2005-0012-0004-a011.pdf) | Author text Introduction/Theorem 1 and mod-2 action description; §4 coordinate projection and special-fiber factorization (PDF p.8); relevant returned passages in §§1–2 | Classical conic decomposition and finite homological action over C. Does **not** directly prove the finite-field point formula in this lane. The source uses x²+y²+z²−xyz−2=t; our κ is t+2. |
| S5 | Alois Cerbu, Elijah Gunther, Michael Magee, Luke Peilen, *The cycle structure of a Markoff automorphism over finite fields*, [arXiv:1610.07077 PDF](https://arxiv.org/pdf/1610.07077) | Abstract, introductory problem framing, theorem 1.5 and surrounding discussion, definition 1.8/proposition 1.9, conjecture 1.10 and surrounding statement | Distinguishes a hyperbolic finite-field longest-orbit problem from our parabolic Frobenius-twist problem. It supports what was proved/conjectured in this source; not a claim that all later developments have been excluded. |

## Metadata and access cautions

S1's returned HTML carries the header `arXiv:2509.15214v1 ... 18 Sep 2025` but the body has `Date: August 24, 2026`. The directly accessed PDF instead prints `Date: September 19, 2025` and the same arXiv v1 header. This audit does not certify bytewise identity of HTML and PDF or provenance of every line. The current selection decision does not depend on resolving that metadata discrepancy. Some HTML displays do have duplicated rendering fragments, but the odd-cycle sign problem below also appears in the PDF and **is not** dismissed as a rendering artifact.

## Literal-formula caveat discovered by independent AI cross-audit

The arithmetic scout identified, and this lane then independently checked, the source's Lemma 4.11 in both HTML and PDF pp.12–13. It asserts the cycle contribution to det(I+sP_k) is 1−sᵏ for all k>1. For a permutation k-cycle the two nonzero determinant terms instead give

\[
\det(I+sP_k)=1+(-1)^{k-1}s^k=1-(-s)^k.
\]

In particular det(I+sP₃)=1+s³. This is an actual algebraic sign issue in the accessed source. The abstract-graph theorem cannot be saved merely by the regularity condition: take one vertex, three loops, J a 3-cycle and L=id. It satisfies definition 3.1, is 3-regular, and has A=[3], Q=[2]. Its non-backtracking transition operator is B=J₃−P₃, where J₃ here means the all-ones matrix. The vector (1,1,1) has eigenvalue 2 and the two other eigenvalues are −ω,−ω². Hence

\[
\zeta(u)=\det(I-uB)^{-1}
=\frac{1+u}{(1-2u)(1+u^3)}.
\]

The printed theorem 4.12 instead produces (1+u)/((1−2u)(1−u³)). Thus its unrestricted abstract claim is false as printed. The same faulty cycle expansion feeds the displayed correction term of theorem 6.9, so we do not certify those odd-cycle cases without correction. We do **not** claim that this three-loop example is realized by an actual supersingular elliptic isogeny graph or that every arithmetic specialization fails.

The determinant identity preceding the final cycle expansion retains the framework and exposes the local sign repair. This bounded observation is a source-reliability limitation, not a retained correction paper or a newly completed isogeny arithmetic contract. Final selection status remains zero. The initial stronger phrase “direct theorem ownership” was revised to “definitions/framework already owned, with no new arithmetic lemma established.”

S3's body find returned the full Lang–Steinberg statement and the next remark. Later attempts to open the same narrow range returned an internal access error. We record the successful body access, not an invented successful second opening. Its theorem 4.4.5 explicitly assumes a connected algebraic group and an endomorphism with finitely many fixed points. Our coordinate proof needs no unavailable pages.

For S4, the author-hosted body is the text actually used for mathematics. The published entry identifies *Mathematical Research Letters* 12 (2005), 575–591; publisher metadata is not substituted for reading the author's theorem. Search snippets about other Markoff papers, an uninspected recent Nielsen-equivalence paper, and secondary ResearchGate summaries were not admitted as support.

## Search scope and negative-evidence discipline

Queries combined positive-characteristic/non-affine dynamics, Witt translation/Frobenius, supersingular isogeny primitive/non-backtracking zeta, Markov/Markoff cubic Frobenius twists, conic fibers and finite-field cycle lengths. Existing local C399–C403 reserve notes were read as collision pointers, not as primary mathematical authority. Other local files were searched narrowly for topic overlap; this is not a repository-wide theorem audit. Parallel teammates owned resonant Hénon and nonlinear birational/proper-surface lanes, so those were not duplicated here.

Three adversarial checkpoints were applied: (1) challenge hidden group conjugacy before selecting a nonlinear polynomial; (2) challenge supposed source gaps with actual recent theorem bodies; (3) separate correctness of a short formula from sufficient research contribution. A second AI scout then challenged the reliability of the S1 printed formula and produced the caveat above. Result: one framework-owned/no-new-arithmetic-lemma rejection, one hidden-group rejection, one insufficient-increment rejection. None implies a global impossibility theorem for all non-affine characteristic-p dynamics.

AI/source disclosure: initial derivation and source screening were performed by the same AI scout, with reproducible symbolic checks; a separate AI lane supplied the later read-only cross-audit and S1 challenge, which this lane verified and incorporated. No independent human expert review or globally complete novelty certification is claimed. No ML metrics, citation-score ranking, or numerical extrapolation were used to make a mathematical theorem claim.
