---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-66-block-cross-column-krylov-gram"
canonical_tex: "zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/main.pdf"
source_sha256: "948cfda75d953fb0fca227d911d8500a02dbfc22a865a3d8a097fae369e7062d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Block Cross-Column Krylov Gram Certificates Preserving Packet Phases in Weighted Stein Tails

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-65 showed that a global Lyapunov metric cannot replace peripheral-mode removal. The remaining route is to project first and weight only the final localized residual. Existing RH-62--RH-64 certificates were vector-valued, however, while the phase-aware Schur construction of RH-58--RH-60 is a cross-column Gram problem. Applying a positive upper to each packet column separately destroys the cancellation that made the finite-horizon route effective.

  This paper gives a block remedy. For an isometry $V$, block source $Z=VB+E$, projected matrix $H=V^*AV$, and Galerkin residual $R=AV-VH$, we prove the exact identity $$A^LZ=VH^LB+
   \sum_{j=0}^{L-1}A^{L-1-j}RH^jB+A^LE.$$ In a positive metric with contraction $q<1$, the identity yields (i) a coefficient-aware center-radius certificate retaining all packet phases and (ii) a positive-semidefinite Gram envelope valid simultaneously for every coefficient vector. Both use the cross-column matrices $(H^jB)^*R^*MR(H^jB)$ before positive majorization.

  On a two-column slow-mode cancellation witness at horizon $32$, independent column bounds lose a factor $2.129\times10^{18}$, whereas the block directional certificate has gain $1.0000014$. A 256-bit Arb audit certifies that the independent-column loss exceeds $10^{18}$. On a nonnormal four-step chain, one block level reduces the gain from $11.37$ to $3.90$ and rank-four closure is exact. A six-mode complex-phase model improves from $1.713$ to $1.288$ before exact rank-six closure. The uniform PSD envelope still has gain $410$ in the specially cancelling direction, exposing the next gate: coefficient-adapted positive residual geometry. No production block depth theorem, Stage A1 closure, arithmetic trace formula, or Hilbert--Polya conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Block Cross-Column Krylov Gram Certificates\
  Preserving Packet Phases in Weighted Stein Tails
```

## Markdown 正文

**Keywords:** block Krylov method; cross Gramian; phase cancellation; Lyapunov metric; Stein tail; packet fusion.

**MSC 2020:** 47A10; 47B65; 65F35; 93B07; 93D05.

# Introduction

The directional Hardy route is intrinsically multi-source. Schur packets produce columns $z_1,\ldots,z_r$ and a coefficient vector $a$; the physical quantity is the norm of the coherent sum $Za$, not the sum of the packet norms. RH-58 kept this information in a time-ordered cross Gram, while RH-60 retained it over a finite horizon. The terminal estimates of RH-62--RH-64 then returned to one source vector [@WangSchurGram2026; @WangWeightedResidual2026].

RH-65 determines the proper order: peripheral or reached slow directions must be removed before a terminal metric is applied [@WangMetricConditioning2026]. To transfer that order to packets, the projection must be block-valued. Block Krylov spaces are standard for multiple right-hand sides [@Saad2003]; the point here is a specific positive Gram certificate that does not scalarize the columns prematurely.

## Contributions and boundary {#contributions-and-boundary .unnumbered}

1.  We prove a block Galerkin power identity with an explicit source reconstruction residual.

2.  We derive a directional center-radius certificate and a uniform PSD Gram envelope in a Lyapunov metric.

3.  We identify exact cancellation and invariant-block closure criteria.

4.  We audit three finite models and isolate the gap between a selected physical direction and one envelope valid for all directions.

All matrix theorems below are finite-dimensional. The model calculations are deterministic binary64 evidence; only the displayed cancellation witness has a 256-bit interval audit.

# Block power identity {#sec:identity}

Let $A\in\mathbb C^{n\times n}$, $Z\in\mathbb C^{n\times r}$, and let $V\in\mathbb C^{n\times k}$ satisfy $V^*V=I$. Define $$B=V^*Z,\qquad E=Z-VB,\qquad
 H=V^*AV,\qquad R=AV-VH.
 \label{eq:block-data}$$ For a block Krylov basis, $V$ spans a numerical approximation to $\operatorname{span}\{Z,AZ,\ldots,A^{d-1}Z\}$, but the next identity does not require that construction.

[\[prop:power\]]{#prop:power label="prop:power"} For every integer $L\ge0$, $$A^LZ=Y_L+\mathcal R_L,
 \qquad Y_L=VH^LB,
 \label{eq:center}$$ where $$\mathcal R_L=
 \sum_{j=0}^{L-1}A^{L-1-j}RH^jB+A^LE.
 \label{eq:block-remainder}$$

The relation $AV=VH+R$ implies by induction $$A^LVB=VH^LB+\sum_{j=0}^{L-1}A^{L-1-j}RH^jB.$$ Add $A^LE$ and use $Z=VB+E$.

The identity keeps every source column inside $B$ and $H^jB$. No triangle inequality has yet been applied across packets.

# Cross-column weighted certificates {#sec:certificate}

Let $M\succ0$ and suppose $$q=\left\lVert M^{1/2}AM^{-1/2}\right\rVert_2<1.
 \label{eq:metric-contraction}$$ The canonical equation $M-A^*MA=I$ is one sufficient construction [@ZhouDoyleGlover1996]. Put $$Q=R^*MR,qquad Q_E=E^*ME,qquad C_j=H^jB.
 \label{eq:residual-grams}$$

[\[thm:directional\]]{#thm:directional label="thm:directional"} For every $a\in\mathbb C^r$, $$\left\lVert A^LZa\right\rVert_M
 \le \left\lVert Y_La\right\rVert_M+\rho_L(a),
 \label{eq:directional-upper}$$ where $$\rho_L(a)=
 \sum_{j=0}^{L-1}q^{L-1-j}
 \sqrt{a^*C_j^*QC_ja}
 +q^L\sqrt{a^*Q_Ea}.
 \label{eq:directional-radius}$$ Consequently $$a^*(A^LZ)^*M(A^LZ)a
 \le\left(\sqrt{a^*Y_L^*MY_La}+\rho_L(a)\right)^2.
 \label{eq:directional-energy}$$

Apply [\[eq:metric-contraction\]](#eq:metric-contraction){reference-type="eqref" reference="eq:metric-contraction"} to each propagated term in [\[eq:block-remainder\]](#eq:block-remainder){reference-type="eqref" reference="eq:block-remainder"}. Since $\left\lVert RC_ja\right\rVert_M^2=a^*C_j^*QC_ja$, the triangle inequality gives [\[eq:directional-upper\]](#eq:directional-upper){reference-type="eqref" reference="eq:directional-upper"}; squaring gives [\[eq:directional-energy\]](#eq:directional-energy){reference-type="eqref" reference="eq:directional-energy"}.

For a certificate valid for every coefficient simultaneously, choose positive weights satisfying $$\theta_0+\cdots+\theta_{L-1}+\theta_E=1,$$ and define $$\mathcal C_L(\theta)=
 \sum_{j=0}^{L-1}
 \frac{q^{2(L-1-j)}}{\theta_j}C_j^*QC_j
 +\frac{q^{2L}}{\theta_E}Q_E.
 \label{eq:residual-envelope}$$

[\[thm:gram\]]{#thm:gram label="thm:gram"} The residual and full block Grams obey $$\begin{aligned}
 \mathcal R_L^*M\mathcal R_L
 &\preceq \mathcal C_L(\theta),
 \label{eq:residual-loewner}\\
 (A^LZ)^*M(A^LZ)
 &\preceq
 (1+\eta)Y_L^*MY_L+(1+\eta^{-1})\mathcal C_L(\theta)
 \label{eq:full-loewner}\end{aligned}$$ for every $\eta>0$.

For a fixed $a$, apply the weighted Cauchy inequality $(\sum_i x_i)^2\le\sum_i x_i^2/\theta_i$ to the summands in [\[eq:directional-radius\]](#eq:directional-radius){reference-type="eqref" reference="eq:directional-radius"}. This proves $\left\lVert\mathcal R_La\right\rVert_M^2\le a^*\mathcal C_L(\theta)a$ for every $a$, which is [\[eq:residual-loewner\]](#eq:residual-loewner){reference-type="eqref" reference="eq:residual-loewner"}. The operator Young inequality $$(X+W)^*(X+W)\preceq
 (1+\eta)X^*X+(1+\eta^{-1})W^*W$$ with $X=M^{1/2}Y_L$ and $W=M^{1/2}\mathcal R_L$ then gives [\[eq:full-loewner\]](#eq:full-loewner){reference-type="eqref" reference="eq:full-loewner"}.

The implementation chooses trace-optimal scalar weights: $$\theta_j\propto q^{L-1-j}
 \sqrt{\operatorname{tr}(C_j^*QC_j)},
 \qquad
 \theta_E\propto q^L\sqrt{\operatorname{tr}Q_E},
 \label{eq:trace-weights}$$ and then $\eta=\sqrt{\operatorname{tr}\mathcal C_L/
\operatorname{tr}(Y_L^*MY_L)}$. These choices minimize the traces of the two successive positive envelopes. They need not be optimal for a selected coefficient direction.

[\[cor:cancellation\]]{#cor:cancellation label="cor:cancellation"} If a coefficient vector $a$ satisfies $$Ea=0,qquad RH^jBa=0\quad(0\le j<L),
 \label{eq:annihilation}$$ then $\rho_L(a)=0$ and the directional certificate is exact. This may hold even when none of the individual source columns has zero residual.

Every quadratic term in [\[eq:directional-radius\]](#eq:directional-radius){reference-type="eqref" reference="eq:directional-radius"} vanishes.

If $E=R=0$, the block subspace is invariant and both certificates are exact for all coefficient vectors.

# Finite-model audit {#sec:audit}

The code builds $V$ by an SVD of the block Krylov matrix and uses the canonical Lyapunov metric. Four uppers are compared: the directional block certificate, the uniform PSD Gram evaluated in the physical direction, independent scalar-column certificates followed by Minkowski, and a rank-matched Krylov certificate built only after fusing the selected source.

::: {#tab:gains}
  model                     rank   block dir.   PSD Gram            independent      fused
  ----------------------- ------ ------------ ---------- ---------------------- ----------
  cancelling slow pair         2     1.000001    410.159   $2.129\times10^{18}$   1.000000
  nonnormal chain              3     3.899145   3.950049                11.3650   5.007690
  complex phase packets        3     1.288471   1.295052                1.71263   1.129739

  : One-level directional energy gains.
:::

The cancellation witness has $$A=\operatorname{diag}(0.995,0.55,0.2),\qquad
 Z=\begin{pmatrix}1&-1\\1&1\\0.2&-0.2\end{pmatrix},\qquad
 a=\binom11.$$ Thus $Za=2e_2$: the slow and fast components cancel before propagation. The block space contains the invariant fused direction and satisfies [\[cor:cancellation\]](#cor:cancellation){reference-type="ref" reference="cor:cancellation"}; floating-point orthogonalization leaves only a $1.4\times10^{-6}$ relative gain. Separate columns must each carry the $0.995$ mode and therefore lose more than eighteen orders of magnitude. A 256-bit Arb calculation certifies the cancellation, positivity of the exact fused energy, residual annihilation on the fused axis, and an independent- column lower loss exceeding $10^{18}$.

The same example reveals a distinction. The trace-global PSD envelope must also cover coefficient vectors that do not cancel the slow mode, so its evaluation at $a=(1,1)$ still has gain $410$. The theorem is valid; the choice of one global positive envelope is geometrically mismatched to a special physical direction.

![Left: one-level gains, including the catastrophic independent-column loss in the cancellation witness. Right: increasing block rank closes the nonnormal and complex-phase models, while independent scalarization retains a packet-fusion penalty.](<../../../../../zeta_mvp0/papers/RH-66-block-cross-column-krylov-gram/figures/block_cross_column_krylov_gram.pdf>){#fig:audit width="98%"}

For the nonnormal chain, rank three improves the directional gain from the independent value $11.37$ to $3.90$; rank four is exact. For the six-mode phase model, rank three improves $1.713$ to $1.288$ and rank six is exact. The minimum eigenvalues of the numerical PSD slack are nonnegative up to $4.4\times10^{-18}$ rounding.

# Route consequence {#sec:route}

RH-66 repairs the cross-column scalarization loss. The viable terminal architecture is now $$\text{block Krylov center}
 \longrightarrow \text{coherent physical coefficient}
 \longrightarrow \text{localized weighted residual}.
 \label{eq:architecture}$$ For a fixed physical coefficient, [\[thm:directional\]](#thm:directional){reference-type="ref" reference="thm:directional"} can be nearly exact even when every columnwise estimate fails.

The unresolved question is stronger: Stage A1 ultimately needs a positive object that can be transferred through packet and continuum limits. The trace-global Young envelope in [\[thm:gram\]](#thm:gram){reference-type="ref" reference="thm:gram"} can overpay for coefficient directions irrelevant to the physical fusion. The next gate is therefore a weighted block residual stress test comparing directional, low-rank cone, and full PSD formulations. It must determine how much positivity is truly needed by the downstream determinant argument.

# No arithmetic or Hilbert--Polya conclusion

This paper constructs no self-adjoint operator, no $T\log T$ counting law, no prime-power trace formula, and no completed-zeta identity. It makes no Hilbert--Polya or Riemann-hypothesis claim. Stage A1 and unconditional Stage A4 remain open.

# Reproducibility

The directory contains block algebra, tests, the model pilot, Arb audit, figures, hashes, and publication artifacts. The principal commands are:

    pytest -q -p no:cacheprovider
    python experiments/run_block_gram_pilot.py
    python experiments/run_arb_cancellation_audit.py
    MPLBACKEND=Agg python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The block identities and positive envelopes are analytic. The model gains are binary64 evidence. Uniform physical-family block depth, interval- certified production packet transfer, Stage A1, unconditional Stage A4, a self-adjoint Hilbert--Polya operator, an arithmetic trace formula, and a zeta-zero identity remain open.
