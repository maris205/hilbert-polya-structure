---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-padic-symplectic-analytic-interpolation-route-a"
canonical_tex: "henon_dynamics/henon_padic_symplectic_analytic_interpolation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_padic_symplectic_analytic_interpolation_route_a/paper/main.pdf"
source_sha256: "3a79c33fd7c913b22b004f5b94b556fa04419913b933f1004fa846ad90daf05b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Analytic Orbits of a Nonlinear $p$-Adic Double Shear: \ifcase\CRevisionRound Joint Interpolation on the Original Clock \or Minimal Components and Every Residue Period \else From Symplectic Interpolation to Complete Return-Time Laws\fi

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_padic_symplectic_analytic_interpolation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_padic_symplectic_analytic_interpolation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_padic_symplectic_analytic_interpolation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_padic_symplectic_analytic_interpolation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A nonlinear symplectic double shear on the $p$-adic unit polydisc admits an analytic extension of its original integer iteration clock. We give the joint Tate-algebra construction at every nonzero parameter with valuation at least one for odd primes and at least two at the prime two. The origin is its only genuine periodic point. \>0 A strict first-term estimate gives the exact two-time displacement scale $p^{-c-2r}$ on the radius-$p^{-r}$ shell. Every nonzero orbit closure is therefore an isometric copy of the $p$-adic adding-one system. The same identity determines all least periods, shell multiplicities and fixed counts at every prime-power residue level. \>1 Algebraic orbit intersections occur at finitely many nonnegative integer times or at every such time. The natural Haar Koopman map is unitary but noncompact, and each nonzero minimal component has zero ambient Haar measure. Independent exact computations audit the formulas without replacing their proofs. The interpolation and analytic-zero methods have classical owners; no new certificate algorithm or target prime-period identity is claimed.
author:
- 'HCS-C394 theorem and reproducibility package'
date: 5 September 2026
title: |
  Exact Analytic Orbits of a Nonlinear $p$-Adic Double Shear:\
  Joint Interpolation on the Original Clock Minimal Components and Every Residue Period From Symplectic Interpolation to Complete Return-Time Laws
```

## Markdown 正文

**Keywords:** p-adic dynamics; symplectic shear; analytic interpolation; minimal component; residue period; algebraic return.

chinese-simplified

中文摘要

本文研究单位多圆盘上的非线性辛双剪切映射，将原始整数迭代时间联合解析地延拓到素进整数。 奇素数下参数估值至少为一，二进情形至少为二，参数零单独排除。 原点是完整素进空间内唯一真正的周期点。 \>0 首项严格支配给出精确的双时间位移尺度，从而识别每个非零最小轨道闭包， 并统一确定所有素数幂剩余层的最小周期、循环重数与固定点数。 \>1 任意代数子簇的整数命中时刻集合不是有限集，就是全部非负整数。 原生测度与反转结构保持不变，但自然酉算子并不紧，不能据此得到目标行列式。 精确有限计算只检验公式的实现。经典插值理论明确归属，不将原生算术结构写成目标零点对应。

关键词：素进动力学；辛剪切；解析插值；最小分量；剩余周期；代数返回。

# One nonlinear source and its arithmetic boundary

Let $p$ be any rational prime and normalize $v_p(p)=1$. Fix a nonzero $a\in\mathbb Z_p$ with $c=v_p(a)\ge1$ when $p$ is odd and $c\ge2$ when $p=2$. On $X=\mathbb Z_p^2$ use the maximum norm and freeze $$\label{map}
 F_a(x,y)=\bigl(x+ay^2,\ y+a(x+ay^2)^2\bigr).$$ The coefficientwise proximity to the identity permits analytic time interpolation, but proximity alone does not describe all orbits. For this map, the additional homogeneous shear structure determines the exact radius-dependent clock. Finite residue permutations and periodic points in $X$ must remain separate throughout.

Poonen's joint interpolation theorem and its dyadic boundary [@poonen] supply the classical method reconstructed below. The analytic zero-set approach to dynamical Mordell--Lang belongs to Bell--Ghioca--Tucker [@bgt]. Recent finite-precision and refined-tail certificate methods belong to Mukhamedov [@mukhamedov]; we claim no new effective certification algorithm. Our question is the full orbit structure of the particular nonlinear source, not a new general interpolation theorem.

The nearest project mechanisms are C166's finite affine dyadic Pascal tower, C174's expanding parity renewal, C258's mixed congruential map, and C283's conductor-shell heat operator. None supplies the nonlinear joint analytic action and valuation-scale decomposition of [\[map\]](#map){reference-type="eqref" reference="map"}. The symbolic branch's P23 imports classical linear-recurrence zero-set rigidity, not this nonlinear analytic-arc proof. These comparisons define the repository increment; they are not a global novelty certification.

# Symplecticity, reversal, and joint analytic time

Write $F_a=S_yS_x$ for the two shears $S_x(x,y)=(x+ay^2,y)$ and $S_y(x,y)=(x,y+ax^2)$. Both preserve $dx\wedge dy$, and $$\label{inv}
 F_a^{-1}(x,y)=\bigl(x-a(y-ax^2)^2,\ y-ax^2\bigr).$$ The involution $R_0(x,y)=(-y,-x)$ satisfies $R_0S_xR_0=S_y^{-1}$ and $R_0S_yR_0=S_x^{-1}$, hence $R_0F_aR_0=F_a^{-1}$ on the same clock. Integral coefficients in [\[map\]](#map){reference-type="eqref" reference="map"}--[\[inv\]](#inv){reference-type="eqref" reference="inv"} make both maps 1-Lipschitz; each is therefore an isometry and induces a permutation modulo every $p^N$.

[\[interpolation\]]{#interpolation label="interpolation"} There is $G_a\in\mathbb Z_p\langle x,y,t\rangle^2$ such that $G_a(u,n)=F_a^n(u)$ for every integer $n\ge0$ and $$G_a(G_a(u,s),t)=G_a(u,s+t)\qquad(s,t\in\mathbb Z_p).$$ Thus negative time is the inverse of positive time, without a new roof.

On $A=\mathbb Z_p\langle x,y\rangle$, set $\Delta h=h\circ F_a-h$. Factoring differences of monomials and taking Gauss-norm limits gives $\left\|\Delta h\right\|_p\le p^{-c}\left\|h\right\|_p$. In particular $\Delta^mu\in p^{cm}A^2$. The joint series $$\label{mahler}
 G_a(u,t)=\sum_{m\ge0}\binom tm\Delta^mu$$ converges in the Tate algebra because its $m$th term has coefficient norm at most $p^{-cm+v_p(m!)}$ and $v_p(m!)\le m/(p-1)$. If $\delta=c-1/(p-1)>0$, its tail after $M$ has norm at most $p^{-(M+1)\delta}$. At integer $n\ge0$ the series truncates to $(I+\Delta)^nu=F_a^n(u)$. The action law holds first at nonnegative integer pairs. Such pairs are dense in $\mathbb Z_p^2$ and all compositions are continuous and integral-valued, so the law holds at every pair. The time-zero map is the identity.

The sufficient threshold cannot be replaced by a general dyadic coefficient congruence modulo two: $f(x)=-x$ has a nonzero two-cycle. An analytic interpolant of the orbit of one would equal one on all even times and therefore identically, contradicting its odd-time value. This general control does not assert failure of every double shear outside the stated threshold. Pointwise residue identity also does not suffice: $x^p=x$ on $\mathbb F_p$, but $x^p-x$ has unit coefficients.

# Genuine periods and the first revision boundary

The action has no nontrivial finite-time stabilizer at a nonfixed point. Indeed, if $F_a^n(u)=u$ for some $n\ge1$, then every coordinate of $G_a(u,t)-u$ vanishes at the infinite set $t=kn$. A nonzero restricted one-variable analytic function has finitely many zeros on $\mathbb Z_p$ by Strassmann's theorem. Hence the coordinates vanish identically and $F_a(u)=u$. Solving [\[map\]](#map){reference-type="eqref" reference="map"} gives $ay^2=0$ and $a(x+ay^2)^2=0$, whence $u=0$. At this point $DF_a(0)=I$, so it is parabolic rather than expanding. The genuine point-counting zeta is $(1-z)^{-1}$.

Round zero establishes the source and joint clock, but does not yet determine nonperiodic orbit closures or all finite quotient periods. Those require the strict displacement estimate developed in the next revision. Neither a finite quotient permutation nor the preceding scalar zeta constructs a target determinant.

\>0

# The exact displacement scale and minimal decomposition

[\[strict\]]{#strict label="strict"} If $u\ne0$ and $r=\min(v_p(x),v_p(y))$, then for every $s,t\in\mathbb Z_p$, $$\label{distance}
 \left\|G_a(u,t)-G_a(u,s)\right\|_p=p^{-c-2r}|t-s|_p.$$

First take a unit-radius vector $v$ and parameter $b$ of valuation $d$. The vector $F_b(v)-v=b(v_2^2,(v_1+bv_2^2)^2)$ has norm $p^{-d}$: either $v_2$ is a unit or $v_1+bv_2^2$ is a unit. For $m\ge2$, $$\binom tm=\frac{t}{m}\binom{t-1}{m-1},\qquad
 v_p(m)<d(m-1).$$ The binomial value on the right is integral, by continuity from integer values. The strict inequality holds for odd $p,d\ge1$; the only possible equality at $d=1$ is $p=m=2$, excluded by $d\ge2$ in the dyadic case. The $m$th higher term in [\[mahler\]](#mahler){reference-type="eqref" reference="mahler"} therefore has value norm at most $|t|_p p^{-d-1}$, whereas the first term has norm exactly $|t|_p p^{-d}$. Strict dominance gives $\left\|G_b(v,t)-v\right\|_p=p^{-d}|t|_p$. This is a value estimate, not the coefficient Gauss estimate used in Theorem [\[interpolation\]](#interpolation){reference-type="ref" reference="interpolation"}.

Now write $u=p^rv$. Substitution gives $F_a(p^rv)=p^rF_{ap^r}(v)$; interpolation and continuity give the same identity for every $t$. Since $d=c+r$, $\left\|G_a(u,t)-u\right\|_p=p^{-c-2r}|t|_p<\left\|u\right\|_p$. Thus $G_a(u,s)$ has the same radius as $u$. Apply the last formula at that basepoint with time $t-s$ and use the action law. This proves [\[distance\]](#distance){reference-type="eqref" reference="distance"}, with both sides zero when $s=t$.

[\[minimal\]]{#minimal label="minimal"} Every nonzero orbit closure is the image $G_a(u,\mathbb Z_p)$, a scaled isometric copy of $\mathbb Z_p$ on which $F_a$ is conjugate to addition by one. These closures are pairwise disjoint or equal and, with the origin, partition $X$ into minimal compact invariant sets. The origin is the only genuine periodic point and $DF_a^n(0)=I$ for every $n\ge1$.

Equation [\[distance\]](#distance){reference-type="eqref" reference="distance"} gives injectivity and an inverse continuous on the compact image. Density of nonnegative integers identifies this image with the forward orbit closure. The action law conjugates iteration to addition by one, which meets every residue class and is minimal. A common point and negative time identify any two intersecting images. No nonzero integer $n$ can make the right side of [\[distance\]](#distance){reference-type="eqref" reference="distance"} zero. The derivative at the origin follows directly from [\[map\]](#map){reference-type="eqref" reference="map"}.

# Every finite residue period and its native zeta

For $N\ge1$ and $0\le r<N$, define $$L_{N,r}=p^{\max(0,N-c-2r)},\qquad
 S_{N,r}=p^{2(N-r)}-p^{2(N-r-1)}.$$

[\[finite\]]{#finite label="finite"} A nonzero residue vector modulo $p^N$ with minimum valuation $r$ has exact period $L_{N,r}$. Shell $r$ has $S_{N,r}/L_{N,r}$ cycles. The zero residue is fixed. For every integer $n\ge1$, $$\label{fixed}
 \#\operatorname{Fix}(F_a^n\bmod p^N)=p^{2(N-R)},\qquad
 R=\max\left(0,\left\lceil\frac{N-c-v_p(n)}2\right\rceil\right).$$

The minimum valuation $r<N$ is independent of the lift. The displacement formula says that return modulo $p^N$ is equivalent to $c+2r+v_p(n)\ge N$, proving the least period. Subtract the number of vectors divisible by $p^{r+1}$ from those divisible by $p^r$ to count the shell. All its cycles have the same length, so division gives their count. The shells with $r\ge R$ and the zero class telescope to [\[fixed\]](#fixed){reference-type="eqref" reference="fixed"}. In particular, every shell with $c+2r\ge N$ is fixed, not only the zero class. The zero class and all shells together have exactly $p^{2N}$ points.

The complete finite point-counting product is $$\label{zeta}
 \zeta_N(z)=(1-z)^{-1}
 \prod_{r=0}^{N-1}(1-z^{L_{N,r}})^{-S_{N,r}/L_{N,r}}.$$ Its logarithmic derivative recovers [\[fixed\]](#fixed){reference-type="eqref" reference="fixed"}. When distinct shells share a period their cycle counts add. By contrast, the genuine zeta on $X$ is only $(1-z)^{-1}$. Finite cycles have $p$-power lengths, but their nonzero representatives never become genuine finite-period points.

\>1

# Algebraic hitting times: finite or all

[\[zeros\]]{#zeros label="zeros"} For nonzero $h(t)=\sum h_jt^j\in\mathbb Q_p\langle t\rangle$, let $J$ be the largest index attaining its coefficient norm. There are at most $J$ distinct zeros in $\mathbb Z_p$.

If $h(b)=0$, $|b|_p\le1$, set $q_j=\sum_{k\ge j+1}h_kb^{k-j-1}$. The coefficients tend to zero and $h=(t-b)q$ by coefficient comparison, including the constant term. For $J\ge1$, $q_{J-1}$ equals $h_J$ plus strictly smaller terms, and all $q_j$ with $j\ge J$ are strictly smaller than the norm of $h$. The largest norm-attaining index drops from $J$ to $J-1$. When $J=0$, the constant coefficient dominates and no zero exists. Successive division by distinct zeros preserves all remaining zeros and therefore bounds their number by $J$.

[\[hitting\]]{#hitting label="hitting"} For every $u\in X$ and every algebraic subvariety $V\subset\mathbb A^2_{\mathbb Q_p}$, the set $\{n\ge0:F_a^n(u)\in V\}$ is finite or all nonnegative integers.

Choose finite polynomial equations $H_1,\ldots,H_k$ for $V$, using the Noetherian property of the polynomial ring. Each $H_i(G_a(u,t))$ belongs to $\mathbb Q_p\langle t\rangle$. If all are identically zero, every $p$-adic time is a hit. Otherwise one nonzero function bounds the simultaneous integer hit set by Lemma [\[zeros\]](#zeros){reference-type="ref" reference="zeros"}. This includes the empty and full varieties.

For $u=(0,1)$ and $V=\{x=0\}$ the first coordinate's first Mahler term is $at$, with all higher terms strictly smaller for $t\ne0$. Thus $|x(G_a((0,1),t))|_p=|at|_p$ and the hit set is exactly $\{0\}$. At the origin, any variety containing it is hit at every time. These are proved examples of both alternatives. There is no uniform last-hit time, universal finite identity-test algorithm, or claim that every minimal component is an algebraic curve or is Zariski dense.

# Haar structure and the noncompact source operator

Every residue ball modulo $p^N$ has Haar measure $p^{-2N}$. The finite permutation preserves these balls' measures; the balls generate the Borel sigma algebra, so $F_a$ preserves Haar measure. Every $p$-adic time map also induces a permutation on each finite quotient, by continuity from integer times and the inverse action law. Therefore it is Haar preserving as well.

On complex $L^2(X)$, $Uf=f\circ F_a$ is unitary, and $Jf=\overline{f\circ R_0}$ is an antiunitary with $J^2=I$ and $JUJ=U^{-1}$. The space has subspaces of unbounded dimensions from residue partitions. A unitary sends an orthonormal sequence to another one, with pairwise distances $\sqrt2$, so $U$ is not compact and belongs to no finite Schatten class. An ordinary trace-class determinant of $I-zU$ does not follow; no claim excludes every possible relative regularization.

A nonzero minimal component of radius $p^{-r}$ meets exactly $p^{N-c-2r}$ residue balls when $N>c+2r$. Their total ambient measure is $p^{-N-c-2r}$, which tends to zero. Hence every such component has zero two-dimensional Haar measure despite its minimal adding-one dynamics.

# Exact audit and target firewall

The producer's shell formulas were checked against complete independently enumerated residue permutations for sixteen parameters at four primes: 56 levels and 109,876 residue vectors. A separate expanded-map computation checks 2,880 displacements at precision three digits beyond their predicted valuation. Sparse integer finite differences give 512 coefficient cells; an independent substitution recurrence reconstructs them. There are 1,024 ordinary factorial-tail rows and 4,592 exact symbolic checks. These finite lanes test implementations, not the universal theorems above.

The reproducibility package also contains two-directory byte replay, repaired-hash semantic and exact-type attacks, strict evaluation locks, actual release-write refusal under hostile YAML, and deterministic double builds of each manuscript revision. It discloses internal same-model-family review rather than external or human peer review.

The strict Route-A tuple is $$(\mathrm{A0\ weak},\mathrm{A1\ weak},\mathrm{A2\ fail},
   \mathrm{A3\ fail},\mathrm{A4\ formal}).$$ Local valuation arithmetic, complete source cycle laws, and natural reversal do not produce an all-prime primitive clock or a target divisor.

All target claim flags remain false. Route B remains disabled. The frozen firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Revision record {#revision-record .unnumbered}

Round zero: source automorphism, joint analytic time and genuine-period collapse. Exact orbit scales and finite-level classification are deferred. Round one: strict first-term dominance, all minimal components, every residue period and the complete finite native zeta are added with proofs. Round two: the self-contained zero bound, all algebraic hitting alternatives, explicit one-hit control, Haar-zero components, operator obstruction and completed exact-audit contract are added. The source is unchanged.

9 B. Poonen, *$p$-adic interpolation of iterates*, Bull. Lond. Math. Soc. **46** (2014), 525--527. [doi:10.1112/blms/bdu010](https://doi.org/10.1112/blms/bdu010). J. P. Bell, D. Ghioca and T. J. Tucker, *The dynamical Mordell--Lang problem for étale maps*, Amer. J. Math. **132** (2010), 1655--1675. [arXiv:0808.3266](https://arxiv.org/abs/0808.3266). F. Mukhamedov, *Effective Strassmann Certificates for Local $p$-adic Dynamical Mordell--Lang Interpolants*, preprint (2026). [arXiv:2607.14339v1](https://arxiv.org/abs/2607.14339v1).
