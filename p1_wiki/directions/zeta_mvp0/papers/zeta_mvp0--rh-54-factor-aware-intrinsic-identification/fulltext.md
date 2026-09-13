---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-54-factor-aware-intrinsic-identification"
canonical_tex: "zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/main.pdf"
source_sha256: "9d87b64a7d257f06f294c8f0372841c43f9b218fcf87a17429ed9b86403ae8df"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Factor-Aware Sparse-to-Full Transfer for Intrinsic Riesz Identification Growing-Horizon Hardy Robustness, a Conditional Closure Theorem, and a Nonnormal No-Go

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The small-noise intrinsic-identification program for a folded-Gaussian quadratic transfer operator has reduced the continuum defect to two directional Hardy energies. Previous work supplied deterministic finite-matrix tail certificates and an adaptive sparse approximation, but did not propagate the cutoff through the matrix's own Riesz factors and normalized Haar coupling ranges. We close that finite-dimensional interface.

  First, a Hilbert--Schmidt coupling perturbation $\left\lVert B-\widetilde B\right\rVert_{\mathfrak S_2}\le\varepsilon_B<\left\lVert B\right\rVert_{\mathfrak S_2}$ gives $$\left\|
   \frac B{\left\lVert B\right\rVert_{\mathfrak S_2}}-
   \frac{\widetilde B}{\left\lVert \widetilde B\right\rVert_{\mathfrak S_2}}
   \right\|_{\mathfrak S_2}
   \le\frac{2\varepsilon_B}{\left\lVert B\right\rVert_{\mathfrak S_2}}.$$ Since adjacent folded-Gaussian couplings have size $\Theta(h\sigma^{-3/2})$, an adaptive cutoff error of order $$\frac{h^2}{(\log(1/h))^{1/4}}$$ is automatically negligible after normalization. Second, we give explicit left/right defect formulas for the intrinsic triples in terms of the Markov, unweighted-projector, weighted-Riesz, and coupling defects. Third, actual finite-time ledgers $a_j=\left\lVert A^j\right\rVert$ and $\widetilde a_j=\left\lVert \widetilde A^j\right\rVert$ yield $$d_M=\delta_A\sum_{j=0}^{M-1}a_{M-1-j}\widetilde a_j,
   \qquad q_M+d_M<1,$$ which transports a growing-horizon block contraction and a complete Hardy upper without replacing nonnormal transients by powers of $\left\lVert A\right\rVert$.

  The resulting synthesis is exact but conditional: if the dyadic left and right Hardy budgets are $O(\sigma^{-\alpha_B})$ and $O(\sigma^{-\alpha_C})$, with range-restricted residues bounded, then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
   =O\!\left(n^{-2}\sigma^{-13/4-\alpha_B-\alpha_C}\right).$$ Every strict $n\sigma^2\to\infty$ schedule survives when $\alpha_B+\alpha_C\le1/4$; polylogarithmic budgets give the expected $n^{-2}\sigma^{-13/4}\operatorname{polylog}(1/\sigma)$ law. We also prove that small matrix error alone cannot control nonnormal Riesz factors, so a contour-conditioning or strong--weak stability ledger is indispensable. A five-scale dense audit through dimension $512$ and a 256-bit Arb arithmetic audit confirm the transfer mechanism, but do not prove the remaining dyadically uniform Hardy or Riesz-conditioning premises.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Factor-Aware Sparse-to-Full Transfer for Intrinsic Riesz Identification\
  Growing-Horizon Hardy Robustness, a Conditional Closure Theorem, and a Nonnormal No-Go
```

## Markdown 正文

**Keywords:** Riesz projection; nonnormal perturbation; Hilbert--Schmidt Hardy energy; growing horizon; Gaussian cutoff; intrinsic Galerkin identification.

**MSC 2020:** 47A10; 47B10; 65F35; 65G20; 93B36.

# Introduction

For each positive noise width $\sigma$, the folded-Gaussian quadratic operator has two simple peripheral branches: the Perron root and a negative parity resonance approaching $-1$. Subtracting their intrinsic weighted Riesz terms produces the bulk relevant to the two-step trace and determinant program. The continuum terms themselves are spatially resolved under the strict mesh condition $n\sigma^2\to\infty$, but a finite Galerkin matrix recomputes its own spectral terms. The remaining defect is therefore $$\mathcal I_{n,\sigma}
 =\mathcal Q_{\rm per}(E_n\mathcal K_\sigma E_n)
  -E_n\mathcal Q_{\rm per}(\mathcal K_\sigma)E_n.$$

RH-48 expressed this defect as an exact dyadic sum and proved that a mixed directional gain $O(\sigma^{-\gamma})$ gives $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-2}\sigma^{-3-\gamma}).
 \label{eq:rh48}$$ The strict bulk-square mesh range survives for $\gamma\le1/2$ [@WangIntrinsic2026]. RH-49 replaced the mixed gain by a purely Hilbert--Schmidt gain $\mathcal F_{n,\sigma}$ at a sharp quarter-power stable-rank cost. Thus $\mathcal F=O(\sigma^{-\delta})$ gives $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-2}\sigma^{-13/4-\delta}),
 \qquad \delta\le\frac14
 \label{eq:rh49}$$ as the full-range threshold [@WangDirectional2026].

RH-50 converted the two normalized reduced-resolvent actions into left and right Hardy energies after exact Perron/parity removal [@WangHardy2026]. RH-52 proved that the explicit range-restricted residues are $O(1)$ from weak intrinsic factors and established $$\left\lVert B\right\rVert_{\mathfrak S_2},\left\lVert C\right\rVert_{\mathfrak S_2}
 =\Theta(h\sigma^{-3/2})
 \label{eq:coupling-scale}$$ along the cell-average schedules [@WangFactorTransfer2026]. RH-51 and RH-53 then replaced fixed-step contraction and a fitted time tail by growing-horizon, deterministic all-column certificates [@WangStructuredStein2026; @WangHardyTail2026]. The last uncomposed finite-matrix interface was that a sparse/full Gaussian perturbation changes the Riesz terms and the normalized coupling sources themselves.

This paper gives that composition. Its role is deliberately narrower than an unconditional Stage-A4 theorem. The exact algebra determines which Riesz-conditioning and Hardy-budget premises suffice, how their exponents combine, and how a finite certificate transfers. It does not derive the remaining uniform premises from five computed noise levels.

## Main results {#main-results .unnumbered}

1.  Normalizing a nonzero Hilbert--Schmidt coupling costs at most twice its relative perturbation. In combination with [\[eq:coupling-scale\]](#eq:coupling-scale){reference-type="eqref" reference="eq:coupling-scale"}, the adaptive Gaussian cutoff is harmless on the normalized coupling ranges.

2.  Common isolating contours give separate perturbation ledgers for the unweighted projectors and weighted Riesz terms. These feed directly into the two intrinsic Hardy triples.

3.  The exact power telescoping identity, evaluated with actual finite-time norm ledgers, transfers a contracting block and gives a complete perturbed Hardy-energy upper.

4.  The RH-48--RH-53 chain composes with the exact exponent $\delta=\alpha_B+\alpha_C$. The quarter-power threshold is therefore a budget shared by the two Hardy directions, not a quarter power available independently to each.

5.  A two-dimensional nonnormal family has matrix perturbation tending to zero while its peripheral Riesz projector changes by order one. Thus cutoff convergence alone cannot close the intrinsic-factor interface.

# Intrinsic directional triples

Let $T$ be a fine matrix and let $U$ and $W$ be the coarse and Haar-detail isometries. Relative to the adjacent split, $$T=\begin{pmatrix}T_c&B\\ C&D\end{pmatrix},
 \qquad B=U^*TW,
 \qquad C=W^*TU.$$ For the two peripheral branches, write $$\begin{aligned}
 P_f&=P_{f,+}+P_{f,-},&
 W_f&=\lambda_{f,+}P_{f,+}+\lambda_{f,-}P_{f,-},\\
 P_c&=P_{c,+}+P_{c,-},&
 W_c&=\lambda_{c,+}P_{c,+}+\lambda_{c,-}P_{c,-}.\end{aligned}$$ Here $P$ denotes an unweighted Riesz projection and $W$ its weighted term. Put $$Q_f=\mathrm I-P_f,\quad N_f=T-W_f,
 \qquad Q_c=\mathrm I-P_c,\quad N_c=T_c-W_c.$$ For a fixed Hardy radius $r$ above the two bulk spectral radii, the RH-53 triples are $$\begin{aligned}
 A_B&=r^{-1}N_f,
 &X_B&=Q_fU\widehat B,
 &Y_B&=U^*,
 \label{eq:left-triple}\\
 A_C&=r^{-1}N_c^*,
 &X_C&=\widehat C^*,
 &Y_C&=Q_c^*,
 \label{eq:right-triple}\end{aligned}$$ where $$\widehat B=B/\left\lVert B\right\rVert_{\mathfrak S_2},
 \qquad
 \widehat C=C/\left\lVert C\right\rVert_{\mathfrak S_2}.$$ Their directional energies are $$\mathcal E(A,X,Y)^2
 =\sum_{m\ge0}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2.
 \label{eq:energy}$$

We compare these quantities with a second matrix, marked by tildes. All norms below are Euclidean operator norms except where $\mathfrak S_2$ is shown.

# Normalization and intrinsic factor transfer

[\[lem:normalization\]]{#lem:normalization label="lem:normalization"} Let $B,\widetilde B\ne0$ and suppose $$\left\lVert B-\widetilde B\right\rVert_{\mathfrak S_2}
 \le\varepsilon_B<\left\lVert B\right\rVert_{\mathfrak S_2}.$$ Then $$\boxed{
 \left\lVert \widehat B-\widehat{\widetilde B}\right\rVert_{\mathfrak S_2}
 \le\frac{2\varepsilon_B}{\left\lVert B\right\rVert_{\mathfrak S_2}}.}
 \label{eq:normalization}$$ The same statement holds for $C$.

Insert $\widetilde B/\left\lVert B\right\rVert_{\mathfrak S_2}$ and use $$\left|\left\lVert \widetilde B\right\rVert_{\mathfrak S_2}-\left\lVert B\right\rVert_{\mathfrak S_2}\right|
 \le\left\lVert \widetilde B-B\right\rVert_{\mathfrak S_2}.$$ The two resulting terms are each at most $\varepsilon_B/\left\lVert B\right\rVert_{\mathfrak S_2}$. The strict premise also guarantees $\widetilde B\ne0$.

[\[cor:adaptive-normalization\]]{#cor:adaptive-normalization label="cor:adaptive-normalization"} Suppose [\[eq:coupling-scale\]](#eq:coupling-scale){reference-type="eqref" reference="eq:coupling-scale"} holds and the adaptive full-versus-sparse matrix defect is $$\varepsilon_h
 =O\!\left(\frac{h^2}{(\log(1/h))^{1/4}}\right).$$ The induced Haar coupling defects are at most $\varepsilon_h$, and hence $$\left\lVert \widehat B-\widehat{\widetilde B}\right\rVert_{\mathfrak S_2}
 +\left\lVert \widehat C-\widehat{\widetilde C}\right\rVert_{\mathfrak S_2}
 =O\!\left(
 \frac{h\sigma^{3/2}}{(\log(1/h))^{1/4}}
 \right).
 \label{eq:adaptive-normalization}$$

Orthogonal block extraction is contractive in Hilbert--Schmidt norm. Apply [\[lem:normalization\]](#lem:normalization){reference-type="ref" reference="lem:normalization"} and divide the adaptive cutoff rate of RH-39 by [\[eq:coupling-scale\]](#eq:coupling-scale){reference-type="eqref" reference="eq:coupling-scale"} [@WangCutoff2026].

The remaining factors require spectral conditioning. Let $\Gamma_+$ and $\Gamma_-$ be common positively oriented isolating contours for $T$ and $\widetilde T$. Set $$M_s=\sup_{z\in\Gamma_s}\left\lVert (z-T)^{-1}\right\rVert,
 \qquad
 \widetilde M_s
 =\sup_{z\in\Gamma_s}\left\lVert (z-\widetilde T)^{-1}\right\rVert.$$

[\[prop:riesz-ledger\]]{#prop:riesz-ledger label="prop:riesz-ledger"} If $\delta_T=\left\lVert T-\widetilde T\right\rVert$, then the rank-two unweighted and weighted defects satisfy $$\begin{aligned}
 \varepsilon_P
 :=\left\lVert P-\widetilde P\right\rVert
 &\le
 \frac{\delta_T}{2\pi}
 \sum_{s\in\{+,-\}}
 |\Gamma_s|M_s\widetilde M_s,
 \label{eq:projector-ledger}\\
 \varepsilon_W
 :=\left\lVert W-\widetilde W\right\rVert
 &\le
 \frac{\delta_T}{2\pi}
 \sum_{s\in\{+,-\}}
 |\Gamma_s|\max_{z\in\Gamma_s}|z|M_s\widetilde M_s.
 \label{eq:weighted-ledger}\end{aligned}$$

Use the Riesz formulas $$P_s=\frac1{2\pi i}\int_{\Gamma_s}(z-T)^{-1}\,dz,
 \qquad
 W_s=\frac1{2\pi i}\int_{\Gamma_s}z(z-T)^{-1}\,dz,$$ and the exact resolvent identity $$(z-T)^{-1}-(z-\widetilde T)^{-1}
 =(z-T)^{-1}(T-\widetilde T)(z-\widetilde T)^{-1}.$$ Sum the two contour estimates. This is the standard nonnormal conditioning dependence, retained rather than suppressed [@Kato1995; @HornJohnson2013].

[\[thm:factor-transfer\]]{#thm:factor-transfer label="thm:factor-transfer"} For the left triple [\[eq:left-triple\]](#eq:left-triple){reference-type="eqref" reference="eq:left-triple"}, suppose $$\begin{aligned}
 \left\lVert T-\widetilde T\right\rVert&\le\delta_{T,f},&
 \left\lVert W_f-\widetilde W_f\right\rVert&\le\varepsilon_{W,f},\\
 \left\lVert P_f-\widetilde P_f\right\rVert&\le\varepsilon_{P,f},&
 \left\lVert B-\widetilde B\right\rVert_{\mathfrak S_2}&\le\delta_B<\left\lVert B\right\rVert_{\mathfrak S_2}.\end{aligned}$$ Then $$\begin{aligned}
 \delta_{A,B}
 &:=\left\lVert A_B-\widetilde A_B\right\rVert
 \le r^{-1}(\delta_{T,f}+\varepsilon_{W,f}),
 \label{eq:left-A}\\
 \delta_{X,B}
 &:=\left\lVert X_B-\widetilde X_B\right\rVert_{\mathfrak S_2}
 \le\varepsilon_{P,f}
 +\left\lVert \widetilde Q_f\right\rVert
 \frac{2\delta_B}{\left\lVert B\right\rVert_{\mathfrak S_2}},
 \label{eq:left-X}\\
 \delta_{Y,B}&=0.
 \label{eq:left-Y}\end{aligned}$$ For the right triple [\[eq:right-triple\]](#eq:right-triple){reference-type="eqref" reference="eq:right-triple"}, $$\begin{aligned}
 \delta_{A,C}
 &\le r^{-1}(\delta_{T,c}+\varepsilon_{W,c}),
 \label{eq:right-A}\\
 \delta_{X,C}
 &\le\frac{2\delta_C}{\left\lVert C\right\rVert_{\mathfrak S_2}},
 \label{eq:right-X}\\
 \delta_{Y,C}&\le\varepsilon_{P,c}.
 \label{eq:right-Y}\end{aligned}$$

For the bulk, $$N_f-\widetilde N_f
 =(T-\widetilde T)-(W_f-\widetilde W_f),$$ which gives [\[eq:left-A\]](#eq:left-A){reference-type="eqref" reference="eq:left-A"}; adjunction gives [\[eq:right-A\]](#eq:right-A){reference-type="eqref" reference="eq:right-A"}. For the left source, insert $\widetilde Q_fU\widehat B$: $$\left\lVert Q_fU\widehat B-
 \widetilde Q_fU\widehat{\widetilde B}\right\rVert_{\mathfrak S_2}
 \le\left\lVert Q_f-\widetilde Q_f\right\rVert
 +\left\lVert \widetilde Q_f\right\rVert
  \left\lVert \widehat B-\widehat{\widetilde B}\right\rVert_{\mathfrak S_2}.$$ Use [\[lem:normalization\]](#lem:normalization){reference-type="ref" reference="lem:normalization"}. The left observation $U^*$ is fixed. The right source is only the normalized coupling, while its observation is the adjoint complement; this proves [\[eq:right-X\]](#eq:right-X){reference-type="eqref" reference="eq:right-X"}--[\[eq:right-Y\]](#eq:right-Y){reference-type="eqref" reference="eq:right-Y"}.

[\[rem:strong-weak\]]{#rem:strong-weak label="rem:strong-weak"} Equations [\[eq:projector-ledger\]](#eq:projector-ledger){reference-type="eqref" reference="eq:projector-ledger"}--[\[eq:weighted-ledger\]](#eq:weighted-ledger){reference-type="eqref" reference="eq:weighted-ledger"} are one fully explicit route, but they may be too expensive in $L^2$ because the peripheral residues themselves grow logarithmically [@WangLogConditioning2026]. A Keller--Liverani strong--weak modulus may replace them if it yields the same two numerical outputs $\varepsilon_P$ and $\varepsilon_W$ [@KellerLiverani1999]. The subsequent theorem uses only those outputs; it does not assume how they were obtained.

# Growing-horizon robustness

Let $(A,X,Y)$ and $(\widetilde A,\widetilde X,\widetilde Y)$ be either pair of triples. Put $$a_j=\left\lVert A^j\right\rVert,
 \qquad
 \widetilde a_j=\left\lVert \widetilde A^j\right\rVert,
 \qquad
 \delta_A=\left\lVert A-\widetilde A\right\rVert.$$

[\[thm:finite-transfer\]]{#thm:finite-transfer label="thm:finite-transfer"} For $m\ge1$, define $$d_m=\delta_A\sum_{j=0}^{m-1}
 a_{m-1-j}\widetilde a_j,
 \qquad d_0=0.
 \label{eq:dm}$$ Then $$\left\lVert A^m-\widetilde A^m\right\rVert\le d_m.
 \label{eq:power-transfer}$$ Moreover, for $\delta_X=\left\lVert X-\widetilde X\right\rVert_{\mathfrak S_2}$ and $\delta_Y=\left\lVert Y-\widetilde Y\right\rVert$, $$\begin{aligned}
 &\left\lVert YA^mX-\widetilde Y\widetilde A^m\widetilde X\right\rVert_{\mathfrak S_2}
 \le b_m,
 \label{eq:bm}\\
 b_m:={}&
 \delta_Ya_m\left\lVert X\right\rVert_{\mathfrak S_2}
 +\left\lVert \widetilde Y\right\rVert d_m\left\lVert X\right\rVert_{\mathfrak S_2}
 +\left\lVert \widetilde Y\right\rVert\widetilde a_m\delta_X.
 \notag\end{aligned}$$ If $E_M$ and $\widetilde E_M$ are the finite energies through time $M-1$, then $$|E_M-\widetilde E_M|
 \le D_M:=\left(\sum_{m=0}^{M-1}b_m^2\right)^{1/2}.
 \label{eq:finite-energy}$$ Finally, if $q_M=\left\lVert A^M\right\rVert$ and $$\boxed{q_M+d_M<1,}
 \label{eq:contraction-transfer}$$ then $\left\lVert \widetilde A^M\right\rVert<1$ and the perturbed full energy obeys $$\boxed{
 \mathcal E(\widetilde A,\widetilde X,\widetilde Y)^2
 \le(E_M+D_M)^2
 +\left\lVert \widetilde Y\right\rVert^2
 \frac{(q_M+d_M)^2}{1-(q_M+d_M)^2}
 \left\lVert \widetilde X\right\rVert_{\mathfrak S_2}^2
 \sum_{j=0}^{M-1}\widetilde a_j^2.}
 \label{eq:complete-transfer}$$

The exact identity $$A^m-\widetilde A^m
 =\sum_{j=0}^{m-1}
 A^{m-1-j}(A-\widetilde A)\widetilde A^j$$ gives [\[eq:power-transfer\]](#eq:power-transfer){reference-type="eqref" reference="eq:power-transfer"}. Insert and subtract $\widetilde YA^mX$ and $\widetilde Y\widetilde A^mX$ to obtain [\[eq:bm\]](#eq:bm){reference-type="eqref" reference="eq:bm"}; Minkowski in the finite time $\ell^2$ space proves [\[eq:finite-energy\]](#eq:finite-energy){reference-type="eqref" reference="eq:finite-energy"}. The power bound at $m=M$ gives [\[eq:contraction-transfer\]](#eq:contraction-transfer){reference-type="eqref" reference="eq:contraction-transfer"}. The block-geometric tail from RH-53 gives $$\sum_{m\ge M}
 \left\lVert \widetilde Y\widetilde A^m\widetilde X\right\rVert_{\mathfrak S_2}^2
 \le
 \left\lVert \widetilde Y\right\rVert^2
 \frac{\left\lVert \widetilde A^M\right\rVert^2}
 {1-\left\lVert \widetilde A^M\right\rVert^2}
 \sum_{j=0}^{M-1}\left\lVert \widetilde A^j\widetilde X\right\rVert_{\mathfrak S_2}^2.$$ Use $\left\lVert \widetilde A^M\right\rVert\le q_M+d_M$ and $\left\lVert \widetilde A^j\widetilde X\right\rVert_{\mathfrak S_2}le
\widetilde a_j\left\lVert \widetilde X\right\rVert_{\mathfrak S_2}$.

Replacing $a_j$ and $\widetilde a_j$ by $\left\lVert A\right\rVert^j$ and $\left\lVert \widetilde A\right\rVert^j$ can make [\[eq:contraction-transfer\]](#eq:contraction-transfer){reference-type="eqref" reference="eq:contraction-transfer"} useless for a nonnormal bulk even when an actual block power is strongly contracting. The theorem stores the measured or enclosed transient through the selected growing horizon. It does not infer transient behavior from spectral radius or one-step norm.

# A nonnormal no-free-lunch theorem

It remains to ask whether the adaptive matrix cutoff bound alone can make the Riesz defects in [\[thm:factor-transfer\]](#thm:factor-transfer){reference-type="ref" reference="thm:factor-transfer"} vanish. The answer is no without a conditioning premise.

[\[prop:no-go\]]{#prop:no-go label="prop:no-go"} Fix $c>0$ and let $$T_K=\begin{pmatrix}0&K\\0&1\end{pmatrix},
 \qquad
 E_K=\begin{pmatrix}0&0\\c/K&0\end{pmatrix}.$$ Then $\left\lVert E_K\right\rVert=c/K\to0$. The eigenvalues of $\widetilde T_K=T_K+E_K$ are $$\lambda_\pm=\frac{1\pm\sqrt{1+4c}}2,$$ independent of $K$. Let $P_K$ be the Riesz projector of $T_K$ at $1$ and $\widetilde P_K$ the Riesz projector of $\widetilde T_K$ at $\lambda_+$. Then $$\liminf_{K\to\infty}\left\lVert P_K-\widetilde P_K\right\rVert
 \ge\frac{\sqrt{1+4c}-1}{2\sqrt{1+4c}}>0.
 \label{eq:no-go}$$ Consequently there is no dimension- and conditioning-free Lipschitz bound $\left\lVert P-\widetilde P\right\rVert\le C\left\lVert T-\widetilde T\right\rVert$ for nonnormal families.

The characteristic polynomial of $\widetilde T_K$ is $\lambda^2-\lambda-c$. Since the two eigenvalues are distinct, $$P_K=T_K,
 \qquad
 \widetilde P_K
 =\frac{\widetilde T_K-\lambda_-\mathrm I}
 {\lambda_+-\lambda_-}.$$ The $(1,1)$ entry of $P_K-\widetilde P_K$ has modulus $$\frac{-\lambda_-}{\lambda_+-\lambda_-}
 =\frac{\sqrt{1+4c}-1}{2\sqrt{1+4c}},$$ which lower-bounds the operator norm. Meanwhile $\left\lVert E_K\right\rVert=c/K$.

For $c=1/4$, the lower bound is about $0.1464$, while a numerical evaluation at $K=10^6$ gives a projector defect about $2.93\times10^5$ because the off-diagonal projector geometry is itself highly conditioned. The fixed entry lower bound is enough for the theorem; the stronger growth illustrates why recomputed finite factors cannot be certified from an unweighted cutoff norm alone.

The proposition does not say that the folded-Gaussian Riesz terms are unstable. It says that their stability must be proved from their own spectral geometry---for example, [\[prop:riesz-ledger\]](#prop:riesz-ledger){reference-type="ref" reference="prop:riesz-ledger"} or a strong--weak transfer theorem. The five-scale audit below observes excellent stability, but observation is not a substitute for this premise.

# Conditional closure of intrinsic identification

The factor-aware finite-matrix theorem can now be joined to the earlier range-resolvent reductions. Let the residue terms be the normalized fine/coarse actions entering RH-50. RH-52 proves they are uniformly bounded along the adopted cell-average schedules.

[\[cond:hardy-budget\]]{#cond:hardy-budget label="cond:hardy-budget"} There are fixed $r<\min_s\inf_{z\in\Gamma_s}|z|$, exponents $\alpha_B,\alpha_C\ge0$, and $C<\infty$ such that, at every required dyadic level, $$\begin{aligned}
 \operatorname{spr}(N_f),\operatorname{spr}(N_c)&<r,
 \label{eq:radius-condition}\\
 \mathcal E_B(r)&\le C\sigma^{-\alpha_B},
 &\mathcal E_C(r)&\le C\sigma^{-\alpha_C},
 \label{eq:energy-powers}\\
 \text{all normalized peripheral range residues}&\le C.
 \label{eq:residue-condition}\end{aligned}$$ The same condition may use fixed powers of $\log(1/\sigma)$ instead of power laws. Sparse certificates may be transferred to the full family by [\[thm:factor-transfer,thm:finite-transfer\]](#thm:factor-transfer,thm:finite-transfer){reference-type="ref" reference="thm:factor-transfer,thm:finite-transfer"}, provided their Riesz ledgers and contraction margins obey those theorems uniformly along the dyadic chain.

[\[thm:composition\]]{#thm:composition label="thm:composition"} Under [\[cond:hardy-budget\]](#cond:hardy-budget){reference-type="ref" reference="cond:hardy-budget"}, the purely Hilbert--Schmidt directional gain of RH-49 satisfies $$\sup_{j\ge0}\mathcal F_{2^jn,\sigma}
 =O(\sigma^{-\delta}),
 \qquad
 \delta=\alpha_B+\alpha_C.
 \label{eq:F-budget}$$ Consequently $$\boxed{
 \left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O\!\left(
 n^{-2}\sigma^{-13/4-\alpha_B-\alpha_C}
 \right).}
 \label{eq:identification-budget}$$ If $$\alpha_B+\alpha_C\le\frac14,
 \label{eq:quarter-budget}$$ then every strict schedule $n(\sigma)\sigma^2\to\infty$ retains the intrinsic bulk-square conclusion. If both energies are polylogarithmic, then for some fixed $a$, $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O\!\left(
 n^{-2}\sigma^{-13/4}(\log(1/\sigma))^a
 \right).
 \label{eq:polylog-composition}$$

The two-pole Laurent decomposition of RH-50 writes each normalized Hilbert--Schmidt range action as finitely many residue terms plus a bulk term. The residues are $O(1)$ by [\[eq:residue-condition\]](#eq:residue-condition){reference-type="eqref" reference="eq:residue-condition"}. The directional Hardy theorem gives $$\begin{aligned}
 \ell_B^{(2)}
 &\le C\{1+\mathcal E_B(r)\},\\
 \ell_C^{(2)}
 &\le C\{1+\mathcal E_C(r)\},\end{aligned}$$ where the fixed factor $(d_\Gamma^2-r^2)^{-1/2}$ is absorbed in $C$. The RH-49 gain is a finite branch sum of products, so $$\mathcal F_{n,\sigma}
 \le C(1+\mathcal E_B(r))(1+\mathcal E_C(r)).
 \label{eq:hardy-product}$$ This proves [\[eq:F-budget\]](#eq:F-budget){reference-type="eqref" reference="eq:F-budget"}. The quarter-power stable-rank bridge adds $1/4$ to the mixed-gain exponent, and [\[eq:rh48\]](#eq:rh48){reference-type="eqref" reference="eq:rh48"} then gives [\[eq:identification-budget\]](#eq:identification-budget){reference-type="eqref" reference="eq:identification-budget"}. The RH-49 threshold is precisely $\delta\le1/4$. Products of fixed logarithmic powers remain a fixed logarithmic power, proving [\[eq:polylog-composition\]](#eq:polylog-composition){reference-type="eqref" reference="eq:polylog-composition"}.

The theorem closes the logical composition and the factor-aware finite-matrix transfer. It does not prove [\[cond:hardy-budget\]](#cond:hardy-budget){reference-type="ref" reference="cond:hardy-budget"}. In particular, five finite noise levels do not give a dyadically uniform analytic Hardy trace budget, and an adaptive cutoff norm does not by itself give the Riesz modulus required by [\[thm:factor-transfer\]](#thm:factor-transfer){reference-type="ref" reference="thm:factor-transfer"}. Stage A4 is therefore a conditional closure criterion, not an unconditional small-noise identification theorem.

# Five-scale transfer audit

The numerical experiment deliberately uses the smaller resolution $$N\sigma=5.12,
 \qquad r=0.85,$$ so that full dense Gaussian matrices and all intrinsic factors can be recomputed. The noise levels are $0.16,0.08,0.04,0.02,0.01$, the dimensions are $32,64,128,256,512$, and the horizons are $4,8,16,24,32$. For every scale we build the full matrix and three row-renormalized sparse matrices with declared cutoffs $L=5,6,8$. The $L=5$ family is an intentionally enlarged stress test, not the production choice.

The audit records the Markov and Haar coupling defects, recomputed unweighted and weighted Riesz defects, bulk and normalized-source defects, actual semigroup-power differences, the telescoping uppers of [\[thm:finite-transfer\]](#thm:finite-transfer){reference-type="ref" reference="thm:finite-transfer"}, exact Lyapunov energies, deterministic all-column certificates, and the complete transferred upper [\[eq:complete-transfer\]](#eq:complete-transfer){reference-type="eqref" reference="eq:complete-transfer"}. Every quantity in this section is binary64.

The largest Markov spectral defect is $6.61\times10^{-8}$, the largest fine weighted-Riesz defect is $3.72\times10^{-8}$, and the largest normalized $B$ defect is $4.12\times10^{-7}$. Every composed factor upper dominates the directly recomputed triple defect. The largest transferred block perturbation consumes only $3.34\times10^{-7}$ of the available contraction margin; all actual block norms stay between $0.0067$ and $0.031$.

At $L=6$, the Markov defect is about $10^{-10}$ from dimension $64$ onward; at $L=8$, direct differences are at binary64 roundoff. On these pilot dimensions the sufficient adaptive prescription is still $L(h)=5$. Its distinction from a fixed window is asymptotic: RH-39 proves that the adaptive multiple eventually grows like $2\sqrt{\log(1/h)}$, whereas any fixed multiple has a positive row-norm continuum floor.

![Factor-aware sparse-to-full audit. (a) The declared five-sigma window creates a visible stress defect; six and eight sigma rapidly reach roundoff. (b) Recomputed intrinsic factors and the normalized outgoing coupling. (c) Actual Hardy-energy changes and conservative finite-time uppers. (d) Actual growing-block defects and the semigroup telescoping ledgers. All panels are binary64 diagnostics.](<../../../../../zeta_mvp0/papers/RH-54-factor-aware-intrinsic-identification/figures/factor_aware_intrinsic_identification.pdf>){#fig:audit width="\\textwidth"}

## Outward-rounded arithmetic audit

A separate 256-bit Arb execution encloses a $3\times2$ coupling, its perturbation, both normalizations, a factor-aware triple ledger, and six semigroup powers [@Johansson2017; @Rump2010]. It certifies $$\left\lVert \Delta\widehat B\right\rVert_{\mathfrak S_2}
 \le1.251468\times10^{-8},
 \qquad
 q_6+d_6\le0.025000445.$$ This validates outward arithmetic for the formulas. It is intentionally a small abstract execution and not an interval eigensolver or production-scale Riesz enclosure.

# Theorem boundary and next gate

The status after this composition is as follows.

Normalized coupling gate

:   Closed analytically. The adaptive cutoff becomes even smaller after division by the physical coupling scale.

Factor-aware finite transfer

:   Closed analytically once projector and weighted-Riesz defect uppers are supplied. A common-contour ledger is explicit.

Growing-horizon robustness

:   Closed analytically. The certificate uses actual finite semigroup ledgers and transports both contraction and the full Hardy upper.

RH-48--RH-53 synthesis

:   Closed as a conditional theorem with exact exponent budget $\alpha_B+\alpha_C\le1/4$.

Uniform Stage A1 budget

:   Open. No analytic theorem yet bounds both dyadic Hardy energies uniformly, polylogarithmically, or with a proved total power at most $1/4$.

Uniform intrinsic Riesz modulus

:   Open. The dense audit observes stability, but the no-go theorem shows that an operator cutoff bound alone cannot prove it.

Unconditional Stage A4

:   Open. The preceding two premises prevent an unconditional claim despite the complete finite-dimensional transfer architecture.

The sharp next target is no longer another fixed-window pilot. One needs a dyadically uniform analytic Hardy/Stein trace budget together with either a strong--weak intrinsic-factor modulus or an outward-rounded contour ledger on the production family. If these provide total Hardy exponent at most $1/4$, [\[thm:composition\]](#thm:composition){reference-type="ref" reference="thm:composition"} closes the identification theorem immediately. If every valid budget exceeds $1/4$, the full strict $n\sigma^2\to\infty$ range fails and a stronger mesh schedule must be stated instead.

No result here constructs an arithmetic trace formula, a prime-power identity, a self-adjoint Hilbert--Pólya operator, a $T\log T$ counting law, or a zeta-zero spectral identity, and no Riemann-hypothesis conclusion is drawn. The independent TPC twin-prime branch is not a premise of this theorem.

# Reproducibility

The archive contains theorem code in , the five-scale pilot, the Arb audit, tests, figure sources, a machine-readable closure certificate, dependency hashes, and the manuscript. From this directory, the main replay is

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q
    OPENBLAS_NUM_THREADS=16 OMP_NUM_THREADS=16 \
      PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_factor_aware_pilot.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_transfer_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_closure_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Conclusion

The sparse/full gap left by deterministic Hardy tails can be propagated through recomputed intrinsic factors without choosing eigenvector gauges. Normalized Haar couplings are stable at twice their relative Hilbert--Schmidt error, the weighted and unweighted Riesz terms enter through separate auditable defects, and one growing contracting block survives under the exact finite semigroup ledger. These ingredients compose RH-48 through RH-53 into a single closure theorem with the transparent threshold $\alpha_B+\alpha_C\le1/4$.

The result also marks the remaining wall precisely. Nonnormal Riesz stability is not free, and finite Hardy plateaus do not prove a uniform trace budget. Thus the route remains viable and substantially clearer, but its last analytic premises must still be proved or validated before the small-noise intrinsic identification can be called unconditional.
