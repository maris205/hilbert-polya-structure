---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-salem-toral-orbit-fluctuation-route-a"
canonical_tex: "henon_dynamics/henon_salem_toral_orbit_fluctuation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_salem_toral_orbit_fluctuation_route_a/paper/main.pdf"
source_sha256: "e4bcc10fa69788745ad9f4bb33521f97c79fbd401ded8f5375c4a733c9776531"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Salem Toral Dynamics: \ifcase\CRevisionRound Exact Fixed Groups and Rational Zeta \or Primitive and Cumulative Orbit Fluctuations \else Orbit Fluctuations, Homoclinic Rigidity and a Cyclotomic Boundary\fi

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_salem_toral_orbit_fluctuation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_salem_toral_orbit_fluctuation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_salem_toral_orbit_fluctuation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_salem_toral_orbit_fluctuation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An explicit integral quartic family gives mixing symplectic toral maps with a nonexpansive central plane. We determine every finite fixed group, primitive cycle count, return multiplier and the complete rational Artin--Mazur zeta function, retaining the sign separating cardinalities from Lefschetz indices. \>0 Normalized primitive counts have an arcsine limiting law on $[0,4]$. Cumulative counts have a different explicit nonconstant oscillatory prefactor, also with an arcsine distribution. Neither result requires a Diophantine lower bound for the unit-circle conjugates. \>1 An elementary rational-subspace argument proves that the homoclinic group is trivial. The excluded cyclotomic parameter instead has positive-dimensional fixed sets and no ordinary cardinality zeta. These are complete source reconstructions of classical quasihyperbolic mechanisms, with independent exact arithmetic and numerical regression. Integral Salem arithmetic is not a prime-to-orbit correspondence, and no target spectral identity or literature priority is claimed.
author:
- 'HCS-C397 theorem and reproducibility package'
date: 5 September 2026
title: |
  Salem Toral Dynamics:\
  Exact Fixed Groups and Rational Zeta Primitive and Cumulative Orbit Fluctuations Orbit Fluctuations, Homoclinic Rigidity and a Cyclotomic Boundary
```

## Markdown 正文

**Keywords:** Salem number; toral automorphism; primitive orbit; dynamical zeta; homoclinic group; arcsine law.

chinese-simplified

中文摘要

本文研究一族整系数四次环面自同构，完整给出固定点群、本原轨道、返回稳定性 和有理动力学函数。系统具有混合性和辛结构，但中心方向并不扩张。 \>0 本原计数与累计计数分别呈现可显式描述的反正弦极限分布；累计轨道增长 不能用一个常数前因子概括，证明不依赖单位圆根的丢番图下界。 \>1 有理不变子空间论证排除全部非零同宿点；例外参数的固定集具有连续分支， 因此普通基数型动力学函数失去定义。 经典理论归属明确，整系数算术及完整源系统证明均不等于目标素数轨道或零点对应。

关键词：萨勒姆数；环面自同构；本原轨道；动力学函数；同宿群；反正弦律。

# A nonexpansive integral source

Fix an integer $a\ge1$, initially $a\ne2$, and let $$P_a(X)=X^4-aX^3-X^2-aX+1,\qquad
 A_a=\begin{pmatrix}0&0&0&-1\\1&0&0&a\\0&1&0&1\\0&0&1&a\end{pmatrix}.$$ The source is $x\mapsto A_ax$ on $\mathbb T^4=\mathbb R^4/\mathbb Z^4$, with one iterate as its clock and normalized Haar measure. Classical accounts of quasihyperbolic dynamics include Lind [@lind]; Waddington [@waddington] studies the nonconstant orbit asymptotics. The homoclinic obstruction is classical as well [@ls]. We prove this family's statements explicitly; the contribution here is complete source coverage and auditable conventions, not certified novelty. An abstract Salem stress polynomial in the project's Abel-law work does not supply these toral orbit and homoclinic theorems. Nor is this simply a hyperbolic cat-map parameter table.

$P_a$ is irreducible and has distinct roots $\lambda,\lambda^{-1},e^{i\theta},e^{-i\theta}$, where $\lambda>1$ and $\theta/(2\pi)$ is irrational. The map is mixing, nonexpansive, symplectic and reversibly defined on the same torus.

Put $Z=X+X^{-1}$. Then $P_a(X)/X^2=Z^2-aZ-3$, with $$z_\pm=\frac{a\pm\sqrt{a^2+12}}2,\qquad
 z_+>2,\quad -2<z_-<0,\quad 2\cos\theta=z_-.$$ The only possible rational roots, $\pm1$, give $1\mp2a\ne0$. A factorization must therefore use two monic integral quadratics. If their constants are $+1$, their linear coefficients $b,c$ satisfy $b+c=-a$, $bc=-3$, forcing $a=2$ for positive $a$. If both constants are $-1$, the cubic and linear coefficients have opposite signs, forcing $a=0$. Gauss's lemma proves irreducibility in the stated range. A root of unity would then force every conjugate onto the unit circle, contrary to $\lambda>1$.

The determinant of $A_a$ is one. The integral form and reversor are $$\Omega_a=\begin{pmatrix}0&0&1&a\\0&0&0&1\\-1&0&0&0\\-a&-1&0&0\end{pmatrix},
 \qquad R_a=[e_1,A_a^{-1}e_1,A_a^{-2}e_1,A_a^{-3}e_1].$$ Direct multiplication gives $\det\Omega_a=1$, $A_a^\top\Omega_aA_a=\Omega_a$ and $R_a^\top\Omega_aR_a=-\Omega_a$. In $\mathbb Q[X]/(P_a)$ the integral involution $X\mapsto X^{-1}$ has matrix $R_a$, so $R_a^2=I$ and $R_aA_aR_a=A_a^{-1}$.

Haar measure is preserved. Nonzero integer Fourier indices under $A_a^\top$ never repeat: a repetition would give a root of unity on their rational cyclic subspace. Distinct integer vectors eventually leave each bounded set. Character correlations therefore vanish eventually for each fixed pair of nonconstant characters. Approximation by trigonometric polynomials and unitarity prove mixing on $L^2$. On the real central plane, diagonalizability gives $\sup_{n\in\mathbb Z}\|A_a^nv\|\le C_a\|v\|$. Arbitrarily small nonzero $v$ project to points remaining arbitrarily close to zero for all time. Hence the map is not expansive.

# Every fixed group, return and zeta coefficient

For every $n\ge1$, with $B_n=A_a^n-I$, the complete fixed group is $$\operatorname{Fix}(A_a^n)\simeq\mathbb Z^4/B_n\mathbb Z^4
 \simeq\bigoplus_{j=1}^4\mathbb Z/d_j\mathbb Z,$$ where $d_1\mid\cdots\mid d_4$ are the positive Smith factors of $B_n$. Its cardinality and the number $O_n$ of oriented primitive cycles are $$\begin{aligned}
 F_n&=(\lambda^n+\lambda^{-n}-2)(2-2\cos n\theta),\label{fixed}\\
 nO_n&=\sum_{d\mid n}\mu(n/d)F_d.\label{mobius}\end{aligned}$$ For $|z|<\lambda^{-1}$ the ordinary zeta converges absolutely, and its complete rational continuation is $$\label{zeta}
 Z_a(z)=\exp\sum_{n\ge1}\frac{F_nz^n}{n}
 =\prod_{n\ge1}(1-z^n)^{-O_n}
 =\frac{(1-z)^4 Q_a(z)}{P_a(z)^2},$$ where $Q_a(z)=1+3z+(a^2+4)z^2+3z^3+z^4$.

No eigenvalue is a root of unity, so $B_n$ is nonsingular. Its kernel on the torus is $B_n^{-1}\mathbb Z^4/\mathbb Z^4$; multiplication by $B_n$ identifies it with the stated cokernel. Smith reduction gives both its structure and its order. The real expanding and contracting factors of $\det(A_a^n-I)$ have opposite signs; the conjugate pair has positive product. Thus $\det(A_a^n-I)=-F_n$, which gives [\[fixed\]](#fixed){reference-type="eqref" reference="fixed"}. Partitioning fixed points by least period gives $F_n=\sum_{d\mid n}dO_d$ and Möbius inversion gives [\[mobius\]](#mobius){reference-type="eqref" reference="mobius"}. This proves nonnegative integrality of $O_n$ without a numerical test.

Every return has derivative $A_a^n$, hence multipliers $\lambda^n,\lambda^{-n},e^{in\theta},e^{-in\theta}$. A primitive cycle of length $d$ contributes its $d$ marked points at every repetition. Reversal preserves length and reciprocates multipliers; we do not divide self-reversing or paired cycles by two. The unweighted cardinality convention has no extra phase; its signed Lefschetz counterpart is $-F_n$, not $F_n$.

Since $F_n\le4\lambda^n$, the initial series is absolutely convergent. Use $\det(I-A_a^n)=\sum_{j=0}^4(-1)^j\operatorname{tr}((\wedge^jA_a)^n)$ and $\det(I-z\wedge^2A_a)=(1-z)^2Q_a(z)$. Exterior degrees one and three both give $P_a(z)$, and zero and four both give $1-z$. The negative cardinality/index sign puts even exterior degrees in the numerator, proving [\[zeta\]](#zeta){reference-type="eqref" reference="zeta"}.

The Koopman operator itself is unitary on infinite-dimensional $L^2$, so it is noncompact and is not the trace-class operator of an ordinary Fredholm determinant. Formula [\[zeta\]](#zeta){reference-type="eqref" reference="zeta"} makes no such identification.

\>0

# Primitive and cumulative fluctuation laws

For fixed admissible $a$, $$\label{primitive}
 \frac{nO_n}{\lambda^n}=2-2\cos(n\theta)
       +O_a(n\lambda^{-n/2}).$$ The left side has cluster set $[0,4]$, limiting density $1/(\pi\sqrt{x(4-x)})$ on $(0,4)$, mean $2$ and variance $2$. For $\Pi(N)=\sum_{n\le N}O_n$, $r=\lambda^{-1}$, put $$C=\frac2{1-r},\qquad B=\frac2{|1-re^{-i\theta}|}.$$ Then $C>B>0$ and $$\label{cumulative}
 \frac{N\Pi(N)}{\lambda^N}
 =C-2\Re\frac{e^{iN\theta}}{1-re^{-i\theta}}+O_a(N^{-1}).$$ Its cluster set is $[C-B,C+B]$ and its limiting density is $1/(\pi\sqrt{B^2-(x-C)^2})$. No constant $K$ gives $\Pi(N)\sim K\lambda^N/N$.

Every proper divisor of $n$ is at most $n/2$. In [\[mobius\]](#mobius){reference-type="eqref" reference="mobius"}, use $F_d\le4\lambda^d$ and at most $n$ divisors. In addition, $F_n/\lambda^n-(2-2\cos n\theta)=O_a(\lambda^{-n})$. This proves the absolute, not relative, error in [\[primitive\]](#primitive){reference-type="eqref" reference="primitive"}. For each nonzero integer $k$, the Cesàro average of $e^{ikn\theta}$ tends to zero by its geometric-sum formula. Trigonometric approximation proves equidistribution on the circle. Pushing uniform angle through $2-2\cos t$ gives the displayed density, cluster set and moments. No assertion of small relative error is made near its zero endpoint.

To sum [\[primitive\]](#primitive){reference-type="eqref" reference="primitive"}, write $n=N-j$. For $0\le j\le N/2$, $N/(N-j)=1+O(j/N)$; the sum weighted by $r^j$ has error $O_a(1/N)$. Terms $n<N/2$ and the omitted geometric tails are exponentially small after normalization, bounded by $O_a(N^2\lambda^{-N/2})$. Summing $r^j$ and $(re^{-i\theta})^j$ gives [\[cumulative\]](#cumulative){reference-type="eqref" reference="cumulative"}. Since $\theta\notin2\pi\mathbb Z$, $|1-re^{-i\theta}|>1-r$. The same equidistribution argument gives the translated arcsine law. Its nonzero width rules out a constant prefactor. The proof never uses a lower bound on $|e^{in\theta}-1|$.

\>1

# Homoclinic obstruction and cyclotomic boundary

The homoclinic group of $A_a$ is trivial for every $a\ge1$, $a\ne2$. At $a=2$, every iterate with $3\mid n$ instead has a two-dimensional identity component in its fixed set. Its ordinary cardinality zeta is undefined.

If $A_a^nx\to0$ as $n\to\pm\infty$, choose torus lifts $v_n\to0$ on both tails. The integral vectors $A_av_n-v_{n+1}$ then vanish for sufficiently large $|n|$. Positive-tail decay forces the lift into the stable space $E_s$, negative-tail decay into the unstable space $E_u$. Since $A_a^{\pm1}$ preserve the lattice, $x=\pi(s)=\pi(u)$ with $s\in E_s$, $u\in E_u$. The vector $k=s-u$ is integral in $E_s\oplus E_u$. If nonzero, its rational cyclic span is a nonzero rational invariant subspace, hence four-dimensional by irreducibility. Its real span would lie in a two-plane, a contradiction. Thus $k=0$ and $E_s\cap E_u=\{0\}$ gives $x=0$. This explicitly specializes the classical obstruction [@ls Theorem 4.1 and Corollary 4.2].

At $a=2$, $P_2=(X^2-3X+1)(X^2+X+1)$. For $3\mid n$, $A_2^n-I$ has a rational kernel of dimension two; its fixed group has a two-torus identity component. For $3\nmid n$ the kernel is zero and the fixed group is finite. Infinite fixed cardinalities prevent the defining zeta series from existing. Formal substitution into a signed rational expression does not fix the absent cardinality coefficients.

# Verification and the arithmetic boundary

The independent audit uses $a=1,3,4,5,8$ and $1\le n\le24$: 120 complete finite fixed groups, 1,920 return-matrix cells, and twelve cyclotomic controls. A permutation/minor producer is checked by Newton power sums and independent Smith reduction. Symbolic symplectic/reversal and exterior identities are supplemented by 70-digit root calculations. These are finite regression checks, not proofs of equidistribution or homoclinic triviality. Full domains and infinite quantifiers are proved above.

The native algebraic unit, integer fixed groups and original cycle clock justify only weak arithmetic/orbit evidence. No intrinsic rational-prime carrier, logarithmic prime roof or target divisor relation is present. The conservative tuple is weak A0, weak A1, failed A2/A3 and a formal A4 hint; overall the target candidate is rejected. This verdict does not invalidate the source theorems. All nine target/Route-B flags are false: `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Revision record.

Round zero establishes exact fixed groups and rational zeta. Round one adds complete primitive and cumulative fluctuation laws. Round two closes the homoclinic and cyclotomic boundary proofs. A different team member checked the mathematics. This is not external peer review.

9 D. Lind, Dynamical properties of quasihyperbolic toral automorphisms, *Ergodic Theory Dynam. Systems* 2 (1982), 49--68. [doi:10.1017/S0143385700009573](https://doi.org/10.1017/S0143385700009573). S. Waddington, The prime orbit theorem for quasihyperbolic toral automorphisms, *Monatsh. Math.* 112 (1991), 235--248. [EuDML record 178542](https://eudml.org/doc/178542). E. Lindenstrauss and K. Schmidt, Symbolic representations of nonexpansive group automorphisms, *Israel J. Math.* 149 (2005), 227--266. [doi:10.1007/BF02772542](https://doi.org/10.1007/BF02772542); [arXiv:math/0409257](https://arxiv.org/abs/math/0409257).
