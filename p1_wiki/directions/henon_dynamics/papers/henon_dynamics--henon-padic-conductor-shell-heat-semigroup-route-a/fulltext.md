---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-padic-conductor-shell-heat-semigroup-route-a"
canonical_tex: "henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a/paper/main.pdf"
source_sha256: "6328548850c721ed81c4a8ccd741268f4d03d8e033002b6f0eabaf2be2574752"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Conductor-Shell p-Adic Fractional Heat Semigroup: Exact Zeta, Scale Oscillation, and Boundary Closure

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every fixed prime $p$ and $\alpha>0$, we define a nonnegative operator on $L^2(\mathbb Z_p)$ directly as the Fourier multiplier $0$ on constants and $p^{\alpha n}$ on characters of exact conductor $n$. Its spectrum and a conditional-expectation reconstruction prove a positive conservative Markov semigroup with an exact heat trace. \>0 We prove the exact eigenvalue staircase, a discrete-scale oscillation and log-periodic heat profile, and the sharp Schatten threshold for fractional resolvents. \>1 The mean-zero spectral zeta has a complete vertical pole lattice and an explicit primed determinant; all $\alpha=0$, $\mu=0$, and $t=0$ faces and a finite-quotient DFT certificate are closed. The fixed local prime is not promoted to all-prime target arithmetic.
author:
- 'Route-A source-local certificate HCS-C283'
date: 1 September 2026
title: |
  Conductor-Shell p-Adic Fractional Heat Semigroup:\
  Exact Zeta, Scale Oscillation, and Boundary Closure
```

## Markdown 正文

suppressoptionalinfo 767 trailerid \[\<C2832026090100000000000000000000\>\<C2832026090100000000000000000000\>\]

# The frozen conductor multiplier

Let $p$ be any fixed rational prime, let $G=\mathbb Z_p$ have Haar mass one, and use $\widehat G=\mathbb Q_p/\mathbb Z_p$. A nonzero class $\xi$ has exact conductor $n(\xi)=n$ when $\chi_\xi$ is trivial on $p^n\mathbb Z_p$ but not on $p^{n-1}\mathbb Z_p$. Exactly $p^n-p^{n-1}=(p-1)p^{n-1}$ characters have conductor $n$.

For $\alpha>0$ we freeze $$D_{p,\alpha}1=0,\qquad
 D_{p,\alpha}\chi_\xi=p^{\alpha n(\xi)}\chi_\xi,             \tag{1}$$ with its maximal diagonal domain. For $\mu\geq0$, set $A_{p,\alpha,\mu}=D_{p,\alpha}+\mu I$ and $T_t=e^{-tA_{p,\alpha,\mu}}$. Equation (1) is the normalization: the paper does not identify it with every convention called a Vladimirov operator. Pseudodifferential spectra over p-adic fields, p-adic wavelet eigenbases, and ultrametric Markov semigroups form the surrounding literature [@Vlad; @Kozyrev; @BGPW; @VVZ]. More directly, Example 5.1 of Chacón-Cortés--Zúñiga-Galindo [@CZ], at dimension one and exponent $\alpha$, already gives exactly our positive shell spectrum, multiplicities, geometric zeta, and vertical pole lattice. Those receive zero priority credit. We retain a source-local Markov, scale-boundary, determinant, and finite-reconstruction closure, not a literature-novelty claim.

Let $E_n$ denote conditional expectation onto functions constant on cosets of $p^n\mathbb Z_p$, so $E_0=P_0$ projects onto constants and $E_n\uparrow I$ strongly. Put $$W_0=\operatorname{ran}E_0,\qquad W_n=\operatorname{ran}E_n\ominus\operatorname{ran}E_{n-1}\quad(n\geq1).$$ Then $\dim W_n=(p-1)p^{n-1}$ and the character and filtration descriptions give the same orthogonal decomposition.

The spectrum of $D_{p,\alpha}$ consists of the simple eigenvalue zero and $p^{\alpha n}$ with multiplicity $(p-1)p^{n-1}$, $n\geq1$. Its resolvent is compact. The spectrum of $A_{p,\alpha,\mu}$ is the simple eigenvalue $\mu$ and $\mu+p^{\alpha n}$ with the same multiplicities. Moreover $e^{-tD_{p,\alpha}}$ is a positive, conservative, self-adjoint contraction semigroup, while $T_t$ is positive sub-Markov and $\lVert T_t\rVert=e^{-\mu t}$.

Character counting and (1) prove the spectral assertion; the eigenvalues tend to infinity. A second reconstruction is $$D_{p,\alpha}=\sum_{n\geq1}p^{\alpha n}P_{W_n}
 =\sum_{n\geq0}a_n(I-E_n),                                \tag{2}$$ where $a_0=p^\alpha$ and $a_n=p^{\alpha(n+1)}-p^{\alpha n}$ for $n\geq1$. On $W_m$, the right side is $\sum_{n<m}a_n=p^{\alpha m}$. For every conditional expectation $E$, $$e^{-s a(I-E)}=E+e^{-sa}(I-E)$$ is positive, constant-preserving, and contractive. The finite factors in (2) commute; their strong limit proves the Markov claims. The scalar killing factor $e^{-\mu t}$ gives the final norm and sub-Markov statement.

This proof derives positivity from the residue filtration. Nonnegative eigenvalues alone would not have established positivity preservation.

\>0

# Heat trace, exact staircase, and Schatten boundary

For $q>0$, write $\mathcal S_q$ for the operators whose singular values have finite $q$-sum. When $0<q<1$, this is the quasi-Schatten ideal with its usual quasi-norm, not a Banach Schatten class.

For $t>0$, $T_t\in\mathcal S_q$ for every $q>0$ and $$\operatorname{Tr}T_t=e^{-\mu t}\left[1+\sum_{n\geq1}(p-1)p^{n-1}
 e^{-tp^{\alpha n}}\right].                              \tag{3}$$ If $N(\Lambda)$ counts the positive spectrum, then $$p^{\alpha m}\leq\Lambda<p^{\alpha(m+1)}
 \quad\Longrightarrow\quad N(\Lambda)=p^m-1.             \tag{4}$$ Consequently $$\limsup_{\Lambda\to\infty}\frac{N(\Lambda)}{\Lambda^{1/\alpha}}=1,
 \qquad
 \liminf_{\Lambda\to\infty}\frac{N(\Lambda)}{\Lambda^{1/\alpha}}=\frac1p.$$ For $\sigma,q>0$, $$(I+D_{p,\alpha})^{-\sigma}\in\mathcal S_q
 \quad\Longleftrightarrow\quad \alpha\sigma q>1;          \tag{5}$$ the equality case diverges.

The spectral theorem and shell multiplicities give (3), and exponential decay in $p^{\alpha n}$ dominates every geometric multiplicity; the same argument applies after taking any positive power of the singular values. Summing the first $m$ multiplicities gives $p^m-1$, proving (4). At a shell and just before its successor, the scaled ratios approach $1$ and $1/p$, respectively. Finally, the $q$-sum in (5) is comparable, up to finitely many terms, to $\sum_n p^{n(1-\alpha\sigma q)}$, which converges exactly under the displayed strict inequality.

The staircase also has an exact small-time scaling profile. If $t=p^{-\alpha m}\tau$, then locally uniformly for $\tau>0$, $$t^{1/\alpha}\bigl(\operatorname{Tr}e^{-tD_{p,\alpha}}-1\bigr)
 \xrightarrow[m\to\infty]{} \Phi_{p,\alpha}(\tau)
 =\frac{p-1}{p}\tau^{1/\alpha}
 \sum_{j\in\mathbb Z}p^j e^{-\tau p^{\alpha j}}.           \tag{6}$$ The negative tail is geometric and the positive tail superexponential, so the limit follows by reindexing $j=n-m$. Reindexing once more gives $\Phi_{p,\alpha}(p^\alpha\tau)=\Phi_{p,\alpha}(\tau)$. Equations (4) and (6) record a genuine discrete-scale oscillation, not a missing smooth Weyl constant. Notice the category distinction: positive-time heat is in every $\mathcal S_q$, whereas the fractional resolvent has the sharp boundary (5).

\>1

# Complete zeta lattice and primed determinant

All zeta statements are on $L^2_0(\mathbb Z_p)$; the prime symbol means that the constant zero mode is omitted.

Initially for $\Re s>1/\alpha$, $$\zeta_{p,\alpha}(s)=\operatorname{Tr}' D_{p,\alpha}^{-s}
 =(1-p^{-1})\frac{p^{1-\alpha s}}{1-p^{1-\alpha s}}.       \tag{7}$$ This is the meromorphic continuation. Its complete pole set is $$s_k=\frac1\alpha+\frac{2\pi i k}{\alpha\log p},
 \qquad k\in\mathbb Z,                                   \tag{8}$$ all poles are simple, and each residue is $(1-p^{-1})/(\alpha\log p)$. Furthermore $$\zeta_{p,\alpha}(0)=-1,
 \quad \zeta'_{p,\alpha}(0)=-\frac{\alpha\log p}{p-1},
 \quad \det{}'_{\zeta}D_{p,\alpha}=p^{\alpha/(p-1)}.      \tag{9}$$

Shell summation gives a geometric series of ratio $p^{1-\alpha s}$, proving (7). The denominator vanishes exactly at (8); its derivative there is $\alpha\log p$, while the numerator is $1-p^{-1}$, proving completeness, simplicity, and the residue. Substitution and differentiation at zero give (9), including the convention $\det{}'_\zeta D=\exp[-\zeta'(0)]$.

The vertical pole lattice is the Mellin counterpart of discrete spatial scaling. It is not a target zero set, and the source-local primed determinant is not a target Euler product.

# Boundary atlas and finite-quotient reconstruction

At $\alpha=0$ the natural face is $D_{p,0}=I-P_0$. It is bounded and noncompact, with eigenvalue one of infinite multiplicity. For fixed $t>0$, $e^{-t(D_{p,\alpha}+\mu I)}$ converges strongly as $\alpha\downarrow0$ to $e^{-t(I-P_0+\mu I)}$, but not in operator norm: the mean-zero norm defect is $e^{-(\mu+1)t}$. Thus trace class, compact resolvent, and (7) do not extend to that face.

At $\mu=0$ constants remain the zero mode and the heat semigroup is Markov; this is why (7)--(9) are mean-zero and primed. At $t=0$, $T_0=I$ is not compact and belongs to no finite $\mathcal S_q$. Conversely, for fixed $t>0$, $\alpha\to\infty$ gives $T_t\to e^{-\mu t}P_0$ in operator norm, since the mean-zero norm is $e^{-\mu t-tp^\alpha}$. No odd-prime step was used, so $p=2$ is included.

On $G_N=\mathbb Z/p^N\mathbb Z$, character $k\ne0$ has conductor $N-v_p(k)$. Hence the finite DFT multiplier agrees exactly with $$\sum_{n=1}^N p^{\alpha n}(E_n-E_{n-1}).                  \tag{10}$$ The executable receipt tests 36 DFT instances through quotient order 4096, alongside 402 analytic and control cells. A separate checker performs 1507 assertions, SymPy supplies 102 exact rational-matrix and zeta checks, fresh replay is byte-identical, and all 17 repaired-hash hostile mutations fail.

# Route-A obstruction

The prime $p$ is intrinsic to the local source, so the ceiling is honestly `A0_WEAK_ARITHMETIC_RELATION`. But one fixed $p$ is not all rational primes; conductor shells are scale eigenspaces, not primitive orbits carrying logarithmic prime lengths. Composite branching numbers $4,6,10$ reproduce the spectrum, geometric zeta, counting, and Schatten algebra, which is the strongest proves-too-much control. There is no target determinant, analytic divisor bridge, or same-clock arithmetic quantization.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$\texttt{(A0\_WEAK\_ARITHMETIC\_RELATION,A1\_FAIL,A2\_FAIL,A3\_FAIL,
A4\_FORMAL\_HINT)},$$ overall `ROUTE_A_REJECTED`; Route B is disabled. No fixed local prime, source heat trace, or zeta determinant is promoted to target Euler data, bad-prime data, root numbers, or a Hilbert--Pólya operator.

9 V. S. Vladimirov, *On the spectrum of some pseudodifferential operators over the field of p-adic numbers*, Algebra i Analiz 2:6 (1990), 107--124; Leningrad Math. J. 2:6 (1991), 1261--1278, [MathNet aa223](https://www.mathnet.ru/eng/aa223). S. V. Kozyrev, *Wavelet theory as p-adic spectral analysis*, Izv. Math. 66:2 (2002), 367--376, [DOI record](https://doi.org/10.1070/IM2002v066n02ABEH000381). A. D. Bendikov, A. A. Grigor'yan, Ch. Pittet, and W. Woess, *Isotropic Markov semigroups on ultra-metric spaces*, Russian Math. Surveys 69:4 (2014), 589--680, [DOI record](https://doi.org/10.1070/RM2014v069n04ABEH004907). L. F. Chacón-Cortés and W. A. Zúñiga-Galindo, *Heat traces and spectral zeta functions for p-adic Laplacians*, St. Petersburg Math. J. 29:3 (2018), 529--544, [DOI record](https://doi.org/10.1090/spmj/1505). V. S. Vladimirov, I. V. Volovich, and E. I. Zelenov, *p-Adic Analysis and Mathematical Physics*, World Scientific, 1994.
