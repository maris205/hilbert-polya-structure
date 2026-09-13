---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-211-ten-layer-transport-frontier-review"
canonical_tex: "zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review/main.pdf"
source_sha256: "a0117d987de17cb499cb3b2ec1287faeaf3e291786cbc6e4ca010b1361dfd9f5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ten Layers at the Cross-Scale Transport Frontier RH-202--RH-210 Review and the Divisor-First Gate-A Route

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-211-ten-layer-transport-frontier-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This paper reviews RH-202--RH-210, a nine-paper investigation of whether the finite source-observable edge quartet can be transported across small-noise levels. The literal answer is negative: the dyadic Haar map has right/left principal sines up to $0.82388$, oblique-projector defect up to $2.29068$, and residue displacement up to $8.18374$. Enlarging the top-modulus cloud through rank 32 gives no two-sided angle-gate pass.

  The batch also identifies what survives. A rectangular resolvent identity and two-term source-channel budget are proved exactly. All four adjacent quartets have unique conjugate branch correspondences, with left/right branch mismatch at most $0.007578$. Endpoint spectral isolation is numerically feasible in all six packets, although naive transport certification fails in all four transitions. The unweighted quartic divisor agrees between physical channels to relative coefficient error at most $0.008112$, while the physical residues require a branch-dependent, source-dependent cocycle.

  An exact rotating-similarity counterexample shows that divisor stability does not require raw projector stability. The revised coordinate is a finite dual-channel divisor flow with its intrinsic renormalization still open. The aggregate reproducibility ledger contains 649 finite items and zero identity failures. Gate A remains open; Gates B--E, Hilbert--Pólya, zeta-zero identification, and RH are untouched.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Ten Layers at the Cross-Scale Transport Frontier\
  RH-202--RH-210 Review and the Divisor-First Gate-A Route
```

## Markdown 正文

# Coordinate inherited from RH-201

RH-201 ended with a corrected source-relative state type and a canonical finite outer-edge quartet [@WangRH201]. The next declared wall was a cross-level map carrying Riesz projectors, source/observation states, residues, and determinant data between $\sigma=0.04,0.02,0.01$.

The new batch answers that question in layers. It does not force one binary verdict on every object. Instead it separates three ledgers: $$\label{eq:ledgers}
 \begin{aligned}
 Q&=\text{spectral branches, divisors, unweighted traces},\\
 R&=\text{right/left states, Riesz projectors, transport maps},\\
 W&=\text{source--observation residues and weighted moments}.
 \end{aligned}$$ The central discovery is that these ledgers have different stability.

# Layer-by-layer result

  paper    principal result                                                      strict status
  -------- --------------------------------------------------------------------- --------------------------
  RH-202   direct Haar quartet transport has order-one state/projector defects   finite negative
  RH-203   resolvent, Riesz, and two-term channel transport identities           exact theorems
  RH-204   unique two-branch correspondence and left/right synchronization       finite positive
  RH-205   optimal endpoint partial isometry; predictivity gap                   exact + finite cost
  RH-206   scalar residue renormalization fails; diagonal cocycle survives       exact + finite negative
  RH-207   dual-channel quartic coherence; nonstationary scale flow              exact + finite mixed
  RH-208   endpoint validation feasible; naive homotopy budget fails             finite feasibility split
  RH-209   top-modulus cloud enlargement through rank 32 fails                   finite negative
  RH-210   divisor stability need not imply projector stability; route pivot     exact counterexample

# The naive shell map is rejected finitely

Let $J$ be the dyadic Haar embedding. RH-202 compares adjacent packet spaces and projectors [@WangRH202]. The four transition/channel cases give $$\label{eq:state-negative}
 \max\sin\theta_R=0.82175,
 \qquad \max\sin\theta_L=0.82388,
 \qquad \max\frac{\left\lVert P_f-JP_cJ^*\right\rVert_F}{\left\lVert P_f\right\rVert_F}=2.29068.$$ The quartet-restricted intertwining defect reaches $0.65573$. Source defects are at least $0.78134$, and one relative residue displacement is $8.18374$.

This rejects one concrete equation: $$\text{fine packet}=\text{Haar lift of coarse packet}+\text{small error}.$$ It does not reject the endpoint quartets or all possible renormalized maps.

# Exact anatomy of transport

RH-203 proves, for $E=A_fJ-JA_c$, $$\label{eq:resolvent}
 R_f(z)J-JR_c(z)=R_f(z)ER_c(z)$$ and integrates it to $$\label{eq:projector}
 P_fJ-JP_c=\frac{1}{2\pi i}\int_\Gamma R_f(z)ER_c(z)\,dz$$ [@WangRH203]. For source matrices and a column embedding $K$, $$\label{eq:channel}
 P_fS_f-JP_cS_cK^*
 =P_f(S_f-JS_cK^*)+(P_fJ-JP_c)S_cK^*.$$

These exact identities show that contour refinement alone cannot repair the physical map: both the operator intertwining term and source term are large. The 240 identity tests have zero failures.

# The spectral branches survive

Every quartet is two nonreal conjugate pairs. RH-204 reduces it to upper representatives $a_-,a_+$ ordered by real part and compares direct versus swapped assignments [@WangRH204]. All four direct assignments are unique. The minimum pointwise margin is $0.08884$ and grows beyond $0.714$ on the finer transition.

At fixed $\sigma$, the two physical channels agree strongly: $$\label{eq:channel-branch}
 \max_{\sigma,j}|\lambda^L_{\sigma,j}-\lambda^R_{\sigma,j}|
 =0.007578.$$ The maximum branch displacement falls descriptively by a ratio below $0.359$ from the first to the second transition. Two transitions do not establish convergence, but they produce a non-post-hoc label for denser experiments.

# Exact endpoint maps are retrospective

For orthonormal packet frames, RH-205 forms the polar factor of $Q_f^*JQ_c$ and the partial isometry $$\label{eq:procrustes}
 H=Q_fUQ_c^*.$$ It maps one endpoint packet exactly onto the other and is optimally close to the embedded frame [@WangRH205]. The rank-normalized physical costs are $0.44075$--$0.70099$.

This proves existence but not prediction: $H$ requires the fine packet as input. Moreover, exact range transport leaves a dynamical defect determined in part by $\Lambda_f-\Lambda_c$, whose maximum movement is $0.38160$.

# Physical residues require a cocycle

Residues are gauge invariant. RH-206 defines exact branch multipliers $$\label{eq:cocycle}
 m_j(c,f)=\frac{r_{f,j}}{r_{c,j}},
 \qquad m_j(a,c)=m_j(b,c)m_j(a,b)$$ [@WangRH206]. Conjugate branches have conjugate multipliers.

The best common complex scalar leaves relative residuals $0.32371$--$0.99985$. The exact diagonal cocycle has roundoff residual, but the corresponding left/right multipliers differ by as much as $1.05364$. Thus $W$ is branch and channel dependent at the current anchors. It cannot be substituted for the unweighted divisor ledger $Q$.

# The quartic divisor is the stable finite object

RH-207 studies $$\label{eq:quartic}
 D_\sigma(z)=\prod_{j=1}^4(z-\lambda_{\sigma,j})
 =z^4+c_1z^3+c_2z^2+c_3z+c_4$$ [@WangRH207]. Left/right coefficient errors are at most $0.008112$. The relative constant-term discrepancy decreases from $0.02716$ to $0.007749$ over the three anchors.

Across scales, however, coefficient errors are $0.240$--$0.317$. The raw quartic is a coherent dual-channel flow, not a converged flow. Newton identities exactly equate its coefficients with all unweighted power traces; 120 implementation cases have zero failures.

# Endpoint validation and transport validation separate

RH-208 uses the local feasibility ratio $$\label{eq:beta}
 \beta=\frac{2\kappa\left\lVert Av-\lambda v\right\rVert}{\delta}.$$ At all six endpoint packets, the maximum is below $3.25\times10^{-13}$ [@WangRH208]. Direct interval validation of each finite endpoint therefore appears plausible.

For Haar-lifted coarse modes, the smallest transport ratio is $3.3486$ and the largest is $29.4916$; no transition passes. These are floating feasibility indicators, not certificates. They nevertheless justify validating endpoints directly rather than attempting to validate a failed homotopy.

# Cloud enlargement is not the missing correction

RH-209 tests top-modulus clouds of ranks $$2,4,6,8,12,16,24,32.$$ None of the 32 rank/transition/channel records has both right and left maximum principal sines below $0.5$ [@WangRH209]. The best joint sine is $0.69373$, and expanded clouds often approach one.

This rejects only equal-rank modulus selection with Haar transport. It leaves adaptive contours, unequal ranks, source-weighted metrics, and renormalized coordinates open.

# Why the divisor-first pivot is logically allowed

RH-210 considers $A_\theta=U_\theta DU_\theta^*$ with fixed diagonal $D$. Its characteristic polynomial is independent of $\theta$, while a selected rank-one projector moves by $|\sin\theta|$ [@WangRH210]. Hence a divisor can be stable while projector distance reaches one.

This does not make operator theory unnecessary. It proves only that raw projector convergence is not a logical prerequisite for first discovering a stable scalar divisor. A later dynamical/Fredholm realization will still require analytic operator or symbolic structure.

# Revised Gate-A subroute

The new order is: $$\label{eq:route}
 \begin{gathered}
 \text{finite branch labels}
 \longrightarrow\text{intrinsically normalized coefficient flow}\\
 \longrightarrow\text{growing locally uniform divisor family}
 \longrightarrow\text{dynamical/Fredholm realization}.
 \end{gathered}$$ In parallel, endpoint projectors can be interval validated and the residue cocycle retained as a separate transfer ledger. Raw state transport should resume only after the scalar flow suggests the correct coordinates.

# Recommended RH-212 experiment

RH-212 should densify the interval near the finest anchors on both physical channels. Before seeing results, compare at least two intrinsic quartic normalizations:

1.  determinant-radius normalization $\rho=|c_4|^{1/4}$ and $\lambda_j\mapsto\lambda_j/\rho$;

2.  centered second-moment normalization $\mu=-c_1/4$ followed by a scale derived from $\sum_j|\lambda_j-\mu|^2$.

The audit should test branch uniqueness, left/right discrepancy, adjacent coefficient variation, and whether one normalization improves all coefficients without fitting each level separately. A positive result gives a candidate renormalization map; a negative result redirects Gate A toward adaptive growing contours.

# Reproducibility ledger

The aggregate count is 649 finite endpoint, mode, random identity, correspondence, rank, and counterexample records. Exact-identity audits report zero failures. Each paper contains focused source, frozen JSON, tests, claim ledgers, and a publication archive. The archive machinery checks reproducibility, not truth of asymptotic extrapolations.

# Position in the five macro gates

-   Gate A: a finite dual-channel divisor flow exists; intrinsic renormalization, growing cloud, and determinant limit remain open.

-   Gate B: time-oriented unitary/scattering completion is untouched.

-   Gate C: self-adjoint generator and internal $T\log T$ count are untouched.

-   Gate D: prime-power/von Mangoldt trace identity is untouched.

-   Gate E: equality with the completed zeta divisor is untouched.

The route coordinate is $$\boxed{\texttt{finite\_dual\_channel\_divisor\_flow\_open\_renormalization}}.$$ No Hilbert--Pólya operator, zeta-zero identification, Riemann-hypothesis implication, or arithmetic trace formula is asserted.
