---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-384-prime-tail-scale-separation"
canonical_tex: "zeta_mvp0/papers/RH-384-prime-tail-scale-separation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-384-prime-tail-scale-separation/main.pdf"
source_sha256: "f38a39739ec472c3d0c846638739e9e5cb57b6679f60f8f90ba1e2a6188186ef"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Prime-Tail Scale Separation below the Quadratic Square-Clock Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-384-prime-tail-scale-separation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-384-prime-tail-scale-separation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-384-prime-tail-scale-separation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-384-prime-tail-scale-separation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-384-prime-tail-scale-separation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the square-clock sequence $q_y=4\prod_{i\le y}p_i^2$, where $3=p_1<p_2<\cdots$ are the odd primes, define the strict prime tails $$P_r(y)=\sum_{p>p_y}\frac{1}{(p^2-1)^r},\qquad
   T_y=P_1(y),\qquad S_y=P_2(y).$$ We prove from the prime number theorem and strict Stieltjes partial summation that, for every fixed integer $r\ge1$, $$P_r(y)\sim\frac{1}{(2r-1)p_y^{2r-1}\log p_y}.$$ Consequently, for each fixed partition $\lambda=1^{k_1}\cdots d^{k_d}$ of degree $d$ and length $\ell$, $$\prod_rP_r(y)^{k_r}
   \sim\prod_r(2r-1)^{-k_r}
   p_y^{-(2d-\ell)}(\log p_y)^{-\ell}.$$ In particular $T_y^3=o(S_y)$ and $S_y=o(T_y^2)$, with $S_y/[T_y^3(\log p_y)^2]\to1/3$.

  Combining this scale dictionary with the exact RH-382 input $$B_\infty-G(q_y)=A T_y+B T_y^2+C S_y+O(T_y^3)$$ gives five normalized gap limits, including two equivalent normalizations of the independent $S_y$ coefficient and a logarithmically amplified third-order residual. The subtractions remain the exact intrinsic terms $A T_y$ and $B T_y^2$: bare prime-number-theorem equivalents cannot be substituted at the smaller scales. A precision-$80$ directed-rounding certificate proves $$1.5463476716710499204
   \le Y_\infty-2m_\infty
   \le1.5484488989771761113,$$ so $C=(Y_\infty-2m_\infty)/\pi^2>0$. Hence the twice-subtracted residual is eventually positive and its quotient by $T_y^3$ tends to $+\infty$, without an effective threshold. The result is confined to fixed $r$, fixed partitions, fixed finite clocks before the prefix limit, and the universally safe phasewise class with $c_{11}=0$. It constructs no operator or zeta-divisor identity and has no implication for the Riemann hypothesis.
author:
- RH research program
bibliography:
- references.bib
date: 'August 8, 2026'
title: 'Prime-Tail Scale Separation below the Quadratic Square-Clock Gap'
```

## Markdown 正文

**Keywords:** prime number theorem; Abel summation; prime-square Euler tails; fixed partitions; scale separation; finite clocks.

# Frozen class, strict tails, and inherited input

We work only in the fixed finite-clock class established in the preceding square-clock papers [@RH374; @RH379; @RH380; @RH381; @RH382; @RH383]. Fix the clock $q$ before sending the prefix length $N$ to infinity. At every phase $a\in\mathbb Z/q\mathbb Z$, the sign rule depends on $(\mu(n-2),\mu(n))\in\{-1,0,1\}^2$, is universally distance-two-safe, and has vanishing phasewise interpolation coefficient $c_{11}(a)$. The resulting optimum is $G(q)$. An active $c_{11}$ would expose an uncontrolled phase-weighted shift-two Möbius correlation and is not admitted.

Let $$3=p_1<p_2<\cdots,\qquad
 q_y=4\prod_{i\le y}p_i^2,\qquad
 a_{j+1}=\frac{1}{p_{j+1}^2-1}.$$ The intrinsic power-sum coordinates introduced in RH-383 are $$P_r(y)=\sum_{j\ge y}a_{j+1}^r
       =\sum_{\substack{p\ \mathrm{prime}\\p>p_y}}
        \frac{1}{(p^2-1)^r},
 \qquad T_y=P_1(y),\qquad S_y=P_2(y).
 \label{eq:tails}$$ Thus the endpoint is strict, and the first atom is at $p_{y+1}$. Absolute convergence makes the exact successor identity $$P_r(y)=\frac{1}{(p_{y+1}^2-1)^r}+P_r(y+1)
 \label{eq:successor}$$ valid for every $r\ge1$ and $y\ge1$.

Define the limiting Euler ratios $$u_m=\prod_{p\ \mathrm{odd}}\frac{p^2-m}{p^2-1}
 \qquad(2\le m\le8)$$ and the three inherited linear forms $$\begin{aligned}
 X_\infty&=2u_4-4u_5+6u_6-8u_7+10u_8,\\
 Y_\infty&=6u_4-16u_5+30u_6-48u_7+70u_8,\\
 m_\infty&=2u_3-4u_4+6u_5-8u_6+10u_7-12u_8.
 \label{eq:XYm}\end{aligned}$$ RH-382 proves, within the frozen class and after the fixed-clock prefix limit has been taken, $$\Delta_y:=B_\infty-G(q_y)
 =A T_y+B T_y^2+C S_y+O(T_y^3),
 \label{eq:rh382-input}$$ where $$A=\frac{2X_\infty}{\pi^2},\qquad
 B=\frac{Y_\infty+2m_\infty}{\pi^2},\qquad
 C=\frac{Y_\infty-2m_\infty}{\pi^2}.
 \label{eq:ABC}$$ Equation [\[eq:rh382-input\]](#eq:rh382-input){reference-type="eqref" reference="eq:rh382-input"} is an immutable predecessor theorem, not a conclusion fitted from the finite rows in Section [6](#sec:artifact){reference-type="ref" reference="sec:artifact"}.

The prime-counting input is the classical prime number theorem $$\pi(x)\sim\frac{x}{\log x},
 \label{eq:pnt}$$ for which we use Montgomery and Vaughan, Chapter 6 [@MontgomeryVaughan2007]. The repository provenance for this exact input is the frozen RH-2 release [@RH2]; later Möbius/Mertens consequences are not treated as a substitute prime-counting source.

# Fixed-r Abel asymptotics

The boundary term in partial summation is decisive for the leading constant. We record it before making any approximation.

[\[lem:stieltjes\]]{#lem:stieltjes label="lem:stieltjes"} For $x=p_y$, $r\ge1$, and $f_r(t)=(t^2-1)^{-r}$, $$P_r(y)=\int_{(x,\infty)}f_r(t)\,d\pi(t)
 =-\frac{\pi(x)}{(x^2-1)^r}
   -\int_x^\infty \pi(t)f_r'(t)\,dt.
 \label{eq:stieltjes}$$ In particular, the negative endpoint term is present because the sum is over $p>x$.

Apply Stieltjes integration by parts on $(x,R]$. Since $f_r(R)\pi(R)=O(R^{1-2r})\to0$, passage to $R\to\infty$ gives [\[eq:stieltjes\]](#eq:stieltjes){reference-type="eqref" reference="eq:stieltjes"}. The value $\pi(x)$ in the boundary term removes the atom at $x$ and therefore implements the strict endpoint.

[\[thm:fixed-r\]]{#thm:fixed-r label="thm:fixed-r"} For every fixed integer $r\ge1$, $$\boxed{
 P_r(y)\sim
 \frac{1}{(2r-1)p_y^{2r-1}\log p_y}}
 \qquad(y\to\infty).
 \label{eq:fixed-r}$$ No assertion of uniformity in a growing $r$ is made.

Put $x=p_y$ and $s=2r$. For fixed $r$, $$(p^2-1)^{-r}-p^{-2r}=O_r(p^{-2r-2}),$$ uniformly over primes $p>x$. Hence $$P_r(y)-\sum_{p>x}p^{-s}
 =O_r\!\left(\sum_{n>x}n^{-s-2}\right)
 =O_r(x^{-s-1})
 =o\!\left(\frac{x^{1-s}}{\log x}\right).
 \label{eq:weight-reduction}$$ Partial summation, equivalently Lemma [\[lem:stieltjes\]](#lem:stieltjes){reference-type="ref" reference="lem:stieltjes"} for $t^{-s}$, gives the exact strict identity $$\sum_{p>x}p^{-s}
 =-\pi(x)x^{-s}+s\int_x^\infty\pi(t)t^{-s-1}\,dt.
 \label{eq:abel-power}$$

Set $g(t)=t/\log t$ and $$\varepsilon_x=\sup_{t\ge x}
 \left|\frac{\pi(t)}{g(t)}-1\right|.$$ The PNT implies $\varepsilon_x\to0$. This tail supremum is the needed uniformization: the error in replacing $\pi(t)$ by $g(t)$ in the integral of [\[eq:abel-power\]](#eq:abel-power){reference-type="eqref" reference="eq:abel-power"} is at most $$s\varepsilon_x\int_x^\infty\frac{t^{-s}}{\log t}\,dt.$$ For fixed $s>1$, integration by parts (or l'Hôpital's rule) gives $$I_s(x):=\int_x^\infty\frac{t^{-s}}{\log t}\,dt
 \sim\frac{x^{1-s}}{(s-1)\log x}.
 \label{eq:Is}$$ Substitution in [\[eq:abel-power\]](#eq:abel-power){reference-type="eqref" reference="eq:abel-power"} therefore yields $$\sum_{p>x}p^{-s}
 =\left(-1+\frac{s}{s-1}+o(1)\right)
   \frac{x^{1-s}}{\log x}
 =\left(\frac{1}{s-1}+o(1)\right)
   \frac{x^{1-s}}{\log x}.$$ Combining this with [\[eq:weight-reduction\]](#eq:weight-reduction){reference-type="eqref" reference="eq:weight-reduction"} and $s=2r$ proves [\[eq:fixed-r\]](#eq:fixed-r){reference-type="eqref" reference="eq:fixed-r"}. The negative Abel boundary is precisely what changes $2r/(2r-1)$ into $1/(2r-1)$.

Replacing $p>p_y$ by $p\ge p_y$ adds one atom of order $p_y^{-2r}$, which is smaller than the main tail by a factor of order $\log p_y/p_y$. Likewise $p_{y+1}/p_y\to1$ follows from the PNT. Thus the leading equivalent [\[eq:fixed-r\]](#eq:fixed-r){reference-type="eqref" reference="eq:fixed-r"} cannot reject either an inclusive endpoint or an RHS written at $p_{y+1}$. The strict convention and first atom in [\[eq:successor\]](#eq:successor){reference-type="eqref" reference="eq:successor"} are frozen by exact membership identities; they are not advertised as distinct leading asymptotics.

# Fixed partitions and the scale dictionary

Let $\lambda=1^{k_1}\cdots d^{k_d}$ be a fixed partition, with degree and length $$|\lambda|=\sum_{r=1}^d rk_r=d,
 \qquad \ell(\lambda)=\sum_{r=1}^d k_r=\ell,$$ and put $P_\lambda(y)=\prod_rP_r(y)^{k_r}$.

[\[cor:partition\]]{#cor:partition label="cor:partition"} For every fixed partition $\lambda$, $$\boxed{
 P_\lambda(y)\sim
 \left(\prod_r(2r-1)^{-k_r}\right)
 p_y^{-(2d-\ell)}(\log p_y)^{-\ell}.}
 \label{eq:partition}$$

Multiply the finitely many fixed-$r$ equivalents in Theorem [\[thm:fixed-r\]](#thm:fixed-r){reference-type="ref" reference="thm:fixed-r"}. The exponent identity is $\sum_r(2r-1)k_r=2d-\ell$, while the logarithmic exponent is $\sum_rk_r=\ell$.

The corollary is pointwise in $\lambda$. It does not license a partition degree or length which grows with $y$. For $T_y=P_1(y)$ and $S_y=P_2(y)$ it gives the complete scale ledger needed below.

[\[prop:scales\]]{#prop:scales label="prop:scales"} As $y\to\infty$, $$\begin{aligned}
 p_y\log p_y\,T_y&\longrightarrow1,
 \label{eq:scale1}\\
 3p_y^3\log p_y\,S_y&\longrightarrow1,
 \label{eq:scale2}\\
 \frac{S_y}{T_y^2}&\longrightarrow0,
 \label{eq:scale3}\\
 \frac{T_y^3}{S_y}&\longrightarrow0,
 \label{eq:scale4}\\
 \frac{S_y}{T_y^3(\log p_y)^2}&\longrightarrow\frac13.
 \label{eq:scale5}\end{aligned}$$ More explicitly, the last three comparisons have equivalents $$\frac{S_y}{T_y^2}\sim\frac{\log p_y}{3p_y},\qquad
 \frac{T_y^3}{S_y}\sim\frac{3}{(\log p_y)^2},\qquad
 \frac{S_y}{T_y^3(\log p_y)^2}\sim\frac13.$$

Theorem [\[thm:fixed-r\]](#thm:fixed-r){reference-type="ref" reference="thm:fixed-r"} gives $T_y\sim[p_y\log p_y]^{-1}$ and $S_y\sim[3p_y^3\log p_y]^{-1}$. The displayed relations follow by division.

In particular, $S_y$ lies strictly between the two quadratic/cubic monomials on the asymptotic scale: $$T_y^3=o(S_y),\qquad S_y=o(T_y^2).
 \label{eq:scale-order}$$ The $P_2$ term in [\[eq:rh382-input\]](#eq:rh382-input){reference-type="eqref" reference="eq:rh382-input"} is therefore an independent intermediate scale; it cannot be absorbed into either adjacent monomial.

# Five normalized square-clock gap limits

We now combine only the exact predecessor expansion [\[eq:rh382-input\]](#eq:rh382-input){reference-type="eqref" reference="eq:rh382-input"} and Proposition [\[prop:scales\]](#prop:scales){reference-type="ref" reference="prop:scales"}.

[\[thm:gap-limits\]]{#thm:gap-limits label="thm:gap-limits"} Within the frozen phasewise class, $$\begin{aligned}
 p_y\log p_y\,\Delta_y&\longrightarrow A,
 \label{eq:L1}\\
 (p_y\log p_y)^2(\Delta_y-A T_y)&\longrightarrow B,
 \label{eq:L2}\\
 \frac{\Delta_y-A T_y-BT_y^2}{S_y}&\longrightarrow C,
 \label{eq:L3}\\
 3p_y^3\log p_y\,(\Delta_y-A T_y-BT_y^2)&\longrightarrow C,
 \label{eq:L4}\\
 \frac{\Delta_y-A T_y-BT_y^2}
 {T_y^3(\log p_y)^2}&\longrightarrow\frac C3.
 \label{eq:L5}\end{aligned}$$ Here $A,B,C$ are exactly those in [\[eq:ABC\]](#eq:ABC){reference-type="eqref" reference="eq:ABC"}.

For [\[eq:L1\]](#eq:L1){reference-type="eqref" reference="eq:L1"}, multiply [\[eq:rh382-input\]](#eq:rh382-input){reference-type="eqref" reference="eq:rh382-input"} by $p_y\log p_y$; the leading term tends to $A$ and all smaller terms vanish. For [\[eq:L2\]](#eq:L2){reference-type="eqref" reference="eq:L2"}, exact subtraction of $AT_y$ leaves $BT_y^2+CS_y+O(T_y^3)$. Multiplication by $(p_y\log p_y)^2$ sends the first term to $B$, while $S_y/T_y^2\to0$ and $T_y\to0$ dispose of the rest.

Put $$R_y=\Delta_y-A T_y-BT_y^2.
 \label{eq:residual}$$ Then [\[eq:rh382-input\]](#eq:rh382-input){reference-type="eqref" reference="eq:rh382-input"} says $R_y=CS_y+O(T_y^3)$. Because $T_y^3/S_y\to0$, division by $S_y$ proves [\[eq:L3\]](#eq:L3){reference-type="eqref" reference="eq:L3"}. Equation [\[eq:L4\]](#eq:L4){reference-type="eqref" reference="eq:L4"} follows from $3p_y^3\log p_y\,S_y\to1$. Finally, $$\frac{R_y}{T_y^3(\log p_y)^2}
 =C\frac{S_y}{T_y^3(\log p_y)^2}
   +O\!\left(\frac{1}{(\log p_y)^2}\right),$$ and [\[eq:scale5\]](#eq:scale5){reference-type="eqref" reference="eq:scale5"} proves [\[eq:L5\]](#eq:L5){reference-type="eqref" reference="eq:L5"}.

The terms in [\[eq:L2\]](#eq:L2){reference-type="eqref" reference="eq:L2"}--[\[eq:L5\]](#eq:L5){reference-type="eqref" reference="eq:L5"} are intrinsic and exact. Bare PNT gives only $$T_y=\frac{1+o(1)}{p_y\log p_y},\qquad
 T_y^2=\frac{1+o(1)}{p_y^2(\log p_y)^2}.$$ It does not say that $T_y-[p_y\log p_y]^{-1}=o(T_y^2)$, so replacing $AT_y$ by its PNT surrogate is unlicensed already in [\[eq:L2\]](#eq:L2){reference-type="eqref" reference="eq:L2"}. At the still smaller $S_y$ scale, an $o(T_y^2)$ error can dominate $S_y$; consequently the exact $BT_y^2$ in [\[eq:L3\]](#eq:L3){reference-type="eqref" reference="eq:L3"}--[\[eq:L5\]](#eq:L5){reference-type="eqref" reference="eq:L5"} cannot be replaced by $B/[p_y^2(\log p_y)^2]$ either. No effective PNT remainder is silently assumed.

# A directed interval and the sign of the residual {#sec:interval}

It remains to certify the sign of $C$. Let $N=100000$, and for $2\le m\le8$ define the finite product $$U_m(N)=\prod_{\substack{p\le N\\p\ \mathrm{odd}}}
 \frac{p^2-m}{p^2-1}.$$ For a tail prime put $b_p=(m-1)/(p^2-1)$. Bonferroni's elementary product bound gives $$1-\sum_{p>N}b_p\le\prod_{p>N}(1-b_p)\le1.$$ Moreover $$\sum_{p>N}\frac1{p^2-1}
 \le\sum_{n>N}\frac1{n^2-1}
 =\frac12\left(\frac1N+\frac1{N+1}\right)
 =\frac{200001}{20000200000}=:\theta_N.
 \label{eq:theta}$$ Therefore the exact enclosure $$U_m(N)\bigl(1-(m-1)\theta_N\bigr)
 \le u_m\le U_m(N)
 \label{eq:um-interval}$$ holds for every $2\le m\le8$.

The artifact evaluates the $9591$ odd-prime factors at decimal precision $80$, with floor rounding for lower endpoints, ceiling rounding for upper endpoints, and binary-float conversion trapped. In particular, the tail loss $(m-1)\theta_N$ is first rounded upward under ceiling rounding; only then is its complement $1-(m-1)\theta_N$ formed under floor rounding for the lower product endpoint. The cutoff anchor is the integer $N=100000$; the last prime below it is $99991$ and the next prime is $100003$, neither of which replaces $N$ in [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}. Sign-aware interval arithmetic is applied independently to $$\begin{aligned}
 Y_\infty&=6u_4-16u_5+30u_6-48u_7+70u_8,\\
 m_\infty&=2u_3-4u_4+6u_5-8u_6+10u_7-12u_8,\\
 Y_\infty-2m_\infty&=-4u_3+14u_4-28u_5+46u_6-68u_7+94u_8.\end{aligned}$$

[\[prop:positive\]]{#prop:positive label="prop:positive"} The full precision-$80$ endpoints are stored in the exact result ledger. They imply the shorter outward bounds $$1.5463476716710499204067249
 <Y_\infty-2m_\infty
 <1.5484488989771761112886458.$$ In particular, outward quantization to $19$ decimal places gives $$\boxed{1.5463476716710499204
 \le Y_\infty-2m_\infty
 \le1.5484488989771761113},
 \label{eq:published-interval}$$ and $C>0$.

Equation [\[eq:um-interval\]](#eq:um-interval){reference-type="eqref" reference="eq:um-interval"} supplies rigorous intervals for $u_2,\ldots,u_8$. For each coefficient in the last linear form, the lower endpoint uses the lower $u_m$ endpoint when the coefficient is positive and the upper endpoint when it is negative; the choices reverse for the upper endpoint. Directed arithmetic gives the displayed raw bounds. Outward quantization gives [\[eq:published-interval\]](#eq:published-interval){reference-type="eqref" reference="eq:published-interval"}. Division by $\pi^2>0$ then proves $C>0$.

[\[cor:sign\]]{#cor:sign label="cor:sign"} The residual $R_y$ in [\[eq:residual\]](#eq:residual){reference-type="eqref" reference="eq:residual"} is eventually positive and $$\frac{R_y}{T_y^3}\longrightarrow+\infty.
 \label{eq:amplification}$$ No effective index from which positivity holds is asserted.

Theorem [\[thm:gap-limits\]](#thm:gap-limits){reference-type="ref" reference="thm:gap-limits"} gives $R_y/S_y\to C>0$, proving eventual positivity. Also $$\frac{R_y}{T_y^3}=C\frac{S_y}{T_y^3}+O(1)
 =\left(\frac{C}{3}+o(1)\right)(\log p_y)^2+O(1)
 \longrightarrow+\infty.$$ The PNT input is qualitative, so the proof supplies no effective threshold.

# Executable certificate and immutable provenance {#sec:artifact}

The executable artifact separates symbolic theorem content from finite reproduction. The exact grid contains the rows in Table [1](#tab:certificate){reference-type="ref" reference="tab:certificate"}. Partition rows enumerate all $66$ partitions of degrees $1$ through $8$. Successor rows use $y\in\{1,2,3,5,8,13\}$ and $r=1,\ldots,8$; they reproduce the exact finite identity [\[eq:successor\]](#eq:successor){reference-type="eqref" reference="eq:successor"}, not the $y\to\infty$ theorem.

::: {#tab:certificate}
  --------------------------------------------------------------------------------------------------
  ledger                 rows          arithmetic role
  -------------------- ------ ------------------- --------------------------------------------------
  fixed $r$                 8   rational/symbolic constants and exponents for $r\le8$

  fixed partitions         66   rational/symbolic all partitions through degree $8$

  strict successors        48     exact fractions endpoint and first-atom interface

  scale relations           5           algebraic constants and relative orders

  normalized gaps           5           algebraic exact-subtraction ledger

  numeric intervals        10    directed decimal $u_2,\ldots,u_8,Y,m,Y-2m$

  negative mutations       20         fail-closed theorem, source, type, JSON, and numeric attacks
  --------------------------------------------------------------------------------------------------

  : Frozen RH-384 certificate grid. Finite rows reproduce proved identities and do not constitute asymptotic evidence.
:::

The mutations include the missing Abel boundary constant, the exponent $2d$ in place of $2d-\ell$, incorrect partition constants and log powers, loss of the factor $3$ in the $S_y$ normalizer, the sign $Y+2m$, both forbidden PNT substitutions in the exact residual, release/hash rebinding, binary-float injection, Boolean/integer aliasing, duplicate or nonfinite JSON, and moving the integer cutoff to either neighboring prime. The two endpoint mutations are explicitly marked as exact-interface failures only; they are not counted as failures of the leading PNT equivalent.

All decimal operations run inside fresh precision-$80$ directed contexts. Three hostile ambient contexts, including altered precision, rounding, exponent ranges, and trapped underflow/clamping, produce byte-identical certificates. The canonical exact certificate has $48689$ bytes and SHA-256

`01c91e57a01de9841f282327ab2f6e1a9368e136393ddab7a2cfe6b019a519c8`.

The closed Draft 2020--12 schema recursively fixes every member, value, type, and array length. Strict loaders reject duplicate keys and nonfinite constants.

The immutable source closure contains $51$ release blobs, with group sizes $7,8,8,8,8,8,2,2$: RH-374; RH-379 through RH-383; the two-file synthesis archive; and the RH-2 PNT main text and bibliography. The aggregate source digest is

`90434e0468ecc062cb522da096a267748725b5dca8e59c642bb7711f45a3e0e4`.

Each live file is checked against its declared release blob before result generation. Mutable root policy and handoff files are excluded. The publication manifest separately locks the manuscript, PDF, certificate, schema, audit ledgers, code, tests, and every external input.

# Claim boundary and theorem budget

The standalone verdict is **Route A: GO**. The fixed-$r$ Abel constant, fixed-partition scale compiler, strict scale ordering, five gap limits, and certified positive intermediate coefficient are new theorem content inside the frozen class. The RH-compatibility verdict is **Route B: STOP\_SCOPED**. The following firewalls remain explicit:

-   $r$ and $\lambda$ are fixed; no uniform growing-degree theorem or effective PNT rate is claimed;

-   the strict endpoint and successor atom are exact interface data, while the leading PNT equivalent alone cannot distinguish their endpoint mutations;

-   all second and lower gap limits retain the exact intrinsic subtractions; no bare-PNT surrogate is inserted;

-   $q$ is fixed before $N\to\infty$; no growing clock $q(N)$, exchange of limits, or adaptive-capacity limit is proved;

-   nonzero phasewise $c_{11}$ remains excluded; no shift-two cancellation theorem is inferred;

-   no intrinsic determinant, scattering completion, self-adjoint generator, von Mangoldt weighted prime-power trace, completed-zeta divisor equality, or Riemann-zero identification is constructed.

Accordingly Gates A--E remain false/open. This paper neither proves nor reduces the Riemann hypothesis. Any successor route must pay for its own new theorem edge rather than promoting this arithmetic tail translation to an operator statement. The four-volume synthesis remains the preserved foundation [@RHMVP2].

# Declarations {#declarations .unnumbered}

**Data and code availability.** The analytic proof, exact certificate generator, closed schema, tests, source-lock ledger, publication manifest, and both byte-identical PDF names are included with this paper. The calculation uses no external dataset.

**Author contributions.** The single author is responsible for conceptualization, methodology, formal analysis, software, validation, writing, and final approval.

**Funding.** No external funding was received for this work.

**Competing interests.** The author declares no competing interests.

**Ethics statement.** No human participants, animals, personal data, or clinical materials were involved; ethics review and informed consent are not applicable.

**AI assistance.** AI-assisted tools were used for proof auditing, symbolic and numerical code checking, adversarial test design, and typesetting support. All claims, citations, source locks, computations, and final text were checked under the author's responsibility.
