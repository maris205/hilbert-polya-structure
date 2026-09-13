---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-1-rigorous-sieve-kneading-reformulation"
canonical_tex: "zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation/rigorous-sieve-kneading-reformulation.pdf"
source_sha256: "e1ef4a2f3a5f01e324382e073e5a832ef4e416535c5a99714181307170b2bbf8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# From Sieve Words to Kneading Coordinates: A Rigorous Reformulation of the One-Dimensional Prime-Sieve Correspondence

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation/rigorous-sieve-kneading-reformulation.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-1-rigorous-sieve-kneading-reformulation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We revisit the one-dimensional symbolic correspondence between cumulative Eratosthenes sieve words and the quadratic family $f_u(x)=1-u x^2$. The correspondence was originally formulated through a finite-horizon topological admissibility hypothesis. We separate three logically distinct issues: convergence in the ordered symbolic space, realizability as a kneading invariant, and topological conjugacy of dynamical systems. First, without any prime-gap hypothesis, we prove that the cumulative sieve words are strictly increasing in the parity-lexicographic order and converge in the product topology to $RLR^\infty$, with first disagreement exactly at the next prime. We identify the corresponding band-merging parameter as the unique root in $(1,2)$ of $u^3-2u^2+2u-2=0$, construct its three-state Markov partition, and obtain the exact entropy $\frac12\log 2$ and even-return rigidity. We then prove that equality of the limiting sieve word with the kneading invariant does not yield a topological conjugacy: the natural shift orbit closure of $RLR^\infty$ has three points and entropy zero, whereas the quadratic attractor has positive entropy.

  At finite stages the universal admissibility hypothesis is false; we reproduce the explicit defect at sieve stage $k=3$. A parity-gap lemma reduces every detected MSS defect to a prime gap of length at least $p_{k+1}-1$. Combining this lemma with the Baker--Harman--Pintz theorem gives an unconditional admissible horizon of every length $H_k=p_{k+1}^{40/21-\varepsilon}$, for fixed $\varepsilon>0$ and all sufficiently large $k$. Although current unconditional gap bounds do not reach the full physical horizon $p_{k+1}^2$, we prove unconditionally that the density of MSS defects there is $O(p_{k+1}^{-1})$. The rigorous conclusion is therefore an ordered kneading-coordinate convergence and a parity factor, not an isomorphism between the prime sequence and a chaotic attractor. No statement about the infinitude of prime constellations is claimed.
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
  **From Sieve Words to Kneading Coordinates:**\
  A Rigorous Reformulation of the One-Dimensional Prime-Sieve Correspondence
```

## Markdown 正文

**Keywords:** sieve of Eratosthenes; kneading theory; parity-lexicographic order; logistic map; prime gaps; symbolic dynamics; topological entropy.

**MSC 2020:** 37E05; 37B10; 11N35; 11A41.

# Introduction

The Sieve of Eratosthenes is naturally expressed as a composition of periodic binary masks. In @Wang2026Published, this elementary algebra was used to propose a symbolic correspondence with the quadratic family $$\label{eq:quadratic-family}
    f_u(x)=1-u x^2, \qquad x\in[-1,1],\quad 0<u\le 2,$$ at the first band-merging parameter $u_{\mathrm c}\approx1.543689$. The proposed correspondence has two attractive features. The cumulative sieve words move monotonically toward the word $RLR^\infty$, and the critical orbit of $f_{u_{\mathrm c}}$ has the same itinerary. A finite-horizon topological admissibility condition was introduced to interpret each sieve stage as a kneading coordinate.

Subsequent analysis found that the finite-stage condition is not universally valid: explicit Metropolis--Stein--Stein (MSS) defects occur at $k=3$ and $k=5$ [@WangTransient2026]. This does not destroy every part of the construction. It instead forces a separation among three statements which are often conflated:

1.  a sequence may converge to a kneading word in the product topology;

2.  a finite or infinite word may satisfy the MSS maximality inequalities and hence be realizable as kneading data;

3.  two dynamical systems may be topologically conjugate.

Statement (i) is purely combinatorial and, as we prove below, is unconditional. Statement (ii) is the genuine role of topological admissibility. Statement (iii) requires phase spaces, evolution maps, and a homeomorphism intertwining them; equality of two distinguished words is not sufficient.

The broader program has also led to a sequential ergodic formulation [@WangSequential2026] and to numerical spectral models [@WangSpectral2026; @WangHenon2026]. The present paper deliberately isolates the topological layer. Its proofs do not use numerical orbit fitting, a non-autonomous density ansatz, or any conjecture concerning twin primes.

## Main results {#main-results .unnumbered}

Our conclusions can be summarized as follows.

1.  The sieve words $Q_k$ satisfy $$Q_1\prec Q_2\prec\cdots\prec K_{\mathrm c}=RLR^\infty,
            \qquad d_\vartheta(Q_k,K_{\mathrm c})=\vartheta^{p_{k+1}},$$ for every standard symbolic metric $d_\vartheta$, without assuming admissibility.

2.  The parameter $u_{\mathrm c}$ associated with $RLR^\infty$ is algebraic. A three-state Markov partition gives $$h_{\mathrm{top}}(f_{u_{\mathrm c}})=\frac12\log 2$$ and proves that successive visits to the $L$-region are separated by an even number of iterates.

3.  Under the natural shift-space interpretation, the limiting sieve system cannot be topologically conjugate to the quadratic attractor: their topological entropies are respectively $0$ and $\frac12\log2$.

4.  A detected finite-horizon MSS defect forces a prime gap of length at least $p_{k+1}-1$. The established bound $G(X)\ll X^{21/40}$ therefore gives unconditional horizon admissibility up to every length $$H_k=p_{k+1}^{40/21-\varepsilon}$$ for fixed $\varepsilon>0$ and all sufficiently large $k$.

5.  At the full physical horizon $N_k=p_{k+1}^2$, the number of detected defects satisfies $$D_k\le \frac{N_k}{p_{k+1}-1}+1,
            \qquad \frac{D_k}{N_k-1}=O(p_{k+1}^{-1}).$$ This defect-density result is unconditional and does not require a finite-defect conjecture.

These results retain a rigorous combinatorial skeleton of the original construction while placing a precise boundary around the word *isomorphism*. The finite sieve is an arithmetic mask, the limiting word is a kneading coordinate, and the quadratic system supplies a parity factor. None of these facts identifies the actual prime indicator with a typical quadratic orbit.

# Sieve words and the unimodal order

## Parity-lexicographic order

Let $\Sigma=\{L,R\}^{\mathbb{N}_0}$ and let $\sigma:\Sigma\to\Sigma$ be the left shift. We use the base order $L<R$.

[\[def:paritylex\]]{#def:paritylex label="def:paritylex"} Let $S=(s_n)$ and $T=(t_n)$ be distinct elements of $\Sigma$, and let $$j=\min\{n\ge0:s_n\ne t_n\}.$$ Let $r_j$ be the number of $R$ symbols in the common prefix $s_0\ldots s_{j-1}$. If $r_j$ is even, compare $s_j$ and $t_j$ using $L<R$; if $r_j$ is odd, reverse the order. The resulting order is denoted by $\prec$.

This is the standard orientation-sensitive order for unimodal itineraries [@Metropolis1973; @MilnorThurston1988]. For a one-sided word without a critical symbol, the MSS maximality condition is $$\label{eq:mss-infinite}
    \sigma^m(S)\preceq S \qquad(m\ge1).$$ We call a word satisfying [\[eq:mss-infinite\]](#eq:mss-infinite){reference-type="eqref" reference="eq:mss-infinite"} *self-admissible*. Endpoint conventions and completions matter when a finite word is promoted to a full kneading invariant; our finite-horizon definition below only records comparisons which are decided inside the stated horizon.

For $0<\vartheta<1$, define the standard symbolic metric $$\label{eq:symbolic-metric}
    d_\vartheta(S,T)=\vartheta^{n(S,T)},
    \qquad
    n(S,T)=\min\{j\ge0:s_j\ne t_j\},$$ with $d_\vartheta(S,S)=0$.

## Cumulative sieve masks

Let $2=p_1<p_2<\cdots$ be the primes and let $$P_k=\prod_{j=1}^k p_j.$$ The $k$th cumulative sieve word $Q_k\in\Sigma$ is defined by $$\label{eq:sieve-word}
    Q_k(n)=
    \begin{cases}
        L,&\gcd(n,P_k)=1,\\
        R,&\gcd(n,P_k)>1,
    \end{cases}
    \qquad n\ge1,
    \qquad Q_k(0)=R.$$ Thus $Q_k$ is periodic with period $P_k$. Notice that the convention [\[eq:sieve-word\]](#eq:sieve-word){reference-type="eqref" reference="eq:sieve-word"} marks each sieving prime $p_j$, $j\le k$, by $R$ along with its multiples. This convention is responsible both for the initial word $RLR\cdots$ and for the pointwise limit established below.

[\[lem:initial-shield\]]{#lem:initial-shield label="lem:initial-shield"} Let $p=p_{k+1}$. Then $$\label{eq:initial-shield}
    Q_k(0)Q_k(1)\cdots Q_k(p)
    =RLR^{p-2}L.$$ Equivalently, $Q_k(n)=R$ for $2\le n<p$, while $Q_k(p)=L$.

Every prime smaller than $p=p_{k+1}$ is among $p_1,\ldots,p_k$, and every composite $2\le n<p$ has a prime divisor smaller than $p$. Hence every $n\in[2,p)$ has nontrivial greatest common divisor with $P_k$. The next prime $p$ is coprime to $P_k$.

Define $$\label{eq:Kc-word}
    K_{\mathrm c}=RLR^\infty.$$

[\[thm:ordered-convergence\]]{#thm:ordered-convergence label="thm:ordered-convergence"} For every $k\ge1$, $$\label{eq:ordered-chain}
    Q_k\prec Q_{k+1}\prec K_{\mathrm c}.$$ The first disagreement between $Q_k$ and $K_{\mathrm c}$ occurs at index $p_{k+1}$, and therefore $$\label{eq:exact-metric-rate}
    d_\vartheta(Q_k,K_{\mathrm c})=\vartheta^{p_{k+1}}.$$ In particular $Q_k\to K_{\mathrm c}$ in the product topology and pointwise on $\mathbb{N}_0$.

Put $p=p_{k+1}$. Adding the new sieve factor $p$ does not alter any symbol with $1\le n<p$, while $$Q_k(p)=L,\qquad Q_{k+1}(p)=R.$$ By [\[lem:initial-shield\]](#lem:initial-shield){reference-type="ref" reference="lem:initial-shield"}, the common prefix at indices $0,\ldots,p-1$ is $RLR^{p-2}$. It contains $$1+(p-2)=p-1$$ symbols $R$. Since $p=p_{k+1}$ is odd for $k\ge1$, this number is even. The comparison at index $p$ therefore uses the base order $L<R$, proving $Q_k\prec Q_{k+1}$.

The same common prefix occurs when comparing $Q_k$ with $K_{\mathrm c}$, and at index $p$ one again compares $L$ in $Q_k$ with $R$ in $K_{\mathrm c}$. Hence $Q_k\prec K_{\mathrm c}$, the first-disagreement index is exactly $p$, and [\[eq:exact-metric-rate\]](#eq:exact-metric-rate){reference-type="eqref" reference="eq:exact-metric-rate"} follows from [\[eq:symbolic-metric\]](#eq:symbolic-metric){reference-type="eqref" reference="eq:symbolic-metric"}.

Finally, for each fixed $n\ge2$, choose $k$ large enough that a prime divisor of $n$ belongs to $\{p_1,\ldots,p_k\}$. Then $Q_k(n)=R$ for all subsequent stages. The symbols at $0$ and $1$ remain $R$ and $L$, respectively, proving pointwise convergence to $RLR^\infty$.

[\[rem:order-limits\]]{#rem:order-limits label="rem:order-limits"} The limit in [\[thm:ordered-convergence\]](#thm:ordered-convergence){reference-type="ref" reference="thm:ordered-convergence"} is not the natural prime indicator. In the pointwise limit every fixed prime is eventually used as a sieve factor and hence is marked $R$. Thus $K_{\mathrm c}$ has exactly one $L$, at index $1$. Retaining primes on a growing interval requires a diagonal choice of the sieve depth as the observation horizon grows. Pointwise convergence in $k$, diagonal sieving in the integer variable, and convergence in natural density are distinct operations.

# The band-merging parameter and its exact Markov skeleton

We now identify the quadratic parameter associated with [\[eq:Kc-word\]](#eq:Kc-word){reference-type="eqref" reference="eq:Kc-word"} without using any sieve admissibility assumption.

[\[prop:uc\]]{#prop:uc label="prop:uc"} The polynomial $$\label{eq:uc-polynomial}
    F(u)=u^3-2u^2+2u-2$$ has a unique zero $u_{\mathrm c}$ in $(1,2)$. Numerically, $$u_{\mathrm c}=1.543689012692\ldots.$$ If $b=u_{\mathrm c}-1$, then the critical orbit of $f_{u_{\mathrm c}}$ satisfies $$\label{eq:critical-orbit}
    0\longmapsto1\longmapsto-b\longmapsto b\longmapsto b.$$ Consequently the itinerary of the critical value $1$ under the partition $L=\{x<0\}$, $R=\{x>0\}$ is $RLR^\infty$.

We have $F(1)=-1$ and $F(2)=2$. Moreover $$F'(u)=3u^2-4u+2=3\left(u-\frac23\right)^2+\frac23>0,$$ so there is exactly one real zero in $(1,2)$. Let $b=u_{\mathrm c}-1$. Equation $F(u_{\mathrm c})=0$ is equivalent to $$1-u_{\mathrm c}b^2=b.$$ Therefore $f_{u_{\mathrm c}}(1)=1-u_{\mathrm c}=-b$ and $$f_{u_{\mathrm c}}(-b)=f_{u_{\mathrm c}}(b)=1-u_{\mathrm c}b^2=b,$$ which proves [\[eq:critical-orbit\]](#eq:critical-orbit){reference-type="eqref" reference="eq:critical-orbit"} and its itinerary.

[\[thm:markov\]]{#thm:markov label="thm:markov"} Let $b=u_{\mathrm c}-1$ and define $$J_L=[-b,0],\qquad J_0=[0,b],\qquad J_1=[b,1].$$ Up to their common endpoints, $$\label{eq:markov-images}
    f_{u_{\mathrm c}}(J_L)=J_1,\qquad
    f_{u_{\mathrm c}}(J_0)=J_1,\qquad
    f_{u_{\mathrm c}}(J_1)=J_L\cup J_0.$$ The associated transition matrix is $$\label{eq:markov-matrix}
    A=
    \begin{pmatrix}
        0&0&1\\
        0&0&1\\
        1&1&0
    \end{pmatrix},
    \qquad \operatorname{spec}(A)=\{0,\sqrt2,-\sqrt2\}.$$ Hence $$\label{eq:entropy}
    h_{\mathrm{top}}(f_{u_{\mathrm c}})=\log\rho(A)=\frac12\log2.$$ Furthermore, for every orbit which does not land on a partition endpoint, the time difference between two successive visits to $J_L$ is even. In particular the word $LL$ is forbidden.

On $[-b,0]$ the map is increasing, with endpoint values $f_{u_{\mathrm c}}(-b)=b$ and $f_{u_{\mathrm c}}(0)=1$. On $[0,b]$ it is decreasing with the same image $[b,1]$. On $[b,1]$ it is decreasing from $b$ to $-b$. This proves [\[eq:markov-images\]](#eq:markov-images){reference-type="eqref" reference="eq:markov-images"} and [\[eq:markov-matrix\]](#eq:markov-matrix){reference-type="eqref" reference="eq:markov-matrix"}. A direct determinant calculation gives $$\det(\lambda I-A)=\lambda(\lambda^2-2),$$ so the spectral radius is $\sqrt2$. The standard entropy formula for a piecewise monotone Markov interval map yields [\[eq:entropy\]](#eq:entropy){reference-type="eqref" reference="eq:entropy"}; see, for example, @deMeloVanStrien1993 and @LindMarcus1995 [Ch. 4].

For the return parity, put $C=[-b,b]$ and $H=[b,1]$. The image relations above give $$f_{u_{\mathrm c}}(C)=H,\qquad f_{u_{\mathrm c}}(H)=C.$$ Thus an orbit alternates between the two sets $C$ and $H$. Since $J_L\subset C$, all visits to $J_L$ occur in the same parity class of the time variable. Successive visit times therefore differ by an even integer. In particular, a visit to $J_L$ is followed by a visit to $H\subset\{x\ge0\}$, excluding $LL$.

# Kneading equality is not topological conjugacy

The phrase *topological isomorphism* requires two dynamical systems, not merely two distinguished symbolic words. The most direct shift-space realization of the limiting sieve word already gives a sharp obstruction.

Let $$X_{K_{\mathrm c}}=\overline{\{\sigma^nK_{\mathrm c}:n\ge0\}}\subset\Sigma$$ be the shift orbit closure of the limiting sieve word.

[\[thm:no-conjugacy\]]{#thm:no-conjugacy label="thm:no-conjugacy"} The shift system $(X_{K_{\mathrm c}},\sigma)$ is not topologically conjugate to $f_{u_{\mathrm c}}$ on its invariant interval $[-b,1]$.

Since $K_{\mathrm c}=RLR^\infty$, $$X_{K_{\mathrm c}}=\{RLR^\infty,\,LR^\infty,\,R^\infty\}.$$ It is a finite dynamical system and has topological entropy zero. By [\[thm:markov\]](#thm:markov){reference-type="ref" reference="thm:markov"}, the quadratic map has topological entropy $\frac12\log2>0$. Topological entropy is invariant under topological conjugacy, so no conjugacy exists.

The equality $\lim_k Q_k=K(f_{u_{\mathrm c}})$ remains a correct statement about a coordinate in the ordered symbolic space. It says that the limiting word is the kneading invariant which determines the boundary of the admissible language at $u_{\mathrm c}$. It does not say that the limiting word is a typical orbit, that its shift orbit closure is the quadratic attractor, or that the actual prime indicator has the same finite-word language as the quadratic system.

# Finite-horizon admissibility and its failure at small stages

## Detected defects

Let $H\ge1$ and write $W_{k,H}=Q_k[0,H)$ for the prefix of length $H$.

[\[def:defect\]]{#def:defect label="def:defect"} A shift $m\in\{1,\ldots,H-1\}$ is a *detected defect at horizon $H$* if there is a first index $j<H-m$ such that $$Q_k(m+i)=Q_k(i)\quad(0\le i<j),$$ and the parity-lexicographic comparison at $j$ gives $$\sigma^m(Q_k)\succ Q_k.$$ Let $\mathcal{D}_k(H)$ be the set of detected defects, $D_k(H)=|\mathcal{D}_k(H)|$, and $$\rho_k(H)=\frac{D_k(H)}{H-1}.$$ The prefix is *horizon-admissible* if $D_k(H)=0$.

This convention makes no assertion when a comparison is not decided before the suffix exits the horizon. It is exactly the finite information available in the sieve-valid window.

[\[prop:k3-defect\]]{#prop:k3-defect label="prop:k3-defect"} At stage $k=3$, with sieve primes $2,3,5$ and physical horizon $H=p_4^2=49$, the shift $m=22$ is a detected MSS defect.

The first ten symbols of $Q_3$ and its shift are $$\begin{array}{c|cccccccccc}
 i&0&1&2&3&4&5&6&7&8&9\\
 \midrule
 Q_3(i)&R&L&R&R&R&R&R&L&R&R\\
 Q_3(22+i)&R&L&R&R&R&R&R&L&R&L.
\end{array}$$ The common prefix of length nine contains seven $R$ symbols, so the order is reversed at the first disagreement. At position $9$, $Q_3$ has $R$ and the shift has $L$; under the reversed order $R<L$. Thus $Q_3\prec\sigma^{22}Q_3$, and the disagreement is detected at the integer $22+9=31<49$.

The assertion that every cumulative sieve stage is kneading-admissible on its entire physical horizon is false.

The analogous defect at $k=5$ is generated by the prime gap $113$--$127$; see @WangTransient2026. We now prove the structural reduction which explains why such defects are rare.

# The parity-gap reduction

For a prime $q$, let $q^+$ denote the next prime and write $g(q)=q^+-q$. Define $$\label{eq:G-def}
    G(X)=\max\{g(q):q\le X,\ q\ \text{prime}\}.$$

[\[lem:parity-gap\]]{#lem:parity-gap label="lem:parity-gap"} Let $p=p_{k+1}$ and let $p<H\le p^2$. If $m\in\mathcal{D}_k(H)$, then

1.  $q=m+1$ is prime;

2.  $g(q)\ge p-1$.

By [\[lem:initial-shield\]](#lem:initial-shield){reference-type="ref" reference="lem:initial-shield"}, the reference prefix begins $$Q_k=RLR^{p-2}L\cdots.$$ We compare $\sigma^m Q_k$ with $Q_k$.

At position $0$, if $Q_k(m)=L$, then the shift begins with $L$ while $Q_k$ begins with $R$. The common prefix is empty, so the base order applies and the shift is smaller. A defective shift must therefore satisfy $Q_k(m)=R$. The common prefix now contains one $R$, and the order is reversed at the next disagreement.

At position $1$, the reference word has $Q_k(1)=L$. If $Q_k(m+1)=R$, then under the reversed order the shifted $R$ is smaller than the reference $L$, again defeating the shift. Hence a defect requires $Q_k(m+1)=L$. Since $2\le m+1<H\le p^2$, every composite integer in this range has a prime factor strictly smaller than $p$ and is marked $R$ by $Q_k$. Therefore $q=m+1$ is prime. In particular $q\ge p$ and is odd.

Let $r<H-m$ be the first disagreement which detects the defect. We claim that $r\ge p$. Otherwise $2\le r\le p-1$, the reference symbol is $Q_k(r)=R$, and the shifted symbol must be $Q_k(m+r)=L$. By the same sieve-validity argument, $m+r$ is prime. Both $m+1$ and $m+r$ are odd primes, so their difference $r-1$ is even and hence $r$ is odd. The common reference prefix through position $r-1$ contains $$1+(r-2)=r-1$$ symbols $R$, an even number. The order at position $r$ is therefore unflipped, and the shifted symbol $L$ is smaller than the reference symbol $R$, contradicting that $r$ detects a defect. Hence $r\ge p$.

The two words therefore agree at every position $2\le j\le p-1$, so $Q_k(m+j)=R$ there. Since $m+j>q\ge p$, each such integer is divisible by one of the sieving primes and is composite. Equivalently, the integers $$q+1,q+2,\ldots,q+p-2$$ are all composite. The next prime satisfies $q^+\ge q+p-1$, and hence $g(q)\ge p-1$.

[\[cor:gap-condition\]]{#cor:gap-condition label="cor:gap-condition"} Let $p=p_{k+1}$ and $p<H\le p^2$. If $$\label{eq:gap-sufficient}
    G(H)<p-1,$$ then $W_{k,H}$ is horizon-admissible.

The contrapositive of [\[lem:parity-gap\]](#lem:parity-gap){reference-type="ref" reference="lem:parity-gap"} states that a defect would produce a prime $q\le H$ with $g(q)\ge p-1$, contradicting [\[eq:gap-sufficient\]](#eq:gap-sufficient){reference-type="eqref" reference="eq:gap-sufficient"}.

Condition [\[eq:gap-sufficient\]](#eq:gap-sufficient){reference-type="eqref" reference="eq:gap-sufficient"} is sufficient, not necessary. In particular a long prime gap does not by itself force the parity of every later tie-breaker to create an MSS defect.

# An unconditional long admissible horizon

The unconditional all-$x$ consecutive-prime estimate needed here is due to @BakerHarmanPintz2001: $$\label{eq:BHP-gap}
    p_{n+1}-p_n\ll p_n^{21/40},$$ for all sufficiently large $n$. In particular, $G(X)\ll X^{21/40}$.

[\[thm:BHP-horizon\]]{#thm:BHP-horizon label="thm:BHP-horizon"} Fix $$0<\varepsilon<\frac{19}{21}$$ and put $$\label{eq:Hk}
    H_k=\left\lfloor p_{k+1}^{40/21-\varepsilon}\right\rfloor.$$ Then $W_{k,H_k}$ is horizon-admissible for all sufficiently large $k$.

Let $p=p_{k+1}$. Since $1<40/21-\varepsilon<2$, we have $p<H_k<p^2$ for all sufficiently large $p$. By [\[eq:BHP-gap\]](#eq:BHP-gap){reference-type="eqref" reference="eq:BHP-gap"}, $$G(H_k)
    \ll H_k^{21/40}
    \ll p^{(40/21-\varepsilon)(21/40)}
    =p^{1-(21/40)\varepsilon}
    =o(p).$$ Thus $G(H_k)<p-1$ for sufficiently large $k$, and [\[cor:gap-condition\]](#cor:gap-condition){reference-type="ref" reference="cor:gap-condition"} applies.

[\[cor:exponent-criterion\]]{#cor:exponent-criterion label="cor:exponent-criterion"} Suppose an all-$X$ prime-gap theorem gives $G(X)\ll X^\theta$. Then every horizon $H_k=p_{k+1}^{a}$ with $$1<a<\min\{2,1/\theta\}$$ is eventually horizon-admissible through [\[cor:gap-condition\]](#cor:gap-condition){reference-type="ref" reference="cor:gap-condition"}. The full quadratic horizon $H_k=p_{k+1}^2$ follows from this route if $G(X)=o(X^{1/2})$.

At $X=p^2$, the Baker--Harman--Pintz exponent gives only $$G(p^2)\ll p^{21/20},$$ which is larger than the required shield $p-1$. A Riemann-hypothesis bound of order $O(X^{1/2}\log X)$ also does not imply [\[eq:gap-sufficient\]](#eq:gap-sufficient){reference-type="eqref" reference="eq:gap-sufficient"} at $X=p^2$. In contrast, Cramér-type polylogarithmic bounds [@Cramer1936] would imply eventual full-horizon admissibility. The latter remains a conditional statement.

# Unconditional decay of the defect density

Full admissibility is much stronger than the vanishing of the proportion of bad shifts. The parity-gap lemma proves the latter unconditionally.

[\[thm:defect-density\]]{#thm:defect-density label="thm:defect-density"} Let $p=p_{k+1}$ and $p<H\le p^2$. Then $$\label{eq:defect-count}
    D_k(H)\le \frac{H}{p-1}+1.$$ Consequently, at the physical horizon $N_k=p_{k+1}^2$, $$\label{eq:defect-density}
    \rho_k(N_k)
    \le \frac{1}{p_{k+1}-1}+O(p_{k+1}^{-2})
    \longrightarrow0.$$

By [\[lem:parity-gap\]](#lem:parity-gap){reference-type="ref" reference="lem:parity-gap"}, every defect $m$ determines the prime $q=m+1$ and a consecutive-prime interval $[q,q^+)$ of length at least $p-1$. The map $m\mapsto q$ is injective, and consecutive-prime intervals associated with distinct $q$ are disjoint.

All their left endpoints satisfy $q\le H$. At most one of these disjoint intervals can cross the endpoint $H$. The remaining intervals lie inside $[0,H]$, have total length at most $H$, and each has length at least $p-1$. Hence there are at most $H/(p-1)$ of them, plus at most one crossing interval. This proves [\[eq:defect-count\]](#eq:defect-count){reference-type="eqref" reference="eq:defect-count"}. Dividing by $H-1$ and setting $H=p^2$ gives [\[eq:defect-density\]](#eq:defect-density){reference-type="eqref" reference="eq:defect-density"}.

[\[rem:defect-limitation\]]{#rem:defect-limitation label="rem:defect-limitation"} The limit $\rho_k(N_k)\to0$ proves asymptotic admissibility in the defect-density sense. It does not by itself construct a true admissible word at Hamming distance $o(N_k)$ from $W_{k,N_k}$, nor does it prove shadowing by a quadratic orbit. A sparse set of failed maximality comparisons is not the same object as a sparse set of symbol edits. Any passage from [\[eq:defect-density\]](#eq:defect-density){reference-type="eqref" reference="eq:defect-density"} to equality of ergodic cylinder statistics requires an additional repair or shadowing theorem.

# An alternative exact prime word and its tradeoff

The obstruction above is partly caused by marking each sieving prime itself as $R$. If one instead uses the natural prime word, absolute self-admissibility becomes elementary, but the band-merging limit is lost.

Define $\mathcal{P}\in\Sigma$ by $$\mathcal{P}(0)=R,\qquad \mathcal{P}(1)=L,$$ and, for $n\ge2$, $$\mathcal{P}(n)=
    \begin{cases}
        L,&n\ \text{is prime},\\
        R,&n\ \text{is composite}.
    \end{cases}$$

[\[prop:natural-prime\]]{#prop:natural-prime label="prop:natural-prime"} For every $m\ge1$, $$\sigma^m\mathcal{P}\prec\mathcal{P}.$$

If $\mathcal{P}(m)=L$, the comparison is decided at position $0$: the shift begins with $L$, while $\mathcal{P}$ begins with $R$, so the shift is smaller in the base order.

Suppose $\mathcal{P}(m)=R$. Then $m\ge4$ is composite and both words begin with $R$, so the order is reversed at the next disagreement. If $\mathcal{P}(m+1)=R$, position $1$ compares the shifted $R$ with $\mathcal{P}(1)=L$; under the reversed order the shift is smaller. If $\mathcal{P}(m+1)=L$, then $m+1$ is an odd prime at least $5$, so $m+2$ is even and composite. The words agree as $RL$ at positions $0,1$, the prefix still contains one $R$, and at position $2$ the shifted $R$ is smaller than $\mathcal{P}(2)=L$ in the reversed order. Thus every nonzero shift is defeated by position $2$ at the latest.

The proposition gives an unconditional inverse-kneading encoding of the prime indicator. However, $\mathcal{P}$ begins $RLLL\cdots$, not $RLR^\infty$, and therefore does not select the band-merging parameter $u_{\mathrm c}$. Exact prime coding and the particular one-dimensional band-merging skeleton are different constructions.

# Interpretation and scope

The preceding results suggest the following replacement for the original strong isomorphism statement.

> *The cumulative sieve masks form a strictly ordered path in the full symbolic space and converge to the band-merging kneading coordinate $RLR^\infty$. The quadratic map at that coordinate realizes the parity factor of the sieve grammar. Finite-stage realization as kneading data is valid on an unconditional growing subquadratic horizon and has vanishing defect density on the full quadratic horizon.*

This statement retains the exact algebraic and topological facts while avoiding four overextensions.

1.  **A finite prefix is not a unique parameter.** Even when every comparison visible in a finite word is admissible, a completion rule is needed before the word becomes an infinite kneading invariant. Different completions can determine an interval of parameters rather than a single $u_k$.

2.  **Pointwise sieve convergence erases the primes.** The word $RLR^\infty$ is a boundary coordinate, not the natural prime sequence; see [\[rem:order-limits\]](#rem:order-limits){reference-type="ref" reference="rem:order-limits"}.

3.  **A kneading invariant is not a typical orbit.** It controls the language of a unimodal system. Equality of a limiting mask with a kneading word does not supply a conjugating homeomorphism; [\[thm:no-conjugacy\]](#thm:no-conjugacy){reference-type="ref" reference="thm:no-conjugacy"} rules out the natural shift-space version.

4.  **Asymptotic admissibility is not arithmetic shadowing.** The defect-density theorem is a genuine unconditional macroscopic statement, but the stronger orbit-shadowing problem remains separate; see [\[rem:defect-limitation\]](#rem:defect-limitation){reference-type="ref" reference="rem:defect-limitation"}.

The numerical computations in @Wang2026Published [@WangTransient2026] remain useful in their proper role: they discovered the small-stage defects, quantified their scarcity over a large finite range, and motivated [\[lem:parity-gap\]](#lem:parity-gap){reference-type="ref" reference="lem:parity-gap"}. The proofs in the present paper neither infer an infinite theorem from that finite range nor discard the numerical observations. They identify exactly which conclusions are stable under the transition from computation to proof.

# Conclusion

The topological admissibility condition is essential for assigning a sieve word itself as kneading data, but it is not needed for the ordered convergence $$Q_k\nearrow RLR^\infty$$ or for the algebraic identification of the band-merging parameter. The universal finite-stage condition is false, while two rigorous replacements are available: an unconditional admissible prefix of length $p_{k+1}^{40/21-\varepsilon}$ and an unconditional $O(p_{k+1}^{-1})$ defect density on the full physical horizon.

At the same time, the entropy obstruction shows that the surviving result cannot be called a topological conjugacy between the limiting sieve word and the chaotic quadratic attractor. The correct object is a kneading-coordinate convergence together with a parity factor. This reformulation provides a stable base for subsequent spectral and non-autonomous work: stronger arithmetic conclusions must enter through a separately stated shadowing, shrinking-target, or sieve-remainder theorem, not through kneading equality alone.

# Data and code availability {#data-and-code-availability .unnumbered}

All statements in this paper are proved analytically and require no numerical data. Code and data associated with the motivating computations are available from the repositories cited in @Wang2026Published [@WangTransient2026] and from the author upon reasonable request.

# Acknowledgements {#acknowledgements .unnumbered}

The author thanks the reviewers of the related manuscripts for comments that motivated a sharper separation between symbolic convergence, admissibility, and conjugacy. AI-assisted tools were used for auxiliary typesetting and proof auditing; all mathematical statements and conclusions are the responsibility of the author.

# Disclosure statement {#disclosure-statement .unnumbered}

The author reports no competing interests.
