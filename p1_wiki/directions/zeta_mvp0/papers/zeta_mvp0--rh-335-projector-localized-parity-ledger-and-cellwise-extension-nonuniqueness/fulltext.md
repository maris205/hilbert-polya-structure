---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness"
canonical_tex: "zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness/main.pdf"
source_sha256: "81ba7bb8bb9f33cf3c661731408c16321f248d90e879f669cf8053c0c2a04bfc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projector-Localized Parity Ledgers and Cellwise Extension Nonuniqueness

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-335-projector-localized-parity-ledger-and-cellwise-extension-nonuniqueness/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The repaired physical observation map localizes the noisy cyclic trace and the deterministic flat trace on the same folded basepoint cells, but its global parity scalar has no canonical cellwise allocation. We freeze one finite-order gauge using the rank-one Riesz projector of the real noisy parity eigenvalue. The set function $\pi_\sigma(J)=\operatorname{Tr}(M_JE_{-,\sigma})$ is a real finite signed measure, is invariant under independent left/right eigenvector rescaling, and has total mass one. Adding its weighted parity correction to each localized raw defect gives cells whose sum is exactly $c^H_{\sigma,n}-c^H_n$. At the first alias the Hardy full-trace constituent is the cell sum minus the counterloop alias packet; the minus sign cannot be discarded. A positive rational row-stochastic fixture verifies the exact ledger and proves that local Perron/parity deflation need not commute with a window even though the commutator trace is zero. We then prove that a global parity scalar admits infinitely many local signed extensions: any nonzero zero-total signed measure changes cells while preserving every partition aggregate. Thus the projector-density allocation is a frozen gauge, not a canonical physical parity localization or deterministic/noisy projector transport. Finally, the planned adapted-norm upper-exponent route remains not testable because all-leg operator errors, physical observation/product norm upper bounds, and a subcritical stability-weight upper exponent are absent. All statements are fixed-order identities or scoped negative results; no moving-order trace replacement or Riemann-hypothesis conclusion is obtained.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Projector-Localized Parity Ledgers\
  and Cellwise Extension Nonuniqueness
```

## Markdown 正文

# Frozen finite-order data type

Let $(X,m)$ be a measure space and $\mathcal H=L^2(X,m)$. For fixed noise $\sigma>0$, let $K_\sigma$ be a real operator whose powers of order $n\ge2$ are trace class. Assume that $1$ and $\lambda_-(\sigma)\in\mathbb R$ are simple eigenvalues with rank-one Riesz projectors $E_{0,\sigma}$ and $E_{-,\sigma}$, respectively. The operator $E_{-,\sigma}$ is the projector itself, not $\lambda_-(\sigma)E_{-,\sigma}$.

For a measurable set $J\subset X$, let $M_J$ denote multiplication by $\mathbf 1_J$ and put $$\label{eq:L-local}
 L_{\sigma,n}(J)=\operatorname{Tr}(M_JK_\sigma^n),\qquad n\ge2.$$ The RH-334 physical observation map supplies the corrected deterministic localization $P_n^{\rm abs}(J)$, with $X=[0,1]$ in that application [@WangObservation2026]. It is additive on every frozen measurable partition and satisfies $P_n^{\rm abs}(X)=P_n$.

We retain the Hardy coefficients and signs fixed in RH-326 [@WangFirstAlias2026]: $$\begin{aligned}
 c^H_{\sigma,n}
 &=r_H^{-n}\{\operatorname{Tr}K_\sigma^n-1-\lambda_-(\sigma)^n\},
 \label{eq:c-noisy}\\
 c^H_n
 &=r_H^{-n}\{P_n-1-(-1)^n\}.
 \label{eq:c-deterministic}\end{aligned}$$ The scalar Perron terms $-1$ cancel in their difference. That global scalar cancellation will not be confused with a commutation statement for localized projectors.

# The parity Riesz-projector measure

Choose real right and left parity eigenfunctions $v_\sigma,w_\sigma$. Without fixing their normalization, the rank-one projector has the form $$\label{eq:rank-one}
 E_{-,\sigma}h
 =\frac{v_\sigma\langle w_\sigma,h\rangle}
 {\langle w_\sigma,v_\sigma\rangle},
 \qquad \langle w_\sigma,v_\sigma\rangle\ne0.$$

[\[thm:projector-measure\]]{#thm:projector-measure label="thm:projector-measure"} The set function $$\label{eq:pi-def}
 \boxed{\pi_\sigma(J)=\operatorname{Tr}(M_JE_{-,\sigma})}$$ is a real finite signed measure. It has density $$\label{eq:pi-density}
 d\pi_\sigma(x)
 =\frac{v_\sigma(x)w_\sigma(x)}
 {\langle w_\sigma,v_\sigma\rangle}\,dm(x),$$ is invariant under independent nonzero rescalings of either eigenfunction, and satisfies $$\label{eq:pi-total}
 \pi_\sigma(X)=1.$$ It need not be positive.

The product $v_\sigma w_\sigma$ belongs to $L^1(X,m)$ by Cauchy--Schwarz. The standard rank-one trace formula applied to $M_JE_{-,\sigma}$ gives [\[eq:pi-density\]](#eq:pi-density){reference-type="eqref" reference="eq:pi-density"}; hence countable additivity, finiteness, and reality follow. Replacing $(v_\sigma,w_\sigma)$ by $(av_\sigma,bw_\sigma)$ multiplies both numerator and denominator by $ab$, so the measure is unchanged. Finally, $\pi_\sigma(X)=\operatorname{Tr}E_{-,\sigma}=1$ because a rank-one projector has one nonzero eigenvalue, equal to one. The product $v_\sigma w_\sigma$ may change sign, so positivity does not follow.

[\[rem:frozen-gauge\]]{#rem:frozen-gauge label="rem:frozen-gauge"} Because [\[eq:pi-total\]](#eq:pi-total){reference-type="eqref" reference="eq:pi-total"} holds, one may write $$(-1)^n=\sum_{J\in\mathcal P}(-1)^n\pi_\sigma(J)$$ for any finite partition $\mathcal P$. This uses the *noisy* projector density to allocate the *deterministic* scalar. We adopt it only as a gauge frozen before cell evaluation. It is not a canonical physical local parity density, a localization of a deterministic parity projector, or a theorem transporting deterministic and noisy projectors.

# Exact corrected ledger and the first-alias sign

For fixed $n\ge2$ define the signed cell $$\label{eq:C-def}
 \boxed{
 \mathcal C_{\sigma,n}(J)=r_H^{-n}\!\left[
 L_{\sigma,n}(J)-P_n^{\rm abs}(J)
 +\{(-1)^n-\lambda_-(\sigma)^n\}\pi_\sigma(J)
 \right].}$$

[\[thm:partition-ledger\]]{#thm:partition-ledger label="thm:partition-ledger"} For every frozen finite measurable partition $\mathcal P$ of $X$ and every $n\ge2$, $$\label{eq:partition-ledger}
 \boxed{
 \sum_{J\in\mathcal P}\mathcal C_{\sigma,n}(J)
 =c^H_{\sigma,n}-c^H_n.}$$

Trace linearity gives $\sum_JL_{\sigma,n}(J)=\operatorname{Tr}K_\sigma^n$. The corrected deterministic localization gives $\sum_JP_n^{\rm abs}(J)=P_n$, while [\[thm:projector-measure\]](#thm:projector-measure){reference-type="ref" reference="thm:projector-measure"} gives $\sum_J\pi_\sigma(J)=1$. Substitution in [\[eq:C-def\]](#eq:C-def){reference-type="eqref" reference="eq:C-def"} yields $$r_H^{-n}\{\operatorname{Tr}K_\sigma^n-P_n+(-1)^n-\lambda_-(\sigma)^n\},$$ which is exactly the difference of [\[eq:c-noisy\]](#eq:c-noisy){reference-type="eqref" reference="eq:c-noisy"} and [\[eq:c-deterministic\]](#eq:c-deterministic){reference-type="eqref" reference="eq:c-deterministic"}.

Let $s_{k,n}$ be the finite counterloop moment, $p_n^{\rm pole}$ the limiting pole moment, and $$\label{eq:alias-anchor}
 \mathcal A_{k,n}=s_{k,n}-p_n^{\rm pole},
 \qquad
 a_n^{\rm num}=c^H_n-p_n^{\rm pole}.$$ The first-alias constituent has the data type fixed in RH-334, $$\label{eq:q-type}
 q_{{\rm FT},\sigma,k,n}
 =c^H_{\sigma,n}-s_{k,n}-a_n^{\rm num},
 \qquad
 \mathtt{coefficient\_type}
 =\mathtt{hardy\_full\_trace\_constituent}.$$

[\[cor:first-alias\]]{#cor:first-alias label="cor:first-alias"} For $k\ge2$ and $n=2k$, $$\label{eq:q-ledger}
 \boxed{
 q_{{\rm FT},\sigma,k,2k}
 =\sum_{J\in\mathcal P}\mathcal C_{\sigma,2k}(J)-\mathcal A_{k,2k}.}$$

The definitions give $$q_{\rm FT}
 =(c^H_{\sigma,n}-c^H_n)-(s_{k,n}-p_n^{\rm pole}).$$ Apply [\[thm:partition-ledger\]](#thm:partition-ledger){reference-type="ref" reference="thm:partition-ledger"}. In particular, replacing [\[eq:q-ledger\]](#eq:q-ledger){reference-type="eqref" reference="eq:q-ledger"} by the bare cell sum omits the nonzero first-alias packet and has the wrong algebraic sign ledger.

# Global Perron cancellation is not local commutation

The absence of a Perron cell in [\[eq:C-def\]](#eq:C-def){reference-type="eqref" reference="eq:C-def"} comes from cancellation of the two global scalars $-1$ in [\[eq:c-noisy\]](#eq:c-noisy){reference-type="eqref" reference="eq:c-noisy"} and [\[eq:c-deterministic\]](#eq:c-deterministic){reference-type="eqref" reference="eq:c-deterministic"}. It does not say that a window preserves the peripheral deflated subspace. Put $$\label{eq:deflation}
 D_{\sigma,n}=E_{0,\sigma}+\lambda_-(\sigma)^nE_{-,\sigma}.$$ Even when both products are trace class, $\operatorname{Tr}[M_J,D_{\sigma,n}]=0$ follows from trace cyclicity and contains no information about whether the commutator itself vanishes [@Simon2005].

[\[prop:commutator-fixture\]]{#prop:commutator-fixture label="prop:commutator-fixture"} Consider the positive rational row-stochastic matrix $$\label{eq:K-fixture}
 K=\begin{pmatrix}
 3/17&7/51&35/51\\
 4/85&83/255&32/51\\
 58/85&1/51&76/255
 \end{pmatrix}.$$ Its spectrum is $\{1,-2/5,1/5\}$, and the Riesz projector at $-2/5$ is $$\label{eq:Eminus-fixture}
 E_-=\begin{pmatrix}
 10/17&-5/51&-25/51\\
 8/17&-4/51&-20/51\\
 -10/17&5/51&25/51
 \end{pmatrix}.$$ It satisfies $E_-^2=E_-$, $KE_-=E_-K=(-2/5)E_-$, and $\operatorname{Tr}E_-=1$. The Perron projector is $$\label{eq:Ezero-fixture}
 E_0=\begin{pmatrix}
 7/17&5/51&25/51\\
 7/17&5/51&25/51\\
 7/17&5/51&25/51
 \end{pmatrix}.$$ For $M_2=\operatorname{diag}(0,1,0)$ and $n=2$, $$\label{eq:strict-commutator}
 [M_2,E_0+(4/25)E_-]
 =\begin{pmatrix}
 0&-7/85&0\\
 207/425&0&109/255\\
 0&-29/255&0
 \end{pmatrix}\ne0,$$ although its trace is zero.

Exact multiplication gives $E_-^2=E_-$ and the two spectral intertwining identities. The polynomial projector $$E_0=\frac{25}{28}(K+\tfrac25I)(K-\tfrac15I)$$ has the displayed value. Setting $E_+=I-E_0-E_-$ gives three pairwise annihilating nonzero projectors with $KE_0=E_0$, $KE_-=(-2/5)E_-$, and $KE_+=(1/5)E_+$; hence the stated spectrum follows. Direct subtraction of the two products with $M_2$ gives [\[eq:strict-commutator\]](#eq:strict-commutator){reference-type="eqref" reference="eq:strict-commutator"}.

This fixture is algebraic and nonphysical. Its role is to reject the invalid inference "global scalar deflation implies windowwise invariant deflation."

# Exact singleton-cell ledger

Use the fixture above with $r_H=17/20$, $n=2$, and set the three deterministic localized values to zero. The diagonal of $K^2$ and the projector masses are $$\begin{aligned}
 (L_1,L_2,L_3)&=(43/85,53/425,242/425),\label{eq:L-fixture}\\
 (\pi_1,\pi_2,\pi_3)&=(10/17,-4/51,25/51).
 \label{eq:pi-fixture}\end{aligned}$$ The negative middle entry proves that $\pi$ is not a probability vector. Since $1-(-2/5)^2=21/25$, [\[eq:C-def\]](#eq:C-def){reference-type="eqref" reference="eq:C-def"} gives $$\label{eq:C-fixture}
 (\mathcal C_1,\mathcal C_2,\mathcal C_3)
 =\left(\frac{400}{289},\frac{400}{4913},
 \frac{6672}{4913}\right).$$ Their sum and the independently evaluated global expression agree: $$\label{eq:C-total-fixture}
 \sum_{i=1}^3\mathcal C_i
 =\frac{48}{17}
 =\left(\frac{20}{17}\right)^2
 \left\{\operatorname{Tr}K^2+1-\left(-\frac25\right)^2\right\}.$$ The archived counterloop definition requires $k\ge2$. Therefore the $n=2$ computation is only a fixed-order ledger reproduction; it is not an attempt to set $k=1$ in [\[eq:q-ledger\]](#eq:q-ledger){reference-type="eqref" reference="eq:q-ledger"}.

# Cellwise extension nonuniqueness

The measure $\pi_\sigma$ makes [\[eq:C-def\]](#eq:C-def){reference-type="eqref" reference="eq:C-def"} exact, but the global scalar does not select it uniquely.

[\[thm:extension-nonuniqueness\]]{#thm:extension-nonuniqueness label="thm:extension-nonuniqueness"} Let $g\in\mathbb R$ and let $\mu$ be any finite signed measure on $X$ with $\mu(X)=g$. For every finite signed measure $\zeta$ with $\zeta(X)=0$, the measure $\mu'=\mu+\zeta$ has the same global mass. Consequently, for every finite measurable partition $\mathcal P$, $$\label{eq:partition-aggregate}
 \sum_{J\in\mathcal P}\mu'(J)
 =\sum_{J\in\mathcal P}\mu(J)=g.$$ If $\zeta$ is nonzero on at least one cell, the corresponding cellwise allocations are distinct.

If $X$ contains disjoint measurable sets $A,B$ of positive finite measure, there are infinitely many such absolutely continuous perturbations.

The first statement is finite additivity and $\mu'(X)=\mu(X)+\zeta(X)=g$. For the last statement, for any $t\ne0$ put $$d\zeta_t=t\left(
 \frac{\mathbf 1_A}{m(A)}-\frac{\mathbf 1_B}{m(B)}
 \right)dm.$$ Then $\zeta_t(X)=0$, while its values on $A$ and $B$ are $t$ and $-t$. Distinct values of $t$ give distinct extensions.

For the rational fixture, the parity scalar is $g=21/25$ and the projector-gauge allocation is $$\label{eq:base-allocation}
 g(\pi_1,\pi_2,\pi_3)
 =(42/85,-28/425,7/17).$$ Adding $(1/51,-1/51,0)$ changes two cells and leaves the total $21/25$ unchanged. This finite row is a witness to nonuniqueness, not evidence that any particular continuum interval has nonzero projector mass. In particular, we make no claim about the corrected mass of the specific fixed-point-free interval used in the RH-334 window-shift reproduction.

# Why the adapted-norm route remains inactive

RH-325 proves a sufficient trace-observation Duhamel majorant [@WangMovingDuhamel2026]. With local operator errors $\delta_j$ and stability weights $W_j$, the required target estimate follows from $$\label{eq:duhamel-majorant}
 \sum_jW_j\delta_j=o(k_\sigma R^{-2k_\sigma}).$$ If there are $O(k_\sigma)$ terms, uniformly $\delta_j=O(\sigma)$, and $$\label{eq:gamma-upper}
 \max_jW_j=O(\sigma^{-\gamma}),$$ then the archived sufficient exponent window is $$\label{eq:gamma-star}
 \gamma<\gamma_*
 =1-\frac{\log(1.4)}{\log\lambda}
 =0.3503698834605293\ldots .$$

The repository does not supply the hypotheses needed to apply this result to the physical cyclic observation:

1.  no uniform physical $\delta_j=O(\sigma)$ theorem covers all legs;

2.  no physical upper bounds are available for the trace observation and the required prefix/suffix operator products; and

3.  no bound [\[eq:gamma-upper\]](#eq:gamma-upper){reference-type="eqref" reference="eq:gamma-upper"} is proved with $\gamma<\gamma_*$.

RH-18 proves instead only $$\label{eq:rh18-lower}
 \operatorname{cond}(D^{\rm G}_{k_\sigma})
 \ge \sigma^{-1/4+o(1)},$$ a lower conditioning bound for an auxiliary Gaussian-packet balance [@WangGaussianReturn2026]. A lower bound cannot replace the upper bound required in [\[eq:gamma-upper\]](#eq:gamma-upper){reference-type="eqref" reference="eq:gamma-upper"}, and RH-18 does not identify that balance with the physical RH-325 observation weight. The positive adapted-norm route is therefore `STOP_SCOPED/NOT_TESTABLE`. Failure of a sufficient majorant is not a divergence theorem.

# Reproduction protocol and claim boundary

The executable artifact uses exact rational arithmetic. It checks the spectral-projector decomposition, independent eigenvector rescaling, idempotence, both intertwining identities, the signed singleton masses, the strict commutator, the three corrected cells, their total, and a nonzero zero-total extension. These finite calculations reproduce algebra only; they are not continuum certificates or moving-order evidence.

RH-335 proves an exact fixed-order projector-gauge ledger and a rigorous cellwise extension nonuniqueness theorem. It does not prove a physical local parity density, deterministic/noisy projector transport, a moving-order ledger, an $o(H_k)$ estimate, signed Duhamel cancellation, a physical upper stability exponent, off-alias or head closure, or determinant gluing. No result constructs a Hilbert--Polya operator, identifies Riemann zeros, proves a von Mangoldt trace formula or completed-zeta divisor equality, or proves the Riemann hypothesis. Gates A--E remain false/open.
