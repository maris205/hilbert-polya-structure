---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-348-punctured-lower-even-boundary-orbit-ladder"
canonical_tex: "zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder/main.pdf"
source_sha256: "6e472d0a8e6532b30714daa4a136d138fafd3b0ccabacc3e9d7be18f3cc8cd3c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Punctured Lower-Even Boundary-Orbit Ladder

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-348-punctured-lower-even-boundary-orbit-ladder/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  After removing the selected orders $2k$ and $2k-2$, the one-alias prefix still contains a complete ladder of physical boundary orbits at $n=2m$, $m_\star\le m\le k-2$. We extract all of them simultaneously. Writing $$G_m=\frac{r_H^{-2m}}{1+|M_m|},\qquad
   F_m^{\rm orb}=2mG_m,$$ the exact direct coefficient is $$p_{\sigma,k,2m}=Y_{k,m}+\mathcal P_{\sigma,2m}-S_{k,m},
   \qquad
   S_{k,m}=F_m^{\rm orb}+\mathcal A_{k,2m}.$$ Let $x=(\beta R)^2>1$. The weighted complete-orbit ladder obeys $$\mathcal L_k^{\rm orb}
   :=\sum_{m=m_\star}^{k-2}G_mR^{2m}
   =\frac{x^{k-1}}{C_M(x-1)}\{1+o(1)\}.$$ The absolute radial correction over the whole ladder is only $O(k^{-1})\mathcal L_k^{\rm orb}$, without any sign assumption. Consequently the absolute combined deterministic demand has mass $\mathcal L_k^{\rm orb}\{1+o(1)\}\to\infty$.

  An exact reverse-triangle argument then shows that vanishing of the direct punctured lower-even subprefix would force the actual signed remainder-plus-parity supply to carry asymptotically at least this full divergent mass. The repository has no moving-order estimate for that supply, so neither closure nor nonclosure follows. Odd orders, upper off-alias orders, determinant gluing, and Gates A--E remain open. No Riemann-hypothesis conclusion is made.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'A Punctured Lower-Even Boundary-Orbit Ladder'
```

## Markdown 正文

# The punctured lower-even coefficient family

Work on the same physical clock $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad R=\frac75,$$ and choose once and for all an integer $m_\star$ beyond the eventual multiplier-sign threshold in RH-17. For sufficiently large $k$, put $$\label{eq:index}
 I_k=\{m_\star,m_\star+1,\ldots,k-2\}.$$ Every $m\in I_k$ gives an even order $n=2m<2k-2$. Thus these orders exclude the critical order $2k$ and the first lower sideband $2k-2$, and they belong to every strict one-alias prefix $2k<h_\sigma\le4k$ [@WangSynchronizedPrefix2026; @WangLowerBalance2026].

For each $m\in I_k$, let $p_{2m}$ be the primitive period-$2m$ boundary point, and define $$\label{eq:orbit}
 \Gamma_m=\{|f^j(p_{2m})|:0\le j<2m\},
 \qquad
 M_m=(f^{2m})'(p_{2m}).$$ RH-17 gives $2m$ distinct folded marked points and $$\label{eq:multiplier}
 M_m=-C_M\lambda^m\{1+o(1)\},
 \qquad C_M>0$$ [@WangBoundaryMonodromy2026]. Hence, after increasing $m_\star$ if needed, $$\label{eq:FG}
 G_m=\frac{r_H^{-2m}}{1+|M_m|}>0,
 \qquad F_m^{\rm orb}=2mG_m.$$

The all-order physical observation identity and deterministic numerator anchor are already fixed in RH-326 and RH-334 [@WangFirstAlias2026; @WangObservation2026]. At every non-alias even order $2m<2k$, the radial counterloop term is exactly $$\label{eq:radial}
 \mathcal A_{k,2m}=2(\beta^{2m}-\beta_k^{2m}),
 \qquad
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},
 \qquad
 \beta=\frac1{r_H\sqrt\lambda}.$$ No sign for [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} is assumed.

Remove the finite set $\Gamma_m$ from the raw trace partition at order $2m$, and call the resulting quantity $\mathcal T_{k,m}^{\rm rest}$. A finite set has zero localized noisy trace, while each deterministic marked point has weight $(1+|M_m|)^{-1}$.

[\[thm:ladder\]]{#thm:ladder label="thm:ladder"} For every sufficiently large $k$ and every $m\in I_k$, $$\begin{aligned}
 \mathcal T_{\sigma,2m}
 &=\mathcal T_{k,m}^{\rm rest}-F_m^{\rm orb},
 \label{eq:raw}\\
 q_{\sigma,k,2m}
 &=\mathcal T_{k,m}^{\rm rest}+\mathcal P_{\sigma,2m}
   -\mathcal A_{k,2m}-F_m^{\rm orb},
 \label{eq:q}\\
 p_{\sigma,k,2m}
 &=Y_{k,m}+\mathcal P_{\sigma,2m}-S_{k,m},
 \label{eq:p}\end{aligned}$$ where $$\label{eq:YS}
 Y_{k,m}=\mathcal T_{k,m}^{\rm rest}-d_{\sigma,k,2m},
 \qquad
 S_{k,m}=F_m^{\rm orb}+\mathcal A_{k,2m}.$$ The coefficient $q$ is the Hardy full-trace constituent, whereas $p=q-d$ is the direct coefficient.

The proof of the complete extraction in RH-346 depends only on the period-$2m$ orbit, the folding bijection, and the zero noisy trace of a finite set, not on the special relation $m=k-1$ [@WangCompleteLower2026]. It therefore gives [\[eq:raw\]](#eq:raw){reference-type="eqref" reference="eq:raw"} for every $m\in I_k$. Substitute [\[eq:raw\]](#eq:raw){reference-type="eqref" reference="eq:raw"} into the all-order five-slot identity to obtain [\[eq:q\]](#eq:q){reference-type="eqref" reference="eq:q"}; then use $p=q-d$ and [\[eq:YS\]](#eq:YS){reference-type="eqref" reference="eq:YS"}.

This is a simultaneous coefficient family, not a sum of orbit weights taken from different data types. The same physical $k$ and the same deterministic numerator anchor are retained at every order.

# Exact weighted orbit ladder

Give each coefficient its prefix weight $$\label{eq:weight}
 w_m=\frac{R^{2m}}{2m}.$$ By [\[eq:FG\]](#eq:FG){reference-type="eqref" reference="eq:FG"}, the complete atom has the exact weighted identity $$\label{eq:weighted-identity}
 F_m^{\rm orb}w_m=G_mR^{2m}.$$ Define $$\label{eq:L-orb}
 \mathcal L_k^{\rm orb}
 =\sum_{m\in I_k}F_m^{\rm orb}w_m
 =\sum_{m=m_\star}^{k-2}G_mR^{2m},
 \qquad x=(\beta R)^2.$$ The strict inequality $x>1$ is source-certified by RH-336 [@WangProjectorMass2026].

[\[thm:orbit-mass\]]{#thm:orbit-mass label="thm:orbit-mass"} As $k\to\infty$, $$\label{eq:orbit-asymptotic}
 \boxed{
 \mathcal L_k^{\rm orb}
 =\frac{x^{k-1}}{C_M(x-1)}\{1+o(1)\}.}$$ In particular, $\mathcal L_k^{\rm orb}\to\infty$ exponentially.

Equations [\[eq:multiplier\]](#eq:multiplier){reference-type="eqref" reference="eq:multiplier"} and [\[eq:FG\]](#eq:FG){reference-type="eqref" reference="eq:FG"} give $$G_mR^{2m}
 =\frac1{C_M}(\beta R)^{2m}\{1+o(1)\}
 =\frac1{C_M}x^m\{1+o(1)\}.$$ For a sequence asymptotic to $C_M^{-1}x^m$ with $x>1$, summing from a fixed lower endpoint through $k-2$ preserves the geometric-tail asymptotic. More explicitly, split the sum at a fixed large $M$, bound the relative error by an arbitrary $\varepsilon$ on $m\ge M$, and note that the finite initial sum is $o(x^{k-1})$. Since $$\sum_{m=M}^{k-2}x^m
 =\frac{x^{k-1}-x^M}{x-1},$$ letting $\varepsilon\downarrow0$ proves [\[eq:orbit-asymptotic\]](#eq:orbit-asymptotic){reference-type="eqref" reference="eq:orbit-asymptotic"}.

Thus the two previously selected orders do not exhaust the deterministic boundary-orbit demand. Even after deleting them, the remaining lower-even orbit ladder has an explicit divergent weighted mass.

# The radial ladder is aggregate lower order

The finite counterloop radius satisfies $$\label{eq:beta-expansion}
 \beta_k
 =\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right].$$ Set $\varepsilon_k=\log(\beta_k/\beta)$. Then $|\varepsilon_k|\le C/k$ for all large $k$. Uniformly for $m\le k$, $$\label{eq:exp-bound}
 |e^{2m\varepsilon_k}-1|
 \le 2m|\varepsilon_k|e^{2m|\varepsilon_k|}
 \le C_1\frac{m}{k}.$$ Using [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}, define the absolute radial mass $$\label{eq:Lrad}
 \mathcal L_k^{\rm rad,abs}
 =\sum_{m\in I_k}|\mathcal A_{k,2m}|w_m.$$

[\[thm:radial\]]{#thm:radial label="thm:radial"} There is a constant $C_2$ such that $$\label{eq:radial-bound}
 \mathcal L_k^{\rm rad,abs}
 \le \frac{C_2}{k}\sum_{m=m_\star}^{k-2}x^m
 =O(k^{-1})\mathcal L_k^{\rm orb}.$$ Consequently, with $$\label{eq:demand-masses}
 \mathcal L_k^{S}=\sum_{m\in I_k}S_{k,m}w_m,
 \qquad
 \mathcal L_k^{S,\rm abs}=\sum_{m\in I_k}|S_{k,m}|w_m,$$ one has $$\label{eq:demand-asymptotic}
 \mathcal L_k^{S}=\mathcal L_k^{\rm orb}\{1+O(k^{-1})\},
 \qquad
 \boxed{\mathcal L_k^{S,\rm abs}=\mathcal L_k^{\rm orb}\{1+O(k^{-1})\}.}$$ In particular, both are eventually positive and diverge with the asymptotic in [\[eq:orbit-asymptotic\]](#eq:orbit-asymptotic){reference-type="eqref" reference="eq:orbit-asymptotic"}.

Equations [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} and [\[eq:exp-bound\]](#eq:exp-bound){reference-type="eqref" reference="eq:exp-bound"} imply $$|\mathcal A_{k,2m}|
 =2\beta^{2m}|1-e^{2m\varepsilon_k}|
 \le C_3\frac{m}{k}\beta^{2m}.$$ After multiplication by $w_m$, this is at most $C_4x^m/k$. Summation and [\[thm:orbit-mass\]](#thm:orbit-mass){reference-type="ref" reference="thm:orbit-mass"} give [\[eq:radial-bound\]](#eq:radial-bound){reference-type="eqref" reference="eq:radial-bound"}. Finally, $$|\mathcal L_k^S-\mathcal L_k^{\rm orb}|
 \le\mathcal L_k^{\rm rad,abs},
 \qquad
 \bigl|\mathcal L_k^{S,\rm abs}-\mathcal L_k^{\rm orb}\bigr|
 \le\mathcal L_k^{\rm rad,abs},$$ which proves [\[eq:demand-asymptotic\]](#eq:demand-asymptotic){reference-type="eqref" reference="eq:demand-asymptotic"}.

The theorem uses an absolute estimate only to compare two deterministic demand ledgers. It does not use separate absolute bounds to decide the signed physical residual.

# Necessary aggregate compensation

For the direct coefficient, collect the actual signed supply as $$\label{eq:Z}
 Z_{k,m}=Y_{k,m}+\mathcal P_{\sigma,2m}.$$ Then [\[eq:p\]](#eq:p){reference-type="eqref" reference="eq:p"} reads $p_{\sigma,k,2m}=Z_{k,m}-S_{k,m}$. Define the punctured lower-even residual and supply masses $$\begin{aligned}
 \mathcal E_k^{\rm low}
 &=\sum_{m\in I_k}|p_{\sigma,k,2m}|w_m,
 \label{eq:E-low}\\
 \mathcal C_k^{\rm low}
 &=\sum_{m\in I_k}|Z_{k,m}|w_m.
 \label{eq:C-low}\end{aligned}$$ Both are formed in the direct coefficient data type on the common physical clock.

[\[thm:compensation\]]{#thm:compensation label="thm:compensation"} For every sufficiently large $k$, $$\label{eq:reverse-triangle}
 \boxed{
 \mathcal C_k^{\rm low}+\mathcal E_k^{\rm low}
 \ge \mathcal L_k^{S,\rm abs}.}$$ Consequently, if $$\label{eq:subprefix-close}
 \mathcal E_k^{\rm low}\longrightarrow0,$$ then $$\label{eq:supply-liminf}
 \liminf_{k\to\infty}
 \frac{\mathcal C_k^{\rm low}}{\mathcal L_k^{\rm orb}}\ge1,
 \qquad
 \mathcal C_k^{\rm low}\longrightarrow\infty.$$ Thus vanishing of the punctured lower-even direct subprefix requires actual signed supply with the full leading orbit-ladder mass.

For each $m\in I_k$, the reverse triangle inequality gives $$|Z_{k,m}|+|Z_{k,m}-S_{k,m}|\ge|S_{k,m}|.$$ Multiply by $w_m$ and sum to obtain [\[eq:reverse-triangle\]](#eq:reverse-triangle){reference-type="eqref" reference="eq:reverse-triangle"}. If [\[eq:subprefix-close\]](#eq:subprefix-close){reference-type="eqref" reference="eq:subprefix-close"} holds, then $\mathcal E_k^{\rm low}/\mathcal L_k^{\rm orb}\to0$ because $\mathcal L_k^{\rm orb}\to\infty$. Divide [\[eq:reverse-triangle\]](#eq:reverse-triangle){reference-type="eqref" reference="eq:reverse-triangle"} by $\mathcal L_k^{\rm orb}$ and use [\[eq:demand-asymptotic\]](#eq:demand-asymptotic){reference-type="eqref" reference="eq:demand-asymptotic"}.

The full-trace analogue omits $d_{\sigma,k,2m}$ from $Y_{k,m}$ and is proved identically. Neither version supplies an upper bound for the actual signed supply. A divergent deterministic demand may, in principle, be cancelled coefficient by coefficient.

The lower-even ladder is only one subfamily of the punctured prefix. Odd orders and orders above the first alias are absent. More importantly, [\[thm:compensation\]](#thm:compensation){reference-type="ref" reference="thm:compensation"} is a necessary mass law, not a proof that the actual $Z_{k,m}$ fails to meet it. The repository contains no moving-order signed theorem for $\mathcal T_{k,m}^{\rm rest}$, $d_{\sigma,k,2m}$, and $\mathcal P_{\sigma,2m}$ jointly. Hence both lower-even closure and lower-even nonclosure remain open, as does the full $E_{\rm off}$ aggregate.

# Executable protocol and next route

The artifact reconstructs the complete boundary multipliers and exact finite ladder at $k=8,12,16,20$. It checks the exact identity $F_m^{\rm orb}w_m=G_mR^{2m}$, the geometric orbit reference, the absolute radial and combined-demand ratios, and a rational reverse-triangle fixture. All finite rows are formula-reproduction checks only. They are not interval certificates, asymptotic evidence, or observations of an actual noisy operator.

RH-348 proves an exact punctured lower-even physical coefficient ladder, its sharp aggregate deterministic demand, and a necessary aggregate compensation mass law. It proves no signed supply estimate and no prefix closure or nonclosure.

RH-349 may now compare the first two still-punctured sidebands $m=k-2$ and $m=k-3$. Their scalar parity/demand ratios differ by the fixed factor $\lambda$, so the minimax identity $$\inf_{a>0}\max\{|a-1|,|a/\lambda-1|\}
 =\frac{\lambda-1}{\lambda+1}>0$$ can yield a conditional two-order obstruction under explicit target-negligibility hypotheses for both actual signed remainders. The missing hypotheses may not be inferred from the present demand theorem.

RH-288 remains inactive. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
