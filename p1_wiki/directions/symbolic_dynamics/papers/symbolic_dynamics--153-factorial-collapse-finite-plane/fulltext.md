---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--153-factorial-collapse-finite-plane"
canonical_tex: "symbolic_dynamics/papers/153-factorial-collapse-finite-plane/main.tex"
canonical_pdf: "symbolic_dynamics/papers/153-factorial-collapse-finite-plane/main.pdf"
source_sha256: "ef98c216b2856ae10da9819ed53cb6d24bb00046adf3008c603f556e7bce134e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Functional graphs and all-time fibres of a factorial-collapse plane map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/153-factorial-collapse-finite-plane>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/153-factorial-collapse-finite-plane/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/153-factorial-collapse-finite-plane/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/153-factorial-collapse-finite-plane/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/153-factorial-collapse-finite-plane/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For an odd prime $p$, consider $$T\colon\mathbb F_p^2\longrightarrow\mathbb F_p^2,\qquad T(x,y)=(x+1,xy).$$ After exchanging coordinates this is a known specialization of a triangular polynomial family, so the construction and the factorial iterate are treated as credited inputs. We determine the remaining finite-map package pointwise: the axis is one $p$-cycle, and the complement is the disjoint union of $p-1$ arms of depth $p$, all entering at $(1,0)$. More importantly, for every time and every target we give its complete inverse fibre. This yields the image-size profile, a sharp coordinate-identifiability criterion, the temporal polynomial, all fixed-iterate counts, and the zeta function. All parameter statements are proved symbolically and checked by a deterministic exhaustive replay.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Functional graphs and all-time fibres\
  of a factorial-collapse plane map
```

## Markdown 正文

# Scope and main theorem

Functional graphs encode a self-map of a finite set by drawing one directed edge from each state to its image; see, for example, @KonyaginEtAl2016. Triangular polynomial systems over finite fields have also been studied through degree growth, periods, permutations, and conjugacy [@OstafeShparlinski2010; @Ostafe2012; @Maubach2011]. The present map sits inside that literature in a literal way. Under $(Y,X)=(y,x)$, it becomes $$(Y,X)\longmapsto(YX,X+1),$$ the one-dependent-coordinate specialization $g_0(X)=X$, $h_0=0$, $a=b=1$ of the family in @OstafeShparlinski2010. Accordingly, the following items are inputs with no contribution credit here: the construction as a triangular family member, its generic degree-growth framework, and the elementary rising-factorial iteration. The object studied below is instead the conjunction of the complete nonpermutation graph and the all-time target-by-target inverse atlas.

For $t\geq0$, set $$P_t(X)=\prod_{j=0}^{t-1}(X+j),\qquad
 C_t(u)=P_t(u-t)=\prod_{r=1}^{t}(u-r),
 \qquad r_t=\min\{t,p\},$$ with empty products equal to $1$.

[\[thm:main\]]{#thm:main label="thm:main"} Let $p$ be an odd prime and let $T(x,y)=(x+1,xy)$ on $\mathbb F_p^2$. Then the following statements hold.

1.  For all $t\geq0$, $$T^t(x,y)=\bigl(x+t,yP_t(x)\bigr).$$ In particular, $T^p(x,y)=(x,0)$, and $T^t(x,y)=(x+t,0)$ for $t\geq p$.

2.  The axis $\{(x,0):x\in\mathbb F_p\}$ is one cycle of length $p$. For each $a\in\mathbb F_p^\times$, the vertices $$v_{a,s}=\left(1-s,\frac{a}{(-1)^{s-1}(s-1)!}\right),
     \qquad 1\leq s\leq p,$$ form a directed arm with $T(v_{a,1})=(1,0)$ and $T(v_{a,s})=v_{a,s-1}$ for $s\geq2$. These $p-1$ arms are disjoint and exhaust the complement of the axis; their leaves are $v_{a,p}=(1,-a)$.

3.  If $\operatorname{tail}(w)$ is the first time at which $w$ reaches the recurrent set, then $$\Theta_p(z):=\sum_{w\in\mathbb F_p^2}z^{\operatorname{tail}(w)}
     =p+(p-1)(z+z^2+\cdots+z^p).$$

4.  For every $t\geq0$ and target $(u,v)$, $$(T^t)^{-1}(u,v)=
     \begin{cases}
     \{(u-t,v/C_t(u))\},&C_t(u)\neq0,\\
     \{(u-t,y):y\in\mathbb F_p\},&C_t(u)=0,\ v=0,\\
     \varnothing,&C_t(u)=0,\ v\neq0.
     \end{cases}                                      \tag{1}\label{eq:fibre}$$ Consequently, $$|\operatorname{im}T^t|=p(p-r_t)+r_t,                           \tag{2}\label{eq:image}$$ and the numbers of targets having fibres of sizes $1,p,0$ are, respectively, $$p(p-r_t),\qquad r_t,\qquad r_t(p-1).              \tag{3}\label{eq:dist}$$ The initial abscissa is always recoverable from a feasible time-$t$ observation; the initial ordinate is recoverable exactly when $C_t(u)\neq0$.

5.  The only periodic orbit is the axis cycle. For $n\geq1$, $$\#\operatorname{Fix}(T^n)=p\,\mathbf 1_{p\mid n},\qquad
     \zeta_T(z)=\frac{1}{1-z^p}.$$

#### Proof dependency graph.

The logical structure is intentionally visible: $$\begin{array}{c}
\text{literal update}\\[-1mm]
\downarrow\\
\text{factorial iterate}
\end{array}
\quad\Longrightarrow\quad
\begin{array}{c}
P_p(X)=X^p-X\\
\downarrow\\
\text{time-\(p\) collapse}\\
\swarrow\qquad\searrow\\[-1mm]
\text{first-zero schedule}\qquad\text{axis translation}\\
\downarrow\hspace{29mm}\downarrow\\[-1mm]
\text{arms and }\Theta_p\qquad \operatorname{Fix}(T^n),\zeta_T
\end{array}$$ $$\begin{gathered}
\text{factorial iterate}\Longrightarrow v=yC_t(u)
\Longrightarrow\text{point fibres},\\
\text{point fibres}\Longrightarrow
\{\text{images, distribution, identifiability}\}.
\end{gathered}
\tag{4}\label{eq:dependency}$$ Thus the graph theorem and the inverse theorem share only the closed iterate; neither is inferred from the other.

# Factorial collapse and the labelled graph

[\[lem:iterate\]]{#lem:iterate label="lem:iterate"} For every $t\geq0$, $$T^t(x,y)=\bigl(x+t,yP_t(x)\bigr).$$ Moreover $P_p(X)=X^p-X$ in $\mathbb F_p[X]$.

The displayed iterate is true at $t=0$. Applying $T$ to the formula at time $t$ multiplies the ordinate by $x+t$, producing $P_{t+1}(x)$. The roots of the monic polynomial $P_p$ are $-j$, $0\leq j<p$, namely all of $\mathbb F_p$; hence $P_p(X)=X^p-X$.

The last identity is a polynomial identity, whereas its use in the dynamics is pointwise: $x^p=x$ for $x\in\mathbb F_p$. Therefore $P_p(x)=0$, $T^p(x,y)=(x,0)$, and the axis is thereafter invariant. On that axis, $T$ is translation $x\mapsto x+1$, hence a single $p$-cycle.

Suppose now that $y\neq0$. Before a zero multiplier appears, all factors are units, so the ordinate remains nonzero. The first vanishing transition has $x+j=0$, and, counting that transition, its depth is the representative $$d(x)\equiv1-x\pmod p,\qquad 1\leq d(x)\leq p.       \tag{5}$$ At time $d(x)$, every such state enters $(1,0)$. For each $s\in\{1,\dots,p\}$, the forced abscissa is $x=1-s$, with $p-1$ choices of nonzero ordinate. This already gives the temporal polynomial in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

To identify the arms rather than merely count depths, evolve a depth-$s$ state through the first $s-1$ nonsingular steps. Its ordinate becomes $$y\prod_{j=0}^{s-2}(1-s+j)
=y(-1)^{s-1}(s-1)!.$$ Calling this value $a$ gives $v_{a,s}$. Substitution verifies every arrow. Different $a$'s give different vertices at depth one, and the total arm population is $p(p-1)$, so no off-axis vertex remains. Finally Wilson's theorem gives $(-1)^{p-1}(p-1)!=-1$, hence $v_{a,p}=(1,-a)$. This sign also shows why labelling an arm by its leaf ordinate would reverse the chosen label.

# Every-target fibres and inverse information

Fix $t\geq0$ and a target $(u,v)$. The first coordinate in [\[lem:iterate\]](#lem:iterate){reference-type="ref" reference="lem:iterate"} forces $$x=u-t.$$ The second coordinate then reduces to the one-variable equation $$v=yP_t(u-t)=yC_t(u).                                 \tag{6}\label{eq:target}$$ If the coefficient is nonzero, it is invertible and gives one source ordinate. If it is zero, every ordinate solves [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"} when $v=0$, and none does when $v\neq0$. This proves the pointwise atlas [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} and the identifiability statement. In particular, the loss of the second coordinate is target dependent before saturation; an image-cardinality statement alone does not locate it.

For $0\leq t\leq p$, the roots of $C_t(u)$ are the $t$ distinct columns $u=1,\ldots,t$. Every uncollapsed column supplies $p$ singleton targets, while every collapsed column supplies one target with fibre $p$ and $p-1$ impossible targets. For $t\geq p$, the product contains a complete residue system, so every column is collapsed. This proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}--[\[eq:dist\]](#eq:dist){reference-type="eqref" reference="eq:dist"}. The two independent conservation laws $$\underbrace{p(p-r_t)+r_t+r_t(p-1)}_{\text{target count}}=p^2,
\qquad
\underbrace{p(p-r_t)+p\,r_t}_{\text{source mass}}=p^2                 \tag{7}$$ close both the codomain partition and the source accounting.

The pointwise formula gives a sharper timeline than the global rank sequence. For $u\in\mathbb F_p$, let $\rho(u)\in\{1,\ldots,p\}$ be the representative of $u\pmod p$, with $\rho(0)=p$. Then $$C_t(u)\neq0\quad\Longleftrightarrow\quad t<\rho(u),
\qquad
C_t(u)=0\quad\Longleftrightarrow\quad t\geq\rho(u).                  \tag{8}$$ Indeed, the first factor of $C_t(u)$ that vanishes has index $r=\rho(u)$, and every later product retains that factor. Thus target column $u$ loses all information about the initial ordinate at the exact time $\rho(u)$, permanently. The columns are lost one at a time in the order $1,2,\ldots,p-1,0$, while the initial abscissa remains recoverable throughout. In particular, the transformation ranks

$$p^2,\ p^2-p+1,\ p^2-2p+2,\ldots,2p-1,\ p$$ decrease by exactly $p-1$ at each of the first $p$ steps and then remain constant.

For example, at $p=5$ the whole inverse schedule is summarized by [1](#tab:p5){reference-type="ref" reference="tab:p5"}. Here $N_s$ counts targets with fibre size $s$.

::: {#tab:p5}
     $t$      $|\operatorname{im}T^t|$  collapsed target columns     $N_1$   $N_5$   $N_0$
  ---------- -------------------------- -------------------------- ------- ------- -------
      0                  25             none                            25       0       0
      1                  21             1                               20       1       4
      2                  17             1,2                             15       2       8
      3                  13             1,2,3                           10       3      12
      4                  9              1,2,3,4                          5       4      16
   $t\geq5$              5              all                              0       5      20

  : The progressive target collapse for $p=5$.
:::

The unlabelled arm graph alone records the multiset of collapse depths, but not which observed target column loses the ordinate at which time. Formula [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"} supplies that labelled inverse information. This is why the graph and fibre clauses are retained as two theorem axes rather than one being advertised as a restatement of the other.

[\[cor:partition\]]{#cor:partition label="cor:partition"} At time $t$, two sources are observationally equivalent precisely when $$T^t(x,y)=T^t(x',y')
\quad\Longleftrightarrow\quad
x=x'\ \text{ and }\ \bigl(y=y'\text{ or }P_t(x)=0\bigr).             \tag{9}$$ For $0\leq t\leq p$, the non-singleton equivalence classes are the $t$ vertical source columns $$\{(x,y):y\in\mathbb F_p\},\qquad
x\in\{-j:0\leq j<t\}.$$ Thus this family of columns is empty at $t=0$. They form a nested sequence that gains one $p$-element block per step. For $t\geq p$, all $p$ vertical columns are blocks.

Equality of the target abscissae forces $x+t=x'+t$, hence $x=x'$. The ordinate equation is then $(y-y')P_t(x)=0$. A nonzero coefficient forces $y=y'$, whereas a zero coefficient identifies the entire vertical column. For $0\leq t<p$, the distinct roots of $P_t$ are exactly $\{-j:0\leq j<t\}$, an empty set at $t=0$; at and after time $p$, every $x\in\mathbb F_p$ is a root.

Thus [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} can also be read as the number of blocks in the time-$t$ observation partition. The target atlas [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} adds the information not contained in that quotient alone: it locates the feasible representative of every block and identifies every impossible observation.

# Periodic data, boundaries, and ownership firewall

If $p\nmid n$, the first coordinate of $T^n(x,y)$ is $x+n$, so there are no fixed points. If $p\mid n$, then $n\geq p$, and collapse gives $T^n(x,y)=(x,0)$; precisely the axis points are fixed. All of them have least period $p$, while every off-axis point is transient. Therefore $$\sum_{n\geq1}\frac{\#\operatorname{Fix}(T^n)}{n}z^n
=\sum_{k\geq1}\frac{z^{kp}}{k}
=-\log(1-z^p),$$ which proves the final clause of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

#### Parameter boundary and a counterexample.

The theorem is stated for odd primes. Characteristic $2$ is a benign degeneration in which $-a=a$, but it is outside the labelled odd-prime family fixed here. Replacing the field by a composite residue ring is not benign: over $\mathbb Z/4\mathbb Z$, the state $(2,2)$ reaches ordinate zero after one step because $2\cdot2=0$, before the complete-residue factorial collapse. Also the time-one target $(3,2)$ has two sources, since $2y=2\pmod4$ has $y=1,3$. Thus the $1/p/0$ fibre trichotomy and the equal-arm graph use field invertibility essentially.

L0.19L0.34L0.38 Neighbour & Overlap receiving no separation credit & Literal separation used here\
Triangular-family sources & Family membership, factorial iteration, degree/period language & Complete nonpermutation graph plus the all-time target equation $v=yC_t(u)$\
P99/P104 & Product or cocycle notation & No sublattice layers or random matrix words; one scalar product dies at a deterministic residue time\
P150 & Finite plane, fibres, graph, and zeta interface & Polynomial map, one $p$-cycle, depth exactly $p$, and progressive all-time image $p(p-t)+t$; no rational totalization or Lyness identity\
P154 & Finite noninvertible map with equal-depth branches & Factorial arms into a translating cycle, not parity-halving subgroup forests into fixed roots\

The first row of [\[tab:firewall\]](#tab:firewall){reference-type="ref" reference="tab:firewall"} is an owner subtraction, not a comparison of strength. The literature search used exact formulas, coordinate-swapped forms, triangular-system terminology, factorial cocycles, and functional graphs. It found the direct family inclusion above and broad functional-graph background, but no source in the bounded search stating the entire graph--fibre conjunction. Such a bounded search is not an ownership certificate.

# Deterministic exact audit

The accompanying script `verify.py` uses only the Python standard library and no randomness. It keeps the literal one-step map separate from all theorem formulas. Its lanes compare literal trajectories with the factorial iterate; discover cycles and tails by first repetitions; check literal indegrees and every labelled arm; construct every target fibre for all $0\leq t\leq p+3$; and compare every fixed set for $1\leq n\leq3p$. The run spans the 25 odd primes through $101$, namely $75{,}993$ states and $18{,}942{,}551$ assertions. Frozen stdout in `CANONICAL.txt` ends with

    PROFILE_SHA256 b44a7815c886a98409b5f56a0c26ce24f8644fa4f6b57a238d5a50d8a2d83810
    TOTAL boxes=25 states=75993 assertions=18942551
    VERDICT PASS_EXACT_REPLAY

The exhaustive replay is a regression and falsification control; the all-parameter quantifiers rest on the proofs above.

#### Reproducibility.

The repository contains the script, canonical transcript, claim/evidence matrix, source-verification ledger, control results, and build instructions.

#### Limitations.

The theorem is restricted to odd prime fields. It makes no claim for prime powers or composite residue rings, and the finite source search is not an ownership certificate. The deterministic replay is bounded evidence, not a proof of the all-prime quantifier.

#### Data availability.

No external dataset is used. All code, frozen transcripts, and claim ledgers needed to reproduce the reported audit accompany the manuscript.

#### Ethics statement.

This work uses no human participants, personal data, animals, or randomized empirical inference.

#### Author contributions.

The anonymous author performed the mathematical analysis, source audit, software implementation, exact verification, and manuscript preparation.

#### Conflict of interest.

The anonymous author declares no conflict of interest.

#### Funding.

No external funding is reported.

#### External status.

The manuscript is anonymous and for internal evaluation only. External circulation remains `HOLD_EXTERNAL`.
