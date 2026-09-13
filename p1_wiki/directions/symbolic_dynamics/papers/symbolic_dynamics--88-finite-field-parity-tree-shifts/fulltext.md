---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--88-finite-field-parity-tree-shifts"
canonical_tex: "symbolic_dynamics/papers/88-finite-field-parity-tree-shifts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/88-finite-field-parity-tree-shifts/main.pdf"
source_sha256: "2e2f6bbaf155ecd236ddb72c18e61b1f194beaf8736031f0caff1a19f3b05e20"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Field Parity Tree Shifts: Exact Boundary Complexity, IID Rays, and Coordinate-Deletion Reconstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/88-finite-field-parity-tree-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/88-finite-field-parity-tree-shifts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/88-finite-field-parity-tree-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/88-finite-field-parity-tree-shifts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/88-finite-field-parity-tree-shifts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $q$ be a prime power, let $d\geq2$, and fix nonzero coefficients $c_1,\ldots,c_d\in\mathbb F_q$. We study labelings of the full rooted $d$-ary tree that satisfy the linear parity rule $$x_w=\sum_{j=1}^d c_jx_{wj}$$ at every vertex. Every height-$h$ block is parametrized uniquely by its $d^h$ terminal labels, so the exact block count is $q^{d^h}$. This gives a complete normalization ledger: boundary-normalized complexity is $\log q$, site-normalized complexity tends to $(d-1)\log q/d$, and double-logarithmic growth is $\log d$.

  Uniform terminal data define compatible uniform block laws and hence a shift-invariant probability measure. This measure is a homogeneous block-Markov chain with an affine-hyperplane offspring kernel. Although siblings are jointly constrained, the labels on every deterministic ray are iid uniform on $\mathbb F_q$. In the opposite direction, the full level at depth $h$ reconstructs the root through an explicit nonzero linear functional. Every proper subset of that level is independent of the root: its mutual information with the root is exactly zero, while the complete level has mutual information $\log q$. Thus an iid process on each ray coexists with an exact coordinate-deletion threshold on every complete level. The tree-shift, entropy-normalization, joint-offspring, reconstruction, and secret-sharing frameworks are assigned to their prior owners; the residual contribution is this finite-field formula package, with no absolute priority claim.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: |
  Finite-Field Parity Tree Shifts:\
  Exact Boundary Complexity, IID Rays, and Coordinate-Deletion Reconstruction
```

## Markdown 正文

# Introduction

Local constraints on a rooted tree can be invisible along every individual lineage and still be perfectly visible across a complete generation. The example in this note makes that separation exact. Labels take values in a finite field, and every parent is a fixed nondegenerate linear combination of its children. A single ray therefore sees a new uniform field element at every step, while the exponentially wide boundary carries one field symbol of purely collective information about the root.

Tree shifts of finite type and their automata-theoretic foundations are due to Aubrun and Béal [@AubrunBeal2012]. Ban and Chang developed the nonlinear-recurrence approach to finite-type tree-shift complexity and used the double-logarithmic entropy normalization [@BanChang2017]. Petersen and Salama introduced and established the site-normalized tree-shift entropy used below [@PetersenSalama2018]. These frameworks are prior. We keep both normalizations visible because the same exact block count produces different constants under them.

Tree-indexed Markov processes form another established line, including the work of Benjamini and Peres [@BenjaminiPeres1994]. In the binary case, a parent-to-pair kernel allowing conditional dependence between siblings is already the bifurcating Markov-chain framework used by Guyon [@Guyon2007]. Souissi later introduced block Markov chains on rooted trees [@Souissi2022]. Our children are not conditionally independent: given their parent, they are uniform on one affine hyperplane. We use the displayed joint-offspring factorization and claim no new Markov framework.

Root reconstruction from noisy independent-edge broadcasts is likewise an established tree problem [@EvansEtAl2000]. The law below is instead noiseless and sibling-coupled, and our result is a finite-depth statement about deleting coordinates from a complete level. We claim no general broadcasting or reconstruction theorem.

The residual results are four exact statements.

1.  Restriction to the terminal level is a bijection, giving $|\mathcal B_h|=q^{d^h}$ and an explicit root functional.

2.  Boundary, volume, and double-log normalizations are all evaluated from this one formula, without fitting a nonlinear recurrence.

3.  The compatible uniform law factors through a homogeneous joint offspring kernel, and every deterministic ray is iid uniform.

4.  The root has zero mutual information with every proper subset of a complete level but is determined by the complete level.

All four statements hold over every finite field, not only over prime fields. The accompanying control program performs exact enumeration over $\mathbb F_2,\mathbb F_3,\mathbb F_4$, and $\mathbb F_5$, together with modular row reduction over $\mathbb F_2,\mathbb F_3,\mathbb F_5$, and $\mathbb F_7$. The single $\mathbb F_4$ lane is an extension-field regression test; the all-prime-power scope comes from the proofs, not from experimental extrapolation.

## Internal collision firewall {#internal-collision-firewall .unnumbered}

Two earlier internal systems require an explicit separation. P49 concerns complete cyclic *hom* tree-shifts defined by parent--child adjacency, transient phase allocation, and Hausdorff dimension in a boundary-weighted metric. The present shift instead has a star constraint coupling all siblings to their parent; it has no transient feeder, phase optimizer, graph homomorphism constraint, or Hausdorff-dimension claim. P77 concerns a one-dimensional countable orbit closure of fixed digit-weight automatic sets, its Cantor--Bendixson tower, and cellular-automaton endomorphisms. The present system is an uncountable free-semigroup tree shift and uses neither automatic digit support nor orbit-closure topology. Accordingly, no claim or proof from either internal paper is reused.

# The parity tree shift {#sec:setup}

Fix an integer $d\geq2$ and write $D=\{1,\ldots,d\}$. The vertex set of the full rooted ordered $d$-ary tree is the free monoid $$\mathcal T_d=D^*=\bigcup_{h\geq0}D^h,$$ whose root is the empty word $\varepsilon$. Put $$\mathsf L_h=D^h,
 \qquad
 \mathsf V_h=\bigcup_{r=0}^h\mathsf L_r.$$ Thus $|\mathsf L_h|=d^h$ and $$\label{eq:volume-size}
 |\mathsf V_h|=1+d+\cdots+d^h=\frac{d^{h+1}-1}{d-1}.$$ For a labeling $x\in\mathbb F_q^{\mathcal T_d}$ and $j\in D$, define the subtree shift by $(\sigma_jx)_w=x_{jw}$.

Let $q$ be a prime power and let $$\label{eq:nonzero-coefficients}
 \boldsymbol c=(c_1,\ldots,c_d)\in(\mathbb F_q^\times)^d.$$

[\[def:shift\]]{#def:shift label="def:shift"} The finite-field parity tree shift is $$\label{eq:shift}
 X_{q,d,\boldsymbol c}
 =\left\{x\in\mathbb F_q^{\mathcal T_d}:
 x_w=\sum_{j=1}^dc_jx_{wj}\text{ for every }w\in\mathcal T_d\right\}.$$ Let $\mathcal B_h(X_{q,d,\boldsymbol c})$ be the set of its restrictions to $\mathsf V_h$.

The rule is a finite list of allowed labeled stars, so $X_{q,d,\boldsymbol c}$ is a tree shift of finite type. It is preserved by each $\sigma_j$. When $q=2$ and $c_1=\cdots=c_d=1$, the rule says that the parent is the parity, or xor, of its children. The terminology "parity" will also be used for its finite-field linear extension.

For $u=u_1\cdots u_h\in\mathsf L_h$, set $$\label{eq:path-coefficient}
 c_u=\prod_{r=1}^h c_{u_r},
 \qquad c_\varepsilon=1.$$ Every $c_u$ is nonzero by [\[eq:nonzero-coefficients\]](#eq:nonzero-coefficients){reference-type="eqref" reference="eq:nonzero-coefficients"}.

[\[thm:boundary\]]{#thm:boundary label="thm:boundary"} For every $h\geq0$, restriction to the terminal level is a bijection $$\label{eq:boundary-bijection}
 \mathcal B_h(X_{q,d,\boldsymbol c})\longrightarrow\mathbb F_q^{\mathsf L_h},
 \qquad b\longmapsto b|_{\mathsf L_h}.$$ For the inverse block, every vertex is reconstructed upward. In particular, $$\label{eq:root-reconstruction}
 b_\varepsilon=\sum_{u\in\mathsf L_h}c_ub_u.$$ Consequently $$\label{eq:block-count}
 |\mathcal B_h(X_{q,d,\boldsymbol c})|=q^{d^h},$$ and exactly $q^{d^h-1}$ of these blocks have any prescribed root label $a\in\mathbb F_q$.

Starting with arbitrary labels on $\mathsf L_h$, apply [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"} successively at levels $h-1,h-2,\ldots,0$. This constructs one legal block and shows both existence and uniqueness on $\mathsf V_h$. The block extends to an infinite tree: for each terminal vertex, choose $d-1$ child labels arbitrarily and solve for the last one using $c_d\ne0$; repeat at every new terminal level. Thus every upward-constructed block belongs to $\mathcal B_h(X_{q,d,\boldsymbol c})$.

Iterating the local equation gives [\[eq:root-reconstruction\]](#eq:root-reconstruction){reference-type="eqref" reference="eq:root-reconstruction"}. More explicitly, substituting the children of the root once produces coefficients $c_j$; each additional substitution multiplies the coefficient along the new edge, yielding $c_u$ after $h$ levels. The bijection now gives [\[eq:block-count\]](#eq:block-count){reference-type="eqref" reference="eq:block-count"}. Finally, the right side of [\[eq:root-reconstruction\]](#eq:root-reconstruction){reference-type="eqref" reference="eq:root-reconstruction"} is a nonzero linear functional on the $d^h$-dimensional space $\mathbb F_q^{\mathsf L_h}$. Each fiber is an affine hyperplane of cardinality $q^{d^h-1}$.

The root-refined block count also closes the Ban--Chang nonlinear recurrence in one line. If $A_h(a)$ denotes the number of height-$h$ blocks rooted at $a$, then $A_h(a)$ is independent of $a$; writing the common value as $A_h$ gives $$\label{eq:snre-collapse}
 A_0=1,
 \qquad A_{h+1}=q^{d-1}A_h^d,
 \qquad A_h=q^{d^h-1}.$$ Indeed there are $q^{d-1}$ child tuples with a prescribed parent, and the $d$ rooted subblocks can then be selected independently. Equation [\[eq:snre-collapse\]](#eq:snre-collapse){reference-type="eqref" reference="eq:snre-collapse"} is a specialization of the prior nonlinear- recurrence framework, not a new recurrence formalism.

# A normalization ledger {#sec:complexity}

Because tree volumes grow exponentially with height, the word "entropy" has been used for more than one normalization. We therefore state the unambiguous finite-height quantity first: $$\label{eq:finite-complexity}
 C_h:=\log|\mathcal B_h(X_{q,d,\boldsymbol c})|=d^h\log q.$$ All logarithms are natural.

[\[thm:complexity\]]{#thm:complexity label="thm:complexity"} For every $h\geq0$, the boundary- and site-normalized complexities satisfy the first two identities below. For every $h\geq1$, the double-logarithmic complexity satisfies the third: $$\begin{aligned}
 \frac{C_h}{|\mathsf L_h|}
   &=\log q,\label{eq:boundary-rate}\\
 \frac{C_h}{|\mathsf V_h|}
   &=\frac{(d-1)d^h}{d^{h+1}-1}\log q
     \longrightarrow\frac{d-1}{d}\log q,\label{eq:site-rate}\\
 \frac{\log C_h}{h}
   &=\log d+\frac{\log\log q}{h}
     \longrightarrow\log d.\label{eq:double-log-rate}\end{aligned}$$ In particular, the Petersen--Salama site-normalized entropy is $(d-1)\log q/d$, while the Ban--Chang double-logarithmic entropy is $\log d$.

Insert [\[eq:finite-complexity\]](#eq:finite-complexity){reference-type="eqref" reference="eq:finite-complexity"}, $|\mathsf L_h|=d^h$, and [\[eq:volume-size\]](#eq:volume-size){reference-type="eqref" reference="eq:volume-size"}. The three displayed identities and their limits follow directly.

::: {#tab:normalizations}
  Normalization                 Finite-height value   Limit
  ----------------------------- --------------------- -----------------
  terminal level                $C_h/d^h$             $\log q$
  all sites                     $C_h/|\mathsf V_h|$   $(d-1)\log q/d$
  double logarithm ($h\geq1$)   $(\log C_h)/h$        $\log d$

  : The same exact block count under three normalizations. The first row is retained as a boundary complexity rather than called a third standard entropy.
:::

The coefficient $\log q$ in $|\mathcal B_h|=\exp((\log q)d^h)$ records one free field symbol per terminal site. By contrast, the full tree shift on $q$ symbols has one free symbol at every site and hence the larger site-normalized rate $\log q$. The parity rule removes precisely the internal-site degrees of freedom.

# The compatible uniform block-Markov law {#sec:measure}

Let $\nu_h$ be the uniform probability on $\mathcal B_h(X_{q,d,\boldsymbol c})$. The next proposition shows that these finite laws define one infinite law without a boundary choice at infinity.

[\[prop:compatible\]]{#prop:compatible label="prop:compatible"} The restriction map from height $h+1$ to height $h$ has constant fiber size $$\label{eq:restriction-fiber}
 q^{(d-1)d^h}=q^{d^{h+1}-d^h}.$$ Hence the laws $(\nu_h)_{h\geq0}$ are projectively compatible and determine a probability measure $\mu_{q,d,\boldsymbol c}$ on $X_{q,d,\boldsymbol c}$. It satisfies $$\label{eq:uniform-cylinder}
 \mu_{q,d,\boldsymbol c}([b])=q^{-d^h}
 \qquad(b\in\mathcal B_h),$$ and is invariant under every subtree shift $\sigma_j$.

Fix a legal block on $\mathsf V_h$. At each of its $d^h$ terminal vertices, a child tuple must satisfy one nonzero linear equation in $d$ variables. It has $q^{d-1}$ solutions. The choices at distinct terminal vertices are independent, proving [\[eq:restriction-fiber\]](#eq:restriction-fiber){reference-type="eqref" reference="eq:restriction-fiber"}. Uniform measures therefore push forward to uniform measures. The projective-limit measure exists because the alphabet is finite, and [\[eq:uniform-cylinder\]](#eq:uniform-cylinder){reference-type="eqref" reference="eq:uniform-cylinder"} follows from [\[eq:block-count\]](#eq:block-count){reference-type="eqref" reference="eq:block-count"}.

For shift invariance, fix a vertex $v$ and a height $h$. The labels at the $d^h$ descendants $vu$, $u\in\mathsf L_h$, are an iid uniform subcollection of the uniform level $|v|+h$. Upward reconstruction inside the subtree rooted at $v$ therefore gives the uniform law on $\mathcal B_h$. Cylinder sets generate the Borel sigma-field, so every $\sigma_j$ preserves $\mu_{q,d,\boldsymbol c}$.

For $a\in\mathbb F_q$ and $y=(y_1,\ldots,y_d)\in\mathbb F_q^d$, define $$\label{eq:offspring-kernel}
 K(a;y_1,\ldots,y_d)
 =q^{-(d-1)}\mathbf 1
   \left\{a=\sum_{j=1}^dc_jy_j\right\}.$$ This is a probability kernel from a parent to its ordered child block. For $h\geq1$ and a labeling $b$ of $\mathsf V_h$, $$\label{eq:block-markov-factorization}
 \mu_{q,d,\boldsymbol c}([b])
 =q^{-1}\prod_{w\in\mathsf V_{h-1}}
 K(b_w;b_{w1},\ldots,b_{wd}),$$ with the convention that the right side is zero when a local rule fails. For $h=0$, the factorization consists only of the root factor $q^{-1}$. For a legal block, the exponent is $1+(d-1)|\mathsf V_{h-1}|=d^h$, so [\[eq:block-markov-factorization\]](#eq:block-markov-factorization){reference-type="eqref" reference="eq:block-markov-factorization"} agrees with [\[eq:uniform-cylinder\]](#eq:uniform-cylinder){reference-type="eqref" reference="eq:uniform-cylinder"}. Thus the measure is a homogeneous block Markov chain in the joint-offspring sense of [@Souissi2022].

[\[lem:local-uniform\]]{#lem:local-uniform label="lem:local-uniform"} Fix a parent value $a\in\mathbb F_q$. Under the kernel $K(a;\cdot)$, every proper subset of the $d$ child coordinates is iid uniform on the corresponding power of $\mathbb F_q$, and its law does not depend on $a$.

Fix $s<d$ child coordinates and prescribe their values. At least one child coordinate remains free, and its coefficient is nonzero. The residual linear equation in $d-s$ variables has exactly $q^{d-s-1}$ solutions. There are $q^{d-1}$ offspring tuples in total. The probability of each prescribed $s$-tuple is therefore $q^{d-s-1}/q^{d-1}=q^{-s}$, independently of the parent value.

The lemma shows why a standard independent-offspring branching description would be inaccurate: a complete sibling block lies on a codimension-one hyperplane. Every proper sibling subblock nevertheless looks exactly independent.

[\[thm:ray\]]{#thm:ray label="thm:ray"} Let $$w_0=\varepsilon,
 \qquad w_{r+1}=w_rj_{r+1}
 \quad(r\geq0)$$ be any deterministic ray. Under $\mu_{q,d,\boldsymbol c}$, the process $(X_{w_r})_{r\geq0}$ is iid with common law $\operatorname{Unif}(\mathbb F_q)$. Equivalently, for all $h\geq0$ and $a_0,\ldots,a_h\in\mathbb F_q$, $$\label{eq:ray-law}
 \mu_{q,d,\boldsymbol c}
 \{X_{w_0}=a_0,\ldots,X_{w_h}=a_h\}=q^{-(h+1)}.$$

The root is uniform by [\[eq:uniform-cylinder\]](#eq:uniform-cylinder){reference-type="eqref" reference="eq:uniform-cylinder"} with $h=0$. By [\[eq:block-markov-factorization\]](#eq:block-markov-factorization){reference-type="eqref" reference="eq:block-markov-factorization"}, conditional on the labels through one generation, the ordered offspring block at each exposed vertex has kernel $K$. Lemma [\[lem:local-uniform\]](#lem:local-uniform){reference-type="ref" reference="lem:local-uniform"} with a single selected child says that the next label on the ray is uniform and its conditional law does not depend on the parent or on the earlier ray labels. Multiplying these $h+1$ conditional probabilities proves [\[eq:ray-law\]](#eq:ray-law){reference-type="eqref" reference="eq:ray-law"}.

Ray iid should not be confused with independence of the whole tree. The next section gives the strongest possible obstruction: one complete level determines the root exactly.

# Exact coordinate-deletion reconstruction {#sec:reconstruction}

Let $R=X_\varepsilon$ and let $Z_h=(X_u)_{u\in\mathsf L_h}$. For a subset $A\subseteq\mathsf L_h$, write $Z_A=(X_u)_{u\in A}$. Shannon entropy and mutual information are computed with natural logarithms.

For a fixed depth, the information condition "all coordinates recover, while every proper coordinate subset reveals nothing" is the perfect $(n,n)$ threshold criterion from classical secret sharing, introduced independently by Blakley and Shamir [@Blakley1979; @Shamir1979]. We claim neither that access structure nor its additive finite-field mechanism. The calculation below identifies its simultaneous realization at every depth by one shift-invariant tree law.

[\[thm:threshold\]]{#thm:threshold label="thm:threshold"} For every $h\geq1$, the complete level is an iid uniform vector in $\mathbb F_q^{d^h}$ and $$\label{eq:root-from-level}
 R=\sum_{u\in\mathsf L_h}c_uX_u
 \quad\text{almost surely, and indeed pointwise on }X_{q,d,\boldsymbol c}.$$ For every proper subset $A\subsetneq\mathsf L_h$, $$\label{eq:proper-independence}
 \mu(R=a,Z_A=z)=q^{-(|A|+1)}
 \quad(a\in\mathbb F_q,\ z\in\mathbb F_q^A).$$ Consequently $$\begin{aligned}
 \operatorname{H}(R\mid Z_A)&=\log q,
 &\operatorname{I}(R;Z_A)&=0,\label{eq:proper-information}\\
 \operatorname{H}(R\mid Z_h)&=0,
 &\operatorname{I}(R;Z_h)&=\log q.
 \label{eq:full-information}\end{aligned}$$

The terminal-level bijection and the uniform block law show that $Z_h$ is uniform on $\mathbb F_q^{\mathsf L_h}$, hence its coordinates are iid uniform. Equation [\[eq:root-from-level\]](#eq:root-from-level){reference-type="eqref" reference="eq:root-from-level"} is [\[eq:root-reconstruction\]](#eq:root-reconstruction){reference-type="eqref" reference="eq:root-reconstruction"}.

Fix $A\subsetneq\mathsf L_h$ and condition on $Z_A=z$. Choose one omitted vertex $v\in\mathsf L_h\setminus A$. All coefficients $c_u$ are nonzero, so $c_vX_v$ is uniform on $\mathbb F_q$ and independent of the conditioned coordinates. Even after conditioning on every other omitted coordinate, the sum in [\[eq:root-from-level\]](#eq:root-from-level){reference-type="eqref" reference="eq:root-from-level"} is therefore uniform. Removing that extra conditioning leaves $\mu(R=a\mid Z_A=z)=q^{-1}$. Since $\mu(Z_A=z)=q^{-|A|}$, this proves [\[eq:proper-independence\]](#eq:proper-independence){reference-type="eqref" reference="eq:proper-independence"}.

The root is uniform, so $\operatorname{H}(R)=\log q$. Independence gives [\[eq:proper-information\]](#eq:proper-information){reference-type="eqref" reference="eq:proper-information"}; deterministic reconstruction gives [\[eq:full-information\]](#eq:full-information){reference-type="eqref" reference="eq:full-information"}.

Thus deleting even one label from a complete level removes all information about the root, not merely some fraction of it. The phenomenon is high-order: every finite ray is a product process by Theorem [\[thm:ray\]](#thm:ray){reference-type="ref" reference="thm:ray"}, and the whole generation is also an unconditional product vector, yet one linear combination of all generation coordinates equals the root.

[\[rem:assumptions\]]{#rem:assumptions label="rem:assumptions"} The condition $d\geq2$ is needed for ray iid: with one child the local rule determines that child from its parent. Nonzero coefficients are needed for the all-proper-subsets statement. If $c_j=0$, then at level one the root is already reconstructed after child $j$ is omitted, so [\[eq:proper-information\]](#eq:proper-information){reference-type="eqref" reference="eq:proper-information"} fails. Boundary parametrization alone is less restrictive; the assumptions are frozen because the combined theorem package requires all of them.

# Owner subtraction, controls, and scope {#sec:scope}

::: {#tab:owners}
  Source or internal system   Owned framework                                   Residual here
  --------------------------- ------------------------------------------------- -------------------------------------------------
  Aubrun--Béal                finite-type and sofic tree shifts                 one affine-star family
  Ban--Chang                  SNRE and double-log entropy                       closed scalar count $q^{d^h}$
  Petersen--Salama            site-normalized tree entropy                      exact rate $(d-1)\log q/d$
  Benjamini--Peres            tree-indexed Markov processes                     no new general process
  Guyon; Souissi              joint sibling kernels and block-Markov language   explicit $d$-ary affine kernel and iid rays
  Evans et al.                tree broadcasting and root reconstruction         noiseless coordinate-deletion law
  Blakley; Shamir             perfect threshold secret sharing                  one law at every tree depth
  Internal P49                hom-tree Hausdorff phase allocation               no parent--child graph or phase optimization
  Internal P77                one-dimensional automatic towers                  no automatic support or Cantor--Bendixson claim

  : Ownership and collision boundary. "Residual here" means the specialized calculation proved in this note, not a priority assertion.
:::

The broad object, both entropy conventions, the joint-offspring and block-Markov language, noisy reconstruction, and the threshold access condition are therefore subtracted from the contribution. A bounded primary-source audit through 28 August 2026 did not locate the combined finite-field formula package stated here. That sentence records a search boundary only; it is not a claim of worldwide novelty. Public posting, submission, author contact, and priority language remain on **HOLD**.

The accompanying script `code/verify_parity_tree.py` uses only the Python standard library. Its two lanes are deliberately redundant.

1.  The enumeration lane constructs every block from every terminal word, checks local legality and injectivity, brute-forces all legal labelings in the smallest cases, measures restriction-fiber multiplicities, enumerates every deterministic ray, and compares complete joint tables for the root and every proper terminal subset in selected cases.

2.  The rank lane forms the local constraint matrix over $\mathbb F_p$, verifies its rank and nullity, constructs the full boundary-extension matrix, checks that it lies in the constraint kernel, and certifies that adjoining the root functional increases the rank of every tested proper observation matrix by one.

The recorded run covers $8{,}315$ enumerated blocks, $811$ exhaustive proper subsets, $78$ constraint rows, $567$ observation-rank certificates, and $19{,}764$ assertions. These finite controls are not proofs of arbitrary $q,d,h$. The implementation has one exhaustive $\mathbb F_4$ lane, while its rank lane handles prime fields only; all-prime-power scope rests on the finite-field arguments in Theorems [\[thm:boundary\]](#thm:boundary){reference-type="ref" reference="thm:boundary"} and [\[thm:threshold\]](#thm:threshold){reference-type="ref" reference="thm:threshold"}.

# Conclusion

The parity tree shift has one free field coordinate per terminal vertex and no other finite-block degrees of freedom. That leaf parametrization gives the entire complexity ledger and a canonical compatible uniform measure. The same measure has two opposing exact faces: every lineage is iid, while every complete generation reconstructs the root and loses all root information after any coordinate is deleted. The coefficient of each terminal label is simply the product of the edge coefficients along its path, so nondegeneracy at one local star propagates to every depth.

The scope is intentionally narrow. We do not classify general linear tree shifts with several equations, spatially varying coefficients, missing coefficients, noisy parity checks, or nonlinear local rules. Those changes can alter rank density, compatibility, or the sharp reconstruction threshold. A natural next problem is to replace the single parity equation by a matrix-valued local code and determine which rank profiles preserve iid rays while producing a nontrivial hierarchy of boundary information.
