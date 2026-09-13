---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-square-wave-hill-floquet-route-a"
canonical_tex: "henon_dynamics/henon_square_wave_hill_floquet_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_square_wave_hill_floquet_route_a/paper/main.pdf"
source_sha256: "4a38c8fe5d80eaac393772ebe1ce8703e0b6a4710a7bf0a89c870bbf158d8227"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Floquet--Jordan Atlas for the Two-Step Hill Oscillator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_square_wave_hill_floquet_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_square_wave_hill_floquet_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_square_wave_hill_floquet_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_square_wave_hill_floquet_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify the periodic two-step Hill oscillator for arbitrary real segment coefficients, including oscillatory, zero-frequency, and hyperbolic pieces. Entire segment functions give one exact $SL(2,\mathbb R)$ monodromy and a closed Floquet discriminant whose elliptic and hyperbolic regions are complete. \>0 At the parabolic boundary we distinguish scalar $\pm I$ from nontrivial Jordan growth, and close every integer iterate and Floquet rate. An independent entire-series checker verifies 900 all-sign transfers. \>1 All zero-duration, constant-coefficient, and segment-order faces are included. No arithmetic or target-determinant claim is made.
author:
- HCS Research Program
date: 31 August 2026(revision 2)
title: |
  A Complete Floquet--Jordan Atlas\
  for the Two-Step Hill Oscillator
```

## Markdown 正文

suppressoptionalinfo 611 trailerid \[\<C2622026083100000000000000000000\>\<C2622026083100000000000000000000\>\]

Hill's periodic-coefficient equation [@Hill1886] and the two-step piecewise-constant resonance setting [@Golubev1997] provide historical context. The all-sign transfer and complete boundary theorem below are derived directly.

# One entire transfer for all segment signs

Fix the periodic equation $$y''+k(t)y=0,\qquad
 k(t)=\begin{cases}k_1,&0\le t<\tau_1,\\
 k_2,&\tau_1\le t<T,\end{cases}
 \quad T=\tau_1+\tau_2>0,                 \label{eq:hill}$$ with $k_j\in\mathbb R$ and $\tau_j\ge0$. Define entire functions $$C(k,t)=\sum_{m\ge0}\frac{(-k)^mt^{2m}}{(2m)!},\qquad
 S(k,t)=\sum_{m\ge0}\frac{(-k)^mt^{2m+1}}{(2m+1)!}.      \label{eq:CS}$$ They obey $C_t=-kS$, $S_t=C$, and $C^2+kS^2=1$. Hence the state $Y=(y,y')^{\mathsf T}$ advances through one constant segment by $$\Phi(k,t)=\begin{pmatrix}C&S\\-kS&C\end{pmatrix},
 \qquad \det\Phi=1.                                      \label{eq:phi}$$ For $k>0$, $k=0$, and $k<0$, this is respectively the cosine--sine, shear, and cosh--sinh transfer, without a square-root branch convention.

# Complete stability and boundary theorem

Put $M=\Phi(k_2,\tau_2)\Phi(k_1,\tau_1)$ and write $C_j,S_j$ for the two segment values. Direct multiplication gives $$\det M=1,\qquad
 \Delta=\operatorname{tr}M=2C_1C_2-(k_1+k_2)S_1S_2.                  \label{eq:delta}$$

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For the oscillator [\[eq:hill\]](#eq:hill){reference-type="eqref" reference="eq:hill"}:

1.  If $|\Delta|<2$, the monodromy is elliptic and every solution is bounded. Its Floquet angle per unit time is $T^{-1}\arccos(\Delta/2)$.

2.  If $|\Delta|>2$, the multipliers are a real reciprocal pair. Generic solutions grow exponentially, one forward eigenline decays, and the positive growth rate is $T^{-1}\operatorname{arcosh}(|\Delta|/2)$.

3.  If $\Delta=\pm2$ and $M=\pm I$, every solution is periodic or antiperiodic over one coefficient period. If instead $M\ne\pm I$, then $\operatorname{rank}(M\mp I)=1$: one Floquet line is bounded and generic solutions grow linearly, with alternating sign on the minus face.

For every $n\ge1$, $$M^n=U_{n-1}(\Delta/2)M-U_{n-2}(\Delta/2)I.              \label{eq:cheb}$$ Here $U_{-1}=0$ and $U_0=1$, so [\[eq:cheb\]](#eq:cheb){reference-type="eqref" reference="eq:cheb"} includes $n=1$.

#### Proof.

The characteristic polynomial is $\lambda^2-\Delta\lambda+1$. Its roots are distinct unit conjugates for $|\Delta|<2$ and distinct real reciprocals for $|\Delta|>2$, proving the first two cases. At trace $\pm2$, a real $2\times2$ determinant-one matrix is either $\pm I$ or has one Jordan block; its powers distinguish bounded from linear growth. Cayley--Hamilton and the recurrence $U_n(x)=2xU_{n-1}(x)-U_{n-2}(x)$ prove [\[eq:cheb\]](#eq:cheb){reference-type="eqref" reference="eq:cheb"}.

=0 The baseline ends with the exact monodromy and stability theorem. Executable receipts and the degenerate-face ledger enter only in later revisions.

\>0

# Exact witnesses and independent receipt

Trace alone does not settle the parabolic dynamics. Four exact sentinels are $$I,\quad -I,\quad
 \begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
 \begin{pmatrix}-1&-1\\0&-1\end{pmatrix};              \label{eq:sentinels}$$ the last two have generic linear growth. A hyperbolic exact control is $$\Phi(-1,\log2)=
 \begin{pmatrix}5/4&3/4\\3/4&5/4\end{pmatrix},$$ with multipliers $2$ and $1/2$.

The producer evaluates all $6^2\cdot5^2=900$ parameter rows with $k_j\in\{-4,-1,0,1,4,9\}$ and $\tau_j\in\{0,1/4,1/2,1,3/2\}$. The checker does not call its trigonometric or hyperbolic implementation; it rebuilds $C,S$ from 90-term power series, then tests determinant, [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"}, classification, and every power through $n=12$.

  gate                        count                             result
  ------------------------- ------- ----------------------------------
  all-sign transfer rows        900      19,849 independent assertions
  exact boundary matrices         6      scalar/Jordan/hyperbolic PASS
  SymPy identities              289   determinant/trace/Chebyshev PASS
  hostile mutations              41                        41 rejected

Finite rows validate implementation and boundary conventions; the continuum classification follows from Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}.

\>1

# Faces, collisions, and Route-A stop

Equations [\[eq:CS\]](#eq:CS){reference-type="eqref" reference="eq:CS"}--[\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"} remain valid when either $k_j$ is zero or negative and when either duration vanishes. Equal coefficients collapse to the constant-coefficient transfer over total time. Swapping the segments can change $M$, but $\operatorname{tr}(\Phi_2\Phi_1)=\operatorname{tr}(\Phi_1\Phi_2)$, so it cannot change the Floquet class.

C110 (forced Hénon Floquet data), C178 (harmonic strobe), C218 (Kelvin--Voigt), C249 (Van der Pol), and C252 (relay oscillator) do not own this two-step linear Hill theorem. Earlier "Hill determinants" are orbit Hessians, not equation [\[eq:hill\]](#eq:hill){reference-type="eqref" reference="eq:hill"}. This is collision bookkeeping, not a priority claim.

The strict assessment is $$\texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)},$$ with `ROUTE_A_REJECTED`, Route B false, and scope `NO_BAD_EULER_OR_ROOT_NUMBER`. The source characteristic polynomial is not a target determinant. No arithmetic local data, Euler factor, root number, automorphy, target divisor or functional equation, target zero match, or Hilbert--Pólya operator is claimed.

# Conclusion and limitations

The all-sign entire transfer, one discriminant, the scalar/Jordan split, and the Chebyshev law together close the two-step family. This does not classify arbitrary periodic coefficients, nonlinear perturbations, or every initial condition's forward behavior in the hyperbolic case.

9 G. W. Hill, "On the part of the motion of the lunar perigee which is a function of the mean motions of the sun and moon," *Acta Mathematica* 8 (1886), 1--36, [doi:10.1007/BF02417081](https://doi.org/10.1007/BF02417081). Y. F. Golubev, "Resonances of linear differential equations with piecewise constant coefficients," Keldysh Institute Preprint 43 (1997), [MathNet record](https://www.mathnet.ru/eng/ipmp1431).
