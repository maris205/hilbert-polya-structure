---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-12-postcritical-weighted-zeta-factorization"
canonical_tex: "zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/postcritical-weighted-zeta-factorization.pdf"
source_sha256: "e84df1ca6d5a5d4679a2b89d4bab7586a05d42b72e159b009710397bdfa1ee2d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Postcritical Factorization of a Weighted Zeta Function at a Quadratic Band-Merging Map: An Analytic Circle Lift, Equivariant Fredholm Determinants, and a Spectral Noncancellation Criterion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/postcritical-weighted-zeta-factorization.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $f_u(x)=1-u x^2$ at the algebraic band-merging parameter $u_{\mathrm c}^3-2u_{\mathrm c}^2+2u_{\mathrm c}-2=0$, put $r=u_{\mathrm c}-1$, and set $\lambda=2u_{\mathrm c}r=1.678573510428\ldots$. For the central component $S=f_{u_{\mathrm c}}^2|_{[-r,r]}$, a preceding weighted-zeta analysis found numerically $$q_n=1-\lambda^{-n}+\lambda^{-2n}+o(\lambda^{-2n}),
   \qquad
   q_n=\sum_{S^n x=x}|(S^n)'(x)|^{-1},$$ and conjectured a centered-zeta zero at $z=\lambda$. We identify the exact mechanism behind those two postcritical terms.

  The branched coordinate $\pi(\theta)=-r\cos\theta$ lifts $S$ to a real-analytic, orientation-preserving, degree-two expanding circle map $F$ satisfying $\pi\circ F=S\circ\pi$. Its derivative obeys $$F'(\theta)^2=
   \frac{16(1-u_{\mathrm c}x^2)^2}
   {u_{\mathrm c}(2-u_{\mathrm c}x^2)(1-x^2)},
   \qquad x=-r\cos\theta,
   \qquad \min F'=\lambda.$$ Let $D_{\beta,+}$ and $D_{\beta,-}$ be the even and odd Fredholm determinants of the analytic transfer operator with weight $(F')^{-\beta}$. An equivariant fixed-point calculation gives, for every $n\ge1$, the exact trace identity $$\boxed{q_n=E_{1,n}-O_{2,n}-\lambda^{-n}+\lambda^{-2n}},$$ where $E_{1,n}$ is the even $\beta=1$ flat trace and $O_{2,n}$ is the odd $\beta=2$ flat trace. Consequently the component zeta function has the exact meromorphic continuation $$\boxed{
   \mathcal Z(z)=\frac{D_{2,-}(z)}{D_{1,+}(z)}
   \frac{1-z/\lambda}{1-z/\lambda^2}.}$$ The displayed rational factor is an orbifold-versus-interval correction at the repelling postcritical endpoint; it is not a fitted asymptotic.

  After removing the simple Perron zero of $D_{1,+}$ at $z=1$, a pressure argument proves $D_{2,-}(\lambda)\ne0$. Thus the centered zeta has an actual simple zero at $\lambda$ if and only if $\lambda^{-1}$ is absent from the non-Perron spectrum of the even $\beta=1$ operator. We do not assume or claim this last spectral noncancellation. Exhaustive 50-decimal arithmetic through $2^{20}$ periodic words gives a deflated remainder ratio $0.20803502$ at $n=20$, tending toward the independent Fredholm estimate $0.20788030$, far below $\lambda^{-1}=0.59574394$. The degree-20 centered zero is $1.6785994451$, and $G_{20}(\lambda)=1.1431449660$. These values are strong evidence for noncancellation, explicitly separated from the theorem.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Postcritical Factorization of a Weighted Zeta Function**\
  **at a Quadratic Band-Merging Map:**\
  An Analytic Circle Lift, Equivariant Fredholm Determinants,\
  and a Spectral Noncancellation Criterion
```

## Markdown 正文

**Keywords:** weighted dynamical zeta function; postcritical orbit; analytic expanding circle map; equivariant transfer operator; Fredholm determinant; quadratic map; spectral noncancellation.

**MSC 2020:** 37E10; 37C30; 37D20; 47A10; 47B10.

# Introduction {#sec:introduction}

Dynamical zeta functions often turn an exponentially small periodic-orbit term into a visible zero or pole. The difficult part is not recognizing a stable numerical rate; it is identifying which geometric orbit produces the factor and proving that the factor is not canceled by the remaining transfer operator. At a postcritically finite map these two questions should be separated.

This paper studies one component of the square of the quadratic map $f_u(x)=1-u x^2$ at its first algebraic band-merging parameter. The preceding flat-trace completion theorem established, without a rate formula, that the standard component weight $$\label{eq:q-introduction}
 q_n=\sum_{S^n x=x}\frac1{|(S^n)'(x)|}$$ satisfies $q_n=1+O(\rho^n)$ for some $\rho<1$ by the Keller--Nowicki Collet--Eckmann weighted-zeta theory [@KellerNowicki1992; @WangFlatTrace2026]. Exhaustive data suggested the much sharper expansion $$\label{eq:previous-sharp}
 q_n=1-\lambda^{-n}+\lambda^{-2n}+O(\kappa^n),
 \qquad \kappa<\lambda^{-2},$$ and a zero at $z=\lambda$ of $$\label{eq:H-introduction}
 H(z)=(1-z)\exp\left(\sum_{n\ge1}\frac{q_nz^n}{n}\right).$$ Those sharper statements were left as a conjecture. The stated obstacle was precise: locate the critical-orbit factor inside an adapted Fredholm or kneading determinant.

We do this by resolving the quadratic critical point geometrically. The coordinate $x=-r\cos\theta$ is a two-sheeted branched cover of the component interval. Under this cover the nonuniformly expanding unimodal map becomes an ordinary analytic expanding circle map. The deck involution separates even and odd transfer sectors, and the one interval endpoint fixed by the dynamics becomes a branch point of the cover. At that point the circle multiplier is $\lambda^n$, whereas the interval multiplier is $\lambda^{2n}$. The entire correction $-\lambda^{-n}+\lambda^{-2n}$ comes from this mismatch.

The method is closely related in spirit to dynamical conjugacies and explicit postcritical factors for postcritically finite polynomials [@BaladiJiangRugh2002]. Our object, however, is a real component Perron weight with an absolute multiplier and a deck-parity projection. We therefore give the lift and the fixed-point bookkeeping directly rather than importing a complex-polynomial formula without checking conventions.

## Main results and logical status {#main-results-and-logical-status .unnumbered}

The conclusions divide into exact, unconditional, and numerical parts.

1.  The branched lift $F$ is a degree-two real-analytic expanding circle map. Its derivative is explicit and its minimum is exactly the postcritical square-root multiplier $\lambda$.

2.  The ordinary and deck-twisted fixed sets have the exact cardinalities $2^n-1$ and $2^n+1$. Their equivariant flat traces reconstruct the interval weight by $$q_n=E_{1,n}-O_{2,n}-\lambda^{-n}+\lambda^{-2n}.$$

3.  The trace identity exponentiates to the exact meromorphic factorization $$\mathcal Z(z)=\frac{D_{2,-}(z)}{D_{1,+}(z)}
      \frac{1-z/\lambda}{1-z/\lambda^2}.$$

4.  A strict pressure estimate proves that the odd $\beta=2$ determinant is nonzero at $z=\lambda$. Hence only one cancellation mechanism remains: an even non-Perron eigenvalue exactly equal to $\lambda^{-1}$.

5.  The statement "$H$ has a simple zero at $\lambda$" is proved equivalent to the absence of that eigenvalue. It is not promoted to an unconditional theorem here.

6.  Exhaustive multiprecision data and two independent determinant truncations place the leading reduced resonances near $0.20788030$ and $0.15252824$, both well below $\lambda^{-2}=0.35491084$. These are numerical diagnostics, not validated spectral enclosures.

The exact factorization is stronger than a fitted coefficient law but weaker than a proved uncanceled zero. Keeping these two statements distinct is the central logical point of the paper.

# Algebraic component and analytic circle lift {#sec:lift}

Let $u_{\mathrm c}$ be the unique root in $(1,2)$ of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and put $$\label{eq:constants}
 r=u_{\mathrm c}-1,
 \qquad
 \lambda=2u_{\mathrm c}r.$$ At 80 decimal places, $$\begin{aligned}
 u_{\mathrm c}&=1.5436890126920763615708559718017479865\ldots,\nonumber\\
 \lambda&=1.6785735104283222651037051293065732008\ldots.
 \label{eq:constants-numerical}\end{aligned}$$ The critical orbit is $$\label{eq:critical-orbit}
 0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r.$$

Set $f=f_{u_{\mathrm c}}$ and let $$\label{eq:S-definition}
 S=f^2|_{[-r,r]}.$$ Direct expansion gives $$\label{eq:S-polynomial}
 S(x)=-r+2u_{\mathrm c}^2x^2-u_{\mathrm c}^3x^4,
 \qquad
 S'(x)=4u_{\mathrm c}^2x(1-u_{\mathrm c}x^2).$$ The two restrictions to $[-r,0]$ and $[0,r]$ are full branches onto $[-r,r]$. In particular $S(-r)=S(r)=r$, $S(0)=-r$, and $$\label{eq:endpoint-multiplier}
 S'(r)=\lambda^2.$$

Consider the branched cover $$\label{eq:pi}
 \pi:\mathbb T\longrightarrow[-r,r],
 \qquad
 \pi(\theta)=-r\cos\theta,
 \qquad
 \mathbb T=\mathbb R/(2\pi\mathbb Z),$$ with deck involution $$\label{eq:iota}
 \iota(\theta)=-\theta.$$

[\[prop:analytic-lift\]]{#prop:analytic-lift label="prop:analytic-lift"} There is a unique orientation-preserving degree-two circle map $F$ with the chosen lift $\widetilde F(0)=\pi$ such that $$\label{eq:semiconjugacy}
 \pi\circ F=S\circ\pi.$$ The map $F$ is real analytic, commutes with $\iota$, and satisfies $$\label{eq:half-period}
 \widetilde F(\theta+\pi)=\widetilde F(\theta)+2\pi,
 \qquad
 \widetilde F(\theta+2\pi)=\widetilde F(\theta)+4\pi.$$ Writing $x=-r\cos\theta$, its derivative is $$\label{eq:lift-derivative}
 \boxed{
 F'(\theta)^2=
 \frac{16(1-u_{\mathrm c}x^2)^2}
 {u_{\mathrm c}(2-u_{\mathrm c}x^2)(1-x^2)}.}$$ Moreover $$\label{eq:min-expansion}
 \min_{\theta\in\mathbb T}F'(\theta)=\lambda>1,$$ with equality exactly over the two interval endpoints $x=\pm r$.

For an explicit construction, put $$\label{eq:alpha}
 \alpha(\theta)=
 \arccos\left(-\frac{S(-r\cos\theta)}r\right)\in[0,\pi].$$ On $0\le\theta\le2\pi$, define the real lift successively by $$\label{eq:piecewise-lift}
 \widetilde F(\theta)=
 \begin{cases}
  2\pi-\alpha(\theta),&0\le\theta\le\pi/2,\\
  2\pi+\alpha(\theta),&\pi/2\le\theta\le\pi,\\
  4\pi-\alpha(\theta),&\pi\le\theta\le3\pi/2,\\
  4\pi+\alpha(\theta),&3\pi/2\le\theta\le2\pi.
 \end{cases}$$ The endpoint values are $\pi,2\pi,3\pi,4\pi,5\pi$, so the pieces join and give degree two. Equation [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"} is immediate. The quadratic zeros at the apparent arccosine singularities cancel the quadratic branching of $\pi$; the analytic square-root theorem in a local coordinate therefore shows that the joined map is real analytic. The same conclusion also follows from the nonsingular derivative formula below. Evenness of $S$ gives [\[eq:half-period\]](#eq:half-period){reference-type="eqref" reference="eq:half-period"}, and uniqueness of the increasing lift gives $F\iota=\iota F$ on the circle.

Away from the branch points, differentiating [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"} and squaring yields $$\label{eq:derivative-intermediate}
 F'(\theta)^2
 =S'(x)^2\frac{r^2-x^2}{r^2-S(x)^2}.$$ Substitution of [\[eq:S-polynomial\]](#eq:S-polynomial){reference-type="eqref" reference="eq:S-polynomial"} and use of the cubic identity [\[eq:cubic\]](#eq:cubic){reference-type="eqref" reference="eq:cubic"} reduce this expression to [\[eq:lift-derivative\]](#eq:lift-derivative){reference-type="eqref" reference="eq:lift-derivative"}. Its right side is positive and analytic for $|x|\le r$, and hence extends the formula across all joined points.

It remains to locate the minimum. Put $t=x^2$. The logarithmic derivative of the right side of [\[eq:lift-derivative\]](#eq:lift-derivative){reference-type="eqref" reference="eq:lift-derivative"}, apart from a positive denominator, has numerator $$\label{eq:log-derivative-numerator}
 2-3u_{\mathrm c}+u_{\mathrm c}^2t.$$ The cubic changes sign between $3/2$ and $8/5$, so $3/2<u_{\mathrm c}<8/5$ and $0<r<3/5$. Therefore, for $0\le t\le r^2$, $$\label{eq:numerator-negative}
 2-3u_{\mathrm c}+u_{\mathrm c}^2t
 <2-\frac92+\left(\frac85\right)^2
 \left(\frac35\right)^2<0.$$ Thus $F'$ decreases as $|x|$ increases and is minimized at $|x|=r$. At $x=r$ the local quadratic semiconjugacy gives $F'(\theta)^2=S'(r)$, while at $x=-r$ it gives $F'(\theta)^2=-S'(-r)$; both values equal $\lambda^2$. Positivity of the lift derivative proves [\[eq:min-expansion\]](#eq:min-expansion){reference-type="eqref" reference="eq:min-expansion"}.

[\[cor:circle-counts\]]{#cor:circle-counts label="cor:circle-counts"} For every $n\ge1$, $$\label{eq:circle-counts}
 \#\operatorname{Fix}(F^n)=2^n-1,
 \qquad
 \#\operatorname{Fix}(\iota F^n)=2^n+1.$$

For the increasing real lift, $\widetilde F^n(\theta)-\theta$ has positive derivative and gains $(2^n-1)2\pi$ over one fundamental interval. It crosses each relevant multiple of $2\pi$ exactly once. Likewise $\widetilde F^n(\theta)+\theta$ is increasing and gains $(2^n+1)2\pi$.

# Deck-equivariant transfer operators {#sec:operators}

For an integer $\beta\ge0$, define the analytic transfer operator $$\label{eq:transfer}
 (\mathcal L_\beta\varphi)(\theta)
 =\sum_{F(\eta)=\theta}
 \frac{\varphi(\eta)}{F'(\eta)^\beta}.$$ Because $F$ is real analytic and uniformly expanding, its inverse branches extend as strict holomorphic contractions on a sufficiently thin complex neighborhood of the circle. On a standard holomorphic Banach space $\mathcal B$, $\mathcal L_\beta$ is nuclear of order zero, its Fredholm determinant is entire, and its nuclear traces are fixed-point traces [@Ruelle1976; @BaladiRuelle1996; @Baladi2000; @Baladi2018]. We use only these classical consequences.

Let $$\label{eq:J}
 (\mathcal J\varphi)(\theta)=\varphi(-\theta),
 \qquad
 P_\pm=\frac{I\pm\mathcal J}{2}.$$ Since $F$ commutes with $\iota$, so do $\mathcal L_\beta$ and $\mathcal J$. Write $$\label{eq:sector-operators}
 \mathcal L_{\beta,\pm}=\mathcal L_\beta|_{P_\pm\mathcal B},
 \qquad
 D_{\beta,\pm}(z)=\det(I-z\mathcal L_{\beta,\pm}).$$

For a periodic lift, put $$\label{eq:Dn}
 D_n(\theta)=(F^n)'(\theta)>1.$$ Define the ordinary and twisted fixed-point traces $$\begin{aligned}
 A_{\beta,n}
 &=\sum_{F^n\theta=\theta}
 \frac{D_n(\theta)^{-\beta}}
 {1-D_n(\theta)^{-1}},\label{eq:A-trace}\\
 B_{\beta,n}
 &=\sum_{\iota F^n\theta=\theta}
 \frac{D_n(\theta)^{-\beta}}
 {1+D_n(\theta)^{-1}}.\label{eq:B-trace}\end{aligned}$$

[\[prop:equivariant-traces\]]{#prop:equivariant-traces label="prop:equivariant-traces"} The flat traces on the two deck sectors are $$\label{eq:sector-traces}
 \operatorname{tr}^{\flat}(\mathcal L_{\beta,+}^n)
 =\frac{A_{\beta,n}+B_{\beta,n}}2,
 \qquad
 \operatorname{tr}^{\flat}(\mathcal L_{\beta,-}^n)
 =\frac{A_{\beta,n}-B_{\beta,n}}2.$$ Consequently $$\label{eq:determinant-traces}
 D_{\beta,\pm}(z)
 =\exp\left[-\sum_{n\ge1}
 \frac{z^n}{n}\operatorname{tr}^{\flat}(\mathcal L_{\beta,\pm}^n)\right]$$ as a germ at zero and, by the analytic expanding-map theorem, as its entire Fredholm continuation.

The trace of a weighted inverse branch $g$ at its fixed point is its weight divided by $1-g'$. For an inverse branch of $F^n$, this gives $D_n^{-\beta}/(1-D_n^{-1})$. Inserting $\mathcal J$ changes the inverse-branch derivative to $-D_n^{-1}$ and gives the denominator $1+D_n^{-1}$. Finally insert the projectors $P_\pm$ and use nuclear trace linearity. Exponentiating the trace series is the Fredholm determinant identity.

For the two sectors needed below, abbreviate $$\label{eq:E-O}
 E_{1,n}=\frac{A_{1,n}+B_{1,n}}2,
 \qquad
 O_{2,n}=\frac{A_{2,n}-B_{2,n}}2.$$

# Exact interval trace reconstruction {#sec:trace-identity}

Recall the component Perron periodic weight $$\label{eq:q-definition}
 q_n=\sum_{x\in\operatorname{Fix}(S^n)}\frac1{|(S^n)'(x)|}.$$ Every inverse word of length $n$ has one fixed point, so $S^n$ has exactly $2^n$ fixed points, including the endpoint $r$.

[\[thm:trace-identity\]]{#thm:trace-identity label="thm:trace-identity"} For every integer $n\ge1$, $$\label{eq:main-trace-identity}
 \boxed{
 q_n=E_{1,n}-O_{2,n}-\lambda^{-n}+\lambda^{-2n}.}$$

First consider $x\in\operatorname{Fix}(S^n)$ with $x\ne r$. Its two lifts are $\theta$ and $-\theta$. There are two cases.

If $F^n\theta=\theta$, both lifts occur in the ordinary fixed set and neither occurs in the twisted fixed set. Put $a=D_n(\theta)^{-1}$. Their combined contribution to $E_{1,n}-O_{2,n}$ is $$\label{eq:untwisted-pair}
 \frac{a}{1-a}-\frac{a^2}{1-a}=a.$$ If instead $F^n\theta=-\theta$, both lifts occur in the twisted fixed set and their contribution is $$\label{eq:twisted-pair}
 \frac{a}{1+a}+\frac{a^2}{1+a}=a.$$ Differentiating the semiconjugacy away from the branch points shows in both cases that $D_n(\theta)=|(S^n)'(x)|$. Thus every nonbranch interval fixed point is counted with exactly its desired weight.

It remains to inspect the branch fixed point. The interval endpoint $r$ has weight $$\label{eq:interval-branch-weight}
 |(S^n)'(r)|^{-1}=\lambda^{-2n}.$$ Its unique circle lift is $\theta=\pi$. This point belongs to both $\operatorname{Fix}(F^n)$ and $\operatorname{Fix}(\iota F^n)$ and has $D_n(\pi)=\lambda^n$. With $a=\lambda^{-n}$, its projected circle contribution is $$\label{eq:orbifold-branch-weight}
 \frac12\left(\frac a{1-a}+\frac a{1+a}\right)
 -\frac12\left(\frac {a^2}{1-a}-\frac {a^2}{1+a}\right)
 =a.$$ The circle orbifold trace therefore assigns $\lambda^{-n}$ where the interval trace requires $\lambda^{-2n}$. Subtracting the former and restoring the latter proves [\[eq:main-trace-identity\]](#eq:main-trace-identity){reference-type="eqref" reference="eq:main-trace-identity"}.

[\[rem:two-weights\]]{#rem:two-weights label="rem:two-weights"} Neither the $\beta=1$ nor the $\beta=2$ flat trace alone equals $q_n$. The elementary identities $$\label{eq:denominator-cancellation}
 \frac{a}{1-a}-\frac{a^2}{1-a}=a,
 \qquad
 \frac{a}{1+a}+\frac{a^2}{1+a}=a$$ remove the inverse-branch fixed-point denominator. Deck parity selects the correct sign in the two lift cases. This is the one-dimensional Lefschetz-type cancellation behind the factorization.

# Fredholm factorization and noncancellation {#sec:factorization}

Define the component weighted zeta function near the origin by $$\label{eq:zeta-definition}
 \mathcal Z(z)=\exp\left(\sum_{n\ge1}\frac{q_nz^n}{n}\right).$$

[\[thm:factorization\]]{#thm:factorization label="thm:factorization"} As a formal germ at zero, and hence throughout its meromorphic continuation, $$\label{eq:main-factorization}
 \boxed{
 \mathcal Z(z)=
 \frac{D_{2,-}(z)}{D_{1,+}(z)}
 \frac{1-z/\lambda}{1-z/\lambda^2}.}$$

By [\[prop:equivariant-traces\]](#prop:equivariant-traces){reference-type="ref" reference="prop:equivariant-traces"}, $$\label{eq:det-ratio-log}
 \log\frac{D_{2,-}(z)}{D_{1,+}(z)}
 =\sum_{n\ge1}\frac{(E_{1,n}-O_{2,n})z^n}{n}.$$ The two endpoint terms exponentiate exactly: $$\begin{aligned}
 \exp\left[\sum_{n\ge1}
 \frac{(-\lambda^{-n}+\lambda^{-2n})z^n}{n}\right]
 &=\frac{1-z/\lambda}{1-z/\lambda^2}.
 \label{eq:postcritical-exponential}\end{aligned}$$ Insert [\[thm:trace-identity\]](#thm:trace-identity){reference-type="ref" reference="thm:trace-identity"}. The identity first holds where the trace series converge. Since the sector Fredholm determinants are entire, the right side supplies the stated meromorphic continuation and uniqueness of analytic continuation finishes the proof.

The Perron operator $\mathcal L_1$ preserves Lebesgue integral and has a simple eigenvalue one because $F$ is topologically mixing. Its invariant density is even by deck symmetry. Therefore $$\label{eq:perron-factor}
 D_{1,+}(z)=(1-z)\widetilde D_{1,+}(z),$$ where $\widetilde D_{1,+}$ is entire. Define $$\label{eq:G-definition}
 G(z)=\frac{D_{2,-}(z)}{\widetilde D_{1,+}(z)}.$$ Then [\[thm:factorization\]](#thm:factorization){reference-type="ref" reference="thm:factorization"} becomes $$\label{eq:H-factorization}
 H(z)=(1-z)\mathcal Z(z)
 =\frac{1-z/\lambda}{1-z/\lambda^2}G(z).$$ The displayed numerator is an exact meromorphic factor. Whether it is an actual zero is now a question about $G$ at one point.

## The odd second-order sector cannot cancel

Let $P(\phi)$ denote topological pressure for the expanding circle map $F$.

[\[prop:pressure-bound\]]{#prop:pressure-bound label="prop:pressure-bound"} The full $\beta=2$ transfer operator, and hence its odd restriction, satisfies $$\label{eq:L2-bound}
 r(\mathcal L_{2,-})\le r(\mathcal L_2)
 =\exp P(-2\log F')<\lambda^{-1}.$$ In particular, $$\label{eq:D2-nonzero}
 D_{2,-}(z)\ne0\quad\text{for }|z|\le\lambda.$$

On a Hölder space, the spectral-radius/pressure identity is standard for a mixing expanding map [@Ruelle1989; @Baladi2000]; the holomorphic realization used in the Fredholm determinant has no additional eigenvalues outside this bound. Let $\mu_2$ be the equilibrium state of $-2\log F'$. It has full support. Put $$\label{eq:chi}
 \chi(\mu_2)=\int\log F'\,d\mu_2.$$ By [\[prop:analytic-lift\]](#prop:analytic-lift){reference-type="ref" reference="prop:analytic-lift"}, $F'\ge\lambda$, with strict inequality on a nonempty open set. Full support gives $$\label{eq:strict-chi}
 \chi(\mu_2)>\log\lambda.$$ Ruelle's entropy inequality in dimension one gives $h_{\mu_2}(F)\le\chi(\mu_2)$. Consequently $$\begin{aligned}
 P(-2\log F')
 &=h_{\mu_2}(F)-2\chi(\mu_2)\nonumber\\
 &\le-\chi(\mu_2)<-\log\lambda.
 \label{eq:pressure-chain}\end{aligned}$$ This proves [\[eq:L2-bound\]](#eq:L2-bound){reference-type="eqref" reference="eq:L2-bound"}. Fredholm zeros are reciprocals of nonzero eigenvalues with algebraic multiplicity, giving [\[eq:D2-nonzero\]](#eq:D2-nonzero){reference-type="eqref" reference="eq:D2-nonzero"}.

[\[cor:noncancellation\]]{#cor:noncancellation label="cor:noncancellation"} The following statements are equivalent:

1.  $H$ has a simple zero at $z=\lambda$;

2.  $\widetilde D_{1,+}(\lambda)\ne0$;

3.  $\lambda^{-1}$ is not a non-Perron eigenvalue of $\mathcal L_{1,+}$.

By [\[prop:pressure-bound\]](#prop:pressure-bound){reference-type="ref" reference="prop:pressure-bound"}, the numerator $D_{2,-}(\lambda)$ in [\[eq:G-definition\]](#eq:G-definition){reference-type="eqref" reference="eq:G-definition"} is nonzero. Hence $G$ is holomorphic and nonzero at $\lambda$ exactly when $\widetilde D_{1,+}(\lambda)\ne0$. In that case the explicit factor $1-z/\lambda$ in [\[eq:H-factorization\]](#eq:H-factorization){reference-type="eqref" reference="eq:H-factorization"} is a simple zero. If $\widetilde D_{1,+}$ vanishes to order $m\ge1$, the local order of $H$ at $\lambda$ is $1-m$, so it is not a simple zero. The Fredholm spectral interpretation gives the equivalence with (iii).

This corollary is deliberately an equivalence, not an assertion that (iii) holds. It reduces a qualitative zeta conjecture to one sharply formulated spectral exclusion.

## A stronger sufficient spectral gap

Let $$\label{eq:reduced-radii}
 r_1=\sup\{|\mu|:\mu\in\operatorname{spec}(\mathcal L_{1,+}),\ \mu\ne1\},
 \qquad
 r_2=r(\mathcal L_{2,-}).$$

[\[prop:conditional-sharp\]]{#prop:conditional-sharp label="prop:conditional-sharp"} If $$\label{eq:strong-gap}
 \max\{r_1,r_2\}<\lambda^{-2},$$ then, for every $\kappa$ with $\max\{r_1,r_2\}<\kappa<\lambda^{-2}$, $$\label{eq:sharp-law-conditional}
 q_n=1-\lambda^{-n}+\lambda^{-2n}+O(\kappa^n).$$ Moreover $H$ has a simple zero at $\lambda$, a simple pole at $\lambda^2$, and $G$ is holomorphic and nonzero on a disk containing $\{|z|\le\lambda^2\}$.

Condition [\[eq:strong-gap\]](#eq:strong-gap){reference-type="eqref" reference="eq:strong-gap"} makes both $\widetilde D_{1,+}$ and $D_{2,-}$ zero-free on a disk of radius strictly larger than $\lambda^2$. Thus $G$ and $1/G$ are holomorphic there. The logarithmic derivative of $G$ has Taylor coefficients $q_n-1+\lambda^{-n}-\lambda^{-2n}$; Cauchy's estimate gives [\[eq:sharp-law-conditional\]](#eq:sharp-law-conditional){reference-type="eqref" reference="eq:sharp-law-conditional"}. Nonvanishing of $G$ at $\lambda$ and $\lambda^2$ leaves the two explicit factors in [\[eq:H-factorization\]](#eq:H-factorization){reference-type="eqref" reference="eq:H-factorization"} uncanceled.

# Exhaustive numerical audit {#sec:numerics}

The numerical work has three independent layers: direct interval inverse words, circle fixed-point traces, and finite Fredholm series. NumPy, SciPy, mpmath, and Matplotlib were used for the implementation [@HarrisEtAl2020; @VirtanenEtAl2020; @JohanssonEtAl2025; @Hunter2007].

## Interval inverse words and multiprecision tail

The positive inverse branch of $S$ is evaluated in the rationalized form $$\label{eq:inverse-branch}
 g(y)=
 \sqrt{
 \frac{y+r}{u_{\mathrm c}^2\left(1+\sqrt{(1-y)/u_{\mathrm c}}\right)}}.$$ The two inverse branches are $\pm g$. For every binary word of length $n$ we iterate the corresponding contraction to its unique fixed point and multiply the inverse derivatives along the word. The main audit enumerates all $2^{20}=1{,}048{,}576$ words. An independent mpmath calculation recomputes every contribution for $14\le n\le20$ at 50-decimal working precision, split over 64 processes. The algebraic constants are separately solved at 80 decimal places.

Put $$\label{eq:e-definition}
 e_n=q_n-\left(1-\lambda^{-n}+\lambda^{-2n}\right).$$ By [\[thm:trace-identity\]](#thm:trace-identity){reference-type="ref" reference="thm:trace-identity"}, this is also exactly $$\label{eq:e-trace}
 e_n=E_{1,n}-O_{2,n}-1.$$ Representative multiprecision values are shown in [1](#tab:tail){reference-type="ref" reference="tab:tail"}. The ratio decreases smoothly toward the Fredholm estimate below. Ordinary long-double subtraction begins to lose the tiny remainder after $n\approx17$; the values in the table are the independent multiprecision results, not the precision-limited subtraction.

::: {#tab:tail}
    $n$                    $q_n$                           $e_n$    $e_n/e_{n-1}$
  ----- ------------------------ ------------------------------- ----------------
     14   $0.999291195348810814$   $2.77751561116\times10^{-10}$              ---
     16   $0.999748322267819715$   $1.20764088766\times10^{-11}$   $0.2084178054$
     18   $0.999910662330463479$   $5.23584683219\times10^{-13}$   $0.2081683796$
     20   $0.999968291264484914$   $2.26661348637\times10^{-14}$   $0.2080350182$

  : Multiprecision component trace and exact-postcritical remainder.
:::

![Postcritical factor audit. Top left: the exact trace and the two explicit postcritical terms. Top right: the remainder over thirteen orders of magnitude. Bottom left: successive ratios approach approximately $0.20788$, slightly below the reference $\lambda^{-3}$. Bottom right: the centered truncation zero approaches $\lambda$ while the deflated value at $\lambda$ stabilizes. The tail points use 50-decimal arithmetic.](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/figures/postcritical_zeta_factorization.pdf>){#fig:postcritical width="\\textwidth"}

## Circle traces and the exact reconstruction

For each $1\le n\le10$, the monotone lift equations $$\label{eq:root-equations}
 \widetilde F^n(\theta)-\theta=2\pi k,
 \qquad
 \widetilde F^n(\theta)+\theta=2\pi k$$ are solved exhaustively. The fixed-set cardinalities agree exactly with [\[cor:circle-counts\]](#cor:circle-counts){reference-type="ref" reference="cor:circle-counts"}, and [\[eq:main-trace-identity\]](#eq:main-trace-identity){reference-type="eqref" reference="eq:main-trace-identity"} agrees with the direct interval calculation to at worst $1.16\times10^{-14}$. Selected rows are in [2](#tab:lift-audit){reference-type="ref" reference="tab:lift-audit"}.

::: {#tab:lift-audit}
    $n$   $\#\operatorname{Fix}(F^n)$   $\#\operatorname{Fix}(\iota F^n)$    $E_{1,n}-O_{2,n}$    reconstruction error
  ----- ----------------------------- ----------------------------------- -------------------- -----------------------
      1                             1                                   3   $1.05556563078010$   $-1.11\times10^{-16}$
      4                            15                                  17   $1.00132623654253$    $1.67\times10^{-15}$
      8                           255                                 257   $1.00000319448343$    $1.15\times10^{-14}$
     10                          1023                                1025   $1.00000014389139$    $7.22\times10^{-15}$

  : Deck-equivariant circle trace audit.
:::

## Centered zero and reduced Fredholm resonances

Let $H_N$ be the degree-$N$ Taylor polynomial obtained formally from $q_1,\ldots,q_N$. Let $$\label{eq:GN}
 \log G_N(\lambda)=\sum_{n=1}^N\frac{e_n\lambda^n}{n}.$$ The smallest positive zero $z_N$ of $H_N$ and the deflated value stabilize as in [3](#tab:zeta-convergence){reference-type="ref" reference="tab:zeta-convergence"}.

::: {#tab:zeta-convergence}
    $N$            $z_N$               $z_N-\lambda$   $G_N(\lambda)$
  ----- ---------------- --------------------------- ----------------
      6   $1.7215098224$   $4.29363120\times10^{-2}$   $1.1430116641$
     10   $1.6833139574$   $4.74044698\times10^{-3}$   $1.1431435791$
     14   $1.6791563531$   $5.82842708\times10^{-4}$   $1.1431449505$
     18   $1.6786466196$   $7.31091461\times10^{-5}$   $1.1431449658$
     20   $1.6785994451$   $2.59346262\times10^{-5}$   $1.1431449660$

  : Centered-zeta and deflated-value convergence.
:::

The reduced determinant series are computed separately from $E_{1,n}-1$ and $O_{2,n}$: $$\begin{aligned}
 \widetilde D_{1,+}(z)
 &=\exp\left[-\sum_{n\ge1}\frac{(E_{1,n}-1)z^n}{n}\right],
 \label{eq:D1-reduced-series}\\
 D_{2,-}(z)
 &=\exp\left[-\sum_{n\ge1}\frac{O_{2,n}z^n}{n}\right].
 \label{eq:D2-series}\end{aligned}$$ At truncation degree ten, the first positive zeros are $$\label{eq:fredholm-zeros-numerical}
 4.81046066,
 \qquad
 6.55616298,$$ corresponding to inferred leading positive resonances $$\label{eq:resonances-numerical}
 \mu_{1,+}^{\mathrm{red}}\approx0.20788030,
 \qquad
 \mu_{2,-}\approx0.15252824.$$ Both estimates stabilize by degree four in the displayed digits relevant here. They are far below $$\label{eq:thresholds}
 \lambda^{-2}=0.3549108444\ldots,
 \qquad
 \lambda^{-1}=0.5957439420\ldots.$$ They explain the tail ratio in [1](#tab:tail){reference-type="ref" reference="tab:tail"} and provide a large numerical noncancellation margin. They remain polynomial-truncation estimates, not a computer-assisted proof that the full operator spectra obey these bounds.

![Circle-lift and Fredholm diagnostics. Top left: the exact analytic lift derivative and its minimum $\lambda$. Top right: interval traces reconstructed from ordinary and twisted circle traces. Bottom left: the two reduced flat-trace sequences. Bottom right: inferred leading resonances are well separated from the only possible cancellation value $\lambda^{-1}$.](<../../../../../zeta_mvp0/papers/RH-12-postcritical-weighted-zeta-factorization/figures/circle_lift_fredholm_audit.pdf>){#fig:lift-fredholm width="\\textwidth"}

# What is proved and what remains {#sec:status}

The trace identity [\[eq:main-trace-identity\]](#eq:main-trace-identity){reference-type="eqref" reference="eq:main-trace-identity"} proves that the two terms $-\lambda^{-n}+\lambda^{-2n}$ are geometrically exact. They are the difference between a square-root multiplier at a branch point of the circle cover and the true multiplier at the interval endpoint. This identifies the postcritical rational factor in [\[eq:main-factorization\]](#eq:main-factorization){reference-type="eqref" reference="eq:main-factorization"} without any large-$n$ approximation.

There are nevertheless two distinct meanings of the word "factor." In a meromorphic identity, an explicit numerator may cancel a zero of the denominator. An actual zeta zero requires the quotient to be holomorphic and nonzero at the point. eliminates the odd second-order determinant as a source of cancellation at $\lambda$. shows that the entire remaining issue is whether $\lambda^{-1}$ is an even non-Perron resonance of $\mathcal L_1$.

The stronger coefficient law [\[eq:previous-sharp\]](#eq:previous-sharp){reference-type="eqref" reference="eq:previous-sharp"} requires more than noncancellation at one point. It follows from the disk bound [\[eq:strong-gap\]](#eq:strong-gap){reference-type="eqref" reference="eq:strong-gap"}, which also prevents cancellation of the pole at $\lambda^2$. The data strongly support this bound: the two estimated reduced radii are $0.20788$ and $0.15253$, versus the threshold $0.35491$. Turning that separation into a theorem would naturally require either an analytic cone/Lasota--Yorke estimate sharp enough for this specific lift or a validated approximation of the two Fredholm operators.

We isolate the remaining statement for future use.

[\[conj:disk-bound\]]{#conj:disk-bound label="conj:disk-bound"} For the analytic lift in [\[prop:analytic-lift\]](#prop:analytic-lift){reference-type="ref" reference="prop:analytic-lift"}, $$\label{eq:disk-bound-conjecture}
 r_1<\lambda^{-2},
 \qquad
 r_2<\lambda^{-2},$$ with $r_1,r_2$ defined in [\[eq:reduced-radii\]](#eq:reduced-radii){reference-type="eqref" reference="eq:reduced-radii"}.

By [\[prop:conditional-sharp\]](#prop:conditional-sharp){reference-type="ref" reference="prop:conditional-sharp"}, this one operator statement implies the full sharp coefficient law conjectured in the preceding paper, including an uncanceled simple zero at $\lambda$ and an uncanceled simple pole at $\lambda^2$. The present paper proves the factorization and the equivalence; it does not use [\[conj:disk-bound\]](#conj:disk-bound){reference-type="ref" reference="conj:disk-bound"} as an assumption in any unconditional result.

# Conclusion

The critical point of the interval map can be removed by a two-sheeted cosine cover. On the resulting analytic expanding circle map, deck parity and two adjacent transfer weights produce an exact Lefschetz cancellation. The only place where the circle and interval traces disagree is the repelling branch endpoint, and that disagreement is exactly $-\lambda^{-n}+\lambda^{-2n}$.

Exponentiation gives a closed Fredholm factorization of the weighted zeta function. A strict pressure estimate rules out cancellation from the odd $\beta=2$ sector, reducing the previously conjectured zero to one explicit non-Perron spectral exclusion. The multiprecision and Fredholm audits show a wide numerical margin for that exclusion but are not substituted for its proof. Thus the main advance is both positive and sharply delimited: the postcritical factor is now exact; its global noncancellation remains a concrete operator bound.

# Reproducibility {#reproducibility .unnumbered}

The source code, tests, exhaustive periodic data, multiprecision tail, figures, and manuscript are archived with this paper [@WangPostcriticalCode2026]. The test suite checks the algebraic parameter, semiconjugate lift, exact fixed-set counts, trace reconstruction, formal determinant algebra, and an independent mpmath calculation. The parallel high-precision script records its working precision and process count in the output file.
