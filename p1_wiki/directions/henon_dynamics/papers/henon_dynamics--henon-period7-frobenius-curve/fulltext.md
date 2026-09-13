---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-period7-frobenius-curve"
canonical_tex: "henon_dynamics/henon_period7_frobenius_curve/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_period7_frobenius_curve/paper/main.pdf"
source_sha256: "724df550669688845db62ebc5edfc9903cfeb818f88e744dfdc7b64489fe97cb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A corrected period-seven Hénon coordinate equation: genus three and an oriented time lift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_period7_frobenius_curve>)
- [规范 TeX](<../../../../../henon_dynamics/henon_period7_frobenius_curve/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_period7_frobenius_curve/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_period7_frobenius_curve/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_period7_frobenius_curve/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We diagnose an apparent constant-term print error in a published period-seven coordinate polynomial for the area-preserving Hénon map. At $(a,\sigma)=(6,26)$ over $\mathbb F_{103}$, the literal equation misses two reversed period-seven cycles, while an adopted placement of the constant has exactly their seven coordinates. We then certify the adopted polynomial generically, without assuming its source provenance. Over $\mathbb Q(\sigma)$, an exact subresultant produces two neighbors for every coordinate root, and their sum is $a-x^2$. The resulting simple two-regular graph on seven roots is forced by geometric transitivity to be one seven-cycle. Its ordered edges form a degree-14 cover carrying an algebraic Hénon time automorphism of exact order seven and its reversor. The degree-seven marked-coordinate quotient has discriminant $(4\sigma-9)^2Q_6(\sigma)^3$; ramification and plane-septic defect calculations both prove that its normalization has genus three. Exact affine counts at $p=5,11,13$, with the displayed branch correction, yield reciprocal degree-six candidate Frobenius numerators and are reproduced by an independent implementation. A simultaneous-normalization theorem at these primes is not claimed. The oriented lift repairs the chronology loss, but the Hénon period remains fixed at seven and no cross-period determinant, Riemann divisor, or Hilbert--Pólya operator is obtained.
author:
- Anonymous research note
bibliography:
- references.bib
date: 8 August 2026
title: |
  A corrected period-seven Hénon coordinate equation:\
  genus three and an oriented time lift
```

## Markdown 正文

# Introduction

A parameter-varying periodic-point scheme can carry weight-one Frobenius cohomology even when every fixed-parameter periodic fibre is a finite permutation. Two questions then have to be separated. Does an exact-period component have positive genus? And does the same algebraic construction keep the phase and orientation required for chronological Hénon time?

We answer both questions for a period-seven carrier, while keeping the much larger Hilbert--Pólya claim out of scope. The starting recurrence is the area-preserving family emphasized in the foundational Hénon--Riemann model of Wang [@wang2026henon], $$\label{eq:paper5}
 q_{j+1}=1-aq_j^2-q_{j-1}.$$ Away from $a=0$, the change $x_j=aq_j$ gives $$\label{eq:hamiltonian}
 x_{j+1}=a-x_j^2-x_{j-1},$$ the Hamiltonian Hénon convention used by Endler and Gallas [@endler2006chiral]. Their period-seven chiral factor and coordinate carrier provide a concrete source-locked test.

The source lock produces the first finding. The last term printed in their Eq. (16) fails an exact period-seven orbit test. An alternative placement of the constant $3$ passes that test. We call the discrepancy an apparent print error, not a publisher-issued erratum. Crucially, we do not promote one finite-field fibre to a generic conclusion: an independent quotient-field subresultant reconstructs the full generic Hénon neighbor graph.

The contributions are five precise statements.

1.  Two reversed Hénon cycles over $\mathbb F_{103}$ refute the literal printed constant and select the adopted formula.

2.  An exact degree-two neighbor correspondence proves that the seven generic roots form one Hénon seven-cycle. Its ordered edges give a degree-14 cover with a genuine order-seven time action and reversal.

3.  The degree-seven marked-coordinate quotient is geometrically integral, and its smooth projective normalization has genus three.

4.  Exact affine counts and a branch-correction protocol at $p=5,11,13$ produce three reciprocal degree-six candidate numerators, verified with independent finite-field arithmetic. Good reduction remains an explicit theorem obligation.

5.  Route A improves at the primitive-orbit layer but still stops: period seven is fixed, no cross-period determinant or target divisor is defined, and no operator domain is constructed.

The result therefore supplies a genuine Hénon dynamical structure rather than a fitted spectral analogy. Its next natural object is the equivariant arithmetic of the ordered-edge cover, especially joint traces of Frobenius and Hénon time.

# Source audit and the adopted curve

Endler and Gallas classify period-seven chiral doublets through $$\label{eq:c7}
 C_7(\sigma)=\sigma^2-2\sigma-a.$$ Their printed coordinate carrier is monic of degree seven in $x$. All terms except the final constant block are frozen exactly as printed. The literal last block is $$\label{eq:literal}
 -2a^3+6a^2+2a+3(a^3-4a^2+a-2)\sigma,$$ whereas the block selected at the specialization of Proposition [\[prop:correction\]](#prop:correction){reference-type="ref" reference="prop:correction"} and generically certified in Section [3](#sec:neighbor){reference-type="ref" reference="sec:neighbor"} is $$\label{eq:corrected}
 -2a^3+6a^2+2a+3+(a^3-4a^2+a-2)\sigma.$$

[\[prop:correction\]]{#prop:correction label="prop:correction"} Over $\mathbb F_{103}$, let $a=6$ and $\sigma=26$. The adopted carrier has root set $$\{10,17,31,54,58,67,98\}.$$ These values support two period-seven state cycles exchanged by the reversor $R(x,y)=(y,x)$. The literal printed carrier has root set $\{55,60\}$ and therefore does not encode these cycles.

Apply $H_6(x,y)=(6-x^2-y,x)$ modulo 103 to $$\begin{aligned}
 &(10,54),(58,10),(31,58),(17,31),(98,17),(67,98),(54,67),\\
 &(10,58),(54,10),(67,54),(98,67),(17,98),(31,17),(58,31).\end{aligned}$$ Each row closes after seven steps; swapping the two entries maps one row to a cyclic rotation of the other. Both coordinate sums are 26, and $26^2-2\cdot26=6$ in $\mathbb F_{103}$. Direct Horner evaluation gives the two root sets stated above.

The literal carrier has $x$-discriminant of degree 42 after substituting Eq. [\[eq:c7\]](#eq:c7){reference-type="eqref" reference="eq:c7"}; in particular it does not have the factorization proved in Section [4](#sec:genus){reference-type="ref" reference="sec:genus"}. Proposition [\[prop:correction\]](#prop:correction){reference-type="ref" reference="prop:correction"} is sufficient to reject the literal equation for the stated orbit. The remainder of the paper is a theorem about the explicitly frozen adopted polynomial, not about the literal typeset equation. The generic Hénon carrier property is proved constructively in Section [3](#sec:neighbor){reference-type="ref" reference="sec:neighbor"}; equality with every component of the full saturated exact-period-seven scheme is not asserted.

Put $a=\sigma^2-2\sigma$ in the adopted carrier and write the resulting polynomial as $P(\sigma,x)$; its full expression appears in Appendix [8.1](#app:poly){reference-type="ref" reference="app:poly"}. Let $\mathcal C$ be the smooth projective normalization of the affine plane curve $P=0$. The base $C_7=0$ is itself the rational $\sigma$-line. The genus calculation concerns the seven-sheeted coordinate cover $\mathcal C\to\mathbb P^1_\sigma$, not the chiral parameter line.

At $a=0$, equivalently $\sigma=0$ or 2, the conjugacy between Eqs. [\[eq:paper5\]](#eq:paper5){reference-type="eqref" reference="eq:paper5"} and [\[eq:hamiltonian\]](#eq:hamiltonian){reference-type="eqref" reference="eq:hamiltonian"} degenerates. The points of $\mathcal C$ above those parameters belong to the algebraic closure of the Hamiltonian model; we do not assign them a direct Paper-5 phase-space interpretation.

# The generic neighbor correspondence {#sec:neighbor}

The one-fibre correction test can be upgraded to a generic dynamical theorem. Put $K=\mathbb Q(\sigma)$, let $A=K[x]/(P)$, and denote the class of $x$ in $A$ by $\bar x$. In $A[y]$ consider $$P(\sigma,y),\qquad P(\sigma,a-y^2-\bar x).$$

[\[thm:neighbor\]]{#thm:neighbor label="thm:neighbor"} Their gcd over $A$ has degree two. If its last nonzero subresultant is $$D_{\bar x}(y)=c_2y^2+c_1y+c_0,$$ then $c_2\ne0$ and $$\label{eq:neighborsum}
 c_1=c_2(\bar x^2-a).$$ The induced relation on the seven geometric roots of $P$ is one simple seven-cycle. Either orientation satisfies the Hénon recurrence and has least period seven.

The exact $y$-subresultant degrees before quotient reduction are $$14,7,6,5,4,3,2,1,0.$$ After every coefficient is reduced modulo $P(\sigma,x)$, the members of degrees one and zero vanish and the degree-two member remains nonzero. This proves the gcd statement. Exact quotient reduction also proves Eq. [\[eq:neighborsum\]](#eq:neighborsum){reference-type="eqref" reference="eq:neighborsum"}. The canonical remainders of $$c_1^2-4c_2c_0
 \quad\hbox{and}\quad
 c_2\bar x^2+c_1\bar x+c_0$$ are nonzero of degree six. Thus the quadratic has two distinct roots and does not contain $\bar x$ itself.

Let $V$ be the seven roots of $P$ over $\overline K$ and declare $x\sim y$ when $$P(\sigma,a-y^2-x)=0.$$ The gcd calculation gives two distinct nonloop neighbors at every vertex. If $y$ is one neighbor of $x$, Eq. [\[eq:neighborsum\]](#eq:neighborsum){reference-type="eqref" reference="eq:neighborsum"} says that the other is $z=a-x^2-y$. Hence $P(z)=0$, so $P(a-x^2-y)=0$ and therefore $y\sim x$. The relation is a simple undirected two-regular graph.

It is defined over $K$, so geometric monodromy permutes its connected components. By geometric integrality, monodromy is transitive on $V$; components are therefore blocks of equal size. Since seven is prime and a simple two-regular component cannot be a singleton, the graph is connected, hence a seven-cycle. Its two orientations obey $x_{i+1}=a-x_i^2-x_{i-1}$. They visit all seven distinct roots, so their least period is seven, and their orbit sum is $\sigma$ by the coefficient $-\sigma x^6$ of $P$.

[\[cor:edgecover\]]{#cor:edgecover label="cor:edgecover"} Over a nonempty open subset of the $\sigma$-line there is a finite ètale ordered-edge cover $\widetilde C\to\mathbb P^1_\sigma$ of degree 14. With states written as $(x_i,x_{i-1})$, the map $$\label{eq:tau}
 \tau(x,y)=(a-x^2-y,x)$$ is an algebraic automorphism of exact order seven. If $R(x,y)=(y,x)$, then $$R^2=1,\qquad R\tau R=\tau^{-1}.$$

Take the ordered edges of the graph in Theorem [\[thm:neighbor\]](#thm:neighbor){reference-type="ref" reference="thm:neighbor"}. The other neighbor of $x$ is $a-x^2-y$, so Eq. [\[eq:tau\]](#eq:tau){reference-type="eqref" reference="eq:tau"} preserves this set and has inverse $(x,y)\mapsto(y,a-y^2-x)$. The 14 ordered edges split into the two directions around the seven-cycle, each one orbit of length seven. The dihedral identities follow by substitution. Clearing the finitely many denominators and excluding the discriminants gives the asserted ètale open locus.

No global choice of orientation was used: $\tau$ acts on the entire ordered edge cover. The projection $(x,y)\mapsto x$ is generically two-to-one. Its deck involution is $$J=R\tau:(x,y)\longmapsto(x,a-x^2-y),$$ so the genus-three marked-coordinate curve is generically $C=\widetilde C/\langle J\rangle$. Hénon time lives upstairs; it does not act on $C$ after the neighbor choice is forgotten.

As an off-source control, the regular split fibre $(p,\sigma,a)=(43,7,35)$ has cycle $$8\longrightarrow16\longrightarrow29\longrightarrow38
\longrightarrow24\longrightarrow23\longrightarrow41\longrightarrow8.$$ The producer and a non-importing checker certify the quotient-field subresultants and this finite-field graph independently.

# Branch analysis and genus {#sec:genus}

Define $$\label{eq:q6}
\begin{split}
Q_6(\sigma)={}&64\sigma^6-448\sigma^5+848\sigma^4+80\sigma^3\\
&-1048\sigma^2+152\sigma-151.
\end{split}$$

[\[thm:genus\]]{#thm:genus label="thm:genus"} The adopted curve $P(\sigma,x)=0$ is geometrically integral. Its smooth projective normalization $\mathcal C$ has genus three. The map $\mathcal C\to\mathbb P^1_\sigma$ has total ramification 18.

Specializing $\sigma=-3$ and reducing modulo 2 gives $x^7+x^6+x^5+x^4+1$, irreducible over $\mathbb F_2$. Since $P$ is monic in $x$, the generic cover is irreducible over $\mathbb Q(\sigma)$. The nontrivial inertia below lies in geometric monodromy. In prime degree seven, the orbits of the normal geometric subgroup are blocks; nontrivial inertia forces one block, so the curve is geometrically integral.

Exact elimination gives $$\label{eq:disc}
 \mathop{\mathrm{Disc}}_xP=(4\sigma-9)^2Q_6(\sigma)^3,
 \qquad \mathop{\mathrm{Disc}}Q_6=2^{63}\cdot97.$$ The polynomial $Q_6$ is irreducible. Over $\mathbb Q[\sigma]/(Q_6)$, the gcd of $P$ and $P_x$ has degree three and has no common root with either $P_{xx}$ or $P_\sigma$. Consequently each of the six $Q_6$-values has three distinct smooth points of ramification index two.

At $\sigma=9/4$, $$P(x,9/4)=\frac{(4x-3)(4x-1)^2(16x^2+7)(16x^2-16x+11)}{16384}.$$ Writing $t=\sigma-9/4$ and $y=x-1/4$, the tangent cone at the unique singular point is $$-\frac18(y^2-10ty+137t^2),$$ with discriminant $-7t^2$. Thus the point is an ordinary node with two nonvertical tangents; both normalization branches are unramified over $t$.

For infinity put $t=1/\sigma$ and $y=x/\sigma$. The integral equation $F(t,y)=t^7P(1/t,y/t)$ has fibre $(y-1)^4(y+1)^3$ at $t=0$. Successive blow-up initial forms listed in Appendix [8.2](#app:infinity){reference-type="ref" reference="app:infinity"} separate four branches above $y=1$ and three above $y=-1$. Each branch uses $t$ as a uniformizer and is unramified. Hence the total ramification is $6\cdot3=18$, and Riemann--Hurwitz yields $$2g-2=7(-2)+18=4.$$ Therefore $g=3$.

The plane closure is a septic of arithmetic genus 15. The finite node has $\delta=1$. The $t$-adic order 22 of $\mathop{\mathrm{Disc}}_yF$, together with zero ramification at infinity, gives total infinity defect 11. Thus $15-1-11=3$, independently checking Theorem [\[thm:genus\]](#thm:genus){reference-type="ref" reference="thm:genus"}.

# Finite-field counts and candidate Frobenius certificates {#sec:frobenius}

For the selected primes $p=5,11,13$, direct modular gcd checks leave only the expected affine node, keep $Q_6$ squarefree and disjoint from that node, and preserve the displayed leading infinity charts. These checks support the expected normalization pattern at the three reductions. They do not construct a smooth proper simultaneous normalization over $\mathbb Z_p$, prove that normalization commutes with reduction, or classify all bad primes.

Let $A_{p,r}$ count affine solutions of $P=0$ over $\mathbb F_{p^r}$. Applying the characteristic-zero branch ledger formally adds seven rational branches at infinity. At the rational plane node, the two tangent directions are rational exactly when $-7$ is a square in $\mathbb F_{p^r}$. We therefore define the explicitly reproducible *branch-corrected count* $$\label{eq:countcorrection}
 \widehat N_{p,r}=A_{p,r}+7+\epsilon_{p,r},\qquad
 \epsilon_{p,r}=\begin{cases}+1,&-7\text{ is a square},\\-1,&\text{otherwise}.
 \end{cases}$$ A simultaneous-normalization proof would promote $\widehat N_{p,r}$ to the point count of the good reduction of $\mathcal C$; absent that proof, the hat is part of the claim boundary.

   $p$   $(A_{p,1},A_{p,2},A_{p,3})$   $(\widehat N_{p,1},\widehat N_{p,2},\widehat N_{p,3})$
  ----- ----------------------------- --------------------------------------------------------
    5           $(3,31,141)$                                $(9,39,147)$
   11          $(11,159,1163)$                            $(19,167,1171)$
   13          $(10,234,2125)$                            $(16,242,2131)$

  : Exact affine and branch-corrected counts.

Set $\widehat S_r=p^r+1-\widehat N_{p,r}$. Newton identities and the genus-three reciprocal completion define the candidate numerator $$\label{eq:localnumerator}
\begin{split}
\widehat L_p(T)={}&1-\widehat S_1T+
\frac{\widehat S_1^2-\widehat S_2}{2}T^2
-\frac{\widehat S_1^3-3\widehat S_1\widehat S_2+2\widehat S_3}{6}T^3\\
&+p\frac{\widehat S_1^2-\widehat S_2}{2}T^4
-p^2\widehat S_1T^5+p^3T^6.
\end{split}$$ The three candidates are $$\begin{aligned}
\widehat L_5(T)&=1+3T+11T^2+31T^3+55T^4+75T^5+125T^6,\\
\widehat L_{11}(T)&=1+7T+47T^2+161T^3+517T^4+847T^5+1331T^6,\\
\widehat L_{13}(T)&=1+2T+38T^2+51T^3+494T^4+338T^5+2197T^6.\end{aligned}$$ Each is irreducible over $\mathbb Q$, satisfies $[T^{6-i}]\widehat L_p=p^{3-i}[T^i]\widehat L_p$, and has reciprocal-root modulus residual below $2.2\cdot10^{-15}$ from $p^{-1/2}$. This circle check is a regression property of the candidates, not a proof of good reduction and not evidence for the Riemann hypothesis.

The producer uses the Python `galois` package. The checker instead constructs $\mathbb F_{p^r}$ as an explicit polynomial quotient, builds its own addition and multiplication tables, and imports no producer code. It repeats all nine frozen affine counts and every branch correction. The recurrence from Eq. [\[eq:localnumerator\]](#eq:localnumerator){reference-type="eqref" reference="eq:localnumerator"} predicts $\widehat N_{5,4}=547$; a sealed direct count gives $A_{5,4}=539$ and Eq. [\[eq:countcorrection\]](#eq:countcorrection){reference-type="eqref" reference="eq:countcorrection"} gives exactly 547.

# Chronology and the Route-A boundary

The neighbor theorem changes the chronology verdict. The scalar curve $C$ does not itself carry $\tau$, because the projection $\widetilde C\to C$ forgets which of the two neighbors is previous. The ordered-edge cover $\widetilde C$, however, retains phase, orientation, reversal, and the exact Hénon time action. Chronological products on this object must use $\tau$; replacing its two directions by an averaged transition matrix would discard genuine information.

The correct future arithmetic observables are therefore equivariant counts of the form $$\#\mathop{\mathrm{Fix}}\!\left(\operatorname{Frob}_p^r\tau^s
       \mid\widetilde C\right),
 \qquad r\ge1,\quad s\in\mathbb Z/7\mathbb Z.$$ Neither the branch-corrected counts of Section [5](#sec:frobenius){reference-type="ref" reference="sec:frobenius"} nor the candidate $\widehat L_p(T)$ determine these joint traces: both belong to the scalar quotient protocol, not to the ordered-edge time sectors.

This distinction gives the following Route-A ruling.

-   **A1\_WEAK.** Primitive period seven, phase, multiplicity, orientation, reversal, and repetition within the generic component are intrinsic and exactly reproducible. But $n=7$ is fixed; there is no cross-period enumeration, stability-multiplier ledger, prime-like clock, or completeness theorem across periods.

-   **A2\_FAIL.** No weighted dynamical zeta or Fredholm determinant has been defined from $(\widetilde C,\tau)$. The candidate Frobenius numerators of $C$ are a different object and cannot fill this gap.

-   **A3\_FAIL.** There is no Riemann divisor, gamma factor, global continuation, functional equation of Riemann type, or Riemann--von Mangoldt law.

-   **A4\_FORMAL\_HINT.** The mother map is area preserving and the ordered-edge cover now carries genuine time reversal, but no quantization, Hilbert space, common clock, or operator domain is defined.

Thus the updated tuple is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),$$ and the overall status is `ROUTE_A_EXPLORATORY`. Route B remains unauthorized.

# Conclusion

The adopted period-seven formula now passes two independent source tests: an exact Hénon fibre rejects the literal printed constant, and a generic subresultant reconstructs the Hénon seven-cycle from the adopted septic itself. The degree-seven marked-coordinate curve has genus three, while its ordered-edge lift has generic degree 14 and carries exact Hénon time and reversal. This is the structural bridge that the scalar quotient alone was missing.

The result remains far from a Hilbert--Pólya construction. The genus and time theorems live on related but distinct objects, selected-prime good reduction is not yet proved, Hénon period is frozen at seven, and no cross-period determinant exists. The next large experiment should determine the geometry of the ordered-edge cover and compute $$\#\mathop{\mathrm{Fix}}(\operatorname{Frob}_p^r\tau^s\mid\widetilde C)$$ without averaging over $s$. This is a genuinely two-clock problem; only after its equivariant sectors and repetition law are understood would a global dynamical zeta test be meaningful.

All symbolic identities, finite-field counts, source witnesses, and independent checks are released with the manuscript. No Riemann zero or prime target table enters any computation.

# Polynomial and reproducibility

## Expanded adopted candidate septic {#app:poly}

After $a=\sigma^2-2\sigma$, the adopted candidate polynomial is $$\begin{aligned}
P={}&x^7-\sigma x^6+(-3\sigma^2+8\sigma)x^5
 +(3\sigma^3-8\sigma^2+4)x^4\\
&+(3\sigma^4-16\sigma^3+20\sigma^2+2\sigma+1)x^3\\
&+(-3\sigma^5+16\sigma^4-20\sigma^3-10\sigma^2+19\sigma-2)x^2\\
&+(-\sigma^6+8\sigma^5-20\sigma^4+14\sigma^3+3\sigma^2+2\sigma+2)x\\
&+\sigma^7-8\sigma^6+20\sigma^5-10\sigma^4-23\sigma^3
 +24\sigma^2-6\sigma+3.\end{aligned}$$

## Infinity charts {#app:infinity}

For $F(t,y)=t^7P(1/t,y/t)$, the first weighted forms are $$\begin{aligned}
y=1+z &: 8z(t+z)^2(2t+z),\\
y=-1+z &:16(z-2t)(z-t)^2,\\
y=1-t+w &: -4t^2w(t^2+2w),\\
y=-1+t+w &: -8t(t^2-2w)(t^2-w).\end{aligned}$$ The remaining $w=0$ branch above $y=1$ has next initial equation $t^4(t^3-4w)$. Together with the branch of valuation two from the first chart, these equations yield four distinct $t$-parameterized branches above $y=1$ and three above $y=-1$.

## Neighbor certificate {#app:neighbor}

The neighbor producer stores the complete subresultant degree/vanishing ledger, SHA-256 hashes of the exact reduced coefficients, the zero neighbor sum remainder, and nonzero discriminant and loop remainders. The checker reconstructs $P$ without importing the producer and repeats the quotient-field calculation. It also verifies the regular split control $(p,\sigma,a)=(43,7,35)$, including all seven recurrence equations and the exact order of $\tau$.

## Commands

From the project directory run

    python code/c19_producer.py --output results
    python code/c19_independent_check.py \
      --certificate results/c19_certificate.json \
      --output results/c19_independent_check.json
    python code/c19_neighbor_correspondence.py \
      --output results/c19_neighbor_correspondence.json
    python code/c19_neighbor_independent_check.py \
      --certificate results/c19_neighbor_correspondence.json \
      --output results/c19_neighbor_independent_check.json
    python -m unittest discover -s code -p 'test_c19.py' -v

The checker does not import the producer or the `galois` package. It uses explicit polynomial quotient fields and stores every modulus in the independent JSON artifact.
