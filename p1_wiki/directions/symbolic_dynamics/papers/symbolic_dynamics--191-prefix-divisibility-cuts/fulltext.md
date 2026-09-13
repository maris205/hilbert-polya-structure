---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--191-prefix-divisibility-cuts"
canonical_tex: "symbolic_dynamics/papers/191-prefix-divisibility-cuts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/191-prefix-divisibility-cuts/main.pdf"
source_sha256: "bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Cut-Deletion Clocks and Exact Fibres for Prefix-Divisibility Dynamics on Compositions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/191-prefix-divisibility-cuts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/191-prefix-divisibility-cuts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/191-prefix-divisibility-cuts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/191-prefix-divisibility-cuts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/191-prefix-divisibility-cuts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a positive composition $a=(a_1,\ldots,a_k)$ of $N$, retain the internal cut at prefix $s_i=a_1+\cdots+a_i$ exactly when $a_i$ divides $s_i$, delete all other cuts simultaneously, and iterate the resulting coarsening. We determine both its temporal structure and its complete one-step inverse problem. Every recurrent composition is fixed, and fixed points are counted by an explicit divisor-step recurrence. The maximum tail is zero for $N\leq3$ and $N-3$ for $N\geq4$. Moreover, $(1,2,1^{N-3})$ is the unique deepest composition, and its complete orbit is $(1,2+t,1^{N-3-t})$. Independently, we encode a source as an increasing path through cut positions. For every labelled target, a no-skipped-target path recurrence gives its exact fibre; mandatory target cuts then factor this count into arithmetic interval factors. Positivity gives a complete image criterion, and the fibres sum to $2^{N-1}$. A paper-local exhaustive control checks all compositions through $N=18$, making 3,408,240 exact assertions; this is regression pressure, not proof or novelty evidence. The direct-owner search remains bounded, so the manuscript is `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'Sharp Cut-Deletion Clocks and Exact Fibres for Prefix-Divisibility Dynamics on Compositions'
```

## Markdown 正文

# The cut filter and its subtraction boundary

Let $\mathcal C_N$ be the set of ordered tuples of positive integers with sum $N$. The familiar cut-set encoding identifies $a=(a_1,\ldots,a_k)\in\mathcal C_N$ with $$\label{eq:cuts}
 \mathcal D(a)=\{s_1,\ldots,s_{k-1}\}\subseteq[N-1],\qquad
 s_i=\sum_{j=1}^i a_j.$$ Thus $|\mathcal C_N|=2^{N-1}$, and deleting cuts is coarsening. We use this standard encoding and refinement language as background [@Stanley2011EC1; @BilleraThomasVanWilligenburg2006].

Define $F_N:\mathcal C_N\to\mathcal C_N$ by its retained cuts: $$\label{eq:update}
 \mathcal D(F_N(a))=\{s_i\in\mathcal D(a):a_i\mid s_i\}.$$ All tests in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} use the parts of the composition at the start of the epoch, and all failing cuts are deleted simultaneously. The final endpoint $N$ is not a cut and is never tested. For example, $$\label{eq:orbit-example}
 (1,2,1,1,1)\longmapsto(1,3,1,1)
 \longmapsto(1,4,1)\longmapsto(1,5).$$

Restricted compositions and local conditions are established enumerative themes [@HeubachMansour2009; @BenderCanfield2005]. A nearby static divisibility class asks whether the *index* $i$ divides the prefix sum [@Navarro2026OEISA398023]; our dynamic test instead asks whether the current *part* $a_i$ divides its endpoint and then changes the parts by coarsening.

We assign the composition--subset bijection, refinement order, elementary divisibility, and generic path dynamic programming zero contribution credit. Internally, the mechanism is not the balanced part splitting of P126, the equal-run merging of P147, the Euclidean quotient rotation of P131, the set-partition token transfer of P169, the permutation prefix reversal of P181, the prefix-diversity word map of P185, or the support-rank compression of P186. This subtraction is not an ownership result. The external search was bounded; a non-hit is not evidence of novelty, priority, completeness, or freedom to operate.

# Fixed states and the sharp clock

Write $\mu(a)$ for the least $t\geq0$ such that $F_N^t(a)$ is recurrent.

[\[prop:fixed\]]{#prop:fixed label="prop:fixed"} Every recurrent state is fixed, and $$\label{eq:fixed-character}
 a\in\operatorname{Fix}(F_N)\quad\Longleftrightarrow\quad
 a_i\mid s_i\quad(1\leq i<k).$$ Set $A(0)=1$ and, for $v\geq1$, set $$\label{eq:A-recurrence}
 A(v)=\sum_{\substack{0\leq u<v\\v-u\mid v}}A(u).$$ Then, for every $N\geq1$, $$\label{eq:fixed-count}
 |\operatorname{Fix}(F_N)|=\sum_{v=0}^{N-1}A(v).$$

Equation [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} gives $\mathcal D(F_N(a))\subseteq\mathcal D(a)$, with equality precisely under [\[eq:fixed-character\]](#eq:fixed-character){reference-type="eqref" reference="eq:fixed-character"}. Every nonfixed epoch strictly loses a cut, so a cycle cannot contain a nonfixed state.

For the count, regard a sequence of internal cuts as an increasing path from $0$. If the last cut is $v$ and its predecessor is $u$, the part ending at $v$ has size $v-u$; fixedness at that cut is exactly $v-u\mid v$. Last-edge decomposition gives [\[eq:A-recurrence\]](#eq:A-recurrence){reference-type="eqref" reference="eq:A-recurrence"}. A fixed composition of $N$ has either no internal cut, represented by $v=0$, or a unique last internal cut $v<N$. The final part $N-v$ is untested, which proves [\[eq:fixed-count\]](#eq:fixed-count){reference-type="eqref" reference="eq:fixed-count"}.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For $N\leq3$, every composition is fixed. For every $N\geq4$, $$\label{eq:max-tail}
 \max_{a\in\mathcal C_N}\mu(a)=N-3,$$ and the unique composition attaining this maximum is $$\label{eq:witness}
 \omega_N=(1,2,1^{N-3}).$$ At every time $0\leq t\leq N-3$ its state is $$\label{eq:witness-orbit}
 F_N^t(\omega_N)=(1,2+t,1^{N-3-t}).$$

If a composition has an internal first cut, that cut always survives: its ending part and endpoint are both $a_1$. A composition of length $k$ therefore has at most $k-2$ deletable cuts. Every nonfixed epoch deletes at least one. The only composition of length $N$ is $(1^N)$, which is fixed, so a nonfixed state has $k\leq N-1$ and hence tail at most $N-3$. Directly from the rule, all compositions for $N=1,2,3$ are fixed.

For $\omega_N$, suppose [\[eq:witness-orbit\]](#eq:witness-orbit){reference-type="eqref" reference="eq:witness-orbit"} holds at time $t<N-3$. The middle part $2+t$ ends at $3+t$. It does not divide this endpoint, because otherwise it would divide their difference $1$. The first part and all trailing unit parts pass their tests, so exactly the cut after the middle part is deleted. This proves [\[eq:witness-orbit\]](#eq:witness-orbit){reference-type="eqref" reference="eq:witness-orbit"} by induction and shows that $\mu(\omega_N)=N-3$.

It remains to prove uniqueness. Equality in the two upper bounds forces an extremizer to have $N-1$ parts and to lose exactly one cut at every nonfixed epoch. A positive composition of $N$ with $N-1$ parts has one part equal to $2$ and all others equal to $1$. It is fixed if the $2$ is first or final. Otherwise let $r\geq1$ be the number of leading unit parts. Throughout the orbit, cuts ending unit parts survive; only the cut after the block containing the $2$ can disappear. There are just $N-r-2$ parts to that block's right, so its tail is at most $N-r-2$. Equality with $N-3$ forces $r=1$, giving exactly [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"}.

The fixed counts for $N=1,\ldots,15$ are $$1,2,4,7,13,20,37,55,97,157,267,378,719,1061,1763.$$ These values follow from [\[eq:A-recurrence\]](#eq:A-recurrence){reference-type="eqref" reference="eq:A-recurrence"}; they are quoted only as small controls, not as a replacement for the recurrence.

# Every-target fibres

Fix a target $b\in\mathcal C_N$ with cut set $T=\mathcal D(b)$. A source composition is uniquely an increasing path $$\label{eq:path}
 0=x_0<x_1<\cdots<x_\ell=N,$$ whose nonfinal vertices are its cuts. Declare an edge $u\to v$ to be $T$-admissible when

(i) no member of $T$ lies strictly between $u$ and $v$; and

(ii) if $v<N$, then $v\in T$ holds exactly when $v-u\mid v$.

No divisibility condition is imposed when $v=N$.

[\[thm:global-fibre\]]{#thm:global-fibre label="thm:global-fibre"} Let $P_T(0)=1$ and, for $1\leq v\leq N$, define $$\label{eq:global-dp}
 P_T(v)=\sum_{\substack{0\leq u<v\\u\to v\;T\text{-admissible}}}P_T(u).$$ Then every labelled target has the exact fibre size $$\label{eq:fibre-global}
 |F_N^{-1}(b)|=P_T(N).$$ Consequently $b\in\operatorname{im}(F_N)$ if and only if $P_T(N)>0$.

Every target cut must already occur on a source path, so a source edge cannot jump over it; this is condition (i). At a nonfinal source vertex $v$, the incoming part is $v-u$. Equation [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} retains $v$ precisely when this step divides $v$. Thus condition (ii) says simultaneously that each target vertex survives and that each extra source vertex is deleted. The final endpoint is untested. It follows that source paths mapping to $b$ are exactly the $T$-admissible paths. Last-edge decomposition gives [\[eq:global-dp\]](#eq:global-dp){reference-type="eqref" reference="eq:global-dp"}, proving the fibre and image statements.

The mandatory target cuts make this inverse count local. List all target endpoints as $$0=t_0<t_1<\cdots<t_m=N,$$ so $T=\{t_1,\ldots,t_{m-1}\}$. For consecutive endpoints $p<q$, put $h_p(p)=1$ and, for $p<v<q$, put $$\label{eq:h-recurrence}
 h_p(v)=\sum_{\substack{p\leq u<v\\v-u\nmid v}}h_p(u).$$ Define an internal and a final interval factor by $$\begin{aligned}
 K(p,q)&=\sum_{\substack{p\leq u<q\\q-u\mid q}}h_p(u)
 &&(q<N),\label{eq:K}\qquad\\[-2mm]
 K_*(p,N)&=\sum_{p\leq u<N}h_p(u).\label{eq:Kstar}\end{aligned}$$

[\[cor:factor\]]{#cor:factor label="cor:factor"} For every target endpoint list as above, $$\label{eq:product}
 |F_N^{-1}(b)|=
 \left(\prod_{j=1}^{m-1}K(t_{j-1},t_j)\right)
 K_*(t_{m-1},N).$$ In particular, the target is in the image exactly when every factor in [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} is positive. The empty product covers the one-part target.

Within an interval $(p,q)$, every extra source vertex must be deleted. Recurrence [\[eq:h-recurrence\]](#eq:h-recurrence){reference-type="eqref" reference="eq:h-recurrence"} counts exactly the paths from $p$ to $v$ whose intervening vertices, including $v$, have nondividing incoming steps. For an internal target endpoint $q$, the last step must instead divide $q$, giving [\[eq:K\]](#eq:K){reference-type="eqref" reference="eq:K"}; at $N$ no test is made, giving [\[eq:Kstar\]](#eq:Kstar){reference-type="eqref" reference="eq:Kstar"}. Restriction to consecutive target intervals and concatenation are inverse bijections. Multiplying their independent path counts proves [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}; positivity is therefore equivalent to image membership.

[\[cor:mass\]]{#cor:mass label="cor:mass"} For every $N\geq1$, $$\label{eq:mass}
 \sum_{b\in\mathcal C_N}|F_N^{-1}(b)|=2^{N-1}.$$

The labelled fibres partition the source carrier $\mathcal C_N$, and the cut-set encoding gives $|\mathcal C_N|=2^{N-1}$.

Both [\[eq:global-dp\]](#eq:global-dp){reference-type="eqref" reference="eq:global-dp"} and the complete collection of interval recurrences can be evaluated with $O(N^2)$ arithmetic operations for a fixed target. The global recurrence exposes the inverse bijection directly, while the product formula separates the contribution of each mandatory target cut.

# Exact pressure, limitations, and conclusion

The paper-local standard-library verifier exhausts all $2^{N-1}$ compositions for every $1\leq N\leq18$. It constructs the literal map, decomposes its functional graph, tests the fixed recurrence and every time slice of the extremal orbit, and compares true indegrees target by target with both [\[eq:global-dp\]](#eq:global-dp){reference-type="eqref" reference="eq:global-dp"} and [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}. It checks image equality and fibre mass only after the pointwise comparisons. Selected complete boxes appear in Table [1](#tab:control){reference-type="ref" reference="tab:control"}.

::: {#tab:control}
    $N$   states   image   fixed   max tail   deepest   max fibre
  ----- -------- ------- ------- ---------- --------- -----------
      4        8       7       7          1         1           2
      8      128      73      55          5         1          11
     12     2048     801     378          9         1          59
     15    16384    4906    1763         12         1         182
     18   131072   28535    7398         15         1         696

  : Selected exhaustive author controls. "Deepest" counts states of maximum tail. Proofs, rather than the finite range, establish the theorems.
:::

The results concern positive compositions, simultaneous updates, and the literal divisibility predicate in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. We do not give a closed scalar formula for the full image size, arbitrary pointwise tails, or time-$t$ fibres. We also make no theorem for weak compositions, asynchronous deletions, other divisibility directions, or weighted refinements. The finite computation is not proof, experiment, or ownership evidence. What is settled here is the all-parameter fixed and sharp-clock structure together with a complete, computable one-step inverse atlas. External circulation remains blocked while ownership is amber.

# Declarations {#declarations .unnumbered}

#### Data availability.

No external data were used. Exact source code and its canonical stdout accompany the manuscript.

#### Ethics.

The work studies a finite combinatorial map and raises no human-subject, personal-data, or deployment issue.

#### CRediT roles.

Anonymous author(s) performed conceptualization, formal analysis, software, validation, original drafting, and review and editing.

#### Competing interests.

No competing interests are declared.

#### Funding.

No external funding is declared for this manuscript.

#### AI-use statement.

Generative AI tools assisted with ideation, drafting, and code scaffolding. The author-side verifier checks finite cases; responsibility for every definition, proof, citation, and disclosure remains with the human author(s).

#### Release status.

External circulation, posting, and submission are not authorized while `HOLD_EXTERNAL` remains active.
