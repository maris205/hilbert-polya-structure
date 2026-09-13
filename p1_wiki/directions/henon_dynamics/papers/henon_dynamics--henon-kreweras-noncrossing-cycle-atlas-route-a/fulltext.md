---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kreweras-noncrossing-cycle-atlas-route-a"
canonical_tex: "henon_dynamics/henon_kreweras_noncrossing_cycle_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kreweras_noncrossing_cycle_atlas_route_a/paper/main.pdf"
source_sha256: "be002d8be3f5ba1caab535cde1821a94be1b1384d18b7e2cbebd28051eeb237d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The ordinary Kreweras complement: an exact finite cycle atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kreweras_noncrossing_cycle_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kreweras_noncrossing_cycle_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kreweras_noncrossing_cycle_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kreweras_noncrossing_cycle_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze a finite dynamical system on the noncrossing partitions of a labelled polygon. The clock is one ordinary Kreweras complement, defined by a permutation formula with an explicit orientation. The type-A order-$2n$ cyclic-sieving theorem supplies every iterate fixed count. We then derive, without fitting, all least-period populations, cycle counts, the finite Artin--Mazur zeta, the reciprocal Koopman determinant, root-of-unity spectral multiplicities, rank duality, and polygon-reflection reversors. The actual order is $1$, $2$, or $2n$ at $n=1$, $n=2$, or $n\geq3$; this small-dimensional boundary is part of the theorem. Independent set-partition enumeration through $n=8$ and exact SymPy cyclotomic checks through $n=12$ audit the ledger. The result is deliberately source-local: Catalan data carry no intrinsic rational-prime clock, so no arithmetic determinant or Hilbert--Pólya claim is made.
author:
- 'HCS-C209 source-derived research package'
date: 28 August 2026
title: 'The ordinary Kreweras complement: an exact finite cycle atlas'
```

## Markdown 正文

suppressoptionalinfo 611

# Object and orientation

Place vertices $[n]=\{0,1,\ldots,n-1\}$ counterclockwise on a convex polygon. A set partition is noncrossing when no two blocks contain $a,c$ and $b,d$ in the cyclic order $a<b<c<d$. For $\pi\in\mathrm{NC}(n)$, let $p_\pi$ cycle each block in increasing order, and let $c=(0\ 1\ \cdots\ n-1)$. We use $$K(\pi)=\operatorname{cycles}(p_\pi^{-1}c).                 \label{eq:K}$$ The notation $\operatorname{cycles}$ means the set partition formed by the cycles of a permutation. This convention gives the clockwise rotation $\rho_{-1}(i)=i-1\pmod n$ in the square identity below. Replacing $c$ by $c^{-1}$ conjugates the action by a reflection and changes only this sign.

There are two useful orders. Let $$L_n=\begin{cases}1,&n=1,\\2,&n=2,\\2n,&n\ge3,\end{cases}\qquad
 G_n=\begin{cases}1,&n=1,\\2n,&n\ge2.\end{cases}                 \label{eq:orders}$$ $L_n$ is the actual order of the permutation $K$. $G_n$ is the abstract cyclic-group order in the order-$2n$ CSP. At $n=2$ the action has a kernel of order two, so these symbols must not be conflated.

# Structural identities

[\[thm:struct\]]{#thm:struct label="thm:struct"} For every $n$, $K$ is a bijection of $\mathrm{NC}(n)$ and $$K^2=\rho_{-1},\qquad |K(\pi)|=n+1-|\pi|.
 \label{eq:square-rank}$$ It reverses refinement. Every reflection $R_j(i)=j-i\pmod n$ obeys $R_j^2=1$ and $R_jKR_j=K^{-1}$. The actual order is $L_n$ in [\[eq:orders\]](#eq:orders){reference-type="eqref" reference="eq:orders"}.

The permutation factorization $p_\pi p_{K(\pi)}=c$ is the usual geodesic factorization for a noncrossing partition. Taking inverses and multiplying by $c$ gives the complement involution on the geodesic interval, hence the block count and refinement reversal. Applying the factorization twice relabels all vertices by $i\mapsto i-1$, giving the first identity in [\[eq:square-rank\]](#eq:square-rank){reference-type="eqref" reference="eq:square-rank"}. Conjugating the displayed permutations by $R_j$ gives the dihedral relation. For $n\ge3$, polygon rotation acts faithfully on $\mathrm{NC}(n)$, so $K^2$ has order $n$. If $n$ is odd, then $K^n$ is an odd power and reverses rank, sending the discrete partition to the indiscrete partition; hence it is not the identity. If $n$ is even, then $K^n=(K^2)^{n/2}=\rho_{-n/2}$, which is nontrivial by the same faithfulness. Thus $K^n\ne1$ in either parity, while $K^{2n}=1$, and the order is $2n$. Directly, $\mathrm{NC}(1)$ is a singleton and $K$ exchanges the two elements of $\mathrm{NC}(2)$.

The rank $r(\pi)=n-|\pi|$ has Narayana distribution $$\#\{\pi:|\pi|=b\}=\frac{1}{n}\binom{n}{b}\binom{n}{b-1},
 \qquad |\mathrm{NC}(n)|=\mathrm{Cat}_n=\frac{1}{n+1}\binom{2n}{n}.       \label{eq:narayana}$$ The rank involution in Theorem [\[thm:struct\]](#thm:struct){reference-type="ref" reference="thm:struct"} is checked row by row in the machine-readable evidence.

#### Audit convention.

The distinction between the actual order $L_n$ and the abstract CSP order $G_n$ is part of the statement, not a post-processing choice; in particular, the $n=2$ generator is evaluated at fourth roots.

# The fixed-point theorem

Write $[m]_q=1+q+\cdots+q^{m-1}$ and $$\mathrm{Cat}_n(q)=\frac{[2n]_q!}{[n]_q![n+1]_q!}\in\mathbb Z[q].       \label{eq:qcat}$$ The rotation CSP for $\mathrm{NC}(n)$ is the type-A theorem of Reiner--Stanton--White. The order-$2n$ complement extension is the $m=1$ type-A Kreweras CSP, recorded by Bessis--Reiner and credited there to direct calculations of White. We use these results with attribution, not as a claim of priority.

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} Let $F_n(d)=|\mathrm{Fix}(K^d)|$. For $n=1$, $F_1(d)=1$. For $n\ge2$, reduce $d$ modulo $L_n$. If $d=2r$ is even, then $$F_n(2r)=\begin{cases}
 \mathrm{Cat}_n,&r\equiv0\pmod n,\\
 \binom{2g}{g},&0<r<n,\quad g=\gcd(n,r).
 \end{cases}                                             \label{eq:even-fixed}$$ For odd $d$, $F_n(d)=\binom{n}{(n-1)/2}$ exactly when $n$ is odd and $d\equiv n\pmod{2n}$; all other odd rows are zero. Equivalently, for $n\ge2$, $$F_n(d)=\mathrm{Cat}_n\!\left(e^{2\pi i d/G_n}\right).             \label{eq:csp}$$ At $n=2$, equation [\[eq:csp\]](#eq:csp){reference-type="eqref" reference="eq:csp"} uses fourth roots for the abstract $C_4$ action even though the image permutation has order two.

The CSP gives [\[eq:csp\]](#eq:csp){reference-type="eqref" reference="eq:csp"}. For even exponents it is the usual rotation specialization: a rotation with $g=\gcd(n,r)$ fixes $\binom{2g}{g}$ partitions, with the identity giving $\mathrm{Cat}_n$. At an odd root the cyclotomic factors in [\[eq:qcat\]](#eq:qcat){reference-type="eqref" reference="eq:qcat"} cancel only for the central half-turn; rank reversal also forces $|\pi|=(n+1)/2$, so this row is absent for even $n$ and has the central binomial value for odd $n$. These elementary cancellations are implemented with integer polynomial remainders in the SymPy audit.

For orientation, the first rows are

   $n$   $L_n$   $\mathrm{Cat}_n$  $(F_n(0),F_n(1),\ldots,F_n(L_n-1))$
  ----- ------- ------------------ -------------------------------------
    1      1            1          \(1\)
    2      2            2          (2,0)
    3      6            5          (5,0,2,3,2,0)
    4      8            14         (14,0,2,0,6,0,2,0)
    5     10            42         (42,0,2,0,2,10,2,0,2,0)
    6     12           132         (132,0,2,0,6,0,20,0,6,0,2,0)

# Periods, zeta, and Koopman spectrum

The rest of the atlas is a finite consequence and needs no additional source assumption. Let $\mu$ denote the integer Möbius function.

[\[thm:cycles\]]{#thm:cycles label="thm:cycles"} For every $\ell\mid L_n$, define $$P_{n,\ell}=\sum_{d\mid\ell}\mu(\ell/d)F_n(d),
 \qquad C_{n,\ell}=P_{n,\ell}/\ell.                    \label{eq:mobius}$$ Then $P_{n,\ell}$ is the number of points of least period $\ell$ and $C_{n,\ell}$ is the number of cycles. They are nonnegative integers and sum to $\mathrm{Cat}_n$. The finite zeta and Koopman determinant are $$\zeta_{K,n}(z)=\prod_{\ell\mid L_n}(1-z^\ell)^{-C_{n,\ell}},\qquad
 \det(I-zU_n)=\prod_{\ell\mid L_n}(1-z^\ell)^{C_{n,\ell}}
 =\zeta_{K,n}(z)^{-1},                                      \label{eq:zeta}$$ where $U_nf=f\circ K$ on $\ell^2(\mathrm{NC}(n))$.

The fixed-point trace identity is $F_n(d)=\sum_{\ell\mid d}P_{n,\ell}$. Möbius inversion gives [\[eq:mobius\]](#eq:mobius){reference-type="eqref" reference="eq:mobius"}; dividing by $\ell$ counts cycles. Each cycle contributes the factor $1-z^\ell$ to a permutation determinant and its reciprocal to the Artin--Mazur product. This proves [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The spectrum of $U_n$ consists of $L_n$th roots, with $$\operatorname{mult}\!\left(e^{2\pi i k/L_n}\right)
 =\sum_{\substack{\ell\mid L_n\\L_n\mid k\ell}}C_{n,\ell},
 \qquad \mathrm{Tr}(U_n^d)=F_n(d).                                  \label{eq:spectrum}$$ The permutation matrix is unitary. For every $j$, the map $J_jf=\overline{f\circ R_j}$ is antiunitary and reverses $U_n$: $J_jU_nJ_j=U_n^{-1}$.

For example, the nonzero cycle lengths for $n=3,4,5,6$ are respectively $\{2,3\}$, $\{2,4,8\}$, $\{2,5,10\}$, and $\{2,4,6,12\}$. The machine ledger stores every exponent rather than only these summaries.

# Independent evidence

The producer emits exact rows for $1\le n\le24$ (597 fixed rows, 131 period rows, 597 spectral rows, 300 rank rows, and 24 structural rows). It also emits q-Catalan coefficients through $n=12$. A separate checker reimplements restricted-growth set partitions, crossing detection, the permutation in [\[eq:K\]](#eq:K){reference-type="eqref" reference="eq:K"}, all reflections, and the cycle decomposition. It enumerates all 2,055 partitions for $1\le n\le8$ and reports 8,025 assertions. It does not import producer code. A separate SymPy program reconstructs the q-factorial quotient and cyclotomic remainders (1,110 exact checks), then independently recomputes the period and spectral rows through $n=24$.

The byte-replay script regenerates identical JSON. The mutation harness tests 32 repaired-hash payload mutations and one stale-hash mutation; all are rejected. The release manifest excludes LaTeX sidecars and itself, and stores the hashes of exactly 27 payload files, including the three round PDFs.

#### Release invariant.

Every displayed finite identity is recomputed from integer rows before the manifest is written; the round PDFs are retained so that later edits cannot silently replace the audited manuscript.

# Scope, relation to C187, and conclusion

C209 is a complete finite combinatorial atlas, not an arithmetic promotion. The integer $n$, Catalan/Narayana counts, and polygon roots have no intrinsic rational-prime carrier. We therefore record the conservative evaluator tuple $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}),$$ with overall verdict 'ROUTE\_A\_REJECTED' and no Route-B invocation. The only operator is the finite source Koopman permutation; no target divisor, functional equation, Euler factor, root number, automorphy statement, or Hilbert--Pólya operator is asserted.

C187 instead owns promotion of rectangular standard Young tableaux, its q-hook polynomial, and evacuation. C209 owns set partitions, geometric complement, the $K^2$ polygon rotation, and the order-$2n$ complement clock. Shared Möbius/CSP bookkeeping does not make one a parameter continuation of the other.

9 G. Kreweras, "Sur les partitions non croisées d'un cycle," *Discrete Mathematics* 1 (1972), 333--350.

V. Reiner, D. Stanton, and D. White, "The cyclic sieving phenomenon," *Journal of Combinatorial Theory, Series A* 108 (2004), 17--50.

D. Bessis and V. Reiner, "Cyclic sieving of noncrossing partitions for complex reflection groups," *Annals of Combinatorics* 15(2) (2011), 197--222.
