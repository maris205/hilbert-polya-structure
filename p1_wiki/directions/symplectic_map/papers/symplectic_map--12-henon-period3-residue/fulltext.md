---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--12-henon-period3-residue"
canonical_tex: "symplectic_map/papers/12-henon-period3-residue/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/12-henon-period3-residue/paper/manuscript.pdf"
source_sha256: "5c3b09a835aa41f35899f3c720982f911acf7046559c8433f38ab38ce61a0447"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Period-Three Trace Residues and a Minimal Separator on an Exceptional Quartic Hénon Fiber

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/12-henon-period3-residue>)
- [规范 TeX](<../../../../../symplectic_map/papers/12-henon-period3-residue/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/12-henon-period3-residue/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/12-henon-period3-residue/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symplectic_map/papers/12-henon-period3-residue/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $f_{m,a}(x,y)=(y+(x^m-a)^2,x)$ over an algebraically closed field of characteristic zero. We study trace moments on its nonreduced formal periodic schemes, rather than replacing those schemes by their reduced supports. The period-one multiplication spectrum is $0^{\times 2m}$, the formal exact-period-two spectrum is $2^{\times((2m)^2-2m)}$, and normalized conjugacy is governed by the coordinate $a^{2m-1}$. For the period-three cyclic complete intersection, we prove the two-term identity $$S_m(a,\varepsilon)=C_m\varepsilon^{3m}+D_m a^{2m-1}\varepsilon^{2m},$$ with $C_m=0$ for odd $m$, and derive a finite nested-binomial certificate for $D_m$ from a terminating normal-form recurrence and an exact Laurent fiber sum. In degree four, every normalized monic-centered map with formal fixed-point trace multiset $0^4$ belongs to the complete fiber $p(x)=(x^2-L)^2$. On this fiber the pointwise formal exact-period-three second trace moment is $$-1296000-1572864L^3,$$ the exact-period-three zero-cycle has length $60$, and the cyclewise moment is $-432000-524288L^3$. Since $L^3$ is precisely the normalized conjugacy coordinate while periods one and two are constant, period three is the minimal separator on this fiber. Universal nonvanishing of $D_m$ remains open.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Period-Three Trace Residues and a Minimal Separator\
  on an Exceptional Quartic Hénon Fiber
```

## Markdown 正文

# Introduction {#sec:introduction}

Finite collections of periodic multipliers can determine a polynomial automorphism only after one understands their exceptional fibers. In the normalized Jacobian-minus-one Hénon category, Cantat and Dujardin identified the quartic family $$(x,y)\longmapsto \bigl(y+(x^2-\lambda^2)^2,x\bigr)$$ whose period-one and period-two trace data are constant [@CantatDujardin2026]. Thus neither the family nor its low-period blindness is new. The concrete question left by this obstruction is whether a later period supplies an effective coordinate on the whole exceptional fiber.

This note answers that question at period three for the complete normalized quartic fiber whose formal fixed-point trace multiset is $0^4$. Writing $L=\lambda^2$, we show that the pointwise formal exact-period-three second trace moment equals $$-384(3375+4096L^3).$$ The coefficient of $L^3$ is nonzero, and $L^3$ is exactly the residual normalized conjugacy coordinate. Since the two lower formal trace multisets are constant, this gives a sharp minimal separator on that fiber. It does not give a global period cutoff for all quartic Hénon maps.

The quartic identity is the endpoint of a uniform algebraic mechanism. For every $m\ge2$, three cyclic orbit equations form a monic complete intersection of rank $(2m)^3$. Their Jacobian determinant is also the trace of the third derivative iterate. Classical quotient-trace and global residue theory then converts the desired trace moment into a top normal-form coefficient [@CattaniDickensteinSturmfels1996]. Weighted homogeneity and a local degeneration leave only two parameter monomials. The remaining slope is evaluated by an explicit recurrence-to-Laurent-to-binomial argument. The conclusion is a formula for $D_m$, not a proof that $D_m\ne0$ in every degree.

Our contributions are therefore the following.

1.  We retain the nonreduced formal periodic algebras and compute the period-one and formal exact-period-two trace spectra, as well as the normalized quotient coordinate $a^{2m-1}$.

2.  We prove the uniform period-three law $S_m=C_m\varepsilon^{3m}+D_ma^{2m-1}\varepsilon^{2m}$, the odd-$m$ identity $C_m=0$, and a transparent finite certificate for $D_m$.

3.  We classify the complete normalized quartic fiber with formal fixed-point trace multiset $0^4$, compute its period-three affine moment by two source-level derivations, and prove its scoped minimality after a separate local-multiplicity argument.

![image](<../../../../../symplectic_map/papers/12-henon-period3-residue/paper/figures/fig1_theorem_architecture.pdf>){width="\\textwidth"}

The proof has two distinctions that cannot be suppressed. First, a trace element can be nonzero and nilpotent on a nonreduced scheme even when its formal multiplication spectrum contains only zero. Second, vanishing of the fixed *moment* does not determine the fixed scheme's local *multiplicity*. The former is handled in the finite quotient algebras; the latter is proved by formal transverse elimination before any exact-period length is subtracted.

# Prior work and claim boundary {#sec:prior}

#### Normal forms and multiplier rigidity.

Friedland--Milnor theory supplies the structural and conjugacy framework for plane polynomial automorphisms and generalized Hénon normal forms [@FriedlandMilnor1989]. Cantat--Dujardin place this framework in a modern multiplier-rigidity setting and provide the direct quartic period-one/two obstruction used here [@CantatDujardin2026]. Our equivalence $f_{m,a}\sim f_{m,b}$ if and only if $a^{2m-1}=b^{2m-1}$ is a proved specialization within the normalized one-factor category, not a new general normal-form theorem.

#### Residues and exact Hénon identities.

Multidimensional residues, quotient-algebra traces, deformations to initial forms, and coefficient extraction are established tools [@CattaniDickensteinSturmfels1996]. Exact periodic-orbit sum rules for Hénon dynamics also predate this work [@CvitanovicHansenRolfVattay1998]. Those contour and Fredholm-type sums use different weights from the raw finite-algebra trace power considered below. The present contribution is the family-specific complete intersection, the two-term reduction, its coefficient certificate, and the quartic separator; it is not the residue formalism itself.

#### Low periods and adjacent multiplier invariants.

Low-period equations and stability for generalized Hénon maps have been studied explicitly, for example in the cubic area-preserving setting [@DullinMeiss2000]. Small-cycle multiplier maps in one-dimensional polynomial moduli provide a close comparison but do not cover Jacobian-minus-one plane automorphisms [@Huguin2024]. Formal dynatomic cycles and higher-dimensional projective multiplier invariants supply adjacent language and background [@Hutz2010; @Hutz2020]. Index-derived fixed-point relations in projective and polynomial-automorphism settings are further methodological neighbors [@GuillotRamirez2019; @Ueda2004]. None of these sources is used as a direct proof of the identities below.

#### Bounded novelty statement.

The literature search underlying this note located no prior explicit formula for the period-three moment, the all-$m$ coefficient certificate, or the scoped quartic minimal-separator theorem. This is a bounded absence statement, not a historical-priority proof. The claim-safe delta is limited to the source-proved period-three results. In particular, we do not claim discovery of the exceptional quartic family, novelty of formal cycles or global residues, or a first exact Hénon period-three calculation of any kind.

# Formal periodic algebras and main results {#sec:setup}

Let $\Bbbk$ be an algebraically closed field of characteristic zero. For an integer $m\ge2$ and $a\in\Bbbk$, set $$p_{m,a}(x)=(x^m-a)^2,
\qquad
q_{m,a}(x)=p_{m,a}'(x)=2m x^{m-1}(x^m-a),
\label{eq:family-polynomials}$$ and $$f_{m,a}(x,y)=\bigl(y+p_{m,a}(x),x\bigr).
\label{eq:family-map}$$ The Jacobian determinant of $f_{m,a}$ is $-1$.

Let $B$ be a finite-dimensional $\Bbbk$-algebra and $h\in B$. The formal multiset of values of $h$ is the multiset of roots of $\det(TI-M_h)$, counted with algebra dimension. Here $M_h$ is multiplication by $h$. This convention retains nilpotent scheme length while attaching to each support point the residue-field value of $h$.

For period two, "formal exact period two" means the formal period-two spectral zero-cycle minus the embedded formal fixed spectral zero-cycle. For prime period three, we use the analogous subtraction, but we will prove separately that the local fixed length inside $\mathop{\mathrm{Fix}}(f^3)$ is the expected one.

Write $$\nu=2m-1,
\qquad
X_{\mathrm{top}}=x_0^\nu x_1^\nu x_2^\nu.
\label{eq:nu-top}$$ All cyclic indices below lie in $\mathbb{Z}/3\mathbb{Z}$.

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} For the family [\[eq:family-map\]](#eq:family-map){reference-type="eqref" reference="eq:family-map"}:

1.  the formal period-one trace multiset is $0^{\times2m}$, and the formal exact-period-two trace multiset is $2^{\times((2m)^2-2m)}$;

2.  within normalized monic-centered Hénon moduli, $$f_{m,a}\sim f_{m,b}
      \quad\Longleftrightarrow\quad
      a^{2m-1}=b^{2m-1};$$

3.  the formal period-three $m$-th trace moment satisfies $$S_m(a,\varepsilon)=C_m\varepsilon^{3m}+D_m a^{2m-1}\varepsilon^{2m}
      \label{eq:two-term-main}$$ for integers $C_m,D_m$, and $C_m=0$ whenever $m$ is odd;

4.  defining $$\begin{aligned}
      H(r,k)
      &=\sum_{\substack{u+v=k\\2u\le r,\;2v\le r}}
        \binom{k}{u}\binom{r}{2u}\binom{r}{2v},
      \label{eq:H-definition}\\
      A_{m,r}
      &=\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
        (-1)^{r+k}\binom{m-1}{2(m-k)-1}H(r,k),
      \label{eq:A-definition}
      \end{aligned}$$ with an empty sum equal to zero, the slope has the exact certificate $$D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
      \binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.
      \label{eq:D-certificate-main}$$

No assertion that $D_m\ne0$ for all $m$ is included.

[\[thm:quartic\]]{#thm:quartic label="thm:quartic"} Let $p$ be any monic-centered quartic, and set $f_p(x,y)=(y+p(x),x)$. Its formal fixed-point trace multiset is $0^4$ if and only if $$p(x)=(x^2-L)^2$$ for a unique $L\in\Bbbk$. On this complete normalized fiber, $$S_2^{(3)}(L)=-1296000-1572864L^3
=-384(3375+4096L^3).
\label{eq:quartic-moment-main}$$ Moreover, $$f_{2,L}\sim f_{2,M}
\quad\Longleftrightarrow\quad
L^3=M^3.$$ The period-one and formal exact-period-two trace multisets are constant on the fiber, whereas [\[eq:quartic-moment-main\]](#eq:quartic-moment-main){reference-type="eqref" reference="eq:quartic-moment-main"} is affine with nonzero slope in $L^3$. Hence period three is the minimal separating period on this fiber. The formal exact-period-three zero-cycle has pointwise length $60$, and its cyclewise second trace moment is $$-432000-524288L^3.$$

The minimality conclusion in [\[thm:quartic\]](#thm:quartic){reference-type="ref" reference="thm:quartic"} concerns only the complete normalized quartic fiber with formal fixed-point trace multiset $0^4$. It is neither a theorem for all quartic Hénon maps nor a global equality for a degree-four period cutoff.

# Low periods and normalized conjugacy {#sec:low-periods}

Write $p=p_{m,a}$ and $q=q_{m,a}$. A fixed point satisfies $x=y$ and $p(x)=0$, so its coordinate algebra is $$B_1=\Bbbk[x]/(p)=\Bbbk[x]/((x^m-a)^2),
\qquad \dim_{\Bbbk}B_1=2m.
\label{eq:fixed-algebra}$$ Within $B_1$, $$q=2m x^{m-1}(x^m-a),
\qquad q^2=0.$$ Since $$Df_{m,a}(x,y)=
\begin{pmatrix}q(x)&1\\1&0\end{pmatrix},$$ the trace element on the fixed algebra is $q$. Multiplication by $q$ is nilpotent, hence its characteristic polynomial is $T^{2m}$. This gives the formal multiset $0^{\times2m}$. The statement is spectral: when $a\ne0$, the class of $q$ is generally not zero in the nonreduced algebra.

A direct iteration gives $$f_{m,a}^2(x,y)=\bigl(x+p(y+p(x)),y+p(x)\bigr).$$ The fixed equations for $f^2$ reduce to $p(x)=p(y)=0$, so $$B_2=\Bbbk[x,y]/(p(x),p(y)),
\qquad \dim_{\Bbbk}B_2=(2m)^2.
\label{eq:period-two-algebra}$$ The derivative trace is $$\mathop{\mathrm{Tr}}(Df_{m,a}^2)=2+q(x)q(y).$$ Because $(q(x)q(y))^2=0$, its sole formal eigenvalue is $2$, with multiplicity $(2m)^2$. On the embedded fixed algebra the same trace is $2+q^2=2$. Subtracting the length-$2m$ fixed spectral cycle yields $2^{\times((2m)^2-2m)}$. Nothing in this argument reduces either scheme, so it remains valid at $a=0$.

We next identify the normalized moduli coordinate. For $h_c(x,y)=(cx,cy)$, $$\begin{aligned}
h_c^{-1}f_{m,a}h_c(x,y)
&=\left(y+c^{-1}(c^m x^m-a)^2,x\right)\notag\\
&=\left(y+c^{2m-1}(x^m-ac^{-m})^2,x\right).
\label{eq:diagonal-conjugacy}\end{aligned}$$ The image stays monic exactly when $c^{2m-1}=1$, and then the new parameter is $b=ac^{-m}$. Thus conjugacy implies $b^{2m-1}=a^{2m-1}$.

Conversely, if $a^{2m-1}=b^{2m-1}$ and $a\ne0$, then $\zeta=b/a$ is a $(2m-1)$-st root of unity. Since $\gcd(m,2m-1)=1$, exponentiation by $-m$ is an automorphism of this root group; choose $c$ with $c^{2m-1}=1$ and $c^{-m}=\zeta$. Equation [\[eq:diagonal-conjugacy\]](#eq:diagonal-conjugacy){reference-type="eqref" reference="eq:diagonal-conjugacy"} gives the desired conjugacy. The case $a=0$ forces $b=0$.

For necessity within the normalized category, normal-form uniqueness reduces a polynomial conjugacy to a simultaneous affine change $(x,y)\mapsto(cx+d,cy+d)$. The coefficient of $x^{2m-1}$ in the transformed degree-$2m$ polynomial is $2md/c$. Centering and characteristic zero force $d=0$, so the diagonal calculation exhausts the normalized conjugacies.

# The cyclic complete intersection and trace residue {#sec:cyclic}

Represent a length-three orbit by states $(x_i,x_{i-1})$. Introduce the deformation $$F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1}),
\qquad
q_i=2m x_i^{m-1}(x_i^m-a).
\label{eq:cyclic-system}$$ At $\varepsilon=1$, the equations $F_i=0$ are exactly the cyclic equations for $\mathop{\mathrm{Fix}}(f_{m,a}^3)$. Their Jacobian matrix is $$\left(\frac{\partial F_i}{\partial x_j}\right)
=
\begin{pmatrix}
q_0&-\varepsilon&\varepsilon\\
\varepsilon&q_1&-\varepsilon\\
-\varepsilon&\varepsilon&q_2
\end{pmatrix},$$ and its determinant is $$t_\varepsilon=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
\label{eq:t-epsilon}$$ If $M(q)=\bigl(\begin{smallmatrix}q&1\\1&0\end{smallmatrix}\bigr)$, then $Df^3=M(q_2)M(q_1)M(q_0)$. Multiplication of these three matrices shows that $\mathop{\mathrm{Tr}}(Df^3)=q_0q_1q_2+q_0+q_1+q_2=t_1$.

Let $$\mathcal{A}_m=
\Bbbk[a,\varepsilon,x_0,x_1,x_2]/(F_0,F_1,F_2).
\label{eq:cyclic-algebra}$$ For any degree-compatible monomial order, the leading monomials are $x_0^{2m},x_1^{2m},x_2^{2m}$. They are pairwise coprime, so the three relations form a Gröbner basis over $\Bbbk[a,\varepsilon]$. Consequently $$x_0^{e_0}x_1^{e_1}x_2^{e_2},
\qquad 0\le e_i<2m,$$ form a free basis of $\mathcal{A}_m$, of rank $(2m)^3$. The leading homogeneous forms have no common point in $\mathbb{P}^2$, hence no intersection length is lost at infinity.

Define $$S_m(a,\varepsilon)=
\mathop{\mathrm{Tr}}_{\mathcal{A}_m/\Bbbk[a,\varepsilon]}\bigl(M_{t_\varepsilon^m}\bigr).
\label{eq:S-definition}$$ The Jacobian of the complete intersection is $t_\varepsilon$. The standard trace--residue identity, valid also for nonreduced complete intersections, gives $$S_m(a,\varepsilon)=\mathop{\mathrm{Res}}_{F_0,F_1,F_2}(t_\varepsilon^{m+1}).
\label{eq:trace-residue}$$ For these monic leading forms, the residue is the top normal-form coefficient: $$\mathop{\mathrm{Res}}(G)=\left[x_0^{2m-1}x_1^{2m-1}x_2^{2m-1}\right]\mathop{\mathrm{NF}}(G).
\label{eq:top-residue}$$ In particular, $S_m\in\mathbb{Z}[a,\varepsilon]$.

# The two-term law {#sec:two-term}

Assign weights $$\mathop{\mathrm{wt}}(x_i)=1,
\qquad
\mathop{\mathrm{wt}}(a)=m,
\qquad
\mathop{\mathrm{wt}}(\varepsilon)=2m-1=\nu.$$ Each $F_i$ has weight $2m$, every $q_i$ has weight $\nu$, and $t_\varepsilon$ has weight $3\nu$. Therefore each monomial $a^r\varepsilon^s$ in $S_m$ satisfies $$mr+\nu s=3m\nu.$$ Since $\gcd(m,\nu)=1$, the only nonnegative solutions are $$(r,s)=(0,3m),(\nu,2m),(2\nu,m),(3\nu,0).$$ Thus $$S_m=c_{0,m}\varepsilon^{3m}+c_{1,m}a^\nu\varepsilon^{2m}
+c_{2,m}a^{2\nu}\varepsilon^m+c_{3,m}a^{3\nu}.
\label{eq:four-term}$$

![image](<../../../../../symplectic_map/papers/12-henon-period3-residue/paper/figures/fig2_weighted_two_term_law.pdf>){width="\\textwidth"}

At $\varepsilon=0$, the algebra is the tensor product of three copies of $\Bbbk[a,x]/((x^m-a)^2)$. In each factor $q_i^2=0$, whereas $t_0=q_0q_1q_2$. Because $m\ge2$, we have $t_0^m=0$, and hence $S_m(a,0)=0$. Therefore $c_{3,m}=0$.

It remains to remove the term of $\varepsilon$-order $m$. Fix $a\ne0$ and work over an algebraic closure of the Puiseux field in $\varepsilon$, normalized by $v(\varepsilon)=1$. Flatness clusters all $(2m)^3$ solutions at triples $(\alpha_0,\alpha_1,\alpha_2)$ of roots of $x^m=a$. Put $x_i=\alpha_i+\delta_i$. Since the roots are nonzero and simple before squaring, $$(x_i^m-a)^2=c_i\delta_i^2+O(\delta_i^3),
\qquad
q_i=d_i\delta_i+O(\delta_i^2),$$ with $c_i,d_i\ne0$. Three root patterns exhaust the possibilities.

#### All roots distinct.

Every constant coupling $\alpha_{i-1}-\alpha_{i+1}$ is nonzero. Balancing its valuation $1$ against $2v(\delta_i)$ gives $v(q_i)=1/2$, hence $$v(t_\varepsilon)\ge\frac32.
\label{eq:valuation-distinct}$$

#### Exactly two roots equal.

After cyclic relabeling take $\alpha_0=\alpha_1\ne\alpha_2$. The first two equations give $v(q_0)=v(q_1)=1/2$. In the third equation the coupling has valuation at least $3/2$. If $v(\delta_2)<3/4$, its square would be the unique least-valuation term. Therefore $$v(q_2)\ge\frac34,
\qquad
v(t_\varepsilon)\ge\frac74.
\label{eq:valuation-twoequal}$$

#### All roots equal.

Let $r_0$ be the minimum valuation of a nonzero $\delta_i$. Coupling terms have valuation at least $1+r_0$. If $r_0<1$, a coordinate with valuation $r_0$ would contribute an uncancelled square of valuation $2r_0<1+r_0$. Hence every nontrivial branch has $r_0\ge1$, and $$v(t_\varepsilon)\ge3.
\label{eq:valuation-allequal}$$ The exact diagonal fixed branch is handled separately in [\[lem:fixed-moment\]](#lem:fixed-moment){reference-type="ref" reference="lem:fixed-moment"}; its moment contribution vanishes identically.

The trace of multiplication by an element of a finite algebra is the sum of its support values weighted by local length; nilpotent parts have trace zero. The three lower bounds show that every nonfixed cluster contributes to $S_m$ with $\varepsilon$-valuation strictly greater than $m$: the bounds are $3m/2$, $7m/4$, and $3m$, respectively. Summation cannot decrease valuation. In [\[eq:four-term\]](#eq:four-term){reference-type="eqref" reference="eq:four-term"}, the only surviving candidate of exact order $m$ is $c_{2,m}a^{2\nu}\varepsilon^m$. Since $a\ne0$, it follows that $c_{2,m}=0$. Setting $C_m=c_{0,m}$ and $D_m=c_{1,m}$ proves [\[eq:two-term-main\]](#eq:two-term-main){reference-type="eqref" reference="eq:two-term-main"}.

Finally, the coordinate reversal $x_i\mapsto x_{-i}$ sends the system with $\varepsilon$ to the system with $-\varepsilon$, while $t_\varepsilon$ is unchanged. Therefore $S_m(a,\varepsilon)=S_m(a,-\varepsilon)$. The $D_m$-term is always even in $\varepsilon$; if $m$ is odd, $3m$ is odd, forcing $C_m=0$.

# A transparent coefficient certificate for $D_m$ {#sec:coefficient}

This section gives the full coefficient extraction. It is an algebraic proof for symbolic $m$, not an interpolation from finitely many degrees.

![image](<../../../../../symplectic_map/papers/12-henon-period3-residue/paper/figures/fig3_step9_certificate_pipeline.pdf>){width="\\textwidth"}

For every integer exponent $e_i\ge2m$, the relation $F_i=0$ yields $$\begin{aligned}
x_i^{e_i}\equiv{}&2a x_i^{e_i-m}-a^2x_i^{e_i-2m}
-\varepsilon x_i^{e_i-2m}x_{i-1}
+\varepsilon x_i^{e_i-2m}x_{i+1}
\pmod{(F_0,F_1,F_2)}.
\end{aligned}
\tag{R}\label{eq:recurrence-R}$$

For $\boldsymbol{e}=(e_0,e_1,e_2)\in\mathbb{Z}^3$ and $\alpha,\beta\in\mathbb{Z}$, define $$\mathcal{R}_m(\boldsymbol{e};\alpha,\beta)=
\left[a^\alpha\varepsilon^\beta X_{\mathrm{top}}\right]\mathop{\mathrm{NF}}(x_0^{e_0}x_1^{e_1}x_2^{e_2}).
\label{eq:R-state}$$ It is zero if some $e_i<0$, or if $\alpha<0$ or $\beta<0$. On the standard box its complete base cases are $$\mathcal{R}_m(\boldsymbol{e};\alpha,\beta)=
\begin{cases}
1,&\boldsymbol{e}=(\nu,\nu,\nu),\ (\alpha,\beta)=(0,0),\\
0,&0\le e_i<2m\text{ for all }i\text{, otherwise}.
\end{cases}
\label{eq:R-base}$$ If $e_i\ge2m$, [\[eq:recurrence-R\]](#eq:recurrence-R){reference-type="eqref" reference="eq:recurrence-R"} gives the four signed branches $$\begin{aligned}
\mathcal{R}_m(\boldsymbol{e};\alpha,\beta)
={}&2\mathcal{R}_m(\boldsymbol{e}-m\boldsymbol{\delta}_i;\alpha-1,\beta)
-\mathcal{R}_m(\boldsymbol{e}-2m\boldsymbol{\delta}_i;\alpha-2,\beta)\\
&-\mathcal{R}_m(\boldsymbol{e}-2m\boldsymbol{\delta}_i+\boldsymbol{\delta}_{i-1};\alpha,\beta-1)
+\mathcal{R}_m(\boldsymbol{e}-2m\boldsymbol{\delta}_i+\boldsymbol{\delta}_{i+1};\alpha,\beta-1).
\end{aligned}
\label{eq:R-branches}$$ The total exponent decreases by $m,2m,2m-1,2m-1$, respectively. Thus [\[eq:R-base\]](#eq:R-base){reference-type="eqref" reference="eq:R-base"}--[\[eq:R-branches\]](#eq:R-branches){reference-type="eqref" reference="eq:R-branches"}, under any fixed reducible-coordinate choice, form a terminating induction certificate.

The same coefficient has the order-independent Laurent representation $$\mathcal{R}_m(\boldsymbol{e};\alpha,\beta)=
\left[a^\alpha\varepsilon^\beta x_0^{-1}x_1^{-1}x_2^{-1}\right]\frac{x_0^{e_0}x_1^{e_1}x_2^{e_2}}{F_0F_1F_2},
\label{eq:R-laurent}$$ where $$\frac1{F_i}=x_i^{-2m}\sum_{h\ge0}
\left(
\frac{2a x_i^m-a^2-\varepsilon x_{i-1}+\varepsilon x_{i+1}}{x_i^{2m}}
\right)^h.
\label{eq:reciprocal-expansion}$$ Unique normal form proves reduction-order independence. In the Laurent picture, interleavings of reductions at distinct coordinates are merely different orders for the same monomial; branch-count tuples, rather than interleavings, index the summands.

Expand $$t_\varepsilon^{m+1}
=\sum_{j=0}^{m+1}\binom{m+1}{j}\varepsilon^{2j}
(q_0q_1q_2)^{m+1-j}(q_0+q_1+q_2)^j.
\label{eq:t-power-expansion}$$ Put $\bar q_i=x_i^{m-1}(x_i^m-a)$. Extracting every scalar $2m$, define $$\begin{aligned}
\mathcal{C}_{m,j}:={}&
\left[a^\nu\varepsilon^{2m-2j}X_{\mathrm{top}}\right]\mathop{\mathrm{NF}}\!\left(
(\bar q_0\bar q_1\bar q_2)^{m+1-j}
(\bar q_0+\bar q_1+\bar q_2)^j
\right).
\end{aligned}
\label{eq:C-precollapse}$$ Then $$D_m=\sum_{j=0}^{m+1}\binom{m+1}{j}
(2m)^{3m+3-2j}\mathcal{C}_{m,j}.
\label{eq:D-precollapse}$$

Set $r=m-j$ for $0\le j\le m$. Choose $\boldsymbol{s}=(s_0,s_1,s_2)\in\mathbb{N}^3$ with $|\boldsymbol{s}|=j$ and put $N_i=r+1+s_i$. Choosing the low term in exactly $\ell_i$ of the $N_i$ factors of $\bar q_i=x_i^{2m-1}-a x_i^{m-1}$ gives $$e_i=(2m-1)N_i-m\ell_i,
\qquad 0\le\ell_i\le N_i.$$ The terminating recurrence therefore gives $$\begin{aligned}
\mathcal{C}_{m,j}
={}&\sum_{|\boldsymbol{s}|=j}\binom{j}{s_0,s_1,s_2}
\sum_{0\le\ell_i\le N_i}
(-1)^{|\boldsymbol{\ell}|}\prod_{i=0}^2\binom{N_i}{\ell_i}\\
&\hspace{25mm}\cdot
\mathcal{R}_m\bigl(\boldsymbol{e};\nu-|\boldsymbol{\ell}|,2r\bigr).
\end{aligned}
\label{eq:C-recurrence-certificate}$$ For $j=m+1$, the requested $\varepsilon$-degree is negative, and $\mathcal{C}_{m,m+1}=0$.

We now unfold [\[eq:reciprocal-expansion\]](#eq:reciprocal-expansion){reference-type="eqref" reference="eq:reciprocal-expansion"}. At source coordinate $i$, let $A_i,B_i,U_i,V_i$ count, respectively, the four branch choices $$2a x_i^m,\qquad -a^2,\qquad -\varepsilon x_{i-1},\qquad +\varepsilon x_{i+1},$$ and set $$h_i=A_i+B_i+U_i+V_i,
\qquad
T_i=U_{i+1}+V_{i-1}.
\label{eq:h-T}$$ A tuple $$(\boldsymbol{s},\boldsymbol{\ell},\boldsymbol{A},\boldsymbol{B},\boldsymbol{U},\boldsymbol{V})
\label{eq:admissible-tuple}$$ is admissible when all entries are nonnegative integers, $|\boldsymbol{s}|=j$, $0\le\ell_i\le N_i$, and $$\begin{aligned}
|\boldsymbol{\ell}|+\sum_i(A_i+2B_i)&=\nu,
\label{eq:admissible-a}\\
\sum_i(U_i+V_i)&=2r,
\label{eq:admissible-epsilon}\\
e_i+mA_i+T_i-2m(h_i+1)&=-1
\qquad(i=0,1,2).
\label{eq:admissible-laurent}\end{aligned}$$ Its signed multiplicity is $$\begin{aligned}
W={}&(-1)^{|\boldsymbol{\ell}|+\sum_i(B_i+U_i)}
2^{\sum_iA_i}\binom{j}{s_0,s_1,s_2}\\
&\cdot\prod_{i=0}^2
\binom{N_i}{\ell_i}
\frac{h_i!}{A_i!B_i!U_i!V_i!}.
\end{aligned}
\label{eq:admissible-weight}$$ Every expanded Laurent choice has exactly one branch-count tuple, and every admissible tuple has the requested parameter degrees and three Laurent exponents. Thus $$\mathcal{C}_{m,j}=\sum_{\text{admissible tuples in }\eqref{eq:admissible-tuple}}W.
\label{eq:C-admissible-sum}$$ The sum is finite by [\[eq:admissible-a\]](#eq:admissible-a){reference-type="eqref" reference="eq:admissible-a"}--[\[eq:admissible-epsilon\]](#eq:admissible-epsilon){reference-type="eqref" reference="eq:admissible-epsilon"}, and the description is exhaustive without double counting.

## The local signed fiber identity {#subsec:fiber-identity}

We use generalized binomial coefficients $$\binom{z}{s}=\frac{z(z-1)\cdots(z-s+1)}{s!}
\quad(s\ge1),
\qquad
\binom{z}{0}=1,$$ and set $\binom{z}{s}=0$ for $s<0$. For a nonnegative integer upper argument, the usual out-of-range values are zero.

[\[lem:local-fiber\]]{#lem:local-fiber label="lem:local-fiber"} For $N,n,\alpha\in\mathbb{N}$, $$\sum_{\substack{\ell,A,B\ge0\\\ell+A+2B=\alpha}}
(-1)^{\ell+B}2^A\binom{N}{\ell}
\frac{(n+A+B)!}{n!A!B!}
=(-1)^\alpha\binom{N-2n-2}{\alpha}.
\label{eq:local-fiber}$$

Take the coefficient of $z^\alpha$ in $$\begin{aligned}
(1-z)^N
\sum_{A,B\ge0}
\frac{(n+A+B)!}{n!A!B!}(2z)^A(-z^2)^B
&=(1-z)^N(1-2z+z^2)^{-n-1}\\
&=(1-z)^{N-2n-2}.\end{aligned}$$ The left coefficient is the sum in [\[eq:local-fiber\]](#eq:local-fiber){reference-type="eqref" reference="eq:local-fiber"}, and the right coefficient is $(-1)^\alpha\binom{N-2n-2}{\alpha}$.

Fix $(\boldsymbol{s},\boldsymbol{U},\boldsymbol{V})$ and put $$n_i=U_i+V_i,
\qquad
\lambda_i=N_i-2n_i-2,
\qquad
\alpha_i=\frac{(2m-1)(N_i-1)+T_i}{m}-2n_i.
\label{eq:local-exponents}$$ Because $\sum_i(N_i-1)=m+2r$ and $\sum_iT_i=\sum_i n_i=2r$, $$\sum_i\alpha_i
=\frac{(2m-1)(m+2r)+2r}{m}-4r
=2m-1=\nu.
\label{eq:alpha-sum}$$ Equation [\[eq:admissible-laurent\]](#eq:admissible-laurent){reference-type="eqref" reference="eq:admissible-laurent"} is precisely $\ell_i+A_i+2B_i=\alpha_i$. Multiplying [\[lem:local-fiber\]](#lem:local-fiber){reference-type="ref" reference="lem:local-fiber"} by the orientation factor $(-1)^{U_i}\binom{n_i}{U_i}$ turns its factorial into $$\binom{n_i}{U_i}
\frac{(n_i+A_i+B_i)!}{n_i!A_i!B_i!}
=\frac{h_i!}{A_i!B_i!U_i!V_i!}.$$ Thus the local identity sums exactly over $(\ell_i,A_i,B_i)$ at fixed coupling orientations, including all signs and powers of two. Define $$\mathcal{B}(\lambda,\alpha)=
\begin{cases}
(-1)^\alpha\binom{\lambda}{\alpha},&\alpha\in\mathbb{N},\\
0,&\text{otherwise}.
\end{cases}
\label{eq:B-local}$$

## Distinguished coordinate and transfer flow {#subsec:transfer}

The integrality condition in [\[eq:local-exponents\]](#eq:local-exponents){reference-type="eqref" reference="eq:local-exponents"} is $$T_i\equiv N_i-1=r+s_i\pmod m.
\label{eq:transfer-congruence}$$ Write $T_i=r+s_i+mz_i$. Since $\sum_iT_i=2r$ and $\sum_i(r+s_i)=m+2r$, $$z_0+z_1+z_2=-1.
\label{eq:z-sum}$$ Also $0\le r+s_i\le m$. Nonnegativity of $T_i$ forces $z_i\ge-1$, and $z_i=-1$ is possible only if $s_i=j$ and $T_i=0$.

Suppose first that $j\ge1$. Two coordinates cannot both have $s_i=j$ because $\sum_i s_i=j$. Equation [\[eq:z-sum\]](#eq:z-sum){reference-type="eqref" reference="eq:z-sum"} therefore forces a unique distinguished coordinate $d$ with $$s_d=j,\quad T_d=0,
\qquad
s_i=0,\quad T_i=r\quad(i\ne d).
\label{eq:distinguished-coordinate}$$ By cyclic symmetry take $d=0$, and write $$u=U_0,
\qquad
v=V_0,
\qquad
k=n_0=u+v.$$ The incoming-transfer equations give uniquely $$U_1=0,\quad V_2=0,\quad
V_1=r-u,\quad U_2=r-v,\quad
n_1=r-u,\quad n_2=r-v.
\label{eq:incoming-flow}$$ Conversely, every nonnegative $(k,u,v)$ satisfying the ranges below gives one transfer configuration.

At the distinguished coordinate, $$(\lambda_0,\alpha_0)=(m-1-2k,2m-1-2k),$$ whereas $$(\lambda_1,\alpha_1)=(2u-r-1,2u),
\qquad
(\lambda_2,\alpha_2)=(2v-r-1,2v).$$ Using $$(-1)^\alpha\binom{\alpha-M}{\alpha}=\binom{M-1}{\alpha}
\qquad(M\ge1,\ \alpha\ge0),$$ the local factors become $$\mathcal{B}(\lambda_0,\alpha_0)
=\binom{m-1}{2(m-k)-1},
\quad
\mathcal{B}(\lambda_1,\alpha_1)=\binom{r}{2u},
\quad
\mathcal{B}(\lambda_2,\alpha_2)=\binom{r}{2v}.
\label{eq:three-local-factors}$$ They are nonzero exactly when $$\left\lceil\frac m2\right\rceil\le k\le m-1,
\qquad
2u\le r,
\qquad
2v\le r.
\label{eq:guarded-ranges}$$ The orientation multiplicity is $\binom{k}{u}$, and its sign is $$(-1)^{U_0+U_1+U_2}=(-1)^{u+r-v}=(-1)^{r+k}.$$ Hence the exact signed fiber over $(d,k,u,v)$ is $$(-1)^{r+k}
\binom{m-1}{2(m-k)-1}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v}.
\label{eq:signed-fiber}$$ The inequalities $2u,2v\le r$ and $u+v=k$ imply $k\le r$. Summing [\[eq:signed-fiber\]](#eq:signed-fiber){reference-type="eqref" reference="eq:signed-fiber"} and then the three choices of $d$ yields $$\mathcal{C}_{m,j}=3A_{m,r}
\qquad(1\le j\le m).
\label{eq:C-collapse-positive-j}$$ When $j>\lfloor m/2\rfloor$, one has $r=m-j<\lceil m/2\rceil$, so the range is empty and $$\mathcal{C}_{m,j}=0.
\label{eq:C-empty-range}$$

The case $j=0$ is not obtained by silently reusing the preceding classification. Here $r=m$, $s_i=0$, and $T_i=m(1+z_i)$. The nonnegative incoming-transfer patterns are exactly the cyclic permutations of $$(0,m,m)
\qquad\text{and}\qquad
(0,0,2m).
\label{eq:jzero-patterns}$$ For the first type, the unique zero coordinate plays the role of $d$, giving $3A_{m,m}$. For the second type, take $T_0=2m$, $T_1=T_2=0$. The flow equations force $n_0=0$, and at coordinate zero $$N_0=m+1,
\qquad
\lambda_0=m-1,
\qquad
\alpha_0=2m+1.$$ Therefore $$\mathcal{B}(\lambda_0,\alpha_0)
=-\binom{m-1}{2m+1}=0.
\label{eq:jzero-exceptional-vanishing}$$ All three rotations of this exceptional type vanish, and hence $\mathcal{C}_{m,0}=3A_{m,m}$.

Combining [\[eq:D-precollapse\]](#eq:D-precollapse){reference-type="eqref" reference="eq:D-precollapse"}, [\[eq:C-collapse-positive-j\]](#eq:C-collapse-positive-j){reference-type="eqref" reference="eq:C-collapse-positive-j"}--[\[eq:jzero-exceptional-vanishing\]](#eq:jzero-exceptional-vanishing){reference-type="eqref" reference="eq:jzero-exceptional-vanishing"}, and $\mathcal{C}_{m,m+1}=0$ proves $$D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j},
\label{eq:D-certificate-proved}$$ which is [\[eq:D-certificate-main\]](#eq:D-certificate-main){reference-type="eqref" reference="eq:D-certificate-main"}. If $q=\lfloor m/2\rfloor$, define $$E_m=\sum_{j=0}^{q}\binom{m+1}{j}
(2m)^{2(q-j)}A_{m,m-j}.
\label{eq:E-definition}$$ Then $$D_m=3(2m)^{3m+3-2q}E_m.
\label{eq:D-factorization}$$ The derivation proves the certificate for every symbolic $m\ge2$. It does not determine whether $E_m$, and therefore $D_m$, is nonzero in every degree.

# The complete quartic fiber and its exact moment {#sec:quartic}

Let $p$ be a monic-centered quartic and $B_p=\Bbbk[x]/(p)$. At each distinct root $\alpha$ of $p$, the formal fixed trace eigenvalue is $p'(\alpha)$, repeated with local algebra length. Thus the formal fixed-point trace multiset is $0^4$ exactly when every root of $p$ is multiple. The only multiplicity partitions are $4$ and $2+2$.

If $p=(x-\alpha)^4$, centering forces $-4\alpha=0$, so $p=x^4$. If $p=(x-\alpha)^2(x-\beta)^2$, centering gives $2\alpha+2\beta=0$, hence $\beta=-\alpha$ and $$p=(x^2-\alpha^2)^2.$$ Writing $L=\alpha^2$ includes the first case as $L=0$. The coefficient of $x^2$ is $-2L$, so $L$ is unique. This proves the full-fiber classification in [\[thm:quartic\]](#thm:quartic){reference-type="ref" reference="thm:quartic"}.

## Two source-level derivations of the quartic slope {#subsec:quartic-slope}

As an internal source-level cross-check, specialize the all-$m$ certificate: $$H(2,1)=2,
\qquad
A_{2,2}=-2,
\qquad
A_{2,1}=0,$$ which gives $$D_2=3\cdot4^9(-2)=-1572864.
\label{eq:D2-crosscheck}$$ We now derive the same slope without the all-degree collapse.

Put $$P_a(x)=(x^2-a)^2,
\qquad
g_a(x)=x(x^2-a),
\qquad
L_i=x_{i-1}-x_{i+1}.$$ Then $F_i=P_a(x_i)+\varepsilon L_i$, $q_i=4g_a(x_i)$, and $$t_\varepsilon=4^3g_0g_1g_2+4\varepsilon^2(g_0+g_1+g_2).$$ Consequently $$t_\varepsilon^3=\sum_{j=0}^3\binom{3}{j}4^{9-2j}\varepsilon^{2j}G_j,
\qquad
G_j=(g_0g_1g_2)^{3-j}(g_0+g_1+g_2)^j.
\label{eq:quartic-t-cube}$$ Define $$\mathcal{L}_j(a,\varepsilon)=
\left[x_0^{-1}x_1^{-1}x_2^{-1}\right]\frac{G_j}{F_0F_1F_2}.$$ Then $$\mathcal{C}_{2,j}=\left[a^3\varepsilon^{4-2j}\right]\mathcal{L}_j(a,\varepsilon),
\qquad
D_2=\sum_{j=0}^3\binom3j4^{9-2j}\mathcal{C}_{2,j}.
\label{eq:quartic-Cj}$$ Weights show that the selected coefficient is a constant multiple of $a^3$, so set $a=1$. With $P(x)=(x^2-1)^2$ and $g(x)=x(x^2-1)$, expand $$\frac1{P_i+\varepsilon L_i}
=\sum_{h_i\ge0}(-1)^{h_i}\varepsilon^{h_i}
\frac{L_i^{h_i}}{P_i^{h_i+1}}.
\label{eq:quartic-reciprocal}$$ Introduce $$\rho_{n,h}(d)=
\left[x^{-1}\right]\frac{x^d g(x)^n}{P(x)^{h+1}}
\qquad(d\ge0).$$ The identities $$\frac{g^3}{P}=x^3(x^2-1),
\qquad
\frac{g^3}{P^2}=\frac{x^3}{x^2-1},
\qquad
\frac{g^3}{P^3}=\frac{x^3}{(x^2-1)^3}$$ give $$\begin{aligned}
\rho_{3,0}(d)&=0 &&(d\ge0),\\
\rho_{3,1}(0)&=\rho_{3,1}(2)=1,
&\rho_{3,1}(1)&=0,\\
\rho_{3,2}(0)&=\rho_{3,2}(1)=0,
&\rho_{3,2}(2)&=1.\end{aligned}$$

For $j=0$, the total internal denominator order is $h_0+h_1+h_2=4$. The first vanishing forces every $h_i\ge1$, leaving only the three cyclic arrangements of $(2,1,1)$. For $(h_0,h_1,h_2)=(2,1,1)$, the tensor coefficient is $$(\rho_{3,2}\otimes\rho_{3,1}\otimes\rho_{3,1})(L_0^2L_1L_2).$$ Since $$L_0=x_2-x_1,
\quad L_1=x_0-x_2,
\quad L_2=x_1-x_0,$$ we have $L_1L_2=-x_0^2+x_0(x_1+x_2)-x_1x_2$. Extracting the $x_0$-coefficient leaves $-(x_2-x_1)^2$, and the remaining two coefficients give $-2$. The other cyclic arrangements agree, and the total sign is $(-1)^4=1$. Hence $$\mathcal{C}_{2,0}=-6.
\label{eq:C20}$$

For $j=1$, each monomial of $G_1$ has coordinate powers $g^3,g^2,g^2$, but the total internal denominator order is only two. A coordinate with $h_i=0$ contributes either $g^2/P=x^2$ or $g^3/P=x^3(x^2-1)$, both polynomials, so no $x_i^{-1}$-term can occur. Nonvanishing would require all three $h_i\ge1$, a contradiction. Thus $\mathcal{C}_{2,1}=0$.

For $j=2$, the internal $\varepsilon$-degree is zero. If $$\mu_n=\left[x^{-1}\right]\frac{g(x)^n}{P(x)},$$ then $\mu_1=1$, $\mu_2=\mu_3=0$. The square terms of $G_2$ have type $(3,1,1)$, and its cross terms have type $(2,2,1)$; their tensor coefficients vanish as $\mu_3\mu_1^2$ and $\mu_2^2\mu_1$. Hence $\mathcal{C}_{2,2}=0$. The $j=3$ summand already contains $\varepsilon^6$ and cannot contribute to $\varepsilon^4$. Equation [\[eq:quartic-Cj\]](#eq:quartic-Cj){reference-type="eqref" reference="eq:quartic-Cj"} now gives $$D_2=4^9(-6)=-1572864
\label{eq:D2-direct}$$ without using the all-degree binomial collapse.

## A direct normal-form ledger for the constant {#subsec:quartic-constant}

Set $a=0$ and $\varepsilon=1$. Then $$F_i=x_i^4+x_{i-1}-x_{i+1},
\qquad
t=64x_0^3x_1^3x_2^3+4(x_0^3+x_1^3+x_2^3).$$ Let $R(e_0,e_1,e_2)$ be the coefficient of $x_0^3x_1^3x_2^3$ in the normal form of $x_0^{e_0}x_1^{e_1}x_2^{e_2}$. Reduction in the three coordinates gives $$\begin{aligned}
R(e_0,e_1,e_2)
&=R(e_0-4,e_1+1,e_2)-R(e_0-4,e_1,e_2+1),\\
R(e_0,e_1,e_2)
&=-R(e_0+1,e_1-4,e_2)+R(e_0,e_1-4,e_2+1),\\
R(e_0,e_1,e_2)
&=R(e_0+1,e_1,e_2-4)-R(e_0,e_1+1,e_2-4).
\end{aligned}
\label{eq:quartic-R}$$ The terminal value is $R(3,3,3)=1$, and every other standard exponent triple has value zero. The complete ledger needed for $t^3$ is

  Exponent pattern                   $R$-value
  --------------------------------- -----------
  $(9,9,9)$                            $-6$
  cyclic permutation of $(9,6,6)$       $2$
  cyclic permutation of $(9,3,3)$       $0$
  cyclic permutation of $(6,6,3)$      $-1$
  permutation of $(9,0,0)$              $0$
  permutation of $(6,3,0)$              $0$
  $(3,3,3)$                             $1$

For example, $$R(9,6,6)=R(5,7,6)-R(5,6,7)=1-(-1)=2,$$ and $$R(9,9,9)=2R(5,10,9)=2(1-4)=-6.$$ The remaining rows require at most two reductions or have total degree nine without already being the top standard monomial.

Put $Q=64x_0^3x_1^3x_2^3$ and $R_0=4(x_0^3+x_1^3+x_2^3)$. Grouping $(Q+R_0)^3$ by the preceding patterns gives

  Source                             Top-coefficient contribution
  --------------------------------- ------------------------------
  $Q^3$                                 $262144(-6)=-1572864$
  $3Q^2R_0$                           $3\cdot49152\cdot2=294912$
  square terms in $3QR_0^2$                      $0$
  mixed terms in $3QR_0^2$             $3\cdot6144(-1)=-18432$
  pure and $2+1$ terms in $R_0^3$                $0$
  fully mixed term in $R_0^3$                   $384$

Therefore $$C_2=-1572864+294912-18432+384=-1296000.
\label{eq:C2-direct}$$ Combining [\[eq:D2-direct\]](#eq:D2-direct){reference-type="eqref" reference="eq:D2-direct"} and [\[eq:C2-direct\]](#eq:C2-direct){reference-type="eqref" reference="eq:C2-direct"} proves [\[eq:quartic-moment-main\]](#eq:quartic-moment-main){reference-type="eqref" reference="eq:quartic-moment-main"}. Both computations are derivations inside the source proof: [\[eq:D2-crosscheck\]](#eq:D2-crosscheck){reference-type="eqref" reference="eq:D2-crosscheck"} is a specialization of the all-degree theorem, while [\[eq:D2-direct\]](#eq:D2-direct){reference-type="eqref" reference="eq:D2-direct"}--[\[eq:C2-direct\]](#eq:C2-direct){reference-type="eqref" reference="eq:C2-direct"} use the separate tensor-Laurent and normal-form routes.

# Fixed moment, local multiplicity, and minimality {#sec:minimality}

The next two lemmas have different conclusions and are used in that order.

[\[lem:fixed-moment\]]{#lem:fixed-moment label="lem:fixed-moment"} On the fixed algebra [\[eq:fixed-algebra\]](#eq:fixed-algebra){reference-type="eqref" reference="eq:fixed-algebra"}, the fixed contribution to the formal period-three $m$-th trace moment is zero for every $m\ge2$.

All three cyclic coordinates agree on the fixed algebra, so $$t_\varepsilon=q^3+3\varepsilon^2q.$$ Since $q^2=0$, $$(q^3+3\varepsilon^2q)^m=0
\qquad(m\ge2).$$ At $\varepsilon=1$, this is the fixed contribution to the trace of $(Df^3)^m$. Hence the formal exact-period-three moment equals the raw $f^3$-fixed moment $S_m(a,1)$ after subtracting a zero fixed moment.

[\[lem:fixed-multiplicity\]]{#lem:fixed-multiplicity label="lem:fixed-multiplicity"} Let $\alpha$ be a root of $p$ of multiplicity $r\ge2$. The local length of $\mathop{\mathrm{Fix}}(f^3)$ at the associated fixed point equals $r$, the fixed-scheme length at $\alpha$.

Set $$\delta=x_0-\alpha,
\qquad
u=x_1-x_0,
\qquad
v=x_2-x_0.$$ At $(\delta,u,v)=(0,0,0)$, the $(u,v)$-Jacobian of $(F_1,F_2)$ is $$\begin{pmatrix}0&-1\\1&0\end{pmatrix},$$ which is invertible. Formal elimination therefore gives $$u=-p(\alpha+\delta)+O(\delta^{2r-1}),
\qquad
v=p(\alpha+\delta)+O(\delta^{2r-1}).$$ The remaining equation is $$F_0=p(\alpha+\delta)+v-u
=3p(\alpha+\delta)+O(\delta^{2r-1}).
\label{eq:local-fixed-equation}$$ Because $2r-1>r$ and the characteristic is zero, the order of [\[eq:local-fixed-equation\]](#eq:local-fixed-equation){reference-type="eqref" reference="eq:local-fixed-equation"} is exactly $r$. This is the local length of $\mathop{\mathrm{Fix}}(f^3)$ at the fixed support.

is a statement about a trace power, while [\[lem:fixed-multiplicity\]](#lem:fixed-multiplicity){reference-type="ref" reference="lem:fixed-multiplicity"} is a statement about scheme length. The first does not imply the second. In particular, zero fixed moment is never used as a shortcut for subtracting reduced fixed support.

For the quartic fiber, the $f^3$-fixed algebra has length $4^3=64$. By [\[lem:fixed-multiplicity\]](#lem:fixed-multiplicity){reference-type="ref" reference="lem:fixed-multiplicity"}, the fixed algebra contributes its full length $4$, so the formal exact-period-three zero-cycle has length $$64-4=60.
\label{eq:exact-length-60}$$ Every exact period-three orbit contains three points, and matrix trace is cyclically invariant along the orbit. Only after the pointwise exact-period subtraction do we divide by three: $$\frac{-1296000-1572864L^3}{3}
=-432000-524288L^3.
\label{eq:cyclewise-moment}$$

The normalized conjugacy calculation from [4](#sec:low-periods){reference-type="ref" reference="sec:low-periods"}, with $m=2$, gives $$f_{2,L}\sim f_{2,M}
\quad\Longleftrightarrow\quad
L^3=M^3.$$ The coefficient of $L^3$ in [\[eq:quartic-moment-main\]](#eq:quartic-moment-main){reference-type="eqref" reference="eq:quartic-moment-main"} is nonzero. Hence the period-three moment separates precisely the normalized conjugacy classes on the complete quartic fiber. Periods one and two are constant there, so period three is minimal. This proves [\[thm:quartic\]](#thm:quartic){reference-type="ref" reference="thm:quartic"}.

# Scope, open problem, and proof provenance {#sec:scope}

## The open coefficient problem

The formula [\[eq:D-certificate-proved\]](#eq:D-certificate-proved){reference-type="eqref" reference="eq:D-certificate-proved"} reduces all-degree period-three recovery to a concrete combinatorial question: $$D_m\stackrel{?}{\ne}0
\qquad\text{for every }m\ge2.
\label{eq:open-nonvanishing}$$ No degree-independent sign, positivity, or nonvanishing proof is known in the present argument. Consequently [\[thm:uniform\]](#thm:uniform){reference-type="ref" reference="thm:uniform"} proves an affine two-term law and an exact slope certificate, but it does not prove that period three separates the family in every degree.

## Nonclaims

To make the theorem boundary explicit, this note does not claim any of the following:

-   universal nonvanishing of $D_m$, or all-degree period-three separation;

-   a theorem for all quartic Hénon maps, a global degree-four period cutoff, a global conjugacy classification, or global multiplier rigidity;

-   discovery of the exceptional quartic family or of its period-one/two blindness;

-   novelty of global residues, quotient traces, formal/dynatomic cycles, or low-period Hénon algebra;

-   a historical-priority conclusion from a bounded no-hit search;

-   an unstable- or saddle-multiplier theorem, an arithmetic height or finiteness result, a prime/zero statement, or a transfer-, Fredholm-, or Euler-product identity; or

-   an all-$m$ inference from any finite diagnostic or development calculation.

## Proof and process provenance

Every theorem claim in this note is derived from the source-locked proof package with SHA-256

`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`.

That package received the independent source verdict `SOURCE_LOCK_PASS` in the review with SHA-256

`5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11`.

No theorem in this note uses registered computational evidence.

The sole earlier registered audit was consumed and ended `REGISTERED_AUDIT_TERMINAL_FAIL`; no rerun is permitted, no raw result exists, and no result gate passed. Static forensic analysis attributes the failure with approximate confidence $0.98$ to a deterministic Track-Q scalar-versus-pair endpoint defect, but the child stderr was not preserved. No scientific mismatch was recorded, and that absence is not evidence of agreement. This disclosure is non-evidentiary and supplies no support for any theorem above.

The historical positioning is equally bounded. Cantat--Dujardin already supply the quartic family and its period-one/two blindness; Friedland--Milnor supply the normalized Hénon framework; and multidimensional residues, quotient traces, and formal periodic cycles are prior methods. The contribution claimed here is limited to the source-proved period-three law and coefficient certificate and the scoped quartic minimal-separator theorem. The bounded literature search is not a proof of historical priority.

# Conclusion {#sec:conclusion}

The exceptional family $f_{m,a}(x,y)=(y+(x^m-a)^2,x)$ is formally blind at periods one and two, yet its period-three trace residue has a rigid two-term dependence on the normalized coordinate $a^{2m-1}$. A complete Laurent fiber calculation turns the slope into the finite certificate [\[eq:D-certificate-proved\]](#eq:D-certificate-proved){reference-type="eqref" reference="eq:D-certificate-proved"}. In degree four, the complete normalized fiber with formal fixed-point trace multiset $0^4$ is $p=(x^2-L)^2$, and its exact affine period-three moment recovers $L^3$. The separate local-multiplicity argument shows that the exact-period scheme has length $60$, so the pointwise and cyclewise normalizations are both controlled.

The quartic theorem is complete within its stated fiber. The uniform theorem ends at a sharper frontier: proving or disproving $D_m\ne0$ in every degree is an explicit open combinatorial problem.
