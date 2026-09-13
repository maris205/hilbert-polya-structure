---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-s4-frobenius-root-scheme-route-a"
canonical_tex: "henon_dynamics/henon_s4_frobenius_root_scheme_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_s4_frobenius_root_scheme_route_a/paper/main.pdf"
source_sha256: "e40d54bf632a798b038725679ebc331e3d9c6912b1eee35f35e5feb145d8e0ce"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Complete $S_4$ Chebotarev--Frobenius Permutation Atlas for the Root Scheme of $x^4-x-1$

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_s4_frobenius_root_scheme_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_s4_frobenius_root_scheme_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_s4_frobenius_root_scheme_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_s4_frobenius_root_scheme_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The integral quartic $f(x)=x^4-x-1$ defines an intrinsic prime-indexed family of finite dynamical systems: arithmetic Frobenius $F_p(\alpha)=\alpha^p$ permutes the four geometric roots at every good prime. We prove that $\operatorname{disc}(f)=-283$ and $\operatorname{Gal}(f/\mathbb Q)=S_4$, identify factor degrees with primitive cycle lengths, and close the fixed-point and finite-determinant identities on every good fiber. All five $S_4$ cycle types are exhibited. The final round adds their Chebotarev densities, the non-étale boundary at $p=283$, and the exact fiberwise Koopman classification. The construction is a source-arithmetic candidate, not a cross-prime target determinant. The universal finite-permutation trace/determinant mechanism remains owned by the prior workspace package HCS-C12A; our owner is the complete $x^4-x-1$-specific atlas and its executable convention lock.
author:
- 'HCS-C369 / HEN-O353'
date: 4 September 2026
title: |
  The Complete $S_4$ Chebotarev--Frobenius Permutation Atlas\
  for the Root Scheme of $x^4-x-1$
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3692026090400000000000000000000\>\<C3692026090400000000000000000000\>\]

# Quartic arithmetic and the $S_4$ proof

Put $$\label{eq:f}
 f(x)=x^4-x-1,\qquad
 \mathcal X=\operatorname{Spec}\mathbb Z[x]/(f).$$ For a rational prime $p$, write $X_p$ for the geometric roots of the reduction of $f$ in $\overline{\mathbb F_p}$. We use *arithmetic Frobenius* $$\label{eq:frob}
 F_p:X_p\longrightarrow X_p,\qquad \alpha\longmapsto\alpha^p.$$ Geometric Frobenius is $F_p^{-1}$. The two conventions have identical cycle lengths, fixed counts, and determinants; this paper never conflates the maps, only their common cycle partition.

[\[thm:galois\]]{#thm:galois label="thm:galois"} The discriminant of $f$ is $-283$. The polynomial is irreducible over $\mathbb Q$ and its splitting field $L$ has $$\operatorname{Gal}(L/\mathbb Q)\cong S_4.$$ Every prime $p\ne283$ is unramified and $\mathcal X_{\mathbb F_p}$ is a finite étale scheme of degree four. If $\lambda_p=(d_1,\ldots,d_k)$ is the multiset of degrees of the distinct irreducible factors of $f\bmod p$, then $\lambda_p$ is exactly the cycle partition of $F_p$ on $X_p$.

For $x^4+qx+r$ the discriminant is $256r^3-27q^4$; inserting $q=r=-1$ gives $-256-27=-283$. Modulo $2$, $$f=x^4+x+1.$$ It has no root, and the only monic irreducible quadratic over $\mathbb F_2$ is $x^2+x+1$, whose square is $x^4+x^2+1$. Hence $f\bmod2$ is irreducible. Gauss's lemma makes $f$ irreducible over $\mathbb Q$, so its Galois group $G\le S_4$ is transitive. Dedekind's theorem [@Serre; @Neukirch] at the unramified prime $2$ supplies a $4$-cycle. At $p=7$, $$\label{eq:p7}
 f\equiv(x-3)(x^3+3x^2+2x-2)\pmod 7,$$ and the cubic factor has no root, so $G$ also contains a $3$-cycle. Consequently $12$ divides $|G|$, while $|G|$ divides $24$. A subgroup of order $12$ in $S_4$ is the index-two sign kernel $A_4$, but a $4$-cycle is odd; equivalently, the discriminant is not a square. Therefore $G=S_4$.

The discriminant criterion makes precisely $p=283$ exceptional. At every other prime, the roots are distinct. An irreducible factor of degree $d$ has its roots in one orbit of $\alpha\mapsto\alpha^p$ of length $d$, and every orbit arises this way [@Lidl]. This proves the dictionary.

[\[prop:witnesses\]]{#prop:witnesses label="prop:witnesses"} Every partition of four occurs among the good fibers. In addition to [\[eq:p7\]](#eq:p7){reference-type="eqref" reference="eq:p7"}, one has $$\begin{aligned}
 p=2 &: & f&=x^4+x+1 &&(4),\\
 p=17&: & f&=(x+2)(x+5)(x^2-7x+5) &&(2+1+1),\\
 p=71&: & f&=(x^2+15x-20)(x^2-15x+32) &&(2+2),\\
 p=83&: & f&=(x+3)(x+7)(x+14)(x-24) &&(1+1+1+1),\end{aligned}$$ where every equality is in the corresponding residue field and the final parenthesis is the Frobenius cycle partition.

Multiplication gives $f$ modulo the displayed prime. The linear factors are explicit; the remaining quadratic or cubic factors have no residue-field root. The mod-$2$ case was proved in Theorem [\[thm:galois\]](#thm:galois){reference-type="ref" reference="thm:galois"}.

\>0

# All-iterate orbit and determinant closure

HCS-C12A already owns the universal zero-dimensional statement that Frobenius on a reduced finite fiber is a permutation, its iterate counts are traces, and its finite zeta is the reciprocal permutation determinant. C369 does not claim workspace ownership of that universal mechanism. This section specializes it to the five $S_4$ classes of $x^4-x-1$ and locks the factor, fixed, primitive, and determinant conventions in one executable all-good-prime ledger. For a good $p$, let $P_p$ be the permutation matrix on $\mathbb C[X_p]$ defined by $P_pe_\alpha=e_{F_p(\alpha)}$, and set $$N_p(r)=\#\operatorname{Fix}(F_p^r).$$

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} Let $p\ne283$, let $\lambda_p=(d_1,\ldots,d_k)$, and let $r,n\ge1$. Then $$\label{eq:fixed}
 N_p(r)=\sum_{j:d_j\mid r}d_j.$$ If $E_p(n)$ is the number of points of exact period $n$ and $C_p(n)$ the number of primitive $n$-cycles, then $$\label{eq:primitive}
 E_p(n)=\sum_{d\mid n}\mu(d)N_p(n/d),
 \qquad C_p(n)=\frac{E_p(n)}n.$$ Finally, in $\mathbb Q[[u]]$ and therefore as a rational function, $$\label{eq:zeta}
 \begin{split}
 Z_p(u)&:=\exp\!\left(\sum_{r\ge1}\frac{N_p(r)}r u^r\right)\\
 &=\det(I-uP_p)^{-1}
 =\prod_{j=1}^k(1-u^{d_j})^{-1}.
 \end{split}$$ Thus the factor degrees are not merely a fixed-point statistic: they are the complete primitive-cycle ledger on the fiber.

A $d$-cycle contributes all its $d$ points to $\operatorname{Fix}(F_p^r)$ exactly when $d\mid r$, proving [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. The relation $N_p(r)=\sum_{n\mid r}E_p(n)$ and Möbius inversion give [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"}; division by $n$ groups exact-period points into cycles. On a $d$-cycle block $C_d$, $\det(I-uC_d)=1-u^d$. Multiplying blocks proves the determinant equality, while $$-\log(1-u^d)=\sum_{m\ge1}\frac{u^{dm}}m
 =\sum_{m\ge1}\frac d{dm}u^{dm}$$ and [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} prove the exponential equality.

::: {#tab:counts}
  type                      $1+1+1+1$   $2+1+1$   $2+2$   $3+1$   $4$
  ----------------------- ----------- --------- ------- ------- -----
  good primes $\le10^4$            43       306     147     411   321
  $S_4$ class size                  1         6       3       8     6

  : Exact finite regression counts. The 1,228 entries sum across the row; these counts are not used to prove an asymptotic density.
:::

The canonical evidence enumerates all $1{,}229$ primes at most $10^4$, removes the unique bad prime $283$, and checks [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}--[\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} for $1\le r\le12$ on all $1{,}228$ good fibers: $14{,}736$ prime--iterate cells. A separate factorization backend recomputes every partition. Exact symbolic and hostile-mutation lanes test the proof anchors and schema. Finite enumeration is an implementation receipt; Theorems [\[thm:galois\]](#thm:galois){reference-type="ref" reference="thm:galois"} and [\[thm:zeta\]](#thm:zeta){reference-type="ref" reference="thm:zeta"} establish the quartic specialization for all good primes and all iterates.

\>1

# Chebotarev density, bad fiber, and operator boundary

This round completes the quartic-specific density, bad-fiber, and route boundary.

[\[thm:density\]]{#thm:density label="thm:density"} The natural densities of good primes with the five factor partitions are

  $\lambda_p$    $1+1+1+1$   $2+1+1$   $2+2$   $3+1$    $4$
  ------------- ----------- --------- ------- ------- -------
  density         $1/24$      $1/4$    $1/8$   $1/3$   $1/4$

At the excluded prime, $$\label{eq:bad}
 f\equiv(x-115)(x-93)^2(x+18)\pmod {283},
 \qquad \gcd(f,f')=x-93.$$ Hence $\mathcal X_{\mathbb F_{283}}$ is non-étale; no four-distinct-point permutation atlas is asserted there.

The conjugacy classes of $S_4$ with cycle types $1+1+1+1,2+1+1,2+2,3+1,4$ have sizes $1,6,3,8,6$. By Theorem [\[thm:galois\]](#thm:galois){reference-type="ref" reference="thm:galois"}, Dedekind's dictionary identifies these classes with the factor partitions. Chebotarev's density theorem divides each class size by $|S_4|=24$ [@Neukirch]. Multiplication verifies [\[eq:bad\]](#eq:bad){reference-type="eqref" reference="eq:bad"}; the common root $93$ of $f$ and $f'$ proves nonreducedness.

[\[prop:koopman\]]{#prop:koopman label="prop:koopman"} For each good $p$, $P_p$ is a canonical unitary on the four-dimensional Hilbert space $\ell^2(X_p)$. It is self-adjoint exactly for types $1+1+1+1$, $2+1+1$, and $2+2$. For types $3+1$ and $4$ it remains unitary but is not self-adjoint.

$P_p$ permutes an orthonormal basis, so $P_p^*=P_p^{-1}$. It is self-adjoint precisely when $P_p=P_p^{-1}$, or $F_p^2=I$; this is equivalent to every cycle having length at most two.

# Route decision and nonclaims

The integral scheme supplies prime fibers, prime-power Frobenius iterates, Chebotarev classes, and source-derived primitive weights. It therefore earns $A0_{\rm STRUCTURAL\_ARITHMETIC\_RELATION}$. The exact rational finite-fiber determinant in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} earns the deliberately local $A1_{\rm PASS\_ANALYTIC}$ as an exact applicability result, not as new ownership of the universal mechanism. Proposition [\[prop:koopman\]](#prop:koopman){reference-type="ref" reference="prop:koopman"} gives $A4_{\rm NATURAL\_QUANTIZATION}$.

The prime $p$ indexes a different fiber; it is not a time step of one autonomous system. We construct no cross-prime Fredholm direct sum, no determinant-class regularization, and no target Euler product. There is no target continuation, functional equation, divisor, zero fit, or counting law. Thus $A2_{\rm FAIL}$ and $A3_{\rm FAIL}$. The overall verdict is `ROUTE_A_ARITHMETIC_CANDIDATE`, under the literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`. Fiber permutation unitaries are not a Hilbert--Pólya operator, and Route B is not invoked.

9 J.-P. Serre, *Topics in Galois Theory*, second edition, A K Peters, 2008. J. Neukirch, *Algebraic Number Theory*, Springer, 1999. R. Lidl and H. Niederreiter, *Finite Fields*, second edition, Cambridge University Press, 1997.
