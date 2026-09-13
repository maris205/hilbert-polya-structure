---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--213-receiver-limited-cyclic-transfer"
canonical_tex: "symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/main.tex"
canonical_pdf: "symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/frozen_round0/main.pdf"
source_sha256: "74fd3730d0f7e1d56e51d6043fc59c73c44f4e33fe17248563f8947f461ded65"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Terminal states and one-step fibres of receiver-limited cyclic transfer

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/frozen_round0/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We consider labelled nonnegative integer states on a cycle, with simultaneous current $\min(a_i,a_{i+1})$ from site $i$ to site $i+1$. The current is limited by the receiver's mass, not its vacancy. Every orbit reaches a fixed point: after subtraction of the invariant minimum, each original positive run deposits its mass at its original right endpoint. The sharp worst fixation time on states of total mass $N$ is zero for cycles of length at most two or $N=0$, is $\lceil\log_2N\rceil$ for length three and $N\ge1$, and is $N-1$ for longer cycles and $N\ge1$. We also give every target's one-step sources through a disjoint comparison-word parametrization. Each word reduces to forced dyadic recursions and independent integer intervals. This yields an exact product for fixed-target fibres and proves that the largest one-step fibre has growth $\Theta_n(N^{\lfloor n/3\rfloor})$ at each fixed cycle length $n\ge3$. All statements are proved deductively; a separately declared finite verification protocol is not used to extrapolate the conclusions.
bibliography:
- references.bib
title: |
  Terminal states and one-step fibres of\
  receiver-limited cyclic transfer
```

## Markdown 正文

# The rule and the questions {#sec:rule}

For integers $n\ge1$ and $N\ge0$, let $$X_{n,N}=\left\{a\in\mathbb Z_{\ge 0}^n:\ \sum_{i=0}^{n-1}a_i=N\right\}.$$ Site labels and cyclic orientation are fixed, and every index is read modulo $n$. Put $$\label{eq:rule}
 q_i(a)=\min(a_i,a_{i+1}),\qquad
 F(a)_i=a_i-q_i(a)+q_{i-1}(a).$$ All currents use the old state. Since $0\le q_i(a)\le a_i$, every updated coordinate is nonnegative; summation telescopes, so $F$ maps $X_{n,N}$ to itself. There is no scheduler, hidden history or quotient by rotation. The rule is an abstract finite deterministic system; no chemical realization is asserted.

Two questions organize the note. Where does each initial state end, and how many labelled sources produce a prescribed target in one step? The first answer uses permanent zero separators after subtraction of the minimum. The second uses the unique weak-ascent/strict-descent word of a source. The temporal description includes a sharp worst clock (Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}); the source parametrization includes every target, not only fixed targets (Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}). Their combination gives an exact fixed-target product and the largest-fibre exponent (Theorem [\[thm:growth\]](#thm:growth){reference-type="ref" reference="thm:growth"}).

#### Relation to conservative rules.

Conservation by local currents is background structure. For finite-alphabet one-dimensional cellular automata, Boccara and Fukś [@boccara2002] give a local characterization of number conservation. That characterization is not a terminal-state or all-target inverse formula for [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"}; its finite-alphabet setting also differs from the present family over all masses $N$.

Receiver mass must be distinguished from receiver vacancy. In the ultradiscrete Burgers rule studied by Nishinari and Takahashi [@nishinari1998], the corresponding current has the form $$\min(M,a_i,L-a_{i+1}),$$ with a capacity $L$ and an optional current bound $M$; the version without the current bound retains $L-a_{i+1}$. Equation [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"} instead uses $a_{i+1}$, with no fixed site-capacity parameter. Fukuda, Segawa and Watanabe [@fukuda2023] derive related discrete and ultradiscrete Burgers variants through correlated random walks; the examined preprint formulation likewise uses a vacancy term and an additional evolving variable. These literal comparisons do not establish nonconjugacy under arbitrary encodings, or priority for the current.

Permanent-zero arguments, ordered piecewise-linear chambers, dyadic integrality tests and interval products are elementary tools here. The claims concern their fully evaluated consequences for [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"}, with scope and exclusions stated in Section [5](#sec:verification){reference-type="ref" reference="sec:verification"}.

# Terminal states and sharp fixation time {#sec:temporal}

For a state $a$, write $m=\min_i a_i$ and $r=a-m\mathbf 1$. A positive run of $r$ is a maximal cyclic interval of positive coordinates. Unless $r=0$, its zero coordinates separate these runs. The right endpoint of a run is its last positive site in the chosen orientation.

[\[lem:minimum\]]{#lem:minimum label="lem:minimum"} The minimum is invariant under $F$. A zero coordinate remains zero, and $$F(a+c\mathbf 1)=F(a)+c\mathbf 1\qquad(c\in\mathbb Z_{\ge 0}).$$

Adding $c$ to every coordinate adds $c$ to every current, giving the displayed identity. If $a_i=0$, then $q_{i-1}=q_i=0$, so $F(a)_i=0$. The residual $r$ is nonnegative and has a zero, which persists. Therefore $\min_i F(r)_i=0$, and translation gives $\min_i F(a)_i=m$.

[\[prop:terminal\]]{#prop:terminal label="prop:terminal"} Every orbit fixes. Its terminal residual has, at each original run's original right endpoint, the total mass of that run, and is zero elsewhere. The terminal state is obtained by adding $m$ back. In particular the fixed states, and also all recurrent states, are precisely $$\label{eq:fixed}
 (a_i-m)(a_{i+1}-m)=0\qquad\text{for every }i.$$

Work with $r$. Original zero boundaries persist and carry no current, so each original run interval keeps its total mass $M$. If both $r_{i-1}$ and $r_i$ are positive, then $$F(r)_i\ge\min(r_{i-1},r_i)>0.$$ A positive site can therefore disappear only at the first site of its current run. With its predecessor zero, it disappears exactly when its mass is at most the next site's mass. Thus a run cannot split internally, and can lose at most one positive site per update. It cannot acquire a site across an existing zero.

Let $e$ be the original right endpoint, initially of mass $b>0$. It never disappears: its next site remains zero, and hence $$F(r)_e=r_e+\min(r_{e-1},r_e).$$ While its run has at least two sites, this increases $r_e$ by at least one. Since $r_e\le M$, there are at most $M-b$ nonfixed rounds in that run. The run must reduce to the single mass $M$ at $e$, which is fixed. Original runs are separated throughout, so the global fixation time is the maximum of their fixation times.

If [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} holds, all residual currents vanish. Conversely a residual run of length at least two makes its endpoint increase, so the state is not fixed. Uniform states correspond to $r=0$. Every orbit has just been shown to fix; hence a recurrent state must itself be fixed.

Define $\tau(a)$ to be the least $t\ge0$ such that $F^t(a)$ is fixed, and put $H(n,N)=\max_{a\in X_{n,N}}\tau(a)$.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For the whole labelled carrier, $$\label{eq:height}
 H(n,N)=
 \begin{cases}
 0,&n\le2\text{ or }N=0,\\
 \lceil\log_2 N\rceil,&n=3,\ N\ge1,\\
 N-1,&n\ge4,\ N\ge1.
 \end{cases}$$

For $n=1$ the only current cancels; for $n=2$ the two currents are equal. Thus $F$ is the identity in both cases. The case $N=0$ is immediate. For $n\ge3$, Proposition [\[prop:terminal\]](#prop:terminal){reference-type="ref" reference="prop:terminal"} bounds every nontrivial run's clock by $M-b\le N-1$.

For $n=3$, a nontrivial residual run has length two. Write its masses as $(A,B)$, followed by zero, with $A,B>0$ and $M=A+B$. Its update is $$(A,B)\longmapsto\bigl((A-B)_+,\,B+\min(A,B)\bigr).$$ Induction gives, including all times after saturation, $$\label{eq:two-site}
 A_t=(M-2^tB)_+,\qquad B_t=\min(2^tB,M).$$ Indeed $B_{t+1}=\min(2B_t,M)$ and $A_{t+1}=M-B_{t+1}$. The exact clock is the least $t$ with $2^tB\ge M$, at most $\lceil\log_2N\rceil$. For $N\ge2$, the state $(N-1,1,0)$ attains this bound. For $N=1$, every state is fixed and the stated value is zero.

For $n\ge4$ and $N\ge3$, use $(N-2,1,1,0,\ldots,0)$. At times $0\le t\le N-2$, its first three coordinates are $$(N-2-t,\,1,\,1+t).$$ While the first coordinate is positive, the middle coordinate receives and sends one, and the last receives one. At time $N-2$ the state has the pair $(1,N-1)$ at its last two occupied positions; one further update gives the single mass $N$. Thus the clock is $N-1$. For $N=2$, use $(1,1,0,\ldots,0)$, whose clock is one. For $N=1$, all states are fixed. These witnesses attain every remaining branch of [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}.

# Every one-step source {#sec:inverse}

For $n\le2$, the identity rule gives one source for each target. Assume $n\ge3$ and fix $y\in X_{n,N}$. A source $a$ has the unique comparison word $$\label{eq:word}
 s_i=1\ \Longleftrightarrow\ a_i\le a_{i+1};
 \qquad s_i=0\ \Longleftrightarrow\ a_i>a_{i+1}.$$ Equality belongs only to 1. The all-zero word is impossible on a cycle. The all-one word forces a uniform source, contributing one source if $y$ is uniform and none otherwise.

For a mixed word, a valley $v$ has $s_{v-1}=0,s_v=1$. Let $p$ be the next peak, where $s_{p-1}=1,s_p=0$, and $w$ the next valley. Unwrap the indices along $v,\ldots,p,\ldots,w$, and put $r=p-v\ge1$, $d=w-p\ge1$. Apply the construction to every such block once around the labelled cycle. This convention does not quotient by rotation and is independent of the valley used to start reading.

Substitution in [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"} gives all four local equations: $$\label{eq:local-table}
\begin{array}{c|c|c}
s_{i-1}&s_i&F(a)_i\\ \hline
0&1&a_i\\
1&1&a_{i-1}\\
0&0&2a_i-a_{i+1}\\
1&0&a_i+a_{i-1}-a_{i+1}
\end{array}.$$ For example, the $0,0$ case has incoming current $a_i$ and outgoing current $a_{i+1}$. Ties satisfy the table with convention [\[eq:word\]](#eq:word){reference-type="eqref" reference="eq:word"}.

#### Valleys and strict descent interiors.

First set $A_v=y_v$ at every valley. In each zero-run, work backwards: $$\label{eq:descent}
 A_j=\frac{y_j+A_{j+1}}2,\qquad j=w-1,w-2,\ldots,p+1.$$ Reject the word if any forced value is nonintegral or negative, or if $A_j\le A_{j+1}$. When $d=1$, there is no interior to force and $A_{p+1}=A_w$ is already assigned. These tests enforce every strict descent edge except the one leaving the peak.

#### A one-edge ascent.

If $r=1$, force $$\label{eq:short-peak}
 A_p=y_p-A_v+A_{p+1},
 \qquad A_v\le A_p>A_{p+1}.$$ Failure of either comparison rejects the word. The comparisons also ensure nonnegativity. This block leaves no choice.

#### A longer ascent.

For $r\ge2$, require $$\label{eq:ascent-tests}
 y_{v+1}=y_v,\qquad
 y_{v+1}\le y_{v+2}\le\cdots\le y_{p-1},$$ and assign $A_j=y_{j+1}$ for $v\le j\le p-2$. The equality makes the valley assignment consistent. For $r=2$, the order chain has one term and is vacuous; the displayed equality still applies. The remaining coordinates are the prepeak and peak. Define $$\label{eq:interval}
 S_p=y_p+A_{p+1},\quad L_p=y_{p-1},\quad
 U_p=\min\left(\left\lfloor\frac{S_p}{2}\right\rfloor,\ y_p-1\right).$$ The expression $y_p-1$ subtracts the integer one; it is not $y_{p-1}$. Choose any integer $t_p\in[L_p,U_p]$ and put $$\label{eq:pair}
 a_{p-1}=t_p,\qquad a_p=S_p-t_p.$$ The last two weak ascent comparisons give $L_p\le t_p$ and $2t_p\le S_p$. Strict descent from the peak gives $S_p-t_p>A_{p+1}$, equivalently $t_p\le y_p-1$. Thus [\[eq:interval\]](#eq:interval){reference-type="eqref" reference="eq:interval"} gives exactly all the comparisons at these coordinates, including the permitted tie $t_p=a_p$. All coordinates are nonnegative, since $L_p\ge0$ and $a_p>A_{p+1}\ge0$.

Let $W_s(y)=0$ if any forced test fails. Otherwise set $$\label{eq:weight}
 W_s(y)=\prod_{\substack{\text{one-runs of }s\\ r\ge2}}
             \max(0,U_p-L_p+1),$$ with empty product one. An empty interval makes the weight zero.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For every target $y\in X_{n,N}$ with $n\ge3$, $$\label{eq:atlas}
 |F^{-1}(y)|=
 \mathbf 1_{\{y\text{ uniform}\}}+
 \sum_{\substack{s\in\{0,1\}^n\\s\ne0^n,\ s\ne1^n}}W_s(y).$$ Each positive summand supplies all its sources explicitly through [\[eq:descent\]](#eq:descent){reference-type="eqref" reference="eq:descent"}--[\[eq:pair\]](#eq:pair){reference-type="eqref" reference="eq:pair"}. Within a word the interval choices are independent; between words the source sets are disjoint.

For necessity, take an actual source and its unique word [\[eq:word\]](#eq:word){reference-type="eqref" reference="eq:word"}. The constant cases were handled above. In a mixed word, the valley line of [\[eq:local-table\]](#eq:local-table){reference-type="eqref" reference="eq:local-table"} forces $A_v=y_v$. The descent-interior line forces [\[eq:descent\]](#eq:descent){reference-type="eqref" reference="eq:descent"}, with all tests satisfied by the actual source. A one-edge ascent forces [\[eq:short-peak\]](#eq:short-peak){reference-type="eqref" reference="eq:short-peak"}. For a longer ascent, each ascent-interior line forces the shifted target assignments and [\[eq:ascent-tests\]](#eq:ascent-tests){reference-type="eqref" reference="eq:ascent-tests"}. The peak line forces the sum $a_{p-1}+a_p=S_p$. The actual comparisons then force precisely the interval [\[eq:interval\]](#eq:interval){reference-type="eqref" reference="eq:interval"}. Thus every source provides an admitted word and one integer from each of its intervals.

For sufficiency, take an admitted word and independent integers from its nonempty intervals. Valleys, descent interiors, ascent interiors, prepeaks and peaks cover the cycle. Their coordinate roles are disjoint, except for the explicitly consistent valley assignment in a longer ascent. The case $r=1$ uses its valley directly and has no free prepeak; $d=1$ uses the next valley directly and has no descent interior. Thus every coordinate is assigned, including blocks crossing index zero.

The tests give exactly weak ascent on the 1-edges and strict descent on the 0-edges, with all entries nonnegative. The resulting vector therefore has precisely the specified word, not merely a word compatible with some ties. Every line of [\[eq:local-table\]](#eq:local-table){reference-type="eqref" reference="eq:local-table"} has target value $y_i$, so $F(a)=y$. Conservation in [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"} then implies $\sum_i a_i=\sum_i y_i=N$: no additional mass condition is missing. Hence the vector belongs to $X_{n,N}$.

Different interval choices differ at a prepeak coordinate. Different words cannot describe the same source because [\[eq:word\]](#eq:word){reference-type="eqref" reference="eq:word"} is unique. These facts prove the bijection, independence and multiplicities in [\[eq:atlas\]](#eq:atlas){reference-type="eqref" reference="eq:atlas"}.

There are at most $2^n-2$ mixed words and $O(n)$ arithmetic operations per word. Consequently [\[eq:atlas\]](#eq:atlas){reference-type="eqref" reference="eq:atlas"} evaluates the fibre cardinality using $O(n2^n)$ arithmetic operations; this is not a bit-cost bound independent of $N$, nor the cost of printing every source. No search over mass compositions or unbounded currents remains inside a weight. In particular a target is in the image exactly when [\[eq:atlas\]](#eq:atlas){reference-type="eqref" reference="eq:atlas"} is positive; no linear-time image test is asserted.

# Fixed-target fibres and largest-fibre degree {#sec:fibres}

Let $y$ be a nonuniform fixed target. Subtract $m=\min_i y_i$. By Proposition [\[prop:terminal\]](#prop:terminal){reference-type="ref" reference="prop:terminal"}, the positive residual coordinates are isolated spikes. Write their masses as $p_e$ at spike sites $e$, and let $d_e\ge1$ be the number of consecutive zeros immediately preceding $e$, back to the previous spike. For a sole spike, $d_e=n-1$.

[\[prop:fixed-fibre\]]{#prop:fixed-fibre label="prop:fixed-fibre"} A uniform target has exactly one source. For a nonuniform fixed target, $$\label{eq:fixed-fibre}
 |F^{-1}(y)|=
 \prod_{\{e:\ d_e\ge2\}}\left(\left\lfloor p_e/2\right\rfloor+1\right).$$

Any source has the same minimum $m$ by Lemma [\[lem:minimum\]](#lem:minimum){reference-type="ref" reference="lem:minimum"}, so work with residuals. If $y$ is uniform, a source with minimum $m$ and total mass $nm$ must be the uniform vector.

For a nonuniform target, consider a positive source run. In one step, it can lose only its first site and at most one site, by the proof of Proposition [\[prop:terminal\]](#prop:terminal){reference-type="ref" reference="prop:terminal"}. Since the output has only isolated positive sites, the run must have length one or two. Its right endpoint remains positive and must be one of the target spikes. Conversely every target spike must arise in this way: a zero source site remains zero, and a nonempty source run has a positive output at its endpoint.

A two-site run ending at $e$ must have masses $(h,p_e-h)$ at $e-1,e$. Its head disappears exactly when $0<h\le p_e-h$. Allowing $h=0$ includes the one-site run. When $d_e=1$, the proposed head at $e-1$ is preceded by the previous target spike. That previous spike is positive in the source, because a source zero cannot produce a positive target. Thus a positive head there could not disappear, so only $h=0$ is possible. When $d_e\ge2$, there is an available zero before the proposed head, and exactly $$0\le h\le\lfloor p_e/2\rfloor$$ is allowed. Heads at different spikes do not overlap and remain separated: a nonzero head is allowed only in a gap of at least two zeros. The choices are independent and exhaust all source runs, proving [\[eq:fixed-fibre\]](#eq:fixed-fibre){reference-type="eqref" reference="eq:fixed-fibre"}. The empty product equals one.

Let $M_n(N)=\max_{y\in X_{n,N}}|F^{-1}(y)|$.

[\[thm:growth\]]{#thm:growth label="thm:growth"} Fix $n\ge3$ and put $k=\lfloor n/3\rfloor$. Then $$\label{eq:upper}
 M_n(N)\le (2^n-1)(N+1)^k\qquad(N\ge0),$$ and $$\label{eq:lower}
 M_n(N)\ge \left(\frac{N}{2k}\right)^k\qquad(N\ge2k).$$ In particular $M_n(N)=\Theta_n(N^k)$ as $N\to\infty$. For $n\le2$ one has $M_n(N)=1$.

Each interval factor in [\[eq:weight\]](#eq:weight){reference-type="eqref" reference="eq:weight"} belongs to a one-run of at least two edges, followed by a nonempty zero-run. These disjoint runs use at least three edges per factor. There can therefore be at most $k$ factors in a mixed word. In a positive-weight word, every permitted interval value is a coordinate of a source in $X_{n,N}$, by Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}, so its interval has at most $N+1$ integers. Including the possible uniform source, $$|F^{-1}(y)|\le 1+(2^n-2)(N+1)^k
              \le(2^n-1)(N+1)^k,$$ proving [\[eq:upper\]](#eq:upper){reference-type="eqref" reference="eq:upper"}.

Choose $k$ sites with at least two zeros between consecutive sites cyclically; this is possible because $3k\le n$. For $N\ge2k$, put $q=\lfloor N/(2k)\rfloor$, assign mass $2q$ to each chosen site, and add the remaining $N-2kq$ to one of them. The resulting target has minimum zero and $k$ positive isolated spikes. By Proposition [\[prop:fixed-fibre\]](#prop:fixed-fibre){reference-type="ref" reference="prop:fixed-fibre"}, its fibre has at least $(q+1)^k\ge(N/(2k))^k$ sources. This proves [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"}. The two bounds give the stated exponent; the identity rule handles $n\le2$.

For instance, $(0,0,2q,0,0,2q)$ on six sites has exactly $(q+1)^2$ sources, for every integer $q\ge0$ (including the uniform zero target). This is a deductive family, not a claim of a numerical asymptotic test. Theorem [\[thm:growth\]](#thm:growth){reference-type="ref" reference="thm:growth"} determines the exponent, not the exact finite-$N$ maximum or all maximizing targets.

# Finite verification and limits {#sec:verification}

The proofs above apply to all declared parameters. A paper-local, standalone author verifier is specified separately for the complete box $1\le n\le6$, $0\le N\le4$: 30 carriers containing 461 labelled states. It compares direct forward-graph predecessor sets with independently implemented comparison-word source sets. It also checks terminal states, minimum preservation, exact finite-carrier height, the two-site clock, fixed-target products and the stated finite instances of the bounds. Word-level output records forced-test rejection reasons and admitted intervals, including the possibility of two free intervals at $n=6$.

The declared author verification has been executed on exactly this finite box. Its accepted initial output supplies the paper canonical. Two separate author replays reproduce that complete output byte-for-byte under unchanged accepted source, parameter, canonical and relevant runtime inputs. These are bounded author checks, not either independent manuscript review. Earlier candidate and gate checks remain historical evidence, not a converted paper canonical. Neither this finite enumeration nor its replay proves an all-parameter statement or the asymptotic theorem.

The temporal and inverse arguments serve different purposes. The original endpoint argument does not decide which comparison words can produce a target. The one-step atlas alone does not establish repeated absorption or the sharp fixation time. Their relationship does not make either a claim of global originality.

Several questions remain outside this note: a closed pointwise clock for $n\ge4$; exact values of $M_n(N)$ and all maximizers at every finite parameter; all-time fibres and a full basin census; and a linear-time image criterion. No arbitrary-encoding nonconjugacy result is asserted.
