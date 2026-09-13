---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-integral-monodromy-units"
canonical_tex: "henon_dynamics/henon_integral_monodromy_units/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_integral_monodromy_units/paper/paper.pdf"
source_sha256: "779825668cecc78cef4df4478f06f989b4e0f5b92b2a1e85c7c5673a002eeccc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Period Integral Monodromy and Algebraic-Unit Multipliers for the Area-Preserving Hénon Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_integral_monodromy_units>)
- [规范 TeX](<../../../../../henon_dynamics/henon_integral_monodromy_units/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_integral_monodromy_units/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_integral_monodromy_units/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Pressure normalization gives a prime-orbit counting law for a certified Hénon suspension, leaving the arithmetic type of its orbit labels as the next gate. We prove an all-period algebraic theorem for the underlying autonomous map $H_6(q,p)=(1-6q^2-p,q)$. After the canonical scaling $x_i=6q_i$, the period-$n$ fixed algebra is defined by monic cyclic quadratics and is finite free over $\mathbb Z$ of rank $2^n$. Every chronological derivative step lies in $SL_2$ over this integral algebra. Therefore every periodic monodromy trace is an algebraic integer and every multiplier is an algebraic unit. A separate exact implementation verifies the Gröbner and trace ledgers through period 10 and recovers the inherited degree-four fixed-point multiplier polynomial. The theorem supplies genuine all-period arithmetic structure, but it also rules out treating a raw multiplier or its field norm as a rational prime. It does not classify the nonalgebraic pressure power $|\Lambda|^{h_*}$.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
date: 'Preprint, August 2026'
title: |
  All-Period Integral Monodromy and Algebraic-Unit\
  Multipliers for the Area-Preserving Hénon Map
```

## Markdown 正文

# Integral cyclic coordinates

The Hénon recurrence is $$q_{i+1}=1-6q_i^2-q_{i-1}.$$ Set $x_i=6q_i$. Then $$\label{eq:scaled}
x_{i+1}=6-x_i^2-x_{i-1}.$$ For period $n$, indices are read cyclically. The neighbor multiset must be retained at low period, giving $$n=1:\quad x_0^2+2x_0-6=0,$$ and $$n=2:\quad x_0^2+2x_1-6=x_1^2+2x_0-6=0.$$

# Finite-free fixed algebra

Let $$\mathcal A_n=\mathbb Z[x_0,\ldots,x_{n-1}]/(f_0,\ldots,f_{n-1}),
\quad
f_i=x_i^2+x_{i-1}+x_{i+1}-6,$$ with the exceptional neighbor multiplicities above.

[\[thm:free\]]{#thm:free label="thm:free"} For every $n\ge1$, $\mathcal A_n$ is finite free over $\mathbb Z$ of rank $2^n$, with basis $$x_0^{\epsilon_0}\cdots x_{n-1}^{\epsilon_{n-1}},
\qquad \epsilon_i\in\{0,1\}.$$ In particular every coordinate value at every geometric periodic point is an algebraic integer.

Under any degree-compatible monomial order, $f_i$ is monic with leading monomial $x_i^2$. The leading monomials are pairwise coprime, so Buchberger's product criterion makes the displayed equations a monic Gröbner basis over $\mathbb Z$. The standard monomials are exactly the square-free monomials, which proves finite freeness and the rank. Specializing a finite integral $\mathbb Z$-algebra at a geometric point sends each $x_i$ to an algebraic integer.

This strengthens the earlier finite-flat statement over $\mathbb Z[A,A^{-1}]$ at the integer specialization: the scaled $A=6$ fibre needs no denominator localization.

# Chronological monodromy

In either the original $(q_i,q_{i-1})$ coordinates or the linearly scaled coordinates, the derivative step is conjugate to $$\label{eq:J}
J_i=\begin{pmatrix}-2x_i&-1\\1&0\end{pmatrix},
\qquad \det J_i=1.$$ For a period-$n$ point, let $$M_\gamma=J_{n-1}\cdots J_0,
\qquad t_\gamma=\operatorname{tr}M_\gamma.$$ Later times act on the left.

[\[thm:unit\]]{#thm:unit label="thm:unit"} For every geometric periodic point of $H_6$ at every period, $t_\gamma$ is an algebraic integer and both eigenvalues of $M_\gamma$ are algebraic units. Their characteristic polynomial is $$X^2-t_\gamma X+1.$$

Equation [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"} and Theorem [\[thm:free\]](#thm:free){reference-type="ref" reference="thm:free"} show that every entry of $M_\gamma$, hence its trace, is an algebraic integer. An eigenvalue $\lambda$ is integral over the ring of algebraic integers by the displayed monic polynomial, hence integral over $\mathbb Z$. Since $\det M_\gamma=1$, the other eigenvalue is $\lambda^{-1}$ and is also an algebraic integer. Thus $\lambda$ is a unit.

The theorem includes nonreal and multiple geometric points scheme by scheme; reducedness is not needed for the integrality statement. On the certified real hyperbolic survivor, the unstable multiplier is the root of modulus greater than one.

# Exact sentinels

The code builds the Gröbner basis and chronological trace independently for $1\le n\le10$. The first reduced traces are $$-2x_0,
\qquad
4x_0x_1-2,
\qquad
-8x_0x_1x_2+2(x_0+x_1+x_2).$$ All coefficients are integers and all monomials lie in the square-free basis. At period one, $x_0=-1\pm\sqrt7$ and the two trace-conjugate characteristic polynomials multiply to $$X^4-4X^3-22X^2-4X+1,$$ recovering the exact non-lattice witness from the instability-roof project.

# Arithmetic consequences and boundary

If an algebraic unit lies in $\mathbb Q$, it is $\pm1$. Thus no hyperbolic raw multiplier can itself be a rational prime. Its field norm is also $\pm1$. Trace and $\det(I-M)$ are algebraic integers but are not multiplicative under repetition, so they cannot simply replace the Euler label without a new compiler.

The pressure-normalized label $|\Lambda|^{h_*}$ is deliberately outside this corollary. The pressure root is a real dynamical invariant whose algebraic type is unknown; no valid transcendence conclusion is available here.

# Evaluator verdict

The all-period unit theorem is positive arithmetic structure at A1/A3, but it constructs no prime correspondence or determinant. The strict tuple is $$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm PARTIAL},A4_{\rm FORMAL}),$$ with overall `ROUTE_A_EXPLORATORY`. Route B is not testable.

# Conclusion

The Hénon instability multipliers are not arbitrary reals: after the correct integral scaling, they form an all-period family of algebraic units. This both strengthens the arithmetic content of the pressure-normalized road and closes its most naive raw-prime interpretation. The next step is to classify which scalar functions of a unit can preserve exact repetition and still produce rational prime labels.

9 B. Buchberger, An algorithmic criterion for the solvability of algebraic systems of equations, *Aequationes Math.* 4 (1970), 374--383. J. H. Silverman, The arithmetic of dynamical systems, Springer, 2007.
