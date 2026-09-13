---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-noisy-mean-field-kuramoto-phase-transition-route-a"
canonical_tex: "henon_dynamics/henon_noisy_mean_field_kuramoto_phase_transition_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_noisy_mean_field_kuramoto_phase_transition_route_a/paper/main.pdf"
source_sha256: "0b5effafa5dd5eb068e9b743c5d590f2d63567bdc8a5b8ea4d6ec09b63e2459a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Stationary Phase Atlas for the Noisy Mean-Field Kuramoto Equation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_noisy_mean_field_kuramoto_phase_transition_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_noisy_mean_field_kuramoto_phase_transition_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_noisy_mean_field_kuramoto_phase_transition_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_noisy_mean_field_kuramoto_phase_transition_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For identical frequencies, positive noise, and attractive sinusoidal mean-field coupling, one theorem joins global classical probability flow, an exact free-energy dissipation law, exhaustion of stationary densities by von Mises profiles, the sharp synchronization threshold, the complete uniform Fourier spectrum, and a two-term critical expansion. The decisive Bessel quotient is proved strictly decreasing by an explicit positive-series coefficient pairing, which simultaneously closes the strict Turán inequality. Exact rational ledgers certify finite Bessel tails, stationary root brackets, and Fourier conventions; they do not replace the analytic continuum proof. No priority or arithmetic-target claim is made.
author:
- 'HCS-C347 source-local reconstruction'
date: 3 September 2026
title: |
  A Complete Stationary Phase Atlas for the\
  Noisy Mean-Field Kuramoto Equation
```

## Markdown 正文

**Revision certificate.** =0 Flow, energy, and stationary-flux closure. =1 Round-one Turan threshold and Fourier closure. Round-two critical expansion and evidence closure.

# Frozen equation and main result

Let $\mathbb T=\mathbb R/(2\pi\mathbb Z)$, use Lebesgue measure $d\theta$, and normalize $\int_{\mathbb T}p\,d\theta=1$. Fix $D>0$, $K\geq0$, and define $$z[p]=\int_{\mathbb T}e^{i\theta}p(\theta)\,d\theta
      =r[p]e^{i\psi[p]},\qquad
 b[p](\theta)=Kr[p]\sin(\psi[p]-\theta).$$ The phase is immaterial when $r=0$. Our equation is $$\partial_t p=Dp_{\theta\theta}-\partial_\theta(b[p]p).
 \label{eq:pde}$$

[\[thm:main\]]{#thm:main label="thm:main"} Let $0<\gamma<1$ and let nonnegative $p_0\in C^{2+\gamma}(\mathbb T)$ have unit mass.

1.  Equation [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} has a unique global classical probability solution. It is strictly positive for $t>0$.

2.  For positive times the free energy $$\mathcal F[p]=D\int_{\mathbb T}p\log p\,d\theta-\frac K2|z[p]|^2$$ satisfies $$\mathcal F[p(t)]-\mathcal F[p(s)]
     =-\int_s^t\!\int_{\mathbb T}p
     \left|\partial_\theta\left(D\log p-KC[p]\right)\right|^2d\theta\,d\tau,
     \label{eq:dissipation}$$ where $C[p](\theta)=\int\cos(\theta-\phi)p(\phi)d\phi$. One may take $s=0$ if $p_0>0$.

3.  Every nonnegative $C^2$ stationary probability density is uniform, $p_*=1/(2\pi)$, or belongs to $$q_{\kappa,\psi}(\theta)=
     \frac{e^{\kappa\cos(\theta-\psi)}}{2\pi I_0(\kappa)},\qquad
     \kappa=\frac KD\frac{I_1(\kappa)}{I_0(\kappa)}.             \label{eq:vm}$$ For $K\leq2D$, only $p_*$ exists. For $K>2D$, there is exactly one $\kappa>0$, and $\psi\in\mathbb T$ gives its complete rotation orbit.

4.  At $p_*$, the constant mass mode has eigenvalue zero, the real first-harmonic plane has eigenvalue $K/2-D$, and the real harmonic plane of order $n\geq2$ has eigenvalue $-Dn^2$. The constant direction is removed on the probability tangent space.

5.  If $\delta=K/D-2\downarrow0$ along the nonuniform branch, then $$\kappa^2=4\delta+\frac23\delta^2+O(\delta^3),\qquad
     r^2=\delta-\frac56\delta^2+O(\delta^3).$$

# Global probability flow and dissipation

The map $p\mapsto b[p]$ uses only two first Fourier coefficients and is smooth and locally Lipschitz between the relevant Hölder spaces. Standard heat-semigroup iteration gives a unique local classical solution. Mass conservation follows by integrating [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"}; comparison preserves nonnegativity, and the strong maximum principle gives strict positivity for positive time.

This local solution cannot blow up at finite time. For probability densities, $\lVert\partial_\theta^j b[p]\rVert_\infty\leq K$ for every $j$. At a spatial maximum of $$p_t=Dp_{\theta\theta}-b[p]p_\theta-(\partial_\theta b[p])p$$ we obtain $\partial_t\max p\leq K\max p$, whence $\lVert p(t)\rVert_\infty\leq e^{Kt}\lVert p_0\rVert_\infty$ on finite intervals. Periodic parabolic Schauder estimates now give continuation through every finite time.

Because $\partial_\theta C[p]=b[p]/K$, with the zero-coupling case read directly, equation [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} is $$p_t=\partial_\theta\left[p\,\partial_\theta
       \left(D\log p-KC[p]\right)\right].                  \tag{2}$$ The first variation of $-K|z[p]|^2/2$ is $-KC[p]$. Multiplying (2) by the chemical potential and integrating by parts proves [\[eq:dissipation\]](#eq:dissipation){reference-type="eqref" reference="eq:dissipation"}. Starting at $s>0$ handles initial zeros.

# Stationary-flux exhaustion

A nonnegative stationary $C^2$ density is positive by the elliptic strong maximum principle. Its flux $$J=b[p]p-Dp_\theta$$ is constant. Division by $p$ and one circuit around $\mathbb T$ give $$0=\int\frac{p_\theta}{p}
   =\frac1D\int b[p]-\frac JD\int\frac{d\theta}{p(\theta)}.$$ The sine drift integrates to zero and the last integral is positive, so $J=0$. Therefore $$\partial_\theta\log p=\frac{Kr}{D}\sin(\psi-\theta)
 =\partial_\theta\left(\frac{Kr}{D}\cos(\theta-\psi)\right).$$ Normalization gives the von Mises form in [\[eq:vm\]](#eq:vm){reference-type="eqref" reference="eq:vm"}. Conversely its first moment is $$z[q_{\kappa,\psi}]=e^{i\psi}R(\kappa),\qquad
 R(\kappa)=I_1(\kappa)/I_0(\kappa),$$ so zero flux is equivalent to $\kappa=(K/D)R(\kappa)$. This proves the stationary list in both directions.

\>0

# Strict Turán inequality and the phase threshold

[\[lem:bessel\]]{#lem:bessel label="lem:bessel"} The function $q(\kappa)=I_1(\kappa)/(\kappa I_0(\kappa))$ decreases strictly from $1/2$ to zero on $(0,\infty)$. Equivalently, $$I_1(\kappa)^2-I_0(\kappa)I_2(\kappa)>0.                  \tag{3}$$

Put $x=\kappa^2$, $A(x)=I_1(\sqrt x)/\sqrt x$, and $B(x)=I_0(\sqrt x)$. Their positive entire coefficients satisfy $$A=\sum_{m\geq0}a_mx^m,\quad B=\sum_{m\geq0}b_mx^m,\quad
 \frac{a_m}{b_m}=\frac1{2(m+1)}.$$ Pairing indices in the derivative numerator yields $$A'B-AB'=\sum_{m>n}(m-n)(a_mb_n-a_nb_m)x^{m+n-1}<0.       \tag{4}$$ Thus $q=A/B$ is strictly decreasing and $q(0+)=1/2$. Moreover $0<R(\kappa)<1$, since it is the strict expectation of $\cos\theta$ under a positive von Mises density, so $q(\kappa)<1/\kappa\to0$.

Termwise Bessel recurrences give $R'=1-R^2-R/\kappa$ and $I_2=I_0-2I_1/\kappa$. Consequently $q'<0$ is equivalent to $\kappa(1-R^2)<2R$, and multiplication by $I_0^2/\kappa$ gives (3). Hence the strict Turán inequality is proved rather than assumed.

For $a=K/D>0$, a nonzero stationary solution obeys $q(\kappa)=1/a$. Lemma [\[lem:bessel\]](#lem:bessel){reference-type="ref" reference="lem:bessel"} gives no solution for $a\leq2$ and exactly one for $a>2$, completing the transition proof.

# Complete uniform Fourier linearization

Write $p=p_*+\varepsilon u$, $\int u=0$. The linearization is $$Lu=Du_{\theta\theta}-p_*\partial_\theta b[u],\qquad
 b[u]=K\operatorname{Im}(z[u]e^{-i\theta}).               \tag{5}$$ For $u=a\cos\theta+c\sin\theta$, $z[u]=\pi(a+ic)$, and the last term in (5) is $Ku/2$. Every harmonic of order $n\geq2$ has zero first moment, leaving $-Dn^2$. Constants give mass conservation. This proves every eigenvalue and real multiplicity stated in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

\>1

# Critical amplitude with a rigorous remainder

Exact series division gives $$\frac{R(\kappa)}\kappa
 =\frac12-\frac{\kappa^2}{16}+\frac{\kappa^4}{96}
  -\frac{11\kappa^6}{6144}+O(\kappa^8).                  \tag{6}$$ With $x=\kappa^2$, the left side of $(2+\delta)R(\sqrt x)/\sqrt x=1$ is analytic near the origin, and its $x$-derivative at $(x,\delta)=(0,0)$ is $-1/8$. The analytic implicit-function theorem applies. Coefficient matching gives $$x=4\delta+\frac23\delta^2+\frac1{18}\delta^3+O(\delta^4).$$ Since $\kappa=(2+\delta)r$, $$r^2=\delta-\frac56\delta^2+\frac{43}{72}\delta^3+O(\delta^4),$$ which proves the asserted expansion.

# Exact evidence and boundaries

The deterministic receipt uses rational arithmetic only.

  finite panel                                         rows
  -------------------------------------------------- ------
  positive $I_0$ and $I_1/\kappa$ coefficients           17
  formal coefficients of $R/\kappa$                       9
  certified positive-series Bessel tail brackets          7
  certified nonzero self-consistency root brackets        4
  uniform real Fourier blocks                           162

After term 20, the positive-series tails are bounded by next-term geometric majorants. An independent checker reconstructs all 199 rows without importing the producer; a 60-check symbolic lane, two-directory byte replay, 71 hostile mutations, and strict JSON/YAML gates protect the artifact. The finite receipt does not prove the continuum theorem.

At $K=0$ the model is the heat equation. At $K=2D$ the first harmonic is neutral but Lemma [\[lem:bessel\]](#lem:bessel){reference-type="ref" reference="lem:bessel"} excludes nonuniform stationary profiles. Above threshold there is one concentration and an $S^1$ phase orbit. The face $D=0$ is excluded: no atomic-state theorem is inferred. We claim neither general-initial-data convergence nor a rate, Hopf or time-periodic branches, disorder, delay, inertia, or finite-particle results.

# Source and Route-A boundary

Sakaguchi's noisy globally coupled oscillator paper[@sakaguchi] and the reversible mean-field rotator analysis of Bertini, Giacomin, and Pakdaman[@bertini] fix the source lineage. The present derivation is a source-local reconstruction and makes no priority claim. The model has no arithmetic origin or prime clock, primitive arithmetic orbit ledger, target determinant, target analytic continuation, or natural target-zero quantization. Its tuple is $$(A0_{\rm FAIL},A1_{\rm FAIL},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FAIL}),$$ the verdict is Route-A rejected, and Route B is false. Bessel and Fourier data are not target arithmetic local data, Euler factors, root numbers, automorphy, a target divisor, target zeros, or a Hilbert--Pólya operator.

9 H. Sakaguchi, Cooperative phenomena in coupled oscillator systems under external fields, *Progress of Theoretical Physics* **79** (1988), 39--46. <https://doi.org/10.1143/PTP.79.39>.

L. Bertini, G. Giacomin, and K. Pakdaman, Dynamical aspects of mean field plane rotators and the Kuramoto model, *Journal of Statistical Physics* **138** (2010), 270--290. <https://doi.org/10.1007/s10955-009-9908-9>.
