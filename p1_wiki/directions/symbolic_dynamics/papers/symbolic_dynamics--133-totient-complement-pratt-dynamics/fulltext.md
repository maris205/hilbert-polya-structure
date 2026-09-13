---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--133-totient-complement-pratt-dynamics"
canonical_tex: "symbolic_dynamics/papers/133-totient-complement-pratt-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/133-totient-complement-pratt-dynamics/main.pdf"
source_sha256: "3f62efbd5a23a5a0a811e92f4f975ba643cd4262b958c6c6ab0804920f602835"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Source Phases and Target Fibres for Totient--Complement Dynamics on Squarefree Divisors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/133-totient-complement-pratt-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/133-totient-complement-pratt-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/133-totient-complement-pratt-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/133-totient-complement-pratt-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/133-totient-complement-pratt-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a nonempty finite prime set $P$, put $n=\prod_{p\in P}p$ and iterate $F_n(d)=\gcd(n,(n/d)\varphi(d))$ on the divisors of $n$. We give three exact all-parameter descriptions of this finite arithmetic dynamics. Its squarefree support is the signed Boolean map $S\mapsto(P\setminus S)\cup N(S)$ on the induced prime-chain directed acyclic graph. If $s$ vertices have no incoming edge, an explicit topological decoder extends arbitrary phases on those vertices to every recurrent state. Consequently there are no fixed states, there are exactly $2^s$ recurrent states, and they form $2^{s-1}$ two-cycles. A two-step erasure identity shows that every orbit reaches recurrence by time at most $h+1$, where $h$ is the longest directed-path length; this bound is not claimed sharp. Finally, inclusion--exclusion gives a closed formula for the one-step fibre over every target divisor, including targets outside the image. Prime-chain geometry, signed-Boolean formalism, topological propagation, and inclusion--exclusion are treated as owned background. The residual contribution is their complete conjunction for the displayed literal map. Exact finite checks are falsification controls only, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Source Phases and Target Fibres for Totient--Complement Dynamics on Squarefree Divisors'
```

## Markdown 正文

# The literal map and the theorem

Let $P$ be a nonempty finite set of primes and $n=\prod_{p\in P}p$. Every divisor of $n$ is squarefree, so we identify $d\mid n$ with $S=\operatorname{supp}(d)\subseteq P$. Put a directed edge $$\label{eq:edge}
                         q\longrightarrow p\quad\Longleftrightarrow\quad p\mid q-1.$$ The edge strictly decreases the prime and hence defines a directed acyclic graph. Write $$\operatorname{Par}(p)=\{q\in P:q\to p\},\qquad
 \operatorname{Par}(U)=\bigcup_{p\in U}\operatorname{Par}(p),$$ and call $p$ a *source* when $\operatorname{Par}(p)=\varnothing$. Thus "source" means no incoming edge under the orientation [\[eq:edge\]](#eq:edge){reference-type="eqref" reference="eq:edge"}. Let $s=|\operatorname{Src}|$, and let $$\delta(p)=\max\{\text{length of a directed path from a source to }p\},
 \qquad h=\max_{p\in P}\delta(p).$$ Every vertex is reached from a source because the graph is finite. Prime chains and their heights are classical objects; we use that geometry as background and make no contribution claim for it [@FordKonyaginLuca2010].

For $S\subseteq P$, set $$N(S)=\{p\in P:\text{some }q\in S\text{ satisfies }q\to p\}.$$ The complete result is as follows. Entry time means the least $t$ for which the state at time $t$ is recurrent.

[\[thm:main\]]{#thm:main label="thm:main"} For $$F_n(d)=\gcd\!\left(n,\frac nd\varphi(d)\right),\qquad d\mid n,$$ the following statements hold.

1.  Under squarefree support, $F_n$ is conjugate to $$\label{eq:support-map}
                            F(S)=(P\setminus S)\cup N(S).$$

2.  The recurrent set has $2^s$ states, no state is fixed, and there are exactly $2^{s-1}$ cycles, all of exact period two. The two phases are explicitly decoded from arbitrary source bits by [\[eq:source-phase\]](#eq:source-phase){reference-type="eqref" reference="eq:source-phase"} and [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"} below.

3.  Every orbit has entry time at most $h+1$.

4.  For every target support $B\subseteq P$, with $Z=P\setminus B$, $$\label{eq:fibre-main}
     |F^{-1}(B)|=
     \sum_{\substack{T\subseteq B\\
     (Z\cup T)\cap\operatorname{Par}(Z\cup T)=\varnothing}}
     (-1)^{|T|}
     2^{|P|-|Z\cup T|-|\operatorname{Par}(Z\cup T)|}.$$ The formula is valid also when $B$ is outside the image, in which case its value is zero.

# Support conjugacy and complemented coordinates

[\[prop:conjugacy\]]{#prop:conjugacy label="prop:conjugacy"} The literal divisor update has support [\[eq:support-map\]](#eq:support-map){reference-type="eqref" reference="eq:support-map"}.

Fix $p\in P$. Since $n$ is squarefree, membership of $p$ in the support of $F_n(d)$ is equivalent to divisibility of $(n/d)\varphi(d)$ by $p$. If $p\notin S$, then $p\mid n/d$. If $p\in S$, then $p\nmid n/d$, while Euler's product formula gives $$\varphi(d)=\prod_{q\in S}(q-1).$$ Thus $p\mid\varphi(d)$ exactly when $p\mid q-1$ for some $q\in S$; the choice $q=p$ never contributes. This is precisely membership in $(P\setminus S)\cup N(S)$, prime by prime.

Let $x_p=\mathbf1_{p\in S}$ and pass to complemented bits $y_p=1-x_p$. Proposition [\[prop:conjugacy\]](#prop:conjugacy){reference-type="ref" reference="prop:conjugacy"} is exactly $$\label{eq:y-rule}
 y_p(t+1)=(1-y_p(t))A_p(t),\qquad
 A_p(t)=\prod_{q\in\operatorname{Par}(p)}y_q(t),$$ where the empty product is one. This is an AND--NOT rule on a signed wiring diagram. General AND--NOT and signed-Boolean frameworks, including their graph reductions, are established background [@VelizCubaEtAl2012; @AracenaCabreraCrotSalinas2021]. One immediate identity will drive both the decoder and the transient bound: $$\label{eq:consecutive-zero}
                              y_p(t)y_p(t+1)=0.$$

# Source phases and complete recurrence

At a source, [\[eq:y-rule\]](#eq:y-rule){reference-type="eqref" reference="eq:y-rule"} is toggling. Assign an arbitrary bit $\eta_r\in\{0,1\}$ to each $r\in\operatorname{Src}$ and set $$\label{eq:source-phase}
                          y_r^0=\eta_r,\qquad y_r^1=1-\eta_r.$$ Process the nonsources in any order in which every parent precedes its child. Once the parent phases of $p$ have been assigned, define $$\label{eq:decoder}
 A_p^\epsilon=\prod_{q\in\operatorname{Par}(p)}y_q^\epsilon,\qquad
                         y_p^0=A_p^1,\quad y_p^1=A_p^0.$$

[\[lem:phase\]]{#lem:phase label="lem:phase"} For a nonsource $p$, suppose every parent phase pair obeys $y_q^0y_q^1=0$. Then $A_p^0A_p^1=0$, and [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"} is the unique pair satisfying the two phase equations induced by [\[eq:y-rule\]](#eq:y-rule){reference-type="eqref" reference="eq:y-rule"}.

Because $\operatorname{Par}(p)$ is nonempty, any one parent gives $A_p^0A_p^1=0$. The phase equations are $$y_p^1=(1-y_p^0)A_p^0,\qquad
 y_p^0=(1-y_p^1)A_p^1.$$ If both $A$'s vanish, they force $(y_p^0,y_p^1)=(0,0)$. If $(A_p^0,A_p^1)=(1,0)$, the second equation first forces $y_p^0=0$ and the first then forces $y_p^1=1$; the remaining case is symmetric. These three possibilities give exactly [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"}. They also show $y_p^0y_p^1=0$, closing the topological induction.

The decoder therefore produces a genuine two-phase orbit from each source assignment and is injective because it retains that assignment on the sources. Completeness will follow from a global entry estimate.

[\[lem:erasure\]]{#lem:erasure label="lem:erasure"} If $p$ is not a source, then for every $t\geq0$, $$\label{eq:erasure}
                               y_p(t+2)=A_p(t+1).$$

By [\[eq:consecutive-zero\]](#eq:consecutive-zero){reference-type="eqref" reference="eq:consecutive-zero"} and nonemptiness of $\operatorname{Par}(p)$, $A_p(t)A_p(t+1)=0$. Applying [\[eq:y-rule\]](#eq:y-rule){reference-type="eqref" reference="eq:y-rule"} twice gives $$y_p(t+2)=A_p(t+1)\bigl(1-A_p(t)(1-y_p(t))\bigr)=A_p(t+1).$$

[\[prop:entry\]]{#prop:entry label="prop:entry"} Each coordinate $p$ is two-periodic from time $\delta(p)+1$ onward. Consequently every orbit enters recurrence by time at most $h+1$.

Sources toggle from time zero, so the asserted weaker starting time one is valid. Let $p$ be a nonsource and assume the claim for all its parents. For $t\geq\delta(p)+1$ we have $t\geq2$, and Lemma [\[lem:erasure\]](#lem:erasure){reference-type="ref" reference="lem:erasure"} applied at $t$ and at $t-2$ gives $$y_p(t+2)=\prod_{q\in\operatorname{Par}(p)}y_q(t+1),\qquad
 y_p(t)=\prod_{q\in\operatorname{Par}(p)}y_q(t-1).$$ Now $t-1\geq\delta(p)=1+\max_{q\in\operatorname{Par}(p)}\delta(q)$. Every parent is therefore already two-periodic at time $t-1$, so the products agree. This proves the coordinate claim by induction. At time $h+1$ all coordinates are two-periodic, hence the whole state is on a cycle of length dividing two.

Every periodic orbit thus has period at most two. No state can be fixed, because every finite nonempty directed acyclic graph has a source and every source coordinate toggles. Hence every periodic orbit has exact period two. Viewed at either phase, it satisfies the equations of Lemma [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"}; topological uniqueness shows that it is the decoder output for its source bits. There are consequently $2^s$ recurrent states and $2^{s-1}$ cycles. This proves Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(ii)--(iii). The estimate $h+1$ is deliberately only an upper bound. It includes the singleton case $h=0$ and applies componentwise to disconnected graphs.

# The fibre over every target

Return to the support bits $x_p$. From [\[eq:support-map\]](#eq:support-map){reference-type="eqref" reference="eq:support-map"}, a target zero at $p$ occurs exactly on the event $$\label{eq:event}
 E_p=\{x_p=1\text{ and }x_q=0\text{ for every }q\in\operatorname{Par}(p)\}.$$ Fix $B\subseteq P$ and $Z=P\setminus B$. The constraints at the target zeros require every event $E_p$ with $p\in Z$, while target ones require that none of the events $E_p$ with $p\in B$ occur. Inclusion--exclusion over the latter events yields the sum over $T\subseteq B$ of $(-1)^{|T|}$ times the number of assignments satisfying all $E_p$ for $p\in Z\cup T$.

For $U=Z\cup T$, this intersection forces every bit in $U$ to one and every bit in $\operatorname{Par}(U)$ to zero. It is empty if $U\cap\operatorname{Par}(U)\ne\varnothing$. When those sets are disjoint, precisely $|P|-|U|-|\operatorname{Par}(U)|$ bits remain free, so there are $2^{|P|-|U|-|\operatorname{Par}(U)|}$ assignments. Substitution gives [\[eq:fibre-main\]](#eq:fibre-main){reference-type="eqref" reference="eq:fibre-main"}. This derivation imposes no image hypothesis on $B$; if the fibre is empty, inclusion--exclusion returns zero. It completes Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# Exact controls and contribution boundary

The paper-local verifier independently evaluates the literal integer map, the support rule, both decoder phases, the entry bound, and [\[eq:fibre-main\]](#eq:fibre-main){reference-type="eqref" reference="eq:fibre-main"} for every state and every target in four boxes. It uses Python integers, no floating point, and no sampling.

::: {#tab:control}
  case              $|P|$   $s$   states   recurrent   max tail   image
  --------------- ------- ----- -------- ----------- ---------- -------
  singleton             1     1        2           2          0       2
  chain5                5     1       32           2          3       8
  mixed6                6     2       64           4          4      17
  disconnected7         7     4      128          16          2      25

  : Exact falsification controls: 226 states, all 226 targets, and 4,774 assertions. The table is not a proof of an unbounded claim.
:::

The arithmetic factorization in Proposition [\[prop:conjugacy\]](#prop:conjugacy){reference-type="ref" reference="prop:conjugacy"}, Euler's totient product, prime-chain/Pratt geometry, AND--NOT representation, generic propagation on a directed acyclic graph, inclusion--exclusion as a method, and finite-map cycle conversion all receive zero contribution credit. Internally, the carrier and update are distinct from P84's unitary Cayley system, P97's sumset squaring, P100's valuation absorber, P107's arithmetic carrier, P128's translation--gcd polynomial erosion, and P131's Euclidean quotient queue. The residual theorem is the conjunction, for the literal displayed arithmetic map, of the complete phase decoder, the nonsharp entry bound, and the every-target fibre law. A bounded literature search did not identify an exact owner of that conjunction, but a search non-hit is not evidence of novelty or priority. Status remains `HOLD_EXTERNAL`.
