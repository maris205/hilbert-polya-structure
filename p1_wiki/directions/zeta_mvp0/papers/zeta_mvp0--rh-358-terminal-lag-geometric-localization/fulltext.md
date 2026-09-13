---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-358-terminal-lag-geometric-localization"
canonical_tex: "zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization/main.pdf"
source_sha256: "8240d00859b7e8271f767801ccb67b73b464c1448930c434da44ad75a403bff3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Terminal-Lag Geometric Localization for the Complete Upper Counterloop Band

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-358-terminal-lag-geometric-localization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We resolve how the complete deterministic upper-counterloop budget is distributed relative to its terminal order. Let $y_k=(\beta_kR)^2$, $x=(\beta R)^2>1$, and $y_k=x\exp[-\log C_M/k+o(k^{-1})]$. For $$B_k(L)=\sum_{j=1}^{L}\frac{y_k^{k+j}}{k+j},\qquad
   C_k=B_k(k-1),\qquad P_k(q)=B_k(k-1-q),$$ where $0\le q\le k-2$, we prove uniformly in $q$ that $$\frac{P_k(q)}{C_k}
   =x^{-q}C_M^{q/k}\frac{2k-1}{2k-1-q}
   \frac{1-x^{-(k-1-q)}}{1-x^{-(k-1)}}(1+o(1)).$$ The corresponding exact terminal-lag probability has weights proportional to $y_k^{-r}/(2k-1-r)$, $0\le r\le k-2$. Extended by zero to the nonnegative integers, it converges in $\ell^1$ to $(1-x^{-1})x^{-r}$, and its mean and variance converge to $1/(x-1)$ and $x/(x-1)^2$. Thus a fixed terminal window of width $q$ retains mass $1-x^{-q}$, and vanishing relative truncation error occurs exactly when $q\to\infty$. We also separate the sublinear, linear, and fixed residual-depth regimes. Actual-head inheritance is stated only conditionally on the original unnormalized same-clock leaf $D_{4k}(R)\to0$. No root or rank identification, determinant closure, Gate A--E promotion, Hilbert--Polya construction, zero identification, or proof of RH is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Terminal-Lag Geometric Localization\
  for the Complete Upper Counterloop Band
```

## Markdown 正文

# Source-locked terminal ledger

Fix the physical constants $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10}.$$ Let $k=k_\sigma\to\infty$ be the first-alias clock used in RH-342. The boundary multiplier and Hardy normalization are $$\begin{aligned}
 |M_k|&=C_M\lambda^k\{1+o(1)\},\qquad C_M>0,\label{eq:multiplier}\\
 \beta_k&=\frac{|M_k|^{-1/(2k)}}{r_H},
 &\beta&=\frac1{r_H\sqrt\lambda}.\end{aligned}$$ Consequently $$\label{eq:x-y}
 x=(\beta R)^2=\frac{(R/r_H)^2}{\lambda}>1,
 \qquad
 y_k=(\beta_kR)^2
 =x\exp\left[-\frac{\log C_M}{k}+o(k^{-1})\right].$$ These facts are the source locks from RH-17 and RH-342 [@WangTimeOrdered2026; @WangHeadCounterloop2026].

The deterministic graded counterloop is $$\label{eq:Y}
 \mathcal Y_k=
 \{\beta_ke^{ij\pi/k},\beta_ke^{-ij\pi/k}:1\le j\le k-1\},$$ with exact power ledger $$\label{eq:s-ledger}
 s_{k,n}=\sum_{\nu\in\mathcal Y_k}\nu^n
 =\beta_k^n\bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr).$$ The even strict upper band $2k<n<4k$ therefore has budget $$\label{eq:B}
 B_k(L):=\sum_{j=1}^{L}
 \frac{|s_{k,2k+2j}|R^{2k+2j}}{2k+2j}
 =\sum_{j=1}^{L}\frac{y_k^{k+j}}{k+j},
 \qquad 1\le L\le k-1.$$ This is the deterministic ledger isolated in RH-355--RH-357 [@WangUpperBurden2026; @WangMesoscopic2026; @WangLinearDepth2026].

Define the complete strict upper budget and its lower residual after removing the top $q$ terminal coordinates by $$\label{eq:C-P}
 C_k:=B_k(k-1),\qquad
 P_k(q):=B_k(k-1-q),\qquad 0\le q\le k-2.$$ The symbol $q$ in this paper is only an integer terminal lag. It is not the open direct/full-trace quantity denoted by the same letter in other project ledgers.

[\[prop:exact\]]{#prop:exact label="prop:exact"} For $0\le r\le k-2$, put $$\label{eq:pi}
 \pi_k(r):=
 \frac{y_k^{2k-1-r}/(2k-1-r)}{C_k},$$ and set $\pi_k(r)=0$ for $r\ge k-1$. Then $\pi_k$ is a probability on $\mathbb Z_{\ge0}$ and, for every $0\le q\le k-2$, $$\label{eq:tail-identity}
 \boxed{\frac{P_k(q)}{C_k}=\sum_{r=q}^{k-2}\pi_k(r).}$$

In [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"}, substitute $r=k-1-j$. The full range $1\le j\le k-1$ becomes $0\le r\le k-2$, and $$C_k=\sum_{r=0}^{k-2}\frac{y_k^{2k-1-r}}{2k-1-r}.$$ The partial range $1\le j\le k-1-q$ becomes $q\le r\le k-2$. Normalization gives both assertions.

# Uniform finite-tail profile

We first record the endpoint estimate in the form needed below.

[\[lem:endpoint\]]{#lem:endpoint label="lem:endpoint"} Uniformly for $1\le L\le k-1$, $$\label{eq:endpoint}
 B_k(L)=\frac{y_k^{k+L+1}(1-y_k^{-L})}
 {(k+L)(y_k-1)}\left(1+O(k^{-1})\right).$$

Reverse the sum in [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"}: $$B_k(L)=\frac{y_k^{k+L}}{k+L}
 \sum_{r=0}^{L-1}y_k^{-r}\frac{k+L}{k+L-r}.$$ Choose $1<\xi<x$ with $y_k\ge\xi$ eventually. Since $k+L-r\ge k+1$, $$0\le \sum_{r=0}^{L-1}y_k^{-r}
 \left(\frac{k+L}{k+L-r}-1\right)
 \le \frac1{k+1}\sum_{r\ge0}r\xi^{-r}=O(k^{-1}).$$ The unweighted geometric sum is at least one and equals $y_k(1-y_k^{-L})/(y_k-1)$. This proves the relative estimate uniformly in $L$.

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} Assume [\[eq:x-y\]](#eq:x-y){reference-type="eqref" reference="eq:x-y"}. Uniformly over all integers $0\le q\le k-2$, $$\begin{aligned}
 \frac{P_k(q)}{C_k}
 &=y_k^{-q}\frac{2k-1}{2k-1-q}
 \frac{1-y_k^{-(k-1-q)}}{1-y_k^{-(k-1)}}
 \left(1+O(k^{-1})\right),\label{eq:y-profile}\\
 &=x^{-q}C_M^{q/k}\frac{2k-1}{2k-1-q}
 \frac{1-x^{-(k-1-q)}}{1-x^{-(k-1)}}
 (1+o(1)).\label{eq:x-profile}\end{aligned}$$ Both errors are relative and uniform in $q$. In particular, the factor $x^{-q}$ alone is not a uniform asymptotic over the full range.

Apply [\[lem:endpoint\]](#lem:endpoint){reference-type="ref" reference="lem:endpoint"} first with $L=k-1-q$ and then with $L=k-1$. Taking the ratio gives [\[eq:y-profile\]](#eq:y-profile){reference-type="eqref" reference="eq:y-profile"}, because the quotient of two uniform factors $1+O(k^{-1})$ is again $1+O(k^{-1})$.

For the source-locked replacement, define $$\rho_k:=k\log(y_k/x)+\log C_M\longrightarrow0.$$ Then, uniformly for $0\le q\le k-2$, $$\label{eq:power-replacement}
 y_k^{-q}=x^{-q}C_M^{q/k}
 \exp\left(-\frac{q}{k}\rho_k\right)
 =x^{-q}C_M^{q/k}(1+o(1)).$$ It remains to replace the finite-tail factors. For $m\ge1$, let $F_m(t)=1-t^{-m}$. On $t\ge\xi$, $$|F_m'(t)|=m t^{-m-1}\le\sup_{j\ge1}j\xi^{-j-1}<\infty,
 \qquad F_m(x)\ge1-x^{-1}>0.$$ The mean-value theorem therefore gives $F_m(y_k)/F_m(x)\to1$ uniformly in $m\ge1$. Apply this with $m=k-1-q$ and $m=k-1$ and combine with [\[eq:power-replacement\]](#eq:power-replacement){reference-type="eqref" reference="eq:power-replacement"}.

# Three lag regimes and the truncation criterion

[\[cor:regimes\]]{#cor:regimes label="cor:regimes"} Let $q=q_k$ be admissible.

1.  If $q=o(k)$ (hence $k-q\to\infty$), then $$\label{eq:sublinear}
     \frac{P_k(q)}{C_k}=x^{-q}(1+o(1)).$$ In particular, for fixed $q$, $P_k(q)/C_k\to x^{-q}$.

2.  If $q/k\to\theta\in[0,1)$, then $$\label{eq:linear}
     \frac{P_k(q)}{C_k}
     \sim \frac{2C_M^\theta}{2-\theta}\,x^{-q}.$$

3.  If $q=k-1-\ell$ with a fixed integer $\ell\ge1$, then $$\label{eq:residual}
     \frac{P_k(k-1-\ell)}{C_k}
     \sim 2C_Mx^{-(k-1-\ell)}(1-x^{-\ell}).$$

Each statement follows by taking limits in [\[eq:x-profile\]](#eq:x-profile){reference-type="eqref" reference="eq:x-profile"}. In the first case, $C_M^{q/k}\to1$, $(2k-1)/(2k-1-q)\to1$, and the finite-tail ratio tends to one. In the second case these factors tend to $C_M^\theta$, $2/(2-\theta)$, and one. In the third case $k-1-q=\ell$, while $q/k\to1$ and $(2k-1)/(2k-1-q)=(2k-1)/(k+\ell)\to2$.

The top terminal window of width $q$ has normalized retained mass $$\label{eq:retained}
 T_k(q):=\sum_{r=0}^{q-1}\pi_k(r)
 =1-\frac{P_k(q)}{C_k},$$ where $T_k(0)=0$. Thus a fixed window has $T_k(q)\to1-x^{-q}$, not one.

[\[prop:criterion\]]{#prop:criterion label="prop:criterion"} For any admissible integer sequence $0\le q_k\le k-2$, $$\label{eq:iff}
 \frac{P_k(q_k)}{C_k}\longrightarrow0
 \quad\Longleftrightarrow\quad q_k\longrightarrow\infty.$$ Equivalently, the terminal retained mass tends to one exactly for diverging window width.

The explicit factors in [\[eq:x-profile\]](#eq:x-profile){reference-type="eqref" reference="eq:x-profile"} are uniformly bounded apart from $x^{-q}$: $C_M^{q/k}$ stays in a fixed compact positive interval, $(2k-1)/(2k-1-q)<2$, and the finite-tail quotient is bounded because its denominator tends to one. Hence $P_k(q)/C_k\le Kx^{-q}$ for all large $k$ and all admissible $q$, proving sufficiency.

If $q_k$ does not tend to infinity, it has a subsequence bounded by a fixed integer. A further subsequence is constant, say $q_k=q_0$. The fixed-lag case of [\[eq:sublinear\]](#eq:sublinear){reference-type="eqref" reference="eq:sublinear"} then gives the positive limit $x^{-q_0}$, so the tail cannot tend to zero.

# Geometric localization in total variation

[\[thm:geometric\]]{#thm:geometric label="thm:geometric"} Extend $\pi_k$ by zero to all $r\in\mathbb Z_{\ge0}$ and define $$\label{eq:geometric}
 \pi(r):=(1-x^{-1})x^{-r},\qquad r\ge0.$$ Then $$\label{eq:l1}
 \|\pi_k-\pi\|_{\ell^1(\mathbb Z_{\ge0})}\longrightarrow0,
 \qquad d_{\rm TV}(\pi_k,\pi)\longrightarrow0.$$ Moreover, $$\label{eq:moments}
 \mathbb E_{\pi_k}r\longrightarrow\frac1{x-1},
 \qquad
 \operatorname{Var}_{\pi_k}(r)\longrightarrow\frac{x}{(x-1)^2}.$$

Multiplying numerator and denominator in [\[eq:pi\]](#eq:pi){reference-type="eqref" reference="eq:pi"} by $(2k-1)y_k^{-(2k-1)}$ gives $$\label{eq:a}
 \pi_k(r)=\frac{a_{k,r}}{A_k^*},\qquad
 a_{k,r}:=\mathbf 1_{0\le r\le k-2}
 y_k^{-r}\frac{2k-1}{2k-1-r},
 \qquad A_k^*:=\sum_{s\ge0}a_{k,s}.$$ For each fixed $r$, $a_{k,r}\to x^{-r}$. Choose $1<\xi<x$ with $y_k\ge\xi$ eventually. Since $0\le r\le k-2$ implies $(2k-1)/(2k-1-r)<2$, $$\label{eq:domination}
 0\le r^m a_{k,r}\le2r^m\xi^{-r},
 \qquad m=0,1,2.$$ The right-hand sequences are summable. Dominated convergence on the counting measure therefore gives, for $m=0,1,2$, $$\label{eq:weighted-convergence}
 \sum_{r\ge0}r^m a_{k,r}\longrightarrow
 \sum_{r\ge0}r^m x^{-r}.$$ For $m=0$, $A_k^*\to(1-x^{-1})^{-1}$; dominated convergence also yields $\sum_r|a_{k,r}-x^{-r}|\to0$. Normalizing proves the $\ell^1$ assertion, and $d_{\rm TV}=\frac12\|\cdot\|_1$.

The cases $m=1,2$ in [\[eq:weighted-convergence\]](#eq:weighted-convergence){reference-type="eqref" reference="eq:weighted-convergence"}, divided by $A_k^*$, give convergence of the first two moments. For a geometric law with ratio $t=x^{-1}$, the mean is $t/(1-t)=1/(x-1)$ and the variance is $t/(1-t)^2=x/(x-1)^2$, proving [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"}.

The theorem localizes deterministic weighted trace mass near the terminal coordinate. It does not turn $\pi_k$ into an eigenvalue distribution, a root counting measure, or a probability law for noisy dynamics.

# Conditional actual-head inheritance

Let $\mathcal H_\sigma$ be the actual modulus-complete Hardy head of RH-342, with moments $h_{\sigma,n}$, and put $d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}$. The original unnormalized same-clock transport leaf is $$\label{eq:D}
 D_{4k}(R):=\sum_{2\le n<4k}
 \frac{|d_{\sigma,k,n}|R^n}{n}\longrightarrow0.$$ It is an open hypothesis, not a conclusion of this paper. For $0\le r\le k-2$, define $$\label{eq:actual-weight}
 w_{k,r}^{\mathcal H}:=
 \frac{|h_{\sigma,4k-2-2r}|R^{4k-2-2r}}{4k-2-2r},
 \quad
 C_k^{\mathcal H}:=\sum_{r=0}^{k-2}w_{k,r}^{\mathcal H},
 \quad
 P_k^{\mathcal H}(q):=\sum_{r=q}^{k-2}w_{k,r}^{\mathcal H}.$$ When $C_k^{\mathcal H}>0$, let $\pi_k^{\mathcal H}(r)=w_{k,r}^{\mathcal H}/C_k^{\mathcal H}$ on this range and set it to zero for $r\ge k-1$.

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Assume [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} on one physical clock. Then, eventually, $C_k^{\mathcal H}>0$ and $$\begin{aligned}
 \frac{C_k^{\mathcal H}}{C_k}&\longrightarrow1,\label{eq:C-inherit}\\
 \sup_{0\le q\le k-2}
 \left|
 \frac{P_k^{\mathcal H}(q)/C_k^{\mathcal H}}{P_k(q)/C_k}-1
 \right|&\longrightarrow0,\label{eq:tail-inherit}\\
 \sup_{0\le r\le k-2}
 \left|\frac{\pi_k^{\mathcal H}(r)}{\pi_k(r)}-1\right|
 &\longrightarrow0,\label{eq:pointwise-inherit}\\
 \sum_{r\ge0}r^m|\pi_k^{\mathcal H}(r)-\pi_k(r)|
 &\longrightarrow0,\qquad m=0,1,2.\label{eq:moment-inherit}\end{aligned}$$ Consequently the actual even-weight terminal distribution inherits the total-variation and first-two-moment conclusions of [\[thm:geometric\]](#thm:geometric){reference-type="ref" reference="thm:geometric"} only under [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}.

The reverse triangle inequality and the fact that every displayed order is below $4k$ give $$\label{eq:l1-transfer}
 \sum_{r=0}^{k-2}
 \left|w_{k,r}^{\mathcal H}-\frac{y_k^{2k-1-r}}{2k-1-r}\right|
 \le D_{4k}(R).$$ Therefore $|C_k^{\mathcal H}-C_k|\le D_{4k}(R)$ and, uniformly in $q$, $|P_k^{\mathcal H}(q)-P_k(q)|\le D_{4k}(R)$. Now $C_k\to\infty$, and the smallest partial budget is $$P_k(k-2)=B_k(1)=\frac{y_k^{k+1}}{k+1}\longrightarrow\infty.$$ Thus both full and partial budgets have uniform relative error tending to zero, which proves [\[eq:C-inherit\]](#eq:C-inherit){reference-type="eqref" reference="eq:C-inherit"}--[\[eq:tail-inherit\]](#eq:tail-inherit){reference-type="eqref" reference="eq:tail-inherit"}.

The same hypothesis gives a stronger coordinatewise statement. Every deterministic weight obeys $$\frac{y_k^{2k-1-r}}{2k-1-r}
 \ge \frac{y_k^{k+1}}{2k-1},
 \qquad 0\le r\le k-2,$$ and each summand difference in [\[eq:l1-transfer\]](#eq:l1-transfer){reference-type="eqref" reference="eq:l1-transfer"} is at most $D_{4k}(R)$. Hence $$\sup_{0\le r\le k-2}
 \left|
 \frac{w_{k,r}^{\mathcal H}}{y_k^{2k-1-r}/(2k-1-r)}-1
 \right|
 \le \frac{(2k-1)D_{4k}(R)}{y_k^{k+1}}\longrightarrow0.$$ Together with [\[eq:C-inherit\]](#eq:C-inherit){reference-type="eqref" reference="eq:C-inherit"}, normalization proves [\[eq:pointwise-inherit\]](#eq:pointwise-inherit){reference-type="eqref" reference="eq:pointwise-inherit"}. The domination argument in [\[eq:domination\]](#eq:domination){reference-type="eqref" reference="eq:domination"}--[\[eq:weighted-convergence\]](#eq:weighted-convergence){reference-type="eqref" reference="eq:weighted-convergence"} shows that $\sum_r r^m\pi_k(r)$ is uniformly bounded for $m=0,1,2$. Multiplying this bound by the supremum in [\[eq:pointwise-inherit\]](#eq:pointwise-inherit){reference-type="eqref" reference="eq:pointwise-inherit"} proves [\[eq:moment-inherit\]](#eq:moment-inherit){reference-type="eqref" reference="eq:moment-inherit"}. The case $m=0$ is the $\ell^1$ conclusion and hence the total-variation conclusion; $m=1,2$ transfer the mean and variance. No root, rank, or determinant information is transferred by this argument.

# Finite protocol, scope, and next route

The artifact uses the exact rational fixture $\lambda=5/3$, $C_M=1$, hence $x=2352/1445$, to check the exact tail identity, the full uniform error envelope, and finite-support probability normalization. A separate high-precision synthetic multiplier law uses the repository diagnostic values of $\lambda$ and $C_M$ to check the source-locked linear and fixed-residual-depth profiles. It also reports $\ell^1$, mean, and variance errors at increasing $k$. These rows reproduce proved formulas; they are not interval certificates or observations of an actual noisy head.

The next read-only candidate is RH-359: invert the terminal-tail law at logarithmic window widths and retain the integer floor phase in polynomial accuracy thresholds. That route remains deterministic until a typed physical transfer theorem is available.

RH-358 does not prove [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}; identify actual roots, ranks, or spectra; close a determinant, $p$, the unrelated open $q$, or $E_{\rm off}$; close the moving noisy envelope of RH-241 [@WangEnvelopeReview2026]; or activate the gluing criterion of RH-288 [@WangGluing2026]. Gates A--E remain false/open. There is no Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace theorem, zeta-divisor equality, or proof of the Riemann hypothesis.
