---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-394-odd-parity-terminal-log-mobius-compiler"
canonical_tex: "zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler/main.pdf"
source_sha256: "1cc35282bb225b47248a07115fbcbaf32ec5bf8857f386809f6d2ca661b52354"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Odd-Parity Terminal-Log Möbius Compiler and the Complete Three-Shift Table Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-394-odd-parity-terminal-log-mobius-compiler/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix finitely many distinct integer shifts, a modulus, phase coefficients, and any terminal clock. We determine terminal logarithmic averages for every coordinatewise-quadratic Möbius monomial whose odd-exponent support has size zero, two, or any positive odd integer. All nonempty admitted odd channels cancel, while the all-even channels have explicit phase-resolved squarefree densities. The new analytic step applies the odd-total-power theorem of Tao and Teräväinen after a fully normalized affine progression reduction; the zero- and two-odd channels are paid separately by a local CRT argument and the frozen two-factor compiler.

  The admitted dimension is $2^m+\binom m2 2^{m-2}+(3^m-1)/2$. Consequently all $27$ coordinatewise-quadratic monomials in three variables are covered. Every fixed phase family of ternary three-shift tables therefore has an exact limit law. In four variables the sole missing coefficient is the signed four-cube coefficient, giving exactly $\binom{16}{8}2^{65}$ eligible sign tables per phase. Intrinsically, a table is covered exactly when the even part on every Boolean support stratum has Fourier degree at most two. For distinguished-current scores, the corresponding odd-degree-one criterion yields an explicit product count; in particular all $512^q$ two-input phase families cancel. The results are qualitative and fixed-data: no even correlation of order at least four, rate, growing family, or prelimit capacity is asserted.
author:
- RH research program
bibliography:
- references.bib
date: 'August 11, 2026'
title: 'Odd-Parity Terminal-Log Möbius Compiler and the Complete Three-Shift Table Law'
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; odd-order correlation; squarefree phase density; ternary interpolation; Boolean Fourier analysis.

# Setup and principal statements

Write $\mu_0(t)=\mu(t)$ for integers $t\geq1$, and $\mu_0(t)=0$ for $t\leq0$. A *terminal clock* is a function $$1\leq\omega(X)\leq X,\qquad \omega(X)\longrightarrow\infty.
  \label{eq:clock}$$ Fix positive integers $m,q$, pairwise-distinct integer shifts $a_1,\ldots,a_m$, and fixed phase coefficients. Every datum, including the clock, is fixed before $X\to\infty$. Put $$z_i(n)=\mu_0(n-a_i),\qquad
 O(\alpha)=\{i:\alpha_i=1\},\qquad
 E(\alpha)=\{i:\alpha_i=2\}$$ for $\alpha\in\{0,1,2\}^m$. Call $\alpha$ *admissible* when $$|O(\alpha)|\in\{0,2\}\cup\{1,3,5,\ldots\}.
 \label{eq:admissible}$$ Thus the first excluded odd-support size is four.

For $E\subseteq[m]$, first deduplicate the shifted residues modulo $p^2$, and define $$B_p(E)=\{a_i\bmod p^2:i\in E\},\quad
 \nu_p(E)=|B_p(E)|,
 \quad
 \tau_{p,E}(r)=|\{b\in B_p(E):b\equiv r\pmod p\}|.
 \label{eq:local-data}$$ Distinct elements of $B_p(E)$ may still collide after reduction modulo $p$. The phase density is $$\begin{aligned}
 \Theta_{q,r}(E)
 &=\frac1q\prod_{p\nmid q}\left(1-\frac{\nu_p(E)}{p^2}\right)
 \prod_{p\parallel q}\left(1-\frac{\tau_{p,E}(r)}p\right)
 \prod_{p^2\mid q}\mathbf 1_{\{r\bmod p^2\notin B_p(E)\}},
 \label{eq:theta}\\
 \kappa_E&=\prod_p\left(1-\frac{\nu_p(E)}{p^2}\right).
 \label{eq:kappa}\end{aligned}$$ In particular, $\Theta_{q,r}(\varnothing)=1/q$.

Let $$P_r(z)=\sum_{\alpha\ \mathrm{admissible}}
 c_\alpha(r)\prod_{i=1}^m z_i^{\alpha_i}
 \label{eq:polynomial}$$ with arbitrary fixed real or complex coefficients for each $r\bmod q$. Define $$T_X(P;\omega)=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\leq X}
 \frac{P_{n\bmod q}(z_1(n),\ldots,z_m(n))}{n}.
 \label{eq:functional}$$

[\[thm:compiler\]]{#thm:compiler label="thm:compiler"} For every fixed datum above and every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, $$T_X(P;\omega)\longrightarrow
 \sum_{r\bmod q}\ \sum_{\alpha\in\{0,2\}^m}
 c_\alpha(r)\Theta_{q,r}(E(\alpha)).
 \label{eq:compiler-limit}$$ Every admitted nonempty odd-support channel vanishes. Moreover, $$\sum_{r\bmod q}\Theta_{q,r}(E)=\kappa_E.
 \label{eq:phase-sum}$$ The number of admitted monomials is $$D'_m=2^m+\binom m2 2^{m-2}+\frac{3^m-1}{2},
 \label{eq:dimension}$$ where the two-odd term is zero for $m<2$.

We next state the exact table law. For $U\subseteq[m]$, set $$\Pi_{q,r}(U)=\sum_{W\subseteq[m]\setminus U}
 (-1)^{|W|}\Theta_{q,r}(U\cup W).
 \label{eq:pi}$$ For a table $f_r:\{-1,0,+1\}^m\to\mathbb R$, write $$\overline f_{r,U}=2^{-|U|}
 \sum_{\varepsilon\in\{-1,+1\}^U}
 f_r(\varepsilon_U,0_{U^c}).
 \label{eq:stratum-average}$$

[\[thm:table\]]{#thm:table label="thm:table"} Let $f_r:\{-1,0,+1\}^m\to\mathbb R$ be fixed for each phase. For $S\subseteq[m]$, let $h_{r,S}(\varepsilon)=f_r(\varepsilon_S,0_{S^c})$ on $\{-1,+1\}^S$, and put $$h_{r,S}^{+}(\varepsilon)
 =\frac{h_{r,S}(\varepsilon)+h_{r,S}(-\varepsilon)}2.$$ The coordinatewise-quadratic interpolant of every $f_r$ contains only admissible monomials if and only if, for every $r$ and $S$, the Boolean Fourier degree of $h_{r,S}^{+}$ is at most two. Under this equivalent condition, $$\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\leq X}
 \frac{f_{n\bmod q}(z_1(n),\ldots,z_m(n))}{n}
 \longrightarrow
 \sum_{r\bmod q}\sum_{U\subseteq[m]}
 \Pi_{q,r}(U)\overline f_{r,U}.
 \label{eq:table-limit}$$ Here $\Pi_{q,r}(U)\geq0$ and $$\sum_{U\subseteq[m]}\Pi_{q,r}(U)=\frac1q.
 \label{eq:pi-mass}$$

[\[cor:three-four\]]{#cor:three-four label="cor:three-four"} For $m=3$, $D'_3=27$, so every fixed phase family of tables $f_r:\{-1,0,+1\}^3\to\mathbb R$ satisfies [\[eq:table-limit\]](#eq:table-limit){reference-type="eqref" reference="eq:table-limit"}. In particular, all $2^{27q}$ sign-table phase families are covered.

For $m=4$, $D'_4=80$ out of $81$. The sole excluded coefficient is $$c_{1111}(f_r)=\frac1{16}
 \sum_{\varepsilon\in\{-1,+1\}^4}
 \varepsilon_1\varepsilon_2\varepsilon_3\varepsilon_4 f_r(\varepsilon).
 \label{eq:c1111}$$ Exactly $\binom{16}{8}2^{65}$ sign tables on $\{-1,0,+1\}^4$ have $c_{1111}=0$ and are covered in one phase; hence the phase-family count is $[\binom{16}{8}2^{65}]^q$. Tables failing this test are outside the theorem, with no claim that their averages are nonzero or divergent.

# Local densities and the old channels

We first pay the all-even channel locally. For a finite prime set $\mathcal P$ containing every divisor of $q$, impose $p^2\nmid n-a_i$ for $p\in\mathcal P$ and $i\in E$. The condition is periodic modulo $\operatorname{lcm}(q,\prod_{p\in\mathcal P}p^2)$. Harmonic mass is equidistributed among the residue classes of any fixed modulus: $$\frac1{\log\omega(X)}
 \sum_{\substack{X/\omega(X)<n\leq X\\n\equiv b\pmod L}}
 \frac1n\longrightarrow\frac1L.
 \label{eq:harmonic-ap}$$ This follows by subtracting the two standard harmonic-progression asymptotics; if the lower endpoint stays bounded, its contribution is constant while $\log X/\log\omega(X)\to1$.

[\[lem:density\]]{#lem:density label="lem:density"} For fixed $E,q,r$, the terminal harmonic density of $$n\equiv r\pmod q,\qquad \mu_0(n-a_i)^2=1\quad(i\in E)$$ exists for every terminal clock and equals $\Theta_{q,r}(E)$. Its sum over phases is $\kappa_E$.

At a prime $p\nmid q$, exactly $\nu_p(E)$ of the $p^2$ classes are forbidden. If $p\parallel q$, fixing $r\pmod p$ leaves $p$ lifts modulo $p^2$, of which $\tau_{p,E}(r)$ are forbidden. If $p^2\mid q$, the phase either forces a forbidden class or avoids all of them. The Chinese remainder theorem and [\[eq:harmonic-ap\]](#eq:harmonic-ap){reference-type="eqref" reference="eq:harmonic-ap"} therefore give the finite truncation of [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}.

It remains to remove the cutoff. An elementary square-divisor union bound gives, for fixed shifts and $P\geq2$, $$\sum_{X/\omega<n\leq X}\frac1n
 \mathbf 1_{\{p^2\mid n-a_i\text{ for some }i\in E, p>P\}}
 \ll_{m,\mathbf a}\frac{\log\omega}{P}+1.
 \label{eq:tail}$$ Indeed, substitute $n-a_i=p^2k$, sum the resulting harmonic $k$-interval, and then use $\sum_{p>P}p^{-2}\ll P^{-1}$; finitely many small or nonpositive arguments contribute $O_{\mathbf a}(1)$. Keep $P$ fixed, let $X\to\infty$, and then let $P\to\infty$. This proves the claimed product. Summing the finite phase counts before cutoff removal restores $1-\nu_p(E)/p^2$ at each prime, proving [\[eq:phase-sum\]](#eq:phase-sum){reference-type="eqref" reference="eq:phase-sum"}.

The two-odd channel is an already established fixed-data input. RH-393, Theorem 1.1, proves terminal cancellation with arbitrary fixed even square masks for exactly two odd Möbius factors [@RH393]. Its analytic two-form input is RH-392, Theorem 2.2 (printed/PDF page 3) [@RH392]; that result in turn uses Tao's fixed nonparallel two-point theorem, Theorem 2, equation (3), printed/PDF page 3 [@Tao2016LogChowla]. These sources are used only for odd support two, not for higher odd order.

[\[lem:old-channels\]]{#lem:old-channels label="lem:old-channels"} For every fixed periodic $\rho$, disjoint $O,E\subseteq[m]$, and every terminal clock, $$\begin{aligned}
 &\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\leq X}
 \frac{\rho(n)\prod_{i\in O}\mu_0(n-a_i)
 \prod_{j\in E}\mu_0(n-a_j)^2}{n}
 \notag\\
 &\hspace{30mm}\longrightarrow
 \begin{cases}
  \displaystyle\sum_{r\bmod q}\rho(r)\Theta_{q,r}(E),&O=\varnothing,\\
  0,&|O|=2,
 \end{cases}
 \label{eq:old-channels}\end{aligned}$$ when $\rho$ has period $q$.

The first line is Lemma [\[lem:density\]](#lem:density){reference-type="ref" reference="lem:density"}, phase by phase. For the second, fix a prime cutoff and replace the squarefree masks by their finite Boolean approximants. The approximant is periodic and RH-392's two-form terminal input applies because $a_i-a_j\neq0$. The error is bounded by [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}. The order is $P$ fixed, then $X\to\infty$, and only then $P\to\infty$, exactly as in the frozen RH-393 synthesis.

# Positive odd support and the affine phase bridge

The new input is Corollary 1.8 of Tao and Teräväinen (PDF page 7), which gives terminal logarithmic cancellation for fixed distinct shifts and fixed nonzero exponents of odd sum [@TaoTeravainen2019]. We use only positive exponents $1$ and $2$. A periodic phase is not silently absorbed into that corollary: Remark 1.5 (PDF page 7) and its proof in Appendix A, Theorem A.1 (PDF page 38), provide the required fixed affine extension.

[\[lem:odd\]]{#lem:odd label="lem:odd"} Let $O,E\subseteq[m]$ be disjoint and $|O|$ be positive and odd. For every fixed phase $r\bmod q$, $$\frac1{\log\omega(X)}
 \sum_{\substack{X/\omega(X)<n\leq X\\n\equiv r\pmod q}}
 \frac{\prod_{i\in O}\mu_0(n-a_i)
 \prod_{j\in E}\mu_0(n-a_j)^2}{n}\longrightarrow0.
 \label{eq:odd-channel}$$

Write $n=qt+r$, with a fixed representative $r$. Remove the finitely many $t$ for which $t\leq0$ or some affine argument is nonpositive. Let $$Y=\left\lfloor\frac{X-r}{q}\right\rfloor,\qquad
 L=\max\!\left(T,\left\lfloor\frac{X/\omega(X)-r}{q}\right\rfloor\right),
 \qquad \Omega=Y/L,$$ where $T\geq1$ is a fixed cutoff larger than all deleted values. Changing strict endpoints to $L<t\leq Y$ changes the unnormalized weighted sum by $O_{q,\mathbf a}(1)$. If $X/\omega(X)\to\infty$, then $\Omega\asymp\omega(X)$; if the lower endpoint is bounded, then $\Omega\asymp X$ and $\omega(X)\asymp X$. Passing to either type of subsequence gives $$\Omega\longrightarrow\infty,\qquad
 \frac{\log\Omega}{\log\omega(X)}\longrightarrow1.
 \label{eq:clock-transform}$$ The same conclusion holds for an arbitrary sequence after taking a subsequence of one of these two types.

For $t>T$, $$\frac1{qt+r}=\frac1{qt}+O_{q,r}(t^{-2}).
 \label{eq:weight-bridge}$$ The total error is $O_{q,r}(1)$. Thus [\[eq:odd-channel\]](#eq:odd-channel){reference-type="eqref" reference="eq:odd-channel"} equals, up to $o(1)$, $$\frac1{q\log\omega(X)}
 \sum_{Y/\Omega<t\leq Y}\frac1t
 \prod_{i\in O}\mu(qt+r-a_i)
 \prod_{j\in E}\mu(qt+r-a_j)^2.
 \label{eq:affine-window}$$ The affine forms have fixed positive slope $q$ and pairwise-distinct intercepts $r-a_i$; their pairwise determinants are $q(a_i-a_j)\neq0$. Their exponents belong to $\{1,2\}$, and the exponent sum is odd because it is congruent to $|O|\pmod2$. Corollary 1.8, transferred to these fixed forms by Remark 1.5 and Theorem A.1, makes the normalized logarithmic expression tend to zero. More explicitly, $$\sum_{Y/\Omega<t\leq Y}\frac1t=\log\Omega+O(1),
 \qquad \frac{\log\Omega}{\log\omega(X)}\longrightarrow1,$$ so its harmonic denominator divided by $\log\omega(X)$ tends to one. Equation [\[eq:clock-transform\]](#eq:clock-transform){reference-type="eqref" reference="eq:clock-transform"}, the summable error in [\[eq:weight-bridge\]](#eq:weight-bridge){reference-type="eqref" reference="eq:weight-bridge"}, and the endpoint $O(1)$ complete the bridge.

For clarity, the cited corollary is formulated for arbitrary sequences $Y_j,\Omega_j\to\infty$. If the ordinary $X$-limit in [\[eq:odd-channel\]](#eq:odd-channel){reference-type="eqref" reference="eq:odd-channel"} failed, a contradicting sequence $X_j\to\infty$ would, after the preceding subsequence split, produce just such a pair of sequences and contradict the cited result. This sequential criterion pays the all-clock quantifier, including clocks as large as $X$.

Expand [\[eq:polynomial\]](#eq:polynomial){reference-type="eqref" reference="eq:polynomial"} into its finitely many phases and monomials. Lemma [\[lem:density\]](#lem:density){reference-type="ref" reference="lem:density"} evaluates $O=\varnothing$. Lemma [\[lem:old-channels\]](#lem:old-channels){reference-type="ref" reference="lem:old-channels"} cancels $|O|=2$, and Lemma [\[lem:odd\]](#lem:odd){reference-type="ref" reference="lem:odd"} cancels every positive odd $|O|$. This proves [\[eq:compiler-limit\]](#eq:compiler-limit){reference-type="eqref" reference="eq:compiler-limit"} and [\[eq:phase-sum\]](#eq:phase-sum){reference-type="eqref" reference="eq:phase-sum"}.

For the dimension, all-even supports contribute $2^m$, two-odd supports contribute $\binom m2 2^{m-2}$, and positive odd supports contribute $$\sum_{\substack{k\leq m\\k\text{ odd}}}\binom mk2^{m-k}
 =\frac{(2+1)^m-(2-1)^m}{2}=\frac{3^m-1}{2}.$$ The three classes are disjoint, proving [\[eq:dimension\]](#eq:dimension){reference-type="eqref" reference="eq:dimension"}.

# Support strata and intrinsic classification

Every table $f:\{-1,0,+1\}^m\to\mathbb R$ has a unique polynomial interpolant with coordinate degree at most two. Index its coefficient by disjoint sets $O,E$: $$F(z)=\sum_{O\cap E=\varnothing}c_{O,E}
 \prod_{i\in O}z_i\prod_{j\in E}z_j^2.
 \label{eq:OE-interpolant}$$ On the support stratum $S$, write $h_S(\varepsilon)=f(\varepsilon_S,0_{S^c})$, with normalized Boolean Fourier coefficients $\widehat h_S(A)$. Direct restriction of [\[eq:OE-interpolant\]](#eq:OE-interpolant){reference-type="eqref" reference="eq:OE-interpolant"} gives, for $O\subseteq S$, $$\widehat h_S(O)=\sum_{E\subseteq S\setminus O}c_{O,E}.
 \label{eq:stratum-relation}$$ Subset Möbius inversion gives the converse formula $$c_{O,E}=\sum_{U\subseteq E}(-1)^{|E|-|U|}
 \widehat h_{O\cup U}(O).
 \label{eq:stratum-inversion}$$

Equations [\[eq:stratum-relation\]](#eq:stratum-relation){reference-type="eqref" reference="eq:stratum-relation"}--[\[eq:stratum-inversion\]](#eq:stratum-inversion){reference-type="eqref" reference="eq:stratum-inversion"} show that all coefficients with a given odd support $O$ vanish exactly when $\widehat h_S(O)=0$ on every stratum $S\supseteq O$. The inadmissible sets $O$ are precisely the positive even sets of size at least four. Those are precisely the Fourier characters of even parity and degree at least four. Since antipodal symmetrization retains exactly the even characters, admissibility is equivalent to $\deg h_S^+\leq2$ for every $S$.

For the limit formula, note the pointwise identity $$\mathbf 1_{\{\operatorname{supp}(z)=U\}}=
 \prod_{i\in U}z_i^2\prod_{j\notin U}(1-z_j^2).
 \label{eq:exact-support}$$ Its all-even limiting density is exactly the inclusion--exclusion sum [\[eq:pi\]](#eq:pi){reference-type="eqref" reference="eq:pi"}; hence $\Pi_{q,r}(U)\geq0$. Summing [\[eq:exact-support\]](#eq:exact-support){reference-type="eqref" reference="eq:exact-support"} over $U$ gives one, so $\sum_U\Pi_{q,r}(U)=\Theta_{q,r}(\varnothing)=1/q$. Writing the table as the sum of its exact-support expansions, the constant Boolean coefficient on support $U$ is $\overline f_{r,U}$. After the expansions are collected, the intrinsic condition eliminates every inadmissible even character, and all remaining nonconstant channels cancel by Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"}. Summing the finitely many strata and phases proves [\[eq:table-limit\]](#eq:table-limit){reference-type="eqref" reference="eq:table-limit"}.

Formula [\[eq:dimension\]](#eq:dimension){reference-type="eqref" reference="eq:dimension"} gives $D'_3=8+6+13=27$, so no monomial is missing. For $m=4$, it gives $D'_4=16+24+40=80$. The only even odd-support of size at least four is $[4]$, yielding [\[eq:c1111\]](#eq:c1111){reference-type="eqref" reference="eq:c1111"} by the tensor Boolean coefficient formula.

For a sign table, multiply each of the sixteen corner signs by $\varepsilon_1\varepsilon_2\varepsilon_3\varepsilon_4$. Their sum is zero exactly when eight transformed signs are positive and eight are negative, giving $\binom{16}{8}$ corner patterns. The other $3^4-2^4=65$ values are free. Phases are independent, so the one-phase count is raised to the $q$th power.

# Distinguished-current tables

Take $m=d+1$ of the fixed distinct shifts, with the first $d$ as inputs and the last as the distinguished current. In one phase let $f:\{-1,0,+1\}^d\to\{-1,+1\}$ and put $g(x,z)=z f(x)$. For every input support $S$, write $$h_S^-(\varepsilon)=\frac{h_S(\varepsilon)-h_S(-\varepsilon)}2.$$ Multiplication by $z$ raises the odd-support size by one. Thus the score interpolant is admissible exactly when no input character has positive odd degree at least three, or equivalently $$\deg h_S^-\leq1\qquad(S\subseteq[d]).
 \label{eq:current-criterion}$$

[\[thm:current\]]{#thm:current label="thm:current"} Set $M_0=2$, $M_1=4$, and, for $k\geq2$, $$M_k=2^{2^{k-1}}+2k+4\binom{k}{2}\,2^{2^{k-2}}.
 \label{eq:Mk}$$ The number of $d$-input sign tables satisfying [\[eq:current-criterion\]](#eq:current-criterion){reference-type="eqref" reference="eq:current-criterion"} is $$B_d=\prod_{k=0}^d M_k^{\binom{d}{k}}.
 \label{eq:Bd}$$ Choose independently in every phase a table $f_r$ satisfying [\[eq:current-criterion\]](#eq:current-criterion){reference-type="eqref" reference="eq:current-criterion"}. Every one of the $B_d^q$ fixed phase families has terminal average zero after multiplication by the distinguished current; explicitly, $$\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\leq X}
 \frac{\mu_0(n-a_{d+1})}{n}
 f_{n\bmod q}\bigl(\mu_0(n-a_1),\ldots,\mu_0(n-a_d)\bigr)
 \longrightarrow0.
 \label{eq:current-limit}$$ In particular, $$B_2=512,\qquad B_3=36{,}700{,}160,$$ so all $512^q$ two-input phase families cancel.

On a Boolean $k$-stratum, condition [\[eq:current-criterion\]](#eq:current-criterion){reference-type="eqref" reference="eq:current-criterion"} says that $L=h^-$ is linear and takes values in $\{-1,0,1\}$. Write $L(x)=\sum_i a_ix_i$. Flipping coordinate $i$ shows $a_i\in\{0,\pm\tfrac12,\pm1\}$, while $\max|L|=\sum_i|a_i|\leq1$. A lone half coefficient is impossible because its values would be $\pm\tfrac12$; three half coefficients are impossible because a choice of signs gives absolute value at least $3/2$. Consequently $$L=0,\qquad L=\pm x_i,\qquad
 L=\frac{\pm x_i\pm x_j}{2}\quad(i<j),
 \label{eq:L-classification}$$ and these cases are disjoint.

If $L=0$, the table has one free common sign on each of the $2^{k-1}$ antipodal pairs, giving $2^{2^{k-1}}$ choices. The $2k$ dictators force all values. Each of the $4\binom{k}{2}$ paired forms vanishes on $2^{k-2}$ antipodal pairs, whose common signs remain free, giving the third term in [\[eq:Mk\]](#eq:Mk){reference-type="eqref" reference="eq:Mk"}. The case $k=0$ has two constant tables and $k=1$ has four tables. There are $\binom{d}{k}$ independent support strata of size $k$, which proves [\[eq:Bd\]](#eq:Bd){reference-type="eqref" reference="eq:Bd"}; the $q$ phases are independent.

Finally, every monomial of $g=z f$ has the distinguished coordinate to odd exponent one. Under [\[eq:current-criterion\]](#eq:current-criterion){reference-type="eqref" reference="eq:current-criterion"} all such monomials are admitted, and none is all-even. Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"} therefore gives zero.

# Source roles and reproducibility

Within this fixed-data terminal-log framework, the new analytic step is the positive odd-support synthesis in Lemma [\[lem:odd\]](#lem:odd){reference-type="ref" reference="lem:odd"}. Tao and Teräväinen are the only new direct analytic source. RH-393 is the direct frozen predecessor for the exact all-even formula and the two-odd-factor channel; RH-392 and Tao's 2016 theorem are inherited two-point provenance. No global priority claim is made, and neither the Johnston--Yang nor the Maynard closure object is used as a proof input.

The companion certificate contains finite monomial, signed-cube, distinguished-current, phase-inversion, source, and firewall checks. It is a reproduction and regression artifact, not an analytic proof. The immutable source closure has $128$ Git objects and four ordered remote logical objects, for $132$ objects in total. In the order Johnston--Yang, Maynard, Tao 2016, and Tao--Teräväinen, the recorded release-redistribution flags are respectively no, no, yes, and no. All four external PDFs remain nonvendored by project policy; the build is offline by default, and all six sealed external payload identities are excluded from the release tree.

# Limitations

The theorem does not cover an even odd-support size at least four. In particular, it does not establish unrestricted table laws once $m\geq4$, and failure of the four-cube test means only "outside this theorem." All of $m,q$, the shifts, masks, phase coefficients, and the clock are fixed; there is no uniform effective rate or growing-data conclusion. Nothing is claimed for ordinary Cesàro averages, a maximum taken before the terminal limit, adaptive or generic graph-coupled capacity, or any operator, trace, zero, Riemann-hypothesis, or Gates A--E construction.

# Declarations {#declarations .unnumbered}

**Data availability.** The finite certificate, exact result and schema, source-lock metadata, and offline verification code are included in the accompanying RH-394 package. No new empirical data were generated and no external source PDF is redistributed.

**Ethics declaration.** This mathematical study involved no human participants, animals, personal data, or sensitive datasets; institutional ethics approval was not applicable.

**Author contributions (CRediT).** The RH research program performed conceptualization, formal analysis, methodology, software, validation, and writing (original draft, review, and editing).

**Conflict of interest.** The author declares no conflict of interest.

**Funding.** No external funding was received for this work.

**AI-use statement.** AI-assisted tools supported drafting, finite-certificate implementation, formatting, and consistency checks. The research program directed and reviewed the mathematical arguments, source roles, and release artifacts and retains responsibility for the content.
