---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-qwz-thouless-chern-pump-route-a"
canonical_tex: "henon_dynamics/henon_qwz_thouless_chern_pump_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_qwz_thouless_chern_pump_route_a/paper/main.pdf"
source_sha256: "713579cbeda2027dc47e82f23815eb1b2f95fc4ad21618d0101652614f3decfb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Chern-Phase Atlas for the QWZ Thouless Pump

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_qwz_thouless_chern_pump_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_qwz_thouless_chern_pump_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_qwz_thouless_chern_pump_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_qwz_thouless_chern_pump_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a two-band pump on the Bloch torus we prove the exact spectrum, direct gap, all lower-band Chern phases, and every gap-closing Dirac jump. The transported charge statement is made only in the filled-band adiabatic limit. Independent symbolic, degree, and lattice-gauge receipts audit the convention-sensitive signs. This revision is the **exact Bloch-gap owner**.
author:
- 'HCS-C356 / HEN-O340'
date: 3 September 2026
title: 'An Exact Chern-Phase Atlas for the QWZ Thouless Pump'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3562026090300000000000000000000\>\<C3562026090300000000000000000000\>\]

# Model and complete gap atlas

Orient $\mathbb T^2$ by $dk\wedge d\tau$ and define $$\label{eq:model}
 H_m(k,\tau)=d_m(k,\tau)\cdot\sigma,\qquad
 d_m=(\sin k,\sin\tau,m+\cos k+\cos\tau).$$ Here $m\in\mathbb R$ and both angular variables have period $2\pi$. Whenever $d_m$ is nonzero, let $n=d_m/|d_m|$ and $P_-=(I-n\cdot\sigma)/2$.

[\[thm:main\]]{#thm:main label="thm:main"} The fibre spectrum is $\{-|d_m|,+|d_m|\}$. The family is gapped exactly for $m\notin\{-2,0,2\}$, with direct gap $$G(m)=2\min\{|m+2|,|m|,|m-2|\}.$$ On a gapped chamber $P_-$ is a smooth rank-one complex line bundle. With $$\label{eq:c1}
 c_1(P_-)=\frac1{2\pi i}\int_{\mathbb T^2}
 \operatorname{Tr}\!\left(P_-[\partial_kP_-,\partial_\tau P_-]\right)dk\,d\tau,$$ its Chern number is $$c_1=\begin{cases}
0,&m<-2,\\ -1,&-2<m<0,\\ +1,&0<m<2,\\ 0,&m>2.
\end{cases}$$

Pauli multiplication gives $H_m^2=|d_m|^2I$. With $x=\cos k$ and $y=\cos\tau$, $$\label{eq:norm}
 |d_m|^2=m^2+2+2m(x+y)+2xy.$$ The right side is affine in each variable separately, so its minimum on $[-1,1]^2$ occurs at a corner. The four corner values are $(m+2)^2,m^2,m^2,(m-2)^2$. This proves both the closing locus and the stated gap. Smooth functional calculus then gives the displayed lower projector. The Chern computation is proved below in revision one.

\>0

# Projector sign, degree, and Dirac walls

This revision is the **analytic Dirac-degree owner**. Direct Pauli algebra fixes the convention-sensitive sign: $$\label{eq:pauli}
 \operatorname{Tr}\!\left(P_-[\partial_kP_-,\partial_\tau P_-]\right)
 =-\frac{i}{2}n\cdot(\partial_kn\times\partial_\tau n).$$ Consequently [\[eq:c1\]](#eq:c1){reference-type="eqref" reference="eq:c1"} is minus the Brouwer degree of $n:\mathbb T^2\to S^2$. For completeness, a direct differentiation before normalization gives $$\label{eq:numerator}
d_m\cdot(\partial_kd_m\times\partial_\tau d_m)
=\cos k+\cos\tau+m\cos k\cos\tau.$$

Choose the north pole as regular value away from the walls. Its possible preimages are the four points with $\sin k=\sin\tau=0$. A point contributes exactly when its mass $M=m+\cos k_0+\cos\tau_0$ is positive, and its local degree is $\chi(k_0,\tau_0)=\cos k_0\cos\tau_0$. Thus $\deg(n)=\sum\chi\mathbf1_{\{M>0\}}$. Substituting $\mathbf1_{\{M>0\}}=(1+\operatorname{sgn}M)/2$ and using $\sum\chi=0$ yields $$\label{eq:masssum}
c_1=-\frac12\bigl[\operatorname{sgn}(m+2)
-2\operatorname{sgn}(m)+\operatorname{sgn}(m-2)\bigr].$$ This proves the remaining part of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} without numerical integration. As $m$ increases, the complete wall ledger is

   mass   zero $(k_0,\tau_0)$   $\chi$   jump of $c_1$
  ------ --------------------- -------- ---------------
   $-2$         $(0,0)$          $+1$        $-1$
   $0$         $(\pi,0)$         $-1$        $+1$
   $0$         $(0,\pi)$         $-1$        $+1$
   $2$        $(\pi,\pi)$        $+1$        $-1$

The simultaneous pair at $m=0$ is essential: its total jump is two.

\>1

# Adiabatic transport and exact boundaries

This revision is the **adiabatic scope and route firewall**.

Let $\tau$ increase from $0$ to $2\pi$, assign unit positive particle charge, and define positive current by $J=\partial_kH_m$. Assume a gapped chamber, a completely filled lower band, and an adiabatic traversal. With the orientation fixed in [\[eq:c1\]](#eq:c1){reference-type="eqref" reference="eq:c1"}, the transported positive-particle charge per cycle equals $c_1(P_-)$.

Indeed, for $$\Omega_{k\tau}=i\operatorname{Tr}P_-[\partial_kP_-,\partial_\tau P_-],
\qquad
Q=-\frac1{2\pi}\int_{\mathbb T^2}\Omega_{k\tau}\,dk\,d\tau
  =\frac1{2\pi i}\int_{\mathbb T^2}\operatorname{Tr}P_-[\partial_kP_-,\partial_\tau P_-]
  =c_1(P_-).$$ For electronic charge the result is multiplied by $-e$. This is an adiabatic-limit statement. At finite driving rate, interband transitions can occur; no exact finite-driving-rate quantization is claimed.

At $m=-2,0,2$ the lower projector is undefined at the zeroes in the table and no gapped-bundle Chern number is assigned. Reversing the torus orientation, or sending $\tau\mapsto-\tau$, reverses the integer. Complex conjugation satisfies $$K H_m(k,\tau)K=H_m(k,-\tau),$$ because only $\sigma_y$ is imaginary. For $m>2$ (respectively $m<-2$), the $z$ component is everywhere positive (respectively negative), and the field contracts without closing the gap to the north (respectively south) pole.

# Evidence, provenance, and claim boundary

The exact evidence records the four corner values, chamber signs, and Dirac ledger. A separate discrete lattice-gauge lane on several grids reproduces the four integers, but is only regression evidence; the analytic degree proof owns the theorem. Strict parsers, repaired-hash hostile mutations, isolated byte replay, and deterministic PDF builds audit the release.

Thouless established quantized adiabatic particle transport [@Thouless]; Qi, Wu, and Zhang give the two-band lattice-Dirac lineage [@QWZ]. We cite lineage, not priority, and rederive every normalization and sign used here. Nearby packages treat finite SSH chains, the Dirac-monopole sphere and its magnetic spectrum, and kicked rotors; none owns this smooth two-parameter Bloch-bundle atlas.

The Chern integer is a source-local natural quantization, but the Chern integer is not a rational-prime carrier. There is no primitive-orbit determinant, target functional equation, target zero match, or Hilbert--Pólya operator. Thus Route A is rejected as $(A0_{\rm FAIL},A1_{\rm FAIL},A2_{\rm FAIL},A3_{\rm FAIL},
A4_{\rm NATURAL\_QUANTIZATION})$, and Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 D. J. Thouless, *Quantization of particle transport*, Phys. Rev. B 27 (1983), 6083--6087. <https://doi.org/10.1103/PhysRevB.27.6083>. X.-L. Qi, Y.-S. Wu, and S.-C. Zhang, *Topological quantization of the spin Hall effect in two-dimensional paramagnetic semiconductors*, Phys. Rev. B 74 (2006), 085308. <https://doi.org/10.1103/PhysRevB.74.085308>.
