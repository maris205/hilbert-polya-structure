---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--7-base2-exponent-clock"
canonical_tex: "symplectic_map/papers/7-base2-exponent-clock/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/7-base2-exponent-clock/paper/manuscript.pdf"
source_sha256: "60a9868f92b2d34e9ae140cebc534118225d05fe647530df1341c5ad0cc96974"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact 2-Adic Valuation of Higher-Period Multipliers for a Frozen PCF Quadratic

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/7-base2-exponent-clock>)
- [规范 TeX](<../../../../../symplectic_map/papers/7-base2-exponent-clock/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/7-base2-exponent-clock/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/7-base2-exponent-clock/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/7-base2-exponent-clock/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the postcritically finite quadratic $g(z)=z^2-u$, where $u^3-2u^2+2u-2=0$, we determine the 2-adic valuation of every multiplier of exact period at least two. A standard non-Archimedean contraction argument shows more generally that, in residue characteristic two, every nontrivial cycle of $z^2+c$ with $0<|c|<1$ consists of units and has multiplier norm exactly $|2|^n$. At the frozen cubic this yields $w(\Lambda_C)=n w(2)$ at every place over two; in particular, every rational multiplier is $2^n$ times an odd integer. We then identify each local cycle as a unique Hensel lift of a Frobenius orbit and its normalized multiplier as an unramified norm; reduction modulo two gives a two-coefficient obstruction that excludes $\Lambda_C=\pm2^n$ at exact periods two and three but already admits an exact degree-four Frobenius orbit. A source-locked audit records twelve sign--period no-hit decisions over periods two through seven, each supported by separately implemented but algebraically equivalent exact gcd and resultant/field-norm certificates; all were development-seen, and a uniform exclusion valid for every $n\ge4$ remains open.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Exact 2-Adic Valuation of Higher-Period Multipliers\
  for a Frozen PCF Quadratic
```

## Markdown 正文

# Introduction {#sec:introduction}

Let $C=(z_0,\ldots,z_{n-1})$ be an exact period-$n$ cycle of a quadratic polynomial. Its multiplier factors as $$\Lambda_C=(g^n)'(z_0)=2^n B_C,
  \qquad B_C=\prod_{j=0}^{n-1}z_j.
  \label{eq:multiplier-factorization}$$ The chain rule gives the visible factor $2^n$, while global algebraic integrality makes a rational normalized product integral; neither observation determines whether $B_C$ is a unit at two. That distinction is decisive at the frozen map $$Q(U)=U^3-2U^2+2U-2,
  \qquad Q(u)=0,
  \qquad g(z)=z^2-u,
  \label{eq:frozen-map}$$ where $u$ denotes the unique real root of $Q$.

The main result is an exact local statement in every period: for every cycle-field place $w$ above two and every exact $n\ge2$, $$w(\Lambda_C)=n w(2).
  \label{eq:intro-main}$$ If $\Lambda_C$ is rational, its normalized product is therefore an odd integer. The theorem sharpens divisibility to exact valuation, but it leaves the boundary values $B_C=\pm1$ unresolved. Figure [1](#fig:boundary-map){reference-type="ref" reference="fig:boundary-map"} places that residual equality beside two predicates that must not be conflated with it.

Our contributions are four concrete claims.

1.  We give a complete elementary proof of a local sharp-boundary lemma for $z^2+c$ in residue characteristic two and specialize it at the unique place over two of $\mathbb{Q}(u)$.

2.  We prove the rational corollary $\Lambda_C=2^n m$ with $m$ odd by combining the local valuation with a self-contained integrality argument.

3.  We describe exact local cycles as Frobenius--Hensel lifts and identify $B_C$ with their unramified norm. Its first two residue coefficients rule out $B_C=\pm1$ for $n=2,3$, while an irreducible degree-four witness shows that this filter alone cannot exclude all higher-degree orbits.

4.  We preserve a one-shot, exact-symbolic ledger through period seven as an implementation-falsification record, with exact-period saturation, two separately implemented but algebraically equivalent exact target certificates (gcd and resultant/field norm), signed controls, and an independent result integrity audit.

![The theorem/evidence boundary. Over a complete non-Archimedean field of characteristic zero and residue characteristic two, the standard local argument places every exact $n\ge2$ cycle on the unit circle and gives $w(\Lambda_C)=n w(2)$. Rationality then forces $\Lambda_C=2^n m$ with $m$ odd. This does not decide a uniform exclusion of the residual rational equality $\Lambda_C=\pm2^n$ over all $n\ge4$, complex-modulus equality without rationality, or characteristic-exponent equality.](<../../../../../symplectic_map/papers/7-base2-exponent-clock/figures/fig1_boundary_map.pdf>){#fig:boundary-map width="98%"}

![The sole registered exact-symbolic audit for periods $n=2,\ldots,7$. Panel (a) reports the exact-set degree $D_n=\deg(\Psi_n^{\mathrm{set}})$ and exact-cycle count $D_n/n$ read from the frozen records. In panel (b), every $B_n=+1$ and $B_n=-1$ target has zero gcd degree and nonzero exact resultant field norm. These algebraically equivalent certificates were implemented by separate exact engines and agree. All periods were development-seen before source lock; this finite reproduction tests the implementation but cannot close the all-period equality question.](<../../../../../symplectic_map/papers/7-base2-exponent-clock/figures/fig2_registered_ledger.pdf>){#fig:registered-ledger width="80%"}

The scope boundary is part of the result. This paper does not exclude $\Lambda_C=\pm2^n$ in all periods, does not decide $|\Lambda_C|=2^n$ without rationality, and makes no claim about prime orbits, zeta zeros, quantization, or a general rigidity theorem for PCF quadratics. In particular, the 2-adic theorem does not imply the Archimedean identity $n^{-1}\log|\Lambda_C|=\log 2$, nor its negation.

Section [2](#sec:object){reference-type="ref" reference="sec:object"} fixes the object and its relation to nearby work. Sections [3](#sec:local){reference-type="ref" reference="sec:local"}--[5](#sec:norm){reference-type="ref" reference="sec:norm"} prove the valuation and norm statements. Section [6](#sec:equality){reference-type="ref" reference="sec:equality"} derives necessary equality conditions, and Section [7](#sec:audit){reference-type="ref" reference="sec:audit"} reports the bounded exact audit. The final section isolates the remaining proof problem. The finite ledger is previewed in Figure [2](#fig:registered-ledger){reference-type="ref" reference="fig:registered-ledger"}; the proof mechanism is summarized later in Figure [3](#fig:frobenius-filter){reference-type="ref" reference="fig:frobenius-filter"}.

# Frozen object, genealogy, and nearby results {#sec:object}

The derivative $Q'(U)=3U^2-4U+2$ is positive on $\mathbb R$, so $Q$ has a unique real root. Put $a=u^2-u$. Direct reduction by $Q(u)=0$ gives $$0\longmapsto -u\longmapsto a\longmapsto -a\longmapsto -a.
  \label{eq:critical-orbit}$$ Thus $g$ is postcritically finite of type $(3,1)$. The same algebraic parameter appears in a recent study [@wang2026prime], cited here only to document the object's genealogy. No empirical dataset, parameter search, or conclusion from that work enters the present note. Every mathematical claim below is proved here from [\[eq:frozen-map\]](#eq:frozen-map){reference-type="eqref" reference="eq:frozen-map"}.

Arithmetic dynamics supplies standard terminology for periodic points, local fields, and multipliers [@silverman2007arithmetic]. Formal dynatomic period and least period need not agree without additional checks [@morton1994rational]; this distinction controls the finite audit in Section [7](#sec:audit){reference-type="ref" reference="sec:audit"}. The closest literature divides into four axes.

\@p0.20Y Y@ Axis & What the cited work supplies & What is proved here instead\
Non-Archimedean PCF dynamics & Critical-point criteria and height bounds for attracting cycles [@benedettoetal2014attracting]; a contemporary sharp strict-threshold theorem [@riveraletelier2026critical]. & Equality of the 2-adic multiplier norm with the threshold for the fixed cubic, and the exact valuation at every cycle-field place.\
Good reduction and periods & Relations between primitive and reduced periods [@hutz2009good] and recent uniform bounds [@rajagopalzhang2025uniform]. & The unique lift, exact Frobenius degree, and unramified norm identity for this map.\
Multiplier formalisms & Prescribed-multiplier parameter loci [@buffgauthier2015quadratic] and arithmetic of multiplier polynomials [@murakami2024arithmetic]. & A value-specific local certificate at one fixed PCF parameter.\
Units and exponent spectra & Arithmetic of Misiurewicz polynomials and associated dynamical units [@benedettogoksel2023part1; @benedettogoksel2024part2], and global characteristic-exponent span [@jixiezhang2026space]. & Necessary conditions for normalized products of arbitrary primitive cycles; no value-specific conclusion is imported from the global theory.\

The local lemma below is standard and carries no priority claim. In particular, Rivera--Letelier's 2026 theorem is used only as a contemporary cross-check: its strict inequality forces attraction of a critical point, whereas the present issue is equality at the threshold. Likewise, the Misiurewicz-unit literature concerns parameter polynomials and associated periodic multipliers; it does not automatically cover every primitive cycle of the fixed map.

# A local sharp-boundary lemma {#sec:local}

We write absolute values multiplicatively and valuations additively. No normalization of the latter is needed, since all valuation identities are homogeneous.

[\[thm:local\]]{#thm:local label="thm:local"} Let $F$ be a complete non-Archimedean field of characteristic zero and residue characteristic two. For $f(z)=z^2+c$ with $0<|c|<1$, every exact period-$n$ point with $n\ge2$ satisfies $$|f^j(z)|=1\quad(0\le j<n),
  \qquad |(f^n)'(z)|=|2|^n.
  \label{eq:local-boundary}$$

If $|z|>1$, then $|f(z)|=|z|^2>|z|$, and successive absolute values escape; hence every periodic point belongs to the closed unit disk. The open unit disk is forward invariant because $|f(z)|\le\max\{|z|^2,|c|\}<1$ whenever $|z|<1$.

Suppose a nontrivial cycle lies in that open disk. For distinct cycle points $x,y$, $$|f(x)-f(y)|=|x-y|\,|x+y|<|x-y|.
  \label{eq:strict-contraction}$$ Taking $x=z_0$, $y=z_1$, and applying [\[eq:strict-contraction\]](#eq:strict-contraction){reference-type="eqref" reference="eq:strict-contraction"} around the cycle would strictly decrease their distance and return to the same pair after $n$ steps, a contradiction. Every point of an exact cycle of length at least two is therefore a unit. Finally, $$(f^n)'(z_0)=2^n\prod_{j=0}^{n-1}f^j(z_0),$$ and every factor in the product has norm one. This proves [\[eq:local-boundary\]](#eq:local-boundary){reference-type="eqref" reference="eq:local-boundary"}.

The displayed value is exact rather than merely a bound. The power map $z\mapsto z^2$, whose parameter $c=0$ lies just outside the strict hypothesis $0<|c|<1$, also attains the ambient multiplier threshold $2^n$ on every nonzero exact cycle. Rivera--Letelier's independent strict-threshold theorem also places the residue-characteristic-two boundary at $|2|^n$ [@riveraletelier2026critical]; the elementary proof above is logically complete without that comparison.

# The frozen 2-adic valuation theorem {#sec:frozen-theorem}

Let $K=\mathbb{Q}(u)$. The polynomial $Q$ is 2-Eisenstein. It is therefore irreducible over $\mathbb{Q}_2$, the tensor product $K\otimes_\mathbb{Q}\mathbb{Q}_2$ is a field, and $K$ has a unique place over two. We denote its completion by $K_u$. This extension of $\mathbb{Q}_2$ is totally ramified of degree three, with uniformizer $u$. The defining equation also gives the useful exact identity $$2=\frac{u^3}{u^2-u+1},
  \qquad v_u(2)=3,
  \label{eq:two-uniformizer}$$ because the denominator is a $u$-adic unit.

[\[thm:frozen\]]{#thm:frozen label="thm:frozen"} Let $L/K$ be a finite extension containing the coordinates of an exact period-$n$ cycle $C$ of $g$, with $n\ge2$, and let $w$ be an additive non-Archimedean valuation of $L$ above the unique valuation of $K$ over two. Every point of $C$ is a $w$-unit and $$w(\Lambda_C)=n w(2).
  \label{eq:frozen-valuation}$$ If $\Lambda_C\in\mathbb{Q}$, then $$v_2(\Lambda_C)=n,
  \qquad \Lambda_C=2^n m
  \quad\text{for some }m\in2\mathbb{Z}+1.
  \label{eq:rational-odd}$$

Complete $L$ at $w$. Since the constant term of $g$ is $-u$, Theorem [\[thm:local\]](#thm:local){reference-type="ref" reference="thm:local"} applies and gives $w(z_j)=0$ for all $j$. Equation [\[eq:multiplier-factorization\]](#eq:multiplier-factorization){reference-type="eqref" reference="eq:multiplier-factorization"} then gives [\[eq:frozen-valuation\]](#eq:frozen-valuation){reference-type="eqref" reference="eq:frozen-valuation"}.

It remains to justify the ordinary integer in [\[eq:rational-odd\]](#eq:rational-odd){reference-type="eqref" reference="eq:rational-odd"} without importing an unpublished result. The polynomial $g^n(X)-X$ is monic over $\mathcal{O}_K$, so each periodic point is integral over $\mathcal{O}_K$, hence is an algebraic integer over $\mathbb{Z}$. The product $B_C$ is therefore an algebraic integer. If $\Lambda_C$ is rational, then $B_C=\Lambda_C/2^n$ is rational as well, and $\mathbb{Q}\cap\overline{\mathbb{Z}}=\mathbb{Z}$ gives $B_C\in\mathbb{Z}$. Its valuation at every place above two is zero, so this integer is odd.

The conclusion "odd" is exact, but it is not an exclusion: the two integers $1$ and $-1$ remain among the allowed normalized quotients. The next section turns those two cases into a local norm problem.

# Frobenius cycles and the norm coordinate {#sec:norm}

The residue field of $K_u$ is $\mathbb{F}_2$. Let $K_{u,n}/K_u$ be the unramified extension of degree $n$, and let $\sigma$ denote the lift of the squaring Frobenius. Reduction modulo $u$ gives $$g^n(X)-X\equiv X^{2^n}-X\pmod u.
  \label{eq:frobenius-reduction}$$ The derivative of the right-hand side is $-1$, so all its roots are simple.

[\[prop:hensel\]]{#prop:hensel label="prop:hensel"} For each $\alpha\in\mathbb{F}_{2^n}$, there is a unique root $z_\alpha\in\mathcal O_{K_{u,n}}$ of $g^n(X)-X$ reducing to $\alpha$. If $\alpha$ has exact Frobenius degree $d\mid n$, then $z_\alpha$ has exact dynamical period $d$, and $$\sigma(z_\alpha)=g(z_\alpha).
  \label{eq:frob-is-dynamics}$$ Consequently, for exact degree $n$, $$B_C=\prod_{j=0}^{n-1}g^j(z_\alpha)
      =\mathop{\mathrm{N}}_{K_{u,n}/K_u}(z_\alpha).
  \label{eq:norm-coordinate}$$

Hensel's lemma applied to [\[eq:frobenius-reduction\]](#eq:frobenius-reduction){reference-type="eqref" reference="eq:frobenius-reduction"} supplies one lift in each of the $2^n$ residue classes. These roots exhaust the degree- $2^n$ polynomial. Suppose that $\alpha$ has exact Frobenius degree $d\mid n$. Let $y\in\mathcal O_{K_{u,d}}\subset\mathcal O_{K_{u,n}}$ be its unique Hensel lift satisfying $g^d(y)=y$. Because $d\mid n$, the same element also satisfies $g^n(y)=y$; uniqueness among the roots of $g^n(X)-X$ reducing to $\alpha$ therefore gives $y=z_\alpha$. Reduction shows that no smaller positive iterate fixes this lift, so its exact period is $d$.

Both $\sigma(z_\alpha)$ and $g(z_\alpha)$ are roots of $g^n(X)-X$ reducing to $\alpha^2$: the coefficients of $g$ lie in $K_u$, and $g$ commutes with its iterates. Hensel uniqueness proves [\[eq:frob-is-dynamics\]](#eq:frob-is-dynamics){reference-type="eqref" reference="eq:frob-is-dynamics"}. Multiplying its $n$ Frobenius conjugates gives [\[eq:norm-coordinate\]](#eq:norm-coordinate){reference-type="eqref" reference="eq:norm-coordinate"}.

The proposition distinguishes least period from formal period before any dynatomic manipulation. It also places every normalized cycle product in the base local field $K_u$, a fact used below for repeated returns.

![The first local obstruction to rational equality. Panel (a) follows an exact Frobenius orbit through its unique Hensel lift to the norm coordinate $B_C=N_{K_{u,n}/K_u}(z_\alpha)$; equality $B_C=\pm1$ forces $e_{n-1}=e_{n-2}=0$. Panel (b) reads the frozen irreducible-polynomial ledger: no degree-two or degree-three polynomial passes, whereas the degree-four witness $T^4+T^3+1$ does. The witness shows that the necessary filter cannot exclude every degree-four orbit; passing it does not thereby certify an equality cycle. Panel (c) records the passed positive, signed, negative-target, and formal-period-pollution controls.](<../../../../../symplectic_map/papers/7-base2-exponent-clock/figures/fig3_frobenius_filter.pdf>){#fig:frobenius-filter width="98%"}

# What rational equality would force {#sec:equality}

Relation [\[eq:two-uniformizer\]](#eq:two-uniformizer){reference-type="eqref" reference="eq:two-uniformizer"} gives $(2)=(u^3)$ in every unramified extension under consideration and identifies the coefficient ring as $$\mathcal O_{K_{u,n}}/(2)
  \simeq \mathbb{F}_{2^n}[\bar u]/(\bar u^3).$$ Thus $1,\bar u,\bar u^2$ are a basis over $\mathbb{F}_{2^n}$. Use Teichmuller representatives for residue-field elements and write a lift as $z_\alpha\equiv\alpha+b_1u+b_2u^2\pmod2$. Substitution into $\sigma(z_\alpha)=z_\alpha^2-u$ may be performed in this quotient: all cross terms in $(\alpha+b_1u+b_2u^2)^2$ contain a factor $2$ and vanish modulo $u^3$. Coefficient comparison gives $\sigma(b_1)=1$ and $\sigma(b_2)=b_1^2=1$. Hence $$z_\alpha\equiv\alpha+u+u^2\pmod2.
  \label{eq:lift-mod-two}$$

Let $\alpha_j=\alpha^{2^j}$, and let $e_k$ be the elementary symmetric function of degree $k$ in $\alpha_0,\ldots,\alpha_{n-1}$, with $e_0=1$. Each $e_k$ is Frobenius-fixed and hence lies in $\mathbb{F}_2$; for an exact orbit, $e_n=\prod_j\alpha_j=1$. Put $t=u+u^2$. In the displayed quotient, $t^2\equiv u^2\pmod{u^3}$ and $t^3=0$, so $$\prod_{j=0}^{n-1}(\alpha_j+t)
  =e_n+e_{n-1}t+e_{n-2}t^2
  =1+e_{n-1}u+(e_{n-1}+e_{n-2})u^2.$$ Together with [\[eq:lift-mod-two\]](#eq:lift-mod-two){reference-type="eqref" reference="eq:lift-mod-two"}, this expands the norm as $$B_C\equiv
  1+e_{n-1}u+(e_{n-1}+e_{n-2})u^2\pmod2.
  \label{eq:norm-expansion}$$

[\[prop:two-coeff\]]{#prop:two-coeff label="prop:two-coeff"} If $B_C=\pm1$, then $$e_{n-1}=e_{n-2}=0.
  \label{eq:two-coeff}$$ No exact period-two or period-three cycle satisfies this condition. In degree four the irreducible polynomial $T^4+T^3+1$ does satisfy it, so [\[eq:two-coeff\]](#eq:two-coeff){reference-type="eqref" reference="eq:two-coeff"} already fails to exclude every exact degree-four orbit.

The two signs reduce to the same element modulo two. Comparing the coefficients in the basis $1,\bar u,\bar u^2$ in [\[eq:norm-expansion\]](#eq:norm-expansion){reference-type="eqref" reference="eq:norm-expansion"} gives [\[eq:two-coeff\]](#eq:two-coeff){reference-type="eqref" reference="eq:two-coeff"}. The only irreducible quadratic is $T^2+T+1$, and the irreducible cubics are $T^3+T+1$ and $T^3+T^2+1$. In each case at least one of the coefficients of $T$ and $T^2$, namely $e_{n-1}$ and $e_{n-2}$, is nonzero. Thus equality is impossible for $n=2,3$. The polynomial $T^4+T^3+1$ is irreducible over $\mathbb{F}_2$ and has zero coefficients of $T$ and $T^2$. Its Frobenius orbit therefore passes the necessary filter. Passing the filter does not certify equality; the statement concerns only the two displayed residue coefficients, not the full norm in $K_u$.

Two further necessary conditions are useful because they retain information discarded by reduction modulo two. Order the points so that $g(z_j)=z_{j+1}$, with indices modulo $n$, and define $P_C(X)=\prod_j(X-z_j)$.

[\[prop:cycle-poly\]]{#prop:cycle-poly label="prop:cycle-poly"} For every exact cycle, $$P_C(g(X))=(-1)^nP_C(X)P_C(-X).
  \label{eq:cycle-poly}$$ If $n\ge2$ and $B_C=\varepsilon\in\{\pm1\}$, then $$P_C(-u)=P_C(u)=P_C(a)=(-1)^n,
  \qquad P_C(0)=(-1)^n\varepsilon.
  \label{eq:special-values}$$ These identities do not imply that the single-cycle polynomial belongs to $K[X]$.

Since $u+z_j=z_{j-1}^2$, $$P_C(g(X))=\prod_j(X^2-z_j^2)
           =(-1)^nP_C(X)P_C(-X),$$ which proves [\[eq:cycle-poly\]](#eq:cycle-poly){reference-type="eqref" reference="eq:cycle-poly"}. The fixed point $-a$ is not on an exact cycle of length at least two. Substitution of $X=-a$ into [\[eq:cycle-poly\]](#eq:cycle-poly){reference-type="eqref" reference="eq:cycle-poly"} and cancellation of $P_C(-a)$ gives $P_C(a)=(-1)^n$. Next, $P_C(0)=(-1)^nB_C$, and substitution at $X=0$ gives $P_C(-u)=(-1)^n$. Substitution at $X=u$, using $g(u)=a$, then gives $P_C(u)=(-1)^n$.

Finally, repetition creates no hidden rational base-two equality. The only roots of unity in $K_u$ are $\pm1$: reduction removes all nontrivial odd-order torsion, while a nontrivial higher 2-power root of unity generates an even-degree extension of $\mathbb{Q}_2$, which cannot lie in the cubic field $K_u$. If the $r$-fold return of an exact period-$n$ orbit is rational with ordinary Archimedean absolute value $2^{nr}$, equivalently if it equals $\pm2^{nr}$, then $B_C^r=\pm1$. Since $B_C\in K_u$, it follows that already $B_C=\pm1$. The point still has exact period $n$, not $nr$, and the argument says nothing about a modulus-only return without rationality.

# Registered finite exact audit {#sec:audit}

The finite calculation is a bounded test of the exact-period implementation, not evidence for extending Proposition [\[prop:two-coeff\]](#prop:two-coeff){reference-type="ref" reference="prop:two-coeff"} to all periods. The source lock fixed the candidate, the signs $\{+1,-1\}$, and the periods $2,\ldots,7$. Every one of those periods had been seen during development before the lock; there is no blind or prospective split.

For each $n$, the implementation forms a squarefree set-theoretic exact component $\Psi_n^{\mathrm{set}}$, verifies that its degree is divisible by $n$, and checks that the cycle product $B_n(X)$ is invariant under $g$ modulo that component. Each sign is checked by two separately implemented but algebraically equivalent exact certificates: the gcd must be the constant polynomial one, while the resultant must have nonzero exact norm from $K$ to $\mathbb{Q}$. All twelve pairs agreed. The complete numbers, including exact nanosecond timings and norm factorizations, appear in Appendix [10](#app:ledger){reference-type="ref" reference="app:ledger"}.

The controls guard the principal false-negative modes. For $z^2$ at period two the positive equality is detected and a declared negative target is rejected. For $z^2-2$, the exact component $X^2+X-1$ has $B=-1$ and multiplier $-4$, so the signed path is exercised. For $z^2-3/4$, a nonempty formal period-two component is removed completely by least-period saturation and produces no false hit. An upstream regression independently preserves the earlier coordinate and multiplier identities. The reviewed code tree passed 38 distinct tests with no failure, error, or skip.

The one authorized candidate run ended `COMPLETED_NO_HIT`. It used exact symbolic arithmetic, performed zero numerical candidate runs and no approximate matching, accessed no external restricted dataset, and did not extend the period range after the null result. Its only defensible finite classification is `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`. The proof-backed all-period classification is instead `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF`.

# Discussion and open boundary {#sec:discussion}

The valuation theorem removes one source of ambiguity: a rational higher-period multiplier cannot have extra powers of two hidden in its normalized cycle product. The remaining equality question lies wholly inside the unit group of $K_u$. Proposition [\[prop:hensel\]](#prop:hensel){reference-type="ref" reference="prop:hensel"} makes that question a norm equation, while Proposition [\[prop:two-coeff\]](#prop:two-coeff){reference-type="ref" reference="prop:two-coeff"} sees only the first two nilpotent coefficients of the norm modulo $u^3$. The degree-four witness pinpoints the failure: those two coefficients can vanish without forcing any conclusion about whether the full norm is $\pm1$.

Three proof-level continuations are natural. One may compute higher $u$-adic coefficients uniformly along Frobenius orbits, study the norm-one subgroup together with the nonlinear Hensel equation, or impose Galois constraints on the special values in [\[eq:special-values\]](#eq:special-values){reference-type="eqref" reference="eq:special-values"}. Each route would need a degree-independent contradiction; a longer finite cutoff would not supply one.

The semantic separations remain strict. Rational equality $\Lambda_C=\pm2^n$, Archimedean modulus equality $|\Lambda_C|=2^n$ for a nonrational multiplier, and characteristic- exponent equality are different predicates. This note proves no uniform equality exclusion for all $n\ge4$. In the surrounding project ledger, Route A is not advanced and Route B is not opened.

# Local-field details and repetition {#app:local}

We record two details used in the main text. First, 2-Eisenstein irreducibility over $\mathbb{Q}_2$ has global force here because $[K:\mathbb{Q}]=3$: the completed tensor product has a single factor of full degree. Thus the phrase "the unique place over two" is not an assumption on the ring of integers. Equation [\[eq:two-uniformizer\]](#eq:two-uniformizer){reference-type="eqref" reference="eq:two-uniformizer"} then shows directly that the ramification index is three and that the residue field remains $\mathbb{F}_2$.

Second, let $\zeta\in K_u$ be a root of unity. Its prime-to-two part injects under reduction into $\mathbb{F}_2^\times$, hence is trivial. If the 2-primary order is at least four, then $\mathbb{Q}_2(\zeta)/\mathbb{Q}_2$ has even degree. The tower law forbids such a subfield of the degree-three extension $K_u/\mathbb{Q}_2$. Therefore $\mu(K_u)=\{\pm1\}$. For an exact period- $n$ cycle, Proposition [\[prop:hensel\]](#prop:hensel){reference-type="ref" reference="prop:hensel"} puts $B_C$ in $K_u$, and $$(g^{nr})'(z_0)=\Lambda_C^r=2^{nr}B_C^r.$$ If this repeated return is rational of ordinary Archimedean absolute value $2^{nr}$, equivalently if it equals $\pm2^{nr}$, then $B_C^{2r}=1$, hence $B_C=\pm1$. This proves the repeat-closed boundary without assigning the repeated return a false least period.

# Exact-period construction and raw registered ledger {#app:ledger}

Write $F_d(X)=g^d(X)-X$ and $R_d=\mathop{\mathrm{rad}}(F_d)$. The frozen set-theoretic exact component is $$\Psi_n^{\mathrm{set}}
  =\frac{R_n}{\gcd\!\left(R_n,
        \prod_{\substack{d\mid n\\d<n}}R_d\right)},
  \label{eq:exact-set-component}$$ made monic over $K$. The formal dynatomic quotient is computed and radicalized separately; in all six candidate rows its radical agrees with [\[eq:exact-set-component\]](#eq:exact-set-component){reference-type="eqref" reference="eq:exact-set-component"}, but the implementation never substitutes that empirical agreement for least-period saturation. With $B_n(X)=\prod_{j=0}^{n-1}g^j(X)$, the two separately implemented but algebraically equivalent exact certificates are $$\gcd(\Psi_n^{\mathrm{set}},B_n-\varepsilon)=1,
 \qquad
 \mathop{\mathrm{N}}_{K/\mathbb{Q}}\!\left(\mathop{\mathrm{Res}}_X(\Psi_n^{\mathrm{set}},B_n-\varepsilon)\right)
 \ne0,
 \quad \varepsilon\in\{\pm1\}.
 \label{eq:dual-certificates}$$

For orientation, the first three exact components are $$\begin{aligned}
 \Psi_2^{\mathrm{set}}={}&X^2+X+1-u,\\
 \Psi_3^{\mathrm{set}}={}&X^6+X^5+(1-3u)X^4+(1-2u)X^3\\
 &+(1-3u+3u^2)X^2+(1-2u+u^2)X-1+u,\\
 \Psi_4^{\mathrm{set}}={}&X^{12}-6uX^{10}+X^9+(-3u+15u^2)X^8-4uX^7\\
 &+(-39+40u-28u^2)X^6+(-2u+6u^2)X^5\\
 &+(24+2u-3u^2)X^4+(-7+8u-4u^2)X^3\\
 &+(12-13u+5u^2)X^2-u^2X-1.\end{aligned}$$ The degree-30, degree-54, and degree-126 coefficient arrays are retained without transcription in the bound machine-readable result; their exact definitions are still [\[eq:exact-set-component\]](#eq:exact-set-component){reference-type="eqref" reference="eq:exact-set-component"}. Table [\[tab:raw-ledger\]](#tab:raw-ledger){reference-type="ref" reference="tab:raw-ledger"} reproduces every registered decision scalar and exact norm factorization.

\@ccccccYYr@ Run & $n$ & $D_n$ & $c_n$ & $G_+$ & $G_-$ & $\mathop{\mathrm{N}}\mathop{\mathrm{Res}}(B_n-1)$ & $\mathop{\mathrm{N}}\mathop{\mathrm{Res}}(B_n+1)$ & ns\
R042 & 2 & 2 & 1 & 0 & 0 & $2^2$ & $2^2$ & 63,931,487\
R043 & 3 & 6 & 2 & 0 & 0 & $2^9$ & $2^9$ & 174,504,404\
R044 & 4 & 12 & 3 & 0 & 0 & $2^{20}$ & $2^{24}$ & 411,053,181\
R045 & 5 & 30 & 6 & 0 & 0 & $2^{50}\!\cdot16807$ & $2^{60}\!\cdot161051$ & 1,637,080,691\
R046 & 6 & 54 & 9 & 0 & 0 & $2^{102}\!\cdot117649$ & $2^{120}\!\cdot387420489$ & 4,033,271,287\
R047 & 7 & 126 & 18 & 0 & 0 & $2^{294}$ & $2^{266}\!\cdot868028736113769706358509$ & 16,919,324,815\

The six times sum to exactly $23{,}239{,}165{,}865$ ns. Every row is marked `DEVELOPMENT_SEEN_` `REPRODUCTION`; the optional $q=3$ diagnostic was not requested. Zero gcd degree (equivalently, absence of a nonconstant gcd) and the nonzero norm are algebraically equivalent decisions here, obtained by separately implemented exact code paths.

# Provenance and evidence map {#app:provenance}

The contemporaneous commitment is `experiments/source_lock.json`, SHA-256

    205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1

The proof package has SHA-256

    9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9

and the independently deployment-reviewed code tree has SHA-256

    7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a

The official result and strict result manifest have respective SHA-256 digests

    847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6
    6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8

The manifest binds twelve regular evidence files, has `pass=true`, and records no missing, extra, nested, symlinked, unsupported, unsafe, or semantically invalid entry. The independent result audit rederived the exact components and all twelve target decisions from the serialized $1,u,u^2$ coefficients without another registered execution.

Claim provenance is as follows. Theorems [\[thm:local\]](#thm:local){reference-type="ref" reference="thm:local"} and [\[thm:frozen\]](#thm:frozen){reference-type="ref" reference="thm:frozen"} alone support the all-period valuation. Proposition [\[prop:two-coeff\]](#prop:two-coeff){reference-type="ref" reference="prop:two-coeff"} alone supports equality absence at periods two and three. The registered result supports only finite absence through period seven in the disclosed development set. Figure [1](#fig:boundary-map){reference-type="ref" reference="fig:boundary-map"} is a theorem-scope map, Figure [3](#fig:frobenius-filter){reference-type="ref" reference="fig:frobenius-filter"} is a proof-and-control map, and Figure [2](#fig:registered-ledger){reference-type="ref" reference="fig:registered-ledger"} is a rendering of the frozen finite records. No finite record is used to prove a degree-independent statement.

The paper build is independent of candidate execution. From the `paper` directory, `./build.sh` produces the review PDF with a fixed UTC epoch. The registered candidate lifecycle is closed and must not be rerun or extended under this source lock.
