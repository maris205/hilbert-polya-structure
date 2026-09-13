---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-83-optimal-endpoint-singular-factorization"
canonical_tex: "zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/main.pdf"
source_sha256: "82a04dbc15cbb9a49d1f369c52b58b4ba33e3432eef377b7b8ec70f244877c01"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Optimal Endpoint Singular Factorization and the Coordinate-Matching Barrier Majorization, Dynamical Outer Maps, and the Next All-Level Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-82 reduced the preferred Stage-A route to a factorization of the physical postblock state through the endpoint Gaussian resolution operator. This paper determines exactly what such a factorization requires and rules out an overly literal coordinate realization.

  Let $\mathcal R$ have singular values $\rho_1\ge\rho_2\ge\cdots>0$, and let a rank-$r$ target $B_r$ have singular values $b_1\ge\cdots\ge b_r>0$. We prove the optimal two-sided factorization formula $$\inf_{B_r=U\mathcal RV}\left\lVert U\right\rVert\left\lVert V\right\rVert
   =\max_{1\le j\le r}\frac{b_j}{\rho_j}.$$ The lower bound is the ideal property of approximation numbers; equality is attained by aligning the two singular systems. For an arbitrary compact $B$, its truncated SVD therefore gives $$B=U\mathcal RV+E_r,
   \qquad \left\lVert E_r\right\rVert_2=\tau_r(B).$$ Consequently, singular-value majorization is sufficient for the RH-82 endpoint-to-postblock criterion. No coordinate alignment of singular vectors is needed.

  A 192-bit audit compares the RH-16 linear endpoint Gram operator with all ten RH-77 frozen postblock states. At ranks within one of $\lceil H_\sigma\rceil+2$, the optimal factor constant is at most $0.161572$ and the largest Hilbert--Schmidt remainder is $1.232\times10^{-9}$. The largest relative remainder is $2.340\times10^{-7}$.

  By contrast, direct coordinate projection onto sampled endpoint-row vectors leaves between $46.86\%$ and $97.90\%$ relative residual. Thus the identity outer map is decisively unsupported. The endpoint mechanism can survive only through a nontrivial dynamical rotation or, equivalently, an all-level singular-value majorization theorem.

  The latter theorem remains open, so uniform Stage A1 and unconditional Stage A4 are not claimed. No Hilbert--Polya or Riemann-hypothesis conclusion is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Optimal Endpoint Singular Factorization and the Coordinate-Matching Barrier\
  Majorization, Dynamical Outer Maps, and the Next All-Level Gate
```

## Markdown 正文

**Keywords:** singular-value majorization; operator factorization; endpoint resolution; approximation numbers; effective rank.

**MSC 2020:** 47A68; 47B06; 47B10; 65G20.

# Why the outer maps matter

RH-82 proved exponential Hilbert--Schmidt tails beyond the half-logarithmic endpoint rank clock and showed that a bounded factorization $$B_\sigma=U_\sigma\mathcal R_\sigma V_\sigma+E_\sigma
 \label{eq:desired}$$ would supply the RH-77 effective-rank premise [@WangHalfLog2026]. The most literal attempt is to identify sampled endpoint rows directly with the physical state coordinates. That would set one outer map approximately equal to the identity.

There is no mathematical reason for this. The endpoint operator describes which singular scales survive Gaussian resolution, while the intervening nonnormal dynamics may rotate their singular vectors almost arbitrarily. The correct invariant question is therefore spectral: do the physical singular values fit underneath the endpoint singular staircase?

# The optimal factorization constant

Let $\mathcal R:\mathcal H_1\to\mathcal H_2$ and $B:\mathcal K_1\to\mathcal K_2$ be compact operators. Write their singular values in decreasing order as $\rho_j=s_j(\mathcal R)$ and $b_j=s_j(B)$.

[\[thm:optimal\]]{#thm:optimal label="thm:optimal"} Suppose $B_r$ has rank $r$ and $\rho_r>0$. Then $$\boxed{
 \inf\left\{\left\lVert U\right\rVert\left\lVert V\right\rVert:B_r=U\mathcal RV\right\}
 =\max_{1\le j\le r}\frac{b_j}{\rho_j}.}
 \label{eq:optimal-constant}$$ The infimum is attained by bounded operators $U$ and $V$ supported on the first $r$ singular directions.

For every factorization $B_r=U\mathcal RV$, the ideal property of approximation numbers gives $$b_j=s_j(B_r)\le\left\lVert U\right\rVert\left\lVert V\right\rVert\,\rho_j,
 \qquad1\le j\le r.$$ This proves the lower bound in [\[eq:optimal-constant\]](#eq:optimal-constant){reference-type="eqref" reference="eq:optimal-constant"} [@Simon2005].

Choose singular systems $$\mathcal Rv_j=\rho_j u_j,
 \qquad B_r y_j=b_jx_j.$$ Let $V$ map $y_j$ isometrically to $v_j$ and vanish on the orthogonal complement. Let $Uu_j=(b_j/\rho_j)x_j$ for $j\le r$ and let $U$ vanish on the remaining singular directions. Then $B_r=U\mathcal RV$, $\left\lVert V\right\rVert=1$, and $\left\lVert U\right\rVert=\max_{j\le r}b_j/\rho_j$, proving equality.

[\[cor:approximate\]]{#cor:approximate label="cor:approximate"} For arbitrary compact $B$, let $B_r$ be its truncated rank-$r$ SVD. If $\rho_r>0$, then $$B=U\mathcal RV+E_r,
 \qquad
 \left\lVert E_r\right\rVert_2=\tau_r(B)
 =\left(\sum_{j>r}b_j^2\right)^{1/2},
 \label{eq:approximate}$$ and the factor constant for $B_r$ is exactly $\max_{j\le r}b_j/\rho_j$.

Thus the endpoint-to-postblock gate separates into two scalar assertions: $$\begin{aligned}
 \max_{j\le r_\sigma}\frac{s_j(B_\sigma)}
 {s_j(\mathcal R_\sigma)}&\le\operatorname{polylog}(1/\sigma),
 \label{eq:majorization}\\
 \tau_{r_\sigma}(B_\sigma)&\le\operatorname{polylog}(1/\sigma),
 \qquad r_\sigma=O(\log(1/\sigma)).
 \label{eq:remainder}\end{aligned}$$ Together with the observability condition in RH-82, these bounds close the effective-rank corridor. They do not require a common coordinate basis.

# Validated singular-majorization audit

For each archived noise scale, the audit constructs the linear endpoint Gram matrix from the exact powered-row affinity of RH-16 [@WangEndpointRank2026]. Its entries are propagated in 192-bit Arb arithmetic after exact lifting of the archived boundary clearances. If $G_f$ is the binary64 Gram matrix and $G_I$ its Arb enclosure, then $$\|G_I-G_f\|_2\le\|G_I-G_f\|_F.$$ Weyl's inequality therefore gives lower bounds for every endpoint singular value whose squared value exceeds the Gram defect.

The physical postblock state is recomputed in Arb from the exact frozen binary64 operator and source entries. Its binary64 SVD supplies candidate singular systems; the float-to-Arb state defect gives upper bounds for the physical singular values. Combining both sides certifies [\[eq:optimal-constant\]](#eq:optimal-constant){reference-type="eqref" reference="eq:optimal-constant"} at the resolved ranks.

::: {#tab:factor}
    $\sigma$   clock rank   factor rank   max factor           max remainder   min coord. residual
  ---------- ------------ ------------- ------------ ----------------------- ---------------------
        0.16            4             4     0.161572    $1.232\times10^{-9}$                0.4686
        0.08            5             5     0.021406   $3.473\times10^{-13}$                0.6407
        0.04            6             5     0.004181   $3.564\times10^{-10}$                0.8657
        0.02            6             6     0.006749   $4.471\times10^{-13}$                0.9294
        0.01            7             7     0.001145   $8.276\times10^{-14}$                0.9372

  : Outward-certified maxima over both channels, except the final column, which is the smaller coordinate residual lower bound. At $\sigma=0.04$, the sixth endpoint Gram eigenvalue lies below the finite arithmetic resolution, so the certified factor rank is five.
:::

The maximum factor constant occurs at the coarsest scale and is already well below one. The sole one-rank certification loss at $\sigma=0.04$ increases the physical remainder only to $3.564\times10^{-10}$. No forbidden power of $\sigma$ is visible at the anchors.

# The coordinate-matching barrier

To test the identity outer-map shortcut, the audit samples the folded linear endpoint rows on the physical state grid, removes the limiting endpoint row, and projects $B_\sigma$ onto the first $\lceil H_\sigma\rceil+2$ left singular vectors of this coordinate dictionary. The state perturbation from binary64 to Arb is subtracted before forming the residual lower bound.

Every channel fails even a permissive $25\%$ residual gate. The certified relative residuals range from $0.4687$ to $0.9790$. The mismatch grows toward small noise in the left channel.

[\[prop:coordinate\]]{#prop:coordinate label="prop:coordinate"} The archived clock-rank postblock states do not lie near the direct sampled endpoint-row coordinate subspaces. In particular, the numerical evidence does not support [\[eq:desired\]](#eq:desired){reference-type="eqref" reference="eq:desired"} with an identity left outer map and small remainder.

This is intentionally a finite-scale branch verdict, not an impossibility theorem for all bounded outer maps. The optimal factorization theorem shows why: singular values match even when singular vectors are strongly rotated.

![Optimal factor constants, SVD remainders, failure of direct coordinate matching, and interval-resolved endpoint ranks.](<../../../../../zeta_mvp0/papers/RH-83-optimal-endpoint-singular-factorization/figures/optimal_endpoint_singular_factorization.pdf>){#fig:factor width="\\textwidth"}

# Next gate and claim boundary

RH-83 removes a potentially expensive and false obligation. One need not identify physical postblock singular vectors with endpoint row vectors. Instead, the next theorem should prove the scalar majorization [\[eq:majorization\]](#eq:majorization){reference-type="eqref" reference="eq:majorization"} and tail bound [\[eq:remainder\]](#eq:remainder){reference-type="eqref" reference="eq:remainder"} uniformly over the dyadic family. A natural route is to compare physical Gram eigenvalues with the exact endpoint Gram kernel through min--max or Schur-complement bounds, allowing nontrivial dynamical outer maps.

This paper proves the optimal factorization theorem and validates finite singular majorization at five scales. It does not prove all-level majorization, uniform Stage A1, unconditional Stage A4, a relative A5 determinant, a self-adjoint Hilbert--Polya operator, a $T\log T$ law, a prime-power trace formula, a zeta-zero identification, or the Riemann Hypothesis.
