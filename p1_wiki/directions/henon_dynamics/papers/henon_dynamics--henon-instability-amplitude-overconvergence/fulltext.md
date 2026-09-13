---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-instability-amplitude-overconvergence"
canonical_tex: "henon_dynamics/henon_instability_amplitude_overconvergence/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_instability_amplitude_overconvergence/paper/paper.pdf"
source_sha256: "2bafc185fe3e2ef206905e6997f6f9ed994b496ea575df983a5e14231bbed8e3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Prime-Power Amplitudes but the Wrong Global Clock: Critical-Line Overconvergence of a Hénon Instability Product

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_instability_amplitude_overconvergence>)
- [规范 TeX](<../../../../../henon_dynamics/henon_instability_amplitude_overconvergence/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_instability_amplitude_overconvergence/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_instability_amplitude_overconvergence/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The instability roof of the certified area-preserving Hénon survivor is intrinsic, positive, non-lattice, and multiplicative under repetitions. We show that its primitive Euler factors have exactly the local syntax required by the von Mangoldt prime-power terms: if an unstable multiplier equals a prime $p$, every repetition contributes $\log p\,p^{-r/2}e^{-itr\log p}$ on the critical line. The global test has the opposite verdict. A previously certified uniform expansion constant places the whole Hénon logarithmic derivative in an ordinary absolutely convergent domain containing $\Re s=1/2$, while the all-prime von Mangoldt series is not absolutely convergent there. Thus the raw instability clock has correct local amplitudes but the wrong global density. The obstruction is all-period and precedes any zero comparison. It leaves a pressure- normalized roof as a distinct candidate.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
date: 'Preprint, August 2026'
title: |
  Exact Prime-Power Amplitudes but the Wrong Global Clock:\
  Critical-Line Overconvergence of a Hénon Instability Product
```

## Markdown 正文

# Frozen object and inherited bound

Let $\mathcal P$ denote the primitive orbits of the certified four-state survivor of $H_6(q,p)=(1-6q^2-p,q)$. For $\gamma\in\mathcal P$, let $\Lambda_\gamma$ be the signed unstable multiplier and set $$\ell_\gamma=\log|\Lambda_\gamma|>0.$$ The raw instability determinant is $$\label{eq:D}
D_{\rm inst}(s)=\prod_{\gamma\in\mathcal P}
(1-|\Lambda_\gamma|^{-s}).$$ The established cone theorem supplies the per-step lower expansion $$J_*=\frac{\sqrt{17}+\sqrt{13}}2,$$ while the symbolic entropy is $\log\varphi$. Consequently the absolute trace-log majorant converges whenever $$\label{eq:sigma0}
\Re s>\sigma_0:=\frac{\log\varphi}{\log J_*}
=0.3559817479\ldots.$$ This paper uses that proved bound and changes no orbit, roof, or normalization.

# The exact local amplitude compiler

[\[prop:local\]]{#prop:local label="prop:local"} For $\Re s>0$ and one primitive orbit, $$\partial_s\log(1-e^{-s\ell_\gamma})
=\sum_{r\ge1}\ell_\gamma e^{-rs\ell_\gamma}.$$ At $s=1/2+it$, its $r$th term is $$\ell_\gamma|\Lambda_\gamma|^{-r/2}
e^{-itr\ell_\gamma}.$$

Differentiate the logarithm and expand the geometric series. The second formula uses $e^{-\ell_\gamma}=|\Lambda_\gamma|^{-1}$.

[\[cor:prime\]]{#cor:prime label="cor:prime"} The complete repetition tower of $\gamma$ equals the local von Mangoldt tower of a rational prime $p$ if and only if $$|\Lambda_\gamma|=p
\quad\text{and hence}\quad \ell_\gamma=\log p.$$

The forward implication follows already from the $r=1$ decay and phase as a function of $t$; the reverse implication is Proposition [\[prop:local\]](#prop:local){reference-type="ref" reference="prop:local"}.

Thus repetition is not the missing operation. Once the clock is a prime logarithm, the Euler factor automatically creates every prime power with the right amplitude and phase.

# Global critical-line overconvergence

[\[thm:over\]]{#thm:over label="thm:over"} The logarithmic derivative of [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"} converges locally absolutely on $\Re s>\sigma_0$, in particular on $\Re s=1/2$. By contrast, $$\sum_p\sum_{r\ge1}\log p\,p^{-r/2}$$ diverges. Therefore no bijection between all rational primes and the raw Hénon primitive orbits can identify the two towers term by term while retaining ordinary absolute values.

On every closed half-plane $\Re s\ge\sigma_0+\varepsilon$, the inherited geometric majorant has ratio below one. Differentiation introduces at most a linear period factor, still summable against this geometric margin. Since $\sigma_0<1/2$, the first assertion follows.

For the second, it suffices to retain $r=1$. Partial summation and the prime number theorem $\vartheta(X)\sim X$ give $$\sum_{p\le X}\frac{\log p}{\sqrt p}
=\int_{2^-}^X u^{-1/2}\,d\vartheta(u)
\sim2\sqrt X,$$ so the absolute prime mass diverges. A termwise bijection would preserve the sum of absolute values, contradicting the first assertion.

The theorem is stronger than a finite density mismatch. It compares the analytic class of the complete signed atoms before any target zeros are opened. Conditional summation or distributional continuation cannot repair an asserted ordinary termwise absolute identification; it would define a new global object requiring its own theorem.

# Finite certificate and controls

The certificate recomputes $\sigma_0$, checks $\varphi/\sqrt{J_*}<1$, and verifies eight repetition atoms for the exact fixture $|\Lambda|=p=7$. A sieve records the growth of $\sum_{p\le X}\log p/\sqrt p$ at fixed cutoffs. The sieve is not used to prove divergence or to fit a Hénon scale.

The negative result is scoped to the raw roof $\ell=\log|\Lambda|$. Multiplying this roof by an intrinsic pressure normalization changes both the abscissa and the putative arithmetic label. That is a new candidate, not a counterexample to Theorem [\[thm:over\]](#thm:over){reference-type="ref" reference="thm:over"}.

# Evaluator verdict

The raw product is a genuine analytic determinant in a half-plane and has an exact local amplitude compiler. Its global arithmetic structure fails. The strict Route-A tuple is $$(A1_{\rm WEAK},A2_{\rm ANALYTIC},A3_{\rm FAIL},A4_{\rm FORMAL}),$$ with overall verdict `ROUTE_A_REJECTED`. No operator is defined, so Route B is not authorized.

# Conclusion

The raw instability roof clears the repetition gate and fails the global clock gate. This clean separation identifies the next large move: pressure-normalize the same non-lattice roof so that its primitive-orbit exponent is one, then test whether the resulting real labels have any source-native arithmetic integrality.

9 D. Ruelle, Zeta-functions for expanding maps and Anosov flows, *Invent. Math.* 34 (1976), 231--242. R. Bowen, Periodic orbits for hyperbolic flows, *Amer. J. Math.* 94 (1972), 1--30. J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$, *Bull. Soc. Math. France* 24 (1896), 199--220.
