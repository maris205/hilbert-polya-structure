---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--170-random-permutation-fixed-point-sieve"
canonical_tex: "symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve/main.tex"
canonical_pdf: "symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve/main.pdf"
source_sha256: "5ca548eeecf686c16599bebe85b2e18c94f93ada2d577b6e8f5771b390711e74"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Endpoint Histories in a Random-Permutation Fixed-Point Sieve

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/170-random-permutation-fixed-point-sieve/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $n\ge2$. At each epoch choose a uniform permutation of $[n]$ and intersect the current subset with its fixed-point set. We give the exact history count between every ordered pair of subsets and diagonalize the transition operator in the Boolean containment basis. The resulting absorption law includes its probability generating function, first two moments, and a necessary separate boundary formula at $n=3$, where the second and third spectral scales coincide. We then retain the total cycle count of every sampled permutation. For every supported endpoint, its history polynomial has an inclusion--exclusion form, sharp lowest and highest degrees $$t\bigl(|B|+\mathbf 1_{\{|B|<n\}}\bigr)
   \quad\hbox{and}\quad
   tn-\Bigl\lceil\frac{|A|-|B|}{2}\Bigr\rceil,$$ and an exact conditional total-cycle expectation. Common fixed points, fixed-set inclusion--exclusion, semilattice spectra, and ordinary cycle polynomials are treated as background; the external status is [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: 'Endpoint Histories in a Random-Permutation Fixed-Point Sieve'
```

## Markdown 正文

# The literal process and the theorem package

Write $[n]=\{1,\ldots,n\}$ and $2^{[n]}$ for its power set. Let $\pi_1,\pi_2,\ldots$ be independent uniform elements of $S_n$. Starting from $A_0=A$, apply the literal update $$\label{eq:update}
             A_r=A_{r-1}\cap\operatorname{Fix}(\pi_r).$$ Thus no action on the complement is implicit and no missing-label convention is needed. For $B\subseteq A$, put $$a=|A|,\qquad b=|B|,\qquad d=a-b,
 \qquad \lambda_j=\frac{(n-j)!}{n!}.$$ Let $K_t(A,B)$ be the number of length-$t$ permutation histories ending at $B$. If $T=\min\{t:A_t=\varnothing\}$, the empty initial state has $T=0$.

The common-fixed-point object is part of the random-permutation and word- measure background [@HananyPuder2023]; fixed-point-set laws and their inclusion--exclusion are classical and appear explicitly in [@DiaconisEvansGraham2014]. Walks on idempotent semigroups already come with lattice and representation-theoretic spectral mechanisms [@Brown2000; @AyyerEtAl2015]. We therefore assign no separate contribution to the unmarked kernel, containment spectrum, or standard tail transforms. They are included so that the endpoint-conditioned cycle calculation can be read without imported machinery.

For a history, set $C_t=\sum_{r=1}^t\operatorname{cyc}(\pi_r)$, counting fixed points as cycles, and define $$\label{eq:marked-def}
 M_t(A,B;u)=\sum_{A_t=B}u^{C_t}.$$ Also put $H_m=\sum_{q=1}^m q^{-1}$ and $H_0=0$.

[\[thm:main\]]{#thm:main label="thm:main"} For the process [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, the following statements hold.

(i) For every $t\ge0$, $$\label{eq:kernel}
     K_t(A,B)=\sum_{j=0}^{d}(-1)^j\binom dj(n-b-j)!^t
     \quad(B\subseteq A),$$ and $K_t(A,B)=0$ otherwise. For $t\ge1$ this count is positive precisely when $B\subseteq A$ and it is not the case that $A=[n]$ and $|B|=n-1$.

(ii) For $S\subseteq[n]$, the $2^n$ functions $\phi_S(A)=\mathbf 1_{\{S\subseteq A\}}$ form an eigenbasis of the one-step probability operator, with eigenvalue $\lambda_{|S|}$. The only equality between two different rank eigenvalues is $\lambda_{n-1}=\lambda_n=1/n!$.

(iii) If $A\ne\varnothing$, then for $t\ge0$, $$\begin{aligned}
       \mathbb P_A(T\le t)&=\sum_{j=0}^a(-1)^j\binom aj\lambda_j^t,
       \label{eq:cdf}\\
       \mathbb P_A(T>t)&=\sum_{j=1}^a(-1)^{j+1}\binom aj\lambda_j^t.\label{eq:survival}\end{aligned}$$ Moreover, $$\begin{aligned}
       \mathbb E_A T&=\sum_{j=1}^a(-1)^{j+1}\binom aj\frac1{1-\lambda_j},
       \label{eq:mean}\\
       \mathbb E_A T^2&=\sum_{j=1}^a(-1)^{j+1}\binom aj
             \frac{1+\lambda_j}{(1-\lambda_j)^2},\label{eq:second}\\
       \mathbb E_A s^T&=1-(1-s)\sum_{j=1}^a(-1)^{j+1}\binom aj
             \frac1{1-s\lambda_j}\label{eq:pgf}\end{aligned}$$ for $|s|<\lambda_1^{-1}=n$, with the last expression also giving the rational continuation.

(iv) The low-dimensional boundaries are $$\begin{aligned}
      n=1 &: \quad \{1\}\text{ never absorbs},\\
      n=2 &: \quad \mathbb P_A(T>t)=2^{-t}\quad(A\ne\varnothing),\\
      n=3 &: \quad \mathbb P_A(T>t)=a3^{-t}
            -\bigl(\tbinom a2-\tbinom a3\bigr)6^{-t}.\end{aligned}$$ Only for $n\ge4$ do the first two distinct scales give $$\label{eq:asymptotic}
      \mathbb P_A(T>t)=a n^{-t}-\binom a2[n(n-1)]^{-t}
                      +O(\lambda_3^t).$$

(v) Define $$\label{eq:Rns}
     R_{n,s}(u)=u^s\prod_{q=0}^{n-s-1}(u+q).$$ Then every endpoint has the exact marked-history polynomial $$\label{eq:marked}
     M_t(A,B;u)=\sum_{j=0}^{d}(-1)^j\binom dj
                  R_{n,b+j}(u)^t
     \quad(B\subseteq A),$$ and zero otherwise. Its coefficients are nonnegative and $M_t(A,B;1)=K_t(A,B)$.

(vi) Suppose $t\ge1$ and the endpoint is supported as in part (i). The least and greatest exponents with nonzero coefficient in $M_t(A,B;u)$ are, sharply, $$\label{eq:extrema}
      L_t(b)=t\bigl(b+\mathbf 1_{\{b<n\}}\bigr),
      \qquad U_t(a,b)=tn-\left\lceil\frac d2\right\rceil.$$ For the same endpoint, $$\label{eq:conditional}
      \mathbb E[C_t\mid A_t=B]
      =\frac{t\displaystyle\sum_{j=0}^{d}(-1)^j\binom dj
            (n-b-j)!^t\bigl(b+j+H_{n-b-j}\bigr)}
      {K_t(A,B)}.$$

Part (iv) is stated separately on purpose: at $n=3$, $\lambda_2=\lambda_3=1/6$, so folding the cubic term into a purportedly smaller remainder would be incorrect.

# Unmarked histories, spectrum, and absorption

Iteration of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} gives the pathwise identity $$\label{eq:pathwise}
 A_t=A\cap\operatorname{Fix}(\pi_1)\cap\cdots\cap\operatorname{Fix}(\pi_t).$$ This immediately yields the endpoint kernel, but we record the support boundary because it will also control the marked statements.

Assume $B\subseteq A$. Every point of $B$ must be fixed at all $t$ epochs, while every point of $D=A\setminus B$ must be moved at least once. If a chosen $j$-set in $D$ is also forced to be fixed throughout, each epoch has $(n-b-j)!$ choices. Inclusion--exclusion on $D$ proves [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}; at $t=0$ its alternating binomial sum is the Kronecker delta.

For positive time, fixing $n-1$ points forces the last point, so the stated exception is impossible. Conversely, if $d\ge2$, derange $D$ at one epoch and use identities thereafter. If $d=1$, support excludes $A=[n]$; transpose the lost point with a point outside $A$. If $d=0$, use identities. Each construction fixes $B$ and has endpoint exactly $B$.

Let $P$ act on functions by $(Pf)(A)=(n!)^{-1}\sum_{\pi\in S_n}f(A\cap\operatorname{Fix}(\pi))$.

The event $S\subseteq A\cap\operatorname{Fix}(\pi)$ requires $S\subseteq A$ and has exactly $(n-|S|)!$ realizing permutations. Hence $P\phi_S=\lambda_{|S|}\phi_S$. The matrix $(\phi_S(A))_{A,S}$ is the Boolean zeta matrix, with inverse $(-1)^{|A\setminus S|}\mathbf 1_{\{S\subseteq A\}}$; the displayed functions therefore form a basis. Finally, the factorials $n!, (n-1)!,\ldots,1!,0!$ decrease strictly except for $1!=0!$, proving the last assertion.

Set $B=\varnothing$ in [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} and divide by $(n!)^t$ to obtain [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}; its complement is [\[eq:survival\]](#eq:survival){reference-type="eqref" reference="eq:survival"}. For $n\ge2$ all $\lambda_j<1$ when $j\ge1$. Summing $\mathbb ET=\sum_{t\ge0}\mathbb P(T>t)$ and $\mathbb ET^2=\sum_{t\ge0}(2t+1)\mathbb P(T>t)$ gives [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}--[\[eq:second\]](#eq:second){reference-type="eqref" reference="eq:second"}. The tail identity $$\mathbb Es^T=1-(1-s)\sum_{t\ge0}s^t\mathbb P(T>t)$$ gives [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"} in its disk of absolute convergence.

For $n=1$ the only permutation fixes the sole point. At $n=2$, $\lambda_1=\lambda_2=1/2$, and the binomial coefficients in [\[eq:survival\]](#eq:survival){reference-type="eqref" reference="eq:survival"} combine to one. At $n=3$, $\lambda_1=1/3$ and $\lambda_2=\lambda_3=1/6$, giving the stated exact formula. For $n\ge4$, $\lambda_1>\lambda_2>\lambda_3$, and the remaining finite terms in [\[eq:survival\]](#eq:survival){reference-type="eqref" reference="eq:survival"} are $O(\lambda_3^t)$.

# Cycle-marked endpoint histories

The ordinary cycle polynomial of a permutation group is standard [@CameronSemeraro2018]. In particular, $\sum_{\sigma\in S_m}u^{\operatorname{cyc}(\sigma)}=u(u+1)\cdots(u+m-1)$: inserting the largest label either creates a new singleton cycle, with weight $u$, or inserts it after one of the $m-1$ existing labels. Thus, if $s$ prescribed labels are fixed, their singleton cycles contribute $u^s$ and the remaining labels give exactly [\[eq:Rns\]](#eq:Rns){reference-type="eqref" reference="eq:Rns"}. This factor is background; the endpoint conditioning is retained explicitly below.

Force every point of $B$ to be fixed at all epochs and apply inclusion--exclusion to the points of $D=A\setminus B$ that must fail to be fixed at least once. If a $j$-subset of $D$ is additionally fixed, the cycle enumerator for one epoch is $R_{n,b+j}(u)$; independence makes its $t$th power. This proves [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"}. Nonnegativity follows from the literal sum [\[eq:marked-def\]](#eq:marked-def){reference-type="eqref" reference="eq:marked-def"}, not from cancellation in the displayed alternating form. At $u=1$, $R_{n,s}(1)=(n-s)!$, recovering [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}.

The specialization $u=1$ discards information: even when it determines the total number of endpoint histories, it does not determine the cycle range or conditional cycle mean.

Every sampled permutation fixes the $b$ labels of $B$. If $b<n$, the remaining labels contain at least one further cycle, so each epoch has at least $b+1$ cycles. If $b=n$, only the identity occurs. The lower bound in [\[eq:extrema\]](#eq:extrema){reference-type="eqref" reference="eq:extrema"} is attained by fixing $B$ and using one cycle on $[n]\setminus B$ at every epoch. When that complement has size one, support forces $A=B$, and its singleton cycle is harmless.

For the upper bound, define the cycle deficit $\delta(\pi)=n-\operatorname{cyc}(\pi)$. A nontrivial $\ell$-cycle moves $\ell$ points and contributes $\ell-1$ to $\delta$; since $\ell\le2(\ell-1)$, $$\label{eq:support-deficit}
 |\operatorname{supp}(\pi)|\le2\delta(\pi).$$ Every one of the $d$ lost labels is moved at some epoch. Taking the union of moved supports and then using [\[eq:support-deficit\]](#eq:support-deficit){reference-type="eqref" reference="eq:support-deficit"} gives $$d\le\sum_{r=1}^t|\operatorname{supp}(\pi_r)|
   \le2\sum_{r=1}^t\delta(\pi_r),$$ and hence $C_t\le tn-\lceil d/2\rceil$.

It remains to realize equality, including the exceptional parity cases. If $d>0$ is even, pair the labels of $D$ into transpositions at one epoch. If $d\ge3$ is odd, use one $3$-cycle on $D$ and pair the remaining labels. If $d=1$, the support criterion gives a label outside $A$; transpose it with the lost label. For $d=0$, use the identity. In every case, use identities at the other epochs. The construction fixes $B$, moves every lost label, and has total deficit $\lceil d/2\rceil$. Thus the endpoint coefficient at each asserted extreme is positive.

Logarithmic differentiation of [\[eq:Rns\]](#eq:Rns){reference-type="eqref" reference="eq:Rns"} at $u=1$ gives $$\frac{R'_{n,s}(1)}{R_{n,s}(1)}
 =s+\sum_{q=0}^{n-s-1}\frac1{1+q}=s+H_{n-s}.$$ Differentiate [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"}, use $R_{n,s}(1)=(n-s)!$, and divide by the positive value $M_t(A,B;1)=K_t(A,B)$. Since $M'_t(A,B;1)/M_t(A,B;1)$ is the mean exponent under the uniform conditional history law, the result is [\[eq:conditional\]](#eq:conditional){reference-type="eqref" reference="eq:conditional"}.

# Claim boundary and exact pressure

The retained statement is the endpoint-resolved conjunction in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(v)--(vi), especially its sharp marked range and conditional mean. No claim is made for the priority of the ingredients: common fixed points, prescribed fixed labels, inclusion--exclusion, Boolean Möbius inversion, semilattice spectra, standard absorption transforms, and the rising-factorial cycle polynomial all receive zero contribution credit. Bounded source searches found no exact owner for the full marked endpoint-conditioned package, but a search non-hit is not evidence of priority. External circulation remains [hold\_external]{.smallcaps}.

The accompanying standard-library verifier enumerates permutations and labelled subset histories literally, checks [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} and [\[eq:marked\]](#eq:marked){reference-type="eqref" reference="eq:marked"} coefficientwise, constructs all sharpness parity cases, and independently solves the size-projected absorbing chain over exact rationals. Its finite boxes are counterexample pressure, not a proof or an ownership certificate.
