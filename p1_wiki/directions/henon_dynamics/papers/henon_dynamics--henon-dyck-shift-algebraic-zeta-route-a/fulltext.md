---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dyck-shift-algebraic-zeta-route-a"
canonical_tex: "henon_dynamics/henon_dyck_shift_algebraic_zeta_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dyck_shift_algebraic_zeta_route_a/paper/main.pdf"
source_sha256: "744d5a569baf2f1f638575045fb234e777d454491f806029b3b2e9978d399616"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Periodic Orbits and Algebraic Zeta Geometry of One-Vertex Edge-Type Dyck Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dyck_shift_algebraic_zeta_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dyck_shift_algebraic_zeta_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dyck_shift_algebraic_zeta_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dyck_shift_algebraic_zeta_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the periodic-point theory of the edge-type Dyck shift associated with one vertex and $N$ loop edges. The algebraic zeta function yields explicit odd and even fixed-count formulas for every $N$ and every period, followed by primitive points and orbits through Möbius inversion. We distinguish the $N=1$ full-two-shift boundary from the $N>1$ double dominant pole, quadratic branchpoints, nonrationality, and orbit asymptotics. Formal series, symbolic algebra, and direct periodic-word enumeration independently audit the result; the source-locked entropy is $\log(N+1)$.
author:
- HCS Research Program
date: 27 August 2026(revision 2)
title: |
  Exact Periodic Orbits and Algebraic Zeta Geometry\
  of One-Vertex Edge-Type Dyck Shifts
```

## Markdown 正文

suppressoptionalinfo 611

# Model and algebraic zeta

Let $D_N^E$ be the edge-type Dyck shift for the graph with one vertex and $N$ loop edges. Its alphabet is $\{a_i,b_i:1\le i\le N\}$, with inverse-monoid relation $a_i b_j=1$ for $i=j$ and $0$ otherwise. A finite block is admissible when its reduction is nonzero. Put $$s_N(z)=\sqrt{1-4Nz^2}.$$ The context-free circular-code series satisfies $$g_N(z)=\frac{Nz^2}{1-g_N(z)},\qquad
 g_N(z)=\frac{1-s_N(z)}2,$$ where the second expression is the small solution. The source theorem, specialized to the one-vertex $N$-loop graph, gives $$\zeta_N(z)=\frac{1-g_N(z)}{(1-Nz-g_N(z))^2}.$$ Substitution, rather than a claim of priority, yields $$\label{eq:zeta}
 \zeta_N(z)=\frac{2(1+s_N(z))}
 {(1+s_N(z)-2Nz)^2}.$$

[\[thm:counts\]]{#thm:counts label="thm:counts"} Let $F_N(n)=|\operatorname{Fix}(\sigma^n)|$. If $n$ is odd, then $$F_N(n)=2\left((N+1)^n-
 \sum_{j=0}^{(n-1)/2}\binom njN^j\right).$$ If $n$ is even, then $$F_N(n)=2\left((N+1)^n-
 \sum_{j=0}^{n/2}\binom njN^j\right)
 +\binom n{n/2}N^{n/2}.$$ The numbers of least-period points and primitive orbits are $$P_N(n)=\sum_{d\mid n}\mu(n/d)F_N(d),\qquad C_N(n)=P_N(n)/n.$$

By definition, $z\,\zeta_N'(z)/\zeta_N(z)=\sum_{n\ge1}F_N(n)z^n$. Insert [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}, expand the quadratic series $s_N(z)$, and separate the central binomial term when $n$ is even. The two displayed parity formulas result. Möbius inversion isolates least periods. A least-period-$n$ orbit has exactly $n$ possible origins, proving the last division.

\>0

# The origin-marked word convention

$F_N(n)$ counts points of $\operatorname{Fix}(\sigma^n)$, equivalently length-$n$ periodic words with a distinguished origin; it does not count cyclic necklaces. Our direct audit enumerates such words and checks every cyclic factor through length $2n$ in the periodic extension. A stack reduction cancels $a_i b_i$ and rejects $a_i b_j$ for $i\ne j$. Thirty-three $(N,n)$ cells, including $N=1,\ldots,6$, agree exactly with Theorem [\[thm:counts\]](#thm:counts){reference-type="ref" reference="thm:counts"}. Only after Möbius inversion is $P_N(n)$ divided by $n$.

This distinction is substantive: division of $F_N(n)$ before inversion would mix points whose least period properly divides $n$ and generally fail integrality.

An $n$-periodic extension is admissible if and only if every cyclic factor of length at most $2n$ has nonzero reduction.

Every nonzero reduced word has normal form $BA$, with unmatched closing letters $B$ followed by unmatched opening letters $A$. Fix a cyclic origin and call its period word $v$. If $v$ reduces to zero, a forbidden prefix already has length at most $n$. Otherwise, in $v^2$ the only new interaction is the $AB$ interface. A colour mismatch is therefore already visible there. If the interface is compatible, equal lengths cancel and unequal lengths leave a monotone excess on one side; crucially, the final copy of $A$ is unchanged. Every later copy, and every prefix of it, repeats the same interface comparison. Thus the first zero prefix has length at most $2n$. Auditing every cyclic origin covers every factor of the bi-infinite extension.

\>1

# Boundary, poles, and asymptotics

For $N=1$, the radical in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} cancels and $\zeta_1(z)=(1-2z)^{-1}$, so $F_1(n)=2^n$. For $N>1$, the point $r_N=(N+1)^{-1}$ is a double pole, strictly inside the quadratic branchpoints $\pm(2\sqrt N)^{-1}$. The zeta function is nonrational and $$F_N(n)=2(N+1)^n+O\!\left(\frac{(2\sqrt N)^n}{\sqrt n}\right),
 \qquad C_N(n)\sim\frac{2(N+1)^n}{n}.$$ Moreover, $h_{\rm top}(D_N^E)=\log(N+1)$.

At $r_N$, $s_N(r_N)=(N-1)/(N+1)$, so the squared denominator vanishes while the numerator and the derivative of its unsquared factor do not. Since $N+1>2\sqrt N$ for $N>1$, this pole precedes both branchpoints. Replacing $s_N$ by $-s_N$ changes [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}; quadratic conjugation therefore rules out rationality. The omitted binomial tail is bounded by a geometric multiple of its central term, which is $O((2\sqrt N)^n/\sqrt n)$. Proper divisors are exponentially smaller, and Möbius inversion gives the cycle asymptotic. Krieger--Matsumoto Proposition 3.1 proves for Markov-Dyck shifts that topological entropy equals the exponential periodic-point growth rate. The displayed asymptotic therefore gives $h_{\rm top}(D_N^E)=\log(N+1)$. This uses that source theorem, not an unproved general identification of periodic growth with entropy.

# Exact audit and scope

For $N=1,\ldots,6$ and $n=1,\ldots,24$, all $144$ counts from the binomial formula equal an independent exact formal logarithmic derivative. SymPy checks $72$ coefficients plus cancellation, pole, dominance, conjugation, and six entropy/dominant-radius identities. Byte replay is exact. Eighteen semantic attacks with repaired payload hashes and one separate stale-hash integrity attack are rejected.

   $N\backslash n$    1    2     3      4      5       6
  ----------------- --- ---- ----- ------ ------ -------
          1           2    4     8     16     32      64
          2           4   12    40    120    384    1152
          3           6   24   108    432   1836    7344
          4           8   40   224   1120   5888   29440

This algebraic zeta is not identified with a target local factor. We claim no root numbers, automorphy, target determinant, or Hilbert--Pólya operator. The registered tuple is

(A0\_FAIL, A1\_WEAK, A2\_FAIL, A3\_FAIL, A4\_FAIL).

The exact record is `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.

# Source note {#source-note .unnumbered}

The model, zeta formula, and entropy lock follow Krieger--Matsumoto [@km2011]; Keller's loop-counting framework gives related context [@keller1991]. The official Münster volume PDF controls pagination; an arXiv journal-reference entry reports 171--185. No priority claim is made.

9 W. Krieger and K. Matsumoto, Zeta functions and topological entropy of the Markov-Dyck shifts, *Münster J. Math.* 4 (2011), 171--184, arXiv:0706.3262. G. Keller, Circular codes, loop counting, and zeta-functions, *J. Combin. Theory Ser. A* 56 (1991), 75--83, [doi:10.1016/0097-3165(91)90023-A](https://doi.org/10.1016/0097-3165(91)90023-A).

# Declarations {#declarations .unnumbered}

**Scope.** The exact registered literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. **Data and code.** Exact ledgers, independent checks, and build instructions are supplied in the HCS-C205 release package. **Competing interests.** None declared. **AI-use disclosure.** Generative AI tools assisted drafting and code generation. Every theorem statement, source record, exact output, and scope claim was checked through the released internal artifact audit chain; this is not external peer review or an independent error process.
