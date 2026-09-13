---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-224-global-cloud-gauge-tightness"
canonical_tex: "zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness/main.pdf"
source_sha256: "5efdc1e9ab20278c92b3a9511c78f4ddb7c294bca1246586e9435d6d625b1c56"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Global Cloud Gauge and Empirical-Root Tightness Exact Moment Compactness for Rank-Growing Conjugate Spectra

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-224-global-cloud-gauge-tightness/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A rank-growing spectral cloud requires one gauge for the whole cloud, not a separate normalization for each quartet or shell. For any nonconstant finite multiset $\Lambda$, we remove its barycenter $m_\Lambda$ and divide by its centered RMS radius $s_\Lambda$. The associated empirical probability measure then has exact complex mean zero and exact second absolute moment one.

  This elementary identity has a strong uniform consequence. For every family of globally normalized clouds, $$\mu_\Lambda(\{|z|>R\})\le R^{-2}.$$ Hence the empirical measures are uniformly tight on $\mathbb C$ and every sequence has a weakly convergent subsequence. The result is exact and independent of the ranks, shell geometry, or noise schedule.

  For the 32 RH-222 clouds, direct recomputation agrees with the archived gauge to machine precision. The maximum mean residual is $4.99\times10^{-17}$, the maximum second-moment error is $6.67\times10^{-16}$, the maximum fourth moment is $2.31691$, and the largest normalized modulus is $1.83188$. All tested tail inequalities have positive slack.

  Tightness provides macroscopic probability compactness. It neither selects a unique weak limit nor proves local finiteness of the unweighted root divisor. That distinction becomes the next exact obstruction.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Global Cloud Gauge and Empirical-Root Tightness\
  Exact Moment Compactness for Rank-Growing Conjugate Spectra
```

## Markdown 正文

# One gauge per growing cloud

RH-220 completed the center-radius-shape dictionary for one quartet, and RH-222 extends the root set to ranks $4$ through $35$ [@WangRH222]. Applying a separate gauge to each shell would erase their relative positions. We instead normalize the entire selected multiset at once.

Let $$\Lambda=\{\lambda_1,\ldots,\lambda_n\}\subset\mathbb C,\qquad n\ge2,$$ with not all roots equal. Define $$\label{eq:gauge}
 m_\Lambda=\frac1n\sum_{j=1}^n\lambda_j,\qquad
 s_\Lambda=\left(\frac1n\sum_{j=1}^n
 |\lambda_j-m_\Lambda|^2\right)^{1/2}>0,$$ and normalized roots $$q_j=\frac{\lambda_j-m_\Lambda}{s_\Lambda}.$$ The empirical measure is $$\label{eq:empirical}
 \mu_\Lambda=\frac1n\sum_{j=1}^n\delta_{q_j}.$$

# Exact moment identities

[\[prop:moments\]]{#prop:moments label="prop:moments"} Every globally normalized cloud satisfies $$\label{eq:identities}
 \int_\mathbb Cz\,d\mu_\Lambda(z)=0,\qquad
 \int_\mathbb C|z|^2\,d\mu_\Lambda(z)=1.$$ If $\Lambda$ is conjugate closed, then $\mu_\Lambda$ is invariant under complex conjugation and $m_\Lambda\in\mathbb R$.

The first identity is $$\frac1{ns_\Lambda}\sum_j(\lambda_j-m_\Lambda)=0.$$ The second is exactly the definition of $s_\Lambda$. Conjugation permutes the roots and therefore the atoms; it also fixes their mean.

These identities do not depend on the root ordering. They remain valid when real singleton shells make the rank odd.

# Uniform tightness

[\[thm:tight\]]{#thm:tight label="thm:tight"} Let $\{\Lambda_\alpha\}$ be any family of nonconstant finite clouds, each normalized by [\[eq:gauge\]](#eq:gauge){reference-type="eqref" reference="eq:gauge"}. Then $$\label{eq:tail}
 \sup_\alpha\mu_{\Lambda_\alpha}(\{|z|>R\})
 \le \min(1,R^{-2}),\qquad R>0.$$ Consequently the family $\{\mu_{\Lambda_\alpha}\}\subset\mathcal P(\mathbb C)$ is uniformly tight.

On $\{|z|>R\}$, one has $1\le |z|^2/R^2$. Therefore $$\mu_{\Lambda_\alpha}(|z|>R)
 \le R^{-2}\int |z|^2\,d\mu_{\Lambda_\alpha}=R^{-2}$$ by Proposition [\[prop:moments\]](#prop:moments){reference-type="ref" reference="prop:moments"}. For every $\varepsilon>0$, choosing $R\ge\varepsilon^{-1/2}$ leaves mass at most $\varepsilon$ outside the compact closed disk.

[\[cor:prok\]]{#cor:prok label="cor:prok"} Every sequence of globally normalized empirical cloud measures has a weakly convergent subsequence in $\mathcal P(\mathbb C)$.

The complex plane is a Polish space. Apply Prokhorov's theorem to Theorem [\[thm:tight\]](#thm:tight){reference-type="ref" reference="thm:tight"}; see @Billingsley1999.

This closes the tightness item in the RH-221 roadmap at the level of empirical probability measures. No numerical asymptotic fit is needed.

# What weak convergence preserves

If $\mu_{n_j}\Rightarrow\mu$, conjugation symmetry passes to the limit because bounded continuous test functions can be conjugated. The mean and second moment require care: $z$ and $|z|^2$ are unbounded. Portmanteau gives only $$\int |z|^2\,d\mu(z)\le1.$$ Equality needs uniform integrability of $|z|^2$. A uniform $(2+\epsilon)$ moment bound would suffice, but the finite maximum fourth moment reported below is not an all-level theorem.

Thus one must not infer that every subsequential limit automatically retains the complete RMS gauge. Mass can vanish to infinity while carrying a nonzero fraction of the second moment, even though probability tightness holds.

# Physical audit

For each of the 32 endpoints, the raw selected roots are normalized again, without reading the archived normalized array. The two representations are then compared. Tail masses are evaluated at $$R=1,\;1.25,\;1.5,\;2,\;3$$ against the exact bound [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}.

  diagnostic                     maximum or minimum
  -------------------------- ----------------------
  absolute empirical mean      $4.99\times10^{-17}$
  second-moment error          $6.67\times10^{-16}$
  fourth absolute moment                  $2.31691$
  normalized root modulus                 $1.83188$
  minimum tail-bound slack                $0.11111$

In particular every audited normalized root lies inside $|z|<2$. This is stronger than the universal $75\%$ mass guarantee at $R=2$, but it is only a finite observation.

For reference, the theorem supplies scale-independent certificate radii $$R_{0.25}=2,\quad R_{0.10}=\sqrt{10},\quad
 R_{0.05}=\sqrt{20},\quad R_{0.01}=10.$$ These values are deliberately not tuned to the observed maximum.

# Probability mass versus divisor mass

The empirical measure gives each root weight $1/n$. A holomorphic zero divisor gives each simple root integer weight one. Therefore tightness of $\mu_\Lambda$ says that a fixed compact set can contain a fixed *fraction* of an expanding cloud. Multiplying that fraction by $n\to\infty$ may force the integer divisor mass on the same compact set to diverge.

This is not a technicality. Probability-measure compactness and local finiteness of zero divisors are different topologies. The next paper proves their direct incompatibility for a tight rank-growing cloud. The likely escape is to use reciprocal resonances, as in the fixed-noise regularized Fredholm determinant of RH-7 [@WangRH7], rather than the resonances themselves.

# Claim boundary

The exact achievements are:

1.  one affine gauge for each full cloud;

2.  zero mean and unit second moment;

3.  uniform tightness and weak subsequential compactness.

No unique weak measure, all-level fourth-moment bound, unweighted divisor limit, or locally uniform determinant is proved. Gate A remains open, and no later Hilbert--Polya or arithmetic claim is made.
