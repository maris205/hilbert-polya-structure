---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mm-infinity-poisson-spectral-route-a"
canonical_tex: "henon_dynamics/henon_mm_infinity_poisson_spectral_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mm_infinity_poisson_spectral_route_a/paper/main.pdf"
source_sha256: "cc839730a49ffb2f46082ad878b39b8a3ad1a6d6ce6881bd4156d6d3bf66ba40"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Poisson--Charlier Spectrum and Trace Class for the M/M/$\infty$ Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mm_infinity_poisson_spectral_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mm_infinity_poisson_spectral_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mm_infinity_poisson_spectral_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mm_infinity_poisson_spectral_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete theorem for the infinite-server immigration--death chain. The unique positive-rate invariant law is Poisson, and the transition kernel is exactly a binomial survivor count convolved with a Poisson immigration count. Charlier polynomials diagonalize the generator on $L^2$ of that law, yielding the sharp gap, all relaxation rates, and a positive-time trace-class semigroup with an explicit source Fredholm product. Coupling gives quantitative total-variation bounds. Pure-death, pure-birth, zero-rate, small-intensity and long-time faces are kept separate. The source semigroup is not relabeled as an arithmetic primitive-orbit determinant. Independent exact, symbolic, replay and hostile-mutation audits accompany the proof.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Poisson--Charlier Spectrum and Trace Class for the M/M/$\infty$ Flow'
```

## Markdown 正文

suppressoptionalinfo 611

# Generator and exact kernel

For $n\in\mathbb N_0$ let $$Qf(n)=\lambda\{f(n+1)-f(n)\}+\mu n\{f(n-1)-f(n)\},\qquad \lambda,\mu>0.
 \label{eq:generator}$$ Write $\rho=\lambda/\mu$ and $a_t=e^{-\mu t}$. The physical clock is the continuous-time Markov time $t$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} The unique reversible invariant law of [\[eq:generator\]](#eq:generator){reference-type="eqref" reference="eq:generator"} is $$\pi_n=e^{-\rho}\frac{\rho^n}{n!},\qquad n\ge0.$$ Conditionally on $X_0=n$, one has the exact decomposition $$X_t\ \stackrel{d}{=}\ B_{n,a_t}+P_{\rho(1-a_t)},
 \tag{2}$$ where the summands are independent, $B_{n,a_t}$ is binomial and $P_m$ is Poisson with mean $m$. Equivalently, $$\mathbb E[z^{X_t}\mid X_0=n]
 =((1-a_t)+a_tz)^n e^{\rho(1-a_t)(z-1)}. \tag{3}$$ Define $C_k$ by $$\sum_{k\ge0}C_k(n;\rho)\frac{u^k}{k!}=e^{-\rho u}(1+u)^n . \tag{4}$$ Then $\mathbb E_\pi[C_kC_\ell]=k!\rho^k\mathbf1_{k=\ell}$ and, for the normalized $\phi_k=C_k/\sqrt{k!\rho^k}$, $$Q\phi_k=-k\mu\phi_k,\qquad P_t\phi_k=e^{-k\mu t}\phi_k . \tag{5}$$ Thus the $L^2(\pi)$ gap is $\mu$ and, for $t>0$, $$\operatorname{Tr}P_t=\frac1{1-e^{-\mu t}},\qquad
 \det(I-zP_t)=\prod_{k\ge0}(1-ze^{-k\mu t})
 \tag{6}$$ in the source-local trace/Fredholm convention.

Detailed balance is $\lambda\pi_n=\mu(n+1)\pi_{n+1}$, which gives the Poisson law and reversibility. Independently thinning each initial customer and superposing the stationary immigration process gives (2), hence (3). Taking coefficients in (4) gives the displayed Charlier polynomial. Applying [\[eq:generator\]](#eq:generator){reference-type="eqref" reference="eq:generator"} to that polynomial yields $QC_k=-k\mu C_k$; Poisson coefficient orthogonality gives the stated norm and completeness. The spectral expansion then proves (5). Summing the geometric eigenvalue sequence gives the trace in (6), and absolute convergence of $\sum_k|ze^{-k\mu t}|$ gives the source Fredholm product.

# Mixing and boundary faces

A shared-immigration coupling leaves each unmatched initial customer alive with probability $a_t$. Therefore $$\|P_t(n,\cdot)-P_t(m,\cdot)\|_{\rm TV}
 \le \min\{1,a_t|n-m|\}. \tag{7}$$ Coupling a deterministic initial state to a stationary Poisson initial state also gives $\|P_t(n,\cdot)-\pi\|_{\rm TV}\le
\min\{1,a_t(n+\rho)\}$. These are deliberately coarse but uniform bounds; the kernel ledger records the finite PMF window and its explicit tail mass.

If $\lambda=0$ and $\mu>0$, the pure-death chain has the absorbing law $\delta_0$. If $\mu=0$ and $\lambda>0$, pure birth has no stationary probability and escapes to infinity. If both rates vanish, the identity chain has every point mass stationary. As $\rho\downarrow0$ the Poisson law collapses weakly to $\delta_0$; as $\mu\downarrow0$ with $\lambda$ fixed it loses tightness. For positive rates, $a_t\downarrow0$ proves total-variation convergence to $\pi$.

\>0

# Finite certificate and source determinant

The canonical ledger freezes five rational rate pairs, four times, four initial states and a 24-cell PMF window. It contains 45 normalized mode rows, 80 kernel rows and 20 trace rows. The producer-independent checker makes 7367 assertions, including direct generator eigen-equations and coupling checks; SymPy verifies 25 identities. Clean replay is byte-for-byte, and the hostile suite rejects 20 repaired-hash/schema mutations plus one stale-hash mutation (21/21 hostile cases). The finite PMF window is an audit oracle, not an unqualified truncation theorem.

\>1

# Route-A boundary

The Charlier modes are stochastic population modes. They have no intrinsic rational-prime owner, logarithmic prime clock, or target divisor, and the source-local product in (6) is not a target zeta or Hilbert--Polya operator. The strict tuple is $$\begin{gathered}
 (\texttt{A0\_FAIL,A1\_FAIL,A2\_FAIL,}\\[-1mm]
 \texttt{A3\_FAIL,A4\_FORMAL\_HINT}) .
 \end{gathered}$$ with `ROUTE_A_REJECTED`; the route-B flag is false, and scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. The positive-time trace class is a theorem about this Markov semigroup only. No external peer review or priority claim is made.

# Source note and declarations {#source-note-and-declarations .unnumbered}

The birth--death spectral framework follows Karlin and McGregor [@KM1957]; the Poisson polynomial normalization follows the Charlier construction [@Ch1929]. The queueing interpretation is standard [@Massey1987]. No target prime or zero table, local arithmetic datum, Euler factor, root number, automorphy object, target functional equation, Hilbert--Polya operator or Route-B input is used. Generative tools assisted drafting and code generation; the artifact chain checks the displayed claims. Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 S. Karlin and J. McGregor, "The differential equations of birth-and-death processes, and the Stieltjes moment problem," *Transactions of the American Mathematical Society* 85 (1957), 489--546. DOI: 10.1090/S0002-9947-1957-0091566-1. C. V. L. Charlier, "Über die Darstellung willkürlicher Funktionen," *Arkiv för Matematik, Astronomi och Fysik* 16 (1929). W. A. Massey, *An Introduction to Queueing Networks*, Springer, 1987. DOI: 10.1007/978-1-4612-4960-1.
