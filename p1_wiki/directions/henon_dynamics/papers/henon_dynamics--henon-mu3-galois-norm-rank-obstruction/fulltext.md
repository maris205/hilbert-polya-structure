---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-galois-norm-rank-obstruction"
canonical_tex: "henon_dynamics/henon_mu3_galois_norm_rank_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_galois_norm_rank_obstruction/paper/main.pdf"
source_sha256: "0910e57a4fb2316e9ed60353d6d8ae327de30ba421544f30cfedda32fb8edb93"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Normalized Hénon Galois Norm at the Riemann Critical Abscissa

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_galois_norm_rank_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_galois_norm_rank_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_galois_norm_rank_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_galois_norm_rank_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_galois_norm_rank_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We apply Galois descent to a conjugate-paired family of finite-field Hénon augmentation determinants whose trace fields have unbounded degree. The ordinary rational norm has virtual local degree $2(p-1)$ and therefore cannot come from a uniformly bounded-rank graded local operator. In contrast, the canonical field-degree-normalized logarithmic norm has first moment $-12/(p-1)$ and uniformly bounded higher moments. We prove that its Euler product converges locally uniformly and is holomorphic and nonzero in the half-plane $\operatorname{Re}s>1/2$. This advances the rigorously controlled Hénon Euler domain to the Riemann critical abscissa from the right without using zero data or fitted parameters. In the canonical clock, the local divisor line remains $\operatorname{Re}s=0$; moving it to $\operatorname{Re}s=1/2$ is an optional display that changes the proved convergence domain. The normalized local roots remain analytic normalized-log germs rather than ordinary rational or Fredholm determinants; continuation, a functional equation, and integral divisor multiplicities are left as explicit gates.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: 13 August 2026
title: A Normalized Hénon Galois Norm at the Riemann Critical Abscissa
```

## Markdown 正文

# Introduction

The coefficient-field obstruction for the full $\mu_3$-graded Hénon kernel is severe: at every split prime $p$, the conjugate-paired first moment generates $\mathbf Q(\zeta_p)^+$, of degree $(p-1)/2$. A conventional compatible system over one fixed number field is therefore impossible. Rather than choosing a different field independently at every prime, we test Galois trace and norm, the two minimal invariant descents.

The additive trace collapses the first moment to $-6$. The multiplicative norm preserves the complete local chronological determinant and restores rational coefficients, but its virtual degree grows linearly with $p$. The central observation of this paper is that dividing the canonical logarithm by the trace-field degree preserves the ordered moments while adding exactly enough first-order decay to move the Euler convergence boundary.

[\[thm:main\]]{#thm:main label="thm:main"} Let $G_p(z)$ be the origin-normalized field-degree root of the Galois norm of the conjugate-paired Hénon augmentation factor, as defined in [3](#sec:normalized){reference-type="ref" reference="sec:normalized"}. Then $$\mathcal G(s)=\prod_{p\equiv1\ (3)}G_p(p^{-s})$$ converges locally uniformly and is holomorphic and nonzero on $\operatorname{Re}s>1/2$.

The statement is both stronger and more limited than an ordinary Euler product theorem. It reaches the Riemann critical abscissa from the right, but the local factors are defined by a normalized logarithm on the unit disk. Their divisor orders need not be integral after division by $(p-1)/2$. Thus this paper proves an analytic normalized-log Euler germ, not a finite-dimensional rational determinant or a Fredholm determinant. The ordinary, unnormalized norm is the rational determinant in the construction.

Normalized determinants are natural in finite and von Neumann algebras [@FugledeKadison1952; @DeLaHarpe2000]; our construction does not yet claim such an operator realization. That distinction becomes the next theorem gate rather than a semantic choice.

# Rational norm descent

Fix a prime $p\equiv1\pmod3$ and set $$K_p=\mathbf Q(\zeta_p),\qquad L_p=K_p^+,
 \qquad d_p=[L_p:\mathbf Q]=(p-1)/2.$$ For the additive character $\psi_a(x)=\zeta_p^{ax}$, denote the C43 local augmentation factor by $D_{p,a}^{\rm aug}(z)$. It is a ratio of sector characteristic polynomials of unitary matrices, has value one at zero, and has finite zero and pole support on $|z|=1$.

Pair the inverse characters: $$E_p(z)=D_{p,1}^{\rm aug}(z)D_{p,-1}^{\rm aug}(z)\in L_p(z).$$ Complex conjugation exchanges the factors. Every $\sigma\in\operatorname{Gal}(L_p/\mathbf Q)$ replaces the additive character while leaving the chronological phase and matrix-power convention unchanged. Consequently $$\operatorname{Log}_0E_p(z)=-\sum_{n\ge1}\frac{B_{p,n}}n z^n,
 \qquad B_{p,n}\in L_p.$$

Define the ordinary rational norm $$N_p(z)=\operatorname{Norm}_{L_p/\mathbf Q}E_p(z).$$ Then $N_p(0)=1$ and $$\operatorname{Log}_0N_p(z)=-\sum_{n\ge1}\frac{C_{p,n}}n z^n,
 \qquad C_{p,n}=\operatorname{Tr}_{L_p/\mathbf Q}B_{p,n}.$$

[\[prop:vdeg\]]{#prop:vdeg label="prop:vdeg"} The ordinary norm has $$\operatorname{vdeg}N_p=4d_p=2(p-1).$$ If $Q_p\in\mathbf Q(z)$ satisfies $|\operatorname{vdeg}Q_p|\le M$ independently of $p$, then $$|\operatorname{vdeg}(Q_pN_p)|\ge2(p-1)-M.$$ Hence no uniformly bounded-rank family of finite-dimensional graded determinants can realize the ordinary norm.

Each paired conjugate has virtual degree four. Virtual degree is the order at infinity, hence is additive under products and unaffected by cancellation in a displayed numerator and denominator. The triangle inequality gives the second statement.

The first rational trace is exact: $$\label{eq:C1}
 C_{p,1}=-6.$$ It follows from the C44 zero-fiber identity $\#\{2x^3+2y^3+(1+\rho)xy=0\}=p-3$. Equation [\[eq:C1\]](#eq:C1){reference-type="eqref" reference="eq:C1"} does not imply that $(1-z)^{-6}$ is a complete local factor; higher moments are different.

# The normalized logarithmic root {#sec:normalized}

On $|z|<1$, all local sector determinants are nonzero. There is therefore a unique analytic logarithm $\operatorname{Log}_0N_p$ with value zero at the origin. Put $$\label{eq:Gp}
 G_p(z)=\exp\!\left(d_p^{-1}\operatorname{Log}_0N_p(z)\right),
 \qquad G_p(0)=1.$$ Its logarithmic moments are $$\log G_p(z)=-\sum_{n\ge1}\frac{c_{p,n}}n z^n,
 \qquad c_{p,n}=C_{p,n}/d_p.$$ In particular, $$\label{eq:c1}
 c_{p,1}=-\frac6{d_p}=-\frac{12}{p-1}.$$

The smooth-leading cubic Artin--Schreier estimate inherited from C43 gives, for every embedding of the paired moment, $$|B_{p,n}^{\sigma}|\le4\cdot4^n.$$ Averaging over all $d_p$ embeddings yields $$\label{eq:bound}
 |c_{p,n}|\le4\cdot4^n.$$

Equations [\[eq:c1\]](#eq:c1){reference-type="eqref" reference="eq:c1"} and [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"} have different analytic roles. The exceptional first moment has an extra factor $p^{-1}$; the uniform bound starts contributing only at $n=2$. Their intersection is the half-plane in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The detailed normal-convergence proof is in [7](#sec:convergence){reference-type="ref" reference="sec:convergence"}.

No parameter is adjusted to place the boundary at $1/2$. The exponent is forced by the exact trace-field degree and the fact that the first nontrivial uncontrolled repetition is $n=2$.

# Chronological second-moment control

The four-variable phase for the second determinant moment is $$\Phi_{p,2}
 =2\sum_{j=0}^3x_j^3+x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0.$$ This is the exact ordered two-step-kernel repetition. It is not a product of averaged transition matrices. Let $Z_{p,2}=\#\Phi_{p,2}^{-1}(0)$. Cyclotomic trace gives $$C_{p,2}=\frac{2Z_{p,2}}p-2p^2,
 \qquad c_{p,2}=\frac{2C_{p,2}}{p-1}.$$

          $p$      7     13     19      31   37      43   61   67      73   79      97
  ----------- ------ ------ ------ ------- ---- ------- ---- ---- ------- ---- -------
    $C_{p,2}$   $-6$   $-6$   $-6$   $-30$   18   $-54$   18   42   $-30$   42   $-30$

The ledger proves that canceling the first coefficient with $(1-z)^6$ is not an all-order Tate cancellation. It does not prove a distribution law or a natural boundary.

Over characteristic zero with $\rho^2+\rho+1=0$, the affine singular ideal of $\Phi_{p,2}$ has only the origin, and its projective leading cubic is smooth. Thus the second moment is a legitimate fixed-dimensional cohomological problem; irregular finite-prime values should not be promoted to random-noise evidence.

# Determinant and boundary firewall

The function $G_p$ in [\[eq:Gp\]](#eq:Gp){reference-type="eqref" reference="eq:Gp"} is canonically single-valued on the open unit disk. Suppose $N_p$ has divisor valuation $m$ at a boundary point. Analytic continuation of the chosen root has local order $m/d_p$. A single-valued meromorphic function requires this order to be integral. Consequently an ordinary rational root can exist only if every divisor valuation of $N_p$ is divisible by $d_p$.

This exact divisibility condition separates three statements:

1.  the normalized logarithmic germ exists on $|z|<1$;

2.  an ordinary rational or Fredholm determinant would require additional integral-divisor and operator theorems;

3.  global continuation across $\operatorname{Re}s=1/2$ would additionally require control of cross-prime divisor coincidences and monodromy.

Only the first is proved here. Under the optional display $z=p^{1/2-s}$, local unit-circle divisors lie on $\operatorname{Re}s=1/2$, but this geometric observation is not a natural-boundary theorem. In the canonical clock $z=p^{-s}$ used in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}, those divisors lie on $\operatorname{Re}s=0$. Moreover, after the optional shift the same $n\ge2$ majorant proves convergence only on $\operatorname{Re}s>1$, so the shift is a divisor display rather than part of the critical-abscissa theorem. HCS-C46 tests the divisor-integrality condition exactly at the first split prime.

# Route-A evaluation and conclusion

The normalized norm has exact Hénon chronological moments and a locally uniform analytic normalized-log Euler germ. Its domain reaches the Riemann critical abscissa from the right. The ordinary norm supplies the rational determinant underlying the A2 label; the normalized root has no determinant operator yet. The primes remain arithmetic fibers rather than primitive orbits of one real system, and no continuation, Gamma factor, functional equation, or Hilbert--Pólya operator is known.

The strict evaluation is $$\begin{aligned}
 \mathrm{A1}&=\mathrm{WEAK},
 &\mathrm{A2}&=\mathrm{ANALYTIC\_DETERMINANT},\\
 \mathrm{A3}&=\mathrm{PARTIAL\_ANALYTIC\_STRUCTURE},
 &\mathrm{A4}&=\mathrm{NATURAL\_QUANTIZATION}.\end{aligned}$$ Overall the project is `ROUTE_A_EXPLORATORY`. It does not authorize Route B.

The result changes the direction of the program. Fixed-field descent is impossible and ordinary norm has growing virtual rank, yet the canonical normalized trace does not collapse: it improves the analytic domain. The next gates are therefore structural rather than numerical. First decide the ordinary determinant promotion by an exact perfect-power and local-branch test. If that fails, decide whether a normalized-trace operator category can carry the signed chronological sequence without falsely invoking ordinary trace-class theory.

# Normal convergence {#sec:convergence}

Let $K$ be compact in $\operatorname{Re}s>1/2$, and choose $\sigma_0>1/2$ with $\operatorname{Re}s\ge\sigma_0$ on $K$. Every fixed local factor is analytic because $|p^{-s}|<1$. We may remove finitely many primes so that $4p^{-\sigma_0}\le1/2$ in the remaining tail.

The $n=1$ contribution to the logarithm is bounded uniformly on $K$ by $$\sum_p\frac{12p^{-\sigma_0}}{p-1},$$ which converges by comparison with $\sum_pp^{-1-\sigma_0}$. Using [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}, the higher repetitions satisfy $$\begin{aligned}
 \sum_p\sum_{n\ge2}\frac{|c_{p,n}|}{n}p^{-n\sigma_0}
 &\le4\sum_p\sum_{n\ge2}\frac{(4p^{-\sigma_0})^n}{n}\\
 &\ll\sum_pp^{-2\sigma_0}<\infty.\end{aligned}$$ Thus the logarithmic series converges normally. Its exponential is holomorphic and nonzero, proving [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.
