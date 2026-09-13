---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-395-all-clock-rigidity-centered-three-window-mobius-capacity"
canonical_tex: "zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/main.pdf"
source_sha256: "8e3d65418d229bd5b990e2c528d2c3c8774b16ef3450d0a8a57f2be4291a30fe"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# All-Clock Rigidity for Centered Three-Window Möbius Capacity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-395-all-clock-rigidity-centered-three-window-mobius-capacity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We introduce a centered, deliberately noncausal local-table model for the distance-two Möbius capacity problem. At phase $r$, a sign table reads $\mu_0(n-1),\mu(n),\mu(n+1)$, and universal safety forbids two $+1$ outputs two steps apart for every ternary input word. The complete three-shift terminal-log table law reduces every fixed-clock limit to nonnegative exact-support densities.

  Positive projection turns the $2^{27}$ local tables into 512 relations. Relation saturation then gives an exact tropical trace on the eight subsets of $\{-1,0,+1\}$ for every clock. For $q\geq3$ a multi-affine argument reduces an optimizer to four antipodally symmetric states; the self-loop clock $q=2$ is a genuine exception and needs a one-sign state. Writing $K_j=\prod_p(1-j/p^2)$, we obtain $$C(1)=K_2-K_3,\quad C(2)=\frac{3K_2-K_3}{4},\quad
   C(3)=\frac{3K_1}{8},\quad C(4)=\frac{2K_1}{3},$$ and $C(6)=K_1/8+K_2/2$, strictly above the corresponding one-site value $3K_1/8$.

  Despite these finite-clock memory gains, the all-clock endpoint is rigid. A phasewise marginal identity on square-support clocks charges every adjacent pair by one common center weight, recovering exactly the one-site path-MWIS value. Divisibility lifting then proves $$\sup_{q<\infty}C(q)=B_\infty,\qquad C(q)<B_\infty
   \quad\text{for every finite }q.$$ The maximum is formed only after each fixed-table terminal limit. No growing clock, ordinary Cesàro, causal-transducer, adaptive-capacity, or higher even-correlation conclusion is asserted.
author:
- RH research program
date: 'August 11, 2026'
title: 'All-Clock Rigidity for Centered Three-Window Möbius Capacity'
```

## Markdown 正文

**Keywords:** Möbius function; terminal logarithmic average; centered local rule; max-plus optimization; squarefree density; nonattained supremum.

# Model, densities, and principal theorem

Write $\mu_0(t)=\mu(t)$ for integers $t\geq1$, and $\mu_0(t)=0$ for $t\leq0$. A *terminal clock* is any function $$1\leq\omega(X)\leq X,\qquad \omega(X)\longrightarrow\infty.
  \label{eq:clock}$$ Fix a positive integer $q$. A centered $q$-phase table family is $$F_r:\{-1,0,+1\}^3\longrightarrow\{-1,+1\},\qquad r\in\mathbb Z/q\mathbb Z.$$ Its output at $n$ reads one future coordinate: $$\varepsilon_n
 =F_{n\bmod q}\bigl(\mu_0(n-1),\mu(n),\mu(n+1)\bigr).
 \label{eq:output}$$ Thus centered is a new noncausal data type, not an online transducer. The family is *universally distance-two safe* when $$\neg\bigl(F_r(a,b,c)=+1\ \text{and}\
 F_{r+2}(c,d,e)=+1\bigr)
 \label{eq:safety}$$ for every $r$ and every $a,b,c,d,e\in\{-1,0,+1\}$. The shared letter $c$ is the only coupling between the two windows.

For fixed $q,F,\omega$, put $$L_{q,X}(F)=\frac1{\log\omega(X)}
 \sum_{X/\omega(X)<n\leq X}
 \frac{\mu(n)F_{n\bmod q}
  (\mu_0(n-1),\mu(n),\mu(n+1))}{n}.
 \label{eq:functional}$$ The complete three-shift law recalled below proves that the limit $L_q(F)=\lim_{X\to\infty}L_{q,X}(F)$ exists for every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}. Only after these fixed-table limits are formed do we set $$C(q)=\max_{\substack{F\text{ fixed and}\\\text{universally safe}}}
 |L_q(F)|.
 \label{eq:capacity}$$

Let $\mathcal I=\{L,C,R\}$ with shifts $$a_L=+1,\qquad a_C=0,\qquad a_R=-1,
 \label{eq:shifts}$$ so that $\mu_0(n-a_L),\mu_0(n-a_C),\mu_0(n-a_R)$ are the entries in [\[eq:output\]](#eq:output){reference-type="eqref" reference="eq:output"}. For $S\subseteq\mathcal I$, set $$B_{p,S}=\{a_i\bmod p^2:i\in S\},\qquad
 \nu_{p,S}=|B_{p,S}|,$$ where the set is deduplicated modulo $p^2$, and $$\tau_{p,S}(r)=
 \#\{b\in B_{p,S}:b\bmod p=r\bmod p\}.$$ The squarefree phase density is $$\Theta_{q,r}(S)=\frac1q
 \prod_{p\nmid q}\left(1-\frac{\nu_{p,S}}{p^2}\right)
 \prod_{p\parallel q}\left(1-\frac{\tau_{p,S}(r)}p\right)
 \prod_{p^2\mid q}\mathbf 1_{\{r\bmod p^2\notin B_{p,S}\}}.
 \label{eq:theta}$$ In particular $\Theta_{q,r}(\varnothing)=1/q$, and $$\sum_{r\bmod q}\Theta_{q,r}(S)=K_{|S|},\qquad
 K_j=\prod_p\left(1-\frac{j}{p^2}\right),\quad K_0=1.
 \label{eq:Kj}$$ The exact-support density is $$\Pi_{q,r}(U)=
 \sum_{W\subseteq\mathcal I\setminus U}
 (-1)^{|W|}\Theta_{q,r}(U\cup W).
 \label{eq:Pi}$$ It is nonnegative and $\sum_{U\subseteq\mathcal I}\Pi_{q,r}(U)=1/q$.

[\[thm:main\]]{#thm:main label="thm:main"} For every fixed $q$, every safe table family has the terminal limit [\[eq:functional\]](#eq:functional){reference-type="eqref" reference="eq:functional"} for every clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}. For $x,y\in\{-1,0,+1\}$, let $S(x,y)\subseteq\{L,C,R\}$ contain $C$, contain $L$ exactly when $x\ne0$, and contain $R$ exactly when $y\ne0$. Define $$\lambda_r(x,y)=
 2^{-\mathbf 1_{\{x\ne0\}}-\mathbf 1_{\{y\ne0\}}}
 \Pi_{q,r}\bigl(S(x,y)\bigr)
 \label{eq:lambda}$$ for $x,y\in\{-1,0,+1\}$, and, for $U,V\subseteq\{-1,0,+1\}$, $$\mathcal K_r(U,V)=
 \sum_{\substack{x\notin U\\y\in V}}\lambda_r(x,y).
 \label{eq:transition}$$ Then the exact all-$q$ capacity is $$\boxed{\displaystyle
 C(q)=\sum_{\gamma}
 \max_{\substack{Y_r\subseteq\{-1,0,+1\}\\r\in\gamma\text{ cyclic}}}
 \sum_{r\in\gamma}\mathcal K_r(Y_{r-2},Y_r),}
 \label{eq:eight-state}$$ where $\gamma$ runs over the $\gcd(q,2)$ cycles of $r\mapsto r+2$. Equivalently, each summand is the tropical trace of a cyclic product of exact $8\times8$ transition matrices.

For $q\geq3$, some optimizer in [\[eq:eight-state\]](#eq:eight-state){reference-type="eqref" reference="eq:eight-state"} uses only the four antipodally symmetric subsets. With $$u(Y)=\left(\mathbf 1_{\{0\in Y\}},
 \frac{|Y\cap\{-1,+1\}|}{2}\right)\in\{0,1\}^2$$ and $$(a_r,b_r,c_r,d_r)=
 \bigl(\Pi_{q,r}(\{C\}),\Pi_{q,r}(\{L,C\}),
 \Pi_{q,r}(\{C,R\}),\Pi_{q,r}(\{L,C,R\})\bigr),$$ the compressed transition is $$a_r(1-u_0)v_0+b_r(1-u_1)v_0+
 c_r(1-u_0)v_1+d_r(1-u_1)v_1.
 \label{eq:four-state}$$ This compression is not a proof for $q=1,2$; their self-loops retain all eight states. The first exact values are $$\begin{aligned}
 C(1)&=K_2-K_3,&
 C(2)&=\frac{3K_2-K_3}{4},\label{eq:C12}\\
 C(3)&=\frac{3K_1}{8}=\frac9{4\pi^2},&
 C(4)&=\frac{2K_1}{3}=\frac4{\pi^2},\label{eq:C34}\\
 C(6)&=\frac{K_1}{8}+\frac{K_2}{2}.&&
 \label{eq:C6}\end{aligned}$$ At $q=6$, this strictly exceeds the embedded one-site value $3K_1/8$.

Let $B_\infty$ be the RH-375 one-site square-clock endpoint, recalled in [\[eq:Binfinity\]](#eq:Binfinity){reference-type="eqref" reference="eq:Binfinity"} below. Then $$\boxed{\displaystyle\sup_{q<\infty}C(q)=B_\infty,\qquad
 C(q)<B_\infty\quad(q<\infty).}
 \label{eq:all-clock}$$ Both signs of every nonzero optimum are attained.

# The analytic reduction to nonnegative relations

RH-394, Theorem 1.1, equation (8), Theorem 1.2, equations (11)--(12), and Corollary 1.3 (printed/PDF pages 2--3) prove the complete fixed three-shift table law for every terminal clock [@RH394]. Applied to $$H_r(x,z,y)=zF_r(x,z,y),$$ that law says that the limit in [\[eq:functional\]](#eq:functional){reference-type="eqref" reference="eq:functional"} is the sum, over exact support strata $U$, of $\Pi_{q,r}(U)$ times the uniform sign average of $H_r$ on that stratum. Equations [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}--[\[eq:Pi\]](#eq:Pi){reference-type="eqref" reference="eq:Pi"} are its phase-resolved densities. Its proof inherits the odd-correlation input of Tao--Teräväinen and the two-point input of Tao [@TaoTeravainen2019; @Tao2016LogChowla]; we do not re-invoke those remote theorems with new quantifiers.

[\[lem:projection\]]{#lem:projection label="lem:projection"} From a safe family $F$, change every $+1$ output at a cell with center $z\ne+1$ to $-1$, leaving all other cells unchanged. The resulting family $F^+$ is safe and $$L_q(F^+)\geq L_q(F).$$ Put $$A_r=\{(x,y)\in\{-1,0,+1\}^2:F^+_r(x,+1,y)=+1\}.
 \label{eq:relation}$$ Then $$L_q(F^+)=\sum_{r\bmod q}\sum_{(x,y)\in A_r}\lambda_r(x,y).
 \label{eq:projected-limit}$$ Every one of the 512 relations occurs, with $2^{18}$ full sign-table preimages before projection.

If $z=-1$, changing the output from $+1$ to $-1$ changes the score $zF$ from $-1$ to $+1$; if $z=0$, the score is unchanged. Deleting $+1$ outputs cannot create a forbidden pair, proving the first claim pointwise before taking any limit.

The all-minus table contributes $H=-z$, whose sign average is zero on every stratum with nonzero center and which vanishes when the center is zero. Turning a center-$+1$ cell $(x,+1,y)$ from minus to plus changes the score by two. On its exact support stratum, the specified nonzero signs have density $2^{-|U|}\Pi_{q,r}(U)$. Multiplication by two leaves exactly [\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"}, proving [\[eq:projected-limit\]](#eq:projected-limit){reference-type="eqref" reference="eq:projected-limit"}. The nine center-$+1$ cells determine $A_r$, while the other 18 sign-table cells are free.

For a relation $A\subseteq\{-1,0,+1\}^2$, write $$\operatorname{Source}(A)=\{x:(x,y)\in A\text{ for some }y\},\qquad
 \operatorname{Target}(A)=\{y:(x,y)\in A\text{ for some }x\}.$$

[\[lem:saturation\]]{#lem:saturation label="lem:saturation"} The projected family is safe if and only if $$\operatorname{Target}(A_r)\cap\operatorname{Source}(A_{r+2})=\varnothing
 \quad(r\bmod q).
 \label{eq:relation-safety}$$ If $Y_r=\operatorname{Target}(A_r)$, replacing every relation by $$\widetilde A_r=(\{-1,0,+1\}\setminus Y_{r-2})\times Y_r
 \label{eq:saturated-relation}$$ preserves safety and weakly increases [\[eq:projected-limit\]](#eq:projected-limit){reference-type="eqref" reference="eq:projected-limit"}. Conversely, every subset profile $(Y_r)$ in [\[eq:saturated-relation\]](#eq:saturated-relation){reference-type="eqref" reference="eq:saturated-relation"} gives a safe relation family.

Two positive outputs at phases $r,r+2$ are composable precisely when the right coordinate of an edge in $A_r$ equals the left coordinate of an edge in $A_{r+2}$, which is [\[eq:relation-safety\]](#eq:relation-safety){reference-type="eqref" reference="eq:relation-safety"}. Hence every source of $A_r$ lies outside $Y_{r-2}$, while every target lies in $Y_r$. Thus $A_r\subseteq\widetilde A_r$. The weights $\lambda_r$ are nonnegative, so adding the missing edges cannot lower the score. Finally, any edge of $\widetilde A_r$ ends in $Y_r$, and any edge of $\widetilde A_{r+2}$ begins outside $Y_r$; therefore the saturated family is safe.

[\[lem:reflection\]]{#lem:reflection label="lem:reflection"} Define $F^\rho_r(x,z,y)=F_r(-x,-z,-y)$. Reflection preserves universal safety and $$L_q(F^\rho)=-L_q(F).$$ Consequently $\max_{\rm safe}|L_q|=\max_{\rm safe}L_q$, with both orientations attained.

Negation is a bijection of all ternary biwords, so it preserves [\[eq:safety\]](#eq:safety){reference-type="eqref" reference="eq:safety"}. For $H=zF$, $$zF^\rho(x,z,y)=-H(-x,-z,-y).$$ Every exact-support sign stratum is invariant under simultaneous negation, and its uniform average therefore changes sign. The RH-394 table law gives the displayed identity.

# The tropical optimizer and the self-loop exception

[\[prop:tropical\]]{#prop:tropical label="prop:tropical"} Formula [\[eq:eight-state\]](#eq:eight-state){reference-type="eqref" reference="eq:eight-state"} holds for every finite $q$, including the self-loop clocks $q=1,2$.

By Lemmas [\[lem:projection\]](#lem:projection){reference-type="ref" reference="lem:projection"}--[\[lem:saturation\]](#lem:saturation){reference-type="ref" reference="lem:saturation"}, a positive optimum is obtained by choosing $Y_r\subseteq\{-1,0,+1\}$, and its phase contribution is exactly $$\sum_{x\notin Y_{r-2}}\sum_{y\in Y_r}\lambda_r(x,y)
 =\mathcal K_r(Y_{r-2},Y_r).$$ Addition by two decomposes the phases into $\gcd(q,2)$ disjoint cycles. The choices on distinct cycles do not interact, so maximizing their sums separately proves [\[eq:eight-state\]](#eq:eight-state){reference-type="eqref" reference="eq:eight-state"}. Keeping all subsets of $\{-1,0,+1\}$ gives eight states, and cyclic closure is the tropical trace. Lemma [\[lem:reflection\]](#lem:reflection){reference-type="ref" reference="lem:reflection"} converts the positive optimum to the absolute capacity.

[\[prop:compression\]]{#prop:compression label="prop:compression"} If $q\geq3$, an optimizer can be chosen so that every $Y_r$ contains either both nonzero signs or neither. On these four states the transition is [\[eq:four-state\]](#eq:four-state){reference-type="eqref" reference="eq:four-state"}.

The density $\lambda_r(x,y)$ depends only on whether each coordinate is zero. Hold fixed the membership of zero in every $Y_r$, and put $k_r=|Y_r\cap\{-1,+1\}|\in\{0,1,2\}$. When $q\geq3$, the two occurrences of $Y_r$ are in distinct transition terms: it is the target of the $r$-term and the excluded source of the $r+2$-term. Holding all other variables fixed, the objective is affine in $k_r$. Replacing an interior value $k_r=1$ by one of the endpoints $0,2$ therefore does not lower the objective. Repeating this finitely many times yields an antipodally symmetric optimizer.

For such a set write $u_0=\mathbf 1_{\{0\in Y\}}$ and $u_1=k/2$. Splitting [\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"} according to the four zero/nonzero support patterns gives the four terms in [\[eq:four-state\]](#eq:four-state){reference-type="eqref" reference="eq:four-state"}. For $q=1,2$, the same variable occurs as both source and target in a self-loop and produces $k_r(2-k_r)$; the affine argument is therefore unavailable.

[\[prop:small\]]{#prop:small label="prop:small"} The values in [\[eq:C12\]](#eq:C12){reference-type="eqref" reference="eq:C12"}--[\[eq:C6\]](#eq:C6){reference-type="eqref" reference="eq:C6"} hold, and $$C(6)-F_{\rm one}(6)=\frac{2K_2-K_1}{4}>0,
 \qquad F_{\rm one}(6)=\frac{3K_1}{8}.
 \label{eq:q6-gap}$$

For $q=1,2$, substitute [\[eq:theta\]](#eq:theta){reference-type="eqref" reference="eq:theta"}--[\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"} into $\mathcal K_r(Y,Y)$ and check the eight subsets. At $q=1$, the zero-only state is optimal and gives $K_2-K_3$. At $q=2$, the even phase is optimized by a one-sign state, contributing $(K_2-K_3)/4$, while the odd phase is optimized by the zero-only state, contributing $K_2/2$. Hence $$C(2)=\frac{K_2-K_3}{4}+\frac{K_2}{2}
 =\frac{3K_2-K_3}{4}.$$ The antipodally symmetric four-state restriction would instead give $K_2-K_3$, so the $q=2$ exception is strict.

For $q=3,4,6$, Proposition [\[prop:compression\]](#prop:compression){reference-type="ref" reference="prop:compression"} reduces the exact calculation to the following four-state max-plus products. Each row lists the resulting coefficient vector in the basis $(K_1,K_2,K_3)$:

   $q$   coefficient vector  value
  ----- -------------------- ---------------
    3       $(3/8,0,0)$      $3K_1/8$
    4       $(2/3,0,0)$      $2K_1/3$
    6      $(1/8,1/2,0)$     $K_1/8+K_2/2$

These are finite products of four-by-four matrices with entries [\[eq:four-state\]](#eq:four-state){reference-type="eqref" reference="eq:four-state"}; comparing the four possible successor states at each step gives the displayed maxima. The full eight-state calculation agrees for $q\geq3$. Explicit maximizing profiles, listed in $+2$ cycle order, are $$\begin{array}{c|c}
q&\text{selector states}\\ \hline
3&(Y_0,Y_2,Y_1)=(\varnothing,\{-1,0,+1\},\varnothing),\\
4&(Y_0,Y_2)=(\varnothing,\{-1,0,+1\}),\quad
  (Y_1,Y_3)=(\{-1,0,+1\},\varnothing),\\
6&(Y_0,Y_2,Y_4)=(\varnothing,\{-1,0,+1\},\varnothing),\quad
  Y_1=Y_3=Y_5=\{0\}.
\end{array}$$ Substitution into [\[eq:four-state\]](#eq:four-state){reference-type="eqref" reference="eq:four-state"} gives the table entries. The other successor states are dominated using only the comparisons below, so no numerical approximation enters the finite maximum.

For completeness, the only Euler-product comparisons needed to order the finite candidates are $$\frac13<\frac{K_3}{K_2}<\frac12,\qquad
 \frac{K_2}{K_1}>\frac12.
 \label{eq:ratios}$$ The upper bound in the first inequality follows from the $p=2$ factor $$\frac{K_3}{K_2}
 =\frac12\prod_{p\geq3}\left(1-\frac1{p^2-2}\right).$$ For the lower bound, use $\prod(1-x_i)\geq1-\sum x_i$ and $$\sum_{p\geq3}\frac1{p^2-2}
 <\sum_{\substack{n\geq3\\n\ {\rm odd}}}\frac1{n(n-1)}
 =1-\log2<\frac13.$$ Likewise $$\frac{K_2}{K_1}
 =\frac23\prod_{p\geq3}\left(1-\frac1{p^2-1}\right)
 >\frac23\left(1-\sum_{\substack{n\geq3\\n\ {\rm odd}}}
 \frac1{n^2-1}\right)=\frac12,$$ where the prime sum is a strict sub-sum and the odd-integer sum is $1/4$. This last inequality proves [\[eq:q6-gap\]](#eq:q6-gap){reference-type="eqref" reference="eq:q6-gap"}. The one-site value follows from the phase-MWIS formula recalled next.
