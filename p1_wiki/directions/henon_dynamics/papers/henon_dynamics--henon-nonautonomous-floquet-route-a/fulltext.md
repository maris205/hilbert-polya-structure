---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-nonautonomous-floquet-route-a"
canonical_tex: "henon_dynamics/henon_nonautonomous_floquet_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_nonautonomous_floquet_route_a/paper/main.pdf"
source_sha256: "4a910f96c1ba2099200043ab161616dd807dd4a92c7df41dd27810e61172e95b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Chronological Floquet Prefixes for a Periodically Forced Hénon Candidate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_nonautonomous_floquet_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_nonautonomous_floquet_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_nonautonomous_floquet_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_nonautonomous_floquet_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a deliberately finite Route-A pilot for a period-two quadratic Hénon cocycle. The two maps are $F_t(x,y)=(x^2+\alpha_t x+\beta_t-y,x)$ with $(\alpha_0,\beta_0)=(0,0)$ and $(\alpha_1,\beta_1)=(1,1/3)$. Frozen samples at $\xi=-1,+1$ give exact Jacobian templates. A block symbol records one branch at each forcing phase, and an admissible four-state word model yields an $8\times8$ matrix-valued Floquet prefix. We retain the chronological product $B_{1,s_1}B_{0,s_0}$ and compare it with reversed and same-phase controls. Twenty-four primitive necklaces through block period six, all trace decompositions, determinant prefixes, and Newton identities are independently checked. This is an A1 weak symbolic pilot and an A2 discrete prefix only: no geometric coding, Fredholm owner, arithmetic data, or Hilbert--Pólya operator is claimed.
author:
- Anonymous
title: Chronological Floquet Prefixes for a Periodically Forced Hénon Candidate
```

## Markdown 正文

# Candidate and frozen conventions

Consider the period-two area-preserving cocycle $$F_t(x,y)=(x^2+\alpha_t x+\beta_t-y,x),\qquad
 (\alpha_0,\beta_0)=(0,0),\quad (\alpha_1,\beta_1)=(1,1/3).$$ Each Jacobian has determinant one. We freeze two branch samples $\xi_0=-1,\xi_1=1$ and set $$B_{t,s}=\begin{pmatrix}2\xi_s+\alpha_t&-1\\1&0\end{pmatrix},
 \qquad s\in\{0,1\}.$$ Thus the phase slopes are $(-2,2)$ and $(-1,3)$. The samples are modeling representatives, not asserted periodic points. A block symbol is $u=(s_0,s_1)$, encoded by $2s_0+s_1$, and the chronological two-step Floquet matrix is $$M_u=B_{1,s_1}B_{0,s_0}.$$ For a finite symbolic control we use $$Q=\begin{pmatrix}1&1&0&0\\0&1&1&0\\1&0&0&1\\0&1&0&1\end{pmatrix}.$$ This adjacency is explicitly a frozen pilot choice, not a claimed Markov partition of the real Hénon map.

# Primitive ledger and Floquet controls

Let $\mathcal P_n$ be the lexicographically least rotations of admissible, non-periodic words of block length $n$. The counts for $n=1,\ldots,6$ are $$3,\;0,\;2,\;4,\;6,\;9,$$ for a total of 24. Every row records the phase pair, rooted-start multiplicity, cyclic stabilizer, orientation, all three monodromies, and repeated traces. For a word $w=(w_0,\ldots,w_{n-1})$, the row-transfer convention is $M_w=M_{w_0}\cdots M_{w_{n-1}}$; each individual block $M_u$ still has the physical chronological order $B_1B_0$.

The three controls are chronological $(0,1)$, reversed $(1,0)$, and same-phase $(0,0)$. Their exact transfer trace vectors through six blocks are $$\begin{array}{c|rrrrrr}
\toprule
 &1&2&3&4&5&6\\
\midrule
\text{chronological} &-4&74&-184&2214&-7604&73538\\
\text{reversed}       &-4&74&8&1702&4556&34370\\
\text{same phase}     &-2&38&202&-986&10538&-26626\\
\bottomrule
\end{array}$$ The chronological and reversed rows differ for 17 of the 24 primitive necklaces, so the finite word control detects noncommuting phase order.

For any of the three controls and $1\le n\le6$, let $A_{ij}=Q_{ij}M_j$ be the $8\times8$ block transfer matrix. Then $$\operatorname{Tr}(A^n)=\sum_{d\mid n}d
 \sum_{[w]\in\mathcal P_d}\operatorname{Tr}(M_w^{\,n/d}).$$

Expand the block trace over closed admissible symbol paths. Each path is a repetition of one primitive cyclic word of length $d\mid n$, with $d$ distinguished starts. The target-weighted block convention gives the stated right product, and trace cyclicity removes the choice of starting point. The exact checker verifies the identity for all six lengths and all controls.

# Finite determinant and reproducibility

The low-to-high coefficients of $\det(I-zA)$ are recorded separately for each control. They are $$\begin{aligned}
 D_{01}:&\ (1,4,-29,-76,91,-120,-19,0,4),\\
 D_{10}:&\ (1,4,-29,-140,-37,-184,-19,0,4),\\
 D_{00}:&\ (1,2,-17,-104,255,-134,-27,4,4).
\end{aligned}$$ These are finite-dimensional polynomial identities, not Fredholm determinants. SymPy independently reproduces all 18 trace powers, the three determinants, and 18 Newton recurrences. Canonical replay passes, and ten hostile semantic mutations are rejected.

# Route-A assessment and boundary

The release evidence is an exact canonical JSON ledger generated without any prime or zero table. The local qualification is $$A1=\texttt{A1\_WEAK}\;(\text{non-autonomous symbolic pilot}),\qquad
 A2=\texttt{A2\_CERTIFIED\_PREFIX}\;(\text{discrete Floquet prefix}),$$ with $A3=\texttt{A3\_NOT\_ADDRESSED}$ and $A4=\texttt{A4\_FAIL}$. A geometric coding theorem, completeness of real Hénon periodic orbits, a function-space Fredholm owner, global zero counts, and analytic continuation are not supplied. Accordingly the determinant notation above is not promoted to a dynamical zeta theorem. No arithmetic/local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Route-B authorization is present.

The next meaningful experiment is to solve the actual period-two periodic equations with certified interval or algebraic methods and compare their monodromies to this pilot after the symbolic choices have been frozen.
