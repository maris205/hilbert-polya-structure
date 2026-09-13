---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-151-ky-fan-reset-packet-atlas"
canonical_tex: "zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/main.pdf"
source_sha256: "a15a058a0243a51e2ceb336a00b358962fe9c69e5f2fcd57a0d64dc225d3eb40"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ky--Fan Energy Loss and a Direct Reset Packet Atlas A Gauge-Free Exit from the Recursive Direction Wall

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-150 proved that source-aligned packet balls are initially tiny but that a separated cross--direction--Ritz radius recursion loses all ten RH-96 chains by the third update. We investigate a gauge-free replacement based on captured energy.

  For a positive semidefinite matrix $A$ with rank-$r$ top projector $P$, gap $g=\lambda_r-\lambda_{r+1}>0$, and any rank-$r$ projector $Q$, define the Ky--Fan deficit $$L=\operatorname{tr}(PA)-\operatorname{tr}(QA).$$ We prove the sharp bounds $$\|P-Q\|^2\leq \frac Lg,
   \qquad
   \|P-Q\|_F^2\leq\frac{2L}{g}.$$ Because every recursive Ritz search space contains its input packet, the captured energy is monotone independently of the threshold branch. This gives a scalar branch-free loss recursion involving only the previous loss, the previous gap, global-packet drift, and Gram drift. The theorem is valid but the finite audit is negative: only 11 of 130 snapshot bounds remain informative as small gaps amplify global-packet motion.

  We then reset independently at each source-memory snapshot. The exact binary memory Gram is enclosed around its numerical center with 384-bit Arb arithmetic; a polar-corrected long-double Rayleigh audit supplies the center gap. All 130 native clock-rank packets certify. The minimum ratio of center gap to twice the matrix radius is $60.368$, and the largest projector radius is $0.008352$. Direct resets also maximize captured energy and therefore dominate every same-rank recursive packet at the same snapshot. This is a finite reset atlas, not an all-level gap theorem and not an identification of the exact threshold-recursive packet. Transition coherence is the next open interface.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Ky--Fan Energy Loss and a Direct Reset Packet Atlas\
  A Gauge-Free Exit from the Recursive Direction Wall
```

## Markdown 正文

# A sharp energy-to-angle theorem

Let $A\succeq0$ have eigenvalues $\lambda_1\geq\cdots\geq\lambda_n$ and let $P$ project onto the first $r$ eigenvectors. For another rank-$r$ orthogonal projector $Q$, write $q_j=\langle e_j,Qe_j\rangle$ and $$\theta=r-\operatorname{tr}(PQ)
 =\sum_{j>r}q_j=\frac12\|P-Q\|_F^2.$$

[\[thm:kyfan\]]{#thm:kyfan label="thm:kyfan"} If $g=\lambda_r-\lambda_{r+1}>0$, then $$L:=\operatorname{tr}(PA)-\operatorname{tr}(QA)
 \geq g\theta.$$ Consequently $$\boxed{\ \|P-Q\|\leq\sqrt{L/g},\qquad
 \|P-Q\|_F\leq\sqrt{2L/g}.\ }$$ Both constants are sharp.

The lost top mass and gained bottom mass both equal $\theta$. Hence $$\begin{aligned}
L&=\sum_{j\leq r}\lambda_j(1-q_j)-
   \sum_{j>r}\lambda_jq_j\\
 &\geq\lambda_r\theta-\lambda_{r+1}\theta=g\theta.\end{aligned}$$ The Frobenius identity above gives the second bound, while the largest principal-angle sine squared is at most their sum $\theta$. A two-dimensional rank-one rotation with spectrum $(\lambda_r,\lambda_{r+1})$ attains equality [@Bhatia1997].

Unlike a selected cross-direction projector, $L$ is invariant under frame rotations. However, dividing by a small spectral gap is unavoidable: if $g=0$, arbitrary rotations inside the boundary eigenspace cost zero energy.

# A branch-free scalar recursion

Let $A_{t-1},A_t\succeq0$ have top-rank projectors $P_{t-1},P_t$. Suppose a rank-$r$ packet $Q_{t-1}$ has deficit $L_{t-1}$ under $A_{t-1}$, and an update chooses the best rank-$r$ Ritz packet $Q_t$ in any search space containing $\operatorname{ran}Q_{t-1}$. Then $$\operatorname{tr}(Q_tA_t)\geq
 \operatorname{tr}(Q_{t-1}A_t)$$ without knowing which threshold width or direction frame was used.

Define $$D_t=\operatorname{tr}(P_tA_t)-
     \operatorname{tr}(P_{t-1}A_t),
 \qquad \Delta_t=\|A_t-A_{t-1}\|_F.$$

[\[thm:scalar\]]{#thm:scalar label="thm:scalar"} If $g_{t-1}>0$, then the output deficit obeys $$L_t\leq D_t+L_{t-1}
 +\sqrt{\frac{2L_{t-1}}{g_{t-1}}}\,\Delta_t.$$

Insert and subtract $A_{t-1}$ in $\operatorname{tr}((P_{t-1}-Q_{t-1})A_t)$. The old term is $L_{t-1}$, and Cauchy--Schwarz plus Theorem [\[thm:kyfan\]](#thm:kyfan){reference-type="ref" reference="thm:kyfan"} bounds the drift term by $\|P_{t-1}-Q_{t-1}\|_F\Delta_t$. The Ritz monotonicity inequality then proves the claim.

The estimate is structurally attractive but pessimistic. It treats all Gram motion as aligned with the packet error and then divides by the next gap. The audit starts at $L_0=0$ and iterates the bound. Only 11 of 130 snapshots retain $L_t<g_t$. Thus removing branches alone does not remove cumulative loss.

# Independent spectral resets

Accumulation disappears if each packet is defined natively at its own snapshot. Let $B_t$ be the archived binary center, let $\widetilde A_t$ be the exact binary memory Gram, and suppose $$\|\widetilde A_t-B_t\|\leq\delta_t.$$

[\[thm:reset\]]{#thm:reset label="thm:reset"} If the rank-$r$ center gap $g_t$ satisfies $g_t>2\delta_t$, the exact top packet $\widetilde P_t$ and center packet $P_t$ obey $$\|\widetilde P_t-P_t\|
 \leq\frac{\delta_t}{g_t-\delta_t}.$$ The non-crossing gate is sharp from a norm ball alone.

This is the Davis--Kahan approximate-gap theorem [@DavisKahan1970; @StewartSun1990]. If $g_t\leq2\delta_t$, a diagonal two-mode perturbation can close or reverse the boundary gap.

The reset packet also has a variational advantage: $$\operatorname{tr}(P_tB_t)
 \geq\operatorname{tr}(QB_t)$$ for every rank-$r$ packet $Q$. Thus replacing an RH-96 recursive packet by the reset packet cannot worsen the frozen captured-energy tail. It changes the construction, but it does so in the favorable direction for all Ky--Fan tail gates.

# The 130-snapshot atlas

For each of five scales and two channels, the audit rebuilds all memory Grams from the exact binary operator and source. The chain lengths are $5,7,12,18,23$ snapshots per channel, totaling 130. Arb evaluates the state, trace normalization, and memory recurrence at 384 bits. The maximum matrix operator radius is $2.642\times10^{-15}$.

Computing 130 full interval eigendecompositions at dimensions up to 256 would be unnecessarily expensive. We instead diagonalize the center, recompute its Rayleigh matrix in long double, bound the off-diagonal Frobenius norm, and correct the almost-orthogonal eigenframe by its polar metric defect. The resulting center spectral error is subtracted twice from the displayed gap; the Arb matrix radius is then inserted into Theorem [\[thm:reset\]](#thm:reset){reference-type="ref" reference="thm:reset"}. This is a hybrid outward audit, not a formal interval eigensolver archive [@Johansson2017].

::: {#tab:atlas}
  quantity                                       0.16                    0.08                    0.04                    0.02                    0.01
  --------------------------- ----------------------- ----------------------- ----------------------- ----------------------- -----------------------
  snapshots, both sides                            10                      14                      24                      36                      46
  direct reset certificates                        10                      14                      24                      36                      46
  worst reset radius            $6.93\!\times10^{-4}$   $2.81\!\times10^{-6}$   $4.54\!\times10^{-5}$   $6.30\!\times10^{-3}$   $8.35\!\times10^{-3}$

  : Independent clock-rank reset packets.
:::

All 130 packets certify. The smallest gap lower is $1.220\times10^{-13}$, but the corresponding matrix ball is smaller still; the global minimum $g_t/(2\delta_t)$ is $60.368$. The maximum packet radius is $0.008352$.

For comparison, the actual frozen recursive packets have informative Ky--Fan angle bounds on 114 snapshots, but their maximum direct distance from the global packet is essentially one. The analytic Ky--Fan inequality has zero dominance failures after outward center-error padding. Independent resets dominate recursive captured energy on all 130 snapshots.

![Direct reset gaps and radii, recursive/global packet separation, and the three information counts.](<../../../../../zeta_mvp0/papers/RH-151-ky-fan-reset-packet-atlas/figures/ky_fan_reset_packet_atlas.pdf>){#fig:atlas width="\\textwidth"}

# Consequence and boundary

RH-150's wall is not a source-gap failure. It is a failure of transporting a specific threshold-recursive gauge through weak selected directions. The same exact binary source model supports a tight top-packet ball at every frozen time when the packet is reset independently.

The next question is geometric rather than spectral existence. Consecutive reset packets must be compared through principal angles, polar Procrustes maps, and pulled-back Grams. If their overlap maps remain uniformly invertible under the certified balls, the reset atlas can replace the failed recursive chain in the outward assembly. If not, a cluster or rank-adaptive packet will be required.

We have not identified reset packets with the exact RH-96 recursive output, inserted them into RH-138, proved a uniform all-level reset gap or transition lower, closed Stage A, constructed a Hilbert--Polya operator, identified zeta zeros, or proved the Riemann Hypothesis.
