---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-53-deterministic-hardy-tail-cutoff"
canonical_tex: "zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/main.pdf"
source_sha256: "0e1d8969e97c3c03b0d3bfd8b2bb22582e636e1b70918aa153366ce5c42f1aba"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Deterministic Block-Tail Certificates for Directional Hardy Energies All-Column Trace Sums, Adaptive Gaussian Cutoff Transfer, and the Remaining Production-Interval Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The two-pole Hardy reduction for the noisy quadratic transfer operator was previously audited with eight Hutchinson probes, a time-64 truncation, and a fitted decay base. We replace all three ingredients at the finite-matrix level. For a stable scaled bulk matrix $A$, directional source $X$, and observation $Y$, put $$S_M=\sum_{m=0}^{M-1}A^mXX^*(A^*)^m,
   \qquad q_M=\left\lVert A^M\right\rVert_2.$$ The finite contribution is the deterministic all-column identity $$\operatorname{tr}(YS_MY^*)=\sum_{m=0}^{M-1}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2.$$ If $q_M<1$, block Stein domination gives the complete infinite-energy certificate $$\sum_{m\ge0}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2
   \le \operatorname{tr}(YS_MY^*)+
   \frac{\left\lVert A^MS_M(A^*)^M\right\rVert_2}{1-q_M^2}\left\lVert Y\right\rVert_{\mathfrak S_2}^2.$$ A complementary block-geometric tail is also proved. Thus neither a probabilistic trace estimate nor a fitted asymptotic decay rate is needed.

  We then give a finite-time perturbation theorem for simultaneous changes of $(A,X,Y)$, using the exact telescoping identity for $A^m-\widetilde A^m$. This transports both the main sum and one contracting block whenever finite-time semigroup norm ledgers leave positive margin. Combined with the folded-Gaussian cutoff estimates of RH-39, it yields an honest route from a sparse family to the canonical full Gaussian family. A fixed eight-standard- deviation window is below $5.60\times10^{-13}$ in the analytic Euclidean bound on all stored RH-50 scales through $N=40960$, but has a strictly positive continuum row defect and therefore cannot define the full-kernel all-grid limit. The adaptive law $$L(h)=\max\{5,2\sqrt{\log(1/h)}\}$$ instead gives an $O(h^2/(\log(1/h))^{1/4})$ cutoff defect.

  A binary64 dense all-column audit at $N=32,\ldots,512$ certifies both directional energies with worst relative excess $4.94\times10^{-4}$. A separate 256-bit Arb run executes the complete outward-rounded algorithm on a small abstract matrix. The production-scale interval trace and the complete factor-aware cutoff transfer have not been executed. Hence the deterministic tail mechanism and adaptive exact-real route close, while Stage A3 as a production certificate does not. No arithmetic trace formula, zeta-zero identity, self-adjoint realization, counting law, or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Deterministic Block-Tail Certificates for Directional Hardy Energies\
  All-Column Trace Sums, Adaptive Gaussian Cutoff Transfer, and the Remaining Production-Interval Gap
```

## Markdown 正文

**Keywords:** Hilbert--Schmidt Hardy energy; Stein inequality; deterministic trace; Gaussian cutoff; interval arithmetic; small-noise transfer operator.

**MSC 2020:** 47A10; 47B10; 65F35; 65G20; 93B36.

# Introduction

RH-49 reduced the last mixed resolvent gate in the dyadic intrinsic identification program to two Hilbert--Schmidt range actions. RH-50 removed the Perron and parity poles, represented the remainder by directional Hardy energies, and observed moderate values over five small-noise scales [@WangHardy2026]. Those values were not upper bounds: each Hilbert--Schmidt norm was estimated with random-sign probes, the series was stopped after power 64, and the omitted tail was interpreted through a fitted decay base.

RH-51 supplied the correct positive mechanism. Exact low-rank Stein supersolutions are obstructed by the growing directional cyclic subspace, but a finite Krylov sum plus a full-dimensional positive tail becomes sharp once one power $A^M$ is a Euclidean contraction [@WangStructuredStein2026]. RH-52 separately closed the sufficient peripheral residue action from weak finite factors [@WangFactorTransfer2026]. The scheduled RH-53 question is whether the infinite tail and sparse Gaussian cutoff can be certified without silently promoting floating evidence.

This paper gives a positive answer at the level of analytic architecture and a deliberately incomplete answer at production interval level. The main contributions are:

1.  a deterministic finite-horizon Hilbert--Schmidt trace algorithm that propagates all source columns and never forms a full Gramian;

2.  two explicit infinite-tail bounds from one contracting block;

3.  an outward-rounding ledger that turns local matrix-action, norm, and trace errors into a complete finite-matrix certificate;

4.  a perturbation theorem for the finite trace and the block contraction;

5.  a proof that fixed eight sigma is a finite-computation convenience, not the canonical full-kernel joint limit; and

6.  an adaptive sparse-to-full route compatible with growing horizons.

Three evidence levels remain separate. Algebraic theorems are exact. Closed cutoff formulas and the small Arb audit are validated. The five-scale all-column experiment and intrinsic eigendata are binary64 diagnostics. This separation is the central conclusion rather than a technical footnote.

# Directional Hardy pairs

Let $T$ be a fine folded-Gaussian matrix, $A_c$ its exact coarse Haar block, and $$T=\begin{pmatrix}A_c&B\\ C&D\end{pmatrix}.$$ After removing the intrinsic Perron and parity Riesz terms, let $N_f,N_c$ be the fine and coarse bulk matrices, $Q_f,Q_c$ the corresponding complements, $U$ the coarse-to-fine isometry, and $r$ a Hardy radius above both bulk spectral radii. The two pairs are $$\begin{aligned}
 A_B&=r^{-1}N_f,
 &X_B&=Q_fUB/\left\lVert B\right\rVert_{\mathfrak S_2},
 &Y_B&=U^*,\\
 A_C&=r^{-1}N_c^*,
 &X_C&=C^*/\left\lVert C\right\rVert_{\mathfrak S_2},
 &Y_C&=Q_c^*.\end{aligned}$$ Both energies have the abstract form $$\mathcal E(A,X,Y)^2=\sum_{m=0}^{\infty}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2.
 \label{eq:energy}$$ We therefore work with $A\in\mathbb C^{d\times d}$, $X\in\mathbb C^{d\times p}$, and $Y\in\mathbb C^{q\times d}$, assuming the spectral radius of $A$ is less than one.

# Deterministic main sum and exact infinite tail

For $M\ge1$, define $$S_M=\sum_{m=0}^{M-1}A^mXX^*(A^*)^m.
 \label{eq:SM}$$

[\[prop:main-sum\]]{#prop:main-sum label="prop:main-sum"} One has the exact identity $$\boxed{\operatorname{tr}(YS_MY^*)=\sum_{m=0}^{M-1}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2.}
 \label{eq:main-sum}$$ It can be evaluated using the recurrence $Z_0=X$, $Z_{m+1}=AZ_m$, accumulating $\left\lVert YZ_m\right\rVert_{\mathfrak S_2}^2$. The algorithm stores only the current $d\times p$ source block and uses no random trace estimator.

Expand [\[eq:SM\]](#eq:SM){reference-type="eqref" reference="eq:SM"}, use linearity and cyclicity of the finite trace, and apply $\operatorname{tr}(WW^*)=\left\lVert W\right\rVert_{\mathfrak S_2}^2$.

The word deterministic distinguishes [\[eq:main-sum\]](#eq:main-sum){reference-type="eqref" reference="eq:main-sum"} from Hutchinson sampling. It does not by itself validate floating arithmetic. Outward rounding is discussed in [4](#sec:rounding){reference-type="ref" reference="sec:rounding"}.

[\[thm:block-tail\]]{#thm:block-tail label="thm:block-tail"} Let $P_M=A^M$, $q_M=\left\lVert P_M\right\rVert_2<1$, and let $S_M$ be [\[eq:SM\]](#eq:SM){reference-type="eqref" reference="eq:SM"}. Then $$\boxed{
 \mathcal E(A,X,Y)^2
 \le \operatorname{tr}(YS_MY^*)+
 \frac{\left\lVert P_MS_MP_M^*\right\rVert_2}{1-q_M^2}\left\lVert Y\right\rVert_{\mathfrak S_2}^2.}
 \label{eq:stein-tail}$$ Also, $$\boxed{
 \mathcal E(A,X,Y)^2
 \le \operatorname{tr}(YS_MY^*)+
 \left\lVert Y\right\rVert_2^2\frac{q_M^2}{1-q_M^2}\operatorname{tr}S_M.}
 \label{eq:simple-tail}$$ The smaller of the two displayed tails is a valid upper.

Let $$G=\sum_{m\ge0}A^mXX^*(A^*)^m.$$ The block decomposition gives $G=S_M+P_MGP_M^*$. Put $$\alpha_M=\frac{\left\lVert P_MS_MP_M^*\right\rVert_2}{1-q_M^2},
 \qquad H_M=S_M+\alpha_M\mathrm I.$$ Since $$\alpha_M(\mathrm I-P_MP_M^*)-P_MS_MP_M^*\ge0,$$ $H_M-P_MH_MP_M^*\ge S_M$. Iterating this block inequality gives $H_M\ge G$. Pair with $Y^*Y\ge0$ to obtain [\[eq:stein-tail\]](#eq:stein-tail){reference-type="eqref" reference="eq:stein-tail"}.

For the second bound, group the tail into residues $m=kM+j$, $0\le j<M$. Submultiplicativity gives $$\sum_{k\ge1}\sum_{j=0}^{M-1}
 \left\lVert YA^{kM+j}X\right\rVert_{\mathfrak S_2}^2
 \le \left\lVert Y\right\rVert_2^2\sum_{k\ge1}q_M^{2k}
 \sum_{j=0}^{M-1}\left\lVert A^jX\right\rVert_{\mathfrak S_2}^2,$$ which is [\[eq:simple-tail\]](#eq:simple-tail){reference-type="eqref" reference="eq:simple-tail"}.

The theorem validates the entire infinite series for each finite matrix once one $q_M<1$ is certified. It does not prove that the resulting upper is uniform or polylogarithmic as noise vanishes. That is the independent Stage A1 trace-budget problem.

# Outward-rounded certificate ledger {#sec:rounding}

The exact formulas admit a direct validated implementation. Suppose an interval or directed-rounding computation returns upper endpoints $$\widehat e_m\ge\left\lVert YA^mX\right\rVert_{\mathfrak S_2},\quad 0\le m<M,
 \qquad
 \widehat q_M\ge\left\lVert A^M\right\rVert_2,$$ and $$\widehat r_M\ge\left\lVert A^MS_M(A^*)^M\right\rVert_2,
 \qquad
 \widehat y_2\ge\left\lVert Y\right\rVert_{\mathfrak S_2}^2.$$

[\[cor:outward\]]{#cor:outward label="cor:outward"} If $\widehat q_M<1$, then $$\mathcal E(A,X,Y)^2
 \le
 \sum_{m=0}^{M-1}\widehat e_m^2
 +\frac{\widehat r_M\widehat y_2}{1-\widehat q_M^2}.
 \label{eq:outward}$$ The same conclusion holds when each displayed upper includes an explicit local roundoff or matrix-data perturbation budget.

Monotonicity of the positive terms and [\[thm:block-tail\]](#thm:block-tail){reference-type="ref" reference="thm:block-tail"} suffice.

Our 256-bit Arb audit encloses all input entries by radius $10^{-30}$, propagates the complete source block, and uses Frobenius interval uppers for the two spectral norms. Since $\left\lVert M\right\rVert_2\le\left\lVert M\right\rVert_{\mathfrak S_2}$, this is rigorous though intentionally coarse. For a $4\times4$ matrix and $M=6$, it certifies $$\widehat q_M\le0.052027,\qquad
 \mathcal E^2\le0.093115,\qquad
 \mathcal E\le0.305147.$$ This proves that the outward algorithm is executable. It is not a validation of the folded-Gaussian production matrix.

# Finite-horizon perturbation and block transfer {#sec:perturbation}

Let $(A,X,Y)$ and $(\widetilde A,\widetilde X,\widetilde Y)$ have compatible dimensions. Set $$a_j=\left\lVert A^j\right\rVert_2,
 \qquad \widetilde a_j=\left\lVert \widetilde A^j\right\rVert_2,
 \qquad \delta_A=\left\lVert A-\widetilde A\right\rVert_2,$$ and define $\delta_X=\left\lVert X-\widetilde X\right\rVert_{\mathfrak S_2}$, $\delta_Y=\left\lVert Y-\widetilde Y\right\rVert_2$.

[\[thm:perturbation\]]{#thm:perturbation label="thm:perturbation"} For $m\ge1$, put $$d_m=\delta_A\sum_{j=0}^{m-1}a_{m-1-j}\widetilde a_j,
 \qquad d_0=0.
 \label{eq:dm}$$ Then $$\begin{aligned}
 \left\lVert YA^mX-\widetilde Y\widetilde A^m\widetilde X\right\rVert_{\mathfrak S_2}
 \le b_m:={}&
 \delta_Ya_m\left\lVert X\right\rVert_{\mathfrak S_2}
 +\left\lVert \widetilde Y\right\rVert_2d_m\left\lVert X\right\rVert_{\mathfrak S_2}
 \notag\\
 &+\left\lVert \widetilde Y\right\rVert_2\widetilde a_m\delta_X.
 \label{eq:bm}\end{aligned}$$ Consequently, if $$E_M=\left(\sum_{m=0}^{M-1}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2\right)^{1/2},
 \quad
 \widetilde E_M=\left(\sum_{m=0}^{M-1}
 \left\lVert \widetilde Y\widetilde A^m\widetilde X\right\rVert_{\mathfrak S_2}^2\right)^{1/2},$$ then $$|E_M-\widetilde E_M|
 \le\left(\sum_{m=0}^{M-1}b_m^2\right)^{1/2},
 \label{eq:energy-difference}$$ and $$|E_M^2-\widetilde E_M^2|
 \le(E_M+\widetilde E_M)
 \left(\sum_{m=0}^{M-1}b_m^2\right)^{1/2}.
 \label{eq:squared-difference}$$ Moreover $$\left\lVert A^M-\widetilde A^M\right\rVert_2\le d_M,
 \qquad
 \left\lVert \widetilde A^M\right\rVert_2\le\left\lVert A^M\right\rVert_2+d_M.
 \label{eq:block-transfer}$$ Thus a certified block contraction transfers whenever the final right-hand side is less than one.

Use the exact identity $$A^m-\widetilde A^m
 =\sum_{j=0}^{m-1}A^{m-1-j}(A-\widetilde A)\widetilde A^j$$ to prove [\[eq:dm\]](#eq:dm){reference-type="eqref" reference="eq:dm"}. Insert and subtract $\widetilde YA^mX$ and $\widetilde Y\widetilde A^mX$, then apply ideal and operator norm inequalities to obtain [\[eq:bm\]](#eq:bm){reference-type="eqref" reference="eq:bm"}. Minkowski in the finite time $\ell^2$ space proves [\[eq:energy-difference\]](#eq:energy-difference){reference-type="eqref" reference="eq:energy-difference"}; the identity $|u^2-v^2|=|u-v|(u+v)$ proves [\[eq:squared-difference\]](#eq:squared-difference){reference-type="eqref" reference="eq:squared-difference"}. The final statements are the same telescoping estimate at time $M$.

If $T_M,\widetilde T_M$ are certified tails for the two triples, then $$|\mathcal E^2-\widetilde{\mathcal E}^{\,2}|
 \le |E_M^2-\widetilde E_M^2|+T_M+\widetilde T_M.
 \label{eq:full-transfer}$$ This conservative formula is enough for a sparse-to-full transfer. The use of actual finite-time ledgers $a_j$, rather than $a_j\le\left\lVert A\right\rVert^j$, is essential for nonnormal bulk matrices.

# Gaussian cutoff: a finite-scale yes and asymptotic no

Let $P_h$ be the exact-real full folded-Gaussian midpoint matrix and $P_h^{(L)}$ the row-renormalized hard-cutoff matrix. The archived support half-width is $$H_h=\left\lceil\frac{L\sigma}{h}\right\rceil+2,
 \qquad \Lambda_h=H_hh/\sigma.$$ RH-39 proves the explicit bound $$\left\lVert P_h^{(L)}-P_h\right\rVert_2\le\varepsilon_h,
 \label{eq:cutoff-bound}$$ where $$\begin{aligned}
 Q_h&=
 \frac{2e^{1/2}e^{-\Lambda_h^2/2}}{\sigma-h}
 \left(h+\frac{\sigma}{\Lambda_h}\right),
 &A_h&=\frac{Q_h}{1-Q_h},\\
 \varepsilon_h^2&=
 \frac{4e e^{-\Lambda_h^2}}{(\sigma-h)^2}
 \left(h+\frac{\sigma}{2\Lambda_h}\right)
 +\frac{eA_h^2}{(\sigma-h)^2}
 (4h+2\sqrt\pi\sigma).\end{aligned}$$ These inequalities follow from Gaussian lattice tails and Mills' ratio [@Gordon1941; @WangCutoff2026].

[\[prop:fixed-no-go\]]{#prop:fixed-no-go label="prop:fixed-no-go"} Fix $L,\sigma>0$ with $L\sigma<1$. Along source cells approaching a zero of the quadratic map, $$\liminf_{h\to0}\left\lVert P_h^{(L)}-P_h\right\rVert_\infty
 \ge2\frac{\int_{L\sigma}^{1}e^{-y^2/(2\sigma^2)}\,dy}
 {\int_0^1e^{-y^2/(2\sigma^2)}\,dy}>0.
 \label{eq:fixed-no-go}$$ In particular, fixed $L=8$ does not converge to the canonical full Gaussian family in row-operator norm.

At a zero-mean row the folded density is proportional to $e^{-y^2/(2\sigma^2)}$. Midpoint sums for the full and retained row masses converge to the two displayed integrals; the two extra support cells have vanishing physical width. Row renormalization has exact $\ell^1$ error twice the omitted mass.

[\[thm:adaptive\]]{#thm:adaptive label="thm:adaptive"} Let $$L(h)=\max\{5,2\sqrt{\log(1/h)}\}.
 \label{eq:adaptive}$$ Then $$\left\lVert P_h^{(L(h))}-P_h\right\rVert_2
 =O\!\left(\frac{h^2}{(\log(1/h))^{1/4}}\right).
 \label{eq:adaptive-rate}$$ Suppose the intrinsic triples built from the sparse and full matrices have factor defects $\delta_X,\delta_Y$, semigroup ledgers through $M$, and one of the triples has a block contraction whose transfer bound [\[eq:block-transfer\]](#eq:block-transfer){reference-type="eqref" reference="eq:block-transfer"} is less than one. Then [\[eq:energy-difference\]](#eq:energy-difference){reference-type="eqref" reference="eq:energy-difference"}--[\[eq:full-transfer\]](#eq:full-transfer){reference-type="eqref" reference="eq:full-transfer"} give an explicit full-energy difference upper. In particular, if $M=O(\log(1/h))$ and the finite-time ledgers and factor defects grow slowly enough that the resulting right-hand side vanishes, the sparse Hardy certificate transfers to the canonical full family.

Since $e^{-L(h)^2/2}\le h^2$ and $e^{-L(h)^2}\le h^4$, substitution in [\[eq:cutoff-bound\]](#eq:cutoff-bound){reference-type="eqref" reference="eq:cutoff-bound"} gives [\[eq:adaptive-rate\]](#eq:adaptive-rate){reference-type="eqref" reference="eq:adaptive-rate"}; see RH-39 for the complete lattice proof. The remaining assertions are direct applications of [\[thm:perturbation,thm:block-tail\]](#thm:perturbation,thm:block-tail){reference-type="ref" reference="thm:perturbation,thm:block-tail"}.

This theorem is a route, not a claim that the intrinsic factor defects have already been enclosed. RH-39 controls the Markov matrix before its Perron/parity factors and normalized Haar coupling ranges are recomputed. That factor-aware perturbation is the remaining interface.

# Numerical audit

The dense audit uses the same exact Haar construction as RH-51, with $N\sigma=5.12$, $r=0.85$, and the growing horizons selected there. For each direction we propagate every source column, accumulate [\[eq:main-sum\]](#eq:main-sum){reference-type="eqref" reference="eq:main-sum"}, apply both tails in [\[thm:block-tail\]](#thm:block-tail){reference-type="ref" reference="thm:block-tail"}, and compare with a dense Lyapunov solve. All values in [1](#tab:energy){reference-type="ref" reference="tab:energy"} are binary64 diagnostics.

::: {#tab:energy}
    $\sigma$   $N$   $M$   left exact   left upper   right exact   right upper
  ---------- ----- ----- ------------ ------------ ------------- -------------
        0.16    32     4     0.903958     0.904143      1.002646      1.002892
        0.08    64     8     1.162561     1.163073      1.265281      1.265905
        0.04   128    16     1.333828     1.333960      1.484540      1.484767
        0.02   256    24     1.409582     1.409679      1.633991      1.634149
        0.01   512    32     1.468074     1.468093      1.760310      1.760362

  : Deterministic complete-energy audit. No Hutchinson probes are used.
:::

The worst relative energy excess is $4.94\times10^{-4}$. Every selected block norm is below $0.031$, and the exact Gramian value lies below the certificate at all ten directional instances. This replaces the mechanism of the RH-50 time-64 fit; it does not reproduce the $N=40960$ production trace in interval arithmetic.

::: {#tab:cutoff}
    $\sigma$     $N$   effective $L$   required adaptive $L(h)$         $\varepsilon_h$
  ---------- ------- --------------- -------------------------- -----------------------
      0.0100    2048          8.1055                     5.5225   $1.251\times10^{-13}$
      0.0040    5120          8.1055                     5.8450   $1.978\times10^{-13}$
      0.0020   10240          8.1055                     6.0775   $2.797\times10^{-13}$
      0.0010   20480          8.1055                     6.3015   $3.956\times10^{-13}$
      0.0005   40960          8.1055                     6.5178   $5.594\times10^{-13}$

  : Analytic fixed-eight-sigma cutoff uppers on the RH-50 production scales.
:::

Eight exceeds the sufficient adaptive prescription through $N\le e^{16}\approx8.886\times10^6$, so every stored scale lies safely on the finite side of the crossover. The increase in the last column is a useful warning: tiny is not the same statement as converging to zero at fixed window.

![Deterministic tail and cutoff ledger. Exact dense energies and all-column uppers are visually indistinguishable in panel (a). Panel (b) shows the explicit tail and certificate excess. Panels (c)--(d) separate the finite-scale usefulness of eight sigma from the adaptive canonical route.](<../../../../../zeta_mvp0/papers/RH-53-deterministic-hardy-tail-cutoff/figures/deterministic_hardy_tail_cutoff.pdf>){#fig:audit width="\\textwidth"}

# Program verdict

RH-53 produces four exact advances:

Hutchinson replacement

:   The finite Hilbert--Schmidt trace is an all-column deterministic sum.

Infinite-tail replacement

:   A certified contracting block replaces both the time-64 truncation and its fitted decay base.

Fixed-window no-go

:   Eight sigma is excellent finite-scale engineering but is not a canonical full-Gaussian all-grid definition.

Adaptive positive route

:   The RH-39 $O(h^2)$ cutoff and the finite-time perturbation theorem give a precise sparse-to-full Hardy interface.

The A3 status is nevertheless not "closed." The following distinction is essential:

Analytic finite-matrix mechanism

:   Closed, including a complete small Arb execution.

Exact-real adaptive cutoff route

:   Closed at the Markov matrix level.

Production interval execution

:   Open: the $N=40960$ all-column trace, intrinsic eigendata, and normalized factor perturbations have not been enclosed together.

Uniform Stage A1 budget

:   Open: no theorem yet bounds the certified Hardy energies uniformly or polylogarithmically over the small-noise dyadic family.

Thus the next paper should not declare Stage A4 immediately from the stored numbers. The sharp next target is a factor-aware semigroup perturbation certificate: combine the adaptive matrix cutoff, intrinsic Riesz-factor stability, source/observation normalization, and one growing-horizon block margin. If that certificate can be made uniform, RH-54 may compose the RH-48--RH-53 ledger into the intrinsic identification theorem. If it cannot, the obstruction will identify which factor or transient prevents the route.

Nothing here constructs an arithmetic trace formula, von Mangoldt or prime-power weights, a zeta-zero spectral identity, a canonical self-adjoint operator, or a $T\log T$ counting law. The independent TPC branch studies twin-prime correlations and is not a premise of this theorem.

# Reproducibility

The archive contains source code, unit tests, the five-scale binary64 pilot, the 256-bit Arb audit, the analytic certificate ledger, figures, hashes, and this manuscript. The main commands are

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q
    OPENBLAS_NUM_THREADS=16 OMP_NUM_THREADS=16 \
      PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_deterministic_tail_pilot.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_tail_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_arb_cutoff_ledger.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_tail_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Conclusion

The RH-50 numerical Hardy mechanism can be made deterministic without a full Gramian, random probes, a finite-time truncation assumption, or a fitted tail. A growing block horizon is sufficient. The sparse/full question also has a clean answer: fixed eight sigma is safe for the archived computations but mathematically noncanonical, whereas an adaptive window gives the needed vanishing full-kernel perturbation. The remaining gap is no longer an unspecified tail. It is the concrete production-scale interval and factor-aware transfer of these exact formulas.
