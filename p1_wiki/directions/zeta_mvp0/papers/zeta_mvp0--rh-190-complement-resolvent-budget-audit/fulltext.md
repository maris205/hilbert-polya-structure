---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-190-complement-resolvent-budget-audit"
canonical_tex: "zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit/main.pdf"
source_sha256: "6c71683e136ab3ff826ab26d55e5f6fbd90060b909be7e54ef16924ee757bbdd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complement-Resolvent Budget Audit The Norm-Only Oblique Route Fails, Leaving Validated Contour Inverses as the Next Wall

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-190-complement-resolvent-budget-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-189 gives an exact oblique Feshbach determinant factorization, but the physical complement resolvent remains unknown. This paper tests the strongest elementary norm-only substitute.

  For a biorthogonal packet with oblique projector $P=VW^*$ and condition $\chi=\left\lVert P\right\rVert$, let $Q=I-P$. In orthonormal complement coordinates, the Feshbach block obeys the sharp elementary bound $$\left\lVert D\right\rVert\le\left\lVert Q\right\rVert\left\lVert A\right\rVert=\chi\left\lVert A\right\rVert.$$ If a cycle root has radius $\rho$ and a contour has radius $\delta$, a Neumann resolvent estimate would require $$\rho-\delta>\chi\left\lVert A\right\rVert.$$ This criterion is intentionally optimistic: it ignores all nonnormal cancellation and uses the best ideal packet contour factor.

  Applied to all 126 RH-185 windows with contour radius $0.4$ times the root half-spacing, the norm-only clearance is negative everywhere. The complement operator bound ranges from $71.46$ to $6.40\times10^5$ while the minimum contour modulus is at most $0.719$. No norm-only complement resolvent exists, no full norm-only certificate passes, and even an unrealistically unit complement-resolvent Schur test has zero successes.

  This is a useful negative result: it rules out a cheap norm closure, not the physical Feshbach route. The next required object is a validated contour inverse exploiting the actual complement spectrum, as in the finite-mesh and operator-ball machinery of RH-167--168. No physical Riesz shell, Gate A, Hilbert--Polya, or RH result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Complement-Resolvent Budget Audit\
  The Norm-Only Oblique Route Fails, Leaving Validated Contour Inverses as the Next Wall
```

## Markdown 正文

# The complement problem after Feshbach factorization

RH-189 writes the physical operator in oblique packet/complement coordinates as $$\label{eq:block}
 S^{-1}AS=\begin{pmatrix}K&B\\C&D\end{pmatrix}$$ and gives $$\label{eq:feshbach}
 \det(zI-A)=\det(zI-D)
 \det\left(zI-K-B(zI-D)^{-1}C\right).$$ The coupling product from RH-188 controls $B(zI-D)^{-1}C$ only after a bound on $(zI-D)^{-1}$ is available [@WangRH188; @WangRH189].

One might first try the universal estimate $$\label{eq:universal}
 \left\lVert(zI-D)^{-1}\right\rVert
 \le\frac1{|z|-\left\lVert D\right\rVert}.$$ This paper shows exactly how far that shortcut is from the physical data.

# Oblique complement norm bound

Let $P=VW^*$ with $W^*V=I$ and $Q=I-P$. By RH-186, $\left\lVert Q\right\rVert=\left\lVert P\right\rVert=\chi$ for a nontrivial oblique decomposition. The orthonormal complement construction of RH-189 chooses an isometry $Z$ onto $\operatorname{Ran}Q=\ker W^*$ and gives $D=Z^*QAZ$ [@WangRH189].

[\[thm:complement\]]{#thm:complement label="thm:complement"} For every bounded $A$, $$\label{eq:D-bound}
 \left\lVert D\right\rVert\le\left\lVert Q\right\rVert\left\lVert A\right\rVert\le\chi\left\lVert A\right\rVert.$$ If $\rho>\delta>0$ and $$\label{eq:clearance}
 \rho-\delta>\chi\left\lVert A\right\rVert,$$ then every $z$ with $|z-\zeta|=\delta$ and $|\zeta|=\rho$ satisfies $$\label{eq:resolvent}
 \left\lVert(zI-D)^{-1}\right\rVert
 \le\frac1{\rho-\delta-\chi\left\lVert A\right\rVert}.$$

The representation $D=Z^*QAZ$ and the isometry of $Z$ give $\left\lVert D\right\rVert\le\left\lVert Q\right\rVert\left\lVert A\right\rVert$. On the contour, $|z|\ge|\zeta|-|z-\zeta|=\rho-\delta$. If [\[eq:clearance\]](#eq:clearance){reference-type="eqref" reference="eq:clearance"} holds, $$zI-D=z\left[I-z^{-1}D\right]$$ has a convergent Neumann inverse, and summing its geometric series gives [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"}.

The theorem is a sufficient condition only. It does not claim that the complement has spectrum reaching $\left\lVert D\right\rVert$; it records what a norm-only proof would need to establish.

# Contour choice

For a length-$L$ cycle of radius $\rho$, the root half-spacing is $$\label{eq:spacing}
 s_L=\rho\sin(\pi/L).$$ We choose the deliberately conservative contour radius $$\label{eq:contour}
 \delta=0.4s_L<s_L.$$ This leaves root shells geometrically disjoint and is more generous than a small perturbative contour. The packet resolvent factor is given its best ideal estimate $a=1/\delta$ for the optimistic Schur comparison.

For each RH-185 window, the stored source-cycle radius supplies $\rho$, the stored length supplies $L$, and the stored operator norm and oblique condition supply $\left\lVert A\right\rVert$ and $\chi$.

# Audit results

There are 126 windows. The norm-only complement data are:

  quantity                                        minimum                median              maximum
  --------------------------------- --------------------- --------------------- --------------------
  $\chi\left\lVert A\right\rVert$                 $71.46$    $1.5547\times10^3$   $6.3996\times10^5$
  $\rho-\delta$                                  $0.3913$              $0.5260$             $0.7188$
  clearance                           $-6.3996\times10^5$   $-1.5542\times10^3$            $-70.979$

Thus $$\label{eq:no-clearance}
 \#\{\text{norm-only complement resolvent successes}\}=0.$$ The result holds in particular for all 38 local $\sigma=0.01,L=4$ windows.

The optimistic comparison sets the complement resolvent factor to one, which is strictly better than the unavailable norm-only bound. Even then, the product $$\label{eq:optimistic}
 a\,b\,c$$ has minimum $1.1116$ and zero successes. Inserting the actual norm-only resolvent would only worsen it.

# Interpretation

The negative result has three layers:

1.  the orthonormal-coordinate complement bound still carries one full oblique factor $\chi$;

2.  the physical $\chi$ values are too large for radial norm separation;

3.  even an artificially favorable complement factor does not close the smallest observed coupling product on the chosen contour.

None of these layers proves that the actual complement spectrum is large. Nonnormal matrices can have resolvents much smaller than a norm-only Neumann bound at selected points, or much larger near pseudospectral regions. The correct next calculation must use actual sample inverses and outward operator balls.

# Validated contour route

The RH-167--168 architecture provides the appropriate replacement:

1.  choose a finite contour mesh around each candidate root;

2.  compute a nominal inverse at each mesh point;

3.  bound inverse defects and operator displacement;

4.  use the Banach denominator to cover the continuous contour;

5.  feed the resulting $d(z)$ into the directed product $a(z)d(z)bc$.

This route may exploit structure invisible to $\chi\left\lVert A\right\rVert$. It is more expensive and is now the precise physical $D$ leaf rather than a vague "resolvent estimate" request.

The finite validation step can be stated as a direct Banach-lemma theorem.

[\[prop:validated-inverse\]]{#prop:validated-inverse label="prop:validated-inverse"} Let $D_0$ be a nominal complement block, let $\left\lVert D-D_0\right\rVert\le\varepsilon$, and choose a mesh point $z_0$ with a computed matrix $M_0$. Suppose $$\label{eq:inverse-defect}
 \left\lVert I-M_0(z_0I-D_0)\right\rVert\le\eta.$$ For every $z$ with $|z-z_0|\le h$, define $$\label{eq:q-bound}
 q=\eta+\left\lVert M_0\right\rVert(h+\varepsilon).$$ If $q<1$, then $zI-D$ is invertible and $$\label{eq:validated-resolvent}
 \left\lVert(zI-D)^{-1}\right\rVert\le\frac{\left\lVert M_0\right\rVert}{1-q}.$$

Expanding around the nominal mesh equation gives $$I-M_0(zI-D)
 =I-M_0(z_0I-D_0)-M_0\bigl((z-z_0)I-(D-D_0)\bigr).$$ Its norm is at most $q$. If $q<1$, the Banach lemma makes $M_0(zI-D)$ invertible and bounds its inverse by $(1-q)^{-1}$. Multiplying by $M_0$ yields [\[eq:validated-resolvent\]](#eq:validated-resolvent){reference-type="eqref" reference="eq:validated-resolvent"}.

This proposition specifies the data missing from the present archive: nominal complement matrices, outward operator radii, contour mesh radii, inverse residuals, and inverse norms. It also explains why the failure of a radial norm disk is not decisive. A good local inverse $M_0$ may exist far inside the disk $|z|\le\left\lVert D\right\rVert$.

# Quantitative distance to the norm-only route

The best elementary clearance is still about $-70.98$, whereas the relevant contour moduli are below one. Thus replacing the ambient $\chi^2$ estimate by the sharp orthonormal-coordinate factor $\chi$ improves the bound by orders of magnitude but leaves a large finite gap. This corrected audit is important: the negative conclusion is not an artifact of paying an unnecessary second oblique factor.

The optimistic unit-complement comparison is logically separate. Its minimum $1.1116$ says that on the chosen contour even a complement inverse of norm one would not close the current product. A successful exact audit must therefore gain jointly from the actual packet resolvent geometry, directional coupling coordinates, and complement inverse; improving only the radial complement norm estimate is insufficient.

# Data contract for the next experiment

The next archive should store the nominal matrices $K,B,C,D$ for every surviving window, not merely their norms. It should also store contour centers, mesh points, mesh covering radii, approximate inverses, inverse defects, and outward operator radii. From these primitive quantities one can independently reconstruct [\[eq:q-bound\]](#eq:q-bound){reference-type="eqref" reference="eq:q-bound"}, the continuous complement bound, and the final Schur product.

Predeclaring this data contract prevents a posteriori contour movement. A contour that meets the complement spectrum is a finite rejection of that root shell; it should not be silently shrunk until a favorable inverse is found. Conversely, a positive margin must survive the full mesh cells and operator ball, not just the sampled contour points.

# Boundary

This paper proves the norm-only complement criterion and audits its complete failure on the current 126 finite windows. It does not establish a complement spectral obstruction, exclude validated contour inverses, prove a Schur/Riesz certificate, or close any all-level interface. The local biorthogonal candidate remains an exploratory seed only.
