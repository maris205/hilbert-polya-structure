---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-2-exact-prime-kneading-spectral-stability"
canonical_tex: "zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability/exact-prime-kneading-spectral-stability.pdf"
source_sha256: "5f2538e648c2ed850b94a03c072a3526f31bcc0c70c90639f65601507f52e532"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Prime Kneading Orbit: Sparse Admissible Repair and Fourier-Spectral Stability of Sieve Words

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability/exact-prime-kneading-spectral-stability.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-2-exact-prime-kneading-spectral-stability/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $Q_k$ be the cumulative Eratosthenes sieve word formed from the first $k$ primes, let $p=p_{k+1}$, and let $\mathcal{P}$ be the natural prime word. We prove that on the full sieve-valid horizon $[0,p^2)$ the two words disagree at exactly the $k$ sieving primes. Thus $$d_H\bigl(Q_k[0,p^2),\mathcal{P}[0,p^2)\bigr)=k,$$ so the repair density is $k/p^2\sim 1/(p\log p)$. This is an explicit sparse repair, rather than an inference from a small density of failed maximality comparisons.

  The repaired word has an exact dynamical realization. We prove directly that $\mathcal{P}$ is strictly maximal in the parity-lexicographic order and is not eventually periodic. The Milnor--Thurston realization theorem and density of hyperbolicity in the real quadratic family therefore yield a unique parameter $u_{\mathcal P}\in(1,2)$ for which the critical-value itinerary of $f_u(x)=1-u x^2$ is exactly $\mathcal{P}$. Nested prime-prefix cylinders give the numerical value $$u_{\mathcal P}=1.962717631158954623214532\ldots.$$

  We then quantify what the sparse repair preserves. For every fixed block length $r$, empirical $r$-cylinder distributions and all bounded $r$-local observables differ by $O(rk/p^2)$. Fixed-lag correlations obey the same scale. For the $\{\pm1\}$ coding, the normalized discrete periodogram measures satisfy $$\bigl\|\mu_{Q_k,p^2}-\mu_{\mathcal{P},p^2}\bigr\|_{\mathrm{TV}}
      \le \frac{2\sqrt{k}}{p}
      =O\!\left((p\log p)^{-1/2}\right).$$ We also identify the limits. The uncentered prime and sieve periodograms converge in total variation to the zero-frequency atom $\delta_0$. After empirical centering and normalization by the centered energy, the prime periodograms converge weakly to Haar measure on the circle. A standard upper-bound sieve for fixed prime pairs proves this through the vanishing of every nonzero fixed Fourier coefficient. The exact repair transfers the centered limit to $Q_k$, with total variation error $O(p^{-1/2})$. These universal limits show that finer arithmetic information, if present, must be sought at growing lags or finer spectral scales. The construction is inverse: the quadratic parameter encodes the prime word and does not independently predict primes. No claim about phase-space shadowing, transfer-operator spectra, or Riemann zeros is made.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **An Exact Prime Kneading Orbit:**\
  Sparse Admissible Repair and Fourier-Spectral Stability of Sieve Words
```

## Markdown 正文

**Keywords:** prime indicator; sieve of Eratosthenes; kneading theory; sparse repair; symbolic shadowing; periodogram; Haar measure; spectral stability.

**MSC 2020:** 37E05; 37B10; 11A41; 11N35; 42A16.

# Introduction

The Sieve of Eratosthenes admits a natural binary formulation: each prime contributes a periodic mask and the cumulative mask removes integers with a small prime factor. A proposed connection between these masks and quadratic dynamics was developed in @Wang2026Published. A subsequent rigorous reformulation separated ordered symbolic convergence, kneading realizability, and topological conjugacy [@WangReformulation2026]. That work proved unconditionally that the cumulative sieve words converge in the parity-lexicographic order to the band-merging coordinate $RLR^\infty$. It also showed that universal finite-stage admissibility is false, while the density of detected maximality defects on the physical horizon tends to zero.

Vanishing defect density is not yet a repair theorem. A failed comparison is a property of a shift of a word, not a symbol which can simply be edited. In general, a sparse collection of failed maximality comparisons need not imply small Hamming distance to the admissible language. This logical gap is important for later statistical and spectral models [@WangSequential2026; @WangSpectral2026; @WangHenon2026].

The arithmetic structure of the Eratosthenes horizon supplies a much stronger and more explicit bridge. Below $p_{k+1}^2$, the cumulative sieve correctly classifies every composite and every prime not already used as a sieve factor. Its only disagreement with the natural prime indicator occurs at the $k$ sieving primes themselves. The natural prime word is therefore an explicit sparse repair of the cumulative mask.

The second observation is dynamical. The natural prime word is not merely close to an admissible word: it is itself strictly admissible. Classical fullness of the quadratic family then realizes it as a critical itinerary. Since the word is aperiodic, density of hyperbolicity eliminates parameter plateaus and gives uniqueness. This creates an exact inverse kneading encoding of the primes and permits deterministic stability estimates for local statistics and finite Fourier spectra.

## Main results {#main-results .unnumbered}

Write $2=p_1<p_2<\cdots$ for the primes and put $p=p_{k+1}$ and $N_k=p^2$. The results are:

1.  The natural prime word $\mathcal{P}$ is strictly self-admissible and aperiodic. There is a unique $u_{\mathcal P}\in(1,2)$ such that $$K(f_{u_{\mathcal P}})=\mathcal{P},
            \qquad f_u(x)=1-u x^2.$$

2.  The cumulative sieve word has the exact repair identity $$\{0\le n<N_k:Q_k(n)\ne\mathcal{P}(n)\}
            =\{p_1,\ldots,p_k\}.$$ Hence $d_H=k$ and $d_H/N_k\sim1/(p\log p)$.

3.  If $\Phi$ depends on $r$ consecutive symbols, then its empirical averages along $Q_k$ and the exact quadratic itinerary $\mathcal{P}$ differ by at most $$\frac{2r\|\Phi\|_\infty k}{N_k-r+1}.$$

4.  For the $\{\pm1\}$ coding and lag $\tau<N_k$, the finite correlations satisfy $$|C_\tau(Q_k;N_k)-C_\tau(\mathcal{P};N_k)|
            \le \frac{4k}{N_k-\tau}.$$

5.  The normalized Fourier periodogram measures satisfy $$\|\mu_{Q_k,N_k}-\mu_{\mathcal{P},N_k}\|_{\mathrm{TV}}
            \le 2\sqrt{\frac{k}{N_k}}
            =\frac{2\sqrt{k}}{p}.$$ Along any fixed subsequence, weak convergence of one sequence of periodogram measures implies convergence of the other to the same limit.

6.  The uncentered measures have the explicit total-variation limit $$\mu_{\mathcal{P},N}\longrightarrow\delta_0,
            \qquad
            \mu_{Q_k,N_k}\longrightarrow\delta_0.$$ If the symbol vectors are instead centered by their empirical means and the periodograms are normalized by centered energy, then $$\mu^{\circ}_{\mathcal{P},N}\Rightarrow m_{\mathbb{T}},
            \qquad
            \mu^{\circ}_{Q_k,N_k}\Rightarrow m_{\mathbb{T}},$$ where $m_{\mathbb{T}}$ is normalized Haar measure. Moreover, $$\|\mu^{\circ}_{Q_k,N_k}-\mu^{\circ}_{\mathcal{P},N_k}\|_{\mathrm{TV}}
            =O(p^{-1/2}).$$

Every theorem above is unconditional. The identification of the centered limit uses only the prime number theorem and the standard upper-bound sieve for prime pairs; no prime-pair asymptotic or unproved gap hypothesis is required.

# Symbolic and arithmetic setup

## Parity-lexicographic order

Let $\Sigma=\{L,R\}^{\mathbb{N}_0}$ and let $\sigma$ denote the left shift. The base order is $L<R$.

[\[def:parity-order\]]{#def:parity-order label="def:parity-order"} Let $S,T\in\Sigma$ be distinct and let $$j=\min\{n\ge0:S(n)\ne T(n)\}.$$ If the common prefix $S[0,j)=T[0,j)$ contains an even number of $R$ symbols, compare $S(j)$ and $T(j)$ by $L<R$. If it contains an odd number, reverse the comparison. The resulting order is denoted by $\prec$.

An endpoint-free word $S$ is *strictly self-admissible* if $$\label{eq:strict-admissibility}
    \sigma^m S\prec S\qquad(m\ge1).$$ For nonperiodic two-symbol itineraries, this is the strict MSS maximality condition. It is equivalent to admissibility of the associated kneading determinant under the standard change from itinerary symbols to cumulative orientation signs; see @MilnorThurston1988 and @deMeloVanStrien1993. Some conventions code the critical point rather than the critical value, or interchange $L$ and $R$; these changes do not affect the arguments below.

For two finite words $S,T$ of the same length $N$, define $$\label{eq:hamming}
    d_H(S,T)=|\{0\le n<N:S(n)\ne T(n)\}|.$$

## Cumulative sieve and natural prime words

Let $$P_k=\prod_{j=1}^k p_j.$$ The cumulative sieve word $Q_k\in\Sigma$ is $$\label{eq:Qk}
    Q_k(0)=R,
    \qquad
    Q_k(n)=
    \begin{cases}
        L,&\gcd(n,P_k)=1,\\
        R,&\gcd(n,P_k)>1,
    \end{cases}
    \quad n\ge1.$$ The natural prime word $\mathcal{P}\in\Sigma$ is $$\label{eq:prime-word}
    \mathcal{P}(0)=R,
    \qquad \mathcal{P}(1)=L,
    \qquad
    \mathcal{P}(n)=
    \begin{cases}
        L,&n\text{ is prime},\\
        R,&n\text{ is composite},
    \end{cases}
    \quad n\ge2.$$ The seed $\mathcal{P}(1)=L$ is the normalization inherited from the sieve word; from index $2$ onward, $L$ is exactly the prime indicator.

Let $p=p_{k+1}$. The half-open interval $$\label{eq:physical-horizon}
    [0,N_k),\qquad N_k=p_{k+1}^2,$$ is the full validity horizon for sieving by primes smaller than $p$. The endpoint $p^2$ is excluded: it is the first composite whose least prime factor is not among $p_1,\ldots,p_k$.

# The exact prime word is a unique quadratic kneading invariant

[\[prop:prime-admissible\]]{#prop:prime-admissible label="prop:prime-admissible"} For every $m\ge1$, $$\sigma^m\mathcal{P}\prec\mathcal{P}.$$

If $\mathcal{P}(m)=L$, then the shift starts with $L$ while $\mathcal{P}$ starts with $R$, so the comparison is decided at position $0$ in the base order and the shift is smaller.

Suppose $\mathcal{P}(m)=R$. Then $m\ge4$ is composite. Both words begin with $R$, so the order is reversed at the next disagreement. If $\mathcal{P}(m+1)=R$, position $1$ compares the shifted $R$ with $\mathcal{P}(1)=L$; in the reversed order the shifted word is smaller.

If $\mathcal{P}(m+1)=L$, then $m+1$ is an odd prime at least $5$, hence $m+2$ is even and composite. The two words agree as $RL$ at positions $0,1$. Their common prefix still contains one $R$, and at position $2$ the shifted symbol $R$ is smaller, in the reversed order, than $\mathcal{P}(2)=L$. Every nonzero shift is therefore defeated by position $2$ at the latest.

[\[prop:prime-aperiodic\]]{#prop:prime-aperiodic label="prop:prime-aperiodic"} The word $\mathcal{P}$ is not eventually periodic.

Suppose that $\mathcal{P}(n+T)=\mathcal{P}(n)$ for every $n\ge n_0$ and some $T\ge1$. Choose a prime $q>n_0$. Then $\mathcal{P}(q)=L$, and periodicity gives $$\mathcal{P}(q+qT)=\mathcal{P}(q)=L.$$ But $q+qT=q(1+T)$ is composite and is larger than $n_0$, a contradiction.

For $0<u\le2$, let $$\label{eq:quadratic-family}
    f_u(x)=1-u x^2.$$ Starting at the critical value $x_0=1$, put $x_{n+1}=f_u(x_n)$ and code $x_n>0$ by $R$ and $x_n<0$ by $L$. The resulting word, when the orbit never reaches $0$, is denoted by $K(f_u)$.

[\[thm:unique-realization\]]{#thm:unique-realization label="thm:unique-realization"} There is a unique parameter $u_{\mathcal P}\in(1,2)$ such that $$\label{eq:prime-kneading}
    K(f_{u_{\mathcal P}})=\mathcal{P}.$$

By [\[prop:prime-admissible\]](#prop:prime-admissible){reference-type="ref" reference="prop:prime-admissible"}, $\mathcal{P}$ satisfies the strict, nonperiodic MSS admissibility condition. The realization theorem of @MilnorThurston1988 [Thm. 12.1] states that every admissible kneading invariant occurs in the real quadratic family. Equivalently, there is a logistic parameter $b\in(2,4]$ such that the critical-value itinerary of $$g_b(t)=b t(1-t)$$ is $\mathcal{P}$. The restriction $b>2$ follows from the first symbol $\mathcal{P}(0)=R$, since the critical value $b/4$ must lie to the right of the critical point $1/2$.

We next prove uniqueness. The kneading invariant is monotone in $b$ [@MilnorThurston1988 Thm. 13.1]. If $b_1<b_2$ both realized the aperiodic word $\mathcal{P}$, monotonicity would force every parameter in $[b_1,b_2]$ to have the same kneading invariant. Hyperbolic parameters are dense in the real logistic family [@GraczykSwiatek1997]. Hence the interval would contain a map with an attracting periodic orbit, whose critical itinerary is eventually periodic, contradicting [\[prop:prime-aperiodic\]](#prop:prime-aperiodic){reference-type="ref" reference="prop:prime-aperiodic"}. Thus $b=b_{\mathcal P}$ is unique.

Finally define the orientation-preserving affine coordinate $$h_b(t)=\frac{4}{b-2}\left(t-\frac12\right).$$ A direct calculation gives $$\label{eq:logistic-conjugacy}
    h_b\circ g_b\circ h_b^{-1}(x)=1-u x^2,
    \qquad
    u=\frac{b(b-2)}4.$$ The map $b\mapsto b(b-2)/4$ is strictly increasing on $(2,4]$, so existence and uniqueness transfer to $u_{\mathcal P}$. Since the second symbol of $\mathcal{P}$ is $L$, one has $f_{u_{\mathcal P}}(1)=1-u_{\mathcal P}<0$, and hence $u_{\mathcal P}>1$.

[\[rem:inverse\]]{#rem:inverse label="rem:inverse"} The parameter $u_{\mathcal P}$ is selected by the complete prime word through inverse kneading theory. Equation [\[eq:prime-kneading\]](#eq:prime-kneading){reference-type="eqref" reference="eq:prime-kneading"} is therefore an exact deterministic encoding, but it is not an independent generator of the primes. Determining $u_{\mathcal P}$ to enough precision to recover a long prime prefix already uses that prefix.

# Exact sparse repair on the quadratic sieve horizon

[\[thm:exact-repair\]]{#thm:exact-repair label="thm:exact-repair"} Let $p=p_{k+1}$ and $N_k=p^2$. Then $$\label{eq:difference-set}
    \{0\le n<N_k:Q_k(n)\ne\mathcal{P}(n)\}
    =\{p_1,p_2,\ldots,p_k\}.$$ Consequently, $$\label{eq:exact-hamming}
    d_H\bigl(Q_k[0,N_k),\mathcal{P}[0,N_k)\bigr)=k.$$

The words agree at $0$ and $1$. Let $2\le n<p^2$.

If $n$ is composite, its least prime factor is at most $\sqrt n<p$. That factor is one of $p_1,\ldots,p_k$, so $\gcd(n,P_k)>1$ and both words mark $n$ by $R$.

If $n$ is prime and $n<p$, then $n\in\{p_1,\ldots,p_k\}$. The cumulative mask marks the sieve factor itself by $R$, whereas the natural prime word marks it by $L$.

If $n$ is prime and $n\ge p$, then $n$ is coprime to $P_k$, so both words mark it by $L$. These cases prove [\[eq:difference-set\]](#eq:difference-set){reference-type="eqref" reference="eq:difference-set"}, and [\[eq:exact-hamming\]](#eq:exact-hamming){reference-type="eqref" reference="eq:exact-hamming"} follows.

[\[cor:repair-density\]]{#cor:repair-density label="cor:repair-density"} The exact repair density satisfies $$\label{eq:repair-rate}
    \frac{d_H(Q_k[0,N_k),\mathcal{P}[0,N_k))}{N_k}
    =\frac{k}{p_{k+1}^2}\longrightarrow 0.$$ More precisely, the prime number theorem gives $$\label{eq:repair-pnt}
    \frac{k}{p_{k+1}^2}
    \sim\frac{1}{p_{k+1}\log p_{k+1}}.$$

The elementary inequality $k<p_{k+1}$ already makes the ratio in [\[eq:repair-rate\]](#eq:repair-rate){reference-type="eqref" reference="eq:repair-rate"} at most $1/p_{k+1}$. The sharper relation [\[eq:repair-pnt\]](#eq:repair-pnt){reference-type="eqref" reference="eq:repair-pnt"} follows from $k=\pi(p_k)$ and the prime number theorem; see, for example, @MontgomeryVaughan2007.

Combining [\[thm:unique-realization,thm:exact-repair\]](#thm:unique-realization,thm:exact-repair){reference-type="ref" reference="thm:unique-realization,thm:exact-repair"} gives an exact form of symbolic shadowing.

[\[cor:symbolic-shadowing\]]{#cor:symbolic-shadowing label="cor:symbolic-shadowing"} On $[0,N_k)$, the sieve word $Q_k$ differs in exactly $k$ symbols from the critical-value itinerary of the single quadratic map $f_{u_{\mathcal P}}$.

The defect-density theorem in @WangReformulation2026 counts shifts which defeat a finite maximality comparison. It does not, by itself, identify symbols whose modification repairs all comparisons. The present repair is obtained independently from the arithmetic validity of Eratosthenes sieving below $p^2$. The repair word is explicit, globally admissible, and realized by one fixed quadratic parameter.

# Stability of cylinders and local observables

We first record a general finite-word estimate. Let $S,T\in\{L,R\}^N$ and fix $1\le r\le N$. For $w\in\{L,R\}^r$, define the empirical $r$-block distribution $$\label{eq:block-distribution}
    \nu_{S,N}^{(r)}(w)
    =\frac{1}{N-r+1}
      \bigl|\{0\le n\le N-r:S[n,n+r)=w\}\bigr|.$$

[\[thm:block-stability\]]{#thm:block-stability label="thm:block-stability"} If $d=d_H(S,T)$, then $$\label{eq:block-tv}
    \bigl\|\nu_{S,N}^{(r)}-\nu_{T,N}^{(r)}\bigr\|_{\mathrm{TV}}
    \le \min\left\{1,\frac{rd}{N-r+1}\right\}.$$ Equivalently, for every bounded function $\Phi:\{L,R\}^r\to\mathbb C$, $$\label{eq:local-observable}
\begin{split}
    \left|
    \frac{1}{N-r+1}\sum_{n=0}^{N-r}\Phi(S[n,n+r))
    -\frac{1}{N-r+1}\sum_{n=0}^{N-r}\Phi(T[n,n+r))
    \right|\\
    \le \frac{2r\|\Phi\|_\infty d}{N-r+1}.
\end{split}$$

A mismatched symbol at index $j$ can affect only those length-$r$ windows whose starting index lies in $[j-r+1,j]$. There are at most $r$ such windows. Hence no more than $rd$ of the $N-r+1$ windows can differ.

Replacing one observed block by another changes the $\ell^1$ distance between empirical distributions by at most $2/(N-r+1)$. Therefore the total variation distance, one half of the $\ell^1$ distance, is bounded by $rd/(N-r+1)$, with the trivial upper bound $1$. For [\[eq:local-observable\]](#eq:local-observable){reference-type="eqref" reference="eq:local-observable"}, each affected summand changes by at most $2\|\Phi\|_\infty$.

[\[cor:prime-blocks\]]{#cor:prime-blocks label="cor:prime-blocks"} Let $N_k=p_{k+1}^2$. Then $$\label{eq:prime-block-bound}
    \bigl\|\nu_{Q_k,N_k}^{(r)}-\nu_{\mathcal{P},N_k}^{(r)}\bigr\|_{\mathrm{TV}}
    \le\frac{rk}{N_k-r+1}.$$ For every fixed $r$, the right-hand side is $$O\!\left(\frac{r}{p_{k+1}\log p_{k+1}}\right).$$ The same estimates compare $Q_k$ with the first $N_k$ symbols of $K(f_{u_{\mathcal P}})$.

Thus every fixed finite pattern statistic is stable under the exact repair. The statement is simultaneous for all $2^r$ cylinders and does not require the existence of a limiting prime-block distribution.

# Correlation stability

Encode a word $S$ by $$\label{eq:pm-encoding}
    a_n(S)=
    \begin{cases}
        +1,&S(n)=L,\\
        -1,&S(n)=R.
    \end{cases}$$ For a word of length $N$ and $0\le\tau<N$, define the finite correlation $$\label{eq:correlation}
    C_\tau(S;N)
    =\frac{1}{N-\tau}
      \sum_{n=0}^{N-\tau-1}a_n(S)a_{n+\tau}(S).$$

[\[thm:correlation-stability\]]{#thm:correlation-stability label="thm:correlation-stability"} If $S,T\in\{L,R\}^N$ and $d_H(S,T)=d$, then $$\label{eq:correlation-bound}
    |C_\tau(S;N)-C_\tau(T;N)|
    \le\min\left\{2,\frac{4d}{N-\tau}\right\}.$$

A mismatch at one index can affect at most two products in [\[eq:correlation\]](#eq:correlation){reference-type="eqref" reference="eq:correlation"}: one in which the index is the left endpoint and one in which it is the right endpoint. Hence at most $2d$ products are affected. Each product lies in $\{\pm1\}$ and changes by at most $2$, giving [\[eq:correlation-bound\]](#eq:correlation-bound){reference-type="eqref" reference="eq:correlation-bound"} after division by $N-\tau$.

[\[cor:prime-correlations\]]{#cor:prime-correlations label="cor:prime-correlations"} For $N_k=p_{k+1}^2$, $$\label{eq:prime-correlation-bound}
    |C_\tau(Q_k;N_k)-C_\tau(\mathcal{P};N_k)|
    \le \frac{4k}{N_k-\tau}.$$ Uniformly for $0\le\tau\le\alpha N_k$, where $0\le\alpha<1$ is fixed, the right-hand side is $$O_\alpha\!\left(\frac{1}{p_{k+1}\log p_{k+1}}\right).$$

The estimate includes fixed lags and lags growing as any fixed fraction below the horizon. It does not assert that the prime correlations themselves converge; it says that the cumulative sieve and exact quadratic itinerary have the same asymptotic correlation behavior whenever either limit exists.

# Fourier-periodogram stability

Let $S\in\{L,R\}^N$ and use the encoding [\[eq:pm-encoding\]](#eq:pm-encoding){reference-type="eqref" reference="eq:pm-encoding"}. Its unitary discrete Fourier transform is $$\label{eq:dft}
    \widehat a_j(S)
    =\frac{1}{\sqrt N}\sum_{n=0}^{N-1}
      a_n(S)e^{-2\pi i jn/N},
    \qquad 0\le j<N.$$ Define the normalized periodogram measure on $\mathbb{T}=\mathbb{R}/\mathbb Z$ by $$\label{eq:periodogram-measure}
    \mu_{S,N}
    =\frac1N\sum_{j=0}^{N-1}
      |\widehat a_j(S)|^2\,\delta_{j/N}.$$ Parseval's identity and $|a_n(S)|=1$ show that $\mu_{S,N}$ is a probability measure.

[\[thm:periodogram-stability\]]{#thm:periodogram-stability label="thm:periodogram-stability"} Let $S,T\in\{L,R\}^N$ and put $d=d_H(S,T)$. Then $$\label{eq:periodogram-tv}
    \|\mu_{S,N}-\mu_{T,N}\|_{\mathrm{TV}}
    \le 2\sqrt{\frac dN}.$$

The two encoded vectors differ by $2$ in absolute value at precisely $d$ coordinates, so $$\|a(S)-a(T)\|_2=2\sqrt d.$$ The discrete Fourier transform in [\[eq:dft\]](#eq:dft){reference-type="eqref" reference="eq:dft"} is unitary. Hence $$\label{eq:parseval-difference}
    \|\widehat a(S)-\widehat a(T)\|_2=2\sqrt d,
    \qquad
    \|\widehat a(S)\|_2=\|\widehat a(T)\|_2=\sqrt N.$$ On the common Fourier grid, twice the total variation distance equals the $\ell^1$ distance between the weights. By Cauchy--Schwarz, $$\begin{aligned}
    2\|\mu_{S,N}-\mu_{T,N}\|_{\mathrm{TV}}
    &=\frac1N\sum_{j=0}^{N-1}
      \left||\widehat a_j(S)|^2-|\widehat a_j(T)|^2\right|\\
    &\le\frac1N
      \bigl(\|\widehat a(S)\|_2+\|\widehat a(T)\|_2\bigr)
      \|\widehat a(S)-\widehat a(T)\|_2\\
    &=4\sqrt{\frac dN}.\end{aligned}$$ Dividing by $2$ proves [\[eq:periodogram-tv\]](#eq:periodogram-tv){reference-type="eqref" reference="eq:periodogram-tv"}.

[\[cor:prime-periodogram\]]{#cor:prime-periodogram label="cor:prime-periodogram"} At $N_k=p_{k+1}^2$, $$\label{eq:prime-periodogram}
    \|\mu_{Q_k,N_k}-\mu_{\mathcal{P},N_k}\|_{\mathrm{TV}}
    \le\frac{2\sqrt{k}}{p_{k+1}}
    =O\!\left(\frac1{\sqrt{p_{k+1}\log p_{k+1}}}\right).$$ Consequently, along any subsequence $k_j$, the measures $\mu_{Q_{k_j},N_{k_j}}$ converge weakly if and only if $\mu_{\mathcal{P},N_{k_j}}$ converge weakly, and their limits are equal.

Insert $d=k$ and $N_k=p_{k+1}^2$ into [\[thm:periodogram-stability\]](#thm:periodogram-stability){reference-type="ref" reference="thm:periodogram-stability"}. The rate follows from the prime number theorem. Total variation convergence to zero implies equality of all weak subsequential limits.

## The uncentered limit is a zero-frequency atom

The uncentered limit can be identified exactly, because primes have density zero.

[\[thm:uncentered-limit\]]{#thm:uncentered-limit label="thm:uncentered-limit"} Put $$\label{eq:prime-count-rN}
    r_N=1+\pi(N-1),$$ where the extra term counts the seed $\mathcal{P}(1)=L$. Then $$\label{eq:prime-delta0-tv}
    \|\mu_{\mathcal{P},N}-\delta_0\|_{\mathrm{TV}}
    =4\frac{r_N}{N}\left(1-\frac{r_N}{N}\right)
    \sim\frac4{\log N}.$$ At $N_k=p_{k+1}^2$ one also has $$\label{eq:sieve-delta0-tv}
    \|\mu_{Q_k,N_k}-\delta_0\|_{\mathrm{TV}}
    =4\frac{r_{N_k}-k}{N_k}
      \left(1-\frac{r_{N_k}-k}{N_k}\right)
    \sim\frac4{\log N_k}.$$ In particular, both uncentered periodograms converge to $\delta_0$ in total variation.

If a length-$N$ word has $r$ symbols equal to $L$, then its empirical mean is $2r/N-1$. Hence the mass of its periodogram at zero is $$\frac1N|\widehat a_0|^2
    =\left(2\frac rN-1\right)^2.$$ For any probability measure $\nu$, one has $\|\nu-\delta_0\|_{\mathrm{TV}}=1-\nu(\{0\})$. It follows exactly that $$\label{eq:exact-uncentered-tv-general}
    \|\mu_{S,N}-\delta_0\|_{\mathrm{TV}}
    =1-\left(2\frac rN-1\right)^2
    =4\frac rN\left(1-\frac rN\right).$$ For $\mathcal{P}[0,N)$, one has $r=r_N$. On the physical horizon, [\[thm:exact-repair\]](#thm:exact-repair){reference-type="ref" reference="thm:exact-repair"} changes precisely $k$ of those $L$ symbols to $R$, so $Q_k[0,N_k)$ has $r_{N_k}-k$ symbols equal to $L$. Substitution into [\[eq:exact-uncentered-tv-general\]](#eq:exact-uncentered-tv-general){reference-type="eqref" reference="eq:exact-uncentered-tv-general"} proves the identities, and the asymptotics follow from the prime number theorem.

Thus the uncentered normalization has a limit, but the limit records only the mean background symbol. To remove this zero-frequency dominance, define the empirical mean, centered vector, and centered energy by $$\label{eq:centered-vector}
    \bar a_N(S)=\frac1N\sum_{n=0}^{N-1}a_n(S),
    \qquad
    a_n^{\circ}(S)=a_n(S)-\bar a_N(S),
    \qquad
    E_N(S)=\sum_{n=0}^{N-1}|a_n^{\circ}(S)|^2.$$ Whenever $E_N(S)>0$, let $$\label{eq:centered-periodogram}
    \mu^{\circ}_{S,N}
    =\frac1{E_N(S)}\sum_{j=0}^{N-1}
      |\widehat a_j^{\circ}(S)|^2\,\delta_{j/N},$$ where $\widehat a^{\circ}$ is the unitary discrete Fourier transform. Parseval's identity makes [\[eq:centered-periodogram\]](#eq:centered-periodogram){reference-type="eqref" reference="eq:centered-periodogram"} a probability measure, and its zero-frequency mass is zero.

[\[prop:mean-atom-decomposition\]]{#prop:mean-atom-decomposition label="prop:mean-atom-decomposition"} For every nonconstant word $S\in\{L,R\}^N$, $$\label{eq:mean-atom-decomposition}
    \mu_{S,N}
    =\bar a_N(S)^2\delta_0
     +\frac{E_N(S)}N\mu^{\circ}_{S,N},
    \qquad
    \frac{E_N(S)}N=1-\bar a_N(S)^2.$$ If $S$ has $r$ symbols equal to $L$, then $$\label{eq:binary-centered-energy}
    \bar a_N(S)=2\frac rN-1,
    \qquad
    E_N(S)=4r\left(1-\frac rN\right).$$

Subtracting the empirical mean changes only the zero-frequency Fourier coefficient: $\widehat a_0(S)=\sqrt N\,\bar a_N(S)$, whereas $\widehat a_0^{\circ}(S)=0$, and $\widehat a_j^{\circ}(S)=\widehat a_j(S)$ for $j\ne0$. This proves the measure decomposition. Parseval and $|a_n(S)|=1$ give $E_N(S)=N-N\bar a_N(S)^2$. The formulas in [\[eq:binary-centered-energy\]](#eq:binary-centered-energy){reference-type="eqref" reference="eq:binary-centered-energy"} follow by counting the two symbol values.

[\[thm:centered-stability\]]{#thm:centered-stability label="thm:centered-stability"} Let $S,T\in\{L,R\}^N$ have positive centered energies and let $d=d_H(S,T)$. Then $$\label{eq:centered-tv-bound}
    \|\mu^{\circ}_{S,N}-\mu^{\circ}_{T,N}\|_{\mathrm{TV}}
    \le
    \frac{4\sqrt d}{\min\{\sqrt{E_N(S)},\sqrt{E_N(T)}\}}.$$

Let $P_N$ be the orthogonal projection in $\mathbb C^N$ onto the orthogonal complement of the constant vector. Centering is exactly the operation $a^{\circ}(S)=P_Na(S)$. Therefore $$\label{eq:centered-vector-difference}
    \|a^{\circ}(S)-a^{\circ}(T)\|_2
    \le \|a(S)-a(T)\|_2
    =2\sqrt d.$$ For nonzero vectors $v,w$ in a Hilbert space, $$\label{eq:normalized-vector-bound}
    \left\|\frac v{\|v\|_2}-\frac w{\|w\|_2}\right\|_2
    \le \frac{2\|v-w\|_2}{\min\{\|v\|_2,\|w\|_2\}}.$$ Apply this inequality after the unitary discrete Fourier transform. If $u$ and $v$ are the resulting normalized Fourier-amplitude vectors, then $$\frac12\sum_j\bigl||u_j|^2-|v_j|^2\bigr|
    \le \frac12(\|u\|_2+\|v\|_2)\|u-v\|_2
    =\|u-v\|_2.$$ Together with [\[eq:centered-vector-difference\]](#eq:centered-vector-difference){reference-type="eqref" reference="eq:centered-vector-difference"} and [\[eq:normalized-vector-bound\]](#eq:normalized-vector-bound){reference-type="eqref" reference="eq:normalized-vector-bound"}, this is [\[eq:centered-tv-bound\]](#eq:centered-tv-bound){reference-type="eqref" reference="eq:centered-tv-bound"}.

## The centered prime spectrum is Haar

The lower bound on centered energy and the limiting measure can both be obtained unconditionally. Write $m_{\mathbb{T}}$ for normalized Haar measure on $\mathbb{T}$ and use the Fourier convention $$\widehat\nu(h)=\int_{\mathbb{T}}e^{2\pi i h x}\,d\nu(x),
    \qquad h\in\mathbb Z.$$

[\[thm:centered-prime-haar\]]{#thm:centered-prime-haar label="thm:centered-prime-haar"} As $N\to\infty$, $$\label{eq:prime-haar-limit}
    \mu^{\circ}_{\mathcal{P},N}\Rightarrow m_{\mathbb{T}}.$$ More precisely, for every fixed nonzero integer $h$, $$\label{eq:fixed-fourier-decay}
    \widehat{\mu^{\circ}_{\mathcal{P},N}}(h)
    =O_h\!\left(\frac1{\log N}\right).$$

Let $x_n$ be $1$ when $n=1$ or $n$ is prime, and $0$ otherwise, for $0\le n<N$. Thus $a_n(\mathcal{P})=2x_n-1$. With $$\rho_N=\frac1N\sum_{n<N}x_n=\frac{r_N}{N},$$ one has $$\label{eq:prime-centered-energy}
    a_n^{\circ}(\mathcal{P})=2(x_n-\rho_N),
    \qquad
    E_N(\mathcal{P})=4N\rho_N(1-\rho_N)
    \sim\frac{4N}{\log N}.$$

Fix $h\ge1$. All indices below are read modulo $N$, and put $$A_N(h)=\sum_{n=0}^{N-1}x_nx_{n+h\bmod N}.$$ Only $O_h(1)$ terms wrap around the endpoint. The standard upper-bound sieve for the pair of linear forms $n$ and $n+h$ gives $$\label{eq:prime-pair-upper-bound}
    A_N(h)\ll_h\frac{N}{(\log N)^2};$$ see, for example, @IwaniecKowalski2004 [Chapter 6]. This estimate is only an upper bound; no twin-prime or Hardy--Littlewood asymptotic is used.

The discrete Wiener--Khinchin identity and [\[eq:prime-centered-energy\]](#eq:prime-centered-energy){reference-type="eqref" reference="eq:prime-centered-energy"} give $$\begin{aligned}
    \widehat{\mu^{\circ}_{\mathcal{P},N}}(h)
    &=\frac1{E_N(\mathcal{P})}
      \sum_{n=0}^{N-1}a_n^{\circ}(\mathcal{P})
      a_{n+h\bmod N}^{\circ}(\mathcal{P})\notag\\
    &=\frac{A_N(h)-N\rho_N^2}
      {N\rho_N(1-\rho_N)}.
    \label{eq:prime-wiener-khinchin}\end{aligned}$$ By the prime number theorem, $\rho_N\sim1/\log N$. Combining this with [\[eq:prime-pair-upper-bound\]](#eq:prime-pair-upper-bound){reference-type="eqref" reference="eq:prime-pair-upper-bound"} proves [\[eq:fixed-fourier-decay\]](#eq:fixed-fourier-decay){reference-type="eqref" reference="eq:fixed-fourier-decay"}. The same conclusion for negative $h$ follows by conjugation, while the zeroth coefficient is $1$. Hence the Fourier coefficients converge pointwise to those of $m_{\mathbb{T}}$. Density of the trigonometric polynomials in $C(\mathbb{T})$ proves [\[eq:prime-haar-limit\]](#eq:prime-haar-limit){reference-type="eqref" reference="eq:prime-haar-limit"}.

[\[cor:centered-sieve-haar\]]{#cor:centered-sieve-haar label="cor:centered-sieve-haar"} Put $p=p_{k+1}$, $N=N_k=p^2$, $M=r_N$, and $m=M-k$. Then $$\label{eq:centered-prime-sieve-tv}
\begin{split}
    \|\mu^{\circ}_{Q_k,N}-\mu^{\circ}_{\mathcal{P},N}\|_{\mathrm{TV}}
    &\le
    \left(
      2-2\sqrt{\frac{m(N-M)}{M(N-m)}}
    \right)^{1/2}\\
    &=\frac{\sqrt2+o(1)}{\sqrt p}.
\end{split}$$ Consequently, $$\label{eq:sieve-haar-limit}
    \mu^{\circ}_{Q_k,N_k}\Rightarrow m_{\mathbb{T}}.$$

Let $A\subset\{0,\ldots,N-1\}$ be the set of $L$ positions of $\mathcal{P}$ and let $B$ be the corresponding set for $Q_k$. The exact repair identity gives $B\subset A$, $|A|=M$, and $|B|=m$. Put $$x_A=\mathbf{1}_A-\frac MN\mathbf{1},
    \qquad
    x_B=\mathbf{1}_B-\frac mN\mathbf{1}.$$ The centered symbol vectors are $2x_A$ and $2x_B$. Direct calculation, using $B\subset A$, gives $$\|x_A\|_2^2=\frac{M(N-M)}N,
    \qquad
    \|x_B\|_2^2=\frac{m(N-m)}N,
    \qquad
    \langle x_A,x_B\rangle=\frac{m(N-M)}N.$$ Hence the squared distance between the normalized centered vectors is $$\label{eq:exact-normalized-repair-distance}
    \left\|
      \frac{x_A}{\|x_A\|_2}-\frac{x_B}{\|x_B\|_2}
    \right\|_2^2
    =2-2\sqrt{\frac{m(N-M)}{M(N-m)}}.$$ As in the proof of [\[thm:centered-stability\]](#thm:centered-stability){reference-type="ref" reference="thm:centered-stability"}, unitarity of the discrete Fourier transform and Cauchy--Schwarz bound the total variation distance of the squared Fourier amplitudes by the vector distance in [\[eq:exact-normalized-repair-distance\]](#eq:exact-normalized-repair-distance){reference-type="eqref" reference="eq:exact-normalized-repair-distance"}. This proves the first line of [\[eq:centered-prime-sieve-tv\]](#eq:centered-prime-sieve-tv){reference-type="eqref" reference="eq:centered-prime-sieve-tv"}.

The prime number theorem gives $$\frac{k}{M}\sim\frac2p,
    \qquad
    \frac{k}{N-M}=o(p^{-1}).$$ Since $$\sqrt{\frac{m(N-M)}{M(N-m)}}
    =\sqrt{\frac{1-k/M}{1+k/(N-M)}},$$ a first-order expansion proves the second line of [\[eq:centered-prime-sieve-tv\]](#eq:centered-prime-sieve-tv){reference-type="eqref" reference="eq:centered-prime-sieve-tv"}. Combine this total-variation estimate with [\[thm:centered-prime-haar\]](#thm:centered-prime-haar){reference-type="ref" reference="thm:centered-prime-haar"} to obtain [\[eq:sieve-haar-limit\]](#eq:sieve-haar-limit){reference-type="eqref" reference="eq:sieve-haar-limit"}.

[\[rem:haar-not-tv\]]{#rem:haar-not-tv label="rem:haar-not-tv"} For every finite $N$, the measure $\mu^{\circ}_{\mathcal{P},N}$ is supported on a finite grid, whereas $m_{\mathbb{T}}$ is nonatomic. Consequently $$\|\mu^{\circ}_{\mathcal{P},N}-m_{\mathbb{T}}\|_{\mathrm{TV}}=1,$$ and the same holds for $\mu^{\circ}_{Q_k,N_k}$. The limits in [\[eq:prime-haar-limit\]](#eq:prime-haar-limit){reference-type="eqref" reference="eq:prime-haar-limit"} and [\[eq:sieve-haar-limit\]](#eq:sieve-haar-limit){reference-type="eqref" reference="eq:sieve-haar-limit"} are therefore genuinely weak limits. By contrast, [\[eq:centered-prime-sieve-tv\]](#eq:centered-prime-sieve-tv){reference-type="eqref" reference="eq:centered-prime-sieve-tv"} compares two measures on the same finite grid and does tend to zero in total variation.

# Nested prime-prefix cylinders and numerical parameter

For $M\ge1$, define the parameter cylinder $$\label{eq:parameter-cylinder}
    I_M=\{u\in[1,2]:K(f_u)[0,M)=\mathcal{P}[0,M)\}.$$

[\[prop:shrinking-cylinders\]]{#prop:shrinking-cylinders label="prop:shrinking-cylinders"} The sets $I_M$ are nonempty intervals, they are nested, and $$\label{eq:cylinder-intersection}
    \bigcap_{M\ge1}\overline{I_M}=\{u_{\mathcal P}\}.$$ In particular, $$\label{eq:cylinder-diameter}
    \mathop{\mathrm{diam}}(\overline{I_M})\longrightarrow0.$$

Nonemptiness follows from $u_{\mathcal P}\in I_M$. A fixed parity-lexicographic prefix determines an interval in the ordered kneading space, and the kneading invariant is monotone in the quadratic parameter. Hence each $I_M$ is an interval. The cylinders are nested because matching $M+1$ symbols implies matching $M$.

Suppose $v\ne u_{\mathcal P}$ belonged to every closed cylinder. Choose $w$ strictly between $v$ and $u_{\mathcal P}$. Since each $I_M$ is an interval containing $u_{\mathcal P}$ and having $v$ in its closure, one has $w\in I_M$ for every $M$. The complete itinerary of $f_w$ would then equal $\mathcal{P}$, contradicting uniqueness in [\[thm:unique-realization\]](#thm:unique-realization){reference-type="ref" reference="thm:unique-realization"}. Thus the intersection is the singleton $\{u_{\mathcal P}\}$. Nested compact intervals with singleton intersection have diameters tending to zero.

Monotone bisection of the cylinder endpoints gives the values in [1](#tab:parameter-cylinders){reference-type="ref" reference="tab:parameter-cylinders"}. The computation used decimal arithmetic and direct iteration of $f_u$; it is auxiliary and is not used in any proof.

::: {#tab:parameter-cylinders}
    $M$       midpoint of $I_M$         $\mathop{\mathrm{diam}}(I_M)$
  ----- ------------------------------ -------------------------------
     10  $1.963201513261313838134946$       $1.646\times10^{-3}$
     20  $1.962717993500556150425984$       $1.852\times10^{-6}$
     40  $1.962717631159734191771903$       $2.618\times10^{-12}$
     80  $1.962717631158954623214533$       $4.515\times10^{-24}$
    120  $1.962717631158954623214533$       $8.377\times10^{-36}$
    160  $1.962717631158954623214533$       $1.463\times10^{-47}$
    200  $1.962717631158954623214533$       $2.465\times10^{-59}$

  : Prime-prefix cylinders for the unique quadratic parameter. The midpoint is rounded to 24 decimal places.
:::

The corresponding logistic parameter, from [\[eq:logistic-conjugacy\]](#eq:logistic-conjugacy){reference-type="eqref" reference="eq:logistic-conjugacy"}, is $$\label{eq:prime-logistic-parameter}
    b_{\mathcal P}=1+\sqrt{1+4u_{\mathcal P}}
    =3.975041264358499363108264\ldots.$$

# Interpretation and limits

The results establish a rigorous bridge between cumulative sieving and a single exact quadratic itinerary: $$Q_k[0,p_{k+1}^2)
    \xrightarrow[\text{exactly }k\text{ edits}]{}
    \mathcal{P}[0,p_{k+1}^2)
    =K(f_{u_{\mathcal P}})[0,p_{k+1}^2).$$ The bridge preserves all fixed finite-block statistics, correlations away from the terminal boundary, and both uncentered and centered normalized finite Fourier periodograms with explicit error bounds.

Four distinctions are essential.

1.  **The realization is inverse.** The full prime word selects $u_{\mathcal P}$. The construction does not provide a shorter algorithm for deciding primality and does not explain the primes from an independently chosen physical parameter.

2.  **Symbolic shadowing is not metric shadowing.** Hamming closeness of itineraries does not bound $|f_{u_{\mathcal P}}^n(1)-x_n|$ for an independently specified orbit. Near the critical point, a single symbolic disagreement can correspond to delicate phase-space behavior.

3.  **Periodograms are not transfer-operator spectra.** concerns the discrete Fourier power of finite symbol vectors. It does not control eigenvalues or resonances of Perron--Frobenius, Koopman, or renormalization operators.

4.  **The weak limits are universal.** The uncentered limit $\delta_0$ is forced by zero prime density. After centering and energy normalization, the fixed-frequency limit is Haar because an upper-bound sieve makes every nonzero fixed cyclic correlation negligible relative to the prime energy. These facts do not identify mesoscopic correlations, growing-lag behavior, local spectral statistics, or any relation to Riemann zeros.

Within these limits, the paper supplies the missing second layer between symbolic convergence and spectral modeling. Subsequent work can start from a fixed admissible orbit and explicit perturbation norms, instead of assuming a finite-stage topological conjugacy.

# Conclusion

The cumulative sieve word on its full quadratic validity horizon admits an exact and exceptionally sparse repair: change the $k$ sieving primes from $R$ to $L$. The repaired word is the natural prime indicator, is strictly kneading-admissible, and determines a unique real quadratic parameter. Thus the prime sequence has an exact inverse realization as a quadratic critical itinerary.

The repair has density $k/p_{k+1}^2\sim1/(p_{k+1}\log p_{k+1})$. This single identity yields quantitative stability for every fixed cylinder statistic, for correlations, and for normalized Fourier periodograms. In particular, the cumulative sieve masks and the exact prime kneading orbit possess the same Fourier-spectral limits along $N_k=p_{k+1}^2$.

Those limits can be identified unconditionally. Without centering, both periodograms converge in total variation to $\delta_0$. With empirical centering and energy normalization, both converge weakly to Haar measure. Thus fixed-frequency weak convergence is too coarse to retain refined prime-pair information. The next theoretical obstruction is sharply located at growing lags, mesoscopic spectral scales, or operators whose spectra have an independent dynamical meaning; none of these follows from kneading realizability alone.

# Data and code availability {#data-and-code-availability .unnumbered}

All principal statements are analytic. A standard-library decimal bisection script reproducing [1](#tab:parameter-cylinders){reference-type="ref" reference="tab:parameter-cylinders"} accompanies the manuscript. The source, script, and verified PDF are available from the author's public repository cited in @WangReformulation2026.

# Acknowledgements {#acknowledgements .unnumbered}

The author thanks the reviewers of the related manuscripts for comments which motivated a precise separation between symbolic repair, statistical stability, and operator spectra. AI-assisted tools were used for auxiliary typesetting, numerical cross-checking, and proof auditing; all mathematical statements and conclusions are the responsibility of the author.

# Disclosure statement {#disclosure-statement .unnumbered}

The author reports no competing interests.
