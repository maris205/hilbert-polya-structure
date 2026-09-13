---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-158-adaptive-lag-reset-cross-bridge"
canonical_tex: "zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/main.pdf"
source_sha256: "88dd74ec250c4c7b8874bda3ebd9460137ef4e1c3bf3d116eb9d27341ed5d282"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Adaptive-Lag Reset Cross Bridge A Shift-Invariant Perturbation Bound and Complete Finite Four-Mode Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a contemporaneous spectral reset $P_t$ of a geometric memory $M_t=R_t+T_t$, RH-157 found the exact cancellation $(I-P_t)R_tP_t=-(I-P_t)T_tP_t$. We show that bounded lag removes this obstruction. If $P_{t-k}$ is the spectral reset $k$ steps earlier, then $$(I-P_{t-k})R_tP_{t-k}
   =\sum_{j=0}^{k-1}\eta^j(I-P_{t-k})S_{t-j}P_{t-k}
    -(I-P_{t-k})T_tP_{t-k}.$$ The recent innovations now survive. We also replace the origin-dependent projector perturbation cost $2\|\widehat R\|\epsilon$ by the shift-invariant, asymptotically sharp cost $(\lambda_{\max}(\widehat R)-\lambda_{\min}(\widehat R))\epsilon$.

  An outward audit evaluates 694 candidates over 120 update targets and chooses the largest certified normalized fourth-cross base among lags at most eight. Lag one certifies only 76 targets; horizons two through seven certify 84, 92, 101, 106, 112, and 117. Horizon eight certifies all 120, including all 62 delayed-half and all 10 terminal targets. The smallest selected base is $2.5874\times10^{-14}$ and the weakest fourth-singular lower is $3.1808\times10^{-16}$. Thus the finite lagged cross bridge closes, but the very small worst margin does not prove an all-level bounded-lag law or the remaining outward assembly.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Adaptive-Lag Reset Cross Bridge\
  A Shift-Invariant Perturbation Bound and Complete Finite Four-Mode Atlas
```

## Markdown 正文

# Lag exposes the recent innovations

Let $S_t\succeq0$ be normalized snapshot Grams and let $M_t=S_t+\eta M_{t-1}$, with $0<\eta<1$ and $M_{-1}=0$. For a recent depth $d$, put $T_t=\eta^dM_{t-d}$ when $t\geq d$ and $T_t=0$ otherwise, and set $R_t=M_t-T_t$. Write $J(P,A)=(I-P)AP$.

[\[thm:lag\]]{#thm:lag label="thm:lag"} For $1\leq k\leq t$, let $P_{t-k}$ be any spectral projector of $M_{t-k}$. Then $$J(P_{t-k},R_t)=\sum_{j=0}^{k-1}\eta^jJ(P_{t-k},S_{t-j})
                  -J(P_{t-k},T_t).$$

Iteration of the memory recursion gives $M_t=\sum_{j=0}^{k-1}\eta^jS_{t-j}+\eta^kM_{t-k}$. Spectral invariance gives $J(P_{t-k},M_{t-k})=0$. Apply $J(P_{t-k},\cdot)$ and subtract the tail.

At $k=0$ the innovation sum is empty and one recovers the RH-157 tail-only identity. At positive lag, current innovations need not preserve the old packet. This is the precise mechanism by which lag can restore cross rank.

# A shift-invariant cross-action ball

Suppose $Q$ is an exact orthogonal projector, $P$ its center, $\|Q-P\|\leq\epsilon$, and $\|A-\widehat A\|\leq r_A$, with $\widehat A$ Hermitian.

[\[thm:center\]]{#thm:center label="thm:center"} Let $\Delta(\widehat A)=\lambda_{\max}(\widehat A)-
\lambda_{\min}(\widehat A)$. Then $$\|J(Q,A)-J(P,\widehat A)\|
 \leq \rho_A:=r_A+\Delta(\widehat A)\epsilon.$$ Consequently $$\sigma_j(J(Q,A))\in
 \bigl[(\sigma_j(J(P,\widehat A))-\rho_A)_+,
       \sigma_j(J(P,\widehat A))+\rho_A\bigr].$$

Changing $A$ at fixed $Q$ costs at most $r_A$. Since $J(P,A-cI)=J(P,A)$, choose $c=(\lambda_{\max}(\widehat A)+\lambda_{\min}(\widehat A))/2$ and write $B=\widehat A-cI$. Expansion gives $$J(Q,B)-J(P,B)=(P-Q)BQ+(I-P)B(Q-P).$$ Its norm is at most $2\|B\|\epsilon=\Delta(\widehat A)\epsilon$. Singular-value perturbation finishes the proof [@Bhatia1997; @StewartSun1990].

[\[prop:sharp\]]{#prop:sharp label="prop:sharp"} The coefficient $\Delta(\widehat A)$ in Theorem [\[thm:center\]](#thm:center){reference-type="ref" reference="thm:center"} cannot be replaced universally by a smaller constant depending only on the spectral endpoints.

Take $A=\operatorname{diag}(a,b)$, let $P$ project onto the first coordinate, and rotate $P$ through angle $\theta$ to obtain $Q_\theta$. Then $\|Q_\theta-P\|=\sin\theta$ while $\|J(Q_\theta,A)-J(P,A)\|=|a-b|\sin\theta\cos\theta$. The ratio tends to $|a-b|=\Delta(A)$ as $\theta\to0$.

For the depth-five split, inherited memory balls give $r_{R,t}=r_{M,t}$ for $t<5$ and $r_{R,t}=r_{M,t}+\eta^5r_{M,t-5}$ otherwise. Theorem [\[thm:center\]](#thm:center){reference-type="ref" reference="thm:center"} therefore uses only already certified reset and matrix balls; it assumes no independence between them.

# Finite adaptive selection and transport

For each target $t$ and candidate $1\leq k\leq\min(8,t)$, define $$\ell_{4,t,k}=(\sigma_4(\widehat J_{t,k})-\rho_{t,k})_+,
 \qquad
 u_{1,t,k}=\sigma_1(\widehat J_{t,k})+\rho_{t,k},
 \qquad b_{t,k}=\ell_{4,t,k}/u_{1,t,k}.$$ We choose a maximizer of $b_{t,k}$, breaking ties toward shorter lag. This is a finite deterministic optimization, not a fitted asymptotic law. By Theorem [\[thm:center\]](#thm:center){reference-type="ref" reference="thm:center"}, $\ell_{4,t,k}>0$ certifies four exact cross modes.

The older packet can also be moved to the current reset frame. If consecutive frame overlaps have certified lowers $a_s>0$, then the $k$-step coordinate transport has $$\sigma_{\min}(C_{t-k+1}\cdots C_t)\geq\prod_{s=t-k+1}^{t}a_s>0.$$ This follows from multiplicativity of least singular values. It proves finite invertibility of every selected path, but not a scale-independent condition number.

# The 120-target audit

The audit covers five frozen scales, two sides, and endpoints $4,6,11,17,22$, hence 120 positive-time targets. There are 694 admissible lag candidates. Table [1](#tab:horizons){reference-type="ref" reference="tab:horizons"} shows the exact prefix counts. The old uncentered radius leaves two targets unresolved even at lag eight; scalar centering supplies their missing margins.

::: {#tab:horizons}
         maximum lag           1    2    3     4     5     6     7     8
  ------------------------- ---- ---- ---- ----- ----- ----- ----- -----
    all targets, centered     76   84   92   101   106   112   117   120
   delayed half, centered     18   26   34    43    48    54    59    62
     terminals, centered       0    0    0     4     4     4     7    10
   all targets, uncentered    73   83   91    99   105   111   116   118

  : Four-mode certificates as the allowed lag horizon grows.
:::

The selected-lag histogram is $(31,19,11,7,10,8,19,15)$. Selected normalized bases range from $2.5874\times10^{-14}$ to $0.52247$, with median $0.03710$. Their transport overlap products remain positive, with minimum $1.4955\times10^{-8}$ and maximum inverse upper $6.6866\times10^7$. The weakest point is the $\sigma=0.16$ left terminal: its lag-four nominal fourth singular value is $6.4322\times10^{-15}$ and its centered radius is $6.1141\times10^{-15}$, leaving only $3.1808\times10^{-16}$. It is a valid finite certificate and simultaneously a warning against extrapolation.

![Lag-horizon closure, selected lag distribution, centered radii, and the joint cross/transport conditioning of the finite atlas.](<../../../../../zeta_mvp0/papers/RH-158-adaptive-lag-reset-cross-bridge/figures/adaptive_lag_reset_cross_bridge.pdf>){#fig:audit width="\\textwidth"}

# Route consequence and boundary

RH-158 repairs the exact contemporaneous cancellation without abandoning spectral resets: a packet at most eight steps old provides four certified cross modes at every frozen update target, and consecutive reset overlaps provide finite coordinate transport. This is the first complete finite bridge between the reset atlas and the projected-cross object used by the directional route.

What remains is substantial. The selected lag is data-dependent, the minimum margin and path overlap are nonuniform, and no theorem yet prevents the required lag from growing at finer scales. Nor has the lagged cross been inserted into every later cap, quotient, and determinant estimate. We do not claim an all-level bounded-lag law, Stage A, a Hilbert--Polya operator, zeta-zero identification, or the Riemann Hypothesis.
