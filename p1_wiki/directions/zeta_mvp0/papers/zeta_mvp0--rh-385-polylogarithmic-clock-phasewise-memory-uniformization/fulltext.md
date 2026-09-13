---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-385-polylogarithmic-clock-phasewise-memory-uniformization"
canonical_tex: "zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization/main.pdf"
source_sha256: "2900021c4273c572b661f0d117884f4faa149a7e945c5a4ce1243ea47ec18368"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Polylogarithmic-Clock Uniformization for Phasewise Chowla-Free Lag-Two Memory

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-385-polylogarithmic-clock-phasewise-memory-uniformization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $B>0$. For every clock $1\le q\le\lfloor(\log N)^B\rfloor$, consider the RH-379 class of universally distance-two-safe, $q$-periodic lag-two sign tables whose shift-two interpolation coefficient vanishes separately at each phase. We prove a limit uniform in both the clock and every table family in that class. If $S_N(q,f)$ is its normalized Möbius score and $L_q(f)$ is the fixed-clock limit, then $$\sup_{q\le\lfloor(\log N)^B\rfloor}\ \sup_{f\in\mathcal F_q}
         \lvert S_N(q,f)-L_q(f)\rvert\longrightarrow0.$$ The proof truncates squarefreeness at $P=\lfloor\sqrt{\log\log N}\rfloor$. With $M_P=(\prod_{p\le P}p)^2$, $Q=\operatorname{lcm}(q,M_P)$, $\tau_P=\sum_{p>P}p^{-2}$, and $D_*(N)$ the maximum of the uniform Davenport sums at $N$ and $N-2$, we retain the explicit bound $$\lvert S_N(q,f)-L_q(f)\rvert
   \le \frac{4\sqrt QD_*(N)}{N}+13\tau_P+\frac{6Q}{N}+\frac4N.$$ The Fourier coefficient costs are $1,1,2$; the last factor cannot be removed because a legal self-compatible table has $c_{21}=-2$. Consequently the finite optimizers converge uniformly to the fixed-clock optimizers, their triangular-array maximum tends to the RH-379 endpoint $B_\infty$, and the cofinal square clocks supply an explicit positive diagonal witness after the admissible set becomes nonempty. The result is not polynomial-clock uniformity, an adaptive-capacity limit, a projective infinite selector, an operator or trace construction, or a statement about Riemann zeros.
author:
- RH research program
bibliography:
- references.bib
date: 'August 8, 2026'
title: |
  Polylogarithmic-Clock Uniformization for\
  Phasewise Chowla-Free Lag-Two Memory
```

## Markdown 正文

**Keywords:** Möbius function; Davenport estimate; polylogarithmic clocks; squarefree cutoff; phasewise lag-two memory.

# Frozen problem and claim boundary

RH-366 records Davenport's estimate uniformly in the additive frequency [@Davenport1937; @IwaniecKowalski2004; @RH366]. RH-378 gives the exact six-monomial interpolation of lag-two tables, including the ordinary shift-two coefficient $c_{11}$ [@RH378]. RH-379 then optimizes the universally safe class with $c_{11}(r)=0$ at every fixed phase and proves $$\sup_{q<\infty}G(q)=B_\infty.
 \label{eq:rh379-supremum}$$ That theorem fixes $q$ before $N\to\infty$ [@RH379]. The purpose here is exactly one limit exchange: clocks may now grow no faster than a fixed power of $\log N$.

Let $$\mu_0(m)=
 \begin{cases}
  \mu(m),&m\ge1,\\
  0,&m\le0.
 \end{cases}
 \label{eq:zero-padding}$$ The zero padding in [\[eq:zero-padding\]](#eq:zero-padding){reference-type="eqref" reference="eq:zero-padding"} is part of the finite score, not an asymptotic convention.

Fix $q\ge1$. A family $f=(f_r)_{r\bmod q}$ belongs to $\mathcal F_q$ when each $f_r:\{-1,0,1\}^2\to\{-1,+1\}$ and the following hold.

1.  For every ternary input word, the output $\epsilon_n=f_{n\bmod q}(a_{n-2},a_n)$ never has $\epsilon_n=\epsilon_{n+2}=+1$.

2.  In the unique interpolation $$zf_r(x,z)=c_{01}(r)z+c_{02}(r)z^2+c_{11}(r)xz
     +c_{12}(r)xz^2+c_{21}(r)x^2z+c_{22}(r)x^2z^2,
     \label{eq:interpolation}$$ one has $c_{11}(r)=0$ for every phase $r$.

The first condition is universal safety, not safety merely along the Möbius word. The second is phasewise: no cancellation between unknown shift-two correlations carrying different phase weights is assumed.

Define $$S_N(q,f)=\frac1N\sum_{n\le N}\mu(n)
 f_{n\bmod q}\bigl(\mu_0(n-2),\mu(n)\bigr).
 \label{eq:finite-score}$$ The one-site progression densities come from RH-375, and RH-379 supplies the lag-two squarefree density and the resulting fixed-clock limit [@RH375; @RH379]: $$\begin{aligned}
 \delta_{q,r}&=\lim_{N\to\infty}\frac1N
  \sum_{\substack{n\le N\\n\equiv r\ (q)}}\mu(n)^2,
 \label{eq:delta}\\
 \vartheta_{q,r}&=\lim_{N\to\infty}\frac1N
  \sum_{\substack{n\le N\\n\equiv r\ (q)}}
       \mu(n-2)^2\mu(n)^2.
 \label{eq:theta}\end{aligned}$$ The corresponding fixed-clock functional is $$L_q(f)=\sum_{r\bmod q}
       \bigl(c_{02}(r)\delta_{q,r}+c_{22}(r)\vartheta_{q,r}\bigr).
 \label{eq:fixed-limit}$$

[\[lem:coefficient-census\]]{#lem:coefficient-census label="lem:coefficient-census"} Among the $512$ truth tables, exactly $192$ have $c_{11}=0$. On those tables, $$\begin{aligned}
 c_{01},c_{02},c_{12}&\in\{-1,0,1\},\\
 c_{21},c_{22}&\in\{-2,-1,0,1,2\}.\end{aligned}$$ There are $24$ distinct six-coefficient vectors, each with multiplicity eight. The table with plus-edge relation $$E=\{(0,-1),(0,+1)\}$$ is self-compatible and has vector $(c_{01},c_{02},c_{11},c_{12},c_{21},c_{22})=(1,0,0,0,-2,0)$.

This is exact ternary interpolation in the basis of [\[eq:interpolation\]](#eq:interpolation){reference-type="eqref" reference="eq:interpolation"}. The $c_{11}$ histogram over all $512$ tables is $$\begin{array}{c|rrrrr}
c_{11}&-1&-1/2&0&1/2&1\\ \hline
\text{count}&32&128&192&128&32.
\end{array}$$ Exact row enumeration gives the alphabets and multiplicities. For the displayed relation, every plus edge has source $0$ and target nonzero, so two plus edges cannot compose. Direct interpolation gives the stated vector. All $4608$ point evaluations are reproduced independently in the finite certificate; the enumeration is a finite identity, not asymptotic evidence.

# Squarefree cutoff and periodic Fourier bounds

Fix an integer $P\ge2$ and put $$\eta_P(m)=\prod_{p\le P}\bigl(1-\mathbf1_{p^2\mid m}\bigr),
 \qquad
 M_P=\left(\prod_{p\le P}p\right)^2,
 \qquad
 \tau_P=\sum_{p>P}\frac1{p^2}.
 \label{eq:cutoff}$$ Divisibility in [\[eq:cutoff\]](#eq:cutoff){reference-type="eqref" reference="eq:cutoff"} is defined for every integer. In particular, $$\eta_P(0)=0,\qquad \eta_P(-1)=1.
 \label{eq:eta-endpoints}$$ The function $\eta_P$ has period $M_P$. This is a valid period; it need not be the minimal period of a particular product involving $\eta_P$.

[\[lem:tail\]]{#lem:tail label="lem:tail"} For every positive integer $m$, $$0\le\eta_P(m)-\mu(m)^2
 \le\sum_{p>P}\mathbf1_{p^2\mid m}.
 \label{eq:point-tail}$$ Consequently, for every $X\ge1$, $$\sum_{m\le X}\bigl(\eta_P(m)-\mu(m)^2\bigr)
 \le\sum_{p>P}\left\lfloor\frac X{p^2}\right\rfloor
 \le X\tau_P.
 \label{eq:summed-tail}$$ The same inequalities compare every limiting periodic squarefree mean with its $P$-cutoff mean.

If $\eta_P(m)=1$ but $\mu(m)^2=0$, a prime $p>P$ has $p^2\mid m$. This proves [\[eq:point-tail\]](#eq:point-tail){reference-type="eqref" reference="eq:point-tail"}; summation gives [\[eq:summed-tail\]](#eq:summed-tail){reference-type="eqref" reference="eq:summed-tail"}. Notice that the exact count is $\lfloor X/p^2\rfloor$, so no $\pi(\sqrt X)$ or $X^{-1/2}$ loss appears. Divide the identical inequalities by $X$ and take limits along any fixed periodic phase selection to obtain the last assertion.

For a $Q$-periodic complex function $w$, use the normalized transform $$\widehat w(a)=\frac1Q\sum_{r\bmod Q}w(r)\mathrm e^{-2\pi i ar/Q}.
 \label{eq:dft}$$

[\[lem:fourier\]]{#lem:fourier label="lem:fourier"} Let $$D(X)=\sup_{\alpha\in\mathbb R}
       \lvert\sum_{n\le X}\mu(n)\mathrm e^{2\pi i\alpha n}\rvert.$$ If $w$ has period $Q$, then $$\lvert\sum_{n\le X}w(n)\mu(n)\rvert
 \le\sqrt Q\lVert w\rVert_\infty D(X).
 \label{eq:fourier-bound}$$

Fourier inversion and the definition of $D(X)$ give the right side with $\sum_a\lvert\widehat w(a)\rvert$ in place of $\sqrt Q\lVert w\rVert_\infty$. Parseval and Cauchy--Schwarz give $$\sum_a\lvert\widehat w(a)\rvert
 \le\sqrt Q\left(\sum_a\lvert\widehat w(a)\rvert^2\right)^{1/2}
 =\sqrt Q\left(\frac1Q\sum_r\lvert w(r)\rvert^2\right)^{1/2}
 \le\sqrt Q\lVert w\rVert_\infty.$$ The sup norm is essential. For $P=2$, $q=1$, and the legal $c_{21}=-2$ witness, one period of the relevant shifted mask is $(-2,-2,0,-2)$. Its normalized Fourier $\ell^1$ norm is $3$, which is larger than $\sqrt4=2$ but no larger than $2\sqrt4$.

# The uniform analytic ledger

For $N\ge3$, set $$D_*(N)=\max_{X\in\{N,N-2\}}D(X),
 \qquad Q=\operatorname{lcm}(q,M_P).
 \label{eq:D-star}$$ Every coefficient sequence $c_{ij}(n\bmod q)$ and every cutoff mask in the proof is $Q$-periodic. Again, $Q$ is only asserted to be a common period.

[\[prop:ledger\]]{#prop:ledger label="prop:ledger"} For every $N\ge3$, $P\ge2$, $q\ge1$, and $f\in\mathcal F_q$, $$\boxed{
 \lvert S_N(q,f)-L_q(f)\rvert
 \le\frac{4\sqrt QD_*(N)}N+13\tau_P+\frac{6Q}N+\frac4N.}
 \label{eq:master-bound}$$

Insert [\[eq:interpolation\]](#eq:interpolation){reference-type="eqref" reference="eq:interpolation"} into [\[eq:finite-score\]](#eq:finite-score){reference-type="eqref" reference="eq:finite-score"}. The $c_{11}$ channel is absent phase by phase. We account for the remaining five channels separately.

The $c_{01}$ channel is a $Q$-periodic weight of sup norm one against $\mu(n)$. Lemma [\[lem:fourier\]](#lem:fourier){reference-type="ref" reference="lem:fourier"} bounds it by $\sqrt QD(N)/N$.

For $c_{12}$, the first two sites vanish and the change of variables $m=n-2$ gives $$\sum_{m\le N-2}c_{12}(m+2)\mu(m)\mu(m+2)^2.$$ Replace $\mu(m+2)^2$ by $\eta_P(m+2)$. The cost is at most $N\tau_P$ by Lemma [\[lem:tail\]](#lem:tail){reference-type="ref" reference="lem:tail"}. The remaining periodic weight has sup norm one, so its Fourier cost is $\sqrt QD(N-2)$.

For $c_{21}$, replace $\mu(n-2)^2$ by $\eta_P(n-2)$ for $n\ge3$. The coefficient bound $\lvert c_{21}\rvert\le2$ makes the tail cost $2N\tau_P$. Extend the periodic Möbius sum to $1\le n\le N$. At $n=2$, $\eta_P(0)=0$; at $n=1$, the cutoff has $\eta_P(-1)=1$ whereas $\mu_0(-1)=0$, costing at most two. The periodic weight has sup norm two. This channel therefore contributes $$2\sqrt QD(N)+2N\tau_P+2.$$ The three Fourier costs are thus $1+1+2=4$.

It remains to compare the two square-only channels with [\[eq:fixed-limit\]](#eq:fixed-limit){reference-type="eqref" reference="eq:fixed-limit"}. For a bounded $Q$-periodic sequence $a$, complete periods plus the final incomplete block give $$\lvert\frac 1N\sum_{n\le N}a(n)-\frac 1Q\sum_{r\bmod Q}a(r)\rvert
 \le\frac{2Q\lVert a\rVert_\infty}{N}.
 \label{eq:period-discrepancy}$$ For $c_{02}\mu(n)^2$, finite-to-cutoff and limit-to-cutoff each cost $\tau_P$, while [\[eq:period-discrepancy\]](#eq:period-discrepancy){reference-type="eqref" reference="eq:period-discrepancy"} costs $2Q/N$. Its total is $$2\tau_P+2Q/N.
 \label{eq:c02-cost}$$

For $c_{22}\mu_0(n-2)^2\mu(n)^2$, the product difference is bounded by the sum of the two one-site differences. Since $\lvert c_{22}\rvert\le2$, finite-to-cutoff costs $4\tau_P$ and limit-to-cutoff costs another $4\tau_P$. The cutoff product has sup norm two, so [\[eq:period-discrepancy\]](#eq:period-discrepancy){reference-type="eqref" reference="eq:period-discrepancy"} costs $4Q/N$. Extending the cutoff product across the padded sites costs two at $n=1$ and zero at $n=2$ by [\[eq:eta-endpoints\]](#eq:eta-endpoints){reference-type="eqref" reference="eq:eta-endpoints"}. This channel contributes $$8\tau_P+4Q/N+2/N.
 \label{eq:c22-cost}$$

Collecting the tail coefficients gives $$\underbrace{1+2}_{\text{Fourier masks}}
 +\underbrace{2}_{c_{02}}
 +\underbrace{8}_{c_{22}}=13.$$ The periodic discrepancies give $2+4=6$, and the two endpoint costs give $2+2=4$. After division by $N$, this is [\[eq:master-bound\]](#eq:master-bound){reference-type="eqref" reference="eq:master-bound"}.

The decomposition also explains the tail constant in a second way. The finite mask replacements cost $1+1+2+4=8$ across the $c_{12},c_{02},c_{21},c_{22}$ channels, and the two limiting square means cost $1+4=5$. These are conservative uniform costs; no sign cancellation between channels is used.

# Polylogarithmic-clock uniformization

All logarithms in the clock budget are natural. For fixed $B>0$, put $$H_B(N)=\left\lfloor(\log N)^B\right\rfloor.
 \label{eq:clock-budget}$$ All suprema and maxima using this budget are understood for sufficiently large $N$, when $H_B(N)\ge1$.

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} For every fixed real $B>0$, $$\boxed{
 \sup_{1\le q\le H_B(N)}\ \sup_{f\in\mathcal F_q}
       \lvert S_N(q,f)-L_q(f)\rvert\longrightarrow0.}
 \label{eq:uniform-limit}$$

Take $$P=P_N=\left\lfloor\sqrt{\log\log N}\right\rfloor,
 \label{eq:P-choice}$$ which is at least two for all sufficiently large $N$. The elementary estimate $$\log M_P=2\sum_{p\le P}\log p\le2P\log P=o(\log\log N)
 \label{eq:M-growth}$$ shows $M_P=(\log N)^{o(1)}$. Uniformly for $q\le H_B(N)$, $$Q\le qM_P\le(\log N)^{B+o(1)}.
 \label{eq:Q-growth}$$

RH-366 freezes Davenport's estimate: for every fixed $A>0$, $$\sup_{\alpha\in\mathbb R}
 \lvert\sum_{n\le X}\mu(n)\mathrm e^{2\pi i\alpha n}\rvert
 \ll_A X(\log X)^{-A}.
 \label{eq:davenport}$$ Choose one fixed $A>B/2$. Equations [\[eq:Q-growth\]](#eq:Q-growth){reference-type="eqref" reference="eq:Q-growth"} and [\[eq:davenport\]](#eq:davenport){reference-type="eqref" reference="eq:davenport"} make the Fourier term in [\[eq:master-bound\]](#eq:master-bound){reference-type="eqref" reference="eq:master-bound"} $$\ll_A(\log N)^{B/2-A+o(1)}=o(1).$$ Also $$\tau_P\le\sum_{n>P}n^{-2}\le\frac1{P-1}\longrightarrow0,
 \qquad Q/N\longrightarrow0,
 \qquad 1/N\longrightarrow0.$$ The right side of [\[eq:master-bound\]](#eq:master-bound){reference-type="eqref" reference="eq:master-bound"} is independent of $f$ and otherwise depends on $q$ only through the displayed uniform bound for $Q$. This proves [\[eq:uniform-limit\]](#eq:uniform-limit){reference-type="eqref" reference="eq:uniform-limit"}.

The fixed nature of $B$ is load-bearing. The proof does not supply a constant uniform in a varying $B=B(N)$. For $q=N^\varepsilon$, the $\sqrt Q$ Fourier mass is polynomial, while [\[eq:davenport\]](#eq:davenport){reference-type="eqref" reference="eq:davenport"} supplies only an arbitrarily fixed logarithmic saving; this route therefore stops before polynomial clocks.

# Triangular optimizers and a diagonal witness

Because every $\mathcal F_q$ is finite, define $$G_N(q)=\max_{f\in\mathcal F_q}\lvert S_N(q,f)\rvert,
 \qquad
 G(q)=\max_{f\in\mathcal F_q}\lvert L_q(f)\rvert.
 \label{eq:optimizers}$$ The second quantity is exactly the RH-379 fixed-clock optimizer.

[\[cor:optimizer-transfer\]]{#cor:optimizer-transfer label="cor:optimizer-transfer"} For every fixed $B>0$, $$\sup_{1\le q\le H_B(N)}\lvert G_N(q)-G(q)\rvert\longrightarrow0.
 \label{eq:optimizer-uniform}$$

For any two finite families of real numbers $(a_f)$ and $(b_f)$, $$\lvert\max_f\lvert a_f\rvert-\max_f\lvert b_f\rvert\rvert
 \le\max_f\lvert a_f-b_f\rvert.$$ Apply this at each $q$ and then Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"}.

[\[thm:triangular-endpoint\]]{#thm:triangular-endpoint label="thm:triangular-endpoint"} For every fixed $B>0$, $$\boxed{\displaystyle
          \max_{1\le q\le H_B(N)}G_N(q)\longrightarrow B_\infty.}
 \label{eq:triangular-endpoint}$$

Equation [\[eq:rh379-supremum\]](#eq:rh379-supremum){reference-type="eqref" reference="eq:rh379-supremum"} gives $G(q)\le B_\infty$ for every fixed $q$. Conversely, for every $\varepsilon>0$ there is one fixed clock $q_\varepsilon$ with $G(q_\varepsilon)>B_\infty-\varepsilon$. Since $H_B(N)\to\infty$, that clock is eventually admissible. Hence $$\max_{q\le H_B(N)}G(q)\longrightarrow B_\infty.$$ Corollary [\[cor:optimizer-transfer\]](#cor:optimizer-transfer){reference-type="ref" reference="cor:optimizer-transfer"} transfers this scalar maximum to $G_N$.

There is also an explicit cofinal witness, with a necessary empty-set convention. Let $3=p_1<p_2<\cdots$ be the odd primes and set $$q_y=4\prod_{i\le y}p_i^2.
 \label{eq:square-clocks}$$ When $H_B(N)<q_1=36$, record `no_square_clock_available`; do not silently substitute $q_1$. Once the set is nonempty, define $$y_B(N)=\max\{y\ge1:q_y\le H_B(N)\}.
 \label{eq:y-diagonal}$$ For each $y$, choose the RH-379 positive optimizer $f_y^+\in\mathcal F_{q_y}$ with $L_{q_y}(f_y^+)=G(q_y)>0$.

[\[cor:diagonal\]]{#cor:diagonal label="cor:diagonal"} After [\[eq:y-diagonal\]](#eq:y-diagonal){reference-type="eqref" reference="eq:y-diagonal"} becomes defined, $$S_N\bigl(q_{y_B(N)},f_{y_B(N)}^+\bigr)\longrightarrow B_\infty.
 \label{eq:diagonal-limit}$$

For every fixed $y$, eventually $q_y\le H_B(N)$; hence $y_B(N)\to\infty$. RH-379 proves $G(q_y)\to B_\infty$. Therefore $$\begin{aligned}
 \lvert S_N(q_{y_B},f_{y_B}^+)-B_\infty\rvert
 &\le\sup_{q\le H_B(N),\ f\in\mathcal F_q}\lvert S_N(q,f)-L_q(f)\rvert\\
 &\quad+\lvert G(q_{y_B})-B_\infty\rvert\longrightarrow0.\end{aligned}$$

The families $f_{y_B(N)}^+$ form a triangular-array witness only. No projective compatibility across clocks, and no single infinite selector, is asserted.

# Finite certificate, source lock, and reproducibility

The standard-library artifact reproduces the finite interfaces used above. It contains all $512$ truth rows and all $4608$ interpolation evaluations; the $192$ zero-$c_{11}$ rows reduce to $24$ coefficient vectors of multiplicity eight. It checks maximum coefficient-vector $\ell^1$ norm $3$, maximum squared $\ell^2$ norm $5$, the self-compatible $c_{21}=-2$ witness, and the three normalized-DFT channel costs $1,1,2$.

The cutoff rows have exact periods $$4,\quad36,\quad900,\quad44100$$ for $P=2,3,5,7$. Coprime and noncoprime least-common-multiple fixtures are included. One additional fixture has $q=5$, $P=3$, and $Q=180$, while its relevant mask has minimal period $36$; this prevents the valid common period from being promoted to a minimal-period claim. Exact square-mask means, the $13=8+5$ tail split, the $4$ endpoint cost, and small-clock finite max-plus rows are regenerated from source.

The certificate is explicitly labelled `reproduction_not_analytic_proof`. Its finite rows do not prove Davenport's theorem, a uniform asymptotic, or any limit in this paper. A closed official Draft 2020--12 schema fixes every nested member and exact JSON primitive type. Twenty-four nontrivial certificate mutations test coefficient, period, shift, factor-two, square-mean, tail, padding, clock, sentinel, and claim-boundary failures. Separate tests mutate source-lock commits and group digests. Optimized Python mode and bool-for-int substitutions are also tested.

The source lock contains $67$ unique files in groups $51/8/8$: the released RH-384 immutable closure, the standard eight RH-384 theorem files, and the standard eight RH-366 Davenport files. Every live file is compared with its Git release blob. Mutable root policy and handoff files are excluded. The RH-366 release is `0396fab97bbe3348c8237f8734dec0e1893fd3bf`. Its frozen `main.tex` SHA-256 is

7df165bd63d43f52dc217dea6691d231d8e40c00c148ab7e1aa4abcac55060fb

The RH-379 release is `9ae9802ed17529ef4adfb81d7e2158d47c3c8d22`. Its frozen `main.tex` SHA-256 is

c5d97a227398a4f1d46a39fdec73ffb86aeb9bfc0f16296be7023b187b497090

# Context, limitations, and Gates

The cubic residual limits recorded in RH-384 are useful context, but they are not the discovery claim here [@RH384]. The new theorem is the restricted growing-clock uniformization in Theorem [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"}.

Route A is `GO`. Proposition [\[prop:ledger\]](#prop:ledger){reference-type="ref" reference="prop:ledger"}, the fixed-$B$ cutoff, optimizer transfer, endpoint theorem, and diagonal witness form a closed theorem chain. Route B is `STOP_SCOPED`. The proof gives no polynomial-clock uniformity: a fixed logarithmic Davenport saving does not pay polynomial Fourier mass. If $c_{11}(r)$ is activated, already $q=1$ exposes the ordinary shift-two Chowla sum, which the frozen sources do not cancel.

The following boundaries are mandatory.

1.  $B>0$ is fixed before $N\to\infty$; no $B=B(N)$ theorem is proved.

2.  No effective finite threshold or rate is claimed. Constants in Davenport's estimate depend on the chosen fixed exponent.

3.  The maximum in [\[eq:triangular-endpoint\]](#eq:triangular-endpoint){reference-type="eqref" reference="eq:triangular-endpoint"} is restricted to $q\le H_B(N)$; it is not $\sup_{q<\infty}G_N(q)$.

4.  The theorem optimizes periodic phase tables, not arbitrary adaptive sign words. It supplies no upper bound proving a limit for $K_N/N$.

5.  The diagonal witness is not a projectively compatible infinite selector.

Gates A--E remain false/open. These externally prescribed arithmetic tables do not construct a canonical intrinsic dynamical spectral determinant, time-oriented scattering completion, self-adjoint generator with an intrinsic $T\log T$ law, signed von-Mangoldt weighted prime-power trace, or completed-zeta divisor equality. Nothing here identifies Riemann zeros, constructs a Hilbert--Pólya operator, or proves the Riemann hypothesis.

# Conclusion

The fixed-clock RH-379 limit is uniform throughout every fixed polylogarithmic clock window. The proof pays every source of growth: four units of Fourier mass, thirteen units of squarefree-tail loss, six units of period discrepancy, and four zero-padding endpoints. The cutoff period is small enough to fit inside Davenport's logarithmic saving precisely because $B$ is fixed. This establishes a genuine, restricted growing-clock theorem while leaving polynomial clocks, active shift-two correlations, adaptive capacity, and all spectral Gates open.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

**Data availability.** All source code, exact outputs, tests, closed schema, source hashes, and archive-verification files are included in the RH-385 repository directory. No new external dataset was created or analyzed. Finite certificate rows reproduce interfaces and are not the analytic proof.

**Ethics.** This mathematical study uses no human participants, animals, personal data, or biological materials. Ethics approval was not required.

**Author contributions.** The RH research program performed conceptualization, methodology, formal analysis, software, validation, and writing---original draft and review/editing.

**Funding.** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Declaration of interests.** The authors declare no known competing financial interests or personal relationships that could have influenced the work reported here.

**AI-assisted workflow.** The manuscript and executable checks were prepared with AI-assisted academic writing and coding tools under the repository's documented multi-agent workflow. The mathematical claims are bounded by frozen sources, explicit proofs, independent audits, and reproducible artifacts. The authors retain responsibility for the final content and its integrity.
