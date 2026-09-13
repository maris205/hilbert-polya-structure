---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--79-noisy-fkm-delayed-irreversibility"
canonical_tex: "symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility/main.tex"
canonical_pdf: "symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility/main.pdf"
source_sha256: "b21d874f05d20be6cce7ff6d06f05e0752f88a91a9e7932cfedaf9d748f81ba9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Delayed Time-Reversal Asymmetry in Noisy FKM de Bruijn Phase Processes

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/79-noisy-fkm-delayed-irreversibility/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every $k\geq 3$, we construct a stationary binary process that is exactly indistinguishable from a fair independent process on every consecutive block of length at most $k$, yet first becomes time-irreversible at length $k+1$. The clean source is the uniformly phased lexicographically least Fredricksen--Kessler--Maiorana de Bruijn cycle, and each symbol is observed through an independent binary symmetric channel with crossover probability $\varepsilon$. An explicit FKM word occurs while its reversal does not. Tensorizing the channel then gives, for the length-$(k+1)$ law $p_{\varepsilon,k+1}$, $$\|p_{\varepsilon,k+1}-Rp_{\varepsilon,k+1}\|_2
   \geq \sqrt{2}\,2^{-k}|1-2\varepsilon|^{k+1},
   \qquad
   \operatorname{TV}(p_{\varepsilon,k+1},Rp_{\varepsilon,k+1})
   \geq 2^{-k}|1-2\varepsilon|^{k+1}.$$ Thus the first reversal defect remains exactly at $k+1$ for every $\varepsilon\neq \tfrac12$. For $0<\varepsilon<1$ the observed law has full support and is ergodic. Away from $\varepsilon=\tfrac12$ it is not mixing; under strictly noisy, nonfair emissions it has infinite Markov order. Its entropy rate is $h_{\mathrm b}(\varepsilon)$ bits, while its excess entropy is exactly $k$ bits away from fair noise and is zero at $\varepsilon=\tfrac12$. All endpoint regimes are separated explicitly. The results concern persistent-phase emission noise; they do not claim novelty for the de Bruijn construction, uniform short-block laws, or transition-noise de Bruijn models.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Delayed Time-Reversal Asymmetry in Noisy FKM de Bruijn Phase Processes'
```

## Markdown 正文

# Introduction

A finite collection of block statistics can hide a deterministic phase for an arbitrarily long prescribed horizon. De Bruijn cycles give the sharpest finite version of this phenomenon: an order-$k$ binary cycle contains every $k$-word exactly once, so a uniformly chosen cyclic phase has the same consecutive block laws as a fair independent process through length $k$. The order of those words, however, controls the next symbol and can carry a time direction.

This note makes that time direction explicit for the lexicographically least de Bruijn cycle produced by the Fredricksen--Kessler--Maiorana (FKM) construction. We corrupt the periodic source by independent bit flips but do not let an error alter its hidden phase. The resulting process is a finite-state hidden Markov process, or a sofic measure in symbolic-dynamical language [@BoylePetersen2010]. Its short blocks remain exactly uniform. At the next length, a concrete FKM word occurs while its reversal does not. Because a nondegenerate binary symmetric channel is an invertible linear map on signed block laws, this first reversal defect survives every noise level except the fair-noise point.

The same persistent phase produces a second separation. The observed measure has full support and is ergodic whenever the emission probabilities are nondegenerate, but it is not mixing away from fair noise. Away from fair noise, an infinite one-sided observation recovers the phase almost surely. Consequently the process has infinite Markov order under strictly noisy nonfair emissions, entropy rate $h_{\mathrm b}(\varepsilon)$, and excess entropy $k$; at fair noise the excess entropy is zero. The local block entropy is therefore maximal through the chosen horizon even though the asymptotic entropy rate can be arbitrarily small.

Our contributions are the following exact statements.

1.  We locate the first reversal defect of the FKM phase law at length $k+1$ using the word $0^{k-1}10$ and its absent reversal.

2.  We prove quantitative Euclidean and total-variation lower bounds after independent binary symmetric emissions for every $\varepsilon\neq\tfrac12$.

3.  We characterize stationarity, ergodicity, support, entropy rate, one-sided phase recovery, excess entropy, mixing, and Markov order, including all noise endpoints and the exceptional orders $k=1,2$.

These are residual calculations around established constructions, not a priority claim. The FKM theorem and its modern proofs are prior work [@FredricksenMaiorana1978; @AmramEtAl2025]. Pincus and Singer use de Bruijn blocks to expose higher-order structure hidden by local equidistribution [@PincusSinger2014], and general time asymmetry in hidden Markov processes has a substantial information-theoretic framework [@EllisonEtAl2011]. Most directly, Mohri et al. use a uniformly seeded de Bruijn successor model to obtain uniform length-$L$ contexts and mention a full-support transition perturbation [@MohriEtAl2026]. We state the overlap and the remaining distinction precisely in [7](#sec:ownership){reference-type="ref" reference="sec:ownership"}.

# The FKM phase process {#sec:setup}

## The Lyndon-concatenation convention

Let the binary alphabet be ordered by $0<1$, and order finite words lexicographically, with a proper prefix preceding its extension. A nonempty word is *Lyndon* if it is strictly smaller than each of its nontrivial cyclic rotations.

[\[def:fkm\]]{#def:fkm label="def:fkm"} For $k\geq 1$, list in increasing lexicographic order all binary Lyndon words whose lengths divide $k$, and concatenate them. The resulting word is denoted $$D_k=d_0d_1\cdots d_{N-1},\qquad N=2^k,$$ with indices read modulo $N$.

The FKM theorem states that $D_k$ is a binary de Bruijn cycle of order $k$: each word in $\{0,1\}^k$ occurs at exactly one cyclic starting position [@FredricksenMaiorana1978; @AmramEtAl2025]. Definition [\[def:fkm\]](#def:fkm){reference-type="ref" reference="def:fkm"} fixes the convention directly; names such as *prefer-min* and *prefer-max* can change under reversal or complementation conventions.

## Persistent phase and emission noise

Let $U$ be uniform on $\mathbb Z/N\mathbb Z$. Independently, let $(Z_t)_{t\in\mathbb Z}$ be independent Bernoulli variables with $$\mathbb P(Z_t=1)=\varepsilon,\qquad 0\leq\varepsilon\leq 1.$$ Define the clean and observed processes $$\label{eq:process}
 X_t=d_{U+t\pmod N},
 \qquad
 Y_t=X_t\oplus Z_t,
 \qquad t\in\mathbb Z.$$ An emission error changes $Y_t$ but not the phase $U+t$. This persistent phase will distinguish [\[eq:process\]](#eq:process){reference-type="eqref" reference="eq:process"} from a noisy successor rule whose next state is the most recent emitted $k$-block.

For $\ell\geq1$, let $p_{\varepsilon,\ell}$ be the probability vector on $\{0,1\}^{\ell}$ defined by $$p_{\varepsilon,\ell}(w)
 =\mathbb P(Y_0Y_1\cdots Y_{\ell-1}=w).$$ For a word $w=w_0\cdots w_{\ell-1}$, write $\operatorname{rev}(w)=w_{\ell-1}\cdots w_0$. Reversal acts on probability vectors by $$(Rp)(w)=p(\operatorname{rev}(w)).$$ A stationary process is time-reversible exactly when $p_{\varepsilon,\ell}=Rp_{\varepsilon,\ell}$ for every $\ell$.

# Stationarity, ergodicity, and support

[\[thm:basic\]]{#thm:basic label="thm:basic"} For every $k\geq1$ and $\varepsilon\in[0,1]$, the process $Y$ is stationary and ergodic. If $0<\varepsilon<1$, its topological support is the full binary shift. At $\varepsilon=0$ and $\varepsilon=1$, its support is one periodic orbit of cardinality $2^k$.

Work first on $$\Omega=(\mathbb Z/N\mathbb Z)\times\{0,1\}^{\mathbb Z}$$ with the product of the uniform phase law and the Bernoulli noise law. The transformation $$S(u,z)=(u+1,\sigma z),\qquad (\sigma z)_t=z_{t+1},$$ preserves this measure, and the observation map in [\[eq:process\]](#eq:process){reference-type="eqref" reference="eq:process"} intertwines $S$ with the left shift of $Y$. This proves stationarity.

Suppose $0<\varepsilon<1$. If an event is $S$-invariant, then it is $S^N$-invariant. On each phase fiber, $S^N$ is the $N$th power of a nondegenerate Bernoulli shift and is ergodic. The event is therefore constant almost surely on each phase fiber. Invariance under $S$ makes those $N$ fiber constants equal, so the event has probability zero or one. Thus $S$, and hence its factor $Y$, is ergodic.

At either endpoint the noise configuration is deterministic. The system reduces to the uniform measure on a single $N$-cycle, which is ergodic. The period is exactly $N$: a shorter period would allow fewer than $N$ distinct length-$k$ blocks.

Finally, let $0<\varepsilon<1$ and fix any finite output word. Conditional on any phase, its probability is a product of factors chosen from $\varepsilon$ and $1-\varepsilon$, so it is positive. Every cylinder therefore has positive measure. At an endpoint only the cyclic shifts of $D_k$, or of its bitwise complement, occur.

# The exact first reversal defect

[\[lem:uniform\]]{#lem:uniform label="lem:uniform"} For every $1\leq\ell\leq k$, every $\varepsilon\in[0,1]$, and every $w\in\{0,1\}^{\ell}$, $$p_{\varepsilon,\ell}(w)=2^{-\ell}.$$ In particular, all block laws through length $k$ are reversible and coincide with those of a fair independent process.

Each $\ell$-word has $2^{k-\ell}$ extensions to a $k$-word. Every such $k$-word occurs once in the de Bruijn cycle, so the uniformly phased clean process assigns probability $2^{k-\ell}/2^k=2^{-\ell}$ to the $\ell$-word. Independent binary symmetric channels map the uniform law on $\{0,1\}^{\ell}$ to itself.

The next lemma is the only point where the choice of the lexicographically least FKM cycle, rather than an arbitrary de Bruijn cycle, is used.

[\[lem:witness\]]{#lem:witness label="lem:witness"} For every $k\geq3$, the length-$(k+1)$ word $$u_k=0^{k-1}10$$ occurs cyclically in $D_k$, whereas $$\operatorname{rev}(u_k)=010^{k-1}$$ does not occur.

Every nonconstant binary Lyndon word begins in $0$ and ends in $1$. Among the Lyndon words whose lengths divide $k$, the first three for $k\geq3$ are $$0,\qquad 0^{k-1}1,\qquad 0^{k-2}11.$$ Indeed, $0^{k-1}1$ has the longest possible initial zero run among the nonzero candidates. The word $0^{k-2}11$ is Lyndon. Any word strictly between these two would need exactly $k-2$ initial zeros and length at least $k-1$. A proper divisor of $k$ cannot equal $k-1$ when $k\geq3$, and at length $k$ the requirement to begin with $0^{k-2}1$ and end in $1$ forces $0^{k-2}11$.

Consequently the FKM concatenation begins $$\label{eq:fkm-prefix}
 0\,0^{k-1}1\,0^{k-2}11
 =0^k1\,0^{k-2}11.$$ Starting at the second symbol of [\[eq:fkm-prefix\]](#eq:fkm-prefix){reference-type="eqref" reference="eq:fkm-prefix"} gives $0^{k-1}10$, so $u_k$ occurs.

Now consider the $k$-word $a_k=010^{k-2}$. It occurs in [\[eq:fkm-prefix\]](#eq:fkm-prefix){reference-type="eqref" reference="eq:fkm-prefix"}, beginning at the last zero of the initial block $0^k$, and the symbol following it there is $1$. A de Bruijn cycle contains $a_k$ at exactly one cyclic position. Hence $a_k$ cannot be followed by $0$, which excludes the length-$(k+1)$ word $010^{k-1}=\operatorname{rev}(u_k)$.

## Robustness under the binary symmetric channel

Let $$C_\varepsilon=
 \begin{pmatrix}
 1-\varepsilon&\varepsilon\\
 \varepsilon&1-\varepsilon
 \end{pmatrix}.$$ We view a block law as a column vector, so the memoryless channel maps the clean length-$\ell$ law to $C_\varepsilon^{\otimes\ell}p_{0,\ell}$.

[\[thm:gap\]]{#thm:gap label="thm:gap"} Let $k\geq3$ and $L=k+1$. For every $\varepsilon\in[0,1]\setminus\{\tfrac12\}$, $$\begin{aligned}
 \bigl\|p_{\varepsilon,L}-Rp_{\varepsilon,L}\bigr\|_2
 &\geq
 \sqrt{2}\,2^{-k}|1-2\varepsilon|^{k+1},
 \label{eq:l2-gap}\\
 \operatorname{TV}\!\left(p_{\varepsilon,L},Rp_{\varepsilon,L}\right)
 &\geq
 2^{-k}|1-2\varepsilon|^{k+1}.
 \label{eq:tv-gap}\end{aligned}$$ The smallest block length at which the law differs from its reversal is therefore exactly $k+1$. At $\varepsilon=\tfrac12$, $Y$ is a fair independent process and is reversible at every length.

Set $$\Delta_0=p_{0,L}-Rp_{0,L},
 \qquad
 \Delta_\varepsilon=p_{\varepsilon,L}-Rp_{\varepsilon,L}.$$ The clean length-$L$ words at different phases are distinct because their length-$k$ prefixes are distinct. By [\[lem:witness\]](#lem:witness){reference-type="ref" reference="lem:witness"}, $$\Delta_0(u_k)=2^{-k},
 \qquad
 \Delta_0(\operatorname{rev}(u_k))=-2^{-k}.$$ Thus $$\label{eq:clean-norms}
 \|\Delta_0\|_2\geq\sqrt{2}\,2^{-k},
 \qquad
 \|\Delta_0\|_1\geq2^{1-k}.$$

Coordinatewise reversal commutes with the identical memoryless channel on each coordinate. Hence $$\Delta_\varepsilon=C_\varepsilon^{\otimes L}\Delta_0.$$ The singular values of $C_\varepsilon$ are $1$ and $|1-2\varepsilon|$. The least singular value of its $L$th tensor power is $|1-2\varepsilon|^L$, which together with [\[eq:clean-norms\]](#eq:clean-norms){reference-type="eqref" reference="eq:clean-norms"} proves [\[eq:l2-gap\]](#eq:l2-gap){reference-type="eqref" reference="eq:l2-gap"}.

For the total-variation bound, $C_\varepsilon$ is invertible away from $\tfrac12$, and direct calculation gives $$\|C_\varepsilon^{-1}\|_{1\to1}
 =|1-2\varepsilon|^{-1}.$$ The induced $\ell^1$ norm is multiplicative under tensor products. Therefore $$\|\Delta_0\|_1
 \leq |1-2\varepsilon|^{-L}\|\Delta_\varepsilon\|_1.$$ Use [\[eq:clean-norms\]](#eq:clean-norms){reference-type="eqref" reference="eq:clean-norms"} and $\operatorname{TV}(p,q)=\tfrac12\|p-q\|_1$ to obtain [\[eq:tv-gap\]](#eq:tv-gap){reference-type="eqref" reference="eq:tv-gap"}.

The laws at all shorter lengths agree with their reversals by [\[lem:uniform\]](#lem:uniform){reference-type="ref" reference="lem:uniform"}; the positive lower bounds prove the exact onset at $L$. If $\varepsilon=\tfrac12$, each output bit is an independent fair bit regardless of the hidden source.

[\[rem:noisy-witness\]]{#rem:noisy-witness label="rem:noisy-witness"} The word $u_k$ is an explicit witness for the *clean* defect. The tensor argument proves that some noisy cylinder remains asymmetric and quantifies the global gap. We do not assert here that the same cylinder $u_k$ witnesses the noisy defect for every $k$ and every noise parameter. Also, the word *exact* in [\[thm:gap\]](#thm:gap){reference-type="ref" reference="thm:gap"} refers to the first detectable block length, not to equality in the norm bounds.

# Entropy, phase recovery, and memory

Write $$h_{\mathrm b}(\varepsilon)
 =-\varepsilon\log_2\varepsilon
  -(1-\varepsilon)\log_2(1-\varepsilon),$$ with the usual convention $0\log_2 0=0$.

[\[thm:entropy\]]{#thm:entropy label="thm:entropy"} For every $k\geq1$ and $\varepsilon\in[0,1]$, the Shannon entropy rate of $Y$ is $$h(Y)=h_{\mathrm b}(\varepsilon)\quad\text{bits per symbol}.$$

Conditional on $U$, the clean sequence is fixed and the observed symbols are independent, each with entropy $h_{\mathrm b}(\varepsilon)$. If $H_n=H(Y_0,\ldots,Y_{n-1})$, then $$nh_{\mathrm b}(\varepsilon)
 =H(Y_0^{n-1}\mid U)
 \leq H_n
 \leq H(Y_0^{n-1},U)
 =nh_{\mathrm b}(\varepsilon)+H(U).$$ Since $H(U)=\log_2N=k$, division by $n$ and passage to the limit proves the claim. The same inequalities include the deterministic-noise endpoints.

Closed entropy-rate formulas are exceptional for general hidden Markov processes [@JacquetEtAl2008]. Here the hidden uncertainty is one finite phase variable, so it contributes only a bounded block-entropy correction. We next determine that correction exactly.

[\[thm:recovery\]]{#thm:recovery label="thm:recovery"} If $\varepsilon\neq\tfrac12$, each infinite one-sided observation determines the phase almost surely. More precisely, there are estimators based on $Y_0,\ldots,Y_{n-1}$, and likewise on $Y_{-n},\ldots,Y_{-1}$, that are eventually equal to $U$ almost surely. Consequently $$H(U\mid Y_0,\ldots,Y_{n-1})\longrightarrow0$$ and the analogous conditional entropy given the finite past also tends to zero.

First suppose $0<\varepsilon<1$ and $\varepsilon\neq\tfrac12$. For a candidate phase $v$, let $$\mathcal L_n(v)
 =\prod_{t=0}^{n-1}
 \mathbb P(Y_t\mid d_{v+t\pmod N})$$ be its conditional likelihood. Distinct cyclic shifts of $D_k$ differ: otherwise $D_k$ would have period less than $N$. Let $m(u,v)\geq1$ be the number of positions in one period where phases $u$ and $v$ differ.

Under the true phase $u$, the expected log-likelihood advantage over $v$ in one period is $$\label{eq:kl-drift}
 m(u,v)\,(1-2\varepsilon)
 \log\frac{1-\varepsilon}{\varepsilon}>0.$$ Indeed, positions where the two clean symbols agree contribute zero. At a disagreement, the observed symbol equals the true clean symbol with probability $1-\varepsilon$ and the other symbol with probability $\varepsilon$, which gives the factor in [\[eq:kl-drift\]](#eq:kl-drift){reference-type="eqref" reference="eq:kl-drift"}. Contributions from successive periods are independent and bounded. The strong law of large numbers implies $$\frac1n\log\frac{\mathcal L_n(u)}{\mathcal L_n(v)}
 \longrightarrow
 \frac{m(u,v)}{N}(1-2\varepsilon)
 \log\frac{1-\varepsilon}{\varepsilon}>0$$ almost surely. There are only $N-1$ false phases, so the maximum-likelihood phase is eventually $u$, and the posterior probability of $u$ tends to one. Because $U$ is finite-valued, posterior concentration also gives convergence of the conditional entropy to zero.

The past proof is identical after replacing $t$ by $-t$, or follows by applying the same likelihood argument to the reversed cyclic patterns. At $\varepsilon=0$, a clean length-$k$ block identifies its unique phase in the de Bruijn cycle. At $\varepsilon=1$, complementing the observation first reduces to the same argument.

[\[cor:excess\]]{#cor:excess label="cor:excess"} Define the excess entropy by $$\mathbf E(Y)=\lim_{n\to\infty}\bigl(H_n-nh(Y)\bigr).$$ Then $$\mathbf E(Y)=
 \begin{cases}
 k,&\varepsilon\neq\tfrac12,\\
 0,&\varepsilon=\tfrac12.
 \end{cases}$$

Conditional independence given the phase gives the exact identity $$H_n=nh_{\mathrm b}(\varepsilon)+I(U;Y_0^{n-1}).$$ For $\varepsilon\neq\tfrac12$, [\[thm:recovery\]](#thm:recovery){reference-type="ref" reference="thm:recovery"} implies that the mutual information tends to $H(U)=k$. At $\varepsilon=\tfrac12$, $Y$ is independent of $U$ and is fair independent, so the mutual information is zero for every $n$.

[\[thm:markov\]]{#thm:markov label="thm:markov"} Let $0<\varepsilon<1$ and $\varepsilon\neq\tfrac12$. The observed process $Y$ is not a Markov process of any finite order. At $\varepsilon=\tfrac12$ it is independent and hence has Markov order zero. At $\varepsilon=0$ and $\varepsilon=1$, it has Markov order exactly $k$.

For strictly noisy nonfair emissions, the infinite past recovers $U$ by [\[thm:recovery\]](#thm:recovery){reference-type="ref" reference="thm:recovery"}. Since $Z_0$ is independent of the past, $$\label{eq:past-predictor}
 \mathbb P(Y_0=1\mid Y_{-\infty}^{-1})
 =\varepsilon+(1-2\varepsilon)d_U
 \quad\text{almost surely}.$$ Fix any proposed order $r$ and any word $w\in\{0,1\}^r$. Full support of the emissions implies $$\mathbb P(U=u,\;Y_{-r}^{-1}=w)>0$$ for every phase $u$. The de Bruijn cycle contains phases $u_0,u_1$ with $d_{u_0}=0$ and $d_{u_1}=1$. On positive-probability sets with the same length-$r$ suffix $w$, the right side of [\[eq:past-predictor\]](#eq:past-predictor){reference-type="eqref" reference="eq:past-predictor"} is respectively $\varepsilon$ and $1-\varepsilon$. It cannot be a function of the last $r$ observations. Since $r$ was arbitrary, no finite Markov order exists.

At fair noise the output is independent. At a deterministic-noise endpoint, the last $k$ observed bits, after complementing when necessary, locate the unique phase and determine the next bit. A $(k-1)$-word occurs twice in an order-$k$ de Bruijn cycle, once followed by $0$ and once followed by $1$, because its two length-$k$ extensions each occur once. Thus order $k-1$ does not suffice, and the endpoint Markov order is exactly $k$.

[\[prop:nonmixing\]]{#prop:nonmixing label="prop:nonmixing"} For every $\varepsilon\neq\tfrac12$, the process $Y$ is not mixing. In fact, if $A_t=(-1)^{Y_t}$, then $\mathbb EA_t=0$ and, for every integer $m\geq1$, $$\operatorname{Cov}(A_0,A_{mN})=(1-2\varepsilon)^2.$$ At $\varepsilon=\tfrac12$, $Y$ is independent and therefore mixing.

An order-$k$ de Bruijn cycle contains equally many zeros and ones, so $\mathbb EA_t=0$. Write $$A_t=(-1)^{X_t}(-1)^{Z_t}.$$ At lag $mN$, the clean signs agree. The two noise variables are independent and each has sign mean $1-2\varepsilon$. Their product expectation is $(1-2\varepsilon)^2$, proving the displayed covariance. It does not decay along multiples of $N$ unless $\varepsilon=\tfrac12$.

# Exceptional parameters and small orders

For reference, [1](#tab:regimes){reference-type="ref" reference="tab:regimes"} collects the regimes for $k\geq3$.

::: {#tab:regimes}
  -------------------------------------------------------------------------------------------------------------------------
  Property                $\varepsilon\in\{0,1\}$   $0<\varepsilon<1$, $\varepsilon\neq\tfrac12$   $\varepsilon=\tfrac12$
  ----------------------- ------------------------- ---------------------------------------------- ------------------------
  Topological support     one periodic orbit        full binary shift                              full binary shift

  Ergodic                 yes                       yes                                            yes

  Mixing                  no                        no                                             yes, independent

  First reversal defect   $k+1$                     $k+1$                                          none

  Entropy rate            $0$                       $h_{\mathrm b}(\varepsilon)$                   $1$

  Excess entropy          $k$                       $k$                                            $0$

  Markov order            exactly $k$               infinite                                       $0$

  Phase recoverable       yes                       yes                                            no
  -------------------------------------------------------------------------------------------------------------------------

  : Complete parameter split for the order-$k$ FKM process with $k\geq3$. Full support requires strictly positive probabilities for both emissions; phase recovery and reversal asymmetry instead fail only at fair noise.
:::

The small orders explain the threshold $k\geq3$ in [\[lem:witness,thm:gap\]](#lem:witness,thm:gap){reference-type="ref" reference="lem:witness,thm:gap"}. The FKM cycles are $$D_1=01,\qquad D_2=0011.$$ Their reversed cycles are cyclic rotations of the originals. Uniform phase therefore makes the clean processes reversible, and a coordinatewise memoryless channel preserves reversibility. Hence the order-one and order-two FKM phase processes are reversible for every $\varepsilon$.

# Direct ownership boundary {#sec:ownership}

The clean construction and its local block laws are classical. The FKM theorem owns the Lyndon concatenation and its de Bruijn property [@FredricksenMaiorana1978; @AmramEtAl2025]. Work on normality and higher-order diagnostics already emphasizes that de Bruijn blocks can be maximally equidistributed locally while retaining strong ordered structure [@PincusSinger2014]. Hidden Markov and sofic-measure viewpoints, as well as general definitions and mechanisms of stochastic time irreversibility, are also established [@BoylePetersen2010; @EllisonEtAl2011].

Mohri et al. provide the closest direct precedent [@MohriEtAl2026 Sec. 4.1]. Given an arbitrary order-$L$ de Bruijn cycle, they seed the first $L$ tokens uniformly and then follow its deterministic successor. In a stationary two-sided extension, that deterministic model is exactly the clean uniform-phase construction used here. Their length-$L$ context distribution is uniform. They also note that positive mass can be added to the opposite successor to give full support.

The noise mechanisms are different. In the transition perturbation, the currently emitted length-$L$ context is the state used to select the next token; an error changes the subsequent context. In [\[eq:process\]](#eq:process){reference-type="eqref" reference="eq:process"}, the latent phase advances deterministically and an error affects only the current observation. Under strictly noisy, nonfair emissions, the latter produces the infinite observed Markov order; for every nonfair emission it produces persistent periodic correlations and exact $k$-bit excess entropy. Our residual result is therefore an explicit combination of an FKM oriented edge and BSC tensor lower bounds with persistent-phase information and mixing invariants. We make no claim that uniform random phase, local uniformity, generic noisy de Bruijn models, or the surrounding hidden-Markov framework originate here.

::: {#tab:ownership}
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Line of work                  Directly owned ingredient                                                                                   Role of the present note
  ----------------------------- ----------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  FKM theory                    Lyndon concatenation and the lexicographically least de Bruijn cycle                                        Uses the explicit first three Lyndon factors to orient one $(k+1)$-edge

  Higher-order diagnostics      Local equidistribution need not control ordered higher-order behavior                                       Uses reversal, rather than partial sums or normal-number bias, as the diagnostic

  Mohri et al. (2026)           Uniformly seeded de Bruijn successor model and uniform $L$-contexts; transition-noise full-support remark   Keeps a persistent latent phase and applies independent emission noise

  Hidden Markov reversibility   General representation and time-reversal frameworks                                                         Computes the first reversal scale and explicit norm bounds for this family
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Prior ownership and the deliberately narrow residual contribution. The table is a scope boundary, not a priority assertion.
:::

# Exact finite controls

The accompanying script `code/verify_noisy_debruijn.py` provides independent finite regression checks. It constructs $D_k$ by the FKM recursion, verifies every short-block multiplicity, checks the oriented witness, computes exact rational noisy block laws for several orders and crossover probabilities, and tests both lower bounds. It also verifies positive cyclic-shift Hamming distance, the periodic covariance formula, and the reversible small-order exceptions. These calculations audit the formulas; the proofs above apply to all orders and all parameters in their stated ranges.

# Limitations and conclusion

The Euclidean and total-variation inequalities are uniform lower bounds, not closed forms for the full reversal gap. They intentionally avoid an unproved assertion that the clean witness remains the same noisy witness. The construction is binary and tied to the lexicographically least FKM cycle; other alphabets and other de Bruijn successor classes require a separate oriented-edge analysis. Finally, full support does not imply mixing here because emission errors never reset the phase.

Within those boundaries, the family gives a sharp delayed-time-arrow example. Every consecutive statistic through order $k$ is exactly that of a fair independent process. The first reversal defect appears at $k+1$, survives every invertible binary symmetric channel with an explicit quantitative guarantee, and coexists with an exact entropy decomposition. The result isolates how a finite hidden phase can be invisible to all prescribed local tests while remaining recoverable from one infinite side.
