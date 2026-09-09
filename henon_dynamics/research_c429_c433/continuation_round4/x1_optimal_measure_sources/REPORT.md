# R4 X1 — bounded source audit for LRL Problem 1.3

Date: 2026-09-09 UTC. Scope: primary-source collision check only. No mathematical computation, author-proof review, shared-file modification, or priority certification.

## Outcome

**No verified post-2013 theorem answering the exact selected-optimal-cycle convergence question was located in this bounded search.** This is a search outcome, not a claim that the problem remains open everywhere, and not a novelty or priority guarantee for the developing proof.

The closest inspected convergence theorem concerns a different sequence of measures. The inspected later papers citing optimal cycles extend ramification criteria and periodic-point norm bounds, not the requested weak-* convergence. No checked source can presently be subtracted as an already published solution of the exact target below.

## Frozen target and original source

Let $K$ be complete and algebraically closed with an ultrametric absolute value, $\operatorname{char}K=p>2$, and $0<|\lambda-1|<1$. Put

\[
P_\lambda(z)=\lambda z+z^2,\qquad
\mu_e=p^{-e}\sum_{z\in\Pi_e}\delta_z,
\]

where $\Pi_e$ is the unique cycle of minimal period $p^e$ inside the open unit disk. The question is convergence of this selected sequence on Berkovich $\mathbf P^1_K$, not degree-normalized counting of all periodic points of the polynomial.

Lindahl–Rivera-Letelier formulate exactly this as Problem 1.3, printed pp. 4–5. The preceding paragraph gives the constant radius $|\lambda-1|^{(p-1)/p}$; the paragraph after the question says that accumulation measures are invariant, but does not identify their support types or prove uniqueness. The existence input is their optimal-cycle theorem, specialized to this quadratic. [Primary text, arXiv:1311.4478v3](https://arxiv.org/pdf/1311.4478v3).

Bibliographic clarification: the preprint began in 2013; the journal paper is *Compositio Mathematica* 152(1), 187–222 (2016), DOI 10.1112/S0010437X15007575, published online 7 September 2015. [Publisher record](https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/optimal-cycles-in-ultrametric-dynamics-and-minimally-ramified-power-series/83B7D75267327F3D0B76E9E6B47BE8F7).

## Closest primary statements checked

### 1. Actual weak convergence, but different measures: Jacobs

Kenneth Jacobs, *Equidistribution of the crucial measures in non-Archimedean dynamics*, arXiv:1409.4808v2, 28 April 2017.

Theorem 2, printed p. 2, assumes a complete algebraically closed non-Archimedean $K$ and a rational map $\phi$ of degree $d\ge2$. It proves weak convergence of Rumely's crucial measures $\nu_{\phi^n}$ to the canonical measure. There is no characteristic-zero restriction on this theorem; the later Theorem 3 has one.

The definition on printed p. 1 is

\[
\nu_\phi=(d-1)^{-1}\sum_Q w_\phi(Q)\delta_Q.
\]

The weights vanish at types I, III, and IV, and depend on reduction at type II points. Consequently these are not the equal-weight measures on $\Pi_e\subset K$. This is a measure-definition mismatch, not an excluded-field argument.

Proof passages checked: §4.2 Laplacian comparison, §4.3 test-function estimate, and the complete proof of Theorem 2 on printed pp. 24–25. The argument approximates continuous functions by piecewise affine functions on finite trees and uses estimates specific to resultant/crucial measures. No estimate for the selected orbit measures is supplied. [Primary text](https://arxiv.org/pdf/1409.4808).

### 2. A later optimal-cycles citation answering a different question: Nordqvist–Rivera-Letelier

Jonas Nordqvist and Juan Rivera-Letelier, *Residue fixed point index and wildly ramified power series*, arXiv:1904.04494v3, 3 February 2020.

Theorem 3, printed p. 5, treats an ultrametric field of odd characteristic $p$, $1\le q<p$, and an integral series

\[
f(z)=z(1+az^q)+O(z^{q+2}),\qquad a\ne0.
\]

Its conclusion for non-fixed periodic points is the norm bound $|z|\ge |a|\,|\operatorname{r\acute esit}(f)|^{1/p}$. Theorem 2 characterizes $q$-ramification using iterative residue. These statements concern a multiplier exactly equal to $1$, rather than directly the target multiplier $\lambda\ne1$.

The full proof of Theorem 3 in §4.2, printed p. 19, combines explicit iterate coefficients with Lemma 7's periodic norm bound. The following remark discusses equality and concentration on a sphere, not measures. The paper explicitly reports progress on LRL **Conjecture 1.2** and Kallal–Kirkpatrick's Conjecture 4.3; this must not be confused with LRL **Problem 1.3**. No convergence or type-support theorem for the target sequence was found in the checked statements/proofs. [Primary text](https://arxiv.org/pdf/1904.04494).

### 3. The preceding citation branch: Kallal–Kirkpatrick

Kenz Kallal and Hudson Kirkpatrick, *Ramification of Wild Automorphisms of Laurent Series Fields*, arXiv:1611.01077v3 (2019).

Theorem 1.6 gives a finite-coefficient criterion for $b$-ramification when $p>b^2$. Its proof and §4, printed pp. 12–13, were checked. The application is a lower bound on periodic-point norms; the period-independent extension is Conjecture 4.3, with a note about the Nordqvist–Rivera-Letelier proof. Neither this statement nor the application treats weak convergence of $\mu_e$. Thus the subsequent resolution of that conjecture is not a resolution of the selected-cycle question. [Primary text](https://arxiv.org/pdf/1611.01077).

## Type-support and scope guardrails

These are audit conclusions, not a new theorem about the limit:

- Every atom of each target $\mu_e$ is type I. This alone does **not** determine the types charged by a weak-* limit.
- Fixed classical absolute value does not by itself identify a unique Berkovich limiting measure or its type support.
- Jacobs supplies a type-II-supported approximating sequence with a different definition. Identifying its limit with a prospective limit of $\mu_e$ would require an additional argument absent from the inspected proof.
- Neither a canonical/equilibrium measure theorem for all periodic points nor a theorem about all Galois conjugates is automatically a theorem for the single local cycle $\Pi_e$.
- No full Galois nesting assertion, interlevel coupling estimate, or developing author-side convergence proof was used as source evidence in this audit.

## Search coverage and access limitations

The search combined exact-question, optimal-cycle, neutral/indifferent-cycle, and Berkovich-measure formulations. Representative executed queries include:

1. `"Lindahl" "Rivera-Letelier" "Problem 1.3" measures`
2. `"optimal cycles" "convergence" Berkovich`
3. `"optimal cycles" "equidistribution"`
4. `"optimal cycles" ultrametric measures convergence`
5. `"Lindahl" "Rivera-Letelier" Berkovich weak convergence periodic cycles`
6. `"Problem 1.3" "optimal cycles" solution`
7. `site:arxiv.org Berkovich neutral indifferent periodic cycles equidistribution` — 184-day recency filter.
8. `site:arxiv.org "optimal cycles" 2024 2025 2026`
9. `site:arxiv.org "minimally ramified" measure convergence` — 184-day recency filter.
10. `site:scholar.google.com "Optimal cycles in ultrametric dynamics"`
11. `site:semanticscholar.org "Optimal cycles in ultrametric dynamics"`

Additional searches combined the explicit quadratic/multiplier with Berkovich convergence, and queried recent optimal-cycle and periodic-orbit-measure work. The 184-day filter covered approximately 9 March–9 September 2026; explicit 2024–2026 arXiv queries provided a wider recent pass. No matching new solution surfaced. Crawl dates on old papers were not treated as publication dates.

Citation discoverability was attempted through the Cambridge record's citation tools, its Google Scholar link, a direct Scholar exact-title query, Semantic Scholar domain search, and Semantic Scholar's public graph endpoint for `ARXIV:1311.4478`. Direct Scholar/graph retrieval did not succeed. Cambridge reported unavailable CrossRef cited-by data; this was **not** interpreted as zero citations. Accordingly this audit does not claim a complete forward-citation graph.

Local-first title/name checks found no task-matching accessible PDF or usable local arXiv-fetch helper. No configured Zotero/Obsidian/Semantic Scholar retrieval tool was available, so primary PDFs were accessed through the web fallback. Search hits alone were used for discovery, not theorem admission.

One 2023 university-hosted hit was inspected and excluded: it is a two-page thesis proposal about Artin–Mazur zeta functions, not a completed selected-cycle convergence theorem. Its bibliography helped locate the later ramification papers above. [Proposal](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/d_crncevic23.pdf).

## Handoff

Safe statement: **the checked sources do not already supply the exact LRL Problem 1.3 conclusion, and this bounded search located no verified later solution.** Unsafe statement: that the problem is definitively still open, that any prospective proof is first, or that generic Berkovich equidistribution settles it.

The author-side convergence argument remains subject to independent mathematical review. This source report neither validates nor invalidates that argument. All older reports, the R4 Fricke report, source files, and shared research records were left unchanged.
