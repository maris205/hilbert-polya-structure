# Source ownership and admission audit: nonlinear resonant Hénon counts

Date: 2026-09-06. This is a bounded primary-source comparison for the single contract in [PROOF_PACKAGE.md](PROOF_PACKAGE.md), not a global novelty certificate, a journal acceptance prediction, or a formal Route-A evaluation. The proof, source comparison, and exact checks are different evidence streams.

## 1. Exact proposed increment

For $H(x,y)=(y,y^q+g(y)-ax)$ over $\mathbb F_q$, with $a\ne0$, $2\le m=\deg g<q$ and $p\nmid m$, the proposed result is the **coefficient-uniform all-period resonant count**

$$
\#\{H^n(P)=\Phi_q^n(P)\}
=\frac{(m-1)q^{2n}+(q-m)q^{2n-p^{v_p(n)}}}{q-1}.
$$

The actual new proof obligation is the nonlinear leading-term calculation for every level of the $p$-divisibility tower, not finiteness of one fixed scheme or a renamed zeta function. The proof uses commuting *linear pullbacks on a polynomial ring* to justify the binomial identity. It never applies that identity to a difference of nonlinear point maps.

The zeta product and its natural boundary are included as consequences of this same count. The analytic mechanism of valuation-distorted counts producing nonrational or natural-boundary zeta functions is already established literature and is **not** separately claimed as an original research direction.

## 2. Closest primary sources: actual access and scope

### S1. Byszewski–Cornelissen–Houben, algebraic-group dynamics

Jakub Byszewski, Gunther Cornelissen, Marc Houben, *Dynamics of endomorphisms of algebraic groups*, [arXiv:2209.00085v2](https://arxiv.org/abs/2209.00085v2), revised 19 April 2024. The official abstract and [author HTML](https://arxiv.org/html/2209.00085v2) were accessed. Relevant text actually read: Theorem A / Theorem 8.2.1; §5.2, including the additive-coordinate description, Smith/Dieudonné reduction, degree and inseparable-degree arguments, and Theorem 5.2.5; introductory Theorem C / Theorem 11.3.3.

Its input is an algebraic-group endomorphism with finite fixed sets for every iterate. Theorem 5.2.5 supplies the vector-group fixed-count formula; the broader work owns finite-adelic distortion and corresponding analytic dichotomies. This is a major mechanism owner, but is not a stated theorem about arbitrary nonlinear polynomial maps of the affine plane. We did not read all 176 pages or claim journal publication metadata not displayed by the consulted record.

### S2. Bridy, polynomial maps of the affine line

Andrew Bridy, *Transcendence of the Artin-Mazur Zeta Function for Polynomial Maps of $\mathbb A^1(\overline{\mathbb F}_p)$*, Acta Arithmetica **156** (2012), no. 3, 293–300, DOI [10.4064/aa156-3-6](https://doi.org/10.4064/aa156-3-6). Bibliographic data were checked through official publisher results and the [author's publication list](https://campuspress.yale.edu/andrewbridy/). The [official arXiv record](https://arxiv.org/abs/1202.0362) and [author PDF](https://arxiv.org/pdf/1202.0362) were accessed; the consulted PDF is v2, 14 May 2012.

Actual theorem locators are **Theorems 1 and 2**, printed page 3, and the opening proof of Theorem 1 on pages 3–4. In one variable, derivative-zero polynomials have rational fixed-point zeta; the same paper treats transcendental examples. These statements neither imply nor contradict our two-dimensional result. No claim is made that the present family is the first positive-characteristic transcendental dynamical zeta, or even the first higher-dimensional example. A repeated attempt to open the publisher download timed out; the theorem text was read in the author PDF, not falsely attributed to a successful publisher-full-text session.

### S3. Dynamically affine maps and quotient mechanisms

Jakub Byszewski, Gunther Cornelissen, Marc Houben, with Lois van der Meijden co-authoring Appendix B, *Dynamically affine maps in positive characteristic*, [arXiv:1904.04942v1](https://arxiv.org/abs/1904.04942), 9 April 2019. Both the official metadata and [author PDF](https://arxiv.org/pdf/1904.04942) were accessed.

The definitions immediately preceding Theorem A and Theorems A–B on printed page 7 were read. Theorem A concerns dynamically affine maps on $\mathbb P^1$; Theorem B treats specified Kummer-variety maps. The text also states an abstract higher-dimensional framework under hypotheses (H1)–(H4). This audit does **not** verify those hypotheses for our affine-plane map or silently apply its dichotomy to an unconstructed quotient presentation. It identifies an important remaining collision check, not a proof that every hidden dynamically affine model has been excluded.

### S4. Classical polynomial-ideal input

David A. Cox, John Little, Donal O'Shea, *Ideals, Varieties, and Algorithms*, 4th edition, Springer, 2015, DOI [10.1007/978-3-319-16721-3](https://link.springer.com/book/10.1007/978-3-319-16721-3). The official book metadata and chapter listing were accessed. This is a classical pointer for the coprime-leading-monomial criterion and standard-monomial basis used in proof §6. We did not obtain the complete official chapter text, and therefore do not certify a page-level full-text verification of the book. Search-discovered third-party book copies were not used as authoritative sources.

This classical input is not the claimed increment. For the special pair here, normalize $f=x^Q+f_0$ and $h=y^d+h_0$. Their sole $S$-polynomial has the representation

$$
y^d f-x^Q h=f_0h-h_0f,
$$

whose two products have leading monomials strictly below $x^Qy^d$. Buchberger's usual criterion therefore applies, and its standard monomials give exactly the stated rectangle. The alternative Bézout proof in the package checks the actual leading forms before counting; neither route is a new intersection-theory theorem.

## 3. A stronger, but explicitly limited, additive-model exclusion

Standard-coordinate nonadditivity is easy but insufficient as a collision audit. There is a coordinate-independent obstruction to a more specific competing claim:

**Observation.** Our system cannot be conjugate, even as a set-theoretic dynamical system on geometric points, to a confined algebraic-group endomorphism of any vector group $\mathbb G_a^d$ in characteristic $p$.

Indeed, the first fixed set of any such endomorphism $\sigma$ is the finite subgroup $\ker(\sigma-I)(K)$ of $\mathbb G_a^d(K)$. It is a finite-dimensional $\mathbb F_p$-vector space, so its cardinality is a power of $p$. In our family, the elementary first-period elimination gives $N_1=qm$. Because $m>1$ and $p\nmid m$, this is not a power of $p$. A conjugacy preserves fixed-set cardinalities, which is a contradiction. This is an elementary finite-group argument, not a new algebraic-group classification theorem.

The observation separates the candidate from the **direct vector-group endomorphism** case and from the prior round's additive Hénon family. It does not rule out a finite quotient, a different algebraic group, a birational model on a restricted domain, or an abstract relation at the level of zeta sequences. No blanket “not dynamically affine” theorem is claimed. The existence of an unrecognized such presentation remains a legitimate admission risk.

## 4. Repository ownership and exact delta

| Existing owner | What is already owned | Difference in this contract |
|---|---|---|
| [C401 nonresonant contract](../../continuation_c399_c403_round2/henon_arithmetic/CONTRACT_SCOUT.md) | The two-clock nonresonant max-law; threshold slices and their distinction from geometric zeta; a first-period resonant counterexample | Here $\deg H^n=q^n$ for every period. The proof closes the excluded resonance for a whole nonlinear degree/coefficient family and all wild periods. It does not merely add the known count 6 instead of 9. |
| [Previous-round arithmetic scout, §2](../../research_c404_c408/henon_arithmetic/SCOUT_REPORT.md) | Additive resonant maps reduce directly to vector-group endomorphisms and collide with S1 | The present family has $m>1$, $p\nmid m$, and the preceding fixed-cardinality obstruction excludes that direct vector-group model. |
| [Previous-round arithmetic scout, §3](../../research_c404_c408/henon_arithmetic/SCOUT_REPORT.md) | Five exact examples, including failures of a constant-density extrapolation; no all-period proof | The new leading-degree lemma gives every cancellation level, arbitrary lower coefficients, and the explicit all-period formula. The former open obligation, not its empirical table, is the starting point. |
| [Wild-additive analytic proof](../../henon_wild_additive_geometric_zeta_route_a/proof/ANALYTIC_PROOF.md) | Valuation-dependent counts and natural-boundary mechanisms for additive maps | Those analytic ideas are acknowledged. The candidate's admission rests on the new nonlinear all-period count, not on the existence of an Euler-type product or natural boundary alone. |

The sealed prior-round files were read as existing evidence, not edited or rerun. In particular, the old finite examples are not counted as new validation runs.

## 5. New exact evidence and hypothesis attack

[CHECK_RECEIPT.md](CHECK_RECEIPT.md) and [exact_results.json](exact_results.json) document five newly composed examples. They test lower-coefficient perturbation, a prime-power base size with wild clock, genuine non-prime-field coefficients, a second $p$-power level, and an out-of-hypothesis nonlinear degree. Three have a secondary F5B quotient-length check; the genuine $\mathbb F_4$ cases explicitly do not claim a SymPy extension-field Gröbner run.

The strongest tested extension failure is $q=8$, $g=y^6+y^3+1$, $a=1$, $n=2$. The actual count is 2816, whereas deleting $p\nmid m$ from the proposed formula gives 2944. Thus the hypothesis is substantive. This is a single counterexample to an overextension, not a classification of all degrees divisible by $p$.

The universal claim is proved in the package; no finite agreement is promoted to an all-period theorem. The package also does not claim ordinary-period counts over fixed finite fields, a Hasse–Weil zeta, Euler factors across primes, a target zero correspondence, or a finite-dimensional characteristic-zero trace realization.

## 6. Search coverage, limitations, and decision

The search began with the repository's already owned contracts and closest cited mechanisms. Available-tool inspection found no Zotero or Obsidian connector; relevant local PDF filename searches yielded no additional primary Hénon/Frobenius document. Primary-source web searches included Hénon/Henon with Frobenius, resonance, positive characteristic, periodic points, purely inseparable maps, and dynamical zeta, including recent-year variants. Unrelated Perron–Frobenius hits were excluded. No Semantic Scholar, Scopus, external model, paid API, manuscript upload, or unperformed local-PDF preflight is claimed.

The consulted sources did not supply this specific nonlinear coefficient-uniform all-period count. That is a **bounded search outcome**, not proof of global priority. Only the listed relevant sections were inspected; no whole-monograph or all-citation audit is asserted. Sources S1–S3 are mathematical primary research, with author-preprint scope stated explicitly rather than a fabricated venue-integrity certificate.

The proof-writing, literature/novelty checks, and scoped ARS primary-source discipline guided the distinction between the new algebraic obligation and the already owned analytic machinery. The current user-authorized pure-mathematics task overrides old-template model calls, ML quotas, and full-pipeline checkpoints. This remains work by the current AI team, not external human peer review.

**Recommendation to the parent:** retain this one unnumbered contract for independent proof and admission review. There is a complete quantified proof, a clear repository gap closed beyond finite special cases, and a stronger direct-additive collision exclusion. Possible unrecognized quotient/group presentations and global bibliographic priority remain open risks. Do not split the zeta corollary into another candidate, assign a paper number, or treat source-system success as target-arithmetic success on this audit alone.
