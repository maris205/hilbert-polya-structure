---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--100-least-valuation-digit-erasure"
canonical_tex: "symbolic_dynamics/papers/100-least-valuation-digit-erasure/main.tex"
canonical_pdf: "symbolic_dynamics/papers/100-least-valuation-digit-erasure/main.pdf"
source_sha256: "b1bc16c0ff98e89b64f7d8517cdd76a77dfd99807acd6baf99a28c428a8e6b7d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Least-Valuation Digit Erasure: Exact Transient Profiles Beyond Periodic Data

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/100-least-valuation-digit-erasure>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/100-least-valuation-digit-erasure/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/100-least-valuation-digit-erasure/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/100-least-valuation-digit-erasure/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/100-least-valuation-digit-erasure/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a prime $p$ and $r\geq1$, consider the absorbing map on $\mathbb Z/p^r\mathbb Z$ that subtracts the place value of the least significant nonzero base-$p$ digit. We give an exact digit-vector normal form: every step lowers the digit sum by one, so the hitting time of zero is precisely the base-$p$ digit sum. Consequently the complete transient-depth polynomial is $$(1+u+\cdots+u^{p-1})^r.$$ We derive every depth-layer cardinality, the sharp global absorption depth, symmetry and unimodality, exact moments, and the fixed-base central and local limit laws. All members of the family have the same periodic-point sequence and Artin--Mazur zeta, whereas the transient profile recovers both $p$ and $r$. This gives a small exact model in which periodic data are completely blind but finite-time basin geometry is rigid. Classical digit-sum and local-limit results are treated as owned background; the residual result is their coupling to this explicit finite dynamical system. For $p=2$ the update is Wegner's classical rightmost-one clearing step, and that specialization is expressly not claimed here.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal preprint, 29 August 2026'
title: |
  Least-Valuation Digit Erasure:\
  Exact Transient Profiles Beyond Periodic Data
```

## Markdown 正文

# Introduction and claim boundary

Periodic-orbit data are among the most effective invariants of finite and symbolic dynamical systems. They can nevertheless discard all transient information. We exhibit an elementary family where this loss is total: every parameter choice has one fixed point and no other recurrent point, but the complete distribution of entrance times is explicit and determines the parameters.

The statistic that appears is the ordinary sum of base-$p$ digits. Its distribution, asymptotics, and refinements have a substantial independent literature; for example, Drmota and Gajdosik study general distributional questions for the sum-of-digits function [@DrmotaGajdosik1998]. Likewise, the central and lattice local limit theorems used below are classical results for sums of independent variables [@Petrov1975]. There is also a direct algorithmic owner at the binary endpoint: $$E_{2,r}(x)=x-2^{v_2(x)}=x\mathbin{\&}(x-1).$$ Wegner introduced this rightmost-one clearing step to count binary ones [@Wegner1960]; its iteration count is the binary digit sum. We do not claim that specialization or identity. Our residual contribution is the general-prime standard-representative dynamics, its full transient polynomial and parameter recovery, and the contrast between universally blind periodic data and a rigid transient profile. A bounded search did not locate that combined general-$p$ dynamical package; this is not a priority certification.

There is also a deliberate internal distinction from earlier work on digit-weight automatic orbit closures. Here the phase space is the finite local ring itself, time is an absorbing arithmetic update, and the invariant is the entire hitting-time profile. No countable subshift, cellular endomorphism monoid, or Cantor--Bendixson analysis is used.

# The erasure map and its digit normal form

Fix a prime $p$ and an integer $r\geq1$. We use the standard representatives $0,1,\ldots,p^r-1$ of $R_{p,r}=\mathbb Z/p^r\mathbb Z$. For nonzero $x$, let $v_p(x)$ be the largest $j$ for which $p^j$ divides $x$. Thus the choice of standard representative is part of the definition; no representative-independent ring operation is being asserted.

The *least-valuation digit erasure map* is $$E_{p,r}(0)=0,
 \qquad
 E_{p,r}(x)=x-p^{v_p(x)}\quad (x\ne0).$$ Its absorption time is $$\tau_{p,r}(x)=\min\{t\geq0:E_{p,r}^t(x)=0\}.$$

Write the unique base-$p$ expansion $$x=\sum_{j=0}^{r-1}a_jp^j,
 \qquad 0\leq a_j\leq p-1,$$ and put $s_p(x)=\sum_ja_j$.

[\[lem:normal\]]{#lem:normal label="lem:normal"} If $x\ne0$ and $j=\min\{i:a_i>0\}$, then $E_{p,r}$ replaces $a_j$ by $a_j-1$ and leaves every other digit unchanged. In particular, $$s_p(E_{p,r}x)=s_p(x)-1.$$

The digits below $j$ vanish, so $v_p(x)=j$. Subtracting $p^j$ decreases the $j$th digit by one and produces neither a borrow nor a carry. The assertion about the digit sum follows immediately.

The choice of the *least* nonzero digit is essential. It makes the map triangular in digit coordinates; subtracting the highest nonzero place would generally create a different ordered traversal, while subtracting an arbitrary $p$-power can require a state-dependent convention.

[\[thm:hitting\]]{#thm:hitting label="thm:hitting"} For every $x\in R_{p,r}$, $$\tau_{p,r}(x)=s_p(x),
 \qquad
 \tau_{p,r}(E_{p,r}^t x)=\max\{s_p(x)-t,0\}.$$ The unique recurrent point is $0$, and the sharp global absorption depth is $$D_{p,r}=(p-1)r.$$ The unique state at this maximum depth is $p^r-1$.

By [\[lem:normal\]](#lem:normal){reference-type="ref" reference="lem:normal"}, every nonzero iterate lowers the nonnegative integer $s_p$ by exactly one. It therefore takes exactly $s_p(x)$ steps to reach digit sum zero, which is equivalent to reaching $0$. This also proves the iterate formula and rules out nontrivial recurrence. The digit sum is at most $(p-1)r$, with equality exactly when every digit is $p-1$.

# The full transient profile

Let $$N_{p,r}(k)=\#\{x\in R_{p,r}:\tau_{p,r}(x)=k\}$$ and call $$H_{p,r}(u)=\sum_{k\geq0}N_{p,r}(k)u^k$$ the transient-depth polynomial.

[\[thm:profile\]]{#thm:profile label="thm:profile"} One has $$\boxed{H_{p,r}(u)=(1+u+\cdots+u^{p-1})^r.}$$ For $0\leq k\leq(p-1)r$, $$\boxed{
 N_{p,r}(k)=
 \sum_{j=0}^{\lfloor k/p\rfloor}
 (-1)^j\binom rj\binom{k-pj+r-1}{r-1},}$$ where a binomial coefficient with an inadmissible lower argument is zero. The sequence $k\mapsto N_{p,r}(k)$ is symmetric and unimodal.

The bijection from ring elements to their $r$ digits, together with [\[thm:hitting\]](#thm:hitting){reference-type="ref" reference="thm:hitting"}, gives $$H_{p,r}(u)=
 \prod_{j=0}^{r-1}\sum_{a=0}^{p-1}u^a.$$ Using $(1+\cdots+u^{p-1})^r=(1-u^p)^r(1-u)^{-r}$ and extracting the $u^k$ coefficient gives the displayed inclusion--exclusion formula.

Symmetry follows by complementing every digit, $a_j\mapsto p-1-a_j$. For unimodality, induct on $r$, the case $r=1$ being immediate. If $c_r(k)$ denotes the coefficient at level $r$, extended by zero outside $0\leq k\leq(p-1)r$, then $$c_{r+1}(k)-c_{r+1}(k-1)=c_r(k)-c_r(k-p).$$ Put $C_r=(p-1)r/2$. If the integer $k\leq C_{r+1}$, then $k\leq C_r+p/2$, and hence $|k-C_r|\leq|k-p-C_r|$. Symmetry and the inductive monotonicity toward $C_r$ therefore give $c_r(k)\geq c_r(k-p)$, so the displayed difference is nonnegative. Symmetry supplies the nonpositive differences after the centre and also covers an integral or half-integral centre.

The polynomial contains more information than merely the maximal depth. In fact, it is a complete parameter fingerprint.

[\[cor:rigidity\]]{#cor:rigidity label="cor:rigidity"} If $H_{p,r}=H_{q,s}$ for primes $p,q$ and positive integers $r,s$, then $(p,r)=(q,s)$. More explicitly, $$r=[u]H_{p,r}(u),
 \qquad
 p=1+\frac{\deg H_{p,r}}{[u]H_{p,r}(u)}.$$

The coefficient of $u$ counts digit vectors with one unit digit and is $r$. The degree is $(p-1)r$, which then recovers $p$.

# Exact laws and asymptotics from a uniform state

Let $X_{p,r}$ be uniform on $R_{p,r}$. Its digits are independent and uniform on $\{0,\ldots,p-1\}$. Thus the dynamical hitting time is exactly a sum of iid bounded lattice variables.

[\[prop:moments\]]{#prop:moments label="prop:moments"} For real $\theta$, $$\mathbb Ee^{\theta\tau_{p,r}(X_{p,r})}
 =\left(\frac{1+e^\theta+\cdots+e^{(p-1)\theta}}p\right)^r.$$ Moreover, $$\boxed{\mathbb E\tau_{p,r}=\frac{r(p-1)}2,\qquad
 \operatorname{Var}(\tau_{p,r})=\frac{r(p^2-1)}{12}.}$$

Apply [\[thm:hitting\]](#thm:hitting){reference-type="ref" reference="thm:hitting"} and multiply the moment generating functions of the $r$ independent uniform digits. A single such digit has mean $(p-1)/2$ and variance $(p^2-1)/12$.

Put $\mu_{p,r}=r(p-1)/2$ and $\sigma_{p,r}^2=r(p^2-1)/12$.

[\[thm:limits\]]{#thm:limits label="thm:limits"} Fix $p$ and let $r\to\infty$. Then $$\frac{\tau_{p,r}(X_{p,r})-\mu_{p,r}}{\sigma_{p,r}}
 \Longrightarrow \mathcal N(0,1).$$ In addition, the span-one lattice local limit holds uniformly in $k\in\mathbb Z$: $$\sup_{k\in\mathbb Z}\left|
 \sigma_{p,r}\frac{N_{p,r}(k)}{p^r}
 -\frac1{\sqrt{2\pi}}
 \exp\!\left(-\frac{(k-\mu_{p,r})^2}{2\sigma_{p,r}^2}\right)
 \right|\longrightarrow0.$$

By [\[thm:hitting\]](#thm:hitting){reference-type="ref" reference="thm:hitting"}, the centered hitting time is a sum of iid bounded nondegenerate variables, so the classical central limit theorem applies. The digit distribution has maximal lattice span one and finite moments of all orders. The standard iid lattice local limit theorem therefore gives the uniform statement in the displayed normalization [@Petrov1975 Chapter VII]. The contribution specific to the present system is the exact identification of that sum with the hitting time.

The fixed-$p$ hypothesis in [\[thm:limits\]](#thm:limits){reference-type="ref" reference="thm:limits"} is part of the statement. Joint regimes in which $p$ varies with $r$ require a triangular-array formulation and are not claimed here.

# Periodic blindness

For a self-map $F$ of a finite set, write $\operatorname{Fix}_n(F)=\#\{x:F^n(x)=x\}$. The Artin--Mazur zeta is [@ArtinMazur1965] $$\zeta_F(z)=\exp\left(\sum_{n\geq1}\frac{\operatorname{Fix}_n(F)}n z^n\right).$$ We use this as an identity in $\mathbb Q[[z]]$.

For every prime $p$, every $r\geq1$, and every $n\geq1$, $$\operatorname{Fix}_n(E_{p,r})=1,
 \qquad
 \zeta_{E_{p,r}}(z)=\frac1{1-z}.$$ Thus periodic counts and zeta distinguish no two members of the family, while the transient-depth polynomial distinguishes all of them by [\[cor:rigidity\]](#cor:rigidity){reference-type="ref" reference="cor:rigidity"}.

Theorem [\[thm:hitting\]](#thm:hitting){reference-type="ref" reference="thm:hitting"} shows that every nonzero state strictly decreases its digit sum until it reaches zero. Hence only zero can be fixed by an iterate. Substitution of $\operatorname{Fix}_n=1$ into the defining exponential gives $\exp(\sum_{n\ge1}z^n/n)=(1-z)^{-1}$.

This contrast is the main dynamical point of the example. Adding a restart edge at zero would manufacture a nontrivial cycle but obscure the canonical absorbing map, so we do not do so.

# Exact controls and limitations

The accompanying deterministic program follows every arithmetic orbit in five registered parameter lanes and builds the resulting depth histogram. It cross-checks that exhaustive histogram against an independently convolved coefficient vector and the inclusion--exclusion formula, then verifies symmetry, unimodality, exact rational moments, nilpotency depth, fixed data, and parameter recovery. The frozen run contains $46{,}319{,}420$ exact assertions. These finite checks guard conventions and endpoints; the proofs above establish the infinite family.

The present result is deliberately narrow. It does not assert a new theorem about the classical sum-of-digits distribution or its local limits, does not classify arbitrary digit-decrement rules, and does not infer global novelty from a bounded literature search. In particular it does not re-claim Wegner's binary clearing step or popcount identity. Public release and priority language remain on hold pending specialist review.
