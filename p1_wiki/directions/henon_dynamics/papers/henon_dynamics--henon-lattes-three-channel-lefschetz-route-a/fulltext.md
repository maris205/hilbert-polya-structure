---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lattes-three-channel-lefschetz-route-a"
canonical_tex: "henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/paper/main.pdf"
source_sha256: "2305a8ac2d6ab644dc7b845f981dba0e1af49b30b97c0e333b7e06c05b2acfc3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Three Multiplier Channels and a Lefschetz Identity for the Full Multiplication Lattès Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lattes_three_channel_lefschetz_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let an integer multiplication map $[m]$ on a complex elliptic curve descend through the quotient by sign to a Lattès map $f_m$ on the sphere. Uniformly over every elliptic modulus, $m\ge2$, and iterate $n\ge1$, we resolve the fixed set into regular plus, regular minus, and branch channels. With $a=m^n$ and $h=1$ for even $a$, $h=4$ for odd $a$, their counts are $((a-1)^2-h)/2$, $((a+1)^2-h)/2$, and $h$, with multipliers $a,-a,a^2$. They give a holomorphic Lefschetz sum equal to one. We derive the exact period ledger, $\zeta_{\rm AM}=((1-z)(1-m^2z))^{-1}$, and the Wold model $I_{\mathbb C}\oplus S^{(\aleph_0)}$ of the natural Haar Koopman isometry. The theorem is a full Lattès classification but a sharp Route-A stop: its counts are modulus-blind and its canonical operator is noncompact.
author:
- 'Route-A structural certificate HCS-C180'
title: |
  Three Multiplier Channels and a Lefschetz Identity\
  for the Full Multiplication Lattès Family
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Lattès map; elliptic torsion; holomorphic Lefschetz formula; Artin--Mazur zeta; Wold decomposition.

chinese-simplified

中文摘要

对任意复椭圆曲线、整数 $m\ge2$ 与迭代次数 $n\ge1$，本文完整分类乘法 $[m]$ 经 $\{\pm1\}$ 商降下的拉泰斯映射不动点。令 $a=m^n$；不动类分为 正、负与分支三通道，其乘子分别为 $a,-a,a^2$，计数中的分支修正由 $a$ 的 奇偶性决定。三通道给出恰为一的莱夫谢茨和，并导出精确周期、动力学 泽塔与自然哈尔及库普曼等距算子的沃尔德分解。该结果是完整动力学定理， 但因计数对模参数失明且算子非紧，它同时构成严格的甲路线停止定理。

# Family and fixed-class theorem

Let $E=\mathbb C/(\mathbb Z+\tau\mathbb Z)$ be any complex elliptic curve, $\pi:E\to E/\{\pm1\}\simeq\mathbb P^1$, and $m\ge2$. Define $f_m$ by $f_m\pi=\pi[m]$. This classical Lattès construction is prior work; see Milnor [@milnor]. We claim no priority for that construction, torsion periodic points, or the holomorphic Lefschetz formula.

Fix $n\ge1$, put $a=m^n$, and define $h(a)=1$ when $a$ is even and $h(a)=4$ when $a$ is odd.

[\[thm:channels\]]{#thm:channels label="thm:channels"} For every $E,m,n$, $$\operatorname{Fix}(f_m^n)=\big(E[a-1]\cup E[a+1]\big)/\{\pm1\}.$$ The fixed classes split disjointly as

  channel                 count          multiplier         origin
  --------------- --------------------- ------------ --------------------
  regular plus     $N_+=((a-1)^2-h)/2$      $+a$           $E[a-1]$
  regular minus    $N_-=((a+1)^2-h)/2$      $-a$           $E[a+1]$
  branch             $N_{\rm br}=h$        $a^2$      common two-torsion

In particular, $\#\operatorname{Fix}(f_m^n)=a^2+1$ and $$\label{eq:lef}
 \frac{N_+}{1-a}+\frac{N_-}{1+a}+\frac{N_{\rm br}}{1-a^2}=1.$$

The equality $f_m^n\pi(P)=\pi(P)$ is equivalent to $[a]P=P$ or $[a]P=-P$, which gives the torsion union. Its intersection is $E[\gcd(a-1,a+1)]$: it has one element for even $a$ and four for odd $a$. These are exactly the quotient branch classes. Remove the intersection and pair the remaining points by sign to obtain the counts.

Off the branch locus, $\pi$ is locally biholomorphic. The chain rule gives $+a$ on the first torsion set. On the second, the identity $D\pi_{-P}=-D\pi_P$ supplies the sign $-a$. At two-torsion a quotient coordinate is the square of a torus coordinate, so the multiplier is $a^2$. The total and [\[eq:lef\]](#eq:lef){reference-type="eqref" reference="eq:lef"} follow by direct algebra.

## Why the branch channel cannot be merged {#why-the-branch-channel-cannot-be-merged .unnumbered}

The common torsion classes are not double-counted regular points. Their local coordinate is quadratic, so replacing them by either regular channel would assign multiplier $\pm a$ instead of $a^2$. The resulting fixed total could still be repaired arithmetically, but the local Lefschetz sum would be wrong. Thus the three-channel statement is strictly stronger than the scalar count $a^2+1$ and is the minimal branch-aware invariant of the quotient.

# Exact periods and zeta

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} The exact-period point count and primitive-cycle count are $$P_m(n)=\sum_{d\mid n}\mu(n/d)(m^{2d}+1),\qquad P_m(n)/n,$$ and $$\label{eq:zeta}
 \zeta_{\rm AM}(z)=\exp\!\left(\sum_{n\ge1}(m^{2n}+1)\frac{z^n}{n}\right)
 =\frac1{(1-z)(1-m^2z)}.$$

Möbius inversion separates exact periods, and exact-period points partition into cycles of size $n$. Equation [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is the sum of two geometric logarithmic series.

# Natural operator and Wold boundary

Let $\nu=\pi_*\operatorname{Haar}_E$ and let $U_mg=g\circ f_m$ on $L^2(\mathbb P^1,\nu)$. Pullback identifies this Hilbert space with the even subspace of $L^2(E)$. For nonzero dual-lattice $k$, set $c_k=(e_k+e_{-k})/\sqrt2$, indexed modulo sign. Then $$U_mc_k=c_{mk}.$$ Every nonzero $k\in\mathbb Z^2$ is uniquely $m^jr$ with $r\notin m\mathbb Z^2$, modulo sign. Each primitive $r$ starts a unilateral shift chain, and there are countably many such roots. Constants form the only unitary summand. Therefore $$\label{eq:wold}
 U_m\simeq I_{\mathbb C}\oplus S^{(\aleph_0)},\qquad
 U_m^*c_k=\begin{cases}c_{k/m},&k\in m\mathbb Z^2,\\0,&\text{otherwise}.
 \end{cases}$$ The isometry is proper, noncompact, and outside every finite Schatten class; an ordinary Fredholm determinant $\det(I-zU_m)$ is unavailable. Pullback of an ample line bundle is only a formal alternative: $[m]^*L$ has degree $m^2\deg L$, so it does not act on one fixed quantization space.

This operator statement uses only pushed-forward Haar measure. It neither chooses a polarization nor identifies Hilbert spaces of different line-bundle degree. Consequently the Wold model is canonical for the frozen measurable system, whereas the line-bundle suggestion is deliberately recorded only as a change-of-space hint.

# Exact validation ledger

The proof above is global; finite computations are regression sentinels, not proof. Exact software independently enumerated the following frozen ledgers.

  ledger                                         exact total
  -------------------------------------------- -------------
  formula rows $(2\le m\le10,\ 1\le n\le12)$             108
  direct torsion-union enumerations                       16
  materialized rational torus points                  25,290
  even Fourier-mode rows                               5,880
  independent-checker assertions                      43,184
  SymPy identity checks                               18,065
  repaired/stale-hash mutation rejections             $23+1$

The torsion sentinel forms both finite rational tori as sets before taking their intersection and sign quotient. The checker imports no producer code; byte replay is exact. This distinguishes branch-class validation from mere substitution into the closed count formula.

# Route-A decision

The exact tuple is $$(\texttt{A0\_FAIL},\texttt{A1\_WEAK},\texttt{A2\_FAIL},
 \texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT}).$$ A0 fails because torsion classes have no intrinsic rational-prime labels or prime-power weights. A1 remains weak despite complete orbit counts because no arithmetic labels or target amplitudes occur. The elementary zeta is independent of $\tau$, giving A2 and A3 failure. Equation [\[eq:wold\]](#eq:wold){reference-type="eqref" reference="eq:wold"} is canonical but non-Schatten, so A4 is only a formal hint. A0 failure forces `ROUTE_A_REJECTED`.

  ------------------------------------------------------------------------------------------------
  gate               decisive boundary
  ------------------ -----------------------------------------------------------------------------
  A0\_FAIL           no rational-prime labels, logarithmic-prime clock, or prime-power weights

  A1\_WEAK           complete primitive ledger, but no arithmetic labels or target amplitudes

  A2\_FAIL           exact elementary zeta is independent of elliptic modulus

  A3\_FAIL           rational continuation has no target functional equation or Weil compression

  A4\_FORMAL\_HINT   canonical Koopman lift is a proper non-Schatten isometry
  ------------------------------------------------------------------------------------------------

## Limitations and ownership {#limitations-and-ownership .unnumbered}

The theorem concerns the multiplication family descended through the sign quotient. It does not cover translated affine maps, general isogenies between different elliptic curves, or arbitrary postcritically finite rational maps. The disappearance of $\tau$ from the fixed count is a proved universality statement, not evidence for an arithmetic target hidden in the modulus.

The Wold theorem is an observable-space classification. It supplies neither a self-adjoint generator nor an ordinary Fredholm determinant, and changing to a natural extension or a varying line-bundle space would change the frozen candidate. These alternatives are therefore boundaries rather than repairs.

Milnor's work is cited for the classical Lattès setting. The branch-resolved ledger, Route-A audit, and software integrity artifacts are the contribution of this certificate; no general literature-priority claim is made for the component identities. Finite ledgers can expose implementation errors but cannot establish the all-parameter theorem.

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. No prime table, target divisor, arithmetic local factor, Euler factor, root number, automorphy, Hilbert--Pólya operator, Route-B authorization, external review, or acceptance rate is claimed.

1 J. Milnor, *On Lattès Maps*, arXiv:math/0402147 (2004), <https://arxiv.org/abs/math/0402147>.
