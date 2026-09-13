---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-holte-carries-base-semigroup-route-a"
canonical_tex: "henon_dynamics/henon_holte_carries_base_semigroup_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_holte_carries_base_semigroup_route_a/paper/main.pdf"
source_sha256: "34a8922fbe330c6206cdb5693ff05c4067739c6b5427546dca5afe310c2ca904"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Base Semigroup of Holte's Carries Chain: An Exact Route-A Certificate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_holte_carries_base_semigroup_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_holte_carries_base_semigroup_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_holte_carries_base_semigroup_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_holte_carries_base_semigroup_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Adding $n$ independent base-$b$ digit columns produces a Markov chain on the carry states $\{0,\ldots,n-1\}$. We source-lock Holte's all-parameter transition formula, mixed-radix semigroup $P_aP_b=P_{ab}$, common eigenvectors, simple spectrum $1,b^{-1},\ldots,b^{-(n-1)}$, and Eulerian stationary law. The diagonalization closes every power trace, finite determinant, and an exact common-projector convergence expansion; a sourced total-variation estimate is kept separate from that algebraic deduction. An exact rational census checks 72 matrices through independent algorithms but is only regression evidence. An ownership and control ledger prevents classical results or prime-tagged fixtures from being recast as package novelty. Ordinary positional addition earns a weak arithmetic relation; prime and composite bases obey the same theorem, so no rational-prime orbit semantics, target divisor, or natural target quantization follows.
author:
- 'Route-A structural certificate HCS-C194'
title: |
  The Base Semigroup of Holte's Carries Chain:\
  An Exact Route-A Certificate
```

## Markdown 正文

**Keywords:** carries; positional addition; Markov chain; Eulerian numbers; matrix semigroup; Route A.

# The frozen digit-column dynamics

Fix $n\ge1$ and $b\ge2$. From a carry-in $i\in X_n=\{0,\ldots,n-1\}$, sample $d_1,\ldots,d_n$ independently and uniformly from $\{0,\ldots,b-1\}$. One clock step returns the unique $j$ such that $$jb\le i+d_1+\cdots+d_n<(j+1)b.$$ Introducing the output remainder as a slack digit gives Holte's coefficient formula [@Holte97 Theorem 1] $$\label{eq:transition}
 P_b(i,j)=b^{-n}[x^{(j+1)b-1-i}]
 (1+x+\cdots+x^{b-1})^{n+1}.$$ The chain is irreducible and aperiodic. The case $n=1$ is the one-state identity, retained as the exact boundary.

# Base semigroup and complete spectrum

Write a base-$ab$ digit uniquely as $x+ay$, with $0\le x<a$ and $0\le y<b$. Applying the carry first to the base-$a$ column and then to the base-$b$ column gives the same output as one base-$ab$ column. Therefore $$\label{eq:semigroup}
 P_aP_b=P_{ab},\qquad P_b^r=P_{b^r}.$$ Holte's Theorem 3 gives a matrix $V_n$, independent of $b$, such that $$\label{eq:diagonal}
 V_nP_bV_n^{-1}=\operatorname{diag}
 (1,b^{-1},\ldots,b^{-(n-1)}).$$ The eigenvalues are distinct. The first row of $V_n$ consists of Eulerian numbers, hence the stationary probability is $$\pi_n(j)=\frac{\mathsf A(n,j)}{n!},\qquad0\le j<n.$$ It follows immediately that $$\begin{aligned}
 \operatorname{tr}(P_b^r)&=\sum_{k=0}^{n-1}b^{-rk},\label{eq:trace}\\
 \det(I-zP_b)&=\prod_{k=0}^{n-1}(1-zb^{-k}),\label{eq:det}\\
 \chi_{P_b}(t)&=\prod_{k=0}^{n-1}(t-b^{-k}).\label{eq:char}\end{aligned}$$ These are finite Markov-operator identities, not an Artin--Mazur or target determinant.

# Common projectors and convergence

Let $E_0,\ldots,E_{n-1}$ be the spectral projectors determined by the base-independent matrix $V_n$. They are independent of $b$, and $$\label{eq:projectors}
 P_b^r-E_0=\sum_{k=1}^{n-1}b^{-rk}E_k.$$ Here $E_0$ maps every row distribution to $\pi_n$. Equation [\[eq:projectors\]](#eq:projectors){reference-type="eqref" reference="eq:projectors"} is an exact identity, not merely an asymptotic statement; in every fixed matrix norm it gives geometric convergence governed by $b^{-r}$ unless the $E_1$ component vanishes.

Diaconis and Fulman identify the carries law with a descent marginal of repeated riffle shuffles and analyze convergence [@DF09]. Their Theorem 3.3 supplies, for $n\ge3$, every start $i$, and $r\ge0$, $$\label{eq:tv}
 \lVert P_b^r(i,\cdot)-\pi_n\rVert_{\mathrm{TV}}
 \le \frac{(n-1)/2+i}{b^r}.$$ We attribute this bound rather than presenting it as a package theorem. For $n=1$ the chain is already stationary; $n=2$ follows directly from the two eigenvalues $1,b^{-1}$ and is not folded into the stated $n\ge3$ source locator.

# Exact regression certificate

The producer reconstructs digit-sum coefficients by convolution. A separate checker uses slack-variable inclusion--exclusion, enumerates Eulerian numbers from permutations, and obtains characteristic coefficients through the Faddeev--LeVerrier algorithm. SymPy independently checks matrix polynomials, eigenspace dimensions, stationary equations and traces.

The frozen census contains 72 cases ($1\le n\le8$, $2\le b\le10$), 1,836 transition cells, 392 base-semigroup tuples and 96 power-identity tuples. Bases $2,3,5,7$ contribute 32 prime-tagged cases; $4,6,8,9,10$ contribute 40 composite-tagged controls. Enumeration tests code only: the all-parameter quantifiers belong to Holte's theorem.

The independent checker passes 24,602 assertions, while the separate SymPy oracle passes 14,248 exact checks. Isolated replay reproduces all 537,471 evidence bytes. A hostile suite rejects 159 repaired-hash semantic attacks and one stale-hash attack. These figures are released outputs, not estimates.

# Ownership and control ledger

  --------------------------------------------------------------------------------------------------------------
  Statement                          Owner or derivation                       Release ceiling
  ---------------------------------- ----------------------------------------- ---------------------------------
  transition coefficient             Holte Theorem 1                           no proof by finite census

  common eigenbasis and spectrum     Holte Theorem 3                           no novelty claim

  right eigenvectors                 Holte Theorem 4                           not a package diagonalization

  descent marginal and TV analysis   Diaconis--Fulman Theorems 1.1, 3.1, 3.3   no shuffle theorem is split off

  trace, determinant, projectors     elementary finite-dimensional deduction   no target divisor

  prime/composite cases              exact regression controls                 no prime privilege
  --------------------------------------------------------------------------------------------------------------

  : Classical ownership, package deductions, and claim ceilings.

The stable JSTOR identifier for Holte's paper is [doi:10.2307/2974981](https://doi.org/10.2307/2974981); the publisher DOI used in the registry is printed below. The two-source population, theorem locators, scope literal, and attribution status are exact-matched by the checker. The package claims neither global literature priority nor external peer review.

# Route-A verdict

Positional addition is genuinely arithmetic, but its base-power semigroup is not a rational-prime primitive-orbit repetition law and supplies neither a $\log p$ clock nor arithmetic weights. The frozen object is a stochastic matrix rather than a deterministic primitive-orbit map. Its finite determinant has no target divisor, and a self-adjoint similarity chosen after diagonalization would be noncanonical. Thus $$\begin{aligned}
(A0,A1,A2,A3,A4)=(&\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},
\mathrm{A1\_FAIL},\\
&\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).
\end{aligned}$$ The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. The overall verdict is rejection and Route B is false. No target tables, arithmetic local data, Euler factors, root numbers, automorphy, target functional equation, or Hilbert--Pólya operator is claimed. Nor is the stochastic kernel promoted to an unweighted deterministic primitive-orbit system on a changed phase space.

2 J. M. Holte, Carries, combinatorics, and an amazing matrix, *Amer. Math. Monthly* 104 (1997), 138--149, [doi:10.1080/00029890.1997.11990612](https://doi.org/10.1080/00029890.1997.11990612).

P. Diaconis and J. Fulman, Carries, shuffling, and symmetric functions, *Adv. Appl. Math.* 43 (2009), 176--196, [doi:10.1016/j.aam.2009.02.002](https://doi.org/10.1016/j.aam.2009.02.002).
