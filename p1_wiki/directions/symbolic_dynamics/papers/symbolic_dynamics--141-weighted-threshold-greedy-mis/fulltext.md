---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--141-weighted-threshold-greedy-mis"
canonical_tex: "symbolic_dynamics/papers/141-weighted-threshold-greedy-mis/main.tex"
canonical_pdf: "symbolic_dynamics/papers/141-weighted-threshold-greedy-mis/main.pdf"
source_sha256: "b312ca8becfcc405de8276195058b9876c8631ae0119b882a5bf4973db2d7f6e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Weighted Reverse-Stick Laws for Random Greedy Independent Sets on Threshold Graphs

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/141-weighted-threshold-greedy-mis>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/141-weighted-threshold-greedy-mis/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/141-weighted-threshold-greedy-mis/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/141-weighted-threshold-greedy-mis/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/141-weighted-threshold-greedy-mis/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The support of maximal independent sets of a threshold graph and the generic random-greedy independent-set process are both known. Assigning those facts zero credit, we compute the endpoint law when vertices have arbitrary fixed positive exponential rates. In creation order, dominant vertices contribute reverse hazards $h_d=w_d/W_d$, and the endpoint masses form a reverse stick-breaking distribution. The terminal law recovers every $h_d$ and gives an explicit bijection between hazard vectors and the open simplex on the known support, while leaving the original vertex rates nonidentifiable. We derive the accepted-update size PGF, all vertex marginals, and nested inclusion laws for zero vertices. Finally, we separate full-order inspections, accepted updates, priority-label span, and continuous elapsed completion time; only the last obeys a state-dependent Laplace recursion.
author:
- Anonymous
bibliography:
- references.bib
title: 'Weighted Reverse-Stick Laws for Random Greedy Independent Sets on Threshold Graphs'
```

## Markdown 正文

# Ownership, carrier, and process

Random sequential adsorption on graphs is an established process [@pippenger1989], and random-order greedy maximal independent sets have a large modern theory [@krivelevichetal2024]. Threshold graphs and the facets of their independent-set complexes are also known [@klivans2007]. Accordingly, this note claims no credit for the greedy algorithm, its maximality, or the possible endpoint sets. Its narrow residual is the positive-rate endpoint distribution and the inverse and marginal consequences of that distribution.

Let $v_1,\ldots,v_n$ be a threshold-graph creation order. Set $b_1=0$; for $i>1$, a creation bit $b_i=0$ makes $v_i$ isolated from all earlier vertices, whereas $b_i=1$ makes $v_i$ adjacent to every earlier vertex. Equivalently, for $i<j$, $$\label{eq:adjacency}
 v_i\sim v_j\quad\Longleftrightarrow\quad b_j=1.$$ Write $$Z=\{i:b_i=0\},\qquad D=\{i:b_i=1\}.$$

Give $v_i$ a fixed rate $w_i>0$ and an independent priority $X_i\sim\operatorname{Exp}(w_i)$. Scan vertices in increasing priority and accept a vertex if no previously accepted neighbor blocks it. Equivalently, among the active vertices accept the first clock and delete its closed active neighborhood, then continue. The induced weighted order is the classical Plackett model [@plackett1975]; that order and its exponential realization receive zero credit here. Let $I$ be the final independent set and $$\label{eq:prefix}
 W_j=\sum_{i=1}^j w_i.$$

# Owned support

The following is the threshold-graph maximal-independent-set support stated by @klivans2007. We include the one-line proof only to fix labels; it is not a contribution of this note.

[\[prop:support\]]{#prop:support label="prop:support"} The maximal independent sets are exactly $$\label{eq:support}
 S_Z=Z,\qquad
 S_d=\{d\}\cup\{i>d:b_i=0\},\quad d\in D.$$

Two dominant-creation vertices are adjacent. If a maximal independent set contains $d\in D$, it contains no earlier vertex and must contain every later zero vertex; these vertices form $S_d$, while every omitted vertex is adjacent to $d$ or to a later dominant vertex. If it contains no dominant vertex, maximality forces every zero vertex, giving $S_Z$; since $1\in Z$, every dominant vertex has an earlier neighbor in $S_Z$.

# Weighted endpoint law and inverse problem

For $d\in D$ define the dominant prefix hazard $$\label{eq:hazard}
 h_d=\frac{w_d}{W_d}\in(0,1).$$

[\[thm:stick\]]{#thm:stick label="thm:stick"} For every positive rate vector, $$\begin{aligned}
 p_d:=\Pr(I=S_d)
 &=h_d\prod_{\substack{j\in D\\j>d}}(1-h_j)
 =\frac{w_d}{W_d}\prod_{\substack{j\in D\\j>d}}
       \frac{W_{j-1}}{W_j},                       \label{eq:pd}\\
 p_Z:=\Pr(I=S_Z)
 &=\prod_{j\in D}(1-h_j)
 =\prod_{j\in D}\frac{W_{j-1}}{W_j}.             \label{eq:pz}\end{aligned}$$ These masses are positive and sum to one.

Read the creation string from the right. If $b_n=0$, then $v_n$ is isolated from the prefix and is always accepted; deleting it from the description leaves the prefix endpoint law unchanged. If $b_n=1$, then $v_n$ is universal. It has the smallest priority among $v_1,\ldots,v_n$ with probability $w_n/W_n=h_n$, in which case $I=\{n\}=S_n$. Otherwise the first prefix vertex is accepted and deletes $v_n$. Conditional on this event, its identity has probability $w_i/W_{n-1}$, and memorylessness leaves precisely the weighted greedy law on the prefix. Thus a terminal dominant bit takes an $h_n$ atom and multiplies every prefix atom by $1-h_n$; a terminal zero bit only appends that zero. Iterating gives [\[eq:pd\]](#eq:pd){reference-type="eqref" reference="eq:pd"}--[\[eq:pz\]](#eq:pz){reference-type="eqref" reference="eq:pz"}. The same recursion proves positivity and normalization.

The endpoint law does more than evaluate forward probabilities: it identifies exactly the hazard coordinates that it can observe.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} From the labelled endpoint masses one recovers every dominant hazard by $$\label{eq:inverse}
 h_d=\frac{p_d}{p_Z+\displaystyle\sum_{\substack{e\in D\\e\leq d}}p_e},
 \qquad d\in D.$$ Consequently, the map from $(h_d)_{d\in D}\in(0,1)^{|D|}$ to the masses in [\[eq:pd\]](#eq:pd){reference-type="eqref" reference="eq:pd"}--[\[eq:pz\]](#eq:pz){reference-type="eqref" reference="eq:pz"} is a bijection onto the open probability simplex on the $|D|+1$ sets in [\[eq:support\]](#eq:support){reference-type="eqref" reference="eq:support"}. Every such mass vector is realized by positive vertex rates.

Order $D$ increasingly. Reverse-stick telescoping gives $$\label{eq:survival}
 p_Z+\sum_{\substack{e\in D\\e\leq d}}p_e
 =\prod_{\substack{j\in D\\j>d}}(1-h_j).$$ Dividing [\[eq:pd\]](#eq:pd){reference-type="eqref" reference="eq:pd"} by [\[eq:survival\]](#eq:survival){reference-type="eqref" reference="eq:survival"} proves [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} and injectivity.

Conversely, start with strictly positive masses summing to one and define $h_d$ by [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}. Its denominator strictly exceeds $p_d$, so $0<h_d<1$. Reversing the telescoping calculation recovers every prescribed mass, proving surjectivity at the hazard level. To realize the hazards by rates, choose arbitrary positive rates at zero positions. Moving from left to right, when $d\in D$ set $$\label{eq:realize}
 w_d=\frac{h_d}{1-h_d}W_{d-1}.$$ Since $b_1=0$, $W_{d-1}>0$; equation [\[eq:realize\]](#eq:realize){reference-type="eqref" reference="eq:realize"} is positive and makes $w_d/W_d=h_d$.

[\[rem:nonid\]]{#rem:nonid label="rem:nonid"} The terminal law identifies the hazard vector, not the original rate vector. All positive rate vectors satisfying $w_d/W_d=h_d$ at dominant positions are observationally equivalent. Global rescaling is always invisible. More strongly, the construction in [\[eq:realize\]](#eq:realize){reference-type="eqref" reference="eq:realize"} permits arbitrary positive choices at every zero position and then adjusts later dominant rates. Zero rates after the last dominant position do not enter any hazard at all. Thus the simplex theorem is not a vertex-rate identifiability theorem.

# Accepted-size PGF and inclusion laws

Let $K$ be the number of accepted active-set updates. Since every update adds one vertex, $K=|I|$. For $d\in D$ put $$\label{eq:kd}
 k_d=1+|\{i>d:b_i=0\}|.$$

[\[thm:pgf\]]{#thm:pgf label="thm:pgf"} The complete PGF of $K$ is $$\label{eq:pgf}
 \mathbb E z^K=p_Zz^{|Z|}+\sum_{d\in D}p_dz^{k_d}.$$ If distinct dominant positions give the same $k_d$, their masses are added at that coefficient. In particular, $$\begin{aligned}
 \mathbb EK&=p_Z|Z|+\sum_{d\in D}p_dk_d,\label{eq:meanK}\\
 \operatorname{Var}(K)&=p_Z|Z|^2+\sum_{d\in D}p_dk_d^2-(\mathbb EK)^2.
 \label{eq:varK}\end{aligned}$$

Proposition [\[prop:support\]](#prop:support){reference-type="ref" reference="prop:support"} gives $|S_Z|=|Z|$ and $|S_d|=k_d$. Mixing these deterministic sizes with Theorem [\[thm:stick\]](#thm:stick){reference-type="ref" reference="thm:stick"} proves [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}; differentiation at $z=1$ proves the moment formulas.

[\[cor:marginal\]]{#cor:marginal label="cor:marginal"} For a dominant vertex $d\in D$ and a zero vertex $i\in Z$, $$\begin{aligned}
 \Pr(d\in I)&=p_d,                                      \label{eq:dom-marginal}\\
 \Pr(i\in I)&=\prod_{\substack{j\in D\\j>i}}(1-h_j).
                                                               \label{eq:zero-marginal}\end{aligned}$$ If $i,k\in Z$ and $i<k$, then $$\label{eq:nesting}
 \{i\in I\}\subseteq\{k\in I\},\qquad
 \Pr(i,k\in I)=\Pr(i\in I).$$

Among the support sets, only $S_d$ contains dominant vertex $d$, proving [\[eq:dom-marginal\]](#eq:dom-marginal){reference-type="eqref" reference="eq:dom-marginal"}. A zero vertex $i$ is present precisely when no later dominant vertex supplies the endpoint. Summing $p_Z$ and the $p_d$ for $d<i$ or, equivalently, using [\[eq:survival\]](#eq:survival){reference-type="eqref" reference="eq:survival"}, gives [\[eq:zero-marginal\]](#eq:zero-marginal){reference-type="eqref" reference="eq:zero-marginal"}. Every support set containing an earlier zero $i$ also contains every later zero $k$, which proves [\[eq:nesting\]](#eq:nesting){reference-type="eqref" reference="eq:nesting"}.

# Four count and clock objects

The reverse-stick formula does not turn every implementation statistic into the same random variable. Under the fixed priorities $X_i$ define $$J=n,\qquad K=|I|,\qquad
 R=\max_iX_i-\min_iX_i,\qquad
 \tau=\max_{v_i\in I}X_i.$$ Here $J$ is the number of inspections in an implementation that scans the entire priority order; $K$ is the number of accepted active-set updates and is governed by [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}; $R$ is the numerical span of all priority labels; and $\tau$ is the continuous time at which the active set becomes empty. The last equality for $\tau$ follows in the one-shot priority coupling because the last accepted clock deletes the last active vertices. Neither $R$ nor $\tau$ is a discrete step count.

For an active vertex set $A$, let $\mathcal N_A[v]$ be the closed neighborhood of $v$ within $A$, and set $L_A(s)=\mathbb E_Ae^{-s\tau}$. Exponential races give the valid recursion $$\label{eq:ct}
 L_\varnothing(s)=1,\qquad
 L_A(s)=\frac{\displaystyle\sum_{v\in A}w_v
 L_{A\setminus\mathcal N_A[v]}(s)}
 {s+\displaystyle\sum_{v\in A}w_v},\qquad s\geq0.$$ Indeed, the first holding time is exponential with the denominator's total rate, its winner has probability proportional to $w_v$, and memorylessness restarts the residual active set. Formula [\[eq:ct\]](#eq:ct){reference-type="eqref" reference="eq:ct"} is state dependent; it is not obtained by substituting a Laplace variable into [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}.

For a two-vertex clique with rates $1$ and $2$, the separation is already literal: $J=2$, $K=1$, and at $s=1$ $$\label{eq:firewall}
 \mathbb Ee^{-\tau}=\frac34,\qquad
 \mathbb Ee^{-R}=\frac13\frac23+\frac23\frac12=\frac59,
 \qquad \mathbb E(1/2)^K=\frac12.$$ The numerical comparison is only a vocabulary firewall; the three transforms belong to different statistics.

# Exact controls and scope

The paper-local program independently enumerates the literal active-set chain and uses rational arithmetic only. It compares the resulting endpoint law with Theorem [\[thm:stick\]](#thm:stick){reference-type="ref" reference="thm:stick"}, then checks inversion, size PGFs, every marginal, and every ordered pair of zero vertices. A separate lane realizes prescribed positive simplex masses, and another enumerates full weighted permutations to check [\[eq:ct\]](#eq:ct){reference-type="eqref" reference="eq:ct"} through size six.

::: {#tab:controls}
  control lane                           inputs or checked cells
  ------------------------------------ -------------------------
  parameter-labelled endpoint inputs                  $31{,}833$
  endpoint cells                                     $114{,}890$
  accepted-size PGF cells                             $65{,}404$
  simplex realizations                                 $1{,}023$
  continuous-time transform inputs                         $567$
  exact assertions                                   $750{,}181$

  : Exact-arithmetic falsification envelope.
:::

The main endpoint grid contains every creation string through $n=6$ and all weights in $\{1,2,3\}^n$, plus every creation string through $n=10$ under four fixed uniform and nonuniform profiles. Finite controls do not prove arbitrary positive-real-rate claims and provide no novelty evidence.

Klivans's support, the generic RSA/MIS process, weighted orders, and exponential races remain fully owned. The defensible internal residual is only Theorems [\[thm:stick\]](#thm:stick){reference-type="ref" reference="thm:stick"}--[\[thm:pgf\]](#thm:pgf){reference-type="ref" reference="thm:pgf"} and Corollary [\[cor:marginal\]](#cor:marginal){reference-type="ref" reference="cor:marginal"}. Because the right-to-left proof is short and may be unpublished folklore, external circulation remains on hold pending a deeper specialist owner search.
