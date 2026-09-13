---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-moser-tardos-resampling-witness-tree-route-a"
canonical_tex: "henon_dynamics/henon_moser_tardos_resampling_witness_tree_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_moser_tardos_resampling_witness_tree_route_a/paper/main.pdf"
source_sha256: "3081f189dfae9c921c5404a43d5e64f91f5824f61bcc5f439710336ec4b1698e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sequential Resampling under the Variable-Model Local Lemma: A Complete Witness-Tree Termination Proof

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_moser_tardos_resampling_witness_tree_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_moser_tardos_resampling_witness_tree_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_moser_tardos_resampling_witness_tree_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_moser_tardos_resampling_witness_tree_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-locked proof of the finite-variable Moser--Tardos theorem. Under the asymmetric witness criterion, every legal sequential violated-event rule terminates almost surely, avoids all bad events, and satisfies the exact per-event and total expectation bounds. The proof includes the resampling-table witness lemma and the complete branching sum. Exact finite chains audit, but do not prove, the general result.
author:
- 'HCS-C325 theorem-and-evidence package'
date: '3 September 2026 --- revision round '
title: |
  Sequential Resampling under the Variable-Model Local Lemma:\
  A Complete Witness-Tree Termination Proof
```

## Markdown 正文

# Frozen variable model

Let $X_1,\ldots,X_n$ be independent, finite-valued variables and let $\mathcal A$ be a finite family of bad events. Write $\operatorname{vbl}(A)$ for the variables determining $A$, and $\Gamma(A)=\{B\ne A:\operatorname{vbl}(A)\cap\operatorname{vbl}(B)\ne\varnothing\}$. Each variable owns an independent table $X_i(0),X_i(1),\ldots$ of copies. Initially the zeroth entries are exposed. At each step an arbitrary legal rule chooses a currently violated $A$ and advances exactly the tables indexed by $\operatorname{vbl}(A)$. The executable audit alone fixes lexicographic choice.

[\[thm:main\]]{#thm:main label="thm:main"} Suppose $x_A\in(0,1)$ and $$\label{eq:lll}
 \mathbb P(A)\le x_A\prod_{B\in\Gamma(A)}(1-x_B),\qquad A\in\mathcal A.$$ Then every legal sequential rule terminates almost surely at an assignment avoiding $\mathcal A$. If $N_A$ counts resamplings of $A$, then $$\mathbb EN_A\le\frac{x_A}{1-x_A},\qquad
 \mathbb E\sum_A N_A\le\sum_A\frac{x_A}{1-x_A}.$$

The three exact binary examples contain seven events and all $112$ assignment rows. Their rational absorbing-chain expectations and proper-tree series through size six are reconstructed independently. They are regression data, not an extrapolation to Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

\>0

# The complete witness-tree proof

Fix an execution prefix $C(1),\ldots,C(t)$ with $C(t)=A$. Start a root labelled $A$, scan earlier resamplings backward, and attach $C(s)$ to a deepest existing label sharing a variable, discarding it if none exists. A fixed tie rule makes the tree unique.

[\[lem:witness\]]{#lem:witness label="lem:witness"} The resulting tree is proper: children of a vertex labelled $B$ have distinct labels in $\Gamma^+(B)=\Gamma(B)\cup\{B\}$. For every fixed proper labelled tree $T$, $$\mathbb P\{T\text{ occurs}\}\le\prod_{v\in T}\mathbb P([v]),$$ where $[v]$ denotes the label of $v$.

Every inserted child overlaps its parent. Were two siblings given the same label, the earlier inserted copy would be a deeper overlapping vertex when the second is scanned, a contradiction.

Define a canonical $T$-check, independently of any log: process vertices by non-increasing distance from the root, with a frozen label/path tie order; at each vertex test its event on the current table cells and then advance exactly its variables. Different vertex tests use disjoint cells, hence the pass probability is exactly $\prod_v\mathbb P([v])$.

If an execution produces $T$, every earlier resampling involving a retained vertex's variable is itself retained when the backward scan reaches it. Fix a variable $Y$. When an earlier retained event containing $Y$ is scanned, it overlaps every already present $Y$-vertex. Its chosen deepest overlapping parent therefore has depth at least the maximum current depth among those vertices, so the new vertex is strictly deeper than all of them. Thus chronological order among vertices using $Y$ is exactly decreasing depth, although those vertices need not form an ancestor chain. The canonical non-increasing-depth order preserves this order for every variable, so every vertex reads the same numbered table cells in the log and in the $T$-check. The successful tests force the canonical check to pass.

[\[lem:branch\]]{#lem:branch label="lem:branch"} For every $A$, $$\sum_{T:\,\mathrm{root}(T)=A}\prod_{v\in T}\mathbb P([v])
 \le \frac{x_A}{1-x_A},$$ where the sum is over all finite proper trees.

Start with root $A$. Independently at every vertex labelled $B$, add one child labelled $D$ with probability $x_D$, for each $D\in\Gamma^+(B)$. Directly multiplying included and omitted child choices gives, for a finite proper $T$, $$p_{\rm br}(T)=\frac{1-x_A}{x_A}
 \prod_{v\in T}\left[x_{[v]}\prod_{D\in\Gamma([v])}(1-x_D)\right].$$ By [\[eq:lll\]](#eq:lll){reference-type="eqref" reference="eq:lll"}, the desired event-weight product is at most $x_Ap_{\rm br}(T)/(1-x_A)$. The probabilities of all finite outputs of this branching experiment sum to at most one; summation proves the claim, whether or not the branching process can be infinite.

The witness trees attached to successive resamplings of $A$ are distinct: the $k$th contains exactly $k$ vertices labelled $A$, since every earlier $A$ overlaps and enters the existing $A$ chain. Lemmas [\[lem:witness\]](#lem:witness){reference-type="ref" reference="lem:witness"} and [\[lem:branch\]](#lem:branch){reference-type="ref" reference="lem:branch"}, followed by monotone convergence, give $\mathbb EN_A\le x_A/(1-x_A)$. Summing over the finite family gives finite expected total length. Hence an infinite log has probability zero. A legal rule stops only when no bad event is violated, so its terminal assignment avoids all of $\mathcal A$.

\>1

# Robustness, ownership, and Route A

The proof conditions only on the resampling tables and the actual legal log; it never uses the lexicographic audit rule. Thus adversarial, history-dependent, and randomized legal sequential choices obey the same bounds. With $\mathcal A=\varnothing$ termination is immediate. A probability-zero event is never initially or subsequently exposed as true outside a null table set.

Moser and Tardos own the constructive theorem [@mt]; this package claims a self-contained reconstruction, not priority. It does not cover lopsided or permutation spaces, parallel resampling, or instances outside [\[eq:lll\]](#eq:lll){reference-type="eqref" reference="eq:lll"}. C192 is a fixed chamber walk, C302 a recursive cost law, and C317 a deterministic matrix iteration; none owns shared-variable witness trees.

The Route-A tuple is $(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},
\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$. The verdict is `ROUTE_A_REJECTED`; Route B is locked. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, no target local data, Euler factor, root number, automorphy, divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.

# Revision certificate: arbitrary-rule robustness and scope closure {#revision-certificate-arbitrary-rule-robustness-and-scope-closure .unnumbered}

This final round adds the rule-independence argument, degenerate faces, source and collision ownership, strict evidence boundary, and Route-A firewall.

# Revision certificate: frozen resampling dynamics and exact chains {#revision-certificate-frozen-resampling-dynamics-and-exact-chains .unnumbered}

This original round fixes the tables, dependencies, legal clock, theorem contract, and complete small-instance transition ledger.

# Revision certificate: complete witness-tree and branching proof {#revision-certificate-complete-witness-tree-and-branching-proof .unnumbered}

This round adds both general lemmas and derives all expectation, termination, and avoidance conclusions without finite extrapolation.

1 R. A. Moser and G. Tardos, "A constructive proof of the general Lovasz Local Lemma," *J. ACM* 57 (2010), Article 11; DOI: 10.1145/1667053.1667060; arXiv:0903.0544.
