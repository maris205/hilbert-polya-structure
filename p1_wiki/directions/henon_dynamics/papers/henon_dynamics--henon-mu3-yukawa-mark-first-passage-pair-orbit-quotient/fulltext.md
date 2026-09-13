---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-pair-orbit-quotient"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/paper/main.pdf"
source_sha256: "9bb852ceca92218cc997d7946ff998028a5c9d4860ba70e0dff1558ecf488325"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ordered-Pair Symmetry Quotients of Exact Finite First-Passage Laws

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_pair_orbit_quotient/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We quotient the 400 ordered pairs in a frozen twenty-target first-passage model by its faithful order-1920 label action. The ambient lifted order 11520 is retained as a distinct quantity. Reconstructing the induced action from all 65536 support indicators gives 272 ordered-pair orbits, with size spectrum $144\times1+128\times2$. The complete exact joint-survival and mixed-moment law is constant on every orbit. Orbit--stabilizer, a finite Burnside count, relation types, and the transpose involution are independently certified. All results are finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Ordered-Pair Symmetry Quotients of Exact Finite First-Passage Laws'
```

## Markdown 正文

# Frozen model and action

Let $L$ be the sixteen named labels and let $H_0,\ldots,H_{19}$ be the actual subgroup targets. A uniform permutation $\pi$ of $L$ has prefix support $A_k$, and $$T_i(\pi)=\min\{k:H_i\leq\Phi(A_k)\}.$$ The frozen source supplies every hit indicator on $2^L$ and all joint survival counts $$J_{ij}(k,\ell)=\#\{\pi:T_i(\pi)>k,\ T_j(\pi)>\ell\}.$$ Five named label permutations generate a faithful group $G$ of order 1920. Its lifted source group has order 11520; the two orders are never identified. Transport of closures induces $gH_i=H_{g i}$ and the diagonal pair action $g(i,j)=(g i,g j)$.

For every $g\in G$ and every ordered pair $(i,j)$, $$J_{ij}(k,\ell)=J_{g i,g j}(k,\ell)
 \quad(0\leq k,\ell\leq16).$$ Consequently all C90 mixed raw moments and covariances are constant on the diagonal $G$-orbit of $(i,j)$.

Relabeling a permutation is a bijection and carries each prefix support $A$ to $gA$. Generator-level verification on all support indicators proves $H_i\leq\Phi(A)$ exactly when $H_{g i}\leq\Phi(gA)$. Hence $T_i(\pi)=T_{g i}(g\pi)$ and likewise for $j$. Counting the joint events proves the identity. Mixed moments and covariance are finite functions of the joint law.

# Pair-orbit theorem

The diagonal action of $G$ on the 400 ordered target pairs has 272 orbits. Their exact statistics are

  -------------------- ----- ------------------------- -----
  orbit size $1$         144 stabilizer order $1920$     144
  orbit size $2$         128 stabilizer order $960$      128
  diagonal                16 incomparable                132
  forward-comparable      62 reverse-comparable           62
  -------------------- ----- ------------------------- -----

Pair transposition induces an involution with 20 fixed orbits. Both coordinate projections recover the sixteen single-target orbits.

Direct enumeration partitions all 400 pairs. Every orbit size divides $|G|$, giving the displayed stabilizers. Target inclusion is equivariant, so each orbit has one relation type. Transposition commutes with the diagonal action, hence descends to an involution. Finally, the fixed-pair sum $$\sum_{g\in G}|\operatorname{Fix}_{\{H_i\}}(g)|^2
   =522240=1920\cdot272$$ independently verifies the orbit count by Burnside's lemma.

# Independent certificate

The producer decodes an exact closure as the unique maximal-order hit target. The checker instead matches the twenty-bit hit vector of every support to a column of the subgroup-inclusion matrix. These independent decoders yield the same target maps and all 272 rows. Each row stores its complete pair membership, stabilizer, relation type, transpose index, covariance, and a SHA-256 digest of the full C90 joint payload. SymPy checks every orbit--stabilizer equation and the fixed-point quotient. Clean replay fixes the evidence digest $$\texttt{099d8f32794d6967b3f2653f92dcaa0b096c711b67ed070330d7763a146bc696}.$$ All 14 hostile mutations are rejected.

# Scope

The invocation of Burnside's lemma is only a finite orbit count. We do not construct or claim a full Burnside ring or table of marks. No arithmetic/local data, Euler factors, root numbers, automorphy, or Hilbert--Polya operator is claimed.
