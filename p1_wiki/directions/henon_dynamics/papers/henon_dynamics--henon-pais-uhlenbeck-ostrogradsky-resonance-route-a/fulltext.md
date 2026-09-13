---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-pais-uhlenbeck-ostrogradsky-resonance-route-a"
canonical_tex: "henon_dynamics/henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/paper/main.pdf"
source_sha256: "233b5e0927342d2560f0cfcce0c06815851effcf8dcba2fa2ca4533862117aeb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Pais--Uhlenbeck Oscillator: Canonical Signs, Resonant Tori, Jordan Collision, and a Quantum Difference Spectrum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_pais_uhlenbeck_ostrogradsky_resonance_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_pais_uhlenbeck_ostrogradsky_resonance_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the two-frequency Pais--Uhlenbeck oscillator we prove an exact Ostrogradsky normal form and classify every classical orbit closure. A rational frequency ratio closes every orbit; an irrational ratio leaves only the equilibrium and single-mode circles periodic, while each genuine double-mode orbit is dense on a two-torus. We then resolve the equal-frequency Jordan collision and all real sign degenerations. \>1 Finally, the natural distinct-positive-frequency quantization is defined on its maximal Hermite diagonal domain. Rational ratios give an eigenvalue lattice of infinite multiplicity, whereas irrational ratios give simple, dense eigenvalues, pure-point spectral measures, and spectrum $\mathbb R$. Finite exact receipts audit conventions; the continuum statements are proved analytically.
author:
- 'HCS-C359 source-local theorem package'
date: 'September 4, 2026'
title: |
  The Pais--Uhlenbeck Oscillator: Canonical Signs, Resonant Tori,\
  Jordan Collision, and a Quantum Difference Spectrum
```

## Markdown 正文

trailerid \[\<C3592026090400000000000000000000\>\<C3592026090400000000000000000000\>\]

# Frozen model and canonical sign

Consider $$L=\frac12\{\ddot x^2-(\omega _1^2+\omega _2^2)\dot x^2
 +\omega _1^2\omega _2^2x^2\},\qquad 0<\omega _1<\omega _2.$$ The higher-order Euler--Lagrange equation factors as $$(D^2+\omega _1^2)(D^2+\omega _2^2)x=0.$$ With $q_0=x,q_1=\dot x,p_1=\ddot x$ and $p_0=-(\omega _1^2+\omega _2^2)\dot x-x^{(3)}$, the Ostrogradsky Hamiltonian is $$H=p_0q_1+\frac12p_1^2+\frac12(\omega _1^2+\omega _2^2)q_1^2
 -\frac12\omega _1^2\omega _2^2q_0^2.$$ Put $\Delta=\omega _2^2-\omega _1^2$ and define $$\begin{aligned}
 Q_1&=(p_1+\omega _2^2q_0)/\sqrt\Delta,&
 P_1&=(p_0+\omega _1^2q_1)/\sqrt\Delta,\nonumber\\
 Q_2&=(p_1+\omega _1^2q_0)/\sqrt\Delta,&
 P_2&=-(p_0+\omega _2^2q_1)/\sqrt\Delta.\end{aligned}$$ Direct Poisson-bracket calculation gives $\{Q_j,P_k\}=\delta_{jk}$ and zero cross brackets. Substitution gives $$H=-\frac12(P_1^2+\omega _1^2Q_1^2)
 +\frac12(P_2^2+\omega _2^2Q_2^2).$$ Thus our convention has a negative low-frequency mode and a positive high-frequency mode. This explicit check is the *canonical-sign owner*; changing either sign changes the theorem.

In the chamber above, the linear Hamiltonian flow is complete. If $\omega _1/\omega _2\in\mathbb Q$, every trajectory is periodic. If the ratio is irrational, exactly the equilibrium and single-mode trajectories are periodic, and each double-mode trajectory is dense on its invariant two-torus.

Equation (2) has the general solution $$x= a_1\cos\omega _1t+b_1\sin\omega _1t
  +a_2\cos\omega _2t+b_2\sin\omega _2t.$$ Equivalently, (5) preserves the two modal radii $R_j^2=Q_j^2+P_j^2/\omega_j^2$. If $\omega _1=gm,\omega _2=gn$ with coprime positive $m,n$, then $T=2\pi/g$ advances the two phases by $2\pi m,2\pi n$. It is a common period; a collapsed one-mode circle can have a smaller least period.

For irrational ratio, a periodic double-mode point would require both $\omega_jT\in2\pi\mathbb Z$, contradicting irrationality. Single-mode circles retain period $2\pi/\omega_j$. Kronecker's theorem makes the two-frequency phase orbit dense in $S^1\times S^1$, and the invertible map (4) carries that closure to the Ostrogradsky torus. Constant coefficients give completeness for all real time.

\>0

# Collision and sign boundaries

The normal map (4) is singular at collision, so the boundary must be solved from (2), not inferred by continuity.

For the real-factor equation $(D^2+\alpha)(D^2+\beta)x=0$, the distinct positive chamber is supplemented by the following exhaustive faces, up to interchange of $\alpha,\beta$.

1.  If $\alpha=\beta=\omega^2>0$, then $$x=(a+bt)\cos\omega t+(c+dt)\sin\omega t.$$ The first-order matrix has one size-two Jordan block at each of $\pm i\omega$; periodicity holds exactly when $b=d=0$.

2.  If $\alpha=0<\beta=\omega^2$, the basis is $1,t,\cos\omega t,\sin\omega t$; boundedness and periodicity hold exactly when the coefficient of $t$ vanishes. If $\alpha=\beta=0$, the basis is $1,t,t^2,t^3$, and only its constant subspace is bounded or periodic.

3.  A negative factor $-\nu^2$ contributes $e^{\nu t},e^{-\nu t}$. Pairing it with a positive factor, a zero factor, or a distinct negative factor supplies the corresponding direct union of bases. At the repeated negative face, the basis is $e^{\nu t},te^{\nu t},e^{-\nu t},te^{-\nu t}$. Every nonzero hyperbolic component is unbounded in at least one time direction. Hence the bounded/periodic subspace is the oscillatory plane for positive/negative factors, the constant line for zero/negative factors, and zero for two negative factors, repeated or distinct.

Each item is the kernel basis of its factored constant-coefficient polynomial. At the positive collision the characteristic polynomial is $(\lambda^2+\omega^2)^2$, while the nullity of the first-order matrix at each root $\pm i\omega$ is one. Algebraic multiplicity two and geometric multiplicity one force the asserted length-two Jordan blocks. The listed positive, zero, and negative cases exhaust both real factors.

This direct calculation is the *Jordan-boundary owner*. It prevents the imaginary repeated roots from being misreported as a diagonalizable stable oscillator.

\>1

# Natural quantum difference operator

Set $\hbar=1$. Let $h_\omega=(-\partial_Q^2+\omega^2Q^2)/2$, and let $\phi_n^{(\omega)}$ be its normalized Hermite basis. On $e_{n_1,n_2}=\phi_{n_1}^{(\omega_1)}\otimes\phi_{n_2}^{(\omega_2)}$, set $$\lambda_{n_1,n_2}=\omega _2(n_2+\tfrac12)-\omega _1(n_1+\tfrac12).$$ Define $\widehat H$ on the maximal diagonal domain $$\mathcal D(\widehat H)=\left\{\sum c_ne_n:
 (c_n)\in\ell^2(\mathbb N_0^2),\quad
 \sum |\lambda_n|^2|c_n|^2<\infty\right\}.$$

The operator $\widehat H=-h_{\omega_1}\otimes I+I\otimes h_{\omega_2}$ with domain (9) is self-adjoint and unbounded in both directions. If $\omega_1=gm,\omega_2=gn$ with $\gcd(m,n)=1$, then $$\sigma(\widehat H)=g(\mathbb Z+(n-m)/2),$$ and every eigenvalue has infinite multiplicity. If the ratio is irrational, all eigenvalues are simple and dense, $\sigma(\widehat H)=\mathbb R$, and all spectral measures are pure point.

The Hermite transform identifies (9) with the maximal domain of multiplication by a real sequence on $\ell^2(\mathbb N_0^2)$, hence the operator is self-adjoint. Finite coefficient arrays are a core. Sending either level to infinity gives the two unbounded directions.

In the rational case, $\lambda/g=nn_2-mn_1+(n-m)/2$. Bézout gives an integer solution to $nv-mu=k$ for each $k\in\mathbb Z$; adding $(n,m)L$ makes both indices nonnegative and produces infinitely many solutions. This proves (10) and its multiplicities.

In the irrational case, equality of two eigenvalues would make the frequency ratio rational unless both index differences vanish. Irrational-rotation density lets $\omega_2n_2-\omega_1n_1$ approximate every real number, with nonnegative indices chosen arbitrarily large. Thus the diagonal values are simple and dense and their closure, the operator spectrum, is $\mathbb R$. For $f=\sum c_ne_n$, the spectral measure is $\sum |c_n|^2\delta_{\lambda_n}$, proving pure-point type. This is the *dense pure-point owner*: dense eigenvalues are not discrete spectrum.

# Evidence and Route-A boundary

The executable receipt checks eight reduced rational frequency triples, seventy-two modal supports, 2,048 Hermite level pairs, three quadratic irrational controls, and seven degeneration rows. Independent symbolic work checks the symplectic matrix, Hamiltonian signs, characteristic polynomial, Jordan nullities, factor solutions, and lattice formula. Finite searches are regression tests only; the infinite results use Kronecker, Bézout, and the maximal diagonal-operator argument.

The evaluator gates say: A0 fails; A1 passes analytically; A2 and A3 fail; and A4 records a natural quantization. Overall, Route A is rejected. Frequency commensurability supplies no prime owner, Euler product, target functional equation, or target zero. Route B is false. The source operator is unbounded below and is not a Hilbert--Pólya operator.

# Source and claim boundary {#source-and-claim-boundary .unnumbered}

Pais and Uhlenbeck introduced the non-local-action model in *Physical Review* 79 (1950), 145--165, [doi:10.1103/PhysRev.79.145](https://doi.org/10.1103/PhysRev.79.145). Smilga analyzed higher-derivative ghost dynamics in *Nuclear Physics B* 706 (2005), 598--614, [doi:10.1016/j.nuclphysb.2004.10.037](https://doi.org/10.1016/j.nuclphysb.2004.10.037). Bolonek and Kosiński studied Hamiltonian structures in [arXiv:quant-ph/0501024](https://arxiv.org/abs/quant-ph/0501024). These sources establish lineage; every displayed claim above is rederived for the frozen convention. No priority claim is made.
