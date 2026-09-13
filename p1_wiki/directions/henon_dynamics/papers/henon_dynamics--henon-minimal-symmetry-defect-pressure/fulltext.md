---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-minimal-symmetry-defect-pressure"
canonical_tex: "henon_dynamics/henon_minimal_symmetry_defect_pressure/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_minimal_symmetry_defect_pressure/paper/paper.pdf"
source_sha256: "d4b8f06874ab7adb6e7b88ee6922415c77f142a8fd4343c48090857da220b0b2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Minimal Symmetry-Defect Pressure for Reflection-Selected Hénon Packets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_minimal_symmetry_defect_pressure>)
- [规范 TeX](<../../../../../henon_dynamics/henon_minimal_symmetry_defect_pressure/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_minimal_symmetry_defect_pressure/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_minimal_symmetry_defect_pressure/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_minimal_symmetry_defect_pressure/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Primitive odd reflection points of the full Hénon horseshoe have two natural sampling limits: a marked reflection-boundary Bernoulli law and, after cyclic time averaging, the invariant maximal-entropy Bernoulli law. A direct rigorous separation of their coordinate-Mahler averages requires cylinder distortion estimates not presently available. We construct instead the minimal finite cross-axis calibration observable $\chi(\omega)=\mathbf1_{\{\omega_{-1}=\omega_1\}}$. Every finite observable supported wholly on one side of the axis has equal expectations under the two laws, but $\mathbb E_J\chi=1$ and $\mathbb E_B\chi=1/2$. The resulting extensive packet pressures are exactly $\frac12\log2-t$ and $\frac12\log2-t/2$. Coupling this calibration to the coordinate Mahler variable produces two pressure planes whose transverse derivatives differ by $1/2$, regardless of the unresolved Mahler-slope gap. Exact primitive-palindrome certificates through period $21$ accompany the theorem. No prime trace or operator is claimed.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  A Minimal Symmetry-Defect Pressure for\
  Reflection-Selected Hénon Packets
```

## Markdown 正文

# Sampling problem

The area-preserving map $H(x,y)=(6-x^2-y,x)$ has a real chain recurrent set conjugate to the full two-shift, with its reversor intertwined with sequence reversal. This rests on the Devaney--Nitecki horseshoe and Arai's hyperbolic plateau [@DevaneyNitecki1979; @Arai2007]; symbolic background is standard [@LindMarcus1995].

Let $\mu_B$ be fair two-sided Bernoulli measure. Let $\eta_J$ be the reflection-boundary law obtained from iid fair bits $(\xi_k)_{k\ge0}$ by $$\label{eq:boundary}
 \omega_k=\omega_{-k}=\xi_k\qquad(k\ge0).$$ The preceding packet-equidistribution theorem proves that marked primitive reflection points converge to $\eta_J$, while cyclically averaging those points converges to $\mu_B$.

For the coordinate observable $\varphi=\log^+|x|$, these limits define constants $\kappa_J$ and $\kappa_{\max}$. Finite data suggest they differ, but an all-period numerical inequality needs an explicit coding-distortion constant. We seek a rigorous local calibration that avoids that missing input.

# One-sided blindness and the first separator

Call an observable positive-one-sided if it depends on finitely many coordinates in $\{0,1,2,\ldots\}$; define negative-one-sided analogously.

[\[thm:blind\]]{#thm:blind label="thm:blind"} For every finite positive- or negative-one-sided observable $f$, $$\label{eq:blind}
 \int f\,d\eta_J=\int f\,d\mu_B.$$

Under both laws, every finite vector $(\omega_0,\ldots,\omega_r)$ consists of independent fair bits. The negative side follows by reflection.

Define the centered radius-one observable $$\label{eq:chi}
 \chi(\omega)=\mathbf1_{\{\omega_{-1}=\omega_1\}}.$$

[\[prop:separator\]]{#prop:separator label="prop:separator"} One has $$\label{eq:means}
 \int\chi\,d\eta_J=1,
 \qquad
 \int\chi\,d\mu_B=\frac12.$$ Thus a centered radius-one cross-axis window distinguishes the measures, whereas [\[thm:blind\]](#thm:blind){reference-type="ref" reference="thm:blind"} excludes every finite one-sided window.

Equation [\[eq:boundary\]](#eq:boundary){reference-type="eqref" reference="eq:boundary"} makes the first equality deterministic. Under $\mu_B$, the two tested bits are independent and fair.

The minimality statement is deliberately support-sensitive. It does not claim invariance under an arbitrary sliding-block recoding.

# Finite primitive reflection packets

Let $n$ be odd and let $U_n$ be the $2^{(n+1)/2}$ palindromic words fixed by the marked reversal. Their exact-period subset has size $$\label{eq:Dn}
 D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}.$$ At the marked center, [\[eq:chi\]](#eq:chi){reference-type="eqref" reference="eq:chi"} equals one for every word.

Now choose both a word in $U_n$ and a cyclic center uniformly. At the reflection center the two tested sites are paired. At each of the other $n-1$ centers they are distinct free half-word bits. Hence the exact full mean is $$\label{eq:fullmean}
 c_n^{\mathrm{full}}=\frac1n+\frac{n-1}{2n}
 =\frac12+\frac1{2n}.$$ Removing lower periods changes expectations of a $[0,1]$-valued observable by at most $$\label{eq:primitive-error}
 \tau(n)2^{-n/3}.$$ Therefore the primitive orbit mean $c_n$ tends to $1/2$.

# Separated pressure planes

Define the pure symmetry packet partitions $$\label{eq:partitions}
 Z_{n,J}(t)=D_ne^{-tn},
 \qquad
 Z_{n,\mathrm{orb}}(t)=D_ne^{-tnc_n}.$$ Since $n^{-1}\log D_n\to\frac12\log2$, we obtain the following exact laws.

[\[thm:pressure\]]{#thm:pressure label="thm:pressure"} For every fixed real $t$, $$\label{eq:pressures}
 P_J(t)=\frac12\log2-t,
 \qquad
 P_{\mathrm{orb}}(t)=\frac12\log2-\frac t2.$$

Add the packet-Mahler parameter $s$ from the preceding work. The resulting two planes are $$\begin{aligned}
\label{eq:planes}
 P_J(s,t)&=\frac12\log2-s\kappa_J-t,\\
 P_{\mathrm{orb}}(s,t)&=\frac12\log2-s\kappa_{\max}-\frac t2.\end{aligned}$$ In particular, $$\label{eq:gradient}
 \partial_tP_J-\partial_tP_{\mathrm{orb}}=-\frac12.$$ This is a certified transverse separation even though the value of $\kappa_J-\kappa_{\max}$ remains open.

# Executable certificate and boundary

Two independent programs enumerate primitive palindromes through periods $21$ and $17$, respectively. They verify [\[eq:fullmean\]](#eq:fullmean){reference-type="eqref" reference="eq:fullmean"}, [\[eq:primitive-error\]](#eq:primitive-error){reference-type="eqref" reference="eq:primitive-error"}, the degree vector $2,2,6,14,28,62,126,246,510,1022,2030$, and 21 hostile claim mutations. Normal and optimized tests agree. No floating-point input is used.

The theorem gives a symbolic calibration channel, not a solution of the coordinate-Mahler gap. Nor does it provide rational-prime labels, a von Mangoldt amplitude, a Fredholm determinant, a self-adjoint operator, or a Hilbert--Pólya correspondence. Its next structural question is whether the marked pressure is invariant under replacing a potential by a symbolic coboundary. Because $\eta_J$ is not invariant, one should expect an exact boundary gauge anomaly.
