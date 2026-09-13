---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-359-logarithmic-terminal-window-accuracy-thresholds"
canonical_tex: "zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds/main.pdf"
source_sha256: "76ab823bee396fb3f955c995ff798c3f8f7c7d9189df27de6e1e1bde7e009938"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Logarithmic Terminal-Window Accuracy Thresholds for the Complete Upper Counterloop Band

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-359-logarithmic-terminal-window-accuracy-thresholds/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We invert the deterministic terminal-tail law of RH-358 at polynomial target accuracy. Let $E_k(q)=P_k(q)/C_k$ be the relative strict-upper-band mass left after retaining the top $q$ terminal coordinates, and let $x>1$ be the source-locked radial constant. For $a>0$, $c\in\mathbb R$, put $$t_k=\frac{a\log k}{\log x}+c,\qquad q_k=\lfloor t_k\rfloor,
   \qquad\theta_k=\{t_k\}.$$ We prove $$k^aE_k(q_k)=x^{\theta_k-c}\{1+o(1)\}.$$ The complete limit set of $\theta_k$ is $[0,1]$, so the normalized error has the complete cluster interval $[x^{-c},x^{1-c}]$ rather than a unique constant. If $$Q_k(a,c)=\min\{q:E_k(q)\le x^{-c}k^{-a}\},$$ then $Q_k=t_k+O(1)$ and the complete limit set of $Q_k-t_k$ is exactly $[0,1]$. We also classify arbitrary sublinear windows by their polynomial accuracy exponent and translate logarithmic width to the physical double-log clock. Actual-head inheritance is only conditional on the original unnormalized same-clock leaf $D_{4k}(R)\to0$. No root or rank identification, determinant closure, Gate A--E promotion, Hilbert--Polya construction, zero identification, or proof of RH is claimed.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Logarithmic Terminal-Window Accuracy Thresholds\
  for the Complete Upper Counterloop Band
```

## Markdown 正文

# Source-locked tail ledger

Let $k\to\infty$ be the RH-342 first-alias clock and let $$\label{eq:x-y}
 x=(\beta R)^2>1,
 \qquad
 y_k=(\beta_kR)^2
 =x\exp\left[-\frac{\log C_M}{k}+o(k^{-1})\right],
 \qquad C_M>0.$$ The deterministic strict upper-counterloop budgets of RH-357--RH-358 are $$\begin{aligned}
 B_k(L)&=\sum_{j=1}^{L}\frac{y_k^{k+j}}{k+j},
 &&1\le L\le k-1,\label{eq:B}\\
 C_k&=B_k(k-1),
 &P_k(q)&=B_k(k-1-q),
 &&0\le q\le k-2.\label{eq:C-P}\end{aligned}$$ Define the relative truncation error $$\label{eq:E}
 E_k(q):=\frac{P_k(q)}{C_k}.$$ Equivalently, $1-E_k(q)$ is the normalized mass in the top $q$ terminal coordinates. Since every terminal-lag weight is positive, $E_k(q)$ is strictly decreasing in $q$.

RH-358 proves the uniform source-locked formula $$\label{eq:full-profile}
 E_k(q)=x^{-q}C_M^{q/k}\frac{2k-1}{2k-1-q}
 \frac{1-x^{-(k-1-q)}}{1-x^{-(k-1)}}\{1+o(1)\},$$ where the relative $o(1)$ is uniform over $0\le q\le k-2$ [@WangTerminalLag2026]. The finite-tail factor in [\[eq:full-profile\]](#eq:full-profile){reference-type="eqref" reference="eq:full-profile"} is essential near $q=k-2$. The present paper uses only the logarithmic subrange, where every displayed correction can be quantified without deleting it outside its valid domain.

The symbol $q$ here is an integer window width. It is not the open direct/full-trace quantity denoted by the same letter elsewhere in the project.

# Uniform logarithmic reduction and phase density

[\[lem:log-window\]]{#lem:log-window label="lem:log-window"} For every fixed $A>0$, $$\label{eq:log-uniform}
 \sup_{0\le q\le A\log k}
 \left|x^qE_k(q)-1\right|\longrightarrow0,$$ where the supremum is over admissible integers.

In the stated range, $q/k=O(\log k/k)$. Hence $C_M^{q/k}\to1$ and $(2k-1)/(2k-1-q)\to1$ uniformly. Also $k-1-q\to\infty$ uniformly, so both finite-tail factors in [\[eq:full-profile\]](#eq:full-profile){reference-type="eqref" reference="eq:full-profile"} tend uniformly to one. The source remainder in [\[eq:full-profile\]](#eq:full-profile){reference-type="eqref" reference="eq:full-profile"} is already uniform on the full admissible range. Multiplication by $x^q$ proves [\[eq:log-uniform\]](#eq:log-uniform){reference-type="eqref" reference="eq:log-uniform"}.

The logarithmic phase mechanism was used for a different post-alias ratio in RH-356 [@WangMesoscopic2026]. We record the exact generality needed for the accuracy problem.

[\[lem:phase\]]{#lem:phase label="lem:phase"} Fix $a>0$ and $c\in\mathbb R$. Then $$\label{eq:theta}
 \theta_k(a,c):=
 \left\{\frac{a\log k}{\log x}+c\right\}$$ has complete limit set $[0,1]$.

For $t\in(0,1)$, take $$k_m=\left\lfloor x^{(m+t-c)/a}\right\rfloor.$$ Then $a\log_x k_m+c=m+t+o(1)$, so a subsequence of phases tends to $t$. For the endpoints, use $$k_m^{(0)}=\left\lceil x^{(m-c)/a}\right\rceil,
 \qquad
 k_m^{(1)}=\left\lceil x^{(m+1-c)/a}\right\rceil-1.$$ The first phase tends to zero and the second to one. Subtracting one in the second construction handles exact integer powers. No phase outside $[0,1]$ is possible.

# Polynomial accuracy and its integer phase

Fix $a>0$ and $c\in\mathbb R$, and define $$\label{eq:t-q}
 t_k(a,c):=\frac{a\log k}{\log x}+c,
 \qquad q_k(a,c):=\lfloor t_k(a,c)\rfloor,
 \qquad \theta_k(a,c):=\{t_k(a,c)\}.$$ These integers are admissible for all sufficiently large $k$.

[\[thm:phase-law\]]{#thm:phase-law label="thm:phase-law"} With [\[eq:t-q\]](#eq:t-q){reference-type="eqref" reference="eq:t-q"}, $$\label{eq:phase-law}
 \boxed{
 k^aE_k(q_k(a,c))
 =x^{\theta_k(a,c)-c}\{1+o(1)\}.}$$ The complete limit set of the left-hand side is $$\label{eq:error-cluster}
 \boxed{[x^{-c},x^{1-c}].}$$ In particular, $$\label{eq:liminf-limsup}
 \liminf k^aE_k(q_k)=x^{-c},
 \qquad
 \limsup k^aE_k(q_k)=x^{1-c},$$ and the sequence has no single limit.

Since $q_k=O(\log k)$, [\[lem:log-window\]](#lem:log-window){reference-type="ref" reference="lem:log-window"} gives $E_k(q_k)=x^{-q_k}\{1+o(1)\}$. The identity $$q_k=\frac{a\log k}{\log x}+c-\theta_k$$ then yields [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"}. Apply [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"} and the continuous increasing map $t\mapsto x^{t-c}$ to obtain the complete cluster interval. Its endpoints differ because $x>1$.

[\[cor:exponent\]]{#cor:exponent label="cor:exponent"} Let $q_k=o(k)$ be admissible. Then $$\label{eq:log-error}
 \log E_k(q_k)=-q_k\log x+o(1).$$ Consequently, if $$\label{eq:exponent-assumption}
 \frac{q_k\log x}{\log k}\longrightarrow a\in[0,\infty],$$ then $$\label{eq:exponent-law}
 \frac{\log E_k(q_k)}{\log k}\longrightarrow-a.$$ For $a=\infty$, this means $E_k(q_k)=o(k^{-A})$ for every fixed $A>0$.

The sublinear specialization of [\[eq:full-profile\]](#eq:full-profile){reference-type="eqref" reference="eq:full-profile"} is $E_k(q_k)=x^{-q_k}\{1+o(1)\}$. Taking logarithms proves [\[eq:log-error\]](#eq:log-error){reference-type="eqref" reference="eq:log-error"}; division by $\log k$ gives the finite cases. If the ratio in [\[eq:exponent-assumption\]](#eq:exponent-assumption){reference-type="eqref" reference="eq:exponent-assumption"} diverges, then for every fixed $A$ it eventually exceeds $A+1$, and [\[eq:log-error\]](#eq:log-error){reference-type="eqref" reference="eq:log-error"} gives the asserted superpolynomial bound.

# The exact minimal integer window

For $a>0$ and $c\in\mathbb R$, let the target error be $$\label{eq:target}
 \varepsilon_k(a,c):=x^{-c}k^{-a}=x^{-t_k(a,c)}.$$ Because $E_k(0)=1$, $E_k$ is strictly decreasing, and the final admissible tail is exponentially small, the following minimum exists for all large $k$: $$\label{eq:Q}
 Q_k(a,c):=min\{0\le q\le k-2:E_k(q)\le\varepsilon_k(a,c)\}.$$

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} For every $a>0$ and $c\in\mathbb R$, $$\label{eq:Q-first}
 Q_k(a,c)=t_k(a,c)+O(1).$$ More precisely, the complete limit set of $$\label{eq:Q-correction}
 Q_k(a,c)-t_k(a,c)$$ is exactly $$\label{eq:Q-cluster}
 \boxed{[0,1].}$$ If $\theta_k(a,c)$ remains in a fixed compact subinterval of $(0,1)$ along a subsequence, then on that subsequence $$\label{eq:generic-ceiling}
 Q_k(a,c)=\lceil t_k(a,c)\rceil$$ eventually.

Write $n_k=\lfloor t_k\rfloor$ and $\theta_k=\{t_k\}$. For each fixed $j\in\{-1,0,1,2\}$, [\[lem:log-window\]](#lem:log-window){reference-type="ref" reference="lem:log-window"} gives $$\label{eq:four-ratios}
 \frac{E_k(n_k+j)}{\varepsilon_k(a,c)}
 =x^{\theta_k-j}\{1+o(1)\},$$ whenever the index is admissible, which it is eventually. The case $j=-1$ is eventually greater than one, while $j=2$ is eventually less than one. Thus $$\label{eq:Q-bracket}
 n_k\le Q_k\le n_k+2,$$ proving [\[eq:Q-first\]](#eq:Q-first){reference-type="eqref" reference="eq:Q-first"}.

Consider any convergent subsequence of [\[eq:Q-correction\]](#eq:Q-correction){reference-type="eqref" reference="eq:Q-correction"}. Passing to a further subsequence, $Q_k-n_k$ is one fixed value $j\in\{0,1,2\}$ and $\theta_k\to\theta\in[0,1]$. If $j=0$, minimality and [\[eq:four-ratios\]](#eq:four-ratios){reference-type="eqref" reference="eq:four-ratios"} force $x^\theta\le1$, hence $\theta=0$ and the correction tends to zero. If $j=2$, then $E_k(n_k+1)>\varepsilon_k$; [\[eq:four-ratios\]](#eq:four-ratios){reference-type="eqref" reference="eq:four-ratios"} forces $x^{\theta-1}\ge1$, hence $\theta=1$ and the correction tends to one. If $j=1$, the correction tends to $1-\theta\in[0,1]$. Therefore every cluster point lies in $[0,1]$.

Conversely, fix $s\in(0,1)$. By [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"}, choose a subsequence with $\theta_k\to1-s$. Along it, the $j=0$ ratio in [\[eq:four-ratios\]](#eq:four-ratios){reference-type="eqref" reference="eq:four-ratios"} tends to $x^{1-s}>1$, while the $j=1$ ratio tends to $x^{-s}<1$. Hence $Q_k=n_k+1$ eventually and $Q_k-t_k\to s$. The limit set of a bounded sequence is closed, so it also contains the endpoints. This proves [\[eq:Q-cluster\]](#eq:Q-cluster){reference-type="eqref" reference="eq:Q-cluster"}. The same strict two-ratio comparison proves [\[eq:generic-ceiling\]](#eq:generic-ceiling){reference-type="eqref" reference="eq:generic-ceiling"} whenever the phase is bounded away from zero and one.

At a phase endpoint, one of the ratios in [\[eq:four-ratios\]](#eq:four-ratios){reference-type="eqref" reference="eq:four-ratios"} tends to one. The source lock [\[eq:x-y\]](#eq:x-y){reference-type="eqref" reference="eq:x-y"} allows an unspecified $o(k^{-1})$ term, so its sign may decide between adjacent integers. The interval [\[eq:Q-cluster\]](#eq:Q-cluster){reference-type="eqref" reference="eq:Q-cluster"} is the sharp source-backed conclusion.

# Physical clock and conditional actual-head inheritance

On the RH-355 physical clock, $$\label{eq:physical-clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1).$$ Therefore $$\label{eq:physical-width}
 \frac{a\log k}{\log x}+c
 =\frac{a}{\log x}\log\log(1/\sigma)
 +c-\frac{a}{\log x}\log(2\log\lambda)+o(1).$$ Polynomial-in-$k$ truncation accuracy thus requires a double-logarithmic number of terminal coordinates. Equation [\[eq:Q-cluster\]](#eq:Q-cluster){reference-type="eqref" reference="eq:Q-cluster"} prevents promotion of [\[eq:physical-width\]](#eq:physical-width){reference-type="eqref" reference="eq:physical-width"} to a unique integer constant without a phase subsequence.

Let $E_k^{\mathcal H}(q)$ be the corresponding actual even-weight relative tail from RH-358. Under the original same-clock unnormalized hypothesis $$\label{eq:D}
 D_{4k}(R):=\sum_{2\le n<4k}
 \frac{|h_{\sigma,n}-s_{k,n}|R^n}{n}\longrightarrow0,$$ RH-358 proves $$\label{eq:actual-uniform}
 \sup_{0\le q\le k-2}
 \left|\frac{E_k^{\mathcal H}(q)}{E_k(q)}-1\right|\longrightarrow0.$$

Assume [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} on one physical clock, and define $$Q_k^{\mathcal H}(a,c):=
 \min\{0\le q\le k-2:E_k^{\mathcal H}(q)\le x^{-c}k^{-a}\}.$$ Then the phase law [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"} and exponent law [\[eq:exponent-law\]](#eq:exponent-law){reference-type="eqref" reference="eq:exponent-law"} hold with $E_k^{\mathcal H}$ in place of $E_k$, and the complete limit set of $Q_k^{\mathcal H}(a,c)-t_k(a,c)$ is $[0,1]$.

Equation [\[eq:actual-uniform\]](#eq:actual-uniform){reference-type="eqref" reference="eq:actual-uniform"} multiplies every tail ratio used above by $1+o(1)$ uniformly in $q$. The proofs of [\[thm:phase-law,thm:inverse\]](#thm:phase-law,thm:inverse){reference-type="ref" reference="thm:phase-law,thm:inverse"} and [\[cor:exponent\]](#cor:exponent){reference-type="ref" reference="cor:exponent"} use only such ratios, monotonicity of nonnegative tails, and phase subsequences. Repeating them gives the conditional claims.

This theorem is inactive until [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} is proved. It transfers weighted budget accuracy only, not roots, ranks, eigenvalues, or determinants.

# Finite protocol, boundary, and next route

The artifact uses the exact rational fixture $x=2352/1445$ to evaluate exact terminal tails and exact minimal widths for rational polynomial targets. High-precision rows reproduce the phase formula and finite cluster coverage. They are finite checks, not evidence for phase density or an actual noisy operator.

The next read-only candidate is RH-360: the exponential generating function $G_k(z)=\sum_r z^r\pi_k(r)$ across the critical value $z=x$. The anticipated scales are a finite transform below $x$, a $k$-scaled Riemann-integral law in the critical window $z_k=x\exp(\tau/k)$, and exponential endpoint dominance above $x$. No such candidate is pre-authorized as an actual spectral law.

RH-359 does not prove [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}; identify actual roots, ranks, or spectra; close a determinant, $p$, the unrelated open $q$, or $E_{\rm off}$; close the moving noisy envelope of RH-241 [@WangEnvelopeReview2026]; or activate the gluing criterion of RH-288 [@WangGluing2026]. Gates A--E remain false/open. There is no Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace theorem, completed-zeta divisor equality, or proof of RH.
