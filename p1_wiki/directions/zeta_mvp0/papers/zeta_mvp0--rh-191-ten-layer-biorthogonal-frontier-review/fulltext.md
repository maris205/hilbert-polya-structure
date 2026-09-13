---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-191-ten-layer-biorthogonal-frontier-review"
canonical_tex: "zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review/main.pdf"
source_sha256: "72510b6b255ab0c2ecb9de974531ef1742ba9176cc2b32bb5abcd1ea72f511fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ten Layers from Orthogonal Clock Failure to an Oblique Feshbach Frontier RH-182--RH-190 Route Review and the Next Physical Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-191-ten-layer-biorthogonal-frontier-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This paper reviews RH-182--RH-190, the next ten-layer exploration after the reset-history/cycle review of RH-181. The batch began with a strict test of the data-derived orthogonal temporal clock at the predeclared lengths $L=r-3$ and $L=r-4$. The exact weighted-cycle construction was correct, but all 126 windows failed the common wrap/primal/adjoint gate; even the best projective endpoint return was too large. This closes the simplest orthogonal physical clock branch at the audited finite anchors.

  The next layer used the physical observation to construct a balanced biorthogonal source/observation clock. The algebra is exact: the cross-Gram SVD gives $W^*V=I$, the optimal oblique condition is the inverse smallest cross singular value, and compressed spectra are gauge-covariant. In the physical audit, 12 of 38 $\sigma=0.01,L=4$ windows pass a two-sided $0.10$ residual gate; no length-three window passes. This is a local floating candidate, not a uniform realization.

  The final layers quantify its boundary. Cross-angle conditioning defeats a coarse maximum-residual gate and every singular-value clipping regularizer; scalar gauge balancing leaves the sharp directional product invariant, with eight windows having absolute coupling product below one. An exact oblique Feshbach determinant factorization is proved and audited. The elementary norm-only complement-resolvent budget then fails on all 126 windows, even under an optimistic unit complement factor.

  The updated frontier is therefore precise: $$\begin{gathered}
   \text{local biorthogonal packet candidate}\\
   \downarrow\\
   \text{validated physical complement contours }D\\
   \downarrow\\
   \text{uniform margin }K,\ \text{transport }H,\ \text{cloud ledger }Q
   \end{gathered}$$ Gate A and all Hilbert--Polya downstream gates remain open. No zero identification or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Ten Layers from Orthogonal Clock Failure to an Oblique Feshbach Frontier\
  RH-182--RH-190 Route Review and the Next Physical Gate
```

## Markdown 正文

# Coordinate before this batch

RH-181 left two architecture-relative routes. The reset-history branch had an exact memory-to-history realization but no history-to-transfer map. The finite-cycle branch had exact determinant algebra but no physical calibration or cycle-to-transfer map [@WangRH181]. The recommended next experiment was a target-independent finite temporal clock using $L=r-3$ and $L=r-4$.

The present review records not only what survived, but also which negative shortcuts are now closed. This matters because a local positive numerical window is not the same object as an all-level physical leaf.

# Layer-by-layer ledger

  paper    principal result                                                       strict status
  -------- ---------------------------------------------------------------------- ----------------------------
  RH-182   finite normalized orbit clock, exact rank-one wrap, 126-window audit   orthogonal branch rejected
  RH-183   optimal phase/scalar wrap and projective lower bound                   finite obstruction proved
  RH-184   balanced cross-Gram biorthogonal frames and optimal conditioning       finite algebra proved
  RH-185   physical source/observation bi-Krylov calibration                      local $L=4$ candidate
  RH-186   oblique conditioning amplification                                     coarse gate rejected
  RH-187   exact clipping Pareto tradeoff                                         clipping branch rejected
  RH-188   scalar gauge balance and invariant directed product                    partial positive signal
  RH-189   exact oblique Feshbach determinant identity                            finite algebra proved
  RH-190   norm-only complement resolvent budget                                  norm route rejected

The machine ledger contains 2,960 finite cases, windows, or sweep items and zero recorded formula/identity failures. This is an implementation ledger, not a statistical sample and not evidence that the open physical leaves are true.

# The orthogonal branch is genuinely closed at finite level

For a normalized source orbit $x_j$ and temporal synthesis $J$, RH-182 pairs the chain with a weighted cycle. The intertwining error is exactly $$\label{eq:rank-one}
 \mathcal AJ-JC
 =a_{t+L-1}(x_{t+L}-\omega x_t)e_{L-1}^*.$$ The cycle spectrum is an exact root grid. Thus the test did not fail because of a poorly assembled determinant.

RH-183 proves that even optimizing over all phases and all final-edge scalars leaves the projective lower bound $$\label{eq:projective}
 a_{t+L-1}\sqrt{1-|\langle x_t,x_{t+L}\rangle|^2}.$$ Across 126 windows, no projective return is at most $0.25$. The minimum adjoint residual in the polar orthogonal construction is $0.7143$. Hence the following finite branch is closed: $$\label{eq:closed-orthogonal}
 \text{one orthogonal temporal packet}
 +\text{one phase/scalar wrap}
 \Longrightarrow\text{two-sided physical clock}.$$

This does not reject a different temporal span, a lagged map, or two distinct right/left spaces.

# The biorthogonal algebraic bridge

RH-184 starts with right and left orthonormal temporal bases $Q_R,Q_L$ and cross Gram $H=Q_L^*Q_R$. If $H=U\Sigma V^*$, the balanced frames are $$\label{eq:balanced}
 V_R=Q_RV\Sigma^{-1/2},
 \qquad W_L=Q_LU\Sigma^{-1/2},
 \qquad W_L^*V_R=I.$$ The exact optimal conditioning is $$\label{eq:optimal-conditioning}
 \left\lVert V_RW_L^*\right\rVert=\sigma_{\min}(H)^{-1}.$$ This is not a frame-choice artifact. Every biorthogonal realization on the same two subspaces has norm product at least this value.

The compressed block and directed residuals are $$\label{eq:directed}
 K=W_L^*AV_R,
 \qquad
 R_R=AV_R-V_RK,
 \qquad
 R_L=A^*W_L-W_LK^*.$$ This is the exact typed replacement for an orthogonal reducing packet.

# Local physical calibration

RH-185 constructs the right history from $A^jS$ and the left history from $(A^*)^jO^*$. The same 126 windows are tested. The results are:

  branch                          windows   two-sided passes   minimum condition
  ----------------------------- --------- ------------------ -------------------
  all length-three candidates          88                  0             $48.22$
  $\sigma=0.01,L=4$, left              19                  5             $88.11$
  $\sigma=0.01,L=4$, right             19                  7            $179.75$

The accepted length-four windows have phase-grid errors near $0.1$ radians and radial errors near a few hundredths. The best residual pair is $(0.02332,0.02498)$.

This selects $L=4$ as a local calibration at the only actual RH-15/RH-151 overlap. It does not select it at untested scales and does not prove a cloud degree law.

# Conditioning and regularization

RH-186 inserts $\chi=\sigma_{\min}(H)^{-1}$ into a coarse coordinate gate $$\label{eq:amp}
 \chi\max(\epsilon_R,\epsilon_L)<1.$$ The minimum amplified residual over all 126 windows is $10.253$, so the gate has zero successes. RH-187 then clips the cross-Gram singular values. If $\gamma=\sigma_{\min}(H)$, residual level $\epsilon$, and clipping level $\tau$, the combined budget is exactly $$\label{eq:clip}
 1+\frac{\epsilon-\gamma}{\max(\gamma,\tau)}
 \quad (\tau\ge\gamma).$$ Strict contraction exists if and only if $\epsilon<\gamma$. The physical minimum ratio is again $10.253$; 1,638 clipping sweeps yield zero strict successes. This closes the simple spectral-clipping repair.

# The directional product remains alive

RH-188 separates the two couplings. Under $V\mapsto\alpha V$, $W\mapsto\alpha^{-1}W$, the couplings transform as $c\mapsto\alpha c$ and $b\mapsto\alpha^{-1}b$. Hence $bc$ is invariant and the maximum is minimized at $\sqrt{bc}$.

The physical absolute product has minimum $0.2486$ and eight windows have $bc<1$, all in the local length-four branch. Twelve local windows have relative product below $0.01$. Therefore the sharp Schur route is not eliminated by the maximum-norm negative result. It still needs packet and complement resolvent factors.

# Exact Feshbach structure

RH-189 makes the missing factors type-correct. Extend $V$ by a basis $Z$ of $\ker W^*$ and write $S=[V,Z]$. Then $$\label{eq:block}
 S^{-1}AS=\begin{pmatrix}K&B\\C&D\end{pmatrix},$$ and $$\label{eq:feshbach}
 \det(zI-A)=\det(zI-D)
 \det\left(zI-K-B(zI-D)^{-1}C\right).$$ The 240-case identity audit has maximum relative determinant error $1.85\times10^{-11}$. The physical complement resolvent is now a specific operator, not an informal remainder.

# The norm-only complement route fails

RH-190 applies the universal estimate $$\label{eq:norm-only}
 \left\lVert D\right\rVert\le\chi\left\lVert A\right\rVert$$ in the orthonormal complement coordinates of RH-189. With contour radius $0.4$ of the cycle half-spacing, every one of 126 windows has negative clearance. The smallest complement norm bound is $71.46$, while the largest contour minimum modulus is only $0.7188$. Even assigning the complement resolvent the artificial value one leaves zero Schur successes; the optimistic product has minimum $1.1116$.

This is a coarse norm failure, not a spectral no-go. It tells us exactly where the next computation belongs: validated sample inverses on the actual contours, with mesh covering and operator balls as in RH-167--168.

# Updated frontier

The current finite route can be written $$\label{eq:route}
 \begin{aligned}
 &\text{balanced bi-Krylov algebra [proved]}\\
 &\quad+\ \text{local }(\sigma=0.01,L=4)\text{ candidate [floating]}\\
 &\quad\longrightarrow\ D_{\rm phys}\text{ [validated contours, open]}\\
 &\quad\longrightarrow\ K_{\rm phys},H_{\rm phys},Q\text{ [open]}.
 \end{aligned}$$ The reset-history branch remains open independently. The orthogonal clock shortcut is removed, but the biorthogonal branch is not a proof of physical interface R.

# Decision tree at the present frontier

The next contour calculation has two informative outcomes. If every predeclared local window fails because the complement contour intersects the validated pseudospectrum or because the full Schur product is at least one, then the present $L=4$ realization is rejected at those finite anchors. The reset-history branch and other biorthogonal seeds remain logically open, but this packet choice should not be carried forward.

If at least one window has a positive continuous margin, the conclusion is still finite: RH-189 then identifies the full Riesz count as $$\label{eq:count-ledger}
 N_A(\Gamma)=N_K(\Gamma)+N_D(\Gamma).$$ The complement count must be shown to vanish, or retained explicitly. Only after this count is stable under outward operator balls can the route move to uniform margin $K$ and shell transport $H$.

This decision tree makes the present exploration falsifiable. A local candidate is not protected by the earlier phase agreement; it survives only if the exact complement calculation does.

# Position inside the five macro gates

The entire batch remains inside Gate A of the larger roadmap. More precisely, it concerns the physical realization and finite Riesz interface that precede an intrinsic cloud ledger. None of the following downstream tasks has begun here:

1.  completion of the non-self-adjoint dynamics into a time-oriented unitary or scattering object;

2.  construction of a self-adjoint generator;

3.  derivation of a $T\log T$ counting law from that generator;

4.  derivation of von Mangoldt prime-power weights from a trace formula;

5.  equality of the resulting spectral divisor with the completed zeta divisor.

Keeping this macro position explicit prevents finite packet eigenvalues from being described as zeta zeros or Hilbert--Polya eigenvalues.

# Batch reproducibility and evidence classes

The 2,960-item aggregate combines formula trials, physical windows, and regularization sweep points. These objects have different logical types. Formula trials test exact finite identities against independent matrix computations. Physical windows evaluate declared deterministic gates. Threshold sweeps map a branch-specific Pareto curve. Their counts are added only for archive completeness; they are not exchangeable observations and do not define a statistical confidence level.

Each paper therefore carries three separate records: a theorem ledger, a machine result, and a roadmap boundary. The batch manifest hashes the publication files across RH-182--RH-191. This makes later revisions able to distinguish a changed theorem, a changed dataset, and a changed interpretation rather than treating the ten layers as one opaque numerical experiment.

# Final boundary

RH-182--190 prove finite weighted-clock, projective, biorthogonal, gauge, Feshbach, and norm-budget statements and provide reproducible finite audits. They do not prove uniform cross-angle control, a physical complement inverse, continuous Schur margins, Riesz shell ranks, shell transport, cloud ledger Q, complement limit U, canonicity Z, marked limit T, or macro Gate A.

Gates B--E, a self-adjoint generator, the $T\log T$ law, a von Mangoldt trace formula, a zeta divisor identity, Hilbert--Polya, and the Riemann Hypothesis remain untouched.
