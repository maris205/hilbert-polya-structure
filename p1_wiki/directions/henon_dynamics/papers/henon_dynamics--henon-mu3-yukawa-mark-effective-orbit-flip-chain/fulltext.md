---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-effective-orbit-flip-chain"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_flip_chain/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_flip_chain/paper/main.pdf"
source_sha256: "bb31a9c5b5a2d37355a568dba913f1cb182d9c019e1318327ca699b83002bb2d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Effective-Orbit One-Bit Flip Chain of a Frozen Hénon Support Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_flip_chain>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_flip_chain/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_flip_chain/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_effective_orbit_flip_chain/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We quotient the sixteen-dimensional support cube by the faithful finite label action of order $1920$. The resulting one-bit flip chain has $3024$ states, constant row sum $16$, and $30240$ nonzero directed entries. We certify strong lumpability at every support, orbit-size detailed balance, the exact flow between four repair-distance levels, and the complete spectrum on orbit-constant functions. Its eigenvalues are $16-2k$, with multiplicity equal to the number of label-group orbits on $k$-subsets. The repair-zero diagonal flow is $445696$, independently reproducing the distance-one correlation from C82. The result is finite and combinatorial under the firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'The Effective-Orbit One-Bit Flip Chain of a Frozen Hénon Support Core'
```

## Markdown 正文

# Finite action and quotient

Let $L$ be the frozen set of sixteen named labels and identify a retained support $A\subseteq L$ with a vertex of $X=\{0,1\}^{16}$. C75 supplies an ambient lifted action of order $11520$, whose kernel on labels has order $6$. Accordingly, every support calculation here uses the faithful image $E\leq\mathfrak S_L$ of order $1920$, never the ambient order as though it were faithful. The action has $3024$ orbits on $X$.

Write $\mathcal O_i$ for these support orbits. For $A\in\mathcal O_i$ define $$q_{ij}=\#\{\ell\in L:A\mathbin{\triangle}\{\ell\}\in\mathcal O_j\}.$$ Thus $Q=(q_{ij})$ records how the ordinary cube adjacency operator acts on functions that are constant on $E$-orbits.

The number $q_{ij}$ is independent of the chosen $A\in\mathcal O_i$. Every row of $Q$ sums to $16$, and $$|\mathcal O_i|q_{ij}=|\mathcal O_j|q_{ji}.$$ Consequently the orbit-size measure is reversible. The quotient has $30240$ nonzero directed entries and $15120$ unoriented orbit pairs.

For $g\in E$, toggling is equivariant: $g(A\mathbin{\triangle}\{\ell\})=gA\mathbin{\triangle}\{g\ell\}$. Since $g$ permutes the sixteen labels, it bijects the toggles from any two representatives of $\mathcal O_i$ and preserves target orbits. This proves strong lumpability and the row sum. Counting actual cube edges from $\mathcal O_i$ to $\mathcal O_j$ in the two orientations gives the detailed-balance identity. Support-size parity changes under every toggle, so there are no self-loops; hence directed entries occur in opposite pairs.

The number of distinct target orbits in a row has distribution $$\begin{array}{c|rrrrrrr}
\toprule
\text{targets}&7&8&9&10&11&12&13\\
\text{rows}&128&384&480&800&864&336&32\\
\bottomrule
\end{array}$$ and positive entries $1,2,3,4,5$ occur respectively $19296,7344,1008,1584,1008$ times.

# Complete invariant spectrum

For $B\subseteq L$, let $\chi_B(A)=(-1)^{|A\cap B|}$ be the Walsh character. A direct cube calculation gives adjacency eigenvalue $16-2|B|$.

The complete spectrum of $Q$ is $16-2k$, $0\leq k\leq16$. Its multiplicity is the number of $E$-orbits on $k$-subsets, namely $$\begin{array}{c|rrrrrrrrr}
\toprule
k&0&1&2&3&4&5&6&7&8\\
m_k&1&7&27&73&151&252&352&424&450\\
\midrule
k&9&10&11&12&13&14&15&16\\
m_k&424&352&252&151&73&27&7&1\\
\bottomrule
\end{array}$$ The multiplicities sum to $3024$; the first and second spectral moments are $0$ and $77760$.

The Walsh characters form an orthogonal eigenbasis of functions on $X$. The action of $E$ permutes them by $g\chi_B=\chi_{gB}$. Summing characters over each orbit of subsets produces a nonzero invariant eigenfunction. Distinct orbit sums have disjoint Walsh support and are independent; every invariant function has coefficients constant on those orbits. They therefore form a basis of the invariant subspace, which is identified with functions on the $3024$ support orbits. The stated multiplicities follow.

# Repair flow and predecessor identity

Let $\rho(A)\in\{0,1,2,3\}$ be the frozen repair distance from C78. The numbers of support orbits at these four levels are $1332,1500,180,12$. Counting actual directed cube edges by the pair of repair levels gives $$\begin{array}{c|rrrr}
\toprule
&0&1&2&3\\\midrule
0&445696&40704&0&0\\
1&40704&469376&13184&0\\
2&0&13184&24064&640\\
3&0&0&640&384\\
\bottomrule
\end{array}$$ whose entries sum to $16\cdot2^{16}$. In particular, the $(0,0)$ entry is the number of ordered Hamming-distance-one pairs for which both endpoints have the full core. Its value $445696$ exactly equals the C82 distance-one autocorrelation, providing a cross-paper identity obtained by a different aggregation route.

# Certificate and scope

The producer explicitly generates all $1920$ label permutations, whereas the independent checker constructs support-orbit components using only five named generators. Both verify every one of the $65536$ supports and every quotient row. A symbolic radial-cube check, clean replay, and twenty hostile mutations complete the audit. The canonical evidence SHA-256 is

`7b3e2179590c3dc8662a59f1d79ffbb1`\
`2f2a4a787438a6902d6c28b2842e70b8`.

No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside ring or table of marks, or Hilbert--Polya operator is claimed.
