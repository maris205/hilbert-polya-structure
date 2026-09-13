---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--142-valuation-gcd-prime-power-divisors"
canonical_tex: "symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors/main.tex"
canonical_pdf: "symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors/main.pdf"
source_sha256: "10cf04525c06f86330bd2db7e99a74c54c42c516cd7f2209ba89b62611ef8a9b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Valuation--GCD Dynamics on Prime-Power Divisors: Exact Entry Times and Every-Target Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/142-valuation-gcd-prime-power-divisors/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix an odd prime $p$ and $e\geq2$. On the divisor chain of $p^e$, consider $d\mapsto\gcd(p^e,d^2+p^e/d)$. Under $p^a\leftrightarrow a$, the literal integer map is exactly $a\mapsto\min(2a,e-a)$. We give its complete finite atlas. The recurrent exponents are $0$ together with the integer band from $\lceil e/3\rceil$ to $\lfloor2e/3\rfloor$; the band consists of fixed points and complement two-cycles. We prove a four-case pointwise entry-time formula, an exact temporal polynomial, and a sharp maximum $1+\lceil\log_2\lceil e/3\rceil\rceil$. For $e\geq4$, the unique deepest divisor is $p^{e-1}$; the cases $e=2,3$ have the unique deepest divisor $p^e$. The image is an interval in valuation coordinates, and every target fibre is the set union of at most two explicit inverse branches. Oddness is necessary: when $p=2$ and $e=3a$, equal valuations create one extra factor of two. General valuation algebra, functional-graph bookkeeping, interval-map theory, and discretized tent maps receive zero contribution credit. Exact computation is used only for falsification, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Valuation--GCD Dynamics on Prime-Power Divisors: Exact Entry Times and Every-Target Fibres'
```

## Markdown 正文

# Scope and complete statement

Piecewise-monotone interval maps have an extensive general theory [@MilnorThurston1988], and finite tent-type discretizations have been studied in both reversible and bijective forms [@Kuzovlev2004; @ChoiEtAl2026]. Those theories receive zero contribution credit here. This note concerns one literal arithmetic self-map and does not claim that its piecewise-linear silhouette is new.

Fix an odd prime $p$ and an integer $e\geq2$. Define $$\label{eq:literal-map}
 \mathcal X_{p,e}=\{p^a:0\leq a\leq e\},\qquad
 \mathsf F_{p,e}(d)=\gcd\!\left(p^e,d^2+\frac{p^e}{d}\right).$$ Put $$\label{eq:parameters}
 L=\left\lceil\frac e3\right\rceil,
 \qquad U=\left\lfloor\frac{2e}{3}\right\rfloor,
 \qquad R=U-L+2,
 \qquad A=1+\boldsymbol 1_{2\mid e}.$$ For a positive rational number $x$, $\lceil\log_2x\rceil$ is used below only when $x\geq1$ and means the least integer $j\geq0$ with $2^j\geq x$.

Under the identification $p^a\leftrightarrow a$, let $\mathsf T_e$ denote the exponent map. The entry time $\tau_e(a)$ is the least $t\geq0$ for which $\mathsf T_e^t(a)$ is recurrent. The following is the claim ceiling for the note.

[\[thm:main\]]{#thm:main label="thm:main"} For every odd prime $p$ and $e\geq2$, the following hold.

1.  The literal valuation identity is $$\label{eq:conjugacy}
     \mathsf F_{p,e}(p^a)=p^{\mathsf T_e(a)},
     \qquad \mathsf T_e(a)=\min(2a,e-a).$$

2.  The recurrent exponent set is $$\label{eq:recurrent-set}
     \operatorname{Rec}(\mathsf T_e)=\{0\}\cup\{L,L+1,\ldots,U\}.$$ It has $R$ elements, of which $A$ are fixed; all other recurrent exponents form strict complement two-cycles. For every $k\geq1$, $$\label{eq:fixed-iterates}
     |\operatorname{Fix}(\mathsf T_e^k)|=
     \begin{cases}
     A,&k\text{ odd},\\
     R,&k\text{ even}.
     \end{cases}$$

3.  The complete pointwise entry law is $$\label{eq:entry-law}
     \tau_e(a)=
     \begin{cases}
     0,&a=0\text{ or }L\leq a\leq U,\\
     \left\lceil\log_2(L/a)\right\rceil,&1\leq a<L,\\
     1,&a=e,\\
     1+\left\lceil\log_2\bigl(L/(e-a)\bigr)\right\rceil,
          &U<a<e.
     \end{cases}$$ Consequently $$\label{eq:max-clock}
     M_e:=\max_{0\leq a\leq e}\tau_e(a)
     =1+\left\lceil\log_2L\right\rceil.$$ For $e\geq4$, the unique deepest exponent is $e-1$; for $e=2,3$, it is $e$.

4.  Let $m=\lceil\log_2L\rceil$ and, for $1\leq j\leq m$, put $$\label{eq:cj}
     c_j=\left\lceil\frac{L}{2^{j-1}}\right\rceil
         -\left\lceil\frac{L}{2^j}\right\rceil.$$ Then the complete temporal polynomial is $$\label{eq:temporal-polynomial}
     D_e(z):=\sum_{a=0}^{e}z^{\tau_e(a)}
     =R+z+(1+z)\sum_{j=1}^{m}c_jz^j.$$

5.  The image and every-target fibres are $$\label{eq:image}
     \operatorname{im}\mathsf T_e=\{0,1,\ldots,U\},$$ and, for $0\leq b\leq e$, $$\label{eq:fibre}
     \mathsf T_e^{-1}(b)=
     \begin{cases}
     \{e-b\}\cup
       \bigl(\{b/2\}\text{ if }2\mid b\bigr),&0\leq b\leq U,\\
     \varnothing,&U<b\leq e.
     \end{cases}$$ The union is a set: its two displayed candidates coincide exactly when $3b=2e$.

The next four sections prove the five parts of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. No finite enumeration is used in those proofs.

# Literal valuation and the binary boundary

[\[lem:valuation\]]{#lem:valuation label="lem:valuation"} For $0\leq a\leq e$, equation [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"} holds.

The argument inside the gcd is $$\label{eq:sum-powers}
 (p^a)^2+\frac{p^e}{p^a}=p^{2a}+p^{e-a}.$$ Set $q=\min(2a,e-a)$. If $3a\neq e$, the two exponents in [\[eq:sum-powers\]](#eq:sum-powers){reference-type="eqref" reference="eq:sum-powers"} differ, and factoring out the smaller one gives $$p^{2a}+p^{e-a}=p^q\bigl(1+p^{|3a-e|}\bigr).$$ The factor in parentheses is not divisible by $p$. If $3a=e$, then $$p^{2a}+p^{e-a}=2p^{2a}=2p^q,$$ and $2$ is again a $p$-adic unit because $p$ is odd. Thus the valuation of [\[eq:sum-powers\]](#eq:sum-powers){reference-type="eqref" reference="eq:sum-powers"} is always $q$. Since $0\leq q\leq e$, taking the gcd with $p^e$ gives $p^q$, which is [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"}.

[\[rem:binary\]]{#rem:binary label="rem:binary"} Oddness cannot be removed from [\[lem:valuation\]](#lem:valuation){reference-type="ref" reference="lem:valuation"}. If $p=2$ and $e=3a$ with $a\geq1$, then $$2^{2a}+2^{e-a}=2^{2a}+2^{2a}=2^{2a+1}.$$ Because $2a+1\leq3a=e$, the literal gcd has valuation $2a+1$, rather than $\min(2a,e-a)=2a$. The smallest witness is $$\gcd(2^3,2^2+2^2)=2^3.$$ This note uses the binary calculation only as a boundary; it claims no replacement atlas for $p=2$.

# The recurrent band and fixed iterates

The elementary identities $$\label{eq:complement-endpoints}
 e-U=L,\qquad e-L=U$$ follow directly from [\[eq:parameters\]](#eq:parameters){reference-type="eqref" reference="eq:parameters"}. They make the two branches of $\mathsf T_e$ especially rigid.

[\[lem:branches\]]{#lem:branches label="lem:branches"} The exponent map satisfies $$\label{eq:branch-form}
 \mathsf T_e(a)=
 \begin{cases}
 2a,&0\leq a<L,\\
 e-a,&L\leq a\leq e.
 \end{cases}$$ The interval $[L,U]$ is invariant and is acted on by $a\mapsto e-a$. Moreover, if $1\leq a<L$ and $j$ is least with $2^ja\geq L$, then $2^ja\leq U$.

The two arguments in the minimum [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"} satisfy $2a\leq e-a$ exactly when $3a\leq e$. Every integer $a<L=\lceil e/3\rceil$ has $3a<e$, while every $a\geq L$ has $3a\geq e$, proving [\[eq:branch-form\]](#eq:branch-form){reference-type="eqref" reference="eq:branch-form"}. If $L\leq a\leq U$, then [\[eq:complement-endpoints\]](#eq:complement-endpoints){reference-type="eqref" reference="eq:complement-endpoints"} gives $L\leq e-a\leq U$, so the band is invariant and the stated complement rule holds there.

It remains to exclude an overshoot by the last doubling. Minimality of $j$ gives $2^{j-1}a<L\leq2^ja$, so $2^ja<2L$. If $e=3q$, then $(L,U)=(q,2q)$; if $e=3q+2$, then $(L,U)=(q+1,2q+1)$. In either case the integer $2^ja<2L$ is at most $U$. If $e=3q+1$, then $(L,U)=(q+1,2q)= (L,2L-2)$. Here $j\geq1$, so $2^ja$ is even. It is less than $2L$ and therefore cannot equal the odd integer $2L-1$; hence it is at most $2L-2=U$.

[\[thm:recurrence\]]{#thm:recurrence label="thm:recurrence"} Equations [\[eq:recurrent-set\]](#eq:recurrent-set){reference-type="eqref" reference="eq:recurrent-set"} and [\[eq:fixed-iterates\]](#eq:fixed-iterates){reference-type="eqref" reference="eq:fixed-iterates"} hold.

Zero is fixed. By [\[lem:branches\]](#lem:branches){reference-type="ref" reference="lem:branches"}, every positive exponent below $L$ doubles until its first entry into $[L,U]$. If $a>U$, its first image is $e-a<L$; this image is zero only when $a=e$, and otherwise the preceding doubling argument applies. Thus every exponent enters the set displayed in [\[eq:recurrent-set\]](#eq:recurrent-set){reference-type="eqref" reference="eq:recurrent-set"}.

On $[L,U]$, the map is the involution $a\mapsto e-a$. Hence every point of that band is recurrent. Conversely, every state outside the displayed set eventually enters the displayed invariant set and never leaves it, so it cannot return to its outside starting state and is not recurrent. This proves [\[eq:recurrent-set\]](#eq:recurrent-set){reference-type="eqref" reference="eq:recurrent-set"}. Its size is $1+(U-L+1)=R$.

Within the band, a fixed exponent satisfies $2a=e$, so it exists exactly when $e$ is even and is then $e/2$. Together with zero, this gives $A$ fixed states. Every other band exponent is in a strict pair $\{a,e-a\}$. A transient point cannot be fixed by a positive iterate. An odd iterate fixes only the $A$ fixed states, whereas an even iterate fixes all $R$ recurrent states, proving [\[eq:fixed-iterates\]](#eq:fixed-iterates){reference-type="eqref" reference="eq:fixed-iterates"}.

For completeness, define the formal Artin--Mazur zeta function by $\zeta_e(z)=\exp(\sum_{k\geq1}|\operatorname{Fix}(\mathsf T_e^k)|z^k/k)$. The cycle census in [\[thm:recurrence\]](#thm:recurrence){reference-type="ref" reference="thm:recurrence"} immediately gives $$\label{eq:zeta}
 \zeta_e(z)=(1-z)^{-A}(1-z^2)^{-(R-A)/2}.$$ Equation [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is standard finite-map bookkeeping and receives zero contribution credit.

# Pointwise times and the temporal polynomial

[\[thm:entry\]]{#thm:entry label="thm:entry"} Equations [\[eq:entry-law\]](#eq:entry-law){reference-type="eqref" reference="eq:entry-law"} and [\[eq:max-clock\]](#eq:max-clock){reference-type="eqref" reference="eq:max-clock"} hold, including the stated unique deepest exponents.

The entry time is zero on the recurrent set. If $1\leq a<L$, then [\[lem:branches\]](#lem:branches){reference-type="ref" reference="lem:branches"} shows that the orbit is $a,2a,4a,\ldots$ until its first band entry. The least number of doublings needed is the least $j$ such that $2^ja\geq L$, namely $\lceil\log_2(L/a)\rceil$. The last assertion of [\[lem:branches\]](#lem:branches){reference-type="ref" reference="lem:branches"} ensures that this first crossing lies in the recurrent band.

If $U<a<e$, the first step sends $a$ to the positive lower exponent $b=e-a<L$, after which the lower formula applies. If $a=e$, the first image is zero. These cases prove [\[eq:entry-law\]](#eq:entry-law){reference-type="eqref" reference="eq:entry-law"}.

Put $m=\lceil\log_2L\rceil$. Lower exponents have depth at most $m$. Upper exponents other than $e$ have the form $e-b$ with $1\leq b<L$ and depth $1+\lceil\log_2(L/b)\rceil$, so their depth is at most $1+m$. The choice $b=1$, or $a=e-1$, attains $1+m$. Suppose $e\geq4$; then $L\geq2$ and $m\geq1$. For $b\geq2$, $$\frac Lb\leq\frac L2\leq2^{m-1},$$ so its upper partner has depth at most $m$. The lower branch also has depth at most $m$, and $a=e$ has depth one. Thus $e-1$ is the unique exponent of depth $1+m$, proving [\[eq:max-clock\]](#eq:max-clock){reference-type="eqref" reference="eq:max-clock"} and uniqueness. When $e=2$ or $3$, one has $L=1$; the recurrent set contains every exponent except $e$, which maps to zero in one step. Hence $e$ is the unique deepest exponent in both small cases.

[\[thm:temporal\]]{#thm:temporal label="thm:temporal"} Equation [\[eq:temporal-polynomial\]](#eq:temporal-polynomial){reference-type="eqref" reference="eq:temporal-polynomial"} holds.

For $1\leq j\leq m$, a lower exponent $a$ has depth exactly $j$ if and only if $$2^{j-1}a<L\leq2^ja.$$ Equivalently, $$\left\lceil\frac{L}{2^j}\right\rceil
 \leq a\leq
 \left\lceil\frac{L}{2^{j-1}}\right\rceil-1.$$ This interval contains exactly $c_j$ integers. These intervals partition $\{1,\ldots,L-1\}$.

Reflection $a\mapsto e-a$ is a bijection from the lower transient exponents to $\{U+1,\ldots,e-1\}$. By [\[eq:entry-law\]](#eq:entry-law){reference-type="eqref" reference="eq:entry-law"}, it increases every depth by one. The recurrent set contributes $R$ states of depth zero, and the remaining exponent $e$ contributes one state of depth one. Therefore each lower layer contributes $c_jz^j$, its reflected layer contributes $c_jz^{j+1}$, and summing all contributions gives $$D_e(z)=R+z+\sum_{j=1}^{m}c_j(z^j+z^{j+1}),$$ which is [\[eq:temporal-polynomial\]](#eq:temporal-polynomial){reference-type="eqref" reference="eq:temporal-polynomial"}.

For example, the exact sharp profile at $e=128$ is $$D_{128}(z)=44+22z+32z^2+16z^3+8z^4+4z^5+2z^6+z^7,$$ and exponent $127$ is the unique depth-seven state.

# Image and every-target fibres

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} Equations [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} and [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} hold for every target $0\leq b\leq e$.

The doubling branch $\mathsf T_e(a)=2a$ applies precisely when $3a\leq e$. Consequently it reaches a target $b$ precisely when $b$ is even, $a=b/2$, and $$3b\leq2e.$$ The reflection branch $\mathsf T_e(a)=e-a$ applies precisely when $3a\geq e$. Its only possible source over $b$ is $a=e-b$, and the branch condition is again $$3(e-b)\geq e\quad\Longleftrightarrow\quad3b\leq2e.$$ At $3a=e$ the two branch labels deliberately overlap, because their values are equal; this is exactly the possible coincidence handled by the set union. For integer $b$, this common inequality is equivalent to $b\leq\lfloor2e/3\rfloor=U$. Hence every $b\leq U$ has the reflection source $e-b$ and, when $b$ is even, the doubling source $b/2$; no $b>U$ has a source. This proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Since the reflection source exists for every $0\leq b\leq U$, it also proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

Finally, the two candidate sources agree exactly when $e-b=b/2$, equivalently $3b=2e$. Treating [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} as a set union therefore gives the correct singleton in the coincident-branch case.

Transporting [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} back through $p^a\leftrightarrow a$ gives the literal divisor fibre $$\mathsf F_{p,e}^{-1}(p^b)=
 \{p^{e-b}\}\cup
 \bigl(\{p^{b/2}\}\text{ if }2\mid b\bigr)
 \quad(0\leq b\leq U),$$ and the empty set for $b>U$.

# Exact controls, zero-credit boundary, and hold

The local verifier recomputes the integer gcd in [\[eq:literal-map\]](#eq:literal-map){reference-type="eqref" reference="eq:literal-map"} for every state with $p\in\{3,5,7,11\}$ and $2\leq e\leq128$. It then builds each complete functional graph and checks recurrence, fixed iterates through $k=12$, every pointwise time, the temporal polynomial, the image, and every target fibre. A separate binary lane checks every state for $2\leq e\leq48$, including all equal-valuation exceptions. The audit uses exact integers without sampling, floating point, a computer algebra system, or a third-party package.

::: {#tab:controls}
  control                                         exact count
  --------------------------------------------- -------------
  odd-prime parameter boxes                               508
  odd-prime states, orbits, and target fibres     33,528 each
  binary parameter boxes / states                  47 / 1,222
  binary equal-valuation cases                             16
  Boolean assertions                                  319,074

  : Dependency-free falsification controls. These counts are not proofs of the all-parameter statements and are not ownership evidence.
:::

The conceptual boundary is equally important. General valuation rules, ceiling-log algebra, functional-graph and zeta identities, and formal generating functions are standard tools and receive zero credit. General piecewise-monotone theory [@MilnorThurston1988], reversible discrete tent-map cycle studies [@Kuzovlev2004], and bijective finite skew-tent constructions [@ChoiEtAl2026] also receive zero credit. The normalized real map $x\mapsto\min(2x,1-x)$ already exposes the doubling/reflection silhouette.

The residual is therefore narrow: the literal odd-prime divisor--gcd system together with its complete arithmetic temporal and inverse atlas. A bounded search did not locate a direct printed owner for that exact conjunction, but absence from a bounded search is not novelty, priority, authorship, or ownership evidence. If a direct owner is found, or if specialist review judges the arithmetic carrier to be merely decorative, the residual should be killed rather than broadened. No external posting, contact, submission, or release is authorized; status remains `HOLD_EXTERNAL`.
