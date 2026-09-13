---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction/main.pdf"
source_sha256: "51ba6283760c87a981d2d52566cb5f0f73037fdce8d8654990924bbed49656f1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projector-Mass First-Alias Threshold and an Isospectral Cell Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-336-projector-mass-first-alias-threshold-and-isospectral-cell-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The projector-density gauge of RH-335 turns the global noisy parity scalar into signed localized cells. We determine the exact first-alias scale of one such cell. On every bounded-phase natural clock, its parity contribution divided by $H_k=kR^{-2k}$ equals $2C_*\lambda^{\eta_\sigma}(\beta R)^{2k}\pi_\sigma(J)(1+o(1))$. Thus the critical projector-mass exponent is $\kappa_{\rm proj}=\log(\beta R)/\log\lambda$, distinct from the earlier Duhamel stability exponent. A fixed finite partition necessarily has a maximum normalized parity cell diverging to $+\infty$, but the maximizing cell may move with noise and is not identified with a physical boundary/sibling aggregate; raw and alias terms may still cancel it. We complement the scale theorem with an exact three-state family. A nontrivial interval of smooth similarities preserves strict positivity, row-stochasticity, the spectrum, and every power trace, while the parity projector masses and corrected singleton cells drift by explicit nonzero zero-sum vectors. This is a nonphysical finite algebraic obstruction to recovering cells from global spectral data. It does not prove physical signed Duhamel cancellation or a physical normalized obstruction, and it yields no determinant or Riemann-hypothesis conclusion.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Projector-Mass First-Alias Threshold\
  and an Isospectral Cell Obstruction
```

## Markdown 正文

# Inherited projector gauge and first-alias clock

Let $K_\sigma$ be the noisy folded operator and let $\lambda_-(\sigma)=-(1-\delta_\sigma)$ be its real simple parity eigenvalue, where the archived law is $$\label{eq:delta-law}
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma),
 \qquad C_*>0.$$ Write $E_{-,\sigma}$ for the rank-one Riesz projector itself. RH-335 proves that $$\label{eq:pi}
 \pi_\sigma(J)=\operatorname{Tr}(M_JE_{-,\sigma})$$ is a real finite signed measure with total mass one [@WangProjectorLedger2026]. Allocating the deterministic parity scalar with this noisy density is a frozen gauge, not canonical physical localization or deterministic/noisy projector transport.

Retain the constants and clock from RH-326 [@WangFirstAlias2026]: $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad R=\frac75,\qquad
 \beta=\frac1{r_H\sqrt\lambda},$$ and $$\label{eq:phase}
 \eta_\sigma
 =k-\frac{\log(1/\sigma)}{2\log\lambda}.$$ Throughout the moving statements, $k=k_\sigma\in\mathbb N$, $k\ge2$, $\eta_\sigma$ remains bounded, and $k\to\infty$ as $\sigma\to0$.

For a measurable cell $J$, possibly depending on $\sigma$, define $$\label{eq:G-H}
 \mathcal G_{\sigma,k}(J)
 =r_H^{-2k}\{1-\lambda_-(\sigma)^{2k}\}\pi_\sigma(J),
 \qquad H_k=kR^{-2k}.$$ This is only the localized parity-gauge constituent of the RH-335 corrected cell. It omits the localized raw defect and the globally subtracted alias packet.

# Moving projector-mass threshold

[\[thm:moving-scale\]]{#thm:moving-scale label="thm:moving-scale"} On every bounded-phase sequence, $$\label{eq:G-over-H}
 \boxed{
 \frac{\mathcal G_{\sigma,k}(J)}{H_k}
 =2C_*\lambda^{\eta_\sigma}(\beta R)^{2k}
 \pi_\sigma(J)\{1+o(1)\}.}$$ The scalar $o(1)$ is independent of the chosen cell.

Because $k\delta_\sigma\to0$, the uniform parity expansion of RH-326 gives $$\label{eq:parity-expansion}
 1-(1-\delta_\sigma)^{2k}
 =2kC_*\sqrt\sigma\{1+o(1)\}.$$ Even order removes the sign of $\lambda_-$, so substitution in [\[eq:G-H\]](#eq:G-H){reference-type="eqref" reference="eq:G-H"} and division by $H_k$ yield $$2C_*\sqrt\sigma\left(\frac{R}{r_H}\right)^{2k}
 \pi_\sigma(J)\{1+o(1)\}.$$ Equation [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"} gives $\sqrt\sigma\lambda^k=\lambda^{\eta_\sigma}$, while $(\beta R)^{2k}=(R/r_H)^{2k}\lambda^{-k}$. Their product is the required scalar in [\[eq:G-over-H\]](#eq:G-over-H){reference-type="eqref" reference="eq:G-over-H"}.

Define $$\label{eq:kappa}
 \boxed{
 \kappa_{\rm proj}
 =\frac{\log(\beta R)}{\log\lambda}
 =\frac{\log(28/17)}{\log\lambda}-\frac12.}$$ The rational bracket $3/2<u_c<25/16$ from the physical observation source implies $\lambda=2u_c(u_c-1)<225/128<(28/17)^2$ [@WangObservation2026]. Hence $\beta R>1$ and $\kappa_{\rm proj}>0$. Ordinary substitution of the archived decimal for $\lambda$ gives $$\label{eq:kappa-decimal}
 \kappa_{\rm proj}=0.463406944517002\ldots .$$ This decimal is diagnostic, not an interval certificate. It is not the RH-325 sufficient Duhamel weight ceiling $\gamma_*=0.3503698834605293\ldots$; in fact their separation is exact. The RH-334 algebraic identities imply $\lambda^3+4\lambda^2-16=0$ [@WangObservation2026]. This polynomial is strictly increasing on the positive half-line, and its value at $17/10$ is $473/1000>0$, so $\lambda<17/10$. Moreover, $$\left(\frac{196}{85}\right)^2-\left(\frac{17}{10}\right)^3
 =\frac{116783}{289000}>0.$$ Since $\lambda>1$ and $$\kappa_{\rm proj}-\gamma_*
 =\frac{\log\!\left((R^2/r_H)/\lambda^{3/2}\right)}{\log\lambda},
 \qquad \frac{R^2}{r_H}=\frac{196}{85},$$ it follows that $\kappa_{\rm proj}>\gamma_*$ exactly. The two exponents also govern different objects.

[\[cor:threshold\]]{#cor:threshold label="cor:threshold"} On every bounded-phase sequence, $$\label{eq:iff}
 \mathcal G_{\sigma,k}(J)=o(H_k)
 \quad\Longleftrightarrow\quad
 \pi_\sigma(J)=o((\beta R)^{-2k}).$$ Moreover, $$\label{eq:phase-conversion}
 \boxed{
 (\beta R)^{-2k}
 =\sigma^{\kappa_{\rm proj}}
  (\beta R)^{-2\eta_\sigma}.}$$ If $$\label{eq:critical-assumption}
 (\beta R)^{2k}\pi_\sigma(J)\longrightarrow p,
 \qquad \eta_\sigma\longrightarrow\eta,$$ then $$\label{eq:critical-limit}
 \frac{\mathcal G_{\sigma,k}(J)}{H_k}
 \longrightarrow 2C_*\lambda^\eta p.$$

Bounded phase makes $2C_*\lambda^{\eta_\sigma}\{1+o(1)\}$ bounded above and away from zero. This proves [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"} from [\[thm:moving-scale\]](#thm:moving-scale){reference-type="ref" reference="thm:moving-scale"}. From [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"}, $k=\log(1/\sigma)/(2\log\lambda)+\eta_\sigma$; inserting this into the left side of [\[eq:phase-conversion\]](#eq:phase-conversion){reference-type="eqref" reference="eq:phase-conversion"} proves the exact identity. Finally apply [\[eq:critical-assumption\]](#eq:critical-assumption){reference-type="eqref" reference="eq:critical-assumption"} to [\[eq:G-over-H\]](#eq:G-over-H){reference-type="eqref" reference="eq:G-over-H"}.

# A forced large parity cell, but not a physical obstruction

[\[thm:partition-max\]]{#thm:partition-max label="thm:partition-max"} Let $\mathcal P=\{J_1,\ldots,J_N\}$ be one fixed finite measurable partition. Then $$\label{eq:max-pi}
 \max_{1\le i\le N}\pi_\sigma(J_i)\ge\frac1N.$$ Consequently, $$\label{eq:max-G}
 \max_{1\le i\le N}
 \frac{\mathcal G_{\sigma,k}(J_i)}{H_k}\longrightarrow+\infty.$$ The maximizing index may depend on $\sigma$. Along every sequence $\sigma_\ell\to0$, some fixed index recurs as a maximizer on a subsequence, and its normalized parity cell diverges on that subsequence.

RH-335 gives $\sum_{i=1}^N\pi_\sigma(J_i)=1$, so the maximum is at least the arithmetic mean $1/N$, even though individual masses may be negative. The scalar in [\[eq:G-over-H\]](#eq:G-over-H){reference-type="eqref" reference="eq:G-over-H"} is positive for small noise. Since bounded phase makes $\lambda^{\eta_\sigma}$ uniformly bounded below and $\beta R>1$, [\[eq:max-pi\]](#eq:max-pi){reference-type="eqref" reference="eq:max-pi"} proves [\[eq:max-G\]](#eq:max-G){reference-type="eqref" reference="eq:max-G"}. The subsequence statement is the pigeonhole principle on the finite index set.

The theorem concerns only the parity-gauge constituent. It does not identify a maximizing cell with the physical $\mathcal B+\mathcal S$ aggregate, and it does not prove a physical nonzero normalized obstruction. The localized raw defect can cancel the parity term inside a corrected cell, other cells can cancel in the partition sum, and the first-alias coefficient further subtracts $\mathcal A_{k,2k}$. The maximizing index may also move with noise. Thus physical signed $\Delta_B+\Delta_S$ cancellation remains `NOT_TESTABLE`.

# A strictly positive isospectral Markov family

We now give a separate finite algebraic witness. Reuse the exact RH-335 matrix and parity projector $$\begin{aligned}
 K&=\begin{pmatrix}
 3/17&7/51&35/51\\
 4/85&83/255&32/51\\
 58/85&1/51&76/255
 \end{pmatrix},\label{eq:K}\\
 E_-&=\begin{pmatrix}
 10/17&-5/51&-25/51\\
 8/17&-4/51&-20/51\\
 -10/17&5/51&25/51
 \end{pmatrix}.\label{eq:E}\end{aligned}$$ For $t\ne1$, put $$\label{eq:S-family}
 S_t=\begin{pmatrix}1-t&t&0\\0&1&0\\0&0&1\end{pmatrix},
 \qquad K_t=S_t^{-1}KS_t.$$ Define $q(t)=35-38t-12t^2$. Exact multiplication gives the audited formula $$\label{eq:Kt-formula}
 K_t=\begin{pmatrix}
 \dfrac{15-4t}{85}&\dfrac{q(t)}{255(1-t)}
   &\dfrac{35-32t}{51(1-t)}\\[0.8em]
 \dfrac{4(1-t)}{85}&\dfrac{83+12t}{255}&\dfrac{32}{51}\\[0.8em]
 \dfrac{58(1-t)}{85}&\dfrac{5+174t}{255}&\dfrac{76}{255}
 \end{pmatrix}.$$

[\[thm:positive-family\]]{#thm:positive-family label="thm:positive-family"} For every $$\label{eq:sufficient-interval}
 \boxed{-\frac5{174}<t<\frac12,}$$ the matrix $K_t$ is strictly positive and row-stochastic. For every such $t$, $$\label{eq:spectrum}
 \operatorname{spec}(K_t)=\{1,-2/5,1/5\},$$ and for every integer $m\ge1$, $$\label{eq:all-traces}
 \boxed{
 \operatorname{Tr}K_t^m=1+(-2/5)^m+(1/5)^m.}$$

On [\[eq:sufficient-interval\]](#eq:sufficient-interval){reference-type="eqref" reference="eq:sufficient-interval"}, every denominator in [\[eq:Kt-formula\]](#eq:Kt-formula){reference-type="eqref" reference="eq:Kt-formula"} is positive. The nonconstant numerators $$15-4t,\quad q(t),\quad35-32t,\quad83+12t,\quad5+174t$$ are also positive; for $q$, it suffices that $t<1/2$ because its positive root exceeds $1/2$. More directly, $q'(t)=-38-24t<0$ on the stated interval and $q(1/2)=13$, so $q(t)>13$. Thus every entry is positive. Since $S_t\mathbf 1=\mathbf 1$, also $S_t^{-1}\mathbf 1=\mathbf 1$, and $K_t\mathbf 1=S_t^{-1}K\mathbf 1=\mathbf 1$.

Similarity preserves the spectrum and gives $K_t^m=S_t^{-1}K^mS_t$. RH-335 supplies the three distinct eigenvalues of $K$, so trace invariance proves [\[eq:all-traces\]](#eq:all-traces){reference-type="eqref" reference="eq:all-traces"}.

The interval [\[eq:sufficient-interval\]](#eq:sufficient-interval){reference-type="eqref" reference="eq:sufficient-interval"} is convenient, not maximal. Intersecting all strict entry inequalities in the connected component containing zero gives $$\label{eq:maximal-interval}
 \left(-\frac5{174},\frac{-19+\sqrt{781}}{12}\right).$$ The upper endpoint is the positive root of $q(t)$. No maximality claim is made beyond this explicit finite family.

# Moving projector masses and corrected singleton cells

Let $$\label{eq:Et}
 E_-(t)=S_t^{-1}E_-S_t.$$ It is the Riesz projector of $K_t$ at $-2/5$ by similarity.

[\[prop:pi-drift\]]{#prop:pi-drift label="prop:pi-drift"} For the three singleton windows, $$\label{eq:pi-t}
 \boxed{
 \pi(t)=\operatorname{diag}E_-(t)
 =\left(\frac{10-8t}{17},\frac{-4+24t}{51},\frac{25}{51}\right).}$$ Therefore $$\label{eq:pi-drift}
 \pi(t)-\pi(0)=\frac{8t}{17}(-1,1,0),
 \qquad \sum_i\pi_i(t)=1.$$

Insert [\[eq:E\]](#eq:E){reference-type="eqref" reference="eq:E"} and [\[eq:S-family\]](#eq:S-family){reference-type="eqref" reference="eq:S-family"} into [\[eq:Et\]](#eq:Et){reference-type="eqref" reference="eq:Et"} and read the diagonal. Subtraction gives [\[eq:pi-drift\]](#eq:pi-drift){reference-type="eqref" reference="eq:pi-drift"}; its entries sum to zero.

Use now the RH-335 fixed-order fixture $n=2$, $r_H=17/20$, parity eigenvalue $-2/5$, and zero deterministic singleton slots. Define $$\label{eq:Ct-def}
 \mathcal C_i(t)=\left(\frac{20}{17}\right)^2
 \left\{(K_t^2)_{ii}+\frac{21}{25}\pi_i(t)\right\}.$$

[\[thm:C-drift\]]{#thm:C-drift label="thm:C-drift"} The corrected singleton cells are $$\label{eq:C-t}
 \boxed{
 \mathcal C(t)=\left(
 \frac{6800-5760t}{4913},
 \frac{400+5760t}{4913},
 \frac{6672}{4913}\right).}$$ For every admissible $t$, $$\begin{aligned}
 \sum_i\mathcal C_i(t)&=\frac{48}{17},\label{eq:C-total}\\
 \mathcal C(t)-\mathcal C(0)&=\frac{5760t}{4913}(-1,1,0).
 \label{eq:C-drift}\end{aligned}$$ At $t=1/100$, the drift is exactly $$\label{eq:one-percent-drift}
 \left(-\frac{288}{24565},\frac{288}{24565},0\right).$$

Similarity applied to $K^2$ gives $$\operatorname{diag}K_t^2
 =\left(\frac{215-192t}{425},
 \frac{53+192t}{425},\frac{242}{425}\right).$$ Combine this with [\[eq:pi-t\]](#eq:pi-t){reference-type="eqref" reference="eq:pi-t"} in [\[eq:Ct-def\]](#eq:Ct-def){reference-type="eqref" reference="eq:Ct-def"} and simplify to [\[eq:C-t\]](#eq:C-t){reference-type="eqref" reference="eq:C-t"}. Summation and subtraction prove [\[eq:C-total\]](#eq:C-total){reference-type="eqref" reference="eq:C-total"}--[\[eq:C-drift\]](#eq:C-drift){reference-type="eqref" reference="eq:C-drift"}; setting $t=1/100$ gives [\[eq:one-percent-drift\]](#eq:one-percent-drift){reference-type="eqref" reference="eq:one-percent-drift"}.

The full spectrum and all power traces are constant, yet the corrected singleton cells move. This proves nonidentification of those cells from global spectral data in a strictly positive row-stochastic family. RH-210 already proved the general logical phenomenon that projectors may move under a fixed divisor [@WangDivisorPivot2026]. The narrow addition here is the simultaneous positivity, Markov normalization, all-power trace lock, and explicit corrected-cell ledger.

The family remains nonphysical finite algebra. In particular, fixed $n=2$ is not a $k=1$ first-alias counterloop: the archived counterloop definition requires $k\ge2$.

# Reproduction and claim boundary

The artifact evaluates every matrix identity with exact rational arithmetic. It checks the displayed formulas, the exact rational exponent-separation certificate, strict positivity at rational sample points inside the proved interval, the endpoint factorization, two-sided projector intertwining, twelve power traces, projector masses, corrected cells, invariant sums, and the exact one-percent drift. Floating-point rows only reproduce the symbolic phase conversion and the diagnostic exponent; they are not interval certificates.

RH-336 proves the moving projector-mass threshold and a nonphysical isospectral corrected-cell obstruction. It does not identify a physical $\Delta_B+\Delta_S$ cancellation, prove a physical nonzero normalized obstruction, exclude raw/local/alias signed cancellation, close the far or off-alias terms, transport the noisy head, or glue a determinant. No result constructs a Hilbert--Polya operator, identifies Riemann zeros, proves a von Mangoldt trace formula or completed-zeta divisor equality, or proves the Riemann hypothesis. Gates A--E remain false/open.
