---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-weighted-reflection-channel-divisor"
canonical_tex: "henon_dynamics/henon_weighted_reflection_channel_divisor/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_weighted_reflection_channel_divisor/paper/paper.pdf"
source_sha256: "9aca5cdd5aac13de0e2d137c1e67c457e85c402942b734361155eee25c819a2a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Two-Fugacity Divisor of the\linebreak Weighted Hénon Reflection Euler Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_weighted_reflection_channel_divisor>)
- [规范 TeX](<../../../../../henon_dynamics/henon_weighted_reflection_channel_divisor/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_weighted_reflection_channel_divisor/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_weighted_reflection_channel_divisor/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_weighted_reflection_channel_divisor/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The orbit-resolved reflection Euler product of the full Hénon horseshoe depends on a positive defect weight $q$, but its previously known all-channel continuation was restricted to $q=1$. We lift each orbit monomial by setting $w=qz$, so that $z^nq^{S_n\chi}=z^{n-S_n\chi}w^{S_n\chi}$. Primitive Möbius subtraction and Euler repetition then give the exact two-variable identity $$\log\mathcal Z^{\sharp}(z,w)
   =\sum_{m\ge1}c_m\frac{2w^m}{1-z^{2m}-w^{2m}},\qquad
   c_m=\frac1m\prod_{\substack{p\mid m\\p\ \mathrm{odd}}}(1-p).$$ Every $c_m$ is nonzero. In the bidisk, the hypersurfaces $\mathcal H_m=\{z^{2m}+w^{2m}=1\}$ are smooth and form a locally finite effective divisor, while the channel sum converges normally on its complement. Restriction to $w=qz$, $q>0$, recovers the weighted orbit product. The $m$th channel has $2m$ explicitly located roots and a nonzero closed principal coefficient at each root, so every one is exponentially essential. We do not infer a dense natural boundary, introduce a weighted Lind zeta, or construct an operator or arithmetic trace.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: 'The Two-Fugacity Divisor of theWeighted Hénon Reflection Euler Family'
```

## Markdown 正文

# The weighted packet and the missing global parameter

For the area-preserving map $H(x,y)=(6-x^2-y,x)$, the inherited horseshoe coding identifies the odd reflection packets used below with reversal-fixed binary words [@DevaneyNitecki1979; @Arai2007]. Let $A_n$ be the primitive marked packet at odd period $n$ and define $$\chi(s)=\mathbf 1\{s_{-1}=s_1\},\qquad
 S_n\chi(s)=\sum_{j=0}^{n-1}\chi(\sigma^js).$$ The orbit-resolved product is $$\label{eq:original-product}
 \mathcal Z_{\rm orb}(z,q)=\prod_{\substack{n\ge1\\n\ \mathrm{odd}}}
 \prod_{\omega\in A_n}
 \left(1-z^nq^{S_n\chi(\omega)}\right)^{-1},\qquad q>0.$$ It is a marked reflection-packet product, not the full Lind zeta of a flip action.

The preceding transfer calculation gives, for $n=2h+1$, $$\begin{aligned}
 F_n(q)&=2q(1+q^2)^h,\label{eq:all-polynomial}\\
 E_n(q)&=\sum_{k\mid n}\mu(k)F_{n/k}(q^k),\label{eq:primitive-polynomial}\end{aligned}$$ where $F_n$ counts all reflection words and $E_n$ counts the primitive marked packet with its individual energy weights. If $E(z,q)=\sum_{n\ \mathrm{odd}}E_n(q)z^n$, expansion of the Euler factors gives $$\label{eq:repetition}
 \log\mathcal Z_{\rm orb}(z,q)=\sum_{r\ge1}\frac1rE(z^r,q^r)$$ in the disk of absolute convergence. At $q=1$, grouping the Möbius and repetition indices exposes infinitely many rational channels. Our goal is to retain the full weight without postulating a new external zeta formula.

# A two-fugacity lift

The inequality $0\le S_n\chi\le n$ permits a bivariate lift of every orbit factor. Set $w=qz$ and write $$\label{eq:monomial-lift}
 z^nq^{S_n\chi}=z^{n-S_n\chi}w^{S_n\chi}.$$ We denote by $\mathcal Z^{\sharp}(z,w)$ the resulting formal Euler product. Equation [\[eq:all-polynomial\]](#eq:all-polynomial){reference-type="eqref" reference="eq:all-polynomial"} immediately becomes a rational all-word function.

[\[prop:all-word\]]{#prop:all-word label="prop:all-word"} For sufficiently small $z,w$, $$\label{eq:Fsharp}
 F^{\sharp}(z,w)
 :=\sum_{h\ge0}2w(z^2+w^2)^h
 =\frac{2w}{1-z^2-w^2}.$$ Primitive subtraction and repetition take the forms $$\begin{aligned}
 E^{\sharp}(z,w)
 &=\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}
   \mu(k)F^{\sharp}(z^k,w^k),\label{eq:Esharp}\\
 \log\mathcal Z^{\sharp}(z,w)
 &=\sum_{r\ge1}\frac1rE^{\sharp}(z^r,w^r).\label{eq:Zsharp-repeat}\end{aligned}$$ On $w=qz$, these identities agree coefficientwise with [\[eq:primitive-polynomial\]](#eq:primitive-polynomial){reference-type="eqref" reference="eq:primitive-polynomial"}--[\[eq:repetition\]](#eq:repetition){reference-type="eqref" reference="eq:repetition"}.

In a reflection word of length $2h+1$, the fixed boundary edge contributes one unit of energy. Each of the remaining $h$ paired edges either changes the symbol, contributing $z^2$, or preserves it, contributing $w^2$; the initial binary symbol contributes the factor $2w$. This proves [\[eq:Fsharp\]](#eq:Fsharp){reference-type="eqref" reference="eq:Fsharp"}. A period-$n/k$ word repeated $k$ times dilates both exponents in [\[eq:monomial-lift\]](#eq:monomial-lift){reference-type="eqref" reference="eq:monomial-lift"} by $k$, so ordinary odd Möbius inversion gives [\[eq:Esharp\]](#eq:Esharp){reference-type="eqref" reference="eq:Esharp"}. Expanding $-\log(1-u)$ yields [\[eq:Zsharp-repeat\]](#eq:Zsharp-repeat){reference-type="eqref" reference="eq:Zsharp-repeat"}. Substitution $w=qz$ reverses [\[eq:monomial-lift\]](#eq:monomial-lift){reference-type="eqref" reference="eq:monomial-lift"} and recovers the original formulas.

# Exact channel regrouping

For $m\ge1$, define $$\label{eq:Psi}
 \Psi_m(z,w)=\frac{2w^m}{1-z^{2m}-w^{2m}}.$$

[\[thm:channels\]]{#thm:channels label="thm:channels"} In the initial domain of absolute convergence, $$\label{eq:channels}
 \log\mathcal Z^{\sharp}(z,w)=\sum_{m\ge1}c_m\Psi_m(z,w),$$ where $$\label{eq:cm}
 c_m=\frac1m\sum_{\substack{k\mid m\\k\ \mathrm{odd}}}k\mu(k)
 =\frac1m\prod_{\substack{p\mid m\\p\ \mathrm{odd}}}(1-p).$$ For every $m$, $c_m\ne0$ and $|c_m|\le1$. Consequently, for fixed $q>0$, $$\label{eq:qchannels}
 \log\mathcal Z_{\rm orb}(z,q)=\sum_{m\ge1}c_m
 \frac{2(qz)^m}{1-(1+q^{2m})z^{2m}}.$$

Insert [\[eq:Esharp\]](#eq:Esharp){reference-type="eqref" reference="eq:Esharp"} into [\[eq:Zsharp-repeat\]](#eq:Zsharp-repeat){reference-type="eqref" reference="eq:Zsharp-repeat"}. A pair consisting of an odd Möbius index $k$ and a repetition index $r$ contributes $$\frac{\mu(k)}r\frac{2w^{kr}}
 {1-z^{2kr}-w^{2kr}}.$$ Grouping by $m=kr$ gives the divisor sum in [\[eq:cm\]](#eq:cm){reference-type="eqref" reference="eq:cm"}. That sum factors over the odd radical of $m$, proving the product formula. No factor $1-p$ vanishes. Moreover $$|c_m|\le \frac1m\prod_{\substack{p\mid m\\p\ \mathrm{odd}}}p\le1.$$ Finally, $w=qz$ in [\[eq:channels\]](#eq:channels){reference-type="eqref" reference="eq:channels"} gives [\[eq:qchannels\]](#eq:qchannels){reference-type="eqref" reference="eq:qchannels"}.

The coefficient $c_m$ is independent of $q$: all weight dependence has moved into the geometry of the channel denominator. This separation is the main reason for using two fugacities rather than treating $q$ as a passive real parameter.

# The bidisk hypersurface divisor

Let $\mathbb D^2=\{(z,w)\in\mathbb C^2:|z|<1,|w|<1\}$ and define $$\label{eq:Hm}
 \mathcal H_m=\{(z,w)\in\mathbb D^2:z^{2m}+w^{2m}=1\},\qquad
 \mathcal H=\bigcup_{m\ge1}\mathcal H_m.$$

[\[thm:divisor\]]{#thm:divisor label="thm:divisor"} Every $\mathcal H_m$ is a smooth reduced hypersurface. The formal sum $\sum_{m\ge1}\mathcal H_m$ is a locally finite effective analytic divisor in the bidisk. The series in [\[eq:channels\]](#eq:channels){reference-type="eqref" reference="eq:channels"} converges normally on compact subsets of $\mathbb D^2\setminus\mathcal H$ and therefore defines a holomorphic function $\mathcal L^{\sharp}$ there. Its exponential is a nonvanishing scalar continuation of the initial Euler germ.

The gradient of $z^{2m}+w^{2m}-1$ is $$(2mz^{2m-1},2mw^{2m-1}).$$ It cannot vanish on $\mathcal H_m$, since simultaneous vanishing would imply $z=w=0$. Thus $\mathcal H_m$ is smooth and reduced.

For a compact $K\subset\mathbb D^2$, choose $r,s<1$ such that $|z|\le r$ and $|w|\le s$ on $K$. Once $m$ is large enough, $r^{2m}+s^{2m}<1$, so $K\cap\mathcal H_m$ is empty. This proves local finiteness.

Now suppose $K\subset\mathbb D^2\setminus\mathcal H$. The finitely many early denominators in [\[eq:Psi\]](#eq:Psi){reference-type="eqref" reference="eq:Psi"} have a positive minimum modulus on $K$. For all sufficiently large $m$, $$|1-z^{2m}-w^{2m}|\ge1-r^{2m}-s^{2m}\ge\tfrac12.$$ Together with $|c_m|\le1$, this gives $|c_m\Psi_m(z,w)|\le4s^m$. The Weierstrass test proves normal convergence. Agreement with the initial logarithm follows from [\[thm:channels\]](#thm:channels){reference-type="ref" reference="thm:channels"}, and exponentiation gives the asserted continuation.

The theorem does not classify intersections $\mathcal H_m\cap\mathcal H_j$. Such joint complex collisions are unnecessary for the fixed-positive-weight fibers considered next.

# Moving roots on positive-weight fibers

Fix $q>0$ and restrict to $w=qz$. The $m$th denominator in [\[eq:qchannels\]](#eq:qchannels){reference-type="eqref" reference="eq:qchannels"} has the roots $$\label{eq:roots}
 \alpha_{m,\ell}(q)=\rho_m(q)e^{\pi i\ell/m},\qquad
 \rho_m(q)=(1+q^{2m})^{-1/(2m)},\qquad 0\le\ell<2m.$$

[\[prop:radii\]]{#prop:radii label="prop:radii"} For every $q>0$, $\rho_m(q)$ is strictly increasing in $m$ and $$\label{eq:radius-limit}
 \lim_{m\to\infty}\rho_m(q)=\min(1,q^{-1}).$$ Hence two different channels have no common root on a fixed positive-$q$ fiber.

It suffices to show that $x\mapsto x^{-1}\log(1+q^{2x})$ is strictly decreasing. Put $y=q^{2x}$. The numerator controlling its derivative is the negative of $$(1+y)\log(1+y)-y\log y,$$ which is positive for $y>0$. This proves strictness. The limit follows by separating $q<1$, $q=1$, and $q>1$ in the defining formula. Distinct radii preclude a common complex root.

[\[thm:principal\]]{#thm:principal label="thm:principal"} Let $q>0$, $m\ge1$, and $0\le\ell<2m$. Near $\alpha=\alpha_{m,\ell}(q)$, $$\label{eq:principal}
 \log\mathcal Z_{\rm orb}(z,q)=
 \frac{c_m(-1)^\ell q^m}{m\sqrt{1+q^{2m}}}
 \frac1{1-z/\alpha}+G_{m,\ell,q}(z),$$ where $G_{m,\ell,q}$ is holomorphic. Thus the scalar continuation has an exponential essential singularity at every root in [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"}.

Set $v=1-z/\alpha$. Since $\alpha^{2m}=(1+q^{2m})^{-1}$ and $\alpha^m=(-1)^\ell/\sqrt{1+q^{2m}}$, $$\begin{aligned}
 1-(1+q^{2m})z^{2m}&=2mv+O(v^2),\\
 2(qz)^m&=\frac{2(-1)^\ell q^m}{\sqrt{1+q^{2m}}}+O(v).\end{aligned}$$ By [\[prop:radii\]](#prop:radii){reference-type="ref" reference="prop:radii"}, no other channel denominator vanishes at $\alpha$. Normal convergence from [\[thm:divisor\]](#thm:divisor){reference-type="ref" reference="thm:divisor"} makes their sum holomorphic in a small neighborhood. Multiplication by the nonzero $c_m$ gives [\[eq:principal\]](#eq:principal){reference-type="eqref" reference="eq:principal"}; exponentiating a nonzero simple pole gives an essential singularity.

The radii and their limit locate the divisor but do not by themselves prove that complex roots approach every point of the limiting circle. We reserve that angular accumulation and the resulting natural-boundary question for a separate theorem.

# Executable certificate and claim boundary

The primary certificate compares [\[eq:qchannels\]](#eq:qchannels){reference-type="eqref" reference="eq:qchannels"}, coefficient by coefficient as exact polynomials in $q$, with the primitive/repetition law through degree $48$. An independent sparse-polynomial implementation extends the comparison through degree $64$ without importing the primary module. The test suite checks degree $100$, reconstructs the first $128$ channel coefficients, and audits all complex roots through channel $24$ at $q=1/2,1,2$. Dependency hashes lock the proofs, certificates, and PDFs of P69, P70, and P72. These finite checks guard the implementation; the all-$m$ statements follow from the proofs above.

The resulting object has a genuine two-variable analytic divisor and exact fiberwise singular data. We make no comparison with a Lind zeta away from $q=1$, because no such source formula has been supplied. We construct no transfer, nuclear, trace-class, or self-adjoint operator, and the integer channel label $m$ has no certified rational-prime or von-Mangoldt meaning. No arithmetic advance or Route-B authorization follows.
