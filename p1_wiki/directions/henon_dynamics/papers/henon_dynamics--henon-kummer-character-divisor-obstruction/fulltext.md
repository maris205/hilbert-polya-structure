---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kummer-character-divisor-obstruction"
canonical_tex: "henon_dynamics/henon_kummer_character_divisor_obstruction/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_kummer_character_divisor_obstruction/paper/paper.pdf"
source_sha256: "2a2771685278bdca88758cbdc6ee44be18f362ab8cb7c23e9a367282e96ebd92"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cyclotomic Channels Do Not Make a Meromorphic Prime Product: A Divisor Obstruction for Kummer--Hénon Holonomy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kummer_character_divisor_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kummer_character_divisor_obstruction/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kummer_character_divisor_obstruction/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kummer_character_divisor_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_kummer_character_divisor_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify the raw all-prime determinant produced by the smallest nonfunctorial survivor of the homogeneous Hénon Kummer lift. A virtual three-channel fibre has eigenvalues $1,\zeta_3,\zeta_3^2$ and integral multiplicities $m_0,m_1,m_2$. We prove two rigidity statements. First, simultaneous cancellation of all repetition characters forces all three multiplicities to vanish. Second, every nonzero virtual channel produces zeros or poles converging to the interior point $s=1/2$ as the prime tends to infinity. Therefore the raw critical-normalized prime divisor is not locally finite and cannot define a nonzero meromorphic function. Exact cyclotomic code exhausts 2,197 virtual multiplicities and independently checks the Fourier classification. Nonfunctorial channel permutation is algebraically real, but a viable global assembly must acquire intrinsic prime-dependent decay.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
bibliography:
- references.bib
date: 'Preprint, August 2026'
title: |
  Cyclotomic Channels Do Not Make a Meromorphic Prime Product:\
  A Divisor Obstruction for Kummer--Hénon Holonomy
```

## Markdown 正文

# Introduction

The homogeneous Hénon quantization supplies a cubic phase and a natural three-channel Kummer grading. Functorial channel lifts are gauge trivial, so the smallest surviving modification inserts an intrinsic cyclic permutation between the two gauge frames. Such a permutation has eigenvalues $1,\zeta_3,\zeta_3^2$, and its repetitions carry genuine periodic characters. The question is no longer whether a local trace is nonzero. It is whether the complete prime family is the divisor of a meromorphic determinant.

We answer negatively for the raw critical normalization. The obstruction does not use a numerical zero comparison. Every surviving local channel places a zero or pole within $O(1/\log p)$ of $1/2$, so infinitely many divisor points accumulate inside the domain. Basic complex analysis then rules out a nonzero meromorphic function [@Conway1978].

The contribution has three parts: an exact Fourier classification of virtual repetition traces, an all-prime divisor theorem, and a finite cyclotomic certificate that attacks common cancellation mistakes. The Hénon motivation comes from the area-preserving model [@Wang2026], but the obstruction applies to any fixed finite unitary channel set.

# Virtual cubic characters

Let $\zeta=e^{2\pi i/3}$, and let $m=(m_0,m_1,m_2)\in\mathbb Z^3$. Negative entries represent odd or denominator channels. The virtual character of the $r$-th repetition is $$\label{eq:char}
 \chi_m(r)=m_0+m_1\zeta^r+m_2\zeta^{2r}.$$ This is the discrete Fourier transform of $m$ on the cyclic group of order three; see [@Serre1977] for the representation-theoretic background.

[\[thm:fourier\]]{#thm:fourier label="thm:fourier"} If $\chi_m(r)=0$ for $r=1,2,3$, then $m=(0,0,0)$. Consequently exact cancellation at every repetition is trivial.

At $r=3$, $m_0+m_1+m_2=0$. At $r=1$, using $\zeta^2=-1-\zeta$, the coefficients of $1$ and $\zeta$ give $m_0-m_2=0$ and $m_1-m_2=0$. Thus all three entries are equal, and their sum is zero. Hence each entry vanishes. The same conclusion follows from invertibility of the order-three Fourier matrix.

Zero superdimension alone is much weaker. For example, $m=(1,-1,0)$ has $\chi_m(3)=0$ but $\chi_m(1)=1-\zeta\ne0$. Any test that inspects only the third repetition therefore accepts a false cancellation.

# The raw all-prime divisor

For every prime $p$, define the virtual local factor $$\label{eq:local}
 F_{p,m}(s)=\prod_{j=0}^{2}
 (1-\zeta^j p^{1/2-s})^{m_j}.$$ This convention preserves signs: negative multiplicity gives a pole rather than deleting a channel. It also freezes the same $\log p$ clock in every factor.

[\[thm:accum\]]{#thm:accum label="thm:accum"} If $m\ne0$, the union over all primes of the zero--pole divisors of $F_{p,m}$ is not locally finite in any neighborhood of $s=1/2$. Therefore it is not the divisor of a nonzero meromorphic function there.

Choose $j$ with $m_j\ne0$. If $j=0$, every local factor has a zero or pole at $s=1/2$ itself. If $j=1$ or $2$, solve $p^{1/2-s}=\zeta^{-j}$. One solution has real part $1/2$ and imaginary part of absolute value at most $$\frac{2\pi}{3\log p}.$$ As primes tend to infinity, these distinct divisor points converge to $1/2$. Zeros and poles of a nonzero meromorphic function are isolated; its divisor is locally finite. The claimed prime divisor violates this condition.

The only integral virtual combination of the three channels whose raw all-prime divisor is locally finite near $1/2$ is $m=0$.

Identical numerator and denominator channels are already combined into the net multiplicities $m_j$. Theorem [\[thm:accum\]](#thm:accum){reference-type="ref" reference="thm:accum"} applies to every nonzero net vector.

The theorem is phase robust. More generally, any fixed finite set of unitary eigenphases yields imaginary displacements $O(1/\log p)$. A fixed number of channels cannot prevent interior accumulation unless every net channel cancels exactly.

# Exact certificate and adversarial controls

We represent $\mathbb Z[\zeta]$ in the basis $(1,\zeta)$, so that $\zeta^2=(-1,-1)$. No floating-point comparison enters the character classification. The release certificate exhausts all $m_j\in[-6,6]$, a total of $13^3=2197$ vectors, and finds only the zero common kernel for repetitions one, two, and three.

The numerical layer lists the primes below $10^5$ and displays the nearest nontrivial-channel distance. Its purpose is visual verification of the formula, not extrapolation. An independent test freezes the false zero-superdimension vector and checks that it survives repetition one.

  Quantity                        Value
  ----------------------------- -------
  Virtual vectors checked         2,197
  Common null vectors                 1
  Primes below $10^5$             9,592
  Random or fitted parameters         0

  : Release certificate.

# What damping would change

Replacing $p^{1/2-s}$ by $p^{-\sigma}p^{1/2-s}$ moves local divisors away from the fixed interior point and can make a block direct sum compact or trace class. It also inserts the second clock $\sigma\log p$. Such a factor counts only if $\sigma$ is derived from an intrinsic conductor or geometric normalization; selecting it merely to force convergence would be a modeling choice. This is the next gate.

# Route evaluation and conclusion

The channel permutation gives an exact but inherited prime-loop character, so A1 is weak. The raw determinant fails at A2, and its global analytic structure fails at A3. A monomial lift is only a formal A4 hint because no determinant-class operator exists. The strict tuple is $$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FORMAL\ HINT}).$$ Route B is not authorized.

The result closes the undamped three-channel product exactly. It does not close a conductor-weighted block operator, an infinite-rank local complex, or a scattering ratio with independently proved cancellation. The next paper therefore asks the only remaining minimal question: what damping is mathematically sufficient, and can the Kummer--Hénon data produce it without an external clock?
