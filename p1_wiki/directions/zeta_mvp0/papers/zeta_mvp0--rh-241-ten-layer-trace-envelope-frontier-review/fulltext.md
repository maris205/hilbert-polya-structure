---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-241-ten-layer-trace-envelope-frontier-review"
canonical_tex: "zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review/main.pdf"
source_sha256: "9d4518bafd09ffebc87043fb6004b3020a1f0fc86e929f837a574d8c7660b886"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ten Layers at the Trace-Envelope Frontier From an Ill-Conditioned Riesz Cloud to a Projection-Free Relative Determinant Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-241-ten-layer-trace-envelope-frontier-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-232--RH-240 decide the moving-cloud fork left open by RH-231. The direct biorthogonal Riesz construction exists at every finite endpoint, but its norm grows from $40.75$ to $2.26\times10^{12}$; a fixed-gap triangular theorem proves that positive radial shell separation cannot prevent this behavior. The operator-projector route is therefore not presently uniform.

  The determinant route survives. A finite eigenvalue submultiset factors $\det_2$ exactly without evaluating a projector. A nilpotent model then proves that divergent Hilbert--Schmidt mass can coexist with trivial $\det_2$, so the RH-229 Frobenius wall is not a spectral obstruction. Direct sparse traces through order twelve produce 384 cloud-extracted moments. The largest observed Cauchy root rate is $0.35989$, the fine-scale unit-disk jet norm is at most $0.01067$, and all 16 dual-channel jet comparisons pass $0.02$.

  A trace-adaptive shell selector with tolerance $\varepsilon_\sigma=\sigma$ succeeds at all 32 endpoints. Vanishing tolerances imply contraction of every fixed finite jet, but not of the full determinant. The exact remaining theorem is an all-order envelope $|\tau_n(\sigma)|\le Mq^n$, together with a coefficient anchor preventing over-extraction. The batch contains 7,280 finite ledger items and zero identity failures. Gate A and all Hilbert--Polya claims remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Ten Layers at the Trace-Envelope Frontier\
  From an Ill-Conditioned Riesz Cloud to a Projection-Free Relative Determinant Gate
```

## Markdown 正文

# Position after RH-231

The previous batch established a rank-growing reciprocal cloud, rejected a direct tight-zero-divisor interpretation, and reconnected the finite atlas to the fixed-noise regularized determinant [@WangRH222; @WangRH228; @WangRH229; @WangRH230; @WangRH231]. Its next target was a moving Riesz or reducing factor with a uniformly controlled complement.

There were two logically distinct questions:

1.  can the cloud be isolated as a stable invariant subspace?

2.  can its determinant factor and complement be controlled even if the projector is badly conditioned?

RH-232--RH-240 show that the answer is currently negative for the first question and positive, at finite order, for the second.

# The nine research layers

  Layer    Result                                                                    Route consequence
  -------- ------------------------------------------------------------------------- -------------------------------------------------------
  RH-232   Biorthogonal projectors at 32 endpoints; norm up to $2.26\times10^{12}$   direct uniform Riesz bound unsupported
  RH-233   fixed spectral gap with unbounded projector norm                          radial gaps are not pseudospectral certificates
  RH-234   exact projection-free finite $\det_2$ factor                              determinant route bypasses eigenvector conditioning
  RH-235   nilpotent trace/HS separation; actual $|\tau_2|\le0.12952$                Frobenius wall is too strong, not decisive
  RH-236   trace moments through order twelve                                        finite trace route opened
  RH-237   /16 unit-disk channel jets below $0.02$                                   finite coefficients are discretization-coherent
  RH-238   $\varepsilon_\sigma=\sigma$ shell selector passes 32/32                   finite rank schedule becomes determinant-adaptive
  RH-239   exact finite-jet contraction; nonmonotone observed distances              fixed jets are not a full entire-function topology
  RH-240   all-order geometric trace-envelope theorem                                order thirteen and above become the precise next wall

  : The RH-232--RH-240 chain.

# The Riesz wall is genuine but local

Given matched right and left invariant bases $R$ and $L$, the formula $$P=R(L^*R)^{-1}L^*$$ is exact. The numerical issue is the collapse of the smallest singular value of $L^*R$. RH-232 finds a minimum of $5.67\times10^{-13}$ and 17 endpoint projectors above $10^6$ [@WangRH232].

RH-233 proves that eigenvalue separation cannot repair this by itself. For $$A_M=\begin{pmatrix}\lambda&M\\0&\mu\end{pmatrix},$$ the projector norm is $\sqrt{1+|M/(\lambda-\mu)|^2}$ even when $|\lambda-\mu|$ is fixed [@WangRH233; @TrefethenEmbree2005]. The minimum archived ratio of radial gap to projector norm, $6.40\times10^{-16}$, is therefore conceptually consistent.

This does not rule out every operator space. A stronger anisotropic norm or an analytic contour estimate could still produce a controlled projector. What it rules out is treating the positive radial gap as if it were already such an estimate.

# Projection-free determinant factor

For a Hilbert--Schmidt operator with eigenvalues $(\lambda_j)$, the canonical product $$\det_2(I-zA)=\prod_j(1-z\lambda_j)e^{z\lambda_j}$$ splits over any finite eigenvalue submultiset. RH-234 verifies the selected and resolved-complement split in 6,144 cases, with maximum discrepancy $1.83\times10^{-15}$ [@WangRH234; @Simon2005]. The factor is algebraic in the eigenvalue multiset and does not carry the Riesz condition number.

The complementary logarithm is generated by $$\label{eq:log}
 \log R_\sigma(z)
 =-\sum_{n\ge2}\frac{\tau_n(\sigma)}{n}z^n,$$ where $\tau_n$ is the full power trace after subtracting the Perron, parity, and cloud powers.

# Why the failed Frobenius bound can be bypassed

The nilpotent shift $S_N$ has $$\left\lVert S_N\right\rVert_2^2=N-1,
 \qquad
 \operatorname{tr}(S_N^n)=0,
 \qquad
 \det_2(I-zS_N)=1.$$ Thus nonnormal singular-value mass need not enter the eigenvalue determinant. In the actual matrices, the complement Hilbert--Schmidt squared upper reaches $308.75$, while the second trace modulus is at most $0.12952$; the ratio can exceed $2.36\times10^6$ [@WangRH235].

The correct interpretation of RH-229 is consequently narrower: a generic ideal-norm proof fails, but a cancellation-sensitive trace proof remains possible.

# Finite trace evidence

RH-236 computes orders one through twelve directly from sparse matrix powers [@WangRH236]. The principal batch statistics are $$\max J_{12}=0.07593,
 \qquad
 \max_{\sigma\le0.005}J_{12}=0.01067,
 \qquad
 \max_{2\le n\le12}|\tau_n|^{1/n}=0.35989.$$ The fine-scale observed rate is $0.14377$. RH-237 compares the same jets between the fine and Haar-coarse channels; the maximum unit-disk distance is $0.01415$, and all 16 cases pass the $0.02$ gate [@WangRH237].

These numbers are substantially more stable than the full Frobenius mass, but they remain finite-order statements.

# Adaptive clouds and their ambiguity

RH-238 chooses the first shell prefix satisfying $$\sum_{n=2}^{12}\frac{|\tau_n|}{n}\le\sigma.$$ All endpoints pass; ranks range from five to 38 [@WangRH238]. If two selected residuals satisfy tolerances $\varepsilon$ and $\delta$, then the triangle inequality gives a jet distance at most $\varepsilon+\delta$. RH-239 verifies every corresponding finite comparison and proves that vanishing tolerances force fixed finite jets to be Cauchy [@WangRH239].

Two ambiguities remain. First, up to ten prefixes can meet the same tolerance. Second, making a residual jet small can absorb regular spectral information as well as the singular cloud. The "first prefix" rule makes the finite selector deterministic, but only a coefficient anchor can prove that it leaves the intended deterministic numerator.

# The all-order theorem

RH-240 proves the decisive sufficient criterion [@WangRH240].

[\[thm:gate\]]{#thm:gate label="thm:gate"} If constants $M,q$ satisfy $$|\tau_n(\sigma)|\le Mq^n
 \quad\text{for all }n\ge2\text{ and all sufficiently small }\sigma,$$ then for $Rq<1$, $$\sup_{|z|\le R}|\log R_\sigma(z)|
 \le M[-\log(1-Rq)-Rq]
 \le \frac{M(Rq)^2}{2(1-Rq)}.$$ Hence the relative determinants and their reciprocals are locally bounded on $|z|<q^{-1}$. If every fixed trace coefficient converges, the determinants converge locally uniformly there.

The observed orders $2$--$12$ fit the unit-amplitude rates $0.35989$ and $0.14377$. If those rates held for all orders, the unit-disk bounds would be $0.10117$ and $0.01207$. They are not yet theorems because the first missing coefficient is order thirteen.

# Logical dependency and surviving branch

The batch separates implications that had previously been bundled together: $$\begin{array}{c}
\text{selected finite eigenvalue multiset}\\
\Downarrow\ \text{(exact, RH-234)}\\
\text{projection-free finite cloud factor}\\
\Downarrow\ \text{(open uniformly in }\sigma\text{)}\\
\text{all-order trace envelope for the complement}\\
\Downarrow\ \text{(RH-240 plus coefficient convergence)}\\
\text{locally uniform zero-free relative determinant}\\
\Downarrow\ \text{(open anchor)}\\
\text{identified deterministic numerator.}
\end{array}$$ Only the first and third arrows have exact theorems at present; the middle uniform estimate and final identification are the active obligations.

This dependency chart also records the status of four alternatives. The Euclidean Riesz route is dormant because its projector norms are enormous, not logically impossible on every function space. The radial-gap shortcut is ruled out by an exact nonnormal counterexample. The whole-complement Hilbert--Schmidt route is too strong and can miss complete spectral cancellation. Fixed finite jets are informative but topologically insufficient. The surviving branch is therefore a projection-free, cancellation-sensitive periodic-trace argument.

# Next research block

The next target coordinate is $$\boxed{\texttt{all\_order\_cloud\_extracted\_periodic\_trace\_envelope}
 \quad\texttt{with\_coefficient\_anchor}}.$$ A ten-step implementation can be organized as follows:

1.  derive an exact finite-noise periodic-loop representation for each cloud-extracted trace $\tau_n(\sigma)$;

2.  isolate the loop families corresponding to the moving peripheral cloud before taking absolute values;

3.  determine which short-loop coefficients should survive as the deterministic numerator anchor;

4.  test cancellation-preserving orbit groupings against the full order-$12$ atlas;

5.  prove a uniform long-loop majorant in a restricted noise--order regime;

6.  quantify the transition between a certified finite head and the analytic long-order tail;

7.  make the shell selector target the anchored coefficients rather than zero whenever the anchor is available;

8.  validate the finite head with outward numerical error bounds in both discretization channels;

9.  apply the RH-240 theorem to obtain compact-set convergence of the relative determinant on its controlled disk;

10. audit whether the resulting local factor is nontrivial, canonical, and compatible with the deterministic determinant route.

Several steps may merge if the periodic formula exposes a direct generating function. Conversely, failure of absolute orbit bounds would not end the branch if a grouped cancellation theorem remains available. The next batch should therefore treat negative bounds as route information rather than force them into a positive asymptotic claim.

# Revised Gate-A route

The coordinate after this batch is $$\boxed{\begin{gathered}
 \texttt{projection\_free\_relative\_det2}\\
 \texttt{\_open\_uniform\_trace\_envelope}
 \end{gathered}}.$$

The next target has two inseparable parts:

1.  derive an all-order cloud-extracted trace bound from noisy periodic-loop integrals, uniform in both orbit length and noise;

2.  prove a coefficient anchor showing that the moving cloud removes the singular factor without swallowing the regular deterministic numerator.

The aggregate finite ledger contains 7,280 cases and zero identity failures. This audit count does not upgrade floating sparse matrices to interval operators and does not prove either next target.

# Macro boundary

Gate A remains open at the uniform trace envelope. Gates B--E have not moved: there is no completed unitary/scattering object, no self-adjoint generator, no intrinsic $T\log T$ counting theorem, no von Mangoldt trace identity, and no equality with the completed zeta divisor. In particular this batch does not construct a Hilbert--Polya operator, identify Riemann zeros, or imply the Riemann Hypothesis.
