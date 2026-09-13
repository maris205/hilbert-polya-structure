---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--45-isospectral-arithmetic-fiber-retractions"
canonical_tex: "symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/main.tex"
canonical_pdf: "symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/main.pdf"
source_sha256: "ef7ece5b087b0f425ef38d83417f08c0322401f18cae743c6552f12cd66d8b9e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Isospectral Arithmetic Fiber Retractions Across the $1/h<\Re s\le 1$ Similarity Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/45-isospectral-arithmetic-fiber-retractions/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every integer $h\ge2$, we compare two idempotent arithmetic retractions onto the $h$-free integers: one caps each prime exponent at $h-1$, while the other reduces it modulo $h$. Weighting the induced basis maps on $\ell^2(\mathbb N)$ by $n^{-s/2}$ produces compact operators $S_{h,s}$ and $M_{h,s}$ on their respective domains $\Re s>0$ and $\Re s>1/h$. Their simple nonzero eigenvalues coincide, and so do all common legal power traces and integer-order regularized determinants. Nevertheless, $S_{h,s}$ is boundedly similar to a compact normal operator exactly when $\Re s>1$, whereas $M_{h,s}$ is so similar throughout its bounded domain. Thus the full band $1/h<\Re s\le1$ is isospectral but not similar.

  The discrepancy is quantified in three ways. Saturated Riesz projections have an exact primorial optimizer and subcritical, critical, and supercritical maximal-order regimes. Both singular-value sequences satisfy Weyl laws with explicit Euler-product constants, meeting at the exact crossover $C_{h,1}=D_{h,1}=1$. Finally, the self-commutators have the sharp wall $\Re(s)q=1$, distinct from the operator Schatten wall $\Re(s)q=2$; the case $h=2$ requires a separate endpoint witness and admits an exact Hilbert--Schmidt Euler identity. Independent finite and analytic recomputations are reported only as implementation checks: all infinite claims are established by proof.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Isospectral Arithmetic Fiber Retractions\
  Across the $1/h<\Re s\le 1$ Similarity Gap
```

## Markdown 正文

# Introduction {#sec:introduction}

Compact operators can share every nonzero eigenvalue and still have incompatible geometry. The simplest obstruction is already visible in a rank-one block: the eigenvalue records the action on its eigenline, whereas the angle between the range and kernel controls the norm of its Riesz projection. The point of this paper is that two elementary arithmetic retractions organize that obstruction into an exact family of phase transitions.

Fix $h\ge2$. Let $\mathcal F_h$ be the positive integers whose prime exponents are strictly smaller than $h$, and define $$\tau_h(n)=\prod_p p^{\min\{v_p(n),h-1\}},
  \qquad
  \omega_h(n)=\prod_p p^{v_p(n)\bmod h}.
  \label{eq:intro-maps}$$ Both maps retract $\mathbb N$ onto $\mathcal F_h$. On the finitely supported sequences set $$S_{h,s}e_n=n^{-s/2}e_{\tau_h(n)},
  \qquad
  M_{h,s}e_n=n^{-s/2}e_{\omega_h(n)},
  \qquad \sigma=\Re s.
  \label{eq:intro-operators}$$ Here and below $n^{-s/2}=\exp(-(s/2)\log n)$ with the real logarithm. The formulas in [\[eq:intro-operators\]](#eq:intro-operators){reference-type="ref" reference="eq:intro-operators"} are algebraic until boundedness is proved. The symbols $S_{h,s}$ and $M_{h,s}$ denote operators on $\ell^2(\mathbb N)$ only on their respective bounded domains; every spectral, ideal, trace, determinant, similarity, and commutator assertion is confined to those domains. For $0<q<\infty$, $\mathcal S_q$ denotes the Schatten class, understood as the usual quasi-Schatten ideal when $q<1$.

The common fixed points in $\mathcal F_h$ force common eigenlines. The fibers above those points are very different: saturation can increase only primes already at exponent $h-1$, whereas reduction modulo $h$ permits an arbitrary $h$th-power multiplier. That distinction changes fiber mass and block angle without changing the eigenvalue on the fixed point.

[\[thm:main\]]{#thm:main label="thm:main"} Let $h\ge2$, $s\in\mathbb C$, and $\sigma=\Re s$.

1.  $S_{h,s}$ extends boundedly exactly for $\sigma>0$, and $M_{h,s}$ extends boundedly exactly for $\sigma>1/h$. Each extension is compact throughout its bounded domain.

2.  For $k\ge1$ and $0<q<\infty$, $$\begin{aligned}
        S_{h,s}^{k}\in\mathcal S_q
          &\iff k\sigma q>2,\\
        M_{h,s}^{k}\in\mathcal S_q
          &\iff \sigma>1/h\ \text{and}\ k\sigma q>2.
      \end{aligned}$$

3.  On each bounded domain the simple nonzero eigenvalues are $\lambda_m=m^{-s/2}$, $m\in\mathcal F_h$. On the common domain $\sigma>1/h$, if $k\sigma>2$, then $$\operatorname{Tr}(S_{h,s}^{k})=\operatorname{Tr}(M_{h,s}^{k})
          =\frac{\zeta(ks/2)}{\zeta(hks/2)}.
        \label{eq:intro-trace}$$ If $r\ge1$ is an integer, $\sigma>1/h$, and $r\sigma>2$, then $$\det_r(I-zS_{h,s})=\det_r(I-zM_{h,s})
        \label{eq:intro-det}$$ as entire functions of $z$. For $r=1$, this is the ordinary Fredholm determinant and requires $\sigma>2$.

4.  The exact normal-similarity domains are $$\begin{aligned}
        S_{h,s}\sim_{\mathrm{bd}}\text{ a compact normal operator}
          &\iff \sigma>1,\\
        M_{h,s}\sim_{\mathrm{bd}}\text{ a compact normal operator}
          &\iff \sigma>1/h.
      \end{aligned}$$ Consequently $1/h<\sigma\le1$ is an isospectral band in which $M_{h,s}$ is similar to normal and $S_{h,s}$ is not, while the two operators have equal order-$r$ regularized determinants for every integer $r$ that is legal for both. The order $r=1$ is never legal inside this band, since the Fredholm determinant requires $\sigma>2$.

5.  Let $P_k=p_1\cdots p_k$, with $P_0=1$, and take the largest $k=k(x)$ for which $P_k^{h-1}\le x$. The largest saturated Riesz norm among $m\in\mathcal F_h$, $m\le x$, is attained at $P_k^{h-1}$. As $x\to\infty$ this maximum tends to $\sqrt{\zeta(\sigma)}$ if $\sigma>1$; it is asymptotic to $\sqrt{\mathrm e^\gamma\log\log x}$ if $\sigma=1$; and if $0<\sigma<1$, its logarithm is asymptotic to $$\frac{(h-1)^{\sigma-1}(\log x)^{1-\sigma}}
             {2(1-\sigma)\log\log x}.
        \label{eq:intro-primorial}$$

6.  The singular values, counted with multiplicity in decreasing order, satisfy $$\begin{aligned}
        s_n(S_{h,s})&\sim(\frac{C_{h,\sigma}}{n})^{\sigma/2}
          &&(\sigma>0),\\
        s_n(M_{h,s})&\sim(\frac{D_{h,\sigma}}{n})^{\sigma/2}
          &&(\sigma>1/h),\\
        |\lambda_n|&\sim
          (\frac{1/\zeta(h)}{n})^{\sigma/2},
      \end{aligned}$$ where $$\begin{aligned}
        C_{h,\sigma}
          &=\prod_p(1-p^{-1})\left[
            \sum_{e=0}^{h-2}p^{-e}
            +p^{-(h-1)}(1-p^{-\sigma})^{-1/\sigma}
            \right],
            \label{eq:intro-C}\\
        D_{h,\sigma}&=\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)}.
            \label{eq:intro-D}
      \end{aligned}$$ The constants meet at $C_{h,\sigma}=D_{h,\sigma}=1$ when $\sigma=1$. No ordering between them is asserted away from that point.

7.  For $0<q<\infty$, $$\begin{aligned}
    \in\mathcal S_q
          &\iff \sigma q>1,\\
        [M_{h,s}^*,M_{h,s}]\in\mathcal S_q
          &\iff \sigma>1/h\ \text{and}\ \sigma q>1.
      \end{aligned}$$

The theorem separates three ledgers. The cyclic ledger---eigenvalues, legal traces, and legal determinants---is common. The metric ledger---block singular values and their Weyl constants---is not. The angular ledger---Riesz projection norms and self-commutators---produces a further pair of sharp walls. In particular, equality of the regularized determinants in [\[eq:intro-det\]](#eq:intro-det){reference-type="ref" reference="eq:intro-det"} is a negative control: it demonstrates how much geometry a complete nonzero-eigenvalue product can fail to see.

#### Relation to prior work.

Weighted composition operators on weighted sequence spaces have general boundedness, compactness, closed-range, and essential-norm theories [@LuanKhoi2015; @AbaninMannanikov2023]. Carlson's discrete setting gives spectral and commutant context for weighted composition operators on $L^2$ spaces [@Carlson1990]. Our basis maps are naturally viewed on the adjoint side of that general framework; this convention and the generic fiber-norm mechanism are not contributions. Power-free parts also have a classical arithmetic life independent of the operators considered here [@deWegerWoestijne1999]. The residual result is the paired all-$h$ classification and its exact arithmetic distortion laws, not a generic weighted-composition theorem and not a claim that the formulas detect the additive semantics of rational primes.

We use standard trace-ideal and regularized-determinant theory from [@Simon2005], classical prime asymptotics from [@MontgomeryVaughan2006], and Wiener--Ikehara in the form discussed in [@Korevaar2004]. The hypotheses needed here are checked explicitly.

#### Proof organization.

derives both fibers and their rank-one blocks. proves existence, compactness, ideal membership, and the common cyclic ledger. identifies the precise similarity gap; [\[sec:primorial,sec:weyl,sec:commutators\]](#sec:primorial,sec:weyl,sec:commutators){reference-type="ref" reference="sec:primorial,sec:weyl,sec:commutators"} quantify its maximal, asymptotic, and commutator manifestations. Independent recomputation is summarized only after the proofs in [8](#sec:evaluation){reference-type="ref" reference="sec:evaluation"}. It checks the implementation but is not used to prove an endpoint or asymptotic statement.

# Arithmetic fibers and rank-one blocks {#sec:fibers}

Write $$\mathcal F_h=\{m\in\mathbb N:v_p(m)<h\ \text{for every prime }p\},
  \qquad
  J_h(m)=\{p:v_p(m)=h-1\}.$$ The set $J_h(m)$ records the prime exponents at which saturation has lost information. It need not equal the set of all prime divisors of $m$.

[\[lem:fibers\]]{#lem:fibers label="lem:fibers"} For every $m\in\mathcal F_h$, $$\begin{aligned}
  \tau_h^{-1}(m)
    &=\left\{m\prod_{p\in J_h(m)}p^{r_p}:r_p\in\mathbb N\cup\{0\}\right\},
      \label{eq:saturated-fiber}\\
  \omega_h^{-1}(m)
    &=\{ma^h:a\in\mathbb N\}.
      \label{eq:modulo-fiber}\end{aligned}$$ Both maps fix $m$.

If $v_p(m)\le h-2$, the equality $\min\{v_p(n),h-1\}=v_p(m)$ forces $v_p(n)=v_p(m)$. If $v_p(m)=h-1$, it forces only $v_p(n)\ge h-1$, leaving a nonnegative extra exponent at that same prime. No new prime can occur, which proves [\[eq:saturated-fiber\]](#eq:saturated-fiber){reference-type="ref" reference="eq:saturated-fiber"}. On the other hand, $v_p(n)\equiv v_p(m)\pmod h$, with $0\le v_p(m)<h$, is equivalent to $v_p(n)=v_p(m)+h v_p(a)$ for a unique positive integer $a$. This proves [\[eq:modulo-fiber\]](#eq:modulo-fiber){reference-type="ref" reference="eq:modulo-fiber"}. Taking every extra exponent to be zero shows that both maps fix $m$.

For $f=\tau_h$ or $\omega_h$, let $$\mathcal H_m^f=\overline{\operatorname{span}}\{e_n:f(n)=m\}.$$ The fibers partition $\mathbb N$, so $$\ell^2(\mathbb N)=\bigoplus_{m\in\mathcal F_h}\mathcal H_m^f.
  \label{eq:block-decomp}$$

[\[lem:block-ledger\]]{#lem:block-ledger label="lem:block-ledger"} Let $T$ denote either algebraic map in [\[eq:intro-operators\]](#eq:intro-operators){reference-type="ref" reference="eq:intro-operators"}, and write $T_m=T|_{\mathcal H_m^f}$. Whenever the coefficient sequence of this block is square summable, $T_m$ is rank one, its range is $\mathbb Ce_m$, and its unique nonzero singular value $\rho_T(m)$ satisfies $$\begin{aligned}
  \rho_S(m)^2
    &=m^{-\sigma}\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1},
      &&\sigma>0,                                      \label{eq:rho-S}\\
  \rho_M(m)^2
    &=m^{-\sigma}\zeta(h\sigma),
      &&\sigma>1/h.                                    \label{eq:rho-M}\end{aligned}$$ Moreover, with $\lambda_m=m^{-s/2}$, $$T_m e_m=\lambda_m e_m,
  \qquad
  T_m^k=\lambda_m^{k-1}T_m\quad(k\ge1).
  \label{eq:block-power}$$

For a finitely supported $x=\sum_n x_ne_n$ in the block, $$T_mx=\left(\sum_{f(n)=m}x_n n^{-s/2}\right)e_m.$$ Thus the squared norm of the coefficient functional is $\sum_{f(n)=m}n^{-\sigma}$, and this is the only nonzero squared singular value. Applying [\[lem:fibers\]](#lem:fibers){reference-type="ref" reference="lem:fibers"}, $$\begin{aligned}
  \sum_{\tau_h(n)=m}n^{-\sigma}
    &=m^{-\sigma}\prod_{p\in J_h(m)}\sum_{r\ge0}p^{-r\sigma},\\
  \sum_{\omega_h(n)=m}n^{-\sigma}
    &=m^{-\sigma}\sum_{a\ge1}a^{-h\sigma},\end{aligned}$$ which gives [\[eq:rho-S,eq:rho-M\]](#eq:rho-S,eq:rho-M){reference-type="ref" reference="eq:rho-S,eq:rho-M"} with their exact convergence conditions. Because $m$ lies in its own fiber, $T_me_m=\lambda_me_m$. A rank-one map with range $\mathbb Ce_m$ then obeys $T_m^2=\lambda_mT_m$, and induction proves [\[eq:block-power\]](#eq:block-power){reference-type="ref" reference="eq:block-power"}.

Two type distinctions will be used repeatedly. The eigenvalue $\lambda_m$ depends on the full complex parameter $s$; the block singular value depends only on $\sigma$. Also, the block index $m$ is an $h$-free integer, not a prime. Confusing either pair erases the phenomenon we are trying to measure.

# Existence, ideal membership, and the common cyclic ledger {#sec:ledger}

The block decomposition converts operator questions into positive sums. This also makes every strict endpoint visible without analytic continuation or finite truncation.

[\[prop:existence\]]{#prop:existence label="prop:existence"} $S_{h,s}$ is bounded exactly when $\sigma>0$, and $M_{h,s}$ is bounded exactly when $\sigma>1/h$. Each bounded operator is compact.

If $\sigma\le0$, the saturated block $m=p^{h-1}$ contains $p^{h-1+r}$ for every $r\ge0$, and its coefficient square mass diverges. Thus $S_{h,s}$ cannot be bounded. Suppose $\sigma>0$. A nonsaturated local contribution to [\[eq:rho-S\]](#eq:rho-S){reference-type="ref" reference="eq:rho-S"} is $p^{-e\sigma}<1$. A saturated contribution is $$b_p=p^{-(h-1)\sigma}(1-p^{-\sigma})^{-1}.$$ Since $b_p\to0$, only finitely many $b_p$ exceed one; their product is a uniform bound for all squared block norms. Hence $S_{h,s}$ is bounded.

As $m\to\infty$ through $\mathcal F_h$, at least one prime divisor of $m$ tends to infinity because every exponent is at most $h-1$. Its local contribution tends to zero, while all other contributions are bounded by the fixed product of the finitely many exceptional factors. Therefore $\rho_S(m)\to0$. An orthogonal direct sum of rank-one blocks is compact exactly when its block norms tend to zero.

For $M_{h,s}$, the block at $m=1$ has squared mass $\zeta(h\sigma)$, which is finite exactly for $\sigma>1/h$. On this domain $\rho_M(m)=\zeta(h\sigma)^{1/2}m^{-\sigma/2}\to0$, giving both boundedness and compactness.

[\[prop:schatten\]]{#prop:schatten label="prop:schatten"} For $k\ge1$ and $0<q<\infty$, $$\begin{aligned}
  S_{h,s}^{k}\in\mathcal S_q&\iff k\sigma q>2,\\
  M_{h,s}^{k}\in\mathcal S_q&\iff \sigma>1/h\ \text{and}\ k\sigma q>2.\end{aligned}$$ Every equality endpoint fails.

For $k=1$, orthogonality and [\[eq:rho-S\]](#eq:rho-S){reference-type="ref" reference="eq:rho-S"} give $$\sum_{m\in\mathcal F_h}\rho_S(m)^q
  =\prod_p\left[
    1+\sum_{e=1}^{h-2}p^{-e\sigma q/2}
    +p^{-(h-1)\sigma q/2}(1-p^{-\sigma})^{-q/2}
    \right].
  \label{eq:S-schatten-product}$$ When $h\ge3$, the first nonconstant term is $p^{-\sigma q/2}$; when $h=2$, the saturated term is asymptotic to the same quantity. The positive Euler product converges exactly for $\sigma q/2>1$.

For $M$, $$\sum_{m\in\mathcal F_h}\rho_M(m)^q
  =\zeta(h\sigma)^{q/2}
    \sum_{m\in\mathcal F_h}m^{-\sigma q/2}
  =\zeta(h\sigma)^{q/2}
    \frac{\zeta(\sigma q/2)}{\zeta(h\sigma q/2)}.
  \label{eq:M-schatten-product}$$ The first factor imposes the boundedness condition $\sigma>1/h$; the positive $h$-free sum converges exactly for $\sigma q/2>1$.

By [\[eq:block-power\]](#eq:block-power){reference-type="ref" reference="eq:block-power"}, the unique singular value of $T_m^k$ is $|\lambda_m|^{k-1}\rho_T(m)$. Repeating the two products replaces the leading exponent $\sigma q/2$ by $k\sigma q/2$ while leaving the modulo fiber factor $\zeta(h\sigma)^{q/2}$ unchanged. This proves the stated conditions. At equality, the leading positive prime sum is harmonic over the primes, so cancellation cannot rescue the endpoint.

[\[prop:cyclic\]]{#prop:cyclic label="prop:cyclic"} On either bounded domain, the nonzero spectrum is the simple set $\{m^{-s/2}:m\in\mathcal F_h\}$. On the common bounded domain, if $k\sigma>2$, then [\[eq:intro-trace\]](#eq:intro-trace){reference-type="ref" reference="eq:intro-trace"} holds. For every integer $r\ge1$ satisfying $\sigma>1/h$ and $r\sigma>2$, the regularized determinant identity [\[eq:intro-det\]](#eq:intro-det){reference-type="ref" reference="eq:intro-det"} holds.

Each block has the sole nonzero eigenvalue $\lambda_m$ by [\[lem:block-ledger\]](#lem:block-ledger){reference-type="ref" reference="lem:block-ledger"}. Since $\sigma>0$ on every bounded domain, $|\lambda_m|=m^{-\sigma/2}$ is strictly decreasing with $m$; hence no two blocks contribute the same eigenvalue. Compactness adds only zero to the spectrum.

If $k\sigma>2$, [\[prop:schatten\]](#prop:schatten){reference-type="ref" reference="prop:schatten"} makes the relevant powers trace class, and absolute convergence permits the block traces to be summed: $$\begin{aligned}
  \operatorname{Tr}(T^k)
    &=\sum_{m\in\mathcal F_h}\lambda_m^k
      =\prod_p\sum_{e=0}^{h-1}p^{-eks/2}\\
    &=\prod_p\frac{1-p^{-hks/2}}{1-p^{-ks/2}}
      =\frac{\zeta(ks/2)}{\zeta(hks/2)}.\end{aligned}$$ At $k\sigma=2$, the modulus sum is the divergent $h$-free harmonic series, so the equality line is excluded.

The determinant statement follows from the common simple nonzero eigenvalues and the regularized determinant product in Simon [@Simon2005 Ch. 9, pp. 75--80]; the exact product and its legality are recorded in [10](#app:determinants){reference-type="ref" reference="app:determinants"}. Nothing in that argument implies similarity.

::: {#tab:ledgers}
  ------------------------------------------------------------------------------------------------------------
  Quantity                Saturated $S_{h,s}$                                    Modulo $M_{h,s}$
  ----------------------- ------------------------------------------------------ -----------------------------
  Bounded domain          $\sigma>0$                                             $\sigma>1/h$

  Nonzero eigenvalues

  Block singular square   $m^{-\sigma}\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1}$   $m^{-\sigma}\zeta(h\sigma)$

  Riesz norm              $\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1/2}$            $\zeta(h\sigma)^{1/2}$

  Similarity to normal    $\sigma>1$                                             $\sigma>1/h$
  ------------------------------------------------------------------------------------------------------------

  : The common cyclic ledger and the distinct metric/angular ledgers.
:::

# Isospectrality without bounded similarity {#sec:similarity}

The spectral idempotent for the nonzero eigenvalue in block $m$ is $$\Pi_{T,m}=\lambda_m^{-1}T_m.
  \label{eq:riesz-block}$$ It is an oblique projection onto $\mathbb Ce_m$, and therefore $$\|\Pi_{T,m}\|=\frac{\rho_T(m)}{|\lambda_m|}.
  \label{eq:riesz-ratio}$$ Combining this ratio with the two block masses yields $$\begin{aligned}
  \|\Pi_{S,m}\|
    &=\prod_{p\in J_h(m)}(1-p^{-\sigma})^{-1/2},
      \label{eq:riesz-S}\\
  \|\Pi_{M,m}\|&=\sqrt{\zeta(h\sigma)}.
      \label{eq:riesz-M}\end{aligned}$$

The following block lemma supplies the converse that a mere appeal to necessary projection bounds would miss.

[\[lem:uniform-diagonalization\]]{#lem:uniform-diagonalization label="lem:uniform-diagonalization"} Let $T=\bigoplus_mT_m$ be a compact orthogonal direct sum of rank-one blocks. Suppose each block has nonzero eigenvalue $\lambda_m$ with range $\mathbb Ce_m$, and suppose that the $\lambda_m$ are pairwise distinct. Then $T$ is boundedly similar to the normal diagonal operator with entries $\lambda_m$ and zeros on the block kernels if and only if $\sup_m\|\lambda_m^{-1}T_m\|<\infty$.

If $T=XNX^{-1}$ and $N$ is normal, the nonzero spectral projections of $N$ are orthogonal. Hence those of $T$ have norms at most $\|X\|\|X^{-1}\|$.

Conversely, decompose a block as $\mathcal H_m=\mathbb Ce_m\oplus K_m$. It has the matrix form $$T_m=\begin{pmatrix}\lambda_m&\varphi_m\\0&0\end{pmatrix}.$$ Set $$Y_m=\begin{pmatrix}1&-\lambda_m^{-1}\varphi_m\\0&I_{K_m}\end{pmatrix}.$$ A direct multiplication gives $Y_m^{-1}T_mY_m=\operatorname{diag}(\lambda_m,0)$. The norm of $\lambda_m^{-1}\varphi_m$ is controlled by the norm of the idempotent $\lambda_m^{-1}T_m$; therefore the hypothesis uniformly bounds both $Y_m$ and $Y_m^{-1}$. The direct sum $Y=\bigoplus_mY_m$ is bounded and invertible and conjugates $T$ to the stated diagonal. Since $|\lambda_m|\to0$, that diagonal is compact and normal. A norm identity and explicit bounds are given in [9](#app:graph-transform){reference-type="ref" reference="app:graph-transform"}.

[\[thm:similarity\]]{#thm:similarity label="thm:similarity"} $$\begin{aligned}
  S_{h,s}\sim_{\mathrm{bd}}\text{ compact normal}&\iff\sigma>1,\\
  M_{h,s}\sim_{\mathrm{bd}}\text{ compact normal}&\iff\sigma>1/h.\end{aligned}$$

The modulo norm in [\[eq:riesz-M\]](#eq:riesz-M){reference-type="ref" reference="eq:riesz-M"} is a finite constant, independent of $m$, throughout the bounded domain. The lemma applies.

Every finite set of primes can occur as $J_h(m)$, by taking $m=\prod_{p\in E}p^{h-1}$. Consequently $$\sup_{m\in\mathcal F_h}\|\Pi_{S,m}\|
  =\left(\prod_p(1-p^{-\sigma})^{-1}\right)^{1/2}$$ as a finite value or $+\infty$. This is finite exactly for $\sigma>1$. The lemma again gives both directions.

In the full interval $1/h<\sigma\le1$, both operators exist and have the same simple nonzero spectrum. Their common power traces and determinants also agree whenever the corresponding ideal condition is met; here "determinants" means order-$r$ regularized determinants for integers $r$ satisfying $r\sigma>2$, never the order-one Fredholm determinant. Yet one operator has uniformly controlled eigenprojections and the other does not. This is an obstruction to bounded similarity, not merely to unitary equivalence.

# Primorial growth of saturated spectral projections {#sec:primorial}

The failure of uniform similarity for $0<\sigma\le1$ has a precise maximal order. Let $p_1<p_2<\cdots$ be the primes and $P_k=\prod_{j\le k}p_j$, with $P_0=1$. For $x\ge1$, let $k(x)$ be the largest integer for which $$P_{k(x)}^{h-1}\le x,
  \qquad m_x=P_{k(x)}^{h-1}.
  \label{eq:primorial-index}$$

[\[prop:primorial-optimizer\]]{#prop:primorial-optimizer label="prop:primorial-optimizer"} For every $x\ge1$ and $\sigma>0$, $$\max_{\substack{m\le x\\m\in\mathcal F_h}}\|\Pi_{S,m}\|
  =\prod_{p\mid P_{k(x)}}(1-p^{-\sigma})^{-1/2},
  \label{eq:exact-primorial-max}$$ and $m_x$ is a maximizing label.

Suppose $m\le x$ has $r=|J_h(m)|$ saturated primes. Their mandatory contribution to $m$ gives $$\prod_{p\in J_h(m)}p^{h-1}\le m\le x.$$ If $r\ge k(x)+1$, the left side is at least $P_{k(x)+1}^{h-1}>x$, a contradiction. For fixed $r$, replacing a saturated prime by a smaller omitted prime decreases the arithmetic cost and increases its factor $(1-p^{-\sigma})^{-1/2}$. Thus the best $r$-prime set is $\{p_1,\ldots,p_r\}$. Adding another admissible saturated prime strictly increases the projection norm. The optimum therefore uses $r=k(x)$ and is attained at $m_x$.

The exact optimizer turns the similarity wall into a classical prime-product problem. Write $y=p_{k(x)}$. The prime number theorem gives $$(h-1)\vartheta(y)\sim\log x,
  \qquad
  y\sim\frac{\log x}{h-1}.
  \label{eq:y-asymptotic}$$

[\[thm:three-regimes\]]{#thm:three-regimes label="thm:three-regimes"} As $x\to\infty$,

1.  if $\sigma>1$, then $$\max_{m\le x,\,m\in\mathcal F_h}\|\Pi_{S,m}\|
          \longrightarrow\sqrt{\zeta(\sigma)};$$

2.  if $\sigma=1$, then $$\max_{m\le x,\,m\in\mathcal F_h}\|\Pi_{S,m}\|
          \sim\sqrt{\mathrm e^\gamma\log\log x};$$

3.  if $0<\sigma<1$, then $$\log\max_{m\le x,\,m\in\mathcal F_h}\|\Pi_{S,m}\|
          \sim
          \frac{(h-1)^{\sigma-1}(\log x)^{1-\sigma}}
               {2(1-\sigma)\log\log x}.$$

For $\sigma>1$, the partial Euler products in [\[eq:exact-primorial-max\]](#eq:exact-primorial-max){reference-type="ref" reference="eq:exact-primorial-max"} converge to $\prod_p(1-p^{-\sigma})^{-1/2}=\sqrt{\zeta(\sigma)}$. At $\sigma=1$, Mertens' product theorem [@MontgomeryVaughan2006 Thm. 2.7(e), p. 50] gives $$\prod_{p\le y}(1-p^{-1})^{-1/2}
    \sim\sqrt{\mathrm e^\gamma\log y},$$ and [\[eq:y-asymptotic\]](#eq:y-asymptotic){reference-type="ref" reference="eq:y-asymptotic"} implies $\log y\sim\log\log x$.

For $0<\sigma<1$, expanding the logarithm and applying partial summation to the prime number theorem [@MontgomeryVaughan2006 Thm. 6.9, p. 179], $$\begin{aligned}
  \log\prod_{p\le y}(1-p^{-\sigma})^{-1/2}
    &=\frac12\sum_{p\le y}-\log(1-p^{-\sigma})\\
    &\sim \frac12\sum_{p\le y}p^{-\sigma}
     \sim\frac{y^{1-\sigma}}{2(1-\sigma)\log y}.\end{aligned}$$ Substituting [\[eq:y-asymptotic\]](#eq:y-asymptotic){reference-type="ref" reference="eq:y-asymptotic"} produces the factor $(h-1)^{\sigma-1}$. In particular, neither its reciprocal nor its deletion is compatible with the exact optimizer.

The proof uses no finite maximization. The finite optimizer rows reported in [12](#app:canonical-evidence){reference-type="ref" reference="app:canonical-evidence"} are implementation checks of [\[prop:primorial-optimizer\]](#prop:primorial-optimizer){reference-type="ref" reference="prop:primorial-optimizer"}; they are not evidence for the asymptotic regimes.

# Singular-value Weyl laws and the crossover {#sec:weyl}

The saturated block mass is not a constant multiple of $m^{-\sigma}$, so ordinary $h$-free counting is insufficient. Define the positive generalized weight $$w_{h,\sigma}(m)=m\prod_{p\in J_h(m)}(1-p^{-\sigma})^{1/\sigma}.
  \label{eq:generalized-weight}$$ Then [\[eq:rho-S\]](#eq:rho-S){reference-type="ref" reference="eq:rho-S"} is exactly $\rho_S(m)=w_{h,\sigma}(m)^{-\sigma/2}$.

## The saturated count

Consider the generalized Dirichlet series $$F_{h,\sigma}(z)=\sum_{m\in\mathcal F_h}w_{h,\sigma}(m)^{-z}
  =\prod_p L_p(z),
  \label{eq:F-series}$$ where initially $\Re z>1$ and $$L_p(z)=\sum_{e=0}^{h-2}p^{-ez}
    +p^{-(h-1)z}(1-p^{-\sigma})^{-z/\sigma}.
  \label{eq:L-local}$$ Factor the single zeta pole: $$F_{h,\sigma}(z)=\zeta(z)G_{h,\sigma}(z),
  \qquad
  G_{h,\sigma}(z)=\prod_p(1-p^{-z})L_p(z).
  \label{eq:F-factorization}$$

[\[lem:tauberian-strip\]]{#lem:tauberian-strip label="lem:tauberian-strip"} $G_{h,\sigma}$ is holomorphic in $$\Re z>\theta_{h,\sigma}
    :=\max\{\frac1h,\frac{1-\sigma}{h-1}\}<1.
  \label{eq:theta-strip}$$ At $z=1$ it has the positive value $C_{h,\sigma}$ in [\[eq:intro-C\]](#eq:intro-C){reference-type="ref" reference="eq:intro-C"}.

On a compact subset of a right half-plane, expand the final term of [\[eq:L-local\]](#eq:L-local){reference-type="ref" reference="eq:L-local"} uniformly for large $p$. Multiplication by $1-p^{-z}$ cancels the first-order $p^{-z}$ term, leaving $$(1-p^{-z})L_p(z)
  =1+O(p^{-h\Re z})
      +O(p^{-(h-1)\Re z-\sigma}).
  \label{eq:local-cancellation}$$ Both error sums converge locally uniformly precisely when $h\Re z>1$ and $(h-1)\Re z+\sigma>1$. The Weierstrass theorem for Euler products gives holomorphy in [\[eq:theta-strip\]](#eq:theta-strip){reference-type="ref" reference="eq:theta-strip"}. Because $h\ge2$ and $\sigma>0$, the boundary lies strictly to the left of one. Substituting $z=1$ gives [\[eq:intro-C\]](#eq:intro-C){reference-type="ref" reference="eq:intro-C"}; every local factor is positive.

[\[lem:wiener-ikehara-check\]]{#lem:wiener-ikehara-check label="lem:wiener-ikehara-check"} Let $$\mu_{h,\sigma}=\sum_{m\in\mathcal F_h}\delta_{w_{h,\sigma}(m)},
  \qquad
  A_S(x)=\mu_{h,\sigma}((0,x]).
  \label{eq:counting-measure}$$ This positive measure is locally finite and has only finitely many atoms below one. If $\mu_+$ is its restriction to $[1,\infty)$, then, for $\Re z>1$, $$\int_{1^-}^{\infty}x^{-z}\,d\mu_+(x)
    =F_{h,\sigma}(z)-E_{h,\sigma}(z),
  \label{eq:mellin-stieltjes}$$ where $E_{h,\sigma}$ is a finite entire sum. Moreover, $$F_{h,\sigma}(z)-E_{h,\sigma}(z)
    -\frac{C_{h,\sigma}}{z-1}
  \label{eq:ikehara-remainder}$$ extends holomorphically to a neighborhood of the closed half-plane $\Re z\ge1$. Thus the classical nondecreasing Mellin--Stieltjes form of Wiener--Ikehara [@Korevaar2004 Ch. III, Sec. 4, pp. 124--127] applies to $\mu_+$ with residue $C_{h,\sigma}$.

For exponent $e<h-1$ the nontrivial local weight is $p^e>1$, whereas for $e=h-1$ it is $p^{h-1}(1-p^{-\sigma})^{1/\sigma}$, which tends to infinity with $p$. Only finitely many prime--exponent pairs therefore have local weight at most any prescribed bound. More explicitly, the pairs with local weight at most one form a finite set; the product of their smallest possible contributions is some $c_0>0$. If $w_{h,\sigma}(m)\le B$, every other nontrivial local factor is at most $B/c_0$, so it belongs to another finite set of prime--exponent pairs. Since one exponent is chosen per prime, only finitely many such $m$ exist. This proves local finiteness and, with $B=1$, finiteness below one.

Removing the atoms below one subtracts the finite entire Dirichlet polynomial $E_{h,\sigma}$, proving [\[eq:mellin-stieltjes\]](#eq:mellin-stieltjes){reference-type="ref" reference="eq:mellin-stieltjes"}. By [\[eq:F-factorization,lem:tauberian-strip\]](#eq:F-factorization,lem:tauberian-strip){reference-type="ref" reference="eq:F-factorization,lem:tauberian-strip"}, $F_{h,\sigma}=\zeta G_{h,\sigma}$ throughout a strip crossing $\Re z=1$, $G_{h,\sigma}(1)=C_{h,\sigma}$, and $\zeta(z)-(z-1)^{-1}$ is holomorphic there. Expanding $G_{h,\sigma}(z)=C_{h,\sigma}+(z-1)H(z)$ near one shows that [\[eq:ikehara-remainder\]](#eq:ikehara-remainder){reference-type="ref" reference="eq:ikehara-remainder"} is holomorphic at one and elsewhere in a neighborhood of $\Re z\ge1$. These are precisely the positivity, convergence, pole, and boundary-regularity hypotheses of the cited theorem.

[\[prop:S-weyl\]]{#prop:S-weyl label="prop:S-weyl"} For $\sigma>0$, let $$A_S(x)=\#\{m\in\mathcal F_h:w_{h,\sigma}(m)\le x\}.$$ Then $$A_S(x)\sim C_{h,\sigma}x,
  \qquad
  s_n(S_{h,s})\sim(\frac{C_{h,\sigma}}{n})^{\sigma/2}.
  \label{eq:S-weyl}$$

The verified hypotheses in [\[lem:wiener-ikehara-check\]](#lem:wiener-ikehara-check){reference-type="ref" reference="lem:wiener-ikehara-check"} give $A_S(x)\sim C_{h,\sigma}x$; the finitely many removed atoms contribute only $O(1)$. The number of singular values at least $t$ equals $A_S(t^{-2/\sigma})$. Monotone asymptotic inversion gives the second relation. Normal convergence of the Euler product is detailed in [11](#app:tauberian-details){reference-type="ref" reference="app:tauberian-details"}.

## Modulo and eigenvalue counts

The elementary $h$-free density is $$\#\{m\le x:m\in\mathcal F_h\}\sim\frac{x}{\zeta(h)}.
  \label{eq:hfree-density}$$ For completeness, the identity $\mathbf 1_{\mathcal F_h}(n)=\sum_{d^h\mid n}\mu(d)$ gives $$\sum_{n\le x}\mathbf 1_{\mathcal F_h}(n)
  =\sum_{d\le x^{1/h}}\mu(d)\lfloor\frac{x}{d^h}\rfloor
  =\frac{x}{\zeta(h)}+O_h(x^{1/h}).$$

[\[prop:M-weyl\]]{#prop:M-weyl label="prop:M-weyl"} For $\sigma>1/h$, $$\begin{aligned}
  s_n(M_{h,s})
    &\sim(\frac{D_{h,\sigma}}{n})^{\sigma/2},
      &D_{h,\sigma}&=\frac{\zeta(h\sigma)^{1/\sigma}}{\zeta(h)},
      \label{eq:M-weyl}\\
  |\lambda_n|
    &\sim(\frac{1/\zeta(h)}{n})^{\sigma/2}.
      \label{eq:eigen-weyl}\end{aligned}$$

By [\[eq:rho-M\]](#eq:rho-M){reference-type="ref" reference="eq:rho-M"}, $\rho_M(m)\ge t$ exactly when $m\le\zeta(h\sigma)^{1/\sigma}t^{-2/\sigma}$. Applying [\[eq:hfree-density\]](#eq:hfree-density){reference-type="ref" reference="eq:hfree-density"} yields the singular-value count $D_{h,\sigma}t^{-2/\sigma}$. The same count without the fiber multiplier gives the eigenvalue constant $1/\zeta(h)$. Monotone inversion proves [\[eq:M-weyl,eq:eigen-weyl\]](#eq:M-weyl,eq:eigen-weyl){reference-type="ref" reference="eq:M-weyl,eq:eigen-weyl"}.

[\[cor:crossover\]]{#cor:crossover label="cor:crossover"} For every $h\ge2$, $C_{h,1}=D_{h,1}=1$.

At $\sigma=1$, the bracket in [\[eq:intro-C\]](#eq:intro-C){reference-type="ref" reference="eq:intro-C"} is $$\sum_{e=0}^{h-2}p^{-e}
  +p^{-(h-1)}(1-p^{-1})^{-1}
  =\sum_{e=0}^{\infty}p^{-e}=(1-p^{-1})^{-1}.$$ Every Euler factor in $C_{h,1}$ is therefore one. Independently, $D_{h,1}=\zeta(h)/\zeta(h)=1$.

The crossover is an equality, not a sign-change theorem: we make no claim about the ordering of $C_{h,\sigma}$ and $D_{h,\sigma}$ for $\sigma\ne1$. None of the asymptotic or endpoint statements in this section depends on finite records.

# Self-commutator ideals {#sec:commutators}

The operator ideal wall arises from the first power of a block singular value. A self-commutator sees its square and hence produces a different threshold.

[\[lem:rankone-commutator\]]{#lem:rankone-commutator label="lem:rankone-commutator"} Let $T=\rho\,u\otimes v$, where $u,v$ are unit vectors, and let $a$ be the modulus of the unique nonzero eigenvalue. The two possibly zero singular values of $T^*T-TT^*$ are equal to $$c=\rho^2\sqrt{1-a^2/\rho^2}.
  \label{eq:commutator-c}$$

$T^*T=\rho^2v\otimes v$ and $TT^*=\rho^2u\otimes u$. Their difference is self-adjoint and traceless on $\operatorname{span}\{u,v\}$. Its determinant there is $-\rho^4(1-|\langle u,v\rangle|^2)$. Since $a=\rho|\langle u,v\rangle|$, the two eigenvalues are $\pm c$, proving the claim.

For the arithmetic blocks, [\[eq:rho-S,eq:rho-M\]](#eq:rho-S,eq:rho-M){reference-type="ref" reference="eq:rho-S,eq:rho-M"} gives the exact angle ratios $$\begin{aligned}
  \frac{|\lambda_m|^2}{\rho_S(m)^2}
    &=\prod_{p\in J_h(m)}(1-p^{-\sigma}),
      \label{eq:S-angle}\\
  \frac{|\lambda_m|^2}{\rho_M(m)^2}
    &=\frac1{\zeta(h\sigma)}.
      \label{eq:M-angle}\end{aligned}$$

[\[thm:commutator-wall\]]{#thm:commutator-wall label="thm:commutator-wall"} For $0<q<\infty$, $$\begin{aligned}
\in\mathcal S_q
    &\iff\sigma q>1,\\
  [M_{h,s}^*,M_{h,s}]\in\mathcal S_q
    &\iff\sigma>1/h\ \text{and}\ \sigma q>1.\end{aligned}$$

Let $c_m$ be the quantity in [\[eq:commutator-c\]](#eq:commutator-c){reference-type="ref" reference="eq:commutator-c"} for block $m$. For $S$, $c_m\le\rho_S(m)^2$, so $$\sum_m c_m^q\le\sum_m\rho_S(m)^{2q}<\infty$$ whenever $\sigma q>1$, by [\[prop:schatten\]](#prop:schatten){reference-type="ref" reference="prop:schatten"} with exponent $2q$.

For necessity when $h\ge3$, fix a prime $p_0$ and let $m_r=p_0^{h-1}r$ as $r\ne p_0$ varies over primes. The prime $r$ has exponent one and is not saturated, so $J_h(m_r)=\{p_0\}$. The angle factor in [\[eq:S-angle\]](#eq:S-angle){reference-type="ref" reference="eq:S-angle"} is a fixed positive constant and $c_{m_r}\asymp r^{-\sigma}$. The prime sum $\sum_r c_{m_r}^q$ diverges when $\sigma q\le1$.

That witness is ill typed for $h=2$, because exponent one is already saturated. Instead fix $p_0$ and take $m_r=p_0r$. Now $J_2(m_r)=\{p_0,r\}$, while $$1-(1-p_0^{-\sigma})(1-r^{-\sigma})\ge p_0^{-\sigma}.$$ Again $c_{m_r}\asymp r^{-\sigma}$, proving divergence at and below the same wall.

For $M$, [\[eq:M-angle\]](#eq:M-angle){reference-type="ref" reference="eq:M-angle"} makes the angular factor a fixed positive constant throughout the bounded domain. Thus $c_m\asymp m^{-\sigma}$, and the $h$-free sum $\sum_mc_m^q$ converges exactly for $\sigma q>1$. The boundedness condition $\sigma>1/h$ remains mandatory. The factor two from the two singular values per nonzero block does not affect membership.

The $h=2$ case also admits a closed Hilbert--Schmidt identity. For a squarefree $m$, define $$\Lambda_m=\prod_{p\mid m}(p^\sigma-1)^{-1},
  \qquad
  \Delta_m=\prod_{p\mid m}(1-p^{-\sigma}).$$ Then $\rho_S(m)^2=\Lambda_m$ and the two commutator singular values are $\Lambda_m\sqrt{1-\Delta_m}$.

[\[prop:h2-euler-control\]]{#prop:h2-euler-control label="prop:h2-euler-control"} If $\sigma>1/2$, then $$\|[S_{2,s}^*,S_{2,s}]\|_2^2
  =2\left\{
    \prod_p\left[1+(p^\sigma-1)^{-2}\right]
    -\prod_p\left[1+\frac{p^{-2\sigma}}{1-p^{-\sigma}}\right]
    \right\}.
  \label{eq:h2-HS}$$ Both products converge separately.

Summing the two squared singular values gives $2\sum_m\Lambda_m^2(1-\Delta_m)$. Squarefree multiplicativity yields the first Euler product from $\sum_m\Lambda_m^2$. The local nontrivial factor in $\Lambda_m^2\Delta_m$ is $$(p^\sigma-1)^{-2}(1-p^{-\sigma})
  =\frac{p^{-2\sigma}}{1-p^{-\sigma}},$$ which gives the second product. Each nonconstant local factor is $O(p^{-2\sigma})$, so both products converge for $\sigma>1/2$. At equality, [\[thm:commutator-wall\]](#thm:commutator-wall){reference-type="ref" reference="thm:commutator-wall"} already gives divergence; no subtraction of divergent Euler products is defined.

No ideal endpoint in this section is inferred from a finite block. The strict failure comes from an explicit infinite positive subfamily.

# Independent recomputation, controls, and limitations {#sec:evaluation}

The formulas were recomputed along two deliberately disjoint routes. One route enumerated the raw maps, constructed finite fiber matrices, and computed spectra, singular values, powers, Riesz idempotents, and self-commutators directly. The other route began from prime-exponent states and independently derived Euler factors, strict convergence walls, the Tauberian strip and residue, the primorial asymptotics, and the commutator families. A third checker audited the infinite proof certificates, while a finite comparator inspected only the common projected fields. The finite and analytic routes agreed on their declared overlap, and registered hostile mutations were rejected. Exact case counts, input seals, and finite optimizer rows are reproducibility metadata in [12](#app:canonical-evidence){reference-type="ref" reference="app:canonical-evidence"}, not premises of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

This separation matters. A growing finite compression cannot establish boundedness at an infinite fiber, a strict Schatten endpoint, a Tauberian continuation, or uniform boundedness of all Riesz projections. Conversely, the analytic proof does not certify that a software implementation parses the two maps correctly. The two forms of evidence answer different questions.

#### Free-UFD negative control.

Let $\mathfrak M$ be the free commutative monoid generated by atoms $a_j$, and assign $N(a_j)=p_j$, the $j$th rational prime. Define exponent saturation, reduction modulo $h$, and the weights through this norm. The relabeling $a_j\leftrightarrow p_j$ reproduces every exponent combinatoric and Euler product used above, even though the atoms carry no addition and no semantics as rational primes. Thus the paired theorem detects normed unique factorization and its two retractions; by itself it does not establish rational-prime selectivity. This control receives no contribution credit.

#### Scope.

The results concern the frozen maps [\[eq:intro-maps\]](#eq:intro-maps){reference-type="ref" reference="eq:intro-maps"}, the coefficient $n^{-s/2}$, and the counting measure on $\mathbb N$. We do not claim a theorem for arbitrary weighted composition operators, changed base measures, other coefficient weights, or non-free factorization systems. Equal regularized determinants are used only to expose cyclic blindness to block geometry. They are not interpreted as a self-adjoint spectral determinant or as a Hilbert--Pólya construction. The equality $C_{h,1}=D_{h,1}=1$ likewise gives no universal ordering away from the crossover.

#### Conclusion.

The two retractions preserve exactly the same $h$-free eigenlines but store discarded prime exponents in incompatible fibers. That difference shifts the existence wall from $0$ to $1/h$, the saturated similarity wall to $1$, and the commutator wall to $1/q$, while leaving the common cyclic ledger unchanged wherever it is legal. The primorial and Weyl laws make the gap quantitative: isospectrality here is not an approximation to similarity, but a precise separation between arithmetic fixed points and the geometry of their fibers.

# The block graph transform {#app:graph-transform}

We record the elementary similarity lemma with explicit constants. Let $K$ be a Hilbert space and $$T=\begin{pmatrix}\lambda&\varphi\\0&0\end{pmatrix}
  \quad\text{on }\mathbb C\oplus K,
  \qquad \lambda\ne0,$$ where $\varphi:K\to\mathbb C$. Its spectral idempotent at $\lambda$ is $$P=\lambda^{-1}T
   =\begin{pmatrix}1&g\\0&0\end{pmatrix},
  \qquad g=\lambda^{-1}\varphi.$$ The row-operator norm gives $$\|P\|=(1+\|g\|^2)^{1/2}.
  \label{eq:projection-graph-norm}$$ Define $$Y=\begin{pmatrix}1&-g\\0&I\end{pmatrix},
  \qquad
  Y^{-1}=\begin{pmatrix}1&g\\0&I\end{pmatrix}.$$ Then $$Y^{-1}TY=\begin{pmatrix}\lambda&0\\0&0\end{pmatrix},
  \qquad
  \|Y\|,\|Y^{-1}\|\le1+\|g\|.
  \label{eq:graph-transform-bound}$$ Thus a uniform bound on the block idempotents is precisely what is needed for the direct sum of the graph transforms to be bounded and invertible.

Conversely, if $T=XNX^{-1}$ and $N$ is compact normal, the Riesz projections $Q_m$ of $N$ at distinct nonzero eigenvalues are orthogonal. The corresponding projections of $T$ are $XQ_mX^{-1}$, so $$\sup_m\|XQ_mX^{-1}\|\le\|X\|\|X^{-1}\|.$$ This proves the necessity and sufficiency used in [\[lem:uniform-diagonalization\]](#lem:uniform-diagonalization){reference-type="ref" reference="lem:uniform-diagonalization"} without appealing to a finite-dimensional condition number that may depend on the block.

# Legality of the common regularized determinant {#app:determinants}

For an integer $r\ge1$ and $T\in\mathcal S_r$, the order-$r$ regularized determinant is standard [@Simon2005 Ch. 9, pp. 75--80]. In terms of the algebraic nonzero eigenvalues, counted with multiplicity, $$\det_r(I-zT)
  =\prod_{\lambda\in\operatorname{spec}(T)\setminus\{0\}}
    \left[(1-z\lambda)
      \exp\left(\sum_{j=1}^{r-1}\frac{(z\lambda)^j}{j}\right)
    \right].
  \label{eq:regularized-product}$$ The empty sum at $r=1$ gives the Fredholm determinant. Membership in $\mathcal S_r$ guarantees convergence and an entire function of $z$.

For the operators in this paper, [\[prop:schatten\]](#prop:schatten){reference-type="ref" reference="prop:schatten"} shows that both $S_{h,s}$ and $M_{h,s}$ lie in $\mathcal S_r$ exactly on the common legal domain $$\sigma>1/h,
  \qquad r\sigma>2.
  \label{eq:det-legal-domain}$$ Their nonzero eigenvalues are the same simple sequence $\lambda_m=m^{-s/2}$, $m\in\mathcal F_h$. Substitution in [\[eq:regularized-product\]](#eq:regularized-product){reference-type="ref" reference="eq:regularized-product"} therefore proves $$\det_r(I-zS_{h,s})=\det_r(I-zM_{h,s})$$ on [\[eq:det-legal-domain\]](#eq:det-legal-domain){reference-type="ref" reference="eq:det-legal-domain"}. When $r=1$, this condition reads $\sigma>2$. No product is asserted for either unbounded algebraic map, and determinant equality is not used to infer bounded similarity. In particular, throughout the isospectral nonsimilarity band $1/h<\sigma\le1$, equality means equality in each common legal integer order $r>2/\sigma$; order $r=1$ does not occur there.

# Tauberian boundary details {#app:tauberian-details}

We make explicit the analytic inputs behind [\[prop:S-weyl\]](#prop:S-weyl){reference-type="ref" reference="prop:S-weyl"}. The local factor in [\[eq:L-local\]](#eq:L-local){reference-type="ref" reference="eq:L-local"} is entire in $z$ for each fixed $p$, because the bases are positive and powers use the real logarithm. On a compact set $K\subset\{\Re z>\theta_{h,\sigma}\}$, choose $\varepsilon>0$ so that $$h\Re z\ge1+\varepsilon,
  \qquad
  (h-1)\Re z+\sigma\ge1+\varepsilon
  \quad(z\in K).$$ The expansion [\[eq:local-cancellation\]](#eq:local-cancellation){reference-type="ref" reference="eq:local-cancellation"} is uniform on $K$, and the sum of its two majorants is bounded by a constant times $\sum_pp^{-1-\varepsilon}$. Hence the Euler product for $G_{h,\sigma}$ converges normally on $K$. This proves local uniform convergence and holomorphy, not merely pointwise convergence of formal factors.

At $z=1$, all local factors are positive and their deviations from one are summable. Thus $G_{h,\sigma}(1)=C_{h,\sigma}$ is finite and strictly positive. Since $$F_{h,\sigma}(z)=\zeta(z)G_{h,\sigma}(z),$$ $F_{h,\sigma}$ has a simple pole at one with residue $C_{h,\sigma}$ and no other singularity on $\Re z=1$. Subtracting the polar part gives a holomorphic boundary remainder. The counting measure, finite exceptional atoms, Mellin--Stieltjes transform, and the exact cited theorem are assembled in [\[lem:wiener-ikehara-check\]](#lem:wiener-ikehara-check){reference-type="ref" reference="lem:wiener-ikehara-check"}; the present appendix supplies only the normal-convergence detail used by that lemma.

Finally, if a decreasing positive sequence has counting function $N(t)\sim C t^{-\alpha}$ as $t\downarrow0$, elementary monotone inversion gives its $n$th term as $(C/n)^{1/\alpha}(1+o(1))$. Here $\alpha=2/\sigma$, which produces [\[eq:S-weyl\]](#eq:S-weyl){reference-type="ref" reference="eq:S-weyl"}. No numerical coefficient fit is involved.

# Compact canonical recomputation record {#app:canonical-evidence}

This appendix retains only the finite rows useful for inspecting the implementation of the exact optimizer. The machine-readable source seals, route inventories, 21 finite records, 15 independently audited infinite certificates, seven-case finite comparison, and hostile-suite transaction metadata are kept in the companion evidence ledger. They are not premises of any theorem in this paper.

::: {#tab:finite-primorial}
   $\sigma$   cutoff $x$    maximizer   primorial label ties
  ---------- ------------ ----------- ----------------- -----------------
    $2/3$        100               36                36 36
     $1$         1000             900               900 900
    $4/3$       10000             900               900 6300, 900, 9900

  : Exact finite optimizer rows generated from the sealed projection. The supercritical finite row has several ties; the canonical maximizer and the primorial label are both 900.
:::

These three rows test the finite optimizer implementation. They do not establish [\[thm:three-regimes\]](#thm:three-regimes){reference-type="ref" reference="thm:three-regimes"}, which follows from [\[prop:primorial-optimizer\]](#prop:primorial-optimizer){reference-type="ref" reference="prop:primorial-optimizer"} and classical prime asymptotics.
