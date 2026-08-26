<!--block:B0001-->
# Introduction

<!--block:B0002-->
Multiplicative symbolic constraints come with more than one natural finite geometry. Arithmetic prefixes retain the indices \(1,\ldots,N\), while prime-valuation or exponent coordinates organize a multiplicative orbit into a lattice. Pattern counts in these geometries need not have the same scale. The difference is structural, not a normalization error.

<!--block:B0003-->
The foundational multiplicative-integer framework and its dimension theory were developed by Kenyon, Peres, and Solomyak \[@KenyonPeresSolomyak2012\]. Two-generator dimension problems and pattern generation for multiplicative systems, as well as coupled multidimensional systems, axial products, surface entropy, and affine multiplicative shifts are treated in \[@PeresSchmelingSeuretSolomyak2014; @BanHuLin2019; @BanHuLai2021; @BanHuLaiLiao2025; @BanHuLaiLiaoAffine2025\]. Prime-valuation coordinates also support exact density and correlation constructions, including recent symbolic realizations \[@MoraCuellarRojasAravenaYavicoli2026\]. Against this established background, we isolate one finite-field linear rule and ask for an exact answer on *every* finite coordinate set.

<!--block:B0004-->
Fix coprime integers \(a,b\geq2\) and a finite field \(\F_q\). On \(\F_q^{\N}\) define \[\label{eq:def-X}
 X_{a,b}=\left\{x:
 x_n-x_{an}-x_{bn}+x_{abn}=0
 \text{ for every }n\in\N\right\}.\] For \(c\in\N\), the decimation \(D_c(x)_n=x_{cn}\) preserves \(X_{a,b}\), so [\[eq:def-X\]](#eq:def-X) is a compact linear multiplicative system. The local rule factors into two first differences after multiplicative coordinates are introduced. That elementary observation is only the starting point: the main result identifies the full finite-projection matroid.

<!--block:B0005-->
Every \(n\in\N\) can be written uniquely as \[n=r a^i b^j,
 \qquad i,j\in\Nzero,
 \qquad a\nmid r,\quad b\nmid r.\] For a finite \(F\subset\N\) and a fixed root \(r\), let \[E_r(F)=\{(i,j):r a^i b^j\in F\}.\] Make a bipartite graph \(G_r(F)\) whose row vertices are the \(i\)’s occurring in \(E_r(F)\), whose column vertices are the \(j\)’s occurring there, and whose edges are the pairs in \(E_r(F)\). Write \(I_r(F)\) and \(J_r(F)\) for its two vertex classes and \(c_r(F)\) for its number of connected components. Empty graphs are omitted. Define \[\begin{aligned}
 d(F)&=\sum_r\bigl(|I_r(F)|+|J_r(F)|-c_r(F)\bigr),
 \label{eq:dF}\\
 \beta(F)&=\sum_r\bigl(|E_r(F)|-|I_r(F)|-|J_r(F)|+c_r(F)\bigr).
 \label{eq:betaF}\end{aligned}\] Thus \(d(F)+\beta(F)=|F|\), and \(\beta(F)\) is the sum of the graph cycle ranks. For precision, the *coordinate-dependence matroid on \(F\)* below is the vector matroid of the evaluation maps \[\epsilon_n:X_{a,b}\longrightarrow\F_q,
 \qquad \epsilon_n(x)=x_n,\qquad n\in F.\] Thus \(A\subseteq F\) is independent when the functionals \(\{\epsilon_n:n\in A\}\) are linearly independent. This is the standard linear-dependence meaning of matroid terminology \[@Whitney1935\].

<!--block:B0006-->
\[thm:main\] Let \(a,b\geq2\) be coprime and let \(\F_q\) be a finite field.

<!--block:B0007-->
1.  Put \(\cB=\{n\in\N:ab\nmid n\}\). Coordinate restriction is a topological-group isomorphism \[X_{a,b}\longrightarrow\F_q^{\cB}.\] Its inverse is explicit: if \(n=r a^i b^j\), then \[\label{eq:global-inverse-intro}
     x_{r a^i b^j}=x_{r a^i}+x_{r b^j}-x_r.\]

2.  For every finite \(F\subset\N\), the image \(\proj_F(X_{a,b})\) is a linear subspace of dimension \(d(F)\). Hence \[\label{eq:finite-count-intro}
     |\proj_F(X_{a,b})|=q^{d(F)}.\] The coordinate-dependence matroid is the direct sum over \(r\) of the graphic matroids of \(G_r(F)\). Equivalently, allowed labels are exactly those whose alternating sum vanishes on every graph cycle.

3.  Let \(\mu\) be normalized Haar measure on \(X_{a,b}\). Then \[\label{eq:haar-intro}
     \Ent_\mu(Z_F)=d(F)\log q,
     \qquad
     \TC_\mu(Z_F)=\beta(F)\log q,
     \qquad Z_F=(x_n)_{n\in F}.\] The coordinates in \(F\) are jointly independent if and only if every \(G_r(F)\) is a forest. In particular, every two distinct coordinates are independent.

<!--block:B0008-->
The theorem unifies two counts that look incompatible when stated alone.

<!--block:B0009-->
\[cor:two-geometries\] For every \(L\geq1\), \[\label{eq:prefix-count-intro}
<!--block:B0010-->
 |\proj_{\{1,\ldots,L\}}(X_{a,b})|
<!--block:B0011-->
 =q^{L-\lfloor L/(ab)\rfloor}.\] For a root \(r\) and \(M,N\geq1\), put \[Q_r(M,N)=\{r a^i b^j:0\leq i<M,\ 0\leq j<N\}.\] Then \[\label{eq:rectangle-count-intro}
<!--block:B0012-->
 |\proj_{Q_r(M,N)}(X_{a,b})|=q^{M+N-1},
<!--block:B0013-->
 \qquad
 \beta(Q_r(M,N))=(M-1)(N-1).\]

<!--block:B0014-->
The first exponent in [\[eq:prefix-count-intro\]](#eq:prefix-count-intro) has positive density in the arithmetic interval. The second is boundary order in the exponent box. We call the former an arithmetic-prefix complexity and the latter an exact exponent-box boundary law. Neither phrase silently selects a Følner sequence or asserts a topological entropy for the multiplicative action.

<!--block:B0015-->
The proof has three short layers. First, the multiplicative root decomposition turns [\[eq:def-X\]](#eq:def-X) into a vanishing mixed difference on \(\Nzero^2\), whose solutions are sums of one row and one column potential. Second, restriction to an arbitrary finite set becomes a vertex-potential map on \(G_r(F)\); its rank and its cycle conditions are the standard incidence rank and cycle space. Third, Haar measure pushes forward uniformly to every finite image, converting rank and cycle rank into exact entropy and total correlation.

<!--block:B0016-->
#### Organization.

<!--block:B0017-->
proves the global coordinates and product homeomorphism. proves the all-finite-shape rank, cycle, and Haar statements. specialize the formula to the two geometries. records the literature context and the claim boundary.

<!--block:B0018-->
# Multiplicative components and global coordinates

<!--block:B0019-->
Write \[\cR_{a,b}=\{r\in\N:a\nmid r,\ b\nmid r\}.\] The coprimality assumption gives a coordinate system adapted to both multipliers.

<!--block:B0020-->
\[lem:root-decomposition\] The map \[\cR_{a,b}\times\Nzero^2\longrightarrow\N,
 \qquad (r,i,j)\longmapsto r a^i b^j,\] is a bijection.

<!--block:B0021-->
For \(n\in\N\), let \(i\) be maximal with \(a^i\mid n\) and let \(j\) be maximal with \(b^j\mid n\). Since \(a\) and \(b\) are coprime, \(a^i b^j\mid n\). The integer \(r=n/(a^i b^j)\) is divisible by neither \(a\) nor \(b\), by maximality.

<!--block:B0022-->
Conversely, suppose \(n=r a^i b^j\) with \(r\in\cR_{a,b}\). The factor \(r b^j\) is not divisible by \(a\): otherwise \(\gcd(a,b^j)=1\) would imply \(a\mid r\). Hence \(i\) is the maximal exponent of a power of \(a\) dividing \(n\). The same argument identifies \(j\) as the maximal \(b\)-exponent. Both exponents and then \(r\) are unique.

<!--block:B0023-->
For \(x\in\F_q^{\N}\) and \(r\in\cR_{a,b}\), set \[y^{(r)}_{i,j}=x_{r a^i b^j},
 \qquad (i,j)\in\Nzero^2.\] The equation defining \(X_{a,b}\) becomes \[\label{eq:mixed-difference}
 y_{i,j}-y_{i+1,j}-y_{i,j+1}+y_{i+1,j+1}=0.\] We omit the root superscript while studying one component.

<!--block:B0024-->
\[lem:integrate\] An array \(y\in\F_q^{\Nzero^2}\) satisfies [\[eq:mixed-difference\]](#eq:mixed-difference) for all \(i,j\geq0\) if and only if \[\label{eq:integrated}
 y_{i,j}=y_{i,0}+y_{0,j}-y_{0,0}
 \qquad(i,j\geq0).\] Equivalently, after the gauge choice \(v_0=0\), it has the unique form \[\label{eq:u-plus-v}
 y_{i,j}=u_i+v_j,
 \qquad
 u_i=y_{i,0},\quad v_j=y_{0,j}-y_{0,0}.\]

<!--block:B0025-->
Rearranging [\[eq:mixed-difference\]](#eq:mixed-difference) gives \[y_{i+1,j+1}-y_{i,j+1}=y_{i+1,j}-y_{i,j}.\] Thus the horizontal increment from row \(i\) to row \(i+1\) is independent of the column. Summing these increments from \(0\) to \(i-1\) yields \(y_{i,j}-y_{0,j}=y_{i,0}-y_{0,0}\), which is [\[eq:integrated\]](#eq:integrated). Direct substitution proves the converse. The gauge formula [\[eq:u-plus-v\]](#eq:u-plus-v) follows immediately and remains valid in characteristic two.

<!--block:B0026-->
The component solution group is therefore explicitly isomorphic to \[\cY\cong \F_q^{\Nzero}\times\F_q^{\N},\] where the two factors record the full row axis and the positive column axis. The next proposition identifies these axes directly in the arithmetic index set.

<!--block:B0027-->
\[prop:global-homeo\] Let \[\cB=\{n\in\N:ab\nmid n\}.\] The restriction map \[\label{eq:restriction-map}
 \rho_{\cB}:X_{a,b}\longrightarrow\F_q^{\cB},
 \qquad x\longmapsto x|_{\cB},\] is a topological-group isomorphism. If \(n=r a^i b^j\) is its root representation, the inverse map is \[\label{eq:inverse-map}
 (\rho_{\cB}^{-1}z)_{r a^i b^j}
 =z_{r a^i}+z_{r b^j}-z_r.\] Consequently, \[\label{eq:global-product}
 X_{a,b}\cong\prod_{r\in\cR_{a,b}}\cY
 \cong\F_q^{\cB}.\]

<!--block:B0028-->
For \(n=r a^i b^j\), the product \(ab\) divides \(n\) exactly when \(i,j\geq1\). The forward implication uses coprimality: if \(i=0\) and \(a\mid r b^j\), then \(a\mid r\), contrary to \(r\in\cR_{a,b}\); the case \(j=0\) is symmetric. Thus \(\cB\) is precisely the union of the two axes in every root component, with the origin counted once.

<!--block:B0029-->
By , those axes determine every point of \(X_{a,b}\), so [\[eq:restriction-map\]](#eq:restriction-map) is injective. Conversely, for arbitrary \(z\in\F_q^{\cB}\), formula [\[eq:inverse-map\]](#eq:inverse-map) is defined because all three indices on its right lie in \(\cB\). It agrees with \(z\) on either axis and satisfies every plaquette equation by . Hence restriction is surjective.

<!--block:B0030-->
Both maps are homomorphisms. Restriction is continuous, and each coordinate of its inverse depends on only three coordinates of \(z\). The inverse is therefore continuous in the product topology. The component product description follows from .

<!--block:B0031-->
\[rem:coprime\] The proof uses \(\gcd(a,b)=1\) twice: to split divisibility exponents and to identify the free axes with \(ab\nmid n\). When the multipliers share a factor, the exponent coordinates can have multiple presentations, so is not asserted.

<!--block:B0032-->
# Finite projections and graphic matroids

<!--block:B0033-->
The product homeomorphism solves global extension, but it does not by itself display the dependence among an arbitrary selection of non-axis coordinates. The right finite object is the bipartite graph introduced before .

<!--block:B0034-->
Fix a finite \(F\subset\N\). For each root \(r\) occurring in \(F\), write \[E_r=E_r(F),\qquad I_r=I_r(F),\qquad J_r=J_r(F),
 \qquad G_r=G_r(F).\] Regard \(I_r\) and \(J_r\) as disjoint vertex classes even if the same integer appears in both. Define the vertex-potential map \[\label{eq:potential-map}
 \Phi_r:\F_q^{I_r}\oplus\F_q^{J_r}\longrightarrow\F_q^{E_r},
 \qquad
 \Phi_r(u,v)_{(i,j)}=u_i+v_j.\]

<!--block:B0035-->
\[lem:potential-rank\] The image of \(\Phi_r\) is exactly the restriction to \(E_r\) of all global solutions of [\[eq:mixed-difference\]](#eq:mixed-difference), and \[\label{eq:potential-rank}
 \rank\Phi_r=|I_r|+|J_r|-c_r.\]

<!--block:B0036-->
Every global component solution has the potential form [\[eq:u-plus-v\]](#eq:u-plus-v), so its restriction lies in \(\im\Phi_r\). Conversely, potentials on the used vertices extend to all row and column indices by assigning arbitrary values to unused vertices. Formula [\[eq:u-plus-v\]](#eq:u-plus-v) then gives a global solution with the prescribed edge labels. This proves the image statement.

<!--block:B0037-->
On one connected component of \(G_r\), a kernel vector satisfies \(u_i=-v_j\) on every edge. Connectivity forces all row potentials to equal one scalar \(t\) and all column potentials to equal \(-t\). Each component therefore contributes one kernel dimension. Rank–nullity proves [\[eq:potential-rank\]](#eq:potential-rank).

<!--block:B0038-->
Distinct root components use disjoint potential variables. Adding the ranks in proves the dimension and count in . We record the complete compatibility description because it also identifies the matroid.

<!--block:B0039-->
Orient every edge of \(G_r\) from its row endpoint to its column endpoint and replace \(v_j\) by \(-w_j\). Then \[\Phi_r(u,v)_{(i,j)}=u_i-w_j,\] so, up to a sign change on one vertex class, \(\Phi_r\) is the graph coboundary map. Write a simple graph cycle as \[\label{eq:cycle-form}
 (i_1,j_1),(i_2,j_1),(i_2,j_2),\ldots,
 (i_k,j_k),(i_1,j_k).\] Set \(i_{k+1}=i_1\). Its alternating edge sum is \[\label{eq:cycle-equation}
 \sum_{\ell=1}^{k}
 \bigl(z_{i_\ell,j_\ell}-z_{i_{\ell+1},j_\ell}\bigr)=0.\] In characteristic two all signs coincide, and the equation is unchanged as a field identity.

<!--block:B0040-->
\[prop:cycle-complete\] An edge labelling \(z\in\F_q^{E_r}\) lies in \(\im\Phi_r\) if and only if [\[eq:cycle-equation\]](#eq:cycle-equation) holds for every simple cycle of \(G_r\). It suffices to check the fundamental cycles relative to any spanning forest.

<!--block:B0041-->
For a potential labelling, the alternating sum telescopes, proving necessity. For sufficiency, choose a spanning forest and one base vertex in each component. Assign potential zero at each base vertex and integrate the edge labels along the unique forest paths. A nonforest edge closes a fundamental cycle. Its cycle equation says exactly that the two integrated endpoint potentials reproduce its label. Hence the constructed potentials reproduce all edge labels.

<!--block:B0042-->
\[cor:graphic-matroid\] The vector matroid of the restricted evaluation maps \(\{\epsilon_n:n\in F\}\) is \[\label{eq:matroid-direct-sum}
 \bigoplus_r M(G_r(F)),\] the direct sum of the graphic matroids of the root-wise incidence graphs. In particular, a subset of coordinates is linearly independent exactly when its root-wise edge sets are forests. Moreover, \[\label{eq:cycle-codimension}
 \dim\proj_F(X_{a,b})=d(F),
 \qquad
 \operatorname{codim}\proj_F(X_{a,b})=\beta(F).\]

<!--block:B0043-->
With potentials as columns and edge values as rows, the rows of the matrix in [\[eq:potential-map\]](#eq:potential-map) represent the evaluation maps \(\epsilon_n\) on the finite potential space. After the column-vertex sign change, those rows are the columns of an oriented vertex–edge incidence matrix after transposition. Its column matroid is the graphic matroid \[@Whitney1935\]. This representation remains valid in characteristic two, where the two incidence signs coincide. Roots give block-diagonal matrices and hence the direct sum. A graphic-matroid basis is a maximal spanning forest, and the codimension identity is the Euler formula \(|E|-|V|+c\) summed over roots.

<!--block:B0044-->
We next convert this rank statement into an exact dependence statement. Let \(\mu\) be normalized Haar measure on the compact abelian group \(X_{a,b}\). For a finite random vector \(Z_F=(x_n)_{n\in F}\), define its total correlation in the standard multivariate-information sense \[@Watanabe1960\] by \[\label{eq:total-correlation-definition}
 \TC_\mu(Z_F)=\sum_{n\in F}\Ent_\mu(x_n)-\Ent_\mu(Z_F),\] with natural logarithms.

<!--block:B0045-->
\[prop:haar\] For every finite \(F\subset\N\), the Haar projection to \(F\) is uniform on \(\proj_F(X_{a,b})\) and \[\label{eq:haar-formulas}
 \Ent_\mu(Z_F)=d(F)\log q,
 \qquad
 \TC_\mu(Z_F)=\beta(F)\log q.\] The coordinates in \(F\) are jointly independent if and only if every \(G_r(F)\) is a forest. Every pair of distinct coordinates is independent.

<!--block:B0046-->
The projection from \(X_{a,b}\) onto its finite image is a continuous surjective group homomorphism. It sends Haar measure to Haar measure on the finite image, which is normalized counting measure. The joint entropy is therefore the logarithm of the image size, namely \(d(F)\log q\).

<!--block:B0047-->
Each single coordinate projection is all of \(\F_q\), so every marginal entropy is \(\log q\). Subtracting the joint entropy and using \(|F|-d(F)=\beta(F)\) proves [\[eq:haar-formulas\]](#eq:haar-formulas). Joint independence is equivalent to equality between joint entropy and the sum of marginal entropies, hence to \(\beta(F)=0\), which is exactly the forest condition. Finally, two distinct arithmetic coordinates produce two distinct edges in simple bipartite graphs, possibly in different root components. Two such edges form a forest.

<!--block:B0048-->
\[ex:plaquette\] For \[F=\{r,ra,rb,rab\},\] the graph is \(K_{2,2}\). Every proper edge subset is a forest, but the four coordinates obey \[x_r-x_{ra}-x_{rb}+x_{rab}=0.\] Thus the four coordinates have joint entropy \(3\log q\) and total correlation \(\log q\), although every distinct pair is independent. Larger finite shapes replace this single plaquette by a cycle basis; no compatibility outside the finite incidence graph is hidden in the global extension problem.

<!--block:B0049-->
# Arithmetic prefixes

<!--block:B0050-->
Let \([L]=\{1,\ldots,L\}\). The global free-axis coordinates immediately give the exact prefix law, including extension to a full point.

<!--block:B0051-->
\[prop:prefix-count\] For every \(L\geq1\), \[\label{eq:prefix-count}
 \left|\proj_{[L]}(X_{a,b})\right|
 =q^{L-\lfloor L/(ab)\rfloor}.\] Equivalently, \[\label{eq:prefix-dimension}
 \dim_{\F_q}\proj_{[L]}(X_{a,b})
 =L-\left\lfloor\frac{L}{ab}\right\rfloor.\]

<!--block:B0052-->
The free indices in the prefix are \[\cB\cap[L]=\{n\leq L:ab\nmid n\},\] whose cardinality is \(L-\lfloor L/(ab)\rfloor\). Every coordinate at most \(L\) is determined by these free values: if \(n=r a^i b^j\leq L\), then the three indices \(r a^i\), \(r b^j\), and \(r\) in [\[eq:inverse-map\]](#eq:inverse-map) are all at most \(n\).

<!--block:B0053-->
Conversely, every assignment on \(\cB\cap[L]\) occurs in a global point. Extend it arbitrarily, for example by zero, to all of \(\cB\) and apply . Restriction from the prefix pattern set to \(\cB\cap[L]\) is therefore a bijection. Counting its assignments proves [\[eq:prefix-count\]](#eq:prefix-count).

<!--block:B0054-->
There is also an independent check of the rank of the internally visible constraint matrix. The identification of its kernel with the actual prefix projection still uses the global extension established in ; the pivot computation below is not, by itself, an extension theorem. The constraints visible inside \([L]\) are indexed by \(1\leq n\leq\lfloor L/(ab)\rfloor\). Each has the form \[\label{eq:prefix-row}
 x_n-x_{an}-x_{bn}+x_{abn}=0.\]

<!--block:B0055-->
\[lem:prefix-pivots\] The rows [\[eq:prefix-row\]](#eq:prefix-row), for \(n\leq\lfloor L/(ab)\rfloor\), are linearly independent over every field. Their rank is \(\lfloor L/(ab)\rfloor\).

<!--block:B0056-->
Suppose that a nontrivial linear combination vanishes and choose the largest index \(n\) with nonzero row coefficient. The coordinate \(abn\) appears in the row indexed by \(n\) with coefficient one. If it appears in another row indexed by \(m\), then one of \[m=abn,\qquad am=abn,\qquad bm=abn,\qquad abm=abn\] holds. Apart from \(m=n\) in the last equality, each possible \(m\) is larger than \(n\). All such row coefficients vanish by maximality. The coefficient of \(x_{abn}\) in the linear combination is therefore the nonzero coefficient of the \(n\)th row, a contradiction.

<!--block:B0057-->
The pivot proof shows that the local constraint matrix has exactly one independent row for each multiple of \(ab\). Together with the extension and dimension results in , this confirms that there are no further prefix relations. In the graph language it gives the identity \[\label{eq:prefix-cycle-rank}
 \beta([L])=\left\lfloor\frac{L}{ab}\right\rfloor.\] Thus the same number is the codimension of the prefix projection and the total root-wise cycle rank of its incidence graphs.

<!--block:B0058-->
\[def:prefix-complexity\] Define \[h_{\mathrm{pref}}(X_{a,b})
 =\lim_{L\to\infty}\frac1L
 \log|\proj_{[L]}(X_{a,b})|.\]

<!--block:B0059-->
\[cor:prefix-rate\] The limit in exists and equals \[\label{eq:prefix-rate}
 h_{\mathrm{pref}}(X_{a,b})
 =\left(1-\frac1{ab}\right)\log q.\]

<!--block:B0060-->
Divide [\[eq:prefix-count\]](#eq:prefix-count) by \(L\) on the logarithmic scale and let \(L\to\infty\).

<!--block:B0061-->
\[rem:prefix-not-entropy\] The sets \([L]\) are arithmetic intervals, not a declared Følner sequence for the multiplicative semigroup acting by decimations. Accordingly, [\[eq:prefix-rate\]](#eq:prefix-rate) is a prefix pattern-growth invariant. No topological or measure entropy for a multiplicative action is inferred from it.

<!--block:B0062-->
# Exponent rectangles and boundary laws

<!--block:B0063-->
Arithmetic prefixes intersect many root components irregularly. An exponent rectangle instead stays inside one component and retains a Cartesian set of valuation coordinates. Fix \(r\in\cR_{a,b}\) and define \[\label{eq:rectangle}
 Q_r(M,N)=\{r a^i b^j:0\leq i<M,\ 0\leq j<N\},
 \qquad M,N\geq1.\]

<!--block:B0064-->
\[prop:rectangle\] For every \(M,N\geq1\), \[\begin{aligned}
 \dim\proj_{Q_r(M,N)}(X_{a,b})&=M+N-1,
 \label{eq:rectangle-dimension}\\
<!--block:B0065-->
 |\proj_{Q_r(M,N)}(X_{a,b})|&=q^{M+N-1},
<!--block:B0066-->
 \label{eq:rectangle-count}\\
 \beta(Q_r(M,N))&=(M-1)(N-1).
 \label{eq:rectangle-beta}\end{aligned}\] Under normalized Haar measure, \[\label{eq:rectangle-haar}
 \Ent_\mu(Z_{Q_r(M,N)})=(M+N-1)\log q,
 \qquad
 \TC_\mu(Z_{Q_r(M,N)})=(M-1)(N-1)\log q.\]

<!--block:B0067-->
The graph \(G_r(Q_r(M,N))\) contains all edges between its \(M\) row vertices and \(N\) column vertices. It is the connected complete bipartite graph \(K_{M,N}\). Its graphic rank is \(M+N-1\), while its cycle rank is \[MN-(M+N)+1=(M-1)(N-1).\] Apply .

<!--block:B0068-->
The pattern exponent has boundary rather than area order: \[\label{eq:rectangle-area-rate}
 \frac{1}{MN}\log|\proj_{Q_r(M,N)}(X_{a,b})|
 =\frac{M+N-1}{MN}\log q.\] In particular, [\[eq:rectangle-area-rate\]](#eq:rectangle-area-rate) tends to zero whenever both \(M\) and \(N\) diverge. This vanishing reflects the factorization into row and column potentials. It does not contradict the positive arithmetic-prefix rate in [\[eq:prefix-rate\]](#eq:prefix-rate); the two sequences sample different portions of the product coordinates.

<!--block:B0069-->
\[cor:root-rectangles\] Let \(r_1,\ldots,r_s\) be distinct roots and let \[F=\bigsqcup_{t=1}^s Q_{r_t}(M_t,N_t).\] Then \[\begin{aligned}
 \dim\proj_F(X_{a,b})
 &=\sum_{t=1}^s(M_t+N_t-1),\
 \beta(F)&=\sum_{t=1}^s(M_t-1)(N_t-1).\end{aligned}\] The corresponding Haar random vectors are independent across the roots.

<!--block:B0070-->
Distinct roots belong to distinct factors in the product [\[eq:global-product\]](#eq:global-product). Their incidence matrices and finite Haar images form direct products, so dimensions, cycle ranks, and entropies add.

<!--block:B0071-->
The same calculation applies to nonrectangular shapes without new extension arguments. We make the one-edge law explicit.

<!--block:B0072-->
\[cor:edge-update\] Let \(F\subset\N\) be finite. If \(n\in F\) and its edge lies on a cycle of its root graph, then \[d(F\setminus\{n\})=d(F),\qquad
 \beta(F\setminus\{n\})=\beta(F)-1.\] If that edge is a bridge, then \[d(F\setminus\{n\})=d(F)-1,\qquad
 \beta(F\setminus\{n\})=\beta(F).\] Conversely, let \(n=r a^i b^j\notin F\). If its two endpoints already lie in the same connected component of \(G_r(F)\), then adjoining \(n\) preserves \(d\) and increases \(\beta\) by one. In every other case, adjoining \(n\) increases \(d\) by one and preserves \(\beta\).

<!--block:B0073-->
An edge on a cycle is dependent on the remaining cycle edges, so its deletion preserves rank; a bridge belongs to every maximal spanning forest, so its deletion lowers rank by one. The deletion formulas for \(\beta=|F|-d\) follow. An added edge is dependent exactly when its endpoints were already connected. This proves the two addition formulas.

<!--block:B0074-->
Thus the arbitrary-shape theorem records more than the number of rows and columns: it tracks precisely which missing cells destroy which dependencies.

<!--block:B0075-->
@\>p.18 \>p.22 \>p.19 \>p.18Y@ Finite set & Incidence graph & Projection dimension & Cycle defect & Reading  
arbitrary \(F\) & root-wise \(G_r(F)\) & \(\sum_r(|I_r|+|J_r|-c_r)\) & \(\sum_r\beta_1(G_r)\) & exact finite-shape rank  
prefix \([L]\) & irregular union over roots & \(L-\lfloor L/(ab)\rfloor\) & \(\lfloor L/(ab)\rfloor\) & divide log count by \(L\)  
rectangle \(Q_r(M,N)\) & \(K_{M,N}\) & \(M+N-1\) & \((M-1)(N-1)\) & area-normalized rate tends to zero  

<!--block:B0076-->
# Comparison, scope, and controls

<!--block:B0077-->
The finite-shape theorem sits at the intersection of several established frameworks, so its claim boundary matters as much as its calculation.

<!--block:B0078-->
#### Multiplicative symbolic systems.

<!--block:B0079-->
Kenyon, Peres, and Solomyak established a foundational setting for symbolic spaces invariant under multiplication and developed dimension formulas and a variational principle \[@KenyonPeresSolomyak2012\]. Ban, Hu, and Lin subsequently studied pattern generation, spatial entropy, and Minkowski dimensions for multiplicative systems \[@BanHuLin2019\]. Closely related two-generator dimension questions for the semigroup generated by \(2\) and \(3\) were studied by Peres, Schmeling, Seuret, and Solomyak \[@PeresSchmelingSeuretSolomyak2014\]. These works provide the established setting for the present problem. We use that setting, not their dimension or entropy machinery: the finite-field space here is solved by an explicit linear parameterization.

<!--block:B0080-->
Ban, Hu, Lai, and Liao compute Hausdorff and Minkowski dimensions for affine multiplicative shifts whose constraints couple shifted indices of the forms \(pk+a\) and \(qk+b\) \[@BanHuLaiLiaoAffine2025\]. That affine index geometry is a direct multiplicative-shift neighbor, but it neither imposes the mixed plaquette difference in [\[eq:def-X\]](#eq:def-X) nor identifies the globally extendable patterns on arbitrary finite coordinate sets.

<!--block:B0081-->
#### Coupled and axial-product entropy.

<!--block:B0082-->
Ban, Hu, and Lai study entropy formulas for multidimensional multiplicative integer subshifts with coupling constraints \[@BanHuLai2021\]. Ban, Hu, Lai, and Liao calculate entropy and surface entropy for axial products of subshifts and multiplicative subshifts \[@BanHuLaiLiao2025\]. Those results provide broad entropy and surface-complexity context. Our rectangle formula is called a boundary law only as an exact count; it is not presented as a new general surface-entropy theorem.

<!--block:B0083-->
#### Valuation coordinates and correlations.

<!--block:B0084-->
Mora Cuellar, Rojas Aravena, and Yavicoli use prime-valuation coordinates to derive additive and multiplicative density statements, exact finite-coordinate correlations, random models, and symbolic realizations \[@MoraCuellarRojasAravenaYavicoli2026\]. Their work is the closest current source for valuation-coordinate correlations. The present Haar calculation concerns a different object: a finite-field linear plaquette constraint whose arbitrary coordinate dependence is represented by root-wise graphic matroids.

<!--block:B0085-->
#### Matroid and information-theoretic ingredients.

<!--block:B0086-->
The linear-dependence language follows Whitney’s matroid framework \[@Whitney1935\], and total correlation is the multivariate entropy deficit introduced by Watanabe \[@Watanabe1960\]. Király, Rosen, and Theran study algebraic matroids and matroids with row–column graph symmetry, motivated in part by matrix completion and rigidity \[@KiralyRosenTheran2013\]. Their framework owns the graph-symmetric matroid neighborhood, but not the arithmetic evaluation matroid of [\[eq:def-X\]](#eq:def-X). Abbe and Spirkl record the general mechanism by which a finite-field representable matroid is realized by an entropy-rank function under uniform linear random variables \[@AbbeSpirkl2019\]. Thus neither incidence-matroid language nor the general linear entropy-rank mechanism is claimed here.

<!--block:B0087-->
The identity \(y_{i,j}=u_i+v_j\) is likewise an elementary integration of a factorized mixed difference. After these owners are subtracted, the residual P67 statement is the explicit global free-axis homeomorphism for [\[eq:def-X\]](#eq:def-X), the identification of every globally extendable finite projection with the direct sum of the particular graphic matroids \(M(G_r(F))\), and the resulting prefix, rectangle, and Haar forest/cycle formulas.

<!--block:B0088-->
#### Bounded exact-neighbor search.

<!--block:B0089-->
An exact-string and citing-neighborhood search frozen on 26 August 2026 covered the displayed equation, sign and function-notation variants, “multiplicative plaquette,” finite-field linear multiplicative subshifts, the representation \(u_i+v_j\), factorized \((1-u)(1-v)\) constraints, and graph-rank/matroid/correlation formulations. It recovered the context cluster above, including the affine-shift, entropic-matroid, and graph-symmetric-matroid neighbors, but no source stating the same equation together with the global free-axis homeomorphism and the all-finite-shape graphic-matroid theorem. This is recorded only as `BOUNDED_NO_EXACT_COLLISION_LOCATED`. Search vocabulary may differ, folklore may exist, and no worldwide novelty conclusion follows.

<!--block:B0090-->
@\>p.39 \>p.18Y@ Statement & Status & Reason  
\(X_{a,b}\cong\F_q^{\{n:ab\nmid n\}}\) & proved & explicit continuous inverse  
every finite projection has the graph-rank and cycle-space description & proved & potential-map rank and spanning-forest integration  
Haar finite families are independent exactly on forests & proved & uniform finite Haar image and entropy equality  
prefix complexity is \((1-1/(ab))\log q\) & proved & exact arithmetic-prefix count  
exponent rectangles have area-normalized rate zero & proved & exact \(q^{M+N-1}\) count  
either rate is a multiplicative Følner entropy & not asserted & no such averaging sequence is selected here  
Haar measure is mixing or ergodic for every decimation action & not asserted & finite-coordinate Haar dependence alone does not prove it  
the theorem is the first result of its kind & not claimed & bounded search cannot certify priority  

<!--block:B0091-->
#### Deterministic controls.

<!--block:B0092-->
The companion standard-library Python program checks root coordinates, global reconstruction, prefix ranks, every subset of \([12]\) in three finite-field/multiplier cases, exponent rectangles through side length six, exact Haar potential counts in characteristics \(2\), \(3\), and \(5\), and the edge-deletion/addition rank dichotomy. These checks exercise composite coprime multipliers and the characteristic-two sign convention. They are regression evidence only; none replaces .

<!--block:B0093-->
The structural rank theorem itself works over any field. Finiteness of \(\F_q\) enters only when rank is converted into pattern count and Shannon entropy. Extending the arithmetic decomposition to noncoprime multipliers is a separate problem, as is computing a dynamical entropy after choosing a specific multiplicative action and Følner sequence.

<!--block:B0094-->
# Conclusion

<!--block:B0095-->
The multiplicative plaquette rule has a global set of free coordinates: on each root component, the two exponent axes determine the entire array, and across all roots these axes are exactly the arithmetic indices not divisible by \(ab\). This gives a concrete product homeomorphism rather than only a finite-rank count.

<!--block:B0096-->
The arbitrary finite-shape theorem adds the missing local organization. Selected coordinates become edges of root-wise bipartite graphs, allowed labels are vertex-potential coboundaries, and graph cycles are the complete compatibility obstruction. As a result, the coordinate matroid is graphic and normalized Haar dependence is exact: forests give joint independence, while each cycle-rank unit contributes \(\log q\) of total correlation. The pairwise-independent but plaquette-dependent four-corner example is the smallest instance of this rule.

<!--block:B0097-->
Arithmetic prefixes and exponent rectangles are therefore not isolated formulas. The former have \[q^{L-\lfloor L/(ab)\rfloor}\] patterns because they retain a positive density of free axes. The latter have \(q^{M+N-1}\) patterns because a complete exponent box uses only \(M+N-1\) independent vertex potentials. Both follow from the same finite-shape rank, but their normalizations describe different geometries. A separate choice of action and averaging sequence is required before either calculation can be promoted to a dynamical entropy statement.

<!--block:B0098-->
The manuscript makes no priority claim. Its proof package is closed at the internal-draft level, while external release remains contingent on specialist exact-neighbor review in multiplicative symbolic dynamics, algebraic actions, finite-field coding, and matroidal probability.
