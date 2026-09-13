# Paper Plan

## Planning status and article profile

**Safe title:** Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps

**Article type:** anonymous, proof-first arithmetic-dynamics journal article.
The plan is for a focused pure-mathematics paper, not a machine-learning
conference submission and not an experimental paper.

**Feasible venue profile:** a Research in Number Theory-style focused article,
with approximately 13.2 pages of front matter, main text, and references,
followed by 3--4 pages of verification appendices. This scale matches the
independently assessed standalone size of 6--6.5: the result is too substantial
for a short note that suppresses the degeneracy proof, but does not need a
long general-theory article.

**Evidence profile:** symbolic proof only. The paper has zero computational,
experimental, numerical, graphical, or data-derived evidence.

## One-sentence contribution

For the monomial Henon automorphism
\[
H(x,y)=(b x^d+a y+c,x)
\]
over any characteristic-zero field, we prove a coefficient-uniform explicit
bound for initial states whose first four transitions remain in the square of
a finite-rank multiplicative subgroup, show by a rank-one number-field family
that three transitions can still admit infinitely many initial states, and
deduce a weighted bound for periodic orbits wholly contained in that subgroup
square.

## Claim hierarchy

The exposition must preserve the following hierarchy from the title page
through the conclusion.

1. **PC1 (dominant primary claim): four-transition finiteness with an explicit
   bound.** This is the principal theorem and receives the largest proof
   allocation.
2. **PC2 (co-primary sharpness claim): rank-one infinitude through three
   transitions.** This is stated on the first page beside PC1, then proved in a
   separate section by a direct family.
3. **COR1 (subordinate consequence): weighted periodic-orbit bound.** This is
   explicitly derived from PC1 under whole-orbit containment; it is not
   advertised as a theorem about periodic points whose single representative
   merely lies in the subgroup square.

No secondary coefficient-stratification claim is promoted. In particular,
the paper does not classify all infinite \(T_2\) or \(T_3\) strata.

## Exact mathematical scope

Let \(K\) be a field of characteristic zero, let \(d\ge 2\), let
\(a,b,c\in K^\ast\), and let \(\Gamma\le K^\ast\) be a multiplicative
subgroup of finite rank \(r\). There is no assumption that \(a\), \(b\),
\(c\), or \(-1\) belongs to \(\Gamma\). Define
\[
H(x,y)=(b x^d+a y+c,x)
\]
and, for every \(m\ge 0\),
\[
T_m(H,\Gamma)
=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2
\text{ for every }0\le j\le m\}.
\]
Thus \(T_m\) records \(m\) transitions and \(m+1\) states. In particular,
the phrase “four-step” means \(0\le j\le4\): four transitions and five
states.

The first main theorem is to be stated exactly as
\[
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\tag{PC1}
\]

The second main theorem is to be stated exactly as follows: for every
\(d\ge2\), there exist a number field \(K\), nonzero coefficients
\(a,b,c\in K\), and a subgroup \(\Gamma\le K^\ast\) of rank one for which
\[
\#T_3(H,\Gamma)=\infty.
\tag{PC2}
\]

For the corollary, let \(C_n^\Gamma(H)\) denote the number of exact-period
\(n\) orbits \(\mathcal O\) satisfying
\(\mathcal O\subseteq\Gamma^2\). Then
\[
\sum_{n\ge1}n\,C_n^\Gamma(H)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\tag{COR1}
\]

## Indexing and terminology contract

Write an initial state as \(P=(x_0,x_{-1})\), so that
\[
H^j(P)=(x_j,x_{j-1})
\quad\text{and}\quad
x_{i+1}=b x_i^d+a x_{i-1}+c.
\]
The four local equations used for \(T_4\) have indices
\(i=0,1,2,3\). For a word in degeneracy labels, the first letter refers to
index \(i\), the second to \(i+1\), and so forth.

At index \(i\), use only the following labels:
\[
\begin{aligned}
A_i&:\ a x_{i-1}+c=0,\\
B_i&:\ b x_i^d+c=0,\\
C_i&:\ b x_i^d+a x_{i-1}=0.
\end{aligned}
\]
With this direction convention, the only free adjacent chains are \(BA\)
and \(CB\), and the only free three-letter extension of \(CB\) is the
exceptional chain \(CBA\). These names must not be reversed or relabeled.

The phrase “finite rank” must not be silently replaced by “finitely
generated.” The word “torus” is shorthand for subgroup-valued coordinates,
not an assertion that \(H\) restricts to a regular self-map of
\(\mathbb G_m^2\).

## Claims-to-evidence matrix

Every public mathematical claim is assigned to a frozen symbolic proof or a
precisely delimited primary source. “None (0)” in the final column is
intentional: no computation or experiment supports any claim.

| ID | Public claim | Frozen proof or source basis | Planned location | Computational or experimental evidence |
|---|---|---|---|---|
| S0 | Exact assumptions, definition of \(T_m\), and \(0\le j\le m\) convention | Research question, proof package, and independent source-design review | Theorem preamble and notation paragraph | None (0) |
| S1 | \(H\) is an automorphism and local-state counts pull back injectively | Explicit inverse-map argument in the proof package | Section 3.1 | None (0) |
| S2 | The fixed-coefficient three-variable unit equation has at most \(E(3,3r)=\exp(18^9(3r+1))\) nondegenerate solutions | Evertse--Schlickewei--Schmidt, Theorem 1.1, as range-locked in the citation record | Section 3.2 | None (0) |
| S3 | The ESS variable group is \(\Gamma^3\) of rank \(3r\), with \(a,b,c\) retained as fixed coefficients | Fixed-coefficient normalization in the proof package and both independent source reviews | Section 3.2 | None (0) |
| S4 | Each ESS solution lifts to at most \(d\) local states | Root-count lemma in the proof package | Section 3.3 | None (0) |
| S5 | All points having a nondegenerate equation at one of four indices contribute at most \(4dE(3,3r)\) | Four-index union bound and injectivity argument in the proof package | Section 3.4 | None (0) |
| S6 | \(A,B,C\) exhaust local degeneracy, including simultaneous degeneracy | Proper-subsums lemma and covering argument in the proof package | Sections 4.1 and 4.6 | None (0) |
| S7 | Only \(BA\) and \(CB\) are free adjacent chains | Nine-transition elimination in the proof package | Section 4.2; expanded algebra in Appendix A | None (0) |
| S8 | Every \(BA\) branch closes at its third letter | \(BAA\), \(BAB\), and \(BAC\) equations in the proof package | Section 4.3 | None (0) |
| S9 | Only \(CBA\) can remain free after three letters, and it closes at the fourth | \(CB\) and \(CBA\) continuation arguments in the proof package | Section 4.4 | None (0) |
| S10 | Every four-letter degeneracy word has at most \(d^2\) initial states, giving \(81d^2\) | Per-word lemma, \(3^4\)-word union bound, and simultaneous-degeneracy audit in the proof package | Sections 4.5--4.7 | None (0) |
| PC1 | Explicit bound for \(\#T_4(H,\Gamma)\) | S1--S10 and the partition lemma in the proof package | Theorem A; completed in Section 4.7 | None (0) |
| PC2 | For each \(d\ge2\), a rank-one example has infinite \(T_3\) | Direct number-field family in the proof package | Theorem B and Section 5 | None (0) |
| COR1 | Weighted bound for whole-orbit periodic cycles | Orbit-disjointness and containment argument in the proof package | Corollary C and Section 6.1 | None (0) |
| RW1 | Bell--Ghioca concerns return times for one fixed orbit and a finitely generated subgroup | Bell--Ghioca, Theorem 1.1, with the regular-map clause stated precisely in the citation record | Section 2.2 | None (0) |
| RW2 | Kim--Krieger--Postolache--Szeto gives degree-dependent abundance for a general-polynomial Henon family | Their Theorems A and B, with degree and congruence ranges fixed in the citation record | Section 2.3 | None (0) |
| RW3 | Mello--Yasufuku is conditional and does not discharge its general main hypothesis through its Vojta-based result | Their Theorems 1.1--1.2, Corollary 1.3, and Theorem 4.2, as precisely delimited in the citation record | Section 2.4 | None (0) |
| N1 | Literature positioning is a bounded comparison, not a priority claim | Citation verification and novelty assessment through 2026-08-16 | End of Section 2 | None (0) |
| L1 | Constants and scope limitations | Proof package, claims matrix, and novelty assessment | Section 6.2 | None (0) |

## Page budget

The page allocations are drafting controls, not content to appear in the
published article.

| Component | Target pages | Purpose |
|---|---:|---|
| Abstract and front matter | 0.35 | State PC1, PC2, method, and COR1 without history or proof detail |
| 1. Introduction and main results | 1.35 | Put both primary claims on page 1 and give a concise proof roadmap |
| 2. Related work and precise boundaries | 1.15 | Synthesize the closest sources without a priority claim |
| 3. Unit equations and the nondegenerate contribution | 1.80 | Give the full fixed-coefficient ESS and \(d\)-state argument |
| 4. The degenerate locus | 6.00 | Carry the complete symbolic closure proof, including simultaneous degeneracy and short orbits |
| 5. Three-step infinitude in rank one | 1.15 | Prove PC2 by direct substitution |
| 6. Periodic corollary and limitations | 0.65 | Prove COR1 and delimit the theorem |
| References | 0.75 | Primary proof source and tightly selected boundary literature |
| **Main article total** | **13.20** | Focused journal-article scale |
| Appendices A--B | 3.0--4.0 | Full transition table and expanded algebraic checks only |

If typesetting pressure arises, related work and exposition are compressed
before any proof step. The ESS normalization, rank calculation, free-chain
closures, simultaneous-degeneracy argument, per-word count, and short-orbit
paragraph remain in the main text.

## Detailed article architecture

### Abstract

Target 140--170 words. Open with the finite-window subgroup-survival problem
for \(H(x,y)=(b x^d+a y+c,x)\). State the exact \(T_4\) bound, then the
rank-one infinite-\(T_3\) theorem, and finally the whole-orbit periodic
corollary in subordinate language. Name the two proof ingredients:
fixed-coefficient ESS counting and a complete symbolic analysis of four
degenerate transitions. Do not use “first,” “optimal” without qualification,
or any empirical language.

### 1. Introduction and main results

#### 1.1 Problem and finite-window viewpoint

Explain that the question counts all initial states whose entire finite
window lies in \(\Gamma^2\), rather than return times along one preselected
orbit. Define \(T_m\) immediately and emphasize that \(T_4\) contains five
states. Explain in one paragraph why a four-transition cutoff is meaningful:
the unit-equation method handles nondegenerate recurrences, while a free
degenerate chain survives through three transitions.

#### 1.2 Theorem A: explicit four-transition bound

State PC1 with all assumptions. Immediately add three clarifications:

- \(\Gamma\) has finite rank and need not be finitely generated;
- \(a,b,c\) are arbitrary nonzero fixed coefficients and need not lie in
  \(\Gamma\);
- the displayed constant is explicit but deliberately coarse.

#### 1.3 Theorem B: three-transition sharpness

State PC2 on the first page or at the top of the second page, visually at the
same theorem level as PC1. Call it “sharpness of the transition threshold,”
not sharpness of either numerical constant. The theorem asserts existence
for every \(d\), not a classification of all coefficients.

#### 1.4 Corollary C and roadmap

State COR1 after the two main theorems. Say explicitly that every point of
each counted orbit lies in \(\Gamma^2\).

End with a seven-part proof roadmap:

1. index the recurrence and record the inverse automorphism;
2. normalize each local recurrence as a fixed-coefficient unit equation;
3. bound all points with at least one nondegenerate local equation;
4. label all degenerate local equations by \(A,B,C\);
5. prove the \(BA\), \(CB\), and exceptional \(CBA\) closure lemmas;
6. cover simultaneous degeneracy and sum the \(81\) word bounds;
7. give the rank-one family and derive the periodic corollary.

### 2. Related work and precise boundaries

This section should be synthetic rather than bibliographic. It must make no
claim of being the first result of its kind. The closing sentence should say
only that the cited theorems address different orbit, map, group, or
conditionality regimes and therefore do not supply PC1 or PC2.

#### 2.1 The imported unit-equation theorem

Cite Evertse--Schlickewei--Schmidt, published Theorem 1.1. Record exactly the
scope used here: a characteristic-zero field, a subgroup of
\((K^\ast)^n\) of finite rank \(R\), arbitrary fixed nonzero coefficients,
and nondegenerate solutions of one linear equation. Display only the
specialization
\[
E(3,3r)=\exp\!\bigl(18^9(3r+1)\bigr).
\]
This is the sole external theorem imported into the proof.

#### 2.2 Fixed-orbit subgroup intersections

State Bell--Ghioca, Theorem 1.1(i), precisely: for one fixed orbit of a
rational self-map of a semiabelian variety and a finitely generated subgroup,
the return-time set is a finite union of arithmetic progressions together
with a Banach-density-zero set. Under the regular-self-map hypothesis,
Theorem 1.1(ii) makes only the residual set finite, not the whole return-time
set. Also state the applicability boundary: the restriction of the present
map to \(\mathbb G_m^2\) is generally rational, not regular, because its first
coordinate can vanish. Their fixed-orbit return-time structure is distinct
from a uniform count of all finite-window initial states.

#### 2.3 Rational periodic-point abundance for Henon maps

State the exact ranges of Kim--Krieger--Postolache--Szeto. Their Theorem A,
for every odd \(d>2\), constructs a rational polynomial \(s_d\) of degree at
most \(d\) such that
\[
h_d(x,y)=(y,-x+s_d(y))
\]
has at least \((d-4)^2\) rational periodic points. Their Theorem B, when
\(d\equiv1\pmod6\), produces an integer cycle of length
\((8d+10)/3\). Explain that this is a general-polynomial,
degree-dependent abundance result, not a monomial-plus-constant
finite-rank-\(T_4\) theorem.

#### 2.4 Conditional higher-dimensional semigroup results

State Mello--Yasufuku with its hypothesis boundary intact. Their Theorems
1.1--1.2 and Corollary 1.3 concern projective semigroups over number fields
and finitely generated subgroups conditional on
\(\mathrm{Hyp}_\epsilon\), with the main results requiring
\(\epsilon\ge(1+c)/2\). Their Theorem 4.2, under additional divisor
hypotheses and Vojta's Main Conjecture, supplies the relevant non-density
only for sufficiently small \(\epsilon\); it does not verify the general
hypothesis needed for those main theorems. It therefore is not an
unconditional Henon fixed-window count over arbitrary characteristic-zero
fields.

#### 2.5 Brief surrounding context

Use a single compact paragraph to place univariate \(S\)-unit orbit bounds,
multiplicative dependence of iterates, integral-point non-density, and
arithmetic Henon height results around the problem. Cite theorem numbers only
where a comparison is made. Do not turn this paragraph into a comprehensive
survey and do not infer novelty from absence in a search.

### 3. Unit equations and the nondegenerate contribution

#### 3.1 Recurrence and invertibility

For \(P=(x_0,x_{-1})\), derive
\[
x_{i+1}=b x_i^d+a x_{i-1}+c
\]
and display
\[
H^{-1}(X,Y)
=
\left(Y,\frac{X-bY^d-c}{a}\right).
\]
Conclude that \(P\mapsto H^i(P)\) is injective for every fixed \(i\).

#### 3.2 Fixed-coefficient ESS normalization

At each local index write
\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}
=1.
\tag{3.1}
\]
The variable triple
\[
(x_{i+1},x_i^d,x_{i-1})
\]
lies in \(\Gamma^3\), whose rank is \(3r\). The quantities
\(1/c,-b/c,-a/c\) are fixed coefficients in \(K^\ast\); they are not
absorbed into the variable group. This sentence is mandatory because it
prevents the false coefficient-membership assumption.

Apply ESS only to nondegenerate solutions of (3.1). State explicitly that
the three-variable bound is \(E(3,3r)\), even if \(\Gamma\) contains torsion
or is not finitely generated.

#### 3.3 At most \(d\) states over an ESS solution

An ESS triple fixes \(x_{i+1}\), \(x_i^d\), and \(x_{i-1}\). The equation for
\(x_i\) has at most \(d\) roots in \(K\), so at most \(d\) local states lie
above the triple. By injectivity of \(H^i\), the same bound applies to initial
states.

#### 3.4 Partition lemma and four-index union

State and prove the partition lemma:

> Every point of \(T_4(H,\Gamma)\) either has a nondegenerate local equation
> at some \(i\in\{0,1,2,3\}\), or all four local equations are degenerate.

The first class has cardinality at most
\[
4dE(3,3r).
\]
The partition is exhaustive but not asserted to be disjoint at the level of
the four nondegenerate-index choices; a union bound suffices.

### 4. The degenerate locus

This is the proof core and receives six main-text pages. The appendices may
expand the eliminations but may not carry a missing logical implication.

#### 4.1 Exhaustive labels

For the three nonzero summands
\[
\frac1c x_{i+1},\qquad
-\frac bc x_i^d,\qquad
-\frac ac x_{i-1},
\]
a degenerate solution has a vanishing proper subsum. A one-term subsum
cannot vanish. A vanishing two-term subsum yields one of, and possibly more
than one of,
\[
\begin{aligned}
A_i&:\ a x_{i-1}+c=0,\\
B_i&:\ b x_i^d+c=0,\\
C_i&:\ b x_i^d+a x_{i-1}=0.
\end{aligned}
\]
Prove this equivalence directly. Set
\(\alpha=-c/a\) and, for one transition, \(u=x_{i-1}\),
\(v=x_i\). Record the resulting next coordinates for all three labels.

#### 4.2 Adjacent-transition lemma

State a nine-case lemma for words in \(\{A,B,C\}^2\). Its main-text proof
substitutes the coordinate formula from the first label into the second and
records enough equations to establish the following complete conclusion:

- \(AA,AB,AC,BB,BC,CA,CC\) each have at most \(d^2\) initial states;
- \(BA\) can be free only when \(b\alpha^d=-c\);
- \(CB\) can be free only when \(bc^{d-1}=-1\).

The main text must state all nine outcomes and show the two compatibility
relations. Appendix A gives the full row-by-row table and expanded
substitutions as an audit aid, not as a replacement for this lemma.

#### 4.3 Closure of every \(BA\) branch

Under \(b\alpha^d=-c\), parameterize the \(BA\) branch by
\(t=x_{i-1}\). Prove in the main text that its three possible third letters
give
\[
\begin{array}{c|c|c}
\text{word}&\text{equation in }t&\text{bound}\\ \hline
BAA&at=\alpha&1\\
BAB&b^{d+1}a^{d^2}t^{d^2}=-c&d^2\\
BAC&b^{d+1}a^{d^2}t^{d^2}=-a^2t&d^2-1.
\end{array}
\]
For \(BAC\), use \(t\ne0\) before dividing by \(t\). Conclude that every
four-letter word beginning with \(BA\) already has at most \(d^2\) states;
the fourth condition cannot increase the count.

#### 4.4 The \(CB\) extension and fourth-letter closure of \(CBA\)

Under \(bc^{d-1}=-1\), parameterize the \(CB\) branch and prove:

- \(CBB\) and \(CBC\) each impose a degree-\(d\) equation;
- \(CBA\) remains free only if \(a=-1\);
- hence the sole free three-letter chain is
  \[
  CBA,\qquad a=-1,\qquad bc^{d-1}=-1.
  \]

For this exceptional chain, carry the fourth transition in the main text.
With parameter \(t\), the three possibilities are
\[
\begin{array}{c|c|c}
\text{word}&\text{equation in }t&\text{bound}\\ \hline
CBAA&-t=c&1\\
CBAB&b^{d+1}(-t)^{d^2}=-c&d^2\\
CBAC&b^{d+1}(-t)^{d^2}=-t&d^2-1.
\end{array}
\]
Again divide only after recording \(t\ne0\). This proves that \(CBA\)
closes at the fourth letter.

#### 4.5 Per-word counting lemma

State and prove:

> For every word \(w\in\{A,B,C\}^4\), the set of initial states realizing
> \(w\) has cardinality at most \(d^2\).

The proof separates three cases: no free adjacent prefix, a \(BA\) prefix,
and a \(CB\) prefix. The adjacent-transition lemma handles the first;
Section 4.3 handles the second; and Section 4.4 handles all extensions in
the third. Explicitly note that initial states and local states are in
bijection at a fixed index because \(H\) is invertible.

#### 4.6 Simultaneous degeneracy

Address overlaps before taking the word union. A local recurrence can satisfy
multiple labels. At each of the four indices, choose any label satisfied by
the point. This assigns every all-degenerate point to at least one word in
\(\{A,B,C\}^4\). Multiple assignments can overcount but cannot omit a
point. Since the per-word bound applies to the full realization set of each
word, overlaps require no correction term.

If the manuscript lists pairwise or triple intersections, treat that list
as a consistency check only; the covering argument is the proof. Characteristic
zero and nonvanishing coordinates prevent a vanishing one-term subsum.

#### 4.7 Completion of PC1 and short periodic orbits

There are \(3^4=81\) words, so the all-degenerate class contributes at most
\[
81d^2.
\]
Combine this with Section 3.4:
\[
\#T_4(H,\Gamma)
\le
4dE(3,3r)+81d^2
=
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
\]

Close the section with the short-orbit check. No proof step assumes the five
states \(P,H(P),\ldots,H^4(P)\) are distinct. Periods \(1,2,3,4\) merely
repeat some indexed equations; repetitions impose compatibility and create
no new choices. Injectivity remains valid. Thus there is no extra
short-period term.

### 5. Three-step infinitude in rank one

Fix \(d\ge2\). Choose \(c\in\overline{\mathbb Q}\) with
\[
c^{d-1}=-1,
\]
and set
\[
K=\mathbb Q(c),\qquad b=1,\qquad a=-1,\qquad
\Gamma=\langle2,c,-1\rangle.
\]
Because \(c\) and \(-1\) are torsion while \(2\) is not,
\(\operatorname{rank}\Gamma=1\).

For \(t=2^n\), \(n\ge0\), take \(P_t=(t,t^d)\). Give the full direct
calculation
\[
\begin{aligned}
H(P_t)&=(c,t),\\
H^2(P_t)&=(-t,c),\\
H^3(P_t)&=((-t)^d,-t).
\end{aligned}
\]
All coordinates belong to \(\Gamma\), and the \(P_t\) are pairwise distinct.
Therefore \(\#T_3(H,\Gamma)=\infty\). Identify the realized degeneracy word
as \(CBA\), linking PC2 to the exceptional chain in Section 4.

End by stating the exact sharpness interpretation: four transitions suffice
uniformly under the theorem's assumptions, while three do not. Do not claim
that \(81d^2\), the ESS constant, or the example itself is numerically
optimal.

### 6. Periodic corollary and limitations

#### 6.1 Whole-orbit periodic consequence

If an exact-period-\(n\) orbit \(\mathcal O\) is wholly contained in
\(\Gamma^2\), every one of its \(n\) points lies in \(T_4(H,\Gamma)\).
Distinct exact-period orbits are disjoint, hence
\[
\sum_{n\ge1}n\,C_n^\Gamma(H)
\le \#T_4(H,\Gamma).
\]
Insert PC1 to obtain COR1. Explicitly contrast this with the larger set of
periodic points having only one chosen representative in \(\Gamma^2\);
the corollary makes no statement about that larger set without
whole-orbit containment.

#### 6.2 Honest limitations

The final discussion records all of the following.

- The ESS exponential and the \(81d^2\) degeneracy term are coarse explicit
  bounds; neither is optimized.
- The paper does not classify the coefficient strata for which \(T_2\) or
  \(T_3\) is finite or infinite.
- The argument is for the monomial-plus-linear-plus-constant family
  \(H(x,y)=(b x^d+a y+c,x)\); it does not establish an analogue for general
  Henon polynomials, compositions of Henon maps, or arbitrary polynomial
  automorphisms.
- The main result controls a finite window. It is not a general orbit
  intersection theorem or a description of return-time sets.
- PC2 proves sharpness of the number of transitions only. It does not improve
  or lower-bound the constant in PC1.

Mention broader polynomial families and coefficient stratifications only as
future questions, with no conjectural theorem inserted into the present
claim set.

## Appendices

The appendices are verification supplements. Every lemma needed to infer PC1,
PC2, and COR1 is stated and proved in the main text.

### Appendix A. Complete adjacent-transition table

Give the full \(3\times3\) table for
\[
AA,AB,AC,BA,BB,BC,CA,CB,CC,
\]
including the constraint on \((u,v)\), the polynomial degree, and the
cardinality bound. Show the coordinate substitution that produces each
entry. Highlight \(BA\) and \(CB\) as the only free entries, using the same
index direction as the main text.

### Appendix B. Expanded closure and overlap algebra

Expand the \(BAA/BAB/BAC\), \(CBB/CBC/CBA\), and
\(CBAA/CBAB/CBAC\) calculations. Check that all divisions are by nonzero
group elements, and record the \(d^2-1\) degree after division. List the
possible simultaneous-label intersections as a cross-check of the covering
argument. End with a compact dependency diagram in prose showing that no
appendix calculation creates an additional assumption.

## Figure and table policy

No empirical figure, numerical plot, dataset table, or computational diagram
is planned. The algebraic transition tables in Section 4 and Appendix A are
part of the written proof, not experimental evidence.

At most one later visual could be considered: a definition-only diagram
showing the recurrence indices and the \(BA\), \(CB\), \(CBA\) branching
pattern. Such a diagram would carry no evidence and would duplicate no proof
step. It is not currently authorized, is not required for submission, and is
excluded from the present plan's deliverables.

## Citation scaffold and language controls

The bibliography should remain compact and primary-source based.

- Import the explicit unit-equation bound only from
  Evertse--Schlickewei--Schmidt, Theorem 1.1.
- Use Bell--Ghioca, Theorem 1.1(i)--(ii), only for the fixed-orbit subgroup
  intersection boundary.
- Use Kim--Krieger--Postolache--Szeto, Theorems A and B, only for the
  general-polynomial rational-periodic abundance boundary.
- Use Mello--Yasufuku, Theorems 1.1--1.2, Corollary 1.3, and Theorem 4.2,
  only with the conditionality and epsilon-range distinction stated in
  Section 2.4.
- Additional arithmetic-dynamics sources may provide context only when their
  exact theorem range is stated and they do not enlarge the paper's claims.

The public prose must avoid:

- any coefficient-membership assumption or enlargement of \(\Gamma\);
- the false statement that coefficient-normalized variables lie in
  \(\Gamma^3\);
- any replacement of finite rank by finite generation;
- any reversal of the \(A,B,C\) index direction;
- any description of Bell--Ghioca's regular clause as making the entire
  return-time set finite;
- any suggestion that Mello--Yasufuku's Vojta-based theorem verifies their
  general main hypothesis;
- a global novelty or priority claim based on the bounded literature search.

## Anonymous-submission and prose controls

- Omit author identities, affiliations, acknowledgments, repository
  references, and self-identifying project history.
- Refer to earlier mathematics neutrally; do not use “our previous work.”
- Introduce every symbol before use and keep \(T_m\), \(C_n^\Gamma(H)\),
  \(E(3,3r)\), and the \(A,B,C\) labels stable.
- State theorem assumptions at the theorem, not only in surrounding prose.
- Lead proof paragraphs with their conclusion and then supply the
  calculation.
- Keep the sharpness construction in a stand-alone section so it cannot be
  mistaken for an assumption in PC1.
- Avoid promotional adjectives. “Explicit,” “uniform in the coefficients,”
  and “sharp in the number of transitions” are justified; “optimal” and
  “complete classification” are not.

## Anticipated referee checks

| Check | Required response in the manuscript |
|---|---|
| Why is the ESS rank \(3r\)? | Prove that the variable group is the direct product \(\Gamma^3\); coefficients stay fixed outside the variables. |
| Do coefficients need to lie in \(\Gamma\)? | No; equation (3.1) uses arbitrary nonzero fixed coefficients. State this in Theorem A and Section 3.2. |
| Why are there at most \(d\) states per ESS solution? | Fix \(x_i^d\), count roots of \(X^d-x_i^d\), and invoke injectivity of \(H^i\). |
| Are the three degeneracy labels exhaustive? | Derive them from all vanishing proper two-term subsums. |
| Can a free chain escape the table? | Give the nine-transition lemma, then close \(BA\), \(CB\), and exceptional \(CBA\) explicitly. |
| What if several labels hold simultaneously? | Use the choose-any-label covering argument; overlaps only overcount. |
| What about periods shorter than four? | Indexed recurrences may repeat; no distinctness was used and no new state is created. |
| Does the periodic corollary count every periodic point in \(\Gamma^2\)? | No; it counts exact-period orbits wholly contained in \(\Gamma^2\). |
| Is PC2 a full \(T_3\) classification? | No; it is an existence family proving transition-threshold sharpness. |
| Is any numerical evidence needed? | No; every claim is supported by symbolic proof or a cited theorem, with zero computational evidence. |

## Internal quality gate for drafting

A manuscript may advance from this plan only if a proof audit confirms all
of the following in the written text:

1. The main theorem uses \(0\le j\le4\) and all three coefficients are
   arbitrary nonzero elements of \(K\).
2. Equation (3.1) is presented as a fixed-coefficient unit equation with
   variables in \(\Gamma^3\) of rank \(3r\).
3. The four nondegenerate indices yield \(4dE(3,3r)\).
4. The main text, not only an appendix, closes \(BA\), \(CB\), and \(CBA\).
5. The per-word lemma and simultaneous-degeneracy cover yield \(81d^2\).
6. Short periods are handled without an added term.
7. The rank-one construction is checked through exactly \(H^3\).
8. The periodic statement retains whole-orbit containment.
9. Bell--Ghioca, Kim--Krieger--Postolache--Szeto, and Mello--Yasufuku retain
   their exact scope boundaries.
10. The article contains no computational or experimental evidence claim.

## Downstream authorization boundary

This document authorizes only a future anonymous prose draft after a separate
planning review. It does not authorize a manuscript source, bibliography
file, figure, build, code, computation, experiment, result, or submission.

**DOWNSTREAM PERMISSIONS REMAIN CLOSED.**
