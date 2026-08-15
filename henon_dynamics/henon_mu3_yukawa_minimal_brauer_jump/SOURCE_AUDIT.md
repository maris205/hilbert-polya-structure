# HCS-C57 primary-source audit

Status: **PAPER_COMPILED; PAPER_HOSTILE_PASS; primary locators and theorem
boundaries verified; machine source contract PREFREEZE_CODE_RESULTS_PASS;
release provenance pending; NOT_RELEASED.**

Search/access date: **2026-08-15 UTC**.

This report separates general theorems, general resolver/descent precedents,
instance-specific exact claims, and bounded novelty screening. No temporary
path or digest is a source authority in this project document.

## 1. Primary-source matrix

| key | source | exact locator | C57 use | not supplied |
|---|---|---|---|---|
| SD93 | P. Swinnerton-Dyer, “The Brauer group of cubic surfaces,” *Mathematical Proceedings of the Cambridge Philosophical Society* 113 (1993), 449--460, DOI [10.1017/S0305004100076106](https://doi.org/10.1017/S0305004100076106) | p. 449; §2; Lemma 1, pp. 451--452; Lemma 2, p. 453; concluding classification on p. 458 | over an algebraic number field, the algebraic Brauer quotient is computed by \(H^1(k,\operatorname{Pic}\overline Y)\); even order is controlled by invariant double-sixes; Lemmas 1--2 distinguish one versus three nonzero order-two classes and bound the 2-primary group | no C57 resolver, fixed field, orientation square, quartic, or frozen-instance class |
| EJ10-BM | A.-S. Elsenhans and J. Jahnel, “On the Brauer--Manin obstruction for cubic surfaces,” *Journal of Combinatorics and Number Theory* 2(2) (2010), 107--128, arXiv:[1011.1430](https://arxiv.org/abs/1011.1430) | introduction §1.3; Lemma 2.5; Remark 3.3 and Notation 3.4; Theorems 3.5 and 4.4; §4.3; Definition 4.1; Proposition 5.8; Theorem 5.11; Fact 6.2, Remark 6.3, Corollary 6.4 | \(U_1\) is the double-six stabilizer; \(U_3\) stabilizes a triple of azygetic double-sixes; every \(\mathbf Z/2\) case is contained in \(U_1\), every \((\mathbf Z/2)^2\) case in \(U_3\); restriction is bijective; the oriented quadratic extension and quaternion class represent the double-six class | no exact degree-36 Yukawa field, compact determinant-defined \(Q_D\), or C57 local evaluation |
| EJ10-DS | A.-S. Elsenhans and J. Jahnel, “Cubic surfaces with a Galois invariant double-six,” *Open Mathematics* 8 (2010), 646--661, DOI [10.2478/s11533-010-0036-1](https://doi.org/10.2478/s11533-010-0036-1) | Theorem 6.6; Algorithm 6.7; Propositions 7.1 and 7.4; Example 9.2 | explicit descent, all 45 tritangent planes, sixer-splitting radicand, and a full-\(U_1\), orbit-\([12,15]\) example | it starts from a surface endowed with a double-six and does not invert the frozen full-\(W(E_6)\) line field |
| EJ12 | A.-S. Elsenhans and J. Jahnel, “On the order three Brauer classes for cubic surfaces,” *Open Mathematics* 10 (2012), 903--926, arXiv:[1110.2086](https://arxiv.org/abs/1110.2086), version 2 | Remark 4.34(iii), printed p. 22 | explicitly records computation of a degree-36 resolver whose roots correspond to the double-sixes | no C57 polynomial or class; it prohibits claiming the general resolver construction as new |
| FW19 | B. Farb and J. Wolfson, “Resolvent degree, Hilbert's 13th Problem and geometry,” *L'Enseignement Mathématique* 65 (2019), 303--376, arXiv:[1803.04063](https://arxiv.org/abs/1803.04063) | Theorem 5.6 and Corollary 5.9 | moduli covers and resolvent-degree context for double-sixes and ordered sixers | no fixed number field or frozen-instance Brauer jump |
| Vir23 | B. Viray, “Rational points on varieties and the Brauer--Manin obstruction,” arXiv:[2303.17796](https://arxiv.org/abs/2303.17796), version 1 (2023) | §2.1, p. 10, equation (24) and the following low-degree exact sequence | supporting modern statement of the Hochschild--Serre Picard/Brauer sequence | no instance computation and no automatic Brauer--Manin conclusion |

## 2. Exact reading of the 2-primary classification

### 2.1 Swinnerton-Dyer

SD93 begins with a smooth rational surface over an algebraic number field and
identifies the algebraic Brauer quotient with

\[
H^1(k,\operatorname{Pic}Y_{\overline k}).
\tag{2.1}
\]

For cubic surfaces, Lemma 1 says that this group has even order exactly when
there is a Galois-invariant double-six satisfying the stated nontriviality
condition. The proof canonically associates a double-six to each order-two
cohomology class.

Lemma 2 says that there are at most three nonzero order-two elements and
characterizes the three-element case through three invariant six-line
configurations whose pairwise unions are double-sixes. Thus the possible
nonzero 2-primary groups are

\[
\mathbf Z/2
\quad\text{and}\quad
(\mathbf Z/2)^2.
\tag{2.2}
\]

It is incorrect to collapse both cases into “the Galois image stabilizes one
double-six” when deriving subgroup indices.

### 2.2 Elsenhans--Jahnel

EJ10-BM §1.3 states the containment needed by C57:

- every subgroup giving a Brauer group of order two is contained in the
  maximal double-six stabilizer \(U_1\);
- every subgroup giving a Brauer group of order four is contained in the
  maximal subgroup \(U_3\) stabilizing a triple of azygetic double-sixes.

The group data are

\[
|U_1|=1440,\qquad [W(E_6):U_1]=36,
\tag{2.3}
\]

and, by §4.3,

\[
U_3\cong(S_3\times S_3)\rtimes\mathbf Z/2,\qquad
|U_3|=72,\qquad [W(E_6):U_3]=720.
\tag{2.4}
\]

Proposition 5.8 proves that restriction from \(U_1\), respectively \(U_3\),
is bijective for subgroups with cohomology
\(\mathbf Z/2\), respectively \((\mathbf Z/2)^2\).
Theorem 5.11 gives the complete class-map description by invariant
double-sixes.

For a finite \(L/\mathbf Q\), put

\[
G_L=\operatorname{Gal}(\overline{\mathbf Q}/L),\qquad
H_L=\operatorname{im}\!\left(G_L\longrightarrow W(E_6)\right).
\]

These source results yield

\[
\begin{array}{rcl}
H^1(H_L,\Lambda)[2]\cong\mathbf Z/2
&\Longrightarrow&H_L\subseteq gU_1g^{-1},\\
H^1(H_L,\Lambda)[2]\cong(\mathbf Z/2)^2
&\Longrightarrow&H_L\subseteq gU_3g^{-1}.
\end{array}
\tag{2.5}
\]

Since both indices in (2.3)--(2.4) are divisible by 36,

\[
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\tag{2.6}
\]

The index-720 branch cannot occur at degree 36. Equality therefore selects a
conjugate of \(U_1\).

### 2.3 Machine/source boundary

The live C57 checker reconstructs \(W(E_6)\), the selected \(U_1\), its
36-point coset action, core, normalizer, line orbits, and \(H^1\), together
with other named natural stabilizers as cross-checks. Those finite checks do
**not** prove (2.5) for all possible subgroups \(H_L\). The universal
containment is a source theorem. The machine-prefreeze tuple verifies that
the chosen attaining field realizes its \(U_1\) model.

### 2.4 Number-field bridge

The general base field in C57 is not supplied by silently changing an EJ
formula from \(\mathbf Q\) to \(k\). SD93 is stated for smooth rational
surfaces over an algebraic number field and supplies the Picard-cohomology
description of the algebraic Brauer quotient in that setting. The EJ
\(U_1/U_3\) containment and restriction results used in (2.5) are finite
group statements about subgroups of \(W(E_6)\), the integral Picard lattice,
and invariant line configurations. Consequently they apply to the image
\(H=\operatorname{im}(G_k\to W(E_6))\) for every number field \(k\), with
no step depending on \(k=\mathbf Q\).

For the representative over \(F_D\), C57 does not invoke a literal
\(\mathbf Q\)-model conclusion from EJ. It carries out the quadratic
extension, norm-divisor, and cyclic-algebra construction directly over the
number field \(F_D\), computes its Picard cocycle, and then uses the
number-field Hochschild--Serre bridge supplied by SD93. These standard
characteristic-zero number-field operations are the written bridge promised
by this audit; they are not an instance novelty claim.

## 3. Exact reading of the quaternion precedent

EJ10-BM Remark 3.3 and Notation 3.4 define the quadratic extension that
separates the two sixers of an invariant double-six. Theorem 3.5 computes the
order-two Brauer quotient and constructs its class by a rational function
built from tritangent planes.

Definition 4.1 defines the class map from invariant double-sixes.
Theorem 5.11 proves that every nonzero order-two element arises in this way.
Fact 6.2 identifies the generic algebra as a quaternion; Remark 6.3 describes
its Azumaya gluing; Corollary 6.4 gives a local evaluation rule.

C57 uses only the global class construction. Its determinant-defined quartic
provides a compact representative whose divisor is checked to be the norm of
the oriented double-six divisor. C57 does not use Corollary 6.4 to claim any
local evaluation.

The literal model calculation in EJ10-BM is written over \(\mathbf Q\).
The bridge in Section 2.4 records exactly which parts are group-lattice
statements and which number-field construction C57 repeats directly; it is
not marketed as a new theorem.

## 4. General resolver precedent

EJ12 Remark 4.34(iii) explicitly says that the authors compute a degree-36
resolver whose roots correspond to the double-sixes for a local cohomology
test. FW19 studies the associated moduli covers and their resolvent degree.

Therefore none of the following is valid C57 novelty wording:

- “the first degree-36 double-six resolver”;
- “a new general resolver construction”;
- “double-sixes have not previously been encoded by a degree-36 polynomial”.

The allowed contribution is the exact field and representative package for
the frozen surface, together with the sharp divisibility theorem.

## 5. Instance-specific claims requiring machine evidence

No external source proves any of the following for the HCS-C55 surface:

1. the exact characteristic-zero incidence gcd and quotient;
2. the all-and-only counts \(135,72,36\);
3. the coefficients and irreducibility of \(R_\theta\) and \(R_\delta\);
4. the exact stabilizers of \(\theta_D,\delta_D,\beta_D\);
5. the exact twelve-line carrier \(A_{12}\);
6. the locked \(60\times31\) matrix and nonzero pivot minor;
7. the determinant-defined quartic \(Q_D\);
8. \(\operatorname{div}(Q_D)=\mathcal E+\mathcal G\);
9. the exact quaternion \((\delta_D,Q_D/u_0^4)\).

These claims are promoted into the C57 machine-prefreeze certificate and
recomputed by the independent checker. Phase-1 and `/tmp` temporary files do
not replace or augment that project-local evidence.

## 6. Bounded novelty search

The following query families were screened through 2026-08-15.

### Exact-instance queries

1. “75081586157” and “28576620789” and “cubic surface”
2. “2646295985484” and “1884468968” and “cubic surface”
3. “The Twenty-Seven-Line Field of the Fourth Henon Yukawa Surface”
4. “fourth Hénon Yukawa surface” and “rational points Brauer”
5. “Yukawa cubic” and “27 lines”

### Configuration/Brauer queries

1. “Galois invariant double-six” and “Brauer cubic surface quaternion”
2. “F30/F15” and “cubic surface Brauer”
3. “orbit structure [12,15]” and “cubic surface Brauer”
4. “degree-36 resolvent” and “double-sixes cubic surface”
5. “36 double-sixes” and “resolvent polynomial cubic surface”
6. “cubic surface double six moduli cover stabilizer S6 C2 resolvent degree”
7. exact identifiers 1011.1430, 1110.2086, and DOI
   10.2478/s11533-010-0036-1

The exact-instance queries located no public source for this frozen 20-term
surface's degree-36 configuration field or determinant-defined Brauer class.
This is a search-bounded result only.

Permitted wording:

> The bounded 2026-08-15 screen did not locate a prior exact computation of
> the degree-36 double-six field, its orientation square, and the
> determinant-defined quaternion generator for this frozen Yukawa surface.

Forbidden wording includes “first”, “unique”, “no prior work”, and any
unbounded priority claim.

## 7. Negative source gates

The cited sources do not prove:

- an expanded \(\delta=P(\theta)\) relation;
- the C57 quartic coefficients;
- local evaluation of the C57 class;
- existence or nonexistence of \(F_D\)-rational points;
- a Brauer--Manin obstruction for this surface;
- complete bad-prime inertia, Artin conductors, Euler factors, or root
  numbers;
- stable irrationality as a C57 contribution;
- a motive, automorphy, Calabi--Yau, or dynamics theorem.

The compiled manuscript preserves these source boundaries, and its independent
hostile audit reports no source or claim-boundary blocker.

## 8. Source decisions

| source | decision |
|---|---|
| SD93 | primary theorem source for number-field \(H^1\) and complete 2-primary structure |
| EJ10-BM | primary theorem source for \(U_1/U_3\) containment, restriction, and quaternion class |
| EJ10-DS | primary construction/context source |
| EJ12 | primary prior-art boundary for the general degree-36 resolver |
| FW19 | primary modern resolvent/moduli context |
| Vir23 | supporting authoritative Hochschild--Serre exposition |

The official paper bibliography now contains six cited entries. Its metadata,
locators, citation closure, and source-boundary wording passed the paper audit;
the bibliography is part of the bound 18-file paper-source set.
