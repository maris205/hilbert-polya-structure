---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-generation-blocker-reliability"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/paper/main.pdf"
source_sha256: "9c67fa1d44c0fad7459b06a3ea5d8277c9b20a7eae51f988b4e9979022389328"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Blocker Geometry and Exact Erasure Reliability of a Named Complement Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An exhaustive coordinate atlas previously classified all named supports of a universal complement core $Q\cong\mathbb Z/3\oplus\mathbb Z/18$. We now determine its deletion geometry. Reduction through the Frattini quotient turns the non-isolated part of the minimal-generation hypergraph into a cone over $K_{1,1,2,5}$, while six dummy labels remain isolated. This yields exactly five inclusion-minimal blockers, a complete deletion spectrum with $35136$ destructive and $30400$ surviving sets, and closed homogeneous and heterogeneous reliability formulae. We separate three non-equivalent robustness parameters and compute the Banzhaf influence and Shapley value of every named coordinate. All results concern only the frozen sixteen-label presentation.
author:
- Anonymous
title: Blocker Geometry and Exact Erasure Reliability of a Named Complement Core
```

## Markdown 正文

# Generation geometry

Let $q_j=8[S_j]$ denote the sixteen named classes in the universal core $$Q=8C\cong\mathbb Z/3\oplus\mathbb Z/18
       \cong\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2.$$ The exact predecessor atlas gives coordinates $(a_j,b_j,c_j)$ in the latter model. A support generates $Q$ precisely when it generates both its $\mathbb Z/2$ coordinate and the Frattini quotient of its odd part. The only nonzero $c_j$ occurs at $j=9$. The nonzero vectors $(a_j,b_j)\bmod3$ fall into four projective directions: $$\label{eq:blocks}
 B_0=\{S_1\},\quad B_1=\{S_{16}\},\quad
 B_2=\{S_7,S_{15}\},\quad
 B_3=\{S_3,S_4,S_8,S_{11},S_{12}\}.$$ The remaining labels $$\mathcal D=\{S_2,S_5,S_6,S_{10},S_{13},S_{14}\}$$ are dummy coordinates for full generation. Here $q_2$ is nonzero, but lies in the Frattini subgroup; the other five vanish in $Q$.

The scope firewall is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ No full table of marks or Burnside ring, arithmetic or local construction, Euler factor, root number, automorphy, or Hilbert--Polya operator is claimed.

[\[thm:criterion\]]{#thm:criterion label="thm:criterion"} A named support generates $Q$ if and only if it contains $S_9$ and meets at least two distinct blocks in Equation [\[eq:blocks\]](#eq:blocks){reference-type="eqref" reference="eq:blocks"}. Consequently, on all sixteen named labels, its inclusion-minimal generating hypergraph consists of six isolated dummy vertices together with the cone having apex $S_9$ over $K_{1,1,2,5}$; its non-isolated part has twenty-five hyperedges.

The unique dyadic coordinate forces $S_9$. For the odd part, Nakayama's criterion for finite abelian $3$-groups reduces generation to spanning the two-dimensional Frattini quotient. Two nonzero projective vectors span it exactly when they have distinct directions. Thus a minimal support consists of $S_9$ and one vertex from each of two different blocks. Summing the edge counts gives $$1\cdot1+1\cdot2+1\cdot5+1\cdot2+1\cdot5+2\cdot5=25.$$

# Minimal blockers and every deletion

A deletion set is *destructive* when its retained complement does not generate $Q$. A minimal blocker is an inclusion-minimal destructive set.

[\[thm:blockers\]]{#thm:blockers label="thm:blockers"} There are exactly five minimal blockers: $$\begin{split}
&\{S_9\},\qquad \{S_1,S_7,S_{15},S_{16}\},\\
&\{S_1,S_3,S_4,S_8,S_{11},S_{12},S_{16}\},\\
&\{S_1,S_3,S_4,S_7,S_8,S_{11},S_{12},S_{15}\},\\
&\{S_3,S_4,S_7,S_8,S_{11},S_{12},S_{15},S_{16}\}.
\end{split}$$ Their size enumerator is $$\beta(x)=x+x^4+x^7+2x^8.$$

One may destroy generation by deleting the apex. If the apex remains, the retained base vertices must lie in at most one projective block. Minimality then forces deletion of the union of the other three blocks. The four choices of surviving block give blocker sizes $8,8,7,4$, respectively.

Let $\Gamma=K_{1,1,2,5}$. Its independent-set and vertex-cover polynomials are $$\begin{aligned}
 I_\Gamma(z)&=1+9z+11z^2+10z^3+5z^4+z^5,\\
 C_\Gamma(x)&=x^4+5x^5+10x^6+11x^7+9x^8+x^9.\end{aligned}$$ All destructive sets, as opposed to only the five minimal ones, have enumerator $$\label{eq:transversal}
 T(x)=x(1+x)^{15}+(1+x)^6C_\Gamma(x).$$ The first term deletes $S_9$; the second retains it, deletes a vertex cover of the base graph, and makes arbitrary choices on the six dummy labels. These two cases are disjoint.

::: {#tab:deletion}
    deleted $k$      0      1      2      3      4      5      6      7       8
  ------------- ------ ------ ------ ------ ------ ------ ------ ------ -------
    destructive      0      1     15    105    456   1376   3058   5171    6775
      surviving      1     15    105    455   1364   2992   4950   6269    6095
    deleted $k$      9     10     11     12     13     14     15     16   total
    destructive   6936   5547   3428   1596    535    120     16      1   35136
      surviving   4504   2461    940    224     25      0      0      0   30400

  : Complete deletion spectrum. Each size-$k$ column sums to $\binom{16}{k}$.
:::

Expanding Equation [\[eq:transversal\]](#eq:transversal){reference-type="eqref" reference="eq:transversal"} gives the destructive row of Table [1](#tab:deletion){reference-type="ref" reference="tab:deletion"}. Direct projective-rank enumeration of all $2^{16}$ retained supports independently gives both rows.

# Exact reliability

Suppose first that every coordinate is deleted independently with probability $q$. Generation succeeds exactly when $S_9$ survives and at most two of the four blocks are deleted in their entirety.

For equal deletion probability, $$\label{eq:homogeneous}
 R(q)=(1-q)(1-q^4-q^7-2q^8+3q^9).$$ More generally, let $q_i$ be the deletion probability of $S_i$ and put $$Q_j=\prod_{S_i\in B_j}q_i\qquad(0\leq j\leq3).$$ Then $$\label{eq:heterogeneous}
 R=(1-q_9)\left(
 1-\sum_{j=0}^3\prod_{k\ne j}Q_k+3\prod_{j=0}^3Q_j
 \right).$$ The deletion probabilities of the six dummy coordinates cancel exactly.

The probability that at least three of four independent block-failure events occur is the sum of their four triple intersections minus three times their common intersection. Taking the complement and requiring the apex to survive gives Equation [\[eq:heterogeneous\]](#eq:heterogeneous){reference-type="eqref" reference="eq:heterogeneous"}. In the homogeneous case the block failure probabilities are $q,q,q^2,q^5$, which gives $q^4+q^7+2q^8-3q^9$ for odd-part failure and proves Equation [\[eq:homogeneous\]](#eq:homogeneous){reference-type="eqref" reference="eq:homogeneous"}.

Three robustness notions must be separated. Without protection, worst-case deletion tolerance is zero because deleting $S_9$ is fatal. If $S_9$ is protected, the smallest remaining blocker has size four, so the worst-case tolerance is three. Existentially, one can delete thirteen coordinates and retain one of the twenty-five minimal triples; fourteen deletions never survive. Thus the three exact parameters are $$0,\qquad3,\qquad13,$$ and exactly twenty-five deletion sets attain the last value.

# Coordinate importance and symmetry boundary

View generation as a monotone simple game on the sixteen labels. The uniform Banzhaf influence is the fraction of coalitions for which a coordinate is pivotal; it is not normalized to sum to one. Shapley values are normalized. The five structural orbits give the complete table.

::: {#tab:importance}
  labels                                 orbit size   Banzhaf influence   Shapley value
  ------------------------------------ ------------ ------------------- ---------------
  $S_9$                                           1           $475/512$       $271/360$
  $S_1,S_{16}$                                    2            $35/512$       $61/1260$
  $S_7,S_{15}$                                    2            $33/512$          $2/45$
  $S_3,S_4,S_8,S_{11},S_{12}$                     5             $5/512$       $31/2520$
  $S_2,S_5,S_6,S_{10},S_{13},S_{14}$              6                 $0$             $0$

  : Coordinate importance in the named generation game. The sixteen Shapley values sum to one.
:::

The abstract automorphism order of this full sixteen-vertex hypergraph is $$6!\,2!\,2!\,5!=345600:$$ the factors permute dummy vertices, the two singleton direction blocks, and vertices within the blocks of sizes two and five. This is an automorphism statement about the unlabelled generation hypergraph. It is not identified with $\operatorname{Aut}(Q)$ and is not a label-preserving symmetry claim.

# Reproducibility and conclusion

The certificate binds the C71 and C72 evidence and manifests. The producer derives the projective partition, blockers, deletion spectrum, reliability, and importance indices. An independent checker rebuilds all projective determinants and enumerates every deletion without importing the C72 support polynomial. SymPy independently enumerates all block-failure states and checks the graph, transversal, and reliability polynomial expansions. GAP checks the order of the structural direct-product subgroup after the orbit classification above. Clean replay passes and thirty-five hostile semantic mutations are rejected. C73 therefore closes the adaptive round with a structural reliability theorem rather than merely reversing the predecessor's coefficient table.
