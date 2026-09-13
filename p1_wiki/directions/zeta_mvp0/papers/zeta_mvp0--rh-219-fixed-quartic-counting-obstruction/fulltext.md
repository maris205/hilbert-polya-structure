---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-219-fixed-quartic-counting-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction/main.pdf"
source_sha256: "b5250cad54f4d32e0ce907160e9f93be8a9fb2451e9b3a3750ad62c3de29c312"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Why a Fixed Quartic Cannot Supply a Growing Spectral Count Bounded Degree, Repeated Support, and Local Finiteness

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-219-fixed-quartic-counting-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-212--RH-218 extract substantial exact geometry from one physical edge quartet. This paper determines what even perfect control of that quartet could contribute to an infinite spectral determinant. The answer is sharply limited.

  First, a locally uniformly convergent family of monic polynomials of uniformly bounded degree has a polynomial limit of bounded degree; it cannot acquire an unbounded zero count. Second, replacing a quartic $Q$ by powers $Q^N$ grows algebraic degree only through multiplicity. Its distinct support remains at most four points, and as $N\to\infty$ the zero divisors cease to be locally finite on every neighborhood of those points. They therefore cannot converge to the divisor of a nonzero holomorphic function on such a domain.

  For the finest normalized physical quartet, powers through $N=64$ raise the degree from four to 256 while the support remains exactly four. The associated height-counting functions have only the same finite jump locations with growing jump sizes. This behavior cannot produce a locally finite spectrum with an extended counting law.

  The conclusion is an exact route obstruction, not a negative result about the quartet's local usefulness. It remains a branch seed and finite factor, but Gate A requires a rank-growing physical divisor that adds genuinely new roots and controls omitted factors. No $T\log T$ theorem or zeta statement is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Why a Fixed Quartic Cannot Supply a Growing Spectral Count\
  Bounded Degree, Repeated Support, and Local Finiteness
```

## Markdown 正文

# The fixed-factor question

The centered quartet has an exact shape manifold, a finite monotone axial clock, and a classified degenerate boundary [@WangRH213; @WangRH214; @WangRH216]. Simple autonomous recurrence is not identified, but suppose optimistically that a later argument controlled the quartet at every scale. Could this alone be the determinant sought in Gate A?

An infinite spectral determinant must have a locally finite zero divisor: every compact subset of its domain contains only finitely many zeros counted with finite multiplicity, unless the function is identically zero. A four-root factor confronts this requirement in two possible ways:

1.  keep degree four while taking a scale limit;

2.  repeat or power the factor so algebraic degree grows.

Both are insufficient.

# Bounded degree stays bounded

[\[thm:degree\]]{#thm:degree label="thm:degree"} Let $p_n$ be polynomials of degree at most $m$ that converge locally uniformly on $\mathbb C$ to an entire function $f$. Then $f$ is a polynomial of degree at most $m$. If every $p_n$ is monic of degree exactly $m$, then $f$ is monic of degree $m$.

Local uniform convergence of holomorphic functions implies convergence of all derivatives on compact subsets by Cauchy's integral formula [@Conway1978]. Since $p_n^{(m+1)}\equiv0$, one has $f^{(m+1)}\equiv0$, so $f$ has degree at most $m$. In the monic degree-$m$ case, $p_n^{(m)}\equiv m!$, hence $f^{(m)}\equiv m!$.

[\[cor:four\]]{#cor:four label="cor:four"} A locally uniform nonzero limit of monic quartics has exactly four zeros on $\mathbb C$, counted with multiplicity. It cannot yield an unbounded spectral count.

On a proper domain, Rouché's theorem gives the corresponding local statement: if a compact contour avoids the zeros of the nonzero limit, the number of enclosed zeros eventually stabilizes and is bounded by four [@Conway1978].

Thus even a rigorously proved limit $$Q_{\sigma}\longrightarrow(z^2-1)^2$$ would produce one finite degenerate factor, not an infinite spectral determinant.

# Powering grows multiplicity, not support

Let $$Q(z)=\prod_{j=1}^{r}(z-\lambda_j)^{m_j},
 \qquad \sum_{j=1}^{r}m_j=4,qquad r\le4.$$ Then $$\label{eq:powerdivisor}
 Q(z)^N=\prod_{j=1}^{r}(z-\lambda_j)^{Nm_j}.$$

[\[prop:support\]]{#prop:support label="prop:support"} For every $N\ge1$, the distinct zero support of $Q^N$ is the support of $Q$ and has cardinality at most four. If $N\to\infty$, the divisors of $Q^N$ are not locally finite on any domain containing a zero of $Q$.

Equation [\[eq:powerdivisor\]](#eq:powerdivisor){reference-type="eqref" reference="eq:powerdivisor"} proves the support statement. If a compact neighborhood contains $\lambda_j$, its divisor mass is at least $Nm_j$, which diverges. Local finiteness requires finite mass on compact sets.

[\[cor:holomorphic\]]{#cor:holomorphic label="cor:holomorphic"} No sequence $Q^{N_k}$ with $N_k\to\infty$ can have zero divisors converging locally to the divisor of a nonzero holomorphic function on a domain containing a zero of $Q$.

Multiplying by nonzero scalar normalizations does not change this divisor. If the functions themselves converge locally uniformly, the only possible way to accommodate unbounded compact zero order is an identically zero limit, which is not a spectral determinant.

# Collapsing quartics do not repair local finiteness

Suppose $Q_n$ tends to $(z^2-1)^2$ and one also chooses powers $N_n\to\infty$. For any sufficiently small fixed neighborhoods of $+1$ and $-1$, all four roots of $Q_n$ eventually lie in their union. The divisor mass there is $4N_n$ and diverges. Root motion toward a compact degenerate pair therefore does not create an extended locally finite support.

To obtain a genuine growing divisor, new roots must enter new locations in a controlled manner. Their multiplicities on every fixed compact set must remain finite in the limiting object.

# Height counting profile

For a finite root multiset $\Lambda$, define $$\label{eq:count}
 N_\Lambda(T)=\sum_{\lambda\in\Lambda}
 \mathbf 1_{\{|\operatorname{Im}\lambda|\le T\}},$$ with multiplicity. For $Q^N$, $$N_{Q^N}(T)=N\,N_Q(T).$$ It has at most four distinct jump heights, independent of $N$. Increasing $N$ enlarges those jumps but does not distribute zeros over increasing height.

This cannot approximate a locally finite extended counting law as a function of $T$. In particular it does not address the $T\log T$ scale required much later in Gate C. That macro-gate is not being proved or tested here; the counting observation only explains why Gate A must not stop at one factor.

# Finite illustration

At $\sigma=0.00125$ on the left channel, the centered quartet has $$u=0.718352,\qquad \eta=-0.093030.$$ Its four roots are distinct. We form powers with $$N=1,2,4,8,16,32,64.$$

     $N$   polynomial degree   distinct support   maximum root multiplicity
  ------ ------------------- ------------------ ---------------------------
     $1$                 $4$                $4$                         $1$
     $8$                $32$                $4$                         $8$
    $32$               $128$                $4$                        $32$
    $64$               $256$                $4$                        $64$

The archive also normalizes $Q(z)^N$ at a basepoint and samples five complex locations. As expected, modulus ratios are exponentially magnified or suppressed with $N$; scalar normalization does not produce a stable divisor. This numerical display illustrates Propositions [\[prop:support\]](#prop:support){reference-type="ref" reference="prop:support"}; it is not needed for their proof.

# What a rank-growing construction must add

A viable next layer should contain divisors $$\label{eq:growing}
 D_{\sigma,k}(z)=\prod_{j=1}^{k}(z-\lambda_{\sigma,j}),
 \qquad k=k(\sigma)\longrightarrow\infty,$$ with genuinely expanding support. At minimum it must audit:

1.  conjugate closure and branch selection as $k$ grows;

2.  one global center and scale for the whole cloud;

3.  tightness of normalized empirical root measures;

4.  local uniform control of canonical products or logarithmic derivatives;

5.  omitted-factor bounds connecting successive ranks;

6.  dual-channel coherence.

Adding roots is necessary, not sufficient. Uncontrolled clouds can diverge or converge to the zero function just as repeated factors do.

# Claim boundary

The exact conclusion is a no-go for a fixed bounded-degree factor and its pure repetitions as the final growing spectral divisor. The quartet remains useful as a local branch seed, a calibration factor, and a test of channel universality.

No physical rank-growing divisor is constructed here. Gate A remains open, Gate C's counting law is untouched, and no arithmetic or zeta identification is asserted.
