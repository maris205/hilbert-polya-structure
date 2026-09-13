---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-connected-algebraic-z2-resonance-route-a"
canonical_tex: "henon_dynamics/henon_connected_algebraic_z2_resonance_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_connected_algebraic_z2_resonance_route_a/paper/main.pdf"
source_sha256: "44f6754363bdf57d25c33e66076b09b00fb66095a448f4c74ce85aef3f718e03"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Lattice Resonance in a Connected Algebraic Action: Complete Quotients and Continuous Fixed Strata

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_connected_algebraic_z2_resonance_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_connected_algebraic_z2_resonance_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_connected_algebraic_z2_resonance_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_connected_algebraic_z2_resonance_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We reconstruct every finite-index fixed group of the connected algebraic action defined by the integral relation $1+u+v$. A canonical Hermite lattice presentation produces an exact integer convolution matrix, whose Smith factors determine the complete compact-group type. There are exactly two possible Fourier zero modes. They occur precisely when the acting lattice lies in one fixed index-three subgroup; otherwise the fixed group is finite. At resonance the fixed group has a two-dimensional torus factor. We give the full quotient conventions, including coincident neighbors and skew lattices, and distinguish finite cardinality from connected components. This is a source-local reconstruction with direct classical ownership, not a claim to have discovered the resonance condition. No scalar prime-time clock or target determinant is supplied by the quotient atlas. We compute the exact component correction for the resonant fixed groups of the connected algebraic action defined by $1+u+v$. A general integer-image covolume lemma converts the product of nonzero singular values into the torsion order of a cokernel. The saturated two-mode kernel has Gram determinant $N^2/3$ at lattice index $N$, so the nonzero Fourier product must be multiplied by $3/N^2$. The index-three all-ones matrix gives an exact minimal counterexample to the uncorrected finite-lattice formula printed in an explicitly identified arXiv version. This statement does not refute the classical entropy asymptotic or establish the status of later corrigenda. Exact Smith witnesses and characteristic coefficients provide reproducible finite controls for the all-lattice proof. We give an all-lattice reconstruction of the connected algebraic action defined by $1+u+v$, retaining the integer covolumes that distinguish a singular Fourier product from a component count. At index $N$, resonance occurs on one congruence class of Hermite lattices; the fixed group then has a two-torus factor and its component count is $3/N^2$ times the nonzero Fourier product. The smallest resonant quotient yields a version-specific correction to the displayed finite-lattice identity in an accessed preprint. Its two-torus also contains uncountably many primitive three-point orbits, obstructing ordinary orbit-cardinality zeta functions for the rank-two action and every rank-one restriction. In contrast, the classical joint entropy has the Smyth character-modulo-three special value, which we rederive by Jensen and Fourier integration. These statements separate an intrinsic arithmetic scalar from a discrete prime-carrying orbit trace. The source has direct classical owners, and no target divisor or quantum-generator claim follows.
author:
- 'HCS-C388 source-theorem and reproducibility package'
date: 5 September 2026
title:
- 'Lattice Resonance in a Connected Algebraic Action: Complete Quotients and Continuous Fixed Strata'
- 'Lattice Resonance in a Connected Algebraic Action: Integer Covolumes and a Finite-Index Correction'
- 'Lattice Resonance in a Connected Algebraic Action: Exact Components, Arithmetic Entropy and Orbit-Count Failure'
```

## Markdown 正文

=3em

中文摘要

本文重建由整数关系定义的紧连通二维代数作用的全部有限指数固定群。 规范埃尔米特格表示给出精确整数卷积矩阵，其史密斯不变量确定固定群的完整紧群类型。 傅里叶分解中只有两个可能零模；当且仅当作用子格包含于指定的指数三子格时出现共振，固定群因而含二维环面。 非共振情形的固定群有限。本文明确斜子格与重合邻点约定，并区分固定点总数和连通分支数。 这些源系统结论具有直接经典文献归属，不被包装成新发现，也没有提供素数飞行时间或目标行列式。 本文给出上述连通代数作用的共振固定群分支数修正。 一般整数像格的体积引理把非零奇异值乘积转化为余核挠子群的阶。 在指数为正整数的子格上，饱和整数核格的格拉姆行列式精确等于指数平方的三分之一，因此必须加入相应倒数修正。 最小指数三的全一矩阵给出所核对预印本版本中有限格公式的精确反例。 这个局部修正不否定经典熵渐近定理，也不声称已确定后续勘误情况。 完整史密斯证书和特征多项式为全子格证明提供独立有限核验。 本文贯通连通二维代数作用的全部子格固定群、整数核格体积修正和本原轨道计数障碍。 共振时固定群包含二维环面；删掉零特征值并不足以得到分支数，还必须乘以指数平方倒数的三倍。 最小共振商给出所核对预印本有限格公式的版本限定修正，同时承载不可数多个三点本原轨道。 因此二维作用及其每个一维限制的普通逐轨计数函数均在有限阶失去有限系数。 与此并存，经典联合熵具有模三特征的算术特殊值，本文用詹森公式和傅里叶积分重新推导并正面标注文献归属。 算术标量并不是离散素数轨道桥梁；本文不声称目标除子匹配、量子生成元或新的文献优先权。

**Keywords:** algebraic action; lattice resonance; Smith form; integer covolume; Mahler measure; orbit counting

# One relation, two different kinds of fixed groups

A Fourier zero is not merely an eigenvalue to omit from a determinant. For a compact connected algebraic action, it can create a continuous family of periodic states. The relation studied here is elementary: $$\label{eq:source}
 X=\{x\in\mathbb T^{\mathbb Z^2}:x_{i,j}+x_{i+1,j}+x_{i,j+1}=0\},
 \qquad (\alpha^{(a,b)}x)_{i,j}=x_{i+a,j+b},
 \quad \mathbb T=\mathbb R/\mathbb Z.$$ The challenge addressed by this reconstruction is to retain the integral lattice while passing between fixed groups, Fourier modes and finite component counts. Real diagonalization alone discards that information.

Every acting sublattice has a unique column Hermite normal form $$\label{eq:hnf}
 \Lambda=\langle(a,0),(b,c)\rangle,\qquad
 a,c>0,\quad0\le b<a,\quad N=[\mathbb Z^2:\Lambda]=ac.$$ We write $\operatorname{Fix}_\Lambda$ for points fixed by every element of $\Lambda$, not for points whose stabilizer is exactly $\Lambda$. The central source dichotomy is finite versus a finite union of two-tori. \>0 The additional finite-lattice statement is that the resonant component count requires the factor $3/N^2$. For example, at the rectangular $3\times3$ quotient the nonzero Fourier product is $81$ but there are only three components. At the smallest skew index-three quotient the product is $3$ and there is one component. \>1 These same continuous modes give the paper's stopping result: an arithmetic entropy value can exist even when the ordinary discrete orbit zeta does not.

#### Classical ownership and the precise scope.

Lind, Schmidt and Ward identify the entropy of principal algebraic actions with Mahler measure, and display this exact polynomial in their introduction [@lsw]. Smyth owns its special-value evaluation [@smyth]. Lind, Schmidt and Verbitskiy give the exact Hermite congruence and the finite-versus-two-torus distinction in Example 3.2 of the accessed source [@lsv]. None of those facts is presented here as a literature discovery. The package supplies an explicit all-lattice reconstruction, complete integer certificates and a careful distinction between the quantities that an orbit-count construction needs. \>0 Section [5](#sec:correction){reference-type="ref" reference="sec:correction"} identifies a finite-lattice error in the displayed formula of one accessed version. It neither infers the status of later corrigenda nor challenges the entropy asymptotic from that error.

# Connected source and exact quotient matrices

The relation in [\[eq:source\]](#eq:source){reference-type="eqref" reference="eq:source"} is closed in a product of circles, so $X$ is a compact metrizable abelian group. Coordinate shifts are automorphisms. Its discrete character module is $$\label{eq:dual}
 \widehat X=\mathbb Z[u^{\pm1},v^{\pm1}]/(1+u+v)
 \simeq\mathbb Z[u^{\pm1},(1+u)^{-1}].$$ The right-hand ring embeds in $\mathbb Q(u)$ and is additively torsion-free. The duality criterion for compact abelian groups therefore makes $X$ connected. This is not a finite-characteristic three-dot shift: its coordinates are circles, and the scalar ring is the integers.

Let $G=\mathbb Z^2/\Lambda$. Choose representatives $(i,j)$ with $0\le i<a$, $0\le j<c$ in lexicographic order. To reduce any integer pair, write $j=qc+r$, $0\le r<c$, and replace it by $((i-qb)\bmod a,r)$. Let $S_1,S_2$ be the permutation matrices $(S_kx)_g=x_{g+e_k}$. They commute and are orthogonal. Define $$\label{eq:matrix}
 A_\Lambda=I+S_1+S_2,
 \qquad\operatorname{Fix}_\Lambda=\ker(A_\Lambda:\mathbb T^N\longrightarrow\mathbb T^N).$$ If two neighbors coincide, their contributions add. In particular, at index one the matrix is $[3]$, not $[1]$. Equation [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"} is exact because a $\Lambda$-periodic array is determined by its quotient coordinates and the defining relation must hold at every quotient site.

[\[thm:smith\]]{#thm:smith label="thm:smith"} Suppose integer unimodular matrices $U,V$ put $A_\Lambda$ into Smith form $$U A_\Lambda V=\operatorname{diag}(d_1,\ldots,d_r,0,\ldots,0),
 \qquad0<d_1\mid\cdots\mid d_r.$$ Then $$\label{eq:group}
 \operatorname{Fix}_\Lambda\simeq\mathbb T^{N-r}\times
 \prod_{j=1}^r\mathbb Z/d_j\mathbb Z.$$ This classifies every finite-index lattice fixed group by an explicit integer algorithm. The splitting need not be canonical.

The matrices $U,V$ induce torus automorphisms since their inverse matrices are integral. A diagonal map $t\mapsto d_jt$ on a circle has kernel $\mathbb Z/d_j\mathbb Z$, whereas a zero diagonal entry leaves a whole circle free. Applying these facts coordinatewise proves [\[eq:group\]](#eq:group){reference-type="eqref" reference="eq:group"}. Smith normal form terminates by exact integer Euclidean row and column operations; no numerical eigenvalue threshold enters the statement.

# All Hermite lattices and the two resonant modes

Write $\omega=\exp(2\pi i/3)$ and $K=\{(i,j)\in\mathbb Z^2:i-j\equiv0\pmod3\}$. Finite characters of $G$ diagonalize [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"}; their eigenvalues are $1+\chi(e_1)+\chi(e_2)$, including every character multiplicity. For unit complex numbers $z,w$, $1+z+w=0$ implies $1=|1+z|^2=2+2\operatorname{Re}z$. Hence $$\label{eq:zeros}
 (z,w)\in\{(\omega,\omega^2),(\omega^2,\omega)\}.$$ The first character descends through $G$ exactly when $\Lambda\subset K$; the conjugate has the identical condition.

[\[thm:resonance\]]{#thm:resonance label="thm:resonance"} For [\[eq:hnf\]](#eq:hnf){reference-type="eqref" reference="eq:hnf"}, resonance is equivalent to $$\label{eq:resonance}
 3\mid a,\qquad b\equiv c\pmod3.$$ At resonance the nullity of $A_\Lambda$ is exactly two and $\operatorname{Fix}_\Lambda$ is a finite union of two-tori. Otherwise it is finite, with cardinality $$\label{eq:nonsingular}
 |\operatorname{Fix}_\Lambda|=|\det A_\Lambda|
 =\prod_{\chi\in\widehat G}|1+\chi(e_1)+\chi(e_2)|.$$

The character $(i,j)\mapsto\omega^{i-j}$ is trivial on the two lattice generators precisely under [\[eq:resonance\]](#eq:resonance){reference-type="eqref" reference="eq:resonance"}. Equation [\[eq:zeros\]](#eq:zeros){reference-type="eqref" reference="eq:zeros"} excludes all other zero modes. Fourier diagonalization gives the nullity; Theorem [\[thm:smith\]](#thm:smith){reference-type="ref" reference="thm:smith"} then proves the compact-group assertion. In the invertible case, the number of kernel points is the determinant's absolute value. These arguments reproduce the classical test in [@lsv Example 3.2] with the current forward-shift convention.

#### Index does not decide resonance.

For $(a,c)=(3,1)$, the shear $b=1$ is resonant and $b=0,2$ are not. Thus a census based only on the index loses the continuous fixed stratum. For rectangular lattices $b=0$, the criterion becomes $3\mid a$ and $3\mid c$. Prime indices, composite indices, and neighboring shears use the same source rule; no rational-prime labels are attached to the orbits.

\>0

# Integer covolumes determine the component count {#sec:covolume}

The nonzero Fourier product is finite at resonance, but it is not by itself the order of the torsion cokernel. The following lattice lemma keeps track of the image of all integer vectors.

[\[lem:covolume\]]{#lem:covolume label="lem:covolume"} Let $A\in M_N(\mathbb Z)$ have rank $r$, and let $P(A)$ be the product of its nonzero singular values. Set $L=\ker A\cap\mathbb Z^N$ and $L'=\ker A^t\cap\mathbb Z^N$. With Euclidean covolumes in their real spans, $$\label{eq:covolume}
 |\operatorname{tors}(\mathbb Z^N/A\mathbb Z^N)|
 =\frac{P(A)}{\operatorname{covol}(L)\operatorname{covol}(L')}.$$ Empty products and zero-dimensional covolumes are one.

The integer kernel $L$ is saturated: if $kz\in L$ for a nonzero integer $k$, then $Az=0$. Extend a basis of $L$ to a unimodular integer basis. Put $E=\operatorname{span}L$ and let $\pi$ be orthogonal projection onto $E^\perp$. The projected complementary columns are a lattice basis of $\pi\mathbb Z^N$. The block-volume formula for the extended basis gives $$1=\operatorname{covol}(L)\,\operatorname{covol}(\pi\mathbb Z^N).$$ The dual lattice of $\pi\mathbb Z^N$ in $E^\perp$ is $E^\perp\cap\mathbb Z^N$: integrality of inner products against every projected integer vector is equivalent to integrality against every integer vector. This also proves that orthogonal complementary saturated integer lattices have equal covolumes.

The restriction of $A$ from $E^\perp$ to $\operatorname{im}A$ scales $r$-dimensional volume by $P(A)$. Therefore $A\mathbb Z^N=A\pi\mathbb Z^N$ has covolume $P(A)/\operatorname{covol}(L)$ in its image span. Its saturation $\operatorname{im}A\cap\mathbb Z^N$ has covolume $\operatorname{covol}(L')$ by the complement identity. The index of the integer image in its saturation is precisely the torsion order of the cokernel. Dividing the two covolumes proves [\[eq:covolume\]](#eq:covolume){reference-type="eqref" reference="eq:covolume"}. The argument does not assume that $A$ is symmetric.

At resonance, the common real kernel of $A_\Lambda$ and $A_\Lambda^t$ consists of vectors with values $A,B,-A-B$ on the three residue classes $i-j=0,1,2\pmod3$. The two conjugate Fourier modes prove completeness of this plane. Each class has $N/3$ coordinates. The saturated integer kernel has colour-value basis $(1,0,-1),(0,1,-1)$, with Gram matrix $$\label{eq:gram}
 \mathcal G=\frac N3\begin{pmatrix}2&1\\1&2\end{pmatrix},
 \qquad\det\mathcal G=\frac{N^2}{3}.$$ Both bases are full integer kernel bases, not smaller-index sublattices. Because the shifts commute and are orthogonal, $A_\Lambda$ is normal; its singular values are the absolute values of its Fourier eigenvalues.

[\[thm:components\]]{#thm:components label="thm:components"} Under [\[eq:resonance\]](#eq:resonance){reference-type="eqref" reference="eq:resonance"}, write $\operatorname{Fix}_\Lambda\simeq\mathbb T^2\times F_\Lambda$ with finite $F_\Lambda$. Its invariant factors are those of Theorem [\[thm:smith\]](#thm:smith){reference-type="ref" reference="thm:smith"}, and $$\label{eq:components}
 |F_\Lambda|=\frac3{N^2}
 \prod_{\substack{\chi\in\widehat G\\1+\chi(e_1)+\chi(e_2)\ne0}}
 |1+\chi(e_1)+\chi(e_2)|.$$

Use Lemma [\[lem:covolume\]](#lem:covolume){reference-type="ref" reference="lem:covolume"}, the common kernel Gram determinant in [\[eq:gram\]](#eq:gram){reference-type="eqref" reference="eq:gram"}, and the Smith description of the torus kernel.

    $(a,b,c)$   $N$   nullity   nonzero product   components
  ----------- ----- --------- ----------------- ------------
    $(3,1,1)$     3         2                 3            1
    $(3,0,3)$     9         2                81            3
    $(3,0,6)$    18         2              2268           21
    $(6,0,6)$    36         2           1778112         4116

The table compares two genuinely different quantities. Treating the fourth column as the fifth fails even at the smallest resonant quotient.

# A version-specific finite-lattice correction {#sec:correction}

The accessed arXiv version 0912.5169v1 of [@lsv] prints, in Lemma 2.1 on visibly numbered page 3, a component formula consisting of the uncorrected nonzero Fourier product. The original PDF pages 3 and 4 were rendered and actually inspected; the diagnosis does not rely only on HTML extraction.

Let $\Lambda=K=\langle(3,0),(1,1)\rangle$. On the three quotient sites, the shift matrices are inverse three-cycles and $$\label{eq:minimal}
 A_K=I+S_1+S_1^2=
 \begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}.$$ Its integer image is $\mathbb Z(1,1,1)$, its cokernel is torsion-free of rank two, and its torus kernel is the connected group $\{(A,B,C)\in\mathbb T^3:A+B+C=0\}$. Its nonzero eigenvalue is $3$. The displayed uncorrected formula gives three components; the actual component count is one.

The proof on printed page 4 replaces the image of the whole integer lattice by the image of its intersection with the nonzero-mode real space. For [\[eq:minimal\]](#eq:minimal){reference-type="eqref" reference="eq:minimal"}, these images are respectively $\mathbb Z(1,1,1)$ and $3\mathbb Z(1,1,1)$. They are not equal. Lemma [\[lem:covolume\]](#lem:covolume){reference-type="ref" reference="lem:covolume"} uses the projected integer lattice and thereby retains the missing index.

This is a counterexample to that finite-lattice identity in that accessed version. The status of subsequent corrigenda is not established. It is not a refutation of the entropy theorem: for the current source, the logarithmic correction divided by $N$ is $\log(N^2/3)/N$, which tends to zero. The source's Example 3.2 remains the direct owner of the correct resonance condition, and component-growth constructions remain distinct from the ordinary point-cardinality object.

\>1

# The complete index-three torus and its primitive orbits {#sec:orbits}

The minimal quotient gives more than a small matrix control. Its fixed group is exactly a two-torus, with coordinates $(A,B)$ and third colour $C=-A-B$. The first shift acts by $$\label{eq:R}
 R(A,B)=(B,-A-B),\qquad
 R=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},
 \qquad R^3=I,$$ and the second shift is $R^{-1}$. The fixed points of the full action are exactly $A=B=C$, $3A=0$, so there are three. Every other point has stabilizer exactly $K$, because the quotient acting group has prime order three. Consequently all other orbits in this torus are primitive three-point orbits, and there are uncountably many of them.

The complex tangent phases of $R$ are $\omega,\omega^2$, while the third-return derivative is the identity. These statements are restricted to the displayed torus. They are not a hyperbolic monodromy calculation on the entire infinite-dimensional source. Interchanging the two lattice coordinates preserves [\[eq:source\]](#eq:source){reference-type="eqref" reference="eq:source"} and exchanges the generators; on this torus it conjugates $R$ to $R^{-1}$. This does not make it a same-clock reversor for every rank-one restriction.

# Classical arithmetic entropy, with the clock kept explicit

Lind--Schmidt--Ward's principal-action entropy theorem applies directly to the module [\[eq:dual\]](#eq:dual){reference-type="eqref" reference="eq:dual"} [@lsw Theorem 3.1]. With normalized Haar measure it gives the joint entropy $$\label{eq:entropy}
 h(\alpha)=m(1+u+v)=
 \int_0^1\int_0^1\log|1+e^{2\pi is}+e^{2\pi it}|\,ds\,dt.$$ This equality is sourced, not a newly proved entropy theorem. The two isolated logarithmic singularities are integrable. Jensen's formula in one variable then gives $$\label{eq:jensen}
 m(1+u+v)=\frac2\pi\int_0^{\pi/3}\log(2\cos t)\,dt.$$ For completeness, an elementary derivation of the classical Smyth value [@smyth] follows. At $0<\rho<1$, expand $\log|1+\rho e^{2it}|$ into its uniformly convergent logarithm series. As $\rho\uparrow1$, the functions converge uniformly on $[0,\pi/3]$, since the arguments stay away from zero near that limit. The integrated series is dominated by $\sum n^{-2}$. Thus $$\begin{aligned}
 m(1+u+v)
 &=\frac1\pi\sum_{n\ge1}
 \frac{(-1)^{n-1}\sin(2\pi n/3)}{n^2}\nonumber\\
 &=\frac{3\sqrt3}{4\pi}L(\chi_{-3},2),\qquad
 L(\chi_{-3},2)=\sum_{n\ge1}\frac{\chi_{-3}(n)}{n^2}.
 \label{eq:smyth}\end{aligned}$$ Here $\chi_{-3}$ is $0,1,-1$ on residues $0,1,2$ modulo three. The sine is $\sqrt3\chi_{-3}(n)/2$, and removing twice the even-index subsum multiplies the Dirichlet value by $3/2$, since $\chi_{-3}(2)=-1$. No Euler product or analytic continuation of an L-function is used.

For exact finite controls set $$L_H=\sum_{k=0}^{H-1}\left((3k+1)^{-2}-(3k+2)^{-2}\right).$$ Each omitted paired term is at most $2/(3k+1)^3$, so a first-term-plus-integral comparison proves $$\label{eq:tail}
 0<L(\chi_{-3},2)-L_H\le
 \frac2{(3H+1)^3}+\frac1{3(3H+1)^2}.$$ The entropy is approximately $0.32306594721945051409$. That decimal is a numerical control; the identity and rational tail inequality are the mathematical statements. A joint rank-two entropy is not a scalar physical period, and a scalar special value is not a target divisor.

# Why ordinary orbit-cardinality zeta fails {#sec:zeta}

An ordinary higher-rank cardinality construction would require finite coefficients in $$\label{eq:zeta}
 \exp\left(\sum_{[\mathbb Z^2:\Lambda]<\infty}
 \frac{|\operatorname{Fix}_\Lambda|}{[\mathbb Z^2:\Lambda]}
 z^{[\mathbb Z^2:\Lambda]}\right).$$ The summand for $K$ already has an uncountable fixed set at index three. The primitive formulation has the same problem: uncountably many primitive three-point orbits cannot give an ordinary product germ with finite logarithmic coefficients.

For every $v\in\mathbb Z^2$, let $T=\alpha^v$ be a rank-one restriction. Equation [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} implies $T^3=I$ on $\operatorname{Fix}_K$. Therefore $\operatorname{Fix}(T^3)$ is uncountable, and its ordinary Artin--Mazur point-cardinality zeta is also undefined. This includes the zero direction. Replacing points by components is a new construction, not a repair of the same orbit trace. No negative claim is made against measured, regularized or separately operator-defined objects.

# Evidence, literature boundary and conclusion

The canonical producer retains every quotient matrix and its integer Smith witnesses. An independent checker imports neither that producer nor a symbolic algebra package: direct multiplication checks the factorization, Bareiss elimination verifies unimodularity, and Faddeev--LeVerrier verifies all characteristic coefficients. A separate library Smith calculation and character-by-character Fourier product give additional controls. The finite grid contains 142 HNF lattices: twenty resonant and 122 nonresonant. It includes every index at most twelve and all shears for $(a,c)=(3,6),(6,3),(6,6)$. \>1 All 4900 denominator-labelled torus grid records for denominators one through twenty-four are also enumerated, together with eight exact rational Dirichlet tails. The same rational point can occur in several grids. These finite receipts test the implementation; the universal theorem is proved independently. Repaired-hash attacks specifically distinguish a pseudodeterminant from a component count, and raw/type-locked evaluation checks reject unknown fields and boolean-to-integer drift.

The direct literature owners must remain visible. Principal-action entropy is an instance of [@lsw]; the exact source resonance is [@lsv Example 3.2]; the special value belongs to [@smyth]. General periodic-component growth results in [@lsv Theorem 1.2] are not replaced by a claim about ordinary point-cardinality zeta. The present reconstruction is owner-heavy and is not a novelty certificate. \>0 Its version-specific correction is confined to the displayed finite-lattice formula and the explicit integer-image error exhibited above.

The strict Route-A assessment is weak arithmetic relation, weak primitive layer, and failure of the target determinant and target analytic layers. Native commuting Haar Koopman unitaries give only a formal quantum hint; no privileged scalar generator is constructed. No target arithmetic local data, Euler factors, root number, automorphy, target-zero match or Hilbert--Polya operator is claimed. Route B remains disabled. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 D. Lind, K. Schmidt and T. Ward, Mahler measure and entropy for commuting automorphisms of compact groups, *Inventiones Mathematicae* **101** (1990), 593--629. [Primary institutional PDF](https://ueaeprints.uea.ac.uk/id/eprint/18590/1/mahlerentropy.pdf). C. J. Smyth, On measures of polynomials in several variables, *Bulletin of the Australian Mathematical Society* **23** (1981), 49--63. [doi:10.1017/S0004972700006894](https://doi.org/10.1017/S0004972700006894). D. Lind, K. Schmidt and E. Verbitskiy, Entropy and growth rate of periodic points of algebraic $\mathbb Z^d$-actions, *Contemporary Mathematics* **532** (2010), 195--211. Version-specific formula audit uses [arXiv:0912.5169v1](https://arxiv.org/abs/0912.5169v1), Lemma 2.1, visibly numbered PDF pages 3--4 and Example 3.2.

Round zero: complete quotient presentations and the resonance test. Round one: integer covolumes and the finite-index correction. Round two: arithmetic entropy and the orbit-cardinality obstruction.
