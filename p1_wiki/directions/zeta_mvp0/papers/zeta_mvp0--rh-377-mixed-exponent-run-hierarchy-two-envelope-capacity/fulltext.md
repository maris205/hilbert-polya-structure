---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-377-mixed-exponent-run-hierarchy-two-envelope-capacity"
canonical_tex: "zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity/main.pdf"
source_sha256: "35a3d2b9eecede4f526490dc184b24e5530762933922962df04c3436e2d39433"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Mixed-exponent Möbius run hierarchies and the two-envelope capacity boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-377-mixed-exponent-run-hierarchy-two-envelope-capacity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The exact RH-371 distance-two capacity uses sixteen overlapping signed-run counts, two signs at each length $1\le k\le8$. We expand every count on its native odd-start endpoint into mixed Möbius exponents. If $H_{k,r}$ is the sum of all terms with $r$ first powers and $k-r$ square masks, and $A_k,B_k$ collect the layers $r\ge2$ of even and odd parity, then $$2^kC_{\sigma,k}=H_{k,0}+A_k+
   \sigma(H_{k,1}+B_k).$$ We prove unconditionally that $H_{k,0}/N\to\Delta_k=\frac12\prod_{p\ \mathrm{odd}}(1-k/p^2)$ and $H_{k,1}=o(N)$. The latter argument uses bounded periodic prime-square masks at fixed cutoff, fixed-progression Davenport cancellation, and only then a large-prime-square union bound. Consequently all sixteen densities exist simultaneously exactly when thirteen aggregate limits exist: $A_k/N$ for $2\le k\le8$ and $B_k/N$ for $3\le k\le8$. The associated formal $466$-coordinate block map has rank $13$ and kernel dimension $453$. This is not an arithmetic minimality theorem. For the adaptive capacity we obtain $$K_N/N=2r_0+2\{U_N+|V_N|\}/N+o(1),$$ so convergence is equivalent to one two-envelope limit. Full mixed-exponent cancellation is sufficient, but not necessary, for the displayed conditional Euler-product constant. A self-contained stationary ternary chain shows that raw, square-only, and one-sign masked moments do not algebraically determine the first directional two-sign masked moment. The chain is synthetic and not Möbius. No capacity limit, operator, trace formula, zero identification, Hilbert--Polya construction, or proof of RH is claimed.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: 'Mixed-exponent Möbius run hierarchies and the two-envelope capacity boundary'
```

## Markdown 正文

# Native endpoints and mixed-exponent coordinates

The frozen RH-371 reduction writes the distance-two adaptive capacity in terms of signed intervals at lengths at most eight [@RH371]. For $I_k=\{0,\ldots,k-1\}$ set $$\mathcal D_k(N)=
 \{n\in\mathbb Z:1\le n\le N-2(k-1),\ n\text{ odd}\}.
 \label{eq:domain}$$ Every object at level $k$ below uses exactly this endpoint. Empty domains give zero. For $S\subseteq I_k$, define $$T_{k,S}(N)=\sum_{n\in\mathcal D_k(N)}
 \prod_{j\in S}\mu(n+2j)
 \prod_{j\in I_k\setminus S}\mu(n+2j)^2,
 \qquad
 H_{k,r}(N)=\sum_{\substack{S\subseteq I_k\\|S|=r}}T_{k,S}(N).
 \label{eq:mixed-moments}$$ The signed interval count is $$C_{\sigma,k}(N)=\#\{n\in\mathcal D_k(N):
       \mu(n)=\cdots=\mu(n+2(k-1))=\sigma\},
 \quad \sigma\in\{-1,+1\}.
 \label{eq:run-count}$$ These are overlapping same-sign windows. They are not counts of maximal runs or runs having exact length $k$.

Separate the higher mixed layers by parity: $$A_k=\sum_{\substack{2\le r\le k\\r\ \mathrm{even}}}H_{k,r},
 \qquad
 B_k=\sum_{\substack{3\le r\le k\\r\ \mathrm{odd}}}H_{k,r}.
 \label{eq:AB}$$ Thus $A_1=B_1=B_2=0$. The first nonzero aggregate is $A_2=T_{2,\{0,1\}}$, the ordinary shift-two correlation on the odd-start endpoint isolated in RH-376 [@RH376].

For every $N\ge1$, $1\le k\le8$, and $\sigma\in\{-1,+1\}$, $$\boxed{\displaystyle
 2^kC_{\sigma,k}=H_{k,0}+A_k+
                  \sigma\bigl(H_{k,1}+B_k\bigr).}
 \label{eq:master}$$

For $x\in\{-1,0,1\}$, $2\mathbf 1_{\{x=\sigma\}}=x^2+\sigma x$. Hence, pointwise in $n\in\mathcal D_k(N)$, $$2^k\prod_{j\in I_k}\mathbf 1_{\{\mu(n+2j)=\sigma\}}
 =\prod_{j\in I_k}\bigl(\mu(n+2j)^2+\sigma\mu(n+2j)\bigr).$$ Expansion over $S\subseteq I_k$, followed by $\sigma^{|S|}=1$ for even $|S|$ and $\sigma$ for odd $|S|$, gives [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"} after summation. No endpoint extension or probabilistic assumption occurs.

# The two deterministic layers

Put $$e_k=\prod_{p\ \mathrm{odd}}\left(1-\frac{k}{p^2}\right),
 \qquad \Delta_k=\frac{e_k}{2},
 \qquad 1\le k\le8.
 \label{eq:delta}$$ The product is only over odd primes. The factor $1/2$ outside the product is exactly the odd-start condition. No $p=2$ local factor is inserted into $e_k$.

For each fixed $1\le k\le8$, $$\frac{H_{k,0}(N)}{N}\longrightarrow\Delta_k,
 \qquad H_{k,1}(N)=o(N).
 \label{eq:H01}$$

For $H_{k,0}$, the summand is the indicator that all $k$ odd integers $n,n+2,\ldots,n+2(k-1)$ are squarefree. Fix a prime cutoff $R$. For an odd prime $p$, the $k$ shifts occupy distinct classes modulo $p^2$: if $2(j-\ell)\equiv0\pmod{p^2}$, then $p^2\mid j-\ell$, which is impossible for $0<|j-\ell|\le7<p^2$. The Chinese remainder theorem therefore gives the finite-sieve density $$\frac12\prod_{\substack{p\le R\\p\ \mathrm{odd}}}
 \left(1-\frac{k}{p^2}\right).$$ An accepted start omitted by the true squarefree condition has $p^2\mid n+2j$ for some $j\in I_k$ and odd prime $p>R$. The union bound is $$O_k\!\left(N\sum_{p>R}\frac1{p^2}+\sqrt N\right)
 =O_k(N/R+\sqrt N).$$ First send $N\to\infty$ at fixed $R$ and then $R\to\infty$. This proves the first limit, in the classical squarefree-pattern framework [@Mirsky1948].

For the second assertion, fix $j\in I_k$ and write the corresponding term of $H_{k,1}$ as $$\sum_{n\in\mathcal D_k(N)}\mu(n+2j)
       \prod_{\ell\ne j}\mu(n+2\ell)^2.
 \label{eq:one-sign-term}$$ For a fixed cutoff $R$, let $$g_R(m)=\mathbf 1_{\{p^2\nmid m\text{ for every prime }p\le R\}}.$$ Replace each square mask in [\[eq:one-sign-term\]](#eq:one-sign-term){reference-type="eqref" reference="eq:one-sign-term"} by $g_R$. The product of these masks and the odd-start indicator is a bounded periodic function with a fixed period depending only on $R$ and $k$. Expanding it into its finitely many residue classes turns the truncated sum, after translating $m=n+2j$, into finitely many fixed-progressions sums of $\mu(m)$. Each is $o(N)$ by Davenport's fixed-frequency theorem and finite Fourier inversion [@Davenport1937].

The true and truncated products can differ only if, for some $\ell\ne j$, a prime $p>R$ satisfies $p^2\mid n+2\ell$. Because the masks are bounded by one, another union bound gives $$O_k\!\left(N\sum_{p>R}\frac1{p^2}+\sqrt N\right)
 =O_k(N/R+\sqrt N).$$ There are only $k$ possible sign positions. Divide by $N$, take $N\to\infty$ with $R$ fixed, and then take $R\to\infty$ to obtain $H_{k,1}=o(N)$.

The one-sign proof uses bounded periodic $0/1$ masks. It does not expand several unrestricted divisor sums and does not apply Davenport to a modulus growing with $N$. The order is fixed $R$, then $N\to\infty$, then $R\to\infty$.

For $k=2$, $e_2/2=\prod_p(1-2/p^2)$, because the missing $p=2$ factor of the full product is $1/2$. Thus the $k=2$ specialization agrees exactly with the RH-376 squarefree-pair normalization.

# Thirteen aggregate density channels

Dividing [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"} by $N$ and using [\[eq:H01\]](#eq:H01){reference-type="eqref" reference="eq:H01"} gives $$\frac{2^kC_{\sigma,k}(N)}N
 =\Delta_k+\frac{A_k(N)}N+\sigma\frac{B_k(N)}N+o(1).
 \label{eq:density-reduction}$$

All sixteen limits $$\lim_{N\to\infty}C_{\sigma,k}(N)/N,
 \qquad \sigma\in\{-1,+1\},\quad1\le k\le8,$$ exist if and only if all thirteen limits $$\lim_{N\to\infty}A_k(N)/N\quad(2\le k\le8),
 \qquad
 \lim_{N\to\infty}B_k(N)/N\quad(3\le k\le8)
 \label{eq:thirteen}$$ exist.

If the limits in [\[eq:thirteen\]](#eq:thirteen){reference-type="eqref" reference="eq:thirteen"} exist, equation [\[eq:density-reduction\]](#eq:density-reduction){reference-type="eqref" reference="eq:density-reduction"} gives all sixteen signed limits. Conversely, for each $k\ge3$, adding the $\sigma=+1$ and $\sigma=-1$ equations recovers $A_k/N$ up to a convergent deterministic term and $o(1)$. Subtracting them recovers $B_k/N+o(1)$. At $k=2$, $B_2=0$, so either signed equation recovers $A_2/N$. At $k=1$ there is no higher aggregate. This yields exactly seven $A$ limits and six $B$ limits.

For a fixed $k\ge3$, convergence for only one sign controls the single combination $(A_k+\sigma B_k)/N$. It need not give separate convergence of $A_k/N$ and $B_k/N$.

There are $$\sum_{k=2}^8(2^k-1-k)=466
 \label{eq:466}$$ formal coordinates $T_{k,S}$ with $|S|\ge2$. Consider the purely formal linear map that sums even-cardinality coordinates into $A_k$ and odd-cardinality coordinates into $B_k$. Its thirteen row supports are pairwise disjoint and nonempty. Their sizes are $$(1,3,7,15,31,63,127)\quad\text{and}\quad
 (1,4,11,26,57,120).$$ Hence the map has rank $13$ and kernel dimension $466-13=453$. This count treats the coordinates as formal independent variables. It does not prove that thirteen is the minimal number of actual Möbius correlation limits, nor does it identify arithmetic relations among those limits.

# Exact two-envelope capacity reduction

Let $E_\sigma(N)$ be the isolated even-path count from RH-371 and set $$s_k=(-1)^{k+1},\qquad
 R_\sigma(N)=E_\sigma(N)+\sum_{k=1}^8s_kC_{\sigma,k}(N).
 \label{eq:R}$$ The locked path formula identifies $R_\sigma$ with a nonnegative maximum-weight independent-set value and gives $$K_N=\max\{|{-M_N+2R_+(N)}|,|{-M_N-2R_-(N)}|\},
 \qquad M_N=\sum_{n\le N}\mu(n).
 \label{eq:K-exact}$$

Define four exact finite channels $$\begin{aligned}
 P_N&=\frac{E_+(N)+E_-(N)}2+
       \sum_{k=1}^8\frac{s_kH_{k,0}(N)}{2^k},
 &Q_N&=\frac{E_+(N)-E_-(N)}2+
       \sum_{k=1}^8\frac{s_kH_{k,1}(N)}{2^k},
 \label{eq:PQ}\\
 U_N&=\sum_{k=2}^8\frac{s_kA_k(N)}{2^k},
 &V_N&=\sum_{k=3}^8\frac{s_kB_k(N)}{2^k}.
 \label{eq:UV}\end{aligned}$$

For every $N$ and $\sigma\in\{-1,+1\}$, $$\begin{aligned}
 R_\sigma&=P_N+U_N+\sigma(Q_N+V_N),
 \label{eq:R-decomposition}\\
 \max(R_+,R_-)&=P_N+U_N+|Q_N+V_N|,
 \label{eq:maxR}\\
 \left|K_N-2\bigl(P_N+U_N+|V_N|\bigr)\right|
 &\le |M_N|+2|Q_N|.
 \label{eq:residual-bound}\end{aligned}$$

Insert [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"} into [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} and group the four types of terms to obtain [\[eq:R-decomposition\]](#eq:R-decomposition){reference-type="eqref" reference="eq:R-decomposition"}. Taking the larger sign gives [\[eq:maxR\]](#eq:maxR){reference-type="eqref" reference="eq:maxR"}. Since $R_\pm\ge0$, equation [\[eq:K-exact\]](#eq:K-exact){reference-type="eqref" reference="eq:K-exact"} and the reverse triangle inequality give $$|K_N-2\max(R_+,R_-)|\le|M_N|.$$ Finally, $\bigl||Q_N+V_N|-|V_N|\bigr|\le|Q_N|$, which proves [\[eq:residual-bound\]](#eq:residual-bound){reference-type="eqref" reference="eq:residual-bound"}.

The fixed-progression squarefree count on $n\equiv2\pmod4$ and Davenport cancellation give $$\frac{E_++E_-}{2N}\longrightarrow\frac1{\pi^2},
 \qquad E_+-E_-=o(N),\qquad M_N=o(N).$$ Indeed, writing $n=2m$ identifies $E_++E_-$ with the number of odd squarefree $m\le N/2$. Their density among all integers is $4/\pi^2$, so $E_++E_-=2N/\pi^2+o(N)$. Moreover, $E_+-E_-=\sum_{n\le N,\ n\equiv2\ (4)}\mu(n)$, while $M_N$ is the corresponding modulus-one sum. Both are $o(N)$ by the same fixed-progression Davenport input. Together with [\[eq:H01\]](#eq:H01){reference-type="eqref" reference="eq:H01"}, these imply $$P_N=r_0N+o(N),\qquad Q_N=o(N),\qquad
 r_0=\frac1{\pi^2}+\sum_{k=1}^8\frac{s_k\Delta_k}{2^k}.
 \label{eq:r0}$$

Unconditionally, $$\begin{aligned}
 R_\sigma(N)&=r_0N+U_N+\sigma V_N+o(N),
 \label{eq:R-asymptotic}\\
 \frac{K_N}{N}&=2r_0+
       2\frac{U_N+|V_N|}{N}+o(1).
 \label{eq:K-asymptotic}\end{aligned}$$ Consequently $K_N/N$ converges if and only if $(U_N+|V_N|)/N$ converges.

Equations [\[eq:R-asymptotic\]](#eq:R-asymptotic){reference-type="eqref" reference="eq:R-asymptotic"} and [\[eq:K-asymptotic\]](#eq:K-asymptotic){reference-type="eqref" reference="eq:K-asymptotic"} follow from [\[eq:R-decomposition\]](#eq:R-decomposition){reference-type="eqref" reference="eq:R-decomposition"}, [\[eq:residual-bound\]](#eq:residual-bound){reference-type="eqref" reference="eq:residual-bound"}, and [\[eq:r0\]](#eq:r0){reference-type="eqref" reference="eq:r0"}. Since $r_0$ is fixed and the remaining error tends to zero, the asserted equivalence follows in both directions.

If every $T_{k,S}(N)=o(N)$ with $|S|\ge2$, then $U_N,V_N=o(N)$ and the conditional capacity limit would be $$\boxed{\displaystyle
 \frac{2}{\pi^2}+\sum_{k=1}^8\frac{(-1)^{k+1}e_k}{2^k}.}
 \label{eq:conditional-constant}$$ This full mixed-exponent cancellation hypothesis is sufficient only. The actual criterion is convergence of one envelope, so cancellation or compensation among aggregates could suffice without every coordinate being $o(N)$. Neither condition is proved here.

# A stationary ternary algebraic boundary

The following witness tests what the low layers can imply by stationarity and ternary algebra alone. It is not an arithmetic model for Möbius.

Fix $0<|\varepsilon|<3/2$. There is a stationary process $(X_t)_{t\in\mathbb Z}$ on $\{-1,0,1\}$ with uniform stationary pair law and second-order transition $$\mathbb P(X_{t+1}=c\mid X_{t-1}=a,X_t=b)
 =\frac13\left[1+\varepsilon ab\left(c^2-\frac23\right)\right].
 \label{eq:transition}$$ It has the following properties.

1.  every nonempty raw moment at distinct times is zero.

2.  every square-only moment at $r$ distinct times equals $(2/3)^r$.

3.  every moment with exactly one first-power factor and otherwise only square masks is zero.

4.  for $A=X_0,B=X_1,C=X_2$, $$\mathbb E[ABC^2]=\frac{8\varepsilon}{81},\qquad
     \mathbb E[AB^2C]=\mathbb E[A^2BC]=0.$$

5.  $\mathbb P(A=B=C=1)=\mathbb P(A=B=C=-1)=
      27^{-1}(1+\varepsilon/3)$.

For $ab\in\{-1,0,1\}$ and $c^2-2/3\in\{-2/3,1/3\}$, the bound on $\varepsilon$ makes every probability in [\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"} positive. Summing over $c$ gives one. If $(A,B)$ is uniform, then for each $(b,c)$ $$\sum_a\frac19\,\mathbb P(c\mid a,b)=\frac19,$$ because $\sum_aa=0$. Hence the uniform pair law is stationary.

Directly from [\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"}, $$\mathbb E[X_{t+1}\mid X_{t-1},X_t]=0,
 \qquad
 \mathbb E[X_{t+1}^2\mid X_{t-1},X_t]
 =\frac23+\frac{2\varepsilon}{9}X_{t-1}X_t.
 \label{eq:conditional-moments}$$ For a raw product at arbitrary distinct times, condition on the history immediately before the latest factor. The first identity in [\[eq:conditional-moments\]](#eq:conditional-moments){reference-type="eqref" reference="eq:conditional-moments"} gives zero. For a square-only product, condition at the latest squared factor. The correction term contains $X_{t-1}X_t$ times earlier squares. Since $x^{2q+1}=x$ on the ternary alphabet, conditioning on the latest of these two first-power factors again annihilates the correction. Induction leaves a factor $2/3$ for each selected time.

The uniform pair law and transition are invariant under the global sign flip $X\mapsto-X$. A monomial with exactly one first power changes sign, proving (iii). The second identity in [\[eq:conditional-moments\]](#eq:conditional-moments){reference-type="eqref" reference="eq:conditional-moments"} gives $$\mathbb E[ABC^2]=\frac{2\varepsilon}{9}\mathbb E[A^2B^2]
 =\frac{2\varepsilon}{9}\left(\frac23\right)^2
 =\frac{8\varepsilon}{81}.$$ The other two directional moments vanish by conditioning on $C$. Finally, the probability of a fixed triple is the uniform pair mass $1/9$ times [\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"}. Substituting $(1,1,1)$ and $(-1,-1,-1)$ proves (v).

At $\varepsilon=1$, the witness gives $\mathbb E[ABC^2]=8/81$ and both same-sign triple probabilities $4/81$. On the odd lattice its one-site nonzero probability is $2/3$, whereas the Möbius odd-lattice density is $e_1=8/\pi^2$. Equivalently, after embedding the chain at odd starts and normalizing by the original $N$, the synthetic contribution is $1/3$, versus $\Delta_1=4/\pi^2$. Thus even its square layer does not match the arithmetic density. The proposition proves only that, in the general stationary ternary class, the directional two-sign masked layer is not forced by raw, square-only, and one-sign masked data. It is neither a Möbius counterexample nor evidence that any Möbius limit fails.

# Executable protocol and frozen rows

The standard-library artifact has four independent components. First, it checks [\[eq:master\]](#eq:master){reference-type="eqref" reference="eq:master"} on all $19680$ ternary-window/sign cases for $1\le k\le8$ and performs exact rational row reduction on the formal $466\to13$ block map. Second, an integer linear sieve streams every native odd-start window through $N=2^{18}$. It checks $1048548$ window updates, $4194304$ cumulative signed identities, and all $262144$ prefix path-DP, $R_\sigma$, $K_N$, and residual relations. Third, exact rational arithmetic checks the stationary chain: $27$ transitions, $9$ stationarity cells, $502$ raw cases, $502$ square-only cases, and $1793$ one-sign masked cases for block lengths at most eight. The analytic proof above, not those finite enumerations, establishes the arbitrary-distinct-time statements. Fourth, a finite Euler diagnostic uses all primes through $2^{20}$.

For compact display, the exact finite channels in the next table are multiplied by $256$. The final two columns are respectively the left side and right side of the scaled version of [\[eq:residual-bound\]](#eq:residual-bound){reference-type="eqref" reference="eq:residual-bound"}.

         $N$     $256P_N$   $256Q_N$   $256U_N$   $256V_N$   residual     bound
  ---------- ------------ ---------- ---------- ---------- ---------- ---------
      $1024$      $64711$     $1108$     $1465$       $44$     $3240$    $3240$
     $65536$    $4127474$     $3132$     $3214$     $4932$     $2680$    $9848$
    $262144$   $16508741$     $4352$      $827$    $11392$     $2560$   $14848$

At the final endpoint, $$(H_{k,0})_{k=1}^8=
 (106237,84569,65768,49604,35783,24127,14429,6449),$$ $$(H_{k,1})_{k=1}^8=(3,-56,-174,-146,115,-54,-111,-14),
 \qquad K_{262144}=129080.$$ The finite Euler-product reproduction is $0.4920202775829839485$ when both $2/\pi^2$ and the $e_k$ are replaced by their stated products through $2^{20}$. It is a truncated conditional diagnostic, not an estimate establishing [\[eq:conditional-constant\]](#eq:conditional-constant){reference-type="eqref" reference="eq:conditional-constant"}. All finite rows reproduce exact identities only. No fit is used as asymptotic evidence.

# Route verdict, scope, and Gates

Route A is `GO`: the mixed hierarchy, deterministic-layer theorem, thirteen-channel simultaneous boundary, exact two-envelope reduction, and stationary algebraic witness are independent theorem edges. Route B is `STOP_SCOPED`: the adaptive capacity is a scalar optimization of a prefix, not an intrinsic dynamical trace, and convergence of $(U_N+|V_N|)/N$ remains open.

The boundary is strict:

-   no $A_k/N$, $B_k/N$, or capacity-envelope limit is proved for the unresolved mixed layers.

-   the $466\to13$ computation is formal and does not establish an arithmetic minimal sufficient statistic.

-   the full-cancellation hypothesis and constant [\[eq:conditional-constant\]](#eq:conditional-constant){reference-type="eqref" reference="eq:conditional-constant"} are conditional and sufficient only.

-   the stationary witness is synthetic, does not have Möbius squarefree statistics, and yields no Möbius nonconvergence result.

-   no finite row, decimal Euler diagnostic, growing-modulus argument, or growing-clock extrapolation is promoted to an asymptotic theorem.

Gates A--E remain false/open. There is no canonical intrinsic spectral determinant, time-oriented scattering or unitary completion, self-adjoint generator with an intrinsic $T\log T$ law, von Mangoldt-weighted prime-power trace, or completed-zeta divisor equality. This paper does not identify Riemann zeros, construct a Hilbert--Polya operator, or prove the Riemann Hypothesis.

# Conclusion

The eight-level run hierarchy separates cleanly into deterministic squarefree support, unconditional one-sign cancellation, and thirteen higher mixed aggregates. For the sixteen densities, all thirteen aggregate limits are necessary and sufficient simultaneously. For the capacity, the weaker unresolved object is the single nonlinear envelope $(U_N+|V_N|)/N$. The stationary witness explains why low-order ternary algebra alone cannot remove its first directional mixed layer. A next route therefore needs a genuine arithmetic theorem for aggregate mixed-exponent cancellation or for the envelope itself. Reproducing more finite prefixes does not cross that boundary.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

**Data availability.** All source, exact outputs, tests, schema, and SHA-256 manifests are contained in the RH-377 repository directory.

**Ethics.** The study uses no human participants, animals, or personal data. No ethics approval was required.

**Author contributions.** The RH research program performed conceptualization, formal analysis, software, validation, and writing.

**Funding and conflicts.** No external funding or conflict of interest is declared.

**AI-assisted workflow.** Drafting and executable checking used the repository's documented multi-agent workflow. Mathematical claims are limited by source locks, proofs, independent audits, and reproducible artifacts recorded here.
