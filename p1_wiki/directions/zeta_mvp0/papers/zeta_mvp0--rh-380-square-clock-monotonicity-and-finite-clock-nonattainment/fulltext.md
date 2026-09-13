---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-380-square-clock-monotonicity-and-finite-clock-nonattainment"
canonical_tex: "zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment/main.pdf"
source_sha256: "6110b876e1b31fe79e7ff72e5058d97179575cf1dccce86e8c7c0a049d57451f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Square-Clock Monotonicity and Finite-Clock Nonattainment for Phasewise Chowla-Free Memory

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-380-square-clock-monotonicity-and-finite-clock-nonattainment/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the finite-clock attainment question left open by RH-379, without enlarging its factor class. A clock $q$ is fixed before $N\to\infty$; the admissible objects are universally distance-two-safe phasewise lag-two tables, and their interpolation coefficient $c_{11}(r)$ is zero at every phase. At the square clocks $$q_y=4\prod_{i\le y}p_i^2,
   \qquad A_y=\prod_{i\le y}(p_i^2-1),
   \qquad D_y=\prod_{i\le y}(p_i^2-2),$$ let $R_\ell^{(y)}$ count positive runs of length $\ell$ in the odd support word, and put $$\mathcal E_y=\sum_{\ell\ \mathrm{even}}R_\ell^{(y)},\quad
   L_y=\sum_{\ell\ \mathrm{even}}\ell R_\ell^{(y)},\quad
   M_y=\sum_{\ell\ \mathrm{odd}}(\ell-1)R_\ell^{(y)}.$$ Deleting the new prime-square residue from replicated old runs gives the all-order identity $$\mathcal E_{y+1}=(p_{y+1}^2-2)\mathcal E_y+M_y.$$ Combining it with the locked RH-374 odd-run recurrence and the exact RH-379 square-clock formula yields an exact increment. Since $L_y-2\mathcal E_y=2R_4^{(y)}+4R_6^{(y)}+6R_8^{(y)}\ge6$, the sequence $G(q_y)$ is strictly increasing.

  We then prove a deliberately special saturation law: if $q_y\mid Q$ and $Q$ has exactly the same prime support, the mod-$4$ and mod-$9$ zero-weight separators split the fine addition-by-two cycles into replicated finite paths, and $G(Q)=G(q_y)$. For arbitrary fixed $q$, taking $Q=\operatorname{lcm}(q,q_y)$ therefore gives $$G(q)\le G(q_y)<B_\infty,
   \qquad
   B_\infty-G(q)\ge
   \frac{12}{\pi^2A_y(p_{y+1}^2-1)}.$$ Thus the RH-379 all-clock supremum is not attained by any finite clock. This is not a growing-clock result, a general cyclic-cover theorem, an adaptive-capacity limit, an operator or trace construction, a zero identification, or a statement about the Riemann hypothesis.
author:
- RH research program
bibliography:
- references.bib
date: 'August 7, 2026'
title: |
  Square-Clock Monotonicity and Finite-Clock Nonattainment\
  for Phasewise Chowla-Free Memory
```

## Markdown 正文

**Keywords:** Möbius function; square clocks; max-plus optimization; run deletion; finite-clock nonattainment.

# Frozen class and predecessor inputs

The object optimized here is exactly the RH-379 phasewise Chowla-free memory class [@RH379]. We restate the boundary because every theorem below depends on it.

Fix a finite integer $q\ge1$ before taking any natural-density limit. At each $r\in\mathbb Z/q\mathbb Z$, choose a table $$f_r:\{-1,0,1\}^2\longrightarrow\{-1,+1\},
 \qquad
 \epsilon_n=f_{n\bmod q}\bigl(\mu(n-2),\mu(n)\bigr).$$ The phase family is universally safe if no ternary input can produce $\epsilon_n=\epsilon_{n+2}=+1$. It belongs to the declared class only if the coefficient $c_{11}(r)$ of $\mu(n-2)\mu(n)$ in the RH-379 interpolation is zero for every phase $r$. Let $G(q)$ be the largest absolute fixed-clock limiting correlation over this class.

The phasewise condition is essential. If $c_{11}(r)\ne0$ at even one phase, the limiting expansion contains a phase-weighted shift-two Möbius correlation not controlled by the frozen sources. No cancellation between different phases is assumed here.

We use three exact predecessor results. RH-374 introduces the square-clock support word, proves its run formula and odd-run recurrence, proves the persistence of a length-eight run, and defines $B_\infty$ as the limit of its strictly increasing square-clock sequence [@RH374]. RH-375 identifies the same constant as the all-clock supremum in the one-site class [@RH375]. RH-379 reduces the present memory class to the three actions $0,J,I$, proves input reflection, and establishes $$\sup_{q<\infty}G(q)=B_\infty.
 \label{eq:rh379-supremum}$$ It did not decide finite-clock attainment.

For reference, the exact progression weights at phase $r$ are $$w_r(0)=0,\qquad w_r(J)=\delta_{q,r}-\vartheta_{q,r},\qquad
 w_r(I)=\delta_{q,r},$$ where $\delta_{q,r}$ is the squarefree density and $\vartheta_{q,r}$ is the joint squarefree density at displacement two. Along an addition-by-two cycle, the compatibility matrix is $$\begin{array}{c|ccc}
 &0&J&I\\ \hline
0&1&1&1\\
J&1&1&0\\
I&1&1&0
\end{array}.
\label{eq:compatibility}$$ In particular, action $0$ is compatible with everything in both directions. RH-379 proves that the positive three-state optimum equals $G(q)$: input reflection realizes the negative of every limiting score, so the absolute optimum introduces no additional case.

# Square-clock runs and a deletion recurrence

Let $3=p_1<p_2<\cdots$ be the odd primes and define $$P_y=\prod_{i\le y}p_i^2,\qquad q_y=4P_y,\qquad
 A_y=\prod_{i\le y}(p_i^2-1),\qquad
 D_y=\prod_{i\le y}(p_i^2-2).
 \label{eq:square-parameters}$$ On $\mathbb Z/P_y\mathbb Z$, set $$w_y(k)=\mathbf1_{\{p_i^2\nmid 2k+1\ \text{for every }i\le y\}}.
 \label{eq:support-word}$$ The multiples of $9$ cut its cyclic positive runs, so every run has length at most eight. Write $R_\ell^{(y)}$ for the number of runs of exact length $\ell$. We need four statistics: $$\begin{aligned}
 O_y&=R_1^{(y)}+R_3^{(y)}+R_5^{(y)}+R_7^{(y)},
 &\mathcal E_y&=R_2^{(y)}+R_4^{(y)}+R_6^{(y)}+R_8^{(y)},
 \label{eq:OE}\\
 L_y&=2R_2^{(y)}+4R_4^{(y)}+6R_6^{(y)}+8R_8^{(y)},
 &M_y&=2R_3^{(y)}+4R_5^{(y)}+6R_7^{(y)}.
 \label{eq:LM}\end{aligned}$$ Thus $L_y$ counts sites inside even runs, while $M_y$ is the sum of $\ell-1$ over odd runs. These quantities must not be conflated with one another.

RH-374 gives, with $$e_m^{(y)}=\prod_{i\le y}\left(1-\frac{m}{p_i^2}\right),$$ the exact finite formula $$R_\ell^{(y)}=
 \begin{cases}
 P_y(e_\ell^{(y)}-2e_{\ell+1}^{(y)}+e_{\ell+2}^{(y)}),&1\le\ell\le7,\\
 P_y e_8^{(y)},&\ell=8.
 \end{cases}
 \label{eq:run-formula}$$ It also proves $$O_{y+1}=(s-1)O_y+L_y,\qquad s=p_{y+1}^2.
 \label{eq:odd-recurrence}$$

[\[lem:deletion\]]{#lem:deletion label="lem:deletion"} Let an old positive run have length $1\le\ell\le8$, and let $s=p_{y+1}^2$. Across the $s$ replicated copies used to pass from $w_y$ to $w_{y+1}$, the number of descendant even positive runs is $$\begin{cases}
 s-2,&\ell\text{ even},\\
 \ell-1,&\ell\text{ odd}.
 \end{cases}
 \label{eq:per-run-ledger}$$

Represent each cyclic old run as an unwrapped interval bracketed by its two old zero sites. Those zeros remain zero in every lift, so no run crosses the chosen $P_y$ seam and no descendant can merge across either bracket. Because $(P_y,s)=1$, each old positive site has exactly one lift at which the new prime square divides $2k+1$. If two distinct positions $d,d'$ in the same run were deleted in the same copy, subtraction would give $2(d-d')\equiv0\pmod s$. This is impossible because $0<2|d-d'|\le14<s$ and every new $s=p_{y+1}^2$ is at least $25$. Hence an old run has $s-\ell$ untouched copies and exactly one single-site deletion at each of its $\ell$ positions, all in distinct copies.

Suppose first that $\ell$ is even. Each untouched copy contributes one even run, giving $s-\ell$. Deleting either endpoint leaves one odd run and contributes no even run. Each of the $\ell-2$ internal deletions leaves two pieces of opposite parity, exactly one of which is a positive even run. The total is $(s-\ell)+(\ell-2)=s-2$.

Now suppose that $\ell$ is odd. Untouched copies contribute no even run. For $\ell=1$, deleting the sole site leaves no positive piece, agreeing with $\ell-1=0$. Let $\ell\ge3$. For a deletion at position $d\in\{0,\ldots,\ell-1\}$, the two pieces have lengths $d$ and $\ell-1-d$, hence the same parity. Each of the two distinct endpoints contributes one positive even piece, and every internal even deletion position contributes two. The total is $2+2(\ell-3)/2=\ell-1$. Odd deletion positions contribute none. This proves [\[eq:per-run-ledger\]](#eq:per-run-ledger){reference-type="eqref" reference="eq:per-run-ledger"}.

[\[prop:even-recurrence\]]{#prop:even-recurrence label="prop:even-recurrence"} For every $y\ge1$, $$\boxed{\displaystyle
 \mathcal E_{y+1}=(s-2)\mathcal E_y+M_y,\qquad s=p_{y+1}^2.}
 \label{eq:even-recurrence}$$

Sum Lemma [\[lem:deletion\]](#lem:deletion){reference-type="ref" reference="lem:deletion"} over all old runs. Each old even run supplies $s-2$ descendant even runs. An old odd run of length $\ell$ supplies $\ell-1$, and the sum of those contributions is precisely $M_y$. Old zero sites remain zero, while new deletions only split positive runs; there is therefore no uncounted merger across old run boundaries.

# Exact increment and strict monotonicity

The locked RH-379 square-clock formula can be written $$G(q_y)=\frac{4}{\pi^2}
       +\frac{2O_y+4\mathcal E_y}{A_y\pi^2}
       -\frac{\mathcal E_y}{D_y}\kappa_2.
 \label{eq:G-square}$$ Put $$H_y=\kappa_2\frac{A_y}{D_y}.
 \label{eq:H}$$ RH-379 proves the exact Euler-product inequality $$0<H_y<\frac4{\pi^2},\qquad
                         H_y\longrightarrow\frac4{\pi^2}.
 \label{eq:H-gap}$$ No finite decimal is used in this statement.

[\[thm:increment\]]{#thm:increment label="thm:increment"} For $s=p_{y+1}^2$, $$\boxed{\begin{aligned}
G(q_{y+1})-G(q_y)
={}&\frac{2(L_y-2\mathcal E_y)}{\pi^2A_y(s-1)}\\
&+\frac{M_y}{A_y(s-1)}
 \left(\frac4{\pi^2}-H_{y+1}\right).
\end{aligned}}
\label{eq:increment}$$ Consequently $$G(q_{y+1})-G(q_y)
 \ge \frac{12}{\pi^2A_y(s-1)}>0.
 \label{eq:increment-lower}$$ Thus $G(q_y)$ is strictly increasing for every $y\ge1$.

Besides [\[eq:odd-recurrence\]](#eq:odd-recurrence){reference-type="eqref" reference="eq:odd-recurrence"} and [\[eq:even-recurrence\]](#eq:even-recurrence){reference-type="eqref" reference="eq:even-recurrence"}, the definitions give $$A_{y+1}=(s-1)A_y,\qquad D_{y+1}=(s-2)D_y.$$ Substituting all four recurrences into [\[eq:G-square\]](#eq:G-square){reference-type="eqref" reference="eq:G-square"} and subtracting the $y$ expression gives, in the exact basis $\mathbb Q\pi^{-2}+\mathbb Q\kappa_2$, $$\frac{2(L_y-2\mathcal E_y)+4M_y}{A_y(s-1)\pi^2}
 -\frac{M_y}{D_y(s-2)}\kappa_2.
 \label{eq:increment-basis}$$ Since $$\frac{H_{y+1}}{A_y(s-1)}
 =\frac{\kappa_2}{D_y(s-2)},$$ equation [\[eq:increment-basis\]](#eq:increment-basis){reference-type="eqref" reference="eq:increment-basis"} is exactly [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"}.

The first numerator has the combinatorial identity $$L_y-2\mathcal E_y
 =2R_4^{(y)}+4R_6^{(y)}+6R_8^{(y)}.
 \label{eq:X}$$ RH-374 proves $R_8^{(y)}\ge1$, so this is at least six. Also $M_y\ge0$ by definition, and the parenthesis in the second line of [\[eq:increment\]](#eq:increment){reference-type="eqref" reference="eq:increment"} is positive by [\[eq:H-gap\]](#eq:H-gap){reference-type="eqref" reference="eq:H-gap"}. Dropping that nonnegative term yields [\[eq:increment-lower\]](#eq:increment-lower){reference-type="eqref" reference="eq:increment-lower"}.

RH-379 writes $G(q_y)=B_y+\Delta_y$ and proves $\Delta_y\to0$. Theorem [\[thm:increment\]](#thm:increment){reference-type="ref" reference="thm:increment"} proves monotonicity of the sum $G(q_y)$; it neither uses nor asserts monotonicity of $\Delta_y$.

# A separator-specific same-support theorem

The next result is not a general statement about covers of weighted cyclic graphs. Its proof uses the precise local densities and zero-weight phases of the square clocks.

[\[thm:saturation\]]{#thm:saturation label="thm:saturation"} Fix $y\ge1$. Suppose $q_y\mid Q$ and $Q$ has exactly the same prime divisors as $q_y$. Writing $Q=Rq_y$, one has $$\boxed{G(Q)=G(q_y).}
 \label{eq:saturation}$$

Every prime in either clock occurs to exponent at least two. The exact local squarefree formula therefore says that a phase has positive $\delta$ precisely when it is nonzero modulo every supported prime square. At such a phase, $$\delta_{q_y,r}=\frac{2}{A_y\pi^2},\qquad
 \delta_{Q,t}=\frac{2}{RA_y\pi^2}
 \quad(t\equiv r\pmod{q_y}),
 \label{eq:delta-scale}$$ and both sides are zero simultaneously otherwise. Likewise, the exact two-squarefree formula gives $$\vartheta_{q_y,r}=\frac{\kappa_2}{2D_y},\qquad
 \vartheta_{Q,t}=\frac{\kappa_2}{2RD_y}
 \quad(t\equiv r\pmod{q_y}),
 \label{eq:theta-scale}$$ whenever neither the current nor its predecessor is forced divisible by a supported prime square, with simultaneous zero otherwise. Thus every three-state weight on a fine phase is exactly $1/R$ times the weight of its projection modulo $q_y$.

Addition by two has an even and an odd cycle because both clocks are even. On the even cycle, a phase divisible by $4$ has $\delta=\vartheta=0$. On the odd cycle, a phase divisible by $9$ has $\delta=\vartheta=0$. At a zero-weight phase, replace the action by $0$. This cannot lower the score and, by [\[eq:compatibility\]](#eq:compatibility){reference-type="eqref" reference="eq:compatibility"}, can only relax the two adjacent compatibility conditions. These mod-$4$ and mod-$9$ phases are therefore genuine separators.

Under projection modulo $q_y$, each fine addition-by-two cycle traverses the corresponding base cycle exactly $R$ times. The separators cut it into $R$ copies of the same finite path collection. Each copied path has weights scaled by $1/R$ by [\[eq:delta-scale\]](#eq:delta-scale){reference-type="eqref" reference="eq:delta-scale"}--[\[eq:theta-scale\]](#eq:theta-scale){reference-type="eqref" reference="eq:theta-scale"}. Max-plus path optimization is positively homogeneous, so the $R$ copies together have exactly the base optimum. Summing the even and odd components proves [\[eq:saturation\]](#eq:saturation){reference-type="eqref" reference="eq:saturation"}. Finally, the RH-379 input reflection transfers the positive optimum identity to the absolute value defining $G$.

The prime-support hypothesis cannot be erased from this proof. For example, $36\mid180$, but $180$ adds the prime $5$, and the exact values are $$G(36)=\frac{9}{2\pi^2}-\frac{\kappa_2}{7},\qquad
 G(180)=\frac{73}{16\pi^2}-\frac{25\kappa_2}{161}.$$ The inequality is exact rather than a comparison of formal coefficient pairs: with $H=\pi^2\kappa_2<4$ from the locked RH-379 enclosure, $$G(180)-G(36)
 =\frac1{\pi^2}\left(\frac1{16}-\frac{2H}{161}\right)
 >\frac1{\pi^2}\left(\frac1{16}-\frac8{161}\right)>0.$$ This is a negative control against a general-multiple or general-cover reading of Theorem [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}; it is not a counterexample to the theorem's same-support statement.

# Finite-clock nonattainment and an explicit gap

[\[lem:divisibility\]]{#lem:divisibility label="lem:divisibility"} If $q\mid Q$, then $G(q)\le G(Q)$.

Repeat every phase table modulo $Q$ according to its residue modulo $q$. The output word is unchanged for every input, so universal safety, $c_{11}=0$, and the fixed-clock limiting score are unchanged. The $Q$-class can only have a larger optimum. Input reflection again identifies the positive and absolute formulations.

[\[thm:nonattainment\]]{#thm:nonattainment label="thm:nonattainment"} Let $q\ge1$ be any fixed finite clock. Choose $y\ge1$ so that every odd prime divisor of $q$ belongs to $\{p_1,\ldots,p_y\}$. Then $$\boxed{\displaystyle
 G(q)<B_\infty,\qquad
 B_\infty-G(q)\ge
 \frac{12}{\pi^2A_y(p_{y+1}^2-1)}>0.}
 \label{eq:gap}$$ Consequently no fixed finite clock attains the all-clock supremum [\[eq:rh379-supremum\]](#eq:rh379-supremum){reference-type="eqref" reference="eq:rh379-supremum"}.

Set $$Q=\operatorname{lcm}(q,q_y).$$ Then $q\mid Q$ and $q_y\mid Q$. The prime support of $Q$ is exactly that of $q_y$: the choice of $y$ contains all odd divisors of $q$, while the factor $4$ in $q_y$ handles the prime $2$. This remains true for an arbitrary $2$-adic exponent in $q$ and arbitrary exponents of its supported odd primes; those exponents merely enlarge $R=Q/q_y$. Lemma [\[lem:divisibility\]](#lem:divisibility){reference-type="ref" reference="lem:divisibility"} and Theorem [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"} give $$G(q)\le G(Q)=G(q_y).
 \label{eq:lcm-chain}$$

RH-379 proves $G(q_j)\to B_\infty$. Theorem [\[thm:increment\]](#thm:increment){reference-type="ref" reference="thm:increment"} makes that sequence strictly increasing, hence $G(q_y)<B_\infty$. More quantitatively, telescope the nonnegative increments: $$B_\infty-G(q_y)
 =\sum_{j\ge y}\bigl(G(q_{j+1})-G(q_j)\bigr)
 \ge G(q_{y+1})-G(q_y)
 \ge\frac{12}{\pi^2A_y(p_{y+1}^2-1)}.$$ Combining this with [\[eq:lcm-chain\]](#eq:lcm-chain){reference-type="eqref" reference="eq:lcm-chain"} proves [\[eq:gap\]](#eq:gap){reference-type="eqref" reference="eq:gap"}.

The quantifiers in Theorem [\[thm:nonattainment\]](#thm:nonattainment){reference-type="ref" reference="thm:nonattainment"} are fixed-clock quantifiers. The index $y$ may be chosen after the finite integer $q$ is given, but both $q$ and the auxiliary clock $Q$ are fixed before the $N\to\infty$ limits already used to define $G$. There is no diagonal choice $q=q(N)$.

# Exact certificate and reproduction protocol

The standard-library artifact is a proof companion, not a source of the all-$y$ theorem. It implements exact rational arithmetic in the basis $u/\pi^2+v\kappa_2$ and fails closed if the locked enclosure $3.18<\pi^2\kappa_2<3.19$ cannot decide a max-plus comparison. The release builder verifies that the sharper RH-379 rational interval lies strictly inside this coarse interval.

The certificate performs four independent finite checks:

1.  it compares the Euler-product run formula with direct cyclic words for $y=1,2,3$ and samples the per-run deletion ledger at $s=25,49,121$;

2.  it checks the recurrence and increment algebra, including the exact anchors in Table [1](#tab:anchors){reference-type="ref" reference="tab:anchors"};

3.  for nine same-support refinements it checks every fine-residue $\delta$ and $\vartheta$ scaling law, the mod-$4$/mod-$9$ separator causes, run replication, and an independent generic three-state cyclic max-plus dynamic program;

4.  it locks $Q=180$ as a new-prime negative control and records finite least-common-multiple fixtures for the exponent scope.

::: {#tab:anchors}
   $y$    $\mathcal E_y$   $L_y$   $M_y$   $L_y-2\mathcal E_y$ $G(q_{y+1})-G(q_y)$
  ----- ---------------- ------- ------- --------------------- -----------------------------------------------------
    1                  1       8       0                     6 $\frac{1}{16\pi^2}$
    2                 23     160      24                   114 $\frac{9}{256\pi^2}-\frac{24}{7567}\kappa_2$
    3               1105    7160    1512                  4950 $\frac{443}{30720\pi^2}-\frac{216}{128639}\kappa_2$

  : Exact finite anchors. These rows reproduce identities; the all-order proofs are Theorem [\[thm:increment\]](#thm:increment){reference-type="ref" reference="thm:increment"} and Theorem [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}.
:::

The result ledger has a recursively closed Draft 2020-12 schema. Its 24 source locks exclude the mutable project instructions and handoff file. For each locked predecessor input, the builder checks both the live SHA-256 and byte identity with the file at its declared release commit. To replay from this directory, run

    make result
    make test
    make pdf
    make archive

The semantic PDF must be byte-identical to `main.pdf`; archive verification fails on any missing member, hash mismatch, source-lock drift, or PDF mismatch.

# Boundaries and next theorem edge

The proved result is narrow but complete: it supplies an all-order even-run recurrence, exact strict square-clock monotonicity, a separator-specific saturation theorem, finite-clock nonattainment, and an explicit positive gap within the frozen RH-379 class.

The following statements are outside the theorem.

-   No table with phasewise $c_{11}(r)\ne0$ is covered. The first missing object is a phase-weighted shift-two Möbius correlation theorem.

-   Same-support saturation is not asserted for an arbitrary weighted cyclic graph, an arbitrary cover, or a multiplier that introduces a new prime.

-   No monotonicity is asserted for the correction $\Delta_y$.

-   No growing clock $q(N)$ and no convergence to adaptive distance-two capacity is asserted.

-   The construction supplies no canonical intrinsic dynamical spectral determinant, time-oriented scattering completion, self-adjoint generator, von Mangoldt prime-power trace identity, or completed-zeta divisor equality. Gates A--E therefore remain false/open.

-   There is no Hilbert--Pólya operator, no identification of Riemann zeros, and no implication for the Riemann hypothesis.

#### Immediate analytic rate trigger (not proved here).

There is a within-class refinement beyond nonattainment. Put $$T_y=\sum_{p>p_y}\frac1{p^2-1},\qquad
 e_m=\prod_{p\ {\rm odd}}\left(1-\frac{m}{p^2}\right),$$ and $$X_\infty=
 \frac{2e_4-4e_5+6e_6-8e_7+10e_8}{e_1}>0.$$ Indeed, if $E_m^{(y)}=\prod_{i\le y}(1-m/p_i^2)$, the locked run formula gives $$\frac{L_y-2\mathcal E_y}{A_y}
 =\frac{2E_4^{(y)}-4E_5^{(y)}+6E_6^{(y)}
              -8E_7^{(y)}+10E_8^{(y)}}{E_1^{(y)}}
 \longrightarrow X_\infty.$$ The same quantity is the normalized $2R_4^{(y)}+4R_6^{(y)}+6R_8^{(y)}$, so $X_\infty\ge6e_8/e_1>0$. This identifies the proposed first-order coefficient; it does not prove the tail asymptotic. The exact reopen target is $$B_\infty-G(q_y)=\frac{2X_\infty}{\pi^2}T_y+O(T_y^2),$$ with the successor required to show that the $M_y$ contribution is only second order. RH-380 does not prove this rate theorem; proving the required Euler-product expansion and $O(T_y^2)$ remainder, not computing further finite rows or fitting decay, is the trigger.

#### First class-enlargement blocker.

Extending beyond $c_{11}=0$ still requires a genuine theorem for phase-weighted shift-two Möbius correlations. Without such an input, the unrestricted-memory route remains [stop\_scoped]{.smallcaps}.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

All theorem inputs, exact code, tests, result schema, source locks, and archive manifests are contained in the repository paper directory. No private dataset is used.

#### Author contributions.

The RH research program performed conceptualization, formal analysis, software construction, verification, visualization checks, and manuscript preparation.

#### Funding.

No external funding is declared.

#### Competing interests.

No competing interests are declared.

#### Ethics and human participants.

This mathematical and computational study uses no human participants, animals, or personal data; ethics approval and consent are not applicable.

#### AI assistance disclosure.

AI-assisted tools supported algebra checking, artifact generation, drafting, and adversarial review. Every released claim is constrained by the locked repository sources and deterministic verification artifacts; responsibility for the scoped mathematical statements remains with the research program.
