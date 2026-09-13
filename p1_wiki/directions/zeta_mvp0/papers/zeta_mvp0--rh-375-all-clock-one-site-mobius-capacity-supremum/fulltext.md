---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-375-all-clock-one-site-mobius-capacity-supremum"
canonical_tex: "zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum/main.pdf"
source_sha256: "7d96987b0236d2788a781565bc03195c59ad2b72d07f1ff8988f8a3fef4a5117"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The all-clock supremum for universally safe one-site Möbius capacity factors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-375-all-clock-one-site-mobius-capacity-supremum/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every fixed finite clock $q$, we optimize all phase/current-input sign factors that satisfy the RH-366 distance-two constraint for every possible ternary input word. Their limiting Möbius correlation exists, and its maximum absolute value is the squarefree-density weighted independent-set value $$F(q)=\max_{I\cap(I+2)=\varnothing}\sum_{r\in I}\delta_{q,r}.$$ The clock need not be a minimal period. Consequently $q\mid Q$ implies $F(q)\le F(Q)$. We then prove a special saturation law for the RH-374 square clocks $q_y=4\prod_{i\le y}p_i^2$: if $q_y\mid Q$ and $Q$ has the same prime support, then $F(Q)=F(q_y)=B_y$. The proof uses zero phases forced by $4$ and $9$ to split the two parity cycles; it is not a general cyclic-cover MWIS law. Lifting an arbitrary finite clock to such a same-support multiple gives $$\sup_{q<\infty}F(q)=B_\infty,
               \qquad F(q)<B_\infty\quad(q<\infty).$$ Thus the RH-374 Euler-product floor is exactly the nonattained all-clock supremum in this one-site class. Memory-dependent observables, growing clocks, infinite selectors, adaptive-capacity convergence, intrinsic operators, traces, Riemann-zero identification, and RH remain outside scope.
author:
- RH research program
bibliography:
- references.bib
date: August 2026
title: 'The all-clock supremum for universally safe one-site Möbius capacity factors'
```

## Markdown 正文

# Frozen capacity and factor class

The RH-366 distance-two capacity is $$K_N=\max_{\substack{\varepsilon_1,\ldots,\varepsilon_N\in\{-1,+1\}\\
 \text{not }(\varepsilon_n,\varepsilon_{n+2})=(+1,+1)}}
 \left|\sum_{n\le N}\mu(n)\varepsilon_n\right|.
 \label{eq:capacity}$$ Its optimizer may read the entire finite prefix and may change with $N$. RH-366 proves the bracket $$\frac4{\pi^2}\le\liminf_{N\to\infty}\frac{K_N}{N}
 \le\limsup_{N\to\infty}\frac{K_N}{N}\le\frac6{\pi^2},
 \label{eq:capacity-bracket}$$ but not convergence [@RH366]. RH-371 gives an exact eight-run formula for every prefix while leaving the required Möbius run envelope open [@RH371]. RH-373 and RH-374 instead construct prescribed one-site certificates, culminating in a strictly increasing square-clock family $B_y\uparrow B_\infty$ [@RH373; @RH374].

Fix $q\ge1$. A $q$-periodic one-site phase/current-input factor is a family $$g_r:\{-1,0,+1\}\longrightarrow\{-1,+1\},
       \qquad r\in\mathbb Z/q\mathbb Z.$$ The declared period need not be minimal. For a ternary word $(a_n)$, its output is $g_{n\bmod q}(a_n)$. The factor is *universally safe* if this output never has two $+1$ values at distance two, for every ternary input word. Its active set is $$S_g=\{r:g_r(a)=+1\text{ for at least one }a\in\{-1,0,+1\}\}.$$

Universal safety is equivalent to $$S_g\cap(S_g+2)=\varnothing.
 \label{eq:active-independent}$$ Indeed, two active phases at distance two can be activated independently; the converse is immediate. This retains loops: for $q=1$ and $q=2$, addition by two fixes every phase, so only the empty active set is safe. The class is the one-site boundary isolated in RH-372, not the class of all finite-memory transducers [@RH372].

# Exact optimization at one clock

For $r\pmod q$, let $$\delta_{q,r}=\lim_{N\to\infty}\frac1N
 \#\{n\le N:n\equiv r\pmod q,\ \mu(n)^2=1\}.
 \label{eq:density}$$ The squarefree progression sieve gives this limit. If $q=\prod_{p\mid q}p^{a_p}$, its useful exact local form is $$\pi^2\delta_{q,r}=
 \begin{cases}
 0,&p^2\mid r\text{ for some }p\text{ with }a_p\ge2,\\[2mm]
 \displaystyle\frac6q
 \prod_{p\mid q}(1-p^{-2})^{-1}
 \prod_{\substack{p\parallel q\\p\mid r}}(1-p^{-1}),&\text{otherwise}.
 \end{cases}
 \label{eq:local-density}$$ The second product accounts for a modulus containing only one power of $p$. It is an exact rational coefficient of $\pi^{-2}$ [@Mirsky1948].

For fixed $q$, Davenport cancellation and finite Fourier inversion give $$\sum_{\substack{n\le N\\n\equiv r\ (q)}}\mu(n)=o(N).$$ Splitting the squarefree entries by sign therefore proves, for every one-site factor, $$L_q(g):=\lim_{N\to\infty}\frac1N\sum_{n\le N}
 \mu(n)g_{n\bmod q}(\mu(n))
 =\frac12\sum_{r\bmod q}\delta_{q,r}
       \bigl(g_r(+1)-g_r(-1)\bigr).
 \label{eq:factor-limit}$$ This is the fixed-clock formula proved in the RH-372 certificate layer [@Davenport1937; @RH372].

Let $$F(q)=\max_g |L_q(g)|,$$ where the maximum is over all universally safe $q$-periodic one-site factors.

For every finite $q$, $$\boxed{\displaystyle
 F(q)=\max_{\substack{I\subset\mathbb Z/q\mathbb Z\\I\cap(I+2)=\varnothing}}
                  \sum_{r\in I}\delta_{q,r}.}
 \label{eq:F-MWIS}$$ Both correlation orientations attain the value. In particular, $F(1)=F(2)=0$.

Put $c_r=(g_r(+1)-g_r(-1))/2\in\{-1,0,+1\}$. Whenever $c_r\ne0$, phase $r$ is active, so the support of $(c_r)$ is contained in the independent set $S_g$. Equation [\[eq:factor-limit\]](#eq:factor-limit){reference-type="eqref" reference="eq:factor-limit"} gives $$|L_q(g)|\le\sum_{r:c_r\ne0}\delta_{q,r}
 \le\max_{I\cap(I+2)=\varnothing}\sum_{r\in I}\delta_{q,r}.$$ Conversely, for an independent set $I$, set $$g_r(+1)=+1,\qquad g_r(0)=g_r(-1)=-1\quad(r\in I),
 \qquad g_r\equiv-1\quad(r\notin I).$$ This universally safe factor has $L_q(g)=\sum_{r\in I}\delta_{q,r}$. Reversing the roles of $+1$ and $-1$ on $I$ realizes the negative orientation. The self-loops at $q=1,2$ force $I=\varnothing$.

For odd $q>1$, addition by two is one $q$-cycle; for even $q>2$, it is two cycles of length $q/2$. Thus [\[eq:F-MWIS\]](#eq:F-MWIS){reference-type="eqref" reference="eq:F-MWIS"} includes odd clocks rather than silently reducing to the two-parity case used by the square family.

The value $g_r(0)$ contributes nothing to [\[eq:factor-limit\]](#eq:factor-limit){reference-type="eqref" reference="eq:factor-limit"}; changing an unnecessary $+1$ there to $-1$ can only remove a safety constraint. Likewise, an active zero-density phase can be made inactive without changing the objective. These observations do not delete positive-weight phases and do not enlarge the theorem beyond one-site factors.

# Divisibility monotonicity

If $q\mid Q$, then for every $r\pmod q$, $$\delta_{q,r}=\sum_{\substack{s\pmod Q\\s\equiv r\ (q)}}
                         \delta_{Q,s}.
 \label{eq:aggregation}$$

For every finite $N$, the squarefree integers in the class $r\pmod q$ are the disjoint union of the classes $s\pmod Q$ above it. Divide by $N$ and take the finitely many limits.

[\[prop:clock-divisibility\]]{#prop:clock-divisibility label="prop:clock-divisibility"} If $q\mid Q$, then $$F(q)\le F(Q).
 \label{eq:monotonicity}$$

View a $q$-periodic factor as the $Q$-periodic factor $\widetilde g_s=g_{s\bmod q}$. This is why minimal period was not required. Condition [\[eq:active-independent\]](#eq:active-independent){reference-type="eqref" reference="eq:active-independent"} shows that universal safety is preserved. The two factors produce the same output word, hence the same limit; equivalently, this follows by inserting [\[eq:aggregation\]](#eq:aggregation){reference-type="eqref" reference="eq:aggregation"} into [\[eq:factor-limit\]](#eq:factor-limit){reference-type="eqref" reference="eq:factor-limit"}. Maximizing gives [\[eq:monotonicity\]](#eq:monotonicity){reference-type="eqref" reference="eq:monotonicity"}.

# Special square-clock saturation

Let $3=p_1<p_2<\cdots$ be the odd primes and recall the RH-374 quantities $$P_y=\prod_{i\le y}p_i^2,\qquad q_y=4P_y,\qquad
 A_y=\prod_{i\le y}(p_i^2-1).
 \label{eq:square-clock}$$ On the odd phase cycle, let $O_y$ be the number of odd-length positive runs in one period of the word $$w_y(k)=\mathbf1_{\{p_i^2\nmid2k+1\ \text{for all }i\le y\}}.$$ RH-374 proves $$F(q_y)=B_y=\frac{4+2O_y/A_y}{\pi^2},
 \label{eq:B-y}$$ and proves $B_y$ strictly increasing. With $$e_m=\prod_{p\ \mathrm{odd}}(1-m/p^2),\qquad e_9=0,$$ its limit is $$B_\infty=\frac{4+2C}{\pi^2},\qquad
 C=\frac1{e_1}\sum_{j\in\{1,3,5,7\}}
       (e_j-2e_{j+1}+e_{j+2}).
 \label{eq:B-infinity}$$

[\[prop:saturation\]]{#prop:saturation label="prop:saturation"} Suppose $q_y\mid Q$ and $Q$ has exactly the same prime divisors as $q_y$. Write $Q=Rq_y$. Then $$\boxed{F(Q)=F(q_y)=B_y.}
 \label{eq:saturation}$$

Because every prime in the support occurs to exponent at least two, a phase $s\pmod Q$ has positive squarefree density precisely when no supported prime square divides $s$. All positive phases have the same weight. By [\[eq:local-density\]](#eq:local-density){reference-type="eqref" reference="eq:local-density"}, it is $1/R$ times the positive $q_y$ weight, hence $$\delta_{Q,s}=\frac{2}{RA_y\pi^2}.
 \label{eq:Q-unit}$$

It remains to count the largest independent subset of the positive support. The distance-two graph has one even and one odd phase cycle. On the even cycle, every phase divisible by $4$ has zero weight; these zero phases split the support, and all $RA_y$ positive even phases may be selected. On the odd cycle, the support is $R$ repetitions of the $q_y$ support. The factor $p_1^2=9$ inserts a zero every nine successive odd-cycle sites, so all positive runs have length at most eight and the repetitions do not join across a hidden all-positive seam. The RH-374 run count therefore repeats literally: its odd-cycle MWIS cardinality is $R(A_y+O_y)$. The total support MWIS cardinality is $$R(2A_y+O_y).
 \label{eq:scaled-count}$$ Multiplying [\[eq:scaled-count\]](#eq:scaled-count){reference-type="eqref" reference="eq:scaled-count"} by [\[eq:Q-unit\]](#eq:Q-unit){reference-type="eqref" reference="eq:Q-unit"} gives $(4+2O_y/A_y)/\pi^2=B_y$.

An MWIS need not scale under an arbitrary cyclic cover. Proposition [\[prop:saturation\]](#prop:saturation){reference-type="ref" reference="prop:saturation"} uses the particular squarefree support: forced $4$-zero phases split the even component and forced $9$-zero phases split the odd component. No claim is made for a general weighted cyclic graph.

# The all-clock supremum {#sec:all-clock}

Over all finite clocks and universally safe one-site phase/current-input factors, $$\boxed{\displaystyle\sup_{q<\infty}F(q)=B_\infty.}
 \label{eq:all-clock}$$ The supremum is not attained: every fixed finite $q$ satisfies $$F(q)<B_\infty.
 \label{eq:nonattainment}$$

Fix an arbitrary finite $q$. Choose $y$ so that every odd prime divisor of $q$ occurs among $p_1,\ldots,p_y$; when $q$ has no odd prime divisor, take $y=1$. Put $$Q=\operatorname{lcm}(q,q_y).$$ Then $q\mid Q$, $q_y\mid Q$, and $Q$ has exactly the prime support of $q_y$: extra exponents in $q$, including high powers of $2$ or of an odd prime, only enlarge the multiplier $R=Q/q_y$. Propositions [\[prop:clock-divisibility\]](#prop:clock-divisibility){reference-type="ref" reference="prop:clock-divisibility"} and [\[prop:saturation\]](#prop:saturation){reference-type="ref" reference="prop:saturation"} give $$F(q)\le F(Q)=B_y<B_\infty,$$ where the last inequality uses the strict RH-374 sequence. This proves the upper bound in [\[eq:all-clock\]](#eq:all-clock){reference-type="eqref" reference="eq:all-clock"} and the nonattainment statement. Conversely $F(q_y)=B_y$ for every $y$, so $\sup_qF(q)\ge\sup_yB_y=B_\infty$.

$$B_\infty\le
                  \liminf_{N\to\infty}\frac{K_N}{N}.
 \label{eq:capacity-floor}$$

Every universally safe factor supplies an admissible word in [\[eq:capacity\]](#eq:capacity){reference-type="eqref" reference="eq:capacity"}, so $F(q)\le\liminf K_N/N$ for each fixed $q$. Take the scalar supremum and apply [\[eq:all-clock\]](#eq:all-clock){reference-type="eqref" reference="eq:all-clock"}.

This recovers the RH-374 floor while adding an exact interpretation: it is the all-finite-clock supremum in the one-site class. It does not identify $B_\infty$ with an ordinary limit of $K_N/N$ and does not choose $q=q(N)$.

# Exact executable audit

The artifact evaluates [\[eq:local-density\]](#eq:local-density){reference-type="eqref" reference="eq:local-density"} with exact `Fraction` arithmetic and solves each addition-by-two cycle by a weighted path/cycle DP. It retains self-loops and handles odd clocks, high $2$-adic exponents, high odd-prime exponents, zero weights, and both factor orientations. Its independent finite checks are:

-   all $8^q$ factor tables for $1\le q\le4$: $4680$ total tables and $249$ universally safe tables;

-   all phase subsets for $1\le q\le10$: $2046$ subsets, with every exact optimum agreeing with the cycle DP;

-   eight divisibility pairs, checking every density aggregation row, the lifted independent set, and $F(q)\le F(Q)$;

-   ten cofinal lifts, including $q=16,27,125,343$ and the largest audited lift $343\mid308700$;

-   the RH-374 square rows $$\pi^2F(36)=4,\qquad \pi^2F(900)=\frac{49}{12},\qquad
       \pi^2F(44100)=\frac{593}{144}.$$

Representative lift rows are

    $q$      $Q$   $R$   $\pi^2F(q)$   $\pi^2F(Q)$
  ----- -------- ----- ------------- -------------
      3       36     1         $9/4$           $4$
      8       72     2           $4$           $4$
     27      108     3           $3$           $4$
    125     4500     5           $3$       $49/12$
    343   308700     7           $3$     $593/144$

A bounded reproduction scan over all $1\le q\le256$ has record clocks $1,3,4,180$ and maximum $\pi^2F(q)=97/24$ at $q=180$. This finite scan is not evidence for [\[eq:all-clock\]](#eq:all-clock){reference-type="eqref" reference="eq:all-clock"}; the theorem is the cofinal argument in Section [5](#sec:all-clock){reference-type="ref" reference="sec:all-clock"}. The result ledger locks twenty-one repository inputs. The ARS integrity audit is repository-locked: it checks claim/source alignment, artifact provenance, and all seven research failure modes, but makes no fresh external bibliographic-verification claim.

# Route verdict and Gate ledger

Route A is `GO`: equations [\[eq:F-MWIS\]](#eq:F-MWIS){reference-type="eqref" reference="eq:F-MWIS"}, [\[eq:monotonicity\]](#eq:monotonicity){reference-type="eqref" reference="eq:monotonicity"}, [\[eq:saturation\]](#eq:saturation){reference-type="eqref" reference="eq:saturation"}, and [\[eq:all-clock\]](#eq:all-clock){reference-type="eqref" reference="eq:all-clock"} form a standalone exact theorem chain. Route B is `STOP_SCOPED`. The class excludes memory-dependent observations; no higher-order Möbius correlation theorem is supplied. There is no $q(N)$, infinite selector, or Davenport estimate uniform in the clock, and the adaptive capacity limit remains open.

Gates A--E remain false/open. These factors are externally prescribed arithmetic certificates, not intrinsic dynamical operators. This paper does not construct a Fredholm or spectral determinant, a time-oriented unitary completion, a self-adjoint generator, a von-Mangoldt prime-power trace, or a completed-zeta divisor equality. It does not identify Riemann zeros, construct a Hilbert--Polya operator, or prove the Riemann Hypothesis.

# Conclusion

The finite-clock one-site question has an exact endpoint: the RH-374 Euler-product constant is its supremum, approached by square clocks and attained by no finite clock. The remaining RH-366 problem is genuinely different. It requires control of adaptive or memory-dependent arithmetic structure; another bounded scan or an unproved growing-clock exchange cannot supply that control.
