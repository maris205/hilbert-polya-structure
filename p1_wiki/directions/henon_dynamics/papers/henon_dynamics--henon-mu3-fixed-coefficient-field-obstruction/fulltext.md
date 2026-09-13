---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-fixed-coefficient-field-obstruction"
canonical_tex: "henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction/paper/main.pdf"
source_sha256: "975cdbc8c25f5186fa26a530d8f6292c41d0c9b83359ae8ed698b8fc988e4868"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Unbounded Cyclotomic Trace Fields in a Quantized Hénon Kernel

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_fixed_coefficient_field_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the first conjugate-paired arithmetic moment of the homogeneous area-preserving Hénon kernel over finite fields. For every prime $p\equiv1\pmod 3$, we prove that this moment generates the maximal real cyclotomic field $\mathbf Q(\zeta_p)^+$ and therefore has degree $(p-1)/2$ over $\mathbf Q$. The proof is uniform in $p$: Galois invariance is converted into a scaling symmetry of an exact value histogram, and two nonzero finite-field power moments force its stabilizer to be $\{\pm1\}$. It follows that the paired Hénon moments cannot be Frobenius traces of a compatible system over one fixed number field that realizes these exact moments. The obstruction occurs before rank, conductor, purity, or a functional equation can be imposed. We also prove that the canonical additive Galois descent collapses to the universal value $-6$. Thus conjugate pairing repairs local real type but does not provide the fixed arithmetic coefficient field needed for a global Hilbert--Pólya candidate.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: 13 August 2026
title: Unbounded Cyclotomic Trace Fields in a Quantized Hénon Kernel
```

## Markdown 正文

# Introduction

A credible arithmetic dynamical determinant should not merely have local unitary matrices. Its local traces must assemble in a coefficient field and normalization that are independent of the place. Compatible systems make this requirement precise: one fixes a number field and a common finite rank, and the unramified Frobenius polynomials have coefficients in that field independently of the auxiliary realization [@Hui2025; @Thorne2023]. Boundedness of Frobenius trace fields is itself a meaningful geometric-origin condition [@KrishnamoorthyLam2026].

The preceding Hénon construction supplies, for every split prime $p\equiv1\pmod3$, a unitary Fourier--cubic quantization $U_p$ and a non-scalar order-three permutation $R_p$. The two-step operator $T_p=U_p^2$ preserves the three $R_p$-grades, and the augmentation determinant retains exact twisted Hénon chronology. Pairing the additive character with its inverse is the source-native repair tested here for the raw local failure of real type. The resulting first moment is real, but it need not be rational.

Our main result shows that it is as far from rational as possible inside the $p$th cyclotomic field.

[\[thm:main\]]{#thm:main label="thm:main"} For every prime $p>3$ with $p\equiv1\pmod3$, the conjugate-paired first Hénon augmentation moment $B_{p,1}$ satisfies $$\mathbf Q(B_{p,1})=\mathbf Q(\zeta_p)^+,
 \qquad
 [\mathbf Q(B_{p,1}):\mathbf Q]=\frac{p-1}{2}.$$ Consequently no fixed number field contains all $B_{p,1}$, and no fixed-coefficient-field compatible system can realize these moments as its Frobenius traces.

The proof does not extrapolate from a prime scan. It converts the Galois stabilizer into a finite-field histogram stabilizer and detects that stabilizer using two closed-form power moments. The same argument covers every split prime, with a short separate check at $p=7$.

There are still Galois-invariant rational descents. Trace and norm are the two minimal operations tested next, not an exhaustive list. The additive trace is unexpectedly rigid: $$\operatorname{Tr}_{\mathbf Q(\zeta_p)^+/\mathbf Q}B_{p,1}=-6.$$ This exact collapse motivates the successor problem: apply the multiplicative norm to the full local determinant and determine whether rational descent creates a bounded object or merely hides growing divisor complexity.

The conclusion is deliberately scoped. The conjugate-paired Euler germ and finite-place quantization remain valid. What fails is their promotion to a fixed-field global arithmetic object. No statement about the Riemann Hypothesis follows.

# The chronological paired moment

Let $p>3$ be prime with $p\equiv1\pmod3$. Choose $\rho\in\mathbf F_p^\times$ of order three and write $$c=1+\rho=-\rho^2,
 \qquad
 f_p(x,y)=2x^3+2y^3+cxy.$$ Let $\zeta_p=\exp(2\pi i/p)$ and let $$U_p(Q,q)=p^{-1/2}\zeta_p^{qQ+2q^3},
 \qquad
 (R_pv)(x)=v(\rho x).$$ The reversing relation $U_pR_p=R_p^{-1}U_p$ implies that $T_p=U_p^2$ commutes with $R_p$. The first augmentation moment is $$A_{p,1}(\psi)=\operatorname{Tr}((R_p+R_p^2)U_p^2).$$

For $j=1,2$, direct chronological kernel composition gives $$\operatorname{Tr}(R_p^jU_p^2)
 =\frac1p\sum_{x,y\in\mathbf F_p}
   \zeta_p^{2x^3+2y^3+(1+\rho^j)xy}. \tag{2.1}$$ The two phase histograms coincide: substituting $x\mapsto\rho^2x$ in the $j=1$ phase produces the $j=2$ phase. Define $$N_p(r)=\#\{(x,y)\in\mathbf F_p^2:f_p(x,y)=r\},
 \qquad
 H_p(r)=N_p(r)+N_p(-r).$$ Equation (2.1) and its complex conjugate yield the exact paired moment $$\label{eq:B}
 B_{p,1}
 =A_{p,1}(\psi)+A_{p,1}(\psi^{-1})
 =\frac2p\sum_{r\in\mathbf F_p}H_p(r)\zeta_p^r.$$

The factor $p^{-1}$ is supplied by two genuine Hénon steps; no formal square-root Tate twist remains. At a split prime $\mathfrak p$ of $\mathbf Q(\rho)$ the clock is $\log\operatorname{N}\mathfrak p=\log p$. Neither the character pairing nor the value histogram replaces chronological products by an averaged transition matrix.

Since $H_p(-r)=H_p(r)$, the moment in [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} is real and belongs to $\mathbf Q(\zeta_p)^+$. The problem is to determine whether it lies in a smaller field uniformly in $p$.

# The two-moment stabilizer theorem

Let $K_p=\mathbf Q(\zeta_p)$. For $a\in\mathbf F_p^\times$, write $\sigma_a(\zeta_p)=\zeta_p^a$.

[\[lem:dictionary\]]{#lem:dictionary label="lem:dictionary"} One has $$\sigma_a(B_{p,1})=B_{p,1}
 \quad\Longleftrightarrow\quad
 H_p(ar)=H_p(r)\quad\text{for all }r\in\mathbf F_p.$$

After relabeling, the coefficient vector of $\sigma_a(B_{p,1})-B_{p,1}$ is $H_p(a^{-1}r)-H_p(r)$. A rational polynomial of degree at most $p-1$ that vanishes at $\zeta_p$ is a scalar multiple of $\Phi_p(X)=1+X+\cdots+X^{p-1}$. The coefficient sum is zero because both histograms have total mass $2p^2$. The scalar is therefore zero. The converse is immediate.

Write $p-1=3m$. Since $p\equiv1\pmod6$, $m$ is even. For even $k$, define $$M_k=\sum_{r\in\mathbf F_p}r^kH_p(r)
     =2\sum_{x,y\in\mathbf F_p}f_p(x,y)^k\quad\text{in }\mathbf F_p.$$

[\[prop:moments\]]{#prop:moments label="prop:moments"} For every split prime, $$M_{2m}=2\binom{2m}{m}4^m\ne0\pmod p.$$ For $p\ge13$, $$M_{2m+2}
 =2\frac{(2m+2)!}{(m-2)!^2\,6!}
   2^{2m-4}c^6\ne0\pmod p.$$

The proof is given in [7](#sec:proofs){reference-type="ref" reference="sec:proofs"}. Its key feature is uniqueness: at each exponent, precisely one multinomial term survives finite-field monomial orthogonality.

[\[thm:stabilizer\]]{#thm:stabilizer label="thm:stabilizer"} For every prime $p\equiv1\pmod3$, $$\operatorname{Stab}(H_p)=\{a\in\mathbf F_p^\times:H_p(ar)=H_p(r)\ \forall r\}
             =\{\pm1\}.$$

If $a$ stabilizes $H_p$, then a change of variables in $M_k$ gives $(a^k-1)M_k=0$. For $p\ge13$, [\[prop:moments\]](#prop:moments){reference-type="ref" reference="prop:moments"} implies $a^{2m}=a^{2m+2}=1$, hence $a^2=1$. At $p=7$, the first formula gives $M_4=3\ne0$, while every $a\in\mathbf F_7^\times$ satisfies $a^6=1$; again $a^2=1$. Conversely, $H_p$ is even, so both signs stabilize it.

# Maximal real trace fields

By [\[lem:dictionary,thm:stabilizer\]](#lem:dictionary,thm:stabilizer){reference-type="ref" reference="lem:dictionary,thm:stabilizer"}, the stabilizer of $B_{p,1}$ in $\operatorname{Gal}(K_p/\mathbf Q)\cong\mathbf F_p^\times$ is $\{\pm1\}$. Its fixed field is exactly the maximal real cyclotomic field. Hence $$\mathbf Q(B_{p,1})=K_p^{\{\pm1\}}=\mathbf Q(\zeta_p)^+,
 \qquad
 [\mathbf Q(B_{p,1}):\mathbf Q]=\frac{p-1}{2}.$$

There are infinitely many primes congruent to one modulo three. For completeness, suppose $q_1,\ldots,q_t$ were all of them, let $n=3q_1\cdots q_t$, and take a prime divisor $r$ of $n^2+n+1$. It is neither $3$ nor one of the $q_i$, and $n$ has exact order three modulo $r$. Thus $r\equiv1\pmod3$, a contradiction. The degrees above are therefore unbounded.

If one fixed number field $E$ contained all $B_{p,1}$, their degrees would be bounded by $[E:\mathbf Q]$. This proves the compatible-system obstruction. The same conclusion holds if a different complex embedding of $E$, or a different Galois conjugate of $B_{p,1}$, is selected at each prime: every such conjugate still has degree $(p-1)/2$ over $\mathbf Q$.

The conclusion is stronger than failure over $\mathbf Q(\rho)$ or over a chosen CM field. It rules out every fixed finite coefficient field. Allowing the field to grow with $p$ is mathematically possible, but it is precisely the condition that a conventional fixed-$E$ compatible system is designed to avoid. The statement concerns a compatible system whose frozen Frobenius traces are the exact moments $B_{p,1}$; it does not classify invariant descent procedures.

The theorem also clarifies the role of finite controls. A prime ledger can detect the degrees $3,6,9,15,18,21,30,33,36$ at the split primes through $73$, but those data do not prove unboundedness. The two-moment theorem supplies the all-prime bridge.

# What survives rational descent?

The trace-field obstruction leaves several possible invariant constructions. Galois trace and Galois norm are the two minimal descents tested here; they do not exhaust restriction of scalars or other invariant constructions. The first can be computed exactly.

[\[prop:trace\]]{#prop:trace label="prop:trace"} For every prime $p\equiv1\pmod3$, $$N_p(0)=p-3,
 \qquad
 \operatorname{Tr}_{\mathbf Q(\zeta_p)^+/\mathbf Q}B_{p,1}=-6.$$

If $xy=0$ and $f_p(x,y)=0$, then $(x,y)=(0,0)$. For $xy\ne0$, put $t=x/y$. The equation becomes $$y=-\frac{ct}{2(t^3+1)}.$$ There is one nonzero solution for each $t\in\mathbf F_p^\times$ except the three roots $-1,-\rho,-\rho^2$ of $t^3=-1$. Thus $N_p(0)=1+(p-1-3)=p-3$.

For $r\ne0$, $\operatorname{Tr}_{K_p/\mathbf Q}(\zeta_p^r)=-1$, while the trace of $1$ is $p-1$. Using [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"}, total mass $\sum_rH_p(r)=2p^2$, and $H_p(0)=2N_p(0)$ gives $$\operatorname{Tr}_{K_p/\mathbf Q}B_{p,1}=2\bigl(H_p(0)-2p\bigr).$$ Because $B_{p,1}$ lies in the real subfield and $[K_p:K_p^+]=2$, division by two yields the result.

Thus additive descent is canonical but erases the maximal trace field into a universal Tate-like first coefficient. It does not follow that the full chronological sequence collapses. The multiplicative successor is the Galois norm of the complete conjugate-paired local determinant. Its logarithm contains the rational traces of every ordered Hénon moment, so it preserves chronology before summing over embeddings.

The next gate is therefore sharp: either the norm has a bounded-degree realization after removing only certified universal modes, or rationality is obtained at the price of growing local divisor complexity. Fractional roots, prime-dependent fields, and fitted cancellations are not admissible normalizations.

# Exact controls and Route-A decision

The released computation reconstructs $N_p$ and $H_p$ over every split prime in a frozen range, verifies both moment formulas, computes the stabilizer, and checks the zero-fiber and trace identities. These controls test conventions and implementation; the theorem itself is symbolic and all-prime. An independent checker rebuilds the arithmetic without importing the producer, and type-strict mutations are rejected.

The relation to prior work is narrow. Classical compatible-system theory supplies the fixed-field criterion [@Hui2025]; cyclotomic and finite-field identities are used directly. Earlier project stages ruled out functorial scalar cubic Kummer decorations, bare fixed three-channel products, external Schatten clocks, and finite CM--Tate repairs. The present theorem concerns the surviving non-scalar full Hénon kernel and is not a reformulation of those obstructions.

Under the Route-A rubric, the paired object inherits exact finite-field chronology, a nonzero Euler germ on $\operatorname{Re}s>1$, and a natural two-step unitary quantization. It still does not identify primes with primitive orbits of one real map, and it has no global functional equation or fixed-field arithmetic completion. The frozen verdict is $$\begin{aligned}
 \mathrm{A1}&=\mathrm{WEAK},
 &\mathrm{A2}&=\mathrm{ANALYTIC\_DETERMINANT},\\
 \mathrm{A3}&=\mathrm{FAIL},
 &\mathrm{A4}&=\mathrm{NATURAL\_QUANTIZATION}.\end{aligned}$$ Overall, the fixed-coefficient-field promotion is rejected. Route B is not authorized.

The result is nevertheless a substantial pruning theorem: the failure occurs at the first moment for every split prime, so neither longer orbit scans nor larger local matrices can rescue the same compatible-system hypothesis.

# Finite-field moment calculation {#sec:proofs}

We prove [\[prop:moments\]](#prop:moments){reference-type="ref" reference="prop:moments"}. In $\mathbf F_p$, $$\sum_{t\in\mathbf F_p}t^e=
 \begin{cases}
 -1,&e>0\text{ and }(p-1)\mid e,\\
 0,&\text{otherwise}.
 \end{cases}$$ Expand $f_p(x,y)^k$ and let $(\alpha,\beta,\delta)$ record the multiplicities of $2x^3$, $2y^3$, and $cxy$. A term survives summation only if $$3\alpha+\delta>0,\quad3\beta+\delta>0,
 \quad
 3m\mid(3\alpha+\delta),\quad
 3m\mid(3\beta+\delta).$$

For $k=2m$, the sum of the two variable exponents is $6m-\delta\le6m$. Both must therefore equal $3m$, which forces $\delta=0$ and $\alpha=\beta=m$. The two monomial sums each contribute $-1$, so their product has positive sign. Multiplying by the even-histogram factor two gives $$M_{2m}=2\frac{(2m)!}{m!m!}2^{2m}.$$ Since $2m<p$, this is nonzero modulo $p$.

For $k=2m+2$ and $m\ge4$, the exponent sum is $6m+6-\delta<9m$. The only possible positive-multiple sum is $6m$. Consequently $\delta=6$, both variable exponents equal $3m$, and $\alpha=\beta=m-2$. This yields $$M_{2m+2}
 =2\frac{(2m+2)!}{(m-2)!^2 6!}2^{2m-4}c^6.$$ All factorial arguments are smaller than $p$, and $c=-\rho^2\ne0$, proving nonvanishing.
