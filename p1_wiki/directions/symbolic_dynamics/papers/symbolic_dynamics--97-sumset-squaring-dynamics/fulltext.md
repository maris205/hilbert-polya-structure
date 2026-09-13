---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--97-sumset-squaring-dynamics"
canonical_tex: "symbolic_dynamics/papers/97-sumset-squaring-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/97-sumset-squaring-dynamics/main.pdf"
source_sha256: "660308034f3c08568e3aa86eba0e190f47676c7be45ae2eef9618e8da5dbb022"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sumset-Squaring Dynamics on Prime Cyclic Groups: Exact Absorption Layers and Finite Zeta Data

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/97-sumset-squaring-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/97-sumset-squaring-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/97-sumset-squaring-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/97-sumset-squaring-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/97-sumset-squaring-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $p$ be an odd prime and let $\Phi_p(A)=A+A$ on the nonempty subsets of the additive group $\mathbb F_p$. Although the phase space has $2^p-1$ points, additive growth collapses its recurrent dynamics to a small explicit core. We prove that every nonsingleton other than $\mathbb F_p$ is transient, while the nonzero singletons form cycles of common length $h=\operatorname{ord}_p(2)$. Consequently $$\#\operatorname{Fix}(\Phi_p^n)
   =2+(p-1)\mathbf 1_{h\mid n},
   \qquad
   \zeta_{\Phi_p}(z)
   =(1-z)^{-2}(1-z^h)^{-(p-1)/h}.$$ The associated Möbius census has only two fixed cycles and $(p-1)/h$ cycles of length $h$. On the layer of $m$-element subsets, $2\leq m\leq p$, the exact worst time to reach $\mathbb F_p$ is $$\left\lceil\log_2\frac{p-1}{m-1}\right\rceil;$$ arithmetic progressions attain the bound. The first deviation of the fixed sequence from $2$ occurs at time $h$ and has height $p+1$, recovering both $p$ and $h$. Deterministic power-set enumeration and a separately constructed iterated-sumset control verify the registered finite cases. Classical sumset growth, critical-pair rigidity, and iterated-sumset structure are treated as inputs rather than residual claims.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Sumset-Squaring Dynamics on Prime Cyclic Groups: Exact Absorption Layers and Finite Zeta Data'
```

## Markdown 正文

# Introduction

Set addition can itself be iterated as a finite dynamical system. Fix an odd prime $p$, write $\mathbb F_p$ additively, and let $$\mathcal X_p=2^{\mathbb F_p}\setminus\{\varnothing\},
 \qquad
 \Phi_p:\mathcal X_p\longrightarrow\mathcal X_p,
 \qquad
 \Phi_p(A)=A+A.$$ This is not the pointwise hyperspace lift of a self-map of $\mathbb F_p$: every output element uses a pair of input elements, and the same binary operation is applied again at the next time. The iterates are therefore sumsets with exponentially many summands.

The phase portrait separates into two regimes. Cauchy--Davenport growth forces every nonsingleton into the full group, whereas a singleton $\{a\}$ follows the multiplicative orbit $a,2a,4a,\ldots$. This separation simultaneously determines recurrence, fixed counts, temporal cycles, zeta data, and the exact transient depth on every cardinality layer.

The contribution is a closed finite-dynamics package for this particular self-map:

1.  We classify every recurrent point and cycle, then derive all fixed counts, the Artin--Mazur zeta function, and the least-period Möbius census.

2.  For each $2\leq m\leq p$, we prove the exact maximum absorption time among all $m$-element subsets. A concrete arithmetic progression reaches the Cauchy--Davenport lower envelope at every pre-absorption time.

3.  The first fixed-count anomaly recovers $p$ and $\operatorname{ord}_p(2)$. The endpoint $m=p$, the excluded singleton layer, the empty set convention, and the exceptional prime $p=2$ are recorded separately.

The central statement is given next. Its proof occupies [\[sec:growth,sec:periodic,sec:depth\]](#sec:growth,sec:periodic,sec:depth){reference-type="ref" reference="sec:growth,sec:periodic,sec:depth"}.

# Statement, notation, and owner boundary

For a nonempty set $A\subseteq\mathbb F_p$ and an integer $q\geq1$, write $$qA=\{a_1+\cdots+a_q:a_i\in A\}$$ for the $q$-fold sumset. This notation is deliberately different from the scalar image $\{qa:a\in A\}$. We use recurrence in the standard topological sense: every neighborhood of the state is revisited at arbitrarily large positive times. Because $\mathcal X_p$ is finite and discrete, a state is recurrent exactly when $\Phi_p^n(A)=A$ for some $n\geq1$, equivalently when it lies on a cycle of the functional graph.

For $\lvert A\rvert\geq2$, define the absorption time $$\tau_p(A)=\min\{t\geq0:\Phi_p^t(A)=\mathbb F_p\}.$$ For $2\leq m\leq p$, put $$T_p(m)=\max\{\tau_p(A):A\subseteq\mathbb F_p,\ \lvert A\rvert=m\}.$$ Finally, let $h=\operatorname{ord}_p(2)$, the multiplicative order of $2$ in $\mathbb F_p^\times$. Since $p$ is odd, $h$ is defined and $h\geq2$. Lagrange's theorem also gives $h\mid p-1$.

[\[thm:main\]]{#thm:main label="thm:main"} Let $p$ be an odd prime and $h=\operatorname{ord}_p(2)$.

1.  For every $t\geq0$ and nonempty $A\subseteq\mathbb F_p$, $$\label{eq:iterate}
       \Phi_p^t(A)=2^tA.$$

2.  The recurrent states are precisely $$\label{eq:recurrent-set}
       \{\mathbb F_p,\{0\}\}\cup\{\{a\}:a\in\mathbb F_p^\times\}.$$ The first two states are fixed, and the nonzero singletons split into $(p-1)/h$ cycles of length $h$.

3.  For every $n\geq1$, $$\label{eq:fixed-count}
       F_p(n):=\lvert \operatorname{Fix}(\Phi_p^n)\rvert
       =2+(p-1)\mathbf 1_{h\mid n}.$$ Consequently the Artin--Mazur zeta function is $$\label{eq:zeta}
       \zeta_{\Phi_p}^{\mathrm{AM}}(z)
       =(1-z)^{-2}(1-z^h)^{-(p-1)/h}.$$ This is an identity of formal power series.

4.  If $C_p(n)$ denotes the number of cycles of least temporal period $n$, then $$\label{eq:cycle-census}
       C_p(n)=\frac1n\sum_{d\mid n}\mu\!\left(\frac nd\right)F_p(d)
       =\begin{cases}
         2,&n=1,\\
         (p-1)/h,&n=h,\\
         0,&\text{otherwise}.
       \end{cases}$$

5.  On every nonsingleton cardinality layer, $$\label{eq:layer-depth}
       \boxed{\displaystyle
       T_p(m)=\left\lceil\log_2\frac{p-1}{m-1}\right\rceil,
       \qquad 2\leq m\leq p.}$$ Every affine arithmetic progression $a+r\{0,1,\ldots,m-1\}$ with $r\in\mathbb F_p^\times$ attains this value.

6.  The first $n\geq1$ for which $F_p(n)\ne2$ is $n=h$, and $F_p(h)=p+1$. Thus the fixed sequence recovers $$\label{eq:recovery}
       h=\min\{n\geq1:F_p(n)\ne2\},
       \qquad p=F_p(h)-1.$$

The growth input is the Cauchy--Davenport theorem [@Davenport1935; @TaoVu2006]: for nonempty $A,B\subseteq\mathbb F_p$, $$\label{eq:cd}
 \lvert A+B\rvert\geq\min\{p,\lvert A\rvert+\lvert B\rvert-1\}.$$ We use it as a cited theorem, not as a result of this manuscript. The critical equality cases also have an established owner. In the range $\lvert A\rvert,\lvert B\rvert\geq2$ and $$\lvert A+B\rvert=\lvert A\rvert+\lvert B\rvert-1\leq p-2,$$ Vosper's theorem says that $A$ and $B$ are arithmetic progressions with a common difference [@Vosper1956; @TaoVu2006]. We invoke only this safe range in [\[prop:vosper\]](#prop:vosper){reference-type="ref" reference="prop:vosper"}; no endpoint extension is implicit.

The notation $qA$, its growth, and inverse questions for iterated sumsets belong to additive combinatorics; modern structural work includes [@Grynkiewicz2020]. Artin--Mazur introduced the periodic-point zeta ledger used in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} [@ArtinMazur1965]. The residual package here is limited to assembling these inputs into the complete phase portrait of the specific self-map $A\mapsto A+A$, including its exact cardinality layers and recovery statement. A bounded search through 29 August 2026 did not locate this exact combined dynamics package. Search absence is not a priority or novelty proof, and external release remains on hold.

# Iterated growth and recurrence {#sec:growth}

[\[lem:growth\]]{#lem:growth label="lem:growth"} For every nonempty $A\subseteq\mathbb F_p$, every integer $q\geq1$, and every $t\geq0$, $$\begin{aligned}
 \Phi_p^t(A)&=2^tA,\label{eq:iterate-lemma}\\
 \lvert qA\rvert&\geq\min\{p,q(\lvert A\rvert-1)+1\}.\label{eq:q-growth}\end{aligned}$$

The identity at $t=0$ is the convention $1A=A$. If $\Phi_p^t(A)=2^tA$, then $$\Phi_p^{t+1}(A)=(2^tA)+(2^tA)=2^{t+1}A,$$ which proves [\[eq:iterate-lemma\]](#eq:iterate-lemma){reference-type="eqref" reference="eq:iterate-lemma"} by induction.

For [\[eq:q-growth\]](#eq:q-growth){reference-type="eqref" reference="eq:q-growth"}, the case $q=1$ is equality. Apply [\[eq:cd\]](#eq:cd){reference-type="eqref" reference="eq:cd"} to $qA$ and $A$. Unless the full group has already been reached, each added copy of $A$ increases the lower bound by $\lvert A\rvert-1$. Induction gives the displayed minimum.

[\[cor:strict\]]{#cor:strict label="cor:strict"} If $2\leq\lvert A\rvert<p$, then either $A+A=\mathbb F_p$ or $\lvert A+A\rvert>\lvert A\rvert$. Every such $A$ reaches $\mathbb F_p$ in finite time.

Equation [\[eq:cd\]](#eq:cd){reference-type="eqref" reference="eq:cd"} with $B=A$ gives $\lvert A+A\rvert\geq\min\{p,2\lvert A\rvert-1\}$. If the minimum is not $p$, then $2\lvert A\rvert-1>\lvert A\rvert$. Finite absorption follows directly from [\[eq:q-growth\]](#eq:q-growth){reference-type="eqref" reference="eq:q-growth"} with $q=2^t$.

We can now prove the recurrent part of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The full group is fixed. A proper nonsingleton cannot return to itself because its cardinality strictly increases until absorption. For a singleton, $$\label{eq:singleton}
 \Phi_p^t(\{a\})=\{2^ta\}.$$ The state $\{0\}$ is fixed. If $a\ne0$, the least return time in [\[eq:singleton\]](#eq:singleton){reference-type="eqref" reference="eq:singleton"} is the least $t\geq1$ with $2^t=1$ in $\mathbb F_p^\times$, namely $h$. All nonzero singletons therefore have period $h$, and they form $(p-1)/h$ cycles. This proves parts 1 and 2 of [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# Fixed data, zeta factors, and recovery {#sec:periodic}

The recurrent classification makes the entire temporal ledger finite.

A state fixed by $\Phi_p^n$ is recurrent. The two fixed states in [\[eq:recurrent-set\]](#eq:recurrent-set){reference-type="eqref" reference="eq:recurrent-set"} contribute $2$. Every nonzero singleton is fixed exactly when $h\mid n$, contributing another $p-1$ in that case. This proves [\[eq:fixed-count\]](#eq:fixed-count){reference-type="eqref" reference="eq:fixed-count"}.

For a finite map with $c_r$ cycles of length $r$, the fixed sequence obeys $$F_p(n)=\sum_{r\mid n}r c_r,$$ and hence $$\exp\!\left(\sum_{n\geq1}F_p(n)\frac{z^n}{n}\right)
 =\prod_{r\geq1}(1-z^r)^{-c_r}.$$ Here $c_1=2$, $c_h=(p-1)/h$, and all other $c_r$ vanish, giving [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. Möbius inversion of the same divisor sum gives the first expression in [\[eq:cycle-census\]](#eq:cycle-census){reference-type="eqref" reference="eq:cycle-census"}; substitution of [\[eq:fixed-count\]](#eq:fixed-count){reference-type="eqref" reference="eq:fixed-count"} gives its three cases.

Because $h\geq2$, the counts are $2$ through time $h-1$ and jump to $p+1$ at time $h$. Formula [\[eq:recovery\]](#eq:recovery){reference-type="eqref" reference="eq:recovery"} follows. Equivalently, the first nontrivial zeta factor has degree $h$ and exponent $(p-1)/h$; the fixed sequence formulation avoids any factorization convention.

The first registered examples are shown in [1](#tab:examples){reference-type="ref" reference="tab:examples"}. The last column is the deepest layer, namely the two-point layer.

::: {#tab:examples}
    $p$   $h=\operatorname{ord}_p(2)$   $F_p(1)$   $F_p(h)$   $T_p(2)$
  ----- ----------------------------- ---------- ---------- ----------
      3                             2          2          4          1
      5                             4          2          6          2
      7                             3          2          8          3
     11                            10          2         12          4
     13                            12          2         14          4

  : Early periodic and transient signals. The fixed count is constant at $2$ before time $h$ and equals $p+1$ at time $h$.
:::

# Exact cardinality-layer absorption {#sec:depth}

The lower envelope in [\[eq:q-growth\]](#eq:q-growth){reference-type="eqref" reference="eq:q-growth"} determines an upper bound for every orbit. Arithmetic progressions show that the bound cannot be improved on any layer.

Fix $2\leq m\leq p$ and set $$K=\left\lceil\log_2\frac{p-1}{m-1}\right\rceil.$$ For every $m$-element set $A$, [\[lem:growth\]](#lem:growth){reference-type="ref" reference="lem:growth"} gives $$\lvert \Phi_p^K(A)\rvert
 \geq\min\{p,2^K(m-1)+1\}=p.$$ Thus $\Phi_p^K(A)=\mathbb F_p$ and $T_p(m)\leq K$.

For sharpness, take an affine arithmetic progression $$A=a+r\{0,1,\ldots,m-1\},\qquad r\in\mathbb F_p^\times.$$ Every integer between $0$ and $q(m-1)$ is a sum of $q$ integers from $\{0,\ldots,m-1\}$. Hence $$\label{eq:ap-sumset}
 qA=qa+r\{0,1,\ldots,q(m-1)\}\pmod p.$$ If $0\leq t<K$, the definition of $K$ gives $2^t(m-1)<p-1$. The residues displayed in [\[eq:ap-sumset\]](#eq:ap-sumset){reference-type="eqref" reference="eq:ap-sumset"} are then distinct, so $$\lvert \Phi_p^t(A)\rvert=2^t(m-1)+1<p.$$ At $t=K$, we have $2^K(m-1)+1\geq p$, so the displayed integer interval contains at least $p$ consecutive integers. Their residues cover all of $\mathbb F_p$; any further wraparound does not change that conclusion. Thus $\tau_p(A)=K$, proving [\[eq:layer-depth\]](#eq:layer-depth){reference-type="eqref" reference="eq:layer-depth"}.

The progression construction proves existence of extremizers. It does not by itself classify every set of maximal absorption time. The following owner-subtracted statement records exactly the local rigidity that we use.

[\[prop:vosper\]]{#prop:vosper label="prop:vosper"} Let $A\subseteq\mathbb F_p$ satisfy $\lvert A\rvert\geq2$ and $$\label{eq:vosper-range}
 \lvert A+A\rvert=2\lvert A\rvert-1\leq p-2.$$ Then $A$ is an arithmetic progression modulo $p$.

Apply Vosper's theorem to the pair $(A,A)$. The hypotheses in [\[eq:vosper-range\]](#eq:vosper-range){reference-type="eqref" reference="eq:vosper-range"} are precisely the critical equality and endpoint restriction in the cited form of that theorem [@Vosper1956].

[\[rem:no-overclaim\]]{#rem:no-overclaim label="rem:no-overclaim"} An orbit can attain the maximal absorption time even when one intermediate Cauchy--Davenport inequality has slack, provided the slack does not fill the remaining distance to $p$. Accordingly, [\[prop:vosper\]](#prop:vosper){reference-type="ref" reference="prop:vosper"} is a classification of the sharp first doubling step in its valid range, not a claim that every maximizer in [\[eq:layer-depth\]](#eq:layer-depth){reference-type="eqref" reference="eq:layer-depth"} is an arithmetic progression.

# Exact controls, endpoints, and authority

The deterministic script `code/verify_sumset_squaring.py` registers two complementary exact finite routes. The first enumerates every nonempty subset for $p=3,5,7,11,13$, constructs its literal functional orbit, and checks the recurrent classification, every fixed count through time $2h$, and every cardinality-layer maximum. It examines 10,403 states in total.

The second route builds $2^tA$ by adding one copy of $A$ at a time rather than applying $\Phi_p$ recursively. It checks the iterate identity on 863 state--time cases, verifies 17,139 ordered Cauchy--Davenport pairs, tests the safe Vosper equality range, and checks arithmetic-progression extremizers for every layer of every odd prime through $43$. Möbius reconstruction independently verifies that only periods $1$ and $h$ survive, while the cycle-product factors reconstruct every registered logarithmic zeta coefficient. The final registered run contains 91,509 exact assertions and no floating-point or randomized test.

The endpoints are material.

-   The singleton layer is not an absorption layer: $\{0\}$ is fixed and the nonzero states have period $h$.

-   At $m=p$, the only state is already $\mathbb F_p$, and [\[eq:layer-depth\]](#eq:layer-depth){reference-type="eqref" reference="eq:layer-depth"} gives $T_p(p)=0$.

-   The empty set was excluded. If adjoined, it is one additional fixed state and multiplies [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} by $(1-z)^{-1}$.

-   At $p=2$, doubling is not a permutation on nonzero singletons: $\{1\}\mapsto\{0\}$. Direct enumeration gives only the two fixed recurrent states $\{0\}$ and $\mathbb F_2$ and no first anomaly. This is why [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} assumes an odd prime.

All infinite-family assertions are proved in the manuscript. Computation is a finite control, not evidence for untested primes. Cauchy--Davenport, Vosper critical-pair rigidity, general iterated-sumset structure, and the Artin--Mazur construction remain positively attributed to their owners. Public posting, submission, author contact, specialist priority claims, and absolute novelty language remain **HOLD**.
