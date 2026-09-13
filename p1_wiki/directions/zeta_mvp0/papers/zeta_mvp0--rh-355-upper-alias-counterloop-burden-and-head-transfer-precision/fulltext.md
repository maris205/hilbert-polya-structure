---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-355-upper-alias-counterloop-burden-and-head-transfer-precision"
canonical_tex: "zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision/main.pdf"
source_sha256: "1958c7fb5f61cec5746c964d887795b7ce7bab7ea5f19f8e05ddd86456cb9a6e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Upper-Alias Counterloop Burden and Head-Transfer Precision

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-355-upper-alias-counterloop-burden-and-head-transfer-precision/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the complete strict upper-alias burden of the source-locked finite-radius graded counterloop on the physical clock. Let $x=(\beta R)^2>1$, $y_k=(\beta_kR)^2$, and $$\mathcal C_k^{\rm up}
   =\sum_{2k<n<4k}\frac{|s_{k,n}|R^n}{n}.$$ The exact counterloop ledger reduces this to $\sum_{m=k+1}^{2k-1}y_k^m/m$. The source-backed multiplier law $|M_k|=C_M\lambda^k\{1+o(1)\}$ then gives $$\mathcal C_k^{\rm up}
   \sim\frac{x^{2k}}{2C_M^2k(x-1)},\qquad
   x^{-k}\mathcal C_k^{\rm up}
   \sim\frac{x^k}{2C_M^2k(x-1)}.$$ Thus the normalized burden has $k$th root $x>1$. Its terminal coordinate $n=4k-2$ contributes an asymptotic fraction $(x-1)/x$.

  We next state the exact price of actual-head transport. Conditional on the original, unnormalized same-clock hypothesis $D_{4k}(R)\to0$, the actual upper-head budget has the same asymptotic, its odd upper budget tends to zero, every even upper coordinate has relative error $o(kx^{-k})$ uniformly, and the terminal coordinate has the stronger error $o(kx^{-2k})$. No theorem proving $D_{4k}(R)\to0$ is supplied. A weaker normalized upper defect still transfers the aggregate normalized budget but does not force bandwise relative matching. A complete $(2k+2)$th-root shell gives a conjugation-closed finite normal information-class counterexample: its normalized defect is $\sim x/(C_Mk)\to0$, while the relative error at $n=2k+2$ equals one and the unnormalized defect diverges. This is not an actual noisy operator. No root or rank identification, direct/full-trace transfer, RH-288 activation, Gate A--E, Hilbert--Polya, zero-identification, or RH conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Upper-Alias Counterloop Burden and\
  Head-Transfer Precision
```

## Markdown 正文

# One physical clock and the exact upper band

Fix $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10}.$$ Let $k=k_\sigma\to\infty$ be the physical first-alias clock used in RH-342. RH-17 proves the boundary multiplier law $$\label{eq:multiplier}
 |M_k|=C_M\lambda^k\{1+o(1)\},\qquad C_M>0,$$ and the finite counterloop radius is $$\label{eq:beta-k}
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},\qquad
 \beta=\frac1{r_H\sqrt\lambda}.$$ Consequently $$\label{eq:beta-asymptotic}
 \beta_k
 =\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right].$$ Put $$\label{eq:x-y}
 x=(\beta R)^2=\frac{(R/r_H)^2}{\lambda},\qquad
 y_k=(\beta_kR)^2
 =x\exp\left[-\frac{\log C_M}{k}+o(k^{-1})\right].$$ The certified upper bound for $\lambda$ makes $x>1$ [@WangProjectorMass2026; @WangTimeOrdered2026].

The counterloop is the finite multiset $$\label{eq:Y}
 \mathcal Y_k=\{\beta_ke^{ij\pi/k},\beta_ke^{-ij\pi/k}:1\le j\le k-1\}.$$ RH-342 locks it in the same Hardy normalization as the actual modulus-complete head and proves the exact moment ledger [@WangHeadCounterloop2026] $$\label{eq:s-ledger}
 s_{k,n}=\sum_{\nu\in\mathcal Y_k}\nu^n
 =\beta_k^n\bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr).$$ For $2k<n<4k$ there is no multiple of $2k$. Hence odd moments vanish and, for $k+1\le m\le2k-1$, $$\label{eq:upper-even}
 s_{k,2m}=-2\beta_k^{2m},\qquad
 \frac{|s_{k,2m}|R^{2m}}{2m}=\frac{y_k^m}{m}.$$ Define the strict upper-alias counterloop budget and its normalized version by $$\label{eq:C-up}
 \mathcal C_k^{\rm up}
 =\sum_{2k<n<4k}\frac{|s_{k,n}|R^n}{n}
 =\sum_{m=k+1}^{2k-1}\frac{y_k^m}{m},
 \qquad
 \widehat{\mathcal C}_k^{\rm up}=x^{-k}\mathcal C_k^{\rm up}.$$ RH-297 computed the isolated alias impulses at multiples of $2k$. Equation [\[eq:C-up\]](#eq:C-up){reference-type="eqref" reference="eq:C-up"} instead sums every nonalias even coordinate in the strict upper band, so the result below is not a relabeling of that ledger [@WangAliasLedger2026].

# The exponential counterloop burden

[\[thm:burden\]]{#thm:burden label="thm:burden"} As $k\to\infty$, $$\begin{aligned}
 \mathcal C_k^{\rm up}
 &\sim\frac{x^{2k}}{2C_M^2k(x-1)},
 \label{eq:C-asymptotic}\\
 \widehat{\mathcal C}_k^{\rm up}
 &\sim\frac{x^k}{2C_M^2k(x-1)},
 \qquad
 \lim_{k\to\infty}
 (\widehat{\mathcal C}_k^{\rm up})^{1/k}=x>1.
 \label{eq:Chat-asymptotic}\end{aligned}$$ For the terminal coordinate, put $$\label{eq:terminal-definition}
 \mathcal T_k
 =\frac{|s_{k,4k-2}|R^{4k-2}}{4k-2}
 =\frac{y_k^{2k-1}}{2k-1}.$$ Then $$\label{eq:terminal-asymptotic}
 x^{-k}\mathcal T_k
 \sim\frac{x^{k-1}}{2C_M^2k},
 \qquad
 \frac{\mathcal T_k}{\mathcal C_k^{\rm up}}
 \longrightarrow\frac{x-1}{x}.$$

Set $m=2k-1-r$ in [\[eq:C-up\]](#eq:C-up){reference-type="eqref" reference="eq:C-up"}. Then $$\label{eq:terminal-geometric}
 \mathcal C_k^{\rm up}
 =y_k^{2k-1}\sum_{r=0}^{k-2}
 \frac{y_k^{-r}}{2k-1-r}.$$ We first prove $$\label{eq:sum-limit}
 k\sum_{r=0}^{k-2}\frac{y_k^{-r}}{2k-1-r}
 \longrightarrow\frac{x}{2(x-1)}.$$ For each fixed $r$, the summand after multiplication by $k$ tends to $x^{-r}/2$. Choose $1<\xi<x$. By $y_k\to x$, eventually $y_k\ge\xi$; also $k/(2k-1-r)\le1$ for $0\le r\le k-2$. After extending the finite sum by zero, its terms are dominated by the summable sequence $\xi^{-r}$. Dominated convergence on the counting measure gives $$\frac12\sum_{r\ge0}x^{-r}=\frac{x}{2(x-1)},$$ which is [\[eq:sum-limit\]](#eq:sum-limit){reference-type="eqref" reference="eq:sum-limit"}.

Equation [\[eq:x-y\]](#eq:x-y){reference-type="eqref" reference="eq:x-y"} also gives $$\label{eq:terminal-power}
 y_k^{2k-1}
 =x^{2k-1}C_M^{-2}\{1+o(1)\}.$$ Substitute [\[eq:sum-limit\]](#eq:sum-limit){reference-type="eqref" reference="eq:sum-limit"} and [\[eq:terminal-power\]](#eq:terminal-power){reference-type="eqref" reference="eq:terminal-power"} into [\[eq:terminal-geometric\]](#eq:terminal-geometric){reference-type="eqref" reference="eq:terminal-geometric"} to obtain [\[eq:C-asymptotic\]](#eq:C-asymptotic){reference-type="eqref" reference="eq:C-asymptotic"}. Division by $x^k$ proves the first part of [\[eq:Chat-asymptotic\]](#eq:Chat-asymptotic){reference-type="eqref" reference="eq:Chat-asymptotic"}; taking $k$th roots proves the second. Finally, divide [\[eq:terminal-power\]](#eq:terminal-power){reference-type="eqref" reference="eq:terminal-power"} by $2k-1$, normalize by $x^k$, and compare with [\[eq:C-asymptotic\]](#eq:C-asymptotic){reference-type="eqref" reference="eq:C-asymptotic"}. This gives both assertions in [\[eq:terminal-asymptotic\]](#eq:terminal-asymptotic){reference-type="eqref" reference="eq:terminal-asymptotic"}.

The theorem is unconditional for the deterministic graded counterloop. It does not yet say that an actual noisy-head budget is large or small: an actual head may match the shell by equally large complex moments.

# What the original head-transport leaf would force

Let $\mathcal H_\sigma$ be the actual modulus-complete Hardy head of RH-342 and $$\label{eq:h-d}
 h_{\sigma,n}=\sum_{\mu\in\mathcal H_\sigma}\mu^n,
 \qquad d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}.$$ Suppress $\sigma=\sigma_k$ in the budgets and define $$\begin{aligned}
 D_{4k}(R)
 &=\sum_{2\le n<4k}\frac{|d_{\sigma,k,n}|R^n}{n},
 \label{eq:D4k}\\
 \mathcal H_k^{\rm up}
 &=\sum_{2k<n<4k}\frac{|h_{\sigma,n}|R^n}{n},
 \label{eq:Hup}\\
 \mathcal H_{k,\rm odd}^{\rm up}
 &=\sum_{\substack{2k<n<4k\\ n\ \mathrm{odd}}}
 \frac{|h_{\sigma,n}|R^n}{n}.
 \label{eq:Hodd}\end{aligned}$$ The quantity [\[eq:D4k\]](#eq:D4k){reference-type="eqref" reference="eq:D4k"} is the original unnormalized, same-clock head/counterloop leaf in RH-288 and RH-340 [@WangGluing2026; @WangSynchronization2026].

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Assume, on one physical clock, that $$\label{eq:D-assumption}
 D_{4k}(R)\longrightarrow0.$$ Then $$\begin{aligned}
 \mathcal H_k^{\rm up}
 &\sim\mathcal C_k^{\rm up}
 \sim\frac{x^{2k}}{2C_M^2k(x-1)},
 \label{eq:H-asymptotic}\\
 \mathcal H_{k,\rm odd}^{\rm up}&\longrightarrow0.
 \label{eq:Hodd-zero}\end{aligned}$$ Moreover, uniformly over $k+1\le m\le2k-1$, $$\label{eq:uniform-relative}
 \max_{k+1\le m\le2k-1}
 \frac{|h_{\sigma,2m}-s_{k,2m}|}{|s_{k,2m}|}
 =o(kx^{-k}),$$ and at the terminal coordinate $$\label{eq:terminal-relative}
 \frac{|h_{\sigma,4k-2}-s_{k,4k-2}|}
 {|s_{k,4k-2}|}
 =o(kx^{-2k}).$$

The reverse triangle inequality gives $$\label{eq:budget-difference}
 |\mathcal H_k^{\rm up}-\mathcal C_k^{\rm up}|
 \le D_{4k}(R)\longrightarrow0.$$ Since [\[thm:burden\]](#thm:burden){reference-type="ref" reference="thm:burden"} gives $\mathcal C_k^{\rm up}\to\infty$, [\[eq:H-asymptotic\]](#eq:H-asymptotic){reference-type="eqref" reference="eq:H-asymptotic"} follows. Odd counterloop moments vanish in the strict upper band, so [\[eq:Hodd\]](#eq:Hodd){reference-type="eqref" reference="eq:Hodd"} is bounded by $D_{4k}(R)$, proving [\[eq:Hodd-zero\]](#eq:Hodd-zero){reference-type="eqref" reference="eq:Hodd-zero"}.

For an even upper order $n=2m$, its weighted counterloop modulus is $y_k^m/m$. Since $y_k\to x>1$, this sequence is increasing in $m\in[k+1,2k-1]$ for all sufficiently large $k$. Thus $$\begin{aligned}
 \max_{k+1\le m\le2k-1}
 \frac{|d_{\sigma,k,2m}|}{|s_{k,2m}|}
 &\le D_{4k}(R)\frac{k+1}{y_k^{k+1}},
 \label{eq:uniform-bound}\\
 \frac{|d_{\sigma,k,4k-2}|}{|s_{k,4k-2}|}
 &\le D_{4k}(R)\frac{2k-1}{y_k^{2k-1}}.
 \label{eq:terminal-bound}\end{aligned}$$ From [\[eq:x-y\]](#eq:x-y){reference-type="eqref" reference="eq:x-y"}, $$\frac{y_k^{k+1}}{x^{k+1}}\to C_M^{-1},
 \qquad
 \frac{y_k^{2k-1}}{x^{2k-1}}\to C_M^{-2}.$$ Now [\[eq:D-assumption\]](#eq:D-assumption){reference-type="eqref" reference="eq:D-assumption"} means $D_{4k}(R)=o(1)$; inserting these two limits into [\[eq:uniform-bound\]](#eq:uniform-bound){reference-type="eqref" reference="eq:uniform-bound"} and [\[eq:terminal-bound\]](#eq:terminal-bound){reference-type="eqref" reference="eq:terminal-bound"} proves [\[eq:uniform-relative\]](#eq:uniform-relative){reference-type="eqref" reference="eq:uniform-relative"} and [\[eq:terminal-relative\]](#eq:terminal-relative){reference-type="eqref" reference="eq:terminal-relative"}. Fixed powers of $x$ are absorbed into the little-$o$ notation.

Hypothesis [\[eq:D-assumption\]](#eq:D-assumption){reference-type="eqref" reference="eq:D-assumption"} is not proved in this paper or inherited from RH-342. The theorem records a necessary precision obligation for any future proof of that original leaf; it is not actual head matching.

# A normalized defect is strictly weaker

Define only the normalized strict-upper defect $$\label{eq:Delta}
 \Delta_k^{\rm up}
 =x^{-k}\sum_{2k<n<4k}
 \frac{|d_{\sigma,k,n}|R^n}{n}.$$ If $\Delta_k^{\rm up}\to0$, then the same reverse triangle inequality and [\[thm:burden\]](#thm:burden){reference-type="ref" reference="thm:burden"} give $$\label{eq:weak-aggregate}
 \frac{x^{-k}\mathcal H_k^{\rm up}}
 {\widehat{\mathcal C}_k^{\rm up}}\longrightarrow1.$$ At the terminal coordinate, [\[eq:terminal-asymptotic\]](#eq:terminal-asymptotic){reference-type="eqref" reference="eq:terminal-asymptotic"} also forces $$\label{eq:weak-terminal}
 \frac{|h_{\sigma,4k-2}-s_{k,4k-2}|}
 {|s_{k,4k-2}|}=o(kx^{-k}).$$ This weaker hypothesis does not, however, control the bottom of the upper band, where a single normalized counterloop coordinate is only of order $k^{-1}$.

[\[prop:shell\]]{#prop:shell label="prop:shell"} Let $$\label{eq:N-a}
 N_k=2k+2,\qquad
 a_k=\beta_k\left(\frac2{N_k}\right)^{1/N_k},$$ and let $\mathcal Z_k$ be the complete $N_k$th-root shell of radius $a_k$. Write $z_{k,n}=\sum_{\zeta\in\mathcal Z_k}\zeta^n$ and form the finite multiset $\mathcal H_k^\sharp=\mathcal Y_k\cup\mathcal Z_k$, with moments $h_{k,n}^\sharp=s_{k,n}+z_{k,n}$. Then $\mathcal H_k^\sharp$ is finite and conjugation closed, and throughout $2k<n<4k$ its defect is supported only at $n=N_k$. At that order, $$\label{eq:relative-one}
 |z_{k,N_k}|=|s_{k,N_k}|=2\beta_k^{N_k},
 \qquad
 \frac{|h_{k,N_k}^\sharp-s_{k,N_k}|}{|s_{k,N_k}|}=1.$$ Nevertheless, $$\begin{aligned}
 x^{-k}\sum_{2k<n<4k}
 \frac{|h_{k,n}^\sharp-s_{k,n}|R^n}{n}
 &=\frac{x^{-k}y_k^{k+1}}{k+1}
 \sim\frac{x}{C_Mk}\longrightarrow0,
 \label{eq:shell-normalized}\\
 \sum_{2\le n<4k}
 \frac{|h_{k,n}^\sharp-s_{k,n}|R^n}{n}
 &=\frac{y_k^{k+1}}{k+1}
 \sim\frac{x^{k+1}}{C_Mk}\longrightarrow\infty.
 \label{eq:shell-raw}\end{aligned}$$ Thus normalized upper-defect convergence does not imply uniform bandwise relative matching or the original unnormalized $D_{4k}(R)\to0$ leaf.

A complete $N_k$th-root shell has moment $$z_{k,n}=N_ka_k^n\mathbf 1_{N_k\mid n}.$$ Since $N_k\in(2k,4k)$ and $2N_k=4k+4$, it is the only multiple of $N_k$ in the strict upper band. Equation [\[eq:N-a\]](#eq:N-a){reference-type="eqref" reference="eq:N-a"} gives $z_{k,N_k}=2\beta_k^{N_k}$. Because $N_k$ is even and is not divisible by $2k$ for $k\ge2$, [\[eq:s-ledger\]](#eq:s-ledger){reference-type="eqref" reference="eq:s-ledger"} gives $s_{k,N_k}=-2\beta_k^{N_k}$, proving [\[eq:relative-one\]](#eq:relative-one){reference-type="eqref" reference="eq:relative-one"}. The weighted defect is $$\frac{|z_{k,N_k}|R^{N_k}}{N_k}
 =a_k^{N_k}R^{N_k}=\frac{y_k^{k+1}}{k+1}.$$ Equations [\[eq:shell-normalized\]](#eq:shell-normalized){reference-type="eqref" reference="eq:shell-normalized"} and [\[eq:shell-raw\]](#eq:shell-raw){reference-type="eqref" reference="eq:shell-raw"} now follow from $y_k^{k+1}=x^{k+1}C_M^{-1}\{1+o(1)\}$.

Because $a_k\to\beta$ and $q<\beta<1/r_H$, the added shell eventually lies inside the broad modulus window used for the Hardy head. This makes [\[prop:shell\]](#prop:shell){reference-type="ref" reference="prop:shell"} a legitimate finite normal information-class counterexample. It is not the spectrum of the actual noisy operator, does not satisfy an asserted actual rank law, and proves no actual nonmatching.

# Claim boundary and reproducibility

RH-354 controls the actual direct coefficient $$\label{eq:p-distinction}
 p_{\sigma,k,n}=\tau_{\sigma,n}-a_n
 =q_{\sigma,k,n}-d_{\sigma,k,n}.$$ Its normalized direct tail is not a theorem for $q$, $d$, or the full-trace $E_{\rm off}$ budget. Conversely, the counterloop asymptotic here does not close the direct coefficient. Transfer still requires the same-clock typed hypotheses of RH-340 and the remaining gluing leaves of RH-288 [@WangDirectTail2026; @WangSynchronization2026; @WangGluing2026].

The executable artifact verifies the exact upper-band ledger at the rational fixture $\lambda=5/3$, $C_M=1$, and evaluates the synthetic exact multiplier law $|M_k|=C_M\lambda^k$ at archived high-precision diagnostics. It checks the two asymptotic ratios, the terminal share, and the complete-shell counterexample. These finite rows reproduce formulas only. The displayed decimal for $C_M$ is not an interval certificate, and no row is an observation of the actual noisy head.

The unconditional theorem is solely about the source-locked graded counterloop. The actual-head conclusions are conditional on $D_{4k}(R)\to0$, which remains open. No root matching, rank identification, physical determinant factorization, low-prefix closure, RH-241 envelope, RH-288 activation, or Gate A--E is proved. This work constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt-weighted trace or completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
