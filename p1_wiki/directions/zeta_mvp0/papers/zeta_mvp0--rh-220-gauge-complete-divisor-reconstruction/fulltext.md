---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-220-gauge-complete-divisor-reconstruction"
canonical_tex: "zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction/main.pdf"
source_sha256: "cc7b6fe6df337a122a69f7f4b40c51a510020e4810177e940996a40f5e59a0de"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Gauge-Complete Reconstruction of the Physical Quartic Divisor Center, RMS Radius, Shape, and the Next Gate-A Route

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-220-gauge-complete-divisor-reconstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Centered-RMS normalization exposes the exact two-coordinate quartet shape, but it discards spectral center and scale. This paper restores those data and proves a complete affine-gauge dictionary for every nondegenerate conjugate quartet.

  Let $\mu$ be the root barycenter, $r>0$ the centered RMS radius, and $Q_{u,\eta}$ the canonical shape polynomial of RH-213. The raw monic divisor is exactly $$D(z)=r^4Q_{u,\eta}\!\left(\frac{z-\mu}{r}\right)
   =(z-\mu)^4+c_2r^2(z-\mu)^2+c_3r^3(z-\mu)+c_4r^4.$$ Thus $(\mu,r,u,\eta)$ reconstructs both the root multiset and every raw coefficient. Conversely these parameters are recovered from the roots, up to the already classified branch-label fibers on the shape boundary. Shape alone is non-injective: every translation and positive dilation orbit has the same $(u,\eta)$.

  All 32 physical endpoint quartets are reconstructed with maximum root error $3.15\times10^{-16}$ and coefficient error $7.78\times10^{-16}$. An exact gauge-first, shape-second telescoping decomposition is audited on all 30 adjacent channel transitions; eight are gauge-leg dominant and 22 are shape-leg dominant. Neither ledger can be discarded.

  Together with RH-219's fixed-degree obstruction, this yields a route decision: the next Gate-A object must be a rank-growing, gauge-complete physical divisor using one global center and radius per cloud. The present paper closes finite reconstruction only; no growing determinant or Gate-A closure is obtained.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Gauge-Complete Reconstruction of the Physical Quartic Divisor\
  Center, RMS Radius, Shape, and the Next Gate-A Route
```

## Markdown 正文

# Why the quotient must be completed

RH-212 showed that centered-RMS coefficients do not contract more strongly than the raw quartic, while RH-213 proved that they lie on an exact two-dimensional shape manifold [@WangRH212; @WangRH213]. The quotient is valuable because it separates geometry, but it cannot by itself reconstruct the raw spectral factor.

RH-219 further proves that one fixed quartic, even repeated, cannot furnish a locally finite growing spectrum [@WangRH219]. Before moving to larger clouds, the finite factor needs a complete state type: not only shape, but also the affine gauge removed by normalization.

# Gauge and shape data

Let $\Lambda=\{\lambda_1,\ldots,\lambda_4\}$ be a nonconstant conjugate-closed quartet. Define $$\label{eq:gauge}
 \mu=\frac14\sum_{j=1}^{4}\lambda_j,
 \qquad
 r=\left(\frac14\sum_{j=1}^{4}|\lambda_j-\mu|^2\right)^{1/2}>0.$$ Conjugate closure makes $\mu\in\mathbb R$. The normalized roots $$q_j=\frac{\lambda_j-\mu}{r}$$ are centered and have unit mean square modulus. With the branch convention of RH-213 they determine $(u,\eta)$ and $$\label{eq:qpoly}
 Q_{u,\eta}(w)=w^4+c_2w^2+c_3w+c_4,$$ where $$\label{eq:shapecoeff}
 c_2=2-4u,quad
 c_3=4\sqrt u(1-u)\eta,quad
 c_4=1-\eta^2(1-u)^2.$$

# Exact reconstruction theorem

[\[thm:reconstruct\]]{#thm:reconstruct label="thm:reconstruct"} The monic raw divisor of $\Lambda$ is $$\label{eq:master}
 \boxed{
 D(z)=\prod_{j=1}^{4}(z-\lambda_j)
 =r^4Q_{u,\eta}\!\left(\frac{z-\mu}{r}\right).}$$ Equivalently, $$\label{eq:centeredexpansion}
 D(z)=(z-\mu)^4+c_2r^2(z-\mu)^2
      +c_3r^3(z-\mu)+c_4r^4.$$

Since $\lambda_j=\mu+rq_j$, $$\prod_j(z-\lambda_j)
 =\prod_j\bigl(r((z-\mu)/r-q_j)\bigr)
 =r^4Q_{u,\eta}((z-\mu)/r).$$ Substituting [\[eq:qpoly\]](#eq:qpoly){reference-type="eqref" reference="eq:qpoly"} gives [\[eq:centeredexpansion\]](#eq:centeredexpansion){reference-type="eqref" reference="eq:centeredexpansion"}.

Expanding in powers of $z$ gives the explicit raw coefficient dictionary: $$\label{eq:rawcoeffs}
\begin{aligned}
 D(z)=\;&z^4-4\mu z^3+(6\mu^2+c_2r^2)z^2\\
 &+(-4\mu^3-2\mu c_2r^2+c_3r^3)z\\
 &+(\mu^4+\mu^2c_2r^2-\mu c_3r^3+c_4r^4).
\end{aligned}$$

[\[cor:complete\]]{#cor:complete label="cor:complete"} Away from the branch-label boundary fibers classified in RH-213, the four real parameters $(\mu,r,u,\eta)$ determine and are determined by a branch-labeled conjugate quartet.

The forward direction is Theorem [\[thm:reconstruct\]](#thm:reconstruct){reference-type="ref" reference="thm:reconstruct"}. Conversely the roots give $\mu$ and $r$ by [\[eq:gauge\]](#eq:gauge){reference-type="eqref" reference="eq:gauge"}; normalized branch geometry gives $u$ and $\eta$.

The parameter count matches the four real coefficients of a generic monic real quartic.

# Shape alone is non-injective

[\[prop:noninjective\]]{#prop:noninjective label="prop:noninjective"} Fix an interior shape $(u,\eta)$. The family $$\Lambda_{\mu,r}=\{\mu+rq_j(u,\eta):1\le j\le4\},
 \qquad \mu\in\mathbb R,\quad r>0,$$ has the same centered shape for every $(\mu,r)$ but consists of distinct raw divisors unless the gauge pairs coincide.

Centering and RMS normalization remove $\mu$ and $r$, so the shape is fixed. If $\mu$ changes, the cubic coefficient $-4\mu$ changes. With $\mu$ fixed, a change in $r$ changes root distances from the center and hence the divisor.

Therefore a normalized shape limit cannot be silently identified with a raw determinant limit. A growing construction must retain a gauge ledger.

# Exact transition decomposition

Let $$\theta_0=(\mu_0,r_0,u_0,\eta_0),\qquad
 \theta_1=(\mu_1,r_1,u_1,\eta_1).$$ Insert the mixed state $\theta_\times=(\mu_1,r_1,u_0,\eta_0)$. Then $$\label{eq:decomp}
 C(\theta_1)-C(\theta_0)
 =\underbrace{C(\theta_\times)-C(\theta_0)}_{\text{gauge leg}}
 +\underbrace{C(\theta_1)-C(\theta_\times)}_{\text{shape leg}},$$ where $C$ is the raw coefficient vector from [\[eq:rawcoeffs\]](#eq:rawcoeffs){reference-type="eqref" reference="eq:rawcoeffs"}.

This path is ordered---gauge first, shape second---so its two norms are not an orthogonal variance decomposition. It is nevertheless exact and answers a useful diagnostic question: can raw motion be explained by gauge alone or shape alone on each transition?

# Physical reconstruction audit

The sixteen-level, two-channel atlas supplies 32 quartets and 30 adjacent channel transitions. Direct root expansion is compared with Theorem [\[thm:reconstruct\]](#thm:reconstruct){reference-type="ref" reference="thm:reconstruct"}.

  diagnostic                                            maximum
  -------------------------------------- ----------------------
  root multiset reconstruction error       $3.15\times10^{-16}$
  raw coefficient reconstruction error     $7.78\times10^{-16}$
  parameter recovery error                        floating zero
  path telescoping residual                $1.39\times10^{-17}$

Of the 30 ordered transition decompositions, eight have a larger gauge leg and 22 have a larger shape leg. Thus the failure of centered normalization to contract in RH-212 is not surprising: on most transitions genuine shape motion is at least as large as the discarded gauge motion. The eight gauge-dominant cases also show why raw coefficients cannot be replaced by shape coordinates alone.

# Dual-channel gauge coherence

At the coarsest level the channel center discrepancy is about $0.00204$ and the RMS-radius discrepancy $0.00077$. At the finest level they fall to approximately $1.06\times10^{-5}$ and $3.60\times10^{-4}$. Shape discrepancies remain comparably small. These finite observations support a shared gauge-complete cloud experiment, but do not prove uniform channel convergence.

# Route decision after the fixed-factor obstruction

The combined state of Gate A is now:

1.  the local quartet has canonical branch labels and dual-channel coherence;

2.  its affine quotient and boundary geometry are exact;

3.  no predictive fixed-shape semigroup has been identified;

4.  a fixed or repeated quartic cannot provide a locally finite growing spectrum;

5.  the raw factor is exactly recoverable when gauge data are retained.

The next object should therefore be a rank-growing cloud $$\Lambda_{\sigma,k}=\{\lambda_{\sigma,1},\ldots,\lambda_{\sigma,k}\},
 \qquad k\to\infty,$$ with one global center $\mu_{\sigma,k}$ and one global RMS radius $r_{\sigma,k}$ for the entire cloud. Independently normalizing every quartet would destroy relative location between factors and cannot define one canonical product.

The route coordinate is $$\boxed{\texttt{finite\_gauge\_complete\_shape\_flow\_open\_rank\_growing\_divisor}}.$$

# Claim boundary

This paper closes finite algebraic reconstruction. It does not prove that the gauge parameters converge, construct the rank-growing physical cloud, control a canonical product, or realize a Fredholm determinant. Gate A is open. Gates B--E, Hilbert--Pólya, zeta-zero identification, and RH remain untouched.
