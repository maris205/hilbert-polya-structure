---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--128-translation-gcd-depth-fibres"
canonical_tex: "symbolic_dynamics/papers/128-translation-gcd-depth-fibres/main.tex"
canonical_pdf: "symbolic_dynamics/papers/128-translation-gcd-depth-fibres/main.pdf"
source_sha256: "fa1c10facf18dbb215896da5d4e6b36af446ce60f85208c1a632159f4d0ee1c7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Depth Enumeration and Terminal Fibres for Translation--GCD Erosion over Finite Fields

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/128-translation-gcd-depth-fibres>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/128-translation-gcd-depth-fibres/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/128-translation-gcd-depth-fibres/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/128-translation-gcd-depth-fibres/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/128-translation-gcd-depth-fibres/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $q=p^a$ and iterate $T(f)=\gcd(f(x),f(x+1))$ on monic polynomials over $\mathbb F_q$. Translation has order $p$, so the process reaches the invariant core $Q(f)=T^{p-1}(f)$. We determine, for every $0\leq t\leq p-1$, an exact all-degree generating function for the states whose stabilization depth is at most $t$. On each nonfixed orbit of irreducible factors, subtracting the minimum exponent leaves a cyclic nonnegative vector with a zero; its depth is its longest positive run. A finite run automaton supplies the local series, and a formal orbit Euler product over irreducible translation orbits gives the global census. We also prove a unique graded split into an invariant core and the unit fibre $Q^{-1}(1)$. Its generating function is $(1-qz^p)/(1-qz)$, yielding the exact-degree and degree-capped fibre over every invariant target. The translation-fixed irreducible counts used in the formal orbit Euler product are due to Garefalakis and Reis, and the underlying finite orbit-fold mechanism is treated as prior background; the residual claims are the all-depth formal orbit Euler product and target-refined fibres. Finite checks over $\mathbb F_4,\mathbb F_8$, and $\mathbb F_9$ are falsification controls only. External release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: |
  All-Depth Enumeration and Terminal Fibres\
  for Translation--GCD Erosion over Finite Fields
```

## Markdown 正文

# Scope and setup

Let $q=p^a$ be a prime power and let $\mathcal M_q$ be the set of monic polynomials in $\mathbb F_q[x]$, including $1$. Write $$\sigma f(x)=f(x+1),\qquad
  T(f)=\gcd(f,\sigma f),\qquad Q=T^{p-1},$$ where every gcd is monic. Since $\sigma^p=1$, the acting subgroup is the prime-subfield copy of $\mathbb F_p$, not the full additive group of $\mathbb F_q$ when $a>1$. We use the stabilization depth $$\operatorname{depth}(f)=\min\{t\geq0:T^t(f)=Q(f)\}.$$ Thus fixed states have depth zero.

The invariant ring for this translation is $\mathbb F_q[x^p-x]$. Its monic elements have series $$\label{eq:invariant-series}
 I_{q,p}(z)=\sum_{h\in\mathcal M_q:\,\sigma h=h}z^{\deg h}
           =\frac{1}{1-qz^p},$$ because $h=g(x^p-x)$ uniquely, with $g$ monic. This characterization and the translation-fixed irreducible classification are established in the finite-field invariant literature, especially @Garefalakis2011 and @Reis2018; related group-action and invariant-function frameworks include [@Reimers2018; @GowMcGuire2022; @Schulz2023].

We state the precise enumerative input. Let $$\label{eq:Nd}
 N_d(q)=\frac1d\sum_{e\mid d}\mu(e)q^{d/e}$$ be the number of degree-$d$ monic irreducibles. Let $b_d$ count those fixed by $\sigma$. Then $b_d=0$ unless $d=pm$, and, if $m=p^v s$ with $(s,p)=1$, $$\label{eq:bd}
 b_{pm}=\frac{p-1}{pm}\sum_{e\mid s}\mu(s/e)q^{p^v e}.$$ This is exactly Reis's formula [@Reis2018 Theorem 2(c)], after changing divisor variables, and is *not* a contribution here. Consequently $$\label{eq:ad}
                  a_d=\frac{N_d(q)-b_d}{p}$$ is the number of length-$p$ translation orbits of degree-$d$ irreducibles. Equations [\[eq:Nd\]](#eq:Nd){reference-type="eqref" reference="eq:Nd"}--[\[eq:ad\]](#eq:ad){reference-type="eqref" reference="eq:ad"} are owned input to our formal orbit Euler product.

The elementary identity $$\label{eq:window}
 T^t(f)=\gcd_{0\leq j\leq t}\sigma^j f$$ follows by induction. It implies $T^{p-1}(f)$ is invariant and $\operatorname{depth}(f)\leq p-1$. These facts, the sharp clock, the fixed set, and old finite depth tables receive zero contribution credit.

[\[rem:p110\]]{#rem:p110 label="rem:p110"} An earlier internal note, P110, studies $J(x)=x\vee\sigma x$ on a cyclically acted lattice and obtains the consecutive orbit join, invariant endpoint, finite clock, and recurrent points. Equation [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"} is its order-dual meet mechanism in the divisibility lattice. We claim none of those generic semilattice conclusions. The contribution below begins only with the polynomial-specific exponent census: cyclic run avoidance over irreducible orbits and the resulting all-depth and target-fibre formulas.

Shifted gcds and shift classes also occur in symbolic summation and shiftless factorization [@GerhardEtAl2003]; those algorithmic interfaces, like standard transfer matrices, are background rather than novelty claims.

# Translation orbits and local depth

Translation acts on monic irreducibles in orbits of length $1$ or $p$. Fix a nonfixed orbit and choose an indexing $$P_0,P_1=\sigma P_0,\ldots,P_{p-1}=\sigma^{p-1}P_0,$$ with indices read modulo $p$. If $e_i$ is the exponent of $P_i$ in $f$, then, up to reversing the cyclic indexing, [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"} says that its exponent after $t$ steps is $$\label{eq:sliding-min}
              e_i^{(t)}=\min_{0\leq j\leq t}e_{i+j}.$$ At $t=p-1$ every coordinate equals $m=\min_i e_i$. Put $c_i=e_i-m$. Then $c_i\geq0$ and $\min_i c_i=0$.

For a cyclic vector $c=(c_0,\ldots,c_{p-1})$ with a zero, let $\lambda(c)$ denote the longest cyclic run of positive coordinates; set $\lambda(0,\ldots,0)=0$.

[\[lem:run\]]{#lem:run label="lem:run"} On a nonfixed irreducible orbit, the least $t$ for which the exponents in [\[eq:sliding-min\]](#eq:sliding-min){reference-type="eqref" reference="eq:sliding-min"} have all reached their terminal value $m$ is $\lambda(c)$.

After subtracting $m$, equation [\[eq:sliding-min\]](#eq:sliding-min){reference-type="eqref" reference="eq:sliding-min"} vanishes in every coordinate exactly when every cyclic interval of length $t+1$ contains a zero. This is equivalent to the absence of a positive cyclic run of length $t+1$, or to $\lambda(c)\leq t$. The least such $t$ is $\lambda(c)$, including the all-zero boundary.

Fixed irreducibles contribute only to the invariant core and have no local transient. Hence the global depth of $f$ is the maximum of $\lambda(c)$ over its nonfixed irreducible orbits, with the maximum of an empty family equal to zero.

# The all-depth formal orbit Euler product

For $0\leq t\leq p-1$, define the local residual series $$\label{eq:R-definition}
 R_{p,t}(y)=
 \sum_{\substack{c\in\mathbb N^p,\ \min_i c_i=0\\\lambda(c)\leq t}}
 y^{c_0+\cdots+c_{p-1}}.$$ It has a finite transfer description. Put $u=y/(1-y)$ and index rows and columns by $0,\ldots,t$. Let $M_t(u)$ be the $(t+1)\times(t+1)$ matrix whose only nonzero entries are $$\label{eq:M}
 (M_t)_{i,0}=1\quad(0\leq i\leq t),\qquad
 (M_t)_{i,i+1}=u\quad(0\leq i<t).$$

[\[lem:transfer\]]{#lem:transfer label="lem:transfer"} For $0\leq t\leq p-1$, $$\label{eq:R-trace}
                         R_{p,t}(y)=\operatorname{tr}\bigl(M_t(u)^p\bigr).$$

Read a cyclic support word of length $p$. State $i$ records the current positive run length. A zero sends every state to $0$ with weight $1$; a positive coordinate sends $i$ to $i+1$ with weight $u=y+y^2+\cdots$, provided $i<t$. A closed length-$p$ path is therefore a cyclic word with no positive run longer than $t$, together with an arbitrary positive height at every positive position.

Fix the cut at labelled coordinates $0,\ldots,p-1$. The state before $j$ is uniquely forced to be the preceding positive-run length. Starting after any zero merely computes that same cyclic assignment, so multiple zeros do not create paths. Thus each labelled vector gives one closed path: the trace neither quotients by rotations nor weights by zeros (and the all-zero vector has its unique all-zero path). Conversely every closed path recovers this labelled support and its heights. Summing closed paths is the trace in [\[eq:R-trace\]](#eq:R-trace){reference-type="eqref" reference="eq:R-trace"}, and their weights are exactly those in [\[eq:R-definition\]](#eq:R-definition){reference-type="eqref" reference="eq:R-definition"}.

Write $[z^n]F(z)$ for coefficient extraction in formal power series.

[\[thm:euler\]]{#thm:euler label="thm:euler"} For every prime power $q=p^a$ and $0\leq t\leq p-1$, the ordinary generating function for monic polynomials of depth at most $t$ is $$\label{eq:H}
 H_{q,p,t}(z)
 :=\sum_{f\in\mathcal M_q:\,\operatorname{depth}(f)\leq t}z^{\deg f}
 =\frac{1}{1-qz^p}
   \prod_{d\geq1}R_{p,t}(z^d)^{a_d},$$ where $a_d$ is the owned input in [\[eq:ad\]](#eq:ad){reference-type="eqref" reference="eq:ad"} and $R_{p,t}$ is given by [\[eq:R-trace\]](#eq:R-trace){reference-type="eqref" reference="eq:R-trace"}. This formal orbit Euler product is coefficientwise well defined.

Unique factorization partitions the irreducible factors of $f$ into fixed orbits and length-$p$ orbits. On each length-$p$ orbit, the exponent vector splits uniquely as $$(e_0,\ldots,e_{p-1})=m(1,\ldots,1)+c,
       \qquad \min_i c_i=0.$$ All common-minimum pieces, together with every fixed irreducible factor, form one arbitrary translation-invariant monic polynomial. Their series is $I_{q,p}(z)$ from [\[eq:invariant-series\]](#eq:invariant-series){reference-type="eqref" reference="eq:invariant-series"}. For each of the $a_d$ nonfixed degree-$d$ orbits, [\[lem:run\]](#lem:run){reference-type="ref" reference="lem:run"} says that depth at most $t$ is equivalent to $\lambda(c)\leq t$, and the residual degree is $d\sum_i c_i$. Its series is therefore $R_{p,t}(z^d)$.

The global depth is the maximum of the local depths, so these conditions hold independently on every orbit. Multiplication yields [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"}. For a fixed coefficient $z^n$, only irreducible degrees $d\leq n$ can contribute, proving formal well-definedness.

[\[cor:layers\]]{#cor:layers label="cor:layers"} Set $H_{q,p,-1}(z)=0$. For $0\leq t\leq p-1$, $$\#\{f\in\mathcal M_q:\deg f=n,\ \operatorname{depth}(f)=t\}
   =[z^n]\bigl(H_{q,p,t}(z)-H_{q,p,t-1}(z)\bigr).$$ Moreover, $$\label{eq:boundaries}
 R_{p,0}(y)=1,\quad H_{q,p,0}(z)=\frac1{1-qz^p},\qquad
 R_{p,p-1}(y)=\frac{1-y^p}{(1-y)^p},\quad
 H_{q,p,p-1}(z)=\frac1{1-qz}.$$

The difference isolates the two nested depth thresholds. At $t=0$, the only normalized vector is zero. At $t=p-1$, every nonnegative vector with minimum zero is allowed, so its series is the series of all vectors minus that of all-positive vectors: $$(1-y)^{-p}-\bigl(y/(1-y)\bigr)^p
   =(1-y^p)/(1-y)^p.$$ The first global identity in [\[eq:boundaries\]](#eq:boundaries){reference-type="eqref" reference="eq:boundaries"} is [\[eq:invariant-series\]](#eq:invariant-series){reference-type="eqref" reference="eq:invariant-series"}; the last follows either from [\[thm:euler\]](#thm:euler){reference-type="ref" reference="thm:euler"} and unique factorization or simply because every monic polynomial has depth at most $p-1$ and there are $q^n$ of degree $n$.

# Unit fibre and every invariant target

The endpoint $Q(f)$ divides $f$ and is invariant. Define the *unit fibre* $$\mathcal U_{q,p}=Q^{-1}(1)$$ and let $U_{q,p,n}$ count its degree-$n$ elements. The word "unit" refers only to the target $1$.

[\[prop:split\]]{#prop:split label="prop:split"} Multiplication gives a degree-preserving bijection $$\label{eq:split}
 \{h\in\mathcal M_q:\sigma h=h\}\times\mathcal U_{q,p}
       \longrightarrow \mathcal M_q,\qquad (h,r)\longmapsto hr.$$ Its inverse is $f\mapsto(Q(f),f/Q(f))$. This is a set-theoretic graded bijection, not a monoid quotient.

On every nonfixed irreducible orbit, $Q(f)$ has the common minimum exponent; on a fixed irreducible it has the full exponent. Hence $h=Q(f)$ is invariant, divides $f$, and the residual $r=f/h$ has minimum exponent zero on every nonfixed orbit and no fixed irreducible factor. Thus $Q(r)=1$. This proves existence and also forces both factors, proving uniqueness.

Equivalently, for invariant $h$ equation [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"} gives the restricted identity $$\label{eq:restricted}
                    Q(hr)=hQ(r).$$ This identity proves that every pair on the left of [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"} maps back to itself. It does not imply multiplicativity on arbitrary pairs.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} The unit-fibre generating function and coefficients are $$\begin{aligned}
 U_{q,p}(z)&:=\sum_{n\geq0}U_{q,p,n}z^n
       =\frac{1-qz^p}{1-qz},\label{eq:U}\\
 U_{q,p,n}&=
 \begin{cases}
 q^n,&0\leq n<p,\\
 q^n-q^{n-p+1},&n\geq p.
 \end{cases}\label{eq:Un}\end{aligned}$$ Let $h$ be any invariant monic polynomial of degree $m$. Then, for every $N\geq0$, $$\label{eq:exact-fibre}
 \#\{f\in\mathcal M_q:\deg f=N,\ Q(f)=h\}
 =\begin{cases}U_{q,p,N-m},&N\geq m,\\0,&N<m.\end{cases}$$ Writing $L=D-m$, the degree-capped fibre through $D$ is zero for $L<0$; for $L\geq0$ it equals $$\label{eq:capped}
 \sum_{n=0}^{L}U_{q,p,n}=
 \begin{cases}
 \dfrac{q^{L+1}-1}{q-1},&0\leq L<p,\\[6pt]
 \dfrac{q^{L+1}-1-q^{L-p+2}+q}{q-1},&L\geq p.
 \end{cases}$$ Thus fibres depend on the target only through its degree.

All monic polynomials have series $(1-qz)^{-1}$. Taking generating functions in the graded bijection [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"} and using [\[eq:invariant-series\]](#eq:invariant-series){reference-type="eqref" reference="eq:invariant-series"} gives $$\frac1{1-qz}=\frac1{1-qz^p}U_{q,p}(z),$$ which is [\[eq:U\]](#eq:U){reference-type="eqref" reference="eq:U"}; coefficient extraction gives [\[eq:Un\]](#eq:Un){reference-type="eqref" reference="eq:Un"}.

For a fixed invariant $h$, multiplication $r\mapsto hr$ maps the degree-$(N-m)$ part of $\mathcal U_{q,p}$ into the fibre over $h$ by [\[eq:restricted\]](#eq:restricted){reference-type="eqref" reference="eq:restricted"}. Conversely, [\[prop:split\]](#prop:split){reference-type="ref" reference="prop:split"} forces every element of that fibre to be $hr$ for a unique such $r$. This proves [\[eq:exact-fibre\]](#eq:exact-fibre){reference-type="eqref" reference="eq:exact-fibre"}. Summing [\[eq:Un\]](#eq:Un){reference-type="eqref" reference="eq:Un"} through $L$ gives [\[eq:capped\]](#eq:capped){reference-type="eqref" reference="eq:capped"}; the second case subtracts $q\sum_{j=0}^{L-p}q^j$ from $\sum_{j=0}^{L}q^j$.

[\[rem:not-kernel\]]{#rem:not-kernel label="rem:not-kernel"} The projection $Q$ is not a monoid homomorphism. In characteristic $p$, put $a=x$ and $b=(x^p-x)/x$. The two exponent supports each miss a member of the full translation orbit, so $Q(a)=Q(b)=1$, whereas $ab=x^p-x$ is invariant and $Q(ab)=x^p-x$. Hence $Q^{-1}(1)$ is a unit fibre, not an algebraic kernel. The proofs above use only orbit exponents and the restricted identity [\[eq:restricted\]](#eq:restricted){reference-type="eqref" reference="eq:restricted"}.

# Mechanical falsification and limitations

An independent verifier constructs $$\mathbb F_4=\mathbb F_2[u]/(u^2+u+1),\quad
 \mathbb F_8=\mathbb F_2[u]/(u^3+u+1),\quad
 \mathbb F_9=\mathbb F_3[u]/(u^2+1)$$ from explicit field tables. It implements literal Horner translation, Euclidean gcd, trial-division irreducibility, translation-orbit partitioning, direct residual-vector enumeration, target fibres, and formal orbit Euler product coefficients. Separately, for $p=2,3$ and every $t$, it constructs the truncated polynomial matrix $M_t(y/(1-y))$, takes the trace of its $p$th power, and matches weights through $9$ against direct vector enumeration. It checks degrees $6,4,4$ in the three fields: $17{,}523$ states and $180{,}453$ assertions. In particular, the $\mathbb F_9$ lane exercises the intermediate depths $0,1,2$. This finite enumeration is evidence against small counterexamples, never a proof of [\[thm:euler,thm:fibres\]](#thm:euler,thm:fibres){reference-type="ref" reference="thm:euler,thm:fibres"}.

The result is limited to the single order-$p$ translation generated by $1$. Characteristic zero has no such finite clock; simultaneous erosion by a larger additive subspace is a different map. We make no priority claim for the literal dynamics, [\[eq:window\]](#eq:window){reference-type="eqref" reference="eq:window"}, the invariant ring, the fixed irreducible formula, or the transfer method. The owner-subtracted residual is precisely the conjunction of [\[thm:euler\]](#thm:euler){reference-type="ref" reference="thm:euler"} with the target-refined [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"}. A bounded literature non-hit is not novelty clearance, and external posting or submission remains on hold pending specialist owner review and explicit authorization.

# Conclusion

After the known orbit fold and fixed-irreducible theory are removed, the transient census is controlled by one local statistic: the longest positive run in a normalized cyclic exponent vector. Its transfer series produces all depth thresholds at once, while the same normalization gives a uniform graded fibre above every invariant endpoint. These two formulas constitute the complete internal claim package; the older clock, fixed set, and owner formulas remain background.
