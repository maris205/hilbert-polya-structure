---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-weighted-reflection-natural-boundary"
canonical_tex: "henon_dynamics/henon_weighted_reflection_natural_boundary/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_weighted_reflection_natural_boundary/paper/paper.pdf"
source_sha256: "3ae489d519f2bc24984a4a8017f1de685455c6bf4e88a12dbe95dc40d9147aea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Weighted Reflection Channels and a Natural-Boundary Circle

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_weighted_reflection_natural_boundary>)
- [规范 TeX](<../../../../../henon_dynamics/henon_weighted_reflection_natural_boundary/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_weighted_reflection_natural_boundary/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_weighted_reflection_natural_boundary/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_weighted_reflection_natural_boundary/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The orbit-resolved reflection Euler product of the full Hénon horseshoe admits a two-variable scalar-channel continuation. We classify the complete complex singular geometry on every positive weight fiber. The $m$th channel has coefficient $$c_m=\frac1m\prod_{\substack{p\mid m\\p\ {\rm odd}}}(1-p)\ne0$$ and poles $$\alpha_{m,k}(q)=(1+q^{2m})^{-1/(2m)}e^{\pi i k/m},
   \qquad 0\le k<2m.$$ For every $q>0$, the channel radii increase strictly to $L(q)=\min(1,q^{-1})$. Each listed point is an exponential essential singularity of the Euler product, while the angular mesh becomes dense. It follows that $|z|=L(q)$ is a natural boundary for the exact unrenormalized punctured continuation. For $q>1$ the limiting circle lies strictly inside the unit disk. The conclusion is deliberately object-specific: an all-channel counterterm changes the function, and no weighted Lind source, transfer operator, arithmetic trace, or Route-B claim is obtained.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  Weighted Reflection Channels and a\
  Natural-Boundary Circle
```

## Markdown 正文

# From the first boundary to the full complex divisor

The area-preserving Hénon map on the frozen horseshoe is conjugate to the full two-shift in the regime used throughout this programme [@DevaneyNitecki1979]. For the cross-axis observable $\chi=\mathbf 1\{s_{-1}=s_1\}$, the earlier orbit-resolved calculation gives the odd reflection polynomial $$F_{2r+1}(q)=2q(1+q^2)^r$$ and the primitive dilation--Möbius inversion $$E_n(q)=\sum_{d\mid n}\mu(d)F_{n/d}(q^d).$$ The associated product is $$\label{eq:product}
 \mathcal Z_{\rm orb}(z,q)=
 \prod_{\substack{n\ge1\\n\ {\rm odd}}}
 \prod_{\omega\in A_n}
 (1-z^nq^{S_n\chi(\omega)})^{-1}.$$ Its first positive convergence boundary is $(1+q^2)^{-1/2}$, where it is essentially singular.

The point of the present paper is that the first boundary is only the first member of a rigid complex divisor. The weighted channel regrouping reads $$\label{eq:channels}
 \log\mathcal Z_{\rm orb}(z,q)=\sum_{m\ge1}c_m\Psi_m(z,q),
 \qquad
 \Psi_m(z,q)=
 \frac{2(qz)^m}{1-(1+q^{2m})z^{2m}},$$ initially in the disk of the Euler product and then on the complement of its locally finite polar set. Here $$\label{eq:cm}
 c_m=\frac1m\sum_{\substack{d\mid m\\d\ {\rm odd}}}d\mu(d)
 =\frac1m\prod_{\substack{p\mid m\\p\ {\rm odd}}}(1-p).$$ In particular no channel disappears.

# Strict separation of channel radii

For $m\ge1$ and $q>0$, put $$\label{eq:rho}
 \rho_m(q)=(1+q^{2m})^{-1/(2m)}.$$

[\[thm:radii\]]{#thm:radii label="thm:radii"} For every fixed $q>0$, $$\rho_1(q)<\rho_2(q)<\rho_3(q)<\cdots$$ and $$\label{eq:limit}
 \lim_{m\to\infty}\rho_m(q)
 =L(q):=\min(1,q^{-1}).$$ Moreover $\rho_m(q)=q^{-1}\rho_m(q^{-1})$.

For $p>0$, let $$N_p(q)=\|(1,q)\|_p=(1+q^p)^{1/p}.$$ The finite-dimensional $\ell^p$ norm of a vector with two nonzero coordinates is strictly decreasing in $p$. Since $\rho_m(q)=N_{2m}(q)^{-1}$, strict increase follows. The standard $p\to\infty$ limit is $N_p(q)\to\max(1,q)$, which proves [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"}. Factoring $q^{2m}$ from [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"} gives the final identity.

Strictness is important: singularities belonging to different channel indices never collide on a positive-weight fiber. This rules out cross-channel cancellation before any local expansion is computed.

# Every complex channel root is essential

The denominator in [\[eq:channels\]](#eq:channels){reference-type="eqref" reference="eq:channels"} has exactly the roots $$\label{eq:roots}
 \alpha_{m,k}(q)=\rho_m(q)e^{\pi i k/m},
 \qquad 0\le k<2m.$$

[\[prop:local\]]{#prop:local label="prop:local"} Fix $q>0$, $m\ge1$, and $0\le k<2m$. With $v=1-z/\alpha_{m,k}(q)$, $$\label{eq:principal}
 \log\mathcal Z_{\rm orb}(z,q)=
 \frac{c_m(-1)^kq^m}{m\sqrt{1+q^{2m}}}
 \frac1v+G_{m,k,q}(z),$$ where $G_{m,k,q}$ is holomorphic near $\alpha_{m,k}(q)$.

The root identity gives $$\alpha_{m,k}(q)^m=
 \frac{(-1)^k}{\sqrt{1+q^{2m}}}.$$ Writing $z=\alpha_{m,k}(q)(1-v)$, we obtain $$1-(1+q^{2m})z^{2m}=2mv+O(v^2)$$ and $$2(qz)^m=
 \frac{2(-1)^kq^m}{\sqrt{1+q^{2m}}}+O(v).$$ Their quotient is the principal term in [\[eq:principal\]](#eq:principal){reference-type="eqref" reference="eq:principal"}. By [\[thm:radii\]](#thm:radii){reference-type="ref" reference="thm:radii"}, every other channel has its poles on a different circle and is therefore holomorphic locally. Normal convergence of the remaining tail supplies $G_{m,k,q}$.

[\[cor:essential\]]{#cor:essential label="cor:essential"} Every point in [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"} is an exponential essential singularity of the continuation of $\mathcal Z_{\rm orb}(\,\cdot\,,q)$.

The coefficient in [\[eq:principal\]](#eq:principal){reference-type="eqref" reference="eq:principal"} is nonzero by [\[eq:cm\]](#eq:cm){reference-type="eqref" reference="eq:cm"}. Exponentiating a nonzero simple pole gives an essential singularity.

# The limiting circle is a natural boundary

For fixed $m$, the arguments in [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"} form the uniform grid $$0,\frac{\pi}{m},\ldots,\frac{(2m-1)\pi}{m}.$$ Its maximum gap is $\pi/m$.

[\[thm:natural\]]{#thm:natural label="thm:natural"} For every $q>0$, no point of the circle $$|z|=L(q)=\min(1,q^{-1})$$ has a neighborhood to which the explicit unrenormalized continuation $\mathcal Z_{\rm orb}(\,\cdot\,,q)$ extends meromorphically. Thus this circle is a natural boundary for that punctured continuation.

Let $z_0=L(q)e^{i\theta}$. Choose a grid angle $\pi k_m/m$ at distance at most $\pi/(2m)$ from $\theta$. By [\[thm:radii\]](#thm:radii){reference-type="ref" reference="thm:radii"}, $$\alpha_{m,k_m}(q)
 =\rho_m(q)e^{\pi i k_m/m}\longrightarrow z_0.$$ Every term of this sequence is an essential singularity by [\[cor:essential\]](#cor:essential){reference-type="ref" reference="cor:essential"}, and the radii are distinct. If a meromorphic continuation existed on a neighborhood of $z_0$, that neighborhood would contain infinitely many of these nonmeromorphic isolated singularities accumulating at its interior point $z_0$. This contradicts the local structure of a meromorphic function [@Conway1978].

The theorem has three regimes. When $0<q<1$, the natural boundary is the unit circle. At $q=1$, it is the unweighted boundary already approached by the positive P72 ladder. When $q>1$, it moves inward to $|z|=q^{-1}$. The last behavior is not a numerical phase transition; it is the exact $\ell^\infty$ limit in [\[thm:radii\]](#thm:radii){reference-type="ref" reference="thm:radii"}.

# Renormalization and operator firewalls

The natural-boundary terminology in [\[thm:natural\]](#thm:natural){reference-type="ref" reference="thm:natural"} refers to analytic continuation of the fixed function [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} through the exact channel continuation [\[eq:channels\]](#eq:channels){reference-type="eqref" reference="eq:channels"}. It does not say that the prescribed divisor cannot be subtracted. An all-channel exponential counterterm can cancel it precisely because the counterterm contains the same complete ledger. The resulting function is a different object.

Likewise, the theorem does not identify a weighted analogue of the full reverse-shift Lind zeta of @KimLeePark2003. No source formula currently supplies such a comparison for $q\ne1$. Nor is the channel continuation itself a transfer determinant: a parameter-dependent diagonal operator can be engineered after the fact, while the direct sum of source-native orbit blocks has a separate compactness gate. Those two notions are compared in the next paper.

In particular, the channel index $m$ has no intrinsic rational-prime meaning, and no prime-power amplitude, explicit formula, self-adjoint operator, zeta-zero correspondence, or Route-B result follows.

# Executable certificate

The main certificate reconstructs forty channels on each of the fibers $q=1/2,1,2$, using high-precision decimal radii to preserve strictness near the limiting circle. It checks every complex root numerically, records the principal coefficient and angular gap, locks nine P70/P72/P75 dependencies, and rejects 24 claim mutations. A separate program reconstructs 192 rows on the fibers $q=0.4,1,2.5$ without importing the main module. Eleven unit tests pass in normal and optimized modes. These finite checks certify the implementation; [\[thm:radii,thm:natural\]](#thm:radii,thm:natural){reference-type="ref" reference="thm:radii,thm:natural"} prove the all-channel claims.
