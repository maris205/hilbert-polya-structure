---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-entropy-von-mangoldt-bridge"
canonical_tex: "henon_dynamics/henon_entropy_von_mangoldt_bridge/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_entropy_von_mangoldt_bridge/paper/paper.pdf"
source_sha256: "a04d404c3a81db2119916fe2aa22b36948bb204af40085371b97dff7a4dffbd7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Entropy--von Mangoldt Mass Bridge for an All-Period Hénon Survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_entropy_von_mangoldt_bridge>)
- [规范 TeX](<../../../../../henon_dynamics/henon_entropy_von_mangoldt_bridge/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_entropy_von_mangoldt_bridge/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_entropy_von_mangoldt_bridge/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We return from finite arithmetic decorations to the all-period chronology of the certified four-state survivor of the area-preserving Hénon map $H_6(q,p)=(1-6q^2-p,q)$. Its transition matrix has Perron root $\varphi=(1+\sqrt5)/2$. We prove that, under the intrinsic entropy clock $X_n=\varphi^n$, the exact-period marked-point count is asymptotic to the cumulative von Mangoldt mass $\vartheta(X_n)$, while the primitive-orbit count is asymptotic to $(\log\varphi)\pi(X_n)$. The proof combines the exact subshift spectrum, Möbius inversion, and the prime number theorem. A deterministic certificate independently reconstructs all orbit counts and finite prime comparisons through period 32. This is a positive mass-level bridge requiring no fitted scale or prime lookup in the candidate. It does not define an orbit--prime bijection, a Riemann determinant, or a Hilbert--Pólya operator.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
date: 'Preprint, August 2026'
title: |
  An Entropy--von Mangoldt Mass Bridge\
  for an All-Period Hénon Survivor
```

## Markdown 正文

# The frozen Hénon carrier

On the previously certified local survivor, $H_6$ is conjugate to the four-state subshift with adjacency matrix $$A=\begin{pmatrix}
1&0&1&0\\1&0&0&0\\0&1&0&1\\0&1&0&0
\end{pmatrix}.$$ The characteristic polynomial factors as $$\det(xI-A)=x^4-x^3-x-1=(x^2-x-1)(x^2+1).$$ Hence the eigenvalues are $\varphi,-\varphi^{-1},i,-i$, and the topological entropy is $h=\log\varphi$. This paper uses the symbolic conjugacy and no additional parameter. It concerns this certified survivor, not the full nonwandering set of $H_6$.

Let $N_n=\operatorname{tr}(A^n)$ be the number of marked points fixed by the $n$th iterate. Let $E_n$ be the number having exact period $n$, and let $P_n=E_n/n$ be the number of unmarked primitive cyclic orbits.

# Exact primitive census

[\[prop:census\]]{#prop:census label="prop:census"} For every $n\ge1$, $$N_n=\varphi^n+(-\varphi^{-1})^n+i^n+(-i)^n,$$ and $$E_n=\sum_{d\mid n}\mu(d)N_{n/d},\qquad P_n=\frac{E_n}{n}.$$ In particular $E_n$ is a nonnegative integer divisible by $n$.

The trace formula is the spectral decomposition of $A^n$. Every point fixed by the $n$th iterate has a unique exact period dividing $n$, so $N_n=\sum_{d\mid n}E_d$. Möbius inversion gives the second formula. An exact-period orbit has exactly $n$ marked phases, proving divisibility.

[\[prop:error\]]{#prop:error label="prop:error"} As $n\to\infty$, $$E_n=\varphi^n+O\!\left(\tau(n)\varphi^{n/2}+\tau(n)\right),
\qquad
P_n=\frac{\varphi^n}{n}\bigl(1+o(1)\bigr).$$

In Proposition [\[prop:census\]](#prop:census){reference-type="ref" reference="prop:census"}, the $d=1$ term is $\varphi^n+O(1)$. For every divisor $d\ge2$, one has $n/d\le n/2$ and $N_{n/d}=O(\varphi^{n/2}+1)$. Summing over at most $\tau(n)$ divisors proves the claim.

# The entropy--arithmetic bridge

Write $$\vartheta(X)=\sum_{p\le X}\log p,
\qquad
\pi(X)=\#\{p\le X\}.$$ The prime number theorem is equivalent to $\vartheta(X)\sim X$ and implies $\pi(X)\sim X/\log X$.

[\[thm:bridge\]]{#thm:bridge label="thm:bridge"} For the intrinsic scale $X_n=e^{hn}=\varphi^n$, $$\boxed{\frac{E_n}{\vartheta(X_n)}\longrightarrow1},
\qquad
\boxed{\frac{P_n}{\pi(X_n)}\longrightarrow h=\log\varphi}.$$

Proposition [\[prop:error\]](#prop:error){reference-type="ref" reference="prop:error"} gives $E_n\sim\varphi^n=X_n$ and $P_n\sim X_n/n$. The prime number theorem gives $\vartheta(X_n)\sim X_n$ and $\pi(X_n)\sim X_n/(n\log\varphi)$. Division proves both limits.

The first limit is the sharper structural statement. The explicit formula weights each prime by $\log p$; marked exact-period points are likewise the phase-resolved version of primitive orbits. Their main terms agree without an adjustable scale. The second limit records the unavoidable passage from marked points to unmarked cycles and exposes the fixed entropy factor.

# Finite exact certificate

The companion program powers $A$ over the integers, performs Möbius inversion, checks $n\mid E_n$, and builds a sieve only for a finite illustration. No finite prime statistic enters the theorem or changes the clock. At $n=32$, the marked ratio $E_n/\vartheta(\varphi^n)$ is already within $10^{-4}$ of one. The primitive ratio approaches $\log\varphi$ more slowly, as expected from the prime-counting remainder.

# What the theorem does not say

Theorem [\[thm:bridge\]](#thm:bridge){reference-type="ref" reference="thm:bridge"} is a mass identity, not a matching theorem. It does not choose a prime for an orbit, prove that an instability multiplier is an integer, derive the amplitude $\log p/p^{r/2}$, or continue a dynamical determinant to the critical line. Many mixing subshifts obey analogous prime orbit asymptotics. The Hénon content is the source-locked realization of this particular chronology and entropy.

Under the Route-A evaluator the outcome is $$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm PARTIAL},A4_{\rm FORMAL}).$$ The positive result justifies the next gate: determine exactly what repetition amplitude one primitive instability Euler factor would supply if its intrinsic multiplier were a prime.

# Conclusion

The all-period Hénon survivor has the correct leading arithmetic mass once time is measured by entropy. This reconnects the large route after the finite CM branch closed, while keeping the decisive missing arrow visible: aggregate density is not a source-native prime label.

9 M. Artin and B. Mazur, On periodic points, *Ann. of Math.* 81 (1965), 82--99. R. Bowen, Periodic orbits for hyperbolic flows, *Amer. J. Math.* 94 (1972), 1--30. J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$, *Bull. Soc. Math. France* 24 (1896), 199--220. C.-J. de la Vallée Poussin, Recherches analytiques sur la théorie des nombres premiers, *Ann. Soc. Sci. Bruxelles* 20 (1896), 183--256.
