---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--67-multiplicative-plaquette-matroid-complexity"
canonical_tex: "symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity/main.tex"
canonical_pdf: "symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity/main.pdf"
source_sha256: "940ceda23385c37a2c3f362640c8cd362807685b848329bbf4897b8f2b4984ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Arithmetic Prefixes and Cycle-Matroid Dependence in a Multiplicative Plaquette Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $a,b\geq2$ be coprime and let $\mathbb F_q$ be a finite field. We study the compact linear multiplicative constraint space $$X_{a,b}=\{x\in\mathbb F_q^{\mathbb N}:x_n-x_{an}-x_{bn}+x_{abn}=0
   \text{ for every }n\geq1\}.$$ Every integer has unique coordinates $r a^i b^j$, and on each root component the rule integrates to $x_{r a^i b^j}=u_i+v_j$. This yields an explicit topological-group isomorphism between $X_{a,b}$ and the unrestricted coordinates whose indices are not divisible by $ab$. We then calculate every finite projection. A coordinate $r a^i b^j$ is viewed as an edge from row vertex $i$ to column vertex $j$; the projection dimension is the sum of the number of vertices minus the number of connected components over the resulting root-wise bipartite graphs. Thus the coordinate-dependence matroid is a direct sum of graphic matroids, and the only finite compatibility conditions are alternating cycle sums. Under Haar measure, forests are exactly the jointly independent coordinate families and each cycle-rank unit contributes $\log q$ of total correlation. Arithmetic prefixes have $q^{N-\lfloor N/(ab)\rfloor}$ patterns, whereas an $M\times N$ exponent rectangle has $q^{M+N-1}$ patterns. These are two normalizations of one finite-shape rank formula, not interchangeable entropy statements.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 25 August 2026'
title: 'Arithmetic Prefixes and Cycle-Matroid Dependence in a Multiplicative Plaquette Shift'
```

## Markdown 正文

# Introduction

Multiplicative symbolic constraints come with more than one natural finite geometry. Arithmetic prefixes retain the indices $1,\ldots,N$, while prime-valuation or exponent coordinates organize a multiplicative orbit into a lattice. Pattern counts in these geometries need not have the same scale. The difference is structural, not a normalization error.

The foundational multiplicative-integer framework and its dimension theory were developed by Kenyon, Peres, and Solomyak [@KenyonPeresSolomyak2012]. Two-generator dimension problems and pattern generation for multiplicative systems, as well as coupled multidimensional systems, axial products, surface entropy, and affine multiplicative shifts are treated in [@PeresSchmelingSeuretSolomyak2014; @BanHuLin2019; @BanHuLai2021; @BanHuLaiLiao2025; @BanHuLaiLiaoAffine2025]. Prime-valuation coordinates also support exact density and correlation constructions, including recent symbolic realizations [@MoraCuellarRojasAravenaYavicoli2026]. Against this established background, we isolate one finite-field linear rule and ask for an exact answer on *every* finite coordinate set.

Fix coprime integers $a,b\geq2$ and a finite field $\mathbb F_q$. On $\mathbb F_q^{\mathbb N}$ define $$\label{eq:def-X}
 X_{a,b}=\left\{x:
 x_n-x_{an}-x_{bn}+x_{abn}=0
 \text{ for every }n\in\mathbb N\right\}.$$ For $c\in\mathbb N$, the decimation $D_c(x)_n=x_{cn}$ preserves $X_{a,b}$, so [\[eq:def-X\]](#eq:def-X){reference-type="eqref" reference="eq:def-X"} is a compact linear multiplicative system. The local rule factors into two first differences after multiplicative coordinates are introduced. That elementary observation is only the starting point: the main result identifies the full finite-projection matroid.

Every $n\in\mathbb N$ can be written uniquely as $$n=r a^i b^j,
 \qquad i,j\in\mathbb N_0,
 \qquad a\nmid r,\quad b\nmid r.$$ For a finite $F\subset\mathbb N$ and a fixed root $r$, let $$E_r(F)=\{(i,j):r a^i b^j\in F\}.$$ Make a bipartite graph $G_r(F)$ whose row vertices are the $i$'s occurring in $E_r(F)$, whose column vertices are the $j$'s occurring there, and whose edges are the pairs in $E_r(F)$. Write $I_r(F)$ and $J_r(F)$ for its two vertex classes and $c_r(F)$ for its number of connected components. Empty graphs are omitted. Define $$\begin{aligned}
 d(F)&=\sum_r\bigl(|I_r(F)|+|J_r(F)|-c_r(F)\bigr),
 \label{eq:dF}\\
 \beta(F)&=\sum_r\bigl(|E_r(F)|-|I_r(F)|-|J_r(F)|+c_r(F)\bigr).
 \label{eq:betaF}\end{aligned}$$ Thus $d(F)+\beta(F)=|F|$, and $\beta(F)$ is the sum of the graph cycle ranks. For precision, the *coordinate-dependence matroid on $F$* below is the vector matroid of the evaluation maps $$\epsilon_n:X_{a,b}\longrightarrow\mathbb F_q,
 \qquad \epsilon_n(x)=x_n,\qquad n\in F.$$ Thus $A\subseteq F$ is independent when the functionals $\{\epsilon_n:n\in A\}$ are linearly independent. This is the standard linear-dependence meaning of matroid terminology [@Whitney1935]. For normalized Haar measure $\mu$ on $X_{a,b}$ and the random vector $Z_F=(x_n)_{n\in F}$, write $$\operatorname{TC}_\mu(Z_F)=\sum_{n\in F}\operatorname{H}_\mu(x_n)-\operatorname{H}_\mu(Z_F)$$ for its total correlation.

[\[thm:main\]]{#thm:main label="thm:main"} Let $a,b\geq2$ be coprime and let $\mathbb F_q$ be a finite field.

1.  Put $\mathcal B=\{n\in\mathbb N:ab\nmid n\}$. Coordinate restriction is a topological-group isomorphism $$X_{a,b}\longrightarrow\mathbb F_q^{\mathcal B}.$$ Its inverse is explicit: if $n=r a^i b^j$, then $$\label{eq:global-inverse-intro}
     x_{r a^i b^j}=x_{r a^i}+x_{r b^j}-x_r.$$

2.  For every finite $F\subset\mathbb N$, the image $\operatorname{proj}_F(X_{a,b})$ is a linear subspace of dimension $d(F)$. Hence $$\label{eq:finite-count-intro}
     |\operatorname{proj}_F(X_{a,b})|=q^{d(F)}.$$ The coordinate-dependence matroid is the direct sum over $r$ of the graphic matroids of $G_r(F)$. Equivalently, allowed labels are exactly those whose alternating sum vanishes on every graph cycle.

3.  Let $\mu$ be normalized Haar measure on $X_{a,b}$. Then $$\label{eq:haar-intro}
     \operatorname{H}_\mu(Z_F)=d(F)\log q,
     \qquad
     \operatorname{TC}_\mu(Z_F)=\beta(F)\log q,
     \qquad Z_F=(x_n)_{n\in F}.$$ The coordinates in $F$ are jointly independent if and only if every $G_r(F)$ is a forest. In particular, every two distinct coordinates are independent.

The theorem unifies two counts that look incompatible when stated alone.

[\[cor:two-geometries\]]{#cor:two-geometries label="cor:two-geometries"} For every $L\geq1$, $$\label{eq:prefix-count-intro}
 |\operatorname{proj}_{\{1,\ldots,L\}}(X_{a,b})|
 =q^{L-\lfloor L/(ab)\rfloor}.$$ For a root $r$ and $M,N\geq1$, put $$Q_r(M,N)=\{r a^i b^j:0\leq i<M,\ 0\leq j<N\}.$$ Then $$\label{eq:rectangle-count-intro}
 |\operatorname{proj}_{Q_r(M,N)}(X_{a,b})|=q^{M+N-1},
 \qquad
 \beta(Q_r(M,N))=(M-1)(N-1).$$

The first exponent in [\[eq:prefix-count-intro\]](#eq:prefix-count-intro){reference-type="eqref" reference="eq:prefix-count-intro"} has positive density in the arithmetic interval. The second is boundary order in the exponent box. We call the former an arithmetic-prefix complexity and the latter an exact exponent-box boundary law. Neither phrase silently selects a Følner sequence or asserts a topological entropy for the multiplicative action.

The proof has three short layers. First, the multiplicative root decomposition turns [\[eq:def-X\]](#eq:def-X){reference-type="eqref" reference="eq:def-X"} into a vanishing mixed difference on $\mathbb N_0^2$, whose solutions are sums of one row and one column potential. Second, restriction to an arbitrary finite set becomes a vertex-potential map on $G_r(F)$; its rank and its cycle conditions are the standard incidence rank and cycle space. Third, Haar measure pushes forward uniformly to every finite image, converting rank and cycle rank into exact entropy and total correlation.

#### Organization.

proves the global coordinates and product homeomorphism. proves the all-finite-shape rank, cycle, and Haar statements. specialize the formula to the two geometries. records the literature context and the claim boundary.

# Multiplicative components and global coordinates {#sec:coordinates}

Write $$\mathcal R_{a,b}=\{r\in\mathbb N:a\nmid r,\ b\nmid r\}.$$ The coprimality assumption gives a coordinate system adapted to both multipliers.

[\[lem:root-decomposition\]]{#lem:root-decomposition label="lem:root-decomposition"} The map $$\mathcal R_{a,b}\times\mathbb N_0^2\longrightarrow\mathbb N,
 \qquad (r,i,j)\longmapsto r a^i b^j,$$ is a bijection.

For $n\in\mathbb N$, let $i$ be maximal with $a^i\mid n$ and let $j$ be maximal with $b^j\mid n$. Since $a$ and $b$ are coprime, $a^i b^j\mid n$. The integer $r=n/(a^i b^j)$ is divisible by neither $a$ nor $b$, by maximality.

Conversely, suppose $n=r a^i b^j$ with $r\in\mathcal R_{a,b}$. The factor $r b^j$ is not divisible by $a$: otherwise $\gcd(a,b^j)=1$ would imply $a\mid r$. Hence $i$ is the maximal exponent of a power of $a$ dividing $n$. The same argument identifies $j$ as the maximal $b$-exponent. Both exponents and then $r$ are unique.

For $x\in\mathbb F_q^{\mathbb N}$ and $r\in\mathcal R_{a,b}$, set $$y^{(r)}_{i,j}=x_{r a^i b^j},
 \qquad (i,j)\in\mathbb N_0^2.$$ The equation defining $X_{a,b}$ becomes $$\label{eq:mixed-difference}
 y_{i,j}-y_{i+1,j}-y_{i,j+1}+y_{i+1,j+1}=0.$$ We omit the root superscript while studying one component.

[\[lem:integrate\]]{#lem:integrate label="lem:integrate"} An array $y\in\mathbb F_q^{\mathbb N_0^2}$ satisfies [\[eq:mixed-difference\]](#eq:mixed-difference){reference-type="eqref" reference="eq:mixed-difference"} for all $i,j\geq0$ if and only if $$\label{eq:integrated}
 y_{i,j}=y_{i,0}+y_{0,j}-y_{0,0}
 \qquad(i,j\geq0).$$ Equivalently, after the gauge choice $v_0=0$, it has the unique form $$\label{eq:u-plus-v}
 y_{i,j}=u_i+v_j,
 \qquad
 u_i=y_{i,0},\quad v_j=y_{0,j}-y_{0,0}.$$

Rearranging [\[eq:mixed-difference\]](#eq:mixed-difference){reference-type="eqref" reference="eq:mixed-difference"} gives $$y_{i+1,j+1}-y_{i,j+1}=y_{i+1,j}-y_{i,j}.$$ Thus the horizontal increment from row $i$ to row $i+1$ is independent of the column. Summing these increments from $0$ to $i-1$ yields $y_{i,j}-y_{0,j}=y_{i,0}-y_{0,0}$, which is [\[eq:integrated\]](#eq:integrated){reference-type="eqref" reference="eq:integrated"}. Direct substitution proves the converse. The gauge formula [\[eq:u-plus-v\]](#eq:u-plus-v){reference-type="eqref" reference="eq:u-plus-v"} follows immediately and remains valid in characteristic two.

The component solution group is therefore explicitly isomorphic to $$\mathcal Y\cong \mathbb F_q^{\mathbb N_0}\times\mathbb F_q^{\mathbb N},$$ where the two factors record the full row axis and the positive column axis. The next proposition identifies these axes directly in the arithmetic index set.

[\[prop:global-homeo\]]{#prop:global-homeo label="prop:global-homeo"} Let $$\mathcal B=\{n\in\mathbb N:ab\nmid n\}.$$ The restriction map $$\label{eq:restriction-map}
 \rho_{\mathcal B}:X_{a,b}\longrightarrow\mathbb F_q^{\mathcal B},
 \qquad x\longmapsto x|_{\mathcal B},$$ is a topological-group isomorphism. If $n=r a^i b^j$ is its root representation, the inverse map is $$\label{eq:inverse-map}
 (\rho_{\mathcal B}^{-1}z)_{r a^i b^j}
 =z_{r a^i}+z_{r b^j}-z_r.$$ Consequently, $$\label{eq:global-product}
 X_{a,b}\cong\prod_{r\in\mathcal R_{a,b}}\mathcal Y
 \cong\mathbb F_q^{\mathcal B}.$$

For $n=r a^i b^j$, the product $ab$ divides $n$ exactly when $i,j\geq1$. The forward implication uses coprimality: if $i=0$ and $a\mid r b^j$, then $a\mid r$, contrary to $r\in\mathcal R_{a,b}$; the case $j=0$ is symmetric. Thus $\mathcal B$ is precisely the union of the two axes in every root component, with the origin counted once.

By , those axes determine every point of $X_{a,b}$, so [\[eq:restriction-map\]](#eq:restriction-map){reference-type="eqref" reference="eq:restriction-map"} is injective. Conversely, for arbitrary $z\in\mathbb F_q^{\mathcal B}$, formula [\[eq:inverse-map\]](#eq:inverse-map){reference-type="eqref" reference="eq:inverse-map"} is defined because all three indices on its right lie in $\mathcal B$. It agrees with $z$ on either axis and satisfies every plaquette equation by . Hence restriction is surjective.

Both maps are homomorphisms. Restriction is continuous, and each coordinate of its inverse depends on only three coordinates of $z$. The inverse is therefore continuous in the product topology. The component product description follows from .

[\[rem:coprime\]]{#rem:coprime label="rem:coprime"} The proof uses $\gcd(a,b)=1$ twice: to split divisibility exponents and to identify the free axes with $ab\nmid n$. When the multipliers share a factor, the exponent coordinates can have multiple presentations, so is not asserted.

# Finite projections and graphic matroids {#sec:finite}

The product homeomorphism solves global extension, but it does not by itself display the dependence among an arbitrary selection of non-axis coordinates. The right finite object is the bipartite graph introduced before .

Fix a finite $F\subset\mathbb N$. For each root $r$ occurring in $F$, write $$E_r=E_r(F),\qquad I_r=I_r(F),\qquad J_r=J_r(F),
 \qquad G_r=G_r(F).$$ Regard $I_r$ and $J_r$ as disjoint vertex classes even if the same integer appears in both. Define the vertex-potential map $$\label{eq:potential-map}
 \Phi_r:\mathbb F_q^{I_r}\oplus\mathbb F_q^{J_r}\longrightarrow\mathbb F_q^{E_r},
 \qquad
 \Phi_r(u,v)_{(i,j)}=u_i+v_j.$$

[\[lem:potential-rank\]]{#lem:potential-rank label="lem:potential-rank"} The image of $\Phi_r$ is exactly the restriction to $E_r$ of all global solutions of [\[eq:mixed-difference\]](#eq:mixed-difference){reference-type="eqref" reference="eq:mixed-difference"}, and $$\label{eq:potential-rank}
 \operatorname{rank}\Phi_r=|I_r|+|J_r|-c_r.$$

Every global component solution has the potential form [\[eq:u-plus-v\]](#eq:u-plus-v){reference-type="eqref" reference="eq:u-plus-v"}, so its restriction lies in $\operatorname{im}\Phi_r$. Conversely, potentials on the used vertices extend to all row and column indices by assigning arbitrary values to unused vertices. Formula [\[eq:u-plus-v\]](#eq:u-plus-v){reference-type="eqref" reference="eq:u-plus-v"} then gives a global solution with the prescribed edge labels. This proves the image statement.

On one connected component of $G_r$, a kernel vector satisfies $u_i=-v_j$ on every edge. Connectivity forces all row potentials to equal one scalar $t$ and all column potentials to equal $-t$. Each component therefore contributes one kernel dimension. Rank--nullity proves [\[eq:potential-rank\]](#eq:potential-rank){reference-type="eqref" reference="eq:potential-rank"}.

Distinct root components use disjoint potential variables. Adding the ranks in proves the dimension and count in . We record the complete compatibility description because it also identifies the matroid.

Orient every edge of $G_r$ from its row endpoint to its column endpoint and replace $v_j$ by $-w_j$. Then $$\Phi_r(u,v)_{(i,j)}=u_i-w_j,$$ so, up to a sign change on one vertex class, $\Phi_r$ is the graph coboundary map. Write a simple graph cycle as $$\label{eq:cycle-form}
 (i_1,j_1),(i_2,j_1),(i_2,j_2),\ldots,
 (i_k,j_k),(i_1,j_k).$$ Set $i_{k+1}=i_1$. Its alternating edge sum is $$\label{eq:cycle-equation}
 \sum_{\ell=1}^{k}
 \bigl(z_{i_\ell,j_\ell}-z_{i_{\ell+1},j_\ell}\bigr)=0.$$ In characteristic two all signs coincide, and the equation is unchanged as a field identity.

[\[prop:cycle-complete\]]{#prop:cycle-complete label="prop:cycle-complete"} An edge labelling $z\in\mathbb F_q^{E_r}$ lies in $\operatorname{im}\Phi_r$ if and only if [\[eq:cycle-equation\]](#eq:cycle-equation){reference-type="eqref" reference="eq:cycle-equation"} holds for every simple cycle of $G_r$. It suffices to check the fundamental cycles relative to any spanning forest.

For a potential labelling, the alternating sum telescopes, proving necessity. For sufficiency, choose a spanning forest and one base vertex in each component. Assign potential zero at each base vertex and integrate the edge labels along the unique forest paths. A nonforest edge closes a fundamental cycle. Its cycle equation says exactly that the two integrated endpoint potentials reproduce its label. Hence the constructed potentials reproduce all edge labels.

[\[cor:graphic-matroid\]]{#cor:graphic-matroid label="cor:graphic-matroid"} The vector matroid of the restricted evaluation maps $\{\epsilon_n:n\in F\}$ is $$\label{eq:matroid-direct-sum}
 \bigoplus_r M(G_r(F)),$$ the direct sum of the graphic matroids of the root-wise incidence graphs. In particular, a subset of coordinates is linearly independent exactly when its root-wise edge sets are forests. Moreover, $$\label{eq:cycle-codimension}
 \dim\operatorname{proj}_F(X_{a,b})=d(F),
 \qquad
 \operatorname{codim}\operatorname{proj}_F(X_{a,b})=\beta(F).$$

With potentials as columns and edge values as rows, the rows of the matrix in [\[eq:potential-map\]](#eq:potential-map){reference-type="eqref" reference="eq:potential-map"} represent the evaluation maps $\epsilon_n$ on the finite potential space. After the column-vertex sign change, those rows are the columns of an oriented vertex--edge incidence matrix after transposition. Its column matroid is the graphic matroid [@Whitney1935]. This representation remains valid in characteristic two, where the two incidence signs coincide. Roots give block-diagonal matrices and hence the direct sum. A graphic-matroid basis is a maximal spanning forest, and the codimension identity is the Euler formula $|E|-|V|+c$ summed over roots.

We next convert this rank statement into an exact dependence statement. Let $\mu$ be normalized Haar measure on the compact abelian group $X_{a,b}$. For a finite random vector $Z_F=(x_n)_{n\in F}$, define its total correlation in the standard multivariate-information sense [@Watanabe1960] by $$\label{eq:total-correlation-definition}
 \operatorname{TC}_\mu(Z_F)=\sum_{n\in F}\operatorname{H}_\mu(x_n)-\operatorname{H}_\mu(Z_F),$$ with natural logarithms.

[\[prop:haar\]]{#prop:haar label="prop:haar"} For every finite $F\subset\mathbb N$, the Haar projection to $F$ is uniform on $\operatorname{proj}_F(X_{a,b})$ and $$\label{eq:haar-formulas}
 \operatorname{H}_\mu(Z_F)=d(F)\log q,
 \qquad
 \operatorname{TC}_\mu(Z_F)=\beta(F)\log q.$$ The coordinates in $F$ are jointly independent if and only if every $G_r(F)$ is a forest. Every pair of distinct coordinates is independent.

The projection from $X_{a,b}$ onto its finite image is a continuous surjective group homomorphism. It sends Haar measure to Haar measure on the finite image, which is normalized counting measure. The joint entropy is therefore the logarithm of the image size, namely $d(F)\log q$.

Each single coordinate projection is all of $\mathbb F_q$, so every marginal entropy is $\log q$. Subtracting the joint entropy and using $|F|-d(F)=\beta(F)$ proves [\[eq:haar-formulas\]](#eq:haar-formulas){reference-type="eqref" reference="eq:haar-formulas"}. Joint independence is equivalent to equality between joint entropy and the sum of marginal entropies, hence to $\beta(F)=0$, which is exactly the forest condition. Finally, two distinct arithmetic coordinates produce two distinct edges in simple bipartite graphs, possibly in different root components. Two such edges form a forest.

[\[ex:plaquette\]]{#ex:plaquette label="ex:plaquette"} For $$F=\{r,ra,rb,rab\},$$ the graph is $K_{2,2}$. Every proper edge subset is a forest, but the four coordinates obey $$x_r-x_{ra}-x_{rb}+x_{rab}=0.$$ Thus the four coordinates have joint entropy $3\log q$ and total correlation $\log q$, although every distinct pair is independent. Larger finite shapes replace this single plaquette by a cycle basis; no compatibility outside the finite incidence graph is hidden in the global extension problem.

# Arithmetic prefixes {#sec:prefixes}

Let $[L]=\{1,\ldots,L\}$. The global free-axis coordinates immediately give the exact prefix law, including extension to a full point.

[\[prop:prefix-count\]]{#prop:prefix-count label="prop:prefix-count"} For every $L\geq1$, $$\label{eq:prefix-count}
 \left|\operatorname{proj}_{[L]}(X_{a,b})\right|
 =q^{L-\lfloor L/(ab)\rfloor}.$$ Equivalently, $$\label{eq:prefix-dimension}
 \dim_{\mathbb F_q}\operatorname{proj}_{[L]}(X_{a,b})
 =L-\left\lfloor\frac{L}{ab}\right\rfloor.$$

The free indices in the prefix are $$\mathcal B\cap[L]=\{n\leq L:ab\nmid n\},$$ whose cardinality is $L-\lfloor L/(ab)\rfloor$. Every coordinate at most $L$ is determined by these free values: if $n=r a^i b^j\leq L$, then the three indices $r a^i$, $r b^j$, and $r$ in [\[eq:inverse-map\]](#eq:inverse-map){reference-type="eqref" reference="eq:inverse-map"} are all at most $n$.

Conversely, every assignment on $\mathcal B\cap[L]$ occurs in a global point. Extend it arbitrarily, for example by zero, to all of $\mathcal B$ and apply . Restriction from the prefix pattern set to $\mathcal B\cap[L]$ is therefore a bijection. Counting its assignments proves [\[eq:prefix-count\]](#eq:prefix-count){reference-type="eqref" reference="eq:prefix-count"}.

There is also an independent check of the rank of the internally visible constraint matrix. The identification of its kernel with the actual prefix projection still uses the global extension established in ; the pivot computation below is not, by itself, an extension theorem. The constraints visible inside $[L]$ are indexed by $1\leq n\leq\lfloor L/(ab)\rfloor$. Each has the form $$\label{eq:prefix-row}
 x_n-x_{an}-x_{bn}+x_{abn}=0.$$

[\[lem:prefix-pivots\]]{#lem:prefix-pivots label="lem:prefix-pivots"} The rows [\[eq:prefix-row\]](#eq:prefix-row){reference-type="eqref" reference="eq:prefix-row"}, for $n\leq\lfloor L/(ab)\rfloor$, are linearly independent over every field. Their rank is $\lfloor L/(ab)\rfloor$.

Suppose that a nontrivial linear combination vanishes and choose the largest index $n$ with nonzero row coefficient. The coordinate $abn$ appears in the row indexed by $n$ with coefficient one. If it appears in another row indexed by $m$, then one of $$m=abn,\qquad am=abn,\qquad bm=abn,\qquad abm=abn$$ holds. Apart from $m=n$ in the last equality, each possible $m$ is larger than $n$. All such row coefficients vanish by maximality. The coefficient of $x_{abn}$ in the linear combination is therefore the nonzero coefficient of the $n$th row, a contradiction.

The pivot proof shows that the local constraint matrix has exactly one independent row for each multiple of $ab$. Together with the extension and dimension results in , this confirms that there are no further prefix relations. In the graph language it gives the identity $$\label{eq:prefix-cycle-rank}
 \beta([L])=\left\lfloor\frac{L}{ab}\right\rfloor.$$ Thus the same number is the codimension of the prefix projection and the total root-wise cycle rank of its incidence graphs.

[\[def:prefix-complexity\]]{#def:prefix-complexity label="def:prefix-complexity"} Define $$h_{\mathrm{pref}}(X_{a,b})
 =\lim_{L\to\infty}\frac1L
 \log|\operatorname{proj}_{[L]}(X_{a,b})|.$$

[\[cor:prefix-rate\]]{#cor:prefix-rate label="cor:prefix-rate"} The limit in exists and equals $$\label{eq:prefix-rate}
 h_{\mathrm{pref}}(X_{a,b})
 =\left(1-\frac1{ab}\right)\log q.$$

Divide [\[eq:prefix-count\]](#eq:prefix-count){reference-type="eqref" reference="eq:prefix-count"} by $L$ on the logarithmic scale and let $L\to\infty$.

[\[rem:prefix-not-entropy\]]{#rem:prefix-not-entropy label="rem:prefix-not-entropy"} The sets $[L]$ are arithmetic intervals, not a declared Følner sequence for the multiplicative semigroup acting by decimations. Accordingly, [\[eq:prefix-rate\]](#eq:prefix-rate){reference-type="eqref" reference="eq:prefix-rate"} is a prefix pattern-growth invariant. No topological or measure entropy for a multiplicative action is inferred from it.

# Exponent rectangles and boundary laws {#sec:rectangles}

Arithmetic prefixes intersect many root components irregularly. An exponent rectangle instead stays inside one component and retains a Cartesian set of valuation coordinates. Fix $r\in\mathcal R_{a,b}$ and define $$\label{eq:rectangle}
 Q_r(M,N)=\{r a^i b^j:0\leq i<M,\ 0\leq j<N\},
 \qquad M,N\geq1.$$

[\[prop:rectangle\]]{#prop:rectangle label="prop:rectangle"} For every $M,N\geq1$, $$\begin{aligned}
 \dim\operatorname{proj}_{Q_r(M,N)}(X_{a,b})&=M+N-1,
 \label{eq:rectangle-dimension}\\
 |\operatorname{proj}_{Q_r(M,N)}(X_{a,b})|&=q^{M+N-1},
 \label{eq:rectangle-count}\\
 \beta(Q_r(M,N))&=(M-1)(N-1).
 \label{eq:rectangle-beta}\end{aligned}$$ Under normalized Haar measure, $$\label{eq:rectangle-haar}
 \operatorname{H}_\mu(Z_{Q_r(M,N)})=(M+N-1)\log q,
 \qquad
 \operatorname{TC}_\mu(Z_{Q_r(M,N)})=(M-1)(N-1)\log q.$$

The graph $G_r(Q_r(M,N))$ contains all edges between its $M$ row vertices and $N$ column vertices. It is the connected complete bipartite graph $K_{M,N}$. Its graphic rank is $M+N-1$, while its cycle rank is $$MN-(M+N)+1=(M-1)(N-1).$$ Apply .

The pattern exponent has boundary rather than area order: $$\label{eq:rectangle-area-rate}
 \frac{1}{MN}\log|\operatorname{proj}_{Q_r(M,N)}(X_{a,b})|
 =\frac{M+N-1}{MN}\log q.$$ In particular, [\[eq:rectangle-area-rate\]](#eq:rectangle-area-rate){reference-type="eqref" reference="eq:rectangle-area-rate"} tends to zero whenever both $M$ and $N$ diverge. This vanishing reflects the factorization into row and column potentials. It does not contradict the positive arithmetic-prefix rate in [\[eq:prefix-rate\]](#eq:prefix-rate){reference-type="eqref" reference="eq:prefix-rate"}; the two sequences sample different portions of the product coordinates.

[\[cor:root-rectangles\]]{#cor:root-rectangles label="cor:root-rectangles"} Let $r_1,\ldots,r_s$ be distinct roots and let $$F=\bigsqcup_{t=1}^s Q_{r_t}(M_t,N_t).$$ Then $$\begin{aligned}
 \dim\operatorname{proj}_F(X_{a,b})
 &=\sum_{t=1}^s(M_t+N_t-1),\
 \beta(F)&=\sum_{t=1}^s(M_t-1)(N_t-1).\end{aligned}$$ The corresponding Haar random vectors are independent across the roots.

Distinct roots belong to distinct factors in the product [\[eq:global-product\]](#eq:global-product){reference-type="eqref" reference="eq:global-product"}. Their incidence matrices and finite Haar images form direct products, so dimensions, cycle ranks, and entropies add.

The same calculation applies to nonrectangular shapes without new extension arguments. We make the one-edge law explicit.

[\[cor:edge-update\]]{#cor:edge-update label="cor:edge-update"} Let $F\subset\mathbb N$ be finite. If $n\in F$ and its edge lies on a cycle of its root graph, then $$d(F\setminus\{n\})=d(F),\qquad
 \beta(F\setminus\{n\})=\beta(F)-1.$$ If that edge is a bridge, then $$d(F\setminus\{n\})=d(F)-1,\qquad
 \beta(F\setminus\{n\})=\beta(F).$$ Conversely, let $n=r a^i b^j\notin F$. If its two endpoints already lie in the same connected component of $G_r(F)$, then adjoining $n$ preserves $d$ and increases $\beta$ by one. In every other case, adjoining $n$ increases $d$ by one and preserves $\beta$.

An edge on a cycle is dependent on the remaining cycle edges, so its deletion preserves rank; a bridge belongs to every maximal spanning forest, so its deletion lowers rank by one. The deletion formulas for $\beta=|F|-d$ follow. An added edge is dependent exactly when its endpoints were already connected. This proves the two addition formulas.

Thus the arbitrary-shape theorem records more than the number of rows and columns: it tracks precisely which missing cells destroy which dependencies.

@\>p.18 \>p.22 \>p.19 \>p.18Y@ Finite set & Incidence graph & Projection dimension & Cycle defect & Reading\
arbitrary $F$ & root-wise $G_r(F)$ & $\sum_r(|I_r|+|J_r|-c_r)$ & $\sum_r\beta_1(G_r)$ & exact finite-shape rank\
prefix $[L]$ & irregular union over roots & $L-\lfloor L/(ab)\rfloor$ & $\lfloor L/(ab)\rfloor$ & divide log count by $L$\
rectangle $Q_r(M,N)$ & $K_{M,N}$ & $M+N-1$ & $(M-1)(N-1)$ & area-normalized rate tends to zero\

# Comparison, scope, and controls {#sec:scope}

The finite-shape theorem sits at the intersection of several established frameworks, so its claim boundary matters as much as its calculation.

#### Multiplicative symbolic systems.

Kenyon, Peres, and Solomyak established a foundational setting for symbolic spaces invariant under multiplication and developed dimension formulas and a variational principle [@KenyonPeresSolomyak2012]. Ban, Hu, and Lin subsequently studied pattern generation, spatial entropy, and Minkowski dimensions for multiplicative systems [@BanHuLin2019]. Closely related two-generator dimension questions for the semigroup generated by $2$ and $3$ were studied by Peres, Schmeling, Seuret, and Solomyak [@PeresSchmelingSeuretSolomyak2014]. These works provide the established setting for the present problem. We use that setting, not their dimension or entropy machinery: the finite-field space here is solved by an explicit linear parameterization.

Ban, Hu, Lai, and Liao compute Hausdorff and Minkowski dimensions for affine multiplicative shifts whose constraints couple shifted indices of the forms $pk+a$ and $qk+b$ [@BanHuLaiLiaoAffine2025]. That affine index geometry is a direct multiplicative-shift neighbor, but it neither imposes the mixed plaquette difference in [\[eq:def-X\]](#eq:def-X){reference-type="eqref" reference="eq:def-X"} nor identifies the globally extendable patterns on arbitrary finite coordinate sets.

#### Coupled and axial-product entropy.

Ban, Hu, and Lai study entropy formulas for multidimensional multiplicative integer subshifts with coupling constraints [@BanHuLai2021]. Ban, Hu, Lai, and Liao calculate entropy and surface entropy for axial products of subshifts and multiplicative subshifts [@BanHuLaiLiao2025]. Those results provide broad entropy and surface-complexity context. Our rectangle formula is called a boundary law only as an exact count; it is not presented as a new general surface-entropy theorem.

#### Valuation coordinates and correlations.

Mora Cuellar, Rojas Aravena, and Yavicoli use prime-valuation coordinates to derive additive and multiplicative density statements, exact finite-coordinate correlations, random models, and symbolic realizations [@MoraCuellarRojasAravenaYavicoli2026]. Their work is the closest current source for valuation-coordinate correlations. The present Haar calculation concerns a different object: a finite-field linear plaquette constraint whose arbitrary coordinate dependence is represented by root-wise graphic matroids.

#### Matroid and information-theoretic ingredients.

The linear-dependence language follows Whitney's matroid framework [@Whitney1935], and total correlation is the multivariate entropy deficit introduced by Watanabe [@Watanabe1960]. Király, Rosen, and Theran study algebraic matroids and matroids with row--column graph symmetry, motivated in part by matrix completion and rigidity [@KiralyRosenTheran2013]. Their framework owns the graph-symmetric matroid neighborhood, but not the arithmetic evaluation matroid of [\[eq:def-X\]](#eq:def-X){reference-type="eqref" reference="eq:def-X"}. Abbe and Spirkl record the general mechanism by which a finite-field representable matroid is realized by an entropy-rank function under uniform linear random variables [@AbbeSpirkl2019]. Thus neither incidence-matroid language nor the general linear entropy-rank mechanism is claimed here.

The identity $y_{i,j}=u_i+v_j$ is likewise an elementary integration of a factorized mixed difference. After these owners are subtracted, the residual P67 statement is the explicit global free-axis homeomorphism for [\[eq:def-X\]](#eq:def-X){reference-type="eqref" reference="eq:def-X"}, the identification of every globally extendable finite projection with the direct sum of the particular graphic matroids $M(G_r(F))$, and the resulting prefix, rectangle, and Haar forest/cycle formulas.

#### Bounded exact-neighbor search.

An exact-string and citing-neighborhood search frozen on 26 August 2026 covered the displayed equation, sign and function-notation variants, "multiplicative plaquette," finite-field linear multiplicative subshifts, the representation $u_i+v_j$, factorized $(1-u)(1-v)$ constraints, and graph-rank/matroid/correlation formulations. It recovered the context cluster above, including the affine-shift, entropic-matroid, and graph-symmetric-matroid neighbors, but no source stating the same equation together with the global free-axis homeomorphism and the all-finite-shape graphic-matroid theorem. This is recorded only as `BOUNDED_NO_EXACT_COLLISION_LOCATED`. Search vocabulary may differ, folklore may exist, and no worldwide novelty conclusion follows.

@\>p.39 \>p.18Y@ Statement & Status & Reason\
$X_{a,b}\cong\mathbb F_q^{\{n:ab\nmid n\}}$ & proved & explicit continuous inverse\
every finite projection has the graph-rank and cycle-space description & proved & potential-map rank and spanning-forest integration\
Haar finite families are independent exactly on forests & proved & uniform finite Haar image and entropy equality\
prefix complexity is $(1-1/(ab))\log q$ & proved & exact arithmetic-prefix count\
exponent rectangles have area-normalized rate zero & proved & exact $q^{M+N-1}$ count\
either rate is a multiplicative Følner entropy & not asserted & no such averaging sequence is selected here\
Haar measure is mixing or ergodic for every decimation action & not asserted & finite-coordinate Haar dependence alone does not prove it\
the theorem is the first result of its kind & not claimed & bounded search cannot certify priority\

#### Deterministic controls.

The companion standard-library Python program checks root coordinates, global reconstruction, prefix ranks, every subset of $[12]$ in three finite-field/multiplier cases, exponent rectangles through side length six, exact Haar potential counts in characteristics $2$, $3$, and $5$, and the edge-deletion/addition rank dichotomy. A separate exact-arithmetic branch over the nonprime extension field $\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)$ checks prefix ranks, every subset of $[12]$, rectangles through side length six, and Haar forest/cycle counts. These checks exercise composite coprime multipliers, the characteristic-two sign convention, and an extension field rather than only prime fields. They are regression evidence only; none replaces .

The structural rank theorem itself works over any field. Finiteness of $\mathbb F_q$ enters only when rank is converted into pattern count and Shannon entropy. Extending the arithmetic decomposition to noncoprime multipliers is a separate problem, as is computing a dynamical entropy after choosing a specific multiplicative action and Følner sequence.

# Conclusion

The multiplicative plaquette rule has a global set of free coordinates: on each root component, the two exponent axes determine the entire array, and across all roots these axes are exactly the arithmetic indices not divisible by $ab$. This gives a concrete product homeomorphism rather than only a finite-rank count.

The arbitrary finite-shape theorem adds the missing local organization. Selected coordinates become edges of root-wise bipartite graphs, allowed labels are vertex-potential coboundaries, and graph cycles are the complete compatibility obstruction. As a result, the coordinate matroid is graphic and normalized Haar dependence is exact: forests give joint independence, while each cycle-rank unit contributes $\log q$ of total correlation. The pairwise-independent but plaquette-dependent four-corner example is the smallest instance of this rule.

Arithmetic prefixes and exponent rectangles are therefore not isolated formulas. The former have $$q^{L-\lfloor L/(ab)\rfloor}$$ patterns because they retain a positive density of free axes. The latter have $q^{M+N-1}$ patterns because a complete exponent box uses only $M+N-1$ independent vertex potentials. Both follow from the same finite-shape rank, but their normalizations describe different geometries. A separate choice of action and averaging sequence is required before either calculation can be promoted to a dynamical entropy statement.

The manuscript makes no priority claim. Its proof package is closed at the internal-draft level, while external release remains contingent on specialist exact-neighbor review in multiplicative symbolic dynamics, algebraic actions, finite-field coding, and matroidal probability.
