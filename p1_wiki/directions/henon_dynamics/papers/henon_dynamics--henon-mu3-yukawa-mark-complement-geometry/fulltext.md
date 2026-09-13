---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-complement-geometry"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/paper/main.pdf"
source_sha256: "b4b0fbc5ea3ce8201950f9d1bac54d36830dda9046dc4db5b5026fee70275286"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Intersection Geometry of Complements in a Restricted Mark Cokernel

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_complement_geometry>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An exact restricted mark cokernel was previously split as $C=D\oplus K$, with $D\cong\mathbb Z/8\oplus(\mathbb Z/2)^2$ and exactly $2^{41}$ complements. We determine the intersection geometry of the entire complement family. Relative to any fixed complement, the possible intersection indices are $1,2,4,8,16,32$, and we give the exact multiplicity of every index and every intersection-quotient type. The common intersection of all complements is $8C\cong\mathbb Z/3\oplus\mathbb Z/18$, whereas their generated span is all of $C$. Finally, we compute the orders of the sixteen named classes in this common core and find exactly twenty-five generating triples, all containing the ninth class. Every claim remains on the frozen sixteen-type support.
author:
- Anonymous
title: Intersection Geometry of Complements in a Restricted Mark Cokernel
```

## Markdown 正文

# Graph model and scope

Fix the C69 decomposition $C=D\oplus K$. In primary exponent notation, $$D:(3,1,1),\qquad K_{(2)}:(4,2,2,2,1^8),\qquad K_{(3)}:(2,1).$$ Every complement of $D$ is uniquely the graph $$\Gamma_f=\{(f(k),k):k\in K\},\qquad f\in\operatorname{Hom}(K,D).$$ The parameter group is $$\operatorname{Hom}(K,D)\cong(\mathbb Z/2)^{32}\oplus(\mathbb Z/4)^3\oplus\mathbb Z/8,
 \qquad |\operatorname{Hom}(K,D)|=2^{41}.$$ For two parameters $f,g$ one has $$\label{eq:graph}
 \Gamma_f\cap\Gamma_g\cong\ker(f-g),\qquad
 K/\ker(f-g)\cong\operatorname{im}(f-g).$$ Thus all intersection statistics are translation invariant in the affine parameter group. Throughout, "intersection index" means $$[\Gamma_f:\Gamma_f\cap\Gamma_g]=[K:\ker(f-g)]=|\operatorname{im}(f-g)|,$$ not the index of the intersection in $C$.

The scope firewall is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ We do not claim a canonical complement, a complete classification of the abstract kernel types, a full table of marks or Burnside ring, arithmetic or local data, Euler factors, root numbers, automorphy, or a Hilbert--Polya operator.

# Exact quotient-type distribution

For a subgroup type $H\leq D$, the number of maps $K\to D$ with image of type $H$ is $$\label{eq:imagecount}
 N_D(H)\,E_K(H),$$ where $N_D(H)$ counts subgroups of $D$ of type $H$ and $E_K(H)$ counts epimorphisms from $K$ onto one fixed copy of $H$. The producer obtains $E_K(H)$ by strict inversion on the concrete 38-element subgroup poset of $D$. Independently, the checker uses $$E_K(H)=N_K(H)|\operatorname{Aut}(H)|,$$ because finite duality sends epimorphisms $K\to H$ to injections $H^\vee\to K^\vee$, and these groups are abstractly self-dual. Birkhoff's subgroup formula evaluates both $N_D(H)$ and $N_K(H)$.

::: {#tab:types}
  $H\cong K/\ker f$                      $N_D(H)$        $E_K(H)$   maps with image type $H$
  ------------------------------------ ---------- --------------- --------------------------
  $0$                                           1               1                          1
  $\mathbb Z/2$                                 7            4095                      28665
  $\mathbb Z/4$                                 4           61440                     245760
  $(\mathbb Z/2)^2$                             7        16764930                  117354510
  $\mathbb Z/8$                                 4           65536                     262144
  $\mathbb Z/2\oplus\mathbb Z/4$                6       251535360                 1509212160
  $(\mathbb Z/2)^3$                             1     68602093560                68602093560
  $\mathbb Z/2\oplus\mathbb Z/8$                6       268304384                 1609826304
  $(\mathbb Z/2)^2\oplus\mathbb Z/4$            1   1029282693120              1029282693120
  $\mathbb Z/8\oplus(\mathbb Z/2)^2$            1   1097901539328              1097901539328

  : Exact image, hence intersection-quotient, distribution from every fixed complement.
:::

From every fixed complement, the numbers of complements at intersection indices $1,2,4,8,16,32$ are respectively $$1,\ 28665,\ 117600270,\ 70111567864,\
 1030892519424,\ 1097901539328.$$ Their sum is $2^{41}$. Table [1](#tab:types){reference-type="ref" reference="tab:types"} refines these six values into all ten possible quotient types.

Equation [\[eq:graph\]](#eq:graph){reference-type="eqref" reference="eq:graph"} makes the index equal to $|\operatorname{im}(f-g)|$. Summing Equation [\[eq:imagecount\]](#eq:imagecount){reference-type="eqref" reference="eq:imagecount"} over subgroup types of each order gives the displayed values. Translation by $f$ is a bijection of $\operatorname{Hom}(K,D)$, so the same row occurs at every fixed complement. Multiplying by $2^{41}$ gives ordered-pair counts; halving the off-diagonal rows gives unordered-pair counts, all recorded in the exact evidence.

# The common core and total span

An element common to every graph must first lie in $\Gamma_0$, hence has the form $(0,k)$, and it belongs to all graphs precisely when every homomorphism $K\to D$ kills $k$. Since $D$ has exponent eight, $8K$ is contained in this universal kernel. Conversely, the cyclic $\mathbb Z/8$ summand of $D$ separates every class outside $8K$ on the dyadic primary part. The odd-primary part is killed by every map to $D$ and multiplication by eight is invertible there. Therefore the universal kernel is exactly $8K$.

The complement family satisfies $$\bigcap_f\Gamma_f=8C\cong\mathbb Z/3\oplus\mathbb Z/18,
 \qquad |8C|=54,$$ and $$\left\langle\Gamma_f:f\in\operatorname{Hom}(K,D)\right\rangle=C.$$ Indeed, from every fixed complement there are $1097901539328$ other parameters whose difference is surjective, and each such pair already generates $C$.

Because $8D=0$, the preceding universal-kernel argument identifies the intersection with $8K=8C$. Multiplication by eight on the primary factors of $K$ leaves one $\mathbb Z/2$, together with $\mathbb Z/3\oplus\mathbb Z/9$; combining coprime factors gives $\mathbb Z/3\oplus\mathbb Z/18$. If $f-g$ is surjective, differences of elements of $\Gamma_f$ and $\Gamma_g$ generate $D$, while either graph maps onto $K$. The last row of Table [1](#tab:types){reference-type="ref" reference="tab:types"} counts all such differences.

# Named generators of the core

Let $e_1,\ldots,e_{16}$ be the named coordinate classes in the frozen mark presentation. Exact rational residues, or independently Hermite lattices, give $$\bigl(|8[e_j]|\bigr)_{j=1}^{16}
 =(9,3,3,3,1,1,9,3,2,1,3,3,1,1,9,9).$$ No singleton or pair among these elements generates the order-$54$ core. Exactly twenty-five triples do. Every one contains $8[e_9]$; after removing that common element, the possible index pairs are $$\begin{split}
&(1,3),(1,4),(1,7),(1,8),(1,11),(1,12),(1,15),(1,16),\\
&(3,7),(3,15),(3,16),(4,7),(4,15),(4,16),\\
&(7,8),(7,11),(7,12),(7,16),(8,15),(8,16),\\
&(11,15),(11,16),(12,15),(12,16),(15,16).
\end{split}$$ This is a statement about the named presentation, not a canonical generating set for the abstract group.

# Reproducibility and conclusion

The evidence binds the exact C64, corrected C69, and C70 bytes. Producer and checker use separate image-count routes: concrete subgroup-poset inversion versus Birkhoff counts and epimorphism duality. GAP independently enumerates all 38 target subgroups in ten types. SymPy Smith and Hermite calculations recover the common core, all named orders, and all twenty-five triples. Clean replay passes and forty-two hostile semantic mutations are rejected. C71 therefore resolves both the local pair-intersection distribution and the two global extrema of the complement family: its common core and its total span.
