---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--168-quartic-inverse-span-dynamics"
canonical_tex: "symbolic_dynamics/papers/168-quartic-inverse-span-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/168-quartic-inverse-span-dynamics/main.pdf"
source_sha256: "866951e658c3dd54c944e14c9d94b5690fa974e566d83bc35847663658571b8b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Quartic Inverse-Span Dynamics: Binary Depth Jump and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/168-quartic-inverse-span-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/168-quartic-inverse-span-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/168-quartic-inverse-span-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/168-quartic-inverse-span-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/168-quartic-inverse-span-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $p$ be prime and send each $\mathbb F_p$-subspace $A$ of $\mathbb F_{p^4}$ to the span of the inverses of its nonzero points. Published work already classifies when patched inversion carries a subspace onto a subspace and describes inverse projective lines; those facts receive no contribution credit here. We use them to determine the resulting finite functional graph. Its sharp maximum tail is two at $p=2$ and one at every odd prime: a non-subfield plane passes through a hyperplane only in the binary case. The recurrent states are zero, the full field, all lines, and all scalar copies of the quadratic subfield, and every period divides two. We give the exact depth enumerator, image stabilization, fixed-iterate counts, and dynamical zeta function. We also determine every target's fibre at every positive time. In particular, the $30$ transient planes over $\mathbb F_2$ distribute uniformly over the $15$ hyperplanes, two predecessors per target, before reaching the full field. A standalone exhaustive control checks $32{,}754$ assertions for $p=2,3,5$. This owner-dependent Round-0 note remains on external hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Quartic Inverse-Span Dynamics: Binary Depth Jump and Exact Fibres'
```

## Markdown 正文

# The literal map, published inputs, and theorem ceiling

Fix a prime $p$, set $K=\mathbb F_{p^4}$, and let $\mathcal X_p$ be the lattice of all $\mathbb F_p$-linear subspaces of $K$. For $A\in\mathcal X_p$, define $$\label{eq:map}
 \mathcal J(A)=\operatorname{span}_{\mathbb F_p}\{a^{-1}:a\in A\setminus\{0\}\},
 \qquad \mathcal J(0)=0.$$ The span in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is part of the update. Powers $\mathcal J^t$ mean iteration on the subspace lattice, not multiplicative powers of its points.

Two published inputs set a hard ceiling on the claims. First, Kolomeec and Bykov classify the affine $\mathbb F_p$-subspaces whose image under patched inversion $0\mapsto0$ is again affine: apart from the size-two boundary, they are exactly scalar copies of subfields [@KolomeecBykov2024]. Earlier inverse-closed and large-intersection results provide the algebraic context [@Mattarei2007; @Csajbok2013]. Second, inverse projective lines in the cyclic field model are known to be normal rational curves in their spans; the small-field regime gives independent tuples [@FainaEtAl2002; @LavrauwZanella2014]. We use the classification as an external proposition and include a short denominator-clearing calculation for the line span. Neither input is a contribution of this note.

For $A\in\mathcal X_p$, let $\operatorname{tail}(A)$ be the least time at which its orbit enters a cycle. Put $$\begin{aligned}
\label{eq:constants}
 L&=p^3+p^2+p+1, &
 P&=(p^2+1)(p^2+p+1), & Q&=p^2+1,\\
 S&=2+2L+P, & R&=2+L+Q, &
 F&=2+\gcd(2,L)+\gcd(2,Q). \notag\end{aligned}$$ Thus $L$ is the common number of lines and hyperplanes, $P$ is the number of planes, and $S=|\mathcal X_p|$. For $t\geq1$ and $B\in\mathcal X_p$, write $$\nu_t(B)=|\{A\in\mathcal X_p:\mathcal J^t(A)=B\}|.$$ The finite-map zeta function is understood formally as $$\zeta_{\mathcal J}(z)=\exp\!\left(\sum_{n\geq1}
          |\operatorname{Fix}(\mathcal J^n)|\frac{z^n}{n}\right),$$ following the periodic-point convention of @ArtinMazur1965.

[\[thm:main\]]{#thm:main label="thm:main"} For the map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, the following statements hold.

(i) The recurrent states are exactly $$\label{eq:recurrent}
     0,\qquad K,\qquad \xi\mathbb F_p,
     \qquad \xi\mathbb F_{p^2}\quad(\xi\in K^\times).$$ The rank transition outside this set is

      input                         number    $\dim\mathcal J(A)$   next state
      --------------------------- ---------- --------------------- ------------
      non-subfield plane, $p=2$    $P-Q=30$           $3$           hyperplane
      non-subfield plane, $p>2$     $P-Q$             $4$              $K$
      hyperplane                     $L$              $4$              $K$

    On the recurrent scalar subfields, $\mathcal J(\xi\mathbb F_{p^d})=\xi^{-1}\mathbb F_{p^d}$ for $d=1,2$; zero and $K$ are fixed.

(ii) The maximum tail and depth enumerator $D_p(u)=\sum_{A\in\mathcal X_p}u^{\operatorname{tail}(A)}$ are $$\label{eq:depth}
      \max_A\operatorname{tail}(A)=
      \begin{cases}2,&p=2,\\1,&p>2,\end{cases}
      \qquad
      D_p(u)=
      \begin{cases}
      R+Lu+(P-Q)u^2,&p=2,\\
      R+(S-R)u,&p>2.
      \end{cases}$$ Moreover, $$\label{eq:image-stabilization}
      |\mathcal J^t(\mathcal X_p)|=
      \begin{cases}
      S,&t=0,\\
      R+L,&p=2,\ t=1,\\
      R,&p=2,\ t\geq2,\\
      R,&p>2,\ t\geq1.
      \end{cases}$$

(iii) There are $R$ recurrent states and $F$ fixed states; the remaining $R-F$ recurrent states form $(R-F)/2$ two-cycles. Hence $$\label{eq:fix-iterates}
       |\operatorname{Fix}(\mathcal J^n)|=
       \begin{cases}F,&n\text{ odd},\\R,&n\text{ even},\end{cases}
       \qquad
       \zeta_{\mathcal J}(z)=(1-z)^{-F}(1-z^2)^{-(R-F)/2}.$$ In particular, $F=4$ for $p=2$ and $F=6$ for odd $p$.

(iv) Every positive-time target fibre is $$\label{eq:fibres}
      \nu_t(B)=
      \begin{cases}
      1,&B\in\operatorname{Rec}(\mathcal J),\ B\ne K,\\
      2,&p=2,\ t=1,\ \dim B=3,\\
      1+L,&p=2,\ t=1,\ B=K,\\
      1+L+P-Q,&p=2,\ t\geq2,\ B=K,\\
      1+L+P-Q,&p>2,\ B=K,\\
      0,&\text{otherwise}.
      \end{cases}$$

(v) Every transient state lies in the component of the fixed state $K$. For odd $p$, that component is a star whose leaves are all hyperplanes and non-subfield planes. For $p=2$, its first level consists of the $15$ hyperplanes, each with exactly two non-subfield-plane children. Every other fixed point or two-cycle is a bare component. Thus the number of weak components is $(R+F)/2$.

The residual theorem is the conjunction of the sharp characteristic dichotomy, the complete graph and image stabilization, and the all-time target fibres. The recurrent classification, inverse-line geometry, Gaussian counts, Singer action, and zeta conversion are treated as inputs or standard consequences. No novelty or priority inference is made.

# Rank growth and the inverse of a plane

[\[lem:rank\]]{#lem:rank label="lem:rank"} For every $A\in\mathcal X_p$, $$\label{eq:rank}
 \dim\mathcal J(A)\geq\dim A.$$ If equality holds, then $$\label{eq:equality}
 \mathcal J(A)=A^{-1}\cup\{0\},\qquad \mathcal J^2(A)=A.$$ Consequently, $A$ is recurrent if and only if equality holds in [\[eq:rank\]](#eq:rank){reference-type="eqref" reference="eq:rank"}, and every recurrent period divides two.

If $d=\dim A$, inversion gives $p^d-1$ distinct nonzero elements inside $\mathcal J(A)$. An $r$-dimensional subspace has only $p^r-1$ nonzero elements, so $r\geq d$. When $r=d$, cardinality forces the first identity in [\[eq:equality\]](#eq:equality){reference-type="eqref" reference="eq:equality"}; patched inversion and a second span give the second.

Dimensions are nondecreasing along every orbit. They must be constant on a cycle, so recurrence forces equality at the first edge. Conversely, [\[eq:equality\]](#eq:equality){reference-type="eqref" reference="eq:equality"} places $A$ on a cycle of length at most two.

We record the exact external input used with Lemma [\[lem:rank\]](#lem:rank){reference-type="ref" reference="lem:rank"}.

[\[prop:external\]]{#prop:external label="prop:external"} Let $E$ be a finite field of characteristic $p$, and patch inversion by $0^{-1}=0$. If an affine $\mathbb F_p$-subspace $A\subseteq E$ has $|A|>2$, then its inverse image is an affine subspace if and only if $A=\xi\mathbb F_{p^d}$ for a subfield $\mathbb F_{p^d}\subseteq E$ and $\xi\in E^\times$.

Proposition [\[prop:external\]](#prop:external){reference-type="ref" reference="prop:external"} receives zero contribution credit. It immediately rules out equality for a three-dimensional subspace of $\mathbb F_{p^4}$, since a subfield degree must divide four. The binary lines have size two, outside the stated hypothesis, but their behavior is direct.

The next calculation exposes exactly where the prime two differs. Its projective interpretation is already contained in inverse-line geometry [@FainaEtAl2002; @LavrauwZanella2014].

[\[lem:plane\]]{#lem:plane label="lem:plane"} Let $A$ be a plane in $K$. Then $$\label{eq:plane-rank}
 \dim\mathcal J(A)=
 \begin{cases}
 2,&A=\xi\mathbb F_{p^2},\\
 3,&A\ne\xi\mathbb F_{p^2}\text{ and }p=2,\\
 4,&A\ne\xi\mathbb F_{p^2}\text{ and }p>2.
 \end{cases}$$

After scaling, write $A=\xi\langle1,\alpha\rangle_{\mathbb F_p}$ and put $r=[\mathbb F_p(\alpha):\mathbb F_p]$. Since $\alpha\in\mathbb F_{p^4}\setminus\mathbb F_p$, we have $r\in\{2,4\}$. Projective representatives for the inverse points, after discarding the harmless scalar $\xi^{-1}$, are $$\label{eq:representatives}
 1,\qquad(\alpha-t)^{-1}\quad(t\in\mathbb F_p).$$

Choose distinct $t_1,\ldots,t_s\in\mathbb F_p$ with $s+1\leq r$. A relation $$c_0+\sum_{i=1}^{s}\frac{c_i}{\alpha-t_i}=0$$ becomes $G(\alpha)=0$ after multiplication by $D(\alpha)=\prod_i(\alpha-t_i)$, where $$G(x)=c_0D(x)+\sum_{i=1}^{s}c_i\frac{D(x)}{x-t_i}$$ has degree at most $s<r$. Minimality of $r$ gives $G=0$. Evaluating this polynomial identity at $t_i$ yields $c_i\prod_{j\ne i}(t_i-t_j)=0$, so every $c_i$ and then $c_0$ vanish. Thus the span of [\[eq:representatives\]](#eq:representatives){reference-type="eqref" reference="eq:representatives"} has dimension $\min\{p+1,r\}$.

If $r=2$, then $\langle1,\alpha\rangle=\mathbb F_{p^2}$. If $r=4$, the minimum is three at $p=2$ and four for every odd prime. Restoring $\xi$ proves [\[eq:plane-rank\]](#eq:plane-rank){reference-type="eqref" reference="eq:plane-rank"}.

[\[cor:transitions\]]{#cor:transitions label="cor:transitions"} Every hyperplane maps to $K$. Every non-subfield plane maps to a hyperplane at $p=2$ and to $K$ at odd $p$.

Lemma [\[lem:rank\]](#lem:rank){reference-type="ref" reference="lem:rank"} leaves image dimension three or four for a hyperplane. Equality at three contradicts Proposition [\[prop:external\]](#prop:external){reference-type="ref" reference="prop:external"}, so its image is $K$. Lemma [\[lem:plane\]](#lem:plane){reference-type="ref" reference="lem:plane"} handles planes.

# Sharp time and the recurrent core

By Lemma [\[lem:rank\]](#lem:rank){reference-type="ref" reference="lem:rank"}, a recurrent state of dimension at least two has a patched inverse image that is a subspace. Proposition [\[prop:external\]](#prop:external){reference-type="ref" reference="prop:external"} therefore makes it a scalar subfield. The subfield degrees inside four are $1,2,4$. Lines, including binary lines, satisfy $\mathcal J(\xi\mathbb F_p)=\xi^{-1}\mathbb F_p$ directly; the same identity holds for scalar quadratic subfields. This proves [\[eq:recurrent\]](#eq:recurrent){reference-type="eqref" reference="eq:recurrent"}. Corollary [\[cor:transitions\]](#cor:transitions){reference-type="ref" reference="cor:transitions"} supplies the remaining rows of the transition table.

There are $L$ lines, $P$ planes, and $L$ hyperplanes. Scalar quadratic subfields are parametrized by $K^\times/\mathbb F_{p^2}^\times$, so their number is $(p^4-1)/(p^2-1)=Q$. This proves the state count $S$ and recurrent count $R$ in [\[eq:constants\]](#eq:constants){reference-type="eqref" reference="eq:constants"}.

Every hyperplane has tail one. At an odd prime every non-subfield plane also has tail one, whereas at $p=2$ it has tail two by Corollary [\[cor:transitions\]](#cor:transitions){reference-type="ref" reference="cor:transitions"}. Since $P-Q=(p^2+1)(p^2+p)>0$, both bounds are attained. Counting these strata gives [\[eq:depth\]](#eq:depth){reference-type="eqref" reference="eq:depth"}; it also shows that $\mathcal J^2(\mathcal X_2)$ and $\mathcal J(\mathcal X_p)$ for odd $p$ lie in the recurrent core.

On recurrent lines, $\mathcal J$ induces inversion on the cyclic quotient $K^\times/\mathbb F_p^\times$, which has order $L$. On recurrent planes it induces inversion on the cyclic quotient $K^\times/\mathbb F_{p^2}^\times$, of order $Q$. Inversion on a cyclic group of order $m$ has $\gcd(2,m)$ fixed points. Adding zero and $K$ gives $F$ fixed states; Lemma [\[lem:rank\]](#lem:rank){reference-type="ref" reference="lem:rank"} allows no periods beyond two. Thus the other $R-F$ recurrent states form $(R-F)/2$ two-cycles. Since $L$ and $Q$ are odd at $p=2$ and even at odd $p$, the displayed values of $F$ follow.

The fixed-iterate count in [\[eq:fix-iterates\]](#eq:fix-iterates){reference-type="eqref" reference="eq:fix-iterates"} is now immediate. Taking the exponential of its defining series, or multiplying the standard factors for fixed points and two-cycles, gives the stated zeta function.

The time jump is therefore a projective-cardinality effect. It does not come from a different rule in characteristic two: the literal update [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is uniform in $p$.

# Every-target fibres and the component graph

Only the binary plane-to-hyperplane row requires a target-resolved count.

[\[lem:singer\]]{#lem:singer label="lem:singer"} For $\lambda\in K^\times$ and $A\in\mathcal X_p$, $$\label{eq:twisted}
 \mathcal J(\lambda A)=\lambda^{-1}\mathcal J(A).$$ The scalar action of $K^\times$ is transitive on the hyperplanes of $K$. Consequently, at $p=2$ every hyperplane has exactly two non-subfield-plane predecessors.

Equation [\[eq:twisted\]](#eq:twisted){reference-type="eqref" reference="eq:twisted"} follows by inverting every nonzero element before taking the span. The trace pairing on the separable extension $K/\mathbb F_p$ is nondegenerate. Hence every hyperplane is $$H_c=\{x\in K:\operatorname{Tr}_{K/\mathbb F_p}(cx)=0\}$$ for some $c\in K^\times$, unique modulo $\mathbb F_p^\times$. Scalar multiplication sends these kernels transitively to one another.

At $p=2$, Lemma [\[lem:plane\]](#lem:plane){reference-type="ref" reference="lem:plane"} sends all $P-Q=30$ non-subfield planes to hyperplanes. Twisted scalar symmetry gives bijections between the fibres over any two hyperplanes, so their sizes are constant. There are $L=15$ targets, and $30/15=2$ sources lie over each.

Lemma [\[lem:singer\]](#lem:singer){reference-type="ref" reference="lem:singer"} shows that every binary hyperplane occurs at time one. Together with the recurrent core this gives $|\mathcal J(\mathcal X_2)|=R+L$. Every such hyperplane maps to $K$, so the second image is exactly the recurrent core. At odd primes the transition table already sends every transient state to $K$, proving all of [\[eq:image-stabilization\]](#eq:image-stabilization){reference-type="eqref" reference="eq:image-stabilization"}.

The restriction of $\mathcal J$ to the recurrent core is an involutive bijection. Every recurrent target other than $K$ therefore has exactly one predecessor at every positive time. No transient state can be an additional predecessor: the transition table sends every transient orbit toward $K$.

A non-subfield plane has no predecessor. Indeed, a source of smaller rank cannot reach a plane, while a plane source with plane image would be an equality case and hence recurrent. At odd primes no update lands on a hyperplane. In the binary case Lemma [\[lem:singer\]](#lem:singer){reference-type="ref" reference="lem:singer"} gives its two predecessors at time one; one further update sends every one of those paths to $K$, so hyperplane fibres vanish for $t\geq2$.

At binary time one, the full field receives itself and all $L$ hyperplanes, giving $1+L$ sources. From time two onward it also receives all $P-Q$ non-subfield planes, giving $1+L+P-Q$. At odd primes those planes arrive in one step, so the latter count holds for every $t\geq1$. This proves [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"}.

The same argument identifies the components. Every transient state reaches $K$, and [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"} shows that no transient tree attaches to any other recurrent cycle. For odd $p$ all transient vertices are leaves. At $p=2$, Lemma [\[lem:singer\]](#lem:singer){reference-type="ref" reference="lem:singer"} gives the uniform two-level tree described in part (v). The recurrent core has $F$ fixed cycles and $(R-F)/2$ two-cycles, so it has $(R+F)/2$ components.

# Exact controls and scope

The formulas specialize as follows. The depth column lists the numbers at successive tail depths, and the last column gives the full-field fibre at times one and two.

   $p$     $S$   $|\operatorname{im}\mathcal J|$   $R$   $F$ cycles                depths   $\nu_{1,2}(K)$
  ----- ------ --------------------------------- ----- ----- --------------- ------------ ----------------
    2       67                                37    22     4 $1^4\,2^9$        $22,15,30$          $16,46$
    3      212                                52    52     6 $1^6\,2^{23}$       $52,160$        $161,161$
    5     1120                               184   184     6 $1^6\,2^{89}$      $184,936$        $937,937$

A paper-local Python verifier uses only the standard library. It constructs an irreducible quartic for each of $p=2,3,5$, implements field arithmetic, enumerates every subspace in reduced row-echelon form, and recomputes every directed edge. It then checks the recurrent scalar-subfield classification, rank transitions, cycles, depth histograms, images, twisted scalar symmetry, and every target fibre at times one through four. Two fresh processes match the frozen $32{,}754$-assertion transcript byte for byte. These exhaustive finite checks are controls for implementation and boundary errors; the proofs above establish the formulas.

The scope is deliberately narrow. The base field is prime and the extension degree is four. The published inverse-image classification and inverse-line geometry remain zero-credit inputs, and the cycle/zeta count is a short consequence once the recurrent core is known. What remains in the note is only the exact temporal anomaly, complete graph and stabilization, and all-time target-fibre synthesis for the literal map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. The bounded source search gives no novelty or priority conclusion. This anonymous Round-0 artifact is `GREEN_OWNER_THIN / HOLD_EXTERNAL`.
