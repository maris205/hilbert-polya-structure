---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-368-parity-factor-mobius-capacity-limit"
canonical_tex: "zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit/main.pdf"
source_sha256: "8829edbf3c4f449f0a555a456e011559e3dfeeef7268dc5e8547ea42595848cb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parity-factor Möbius capacity limit

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-368-parity-factor-mobius-capacity-limit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate an exact constraint-graph theorem from a postcritically finite quadratic map. Its three-cell Markov partition has matrix $A=\left(\begin{smallmatrix}0&0&1\\0&0&1\\1&1&0\end{smallmatrix}\right)$, and the binary factor $A_{\{2\}}$ consists of words whose positive symbols lie in one parity class. For the Möbius prefix, the resulting adaptive capacity has an exact finite formula and satisfies $K_N^{(2)}/N\to4/\pi^2$. The proof uses parity Mertens cancellation and odd/even squarefree densities. This is a reduced parity factor, not the four-state distance-two constraint of RH-366. The optimizer is chosen after reading the arithmetic prefix, so no canonical operator, prime trace, Riemann-zero model, Hilbert--Polya construction, or RH implication is claimed.
author:
- RH research program
date: August 2026
title: 'Parity-factor Möbius capacity limit'
```

## Markdown 正文

# Scope and source boundary

The external source [@DynaZeta2026] proves that the restriction of $f_u(x)=1-ux^2$ at the real root $$u_c^3-2u_c^2+2u_c-2=0,
 \qquad r=u_c-1,\qquad J=[-r,1],$$ has the postcritical itinerary $$0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r.$$ The partition $I_1=[-r,0], I_2=[0,r], I_3=[r,1]$ has transition matrix $$A=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix}.
 \tag{1}$$ Labelling $I_1$ by $1$ and the other intervals by $0$ gives the factor $A_{\{2\}}$: all $1$-positions lie in one parity class. The same source records the boundary-aware factor zeta function $$\zeta_{f_{u_c}|_J}(z)=\zeta_{A_{\{2\}}}(z)=\frac{1+z}{1-2z^2},
 \tag{2}$$ but (2) is used here only as a provenance anchor.

The distinction from RH-366 is essential. RH-366 permits positive symbols on both parity paths but forbids two positives at distance two; its capacity limit is still open. Here we study a distinct, explicitly defined reduced factor $A_{\{2\}}$, where all positive positions must use one parity class.

# The finite parity-factor capacity

For $N\geq1$, write $\mu_n=\mu(n)$ and $$M_N=\sum_{n\leq N}\mu_n,
 \qquad
 P_r(N)=\#\{n\leq N:n\equiv r\pmod 2,\ \mu_n=1\},$$ $$N_r(N)=\#\{n\leq N:n\equiv r\pmod 2,\ \mu_n=-1\},
 \qquad r\in\{0,1\}.$$ Define $$K_N^{(2)}=\max_{\varepsilon\in(A_{\{2\}})_N}
 \left|\sum_{n=1}^N\mu_n\varepsilon_n\right|,
 \tag{3}$$ where $(A_{\{2\}})_N$ is the set of sign words for which the set $\{n:\varepsilon_n=+1\}$ is empty or contained in one residue class modulo $2$.

[\[prop:finite\]]{#prop:finite label="prop:finite"} For every $N$, $$K_N^{(2)}=
 \max_{r\in\{0,1\}}
 \max\bigl\{|{-M_N+2P_r(N)}|,\ |{-M_N-2N_r(N)}|\bigr\}.
 \tag{4}$$

Start with the all-negative word, whose score is $-M_N$. If positives are allowed only in parity class $r$, changing a position with $\mu_n=1$ from $-1$ to $+1$ raises the score by $2$, while changing a position with $\mu_n=-1$ lowers it by $2$. Thus the largest score in that class is $-M_N+2P_r(N)$, obtained by flipping every positive Möbius entry; the smallest is $-M_N-2N_r(N)$, obtained by flipping every negative entry. Empty or partial flips cannot improve either extremum. Taking absolute values and then the two parity classes proves (4).

# All-order limit

We use the standard consequences of the prime number theorem in arithmetic progressions and squarefree counting: $$\frac{M_N}{N}\to0,\qquad
 \frac{P_1(N)+N_1(N)}{N}\to\frac4{\pi^2},\qquad
 \frac{P_0(N)+N_0(N)}{N}\to\frac2{\pi^2}.
 \tag{5}$$ The signed parity cancellation is an independent input: Davenport's fixed frequency estimate at $\theta=1/2$ gives $$A_N=\sum_{n\le N}\mu(n)(-1)^n=o(N)
 \quad\text{(see \cite{Davenport1937}).}$$ Together with $M_N=o(N)$, this implies that the even and odd Möbius sums, $(M_N+A_N)/2$ and $(M_N-A_N)/2$, are both $o(N)$. The squarefree sieve gives the two densities in (5). Since $P_r-N_r=o(N)$ on each class, (5) gives $$\frac{P_1(N)}N,\frac{N_1(N)}N\to\frac2{\pi^2},
 \qquad
 \frac{P_0(N)}N,\frac{N_0(N)}N\to\frac1{\pi^2}.
 \tag{6}$$

[\[thm:limit\]]{#thm:limit label="thm:limit"} For the factor $A_{\{2\}}$, $$\boxed{\displaystyle \lim_{N\to\infty}\frac{K_N^{(2)}}N=\frac4{\pi^2}.}
 \tag{7}$$

By (4) and (6), the two odd-parity candidates converge after division by $N$ to $+4/\pi^2$ and $-4/\pi^2$, respectively. The two even-parity candidates converge to $+2/\pi^2$ and $-2/\pi^2$. The maximum of their absolute values therefore converges to $4/\pi^2$.

The limit in (7) is not the unresolved RH-366 capacity for the distance-two four-state survivor. It is a capacity law for the distinct reduced factor $A_{\{2\}}$; the two languages are not comparable by set inclusion. Nor does (7) turn an adaptive sign word into a nonadaptive orbit, a canonical coupling, or a trace.

# Frozen executable audit

The package checks the integer Möbius sieve, (4) against exhaustive words through $N=12$, and the source hashes. At $N=2^{20}$ it records $$K_N^{(2)}=425095,
 \qquad K_N^{(2)}/N=0.40540218353271484.$$ This row is a reproduction diagnostic only. It is not a fit and is not used to establish (7).

# Route and Gate ledger

Route A is `GO`: (1)--(7) give a source-locked PCF realization, an exact finite identity, and an all-order capacity theorem. Route B is `STOP_SCOPED`: the maximizing word reads the complete Möbius prefix, and the quantities are scalar adaptive sums. They are not a canonical dynamical determinant, a von Mangoldt prime-power trace, or a completed-zeta divisor. Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, or proof of RH follows.

9 Source package, *A postcritically finite quadratic realization of $W=2$*, source commit `7fd3a3fdd5a6`, 2026. RH-366, *Möbius orthogonality, adaptive encoding, and Parry covariance*, repository release, 2026. RH-367, *Boundary-aligned cyclic-Ulam structure and phase-local leakage*, repository release, 2026. L. Mirsky, Arithmetical pattern problems relating to divisibility by $r$th powers, *Proc. London Math. Soc.* 50 (1949), 497--508. H. Davenport, On some infinite series involving arithmetical functions (II), *Quart. J. Math.* 8 (1937), 313--320.
