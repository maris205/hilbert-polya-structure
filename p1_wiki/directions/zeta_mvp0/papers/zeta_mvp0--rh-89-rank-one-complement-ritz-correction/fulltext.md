---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-89-rank-one-complement-ritz-correction"
canonical_tex: "zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/main.pdf"
source_sha256: "f726e13ddb5747927e4cafd197b80924085d7b2d62ac5ed91f7bec25cec28e25"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rank-One Complement Ritz Correction for Dynamic Packet Energy A Logarithmic-Dimensional Corrector for the RH-88 Dividend

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-88 showed that old-packet prediction need not contract, whereas variational packet reoptimization restores contraction in all ten archived channels. The open question was whether that reoptimization dividend requires a full ambient-dimensional eigensolve. This paper gives a negative answer at the level of both theorem and validated evidence.

  Let $G\ge0$, let $V$ be an isometric rank-$r$ packet, and choose one unit direction $q\perp V$. In the enriched space $Z=[V,q]$, retain the leading rank-$r$ Ritz subspace of the $(r+1)\times(r+1)$ compression $Z^*GZ$. The rank-one complement Ritz theorem states that this packet captures at least as much energy as $V$ and gives a valid upper bound on the full optimal tail. Choosing $q$ as the leading left singular direction of $(I-VV^*)GV$ gives maximal cross-block coupling among all single complement directions.

  At the final RH-88 update, ranks four through seven require compressed dimensions only five through eight. A 256-bit exact-binary-lift audit certifies that one complement direction reproduces more than $96\%$ of the full floating reference correction dividend in every channel. The corrected tail is at most $3.28$ times the full reference tail, and its memory contraction factor remains below $0.24$ in all ten channels.

  Thus the corrector is logarithmic-dimensional and driven by one cross-block direction at the anchors. A uniform cross-block enrichment bound, Stage A, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Rank-One Complement Ritz Correction for Dynamic Packet Energy\
  A Logarithmic-Dimensional Corrector for the RH-88 Dividend
```

## Markdown 正文

**Keywords:** Rayleigh--Ritz; complement enrichment; Ky Fan energy; dynamic packet; cross Gramian; interval arithmetic.

**MSC 2020:** 47A75; 65F15; 15A18; 65G20.

# A small corrector for a large ambient problem

RH-88 factored memory contraction into old-packet prediction and a reoptimization dividend [@WangPredictor2026]. The full corrected packet was obtained from an ambient Gramian. To become an analytic mechanism, the correction must be represented by a small object whose dimension follows the half-logarithmic clock rather than the mesh.

Let $G$ be positive trace class on $\mathcal K$, let $V:\mathbb C^r\to\mathcal K$ be an isometry, and write $P=VV^*$. Choose a unit vector $q\in\operatorname{ran}(I-P)$ and define $Z=[V,q]:\mathbb C^{r+1}\to\mathcal K$.

# Rank-one complement Ritz theorem

[\[thm:ritz\]]{#thm:ritz label="thm:ritz"} Let $C:\mathbb C^r\to\mathbb C^{r+1}$ contain the leading $r$ orthonormal eigenvectors of $H=Z^*GZ$, and put $U=ZC$. Then $$\operatorname{tr}(U^*GU)
 =\sum_{k=1}^r\lambda_k(H)
 \ge\operatorname{tr}(V^*GV).
 \label{eq:capture}$$ Consequently $$E_r(G)\le\operatorname{tr}G-\operatorname{tr}(U^*GU)
 \le\operatorname{tr}G-\operatorname{tr}(V^*GV).
 \label{eq:tails}$$ The corrected packet requires only an $(r+1)$-dimensional eigenproblem.

The old packet range is an admissible rank-$r$ subspace of $\operatorname{ran}Z$. Ky Fan's maximum principle applied to the compressed Hermitian matrix $H$ gives [\[eq:capture\]](#eq:capture){reference-type="eqref" reference="eq:capture"}. The full optimal rank-$r$ captured energy is at least the restricted Ritz energy, yielding [\[eq:tails\]](#eq:tails){reference-type="eqref" reference="eq:tails"} [@Bhatia1997; @Parlett1998].

The theorem controls captured energy without comparing principal angles or small tail gaps. It also explains why a one-pair swap can be too weak: the Ritz solve may rotate all $r$ retained directions jointly after adding only one new complement direction.

[\[prop:cross\]]{#prop:cross label="prop:cross"} Let $Q=I-P$ and $B=QGV$. Among unit $q\in\operatorname{ran}Q$, $$\max_q\left\lVert q^*GV\right\rVert_2=\left\lVert B\right\rVert,$$ and any leading left singular vector of $B$ attains the maximum.

The objective is $\left\lVert q^*B\right\rVert_2$. Its maximum over unit left vectors is the largest singular value of $B$.

This proposition selects a canonical one-dimensional correction from the old-packet/new-Gram cross block.

# Ten-channel 256-bit audit

At the last RH-88 predictor-corrector update, we form the normalized memory Gramian, the old clock-rank packet, and the leading cross-block direction. The corrected packet is obtained from a compressed matrix of dimension $r+1\le8$. All frozen binary Gramians and packet entries are lifted exactly to 256-bit Arb arithmetic. Candidate residual energies are evaluated in the form $$\operatorname{tr}G-2\operatorname{tr}(U^*GU)
 +\operatorname{tr}\bigl((U^*U)(U^*GU)\bigr),$$ which remains a valid rank-$r$ residual even under tiny lifted orthogonality defects.

::: {#tab:audit}
    $\sigma$   Ritz dimension   min dividend fraction   max tail ratio   max contraction
  ---------- ---------------- ----------------------- ---------------- -----------------
        0.16                5                  0.9965            1.481            0.0043
        0.08                6                  0.9788            3.273            0.0212
        0.04                7                  0.9612            1.500            0.0584
        0.02                7                  0.9810            1.034            0.2385
        0.01                8                  0.9973            1.014            0.1900

  : Worst directional channel at each scale, rounded conservatively. The dividend reference is the full binary64 packet at the same update.
:::

The minimum fraction occurs at $\sigma=0.04$ and still exceeds $96\%$. The largest corrected/reference tail ratio occurs at $\sigma=0.08$, where the absolute contraction remains below one percent. At the hardest contraction scale $\sigma=0.02$, the small Ritz corrector remains below $0.24$.

![Reference dividend fraction, corrected contraction, corrected tail ratio, and compressed dimension versus the ambient mesh.](<../../../../../zeta_mvp0/papers/RH-89-rank-one-complement-ritz-correction/figures/rank_one_complement_ritz_correction.pdf>){#fig:audit width="\\textwidth"}

# Boundary and next theorem

The all-level route now has a concrete corrector criterion. It is sufficient to prove that the leading cross-block complement direction yields a fixed fraction of the old-packet Ky Fan deficit, while the resulting corrected factor stays below one after burn-in. Such a bound may be attacked through a Schur complement of the $(P,Q)$ block Gramian rather than full spectral perturbation theory.

RH-89 proves the Ritz and maximal-coupling statements and validates a small corrected packet at ten anchors. It does not prove uniform cross-block enrichment, close Stage A1 or Stage A4, construct a relative determinant or a self-adjoint Hilbert--Polya operator, identify zeta zeros, or prove the Riemann Hypothesis.
