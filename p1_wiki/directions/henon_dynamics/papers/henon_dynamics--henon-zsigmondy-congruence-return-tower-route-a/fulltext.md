---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-zsigmondy-congruence-return-tower-route-a"
canonical_tex: "henon_dynamics/henon_zsigmondy_congruence_return_tower_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_zsigmondy_congruence_return_tower_route_a/paper/main.pdf"
source_sha256: "c0e6b514b42192107b4facb14ef8f40bf2f200712a30418ef82da3a915787457"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Zsigmondy Congruence-Return Towers and the Global Determinant-Owner Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_zsigmondy_congruence_return_tower_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_zsigmondy_congruence_return_tower_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_zsigmondy_congruence_return_tower_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_zsigmondy_congruence_return_tower_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every coprime pair $a>b\ge1$, multiplication by $ab^{-1}$ on $(\mathbb Z/N\mathbb Z)^\times$ defines an arithmetic dynamics without fitted data. A prime $p$ is primitive for $a^n-b^n$ exactly when the marked point $1$ first returns at time $n$ on the $p$-fiber. Classical Zsigmondy existence supplies such a prime outside its two exact exception forms; that theorem is attributed, not claimed new. If $e=v_p(a^n-b^n)$, the least return on every $p^k$-fiber is $np^{\max(0,k-e)}$. Every admissible finite fiber has a complete cycle, fixed-point, zeta, determinant, and reversor ledger. Globally, however, the disjoint union has fixed ledger $a^n-b^n$ and zeta $(1-bz)/(1-az)$, whereas the profinite inverse-limit translation has no positive-time fixed points and zeta $1$. Thus finite fibers alone do not select a unique global determinant owner.
author:
- 'Route-A structural certificate C179'
title: 'Zsigmondy Congruence-Return Towers and the Global Determinant-Owner Obstruction'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** primitive divisor; first return; congruence dynamics; multiplicative order; Zsigmondy theorem.

chinese-simplified

中文摘要

对互素整数 $a>b\ge1$，在有限单位群 $(\mathbb Z/N\mathbb Z)^\times$ 上乘以 $ab^{-1}$ 给出一个无需拟合数据的算术动力系统。本文证明：素数 $p$ 是 $a^n-b^n$ 的本原素因子，当且仅当标记点 $1$ 在模 $p$ 纤维上首次于时刻 $n$ 返回。经典的 [Zsigmondy]{lang="en"} 定理给出除两个精确例外类型之外的存在性； 本文明确归属该经典结果，并不声称其为新定理。若 $e=v_p(a^n-b^n)$，模 $p^k$ 纤维的最小返回时间为 $np^{\max(0,k-e)}$；每个允许的有限纤维都有完整的 循环、不动点、$\zeta$、行列式与反演账本。然而，两种自然全局化并不一致： 不交并的第 $n$ 步不动点数为 $a^n-b^n$，而逆极限平移在所有正时间均无不动点。 因此，有限纤维本身不能选出唯一的全局行列式载体。

# Frozen arithmetic dynamics

Fix coprime integers $a>b\ge1$. For every $N\ge2$ with $(N,ab)=1$, set $$U_N=(\mathbb Z/N\mathbb Z)^\times,\qquad
q_N=ab^{-1}\pmod N,\qquad R_N(x)=q_Nx,$$ and mark $1\in U_N$. One multiplication is one discrete source step. No logarithmic prime roof, prime weight, target table, or fitted parameter is introduced.

# Primitive-return theorem

**Theorem.** For every prime $p$ and $n\ge2$, the following are equivalent:

1.  $p\mid a^n-b^n$ and $p\nmid a^m-b^m$ for $1\le m<n$;

2.  $p\nmid ab$ and $\operatorname{ord}_p(ab^{-1})=n$;

3.  $1$ has least positive return $n$ under $R_p$.

Moreover, such a prime exists except when $(a,b,n)=(2,1,6)$, or when $n=2$ and $a+b$ is a power of two.

*Proof.* A prime divisor of $a^n-b^n$ cannot divide $ab$. Thus $a^m\equiv b^m\pmod p$ is equivalent to $(ab^{-1})^m\equiv1\pmod p$. Excluding all earlier $m$ is exactly the definition of multiplicative order, and the orbit of the mark is $1,q_p,q_p^2,\ldots$. The existence and exception sentence is the classical Zsigmondy theorem [@Zsigmondy1892]; no new proof or strengthening of that theorem is claimed. $\square$

Every primitive return prime for $n\ge2$ is odd. Indeed, if $a,b$ are odd, then $2\mid a-b$ already at time one; if they have opposite parity, every $a^n-b^n$ is odd.

# Exact lift through every prime power

Let $p$ be primitive at $n$, and set $e=v_p(a^n-b^n)$. Then $p$ is odd and $n=\operatorname{ord}_p(ab^{-1})\mid p-1$. For every $k\ge1$, $$\boxed{\operatorname{ord}_{p^k}(ab^{-1})
=n p^{\max(0,k-e)}}.\tag{1}$$ Indeed, an exponent returning modulo $p^k$ must be $nr$. Since $b$ is a $p$-adic unit, odd-prime lifting of the exponent gives $$v_p((ab^{-1})^{nr}-1)=e+v_p(r).$$ The least eligible $r$ is $p^{\max(0,k-e)}$. Thus every orbit on the $p^k$-fiber has the length in (1), and the number of cycles is $\varphi(p^k)/(np^{\max(0,k-e)})$.

# Complete dynamics on every finite fiber

For any admissible $N$, write $L_N=\operatorname{ord}_N(q_N)$. Translation returns a point $x$ exactly when $q_N^t=1$, independently of $x$. Hence $U_N$ is $\varphi(N)/L_N$ cycles, each of length $L_N$, and $$\#\operatorname{Fix}(R_N^t)=
\begin{cases}\varphi(N),&L_N\mid t,\\0,&L_N\nmid t,\end{cases}
\quad
\zeta_N(z)=(1-z^{L_N})^{-\varphi(N)/L_N}.\tag{2}$$ For the finite permutation Koopman matrix $\mathcal U_N$, using the fixed-count convention of Artin and Mazur [@ArtinMazur1965], $$\det(I-z\mathcal U_N)=(1-z^{L_N})^{\varphi(N)/L_N}.\tag{3}$$ Inversion $J_N(x)=x^{-1}$ satisfies $J_NR_NJ_N=R_N^{-1}$ because $(q_Nx^{-1})^{-1}=xq_N^{-1}$.

# Two globalizations and owner nonselection

Adjoin the singleton $U_1$ and act fiberwise on $\mathcal D_{a,b}=\bigsqcup_{(N,ab)=1}U_N$. The $N$-fiber is fixed at time $n$ exactly when $N\mid a^n-b^n$. Every such divisor is admissible, and the divisor--totient identity gives $$\#\operatorname{Fix}(R^n)=\sum_{N\mid a^n-b^n}\varphi(N)=a^n-b^n.\tag{4}$$ Consequently, $$\zeta_{\mathcal D}(z)
=\exp\!\left(\sum_{n\ge1}\frac{a^n-b^n}{n}z^n\right)
=\frac{1-bz}{1-az},\qquad
C_n=\frac1n\sum_{d\mid n}\mu(n/d)(a^d-b^d),\tag{5}$$ where $C_n$ counts primitive cycles of length $n$.

Now take the inverse limit $\widehat U^{(ab)}=\varprojlim_{(N,ab)=1}U_N$ and translate by the compatible element $q=a/b$. A time-$n$ fixed point would force $q^n=1$ in every finite quotient. Choosing a prime outside the finite divisor set of $ab(a^n-b^n)$ contradicts this. Hence $$\operatorname{Fix}(R^n\mid\widehat U^{(ab)})=\varnothing\quad(n\ge1),
\qquad \zeta_{\widehat U}(z)=1.\tag{6}$$ Equations (4) and (6) are incompatible fixed ledgers for two source-natural globalizations. Therefore the finite congruence fibers do not select one global periodic-orbit determinant owner. This is a no-go for uniqueness without extra structure, not an absolute claim that every enlarged owner is impossible.

#### Same-clock operator corollary.

Counting measure makes each finite permutation Koopman operator unitary, and normalized counting measures are compatible with the inverse-limit Haar probability measure. Translation by $q$ therefore induces a canonical unitary Koopman operator on $L^2(\widehat U^{(ab)})$. Fiberwise inversion and profinite inversion reverse these operators on the unchanged discrete clock. This supplies the natural A4 lift; it does not choose between (4) and (6), nor does it create a target determinant.

# Exact audit and Route-A decision

The ledger has 567 primitive-divisor, 2,080 prime-power, 1,650 finite-fiber, and 630 globalization rows. Its seven no-return rows are exactly the classical exceptions. A producer-independent checker passes 320,291 assertions; SymPy passes 6,674 exact checks; byte replay is exact; 64 repaired-hash mutations and one stale-hash mutation are rejected. These are regression sentinels; (1)--(6) have no cutoff.

  Gate   Verdict     Exact boundary
  ------ ----------- ----------------------------------------------------------------
  A0     `WEAK`      primes are intrinsic first-return moduli, not one global owner
  A1     `WEAK`      every finite fiber is exact; global ledgers disagree
  A2     `FAIL`      no target divisor or frozen target validation protocol
  A3     `FAIL`      no target analytic law or Weil compression
  A4     `NATURAL`   finite permutation and profinite Haar Koopman lifts

The exact tuple is

`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,` `A4_NATURAL_QUANTIZATION)`.

Overall: `ROUTE_A_EXPLORATORY`; Route B is false. A0 is weak, not passed: no logarithmic prime clock or selected global prime-orbit owner exists. A4 records canonical same-clock source unitaries and repairs none of A0--A3.

#### Attribution boundary.

Zsigmondy's existence theorem is external. Birkhoff--Vandiver [@BirkhoffVandiver1904] supplies historical divisor context, while Silverman's dynamical Zsigmondy work [@Silverman2013] supplies modern context only. Neither is presented as proof of the package's lift, finite-fiber, or globalization theorems.

#### Scope and limitations.

No target zero or prime table, local arithmetic factor, root number, automorphy input, prime-weighted global product, logarithmic prime roof, or Route-B authorization enters this note. Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`. A primitive prime labels a finite return fiber; it is not identified with an isolated prime-labeled orbit inside one global phase space. The rational function in (5) is an unweighted source zeta, not an arithmetic local factor or a product indexed by primes. The profinite result rules out fixed points for that natural inverse-limit translation only. It does not rule out a future enlarged model supplied with an independently justified owner-selection principle.

# Declarations {#declarations .unnumbered}

**Data and code.** Package-local exact evidence and deterministic code accompany the paper. **Ethics.** No human, animal, clinical, personal, private, or sensitive data are used; approval is not applicable. **CRediT.** This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing; AI systems are not authors. **Funding.** No external funding. **Conflicts.** None known. **AI use.** An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or an independent error process.

9 K. Zsigmondy, "Zur Theorie der Potenzreste," *Monatshefte für Mathematik und Physik* 3 (1892), 265--284. [doi:10.1007/BF01692444](https://doi.org/10.1007/BF01692444). G. D. Birkhoff and H. S. Vandiver, "On the Integral Divisors of $a^n-b^n$," *Annals of Mathematics* 5(4) (1904), 173--180. [doi:10.2307/2007263](https://doi.org/10.2307/2007263). M. Artin and B. Mazur, "On Periodic Points," *Annals of Mathematics* 81(1) (1965), 82--99. [doi:10.2307/1970384](https://doi.org/10.2307/1970384). J. H. Silverman, "Primitive Divisors, Dynamical Zsigmondy Sets, and Vojta's Conjecture," *Journal of Number Theory* 133(9) (2013), 2948--2963. [doi:10.1016/j.jnt.2013.03.005](https://doi.org/10.1016/j.jnt.2013.03.005).
