---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--129-rootward-active-pile-coalescence"
canonical_tex: "symbolic_dynamics/papers/129-rootward-active-pile-coalescence/main.tex"
canonical_pdf: "symbolic_dynamics/papers/129-rootward-active-pile-coalescence/main.pdf"
source_sha256: "6f187199a00764f23faf40cf8efec56dfb989cdf4771ee5a3316f7b631d111dd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rootward Active-Pile Coalescence on a Path: Interface Additivity and Exact Jump Counts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/129-rootward-active-pile-coalescence>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/129-rootward-active-pile-coalescence/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/129-rootward-active-pile-coalescence/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/129-rootward-active-pile-coalescence/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/129-rootward-active-pile-coalescence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study a finite coalescing process on a rooted path. A discrete update selects one occupied nonroot site uniformly, moves its pile one edge toward the root, and erases multiplicity on contact. For every initial state $S=\{0=s_0<s_1<\cdots<s_r\}$, we prove that the expected number of updates to absorption is the additive interface functional $$\mathbb ET_S=\sum_{i=1}^{r}h(s_{i-1},s_i),$$ where $h$ is the meeting-time mean of two ordered rate-one pure-death paths. The proof Poissonizes the active-pile scheduler, identifies the embedded jump chain exactly, and converts its jump count into the integral of the number of open initial interfaces. A first-passage recurrence determines $h$; a ballot evaluation gives $h(m-1,m)=(2m-1)!!/(2m-2)!!$. Thus full occupancy on $\{0,\ldots,n-1\}$ has mean $$\sum_{m=1}^{n-1}\frac{(2m-1)!!}{(2m-2)!!}
   =\frac{4}{3\sqrt\pi}n^{3/2}+O(n^{1/2}).$$ We also give the complete support of the hitting-time law from every rooted state and the minimum-time mass from full occupancy. Exact rational controls corroborate all finite recurrences. Standard coalescing-walk, graphical, and first-passage machinery is treated as background; the owner search is bounded, and no novelty or external-release claim is made.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Rootward Active-Pile Coalescence on a Path:\
  Interface Additivity and Exact Jump Counts
```

## Markdown 正文

# The process and the subtraction boundary {#sec:model}

Let $S$ be a finite subset of $\mathbb N_0$ containing the root $0$. If $S\ne\{0\}$, select $v\in S\setminus\{0\}$ uniformly and set $$C_v(S)=(S\setminus\{v\})\cup\{v-1\}.                 \label{eq:update}$$ If $v-1$ is already occupied, the two piles coalesce; the state records no multiplicity. Let $T_S$ be the number of updates until $\{0\}$ is reached. This is an *active-pile* chain: uniform selection is among the current nonroot piles. Uniform selection from a fixed geometric set with lazy empty events gives a different discrete-time law.

Coalescing random walks and their voter-model duals form a classical interacting-particle framework; full occupancy, consensus time, and meeting-time comparison are established themes [@Cox1989; @Cooper2013; @Kanade2023]. Graphical constructions and recurrence questions on infinite or rooted carriers are likewise standard [@Benjamini2016]. Exact one-dimensional coalescence and reductions to simple-walk first passage also have a substantial history [@Ermakov1997]. We assign zero contribution credit to coalescing-walk formalism, graphical arrows, voter duality, meeting/hitting comparisons, ballot identities, and central-binomial asymptotics.

Three closer interfaces sharpen that subtraction. @Assiotis2018 develops stochastic coalescing flows associated with birth--death chains, while @SniadyUrban2026 treat prescribed coalescence patterns for nearest-neighbor systems, including birth--death chains, using ordered interval labels and an explicit finite coalescing construction. @HitczenkoWesolowski2025 [Theorem 3] identify, for step-initial TASEP, the expected active-particle count as the derivative of the expected total jump count. Their kernels and observables differ from ours, but the site-arrow flow, ordered-label-block, coalescence-pattern, and generic active-count--jump-current mechanisms all receive zero contribution credit here.

The literal chain in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} differs in three linked respects. Motion is deterministic and one-way, the scheduler is uniform among current piles, and $T_S$ counts embedded updates rather than elapsed coalescence time. The residual question is whether this update count admits an exact formula from an arbitrary initial set. A bounded primary-source search found no statement of the theorem package below. That non-hit is not a novelty certificate, so external release remains on hold.

The internal subtraction is also strict. P114 already owns synchronous rooted-forest peeling. P117 acts on labelled cyclic binary words by flipping every odd maximal run; its boundary-parity eroder has neither piles, a root, nor a random scheduler. P121 instead selects a current adjacent separator, performs a product-plus-one merge, and obtains a random-BST/Yule deletion history. Here the selected object is a current pile, a move need not coalesce, and the observable is the number of embedded effective updates. P126 concerns synchronous length-increasing refinement. Rooted monotonicity, eroder language, generic coalescence, adjacent interfaces, and random scheduling therefore receive no internal credit. The only claimed residual is the exact arbitrary-state embedded-update mean for the literal deterministic-rootward, uniform-active-pile chain, together with its support and full-start consequences.

# The finite law and its support {#sec:law}

Write $$\Phi(S)=\sum_{v\in S}v,
 \qquad G_S(z)=\mathbb E[z^{T_S}].$$

[\[prop:pgf\]]{#prop:pgf label="prop:pgf"} Every trajectory is absorbed after at most $\Phi(S)$ updates. Moreover, $$G_{\{0\}}(z)=1,
 \qquad
 G_S(z)=\frac{z}{|S|-1}
       \sum_{v\in S\setminus\{0\}}G_{C_v(S)}(z).       \label{eq:pgf}$$ Thus [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"} is a finite acyclic recursion for the complete law.

If $v-1\notin S$, the update decreases $\Phi$ by one. If $v-1\in S$, the collision removes $v$ and decreases $\Phi$ by $v$. The nonnegative integer potential therefore decreases strictly. Conditioning on the uniformly chosen first active site gives [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}; potential descent makes the recursion acyclic.

The recursion has no internal gaps, even for a sparse initial state.

[\[thm:support\]]{#thm:support label="thm:support"} If $S\ne\{0\}$, then $$\operatorname{supp}(T_S)=\{\max S,\max S+1,\ldots,\Phi(S)\}.       \label{eq:support}$$

Each update decreases $\Phi$ by at least one, so $T_S\leq\Phi(S)$. An update lowers the maximum occupied coordinate by at most one: moving the maximum either places it at its predecessor or removes it when that predecessor is occupied; a move below the maximum leaves it fixed. Hence $T_S\geq\max S$.

We prove that every intermediate value occurs by induction on $\Phi(S)$. Put $m=\max S$. If $m-1\notin S$, choose $m$ first. The successor has maximum $m-1$ and potential $\Phi(S)-1$, so induction and the first update realize the whole interval $[m,\Phi(S)]$.

Suppose instead that $m-1\in S$. The case $m=1$ is immediate. Choosing $m$ first is a collision; induction supplies $$.                                   \label{eq:lowinterval}$$ Let $a$ be the bottom of the consecutive occupied run ending at $m$. If $a=1$, moving $a$ collides at the root; if $a>1$, its predecessor is empty. Either move decreases the potential by one and leaves maximum $m$. This first choice and induction supply $$.                                     \label{eq:highinterval}$$ Since $m,m-1\in S$, we have $\Phi(S)\geq2m-1$; the integer intervals in [\[eq:lowinterval\]](#eq:lowinterval){reference-type="eqref" reference="eq:lowinterval"}--[\[eq:highinterval\]](#eq:highinterval){reference-type="eqref" reference="eq:highinterval"} touch or overlap. Their union proves [\[eq:support\]](#eq:support){reference-type="eqref" reference="eq:support"}. Every constructed schedule has positive probability because each of its active choices does.

Let $S_n=\{0,1,\ldots,n-1\}$ and $T_n=T_{S_n}$.

[\[cor:minmass\]]{#cor:minmass label="cor:minmass"} For $n\geq2$, $$\mathbb P(T_n=n-1)=\frac{1}{(n-1)!}.                         \label{eq:minmass}$$

A trajectory of length $n-1$ must reduce the number of nonroot piles at every update, so every move must collide. Removing a site before its larger neighbor would leave a vacancy for that neighbor's next move. The unique all-collision order is therefore $n-1,n-2,\ldots,1$. The successive numbers of active sites are $n-1,n-2,\ldots,1$, giving [\[eq:minmass\]](#eq:minmass){reference-type="eqref" reference="eq:minmass"}.

# Poisson clocks and interface additivity {#sec:interfaces}

The clock construction must preserve the discrete scheduler, not merely the set of possible moves. Fix an initial state $S$, put $M=\max S$, and place an independent rate-one Poisson clock at each site in the finite accessible set $\{1,\ldots,M\}$. A ring at an occupied site triggers [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}; a ring at an empty site is ignored, and the root has no clock. Every effective ring time is a stopping time for this finite clock vector. The strong Markov property gives fresh independent rate-one exponential residuals there, including at a newly occupied site whose clock may have rung earlier while empty. If the current state has $k$ nonroot piles, the next effective ring is consequently uniform among their $k$ sites, with total rate $k$. Hence the embedded effective-jump chain is exactly the chain of [1](#sec:model){reference-type="ref" reference="sec:model"}.

For $0\leq a\leq b$, define $h(a,b)$ by $$\begin{aligned}
 h(a,a)&=0,                                             \label{eq:hdiag}\\
 h(0,b)&=b,                                             \label{eq:hroot}\\
 h(a,b)&=\frac12+
 \frac{h(a-1,b)+h(a,b-1)}2 \quad(0<a<b).               \label{eq:hrec}\end{aligned}$$ This triangular recursion uniquely defines nonnegative rational values.

[\[thm:additivity\]]{#thm:additivity label="thm:additivity"} Let $S=\{0=s_0<s_1<\cdots<s_r\}$. Then $$\boxed{\displaystyle
 \mathbb E[T_S]=\sum_{i=1}^{r}h(s_{i-1},s_i).}                \label{eq:additivity}$$ The empty sum for $S=\{0\}$ equals zero.

Label the initial piles $0,1,\ldots,r$ from left to right and follow each label through the site-clock arrows. Labels that meet share one path thereafter. Rootward nearest-neighbor paths preserve order: they can coalesce but cannot cross.

More precisely, at every time each current pile carries a nonempty interval of initial labels, and the spatial order of the piles is the order of these intervals. This holds initially for the singleton intervals. A move to an empty predecessor carries one interval without changing the order. At a collision the occupied predecessor is the immediately preceding pile, so the two label intervals are consecutive and their union is again an interval. Induction over effective rings proves the claim. In particular, an outside label joining either member of a designated adjacent pair does not alter that path's future site arrows.

For $1\leq i\leq r$, let $\tau_i$ be the first meeting time of the paths started at $s_{i-1}$ and $s_i$. At time $t$, consecutive initial labels belong to the same current pile exactly when their interface has closed. The current piles are therefore the consecutive label blocks separated by open interfaces. One block contains the root, so the number $N_t$ of nonroot piles satisfies the pathwise identity $$N_t=\sum_{i=1}^{r}\mathbf 1_{\{\tau_i>t\}}.                  \label{eq:interfaces}$$

Let $J_t$ count effective updates by continuous time $t$. Conditional on the past just before $t$, its predictable intensity is $N_{t-}$. Thus, for each finite $t$, $$J_t-\int_0^tN_{u-}\,du$$ is the compensated jump-count martingale and $\mathbb EJ_t=\mathbb E\int_0^tN_{u-}\,du$. By [\[prop:pgf\]](#prop:pgf){reference-type="ref" reference="prop:pgf"}, there are at most $\Phi(S)$ effective waits; each has positive finite rate before absorption, so $J_\infty=T_S\leq\Phi(S)$ almost surely. Monotone convergence on both sides, followed by Tonelli's theorem, gives $$\begin{aligned}
 \mathbb ET_S
 &=\mathbb EJ_\infty
  =\mathbb E\int_0^\infty N_{t-}\,dt
  =\mathbb E\int_0^\infty N_t\,dt \notag\\
 &=\sum_{i=1}^{r}\mathbb E\int_0^\infty
       \mathbf 1_{\{\tau_i>t\}}\,dt
  =\sum_{i=1}^{r}\mathbb E\tau_i.                             \label{eq:compensator}\end{aligned}$$ The two time integrals agree because the jump times are Lebesgue-null.

It remains to identify one interface marginal. Before two paths at $0<a<b$ meet, they occupy distinct sites and read independent rate-one clocks. The next event takes mean time $1/2$; either the lower path moves to $a-1$ or the upper path moves to $b-1$, each with probability $1/2$. The strong Markov property supplies fresh exponentials even when a site was visited earlier. At equality the interface is closed, while a lower path at zero is fixed and the upper path needs $b$ mean-one moves. First-event conditioning is exactly [\[eq:hdiag\]](#eq:hdiag){reference-type="eqref" reference="eq:hdiag"}--[\[eq:hrec\]](#eq:hrec){reference-type="eqref" reference="eq:hrec"}, so $\mathbb E\tau_i=h(s_{i-1},s_i)$. Substitution into [\[eq:compensator\]](#eq:compensator){reference-type="eqref" reference="eq:compensator"} proves [\[eq:additivity\]](#eq:additivity){reference-type="eqref" reference="eq:additivity"}.

The interface lifetimes are generally dependent. Equation [\[eq:additivity\]](#eq:additivity){reference-type="eqref" reference="eq:additivity"} uses only the pathwise count [\[eq:interfaces\]](#eq:interfaces){reference-type="eqref" reference="eq:interfaces"}, Tonelli's theorem, and their individual means.

# A ballot evaluation and full occupancy {#sec:ballot}

The recurrence for $h$ is already an exact finite algorithm. Consecutive starts have a closed form.

[\[lem:adjacent\]]{#lem:adjacent label="lem:adjacent"} For every $m\geq1$, $$h(m-1,m)
 =\frac{(2m-1)!!}{(2m-2)!!}
 =\frac{2m}{4^m}\binom{2m}{m}.                         \label{eq:adjacent}$$ Equivalently, this value is $\mathbb E|W_{2m}|$ for a length-$2m$ simple symmetric walk $W$.

The case $m=1$ is [\[eq:hroot\]](#eq:hroot){reference-type="eqref" reference="eq:hroot"}. Suppose $m\geq2$ and put $p=m-1$. Superpose the two clocks until the paths meet or the lower path reaches zero. Each inter-event time has mean $1/2$, and the event type is a fair coin. Call a lower-path move an up-step and an upper-path move a down-step. The gap starts at one; a down-step at gap one closes the interface, while the $p$th up-step puts the lower path at zero.

If meeting occurs after $j$ up-steps and $j+1$ down-steps, the event word is a Catalan first-passage word. There are $$A_j=\frac{1}{j+1}\binom{2j}{j},\qquad 0\leq j<p,$$ such words. If the $p$th up-step occurs after $q$ down-steps, reflection at the first forbidden prefix gives $$B_{p,q}=\binom{p+q-1}{q}-\binom{p+q-1}{q-1},
 \qquad 0\leq q<p,                                    \label{eq:ballotcount}$$ where the second binomial coefficient is zero at $q=0$. On this second exit, the upper path is $p+1-q$ steps from zero. Consequently $$\begin{aligned}
 h(m-1,m)
={}&\sum_{j=0}^{p-1}
 \frac{A_j}{2^{2j+1}}\frac{2j+1}{2} \notag\\
 &+\sum_{q=0}^{p-1}\frac{B_{p,q}}{2^{p+q}}
 \left(\frac{p+q}{2}+p+1-q\right).                    \label{eq:ballotsum}\end{aligned}$$ The first parenthesis is elapsed mean time; the second also includes the one-clock residual time after the lower path reaches zero.

We now evaluate both finite sums. Let $\xi_k=1$ when the $k$th two-clock event moves the lower path and $\xi_k=-1$ when it moves the upper path, and put $$U_k=\#\{\ell\leq k:\xi_\ell=1\},\qquad
 D_k=1+\sum_{\ell=1}^k\xi_\ell,
 \qquad
 K=\inf\{k\geq0:D_k=0\text{ or }U_k=p\}.$$ Up to $K$, $D_k$ is the gap between the paths. At meeting, $K=2j+1$ for some $0\leq j<p$; on root exit, $K=p+q$ for some $0\leq q<p$ and $D_K=p+1-q$. Hence $K\leq2p-1$.

Set $$t_r=4^{-r}\binom{2r}{r}\qquad(r\geq0).$$ The $j$th meeting summand satisfies $$\frac{A_j}{2^{2j+1}}\frac{2j+1}{2}=\frac{t_{j+1}}2.$$ Moreover, $$(2r+1)t_r-(2r-1)t_{r-1}=t_r\qquad(r\geq1),$$ so telescoping, with $t_0=1$, gives the meeting contribution $$S_1=\frac12\sum_{r=1}^{p}t_r
    =\frac{(2p+1)t_p-1}{2}.                            \label{eq:Sone}$$

For the root alternative define $$P_{p,q}=\frac{B_{p,q}}{2^{p+q}},\qquad
 F_q=\frac1{2^{p+q}}\binom{p+q}{q},\qquad F_{-1}=0.$$ Pascal's identity now has the explicit telescoping form $$P_{p,q}=F_q-F_{q-1},\qquad 0\leq q<p.                \label{eq:Ptel}$$ Consequently $$\mathbb P(\text{root exit})=F_{p-1}
 =\frac1{2^{2p-1}}\binom{2p-1}{p-1}=t_p.              \label{eq:rootprob}$$ The fair walk $(D_k)$ is a martingale and $K$ is bounded, so optional stopping gives $\mathbb ED_K=D_0=1$. Since $D_K=0$ at meeting and $D_K=p+1-q$ on root exit, $$\begin{aligned}
 \sum_{q=0}^{p-1}P_{p,q}(p+1-q)&=1,\notag\\
 \sum_{q=0}^{p-1}qP_{p,q}&=(p+1)t_p-1,\notag\\
 \mathbb E\!\left[K\mathbf 1_{\{\text{root exit}\}}\right]
   &=(2p+1)t_p-1.                                     \label{eq:rootmoment}\end{aligned}$$ The root contribution, including the one-clock residual time $D_K$, is therefore $$S_2=\frac12\mathbb E\!\left[K\mathbf 1_{\{\text{root exit}\}}\right]
       +\mathbb E\!\left[D_K\mathbf 1_{\{\text{root exit}\}}\right]
    =\frac{(2p+1)t_p+1}{2}.                            \label{eq:Stwo}$$ Combining [\[eq:Sone\]](#eq:Sone){reference-type="eqref" reference="eq:Sone"} and [\[eq:Stwo\]](#eq:Stwo){reference-type="eqref" reference="eq:Stwo"}, then using $2(p+1)t_{p+1}=(2p+1)t_p$, gives $$h(m-1,m)=(2p+1)t_p
 =2m t_m
 =\frac{2m}{4^m}\binom{2m}{m}
 =\frac{(2m-1)!!}{(2m-2)!!}.$$

Finally, if $W_{2m}=2X-2m$ with $X\sim\operatorname{Bin}(2m,1/2)$, then symmetry and $$(2k-2m)\binom{2m}{k}
 =2m\left\{\binom{2m-1}{k-1}-\binom{2m-1}{k}\right\}$$ give, by telescoping over $m<k\leq2m$, $$\mathbb E|W_{2m}|
 =\frac2{4^m}\sum_{k=m+1}^{2m}
   (2k-2m)\binom{2m}{k}
 =\frac{2m}{4^m}\binom{2m}{m}.$$

[\[thm:fullmean\]]{#thm:fullmean label="thm:fullmean"} For $n\geq1$, $$\boxed{\displaystyle
 \mathbb ET_n=\sum_{m=1}^{n-1}
 \frac{(2m-1)!!}{(2m-2)!!}.}                           \label{eq:fullmean}$$ As $n\to\infty$, $$\mathbb ET_n=\frac{4}{3\sqrt\pi}n^{3/2}+O(n^{1/2}).        \label{eq:asymptotic}$$

The consecutive interfaces of $S_n$ start at $(m-1,m)$ for $1\leq m<n$. Equations [\[eq:additivity\]](#eq:additivity){reference-type="eqref" reference="eq:additivity"} and [\[eq:adjacent\]](#eq:adjacent){reference-type="eqref" reference="eq:adjacent"} give [\[eq:fullmean\]](#eq:fullmean){reference-type="eqref" reference="eq:fullmean"}. The standard estimate $$\binom{2m}{m}=\frac{4^m}{\sqrt{\pi m}}
 \bigl(1+O(m^{-1})\bigr)$$ makes the $m$th summand $2\sqrt{m/\pi}+O(m^{-1/2})$. Summing and comparing $\sum_{m<n}\sqrt m$ with its integral gives [\[eq:asymptotic\]](#eq:asymptotic){reference-type="eqref" reference="eq:asymptotic"}.

# Exact control and scope {#sec:control}

The paper-local verifier constructs [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} literally and uses integer arithmetic and `fractions.Fraction` only. It compares the Bellman expectation with the independent interface sum for every rooted subset through $n=14$ (16,383 states), audits every rooted hitting-time law through $n=11$ (2,047 states), checks the full pair recurrence triangle $0\leq a\leq b\leq80$, and evaluates the Catalan/ballot sum independently for $m\leq80$. It also checks the full-start law and [\[cor:minmass\]](#cor:minmass){reference-type="ref" reference="cor:minmass"}. The deterministic run executes 506,663 assertions and its stdout is frozen byte for byte. These finite controls expose boundary, scheduler, and indexing errors; they are not substitutes for the proofs.

One additional upper-endpoint pattern is retained in the program under the literal label `PILOT_ONLY`. It is not a theorem, does not appear in the abstract or contribution list, and supplies no promotion credit.

The scope is deliberately narrow. The state is a set, the root never rings, every positive pile has the same active rate, and motion is deterministically one edge toward zero. Retaining mass labels, assigning clocks permanently to original particles, sampling geometric sites with lazy holds, using unbiased motion, or replacing the path by a tree changes the process. No claim here transfers to those variants.

# Conclusion {#sec:conclusion}

The active-pile chain has an exact arbitrary-state statistic: its expected number of embedded updates is the sum of the meeting-time means of consecutive initial interfaces. The site-clock construction proves scheduler equivalence, while the compensator converts elapsed interface lifetimes back to the discrete update count. A ballot calculation then yields the double-factorial full-start mean and its $n^{3/2}$ scale. The finite PGF and support theorem provide a second description of the hitting law.

The result is path-specific and does not assert independent interfaces. Generic coalescing-walk and first-passage methods have been subtracted, and the source search remains bounded. Accordingly, novelty, priority, posting, submission, and external release remain on hold.
