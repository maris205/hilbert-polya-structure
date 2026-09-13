# Batch 06 — Paper 23 Candidate Novelty / Portfolio Review R1

## Review identity and frozen candidate

- Review role: fresh independent candidate novelty/portfolio reviewer R1.
- Review cutoff: 2026-08-24 UTC.
- Candidate ID: `hamiltonian_quartic_spectral_escape_v1`.
- Public title: **Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies**.
- Conditionally proposed future project path: `papers/23-hamiltonian-quartic-spectral-escape`.
- That project path is not created by this review and remains conditional on later authorization.
- The review was performed independently of Paper 23 candidate review R2 and independently of the candidate-scout agent record. Neither was opened or used.

## Gate decision

**Decision: PASS, with narrow novelty margin and mandatory theorem-boundary controls.**

| Dimension | Score | Required threshold | Result |
|---|---:|---:|---|
| Novelty / portfolio differentiation | **7.8 / 10** | 7.5 | PASS |
| Standalone-paper potential | **8.3 / 10** | 7.5 | PASS |
| Proof plausibility | **9.1 / 10** | 9.0 | PASS |

This is not an absolute-priority finding. It means only that, within the frozen Papers 12–22 portfolio and the bounded public search described below, I found no theorem-level collision with the complete package

> explicit four-mode Hamiltonian alternating product shears + four staggered selectors + an invariant cone + exact (BA) degree recurrence + (q_4) visibility + the stated quartic characteristic polynomial + an infinite irreducible quartic Perron subfamily for (g\equiv3\pmod 5).

The reusable selector/matrix/Perron proof architecture is already heavily represented in Papers 20–22. The candidate passes because its concrete four-spike construction removes the common unit sector responsible for Paper 22's cubic collapse and yields a genuinely quartic, visible spectral family—not because matrix recurrences, Perron–Frobenius theory, support rank, or common-kernel reasoning are new.

## Exact frozen family and candidate theorem

Let (K) be a field of characteristic zero and (g\ge 10). On (K^8) with canonical coordinates

\[
(q,p)=(q_1,q_2,q_3,q_4,p_1,p_2,p_3,p_4),
\]

set

\[
V_g(q)=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},
\]

\[
W_g(p)=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g.
\]

With the sign convention

\[
S_{V_g}(q,p)=(q,p-\nabla V_g(q)),\qquad
T_{W_g}(q,p)=(q+\nabla W_g(p),p),
\]

the candidate map is

\[
F_g=T_{W_g}\circ S_{V_g}.
\]

Changing both standard shear signs does not change the degree calculation, but the eventual paper must fix one convention and one composition order before stating any recurrence.

The candidate theorem to be proved standalone is:

1. (F_g) is a polynomial symplectic automorphism over every characteristic-zero field (K).
2. Four strict selector inequalities hold on a forward-invariant degree cone containing the ordinary seed.
3. If (u_n) is the four-vector of (q)-coordinate degrees after (n) full iterates, then
   \[
   u_n=C_g^n\mathbf 1,
   \qquad \mathbf1=(1,1,1,1)^T,
   \]
   and the intermediate (p)-degree vector is (A_gC_g^{n-1}\mathbf1) for (n\ge1).
4. The fourth (q)-coordinate is visible at every positive iterate, so
   \[
   \deg(F_g^n)=e_4^TC_g^n\mathbf1.
   \]
5. Consequently the degree sequence obeys the exact order-four recurrence induced by the characteristic polynomial below and
   \[
   \lambda(F_g)=\rho(C_g).
   \]
6. For (g\equiv3\pmod5), (g\ge10), this Perron root has algebraic degree exactly four, producing an infinite subfamily of distinct quartic Perron numbers.

## Independent selector and matrix recomputation

Put

\[
h=g-1,\qquad k=g-2.
\]

The mixed derivative monomial has exponent matrix (2\mathbf1\mathbf1^T-I_4). The selected pure (q_1,q_2) branches in the first shear and pure (p_3,p_4) branches in the second shear give

\[
A_g=
\begin{pmatrix}
h&0&0&0\\
0&k&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
\qquad
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&k&0\\
0&0&0&h
\end{pmatrix}.
\]

Hand multiplication gives

\[
C_g=B_gA_g=
\begin{pmatrix}
h+8&2k+8&6&6\\
2h+8&k+8&6&6\\
2k&2k&k&2k\\
2h&2h&2h&h
\end{pmatrix}.
\]

For a positive input degree vector (u=(u_1,u_2,u_3,u_4)^T), the four selected-branch wall functionals can be written as

\[
\begin{aligned}
L_1(u)&=k u_1-2u_2-2u_3-2u_4,\\
L_2(u)&=-2u_1+(k-1)u_2-2u_3-2u_4,\\
L_3(u)&=-8u_1-6u_2+(g-7)u_3+(2g-8)u_4,\\
L_4(u)&=-6u_1-4u_2+(2g-6)u_3+(g-6)u_4.
\end{aligned}
\]

At the ordinary seed, accounting for the intermediate vector (A_g\mathbf1=(h,k,7,7)^T), their strict selector margins are

\[
g-8,\qquad g-9,\qquad 3g-29,\qquad 3g-22.
\]

At (g=10) these are (2,1,1,8), so all four branches are strictly selected. At (g=9) they are (1,0,-2,5): the second first-shear selector ties and the third second-shear selector loses. Thus (g\ge10) is the exact threshold for this four-selector ordinary-seed mechanism. This does **not** prove that all smaller (g) lack quartic behavior under some other branch regime.

The first exact (q)-degree vector is

\[
C_g\mathbf1=(3g+23,\ 3g+24,\ 7g-14,\ 7g-7)^T,
\]

which makes (q_4) strictly visible at the first full iterate. The proposed proof route for all iterates is credible, but the manuscript must provide a symbolic wall-by-wall certificate that its chosen cone is forward invariant and that (q_4) remains the scalar maximum. Finite samples cannot replace this certificate.

## Independent characteristic-polynomial computation

Using the trace, all principal (2\times2) and (3\times3) minors, and the determinant—not a finite-(g) interpolation—I obtain

\[
\operatorname{tr}(C_g)=4g+10,
\]

\[
e_2(C_g)=-2g^2-26g+45,
\]

\[
e_3(C_g)=-12g^3+70g^2-126g+72,
\]

\[
\det(C_g)=9(g-1)^2(g-2)^2.
\]

Therefore

\[
\boxed{
\begin{aligned}
\chi_{C_g}(t)
={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}}
\]

If (d_n=e_4^TC_g^n\mathbf1), Cayley–Hamilton gives

\[
\begin{aligned}
d_{n+4}={}&(4g+10)d_{n+3}+(2g^2+26g-45)d_{n+2}\\
&-(12g^3-70g^2+126g-72)d_{n+1}\\
&-9(g-1)^2(g-2)^2d_n.
\end{aligned}
\]

The recurrence becomes a theorem about total degrees only after the invariant-cone, old-coordinate suppression, noncancellation, and (q_4)-visibility lemmas are proved.

For (g\ge10), every entry of (C_g) is strictly positive. Perron–Frobenius therefore supplies a simple positive spectral radius that strictly dominates the moduli of the other eigenvalues. Once the exact degree recurrence is established, this gives (lambda(F_g)=\rho(C_g)).

## Hand proof of the (g\equiv3\pmod5) subfamily

For (g\equiv3\pmod5), reduction of the displayed characteristic polynomial gives

\[
\overline\chi(t)=t^4+3t^3+4t^2+1\in\mathbf F_5[t].
\]

Its values at (0,1,2,3,4) are respectively

\[
1,4,2,4,3,
\]

so it has no linear factor. If it factored as

\[
(t^2+at+b)(t^2+ct+d),
\]

then

\[
bd=1,\qquad a+c=3,\qquad ac+b+d=4,\qquad ad+bc=0.
\]

Writing (d=b^{-1}), the last equation gives (a=-b^2c), hence

\[
c(1-b^2)=3.
\]

For (b=1,4), the left side is zero. For (b=2,3), one obtains (a=c=4), but then (ac+b+d=1\ne4). Thus no quadratic factor exists, and (overline\chi) is irreducible over (mathbf F_5). Gauss's lemma and reduction modulo (5) imply that (chi_{C_g}) is irreducible over (mathbf Q).

The Perron root consequently has algebraic degree four for

\[
g=13,18,23,\ldots.
\]

These roots are pairwise distinct: if two were equal, their monic irreducible degree-four minimal polynomials would coincide, but the (t^3) coefficient ( -(4g+10)) determines (g).

No CAS calculation and no finite list of numerical factorizations is being used as the irreducibility certificate.

## Papers 12–22 portfolio audit

I independently inspected the local source/PDF content of Papers 12–22. Papers 12–19 concern period-three Hénon trace/residue structure, primitive-cycle covers, monomial Hénon torus escape, quartic Hénon trace fibers, support-size escape, shift-like torus-coset decay, marked Hénon scalar boundaries, and translate/gcd obstructions. They provide broad degree-growth context but no direct theorem collision with this four-mode Hamiltonian product-shear family.

The material collisions begin with Papers 20–22:

- **Paper 20:** already establishes the selector-to-nonnegative-matrix-to-Perron architecture for two-mode Hamiltonian product shears and a quadratic spectral outcome.
- **Paper 21:** extends essentially the same architecture to three modes, exact matrix degree growth, a cubic characteristic polynomial, and infinite cubic Perron subfamilies.
- **Paper 22:** is the closest neighbor. Its endpoint-only spikes in arbitrary mode number retain a common unit sector and therefore force cubic spectral collapse. Its support-rank/common-kernel explanation is directly reusable background, not a new Paper 23 claim.

### Claims × neighbors collision matrix

| Paper 23 candidate claim | Papers 12–19 | Paper 20 | Paper 21 | Paper 22 | Closest public neighbors | Judgment |
|---|---|---|---|---|---|---|
| Four staggered selectors and invariant cone | No direct collision | Medium method collision | High method collision | High method collision | No same four-spike family found | Concrete wall system is incremental; selector method is not new |
| Exact (BA) vector recurrence | No direct collision | Two-dimensional precedent | Three-dimensional precedent | Arbitrary-mode precedent with collapse | General degree-growth context only | Exact candidate matrix is distinct; recurrence method cannot be a novelty headline |
| (q_4)-visible scalar recurrence | No direct collision | Low-dimensional visibility analogy | Three-mode visibility analogy | Visibility inside cubic-collapse regime | No same coordinate/matrix located | Retain only as a theorem specific to this family |
| Explicit escape from cubic collapse | No direct collision | Quadratic spectrum | Cubic spectrum | Strongest contrast: forced cubic collapse | Shao–Sun gives a broad degree-four bound in another class | Clear portfolio delta if proved standalone |
| Infinite (g\equiv3\pmod5) irreducible quartic Perron subfamily | No direct collision | Quadratic families | Cubic families | Cubic families | Blanc–van Santen realizes weak Perron numbers generally | Novelty lies in this restricted symplectic explicit family, not general Perron realization |
| Support-rank/common-kernel explanation | No direct collision | Structural precursor | Structural precursor | Direct explanatory collision | Standard linear-algebra mechanism | Explicitly nonnovel; explanation only |

The portfolio novelty score is held to 7.8 because Papers 20–22 already supply almost all of the proof grammar. The genuine increment is the removal of Paper 22's common unit sector by four staggered pure branches, together with the resulting visible quartic polynomial and infinite irreducible residue-class family.

## Bounded public literature search

### Exact query log

Six bounded batches, 24 exact searches, were executed:

**Batch 1 — core terminology**

1. `site:arxiv.org polynomial symplectic automorphism dynamical degree Hamiltonian shear degree growth`
2. `site:arxiv.org "Hamiltonian shear" polynomial automorphism degree`
3. `site:arxiv.org symplectic polynomial automorphisms Perron dynamical degree`
4. `site:arxiv.org quartic Perron dynamical degree polynomial automorphism`

**Batch 2 — synonym reformulation**

5. `"polynomial symplectic maps" "degree growth"`
6. `"symplectic polynomial automorphism" "dynamical degree"`
7. `"gradient shear" polynomial automorphism symplectic`
8. `"Hamiltonian shears" polynomial maps symplectic`

**Batch 3 — nearest dynamical-degree authors/results**

9. `site:arxiv.org Blanc van Santen affine automorphism dynamical degrees polynomial automorphisms`
10. `site:arxiv.org Shao Sun polynomial automorphisms dynamical degree algebraic number degree`
11. `site:arxiv.org "dynamical degrees of affine automorphisms" polynomial`
12. `site:arxiv.org "weak Perron" "polynomial automorphism"`

**Batch 4 — exact construction vocabulary**

13. `"product potential" "Hamiltonian shear" dynamical degree`
14. `"monomial potential" symplectic shear degree growth`
15. `"q_1^2 q_2^2" Hamiltonian map`
16. `"Perron" "symplectic polynomial automorphism"`

**Batch 5 — foundational shear neighbors**

17. `Berger Turaev Generators of groups of Hamiltonian maps DOI`
18. `Forstneric theorem complex symplectic geometry symplectic shears DOI`
19. `Rangarajan polynomial symplectic maps factorization arxiv`
20. `"On Hamiltonian flows whose orbits are straight lines"`

**Batch 6 — recent cutoff audit**

21. `site:arxiv.org 2025 2026 polynomial automorphism dynamical degree Perron`
22. `site:arxiv.org 2025 2026 symplectic automorphism degree growth polynomial`
23. `site:arxiv.org 2025 "degree growth" "symplectic" automorphism`
24. `site:arxiv.org 2026 Hamiltonian shear dynamical degree`

The search stopped after the exact-construction batch, the foundational-neighbor batch, and the 2025–2026 cutoff batch produced no direct match to the frozen four-spike family. Continuing into a general systematic review was outside the bounded candidate-review scope.

### Sources, identifiers, access level, and collision result

| Source | Identifier / URL | Access level actually used | Relevance and collision finding |
|---|---|---|---|
| Blanc–van Santen, *Dynamical degrees of affine-triangular automorphisms of affine spaces* | arXiv:1912.01324; https://arxiv.org/abs/1912.01324; DOI 10.48550/arXiv.1912.01324 | Abstract and authoritative metadata | Proves every weak Perron number occurs for some affine-triangular automorphism. This blocks novelty claims about general Perron realization, but the abstract does not state this Hamiltonian four-spike family or its (BA) recurrence. |
| Shao–Sun, *Dynamical degrees of affine-triangular automorphisms in dimension four* | arXiv:2509.14584; https://arxiv.org/abs/2509.14584; DOI 10.48550/arXiv.2509.14584 | Abstract and authoritative metadata | Gives algebraic-degree-at-most-four results for a different affine-triangular class. Abstract-level evidence cannot establish absence from its full details, so this remains a medium-confidence near neighbor, not a direct collision. |
| Favre–Firsova–Palmisano–Raissy–Vigny et al., *Hénon maps: a list of open problems* | https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html | Full HTML; relevant Problem 8 / Question 38 and bibliography inspected | Authoritative context for weak Perron questions and higher-dimensional polynomial automorphism degree growth; no candidate-specific theorem. |
| Berger–Turaev, *Generators of groups of Hamiltonian maps* | arXiv:2210.14710; https://arxiv.org/abs/2210.14710; DOI 10.1007/s11856-024-2709-7 | arXiv abstract plus institutional/publisher metadata | Establishes approximation/generation by position and momentum shears, not exact iterated algebraic-degree recurrences. |
| Forstnerič, *A theorem in complex symplectic geometry* | DOI 10.1007/BF02921802; https://users.fmf.uni-lj.si/forstneric/papers/1995J.Geom.Anal.pdf | Author-hosted full text available; relevant symplectic-shear passages inspected | Foundational shear-generation background; no degree-growth collision. |
| Koch–Lomelí, *On Hamiltonian flows whose orbits are straight lines* | arXiv:1304.3377; https://arxiv.org/abs/1304.3377; DOI 10.3934/DCDS.2014.34.2091 | Full text available; abstract and relevant shear/factorization passages inspected | Distinguishes cubic and quartic affine-integrable Hamiltonian structure; does not address this alternating product's exact dynamical degree. |
| Rangarajan, *Polynomial map symplectic algorithm* | arXiv:physics/0212098; https://arxiv.org/abs/physics/0212098 | Abstract and author bibliographic metadata | Polynomial symplectic-map factorization for numerical integration; no exact candidate recurrence. |
| Déserti, *Degree growth of polynomial automorphisms and birational maps: some examples* | arXiv:1602.04642; https://arxiv.org/abs/1602.04642; Eur. J. Math. 4 (2018), 200–211 | Abstract and journal metadata | Produces polynomial-growth examples, orthogonal to this exponential Perron family. |
| Dang–Favre, *Spectral interpretations of dynamical degrees and applications* | Ann. of Math. 194 (2021), 299–359 | Bibliographic pointer in the inspected authoritative survey only | Used only as general context; no noncollision conclusion is inferred from an uninspected full text. |

### Search omission boundary

This audit did not exhaust MathSciNet, zbMATH, subscription-only full texts, nonindexed manuscripts, private drafts, every language, every citation graph, or works not publicly discoverable by the cutoff. Some closest recent papers were assessed only at abstract/metadata level. Accordingly:

- do not claim “first,” “only,” “unprecedented,” or absolute priority;
- use “within the bounded search, no direct collision was located”;
- cite the general weak-Perron realization and affine-triangular degree-four neighbors explicitly;
- rerun a focused current search immediately before any public submission.

No login, upload, author contact, repository publication, or other external-effect action was performed.

## Standalone 26-content-page plan

The result can fit the required 22–30 content pages without depending on Paper 22 for definitions or proofs. A credible target is 26 content pages, excluding references:

| Material | Target pages |
|---|---:|
| Introduction, precise contribution, bounded related-work positioning | 3 |
| Symplectic shears, field, degree conventions, full theorem statement | 3 |
| Weighted-degree calculus and four selector walls | 4 |
| Invariant cone, old-coordinate suppression, no-cancellation, exact (BA) recurrence | 7 |
| (q_4) visibility, characteristic polynomial, Perron conclusion | 4 |
| Modulo-5 irreducibility, infinitude, and (g=9) boundary | 3 |
| Anti-claims, limitations, and comparison with cubic collapse | 2 |
| **Total** | **26** |

The Paper 22 contrast may motivate the paper, but every definition, selector inequality, cone wall, degree induction, characteristic-polynomial calculation, and Perron argument must appear locally. Cross-reference to Paper 22 cannot replace a proof.

## Mandatory anti-claims

The future manuscript must state or unmistakably respect all of the following:

1. It does not classify degree growth for all four-mode Hamiltonian shears.
2. It does not classify all branch regimes for these potentials when (g<10).
3. It does not assert that (g\ge10) is globally necessary for any quartic behavior; it is the threshold for the displayed four-selector mechanism.
4. It does not assert irreducibility for every (g); the certified infinite family is (g\equiv3\pmod5), (g\ge10).
5. It does not claim that all roots of the quartic are positive. “Quartic Perron” refers to the positive Perron root having algebraic degree four.
6. It does not claim a general realization theorem for quartic or weak Perron numbers.
7. It does not claim minimal dimension, minimal degree, optimal sparsity, or absolute priority.
8. It does not claim the selector-to-matrix method, Cayley–Hamilton recurrence, Perron–Frobenius theorem, reduction-modulo-(5) test, support rank, or common-kernel explanation as new.
9. It does not extend the theorem to positive characteristic without a separate proof; characteristic zero prevents derivative coefficients such as (2,g,g-1) from vanishing.
10. It does not use CAS output, floating-point spectra, or finitely many iterates as a proof certificate.

## Proof obligations and STOP conditions

The 9.1 proof-plausibility score reflects that the four branch matrices, threshold, characteristic polynomial, and modular irreducibility all survive independent hand recomputation. It is not permission to omit the difficult degree-induction layer.

Writing or release must STOP rather than weaken the theorem if any of these obligations fails:

- no explicit polyhedral cone containing the ordinary seed can be shown to satisfy (C_g\mathcal K\subseteq\operatorname{int}\mathcal K) for all (g\ge10);
- any of the four selected gradient branches ceases to be strictly dominant on that cone;
- an inherited old coordinate can tie or exceed the claimed new leading degree;
- two leading monomials can cancel over a characteristic-zero field;
- (q_4) is not the total-degree-visible coordinate at every positive iterate;
- the exact multiplication order yields a matrix other than the displayed (B_gA_g);
- a handwritten coefficient check disagrees with the displayed characteristic polynomial;
- the modulo-(5) irreducibility proof cannot be stated uniformly for every (g\equiv3\pmod5);
- a later focused primary-source search finds the same explicit family and theorem package;
- the paper cannot be made standalone in 22–30 content pages without outsourcing essential arguments to Paper 22.

If a STOP condition occurs, the correct response is to narrow or block the candidate, not to retain the headline using experimental evidence.

## Final R1 assessment

The candidate clears the gate because it supplies a mathematically concrete portfolio delta: four staggered pure-power selectors remove the common unit sector behind Paper 22's cubic spectral collapse, leading to a positive (4\times4) degree matrix with a visible quartic characteristic polynomial and a hand-certifiable infinite irreducible Perron subfamily. Its novelty is meaningful but incremental, hence 7.8 rather than a stronger score. A self-contained 26-page presentation is realistic, and the independently recomputed algebra supports a proof-plausibility score of 9.1, provided the invariant-cone and (q_4)-visibility certificates are written symbolically in full.

This review creates no Paper 23 project, changes no status or idea ledger, and has no external effect.

PAPER23_CANDIDATE_GATE_PASS_R1
