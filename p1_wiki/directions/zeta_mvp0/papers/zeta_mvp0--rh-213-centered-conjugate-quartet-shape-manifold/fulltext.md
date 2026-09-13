---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-213-centered-conjugate-quartet-shape-manifold"
canonical_tex: "zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold/main.pdf"
source_sha256: "d7dd434226a9c43c63214525b532ea05cc17703b3c0376bd0dc9268308f14a19"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Centered Conjugate-Quartet Shape Manifold Exact Coordinates Behind the Physical Quartic Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-213-centered-conjugate-quartet-shape-manifold/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Centered-RMS normalization did not contract the physical quartic flow in RH-212, but it exposed a stronger exact structure. We classify every branch-labeled quartet consisting of two conjugate pairs, with zero barycenter and unit mean square modulus. In canonical coordinates its roots are $$\sqrt u\pm i\sqrt{(1-u)(1+\eta)},\qquad
   -\sqrt u\pm i\sqrt{(1-u)(1-\eta)},$$ where $0\le u\le1$ and $-1\le\eta\le1$. Its monic polynomial is $$z^4+(2-4u)z^2+4\sqrt u(1-u)\eta z
         +1-\eta^2(1-u)^2.$$ Consequently the three nontrivial coefficients satisfy the exact algebraic identity $$c_3^2=4(2-c_2)(1-c_4).$$

  The interior of the branch-labeled quotient is a smooth two-dimensional surface; explicit inverse formulas recover $(u,\eta)$. Boundary fibers are identified: the entire $u=1$ edge collapses to the double pair $\{\pm1\}$, and branch labels lose orientation at $u=0$. All 32 physical quartets in the sixteen-level RH-212 atlas satisfy the manifold identity with maximum floating residual $8.81\times10^{-15}$; 400 random formula checks have coefficient error at most $6.67\times10^{-16}$.

  This paper provides an exact finite-dimensional quotient, not a small-noise limit or dynamical law. Gate A remains open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  The Centered Conjugate-Quartet Shape Manifold\
  Exact Coordinates Behind the Physical Quartic Flow
```

## Markdown 正文

# From a failed contraction to an exact quotient

RH-212 compared raw, determinant-radius, and centered-RMS coefficient flows [@WangRH212]. The centered normalization did not reduce adjacent variation, so it cannot presently be called a renormalization fixed point. Nevertheless it imposes two exact constraints: $$\label{eq:centerconstraints}
 \sum_{j=1}^{4}q_j=0,
 \qquad \frac14\sum_{j=1}^{4}|q_j|^2=1.$$ The inherited real finite operators also force conjugate closure. These three facts reduce the apparent three-coefficient family to two real shape coordinates.

The objective here is purely algebraic: classify that quotient completely, including its boundary identifications. No dependence on $\sigma$ is used in the proof.

# Canonical form

Let a branch-labeled conjugate quartet be $$\label{eq:generalpairs}
 \alpha\pm i b,\qquad \gamma\pm i d,
 \qquad \alpha,\gamma\in\mathbb R,\quad b,d\ge0.$$ The label records which pair lies on the positive-real and negative-real branch whenever those branches are distinct.

[\[lem:center\]]{#lem:center label="lem:center"} If the quartet in [\[eq:generalpairs\]](#eq:generalpairs){reference-type="eqref" reference="eq:generalpairs"} is centered, then $\gamma=-\alpha$. After ordering the branches one may write $$\label{eq:abd}
 a\pm ib,\qquad -a\pm id,qquad a,b,d\ge0.$$ If it also has unit mean square modulus, then $$\label{eq:rmsrelation}
 a^2+\frac{b^2+d^2}{2}=1.$$

The root sum is $2(\alpha+\gamma)$, proving the first statement. Relabeling sets $a=|\alpha|$. The sum of squared moduli is $2(a^2+b^2)+2(a^2+d^2)$; division by four gives [\[eq:rmsrelation\]](#eq:rmsrelation){reference-type="eqref" reference="eq:rmsrelation"}.

# Shape coordinates

Set $$\label{eq:coordinates}
 u=a^2,
 \qquad
 \eta=\frac{b^2-d^2}{b^2+d^2}$$ when $b^2+d^2>0$. Equation [\[eq:rmsrelation\]](#eq:rmsrelation){reference-type="eqref" reference="eq:rmsrelation"} gives $$\label{eq:bd}
 b^2=(1-u)(1+\eta),\qquad
 d^2=(1-u)(1-\eta).$$ Nonnegativity is equivalent to $$\label{eq:rectangle}
 0\le u\le1,qquad -1\le\eta\le1.$$

[\[thm:param\]]{#thm:param label="thm:param"} For every $(u,\eta)$ in [\[eq:rectangle\]](#eq:rectangle){reference-type="eqref" reference="eq:rectangle"}, the multiset $$\label{eq:roots}
 \begin{aligned}
 q_{1,2}&=\sqrt u\pm i\sqrt{(1-u)(1+\eta)},\\
 q_{3,4}&=-\sqrt u\pm i\sqrt{(1-u)(1-\eta)}
 \end{aligned}$$ is conjugate closed, centered, and has unit mean square modulus. Conversely, every quartet of the form [\[eq:abd\]](#eq:abd){reference-type="eqref" reference="eq:abd"} satisfying [\[eq:rmsrelation\]](#eq:rmsrelation){reference-type="eqref" reference="eq:rmsrelation"} is represented by [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"}.

The forward assertions follow by direct substitution. Conversely set $u=a^2$ and use [\[eq:coordinates\]](#eq:coordinates){reference-type="eqref" reference="eq:coordinates"}; then [\[eq:rmsrelation\]](#eq:rmsrelation){reference-type="eqref" reference="eq:rmsrelation"} yields [\[eq:bd\]](#eq:bd){reference-type="eqref" reference="eq:bd"}.

For $0<u<1$, branch ordering makes the representation unique. At $u=1$, $b=d=0$ and every $\eta$ gives the same double pair. At $u=0$, the two branches share real part zero and changing $\eta$ to $-\eta$ merely swaps the two conjugate pairs as an unlabeled multiset. These are quotient fibers, not failures of the formula.

# Coefficient map and algebraic image

Let $$Q_{u,\eta}(z)=\prod_{j=1}^{4}(z-q_j)
 =z^4+c_2z^2+c_3z+c_4.$$

[\[thm:coeff\]]{#thm:coeff label="thm:coeff"} The coefficient map $\Phi:(u,\eta)\mapsto(c_2,c_3,c_4)$ is $$\label{eq:coefficients}
 \boxed{
 \begin{aligned}
 c_2&=2-4u,\\
 c_3&=4\sqrt u(1-u)\eta,\\
 c_4&=1-\eta^2(1-u)^2.
 \end{aligned}}$$ In particular, $$\label{eq:manifoldidentity}
 \boxed{c_3^2=4(2-c_2)(1-c_4).}$$

Factor the two conjugate quadratics: $$((z-a)^2+b^2)((z+a)^2+d^2).$$ Expanding and substituting $a^2=u$ and [\[eq:bd\]](#eq:bd){reference-type="eqref" reference="eq:bd"} gives [\[eq:coefficients\]](#eq:coefficients){reference-type="eqref" reference="eq:coefficients"}. Squaring the formula for $c_3$ and using $2-c_2=4u$ and $1-c_4=\eta^2(1-u)^2$ proves [\[eq:manifoldidentity\]](#eq:manifoldidentity){reference-type="eqref" reference="eq:manifoldidentity"}.

The identity alone is not the full semialgebraic description. Since $u=(2-c_2)/4$, the image also satisfies $$\label{eq:inequalities}
 -2\le c_2\le2,qquad
 1-\frac{(2+c_2)^2}{16}\le c_4\le1.$$ Together with [\[eq:manifoldidentity\]](#eq:manifoldidentity){reference-type="eqref" reference="eq:manifoldidentity"}, these bounds describe the real coefficient image, with the boundary identifications above.

# Inverse formulas and smooth interior

[\[prop:inverse\]]{#prop:inverse label="prop:inverse"} For $0<u<1$, the branch-labeled coordinates are recovered from the coefficients by $$\label{eq:inverse}
 u=\frac{2-c_2}{4},
 \qquad
 \eta=\frac{c_3}{4\sqrt u(1-u)}.$$ Moreover, $\Phi$ has differential of rank two throughout $(0,1)\times(-1,1)$.

The inverse is immediate from [\[eq:coefficients\]](#eq:coefficients){reference-type="eqref" reference="eq:coefficients"}. The $u$ derivative has first component $-4$, while the $\eta$ derivative has first component zero and second component $4\sqrt u(1-u)>0$. They are linearly independent.

Thus the normalized physical quartic does not occupy a generic three-dimensional real coefficient body. It lies on a smooth two-dimensional interior surface with explicit compactification.

# Finite physical atlas

The RH-212 atlas contains sixteen scales from $0.04$ to $0.00125$ and two channels at each scale. For every endpoint we recover $(u,\eta)$ from the normalized roots and independently reconstruct the coefficients using [\[eq:coefficients\]](#eq:coefficients){reference-type="eqref" reference="eq:coefficients"}.

  diagnostic                             maximum over 32 endpoints
  ------------------------------------ ---------------------------
  manifold identity residual                  $8.81\times10^{-15}$
  coefficient reconstruction error            $8.81\times10^{-15}$
  coordinate reconstruction error                 below $10^{-13}$
  root multiset reconstruction error             floating roundoff

In a separate 400-case random audit over the interior rectangle, direct root expansion and formula coefficients disagree by at most $6.67\times10^{-16}$. These computations verify the implementation; the theorems themselves are elementary exact algebra.

# Interpretation for the divisor-first route

The result changes the status of centered-RMS normalization. It is not a successful contraction in RH-212, but it is the canonical quotient by root translation and positive scale. The remaining motion has two distinct components:

Axial coordinate $u$

:   the squared separation of the two real branch lines;

Asymmetry coordinate $\eta$

:   the imbalance between the squared imaginary heights of the positive and negative real branches.

This vocabulary is intrinsic to the branch-labeled conjugate quartet. It does not identify the branches with arithmetic objects and does not produce an infinite spectrum.

# Claim boundary

Nothing in the algebra proves that $(u_\sigma,\eta_\sigma)$ converges, that $u_\sigma$ is monotone at all levels, or that the finite points lie on an autonomous orbit. It also discards the center and RMS radius, which must be restored before reconstructing the raw divisor. Those questions are separated into later layers.

The exact conclusion is the shape manifold and its coordinate dictionary. Gate A remains open; Gates B--E, Hilbert--Pólya, zeta-zero identification, and RH are untouched.
