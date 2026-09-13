---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--192-first-collision-hurwitz"
canonical_tex: "symbolic_dynamics/papers/192-first-collision-hurwitz/main.tex"
canonical_pdf: "symbolic_dynamics/papers/192-first-collision-hurwitz/main.pdf"
source_sha256: "30cd2c9bc853d9b195f89527db4794681e4d3dcacd8c45f5aea0b49a98ab12f9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# First-Collision Hurwitz Dynamics on Minimal Cycle Factorizations: Sharp Tails, Fixed Census, and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/192-first-collision-hurwitz>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/192-first-collision-hurwitz/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/192-first-collision-hurwitz/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/192-first-collision-hurwitz/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/192-first-collision-hurwitz/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $\mathcal F_n$ be the minimal transposition factorizations of the long cycle $(1\,2\,\cdots\,n)$. At each epoch, find the first adjacent pair of transpositions having the same lower endpoint and apply the right Hurwitz move there; hold if no such pair exists. Although each local move is classical, this state-dependent scheduler creates a terminating finite map. We prove that successive update positions increase strictly, giving the sharp tail bound $n-2$. Via the classical lower-endpoint bijection with parking functions and Pollak's circular model, the fixed-state count is $(n-1)^{n-2}$. Independently, we classify every predecessor of every labelled target by one inverse Hurwitz test. The maximum one-step fibre is $n-1$, attained uniquely by the canonical adjacent-transposition factorization. Exact exhaustion through $n=8$ checks 280,392 states and reveals a stronger binomial law for complete scheduler histories; because an all-$n$ bijection is not yet proved, that law is stated only as a conjecture. Hurwitz actions, factorization--parking correspondences, and ordinary Prüfer enumerations receive zero contribution credit. The owner gate is `OWNER_RED_AMBER/HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'First-Collision Hurwitz Dynamics on Minimal Cycle Factorizations: Sharp Tails, Fixed Census, and Exact Fibres'
```

## Markdown 正文

# Convention, map, and subtraction

Fix $n\ge2$ throughout. Permutations compose in the standard order: in $\sigma\rho$, the permutation $\rho$ acts first. Put $c_n=(1\,2\,\cdots\,n)$ and $$\label{eq:carrier}
 \mathcal F_n=\{(\tau_1,\ldots,\tau_{n-1}):
 \tau_i\text{ is a transposition and }\tau_1\cdots\tau_{n-1}=c_n\}.$$ For a transposition $(a,b)$ written with $a<b$, set $\ell((a,b))=a$. The right Hurwitz move at $i$ is $$\label{eq:hurwitz}
 H_i(\ldots,\tau_i,\tau_{i+1},\ldots)
 =(\ldots,\tau_{i+1},\tau_{i+1}\tau_i\tau_{i+1},\ldots).$$ It preserves the product.

Define $T_n:\mathcal F_n\to\mathcal F_n$ by choosing the least $i\in\{1,\ldots,n-2\}$ with $$\label{eq:collision}
 \ell(\tau_i)=\ell(\tau_{i+1})$$ and applying $H_i$; if no such $i$ exists, fix the state. The product, Hurwitz orientation, numeric endpoint order, and least-index convention are part of the definition. Reversing only the long-cycle orientation does not preserve the dynamics.

Minimal long-cycle factorizations, their Cayley-tree count, and Hurwitz actions are classical [@Denes1959; @GorskyGorsky2013]. The lower-endpoint map $$\label{eq:parking-map}
 (\tau_1,\ldots,\tau_{n-1})\longmapsto
 (\ell(\tau_1),\ldots,\ell(\tau_{n-1}))$$ is the classical bijection from $\mathcal F_n$ to parking functions of length $n-1$ [@Stanley1997; @IrvingRattan2021]. All of this receives zero contribution credit. The residual claims concern the adaptive first-collision scheduler and its target-resolved inverse graph.

Campion Loth and Rattan give a deterministic bijection built from ordered strings of conditional Hurwitz moves in their study of star and monotone factorizations [@CampionLothRattan2025]; in particular, equality of lower endpoints appears in one case of their local construction. That conditional Hurwitz-string machinery also receives zero contribution credit here. Its move convention, monotone/string order-change scheduler, reversible-bijection objective, and theorem output differ from the present repeated map, which always selects the first adjacent lower-endpoint collision and studies its tails and target-resolved fibres. This distinction is an exact object separation, not a novelty claim.

Internally, direct Hurwitz actions have repeatedly been owner-killed, and P181 uses first-descent prefix reversal on ordinary permutations. The present map is not a braid-group orbit census, a $0$-Hecke action, or a prefix reversal. Indeed its conditional local operators fail the braid relation already on $((1,4),(1,3),(1,2))$. A bounded owner search found the classical ingredients above but no literal scheduler theorem package. This non-hit is not evidence of novelty, priority, completeness, or freedom to operate.

# Strictly advancing collisions

For $f\in\mathcal F_n$, let $i_1,i_2,\ldots$ be its successive update positions.

[\[thm:tail\]]{#thm:tail label="thm:tail"} Every nonempty update history is strictly increasing: $$\label{eq:increasing-history}
                  1\le i_1<i_2<\cdots\le n-2.$$ Consequently every recurrent state is fixed and every tail is at most $n-2$. For $n\ge3$ the bound is sharp; one witness is $$\label{eq:deep-witness}
 ((1,n),(1,2),(2,3),\ldots,(n-2,n-1)),$$ whose history is $1,2,\ldots,n-2$ and whose terminal state is $((1,2),(2,3),\ldots,(n-1,n))$. For $n=2$, the sole factorization $((1,2))$ is fixed, so the same sharp bound equals zero.

At an active position write $\tau_i=(a,b)$ and $\tau_{i+1}=(a,c)$, where $a<b,c$. The two transpositions are distinct: otherwise they cancel and the $n$-cycle would be expressed using fewer than $n-1$ transpositions. The update replaces them by $$\label{eq:local-update}
                   (a,c),(b,c).$$ The new lower endpoints at positions $i,i+1$ are $a,\min(b,c)$, and the second is strictly larger than $a$. All earlier lower endpoints are unchanged, including the endpoint at position $i$. Since $i$ was the first old equality, no equality is created before $i$ and the equality at $i$ disappears. The next update position is therefore strictly larger. This proves [\[eq:increasing-history\]](#eq:increasing-history){reference-type="eqref" reference="eq:increasing-history"}, termination, and the upper bound.

For $n\ge3$, the first move in [\[eq:deep-witness\]](#eq:deep-witness){reference-type="eqref" reference="eq:deep-witness"} changes the initial two factors to $(1,2),(2,n)$. The next collision is at position two. Inductively the factor $(j,n)$ meets $(j,j+1)$, and the Hurwitz move replaces them by $(j,j+1),(j+1,n)$. The stated history and terminal chain follow.

The proof supplies a pointwise certificate: the history is a subset of $[n-2]$ written in increasing order, and the depth is its cardinality.

# Exact fixed-state census

Put $N=n-1$. A parking function is a word $a\in[N]^N$ whose increasingly sorted entries $b_1\le\cdots\le b_N$ satisfy $b_i\le i$.

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} The fixed states of $T_n$ are exactly the factorizations whose lower-endpoint word has no equal adjacent letters, and $$\label{eq:fixed-count}
                  |\operatorname{Fix}(T_n)|=(n-1)^{n-2}.$$

The characterization is the stopping rule. Under [\[eq:parking-map\]](#eq:parking-map){reference-type="eqref" reference="eq:parking-map"}, it remains to count parking functions $a_1\cdots a_N$ with $a_i\ne a_{i+1}$ for $i<N$.

Use Pollak's circular parking model on $N+1$ spots [@Stanley2011EC2]. There are $(N+1)N^{N-1}$ circular preference words with adjacent entries unequal: choose the first preference freely and each later one in $N$ ways. Simultaneous translation modulo $N+1$ preserves the inequalities, every translation orbit has size $N+1$, and each orbit has exactly one representative that becomes an ordinary parking function after placing the empty spot at the end. Division by $N+1$ gives $N^{N-1}$, which is [\[eq:fixed-count\]](#eq:fixed-count){reference-type="eqref" reference="eq:fixed-count"}.

# Every-target inverse Hurwitz atlas

Fix a target $y=(\sigma_1,\ldots,\sigma_{n-1})$. Let $$\label{eq:first-target-collision}
 j(y)=\min\{j:\ell(\sigma_j)=\ell(\sigma_{j+1})\},$$ with sentinel value $j(y)=n-1$ when the set is empty. For $i<j(y)$, write $\sigma_i=(a,b)$ with $a<b$. Call $i$ reverse-admissible when $$\label{eq:admissible}
 \sigma_{i+1}=(b,c)\text{ for some }c>a,$$ where the transposition is unordered, so the condition means that it contains $b$ and its other endpoint exceeds $a$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Every target has exact indegree $$\label{eq:fibre}
 \operatorname{indeg}(y)=\mathbf1_{\{j(y)=n-1\}}
 +\#\{i<j(y):i\text{ is reverse-admissible}\}.$$ For each counted $i$, the unique nonself predecessor is $H_i^{-1}y$. Moreover, $$\label{eq:max-fibre}
 \max_{y\in\mathcal F_n}\operatorname{indeg}(y)=n-1,$$ and the unique maximizer is the canonical chain $$\label{eq:canonical}
                 ((1,2),(2,3),\ldots,(n-1,n)).$$ For $n=2$, this chain is the sole target and its self-fibre has indegree $1=n-1$.

Suppose a nonself source updates at $i$ to $y$. Positions before $i$ are unchanged, while the source equality at $i$ is removed, so necessarily $i<j(y)$. Inverting [\[eq:hurwitz\]](#eq:hurwitz){reference-type="eqref" reference="eq:hurwitz"} gives the pair $$\label{eq:inverse-pair}
 (\sigma_i\sigma_{i+1}\sigma_i,\sigma_i).$$ For its two lower endpoints to agree, $\sigma_{i+1}$ must contain the upper endpoint $b$ of $\sigma_i=(a,b)$, and its other endpoint $c$ must exceed $a$. The coincident-transposition case would cancel and is impossible. Thus [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"} is necessary. Conversely it turns [\[eq:inverse-pair\]](#eq:inverse-pair){reference-type="eqref" reference="eq:inverse-pair"} into $(a,c),(a,b)$; positions before $i$ retain no collision, so the scheduler selects exactly $i$. This proves the atlas and uniqueness of each inverse.

A fixed target contributes itself and at most one inverse at each of the $n-2$ positions; a nonfixed target contributes fewer. Hence $\operatorname{indeg}(y)\le n-1$. Every adjacent pair of [\[eq:canonical\]](#eq:canonical){reference-type="eqref" reference="eq:canonical"} is reverse-admissible, so it attains equality. Equality forces a fixed target with every position admissible. If $\sigma_i=(a_i,b_i)$, admissibility makes both endpoints of $\sigma_{i+1}$ exceed $a_i$, whence $a_{i+1}>a_i$. A strictly increasing parking function of length $n-1$ is necessarily $(1,2,\ldots,n-1)$, and the classical lower-endpoint bijection then forces the unique factorization [\[eq:canonical\]](#eq:canonical){reference-type="eqref" reference="eq:canonical"}.

Iterating [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} gives an exact finite reverse dynamic program for every higher fibre; no uniform closed form is asserted.

# A verified history law left open

The exact controls expose a stronger pattern. We isolate it to prevent finite evidence from silently becoming a theorem.

[\[conj:history\]]{#conj:history label="conj:history"} For every $I\subseteq[n-2]$, $$\label{eq:history-conjecture}
 \#\{f\in\mathcal F_n:\operatorname{Hist}(f)=I\}=(n-1)^{n-2-|I|}.$$ Equivalently, the number of states of exact depth $t$ would be $$\label{eq:depth-conjecture}
 \binom{n-2}{t}(n-1)^{n-2-t}.$$

The verifier proves [\[eq:history-conjecture\]](#eq:history-conjecture){reference-type="eqref" reference="eq:history-conjecture"} only for $2\le n\le8$ by exhaustion. A separate Cayley-tree stream also checks $n=9$. The histogram matches the occurrence-set law of a distinguished letter in a Prüfer word, but tested standard factorization--tree bijections do not identify the scheduler history with those positions. No all-$n$ bijection is presently known here. Accordingly [\[eq:history-conjecture\]](#eq:history-conjecture){reference-type="eqref" reference="eq:history-conjecture"}, the resulting unique deepest-state claim, and any derived basin formula receive no theorem status.

# Controls and limitations

The paper-local standard-library verifier generates the full Hurwitz orbit from [\[eq:canonical\]](#eq:canonical){reference-type="eqref" reference="eq:canonical"}, checks its Cayley cardinality and product, the lower-endpoint parking bijection, every orbit, every history mask through $n=8$, and every target fibre against [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. It also checks the orientation-sensitive convention: only the frozen product/order is covered. These computations are regression pressure, not proof or novelty evidence.

The paper does not claim a new Hurwitz action, conditional Hurwitz-string bijection, parking-function bijection, or tree code. It does not cover inverse-cycle conventions, other reflection groups, nonminimal factorizations, random schedulers, or the conjectural all-$n$ history law. External circulation remains unauthorized under `HOLD_EXTERNAL`.
