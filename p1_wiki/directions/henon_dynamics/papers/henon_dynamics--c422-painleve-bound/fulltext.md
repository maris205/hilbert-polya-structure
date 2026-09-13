---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c422-painleve-bound"
canonical_tex: "henon_dynamics/research_c419_c423/papers/C422_painleve_bound/main.tex"
canonical_pdf: "henon_dynamics/research_c419_c423/papers/C422_painleve_bound/main.pdf"
source_sha256: "d212289fdb5ff08ca28c50b7e87f8d419f6caf702c5d986c4326b32535fa679b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A uniform orbit bound for discrete Painlevé I\texorpdfstring over finite fields

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c419_c423/papers/C422_painleve_bound>)
- [规范 TeX](<../../../../../henon_dynamics/research_c419_c423/papers/C422_painleve_bound/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c419_c423/papers/C422_painleve_bound/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c419_c423/papers/C422_painleve_bound/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c419_c423/papers/C422_painleve_bound/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove a uniform upper bound for every orbit of the resolved discrete Painlevé I system over a finite field $\mathbb F_q$. If the nonzero phase multiplier $s$ has multiplicative order $r$, then every state in the original torus-plus-four-lines space is periodic, and its least native period $\ell$ satisfies $r\mid\ell$ and $\ell/r\le q+1+2\sqrt q$. The existence of an invariant alone does not justify applying Hasse's theorem to every orbit, because special fibres may be singular, reducible or multiple. We address this issue on an explicit eight-blowup compactification. An integral boundary-lattice calculation and four local face-polynomial conditions show that any nonconstant regular function has a uniform boundary pole order divisible by $r$. The known matrix integral realizes pole order $r$, forcing each finite geometric fibre to be integral and reduced of arithmetic genus one. Smooth fibres satisfy Hasse's bound, while normalization bounds singular fibres by $q+2$ rational points. The proof includes every exceptional-line point and characteristics two and three; it requires neither a discriminant formula nor generic smoothness of the fibration.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  A uniform orbit bound for discrete Painlevé I\
  over finite fields
```

## Markdown 正文

# Introduction and main results {#sec:introduction}

A finite-field orbit of a nonautonomous rational map carries two clocks: the original update and the return of its coefficients. For the discrete Painlevé I map $$\label{eq:torus-map-intro}
X=\frac{st}{sx-y},\qquad Y=\frac{sx}{y},\qquad T=st,$$ the phase multiplier $s\in\mathbb F_q^*$ has finite multiplicative order $r$. The natural question is whether the orbit length divided by $r$ admits the same upper bound as the number of points on an elliptic curve. Here $q$ denotes the field cardinality, whereas $s$ is the iterative parameter traditionally denoted by $q$ in the name $q$-Painlevé I.

Joshi and Roffelsen defined the resolved state space for [\[eq:torus-map-intro\]](#eq:torus-map-intro){reference-type="eqref" reference="eq:torus-map-intro"}, constructed a matrix integral at every root-of-unity parameter, and proposed this upper bound [@JoshiRoffelsen2026]. The state space includes four accessible exceptional affine lines. Deleting them would remove valid orbits, including points whose line coordinate is zero. We retain exactly their seven native branches, displayed in Table [2](#tab:native){reference-type="ref" reference="tab:native"} below. Conjecture and theorem numbers attributed to that source in this article refer to the explicitly identified arXiv v2 text.

[\[thm:period\]]{#thm:period label="thm:period"} Let $k=\mathbb F_q$, choose $s,t_0\in k^*$, and put $r=\mathop{\mathrm{ord}}_{k^*}(s)$. Apply the seven branches in Table [2](#tab:native){reference-type="ref" reference="tab:native"} on all states $$\label{eq:state-domain-intro}
\begin{split}
\gamma&=(j,x,y,t,s),\qquad t\in t_0\langle s\rangle,\\
(j,x,y)&\in\bigl(\{0\}\times(k^*)^2\bigr)
\sqcup\bigsqcup_{j=1}^{4}\bigl(\{j\}\times\{0\}\times k\bigr).
\end{split}$$ Every state is periodic. If $\ell$ is its least period under one native branch update, then $$\label{eq:main-bound}
r\mid\ell,\qquad \frac{\ell}{r}\le q+1+2\sqrt q.$$

This proves the upper-bound part of the source's Conjecture 1.2.A. The theorem is uniform in the finite field, the phase orbit, the order $r$, and the ordinary state. In particular, there is no exclusion in characteristics two or three. The counted objects are distinct states of the resolved system, not lengths of fixed-point schemes.

The geometric issue is stronger than the existence of an invariant. A generic genus-one fibre does not control reducible or multiple special fibres, and Hasse's theorem applies to smooth elliptic curves, not to an arbitrary affine equation. We prove the following statement on the actual compactification of the ordinary state space.

[\[thm:fibres-intro\]]{#thm:fibres-intro label="thm:fibres-intro"} Let $S_{t,s}$ be the smooth rational surface obtained by the eight blowups in Table [4](#tab:blowups){reference-type="ref" reference="tab:blowups"}, and let $D$ be its reduced eight-component boundary cycle. For every nonzero phase $t$, the Joshi--Roffelsen integral extends to a morphism $$f_t:S_{t,s}\longrightarrow\mathbb P^1,
\qquad f_t^{-1}(\infty)=rD.$$ Every finite geometric fibre is integral and reduced, has arithmetic genus one, and lies entirely in $U_{t,s}=S_{t,s}\setminus D$.

Arithmetic genus one in this statement does not assert smoothness. When a finite fibre is singular, its normalization has genus zero and there is exactly one geometric singular point. This gives the bound $q+2$ without classifying the singularity or assuming that an orbit contains a smooth rational point.

## Prior inputs and the proof mechanism

The original resolution, invariant, conjectured bound and local leading term of the invariant belong to Joshi--Roffelsen [@JoshiRoffelsen2026 Definitions 2.1--2.2, Algorithm 1 and Theorem 3.1]. The connection between roots of unity and Halphen pencils is also established prior work. In particular, Carstea--Takenawa [@CarsteaTakenawa2012 Theorem 2.2 and Remark 2.3] give a criterion using a complex period map. We do not specialize that analytic argument to small characteristic. Table [1](#tab:ownership){reference-type="ref" reference="tab:ownership"} separates these inputs from the all-finite-fibre argument used here.

::: {#tab:ownership}
  Input                                      Role and scope
  ------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Joshi--Roffelsen [@JoshiRoffelsen2026]     Resolved native system, proposed upper bound, matrix integral and its nonzero leading coefficient.
  Carstea--Takenawa [@CarsteaTakenawa2012]   Roots-of-unity Halphen-pencil context; the inspected criterion uses a complex period map.
  This article                               Integral boundary lattice and minimal-pole divisibility force every finite fibre to be integral and reduced in all allowed characteristics; smooth and singular point counts then bound native periods.

  : Roles of the main inputs. The new conclusion concerns every finite fibre of the specified resolved surface; neither the invariant nor the root-of-unity mechanism is claimed as new.
:::

There are three linked steps. First, the integral Picard lattice and adjunction show that an integral curve disjoint from the boundary has class $dD$ for a positive integer $d$. Second, every regular nonconstant function on $U$ has pole divisor $mD$, and four explicit face-root conditions force $s^m=1$. Third, the source integral has exact pole divisor $rD$. Applying the divisibility condition separately to the components of a finite fibre leaves room for only one component with multiplicity one.

These are algebraic calculations on the specified surface, with integer intersection numbers and local-ring multiplicities. They do not use a proposed formula for singular values, a section of the fibration, a translation law, or an identification with a spectral curve. The underlying tools are classical; the conclusion is the uniform all-finite-fibre statement needed for the original orbit bound.

Section [2](#sec:states){reference-type="ref" reference="sec:states"} fixes the states and proves bijectivity. Section [3](#sec:surface){reference-type="ref" reference="sec:surface"} constructs the compactification and computes its boundary lattice. Sections [4](#sec:poles){reference-type="ref" reference="sec:poles"} and [5](#sec:integral){reference-type="ref" reference="sec:integral"} establish the minimal pole order and the exact divisor of the source integral. Section [6](#sec:fibres){reference-type="ref" reference="sec:fibres"} proves Theorem [\[thm:fibres-intro\]](#thm:fibres-intro){reference-type="ref" reference="thm:fibres-intro"}, and Section [7](#sec:periods){reference-type="ref" reference="sec:periods"} converts the fibre point counts into Theorem [\[thm:period\]](#thm:period){reference-type="ref" reference="thm:period"}.

# The resolved states and the native clock {#sec:states}

Fix $k=\mathbb F_q$, $s,t_0\in k^*$, and $r=\mathop{\mathrm{ord}}_{k^*}(s)$. The native state space is [\[eq:state-domain-intro\]](#eq:state-domain-intro){reference-type="eqref" reference="eq:state-domain-intro"}. At a fixed phase the torus states have label $j=0$. For $1\le j\le4$, write $L_j$ for the exceptional affine line with states $(j,0,v,t,s)$, where $v\in k$. The line parameter $v$ is the third coordinate of the state, not necessarily the rational coordinate $y$ in a torus chart.

::: {#tab:native}
  Input condition   New $(j',x',y')$
  ----------------- ----------------------
  $j=0,\ sx\ne y$   $(0,st/(sx-y),sx/y)$
  $j=0,\ sx=y$      $(1,0,t/x)$
  $j=1$             $(2,0,st(1-sy))$
  $j=2$             $(3,0,sy)$
  $j=3$             $(4,0,s(sy-t)/t)$
  $j=4,\ y\ne0$     $(0,-s^2t/y,1)$
  $j=4,\ y=0$       $(1,0,0)$

  : The seven native branches. In every row the phase changes by $t'=st$, and $s'=s$. On an exceptional line the third state coordinate is allowed to vanish.
:::

The update in Table [2](#tab:native){reference-type="ref" reference="tab:native"} is defined at every state. In its first row the denominator $sx-y$ is nonzero by assumption; the other denominators are powers or products of the nonzero phase parameters and nonzero coordinates explicitly stipulated by the row. The rows are disjoint and exhaust the domain. In particular, the final row is part of the evolution, not a convention for discarding a pole.

[\[prop:permutation\]]{#prop:permutation label="prop:permutation"} The native update is a bijection on the finite union of phases $t_0\langle s\rangle$. The same branch formulas give a bijection between the state sets at phases $t$ and $st$ over any field containing the nonzero parameters.

Let an output have phase $T$. Its input phase must be $T/s$. The complete inverse is Table [3](#tab:inverse){reference-type="ref" reference="tab:inverse"}.

::: {#tab:inverse}
  Output at phase $T$        Input at phase $T/s$
  -------------------------- -----------------------------------------------
  Torus $(X,Y)$, $Y\ne1$     Torus $\bigl(TY/[sX(Y-1)],\ T/[X(Y-1)]\bigr)$
  Torus $(X,1)$              $L_4$ coordinate $-sT/X$
  $L_1$ coordinate $W\ne0$   Torus $\bigl(T/(sW),T/W\bigr)$
  $L_1$ coordinate $0$       $L_4$ coordinate $0$
  $L_2$ coordinate $W$       $L_1$ coordinate $(1-W/T)/s$
  $L_3$ coordinate $W$       $L_2$ coordinate $W/s$
  $L_4$ coordinate $W$       $L_3$ coordinate $T(W+s)/s^3$

  : The unique preceding state for an output at phase $T$. Every input has phase $T/s$; $L_j$ denotes the exceptional line with label $j$, parametrized by its third state coordinate.
:::

For a torus output with $Y\ne1$, the equations $Y=sx/y$ and $X=T/(sx-y)$ give $$y=\frac{T}{X(Y-1)},\qquad
x=\frac{TY}{sX(Y-1)}.$$ Both are nonzero, and $sx-y=T/X\ne0$. A torus output with $Y=1$ instead has the unique input on $L_4$ with coordinate $-sT/X\ne0$. A nonzero $L_1$ output with coordinate $W$ comes from the torus point $(T/(sW),T/W)$, which satisfies $sx=y$; a zero $L_1$ output comes from the zero point of $L_4$. These alternatives are disjoint.

The remaining line maps are affine with nonzero slope. Solving them at phase $T/s$ gives the last three rows. In particular, the equation for an $L_4$ output is $$W=\frac{s\bigl(sv-T/s\bigr)}{T/s}
=\frac{s^3v}{T}-s,$$ so $v=T(W+s)/s^3$. This also checks the phase power in that inverse formula. Substitution verifies all seven rows, proving bijectivity. The fixed finite phase union is therefore permuted.

Every state consequently has a least positive native period. If it returns after $n$ updates, its phase satisfies $s^nt=t$, so $r\mid n$. The exact relation between the least native period and the fixed-phase return period will be used after the invariant has been extended to every ordinary point.

# The compactification and its boundary lattice {#sec:surface}

The geometry will first be described over an arbitrary field containing $s,t\ne0$. Intersection and component arguments will then be made over its algebraic closure. All blowup centres and formulas are defined over the ground field.

## Eight blowups and exactly four accessible lines

Start with $\mathbb P^1_x\times\mathbb P^1_y$, and make the eight blowups in Table [4](#tab:blowups){reference-type="ref" reference="tab:blowups"}. Centres over disjoint points may be treated in either order. Let $S=S_{t,s}$ be the resulting smooth projective rational surface. Write $H_x,H_y$ for the pullbacks of the classes of $x=\text{constant}$ and $y=\text{constant}$. The symbols $E_i$ denote total exceptional classes, rather than strict transforms throughout the sequence.

::: {#tab:blowups}
  Class   Centre
  ------- --------------------------------------------------------------------------------------------------
  $E_1$   $(x,y)=(\infty,1)$.
  $E_2$   $(x,y)=(0,\infty)$.
  $E_3$   On the first exceptional curve over $(0,\infty)$, at $xy=t$.
  $E_4$   $(x,y)=(0,0)$.
  $E_5$   The intersection of the first exceptional curve over $(0,0)$ with the strict transform of $y=0$.
  $E_6$   On the exceptional curve created by the preceding blowup, at $x^2/y=t$.
  $E_7$   $(x,y)=(\infty,\infty)$.
  $E_8$   On the first exceptional curve over $(\infty,\infty)$, at $y/x=s$.

  : The eight blowups of $\mathbb P^1_x\times\mathbb P^1_y$. Each $E_i$ denotes the total exceptional class. The conditions for infinitely near centres are evaluated on the indicated exceptional curve.
:::

For the three infinitely near smooth-boundary centres $E_3,E_6,E_8$, coordinates immediately before the last blowup are respectively $$\label{eq:pre-blowup-charts}
(x,y)=(uv,u^{-1}),\qquad
(uv,u^2v),\qquad ((uv)^{-1},u^{-1}).$$ The centres are $(u,v)=(0,t),(0,t),(0,s)$. The remaining smooth-boundary blowup $E_1$ has centre $x^{-1}=0,y=1$. Thus none of these four centres is a boundary node, in any characteristic, because $s,t\ne0$.

The free Picard basis is $H_x,H_y,E_1,\ldots,E_8$, with intersection form $$\label{eq:intersection-form}
H_x^2=H_y^2=0,\quad H_xH_y=1,\quad
E_iE_j=-\delta_{ij},\quad H_xE_i=H_yE_i=0.$$ The following classes are the actual irreducible boundary curves: $$\label{eq:boundary-classes}
\begin{array}{ll}
D_1=H_x-E_1-E_7,&D_2=E_7-E_8,\\
D_3=H_y-E_2-E_7,&D_4=E_2-E_3,\\
D_5=H_x-E_2-E_4,&D_6=E_4-E_5,\\
D_7=E_5-E_6,&D_8=H_y-E_4-E_5.
\end{array}$$ They form a transverse cycle in the displayed order. Each has square $-2$; consecutive components meet once, including $D_8,D_1$; all other intersections vanish. One can see this directly by making the four corner blowups $E_2,E_4,E_5,E_7$, followed by the four smooth-boundary blowups. It also follows from [\[eq:intersection-form\]](#eq:intersection-form){reference-type="eqref" reference="eq:intersection-form"} and [\[eq:boundary-classes\]](#eq:boundary-classes){reference-type="eqref" reference="eq:boundary-classes"}. Their sum is $$\label{eq:anticanonical-cycle}
D=\sum_{i=1}^8D_i
=2H_x+2H_y-\sum_{i=1}^8E_i=-K_S,
\qquad D^2=0,\quad DD_i=0.$$

Set $U=U_{t,s}=S\setminus D$. Its points are the disjoint union of the torus and the four accessible exceptional curves $E_1,E_3,E_6,E_8$, each with its one boundary point removed. Those four curves are affine lines. Neighbourhood coordinates are $$\label{eq:accessible-charts}
\begin{array}{lll}
L_1:&x=u^{-1},&y=1+uv,\\
L_2:&x=u(t+uv),&y=u^{-1},\\
L_3:&x=u(t+uv),&y=u^2(t+uv),\\
L_4:&x=[u(s+uv)]^{-1},&y=u^{-1}.
\end{array}$$ In each row the line is $u=0$, with arbitrary finite coordinate $v$. These are the source's accessible charts [@JoshiRoffelsen2026 Section 2.1]. Their point decomposition is exactly the state set in Section [2](#sec:states){reference-type="ref" reference="sec:states"}. The intermediate exceptional curves occur in $D$ and are not additional ordinary states.

## Regularity of every forward branch

The torus formula [\[eq:torus-map-intro\]](#eq:torus-map-intro){reference-type="eqref" reference="eq:torus-map-intro"} extends to a morphism $F_t:U_{t,s}\to U_{st,s}$. We give the local formulas, since regularity at the exceptional points will later extend the invariant. In each target chart use coordinates $(a,b)$ and phase $T=st$ in place of $(u,v)$ and $t$ in [\[eq:accessible-charts\]](#eq:accessible-charts){reference-type="eqref" reference="eq:accessible-charts"}.

Near the torus divisor $sx-y=0$, target $L_1$ coordinates are $$\label{eq:extension-torus}
a=\frac{sx-y}{st},\qquad b=\frac{st}{y}.$$ They give $X=a^{-1}$ and $Y=1+ab$ where $a\ne0$, and extend to $a=0$.

On input $L_1$, put $A=1+uv$ and $B=s-uA$. Target $L_2$ coordinates are $$\label{eq:extension-L1}
a=\frac{uA}{s},\qquad
b=\frac{s^2t(A^2-sv)}{A^2B}.$$ On input $L_2$, put $A=t+uv$ and $B=su^2A-1$. Target $L_3$ coordinates are $$\label{eq:extension-L2}
a=\frac{uAB}{t},\qquad
b=\frac{st^2(-v+2suA^2-s^2u^3A^3)}{A^2B^3}.$$ On input $L_3$, put $A=t+uv$. Target $L_4$ coordinates are $$\label{eq:extension-L3}
a=\frac us,\qquad b=\frac{s(sv-A)}t.$$ Finally, on input $L_4$, put $A=s+uv$. Target $L_1$ coordinates are $$\label{eq:extension-L4}
a=-\frac{v}{stA},\qquad b=stu.$$

These are rational identities obtained by inserting [\[eq:accessible-charts\]](#eq:accessible-charts){reference-type="eqref" reference="eq:accessible-charts"} into [\[eq:torus-map-intro\]](#eq:torus-map-intro){reference-type="eqref" reference="eq:torus-map-intro"}. For example, in [\[eq:extension-L2\]](#eq:extension-L2){reference-type="eqref" reference="eq:extension-L2"} the identity $$t-AB^2=u\bigl(-v+2suA^2-s^2u^3A^3\bigr)$$ gives the second coordinate after cancelling the displayed factor $u$. At a relevant input-line point, every denominator in [\[eq:extension-L1\]](#eq:extension-L1){reference-type="eqref" reference="eq:extension-L1"}--[\[eq:extension-L4\]](#eq:extension-L4){reference-type="eqref" reference="eq:extension-L4"} is a unit: the values of $A,B$ are among $1,s,t,-1$. The formulas therefore define morphisms on neighbourhoods of every line point. No division by $2$ or $3$ occurs.

Evaluating them at $u=0$ gives the branches in Table [2](#tab:native){reference-type="ref" reference="tab:native"}. In [\[eq:extension-L4\]](#eq:extension-L4){reference-type="eqref" reference="eq:extension-L4"}, a nonzero $v$ gives the torus point $(-s^2t/v,1)$, whereas $v=0$ gives the target $L_1$ point $(a,b)=(0,0)$. Thus that special point is included by a regular local map. Together with the regular torus branch these formulae cover $U$, and agreement on the dense torus shows that they define the claimed morphism.

## Curves orthogonal to the boundary

The next lemma is the lattice input to the fibre argument. Work over $\overline{k}$ for the remainder of this section.

[\[lem:boundary-lattice\]]{#lem:boundary-lattice label="lem:boundary-lattice"} Every integral curve $Z$ on $S$ disjoint from $D$ is linearly equivalent to $dD$ for a positive integer $d$.

Write the integral divisor class in the free Picard basis as $$Z=aH_x+bH_y-\sum_{i=1}^{8}m_iE_i.$$ Here the coefficients are integers, not assumed to be multiplicities of a plane-curve presentation. The eight equations $ZD_i=0$ are $$\begin{aligned}
b-m_1-m_7&=0,& m_7-m_8&=0,\\
a-m_2-m_7&=0,& m_2-m_3&=0,\\
b-m_2-m_4&=0,& m_4-m_5&=0,\\
m_5-m_6&=0,& a-m_4-m_5&=0.\end{aligned}$$ Their full integer solution has two parameters $u,v\in\mathbb Z$: $$\label{eq:lattice-solution}
\begin{split}
a&=2u,\qquad b=u+v,\qquad m_1=2v-u,\\
m_2=m_3&=v,\qquad m_4=m_5=m_6=u,\qquad
m_7=m_8=2u-v.
\end{split}$$ Substitution in the intersection form gives $$Z^2=2ab-\sum m_i^2=-8(u-v)^2.$$ Since $K_S=-D$, adjunction for the integral curve $Z$ yields $$p_{\mathrm a}(Z)=1+\frac{Z^2+ZK_S}{2}=1-4(u-v)^2.$$ An integral proper curve over an algebraically closed field has $p_{\mathrm a}(Z)=\dim H^1(Z,\mathcal O_Z)\ge0$. Therefore $u=v=d$, and [\[eq:lattice-solution\]](#eq:lattice-solution){reference-type="eqref" reference="eq:lattice-solution"} becomes the class $dD$. The calculation takes place in the actual free Picard group, so it gives linear equivalence, not only numerical equivalence. Intersecting with an ample divisor shows $d>0$, since both $Z$ and $D$ are nonzero effective divisors.

The intersection form and adjunction compute integers. In particular, the coefficients $8$ and $4$ in this argument are not reduced modulo the characteristic of the ground field.

# Uniform poles and the minimal-pole obstruction {#sec:poles}

Throughout this section the ground field is algebraically closed. We first show that a regular function on $U$ cannot have different pole orders on different boundary components. The local blowup conditions then restrict the common order.

[\[lem:uniform-poles\]]{#lem:uniform-poles label="lem:uniform-poles"} If $g\in\Gamma(U,\mathcal O_U)$ is nonconstant, then $\operatorname{div}_{\infty}(g)=mD$ for an integer $m>0$. The rational function defines a morphism $g:S\to\mathbb P^1$ with infinity fibre $mD$. Each finite fibre is disjoint from $D$ and has divisor class $mD$.

Since $g$ is regular on $U$, its polar divisor on $S$ is $P=\sum n_iD_i$, with $n_i\ge0$. It is nonzero: a regular function on the projective integral surface $S$ is constant. Choose a constant $c$ so that the effective zero divisor $C$ of $g-c$ has no component $D_i$. There are only finitely many forbidden constants, namely the constant residues of $g$ on those boundary components on which it has no pole. This choice is made over the algebraically closed field, not inside a possibly small finite field.

Subtracting $c$ leaves the polar divisor $P$ unchanged, so $C\sim P$. Since $C$ and each $D_i$ have no common component, $$PD_i=CD_i\ge0.$$ On the other hand, $PD=0$ by [\[eq:anticanonical-cycle\]](#eq:anticanonical-cycle){reference-type="eqref" reference="eq:anticanonical-cycle"}. Summing the eight nonnegative intersections gives zero, hence $PD_i=0$ for every $i$. The intersection matrix of the boundary cycle gives the equations $$-2n_i+n_{i-1}+n_{i+1}=0$$ with cyclic indices. All successive differences are equal, and their sum is zero, so all $n_i$ are equal. Thus $P=mD$, $m>0$.

We also have $CD_i=0$ for every $i$. Positivity of local intersection multiplicities for curves without a common component shows $C\cap D=\varnothing$. The sections with divisors $C$ and $mD$ consequently have no common zero. Their ratio defines $g-c:S\to\mathbb P^1$, hence also $g$, with infinity fibre $mD$. For any finite constant $a$, the function $g-a$ still has order $-m$ along each $D_i$. Its zero divisor has no boundary component, is linearly equivalent to $mD$, and has zero intersection with every $D_i$. The same local-intersection argument shows that this finite fibre is disjoint from $D$.

[\[lem:pole-order\]]{#lem:pole-order label="lem:pole-order"} For any nonconstant $g\in\Gamma(U,\mathcal O_U)$ with pole divisor $mD$, one has $s^m=1$. If $s$ has exact order $r$, then $r\mid m$.

The restriction of $g$ to the torus is a Laurent polynomial $g=\sum c_{a,b}x^ay^b$. Consider the toric surface obtained by the four corner blowups $E_2,E_4,E_5,E_7$, before making the four smooth-boundary blowups. The latter do not change valuations at generic toric boundary points. The eight toric valuations of a monomial have primitive vectors $$\label{eq:valuation-vectors}
(1,0),\ (-1,0),\ (0,1),\ (0,-1),\
(1,-1),\ (1,1),\ (1,2),\ (-1,-1).$$ Every boundary valuation of $g$ is at least $-m$. Distinct monomials of the same valuation restrict to distinct characters on the corresponding toric divisor; they cannot cancel an entire leading Laurent polynomial. Thus every exponent of $g$ satisfies $$\begin{gathered}
-m\le a\le m,\qquad -m\le b\le m,\\
a-b\ge-m,\qquad a+b\ge-m,\qquad
a+2b\ge-m,\qquad a+b\le m.\end{gathered}$$ The intersection of these half-spaces is the polygon $$\label{eq:exponent-polygon}
m\Delta=\mathop{\mathrm{conv}}\{(-m,0),(0,m),(m,0),(m,-m)\}.$$

Denote its vertex coefficients by $$\label{eq:vertex-coefficients}
A=[x^{-m}]g,\qquad B=[y^m]g,\qquad
C=[x^m]g,\qquad E=[(x/y)^m]g.$$ The coefficient $B$ is nonzero. Indeed $g$ has exact pole order $m$ on the strict transform of $y=\infty$, and the only exponent in [\[eq:exponent-polygon\]](#eq:exponent-polygon){reference-type="eqref" reference="eq:exponent-polygon"} with $b=m$ is $(0,m)$.

Here is the local effect of a smooth-boundary blowup. In coordinates $(u,v)$, let the boundary be $u=0$ and the centre be $(0,v_0)$. Write $g=u^{-m}h(u,v)$, with $h$ regular near the centre. The valuation of $h$ on the new exceptional divisor is its multiplicity at that centre. If $g$ is regular along the new accessible divisor, this multiplicity is at least $m$. Restricting $h$ to $u=0$ therefore gives a zero of order at least $m$ at $v_0$. This is a local-ring multiplicity statement and does not use derivatives or factorials.

Apply this argument to $E_1,E_3,E_6,E_8$, which are precisely the accessible exceptional divisors. The four relevant faces are listed in Table [5](#tab:faces){reference-type="ref" reference="tab:faces"}. The expression in its third column is the coefficient of $u^{-m}$ in the local Laurent expansion. After multiplication by a unit at the specified nonzero root, it is a polynomial of degree at most $m$.

::: {#tab:faces}
  Blowup   Boundary coordinates       Face expression           Root
  -------- -------------------------- ------------------------- -------
  $E_1$    $u=x^{-1},\ z=y^{-1}$      $C+\cdots+Ez^m$           $z=1$
  $E_3$    $x=uv,\ y=u^{-1}$          $v^{-m}(A+\cdots+Bv^m)$   $v=t$
  $E_6$    $x=uv,\ y=u^2v$            $v^{-m}(A+\cdots+Ev^m)$   $v=t$
  $E_8$    $x=(uv)^{-1},\ y=u^{-1}$   $v^{-m}(C+\cdots+Bv^m)$   $v=s$

  : The four smooth-boundary face conditions for a pole divisor $mD$. In each row the boundary is $u=0$, and the displayed face expression must vanish to order at least $m$ at the indicated root. The omitted terms are the intermediate powers of the face coordinate.
:::

A polynomial of degree at most $m$ vanishing to order at least $m$ at $z_0$ is a scalar multiple of $(z-z_0)^m$, including the zero polynomial. Comparing its endpoint coefficients in the four rows gives $$\label{eq:face-relations}
\begin{split}
C&=(-1)^mE,\qquad A=(-t)^mB,\\
A&=(-t)^mE,\qquad C=(-s)^mB.
\end{split}$$ The second and third equations, with $t\ne0$ and $B\ne0$, imply $E=B\ne0$. The first and fourth then yield $$(-1)^mB=(-s)^mB,$$ so $s^m=1$. Its exact order $r$ divides $m$.

The proof remains valid when some intermediate binomial coefficients vanish in the ground field, or when its characteristic divides $m$. Only the degree and multiplicity of a linear factor were used. In particular, no root-of-unity convention from a complex period-map calculation enters the relation $s^m=1$.

# The source invariant and its exact polar divisor {#sec:integral}

We now use the proved matrix integral of Joshi--Roffelsen. Its algebraic construction is an external dynamical input; the arguments here identify its polar divisor on the complete resolved surface and control its extension at every ordinary point.

## The explicit integral and its specialization

For a primitive $r$-th root parameter, set $R=\mathbb Z[s]/(\Phi_r(s))$, where $\Phi_r$ is the cyclotomic polynomial. At gauge $w=1$, write $$\label{eq:source-matrix}
A(z)=A_0+zA_1+z^2A_2,$$ where $$\begin{aligned}
A_0&=\begin{pmatrix}
t+x-xy&-x\\
t+x-ty-2xy+xy^2&x(y-1)
\end{pmatrix},\\[3pt]
A_1&=\begin{pmatrix}
y-x+x/y-1-t/x&1\\
y-2x-1+xy+x/y-t/x&1
\end{pmatrix},\qquad
A_2=\begin{pmatrix}1&0\\0&0\end{pmatrix}.\end{aligned}$$ Define $$\label{eq:source-integral}
I_{r,t}(x,y)=\mathop{\mathrm{Tr}}\bigl(A(s^{r-1})\cdots A(s)A(1)\bigr)-(t^r+1).$$ The source proves that this is a Laurent polynomial in $x,y$, polynomial in $t$, with coefficients in $R$, and that $$\label{eq:invariance}
I_{r,st}\bigl(F_t(x,y)\bigr)=I_{r,t}(x,y)$$ as a rational identity over the cyclotomic field [@JoshiRoffelsen2026 Theorem 3.1]. The trace is independent of the auxiliary gauge. The source's proof uses the cyclic trace of $A(s^{r-1}z)\cdots A(z)$ and telescoping Lax compatibility; its constant and leading trace coefficients are $t^r$ and $1$. It does not assume the source's later conjecture about genera of fibres.

For the finite field $k=\mathbb F_q$, the order $r$ divides $q-1$, so $p=\operatorname{char}k$ does not divide $r$. An element of exact order $r$ in $k^*$ is a zero of $\Phi_r$ modulo $p$. Indeed the factorization $$X^r-1=\prod_{d\mid r}\Phi_d(X)$$ remains a product of pairwise coprime polynomials because $X^r-1$ is separable. If the element were a zero of a factor indexed by a proper divisor $d$, its order would divide $d$. Hence there is a specialization $R\to k$ sending the parameter to the chosen $s$.

Formula [\[eq:source-integral\]](#eq:source-integral){reference-type="eqref" reference="eq:source-integral"} has no integer denominators. To specialize [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"}, substitute the torus formulas and clear only powers of $$x,\ y,\ t,\ s,\ sx-y.$$ The resulting numerator is an element of an integral polynomial/Laurent ring over $R$. It is zero in the fraction field by the source theorem, and is therefore zero in that ring. Specialization preserves the identity of rational functions over $k$. The allowed phase parameters $s,t$ are units, and $sx-y$ is not the zero polynomial after specialization. This argument imports no smoothness assertion from characteristic zero.

## Extension across the accessible lines

The function $I_{r,t}$ is regular on the torus. The generic point of $L_4$ reaches the torus after one forward step. The generic points of $L_3,L_2,L_1$ do so after two, three and four steps, respectively. To see this, use Table [2](#tab:native){reference-type="ref" reference="tab:native"}: each intermediate map between line coordinates is affine with nonzero slope, and the last $L_4$ coordinate is generically nonzero.

All these forward maps are morphisms by [\[eq:extension-torus\]](#eq:extension-torus){reference-type="eqref" reference="eq:extension-torus"}--[\[eq:extension-L4\]](#eq:extension-L4){reference-type="eqref" reference="eq:extension-L4"}. Repeated invariance therefore expresses $I_{r,t}$, near each line's generic point, as the pullback of a regular Laurent function on a target torus. It has no pole along any of the four accessible lines. Every other prime divisor of $U$ meets the torus, so it has no pole there either. Smoothness makes $U$ normal; on a normal variety a rational function without a codimension-one pole is regular. Consequently $$\label{eq:integral-regular}
I_{r,t}\in\Gamma(U_{t,s},\mathcal O_{U_{t,s}}).$$

This conclusion includes the special points with zero line coordinate. There is no isolated pole of a rational function left at one of those points. The two sides of [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"} are now regular functions on $U_{t,s}$ agreeing on a dense open subset, so they agree everywhere on $U_{t,s}$.

## Exact order on the boundary

For completeness, reproduce the nonzero leading term calculated in the proof of the source's Theorem 3.1 [@JoshiRoffelsen2026]. At the generic point of $x=0$, with $y$ finite and nonzero, $$\label{eq:idempotent-leading}
A(z)=-\frac{tz}{x}V+O(1),\qquad
V=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad
V^2=V,\quad\mathop{\mathrm{Tr}}V=1.$$ The coefficient of $x^{-r}$ in the product defining [\[eq:source-integral\]](#eq:source-integral){reference-type="eqref" reference="eq:source-integral"} is $(-1)^rs^{r(r-1)/2}t^rV$. The product of all the roots of $X^r-1$ is $(-1)^{r-1}$; since the roots are $1,s,\ldots,s^{r-1}$, this gives $$(-1)^rs^{r(r-1)/2}=-1.$$ Taking the trace yields $$\label{eq:nonzero-leading}
I_{r,t}=-t^rx^{-r}+O\bigl(x^{-(r-1)}\bigr).$$ Its leading coefficient never vanishes on the allowed domain, even in characteristic two. The integral is nonconstant and has exact pole order $r$ on $D_5$, the strict transform of $x=0$.

Apply Lemma [\[lem:uniform-poles\]](#lem:uniform-poles){reference-type="ref" reference="lem:uniform-poles"} to [\[eq:integral-regular\]](#eq:integral-regular){reference-type="eqref" reference="eq:integral-regular"}. The order on this one boundary component determines the entire polar divisor: $$\label{eq:exact-fibration}
\operatorname{div}_{\infty}(I_{r,t})=rD,\qquad
f_t:S_{t,s}\longrightarrow\mathbb P^1,\qquad
f_t^{-1}(\infty)=rD.$$ The morphism is defined over $k$, since the surface and function are. Its nonconstancy and projectivity imply surjectivity onto $\mathbb P^1$. Every finite fibre is a nonzero effective divisor of class $rD$, disjoint from $D$.

# Every finite fibre is integral and reduced {#sec:fibres}

We now prove Theorem [\[thm:fibres-intro\]](#thm:fibres-intro){reference-type="ref" reference="thm:fibres-intro"}. The argument treats an arbitrary finite fibre over the algebraic closure. There is no passage from a generic irreducibility statement to a special fibre.

The morphism and its infinity fibre were constructed in [\[eq:exact-fibration\]](#eq:exact-fibration){reference-type="eqref" reference="eq:exact-fibration"}. Fix any $c\in\overline{k}$, and write the finite fibre divisor as $$\label{eq:fibre-decomposition}
C_c=f_t^{-1}(c)=\sum_{j=1}^{h}n_jZ_j,\qquad n_j\ge1,$$ with distinct integral geometric components $Z_j$. By Lemma [\[lem:uniform-poles\]](#lem:uniform-poles){reference-type="ref" reference="lem:uniform-poles"}, this fibre is disjoint from $D$ and is linearly equivalent to $rD$. Each $Z_j$ is therefore disjoint from $D$. Lemma [\[lem:boundary-lattice\]](#lem:boundary-lattice){reference-type="ref" reference="lem:boundary-lattice"} gives $$Z_j\sim d_jD,\qquad d_j\in\mathbb Z_{>0}.$$

This is linear equivalence in $\mathop{\mathrm{Pic}}(S_{\overline{k}})$, so there is a rational function $g_j$ with $$\operatorname{div}(g_j)=Z_j-d_jD.$$ Since $Z_j\cap D=\varnothing$, its polar divisor is exactly $d_jD$. In particular $g_j$ is nonconstant and regular on $U_{\overline{k}}$. Lemma [\[lem:pole-order\]](#lem:pole-order){reference-type="ref" reference="lem:pole-order"} applies separately to each component and forces $r\mid d_j$.

Comparison of classes in [\[eq:fibre-decomposition\]](#eq:fibre-decomposition){reference-type="eqref" reference="eq:fibre-decomposition"} now gives $$\label{eq:component-sum}
\sum_{j=1}^{h}n_jd_j=r.$$ The class $D$ is nonzero in the free Picard group, so its integer coefficient can be compared. Every summand in [\[eq:component-sum\]](#eq:component-sum){reference-type="eqref" reference="eq:component-sum"} is a positive multiple of $r$. Thus $h=1$, $n_1=1$, and $d_1=r$.

This establishes a unique geometric component with multiplicity one. To obtain reducedness of the whole fibre as a scheme, note that it is an effective Cartier divisor on the smooth surface. Locally it is cut out by a nonzerodivisor in a regular local ring, so the quotient is Cohen--Macaulay of pure dimension one. There are no embedded associated points. Since it is reduced at the generic point of its unique component, a nilpotent cannot be supported at a remaining closed point: a nonzero such submodule would have a closed associated point. The entire fibre is therefore reduced. It is geometrically integral.

Finally, adjunction and $K_S=-D$, $D^2=0$, give $$\label{eq:fibre-genus}
p_{\mathrm a}(C_c)=1+\frac{(rD)^2+(rD)K_S}{2}=1.$$ Lemma [\[lem:uniform-poles\]](#lem:uniform-poles){reference-type="ref" reference="lem:uniform-poles"} already places this projective curve entirely inside $U$, completing all assertions.

The componentwise use of linear equivalence in this proof is essential. An invariant of degree $rD$ alone would not exclude a sum of smaller components; the minimal-pole obstruction excludes each smaller positive class separately. In particular, no permutation of components in a reducible finite fibre can create a longer exceptional orbit, because such finite fibres do not occur. Multiple finite fibres are excluded by the same argument.

This reasoning does not require a section of the fibration, a connected-fibre descent theorem, generic smoothness, or the exclusion of quasi-elliptic behaviour. None of those additional statements is being asserted here.

# Rational points and the original least period {#sec:periods}

The fibre theorem turns the orbit question into a point-count problem for a projective geometrically integral curve. Singular fibres require a separate argument, but arithmetic genus one makes that argument short and uniform in the characteristic.

[\[lem:point-bound\]]{#lem:point-bound label="lem:point-bound"} Let $C$ be a projective geometrically integral curve of arithmetic genus one over $k=\mathbb F_q$, and suppose $C(k)\ne\varnothing$. Then $$\#C(k)\le q+1+2\sqrt q.$$ If $C$ is singular, the stronger estimate $\#C(k)\le q+2$ suffices.

If $C$ is smooth, its rational point makes it an elliptic curve over $k$. Hasse's theorem gives the stated upper bound; a proof for arbitrary finite fields is @Sutherland2021 [Theorem 7.3]. No odd-characteristic hypothesis is part of that theorem.

Suppose instead that $C$ is singular, and let $\nu:\widetilde C\to C$ be its normalization. The field $k$ is perfect, so $\widetilde C$ is a smooth projective geometrically integral curve. Over $\overline{k}$, the normalization exact sequence is $$\label{eq:normalization-sequence}
0\longrightarrow\mathcal O_{C_{\overline{k}}}
\longrightarrow\nu_*\mathcal O_{\widetilde C_{\overline{k}}}
\longrightarrow\mathcal Q\longrightarrow0,$$ where $\mathcal Q$ has finite support at the singular points. Its local length at a geometric singular point $Q$ is the positive integer $\delta_Q$. These normalization and delta-invariant facts are recorded in @stacks-project [[Tag 0C3Q](https://stacks.math.columbia.edu/tag/0C3Q), Lemma 33.39.2, Definition 33.39.3 and Lemma 33.39.4]; the genus comparison is also discussed in @stacks-project [[Tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0)]. Taking Euler characteristics in [\[eq:normalization-sequence\]](#eq:normalization-sequence){reference-type="eqref" reference="eq:normalization-sequence"} gives $$\label{eq:delta-genus}
1=p_{\mathrm a}(C)=g(\widetilde C)+
\sum_{Q\in\mathop{\mathrm{Sing}}(C_{\overline{k}})}\delta_Q.$$ The curve is singular, so the sum is positive. Hence $g(\widetilde C)=0$, and there is exactly one geometric singular point, with $\delta=1$.

We always have $\#\widetilde C(k)\le q+1$. If $\widetilde C(k)$ is empty, this is immediate. Otherwise, genus-zero Riemann--Roch applied to a rational point supplies a degree-one map to $\mathbb P^1_k$, so $\widetilde C\simeq\mathbb P^1_k$ and the count is $q+1$. Normalization is an isomorphism over the smooth locus. Thus every smooth rational point of $C$ has a unique rational lift, and at most one remaining rational point can be singular. It follows that $$\label{eq:singular-bound}
\#C(k)\le\#\widetilde C(k)+1\le q+2
\le q+1+2\sqrt q,$$ where the last inequality holds for every finite field, $q\ge2$.

The singular argument does not assume that the given rational point is smooth. It also makes no assumption about split nodes or cusps. These distinctions therefore cause no missing cases in small characteristic.

Proposition [\[prop:permutation\]](#prop:permutation){reference-type="ref" reference="prop:permutation"} makes every state periodic on the finite phase union. Let $\ell$ be its least native period, and let $t$ be its starting phase. A return after $n$ steps requires $s^nt=t$. Since $t\ne0$ and $s$ has exact order $r$, every return time is divisible by $r$; in particular $r\mid\ell$.

The fixed-phase return map is $$G=F_{s^{r-1}t}\circ\cdots\circ F_{st}\circ F_t.$$ For $r=1$ this means $G=F_t$. It is a bijection of $U_{t,s}(k)$, and [\[eq:invariance\]](#eq:invariance){reference-type="eqref" reference="eq:invariance"}, extended to every ordinary point, shows that it preserves $I_{r,t}$. The starting state has a finite invariant value $c\in k$ by [\[eq:integral-regular\]](#eq:integral-regular){reference-type="eqref" reference="eq:integral-regular"}. Its $G$-orbit is contained in the finite fibre $C_c(k)$.

The least period under $G$ is exactly $\ell/r$: a return under $G^m$ is a native return after $rm$ steps, and the least positive native return is $\ell$, itself a multiple of $r$. Consequently the $\ell/r$ points of this return orbit are distinct ordinary rational points of $C_c$. By Theorem [\[thm:fibres-intro\]](#thm:fibres-intro){reference-type="ref" reference="thm:fibres-intro"}, this is a projective geometrically integral curve of arithmetic genus one. Applying Lemma [\[lem:point-bound\]](#lem:point-bound){reference-type="ref" reference="lem:point-bound"} gives $$\frac{\ell}{r}\le\#C_c(k)\le q+1+2\sqrt q.$$ This proves the theorem for every phase and every state in the seven-branch domain.

# Scope and conclusion {#sec:conclusion}

The bound $\ell/r\le q+1+2\sqrt q$ holds on the complete resolved native state space, uniformly over finite fields and nonzero phase parameters. The decisive point is not only the availability of an integral, but its minimal boundary pole order. The boundary lattice and four face-root conditions force every finite fibre to be integral and reduced. Arithmetic genus one then accommodates both the smooth Hasse bound and the singular normalization bound without deleting exceptional states.

Only the upper-bound part of the Joshi--Roffelsen orbit conjecture is settled here. The proposed bin distribution and explicit singular-value discriminant are separate questions. We do not prove generic smoothness in every characteristic or identify the invariant fibres with a spectral quotient. The argument does not use those assertions.

The conclusion concerns this source dynamical system and its ordinary periods. It does not identify those periods with Euler factors, root numbers or zeros of an external $L$-function, and it makes no spectral-realization claim.

#### Preparation and verification.

This article was prepared with AI assistance. Its underlying proof package received separate current-team internal mathematical and source-scope reviews. Such checking is not human peer review or a certificate of worldwide priority. The argument is proof-only and does not rely on a finite-field census or new numerical experiments.
