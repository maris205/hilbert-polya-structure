# HCS-C56 primary-source audit

Status: **DOCS_FINAL_NO_MORE_EDITS; primary locators, exact instance boundary,
and official paper citations verified for the project RELEASE_FROZEN.**

Search/access date: **2026-08-15 UTC**.

This audit separates three kinds of support:

1. classical geometry valid for every smooth cubic surface;
2. group-theoretic criteria valid for subgroups of \(W(E_6)\);
3. instance-specific exact claims that no external paper proves and that the
   current C56 producer/checker certify.

No temporary-file digest is evidence in this report.  Original PDFs were read
for locator verification, but a licensed repository source pack has not yet
been promoted.

## 1. Source matrix

| Key | Source and primary access | Exact locator | What C56 uses | What it does not supply |
|---|---|---|---|---|
| EJ09 | A.-S. Elsenhans and J. Jahnel, “Experiments with General Cubic Surfaces,” in *Algebra, Arithmetic, and Geometry*, Progress in Mathematics 269, Birkhäuser, print/copyright volume year 2009, pp. 637–653 (ebook 2010), DOI [10.1007/978-0-8176-4745-2_14](https://doi.org/10.1007/978-0-8176-4745-2_14); [author PDF](https://math.nyu.edu/~tschinke/.manin/final/elsenhans/elsenhans.pdf) | Fact 3; Remarks 4–5; Lemma 8; Algorithm 10; Remarks 11–15.  In the author PDF these occur on PDF pp. 3–7. | Common line field is Galois and its group embeds in \(W(E_6)\); \(U\) is the index-two simple subgroup of order 25920; transitive plus an order-five element leaves only \(U\) or \(W(E_6)\); the pattern \((2,5,5,5,10)\) can discharge both the order-five and odd-class gates; the patterns used by Algorithm 10 are single \(W(E_6)\)-conjugacy classes. | It does not prove the present eliminant, its irreducibility, its modular factorizations, or the C56 surface's Galois group. |
| KW21 | J. L. Kass and K. Wickelgren, “An arithmetic count of the lines on a smooth cubic surface,” *Compositio Mathematica* 157 (2021), 677–709, DOI [10.1112/S0010437X20007691](https://doi.org/10.1112/S0010437X20007691); [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C8185732FC5F02F54699DC1E73757FBE/S0010437X20007691a.pdf/an_arithmetic_count_of_the_lines_on_a_smooth_cubic_surface.pdf) | Theorem 2 and its rank specialization; §5, Definition 41; Corollary 53, p. 701; Corollary 54, p. 702. | \(\sigma_F\) is the section of \(\operatorname{Sym}^3(\mathcal S^\vee)\) whose zeros are lines; the arithmetic count has rank 27; for a smooth cubic every zero is simple; a line's residue field is separable. | Corollary 53 alone does not give the total count 27.  It supplies simplicity; total degree comes from Cayley–Salmon or the rank of Theorem 2.  It does not supply connectedness or the instance Galois group. |
| Vir23 | B. Viray, “Rational points on varieties and the Brauer–Manin obstruction,” arXiv:[2303.17796](https://arxiv.org/abs/2303.17796), v1 (2023) | §2.1, p. 10, equation (24) and the immediately following low-degree exact sequence; the notes point to Poonen, *Rational Points on Varieties*, Proposition 6.7.1. | The exact segment \(0\to\operatorname{Pic}(Y)\to\operatorname{Pic}(Y_{\bar{\mathbf Q}})^{G_{\mathbf Q}}\to\operatorname{Br}(\mathbf Q)\).  Since field Brauer groups are torsion, the Picard-map cokernel is torsion and ranks agree. | No integral surjectivity \(\operatorname{Pic}(Y)\twoheadrightarrow\operatorname{Pic}(Y_{\bar{\mathbf Q}})^G\) is inferred.  No Brauer–Manin conclusion is inferred. |
| Das21 | R. Das, “The space of cubic surfaces equipped with a line,” *Mathematische Zeitschrift* 298 (2021), 653–670, DOI [10.1007/s00209-020-02606-5](https://doi.org/10.1007/s00209-020-02606-5), arXiv:[1803.04146](https://arxiv.org/abs/1803.04146) | Introduction and the incidence cover \(\widetilde{\mathcal M}\to\mathcal M\). | Modern context for the 27-sheeted cover that marks a line on a smooth complex cubic surface. | It is not an arithmetic calculation for the fixed C55 cubic and does not identify \(E\) or \(K\). |
| PPT25 | E. Pichon-Pharabod and S. Telen, “Galois Groups of Symmetric Cubic Surfaces,” arXiv:[2509.06785](https://arxiv.org/abs/2509.06785), v1 (2025) | Abstract; §1, especially the discussion preceding and following Theorem 2 and Table 1. | Closest recent neighbor: monodromy/Galois groups of symmetric families can be proper subgroups of \(W(E_6)\), so maximality must be certified. | It treats family monodromy for \(S_5\)-symmetric linear systems using certified numerical methods, not the exact degree-27 number field of the C55 Yukawa surface. |
| McK21 | S. McKean, “Rational lines on smooth cubic surfaces,” arXiv:[2101.08217](https://arxiv.org/abs/2101.08217), v4 | Theorems 1.1–1.2; §1.2; Appendix A. | Context for possible rational-line counts and the role of subgroup actions on the Schläfli graph. | It does not prove that this surface has zero rational lines or full \(W(E_6)\); C56 derives that from its connected line field. |

## 2. Exact Elsenhans–Jahnel reading

The following distinctions are release-critical.

### Fact 3

For a smooth cubic surface over \(\mathbf Q\), the common field of definition
of all 27 lines is Galois and its Galois group is a subgroup of \(W(E_6)\).
This supports the ambient subgroup statement once C56 has actually identified
its splitting field with the common line field.

### Remarks 4–5

Remark 4 identifies the index-two subgroup \(U\), simple of order 25920.
Remark 5 states both that the action of \(W(E_6)\) on the 27 lines is
transitive and that its image lies in \(A_{27}\).  It then defines an element
to be “even” when it belongs to \(U\) and “odd” otherwise.

Therefore:

$$
\text{EJ odd/even parity}\ne\text{ordinary sign in }S_{27}.
\tag{2.1}
$$

Every \(W(E_6)\) element has ordinary 27-line permutation sign \(+1\).  Any
checker using the usual permutation sign to exclude \(U\) is mathematically
wrong.

### Lemma 8

The precise hypothesis is a subgroup \(H\subseteq W(E_6)\) that

1. acts transitively on the 27 lines, and
2. contains an element of order five.

The conclusion is exactly \(H=U\) or \(H=W(E_6)\).  It does not alone prove
the second alternative.  C56 must separately exhibit an element outside
\(U\).

### Algorithm 10 and Remarks 11–13

Algorithm 10 lists

$$
\begin{aligned}
A&=(9,9,9),\\
B&\in\{(1,1,5,5,5,5,5),(2,5,5,5,10)\},\\
C&\in\{(1,4,4,6,12),(2,5,5,5,10),(1,2,8,8,8)\}.
\end{aligned}
\tag{2.2}
$$

Remark 11 explains that \(B\) supplies order five, \(A+B\) supply the
article's irreducibility route, and \(C\) consists of selected odd classes.
Remark 12 explicitly says that the common pattern
\((2,5,5,5,10)\) can replace both \(B\) and \(C\).  Remark 13 warns that
cycle type need not generally determine a unique \(W(E_6)\)-class, but confirms
that every type used in Algorithm 10 does represent a single class.

C56 uses its own four-prime subset-sum argument for irreducibility and uses
\((2,5,5,5,10)\) only for the order-five and outside-\(U\) gates.  The machine
lane is stronger still: it must enumerate all 5184 elements of this cycle type
and verify that all 5184 lie outside \(U\), with zero in \(U\).

## 3. Exact Kass–Wickelgren reading

In §5, Definition 41 sets

$$
\mathcal E=\operatorname{Sym}^3(\mathcal S^\vee)
\tag{3.1}
$$

on \(\operatorname{Gr}(4,2)\) and defines \(\sigma_f\) by restriction of a
cubic form to the tautological plane.  Its zero scheme is the scheme of lines
on the cubic.

Theorem 2 gives the arithmetic line count

$$
\sum_{\text{lines}}\operatorname{Tr}_{L/k}\langle\alpha\rangle
=15\langle1\rangle+12\langle-1\rangle.
\tag{3.2}
$$

Taking ranks gives total degree \(27\).  Independently, the classical
Cayley–Salmon theorem gives 27 geometric lines.

Corollary 53, printed p. 701, states that \(\sigma_f\) for a smooth cubic
surface has only simple zeros; its more general clause applies to any line on a
possibly singular cubic that is disjoint from the singular locus.  For C56 the
surface is smooth, so every line is covered.

Corollary 54, printed p. 702, deduces that the field of definition of a line is
separable because its component in the geometrically reduced zero scheme is
geometrically reduced.

The valid scheme chain is therefore

$$
\begin{gathered}
\text{zero scheme of }\sigma_F
\quad+\quad
\text{27 geometric lines/total rank 27}
\quad+\quad
\text{all zeros simple}\\
\Longrightarrow
F_1(Y)\text{ finite étale of rank }27.
\end{gathered}
\tag{3.3}
$$

Writing “Corollary 53 proves there are 27 lines” would be an incorrect locator
use.

## 4. Hochschild–Serre rank wording

Viray §2.1 gives the low-degree exact sequence

$$
0\longrightarrow\operatorname{Pic}(Y)
\longrightarrow
\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}
\longrightarrow\operatorname{Br}(\mathbf Q)
\longrightarrow\cdots.
\tag{4.1}
$$

Every Brauer class of a field is torsion.  Hence the quotient

$$
\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}
/\operatorname{Pic}(Y)
\tag{4.2}
$$

is torsion.  Since the geometric Picard group of a smooth cubic surface is a
finitely generated free lattice, tensoring (4.1) with \(\mathbf Q\) gives

$$
\operatorname{rank}\operatorname{Pic}(Y)
=
\operatorname{rank}
\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}.
\tag{4.3}
$$

This is the exact claim used.  The manuscript must not replace (4.3) by an
unqualified integral equality.  It also must not infer a nontrivial Brauer
class, a Brauer–Manin obstruction, or anything about \(Y(\mathbf Q)\).

## 5. Certified instance claims with no external substitute

The current exact C56 artifacts certify the following claims, for which the
literature supplies no instance-specific substitute:

- the four chart polynomials \(f_i\);
- the full coefficient arrays of \(g,h_a,h_b,h_c\) and nonzero
  \(\lambda_a,\lambda_b,\lambda_c\);
- the four direct zero-remainder identities;
- all complementary-chart unit ideals;
- the four complete modular factorizations and subset-sum intersection;
- the identification of the splitting field with all line coordinates;
- the exact \(W(E_6)\) enumeration, target class count, Coxeter parity, and
  Picard fixed rank.

The cited sources justify the general implication from those data.  They do
not verify the data for \(Y\); that role belongs to the producer/checker pair,
which passes all 10 semantic gates and all 2684 rebound cases at prefreeze.

## 6. Bounded recent-neighbor search

The following exact web/arXiv searches were run on 2026-08-15:

1. “Yukawa cubic” + “27 lines”;
2. “Yukawa surface” + “Galois lines cubic”;
3. “Hénon Yukawa cubic surface 27 lines Galois E6”;
4. “Yukawa cubic surface” + “arithmetic”;
5. arXiv 2024–2026 + “cubic surface 27 lines Galois group W(E6)”.

The search included exact-title/arXiv checks and forward-neighbor screening.
It located no source treating the fixed 20-term C55 Yukawa cubic or computing
its degree-27 line field.  The closest 2024–2026 mathematical neighbor found
was PPT25, which studies monodromy groups of symmetric families and explicitly
finds many proper subgroups of \(W(E_6)\).

This search is bounded by the listed queries, indexed sources, and date.  The
allowed conclusion is:

> The bounded search did not locate a prior computation of the full
> four-prime degree-27 line field and \(W(E_6)\) closure for this exact C55
> surface.

It is not a proof that no such computation exists, and the paper must not use
“first,” “unique,” or an exhaustive global novelty claim without a broader
updated search.

## 7. Source-quality assessment

| Source | Original/full text checked | Peer-reviewed status | Fitness for C56 claim | Decision |
|---|---:|---:|---|---|
| EJ09 | yes | published book chapter | exact subgroup and cycle-class criterion | primary |
| KW21 | yes | peer-reviewed journal | exact line-section/simple-zero/separability statements | primary |
| Vir23 | yes | arXiv lecture notes, with textbook backpointer | exact low-degree sequence and safe rank wording | supporting authoritative exposition |
| Das21 | yes | peer-reviewed journal | modern incidence-cover context | context only |
| PPT25 | yes | preprint | current symmetric-family neighbor/caution | bounded-search neighbor only |
| McK21 | yes | preprint | rational-line-count and subgroup context | context only |

No source was rejected as fabricated or unverifiable.  The time distribution
is necessarily concentrated in foundational/classical sources because the
mathematical criteria are stable; the bounded current search was run
separately to avoid confusing foundational authority with novelty coverage.

## 8. Applied citation gates

The drafted paper source applies the following locks:

1. bibliography metadata must be copied from the primary DOI/arXiv records;
2. the paper must cite KW21 Corollary 53 specifically for simplicity and
   Cayley–Salmon or KW21 Theorem 2 for total degree 27;
3. the paper cites EJ09 Lemma 8 and Remarks 11–13 together for the
   \(U/W(E_6)\) branch and odd-class exclusion;
4. every use of “odd” must say “Coxeter-even kernel \(U\)” or equivalent;
5. the Picard sentence must say “same rank” or “isomorphic after tensoring
   with \(\mathbf Q\),” never unqualified integral equality;
6. the current-neighbor sentence must retain “bounded search did not locate.”
