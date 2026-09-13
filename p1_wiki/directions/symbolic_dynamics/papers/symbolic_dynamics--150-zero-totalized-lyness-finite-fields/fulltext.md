---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--150-zero-totalized-lyness-finite-fields"
canonical_tex: "symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields/main.tex"
canonical_pdf: "symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields/main.pdf"
source_sha256: "ce5b87615188ab870700e1f3eee0e892ea090c5e18328ae86d893204262acf9b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The All-Affine Functional Graph of the Zero-Totalized Lyness Map over Odd Finite Fields

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/150-zero-totalized-lyness-finite-fields/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $\mathbb F_q$ be a finite field of odd order, set $\operatorname{inv}_0(0)=0$ and $\operatorname{inv}_0(x)=x^{-1}$ for $x\ne0$, and consider the all-affine self-map $\mathsf L(x,y)=(y,(1+y)\operatorname{inv}_0(x))$. We determine its complete functional graph. The plane splits disjointly into a generic Lyness locus, the two coordinate axes, and three exceptional tail layers. The recurrent set has $q^2-3q+5$ points, while the tail polynomial is $$(q^2-3q+5)+(q-1)z+(q-2)z^2+(q-2)z^3;$$ thus the maximum tail is exactly three for every odd $q$. If $r_q$ counts the roots of $a^2-a-1$, then the graph has $1+r_q$ fixed points, two 2-cycles, $(q-3)/2$ 4-cycles, and $((q-2)(q-3)-r_q)/5$ 5-cycles. We also prove a codomain-wide inverse law: fibres have size $q$ at $(-1,0)$, size zero at $(-1,v)$ for $v\ne0$, and size one elsewhere. Classical Lyness five-periodicity, QRT and cluster interpretations, and general finite-field birational dynamics receive zero contribution credit. The residual result is the exact zero-totalized affine boundary completion. External release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'The All-Affine Functional Graph of the Zero-Totalized Lyness Map over Odd Finite Fields'
```

## Markdown 正文

# Scope and complete statement

The parameter-one Lyness recurrence and its five-cycle are classical. The same map is a basic QRT system and a type-$A_2$ cluster example [@Lyness1942; @HoneKouloukas2023; @Hone2020]. Integrable birational maps over finite fields also admit general algebraic-geometric and almost-good-reduction treatments [@JogiaRobertsVivaldi2006; @Kanki2013]. Kanki resolves division-by-zero obstructions by extending/reducing the state space, not by setting inverse zero to zero. All of that material is background here. We study one boundary convention on the whole affine plane, including every point at which the usual rational formula has a zero denominator.

Fix a finite field $\mathbb F_q$ of odd order. Define $$\label{eq:invzero}
 \operatorname{inv}_0(x)=
 \begin{cases}
 0,&x=0,\\
 x^{-1},&x\ne0,
 \end{cases}
 \qquad
 \mathsf L(x,y)=\bigl(y,(1+y)\operatorname{inv}_0(x)\bigr).$$ Let $r_q$ be the number of roots in $\mathbb F_q$ of $$\label{eq:fixed-polynomial}
 a^2-a-1=0.$$ For a point $P$, its tail $\tau(P)$ is the least $t\geq0$ such that $\mathsf L^t(P)$ is recurrent.

The five sets below will describe every point. Put $$\begin{aligned}
 \mathcal G&=\{(x,y):xy(1+x)(1+y)(1+x+y)\ne0\},\label{eq:generic}\\
 \mathcal A&=(\{0\}\times\mathbb F_q)\cup(\mathbb F_q\times\{0\}),\label{eq:axes}\\
 \mathcal E_1&=\{(a,-1):a\in\mathbb F_q\setminus\{0\}\},\label{eq:e1}\\
 \mathcal E_2&=\{(-1-a,a):a\in\mathbb F_q\setminus\{0,-1\}\},\label{eq:e2}\\
 \mathcal E_3&=\{(-1,-1-a):a\in\mathbb F_q\setminus\{0,-1\}\}.\label{eq:e3}\end{aligned}$$

[\[thm:main\]]{#thm:main label="thm:main"} For every odd prime power $q$, the following statements hold.

1.  The five sets in [\[eq:generic\]](#eq:generic){reference-type="eqref" reference="eq:generic"}--[\[eq:e3\]](#eq:e3){reference-type="eqref" reference="eq:e3"} are pairwise disjoint and their union is $\mathbb F_q^2$. Their respective sizes are $$\label{eq:strata-sizes}
     (q-2)(q-3),\qquad 2q-1,\qquad q-1,\qquad q-2,\qquad q-2.$$ The recurrent set is $\mathcal G\cup\mathcal A$, and $\tau$ equals $j$ on $\mathcal E_j$. Consequently $$\label{eq:temporal}
     \sum_{P\in\mathbb F_q^2}z^{\tau(P)}
     =(q^2-3q+5)+(q-1)z+(q-2)z^2+(q-2)z^3.$$ In particular, the maximum tail is exactly three.

2.  The cycle census is

       cycle length     number of cycles
      -------------- ----------------------
           $1$              $1+r_q$
           $2$                $2$
           $4$             $(q-3)/2$
           $5$        $((q-2)(q-3)-r_q)/5$

    There are no other cycles. Hence the dynamical zeta function is $$\label{eq:zeta}
     \zeta_{\mathsf L}(z)=
     (1-z)^{-(1+r_q)}(1-z^2)^{-2}
     (1-z^4)^{-(q-3)/2}
     (1-z^5)^{-((q-2)(q-3)-r_q)/5}.$$

3.  For every target $(u,v)\in\mathbb F_q^2$, $$\label{eq:fibre-law}
     |\mathsf L^{-1}(u,v)|=
     \begin{cases}
     q,&(u,v)=(-1,0),\\
     0,&u=-1\text{ and }v\ne0,\\
     1,&u\ne-1.
     \end{cases}$$ Thus $|\operatorname{im}\mathsf L|=q^2-q+1$, and the exceptional in-tree attached to the two-cycle $(-1,0)\leftrightarrow(0,-1)$ is exactly the one displayed in [\[cor:tree\]](#cor:tree){reference-type="ref" reference="cor:tree"} below.

The next three sections prove [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Enumeration is used only for the independent controls reported in [5](#sec:controls){reference-type="ref" reference="sec:controls"}.

# Disjoint strata and the sharp tail polynomial

We first prove coverage pointwise; the cardinality identity will be a consequence rather than a substitute.

[\[prop:partition\]]{#prop:partition label="prop:partition"} The sets $\mathcal G,\mathcal A,\mathcal E_1,\mathcal E_2,\mathcal E_3$ are pairwise disjoint and cover $\mathbb F_q^2$. Their sizes are given by [\[eq:strata-sizes\]](#eq:strata-sizes){reference-type="eqref" reference="eq:strata-sizes"}.

Every point of $\mathcal A$ has a zero coordinate. Every point in an exceptional set has two nonzero coordinates: the exclusions on the parameter in [\[eq:e1\]](#eq:e1){reference-type="eqref" reference="eq:e1"}--[\[eq:e3\]](#eq:e3){reference-type="eqref" reference="eq:e3"} guarantee this. Hence $\mathcal A$ is disjoint from the other four sets.

Now take $(x,y)\notin\mathcal A$. If $y=-1$, then $(x,y)\in\mathcal E_1$. Suppose $y\ne-1$. If $x=-1$, set $a=-1-y$. Since $y\notin\{0,-1\}$, one has $a\notin\{0,-1\}$ and $(x,y)=(-1,-1-a)\in\mathcal E_3$. Suppose also $x\ne-1$. If $1+x+y=0$, then $(x,y)=(-1-a,a)\in\mathcal E_2$ with $a=y\notin\{0,-1\}$. If none of these three equalities holds, all five factors in [\[eq:generic\]](#eq:generic){reference-type="eqref" reference="eq:generic"} are nonzero, so $(x,y)\in\mathcal G$. The tests are ordered by mutually exclusive equations. They therefore prove both coverage and unique membership.

The axis union has size $2q-1$, while the three exceptional parametrizations are injective and have sizes $q-1,q-2,q-2$. Subtracting these disjoint sets from the $q^2$ points of the plane gives $$|\mathcal G|=q^2-(2q-1)-(q-1)-2(q-2)=(q-2)(q-3).$$

On $\mathcal G$, the zero-totalized map agrees for five steps with the classical rational recurrence. We record the algebra because it also verifies that no zero denominator is crossed.

[\[lem:five\]]{#lem:five label="lem:five"} If $(x,y)\in\mathcal G$, then $$\begin{aligned}
 \mathsf L(x,y)&=\left(y,\frac{1+y}{x}\right),\nonumber\\
 \mathsf L^2(x,y)&=\left(\frac{1+y}{x},
                  \frac{1+x+y}{xy}\right),\nonumber\\
 \mathsf L^3(x,y)&=\left(\frac{1+x+y}{xy},
                  \frac{1+x}{y}\right),\label{eq:five-iterates}\\
 \mathsf L^4(x,y)&=\left(\frac{1+x}{y},x\right),\nonumber\\
 \mathsf L^5(x,y)&=(x,y).\nonumber\end{aligned}$$ In particular every point of $\mathcal G$ is recurrent.

The five possible first coordinates at successive divisions are $$x,\quad y,\quad \frac{1+y}{x},\quad
 \frac{1+x+y}{xy},\quad \frac{1+x}{y}.$$ They are all nonzero by [\[eq:generic\]](#eq:generic){reference-type="eqref" reference="eq:generic"}, so $\operatorname{inv}_0$ is ordinary inversion at every displayed step. Repeated substitution in [\[eq:invzero\]](#eq:invzero){reference-type="eqref" reference="eq:invzero"} gives [\[eq:five-iterates\]](#eq:five-iterates){reference-type="eqref" reference="eq:five-iterates"}; the only cancellations use $(1+x)(1+y)=1+x+y+xy$. The last line proves recurrence.

The complement of $\mathcal G$ has equally explicit arrows.

[\[lem:arrows\]]{#lem:arrows label="lem:arrows"} For $a\in\mathbb F_q$, $$\label{eq:axis-arrows}
 \mathsf L(0,a)=(a,0),\qquad
 \mathsf L(a,0)=(0,a^{-1})\quad(a\ne0),$$ and $(0,0)$ is fixed. For $a\in\mathbb F_q\setminus\{0,-1\}$, $$\label{eq:tail-chain}
 (-1,-1-a)\longmapsto(-1-a,a)
 \longmapsto(a,-1)\longmapsto(-1,0),$$ while $$\label{eq:leaf-and-cycle}
 (-1,-1)\longmapsto(-1,0)
 \longmapsto(0,-1)\longmapsto(-1,0).$$

Equations [\[eq:axis-arrows\]](#eq:axis-arrows){reference-type="eqref" reference="eq:axis-arrows"} follow directly from $\operatorname{inv}_0(0)=0$ and $\operatorname{inv}_0(a)=a^{-1}$ for $a\ne0$. For the exceptional arrows, substitute into [\[eq:invzero\]](#eq:invzero){reference-type="eqref" reference="eq:invzero"}: $$\begin{aligned}
 \mathsf L(-1,-1-a)&=(-1-a,a),\\
 \mathsf L(-1-a,a)&=\left(a,\frac{1+a}{-1-a}\right)=(a,-1),\\
 \mathsf L(a,-1)&=(-1,0).\end{aligned}$$ The parameter exclusions make each displayed denominator nonzero. The two remaining arrows in [\[eq:leaf-and-cycle\]](#eq:leaf-and-cycle){reference-type="eqref" reference="eq:leaf-and-cycle"} are immediate.

[\[thm:tails\]]{#thm:tails label="thm:tails"} The recurrent set is $\mathcal G\cup\mathcal A$. The sets $\mathcal E_1,\mathcal E_2,\mathcal E_3$ are exactly the tail layers of depths $1,2,3$, respectively. Hence [\[eq:temporal\]](#eq:temporal){reference-type="eqref" reference="eq:temporal"} holds and the maximum tail is three.

The generic points are recurrent by [\[lem:five\]](#lem:five){reference-type="ref" reference="lem:five"}. Equations [\[eq:axis-arrows\]](#eq:axis-arrows){reference-type="eqref" reference="eq:axis-arrows"} show that $(0,0)$ is fixed and every other axis point lies in a cycle generated by inversion in $\mathbb F_q^*$. Thus every point of $\mathcal A$ is recurrent.

By [\[lem:arrows\]](#lem:arrows){reference-type="ref" reference="lem:arrows"}, $\mathcal E_1$ maps into the recurrent two-cycle in one step, $\mathcal E_2$ maps into $\mathcal E_1$, and $\mathcal E_3$ maps into $\mathcal E_2$. The disjointness in [\[prop:partition\]](#prop:partition){reference-type="ref" reference="prop:partition"} makes these depths exact. No exceptional point is recurrent because its orbit enters the invariant axis set and never returns to its exceptional stratum. This proves the recurrent-set assertion and all pointwise depths.

The recurrent coefficient is $$|\mathcal G|+|\mathcal A|=(q-2)(q-3)+2q-1=q^2-3q+5.$$ Adding the three exceptional layer sizes gives [\[eq:temporal\]](#eq:temporal){reference-type="eqref" reference="eq:temporal"}. Since $q\geq3$, the set $\mathcal E_3$ has size $q-2>0$, so depth three is attained for every allowed field.

# The complete cycle census and zeta function

The generic locus contributes only periods one and five. The axes contribute the remaining periods.

[\[lem:fixed\]]{#lem:fixed label="lem:fixed"} The fixed points are $(0,0)$ and the $r_q$ points $(a,a)$ satisfying [\[eq:fixed-polynomial\]](#eq:fixed-polynomial){reference-type="eqref" reference="eq:fixed-polynomial"}. Every latter point belongs to $\mathcal G$.

If $\mathsf L(x,y)=(x,y)$, then $y=x$. At $x=0$ this gives $(0,0)$. For $x\ne0$, the second coordinate equation is $(1+x)/x=x$, equivalently $x^2-x-1=0$. Conversely every such root gives a fixed point.

A root $a$ is neither $0$ nor $-1$. It also satisfies $1+2a\ne0$: otherwise $a=-1/2$, and substitution into $a^2-a-1$ gives $-1/4\ne0$ because the characteristic is odd. Thus all five factors defining $\mathcal G$ are nonzero at $(a,a)$.

[\[lem:axis-cycles\]]{#lem:axis-cycles label="lem:axis-cycles"} The axes contain $(0,0)$, exactly two 2-cycles, and exactly $(q-3)/2$ 4-cycles. The 2-cycles are $$\label{eq:two-cycles}
 (0,1)\longleftrightarrow(1,0),\qquad
 (0,-1)\longleftrightarrow(-1,0).$$ For $a\in\mathbb F_q^*\setminus\{1,-1\}$, the inversion pair $\{a,a^{-1}\}$ indexes the 4-cycle $$\label{eq:four-cycle}
 (0,a)\longmapsto(a,0)\longmapsto(0,a^{-1})
 \longmapsto(a^{-1},0)\longmapsto(0,a).$$

The arrows are [\[eq:axis-arrows\]](#eq:axis-arrows){reference-type="eqref" reference="eq:axis-arrows"}. An element of $\mathbb F_q^*$ is fixed by inversion exactly when $a^2=1$. Since the characteristic is odd, these are the two distinct elements $1$ and $-1$, and they give [\[eq:two-cycles\]](#eq:two-cycles){reference-type="eqref" reference="eq:two-cycles"}. Inversion acts without fixed points on the remaining $q-3$ elements, giving $(q-3)/2$ unordered pairs and the cycles [\[eq:four-cycle\]](#eq:four-cycle){reference-type="eqref" reference="eq:four-cycle"}. Distinct inversion pairs give disjoint cycles.

[\[thm:cycles\]]{#thm:cycles label="thm:cycles"} The cycle counts in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}[(ii)]{.upright} are complete.

The exceptional layers contain no recurrent point by [\[thm:tails\]](#thm:tails){reference-type="ref" reference="thm:tails"}. The axis contribution is completely classified by [\[lem:axis-cycles\]](#lem:axis-cycles){reference-type="ref" reference="lem:axis-cycles"}, including the fixed point $(0,0)$. On $\mathcal G$, [\[lem:five\]](#lem:five){reference-type="ref" reference="lem:five"} shows that every least period divides the prime $5$. By [\[lem:fixed\]](#lem:fixed){reference-type="ref" reference="lem:fixed"}, exactly $r_q$ generic points have period one; all other $(q-2)(q-3)-r_q$ generic points therefore have exact period five. Dividing these points into their disjoint five-element $\mathsf L$-orbits simultaneously proves the divisibility of $(q-2)(q-3)-r_q$ by five and gives their cycle count. These cases exhaust the disjoint partition from [\[prop:partition\]](#prop:partition){reference-type="ref" reference="prop:partition"}.

[\[rem:small-fields\]]{#rem:small-fields label="rem:small-fields"} For $q=3$, the generic locus is empty, so the 4- and 5-cycle families are empty, while $|\mathcal E_3|=1$ still attains tail three. In characteristic five, the discriminant of $a^2-a-1$ is zero, so the polynomial has one double root and $r_q=1$ over every finite extension; at $q=5$ this yields one generic 5-cycle. These degeneracies are already included in the census.

For a finite self-map, define $$\label{eq:zeta-definition}
 \zeta_{\mathsf L}(z)=
 \exp\left(\sum_{n\geq1}\frac{|\operatorname{Fix}(\mathsf L^n)|}{n}z^n\right).$$ Equivalently, a cycle of length $d$ contributes $(1-z^d)^{-1}$. Substituting the four counts from [\[thm:cycles\]](#thm:cycles){reference-type="ref" reference="thm:cycles"} gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. This last Euler product conversion is standard finite-map bookkeeping and receives zero contribution credit.

# Every-target fibres and the complete singular in-tree

The inverse problem is simpler than the forward stratification because a target's first coordinate fixes one source coordinate.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} Equation [\[eq:fibre-law\]](#eq:fibre-law){reference-type="eqref" reference="eq:fibre-law"} holds. Consequently $|\operatorname{im}\mathsf L|=q^2-q+1$, and $(-1,0)$ is the unique target of maximum fibre.

If $\mathsf L(x,y)=(u,v)$, the first coordinate forces $y=u$, and the remaining equation is $$\label{eq:inverse-equation}
 (1+u)\operatorname{inv}_0(x)=v.$$ If $u=-1$, its left side is zero for every $x\in\mathbb F_q$. This gives all $q$ sources $(x,-1)$ when $v=0$ and no source when $v\ne0$.

Suppose $u\ne-1$. If $v=0$, then [\[eq:inverse-equation\]](#eq:inverse-equation){reference-type="eqref" reference="eq:inverse-equation"} forces $\operatorname{inv}_0(x)=0$, hence $x=0$, giving the unique source $(0,u)$. If $v\ne0$, the unique solution is the nonzero element $x=(1+u)/v$. These cases prove [\[eq:fibre-law\]](#eq:fibre-law){reference-type="eqref" reference="eq:fibre-law"}.

There are $q(q-1)$ targets with $u\ne-1$, all in the image, and the only image target with $u=-1$ is $(-1,0)$. Thus the image size is $q(q-1)+1=q^2-q+1$. Since $q\geq3$, the fibre of size $q$ is uniquely maximal.

[\[cor:tree\]]{#cor:tree label="cor:tree"} The connected functional-graph component containing $(-1,0)\leftrightarrow(0,-1)$ consists exactly of that two-cycle, the leaf $$\label{eq:single-leaf}
 (-1,-1)\longmapsto(-1,0),$$ and, for each $a\in\mathbb F_q\setminus\{0,-1\}$, the length-three chain $$\label{eq:all-chains}
 (-1,-1-a)\longmapsto(-1-a,a)\longmapsto(a,-1)
 \longmapsto(-1,0).$$ There are no further vertices or incoming branches in this component.

The displayed arrows are [\[lem:arrows\]](#lem:arrows){reference-type="ref" reference="lem:arrows"}. It remains to prove completeness. The fibre of $(-1,0)$ is exactly $\{(x,-1):x\in\mathbb F_q\}$. Among these sources, $(0,-1)$ is the cycle predecessor, $(-1,-1)$ is [\[eq:single-leaf\]](#eq:single-leaf){reference-type="eqref" reference="eq:single-leaf"}, and the other $q-2$ points are the endpoints $(a,-1)$ in [\[eq:all-chains\]](#eq:all-chains){reference-type="eqref" reference="eq:all-chains"}.

For $a\notin\{0,-1\}$, the target $(a,-1)$ has the unique predecessor $(-1-a,a)$, and that target has the unique predecessor $(-1,-1-a)$, by the unique-source case of [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"}. Finally, $(-1,-1-a)$ has first coordinate $-1$ and nonzero second coordinate, so its fibre is empty. The point $(-1,-1)$ has empty fibre for the same reason. The target $(0,-1)$ has the unique predecessor $(-1,0)$. Thus no additional branch can enter any displayed vertex.

# Exact controls, limitations, and declarations {#sec:controls}

The paper-local verifier constructs every literal state and target over all odd prime fields through $101$ and six nonprime fields of orders $9,25,27,49,121,125$. It checks the field arithmetic, unique stratum membership, the five generic iterates, every pointwise tail and period, the cycle census, the temporal polynomial, every target fibre, and the complete exceptional predecessor sets. It uses exact standard-library arithmetic without sampling, floating point, a computer algebra system, runtime network access, or a third-party package.

::: {#tab:controls}
  control                   exact count
  ---------------------- --------------
  finite-field boxes                 31
  state/target cells       110,095 each
  nonprime field boxes                6
  Boolean assertions          2,144,131

  : Dependency-free falsification controls. These counts prove neither the all-parameter statements nor any ownership claim.
:::

#### Limitations.

The cycle census uses odd characteristic: in characteristic two the two elements $1$ and $-1$ coincide, so the displayed pair of 2-cycles and the 4-cycle count do not persist. The note treats only the literal affine convention [\[eq:invzero\]](#eq:invzero){reference-type="eqref" reference="eq:invzero"}; it does not classify projective compactifications, other values assigned to inverse zero, general Lyness parameters, or higher-order recurrences. The exact controls cover finitely many fields and serve only as falsification. The source search was also bounded. A direct owner of the residual all-affine conjunction would reopen the result.

#### Data and code availability.

No external dataset is used. The deterministic verifier and its frozen stdout transcript accompany the internal paper package. They are not an external release authorization.

#### Ethics statement.

The work uses no human participants, animal subjects, personal data, or stochastic intervention, and raises no application-specific ethical issue.

#### Author contributions.

The anonymous author or authors developed the finite system, proved the results, implemented the exact controls, audited the sources, and prepared the manuscript.

#### Conflict of interest.

The anonymous author or authors declare no conflict of interest.

#### Funding.

No external funding is declared for this anonymous internal manuscript.

Classical Lyness five-periodicity, QRT and cluster interpretations, finite-field birational methods, and generic zeta algebra remain zero-credit inputs. The residual is limited to the exact zero-totalized all-affine graph proved above. A bounded source non-hit is not novelty, priority, authorship, or ownership evidence. No posting, specialist contact, submission, or release is authorized; status remains `HOLD_EXTERNAL`.
