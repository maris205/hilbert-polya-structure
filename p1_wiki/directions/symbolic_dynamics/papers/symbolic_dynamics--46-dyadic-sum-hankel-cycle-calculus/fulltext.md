---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--46-dyadic-sum-hankel-cycle-calculus"
canonical_tex: "symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus/main.tex"
canonical_pdf: "symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus/main.pdf"
source_sha256: "4cb7d1a0af05ac70ea27d6e49ee001cf763c254eaafc453e8371f96967512a28"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dyadic-Sum Weighted Hankel Operators: Sharp Ideal Thresholds, 2-Adic Blocks, and Labeled Cycle Equations

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/46-dyadic-sum-hankel-cycle-calculus/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the Dirichlet-weighted adjacency matrix supported on the dyadic anti-diagonals $m+n=2^a$ of the positive-integer lattice. For $s\in\mathbb C$ and $\sigma=\Re s$, its matrix coefficients admit a bounded operator realization on $\ell^2(\mathbb N)$ exactly when $\sigma>0$; throughout that half-plane the operator is compact. We prove the sharp ideal walls $H_s\in\mathcal S_{2}$ exactly for $\sigma>1/2$ and $H_s\in\mathcal S_{1}$ exactly for $\sigma>1$. The arithmetic support also forces every edge to preserve the $2$-adic valuation. Consequently, in the bounded region, $H_s$ is the orthogonal direct sum of the scaled blocks $2^{-ks}A_s$, where $A_s$ is the odd-vertex compression. This gives exact trace-power factors and a locally uniformly convergent block product for the Hilbert--Carleman determinant in the Hilbert--Schmidt half-plane. Separately, we solve every cyclic system $n_i+n_{i+1}=2^{a_i}$ with fixed ordered labels: odd length has one candidate, whereas even length has an alternating compatibility condition followed by an explicit integer positivity interval. A canonical finite replay compared two independent implementations on four support cutoffs, $335{,}922$ ordered label tuples, and $36$ exact rational trace cases, with zero mismatches. These finite checks test implementation fidelity; every infinite statement and endpoint is established analytically.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  Dyadic-Sum Weighted Hankel Operators:\
  Sharp Ideal Thresholds, 2-Adic Blocks, and Labeled Cycle Equations
```

## Markdown 正文

# Introduction {#sec:introduction}

Arithmetic sparsity can make an infinite matrix simultaneously tractable and deceptive. In the matrix studied here, an entry is present only when its two indices sum to a power of two, but every present entry is weighted by both indices. The support is lacunary, the weights are not translation invariant, and the three basic operator-ideal questions have three different sharp answers.

For $s\in\mathbb C$, write $\sigma=\Re s$ and consider the coefficient array $$h_s(m,n)=\mathbf 1_{\{m+n=2^a\text{ for some }a\ge1\}}
  (mn)^{-s/2},\qquad m,n\in\mathbb N,
  \label{eq:intro-matrix}$$ where powers use the real logarithm and loops are retained. We prove that these coefficients define a bounded operator $H_s$ on $\ell^2(\mathbb N)$ exactly for $\sigma>0$, and that the resulting operator is then compact. Its Hilbert--Schmidt and trace-class walls are, sharply, $$H_s\in\mathcal S_{2}\iff\sigma>\frac12,
  \qquad
  H_s\in\mathcal S_{1}\iff\sigma>1.
  \label{eq:intro-walls}$$ The endpoints are not consequences of a common interpolation argument. The wall at zero is detected by one infinite row, the Hilbert--Schmidt wall by central mass on each dyadic anti-diagonal, and the trace-class wall by pairwise disjoint trace-dual matchings.

The same support has an exact arithmetic symmetry. Every legal edge preserves the $2$-adic valuation, so in the bounded half-plane the operator is an orthogonal direct sum of scaled copies of its odd-vertex block. This identity yields trace-power factors and, in the Hilbert--Schmidt domain, a locally uniformly convergent block product for the Hilbert--Carleman determinant. It also explains why the marker for walk length and the $2$-adic scale weight must remain different variables.

Our third component is algebraic rather than asymptotic. Given fixed ordered dyadic labels $q_i$, the equations $n_i+n_{i+1}=q_i$ around a cycle reduce to an alternating recurrence. Odd length fixes one candidate vertex word. Even length imposes one alternating compatibility equation and leaves an explicit finite interval for $n_1$. This solver classifies based positive vertex solutions for the fixed ordered label tuple; it does not by itself quotient cyclic rotations or identify primitive orbits.

The contributions are therefore three precise statements.

1.  We establish the sharp bounded/compact, Hilbert--Schmidt, and trace-class walls $0$, $1/2$, and $1$, including analytic endpoint obstructions.

2.  We prove the exact bounded-operator decomposition $H_s\simeq\bigoplus_{k\ge0}2^{-ks}A_s$, derive its legal trace formulas, and give a self-contained proof of the regularized-determinant block product.

3.  We give the complete odd/even solver for fixed ordered dyadic cycle labels and compare an algebraic implementation with a direct finite walk enumerator.

The computational comparison is deliberately narrower than the theorem. The exact finite replays agree without a mismatch on the declared grid; the complete counts are reported once in [3](#tab:canonical-replay-main){reference-type="ref" reference="tab:canonical-replay-main"}. This agreement establishes implementation fidelity, not an infinite endpoint, external novelty, or a priority claim.

positions the result. fixes the source, types, and complex-parameter convention. prove the three walls. develops valuation blocks, traces, and determinants, while [7](#sec:cycles){reference-type="ref" reference="sec:cycles"} solves the labeled cyclic systems. reports the finite replay and closes with limitations.

# Related work and ownership boundaries {#sec:related}

#### Hankel operators and Schatten ideals.

Classical Hankel operator theory relates ideal membership to analytic regularity and approximation properties; Peller's characterization and monograph provide the standard setting and terminology [@peller1985description; @peller2003hankel]. The matrix in [\[eq:intro-matrix\]](#eq:intro-matrix){reference-type="ref" reference="eq:intro-matrix"} has Hankel *support*, but for $s\ne0$ its values are not a function of $m+n$ alone: the left and right Dirichlet factors weight the two indices separately. Thus "weighted Hankel" in the title means a two-sided diagonal weighting of a Hankel-supported matrix, not a classical matrix with entries $a_{m+n}$. We use standard ideal facts, such as Hölder multiplication for Schatten classes, but prove the three thresholds directly from this particular coefficient array.

#### Lacunary support and Schur estimates.

Fournier and Wagner develop Schur-test proofs in a lacunary Hankel setting and analyze reflection, folding, and alternating representations [@fournier2015paley]. Those tools motivate the broader lacunary context. Our row estimate is reproduced in full because its two-sided Dirichlet weight is specific to [\[eq:intro-matrix\]](#eq:intro-matrix){reference-type="ref" reference="eq:intro-matrix"}; the generic Schur machinery remains attributed to that work.

#### Finite powers-of-two problems.

Two nearby finite objects must be kept separate from the present infinite operator. Guo studies regularity of finite Hankel determinants formed from the characteristic sequence of the powers of two [@guo2019regularity]. Alekseyev studies finite distinct-integer graph labelings whose endpoint sums are powers of two, together with associated restricted systems of linear equations and inequations [@alekseyev2026maximizing]. Neither object is the Dirichlet-weighted operator on $\ell^2(\mathbb N)$, and neither supplies its Schatten thresholds or determinant identities. Conversely, our cyclic solver fixes an ordered label tuple and allows repeated vertices and labels; it is not a solution of the finite distinct-label optimization problem.

#### Determinants.

We use the Hilbert--Carleman determinant for Hilbert--Schmidt operators and the ordinary Fredholm determinant for trace-class operators; Simon gives the general trace-ideal framework [@simon2005trace]. The direct-sum identity needed below is proved inside the paper by combining the block eigenvalues and controlling the canonical factors. Thus the reference supplies definitions and background, not a page-level substitute for the specialized convergence argument.

A bounded search over these families did not locate the exact combined package of the three sharp walls, the valuation direct sum, and the ordered odd/even closure theorem. Together with the distinctions above, this records our claim and source boundary; it is not evidence that the package is first or unique.

# The dyadic-sum source and its weighted operator {#sec:source}

Let $G_2$ be the undirected looped graph with vertex set $\mathbb N$ and $$m\sim n \quad\Longleftrightarrow\quad
  m+n=2^a\text{ for some integer }a\ge1.
  \label{eq:edge-relation}$$ Its one-sided edge shift consists of sequences $(n_j)_{j\ge0}$ satisfying $n_j\sim n_{j+1}$. One edge is one unit of time, and the formal marker $z$ records that time. A primitive orbit, when needed, is a cyclic vertex word of least shift period, modulo rotation. Dyadic edge labels are constraints derived from a vertex word; they are not the primitive objects.

For $s\in\mathbb C$, define the coefficient array $h_s$ by [\[eq:intro-matrix\]](#eq:intro-matrix){reference-type="ref" reference="eq:intro-matrix"}, with $n^{-s/2}=\exp[-(s/2)\log n]$ and the real logarithm. We say that $h_s$ has a *bounded realization* if there is $H_s\in\mathcal B(\ell^2(\mathbb N))$ with matrix coefficients $\langle H_se_n,e_m\rangle=h_s(m,n)$. This formulation matters when $\sigma\le0$: a column then need not lie in $\ell^2$, so we do not silently introduce an unbounded operator on finitely supported vectors. On odd vertices, $A_s$ denotes the corresponding compression whenever the bounded realization exists.

::: {#tab:typed-objects}
  Object               Mathematical type                        Not identified with
  -------------------- ---------------------------------------- -------------------------------
  $n$                  positive-integer vertex                  rational-prime primitive
  $q_i=2^{a_i}$        derived edge label                       temporal orbit
  $(n_1,\ldots,n_r)$   based closed vertex walk                 unordered labels
  $z$                  one-edge time marker                     valuation weight
  $2^{-krs}$           $r$-step block weight                    time marker
  $H_s$                bounded weighted adjacency, when legal   nonreal self-adjoint operator

  : The typed objects used in the operator and walk ledgers.
:::

[\[lem:phase\]]{#lem:phase label="lem:phase"} Let $s=\sigma+it$, let $U_t e_n=n^{-it/2}e_n$, and write $H_s^{(N)}=(h_s(m,n))_{1\le m,n\le N}$ and $U_t^{(N)}=\mathop{\mathrm{diag}}(n^{-it/2})_{1\le n\le N}$. Entrywise, and hence for every finite matrix, $$H_s^{(N)}=U_t^{(N)}H_\sigma^{(N)}U_t^{(N)}.
  \label{eq:finite-phase}$$ If the coefficient arrays have bounded realizations, then $H_s=U_tH_\sigma U_t$. Consequently boundedness, compactness, singular values, Schatten membership, and the corresponding norms depend only on $\sigma$.

The $(m,n)$ coefficient on the right of [\[eq:finite-phase\]](#eq:finite-phase){reference-type="ref" reference="eq:finite-phase"} is $m^{-it/2}h_\sigma(m,n)n^{-it/2}=h_s(m,n)$. Each finite compression is an ordinary matrix identity. If $H_\sigma$ is bounded, the same calculation gives the full bounded identity. Conversely, $U_t^*H_sU_t^*$ is a bounded operator with coefficients $h_\sigma$. Left and right multiplication by unitaries preserves singular values and all properties listed above.

The factorization is not a unitary conjugacy: the two copies of $U_t$ point in the same direction. It therefore transfers neither spectra nor powers, traces, or determinants. All such identities below retain the complex parameter and come instead from an actual basis-reordering direct sum.

The loop locations and valuation constraint are elementary but structural. There is a loop at $m$ precisely when $2m=2^a$, hence precisely at $m=2^k$, $k\ge0$.

[\[lem:valuation\]]{#lem:valuation label="lem:valuation"} If $m+n=2^a$ with $m,n\in\mathbb N$, then $\mathop{\mathrm{v_2}}(m)=\mathop{\mathrm{v_2}}(n)$. If this common value is $k$ and $m=2^ku$, $n=2^kv$, then $u,v$ are odd and $u+v=2^{a-k}$.

If the two valuations differed, the valuation of their sum would equal the smaller one. Because $m,n<2^a$, that value is strictly smaller than $a$, contradicting $\mathop{\mathrm{v_2}}(m+n)=a$. Dividing the equality by $2^k$ gives the second statement.

# The boundedness and compactness wall {#sec:bounded}

The absolute row sums simultaneously give a Schur bound and a compactness criterion. For $\sigma>0$, let $$R_m=\sum_{n\ge1}\lvert h_s(m,n)\rvert.
  \label{eq:row-sum}$$ Let $A=A(m)$ be the least integer for which $2^A>m$. The neighbors of $m$ are exactly $n_j=2^{A+j}-m$, $j\ge0$. The first neighbor is a positive integer, while for $j\ge1$, $n_j\ge2^{A+j-1}$. Consequently the row sum satisfies $$\begin{aligned}
 R_m
 &=m^{-\sigma/2}\sum_{j\ge0}(2^{A+j}-m)^{-\sigma/2} \notag\\
 &\le m^{-\sigma/2}
   +\frac{m^{-\sigma/2}2^{-A\sigma/2}}
          {1-2^{-\sigma/2}}
 \le m^{-\sigma/2}+C_\sigma m^{-\sigma}.
 \label{eq:row-decay}\end{aligned}$$ In particular, $\sup_mR_m<\infty$ and $R_m\to0$.

[\[thm:bounded\]]{#thm:bounded label="thm:bounded"} The coefficient array $h_s$ admits a bounded operator realization on $\ell^2(\mathbb N)$ if and only if $\sigma>0$. Whenever it does, the realization $H_s$ is compact.

For $\sigma>0$, the modulus array is symmetric, so the Schur test and [\[eq:row-decay\]](#eq:row-decay){reference-type="ref" reference="eq:row-decay"} give a bounded realization. To prove compactness, fix $\varepsilon>0$. Choose $M$ so that $R_m<\varepsilon$ for $m>M$. Each of the finitely many rows $m\le M$ is absolutely summable, so some $N\ge M$ satisfies $$\sum_{n>N}\lvert h_s(m,n)\rvert<\varepsilon,
  \qquad 1\le m\le M.$$ Every absolute row sum of $H_s-P_NH_sP_N$ is then below $\varepsilon$: for $m\le M$ it is the selected row tail, and for $m>M$ it is at most $R_m$. The same holds for columns by symmetry of the modulus array. A second Schur estimate yields $\lVert H_s-P_NH_sP_N\rVert\le\varepsilon$. Hence finite-rank compressions converge in norm.

Suppose now that $\sigma\le0$ and that a bounded operator had the declared matrix coefficients. In its row indexed by $1$, the entries at $n=2^a-1$, $a\ge1$, have squared moduli $(2^a-1)^{-\sigma}$. Therefore $$\sum_{a\ge1}\lvert h_s(1,2^a-1)\rvert^2
  =\sum_{a\ge1}(2^a-1)^{-\sigma}=\infty.
  \label{eq:row-one-obstruction}$$ But a row of a bounded operator is the coordinate sequence of its adjoint applied to a basis vector and must lie in $\ell^2$. This contradiction excludes every bounded realization on $\sigma\le0$.

The proof is genuinely infinite at the boundary: no finite singular-value calculation can witness the divergent row in [\[eq:row-one-obstruction\]](#eq:row-one-obstruction){reference-type="ref" reference="eq:row-one-obstruction"}.

# Sharp Hilbert--Schmidt and trace-class thresholds {#sec:ideals}

Distinct dyadic anti-diagonals have disjoint support. Hence, whenever the sum is finite, $$\lVert H_s\rVert_2^2
  =\sum_{a\ge1}\sum_{m=1}^{2^a-1}
     [m(2^a-m)]^{-\sigma}.
  \label{eq:hs-levels}$$ The following elementary level estimates contain the entire Hilbert--Schmidt threshold. Their detailed constants are recorded in [9](#app:endpoints){reference-type="ref" reference="app:endpoints"}.

[\[lem:level-estimates\]]{#lem:level-estimates label="lem:level-estimates"} For $N=2^a$:

1.  if $0<\alpha<1$, then $$\sum_{m=1}^{N-1}[m(N-m)]^{-\alpha}
        \asymp_\alpha N^{1-2\alpha};$$

2.  if $\alpha=1$, then the sum is $2H_{N-1}/N$;

3.  if $\alpha>1$, then the sum is $O_\alpha(N^{-\alpha})$.

By symmetry it suffices to sum over $m\le N/2$. There, $N/2\le N-m<N$, so the level is comparable to $N^{-\alpha}\sum_{m\le N/2}m^{-\alpha}$. This is $N^{1-2\alpha}$ for $\alpha<1$ and $O(N^{-\alpha})$ for $\alpha>1$. At $\alpha=1$, the partial-fraction identity $$\frac1{m(N-m)}=\frac1N(\frac1m+\frac1{N-m})$$ gives the exact formula.

[\[thm:hs\]]{#thm:hs label="thm:hs"} The bounded realization $H_s$ belongs to $\mathcal S_{2}$ if and only if $\sigma>1/2$.

For $0<\sigma<1$, applying the first part of [\[lem:level-estimates\]](#lem:level-estimates){reference-type="ref" reference="lem:level-estimates"} to [\[eq:hs-levels\]](#eq:hs-levels){reference-type="ref" reference="eq:hs-levels"} gives a dyadic outer series comparable to $\sum_a2^{a(1-2\sigma)}$, which converges exactly when $\sigma>1/2$. In particular, the level mass stays bounded below at $\sigma=1/2$. At $\sigma=1$, the exact harmonic formula is $2H_{2^a-1}/2^a$, which is summable in $a$. For $\sigma>1$, the third part gives an $O(2^{-a\sigma})$ level bound. Finally, [\[thm:bounded\]](#thm:bounded){reference-type="ref" reference="thm:bounded"} already excludes $\sigma\le0$.

Trace class needs a different endpoint witness. Sufficiency follows from entrywise summability: $$\sum_{m,n\ge1}\lvert h_s(m,n)\rvert
  =\sum_{a\ge1}\sum_{m=1}^{2^a-1}
    [m(2^a-m)]^{-\sigma/2}.
  \label{eq:entrywise-sum}$$ For $1<\sigma<2$, the $a$th level is $O(2^{a(1-\sigma)})$; for $\sigma=2$ it is $2H_{2^a-1}/2^a=O(a2^{-a})$; and for $\sigma>2$ it is $O(2^{-a\sigma/2})$. These level bounds make [\[eq:entrywise-sum\]](#eq:entrywise-sum){reference-type="ref" reference="eq:entrywise-sum"} finite whenever $\sigma>1$. Expanding the matrix into rank-one coordinate operators then converges absolutely in trace norm.

For necessity, set $Q_j=4^j$ and $$I_j=\mathbb Z\cap[Q_j/4,Q_j/3],
  \qquad
  J_j=\{Q_j-m:m\in I_j\}.
  \label{eq:matching-sets}$$ All sets $I_j$ and $J_j$ are pairwise disjoint. For a finite upper index $J$, define a partial isometry $V_J$ by $$V_J e_{Q_j-m}
  =\frac{h_s(m,Q_j-m)}{\lvert h_s(m,Q_j-m)\rvert}e_m,
  \qquad m\in I_j,\quad j\le J,$$ and let it vanish on the orthogonal complement. Its selected domain and range vectors are orthonormal, so $\lVert V_J\rVert=1$. Direct matrix multiplication gives $$\mathop{\mathrm{Tr}}(V_J^*H_s)
  =\sum_{j\le J}\sum_{m\in I_j}
    [m(Q_j-m)]^{-\sigma/2}.
  \label{eq:trace-dual-pairing}$$ Each inner sum is comparable to $Q_j^{1-\sigma}$: it contains a fixed positive proportion of $Q_j$ indices, and both factors are comparable to $Q_j$. If $H_s$ were trace class for $\sigma\le1$, standard trace duality [@simon2005trace] would bound [\[eq:trace-dual-pairing\]](#eq:trace-dual-pairing){reference-type="ref" reference="eq:trace-dual-pairing"} by $\lVert H_s\rVert_1$ uniformly in $J$, whereas its right-hand side diverges.

[\[thm:trace-class\]]{#thm:trace-class label="thm:trace-class"} The bounded realization $H_s$ belongs to $\mathcal S_{1}$ if and only if $\sigma>1$.

Entrywise summability proves sufficiency. The disjoint matching argument proves necessity for $0<\sigma\le1$, including the endpoint; for $\sigma\le0$ there is no bounded realization by [\[thm:bounded\]](#thm:bounded){reference-type="ref" reference="thm:bounded"}.

::: {#tab:phase-domains-main}
  Property              Exact domain        Boundary obstruction
  --------------------- ------------------- -------------------------------
  Bounded and compact   $\sigma>0$          row $m=1$ is not in $\ell^2$
  Hilbert--Schmidt      $\sigma>\tfrac12$   central anti-diagonal mass
  Trace class           $\sigma>1$          disjoint trace-dual matchings
  $\det_2(I-zH_s)$      $\sigma>\tfrac12$   requires $H_s\in\mathcal S_2$
  $\det(I-zH_s)$        $\sigma>1$          requires $H_s\in\mathcal S_1$

  : Exact operator-ideal and determinant domains. Every endpoint is rejected analytically rather than by finite-cutoff extrapolation.
:::

# Valuation blocks, trace powers, and legal determinants {#sec:blocks}

For $k\ge0$, let $$\mathcal H_k
  =\overline{\operatorname{span}}\{e_{2^ku}:u\in\mathbb N_{\mathrm{odd}}\}.$$ These spaces are mutually orthogonal and exhaust $\ell^2(\mathbb N)$. Let $W_k:\ell^2(\mathbb N_{\mathrm{odd}})\to\mathcal H_k$ send $e_u$ to $e_{2^ku}$. Define $$\mathcal K:=\bigoplus_{k\ge0}\ell^2(\mathbb N_{\mathrm{odd}}),
  \qquad
  W:\mathcal K\longrightarrow\ell^2(\mathbb N),
  \qquad
  W((x_k)_{k\ge0})=\sum_{k\ge0}W_kx_k.$$ Orthogonality of the $\mathcal H_k$ makes $W$ a unitary. Every block direct sum below is an operator on the explicitly named source space $\mathcal K$.

[\[thm:direct-sum\]]{#thm:direct-sum label="thm:direct-sum"} If $\sigma>0$, then, as bounded operators, $$W^*H_sW=\bigoplus_{k\ge0}2^{-ks}A_s.
  \label{eq:direct-sum}$$ No unbounded-operator equivalence is asserted for $\sigma\le0$.

makes all off-diagonal blocks between distinct $\mathcal H_k$ vanish. If $m=2^ku$ and $n=2^kv$ with $u,v$ odd, then $$h_s(m,n)
  =2^{-ks}\mathbf 1_{\{u+v=2^b\text{ for some }b\ge1\}}(uv)^{-s/2}.$$ Thus the $k$th diagonal block is exactly $2^{-ks}A_s$. Boundedness on $\sigma>0$ is supplied by [\[thm:bounded\]](#thm:bounded){reference-type="ref" reference="thm:bounded"}, so the block identity is an identity of bounded operators.

The direct sum now carries operator algebra, unlike the left--right phase factorization in [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"}. In the Hilbert--Schmidt half-plane, $H_s^2$ and $A_s^2$ are trace class by Schatten Hölder, and multiplication by bounded powers handles every $r\ge2$.

[\[prop:trace-powers\]]{#prop:trace-powers label="prop:trace-powers"} If $\sigma>1/2$ and $r\ge2$, then $$\mathop{\mathrm{Tr}}(H_s^r)
  =\frac{\mathop{\mathrm{Tr}}(A_s^r)}{1-2^{-rs}}.
  \label{eq:trace-factor}$$ If $\sigma>1$, then $$\mathop{\mathrm{Tr}}(H_s)=\sum_{k\ge0}2^{-ks}
  =\frac1{1-2^{-s}}.
  \label{eq:ordinary-trace}$$

Taking the $r$th power of [\[eq:direct-sum\]](#eq:direct-sum){reference-type="ref" reference="eq:direct-sum"} gives blocks $2^{-krs}A_s^r$. Because the full power is trace class, its trace is the absolutely convergent sum of the block traces. The scalar geometric series converges since $r\sigma>1$, proving [\[eq:trace-factor\]](#eq:trace-factor){reference-type="ref" reference="eq:trace-factor"}. In the trace-class domain, the trace is the absolutely convergent diagonal sum. Loops occur exactly at $2^k$, and the diagonal entry there is $2^{-ks}$, which gives [\[eq:ordinary-trace\]](#eq:ordinary-trace){reference-type="ref" reference="eq:ordinary-trace"}.

We next separate an entire determinant identity from its local logarithm. For a Hilbert--Schmidt operator $T$, write $$E_2(w)=(1-w)e^w,\qquad
  \det_2(I-zT)=\prod_j E_2(z\lambda_j(T)),$$ where eigenvalues are repeated with algebraic multiplicity. This is the standard Hilbert--Carleman determinant convention [@simon2005trace].

[\[prop:det2-product\]]{#prop:det2-product label="prop:det2-product"} If $\sigma>1/2$, then $$\det_2(I-zH_s)
  =\prod_{k\ge0}\det_2(I-z2^{-ks}A_s),
  \label{eq:det2-product}$$ and the product converges uniformly on every compact subset of $\mathbb C$.

Set $T_k=2^{-ks}A_s$ on the $k$th summand of $\mathcal K$. Each $T_k$ is Hilbert--Schmidt, and $$\sum_{k\ge0}\lVert T_k\rVert_2^2
  =\lVert A_s\rVert_2^2\sum_{k\ge0}2^{-2k\sigma}<\infty.$$ By [\[thm:direct-sum\]](#thm:direct-sum){reference-type="ref" reference="thm:direct-sum"}, $\bigoplus_kT_k=W^*H_sW$. Applying the square-summable direct-sum theorem [\[lem:abstract-det2-sum\]](#lem:abstract-det2-sum){reference-type="ref" reference="lem:abstract-det2-sum"} therefore gives [\[eq:det2-product\]](#eq:det2-product){reference-type="ref" reference="eq:det2-product"} and compact-uniform convergence. That lemma also supplies the complete nonnormal combined-eigenvalue argument, including the finite exceptional factors and canonical-product tail control.

Both sides of [\[eq:det2-product\]](#eq:det2-product){reference-type="ref" reference="eq:det2-product"} are entire in $z$. On the smaller zero-free disk $\lvert z\rvert\lVert H_s\rVert<1$, choose the logarithm branch normalized by $\log\det_2(I)=0$. Then $$\log\det_2(I-zH_s)
  =-\sum_{r\ge2}\frac{z^r}{r}
      \frac{\mathop{\mathrm{Tr}}(A_s^r)}{1-2^{-rs}}.
  \label{eq:local-log-det2}$$ This logarithmic series is local; it is not a global logarithm of the entire function in [\[eq:det2-product\]](#eq:det2-product){reference-type="ref" reference="eq:det2-product"}.

In the overlap $\sigma>1$, $H_s$ and $A_s$ are trace class. Let $D_K=\bigoplus_{k=0}^K2^{-ks}A_s$. Then $$\lVert W^*H_sW-D_K\rVert_1
  =\lVert A_s\rVert_1\sum_{k>K}2^{-k\sigma}\longrightarrow0.$$ For finite $K$, the Fredholm determinant of $I-zD_K$ is the product of the block determinants. Continuity of the determinant in trace norm, uniformly for $z$ in a compact set, permits $K\to\infty$ and gives $$\det(I-zH_s)
  =\prod_{k\ge0}\det(I-z2^{-ks}A_s)
  \label{eq:det-product}$$ locally uniformly in $z$. The two determinant conventions agree through $$\det_2(I-zH_s)
  =\det(I-zH_s)\exp\!(\frac{z}{1-2^{-s}}).
  \label{eq:det-overlap}$$ No ordinary determinant is used on $1/2<\sigma\le1$, and no infinite determinant is defined outside its corresponding ideal domain.

# Complete labeled cyclic closure {#sec:cycles}

Fix a length $r\ge1$ and an ordered tuple of dyadic labels $q_i=2^{a_i}\ge2$. We seek positive integers $n_1,\ldots,n_r$, with $n_{r+1}=n_1$, satisfying $$n_i+n_{i+1}=q_i,\qquad 1\le i\le r.
  \label{eq:cycle-system}$$ The length range here includes $r=1$ because the graph retains loops. By contrast, traces in the Hilbert--Schmidt-only domain use $r\ge2$.

Iterating $n_{i+1}=q_i-n_i$ gives, for $2\le i\le r+1$, $$n_i=(-1)^{i-1}n_1+
      \sum_{j=1}^{i-1}(-1)^{i-1-j}q_j.
  \label{eq:cycle-recurrence}$$ Closing at $i=r+1$ yields the single equation $$(1-(-1)^r)n_1
  =\sum_{j=1}^r(-1)^{r-j}q_j.
  \label{eq:cycle-closing}$$

[\[thm:cycle-solver\]]{#thm:cycle-solver label="thm:cycle-solver"} For the ordered system [\[eq:cycle-system\]](#eq:cycle-system){reference-type="ref" reference="eq:cycle-system"}:

1.  If $r$ is odd, there is one algebraic candidate, $$n_1=\frac12(q_1-q_2+q_3-\cdots+q_r).
        \label{eq:odd-candidate}$$ It is a positive solution exactly when every vertex obtained from [\[eq:cycle-recurrence\]](#eq:cycle-recurrence){reference-type="ref" reference="eq:cycle-recurrence"} is positive.

2.  If $r$ is even, a solution exists only if $$q_1-q_2+q_3-\cdots-q_r=0.
        \label{eq:even-compatibility}$$ Under this condition, set $$b_1=0,\qquad
        b_i=\sum_{j=1}^{i-1}(-1)^{i-1-j}q_j\quad(2\le i\le r),
        \label{eq:bi-definition}$$ and $$L(q)=\max_{\substack{1\le i\le r\\i\ {\rm odd}}}(-b_i),
        \qquad
        U(q)=\min_{\substack{1\le i\le r\\i\ {\rm even}}}b_i.
        \label{eq:LU-definition}$$ The positive solutions are exactly $$n_1=x\in\mathbb Z\cap(L(q),U(q)),\qquad
        n_i=(-1)^{i-1}x+b_i.
        \label{eq:even-solutions}$$ Thus their number is $\max\{0,U(q)-L(q)-1\}$.

In the odd block $A_s$, retain precisely those solutions for which $n_1$ is odd.

follow by induction. If $r$ is odd, the coefficient on the left of [\[eq:cycle-closing\]](#eq:cycle-closing){reference-type="ref" reference="eq:cycle-closing"} is $2$, which gives [\[eq:odd-candidate\]](#eq:odd-candidate){reference-type="ref" reference="eq:odd-candidate"}; it is integral because every $q_i$ is even. The recurrence fixes every remaining vertex, so positivity is the only condition left.

If $r$ is even, the left side of [\[eq:cycle-closing\]](#eq:cycle-closing){reference-type="ref" reference="eq:cycle-closing"} vanishes, and its right side vanishes exactly under [\[eq:even-compatibility\]](#eq:even-compatibility){reference-type="ref" reference="eq:even-compatibility"}. Write $x=n_1$. Formula [\[eq:cycle-recurrence\]](#eq:cycle-recurrence){reference-type="ref" reference="eq:cycle-recurrence"} becomes $n_i=(-1)^{i-1}x+b_i$. For odd $i$, positivity says $x>-b_i$; for even $i$, it says $x<b_i$. Their intersection is exactly $\mathbb Z\cap(L(q),U(q))$. The endpoints are integers, giving the stated count. Finally, subtracting a vertex from the even integer $q_i$ preserves parity along every edge. Hence all vertices are odd exactly when $n_1$ is odd.

The frozen examples illustrate all branches. Labels $(2,4,4)$ give the unique odd-length solution $(1,1,3)$. Labels $(4,8,8,4)$ satisfy [\[eq:even-compatibility\]](#eq:even-compatibility){reference-type="ref" reference="eq:even-compatibility"}; here $$(n_1,n_2,n_3,n_4)=(x,4-x,4+x,4-x),$$ so positivity gives $x\in\{1,2,3\}$, with $x=1,3$ in the odd block. Labels $(4,4,8,4)$ have nonzero alternating sum and no solution.

The passage from matrices to an absolutely convergent infinite walk sum uses the following ideal estimate.

[\[lem:compression-powers\]]{#lem:compression-powers label="lem:compression-powers"} Let $T\in\mathcal S_{2}$, let $P_N$ be the coordinate projection onto the first $N$ basis vectors, and set $T_N=P_NTP_N$. Then $\lVert T_N-T\rVert_2\to0$ and, for every integer $r\ge2$, $$\lVert T_N^r-T^r\rVert_1\longrightarrow0.
  \label{eq:compression-power-convergence}$$

The Hilbert--Schmidt convergence follows first for finite-rank operators and then for $T$ by finite-rank density, because left and right multiplication by an orthogonal projection are contractions in $\mathcal S_{2}$. Put $\delta_N=\lVert T_N-T\rVert_2$. Schatten Hölder gives the explicit square estimate $$\lVert T_N^2-T^2\rVert_1
  \le \delta_N(\lVert T_N\rVert_2+\lVert T\rVert_2)
  \longrightarrow0.
  \label{eq:compression-square-estimate}$$ For $r>2$, the exact identity $$T_N^r-T^r
  =(T_N^2-T^2)T_N^{r-2}
   +T^2(T_N^{r-2}-T^{r-2})$$ and the ideal inequality yield $$\lVert T_N^r-T^r\rVert_1
  \le \lVert T_N^2-T^2\rVert_1\lVert T_N\rVert^{r-2}
   +\lVert T^2\rVert_1\lVert T_N^{r-2}-T^{r-2}\rVert.$$ Here $\lVert T_N\rVert\le\lVert T\rVert$ and $\lVert T_N-T\rVert\le\delta_N$; the usual telescoping formula for bounded powers therefore makes the last factor tend to zero. This proves [\[eq:compression-power-convergence\]](#eq:compression-power-convergence){reference-type="ref" reference="eq:compression-power-convergence"}.

When $\sigma>1/2$ and $r\ge2$, the trace admits a closed-walk interpretation. The product of edge weights around a based closed walk is $$\prod_{i=1}^r h_s(n_i,n_{i+1})
  =\prod_{i=1}^r n_i^{-s}.
  \label{eq:walk-weight}$$ Indeed, apply [\[lem:compression-powers\]](#lem:compression-powers){reference-type="ref" reference="lem:compression-powers"} first to $H_\sigma$. For every $N$, expansion of the finite matrix trace gives $$\mathop{\mathrm{Tr}}\!\left((P_NH_\sigma P_N)^r\right)
  =\sum_{1\le n_1,\ldots,n_r\le N}
    \prod_{i=1}^r h_\sigma(n_i,n_{i+1}),
  \qquad n_{r+1}=n_1.$$ Every summand is nonnegative. These finite sums increase with $N$ and, by [\[eq:compression-power-convergence\]](#eq:compression-power-convergence){reference-type="ref" reference="eq:compression-power-convergence"}, converge to the finite value $\mathop{\mathrm{Tr}}(H_\sigma^r)$. Moreover, $$\left|\prod_{i=1}^r h_s(n_i,n_{i+1})\right|
  =\prod_{i=1}^r h_\sigma(n_i,n_{i+1}),$$ so the complex closed-walk series is absolutely convergent by comparison. A second application of the lemma to $H_s$ identifies its sum with $\mathop{\mathrm{Tr}}(H_s^r)$. Consequently the solver is a matrix-independent trace evaluator: enumerate an ordered label tuple, solve it using [\[thm:cycle-solver\]](#thm:cycle-solver){reference-type="ref" reference="thm:cycle-solver"}, and add [\[eq:walk-weight\]](#eq:walk-weight){reference-type="ref" reference="eq:walk-weight"} for the accepted based vertex words. Primitive-period reduction and quotienting by cyclic base point are separate operations, as detailed in [11](#app:cycles){reference-type="ref" reference="app:cycles"}.

# Independent replay, limitations, and conclusion {#sec:replay}

## Canonical finite replay {#sec:canonical-replay}

The replay compares two structurally independent finite representations. Evaluator M constructs cutoff matrices from the bit predicate and uses matrix operations; Evaluator C constructs dyadic anti-diagonals, partitions them by valuation, and applies [\[thm:cycle-solver\]](#thm:cycle-solver){reference-type="ref" reference="thm:cycle-solver"} without constructing Evaluator M's matrix.

::: {#tab:canonical-replay-main}
  Replay surface                     Cases   Mismatches
  ------------------------------ --------- ------------
  Complete support cutoffs               4            0
  Ordered dyadic label tuples      335,922            0
  Exact rational finite traces          36            0

  : Canonical State-A implementation replay. These finite exact comparisons test two independent implementations; they do not prove an infinite theorem or a priority claim.
:::

The table covers complete cutoffs $N=8,16,32,64$, every ordered label tuple in the declared grid, and $36$ exact rational traces. All comparisons use strict recursive type-and-value equality. Finite traces retain their scale-dependent odd-block cutoffs and endpoint partial sums remain finite diagnostics. Thus the replay tests implementation fidelity only; the infinite statements are proved analytically. Exact truncation, hash, integrity, and adversarial metadata are recorded in [12](#app:evidence){reference-type="ref" reference="app:evidence"}.

## Limitations and conclusion {#sec:conclusion}

The results concern one frozen looped graph, one real-logarithm branch, and one Dirichlet weighting. We prove neither an all-$\mathcal S_{p}$ theorem nor any connection between this powers-of-two support and rational primes; no Hilbert--Polya operator, completed divisor, or functional equation is claimed. For nonreal $s$, $H_s$ is complex symmetric but is not asserted to be Hermitian. The cycle theorem classifies a fixed ordered label system; it does not by itself enumerate primitive orbits modulo rotation.

Within those boundaries, one dyadic constraint controls both halves of the paper. Its anti-diagonal geometry creates the strict ideal walls, while its valuation invariance turns the bounded operator into repeated odd blocks. The alternating recurrence is the finite-dimensional counterpart of that same support and closes every labeled cyclic system. A concrete next question is whether the intermediate Schatten classes of this same frozen operator admit comparably sharp thresholds; the cases $p=1,2$ proved here do not justify extrapolating an answer.

# Endpoint estimates and the trace-dual matching {#app:endpoints}

This appendix records the quantitative bounds used in [\[sec:bounded,sec:ideals\]](#sec:bounded,sec:ideals){reference-type="ref" reference="sec:bounded,sec:ideals"}. They are included to make the endpoint strictness independent of any finite-cutoff trend.

## Anti-diagonal levels

For $N\ge2$ and $\alpha>0$, put $$S_\alpha(N)=\sum_{m=1}^{N-1}[m(N-m)]^{-\alpha}.$$ By symmetry, $$S_\alpha(N)
  =2\sum_{1\le m<N/2}[m(N-m)]^{-\alpha}
   +\mathbf 1_{\{N\ {\rm even}\}}(N^2/4)^{-\alpha}.$$ On $m\le N/2$, $$N^{-\alpha}m^{-\alpha}
  \le [m(N-m)]^{-\alpha}
  \le 2^\alpha N^{-\alpha}m^{-\alpha}.$$ For $0<\alpha<1$, the integral comparison $$c_\alpha M^{1-\alpha}
  \le\sum_{m\le M}m^{-\alpha}
  \le C_\alpha M^{1-\alpha}$$ therefore gives $$c_\alpha N^{1-2\alpha}
  \le S_\alpha(N)
  \le C_\alpha N^{1-2\alpha}.$$ At $\alpha=1$, summing the partial-fraction identity in [\[lem:level-estimates\]](#lem:level-estimates){reference-type="ref" reference="lem:level-estimates"} gives $S_1(N)=2H_{N-1}/N$. For $\alpha>1$, the same half-interval estimate and $\sum_{m\ge1}m^{-\alpha}<\infty$ give $S_\alpha(N)\le C_\alpha N^{-\alpha}$.

At the Hilbert--Schmidt boundary $\sigma=1/2$, one can see divergence without invoking the full comparison. For $N/4\le m\le3N/4$, both factors are at most $3N/4$, so each of the $\gg N$ central summands in [\[eq:hs-levels\]](#eq:hs-levels){reference-type="ref" reference="eq:hs-levels"} is $\gg N^{-1}$. Every dyadic level therefore has mass bounded below by a positive constant.

## Compactness from row decay

The row-decay estimate in [\[eq:row-decay\]](#eq:row-decay){reference-type="ref" reference="eq:row-decay"} gives both $\sup_mR_m<\infty$ and $R_m\to0$. The second assertion alone does not immediately make an arbitrary bounded matrix compact, so we record the finite-row tail step. For fixed $M$, absolute summability of each of the rows $1,\ldots,M$ permits one common $N$ for their tails. Rows above $M$ are controlled in their entirety by $R_m$. Thus the modulus of $H_s-P_NH_sP_N$ has uniformly small row and column sums. This is the precise norm-approximation argument used in [\[thm:bounded\]](#thm:bounded){reference-type="ref" reference="thm:bounded"}.

## Disjoint matching details

For $Q_j=4^j$, the sets in [\[eq:matching-sets\]](#eq:matching-sets){reference-type="ref" reference="eq:matching-sets"} satisfy $$I_j\subset[Q_j/4,Q_j/3],
 \qquad
 J_j\subset[2Q_j/3,3Q_j/4].$$ They are disjoint within a scale. Their union lies below $3Q_j/4$, whereas the next interval $I_{j+1}$ begins at $Q_{j+1}/4=Q_j$; consequently all domains and ranges used by the matchings are pairwise disjoint across scales.

If $m\in I_j$ and $n\in J_j$, then $11Q_j/12\le m+n\le13Q_j/12$. The only power of two in that interval is $Q_j$, so the selected support entry is present exactly when $n=Q_j-m$. Define the matrix of $V_J$ on these entries by $$(V_J)_{m,Q_j-m}
  =\frac{h_s(m,Q_j-m)}{\lvert h_s(m,Q_j-m)\rvert}.$$ Disjointness makes $V_J$ a partial isometry of norm one. With the matrix convention $T_{m,n}=\langle Te_n,e_m\rangle$, $$\mathop{\mathrm{Tr}}(V_J^*H_s)
  =\sum_{j\le J}\sum_{m\in I_j}
    \overline{(V_J)_{m,Q_j-m}}\,h_s(m,Q_j-m),$$ which is the positive sum in [\[eq:trace-dual-pairing\]](#eq:trace-dual-pairing){reference-type="ref" reference="eq:trace-dual-pairing"}. Moreover, $\lvert I_j\rvert\asymp Q_j$ and $m,Q_j-m\asymp Q_j$ uniformly on $I_j$, so $$\sum_{m\in I_j}[m(Q_j-m)]^{-\sigma/2}
  \asymp_\sigma Q_j^{1-\sigma}.$$ For $\sigma=1$ each scale contributes a positive constant; for $\sigma<1$ its contribution grows. Trace duality would require all finite partial sums to be at most $\lVert H_s\rVert_1$, completing the endpoint contradiction without estimating finite-cutoff trace norms.

# Direct sums of Hilbert--Carleman determinants {#app:determinants}

We prove the specialized direct-sum statement used in [\[prop:det2-product\]](#prop:det2-product){reference-type="ref" reference="prop:det2-product"}. The proof is included so that the block product does not depend on a brittle page citation.

[\[lem:abstract-det2-sum\]]{#lem:abstract-det2-sum label="lem:abstract-det2-sum"} Let $T_k$ be compact Hilbert--Schmidt operators, and suppose $$\sum_{k\ge0}\lVert T_k\rVert_2^2<\infty.$$ Then $T=\bigoplus_{k\ge0}T_k$ is Hilbert--Schmidt and $$\det_2(I-zT)=\prod_{k\ge0}\det_2(I-zT_k),
  \label{eq:abstract-det2-product}$$ with uniform convergence on compact subsets of $\mathbb C$.

List the nonzero eigenvalues of $T_k$, with algebraic multiplicity, as $\lambda_{k,j}$. Weyl's eigenvalue inequality gives $$\sum_{k,j}\lvert \lambda_{k,j}\rvert^2
  \le\sum_k\lVert T_k\rVert_2^2<\infty.
  \label{eq:combined-eigenvalue-l2}$$ Also $\lVert T_k\rVert\le\lVert T_k\rVert_2\to0$. Hence the nonzero eigenvalues of the compact direct sum $T$ are exactly the combined multiset $\{\lambda_{k,j}\}_{k,j}$.

Fix a compact set $K\subset\mathbb C$ and put $R=\max_{z\in K}\lvert z\rvert$. By [\[eq:combined-eigenvalue-l2\]](#eq:combined-eigenvalue-l2){reference-type="ref" reference="eq:combined-eigenvalue-l2"}, only finitely many combined eigenvalues satisfy $R\lvert \lambda_{k,j}\rvert>1/2$. For every remaining factor, use the analytic branch at zero: $$\log E_2(w)=\log(1-w)+w
  =-\sum_{r\ge2}\frac{w^r}{r},
  \qquad \lvert w\rvert\le\frac12.
  \label{eq:E2-log-bound}$$ The series gives $\lvert \log E_2(w)\rvert\le\lvert w\rvert^2$ on this disk. Therefore $$\sum_{k,j}\sup_{z\in K}
  \lvert \log E_2(z\lambda_{k,j})\rvert
  \le R^2\sum_{k,j}\lvert \lambda_{k,j}\rvert^2<\infty$$ after removing the finite exceptional set. The combined canonical product thus converges normally on $K$. Normal convergence makes its value independent of the ordering and permits grouping first over $j$ and then over $k$. The ungrouped product is the eigenvalue definition of $\det_2(I-zT)$; each grouped product is $\det_2(I-zT_k)$. This proves [\[eq:abstract-det2-product\]](#eq:abstract-det2-product){reference-type="ref" reference="eq:abstract-det2-product"}, including compact-uniform convergence. Zeros among the finitely many exceptional factors cause no difficulty, because the identity follows between the resulting entire products.

Apply the lemma with $T_k=2^{-ks}A_s$. In the domain $\sigma>1/2$, $A_s\in\mathcal S_{2}$ and $$\sum_{k\ge0}\lVert T_k\rVert_2^2
  =\lVert A_s\rVert_2^2\sum_{k\ge0}2^{-2k\sigma}<\infty.$$ The unitary equivalence in [\[thm:direct-sum\]](#thm:direct-sum){reference-type="ref" reference="thm:direct-sum"} identifies $T=\bigoplus_kT_k$ with $H_s$, proving [\[eq:det2-product\]](#eq:det2-product){reference-type="ref" reference="eq:det2-product"}.

For completeness, if $\lvert z\rvert\lVert H_s\rVert<1$, then $I-zH_s$ is invertible by the Neumann series, so the determinant has no zero on that disk. The branch of its logarithm fixed at zero satisfies $$\log\det_2(I-zH_s)
  =-\sum_{r\ge2}\frac{z^r}{r}\mathop{\mathrm{Tr}}(H_s^r).$$ Indeed, $$\lvert \mathop{\mathrm{Tr}}(H_s^r)\rvert
  \le\lVert H_s^r\rVert_1
  \le\lVert H_s\rVert_2^2\lVert H_s\rVert^{r-2},$$ so the series converges absolutely under the displayed condition. Inserting [\[eq:trace-factor\]](#eq:trace-factor){reference-type="ref" reference="eq:trace-factor"} gives [\[eq:local-log-det2\]](#eq:local-log-det2){reference-type="ref" reference="eq:local-log-det2"}. This derivation also shows why the local logarithm cannot be promoted to a single global branch when the entire determinant has zeros.

If $\sigma>1$, then $A_s\in\mathcal S_{1}$ and $$\sum_{k\ge0}\lVert 2^{-ks}A_s\rVert_1
  =\lVert A_s\rVert_1\sum_{k\ge0}2^{-k\sigma}<\infty.$$ The genus-zero eigenvalue products consequently converge normally on compact $z$-sets and give [\[eq:det-product\]](#eq:det-product){reference-type="ref" reference="eq:det-product"}. Finally, the defining relation $\det_2(I+T)=\det(I+T)e^{-\mathop{\mathrm{Tr}}T}$ for trace-class $T$, applied to $T=-zH_s$ and combined with [\[eq:ordinary-trace\]](#eq:ordinary-trace){reference-type="ref" reference="eq:ordinary-trace"}, gives [\[eq:det-overlap\]](#eq:det-overlap){reference-type="ref" reference="eq:det-overlap"}.

# Cycle intervals, parity, and orbit bookkeeping {#app:cycles}

The affine coordinates in [\[thm:cycle-solver\]](#thm:cycle-solver){reference-type="ref" reference="thm:cycle-solver"} make positivity transparent. Under even compatibility, $$n_i=(-1)^{i-1}x+b_i.$$ Every odd index contributes a strict lower bound $x>-b_i$, and every even index contributes a strict upper bound $x<b_i$. Both index sets are nonempty for even $r\ge2$, so the interval $(L(q),U(q))$ is finite. It may be empty. Since all $q_i$ and hence all $b_i$ are integers, its positive solution count is exactly $$\#(\mathbb Z\cap(L(q),U(q)))
  =\max\{0,U(q)-L(q)-1\}.$$ For the odd block, the recurrence modulo two reads $n_{i+1}\equiv n_i\pmod2$, because $q_i$ is even. Thus filtering $x=n_1$ to odd values filters every vertex simultaneously.

At $r=1$, [\[eq:odd-candidate\]](#eq:odd-candidate){reference-type="ref" reference="eq:odd-candidate"} gives $n_1=q_1/2$. This is exactly the loop at a power of two. In the odd block only $q_1=2$ remains, corresponding to the loop at vertex $1$. This length-one convention is independent of the restriction $r\ge2$ used for Hilbert--Schmidt trace powers.

#### Based words, rotations, and primitive period.

A solution of [\[eq:cycle-system\]](#eq:cycle-system){reference-type="ref" reference="eq:cycle-system"} is a based vertex word $(n_1,\ldots,n_r)$. Rotating the word changes its base point but represents the same cyclic orbit. The edge labels rotate with it. A word is primitive only when its least cyclic shift period is $r$; a repeated traversal is not a new primitive orbit. The label tuple is derived from the vertex word and does not replace it: the same compatible even label tuple can have several vertex solutions, as $(4,8,8,4)$ demonstrates.

The coefficient $1/r$ in the local determinant logarithm removes cyclic base points at the level of based trace terms. It does not declare every label tuple primitive, nor does it turn a repeated word into a new primitive. Any Euler-product reorganization would require a separate least-period reduction. No such primitive-orbit product is claimed in this paper.

#### Finite-cutoff evaluation.

For a cutoff $N$, a matrix-independent evaluator lists the allowed ordered labels, applies [\[thm:cycle-solver\]](#thm:cycle-solver){reference-type="ref" reference="thm:cycle-solver"}, and then retains precisely the solutions with $1\le n_i\le N$ for every $i$. Summing $\prod_i n_i^{-s}$ over these based solutions agrees with the trace of the cutoff matrix power. The procedure is exact because the theorem classifies all positive solutions for each fixed ordered tuple; it uses neither a spectral approximation nor a primitive-orbit heuristic.

# Canonical State-A evidence binding {#app:evidence}

The manuscript table was generated from a protected State-A snapshot by a writer-side extractor. The extractor rejects duplicate JSON keys, noncanonical serialization, unexpected paths, failed statuses, and any ledger/hash mismatch before emitting the local summary. The relevant bindings are listed below.

**State-A result ledger.** ``.

**Science projection.** ``.

**Writer canonical summary.** ``.

**Protected authority snapshot.** ``.

The exact finite block identity retains a different odd cutoff at every valuation scale. If $A_s^{(M)}$ denotes the odd block restricted to odd $u\le M$, then the evaluated identity is $$\mathop{\mathrm{Tr}}\!((P_NH_sP_N)^r)
  =\sum_{0\le k\le\lfloor\log_2N\rfloor}
    2^{-krs}
    \mathop{\mathrm{Tr}}\!(
      (A_s^{(\lfloor N/2^k\rfloor)})^r
    ).
  \label{eq:finite-scale-trace}$$ The summands in [\[eq:finite-scale-trace\]](#eq:finite-scale-trace){reference-type="ref" reference="eq:finite-scale-trace"} do not share a common truncation, so the finite sum is not a geometric factor. Only the analytic infinite-operator proof licenses [\[eq:trace-factor\]](#eq:trace-factor){reference-type="ref" reference="eq:trace-factor"}.

The two evaluator sources have different digests, use no project-local imports, and share neither expanded fixtures nor serialized intermediates. The adversarial closeout exercised $62$ mutations in $25$ families across $162$ designated consumer invocations, with no survivor. A separate frozen audit rejected all $13$ physical mutated clones across $22$ invocations. These are reproducibility and type-discipline metadata, not additional mathematical evidence.

The comparison type is `FINITE_EXACT_DIAGNOSTIC`; its recorded infinite-theorem status is `NOT_INFERRED_FROM_FINITE_EVIDENCE`. State A contains no publication manifest or State-B provenance, and this appendix makes no such claim. These checks establish reproducibility of the evaluated artifact only. They do not prove an endpoint, external priority, rational-prime emergence, or any target divisor.
