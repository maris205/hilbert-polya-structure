---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hegselmann-krause-finite-termination-route-a"
canonical_tex: "henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/paper/main.pdf"
source_sha256: "838fccfb67a25f94f6de3180ee967d5e6f7948d80c04009eaebe9cbbddacc87a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Finite Termination and Cell Geometry for One-Dimensional Bounded Confidence

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hegselmann_krause_finite_termination_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the homogeneous one-dimensional Hegselmann--Krause map we prove order and permanent-gap decomposition, exact finite termination within $4n^3+2n+2$ updates, and the complete fixed-cluster classification. \>0 We also describe every strict neighbor cell as a rational row-stochastic linear map, retain threshold discontinuities and affine covariance, and give an exact counterexample to mean conservation. \>1 An exhaustive 801-system rational archive and independent adversarial lanes audit the theorem without replacing its all-data proof.
author:
- 'Route-A source-local certificate HCS-C312'
date: 3 September 2026
title: 'Exact Finite Termination and Cell Geometry for One-Dimensional Bounded Confidence'
```

## Markdown 正文

trailerid \[\<C3122026090300000000000000000000\>\<C3122026090300000000000000000000\>\]

# Order, decomposition, and finite-time theorem

Let $\varepsilon>0$ and, after sorting the labels, set $$\label{eq:hk}
 N_i(t)=\{j:|x_j(t)-x_i(t)|\le\varepsilon\},\qquad
 x_i(t+1)=\frac1{|N_i(t)|}\sum_{j\in N_i(t)}x_j(t).$$ The inequality is closed: a pair at distance exactly $\varepsilon$ interacts.

[\[thm:hk\]]{#thm:hk label="thm:hk"} For every $n\ge1$ and every real initial state:

1.  order, coincident blocks, and the convex hull are preserved;

2.  a consecutive gap greater than $\varepsilon$ never closes and splits the dynamics into independent subsystems;

3.  the state becomes exactly fixed by time $4n^3+2n+2$;

4.  a state is fixed iff its distinct occupied positions are separated by gaps strictly greater than $\varepsilon$.

The key quantitative fact is included for clarity.

[\[lem:progress\]]{#lem:progress label="lem:progress"} If the system is not fixed at time $t$, let $\ell$ be its leftmost nonfrozen position block. By time $t+2$, that block has gained multiplicity, has frozen, or its position has moved right by at least $\varepsilon/(2n^2)$.

Scale to $\varepsilon=1$ and let $r$ be the first strictly right neighbor of $\ell$. If their neighborhoods coincide, their next averages coincide and the left block gains weight. Otherwise $r$ has a right neighbor unseen by $\ell$, hence beyond $x_\ell+1$. Direct averaging over at most $n$ points gives $x_r(t+1)\ge x_\ell(t)+1/n$. If $\ell$ itself moved by $1/(2n)$ we are done. Otherwise their new separation is at least $1/(2n)$. If it now exceeds one, $\ell$ freezes; if not, the next average moves its block by at least another factor $1/n$. Rescaling proves the claim.

The average of two ordered interval neighborhoods is ordered; identical positions have identical neighborhoods. Every update lies in its neighborhood convex hull. If a consecutive gap exceeds $\varepsilon$, the two sides never average across it and their separate convex hulls cannot approach, proving items 1--2.

Decompose the initial state at all such gaps. A component of $m$ agents has width at most $(m-1)\varepsilon$. Apply Lemma [\[lem:progress\]](#lem:progress){reference-type="ref" reference="lem:progress"} at even times. The leftmost active position is nondecreasing; multiplicity/freeze events exhaust at most $m$ labels, while displacement events occur at most $2m^3$. Thus the component stops within $4m^3+2m+2$ updates. Independent components evolve in parallel, so the full stopping time is their maximum; since every $m_j\le n$, this is at most $4n^3+2n+2$, proving item 3.

Clusters separated by strict gaps are plainly fixed. Conversely, the leftmost occupied position having any distinct neighbor within $\varepsilon$ would average strictly to the right, contradicting fixedness. This proves item 4.

\>0

# Strict cells, covariance, and the missing mean invariant

Away from threshold hyperplanes $|x_i-x_j|=\varepsilon$, the neighbor graph $G$ is locally constant and [\[eq:hk\]](#eq:hk){reference-type="eqref" reference="eq:hk"} is $$\label{eq:matrix}
 x^+=A_Gx,\qquad (A_G)_{ij}=|N_i|^{-1}{\bf1}_{\{j\in N_i\}}.$$ Thus $A_G\mathbf1=\mathbf1$, but its columns need not sum to one. The global map is piecewise rational linear and generally discontinuous across a closed threshold face because a new averaging edge is inserted there.

Translation by $c$ commutes with the map. Multiplying both opinions and $\varepsilon$ by $s>0$ multiplies every later state by $s$. In contrast, the arithmetic mean is not invariant. With $\varepsilon=1$, $$\label{eq:mean}
 (0,1/2,7/5)\longmapsto(1/4,19/30,19/20),
 \qquad 19/30\longmapsto11/18,$$ a drift of $-1/45$. This is exactly the failure of $A_G$ to be doubly stochastic; it does not conflict with order or convex-hull preservation.

\>1

# Evidence, collisions, and Route-A boundary

All 791 nondecreasing half-integer configurations with $n\le5$, plus ten signed, scaled, threshold, duplicate and mean-drift controls, are evolved in exact rational arithmetic. The archive retains 1,843 states and 28,895 leaves; its maximum observed stop is six and 209 cases change mean. An independent implementation performs 28,870 checks, SymPy closes 38 exact identities, replay is byte-identical, and 26 repaired-hash or parser attacks must fail. The finite grid is a regression oracle; Lemma [\[lem:progress\]](#lem:progress){reference-type="ref" reference="lem:progress"} proves the all-real theorem.

C203 uses a fixed signed graph and continuous semigroup, C259 a tree Kuramoto flow, and C301 a random absorbing partition refinement. C312 has a deterministic state-dependent confidence graph and literal finite stopping.

The exact tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ Agent and threshold data have no rational-prime owner (A0); all trajectories eventually fix, leaving no nontrivial primitive cycles (A1); update time is not a logarithmic-prime roof (A2); the rational cell matrices give no target determinant (A3) or self-adjoint target-zero quantization (A4). Route A is rejected and Route B stays locked under `NO_BAD_EULER_OR_ROOT_NUMBER`. No target Euler factor, root number, automorphy, divisor law, functional equation, or zero match is asserted.

#### AI use.

A generative language model assisted prose and code scaffolding. The reproduced proof, exact independent trajectories, adversarial tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 A. Bhattacharyya, M. Braverman, B. Chazelle, and H. L. Nguyen, "On the convergence of the Hegselmann--Krause system," *ITCS 2013*, 61--66. [arXiv:1211.1909](https://arxiv.org/abs/1211.1909).
