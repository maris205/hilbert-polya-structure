---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c421-integral-return"
canonical_tex: "henon_dynamics/research_c419_c423/papers/C421_integral_return/main.tex"
canonical_pdf: "henon_dynamics/research_c419_c423/papers/C421_integral_return/main.pdf"
source_sha256: "8d7cd8949cd8b635705b1f451a372286899f477904abf5b2a7e4f4a1b94995dd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Integral periodic orbits of a cubic three-term recurrence

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c419_c423/papers/C421_integral_return>)
- [规范 TeX](<../../../../../henon_dynamics/research_c419_c423/papers/C421_integral_return/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c419_c423/papers/C421_integral_return/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c419_c423/papers/C421_integral_return/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c419_c423/papers/C421_integral_return/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify every integral periodic orbit of $T_a(x,y,z)=(y,z,yz+a-x)$ for every integer $a$. The answer consists of eight explicitly parametrized families and two sporadic orbits, with least periods exactly $1,2,3,4,5,6,8,9,12$. The proof is computer-assisted, but its reduction is uniform in the parameter, invariant level and period. For a periodic scalar sequence, the two-step differences satisfy a linear identity in which the forcing parameter cancels. Extremal differences isolate the unbounded families; every remaining orbit has maximum difference at most $100$ and all coordinates between $-301$ and $299$. A terminating exact certificate exhausts that residual set without a period cutoff. An independently organized, inverse-time, two-sign enumeration agrees on all $25\,851$ oriented cycles in the finite certificate. We resolve all least-period degeneracies and cyclic identifications, and give finite square tests for the number of oriented cycles on each integral invariant level. These yield the exact ordinary fixed-point counts and a finite rational dynamical zeta product. The classical unforced families and the earlier unforced integral classification are explicitly excluded from the contribution claimed here.
author:
- Anonymous
bibliography:
- references.bib
date: 8 September 2026
title: 'Integral periodic orbits of a cubic three-term recurrence'
```

## Markdown 正文

# Introduction {#sec:introduction}

Consider the polynomial automorphism $$T_a(x,y,z)=(y,z,yz+a-x),\qquad a\in\mathbb Z.
 \label{eq:map}$$ We ask for every periodic point in $\mathbb Z^3$, with one application of $T_a$ as one time step. The forcing parameter is arbitrary and is held fixed along the orbit. A classification of short returns in chosen boxes would not answer this question: both the parameter and the height of periodic points are unbounded. In fact, there are infinitely many four-cycles for each fixed parameter when the invariant level is allowed to vary.

The main result gives a disjoint list of all oriented cycles. Its proof has two parts. First, a two-step difference identity removes $a$ from the local growth constraints. A large coordinate then forces a four-cycle, while a large extremal difference leaves only five possible central coordinates. Their exact analysis extracts the other unbounded families. Second, the remaining difference and height bounds define a finite seed problem. Exact iteration from each seed stops at an exit or a first return by finiteness and injectivity; no maximum period is imposed. The two sporadic cycles are the remainder after the complete finite output is matched with the symbolic families. The finite computation is a proof component, not empirical support for a conjectured bound.

#### Prior work and the precise scope of the increment.

The ambient cubic surfaces and their Vieta-type automorphisms are classical. Under $(X,Y,Z)=(-x,-y,-z)$ the invariant equation becomes $$X^2+Y^2+Z^2+XYZ=-a(X+Y+Z)+k,$$ a specialization of the standard character-variety cubic family studied by @cantatLoray2009. For $a=0$, the map is the Fibonacci trace map in full-trace coordinates. Its invariant, reversibility, and explicit periodic families are part of the trace-map theory of @robertsBaake1994; general escape mechanisms for unforced trace maps are developed by @roberts1996. We do not claim these structures, the known four-step family, or the unforced periodic families as new. The anonymous predecessor [@priorIntegralTrace] already gives the complete integral classification at $a=0$; that entire subcase is likewise deducted here. None of its proof is needed as an unprinted lemma in the argument below.

Other trace-map finiteness questions have different quantifiers. The finite-orbit results for character-variety group actions in @cantatLoray2009, and the comparison between finite group orbits and periodicity under every group element in @humphries2016, do not directly classify integer periodic points of this one specified map. The versioned Cantat--Loray preprint used for the group-action comparison is [arXiv:0711.1579v2](https://arxiv.org/abs/0711.1579v2); its Theorem C is not cited as a theorem number of the shorter journal layout. Hone's related third-order recurrence [@hone2006 Proposition 1] has a parameter multiplying the product term, rather than the additive forcing in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. These related settings motivate the methods but do not replace the all-forcing exhaustion proved here.

The contribution is the uniform extremal-difference reduction, its complete residual certificate, and the resulting all-parameter oriented classification and level counts. We make no worldwide priority claim. Table [1](#tab:ownership){reference-type="ref" reference="tab:ownership"} records the scope distinctions that matter to the theorem.

::: {#tab:ownership}
  ----------------------------------------------------------------------------------------------------------------------------------------------------
  Input or related setting              Scope retained or distinguished
  ------------------------------------- --------------------------------------------------------------------------------------------------------------
  Classical cubic and trace maps        Ambient cubic, reversibility, unforced families, four-step family and escape framework are prior structures.

  Unforced integral predecessor         The complete $a=0$ classification is already established; it is reproved where needed here.

  Whole-group finite orbits             A group orbit, or periodicity under every group element, is not periodicity under one fixed $T_a$.

  Multiplicative-parameter recurrence   Its product coefficient is not the additive integer forcing $a$.

  Present theorem                       Every integer $a$, every height and period; all oriented cycles and exact invariant-level multiplicities.
  ----------------------------------------------------------------------------------------------------------------------------------------------------

  : Source scope and the additional question answered here. The distinctions concern the object and quantifiers, not a priority ranking. All present counts use ordinary integer points and the specified map's time step.
:::

#### Organization.

Section [2](#sec:classification){reference-type="ref" reference="sec:classification"} states the full list. Sections [3](#sec:differences){reference-type="ref" reference="sec:differences"} and [4](#sec:large){reference-type="ref" reference="sec:large"} prove the uniform analytic reduction. Section [5](#sec:finite){reference-type="ref" reference="sec:finite"} specifies and justifies both exact finite certificates. Section [6](#sec:least){reference-type="ref" reference="sec:least"} verifies least periods and representatives, and Section [7](#sec:counts){reference-type="ref" reference="sec:counts"} derives the arithmetic level tests. The complete primary certifier and evidence identifiers are included in Appendix [9](#app:certificate){reference-type="ref" reference="app:certificate"}.

# The complete classification {#sec:classification}

The inverse and a polynomial invariant of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} are $$\begin{aligned}
 T_a^{-1}(x,y,z)&=(xy+a-z,x,y), \label{eq:inverse}\\
 K_a(x,y,z)&=x^2+y^2+z^2-xyz-a(x+y+z).
 \label{eq:invariant}\end{aligned}$$ The inverse identity is immediate. For invariance, put $w=yz+a-x$. The difference $K_a(y,z,w)-K_a(x,y,z)$ factors as $(w-x)(w+x-yz-a)=0$.

A repeated word $w=(w_0,\ldots,w_{\ell-1})$ encodes the consecutive triples $(w_i,w_{i+1},w_{i+2})$. These form an orbit, with indices modulo $\ell$, provided $$w_{i+3}=w_{i+1}w_{i+2}+a-w_i
 \quad\text{for every }i\pmod\ell.
 \label{eq:scalar}$$ Conversely every periodic triple orbit has this encoding. Its least scalar period equals the first-return time of a triple: a repeated triple determines the entire forward and backward sequence by [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} and [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}. An *oriented cycle* is an orbit under forward iteration. Cyclic rotations represent the same cycle. We do not identify a word with its reverse unless those two words are cyclic rotations.

[\[thm:classification\]]{#thm:classification label="thm:classification"} For every $a\in\mathbb Z$, all periodic points of $T_a$ in $\mathbb Z^3$ are the consecutive triples of precisely the words in Table [2](#tab:classification){reference-type="ref" reference="tab:classification"}. The indicated parameter ranges give one representative per oriented cycle, with exactly the stated least period and invariant level. The table includes singular points of every level surface.

::: {#tab:classification}
  ----------------------------------------------------------------------------------------------------------------
   $\ell$  Word and parameter range                                                            $k$
  -------- ----------------------------------------------------------------------------------- -------------------
   $\ell$  Word and parameter range                                                            $k$

           $F_1:(r)$; $r\in\mathbb Z$, $a=2r-r^2$                                              $r^2(2r-3)$

     2     $F_2:(u,v)$; $u<v$, $a=u+v-uv$                                                      $uv(u+v-3)$

     3     $F_3:(-2,-2,t)$; $a=2t-4$, $t\ne-2$                                                 $8-(t-4)^2$

     4     $F_4:(-1,t,-1,a+1-t)$; $2t<a+1$                                                     $t^2-(a+1)t+2a+2$

     5     $F_5:(-1,t,0,0,-1-t)$; $a=-1$, $t\in\mathbb Z\setminus\{-1\}$                       $t(t+1)$

     5     $E_5:(-4,-2,-3,-3,-2)$; $a=-13$                                                     $-64$

     6     $F_6:(0,0,t,0,0,-t)$; $a=0$, $t\ge1$                                                $t^2$

     8     $F_8:(-1,t,1,t,-1,-t-2,1,-t-2)$; $a=-1$, $t\ge0$                                    $(t+1)^2+1$

     9     $E_9:(-2,-1,0,0,-1,-2,0,-1,0)$; $a=-2$                                              $-1$

     12    $F_{12}:(1,m,1,m-1,-1,-m,$ $\phantom{F_{12}:(}1,1-m,1,-m,-1,m-1)$; $a=0$, $m\ge1$   $m^2-m+2$
  ----------------------------------------------------------------------------------------------------------------

  : Complete disjoint list of oriented integral cycles. Every displayed word is repeated. The range conditions remove cyclic duplications and shorter-period cases; reversal is not an additional quotient. The symbol $k$ denotes $K_a$.
:::

There are eight parametric rows and two sporadic rows. The labels $F_\ell$ denote the parametric families and $E_5,E_9$ the two exceptions. In particular, the set of possible least periods is $$\mathcal L=\{1,2,3,4,5,6,8,9,12\}.
 \label{eq:periodset}$$ Each length actually occurs: one may take $r=0$ in $F_1$, $(u,v)=(0,1)$ in $F_2$, $t=0$ in $F_3$, $(a,t)=(0,0)$ in $F_4$, $t=0$ in $F_5$, $t=1$ in $F_6$, $t=0$ in $F_8$, the word $E_9$, and $m=1$ in $F_{12}$. Thus $T_a^{360}$ fixes the integral periodic locus for each $a$. This is not a finite-order assertion about $T_a$ on its full phase space.

The theorem's exhaustion is computer-assisted: the analytic part reduces every unlisted cycle to a proved finite core, whose complete exact evaluation is described in Section [5](#sec:finite){reference-type="ref" reference="sec:finite"}. All existence, period and overlap statements for the infinite families are polynomial or finite-word arguments and apply outside that core as well.

# A parameter-free difference identity {#sec:differences}

Let $(x_i)_{i\in\mathbb Z}$ be a periodic integral sequence satisfying [\[eq:scalar\]](#eq:scalar){reference-type="eqref" reference="eq:scalar"}. Define $$d_i=x_{i+2}-x_i,\qquad D=\max_i|d_i|.
 \label{eq:difference}$$ Subtract the recurrence at $i-1$ from that at $i$. It gives $$d_{i-1}+d_{i+1}=(x_{i+1}+1)d_i,
 \qquad |(x_{i+1}+1)d_i|\le2D.
 \label{eq:key}$$ The forcing cancels. Two adjacent zero differences force all differences to be zero, by propagation of [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} in both directions.

Reversal of a scalar sequence preserves [\[eq:scalar\]](#eq:scalar){reference-type="eqref" reference="eq:scalar"}. On triples it is the actual reversing involution $$R(x,y,z)=(z,y,x),\qquad RT_aR=T_a^{-1}.
 \label{eq:reversor}$$ We use this symmetry to normalize an extremum, but restore both time orientations at the end.

[\[lem:zero\]]{#lem:zero label="lem:zero"} If $D=0$, the scalar sequence alternates two integers $u,v$ and $$a=u+v-uv=1-(u-1)(v-1).
 \label{eq:alternating}$$ It is fixed when $u=v$ and otherwise has least period two.

The equation $d_i=0$ is $x_{i+2}=x_i$. Substitution of $(u,v,u,v,\ldots)$ into the recurrence is equivalent to [\[eq:alternating\]](#eq:alternating){reference-type="eqref" reference="eq:alternating"}. The assertion about the least period follows directly.

[\[lem:height\]]{#lem:height label="lem:height"} If $D>0$ and $|x_j+1|>3D$ at some phase, the orbit is a word of the form $(-1,t,-1,a+1-t)$ repeated. Consequently, every orbit not of this form satisfies $$|x_i+1|\le3D\quad\text{for all }i.
 \label{eq:heightbound}$$

Rotate to $j=1$. Integrality in [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} forces $d_0=0$. Put $x_0=x_2=b$, $x_1=m$, and $e=d_1=-d_{-1}$. We have $e\ne0$, since two adjacent zero differences would give $D=0$, and $|e|\le D$. Moreover, $x_{-1}=x_3=m+e$; in particular the sign in both of these expressions is the same. Thus $|x_{-1}+1|,|x_3+1|>2D$, forcing $d_{-2}=d_2=0$ by [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"}. Its equation at $i=1$ is now $(b+1)e=0$, so $b=-1$. Direct use of the scalar recurrence yields $(-1,m,-1,a+1-m)$ repeated. Conversely this word satisfies every recurrence equation. Its period is four unless $2m=a+1$, when it is alternating (and fixed if also $m=-1$).

# Exhaustion when the maximum difference is large {#sec:large}

[\[prop:large\]]{#prop:large label="prop:large"} Every integral periodic sequence with $D>100$ is one of the families $F_3,F_4,F_5,F_6,F_8,F_{12}$, allowing the shorter-period degeneracies before choosing the ranges in Table [2](#tab:classification){reference-type="ref" reference="tab:classification"}.

Choose a phase and initially reverse if necessary so that $d_0=D>0$. Write $$(x_0,x_1,x_2)=(u,s,v),\quad v-u=D,\quad
 p=d_{-1}=v-su+s-a,\quad q=d_1=sv+a-u-s.
 \label{eq:extremal}$$ Equation [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} gives $$s\in\{-3,-2,-1,0,1\},\qquad
 p+q=(s+1)D,\qquad |p|,|q|\le D.
 \label{eq:fivecenters}$$ All bounds below are consequences of the global maximum $D$; a violation excludes a periodic sequence, not just a sampled initial condition.

## The endpoint centers

If $s=1$, then $p=q=D$, and [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} gives $d_{-2}=uD$, $d_2=vD$. Hence $u,v\in[-1,1]$, implying $D\le2$, a contradiction. If $s=-3$, then $p=q=-D$ and $d_{-2}=-(u+2)D$, $d_2=-(v+2)D$. Now $u,v\in[-3,-1]$, giving the same contradiction.

## The center $s=-1$

Set $E=u+v-a-1$, so $p=E$ and $q=-E$. We have $$d_{-2}=(u+1)E-D,\qquad d_2=-(v+1)E-D.$$ Their bounds imply $(u+1)E\ge0$ and $(v+1)E\le0$. Since $u<v$, the case $E>0$ is impossible. If $E=0$, the recurrence is the four-step word $F_4$ (up to rotation). Otherwise write $E=-\kappa$, with $\kappa\in\mathbb Z_{>0}$. Then $$u\le-1\le v,\quad
 \kappa(-u-1)\le2D,\quad \kappa(v+1)\le2D.$$ Adding the latter inequalities gives $\kappa\le4$. Both $x_{-1}$ and $x_3$ equal $\kappa-1$, and one more application of [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} gives $$d_{-3}+d_3=\kappa(\kappa-2)D.$$ Its absolute value is at most $2D$, excluding $\kappa=3,4$.

For $\kappa=1$ we have $a=u+v$, $x_{-1}=x_3=0$, $d_{-3}=-v$ and $d_3=u$. The centers of these differences are both $a+1$, so $$|a+2|\max(|u|,|v|)\le2D.$$ Since the maximum is at least $D/2$, it follows that $-6\le a\le2$. The forward sequence begins $$u,-1,v,0,a+1,u,(a+1)u+a,(a+1)u^2+au-1.$$ Consequently $d_5=(a+1)u^2+(a-1)u-1$. If $a\ne-1$, put $U=|u|$. As $u=(a-D)/2<0$, we have $U>49$ and $D\le2U+6$, while $$|d_5|\ge U^2-7U-1>2U+6\ge D,$$ a contradiction. If $a=-1$, the repeated word is $(u,-1,-1-u,0,0)$, a rotation of $F_5$.

For $\kappa=2$ we have $a=u+v+1$, $d_{-3}=-2a$ and $d_3=2a$, with centers $u+a+1$ and $v+a+1$. Applying [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} at these centers gives $$|2a(u+a+2)|\le2D,\qquad |2a(v+a+2)|\le2D.$$ The shifted coefficients differ by $D$, so one has absolute value at least $D/2$. Hence $|a|\le2$, including $a=0$. The forward sequence begins $$u,-1,v,1,v+a+1,2a+1,(v+a+1)(2a+1)+a-1,$$ and hence $$d_4=2a(v+a+1)+a-1,\qquad D=2v-a+1,\qquad v>48.$$ For $a=1$ we obtain $d_4=D+4$. For $a=2$ we obtain $d_4=4v+13>D$, and for $a=-2$ we obtain $|d_4|=4v-1>D=2v+3$. All are impossible. For $a=-1$ direct iteration gives $F_8$; for $a=0$ it gives $F_{12}$. In the latter case $u=-1-v$ and $m=v+1>0$; the triple $(u,-1,v)$ occurs starting at position $9$ of the displayed $F_{12}$ word, with zero-based indices.

## The signed normalization at $s=0,-2$

For either remaining center, $|p+q|=D$, so at least one of $|p|,|q|$ is at least $D/2$. Reverse if needed to arrange $|p|\ge D/2$. This second reversal can change the extremum's sign. We therefore write $$d_0=\varepsilon L,\quad L=D>100,\quad
 \varepsilon\in\{-1,1\},\quad v=u+\varepsilon L.
 \label{eq:signed}$$ The bound at $p$ gives $|u+1|\le4$, so $-5\le u\le3$. Since $|v+1|\ge L-6$, the bound at $q$ gives $|q|\le2L/(L-6)<3$. Keeping $\varepsilon$ in the next two cases is essential.

## The center $s=0$

Here $p+q=\varepsilon L$, so $p,q$ have sign $\varepsilon$ or are zero. Write $q=\varepsilon r$, $r\in\{0,1,2\}$. Then $a=u+\varepsilon r$, $x_3=\varepsilon r$, and $$d_2=(v+1)\varepsilon r-\varepsilon L.$$ If $\varepsilon=-1$ and $r\ge1$, this is $(r+1)L-r(u+1)>L$, a contradiction. If $\varepsilon=1,r=2$, it is $L+2u+2\ge L-8$, with center $x_3=2$. Equation [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} would require $3(L-8)\le2L$, again impossible.

If $\varepsilon=1,r=1$, put $a=u+1$, so $-4\le a\le4$. We obtain $d_2=a$, $d_3=2a-1$, with the latter center $x_4=L+2a-1$. Thus $$|(L+2a)(2a-1)|\le2L.$$ For an integer $a\notin\{0,1\}$ the left side is at least $3(L-8)>2L$. If $a=1$, the initial triple is $(0,0,L)$, and $x_4=L+1$, $x_6=2L+2$, so $d_4=L+1>D$. If $a=0$, the initial triple is $(-1,0,L-1)$, and $x_7=1-L$, $x_9=1-(L-1)^2$, giving $d_7=-L^2+3L-1$ of magnitude greater than $L$.

Only $r=0$ remains. Now $a=u$, $x_3=0$, $x_4=u$, $x_5=-\varepsilon L$, and $d_2=d_3=-\varepsilon L$. The bound at $d_3$ gives $-3\le u\le1$. Also $d_4=-u\varepsilon L$, centered at $x_5=-\varepsilon L$. Since $L>100$, the inequality $|(-\varepsilon L+1)u\varepsilon L|\le2L$ forces $u=0$. Hence $a=0$ and the word is $F_6$.

## The center $s=-2$

Here $p+q=-\varepsilon L$, so write $q=-\varepsilon r$, $r\in\{0,1,2\}$. Then $$d_2=-rL-\varepsilon\bigl(r(u+1)+L\bigr).$$ For $\varepsilon=1,r\ge1$ this is at most $-(r+1)L+4r<-L$. Consider $\varepsilon=-1$. Then $q=r$, $v=u-L$, $a=2v+u+r-2$, $x_3=r-2$, and $x_4=rv+u+r$.

If $r=2$, we have $x_4=2v+u+2$, $x_5=v+u$, $a=2v+u$, and $d_4=x_4x_5+a-x_4$. Using $|u|\le5$ gives the conservative estimate $$|d_4|\ge(2L-17)(L-10)-4L-32>L
 \qquad(L>100),$$ a contradiction. If $r=1$, the next entries are $$\begin{aligned}
 x_3&=-1,&x_4&=v+u+1,&x_5&=-2,\\
 x_6&=-u-2,&x_7&=v+2u+2,&
 x_8&=-uv-2u^2-5u-3.\end{aligned}$$ Thus $d_5=-L+3u+4$, centered at $-u-2$. For $u\in[-5,3]\setminus[-3,1]$, $|(u+1)d_5|\ge3(L-13)>2L$, impossible. For $-3\le u\le1$, the difference $d_6=uL-3u^2-4u-1$ has center $x_7=-L+3u+2$. Its bound implies $$|d_6|\le\frac{2L}{L-6}<3.$$ If $u\ne0$, then $|d_6|\ge L-16>2$, contradicting integrality and this strict bound. For $u=0$, direct iteration instead gives $d_7=2L-7>L$.

Only $r=0$ remains, for either sign. Now $$\begin{gathered}
 a=2v+u-2,\quad x_3=-2,\quad x_4=u,\quad
 x_5=\varepsilon L-2,\\
 d_2=-\varepsilon L,\quad d_3=\varepsilon L,
 \quad d_4=(u+2)\varepsilon L.\end{gathered}$$ The bound for $d_4$ at center $x_5$ forces $u=-2$. The resulting word is $(-2,-2,t)$ with $a=2t-4$, namely $F_3$.

## Restoring orientation and concluding the reduction

At the centered triple, reversal sends $(d_0,p,q)$ to $(-d_0,-q,-p)$, exactly the rule used in [\[eq:signed\]](#eq:signed){reference-type="eqref" reference="eq:signed"}. Reversing $F_3,F_4,F_6,F_8$ or $F_{12}$ gives a rotation of the same word. For the form $(u,-1,-1-u,0,0)$ of $F_5$, the reverse is a rotation of $(-1-u,-1,u,0,0)$, which is also included as the parameter ranges over all integers. Alternating words are reversal-closed as well. Thus normalization has not lost an oriented orbit. This completes the proof of Proposition [\[prop:large\]](#prop:large){reference-type="ref" reference="prop:large"}.

[\[cor:core\]]{#cor:core label="cor:core"} Every integral periodic orbit is either an alternating word, one of $F_3,F_4,F_5,F_6,F_8,F_{12}$, or satisfies $$1\le D\le100,\qquad -3D-1\le x_i\le3D-1
 \quad\text{at every phase}.
 \label{eq:core}$$ In particular the residual coordinates belong to $[-301,299]$.

Apply Lemma [\[lem:zero\]](#lem:zero){reference-type="ref" reference="lem:zero"}, Proposition [\[prop:large\]](#prop:large){reference-type="ref" reference="prop:large"}, and then Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} outside $F_4$.

# A terminating finite certificate {#sec:finite}

For an orbit remaining after the listed channels have been removed, the bound $D\le100$ is now a theorem, not a search parameter. This section specifies the complete finite task and records its accepted exact evaluation. The two enumerations were performed in the proof stage; they were not rerun merely to prepare this article. Appendix [9](#app:certificate){reference-type="ref" reference="app:certificate"} prints the primary implementation and identifies the preserved source and output files.

## The forward, positive-extremum algorithm

For each integer $D\in[1,100]$ put $$b_-=-3D-1,\qquad b_+=3D-1.$$ Perform the following finite loops and exact orbit walks.

1.  For every integer $u\in[b_-,b_+-D]$ and every $s\in\{-3,-2,-1,0,1\}\cap[b_-,b_+]$, put $v=u+D$. For every integer $p\in[-D,D]$, put $q=(s+1)D-p$. Retain the seed precisely when $$|q|\le D,\qquad |(u+1)p|\le2D,\qquad
     |(v+1)q|\le2D.
     \label{eq:seedbounds}$$ Set $a=v-su+s-p$ and the starting triple $P=(u,s,v)$. The code intersects the corresponding integer $p$ intervals before entering their innermost loop; this is exactly the same finite set.

2.  Keep this $a,D$ fixed. At the current state $(x,y,z)$, test first whether a coordinate is outside $[b_-,b_+]$, then whether $|z-x|>D$. If either test holds, record the corresponding exit and stop this walk.

3.  Otherwise append $x$ to the scalar word and replace the state by $(y,z,yz+a-x)$. If it equals $P$, record the first return and stop; otherwise repeat the preceding step.

4.  For each returned word, check the recurrence at every wraparound phase and absence of any smaller scalar period. Insert both the word and its reverse, identifying words only by cyclic rotation. Store the pair consisting of $a$ and the lexicographically least rotation.

5.  Compare each resulting word, at every cyclic phase, with the explicit family formulas in Table [2](#tab:classification){reference-type="ref" reference="tab:classification"}. For this subtraction allow their degenerate parameter values; classify by the actual word length. Output every unmatched word with its parameter and first-return length.

[\[lem:certificate\]]{#lem:certificate label="lem:certificate"} The algorithm covers every orbit satisfying [\[eq:core\]](#eq:core){reference-type="eqref" reference="eq:core"}, including its original time orientation. Every orbit walk stops, without any imposed bound on $a$ or on the number of iterates. An exit excludes the seed from a periodic orbit having the specified maximum difference and height bounds.

Every residual periodic word has a phase with $|d_0|=D$; reverse if necessary to obtain $d_0=D$. Equation [\[eq:key\]](#eq:key){reference-type="eqref" reference="eq:key"} gives precisely the five choices of $s$, the relation defining $q$, and the two neighboring bounds [\[eq:seedbounds\]](#eq:seedbounds){reference-type="eqref" reference="eq:seedbounds"}. The height bounds place $u,v$ in the enumerated intervals. The equation defining $p$ in [\[eq:extremal\]](#eq:extremal){reference-type="eqref" reference="eq:extremal"} uniquely recovers $a$. Thus an extremal seed of this word occurs. The reversed word is also a valid word for the same $a$ by [\[eq:reversor\]](#eq:reversor){reference-type="eqref" reference="eq:reversor"}; explicitly restoring both reverses recovers whichever orientation was used originally.

For fixed $a,D$, all nonexiting states belong to the finite set $[b_-,b_+]^3\cap\mathbb Z^3$. If a walk never exited, it would repeat a state. Under an injective map the first repeat must be the initial state: if $P_j=P_i$ with $j>i>0$, apply the inverse $i$ times to obtain $P_{j-i}=P_0$, an earlier return. This proves termination at a first return or exit. A genuine bounded periodic word could violate neither necessary bound, so an exit is a valid exclusion. The existence of this finite-state argument is not an operational period cutoff in the code.

## Independent interval seeds and inverse traversal

The independent implementation changes the seed order, treats both extremum signs directly, walks the inverse map, and compares complete triple-state sets. It neither imports nor executes the primary implementation. Its complete mathematical algorithm is as follows.

For $D=1,\ldots,100$, $\delta\in\{-D,D\}$, $s=-3,-2,-1,0,1$, and $q=-D,\ldots,D$, set $p=(s+1)\delta-q$ and discard $|p|>D$. Start with the integer interval $$I=[b_-,b_+]\cap[b_--\delta,b_+-\delta].
 \label{eq:interval0}$$ If $p\ne0$, intersect $I$ with $$;
 \label{eq:intervalp}$$ if $q\ne0$, intersect it with $$.
 \label{eq:intervalq}$$ Zero $p$ or $q$ imposes no corresponding interval constraint. For each integer $u\in I$, put $$v=u+\delta,\qquad a=q-sv+u+s,
 \qquad P=(u,s,v).
 \label{eq:independentseed}$$ Check the reconstruction of both $p$ and $q$ and their bounds. All five centers already lie in $[b_-,b_+]$ for $D\ge1$. These interval intersections are exactly the integer solutions of the same neighboring inequalities, now with both signs.

At each inverse-time state, test height first, then the difference bound, and then membership in a visited set. A repeated state must equal $P$; a noninitial first repeat raises an explicit error. Otherwise insert the state and apply $(x,y,z)\mapsto(xy+a-z,x,y)$, checking that a forward step recovers the previous state. The proof of Lemma [\[lem:certificate\]](#lem:certificate){reference-type="ref" reference="lem:certificate"}, applied to the inverse bijection, proves termination here too.

Upon return, choose the lexicographically least visited triple and reconstruct its native *forward* word. Check every forward state belongs to the inverse visited set, that the first repeat is the chosen triple, that all visited states are used, and that the word has as many distinct triples as entries. Represent this cycle by $(a,\min\{\text{visited triples}\})$, while retaining the complete triple set. For fixed $a$ that set determines the forward transitions uniquely, so this representation does not quotient by reversal.

For independent family matching, generate candidate words rather than use the primary rotation predicates. Generate $F_3$ with $t=(a+4)/2$ when $a$ is even. For every value $t$ occurring in the reconstructed word, generate $F_4$ and, at their required parameters, $F_5,F_6,F_8$. At $a=0$ also generate $F_{12}$ with $m=\max_i|x_i|\ge1$. For a word of length at most two, generate its alternating candidate. Verify candidate recurrences and compare their complete triple-state sets. Assign the first matching label in the order $F_2,F_3,F_4,F_5,F_6,F_8,F_{12}$; this resolves the degenerate family overlaps. An unmatched word is an exception. These candidate rules cover every family match: its parameter is either fixed by $a$, appears in the word, or equals its maximum absolute coordinate in $F_{12}$.

Only after discovery is complete does the independent algorithm parse the primary cycle output. It validates every recorded integer word, recurrence, first-return length and family label, rejects duplicate keys, compares the complete key sets in both directions, and compares every full triple-state set. Reading the input bytes earlier to hash them does not influence discovery. Both implementations use exact unbounded integers.

## The complete finite outcome

The preserved executions give Table [3](#tab:certificate){reference-type="ref" reference="tab:certificate"}. Both implementations produce exactly $25\,851$ oriented cycles, with the identical family partition $$(F_3,F_4,F_5,F_6,F_8,F_{12},\text{unmatched})
 =(200,25350,99,100,50,50,2).
 \label{eq:familypartition}$$ These counts refer only to the finite certificate, not to the infinite global families. There are $25\,753$ self-reversing cycles and $49$ pairs of distinct reversed cycles in this output; the latter all lie in $F_5$.

::: {#tab:certificate}
  Traversal and extremum       Seeds   Returns   Difference exits   Height exits
  ------------------------ --------- --------- ------------------ --------------
  Forward, positive           74,866    25,907             30,335         18,624
  Inverse, negative           74,866    25,907             30,335         18,624
  Inverse, positive           74,866    25,907             30,344         18,615
  Inverse, both signs        149,732    51,814             60,679         37,239

  : Complete historical seed dispositions in the proved residual core. The extremum sign and traversal direction are distinct choices. Every row is an exact partition; these are accepted proof-stage executions, not new manuscript experiments.
:::

The two unmatched words are $$\begin{aligned}
 a=-13 &: \quad (-4,-2,-3,-3,-2),\\
 a=-2 &: \quad (-2,-1,0,0,-1,-2,0,-1,0).\end{aligned}$$ Their first-return lengths are five and nine. The independently reconstructed output agrees with every one of the primary $25\,851$ records, not only its aggregate counts. The nine-seed exchange between inverse exit types in Table [3](#tab:certificate){reference-type="ref" reference="tab:certificate"} is not a mismatch: opposite directions can first cross different rejecting boundaries. The longest observed walks were $12$ forward and $18$ backward; neither number was an input. Likewise the observed seed forcing range $[-503,497]$ was an output, not a prescribed parameter interval.

Corollary [\[cor:core\]](#cor:core){reference-type="ref" reference="cor:core"}, Lemma [\[lem:certificate\]](#lem:certificate){reference-type="ref" reference="lem:certificate"}, and this complete exact residual outcome prove exhaustion of the table. The remaining sections verify its existence, least-period, disjointness and level-count assertions without relying on a finite sample of its unbounded parameters.

# Existence, least periods and oriented representatives {#sec:least}

For each row of Table [2](#tab:classification){reference-type="ref" reference="tab:classification"}, substitute its displayed entries and parameter into $x_{i+3}+x_i-x_{i+1}x_{i+2}-a$. The result is identically zero at every wraparound phase. This is a polynomial identity in the displayed free integer variables, so it establishes existence on the full parameter range, not just on the finite core. Substitution of the initial triple in $K_a$ gives exactly the displayed level. Invariance then gives that same value at all other phases. The preserved separate symbolic check verifies these recurrence and level identities at all $55$ phases across the ten rows, in addition to the full invariant identity; the identities themselves are immediate from the printed words.

We give all period and identification arguments, since a periodic word alone is not a disjoint list of native cycles. For $F_1$ and $F_2$, Lemma [\[lem:zero\]](#lem:zero){reference-type="ref" reference="lem:zero"} already gives the least period, and $u<v$ chooses the unique ordering of an alternating pair. The length-three word $(-2,-2,t)$ is constant only at $t=-2$. Thus $t\ne-2$ gives exactly period three; its parameter is uniquely recovered from $a=2t-4$.

For $F_4$, shifting by two positions exchanges $t$ and $a+1-t$. A shorter period is possible exactly when $2t=a+1$, giving an alternating word. At fixed $a$, the strict inequality $2t<a+1$ removes that case and chooses one representative of each exchange. Any further cyclic identification must preserve the alternating positions carrying $-1$; if one of the free entries also equals $-1$, checking the four positions gives the same exchange and no extra identification.

The $F_5$ word has prime length five and is never constant, as it contains both $0$ and $-1$. For $t\notin\{0,-1\}$ its displayed occurrence of $-1$ is unique. A cyclic identification of two such words must align that occurrence, forcing equal parameters. The words at $t=0$ and $t=-1$ are rotations of one another and are the sole duplication. Omitting $t=-1$ therefore gives the stated range. In particular, parameters $t$ and $-1-t$ generally give different oriented cycles, exchanged by time reversal. The exceptional five-cycle $E_5$ is nonconstant and lies at the different parameter $a=-13$.

For $F_6$, the condition $t\ne0$ excludes every proper divisor $1,2,3$ of six. A shift by three positions exchanges $t$ with $-t$, and the two nonzero positions show that these are the only possible parameter identifications. The choice $t\ge1$ is consequently exact.

For $F_8$, a shift by four positions exchanges $t$ with $-t-2$. Period four would force $t=-1$, and periods one or two would imply period four. The excluded value $t=-1$ is already $F_4$ at level $1$. For $t\ge0$, the positions carrying $-1$ occur precisely four apart, so a cyclic identification can only give the stated exchange. Exactly one member of each nondegenerate pair has $t\ge0$.

For $F_{12}$ with $m\ge2$, compare entries with zero-based indices. Periods one or two are impossible because the entries at positions $0$ and $4$ are $1$ and $-1$. Period three is excluded by positions $1$ and $4$; period four by positions $0$ and $4$; period six by positions $1$ and $7$, which are $m$ and $1-m$. For $m=1$ the word is $$(1,1,1,0,-1,-1,1,0,1,-1,-1,0).$$ Positions $0,3$ exclude period three, positions $0,4$ exclude period four, and positions $1,7$ exclude period six. Periods one and two are again excluded by positions $0,4$. These are every proper divisor of twelve. Since $m^2-m+2$ is strictly increasing for integers $m\ge1$, different standard parameters cannot describe the same cycle. This is a direct least-period argument; no unprinted appeal to the unforced predecessor is required.

The length-nine exceptional word has different entries in positions $0$ and $3$, so it has neither period three nor period one. It therefore has least period nine. The reversed $E_5$ word is its rotation by one position, and the reversed $E_9$ word is its rotation by six. Thus no additional reverse-oriented exceptions are hidden by the list.

Finally, rows of different least periods cannot overlap, and the two rows of length five have different forcing parameters. Together with Section [5](#sec:finite){reference-type="ref" reference="sec:finite"}, these observations complete every assertion of Theorem [\[thm:classification\]](#thm:classification){reference-type="ref" reference="thm:classification"}.

# Exact level counts and the native dynamical zeta function {#sec:counts}

Fix integers $a,k$. Let $c_\ell(a,k)$ be the number of oriented cycles of least period $\ell$ on the ordinary integer level set $$X_{a,k}(\mathbb Z)=\{(x,y,z)\in\mathbb Z^3:K_a(x,y,z)=k\}.$$ All lengths outside [\[eq:periodset\]](#eq:periodset){reference-type="eqref" reference="eq:periodset"} have count zero. The following explicit tests remove every remaining orbit search. Here a positive square means $h^2$ for an integer $h>0$; zero is excluded whenever positivity is specified.

[\[prop:counts\]]{#prop:counts label="prop:counts"} The counts $c_\ell(a,k)$ are given by the following rules.

1.  $c_1$ is the number of distinct integers $r=1\pm\sqrt{1-a}$ satisfying $k=r^2(2r-3)$. If $1-a$ is not a nonnegative integer square, the count is zero; if the square root is zero, count the common root once.

2.  Let $P$ run over the distinct integer roots of $$P^2+(a-3)P-k=0.
     \label{eq:period2quadratic}$$ Put $S=P+a$. Each root contributes one to $c_2$ exactly when $S^2-4P=h^2>0$ with $h\equiv S\pmod2$. Otherwise it contributes zero.

3.  $c_3=1$ exactly when $a$ is even, $t=(a+4)/2\ne-2$, and $k=8-(t-4)^2$; otherwise $c_3=0$.

4.  $c_4=1$ exactly when $$(a+1)(a-7)+4k=h^2>0,\qquad h\equiv a+1\pmod2;
     \label{eq:period4square}$$ otherwise $c_4=0$.

5.  At $a=-1$, the $F_5$ contribution is one if $k=0$, two if $k>0$ and $4k+1$ is an integer square, and zero otherwise. Add one precisely for $(a,k)=(-13,-64)$. There is no other contribution to $c_5$.

6.  $c_6=1$ exactly when $a=0$ and $k$ is a positive integer square.

7.  $c_8=1$ exactly when $a=-1$ and $k-1$ is a positive integer square.

8.  $c_9=1$ exactly when $(a,k)=(-2,-1)$.

9.  $c_{12}=1$ exactly when $a=0$ and $4k-7$ is a positive integer square.

In the last four rules the count is zero when the stated condition fails.

The fixed-point relation is $(r-1)^2=1-a$, giving the first test. For an alternating pair put $S=u+v$ and $P=uv$. The parameter and level equations become $$a=S-P,\qquad k=P(S-3)=P(P+a-3).$$ This proves [\[eq:period2quadratic\]](#eq:period2quadratic){reference-type="eqref" reference="eq:period2quadratic"}. A distinct integral unordered pair exists exactly when its discriminant is a positive square with the required parity; then $$u=(S-h)/2<v=(S+h)/2.$$ Distinct values of $P$ give distinct pairs, since $S=P+a$. This formulation remains valid at $a=1$ and does not divide by $u-1$ or lose a factor-zero case.

The $F_3$ relation uniquely fixes $t$ when $a$ is even. For $F_4$, solving $k=t^2-(a+1)t+2a+2$ gives discriminant $(a+1)(a-7)+4k$. Its smaller root is $(a+1-h)/2$; it is integral and satisfies $2t<a+1$ exactly under [\[eq:period4square\]](#eq:period4square){reference-type="eqref" reference="eq:period4square"}. Thus there is one cycle, not two, when that test succeeds.

For $F_5$, $k=t(t+1)\ge0$ for integral $t$. At $k=0$ the two roots $0,-1$ give the same cyclic word and the specified range retains only $0$. At $k>0$ the square test $4k+1=(2t+1)^2$ gives two distinct integer parameters, neither excluded; they give the two distinct reversed oriented cycles and must both be counted. The additional exceptional contribution is read at its separate parameter and level.

The formulas $k=t^2$ with $t\ge1$ and $k-1=(t+1)^2$ with $t\ge0$ give the sixth and seventh tests. The eighth is the unique $E_9$ row. Finally $k=m^2-m+2$ is equivalent to $4k-7=(2m-1)^2$. A positive square congruent to $1$ modulo $4$ has odd positive root $h$, yielding the unique $m=(1+h)/2\ge1$. The disjointness already proved means that no further identifications enter these tests.

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} For all integers $a,k$ and $n\ge1$, $$\#\operatorname{Fix}\bigl(T_a^n\vert X_{a,k}(\mathbb Z)\bigr)
 =\sum_{\substack{\ell\in\mathcal L\\\ell\mid n}}
   \ell c_\ell(a,k).
 \label{eq:fixedcounts}$$ The Artin--Mazur dynamical zeta series in the ordinary time variable $\tau$ is the finite rational product $$\zeta_{a,k}(\tau)
 :=\exp\!\left(\sum_{n\ge1}
 \frac{\#\operatorname{Fix}(T_a^n\vert X_{a,k}(\mathbb Z))}{n}\tau^n\right)
 =\prod_{\ell\in\mathcal L}(1-\tau^\ell)^{-c_\ell(a,k)}.
 \label{eq:zeta}$$

Each arithmetic test admits at most finitely many parameters, so $X_{a,k}(\mathbb Z)$ has finitely many periodic points. An oriented cycle of length $\ell$ contributes its $\ell$ distinct points to $\operatorname{Fix}(T_a^n)$ exactly when $\ell\mid n$, proving [\[eq:fixedcounts\]](#eq:fixedcounts){reference-type="eqref" reference="eq:fixedcounts"}. For each such cycle its contribution to the logarithm of the zeta series is $\sum_{j\ge1}\tau^{j\ell}/j=-\log(1-\tau^\ell)$. Summing over the finitely many cycles proves [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} as a formal power-series identity.

There is no analogous unrestricted all-level finite-count assertion here. For every fixed $a$, the infinitely many integers $t$ with $2t<a+1$ give distinct four-cycles. In particular the all-level fixed set of $T_a^4$ is infinite. Fixing the invariant level is indispensable for the finite counts in [\[eq:fixedcounts\]](#eq:fixedcounts){reference-type="eqref" reference="eq:fixedcounts"}.

# Scope, evidence and limitations {#sec:scope}

The classification concerns ordinary integer triples for the specified polynomial automorphism, including singular ordinary points on its cubic levels. It makes no claim about all rational points, whole-group finite orbits, complex scheme-theoretic fixed loci, multiplicity weights, or an altered compactified or induced return clock. The residual computation is conditional only on the printed analytic reduction and exact integer execution; it is not a proof based on checking a guessed height or period limit. Its finite outputs do not enumerate the unbounded families globally.

The polynomial identities and all signed analytic branches are included in the article. The finite part was checked by a separately written inverse-time implementation, which matched every complete directed-state set. This is computational corroboration with a disclosed implementation boundary, not a formal verification in a proof assistant. Hashes identify the accepted files but do not by themselves establish their mathematical correctness. The assertion caveat for the primary Python implementation is stated in Appendix [9](#app:certificate){reference-type="ref" reference="app:certificate"}. The unchanged source files, complete cycle outputs and full execution summaries accompany the manuscript so the finite claim is reproducible.

The factors in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} are dynamical cycle factors. They are not Euler factors of an elliptic curve, an arithmetic $L$-function, or evidence for a root-number assertion. No transfer from source dynamical arithmetic to such a target is asserted.

#### Preparation and review disclosure.

The manuscript and proof artifacts were prepared with AI assistance. The analytic and computational checks cited here are internal current-team reviews, not external human peer review. New manuscript-transcription reviews and release checks are tracked separately from the accepted mathematical executions. Anonymous authorship is maintained; no institution, journal acceptance or external reviewer identity is implied.

# Exact implementation and preserved evidence {#app:certificate}

## Computational contract and provenance

The primary script below is the unchanged implementation used for the accepted positive-extremum run. It uses Python integers, not floating-point approximations, and its only maximum is the proved amplitude constant $100$. The infinite-looking orbit loop terminates by Lemma [\[lem:certificate\]](#lem:certificate){reference-type="ref" reference="lem:certificate"}. The script contains assertions: reproducing its historical validation requires ordinary Python execution, *without* the optimization flag `-O`. The independent implementation uses explicit exceptions and a separately implemented seed and state-set algorithm as specified completely in Section [5](#sec:finite){reference-type="ref" reference="sec:finite"}.

The accompanying `supplement/` tree preserves the relative layout needed by the independent script: its primary input directory is , and its own directory is . The source proof, both certifiers, both complete cycle JSONL files, both execution summaries, the separate symbolic checker, and the internal proof-review reports are retained unchanged. Running the scripts writes their outputs beside their sources; to reproduce without replacing the accepted receipts, first copy the supplement to a fresh scratch directory and run there. The raw $25\,851$ records are machine-readable witnesses; their seed generation, stopping criterion, matching and semantic comparison have all been specified in the article.

The independent run used Python 3.12.3. Its recorded runtime was $3.37218$ seconds; the primary recorded runtime was $0.834775$ seconds. These are historical provenance, not benchmark claims or complexity bounds. The separate symbolic receipt used Python 3.12.3 and SymPy 1.14.0 and checked the ten rows at all $55$ wraparound phases for each recurrence and level identity, the invariant identity and four algebraic count-reduction identities. None of these accepted mathematical programs was rerun during manuscript preparation.

The full primary and independent summaries retain the exact seed dispositions, per-amplitude independent counts and all observed bounds. In the primary JSONL, each record contains `a`, `least_period`, `word`, and `family`; the word is the least cyclic rotation and the records are sorted by parameter and word. The independent output instead reconstructs native words from least triples. Different byte encodings therefore need not share a hash; agreement was checked on the full oriented mathematical data.

## Accepted byte identifiers

The following SHA-256 values identify the historical evidence. They are not substitutes for the reduction proof or the complete finite comparison.

Primary certifier

:   \
    `750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330`

Primary cycle JSONL

:   \
    `352ffd5b5b188e32c347a4083559680e5d1bad12c8e6c6d7cd3dad6324935805`

Primary summary

:   \
    `7000a021df6d38d82e14f6a22b3b764026e9545881aa4b7247cd041e5cf4af0b`

Independent certifier

:   \
    `8bd343b599f9ed6c605b255dfe60b544a81375975083fd5d7ffb2b18a1d6c7c3`

Independent cycle JSONL

:   \
    `0432cd5d8c35fe3cf9fdc0027451bf2e85d04eb880da6da1c03457571fffe35b`

Separate symbolic checker

:   \
    `be9ca47f3b7c8f94b43b25d6857f823f35f004407eff71807770dadf6dac40bd`

## Complete primary certifier

The following listing includes the full source, including family subtraction, primitive-word checks, both orientation restoration and summary generation. The inverse-time script is supplied in machine-readable form; its exact mathematical specification is in Section [5](#sec:finite){reference-type="ref" reference="sec:finite"}.

``` {.python}
#!/usr/bin/env python3
"""Exhaust the analytically proved IR1 core, using exact Python integers.

No chosen parameter bound, period bound, numerical tolerance or random
sample occurs. D_MAX=100 is the theorem's proved reduction constant.
The input contract and termination argument are in IR1_PROOF.md, §4.
Generated JSON files are evidence, not independent proof of the reduction.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import monotonic

D_MAX = 100
OUT = Path(__file__).resolve().parent


def canonical(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def family(a, word):
    n = len(word)
    if n <= 2:
        return "F2"
    for j in range(n):
        w = word[j:] + word[:j]
        t = w[1]
        if n == 3 and w[:2] == (-2, -2) and a == 2*w[2]-4:
            return "F3"
        if n == 4 and w[0] == w[2] == -1 and w[3] == a+1-t:
            return "F4"
        if n == 5 and a == -1 and w == (-1, t, 0, 0, -1-t):
            return "F5"
        if n == 6 and a == 0 and w == (0, 0, w[2], 0, 0, -w[2]):
            return "F6"
        if n == 8 and a == -1 and w == (-1,t,1,t,-1,-t-2,1,-t-2):
            return "F8"
        if n == 12 and a == 0 and t >= 1:
            if w == (1,t,1,t-1,-1,-t,1,1-t,1,-t,-1,t-1):
                return "F12"
    return "EXCEPTION"


def verify_cycle(a, word):
    n = len(word)
    assert n > 0
    for i in range(n):
        assert word[(i+3) % n] == word[(i+1) % n]*word[(i+2) % n]+a-word[i]
    assert all(any(word[i] != word[(i+k) % n] for i in range(n)) for k in range(1,n))


def run():
    start = monotonic()
    counts = Counter()
    exits = Counter()
    cycles = set()
    max_steps = 0
    # No change of a or D during an orbit. Every loop is explicitly finite
    # except its orbit iteration, whose termination follows by injectivity.
    for D in range(1, D_MAX+1):
        lo, hi = -3*D-1, 3*D-1
        for u in range(lo, hi-D+1):
            v = u+D
            for s in (-3,-2,-1,0,1):
                if not lo <= s <= hi:
                    continue
                center_sum = (s+1)*D
                p_lo = max(-D, center_sum-D)
                p_hi = min(D, center_sum+D)
                if u+1:
                    bp = (2*D)//abs(u+1)
                    p_lo, p_hi = max(p_lo,-bp), min(p_hi,bp)
                if v+1:
                    bq = (2*D)//abs(v+1)
                    p_lo, p_hi = max(p_lo,center_sum-bq), min(p_hi,center_sum+bq)
                for p in range(p_lo,p_hi+1):
                    q = center_sum-p
                    assert abs(p)<=D and abs(q)<=D
                    assert abs((u+1)*p)<=2*D and abs((v+1)*q)<=2*D
                    a = v-s*u+s-p
                    seed = (u,s,v)
                    x,y,z = seed
                    word = []
                    counts["seeds"] += 1
                    while True:
                        if not (lo<=x<=hi and lo<=y<=hi and lo<=z<=hi):
                            exits["height"] += 1
                            break
                        if abs(z-x)>D:
                            exits["difference"] += 1
                            break
                        word.append(x)
                        x,y,z = y,z,y*z+a-x
                        if (x,y,z) == seed:
                            w = tuple(word)
                            verify_cycle(a,w)
                            # The extremal normalization may reverse time.
                            # Restore both native orientations explicitly.
                            for candidate in (w, tuple(reversed(w))):
                                verify_cycle(a,candidate)
                                cycles.add((a,canonical(candidate)))
                            counts["returning_seeds"] += 1
                            break
                    max_steps = max(max_steps,len(word))
    ordered = sorted(cycles)
    rows = []
    family_counts = Counter()
    exceptions = []
    for a,w in ordered:
        kind = family(a,w)
        row = {"a":a,"least_period":len(w),"word":list(w),"family":kind}
        rows.append(row)
        family_counts[kind] += 1
        if kind == "EXCEPTION":
            exceptions.append(row)
    assert counts["seeds"] == counts["returning_seeds"] + sum(exits.values())
    raw = "".join(json.dumps(row,separators=(",",":"),sort_keys=True)+"\n" for row in rows)
    (OUT/"IR1_CORE_CYCLES.jsonl").write_text(raw,encoding="utf-8")
    summary = {
        "D_MAX":D_MAX,
        "seed_rule":"IR1_PROOF.md section 4; neighbor bounds included",
        "parameter_cutoff":None,"period_cutoff":None,"exact_integer_arithmetic":True,
        "all_counts":dict(counts),"exit_counts":dict(exits),
        "max_orbit_steps_before_return_or_certified_exit":max_steps,
        "distinct_oriented_cycles_in_completed_seed_output":len(rows),
        "family_cycle_counts_in_finite_certificate_only":dict(sorted(family_counts.items())),
        "exceptions":exceptions,
        "cycle_jsonl_sha256":sha256(raw.encode()).hexdigest(),
        "code_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":round(monotonic()-start,6),
    }
    (OUT/"IR1_CORE_SUMMARY.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,sort_keys=True))


if __name__ == "__main__":
    run()
```
