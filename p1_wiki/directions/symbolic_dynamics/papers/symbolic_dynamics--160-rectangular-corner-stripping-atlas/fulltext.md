---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--160-rectangular-corner-stripping-atlas"
canonical_tex: "symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas/main.tex"
canonical_pdf: "symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas/main.pdf"
source_sha256: "a898c69e641821f68b6c3bde7b4184355b2d1dfdf5addffafdc635b4c1dce4c2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rectangular-Corner Stripping of Integer Partitions: Clocks, Fibres, and Parameter Recovery

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/160-rectangular-corner-stripping-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix positive integers $a,b$. From the Ferrers diagram of an integer partition, delete the first $a$ rows and first $b$ columns and iterate on the translated southeast remainder. We determine this rank-changing finite dynamics on all partitions of weight at most $N$. A cell-coordinate formula gives every iterate, a pointwise rectangle-survival clock, and the sharp height $$\min\{t\geq0:(at+1)(bt+1)>N\}.$$ Independently, we enumerate every rank-$t$ fibre. For a nonempty target $\mu$, the weight series is a forced monomial times $1/((q;q)_{at}(q;q)_{bt})$; the empty target has a separate finite hook series. This yields an exact image threshold under every weight cap. The thresholds of the one-cell, two-cell row, and two-cell column targets recover the ordered pair $(a,b)$. Generalized rectangular Durfee viewpoints, static two-boundary symbols and decompositions, and their two-factor partition products are explicit zero-credit inputs. A deterministic audit checks $3{,}462{,}895$ exact consequences.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Rectangular-Corner Stripping of Integer Partitions:\
  Clocks, Fibres, and Parameter Recovery
```

## Markdown 正文

# System and source boundary {#sec:setup}

Let $\mathcal P$ be the set of integer partitions, including $\varnothing$. We use English Ferrers diagrams: $(i,j)$ is a cell of $\lambda=(\lambda_1,\lambda_2,\ldots)$ when $1\leq j\leq\lambda_i$. For fixed $a,b\geq1$, define $$\label{eq:map}
 T_{a,b}(\lambda)
  =(\lambda_{a+1}-b,\lambda_{a+2}-b,\ldots)_+,$$ where nonpositive parts are omitted. Geometrically, we delete the first $a$ rows and first $b$ columns, then translate the southeast remainder. Since weight decreases on every nonempty state, [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} restricts to the finite carrier $\mathcal P_{\leq N}=\{\lambda:|\lambda|\leq N\}$.

The operation has classical inputs. Barnes and Savage delete the first row and column in a recurrence for graphical partitions and explicitly note its Durfee decrement [@BarnesSavage1995]. Generalized rectangular Durfee viewpoints, including unequal or rational-slope rectangles, occur in the classical literature [@GordonHouten1968; @Andrews1971]. In particular, Chen, Ji, and Zang describe an $m$-Durfee rectangle symbol by the two partitions beside and below a largest rectangle, with total weight equal to rectangle area plus the two boundary weights [@ChenJiZang2015 Sec. 3]. Andrews and Eriksson give standard Ferrers, Gaussian-polynomial, bounded-partition, and Durfee background [@AndrewsEriksson2004]. We assign zero credit to all of this static rectangle and two-boundary structure, to Ferrers conjugation, and to the product $$\label{eq:pochhammer}
 \frac1{(q;q)_{r}}=\prod_{j=1}^{r}\frac1{1-q^j},\qquad (q;q)_{0}=1,$$ which enumerates partitions with at most $r$ parts, equivalently those whose largest part is at most $r$. Thus the two-factor Pochhammer factorization is also zero credit. The scoped residual begins only with iterating the fixed literal crop $(a,b)$ through every time, prescribing an arbitrary southeast target, separating the empty branch, proving exact cap support, and recovering the ordered parameters. The source search is bounded; no novelty, priority, or owner-absence conclusion is drawn.

::: {#tab:subtraction}
  Record                                                      Zero-credit input                                                Scoped residual
  ----------------------------------------------------------- ---------------------------------------------------------------- -------------------------------------------------------------------------------------------
  Barnes--Savage [@BarnesSavage1995]                          delete one row and column; Durfee decrement                      no residual from the one-step square case
  Gordon--Houten; Andrews [@GordonHouten1968; @Andrews1971]   generalized/rational-slope rectangular Durfee viewpoints         no residual from a static rectangle
  Chen--Ji--Zang [@ChenJiZang2015]                            static two-boundary symbol, decomposition, and product factors   no residual from static factorization
  Here                                                        generic finite-map language                                      fixed-crop all-time atlas, arbitrary targets, empty branch, cap support, ordered recovery

  : Source subtraction and retained scope.
:::

For a nonempty $\mu$, write $\ell(\mu)$ for its length and set, for $h,w\geq0$, $$\begin{aligned}
 M_{h,w}(\mu)&=|\mu|+h(\mu_1+w)+w\ell(\mu),\label{eq:M}\\
 E_{h,w}(q)&=\frac1{(q;q)_{h}}\sum_{k=0}^{w}
       \frac{q^{k(h+1)}}{(q;q)_{k}}.\label{eq:E}\end{aligned}$$ Let $\tau_{a,b}(\lambda)$ be the least $t$ for which $T_{a,b}^{t}(\lambda)=\varnothing$.

# The rectangle clock {#sec:clock}

The temporal statement is pointwise before it is enumerative.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For $a,b\geq1$ and $t\geq0$, put $h=at,w=bt$. Then $$\label{eq:iterate}
 T_{a,b}^{t}(\lambda)
   =(\lambda_{h+1}-w,\lambda_{h+2}-w,\ldots)_+.$$ Consequently $$\label{eq:point-clock}
 \tau_{a,b}(\lambda)=\min\{t\geq0:\lambda_{at+1}\leq bt\},
 \qquad
 \tau_{a,b}(\lambda)>t\iff (at+1,bt+1)\in\lambda,$$ where missing parts are zero. The empty partition is the unique recurrent state, and the maximum entry time on $\mathcal P_{\leq N}$ is $$\label{eq:height}
 H_{a,b}(N)=\min\{t\geq0:(at+1)(bt+1)>N\}.$$ Moreover, the exact weight-refined absorbed census is $$\label{eq:absorbed}
 \sum_{\lambda:T_{a,b}^{t}(\lambda)=\varnothing}q^{|\lambda|}
   =E_{at,bt}(q).$$ Thus $[q^n]E_{at,bt}$ counts weight-$n$ states absorbed by rank $t$; consecutive differences give every exact clock shell.

One update retains exactly the cells $(i,j)$ satisfying $i>a,j>b$ and sends them to $(i-a,j-b)$. Induction adds these offsets and proves [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}. The retained diagram is nonempty exactly when its northwest cell existed before translation, which is [\[eq:point-clock\]](#eq:point-clock){reference-type="eqref" reference="eq:point-clock"}. Every nonempty state loses $(1,1)$, so only $\varnothing$ is recurrent.

Survival through rank $t$ forces the rectangle $[1,at+1]\times[1,bt+1]$ and therefore at least $(at+1)(bt+1)$ cells. Conversely, that rectangle itself survives rank $t$. This proves [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}, including $H_{a,b}(0)=0$.

It remains to count $T^t(\lambda)=\varnothing$, equivalently $\lambda_{h+1}\leq w$. Slice by $k=\lambda_{h+1}$. For $k=0$, the diagram has at most $h$ rows and contributes $1/(q;q)_{h}$. For $1\leq k\leq w$, remove a $k$-by-$(h+1)$ rectangle. The excess in the first $h$ rows is an arbitrary partition with at most $h$ parts, while the remaining lower rows form an arbitrary partition with largest part at most $k$. This reversible decomposition contributes $q^{k(h+1)}/((q;q)_{h}(q;q)_{k})$. Summing the disjoint slices proves [\[eq:absorbed\]](#eq:absorbed){reference-type="eqref" reference="eq:absorbed"}.

For $a=b=1$, [\[eq:point-clock\]](#eq:point-clock){reference-type="eqref" reference="eq:point-clock"} is the classical Durfee-size statement; that specialization is contextual rather than part of the retained claim. For unequal $a,b$, the clock tests a moving rectangular corner and the capped height is the first failure of a quadratic area inequality.

# Every target at every time {#sec:fibres}

The clock sees one corner cell. The inverse problem instead records two entire boundaries around a prescribed southeast remainder.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} Let $t\geq0$, $h=at$, and $w=bt$. For every target $\mu\in\mathcal P$, $$\label{eq:fibre-series}
 \sum_{\lambda:T_{a,b}^{t}(\lambda)=\mu}q^{|\lambda|}
 =\begin{cases}
 \displaystyle
  \frac{q^{M_{h,w}(\mu)}}{(q;q)_{h}(q;q)_{w}},&\mu\ne\varnothing,\\[7pt]
 E_{h,w}(q),&\mu=\varnothing.
 \end{cases}$$ For $t\geq1$, a nonempty $\mu$ lies in the rank-$t$ image of $\mathcal P_{\leq N}$ exactly when $$\label{eq:image-threshold}
 M_{at,bt}(\mu)\leq N.$$ When this holds, $\mu$ has a source of every weight from its threshold through $N$; the corresponding coefficient in [\[eq:fibre-series\]](#eq:fibre-series){reference-type="eqref" reference="eq:fibre-series"} is the exact size-refined fibre.

The empty line is [\[eq:absorbed\]](#eq:absorbed){reference-type="eqref" reference="eq:absorbed"}. Fix nonempty $\mu=(\mu_1,\ldots,\mu_r)$. Formula [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} says that a source has the forced middle rows $$\label{eq:middle}
 \lambda_{h+j}=\mu_j+w\quad(1\leq j\leq r),
 \qquad \lambda_{h+r+1}\leq w.$$ The first $h$ rows have baseline $\mu_1+w$. Their excesses form an arbitrary partition $\gamma$ with at most $h$ parts. The rows below the block in [\[eq:middle\]](#eq:middle){reference-type="eqref" reference="eq:middle"} form an arbitrary partition $\beta$ with largest part at most $w$. Conversely, after padding $\gamma$ with zeros, any such pair $(\gamma,\beta)$ reconstructs a unique weakly decreasing source. The forced weight is $$h(\mu_1+w)+\sum_{j=1}^r(\mu_j+w)=M_{h,w}(\mu),$$ and the two independent free pieces contribute $1/(q;q)_{h}$ and $1/(q;q)_{w}$. This proves the nonempty line of [\[eq:fibre-series\]](#eq:fibre-series){reference-type="eqref" reference="eq:fibre-series"}. At $t=0$, both orders are zero and the sole source is $\mu$, as required.

For $t\geq1$, both $h$ and $w$ are positive. The product $1/((q;q)_{h}(q;q)_{w})$ has a positive coefficient in every nonnegative degree $d$: take $\gamma=(d)$ and $\beta=\varnothing$, interpreting $\gamma=\varnothing$ when $d=0$. Since $h\geq1$, this $\gamma$ has at most $h$ parts. Hence no source exists below the forced weight and a source exists at every weight at or above it. Intersecting with $\mathcal P_{\leq N}$ proves [\[eq:image-threshold\]](#eq:image-threshold){reference-type="eqref" reference="eq:image-threshold"}.

The separate empty line is essential. Substituting an undefined $\mu_1$ or $\ell(\mu)$ into the nonempty formula would miss all hook-shaped sources. Likewise, the threshold claim is restricted to $t\geq1$; at $t=0$, the fibre consists only of the target at its exact weight.

# Coefficient consequences and one worked fibre {#sec:coefficients}

Let $$p_r(d)=[q^d]\frac1{(q;q)_{r}},$$ with $p_r(d)=0$ for $d<0$. Thus $p_r(d)$ counts partitions of $d$ with at most $r$ parts. Reading coefficients in Theorem [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"} gives the fully numerical form $$\label{eq:coefficient-fibre}
 \#\{\lambda\vdash n:T_{a,b}^{t}(\lambda)=\mu\}
 =\sum_{j=0}^{n-M_{h,w}(\mu)}p_h(j)
    p_w\bigl(n-M_{h,w}(\mu)-j\bigr)$$ for nonempty $\mu$, where the sum is zero when $n<M_{h,w}(\mu)$. This formula separates the top and bottom freedom even after the total source weight is fixed.

For example, take $(a,b)=(2,1)$, $t=2$, and $\mu=(3,1)$. Then $h=4,w=2$ and $$M_{4,2}((3,1))=4+4(3+2)+2\cdot2=28.$$ The target therefore first appears at source weight $28$, and its exact fibre series is $$\label{eq:worked-fibre}
 \frac{q^{28}}{(q;q)_{4}(q;q)_{2}}
  =q^{28}\bigl(1+2q+5q^2+9q^3+17q^4+\cdots\bigr).$$ Hence its fibres at source weights $28,29,30,31,32$ have sizes $1,2,5,9,17$. The corresponding empty fibre is not obtained by setting $\mu=\varnothing$ here; by [\[eq:E\]](#eq:E){reference-type="eqref" reference="eq:E"} it is $$E_{4,2}(q)=\frac1{(q;q)_{4}}
 \left(1+\frac{q^5}{(q;q)_{1}}+\frac{q^{10}}{(q;q)_{2}}\right).$$

Two aggregate consequences are useful checks on the atlas. First, the exact rank-$t$ image size on the capped carrier is $$\label{eq:image-size}
 1+\#\{\mu\ne\varnothing:M_{at,bt}(\mu)\leq N\};$$ the initial one counts the empty target. Second, because the fibres partition all sources, summing [\[eq:fibre-series\]](#eq:fibre-series){reference-type="eqref" reference="eq:fibre-series"} over targets gives the formal mass identity $$\label{eq:mass-identity}
 \frac1{(q;q)_\infty}
 =E_{h,w}(q)+\frac1{(q;q)_{h}(q;q)_{w}}
   \sum_{\mu\ne\varnothing}q^{M_{h,w}(\mu)}.$$ This is not an additional ownership claim; it is the global consistency equation for the target-resolved bijection.

# Duality and parameter recovery {#sec:recovery}

Let $\lambda'$ be the conjugate partition. Transposing cell coordinates in the definition immediately gives $$\label{eq:duality}
 T_{a,b}(\lambda)'=T_{b,a}(\lambda').$$ This symmetry explains why a square clock alone cannot orient the two parameters. The target thresholds do.

[\[cor:recovery\]]{#cor:recovery label="cor:recovery"} Let $m(\mu)$ denote the minimum source weight of the one-step nonempty target $\mu$. Then $$\begin{aligned}
 m((1))&=(a+1)(b+1),\label{eq:mcell}\\
 m((2))&=m((1))+a+1,\label{eq:mrow}\\
 m((1,1))&=m((1))+b+1.\label{eq:mcolumn}\end{aligned}$$ Therefore $$\label{eq:recover}
 a=m((2))-m((1))-1,\qquad
 b=m((1,1))-m((1))-1.$$ The ordered update parameters are determined by the one-step target-support profile.

Theorem [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"} identifies $m(\mu)$ with $M_{a,b}(\mu)$. Substitution of the three displayed shapes gives $$\begin{aligned}
 M_{a,b}((1))&=1+a(1+b)+b,\\
 M_{a,b}((2))&=2+a(2+b)+b,\\
 M_{a,b}((1,1))&=2+a(1+b)+2b.\end{aligned}$$ Taking the two differences proves [\[eq:mcell\]](#eq:mcell){reference-type="eqref" reference="eq:mcell"}--[\[eq:recover\]](#eq:recover){reference-type="eqref" reference="eq:recover"}.

This interface is stronger than recovering only the symmetric product $(a+1)(b+1)$. Row and column probes retain the orientation exchanged by [\[eq:duality\]](#eq:duality){reference-type="eqref" reference="eq:duality"}.

# Exact control and limitations {#sec:control}

The accompanying standard-library verifier enumerates every partition through weight $32$. For $(a,b)=(1,1),(2,1),(1,3),(2,2),(3,2)$ and $0\leq t\leq5$, it compares literal repeated updates with [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}; checks every clock and capped height; checks conjugation duality; and compares every fibre coefficient for targets through weight nine with [\[eq:fibre-series\]](#eq:fibre-series){reference-type="eqref" reference="eq:fibre-series"}. It also checks fibre-mass conservation, the zero/nonzero image threshold, and all three recovery probes. The frozen run contains $3{,}462{,}895$ exact assertions.

Enumeration is falsification pressure, not proof. The theorem is formal and enumerative: it makes no asymptotic statement, no mixing claim, and no claim about a probability law unless a distribution on partitions is separately chosen. The bounded owner search does not certify absence, and all external release, posting, authorship, and submission decisions remain outside this anonymous internal note.

This artifact remains `HOLD_EXTERNAL`.
