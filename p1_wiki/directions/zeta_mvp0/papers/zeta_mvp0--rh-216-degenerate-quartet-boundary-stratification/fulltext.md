---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-216-degenerate-quartet-boundary-stratification"
canonical_tex: "zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification/main.pdf"
source_sha256: "1424339f05eaa8bbd50393234d5e8b3131c32d589a1b983024b5d6c67456205c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Boundary Stratification of the Centered Quartet Manifold Discriminant Factorization and Uniform Collapse to a Double Pair

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-216-degenerate-quartet-boundary-stratification/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The finite shape clock of RH-214 moves monotonically in the axial coordinate $u$, and RH-215 finds a power-gap model to be the best of three finite extrapolants. Neither result proves a limit. This paper instead answers the conditional geometric question exactly: what happens to a centered conjugate quartet if $u$ approaches the boundary value one?

  For the canonical shape polynomial $Q_{u,\eta}$, we prove $$\operatorname{Disc}Q_{u,\eta}
   =256(1-u)^2(1-\eta^2)
     \bigl[4u+(1-u)^2\eta^2\bigr]^2.$$ Hence degeneracy occurs precisely on the axial edge $u=1$, on either edge $|\eta|=1$, or at the isolated point $(u,\eta)=(0,0)$. The strata correspond respectively to two real double roots, one real double pair, and coincident imaginary conjugate pairs.

  Uniformly for $|\eta|\le1$, the root multiset approaches $\{1,1,-1,-1\}$ as $u\to1$, with an explicit matching bound $$d_{\rm root}\le \sqrt{2(1-u)}+
   \frac{1-u}{1+\sqrt u}.$$ The coefficient distance to $(z^2-1)^2$ is exactly $4(1-u)$ in maximum norm. Thus axial convergence, coefficient convergence, and root-multiset convergence are equivalent. Six hundred random checks verify the formulas to roundoff. The physical data move toward this stratum but reach only $u\approx0.718$ at the finest anchor; no physical convergence claim is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Boundary Stratification of the Centered Quartet Manifold\
  Discriminant Factorization and Uniform Collapse to a Double Pair
```

## Markdown 正文

# Conditional geometry without a convergence claim

RH-213 gives the exact canonical roots $$\label{eq:roots}
 a\pm ib,\qquad -a\pm id,$$ where $$\label{eq:abd}
 a=\sqrt u,qquad
 b^2=(1-u)(1+\eta),qquad
 d^2=(1-u)(1-\eta)$$ for $(u,\eta)\in[0,1]\times[-1,1]$ [@WangRH213]. The polynomial is $$\label{eq:poly}
 Q_{u,\eta}(z)=z^4+(2-4u)z^2
 +4\sqrt u(1-u)\eta z+1-\eta^2(1-u)^2.$$

RH-214 observes finite monotonicity of $u$ and RH-215 tests three candidate tails [@WangRH214; @WangRH215]. We do not assume any of those tails. All results below hold for an arbitrary point of the compact shape rectangle.

# Quadratic factorization

Write $$\label{eq:factors}
 Q_+(z)=(z-a)^2+b^2,qquad
 Q_-(z)=(z+a)^2+d^2,qquad Q=Q_+Q_-.$$ The discriminants of the two monic quadratics are $-4b^2$ and $-4d^2$.

[\[lem:resultant\]]{#lem:resultant label="lem:resultant"} The resultant of the two factors is $$\label{eq:resultant}
 \operatorname{Res}(Q_+,Q_-)
 =4\bigl[4u+(1-u)^2\eta^2\bigr].$$

Evaluating $Q_-$ at the two roots $a\pm ib$ of $Q_+$ gives $$\begin{aligned}
 \operatorname{Res}(Q_+,Q_-)
 &=\bigl((2a+ib)^2+d^2\bigr)
   \bigl((2a-ib)^2+d^2\bigr)\\
 &=\bigl(4a^2-b^2+d^2\bigr)^2+16a^2b^2.\end{aligned}$$ Using [\[eq:abd\]](#eq:abd){reference-type="eqref" reference="eq:abd"}, the terms linear in $\eta$ cancel and the expression reduces to [\[eq:resultant\]](#eq:resultant){reference-type="eqref" reference="eq:resultant"}.

# Complete discriminant factorization

For monic polynomials, $$\operatorname{Disc}(Q_+Q_-)
 =\operatorname{Disc}(Q_+)\operatorname{Disc}(Q_-)
  \operatorname{Res}(Q_+,Q_-)^2.$$

[\[thm:disc\]]{#thm:disc label="thm:disc"} For the canonical quartet, $$\label{eq:disc}
 \boxed{
 \operatorname{Disc}Q_{u,\eta}
 =256(1-u)^2(1-\eta^2)
 \bigl[4u+(1-u)^2\eta^2\bigr]^2.}$$

Since $b^2d^2=(1-u)^2(1-\eta^2)$, the product of the two quadratic discriminants is $16(1-u)^2(1-\eta^2)$. Multiplying by the square of [\[eq:resultant\]](#eq:resultant){reference-type="eqref" reference="eq:resultant"} proves [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"}.

# Degeneracy strata

All factors in [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"} are nonnegative on the shape rectangle.

[\[cor:strata\]]{#cor:strata label="cor:strata"} The quartet has a repeated root if and only if at least one of the following holds:

1.  $u=1$;

2.  $|\eta|=1$;

3.  $(u,\eta)=(0,0)$.

The first two factors in [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"} give the first two cases. The final square bracket vanishes only when both nonnegative terms $4u$ and $(1-u)^2\eta^2$ vanish, which is exactly $u=0$, $\eta=0$.

The geometry of each stratum is explicit:

$u=1$

:   $a=1$ and $b=d=0$, giving roots $1,1,-1,-1$.

$\eta=1$

:   $d=0$, so the negative-real pair coalesces at $-\sqrt u$; for $\eta=-1$, the positive-real pair coalesces at $+\sqrt u$.

$(u,\eta)=(0,0)$

:   $a=0$ and $b=d=1$, so both quadratic factors equal $z^2+1$ and the roots $\pm i$ each have multiplicity two.

Intersections carry the corresponding higher overlap, but introduce no new zero set.

# Uniform collapse along the axial boundary

Let $\mathcal B=\{1,1,-1,-1\}$, with multiplicity, and let $d_{\rm match}$ be the minimum over root permutations of the maximum paired distance.

[\[thm:collapse\]]{#thm:collapse label="thm:collapse"} For every $(u,\eta)$ in the shape rectangle, $$\label{eq:rootbound}
 d_{\rm match}(\operatorname{roots}Q_{u,\eta},\mathcal B)
 \le \sqrt{2(1-u)}+\frac{1-u}{1+\sqrt u}.$$ In particular the convergence to $\mathcal B$ is uniform in $\eta$ as $u\to1$.

Match the two roots with real part $a=\sqrt u$ to $1$ and the two with real part $-a$ to $-1$. For the positive pair, $$|a\pm ib-1|\le |1-a|+b
 \le \frac{1-u}{1+\sqrt u}+\sqrt{2(1-u)},$$ because $b^2\le2(1-u)$. The same estimate holds for the negative pair using $d^2\le2(1-u)$.

The square-root term is natural at root level: imaginary heights vanish like $\sqrt{1-u}$ in the worst transverse direction.

# Coefficient collapse and equivalence

The boundary polynomial is $$Q_{1,\eta}(z)=(z^2-1)^2=z^4-2z^2+1,$$ independent of $\eta$.

[\[prop:coeffdistance\]]{#prop:coeffdistance label="prop:coeffdistance"} Let $C(u,\eta)=(1,0,c_2,c_3,c_4)$ and $C_\star=(1,0,-2,0,1)$. Then $$\label{eq:coeffdistance}
 \left\lVert C(u,\eta)-C_\star\right\rVert_\infty=4(1-u).$$

The $c_2$ difference is exactly $4(1-u)$. Moreover $$|c_3|\le4\sqrt u(1-u)\le4(1-u),qquad
 |c_4-1|\le(1-u)^2\le4(1-u).$$ Thus no other coefficient exceeds the $c_2$ difference.

[\[cor:equiv\]]{#cor:equiv label="cor:equiv"} For any sequence $(u_n,\eta_n)$ in the shape rectangle, the following are equivalent:

1.  $u_n\to1$;

2.  $Q_{u_n,\eta_n}\to(z^2-1)^2$ coefficientwise;

3.  the root multisets converge to $\mathcal B$ in matching distance.

Proposition [\[prop:coeffdistance\]](#prop:coeffdistance){reference-type="ref" reference="prop:coeffdistance"} proves equivalence of the first two. Theorem [\[thm:collapse\]](#thm:collapse){reference-type="ref" reference="thm:collapse"} gives the first implies the third. Conversely, root convergence forces the positive real branch coordinate $\sqrt{u_n}$ to approach one.

# Machine audit and physical position

Six hundred uniformly sampled parameter pairs verify Theorem [\[thm:disc\]](#thm:disc){reference-type="ref" reference="thm:disc"} by direct root-product discriminants. The maximum relative error, normalized by $\max(1,|\operatorname{Disc}|)$, is below $10^{-14}$; no violation of [\[eq:rootbound\]](#eq:rootbound){reference-type="eqref" reference="eq:rootbound"} occurs.

For the physical atlas, $u$ rises from about $0.02$ to about $0.718$. Consequently the maximum-norm coefficient distance in [\[eq:coeffdistance\]](#eq:coeffdistance){reference-type="eqref" reference="eq:coeffdistance"} falls monotonically, but at the finest level it is still approximately $1.13$. The matching distance to the double pair is about $0.577$. These are directional observations, not evidence that the asymptotic regime has been reached.

# Route consequence and claim boundary

The axial boundary is now mathematically understood. If a later analytic or validated argument proves $u_\sigma\to1$, no separate control of $\eta$ is needed for coefficient convergence: transverse dependence is uniformly suppressed. RH-217 quantifies that suppression differentially.

Even a proved fixed-quartet limit would still have only four roots, with two limiting locations. It cannot by itself provide a growing spectral divisor. No physical limit, determinant construction, Gate-A closure, Hilbert--Pólya operator, or zeta statement is asserted here.
