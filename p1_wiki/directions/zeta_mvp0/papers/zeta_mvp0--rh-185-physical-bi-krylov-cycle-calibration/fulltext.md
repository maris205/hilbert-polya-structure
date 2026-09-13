---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-185-physical-bi-krylov-cycle-calibration"
canonical_tex: "zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration/main.pdf"
source_sha256: "d45aa623eabf8cde1ed03d7fa46dc50f7615f2877536089131e7b2b2c4c31199"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Physical Bi-Krylov Cycle Calibration A Local Length-Four Candidate, Two Directed Residuals, and the Cross-Angle Price

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-185-physical-bi-krylov-cycle-calibration/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-182--183 reject a single orthogonal temporal range. RH-184 replaces it by balanced right and left frames generated from two subspaces. This paper instantiates that construction on the actual physical source and observation orbits.

  At each admissible anchor, the right temporal synthesis is formed from $A^jS$ and the left synthesis from $(A^*)^jO^*$, with independent Frobenius normalization. Candidate lengths are still fixed by $L=r-3$ and $L=r-4$. The balanced cross-Gram construction gives biorthogonal frames $V,W$, the Petrov--Galerkin compression $K=W^*AV$, and directed residuals $AV-VK$ and $A^*W-WK^*$. No target eigenvector is used.

  The audit covers the same 126 windows as RH-182. Every balanced pair is biorthogonal to numerical precision. No length-three window passes a common $0.10$ two-sided relative-residual gate. At the only reset/cloud overlap, $\sigma=0.01$ and $L=4$, twelve of 38 windows pass: five on the left channel and seven on the right. The best residual pair is $(0.02332,0.02498)$. In the accepted late windows the compressed phase-grid RMS error is about $0.095$--$0.099$ and the radial RMS error is about $0.03$--$0.05$.

  This is the first local physical candidate linking the predeclared clock length $L=4$ to a two-sided nonnormal temporal packet. It is not yet a Riesz certificate. The smallest cross singular values are only about $10^{-3}$--$5\times10^{-3}$ in the accepted windows, so the optimal oblique condition number is roughly $194$--$960$. Across all windows it ranges from $48.2$ to $4.33\times10^5$.

  Thus cycle calibration advances locally while conditioning becomes the next wall. No uniform scale theorem, validated contour inverse, physical Riesz shell, Gate A, Hilbert--Polya, or RH conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Physical Bi-Krylov Cycle Calibration\
  A Local Length-Four Candidate, Two Directed Residuals, and the Cross-Angle Price
```

## Markdown 正文

# The physical right and left histories

For each frozen physical model let $A$ act by left multiplication on the Frobenius Hilbert space of source matrices. The model supplies a source $S$ and an observation $O$. Define normalized right and left orbits $$\begin{aligned}
 x_j&=\frac{A^jS}{\left\lVert A^jS\right\rVert_{\mathrm F}},
 \label{eq:right-orbit}\\
 y_j&=\frac{(A^*)^jO^*}{\left\lVert(A^*)^jO^*\right\rVert_{\mathrm F}}.
 \label{eq:left-orbit}\end{aligned}$$ For a start $t$ and length $L$, vectorize the matrices and set $$\label{eq:syntheses}
 J_R=[x_t,\ldots,x_{t+L-1}],
 \qquad
 J_L=[y_t,\ldots,y_{t+L-1}].$$

QR factorization gives orthonormal frames $Q_R,Q_L$. If $H=Q_L^*Q_R$ is invertible, RH-184 supplies the balanced pair $$\label{eq:balanced}
 V=Q_RV_H\Sigma^{-1/2},
 \qquad
 W=Q_LU_H\Sigma^{-1/2},
 \qquad W^*V=I,$$ where $H=U_H\Sigma V_H^*$ [@WangRH184].

The procedure uses no target transfer eigenvectors. It uses both physical directions that were already present in the source/observation model.

# Two directed residuals and compressed clock

Define $$\begin{aligned}
 K&=W^*AV,
 \label{eq:K}\\
 R_R&=AV-VK,
 \label{eq:RR}\\
 R_L&=A^*W-WK^*.
 \label{eq:RL}\end{aligned}$$ Because $W^*V=I$, these are the exact right and left Petrov--Galerkin residuals. Their relative forms are $$\label{eq:relative}
 \epsilon_R=\frac{\left\lVert R_R\right\rVert}{\left\lVert AV\right\rVert},
 \qquad
 \epsilon_L=\frac{\left\lVert R_L\right\rVert}{\left\lVert A^*W\right\rVert}.$$ The declared local residual gate is $$\label{eq:gate}
 \epsilon_R\le0.10,
 \qquad
 \epsilon_L\le0.10.$$

The residuals satisfy the exact Petrov--Galerkin orthogonality relations $$\label{eq:petrov-orthogonality}
 W^*R_R=0,
 \qquad
 V^*R_L=0.$$ Indeed, $W^*R_R=W^*AV-K=0$, and the second identity is its adjoint analogue. Thus the two recorded norms measure leakage into the two directed complements; they are not contaminated by a remaining least-squares error inside the packet coordinates.

The smallest singular value $$\label{eq:sigma-cross}
 \gamma=\sigma_{\min}(Q_L^*Q_R)$$ is also recorded. The exact optimal oblique condition number is $$\label{eq:chi}
 \chi=\left\lVert VW^*\right\rVert=\gamma^{-1}.$$

# Predeclared cycle geometry

Candidate lengths remain $$\label{eq:lengths}
 L\in\{r-3,r-4\},\qquad L\ge3.$$ The right source orbit determines the radius and orientation mark $$\begin{aligned}
 \rho_{t,L}
 &=\left(\frac{\left\lVert A^{t+L}S\right\rVert_{\mathrm F}}
 {\left\lVert A^tS\right\rVert_{\mathrm F}}\right)^{1/L},
 \label{eq:radius}\\
 \omega_{t,L}
 &=\frac{\langle x_t,x_{t+L}\rangle}
 {|\langle x_t,x_{t+L}\rangle|}.
 \label{eq:mark}\end{aligned}$$ The ideal weighted cycle has the $L$ roots of $z^L=\omega_{t,L}\rho_{t,L}^L$. The eigenvalues of $K$ are compared with that grid by optimal finite matching. We record phase RMS and radial RMS errors separately. Unlike RH-182, the spectrum of $K$ is not forced to be the exact grid; agreement is now physical information.

# Audit design

The admissible groups are the same as in RH-182:

   $\sigma$   rank $r$   candidate $L$   number of groups
  ---------- ---------- --------------- ------------------
    $0.04$       6             3                2
    $0.02$       6             3                2
    $0.01$       7            3,4               4

There are 126 start/side/length windows. Every window records the full cross-singular-value ledger, frame norms, biorthogonality defect, absolute and relative residuals, compressed eigenvalues, phase and radial errors, and the source-derived cycle radius.

Independent normalization of the history columns is a numerical choice, not a fitted spectral degree of freedom. Replacing either synthesis by the same columns times an invertible diagonal matrix leaves its column space unchanged. The balanced frames may change gauge, but the oblique projector and the similarity class of $K$ do not. Consequently the phase and radial comparison is attached to the two temporal subspaces, while normalization only controls how reliably those subspaces are computed.

# Length-three rejection

No length-three window passes [\[eq:gate\]](#eq:gate){reference-type="eqref" reference="eq:gate"}. The groupwise minimum residuals remain large:

   $\sigma$   side    $\min\epsilon_R$   $\min\epsilon_L$   $\min\chi$
  ---------- ------- ------------------ ------------------ ------------
    $0.04$    left        $0.8842$           $0.9027$         $48.2$
    $0.04$    right       $0.8656$           $0.8355$         $52.5$
    $0.02$    left        $1.5479$           $1.4280$        $225.1$
    $0.02$    right       $1.1105$           $1.1417$        $304.0$
    $0.01$    left        $0.9627$           $1.0443$        $203.5$
    $0.01$    right       $0.8064$           $0.9656$        $290.9$

Thus the alternative offset-four calibration $L=r-4=3$ is not supported at the only cloud/reset overlap.

# The local length-four candidate

For $\sigma=0.01,L=4$, there are 19 starts in each channel. The summary is

   side    windows   gate passes   $\min\epsilon_R$   $\min\epsilon_L$   median $\chi$
  ------- --------- ------------- ------------------ ------------------ ---------------
   left      19           5           $0.05286$          $0.04033$          $195.1$
   right     19           7           $0.02332$          $0.02498$          $956.8$

All twelve accepted windows occur late in the finite horizon. On the left they begin at $t=14,\ldots,18$; on the right at $t=12,\ldots,18$. The best right-channel pair at $t=18$ is $$\label{eq:best-pair}
 (\epsilon_R,\epsilon_L)
 =(0.0233225,0.0249804).$$ Its source-cycle radius is $0.79449$, compressed phase RMS error is $0.09817$, and radial RMS error is $0.04531$.

The best left-channel pair is $(0.05286,0.04033)$ at $t=18$, with phase error $0.09506$ and radial error $0.04104$. Across the accepted windows, the phase error remains close to $0.1$ radians and the radial error stays at a few hundredths. This is a nontrivial local resemblance to the predeclared four-cycle, but not an exact spectral identification.

# The conditioning price

The local candidate is strongly oblique. In the accepted left windows, $\gamma$ is about $0.005$, so $\chi$ is about $194$--$202$. In the accepted right windows, $\gamma$ is about $0.00105$, so $\chi$ is about $920$--$961$. Across all 126 windows, $$\label{eq:conditioning-range}
 48.22\le\chi\le4.3273\times10^5.$$ The underlying principal angles are therefore close to $90^\circ$.

Small relative residuals do not erase this price. The oblique projector and coordinate maps can amplify operator balls, frame errors, and resolvent estimates. The next paper must insert [\[eq:chi\]](#eq:chi){reference-type="eqref" reference="eq:chi"} into the Riesz budget before treating the twelve windows as physical shells.

# Calibration consequence

At the only actual overlap with the RH-15 cloud and RH-151 reset atlas, the two predeclared candidates behave differently: $$\label{eq:calibration-choice}
 L=3:\ 0\text{ passes},
 \qquad
 L=4:\ 12\text{ local passes}.$$ Thus $L=4=N+1=r-3$ becomes the unique surviving local calibration in this finite experiment. This does not prove an asymptotic degree law or authorize choosing $L=4$ at scales not represented in the reset atlas.

The result also clarifies the role of the observation. The one-space orthogonal route has minimum adjoint residual $0.7143$; the balanced source/observation pair lowers both directed residuals below $0.1$ in a coherent late-time block. Separate left information is essential.

# Selection logic and finite robustness

Three filters must be kept distinct:

1.  the rank offsets declare which lengths are admissible;

2.  the two residual inequalities select local Petrov--Galerkin packets;

3.  phase and radial errors diagnose whether the selected compression resembles the predeclared cycle geometry.

The spectral errors were not used to choose the twelve residual passes. This prevents a favorable eigenvalue plot from compensating for a failed two-sided packet equation.

The accepted windows form contiguous late-time blocks in both channels, rather than isolated single starts. That coherence is the main reason to retain the branch as a candidate. It is still only finite coherence. The windows overlap heavily, share the same frozen matrix, and are therefore not independent statistical observations. Their role is deterministic model selection: they identify where a later validated contour calculation should be attempted first.

The conditioning ledger also prevents overinterpretation. A residual pair near $0.025$ and a condition number near $950$ cannot be combined by simply calling both "small." Any outward perturbation of the cross Gram, source, observation, or operator must be transported through the oblique coordinates. RH-186 therefore tests a sufficient conditioned gate before the local phase agreement is promoted to a shell claim.

# What a successful continuation must preserve

A continuation of the $L=4$ branch should keep the present choices frozen: the same source/observation construction, start windows, orientation mark, and root contours. It may add outward error balls and complement inverses, but it should not refit $L$, rotate the target grid after seeing $K$, or discard one of the directed residuals. Under those rules a positive Schur margin would be new information, while a failure would be a clean rejection of this local candidate rather than an ambiguous change of model.

This also explains why the result is called a calibration. It chooses the first physically motivated finite target for a harder proof; it does not yet establish that the target survives perturbation, scale transport, or the continuum limit.

# Boundary and next target

This paper supplies a finite floating candidate for the ambient realization leaf at one scale and one length. It does not prove:

-   a uniform lower bound on the cross singular value;

-   an outward enclosure of the residuals or frames;

-   a complement resolvent on a root contour;

-   a Schur product below one after all conditioning factors;

-   shellwise transport across scales;

-   physical interface R or Gate A.

The next step is therefore not to declare a physical spectrum. It is to quantify the exact oblique amplification and test whether any Riesz budget survives it.

No self-adjoint operator, Hilbert--Polya identification, zeta divisor, or Riemann-hypothesis conclusion is claimed.
