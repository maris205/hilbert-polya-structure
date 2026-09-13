---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-pgl2-projective-mobius-cycle-atlas-route-a"
canonical_tex: "henon_dynamics/henon_pgl2_projective_mobius_cycle_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_pgl2_projective_mobius_cycle_atlas_route_a/paper/main.pdf"
source_sha256: "abfcbee87fa15912ae103765b4d71fd024cca2d936d492992842db2fb65cb88b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Cycle Atlas for Projective Möbius Dynamics over Finite Fields

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_pgl2_projective_mobius_cycle_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_pgl2_projective_mobius_cycle_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_pgl2_projective_mobius_cycle_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_pgl2_projective_mobius_cycle_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every prime power $q=p^r$, we classify the permutation induced by each $g\in\mathrm{PGL}_2(\mathbb F_q)$ on $\mathbb P^1(\mathbb F_q)$. Four cases give the complete cycle multiset, all iterated fixed counts, primitive cycles, the finite Artin--Mazur zeta, and the finite Koopman spectrum. Exhaustive direct permutation checks cover 18 prime and extension fields. We also close the characteristic-two classifier, the exact per-order type census, and explicit projective reversors in every characteristic. All statements are source-local and use no target spectral data.
author:
- 'Route-A source-local certificate HCS-C260'
date: 31 August 2026
title: A Complete Cycle Atlas for Projective Möbius Dynamics over Finite Fields
```

## Markdown 正文

trailerid \[\<C2602026083100000000000000000000\>\<C2602026083100000000000000000000\>\] suppressoptionalinfo 767

# The four cycle types

Represent $g$ by $A\in\mathrm{GL}_2(\mathbb F_q)$, modulo nonzero scalar. In the semisimple cases let $d$ be the order of the eigenvalue ratio.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} Exactly one of the following rows applies.

  type        condition               cycles on $\mathbb P^1(\mathbb F_q)$   $F_n=\#\operatorname{Fix}(g^n)$
  ----------- ----------------------- -------------------------------------- ---------------------------------
  identity    $g=1$                   $1^{q+1}$                              $q+1$
  unipotent   nontrivial, order $p$   $1^1p^{q/p}$                           $1+q\mathbf1_{p\mid n}$
  split       $d>1$, $d\mid q-1$      $1^2d^{(q-1)/d}$                       $2+(q-1)\mathbf1_{d\mid n}$
  nonsplit    $d>1$, $d\mid q+1$      $d^{(q+1)/d}$                          $(q+1)\mathbf1_{d\mid n}$

For every $m\ge1$, the numbers of points and cycles of least period $m$ are $$P_m=\sum_{e\mid m}\mu(m/e)F_e,\qquad C_m=P_m/m.       \tag{1}$$

The scalar case is immediate. A nonscalar repeated-root matrix has one rational eigenline and is projectively conjugate to $x\mapsto x+1$. It fixes infinity and partitions the affine line into $q/p$ cycles of length $p$. If the characteristic polynomial splits with distinct roots, conjugate the two rational eigenlines to $0$ and infinity. The map is $x\mapsto\rho x$; $\rho$ has order $d\mid q-1$ and acts freely on $\mathbb F_q^*$.

In the irreducible case the two eigenlines lie over $\mathbb F_{q^2}$ and Frobenius interchanges them. Thus $\rho^q=\rho^{-1}$ and $d\mid q+1$. A proper nonidentity power cannot acquire a rational eigenline: it retains the same two nonrational eigenlines. Hence the cyclic action is semiregular on all $q+1$ rational projective points. The fixed formulas sum cycle lengths dividing $n$, and Möbius inversion gives (1).

# Characteristic two and the type census

When $p=2$, discriminant-square language is not a valid classifier. If $\operatorname{tr}A=0$, the characteristic polynomial has a repeated root; apart from the scalar identity this is the unipotent face. If $\operatorname{tr}A\ne0$, scale the polynomial to $$y^2+y+u,\qquad u=\frac{\det A}{(\operatorname{tr}A)^2}.                \tag{2}$$ The Artin--Schreier equation $y^2+y=u$ is soluble in $\mathbb F_q$ precisely when $\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(u)=0$. Absolute trace zero therefore means split, while absolute trace one means nonsplit.

The order-refined census is also exact. There is one identity and $q^2-1$ nonidentity unipotents. For every $d>1$, $$\begin{array}{ll}
d\mid q-1:& \#\{\hbox{split elements of order }d\}
=q(q+1)\varphi(d)/2,\\[2pt]
d\mid q+1:& \#\{\hbox{nonsplit elements of order }d\}
=q(q-1)\varphi(d)/2.                                 \tag{3}
\end{array}$$ For $d>2$, pair the $\varphi(d)$ ratios as $\{\rho,\rho^{-1}\}$ and use torus centralizers of sizes $q-1$ and $q+1$. At $d=2$ the ratio is self-inverse and its torus normalizer doubles the centralizer, producing the same formulas. This boundary is important for odd $q$: split involutions have two rational fixed points, whereas nonsplit involutions have none. In characteristic two, $q-1$ and $q+1$ are odd, so nonidentity projective involutions are unipotent. Summing the census with $\sum_{d\mid N}\varphi(d)=N$ gives $q(q^2-1)$.

# Uniform exact reversibility

Every nonscalar $2\times2$ matrix is cyclic. In a cyclic basis put $$C=\begin{pmatrix}0&-\delta\\1&\tau\end{pmatrix},\qquad
H=\begin{pmatrix}0&\delta\\1&0\end{pmatrix},
\quad \tau=\operatorname{tr}A,\quad\delta=\det A.     \tag{4}$$ Direct multiplication, with no characteristic restriction, yields $$H^2=\delta I,\qquad HCH^{-1}=\delta C^{-1}.          \tag{5}$$ Thus $[H]$ is a projective involution and $[H]g[H]^{-1}=g^{-1}$. The identity is trivially reversible. This closes the reversor problem for all four rows, including characteristic two; it does not assert that the Koopman operator itself is self-adjoint (that occurs only when the projective order is at most two).

# Zeta and finite Koopman closure

For a finite permutation with $c_L$ cycles of length $L$, $$\zeta_g(t)=\exp\!\left(\sum_{n\ge1}\frac{F_n}{n}t^n\right)
=\prod_L(1-t^L)^{-c_L}.                              \tag{6}$$ Consequently the four rows give, respectively, $$(1-t)^{-(q+1)},\quad
(1-t)^{-1}(1-t^p)^{-q/p},\quad
(1-t)^{-2}(1-t^d)^{-(q-1)/d},\quad
(1-t^d)^{-(q+1)/d}.                                  \tag{7}$$ On counting-measure $\ell^2(\mathbb P^1(\mathbb F_q))$, the Koopman operator is a permutation unitary. Every $L$-cycle contributes each $L$th root of unity once, and $$\det(I-tU_g)=\prod_L(1-t^L)^{c_L}=\zeta_g(t)^{-1}.   \tag{8}$$

# Exact regression and boundary

Two implementations cover $q=2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32$. The independent checker shares no finite-field or classifier code with the producer: it rebuilds every field and projective permutation, derives the type only from fixed-point geometry and cycle lcm, and matches a canonical per-matrix record hash. In total it checks $155{,}346$ transformations, $4{,}367{,}094$ state images, and closes $6{,}159{,}318$ assertions. The extension-field sentinels have degrees two through five and exercise the absolute-trace rule. Symbolic algebra closes 193 identities; byte replay is exact; semantic mutation rejects $40/40$ repaired-hash changes, including swapped $q-1/q+1$ channels and corrupted involution faces. Finite enumeration is a regression oracle, not the proof for arbitrary $q$.

Finite-field arithmetic provides only `A0_WEAK_ARITHMETIC_RELATION`; Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"} earns `A1_PASS_ANALYTIC`, while (8) gives `A4_NATURAL_QUANTIZATION`. There is no rational-prime orbit dictionary, target divisor, or target global analytic structure. The strict tuple is $$\texttt{(A0\_WEAK\_ARITHMETIC\_RELATION,A1\_PASS\_ANALYTIC,
A2\_FAIL,A3\_FAIL,A4\_NATURAL\_QUANTIZATION)}.$$ The verdict is `ROUTE_A_EXPLORATORY`; Route B is disabled. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, (6) is only a finite source zeta, and (8) is not a Hilbert--Polya identification. We claim neither literature priority for the classical context in Refs. \[1--3\] nor that finite tests prove the arbitrary-prime-power theorem.

# References {#references .unnumbered}

\[1\] E. Sakzad, M.-R. Sadeghi, and D. Panario, *Adv. Math. Commun.* **6** (2012), 347--361, [doi:10.3934/amc.2012.6.347](https://doi.org/10.3934/amc.2012.6.347).

C. Forsyth, J. Gurev, and S. Shrima, *Proc. Amer. Math. Soc.* **144** (2016), 4583--4590, [doi:10.1090/proc/13126](https://doi.org/10.1090/proc/13126).

G. E. Wall, *Bull. Aust. Math. Soc.* **22** (1980), 339--364, [doi:10.1017/S0004972700006675](https://doi.org/10.1017/S0004972700006675).
