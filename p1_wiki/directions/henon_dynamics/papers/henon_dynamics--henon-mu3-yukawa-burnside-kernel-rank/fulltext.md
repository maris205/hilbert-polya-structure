---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-burnside-kernel-rank"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/paper/main.pdf"
source_sha256: "25e73a0c98749b46185baf7a06bdf87dd23159aeaed7e5ad5cf55654db611555"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Primitive Four-versus-Four Burnside Relation from a \texorpdfstring$W(E_6)$W(E6) Lambda-Square Shadow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Equal permutation characters can hide relations among nonconjugate finite sets. We expose one such relation in the degree-320 Hénon $W(E_6)$-Gassmann construction. Starting from the complete exterior- and symmetric-square atlas of the two C61 permutation sets, we rebind the ambient group, enumerate its 25 conjugacy classes, and recompute the fixed-coset character matrix on the 16 ambient-conjugacy subgroup types. The resulting $25\times16$ integer matrix has rank 13. Its exterior-square difference is the primitive four-versus-four relation $$[G/S_2]+[G/S_3]+[G/S_5]+[G/S_6]
   = [G/S_{11}]+[G/S_{12}]+[G/S_{13}]+[G/S_{14}],$$ where the eight core-free types have degrees $480,480,4320,4320$ on each side. A support-restricted rank-7 certificate proves that no proper subset supports a further relation. We also locate the original C61 relation and an inherited C60 collision inside the full three-dimensional restricted kernel. The result is finite-group/Burnside evidence only; no arithmetic resolvent, local-field, bad-Euler-factor, or root-number claim is made.
author:
- Anonymous Authors
bibliography:
- references.bib
title: 'A Primitive Four-versus-Four Burnside Relation from a $W(E_6)$ Lambda-Square Shadow'
```

## Markdown 正文

# Introduction

Gassmann equivalence is deliberately subtle: two transitive $G$-sets can have the same rational permutation character even when their stabilizers are not conjugate. The first two degree-two lambda shadows of the C61 $W(E_6)$ pair make this tension visible. C62 computed the complete exterior-square and symmetric-square orbit atlases, but left open a structural question: which relation in the linearization kernel is actually being seen by the exterior-square atlas?

This paper answers that question on a precisely bounded submodule. We take the 16 subgroup-conjugacy types recorded by C62, evaluate their transitive permutation characters on all 25 conjugacy classes of $W(E_6)$, and perform an exact rational rank computation. The exterior-square difference is not merely a vanishing character vector. It is a support-minimal four-versus-four Burnside relation among eight nonconjugate fixed-field types.

Our contributions are:

1.  We give an independent, source-bound reconstruction of the 25-class $W(E_6)$ character matrix on the 16 C62 types and certify rank 13 and nullity 3.

2.  We identify the primitive relation $R_4$ exposed by the exterior square and prove support minimality by a rank-7 restriction, rather than by subgroup order or a table position.

3.  We place the relation next to the original C61 Gassmann direction and the symmetric-square relation, while explicitly treating the $S_9-S_{10}$ collision as inherited C60 material rather than a new claim.

All statements are scoped by `NO_BAD_EULER_OR_ROOT_NUMBER`. In particular, the word "field" below means the core-free fixed-field type supplied by the C62 finite-group atlas; we do not infer local arithmetic data from its degree or normalizer.

# Relation to prior work

The linearization map from finite $G$-sets to permutation characters is a classical Burnside-ring construction [@burnside1911]. Gassmann's criterion and its number-field interpretation explain why equality of these characters can coexist with nonconjugate stabilizers [@gassmann1926; @perlis1977]. C63 uses these general mechanisms only as background. Its claim is the bounded, instance-specific computation on the 16 subgroup types produced by C62: the lambda-square difference selects an eight-column support whose restricted kernel is one-dimensional. We do not claim a new general theorem about Burnside rings or Gassmann equivalence.

# Finite-group setup

Let $G=W(E_6)$, with $|G|=51840$, and let $H_+,H_-$ be the two order-162 stabilizers in the released C61 source contract. Put $X_\pm=G/H_\pm$, so $|X_\pm|=320$. C62 enumerated the $G$-orbits on 2-subsets and size-two multisets of each $X_\pm$, and grouped the complete stabilizer element sets by ambient conjugacy. We denote the resulting 16 types by $S_1,\ldots,S_{16}$, and write $$Y_i=[G/S_i]$$ for the corresponding transitive basis symbols.

For $g\in G$, let $C(g)$ be its conjugacy class and let $c(g)=|C_G(g)|$. The fixed-coset formula used in the producer is $$\chi_{G/S}(g)=\frac{c(g)\,|S\cap C(g)|}{|S|}.
 \label{eq:fixed-coset}$$ It follows by counting pairs $(x,s)$ with $x^{-1}gx=s$. Formula [\[eq:fixed-coset\]](#eq:fixed-coset){reference-type="eqref" reference="eq:fixed-coset"} uses complete subgroup element sets, so it does not identify types using only $|S|$.

The C62 lambda identities explain why a relation must occur: $$\chi_{\Lambda^2X}(g)=\frac{\chi_X(g)^2-\chi_X(g^2)}2,
 \qquad
 \chi_{\operatorname{Sym}^2X}(g)=\frac{\chi_X(g)^2+\chi_X(g^2)}2.$$ Since C61 has $\chi_{X_+}=\chi_{X_-}$, both lambda differences linearize to zero. C63 determines their exact support in the 16-type basis.

# Main result

Let $M$ be the matrix with one row for each of the 25 conjugacy classes of $G$, one column for each $Y_i$, and entries given by [\[eq:fixed-coset\]](#eq:fixed-coset){reference-type="eqref" reference="eq:fixed-coset"}.

The matrix $M$ has $$\operatorname{rank}_{\mathbb{Q}} M=13,
 \qquad \dim_{\mathbb{Q}}\ker M=3.$$ A basis is $$\begin{aligned}
 z_1&=Y_{10}-Y_9,\\
 z_2&=-Y_2-Y_3-Y_5-Y_6+Y_{11}+Y_{12}+Y_{13}+Y_{14},\\
 z_3&=Y_{16}-Y_{15}.\end{aligned}$$ The C61 difference is $r=Y_{15}-Y_{16}=-z_3$. The C62 differences are $$q_{\Lambda}=Y_2+Y_3+Y_5+Y_6-Y_{11}-Y_{12}-Y_{13}-Y_{14}=-z_2,
 \qquad q_{\operatorname{Sym}}=q_{\Lambda}+r.$$ On the eight-term support of $q_{\Lambda}$, the restricted matrix has rank 7. Hence its rational kernel is one-dimensional and $q_{\Lambda}$ has no nonzero proper-support subrelation.

The theorem is intentionally a statement about the 16-type submodule, not a classification of the full Burnside ring of $G$. The vector $z_1$ is an inherited C60 order-4 collision and is included to prevent a false novelty claim.

# The four-versus-four support

The eight terms of $q_\Lambda$ split into two degree blocks. Every listed subgroup is core-free; the order and normalizer data come directly from the C62 element-set atlas.

   side                 degrees
  ------- ---------- ---------- ---------- ---------- ---------------------
   plus        $S_2$      $S_3$      $S_5$      $S_6$  $480,480,4320,4320$
   minus    $S_{11}$   $S_{12}$   $S_{13}$   $S_{14}$  $480,480,4320,4320$

The order-108 pair $(S_2,S_3)$ and $(S_{11},S_{12})$ contributes degree 480 fields; the order-12 pair $(S_5,S_6)$ and $(S_{13},S_{14})$ contributes degree 4320 fields. The four plus types and four minus types are distinct ambient-conjugacy classes even when their subgroup orders agree. Their total degree is 9600 on each side.

To make "primitive" checkable, let $M_{R_4}$ be the submatrix obtained by retaining only these eight columns. Exact elimination gives $$\operatorname{rank}_{\mathbb{Q}}M_{R_4}=7,
 \qquad \dim_{\mathbb{Q}}\ker M_{R_4}=1.$$ Since all eight coefficients of $q_\Lambda$ are nonzero, any vector in this one-dimensional kernel has the same support. This rules out a hidden two-term or smaller relation inside the C62 support.

# Where the lambda shadows land

The diagonal multisets in $\operatorname{Sym}^2X_\pm$ form copies of $X_\pm$. Therefore the symmetric difference is forced to be the exterior difference plus the original C61 difference: $$[\operatorname{Sym}^2X_+]-[\operatorname{Sym}^2X_-]
 =([\Lambda^2X_+]-[\Lambda^2X_-])+([X_+]-[X_-]).$$ The producer recovers exactly $q_{\operatorname{Sym}}=q_\Lambda+r$. This identity is useful as a semantic check: treating the symmetric atlas as an unrelated second relation would double-count the diagonal direction.

The remaining basis vector $z_1$ has equal character but comes from the degree-12960 types $S_9,S_{10}$. C60 already recorded that collision, so C63 uses it only as a control for the rank computation. The new content is the eight-term support exposed by the lambda-square shadow and the proof that it is primitive inside the recorded submodule.

# Fixed-field and zeta interpretation

Every $S_i$ in the C62 dictionary is core-free, and its fixed-field degree is $51840/|S_i|$. Thus the four-versus-four relation can be read as an equality of formal permutation characters attached to eight fixed fields in the common finite normal-closure model. When the corresponding Artin formalism is invoked, it gives the product identity $$\prod_{i\in\{2,3,5,6\}} L(s,\mathbf{1}_{S_i})
 =
 \prod_{i\in\{11,12,13,14\}} L(s,\mathbf{1}_{S_i}).$$ This sentence records only the character-level identity. We do not expand arithmetic resolvents, identify discriminants or maximal orders, classify local extensions, or separate bad Euler factors and root numbers.

# Reproducibility

The producer reads the frozen C61 group bytes and the C62 atlas/dictionary bytes, verifies their SHA-256 digests, and reconstructs every subgroup and conjugacy class. The evidence matrix digest is `e912b0f37f69ac1e23cf432915aa4258818312f84fba776986876c7625a84a9b`. The commands are:

    python3 -m py_compile code/*.py
    python3 code/c63_kernel.py
    python3 code/c63_kernel_checker.py
    python3 code/c63_mutation_test.py

The hostile suite rejects mutations of source hashes, matrix entries, rank, kernel vectors, support rank, scope, and nonclaim flags.

# Limitations and conclusion

C63 is scoped to a finite list of 16 core-free subgroup types inherited from the C62 atlas. It does not assert that the displayed three-dimensional kernel is the kernel of the full Burnside ring, nor does it make arithmetic local or analytic claims. Within that boundary, the lambda-square operation does more than reproduce a character equality: it exposes a support-minimal four-versus-four relation whose exact rank certificate distinguishes it from both the original C61 direction and the inherited C60 collision.

# Conjugacy-class audit

For reproducibility, the deterministic class-size vector used by the evidence is $$\begin{split}
(&1,36,240,270,1440,1620,5184,540,2160,1440,6480,3240,4320,\\
 &540,540,45,5184,480,1440,4320,4320,5760,720,1440,80).
\end{split}$$ It sums to 51840. The corresponding centralizer orders are obtained by dividing 51840 by each entry. The JSON evidence stores the representative permutation for every class, the full 25-by-16 matrix, and all relation vectors, so the displayed digest is not a compact substitute for the data.
