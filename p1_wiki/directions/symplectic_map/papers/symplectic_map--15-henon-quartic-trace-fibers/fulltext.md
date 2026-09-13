---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--15-henon-quartic-trace-fibers"
canonical_tex: "symplectic_map/papers/15-henon-quartic-trace-fibers/paper/main.tex"
canonical_pdf: "symplectic_map/papers/15-henon-quartic-trace-fibers/paper/main.pdf"
source_sha256: "faa8f60bc7c51c2310b2e48450599823386e8d339fc92feeaf43161d247210d5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Low-Period Trace Fibers of Quartic Generalized Hénon Maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/15-henon-quartic-trace-fibers>)
- [规范 TeX](<../../../../../symplectic_map/papers/15-henon-quartic-trace-fibers/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/15-henon-quartic-trace-fibers/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/15-henon-quartic-trace-fibers/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/15-henon-quartic-trace-fibers/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the sharp quasi-finite cutoff for pure formal trace data on the single-factor monic-centered quartic generalized Hénon space: periods through three suffice, whereas periods through two do not. Two obstacles make this statement more than a calculation on one exceptional family. Low-period rigidity away from Jacobian $-1$ requires the Jacobian as an input, although the trace map considered here supplies only traces; moreover, the Jacobian-$-1$ family with constant period-one and period-two data must be shown to exhaust the lower-period failure locus. We resolve the first obstacle in every degree over an algebraically closed field of characteristic zero. If $s=1-a$ and $C_f$ is the characteristic polynomial of multiplication by $p'$ on the fixed algebra $k[x]/(p-sx)$, then $C_f'(s)=0$. Thus quartic fixed traces leave at most three Jacobian candidates. Over $\mathbb C$, a complete analysis of the five centered quartic root strata shows that the unique positive-dimensional lower trace fiber is $E=\{a=1,\ p=(x^2-L)^2\}$, with quotient coordinate $L^3$. Finally, a formal complete-intersection residue argument, retaining all local multiplicities, gives the pointwise period-three second moment $-1296000-1572864L^3$. It separates the residual coordinate on $E$ and yields global quasi-finiteness through period three, without asserting injectivity or an exact map degree.
author:
- Anonymous
bibliography:
- references.bib
title: 'Low-Period Trace Fibers of Quartic Generalized Hénon Maps'
```

## Markdown 正文

# Introduction {#sec:introduction}

For a polynomial automorphism of the affine plane, periodic derivative data is a natural conjugacy invariant. The concrete question studied here is whether finitely many low-period traces determine only finitely many normalized single Hénon maps. We insist on two features that make the question genuinely intrinsic. First, the input consists only of trace multisets; the Jacobian is not supplied. Second, the multisets live on formal periodic zero-cycles, so a multiple periodic point contributes with its full local-algebra multiplicity.

Write $$f_{a,p}(x,y)=(ay+p(x),x),
\qquad a\in \mathbb C^*,
\label{eq:henon-normal-form-intro}$$ where $p$ is monic centered. The generalized Hénon normal form and its finite residual ambiguity are classical; see [@FriedlandMilnor1989]. Cantat and Dujardin prove rigidity from the full trace spectrum and, by a Noetherian argument, the existence of some finite cutoff. Their fixed-Jacobian low-period theorem gives finiteness from periods one and two when the Jacobian is not $-1$. They also exhibit the quartic Jacobian-$-1$ family $$p_L(x)=(x^2-L)^2
\label{eq:exceptional-intro}$$ on which periods one and two are blind [@CantatDujardin2026]. We use the author version dated May 10, 2026; the arXiv v1 cited in its bibliographic record is an earlier version. These facts define the precise boundary of the present argument: the exceptional family and its lower-period blindness are known, while the cutoff supplied by the general theorem is unspecified.

There are two missing implications. A theorem about pure traces cannot invoke a fixed-Jacobian theorem until the trace data has first restricted the unknown Jacobian. Conversely, displaying the curve in [\[eq:exceptional-intro\]](#eq:exceptional-intro){reference-type="eqref" reference="eq:exceptional-intro"} neither proves that it is the entire non-quasi-finite locus nor rules out another lower-period component. The proof below closes both gaps and then uses period three only after the lower fiber has been reduced to that one curve.

For each $n$, let $\operatorname{Trace}_n(f)$ denote the multiset of $\operatorname{tr}(D_zf^n)$ on the formal-period-$n$ zero-cycle, with scheme-theoretic multiplicity. Let $$\mathfrak T_{\le P}(f)
=
\bigl(\operatorname{Trace}_1(f),\ldots,\operatorname{Trace}_P(f)\bigr).$$ The target of each component is an affine symmetric product in elementary-symmetric coordinates. In quartic degree the formal lengths for periods $1,2,3$ are $4,12,60$.

The main result is one dependent three-part theorem.

[\[thm:unified\]]{#thm:unified label="thm:unified"} Let $f_{a,p}$ be as in [\[eq:henon-normal-form-intro\]](#eq:henon-normal-form-intro){reference-type="eqref" reference="eq:henon-normal-form-intro"}, with $p$ monic centered.

1.  Let $k$ be an algebraically closed field of characteristic zero, let $a\in k^*$, and let $p\in k[x]$ be monic centered of degree $d\ge 2$. Put $$s=1-a,\qquad q=p-sx,\qquad
    C_f(T)=\det\!\left(T-M_{p'}\mid k[x]/(q)\right).$$ The formal fixed trace multiset determines $C_f$, and $$C_f'(s)=0.
    \label{eq:headline-derivative}$$ Consequently a prescribed fixed trace multiset leaves at most $d-1$ possible Jacobians. In degree four it leaves at most three.

2.  Over $\mathbb C$, the exact non-quasi-finite locus of $$\mathfrak T_{\le2}:\mathcal H^1_4
    \longrightarrow \operatorname{Sym}^4(\mathbb C)\times\operatorname{Sym}^{12}(\mathbb C)$$ is $$E=\{(a,p):a=1,\ p(x)=(x^2-L)^2,\ L\in\mathbb C\}.
    \label{eq:headline-E}$$ Its common lower trace data is $$\operatorname{Trace}_1=0^{\times4},\qquad
    \operatorname{Trace}_2=2^{\times12},$$ and the finite residual quotient satisfies $E/\mu_3\simeq\mathbb A^1_{L^3}$.

3.  Over $\mathbb C$, the morphism $\mathfrak T_{\le3}$ is quasi-finite on $\mathcal H^1_4$ and descends to a quasi-finite morphism on $\mathcal M^1_4=\mathcal H^1_4/\mu_3$. The period-at-most-two maps are not quasi-finite on either space. On $E$, the pointwise formal-period-three second power sum is $$S^{(3)}_2(L)=-1296000-1572864L^3.
    \label{eq:headline-moment}$$ Therefore the sharp quasi-finite cutoff for formal pure trace data on this normalized single-factor quartic space is $$P_{\mathcal H^1}(4)=3.$$

No part of the theorem asserts injectivity, an exact fiber cardinality, a generic degree, or a branch divisor. Parts [(B)]{.nodecor} and [(C)]{.nodecor} are complex statements and concern no composition of Hénon factors.

The three contributions are best read as successive repairs of one fiber problem.

1.  Pure fixed traces determine a characteristic polynomial whose derivative vanishes at $1-a$. This turns the missing Jacobian into a finite list before any fixed-Jacobian theorem is used.

2.  After the nonconservative candidates are closed, the five centered quartic root partitions identify the exact conservative failure locus. The simple-root stratum uses a one-variable finiteness theorem, whereas every singular stratum is treated directly.

3.  On the remaining curve, a formal period-three complete intersection yields the affine $L^3$-moment [\[eq:headline-moment\]](#eq:headline-moment){reference-type="eqref" reference="eq:headline-moment"}. Equality of full trace multisets forces equality of that moment, which is enough for finite fibers on the curve.

The three formulas $$C_f'(1-a)=0,
\qquad
E=\{a=1,\ p=(x^2-L)^2\},
\qquad
S^{(3)}_2(L)=-1296000-1572864L^3$$ also record the logical order. The first provides finitely many Jacobian slices. The second says that only one slice and one curve survive periods one and two. The third makes the residual quotient coordinate finite. The last formula is not used as a classifier away from $E$.

For later reference, the proof has the following seven-step dependency chain.

1.  Formal trace data is first placed in elementary-symmetric coordinates. Multiplication on a finite algebra, rather than evaluation on its reduced support, makes these coordinates regular under specialization and remembers the length of every local factor.

2.  For fixed points, the two plane equations reduce to the single monic equation $q=p-(1-a)x$. The trace multiset is therefore the characteristic polynomial of multiplication by $p'$ on $k[x]/(q)$. A residue cancellation when $q$ is squarefree and a local nilpotence argument when it is not prove $C_f'(1-a)=0$ in complementary cases.

3.  In degree four, the preceding derivative identity produces at most three candidates for $a$. Only after this finite enumeration do we apply the fixed-Jacobian theorem, separately on every candidate with $a\ne1$. Thus the Jacobian is an output of the pure trace data, never an extra input.

4.  On the remaining slice $a=1$, the full $f^2$-fixed algebra is the tensor square of the fixed algebra. Its trace characteristic polynomial and the characteristic polynomial of the embedded diagonal are both functorial in the period-one polynomial. Formal subtraction consequently determines the length-$12$ period-two multiset from period one.

5.  The conservative fixed-trace fiber is divided into the five root partitions of a centered quartic. Sugiyama's theorem is confined to the simple-root part; direct root coordinates treat $[31]$ and $[211]$ and all their boundaries. The two partitions without simple roots are exactly the curve $E$, whose residual coordinate is $L^3$.

6.  On $E$, three orbit equations give a rank-$64$ complete intersection. At the dynamical specialization, the complete-intersection Jacobian is also the derivative trace, so the second moment is a residue with numerator $t^3$. Weighted support, two independent slope certificates, the constant ledger, and local formal subtraction yield the length-$60$ pointwise moment in [\[eq:headline-moment\]](#eq:headline-moment){reference-type="eqref" reference="eq:headline-moment"}.

7.  Finally, a full period-three fiber is either contained in an already finite lower fiber or lies on $E$. In the latter case equality of trace multisets implies equality of the displayed second moment and hence of $L^3$. Finite geometric fibers and finite type give quasi-finiteness, and the same argument survives the finite residual quotient.

Each step uses the output of the preceding one. In particular, the fixed-Jacobian input cannot be moved before Step 3, and the period-three moment cannot be used globally before Step 5 has identified the complete lower fiber.

Section [2](#sec:setup){reference-type="ref" reference="sec:setup"} fixes the normalized spaces, formal cycles, and imported theorem scopes. Section [3](#sec:jacobian){reference-type="ref" reference="sec:jacobian"} proves Part [(A)]{.nodecor}. Sections [4](#sec:conservative){reference-type="ref" reference="sec:conservative"} and [5](#sec:strata){reference-type="ref" reference="sec:strata"} determine the exact lower failure locus. Section [6](#sec:period-three){reference-type="ref" reference="sec:period-three"} proves the period-three moment with formal multiplicities, and Section [7](#sec:global){reference-type="ref" reference="sec:global"} converts it into global quasi-finiteness. Section [8](#sec:conclusion){reference-type="ref" reference="sec:conclusion"} records the limitations and publication relationship of the absorbed development proof before concluding.

# Normalized spaces, formal traces, and prior framework {#sec:setup}

## The normalized single-factor space

[\[def:spaces\]]{#def:spaces label="def:spaces"} For a field $k$ and $d\ge2$, let $$\mathcal H^1_d(k)
=
\{(a,p):a\in k^*,\ p\in k[x]\text{ monic of degree }d,
\ [x^{d-1}]p=0\}.$$ The associated map is $f_{a,p}(x,y)=(ay+p(x),x)$ and $$\operatorname{Jac}(f_{a,p})=-a.$$ The superscript $1$ records that the normal form has one Hénon factor.

If $\zeta^{d-1}=1$, diagonal scaling $h_\zeta(x,y)=(\zeta x,\zeta y)$ gives $$h_\zeta^{-1}f_{a,p}h_\zeta(x,y)
=
\bigl(ay+\zeta^{-1}p(\zeta x),x\bigr).
\label{eq:residual-action}$$ The transformed polynomial is again monic centered. Thus $\mu_{d-1}$ acts on $\mathcal H^1_d$, and we write $$\mathcal M^1_d=\mathcal H^1_d/\mu_{d-1}$$ for the finite normalized quotient. We use this quotient only as a finite orbit space; no fine-moduli assertion is needed. The structural role of this finite ambiguity agrees with the normal-form framework of [@FriedlandMilnor1989].

## Formal cycles and symmetric-product targets

For a parameter $f$, the graph of $f^n$ meets the diagonal in a zero-dimensional cycle, denoted $[\operatorname{Fix}(f^n)]$, whenever the intersection is proper. Intersection multiplicity, rather than reduced support, is part of this cycle. Following the formal-period convention used by Cantat and Dujardin [@CantatDujardin2026], the formal-period-$n$ cycle $[\operatorname{Per}_n^*(f)]$ is obtained by taking the closure of the exact-period cycle from the generic locus, equivalently by the dynatomic subtraction on the locus where the fixed cycles meet properly. For the two prime periods used below, $$=[\operatorname{Fix}(f^2)]-[\operatorname{Fix}(f)],
\qquad
[\operatorname{Per}_3^*(f)]=[\operatorname{Fix}(f^3)]-[\operatorname{Fix}(f)].
\label{eq:formal-prime-subtraction}$$ These equalities are cycle equalities with local lengths. They are not set-theoretic deletions of points.

[\[def:formal-trace\]]{#def:formal-trace label="def:formal-trace"} Let $Z_n(f)=[\operatorname{Per}_n^*(f)]$ have degree $p_n$, and let $$\tau_n(z)=\operatorname{tr}(D_zf^n).$$ On each local Artin algebra of $Z_n(f)$, multiplication by $\tau_n$ has a characteristic polynomial. The product of these local characteristic polynomials is a monic polynomial of degree $p_n$; its root multiset is $\operatorname{Trace}_n(f)$. Thus local length is retained even when the support is nonreduced.

For quartic single Hénon maps, Bézout degrees give $$p_1=4,
\qquad
p_2=4^2-4=12,
\qquad
p_3=4^3-4=60.
\label{eq:formal-degrees}$$ The last two equalities will also be recovered from the explicit finite algebras in Sections [4](#sec:conservative){reference-type="ref" reference="sec:conservative"} and [6](#sec:period-three){reference-type="ref" reference="sec:period-three"}.

The symmetric product $\operatorname{Sym}^r(\mathbb C)$ is identified with affine $r$-space by elementary symmetric coordinates. Explicitly, if a finite locally free algebra $B$ of rank $r$ carries an element $u$, the coefficients of $$\chi_{B,u}(T)=\det(T-M_u\mid B)
=T^r+c_1T^{r-1}+\cdots+c_r
\label{eq:characteristic-symmetric}$$ are regular functions of the parameters. They record the unordered formal values of $u$, with local multiplicity.

Two elementary finite-algebra facts explain why this is the appropriate target. If $R\to R'$ is a base change, $B$ is finite locally free over $R$, and $u\in B$, then the multiplication matrix after base change is $M_u\otimes_RR'$. Hence $$\chi_{B\otimes_RR',\,u\otimes1}(T)
=\chi_{B,u}(T)\otimes_RR'.$$ The coefficient tuple therefore specializes without choosing or ordering geometric points. On a local factor of length $m$ supported at a point where $u$ has residue value $\lambda$, write $u=\lambda+n$ with $n$ in the maximal ideal. Since that ideal is nilpotent, $M_n$ is nilpotent and $$\det(T-M_u)=(T-\lambda)^m.$$ Thus a nonreduced point contributes $m$ copies of its residue value, even though its reduced support contains only one point. More generally, different local factors multiply their characteristic polynomials, exactly as disjoint components add as zero-cycles. This mechanism also shows why formal subtraction must occur at the level of finite algebras or cycles: deleting a support point would discard its length. Over $\mathbb C$, every power sum is a symmetric polynomial in the formal values, so equality in the symmetric-product target implies equality of the second moment used later; the converse implication is neither needed nor asserted.

[\[prop:regular-trace\]]{#prop:regular-trace label="prop:regular-trace"} For every fixed $n$, elementary symmetric functions of $\tau_n$ define a regular morphism $$\operatorname{Trace}_n:\mathcal H^1_d(\mathbb C)\longrightarrow\operatorname{Sym}^{p_n}(\mathbb C).$$ Consequently $$\mathfrak T_{\le P}:\mathcal H^1_d(\mathbb C)
\longrightarrow\prod_{n=1}^P\operatorname{Sym}^{p_n}(\mathbb C)$$ is a finite-type morphism. It is invariant under [\[eq:residual-action\]](#eq:residual-action){reference-type="eqref" reference="eq:residual-action"} and therefore descends through $\mathcal H^1_d\to\mathcal M^1_d$.

The formal cycle is finite of constant degree over the normalized parameter space, and $\tau_n$ is a regular function on it. The determinant construction [\[eq:characteristic-symmetric\]](#eq:characteristic-symmetric){reference-type="eqref" reference="eq:characteristic-symmetric"} is compatible with base change, so every coefficient is regular, including over nonreduced fibers. Equation [\[eq:residual-action\]](#eq:residual-action){reference-type="eqref" reference="eq:residual-action"} is a conjugacy. It carries formal cycles with their intersection multiplicities to the corresponding cycles and conjugates every derivative product, so it preserves $\tau_n$ and its characteristic polynomial. Finite-group invariance gives the descended morphism.

[\[def:cutoff\]]{#def:cutoff label="def:cutoff"} The number $P_{\mathcal H^1}(4)$ is the least $P$ for which $\mathfrak T_{\le P}$ is quasi-finite on $\mathcal H^1_4(\mathbb C)$. This is a finite-fiber threshold for a finite-type morphism, not an injectivity threshold.

## Imported theorems and their exact roles

Formal periodic cycles have a broader dynatomic history; for projective morphisms, one reference is [@Hutz2010]. Here the operative multiplicity convention and regular trace morphisms are those of Cantat and Dujardin [@CantatDujardin2026]. Their Theorem 3.7 gives existence of some finite period bound but does not provide the quartic number three. Their Theorem 4.2 is used later only over $\mathbb C$, only after fixing the Jacobian, and only when $a\ne1$. Their Example 4.3 is the direct precedent for the curve $E$ and its period-one/two blindness.

On the conservative slice, a simple-root stratum reduces to one-variable fixed-multiplier data. Sugiyama proves finite fibers for the fixed-multiplier map on the domain $V_d$ where no fixed multiplier is $1$ [@Sugiyama2017]; the monic-centered formulation and finite residual normalization are clarified in [@Sugiyama2023]. We apply this input only when all four fixed points are simple. The one-variable small-cycle work of Huguin [@Huguin2024] is adjacent background, not an imported theorem about the Jacobian-$-1$ Hénon slice.

The period-three proof uses the classical trace--residue identity for zero-dimensional complete intersections, in the form developed in [@CattaniDickensteinSturmfels1996]. The residue formalism is an established method. What must be proved here is the exact specialization to the quartic Hénon family, including the correct Jacobian factor, coefficient support, signs, and formal subtraction.

# Pure fixed traces and the Jacobian {#sec:jacobian}

This section proves Theorem [\[thm:unified\]](#thm:unified){reference-type="ref" reference="thm:unified"}[(A)]{.nodecor} without any complex-analytic input. Let $k$ be algebraically closed of characteristic zero, let $d\ge2$, and let $(a,p)\in\mathcal H^1_d(k)$.

[\[lem:fixed-algebra\]]{#lem:fixed-algebra label="lem:fixed-algebra"} Put $$s=1-a,
\qquad q=p-sx,
\qquad A_q=k[x]/(q).$$ The fixed scheme of $f_{a,p}$ is $\operatorname{Spec}A_q$, and its formal trace multiset is the formal value multiset of $p'$ in $A_q$. Hence $\operatorname{Trace}_1(f)$ determines $$C_f(T)=\det(T-M_{p'}\mid A_q).$$

A fixed point satisfies $y=x$ and $$x=ax+p(x),$$ or equivalently $q(x)=p(x)-(1-a)x=0$. Since $q$ is monic of degree $d$, $A_q$ has length $d$. Moreover $$Df(x,y)=
\begin{pmatrix}
p'(x)&a\\
1&0
\end{pmatrix},
\qquad
\operatorname{tr}(Df)=p'(x).
\label{eq:first-derivative}$$ Definition [\[def:formal-trace\]](#def:formal-trace){reference-type="ref" reference="def:formal-trace"} therefore identifies the fixed trace characteristic polynomial with $C_f$. This remains true at a multiple fixed point because the multiplication operator is taken on the full local Artin factor.

We next locate the scalar $s$ inside the derivative of $C_f$. The squarefree and nonreduced arguments must be separated because the logarithmic derivative used in the first case is undefined at $C_f(s)=0$.

[\[lem:squarefree\]]{#lem:squarefree label="lem:squarefree"} If $q$ is monic, squarefree, and has degree $d\ge2$, then $$\sum_{q(\alpha)=0}\frac{1}{q'(\alpha)}=0.$$ For the fixed algebra of Lemma [\[lem:fixed-algebra\]](#lem:fixed-algebra){reference-type="ref" reference="lem:fixed-algebra"}, this identity implies $C_f'(s)=0$.

Let $\alpha_1,\ldots,\alpha_d$ be the roots of $q$. Lagrange interpolation of the constant polynomial $1$ reads $$1=
\sum_{i=1}^d
\frac{q(x)}{q'(\alpha_i)(x-\alpha_i)}.
\label{eq:lagrange-one}$$ The coefficient of $x^{d-1}$ on the left vanishes, while the corresponding coefficient of the $i$th summand is $1/q'(\alpha_i)$. This proves the sum identity.

Because $p'=q'+s$, the characteristic polynomial splits as $$C_f(T)=\prod_{i=1}^d\bigl(T-s-q'(\alpha_i)\bigr).$$ Every $q'(\alpha_i)$ is nonzero, so $C_f(s)\ne0$ and logarithmic differentiation is legitimate: $$\frac{C_f'(s)}{C_f(s)}
=
\sum_{i=1}^d\frac{1}{s-p'(\alpha_i)}
=-
\sum_{i=1}^d\frac{1}{q'(\alpha_i)}
=0.$$ Thus $C_f'(s)=0$.

[\[lem:nonreduced\]]{#lem:nonreduced label="lem:nonreduced"} If $q$ has a root $\alpha$ of local length $m\ge2$, then $$(T-s)^m\mid C_f(T).$$ In particular $C_f'(s)=0$.

Write $q=(x-\alpha)^m u(x)$ with $u(\alpha)\ne0$. In the corresponding length-$m$ local factor of $A_q$, the class of $q'$ belongs to the maximal ideal and is nilpotent. Since $p'=s+q'$, multiplication by $p'$ on that factor is $sI+N$ with $N$ nilpotent. Its characteristic polynomial is $(T-s)^m$. This factor divides the global characteristic polynomial. As $m\ge2$, differentiation gives $C_f'(s)=0$. No division by $C_f(s)$ occurs.

The squarefree and nonreduced proofs use different information and neither is a limiting version of the other. When $q$ is squarefree, every $q'(\alpha)$ is a unit in its one-dimensional local factor. Consequently $C_f(s)\ne0$, and the global cancellation of the residues $1/q'(\alpha)$ can be expressed by the logarithmic derivative of $C_f$. When $q$ has a multiple root, $q'$ lies in the maximal ideal of a local Artin factor. Then $C_f(s)=0$, so that logarithmic derivative is unavailable; instead the nilpotent part of multiplication by $p'=s+q'$ supplies at least a double factor at $T=s$. The two cases therefore establish the same derivative identity for opposite local reasons: cancellation among distinct reduced points in the first case, and multiplicity at one nonreduced point in the second. This dichotomy is also why reduced fixed-point data would not suffice for Part [(A)]{.nodecor}.

[\[thm:derivative-identity\]]{#thm:derivative-identity label="thm:derivative-identity"} For every $(a,p)\in\mathcal H^1_d(k)$, $$C_f'(1-a)=0.$$

If $q$ is squarefree, apply Lemma [\[lem:squarefree\]](#lem:squarefree){reference-type="ref" reference="lem:squarefree"}. If it is not squarefree, one of its local factors has length at least two and Lemma [\[lem:nonreduced\]](#lem:nonreduced){reference-type="ref" reference="lem:nonreduced"} applies. These cases exhaust all monic $q$.

[\[cor:jacobian-bound\]]{#cor:jacobian-bound label="cor:jacobian-bound"} A prescribed formal fixed trace multiset leaves at most $d-1$ possible values of $\operatorname{Jac}(f)$. In degree four it leaves at most three.

The trace multiset fixes the monic degree-$d$ polynomial $C_f$. In characteristic zero its derivative is a nonzero polynomial of degree $d-1$, so Theorem [\[thm:derivative-identity\]](#thm:derivative-identity){reference-type="ref" reference="thm:derivative-identity"} leaves at most $d-1$ possibilities for $s$. Finally $$\operatorname{Jac}(f)=-a=s-1,$$ which is a bijective affine change of the candidate parameter. For $d=4$ the bound is three.

The corollary is deliberately a candidate bound. It does not assert that every root of $C_f'$ occurs, that the candidates are distinct in a fiber, or that a trace fiber is injective after $a$ is fixed. Its role is to remove the hidden-Jacobian obstruction before the fixed-Jacobian theorem is invoked.

# Reduction to the conservative slice {#sec:conservative}

We return to quartic maps over $\mathbb C$. The parameter $a=1$ is conservative in the convention [\[eq:henon-normal-form-intro\]](#eq:henon-normal-form-intro){reference-type="eqref" reference="eq:henon-normal-form-intro"}, because then $\operatorname{Jac}(f)=-1$. Corollary [\[cor:jacobian-bound\]](#cor:jacobian-bound){reference-type="ref" reference="cor:jacobian-bound"} and the fixed-Jacobian theorem close all other candidates. On the conservative slice, an explicit tensor-algebra identity shows that period two carries no additional fiber information beyond period one.

[\[prop:nonconservative-finite\]]{#prop:nonconservative-finite label="prop:nonconservative-finite"} Fix a value of $\mathfrak T_{\le2}$ on $\mathcal H^1_4(\mathbb C)$. Its intersection with the locus $a\ne1$ is finite.

The period-one component determines $C_f$. By Corollary [\[cor:jacobian-bound\]](#cor:jacobian-bound){reference-type="ref" reference="cor:jacobian-bound"}, its roots through the relation $C_f'(1-a)=0$ leave at most three values $$a_1,a_2,a_3.$$ A candidate $a_i=0$ is discarded because $\mathcal H^1_4$ parametrizes automorphisms and requires $a\ne0$. For each remaining candidate with $a_i\ne1$, the Jacobian $-a_i$ is fixed and differs from $-1$. Cantat--Dujardin's Theorem 4.2 then gives a finite fiber for the data consisting of this fixed Jacobian and the formal traces in periods one and two [@CantatDujardin2026]. The required pure-trace fiber is a finite union of these fixed-Jacobian fibers.

The order is essential: $$\operatorname{Trace}_1
\longrightarrow
\{a_1,a_2,a_3\}
\longrightarrow
\text{the fixed-Jacobian theorem for each }a_i\ne1.$$ No Jacobian is inserted into the original trace datum.

[\[prop:period-two-determined\]]{#prop:period-two-determined label="prop:period-two-determined"} Let $f=f_{1,p}$ with $p$ monic centered quartic. The formal period-two trace multiset is determined functorially by $\operatorname{Trace}_1(f)$, including when the fixed scheme is nonreduced.

The fixed algebra is $$A_1=\mathbb C[x]/(p).$$ A point $(x,y)$ is fixed by $f^2$ precisely when $$p(x)=0,
\qquad
p(y)=0.$$ Indeed $f(x,y)=(y+p(x),x)$, and the two equations obtained from $f^2(x,y)=(x,y)$ reduce to those displayed equations. Hence the full $f^2$-fixed algebra is $$A_2=\mathbb C[x,y]/(p(x),p(y))
\simeq A_1\otimes_\mathbb CA_1,
\label{eq:period-two-algebra}$$ of length $4^2=16$.

From [\[eq:first-derivative\]](#eq:first-derivative){reference-type="eqref" reference="eq:first-derivative"} with $a=1$, $$Df(x,y)=
\begin{pmatrix}p'(x)&1\\1&0\end{pmatrix}.$$ Along a two-step orbit, direct multiplication gives the regular trace element $$\operatorname{tr}(Df^2)=2+p'(x)p'(y)
\quad\text{in }A_2.
\label{eq:period-two-trace}$$ Let $r_1,\ldots,r_4$ be the formal eigenvalues of multiplication by $p'$ on $A_1$, with local-algebra multiplicity. Since $A_2=A_1\otimes A_1$, the full $f^2$-fixed trace multiset is $$\{\,2+r_ir_j:1\le i,j\le4\,\}.
\label{eq:full-period-two-values}$$ This tensor statement concerns characteristic polynomials of multiplication operators, so it remains valid when $A_1$ is not semisimple.

It is useful to display the two polynomials that enter formal subtraction. Over a splitting field, with every $r_i$ repeated according to its local-algebra multiplicity, they are $$\begin{aligned}
\Phi_{\mathrm{full}}(T)
&=\prod_{1\le i,j\le4}\bigl(T-(2+r_ir_j)\bigr),\\
\Phi_{\mathrm{fix}}(T)
&=\prod_{1\le i\le4}\bigl(T-(2+r_i^2)\bigr).\end{aligned}$$ Both expressions are symmetric in the $r_i$, so their coefficients descend and are determined by the characteristic polynomial of multiplication by $p'$ on $A_1$. The diagonal is a closed length-$4$ subcycle of the length-$16$ full fixed cycle. The prime-period cycle identity makes the quotient $$\Phi_2^*(T)=\frac{\Phi_{\mathrm{full}}(T)}{\Phi_{\mathrm{fix}}(T)}$$ the characteristic polynomial on the effective formal period-two cycle. This is a polynomial identity produced by scheme-theoretic subtraction, not a cancellation that assumes sixteen distinct points. It remains valid when several $r_i$ coincide or arise from a nilpotent local factor.

The diagonal morphism $A_2\to A_1$, $x,y\mapsto x$, embeds the formal fixed cycle into the $f^2$-fixed cycle. On that length-$4$ cycle the values are $$2+r_i^2,
\qquad 1\le i\le4.$$ The prime-period cycle identity [\[eq:formal-prime-subtraction\]](#eq:formal-prime-subtraction){reference-type="eqref" reference="eq:formal-prime-subtraction"} subtracts this embedded cycle scheme-theoretically from the length-$16$ cycle. It leaves a formal period-two cycle of length $12$, and its characteristic polynomial is determined by dividing the full characteristic polynomial from [\[eq:full-period-two-values\]](#eq:full-period-two-values){reference-type="eqref" reference="eq:full-period-two-values"} by the fixed-cycle characteristic polynomial. Both factors are determined by $\{r_i\}_{i=1}^4$. Therefore $\operatorname{Trace}_2(f)$ is determined by $\operatorname{Trace}_1(f)$.

[\[cor:conservative-reduction\]]{#cor:conservative-reduction label="cor:conservative-reduction"} On the slice $a=1$, the fibers of $\mathfrak T_{\le2}$ are exactly the fibers of the fixed trace map on monic centered quartics.

The period-one component is part of $\mathfrak T_{\le2}$, and Proposition [\[prop:period-two-determined\]](#prop:period-two-determined){reference-type="ref" reference="prop:period-two-determined"} makes its period-two component a functorial consequence of that first component.

# The five quartic strata and the exact exceptional fiber {#sec:strata}

Let $a=1$. A root $\alpha$ of $p$ of local length $m$ contributes the formal eigenvalue $p'(\alpha)$ with algebraic multiplicity $m$ to $\operatorname{Trace}_1$. Every monic centered quartic has one of the root partitions $$[1111],\quad[31],\quad[211],\quad[22],\quad[4].$$ We prove finiteness on the first three strata, identify the last two with $E$, and then check every boundary. The classification is exhaustive at the level of locally closed strata and their closures.

The multiplicity of zero in the fixed trace multiset already records the total length of the multiple-root part: $p'(\alpha)=0$ at every multiple root, while $p'(\alpha)\ne0$ at every simple root. Thus the partitions have zero multiplicities $0,3,2,4,4$, respectively. This observation separates the first three strata from one another inside a fixed-trace fiber. It also identifies the only possible ambiguity: $[22]$ and $[4]$ both have four zero formal values and must be analyzed together, including the collision where the two double roots merge.

## The simple-root stratum

[\[prop:1111\]]{#prop:1111 label="prop:1111"} Every fixed-trace fiber on the stratum of quartics with four simple roots is finite.

Put $$h(x)=x+p(x).$$ The roots $\alpha$ of $p$ are precisely the fixed points of the one-variable polynomial $h$. At each such root, $$h'(\alpha)=1+p'(\alpha).$$ Because $\alpha$ is simple, $p'(\alpha)\ne0$, so no fixed multiplier of $h$ equals $1$. The multiplier tuple therefore belongs to Sugiyama's domain $V_4$. The finite-fiber theorem for the fixed-multiplier map on that domain gives finitely many affine-conjugacy classes of $h$ [@Sugiyama2017]. Its monic-centered refinement has only the finite residual normalization ambiguity [@Sugiyama2023]. Hence a prescribed unordered set of $p'(\alpha)=h'(\alpha)-1$ leaves finitely many monic centered $p$.

No assertion from these references is used when $p$ has a multiple root.

## The two finite singular strata

[\[prop:31\]]{#prop:31 label="prop:31"} Every fixed-trace fiber on the root partition $[31]$ is finite.

Let $r$ be the triple root. Centering forces the simple root to be $-3r$, so $$p(x)=(x-r)^3(x+3r).
\label{eq:31-param}$$ The triple local factor contributes zero three times. At the simple root, $$p'(-3r)=(-3r-r)^3=-64r^3.$$ Thus $$\operatorname{Trace}_1(f_{1,p})=\{0,0,0,-64r^3\}.
\label{eq:31-trace}$$ A prescribed trace multiset fixes $r^3$, leaving at most three normalized values of $r$ and one residual orbit. If $r=0$, the parameter is the fourfold-root boundary, which is a single point. The fiber remains finite.

The formula also describes the closure of this stratum. For $r\ne0$ the unique nonzero trace value marks the simple root and determines the parameter through the finite map $r\mapsto r^3$. At $r=0$ the simple root and the triple root collide, giving the single $[4]$ polynomial $x^4$. No free parameter survives at the boundary.

[\[prop:211\]]{#prop:211 label="prop:211"} Every fixed-trace fiber on the root partition $[211]$ is finite.

Write the roots as $$r,r,r+u,r+v,$$ where $$u\ne0,
\qquad v\ne0,
\qquad u\ne v,
\qquad 4r+u+v=0.
\label{eq:211-conditions}$$ Then $$p(x)=(x-r)^2(x-r-u)(x-r-v).$$ The double root contributes zero twice. At the two simple roots the derivative values are $$A=u^2(u-v),
\qquad
B=-v^2(u-v).
\label{eq:211-AB}$$ Both are nonzero under [\[eq:211-conditions\]](#eq:211-conditions){reference-type="eqref" reference="eq:211-conditions"}, and $$\frac BA=-\left(\frac vu\right)^2.
\label{eq:211-ratio}$$

The trace multiset gives the unordered pair $\{A,B\}$. Choose one of its two possible orderings and set $z=v/u$. Equation [\[eq:211-ratio\]](#eq:211-ratio){reference-type="eqref" reference="eq:211-ratio"} leaves at most two values of $z$. The condition $u\ne v$ says $z\ne1$, and then $$A=u^3(1-z)
\label{eq:211-recover-u}$$ leaves at most three values of $u$. Finally $v=zu$ and $r=-(u+v)/4$. The two orderings, the at most two square-root choices, and the at most three cube-root choices form a finite set. This proves finiteness without applying a simple-fixed-point theorem to a singular polynomial.

Here the ratio is the step that removes a possible one-parameter ambiguity. Before the traces are imposed, $z=v/u$ is free. The ordered ratio $B/A$ fixes $z^2$, after which the nonzero value $A$ fixes $u^3$ because $z\ne1$. Centering then fixes $r$. Permuting $A$ and $B$ only exchanges finitely many choices; it does not restore a continuous parameter. The exclusions $u=0$, $v=0$, and $u=v$ are exactly the divisors on which this reconstruction degenerates, and the next lemma assigns each of them to a remaining partition.

[\[lem:boundaries\]]{#lem:boundaries label="lem:boundaries"} The excluded root-coordinate boundaries in Proposition [\[prop:211\]](#prop:211){reference-type="ref" reference="prop:211"} lie in the remaining listed strata: exactly one of $u,v$ is zero gives $[31]$; $u=v\ne0$ gives $[22]$; and $u=v=0$ gives $[4]$.

If $u=0$, the root $r+u$ joins the double root $r$, while $r+v$ remains simple unless $v=0$; the case $v=0$ is symmetric. If $u=v\ne0$, the two formerly simple roots coincide and give a second double root. If both vanish, all four roots equal $r$, and centering forces $4r=0$, hence $r=0$ over $\mathbb C$. These are respectively the partitions stated.

These equalities exhaust the boundary because the configuration uses only the two differences from the double root. Away from $u=0$, $v=0$, and $u=v$, the partition is $[211]$; on their union it is one of the three partitions listed in the lemma. The centering equation determines $r$ throughout, so taking closure in the monic-centered coefficient space creates no additional direction.

## The exceptional strata

[\[prop:exceptional-strata\]]{#prop:exceptional-strata label="prop:exceptional-strata"} The union of the $[22]$ and $[4]$ strata is exactly $$\{p_L(x)=(x^2-L)^2:L\in\mathbb C\}.$$ It is exactly the fixed-trace fiber $0^{\times4}$ on the conservative slice, and its period-two trace multiset is $2^{\times12}$.

For partition $[22]$, write the double roots as $r$ and $r'$. Centering gives $2r+2r'=0$, so $r'=-r$ and $$p(x)=(x-r)^2(x+r)^2=(x^2-r^2)^2.$$ Set $L=r^2$. Partition $[4]$ has one root $r$ of length four; centering forces $r=0$, which is the parameter $L=0$. This proves one inclusion and includes the boundary.

Conversely, every $p_L=(x^2-L)^2$ has only multiple roots. Multiplication by $p_L'$ on each fixed local algebra is nilpotent, so its characteristic polynomial is $T^4$ and $\operatorname{Trace}_1=0^{\times4}$. If an arbitrary monic centered quartic has this same formal trace multiset, then a simple root $\alpha$ would contribute the nonzero eigenvalue $p'(\alpha)$, a contradiction. Thus every root is multiple. The only degree-four partitions with no simple part are $[22]$ and $[4]$, already parametrized above.

Proposition [\[prop:period-two-determined\]](#prop:period-two-determined){reference-type="ref" reference="prop:period-two-determined"} now applies with $r_i=0$ for all $i$. The full $f^2$-fixed trace is $2^{\times16}$, and subtracting its length-$4$ fixed part leaves $$\operatorname{Trace}_2=2^{\times12}.$$

The parameter $L$ has a scheme-theoretic meaning across both partitions. For $L\ne0$ there are two double roots $\pm\sqrt L$, each of local length two; at $L=0$ they coalesce into the length-four root at the origin. Multiplication by $p_L'$ is nilpotent on these local factors, so the characteristic polynomial remains $T^4$ at the collision. The family is therefore one closed curve with a distinguished boundary point, rather than two unrelated pieces sharing the same reduced trace values.

The family in Proposition [\[prop:exceptional-strata\]](#prop:exceptional-strata){reference-type="ref" reference="prop:exceptional-strata"}, including its lower-period blindness, is the family exhibited by Cantat and Dujardin [@CantatDujardin2026]. The point here is the exactness of its role inside the whole normalized quartic trace map.

[\[lem:E-quotient\]]{#lem:E-quotient label="lem:E-quotient"} Under the residual action of $\mu_3$, the parameter on $E$ transforms as $L\mapsto\zeta L$. Hence $$E/\mu_3\simeq\mathbb A^1_{L^3}.$$

For $\zeta^3=1$, equation [\[eq:residual-action\]](#eq:residual-action){reference-type="eqref" reference="eq:residual-action"} gives $$\zeta^{-1}\bigl((\zeta x)^2-L\bigr)^2
=
(x^2-\zeta L)^2.$$ Thus the invariant ring on the parameter line is $\mathbb C[L]^{\mu_3}=\mathbb C[L^3]$.

[\[thm:lower-locus\]]{#thm:lower-locus label="thm:lower-locus"} The non-quasi-finite locus of $\mathfrak T_{\le2}$ on $\mathcal H^1_4(\mathbb C)$ is exactly $E$. The complete inverse image of the value $$(0^{\times4},2^{\times12})$$ is $E$.

Proposition [\[prop:nonconservative-finite\]](#prop:nonconservative-finite){reference-type="ref" reference="prop:nonconservative-finite"} makes every fiber on $a\ne1$ finite. On $a=1$, Corollary [\[cor:conservative-reduction\]](#cor:conservative-reduction){reference-type="ref" reference="cor:conservative-reduction"} reduces the problem to fixed traces. Propositions [\[prop:1111\]](#prop:1111){reference-type="ref" reference="prop:1111"}, [\[prop:31\]](#prop:31){reference-type="ref" reference="prop:31"}, and [\[prop:211\]](#prop:211){reference-type="ref" reference="prop:211"} give finite intersections with the first three strata. Lemma [\[lem:boundaries\]](#lem:boundaries){reference-type="ref" reference="lem:boundaries"} shows that their closures introduce no unlisted partition. Proposition [\[prop:exceptional-strata\]](#prop:exceptional-strata){reference-type="ref" reference="prop:exceptional-strata"} identifies the last two strata with $E$, which is contracted to the displayed lower trace value.

It remains to exclude an unseen $a\ne1$ component over that particular value. There $C_f(T)=T^4$. Theorem [\[thm:derivative-identity\]](#thm:derivative-identity){reference-type="ref" reference="thm:derivative-identity"} gives $$0=C_f'(s)=4s^3.$$ Since the base field has characteristic zero, $s=0$ and $a=1$. Proposition [\[prop:exceptional-strata\]](#prop:exceptional-strata){reference-type="ref" reference="prop:exceptional-strata"} then forces $p=p_L$. Hence the inverse image is exactly $E$.

Every other geometric fiber is a finite union of finite intersections with the five strata and the at most three Jacobian slices. A finite-type morphism is quasi-finite at a point exactly when that point is isolated in its geometric fiber. Thus every point outside $E$ is a quasi-finite point, while each point of $E$ belongs to the positive-dimensional fiber $E$ and is not a quasi-finite point.

# Formal period three on the exceptional curve {#sec:period-three}

We now work entirely on $E$. Put $$p_L(x)=(x^2-L)^2,
\qquad
q_L(x)=p_L'(x)=4x(x^2-L).
\label{eq:pqL}$$ The goal is to calculate the second power sum of $\operatorname{Trace}_3$ without replacing the formal $f^3$-fixed algebra by its reduced support. A deformation parameter $\varepsilon$ separates the coefficient support and gives two independent ways to verify the nonzero slope.

## The complete intersection and the residue bridge

Use cyclic indices in $\mathbb Z/3\mathbb Z$ and define $$F_i=(x_i^2-L)^2+\varepsilon(x_{i-1}-x_{i+1}),
\qquad i=0,1,2.
\label{eq:Fi}$$ Let $$\mathcal A
=
\mathbb C[L,\varepsilon,x_0,x_1,x_2]/(F_0,F_1,F_2),
\label{eq:period-three-A}$$ and abbreviate $q_i=q_L(x_i)$. Finally set $$t_\varepsilon
=
q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
\label{eq:t-epsilon}$$

[\[prop:residue-bridge\]]{#prop:residue-bridge label="prop:residue-bridge"} The algebra $\mathcal A$ is free of rank $64$ over $\mathbb C[L,\varepsilon]$, with basis $$x_0^{e_0}x_1^{e_1}x_2^{e_2},
\qquad 0\le e_i<4.$$ The complete-intersection Jacobian is $t_\varepsilon$. At $\varepsilon=1$, the equations define the full $f_L^3$-fixed scheme and $$t_1=\operatorname{tr}(Df_L^3).$$ If $\operatorname{Res}$ denotes the global complete-intersection residue, then $$\operatorname{Tr}_{\mathcal A/\mathbb C[L,\varepsilon]}(M_h)
=\operatorname{Res}(h\,t_\varepsilon).
\label{eq:trace-residue}$$ In particular, $$\operatorname{Tr}(M_{t_\varepsilon^2})
=\operatorname{Res}(t_\varepsilon^3).
\label{eq:residue-exponent}$$

With a total-degree monomial order, the leading monomials of $F_0,F_1,F_2$ are $x_0^4,x_1^4,x_2^4$. They are pairwise coprime. Division by the three monic relations is therefore confluent, and the standard monomials are exactly those displayed. In particular the quotient is finite free of rank $4^3=64$ over the parameter ring.

The Jacobian matrix of [\[eq:Fi\]](#eq:Fi){reference-type="eqref" reference="eq:Fi"} is $$\left(\frac{\partial F_i}{\partial x_j}\right)_{i,j}
=
\begin{pmatrix}
q_0&-\varepsilon&\varepsilon\\
\varepsilon&q_1&-\varepsilon\\
-\varepsilon&\varepsilon&q_2
\end{pmatrix}.$$ The two cubic off-diagonal terms cancel, and expansion of the determinant gives $$\det\left(\frac{\partial F_i}{\partial x_j}\right)
=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2)
=t_\varepsilon.$$ At $\varepsilon=1$, equation $F_i=0$ is the orbit recurrence $$x_{i+1}=x_{i-1}+p_L(x_i),$$ so the quotient is the full $f_L^3$-fixed algebra. Along this orbit, write $$D_i=
\begin{pmatrix}q_i&1\\1&0\end{pmatrix}.$$ Multiplying three matrices yields $$\operatorname{tr}(D_2D_1D_0)=q_0q_1q_2+q_0+q_1+q_2=t_1.$$

The classical quotient trace--residue identity for a finite zero-dimensional complete intersection is [\[eq:trace-residue\]](#eq:trace-residue){reference-type="eqref" reference="eq:trace-residue"}; see [@CattaniDickensteinSturmfels1996]. Substituting $h=t_\varepsilon^2$ proves [\[eq:residue-exponent\]](#eq:residue-exponent){reference-type="eqref" reference="eq:residue-exponent"}. The extra factor is the complete-intersection Jacobian, so the residue numerator is $t_\varepsilon^3$, not $t_\varepsilon^2$.

Three logically separate facts meet in Proposition [\[prop:residue-bridge\]](#prop:residue-bridge){reference-type="ref" reference="prop:residue-bridge"}. First, monicity gives a parameter-independent basis and therefore counts the full fixed scheme with multiplicity: the number $64$ is a rank, not a count of distinct solutions. Second, the determinant of the three orbit equations agrees with the derivative trace only after the orbit recurrence is specialized at $\varepsilon=1$. Third, the trace--residue formula inserts one copy of the complete-intersection Jacobian. Since the desired operator is multiplication by $t_\varepsilon^2$, its trace is $\operatorname{Res}(t_\varepsilon^2t_\varepsilon)=\operatorname{Res}(t_\varepsilon^3)$. Omitting this last factor would compute a different functional and would not give the second power sum. These distinctions allow the deformation to organize coefficients while keeping the specialization tied to the dynamical trace.

Because the leading forms are the monomials $x_i^4$, the global residue in [\[eq:residue-exponent\]](#eq:residue-exponent){reference-type="eqref" reference="eq:residue-exponent"} is equivalently the coefficient of $x_0^3x_1^3x_2^3$ in the standard normal form of $t_\varepsilon^3$. We will use both descriptions.

## Support of the second moment

Define the raw full-fixed-scheme moment $$S_2(L,\varepsilon)=\operatorname{Tr}_{\mathcal A/\mathbb C[L,\varepsilon]}(M_{t_\varepsilon^2}).
\label{eq:S2-deformed}$$

[\[lem:two-term-support\]]{#lem:two-term-support label="lem:two-term-support"} There are constants $C_2,D_2\in\mathbb C$ such that $$S_2(L,\varepsilon)
=C_2\varepsilon^6+D_2L^3\varepsilon^4.
\label{eq:two-term-support}$$

Assign weights $$\operatorname{wt}(x_i)=1,
\qquad
\operatorname{wt}(L)=2,
\qquad
\operatorname{wt}(\varepsilon)=3.$$ Each $F_i$ has weight $4$, each $q_i$ has weight $3$, and $t_\varepsilon$ has weight $9$. The trace of multiplication by $t_\varepsilon^2$ consequently has weight $18$. Interchanging $x_1$ and $x_2$ changes $\varepsilon$ to $-\varepsilon$ but preserves the trace, so the parameter polynomial is even in $\varepsilon$. The nonnegative solutions of $2a+3b=18$ with $b$ even give the four initial possibilities $$\varepsilon^6,
\qquad
L^3\varepsilon^4,
\qquad
L^6\varepsilon^2,
\qquad
L^9.
\label{eq:four-weight-terms}$$

At $\varepsilon=0$, the quotient is the tensor product of three copies of $$\mathbb C[L,x]/((x^2-L)^2).$$ In each factor $$q_L(x)^2=16x^2(x^2-L)^2=0.$$ Since $t_0=q_0q_1q_2$, it follows that $t_0^2=0$. Thus $S_2(L,0)=0$, and the $L^9$ term in [\[eq:four-weight-terms\]](#eq:four-weight-terms){reference-type="eqref" reference="eq:four-weight-terms"} vanishes.

To remove $L^6\varepsilon^2$, it suffices to work on the dense set $L\ne 0$. Pass to an algebraic closure of the Puiseux field in $\varepsilon$, normalize its valuation by $v(\varepsilon)=1$, and choose square roots $\alpha_i^2=L$. Flatness and the rank-$64$ basis group all branches around triples $(\alpha_0,\alpha_1,\alpha_2)$. Write $$x_i=\alpha_i+\delta_i.$$ Because $\alpha_i\ne 0$, $$(x_i^2-L)^2=c_i\delta_i^2+O(\delta_i^3),
\qquad
q_i=d_i\delta_i+O(\delta_i^2),
\label{eq:local-double-expansion}$$ with $c_i,d_i\ne 0$.

There are only two cluster types. Suppose first that exactly two of the $\alpha_i$ agree. After cyclic relabeling, take $\alpha_0=\alpha_1\ne\alpha_2$. In two equations the coupling term has a nonzero constant difference multiplied by $\varepsilon$, so cancellation with the quadratic terms in [\[eq:local-double-expansion\]](#eq:local-double-expansion){reference-type="eqref" reference="eq:local-double-expansion"} gives $$v(q_0)=v(q_1)=\tfrac 12.$$ After these leading cancellations, the remaining coupling has valuation at least $3/2$. If $v(\delta_2)<3/4$, then the quadratic term in the third equation would be its unique term of least valuation and could not cancel. Hence $$v(q_2)\ge\tfrac 34.$$ The two summand types in [\[eq:t-epsilon\]](#eq:t-epsilon){reference-type="eqref" reference="eq:t-epsilon"} now give $$v(q_0q_1q_2)\ge\tfrac 74,
\qquad
v(\varepsilon^2q_i)>\tfrac 74,$$ and therefore $v(t_\varepsilon)\ge 7/4$.

Suppose instead that all three $\alpha_i$ agree. On a nontrivial branch let $r$ be the smallest valuation among the nonzero $\delta_i$. Every coupling difference has valuation at least $1+r$. If $r<1$, the quadratic term at an index realizing $r$ has valuation $2r<1+r$ and is uniquely minimal, which is impossible. Thus $r\ge 1$, and [\[eq:t-epsilon\]](#eq:t-epsilon){reference-type="eqref" reference="eq:t-epsilon"} gives $$v(t_\varepsilon)\ge 3$$ on every nontrivial branch in this cluster. The remaining diagonal branch is a fixed branch; Proposition [\[prop:formal-subtraction\]](#prop:formal-subtraction){reference-type="ref" reference="prop:formal-subtraction"} below proves directly on its local algebra that $t_\varepsilon^2=0$.

For a finite algebra over a splitting field, the trace of multiplication by an element is the sum of its support values weighted by local lengths; multiplication by a nilpotent element has trace zero. In both nonfixed cluster types, $t_\varepsilon^2$ has valuation strictly greater than $2$, while the fixed branch contributes zero. Hence the coefficient of $\varepsilon^2$ in the trace vanishes. This removes $L^6\varepsilon^2$ for $L\ne 0$. Since $S_2$ is polynomial in $L$ and $\varepsilon$, the vanishing extends to $L=0$. Only the two terms in [\[eq:two-term-support\]](#eq:two-term-support){reference-type="eqref" reference="eq:two-term-support"} remain.

Lemma [\[lem:two-term-support\]](#lem:two-term-support){reference-type="ref" reference="lem:two-term-support"} reduces an a priori parameter polynomial to two scalar coefficients before either coefficient is evaluated. Weight and parity first permit the four monomials in [\[eq:four-weight-terms\]](#eq:four-weight-terms){reference-type="eqref" reference="eq:four-weight-terms"}. Nilpotence in the tensor product at $\varepsilon=0$ removes the term with no deformation parameter. The Puiseux argument then removes the only remaining term of $\varepsilon$-degree two by showing that every nonfixed branch has strictly larger valuation, while the diagonal branch contributes zero in its local algebra. Polynomiality extends that conclusion across $L=0$. Thus the later ledgers need determine only $C_2$ and $D_2$; they are not being used to infer the support from selected parameter values.

## Two exact certificates for the slope

The first certificate is a finite binomial ledger. For nonnegative integers in the ranges below, define $$H(r,k)
=
\sum_{\substack{u+v=k\\2u\le r,\ 2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v},
\label{eq:H-def}$$ and $$A_{m,r}
=
\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}
\binom{m-1}{2(m-k)-1}H(r,k).
\label{eq:A-def}$$ For the quartic case $m=2$, coefficient collection in the three cyclic factors specializes to $$D_2
=3\left(
4^9A_{2,2}+3\cdot 4^7A_{2,1}
\right).
\label{eq:D-first-specialized}$$

[\[prop:first-slope\]]{#prop:first-slope label="prop:first-slope"} The finite sums [\[eq:H-def\]](#eq:H-def){reference-type="eqref" reference="eq:H-def"}--[\[eq:D-first-specialized\]](#eq:D-first-specialized){reference-type="eqref" reference="eq:D-first-specialized"} give $$D_2=-1572864.$$

For $H(2,1)$, the only admissible pairs are $(u,v)=(0,1)$ and $(1,0)$. Each contributes one, so $$H(2,1)=2.$$ The sum defining $A_{2,2}$ has only $k=1$, and therefore $$A_{2,2}
=(-1)^3\binom 11H(2,1)=-2.$$ For $A_{2,1}$ the same formal $k=1$ term contains $H(1,1)$, but neither $(0,1)$ nor $(1,0)$ satisfies both inequalities $2u\le 1$ and $2v\le 1$. Hence $$H(1,1)=0,
\qquad A_{2,1}=0.$$ Substitution into [\[eq:D-first-specialized\]](#eq:D-first-specialized){reference-type="eqref" reference="eq:D-first-specialized"} gives $$D_2=3\cdot 4^9(-2)=-6\cdot 262144=-1572864.$$ Appendix [9](#app:first-slope){reference-type="ref" reference="app:first-slope"} records the coefficient provenance leading to the specialized expression; no assertion for general $m$ is used.

We next derive the same number directly from the quartic residue. Put $$P_L(x)=(x^2-L)^2,
\qquad
g_L(x)=x(x^2-L),
\qquad
\Lambda_i=x_{i-1}-x_{i+1}.$$ Then $F_i=P_L(x_i)+\varepsilon\Lambda_i$ and $$t_\varepsilon
=4^3g_0g_1g_2+4\varepsilon^2(g_0+g_1+g_2).$$ Consequently $$t_\varepsilon^3
=
\sum_{j=0}^3
\binom 3j4^{9-2j}\varepsilon^{2j}G_j,
\qquad
G_j=(g_0g_1g_2)^{3-j}(g_0+g_1+g_2)^j.
\label{eq:t3-Gj}$$ Define $$\mathcal L_j(L,\varepsilon)
=
[x_0^{-1}x_1^{-1}x_2^{-1}]
\frac{G_j}{F_0F_1F_2},
\qquad
\mathcal C_{2,j}
=
[L^3\varepsilon^{4-2j}]\mathcal L_j.
\label{eq:C2j}$$ Weighted homogeneity permits setting $L=1$ in the one-variable Laurent functionals. Write $$P(x)=(x^2-1)^2,
\qquad
g(x)=x(x^2-1),$$ and expand $$\frac 1{P_i+\varepsilon\Lambda_i}
=
\sum_{h_i\ge 0}(-1)^{h_i}\varepsilon^{h_i}
\frac{\Lambda_i^{h_i}}{P_i^{h_i+1}}.
\label{eq:denominator-expansion}$$ For $n,h,e\ge 0$, set $$\rho_{n,h}(e)
=
[x^{-1}]\frac{x^eg(x)^n}{P(x)^{h+1}}.
\label{eq:rho-def}$$ The values needed for $n=3$ are $$\begin{array}{c|ccc}
 &e=0&e=1&e=2\\ \hline
\rho_{3,0}(e)&0&0&0\\
\rho_{3,1}(e)&1&0&1\\
\rho_{3,2}(e)&0&0&1
\end{array}
\label{eq:rho-values}$$ and $\rho_{3,0}(e)=0$ for every $e\ge 0$. These follow respectively from $$\frac{g^3}{P}=x^3(x^2-1),
\qquad
\frac{g^3}{P^2}=\frac{x^3}{x^2-1},
\qquad
\frac{g^3}{P^3}=\frac{x^3}{(x^2-1)^3}.$$

[\[prop:second-slope\]]{#prop:second-slope label="prop:second-slope"} The direct quartic residue gives $$\mathcal C_{2,0}=-6,
\qquad
\mathcal C_{2,1}=\mathcal C_{2,2}=0,$$ while $j=3$ has excessive $\varepsilon$-degree. Hence again $$D_2=-1572864.$$

For $j=0$, equation [\[eq:denominator-expansion\]](#eq:denominator-expansion){reference-type="eqref" reference="eq:denominator-expansion"} must provide total denominator increment $$h_0+h_1+h_2=4.$$ The vanishing of $\rho_{3,0}$ forces every $h_i\ge 1$. Thus the only patterns are the three cyclic placements of $(2,1,1)$. For the placement $(h_0,h_1,h_2)=(2,1,1)$, the tensor functional is $$(\rho_{3,2}\otimes\rho_{3,1}\otimes\rho_{3,1})
(\Lambda_0^2\Lambda_1\Lambda_2).$$ Here $$\Lambda_0=x_2-x_1,
\quad
\Lambda_1=x_0-x_2,
\quad
\Lambda_2=x_1-x_0,$$ and $$\Lambda_1\Lambda_2
=-x_0^2+x_0(x_1+x_2)-x_1x_2.$$ Applying $\rho_{3,2}$ in the $x_0$ coordinate retains $-(x_2-x_1)^2$. The remaining functionals give $$-(1+0+1)=-2$$ by [\[eq:rho-values\]](#eq:rho-values){reference-type="eqref" reference="eq:rho-values"}. The expansion sign is $(-1)^4=1$, and all three cyclic placements give the same value. Therefore $\mathcal C_{2,0}=-6$.

For $j=1$, every monomial of $G_1$ has exponent type $(3,2,2)$, while the required internal $\varepsilon$-degree is $2$. If some $h_i=0$, then in that coordinate either $$\frac{g^2}{P}=x^2
\quad\text{or}\quad
\frac{g^3}{P}=x^3(x^2-1)$$ is a polynomial. Nonnegative powers supplied by the $\Lambda_i$ cannot create an $x_i^{-1}$ coefficient. A nonzero tensor term would require all three $h_i\ge 1$, contradicting their total $2$. Hence $\mathcal C_{2,1}=0$.

For $j=2$, no internal $\varepsilon$ is available. Define $$\mu_n=[x^{-1}]\frac{g(x)^n}{P(x)}.$$ Laurent expansion gives $$\mu_1=1,
\qquad
\mu_2=0,
\qquad
\mu_3=0.
\label{eq:mu-values}$$ The square monomials of $G_2$ have exponent type $(3,1,1)$ and contribute $\mu_3\mu_1^2=0$; the cross monomials have type $(2,2,1)$ and contribute $\mu_2^2\mu_1=0$. Thus $\mathcal C_{2,2}=0$. The $j=3$ summand in [\[eq:t3-Gj\]](#eq:t3-Gj){reference-type="eqref" reference="eq:t3-Gj"} already contains $\varepsilon^6$ and cannot enter the $\varepsilon^4$ coefficient. Finally, $$D_2
=
\sum_{j=0}^3\binom 3j4^{9-2j}\mathcal C_{2,j}
=4^9(-6)
=-1572864.$$ Appendix [10](#app:second-slope){reference-type="ref" reference="app:second-slope"} expands every Laurent sign and multiplicity.

The two slope certificates have different inputs. Proposition [\[prop:first-slope\]](#prop:first-slope){reference-type="ref" reference="prop:first-slope"} collects finite binomial choices after a cyclic coefficient expansion, whereas Proposition [\[prop:second-slope\]](#prop:second-slope){reference-type="ref" reference="prop:second-slope"} factors the same coefficient into one-variable Laurent residues. Their agreement checks the cyclic multiplicity, the sign from the denominator expansion, and the power $4^9$ independently. Only the specialized quartic number $D_2$ is concluded. The longer ledgers in Appendices [9](#app:first-slope){reference-type="ref" reference="app:first-slope"} and [10](#app:second-slope){reference-type="ref" reference="app:second-slope"} expose every admissible term without turning either certificate into an all-degree claim.

## The constant coefficient

Set $L=0$ and $\varepsilon=1$. The relations and trace element become $$F_i=x_i^4+x_{i-1}-x_{i+1},
\qquad
t=64x_0^3x_1^3x_2^3+4(x_0^3+x_1^3+x_2^3).
\label{eq:L0-relations}$$ Let $R(e_0,e_1,e_2)$ be the coefficient of $x_0^3x_1^3x_2^3$ in the standard normal form of $x_0^{e_0}x_1^{e_1}x_2^{e_2}$. The three defining relations give $$\begin{aligned}
R(e_0,e_1,e_2)
&=R(e_0-4,e_1+1,e_2)-R(e_0-4,e_1,e_2+1),
\label{eq:R0-rec}\\
R(e_0,e_1,e_2)
&=-R(e_0+1,e_1-4,e_2)+R(e_0,e_1-4,e_2+1),
\label{eq:R1-rec}\\
R(e_0,e_1,e_2)
&=R(e_0+1,e_1,e_2-4)-R(e_0,e_1+1,e_2-4).
\label{eq:R2-rec}\end{aligned}$$ Each use lowers total exponent by three. Reduction therefore terminates at triples with $0\le e_i<4$, where $R(3,3,3)=1$ and every other $R$ is zero.

[\[prop:constant\]]{#prop:constant label="prop:constant"} The constant in [\[eq:two-term-support\]](#eq:two-term-support){reference-type="eqref" reference="eq:two-term-support"} is $$C_2=-1296000.$$

The terminating recurrences [\[eq:R0-rec\]](#eq:R0-rec){reference-type="eqref" reference="eq:R0-rec"}--[\[eq:R2-rec\]](#eq:R2-rec){reference-type="eqref" reference="eq:R2-rec"} give the finite pattern ledger $$\begin{array}{c|r}
\text{exponent pattern}&R\text{-value}\\ \hline
(9,9,9)&-6\\
\text{cyclic }(9,6,6)&2\\
\text{cyclic }(9,3,3)&0\\
\text{cyclic }(6,6,3)&-1\\
\text{any permutation of }(9,0,0)&0\\
\text{any permutation of }(6,3,0)&0\\
(3,3,3)&1
\end{array}
\label{eq:R-patterns}$$ For example, $$R(9,6,6)=R(5,7,6)-R(5,6,7)=1-(-1)=2,$$ and $$R(9,9,9)=2R(5,10,9)=2(1-4)=-6.$$ Appendix [11](#app:constant-ledger){reference-type="ref" reference="app:constant-ledger"} supplies the terminating subledgers for all seven rows.

Write $$Q=64x_0^3x_1^3x_2^3,
\qquad
U=4(x_0^3+x_1^3+x_2^3).$$ Expanding $(Q+U)^3$ and using [\[eq:R-patterns\]](#eq:R-patterns){reference-type="eqref" reference="eq:R-patterns"} gives six groups: $$\begin{aligned}
_{\mathrm{top}}
&=64^3R(9,9,9)=262144(-6)=-1572864,\\
[3Q^2U]_{\mathrm{top}}
&=3\cdot(64^2\cdot 4)\cdot 3\cdot 2
=3\cdot 49152\cdot 2=294912,\\
[3QU^2]_{\mathrm{top},\,\mathrm{squares}}
&=0,\\
[3QU^2]_{\mathrm{top},\,\mathrm{mixed}}
&=3\cdot(64\cdot 16\cdot 2)\cdot 3\cdot(-1)
=3\cdot 6144(-1)=-18432,\\
[U^3]_{\mathrm{top},\,\mathrm{pure\ or}\ 2+1}
&=0,\\
[U^3]_{\mathrm{top},\,\mathrm{fully\ mixed}}
&=6\cdot 4^3R(3,3,3)=384.\end{aligned}$$ The notation $[\cdot]_{\mathrm{top}}$ means the $x_0^3x_1^3x_2^3$ coefficient after normal-form reduction. Summing the nonzero groups yields $$C_2=-1572864+294912-18432+384=-1296000.$$ Because every recurrence step strictly lowers total exponent, this is a finite certificate rather than a sampling of normal forms.

Setting $L=0$ isolates $C_2$ because the other surviving term in [\[eq:two-term-support\]](#eq:two-term-support){reference-type="eqref" reference="eq:two-term-support"} contains $L^3$. The recurrence ledger is exact: each replacement lowers total exponent by three and terminates in the fixed standard basis. Consequently the displayed sum is the normal-form coefficient itself, not an interpolation from several values of $L$. This supplies the constant independently of the two slope calculations.

Combining Lemma [\[lem:two-term-support\]](#lem:two-term-support){reference-type="ref" reference="lem:two-term-support"} with Propositions [\[prop:first-slope\]](#prop:first-slope){reference-type="ref" reference="prop:first-slope"}, [\[prop:second-slope\]](#prop:second-slope){reference-type="ref" reference="prop:second-slope"}, and [\[prop:constant\]](#prop:constant){reference-type="ref" reference="prop:constant"} gives $$S_2(L,\varepsilon)
=-1296000\varepsilon^6-1572864L^3\varepsilon^4.
\label{eq:deformed-moment-final}$$

## Formal subtraction and local lengths

[\[prop:formal-subtraction\]]{#prop:formal-subtraction label="prop:formal-subtraction"} On the embedded formal fixed cycle, multiplication by $t_\varepsilon^2$ has trace zero. At a root of $p_L$ of multiplicity $r=2$ or $4$, the local length of the $f_L^3$-fixed scheme equals $r$. Thus formal subtraction removes all fixed support with its full scheme length.

On the fixed algebra $$B_1=\mathbb C[x]/((x^2-L)^2),$$ all three cyclic coordinates agree. Put $q=4x(x^2-L)$. Then $$q^2=16x^2(x^2-L)^2=0
\quad\text{in }B_1.$$ Restriction of [\[eq:t-epsilon\]](#eq:t-epsilon){reference-type="eqref" reference="eq:t-epsilon"} to the diagonal gives $$t_\varepsilon=q^3+3\varepsilon^2q,$$ and hence $t_\varepsilon^2=0$. The fixed-cycle contribution to the second moment is therefore zero as an equality in its finite algebra, not merely as a sum over reduced points.

We next compare local lengths. Let $\alpha$ be a root of $p_L$ of multiplicity $r\in\{2,4\}$ and set $$\delta=x_0-\alpha,
\qquad
u=x_1-x_0,
\qquad
v=x_2-x_0.$$ At $\varepsilon=1$, equations [\[eq:Fi\]](#eq:Fi){reference-type="eqref" reference="eq:Fi"} become $$\begin{aligned}
F_0&=p_L(\alpha+\delta)+v-u,\\
F_1&=p_L(\alpha+\delta+u)-v,\\
F_2&=p_L(\alpha+\delta+v)+u.\end{aligned}$$ At $(\delta,u,v)=(0,0,0)$, the Jacobian of $(F_1,F_2)$ with respect to $(u,v)$ is $$\begin{pmatrix}0&-1\\1&0\end{pmatrix},$$ which is invertible. Formal implicit elimination gives $$u=-p_L(\alpha+\delta)+O(\delta^{2r-1}),
\qquad
v=p_L(\alpha+\delta)+O(\delta^{2r-1}).
\label{eq:uv-elimination}$$ Substitution into $F_0$ yields $$F_0
=3p_L(\alpha+\delta)+O(\delta^{2r-1}).
\label{eq:remaining-local-equation}$$ The first term has exact order $r$, while $2r-1>r$ for $r=2,4$. Its coefficient is nonzero in characteristic zero. Hence the remaining local equation has exact order $r$, so the local $f_L^3$-fixed length agrees with the fixed-scheme length. Appendix [12](#app:local-length){reference-type="ref" reference="app:local-length"} expands the substitutions separately for $r=2$ and $r=4$.

Formal subtraction has two obligations, both needed in the theorem that follows. The first is numerical: the trace of multiplication by $t_\varepsilon^2$ on the embedded fixed algebra must vanish. Nilpotence of $q$ proves this inside the length-$4$ algebra, so multiplicities do not hide a contribution. The second is cycle-theoretic: the local length carried by the full $f_L^3$-fixed scheme at fixed support must equal the length being subtracted. For $L\ne 0$ the two fixed roots each have length two; for $L=0$ the single fixed root has length four. The implicit-elimination calculation proves the matching local lengths in both cases. Hence the rank-$64$ full scheme loses exactly length four, uniformly across the collision, and the remainder is the formal period-three cycle of length $60$.

[\[thm:period-three-moment\]]{#thm:period-three-moment label="thm:period-three-moment"} On $E$, the second power sum of the trace multiset on the pointwise formal-period-three zero-cycle is $$S_2^{(3)}(L)=-1296000-1572864L^3.$$

At $\varepsilon=1$, Proposition [\[prop:residue-bridge\]](#prop:residue-bridge){reference-type="ref" reference="prop:residue-bridge"} identifies $S_2(L,1)$ with the second moment on the full $f_L^3$-fixed algebra. Proposition [\[prop:formal-subtraction\]](#prop:formal-subtraction){reference-type="ref" reference="prop:formal-subtraction"} shows that the embedded formal fixed cycle has zero second-moment contribution and that formal subtraction leaves no residual fixed support. Therefore the formal period-three moment equals $S_2(L,1)$. Equation [\[eq:deformed-moment-final\]](#eq:deformed-moment-final){reference-type="eqref" reference="eq:deformed-moment-final"} gives the stated formula.

[\[cor:length-sixty\]]{#cor:length-sixty label="cor:length-sixty"} The full $f_L^3$-fixed scheme has length $64$, the embedded fixed scheme has length $4$, and the pointwise formal-period-three cycle has length $$64-4=60.$$ Only after this subtraction, the cyclewise second moment is $$-432000-524288L^3.$$

The first length is the rank in Proposition [\[prop:residue-bridge\]](#prop:residue-bridge){reference-type="ref" reference="prop:residue-bridge"}; the second is the degree of $p_L$. Proposition [\[prop:formal-subtraction\]](#prop:formal-subtraction){reference-type="ref" reference="prop:formal-subtraction"} verifies the subtraction locally at multiplicities two and four, so the difference is the formal length, not a reduced-point count. Every remaining orbit has exactly three points. The derivative products at the three points differ by cyclic permutation, and matrix trace is cyclically invariant. The pointwise second moment is therefore three times the cyclewise moment. Dividing Theorem [\[thm:period-three-moment\]](#thm:period-three-moment){reference-type="ref" reference="thm:period-three-moment"} by three gives the formula.

# Global quasi-finiteness, quotient, and sharpness {#sec:global}

The period-three formula becomes a global statement only because Theorem [\[thm:lower-locus\]](#thm:lower-locus){reference-type="ref" reference="thm:lower-locus"} has already isolated the whole lower bad fiber. We now make that reduction explicit.

[\[thm:finite-geometric-fibers\]]{#thm:finite-geometric-fibers label="thm:finite-geometric-fibers"} Every geometric fiber of $$\mathfrak T_{\le3}:\mathcal H^1_4(\mathbb C)
\longrightarrow
\operatorname{Sym}^4(\mathbb C)\times\operatorname{Sym}^{12}(\mathbb C)\times\operatorname{Sym}^{60}(\mathbb C)$$ is finite.

Fix a value of the full trace tuple and first forget its period-three component. There are two cases.

If the resulting lower value is not $(0^{\times4},2^{\times12})$, Theorem [\[thm:lower-locus\]](#thm:lower-locus){reference-type="ref" reference="thm:lower-locus"} says that its entire period-at-most-two fiber is finite. Imposing one further equality of trace multisets only selects a subset of that finite fiber.

Suppose the lower value is $(0^{\times4},2^{\times12})$. The fixed trace characteristic polynomial is $C_f(T)=T^4$, and the pure-trace identity gives $$C_f'(s)=4s^3=0.$$ Thus $s=0$ and $a=1$. Proposition [\[prop:exceptional-strata\]](#prop:exceptional-strata){reference-type="ref" reference="prop:exceptional-strata"} then identifies the complete lower fiber as $$E=\{(1,p_L):L\in\mathbb C\}.$$ Take two parameters $L,M$ in the same full trace fiber. Equality of their full formal period-three multisets implies equality of every symmetric polynomial in those multisets, in particular equality of their second power sums. Theorem [\[thm:period-three-moment\]](#thm:period-three-moment){reference-type="ref" reference="thm:period-three-moment"} gives $$-1296000-1572864L^3
=
-1296000-1572864M^3.$$ The slope is nonzero, so $L^3=M^3$. For fixed $M$, this equation has at most three normalized solutions $L$. Hence the full geometric fiber is finite in the second case as well.

The second moment is used here in only one direction. Equality of full period-three multisets implies equality of their power sums, and Theorem [\[thm:lower-locus\]](#thm:lower-locus){reference-type="ref" reference="thm:lower-locus"} has already forced both parameters onto $E$ before that implication is invoked. On $E$, the resulting equation $L^3=M^3$ has three or fewer solutions in the normalized parameter line. We do not infer equality of trace multisets from equality of this one moment, nor do we apply the moment to a lower fiber not already identified with $E$. The finite-fiber conclusion combines the complete lower-fiber classification with this one separating consequence.

[\[cor:global-quasi-finite\]]{#cor:global-quasi-finite label="cor:global-quasi-finite"} The morphism $\mathfrak T_{\le3}$ is quasi-finite on $\mathcal H^1_4(\mathbb C)$.

The source is the affine finite-type variety parametrized by $$a\in\mathbb C^*,
\qquad
p(x)=x^4+b_2x^2+b_1x+b_0.$$ The target is a finite product of affine symmetric products, and Proposition [\[prop:regular-trace\]](#prop:regular-trace){reference-type="ref" reference="prop:regular-trace"} makes the trace map a finite-type, hence quasi-compact and locally finite-type, morphism. Theorem [\[thm:finite-geometric-fibers\]](#thm:finite-geometric-fibers){reference-type="ref" reference="thm:finite-geometric-fibers"} supplies finite geometric fibers. The finite-type finite-fiber criterion for quasi-finiteness, Stacks Project Tag 02NH [@Stacks02NH], proves the claim.

Both hypotheses in the last sentence matter. The coefficient construction supplies a morphism of finite type, while Theorem [\[thm:finite-geometric-fibers\]](#thm:finite-geometric-fibers){reference-type="ref" reference="thm:finite-geometric-fibers"} controls fibers after passage to algebraically closed residue fields. Tag 02NH converts precisely those two facts into quasi-finiteness. It does not make the morphism finite or proper, and it gives neither a singleton fiber nor a uniform exact fiber cardinality.

[\[cor:quotient-quasi-finite\]]{#cor:quotient-quasi-finite label="cor:quotient-quasi-finite"} The invariant trace morphism descends to a quasi-finite morphism on $$\mathcal M^1_4=\mathcal H^1_4/\mu_3.$$

Proposition [\[prop:regular-trace\]](#prop:regular-trace){reference-type="ref" reference="prop:regular-trace"} gives the descent. For a target point $y$, the inverse image in $\mathcal M^1_4$ is the image under the finite quotient map of the inverse image of $y$ in $\mathcal H^1_4$. The latter is finite by Theorem [\[thm:finite-geometric-fibers\]](#thm:finite-geometric-fibers){reference-type="ref" reference="thm:finite-geometric-fibers"}, so the quotient fiber is finite. The quotient is a finite-type complex variety and the descended target is unchanged; the same finite-type finite-fiber criterion yields quasi-finiteness. This direct argument does not enlarge the field of definition.

More explicitly, if $q:\mathcal H^1_4\to\mathcal M^1_4$ is the finite quotient and $\overline{\mathfrak T}_{\le3}$ is the descended map, then for every geometric target point $y$, $$\overline{\mathfrak T}_{\le3}^{-1}(y)
=q\bigl(\mathfrak T_{\le3}^{-1}(y)\bigr).$$ Surjectivity of $q$ and invariance of the trace coordinates give this equality. A finite source fiber therefore cannot become infinite after quotienting. For periods at most two, by contrast, the contracted curve maps to the positive-dimensional quotient $E/\mu_3\simeq\mathbb A^1_{L^3}$, so the same finite group cannot repair the lower-period failure.

[\[cor:sharpness\]]{#cor:sharpness label="cor:sharpness"} For formal pure trace data on the normalized single-factor quartic space and its finite residual quotient, the quasi-finite cutoff is sharply three.

The period-at-most-two morphism contracts the curve $E$ by Proposition [\[prop:exceptional-strata\]](#prop:exceptional-strata){reference-type="ref" reference="prop:exceptional-strata"}, so it is not quasi-finite. On the quotient it contracts $$E/\mu_3\simeq\mathbb A^1_{L^3}$$ by Lemma [\[lem:E-quotient\]](#lem:E-quotient){reference-type="ref" reference="lem:E-quotient"}, and hence is again not quasi-finite. Period three is sufficient by Corollaries [\[cor:global-quasi-finite\]](#cor:global-quasi-finite){reference-type="ref" reference="cor:global-quasi-finite"} and [\[cor:quotient-quasi-finite\]](#cor:quotient-quasi-finite){reference-type="ref" reference="cor:quotient-quasi-finite"}. Therefore $P_{\mathcal H^1}(4)=3$ in the sense of Definition [\[def:cutoff\]](#def:cutoff){reference-type="ref" reference="def:cutoff"}.

The proof uses only one implication from the explicit moment: once a lower fiber has been proved to equal $E$, equality of full period-three trace data forces equality of $L^3$. Nothing in the argument says that the moment [\[eq:headline-moment\]](#eq:headline-moment){reference-type="eqref" reference="eq:headline-moment"} separates parameters elsewhere in $\mathcal H^1_4$.

# Limitations, disclosure, and conclusion {#sec:conclusion}

#### Scope and limitations.

The global theorem is complex, quartic, and restricted to a single monic-centered Hénon factor and its finite residual quotient. Part [(A)]{.nodecor} is algebraic over any algebraically closed characteristic-zero field, but no descent of Parts [(B)]{.nodecor} or [(C)]{.nodecor} beyond $\mathbb C$ is asserted. There is no positive-characteristic conclusion. The trace maps use formal-period zero-cycles with local-algebra multiplicity; replacing them by reduced periodic supports would remove information used in the tensor subtraction and local-length arguments.

The cutoff is tied to this formal convention. In periods two and three, the lengths $12$ and $60$ arise only after subtracting embedded fixed cycles with their local lengths. A reduced-support version would define a different target and would not be covered by the finite-algebra identities proved here. Likewise, the quotient statement uses only the residual $\mu_3$-action of the monic-centered normalization; it is not a statement about a larger moduli problem.

The conclusion is quasi-finiteness. We do not determine injectivity, global uniqueness, an exact fiber cardinality, a generic or total map degree, or a branch divisor. The theorem does not cover compositions of quartic Hénon factors, arbitrary loxodromic polynomial automorphisms, unnormalized parameter spaces, or multifactored moduli. It gives no all-degree identity $P(d)=3$, no effective universal cutoff, and no universal nonvanishing statement for a family of slope coefficients. The explicit second moment separates only the already isolated curve $E$; it is not a global classifier.

The exceptional family and its period-one/two blindness, the general finite rigidity framework, generalized Hénon normal forms, one-variable multiplier finiteness, formal dynatomic cycles, and complete-intersection residues are prior inputs rather than method claims of this article. All coefficient reductions in Section [6](#sec:period-three){reference-type="ref" reference="sec:period-three"} are exact parts of the proof. The proof is entirely algebraic and invokes no empirical or machine-assisted evidence. No priority claim is made.

#### Publication-overlap disclosure.

The exceptional-curve theorem and derivation presented here supersede and absorb an earlier non-public development manuscript. That earlier artifact carries no separate novelty claim, is not a black-box dependency of this article, and will not be submitted in parallel. The present article is the sole external vehicle for the overlapping theorem and proof.

All overlapping statements needed for the argument, including the exceptional-locus classification, formal subtraction, both slope certificates, the constant ledger, and the local-length calculation, are reproduced here. No access to the earlier artifact is required to check a theorem assumption or a coefficient. This disclosure records consolidation of the proof; it does not assert priority for the classical normal form, residue identity, dynatomic convention, or imported rigidity and multiplier theorems.

#### Conclusion.

The proof closes a chain whose links cannot be exchanged. Formal fixed traces first turn an unknown Jacobian into a finite list through $C_f'(1-a)=0$. Fixed-Jacobian rigidity closes every nonconservative candidate, while the five centered quartic root partitions isolate one conservative lower-period curve. The formal period-three complete intersection then supplies an affine, nonconstant function of the residual coordinate $L^3$. Finite geometric fibers and finite type finish the argument. Within the stated normalized single-factor scope, and for formal pure trace data, the sharp quasi-finite cutoff is $$P_{\mathcal H^1}(4)=3.$$

# The finite first slope certificate {#app:first-slope}

This appendix expands the first certificate used in Proposition [\[prop:first-slope\]](#prop:first-slope){reference-type="ref" reference="prop:first-slope"}. Its purpose is only to verify the quartic coefficient $D_2$. No formula in this appendix is promoted to an all-degree nonvanishing statement.

The residue coefficient of $L^3\varepsilon^4$ may be collected according to three choices of the cyclic factor carrying the $L^3$ contribution and according to the number $j\in\{0,1\}$ of paired linear selections. In quartic degree this finite collection is $$D_2
=3\sum_{j=0}^{1}
\binom{3}{j}4^{9-2j}A_{2,2-j}.
\label{eq:appA-D2}$$ The outer factor $3$ is the cyclic placement, $4^{9-2j}$ comes from the nine derivative factors with two factors removed for each paired linear selection, and $\binom3j$ chooses that selection. The remaining signed parity collection is $$A_{m,r}
=
\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}
\binom{m-1}{2(m-k)-1}H(r,k),$$ where $$H(r,k)
=
\sum_{\substack{u+v=k\\2u\le r,\ 2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v}.$$ All ranges collapse at $m=2$.

For $r=2$ and $k=1$, the complete admissible-pair ledger is $$\begin{array}{c|c|c|c|c}
(u,v)&\binom1u&\binom2{2u}&\binom2{2v}&\text{product}\\ \hline
(0,1)&1&1&1&1\\
(1,0)&1&1&1&1
\end{array}
\label{eq:appA-H21-ledger}$$ and hence $H(2,1)=2$. For $r=1$ and $k=1$, the same two pairs fail one of the inequalities $2u\le1$ or $2v\le1$, so the admissible set is empty and $$H(1,1)=0.$$ The $k$-range in both $A$-terms is the singleton $\{1\}$. Therefore $$\begin{aligned}
A_{2,2}
&=(-1)^{2+1}
\binom{1}{2(2-1)-1}H(2,1)
=-\binom11\cdot2=-2,\\
A_{2,1}
&=(-1)^{1+1}
\binom{1}{2(2-1)-1}H(1,1)
=\binom11\cdot0=0.\end{aligned}$$ Substitution in [\[eq:appA-D2\]](#eq:appA-D2){reference-type="eqref" reference="eq:appA-D2"} exposes every numerical factor: $$\begin{aligned}
D_2
&=3\left[
\binom30 4^9(-2)
+\binom31 4^7(0)
\right]\\
&=3\cdot(-2)\cdot262144\\
&=-1572864.\end{aligned}$$ The independently derived tensor--Laurent certificate below begins again from the quartic residue and does not use [\[eq:appA-D2\]](#eq:appA-D2){reference-type="eqref" reference="eq:appA-D2"}.

# The tensor--Laurent slope ledger {#app:second-slope}

We expand all Laurent values, signs, and multiplicities entering Proposition [\[prop:second-slope\]](#prop:second-slope){reference-type="ref" reference="prop:second-slope"}. Set $L=1$ after weighted coefficient extraction, and recall $$P=(x^2-1)^2,
\qquad
g=x(x^2-1).$$ At infinity, $$\begin{aligned}
\frac{g^3}{P}
&=x^3(x^2-1),\\
\frac{g^3}{P^2}
&=\frac{x^3}{x^2-1}
=x\sum_{k\ge0}x^{-2k},\\
\frac{g^3}{P^3}
&=\frac{x^3}{(x^2-1)^3}
\;=x^{-3}\sum_{k\ge0}\binom{k+2}{2}x^{-2k}.\end{aligned}$$ More directly, after multiplying by $x^e$, the exponent conditions for an $x^{-1}$ term are $$e+1-2k=-1
\quad\text{for }h=1,
\qquad
e-3-2k=-1
\quad\text{for }h=2.$$ They give the complete values used in the slope extraction: $$\begin{aligned}
\rho_{3,0}(e)&=0 &&(e\ge0),\\
\rho_{3,1}(0)&=1,&
\rho_{3,1}(1)&=0,&
\rho_{3,1}(2)&=1,\\
\rho_{3,2}(0)&=0,&
\rho_{3,2}(1)&=0,&
\rho_{3,2}(2)&=1.\end{aligned}$$

For $j=0$, the coefficient of internal degree $\varepsilon^4$ in $$\prod_{i=0}^2
\sum_{h_i\ge0}(-1)^{h_i}\varepsilon^{h_i}
\frac{\Lambda_i^{h_i}}{P_i^{h_i+1}}$$ has $h_0+h_1+h_2=4$. If some $h_i=0$, its tensor factor is $\rho_{3,0}$ and vanishes. Thus the full list of denominator patterns is $$(2,1,1),
\qquad
(1,2,1),
\qquad
(1,1,2).$$ Their common expansion sign is $(-1)^4=1$.

For the first placement, $$\Lambda_0^2\Lambda_1\Lambda_2
=(x_2-x_1)^2
\bigl[-x_0^2+x_0(x_1+x_2)-x_1x_2\bigr].$$ Only the $-x_0^2$ term survives $\rho_{3,2}$, leaving $$-(x_2-x_1)^2
=-x_2^2+2x_1x_2-x_1^2.$$ Applying $\rho_{3,1}\otimes\rho_{3,1}$ gives the ledger $$\begin{array}{c|c|c}
\text{monomial}&\text{coefficient}&
\rho_{3,1}(e_1)\rho_{3,1}(e_2)\\ \hline
x_2^2&-1&1\cdot1\\
x_1x_2&2&0\cdot0\\
x_1^2&-1&1\cdot1
\end{array}
\label{eq:appB-one-placement}$$ so the placement contributes $-1+0-1=-2$. Cyclically permuting the coordinates preserves the residue orientation and supplies the other two placements, also $-2$. Hence $$\mathcal C_{2,0}=3(-2)=-6.$$

For $j=1$, the numerator types are the three cyclic permutations of $(3,2,2)$ and the required denominator increment is $2$. At least one $h_i$ is zero. At a zero-increment coordinate, $$\frac{g^2}{P}=x^2,
\qquad
\frac{g^3}{P}=x^3(x^2-1)$$ is a polynomial. Each $\Lambda$ contributes only nonnegative powers of that coordinate, so no $x_i^{-1}$ term exists. This handles every distribution $(2,0,0)$ and $(1,1,0)$ and proves $\mathcal C_{2,1}=0$.

For $j=2$, all $h_i$ are zero. The one-variable functionals are $$\begin{aligned}
\mu_1
&=[x^{-1}]\frac{x(x^2-1)}{(x^2-1)^2}
=[x^{-1}]\frac{x}{x^2-1}=1,\\
\mu_2
&=[x^{-1}]\frac{x^2(x^2-1)^2}{(x^2-1)^2}
=[x^{-1}]x^2=0,\\
\mu_3
&=[x^{-1}]x^3(x^2-1)=0.\end{aligned}$$ Expanding $$(g_0g_1g_2)(g_0+g_1+g_2)^2$$ gives three square types $(3,1,1)$ with value $\mu_3\mu_1^2=0$ and three unordered cross pairs, each appearing twice, of type $(2,2,1)$ with value $\mu_2^2\mu_1=0$. Thus $\mathcal C_{2,2}=0$. Finally $j=3$ carries the external factor $\varepsilon^6$ and has no nonnegative internal degree capable of contributing to $\varepsilon^4$.

Restoring the powers and binomial multiplicities from [\[eq:t3-Gj\]](#eq:t3-Gj){reference-type="eqref" reference="eq:t3-Gj"}, $$\begin{aligned}
D_2
&=\binom30 4^9(-6)
+\binom31 4^7(0)
+\binom32 4^5(0)\\
&=-6\cdot262144
=-1572864,\end{aligned}$$ which agrees with Appendix [9](#app:first-slope){reference-type="ref" reference="app:first-slope"}.

# The normal-form constant ledger {#app:constant-ledger}

We give a terminating hand ledger for every exponent pattern used in Proposition [\[prop:constant\]](#prop:constant){reference-type="ref" reference="prop:constant"}. Throughout, $R(a,b,c)$ denotes the top-standard-monomial coefficient, and a triple with all entries below four has value one only for $(3,3,3)$ and zero otherwise. Every displayed equality applies one of [\[eq:R0-rec\]](#eq:R0-rec){reference-type="eqref" reference="eq:R0-rec"}--[\[eq:R2-rec\]](#eq:R2-rec){reference-type="eqref" reference="eq:R2-rec"}; consequently every branch lowers total exponent by three.

We begin with the cyclic pattern $(9,3,3)$. Its two branches vanish as follows: $$\begin{aligned}
R(9,3,3)
&=R(5,4,3)-R(5,3,4),\\
R(5,4,3)
&=R(1,5,3)-R(1,4,4)=0-0,\\
R(1,5,3)
&=-R(2,1,3)+R(1,1,4)=0,\\
R(1,1,4)
&=R(2,1,0)-R(1,2,0)=0,\\
R(1,4,4)
&=-R(2,0,4)+R(1,0,5)=0,\\
R(2,0,4)
&=R(3,0,0)-R(2,1,0)=0,\\
R(1,0,5)
&=R(2,0,1)-R(1,1,1)=0,\\
R(5,3,4)
&=R(1,4,4)-R(1,3,5)=0,\\
R(1,3,5)
&=R(2,3,1)-R(1,4,1)=0,\\
R(1,4,1)
&=-R(2,0,1)+R(1,0,2)=0.\end{aligned}$$ Thus $R(9,3,3)=0$, and cyclic invariance of the relations gives the other two placements.

For the pattern $(6,6,3)$, the unique nonzero terminal leaf is $R(3,3,3)$: $$\begin{aligned}
R(6,6,3)
&=R(2,7,3)-R(2,6,4),\\
R(2,7,3)
&=-R(3,3,3)+R(2,3,4)=-1,\\
R(2,3,4)
&=R(3,3,0)-R(2,4,0)=0,\\
R(2,4,0)
&=-R(3,0,0)+R(2,0,1)=0,\\
R(2,6,4)
&=-R(3,2,4)+R(2,2,5)=0,\\
R(3,2,4)
&=R(4,2,0)-R(3,3,0)=0,\\
R(4,2,0)
&=R(0,3,0)-R(0,2,1)=0,\\
R(2,2,5)
&=R(3,2,1)-R(2,3,1)=0.\end{aligned}$$ Hence $R(6,6,3)=-1$, again for every cyclic placement.

The $(9,6,6)$ ledger uses two short subtrees. First, $$\begin{aligned}
R(5,7,6)
&=R(1,8,6)-R(1,7,7),\\
R(1,8,6)
&=-R(2,4,6)+R(1,4,7)=0,\\
R(2,4,6)
&=-R(3,0,6)+R(2,0,7)=0,\\
R(3,0,6)
&=R(4,0,2)-R(3,1,2)=0,\\
R(2,0,7)
&=R(3,0,3)-R(2,1,3)=0,\\
R(1,4,7)
&=-R(2,0,7)+R(1,0,8)=0,\\
R(1,0,8)
&=R(2,0,4)-R(1,1,4)=0,\\
R(1,7,7)
&=-R(2,3,7)+R(1,3,8)=-1,\\
R(2,3,7)
&=R(3,3,3)-R(2,4,3)=1,\\
R(2,4,3)
&=-R(3,0,3)+R(2,0,4)=0,\\
R(1,3,8)
&=R(2,3,4)-R(1,4,4)=0.\end{aligned}$$ Thus $R(5,7,6)=1$. Second, $$\begin{aligned}
R(5,6,7)
&=R(1,7,7)-R(1,6,8),\\
R(1,6,8)
&=-R(2,2,8)+R(1,2,9)=0,\\
R(2,2,8)
&=R(3,2,4)-R(2,3,4)=0,\\
R(1,2,9)
&=R(2,2,5)-R(1,3,5)=0.\end{aligned}$$ Therefore $R(5,6,7)=-1$, and $$R(9,6,6)=R(5,7,6)-R(5,6,7)=2.$$

It remains to expose the longest row, $(9,9,9)$. Reduction in the first coordinate gives $$R(9,9,9)=R(5,10,9)-R(5,9,10).
\label{eq:appC-999-first}$$ For the first term, $$\begin{aligned}
R(5,10,9)
&=R(1,11,9)-R(1,10,10),\\
R(1,11,9)
&=-R(2,7,9)+R(1,7,10)=0+1,\\
R(2,7,9)
&=-R(3,3,9)+R(2,3,10)=0,\\
R(3,3,9)
&=R(4,3,5)-R(3,4,5)=0,\\
R(4,3,5)
&=R(0,4,5)-R(0,3,6)=0,\\
R(3,4,5)
&=-R(4,0,5)+R(3,0,6)=0,\\
R(2,3,10)
&=R(3,3,6)-R(2,4,6)=0,\\
R(1,7,10)
&=-R(2,3,10)+R(1,3,11)=1,\\
R(1,3,11)
&=R(2,3,7)-R(1,4,7)=1.\end{aligned}$$ The remaining positive branch is $$\begin{aligned}
R(1,10,10)
&=-R(2,6,10)+R(1,6,11)=4,\\
R(2,6,10)
&=-R(3,2,10)+R(2,2,11)=-2,\\
R(3,2,10)
&=R(4,2,6)-R(3,3,6)=0,\\
R(2,2,11)
&=R(3,2,7)-R(2,3,7)=-1-1=-2,\\
R(3,2,7)
&=R(4,2,3)-R(3,3,3)=-1,\\
R(1,6,11)
&=-R(2,2,11)+R(1,2,12)=2,\\
R(1,2,12)
&=R(2,2,8)-R(1,3,8)=0.\end{aligned}$$ All zeros on the right reduce by the already displayed zero subtrees or immediately to standard triples. Hence $$R(5,10,9)=1-4=-3.$$ For clarity, the remaining zero-node closure used in the two long subtrees is the following finite list; every last term is a standard zero or a zero already established above: $$\begin{aligned}
R(0,4,5)
&=-R(1,0,5)+R(0,0,6),\\
R(0,0,6)&=R(1,0,2)-R(0,1,2),\\
R(0,3,6)
&=R(1,3,2)-R(0,4,2),\\
R(0,4,2)&=-R(1,0,2)+R(0,0,3),\\
R(4,0,5)
&=R(0,1,5)-R(0,0,6),\\
R(0,1,5)&=R(1,1,1)-R(0,2,1),\\
R(3,3,6)
&=R(4,3,2)-R(3,4,2),\\
R(4,3,2)&=R(0,4,2)-R(0,3,3),\\
R(3,4,2)
&=-R(4,0,2)+R(3,0,3),\\
R(4,0,2)&=R(0,1,2)-R(0,0,3),\\
R(4,2,6)
&=R(0,3,6)-R(0,2,7),\\
R(0,2,7)&=R(1,2,3)-R(0,3,3),\\
R(4,2,3)
&=R(0,3,3)-R(0,2,4),\\
R(0,2,4)&=R(1,2,0)-R(0,3,0),\\
R(4,1,7)
&=R(0,2,7)-R(0,1,8),\\
R(0,1,8)&=R(1,1,4)-R(0,2,4),\\
R(3,1,8)
&=R(4,1,4)-R(3,2,4),\\
R(4,1,4)&=R(0,2,4)-R(0,1,5),\\
R(2,1,9)
&=R(3,1,5)-R(2,2,5),\\
R(3,1,5)&=R(4,1,1)-R(3,2,1),\\
R(4,1,1)
&=R(0,2,1)-R(0,1,2).\end{aligned}$$ For the second term in [\[eq:appC-999-first\]](#eq:appC-999-first){reference-type="eqref" reference="eq:appC-999-first"}, $$\begin{aligned}
R(5,9,10)
&=R(1,10,10)-R(1,9,11)=4-1=3,\\
R(1,9,11)
&=-R(2,5,11)+R(1,5,12)=1,\\
R(2,5,11)
&=-R(3,1,11)+R(2,1,12)=-1,\\
R(3,1,11)
&=R(4,1,7)-R(3,2,7)=1,\\
R(4,1,7)
&=R(0,2,7)-R(0,1,8)=0,\\
R(2,1,12)
&=R(3,1,8)-R(2,2,8)=0,\\
R(1,5,12)
&=-R(2,1,12)+R(1,1,13)=0,\\
R(1,1,13)
&=R(2,1,9)-R(1,2,9)=0.\end{aligned}$$ Substitution into [\[eq:appC-999-first\]](#eq:appC-999-first){reference-type="eqref" reference="eq:appC-999-first"} yields $$R(9,9,9)=-3-3=-6.$$

The remaining two zero patterns have total exponent nine. Any application of a recurrence to a nonstandard triple of that total produces triples of total exponent six, all of whose terminal reductions differ from $(3,3,3)$. For example, $$\begin{aligned}
R(9,0,0)
&=R(5,1,0)-R(5,0,1)\\
&=\bigl(R(1,2,0)-R(1,1,1)\bigr)
-\bigl(R(1,1,1)-R(1,0,2)\bigr)=0,\end{aligned}$$ and $$\begin{aligned}
R(6,3,0)
&=R(2,4,0)-R(2,3,1)=0.\end{aligned}$$ The same total-degree argument handles every permutation. Together with the terminal identity $R(3,3,3)=1$, these paths establish every row of [\[eq:R-patterns\]](#eq:R-patterns){reference-type="eqref" reference="eq:R-patterns"}.

For completeness, the six groups in $t^3=(Q+U)^3$ now follow without suppressed multiplicities: $$\begin{aligned}
Q^3 &: 64^3(-6)=-1572864,\\
3Q^2U &: 3(64^2)(4)\,[3\cdot2]=294912,\\
3QU^2\text{, squares} &:3(64)(4^2)\,[3\cdot0]=0,\\
3QU^2\text{, cross terms} &:3(64)(4^2)\,[2\cdot3\cdot(-1)]=-18432,\\
U^3\text{, pure and }2+1 &:4^3\,[3\cdot0+3\cdot2\cdot3\cdot0]=0,\\
U^3\text{, fully mixed} &:4^3\,[6\cdot1]=384.\end{aligned}$$ Their sum is $-1296000$, as asserted.

# Formal period-three subtraction and local lengths {#app:local-length}

We expand the two local multiplicity cases in Proposition [\[prop:formal-subtraction\]](#prop:formal-subtraction){reference-type="ref" reference="prop:formal-subtraction"}. The argument takes place in completed local rings, so it retains nilpotents and intersection lengths.

First consider the fixed algebra. With $z=x^2-L$ and $q=4xz$, $$B_1=\mathbb C[x]/(z^2),
\qquad
q^2=16x^2z^2=0.$$ On the diagonal $x_0=x_1=x_2=x$, the complete-intersection Jacobian restricts to $$t_\varepsilon=q^3+3\varepsilon^2q=3\varepsilon^2q,$$ so $$t_\varepsilon^2=9\varepsilon^4q^2=0.$$ This identity holds on the entire length-four fixed algebra. It proves both that the fixed second-moment contribution vanishes and that nilpotent directions have not been discarded.

Let $\alpha$ be a root of multiplicity $r\in\{2,4\}$ and write $z_0=\alpha+\delta$. With $$x_0=z_0,
\qquad
x_1=z_0+u,
\qquad
x_2=z_0+v,$$ the period-three equations at $\varepsilon=1$ are $$\begin{aligned}
0&=p_L(z_0)+v-u,
\label{eq:appD-F0}\\
0&=p_L(z_0+u)-v,
\label{eq:appD-F1}\\
0&=p_L(z_0+v)+u.
\label{eq:appD-F2}\end{aligned}$$ The transverse linear part of the last two equations is $(u,v)\mapsto(-v,u)$, whose determinant is one. Thus [\[eq:appD-F1\]](#eq:appD-F1){reference-type="eqref" reference="eq:appD-F1"}--[\[eq:appD-F2\]](#eq:appD-F2){reference-type="eqref" reference="eq:appD-F2"} have unique formal solutions $u(\delta),v(\delta)$ with zero constant term.

Since $p_L(z_0)$ has order $r$, the equations first imply $u,v=O(\delta^r)$. Taylor expansion then gives $$\begin{aligned}
p_L(z_0+u)
&=p_L(z_0)+p_L'(z_0)u+O(u^2),\\
p_L(z_0+v)
&=p_L(z_0)+p_L'(z_0)v+O(v^2).\end{aligned}$$ Here $p_L'(z_0)=O(\delta^{r-1})$. Consequently $$p_L'(z_0)u, p_L'(z_0)v
=O(\delta^{2r-1}),$$ and the quadratic Taylor remainders have still higher order. Equations [\[eq:appD-F1\]](#eq:appD-F1){reference-type="eqref" reference="eq:appD-F1"}--[\[eq:appD-F2\]](#eq:appD-F2){reference-type="eqref" reference="eq:appD-F2"} therefore yield $$v=p_L(z_0)+O(\delta^{2r-1}),
\qquad
u=-p_L(z_0)+O(\delta^{2r-1}).
\label{eq:appD-uv}$$ Substitution in [\[eq:appD-F0\]](#eq:appD-F0){reference-type="eqref" reference="eq:appD-F0"} gives $$3p_L(\alpha+\delta)+O(\delta^{2r-1})=0.
\label{eq:appD-final}$$

For $r=2$, one has $L=\alpha^2\ne0$ and $$p_L(\alpha+\delta)
=\delta^2(2\alpha+\delta)^2
=4\alpha^2\delta^2+4\alpha\delta^3+\delta^4.$$ Equation [\[eq:appD-final\]](#eq:appD-final){reference-type="eqref" reference="eq:appD-final"} begins with $12\alpha^2\delta^2$; its error begins in order $2r-1=3$. The leading coefficient is nonzero, so the quotient has length two.

For $r=4$, necessarily $L=\alpha=0$ and $$p_0(\delta)=\delta^4.$$ Equation [\[eq:appD-final\]](#eq:appD-final){reference-type="eqref" reference="eq:appD-final"} is $3\delta^4+O(\delta^7)=0$, and its quotient has length four. Thus at both possible multiplicities, the local $f^3$-fixed length is exactly the fixed local length.

The full complete intersection is free of rank $64$, while the fixed algebra has total length $4$. Since the local calculation leaves no additional formal-period-three length at fixed support, prime-period subtraction produces pointwise length $60$. Only then may one group points into length-three orbits. The trace of the derivative product is constant around such an orbit by cyclic invariance, so the pointwise power sum is three times its cyclewise counterpart.

# Auxiliary coordinate, matrix, and valuation details {#app:auxiliary}

This appendix collects supporting expansions for Sections [2](#sec:setup){reference-type="ref" reference="sec:setup"}, [4](#sec:conservative){reference-type="ref" reference="sec:conservative"}, and [6](#sec:period-three){reference-type="ref" reference="sec:period-three"}. It introduces no additional hypothesis.

## Elementary-symmetric trace coordinates

Let $R$ be a parameter ring, let $B$ be finite locally free of rank $r$ over $R$, and let $u\in B$. Exterior powers give $$\det(T-M_u\mid B)
=
T^r+\sum_{j=1}^r(-1)^j
\operatorname{Tr}\!\left(\bigwedge^jM_u\right)T^{r-j}.$$ Each coefficient is a regular element of $R$ and commutes with arbitrary base change. Over a splitting field it becomes the elementary symmetric function of the formal eigenvalues of $M_u$. This construction explains simultaneously why the target is the affine symmetric product and why a nonreduced local factor contributes its full algebraic multiplicity. No ordering of periodic points is chosen.

For the residual action, the diagonal conjugacy $h_\zeta$ identifies the finite formal-period algebras and conjugates multiplication by the derivative trace. Characteristic polynomials are therefore unchanged. The coordinate morphism is $\mu_{d-1}$-invariant coefficient by coefficient, not only as a set of complex values.

## The embedded period-two cycle

On $a=1$, set $A_1=\mathbb C[x]/(p)$ and let $u$ be the class of $p'(x)$. The full period-two algebra is $A_1\otimes A_1$, and multiplication by the trace element is $$2I+M_u\otimes M_u.$$ If $\chi_u(T)=\prod_i(T-r_i)$ after a splitting base change, its characteristic polynomial is $$\chi_{\operatorname{Fix}(f^2)}(T)
=
\prod_{i,j=1}^4\bigl(T-(2+r_ir_j)\bigr).$$ The diagonal quotient $A_1\otimes A_1\to A_1$ sends the trace element to $2+u^2$, so the embedded fixed-cycle characteristic polynomial is $$\chi_{\operatorname{Fix}(f)}^{(2)}(T)
=
\prod_{i=1}^4\bigl(T-(2+r_i^2)\bigr).$$ The effective formal-cycle identity gives the monic polynomial quotient $$\chi_{\operatorname{Per}_2^*(f)}(T)
=
\frac{\chi_{\operatorname{Fix}(f^2)}(T)}{\chi_{\operatorname{Fix}(f)}^{(2)}(T)}$$ of degree twelve. The construction by finite algebras proves divisibility before any specialization and remains valid when several $r_i$ coincide or arise from a nilpotent local multiplication operator.

## The three-matrix trace

With $D_i=\left(\begin{smallmatrix}q_i&1\\1&0\end{smallmatrix}\right)$, $$D_1D_0
=
\begin{pmatrix}
q_1q_0+1&q_1\\
q_0&1
\end{pmatrix},$$ and hence $$D_2D_1D_0
=
\begin{pmatrix}
q_2q_1q_0+q_2+q_0&q_2q_1+1\\
q_1q_0+1&q_1
\end{pmatrix}.$$ Its trace is $$q_0q_1q_2+q_0+q_1+q_2.$$ This matches the determinant of the cyclic Jacobian matrix at $\varepsilon=1$. In the determinant, the two oriented three-cycles of off-diagonal $\varepsilon$ entries cancel, while choosing one diagonal $q_i$ and the complementary two-cycle contributes $+\varepsilon^2q_i$ for each $i$.

## Expanded Puiseux valuation branches

Assume $L\ne0$ and choose $\alpha^2=L$. Each coordinate specializes near either $\alpha$ or $-\alpha$. Since there are only two choices, a root triple is either constant or has exactly two equal entries.

For the second type, cyclically arrange $$(\alpha_0,\alpha_1,\alpha_2)=(\alpha,\alpha,-\alpha).$$ Writing $x_i=\alpha_i+\delta_i$, the constant parts of the couplings in $F_0,F_1$ are respectively $-2\alpha\varepsilon$ and $2\alpha\varepsilon$. Their valuations are one. The quadratic leading terms of $P_L(x_0)$ and $P_L(x_1)$ must balance them, so $$v(\delta_0)=v(\delta_1)=\tfrac12.$$ In $F_2$ the constant part of the coupling cancels, leaving $$\varepsilon(\delta_1-\delta_0),$$ of valuation at least $3/2$. If $v(\delta_2)<3/4$, then $P_L(x_2)$, of valuation $2v(\delta_2)$, would be the unique term of lowest valuation in $F_2$. Thus $v(\delta_2)\ge3/4$. Since $q_i$ has the same leading valuation as $\delta_i$, $$v(q_0q_1q_2)\ge\tfrac12+\tfrac12+\tfrac34=\tfrac74,
\qquad
v(\varepsilon^2q_i)\ge\tfrac52.$$

For a constant root triple, all constant coupling terms vanish. Let $$r=\min_i v(\delta_i)$$ on a nontrivial branch. Every coupling has valuation at least $1+r$. If $r<1$, an equation at an index attaining the minimum contains a quadratic term of valuation $2r<1+r$ with no term at the same valuation to cancel it. Hence $r\ge1$. It follows that $$v(q_0q_1q_2)\ge3,
\qquad
v(\varepsilon^2q_i)\ge3,$$ so $v(t_\varepsilon)\ge3$. The diagonal fixed branch is treated inside its local algebra in Appendix [12](#app:local-length){reference-type="ref" reference="app:local-length"}, where $t_\varepsilon^2=0$.

Thus every nonfixed branch contributes to the trace of $t_\varepsilon^2$ only above valuation two, and the fixed branch contributes zero. The $L^6\varepsilon^2$ coefficient vanishes for $L\ne0$. Because the trace is a polynomial in $L$ and $\varepsilon$, the same coefficient vanishes identically, including at $L=0$.
