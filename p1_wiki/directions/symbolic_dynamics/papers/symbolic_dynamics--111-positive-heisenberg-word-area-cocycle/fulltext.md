---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--111-positive-heisenberg-word-area-cocycle"
canonical_tex: "symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle/main.tex"
canonical_pdf: "symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle/main.pdf"
source_sha256: "27aecd7aa6e2a8d8920ad5c311d2f6812f13bb85e8673d3f837374cb1297ec09"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Positive Heisenberg Word-Area Cocycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/111-positive-heisenberg-word-area-cocycle/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $X=I+E_{12}$ and $Y=I+E_{23}$, choose $X$ with probability $p$ and $Y$ with probability $1-p$, and form the chronological left product $M_n=A_n\cdots A_1$. Every finite product has a three-coordinate normal form: its central entry is the number $C_n$ of pairs in which a $Y$ occurs before a later $X$. Conditioning on the number of $X$ letters gives the Gaussian-binomial inversion polynomial, while averaging the slices gives an exact biased finite-time law. We record $$\mathbb EC_n=\frac{n(n-1)}2p(1-p)$$ and a closed variance, then prove a strong law and an $n^{3/2}$ central limit theorem with variance $p(1-p)(3p^2-3p+1)/3$. The same normal form yields a sharp growth boundary: every nondegenerate Bernoulli environment has matrix-norm exponent two in $\log n$ scale, whereas both deterministic endpoints have exponent one. Finally, the $n^2$-scale annealed area pressure is zero for nonpositive tilt and equals one quarter of the positive tilt, producing a strict gap from the typical area rate. Gaussian-binomial inversion laws, random-word limit theory, and random walks on Heisenberg groups are treated as established background. The note claims only this owner-subtracted exact conjunction; external circulation remains on hold.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Positive Heisenberg Word-Area Cocycles'
```

## Markdown 正文

# Introduction

Two elementary unipotent shears already retain the order of the random letters that generate their product. For the positive Heisenberg pair $$X=I+E_{12},\qquad Y=I+E_{23},$$ the two first-superdiagonal entries count letters. The central entry is more informative: it counts every $Y$ that precedes a later $X$. Thus a noncommutative matrix coordinate becomes an oriented area of a Bernoulli word.

The ingredients behind this reduction have substantial prior ownership. Gaussian polynomials enumerate inversions in fixed-content words, and their asymptotic normality is developed by Canfield, Janson, and Zeilberger [@CanfieldJansonZeilberger2011; @CanfieldJansonZeilberger2012]. For the fair binary law, the same statistic is the area under a uniformly random north--east lattice path: Takács proved moment and limit results for that area [@Takacs1986], while Janson gave random-word inversion interpretations, exact moments, limit theorems, and a Hoeffding-decomposition route for uniform alphabets, including the binary case [@Janson2012]. General iid random-word subsequence methods are also established [@IslakOzdemir2018]. Random walks on Heisenberg and higher unitriangular groups have a broad coordinate-level limit theory [@DiaconisHough2021]. The inversion law, the general random-word CLT mechanism, the fair binary specialization, and Heisenberg random-walk theory are not claims of this note.

The residual calculation is a finite and auditable conjunction for the specific positive pair above. It consists of four parts.

1.  Every word has an exact matrix normal form, and its complete biased area distribution is a Bernoulli mixture of Gaussian polynomials.

2.  The first two moments are closed for arbitrary $p$, and a direct centered-pair decomposition proves the strong law and an explicit $n^{3/2}$ CLT without importing a group-level limit theorem.

3.  The matrix norm has polynomial exponent two for $0<p<1$ but exponent one at $p=0,1$.

4.  Rare ordered words determine a kinked $n^2$-scale annealed pressure and a strict annealed--typical gap for every nonzero tilt.

Two proof lanes are kept separate. The first uses literal matrix multiplication and a last-letter Gaussian-polynomial recurrence. The second expands the area into centered iid Bernoulli variables. Their intersection at the exact biased moments supplies an internal consistency check rather than a novelty argument. External release is **HOLD**; no absolute novelty or priority statement is made.

# Cocycle convention and finite-word normal form {#sec:normal}

For $a,b,c\in\mathbb R$, write $$\label{eq:H-coordinate}
 H(a,b,c)=
 \begin{pmatrix}1&a&c\\0&1&b\\0&0&1\end{pmatrix}.$$ The multiplication rule is $$\label{eq:H-law}
 H(a,b,c)H(a',b',c')
 =H(a+a',b+b',c+c'+ab').$$ Set $X=H(1,0,0)$ and $Y=H(0,1,0)$. Let $(A_t)_{t\geq1}$ be iid with $$\label{eq:environment-law}
 \mathbb P(A_t=X)=p,\qquad \mathbb P(A_t=Y)=q:=1-p,
 \qquad 0\leq p\leq1,$$ and fix the chronological convention $$\label{eq:left-product}
 M_0=I,\qquad M_n=A_nA_{n-1}\cdots A_1.$$ Thus $A_1$ acts first.

Encode $X$ by $B_t=1$ and $Y$ by $B_t=0$. Define $$\label{eq:counts}
 J_n=\sum_{t=1}^n B_t,\qquad K_n=n-J_n,$$ and the oriented word-area $$\label{eq:area}
 C_n=\sum_{1\leq i<j\leq n}(1-B_i)B_j.$$ Equivalently, $C_n$ is the number of $Y$-before-$X$ pairs. If the word is drawn as a north--east lattice path, it is the sum of the heights of the east steps.

[\[thm:normal-law\]]{#thm:normal-law label="thm:normal-law"} For every finite word and every $n\geq0$, $$\label{eq:normal-form}
 \boxed{\quad M_n=H(J_n,K_n,C_n).\quad}$$ Moreover, for $0\leq j\leq n$, $$\label{eq:gaussian-slice}
 \sum_{c\geq0}
 \#\{w:J_n(w)=j,\ C_n(w)=c\}\,z^c
 =\genfrac{[}{]}{0pt}{}{n}{j}_{z},$$ where the right side is the Gaussian binomial polynomial. Consequently, the formal probability generating polynomial is $$\label{eq:biased-pgf}
 \boxed{\quad
 \mathbb Ez^{C_n}=\sum_{j=0}^n p^j q^{n-j}\genfrac{[}{]}{0pt}{}{n}{j}_{z}.
 \quad}$$ The formula includes $p=0,1$, with the natural convention $0^0=1$.

The claim holds at time zero. Suppose $M_n=H(J_n,K_n,C_n)$. Direct left multiplication gives $$\begin{aligned}
 XM_n&=H(J_n+1,K_n,C_n+K_n),\label{eq:X-update}\\
 YM_n&=H(J_n,K_n+1,C_n).\label{eq:Y-update}\end{aligned}$$ Appending an $X$ adds one pair for each of the $K_n$ earlier $Y$ letters; appending a $Y$ adds no $Y$-before-$X$ pair. These are precisely the updates of [\[eq:counts\]](#eq:counts){reference-type="eqref" reference="eq:counts"}--[\[eq:area\]](#eq:area){reference-type="eqref" reference="eq:area"}, proving [\[eq:normal-form\]](#eq:normal-form){reference-type="eqref" reference="eq:normal-form"}.

Let $G_{n,j}(z)$ denote the left side of [\[eq:gaussian-slice\]](#eq:gaussian-slice){reference-type="eqref" reference="eq:gaussian-slice"}. Splitting words by their last letter gives $$\label{eq:gaussian-recurrence}
 G_{n,j}(z)=G_{n-1,j}(z)+z^{n-j}G_{n-1,j-1}(z),$$ with $G_{0,0}=1$ and zero outside $0\leq j\leq n$. This is the standard Gaussian-binomial recurrence, so [\[eq:gaussian-slice\]](#eq:gaussian-slice){reference-type="eqref" reference="eq:gaussian-slice"} follows. Every word in the $j$th slice has probability $p^jq^{n-j}$; summing the slices proves [\[eq:biased-pgf\]](#eq:biased-pgf){reference-type="eqref" reference="eq:biased-pgf"}.

The Gaussian-polynomial statement in [\[thm:normal-law\]](#thm:normal-law){reference-type="ref" reference="thm:normal-law"} is included to make the cocycle calculation self-contained. Its combinatorial content is owned background [@CanfieldJansonZeilberger2011]; the fair Bernoulli specialization is likewise direct prior territory [@Takacs1986; @Janson2012].

# Exact biased moments and limit laws {#sec:moments}

The conditional law gives one route to the exact moments. A direct iid expansion then proves the asymptotic statements independently of that enumeration.

[\[lem:slice-moments\]]{#lem:slice-moments label="lem:slice-moments"} For $J_n=j$, $$\label{eq:conditional-moments}
 \mathbb E(C_n\mid J_n=j)=\frac{j(n-j)}2,
 \qquad
 \operatorname{Var}(C_n\mid J_n=j)
 =\frac{j(n-j)(n+1)}{12}.$$

Put $k=n-j$ and $z=e^t$. The product form of the Gaussian polynomial gives $$\frac{\genfrac{[}{]}{0pt}{}{n}{j}_{z}\big|_{z=e^t}}{\binom nj}
 =\prod_{r=1}^j
 \frac{(e^{(k+r)t}-1)/((k+r)t)}{(e^{rt}-1)/(rt)}.$$ For fixed $a>0$, $$\log\frac{e^{at}-1}{at}=\frac{a}{2}t+\frac{a^2}{24}t^2+O(t^3).$$ The first two derivatives of the logarithm of the conditional moment generating function are therefore $$\frac12\sum_{r=1}^j[(k+r)-r]=\frac{jk}{2}$$ and $$\frac1{12}\sum_{r=1}^j[(k+r)^2-r^2]
 =\frac{jk(j+k+1)}{12}.$$ These derivatives are the first two cumulants, which proves [\[eq:conditional-moments\]](#eq:conditional-moments){reference-type="eqref" reference="eq:conditional-moments"}.

[\[thm:moments-clt\]]{#thm:moments-clt label="thm:moments-clt"} For every $0\leq p\leq1$ and $n\geq0$, $$\label{eq:mean}
 \mathbb EC_n=\frac{n(n-1)}2pq$$ and $$\label{eq:variance}
 \boxed{\quad
 \operatorname{Var}(C_n)
 =\frac{n(n-1)pq}{6}
 \left(6np^2-6np+2n-9p^2+9p-1\right).
 \quad}$$ For $0<p<1$, $$\label{eq:slln}
 \frac{C_n}{n^2}\longrightarrow\frac{pq}{2}
 \qquad\text{almost surely},$$ and $$\label{eq:clt}
 \frac{C_n-\frac{n(n-1)}2pq}{n^{3/2}}
 \Longrightarrow N(0,\sigma_p^2),
 \qquad
 \sigma_p^2=\frac{pq(3p^2-3p+1)}{3}.$$ At $p=0,1$, $C_n=0$ deterministically.

Conditioning on $J_n\sim\operatorname{Bin}(n,p)$ and using [\[lem:slice-moments\]](#lem:slice-moments){reference-type="ref" reference="lem:slice-moments"} proves [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}. The law of total variance gives $$\operatorname{Var}(C_n)
 =\frac{n+1}{12}\mathbb E[J_n(n-J_n)]
 +\frac14\operatorname{Var}(J_n(n-J_n)).$$ Substitution of the binomial falling moments $\mathbb E[(J_n)_r]=(n)_rp^r$, for $1\leq r\leq4$, reduces the right side to [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}.

There is also a direct derivation that does not use the conditional Gaussian-polynomial law. Put $Z_{ij}=(1-B_i)B_j$ for $i<j$. Then $\operatorname{Var}(Z_{ij})=pq(1-pq)$. For every triple $i<j<k$, the three possible covariances between $Z_{ij},Z_{ik},Z_{jk}$ are $$p^3q,\qquad pq^3,\qquad -p^2q^2,$$ respectively. Pair variables with disjoint index sets are independent. Consequently, $$\label{eq:pair-covariance-variance}
 \operatorname{Var}(C_n)
 =\binom n2pq(1-pq)
  +2\binom n3pq(1-3pq),$$ and elementary simplification gives [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}. Thus the full finite-time variance already has two independent derivations.

For an independent route to the limits, put $\eta_k=B_k-p$. Expanding each summand in [\[eq:area\]](#eq:area){reference-type="eqref" reference="eq:area"} yields the exact centered identity $$\label{eq:centered-decomposition}
 C_n-\frac{n(n-1)}2pq
 =L_n+R_n,$$ where $$\begin{aligned}
 L_n&=\sum_{k=1}^n[k-1-p(n-1)]\eta_k,
 \label{eq:linear-part}\\
 R_n&=-\sum_{1\leq i<j\leq n}\eta_i\eta_j
 =-\frac12\left[
 \left(\sum_{k=1}^n\eta_k\right)^2-\sum_{k=1}^n\eta_k^2
 \right].\label{eq:quadratic-part}\end{aligned}$$

The ordinary strong law gives $S_n:=\sum_{k=1}^n\eta_k=o(n)$ almost surely. Summation by parts gives $$\sum_{k=1}^n(k-1)\eta_k
 =(n-1)S_n-\sum_{m=1}^{n-1}S_m=o(n^2).$$ Equations [\[eq:linear-part\]](#eq:linear-part){reference-type="eqref" reference="eq:linear-part"}--[\[eq:quadratic-part\]](#eq:quadratic-part){reference-type="eqref" reference="eq:quadratic-part"} then imply $L_n=o(n^2)$ and $R_n=o(n^2)$ almost surely. Combining this with [\[eq:centered-decomposition\]](#eq:centered-decomposition){reference-type="eqref" reference="eq:centered-decomposition"} proves [\[eq:slln\]](#eq:slln){reference-type="eqref" reference="eq:slln"}.

For the CLT, independence gives $$\begin{aligned}
 \operatorname{Var}(L_n)
 &=pq\sum_{k=1}^n[k-1-p(n-1)]^2\notag\\
 &=\frac{pq\,n(n-1)}6
 \left(2n-1-6p(n-1)+6p^2(n-1)\right).
 \label{eq:linear-variance}\end{aligned}$$ After division by $n^3$, this converges to $\sigma_p^2>0$. Every summand in [\[eq:linear-part\]](#eq:linear-part){reference-type="eqref" reference="eq:linear-part"} has magnitude at most $n$, whereas $\sqrt{\operatorname{Var}(L_n)}$ has order $n^{3/2}$. The Lindeberg condition is therefore eventually vacuous, and the triangular-array Lindeberg--Feller theorem gives $L_n/n^{3/2}\Longrightarrow N(0,\sigma_p^2)$. Finally, $$\mathbb E|R_n|
 \leq\frac12\left(
 \mathbb ES_n^2+\sum_{k=1}^n\mathbb E\eta_k^2\right)=npq.$$ Hence $R_n/n^{3/2}\to0$ in probability. Slutsky's theorem proves [\[eq:clt\]](#eq:clt){reference-type="eqref" reference="eq:clt"}. The endpoint statement follows directly from [\[eq:area\]](#eq:area){reference-type="eqref" reference="eq:area"}.

At $p=1/2$, [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"} becomes $n(n-1)(2n+5)/96$, while $\sigma_{1/2}^2=1/48$.

# Polynomial matrix growth {#sec:growth}

All norms on the nine-dimensional space of $3\times3$ real matrices are equivalent. The positive normal form therefore turns area growth into matrix-norm growth without cancellation.

[\[thm:norm-boundary\]]{#thm:norm-boundary label="thm:norm-boundary"} For every fixed matrix norm, $$\label{eq:norm-exponent}
 \lim_{n\to\infty}\frac{\log\lVert M_n\rVert}{\log n}
 =\begin{cases}
 2,&0<p<1,\\
 1,&p=0\text{ or }p=1,
 \end{cases}
 \qquad\text{almost surely}.$$

It suffices to use the Frobenius norm, for which $$\label{eq:Frobenius}
 \lVert M_n\rVert_{\mathrm F}^2=3+J_n^2+K_n^2+C_n^2.$$ If $0<p<1$, [\[eq:slln\]](#eq:slln){reference-type="eqref" reference="eq:slln"} gives $C_n/n^2\to pq/2>0$ almost surely. Equation [\[eq:Frobenius\]](#eq:Frobenius){reference-type="eqref" reference="eq:Frobenius"} then implies $\lVert M_n\rVert_{\mathrm F}=n^{2+o(1)}$. At $p=1$, $M_n=I+nE_{12}$; at $p=0$, $M_n=I+nE_{23}$. In either endpoint, $\lVert M_n\rVert_{\mathrm F}^2=n^2+3$. Norm equivalence changes logarithms by a bounded amount and therefore preserves [\[eq:norm-exponent\]](#eq:norm-exponent){reference-type="eqref" reference="eq:norm-exponent"}.

This boundary is polynomial rather than Lyapunov: all eigenvalues of every $M_n$ equal one, and $n^{-1}\log\lVert M_n\rVert\to0$ in every regime.

# Quadratic area pressure {#sec:pressure}

For $\theta\in\mathbb R$, define the annealed area pressure and its pathwise counterpart by $$\begin{aligned}
 \mathcal P_p(\theta)
 &=\lim_{n\to\infty}\frac1{n^2}
   \log\mathbb Ee^{\theta C_n},\label{eq:annealed-pressure}\\
 \mathcal Q_p(\theta)
 &=\lim_{n\to\infty}\frac{\theta C_n}{n^2},
 \label{eq:typical-pressure}\end{aligned}$$ whenever the limits exist. The $n^2$ normalization matches the central coordinate, rather than the usual exponential norm scale.

[\[prop:extrema\]]{#prop:extrema label="prop:extrema"} For every $n\geq0$, $$\label{eq:max-area}
 \max_w C_n(w)=\left\lfloor\frac{n^2}{4}\right\rfloor.$$ For $0<p<1$, $$\label{eq:max-probability}
 \mathbb P\left(C_n=\left\lfloor\frac{n^2}{4}\right\rfloor\right)
 =(pq)^{\lfloor n/2\rfloor}.$$ The zero-area probability is $$\label{eq:zero-probability}
 \mathbb P(C_n=0)=\sum_{j=0}^n p^jq^{n-j}
 =\begin{cases}
 \dfrac{p^{n+1}-q^{n+1}}{p-q},&p\neq q,\\[6pt]
 (n+1)2^{-n},&p=q=\frac12.
 \end{cases}$$

With $j$ letters $X$ and $n-j$ letters $Y$, at most $j(n-j)$ ordered pairs contribute. Equality requires the word $Y^{n-j}X^j$. Maximizing $j(n-j)$ over integers gives [\[eq:max-area\]](#eq:max-area){reference-type="eqref" reference="eq:max-area"}. There is one balanced maximizer when $n$ is even and two when $n$ is odd; their probabilities sum to [\[eq:max-probability\]](#eq:max-probability){reference-type="eqref" reference="eq:max-probability"}. Area zero means that no $Y$ precedes an $X$, so the word is uniquely $X^jY^{n-j}$ for some $0\leq j\leq n$. Summing their probabilities gives [\[eq:zero-probability\]](#eq:zero-probability){reference-type="eqref" reference="eq:zero-probability"}.

[\[thm:pressure\]]{#thm:pressure label="thm:pressure"} The limit [\[eq:annealed-pressure\]](#eq:annealed-pressure){reference-type="eqref" reference="eq:annealed-pressure"} exists for every $p\in[0,1]$ and $\theta\in\mathbb R$. It is $$\label{eq:pressure-formula}
 \boxed{\quad
 \mathcal P_p(\theta)=
 \begin{cases}
 \theta/4,&0<p<1\text{ and }\theta>0,\\
 0,&0<p<1\text{ and }\theta\leq0,\\
 0,&p\in\{0,1\}.
 \end{cases}\quad}$$ For $0<p<1$, the pathwise limit is $$\label{eq:typical-formula}
 \mathcal Q_p(\theta)=\frac{\theta pq}{2}
 \qquad\text{almost surely}.$$ Thus $\mathcal P_p(\theta)>\mathcal Q_p(\theta)$ for every $\theta\neq0$ and $0<p<1$.

Suppose first that $0<p<1$ and $\theta>0$. By [\[prop:extrema\]](#prop:extrema){reference-type="ref" reference="prop:extrema"}, $$(pq)^{\lfloor n/2\rfloor}
 e^{\theta\lfloor n^2/4\rfloor}
 \leq \mathbb Ee^{\theta C_n}
 \leq e^{\theta\lfloor n^2/4\rfloor}.$$ Taking logarithms and dividing by $n^2$ proves the first line of [\[eq:pressure-formula\]](#eq:pressure-formula){reference-type="eqref" reference="eq:pressure-formula"}. If $\theta<0$, then $$\mathbb P(C_n=0)\leq\mathbb Ee^{\theta C_n}\leq1.$$ The probability in [\[eq:zero-probability\]](#eq:zero-probability){reference-type="eqref" reference="eq:zero-probability"} is bounded below by $\max\{p,q\}^n$, so both logarithmic bounds have limit zero on the $n^2$ scale. The case $\theta=0$ is immediate. At $p=0,1$, $C_n=0$.

Equation [\[eq:typical-formula\]](#eq:typical-formula){reference-type="eqref" reference="eq:typical-formula"} is [\[eq:slln\]](#eq:slln){reference-type="eqref" reference="eq:slln"} multiplied by $\theta$. For positive $\theta$, $1/4-pq/2\geq1/8$; for negative $\theta$, the annealed value is zero while the typical value is negative. This proves strictness.

# Proof lanes, controls, and owner boundary {#sec:scope}

The two proof lanes use different primitive data.

-   **Finite-word lane.** Raw matrix multiplication gives [\[eq:normal-form\]](#eq:normal-form){reference-type="eqref" reference="eq:normal-form"}; a last-letter recurrence gives the complete conditional area polynomial. Differentiating its product form gives the conditional moments, and binomial mixing gives the biased moments.

-   **Centered-pair lane.** The iid identity [\[eq:centered-decomposition\]](#eq:centered-decomposition){reference-type="eqref" reference="eq:centered-decomposition"} does not use Gaussian polynomials. Shared-index covariance counting first recovers the complete variance [\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}; the centered identity then proves the strong law and CLT. This lane meets the first at an exact finite-time formula, not only at its leading coefficient.

The norm theorem uses positivity and finite-dimensional norm equivalence. The pressure theorem instead uses exact extremizers and their probabilities; neither conclusion is extrapolated from computation.

The standard-library verifier mirrors these lanes. It multiplies all $131{,}071$ binary words through length $16$, independently scans their letter and area statistics, and compares every conditional histogram with the Gaussian recurrence. Separate exact-rational lanes check biased moments and the independent pair-covariance formula through time $32$, the centered decomposition word by word through time $12$, endpoint norms, extremal probabilities, and exponential-moment bounds. The stored output records the exact assertion count. These controls are finite falsification tests, not proofs of the asymptotic statements.

The owner boundary is part of the result's scope. Gaussian-binomial enumeration and fixed-content inversion asymptotics are subtracted against [@CanfieldJansonZeilberger2011; @CanfieldJansonZeilberger2012]; fair-word inversion moments and limit laws are subtracted directly against [@Takacs1986; @Janson2012]; and general iid random-word subsequence methods are subtracted against [@IslakOzdemir2018]. General Heisenberg and unitriangular random-walk limit theory is subtracted against [@DiaconisHough2021]. The internally studied residual package is only the arbitrary-bias conjunction for this particular matrix cocycle, the polynomial exponent boundary, and the quadratic pressure kink for the two displayed positive generators. This is a scope description, not a novelty claim. Search absence is not evidence, and external circulation remains **HOLD** pending specialist direct-owner review.

Internally, P70 studies weighted shifts on finite Heisenberg quotients via convolution nullities; P93 is a symbolic push--pop stack cocycle controlled by a reflected random walk; P99 studies one deterministic shear acting on finite-index sublattices; and P104 studies exponentially contracting monomial random matrices through occupation and singular-value pressure. The phase spaces and observables here are different, but the shared cocycle, Heisenberg, and random-matrix vocabulary remains disclosed.

# Conclusion

The positive Heisenberg product stores Bernoulli word order in one central entry. Combining its exact finite-word law with an independent centered pair expansion yields the complete biased moments, a strong law, and an explicit CLT. Positivity then exposes a polynomial norm boundary, while rare ordered words force a kinked quadratic pressure and a strict annealed--typical gap. These conclusions define the paper's full scope; all broader inversion, random-word, and Heisenberg-walk theory remains owned background. External release is on hold.
