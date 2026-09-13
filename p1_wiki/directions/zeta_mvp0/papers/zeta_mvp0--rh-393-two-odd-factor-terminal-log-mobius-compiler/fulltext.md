---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-393-two-odd-factor-terminal-log-mobius-compiler"
canonical_tex: "zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler/main.pdf"
source_sha256: "d153d9b9597142d42c0d59905534eb57c81b503883ff3a3085d2b32823a1002c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Odd-Factor Terminal-Log Möbius Compiler and the Multi-Shift Squarefree Landscape

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-393-two-odd-factor-terminal-log-mobius-compiler/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For any fixed finite set of distinct integer shifts, we diagonalize terminal logarithmic averages of coordinatewise-quadratic Möbius polynomials whose monomials contain at most two odd exponents. The total polynomial degree may be as large as twice the number of shifts. All channels with one or two odd Möbius factors vanish; the surviving all-even channels are exact multi-shift squarefree phase densities. Their Euler factors retain the collision distinction between congruence classes modulo $p$ and modulo $p^2$.

  The proof combines a local finite-CRT calculation with a uniform Boolean square-mask tail. After fixing the cutoff, one odd factor is handled by the frozen periodic one-form cancellation in RH-392 and two odd factors by its arbitrary-nonzero-determinant terminal theorem. The order of limits is cutoff fixed, terminal limit, and then cutoff removal. In three variables the compiler contains $26$ of the $27$ ternary interpolation monomials; the sole excluded coefficient is the signed-cube coefficient $c_{111}$. This gives a concrete cancellation class of exactly $192$ among the $512$ two-input truth tables used in a distinguished-current score.

  We also determine the global squarefree-density landscape. For at most three shifts it has a positive sharp lower product, with equality exactly when all pairwise differences are squarefree. From four shifts onward zero is attained precisely through a complete residue cover modulo some $p^2$. For every fixed number of at least two shifts the supremum is $6/\pi^2$, approached but never attained. Every datum is fixed before the terminal limit; no higher odd correlation, growing family, ordinary Cesàro, or multishift safe-table capacity is claimed.
author:
- RH research program
bibliography:
- references.bib
date: 'August 10, 2026'
title: 'Two-Odd-Factor Terminal-Log Möbius Compiler and the Multi-Shift Squarefree Landscape'
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; squarefree patterns; finite Chinese remainder theorem; ternary interpolation.

# Definitions and main results

Write $\mu_0(t)=\mu(t)$ for integers $t\ge1$, and $\mu_0(t)=0$ for $t\le0$. A terminal clock is a function satisfying $$1\le \omega(X)\le X,\qquad \omega(X)\longrightarrow\infty.
 \label{eq:clock}$$ Fix integers $m,q\ge1$, pairwise-distinct integer shifts $a_1,\ldots,a_m$, and fixed $q$-periodic coefficients $c_\alpha(r)$. All these data, including the clock, are fixed before $X\to\infty$. Put $$z_i(n)=\mu_0(n-a_i),\qquad
 O(\alpha)=\{i:\alpha_i=1\},\qquad
 E(\alpha)=\{i:\alpha_i=2\}.$$ For polynomials $$P_r(z)=\sum_{\substack{\alpha\in\{0,1,2\}^m\\|O(\alpha)|\le2}}
 c_\alpha(r)\prod_{i=1}^m z_i^{\alpha_i},
 \label{eq:poly}$$ define the terminal functional $$T_X(P;\omega)=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\le X}\frac{P_{n\bmod q}(z_1(n),\ldots,z_m(n))}{n}.
 \label{eq:functional}$$

For $E\subseteq\{1,\ldots,m\}$, let $$B_p(E)=\{a_i\bmod p^2:i\in E\},\quad
 \nu_p(E)=|B_p(E)|,
 \quad \tau_{p,E}(r)=|\{b\in B_p(E):b\equiv r\pmod p\}|.
 \label{eq:local-data}$$ The braces in $B_p(E)$ are essential: residues are first deduplicated modulo $p^2$, while two distinct such residues may still collide modulo $p$. Define $$\begin{aligned}
 \Theta_{q,r}(E)
  &=\frac1q\prod_{p\nmid q}\left(1-\frac{\nu_p(E)}{p^2}\right)
    \prod_{p\parallel q}\left(1-\frac{\tau_{p,E}(r)}p\right)
    \prod_{p^2\mid q}\mathbf 1_{\{r\bmod p^2\notin B_p(E)\}},
 \label{eq:theta}\\
 \kappa_E&=\prod_p\left(1-\frac{\nu_p(E)}{p^2}\right).
 \label{eq:kappa}\end{aligned}$$ Thus $\Theta_{q,r}(\varnothing)=1/q$.

[\[thm:compiler\]]{#thm:compiler label="thm:compiler"} For every fixed datum above and every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, $$T_X(P;\omega)\longrightarrow
 \sum_{r\bmod q}\ \sum_{\alpha\in\{0,2\}^m}
 c_\alpha(r)\Theta_{q,r}(E(\alpha)).
 \label{eq:compiler}$$ Every admissible monomial with one or two odd exponents vanishes. The all-even channels are the only survivors, and $$\sum_{r\bmod q}\Theta_{q,r}(E)=\kappa_E.
 \label{eq:phase-sum}$$

The number of admitted monomials is $$D_m=2^m+m2^{m-1}+\binom m2 2^{m-2},
 \label{eq:dimension}$$ where terms with impossible support sizes are interpreted as zero. In particular, $D_3=26$: only $z_1z_2z_3$ is absent.

[\[cor:c111\]]{#cor:c111 label="cor:c111"} Let $f:\{-1,0,+1\}^3\to\mathbb R$, and let its unique coordinatewise-quadratic interpolant have coefficient $c_{111}(f)$. Then $$c_{111}(f)=\frac18\sum_{\varepsilon\in\{-1,+1\}^3}
 \varepsilon_1\varepsilon_2\varepsilon_3f(\varepsilon).
 \label{eq:c111}$$ The interpolant is covered by Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"} exactly when $c_{111}(f)=0$.

[\[cor:192\]]{#cor:192 label="cor:192"} Fix three distinct shifts and, in every phase $r$, a table $f_r:\{-1,0,+1\}^2\to\{-1,+1\}$ satisfying $$f_r(1,1)-f_r(1,-1)-f_r(-1,1)+f_r(-1,-1)=0.
 \label{eq:corner}$$ Then, for every terminal clock, $$\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\le X}
 \frac{\mu_0(n-a_3)
 f_{n\bmod q}(\mu_0(n-a_1),\mu_0(n-a_2))}{n}
 \longrightarrow0.
 \label{eq:table-limit}$$ Exactly $192$ of the $512$ tables satisfy [\[eq:corner\]](#eq:corner){reference-type="eqref" reference="eq:corner"}. The other $320$ tables are outside this theorem; no assertion about their limits is made.

For a finite set $A=\{a_1,\ldots,a_m\}$ of distinct integers, write $$\kappa_A=\prod_p\left(1-\frac{|A\bmod p^2|}{p^2}\right).
 \label{eq:global-kappa}$$

[\[thm:landscape\]]{#thm:landscape label="thm:landscape"} The following statements hold.

1.  If $1\le m\le3$, then $$\kappa_A\ge C_m:=\prod_p(1-mp^{-2})>0.$$ Equality holds exactly when every nonzero pairwise difference in $A$ is squarefree. The set $\{0,\ldots,m-1\}$ is a witness.

2.  If $m\ge4$, then $\inf_A\kappa_A=0$, and zero is attained. More precisely, $\kappa_A=0$ exactly when $A\bmod p^2$ covers all $p^2$ residues for some prime $p$. The residues $0,1,2,3\pmod4$, extended by arbitrary distinct shifts, give a witness for every $m\ge4$.

3.  For $m=1$, $\kappa_A=6/\pi^2$. For each fixed $m\ge2$, $$\sup_A\kappa_A=\frac6{\pi^2},$$ but the supremum is not attained.

An individual phase density $\Theta_{q,r}(E)$ may vanish even when $\kappa_E>0$.

# Squarefree phase densities {#sec:density}

[\[lem:finite-crt\]]{#lem:finite-crt label="lem:finite-crt"} Let $\mathcal P$ be a finite set of primes containing every prime divisor of $q$, and put $M=\mathop{\mathrm{lcm}}(q,\prod_{p\in\mathcal P}p^2)$. The density in the phase $n\equiv r\pmod q$ of integers avoiding $n\equiv a_i\pmod{p^2}$, for all $i\in E$ and $p\in\mathcal P$, equals the finite truncation of [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}. Summing these phase densities over $r\pmod q$ gives $\prod_{p\in\mathcal P}(1-\nu_p(E)/p^2)$.

Count directly in one complete block modulo $M$. The Chinese remainder theorem separates the prime-square coordinates. If $p\nmid q$, exactly $\nu_p(E)$ of the $p^2$ residues are forbidden. If $p\parallel q$, the fixed residue modulo $p$ leaves $p$ lifts, of which $\tau_{p,E}(r)$ are forbidden. If $p^2\mid q$, the phase is either forced into a forbidden class or avoids all of them. These are the three factors in [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}. Summing over the compatible phase coordinates restores the unrestricted factor at every prime.

[\[lem:tail\]]{#lem:tail label="lem:tail"} For fixed shifts and a cutoff $P$, the terminal harmonic mass on which at least one $n-a_i$, $i\in E$, is divisible by $p^2$ for some prime $p>P$ is $$O_{m,\mathbf a}\!\left(\frac{\log\omega(X)}P+1\right).
 \label{eq:tail}$$ The corresponding prefix counting error is $O_{m,\mathbf a}(N/P+\sqrt N)$.

For the prefix bound, sum $N/p^2+1$ over $P<p\le\sqrt{N+\max_i|a_i|}$, and use a union bound over the fixed set of shifts. For the terminal bound, split $(X/\omega(X),X]$ into dyadic blocks. On a block $(T,2T]$, each progression contributes $O(T/p^2+1)$ points, each of weight $O(1/T)$. Summation over primes and then over the dyadic blocks gives [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}; blocks meeting the fixed lower endpoint contribute only $O_{m,\mathbf a}(1)$. The implied constants may depend on the fixed shifts, but not on $X$ or $P$.

[\[prop:theta\]]{#prop:theta label="prop:theta"} The density of integers $n\equiv r\pmod q$ for which every $n-a_i$, $i\in E$, is squarefree exists and equals $\Theta_{q,r}(E)$ in [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}.

Lemma [\[lem:finite-crt\]](#lem:finite-crt){reference-type="ref" reference="lem:finite-crt"} gives the result with finitely many local conditions. Lemma [\[lem:tail\]](#lem:tail){reference-type="ref" reference="lem:tail"} removes the remaining prime squares. First let $N\to\infty$ with $P$ fixed, and then let $P\to\infty$. The same argument after summing phases proves [\[eq:phase-sum\]](#eq:phase-sum){reference-type="eqref" reference="eq:phase-sum"}. This is a local proof; Mirsky's classical pattern theorem is historical context, not an invoked black box [@Mirsky1948].

# Cancellation with square masks {#sec:cancellation}

We use two frozen inputs from RH-392. Its equation (19), on printed/PDF page 5, gives the prefix estimate $\sum_{n\le N}\mu_0(n-a)\rho(n)=o(N)$ for every fixed periodic $\rho$ and fixed integer shift $a$. RH-392, Lemma 2.1, transfers this prefix estimate to every terminal clock, giving $$\sum_{X/\omega(X)<n\le X}\frac{\mu_0(n-a)\rho(n)}n
 =o(\log\omega(X)).
 \label{eq:one-form}$$ Its Theorem 2.2 on printed/PDF page 3 gives the analogous terminal statement for the product of two fixed positive-leading affine forms of arbitrary nonzero determinant [@RH392]. The latter ultimately uses Tao's fixed nonparallel two-point logarithmic theorem [@Tao2016LogChowla]; the one-form input rests on Davenport's classical estimate [@Davenport1937]. TPC-137 is only a determinant-two proof blueprint and is not being promoted to an arbitrary-determinant theorem [@TPC137].

[\[lem:masked\]]{#lem:masked label="lem:masked"} Fix $O,E\subseteq\{1,\ldots,m\}$, with $O\cap E=\varnothing$, and a fixed periodic $\rho$. If $1\le|O|\le2$, then $$\frac1{\log\omega(X)}\sum_{X/\omega(X)<n\le X}
 \frac{\rho(n)\prod_{i\in O}\mu_0(n-a_i)
       \prod_{j\in E}\mu_0(n-a_j)^2}{n}\longrightarrow0.
 \label{eq:masked}$$

Fix $P$ and replace each squarefree indicator in the even support by the finite Boolean condition excluding $p^2\mid n-a_j$ for $p\le P$. The product is then periodic, so it may be absorbed into $\rho$. If $|O|=1$, equation [\[eq:one-form\]](#eq:one-form){reference-type="eqref" reference="eq:one-form"} applies. If $|O|=2$, the two forms $n-a_i$ and $n-a_j$ have determinant $a_i-a_j\ne0$, because the shifts are distinct, and RH-392, Theorem 2.2 applies. Values with a nonpositive argument affect only finitely many terms.

Lemma [\[lem:tail\]](#lem:tail){reference-type="ref" reference="lem:tail"} bounds the unnormalized replacement error by $O_{m,\mathbf a}(\|\rho\|_\infty(\log\omega/P+1))$. After division by $\log\omega$, keep $P$ fixed and let $X\to\infty$, then let $P\to\infty$. This proves [\[eq:masked\]](#eq:masked){reference-type="eqref" reference="eq:masked"}. The fixed-data order is indispensable: neither frozen input supplies a rate uniform in growing shifts, periods, or masks.

Expand [\[eq:poly\]](#eq:poly){reference-type="eqref" reference="eq:poly"}. When $O(\alpha)=\varnothing$, the monomial is the indicator that all shifts indexed by $E(\alpha)$ are squarefree. Proposition [\[prop:theta\]](#prop:theta){reference-type="ref" reference="prop:theta"} and terminal Abel summation give its limit $\Theta_{q,r}(E(\alpha))$ in phase $r$. When the odd support has size one or two, Lemma [\[lem:masked\]](#lem:masked){reference-type="ref" reference="lem:masked"} gives zero. There are finitely many phases and monomials, so the limits may be summed. Counting the choices of zero/two exponents outside an odd support of size $0,1,2$ gives [\[eq:dimension\]](#eq:dimension){reference-type="eqref" reference="eq:dimension"}.

For completeness, the terminal Abel step used above follows from partial summation: if $A(t)=\alpha t+o(t)$ for a bounded sequence, then its harmonic mean over $(X/\omega(X),X]$, divided by $\log\omega(X)$, tends to $\alpha$. When the lower endpoint remains bounded, split at a fixed large threshold; then $\log X/\log\omega(X)\to1$.

# Interpolation and the 192-table class

The one-variable coefficient of $x$ in quadratic interpolation on $\{-1,0,+1\}$ is $(f(1)-f(-1))/2$. Taking the tensor product in three coordinates yields [\[eq:c111\]](#eq:c111){reference-type="eqref" reference="eq:c111"}. Among the $27$ exponent vectors in $\{0,1,2\}^3$, the only one with three odd entries is $(1,1,1)$. Consequently its vanishing is necessary and sufficient for the whole interpolant to lie in the compiler.

Put $g(x,y,z)=z f(x,y)$. Tensor interpolation gives $c_{111}(g)=c_{11}(f)$, and $$c_{11}(f)=\frac14\{f(1,1)-f(1,-1)-f(-1,1)+f(-1,-1)\}.$$ If [\[eq:corner\]](#eq:corner){reference-type="eqref" reference="eq:corner"} holds, every monomial of $g$ has one or two odd exponents; it therefore vanishes by Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"}. For the census, multiply the four corner signs by their alternating weights. Their sum is zero exactly when two of the four transformed signs are positive, giving $\binom42=6$ corner patterns. The five noncorner values are free, so the count is $6\cdot2^5=192$.

# Proof of the density landscape

Write $\nu_p=|A\bmod p^2|$. If $m\le3$, then $1-\nu_p/p^2\ge1-m/p^2>0$. Equality in the product holds exactly when $\nu_p=m$ for every prime, which is equivalent to no nonzero pairwise difference being divisible by a prime square. This proves part (i), and the displayed witness has only the squarefree differences $1$ and $2$.

Because $\sum_p\nu_p/p^2<\infty$, an Euler product [\[eq:global-kappa\]](#eq:global-kappa){reference-type="eqref" reference="eq:global-kappa"} can vanish only through a zero local factor. Such a factor is precisely a complete cover of the $p^2$ residues. The four residues modulo $4$ give the asserted witness, and adding distinct shifts preserves the cover. This proves part (ii).

Since $\nu_p\ge1$, one always has $\kappa_A\le\prod_p(1-p^{-2})=6/\pi^2$. For $m\ge2$, choose a nonzero difference $d$. Some prime does not divide $d$, so $\nu_p\ge2$ at that prime and the inequality is strict. To approach the upper value, set $$Q_y=\prod_{p\le y}p^2,\qquad A_{m,y}=\{jQ_y:0\le j<m\}.$$ For $p\le y$, all shifts coincide modulo $p^2$, so $\nu_p=1$. Once every $p>y$ has $p^2>m$, $$\prod_{p\le y}(1-p^{-2})\prod_{p>y}(1-mp^{-2})
 \le\kappa_{A_{m,y}}\le\frac6{\pi^2}.$$ The second product on the left tends to one, proving the supremum claim. For $m=1$, every $\nu_p=1$, so equality is attained. Finally, a phase indicator in [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"} can vanish because of a forced residue even when the global Euler product is positive; for example, this occurs for shifts $\{0,2\}$, $q=2$, in the even phase.

# Provenance, reproducibility, and scope

The analytic advance here is a finite-mask synthesis, not a new higher-order Möbius input. RH-392 proves the one- and two-odd-factor terminal cancellations used in Lemma [\[lem:masked\]](#lem:masked){reference-type="ref" reference="lem:masked"}; the present paper adds arbitrarily many fixed even square masks, the full multi-shift phase formula, the sharp density landscape, and the $26/27$ and $192/512$ compiler consequences. The lineage through Tao, Davenport, Mirsky, and TPC-137 is recorded with the restricted roles stated above [@Tao2016LogChowla; @Davenport1937; @Mirsky1948; @TPC137].

The companion certificate enumerates $576$ finite rows: $512$ truth tables, $27$ three-variable monomials, eight dimension rows, twelve finite-CRT fixtures, nine landscape rows, and eight analytic-contract rows. It is a finite reproduction and regression oracle, not the analytic proof. The immutable closure contains $117$ Git objects and three ordered remote logical objects, hence $120$ logical sources. Its ordered all-Git digest is `2c187ec15a427ffb0b06a48679f8419be82152fe16ea914c2a86437549117220`, and its logical digest is `9315d7c01651ed8b4d94f98c3e4019ad11e28469ee6722903721db280b9f92eb`. Tao is the only remote analytic provenance: the locator is Theorem 2, equation (3), printed/PDF page 3, DOI `10.1017/fmp.2016.6`; the Cambridge version is CC BY 4.0 but remains nonvendored by project policy. The Johnston--Yang and Maynard remote objects are closure-only and are conservatively marked nonredistributable. All three offline verifiers make zero network requests by default. No remote PDF is vendored, and five inherited payload identities are excluded from both the package members and the full tree. RH-393 adds no new remote source.

The theorem does not cover monomials with three or more odd exponents, unrestricted three-coordinate truth tables, or a generic multishift safe-table capacity. It gives no result for growing $m$, $q$, shifts, periodic masks, or $X$-dependent coefficients; no effective uniform rate, ordinary Cesàro average, maximum-before-limit, or adaptive capacity is asserted. Nothing here supplies an operator model, trace formula, zero model, or any of Gates A--E.

# Limitations

The fixed-data restriction is qualitative and essential. The cutoff argument loses all uniformity as the number of masks, the shifts, or the period grows. The first excluded monomial in three variables is exactly a three-point unsquared Möbius correlation; neither RH-392 nor Tao's two-point theorem controls it. The $192$-table corollary is therefore a genuine but deliberately typed subclass, not evidence that the remaining $320$ tables converge or have nonzero limits. The density landscape is an arithmetic statement about fixed configurations and does not optimize a global compatibility problem among several lag constraints.

# Declarations {#declarations .unnumbered}

**Data availability.** All finite data, source-lock metadata, exact schemas, and verification code used in this work are included in the accompanying repository package. No external payload is redistributed.

**Ethics declaration.** This mathematical study uses no human participants, animals, personal data, or sensitive datasets; institutional ethics approval was not applicable.

**Author contributions (CRediT).** The RH research program performed conceptualization, formal analysis, methodology, software, validation, visualization-free presentation, and writing (original draft, review, and editing).

**Conflict of interest.** The author declares no conflict of interest.

**Funding.** No external funding was received for this work.

**AI-use statement.** AI-assisted tools supported drafting, finite-certificate implementation, and consistency checks. Every theorem statement, proof dependency, citation role, and released byte identity was independently audited; the RH research program retains responsibility for the content.
