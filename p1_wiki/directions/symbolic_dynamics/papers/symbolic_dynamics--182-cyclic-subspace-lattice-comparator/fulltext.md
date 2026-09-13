---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--182-cyclic-subspace-lattice-comparator"
canonical_tex: "symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/main.tex"
canonical_pdf: "symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/main.pdf"
source_sha256: "9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cyclic Subspace-Lattice Comparator: A Complete Depth-Two and Fibre Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For three subspaces, retain the third, replace the first two by their intersection and sum, and cyclically move the retained subspace to the front. We determine the resulting functional graph. On every lattice the analogous map satisfies $T^4=T^2$; its recurrent states are exactly the triples whose middle coordinate lies below both outer coordinates, where $T$ swaps the outer coordinates. On $\mathcal L_d(q)^3$, the cube of the subspace lattice of $\mathbb F_q^d$, we give closed formulas for the image, fixed points, two-cycles, and all three depth populations for every prime power $q$ and every $d\ge0$. We also determine every predecessor fibre: a target $(C,M,J)$ is unreachable unless $M\subseteq J$, and otherwise its fibre is the set of ordered complementary pairs in $J/M$. This yields the complete fibre histogram and all maximizers. At $(q,d)=(2,4)$, for example, the $300{,}763$ states split into depths $9{,}265$, $157{,}272$, and $134{,}226$, with $513$ fixed points and $4{,}376$ strict two-cycles. A paper-local exact audit checks $328{,}700$ transitions. External status remains [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Cyclic Subspace-Lattice Comparator:\
  A Complete Depth-Two and Fibre Atlas
```

## Markdown 正文

# The rule and complete theorem package

Let $L$ be a lattice. The cyclic comparator is the lattice polynomial $$\label{eq:map}
        T_L(a,b,c)=(c,a\wedge b,a\vee b),\qquad (a,b,c)\in L^3.$$ The third register rotates to the front while the first two emit their meet and join. Lattice polynomials and absorption are classical [@Birkhoff1967]. Recent work studies different lattice operators, such as the meet-of-covers pop map on Tamari lattices [@Hong2022]; meet--join sorting relations also appear in Hibi-type algebras [@GasanovaNicklasson2024]. These sources provide background, not a claim about the functional graph of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}.

We first state the finite-field specialization. Fix a prime power $q$ and let $\mathcal L_d(q)$ be the lattice of subspaces of $V=\mathbb F_q^d$, with meet $A\mathbin{\cap}B$ and join $A\mathbin{+}B$. Gaussian coefficients and finite subspace enumeration are standard [@GoldmanRota1970; @ChajdaLanger2019]. Write $$\begin{aligned}
 g_n&=\sum_{r=0}^n\genfrac{[}{]}{0pt}{}{n}{r}_{q},\label{eq:galois}\\
 \alpha_d&=\sum_{b=0}^d\genfrac{[}{]}{0pt}{}{d}{b}_{q} g_{d-b},&
 \rho_d&=\sum_{b=0}^d\genfrac{[}{]}{0pt}{}{d}{b}_{q} g_{d-b}^{2},\label{eq:alpha-rho}\\
 Q_n&=\sum_{a=0}^n\sum_{s=0}^{n-a}
       \genfrac{[}{]}{0pt}{}{n}{a}_{q}\genfrac{[}{]}{0pt}{}{n-a}{s}_{q} q^{as},&
 \eta_d&=\sum_{m=0}^d\genfrac{[}{]}{0pt}{}{d}{m}_{q} Q_{d-m}g_{d-m},\label{eq:q-eta}\\
 \kappa_k&=\sum_{a=0}^k\genfrac{[}{]}{0pt}{}{k}{a}_{q} q^{a(k-a)}.\label{eq:kappa}\end{aligned}$$ Thus $g_n$ is the number of subspaces of an $n$-space. The other quantities will count intervals, recurrent triples, disjoint pairs, the depth-at-most-one set, and ordered complementary pairs, respectively.

For a finite self-map, the depth of a state is its distance to the recurrent set. A strict two-cycle means an orbit of two distinct states.

[\[thm:main\]]{#thm:main label="thm:main"} For every prime power $q$ and every $d\ge0$, let $T=T_{\mathcal L_d(q)}$. Then the following statements hold.

(i) On every lattice, not merely $\mathcal L_d(q)$, $$\label{eq:square-collapse}
     T^2(a,b,c)=(a\vee b,c\wedge a\wedge b,c\vee(a\wedge b)),
     \qquad T^4=T^2.$$

(ii) The image consists exactly of triples $(C,M,J)$ with $M\subseteq J$. The recurrent set consists exactly of triples $(A,B,C)$ with $B\subseteq A\mathbin{\cap}C$; there $T(A,B,C)=(C,B,A)$. Hence a recurrent state is fixed exactly when $A=C$, and every other recurrent orbit is a strict two-cycle.

(iii) The carrier has $g_d^3$ states. The image, fixed-point set, recurrent set, and strict two-cycle set have respective sizes $$\label{eq:basic-counts}
       g_d\alpha_d,\qquad \alpha_d,\qquad \rho_d,
       \qquad \frac{\rho_d-\alpha_d}{2}.$$

(iv) A state outside the recurrent set has depth one exactly when $A\mathbin{\cap}B\subseteq C$, and depth two otherwise. The depth populations are $$\label{eq:depth-counts}
                N_0=\rho_d,\qquad N_1=\eta_d-\rho_d,
                \qquad N_2=g_d^3-\eta_d.$$ For $d\ge1$, the height is exactly two.

(v) Every target has the target-local fibre formula $$\label{eq:fibre}
     |T^{-1}(C,M,J)|=
     \begin{cases}
      \kappa_{\dim(J/M)},&M\subseteq J,\\
      0,&M\not\subseteq J.
     \end{cases}$$

(vi) For $0\le k\le d$, the number of targets with fibre $\kappa_k$ is $$\label{eq:fibre-histogram}
      g_d\sum_{m=0}^{d-k}\genfrac{[}{]}{0pt}{}{d}{m}_{q}\genfrac{[}{]}{0pt}{}{d-m}{k}_{q};$$ the remaining $g_d^3-g_d\alpha_d$ targets have empty fibre. Moreover $\kappa_0<\kappa_1<\cdots<\kappa_d$. The maximum fibre $\kappa_d$ occurs at exactly the $g_d$ targets $(C,0,V)$, and the minimum positive fibre one occurs at exactly the $g_d^2$ targets $(C,M,M)$.

The package separates two mechanisms:

  --------------------------------------------------------------------------------
  input                     output
  ------------------------- ------------------------------------------------------
  lattice absorption        $T^4=T^2$, recurrence, periods, and depth predicates

  finite-field modularity   all populations and every target fibre via $J/M$
  --------------------------------------------------------------------------------

# Universal lattice dynamics

The temporal collapse does not depend on finiteness, distributivity, or modularity.

[\[lem:universal\]]{#lem:universal label="lem:universal"} For every lattice $L$, [\[eq:square-collapse\]](#eq:square-collapse){reference-type="eqref" reference="eq:square-collapse"} holds. The image of $T_L$ is the set of $(c,m,j)$ with $m\le j$. A point is recurrent exactly when $b\le a,c$; the restriction of $T_L$ to the recurrent set swaps the outer coordinates.

Put $m=a\wedge b$ and $j=a\vee b$. Direct substitution gives $$\label{eq:square}
             T^2(a,b,c)=(j,c\wedge m,c\vee m).$$ If $u=c\wedge m$ and $v=c\vee m$, then $u\le m\le j$ and $u\le v$. Absorption therefore gives $$T^3(a,b,c)=(v,u,j),\qquad
             T^4(a,b,c)=(j,u,v)=T^2(a,b,c).$$ Every image has its second coordinate below its third. Conversely, $T(m,j,c)=(c,m,j)$ whenever $m\le j$, proving the image statement.

Identity $T^4=T^2$ puts $T^2x$ on a cycle of length at most two. Thus a point is recurrent precisely when $T^2(a,b,c)=(a,b,c)$. The first equation says $b\le a$. Under that condition, the remaining equations reduce to $b\le c$. Finally $a\wedge b=b$ and $a\vee b=a$ on this set, so $T(a,b,c)=(c,b,a)$.

Lemma [\[lem:universal\]](#lem:universal){reference-type="ref" reference="lem:universal"} proves (i)--(ii). The first image of $(A,B,C)$ is $(C,A\mathbin{\cap}B,A\mathbin{+}B)$. By the recurrent criterion, it is recurrent if and only if $A\mathbin{\cap}B\subseteq C$, since $A\mathbin{\cap}B\subseteq A\mathbin{+}B$ is automatic. A nonrecurrent source satisfying this inclusion has depth one; if the inclusion fails, its first image is not recurrent and its second image is recurrent by $T^4=T^2$, giving depth two. When $d\ge1$, take $A=B$ to be a line and $C=0$ to realize depth two.

# Subspace counts and the functional graph

The universal predicates reduce every population to a finite-geometry count. We include the reductions to make clear which uses of Gaussian coefficients are needed.

[\[lem:disjoint\]]{#lem:disjoint label="lem:disjoint"} The number of ordered pairs $(X,Y)$ of subspaces of an $n$-space satisfying $X\mathbin{\cap}Y=0$ is $Q_n$ from [\[eq:q-eta\]](#eq:q-eta){reference-type="eqref" reference="eq:q-eta"}.

Fix $a=\dim X$ and $s=\dim Y$. There are $\genfrac{[}{]}{0pt}{}{n}{a}_{q}$ choices for $X$. Projection to $V/X$ embeds $Y$ as an $s$-subspace, with $\genfrac{[}{]}{0pt}{}{n-a}{s}_{q}$ possible images. Above a fixed image, the subspaces $Y$ are the graphs of the $q^{as}$ linear maps to $X$. Sum over $a$ and $s$.

Choose a middle subspace $B$ of dimension $b$. Its superspaces correspond to arbitrary subspaces of $V/B$, so there are $g_{d-b}$ of them. A fixed state is $(A,B,A)$ with $B\subseteq A$, giving $\alpha_d$. Recurrent states allow two independent superspaces $A,C$, giving $\rho_d$. Lemma [\[lem:universal\]](#lem:universal){reference-type="ref" reference="lem:universal"} pairs all recurrent nonfixed states, proving the two-cycle count. The image has an arbitrary first coordinate and an interval $M\subseteq J$, so its size is $g_d\alpha_d$.

It remains to count triples with $A\mathbin{\cap}B\subseteq C$. Fix $M=A\mathbin{\cap}B$ of dimension $m$. In $V/M$, the images of $A$ and $B$ are an ordered disjoint pair, counted by $Q_{d-m}$, while $C/M$ is an arbitrary subspace, counted by $g_{d-m}$. Choosing $M$ and summing gives $\eta_d$. The depth predicate already proved now yields [\[eq:depth-counts\]](#eq:depth-counts){reference-type="eqref" reference="eq:depth-counts"}.

# Every-target fibres and their extrema

The fibre theorem is local: its input is the interval carried by the target, not a global rank statistic.

A predecessor of $(C,M,J)$ has forced third coordinate $C$ and first two coordinates satisfying $$\label{eq:meet-join-fibre}
                 A\mathbin{\cap}B=M,\qquad A\mathbin{+}B=J.$$ These equations have no solution unless $M\subseteq J$. If the inclusion holds and $k=\dim(J/M)$, quotienting [\[eq:meet-join-fibre\]](#eq:meet-join-fibre){reference-type="eqref" reference="eq:meet-join-fibre"} by $M$ identifies its solutions with ordered decompositions $$J/M=(A/M)\oplus(B/M).$$ After choosing $A/M$ of dimension $a$, it has $q^{a(k-a)}$ complements [@ChajdaLanger2019]. Summing over $a$ proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

An interval $M\subseteq J$ with $\dim(J/M)=k$ is obtained by choosing $m=\dim M$, then $M$, then a $k$-subspace of $V/M$. Multiplication by the $g_d$ choices of $C$ gives [\[eq:fibre-histogram\]](#eq:fibre-histogram){reference-type="eqref" reference="eq:fibre-histogram"}; summing over $k$ recovers $g_d\alpha_d$ nonempty fibres.

To compare the fibre values, write a $(k+1)$-space as $H\oplus\ell$ with $\dim H=k$. The injection $$(X,Y)\longmapsto (X,Y\oplus\ell)$$ sends ordered decompositions of $H$ to ordered decompositions of $H\oplus\ell$ and misses $(\ell,H)$. Hence $\kappa_k<\kappa_{k+1}$. The maximum therefore requires $\dim(J/M)=d$, equivalently $(M,J)=(0,V)$, and $C$ remains arbitrary. The minimum positive value is $\kappa_0=1$, attained exactly when $M=J$.

For $d=0$, the carrier is the unique fixed triple, and all formulas give one state, one image point, and a unit fibre. The strict height-two statement is therefore correctly restricted to $d\ge1$.

# Exact audit, subtraction, and limitations

The paper-local verifier enumerates canonical reduced row-echelon bases, builds every transition, decomposes the functional graph, and checks every target fibre. It covers $15$ prime-field boxes: $$(q,d)\in\{2\}\!\times\!\{0,\ldots,4\}
 \cup\{3\}\!\times\!\{0,\ldots,3\}
 \cup\{5,7\}\!\times\!\{0,1,2\}.$$ The run checks $328{,}700$ transitions with $1{,}667{,}850$ explicit assertions and a frozen transition digest. For orientation, selected boxes are shown below.

    $(q,d)$        states        image   fixed   strict $2$-cycles     depth $2$
  --------- ------------- ------------ ------- ------------------- -------------
    $(2,4)$   $300{,}763$   $34{,}371$   $513$           $4{,}376$   $134{,}226$
    $(3,3)$    $21{,}952$    $3{,}724$   $133$               $586$     $7{,}619$
    $(5,2)$         $512$        $168$    $21$                $34$         $115$
    $(7,2)$     $1{,}000$        $270$    $27$                $53$         $201$

The exact audit is a falsifier, not the proof above and not ownership evidence.

We assign no contribution credit to lattice absorption, Gaussian coefficients, standard counts of subspace complements, Hibi meet--join sorting, pop-operator dynamics, or generic finite-map bookkeeping. Internally, the rule was also screened against monotone join/gcd folds, subspace-product closures, polarity maps, and fixed-linear/Jordan dynamics. Those engines do not transfer the conjunction of a universal cyclic-register identity and the target-local ordered-complement atlas.

Two limitations remain. First, the explicit census uses the homogeneous geometry of a finite subspace lattice; an arbitrary finite lattice retains the temporal theorem but not these Gaussian formulas. Second, a bounded primary-source search found no exact owner for the full conjunction, but a non-hit is not a novelty or priority result. The owner gate is [owner\_amber]{.smallcaps}, and external circulation remains [hold\_external]{.smallcaps} pending deeper database search and independent proof review.

# Data availability {#data-availability .unnumbered}

No external data are used. The standard-library verifier and canonical stdout are included with the paper source.

# Ethics statement {#ethics-statement .unnumbered}

This theoretical study uses no human participants, animals, personal data, or deployed decision system.

# CRediT author statement {#credit-author-statement .unnumbered}

Anonymous author(s): Conceptualization, Formal analysis, Methodology, Software, Validation, Visualization, and Writing---original draft.

# Competing interests {#competing-interests .unnumbered}

The author(s) declare no competing interests.

# Funding {#funding .unnumbered}

No external funding is declared for this work.

# AI-use statement {#ai-use-statement .unnumbered}

Generative-AI tools assisted with exploratory algebra, code drafting, and language editing. The author(s) remain responsible for every definition, proof, citation, computation, and disclosure. No AI output is treated as owner or novelty evidence.
