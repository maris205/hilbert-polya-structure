---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-225-tight-cloud-local-finiteness-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction/main.pdf"
source_sha256: "c0ffa14672ba1dacb9bc02a8e86b244c66e213f0ee79db2d5a8c64a3a95c152e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Tight Clouds versus Locally Finite Divisors An Exact Obstruction to Direct Rank-Growing Root Limits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-225-tight-cloud-local-finiteness-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Global centered-RMS normalization makes every empirical root measure have unit second moment, and RH-224 therefore proves uniform tightness. This paper shows why that positive probability result cannot be promoted directly to a holomorphic zero-divisor limit.

  Let $\Lambda_n$ be finite clouds with ranks $d_n\to\infty$, let $\nu_n=\sum_{\lambda\in\Lambda_n}\delta_\lambda$ be their integer root divisors, and let $\mu_n=d_n^{-1}\nu_n$ be their empirical probability measures. If $\{\mu_n\}$ is uniformly tight, one fixed compact set contains at least half of every cloud. Hence $\nu_n$ has mass at least $d_n/2$ on a fixed compact set, which diverges. The divisors cannot converge vaguely to a locally finite divisor, and they cannot be zero divisors of a locally uniformly convergent nonzero holomorphic family.

  In the RH-222 atlas all normalized roots lie in $|z|\le2$, while all raw Hardy-scaled resonances lie in $|z|<1$ with maximum modulus $0.86860$. Compact divisor counts grow from $4$ to $35$ on the left and from $4$ to $34$ on the right.

  The obstruction rejects the resonances themselves, normalized or raw, as the zeros of the sought growing determinant. It does not reject the reciprocal Fredholm zeros $1/\lambda$, which can escape to infinity when resonances tend to zero. This distinction redirects the next layer to the correct spectral variable.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Tight Clouds versus Locally Finite Divisors\
  An Exact Obstruction to Direct Rank-Growing Root Limits
```

## Markdown 正文

# Two measures carried by the same roots

For a finite multiset $$\Lambda_n=\{\lambda_{n,1},\ldots,\lambda_{n,d_n}\}\subset\mathbb C,$$ there are two natural measures: $$\label{eq:measures}
 \nu_n=\sum_{j=1}^{d_n}\delta_{\lambda_{n,j}},\qquad
 \mu_n=\frac1{d_n}\nu_n.$$ The first is the integer divisor measure. The second is the empirical probability measure.

Weak compactness of $\mu_n$ is a macroscopic statement in which each root has mass $1/d_n$. Local finiteness of $\nu_n$ is a microscopic statement in which each simple root has mass one. RH-224 proves tightness only for the first normalization [@WangRH224].

# The tightness obstruction

[\[thm:obstruction\]]{#thm:obstruction label="thm:obstruction"} Suppose $d_n\to\infty$ and the empirical measures $\{\mu_n\}$ in [\[eq:measures\]](#eq:measures){reference-type="eqref" reference="eq:measures"} are uniformly tight. Then there is a compact set $K\subset\mathbb C$ such that $$\label{eq:massgrowth}
 \nu_n(K)\ge\frac{d_n}{2}$$ for every $n$. Consequently no subsequence of $\nu_n$ converges vaguely to a locally finite Radon measure.

Uniform tightness with $\varepsilon=1/2$ supplies compact $K$ such that $\mu_n(K)\ge1/2$ for all $n$. Multiplying by $d_n$ proves [\[eq:massgrowth\]](#eq:massgrowth){reference-type="eqref" reference="eq:massgrowth"}.

Choose a compactly supported continuous function $\phi\ge0$ that equals one on $K$. Then $$\int\phi\,d\nu_n\ge\nu_n(K)\longrightarrow\infty.$$ Vague convergence to a locally finite Radon measure $\nu$ would instead give the finite limit $\int\phi\,d\nu$. This is impossible.

The fraction $1/2$ is arbitrary. For any fixed $0<\varepsilon<1$, one compact set carries at least $(1-\varepsilon)d_n$ divisor mass.

[\[cor:holo\]]{#cor:holo label="cor:holo"} Under the assumptions of Theorem [\[thm:obstruction\]](#thm:obstruction){reference-type="ref" reference="thm:obstruction"}, the $\Lambda_n$ cannot be the complete zero divisors on $\mathbb C$ of holomorphic functions $f_n$ converging locally uniformly to a nonzero entire function $f$, with zeros counted by algebraic multiplicity.

On a compact neighborhood whose boundary avoids the zeros of $f$, local uniform convergence and Rouche's theorem make the number of zeros eventually equal to that of $f$; see @Conway1978. Equivalently, zero divisors of a nonzero locally uniform limit are locally bounded. This contradicts Theorem [\[thm:obstruction\]](#thm:obstruction){reference-type="ref" reference="thm:obstruction"}.

The only holomorphic escape is degeneration to the identically zero function, which is not a spectral determinant.

# Application to globally normalized clouds

RH-224 gives $$\mu_n(|z|>R)\le R^{-2}.$$ At $R=2$, every normalized cloud has at least $75\%$ of its roots in one fixed disk. Thus any all-level extension with ranks tending to infinity would satisfy $$\nu_n(\overline{D(0,2)})\ge\frac34d_n\to\infty.$$ The exact theorem already rejects the direct normalized-root divisor. No numerical convergence assumption is needed.

This conclusion complements the fixed-quartic obstruction RH-219 [@WangRH219]. RH-219 rules out degree four and repeated fixed support. Theorem [\[thm:obstruction\]](#thm:obstruction){reference-type="ref" reference="thm:obstruction"} rules out a different failure mode: genuinely new roots are added, but a positive fraction remains in one compact region.

# Finite physical audit

The sixteen-level clouds have strictly increasing ranks. The normalized and raw compact counts are:

  channel                         first rank   final rank   compact-count growth
  ----------------------------- ------------ ------------ ----------------------
  left, normalized $|z|\le2$               4           35                     31
  right, normalized $|z|\le2$              4           34                     30
  left, raw $|z|\le1$                      4           35                     31
  right, raw $|z|\le1$                     4           34                     30

Every audited normalized root lies in $|z|\le2$. Every raw selected resonance lies in the unit disk, and the largest raw modulus is $0.868592$.

The raw statement is finite. Although Markov resonances before Hardy scaling lie in the unit disk at fixed positive noise, the chosen $0.85$ scaling could in principle move some bulk roots beyond one at smaller unobserved scales. The theorem-level direct-normalization obstruction does not depend on that finite raw-radius observation.

# Why reciprocal zeros are different

For a compact operator with nonzero eigenvalues $\lambda_j\to0$, the Fredholm determinant has zeros at $$z_j=\lambda_j^{-1}.$$ The newly added reciprocal zeros can escape every compact set. Their integer divisor may therefore remain locally finite even though the resonance empirical measure is tight or even converges to a point at zero.

Inversion is singular at the resonance accumulation point. It does not preserve probability tightness, and Theorem [\[thm:obstruction\]](#thm:obstruction){reference-type="ref" reference="thm:obstruction"} cannot be applied to the reciprocal cloud without a separate hypothesis.

This is precisely the fixed-noise architecture of the regularized determinant constructed in RH-7 [@WangRH7]. The next paper restores the finite identity between the characteristic polynomial in $\lambda$ and the Fredholm polynomial in $z$.

# Route consequence

The following routes are now separated:

1.  raw or centered resonances used directly as zeros: rejected;

2.  repeated fixed factors: rejected by RH-219;

3.  reciprocal resonance zeros at fixed noise: operator-theoretically valid;

4.  a reciprocal small-noise divisor: still open and must pass local-count and omitted-tail tests.

No small-noise obstruction for reciprocal zeros is proved here. Gate A remains open, as do all self-adjoint, counting-law, arithmetic, and zeta identification stages.
