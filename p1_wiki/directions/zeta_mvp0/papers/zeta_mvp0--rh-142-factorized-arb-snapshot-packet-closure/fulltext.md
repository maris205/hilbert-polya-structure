---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-142-factorized-arb-snapshot-packet-closure"
canonical_tex: "zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/main.pdf"
source_sha256: "2ca415539fac4d532a855a0d00f55fa58faf8e44eeabbabaac1efd6a59c0be79"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Factorized Arb Closure of the Snapshot-to-Packet Interface Direct Quadratic Cancellation and Two Thin-Gap Rescues

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-141 proved a sharp gap criterion for turning a normalized-snapshot norm ball into a spectral packet, but the universal RH-140 ball certified only four of ten rank-four source anchors. We retain the low-rank geometry directly. Write the numerical rank-four approximation as an exact factorized binary matrix $H=LR$, evaluate the frozen binary source state $S$ and $$D=\frac{S^*S}{\|S\|_F^2}-\frac{H^*H}{\|H\|_F^2}$$ in 512-bit Arb arithmetic, and lower-bound the fourth-mode gap by $$g_H\geq
   \frac{\lambda_{\min}(L^*L)\lambda_{\min}(RR^*)}{\|LR\|_F^2}.$$ The factorization keeps $H$ exactly rank at most four and avoids dense reconstruction noise.

  Eight of ten channels satisfy $g_H>2\|D\|_F$. The two coarsest channels do not: the Frobenius upper loses the small margin. For those two matrices we compute validated interval eigenvalue enclosures for $D$ and use their maximum modulus instead. Both then pass. The minimum certified ratio $g_H/(2\|D\|)$ is $1.02227$, on the coarse right channel. Thus all ten rank-four packets are rigorously identified for the frozen binary source model. This is a genuine closure of the finite snapshot-to-projector interface, not an all-level source theorem. Moreover, the same coarse right channel has projector radius $0.9574$: non-crossing is proved, but tight frame-level propagation through a recursive threshold update is not.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Factorized Arb Closure of the Snapshot-to-Packet Interface\
  Direct Quadratic Cancellation and Two Thin-Gap Rescues
```

## Markdown 正文

# Why the universal ball lost six packets

RH-140 used only the Frobenius state residual. That information allows the state error to point in the worst projective direction, so the normalized snapshot radius is linear in the residual. A singular-value truncation is more correlated: to first order, the retained and discarded pieces are orthogonal and the normalized Gram error is quadratic. RH-141 showed that the difference is decisive. Its universal radius crossed only four rank-four gaps, while the quadratic diagnostic crossed all ten.

The issue is not solved by recording a dense floating rank-four matrix. Entrywise rounding of a dense product can create tiny extra singular values and obscure the exact zero beyond rank four. We instead retain the computed factors $L$ and $R$ as binary inputs and define $H=LR$ inside Arb. The candidate then has exact algebraic rank at most four relative to those inputs, and both its gap and its normalized Gram can be enclosed without an unvalidated SVD claim.

# A factorized gap lower

The following elementary inequality is the central reduction from the large ambient matrix to two four-dimensional Gramians.

[\[thm:gap\]]{#thm:gap label="thm:gap"} Let $L\in\mathbb C^{m\times r}$ have full column rank and $R\in\mathbb C^{r\times n}$ have full row rank. For $H=LR$, the smallest nonzero eigenvalue of $H^*H/\|H\|_F^2$ obeys $$\lambda_r\!\left(\frac{H^*H}{\|H\|_F^2}\right)
 \geq
 \frac{\lambda_{\min}(L^*L)\lambda_{\min}(RR^*)}{\|LR\|_F^2}.$$ Since $\operatorname{rank}H=r$, this is also its top-$r$ packet gap.

For every vector $x$ orthogonal to $\ker R$, $$\|LRx\|^2
 \geq\lambda_{\min}(L^*L)\|Rx\|^2
 \geq\lambda_{\min}(L^*L)\lambda_{\min}(RR^*)\|x\|^2.$$ The min--max principle gives the lower bound for the smallest nonzero singular value squared of $LR$. Division by $\|LR\|_F^2$ proves the claim [@HornJohnson2013].

In the audit, both $r\times r$ factor Gramians are enclosed by Arb and their smallest eigenvalues are bounded below by outward Gershgorin disks. This avoids an ambient eigenproblem for the candidate gap.

# Direct normalized-snapshot enclosure

Let $S$ be the exact result of evaluating the archived binary operator and source matrices in Arb, and let $H=LR$ be the exact factorized binary candidate. Positive interval lowers for both Frobenius norms validate the normalizations. Arb then evaluates the entries of $$D=\mathcal N(S)-\mathcal N(H)$$ with directed rounding [@Johansson2017].

The universally safe extraction is $$\|D\|\leq\|D\|_F.$$ When the resulting radius $f$ satisfies $g_H>2f$, RH-141 immediately gives a packet certificate. When it fails, we ask Arb for interval enclosures of all eigenvalues of the real symmetric $D$ and set $$e=\max_j\sup |\lambda_j(D)|.$$ Then $\|D\|\leq e$, and the same gap theorem applies with $e$. This second step is needed only in dimension sixteen at the two coarse channels.

[\[prop:fro\]]{#prop:fro label="prop:fro"} No constant smaller than $\sqrt2$ converts the operator norm of every traceless Hermitian matrix to its Frobenius norm. Consequently a packet with gap ratio between $1$ and $\sqrt2$ may be certifiable by a sharp spectral radius while failing the Frobenius gate.

For $D=\operatorname{diag}(a,-a)$, $\|D\|_F=\sqrt2|a|$ and $\|D\|=|a|$. This attains the constant. Choosing a gap between $2|a|$ and $2\sqrt2|a|$ gives the stated separation.

Thus the two interval-eigen rescues are not cosmetic. The coarse margins are small enough that a sharp norm extraction changes the logical outcome.

# 512-bit audit

At each of five scales and both channels, the script rebuilds the frozen binary source state using binary powering, computes a floating SVD only to choose the binary factors $L,R$, and performs every subsequent matrix product, normalization, gap lower, and residual enclosure in 512-bit Arb arithmetic. The dependency archive hashes the source builder, both preceding interface papers, and all local scripts.

::: {#tab:audit}
  certificate route        channels       minimum gap ratio        result
  ----------------------- ---------- --------------------------- -----------
  Frobenius extraction       $8$      $25.64$ within that group   certified
  interval-eigen rescue      $2$              $1.02227$           certified
  combined                   $10$             $1.02227$           certified

  : Validated packet closure for the ten frozen binary anchors.
:::

The two rescue radii are approximately $5.473\times10^{-14}$ and $3.006\times10^{-14}$, whereas the corresponding Frobenius uppers are $7.735\times10^{-14}$ and $4.248\times10^{-14}$. The right-channel gap lower is only $6.146\times10^{-14}$, explaining its thin $1.02227$ crossing margin. All imaginary radii returned by the validated Hermitian eigenproblems are at the negligible Arb rounding scale.

![Validated gaps and radii, gap ratios and rescue methods, projector/frame radii, and the two sharp norm extractions.](<../../../../../zeta_mvp0/papers/RH-142-factorized-arb-snapshot-packet-closure/figures/factorized_arb_snapshot_packet.pdf>){#fig:audit width="\\textwidth"}

The packet result is exact relative to the archived binary matrices, but its quality is nonuniform. The coarse right channel gives the RH-141 projector radius $$\frac{e}{g_H-e}=0.9574,$$ and a polar-aligned frame radius about $1.193$. This rules out complete subspace swapping but permits a large rotation. The remaining eight fine or well-separated channels are much tighter.

# Consequence and claim boundary

The finite interface now reads $$\text{binary source model}
 \xrightarrow[\text{512-bit Arb}]{\text{direct normalized Gram}}
 \text{snapshot ball}
 \xrightarrow[\text{factor gap}]{g>2e}
 \text{rank-four projector ball}$$ at all ten anchors. This removes the six universal norm-ball walls of RH-141 without assuming that a floating SVD is exact.

The next map is nonlinear and branch dependent: adaptive width or threshold selection followed by a Ritz/polar update. Strict threshold margins can make that branch locally constant; a threshold contact cannot. Broad coarse projector balls may require a projector-level enclosure rather than a direct frame-coordinate Lipschitz estimate.

We have not enclosed a thresholded recursive update, intervalized the continuum source construction, proved a uniform all-level packet gap, controlled the RH-139 tail tube or normalized-base liminf, established Stage A, constructed a Hilbert--Polya operator, identified zeta zeros, or proved the Riemann Hypothesis.
