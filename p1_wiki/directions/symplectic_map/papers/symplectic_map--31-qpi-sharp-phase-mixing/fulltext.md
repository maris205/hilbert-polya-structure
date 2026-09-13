---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--31-qpi-sharp-phase-mixing"
canonical_tex: "symplectic_map/papers/31-qpi-sharp-phase-mixing/paper/v1/main.tex"
canonical_pdf: "symplectic_map/papers/31-qpi-sharp-phase-mixing/build/natural-20260913-r0/work/main.pdf"
source_sha256: "fcbfe0ac6f8ad6364728e7c86981bd1eef2d912c7d125c6d710a155d50cd53fa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp phase mixing for the autonomous q-Painlevé I map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/31-qpi-sharp-phase-mixing>)
- [规范 TeX](<../../../../../symplectic_map/papers/31-qpi-sharp-phase-mixing/paper/v1/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/31-qpi-sharp-phase-mixing/build/natural-20260913-r0/work/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/31-qpi-sharp-phase-mixing/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/31-qpi-sharp-phase-mixing/paper/v1/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove sharp, unaveraged correlation asymptotics for the autonomous q-Painlevé I map on its complete real space of initial values. The observables are smooth and compactly supported in the original surface, and their means are removed on each connected energy circle. For every fixed positive parameter $T\ne1$, the optimal global rate is $n^{-1/2}$, with explicit oscillatory coefficients from all stationary circles. At $T=1$ no stationary circle remains: original first jets at the elliptic centre give a sharp $n^{-2}$ term with an $O(n^{-3})$ remainder. At $T=3/16$ the shrinking circle contributes an additional $n^{-1}$ term, while a different, persistent circle at the same energy still contributes at order $n^{-1/2}$. The proof combines a complete frequency classification with mixed energy--angle estimates at the hyperbolic fibre and symmetric time coordinates at the elliptic centre. A fixed neighbourhood of the hyperbolic fibre contributes faster than every prescribed inverse power, with an explicit finite-order original norm bound. All Fourier modes, both critical fibres, and the four terminal lines are retained. The global remainders are controlled by original $C^{20}$ norms. We also determine the even--odd coefficients of the original map, including its exchange of the two upper circles, and realize sharpness with real and complex original observables.
author:
- Anonymous
bibliography:
- references.bib
title: 'Sharp phase mixing for the autonomous q-Painlevé I map'
```

## Markdown 正文

# Introduction {#sec:introduction}

An integrable map can preserve every energy level without preserving the correlations of an ensemble spread over different energies. The relevant cancellation is phase mixing: rotation frequencies vary with energy, so the nonconstant angular modes interfere. A single circle rotation is not mixing. Moreover, when a level has two circles, centering by its whole-fibre mean can leave a nondecaying mode even if all nonconstant angular modes decay.

For the autonomous q-Painlevé I map we determine the sharp correlations after the correct, circlewise centering. The observables live on the complete original real surface, not on an affine chart with the exceptional points or singular energy bands deleted. Write $C_n$ for this centered correlation and $n=2m+r$, $r=0,1$. The main asymptotics have the following three forms; the bounded oscillatory sequences are explicitly defined in Section [2](#sec:surface){reference-type="ref" reference="sec:surface"}.

::: {#intro:rates}
  Parameter             Correlation $C_{2m+r}$                                  Source of the leading terms
  --------------------- ------------------------------------------------------- ----------------------------------
  $T\notin\{3/16,1\}$   $m^{-1/2}\mathcal A_r+O(m^{-3/2})$                      Stationary circles
  $T=3/16$              $m^{-1/2}\mathcal A_r+m^{-1}\mathcal D_r+O(m^{-3/2})$   Persistent and shrinking circles
  $T=1$                 $m^{-2}\mathcal B_r+O(m^{-3})$                          Original centre jets

  : The original map is evaluated at both parities. At $T=3/16$ the two contributions come from different components of the same critical energy level. Remainders use original $C^{20}$ norms.
:::

Three features distinguish the complete statement from a regular-band estimate. First, an observable smooth in the original surface need not have a smooth circlewise mean at the hyperbolic fibre. We control mixed energy and angle derivatives before centering, retain the whole Fourier series, and prove that a fixed saddle neighbourhood contributes $O(m^{-N})$ for each specified $N$, using original $C^{N+2}$ norms. Second, the frequency geometry determines all stationary circles for every $T>0$. Their absence at $T=1$ exposes an elliptic first-jet term; at $T=3/16$ a quadratic endpoint on the shrinking circle coexists with an interior stationary point on the persistent circle. Third, the original map exchanges two circles above the saddle. The odd-step coefficients are therefore cross-pairings, not copies of the even ones. We compute these coefficients and prove positive normalized limsup for legitimate original real and complex observables.

#### Phase mixing near trapped and degenerate trajectories.

The analytical mechanisms have strong precedents. Faou, Horsin, and Rousset treat inhomogeneous Vlasov--HMF dynamics using action--angle Fourier analysis, estimates through the separatrix, and the behaviour of original smooth observables at the centre [@FaouHorsinRousset2021]. Their analysis already includes arbitrary prescribed inverse powers at the hyperbolic boundary; crossing a separatrix and summing angular modes are not new principles here. Hadžić, Rein, Schrecker, and Straub analyze quantitative phase mixing for Hamiltonians with trapping, including the Fourier vanishing of original observables at elliptic stagnation points [@HadzicReinSchreckerStraub2024]. Those results motivate keeping original-space regularity separate from regularity in a degenerating angle chart. Our contribution is the complete sharp correlation theorem for this specific discrete map, including its parameter transitions and actual one-step phases, rather than a new general damping method.

#### Frequency geometry and discrete ensemble limits.

Moreno, Rioseco, and Van Den Bosch study mixing under frequency nondegeneracy and finite degeneracies [@MorenoRiosecoVanDenBosch2022]. Their Theorem 1.2 in the cited preprint version gives a $t^{-1/3}$ estimate under its $C^1$ assumptions; it is not the sharp smooth stationary-phase expansion used below. The stationary-phase mechanism itself is classical. For discrete integrable Hamiltonian systems, the deterministic ensemble law of large numbers of Liu, Zhang, and Li [@LiuZhangLi2025 Theorem 3.1] concerns Cesàro averages under its nonresonance hypotheses. Liu's weak-convergence result with Markov perturbations [@Liu2026Markov] uses a stochastic mechanism. Neither time averaging nor random perturbation is part of our correlation statement. The comparisons with Faou--Horsin--Rousset and Moreno--Rioseco--Van Den Bosch use the fixed preprint versions identified in the bibliography; the preprint theorem numbering is not assigned to the journal versions.

#### Geometry and proof organization.

The original eight-centre surface and its complete finite fibres are the geometric input recorded in [@QPI30Local2026], an unpublished local manuscript. We recall its precise interface and prove the real translation, measure, and component statements needed here. The Picard--Fuchs forcing and full frequency classification are included with their proofs: the endpoint constants are necessary even though the observables have compact support, because they rule out additional stationary circles. These geometric inputs are not separate claims of novelty. Sections [3](#sec:forcing){reference-type="ref" reference="sec:forcing"} and [4](#sec:frequency){reference-type="ref" reference="sec:frequency"} establish them; Sections [5](#sec:hyperbolic){reference-type="ref" reference="sec:hyperbolic"} and [6](#sec:elliptic){reference-type="ref" reference="sec:elliptic"} treat the two degenerations; and Section [7](#sec:global){reference-type="ref" reference="sec:global"} combines the estimates, restores the original parities, and proves sharpness.

# The real surface and main theorem {#sec:surface}

## The original surface and finite fibres

Fix $T>0$. On the original torus the autonomous map, its integral, and its symplectic form are $$F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
 h=-x+y+\frac{x}{y}-\frac{T}{x},\qquad
 \Omega=\frac{\mathrm dx\wedge\mathrm dy}{xy}.
 \label{eq:map}$$ The rational expression for $F_T$ is not its domain of definition. We use the original space of initial values, whose geometric construction and finite-fibre properties are recorded in the local manuscript [@QPI30Local2026 Section 2]. Here is the precise specialization needed in this paper. Starting from $\mathbb P^1\times\mathbb P^1$, perform the following four clusters of successive blowups: $$\begin{array}{cl}
1:&(x^{-1},y-1)=(0,0),\\
2:&(x,y^{-1})=(0,0),\quad xy=T,\\
3:&(x,y)=(0,0),\quad E_{3,1}\cap\{y=0\},\quad x^2/y=T,\\
4:&(x^{-1},y^{-1})=(0,0),\quad y/x=1.
\end{array}$$ A ratio in this list specifies the point on the preceding exceptional divisor. There are $1+2+3+2=8$ centres. Denote the resulting projective surface by $S_T$ and the final strict transforms of the exceptional curves by $E_{i,j}$. Its polar cycle is $$D=C_{x0}+E_{3,1}+E_{3,2}+C_{y0}+C_{x\infty}
  +E_{4,1}+C_{y\infty}+E_{2,1}.$$ Write $\mathcal U_T=S_T\setminus D$ for the algebraic open surface and $U_T=\mathcal U_T(\mathbb{R})$ for its full real locus, rather than a punctured affine energy curve. We usually suppress $T$ on $U_T$ and $F_T$.

[\[prop:surface\]]{#prop:surface label="prop:surface"} The map $F_T$ lifts to an automorphism of $\mathcal U_T$, and $\Omega$ is nowhere degenerate there. The integral extends to a morphism $\bar h:S_T\to\mathbb P^1$ with scheme fibre $\bar h^{-1}(\infty)=D$. Every finite geometric fibre is complete and connected, has arithmetic genus one, and is contained in $\mathcal U_T$ after base change. The complement of the real torus in $U_T$ consists of four complete terminal affine lines. On every smooth finite fibre, the original map is identified with translation by $P=(0,T)$ on $$E_h:\quad v^2+huv-Tv=u^3-Tu^2,\qquad O=[0:1:0].
 \label{eq:weierstrass}$$

The surface, polar divisor, lift, and complete-fibre assertions are the geometric interface just cited, specialized to the autonomous case; no normal-bundle or arithmetic critical-ideal result is used below. We verify the real-fibre identification and all the analytic interfaces that enter the correlation theorem. On the torus the birational maps are $$u=T/y,\qquad v=Tx(y-1)/y^2,\qquad
 x=Tu/(T-hu-v),\qquad y=T/u.
 \label{surf:birational}$$ Substitution in the energy equation proves that these maps are inverse and satisfy [\[eq:weierstrass\]](#eq:weierstrass){reference-type="eqref" reference="eq:weierstrass"}. A smooth complete connected fibre is geometrically integral: the components of a smooth curve are disjoint, whereas the geometric fibre is connected. The birational map between these smooth projective curves therefore extends uniquely to an isomorphism over $\mathbb{R}$. To check the translation, put $m=(v-T)/u$. The chord through $P$ gives $$(u,v)+P=
 \bigl(m^2+hm+T-u,-(m+h)(m^2+hm+T-u)\bigr).$$ Using the energy relation, this is $(Ty/x,T^2y/x^2)=\phi F_T(x,y)$, where $\phi$ is [\[surf:birational\]](#surf:birational){reference-type="eqref" reference="surf:birational"}. Equality on this dense open set extends over the complete smooth fibre, since both maps are regular.

For later use Table [2](#surf:terminal-table){reference-type="ref" reference="surf:terminal-table"} gives the four actual terminal charts. Each line is $a=0$, with $b\in\mathbb{R}$ arbitrary; write $B=T+ab$. The entries follow by substitution in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} and [\[surf:birational\]](#surf:birational){reference-type="eqref" reference="surf:birational"}. In chart 3, $u\sim a^{-2}$ and $v\sim-a^{-3}$, giving the unique point $O$ at infinity.

::: {#surf:terminal-table}
   Chart  $(x,y)$                     $h|_{a=0}$   $\Omega/(\mathrm da\wedge\mathrm db)$   Image on $E_h$
  ------- --------------------------- ------------ --------------------------------------- ----------------
     1    $(a^{-1},1+ab)$             $1-b$        $-1/(1+ab)$                             $-2P$
     2    $(aB,a^{-1})$               $b/T$        $1/B$                                   $-P$
     3    $(aB,a^2B)$                 $b/T$        $-1/B$                                  $O$
     4    $([a(1+ab)]^{-1},a^{-1})$   $1+b$        $-1/(1+ab)$                             $P$

  : The four terminal lines belong to the original surface. Their points remain regular for the energy map even when the complete fibre has a critical point elsewhere.
:::

The four images are distinct. Indeed $-P=(0,0)$ and the tangent there is $v=0$, so $2P=(T,0)$. Thus $P$ is not of order two or three, and $-2P\ne O$. No terminal point is removed from any of the circles considered below. The table also gives $h_b=-1,1/T,1/T,1$ on the respective lines; hence none of them contains a critical point.

## Real circles and the two critical fibres

Put $$\begin{gathered}
 \delta(h)=h^4-h^3-8Th^2+36Th+16T^2-27T,\\
 w_-<0,\quad w_+>1,\quad w_\pm^3(w_\pm-1)=T,\qquad
 s_\pm=(w_\pm^2,w_\pm),\quad h_\pm=3w_\pm-2w_\pm^2.
\end{gathered}
\label{eq:critical}$$

[\[prop:real-geometry\]]{#prop:real-geometry label="prop:real-geometry"} There are exactly two real critical values, $h_-<h_+<1$. Each has a single critical point: $s_-$ is a nondegenerate elliptic maximum, and $s_+$ is a nondegenerate hyperbolic saddle. The complete regular fibres have respectively two, one, and two circles on $(-\infty,h_-)$, $(h_-,h_+)$, and $(h_+,\infty)$. The map $F$ preserves each circle in the first two intervals and exchanges the two circles in the last. At $h_-$ an isolated real node coexists with a persistent smooth circle. At $h_+$ the node is split.

The equations $h_x=h_y=0$ on the torus give $x=y^2$ and $y^4-y^3=T$, hence the points in [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}. The function $w^3(w-1)$ decreases from infinity to zero on $(-\infty,0)$ and increases from zero to infinity on $(1,\infty)$; its derivative is $w^2(4w-3)$, and it is nonpositive on $[0,1]$. Thus these are the only real critical points. To order their values, write $w_-=-a$, $w_+=1+b$, with $a,b>0$. The identities $a^3(a+1)=b(b+1)^3=T$ imply $b<a$, because $s(s+1)^3$ is increasing and $a(a+1)^3>a^3(a+1)$. Consequently $$h_+=1-b-2b^2<1,\qquad
 h_+-h_-=1+3a-b+2(a^2-b^2)>0.$$ The Hessian at $s_w=(w^2,w)$ is $$D^2h(s_w)=
 \begin{pmatrix}-2(w-1)/w^3&-1/w^2\\-1/w^2&2/w\end{pmatrix},
 \qquad \det D^2h(s_w)=\frac{3-4w}{w^4}.$$ It is negative definite at $w_-$ and indefinite at $w_+$.

Complete the square without moving $u$: $$Y=v+(hu-T)/2,\qquad
 Y^2=\Phi_h(u):=u^3+(h^2/4-T)u^2-hTu/2+T^2/4.
 \label{surf:completed-square}$$ Here $P=(0,T/2)$ and $\operatorname{disc}\Phi_h=T^3\delta(h)/16$. To see that $\delta$ has no other real zeros, a singular point has $u,v\ne0$. Setting $z=v/u$, its equations give $$u=T-z^2,\quad v=z(T-z^2),\quad u^2=Tz,\quad h=T/z-3z.$$ Then $w=u/z$ gives $z=w(w-1)$ and precisely $$T=w^3(w-1),\quad h=w(3-2w),\quad
 u_0=w^2(w-1),\quad v_0=w^3(w-1)^2.$$ At a real singular cubic the multiple root is real, since a nonreal multiple root and its conjugate would require degree at least four. The preceding elimination therefore includes every real singular fibre. Direct substitution yields $\delta'(h_w)=w^2(4w-3)^3\ne0$. Thus $\delta$ is positive on the two outer intervals and negative between its two simple real roots.

For $\delta>0$, let $r_1<r_2<r_3$ be the three roots of $\Phi_h$. The bounded oval $r_1\le u\le r_2$ is the nonidentity circle; $u\ge r_3$ together with $O$ is the identity circle. The two signs of $Y$ glue at the indicated root endpoints, not to each other at infinity. For $\delta<0$ there is one real root and one circle. If $h<h_-$, all coefficients of $\Phi_h$ are positive, since $h<0$ and $h_-^2/4-T=w_-^2(9/4-2w_-)>0$. Its three roots are therefore negative and $P$ lies on the identity circle. On the upper interval use the exact anchor $$\Phi_1(u)=(u-T)(u^2+u/4-T/4).$$ The quadratic roots are $(-1\pm\sqrt{1+16T})/8$; its positive root $b_1$ satisfies $T=4b_1^2+b_1>b_1$. Hence $P$ lies on the bounded oval at $h=1$. Simple roots vary continuously on $(h_+,\infty)$, and none can cross zero because $\Phi_h(0)=T^2/4>0$. So $P$ remains on that nonidentity circle throughout the interval. The component group of a real elliptic curve with two components is $\mathbb{Z}/2\mathbb{Z}$. Translation by $P$ therefore gives the stated preservation or exchange, with minimal component return $F^2$ in the upper interval. The identity $2P=(T,0)$ also shows that $P$ has exact order four at $h=1$.

Finally, $$\Phi_{h_w}(u)=(u-w^2(w-1))^2(u+w^2/4).$$ The coefficient in the nodal tangent cone is $w^2(4w-3)/4$. It is negative for $w_-$, giving an isolated real node, and positive for $w_+$, giving two real branches. At the lower value the other real points form the smooth circle $u\ge-w_-^2/4$ with $O$. It is separated from the isolated point, because $w_-^2(w_--1)<-w_-^2/4$.

## Measure, conditional means, and original norms

Let $\iota_X\Omega=-\mathrm dh$. On the regular locus the relative time form $\eta$ is uniquely characterized by $\mathrm dh\wedge\eta=\Omega$, where a local lift of $\eta$ is understood. Two lifts differ by a multiple of $\mathrm dh$, and contraction gives $\eta(X)=1$. We orient each circle by $X$ and write its positive period as $L_c(h)=\int_{C_h^c}\eta$.

[\[lem:coarea-projection\]]{#lem:coarea-projection label="lem:coarea-projection"} The measure $\mu=|\Omega|$ is $F$-invariant. On every regular circle one has $$\eta=\frac{\mathrm du}{2v+hu-T}=\frac{\mathrm du}{2Y},
 \qquad \mathrm d\mu=L(h)|\mathrm dh|\mathrm d\theta,
 \qquad \theta=t/L(h)\in\mathbb{R}/\mathbb{Z}.$$ The two circles at the same regular energy have the same positive period. Closed finite energy bands are compact, and the two critical fibres are $\mu$-null. The circlewise mean $$(\Pi f)|_{C_h^c}=\int_0^1 f(z_c(h,\theta))\,\mathrm{d}\theta
 \label{surf:projection}$$ defines an orthogonal projection on $L^2(\mu)$ and commutes with the Koopman operator $\mathsf U f=f\circ F$.

If $(X_1,Y_1)=F(x,y)$, then $\det DF=T/[y^2(x-y)]$ and $X_1Y_1=Tx/[y(x-y)]$. Thus $F^*\Omega=\Omega$ on the dense rational chart, and direct substitution gives $h\circ F=h$. Both identities extend to $U$. For the sign of the relative differential put $A=x(y-1)-Ty/x$. Then $2v+hu-T=TA/y^2$, $\mathrm du=-T\mathrm dy/y^2$, and $h_x=-A/(xy)$, so $\mathrm dh\wedge\mathrm du/(2v+hu-T)=+\Omega$. This is an identity of relative forms on regular fibres, not a smooth lift through a point with $\mathrm dh=0$. Real elliptic translation takes the identity circle to its other coset, preserving the invariant differential and its orientation. The periods are therefore equal. The time coordinate gives the displayed coarea formula with positive measure on each energy interval.

Properness is not inferred merely from compact fibres: $S_T\setminus D=\bar h^{-1}(\mathbb A^1)$ is a base change of the proper morphism $\bar h$. In real topology $S_T(\mathbb{R})$ is compact, and a closed finite interval $J\subset\mathbb{R}$ is closed in $\mathbb RP^1$. Thus $h^{-1}(J)$ is compact in $U$, with finite smooth area. A critical fibre minus its critical point is locally one-dimensional; adding that point does not change its zero area. Coarea and Fubini now reduce orthogonality of $\Pi$ to orthogonality of the constant-mode projection on each circle. Values on critical fibres do not affect this $L^2$ definition. For compactly supported $f$, its mean vanishes outside the compact saturation $h^{-1}(h(\mathop{\mathrm{supp}}f))$ and is bounded by $\|f\|_\infty$. Since $F$ carries each conditional probability to that on the image circle, taking its mean before or after $F$ gives the same result. This proves $\Pi\mathsf U=\mathsf U\Pi$.

The image of $\Pi$ is not the fixed-point subspace $\ker(\mathsf U-I)$. Choose a nonzero $\chi\in C_c^\infty((h_+,\infty))$, and put $f=\chi(h)$ and $f=-\chi(h)$ on the two upper circles, respectively, extending by zero elsewhere. The separated circle tubes and properness make this an original function in $C_c^\infty(U)$, including their terminal points. Equal periods give zero whole-fibre mean, whereas $\mathsf Uf=-f$ and $\langle\mathsf U^n f,f\rangle=(-1)^n\|f\|_2^2$. The same construction in the lower interval gives a $+1$ eigenfunction with zero whole-fibre mean. Thus whole-fibre centering does not even ensure convergence to zero; the required centering is [\[surf:projection\]](#surf:projection){reference-type="eqref" reference="surf:projection"}. It need not preserve original smoothness across the saddle, as Section [5](#sec:hyperbolic){reference-type="ref" reference="sec:hyperbolic"} will show.

[\[lem:regular-norms\]]{#lem:regular-norms label="lem:regular-norms"} On a compact regular circle tube, energy and positive time angle give bounded finite-order norm transformations from any fixed original smooth atlas. Terminal charts cause no additional loss.

In a terminal chart write $\Omega=c\,\mathrm da\wedge\mathrm db$. The table gives $h_b\ne0$ on $a=0$. On a sufficiently small compact neighbourhood $(h,a)$ are coordinates and $$\eta=-\frac{c}{h_b}\mathrm da,\qquad
 \partial_h=h_b^{-1}\partial_b,\qquad
 \partial_a|_h=\partial_a-(h_a/h_b)\partial_b.$$ All coefficients and any prescribed finite number of their derivatives are bounded; the inverse transformation has the same property. On a compact regular tube, a transverse section and the nonvanishing Hamiltonian flow produce smooth circle coordinates. A finite cover and the positive bounded period give the same derivative bounds.

## The sharp correlation theorem

For $f,g\in C_c^\infty(U)$, with inner product linear in its first slot, define $$C_n(f,g)=\langle\mathsf U^n(I-\Pi)f,(I-\Pi)g\rangle_{L^2(\mu)}.
 \label{surf:correlation}$$ Fix a closed finite interval $J$ containing the support energies; it may be enlarged to include both critical values and all stationary energies occurring below. Norms $\|\cdot\|_{C^a}$ mean ordinary finite-order norms in a fixed finite original atlas on a slightly larger compact saturated band. Constants may depend on $T,J$, that atlas, and the specified order. No uniformity as $T$ approaches a transition value is asserted.

Write $n=2m+r$, $m\ge1$, $r\in\{0,1\}$, and set $G=G_T=F_T^2$, $f_r=f\circ F^r$. Let $\rho_-,\rho_0$ be real lifts of the positive-time rotation of $F$ on the lower and middle intervals, and let $\rho_+$ be the lift of the return $F^2$ on the upper interval. The lifts and their complete derivative classification are proved in Section [4](#sec:frequency){reference-type="ref" reference="sec:frequency"}. In particular, both lower circles have the same rotation. The phase of $G$ is $$\sigma=2\rho_-\quad(h<h_-),\qquad
 \sigma=2\rho_0\quad(h_-<h<h_+),\qquad
 \sigma=\rho_+\quad(h>h_+).
 \label{eq:frequency-lifts}$$ On the persistent circle these phases extend analytically across $h_-$. Integer changes of lift have no effect on any formula below. Use the Fourier convention $\widehat f_{c,k}(h)=\int_0^1 f(z_c(h,\theta))e^{-2\pi\mathrm{i}k\theta}\,\mathrm{d}\theta$. An energy-dependent change of angular origin multiplies the two Fourier factors in a correlation by opposite phases, so their product is independent of this choice.

Let $\mathcal S_T$ be the set of stationary smooth circles for $\sigma$, counted by circle, not merely by energy. It consists of one middle circle if $0<T<3/16$; the persistent circle at $h_-=-2$ if $T=3/16$; two lower circles at one energy if $3/16<T<1$; no circle if $T=1$; and two upper circles at one energy if $T>1$. Each is a nondegenerate maximum, $\sigma''(h_c)<0$. Define the absolutely convergent series $$\mathcal A_r(m)=\sum_{c\in\mathcal S_T}\sum_{k\ne0}
 \frac{L(h_c)\widehat{f_r}_{c,k}(h_c)
       \overline{\widehat g_{c,k}(h_c)}}{\sqrt{|k\sigma''(h_c)|}}
 e^{2\pi\mathrm{i}km\sigma(h_c)+\mathrm{i}\pi\mathop{\mathrm{sgn}}(k\sigma''(h_c))/4}.
 \label{eq:stationary-coefficient}$$ For the shrinking circle at $s_-$ put $$\varepsilon=h_--h,\qquad
 \theta_T=\frac12+\frac1\pi\arctan\frac1{\sqrt{3-4w_-}},\qquad
 \sigma_c=2\theta_T,\quad \sigma_E(\varepsilon)=2\rho_-(h_--\varepsilon).$$ In the positive symmetric angle of Section [6](#sec:elliptic){reference-type="ref" reference="sec:elliptic"}, for $k\ne0$ set $$\begin{gathered}
 A_k^{(r)}=\left.\partial_\varepsilon
       \left[L\widehat{f_r}_k\overline{\widehat g_k}\right]
       \right|_{\varepsilon=0},\qquad A_k^{(r)}=0\quad(|k|\ne1),\\
 \mathcal B_r(m)=-\sum_{k=\pm1}
       \frac{A_k^{(r)}}{(2\pi k\beta)^2}e^{2\pi\mathrm{i}km\sigma_c},
 \quad \beta=\sigma_E'(0)=-2\rho_-'(h_-)\ne0
       \quad(T\ne3/16),\\
 \mathcal D_r(m)=\sum_{k=\pm1}
       \frac{\mathrm{i}A_k^{(r)}}{2\pi k\gamma}e^{2\pi\mathrm{i}km\sigma_c},
 \quad \gamma=\sigma_E''(0)=2\rho_-''(h_-)<0
       \quad(T=3/16).
\end{gathered}
\label{eq:center-coefficients}$$ Here the derivatives and the vanishing assertion concern $k\ne0$. They are well defined by the original-jet expansion proved below; neither the observable nor its remainder is restricted to two modes.

[\[thm:main\]]{#thm:main label="thm:main"} For each fixed $T>0$ and compact band as above, the original observables $f,g\in C_c^\infty(U)$ satisfy, for $m\ge1$ and $r=0,1$, $$\begin{array}{ll}
 T\notin\{3/16,1\}:&
 C_{2m+r}=m^{-1/2}\mathcal A_r(m)+O(M_{20}m^{-3/2}),\\[1mm]
 T=3/16:&
 C_{2m+r}=m^{-1/2}\mathcal A_r(m)+m^{-1}\mathcal D_r(m)
                    +O(M_{20}m^{-3/2}),\\[1mm]
 T=1:&
 C_{2m+r}=m^{-2}\mathcal B_r(m)+O(M_{20}m^{-3}),
\end{array}
\label{eq:main-asymptotics}$$ where $M_a=\|f\|_{C^a}\|g\|_{C^a}$ and the implicit constants are independent of $f,g,m,r$.

There is a sufficiently small fixed saddle energy neighbourhood such that, for every fixed smooth energy cutoff $\chi$ supported there and every specified integer $N\ge1$, $$\left|\int_U\chi(h(z))[(I-\Pi)f](F^{2m+r}z)
                  \overline{[(I-\Pi)g](z)}\,\mathrm{d}\mu(z)\right|
 \le C_{N,\chi} M_{N+2}m^{-N}.$$ The integral includes all circles on both sides of the saddle.

The global rates are $O(|n|^{-1/2})$ for $T\ne1$ and $O(|n|^{-2})$ for $T=1$. For every fixed $T$, there are real-valued original observables, and also complex-valued choices, for which the corresponding normalized absolute correlation has positive $\limsup$ as $n\to\infty$. At $T=1$ this holds whenever $A_1^{(0)},A_{-1}^{(0)}$ are not both zero, an open dense condition on pairs of original first jets. If both vanish, the correlation is $O(M_{20}|n|^{-3})$.

The proof occupies the remaining sections. The coefficients already retain the original odd steps through $f_r$; Proposition [\[prop:parity\]](#prop:parity){reference-type="ref" reference="prop:parity"} will give their explicit two-circle form. Negative times satisfy $C_{-n}(f,g)=\overline{C_n(g,f)}$ by unitarity. Sharpness is an existence or nonvanishing-jet statement, not a lower bound for every pair of observables or at every time. In particular, a function on only one of two exchanged circles can have identically zero odd autocorrelations. The theorem imposes no nonresonance assumption and does not assert mixing of an individual circle or of the unprojected system.

# Picard--Fuchs forcing {#sec:forcing}

The locations and orders of the stationary circles are controlled by an inhomogeneous period equation. Its forcing depends on the marked section $P$, so the moving endpoint must be retained throughout the reduction. In the curve [\[eq:weierstrass\]](#eq:weierstrass){reference-type="eqref" reference="eq:weierstrass"}, set $$\begin{gathered}
s=h^2-4T,\qquad X=u+s/12,\qquad Y=v+(hu-T)/2,\\
Y^2=f(X,h)=X^3+aX+b,\\
a=-\frac{s^2+24hT}{48},\qquad
b=\frac{s^3+36hTs+216T^2}{864}.
\end{gathered}$$ The marked point is $(X_P,Y_P)=(s/12,T/2)$, and the relative differential is still $\omega=\,\mathrm{d}X/(2Y)$: no energy-dependent rescaling has been made. Write $q_0=8h-9$ and $H=32T+3h$, and retain the discriminant polynomial $\delta$ from [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}.

[\[prop:pf\]]{#prop:pf label="prop:pf"} On any sufficiently small complex parameter domain with $q_0\delta\ne0$, every period $L$ of $\omega$ and every local integral $I=\int_O^P\omega$ satisfy $$\begin{aligned}
\mathcal L
&=\partial_h^2+\left(\frac{\delta'}{\delta}-\frac8{q_0}\right)
  \partial_h+\frac{8h^3-18h^2+9h-12T}{q_0\delta},
\label{eq:pf-operator}\\
\mathcal L L&=0,\qquad \mathcal L I=-\frac{H}{q_0\delta}.
\label{eq:pf-forcing}\end{aligned}$$ For a real positive period $L$ and the real positive arc integral $I_j$ from $O$ to $jP$, put $\rho=I_j/L$. Here $j=1$ on the lower and middle intervals, while $j=2$ on the upper interval. Then $$\label{eq:wronskian}
J_\rho=\frac{\delta}{q_0}L^2\rho',\qquad
J_\rho'=-\frac{jHL}{q_0^2}.$$ These identities use the actual circle return: $+P$ below the saddle and $+2P$ above it.

*Marked reduction.* In this proof $D=\partial_h$ acts at fixed $X$ and $T$, whereas primes on the marked coordinates denote their total derivatives. Thus $DY=f_h/(2Y)$, and $f_h(P)$ means differentiation before evaluation at $X_P$. With $\omega_1=X\omega$, define $$\begin{gathered}
\alpha_{\mathrm{PF}}=-\frac{\delta'}{12\delta},\qquad
\beta_{\mathrm{PF}}=-\frac{q_0}{\delta},\qquad
\gamma_{\mathrm{PF}}=\frac{a\beta_{\mathrm{PF}}}{3},\\
\kappa_{\mathrm{PF}}=\frac{\beta_{\mathrm{PF}}'}{\beta_{\mathrm{PF}}}
=\frac8{q_0}-\frac{\delta'}{\delta},\\
V_{\mathrm{PF}}=\alpha_{\mathrm{PF}}'+\alpha_{\mathrm{PF}}^2
+\beta_{\mathrm{PF}}\gamma_{\mathrm{PF}}
-\alpha_{\mathrm{PF}}\kappa_{\mathrm{PF}},\\
r_0=2\alpha_{\mathrm{PF}}X-2\beta_{\mathrm{PF}}X^2
-\tfrac43a\beta_{\mathrm{PF}},\\
r_1=2\alpha_{\mathrm{PF}}X^2+\tfrac23a\beta_{\mathrm{PF}}X
+2b\beta_{\mathrm{PF}},\qquad R_i=\frac{r_i}{2Y}.
\end{gathered}$$ Differentiating the displayed coefficients $a,b$ gives $a'=-4a\alpha_{\mathrm{PF}}+6b\beta_{\mathrm{PF}}$ and $b'=-6b\alpha_{\mathrm{PF}}-4a^2\beta_{\mathrm{PF}}/3$. Equating coefficients of $X$ then gives the two polynomial identities $$\label{pf:reduction-polynomials}
\begin{aligned}
-f_h&=2(\alpha_{\mathrm{PF}}+\beta_{\mathrm{PF}}X)f
       +2f(r_0)_X-f_Xr_0,\\
-Xf_h&=2(\gamma_{\mathrm{PF}}-\alpha_{\mathrm{PF}}X)f
       +2f(r_1)_X-f_Xr_1.
\end{aligned}$$ Multiplication by $\,\mathrm{d}X/(4Y^3)$ proves the exact differential identities $$\label{pf:gauss-manin}
\begin{aligned}
D\omega&=\alpha_{\mathrm{PF}}\omega
+\beta_{\mathrm{PF}}\omega_1+\,\mathrm{d}_XR_0,\\
D\omega_1&=\gamma_{\mathrm{PF}}\omega
-\alpha_{\mathrm{PF}}\omega_1+\,\mathrm{d}_XR_1.
\end{aligned}$$ Here $\,\mathrm{d}_X$ denotes the relative differential. The same polynomials also give $R_1-XR_0=\beta_{\mathrm{PF}}Y$. Differentiating the first line of [\[pf:gauss-manin\]](#pf:gauss-manin){reference-type="eqref" reference="pf:gauss-manin"} and eliminating $\omega_1$ yields $$\label{pf:exact-primitive}
\begin{aligned}
(D^2-\kappa_{\mathrm{PF}}D-V_{\mathrm{PF}})\omega
&=\,\mathrm{d}_XQ_{\mathrm{PF}},\\
Q_{\mathrm{PF}}
&=(D+\alpha_{\mathrm{PF}}-\kappa_{\mathrm{PF}})R_0
  +\beta_{\mathrm{PF}}R_1\\
&=\frac{2V_{\mathrm{PF}}X-\beta_{\mathrm{PF}}a'}{2Y}
  -\frac{r_0f_h}{4Y^3}.
\end{aligned}$$ For the last equality, the numerator identity is $Dr_0+(\alpha_{\mathrm{PF}}-\kappa_{\mathrm{PF}})r_0
+\beta_{\mathrm{PF}}r_1=2V_{\mathrm{PF}}X-\beta_{\mathrm{PF}}a'$. Substitution and a common denominator give $-V_{\mathrm{PF}}=(8h^3-18h^2+9h-12T)/(q_0\delta)$; hence the operator in [\[pf:exact-primitive\]](#pf:exact-primitive){reference-type="eqref" reference="pf:exact-primitive"} is [\[eq:pf-operator\]](#eq:pf-operator){reference-type="eqref" reference="eq:pf-operator"}. Integrating the exact differential over any locally transported closed cycle proves $\mathcal L L=0$.

*The two endpoints.* Near $O$ choose the local coordinate $t=X^{-1/2}$ with $Y=t^{-3}(1+at^4+bt^6)^{1/2}$. Then $\omega=-(1+O(t^4))\,\mathrm{d}t$, so $I$ converges, but the individual primitives have poles: $$R_0=-\frac{\beta_{\mathrm{PF}}}{t}
  +\alpha_{\mathrm{PF}}t+O(t^3),\qquad
R_1=\frac{\alpha_{\mathrm{PF}}}{t}
  +\gamma_{\mathrm{PF}}t+O(t^3).$$ Their combination in [\[pf:exact-primitive\]](#pf:exact-primitive){reference-type="eqref" reference="pf:exact-primitive"} has pole coefficient $-\beta_{\mathrm{PF}}'
-(\alpha_{\mathrm{PF}}-\kappa_{\mathrm{PF}})\beta_{\mathrm{PF}}
+\beta_{\mathrm{PF}}\alpha_{\mathrm{PF}}=0$. There is no constant term, so $Q_{\mathrm{PF}}=O(t)$ and $Q_{\mathrm{PF}}(O)=0$. In particular, the two divergent primitives have not been separately assigned values at $O$.

Apply Leibniz' rule twice, first with a fixed $X$ cutoff near $O$ and then let the cutoff tend to $O$. The preceding expansions control this limit and give all moving-endpoint terms: $$\label{pf:leibniz}
\begin{aligned}
\mathcal L I&=Q_{\mathrm{PF}}(P)-Q_{\mathrm{PF}}(O)
+\frac{X_P''-\kappa_{\mathrm{PF}}X_P'}{2Y_P}
\\
&\hspace{1em}-\frac{2X_P'f_h(P)+(X_P')^2f_X(P)}{4Y_P^3}.
\end{aligned}$$ Although $Y_P'=0$, the identity is $f_h(P)+f_X(P)X_P'=0$, not $f_h(P)=0$. In fact $X_P'=h/6$, $X_P''=1/6$, $f_X(P)=-Th/2$ and $f_h(P)=Th^2/12$. Thus the moving terms in [\[pf:leibniz\]](#pf:leibniz){reference-type="eqref" reference="pf:leibniz"} sum to $-h^3/(36T^2)+(1-\kappa_{\mathrm{PF}}h)/(6T)$, while evaluation of [\[pf:exact-primitive\]](#pf:exact-primitive){reference-type="eqref" reference="pf:exact-primitive"} gives $$Q_{\mathrm{PF}}(P)=\frac{h^3}{36T^2}
+\frac{\kappa_{\mathrm{PF}}h-1}{6T}-\frac{H}{q_0\delta}.$$ The cancellation proves the inhomogeneous identity [\[eq:pf-forcing\]](#eq:pf-forcing){reference-type="eqref" reference="eq:pf-forcing"}.

*The real return and its Wronskian.* For $j=1$ the positive real arc is a choice of $I$. For $j=2$, a local complex elliptic logarithm satisfies $\log(2P)=2\log(P)$ modulo the period lattice. Consequently the actual real arc $I_2$ differs from $2I$ by a locally fixed integral combination of periods, all annihilated by $\mathcal L$. This proves $\mathcal L I_j=-jH/(q_0\delta)$ in both cases; it does not identify a complex arc to $P$ on the upper interval with a real single-circle step. For $W=L I_j'-I_jL'=L^2\rho'$, subtraction of the two scalar equations gives $$W'=\kappa_{\mathrm{PF}}W-\frac{jHL}{q_0\delta}.$$ Since $(\delta/q_0)'/(\delta/q_0)=-\kappa_{\mathrm{PF}}$, multiplication by $\delta/q_0$ proves [\[eq:wronskian\]](#eq:wronskian){reference-type="eqref" reference="eq:wronskian"}.

The zero of $q_0$ is introduced by eliminating $\omega_1$; it is not a singular fibre. The real rotation function remains analytic there. The next section treats this apparent pole and fixes the integration constants in [\[eq:wronskian\]](#eq:wronskian){reference-type="eqref" reference="eq:wronskian"} using the actual finite and infinite ends of the real circles.

# The global frequency geometry {#sec:frequency}

The forcing identity determines the frequency derivative only after its integration constant has been fixed. The persistent circle at $h_-$ fixes one constant; differentiable real integrals at the two infinite ends fix the others. We keep the positive time orientation and the lifts [\[eq:frequency-lifts\]](#eq:frequency-lifts){reference-type="eqref" reference="eq:frequency-lifts"} throughout.

## The persistent circle and its anchor

Use the completed-square coordinates [\[surf:completed-square\]](#surf:completed-square){reference-type="eqref" reference="surf:completed-square"}, and write $f_h=\Phi_h$ for that cubic. Thus $$\label{freq:cubic}
 Y^2=f_h(u),\qquad \omega=\frac{\,\mathrm{d}u}{2Y}.$$ At either critical value from [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}, direct substitution gives $$\label{freq:node-factorization}
 f_{h(w)}(u)=(u-a_w)^2(u-b_w),\qquad
 a_w=w^2(w-1),\quad b_w=-w^2/4.$$ For $w=w_-$, we have $a_w<b_w<0$; hence the isolated node is separated from the circle containing $O$ and $P$.

[\[lem:persistent\]]{#lem:persistent label="lem:persistent"} The positive period $L$ and the one-step frequency on the persistent circle extend real analytically across $h_-$. The frequency restricts to $\rho_-$ below $h_-$ and to $\rho_0$ above it. Writing $L_0=L(h_-)$, their common endpoint values are $$\label{eq:center-frequency}
 L_0=\frac{2\pi}{|w_-|\sqrt{3-4w_-}},\qquad
 \rho(h_-)=\theta_T:=\frac12+
 \frac1\pi\arctan\frac1{\sqrt{3-4w_-}}\in(1/2,2/3).$$ With a star denoting evaluation at $h_-$, the centre phase has jets $$\label{eq:center-phase-jets}
 \begin{aligned}
 \rho'(h_-)&=-\frac{H_*}{q_{0,*}\delta'_*L_0},
 &\beta=-2\rho'(h_-)&=\frac{2H_*}{q_{0,*}\delta'_*L_0},\\
 T=3/16:\quad \rho''(h_-)&=-\frac{3}{2q_{0,*}\delta'_*L_0},
 &\gamma=2\rho''(h_-)&=-\frac{12}{3125L_0}<0.
 \end{aligned}$$ In particular, $\beta$ vanishes exactly at $T=3/16$.

The simple root $b_{w_-}$ extends to a real analytic root $r(h)$ near $h_-$, with $f_h(u)=(u-r(h))g_h(u)$. At $h_-$, $g_h(u)=(u-a_{w_-})^2$, which is positive for $u\ge r(h)$. This positivity persists uniformly: on a bounded interval it follows from a positive lower bound, and at infinity from the monic quadratic term. A single analytic parametrization of the persistent circle is $$\label{freq:persistent-parametrization}
 u=r(h)+s^2,\qquad Y=s\sqrt{g_h(r(h)+s^2)},\qquad
 \omega=\frac{\,\mathrm{d}s}{\sqrt{g_h(r(h)+s^2)}},
 \quad s\in\mathbb{R}\mathbf P^1.$$ At $s=0$ the differential is regular after cancellation; in the chart $1/s$ it is analytic and nonzero at $O$. Thus the integrals on this compact circle are analytic in $h$. The marked section $P$ corresponds to $s=p(h):=\sqrt{-r(h)}>0$. Since increasing $s$ is positive time, $$\label{freq:one-step-integrals}
 L=\int_{-\infty}^{\infty}\frac{\,\mathrm{d}s}{\sqrt{g_h(r(h)+s^2)}},\qquad
 A=\int_0^{p(h)}\frac{\,\mathrm{d}s}{\sqrt{g_h(r(h)+s^2)}},\qquad
 \rho=\frac12+\frac{A}{L}.$$ This fixes both the orientation and the integer lift. At $h_-$ the kernel is $(s^2+d_-^2)^{-1}$, where $d_-^2=b_{w_-}-a_{w_-}=w_-^2(3-4w_-)/4$. Consequently $L_0=\pi/d_-$ and $A(h_-)=d_-^{-1}\arctan(\sqrt{-b_{w_-}}/d_-)$, proving [\[eq:center-frequency\]](#eq:center-frequency){reference-type="eqref" reference="eq:center-frequency"}. Below $h_-$, translation identifies the two real circles, preserving $\omega$ and commuting with $+P$. Their periods and frequencies therefore agree, so the same endpoint jets apply to the circle that shrinks to the centre.

By [\[eq:wronskian\]](#eq:wronskian){reference-type="eqref" reference="eq:wronskian"}, with the single-step factor $j=1$, $$\label{freq:anchored-wronskian}
 J_\rho=\frac{\delta}{q_0}L^2\rho'
 =-\int_{h_-}^{h}\frac{H(s)L(s)}{q_0(s)^2}\,\,\mathrm{d}s,
 \qquad h<h_+.$$ Indeed, $L$ and $\rho'$ are analytic at $h_-$, $q_0(h_-)\ne0$, and $\delta(h_-)=0$, so the integration constant is zero. The elementary factorizations $$\label{freq:anchor-signs}
 H_* =w_-(2w_-+1)(4w_--3)^2,\qquad
 \delta'_* =w_-^2(4w_--3)^3<0$$ show that $H_*$ is negative, zero, or positive according as $T<3/16$, $T=3/16$, or $T>3/16$; equality corresponds to $w_-=-1/2$. Expanding [\[freq:anchored-wronskian\]](#freq:anchored-wronskian){reference-type="eqref" reference="freq:anchored-wronskian"} to first order gives the first line of [\[eq:center-phase-jets\]](#eq:center-phase-jets){reference-type="eqref" reference="eq:center-phase-jets"}. When $H_*=0$, put $t=h-h_-$. Since $H=3t$, $J_\rho=-3L_0t^2/(2q_{0,*}^2)+O(t^3)$, whereas $\delta=\delta'_*t+O(t^2)$. Comparing these analytic expansions gives the second line; here $h_-=-2$, $q_{0,*}=-25$, and $\delta'_*=-125/4$.

The anchored identity also bounds the number of stationary energies. Put $h_0=-32T/3$, the unique zero of $H$. Since $q_0<0$ on $h<h_+$, the sign of $\rho'$ is the sign of $-J_\rho$ below $h_-$ and of $J_\rho$ above it. If $T\le3/16$, then $H<0$ below $h_-$, so $J_\rho<0$ and $\rho_-'>0$. If $T\ge3/16$, then $H>0$ on $(h_-,h_+)$, so $J_\rho<0$ and $\rho_0'<0$. For $T>3/16$, we have $h_0<h_-$, $J_\rho>0$ on $[h_0,h_-)$, and $J_\rho'>0$ on $(-\infty,h_0)$. There is at most one zero there, and at that zero $\rho''=q_0J_\rho'/(\delta L^2)<0$. For $T<3/16$, the factorization at $w_+>1$ gives $H(h_+)>0$, so $h_-<h_0<h_+$. Now $J_\rho>0$ on $(h_-,h_0]$ and $J_\rho'<0$ on $(h_0,h_+)$. Again there is at most one zero, and it is a nondegenerate maximum.

## The middle interval and the upper return

On $(h_-,h_+)$, the cubic $f_h$ has a single real root $r(h)<0$. Its remaining quadratic factor is positive everywhere. Thus [\[freq:persistent-parametrization\]](#freq:persistent-parametrization){reference-type="eqref" reference="freq:persistent-parametrization"}--[\[freq:one-step-integrals\]](#freq:one-step-integrals){reference-type="eqref" reference="freq:one-step-integrals"} hold on the whole middle interval, with $1/2<\rho_0<1$. As $h\uparrow h_+$, write $a=a_{w_+}>0$ and $b=b_{w_+}<0$. The simple root tends to $b$ and $g_h(u)$ tends to $(u-a)^2$. The short arc $0\le s\le\sqrt{-r(h)}$ stays a fixed distance from $u=a$; hence its integral has the finite limit $$A(h)\longrightarrow\int_0^{\sqrt{-b}}\frac{\,\mathrm{d}s}{a-b-s^2}.$$ The full-period kernel tends to $|s^2-(a-b)|^{-1}$. On a fixed interval around $\sqrt{a-b}$, Fatou's lemma forces $L\to\infty$, since the limiting nonnegative kernel is not integrable. This holds along every approaching sequence. Therefore $\rho_0\to1/2$. For $T<3/16$, [\[eq:center-phase-jets\]](#eq:center-phase-jets){reference-type="eqref" reference="eq:center-phase-jets"} gives $\rho_0'(h_-)>0$, while the upper endpoint $1/2$ lies below $\theta_T$. The mean value theorem supplies a point with negative derivative. The preceding one-zero bound now proves that the middle maximum exists and is unique.

On the upper interval the ordered roots satisfy $r_1<0<r_2<r_3$. Parametrize its identity circle by $$u=r_3+s^2,\qquad
 Y=s\sqrt{(s^2+r_3-r_1)(s^2+r_3-r_2)}.$$ Let $\psi_h(s)$ denote the positive reciprocal square root in this formula. Since $2P$ belongs to this component, $T\ge r_3>r_2$. The point $2P=(T,T(h-1)/2)$ has the analytic signed parameter $$\label{freq:upper-real-arc}
 s_2(h)=\frac{T(h-1)}{2\sqrt{(T-r_1)(T-r_2)}},\qquad
 s_2(h)^2=T-r_3,\qquad
 \rho_+(h)=\frac{\displaystyle\int_{-\infty}^{s_2(h)}\psi_h(s)\,\,\mathrm{d}s}
 {\displaystyle\int_{-\infty}^{\infty}\psi_h(s)\,\,\mathrm{d}s}.$$ The denominator defining $s_2$ is strictly positive. Thus the formula has no spurious singularity at $h=1$, where evenness gives $\rho_+(1)=1/2$. Compact-circle regularity, including the $1/s$ chart, proves that $L$ and $\rho_+$ are analytic for every $h>h_+$, and $0<\rho_+<1$. This is the real $2P$ arc, not an arc from $O$ to the other component.

At $h\downarrow h_+$, the roots tend to $b,a,a$ and $s_2\to-\sqrt{T-a}<0$, since $T=w_+a>a$. The full-period kernel tends to $1/(|s|\sqrt{s^2+a-b})$, so Fatou's lemma again gives $L\to\infty$. The arc in the numerator ends a fixed negative distance from zero. On bounded subarcs its kernel is uniformly bounded, and at negative infinity it is bounded by $C/s^2$. Dominated convergence gives a finite positive numerator limit. Hence $\rho_+\to0$.

The double-step identity [\[eq:wronskian\]](#eq:wronskian){reference-type="eqref" reference="eq:wronskian"} gives $J_{\rho_+}'=-2HL/q_0^2<0$ wherever $q_0\ne0$; here $H>0$ on the entire upper interval. The apparent singularity $h_q=9/8$ does not belong to the discriminant. Indeed, $K_{\mathrm{tw}}:=\delta L^2\rho_+'$ is analytic there, and $$\label{freq:apparent-point}
 q_0K_{\mathrm{tw}}'-8K_{\mathrm{tw}}=-2HL,
 \qquad
 \rho_+'(h_q)=\frac{H(h_q)}{4\delta(h_q)L(h_q)}>0.$$ The second equality follows by analytic continuation and evaluation at $h_q$. Thus $J_{\rho_+}=K_{\mathrm{tw}}/q_0$ tends to $-\infty$ from the left and $+\infty$ from the right. On $(h_+,h_q)$, a point with $J_{\rho_+}\ge0$ would, by strict decrease, give $J_{\rho_+}>0$ at all earlier points and hence $\rho_+'<0$ there. This contradicts $\rho_+>0$ and its lower endpoint zero. Therefore $\rho_+'>0$ up to and including $h_q$. Above $h_q$, $J_{\rho_+}$ strictly decreases from $+\infty$ and has at most one zero. At such a zero, $\rho_+''=q_0J_{\rho_+}'/(\delta L^2)<0$.

## Differentiable infinity constants

The remaining existence decisions require constants, not just the sign of the forcing. Although the observables have compact support, these limits are needed to classify all finite stationary circles.

[\[lem:infinity\]]{#lem:infinity label="lem:infinity"} For each fixed $T>0$, the two weighted derivatives satisfy $$\label{eq:infinity-constants}
 \begin{aligned}
 J_{\rho_-}(h)&=\frac{\log T}{8}
       +O_T\!\left(\frac{\log|h|}{|h|}\right)&& (h\to-\infty),\\
 J_{\rho_+}(h)&=-\frac{\log T}{4}
       +O_T\!\left(\frac{\log h}{h}\right)&& (h\to+\infty).
 \end{aligned}$$ The limits hold also at $T=1$.

Write $h=\nu/\xi$, where $\nu\in\{-1,1\}$ and $\xi>0$ tends to zero, and put $\ell=\log(1/\xi)$, $c=\log T$. The notation $R=O_{C^1,T}(\xi^a\ell^b)$ means $|R|+|\xi\partial_\xi R|\le C_T\xi^a\ell^b$. Substitution of $u=\nu T\xi+\xi^2z$ into $\xi^{-2}f_{\nu/\xi}(u)$ gives the exact polynomial $$\Phi_\nu(\xi,z)=\frac{z^2}{4}-T^3
 +\nu\xi(T^3-2T^2z)+\xi^2(3T^2z-Tz^2)
 +3\nu T\xi^3z^2+\xi^4z^3.$$ Its roots $z=\pm2T^{3/2}$ at $\xi=0$ are simple. Their analytic continuations $z_\pm(\xi)$ therefore give $$r_2=\nu T\xi+\xi^2z_-(\xi),\quad
 r_3=\nu T\xi+\xi^2z_+(\xi),\quad
 r_1=T-\frac1{4\xi^2}-r_2-r_3.$$ These are all three ordered real roots for sufficiently small $\xi$. Analytic Taylor remainders yield $$\label{freq:root-scales}
 \begin{aligned}
 D_r:=r_3-r_1&=\frac{1+O_{C^1,T}(\xi^2)}{4\xi^2},&
 d_r:=r_3-r_2&=4T^{3/2}\xi^2(1+O_{C^1,T}(\xi)),\\
 \kappa_{\mathrm{mod}}:=\sqrt{d_r/D_r}
 &=4T^{3/4}\xi^2(1+O_{C^1,T}(\xi)).
 \end{aligned}$$ In particular $\xi\kappa_{\mathrm{mod}}'/\kappa_{\mathrm{mod}}
=2+O_T(\xi)$. The derivative information comes from the root equation, not from differentiating an uncontrolled asymptotic.

For $\lambda>0$ define $$K_c(\lambda)=\int_0^\infty
 \frac{\,\mathrm{d}t}{\sqrt{(1+t^2)(\lambda^2+t^2)}}.$$ The substitution $u=r_3+D_rt^2$ gives $L=2K_c(\kappa_{\mathrm{mod}})/\sqrt{D_r}$. We need the constant and a derivative estimate: $$\label{freq:complete-integral}
 K_c(\lambda)=\log(4/\lambda)+E(\lambda),\qquad
 |E|+|\lambda E'|\le C\lambda^2\log(1/\lambda).$$ To prove it, subtract $\operatorname{arsinh}(1/\lambda)$ and split at $t=1$. The remainder is $$R(\lambda)=\int_0^1\frac{a(t)\,\,\mathrm{d}t}{\sqrt{t^2+\lambda^2}}
 +\int_1^\infty\frac{\,\mathrm{d}t}{\sqrt{1+t^2}\sqrt{t^2+\lambda^2}},
 \qquad a(t)=(1+t^2)^{-1/2}-1.$$ Since $|a(t)|\le Ct^2$, setting $\lambda=0$ is legitimate. The primitive $\log(t/(1+\sqrt{1+t^2}))$ of $1/(t\sqrt{1+t^2})$ shows that $R(0)=\log2$. For $t<\lambda$, bound the difference of the reciprocal square roots by $1/t$; for $\lambda<t<1$, bound it by $\lambda^2/(2t^3)$. After multiplication by $|a(t)|$, these give $|R(\lambda)-R(0)|\le C\lambda^2\log(1/\lambda)$; the tail is $O(\lambda^2)$. Differentiation is legitimate for each positive $\lambda$. The first derivative kernel, after multiplication by $\lambda$, is bounded by $\lambda^2|a(t)|/(t^2+\lambda^2)^{3/2}$. The same split gives respectively $O(\lambda^2)$ and $O(\lambda^2\log(1/\lambda))$, with an $O(\lambda^2)$ tail. Finally $\operatorname{arsinh}(1/\lambda)-\log(2/\lambda)$ and its $\lambda\partial_\lambda$ derivative are $O(\lambda^2)$. This proves [\[freq:complete-integral\]](#freq:complete-integral){reference-type="eqref" reference="freq:complete-integral"}, and hence $$\label{freq:period-C1}
 L=\xi\bigl(8\ell-3c+R_L(\xi)\bigr),\qquad
 R_L=O_{C^1,T}(\xi).$$

The two incomplete arcs have different moving scales. Set $U_-=0$ and $U_+=T$, so the relevant marked point is $P$ at the negative end and $2P$ at the positive end. There its $Y$ coordinate is positive, and $B_\nu:=U_\nu-r_3>0$. The exact positive integrals are $$\label{freq:infinity-arcs}
 \begin{aligned}
 A_\nu&=\frac12\int_{r_3}^{U_\nu}\frac{\,\mathrm{d}u}{\sqrt{f_h(u)}}
 =\frac1{2\sqrt{D_r}}\int_0^{B_\nu}
 \frac{(1+t/D_r)^{-1/2}}{\sqrt{t(t+d_r)}}\,\,\mathrm{d}t,\\
 \rho_\nu&=\frac12+\frac{A_\nu}{L}.
 \end{aligned}$$ Put $\eta=d_r/B_\nu$ and $\zeta=B_\nu/D_r$. The integral without the factor $(1+t/D_r)^{-1/2}$ is $2\operatorname{arsinh}(\eta^{-1/2})$. After $t=B_\nu x$, its error is $$\mathcal E(\eta,\zeta)=\int_0^1
 \frac{(1+\zeta x)^{-1/2}-1}{\sqrt{x(x+\eta)}}\,\,\mathrm{d}x,
 \qquad
 |\mathcal E|+|\eta\partial_\eta\mathcal E|
       +|\zeta\partial_\zeta\mathcal E|\le C\zeta.$$ Indeed, the numerator and its $\zeta\partial_\zeta$ derivative are bounded by $C\zeta x$; the $\eta$ derivative adds a factor bounded by $\eta/(2(x+\eta))\le1/2$. The resulting integrals are dominated by $C\zeta$. The analytic roots give $$\begin{array}{ll}
 B_-=T\xi(1+O_{C^1,T}(\xi)),&
 \eta_-=4\sqrt T\,\xi(1+O_{C^1,T}(\xi)),\quad
 \zeta_-=O_{C^1,T}(\xi^3),\\
 B_+=T(1+O_{C^1,T}(\xi)),&
 \eta_+=4\sqrt T\,\xi^2(1+O_{C^1,T}(\xi)),\quad
 \zeta_+=O_{C^1,T}(\xi^2).
 \end{array}$$ All these positive parameters have bounded $\xi$ logarithmic derivatives. Thus the displayed two-parameter bound remains valid with first-derivative control along both paths. Using $$\operatorname{arsinh}(\eta^{-1/2})=
 \log2-\tfrac12\log\eta+
 \log\frac{1+\sqrt{1+\eta}}2,$$ whose last term and $\eta\partial_\eta$ derivative are $O(\eta)$, we obtain $$\label{freq:arcs-C1}
 A_-=\xi(\ell-c/2+R_-),\qquad
 A_+=\xi(2\ell-c/2+R_+),\qquad
 R_\pm=O_{C^1,T}(\xi).$$

We can now differentiate before taking a limit. Let $a_-=1$, $a_+=2$, $B=8\ell-3c$ and $C_\nu=a_\nu\ell-c/2$. Equations [\[freq:period-C1\]](#freq:period-C1){reference-type="eqref" reference="freq:period-C1"} and [\[freq:arcs-C1\]](#freq:arcs-C1){reference-type="eqref" reference="freq:arcs-C1"} imply $$L\partial_\xi A_\nu-A_\nu\partial_\xi L
 =\xi^2(B\partial_\xi C_\nu-C_\nu\partial_\xi B)
       +O_T(\xi^2\ell)
 =\xi(3a_\nu-4)c+O_T(\xi^2\ell).$$ Every remainder term here uses the proved bounds $|R_L|+|R_\nu|=O_T(\xi)$ and $|R_L'|+|R_\nu'|=O_T(1)$. Since $\partial_h=-\nu\xi^2\partial_\xi$ and $\delta/q_0=\nu(1+O_T(\xi))/(8\xi^3)$, $$L^2\rho_\nu'=-\nu(3a_\nu-4)c\xi^3+O_T(\xi^4\ell),
 \qquad
 J_{\rho_\nu}=-\frac{(3a_\nu-4)c}{8}+O_T(\xi\ell).$$ This proves [\[eq:infinity-constants\]](#eq:infinity-constants){reference-type="eqref" reference="eq:infinity-constants"} without division by $c$, so it includes $T=1$. The same integral ratios give $\rho_-\to5/8$ and $\rho_+\to3/4$; no derivative is taken of these last ratio limits.

## Exactly the stationary circles

[\[prop:frequency\]]{#prop:frequency label="prop:frequency"} The three return-frequency lifts have exactly the derivative signs in Table [3](#freq:classification-table){reference-type="ref" reference="freq:classification-table"}. Every stationary point listed there is a nondegenerate maximum, and there are no other stationary points. At $T=3/16$, the persistent circle at $h_-=-2$ is an additional nondegenerate stationary circle, although the whole fibre at that energy is singular.

Only the two outer existence decisions remain. If $T>3/16$, the anchored identity gives $J_{\rho_-}>0$ on $[h_0,h_-)$ and strict increase on $(-\infty,h_0)$. For $3/16<T<1$ its limit $(\log T)/8$ is negative, so it crosses zero exactly once. For $T\ge1$ the limit is nonnegative, and strict increase makes $J_{\rho_-}>0$ throughout the remaining interval. Since $q_0/(\delta L^2)<0$, these are respectively the lower maximum and strict decrease. In particular, the zero limit at $T=1$ does not produce a finite zero.

Above $h_q$, $J_{\rho_+}$ strictly decreases from $+\infty$ to $-(\log T)/4$. For $T\le1$ it is strictly positive at every finite point, while for $T>1$ it crosses zero exactly once. The signs below $h_q$ and the nondegeneracy at any zero were proved above. The middle existence argument and the anchored lower signs give the other entries. All inequalities are strict away from the specified zeros, excluding horizontal inflection points. Finally, [\[eq:center-phase-jets\]](#eq:center-phase-jets){reference-type="eqref" reference="eq:center-phase-jets"} proves the assertion at $T=3/16$ on the analytic persistent-circle family.

::: {#freq:classification-table}
      $T$        $h<h_-$: $\rho_-$     $h_-<h<h_+$: $\rho_0$    $h>h_+$: $\rho_+$
  ------------ ---------------------- ----------------------- ----------------------
   $0<T<3/16$        $\uparrow$        $\uparrow\downarrow$         $\uparrow$
    $T=3/16$         $\uparrow$            $\downarrow$             $\uparrow$
   $3/16<T<1$   $\uparrow\downarrow$       $\downarrow$             $\uparrow$
     $T=1$          $\downarrow$           $\downarrow$             $\uparrow$
     $T>1$          $\downarrow$           $\downarrow$        $\uparrow\downarrow$

  : Strict frequency classification on the three regular energy intervals. The lower and middle lifts describe $F_T$; the upper lift describes its first circle return $F_T^2$. An arrow denotes an everywhere strict derivative sign, and $\uparrow\downarrow$ denotes exactly one nondegenerate maximum. The persistent stationary circle at $T=3/16$, $h_-=-2$, lies outside these open intervals.
:::

For the phase $\sigma$ of $F_T^2$, the lower and middle derivatives are multiplied by two, while the upper phase is already $\rho_+$. Consequently $\sigma''<0$ at every stationary circle. In the five parameter rows the stationary-circle set $\mathcal S_T$ consists, respectively, of one middle circle, the persistent circle at $h_-$, two lower circles at the same energy, no circle, and two upper circles at the same energy. These are exactly the circles in the stationary-phase sum of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The shrinking circle at $T=3/16$ instead supplies the endpoint jet in [\[eq:center-phase-jets\]](#eq:center-phase-jets){reference-type="eqref" reference="eq:center-phase-jets"}; it must not be identified with the persistent circle on that energy level.

# Hyperbolic fibre estimates {#sec:hyperbolic}

The saddle contribution decays faster than every prescribed inverse power of time on a fixed energy neighbourhood. The required estimates must be proved for the original observables: their circlewise means need not be Hölder continuous at the saddle. Throughout this section set $e=h-h_+$ and $\ell(e)=1+\log(1/|e|)$, with $0<|e|<\delta<1$. All original-coordinate norms are taken on the fixed saturated band $K=h^{-1}([h_+-2\delta,h_++2\delta])$, in a finite original atlas. This band is compact by Lemma [\[lem:coarea-projection\]](#lem:coarea-projection){reference-type="ref" reference="lem:coarea-projection"}.

## The original passage time

At the critical point $s_w=(w^2,w)$ of [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}, the Hessian computed in Proposition [\[prop:real-geometry\]](#prop:real-geometry){reference-type="ref" reference="prop:real-geometry"} determines the Hamiltonian linearization. Direct differentiation of $F_T$ then gives $$\label{hyp:linearization}
\begin{gathered}
 A_w:=DF_T(s_w)=
 \begin{pmatrix}-w/(w-1)&w/(w-1)\\1/w&-1\end{pmatrix},
 \qquad
 DX(s_w)=\begin{pmatrix}w&-2w^2\\-2(w-1)&-w\end{pmatrix},\\
 A_w=\frac{\operatorname{tr}A_w}{2}I-
       \frac{DX(s_w)}{2w(w-1)}.
\end{gathered}$$ Here $\iota_X\Omega=-\,\mathrm{d}h$. For $w=w_+>1$ put $$\kappa=w_+\sqrt{4w_+-3},\qquad
 \mathfrak a=\operatorname{arcosh}
       \frac{2w_+-1}{2(w_+-1)}>0.$$ The eigenvalues of $DX(s_+)$ are $\pm\kappa$, and those of $A_{w_+}$ on the unstable and stable directions are respectively $-e^{\mathfrak a}$ and $-e^{-\mathfrak a}$. Thus $F_T$ reverses the half-branches of both axes, whereas $G_T=F_T^2$ preserves them.

[\[lem:hyperbolic-period\]]{#lem:hyperbolic-period label="lem:hyperbolic-period"} For each one-sided family of circles approaching $h_+$, $$\label{hyp:period}
 L(e)=A(e)\log(1/|e|)+B(e),\qquad
 A(0)=\frac{m_c}{\kappa},\qquad
 m_c=\begin{cases}1,&e>0,\\2,&e<0.\end{cases}$$ The functions $A$ and $B$ extend analytically to zero on the chosen side. More precisely, $A=m_c\mathcal A$ for one two-sided analytic function $\mathcal A$ with $\mathcal A(0)=1/\kappa$. The two upper circles have equal periods. In particular, $L=m_c\kappa^{-1}\log(1/|e|)+O(1)$ and $L'=-m_c/(\kappa e)+O(\ell)$.

The analytic Morse lemma and the orientation in [\[hyp:linearization\]](#hyp:linearization){reference-type="eqref" reference="hyp:linearization"} give local coordinates $$\label{hyp:morse}
 e=pq,\qquad \Omega=-a_0(p,q)\,\,\mathrm{d}p\wedge\,\mathrm{d}q,\qquad
 X=\frac{p\partial_p-q\partial_q}{a_0(p,q)},\qquad
 a_0(0,0)=\kappa^{-1}>0.$$ The density $a_0$ is positive on the chart. Along a regular fibre $\,\mathrm{d}t=a_0(p,e/p)\,\mathrm{d}p/p$, with $\Omega=\,\mathrm{d}e\wedge\,\mathrm{d}t$. Choose a fixed small box $|p|,|q|\le d_0$. A positive passage through it has time $$L_{\rm box}(e)=\int_{|e|/d_0}^{d_0}
     a_0(\epsilon_p s,\epsilon_p e/s)\frac{\,\mathrm{d}s}{s},
 \qquad \epsilon_p\in\{1,-1\}.$$ To retain differentiable remainders, expand the analytic density in its convergent power series $\sum_{j,k\ge0}a_{jk}p^jq^k$. The diagonal terms integrate to $a_{jj}e^j\log(d_0^2/|e|)$; each off-diagonal term gives a function analytic up to zero on either fixed side. Take the box strictly inside the convergence domain. The geometric majorant then controls the integrated series and each prescribed finite number of derivatives. Consequently $L_{\rm box}=\mathcal A(e)\log(1/|e|)+B_{\epsilon_p,\pm}(e)$ with the asserted analytic functions.

Outside the box, the limiting separatrix arcs are compact and regular. Analytic flow boxes and transverse entry and exit sections give analytic travel times along these arcs. The normalization of the split nodal fibre is a real projective circle with two real preimages of the node. Removing those preimages leaves two regular arcs. The smoothing in Proposition [\[prop:real-geometry\]](#prop:real-geometry){reference-type="ref" reference="prop:real-geometry"} joins them into two circles above $h_+$, each with one box passage, and into one circle below $h_+$, with two passages. Summing these times proves [\[hyp:period\]](#hyp:period){reference-type="eqref" reference="hyp:period"} and its derivative formula. Finally, $F_T$ exchanges the upper circles and preserves $X$, hence preserves their positive periods.

[\[lem:original-time\]]{#lem:original-time label="lem:original-time"} There is one two-sided real analytic function $\tau(e)$ such that, on every nearby complete regular circle $\Gamma_e$, $$\label{hyp:original-time}
 G_T|_{\Gamma_e}=\phi_X^{\tau(e)}|_{\Gamma_e},\qquad
 \tau(0)=\frac{2\mathfrak a}{\kappa}>0.$$ In particular the bounded lift $\alpha(e)=\tau(e)/L(e)$ satisfies $\alpha(e)=2\mathfrak a/(m_c\log(1/|e|))+O(\ell^{-2})$.

Symplecticity and energy preservation imply $(F_T)_*X=X$. On a sufficiently small fixed section $p=p_0>0$ write $z_e=(p_0,e/p_0)$ and $G_Tz_e=(p_1(e),e/p_1(e))$, where $p_1$ is positive and analytic near zero. For small $p_0$, both points and their connecting orbit remain in the Morse chart. Define $$\tau(e)=\int_{p_0}^{p_1(e)}a_0(s,e/s)\frac{\,\mathrm{d}s}{s}.$$ Since $s$ stays bounded away from zero, this integral is two-sided analytic. The return identity holds at $z_e$, and commutation with the flow extends it to an open flow box. On a connected sufficiently small neighbourhood containing the saddle and this flow box, both $G_T$ and $z\mapsto\phi_X^{\tau(h(z)-h_+)}z$ are analytic; bounded-time local flow existence follows after shrinking the neighbourhood. The analytic identity theorem extends their equality across all local quadrants. Every neighbouring complete circle meets this neighbourhood, and its nonvanishing Hamiltonian flow is transitive. Commutation therefore extends the same identity to each entire circle.

Differentiating at the saddle in the unstable direction gives $e^{\kappa\tau(0)}=e^{2\mathfrak a}$, which determines the stated positive value. No nonzero integer multiple of the diverging complete period can be added while retaining a bounded analytic time lift. The formula for $\alpha$ follows from [\[hyp:period\]](#hyp:period){reference-type="eqref" reference="hyp:period"}.

Near the saddle the phase of $G_T$ is $\sigma=1+\alpha$ below $h_+$ and $\sigma=\alpha$ above it. Both its derivatives and its integer-time Fourier exponential can therefore be computed with $\alpha$. Above $h_+$ this is a two-step return phase; the original single step still exchanges the two circles. Lemma [\[lem:original-time\]](#lem:original-time){reference-type="ref" reference="lem:original-time"} identifies an energy-dependent local time of the original map, not a global constant-time Hamiltonian representation.

## Why original regularity must be retained

For an original smooth observable put $c=f(s_+)$ and $b=f-c$. In the box $|b|\le C\|f\|_{C^1}(|p|+|q|)$, and $$\int_{|e|/d_0}^{d_0}
       \left(s+\frac{|e|}{s}\right)\frac{\,\mathrm{d}s}{s}=O(1).$$ The exterior times are uniformly bounded. Thus, for every fixed $q_1\ge1$, $\int_{\Gamma_e}|b|^{q_1}\,\mathrm{d}t$ is bounded in terms of an original finite norm. Writing $B_f(e)=\int_{\Gamma_e}b\,\,\mathrm{d}t$ gives $$\label{hyp:mean}
 \Pi f=c+\frac{B_f(e)}{L(e)}=c+O(L^{-1}),\qquad
 \int_{\Gamma_e}|f-\Pi f|^2\,\mathrm{d}t
  =\int_{\Gamma_e}|b|^2\,\mathrm{d}t-\frac{|B_f(e)|^2}{L(e)}=O(1).$$ The centered $L^1(\,\mathrm{d}t)$ norm is bounded as well. Consequently, for all $k\ne0$ and integers $j\ge1$, $$\label{hyp:two-fourier-bounds}
 |\widehat f_k(e)|\le\frac{C\|f\|_{C^1}}{L(e)},\qquad
 |\widehat f_k(e)|\le
 C_j\|f\|_{C^j}L(e)^{j-1}|k|^{-j}.$$ The first bound follows by integrating $b$ in Hamiltonian time. For the second, the differential operator $X^j$ has coefficients vanishing at least linearly at the saddle, so $X^jf$ has the same bounded $L^1(\,\mathrm{d}t)$ estimate. Integration by parts on the time circle gives the second inequality, including its uniformity in $k$.

For any $s\ge0$, split the sums at $|k|=L$ and use an integer $j>s+1$ in [\[hyp:two-fourier-bounds\]](#hyp:two-fourier-bounds){reference-type="eqref" reference="hyp:two-fourier-bounds"}. This yields $$\sum_{k\ne0}|k|^s|\widehat f_k|\le C_{f,s}L^s,
 \qquad
 \sum_{k\ne0}|k|^{2s}|\widehat f_k|^2\le C_{f,s}L^{2s-1}.$$ In particular the unweighted Wiener norm remains bounded, although weighted angular norms can grow. A nonzero bump supported near a regular point of a separatrix gives, for each $j\ge1$, $\|\partial_\theta^j f\|_{L^2(\,\mathrm{d}\theta)}^2
 =L^{2j-1}\int_{\Gamma_e}|X^jf|^2\,\mathrm{d}t\asymp L^{2j-1}$: the limiting time derivative cannot vanish identically for a nonzero compactly supported bump along that arc.

The same example makes the projection loss explicit. Choose the bump nonnegative, supported away from $s_+$, and nonzero on a regular separatrix arc approached by one upper circle. Its time integral tends to $B_f(0)>0$, since its support lies in regular flow boxes. Hence $\Pi f\sim\kappa B_f(0)/\log(1/e)$ on that circle. Along its saddle quadrant take $(p,q)=(s,s)$ or $(-s,-s)$, $s\downarrow0$. Here $f=0$ and $e=s^2$, so $|f-\Pi f|\asymp1/\log(1/s)$. Assigning the value zero at $s_+$ gives the limiting value, but no positive Hölder exponent is possible. All derivatives below are therefore taken on $f$ and $g$ themselves; centering only removes their zero Fourier modes.

## Mixed symbols on the full circle

[\[prop:mixed-symbols\]]{#prop:mixed-symbols label="prop:mixed-symbols"} On each one-sided complete circle family there is a fixed analytic regular section $z_0(e)$, extending to $e=0$, for which the positive time angle $z(e,\theta)=\phi_X^{\theta L(e)}z_0(e)$ obeys $$\begin{aligned}
 \sup_{\theta\in\mathbb{R}/\mathbb{Z}}
 |\partial_e^a\partial_\theta^b(f\circ z)(e,\theta)|
 &\le C_{a,b}\|f\|_{C^{a+b}(K)}
            |e|^{-a}\ell^{a+b},\label{eq:hyp-mixed-est}\\
 |\partial_e^a\widehat f_k(e)|
 &\le C_{a,s}\|f\|_{C^{a+s}(K)}
            |e|^{-a}\ell^{a+s}|k|^{-s},\quad k\ne0.
            \label{eq:hyp-fourier-est}\end{aligned}$$ These statements hold for every pair of nonnegative integer orders, with the indicated finite original regularity. Their constants are independent of $e,\theta,k,f$ but may depend on the chosen sections, the compact window, $T$, and the orders.

Choose $z_0(e)$ on a fixed transverse section through a regular point of the limiting separatrix; the analytic implicit function theorem supplies its extension to zero. For each nonzero $e$ the time angle is smooth and periodic. To estimate it, enlarge the Morse box to $|p|,|q|\le d_1$, with $d_1>d_0$, still inside the analytic chart and with $a_0\ge c_*>0$. The box passages and finitely many exterior arcs give a fixed itinerary on each side. Let $c_j(e)$ be the accumulated time from the base section to the start of a segment. Analytic exterior times and [\[hyp:period\]](#hyp:period){reference-type="eqref" reference="hyp:period"}, applied to each passage, imply $$\label{hyp:euler-times}
 |D^i L(e)|+|D^i c_j(e)|\le C_i\ell(e),\qquad
 D=e\partial_e,\quad i\ge0.$$ Here $D$ acts at fixed normalized angle when applied to a composed orbit coordinate.

For a box passage use the logarithmic variable $u_\ell=\log|p|$: $$p=\epsilon_p e^{u_\ell},\quad
 q=\epsilon_p e e^{-u_\ell},\quad
 u_0(e)=\log|e|-\log d_0,\quad u_1=\log d_0.$$ Set $H_{\rm box}(e,u_\ell)=a_0(\epsilon_p e^{u_\ell},\epsilon_p e e^{-u_\ell})$. The fixed-$u_\ell$ Euler derivative and the logarithmic coordinate derivative act on original-coordinate functions as $$D_0:=e\partial_e|_{u_\ell}=q\partial_q,\qquad
 \partial_{u_\ell}=p\partial_p-q\partial_q.$$ They commute and have bounded coefficients and derivatives on the larger box. Thus $|D_0^i\partial_{u_\ell}^jH_{\rm box}|\le C_{i,j}$ and $H_{\rm box}\ge c_*$ there, for all finite orders.

The passage time $I(e,u_\ell)=\int_{u_0(e)}^{u_\ell}H_{\rm box}(e,v)\,\mathrm{d}v$ has interval length $O(\ell)$. Its higher energy derivatives must include the moving entry. Put $\mathcal E_0=D_0+\partial_{u_\ell}=p\partial_p$ and $\mathcal R_0B=B(e,u_0(e))$. Since $Du_0=1$, $D\mathcal R_0B=\mathcal R_0\mathcal E_0B$, and repeated Leibniz differentiation gives the exact formula $$\label{hyp:moving-entry}
 D_0^i I(e,u_\ell)=\int_{u_0(e)}^{u_\ell}D_0^iH_{\rm box}(e,v)\,\mathrm{d}v
 -\mathcal R_0\!\left(
     \sum_{j=0}^{i-1}\mathcal E_0^{\,i-1-j}D_0^jH_{\rm box}\right),
 \qquad i\ge1.$$ Every entry term is bounded. If at least one $u_\ell$ derivative is taken, the integral is replaced by derivatives of $H_{\rm box}$. For $S(e,u_\ell)=c_j(e)+I(e,u_\ell)$ we obtain $$\label{hyp:time-symbols}
 |D_0^iS|\le C_i\ell,\qquad
 |D_0^i\partial_{u_\ell}^jS|\le C_{i,j}\quad(j\ge1),\qquad S_{u_\ell}\ge c_*.$$

On a local angle lift $\vartheta=\theta+\nu$, with a fixed integer $\nu$ and $|\vartheta|\le2$, the current point solves $S(e,u_\ell(e,\theta))=\vartheta L(e)$. The first derivatives are $$Du_\ell=\frac{\vartheta DL-D_0S}{S_{u_\ell}},\qquad
 \partial_\theta u_\ell=\frac{L}{S_{u_\ell}}.$$ Both are $O(\ell)$. Induct on $n=a+b\ge1$ to obtain $|D^a\partial_\theta^b u_\ell|\le C_{a,b}\ell^{a+b}$. Indeed, differentiating the time equation leaves the unique top-order unknown $S_{u_\ell}D^a\partial_\theta^bu_\ell$. A remaining term without derivatives of $u_\ell$ is a pure $D_0$ derivative of $S$, hence $O(\ell)$. Every other term has a coefficient containing a positive $u_\ell$ derivative of $S$, bounded by [\[hyp:time-symbols\]](#hyp:time-symbols){reference-type="eqref" reference="hyp:time-symbols"}, and a product of lower-order jets of $u_\ell$ of total order at most $n$. The inductive bound makes that product $O(\ell^n)$. The right side is $O(\ell)$ by [\[hyp:euler-times\]](#hyp:euler-times){reference-type="eqref" reference="hyp:euler-times"}, or zero for two or more angle derivatives. Division by $S_{u_\ell}\ge c_*$ completes the induction.

Restoring the original coordinates does not introduce any division by $p$ or $q$: $$Dp=pDu_\ell,\quad \partial_\theta p=p\partial_\theta u_\ell,\qquad
 Dq=q(1-Du_\ell),\quad \partial_\theta q=-q\partial_\theta u_\ell.$$ Every further mixed derivative retains a factor $p$ or $q$ times a polynomial in the jets of $u_\ell$, of total differential order no larger than the order being estimated. Since $|p|,|q|\le d_1$, the chain rule gives $|D^a\partial_\theta^b(f\circ z)|
 \le C_{a,b}\ell^{a+b}\|f\|_{C^{a+b}(K)}$ throughout each box passage.

The exterior arcs require bounded-time, not long-time, flow estimates. Their regular limiting arcs are compact. Starting at an entry section gives analytic maps $Z_j(e,t)$ for a uniformly bounded time interval, slightly extended at both ends, with bounded finite derivatives. There the same point is $$z(e,\theta)=Z_j(e,t(e,\theta)),\qquad
 t(e,\theta)=\vartheta L(e)-c_j(e).$$ The time $t$ stays bounded; all its positive-order mixed $D,\partial_\theta$ derivatives are $O(\ell)$ by [\[hyp:euler-times\]](#hyp:euler-times){reference-type="eqref" reference="hyp:euler-times"}. The chain rule therefore gives the same $O(\ell^{a+b})$ estimate on every exterior arc, including arcs through terminal charts by Lemma [\[lem:regular-norms\]](#lem:regular-norms){reference-type="ref" reference="lem:regular-norms"}.

These segment descriptions estimate one smooth map, without multiplying by moving characteristic functions. Extend the box coordinates into fixed physical strips between the small and large boxes, and extend the neighbouring exterior flow maps for a fixed short time. Their expressions agree on open overlaps at every entry and exit. The bounds in [\[hyp:moving-entry\]](#hyp:moving-entry){reference-type="eqref" reference="hyp:moving-entry"}--[\[hyp:time-symbols\]](#hyp:time-symbols){reference-type="eqref" reference="hyp:time-symbols"} persist on these strips; an extension before entry only adds a bounded-length reverse integral. The overlap's angular width may be $O(L^{-1})$, but no inverse width is used in a pointwise derivative estimate. Equality on the open overlaps identifies all actual derivatives at the seams. The periodic seam lies at the regular base section. A flow box there uses the time $\theta L$ on one side and $(\theta-1)L$ on the other, with both positive and negative short times allowed. The identity $\phi_X^{L(e)}z_0(e)=z_0(e)$ identifies those expressions in the local circle coordinate, with all derivatives. This proves the Euler estimate on the full circle, not only inside the Morse box.

Finally, $e^a\partial_e^a=D(D-1)\cdots(D-a+1)$ for $a\ge1$. Since $D$ commutes with $\partial_\theta$, this exact identity and $\ell\ge1$ prove [\[eq:hyp-mixed-est\]](#eq:hyp-mixed-est){reference-type="eqref" reference="eq:hyp-mixed-est"}. At each $e\ne0$, differentiation of the compact angle integral and $s$ integrations by parts give $$\partial_e^a\widehat f_k(e)=(2\pi\mathrm{i}k)^{-s}
 \int_0^1\partial_e^a\partial_\theta^s(f\circ z)(e,\theta)
                      e^{-2\pi\mathrm{i}k\theta}\,\mathrm{d}\theta.$$ The periodic boundary terms vanish. Substitution of [\[eq:hyp-mixed-est\]](#eq:hyp-mixed-est){reference-type="eqref" reference="eq:hyp-mixed-est"} proves [\[eq:hyp-fourier-est\]](#eq:hyp-fourier-est){reference-type="eqref" reference="eq:hyp-fourier-est"} uniformly over the entire nonzero Fourier family.

The section-based choice of angle is part of the proposition. An arbitrary energy-dependent rotation of the angle need not obey its derivative bounds. A common change of angle multiplies the two Fourier factors in a correlation amplitude by conjugate phases, so that their product is unchanged.

## The inverse phase derivative and actual boundary terms

[\[lem:inverse-phase\]]{#lem:inverse-phase label="lem:inverse-phase"} For the same complete period and the same analytic time lift, $\alpha'= (\tau/L)'$ is nonzero on each sufficiently small punctured side, and $Q_{\rm inv}=1/\alpha'$ satisfies $$\label{hyp:inverse-estimate}
 |\partial_e^aQ_{\rm inv}(e)|\le
       C_a|e|^{1-a}\ell(e)^2,\qquad a\ge0.$$

Writing $l=\log(1/|e|)$, use $L=Al+B$ from Lemma [\[lem:hyperbolic-period\]](#lem:hyperbolic-period){reference-type="ref" reference="lem:hyperbolic-period"} to compute $$\begin{aligned}
 R_{\rm hyp}:=(D\tau)L-\tau DL
 &=\tau A+e(\tau'A-\tau A')l
                 +e(\tau'B-\tau B'),\label{hyp:inverse-R}\\
 \alpha'&=\frac{R_{\rm hyp}}{eL^2},\qquad
 Q_{\rm inv}=\frac{eL^2}{R_{\rm hyp}}.\label{hyp:inverse-exact}\end{aligned}$$ Thus $R_{\rm hyp}\to\tau(0)A(0)>0$ and, after shrinking $\delta$, it is bounded below by a positive constant. Each finite Euler derivative of $e$ times an analytic function times $l$ remains of that form. Hence $D^jR_{\rm hyp}$ is bounded for every $j$. Differentiating $R_{\rm hyp}R_{\rm hyp}^{-1}=1$ inductively bounds all $D^j(R_{\rm hyp}^{-1})$, while [\[hyp:euler-times\]](#hyp:euler-times){reference-type="eqref" reference="hyp:euler-times"} bounds $D^j(L^2)$ by $C_j\ell^2$. Consequently, with $V=L^2/R_{\rm hyp}$, every $D^jV$ is $O(\ell^2)$. For $a\ge1$ the exact identity $$\partial_e^a(eV)=e^{1-a}
          \prod_{j=0}^{a-1}(D+1-j)V$$ proves [\[hyp:inverse-estimate\]](#hyp:inverse-estimate){reference-type="eqref" reference="hyp:inverse-estimate"}; $a=0$ follows directly from [\[hyp:inverse-exact\]](#hyp:inverse-exact){reference-type="eqref" reference="hyp:inverse-exact"}. That equation also shows that the sign of $\alpha'$ is the sign of $e$.

[\[prop:hyperbolic-decay\]]{#prop:hyperbolic-decay label="prop:hyperbolic-decay"} Let $\chi\in C_c^\infty((-\delta,\delta))$ be fixed, with $\delta$ as above. In particular, $\chi$ may equal one near zero. For every prescribed integer $N\ge1$, $m\ge1$, $r\in\{0,1\}$, and original $f,g\in C_c^\infty(U_T)$, $$\label{hyp:decay}
 \begin{aligned}
 &\left|\int_{U_T}\chi(h-h_+)
 ((I-\Pi)f)(F_T^{2m+r}z)
       \overline{((I-\Pi)g)(z)}\,\,\mathrm{d}\mu(z)\right|\\
 &\qquad\le C_{N,\chi}m^{-N}
          \|f\|_{C^{N+2}(K)}\|g\|_{C^{N+2}(K)}.
 \end{aligned}$$ The estimate includes both upper circles and the complete lower circle. The cutoff does not depend on $m$.

Put $f_r=f\circ F_T^r$. The commutation in Lemma [\[lem:coarea-projection\]](#lem:coarea-projection){reference-type="ref" reference="lem:coarea-projection"} moves the iterate past $\Pi$, and the original smooth automorphism gives $\|f_r\|_{C^j(K)}\le C_j\|f\|_{C^j(K)}$. On one side and one circle family the Fourier amplitudes are $$a_k(e)=\chi(e)L(e)\widehat{f_r}_k(e)
                           \overline{\widehat g_k(e)},\qquad k\ne0.$$ Coarea and circlewise Cauchy--Schwarz justify this Fourier expression: the sum of the absolute paired coefficients is bounded by the product of the two circle $L^2(\,\mathrm{d}\theta)$ norms, and $L=O(\ell)$ is integrable in energy. Centering deletes precisely $k=0$. The integer offset between $\sigma$ and $\alpha$ contributes no factor to $e^{2\pi\mathrm{i}km\sigma}$.

Leibniz differentiation of the analytic logarithmic period and [\[eq:hyp-fourier-est\]](#eq:hyp-fourier-est){reference-type="eqref" reference="eq:hyp-fourier-est"}, applied to both Fourier factors, gives for every finite $j,s$ $$\label{hyp:amplitude-class}
 |\partial_e^j a_k(e)|\le
 C_{j,s,\chi}\|f\|_{C^{j+s}(K)}\|g\|_{C^{j+s}(K)}
       |e|^{-j}\ell^{M_{j,s}}|k|^{-2s},$$ where $M_{j,s}$ is a finite nonnegative exponent. Define the transpose operator $\mathcal T a=-\partial_e(Q_{\rm inv}a)$, independent of $k$ and $m$. For every $j$, $$\partial_e^j\mathcal T a
 =-\sum_{v=0}^{j+1}\binom{j+1}{v}
     (\partial_e^vQ_{\rm inv})(\partial_e^{j+1-v}a).$$ Each summand has energy power $|e|^{1-v}|e|^{-(j+1-v)}=|e|^{-j}$. Thus [\[hyp:inverse-estimate\]](#hyp:inverse-estimate){reference-type="eqref" reference="hyp:inverse-estimate"} preserves the class [\[hyp:amplitude-class\]](#hyp:amplitude-class){reference-type="eqref" reference="hyp:amplitude-class"} under $\mathcal T$, increasing only the finite logarithmic exponents and derivative requirements. Induction gives an integrable bound for $\mathcal T^Na_k$ by $C|k|^{-2s}\ell^{M_N}$, and, at the actual nodal boundary, $$\label{hyp:vanishing-boundary}
 Q_{\rm inv}\mathcal T^ja_k
      =O\bigl(|k|^{-2s}|e|\ell^{M_j}\bigr)\longrightarrow0.$$ At the outer boundary the cutoff and all its derivatives vanish.

First integrate by parts $N$ times on a closed interval truncated away from $e=0$. Then let that truncation tend to zero. Equation [\[hyp:vanishing-boundary\]](#hyp:vanishing-boundary){reference-type="eqref" reference="hyp:vanishing-boundary"} eliminates every boundary term, and the integrable logarithmic bound permits passage to the limit. On either side, with increasing energy as the integration orientation, the resulting identity is $$\label{hyp:transpose-identity}
 \int a_k(e)e^{2\pi\mathrm{i}km\alpha(e)}\,\mathrm{d}e
 =(2\pi\mathrm{i}km)^{-N}
     \int\mathcal T^Na_k(e)e^{2\pi\mathrm{i}km\alpha(e)}\,\mathrm{d}e.$$ For $s=1$, the absolute sum is bounded by $$C_Nm^{-N}\|f\|_{C^{N+2}(K)}\|g\|_{C^{N+2}(K)}
 \sum_{k\ne0}|k|^{-N-2}\int_0^\delta\ell(e)^{M_N}\,\mathrm{d}e<\infty.$$ The calculation uses at most $N$ energy derivatives and one angular derivative on each observable; in particular the stated original $C^{N+2}$ norms suffice, including the fixed charts and the pullback by $F_T^r$. Summing over the two upper circles and the one lower circle proves [\[hyp:decay\]](#hyp:decay){reference-type="eqref" reference="hyp:decay"}.

The vanishing boundary factor in this argument is $Q_{\rm inv}\mathcal T^ja_k$, not necessarily $\mathcal T^ja_k$, which may grow logarithmically. The full nodal neighbourhood remains fixed throughout. For each chosen $N$ the proof uses a finite original norm; it does not assert that a fixed $C^{20}$ norm controls all orders.

# Elliptic jets and endpoint asymptotics {#sec:elliptic}

The circle shrinking to the elliptic centre requires a different estimate from the hyperbolic circles. Its period stays finite, but smoothness in the original surface forces the nonzero Fourier amplitudes to vanish. We construct a time angle in which this vanishing has a smooth expansion in $\varepsilon=h_--h$. Throughout this section only the shrinking circle is integrated; the persistent circle at the same limiting energy is disjoint from the local domain.

## A positive symmetric time angle

Write $s_-=s_{w_-}$ and $\omega_-=|w_-|\sqrt{3-4w_-}$. The negative-definite Hessian at $s_-$ and the analytic Morse lemma give a real analytic chart $\mathcal K$ with $$\label{ell:morse-chart}
 h\circ\mathcal K(p,q)=h_--\frac{p^2+q^2}{2},\qquad
 \mathcal K^*\Omega=-b(p,q)\,\,\mathrm{d}p\wedge\,\mathrm{d}q,
 \quad b>0,\quad b(0,0)=\omega_-^{-1}.$$ If necessary, reflecting $q$ gives the stated orientation without changing the energy. The value of $b(0,0)$ follows from the linear Hamiltonian frequency. For $p=\varrho\cos\varphi$ and $q=\varrho\sin\varphi$, our convention $\iota_X\Omega=-\,\mathrm{d}h$ gives $X=b^{-1}\partial_\varphi$ and $\,\mathrm{d}t=b\,\,\mathrm{d}\varphi$. Thus increasing $\varphi$, not its negative, is the positive time direction, and $L_0=2\pi/\omega_-$.

Choose a sufficiently small $\varepsilon_0>0$ and put $\varrho_0=\sqrt{2\varepsilon_0}$. For the construction alone, allow $-\varrho_0\leq\varrho\leq\varrho_0$; negative radius does not label an additional physical circle. Set $$b_\varrho(\varphi)=b(\varrho\cos\varphi,\varrho\sin\varphi),\qquad
 \bar b(\varrho)=\frac1{2\pi}\int_0^{2\pi}b_\varrho(\varphi)\,\,\mathrm{d}\varphi,
 \qquad \widetilde L(\varrho)=2\pi\bar b(\varrho).$$ Let $B_\varrho$ be the unique zero-mean periodic primitive of $b_\varrho-\bar b(\varrho)$. It is real analytic in $(\varrho,\varphi)$: substitution into the convergent local power series of $b$ gives finite trigonometric polynomials in each homogeneous degree, and integration of their nonzero frequencies preserves normal convergence, with every fixed finite number of derivatives on a smaller cylinder. Define the lift $$\Psi_\varrho(\varphi)
   =\varphi+\frac{B_\varrho(\varphi)}{\bar b(\varrho)}.$$ Its derivative is $b_\varrho/\bar b>0$, and it commutes with translation by $2\pi$. The analytic inverse function theorem on a finite cover of the angle circle therefore gives an analytic inverse lift $\varphi_\varrho(\psi)$. The parametrization $$\label{ell:time-angle}
 z(\varrho,\theta)=\mathcal K\bigl(
 \varrho\cos\varphi_\varrho(2\pi\theta),
 \varrho\sin\varphi_\varrho(2\pi\theta)\bigr),\qquad \theta\in\mathbb{R}/\mathbb{Z},$$ is analytic on the full signed-radius cylinder. On the physical circle $\varrho=\sqrt{2\varepsilon}$ it satisfies $\,\mathrm{d}t=L(\varepsilon)\,\,\mathrm{d}\theta$ and $\,\mathrm{d}\mu=L(\varepsilon)\,\,\mathrm{d}\varepsilon\,\,\mathrm{d}\theta$, where $L(\varepsilon)=\widetilde L(\sqrt{2\varepsilon})>0$. Since $B_0=0$, $$\label{ell:angle-first-jet}
 z(0,\theta)=s_-,\qquad
 \partial_\varrho z(0,\theta)
   =D\mathcal K_0(\cos2\pi\theta,\sin2\pi\theta).$$

The zero-mean normalization fixes the symmetry needed below. Indeed, $b_{-\varrho}(\varphi)=b_\varrho(\varphi+\pi)$ implies $\bar b(-\varrho)=\bar b(\varrho)$ and, by uniqueness, $B_{-\varrho}(\varphi)=B_\varrho(\varphi+\pi)$. Hence $$\Psi_{-\varrho}(\varphi)=\Psi_\varrho(\varphi+\pi)-\pi,
 \qquad
 \varphi_{-\varrho}(\psi)=\varphi_\varrho(\psi+\pi)-\pi,$$ which proves the exact identity $$\label{ell:half-turn}
 z(-\varrho,\theta)=z(\varrho,\theta+1/2).$$ An arbitrary energy-dependent choice of angle origin would not by itself supply this identity.

## Ambient jets and summable remainders

All norms below are ordinary finite-order norms in a fixed, slightly larger compact Morse neighbourhood $K$. They are equivalent to the corresponding original-chart norms used in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. For $k\ne0$, write $$\widehat f_k(\varepsilon)=\int_0^1
 f(z(\sqrt{2\varepsilon},\theta))e^{-2\pi\mathrm{i}k\theta}\,\,\mathrm{d}\theta,
 \qquad a_k(\varepsilon)=L(\varepsilon)
 \widehat f_k(\varepsilon)\overline{\widehat g_k(\varepsilon)}.$$ These are the Fourier coefficients of the original functions; subtracting $\Pi$ removes only $k=0$ and requires no assertion about the original smoothness of $f-\Pi f$.

[\[prop:elliptic-jets\]]{#prop:elliptic-jets label="prop:elliptic-jets"} For original smooth $f,g$, the amplitudes have expansions $$\label{eq:jet-amplitudes}
 a_k(\varepsilon)=\varepsilon A_k+\varepsilon^2R_k(\varepsilon),
 \qquad
 A_k=2L_0d_{f,k}\overline{d_{g,k}},\qquad k\ne0,$$ where $R_k$ is smooth on the closed half-interval and $A_k=0$ for $|k|\ne1$. If $f\circ\mathcal K=f(s_-)+a_fp+b_fq+O(p^2+q^2)$, then $$\label{ell:first-mode-jets}
 d_{f,1}=\frac{a_f-\mathrm{i}b_f}{2},\qquad
 d_{f,-1}=\frac{a_f+\mathrm{i}b_f}{2},\qquad d_{f,k}=0\quad(|k|\ne1).$$ For all integers $J,S\geq0$, $$\label{eq:elliptic-remainder-norm}
 \sup_{k\ne0}(1+|k|)^S
 \|R_k\|_{C^J([0,\varepsilon_0])}
 \leq C_{J,S}
 \|f\|_{C^{2J+4+S}(K)}\|g\|_{C^{2J+4+S}(K)}.$$ The constants depend on the fixed parameter and chart, not on $k$.

Use the signed radius to define $f_k(\varrho)=\int_0^1f(z(\varrho,\theta))e^{-2\pi\mathrm{i}k\theta}\,\,\mathrm{d}\theta$. Equation [\[ell:half-turn\]](#ell:half-turn){reference-type="eqref" reference="ell:half-turn"} gives $$f_k(-\varrho)=(-1)^kf_k(\varrho),\qquad f_k(0)=0\quad(k\ne0).$$ The finite chain rule on the fixed cylinder and periodic integration by parts give, for all integers $u,S\geq0$, $$\label{ell:radial-fourier-norm}
 \|f_k\|_{C^u([-\varrho_0,\varrho_0])}
 \leq C_{u,S}(1+|k|)^{-S}\|f\|_{C^{u+S}(K)}.$$ For $S=0$ this follows directly from the integral; for $S>0$ move $S$ angle derivatives onto the composed function. As $\widetilde L$ is positive, even and analytic, $\widetilde a_k(\varrho)=\widetilde L(\varrho)
f_k(\varrho)\overline{g_k(\varrho)}$ is even and vanishes to order at least two at zero.

We use a finite-norm form of smooth even descent. If $v$ is even and $C^{2J}$, then $V(\varepsilon)=v(\sqrt{2\varepsilon})$ is $C^J$ up to zero, with norm bounded by a constant times $\|v\|_{C^{2J}}$. For the first derivative the identity $$\label{ell:even-descent}
 \frac1\varrho v'(\varrho)=\int_0^1v''(t\varrho)\,\,\mathrm{d}t$$ follows from $v'(0)=0$. Repeated application of $\varrho^{-1}\partial_\varrho$ expresses its $j$th iterate as multiple integrals of $v^{(2j)}$ with bounded weights: at each step the next odd derivative vanishes at zero and the same identity applies again. These integrals extend continuously to zero. Since $\partial_\varepsilon=\varrho^{-1}\partial_\varrho$, they prove the claim and its norm bound for $0\leq j\leq J$.

Let $d_{f,k}=f_k'(0)$. Subtracting the quadratic Taylor coefficient from $\widetilde a_k$ leaves an even function vanishing to order four. The integral remainder formula therefore yields $$\widetilde a_k(\varrho)
 =\varrho^2L_0d_{f,k}\overline{d_{g,k}}
      +\varrho^4q_k(\varrho),\qquad
 \|q_k\|_{C^{2J}}
 \leq C_J\|\widetilde a_k\|_{C^{2J+4}},$$ where $q_k$ is smooth and even. In particular, the apparent division by $\varrho^4$ is justified at zero by the fourth-order integral remainder, not merely by formal parity. Applying [\[ell:even-descent\]](#ell:even-descent){reference-type="eqref" reference="ell:even-descent"} to $q_k$ gives [\[eq:jet-amplitudes\]](#eq:jet-amplitudes){reference-type="eqref" reference="eq:jet-amplitudes"} with $R_k(\varepsilon)=4q_k(\sqrt{2\varepsilon})$. The product rule and [\[ell:radial-fourier-norm\]](#ell:radial-fourier-norm){reference-type="eqref" reference="ell:radial-fourier-norm"} prove [\[eq:elliptic-remainder-norm\]](#eq:elliptic-remainder-norm){reference-type="eqref" reference="eq:elliptic-remainder-norm"}; $S$ angle derivatives on one Fourier factor suffice for the stated weight, so $2J+4+S$ original derivatives on each function are sufficient. Finally, [\[ell:angle-first-jet\]](#ell:angle-first-jet){reference-type="eqref" reference="ell:angle-first-jet"} gives [\[ell:first-mode-jets\]](#ell:first-mode-jets){reference-type="eqref" reference="ell:first-mode-jets"} and $d_{f,k}=0$ for $|k|\ne1$.

The two possible leading coefficients are consequently $$A_1=\frac{L_0}{2}(a_f-\mathrm{i}b_f)
                  (\overline{a_g}+\mathrm{i}\overline{b_g}),\qquad
 A_{-1}=\frac{L_0}{2}(a_f+\mathrm{i}b_f)
                  (\overline{a_g}-\mathrm{i}\overline{b_g}).$$ They determine only the first energy coefficient. All higher modes and the higher-order parts of the two first modes remain in $R_k$. Replacing $f$ by $f_r=f\circ F_T^r$ gives the coefficients $A_k^{(r)}$ in [\[eq:center-coefficients\]](#eq:center-coefficients){reference-type="eqref" reference="eq:center-coefficients"}; the original parity relation is treated together with the other circles in Section [7](#sec:global){reference-type="ref" reference="sec:global"}.

## The nonstationary endpoint

Let $\chi\in C_c^\infty([0,\varepsilon_0))$ equal one near zero; this means smoothness on the closed half-axis and vanishing before the right endpoint. With $\Gamma_\varepsilon$ the shrinking circle, define $$\begin{aligned}
 \mathcal E_m(f,g)
 &=\int_0^{\varepsilon_0}\chi(\varepsilon)
   \int_{\Gamma_\varepsilon}
   ((I-\Pi)f)(G_T^mz)\,
   \overline{((I-\Pi)g)(z)}\,\,\mathrm{d}t\,\,\mathrm{d}\varepsilon
   \notag\\
 &=\sum_{k\ne0}\int_0^{\varepsilon_0}
   \chi(\varepsilon)a_k(\varepsilon)
   e^{2\pi\mathrm{i}km\sigma_E(\varepsilon)}\,\,\mathrm{d}\varepsilon,
 \qquad m\geq1.\label{ell:fourier-integral}\end{aligned}$$ The first equality uses positive time and the measure in Lemma [\[lem:coarea-projection\]](#lem:coarea-projection){reference-type="ref" reference="lem:coarea-projection"}. For the second, $G_T$ translates this angle by $\sigma_E(\varepsilon)=2\rho_-(h_--\varepsilon)$. Proposition [\[prop:elliptic-jets\]](#prop:elliptic-jets){reference-type="ref" reference="prop:elliptic-jets"} with $J=0,S=2$ gives an integrable absolute majorant for the entire sum, justifying the Fourier identity and Fubini without a finite-mode truncation. Put $\sigma_c=\sigma_E(0)=2\theta_T$. The centre phase jets [\[eq:center-phase-jets\]](#eq:center-phase-jets){reference-type="eqref" reference="eq:center-phase-jets"} give $\beta=\sigma_E'(0)=-2\rho_-'(h_-)$, which is nonzero unless $T=3/16$; at that parameter $\gamma=\sigma_E''(0)=2\rho_-''(h_-)<0$.

[\[prop:elliptic-endpoints\]]{#prop:elliptic-endpoints label="prop:elliptic-endpoints"} For a sufficiently small fixed cutoff, if $T\ne3/16$ then $$\label{ell:ordinary-endpoint}
 \mathcal E_m(f,g)
 =-\frac1{m^2}\sum_{k=\pm1}
   \frac{A_ke^{2\pi\mathrm{i}km\sigma_c}}{(2\pi k\beta)^2}
   +O\bigl(m^{-3}\|f\|_{C^{20}(K)}\|g\|_{C^{20}(K)}\bigr).$$ If $T=3/16$, then $$\label{ell:quadratic-endpoint}
 \mathcal E_m(f,g)
 =\frac1m\sum_{k=\pm1}
   \frac{\mathrm{i}A_ke^{2\pi\mathrm{i}km\sigma_c}}{2\pi k\gamma}
   +O\bigl(m^{-3/2}\|f\|_{C^{20}(K)}\|g\|_{C^{20}(K)}\bigr).$$ The constants may depend on $T,K,\chi$. Both remainders include all nonzero Fourier modes.

Shrink the cutoff so that $\sigma_E'$ has no zero on its whole support. Set $s_\beta=\mathop{\mathrm{sgn}}\beta$ and $x=s_\beta(\sigma_E(\varepsilon)-\sigma_c)$. This is an increasing analytic coordinate with inverse $\varepsilon=E(x)$, $E(0)=0$ and $E'(0)=|\beta|^{-1}$. The transformed amplitude $$b_k(x)=\chi(E(x))a_k(E(x))E'(x)$$ is smooth and compactly supported on the closed half-axis, with $b_k(0)=0$ and $b_k'(0)=A_k/\beta^2$. For every real $\omega\ne0$, three integrations by parts give $$\label{ell:three-ibp}
 \int_0^\infty b_k(x)e^{\mathrm{i}\omega x}\,\,\mathrm{d}x
 =-\frac{b_k'(0)}{\omega^2}+E_k(\omega),\qquad
 |E_k(\omega)|\leq
 \frac{|b_k''(0)|+\|b_k'''\|_{L^1}}{|\omega|^3}.$$ All right-end boundary terms vanish by compact support. The fixed coordinate change gives $$|b_k''(0)|+\|b_k'''\|_{L^1}
 \leq C\bigl(|A_k|+\|R_k\|_{C^3}\bigr).$$ Taking $\omega=2\pi km s_\beta$ and restoring $e^{2\pi\mathrm{i}km\sigma_c}$ proves the stated negative coefficient, independently of the sign of $\beta$. Equation [\[eq:elliptic-remainder-norm\]](#eq:elliptic-remainder-norm){reference-type="eqref" reference="eq:elliptic-remainder-norm"} with $J=3,S=2$ makes the remainders summable over all $k$ and uses only original $C^{12}$ norms. Thus the common $C^{20}$ bound in the statement is sufficient.

## The quadratic endpoint at $T=3/16$

Here $\sigma_E'(0)=0$ and $\gamma<0$. The positive extension of $$x=\sqrt{\frac{2(\sigma_E(\varepsilon)-\sigma_c)}{\gamma}}
   =\varepsilon(1+O(\varepsilon))$$ is an increasing analytic coordinate after shrinking the fixed neighbourhood. Its inverse $E$ has $E'(0)=1$, and the phase is exactly $\sigma_c+\gamma x^2/2$. Write the transformed amplitude as $$\chi(E(x))a_k(E(x))E'(x)=x c_k(x).$$ The function $c_k$ is smooth and compactly supported, $c_k(0)=A_k$, and finite-order division and the fixed change of variable give $$\label{ell:quadratic-amplitude-bound}
 \|c_k'\|_\infty+\|c_k''\|_{L^1}
 \leq C\bigl(|A_k|+\|R_k\|_{C^2}\bigr).$$ With $\omega=2\pi km\gamma$, an integration by parts with this actual compactly supported amplitude gives $$\label{ell:quadratic-ibp}
 \int_0^\infty xc_k(x)e^{\mathrm{i}\omega x^2/2}\,\,\mathrm{d}x
 =\frac{\mathrm{i}A_k}{\omega}
  -\frac1{\mathrm{i}\omega}\int_0^\infty
        c_k'(x)e^{\mathrm{i}\omega x^2/2}\,\,\mathrm{d}x.$$ Only the value $c_k(0)$ contributes at the boundary.

For completeness, let $d$ be compactly supported and $C^1$, and split its oscillatory integral at $\delta=|\omega|^{-1/2}$. The part on $[0,\delta]$ is at most $\delta\|d\|_\infty$. On $[\delta,\infty)$ use $\partial_xe^{\mathrm{i}\omega x^2/2}=\mathrm{i}\omega x e^{\mathrm{i}\omega x^2/2}$. The boundary and derivative terms are bounded by $$\frac{\|d\|_\infty}{|\omega|\delta}
 +\frac1{|\omega|}\int_\delta^\infty
      \left(\frac{|d'|}{x}+\frac{|d|}{x^2}\right)\,\,\mathrm{d}x
 \leq |\omega|^{-1/2}
       \bigl(2\|d\|_\infty+\|d'\|_{L^1}\bigr).$$ Consequently, $$\label{ell:quadratic-remainder}
 \left|\int_0^\infty d(x)e^{\mathrm{i}\omega x^2/2}\,\,\mathrm{d}x\right|
 \leq |\omega|^{-1/2}
       \bigl(3\|d\|_\infty+\|d'\|_{L^1}\bigr).$$ Apply this with $d=c_k'$ in [\[ell:quadratic-ibp\]](#ell:quadratic-ibp){reference-type="eqref" reference="ell:quadratic-ibp"}. The resulting single-mode error is at most $C|km|^{-3/2}(|A_k|+\|R_k\|_{C^2})$. Equation [\[eq:elliptic-remainder-norm\]](#eq:elliptic-remainder-norm){reference-type="eqref" reference="eq:elliptic-remainder-norm"} with $J=2,S=2$ sums these errors absolutely using original $C^{10}$ norms, and hence also the stated $C^{20}$ norms. Restoring the constant phase gives [\[ell:quadratic-endpoint\]](#ell:quadratic-endpoint){reference-type="eqref" reference="ell:quadratic-endpoint"}. This argument never treats the uncut integral of $xe^{\mathrm{i}\omega x^2/2}$ as a convergent ordinary improper integral.

The $m^{-1}$ term comes from the shrinking circle alone. At $T=3/16$ the persistent circle at $h_-$ is a separate, two-sided nondegenerate stationary circle, and contributes at order $m^{-1/2}$. The invariant partition in Section [7](#sec:global){reference-type="ref" reference="sec:global"} includes it once and combines the two contributions without changing the original observable class.

# Global asymptotics and sharpness {#sec:global}

## The global Fourier formula

Keep the compact energy window and original norms of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The commutation in Lemma [\[lem:coarea-projection\]](#lem:coarea-projection){reference-type="ref" reference="lem:coarea-projection"} gives $C_{2m+r}(f,g)=C_{2m}(f_r,g)$, where $f_r=f\circ F_T^r$. Since $F_T$ is a smooth energy-preserving automorphism and $r=0,1$, the chain rule on the fixed compact window gives $\|f_r\|_{C^a}\leq C_a\|f\|_{C^a}$, with no loss depending on $m$. Only the original observables are differentiated; the possibly nonsmooth functions $(I-\Pi)f$ and $(I-\Pi)g$ enter as $L^2$ functions.

Let $c$ initially index the circle families over the three regular energy intervals $I_c$. Coarea and circlewise Parseval yield $$\label{eq:global-fourier}
 C_{2m+r}(f,g)=\sum_c\sum_{k\ne0}\int_{I_c}
 L(h)\widehat f_{r,c,k}(h)\overline{\widehat g_{c,k}(h)}
 e^{2\pi\mathrm{i}km\sigma_c(h)}\,\,\mathrm{d}h.$$ This is an absolutely integrable Fourier representation. Indeed, Cauchy--Schwarz in $k$ and Parseval give, on each circle, $$\sum_{k\ne0}L\bigl|\widehat f_{r,c,k}
                  \overline{\widehat g_{c,k}}\bigr|
 \leq
 \left(\int_{C_h^c}|f_r-\Pi f_r|^2\,\,\mathrm{d}t\right)^{1/2}
 \left(\int_{C_h^c}|g-\Pi g|^2\,\,\mathrm{d}t\right)^{1/2}.$$ Integrating and applying Cauchy--Schwarz in $(h,c)$ bounds the result by $\|(I-\Pi)f_r\|_{L^2(\mu)}\|(I-\Pi)g\|_{L^2(\mu)}$. These norms are finite by properness, and the critical fibres have zero $\mu$-measure. Tonelli and Fubini therefore justify [\[eq:global-fourier\]](#eq:global-fourier){reference-type="eqref" reference="eq:global-fourier"}. Exchanges involving derivatives or asymptotic remainders require the additional summable bounds below; they do not follow from this first application of Fubini alone.

## Uniform stationary phase on regular tubes

[\[lem:stationary-phase\]]{#lem:stationary-phase label="lem:stationary-phase"} Suppose a smooth real phase $\sigma$ has a nondegenerate critical point $h_*$. On a sufficiently small fixed interval about $h_*$, every $a\in C_c^4$ satisfies, uniformly for $m\geq1$ and $k\in\mathbb{Z}\setminus\{0\}$, $$\label{glob:stationary-formula}
 \int a(h)e^{2\pi\mathrm{i}km\sigma(h)}\,\,\mathrm{d}h
 =\frac{a(h_*)e^{2\pi\mathrm{i}km\sigma(h_*)
       +\mathrm{i}\pi\mathop{\mathrm{sgn}}(k\sigma''(h_*))/4}}
       {\sqrt{m|k\sigma''(h_*)|}}
 +O\bigl(\|a\|_{C^4}(m|k|)^{-3/2}\bigr).$$ The implicit constant depends on the fixed phase and interval, not on the amplitude, $m$, or $k$.

The increasing Morse coordinate $y=\mathop{\mathrm{sgn}}(h-h_*)\sqrt{2|\sigma(h)-\sigma(h_*)|}$ gives $\sigma(h)=\sigma(h_*)+s_*y^2/2$, where $s_*=\mathop{\mathrm{sgn}}\sigma''(h_*)$, and $h'(0)=|\sigma''(h_*)|^{-1/2}$. Set $b(y)=a(h(y))h'(y)$, extended by zero, and use the Fourier transform $\widehat b(\xi)=\int_\mathbb{R}b(y)e^{-2\pi\mathrm{i}\xi y}\,\,\mathrm{d}y$. The Gaussian identity and Fourier inversion give, for real $v\ne0$, $$\int_\mathbb{R}b(y)e^{\mathrm{i}\pi vy^2}\,\,\mathrm{d}y
 =|v|^{-1/2}e^{\mathrm{i}\pi\mathop{\mathrm{sgn}}(v)/4}
   \int_\mathbb{R}\widehat b(\xi)e^{-\mathrm{i}\pi\xi^2/v}\,\,\mathrm{d}\xi.$$ To justify the identity, first insert $e^{-\delta y^2}$, $\delta>0$. The absolutely convergent Gaussian calculation has Fourier kernel bounded in modulus by $|v|^{-1/2}$; hence dominated convergence applies as $\delta\downarrow0$, since $\widehat b\in L^1$. Four integrations by parts, together with the fixed compact support, give $\int_\mathbb{R}\xi^2|\widehat b(\xi)|\,\,\mathrm{d}\xi\leq C\|b\|_{C^4}$. Thus replacing $e^{-\mathrm{i}\pi\xi^2/v}$ by $1$ has error at most $C\|b\|_{C^4}|v|^{-1}$. Take $v=mk s_*$, use Fourier inversion at zero, and substitute the value of $h'(0)$.

On a fixed regular circle tube, Lemma [\[lem:regular-norms\]](#lem:regular-norms){reference-type="ref" reference="lem:regular-norms"} and periodic integration by parts imply, for finite $j,s\geq0$, $$|\partial_h^j\widehat f_{r,c,k}(h)|
 \leq C_{j,s}\|f\|_{C^{j+s}}|k|^{-s},\qquad k\ne0.$$ For a fixed smooth energy cutoff $\chi$, the amplitude $a_k=\chi L\widehat f_{r,c,k}\overline{\widehat g_{c,k}}$ therefore has $\|a_k\|_{C^4}\leq C\|f\|_{C^5}\|g\|_{C^5}|k|^{-2}$. Lemma [\[lem:stationary-phase\]](#lem:stationary-phase){reference-type="ref" reference="lem:stationary-phase"} is consequently summable in all nonzero modes, both in its leading term and in its $O(m^{-3/2})$ remainder. At every stationary circle it supplies exactly the coefficient in [\[eq:stationary-coefficient\]](#eq:stationary-coefficient){reference-type="eqref" reference="eq:stationary-coefficient"}, including its Jacobian and phase sign. On the remaining regular tubes $|\sigma'|$ is bounded below. Repeated integration by parts with the transpose $a\mapsto-\partial_h(a/\sigma')$ has zero support-boundary terms and bounded coefficients. The same Fourier bound with $j=N,s=1$ gives an absolutely summed $O(m^{-N})$ contribution for each fixed $N$.

## One partition of the complete surface

We now combine the estimates in a single decomposition of [\[eq:global-fourier\]](#eq:global-fourier){reference-type="eqref" reference="eq:global-fourier"}. First choose a smooth energy cutoff near $h_+$ covering every degenerating complete circle. Proposition [\[prop:hyperbolic-decay\]](#prop:hyperbolic-decay){reference-type="ref" reference="prop:hyperbolic-decay"} applies to the lower circle and both upper circles, with no deleted neighbourhood of the saddle. Near $h_-$, the isolated elliptic point and the persistent compact circle have disjoint neighbourhoods. In a sufficiently narrow energy band the vanishing circles lie in the former and the persistent circles in the latter. Assign the same energy cutoff separately to these two families. The vanishing-family cutoff is constant near the centre and extends smoothly there; the persistent-family cutoff is smooth across $h_-$. On either regular side their sum is precisely the chosen band cutoff.

The remaining compact regular part has a finite cover by stationary and nonstationary circle tubes, with a smooth energy partition of unity. Every weight is constant on each entire circle and is inserted once in the amplitude. The partition is invariant under $G_T$; separate upper weights need not be invariant under $F_T$, since the latter has already been accounted for by $f_r$. At $T=3/16$ the persistent tube crosses $h_-=-2$, and its stationary point is treated once by the two-sided formula [\[glob:stationary-formula\]](#glob:stationary-formula){reference-type="eqref" reference="glob:stationary-formula"}. Splitting it at $h_-$ would introduce artificial endpoints. The vanishing family at the same energy is the different domain treated in Proposition [\[prop:elliptic-endpoints\]](#prop:elliptic-endpoints){reference-type="ref" reference="prop:elliptic-endpoints"}. For other parameters the persistent tube can be chosen nonstationary.

There are no further spatial endpoints: the energy-saturated supports are compact by Proposition [\[prop:surface\]](#prop:surface){reference-type="ref" reference="prop:surface"}, and the four terminal charts are regular parts of the tubes by Lemma [\[lem:regular-norms\]](#lem:regular-norms){reference-type="ref" reference="lem:regular-norms"}. Take $N=3$ for the saddle and regular nonstationary pieces. The former requires original $C^5$ norms; the regular stationary estimate also uses $C^5$. The elliptic remainders are controlled by $C^{12}$ in the nonstationary case and $C^{10}$ in the quadratic case, by [\[eq:elliptic-remainder-norm\]](#eq:elliptic-remainder-norm){reference-type="eqref" reference="eq:elliptic-remainder-norm"} and Proposition [\[prop:elliptic-endpoints\]](#prop:elliptic-endpoints){reference-type="ref" reference="prop:elliptic-endpoints"}. The fixed cutoffs and $f\mapsto f_r$ preserve these finite-order bounds. Thus the common original $C^{20}$ bound in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} controls every term, without asserting that it controls arbitrary $N$.

Adding the summable stationary terms gives $m^{-1/2}\mathcal A_r(m)$. For $T\notin\{3/16,1\}$, the elliptic $m^{-2}\mathcal B_r(m)$ term is absorbed by the $O(m^{-3/2})$ remainder, not absent. At $T=3/16$, the vanishing family contributes $m^{-1}\mathcal D_r(m)$, separately from the persistent-circle stationary term. At $T=1$, Proposition [\[prop:frequency\]](#prop:frequency){reference-type="ref" reference="prop:frequency"} leaves no stationary circle, so the elliptic term is the global leading term, with $O(m^{-3})$ remainder. This proves all three expansions in [\[eq:main-asymptotics\]](#eq:main-asymptotics){reference-type="eqref" reference="eq:main-asymptotics"}, together with the separately quantified hyperbolic estimate.

## The original even and odd coefficients

[\[prop:parity\]]{#prop:parity label="prop:parity"} On a circle preserved by $F_T$, including the persistent circle, $$\widehat f_{r,c,k}(h)=e^{2\pi\mathrm{i}kr\rho(h)}\widehat f_{c,k}(h),
 \qquad A_k^{(r)}=e^{2\pi\mathrm{i}kr\theta_T}A_k^{(0)}.$$ On an upper two-circle tube choose $z_0(h,\theta)$, set $z_1=F_Tz_0$, and denote the Fourier coefficients of $f\circ z_j$ and $g\circ z_j$ by $\widehat f_{j,k}$ and $\widehat g_{j,k}$. After combining the two equal phases, the even amplitude is $$L\bigl(\widehat f_{0,k}\overline{\widehat g_{0,k}}
       +\widehat f_{1,k}\overline{\widehat g_{1,k}}\bigr),$$ whereas the odd amplitude is $$\label{eq:odd-upper}
 L\bigl(\widehat f_{1,k}\overline{\widehat g_{0,k}}
       +e^{2\pi\mathrm{i}k\sigma(h)}\widehat f_{0,k}
                                      \overline{\widehat g_{1,k}}\bigr).$$ These amplitudes give the corresponding stationary coefficients on evaluation at the stationary energy. For every integer $n$, $C_{-n}(f,g)=\overline{C_n(g,f)}$.

On a preserved circle, $F_Tz(h,\theta)=z(h,\theta+\rho(h))$, so Fourier translation gives the first identity. Differentiating the amplitude at the elliptic endpoint gives the second: its constant term is zero by [\[eq:jet-amplitudes\]](#eq:jet-amplitudes){reference-type="eqref" reference="eq:jet-amplitudes"}, while $\rho(h_--\varepsilon)\to\theta_T$. On the upper tube, $(F_T)_*X=X$ ensures that $z_1$ has the same positive time angle and period as $z_0$. The exact relations are $$F_Tz_0(h,\theta)=z_1(h,\theta),\qquad
 F_Tz_1(h,\theta)=z_0(h,\theta+\sigma(h)).$$ Substitution in [\[eq:global-fourier\]](#eq:global-fourier){reference-type="eqref" reference="eq:global-fourier"} yields the two amplitudes. Finally the Koopman operator is unitary and commutes with $\Pi$; moving its inverse between the slots of the inner product and taking the conjugate proves the negative-time identity.

In particular, observables supported on only one upper circle family can have identically zero odd correlations and nonzero even correlations. Thus sharpness must not be formulated as a positive lower bound on both parity subsequences.

## Sharpness for original smooth observables

[\[prop:sharpness\]]{#prop:sharpness label="prop:sharpness"} For each fixed $T>0$, there exist real observables, and there exist complex observables, in $C_c^\infty(U_T)$ attaining a strictly positive normalized limsup at the rate in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. At $T=1$, the condition $(A_1^{(0)},A_{-1}^{(0)})\ne(0,0)$ is open and dense in the space of original first-jet pairs and suffices for this conclusion.

If $T\ne1$, choose one stationary circle $c\in\mathcal S_T$, a small regular tube about it, and a real bump $\chi$ with $\chi(h_c)=1$. Set $f=g=\chi(h)e^{2\pi\mathrm{i}\theta}$ on that tube and zero elsewhere. The bump vanishes near the tube boundary, so the regular trivialization makes these original smooth compactly supported functions, also through any terminal charts. If two circles share the energy, choose only one. At $T=3/16$ the tube about the persistent circle stays away from the elliptic point. There is only the mode $k=1$, and the even expansion is $$C_{2m}(f,f)=\frac{L(h_c)}{\sqrt{m|\sigma''(h_c)|}}
 e^{2\pi\mathrm{i}m\sigma(h_c)-\mathrm{i}\pi/4}+O(m^{-3/2}).$$ Its normalized modulus tends to a positive constant. For the real part of $f$, the leading term is a nonzero constant times $m^{-1/2}\cos(2\pi m\sigma(h_c)-\pi/4)$. This cosine cannot tend to zero: otherwise $e^{4\pi\mathrm{i}m\sigma(h_c)}\to-\mathrm{i}$, whose adjacent ratios force $e^{4\pi\mathrm{i}\sigma(h_c)}=1$; the sequence would then be identically one. Hence the real observables have positive normalized limsup as well.

For $T=1$, use the oriented Morse coordinates of Proposition [\[prop:elliptic-jets\]](#prop:elliptic-jets){reference-type="ref" reference="prop:elliptic-jets"} and take $f=g=\zeta((p^2+q^2)/2)(p+\mathrm{i}q)$, with $\zeta=1$ near zero and supported strictly inside the coordinate disc. Extension by zero is smooth on the original surface. The first-jet formula [\[eq:jet-amplitudes\]](#eq:jet-amplitudes){reference-type="eqref" reference="eq:jet-amplitudes"} gives $A_1^{(0)}=2L_0$ and $A_{-1}^{(0)}=0$; it does not assert that all higher Fourier modes vanish. Consequently $$C_{2m}(f,f)=-\frac{2L_0}{(2\pi\beta)^2m^2}
                    e^{2\pi\mathrm{i}m\sigma_c}+O(m^{-3}),$$ and again the normalized modulus tends to a positive constant. The real choice $\zeta p$ gives $A_1^{(0)}=A_{-1}^{(0)}=L_0/2$ and a nonzero cosine leading term. The sequence $\cos(2\pi m\sigma_c)$ cannot tend to zero, since $\cos(2x)=2\cos^2x-1$ would make its even subsequence tend to $-1$.

Finally, $\sigma_c=2\theta_T\in(1,4/3)$, so $q_*=e^{2\pi\mathrm{i}\sigma_c}$ and $q_*^{-1}$ are distinct. Write $\mathcal B_0(m)=b_+q_*^m+b_-q_*^{-m}$, where $b_\pm=-A_{\pm1}^{(0)}/(2\pi\beta)^2$. A finite geometric sum gives $$\lim_{M\to\infty}\frac1M\sum_{m=1}^M|\mathcal B_0(m)|^2
 =|b_+|^2+|b_-|^2.$$ When the two jet coefficients do not both vanish, this limit is positive, and hence the unaveraged normalized correlation has positive limsup. Their simultaneous vanishing is a proper closed real-algebraic condition on the finite-dimensional first-jet pair: the coefficients are sesquilinear expressions, and the example above shows they are not identically zero. A nonzero real polynomial cannot vanish on an open set, proving density of the complement; continuity proves openness. If both coefficients vanish, [\[eq:main-asymptotics\]](#eq:main-asymptotics){reference-type="eqref" reference="eq:main-asymptotics"} instead gives $O(m^{-3})$. No optimal classification of higher jets is needed.

The Cesàro mean in the last proof only tests nonvanishing of a finite oscillatory leading term. The correlations in the theorem, including the sharpness conclusions, remain unaveraged.

# Conclusion {#sec:conclusion}

The complete real q-Painlevé I map has sharp circlewise-centered correlations whose slowest scale is determined by its frequency geometry and original elliptic jets. Stationary circles give $n^{-1/2}$ decay for $T\ne1$; their absence at $T=1$ leaves the sharp $n^{-2}$ centre term. The value $T=3/16$ exhibits two different asymptotic contributions at one energy, and the original circle exchange remains visible in the odd-step coefficients. The theorem retains original smooth observables through both critical fibres and all terminal points. It does not assert unprojected or single-circle mixing, a central limit theorem, uniform estimates across parameter transitions, or a complete optimal hierarchy for higher centre jets.

[\[LastBodyPage\]]{#LastBodyPage label="LastBodyPage"}
