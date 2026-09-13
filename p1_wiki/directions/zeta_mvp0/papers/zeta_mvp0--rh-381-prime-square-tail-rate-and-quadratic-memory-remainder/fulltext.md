---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-381-prime-square-tail-rate-and-quadratic-memory-remainder"
canonical_tex: "zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder/main.pdf"
source_sha256: "b1025502880530602f134ea5bdc6dcde34e2cdfd18fb364cb104343d456b643a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Prime-Square Tail Rate and a Quadratic Memory Remainder for Phasewise Chowla-Free Memory

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-381-prime-square-tail-rate-and-quadratic-memory-remainder/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Within the fixed finite-clock, universally distance-two-safe phasewise lag-two class whose interpolation coefficient $c_{11}(r)$ vanishes at every phase, RH-379 identifies an all-clock supremum $B_\infty$ and RH-380 proves that the square-clock values $G(q_y)$ increase strictly to it. We determine the first-order rate of that convergence. Put $$a_{j+1}=\frac1{p_{j+1}^2-1},\qquad
   T_y=\sum_{j\ge y}a_{j+1},$$ where $3=p_1<p_2<\cdots$ are the odd primes, and let $$e_m=\prod_{p\ \mathrm{odd}}\left(1-\frac m{p^2}\right),\qquad
   X_\infty=\frac{2e_4-4e_5+6e_6-8e_7+10e_8}{e_1}.$$ The run formula gives $X_\infty\ge6e_8/e_1>0$. A factorwise Euler-tail comparison proves $|X_j-X_\infty|\le170T_j$. The exact RH-379 product for $H_{j+1}$ gives $$0\le\frac4{\pi^2}-H_{j+1}
   \le\frac4{\pi^2}T_{j+1},$$ and the normalized memory statistic satisfies $0\le M_j/A_j\le1$. Telescoping the exact RH-380 increment and using two exact tail-sum identities yields, for every $y\ge1$, $$\left|B_\infty-G(q_y)-\frac{2X_\infty}{\pi^2}T_y\right|
   \le \frac{342}{\pi^2}T_y^2.$$ Consequently $$\frac{B_\infty-G(q_y)}{T_y}\longrightarrow
   \frac{2X_\infty}{\pi^2}>0.$$ No prime number theorem is used. The result supplies neither a second-order coefficient nor a $p_y$-scale asymptotic, growing-clock theorem, adaptive capacity limit, operator, trace formula, zero identification, or implication for the Riemann hypothesis.
author:
- RH research program
bibliography:
- references.bib
date: 'August 7, 2026'
title: |
  Prime-Square Tail Rate and a Quadratic Memory Remainder\
  for Phasewise Chowla-Free Memory
```

## Markdown 正文

**Keywords:** Möbius function; prime-square Euler tail; square clocks; quantitative convergence; lag-two memory.

# Frozen class and exact predecessor inputs

The theorem concerns exactly the class isolated in RH-379 and retained in RH-380 [@RH379; @RH380]. We begin by fixing its quantifiers.

Fix an integer $q\ge1$ before taking $N\to\infty$. For every $r\in\mathbb Z/q\mathbb Z$, choose a table $$f_r:\{-1,0,1\}^2\longrightarrow\{-1,+1\},\qquad
 \epsilon_n=f_{n\bmod q}\bigl(\mu(n-2),\mu(n)\bigr).$$ The family is universally distance-two-safe if no ternary input can give $\epsilon_n=\epsilon_{n+2}=+1$. It is in the present class only when the coefficient $c_{11}(r)$ of $\mu(n-2)\mu(n)$ in the RH-379 interpolation is zero for every phase. The exact fixed-clock optimum is denoted by $G(q)$.

The phasewise condition is not cosmetic. If $c_{11}(r)\ne0$, the limiting expansion contains a phase-weighted shift-two Möbius correlation that is not controlled by the frozen sources. Nothing below averages or cancels those missing terms.

Let $3=p_1<p_2<\cdots$ be the odd primes and define the square-clock data $$P_y=\prod_{i\le y}p_i^2,\qquad q_y=4P_y,\qquad
 A_y=\prod_{i\le y}(p_i^2-1),\qquad
 D_y=\prod_{i\le y}(p_i^2-2).
 \label{eq:square-data}$$ RH-374 associates a cyclic odd squarefree-support word to $P_y$. Its positive runs have lengths at most eight; write $R_\ell^{(y)}$ for the number of runs of length $\ell$ [@RH374]. With $$E_m^{(y)}=\prod_{i\le y}\left(1-\frac m{p_i^2}\right),
 \label{eq:finite-euler}$$ the exact run formula is $$R_\ell^{(y)}=
 \begin{cases}
 P_y\bigl(E_\ell^{(y)}-2E_{\ell+1}^{(y)}+E_{\ell+2}^{(y)}\bigr),
      &1\le\ell\le7,\\
 P_yE_8^{(y)},&\ell=8.
 \end{cases}
 \label{eq:run-formula}$$ Set $$\begin{aligned}
 \mathcal E_y&=R_2^{(y)}+R_4^{(y)}+R_6^{(y)}+R_8^{(y)},
 &L_y&=2R_2^{(y)}+4R_4^{(y)}+6R_6^{(y)}+8R_8^{(y)},
 \label{eq:EL}\\
 M_y&=2R_3^{(y)}+4R_5^{(y)}+6R_7^{(y)}.
 \label{eq:M}\end{aligned}$$ RH-380 proves the exact increment $$\begin{aligned}
G(q_{j+1})-G(q_j)
={}&\frac{2(L_j-2\mathcal E_j)}{\pi^2A_j(p_{j+1}^2-1)}\\
&+\frac{M_j}{A_j(p_{j+1}^2-1)}
\left(\frac4{\pi^2}-H_{j+1}\right),
\end{aligned}
\label{eq:rh380-increment}$$ where $H_j=\kappa_2A_j/D_j$, and it records $$G(q_j)\longrightarrow B_\infty.
 \label{eq:G-limit}$$ The limit in [\[eq:G-limit\]](#eq:G-limit){reference-type="eqref" reference="eq:G-limit"} is the RH-379 all-clock supremum. It is a cofinal limit after the fixed-clock $N$-limits, not a growing choice $q=q(N)$.

# Prime-square tails and the normalized run statistic

For $j\ge1$, put $$a_{j+1}=\frac1{p_{j+1}^2-1},\qquad
 T_j=\sum_{k\ge j}a_{k+1}.
 \label{eq:T}$$ The notation deliberately keeps the successor index visible: the increment from $q_j$ to $q_{j+1}$ carries $a_{j+1}$.

For $1\le m\le8$, define $$e_m=\prod_{p\ \mathrm{odd}}\left(1-\frac m{p^2}\right),\qquad
 U_m^{(j)}=\frac{E_m^{(j)}}{E_1^{(j)}},\qquad
 u_m=\frac{e_m}{e_1}.
 \label{eq:ratios}$$ All factors in these products are positive. Their convergence and positivity follow elementarily from convergence of $\sum_{n\ge3}n^{-2}$. The RH-374 normalization is $e_1=8/\pi^2$ [@RH374].

Define $$X_j=\frac{L_j-2\mathcal E_j}{A_j},
 \qquad
 X_\infty=2u_4-4u_5+6u_6-8u_7+10u_8.
 \label{eq:X-def}$$ Equivalently, $$X_\infty=
 \frac{2e_4-4e_5+6e_6-8e_7+10e_8}{e_1}.$$

[\[lem:X-euler\]]{#lem:X-euler label="lem:X-euler"} For every $j\ge1$, $$X_j=2U_4^{(j)}-4U_5^{(j)}+6U_6^{(j)}
      -8U_7^{(j)}+10U_8^{(j)}.
 \label{eq:X-euler}$$ Moreover, $$X_\infty\ge\frac{6e_8}{e_1}>0.
 \label{eq:X-positive}$$

The run identity in RH-380 is $$L_j-2\mathcal E_j=2R_4^{(j)}+4R_6^{(j)}+6R_8^{(j)}.$$ Since $A_j=P_jE_1^{(j)}$, substituting [\[eq:run-formula\]](#eq:run-formula){reference-type="eqref" reference="eq:run-formula"} gives $$\begin{aligned}
X_j
&=2\frac{E_4^{(j)}-2E_5^{(j)}+E_6^{(j)}}{E_1^{(j)}}
 +4\frac{E_6^{(j)}-2E_7^{(j)}+E_8^{(j)}}{E_1^{(j)}}
 +6\frac{E_8^{(j)}}{E_1^{(j)}}\\
&=2U_4^{(j)}-4U_5^{(j)}+6U_6^{(j)}
 -8U_7^{(j)}+10U_8^{(j)}.\end{aligned}$$ Passing to convergent Euler products proves the formula for $X_\infty$. The two finite second differences in the first line are normalized run counts and hence nonnegative. Their limits remain nonnegative. Dropping them leaves $6e_8/e_1$, which is strictly positive.

[\[lem:X-bound\]]{#lem:X-bound label="lem:X-bound"} For every $j\ge1$, $$\boxed{|X_j-X_\infty|\le170T_j.}
 \label{eq:X-bound}$$

For $m\in\{4,5,6,7,8\}$, division of the Euler factors gives the exact tail identity $$\frac{u_m}{U_m^{(j)}}
 =\prod_{p>p_j}\frac{1-m/p^2}{1-1/p^2}
 =\prod_{p>p_j}\left(1-\frac{m-1}{p^2-1}\right).
 \label{eq:ratio-tail}$$ For numbers $0\le v_i\le1$, the elementary product union bound $0\le1-\prod_i(1-v_i)\le\sum_i v_i$ follows first for finite products and then by monotone passage to the limit. Also $0<U_m^{(j)}\le1$. Therefore $$0\le U_m^{(j)}-u_m
 \le (m-1)T_j.
 \label{eq:one-ratio-bound}$$ Apply the triangle inequality to [\[eq:X-euler\]](#eq:X-euler){reference-type="eqref" reference="eq:X-euler"}. The coefficient ledger is $$2\cdot3+4\cdot4+6\cdot5+8\cdot6+10\cdot7
 =6+16+30+48+70=170,$$ which proves [\[eq:X-bound\]](#eq:X-bound){reference-type="eqref" reference="eq:X-bound"}.

# The $H$ tail and the memory statistic

[\[lem:H-tail\]]{#lem:H-tail label="lem:H-tail"} For every $j\ge1$, $$\frac{H_{j+1}}{4/\pi^2}
 =\prod_{p>p_{j+1}}\left(1-\frac1{p^2-1}\right),
 \label{eq:H-product}$$ and hence $$0\le\frac4{\pi^2}-H_{j+1}
 \le\frac4{\pi^2}T_{j+1}.
 \label{eq:H-bound}$$

The exact RH-379 product is $H_j=\kappa_2A_j/D_j$, where $\kappa_2=\prod_p(1-2/p^2)$. Separating the prime $2$ and cancelling the finite odd-prime factors gives $$H_{j+1}=\frac12 E_1^{(j+1)}
 \prod_{p>p_{j+1}}\left(1-\frac2{p^2}\right).$$ Because $4/\pi^2=e_1/2$, division yields $$\frac{H_{j+1}}{4/\pi^2}
 =\prod_{p>p_{j+1}}
 \frac{1-2/p^2}{1-1/p^2}
 =\prod_{p>p_{j+1}}\left(1-\frac1{p^2-1}\right).$$ The same product union bound used in Lemma [\[lem:X-bound\]](#lem:X-bound){reference-type="ref" reference="lem:X-bound"} now gives [\[eq:H-bound\]](#eq:H-bound){reference-type="eqref" reference="eq:H-bound"}.

[\[lem:M-bound\]]{#lem:M-bound label="lem:M-bound"} For every $j\ge1$, $$0\le\frac{M_j}{A_j}\le1.
 \label{eq:M-bound}$$

Nonnegativity is immediate from [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"}. An odd run of length $\ell$ contributes $\ell-1\le\ell$ to $M_j$. Thus $M_j$ is at most the number of positive sites lying in odd runs, which is at most the total number of positive sites. The latter is exactly $P_jE_1^{(j)}=A_j$. This proves [\[eq:M-bound\]](#eq:M-bound){reference-type="eqref" reference="eq:M-bound"}.

The word "quadratic" in the title refers to the contribution of this memory statistic to the final $T_y^2$ remainder. It does not announce a quadratic coefficient expansion.

# Two exact tail-sum identities

[\[lem:tail-algebra\]]{#lem:tail-algebra label="lem:tail-algebra"} For every $y\ge1$, $$\begin{aligned}
 \sum_{j\ge y}a_{j+1}T_j
 &=\frac12\left(T_y^2+\sum_{j\ge y}a_{j+1}^2\right)
 \le T_y^2,
 \label{eq:tail-current}\\
 \sum_{j\ge y}a_{j+1}T_{j+1}
 &=\frac12\left(T_y^2-\sum_{j\ge y}a_{j+1}^2\right)
 \le\frac12T_y^2.
 \label{eq:tail-next}\end{aligned}$$

Since $T_{j+1}=T_j-a_{j+1}$, $$\begin{aligned}
 a_{j+1}T_j
 &=\frac12\bigl(T_j^2-T_{j+1}^2+a_{j+1}^2\bigr),\\
 a_{j+1}T_{j+1}
 &=\frac12\bigl(T_j^2-T_{j+1}^2-a_{j+1}^2\bigr).\end{aligned}$$ Sum these identities from $j=y$ to a finite endpoint and then let that endpoint tend to infinity. The tails tend to zero because $$0<T_y\le\sum_{n>p_y}\frac1{n^2-1}
 =\frac12\left(\frac1{p_y}+\frac1{p_y+1}\right)\longrightarrow0.
 \label{eq:T-zero}$$ Here positivity holds for every finite $y$ because there are infinitely many odd primes. Finally, $\sum a_{j+1}^2\le(\sum a_{j+1})^2=T_y^2$, which gives both displayed inequalities. No estimate for the distribution of primes is involved.

# First-order gap rate

[\[prop:infinite-sum\]]{#prop:infinite-sum label="prop:infinite-sum"} For every $y\ge1$, $$\begin{aligned}
B_\infty-G(q_y)
=\sum_{j\ge y}\biggl[
 &\frac{2X_j}{\pi^2}a_{j+1}\\
 &+\frac{M_j}{A_j}a_{j+1}
 \left(\frac4{\pi^2}-H_{j+1}\right)
\biggr].
\end{aligned}
\label{eq:infinite-sum}$$

For a finite $K>y$, telescope the exact RH-380 increment [\[eq:rh380-increment\]](#eq:rh380-increment){reference-type="eqref" reference="eq:rh380-increment"} from $j=y$ through $K-1$ and use $X_j=(L_j-2\mathcal E_j)/A_j$ and $a_{j+1}=(p_{j+1}^2-1)^{-1}$. Then let $K\to\infty$ and invoke the already proved cofinal limit [\[eq:G-limit\]](#eq:G-limit){reference-type="eqref" reference="eq:G-limit"}. This is a limit of finite telescoping identities after all fixed-clock $N$-limits have been taken; there is no exchange of an $N$-limit with a $j$-limit.

[\[thm:rate\]]{#thm:rate label="thm:rate"} For every $y\ge1$, $$\boxed{
 \left|B_\infty-G(q_y)-\frac{2X_\infty}{\pi^2}T_y\right|
 \le\frac{342}{\pi^2}T_y^2.}
 \label{eq:rate-bound}$$ Consequently, $$\boxed{
 \frac{B_\infty-G(q_y)}{T_y}
 \longrightarrow\frac{2X_\infty}{\pi^2}>0.}
 \label{eq:ratio-limit}$$

Subtract $(2X_\infty/\pi^2)T_y$ from [\[eq:infinite-sum\]](#eq:infinite-sum){reference-type="eqref" reference="eq:infinite-sum"}. Since $T_y=\sum_{j\ge y}a_{j+1}$, the first remainder is bounded using Lemma [\[lem:X-bound\]](#lem:X-bound){reference-type="ref" reference="lem:X-bound"} and [\[eq:tail-current\]](#eq:tail-current){reference-type="eqref" reference="eq:tail-current"}: $$\begin{aligned}
\left|\sum_{j\ge y}\frac{2(X_j-X_\infty)}{\pi^2}a_{j+1}\right|
&\le\frac{340}{\pi^2}\sum_{j\ge y}a_{j+1}T_j
\le\frac{340}{\pi^2}T_y^2.
\label{eq:X-remainder}\end{aligned}$$ The memory summand is nonnegative. Lemmas [\[lem:H-tail\]](#lem:H-tail){reference-type="ref" reference="lem:H-tail"} and [\[lem:M-bound\]](#lem:M-bound){reference-type="ref" reference="lem:M-bound"}, followed by [\[eq:tail-next\]](#eq:tail-next){reference-type="eqref" reference="eq:tail-next"}, give $$\begin{aligned}
0&\le\sum_{j\ge y}\frac{M_j}{A_j}a_{j+1}
 \left(\frac4{\pi^2}-H_{j+1}\right)\\
&\le\frac4{\pi^2}\sum_{j\ge y}a_{j+1}T_{j+1}
\le\frac2{\pi^2}T_y^2.
\label{eq:M-remainder}\end{aligned}$$ Adding [\[eq:X-remainder\]](#eq:X-remainder){reference-type="eqref" reference="eq:X-remainder"} and [\[eq:M-remainder\]](#eq:M-remainder){reference-type="eqref" reference="eq:M-remainder"} proves [\[eq:rate-bound\]](#eq:rate-bound){reference-type="eqref" reference="eq:rate-bound"}; the ledger is $340+2=342$.

For each finite $y$, $T_y>0$ by [\[eq:T-zero\]](#eq:T-zero){reference-type="eqref" reference="eq:T-zero"}. Divide [\[eq:rate-bound\]](#eq:rate-bound){reference-type="eqref" reference="eq:rate-bound"} by $T_y$, then use $T_y\to0$ from the same elementary integer-square comparison. Equation [\[eq:ratio-limit\]](#eq:ratio-limit){reference-type="eqref" reference="eq:ratio-limit"} follows, and its limit is positive by [\[eq:X-positive\]](#eq:X-positive){reference-type="eqref" reference="eq:X-positive"}.

The scale in Theorem [\[thm:rate\]](#thm:rate){reference-type="ref" reference="thm:rate"} is the intrinsic prime-square tail $T_y$. We never replace it by a function of $p_y$. The only tail comparison is [\[eq:T-zero\]](#eq:T-zero){reference-type="eqref" reference="eq:T-zero"}, obtained by telescoping the integer series $(n^2-1)^{-1}$. Thus the proof uses neither the prime number theorem nor a weaker prime-counting asymptotic.

# Exact artifact and finite diagnostics

The standard-library artifact has two distinct layers. First, exact `Fraction` arithmetic regenerates the run statistics, normalized Euler ratios, RH-380 increments, and finite versions of both identities in Lemma [\[lem:tail-algebra\]](#lem:tail-algebra){reference-type="ref" reference="lem:tail-algebra"}. The independently frozen six-row fixture has canonical SHA-256

`d55fd48071eb5b88c054f3d34329f274f792f2bbd859b4ab98e31b5b7020beb8`.

Second, directed decimal arithmetic at precision $60$ is converted to exact rational endpoints. It enumerates the $9592$ primes through $100000$ and bounds every omitted prime by the exact integer tail $$\sum_{n>100000}\frac1{n^2-1}
 =\frac{200001}{20000200000}.
 \label{eq:numeric-tail}$$ All comparisons fail closed if outward upper and lower endpoints overlap in the wrong order. The rows $y=1,2,3,5,10,25$ reproduce the $170$ and $342$ bounds; they do not prove the all-$y$ theorem by fitting.

For orientation only, the directed product layer encloses $$0.46967971561917<X_\infty<0.46993774873491.$$ These decimals are a finite diagnostic. Positivity in the theorem is the exact run argument [\[eq:X-positive\]](#eq:X-positive){reference-type="eqref" reference="eq:X-positive"}, not this numerical enclosure.

The release builder locks exactly $25$ immutable inputs: seven RH-374 files, eight RH-379 files, eight RH-380 files, and two RH-MVP2 archive summaries. It checks both the live SHA-256 and byte identity with each declared release commit. Mutable project instructions and handoff state are deliberately excluded. The result ledger has a recursively closed Draft 2020-12 schema, and archive replay rejects missing members, unsafe paths, duplicate JSON keys, hash drift, release-commit rebinding, or a semantic PDF that differs from `main.pdf`.

Reproduction from this directory is

    make result
    make test
    make pdf
    make archive

# Scope, limitations, and next edge

The theorem closes one precise question: it identifies the first-order prime-square-tail scale of the square-clock nonattainment gap and proves an explicit quadratic remainder inside the frozen RH-379 class. Its limits are equally precise.

-   The theorem is phasewise $c_{11}=0$. It does not cover unrestricted lag-two tables or assume the missing phase-weighted shift-two correlation cancellation.

-   The constant $342$ is explicit and uniform for $y\ge1$, but no optimality is claimed for either $170$ or $342$.

-   No exact second-order coefficient is identified. In particular, the theorem does not collapse all quadratic information to one multiple of $T_y^2$.

-   No asymptotic for $T_y$ in terms of $p_y$, no growing clock $q(N)$, and no adaptive-capacity convergence is proved.

-   Finite product rows and decimal enclosures are reproduction only; they are not finite-order regression promoted to an all-order claim.

-   No canonical intrinsic dynamical spectral determinant, time-oriented scattering completion, self-adjoint generator, von Mangoldt prime-power trace identity, or completed-zeta divisor equality is constructed. Gates A--E remain false/open [@RHMVP2].

-   There is no Hilbert--Pólya operator, no identification of Riemann zeros, and no implication for the Riemann hypothesis.

The immediate within-class next edge is a genuinely second-order analysis of the Euler tails and of $M_j/A_j$. Such a successor must retain every independent quadratic tail scale that survives the exact algebra and prove an all-order remainder; this paper does not state its coefficient. The first class-enlargement trigger remains a theorem for the required phase-weighted shift-two Möbius correlations.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

All theorem inputs, exact source code, tests, closed result schema, source locks, and archive manifests are contained in the repository paper directory. No private dataset is used.

#### Author contributions.

The RH research program performed conceptualization, formal analysis, software construction, verification, artifact curation, adversarial review, and manuscript preparation.

#### Funding.

No external funding is declared.

#### Competing interests.

No competing interests are declared.

#### Ethics and human participants.

This mathematical and computational study uses no human participants, animals, or personal data; ethics approval and consent are not applicable.

#### AI assistance disclosure.

AI-assisted tools supported source triage, symbolic checking, deterministic artifact generation, drafting, and adversarial review. Every released claim is constrained by immutable repository sources and reproducible verification artifacts; responsibility for the scoped mathematical statements remains with the research program.
