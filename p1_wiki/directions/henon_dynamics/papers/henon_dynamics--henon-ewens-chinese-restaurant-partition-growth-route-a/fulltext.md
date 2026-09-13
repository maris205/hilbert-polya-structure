---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-ewens-chinese-restaurant-partition-growth-route-a"
canonical_tex: "henon_dynamics/henon_ewens_chinese_restaurant_partition_growth_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_ewens_chinese_restaurant_partition_growth_route_a/paper/main.pdf"
source_sha256: "f335e2515da02e740ff19b7e82b781438a9eac6599e8957ecfaffdc4d57a8af1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# From Restaurant Growth to an Exact Partition Atlas: Ewens Laws, Block-Count Fluctuations, and Poisson Limits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_ewens_chinese_restaurant_partition_growth_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_ewens_chinese_restaurant_partition_growth_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_ewens_chinese_restaurant_partition_growth_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_ewens_chinese_restaurant_partition_growth_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We carry the one-parameter Chinese-restaurant insertion rule through a complete finite and asymptotic partition atlas. A labelled-partition induction proves exchangeability and the Ewens sampling formula; exact counting gives the full occupancy-vector law. The total number of blocks is factored into independent Bernoulli innovations, yielding its exact probability generating polynomial, almost-sure logarithmic law, and variance-normalized central limit theorem. A separate mixed falling-factorial identity proves joint independent-Poisson limits for every fixed collection of block sizes. A 5,238-row exact certificate checks finite coefficients and conventions but does not replace the asymptotic proofs. No priority or arithmetic-target claim is made.
author:
- 'HCS-C353 source-local reconstruction'
date: 3 September 2026
title: |
  From Restaurant Growth to an Exact Partition Atlas:\
  Ewens Laws, Block-Count Fluctuations, and Poisson Limits
```

## Markdown 正文

**Revision certificate.** =0 Exchangeability, EPPF, and exact occupancy-law closure. =1 Round-one innovation factorization, strong-law, and CLT closure. Round-two Poisson-limit, boundary, evidence, and Route-A closure.

# Growth rule and complete theorem

Fix $\theta>0$. Set $\Pi_1=\{\{1\}\}$. Given a partition $\Pi_n$ of $[n]=\{1,\ldots,n\}$, customer $n+1$ starts a singleton block with probability $\theta/(\theta+n)$, or joins an existing block $B$ with probability $|B|/(\theta+n)$. Let $K_n=|\Pi_n|$ and let $C_j(n)$ be the number of blocks of size $j$. Write $(a)^{\overline{n}}=a(a+1)\cdots(a+n-1)$ and use $(x)_{\underline{r}}=x(x-1)\cdots(x-r+1)$.

[\[thm:main\]]{#thm:main label="thm:main"} For the preceding process:

1.  $\Pi_n$ is exchangeable. A particular labelled partition $\{B_1,\ldots,B_k\}$ has probability $$\mathbb P(\Pi_n=\{B_1,\ldots,B_k\})
     =\frac{\theta^k}{(\theta)^{\overline{n}}}
       \prod_{i=1}^k(|B_i|-1)!.                              \tag{1}$$

2.  If $c_1,\ldots,c_n\geq0$ and $\sum_j j c_j=n$, then $$\mathbb P(C_j(n)=c_j,1\leq j\leq n)
     =\frac{n!}{(\theta)^{\overline{n}}}
       \prod_{j=1}^n\frac{(\theta/j)^{c_j}}{c_j!}.            \tag{2}$$

3.  There are independent Bernoulli variables $I_i$ with $\mathbb P(I_i=1)=\theta/(\theta+i-1)$ such that $K_n=\sum_{i=1}^nI_i$. Consequently $$\mathbb E z^{K_n}=\frac{(\theta z)^{\overline{n}}}
                              {(\theta)^{\overline{n}}}.            \tag{3}$$

4.  As $n\to\infty$, $$\frac{K_n}{\log n}\longrightarrow\theta\quad\hbox{almost surely},
     \qquad
     \frac{K_n-\mathbb EK_n}{\sqrt{\operatorname{Var}K_n}}
     \Longrightarrow N(0,1).                                \tag{4}$$

5.  For every fixed $m$, $$(C_1(n),\ldots,C_m(n))\Longrightarrow(Z_1,\ldots,Z_m),
     \qquad Z_j\ \hbox{independent},\quad Z_j\sim
     \operatorname{Poisson}(\theta/j).                       \tag{5}$$

# Labelled induction and the occupancy law

Formula (1) holds at $n=1$. Assume it at $n$. If $n+1$ creates a new block, multiplication by $\theta/(\theta+n)$ adds one power of $\theta$ and the next rising-factorial denominator. If it joins a block of size $b$, multiplication by $b/(\theta+n)$ changes $(b-1)!$ to $b!$. Every labelled partition at time $n+1$ has a unique predecessor obtained by deleting label $n+1$, so induction proves (1) without multiplicity ambiguity. Its dependence only on block sizes proves exchangeability.

For a count vector $c=(c_1,\ldots,c_n)$, the number of labelled set partitions with those counts is $$\frac{n!}{\prod_{j=1}^n(j!)^{c_j}c_j!}.                 \tag{6}$$ Multiplying (6) by (1), with $\prod_i(|B_i|-1)!=\prod_j((j-1)!)^{c_j}$, gives (2). Summing (2) also yields $$(\theta)^{\overline{n}}=\sum_{k=1}^n c(n,k)\theta^k,$$ where $c(n,k)$ is the unsigned Stirling number of the first kind.

\>0

# Independent innovations, strong law, and CLT

Let $I_i$ indicate that customer $i$ opens a new block; $I_1=1$. Crucially, $$\mathbb P(I_i=1\mid\Pi_1,\ldots,\Pi_{i-1})
 =p_i:=\frac{\theta}{\theta+i-1}                         \tag{7}$$ is deterministic. Iterated conditioning therefore factors every finite joint event in the $I_i$, proving mutual independence rather than merely uncorrelatedness. Since $K_n=\sum I_i$, multiplying their Bernoulli PGFs gives (3). In particular $$\begin{aligned}
 a_n:=\mathbb EK_n&=\sum_{i=1}^np_i=\theta\log n+O(1),\\
 v_n:=\operatorname{Var}K_n&=\sum_{i=1}^np_i(1-p_i)
                         =\theta\log n+O(1).              \tag{8}\end{aligned}$$ The second estimates use $p_i=\theta/i+O(i^{-2})$ and $\sum_i p_i^2<\infty$.

Set $X_i=I_i-p_i$. Independence and $$\sum_{i\geq2}\frac{\operatorname{Var}X_i}{(\log i)^2}<\infty$$ imply, by the Kolmogorov convergence theorem, that $\sum_{i\geq2}X_i/\log i$ converges almost surely. Kronecker's lemma gives $\sum_{i\leq n}X_i/\log n\to0$ almost surely. Combining this with (8) proves the first limit in (4).

For the second, $v_n\to\infty$ while $|X_i|\leq1$. Thus for every $\varepsilon>0$, the Lindeberg indicators $\mathbf1_{\{|X_i|>\varepsilon\sqrt{v_n}\}}$ vanish identically once $n$ is large. The Lindeberg--Feller theorem proves the centered, variance-normalized limit in (4).

\>1

# Mixed factorial moments and the Poisson limit

Fix nonnegative integers $r_1,\ldots,r_m$ and put $s=\sum_{j=1}^mjr_j$. Selecting an ordered family of $r_j$ disjoint $j$-sets from $[n]$ can be done in $$\frac{(n)_{\underline{s}}}{\prod_{j=1}^m(j!)^{r_j}}$$ ways. Requiring those sets to be blocks contributes $\theta^{\sum r_j}\prod_j((j-1)!)^{r_j}$, while summing the EPPF over the unmarked labels contributes $(\theta)^{\overline{n-s}}/(\theta)^{\overline{n}}$. Therefore, for $s\leq n$, $$\mathbb E\prod_{j=1}^m(C_j(n))_{\underline{r_j}}
 =\frac{(n)_{\underline{s}}(\theta)^{\overline{n-s}}}
        {(\theta)^{\overline{n}}}
   \prod_{j=1}^m\left(\frac\theta j\right)^{r_j}.         \tag{9}$$ For fixed $s$ the leading ratio in (9) tends to one. Hence every mixed falling-factorial moment tends to $\prod_j(\theta/j)^{r_j}$, exactly the mixed factorial moment of independent Poisson variables with means $\theta/j$. First moments give tightness of every fixed vector. For a fixed multi-index $r$, the square of its falling-factorial monomial is a finite linear combination of such monomials with orders at most $2r$; formula (9) uniformly bounds all their expectations. The monomials are therefore uniformly integrable, so their expectations pass to every weak subsequential limit. Product Poisson laws are factorial-moment determinate. Every subsequential limit is consequently the same product law, which proves (5). Notice that (9) is generally not a product at finite $n$; finite block counts have not been declared independent.

# Parameter boundaries and finite evidence

At $\theta=1$, (1) is the cycle-support partition of a uniformly random permutation: a fixed block supports $(|B|-1)!$ cycles. For fixed $n$, $$\mathbb P(\Pi_n=\{[n]\})
 =\frac{\theta(n-1)!}{(\theta)^{\overline{n}}}\longrightarrow1
 \quad(\theta\downarrow0),$$ whereas $\mathbb P(\Pi_n\text{ is all singletons})=\theta^n/(\theta)^{\overline{n}}
\to1$ as $\theta\to\infty$. These are fixed-$n$ boundaries; no interchange with $n\to\infty$ is asserted.

The exact certificate contains 914 occupancy vectors through $n=16$, 528 Stirling rows and 2,640 block-count probabilities through $n=32$, 320 innovation rows, 740 mixed factorial moments, 80 normalization rows, and 16 boundary rows. An independent implementation checks all 5,238 rows; 219 symbolic identities, two isolated byte replays, and 69 hostile mutations give separate receipts. None of these finite checks proves (4) or (5); the probability arguments above do.

# Lineage and Route-A boundary

Ewens is the primary sampling-formula source [@ewens]; Hoppe supplies the Pólya-like urn lineage [@hoppe]. We make no priority claim and do not invoke the stronger ranked-frequency Poisson--Dirichlet theorem.

The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ Customer count is not a rational-prime clock, blocks are not primitive periodic orbits, and the finite factorization (3) is not an arithmetic Euler product. No target divisor, functional equation, counting law, zero matching, or natural target quantization is produced. Route A is rejected and Route B is not invoked. In particular, no target arithmetic local data, Euler factors, root number, automorphy, target-zero match, or Hilbert--Pólya operator is claimed.

9 W. J. Ewens, "The sampling theory of selectively neutral alleles," *Theor. Popul. Biol.* 3 (1972), 87--112. [doi:10.1016/0040-5809(72)90035-4](https://doi.org/10.1016/0040-5809(72)90035-4).

F. M. Hoppe, "Pólya-like urns and the Ewens' sampling formula," *J. Math. Biol.* 20 (1984), 91--94. [doi:10.1007/BF00275863](https://doi.org/10.1007/BF00275863).
