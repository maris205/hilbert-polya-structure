---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--172-fresh-map-self-image-erosion"
canonical_tex: "symbolic_dynamics/papers/172-fresh-map-self-image-erosion/main.tex"
canonical_pdf: "symbolic_dynamics/papers/172-fresh-map-self-image-erosion/main.pdf"
source_sha256: "c1d72b29b57f967f84ed49daccb4ff7053d1d4d96a7d89172a91ee0bfee75f58"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fresh-Map Self-Image Erosion: Labelled Kernels and a Forced Jordan Block

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/172-fresh-map-self-image-erosion>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/172-fresh-map-self-image-erosion/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/172-fresh-map-self-image-erosion/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/172-fresh-map-self-image-erosion/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/172-fresh-map-self-image-erosion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix an integer $n\ge1$ and repeatedly intersect a labelled subset $A\subseteq[n]$ with its image under a freshly resampled uniform endomap of $[n]$. We determine the transition to every labelled target while retaining the total image size of the sampled map on $A$. An $(n+1)$-state cardinality quotient then gives every-time labelled transition and absorption formulas. The full operator has eigenvalues $a!/n^a$ with binomial layer multiplicities $\binom na$; the equality of its top two size-layer eigenvalues is not semisimple, and the quotient contains a forced $2$-by-$2$ Jordan block for every $n\ge2$. Finally, products of a polynomial quotient give the joint image-size marks at arbitrary epochs. Specified-bin occupancy, Stirling surjection counts, marked-kernel products, and generic triangular-chain algebra are treated as background. The literal conjunction remains owner-thin and its external status is [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Fresh-Map Self-Image Erosion:\
  Labelled Kernels and a Forced Jordan Block
```

## Markdown 正文

# The literal chain and theorem package

Fix an integer $n\ge1$ and write $[n]=\{1,\ldots,n\}$. At epoch $r$, sample an independent uniform map $f_r:[n]\to[n]$ and update $$\label{eq:update}
                   A_r=A_{r-1}\cap f_r(A_{r-1}).$$ Only the restriction of $f_r$ to the current set affects this update. The process therefore differs from the ordinary random-image chain, whose image sizes and compositions already have a direct literature [@ZubkovSerov2017]; random mappings and their classical statistics are also mature [@FlajoletOdlyzko1990]. More directly, specified-cell occupancy is classical [@Charalambides1984], and the extended-occupancy distribution has a noncentral-Stirling and spectral formulation [@ONeill2023]. Successive-elimination and leader-election games provide another nearby vocabulary [@HoffmanJenkinsRoughgarden2002]. In one simultaneous round of that directed-graph game, selected endpoints are eliminated, so the survivors are zero-indegree vertices. In [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, by contrast, the selected endpoints inside the active set are retained, so they have positive indegree; moreover each fresh map is sampled into the fixed ambient set $[n]$, rather than along the induced current graph. We assign all of those objects, Stirling surjection counts, and generic finite-chain linear algebra no contribution credit. They are included below only to make the literal conjunction self-contained.

Let $\genfrac\{\}{0pt}{}{a}{k}$ be a Stirling number of the second kind. For $0\le b\le a\le n$, set $$\begin{aligned}
H_n(a,b;k)&=\binom{n-a}{k-b}k!\genfrac\{\}{0pt}{}{a}{k},                 \label{eq:H}\\
N_{ab}&=\sum_{k=0}^{a}H_n(a,b;k),                      \label{eq:N}\\
Q_{ab}&=\binom ab\frac{N_{ab}}{n^a},                  \label{eq:Q}\end{aligned}$$ where a binomial coefficient outside its natural range is zero, $\genfrac\{\}{0pt}{}{0}{0}=1$, and $\genfrac\{\}{0pt}{}{a}{0}=0$ for $a>0$. At $a=0$ the denominator is one. For later owner subtraction, inclusion--exclusion also gives $$\label{eq:required-box}
 N_{ab}=\sum_{j=0}^{b}(-1)^j\binom bj(n-a+b-j)^a.$$ For $a\ge1$, the notation of @ONeill2023 identifies the whole unmarked size row as $$\label{eq:occupancy-owner}
 Q_{ab}=\operatorname{Occ}(b\mid a,a,a/n)
       =n^{-a}(a)_b S_{\rm nc}(a,b;n-a),$$ with $(a)_b=a!/(a-b)!$ and $S_{\rm nc}$ the source's noncentral Stirling number. The $a=0$ row is separately the unit mass $Q_{00}=1$, since the extended-occupancy source assumes a positive number of bins and positive $\theta$. Thus [\[eq:required-box\]](#eq:required-box){reference-type="eqref" reference="eq:required-box"}--[\[eq:occupancy-owner\]](#eq:occupancy-owner){reference-type="eqref" reference="eq:occupancy-owner"}, including their occupancy algebra, earn no contribution credit here. Let $P$ denote the full transition matrix indexed by the $2^n$ labelled subsets.

[\[thm:main\]]{#thm:main label="thm:main"} For the chain [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, the following statements hold.

(i) If $B\subseteq A$, $|A|=a$, $|B|=b$, and $k\ge0$, then $$\label{eq:marked-one}
     \#\{f|_A:A\cap f(A)=B,\ |f(A)|=k\}=H_n(a,b;k).$$ Consequently $P(A,B)=N_{ab}/n^a$; a target outside $A$ has probability zero.

(ii) For every $t\ge0$ and $B\subseteq A$, $$\label{eq:alltime}
             P^t(A,B)=\frac{(Q^t)_{ab}}{\binom ab}.$$ This formula is zero when $B\nsubseteq A$.

(iii) The complete algebraic eigenvalue multiset of $P$ is $$\label{eq:spectrum}
       \left\{\frac{a!}{n^a}\text{ with multiplicity }\binom na:
                        0\le a\le n\right\}.$$ For $n\ge2$, the common value $$\label{eq:collision}
       \lambda=\frac{(n-1)!}{n^{n-1}}=\frac{n!}{n^n}$$ has one $J_2(\lambda)$ block in the cardinality quotient. Hence the full operator is not diagonalizable. No complete Jordan form for $P$ is claimed.

(iv) For $n\ge2$, the empty set is the unique recurrent state. If $\tau=\min\{t:A_t=\varnothing\}$ and $|A_0|=a$, then $$\begin{aligned}
      \mathbb P_a(\tau\le t)&=(Q^t)_{a0},                         \label{eq:cdf}\\
      m_0&=0,\qquad
      m_a=\frac{1+\sum_{b<a}Q_{ab}m_b}{1-Q_{aa}}=\mathbb E_a\tau.
                                                                    \label{eq:mean}\end{aligned}$$ At $n=1$, both subsets are fixed. At $n=2$, $$\label{eq:n2}
      Q=\begin{pmatrix}1&0&0\\[1mm]1/2&1/2&0\\[1mm]0&1/2&1/2\end{pmatrix},
      \qquad m_2=4.$$

(v) Define the polynomial quotient $$\label{eq:polyQ}
     Q_{ab}(z)=\binom ab n^{-a}\sum_{k=0}^{a}H_n(a,b;k)z^k.$$ For $W_r=|f_r(A_{r-1})|$ and every fixed labelled target $B$, put $$\label{eq:fixed-mark}
     M_t^{A,B}(z_1,\ldots,z_t)=
     \mathbb E_A\!\left[\mathbf 1_{\{A_t=B\}}\prod_{r=1}^{t}z_r^{W_r}\right].$$ Then, for every $t\ge1$ and $|A|=a$, $$\begin{aligned}
     \sum_{\substack{B\subseteq A\\ |B|=b}}M_t^{A,B}(z_1,\ldots,z_t)
       &=[Q(z_1)\cdots Q(z_t)]_{ab},                         \label{eq:mark-aggregate}\\
     M_t^{A,B}(z_1,\ldots,z_t)
       &=\mathbf 1_{\{B\subseteq A\}}
         \frac{[Q(z_1)\cdots Q(z_t)]_{ab}}{\binom ab}.
                                                                   \label{eq:mark-fixed}\end{aligned}$$

The last statement retains information lost by the subset endpoint. It does not assert that the epoch marks are independent.

# Endpoint counts and labelled powers

Fix $B\subseteq A$ and require $|f(A)|=k$. The part of the image outside $A$ is a $(k-b)$-subset $R$ of $[n]\setminus A$, giving $\binom{n-a}{k-b}$ choices. Once $R$ is fixed, the restriction $f|_A$ must map onto the $k$-set $B\cup R$. There are $k!\genfrac\{\}{0pt}{}{a}{k}$ such surjections. This proves [\[eq:marked-one\]](#eq:marked-one){reference-type="eqref" reference="eq:marked-one"}. Summing over $k$ and dividing by the $n^a$ restrictions gives the stated probability. The values of $f$ outside $A$ would contribute the common factor $n^{n-a}$ if full maps were counted.

Summing [\[eq:marked-one\]](#eq:marked-one){reference-type="eqref" reference="eq:marked-one"} over the $\binom ab$ possible targets proves $\sum_bQ_{ab}=1$. Thus $Q$ is the transition matrix of the cardinality process.

Every trajectory is nested. Simultaneous relabelling of $[n]$ commutes with the distribution of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, so conditional on the initial $a$-set and final cardinality $b$, all $\binom ab$ labelled endpoints have equal probability. The total probability of that layer is $(Q^t)_{ab}$, which proves [\[eq:alltime\]](#eq:alltime){reference-type="eqref" reference="eq:alltime"}, including $t=0$.

This argument is stronger than a size marginal: after the small quotient has been powered, it recovers every labelled endpoint exactly.

# The forced Jordan block and absorption

Order labelled subsets by nondecreasing cardinality. Since transitions only go to subsets, $P$ is lower triangular. A self-loop at an $a$-set requires $f|_A$ to be a permutation of $A$, and therefore $$\label{eq:diagonal}
                         P(A,A)=\lambda_a=\frac{a!}{n^a}.$$ This proves the algebraic multiset [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"}.

The ratios $\lambda_{a+1}/\lambda_a=(a+1)/n$ are strictly below one for $a<n-1$, while [\[eq:collision\]](#eq:collision){reference-type="eqref" reference="eq:collision"} gives the only repeated adjacent quotient diagonal. Also $$Q_{n,n-1}=\binom n{n-1}\frac{(n-1)!\genfrac\{\}{0pt}{}{n}{n-1}}{n^n}>0.$$ Solve $(Q-\lambda I)x=0$ from row zero upward. The distinct first $n-1$ diagonal entries force $x_0=\cdots=x_{n-2}=0$. Row $n-1$ is then free, but row $n$ and the displayed positive coefficient force $x_{n-1}=0$; only $x_n$ remains free. Thus the repeated eigenvalue has algebraic multiplicity two and geometric multiplicity one, giving exactly one $J_2$ in $Q$.

Functions of subset cardinality form a $P$-invariant subspace on which the operator is represented by $Q$. The nonsimple restriction proves that $P$ itself is not diagonalizable.

For $n\ge2$, every nonempty proper set has a positive chance of strict loss: one may map all its points to a point outside it, reaching zero in one step. From the full set, a constant map reaches a singleton; that singleton has a positive next-step chance to map outside itself and reach zero. Moreover $a!/n^a<1$ for every nonempty layer when $n\ge2$. Hence no nonzero closed class exists, absorption at zero is almost sure, and zero is the only recurrent state. Formula [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} is the all-time kernel with final size zero. First-step conditioning gives [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}. Direct substitution gives [\[eq:n2\]](#eq:n2){reference-type="eqref" reference="eq:n2"}. When $n=1$, the sole endomap fixes both subsets, which is why that boundary is separate.

# Image-size marks and the claim boundary

Equation [\[eq:marked-one\]](#eq:marked-one){reference-type="eqref" reference="eq:marked-one"}, summed over the $\binom ab$ targets of size $b$, is exactly [\[eq:polyQ\]](#eq:polyQ){reference-type="eqref" reference="eq:polyQ"}. Conditioning successively on the intermediate sizes and multiplying the mark monomials gives [\[eq:mark-aggregate\]](#eq:mark-aggregate){reference-type="eqref" reference="eq:mark-aggregate"}; this generic marked-kernel step is standard Feynman--Kac/Markov-additive machinery [@FitzsimmonsPitman1999] and earns no contribution credit.

For the fixed-target identity, take two $b$-subsets of $A$ and a permutation of $[n]$ stabilizing $A$ setwise and carrying one target to the other. Conjugating every fresh map in a complete history is a probability-preserving bijection and preserves every $W_r$. Consequently, for each monomial $\prod_r z_r^{k_r}$, its coefficients in the two fixed-target subprobability polynomials coincide. Summing those equal polynomials over the $\binom ab$ targets proves [\[eq:mark-fixed\]](#eq:mark-fixed){reference-type="eqref" reference="eq:mark-fixed"} coefficientwise.

The owner boundary is deliberately narrow. Random-map statistics and ordinary image-size composition are subtracted through [@FlajoletOdlyzko1990; @ZubkovSerov2017]; successive-elimination and leader-election vocabulary is subtracted through [@HoffmanJenkinsRoughgarden2002]; specified-cell and extended occupancy, the fixed-target required-box count, ordinary Stirling/surjection algebra, and marked-kernel multiplication are subtracted through [@Charalambides1984; @ONeill2023; @FitzsimmonsPitman1999]; and triangular spectra, Jordan recursion, and hitting-time recursions are generic. The latter game's zero-indegree survivors are the complementary selection convention to our positive-indegree retained set, and its next round uses the induced graph rather than a fresh map into a fixed ambient label set.

Internally, P158's graph-cut masks, P162's group translations, and P170's permutation fixed sets already occupy nested intersection, labelled recovery, absorption, and marked-history language. The sibling P173 shares fresh ambient maps, nested erosion, a small quotient, every-target symmetry lift, triangular spectra, Jordan recursion, and absorption. All of that proof shell earns zero separation credit. P173's inverse axis is instead a quotient-kernel injectivity count with a complementary-dimension Jordan ladder. The residue under evaluation here is only the specified-bin endpoint count refined by total image size, its coefficientwise labelled lift, and the single terminal $J_2$ forced by [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}.

The standalone verifier enumerates every restriction for all subsets through $n=6$, checks full labelled powers through four epochs, and performs exact rational Jordan tests through $n=9$. These finite checks target arithmetic, boundary, and labelling errors; they do not prove the displayed formulas. The source search was bounded, and its failure to locate the literal conjunction is not evidence of novelty, priority, or freedom to operate. Accordingly the manuscript remains an anonymous internal note with status [hold\_external]{.smallcaps}.
