---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--98-equal-block-sum-torsion-shifts"
canonical_tex: "symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts/main.pdf"
source_sha256: "ad8eabf1b4b7bf96d67ac68b04a9c2ce558fd248ebca5f4bc65f61cae3a9c948"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Equal-Block-Sum Torsion Shifts: Repeated-Root Fixed Counts and Finite Zeta Functions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/98-equal-block-sum-torsion-shifts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix a prime power $q$ of characteristic $p$ and a window length $r$. We study the two-sided finite-field shift in which every block of length $r$ has the same sum as the adjacent block of length $r$. A global normal form writes each residue-class subsequence as an affine function of time, with one zero-sum constraint on the slopes; in particular the phase space has $q^{2r-1}$ points. The shift is the companion action of $$f_r(z)=\frac{(z^r-1)^2}{z-1}.$$ Writing $r=p^a r_0$ and $n=p^b n_0$ with $p\nmid r_0n_0$, we prove $$\#\operatorname{Fix}(\sigma^n)=q^{D_r(n)},\qquad
   D_r(n)=\min(2p^a-1,p^b)
   +(\gcd(r_0,n_0)-1)\min(2p^a,p^b).$$ This separates a semisimple root-intersection signal from a characteristic- $p$ torsion staircase. We derive the exact order, every least-period orbit, the finite Artin--Mazur zeta, and parameter recovery from the fixed sequence. General algebraic-dynamical and finite-linear-network theory is treated as owned background; the residual statement is the closed package for this specific equal-window relation.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal preprint, 29 August 2026'
title: |
  Equal-Block-Sum Torsion Shifts:\
  Repeated-Root Fixed Counts and Finite Zeta Functions
```

## Markdown 正文

# Introduction and ownership boundary

Linear local constraints over finite alphabets form a basic meeting point of symbolic dynamics, compact algebraic actions, and finite linear sequential networks. Their general structure belongs to established theory; see, for example, Kitchens and Schmidt on compact-group automorphisms [@KitchensSchmidt1989], Schmidt's algebraic-dynamics monograph [@Schmidt1995], and Elspas on finite linear networks [@Elspas1959]. The repeated-root algebra used below is standard finite- field material [@LidlNiederreiter1996].

Our purpose is narrower. We take one transparent symbolic rule---equality of adjacent block sums---and determine its entire temporal dynamics. The first calculation already reveals two independent structures: telescoping turns each residue class into an affine sequence, while the polynomial of the recurrence has root multiplicities that jump with the $p$-parts of both $r$ and the observation time. Combining them yields a fixed-count formula, cycle inventory, and rational zeta for every prime power and every window length.

A bounded search by the exact local relation, annihilating polynomial, and fixed-count formula did not locate the same combined statement. This is not an absolute novelty claim. We explicitly subtract general companion-matrix, algebraic-shift, repeated-root, and finite-zeta ownership. Public release and priority language remain on hold.

# The shift and a global affine normal form

Let $q=p^e$ be a prime power. For $r\geq1$, define $$X_{q,r}=\left\{x\in\mathbb F_q^{\mathbb Z}:
 \sum_{j=0}^{r-1}x_{i+j}=\sum_{j=r}^{2r-1}x_{i+j}
 \text{ for every }i\in\mathbb Z\right\}.$$ The left shift $\sigma(x)_i=x_{i+1}$ preserves $X_{q,r}$.

[\[thm:normal\]]{#thm:normal label="thm:normal"} Every $x\in X_{q,r}$ is uniquely represented by vectors $a=(a_0,\ldots,a_{r-1})$ and $d=(d_0,\ldots,d_{r-1})$ in $\mathbb F_q^r$ satisfying $\sum_jd_j=0$, through $$\boxed{x_{j+kr}=a_j+k d_j
 \quad(0\leq j<r,\ k\in\mathbb Z).}$$ Here the integer $k$ acts through the prime subfield. Consequently $|X_{q,r}|=q^{2r-1}$, and in these coordinates $$\sigma(a,d)=
 (a_1,\ldots,a_{r-1},a_0+d_0;\
  d_1,\ldots,d_{r-1},d_0).$$ In particular, $$\sigma^r(a,d)=(a+d,d),
 \qquad \sigma^{pr}=\mathrm{id}.$$

Put $S_i=\sum_{j=0}^{r-1}x_{i+j}$. The defining relation is $S_i=S_{i+r}$. Since $$S_{i+1}-S_i=x_{i+r}-x_i,$$ the equality at $i$ and $i+1$ implies $$x_{i+2r}-x_{i+r}=x_{i+r}-x_i.$$ Thus $d_i=x_{i+r}-x_i$ is $r$-periodic, and summation along a residue class gives the displayed affine formula with $a_j=x_j$. The original equality at $i=0$ is exactly $\sum_jd_j=0$. Conversely, for an affine-residue sequence, $$S_{i+r}-S_i=\sum_{j=0}^{r-1}(x_{i+r+j}-x_{i+j})
 =\sum_{j=0}^{r-1}d_j=0,$$ so the condition is sufficient. Uniqueness is immediate from $x_j$ and $x_{j+r}-x_j$. The shift-coordinate formula follows by rotating the residue classes; iterating it $r$ times adds $d$ to $a$. Characteristic $p$ then gives $\sigma^{pr}=\mathrm{id}$.

This normal form is the first independent proof engine in the paper. It settles finiteness, dimension, and a uniform period bound without factoring any polynomial.

# Companion module and fixed-point dimensions

The local equation is $$f_r(\sigma)x=0,
 \qquad
 f_r(z)=\frac{(z^r-1)^2}{z-1}
       =(z^r-1)(1+z+\cdots+z^{r-1}).$$ This is a monic polynomial of degree $2r-1$ with nonzero constant term. The first $2r-1$ coordinates determine the next coordinate in both time directions. With column states $(x_i,\ldots,x_{i+2r-2})^{\mathsf T}$, the literal shift matrix is the transpose of the multiplication-by-$z$ Frobenius companion of $f_r$. Consequently $g(\sigma)$ and $g(C_{f_r})$ have the same rank for every polynomial $g$, since their matrices are transposes. This fixes the companion convention used below.

[\[lem:gcd\]]{#lem:gcd label="lem:gcd"} Let $C_f$ be the companion action of a monic polynomial $f\in\mathbb F_q[z]$ with $f(0)\ne0$. Then for every polynomial $g$, $$\dim_{\mathbb F_q}\ker g(C_f)=\deg\gcd(f,g).$$

Identify the companion module with $A=\mathbb F_q[z]/(f)$, on which $C_f$ is multiplication by $z$. Write $h=\gcd(f,g)$, $f=hf_1$, and $g=hg_1$ with $\gcd(f_1,g_1)=1$. The congruence $ga=0\pmod f$ is equivalent to $f_1\mid a$. The multiples of $f_1$ modulo $f$ form a vector space of dimension $\deg h$.

We now isolate the two arithmetic parts of the answer. Write $$r=p^a r_0,\qquad n=p^b n_0,
 \qquad p\nmid r_0n_0,$$ and put $g=\gcd(r_0,n_0)$.

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} For every $n\geq1$, $$\boxed{\#\operatorname{Fix}(\sigma^n\mid X_{q,r})=q^{D_r(n)},}$$ where $$\boxed{D_r(n)=
 \min(2p^a-1,p^b)
 +(g-1)\min(2p^a,p^b).}$$ In particular, $$D_r(n)=\gcd(r_0,n)\quad\text{when }p\nmid n,$$ and $$D_r(p^b)=\min(2p^a-1,p^b).$$

In characteristic $p$, $$z^r-1=(z^{r_0}-1)^{p^a}.$$ Because $p\nmid r_0n_0$, both $z^{r_0}-1$ and $z^{n_0}-1$ are separable over an algebraic closure. The root $1$ therefore has multiplicity $2p^a-1$ in $f_r$, while each of the other $r_0-1$ roots of $z^{r_0}-1$ has multiplicity $2p^a$. Similarly, every root of $z^{n_0}-1$ has multiplicity $p^b$ in $z^n-1$. The common root set is the set of roots of $z^g-1$: it contains $1$ and $g-1$ other roots. Summing the minimum multiplicities gives $$\deg\gcd(f_r,z^n-1)=D_r(n).$$ The fixed space is $\ker(\sigma^n-I)$, so [\[lem:gcd\]](#lem:gcd){reference-type="ref" reference="lem:gcd"} and its vector-space cardinality give the formula. The two specializations set respectively $b=0$ and $g=1$.

The formula applies unchanged to nonprime fields: $q$ controls the size of a fixed vector space, whereas its characteristic $p$ controls the repeated roots.

# Order, cycle census, and zeta

Define $$M_{p,r}=\begin{cases}1,&r=1,\\pr,&r>1.\end{cases}$$

[\[prop:order\]]{#prop:order label="prop:order"} The permutation $\sigma$ of $X_{q,r}$ has order $M_{p,r}$.

The upper bound follows from [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"}. The order is the least $n$ for which every point is fixed, equivalently $D_r(n)=2r-1$. If $r=1$, the system consists of constant sequences. Suppose $r>1$. The formula in [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"} reaches $2r-1$ only if $r_0\mid n_0$ and the $p$-power multiplicity is at least $2p^a$ when $r_0>1$, or at least $2p^a-1$ when $r_0=1$. In either case the least admissible $p$-power is $p^{a+1}$. Indeed, in the second case $r>1$ implies $p^a>1$, so $p^a<2p^a-1\leq p^{a+1}$. The least $n$ is therefore $p^{a+1}r_0=pr$.

Let $P_m$ be the number of points of least period $m$, and let $O_m=P_m/m$ be the number of temporal $m$-cycles.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} For $m\mid M_{p,r}$, $$\boxed{P_m=\sum_{d\mid m}\mu(m/d)q^{D_r(d)},\qquad
 O_m=\frac1m\sum_{d\mid m}\mu(m/d)q^{D_r(d)}.}$$ For $m\nmid M_{p,r}$, one has $P_m=O_m=0$. The Artin--Mazur zeta is the finite rational product $$\boxed{\zeta_{q,r}(z)=
 \prod_{m\mid M_{p,r}}(1-z^m)^{-O_m}.}$$ The identity is understood in the ring of formal power series.

Every orbit length divides the order in [\[prop:order\]](#prop:order){reference-type="ref" reference="prop:order"}. Fixed points of $\sigma^n$ are the disjoint union of points whose least periods divide $n$. Möbius inversion gives $P_m$, and division by $m$ counts cycles. The cycle factorization of the Artin--Mazur zeta [@ArtinMazur1965] gives the final product.

[\[cor:recovery\]]{#cor:recovery label="cor:recovery"} The full fixed-count sequence recovers $(q,r)$. Explicitly, $$q=\#\operatorname{Fix}(\sigma),\qquad
 2r-1=\log_q\left(\max_{n\geq1}\#\operatorname{Fix}(\sigma^n)\right).$$ For $r>1$, the least index at which the maximum is reached is $pr$.

Theorem [\[thm:fixed\]](#thm:fixed){reference-type="ref" reference="thm:fixed"} gives $D_r(1)=1$, while [\[prop:order\]](#prop:order){reference-type="ref" reference="prop:order"} shows that the maximum is the whole phase-space size $q^{2r-1}$ and identifies its first occurrence.

   $(q,r)$   order   fixed counts on divisor times              $\zeta_{q,r}(z)$
  --------- ------- -------------------------------- --------------------------------------
   $(2,1)$    $1$               $F_1=2$                           $(1-z)^{-2}$
   $(2,2)$    $4$       $(F_1,F_2,F_4)=(2,4,8)$       $(1-z)^{-2}(1-z^2)^{-1}(1-z^4)^{-1}$
   $(3,2)$    $6$    $(F_1,F_2,F_3,F_6)=(3,9,3,27)$   $(1-z)^{-3}(1-z^2)^{-3}(1-z^6)^{-3}$

  : Small exact cycle inventories. Exponents are numbers of cycles.

# Independent exact controls and scope

The accompanying standard-library program implements two genuinely different probes. Its polynomial lane computes $\deg\gcd(f_r,z^n-1)$ and the rank of the literal companion matrix independently. Its configuration lane enumerates recurrence states over prime and nonprime fields, reconstructs the affine residue normal form, applies the shift literally, and compares all fixed counts and cycle endpoints. These checks protect sign, characteristic, and endpoint conventions. The frozen run contains exactly $152{,}266$ exact assertions; the preceding proofs carry the infinite family.

The formulas do not classify arbitrary linear subshifts or claim a new general repeated-root theorem. The paper also makes no mixing or positive- entropy claim: every $X_{q,r}$ is finite and has zero topological entropy. The residual contribution is exactly the equal-adjacent-block-sum system and the closed temporal package stated above.
