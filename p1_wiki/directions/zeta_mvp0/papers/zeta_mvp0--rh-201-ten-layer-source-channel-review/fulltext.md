---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-201-ten-layer-source-channel-review"
canonical_tex: "zeta_mvp0/papers/RH-201-ten-layer-source-channel-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-201-ten-layer-source-channel-review/main.pdf"
source_sha256: "6d0e937a4904d729336c5caa75f993970f1ccd5d3d0c90d779dcd6bdd863d5b9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ten Layers from Frobenius Multiplicity to a Canonical Source Channel RH-192--RH-200 Review and the Cross-Scale Transport Frontier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-201-ten-layer-source-channel-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-201-ten-layer-source-channel-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-201-ten-layer-source-channel-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-201-ten-layer-source-channel-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-201-ten-layer-source-channel-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This paper reviews RH-192--RH-200, a ten-layer correction and reconstruction of the physical temporal-packet route. The batch begins with an exact negative result: on matrix states $X\in\mathbb C^{n\times m}$, the physical dynamics $X\mapsto AX$ is $I_m\otimes A$. Every base Riesz multiplicity is therefore multiplied by $m$, so the earlier literal rank-one or rank-four full-Frobenius shell is impossible at widths $64,128,256$.

  The numerical signal survives in the correct state type. The single-source cyclic space has dimension at most $n$ and preserves every source-observation moment. At the surviving $\sigma=0.01,L=4$ anchor, all 48 temporal roots lie in predeclared discs containing one base eigenvalue; the maximum matching error is $1.27\times10^{-3}$. All windows on each side select one common physical quartet.

  Riesz projectors then produce exact source-observation channel states $P_\lambda S$ and $P_\lambda^*O^*$, whose pairing equals the transfer residue. Balanced coordinates give a zero-residual exact spectral packet with determinant, Newton traces, and residue-weighted physical moments. The physical packet is transverse but poorly conditioned: the optimal norm products are $192.05$ and $950.26$. Late temporal windows nevertheless align with it, with maximum subspace gap below $0.051$ and late determinant and trace errors below $10^{-4}$ and $8\times10^{-4}$.

  Finally, the four largest-modulus modes form two source-observable conjugate pairs at all six audited scale/channel cases, with minimum gap $0.05949$ to the fifth modulus. This supplies a finite outer-edge selection rule and explains the mismatch of the length-three branch.

  The aggregate machine ledger contains 1,352 finite items and zero identity failures. The next wall is validated cross-level Riesz-projector transport. Gate A remains open; Gates B--E, Hilbert--Pólya, zeta-zero identification, and RH are untouched.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Ten Layers from Frobenius Multiplicity to a Canonical Source Channel\
  RH-192--RH-200 Review and the Cross-Scale Transport Frontier
```

## Markdown 正文

# Coordinate inherited from RH-191

RH-191 ended with a local balanced bi-Krylov candidate and an exact oblique Feshbach identity, but no validated complement inverse [@WangRH191]. The proposed next calculation was an expensive contour inverse for a complement of the full matrix-state operator.

Before that calculation, RH-192 checks the ambient type. This changes the problem fundamentally: the full complement was not merely large; the desired low-rank full Riesz count was arithmetically incompatible with the operator. The present batch records both the correction and the surviving source- relative route.

# Layer-by-layer ledger

  paper    principal result                                               strict status
  -------- -------------------------------------------------------------- -------------------------------------
  RH-192   $\mathcal L_A\simeq I_m\otimes A$ and $m$-fold Riesz rank      exact type obstruction
  RH-193   source-cyclic invariant quotient; all moments preserved        exact theorem
  RH-194   48 roots match eight unique physical modes                     finite floating positive
  RH-195   Riesz source/observation channels; pairing equals residue      exact theorem
  RH-196   optimally balanced zero-residual spectral packet               exact theorem
  RH-197   residues and cross-angle geometry of the physical quartet      finite positive, ill-conditioned
  RH-198   graph-angle mechanism and temporal alignment decay             conditional theorem + finite signal
  RH-199   determinant, Newton traces, weighted moments, feedback ratio   exact finite theorem
  RH-200   conjugate-pair parity and outer-edge quartet selection         exact parity + finite support

The aggregate ledger counts 1,352 windows, roots, modes, random identity cases, or finite diagnostic sequences. The identity audits have zero failures. This count is a reproducibility ledger, not statistical evidence for an all-level theorem.

# The exact negative result: the old shell type is wrong

For $X\in\mathbb C^{n\times m}$, $$\label{eq:left-action}
 \mathcal L_AX=AX,
 \qquad
 \operatorname{vec}(AX)=(I_m\otimes A)\operatorname{vec}(X).$$ Hence $$\label{eq:multiplicity}
 \det(zI-\mathcal L_A)=\det(zI-A)^m,
 \qquad
 \operatorname{rank}P_\Gamma(\mathcal L_A)
 =m\operatorname{rank}P_\Gamma(A)$$ [@WangRH192].

Across the 126 RH-185 windows, $m\in\{64,128,256\}$ and packet length is three or four. No packet count is divisible by $m$. If one root contour contains one simple base eigenvalue, the full Frobenius count is $m$ and the RH-189 complement must carry $m-1$ copies. The one-root burden is 63--255.

This rejects only $$\text{small temporal packet}
 =\text{complete Riesz projection of }I_m\otimes A.$$ It does not reject the root location.

# The correct source-relative state

The physical experiment starts from one matrix $S$, so its reachable state is $$\label{eq:cyclic}
 \mathcal K_S=\operatorname{span}\{S,AS,A^2S,\ldots\}.$$ RH-193 proves $$\label{eq:cyclic-dim}
 \dim\mathcal K_S=\deg\mu_{A,S}\le n,$$ and constructs an exact restriction $T$ with $$\label{eq:moments}
 \langle O^*,A^qS\rangle_F=c^*T^qb$$ for every $q\ge0$ [@WangRH193].

Every right temporal packet lies in this cyclic state. Restricting the left frame to it preserves biorthogonality. Thus the packet can have one channel per simple source-excited eigenvalue without contradicting the ambient $m$-fold multiplicity.

# The numerical roots are physical

RH-194 performs the direct spectral test [@WangRH194]. The accepted starts are 14--18 on the left and 12--18 on the right at $\sigma=0.01,L=4$. Each of the 48 compressed roots has one distinct nearest base eigenvalue inside the frozen root disc. The maximum match error is $$\label{eq:match}
 1.2693\times10^{-3},$$ while the minimum computed radial clearance from any eigenvalue to a contour is approximately $0.194$.

All windows on one side select the same four modes. Their approximate geometry is $$\label{eq:quartet}
 -0.495\pm0.620i,
 \qquad
 0.474\pm0.557i.$$ The two channels have small discretization differences. The result is floating, but the root signal is much smaller than the contour scale.

# Source-observation channels

For an isolated simple mode with projector $P_i$, RH-195 defines $$\label{eq:channel-states}
 X_i=P_iS,
 \qquad Y_i=P_i^*O^*,$$ and proves $$\label{eq:residue-pairing}
 \langle Y_i,X_j\rangle_F
 =\delta_{ij}r_i,
 \qquad
 r_i=\operatorname{tr}(OP_iS)$$ [@WangRH195]. The scalar $r_i$ is the transfer residue.

Nonzero residues produce exact biorthogonal channel coordinates. Unlike a generic Ritz packet, these states satisfy zero right and left residuals. Their rank is the number of selected source-observable modes, while the complete ambient projector retains rank $m$ per base mode.

# Canonical packet and intrinsic conditioning

RH-196 balances the exact right and left channel spaces with the cross-Gram SVD [@WangRH196]. If $\gamma$ is the minimum cross singular value, the optimal frame norm product is $$\label{eq:optimal-condition}
 \chi_{\rm can}=\gamma^{-1}.$$ The compressed packet is similar to the selected spectral restriction, so its determinant and traces are exact.

The RH-197 physical audit gives

  side        $\gamma$   $\chi_{\rm can}$   minimum $|r_i|$
  ------- ------------ ------------------ -----------------
  left      $0.005207$           $192.05$         $0.02610$
  right     $0.001052$           $950.26$         $0.01107$

[@WangRH197]. The packet is transverse, but especially on the right it is not benignly conditioned.

At the latest temporal starts, the RH-185 conditions differ from these canonical optima by about one percent. Large obliqueness is therefore part of the physical source-observation geometry, not merely an avoidable frame choice.

# Temporal alignment with the exact endpoint

RH-198 proves the graph identity $$\label{eq:graph-angle}
 \tan\theta_{\max}=\left\lVert G\right\rVert$$ and a conditional Krylov convergence theorem under spectral-gap and selected-block inverse bounds [@WangRH198].

In the finite data, all four right/left gap sequences have negative fitted log slopes. Their descriptive per-step ratios lie between $0.830$ and $0.850$; the minimum fit $R^2$ is $0.899$. The latest maximum gap is $0.0505$. Root errors decay faster, with fitted ratios $0.695$--$0.739$.

These are finite diagnostics. Eventually a normalized orbit can lose four-dimensional rank as the outermost conjugate pair dominates, so the short-start ratio must not be extrapolated blindly.

# Determinant, traces, and physical moments

RH-199 separates the unweighted spectral ledger $$\label{eq:unweighted}
 D_E(z)=\det(zI-K),
 \qquad s_q=\operatorname{tr}K^q=\sum_j\lambda_j^q$$ from the residue-weighted physical moments $$\label{eq:weighted}
 h_q=c^*K^qb=\sum_jr_j\lambda_j^q$$ [@WangRH199]. The exact feedback ratio is $$\label{eq:feedback-ratio}
 \frac{\det(zI-(K+bc^*))}{\det(zI-K)}
 =1-c^*(zI-K)^{-1}b.$$

At the latest physical windows the maximum determinant error is $8.91\times10^{-5}$ and the maximum trace error through power eight is $7.66\times10^{-4}$. Similarity invariants converge even though coordinate norms are large.

These traces are not von Mangoldt traces. The residues are physical transfer weights with no established arithmetic identification.

# An outer-edge selection principle

RH-200 replaces post hoc root matching by a candidate intrinsic rule: select the four largest-modulus source-observable modes [@WangRH200]. Since the physical matrices are real, nonreal modes occur in conjugate pairs. At all three audited scales and on both channels, the outer four modes are two nonreal pairs.

The gap $|\lambda_4|-|\lambda_5|$ is positive in all six cases and has minimum $0.05949$. All 24 selected mode records have nonzero residue. Thus the edge quartet is defined without consulting temporal roots at these anchors.

This also explains the finite length-three failure: an odd-dimensional real conjugation-closed packet cannot contain two complete nonreal pairs. It is an explanation of the audited branch, not an all-level no-go theorem for all possible length-three constructions.

# What the batch achieved

The strongest defensible statement is:

> The earlier temporal-clock numerics identified a genuine physical outer-edge quartet, but the correct low-rank object is a source--observation Riesz channel packet, not the complete Riesz projection of the full Frobenius left-multiplication operator.

This statement combines one exact correction, several exact finite algebra theorems, and one finite physical discovery. It is substantially firmer than the RH-191 frontier because the complement-count paradox is resolved rather than hidden inside an inverse estimate.

# What remains open inside Gate A

The next missing objects are:

1.  interval or outward-validated contours and Riesz projectors for the edge quartets;

2.  a common-coordinate map between quartets at adjacent refinement levels;

3.  bounds on interlevel projector angles, residues, and determinant coefficients;

4.  a growing cloud rule---a fixed quartet alone can never produce a $T\log T$ spectral count;

5.  an all-level physical interface and intrinsic cloud ledger $Q$.

The fixed quartet should be viewed as a local building block and a test case for transport, not as the eventual infinite spectrum.

# Recommended RH-202 experiment

Use the existing coarse/fine embeddings to place the outer quartets at $\sigma=0.04,0.02,0.01$ in common coordinates. For each adjacent pair, compute: $$\label{eq:transport-data}
 \begin{gathered}
 \text{embedded projector principal angles},\quad
 \text{intertwining defects},\\
 \text{transported residues},\quad
 \text{determinant-coefficient differences}.
 \end{gathered}$$ Where feasible, wrap the contour counts and projectors in validated error bounds. A positive result would be the first concrete shell-transport map $H$. A negative result would show that a fixed outer quartet is not stable and that the cloud must be selected by a larger cluster rule.

# Position in the five macro gates

The entire batch remains within Gate A:

-   Gate A, intrinsic dynamical spectral determinant/cloud: one finite source-channel block exists; the all-level object is open.

-   Gate B, time-oriented unitary or scattering completion: untouched.

-   Gate C, self-adjoint generator and internal $T\log T$ count: untouched.

-   Gate D, prime-power/von Mangoldt trace identity: untouched.

-   Gate E, equality with the completed zeta divisor: untouched.

No Hilbert--Pólya operator, zeta-zero correspondence, or Riemann-hypothesis implication is claimed.

# Reproducibility

Each paper contains source, focused tests, frozen result JSON, theorem and roadmap ledgers, and an individual publication manifest. RH-201 additionally builds a batch manifest for RH-192--RH-201. Heavy physical eigendecomposition is performed once in RH-194 and reused by downstream audits; RH-200 performs an independent three-scale edge check.

The review script reads the frozen outputs and verifies all key counts and claim boundaries. The aggregate identity-failure count is zero. Floating physical positives remain labeled as such and are not upgraded by the archive machinery.
