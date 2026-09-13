---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-371-eight-run-distance-two-capacity-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction/main.pdf"
source_sha256: "fa2b1e37c5daf791b9d44cb424f63457014d8ca5b8293e524f66c14425a31a0e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Eight-run reduction and the cyclic pair-ledger obstruction for distance-two Mobius capacity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-371-eight-run-distance-two-capacity-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We continue the open distance-two capacity problem from RH-366. Positive signs may not occur two places apart in the raw Mobius prefix. The two path components of this constraint admit an exact finite reduction: even nonzero vertices are isolated, while every odd same-sign run has length at most eight because nine step-two odd positions contain a multiple of nine. The resulting eight alternating run frequencies give the exact capacity for every prefix. This is an all-$N$ identity, not a numerical fit. A separate period-18 ternary construction has the same complete ordered three-symbol pair ledger at every cyclic lag for two words, but capacities $10q$ and $12q$ after $q$ repetitions. The construction is a scoped negative for pair data as a sufficient statistic; it is not a Mobius sequence and does not prove that the Mobius capacity limit fails. No canonical operator, prime trace, Hilbert--Polya construction, or proof of RH is claimed.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: |
  Eight-run reduction and the cyclic pair-ledger obstruction\
  for distance-two Mobius capacity
```

## Markdown 正文

# Scope and frozen source

RH-366 fixes the open raw capacity $$K_N=\max_{\substack{\varepsilon_1,\ldots,\varepsilon_N\in\{-1,+1\}\\
 \varepsilon_n=\varepsilon_{n+2}=+1\ \text{never}}}
 \left|\sum_{n\leq N}\mu(n)\varepsilon_n\right|.
 \label{eq:capacity}$$ The optimizer is allowed to depend on the complete prefix. The frozen source gives a two-path maximum-weight-independent-set (MWIS) algorithm and the bracket $$\frac4{\pi^2}\leq\liminf_{N\to\infty}\frac{K_N}{N}
 \leq\limsup_{N\to\infty}\frac{K_N}{N}\leq\frac6{\pi^2},
 \label{eq:oldbracket}$$ but no existence theorem for the limit [@rh366; @capacitysource].

Put $M_N=\sum_{n\leq N}\mu(n)$. Starting from the all-negative word, changing a position to $+1$ adds $2\mu(n)$. Thus the positive positions form independent sets on the odd and even step-two paths. All claims below are in this scalar adaptive-capacity data type. They are not trace or determinant statements.

Finite endpoint rows reproduce an exact calculation only. The periodic words used later are synthetic ternary words, not values of $\mu$. Their cyclic pair ledger is not an open-prefix ledger. The physical route coordinate remains the frozen RH-366 same-clock coordinate.

# Exact eight-run reduction

For $\sigma\in\{-1,+1\}$ and $1\leq k\leq8$, define $$C_{\sigma,k}(N)=\#\left\{\begin{array}{l}
 n\leq N-2(k-1),\ n\text{ odd},\\
 \mu(n+2j)=\sigma\text{ for }0\leq j<k
 \end{array}\right\}.
 \label{eq:C}$$ Also define the isolated even count $$E_\sigma(N)=\#\{n\leq N:n\equiv2\pmod4,\ \mu(n)=\sigma\}.
 \label{eq:E}$$

Every odd step-two run of nonzero Mobius values having one fixed sign has length at most eight.

The nine integers $n,n+2,\ldots,n+16$ represent every residue class modulo 9, since $2$ is invertible modulo 9. One is divisible by 9 and hence has Mobius value zero. Such a zero interrupts every fixed-sign nonzero run.

Let $W_\sigma(N)$ be the sum of the positive weights in the two path MWIS problems with weights $\sigma\mu(n)$. Then for every $N\geq1$, $$W_\sigma(N)=E_\sigma(N)+
 \sum_{k=1}^{8}(-1)^{k+1}C_{\sigma,k}(N).
 \label{eq:runformula}$$ Consequently, $$S_N^{\max}=-M_N+2W_{+1}(N),\qquad
 S_N^{\min}=-M_N-2W_{-1}(N),
 \label{eq:extremes}$$ and $$K_N=\max\bigl\{|S_N^{\max}|,|S_N^{\min}|\bigr\}.
 \label{eq:Kformula}$$

If $n$ is even and $\mu(n)\ne0$, then $n\equiv2\pmod4$; the intervening multiple of four has Mobius value zero. Hence the even path contributes exactly $E_\sigma(N)$ to the MWIS for weights $\sigma\mu$. On the odd path, discard zero and opposite-sign vertices and consider one fixed-sign run of length $L$. Its MWIS contribution is $\lceil L/2\rceil$. The elementary identity $$\left\lceil\frac L2\right\rceil
 =\sum_{k=1}^{L}(-1)^{k+1}(L-k+1)
 \label{eq:ceilidentity}$$ counts the all-one intervals in that run. Summing over all runs turns the right side into the alternating interval counts in [\[eq:C\]](#eq:C){reference-type="eqref" reference="eq:C"}; the lemma truncates it at $k=8$. The baseline identity $$\sum_{n\leq N}\mu(n)\varepsilon_n
 =-M_N+2\sum_{n:\,\varepsilon_n=+1}\mu(n)$$ then gives [\[eq:extremes\]](#eq:extremes){reference-type="eqref" reference="eq:extremes"} and [\[eq:Kformula\]](#eq:Kformula){reference-type="eqref" reference="eq:Kformula"}.

Set $$R_\sigma(N)=E_\sigma(N)+
 \sum_{k=1}^{8}(-1)^{k+1}C_{\sigma,k}(N).
 \label{eq:R}$$ Then $$\left|\frac{K_N}{N}-2\max_{\sigma\in\{-1,+1\}}
 \frac{R_\sigma(N)}{N}\right|\leq\frac{|M_N|}{N}.
 \label{eq:criterionbound}$$ Since $M_N=o(N)$, the limit $K_N/N$ exists if and only if $$\max\{R_{+1}(N),R_{-1}(N)\}/N
 \label{eq:maxcriterion}$$ converges. Existence of each individual $C_{\sigma,k}(N)/N$ is sufficient, but is not necessary.

For each nonnegative $R$, the reverse triangle inequality gives $$\bigl||-M+2R|-2R\bigr|\leq|M|,
 \qquad
 \bigl||-M-2R|-2R\bigr|\leq|M|.$$ Take maxima and use [\[eq:extremes\]](#eq:extremes){reference-type="eqref" reference="eq:extremes"}. The prime number theorem gives $M_N=o(N)$, proving the equivalence.

The elementary squarefree sieve gives $\#\{m\leq X:m\text{ odd},\mu(m)^2=1\}\sim4X/\pi^2$. Writing $n=2m$ therefore shows that $E_{+1}(N)+E_{-1}(N)\sim2N/\pi^2$. If $S_{\rm odd}(X)=\sum_{m\leq X,\,m\text{ odd}}\mu(m)$, then $M_X=S_{\rm odd}(X)-S_{\rm odd}(X/2)$. Iterating this relation and using $M_X=o(X)$ gives $S_{\rm odd}(X)=o(X)$, so the two signs split equally: $$\frac{E_{+1}(N)}N,\frac{E_{-1}(N)}N\longrightarrow\frac1{\pi^2}.
 \label{eq:Edensity}$$ Thus the open part can also be written as the convergence of the maximum of the two alternating eight-run combinations after subtracting their common baseline $1/\pi^2$. No source here proves those combinations converge.

# A cyclic pair-ledger obstruction

Consider the period-18 words $$u=\texttt{+++++-++0--+-----0},\qquad
 v=\texttt{+++++---0--+---++0}.
 \label{eq:words}$$ Both have eight plus signs, eight minus signs, and zeros at positions 9 and 18. For any finite ternary weight word $w=(w_n)$, write $$K_N(w)=\max_{\varepsilon_n=\varepsilon_{n+2}=+1\ \mathrm{never}}
 \left|\sum_{n=1}^{N}w_n\varepsilon_n\right|.
 \label{eq:generalcapacity}$$ Thus [\[eq:capacity\]](#eq:capacity){reference-type="eqref" reference="eq:capacity"} is the special case $w_n=\mu(n)$. For a ternary word $w$ let $B_{ab,w}(d)$ count ordered pairs $(w_j,w_{j+d})=(a,b)$ with indices modulo 18. The complete cyclic ledger is the nine-vector $(B_{++},B_{+-},B_{+0},B_{-+},B_{--},B_{-0},B_{0+},B_{0-},B_{00})$ for each $d\in\mathbb Z/18\mathbb Z$.

The words in [\[eq:words\]](#eq:words){reference-type="eqref" reference="eq:words"} have identical cyclic ordered pair ledgers at all 18 lags. Nevertheless, for every integer $q\geq1$, $$K_{18q}(u^q)=10q,\qquad K_{18q}(v^q)=12q.
 \label{eq:periodcapacity}$$

Work in $\mathbb Z[x]/(x^{18}-1)$ and let $^*$ send $x$ to $x^{-1}$. The plus indicator polynomials and the common zero indicator are $$\begin{aligned}
 A&=1+x+x^2+x^3+x^4+x^6+x^7+x^{11},\\
 B&=1+x+x^2+x^3+x^4+x^{11}+x^{15}+x^{16},\\
 Z&=x^8+x^{17}.\end{aligned}$$ One has $A-B=x^6(1+x)(1-x^9)$ and $$(A-B)Z^*=0\pmod{x^{18}-1}.
 \label{eq:crosscert}$$ Direct expansion gives the second finite group-ring certificate $$AA^*-BB^*=0\pmod{x^{18}-1}.
 \label{eq:autocert}$$ Representing each $x^{-j}$ by $x^{18-j}$, the resulting unreduced polynomial difference is $(x^{18}-1)$ times $$-x^2(x-1)(x+1)^2(x^2+1)(x^2+x+1)(x^6+x^3+1).$$ Let $J=1+x+\cdots+x^{17}$. Cyclic multiplication by $J^*$ records only the common plus count, while [\[eq:crosscert\]](#eq:crosscert){reference-type="eqref" reference="eq:crosscert"} records the plus-zero cross terms. Since the minus indicators are $J-Z-A$ and $J-Z-B$, these identities and [\[eq:autocert\]](#eq:autocert){reference-type="eqref" reference="eq:autocert"} show that every cross-correlation among plus, minus, and zero indicators agrees. This is exactly equality of all nine ordered pair counts at every cyclic lag.

For the capacity, split each repeated word into its odd and even paths and use the run formula for a ternary word. The four parity strings and their positive/negative MWIS totals are

  word/path    repeated block   $W_+$    $W_-$
  ----------- ---------------- -------- -------
  $u$, odd       `++++0—-`       $2q$    $2q$
  $u$, even      `++-+-+–0`      $3q$    $3q$
  $v$, odd       `+++-0—+`      $2q+1$   $3q$
  $v$, even      `++—+-+0`       $3q$    $3q$

Both words have total weight zero. Therefore $u^q$ has capacity $2(5q)=10q$; for $v^q$ the two extrema are $2(5q+1)=10q+2$ and $2(6q)=12q$, and the latter is at least the former for $q\geq1$.

The ledger equality is cyclic only. At open lag two, the $++$ count is 4 for $u$ and 3 for $v$ (and the $-+$ count is 2 versus 3). The periodic words are not a Mobius sequence and do not prove that the Mobius capacity limit fails. They show only that a general periodic ternary two-point law is not a sufficient statistic for this nonlinear capacity.

# Executable audit and finite endpoint

The artifact uses a linear integer Mobius sieve, exact path dynamic programming, and the run formula. It checks all prefixes $1\leq N\leq1000$, the endpoint $N=2^{20}$, all 162 cyclic pair cells, and the repeated-word capacity identities for $1\leq q\leq256$. At the endpoint it reproduces

  ------------------------- --------------------
  $M_N$                                    $257$
  $E_{+1},E_{-1}$              $106305,\ 106183$
  $W_{+1},W_{-1}$              $258120,\ 257953$
  $S_N^{\max},S_N^{\min}$     $515983,\ -516163$
  $K_N$                                 $516163$
  ------------------------- --------------------

These are exact reproduction rows, not asymptotic evidence. The semantic PDF, source locks, and archive manifest are checked separately.

# Route verdict and Gate ledger

-   Route A is `GO`: the all-prefix eight-run theorem and the cyclic pair-ledger obstruction are independent, typed theorem edges.

-   Route B is `STOP_SCOPED`: the required Mobius run-combination convergence is absent, the optimizer is adaptive, and the periodic witness is synthetic rather than arithmetic.

The five project Gates remain false/open. This paper does not construct a canonical intrinsic dynamical spectral determinant, a scattering completion, a self-adjoint generator, a von-Mangoldt weighted trace, or equality with the completed-zeta divisor. It does not identify Riemann zeros, construct a Hilbert--Polya operator, or prove the Riemann Hypothesis.

# Conclusion

The distance-two capacity is not an uncontrolled infinite run problem: its finite-prefix value is exactly an eight-frequency arithmetic expression. The remaining obstacle is a genuine higher-order Mobius pattern theorem, not another finite fit. Cyclic pair data alone cannot replace that theorem in a general ternary model. The next route must either control the alternating eight-run envelope in the Mobius data type or supply a distinct source-backed edge.
