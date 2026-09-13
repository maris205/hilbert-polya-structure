---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--96-finite-subset-circle-expansion"
canonical_tex: "symbolic_dynamics/papers/96-finite-subset-circle-expansion/main.tex"
canonical_pdf: "symbolic_dynamics/papers/96-finite-subset-circle-expansion/main.pdf"
source_sha256: "586edfc8e03fe11e48dd3352ddcb51c6bd4c09b5786dee42f93c65c179f1115f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Subset Circle Expansion: Parity-Split Fixed Counts and Alternating Zeta Factors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/96-finite-subset-circle-expansion>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/96-finite-subset-circle-expansion/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/96-finite-subset-circle-expansion/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/96-finite-subset-circle-expansion/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/96-finite-subset-circle-expansion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $m_d(x)=dx\pmod 1$ on the circle, where $d\geq2$, and let $H_{d,k}$ send a nonempty subset of at most $k$ circle points to its image under $m_d$. This gives a nonlinear, cardinality-collapsing map on the $k$-dimensional finite-subset space. We compute its complete unsigned periodic ledger. If $Q=d^n$, then fixed subsets of exact cardinality $j$ number $$E_j(Q)=\frac{(Q-1)(Q^j-(-1)^j)}{Q+1}.$$ Summing through $j=k$ yields $Q(Q^k-1)/(Q+1)$ for even $k$ and $(Q^{k+1}-1)/(Q+1)$ for odd $k$. The resulting Artin--Mazur zeta function is a finite alternating product of the factors $1-d^r z$. We also obtain an exact Möbius census and a prime-orbit asymptotic, prove $h_{\rm top}(H_{d,k})=k\log d$ through a uniformly finite-to-one product cover, and recover $(d,k)$ from the zeta function. The proof rests on a binary Euler transform: a fixed finite subset is a disjoint union of base cycles, so each base cycle is either absent or present once. Independent coefficient and literal rational-circle enumerations verify the registered finite controls.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: 'Finite-Subset Circle Expansion: Parity-Split Fixed Counts and Alternating Zeta Factors'
```

## Markdown 正文

# Introduction

Finite-subset dynamics retains the motion of individual points while adding collisions: distinct points may acquire the same image, and the cardinality of a configuration may drop. Even for the expanding circle map $x\mapsto dx$, this quotient is not a group endomorphism and is not a fixed Cartesian power. The collision strata interact with periodic counting in a particularly rigid way.

Write $\mathbb T=\mathbb R/\mathbb Z$ and let $X_k$ be the space of all nonempty subsets of $\mathbb T$ of cardinality at most $k$. For $d\geq2$, define $$H_{d,k}:X_k\longrightarrow X_k,
 \qquad H_{d,k}(A)=\{dx\pmod1:x\in A\}.$$ We give an exact unsigned periodic classification of this quotient, with a standard finite-to-one entropy control. Three conclusions carry the main content.

1.  We classify every fixed configuration of every iterate and derive a bivariate Euler product for the exact-cardinality strata. Its rational collapse gives the closed formula in the abstract.

2.  The total fixed count has an even--odd split, and the complete Artin--Mazur zeta function is an alternating product of $k$ linear factors (of $k+1$ factors when $k$ is odd and the factor at $d^0$ is included). Möbius inversion gives the least-period orbit census and the asymptotic $d^{km}/m+O_{d,k}(d^{(k-1)m}/m)$.

3.  The quotient map $\mathbb T^k\to X_k$ has uniformly finite fibers. It therefore transfers the product entropy exactly, giving $k\log d$. The two outermost zeta factors recover $d$ and $k$, so the parameter family is rigid under topological conjugacy.

The first signal is visible without asymptotics. At time $n$, put $Q=d^n$. The counts for subsets of sizes $1,2,3,4$ are $$Q-1,\qquad (Q-1)^2,\qquad (Q-1)(Q^2-Q+1),\qquad
 (Q-1)^2(Q^2+1).$$ Their partial sums are $Q-1$, $Q(Q-1)$, $(Q-1)(Q^2+1)$, and $Q(Q-1)(Q^2+1)$. The alternating boundary term is the early anomaly that leads to the parity theorem.

# Finite-subset spaces and the owner boundary

For a compact metric space $Y$, its $k$th finite-subset space is $$\exp_k(Y)=\{A\subseteq Y:1\leq\lvert A\rvert\leq k\},$$ with the Hausdorff topology. Equivalently, it has the quotient topology of $$\pi_k:Y^k\longrightarrow \exp_k(Y),\qquad
 \pi_k(y_1,\ldots,y_k)=\{y_1,\ldots,y_k\}.$$ We use $X_k=\exp_k(\mathbb T)$. Tuffley determined the topology of these circle spaces, their homotopy type, and the degree of maps induced from circle maps [@Tuffley2002]. In particular, $X_k$ has topological dimension $k$; for $k\geq4$ it is generally a stratified compactum rather than a manifold.

The notation needs a firewall. Some hyperspace papers call $\exp_k(Y)$ an "$n$-fold symmetric product." The topological symmetric power $\operatorname{SP}^k(Y)=Y^k/S_k$ remembers multiplicities, whereas $\exp_k(Y)$ forgets them. The two agree for $k\leq2$ but differ for $k\geq3$: for example, $(a,a,b)$ and $(a,b,b)$ define different points in $\operatorname{SP}^3(Y)$ and the same point in $\exp_3(Y)$.

General induced hyperspace dynamics is well developed. Akin, Auslander, and Nagar study the relation between a map and the induced map on compact subsets [@AkinAuslanderNagar2017]. Higuera and Illanes record, among other facts, the finite-permutation mechanism behind periodic induced subsets [@HigueraIllanes2011]. Gómez-Rueda, Illanes, and Méndez prove qualitative transfer statements for periodicity, recurrence, and related properties on finite-subset spaces [@GomezRuedaIllanesMendez2012]. Fernández, Good, and Puljiz analyze admissible period sets in hyperspaces and symmetric products [@FernandezGoodPuljiz2018]. These results supply the qualitative owner boundary; they do not give the unsigned exact-cardinality ledger computed below.

For multiplication maps of the circle, Tan studies rotational finite subsets and their rotation data [@Tan2024]. Our count instead includes every union of base cycles that fits below a cardinality cutoff, without imposing one cyclic order type or a rotation number.

Finally, Artin--Mazur counting records cardinalities of fixed sets [@ArtinMazur1965]. Lefschetz zeta functions and symmetric-power identities record fixed point indices; recent functorial treatments include [@BlancoGomezEtAl2016; @Crabb2025]. We compare the two ledgers in [6](#sec:entropy-control){reference-type="ref" reference="sec:entropy-control"}, but do not identify them. The residual theorem package here is the circle-multiplication specialization and rational collapse of binary cycle selection, its parity split, the resulting unsigned Artin--Mazur factors, temporal census, and parameter rigidity. The finite-to-one entropy argument is a standard application of Bowen's factor inequality, not a claimed family-specific mechanism. A bounded search through 28 August 2026 did not locate that combined package. This is not a priority proof, and external novelty language remains on hold.

# Invariant finite sets as binary cycle selections

Fix $d\geq2$ and $k\geq1$. At time $n\geq1$, write $$Q=d^n,
 \qquad g_Q=m_d^n=m_Q:\mathbb T\longrightarrow\mathbb T.$$ For $\ell\geq1$, let $O_\ell(Q)$ denote the number of $g_Q$-orbits of least period $\ell$.

[\[lem:base\]]{#lem:base label="lem:base"} For every $\ell\geq1$, $$\label{eq:base-orbits}
 \lvert \operatorname{Fix}(g_Q^\ell)\rvert=Q^\ell-1,
 \qquad
 O_\ell(Q)=\frac1\ell\sum_{e\mid\ell}
 \mu\!\left(\frac{\ell}{e}\right)(Q^e-1).$$ Moreover, as a formal power series, $$\label{eq:base-zeta}
 \prod_{\ell\geq1}(1-u^\ell)^{-O_\ell(Q)}
 =\exp\!\left(\sum_{r\geq1}\frac{Q^r-1}{r}u^r\right)
 =\frac{1-u}{1-Qu}.$$

The equation $g_Q^\ell(x)=x$ is $(Q^\ell-1)x=0$ in $\mathbb T$. Its solutions form the cyclic subgroup of order $Q^\ell-1$. If $R_\ell(Q)$ is the number of points of least $g_Q$-period $\ell$, then $Q^\ell-1=\sum_{e\mid\ell}R_e(Q)$. Möbius inversion gives $R_\ell(Q)=\ell O_\ell(Q)$ and proves [\[eq:base-orbits\]](#eq:base-orbits){reference-type="eqref" reference="eq:base-orbits"}.

The infinite product in [\[eq:base-zeta\]](#eq:base-zeta){reference-type="eqref" reference="eq:base-zeta"} is well defined formally, because only finitely many factors affect each coefficient. Its logarithm has coefficient $$[u^r]\sum_{\ell\geq1}O_\ell(Q)
       \sum_{a\geq1}\frac{u^{a\ell}}a
 =\frac1r\sum_{\ell\mid r}\ell O_\ell(Q)
 =\frac{Q^r-1}{r}.$$ Exponentiating gives the first equality. Summing the two geometric logarithms gives the rational expression.

We denote the common formal series in [\[eq:base-zeta\]](#eq:base-zeta){reference-type="eqref" reference="eq:base-zeta"} by $\zeta_{g_Q}(u)$.

The next lemma is the point where the induced dynamics becomes a binary Euler transform. The finite-permutation observation is general and appears in the induced finite-subset literature; see, for example, [@HigueraIllanes2011 Lemma 4.7]. We include the short proof to fix the exact orbit inventory used below.

[\[lem:union\]]{#lem:union label="lem:union"} Let $A\subset\mathbb T$ be nonempty and finite. Then $g_Q(A)=A$ if and only if $A$ is a disjoint union of complete finite $g_Q$-orbits. This decomposition is unique.

If $g_Q(A)=A$, the restriction $g_Q|_A:A\to A$ is surjective. A surjection of a finite set is bijective, so $g_Q|_A$ is a permutation. Its permutation cycles are complete $g_Q$-orbits in $\mathbb T$, they are pairwise disjoint, and their union is $A$. The cycle decomposition of a permutation is unique. Conversely, $g_Q$ maps every complete orbit onto itself, so it maps any finite disjoint union of such orbits onto that union.

For $j\geq1$, define the exact-cardinality fixed stratum $$E_j(Q)=\lvert \{A\in X_j:\lvert A\rvert=j,\ g_Q(A)=A\}\rvert.$$ The number is independent of the ambient cutoff once that cutoff is at least $j$. These strata are used only to partition fixed points; the exact-$j$ stratum is not generally forward invariant because collisions may reduce cardinality.

[\[thm:euler\]]{#thm:euler label="thm:euler"} As a formal power series in $u$, $$\begin{aligned}
 \Phi_Q(u)
 &:=1+\sum_{j\geq1}E_j(Q)u^j \
 &=\prod_{\ell\geq1}(1+u^\ell)^{O_\ell(Q)}
   =\frac{\zeta_{g_Q}(u)}{\zeta_{g_Q}(u^2)}
   =\frac{1-Qu^2}{(1-Qu)(1+u)}.\label{eq:euler-quotient}\end{aligned}$$ Consequently, for every $j\geq1$, $$\label{eq:exact-j}
 E_j(Q)=\frac{(Q-1)(Q^j-(-1)^j)}{Q+1}.$$

By [\[lem:union\]](#lem:union){reference-type="ref" reference="lem:union"}, a fixed finite subset is specified by deciding, for each $g_Q$-orbit, whether to include that orbit. An orbit of length $\ell$ contributes either $1$ or $u^\ell$, and there are $O_\ell(Q)$ such orbits. Multiplying these independent binary choices proves the first product.

Since $1+u^\ell=(1-u^{2\ell})/(1-u^\ell)$, [\[lem:base\]](#lem:base){reference-type="ref" reference="lem:base"} gives $$\prod_{\ell\geq1}(1+u^\ell)^{O_\ell(Q)}
 =\frac{\prod_\ell(1-u^{2\ell})^{O_\ell(Q)}}
        {\prod_\ell(1-u^\ell)^{O_\ell(Q)}}
 =\frac{\zeta_{g_Q}(u)}{\zeta_{g_Q}(u^2)}.$$ Substitution of [\[eq:base-zeta\]](#eq:base-zeta){reference-type="eqref" reference="eq:base-zeta"} cancels $1-u$ and produces the final rational function in [\[eq:euler-quotient\]](#eq:euler-quotient){reference-type="eqref" reference="eq:euler-quotient"}.

For coefficient extraction, rewrite it as $$\Phi_Q(u)=1+\frac{(Q-1)u}{(1-Qu)(1+u)}.$$ The coefficient of $u^{j-1}$ in the reciprocal product is $$\frac{Q}{Q+1}Q^{j-1}+\frac1{Q+1}(-1)^{j-1}
 =\frac{Q^j-(-1)^j}{Q+1}.$$ Multiplication by $Q-1$ proves [\[eq:exact-j\]](#eq:exact-j){reference-type="eqref" reference="eq:exact-j"}. The quotient is an integer because $Q^j-(-1)^j$ is divisible by $Q+1$; integrality also follows from the orbit-selection interpretation.

# Parity-split fixed counts and zeta factors

Put $$A_k(Q)=\sum_{j=1}^k E_j(Q).$$ Since $H_{d,k}^n(A)=g_Q(A)$ for $Q=d^n$, this is exactly $\lvert \operatorname{Fix}(H_{d,k}^n)\rvert$.

[\[thm:parity\]]{#thm:parity label="thm:parity"} For $Q\geq2$ and $k\geq1$, $$\label{eq:total-fix}
 A_k(Q)=
 \begin{cases}
 \displaystyle \frac{Q(Q^k-1)}{Q+1},&k\ \text{even},\\[6pt]
 \displaystyle \frac{Q^{k+1}-1}{Q+1},&k\ \text{odd}.
 \end{cases}$$ Equivalently, with $$r_0(k)=\begin{cases}1,&k\ \text{even},\\0,&k\ \text{odd},\end{cases}$$ one has the alternating polynomial $$\label{eq:alternating-polynomial}
 A_k(Q)=\sum_{r=r_0(k)}^k(-1)^{k-r}Q^r.$$

Summing [\[eq:exact-j\]](#eq:exact-j){reference-type="eqref" reference="eq:exact-j"} gives $$A_k(Q)=\frac{Q-1}{Q+1}
 \left(\frac{Q(Q^k-1)}{Q-1}-\sum_{j=1}^k(-1)^j\right).$$ The alternating sum is zero for even $k$ and $-1$ for odd $k$. This proves [\[eq:total-fix\]](#eq:total-fix){reference-type="eqref" reference="eq:total-fix"}. Polynomial division by $Q+1$ gives [\[eq:alternating-polynomial\]](#eq:alternating-polynomial){reference-type="eqref" reference="eq:alternating-polynomial"}; its lower endpoint is $Q^1$ in the even case and $Q^0$ in the odd case.

Define the Artin--Mazur zeta function formally by $$\zeta^{\mathrm{AM}}_{d,k}(z)=
 \exp\!\left(\sum_{n\geq1}
 \lvert \operatorname{Fix}(H_{d,k}^n)\rvert\frac{z^n}{n}\right).$$

[\[thm:am-zeta\]]{#thm:am-zeta label="thm:am-zeta"} For $d\geq2$ and $k\geq1$, $$\label{eq:am-zeta}
 \boxed{\displaystyle
 \zeta^{\mathrm{AM}}_{d,k}(z)=
 \prod_{r=r_0(k)}^k
 (1-d^r z)^{(-1)^{k-r+1}}.}$$ In particular,

   $k$         $\zeta^{\mathrm{AM}}_{d,k}(z)$
  ----- --------------------------------------------
   $1$              $\dfrac{1-z}{1-dz}$
   $2$             $\dfrac{1-dz}{1-d^2z}$
   $3$    $\dfrac{(1-z)(1-d^2z)}{(1-dz)(1-d^3z)}$
   $4$   $\dfrac{(1-dz)(1-d^3z)}{(1-d^2z)(1-d^4z)}$

Insert $Q=d^n$ into [\[eq:alternating-polynomial\]](#eq:alternating-polynomial){reference-type="eqref" reference="eq:alternating-polynomial"}. Then $$\begin{aligned}
 \log\zeta^{\mathrm{AM}}_{d,k}(z)
 &=\sum_{r=r_0(k)}^k(-1)^{k-r}
   \sum_{n\geq1}\frac{(d^rz)^n}{n}\\
 &=-\sum_{r=r_0(k)}^k(-1)^{k-r}\log(1-d^rz).\end{aligned}$$ Exponentiation gives [\[eq:am-zeta\]](#eq:am-zeta){reference-type="eqref" reference="eq:am-zeta"}. The displayed examples are direct specializations.

[\[cor:rigidity\]]{#cor:rigidity label="cor:rigidity"} Within the family $d\geq2$, $k\geq1$, the Artin--Mazur zeta function determines the ordered pair $(d,k)$. Hence $H_{d,k}$ and $H_{d',k'}$ can be topologically conjugate only if $(d,k)=(d',k')$.

The factorization [\[eq:am-zeta\]](#eq:am-zeta){reference-type="eqref" reference="eq:am-zeta"} has no internal cancellation, because $d^r$ is strictly increasing in $r$. Its positive pole nearest the origin is $d^{-k}$, and its positive zero nearest the origin is $d^{-(k-1)}$. For $k=1$ this zero is the factor at $d^0=1$. The ratio of the zero location to the pole location is $d$. The pole then recovers $k$. Topological conjugacy bijects the fixed sets of corresponding iterates and therefore preserves the Artin--Mazur zeta function.

# Least-period orbits

Let $P_{d,k}(m)$ be the number of $H_{d,k}$-orbits of least temporal period $m$.

[\[thm:temporal\]]{#thm:temporal label="thm:temporal"} For every $m\geq1$, $$\label{eq:temporal-census}
 P_{d,k}(m)=\frac1m\sum_{e\mid m}
 \mu\!\left(\frac me\right)A_k(d^e),$$ where $A_k$ is given by either [\[eq:total-fix\]](#eq:total-fix){reference-type="eqref" reference="eq:total-fix"} or [\[eq:alternating-polynomial\]](#eq:alternating-polynomial){reference-type="eqref" reference="eq:alternating-polynomial"}. This expression is a nonnegative integer. For fixed $d\geq2$ and $k\geq2$, $$\label{eq:prime-orbit}
 P_{d,k}(m)=\frac{d^{km}}m
 +O_{d,k}\!\left(\frac{d^{(k-1)m}}m\right).$$

Let $R_{d,k}(m)$ count points of least $H_{d,k}$-period $m$. Every point fixed by the $n$th iterate has a unique least period dividing $n$, so $$A_k(d^n)=\sum_{m\mid n}R_{d,k}(m).$$ Möbius inversion gives the numerator of [\[eq:temporal-census\]](#eq:temporal-census){reference-type="eqref" reference="eq:temporal-census"}. Every least-$m$ orbit contains exactly $m$ points, hence $P_{d,k}(m)=R_{d,k}(m)/m$. This proves both the formula and its nonnegative integrality without an auxiliary congruence argument.

Equation [\[eq:alternating-polynomial\]](#eq:alternating-polynomial){reference-type="eqref" reference="eq:alternating-polynomial"} gives $$A_k(d^m)=d^{km}+O_{d,k}(d^{(k-1)m}).$$ Every proper divisor $e$ of $m$ satisfies $e\leq m/2$. Also $A_k(d^e)\leq C_{d,k}d^{ke}$, and therefore $$\sum_{\substack{e\mid m\\e<m}}A_k(d^e)
 \leq C_{d,k}\sum_{e=1}^{\lfloor m/2\rfloor}d^{ke}
 =O_{d,k}(d^{km/2})
 =O_{d,k}(d^{(k-1)m}),$$ where the last inequality uses $k\geq2$. Substitution in [\[eq:temporal-census\]](#eq:temporal-census){reference-type="eqref" reference="eq:temporal-census"} proves [\[eq:prime-orbit\]](#eq:prime-orbit){reference-type="eqref" reference="eq:prime-orbit"}.

# Entropy and two owner controls {#sec:entropy-control}

The finite-subset quotient is not a product, but it has a product cover with uniformly bounded fibers. This section records a general entropy control, not a residual novelty claim for the circle family; related entropy questions for induced hyperspace maps are surveyed and developed in [@KwietniakOprocha2007].

[\[thm:entropy\]]{#thm:entropy label="thm:entropy"} For $d\geq2$ and $k\geq1$, $$\label{eq:entropy}
 h_{\mathrm{top}}(H_{d,k})=k\log d.$$

Let $M_{d,k}=m_d^{\times k}$ on $\mathbb T^k$. The quotient map $\pi_k$ satisfies $$\pi_k\circ M_{d,k}=H_{d,k}\circ\pi_k.$$ It is onto. If $A\in X_k$ has $j$ elements, then $\pi_k^{-1}(A)$ consists of the $k$-tuples in which every member of $A$ occurs at least once. In particular, $$\lvert \pi_k^{-1}(A)\rvert\leq j^k\leq k^k,$$ uniformly in $A$.

Entropy does not increase under a factor, so $h_{\mathrm{top}}(H_{d,k})\leq h_{\mathrm{top}}(M_{d,k})$. Bowen's factor inequality bounds the reverse difference by the supremum of the Bowen entropies of the fibers [@Bowen1971]. Every fiber above has at most $k^k$ points, independent of orbit length, and hence has Bowen entropy zero. Thus the two entropies are equal. This is the standard uniformly finite-to-one consequence of Bowen's factor inequality. The product formula and $h_{\mathrm{top}}(m_d)=\log d$ give $h_{\mathrm{top}}(M_{d,k})=k\log d$.

#### Homological control.

Tuffley's results [@Tuffley2002] give $$X_k\simeq S^{2\lceil k/2\rceil-1},
 \qquad
 \deg(H_{d,k})=d^{\lceil k/2\rceil}
 \quad\text{on top nonzero homology}.$$ Since this homology dimension is odd, the Lefschetz number of the $n$th iterate is $$L(H_{d,k}^n)=1-d^{n\lceil k/2\rceil},$$ and the corresponding Lefschetz zeta function is $$\zeta^{\mathrm{L}}_{d,k}(z)
 =\exp\!\left(\sum_{n\geq1}L(H_{d,k}^n)\frac{z^n}{n}\right)
 =\frac{1-d^{\lceil k/2\rceil}z}{1-z}.$$ For $k\geq2$, this homological scale differs from the unsigned growth scale $d^{kn}$ in [\[thm:parity\]](#thm:parity){reference-type="ref" reference="thm:parity"}. Thus the Artin--Mazur factors in [\[eq:am-zeta\]](#eq:am-zeta){reference-type="eqref" reference="eq:am-zeta"} are not a reformulation of the Lefschetz or fixed-index formulas owned by the cited literature.

#### Multiplicity control.

Periodic points of symmetric-product mappings have a direct earlier literature, including Rallis [@Rallis1983]; the following calculation is only a comparison control. On the genuine symmetric power $\operatorname{SP}^k(\mathbb T)$, equality of a multiset with its image first forces its finite support to map onto itself. Thus $g_Q$ permutes the support, and the multiplicity is constant along every support cycle. A fixed multiset may consequently use a complete $g_Q$-orbit with any nonnegative common multiplicity. Therefore its mass generating function is $$\prod_{\ell\geq1}(1-u^\ell)^{-O_\ell(Q)}
 =\frac{1-u}{1-Qu}.$$ The coefficient at mass $k\geq1$ is $Q^{k-1}(Q-1)$. Hence the induced map on $\operatorname{SP}^k(\mathbb T)$ has $$\zeta^{\mathrm{AM}}_{\operatorname{SP}^k(m_d)}(z)
 =\frac{1-d^{k-1}z}{1-d^kz}.$$ This agrees with the finite-subset result at $k\leq2$, when multiplicity and support encode the same quotient, but it lacks the lower alternating factors for $k\geq3$. The comparison isolates the mechanism: arbitrary orbit multiplicity gives the ordinary Euler transform, whereas forgetting multiplicity leaves a binary transform and creates the parity boundary.

# Exact controls, boundary cases, and scope

The registered script implements two independent finite probes. The first computes the Möbius orbit counts $O_\ell(Q)$ and multiplies the truncated binary Euler factors with exact integer arithmetic. For $2\leq Q\leq8$ and $j,k\leq9$, it compares every coefficient and partial sum with [\[eq:exact-j\]](#eq:exact-j){reference-type="eqref" reference="eq:exact-j"} and [\[eq:total-fix\]](#eq:total-fix){reference-type="eqref" reference="eq:total-fix"}. A separate formal-factor probe checks every logarithmic coefficient and the outer pole/zero recovery for $2\leq d\leq7$, $1\leq k\leq9$, and iterates through 15. It also checks the temporal Möbius census, including $k=1$, and its divisibility.

The second probe works with actual rational circle points. For a chosen $(Q,k)$ it takes $$L=\operatorname{lcm}_{1\leq\ell\leq k}(Q^\ell-1),$$ decomposes multiplication by $Q$ on $\mathbb Z/L\mathbb Z$ into literal cycles, and counts cycle selections by cardinality. Small cases additionally enumerate every subset of $\mathbb Z/L\mathbb Z$ of size at most $k$ and test $QA=A$ directly. The two routes share neither coefficient extraction nor subset enumeration.

The assumptions are material. We exclude $d=1$, because the identity has uncountably many fixed configurations and its unsigned Artin--Mazur zeta function is not defined by finite cardinalities. The case $k=1$ is included as a base control, but $k\geq2$ is the genuinely higher-dimensional family. We exclude the empty subset; adding it would add one fixed point to every iterate and multiply [\[eq:am-zeta\]](#eq:am-zeta){reference-type="eqref" reference="eq:am-zeta"} by $(1-z)^{-1}$. Exact-cardinality coefficients $E_j(Q)$ are fixed-point strata, not zeta functions of invariant exact-$j$ subsystems.

This manuscript is an internal theorem record. Public posting, submission, and absolute priority language remain on external hold pending a broader specialist and database search.
