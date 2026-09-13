---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dissipative-route-a"
canonical_tex: "henon_dynamics/henon_dissipative_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dissipative_route_a/paper/main.pdf"
source_sha256: "8a3d9aaf19177dc7e3dcf1a9d0482ad6a144b316876fe54b4663534a8abd4e8d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Dissipative Hénon Cycle and Discrete Transfer Prefix

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dissipative_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dissipative_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dissipative_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dissipative_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the dissipative polynomial Hénon map $F(x,y)=(x^2-91/16-y,x/2)$. Its two fixed points and one genuine period-two orbit are rational and are recovered by exact elimination. A local Jacobian-denominator potential on these four certified witnesses gives a finite weighted transition matrix with determinant $1+18z^2/175-z^4/175$. This is a reproducible discrete transfer prefix, not a global Fredholm determinant: a complete real coding and an analytic operator owner are not established. The paper therefore records a bounded Route-A result and makes no arithmetic or Route-B claims.
author:
- 'Anonymous Route-A report'
title: An Exact Dissipative Hénon Cycle and Discrete Transfer Prefix
```

## Markdown 正文

# Frozen dissipative model

We use the companion form $$F(x,y)=\left(x^2+a-y,\;bx\right),
 \qquad a=-\frac{91}{16},\quad b=\frac12.$$ Its derivative is $$DF(x,y)=\begin{pmatrix}2x&-1\\[1pt]1/2&0\end{pmatrix},
 \qquad \det DF=\frac12.$$ Thus every one-step area element is contracted by a factor $1/2$. This simple dissipative subtype is intentionally independent of any previously used symbolic survivor or arithmetic data.

# Exact low-period algebra

The fixed equation uses $y=x/2$, and hence $$x^2-\frac32x-\frac{91}{16}
 =\frac{(4x-13)(4x+7)}{16}.$$ The two fixed points are $$p_+=\left(\frac{13}{4},\frac{13}{8}\right),
 \qquad
 p_- =\left(-\frac74,-\frac78\right).$$ For $F^2(x,y)=(x,y)$, eliminating $y$ gives $$\operatorname{Res}_y
 =\frac{(4x-13)(4x-5)(4x+7)(4x+11)}{256}.$$ After removing the fixed factors, the primitive factor is $(4x-5)(4x+11)$. Direct substitution gives the genuine two-cycle $$q_+=\left(\frac54,-\frac{11}{8}\right)
 \longmapsto
 q_- =\left(-\frac{11}{4},\frac58\right)
 \longmapsto q_+.$$ No completeness beyond the roots of this finite $F^2$ resultant is used.

For reference, the local Jacobian data are summarized in Table [1](#tab:cycles){reference-type="ref" reference="tab:cycles"}. The determinant $1/2$ is the same at every point, while the denominator $\det(I-DF)$ distinguishes the four witnesses.

::: {#tab:cycles}
  state    point $(x,y)$   $\det(I-DF)$    $\omega=\det(I-DF)^{-1}$
  ------- --------------- -------------- --------------------------
  $p_+$    $(13/4,13/8)$       $-5$                          $-1/5$
  $p_-$    $(-7/4,-7/8)$       $5$                            $1/5$
  $q_+$    $(5/4,-11/8)$       $-1$                            $-1$
  $q_-$    $(-11/4,5/8)$       $7$                            $1/7$

  : Exact cycle witnesses and local weights.
:::

# A finite weighted transfer witness

To make the finite nature explicit, order the four states as $(p_+,p_-,q_+,q_-)$ and put the source weight on each exact transition. The resulting matrix is $$M=\begin{pmatrix}
 -1/5&0&0&0\\
 0&1/5&0&0\\
 0&0&0&-1\\
 0&0&1/7&0
 \end{pmatrix}.$$ Its first six traces are $$0,\; -\frac{36}{175},\;0,\;\frac{1348}{30625},\;0,
 \;-\frac{30564}{5359375},$$ and direct factorization gives $$\det(I-zM)=\left(1-\frac{z^2}{25}\right)
 \left(1+\frac{z^2}{7}\right)
 =1+\frac{18}{175}z^2-\frac1{175}z^4.$$ The unweighted underlying permutation has two primitive cycles of length one and one primitive cycle of length two. These are certified witnesses, not a claim that the full dissipative map has only three primitive orbits.

The fixed points, the primitive two-cycle, the displayed Jacobian weights, all six traces, and the determinant factorization are exact identities independently reproduced by the checker and by a separate SymPy calculation.

The checker reconstructs the two elimination equations, substitutes each listed rational point, and rebuilds $M$ from the transition rule. The cross-check recomputes the resultant and the characteristic determinant from fresh symbolic expressions. Replay and hostile mutation tests close the byte-level evidence boundary.

# Route-A boundary

This package earns the A1 partial-certified level: exact fixed and primitive period-two witnesses are complete for the frozen $F^2$ elimination, but no global real coding or primitive-orbit atlas is supplied. It earns the A2 certified-prefix level only for the four-state discrete weighted graph. Calling $\det(I-zM)$ a Fredholm determinant of $F$ would require a named function space, an invariant/compact transfer operator, and a tail theorem; none is asserted here.

We explicitly make no claim about Euler factors, root numbers, automorphy, Riemann zeros, a Hilbert--Pólya operator, or Route B. The source, exact evidence, independent tests, and content-addressed manifest are distributed with this paper.
