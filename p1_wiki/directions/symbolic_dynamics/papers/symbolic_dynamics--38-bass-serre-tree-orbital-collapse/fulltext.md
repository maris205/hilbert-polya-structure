---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--38-bass-serre-tree-orbital-collapse"
canonical_tex: "symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse/main.tex"
canonical_pdf: "symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse/main.pdf"
source_sha256: "c8437cffa2dc9ec34900f1efb8db0ebd3fc778064c04e7e09686e62015f035ea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Empty on the Tree, Generic on the Orbits: A Bass--Serre No-Go for the Affine Branch

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/38-bass-serre-tree-orbital-collapse/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test the final affine symbolic candidate left by a sequence of object and coefficient firewalls: the full oriented-edge geodesic shift on the original ascending-HNN Bass--Serre tree of $\operatorname{BS}(1,r)=\langle u,v\mid vuv^{-1}=u^r\rangle$, equipped only with its canonical modular cocycle. The candidate fails in three independently typed ways. A tree has no positive reduced closed path, so the literal full-tree primitive ledger is empty. Its Hashimoto operator maps infinitely many orthogonal edge states to pairwise orthogonal vectors of norm $\sqrt r$; it is noncompact and non-trace-class, and therefore owns no ordinary Fredholm determinant. For $r\ge2$, the faithful action image is non-discrete. At $r=1$, the image is a discrete translation group, but the frozen $\mathbb Z^2$ action has kernel $\langle u\rangle$, is non-proper, and fails the finite-stabilizer tree-lattice hypotheses. Changing recurrence to positive-height group conjugacy does produce an exact Euler product for $r\ge2$, but Burnside and Möbius inversion reduce it to the generic necklace law $Z_{+,r}(z)=(1-z)/(1-rz)$; the modular cocycle only rescales $z$, while the balanced case $r=1$ diverges. Bass--Serre translation length also collapses the previous generator-step marker. The corrected authority evaluator passes $277/277$ exact checks; fresh A/B and isolated cold C are byte-identical, with $44/44$ integration tests and $96/96$ integrity checks. These results close the affine branch; they do not preclude zeta functions in different quotient, weighted, von Neumann, groupoid, or double-coset categories.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Empty on the Tree, Generic on the Orbits:\
  A Bass--Serre No-Go for the Affine Branch
```

## Markdown 正文

# Introduction {#sec:introduction}

A change of symbolic geometry does not automatically preserve recurrence or determinant ownership. The distinction becomes sharp for the original ascending-HNN splitting $$G_r=\operatorname{BS}(1,r)=\langle u,v\mid vuv^{-1}=u^r\rangle,
  \qquad r\ge1.
  \label{eq:presentation-intro}$$ Its Bass--Serre tree is canonical relative to the displayed splitting, and the HNN height supplies a canonical modular cocycle. These facts make the tree a natural last candidate after relation fillings and finite-rank coefficient repairs have failed. They do not imply that the full tree has closed geodesics, that its edge operator is trace class, or that a tree-lattice determinant applies.

The relevant neighboring theories count different objects. Ihara--Bass zeta functions for tree lattices organize primitive hyperbolic classes and quotient geometry [@bass1992ihara; @clair2001zeta]. Infinite weighted and measure-graph theories obtain determinants only after specifying finite total weight or a noncommutative trace [@deitmar2015ihara; @lenz2019ihara]. Bass--Serre theory itself separates the tree from its graph-of-groups quotient [@serre1980trees]. Treating these valid constructions as interchangeable would erase precisely the ownership question that the affine search must decide.

We therefore freeze the literal full oriented-edge geodesic shift on the tree, one new marker per tree edge, and only the canonical modular cocycle. The object receives no credit from the preceding Cayley shift or its old generator-step clock. The resulting conclusion is a terminal trilemma: the full-tree ledger is empty, the full-tree Hashimoto operator is not an ordinary Fredholm object, and the strongest group-orbital replacement is generic or divergent. exposes the entire decision before the technical derivation.

Our contributions are four specific negative statements.

1.  We prove that the full-tree geodesic shift has no positive-period point and that its Hashimoto operator admits an infinite orthogonal constant-norm image family. Thus a formal zero diagonal does not define an ordinary Fredholm determinant.

2.  We show that the allowed modular step weights preserve this noncompactness. For $r\ge2$ the faithful action image is non-discrete; for $r=1$ the image is discrete, but the original action has infinite kernel, is non-proper, and still fails the finite-stabilizer tree-lattice hypotheses.

3.  We derive the strongest separately typed substitute. At height $k>0$, conjugacy classes are multiplication-by-$r$ orbits in $\mathbb Z/(r^k-1)\mathbb Z$. Primitive repetition gives $$Z_{+,r}(z)=\frac{1-z}{1-rz},
        \qquad
        Z_{+,r,s}(z)=\frac{1-r^{-s}z}{1-r^{1-s}z}.
        \label{eq:intro-rational}$$ The law is generic across matched cyclic HNN controls, while $r=1$ diverges.

4.  We prove that tree translation length equals absolute HNN height. It sends every $u^m$ to zero and every $u^mv$ to one, so the new marker cannot inherit the old generator-step clock.

An exact CPU audit supports the formulas and control logic without standing in for the infinite proofs. The corrected evaluator passes $277/277$ integer and rational checks across $11$ parameter rows, $18$ deliberate GBS presentations, $64$ seeded random one-relator eligibility controls, residue orbits, primitive repetitions, finite trees, noncompactness certificates, and marker witnesses. Fresh A/B and isolated cold C reproduce the science, source-packet, and Route bytes exactly. The integration passes $44/44$ tests and $96/96$ integrity checks; its scientific SHA-256 is `a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.

The result is deliberately narrow. We do not claim a new Bass--Serre or Ihara theory, nor a no-go for every invariant of $\operatorname{BS}(1,r)$. We prove that this one source-locked affine candidate cannot simultaneously own a nonempty selective primitive ledger, an ordinary same-object Fredholm determinant, and a compatible marker. The strict Route-A tuple is $(A0_{\mathrm{struct}},A1_{\mathrm{fail}},A2_{\mathrm{fail}},A3_{\mathrm{fail}},A4_{\mathrm{fail}})$; Route A is rejected, Route B remains locked, and the entire affine branch closes.

The rest of the paper fixes the literature and object boundaries (), states the terminal theorem (), proves the full-tree and determinant obstructions (), derives the orbital necklace boundary (), audits markers and controls (), and records the terminal route decision ().

# Primary-source boundary {#sec:literature}

The closest literature falls into five object categories. Organizing it by category, rather than as a list of papers, prevents a determinant or cycle count from silently moving between state spaces.

#### Bass--Serre geometry and ascending HNN actions.

The Bass--Serre construction attaches a tree to a graph of groups and keeps the universal tree distinct from its quotient [@serre1980trees]. For the original splitting in [\[eq:presentation-intro\]](#eq:presentation-intro){reference-type="eqref" reference="eq:presentation-intro"}, the incidence indices are $1$ and $r$, giving an $(r+1)$-regular tree when $r\ge2$ and a line when $r=1$. Modern valuation models make these actions explicit and show that composite parameters can support other divisor splittings [@abbott2024valuations]. Those alternatives sharpen the source-lock requirement: selecting a different valuation tree after seeing the result would replace the candidate. Ascending HNN actions also have a common-end, quasi-parabolic geometry [@fima2022transitivity]; that geometry is used to inspect the end stabilizer, not to identify an orbital geodesic with a periodic path on the raw tree.

#### Discrete tree-lattice zeta functions.

Bass develops the Ihara--Selberg zeta for a tree lattice and relates primitive hyperbolic data to determinant formulas [@bass1992ihara]. Clair and Mokhtari-Sharghi extend this program using von Neumann algebras and Hilbert representations [@clair2001zeta]. Their setup explicitly begins with a discrete subgroup of the automorphism group of a bounded-degree tree; for a locally finite tree, discreteness is equivalent to finite vertex stabilizers in that image subgroup. For $r\ge2$, the $G_r$ action is faithful and its image has an infinite vertex stabilizer, hence is non-discrete. For $r=1$, the image is the discrete translation group $\mathbb Z$, but the original $\mathbb Z^2$ action has kernel $\langle u\rangle$, is non-proper, and has infinite stabilizers. Passing to the faithful image changes the acting group and the orbital ledger. Thus a finite graph-of-groups quotient does not place the frozen action inside the finite-stabilizer tree-lattice hypotheses, and the associated von Neumann determinant is not the ordinary Fredholm determinant of the raw full-tree Hashimoto operator.

#### Infinite weighted and measured graphs.

Infinite graphs can carry rigorous Ihara-type determinants once their trace category is specified. Deitmar assumes finite total graph weight and obtains Fredholm determinant formulas [@deitmar2015ihara]. Lenz, Pogorzelski, and Schmidt instead place graphs over groupoids with invariant measures and use noncommutative integration [@lenz2019ihara]. Neither framework licenses the unweighted full regular tree by omission. A nonzero invariant step weight has infinite total mass, whereas a summable radial weight chooses a basepoint and changes the object. A groupoid trace is likewise a different determinant ownership claim.

#### Conjugacy in soluble Baumslag--Solitar groups.

Group conjugacy is the most favorable nearby replacement for full-tree periodicity. Ciobanu, Evetts, and Ho describe geodesic conjugacy representatives and word-metric conjugacy growth for the soluble groups $\operatorname{BS}(1,k)$ [@ciobanu2020conjugacy]. Guo gives the fixed-height congruence criterion that identifies conjugacy with multiplication by powers of $k$ modulo $k^n-1$ [@guo2026conjugacy]. That criterion directly anticipates our residue-orbit step; we do not claim it as new. Burnside's lemma and primitive-necklace inversion then yield a simple height-only rational product. Its simplicity is a genericity diagnostic, not evidence that the raw tree acquired periodic points.

#### Current quotient and double-coset zetas.

Recent work continues to develop zetas from groups acting on trees. Hong and Kwon study geometrically finite quotient graphs of groups arising from cuspidal tree lattices [@hong2023zeta]. Marchionna studies double-coset Dirichlet series and determinant formulas based on local action data [@marchionna2026double]. These constructions are the closest active alternatives, but they count quotient or double-coset data. Importing them would change both the invariant and its determinant category.

L3.1cmYY Category & Required object or hypothesis & SD-C40 boundary\
Tree lattice & discrete faithful image, finite stabilizers/volume data & $r\ge2$: image non-discrete; $r=1$: frozen action non-proper\
Finite-total-weight graph & summable graph weight & invariant modular step weight is not summable\
Measure graph & invariant groupoid measure and noncommutative trace & trace and determinant category changes\
Group conjugacy & closure modulo a group element & not a periodic point of the literal full-tree shift\
Double-coset zeta & local action/double-coset Dirichlet data & different primitive unit and state space\

The defensible contribution is therefore a typed negative synthesis. The paper does not introduce a positive zeta construction. It proves that the one frozen full-tree candidate is empty and non-Fredholm, while its strongest orbital neighbor is already close to known conjugacy theory and collapses to a generic necklace law.

# Frozen new object and ownership {#sec:source-lock}

## Original Bass--Serre tree

Put $A=\langle u\rangle\cong\mathbb Z$. We use only the Bass--Serre tree $T_r$ of the original HNN splitting in [\[eq:presentation-intro\]](#eq:presentation-intro){reference-type="eqref" reference="eq:presentation-intro"}. Its vertices are left cosets of $A$ and its edge incidence indices are $1$ and $r$. For $r\ge2$, every vertex has degree $r+1$; for $r=1$, the tree is a line. The action has one vertex orbit and one unoriented-edge orbit.

[\[conv:height\]]{#conv:height label="conv:height"} The HNN height is the homomorphism $$\mathsf{h}:G_r\longrightarrow\mathbb Z,
  \qquad \mathsf{h}(u)=0,\quad \mathsf{h}(v)=1.$$ We use the modular convention $\Delta(g)=r^{\mathsf{h}(g)}$. The inverse convention replaces $s$ by $-s$ in every weighted formula and has no effect on the verdict.

## Literal full-tree shift

Let $E^{\mathrm{or}}T_r$ be the actual oriented edges of the universal tree. A transition $e\to f$ is legal when $o(f)=t(e)$ and $f\ne\bar e$. The full two-sided edge shift consists of sequences $(e_i)_{i\in\mathbb Z}$ satisfying this rule. The corresponding operator on $\ell^2(E^{\mathrm{or}}T_r)$ is $$\mathsf{B}\delta_e
  =\sum_{\substack{o(f)=t(e)\\f\ne\bar e}}\delta_f.
  \label{eq:hashimoto}$$ One application of the shift is one new Bass--Serre edge marker.

The allowed coefficient may multiply a positive or negative height step by the corresponding nonzero scalar power of $r$. It may not depend on a chosen root, a fitted representation, a divisor splitting, or an accepted-support predicate.

## Four ledgers that cannot be conflated

L3.3cmYYL2.4cm Object & Primitive unit & Determinant candidate & Status\
Literal full tree & periodic actual-edge geodesic & ordinary Fredholm on $\ell^2(E^{\mathrm{or}}T_r)$ & primary, fails\
Quotient graph of groups & quotient loop with stabilizer data & finite or tree-lattice/von Neumann & different object\
Group orbital ledger & hyperbolic conjugacy class & formal orbital Euler product & boundary only\
Fixed-end/double-coset ledger & end orbit or double coset & representation or Dirichlet determinant & boundary only\

A path that returns only after applying $g\in G_r$ is not a periodic point of the first row. Likewise, a determinant built after quotienting or changing the trace does not certify trace class of [\[eq:hashimoto\]](#eq:hashimoto){reference-type="eqref" reference="eq:hashimoto"}.

## Acceptance and falsification

The candidate would pass only if the primary row simultaneously supplied a nonempty source-selective primitive ledger, an ordinary Fredholm determinant, and a consistent new marker. One positive reduced closed path would falsify the emptiness claim. A nonzero canonical modular weighting that made the same full-tree operator trace class would falsify the analytic obstruction. A proper finite-stabilizer action satisfying the tree-lattice hypotheses without quotienting the acting group would falsify the tree-lattice boundary.

The controls include balanced $r=1$, prime $r=2,3,5,7$, composite baseline $r=4$, composites $r=6,8,9,10,12$, deliberate ascending and non-ascending $\operatorname{BS}(p,q)$ presentations, seeded random one-relator eligibility rows, finite trees, orthogonal columns, divergence, and marker collisions. Any empty, generic, divergent, non-trace-class, or marker-incompatible outcome is terminal; no repair search follows it.

# Bass--Serre terminal theorem {#sec:main-theorem}

The main statement combines three primary-object failures with the strongest separately typed orbital boundary.

[\[thm:terminal\]]{#thm:terminal label="thm:terminal"} Fix $r\ge1$ and the source-locked object of .

1.  The literal full-tree geodesic shift has no positive-period point and no primitive periodic orbit.

2.  The full-tree Hashimoto operator $\mathsf{B}$ is noncompact and not trace class. Every nonzero per-step scalar weighting supplied only by the canonical modular cocycle has the same obstruction. Hence the ordinary Fredholm determinant $\det(I-z\mathsf{B})$ is not owned.

3.  For $r\ge2$, the action of $G_r$ on $T_r$ is faithful and its image in $\mathop{\mathrm{Aut}}(T_r)$ is non-discrete. For $r=1$, $G_1\cong\mathbb Z^2$ has kernel $\langle u\rangle$ and discrete translation image $\mathbb Z$, but the original action is non-proper and fails the finite-stabilizer tree-lattice hypotheses. Passing to the image changes the acting group and orbital ledger. For $r\ge2$, the signed-translation kernel at the common ascending end is infinite as well.

4.  If the ledger is changed to positive-height group conjugacy, then for $r\ge2$ $$C_r(k)=\frac1k\sum_{j=0}^{k-1}
          \bigl(r^{\gcd(j,k)}-1\bigr),
        \qquad
        Z_{+,r}(z)=\frac{1-z}{1-rz}.$$ The modular weight only substitutes $z\mapsto r^{-s}z$. This ledger is generic across matched cyclic index-$r$ ascending HNN controls. For $r=1$, it has infinitely many classes at every positive height.

5.  Bass--Serre translation length is $\ell_{T_r}(g)=|\mathsf{h}(g)|$. The new tree-edge clock is therefore incompatible with the old generator-step marker.

No branch supplies a nonempty source-selective primitive ledger and an ordinary Fredholm determinant on the same object. The strict Route-A tuple is $(A0_{\mathrm{struct}},A1_{\mathrm{fail}},A2_{\mathrm{fail}},A3_{\mathrm{fail}},A4_{\mathrm{fail}})$, Route A is rejected, Route B is locked, and the affine branch closes.

#### Proof map.

The first claim is the defining acyclicity of a tree applied to one proposed period. The second uses an infinite family of edges with distinct terminal vertices; their Hashimoto images have disjoint supports and norm $\sqrt r$. The third first separates the faithful image from the original action and then applies the finite-stabilizer criterion to that image [@clair2001zeta]; the balanced case is handled by its infinite kernel and non-properness. For the fourth, the semidirect-product conjugation formula reduces fixed-height classes to multiplication-by-$r$ residue orbits; Burnside and Möbius inversion identify necklaces and their primitive roots. The final claim follows from the Busemann lower bound and a conjugate normal form $u^m v^k$. Complete proofs appear in and .

## Why the three failures cannot be merged

The empty ledger and noncompact operator are not contradictory. The operator has many nonclosed geodesic trajectories, and those trajectories prevent compactness even though none is periodic. Conversely, a group element may translate an infinite geodesic and define a hyperbolic conjugacy class without creating a closed path in the universal tree.

The determinant categories also remain separate. An ordinary Fredholm determinant requires a trace-class perturbation of the identity. A tree-lattice or groupoid determinant uses a different trace and different hypotheses. The following implications are forbidden: $$\text{formal zero diagonal}
  \nRightarrow \text{trace class},
  \qquad
  \text{finite quotient graph}
  \nRightarrow \text{discrete action},$$ $$\text{hyperbolic conjugacy class}
  \nRightarrow \text{full-tree periodic point}.$$

## The stabilizer zero-weight loophole

The tree-lattice volume uses reciprocals of finite stabilizer orders. The present stabilizers are copies of $\mathbb Z$. Assigning $1/|\mathbb Z|=0$ by fiat would erase every vertex, edge, and common-end term for every deliberate GBS control. It would give the same empty answer for ascending, balanced, and non-ascending presentations.

The zero convention is not a limiting construction specified by the source and does not satisfy the cited finite-stabilizer formulas. Because it annihilates all matched controls, it cannot earn arithmetic selectivity or determinant ownership.

The theorem is a no-go for the one frozen candidate, not a claim that other quotient, weighted, measure-graph, groupoid, or double-coset zetas are invalid.

# Tree emptiness and Fredholm failure {#sec:tree-fredholm}

## No periodic actual-edge geodesic

[\[lem:no-period\]]{#lem:no-period label="lem:no-period"} The full oriented-edge geodesic shift on $T_r$ has no periodic point of positive period.

Suppose $(e_i)_{i\in\mathbb Z}$ has period $n>0$. The word $e_0e_1\cdots e_{n-1}$ is reduced because immediate reversal is forbidden. Periodicity identifies the terminal vertex after one period with the initial vertex, so the word is a positive reduced closed path. A tree has no such path. This contradiction proves the claim.

The qualifier "actual edge" matters. If $e_n=g e_0$ for some nontrivial $g\in G_r$, the segment is an orbital fundamental segment, not a period of the raw edge sequence.

## An infinite orthogonal-column witness

[\[prop:noncompact\]]{#prop:noncompact label="prop:noncompact"} The operator $\mathsf{B}$ in [\[eq:hashimoto\]](#eq:hashimoto){reference-type="eqref" reference="eq:hashimoto"} is noncompact and therefore not trace class.

Choose oriented edges $e_1,e_2,\ldots$ with distinct terminal vertices. For $i\ne j$, the support of $\mathsf{B}\delta_{e_i}$ consists of oriented edges whose origin is $t(e_i)$, while the support of $\mathsf{B}\delta_{e_j}$ has origin $t(e_j)$. The supports are disjoint. Since $T_r$ has degree $r+1$, $$\langle \mathsf{B}\delta_{e_i},\mathsf{B}\delta_{e_j}\rangle=0,
  \qquad
  \|\mathsf{B}\delta_{e_j}\|_2^2=r.$$ Thus the image of an orthonormal sequence has no convergent subsequence. The operator is not compact. Every trace-class operator is compact, which proves the second assertion.

For $r=1$, this witness is the bilateral shift along either orientation of the line. For $r\ge2$, each image has $r$ legal nonbacktracking continuations.

[\[cor:modular-noncompact\]]{#cor:modular-noncompact label="cor:modular-noncompact"} Fix a finite complex parameter $s$. Any nonzero per-step scalar weighting derived only from $\Delta^{-s}$ remains noncompact on the full tree.

One tree step changes height by $+1$ or $-1$. The two possible transition magnitudes are $r^{-\operatorname{Re}s}$ and $r^{\operatorname{Re}s}$ (both one when $r=1$). Restrict the family in to one oriented type. Its images remain pairwise orthogonal with a fixed positive norm.

A potential $r^{-s\beta(x)}$ based on an absolute Busemann coordinate is not the per-step cocycle: choosing its zero chooses a basepoint, and one tree direction makes the reciprocal weight grow. A different radial damping may be analytically useful, as finite-total-weight graph theory illustrates [@deitmar2015ihara], but it is outside the frozen object.

## Why formal zero traces are insufficient

By , every diagonal matrix coefficient $\langle\delta_e,\mathsf{B}^n\delta_e\rangle$ vanishes. It is tempting to write $$\mathop{\mathrm{Tr}}(\mathsf{B}^n)=0,
  \qquad
  \det(I-z\mathsf{B})=
  \exp\!\left(-\sum_{n\ge1}\frac{z^n}{n}\mathop{\mathrm{Tr}}(\mathsf{B}^n)\right)=1.
  \label{eq:unowned-formal}$$ Equation [\[eq:unowned-formal\]](#eq:unowned-formal){reference-type="eqref" reference="eq:unowned-formal"} is not an ordinary Fredholm identity. The trace-log expansion requires trace-class ownership before the diagonal is summed. rules out that premise. A groupoid or von Neumann trace can be meaningful in another framework [@clair2001zeta; @lenz2019ihara]; it must be named as that framework and cannot be relabeled as the ordinary trace on $\ell^2(E^{\mathrm{or}}T_r)$.

## Action, properness, and the common end

Let $\rho_r:G_r\to\mathop{\mathrm{Aut}}(T_r)$ be the action homomorphism and put $H_r=\rho_r(G_r)$. The base vertex is the coset $A$. Its stabilizer for the original action is $A\cong\mathbb Z$, and all vertex stabilizers are conjugate copies; edge stabilizers are also infinite cyclic. In the compact-open topology, a subgroup of the automorphism group of a locally finite tree is discrete precisely when its vertex stabilizer is finite [@clair2001zeta]. This criterion applies to the image $H_r$.

For $r\ge2$, the kernel is the core of $A$ and $$\ker\rho_r\subseteq
  \bigcap_{n\ge0}v^nAv^{-n}
  =\bigcap_{n\ge0}\langle u^{r^n}\rangle=\{1\}.$$ Thus the action is faithful. The base-vertex stabilizer in $H_r$ is the infinite group $\rho_r(A)\cong\mathbb Z$, so $H_r$ is non-discrete.

For $r=1$, $G_1=A\times\langle v\rangle\cong\mathbb Z^2$ and $T_r$ is a line. The subgroup $A=\langle u\rangle$ fixes the line pointwise, while $v$ translates it by one edge. Hence $$\ker\rho_1=A,
  \qquad H_1\cong\langle v\rangle\cong\mathbb Z,$$ and $H_1$ is discrete. The original $G_1$ action is nevertheless non-proper because its vertex and edge stabilizers contain the infinite kernel. It is not a finite-stabilizer tree-lattice action. Replacing it by $G_1/A$ changes the acting group and collapses the original group-conjugacy ledger.

For $r\ge2$, the ascending action fixes a common end. The union $$N_r=\bigcup_{j\ge0}v^{-j}Av^j\cong\mathbb Z[1/r]
  \label{eq:end-kernel}$$ has zero signed translation and lies in the end stabilizer kernel. It is infinite. Hence the finite-cardinality end average used in the discrete tree-lattice construction is unavailable. This observation agrees with the standard quasi-parabolic description of ascending HNN actions [@fima2022transitivity].

At $r=1$, the infinite kernel $A$ already fixes every vertex and edge, so the finite-stabilizer hypothesis fails even though the quotient image is discrete. The three statements in this section are logically distinct: no cycles, non-trace-class edge dynamics, and the $r$-split tree-lattice hypothesis failure. Each one independently prevents the requested same-object determinant/ledger pair.

# Orbital necklace collapse {#sec:orbital}

We now give the strongest favorable calculation after explicitly changing the primitive unit from full-tree periods to positive-height group conjugacy classes. The fixed-height congruence is consistent with current conjugacy theory for soluble Baumslag--Solitar groups [@ciobanu2020conjugacy; @guo2026conjugacy].

## Conjugacy at fixed height

For $r\ge2$, write $$G_r\cong\mathbb Z[1/r]\rtimes\mathbb Z,
  \qquad
  (a,\ell)(b,k)=(a+r^\ell b,\ell+k).
  \label{eq:semidirect}$$ The inverse is $(-r^{-\ell}a,-\ell)$, and direct multiplication yields $$(c,m)(b,k)(c,m)^{-1}
  =\bigl(r^m b+(1-r^k)c,k\bigr).
  \label{eq:conjugation}$$ Height is therefore a conjugacy invariant. At fixed $k>0$, addition by $(1-r^k)c$ passes to $$\mathbb Z[1/r]/(r^k-1)\mathbb Z[1/r]
  \cong \mathbb Z/(r^k-1)\mathbb Z,$$ and conjugation by height $m$ acts by multiplication by $r^m$.

[\[prop:burnside\]]{#prop:burnside label="prop:burnside"} The number of conjugacy classes at height $k$ is $$C_r(k)=\frac1k\sum_{j=0}^{k-1}
  \bigl(r^{\gcd(j,k)}-1\bigr)=N_r(k)-1,
  \label{eq:class-count}$$ where $N_r(k)$ is the number of length-$k$ necklaces on $r$ symbols.

Multiplication by $r$ has exact order $k$ modulo $r^k-1$. Its $j$th power fixes $$\gcd(r^j-1,r^k-1)=r^{\gcd(j,k)}-1$$ residues. Burnside's lemma gives the first equality. The ordinary necklace formula has the same average with $r^{\gcd(j,k)}$ in place of $r^{\gcd(j,k)}-1$, proving the second equality.

The explicit digit map sends $(d_0,\ldots,d_{k-1})$ to $\sum_i d_ir^i$ modulo $r^k-1$. Rotation acts by multiplication by $r$. The only duplicate in the integer range $[0,r^k-1]$ is the pair $0^k$ and $(r-1)^k$, which explains the subtraction of one.

## Primitive roots and the Euler product

Let $P_r(k)$ count primitive positive-height conjugacy classes. A word of minimal period $d\mid k$ repeats $k/d$ times, and the associated translation coordinate is multiplied by $1+r^d+\cdots+r^{k-d}$. This is exactly the first coordinate of the corresponding semidirect-product power. Möbius inversion gives $$P_r(1)=r-1,
  \qquad
  P_r(k)=\frac1k\sum_{d\mid k}\mu(d)r^{k/d}\quad(k>1),
  \qquad
  C_r(k)=\sum_{d\mid k}P_r(d).
  \label{eq:primitive-count}$$

The ordinary Witt necklace product is $(1-rz)^{-1}$. Our primitive counts differ only by one missing degree-one class, so $$Z_{+,r}(z)
  =\prod_{k\ge1}(1-z^k)^{-P_r(k)}
  =\frac{1-z}{1-rz}.
  \label{eq:orbital-product}$$ This factorization owns primitive/repetition bookkeeping inside the group-orbital ledger. It does not repair the object change.

## The modular cocycle only rescales length

At positive height $k$, Convention [\[conv:height\]](#conv:height){reference-type="ref" reference="conv:height"} gives $\Delta^{-s}=r^{-sk}$. Weighting [\[eq:orbital-product\]](#eq:orbital-product){reference-type="eqref" reference="eq:orbital-product"} therefore makes the substitution $z\mapsto r^{-s}z$: $$Z_{+,r,s}(z)
  =\frac{1-r^{-s}z}{1-r^{1-s}z}.
  \label{eq:modular-product}$$ The cocycle supplies no second label beyond signed tree length. In particular, it produces neither a graded cancellation nor a prime/composite split.

## Balanced divergence and genericity

For $r=1$, the group is $\mathbb Z^2$ and conjugacy is equality. At each height $k>0$, the elements $(b,k)$ for $b\in\mathbb Z$ give infinitely many classes. The orbital Euler product is not locally finite. Quotienting the infinite height-zero kernel leaves a generic line action and changes the object again.

::: {#tab:necklace-counts}
   $r$  $C_r(1{:}6)$              $P_r(1{:}6)$
  ----- ------------------------- -------------------------
    2   $1,2,3,5,7,13$            $1,1,2,3,6,9$
    3   $2,5,10,23,50,129$        $2,3,8,18,48,116$
    4   $3,9,23,69,207,699$       $3,6,20,60,204,670$
    5   $4,14,44,164,628,2634$    $4,10,40,150,624,2580$
    6   $5,20,75,335,1559,7825$   $5,15,70,315,1554,7735$

  : First six total and primitive orbital counts. Prime and composite rows follow one index law; the table is a genericity control, not a factorization classifier.
:::

Every cyclic index-$r$ ascending HNN control reproduces [\[eq:orbital-product\]](#eq:orbital-product){reference-type="eqref" reference="eq:orbital-product"}. The formula remembers the numerical incidence index, but it does not distinguish the source presentation from its matched controls. Under the preregistered rule, that genericity is terminal.

# Marker and control firewalls {#sec:marker-controls}

The Bass--Serre candidate is a genuinely new symbolic object. Its unit clock is one actual tree edge, whereas the preceding affine candidates used one displayed generator step. The two clocks must therefore be compared rather than identified.

## Translation length is absolute height

[\[prop:translation-length\]]{#prop:translation-length label="prop:translation-length"} For every $g=(a,k)\in\mathbb Z[1/r]\rtimes\mathbb Z$, $$\ell_{T_r}(g)=|k|=|\mathsf{h}(g)|.
  \label{eq:translation-length}$$ Consequently, every $u^m$ is elliptic, every $u^mv$ has tree translation length one, and the displayed defining relator has translation length zero.

Let $\beta$ be the Busemann height toward the distinguished end. One tree edge changes $\beta$ by one, so $d(x,gx)\ge |k|$ for every vertex $x$. Choose $j\ge0$ such that $r^ja=m\in\mathbb Z$. Conjugation by $v^j$ sends $(a,k)$ to $(m,k)=u^mv^k$. At the base vertex $A=\langle u\rangle$, the factor $u^m$ fixes $A$, while $v^k$ traverses exactly $|k|$ HNN edges. Thus the Busemann lower bound is attained. Translation length is conjugacy invariant, which proves [\[eq:translation-length\]](#eq:translation-length){reference-type="eqref" reference="eq:translation-length"}.

The comparison with the old displayed Cayley paths is therefore $$\begin{array}{c|ccc}
\text{element or displayed word} & u^m & u^mv & vuv^{-1}u^{-r} \\
\hline
\text{old generator-step length} & m & m+1 & r+3 \\
\text{new tree translation length} & 0 & 1 & 0 .
\end{array}
\label{eq:marker-table}$$ This is a many-to-one loss of the previous clock, not an inconsistency in the Bass--Serre metric. In particular, no inherited same-marker claim is available.

## Prime, composite, balanced, and presentation controls

Prime values $r=2,3,5,7$ and composite values $r=4,6,8,9,10,12$ obey the same formulas in . The source-locked tree always has degree $r+1$, but neither the necklace identity nor the modular rescaling detects primality. Composite $r$ may admit other valuation or divisor splittings [@abbott2024valuations]; selecting one would replace the original splitting and was forbidden before evaluation.

The balanced row $r=1$ supplies two opposite controls. The literal tree is a line and still has no reduced closed path, while its Hashimoto operator is a bilateral shift on each oriented component and remains noncompact. In contrast, its group-orbital ledger diverges because $\operatorname{BS}(1,1)\cong\mathbb Z^2$ has infinitely many conjugacy classes at every positive height. Empty and divergent are differently typed failures.

For a deliberate cyclic generalized Baumslag--Solitar presentation $\operatorname{BS}(p,q)$ with positive incidence indices, the original Bass--Serre tree has degree $p+q$ and infinite cyclic stabilizers. Its literal full-tree ledger is again empty, and its Hashimoto operator has the same orthogonal- column witness with squared norm $p+q-1$. The $18$ deliberate controls span ascending, reversed-ascending, balanced, and non-ascending cases. They show that the tree obstruction is structural, not a selective signature of the specific relation.

The $64$ seeded two-generator one-relator controls play a narrower role. None passes the independent cyclic-GBS eligibility parser. They are therefore excluded rather than counted as mathematical counterexamples. This separation prevents a random word with no canonical HNN source from being assigned a tree after the fact.

## The stabilizer convention that proves too much

Setting $1/|\mathbb Z|$ equal to zero would annihilate every vertex, edge, and common-end contribution for all of the deliberate GBS controls. It would give the same result in ascending, balanced, and non-ascending rows. The convention is neither part of the finite-stabilizer tree-lattice formula nor a source-specified limiting process. It is rejected as `PROVES_TOO_MUCH`.

Together, the controls separate four terminal outcomes: literal-tree emptiness, analytic non-Fredholmness, orbital genericity or divergence, and marker incompatibility. No control permits credit to move between them.

# Source/evaluator-separated exact audit {#sec:exact-audit}

The computational artifact is a deterministic audit of the finite algebra, not a search for a positive example and not a substitute for the infinite proofs. The source process writes only presentation rows, fixed parameter ranges, marker words, deterministic seeds, and finite trees. It imports no evaluator module and contains no orbit formula, determinant target, acceptance table, or verdict. A fresh evaluator process parses that source JSON and independently implements the residue action, Burnside counts, Möbius inversion, truncated product algebra, eligibility checks, and finite graph witnesses.

All scientific arithmetic uses integers or `fractions.Fraction`. There is no floating-point tolerance, external oracle, network call, or unbounded word enumeration. Fresh A/B and isolated cold C reproduce the science, source packet, and Route evaluation byte for byte. The cold copy is removed. Four transport-metadata states and two simulated future-manifest states preserve the scientific and Route bytes.

L4.1cmL2.7cmY Audit block & Frozen size & Exact obligation\
Parameter controls & $11$ rows & balanced, prime, and composite indices\
Deliberate GBS controls & $18$ presentations & ascending, reversed, balanced, non-ascending\
Random one-relator controls & $64$ words; $0$ eligible & cyclic-GBS parser excludes inapplicable objects\
Residue and Burnside checks & frozen direct range & explicit orbits equal closed counts\
Primitive/product checks & through degree $12$ & repetition ledger and rational product agree\
Finite-tree controls & $3$ trees & no reduced closed path; distinct-origin columns\
Full assertion ledger & $277/277$ & every preregistered exact check passes\
Fresh/cold executions & A/B/C: $3/3$ identical & isolated cold copy removed\
Integration and integrity & $44/44$; $96/96$ & all checks pass\
Closed artifacts & $28$ results; $42$ ledger entries; $44$ managed texts & exact membership and hashes\

The authority scientific digest is

`a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.

The digest covers scientific content rather than volatile timestamps or absolute paths. The immutable ledger verifies $42/42$ entries and has SHA-256

`af2db7457808bcb956c284d28387bf74bfda59f329b688e9491b5ef38066d309`.

A second primary materialization has an empty changed-path list.

## What the finite audit establishes

The direct residue enumeration checks that multiplication-by-$r$ orbits in $\mathbb Z/(r^k-1)\mathbb Z$ match [\[eq:class-count\]](#eq:class-count){reference-type="eqref" reference="eq:class-count"}. Independent divisor arithmetic checks $C_r(k)=\sum_{d\mid k}P_r(d)$ and the degree-$12$ truncation of [\[eq:orbital-product\]](#eq:orbital-product){reference-type="eqref" reference="eq:orbital-product"}. Marker witnesses verify [\[eq:marker-table\]](#eq:marker-table){reference-type="eqref" reference="eq:marker-table"}. Finite trees confirm the combinatorial no-cycle invariant, and finite column calculations instantiate the support disjointness used in .

The audit also exercises all verdict firewalls. An empty full-tree ledger is not rewritten as a determinant of one; an infinite stabilizer is not given reciprocal zero; ineligible random presentations do not enter the GBS denominator; group conjugacy and tree periodicity remain separate table keys; and positive-height restriction is not relabeled as graded cancellation.

## What the audit does not establish

No finite truncation proves that every tree lacks a reduced closed path, that the infinite Hashimoto operator is noncompact, that the faithful image is non-discrete for $r\ge2$, that the $r=1$ action is non-proper with infinite kernel, or that the necklace formula holds for every $k$. Those are theorem-owned statements proved in and . Because the computation is exact and deterministic, sampling uncertainty, confidence intervals, and error bars are inapplicable. The purpose of the three-run and metadata-stability checks is implementation reproducibility, not statistical replication.

# Strict route decision {#sec:route}

The candidate is evaluated only against the preregistered Route-A v0.2 gates. Structural occurrence of the exponent is not enough: a surviving route would also need a selective primitive sector, same-object determinant ownership, robust controls, and a consistent unit marker.

L1.2cmL3.2cmYL1.9cm Gate & Requirement & Evidence & Verdict\
$A0$ & structural relation input & the HNN incidence index $r$ enters the tree and orbital formulas & structural\
$A1$ & nonempty selective primitive ledger & full tree empty; orbital substitute generic for $r\ge2$ and divergent for $r=1$ & fail\
$A2$ & honest same-object determinant & full-tree operator noncompact and non-trace-class; lattice hypotheses fail & fail\
$A3$ & control-robust selectivity & prime/composite and matched GBS controls follow one structural law & fail\
$A4$ & internally owned unit marker & tree length $|\mathsf{h}|$ collapses the old generator clock & fail\

Thus the strict tuple is $$(A0_{\mathrm{struct}},A1_{\mathrm{fail}},A2_{\mathrm{fail}},A3_{\mathrm{fail}},A4_{\mathrm{fail}}),$$ with the machine-readable outcome

`STOP_BASS_SERRE_TREE_BRANCH` `ROUTE_A_REJECTED` `CLOSE_ENTIRE_AFFINE_BRANCH`.

Route B is not invoked.

The conclusion is narrower than a universal impossibility theorem. It does not rule out quotient graph zetas, groupoid or von Neumann determinants, finite-total-weight models, double-coset Dirichlet series, or other invariants of Baumslag--Solitar groups. It rules out using any of those different categories as evidence that the frozen full-tree edge shift owns a nonempty primitive ledger and an ordinary Fredholm determinant.

The closure is nevertheless terminal for the affine program. The preceding coefficient branch and the present geometry branch have exhausted the predeclared affine repairs. Another affine tree, quotient, local system, representation, cocycle, damping, first-return scheme, or marker would be a post hoc new mechanism rather than a control.

The sole permissible successor is therefore an obstruction synthesis. Paper 39 may organize the typed failures of Papers 35--38 into an affine branch-closure DAG and return control to the pre-existing non-affine candidate registry. It may not reopen the branch by testing one more arbitrary affine representation or symbolic object.

# Proof details for the orbital boundary {#app:proofs}

This appendix gives the algebra suppressed in the main proof map. Its statements belong to the group-orbital boundary unless they explicitly name the full-tree object.

## Localization and the fixed-height quotient

[\[lem:localization-quotient\]]{#lem:localization-quotient label="lem:localization-quotient"} For $r\ge2$ and $k>0$, $$\mathbb Z[1/r]/(r^k-1)\mathbb Z[1/r]
 \cong \mathbb Z/(r^k-1)\mathbb Z.$$

Put $M=r^k-1$. Since $\gcd(r,M)=1$, multiplication by every power of $r$ is invertible modulo $M$. Hence a localized element $a/r^j$ has the integer residue $a(r^j)^{-1}\pmod M$, so the natural map from $\mathbb Z$ is surjective after quotienting. Its kernel consists exactly of the integers in $M\mathbb Z[1/r]$. If $n=M a/r^j$ is integral, invertibility of $r^j$ modulo $M$ implies $M\mid n$; the kernel is $M\mathbb Z$.

Equation [\[eq:conjugation\]](#eq:conjugation){reference-type="eqref" reference="eq:conjugation"} shows that height-$k$ conjugation by $(c,0)$ changes $b$ by $(1-r^k)c$, whereas conjugation by $(0,m)$ multiplies $b$ by $r^m$. Lemma [\[lem:localization-quotient\]](#lem:localization-quotient){reference-type="ref" reference="lem:localization-quotient"} therefore gives the claimed multiplication action on $\mathbb Z/M\mathbb Z$.

## Order, fixed points, and endpoint identification

[\[lem:mult-order\]]{#lem:mult-order label="lem:mult-order"} Multiplication by $r$ has exact order $k$ modulo $M=r^k-1$, and the $j$th power has $r^{\gcd(j,k)}-1$ fixed residues.

Certainly $r^k\equiv1\pmod M$. If $0<j<k$, then $0<r^j-1<M$, so $M\nmid r^j-1$; the order is exactly $k$. A residue $x$ is fixed by the $j$th power precisely when $(r^j-1)x\equiv0\pmod M$. A multiplication map by $q$ on $\mathbb Z/M\mathbb Z$ has $\gcd(q,M)$ kernel elements. Finally, $$\gcd(r^j-1,r^k-1)=r^{\gcd(j,k)}-1,$$ which proves the count.

For a digit word $d=(d_0,\ldots,d_{k-1})$ with $0\le d_i<r$, define $$\Phi(d)=\sum_{i=0}^{k-1}d_i r^i\pmod M.$$ A cyclic digit rotation changes $\Phi$ by multiplication by $r$ (up to the choice of rotation direction, which replaces $r$ by its inverse). Before reduction, the digit sum ranges from $0$ to $M$. Distinct values inside this closed interval can be congruent modulo $M$ only at the endpoints. Those endpoints are realized uniquely by $0^k$ and $(r-1)^k$. This proves both the single endpoint collision and $C_r(k)=N_r(k)-1$.

## Primitive repetition and the rational product

Suppose a length-$d$ word represents $b$. Repeating it $m$ times, where $k=md$, represents $$b\bigl(1+r^d+\cdots+r^{(m-1)d}\bigr).
 \label{eq:digit-repeat}$$ The same factor occurs in the semidirect-product power $$(b,d)^m=
 \left(b\bigl(1+r^d+\cdots+r^{(m-1)d}\bigr),md\right).$$ Thus minimal necklace period agrees with primitive positive group height. The sole endpoint collision is already of period one. If $L_r(k)$ denotes the ordinary number of primitive $r$-ary necklaces, then $$P_r(1)=L_r(1)-1=r-1,
 \qquad P_r(k)=L_r(k)\quad(k>1).$$ The Witt identity $$\prod_{k\ge1}(1-z^k)^{-L_r(k)}=(1-rz)^{-1}$$ immediately gives [\[eq:orbital-product\]](#eq:orbital-product){reference-type="eqref" reference="eq:orbital-product"}. Equivalently, taking formal logarithms shows that the coefficient of $z^n$ is $n^{-1}\sum_{d\mid n}dP_r(d)=r^n/n-1/n$, the logarithm of $(1-z)/(1-rz)$.

## Weighted noncompactness in operator form

Let $W_s$ be any allowed per-step modular weighting. On a fixed oriented step type its coefficient is a nonzero scalar $c_s$. Choose the edge family in so that every selected edge has that type. After passing to an infinite subfamily if necessary, the vectors $W_s\mathsf{B}\delta_{e_j}$ have disjoint supports and one fixed positive squared norm. Hence they have no norm-convergent subsequence. This proves noncompactness without using a diagonal trace or a spectral-radius calculation.

## Translation length without an inherited marker

The HNN height extends to a Busemann function on vertices: adjacent vertices have heights differing by one. Therefore a path from $x$ to $gx$ has at least $|\mathsf{h}(g)|$ edges. For $g=(a,k)$, choose $j$ with $r^ja\in\mathbb
Z$ and conjugate by $v^j$. The resulting $u^mv^k$ moves the base vertex by exactly $|k|$. This proves [\[eq:translation-length\]](#eq:translation-length){reference-type="eqref" reference="eq:translation-length"}; it also shows why the statement concerns translation length, not the length of an arbitrary written word. The distinction is exactly the marker firewall used in .

# Scope, ownership, and reproducibility declarations {#app:scope}

## Claim ledger

L2.8cmYL3.8cm Statement & Owned evidence & Excluded inference\
Full-tree ledger is empty & reduced-path proof on the universal tree & no claim about quotient or orbital ledgers\
Ordinary Fredholm fails & infinite orthogonal constant-norm image family & no claim that groupoid or von Neumann determinants are invalid\
Orbital product is rational & fixed-height conjugacy, Burnside, primitive repetition & no transfer to a full-tree periodic determinant\
Modular factor is generic & height-only rescaling and matched controls & no graded cancellation or arithmetic selectivity\
Marker is incompatible & exact translation-length formula and collisions & no inherited old-clock credit\
Affine branch closes & frozen Route-A gates and forbidden-repair list & no universal no-go outside the affine registry\

Positive height is a restriction, not a sign-reversing or supertrace sector. All orbital factors in this paper have nonnegative integer multiplicity. Accordingly, no cancellation language is used to promote [\[eq:modular-product\]](#eq:modular-product){reference-type="eqref" reference="eq:modular-product"}. Primitive classes are separated from their repetitions before the Euler product is formed.

## Forbidden credit transfers

The following moves are outside the source lock: replacing the full tree by its quotient loop; choosing a fundamental domain; installing a von Neumann or groupoid trace; adding a finite-total radial weight; selecting another valuation tree for composite $r$; inducing or accelerating the shift; introducing a local system, character, representation, grading, or fitted fiber; declaring $1/|\mathbb Z|=0$; or inheriting the old generator marker. Each may define a legitimate new problem, but none can repair SD-C40 after evaluation.

## Reproducibility boundary

The finite audit uses exact CPU arithmetic and separated source/evaluator processes. The corrected authority evaluator reports $277/277$ assertions; fresh A/B and isolated cold C are byte-identical, integration tests pass $44/44$, and the full audit passes $96/96$. The scientific SHA-256 is

`a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.

The source lock, preregistration, derivation, proof, and literature audit were frozen before manuscript integration. The manuscript does not use its finite rows to infer an infinite theorem. No external dataset, learned model, stochastic optimizer, or human-subject data are involved.

The independent integration layer owns code, results, experiment plans, dependency and research locks, evaluations, and the experiment report. The repository root alone owns the future Stage-2 manifest, metadata-only seal, root registration, Git operations, and mirror synchronization.

## Limitations and disclosure

The analysis is tied to the original ascending-HNN splitting of $\operatorname{BS}(1,r)$ and its literal full-tree oriented-edge shift. It neither classifies every action of the group on a tree nor compares all possible noncommutative determinants. The orbital calculation is a boundary diagnostic close to established conjugacy theory, not a novelty claim for the fixed-height congruence itself.

AI assistance was used to organize derivations, implement the exact audit, and prepare the manuscript. Every mathematical claim is accompanied by a proof or a primary-source boundary, and all finite claims are tied to the deterministic artifact. No external-review or iterative paper-improvement loop was used. Responsibility for the final claims and source distinctions remains with the authors.
