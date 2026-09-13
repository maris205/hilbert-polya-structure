---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--204-previous-smaller-distance-feedback"
canonical_tex: "symbolic_dynamics/papers/204-previous-smaller-distance-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/204-previous-smaller-distance-feedback/main.pdf"
source_sha256: "49c6f883cfe9a2a4109e021f9dbb7ee91dcfcbe10ff8a32310d292e6461efe52"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Step Dynamics and Flagged Fibres\protect of Previous-Smaller Distances

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/204-previous-smaller-distance-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/204-previous-smaller-distance-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/204-previous-smaller-distance-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/204-previous-smaller-distance-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/204-previous-smaller-distance-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Recomputing strict previous-smaller distances on an inversion sequence reaches an explicit recurrent involution after at most two updates. The nearest-smaller statistic is classical, but feedback compares the new distances themselves rather than following the original predecessor links. We prove that zero positions remain fixed and that the second iterate records precisely the original ascent set inside each positive block. At local block position $j$, the recurrent choices are $1$ and $j$, which are exchanged by the next update. The maximum transient is two for every length at least four, with separate smaller-length boundaries. The recurrent and fixed populations are $F_{2n-1}$ and $F_{n+1}$. Independently, we evaluate every target fibre at every time $t\ge2$ by an alternating product of binomial coefficients. The formula retains the global position bounds of each block and distinguishes the two eventual phases. Complete proofs, together with bounded exact verification, separate this endpoint-to-fibre description from its classical static nearest-smaller and inversion-statistic ingredients.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Two-Step Dynamics and Flagged Fibres\
  of Previous-Smaller Distances
```

## Markdown 正文

# The map and its scope

For $n\ge1$ use indices $0,\ldots,n-1$ and the inversion-sequence box $$\label{eq:carrier}
 E_n=\{x=(x_0,\ldots,x_{n-1}):0\le x_i\le i\},\qquad |E_n|=n!.$$ The strict previous-smaller distance map is $$\label{eq:map}
 P(x)_i=
 \begin{cases}
 i-\max\{h<i:x_h<x_i\},&\text{if this set is nonempty},\\
 0,&\text{otherwise}.
 \end{cases}$$ It is a self-map of $E_n$: a positive distance lies between $1$ and $i$. Every output is computed from the same old word. In particular, the update recomputes comparisons; it does not follow a pointer stored in $x_i$. The tail $\tau(x)$ is the least $t\ge0$ at which $P^t(x)$ is periodic.

Static nearest-smaller values are classical algorithmic objects [@Berkman1993Nearest]. Parent-distance representations also encode Cartesian trees [@Park2019Cartesian], although that paper's convention uses an earlier value at most the current value. Ties matter here: [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} sends $011$ to $012$, whereas the weak convention sends it to $011$. Neither the static search nor its data structures are contributions of this note.

The two results below concern the feedback itself. First, its second iterate decodes the original zero positions and internal ascent sets, and the resulting core has an explicit involution. Second, each target in either eventual phase has an evaluated source count with its original position-dependent bounds. Ascent sets and zero positions are already classical joint statistics: under the usual inversion code they correspond to permutation descents and left-to-right maxima [@Lin2018Sextuple]. The contribution asserted here is the concrete iterate and its fibre evaluation, not the discovery of those statistics or of the counting tools.

# Two-step decoding and the recurrent involution

Zeros are invariant under $P$. If $x_i=0$, no nonnegative entry is smaller; if $x_i>0$, the earlier entry $x_0=0$ is smaller. Let $\mathcal B(x)$ be the set of pairs $(r,m)$ such that $r+1,\ldots,r+m$ is a maximal positive block of $x$, immediately following the zero at position $r$. Its output distances lie in $\{1,\ldots,j\}$ at position $r+j$, because the nearest smaller predecessor cannot be to the left of $r$.

[\[lem:rise\]]{#lem:rise label="lem:rise"} Let $(r,m)\in\mathcal B(x)$ and $b_j=P(x)_{r+j}$. Then $b_1=1$, and for $2\le j\le m$ either $b_j=1$ or $b_j>b_{j-1}$.

Write $p_j$ for the nearest smaller predecessor of $x_{r+j}$. If $b_j>1$, then $x_{r+j}\le x_{r+j-1}$. Every entry strictly between $p_{j-1}$ and $r+j-1$ is at least $x_{r+j-1}$, hence at least $x_{r+j}$; the entry at $r+j-1$ is not smaller either. Thus $p_j\le p_{j-1}$ and $b_j=r+j-p_j\ge r+j-p_{j-1}=b_{j-1}+1$. The first entry of the block has its zero barrier as nearest smaller predecessor, so $b_1=1$.

Define the block core $$\label{eq:core}
 \mathcal C_n=\{y\in E_n:y_{r+j}\in\{1,j\}
       \text{ for all }(r,m)\in\mathcal B(y),\ 1\le j\le m\}.$$ On this set let $J$ keep zeros and block starts fixed and exchange $1\leftrightarrow j$ at each local position $j\ge2$.

[\[thm:temporal\]]{#thm:temporal label="thm:temporal"} The zero set of $P^2(x)$ is that of $x$. In each positive block, $$\label{eq:decoder}
 P^2(x)_{r+1}=1,\qquad
 P^2(x)_{r+j}=
 \begin{cases}
 j,&x_{r+j-1}<x_{r+j},\\
 1,&x_{r+j-1}\ge x_{r+j},
 \end{cases}\quad 2\le j\le m.$$ Moreover $P^2(E_n)=\mathcal C_n$, $P|_{\mathcal C_n}=J$, and $P^4=P^2$. The recurrent set is exactly $\mathcal C_n$, all periods divide two, and $$\label{eq:height}
 \max_{x\in E_n}\tau(x)=
 \begin{cases}0,&n\le2,\\1,&n=3,\\2,&n\ge4.\end{cases}$$

For $j\ge2$, $b_j=1$ is equivalent to the original adjacent ascent in [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"}. When $b_j=1$, its only smaller value in the block or left barrier is zero, so the next distance is $j$. When $b_j>1$, Lemma [\[lem:rise\]](#lem:rise){reference-type="ref" reference="lem:rise"} makes the immediately preceding distance smaller, so the next distance is one. This proves [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"} and $P^2(E_n)\subseteq\mathcal C_n$.

At a core coordinate with value $j\ge2$, the preceding core value is at most $j-1$, and the next distance is one. At a core coordinate with value one, only the left zero is smaller, and the next distance is $j$. Thus $P$ restricts to $J$, with $J^2$ the identity. Each core word is therefore its own two-step preimage. This proves the exact second image and $P^4=P^2$. Every periodic state lies in the second image, so the recurrent set is precisely the core.

For $n=1,2$ the whole carrier is fixed. At $n=3$ the six states are $000,001,002,010,011,012$; only $002$ is outside the core, and it maps to $001$. For $n\ge4$, prepend $n-4$ zeros to $0122$. Its first-image positive block is $112$, whose last value is neither one nor its local index three. That image is not recurrent, proving the sharp lower bound two; the second-image theorem supplies the upper bound.

[\[cor:census\]]{#cor:census label="cor:census"} Let $F_0=0,F_1=1$ and $F_{k+2}=F_{k+1}+F_k$. There are $F_{2n-1}$ recurrent states, $F_{n+1}$ fixed states, and $(F_{2n-1}-F_{n+1})/2$ strict two-cycles.

For the $N=n-1$ positions after the initial zero, let $a_N,b_N$ count core words ending respectively in zero and in a positive entry, with $(a_0,b_0)=(1,0)$. A new zero has one choice, a positive block starts with one, and its continuation has the two distinct choices $1,j$. Hence $$\label{eq:countrec}
 (a_{N+1},b_{N+1})=(a_N+b_N,a_N+2b_N).$$ For $N\ge1$, induction gives $(a_N,b_N)=(F_{2N-1},F_{2N})$, so the total is $F_{2N+1}$, also valid at $N=0$. A core word is fixed exactly when every positive block is a singleton. Binary words of length $N$ with no consecutive ones are counted by $F_{N+2}$: conditioning on an initial zero or an initial $10$ gives the Fibonacci recurrence, with initial counts $1,2$. The remaining core states are paired by $J$.

# Every target fibre after two steps

Fix $(r,m)$ with $r\ge0,m\ge1$ and a set $A\subseteq\{2,\ldots,m\}$. For $B\subseteq A$, let $\mathop{\mathrm{Seg}}(B)$ partition $\{1,\ldots,m\}$ into consecutive segments by cutting immediately before each $j\in B$. Define the globally flagged count $$\label{eq:cut}
 D_{r,m}(A)=\sum_{B\subseteq A}(-1)^{|A|-|B|}
       \prod_{[a,b]\in\mathop{\mathrm{Seg}}(B)}\binom{r+b}{b-a+1}.$$ The word "flagged" refers to the position-dependent bounds $r+j$; the offset $r$ is part of the count, not an ignorable block label. For $y\in\mathcal C_n$ and $t\ge2$, set $$\label{eq:mask}
 A_t(y;r,m)=
 \begin{cases}
 \{j\in\{2,\ldots,m\}:y_{r+j}=j\},&t\text{ even},\\
 \{j\in\{2,\ldots,m\}:y_{r+j}=1\},&t\text{ odd}.
 \end{cases}$$

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For every $n\ge1$, every $t\ge2$ and every $y\in E_n$, $$\label{eq:fibre}
 \bigl|(P^t)^{-1}(y)\bigr|=
 \begin{cases}
 \displaystyle\prod_{(r,m)\in\mathcal B(y)}D_{r,m}(A_t(y;r,m)),
       &y\in\mathcal C_n,\\
 0,&y\notin\mathcal C_n.
 \end{cases}$$ The empty product is one. Thus the all-zero target has exactly one source.

Theorem [\[thm:temporal\]](#thm:temporal){reference-type="ref" reference="thm:temporal"} gives $P^t(x)=J^{t-2}P^2(x)$. A source of $y$ must have exactly its zero set. For a core target, [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"} says that the source's internal ascent set in block $(r,m)$ must be $A_t(y;r,m)$, and this condition is sufficient. Different positive blocks are independent after the zero positions are fixed. It remains to count one block with entries $1\le x_{r+j}\le r+j$ and exact internal ascent set $A$.

Impose nonascent on each edge outside $A$. Inclusion--exclusion on failures of the required ascents gives the sum over $B\subseteq A$ with sign $(-1)^{|A|-|B|}$, where ascents are allowed only before positions in $B$. The resulting word is weakly decreasing on every segment $[a,b]$ of $\mathop{\mathrm{Seg}}(B)$. All entries of that segment are at most its first entry, which is at most $r+a$. Conversely, every weakly decreasing sequence of length $b-a+1$ in $\{1,\ldots,r+a\}$ satisfies the later, increasing position bounds. Counting its value multiplicities gives $$\binom{(r+a)+(b-a+1)-1}{b-a+1}=\binom{r+b}{b-a+1}.$$ Segments are independent, giving [\[eq:cut\]](#eq:cut){reference-type="eqref" reference="eq:cut"}; blocks are independent, giving [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Noncore targets have no source because every iterate at time at least two lies in $\mathcal C_n$.

For a two-letter block, the number of strictly rising positive sources is $$D_{r,2}(\{2\})=(r+1)(r+2)-\binom{r+2}{2}
               =\binom{r+2}{2}.$$ It equals one at offset zero and three at offset one. Thus an unflagged ascent count cannot substitute for the block factor in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. At even times this ascent factor belongs to the local target $12$; at odd times at least three it belongs to the exchanged target $11$.

# Verification and limitations

The paper-local standard-library verifier exhausts $E_n$ for $1\le n\le8$ (46,233 input states). It tests zero barriers, the first-image inequality, the endpoint, core action, sharp heights and both Fibonacci counts. Every target fibre is compared with literal iteration at $t=2,3,4,5$. A separate bounded source-word enumeration checks 315 flagged ascent patterns for $0\le r\le4$, $1\le m\le6$. The resulting 485,578 assertions are finite pressure on the proofs, not an argument for larger parameters.

The results concern the full box [\[eq:carrier\]](#eq:carrier){reference-type="eqref" reference="eq:carrier"} and the strict rule [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. They do not characterize the first image or one-step fibres, classify largest fibres, or extend the carrier to arbitrary words. Under the classical inversion code, [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} also counts an intersection of prescribed permutation descent and record-position sets; that interpretation is not a new statistic [@Lin2018Sextuple]. Fibonacci recurrence, inclusion--exclusion and multiset counting likewise remain standard. The narrow conclusion is the exact two-step decoder and the explicit source count for each target and eventual phase. No claim of global priority or external publication clearance is made.
