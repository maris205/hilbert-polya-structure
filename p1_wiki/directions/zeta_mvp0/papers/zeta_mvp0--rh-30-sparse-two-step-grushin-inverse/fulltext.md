---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-30-sparse-two-step-grushin-inverse"
canonical_tex: "zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/sparse-two-step-grushin-inverse.pdf"
source_sha256: "69496b6c1aa45f2e8526f4ae5e399f23b03e01aa5736f243790a5eb705b31d9e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sparse Two-Step Grushin Linearization and Deterministic Lifted-Resolvent Closure Two Outward-Rounded Stored-Model Certificates at a Quadratic Band-Merging Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/sparse-two-step-grushin-inverse.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A preceding one-channel deflation reduced an unresolved nonnormal complement-resolvent estimate to a substantially better-conditioned lifted inverse gate. The remaining task was to turn a floating smallest-singular- value candidate into an upper bound. This paper closes that gate at two stored finite scales.

  Let $M$ be the stored sparse one-step transfer matrix, $U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}$ its peripheral-mode-extracted factor, $Q=\mathrm I-VW$ the packet complement, and $\widetilde A=z\mathrm I-QU^2Q+cuv^*$. We introduce the exact two-step linearization $$\mathcal L_t=
   \begin{pmatrix}
    z\mathrm I+cuv^* & -tQU\\
    -t^{-1}UQ & \mathrm I
   \end{pmatrix}.$$ Its leading inverse block is $\widetilde A^{-1}$. Moreover, $M-QU=R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}+V(WU)$ and $M-UQ=R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}+(UV)W$, so $\mathcal L_t$ is a sparse block matrix plus $1+2p+2k$ rank-one channels. Bordering that correction produces a sparse Grushin matrix of dimension $2n+1+2p+2k$ whose first $n$ inverse coordinates again equal $\widetilde A^{-1}$.

  Sparse LU is used only to generate a binary64 approximate right inverse $\mathcal R$. The certificate is independent of the LU backward error: the exact stored-factor graph directly encloses $E=\mathrm I-\widetilde A\mathcal R$ componentwise, while Arb encloses the exact normalization coefficient in the rank-one lift. The elementary estimate $$\left\lVert\widetilde A^{-1}\right\rVert_2
   \leq \frac{\left\lVert\mathcal R\right\rVert_F}{1-\left\lVert E\right\rVert_F}$$ then gives deterministic upper bounds. At $\sigma=10^{-2}$ and $4\times10^{-3}$, respectively, the outward residual bounds are $5.744\times10^{-10}$ and $1.682\times10^{-9}$, and the certified lifted inverse bounds are $108.745$ and $151.491$. The required conditional budgets are $9497.415$ and $34053.573$, leaving factors $87.3$ and $224.8$. Substitution into the preceding exact one-channel theorem gives original center-resolvent bounds $545.053$ and $730.494$, and selected-arc bounds $576.695$ and $746.234$.

  Floating sparse pilots remain favorable through $n=10240$, but the present all-column Frobenius certificate has quadratic-like measured cost. Thus the spectral gate is closed at two selected arcs, while scalable deterministic closure of the remaining scales is left open. No full-contour root count, continuum limit, Hilbert--Pólya construction, statement about zeta zeros, or statement about the Riemann hypothesis is claimed.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Sparse Two-Step Grushin Linearization and\
  Deterministic Lifted-Resolvent Closure**\
  Two Outward-Rounded Stored-Model Certificates\
  at a Quadratic Band-Merging Map
```

## Markdown 正文

**Keywords:** sparse Grushin problem; verified inverse; nonnormal resolvent; low-rank linearization; interval arithmetic; Frobenius--Neumann certificate.

**MSC 2020:** 47A10; 47A55; 65F05; 65F35; 65F50; 65G20; 65P30.

# Introduction {#sec:introduction}

The packet--complement program considered here studies finite noisy transfer matrices near a quadratic band-merging regime. Earlier layers constructed a finite packet Feshbach reduction, a holomorphic shifted Arnoldi model, directional and primal--dual residual formulas, componentwise outward rounding, and an exact adaptive cover of a mathematical contour [@WangContourFeshbach2026; @WangDirectionalRouche2026; @WangPrimalDual2026; @WangOutwardCode2026; @WangArcwise2026]. Those developments reduced a matrix Rouché estimate to one unresolved input: an upper bound for the norm of a nonnormal complement resolvent.

The immediate predecessor isolated one dangerous singular direction and proved an exact one-channel reduction [@WangDeflated2026]. If $A=z_0\mathrm I-B$, if $u,v$ are exact unit vectors obtained by normalizing stored binary64 vectors, and if $$r=Av-\widehat s u,
 \qquad
 q=A^*u-\widehat s v,$$ then the lifted matrix $$\widetilde A=A+(\tau-\widehat s)uv^*
 \label{eq:intro-lift}$$ satisfies the following implication. Any validated $K\geq\|\widetilde A^{-1}\|_2$ in the admissible range gives $$\left\lVert A^{-1}\right\rVert_2
 \leq K+
 \frac{|\tau-\widehat s|(1+K\|r\|_2)(1+K\|q\|_2)}
 {\tau(\widehat s-|\tau-\widehat s|K\|r\|_2)}.
 \label{eq:predecessor-bound}$$ The associated downward budgets $K_*^-$ exceed floating lifted-inverse candidates by factors between $95.0$ and $1.73\times10^3$ across seven stored scales. Simple accretivity cannot close the gate: a certified numerical- range witness places the origin inside the coarse lifted numerical range.

The present paper takes the next route through the maze. It avoids both a dense construction of $QU^2Q$ and a cancellation-free bound on sparse LU triangular factors. The main contributions are:

1.  an exact sparse two-step linearization whose physical inverse block is $\widetilde A^{-1}$;

2.  an explicit factorization with $1+2p+2k$ rank-one channels for every dense-looking correction, including peripheral, packet, and lifted channels;

3.  a direct Frobenius--Neumann certificate that uses sparse LU only to generate an approximate inverse and then rechecks the exact stored target with componentwise outward arithmetic;

4.  rigorous stored-model lifted-inverse bounds at $\sigma=10^{-2}$ and $4\times10^{-3}$, closing the selected RH-28 arc at both scales;

5.  a three-scale sparse audit separating the favorable sparse-factor scaling from the present quadratic-like all-column certification cost.

The distinction between generating and certifying the inverse is essential. No statement relies on treating a computed singular value as a lower bound, and no theorem requires the floating sparse LU factors to be exact. The computed inverse columns are merely stored trial data. The final residual is reevaluated through the same exact stored-factor model used by the preceding outward-rounded papers.

## Evidence hierarchy

Three levels are kept separate.

1.  *Exact algebra*: the Schur-complement identities, low-rank channel factorization, scaling invariances, and Frobenius--Neumann inequality.

2.  *Rigorous stored-model computation*: the two componentwise residual enclosures, exact-normalization intervals, lifted-inverse upper bounds, and their consequences under [\[eq:predecessor-bound\]](#eq:predecessor-bound){reference-type="ref" reference="eq:predecessor-bound"}.

3.  *Floating evidence*: inverse power iterations, full bordered inverse candidates, LU fill ratios, timings, and empirical scaling exponents.

No floating candidate is used as an upper bound in a theorem.

# Stored complement shifts and lifted budgets {#sec:model}

Fix one stored scale and let $n$ be its folded physical dimension. Let $M\in\mathbb C^{n\times n}$ be the stored sparse one-step matrix. The two stored peripheral modes are collected in $R_{\rm p},L_{\rm p}\in\mathbb C^{n\times p}$, with $p=2$, and their values in the diagonal matrix $\Lambda\in\mathbb C^{p\times p}$. Define $$U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}.
 \label{eq:stored-one-step}$$ The packet synthesis and analysis maps are $V\in\mathbb C^{n\times k}$ and $W\in\mathbb C^{k\times n}$, and $$P=VW,
 \qquad
 Q=\mathrm I-P.
 \label{eq:packet-complement}$$ No exact orthogonality assumption is needed below: these formulas use the stored matrices as given.

The physical two-step complement block and its shift are $$B=QU^2Q,
 \qquad
 A(z)=z\mathrm I-B.
 \label{eq:physical-shift}$$ For the budget-tightest archived RH-28 arc, write its disc center and radius as $z_0$ and $\rho$, and abbreviate $A=A(z_0)$.

The archived dangerous vectors $u_0,v_0$ are binary64 arrays. Their exact Euclidean norms, interpreted as norms of exact dyadic vectors, define $$u=\frac{u_0}{\|u_0\|_2},
 \qquad
 v=\frac{v_0}{\|v_0\|_2}.
 \label{eq:exact-normalization}$$ With the stored positive scalar $\widehat s$ and $\tau=1$, put $$c=\tau-\widehat s,
 \qquad
 \widetilde A=z_0\mathrm I-QU^2Q+cuv^*.
 \label{eq:lifted-target}$$ All later rigorous claims refer to this exact finite stored model.

At the two scales certified below, the predecessor provides the downward budgets $$K_*^-=9497.41451992225
 \quad(\sigma=10^{-2}),
 \qquad
 K_*^-=34053.572294052305
 \quad(\sigma=4\times10^{-3}).
 \label{eq:two-budgets}$$ If a rigorous bound $K<K_*^-$ is supplied, then [\[eq:predecessor-bound\]](#eq:predecessor-bound){reference-type="ref" reference="eq:predecessor-bound"} and the archived center-to-arc Neumann transport close the selected arc. The task is therefore precise: certify one lifted inverse norm, not infer a singular gap from a plot.

# Exact sparse two-step Grushin linearization {#sec:linearization}

For any $t>0$, define the $2n\times2n$ block matrix $$\mathcal L_t=
 \begin{pmatrix}
  z_0\mathrm I+cuv^* & -tQU\\
  -t^{-1}UQ & \mathrm I
 \end{pmatrix}.
 \label{eq:two-step-linearization}$$ The parameter $t$ balances the two auxiliary directions without changing the physical inverse block.

[\[lem:physical-schur\]]{#lem:physical-schur label="lem:physical-schur"} The Schur complement of the lower-right identity in [\[eq:two-step-linearization\]](#eq:two-step-linearization){reference-type="ref" reference="eq:two-step-linearization"} is exactly $\widetilde A$. Consequently, $\mathcal L_t$ is invertible if and only if $\widetilde A$ is invertible, and $$_{11}=\widetilde A^{-1}.
 \label{eq:physical-inverse-block}$$

The Schur complement is $$z_0\mathrm I+cuv^*-(-tQU)\mathrm I^{-1}(-t^{-1}UQ)
 =z_0\mathrm I-QU^2Q+cuv^*=\widetilde A.$$ The standard block inverse formula gives [\[eq:physical-inverse-block\]](#eq:physical-inverse-block){reference-type="ref" reference="eq:physical-inverse-block"}.

The point of [\[eq:two-step-linearization\]](#eq:two-step-linearization){reference-type="ref" reference="eq:two-step-linearization"} is that its apparently dense off-diagonal factors are low-rank corrections of $M$. Put $$C_{\rm p}=R_{\rm p}\Lambda.$$ Then exact algebra gives $$\begin{aligned}
 M-QU
 &=C_{\rm p}L_{\rm p}^{\mathsf T}+V(WU),
 \label{eq:top-correction}\\
 M-UQ
 &=C_{\rm p}L_{\rm p}^{\mathsf T}+(UV)W.
 \label{eq:bottom-correction}\end{aligned}$$ Indeed, $QU=U-VWU$ and $UQ=U-UVW$, while $M-U=C_{\rm p}L_{\rm p}^{\mathsf T}$.

Define the sparse base $$\mathcal L_{0,t}=
 \begin{pmatrix}
  z_0\mathrm I& -tM\\
  -t^{-1}M & \mathrm I
 \end{pmatrix}.
 \label{eq:sparse-base}$$ The correction $\mathcal L_t-\mathcal L_{0,t}$ has $r=1+2p+2k$ channels. For completeness, write a column channel as $x=(x_{\rm top},x_{\rm bottom})^{\mathsf T}$ and a row channel as $y=(y_{\rm left},y_{\rm right})$. The channels are: $$\begin{aligned}
 &x_{\rm lift}=(cu,0)^{\mathsf T},
 &&y_{\rm lift}=(v^*,0),\\
 &x_{{\rm tp},j}=(t(C_{\rm p})_j,0)^{\mathsf T},
 &&y_{{\rm tp},j}=(0,(L_{\rm p}^{\mathsf T})_j),\\
 &x_{{\rm tk},j}=(tV_j,0)^{\mathsf T},
 &&y_{{\rm tk},j}=(0,(WU)_j),\\
 &x_{{\rm bp},j}=(0,t^{-1}(C_{\rm p})_j)^{\mathsf T},
 &&y_{{\rm bp},j}=((L_{\rm p}^{\mathsf T})_j,0),\\
 &x_{{\rm bk},j}=(0,t^{-1}(UV)_j)^{\mathsf T},
 &&y_{{\rm bk},j}=(W_j,0).\end{aligned}$$ Collecting the columns and rows into $X\in\mathbb C^{2n\times r}$ and $Y\in\mathbb C^{r\times2n}$ gives $$\mathcal L_t=\mathcal L_{0,t}+XY.
 \label{eq:low-rank-linearization}$$

[\[thm:sparse-grushin\]]{#thm:sparse-grushin label="thm:sparse-grushin"} Let $$\mathcal G_t=
 \begin{pmatrix}
  \mathcal L_{0,t} & X\\
  Y & -\mathrm I_r
 \end{pmatrix}.
 \label{eq:bordered-grushin}$$ Let $J_n:\mathbb C^n\to\mathbb C^{2n+r}$ inject a vector into the first $n$ coordinates. Then $\mathcal G_t$ is invertible if and only if $\widetilde A$ is invertible, and $$J_n^*\mathcal G_t^{-1}J_n=\widetilde A^{-1}.
 \label{eq:grushin-physical-block}$$ The bordered dimension is $2n+1+2p+2k$.

The Schur complement of $-\mathrm I_r$ in [\[eq:bordered-grushin\]](#eq:bordered-grushin){reference-type="ref" reference="eq:bordered-grushin"} is $\mathcal L_{0,t}+XY=\mathcal L_t$. Hence the leading $2n$ block of $\mathcal G_t^{-1}$ is $\mathcal L_t^{-1}$. Apply [\[lem:physical-schur\]](#lem:physical-schur){reference-type="ref" reference="lem:physical-schur"} to its first $n$ coordinates.

[\[prop:balancing\]]{#prop:balancing label="prop:balancing"} Let $D$ be any invertible diagonal $r\times r$ matrix. Replacing $X,Y$ by $XD,D^{-1}Y$ leaves [\[eq:grushin-physical-block\]](#eq:grushin-physical-block){reference-type="ref" reference="eq:grushin-physical-block"} unchanged. Likewise, changing $t>0$ leaves the physical inverse block unchanged.

The channel transformation preserves $XY$ and is the similarity $$\begin{pmatrix}\mathrm I&0\\0&D^{-1}\end{pmatrix}
 \mathcal G_t
 \begin{pmatrix}\mathrm I&0\\0&D\end{pmatrix}.$$ For the auxiliary scale, with $S_t=\operatorname{diag}(t\mathrm I_n,\mathrm I_n)$, $\mathcal L_t=S_t\mathcal L_1S_t^{-1}$, whose leading inverse block equals that of $\mathcal L_1^{-1}$.

In the implementation, every rank-one channel is balanced by multiplying its column by the square root of the row-to-column norm ratio and dividing its row by the same number. This changes the norm of the full bordered inverse but not its physical block.

# A direct Frobenius--Neumann certificate {#sec:certificate}

The sparse Grushin matrix provides an efficient *generator* for an approximate inverse. It need not itself be promoted to exact arithmetic. Let $\widehat{\mathcal G}_t$ denote its binary64 assembly and sparse LU factorization. Solving $$\widehat{\mathcal G}_t x_j=J_ne_j,
 \qquad j=1,\dots,n,$$ and retaining the first $n$ coordinates gives a stored matrix $$\mathcal R=[J_n^*x_1\ \cdots\ J_n^*x_n].
 \label{eq:approximate-right-inverse}$$ Rounding in the Grushin assembly and LU solve affects only the quality of $\mathcal R$; it does not affect the validity of the next theorem.

[\[thm:frobenius-neumann\]]{#thm:frobenius-neumann label="thm:frobenius-neumann"} Let $T,R\in\mathbb C^{n\times n}$. Suppose outward bounds $\rho,\varepsilon$ satisfy $$\left\lVert R\right\rVert_F\leq\rho,
 \qquad
 \left\lVert\mathrm I-TR\right\rVert_F\leq\varepsilon<1.
 \label{eq:neumann-inputs}$$ Then $T$ is invertible and $$\left\lVert T^{-1}\right\rVert_2
 \leq \frac{\rho}{1-\varepsilon}.
 \label{eq:frobenius-neumann}$$

Set $E=\mathrm I-TR$. Since $\|E\|_2\leq\|E\|_F<1$, the matrix $\mathrm I-E$ is invertible and $$T\bigl(R(\mathrm I-E)^{-1}\bigr)=\mathrm I.$$ A square matrix with a right inverse is invertible. Therefore $T^{-1}=R(\mathrm I-E)^{-1}$, and $$\left\lVert T^{-1}\right\rVert_2
 \leq \left\lVert R\right\rVert_2\frac{1}{1-\left\lVert E\right\rVert_2}
 \leq \frac{\left\lVert R\right\rVert_F}{1-\left\lVert E\right\rVert_F}.$$ Apply [\[eq:neumann-inputs\]](#eq:neumann-inputs){reference-type="ref" reference="eq:neumann-inputs"}.

The Frobenius norm is intentionally conservative. It replaces a difficult global spectral upper bound by a deterministic all-column calculation. The large RH-29 budgets make this trade useful at the first two scales.

## Outward stored-factor residual

The exact target in the certificate is $T=\widetilde A$ from [\[eq:lifted-target\]](#eq:lifted-target){reference-type="ref" reference="eq:lifted-target"}, not the rounded Schur complement of $\widehat{\mathcal G}_t$. Each binary64 input is interpreted as an exact dyadic number. The stored-factor graph evaluates, for a componentwise complex-disc ball $X$, $$X\longmapsto z_0X-Q\bigl(U(U(QX))\bigr)+cuv^*X
 \label{eq:stored-factor-action}$$ with one outward radius per output entry. Sparse and dense dot products use conservative Higham $\gamma_k$ factors under the usual IEEE round-to-nearest model [@Higham2002; @Rump2010]. Positive radius products are divided by a downward-rounded $1-\gamma_k$ before a final upward step.

The coefficient multiplying the stored vectors is $$\frac{\tau-\widehat s}{\|u_0\|_2\|v_0\|_2}.
 \label{eq:normalized-coefficient}$$ Its exact dyadic numerator and exact norms are enclosed at 160-bit precision with Arb [@Johansson2017]; the resulting interval is propagated through the rank-one action. Thus exact normalization is not silently replaced by binary64 normalization.

Columns are processed in chunks. If $\rho_j$ and $\varepsilon_j$ are outward Frobenius bounds for the approximate inverse and residual in chunk $j$, then $$\rho=\operatorname{up}\sqrt{\sum_j\rho_j^2},
 \qquad
 \varepsilon=\operatorname{up}\sqrt{\sum_j\varepsilon_j^2}
 \label{eq:chunk-combination}$$ are valid global bounds. The archived implementation applies an upward step after each nonnegative addition, multiplication, and square root.

The LU factors can contain large cancellations. Entrywise comparison triangular bounds discard those cancellations and can be useless even when the inverse is moderate. In the present route, LU only proposes $\mathcal R$. Every error in that proposal is measured by the direct exact-target residual $\mathrm I-\widetilde A\mathcal R$ and absorbed by [\[thm:frobenius-neumann\]](#thm:frobenius-neumann){reference-type="ref" reference="thm:frobenius-neumann"}.

# Floating sparse audit {#sec:floating-audit}

Before the all-column calculation, we test whether the bordered inverse is numerically compatible with the RH-29 budgets. These calculations are floating diagnostics only. SuperLU with COLAMD ordering factors $\widehat{\mathcal G}_t$, and inverse-normal power iteration is applied both to the physical block $J_n^*\widehat{\mathcal G}_t^{-1}J_n$ and to the full bordered inverse. Sparse direct methods and their fill behavior are discussed in [@Davis2006; @GolubVanLoan2013].

At $\sigma=10^{-2}$, the auxiliary scales $t=0.25,0.5,1,2,4$ give full bordered inverse candidates approximately $41.36,25.78,21.19,24.86,43.48$. Thus $t=1$ is the best of this small scan. The physical candidate is invariant to the displayed precision, as required by [\[prop:balancing\]](#prop:balancing){reference-type="ref" reference="prop:balancing"}.

::: {#tab:sparse-pilot}
            $\sigma$     $n$   $\dim\mathcal G$   $\operatorname{nnz}\mathcal G$   fill   LU (s)   physical cand.   full cand.   budget/full
  ------------------ ------- ------------------ -------------------------------- ------ -------- ---------------- ------------ -------------
           $10^{-2}$    2048               4109                $1.295\times10^6$   3.48     2.78            15.93        21.19           448
    $4\times10^{-3}$    5120              10255                $3.387\times10^6$   4.12    12.28            29.36        41.09           829
    $2\times10^{-3}$   10240              20497                $6.934\times10^6$   5.39    52.60            62.93        89.44           992

  : Floating sparse-LU audit at $t=1$. The final column is the ratio of the rigorous RH-29 lifted budget to the *floating* full bordered inverse candidate. It is a feasibility diagnostic, not a certificate.
:::

The physical inverse candidates reproduce the independent lifted values from RH-29. More importantly, the full bordered inverse remains only a modest factor above the physical block and hundreds of times below the available budget. Therefore certifying the full border would not be ruled out by norm inflation, although the direct physical residual route is sharper.

![Floating three-scale sparse audit. Left: stored matrix and LU nonzeros. Right: physical and full inverse candidates compared with the rigorous lifted budgets. The lines summarize three finite data points and are not asymptotic theorems.](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/figures/sparse_grushin_scaling.pdf>){#fig:sparse-scaling width="98%"}

Power-law fits over only these three points give exponents $1.043$ for $\operatorname{nnz}\mathcal G$, $1.310$ for LU nonzeros, and $1.817$ for LU wall time. These empirical values show that sparse generation remains practical through $n=10240$ on the present machine. They do not predict the finest stored scales.

# Two rigorous stored-model closures {#sec:rigorous-results}

We now apply [\[thm:frobenius-neumann\]](#thm:frobenius-neumann){reference-type="ref" reference="thm:frobenius-neumann"} to every physical column at the first two stored scales. The sparse Grushin solve uses $t=1$ and balanced channels. The exact target residual is then recomputed by [\[eq:stored-factor-action\]](#eq:stored-factor-action){reference-type="ref" reference="eq:stored-factor-action"}; 256 columns are processed per chunk in the archived runs.

::: {#tab:rigorous-certificates}
            $\sigma$    $n$       $\rho$           $\varepsilon$          $K$   $K_*^-/K$   $\|A(z_0)^{-1}\|_2$   selected arc   time (s)
  ------------------ ------ ------------ ----------------------- ------------ ----------- --------------------- -------------- ----------
           $10^{-2}$   2048   108.744783   $5.744\times10^{-10}$   108.744783        87.3               545.053        576.695       32.1
    $4\times10^{-3}$   5120   151.490497    $1.682\times10^{-9}$   151.490497       224.8               730.494        746.234      240.1

  : Outward-rounded stored-model inverse certificates. Here $\rho\geq\|\mathcal R\|_F$, $\varepsilon\geq\|\mathrm I-\widetilde A\mathcal R\|_F$, and $K=\rho/(1-\varepsilon)$. The last two columns follow from the exact one-channel formula and center-to-arc transport of RH-29.
:::

[\[thm:computer-closure\]]{#thm:computer-closure label="thm:computer-closure"} Assume the archived binary64 factors are exact inputs and IEEE round-to-nearest arithmetic has no overflow or harmful underflow. At $\sigma=10^{-2}$, $$\left\lVert\widetilde A^{-1}\right\rVert_2<108.745,
 \qquad
 \left\lVert A(z_0)^{-1}\right\rVert_2<545.053,
 \qquad
 \sup_{z\text{ in selected arc}}\left\lVert A(z)^{-1}\right\rVert_2<576.695.
 \label{eq:coarse-certified}$$ At $\sigma=4\times10^{-3}$, $$\left\lVert\widetilde A^{-1}\right\rVert_2<151.491,
 \qquad
 \left\lVert A(z_0)^{-1}\right\rVert_2<730.494,
 \qquad
 \sup_{z\text{ in selected arc}}\left\lVert A(z)^{-1}\right\rVert_2<746.234.
 \label{eq:mid-certified}$$ In particular, the RH-29 lifted budgets and the corresponding selected-arc resolvent gates are rigorously satisfied at both scales.

At $\sigma=10^{-2}$, the archived outward computation gives $$\left\lVert\mathcal R\right\rVert_F\leq108.74478206784087,
 \qquad
 \left\lVert\mathrm I-\widetilde A\mathcal R\right\rVert_F
 \leq5.743634700225225\times10^{-10}.$$ At $\sigma=4\times10^{-3}$, it gives $$\left\lVert\mathcal R\right\rVert_F\leq151.4904965112043,
 \qquad
 \left\lVert\mathrm I-\widetilde A\mathcal R\right\rVert_F
 \leq1.6813946390231736\times10^{-9}.$$ Apply [\[thm:frobenius-neumann\]](#thm:frobenius-neumann){reference-type="ref" reference="thm:frobenius-neumann"}; outward division yields $108.74478213029992$ and $151.49049676591966$. These are below the downward budgets in [\[eq:two-budgets\]](#eq:two-budgets){reference-type="ref" reference="eq:two-budgets"}. Substituting them, together with the archived normalized right and left residual majorants, into the exact outward implementation of [\[eq:predecessor-bound\]](#eq:predecessor-bound){reference-type="ref" reference="eq:predecessor-bound"} gives center bounds $545.0520168716026$ and $730.4936951203142$. The archived arc radii and an outward Neumann transport give $576.69452966032$ and $746.2336551496244$. Rounding the displayed theorem bounds upward proves [\[eq:coarse-certified,eq:mid-certified\]](#eq:coarse-certified,eq:mid-certified){reference-type="ref" reference="eq:coarse-certified,eq:mid-certified"}.

![Left: floating physical candidates, rigorous Frobenius--Neumann upper bounds, and required RH-29 budgets. Right: outward residuals remain far below one, while the deterministic all-column wall time grows rapidly.](<../../../../../zeta_mvp0/papers/RH-30-sparse-two-step-grushin-inverse/figures/stored_inverse_closure.pdf>){#fig:rigorous-closure width="98%"}

The certified upper bounds are roughly $6.8$ and $5.2$ times the floating spectral candidates. This gap is the price of replacing the spectral norm of the approximate inverse by its Frobenius norm. The available budgets are large enough that the conservative replacement still succeeds decisively.

At the coarse scale, repeating the full calculation with 128 rather than 256 columns per chunk changes the final lifted bound by less than $4\times10^{-9}$. This is a reproducibility cross-check, not an additional ingredient in the proof.

# The remaining scaling barrier {#sec:scaling-barrier}

The result is positive but deliberately partial. Sparse factorization is not yet the bottleneck: at $n=10240$, the bordered factorization uses about $1.15$ GiB peak resident memory in the floating pilot and retains a full inverse candidate margin near $10^3$. The expensive step is instead the deterministic Frobenius certificate, which solves and outwardly rechecks all $n$ physical columns.

Between $n=2048$ and $n=5120$, the measured certificate time grows from $32.1$ to $240.1$ seconds, a two-point exponent $2.20$. This is consistent with a quadratic-like all-column workload on the tested range. It is a limitation of the present certificate, not evidence that the lifted inverse bound fails at smaller noise.

Several next routes preserve the exact sparse linearization while avoiding all columns:

1.  a verified sparse Hermitian-inertia test at the threshold $K_*^{-1}$, using a symmetry-preserving indefinite factorization;

2.  a hierarchical or block-local approximate inverse with a deterministic tail bound for omitted columns;

3.  selected inversion combined with an operator-decay estimate;

4.  a multilevel Grushin decomposition that replaces one ambient Frobenius norm by certified norms of smaller diagonal blocks and a low-rank coupling matrix.

The first route tests the desired singular threshold directly. The other three attempt to exploit locality and low rank. None is assumed here.

# Scope and limitations {#sec:limitations}

The exact achievements are:

1.  a sparse two-step Grushin linearization with an exact physical inverse block;

2.  an explicit $1+2p+2k$-channel correction formula and free balancing parameters;

3.  a direct exact-target Frobenius--Neumann certificate;

4.  rigorous selected-arc stored-model closures at two scales.

The following are not proved.

1.  Only the budget-tightest selected arc is closed at each of two scales. Other arcs and the remaining five stored scales are not certified.

2.  Therefore no full-contour matrix Rouché theorem or root count follows from this paper alone.

3.  The stored sparse transfer matrices are not enclosed relative to an exact Gaussian integral operator, exact critical constants, or a zero-noise continuum limit.

4.  The work does not construct a self-adjoint Hilbert--Pólya operator, identify zeta zeros as eigenvalues, prove a prime-power trace formula, or imply any statement about the Riemann hypothesis.

The result should therefore be read as a finite-dimensional certified resolvent advance. It removes one genuine conditional gate at two scales and identifies the next computational-mathematical barrier without extrapolating past it.

# Conclusion {#sec:conclusion}

One-channel lifting created a large gap between the inverse bound required by the contour argument and the observed lifted inverse. The present paper turns part of that gap into theorem. A two-step auxiliary state keeps the physical square $QU^2Q$ out of the sparse matrix, while peripheral and packet corrections enter through only $1+2p+2k$ border channels. Sparse LU then produces an approximate inverse whose exact stored-target residual can be checked independently.

At the first two stored scales, the conservative Frobenius--Neumann bound is already far below the available lifted budget, so the selected complement- resolvent arcs close rigorously. The next problem is no longer whether the sparse linearization has enough numerical margin. It is how to certify that margin without processing every physical column. That is a narrower and more structured next gate.

# Implementation checks {#app:checks}

The unit tests verify three exact identities on independent synthetic matrices:

1.  the first $n\times n$ block of $\mathcal G_t^{-1}$ equals $\widetilde A^{-1}$;

2.  channel balancing preserves $XY$;

3.  changing $t$ preserves the physical inverse block.

Two additional tests verify the Frobenius block-combination formula and the Neumann inverse bound against a directly inverted small matrix.

The archived certificate stores SHA-256 hashes of the dangerous triplet, the generated approximate inverse stream, the residual centers and radii, the linearization and certification sources, the componentwise outward arithmetic, the RH-29 scalar algebra, and the RH-29 scale summary.

# Reproduction {#app:reproduction}

From the RH-30 directory, the principal commands are

    PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
      python experiments/run_sparse_grushin_pilot.py \
      --sigma 1e-2 --auxiliary-scales 0.25 0.5 1 2 4 --iterations 30

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
      python experiments/run_stored_inverse_certificate.py \
      --sigma 1e-2 --chunk-size 256

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
      python experiments/run_stored_inverse_certificate.py \
      --sigma 4e-3 --chunk-size 256

    MPLCONFIGDIR=/tmp/rh30-mpl python experiments/make_figures.py

The certificates assume finite intermediates, no overflow, no harmful underflow, and the standard round-to-nearest model used by the outward-error constants. Sparse LU output can vary slightly across SuperLU builds; this does not invalidate the method because the resulting stored trial inverse is rechecked directly.
