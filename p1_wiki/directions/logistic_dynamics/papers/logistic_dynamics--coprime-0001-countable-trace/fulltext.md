---
p1_kind: "derived-fulltext-reading-copy"
route: "logistic_dynamics"
logical_paper_id: "logistic_dynamics--coprime-0001-countable-trace"
canonical_tex: "logistic_dynamics/projects/coprime_0001_countable_trace/paper/main.tex"
canonical_pdf: "logistic_dynamics/projects/coprime_0001_countable_trace/paper/main.pdf"
source_sha256: "02eff6144a52835761a117df9f24a59d9cf7f7bb5fdca31b44c5b10e43031def"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Countable Coprime Renewal Determinant: Trace Class, Exact Cycle Ledgers, and the Operator Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../logistic_dynamics/projects/coprime_0001_countable_trace>)
- [规范 TeX](<../../../../../logistic_dynamics/projects/coprime_0001_countable_trace/paper/main.tex>)
- [关联 PDF](<../../../../../logistic_dynamics/projects/coprime_0001_countable_trace/paper/main.pdf>)
- [支撑 Markdown](<../../../../../logistic_dynamics/projects/coprime_0001_countable_trace/README.md>)
- [BibTeX](<../../../../../logistic_dynamics/projects/coprime_0001_countable_trace/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze a target-free countable renewal suspension whose symbols are integers $n\geq2$ and whose adjacent symbols are required to be coprime. The roof is $\log n$, and a symmetric half-roof convention gives the transfer kernel $$(L_s)_{mn}=\mathbf 1_{\gcd(m,n)=1}(mn)^{-s/2}.$$ For $\Re s>1$, a Möbius rank-one expansion proves local uniform trace-norm convergence, holomorphicity of the family, and existence of the same-object Fredholm determinant $D_{\rm cop}(s)=\det_F(I-L_s)$. Finite projections then give an exact cyclic trace-power formula and the primitive-repetition ledger. We certify the absence of period-one cycles, the orientation factors for periods two and three, and rational finite cutoffs through repetition power six. The boundary is sharp for the frozen $\ell^2$ realization: the $e_2$ column is not square summable when $\Re s\leq1$. These results establish an analytic Route-A theorem edge, not a prime-orbit law or a completed-$\xi$ determinant. We state the remaining continuation question without evaluating determinant roots.
author:
- Anonymous Research Team
date: August 2026
title: |
  A Countable Coprime Renewal Determinant:\
  Trace Class, Exact Cycle Ledgers, and the Operator Boundary
```

## Markdown 正文

# Introduction

The finite-state symbolic models examined in the preceding search were useful controls, but their finite exponential structure forces an $O(T)$ divisor count. A different object must therefore be infinite-dimensional before a global determinant comparison is even meaningful. This paper records the first audit of one such object: a countable shift with a local coprimality constraint and an intrinsic logarithmic roof.

The construction is deliberately modest. It asks whether the transfer operator is mathematically defined, whether its traces have a reproducible primitive-cycle interpretation, and where the defining Hilbert-space domain ends. It does not fit parameters to primes or zeros, evaluate a Fredholm determinant, or claim a Riemann spectral identity.

Our contributions are:

1.  a trace-class theorem for the frozen symmetric kernel on $\Re s>1$, obtained from a Möbius rank-one decomposition;

2.  an exact trace-power identity with primitive periods and repetitions, including closed formulas for periods one through three;

3.  a target-free finite certificate using disjoint label blocks and exact rational arithmetic through $k=6$;

4.  a sharp operator-domain observation: the same counting-measure $\ell^2$ matrix is not bounded for $\Re s\leq1$.

The resulting Route-A tuple is $$\begin{gathered}
(\mathrm{A1\_WEAK},\ \mathrm{A2\_ANALYTIC\_DETERMINANT},\\
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\ \mathrm{A4\_FAIL}).
\end{gathered}$$ The next question is scalar continuation across the operator boundary. Any such continuation must be proved as a separate object-level theorem.

# Frozen object and determinant convention

Let $$\Sigma_{\mathrm{cop}}=\left\{(n_k)_{k\in\mathbb Z}: n_k\in\{2,3,\ldots\},\
\operatorname{gcd}(n_k,n_{k+1})=1\text{ for every }k\right\}.$$ The left shift is the dynamics and the roof is $\tau((n_k))=\log n_0$.

The edge potential is split symmetrically. On $\mathcal H=\ell^2(\{2,3,\ldots\})$, with counting measure, define $$(L_s f)(m)=\sum_{\substack{n\in\{2,3,\ldots\}\\gcdop(m,n)=1}}
(mn)^{-s/2}f(n),\qquad \Re s>1.$$ The real logarithm fixes the complex powers. A cyclic word $(n_0,\ldots,n_{k-1})$ has edge product $$\prod_{j=0}^{k-1}(n_jn_{j+1})^{-s/2}
=\left(\prod_{j=0}^{k-1}n_j\right)^{-s},
\qquad n_k=n_0.$$ This identity fixes the clock, normalization, and determinant data type.

The only object used below is $$D_{\mathrm{cop}}(s)=\operatorname{det}_{F}(I-L_s).$$ The reciprocal, logarithmic derivative, a scattering determinant, and the completed Riemann function are excluded from this stage. Trace class alone does not authorize a $\lambda=1$ trace-log expansion unless a separate spectral-radius or norm bound is proved.

# Trace-class theorem

For $\sigma=\Re s>1$, $L_s$ is trace class on $\mathcal H$, and $s\mapsto L_s$ is locally uniformly holomorphic in trace norm.

Use $$\mathbf{1}_{\operatorname{gcd}(m,n)=1}=\sum_{d\mid m,n}\mu(d).$$ Set $$a_d(m)=\mathbf{1}_{d\mid m}m^{-s/2},\qquad
c_d(m)=\mathbf{1}_{d\mid m}m^{-\overline{s}/2}.$$ Then $L_s=\sum_{d\geq1}\mu(d)a_dc_d^*$. The $d$-th term is rank one and $$\lVert a_dc_d^*\rVert_1
=\lVert a_d\rVert_2\lVert c_d\rVert_2
=S_d:=\sum_{\substack{m\geq2\\d\mid m}}m^{-\sigma}.$$ Since $$\sum_{d\geq1}|\mu(d)|S_d
=\sum_{m\geq2}2^{\omega(m)}m^{-\sigma}
=\frac{\zeta(\sigma)^2}{\zeta(2\sigma)}-1<\infty,$$ the rank-one series converges in trace norm. Local uniformity on compact subsets of $\Re s>1$ follows from the same majorant with a compact lower bound for $\sigma$. Holomorphicity of each rank-one term gives the claim.

The Fredholm determinant $D_{\mathrm{cop}}(s)=\operatorname{det}_{F}(I-L_s)$ is well-defined and holomorphic on $\Re s>1$.

The theorem is a half-plane statement. It does not assert that $D_{\mathrm{cop}}$ continues through $\Re s=1$, nor does it identify a global divisor.

# Exact trace powers and primitive cycles

Let $P_N$ be the projection onto labels $2,\ldots,N$. The finite matrices $P_NL_sP_N$ have the usual cyclic trace expansion. Trace-norm convergence passes this identity to the limit; alternatively, absolute values are bounded by $(\zeta(\sigma)-1)^k$. Therefore, for every $k\geq1$, $$\operatorname{Tr}L_s^k
=\sum_{\substack{n_0,\ldots,n_{k-1}\in\{2,3,\ldots\}\\
\operatorname{gcd}(n_j,n_{j+1})=1\ {\rm cyclic}}}
\left(\prod_{j=0}^{k-1}n_j\right)^{-s}.$$

If $\gamma$ is a primitive directed cycle, write $d=|\gamma|$ and $w_\gamma=\prod_i n_i^{-s}$. Cyclic starting points give the exact ledger $$\operatorname{Tr}L_s^k
=\sum_{\substack{\gamma\ {\rm primitive}\\d\mid k}}
d\,w_\gamma^{\,k/d}.$$ The factor is the primitive period $d$, not the total power $k$.

$C_1(s)=0$, and $$C_2(s)=2\sum_{\substack{2\leq a<b\\gcdop(a,b)=1}}(ab)^{-s}
=\frac{\zeta(s)^2}{\zeta(2s)}-2\zeta(s)+1.$$ Moreover, $$C_3(s)=6\sum_{\substack{2\leq a<b<c\\
\text{pairwise coprime}}}(abc)^{-s}.$$

A self-loop would require $\operatorname{gcd}(n,n)=1$, impossible for $n\geq2$. For period two, the two cyclic starting points represent one canonical rotation class with $a<b$. For period three, cyclic admissibility is pairwise coprimality, which forces distinct labels; six ordered triples represent two directed rotations for each unordered triple.

For a symbolic closed form, define $$F_3(s)=\prod_p\frac{1+2p^{-s}}{1-p^{-s}}.$$ Inclusion--exclusion of the forbidden label $1$ gives $$C_3(s)=F_3(s)-3\frac{\zeta(s)^2}{\zeta(2s)}
+3\zeta(s)-1.$$ The Euler product is used only as a symbolic identity; no prime list is evaluated by the certificate.

# The exact operator boundary

For $\sigma=\Re s\leq1$, the frozen matrix $L_s$ is not a bounded operator on $\ell^2(\{2,3,\ldots\})$.

Apply $L_s$ to $e_2$. The only nonzero entries occur at odd $m\geq3$, and $$\lVert L_se_2\rVert_2^2
=2^{-\sigma}\sum_{\substack{m\geq3\\m\ {\rm odd}}}m^{-\sigma}.$$ The odd subseries of the p-series diverges for $\sigma\leq1$.

This is a boundary for the frozen Hilbert-space realization, not a no-go theorem for every scalar continuation. A continuation of $D_{\mathrm{cop}}$, a different Banach space, or a regularized operator would require a new source lock and a separate determinant identity. The current stage keeps all such objects outside scope.

# Exact finite certificate

The generator uses only integer gcd tests and rational weights at $s=2$. Validation uses labels $2,\ldots,10$; the sealed test uses the disjoint block $11,\ldots,18$. A separate repetition control uses labels $2,\ldots,8$ and checks powers $k=1,\ldots,6$.

::: {#tab:counts}
  label block                period 1   period 2   period 3
  ------------------------ ---------- ---------- ----------
  validation $2$--$10$            $0$       $44$      $120$
  sealed test $11$--$18$          $0$       $40$      $132$

  : Exact cyclic-word and primitive-cycle counts.
:::

For the validation block, the primitive cycle counts at periods two and three are $22$ and $40$, respectively. The exact $s=2$ inclusion-- exclusion checks return $$C_2=\frac{7591}{52920},\qquad
C_3=\frac{3637}{211680},$$ both by direct cyclic enumeration and by the finite formulas. Every row of the repetition ledger through $k=6$ agrees as a reduced Fraction. These checks certify the combinatorial and determinant conventions; they do not measure agreement with any external spectrum.

# Limitations and next theorem

The coprimality grammar is arithmetic-looking but is not a prime grammar. Nothing in the local transition rule singles out a primitive cycle for each prime, and no amplitude $\log p\,p^{-r/2}$ has been derived. The determinant is currently a half-plane Fredholm determinant, not a known entire function. Consequently there is no functional equation, Riemann--von Mangoldt counting law, completed-$\xi$ divisor equality, natural quantization, or Route-B operator.

The next smallest verifiable task is to study scalar continuation or a same-object growth obstruction at $\Re s=1$, while keeping the original $\ell^2$ operator domain and determinant convention explicit. A successful continuation would need its own theorem; a failure would be a reusable candidate-local obstruction. Root searches and comparisons with Riemann zeros are deliberately deferred.

# Proof details

## Trace-norm majorant

For $\sigma>1$, the rank-one vectors in the Möbius decomposition satisfy $$\lVert a_d\rVert_2^2=\lVert c_d\rVert_2^2
=\sum_{\substack{m\geq2\\d\mid m}}m^{-\sigma}.$$ The identity $$\sum_{d\geq1}|\mu(d)|\sum_{\substack{m\geq2\\d\mid m}}m^{-\sigma}
=\sum_{m\geq2}2^{\omega(m)}m^{-\sigma}
=\frac{\zeta(\sigma)^2}{\zeta(2\sigma)}-1$$ is absolutely convergent. It also supplies a compact-subset majorant, since $\sigma$ has a positive margin above one on every compact subset of the defining half-plane.

## Trace expansion

For a finite projection $P_N$, ordinary matrix multiplication gives $$\operatorname{Tr}(P_NL_sP_N)^k
=\sum_{\substack{n_0,\ldots,n_{k-1}\leq N\\
\operatorname{gcd}(n_j,n_{j+1})=1\ {\rm cyclic}}}
\left(\prod_jn_j\right)^{-s}.$$ The trace-norm convergence of $P_NL_sP_N$ to $L_s$ passes the trace of each fixed power to the limit. The same result follows directly from the absolute bound $(\zeta(\sigma)-1)^k$, which permits Fubini and cyclic reindexing.

## Primitive repetition factor

Every cyclic word has a unique minimal primitive period $d$ dividing its length $k$. A primitive orbit of period $d$ contributes exactly $d$ cyclic starting points, and repeating it $k/d$ times raises its weight to $w_\gamma^{k/d}$. Summing over primitive rotation classes gives the stated ledger.
