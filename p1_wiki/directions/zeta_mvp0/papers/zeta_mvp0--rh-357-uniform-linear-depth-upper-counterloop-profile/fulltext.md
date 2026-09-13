---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-357-uniform-linear-depth-upper-counterloop-profile"
canonical_tex: "zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile/main.pdf"
source_sha256: "c23565f0ce95d76ad3e61b1fe27570dc76f80eb580f78071cb8d6790168c9516"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Uniform Linear-Depth Profile for the Upper Counterloop Band

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-357-uniform-linear-depth-upper-counterloop-profile/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We resolve the deterministic graded-counterloop budget at every integer depth below the second alias. Let $y_k=(\beta_kR)^2$, $x=(\beta R)^2>1$, and $y_k=x\exp[-\log C_M/k+o(k^{-1})]$. If $$A_k=(1-k^{-1})y_k^k,
   \qquad
   B_k(L)=\sum_{j=1}^{L}\frac{y_k^{k+j}}{k+j},
   \qquad 1\le L\le k-1,$$ then, uniformly over the complete range of $L$, $$B_k(L)=\frac{y_k^{k+L+1}(1-y_k^{-L})}{(k+L)(y_k-1)}
   \left(1+O(k^{-1})\right).$$ The source-locked form and the ratio to the first alias are $$B_k(L)=\frac{x^{k+L+1}(1-x^{-L})}
   {C_M^{1+L/k}(k+L)(x-1)}(1+o(1)),
   \quad
   \frac{B_k(L)}{A_k}=\frac{x^{L+1}(1-x^{-L})}
   {C_M^{L/k}(k+L)(x-1)}(1+o(1)),$$ again with uniform relative errors. Consequently, if $L/k\to\alpha\in(0,1]$, the constants $C_M^{-(1+\alpha)}$ and $C_M^{-\alpha}$ and the denominator factor $(1+\alpha)^{-1}$ are unavoidable; the $k$th-root rates are $x^{1+\alpha}$ and $x^\alpha$. For $L=\lfloor\alpha k+c\rfloor$, the phase $\theta_k=\{\alpha k+c\}$ remains in the normalized leading term. Rational slopes give a finite periodic orbit, while irrational slopes give the full closed phase interval. The actual-head transfer is stated only conditionally on the original unnormalized same-clock leaf $D_{4k}(R)\to0$. No root or rank identification, Gate A--E promotion, Hilbert--Polya construction, zero identification, or proof of RH is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Uniform Linear-Depth Profile\
  for the Upper Counterloop Band
```

## Markdown 正文

# Source-locked counterloop ledger

Fix the physical constants $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10}.$$ Let $k=k_\sigma\to\infty$ be the first-alias clock used in RH-342. The boundary multiplier law from RH-17 is $$\label{eq:multiplier}
 |M_k|=C_M\lambda^k\{1+o(1)\},\qquad C_M>0.$$ The Hardy-normalized radii are $$\label{eq:beta}
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},
 \qquad \beta=\frac1{r_H\sqrt\lambda},$$ so that $$\label{eq:x-y}
 x=(\beta R)^2=\frac{(R/r_H)^2}{\lambda}>1,
 \qquad
 y_k=(\beta_kR)^2
 =x\exp\left[-\frac{\log C_M}{k}+o(k^{-1})\right].$$ The strict inequality $x>1$ follows from the certified upper bound on $\lambda$[@WangProjectorMass2026; @WangTimeOrdered2026].

The finite graded counterloop is $$\label{eq:Y}
 \mathcal Y_k=\{\beta_ke^{ij\pi/k},\beta_ke^{-ij\pi/k}:1\le j\le k-1\}.$$ Its exact power ledger is $$\label{eq:s-ledger}
 s_{k,n}=\sum_{\nu\in\mathcal Y_k}\nu^n
 =\beta_k^n\bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr)$$ [@WangAliasLedger2026; @WangHeadCounterloop2026]. Thus the first alias at order $2k$ has weighted modulus $$\label{eq:A}
 A_k:=\frac{|s_{k,2k}|R^{2k}}{2k}=(1-k^{-1})y_k^k.$$ For $1\le L\le k-1$, define the even post-first-alias budget $$\label{eq:B}
 B_k(L):=\sum_{j=1}^{L}
 \frac{|s_{k,2k+2j}|R^{2k+2j}}{2k+2j}
 =\sum_{j=1}^{L}\frac{y_k^{k+j}}{k+j}.$$ The upper bound $L\le k-1$ is exactly the strict band $2k<2k+2L<4k$; the odd counterloop moments in this band vanish.

[\[prop:exact\]]{#prop:exact label="prop:exact"} For every finite $k\ge2$ and $1\le L\le k-1$, $$\label{eq:exact-ratio}
 \frac{B_k(L)}{A_k}=\frac{k}{k-1}\sum_{j=1}^{L}\frac{y_k^j}{k+j}.$$

In the strict upper band, [\[eq:s-ledger\]](#eq:s-ledger){reference-type="eqref" reference="eq:s-ledger"} gives $s_{k,2k+2j}=-2\beta_k^{2k+2j}$. Substitution into [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} and division by [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"} gives [\[eq:exact-ratio\]](#eq:exact-ratio){reference-type="eqref" reference="eq:exact-ratio"}.

# Uniform endpoint localization

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} Assume [\[eq:x-y\]](#eq:x-y){reference-type="eqref" reference="eq:x-y"}. There is a constant (depending only on the eventual compact neighborhood of $x$) such that, uniformly for every integer $1\le L\le k-1$, $$\label{eq:y-endpoint}
 \boxed{
 B_k(L)=\frac{y_k^{k+L+1}(1-y_k^{-L})}{(k+L)(y_k-1)}
 \left(1+O(k^{-1})\right).}$$ Moreover, uniformly over the same complete band, $$\begin{aligned}
 B_k(L)&=\frac{x^{k+L+1}(1-x^{-L})}
 {C_M^{1+L/k}(k+L)(x-1)}(1+o(1)),\label{eq:x-endpoint}\\
 \frac{B_k(L)}{A_k}&=\frac{x^{L+1}(1-x^{-L})}
 {C_M^{L/k}(k+L)(x-1)}(1+o(1)).\label{eq:ratio-endpoint}\end{aligned}$$ All $o(1)$ terms in this theorem are relative errors uniform in $L$.

Reindex the sum in [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} from its terminal coordinate: $$\label{eq:reindex}
 B_k(L)=\frac{y_k^{k+L}}{k+L}
 \sum_{r=0}^{L-1}y_k^{-r}\frac{k+L}{k+L-r}.$$ Since $y_k\to x>1$, choose $1<\xi<x$ so that $y_k\ge\xi$ for all large $k$. Writing the last factor as $1+r/(k+L-r)$ gives $$0\le\sum_{r=0}^{L-1}y_k^{-r}
 \left(\frac{k+L}{k+L-r}-1\right)
 \le\frac1{k+1}\sum_{r\ge0}r\xi^{-r}=O(k^{-1}).$$ The unweighted geometric sum is at least $1$, so the sum in [\[eq:reindex\]](#eq:reindex){reference-type="eqref" reference="eq:reindex"} equals $$\sum_{r=0}^{L-1}y_k^{-r}\{1+O(k^{-1})\}
 =\frac{y_k}{y_k-1}(1-y_k^{-L})\{1+O(k^{-1})\},$$ with the relative error uniform in $L$. This proves [\[eq:y-endpoint\]](#eq:y-endpoint){reference-type="eqref" reference="eq:y-endpoint"}.

For the source-locked replacement, put $$\rho_k:=k\log(y_k/x)+\log C_M\longrightarrow0.$$ Then, uniformly for $L\le k-1$, $$\label{eq:power-replacement}
 \frac{y_k^{k+L+1}}
 {x^{k+L+1}C_M^{-(1+L/k)}}
 =C_M^{-1/k}\exp\left((1+L/k+1/k)\rho_k\right)\longrightarrow1.$$ The function $$G_L(t):=\frac{1-t^{-L}}{t-1}=\sum_{r=1}^{L}t^{-r}$$ has $|G_L'(t)|\le\sum_{r\ge1}r\xi^{-r-1}$ for $t\ge\xi$ and $G_L(x)\ge x^{-1}$. Hence $G_L(y_k)/G_L(x)\to1$ uniformly in $L\ge1$. Combining this observation with [\[eq:y-endpoint\]](#eq:y-endpoint){reference-type="eqref" reference="eq:y-endpoint"} and [\[eq:power-replacement\]](#eq:power-replacement){reference-type="eqref" reference="eq:power-replacement"} proves [\[eq:x-endpoint\]](#eq:x-endpoint){reference-type="eqref" reference="eq:x-endpoint"}. Finally, $$A_k=(1-k^{-1})y_k^k=C_M^{-1}x^k(1+o(1)),$$ and division of [\[eq:x-endpoint\]](#eq:x-endpoint){reference-type="eqref" reference="eq:x-endpoint"} by this expression gives [\[eq:ratio-endpoint\]](#eq:ratio-endpoint){reference-type="eqref" reference="eq:ratio-endpoint"}; the factor $C_M^{-1}$ cancels from the ratio.

The denominator is not replaced by $k$ when $L$ is linear. Instead, after reversal, the geometrically decaying weight $y_k^{-r}$ makes the weighted average of $r$ bounded, while every denominator $k+L-r$ is at least $k+1$. This is the reason the complete-band error remains $O(k^{-1})$.

# Linear depth and physical-clock rates

[\[cor:linear\]]{#cor:linear label="cor:linear"} If $L=L_k$ satisfies $1\le L_k\le k-1$ and $$\frac{L_k}{k}\longrightarrow\alpha\in(0,1],$$ then $$\begin{aligned}
 A_k&\sim C_M^{-1}x^k,\label{eq:A-asymp}\\
 B_k(L_k)&\sim
 \frac{x^{k+L_k+1}}
 {C_M^{1+\alpha}k(1+\alpha)(x-1)},\label{eq:B-linear}\\
 \frac{B_k(L_k)}{A_k}&\sim
 \frac{x^{L_k+1}}
 {C_M^{\alpha}k(1+\alpha)(x-1)}.\label{eq:ratio-linear}\end{aligned}$$ In particular, $$\label{eq:roots}
 \lim_{k\to\infty}B_k(L_k)^{1/k}=x^{1+\alpha},
 \qquad
 \lim_{k\to\infty}\left(\frac{B_k(L_k)}{A_k}\right)^{1/k}=x^\alpha.$$

Because $\alpha>0$, $L_k\to\infty$, so $1-x^{-L_k}\to1$. Also $k+L_k\sim(1+\alpha)k$ and $C_M^{L_k/k}\to C_M^\alpha$. Substitution into [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} gives [\[eq:B-linear\]](#eq:B-linear){reference-type="eqref" reference="eq:B-linear"} and [\[eq:ratio-linear\]](#eq:ratio-linear){reference-type="eqref" reference="eq:ratio-linear"}; [\[eq:A-asymp\]](#eq:A-asymp){reference-type="eqref" reference="eq:A-asymp"} follows directly from [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"} and [\[eq:x-y\]](#eq:x-y){reference-type="eqref" reference="eq:x-y"}. Taking logarithms and dividing by $k$ gives [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"}; all polynomial factors and fixed positive constants have zero logarithmic rate.

On the physical first-alias clock, RH-355 records $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1).$$ Thus the terminal order $n_k=2k+2L_k$ obeys $$\label{eq:order-rate}
 \frac{n_k}{\log(1/\sigma)}\longrightarrow\frac{1+\alpha}{\log\lambda},
 \qquad
 \frac{n_k-2k}{\log(1/\sigma)}\longrightarrow\frac{\alpha}{\log\lambda}.$$ The budget logarithmic rates are $$\begin{aligned}
 \frac{\log B_k(L_k)}{\log(1/\sigma)}&\longrightarrow
 \frac{(1+\alpha)\log x}{2\log\lambda},\label{eq:B-clock-rate}\\
 \frac{\log(B_k(L_k)/A_k)}{\log(1/\sigma)}&\longrightarrow
 \frac{\alpha\log x}{2\log\lambda}.\label{eq:ratio-clock-rate}\end{aligned}$$ These are deterministic counterloop rates, not probabilities or actual-head measurements.

# Phase-safe integer normalization

[\[thm:phase\]]{#thm:phase label="thm:phase"} Fix $\alpha\in(0,1]$ and $c\in\mathbb R$, and let $$L_k=\lfloor\alpha k+c\rfloor,
 \qquad \theta_k=\{\alpha k+c\}.$$ Assume $1\le L_k\le k-1$ eventually (for $\alpha=1$ this requires $c<0$). Then $$\begin{aligned}
 kx^{-(1+\alpha)k}B_k(L_k)
 &=\frac{x^{c+1-\theta_k}}
 {C_M^{1+\alpha}(1+\alpha)(x-1)}(1+o(1)),\label{eq:phase-B}\\
 kx^{-\alpha k}\frac{B_k(L_k)}{A_k}
 &=\frac{x^{c+1-\theta_k}}
 {C_M^{\alpha}(1+\alpha)(x-1)}(1+o(1)).\label{eq:phase-ratio}\end{aligned}$$ If $\alpha=a/b$ is rational in lowest terms, $\theta_k$ has the exact period-$b$ orbit $$\left\{\left\{\frac{ar}{b}+c\right\}:0\le r<b\right\};$$ the normalized quantities have the corresponding finite cluster sets. If $\alpha$ is irrational, $\{\theta_k:k\ge1\}$ is dense in $[0,1]$, and the closed cluster sets in [\[eq:phase-B\]](#eq:phase-B){reference-type="eqref" reference="eq:phase-B"} and [\[eq:phase-ratio\]](#eq:phase-ratio){reference-type="eqref" reference="eq:phase-ratio"} are, respectively, $$\begin{aligned}
 \left[\frac{x^c}{C_M^{1+\alpha}(1+\alpha)(x-1)},
       \frac{x^{c+1}}{C_M^{1+\alpha}(1+\alpha)(x-1)}\right],\label{eq:phase-cluster-B}\\
 \left[\frac{x^c}{C_M^{\alpha}(1+\alpha)(x-1)},
       \frac{x^{c+1}}{C_M^{\alpha}(1+\alpha)(x-1)}\right].\label{eq:phase-cluster-ratio}\end{aligned}$$

Write $L_k=\alpha k+c-\theta_k$ in [\[eq:B-linear\]](#eq:B-linear){reference-type="eqref" reference="eq:B-linear"} and [\[eq:ratio-linear\]](#eq:ratio-linear){reference-type="eqref" reference="eq:ratio-linear"}; the two displayed normalizations follow directly. For rational $a/b$, adding $a/b$ permutes the $b$ residue classes modulo one, which gives the stated finite orbit. For irrational $\alpha$, the standard irrational-rotation lemma says that the fractional parts of $k\alpha+c$ are dense modulo one. A short proof uses the pigeonhole approximation $0<\|q\alpha\|<1/N$ and the translates of the resulting fine mesh; letting $N\to\infty$ gives a point in every subinterval of $[0,1)$. The continuous map $t\mapsto x^{c+1-t}$ then maps the closed phase set to the intervals in [\[eq:phase-cluster-B\]](#eq:phase-cluster-B){reference-type="eqref" reference="eq:phase-cluster-B"}--[\[eq:phase-cluster-ratio\]](#eq:phase-cluster-ratio){reference-type="eqref" reference="eq:phase-cluster-ratio"}.

For $\alpha=1$ and any $c\in[-1,0)$, $L_k=k-1$ and $\theta_k=c+1$. Equation [\[eq:phase-B\]](#eq:phase-B){reference-type="eqref" reference="eq:phase-B"} becomes $$kx^{-2k}B_k(k-1)\longrightarrow\frac1{2C_M^2(x-1)},$$ which is exactly the complete strict upper-band constant of RH-355. The phase notation is still useful for terminal lags other than one.

# Boundary stitching and conditional actual-head transfer

The complete theorem includes bounded depths, but the simplification $1-x^{-L}\sim1$ does not. If $L$ is fixed, the factor is a leading constant. If $L\to\infty$ while $L=o(k)$, it may be deleted and RH-356's mesoscopic law is recovered. The case $L/k\to0$ with bounded $L$ is therefore not the same asymptotic regime as the case $L/k\to0$ with $L\to\infty$.

At the other endpoint $L=k-1$, [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} is the whole strict upper band and the theorem recovers RH-355. No interpolation of these deterministic budgets is an actual-head result.

Let $\mathcal H_\sigma$ be the actual modulus-complete Hardy head of RH-342, with moments $h_{\sigma,n}$, and put $$d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}.$$ The original unnormalized same-clock transport leaf is $$\label{eq:D}
 D_{4k}(R):=\sum_{2\le n<4k}\frac{|d_{\sigma,k,n}|R^n}{n}\longrightarrow0.$$ It is an open hypothesis, not proved in this paper. Define $$\begin{aligned}
 A_k^{\mathcal H}&:=\frac{|h_{\sigma,2k}|R^{2k}}{2k},\label{eq:AH}\\
 B_k^{\mathcal H}(L)&:=\sum_{j=1}^{L}
 \frac{|h_{\sigma,2k+2j}|R^{2k+2j}}{2k+2j},\label{eq:BH}\\
 O_k^{\mathcal H}(L)&:=\sum_{2k<n\le2k+2L-1,\ n\ \mathrm{odd}}
 \frac{|h_{\sigma,n}|R^n}{n}.\end{aligned}$$

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Assume [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} on one physical clock. Then $$\label{eq:conditional-budgets}
 \frac{A_k^{\mathcal H}}{A_k}\to1,
 \qquad
 \sup_{1\le L\le k-1}
 \left|\frac{B_k^{\mathcal H}(L)}{B_k(L)}-1\right|\to0,
 \qquad
 \sup_{1\le L\le k-1}O_k^{\mathcal H}(L)\to0.$$ Consequently the linear-depth and phase-safe budget formulas transfer to $B_k^{\mathcal H}(L)/A_k^{\mathcal H}$ only under this hypothesis.

The reverse triangle inequality and the fact that every displayed order lies below $4k$ give $$|A_k^{\mathcal H}-A_k|\le D_{4k}(R),
 \qquad
 |B_k^{\mathcal H}(L)-B_k(L)|\le D_{4k}(R).$$ Since $A_k\sim C_M^{-1}x^k$ and, uniformly for $L\ge1$, $$B_k(L)\ge B_k(1)=\frac{y_k^{k+1}}{k+1}
 \sim\frac{x^{k+1}}{C_M k},$$ division by these diverging lower bounds proves the first two assertions. The counterloop odd moments vanish, so each actual odd budget is bounded by $D_{4k}(R)$. The ratio assertion follows by dividing the two inherited even budget asymptotics. This is a conditional budget statement only; it neither identifies actual roots or rank nor proves [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}.

# Scope, next route, and reproducibility

The endpoint theorem is a deterministic statement about the source-locked finite graded shell. Its numerical rows are exact rational or high-precision synthetic checks and are not finite-order evidence for an all-order theorem beyond the proof above. In particular, the paper does not replace the counterloop by an actual noisy operator, turn a local law into a trace law, or identify any Riemann zero.

The next read-only candidate is RH-358: reindex the upper band by the terminal lag $q=k-1-L$ and quantify the resulting geometric localization. It should remain on the deterministic counterloop until a typed actual-head theorem is available.

#### Reproduction.

The accompanying Python artifact implements exact rational rows, the full-band endpoint-error envelope, rational phase orbits, and high-precision synthetic linear-depth rows. It explicitly marks every row as formula reproduction only. Build and archive commands are listed in the README.
