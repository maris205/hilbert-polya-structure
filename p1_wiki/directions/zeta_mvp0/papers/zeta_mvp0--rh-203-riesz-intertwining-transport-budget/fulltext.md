---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-203-riesz-intertwining-transport-budget"
canonical_tex: "zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget/main.pdf"
source_sha256: "e815ffb931ba2b7d383b2bca73d4b0830b1eae024e433cbf5da134dd63033654"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Riesz Intertwining and the Two-Term Channel Transport Budget Exact Identities Behind the RH-202 Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-203-riesz-intertwining-transport-budget/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-202 showed that the physical edge quartet is not carried between adjacent levels by the unmodified Haar embedding. This paper isolates the exact mechanism. For operators $A_c,A_f$ and a rectangular embedding $J$, set $E=A_fJ-JA_c$. On the common resolvent set we prove $$(z-A_f)^{-1}J-J(z-A_c)^{-1}
   =(z-A_f)^{-1}E(z-A_c)^{-1}.$$ Integration gives the corresponding Riesz-projector identity and a contour bound. For source states we further prove an exact two-term decomposition: channel transport equals a source defect passed through the fine projector plus the projector-transport defect acting on the coarse source. A dual formula controls observations and residues.

  A 240-case complex audit has zero identity failures; maximum residuals are $2.42\times10^{-16}$ for the resolvent formula and $1.12\times10^{-14}$ for the channel decomposition. Applied to RH-202, the identity explains why a contour estimate cannot close without a new map: the quartet-restricted intertwining defects are $0.236$--$0.656$, while the source defect is at least $0.781$. The paper supplies an exact criterion, not a physical resolvent bound or an all-level transport theorem.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Riesz Intertwining and the Two-Term Channel Transport Budget\
  Exact Identities Behind the RH-202 Obstruction
```

## Markdown 正文

# Rectangular interlevel problem

Let $X_c=\mathbb C^{n_c}$ and $X_f=\mathbb C^{n_f}$ with $n_f\ge n_c$. We do not assume that $A_c$ is a compression of $A_f$. Let $$\label{eq:data}
 A_c:X_c\to X_c,\qquad A_f:X_f\to X_f,
 \qquad J:X_c\to X_f.$$ The basic defect is $$\label{eq:E}
 E=A_fJ-JA_c.$$ When $J$ is the Haar embedding, $E$ measures both discretization change and the physical change in noise scale. This distinction matters: refinement alone does not imply $E\to0$.

The standard perturbation theory of spectral subspaces is usually stated for two operators on one space [@Kato1995; @StewartSun1990]. The rectangular identity below is the appropriate interlevel form.

# Resolvent intertwining identity

Write $R_f(z)=(zI-A_f)^{-1}$ and $R_c(z)=(zI-A_c)^{-1}$.

[\[thm:resolvent\]]{#thm:resolvent label="thm:resolvent"} If $z\in\rho(A_f)\cap\rho(A_c)$, then $$\label{eq:resolvent}
 R_f(z)J-JR_c(z)=R_f(z)ER_c(z).$$

Using $R_fA_f=zR_f-I$ and $A_cR_c=zR_c-I$, $$\begin{aligned}
 R_fER_c
 &=R_f(A_fJ-JA_c)R_c\\
 &=(zR_f-I)JR_c-R_fJ(zR_c-I)\\
 &=R_fJ-JR_c.\end{aligned}$$ No equality of dimensions or invertibility of $J$ is used.

The formula separates geometry from spectral amplification. A moderate $E$ can still produce a large projector defect when either resolvent is large, as is common for nonnormal operators [@TrefethenEmbree2005].

# Riesz projectors and a contour budget

Let $\Gamma$ be a positively oriented rectifiable contour contained in both resolvent sets. Define $$\label{eq:riesz}
 P_f=\frac{1}{2\pi i}\int_\Gamma R_f(z)\,dz,
 \qquad
 P_c=\frac{1}{2\pi i}\int_\Gamma R_c(z)\,dz.$$

[\[cor:riesz\]]{#cor:riesz label="cor:riesz"} The exact interlevel projector defect is $$\label{eq:projector-identity}
 P_fJ-JP_c
 =\frac{1}{2\pi i}\int_\Gamma R_f(z)ER_c(z)\,dz.$$ Consequently, $$\label{eq:projector-bound}
 \left\lVert P_fJ-JP_c\right\rVert
 \le \frac{|\Gamma|}{2\pi}
 \sup_{z\in\Gamma}\left\lVert R_f(z)\right\rVert
 \sup_{z\in\Gamma}\left\lVert R_c(z)\right\rVert\left\lVert E\right\rVert.$$

The same contour must isolate the intended clusters at both levels. A post hoc contour around two unrelated packets would make the formula true but would not establish branch continuity.

# Source-channel decomposition

Matrix source states introduce a second embedding. Let $S_c\in\mathbb C^{n_c\times m_c}$, $S_f\in\mathbb C^{n_f\times m_f}$ and $K:\mathbb C^{m_c}\to\mathbb C^{m_f}$. Define $$\label{eq:source-defect}
 \Delta_S=S_f-JS_cK^*.$$

[\[thm:channel\]]{#thm:channel label="thm:channel"} For arbitrary projectors $P_c,P_f$, $$\label{eq:channel-identity}
 P_fS_f-JP_cS_cK^*
 =P_f\Delta_S+(P_fJ-JP_c)S_cK^*.$$ If $K$ is an isometry, then $$\label{eq:channel-bound}
 \left\lVert P_fS_f-JP_cS_cK^*\right\rVert_F
 \le \left\lVert P_f\right\rVert\left\lVert\Delta_S\right\rVert_F
 +\left\lVert P_fJ-JP_c\right\rVert\left\lVert S_c\right\rVert_F.$$

Add and subtract $P_fJS_cK^*$ and apply submultiplicativity. No spectral assumption is needed for the algebraic identity.

Thus a good projector map is insufficient when the physical source itself changes substantially. Conversely, a perfectly embedded source cannot repair a bad spectral projector map.

# Observation and residue budget

Let $O_c:\mathbb C^{n_c}\to\mathbb C^{m_c}$ and $O_f:\mathbb C^{n_f}\to\mathbb C^{m_f}$. Define $$\label{eq:obs-defect}
 \Delta_O=O_f-KO_cJ^*.$$ Applying Theorem [\[thm:channel\]](#thm:channel){reference-type="ref" reference="thm:channel"} to adjoints gives a two-term formula for $P_f^*O_f^*-JP_c^*O_c^*K^*$.

More explicitly, with $\Delta_{O^*}=O_f^*-JO_c^*K^*$, $$\label{eq:dual-channel}
 P_f^*O_f^*-JP_c^*O_c^*K^*
 =P_f^*\Delta_{O^*}+(P_f^*J-JP_c^*)O_c^*K^*.$$

The transfer residue of a cluster is $$\label{eq:residue}
 r=\operatorname{tr}(OP S).$$ After inserting and subtracting transported source, observation, and projector factors, $r_f-r_c$ is bounded by three physical defects multiplied by the remaining factor norms. This makes clear that residue transport is strictly more demanding than eigenvalue matching.

There is also a direct channel-state bound. Put $\widehat X_c=JX_cK^*$ and $\widehat Y_c=JY_cK^*$. Isometry of $J,K$ preserves the coarse Frobenius pairing, and therefore $$\begin{aligned}
\label{eq:residue-bound}
 |r_f-r_c|
 &\le \left\lVert Y_f-\widehat Y_c\right\rVert_F\left\lVert X_f\right\rVert_F
 +\left\lVert\widehat Y_c\right\rVert_F\left\lVert X_f-\widehat X_c\right\rVert_F.\end{aligned}$$ Combining [\[eq:channel-bound\]](#eq:channel-bound){reference-type="eqref" reference="eq:channel-bound"}, [\[eq:dual-channel\]](#eq:dual-channel){reference-type="eqref" reference="eq:dual-channel"}, and [\[eq:residue-bound\]](#eq:residue-bound){reference-type="eqref" reference="eq:residue-bound"} gives a fully typed finite residue budget. It requires no eigenvector gauge, only projector, source, and observation estimates.

# Identity audit

We generated 120 random complex rectangular operator pairs with dimensions $2$--$7$, random isometric embeddings, and spectral parameters well outside both spectra. The maximum residual in [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"} is $$2.4157\times10^{-16}.$$ An independent 120-case audit used arbitrary projectors, sources, and row and column isometries in [\[eq:channel-identity\]](#eq:channel-identity){reference-type="eqref" reference="eq:channel-identity"}. Its maximum Frobenius identity residual is $1.1178\times10^{-14}$. All 240 cases pass the $10^{-10}$ gate.

These checks validate implementation, not the physical assumptions of a common contour.

# Application to the physical quartet

RH-202 gives the following inherited ranges:

  quantity                                   finite range or extremum
  ---------------------------------------- --------------------------
  quartet-restricted relative $E$ defect         $0.23623$--$0.65573$
  minimum relative source defect                            $0.78134$
  maximum oblique-projector defect                          $2.29068$
  maximum relative residue displacement                     $8.18374$

The right side of [\[eq:projector-bound\]](#eq:projector-bound){reference-type="eqref" reference="eq:projector-bound"} cannot be small merely from these data. Moreover, the source term in [\[eq:channel-bound\]](#eq:channel-bound){reference-type="eqref" reference="eq:channel-bound"} is already order one before resolvent amplification is considered.

This is the exact explanation of the RH-202 obstruction: the naive map fails in at least two independent places. Improving only the contour calculation would not make the source defect disappear.

# Necessary conditions for a successful map

A future scale-dependent map $J_\sigma$ should provide all of:

1.  a common contour with controlled $R_f$ and $R_c$;

2.  a small intertwining defect $A_fJ_\sigma-J_\sigma A_c$ on the packet;

3.  compatible row and column source embeddings;

4.  a dual observation estimate;

5.  nonvanishing residues after transport.

These are sufficient ingredients for finite packet transport. Uniform versions would still be needed for Gate A.

# Norm choice and validation strategy

Equation [\[eq:projector-bound\]](#eq:projector-bound){reference-type="eqref" reference="eq:projector-bound"} is valid in every subordinate operator norm. Spectral norms are natural for principal-angle control; Frobenius norms are natural for matrix channel states. Mixing them is legitimate only with the explicit submultiplicative steps used in [\[eq:channel-bound\]](#eq:channel-bound){reference-type="eqref" reference="eq:channel-bound"}.

For a validated implementation, one should bound the resolvents directly on $\Gamma$, not infer them from distance to the spectrum. The latter is unsafe for nonnormal matrices. A quadrature approximation also needs a separate integration remainder or an argument-principle count. These requirements explain why the exact identity is a roadmap rather than a certificate by itself.

# Claim boundary and next step

The resolvent, projector, and channel identities are exact finite theorems. The physical use is diagnostic only: no supremum resolvent bound or interval Riesz contour has been supplied. RH-204 next asks a weaker question that does not require state transport: whether the two conjugate spectral branches themselves possess a unique correspondence across levels and channels.
