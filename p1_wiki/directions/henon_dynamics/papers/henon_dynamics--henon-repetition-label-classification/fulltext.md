---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-repetition-label-classification"
canonical_tex: "henon_dynamics/henon_repetition_label_classification/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_repetition_label_classification/paper/paper.pdf"
source_sha256: "6aa3708030a80348aae7645c48592126857fc7e959d9c05a6102557121c9274f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Classification of Repetition-Compatible Scalar Labels for Hénon Monodromy Units

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_repetition_label_classification>)
- [规范 TeX](<../../../../../henon_dynamics/henon_repetition_label_classification/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_repetition_label_classification/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_repetition_label_classification/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Every periodic multiplier of the integral area-preserving Hénon map is an algebraic unit. Could a natural scalar transform nevertheless turn these units into rational prime labels while preserving all orbit repetitions? We classify the functorial rational category. If $R\in\mathbb Q(X)^\times$ satisfies $R(X^r)=R(X)^r$ identically for every $r\ge1$, then $R(X)=X^k$ for an integer $k$. The divisor proof is global and uses no orbit cutoff. Hence every rational repetition-compatible label of a Hénon multiplier remains an algebraic unit and cannot be a rational prime. We also classify continuous positive labels on the unstable ray $X>1$ under the repetition law: they are exactly $X^c$ with $c\in\mathbb R$. The pressure-normalized label $X^{h_*}$ from the preceding prime-orbit theorem is therefore the precise nonrational survivor. A finite adversarial scan of 2,187 Laurent polynomials and explicit trace/determinant mutations independently checks the theorem's boundaries.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
date: 'Preprint, August 2026'
title: |
  A Classification of Repetition-Compatible Scalar Labels\
  for Hénon Monodromy Units
```

## Markdown 正文

# The scalar repetition problem

For a primitive Hénon orbit with multiplier $\lambda$, the $r$th repetition has multiplier $\lambda^r$. A scalar Euler label $R(\lambda)$ preserves the prime-power law only if $$\label{eq:law}
R(\lambda^r)=R(\lambda)^r.$$ We first impose functoriality: [\[eq:law\]](#eq:law){reference-type="eqref" reference="eq:law"} is an identity on the multiplicative group $\mathbb G_m$, not a coincidence on a finite orbit table. This is the minimal source-native rational category.

# Rational classification

[\[thm:rational\]]{#thm:rational label="thm:rational"} Let $R\in\mathbb C(X)^\times$. If $$R(X^r)=R(X)^r$$ as rational functions for every integer $r\ge1$, then $$\boxed{R(X)=X^k}$$ for a unique $k\in\mathbb Z$.

It is enough to use $r=2$. Let $D=\operatorname{div}(R)$ on $\mathbb P^1$. The identity gives $$[2]^*D=2D,
\qquad [2](X)=X^2.$$ Suppose a point $a\in\mathbb C^\times$ lies in the support of $D$. Every $2^m$th root of $a$ then lies in the support of $[2]^{m*}D=2^mD$. The union of these root sets has unbounded cardinality as $m$ grows, contradicting the finite support of a rational divisor. Hence $D$ is supported on $\{0,\infty\}$, so $R(X)=cX^k$ for $c\ne0$ and $k\in\mathbb Z$. Substitution into $R(X^2)=R(X)^2$ gives $c=c^2$, hence $c=1$.

The same proof works over $\mathbb Q$ and any characteristic-zero field. The statement does not assume that the actual Hénon multiplier set is Zariski dense; it explicitly classifies rules functorial on all of $\mathbb G_m$.

# Hénon unit obstruction

The preceding all-period theorem proves that every $H_6$ periodic multiplier $\lambda$ and its inverse are algebraic integers.

[\[cor:noprime\]]{#cor:noprime label="cor:noprime"} For every $R$ in Theorem [\[thm:rational\]](#thm:rational){reference-type="ref" reference="thm:rational"}, $R(\lambda)$ is an algebraic unit. If it is rational, it is $\pm1$. It can never be a rational prime.

Theorem [\[thm:rational\]](#thm:rational){reference-type="ref" reference="thm:rational"} gives $R(\lambda)=\lambda^k$, which is a unit. The only units in $\mathbb Q$ integral over $\mathbb Z$ are $\pm1$.

Two obvious alternatives fail before this corollary is applied. Trace uses $$T(X)=X+X^{-1},
\qquad T(X^2)=T(X)^2-2,$$ not $T(X)^2$. The fixed-point determinant uses $$F(X)=2-X-X^{-1}$$ and also fails the square law. Their repetition sequences are Chebyshev or cyclic-resultant data, not powers of one primitive scalar label.

# Continuous positive unstable-ray classification

The rational theorem must not be overextended to the pressure normalization.

[\[thm:continuous\]]{#thm:continuous label="thm:continuous"} Let $L:(1,\infty)\to\mathbb R_{>0}$ be continuous and suppose $$L(X^r)=L(X)^r$$ for every $X>1$ and integer $r\geq1$. Then there is a unique $c\in\mathbb R$ such that $$L(X)=X^c.$$

Set $f(t)=\log L(e^t)$ for $t>0$. The repetition law says $f(rt)=rf(t)$ for every positive integer $r$. If $q=m/n$ is a positive rational, then $$n f(qt)=f(nqt)=f(mt)=m f(t),$$ so $f(qt)=qf(t)$. Taking $t=1$ and approximating any positive real by positive rationals, continuity gives $f(t)=t f(1)$. Put $c=f(1)$ and exponentiate.

For $c\in\mathbb Z$ this agrees with Theorem [\[thm:rational\]](#thm:rational){reference-type="ref" reference="thm:rational"}. The pressure-normalized label from the entropy-one Hénon suspension has $$c=h_*,\qquad L(|\lambda|)=|\lambda|^{h_*}.$$ No theorem in this batch says that $h_*$ is integral, rational, algebraic, or transcendental. Thus this label is a genuine survivor, not a loophole that Corollary [\[cor:noprime\]](#cor:noprime){reference-type="ref" reference="cor:noprime"} already closes.

# Finite adversarial certificate

The code scans all $3^7=2{,}187$ Laurent polynomials supported on exponents $-3,\ldots,3$ with coefficients in $\{-1,0,1\}$. Exactly eight satisfy the square law: zero and the seven monomials $X^k$ with coefficient one. The zero polynomial is retained only as a test sentinel and is excluded from Theorem [\[thm:rational\]](#thm:rational){reference-type="ref" reference="thm:rational"}. Separate mutations verify that trace and $2-X-X^{-1}$ fail. C46's certificate and README are hash locked.

# Evaluator verdict and next road

The rational scalar lane is completely closed, with strict tuple $$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm PARTIAL},A4_{\rm FORMAL})$$ and overall `ROUTE_A_REJECTED`. The continuous unstable-ray pressure-power lane remains `ROUTE_A_EXPLORATORY`; coordinatewise maxima are not combined into a certificate. Route B is not authorized for either lane.

The next large theorem must address one of three genuinely different categories: arithmetic/transcendence of $|\lambda|^{h_*}$, nonlocal cross-orbit packet labels, or a distributional/scattering trace not based on termwise rational primes.

# Conclusion

Exact repetition is highly rigid. In the rational category it permits only integer powers, and the all-period Hénon unit theorem then forbids rational prime labels. Pressure normalization survives precisely because it exits that category. The batch therefore ends with one sharply isolated positive candidate rather than an open-ended list of scalar repairs.

9 S. Lang, *Algebra*, revised third edition, Springer, 2002. J. H. Silverman, *The Arithmetic of Dynamical Systems*, Springer, 2007.
