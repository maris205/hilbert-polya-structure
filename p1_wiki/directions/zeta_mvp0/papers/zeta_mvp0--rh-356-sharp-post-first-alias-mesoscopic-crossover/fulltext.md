---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-356-sharp-post-first-alias-mesoscopic-crossover"
canonical_tex: "zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover/main.pdf"
source_sha256: "db8aa7d7ed707323e7b7deac2751f5a60ac81dbf4c29b069e516ddca1b352cb6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Sharp Post-First-Alias Mesoscopic Crossover

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-356-sharp-post-first-alias-mesoscopic-crossover/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We resolve the crossover between the first counterloop alias and the first $L$ even coordinates immediately above it. Let $y_k=(\beta_kR)^2$, $x=(\beta R)^2>1$, and define $$A_k=\frac{|s_{k,2k}|R^{2k}}{2k},\qquad
   B_k(L)=\sum_{j=1}^L
   \frac{|s_{k,2k+2j}|R^{2k+2j}}{2k+2j}.$$ The exact graded ledger gives $$A_k=(1-k^{-1})y_k^k,\qquad
   \frac{B_k(L)}{A_k}
   =\frac{k}{k-1}\sum_{j=1}^L\frac{y_k^j}{k+j}.$$ For every integer envelope $\ell_k=o(k)$, uniformly over $1\le L\le\ell_k$, $$\frac{B_k(L)}{A_k}
   =\frac{x(x^L-1)}{k(x-1)}\{1+o(1)\}.$$ The finite-radius factor $1-y_k^{-L}$ is deleted only when $L\to\infty$ as well as $L=o(k)$. In that regime the sharp transition variable is $\delta_k=L-\log_xk$: the ratio tends to zero, a finite nonzero limit, or infinity according as $\delta_k\to-\infty$, $c\in\mathbb R$, or $+\infty$. The finite limit is $x^{c+1}/(x-1)$.

  Integer depth retains a real phase. For $L_k=\lfloor\log_xk+c\rfloor$ and $\theta_k=\{\log_xk+c\}$, $$\frac{B_k(L_k)}{A_k}
   =\frac{x^{c+1-\theta_k}}{x-1}\{1+o(1)\}.$$ The phase limit set is $[0,1]$, so the ratio has no single limit; its liminf and limsup are $x^c/(x-1)$ and $x^{c+1}/(x-1)$. On the physical noise clock the crossover lies only $2L=(2/\log x)\log\log(1/\sigma)+O(1)$ orders above the first alias. Actual-head statements remain conditional on the original unnormalized same-clock hypothesis $D_{4k}(R)\to0$, which is not proved. Linear depth, direct/full-trace transfer, RH-288, Gates A--E, Hilbert--Polya, zero identification, and RH remain open.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Sharp Post-First-Alias\
  Mesoscopic Crossover
```

## Markdown 正文

# Exact first-alias and post-alias ledgers

Fix the physical constants $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10}.$$ On the physical first-alias clock $k=k_\sigma\to\infty$, RH-17 proves $$\label{eq:multiplier}
 |M_k|=C_M\lambda^k\{1+o(1)\},\qquad C_M>0.$$ Put $$\label{eq:beta}
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},\qquad
 \beta=\frac1{r_H\sqrt\lambda},$$ and $$\label{eq:x-y}
 x=(\beta R)^2=\frac{(R/r_H)^2}{\lambda}>1,
 \qquad
 y_k=(\beta_kR)^2
 =x\exp\left[-\frac{\log C_M}{k}+o(k^{-1})\right].$$ These are the multiplier and Hardy-normalization locks used in RH-355 [@WangTimeOrdered2026; @WangProjectorMass2026; @WangUpperBurden2026].

The finite graded counterloop is $$\label{eq:Y}
 \mathcal Y_k=\{\beta_ke^{ij\pi/k},\beta_ke^{-ij\pi/k}:1\le j\le k-1\}.$$ Its exact power ledger is $$\label{eq:s-ledger}
 s_{k,n}=\sum_{\nu\in\mathcal Y_k}\nu^n
 =\beta_k^n\bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr)$$ [@WangAliasLedger2026; @WangHeadCounterloop2026]. Thus the first alias at $n=2k$ has weighted modulus $$\label{eq:A}
 A_k:=\frac{|s_{k,2k}|R^{2k}}{2k}
 =\left(1-\frac1k\right)y_k^k.$$ For an integer depth $$\label{eq:L-domain}
 1\le L\le k-1,$$ define the even post-first-alias budget through $n=2k+2L$ by $$\label{eq:B}
 B_k(L):=\sum_{j=1}^L
 \frac{|s_{k,2k+2j}|R^{2k+2j}}{2k+2j}
 =\sum_{j=1}^L\frac{y_k^{k+j}}{k+j}.$$ The upper limit in [\[eq:L-domain\]](#eq:L-domain){reference-type="eqref" reference="eq:L-domain"} keeps every order strictly below the second alias $4k$. Odd counterloop moments in this band vanish.

[\[prop:exact-ratio\]]{#prop:exact-ratio label="prop:exact-ratio"} For every finite $k\ge2$ and every depth in [\[eq:L-domain\]](#eq:L-domain){reference-type="eqref" reference="eq:L-domain"}, $$\label{eq:exact-ratio}
 \boxed{
 \frac{B_k(L)}{A_k}
 =\frac{k}{k-1}\sum_{j=1}^L\frac{y_k^j}{k+j}.}$$

In the strict upper band, [\[eq:s-ledger\]](#eq:s-ledger){reference-type="eqref" reference="eq:s-ledger"} gives $s_{k,2k+2j}=-2\beta_k^{2k+2j}$. Hence the displayed summands in [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} are exact. Divide their sum by [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"}.

The common factor $y_k^k$ cancels exactly in [\[eq:exact-ratio\]](#eq:exact-ratio){reference-type="eqref" reference="eq:exact-ratio"}. The remaining finite-radius drift is carried by $y_k^j$ and is negligible precisely when the post-alias depth is sublinear.

# Uniform mesoscopic law

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} Let $\ell_k$ be any positive integer sequence with $\ell_k=o(k)$. Then $$\label{eq:uniform-sup}
 \sup_{1\le L\le\ell_k}
 \left|
 \frac{B_k(L)/A_k}
 {x(x^L-1)/\{k(x-1)\}}-1
 \right|\longrightarrow0.$$ Equivalently, uniformly on that domain, $$\label{eq:uniform-law}
 \boxed{
 \frac{B_k(L)}{A_k}
 =\frac{x(x^L-1)}{k(x-1)}\{1+o(1)\}.}$$ The constant $C_M$ does not occur in the mesoscopic leading term.

Write $$\label{eq:epsilon}
 \varepsilon_k=\log(y_k/x)
 =-\frac{\log C_M}{k}+o(k^{-1}).$$ Since $\ell_k=o(k)$, $$\label{eq:y-x-uniform}
 \sup_{1\le j\le\ell_k}
 \left|\frac{y_k^j}{x^j}-1\right|
 =\sup_{1\le j\le\ell_k}|e^{j\varepsilon_k}-1|
 \longrightarrow0.$$ Also $$\label{eq:denominator-uniform}
 \sup_{1\le j\le\ell_k}
 \left|\frac{k^2}{(k-1)(k+j)}-1\right|
 \longrightarrow0.$$ All summands are positive. Therefore [\[eq:exact-ratio\]](#eq:exact-ratio){reference-type="eqref" reference="eq:exact-ratio"}, [\[eq:y-x-uniform\]](#eq:y-x-uniform){reference-type="eqref" reference="eq:y-x-uniform"}, and [\[eq:denominator-uniform\]](#eq:denominator-uniform){reference-type="eqref" reference="eq:denominator-uniform"} show, uniformly in $L$, that $$\begin{aligned}
 \frac{B_k(L)}{A_k}
 &=\frac{y_k(y_k^L-1)}{k(y_k-1)}\{1+o(1)\}
 \label{eq:y-geometric}\\
 &=\frac{y_k^{L+1}}{k(y_k-1)}
   (1-y_k^{-L})\{1+o(1)\}
 \label{eq:y-minus-one}\\
 &=\frac{1+o(1)}{k}\sum_{j=1}^Lx^j
 =\frac{x(x^L-1)}{k(x-1)}\{1+o(1)\}.\end{aligned}$$ This proves [\[eq:uniform-sup\]](#eq:uniform-sup){reference-type="eqref" reference="eq:uniform-sup"}. The cancellation of $C_M$ follows from [\[eq:y-x-uniform\]](#eq:y-x-uniform){reference-type="eqref" reference="eq:y-x-uniform"}; no numerical value of $C_M$ is used.

The geometric subtraction in [\[eq:uniform-law\]](#eq:uniform-law){reference-type="eqref" reference="eq:uniform-law"} must be retained at bounded depth.

[\[cor:fixed-growing\]]{#cor:fixed-growing label="cor:fixed-growing"} For every fixed integer $L\ge1$, $$\label{eq:fixed-L}
 k\frac{B_k(L)}{A_k}
 \longrightarrow\frac{x(x^L-1)}{x-1}.$$ If instead $$\label{eq:growing-L}
 L\longrightarrow\infty,
 \qquad L=o(k),$$ then and only at this quantified simplification step, $$\label{eq:master}
 \boxed{
 \frac{B_k(L)}{A_k}
 =\frac{x}{x-1}\,x^{L-\log_xk}\{1+o(1)\}.}$$

Equation [\[eq:fixed-L\]](#eq:fixed-L){reference-type="eqref" reference="eq:fixed-L"} is the fixed-depth specialization of [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"}. Under [\[eq:growing-L\]](#eq:growing-L){reference-type="eqref" reference="eq:growing-L"}, $y_k$ is eventually bounded below by a fixed number greater than one, so $y_k^{-L}\to0$. Thus and only under this additional $L\to\infty$ quantifier may the factor $1-y_k^{-L}$ in [\[eq:y-minus-one\]](#eq:y-minus-one){reference-type="eqref" reference="eq:y-minus-one"} be deleted. Equivalently, $x^L-1=x^L(1-x^{-L})=x^L\{1+o(1)\}$; substitution in [\[eq:uniform-law\]](#eq:uniform-law){reference-type="eqref" reference="eq:uniform-law"} gives [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"}.

In particular, deleting $1-y_k^{-L}$ (or its limiting counterpart $1-x^{-L}$) at fixed $L$ would change the leading constant. No finite table or informal use of "mesoscopic" licenses that deletion.

# The crossover and its integer phase

[\[thm:crossover\]]{#thm:crossover label="thm:crossover"} Let $1\le L\le\ell_k$ for some $\ell_k=o(k)$, and put $$\label{eq:delta}
 \delta_k=L-\log_xk.$$ Then:

1.  if $\delta_k\to-\infty$, then $B_k(L)/A_k\to0$;

2.  if $\delta_k\to c\in\mathbb R$, then $$\label{eq:finite-crossover}
      \frac{B_k(L)}{A_k}\longrightarrow
      \frac{x^{c+1}}{x-1};$$

3.  if $\delta_k\to+\infty$, then $B_k(L)/A_k\to\infty$.

The continuous balance offset is $$\label{eq:balance-offset}
 L=\log_xk+\log_x\left(\frac{x-1}{x}\right)+o(1).$$

In the first case, [\[eq:uniform-law\]](#eq:uniform-law){reference-type="eqref" reference="eq:uniform-law"} and $x^L-1\le x^L$ give $$0\le\frac{B_k(L)}{A_k}
 \le\frac{x}{x-1}x^{\delta_k}\{1+o(1)\}\longrightarrow0.$$ In the finite and supercritical cases, $L\to\infty$ automatically, so [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"} applies and gives the asserted limits. Setting the finite limit equal to one yields [\[eq:balance-offset\]](#eq:balance-offset){reference-type="eqref" reference="eq:balance-offset"}.

Because the depth is integer, a fixed offset does not normally produce a single limit.

[\[thm:integer-phase\]]{#thm:integer-phase label="thm:integer-phase"} Fix $c\in\mathbb R$ and define $$\label{eq:floor-phase}
 L_k(c)=\lfloor\log_xk+c\rfloor,
 \qquad
 \theta_k(c)=\{\log_xk+c\}.$$ Then $$\label{eq:phase-law}
 \boxed{
 \frac{B_k(L_k(c))}{A_k}
 =\frac{x^{c+1-\theta_k(c)}}{x-1}\{1+o(1)\}.}$$ The limit set of $\theta_k(c)$ is the closed interval $[0,1]$. Hence $$\begin{aligned}
 \liminf_{k\to\infty}\frac{B_k(L_k(c))}{A_k}
 &=\frac{x^c}{x-1},
 \label{eq:liminf}\\
 \limsup_{k\to\infty}\frac{B_k(L_k(c))}{A_k}
 &=\frac{x^{c+1}}{x-1}.
 \label{eq:limsup}\end{aligned}$$ In particular, the full sequence has no single limit.

Here $L_k(c)\sim\log_xk$, so $L_k(c)\to\infty$ and $L_k(c)=o(k)$. Moreover $L_k(c)-\log_xk=c-\theta_k(c)$. Equation [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"} follows from [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"}.

For $t\in(0,1)$, take $k_m=\lfloor x^{m+t-c}\rfloor$. Then $\log_xk_m+c=m+t+o(1)$, so a subsequence of phases tends to $t$. For the endpoints, the choices $$\label{eq:phase-endpoint-subsequences}
 k_m^{(0)}=\left\lceil x^{m-c}\right\rceil,
 \qquad
 k_m^{(1)}=\left\lceil x^{m+1-c}\right\rceil-1$$ give phases tending to zero and one, respectively. The second formula also handles the case in which $x^{m+1-c}$ is an integer: subtracting one keeps the logarithm just below the next integer. Thus the complete phase limit set is $[0,1]$. Apply the continuous decreasing function $t\mapsto x^{c+1-t}/(x-1)$ to obtain [\[eq:liminf\]](#eq:liminf){reference-type="eqref" reference="eq:liminf"} and [\[eq:limsup\]](#eq:limsup){reference-type="eqref" reference="eq:limsup"}. Since $x>1$, the endpoints differ.

On the physical clock $$\label{eq:physical-clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1).$$ Therefore every bounded crossover window $L=\log_xk+O(1)$ lies at the order displacement $$\label{eq:physical-depth}
 n-2k=2L
 =\frac{2}{\log x}\log\log(1/\sigma)+O(1).$$ This is a post-first-alias mesoscopic scale: it diverges, but is $o(k)$.

# Conditional actual-head transfer

Let $\mathcal H_\sigma$ be the actual modulus-complete Hardy head of RH-342, with moments $h_{\sigma,n}$, and set $$\label{eq:defect}
 d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}.$$ The original same-clock unnormalized transport leaf is $$\label{eq:D4k}
 D_{4k}(R)=\sum_{2\le n<4k}
 \frac{|d_{\sigma,k,n}|R^n}{n}\longrightarrow0$$ [@WangGluing2026; @WangSynchronization2026]. It is an open hypothesis, not a result of this paper.

Define the actual first-alias and even post-alias budgets $$\begin{aligned}
 A_k^{\mathcal H}
 &=\frac{|h_{\sigma,2k}|R^{2k}}{2k},
 \label{eq:AH}\\
 B_k^{\mathcal H}(L)
 &=\sum_{j=1}^L
 \frac{|h_{\sigma,2k+2j}|R^{2k+2j}}{2k+2j},
 \label{eq:BH}\end{aligned}$$ and let $O_k^{\mathcal H}(L)$ be the corresponding weighted sum over odd orders strictly between $2k$ and $2k+2L$.

[\[thm:actual-conditional\]]{#thm:actual-conditional label="thm:actual-conditional"} Assume [\[eq:D4k\]](#eq:D4k){reference-type="eqref" reference="eq:D4k"} on one physical clock. Then $$\label{eq:actual-alias}
 \frac{A_k^{\mathcal H}}{A_k}\longrightarrow1,
 \qquad
 \sup_{1\le L\le k-1}
 \left|\frac{B_k^{\mathcal H}(L)}{B_k(L)}-1\right|
 \longrightarrow0,$$ and $$\label{eq:actual-odd}
 \sup_{1\le L\le k-1}O_k^{\mathcal H}(L)\longrightarrow0.$$ Consequently every mesoscopic conclusion of [\[thm:uniform,thm:crossover,thm:integer-phase\]](#thm:uniform,thm:crossover,thm:integer-phase){reference-type="ref" reference="thm:uniform,thm:crossover,thm:integer-phase"} transfers to $B_k^{\mathcal H}(L)/A_k^{\mathcal H}$ under this hypothesis.

The reverse triangle inequality gives $$\label{eq:actual-differences}
 |A_k^{\mathcal H}-A_k|\le D_{4k}(R),
 \qquad
 |B_k^{\mathcal H}(L)-B_k(L)|\le D_{4k}(R).$$ Now $A_k\sim C_M^{-1}x^k\to\infty$, while uniformly in $L\ge1$, $$B_k(L)\ge B_k(1)
 =\frac{y_k^{k+1}}{k+1}
 \sim\frac{x^{k+1}}{C_Mk}\longrightarrow\infty.$$ Divide [\[eq:actual-differences\]](#eq:actual-differences){reference-type="eqref" reference="eq:actual-differences"} by these lower bounds and use $D_{4k}(R)=o(1)$. Odd counterloop moments vanish, so every $O_k^{\mathcal H}(L)$ is bounded by $D_{4k}(R)$. Finally divide the two actual budget asymptotics to transfer the ratios.

This theorem is conditional only. It identifies neither the actual head rank nor its roots with the counterloop and does not prove [\[eq:D4k\]](#eq:D4k){reference-type="eqref" reference="eq:D4k"}.

# Boundary and reproducibility

The condition $L=o(k)$ is structural. At a linear depth $L\sim\alpha k$, the two uniform replacements used in [\[eq:y-x-uniform\]](#eq:y-x-uniform){reference-type="eqref" reference="eq:y-x-uniform"} and [\[eq:denominator-uniform\]](#eq:denominator-uniform){reference-type="eqref" reference="eq:denominator-uniform"} fail: $y_k^L/x^L$ can retain a $C_M^{-\alpha}$ factor, and $(k+j)^{-1}$ is not uniformly $k^{-1}$. No linear-depth extension is claimed. The exact ratio [\[eq:exact-ratio\]](#eq:exact-ratio){reference-type="eqref" reference="eq:exact-ratio"} does, however, leave a source-backed next problem: for $L/k\to\alpha\in(0,1]$, endpoint geometric domination should be audited with the new factors $C_M^{-\alpha}$ and $(1+\alpha)^{-1}$. This separate profile is not proved here.

RH-354 controls the direct coefficient $$\label{eq:p-distinction}
 p_{\sigma,k,n}=\tau_{\sigma,n}-a_n
 =q_{\sigma,k,n}-d_{\sigma,k,n}.$$ Neither the unconditional counterloop crossover nor the conditional head statement proves a theorem for $p$, $q$, or the full-trace $E_{\rm off}$ budget [@WangDirectTail2026]. The remaining typed gluing hypotheses are still required.

The executable artifact checks the exact rational ledger at $\lambda=5/3$, $C_M=1$, the full geometric factor $x^L-1$, and synthetic finite-radius phase rows at archived high-precision diagnostics. The finite ratio itself is not required to lie inside its limiting phase cluster at any prescribed $k$; only convergence to the phase law is tested. The decimals are not interval certificates, actual noisy-head observations, or asymptotic evidence.

RH-356 proves an unconditional mesoscopic crossover only for the graded counterloop and a conditional transfer statement for the actual head. It does not prove $D_{4k}(R)\to0$, root or rank matching, a linear-depth law, direct/full-trace closure, the RH-241 moving noisy envelope, or RH-288 activation. Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace, completed-zeta divisor equality, or proof of the Riemann Hypothesis is claimed.
