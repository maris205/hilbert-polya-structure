---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-local-jet-koopman-route-a"
canonical_tex: "henon_dynamics/henon_local_jet_koopman_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_local_jet_koopman_route_a/paper/main.pdf"
source_sha256: "71a6b99b9de97e7ffd4038278d80ceb3093108d2fa728a09c193b191b7e83b50"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Fifteen-Dimensional Local Koopman Jet for a Polynomial Hénon Germ

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_local_jet_koopman_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_local_jet_koopman_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_local_jet_koopman_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_local_jet_koopman_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct the exact Koopman pullback of the polynomial germ $F(u,v)=(u^2+3u/2-v/2,u)$ on the local algebra $A_4=\mathbb Q[u,v]/(u,v)^5$. In its fifteen-element monomial basis, the operator has trace $129/16$, determinant $2^{-20}$, and a characteristic polynomial determined by five associated-graded blocks. The nonlinear term changes eleven matrix entries, but only in strictly degree-raising positions; the correction is nilpotent of index four. The resulting finite determinant is an exact operator-first Route-A prefix. It is not a global Koopman spectrum or Fredholm determinant, and no arithmetic or Route-B claim is made.
author:
- 'Anonymous Route-A report'
title: |
  An Exact Fifteen-Dimensional Local Koopman Jet\
  for a Polynomial Hénon Germ
```

## Markdown 正文

# A finite local operator

Let $\mathfrak m=(u,v)$ and freeze $$F(u,v)=\left(u^2+\frac32u-\frac12v,\;u\right),
 \qquad F(0,0)=(0,0).$$ Because both coordinates of $F$ lie in $\mathfrak m$, pullback sends $\mathfrak m^5$ into itself. Composition therefore defines the rational operator $$K:A_4\longrightarrow A_4,\qquad K[p]=[p\circ F],
 \quad A_4=\mathbb Q[u,v]/\mathfrak m^5.$$ We order the basis by total degree, $$\mathcal B=(1;u,v;u^2,uv,v^2;u^3,u^2v,uv^2,v^3;
 u^4,u^3v,u^2v^2,uv^3,v^4),$$ and use the convention that column $j$ contains $K(\mathcal B_j)$. Exact truncated substitution gives all $225$ matrix cells in the accompanying evidence. For example, $$K[u]=u^2+\frac32u-\frac12v,\qquad K[v]=u,$$ so the finite operator already retains nonlinear information.

# Graded blocks and exact determinant

The total-degree filtration is $K$-invariant. On its degree-$d$ quotient, only the linearization $$L(u,v)=\left(\frac32u-\frac12v,u\right),\qquad
 DL(0)=\begin{pmatrix}3/2&-1/2\\1&0\end{pmatrix}$$ survives. Its eigenvalues are $1$ and $1/2$, so the degree-$d$ pullback has eigenvalues $1,1/2,\ldots,2^{-d}$. Table [1](#tab:blocks){reference-type="ref" reference="tab:blocks"} records the five exact blocks without printing an unreadable full matrix.

::: {#tab:blocks}
   $d$   dimension       eigenvalues         trace    determinant
  ----- ----------- ---------------------- --------- -------------
    0        1               $1$              $1$         $1$
    1        2             $1,1/2$           $3/2$       $1/2$
    2        3           $1,1/2,1/4$         $7/4$       $1/8$
    3        4         $1,1/2,1/4,1/8$      $15/8$      $1/64$
    4        5       $1,1/2,1/4,1/8,1/16$   $31/16$    $1/1024$

  : Associated-graded data for the order-four jet.
:::

On $A_4$, eigenvalue $2^{-k}$ has algebraic multiplicity $5-k$. Hence $$\chi_K(\lambda)=\prod_{k=0}^{4}(\lambda-2^{-k})^{5-k},\qquad
 \det(I-zK)=\prod_{k=0}^{4}(1-2^{-k}z)^{5-k}.$$ In particular $\operatorname{tr}K=129/16$, $\det K=2^{-20}$, and $$\operatorname{tr}(K^n)=\sum_{k=0}^{4}(5-k)2^{-kn}\quad(1\leq n\leq8).$$

In the degree-ordered basis, $K$ is block triangular. Its diagonal blocks are the homogeneous pullbacks of $L$, whose degree-$d$ eigenvalues are the monomials $1^{d-k}(1/2)^k$. Multiplying the five block characteristic polynomials proves both factorizations; summing and multiplying their eigenvalues gives the trace formulas and determinant.

# Nonlinear signal and linear control

Let $K_{\rm lin}$ be the pullback obtained by replacing $F$ with $L$ and let $N=K-K_{\rm lin}$. Independent exact reconstruction finds eleven nonzero entries in $N$. Every one maps a degree-$d$ column to a row of strictly higher degree, and direct multiplication gives $N^4=0$ but $N^3\ne0$. Thus $K\ne K_{\rm lin}$ while their diagonal graded blocks, characteristic polynomials, and finite determinants agree. This comparison prevents two opposite errors: discarding the nonlinear jet, or attributing new finite eigenvalues to a strictly filtration-raising correction.

The canonical ledger also stores the first eight traces of powers. A producer using rational polynomial dictionaries, a checker with a separately written engine, and a fresh SymPy expansion agree on every matrix cell and identity. Canonical replay fixes the evidence bytes; thirteen hostile edits to the model, basis, matrix, invariants, verdict, and nonclaims are all rejected.

# Route-A boundary

The A1 result is partial-certified only for one fixed point and its order-four local jet. The A2 result is certified-prefix only for the finite fifteen-dimensional quotient $A_4$. No global orbit classification, invariant Banach or Hilbert space, global Koopman spectrum, nuclearity, analytic tail theorem, or Fredholm determinant has been established; A3 is not addressed and A4 fails.

In particular, the displayed $\det(I-zK)$ is an ordinary finite matrix determinant. We make no claim about arithmetic/local data, Euler factors, root numbers, automorphy, Riemann zeros, a Hilbert--Pólya operator, or Route B. The release scope is the literal `NO_BAD_EULER_OR_ROOT_NUMBER`.
