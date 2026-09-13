---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-tree-kuramoto-locking-morse-route-a"
canonical_tex: "henon_dynamics/henon_tree_kuramoto_locking_morse_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_tree_kuramoto_locking_morse_route_a/paper/main.pdf"
source_sha256: "2699e783282b04cd2423f4d1f59fee08735f758275bdcf3471bdb89cb5e01f9b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cut-Flow Locking and Edgewise Morse Indices on Kuramoto Trees

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_tree_kuramoto_locking_morse_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_tree_kuramoto_locking_morse_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_tree_kuramoto_locking_morse_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_tree_kuramoto_locking_morse_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For heterogeneous first-harmonic Kuramoto oscillators on any finite positive-weight tree, we classify every phase-locked relative equilibrium. One cut sum per edge gives a necessary-and-sufficient locking test, the exact branch count, and the complete quotient Morse-index distribution. Equality faces are branch mergers with predictable nullity. The result is a source-local mechanics theorem, not a classification of unlocked motion or an arithmetic determinant.
author:
- 'Route-A source-local certificate HCS-C259'
date: 31 August 2026
title: 'Cut-Flow Locking and Edgewise Morse Indices on Kuramoto Trees'
```

## Markdown 正文

trailerid \[\<C2592026083100000000000000000000\>\<C2592026083100000000000000000000\>\]

# Frozen model

Root a connected tree $T=(V,E)$, $V=\{0,\ldots,N-1\}$, at $0$ and orient each edge from parent to child. The incidence column has $-1$ at the parent and $+1$ at the child. For $K=\operatorname{diag}(K_e)$ with $K_e>0$, the model is $$\dot\theta=\omega-BK\sin(B^{\mathsf T}\theta).$$ The sine is componentwise. Put $\Omega=N^{-1}\mathbf 1^{\mathsf T}\omega$, $\eta=\omega-\Omega\mathbf 1$, and $\delta=B^{\mathsf T}\theta$. States differing by a diagonal rotation are identified. Equation (1) is the heterogeneous network form of the Kuramoto phase model [@Kuramoto]; the theorem below is proved directly.

Deleting an edge $e=(p,c)$ leaves a component $S_e$ containing its child. Define the oriented cut demand $$F_e=\sum_{i\in S_e}\eta_i.$$

# Locking and branch theorem

A locked relative equilibrium exists if and only if $$|F_e|\le K_e\quad\hbox{for every }e.$$ Its laboratory-frame frequency is $\Omega$. If all inequalities are strict, there are exactly $2^{N-1}$ locked states modulo diagonal rotation. If exactly $s$ edges are saturated and none is violated, there are exactly $2^{N-1-s}$ states. If any edge violates (3), there is no locked state.

Summing (1) fixes the common frequency as $\Omega$. In the rotating frame a locked state obeys $Bf=\eta$, where $f=K\sin\delta$. The tree incidence matrix has rank $N-1$ and therefore determines $f$ uniquely. Summing $Bf$ over $S_e$ cancels internal columns and leaves $f_e=F_e$, proving (2). Thus each edge reduces to $$K_e\sin\delta_e=F_e.$$ It has two solutions modulo $2\pi$ under strict inequality, one at equality, and none outside. Since a tree has no cycle constraint, arbitrary edge differences reconstruct one phase vector after fixing $\theta_0=0$: for a vertex $v$, sum the signed $\delta_e$ along the unique root-to-$v$ path. This also proves injectivity of the reconstruction modulo diagonal rotation. Multiplication of the independent edge choices gives the stated counts.

Writing $r$ for the number of strict edges, the full branch-generating polynomial is $$\sum_{\text{locked branches}}z^{\#\{e:\cos\delta_e<0\}}
   =(1+z)^r,$$ with $r=N-1$ in a strict chamber and $r=N-1-s$ on a face with $s$ saturated edges. Thus the theorem gives the whole branch distribution, not only its total.

# Morse theorem

On a local lift of the torus, set $$V(\phi)=-\eta^{\mathsf T}\phi-\sum_e K_e
              \cos((B^{\mathsf T}\phi)_e).$$ This is a local lifted potential; the linear term need not define a single-valued global torus potential. Its Hessian at a locked branch is $$H=B\,\operatorname{diag}(K_e\cos\delta_e)B^{\mathsf T}.$$

On the diagonal-rotation quotient, the Morse index of a locked branch equals the number of edges with $\cos\delta_e<0$, and its nullity equals the number of saturated edges. Hence a strict chamber has one and only one linearly asymptotically stable branch modulo rotation; all other strict branches are unstable. Saturated branches are nonhyperbolic.

Let the columns of $Q$ span $\mathbf 1^\perp$ and put $P=B^{\mathsf T}Q$. The square matrix $P$ is invertible because $\ker B^{\mathsf T}=\operatorname{span}\{\mathbf 1\}$. Therefore $$Q^{\mathsf T}HQ=P^{\mathsf T}
 \operatorname{diag}(K_e\cos\delta_e)P.$$ Sylvester's law proves the inertia statement. The rotating-frame linearization is $-H$, so quotient stability holds precisely when all edge cosines are positive.

# Degeneration ledger

At saturation the inverse-sine branches merge and the Hessian gains one null vector per saturated edge; no nonlinear stability conclusion is inferred. For $N=1$ the quotient is a point. If $K_e=0$, a nonzero cut demand forbids locking while zero demand disconnects the phase constraint, changing the positive-weight owner. Cyclic graphs add flow freedom and cycle constraints, so the theorem does not transfer by relabeling. No global classification of unlocked running states is claimed.

  edge condition                 locked branches   quotient Hessian status
  ------------------------------ ----------------- ----------------------------------
  $|F_e|<K_e$ for all $e$        $2^{N-1}$         one stable; binomial index law
  $s$ equalities, no violation   $2^{N-1-s}$       nullity $s$; nonhyperbolic
  some $|F_e|>K_e$               none              no locked Hessian
  $K_e=0$                        changed owner     disconnected constraint possible
  cycle added                    changed owner     flow and phase cycle freedom

# Executable exact audit

The certificate independently enumerates every labeled Prüfer tree for $2\le N\le7$: $18{,}248$ trees in all. It constructs rational cut demands, couplings and centered frequencies, then rederives incidence balance, every subtree cut, the strict/saturated/violated classification, the complete branch histogram and quotient nullity. The deterministic corpus contains $6{,}082$ strict, $6{,}083$ saturated and $6{,}083$ violated instances.

The producer-independent checker closes $477{,}330$ assertions; a separate SymPy computation closes 261 matrix and trigonometric identities; replay is byte-exact; and 34 rehashed hostile semantic mutations are rejected. These finite receipts stress conventions and regression paths. The all-$N$ theorem rests on the cut cancellation, tree reconstruction and congruence proofs above, not on enumeration. Kuramoto's 1975 chapter is cited only for model attribution; no literature-priority claim is made.

# Route A and claim boundary

The arithmetic origin is `none`. The strict evaluator tuple is

(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT).

The verdict and gate are

ROUTE\_A\_REJECTED,route\_b\_invocation\_allowed: false,

under `NO_BAD_EULER_OR_ROOT_NUMBER`. No target divisor, Euler factor, root number, automorphy, functional equation, or Hilbert--Pólya operator is claimed.

9 Y. Kuramoto, "Self-entrainment of a population of coupled non-linear oscillators," in *International Symposium on Mathematical Problems in Theoretical Physics*, Lecture Notes in Physics 39 (1975), 420--422. <https://doi.org/10.1007/BFb0013365>.
