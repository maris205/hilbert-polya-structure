---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-polynomial-multibranch-route-a"
canonical_tex: "henon_dynamics/henon_polynomial_multibranch_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_polynomial_multibranch_route_a/paper/main.pdf"
source_sha256: "eadadae4084b7841401bcbadfc3c5fb69d2ba8a08b3ecc071687c4366a310f5f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Three-Branch Polynomial Hénon Candidate: Exact Primitive-Word and Transfer-Prefix Pilot

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_polynomial_multibranch_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_polynomial_multibranch_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_polynomial_multibranch_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_polynomial_multibranch_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We design a three-branch polynomial Hénon candidate for Route A and report an exact, deliberately limited pilot. For $H_a(x,y)=(x^3-3x+a-y,x)$ at $a=1/7$, the cubic has three monotonicity intervals. We freeze their full one-sided symbolic word model and three representative Jacobian samples, enumerate all primitive necklaces through length six, and build a $6\times6$ matrix-valued transfer prefix. Integer trace decomposition and the finite determinant are independently reproduced and mutation-tested. No complete Hénon coding or Fredholm ownership is assumed: the result is an A1 symbolic pilot and an A2 discrete prefix only.
author:
- Anonymous
title: |
  A Three-Branch Polynomial Hénon Candidate:\
  Exact Primitive-Word and Transfer-Prefix Pilot
```

## Markdown 正文

# Candidate and evidence boundary

Consider the area-preserving polynomial Hénon map $$H_{1/7}(x,y)=(x^3-3x+1/7-y,x),\qquad
 \det DH_{1/7}=1.$$ The cubic's monotonicity intervals are labeled $0,1,2$ by $( -\infty,-1),(-1,1),(1,\infty)$. A Markov partition, invariant compact set, and coding theorem are not supplied here; instead we explicitly freeze the full shift $\Sigma_3$ as a falsifiable screening model. At $\xi=(-2,0,3)$ the derivative samples are $\sigma=(9,-3,24)$ and $$B_j=\begin{pmatrix}\sigma_j&-1\\1&0\end{pmatrix},\qquad \det B_j=1.$$ These are representative matrices, not asserted periodic-orbit monodromies.

# Primitive ledger and finite transfer

For a word $w\in\{0,1,2\}^n$, let $[w]$ be its lexicographically least cyclic rotation, retaining it only when $w$ is not a repetition. Put $B_w=B_{w_{n-1}}\cdots B_{w_0}$. The block transfer matrix $A$ has $2\times2$ blocks $A_{ij}=B_j$ for every $i,j\in\{0,1,2\}$. Direct integer enumeration gives the following primitive-necklace counts.

      length $n$       1   2   3    4    5     6   total
  ------------------ --- --- --- ---- ---- ----- -------
   $|\mathcal P_n|$    3   3   8   18   48   116     196

For $1\le n\le6$, $$\operatorname{Tr}(A^n)=\sum_{d\mid n}d
 \sum_{[w]\in\mathcal P_d}\operatorname{Tr}(B_w^{n/d}).$$

Expand the block trace as a sum over closed length-$n$ symbol paths. Each path is a repetition of a unique primitive necklace of length $d\mid n$; there are $d$ distinguished starts, and cyclic invariance of trace identifies the corresponding matrix products. The certificate checks the equality for all six values of $n$ with integer arithmetic.

For this frozen sample, the direct trace vector is $$(\operatorname{Tr}A,\ldots,\operatorname{Tr}A^6)=
(30,882,26190,777762,23097150,685914642),
\qquad D(z)=1-30z+9z^2.$$

Writing $D(z)=\det(I-zA)=\sum c_kz^k$, SymPy independently verifies $$k c_k=-\sum_{j=1}^k c_{k-j}\operatorname{Tr}(A^j),\qquad 1\le k\le6,$$ with zero coefficients after the actual degree. The observed degree-two collapse is a diagnostic of the rank-one block construction, not a spectral claim.

# Route-A assessment and reproducibility

The canonical evidence file records all 196 rows, branch counts, matrices, repeated traces, six direct traces, primitive decompositions, and determinant coefficients. An independent checker, a SymPy/Newton cross-check, canonical replay, and nine hostile mutations all pass. The finite matrix is not called a Fredholm operator: no function space, nuclearity estimate, geometric orbit completeness, or zero-count experiment is claimed. Accordingly, the four-layer status is recorded as $$\begin{aligned}
A1&=\texttt{A1\_OPEN}\;\text{(symbolic-pilot qualification)},\\
A2&=\texttt{A2\_CERTIFIED\_PREFIX}\;\text{(discrete-prefix qualification)},\\
A3&=\texttt{A3\_NOT\_ADDRESSED},\qquad A4=\texttt{A4\_FAIL}.
\end{aligned}$$ No arithmetic/local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Route-B authorization is present. The next experiment must freeze a compact candidate set and independently solve the actual Hénon periodic equations before upgrading A1.
