---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rule90-maximal-subgroup-sieve-route-a"
canonical_tex: "henon_dynamics/henon_rule90_maximal_subgroup_sieve_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rule90_maximal_subgroup_sieve_route_a/paper/main.pdf"
source_sha256: "7dffd8fec704f0f94e1c01ff5a8b7333983bbeb9d9bbb218e72653cc8bbb111a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Maximal-Subgroup Period Sieve for Mersenne Rule 90

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rule90_maximal_subgroup_sieve_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rule90_maximal_subgroup_sieve_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rule90_maximal_subgroup_sieve_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rule90_maximal_subgroup_sieve_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For cyclic Rule 90 at every Mersenne circumference, we replace a union over all proper clock times by an exact inclusion--exclusion over maximal subgroups of the finite time group. Fixed-space intersections are controlled by greatest-common-divisor clocks and polynomial gcds, giving $N_{<L}=\sum_{\varnothing\ne Q}(-1)^{|Q|+1}
  2^{D_L(L/\prod_{p\in Q}p)}$. If the circumference $L>3$ is also prime, zero is the only fixed state and all remaining $2^{L-1}-1$ states in the periodic image have exact period $L$; the short-period probability is exactly $2^{-(L-1)}$. We obtain the corresponding primitive-cycle count and complete finite dynamical zeta for every length meeting that premise. Independent finite-field and symbolic reconstructions verify the source formulas. We do not claim infinitely many such lengths, a target divisor, or an operator realization. Circumference factors are source clock data, not arithmetic local factors.
author:
- 'Route-A structural certificate C160'
title: 'An Exact Maximal-Subgroup Period Sieve for Mersenne Rule 90'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** cellular automaton; Rule 90; Mersenne circumference; finite-field dynamics; maximal subgroup; exact period; Artin--Mazur zeta.

chinese-simplified

中文摘要

对任意梅森型圆周长度上的循环[Rule 90]{lang="en"}，本文把遍历所有真时钟的并集上界提升为有限时间群极大子群上的精确容斥公式。 各固定子空间交由时钟的最大公因数以及二元有限域多项式最大公因式完全控制。 若圆周长度 $L>3$ 本身还是素数，则零态是唯一不动点，周期像中的其余状态全部具有精确周期 $L$；由此得到精确概率、几何周期数以及完整有限动力 $\zeta$ 函数。 定理适用于每个满足前提的源长度，但不宣称这类长度有无穷多个。圆周因子只描述源时钟子群，并非算术局部因子。

关键词：元胞自动机；[Rule 90]{lang="en"}；梅森圆周；有限域动力系统； 极大子群；精确周期；[Artin--Mazur]{lang="en"} $\zeta$ 函数。

# Periodic image and fixed spaces

Let $L=2^r-1$, $r\geq2$, and identify cyclic binary states with $$R_L=\mathbb F_2[x,x^{-1}]/(x^L-1).$$ Rule 90 multiplies by $a=x+x^{-1}$. Frobenius gives $a^{L+1}=a$. Clearing the invertible monomial $x$ identifies the kernel with that of $(x+1)^2$ modulo the squarefree polynomial $x^L+1$; hence $\dim\ker a=1$. The complete periodic set is $V=\operatorname{im}a$, $\dim V=L-1$, and $g=a|_V$ satisfies $g^L=I$. Every realized period thus divides $L$: if $a^dv=v$ then $v=a(a^{d-1}v)\in V$, while $a^L(au)=a^{L+1}u=au$. The same first implication shows that the full-ring fixed kernel already lies in $V$. For every $d\geq1$, $$D_L(d)=\deg\gcd\bigl(x^L+1,(x^2+1)^d+x^d\bigr),\qquad
|\operatorname{Fix}_V(g^d)|=2^{D_L(d)}.             \tag{1}$$

# The maximal-subgroup sieve

Let $\mathcal P(L)$ denote the distinct ordinary integer prime divisors of the source circumference, computed from $L$ rather than read from any target table. If $v$ has period $m<L$, choose $p\in\mathcal P(L)$ dividing $L/m$. Then $m\mid L/p$, while the converse implication is immediate. Therefore $$\{v\in V:\operatorname{per}(v)<L\}
=\bigcup_{p\in\mathcal P(L)}\operatorname{Fix}(g^{L/p}).       \tag{2}$$ For a nonempty subset $Q\subseteq\mathcal P(L)$, polynomial Bézout identities for $g^L=I$ identify the intersection with the fixed space at the gcd clock. Distinctness of the factors gives $$\bigcap_{p\in Q}\operatorname{Fix}(g^{L/p})
=\operatorname{Fix}\left(g^{L/\prod_{p\in Q}p}\right).        \tag{3}$$ Inclusion--exclusion and (1) now give, for every Mersenne $L$, $$N_{<L}=\sum_{\varnothing\ne Q\subseteq\mathcal P(L)}
(-1)^{|Q|+1}2^{D_L(L/\prod_{p\in Q}p)}.                       \tag{4}$$ Only distinct factors index maximal subgroups; their multiplicities remain present in the intersection clocks $L/\prod_{p\in Q}p$. The singleton sum is an upper bound and singleton-minus-pair sum a lower bound. Equation (4) uses $2^{\omega(L)}-1$ subgroup intersections and records all overlaps exactly; the independent Möbius fixed-point formula gives the same full-period count. This is strictly stronger than an all-proper-clock union bound.

# Closed law at every Mersenne-prime length

Suppose now that $L>3$ is prime. Period support lies in $\{1,L\}$. A fixed mode would require $a=1$, hence $$x^2+x+1=0.                                                     \tag{5}$$ Its nontrivial roots have order three. Since $3\nmid L$, they are absent from the $L$-th roots, so $D_L(1)=0$ and zero is the unique fixed state. Consequently $$P_L(1)=1,\quad P_L(L)=2^{L-1}-1,\quad
C_L(L)=\frac{2^{L-1}-1}{L},\quad
\Pr_V(\operatorname{per}<L)=2^{-(L-1)}.                       \tag{6}$$ The complete finite dynamical zeta is $$\zeta_g(z)=\frac1{(1-z)(1-z^L)^{(2^{L-1}-1)/L}}.              \tag{7}$$ For the sentinels $L=7,31,127$, the numbers of full cycles are respectively $9$, $34{,}636{,}833$, and $(2^{126}-1)/127$. At the excluded $L=3$, (5) divides $x^3+1$ and $g$ is the identity on the four-state image. No infinitude of Mersenne-prime lengths is assumed or claimed.

Exact ledgers for $2\leq r\leq10$ contain 27 subgroup intersections and 38 divisor cells; these are sentinels, not theorem cutoffs. The independent checker passes 186 assertions, SymPy passes 100 checks, replay is byte-identical, and 47 hostile cases are rejected. The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$. Circumference factors index finite source-clock subgroups; they are not arithmetic local or Euler factors. We claim no target divisor, target functional equation/counting law, root number, automorphy, natural self-adjoint or Hilbert--Pólya lift, or Route-B authorization. Scope:

`NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local evidence and code provide exact certificates, an independent checker, symbolic reconstruction, replay, and mutation audit.

#### Ethics.

No human participants, animals, personal, clinical, or sensitive data are used; research ethics approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing at artifact level. AI systems are not authors.

#### Conflicts of interest.

No conflict of interest is known.

#### Funding.

No external funding is reported.

#### AI-use disclosure.

An AI coding assistant supported drafting, exact-code development, and internal proof checking. It was not an external reviewer; released claims are exposed to deterministic, independent-code, symbolic, and hostile checks.
