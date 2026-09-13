---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--174-minimum-pivot-mobius-feedback"
canonical_tex: "symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback/main.pdf"
source_sha256: "5d1790a4fc0f15a79e3632646783598cc3d97da61fca11735c20f881c58df958"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Minimum-Pivot Möbius Feedback on Projective-Line Subsets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/174-minimum-pivot-mobius-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Order the finite points of $\mathbb P^1(\mathbb F_p)$ by their standard representatives. For a $k$-subset $S$, translate its least finite point to zero and then apply projective inversion. We determine the resulting state-dependent finite dynamics for every prime $p$ and $2\leq k\leq p$. Its first two images are respectively the subsets containing $\infty$ and those containing $\{0,\infty\}$; the latter form an inversion core. Consequently the sharp maximum tail is two, $\mathcal M^4=\mathcal M^2$, and all cycles have length at most two. We give the exact three depth layers and a coefficient formula for the fixed states. Independently, every target fibre is determined: for a target containing $\infty$, the possible feedback pivots form an initial interval, so its pivot enumerator is $1+z+\cdots+z^{h-1}$ for an explicit target-dependent $h$; every other target has empty fibre. A standalone exhaustive control checks $131{,}018{,}555$ assertions in all $69$ parameter boxes through $p=19$. The clock is shallow and the coordinate order is artificial; this provisional-amber Round-0 note remains on external hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Minimum-Pivot Möbius Feedback on Projective-Line Subsets'
```

## Markdown 正文

# The map and its claim ceiling

Fix a prime $p$ and identify $$\mathbb P^1(\mathbb F_p)=\mathbb F_p\cup\{\infty\},
 \qquad 0<1<\cdots<p-1<\infty,$$ where inequalities refer to the displayed integer representatives, not to an order on the field. For $2\leq k\leq p$, let $\mathcal X_{p,k}=\binom{\mathbb P^1(\mathbb F_p)}{k}$. Every state $S\in\mathcal X_{p,k}$ contains a finite point. Put $$a(S)=\min(S\cap\mathbb F_p),
 \qquad
 \gamma_a(x)=\frac{1}{x-a},$$ with the projective conventions $\gamma_a(a)=\infty$ and $\gamma_a(\infty)=0$, and define $$\label{eq:literal}
 \mathcal M(S)=\gamma_{a(S)}(S).$$ The coordinate order and prime-field representatives are part of the literal rule. In particular, [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"} is not claimed to be projectively natural.

Dynamics of one fixed fractional-linear transformation over a finite field are established background [@ElAbdalaouiShparlinski2019]. So are $\mathrm{PGL}(2)$-orbits of projective configurations and the $\mathrm{PGL}(2,q)$ action on projective-line subsets [@AluffiFaber1993; @Tricot2025]. More generally, minimal and canonical images of ordered subsets under permutation-group actions, together with canonizing elements, have a direct algorithmic theory [@JeffersonEtAl2019]. Those facts, projective inversion, canonical- image language, and ordinary subset enumeration receive no contribution credit here. The map [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"} is not a canonical-image function: it need not be constant on a group orbit, it chooses one projectivity from the current pivot rather than minimizing over the group, and its iterates and target fibres are the objects being counted.

The internal proof-engine firewall is stricter still. P96 already covers finite subsets under a transformation induced from a fixed base map, and P168 covers spans of inverses of finite-field subspaces. Our rule chooses its projectivity from the current subset and takes no span, but fixed-map hyperspace language and inverse geometry remain zero credit. The killed AQN control is closer architecturally: it selects a normalization from the state and then exposes a classical group action. Its quotient is adjacent to simultaneous group multiplication and cyclic rotation on words [@GrinbergMao2024]. We therefore assign no value to adaptive normalization or the eventual involution by itself. The only residual under evaluation is the literal two-stage containment tower together with the nonuniform target-local inverse below. A bounded search found no literal owner for that conjunction, but a search non-hit is not evidence of novelty, priority, ownership, or freedom to operate.

Write $$\mathcal Z_{p,k}=\{S\in\mathcal X_{p,k}:\infty\in S\},\qquad
 \mathcal Y_{p,k}=\{S\in\mathcal X_{p,k}:\{0,\infty\}\subseteq S\},$$ and put $R_{p,k}=|\mathcal Y_{p,k}|=\binom{p-1}{k-2}$. For a target $T\in\mathcal X_{p,k}$ define $$\label{eq:height}
 \beta(T)=\max\bigl(\{\overline{y^{-1}}:
      y\in T\cap\mathbb F_p^\times\}\cup\{0\}\bigr),
 \qquad h(T)=p-\beta(T),$$ where the bar denotes the representative in $\{1,\ldots,p-1\}$.

[\[thm:main\]]{#thm:main label="thm:main"} For every prime $p$ and $2\leq k\leq p$, the map [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"} has the following properties.

(i) Its first two images are $$\label{eq:images}
     \operatorname{im}\mathcal M=\mathcal Z_{p,k},\qquad \operatorname{im}\mathcal M^2=\mathcal Y_{p,k}.$$ The recurrent set is $\mathcal Y_{p,k}$. On it, $\mathcal M$ fixes $0,\infty$ setwise and sends $x\in\mathbb F_p^\times$ to $x^{-1}$; hence $\mathcal M^4=\mathcal M^2$ on all of $\mathcal X_{p,k}$.

(ii) A state has tail zero, one, or two according as it lies in $\mathcal Y_{p,k}$, $\mathcal Z_{p,k}\setminus\mathcal Y_{p,k}$, or $\mathcal X_{p,k}\setminus\mathcal Z_{p,k}$. Thus the depth enumerator is $$\label{eq:depth}
      D_{p,k}(u)=\binom{p-1}{k-2}
      +\binom{p-1}{k-1}u+\binom pk u^2,$$ and the maximum tail is sharply two.

(iii) Suppose $p$ is odd and set $r=k-2$. The number of fixed states is $$\label{eq:fixed}
       F_{p,k}=[v^r](1+v)^2(1+v^2)^{(p-3)/2}.$$ The remaining recurrent states form $(R_{p,k}-F_{p,k})/2$ two-cycles. For $p=2,k=2$, the recurrent core is one fixed state; set $F_{2,2}=1$. In either case, the number of weak components is $(R_{p,k}+F_{p,k})/2$, and for every $m\geq1$, $$\label{eq:fixed-iterates}
       |\operatorname{Fix}(\mathcal M^m)|=
       \begin{cases}F_{p,k},&m\text{ odd},\\
       R_{p,k},&m\text{ even}.
       \end{cases}$$

(iv) Every one-step target fibre, including empty fibres, satisfies $$\label{eq:fibre}
      |\mathcal M^{-1}(T)|=
      \begin{cases}
      0,&\infty\notin T,\\
      h(T),&\infty\in T,
      \end{cases}$$ and, when $\infty\in T$, its pivot-marked form is $$\label{eq:marked}
      \sum_{S:\,\mathcal M(S)=T}z^{a(S)}
        =1+z+\cdots+z^{h(T)-1}.$$

(v) For $1\leq q\leq p$, $$\label{eq:fibre-distribution}
     \#\{T\in\mathcal X_{p,k}:|\mathcal M^{-1}(T)|=q\}
       =\binom{p-q}{k-2}.$$ There are $\binom pk$ zero-fibre targets, and the maximum fibre is $p-k+2$, attained by a unique target.

Parts (i)--(iii) give the whole temporal graph; part (iv) gives every incoming branch and its feedback label. The marked inverse is not inferred from the depth census.

# The two-stage image tower

[\[lem:tower\]]{#lem:tower label="lem:tower"} The pivot always maps to $\infty$, and $\infty$ is the unique point that maps to $0$. Consequently $$S\notin\mathcal Z_{p,k}\Longrightarrow
 \mathcal M(S)\in\mathcal Z_{p,k}\setminus\mathcal Y_{p,k},\qquad
 S\in\mathcal Z_{p,k}\Longrightarrow\mathcal M(S)\in\mathcal Y_{p,k}.$$ Moreover, $\mathcal M$ restricts to ordinary inversion on $\mathcal Y_{p,k}$.

The first two assertions follow directly from the projective conventions for $\gamma_{a(S)}$. If $S$ avoids $\infty$, its image avoids $0$; if $S$ contains $\infty$, its image contains both $0$ and the image $\infty$ of the pivot. Finally, a state in $\mathcal Y_{p,k}$ has pivot zero, so its update is $x\mapsto x^{-1}$ with $0$ and $\infty$ exchanged. As a set it still contains both distinguished points, and a second update returns it.

Lemma [\[lem:tower\]](#lem:tower){reference-type="ref" reference="lem:tower"} gives $\operatorname{im}\mathcal M\subseteq\mathcal Z_{p,k}$. Conversely, if $T\in\mathcal Z_{p,k}$, then $S=\gamma_0(T)$ contains zero, has pivot zero, and satisfies $\mathcal M(S)=T$. Thus $\operatorname{im}\mathcal M=\mathcal Z_{p,k}$. The same lemma sends this first image into $\mathcal Y_{p,k}$, while every $T\in\mathcal Y_{p,k}$ satisfies $\mathcal M^2(T)=T$. This proves [\[eq:images\]](#eq:images){reference-type="eqref" reference="eq:images"}.

The three implications in Lemma [\[lem:tower\]](#lem:tower){reference-type="ref" reference="lem:tower"} show that states in $\mathcal Y_{p,k}$, $\mathcal Z_{p,k}\setminus\mathcal Y_{p,k}$, and $\mathcal X_{p,k}\setminus\mathcal Z_{p,k}$ have tails zero, one, and two, respectively. No state outside $\mathcal Y_{p,k}$ can therefore recur. Choosing the remaining points in each stratum gives the three coefficients in [\[eq:depth\]](#eq:depth){reference-type="eqref" reference="eq:depth"}. The last coefficient is nonzero because $k\leq p$, so the height two is attained. Since $\mathcal M^2(S)\in\mathcal Y_{p,k}$ for every $S$ and $\mathcal M^2$ is the identity there, $\mathcal M^4=\mathcal M^2$ globally.

A recurrent state is $\{0,\infty\}\cup A$ for an $r$-subset $A\subseteq\mathbb F_p^\times$. At odd $p$, inversion has singleton orbits $\{1\}$ and $\{-1\}$ and $(p-3)/2$ two-element orbits. An invariant $r$-subset is a union of these orbits, which gives the coefficient [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. All other recurrent points are exchanged in pairs. At $p=2,k=2$, no nonzero point is selected and the sole core state is fixed.

Every transient state reaches one recurrent cycle, so the weak components are counted by the recurrent cycles: $F_{p,k}+(R_{p,k}-F_{p,k})/2=(R_{p,k}+F_{p,k})/2$. A point fixed by a positive iterate is recurrent. Inversion fixes exactly $F_{p,k}$ recurrent states at odd times and all $R_{p,k}$ recurrent states at even times, proving [\[eq:fixed-iterates\]](#eq:fixed-iterates){reference-type="eqref" reference="eq:fixed-iterates"}.

# Every-target fibres and marked pivots

The inverse calculation remembers the state-selected normalization that the forward image counts forget.

[\[lem:nowrap\]]{#lem:nowrap label="lem:nowrap"} Fix $a\in\mathbb F_p$. The inverse projectivity is $$\label{eq:inverse-projectivity}
 \gamma_a^{-1}(\infty)=a,\qquad
 \gamma_a^{-1}(0)=\infty,\qquad
 \gamma_a^{-1}(y)=a+y^{-1}\quad(y\in\mathbb F_p^\times).$$ For integer representatives $0\leq a<p$ and $1\leq b<p$, $$\label{eq:nowrap}
 \overline{a+b}\geq a\quad\Longleftrightarrow\quad a<p-b.$$

Equation [\[eq:inverse-projectivity\]](#eq:inverse-projectivity){reference-type="eqref" reference="eq:inverse-projectivity"} follows by solving $y=1/(x-a)$, including the two projective points. If $a+b<p$, reduction does nothing and the left side of [\[eq:nowrap\]](#eq:nowrap){reference-type="eqref" reference="eq:nowrap"} holds. If $a+b\geq p$, the representative is $a+b-p<a$ because $b<p$. These are the only cases.

Every image contains $\infty$, proving the zero line of [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Now take $T\in\mathcal Z_{p,k}$. A parent with proposed pivot $a$ is forced to be $S_a=\gamma_a^{-1}(T)$. Besides the forced point $a$, its finite points are $$\overline{a+y^{-1}},\qquad y\in T\cap\mathbb F_p^\times.$$ Thus $a$ is actually the least finite point of $S_a$ exactly when every one of these representatives is at least $a$. By Lemma [\[lem:nowrap\]](#lem:nowrap){reference-type="ref" reference="lem:nowrap"}, this holds precisely when $$0\leq a<p-\max\bigl(\{\overline{y^{-1}}:
                   y\in T\cap\mathbb F_p^\times\}\cup\{0\}\bigr)=h(T).$$ Each valid $a$ yields a parent, and different values yield different parents because they are their parents' least finite points. Hence the valid pivots are exactly $0,\ldots,h(T)-1$, proving both [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} and [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"}.

The formula also resolves the rooted trees attached to the inversion core. For $T\in\mathcal Y_{p,k}$, its pivot-zero parent is the recurrent point $\gamma_0(T)$, and its other $h(T)-1$ parents have depth one. A target in $\mathcal Z_{p,k}\setminus\mathcal Y_{p,k}$ has $h(T)$ parents, all at depth two. Targets outside $\mathcal Z_{p,k}$ have none. Thus no aggregate branch remains unspecified.

Inversion permutes $\mathbb F_p^\times$, so count a target through the set $B(T)=\{\overline{y^{-1}}:y\in T\cap\mathbb F_p^\times\}$. Put $j=p-q$. For $j\geq1$, a target with $\beta(T)=j$ and without zero has $|B(T)|=k-1$ and is counted by $\binom{j-1}{k-2}$. A target containing zero has $|B(T)|=k-2$ and is counted by $\binom{j-1}{k-3}$. Their sum is $\binom{j}{k-2}$. At $j=0$, only $T=\{0,\infty\}$ at $k=2$ occurs, again matching $\binom{0}{k-2}$. Substitution of $j=p-q$ proves [\[eq:fibre-distribution\]](#eq:fibre-distribution){reference-type="eqref" reference="eq:fibre-distribution"}.

Targets avoiding $\infty$ number $\binom pk$. A positive fibre of size $q$ exists exactly when $p-q\geq k-2$, so the maximum is $p-k+2$; equality in the binomial count shows that its target is unique. As a consistency check, the distribution has total source mass $$\sum_{q=1}^{p}q\binom{p-q}{k-2}=\binom{p+1}{k},$$ which is the carrier size.

# Exact controls, boundary, and limitations

Representative specializations of the theorem are shown below. The depth column lists the populations at depths zero, one, and two.

   $p$   $k$    $|\mathcal X_{p,k}|$   $|\operatorname{im}\mathcal M|$   $R_{p,k}$   $F_{p,k}$          depths   max fibre
  ----- ----- ---------------------- --------------------------------- ----------- ----------- --------------- -----------
    2     2                        3                                 2           1           1         $1,1,1$           2
    3     3                        4                                 3           2           2         $2,1,1$           2
    5     3                       20                                10           4           2        $4,6,10$           4
    7     4                       70                                35          15           3      $15,20,35$           5
   11     5                      792                               330         120           8   $120,210,462$           8

At the smallest parameter the entire graph is visible: $$\{0,1\}\longmapsto\{1,\infty\}
 \longmapsto\{0,\infty\}\longmapsto\{0,\infty\}.$$ This handles $p=2,k=2$ directly. The lower bound $k\geq2$ avoids the singleton $\{\infty\}$, which has no finite pivot. The upper bound $k\leq p$ makes the depth-two stratum nonempty. The full projective line at $k=p+1$ is a separate degenerate fixed state and is outside the stated family.

A paper-local verifier uses only the Python standard library and imports no scouting code. It exhausts every allowed $k$ for $p\in\{2,3,5,7,11,13,17,19\}$: all $69$ complete parameter boxes. For every state it rebuilds the edge, orbit, first and second images, and $\mathcal M^4=\mathcal M^2$; for every target it checks the fibre, unique pivot labels, fibre-size distribution, and mass identity. Two fresh processes match the frozen $131{,}018{,}555$-assertion transcript byte for byte. These checks are controls against implementation and boundary mistakes; the arguments above prove the all-parameter statements.

The limitations are structural. The sharp clock is only two, the recurrent action is ordinary inversion, and the literal rule depends on an artificial coordinate order. P96, P168, and AQN remove the nearest internal engines, but a specialist source or general adaptive-section theorem could still subsume the residual pivot interval. This anonymous Round-0 artifact is therefore `PROVISIONAL_AMBER / HOLD_EXTERNAL`. It makes no novelty, priority, ownership, release, or submission claim.
