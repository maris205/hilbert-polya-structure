---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-krawtchouk-xx-mirror-inversion-route-a"
canonical_tex: "henon_dynamics/henon_krawtchouk_xx_mirror_inversion_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_krawtchouk_xx_mirror_inversion_route_a/paper/main.pdf"
source_sha256: "03f6ba3b6e181ce0c4e11c865f99055f2f64feceae508512d7626d188abe5419"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Krawtchouk XX Chain: Exact Propagation, Perfect Mirror Transfer, and the Full Fermionic Phase

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_krawtchouk_xx_mirror_inversion_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_krawtchouk_xx_mirror_inversion_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_krawtchouk_xx_mirror_inversion_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_krawtchouk_xx_mirror_inversion_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We identify the engineered open XX chain with the spin- $N/2$ representation of $J_x$, obtaining its complete Krawtchouk spectrum and propagator for every chain length. An endpoint excitation follows an exact binomial law and is mirrored perfectly at time $\pi/\Omega$. \>0 Fermionic second quantization then gives the propagator in every excitation sector and exposes the wedge-reordering sign that a one-particle argument cannot determine. \>1 We close all size, coupling, field, and revival boundaries and distinguish a sectorwise phase from a global Fock-space revival. Finite exact ledgers audit the formulas; representation theory proves the all-size statements.
author:
- 'HCS-C366 source-local theorem package'
date: 'September 4, 2026'
title: |
  A Krawtchouk XX Chain: Exact Propagation, Perfect Mirror Transfer,\
  and the Full Fermionic Phase
```

## Markdown 正文

trailerid \[\<C3662026090400000000000000000000\>\<C3662026090400000000000000000000\>\]

\>1

# Frozen chain and one-particle spectrum

On the ordered basis $\{|j\rangle:0\le j\le N\}$, let $$h_N=\frac{\Omega}{2}\sum_{j=0}^{N-1}\sqrt{(j+1)(N-j)}
 (|j\rangle\langle j+1|+|j+1\rangle\langle j|),\qquad \Omega>0.$$ Identifying $|j\rangle$ with the $J_z$-weight $j-N/2$, the standard matrix element of $J_x$ makes (1) exactly $\Omega J_x$.

The simple eigenvalues are $$E_r=\Omega(N/2-r),\qquad 0\le r\le N.$$ If $$K_r(j)=\sum_\ell(-1)^\ell\binom j\ell\binom{N-j}{r-\ell},$$ then normalized eigenvectors have components $$v_r(j)=\frac{\sqrt{\binom Nj}K_r(j)}{\sqrt{2^N\binom Nr}}.$$

Spin rotation sends the $J_z$ weights to the $J_x$ weights, proving (2). Pascal identities in the tridiagonal recurrence prove $h_Nv_r=E_rv_r$. Coefficient extraction from $$\sum_j\binom Nj(1-z)^j(1+z)^{N-j}(1-w)^j(1+w)^{N-j}
=2^N(1+zw)^N$$ gives $\sum_j\binom NjK_r(j)K_s(j)=2^N\binom Nr\delta_{rs}$. Thus the $N+1$ displayed vectors are a complete orthonormal basis.

For $U_1(t)=e^{-ith_N}$, $$\langle k|U_1(t)|0\rangle=(-i)^k\sqrt{\binom Nk}
 \sin^k\!\frac{\Omega t}{2}\cos^{N-k}\!\frac{\Omega t}{2}.$$ At $t_*=\pi/\Omega$, $U_1(t_*)=(-i)^NR$, where $R|j\rangle=|N-j\rangle$.

The spin-$N/2$ module is the symmetric power of $N$ spin halves. Expanding $e^{-it\Omega\sigma_x/2}|0\rangle=\cos(\Omega t/2)|0\rangle-
i\sin(\Omega t/2)|1\rangle$ in normalized symmetric weights gives (5). At angle $\pi$, every factor flips with phase $-i$.

This identity is the *single-particle propagator owner*. In particular, at $t_*/2$ the endpoint-start probabilities are $2^{-N}\binom Nk$.

\>0

# The many-body theorem

Let $H_N=d\Gamma(h_N)$, and order every fermionic basis wedge increasingly.

On the $m$-particle sector, $$e^{-itH_N}=\bigwedge^m U_1(t).$$ At $t_*$, $$|j_1<\cdots<j_m\rangle\mapsto
(-i)^{mN}(-1)^{m(m-1)/2}
|N-j_m<\cdots<N-j_1\rangle .$$ For $S\subseteq\{0,\ldots,N\}$, $|S|=m$, the corresponding energy is $$E_S=\Omega\left(mN/2-\sum_{r\in S}r\right),$$ and all degeneracies are encoded by $$\prod_{r=0}^N(1+yq^r)=
\sum_{m=0}^{N+1}y^mq^{m(m-1)/2}
\mathcal G_{N+1,m}(q).$$ Here the Gaussian $q$-binomial polynomial is fixed by $$\mathcal G_{n,m}(q)=\mathcal G_{n-1,m}(q)+
q^{n-m}\mathcal G_{n-1,m-1}(q),
\qquad
\mathcal G_{n,0}(q)=\mathcal G_{n,n}(q)=1,$$ with out-of-range entries zero.

A number-conserving quadratic fermion Hamiltonian induces the exterior power of its one-particle unitary. At $t_*$, each occupied orbital contributes $(-i)^N$. Reflection reverses all $m$ wedge factors, and restoring increasing order needs $m(m-1)/2$ transpositions. Exterior products of the one-particle eigenbasis prove (8).

Let $A_{N,m}(q)$ be the coefficient of $y^m$ in the product in (9). Splitting subsets according to whether they contain $N$ gives $A_{N,m}=A_{N-1,m}+q^N A_{N-1,m-1}$. The expression $q^{m(m-1)/2}\mathcal G_{N+1,m}(q)$ satisfies the same recurrence: the second term of (10) supplies $q^{N+1-m}$, and shifting the prefactor from $m$ to $m-1$ supplies $q^{m-1}$. The empty product is the common base case, so induction proves (9) coefficient by coefficient.

Equation (7) is the *many-body phase owner*; deleting its reordering sign changes the unitary in entire excitation sectors.

\>1

# Boundary and revival audit

For $N=0$, reflection is the one-site identity. For $\Omega=0$, the Hamiltonian vanishes and distinct endpoints do not transfer. Negative $\Omega$ reverses time and replaces $(-i)^N$ by $i^N$ at positive time $\pi/|\Omega|$. A uniform field $B\widehat m$ contributes only $e^{-imBt}$ in sector $m$.

For the field-shifted model the exact Fock operators are $$U_B(2\pi/|\Omega|)=
 e^{-i(2\pi B/|\Omega|)\widehat m}(-1)^{N\widehat m},\qquad
 U_B(4\pi/|\Omega|)=e^{-i(4\pi B/|\Omega|)\widehat m}.$$ The first is identity exactly when $2B/|\Omega|+N\in2\mathbb Z$; the second is identity exactly when $2B/|\Omega|\in\mathbb Z$. In particular, for the unshifted model $B=0$, the $2\pi/|\Omega|$ propagator is identity for even $N$ and fermion parity for odd $N$, while $4\pi/|\Omega|$ is always identity. These conditions include the vacuum sector, so a sectorwise phase is not silently promoted to a global Fock revival. This is the *revival-boundary owner*. No persistence of perfect transfer under a generic coupling perturbation is asserted.

\>1

# Evidence and Route-A boundary

The executable receipt covers 66 spectral rows, all 65,534 fermionic subsets through $N=14$, complete energy histograms, 231 formal all-time endpoint cells, and all 136 Gaussian-polynomial rows through order 15. Independent code and SymPy reconstruct the formulas; finite checks do not replace the proofs.

The strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ Natural quantization does not automatically furnish arithmetic ownership or an analytic Euler-product mechanism. Overall, Route A is rejected and Route B is false. The finite source Hamiltonian has no rational-prime owner, logarithmic-prime clock, target Euler product, divisor, functional equation, zero match, or Hilbert--Pólya interpretation. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

\>1

# Source and claim boundary {#source-and-claim-boundary .unnumbered}

Christandl, Datta, Ekert, and Landahl introduced fixed-coupling perfect transfer networks in *Physical Review Letters* 92 (2004), 187902, [doi:10.1103/PhysRevLett.92.187902](https://doi.org/10.1103/PhysRevLett.92.187902). Albanese, Christandl, Datta, and Ekert treated mirror inversion in *Physical Review Letters* 93 (2004), 230502, [doi:10.1103/PhysRevLett.93.230502](https://doi.org/10.1103/PhysRevLett.93.230502). They establish lineage; the frozen formulas above are rederived, and no literature-priority claim is made. \>1
