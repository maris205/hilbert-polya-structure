---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--20-recurrent-verifier-clock-dilution"
canonical_tex: "symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution/main.tex"
canonical_pdf: "symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution/main.pdf"
source_sha256: "f7e735a2e3448f0458f6cf2d260f2f7d85ec7ec8a14d01b554dadfd4058a4706"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Recurrent Verifier Cycles and Clock Dilution: An Operator Obstruction for Arithmetic Countable Markov Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/20-recurrent-verifier-clock-dilution/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Finite full shifts encode the positive-integer semiring through alphabet product, alphabet-sum, and entropy. We close an explicit quotient-search trial-division verifier into a one-sided countable Markov shift: for every prime $p$ the complete computation is one simple recurrent cycle, while every composite trace enters a one-way cemetery. Under the contracted terminal convention the prime cycle has exact graph length $$\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\left\lceil\frac pd\right\rceil
  =\frac12p\log p+(\gamma-1)p+O(\sqrt p).$$ Assigning the source-intrinsic total roof $h(F_p)=\log p$ gives every prime orbit weight $p^{-s}$. This achieves an exact primitive/repetition ledger, but it creates a distribution-free obstruction on the natural vertex space. For every nonnegative allocation of that total clock and every $\operatorname{Re}s>0$, some edge weight on each prime block tends to one. The source-weighted vertex adjacency therefore has essential norm one, is noncompact, belongs to no finite Schatten class, and has the unit circle in its essential approximate spectrum. Its ordinary whole-space Fredholm determinant does not exist. The normally convergent combinatorial product $\prod_p(1-z^{\ell(p)}p^{-s})$ remains valid for $\operatorname{Re}s>1$, and at $z=1$ equals $1/\zeta(s)$; it is not that missing determinant. First return to the input states gives the trace-class diagonal operator $R_s e_p=p^{-s}e_p$, but contracts the verifier and changes the graph-step marker from $z^{\ell(p)}$ to $z$. A padded total-decider theorem reproduces the same failure for arbitrary decidable supports. Thus recurrence repairs the orbit inventory but not the same-object operator gate: the construction is selector-tautological, Route A is rejected, and no statement about Riemann zeros follows.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Recurrent Verifier Cycles and Clock Dilution:\
  An Operator Obstruction for Arithmetic Countable Markov Shifts
```

## Markdown 正文

# Introduction {#sec:introduction}

An arithmetic symbolic model should make its arithmetic visible in recurrent dynamics. Attaching one loop of weight $p^{-s}$ after a terminating prime test gives the correct Euler factor, but periodic orbits remember only the answer, not the computation that produced it. The natural repair is to close the entire verification path. Then every divisor trial and every exposed quotient-search state belongs to the primitive orbit itself.

This paper carries out that repair and finds a different obstruction. The source is the elementary semiring of finite full shifts. If $F_n$ denotes the full shift on $n$ symbols, alphabet product and alphabet-sum realize $mn$ and $m+n$, while topological entropy gives $h(F_n)=\log n$. Trial division can therefore be expanded into local successor, multiplication, and comparison transitions without a factor-existence oracle. Successful traces are sent directly back to their input states; unsuccessful traces enter one-way cemetery rays. The accepted primitive cycles are exactly the primes, with multiplicity one.

The positive orbit statement is exact. For $m=\lfloor\sqrt p\rfloor$, a prime input visits every quotient candidate $2\le q\le\lfloor p/d\rfloor+1$ for each $2\le d\le m$. With the terminal accept state contracted, the cycle length is $$\ell(p)=2+\sum_{d=2}^{m}\left\lceil\frac pd\right\rceil
       \sim\frac12p\log p.
\label{eq:intro-length}$$ Giving the cycle exact total roof $\log p$ makes one traversal weigh $p^{-s}$ and its $r$-fold temporal repetition weigh $p^{-rs}$. The corresponding finite block factor is $$1-z^{\ell(p)}p^{-s}.
\label{eq:intro-factor}$$

The same length that certifies the computation blocks the requested whole-space determinant. Let $\tau(e)\ge0$ be any edge allocation with $\sum_{e\in\Gamma_p}\tau(e)=\log p$. At least one of the $\ell(p)$ edges has $$\tau(e)\le\frac{\log p}{\ell(p)}\longrightarrow0.$$ On the natural counting space $\ell^2(V)$, the associated edge image has norm at least $p^{-\sigma/\ell(p)}\to1$, where $\sigma=\operatorname{Re}s>0$. Different prime cycles give orthogonal witnesses. The source-weighted vertex adjacency is therefore noncompact for every exact-clock allocation. In fact it has essential norm one, lies in no finite Schatten class, and has the unit circle in its essential approximate spectrum.

This conclusion is deliberately same-object. Countable symbolic systems admit local zeta functions, formal orbit products, induced maps, and transfer operators on other function spaces. We do not deny any of them. We freeze one graph, one edge-clock rule, the counting vertex Hilbert space, and the ordinary Hilbert-space Fredholm determinant. On that object the determinant is unavailable because the operator is not even compact.

Two weaker Euler ledgers survive. First, the normally convergent raw orbit product $$D^{\mathrm{raw}}_{\mathrm{orb}}(s,z)
=\prod_p(1-z^{\ell(p)}p^{-s})$$ exists for $\operatorname{Re}s>1$ and $|z|\le1$; at $z=1$ it is $1/\zeta(s)$. It must not be relabeled as the Fredholm determinant of the whole adjacency. Second, first return to the input states gives $R_s e_p=p^{-s}e_p$, whose ordinary Fredholm determinant is the Euler product. That induced operator is unitarily the diagonal prime-loop model. Its marker $z$ counts returns, whereas [\[eq:intro-factor\]](#eq:intro-factor){reference-type="eqref" reference="eq:intro-factor"} counts original graph steps. The two descriptions meet at $z=1$ only, unless the composite marker $z^{\ell(p)}$ is explicitly transported.

Our contributions are the following.

1.  We define an explicit one-sided countable Markov graph whose prime primitive orbit contains the complete semiring quotient search, with no prime table or factor-existence transition.

2.  We prove the exact contracted cycle formula [\[eq:intro-length\]](#eq:intro-length){reference-type="eqref" reference="eq:intro-length"}, elementary bounds, and its sharp first-order asymptotic.

3.  We derive the spectrum, singular values, powers, and graph-step determinant of an arbitrarily weighted finite cycle.

4.  We prove allocation-independent noncompactness, essential norm one, absence from every finite Schatten class, and the essential approximate unit circle for the full accepted restriction.

5.  We separate the raw periodic-orbit product from the nonexistent whole-vertex Fredholm determinant, and prove the first-return marker firewall.

6.  We give an exact compactness criterion for disjoint cycles with prescribed total clocks, then use padded total deciders and state subdivision to show that the mechanism is not prime-selective.

7.  We report a deterministic source/no-oracle and finite exact certificate without using target-zero data or finite numerics as proofs of infinite claims.

The result is a negative advance rather than a Riemann-hypothesis claim. It identifies a concrete incompatibility that any next Symbolic Dynamics candidate must evade: the arithmetic period and the operator clock cannot be chosen independently once a long verification computation is itself made recurrent.

# Classical boundary and novelty scope {#sec:boundary}

Periodic-orbit products and matrix determinants are classical for finite-state shifts [@BowenLanford1970]. A simple cycle of graph length $\ell$ contributes the discrete-time marker $z^\ell$; this convention is essential here because the verifier length diverges. Infinite weighted graphs can also support determinant and zeta formulas under appropriate summability hypotheses [@Deitmar2015]. Our claim is not a new abstract cycle-determinant identity. It is a scoped obstruction for one explicitly defined arithmetic graph and its natural counting-space adjacency.

Countable Markov shifts have a mature thermodynamic formalism, including recurrence classifications, pressure, local zeta functions, and first-return generating functions [@GurevichSavchenko1998; @Sarig1999]. Loop shifts organize periodic data through first-return words [@BoyleBuzziGomez2006]. These theories prevent a broad claim that a noncompact vertex adjacency eliminates all meaningful zeta data. In this paper $L_s$ is a source-weighted vertex adjacency on $\ell^2(V)$, not a Ruelle--Perron--Frobenius operator on a thermodynamic function space. The negative theorem applies to the ordinary Hilbert-space Fredholm determinant of that frozen object.

Suspension flows over countable Markov shifts likewise require their own roof and recurrence hypotheses [@BarreiraIommi2006]. In particular, roofs need not always be bounded away from zero [@IommiJordanTodd2015]. We therefore do not argue that the clocks $\tau(e)\to0$ make a suspension meaningless. Our conclusion is narrower: their exponential edge weights prevent compactness of a specified vertex operator. The representative roof can be chosen strictly positive even though its infimum is zero.

The first-return and subdivision interpretation also has classical antecedents. State expansion is central to flow equivalence [@ParrySullivan1975]; it need not preserve a discrete-time zeta function with an unchanged graph-step variable. Closing an exposed computation can therefore be regarded as a long state expansion of a single return. We use this as a warning, not as a novelty claim. The new application is that the arithmetic clock $\log p$ and the explicitly counted verifier subdivision together determine the operator-theoretic failure.

Embedding computation in symbolic dynamics is also established [@Kurka1997; @DelvenneKurkaBlondel2006]. Consequently, neither "a shift can simulate trial division" nor "a total decider can be made dynamical" is claimed as new. The relevant conjunction is an explicit full-shift semiring verifier, its exact quotient-state cycle length, an exact Euler total clock, and the resulting allocation-independent noncompactness plus return collapse.

Weighted shifts on directed graphs provide the natural operator setting [@JablonskiJungStochel2012]. The minimum-roof proof below is elementary; we do not claim a new general compactness criterion for weighted shifts. For ordinary Hilbert-space determinants we use the classical trace-class boundary [@Grothendieck1956; @Simon1977]. A raw orbit product may exist without satisfying that operator hypothesis, and a determinant on another space or after induction is a different construction.

The defensible novelty statement is therefore precise:

> For the contracted expanded quotient-search compiler, exact arithmetic clock $\log p$ and graph-step recurrence are incompatible with compactness of the natural counting-space weighted vertex adjacency; inducing restores a trace-class Euler determinant only after contracting the computation.

The literature audit found no primary-source collision with that complete claim bundle through August 14, 2026. This is an absence-of-discovery claim, not proof of global priority. Overlapping recurrent grammars, signed or matrix-valued cancellations, anisotropic spaces, regularized determinants, and geometric carriers remain outside the result.

# The recurrent semiring verifier {#sec:verifier}

## Finite-full-shift source

Let $A_n$ be an $n$-element alphabet and let $F_n=A_n^{\mathbb Z}$ be the two-sided full shift, considered up to topological conjugacy. Define $$F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn},
\qquad
F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n}.$$ We call $\boxplus$ the *alphabet-sum*. It is not asserted to be a categorical coproduct of subshifts: the full shift on a disjoint alphabet allows temporal mixing between the summands. The frozen structural rules are $$h(F_n)=\log n,
\qquad
S(F_d)=F_d\boxplus F_1=F_{d+1},
\qquad
F_d\boxtimes F_q\cong F_{dq}.$$ Equality and order are comparisons of the represented finite alphabet cardinalities. These are the only arithmetic instructions used below.

## Expanded quotient-search graph

For every input $n\ge2$, introduce reachable states $$I_n,\qquad T_{n,d},\qquad Q_{n,d,q},\qquad R_{n,k}.$$ The first is the input; $T_{n,d}$ tests the next divisor; $Q_{n,d,q}$ exposes successive cofactor candidates; and $R_{n,k}$ belongs to a one-way cemetery ray. The directed edges are $$I_n\longrightarrow T_{n,2},
\label{eq:input-edge}$$ $$T_{n,d}\longrightarrow
\begin{cases}
I_n,&d^2>n,\\
Q_{n,d,2},&d^2\le n,
\end{cases}
\label{eq:trial-edge}$$ and $$Q_{n,d,q}\longrightarrow
\begin{cases}
Q_{n,d,q+1},&dq<n,\\
R_{n,1},&dq=n,\\
T_{n,d+1},&dq>n.
\end{cases}
\label{eq:quotient-edge}$$ Finally $R_{n,k}\to R_{n,k+1}$. Distinct inputs use disjoint copies of all states. The successful transition in [\[eq:trial-edge\]](#eq:trial-edge){reference-type="eqref" reference="eq:trial-edge"} returns directly to $I_n$: there is no separate accept vertex. This contracted convention fixes every endpoint count in the sequel.

The equality edge in [\[eq:quotient-edge\]](#eq:quotient-edge){reference-type="eqref" reference="eq:quotient-edge"} is not a divisibility oracle. For fixed $d$, the graph constructs $q=2,3,\ldots$ by successor until the product $F_d\boxtimes F_q$ equals or exceeds $F_n$. A composite input reaches equality at its least divisor $d\le\sqrt n$ and then enters an acyclic ray. A prime input overshoots for every $2\le d\le\lfloor\sqrt p\rfloor$ and returns to its input after the square test.

[\[prop:recurrent-census\]]{#prop:recurrent-census label="prop:recurrent-census"} The graph component reachable from $I_n$ contains a closed walk if and only if $n$ is prime. In that case the reachable recurrent component is one simple directed cycle $\Gamma_n$ containing the entire successful verification path. Composite components are acyclic.

Determinism gives a unique forward path. If $n$ is composite, its least factor is at most $\sqrt n$, so an equality branch enters a one-way ray and never returns. If $n=p$ is prime, no tested product equals $p$; every quotient search overshoots, the divisor increments, and the first state with $d^2>p$ returns to $I_p$. No state repeats before that return because either $d$ or $q$ strictly increases. Thus the closed path is simple. Disjoint input copies exclude mixed cycles.

Let $G^{\circlearrowleft}$ denote this recurrently closed graph and let $X^+_{G^{\circlearrowleft}}$ be its one-sided edge shift. The graph is the symbolic phase-space presentation; the operator studied below acts on the separate vertex counting space.

## Exact clock class and natural operator

For each prime component choose finite nonnegative clocks $\tau(e)$ with $$\sum_{e\in\Gamma_p}\tau(e)=h(F_p)=\log p.
\label{eq:exact-clock}$$ Only the total is source-visible. Its distribution over expanded machine states is a modeling choice. The uniform representative $\tau(e)=\log p/\ell(p)$ is strictly positive; the operator theorem permits zero clocks as well. Composite computation and cemetery edges may retain the summable source roofs of the previous transient model, but those edges do not affect any accepted-block obstruction.

Set $\mathcal{H}=\ell^2(V)$ with its standard vertex basis. For $s\in\mathbb{C}$, $\sigma=\operatorname{Re}s>0$, define the source-weighted vertex adjacency $$L_s\delta_u=e^{-s\tau(u\to v)}\delta_v
\label{eq:vertex-adjacency}$$ on every functional edge $u\to v$, first on finitely supported vectors and then by bounded extension under the frozen roof choice. On the accepted subspace it is an orthogonal direct sum of finite weighted cyclic permutations. We do not call $L_s$ a Ruelle transfer operator.

The requested determinant is the ordinary Hilbert-space Fredholm determinant $\det_{\mathcal{H}}(I-zL_s)$, admitted when $L_s\in\mathcal{S}_1$. This same-object lock prevents a formal orbit product or an induced operator from silently replacing the whole vertex adjacency.

# Exact prime-cycle census {#sec:census}

The quotient states make the recurrent computation much longer than a trial-state count. The exact length is the bridge from arithmetic execution to operator compactness.

[\[thm:length\]]{#thm:length label="thm:length"} Let $p$ be prime and $m=\lfloor\sqrt p\rfloor$. The simple cycle $\Gamma_p$ in [\[prop:recurrent-census\]](#prop:recurrent-census){reference-type="ref" reference="prop:recurrent-census"} has graph length $$\boxed{
\ell(p)=2+\sum_{d=2}^{m}\left\lceil\frac pd\right\rceil
=2+\sum_{d=2}^{m}\left(1+\left\lfloor\frac pd\right\rfloor\right).}
\label{eq:exact-length}$$ In particular, $\ell(5)=5$ and $\ell(4093)=15293$.

Fix $2\le d\le m$. Because $p$ is prime, the branch begins with $T_{p,d}\to Q_{p,d,2}$ and then visits the quotient values $$2,3,\ldots,\left\lfloor\frac pd\right\rfloor+1.$$ At the last value $dq>p$, so the edge goes to $T_{p,d+1}$. From $T_{p,d}$ through this last quotient state to $T_{p,d+1}$ there are $$1+\left\lfloor\frac pd\right\rfloor
=\left\lceil\frac pd\right\rceil$$ edges; the equality uses $d\nmid p$. Summing these contributions and adding $I_p\to T_{p,2}$ plus the contracted terminal return $T_{p,m+1}\to I_p$ gives [\[eq:exact-length\]](#eq:exact-length){reference-type="eqref" reference="eq:exact-length"}. Direct substitution gives the two stated values.

[\[cor:length-asymptotic\]]{#cor:length-asymptotic label="cor:length-asymptotic"} With $H_m=\sum_{d=1}^m d^{-1}$, $$p(H_m-1)+2\le\ell(p)\le p(H_m-1)+m+1.
\label{eq:length-bounds}$$ The lower inequality is strict for $p\ge5$. Moreover, $$\ell(p)=\frac12p\log p+(\gamma-1)p+O(\sqrt p),
\qquad
\frac{\ell(p)}{p\log p}\longrightarrow\frac12.
\label{eq:length-asymptotic}$$

For each tested divisor, $$\frac pd\le\left\lceil\frac pd\right\rceil
<\frac pd+1.$$ There are $m-1$ terms, yielding [\[eq:length-bounds\]](#eq:length-bounds){reference-type="eqref" reference="eq:length-bounds"}; the upper strict bound can be weakened to the displayed integer-friendly inequality. For a prime and $2\le d\le m$, $p/d$ is not integral, so the lower inequality is strict whenever this range is nonempty, namely $p\ge5$.

Now $m=\sqrt p+O(1)$ and $H_m=\log m+\gamma+O(m^{-1})$. Hence $$p(H_m-1)
=\frac12p\log p+(\gamma-1)p+O(\sqrt p),$$ while the gap in [\[eq:length-bounds\]](#eq:length-bounds){reference-type="eqref" reference="eq:length-bounds"} is $O(\sqrt p)$. This proves [\[eq:length-asymptotic\]](#eq:length-asymptotic){reference-type="eqref" reference="eq:length-asymptotic"}.

The key quotient is therefore $$\frac{\log p}{\ell(p)}\sim\frac2p\longrightarrow0.
\label{eq:mean-clock}$$ It is the average edge clock forced by the arithmetic total. No roof allocation can make its minimum exceed its average, so [\[eq:mean-clock\]](#eq:mean-clock){reference-type="eqref" reference="eq:mean-clock"} is already a warning that the expanded computation and a compact weighted adjacency may be incompatible.

# Weighted-cycle algebra {#sec:cycle-algebra}

We first isolate the finite calculation that controls every accepted block. It is independent of how the total roof is distributed.

[\[lem:cycle-block\]]{#lem:cycle-block label="lem:cycle-block"} Let $C_\ell$ be a simple directed cycle with vertices $v_0,\ldots,v_{\ell-1}$ and clocks $\tau_0,\ldots,\tau_{\ell-1}\ge0$. Set $T=\sum_{j=0}^{\ell-1}\tau_j$ and define $$B_s\delta_{v_j}=e^{-s\tau_j}\delta_{v_{j+1\bmod\ell}}.$$ Then $$\begin{aligned}
B_s^\ell&=e^{-sT}I,                                      \label{eq:block-power}\\
\operatorname{spec}(B_s)&=\{e^{-sT/\ell}\omega:\omega^\ell=1\},       \label{eq:block-spectrum}\\
\{\text{singular values of }B_s\}
 &=\{e^{-\sigma\tau_j}:0\le j<\ell\},                   \label{eq:block-singular}\\
\det(I-zB_s)&=1-z^\ell e^{-sT}.                           \label{eq:block-det}\end{aligned}$$ Here any fixed choice of the $\ell$th root in [\[eq:block-spectrum\]](#eq:block-spectrum){reference-type="eqref" reference="eq:block-spectrum"} yields the same set.

One complete traversal multiplies every basis vector by the product of the edge weights, proving [\[eq:block-power\]](#eq:block-power){reference-type="eqref" reference="eq:block-power"}. Its roots give [\[eq:block-spectrum\]](#eq:block-spectrum){reference-type="eqref" reference="eq:block-spectrum"}. Since $B_s^*B_s$ is diagonal with entries $e^{-2\sigma\tau_j}$, [\[eq:block-singular\]](#eq:block-singular){reference-type="eqref" reference="eq:block-singular"} follows. Finally the only nonconstant term in the permutation expansion of $\det(I-zB_s)$ selects the whole cyclic permutation, giving [\[eq:block-det\]](#eq:block-det){reference-type="eqref" reference="eq:block-det"}. Equivalently, multiply $1-z\lambda$ over the spectrum in [\[eq:block-spectrum\]](#eq:block-spectrum){reference-type="eqref" reference="eq:block-spectrum"}.

For a prime block, $T=\log p$ and $\ell=\ell(p)$, so $$B_{p,s}^{\ell(p)}=p^{-s}I,
\qquad
\det(I-zB_{p,s})=1-z^{\ell(p)}p^{-s}.
\label{eq:prime-block}$$ The eigenvalue radius is $$r_p(s)=p^{-\sigma/\ell(p)}\longrightarrow1.
\label{eq:block-radius}$$ This spectral radius depends only on the total clock, not on its allocation. By contrast, the singular values record every individual edge clock.

The graph-step power trace also retains the subdivision. For $r\ge1$, $$\operatorname{Tr}(B_{p,s}^{r})=
\begin{cases}
\ell(p)p^{-sk},&r=k\ell(p),\\
0,&\ell(p)\nmid r.
\end{cases}
\label{eq:block-traces}$$ Thus the usual return-time weight $p^{-s}$ does not imply a nonzero length-one graph trace. This distinction will prevent the first-return map from being mistaken for the original discrete-time operator.

For fixed total $T$, $$\max_j e^{-\sigma\tau_j}
=e^{-\sigma\min_j\tau_j}
\ge e^{-\sigma T/\ell}.$$ Equality holds for the uniform allocation. Consequently the representative roof used in the certificate is the most favorable possible allocation for compactness; an adversarial concentration of the clock only increases the largest edge weight.

# Clock dilution and the whole-operator obstruction {#sec:dilution}

Let $\mathcal{H}_{\mathrm{acc}}$ be the closed span of vertices on the prime cycles. It is a reducing subspace, and $$L_s\big|_{\mathcal{H}_{\mathrm{acc}}}=\bigoplus_p B_{p,s}.$$ The next theorem uses only disjointness, nonnegative clocks, the exact total, and $\log p/\ell(p)\to0$. It is therefore independent of all modeling choices about how the source clock is distributed.

[\[thm:noncompact\]]{#thm:noncompact label="thm:noncompact"} For every $s\in\mathbb{C}$ with $\sigma=\operatorname{Re}s>0$ and every nonnegative exact-clock allocation satisfying [\[eq:exact-clock\]](#eq:exact-clock){reference-type="eqref" reference="eq:exact-clock"}, the accepted restriction of $L_s$ is noncompact and $$\left\lVert L_s\right\rVert_{\mathrm{ess}}=1.
\label{eq:essential-norm}$$ Consequently the whole source-weighted vertex adjacency is noncompact.

Choose on every $\Gamma_p$ an edge $e_p$ of minimum roof. Then $$\tau(e_p)\le\frac{\log p}{\ell(p)}.$$ Let $u_p$ be its source. Distinct prime cycles are vertex-disjoint, so $(\delta_{u_p})_p$ is an orthonormal, hence weakly null, sequence. Yet $$\left\lVert L_s\delta_{u_p}\right\rVert
=e^{-\sigma\tau(e_p)}
\ge p^{-\sigma/\ell(p)}\longrightarrow1.
\label{eq:edge-witness}$$ A compact operator maps weakly null bounded sequences to norm-null sequences, proving noncompactness.

All nonnegative-roof edge weights have modulus at most one, and the functional graph has at most one outgoing edge per vertex, so $\left\lVert L_s\right\rVert\le1$. After subtracting any compact operator, [\[eq:edge-witness\]](#eq:edge-witness){reference-type="eqref" reference="eq:edge-witness"} still supplies a tail with lower norm tending to one. Thus $\left\lVert L_s\right\rVert_{\mathrm{ess}}\ge1$, while the operator-norm upper bound gives [\[eq:essential-norm\]](#eq:essential-norm){reference-type="eqref" reference="eq:essential-norm"}.

[\[thm:no-schatten\]]{#thm:no-schatten label="thm:no-schatten"} For every $q>0$ and $\sigma>0$, the accepted restriction of $L_s$ does not belong to $\mathcal{S}_q$.

By [\[eq:block-singular\]](#eq:block-singular){reference-type="eqref" reference="eq:block-singular"}, its $q$th singular-value sum on the $p$-block is $$\sum_{e\in\Gamma_p}e^{-q\sigma\tau(e)}.$$ The convexity of $x\mapsto e^{-q\sigma x}$ and the exact total give $$\sum_{e\in\Gamma_p}e^{-q\sigma\tau(e)}
\ge \ell(p)\exp\!\left(-\frac{q\sigma\log p}{\ell(p)}\right).
\label{eq:jensen-schatten}$$ The right side tends to infinity. In particular the block contributions do not tend to zero, so their sum over primes diverges. This is precisely the $q$th power sum of the singular values of the orthogonal direct sum.

Trace class is the $q=1$ case. Therefore the ordinary Hilbert-space Fredholm determinant $\det_{\mathcal{H}}(I-zL_s)$ requested by the same-object protocol is not defined on any half-plane through the usual trace-class theory [@Simon1977]. The failure is stronger than divergence of a particular rank-one edge expansion: the operator is not even compact.

[\[thm:essential-circle\]]{#thm:essential-circle label="thm:essential-circle"} For every $s$ with $\operatorname{Re}s>0$, $$\mathbb{T}\subset\sigma_{\mathrm{ap},\mathrm{ess}}(L_s).
\label{eq:essential-circle}$$ Hence $I-zL_s$ is not Fredholm whenever $|z|=1$.

Fix $\lambda\in\mathbb{T}$. By [\[lem:cycle-block\]](#lem:cycle-block){reference-type="ref" reference="lem:cycle-block"}, the eigenvalues of the prime block are the $\ell(p)$ roots of $p^{-s}$. Their common modulus tends to one by [\[eq:block-radius\]](#eq:block-radius){reference-type="eqref" reference="eq:block-radius"}; their angular mesh is $2\pi/\ell(p)\to0$, and the common phase offset has size $O(\log p/\ell(p))\to0$. Choose an exact block eigenvalue $\lambda_p$ tending to $\lambda$ and a normalized eigenvector $x_p$ supported on that block. The vectors lie in mutually orthogonal finite-dimensional blocks, hence $x_p\rightharpoonup0$, while $$\left\lVert(L_s-\lambda I)x_p\right\rVert=|\lambda_p-\lambda|\longrightarrow0.$$ This singular Weyl sequence proves [\[eq:essential-circle\]](#eq:essential-circle){reference-type="eqref" reference="eq:essential-circle"}. If $|z|=1$, take $\lambda=z^{-1}$; a Fredholm operator cannot admit such a singular sequence for its zero spectral value.

The theorem does not identify a self-adjoint spectrum and does not concern Riemann zeros. It says that the graph-step verifier creates essential spectrum at the unit circle before any critical-strip spectral mechanism is available.

## An exact criterion behind the example

[\[prop:compactness-criterion\]]{#prop:compactness-criterion label="prop:compactness-criterion"} Let $B=\bigoplus_a B_a$ be a weighted adjacency on pairwise disjoint finite cycles of lengths $\ell_a$, with nonnegative edge roofs $\tau_{a,j}$ and totals $T_a=\sum_j\tau_{a,j}$. For a fixed allocation, $B$ is compact if and only if $$\min_j\tau_{a,j}\longrightarrow\infty.$$ There exists some allocation with the prescribed totals for which $B$ is compact if and only if $$\frac{T_a}{\ell_a}\longrightarrow\infty.
\label{eq:allocation-criterion}$$

The singular values of each block are its edge-weight moduli. A block direct sum of finite matrices is compact exactly when its largest block singular value tends to zero. Since that value is $e^{-\sigma\min_j\tau_{a,j}}$, this gives the first equivalence. Necessity of [\[eq:allocation-criterion\]](#eq:allocation-criterion){reference-type="eqref" reference="eq:allocation-criterion"} follows from $\min_j\tau_{a,j}\le T_a/\ell_a$. For sufficiency, use the uniform allocation $\tau_{a,j}=T_a/\ell_a$.

The prime verifier has $T_p/\ell(p)=\log p/\ell(p)\to0$, the opposite of the compactness regime. This criterion is included to expose the mechanism; we make no claim that its abstract weighted-shift content is novel.

# Raw orbit product and first-return collapse {#sec:return}

Noncompactness does not erase the finite-block cycle census. It changes what can legitimately be called an operator determinant.

[\[thm:raw-product\]]{#thm:raw-product label="thm:raw-product"} For $\operatorname{Re}s>1$ and $|z|\le1$, the product $$D_{\mathrm{orb}}^{\mathrm{raw}}(s,z)
:=\prod_p\left(1-z^{\ell(p)}p^{-s}\right)
\label{eq:raw-product}$$ converges normally on compact subsets of that domain. At $z=1$, $$D_{\mathrm{orb}}^{\mathrm{raw}}(s,1)
=\prod_p(1-p^{-s})=\zeta(s)^{-1}.
\label{eq:raw-zeta}$$ It is not the ordinary Fredholm determinant of the whole $L_s$.

For $|z|\le1$ and $\sigma>1$, $$\sum_p\left|z^{\ell(p)}p^{-s}\right|
\le\sum_pp^{-\sigma}<\infty.$$ The same majorant is locally uniform after fixing a compact lower bound for $\sigma$, so the canonical product converges normally. Equation [\[eq:raw-zeta\]](#eq:raw-zeta){reference-type="eqref" reference="eq:raw-zeta"} is Euler's absolutely convergent product. On every finite prime cutoff, [\[eq:prime-block\]](#eq:prime-block){reference-type="eqref" reference="eq:prime-block"} shows that [\[eq:raw-product\]](#eq:raw-product){reference-type="eqref" reference="eq:raw-product"} is the determinant of the finite direct sum. But [\[thm:noncompact,thm:no-schatten\]](#thm:noncompact,thm:no-schatten){reference-type="ref" reference="thm:noncompact,thm:no-schatten"} show that the infinite whole adjacency is not trace class. Thus no ordinary Hilbert-space Fredholm determinant of $L_s$ has been produced.

This theorem gives full graph-step information, not merely the specialization $z=1$. Formally differentiating its logarithm near $z=0$ recovers the block trace rule [\[eq:block-traces\]](#eq:block-traces){reference-type="eqref" reference="eq:block-traces"}; nonzero terms occur only at multiples of the expanding cycle lengths.

## Poincaré section

Let $$\Sigma=\{I_p:p\text{ prime}\}$$ be the section of accepted input states. One full return from $I_p$ traverses $\Gamma_p$ and accumulates weight $p^{-s}$.

[\[thm:first-return\]]{#thm:first-return label="thm:first-return"} The induced weighted return operator on $\ell^2(\Sigma)$ is $$R_s\delta_{I_p}=p^{-s}\delta_{I_p}.
\label{eq:return-diagonal}$$ For $\operatorname{Re}s>1$, $R_s\in\mathcal{S}_1$ and $$\det(I-zR_s)=\prod_p(1-zp^{-s}).
\label{eq:return-det}$$ As an operator, $R_s$ is unitarily equivalent to the diagonal prime-loop core obtained by replacing each entire verification cycle with one loop.

The product of the edge weights around $\Gamma_p$ is $p^{-s}$, proving [\[eq:return-diagonal\]](#eq:return-diagonal){reference-type="eqref" reference="eq:return-diagonal"}. Since $\sum_p|p^{-s}|<\infty$ for $\sigma>1$, the diagonal operator is trace class. Its Fredholm determinant is the product of its diagonal factors. Sending $\delta_{I_p}$ to the standard prime basis gives the asserted unitary equivalence.

First return is a legitimate dynamical operation; the point is that it is not the same discrete-time object. The original block and its induced loop give the respective factors $$\underbrace{1-z^{\ell(p)}p^{-s}}_{\text{original graph steps}}
\qquad\text{and}\qquad
\underbrace{1-zp^{-s}}_{\text{return steps}}.
\label{eq:marker-firewall}$$ They coincide at $z=1$. They also agree if induction explicitly carries the composite marker $z^{\ell(p)}$ as part of the return weight. Without that transport, equality at $z=1$ cannot be promoted to equality of marked determinants. This is the marker firewall in [\[fig:overview\]](#fig:overview){reference-type="ref" reference="fig:overview"}.

## The opposite roof choice

There is an instructive trace-class control. Retain the summable source roofs from the transient SD-C21 verifier and redirect the old terminal successful edge directly to $I_p$. In particular, retain its roof $\log(p(m+1))$; do not add a new $\log p$ return edge. The edge-by-edge summability majorant then survives on $\operatorname{Re}s>1$. However, every verifier edge already carries a clock comparable to at least $\log p$, so the total around $\Gamma_p$ is at least $\ell(p)\log p$, not $\log p$.

Thus the two natural objectives point in opposite directions: $$\begin{array}{ccl}
\text{exact total clock }\log p
&\Longrightarrow&\text{noncompact whole adjacency},\\[2pt]
\text{summable source edge clocks}
&\Longrightarrow&\text{trace class but wrong orbit clock}.
\end{array}
\label{eq:clock-dichotomy}$$ The source roofs are themselves a frozen modeling choice and are invisible to the desired Euler total once first return is imposed.

# Universal deciders and subdivision instability {#sec:universal}

The prime verifier is one instance of a general tension between exposed runtime and a short prescribed orbit clock. This generalization is an adversarial control: it shows that the mechanism compiles accepted supports rather than isolating a prime-specific invariant.

[\[thm:decider\]]{#thm:decider label="thm:decider"} Let a total deterministic machine decide $S\subseteq\{2,3,\ldots\}$, and suppose $S$ is infinite. Close the complete accepted computation on input $n\in S$ into a simple cycle of length $\ell_M(n)$ and send rejects to acyclic rays. Give every accepted cycle a nonnegative exact total roof $\log n$. Then:

1.  a compact allocation on the natural vertex space can exist only if $$\frac{\log n}{\ell_M(n)}\longrightarrow\infty
    \quad\text{along }n\in S;
    \label{eq:decider-compactness}$$

2.  if $\ell_M(n)/\log n\to\infty$ along an infinite accepted subsequence, then the associated block radii tend to one and every exact allocation is noncompact;

3.  the raw accepted-orbit ledger at $z=1$ is nevertheless $\prod_{n\in S}(1-n^{-s})$ wherever that product converges absolutely.

Apply [\[prop:compactness-criterion\]](#prop:compactness-criterion){reference-type="ref" reference="prop:compactness-criterion"} with $T_n=\log n$ and $\ell_n=\ell_M(n)$. This proves the first assertion. In the second regime, the cyclic-block radius $n^{-\sigma/\ell_M(n)}$ tends to one, and the minimum-roof proof of [\[thm:noncompact\]](#thm:noncompact){reference-type="ref" reference="thm:noncompact"} applies verbatim. The finite-block determinant at $z=1$ is $1-n^{-s}$ independently of the subdivision, which gives the third assertion by absolute convergence.

Every total decider can be slowed by an acceptance-independent uniformly prescribed delay: on input $n$, execute the original algorithm and then add, for example, $n$ dummy successor states before applying the already-computed decision. The padding rule does not inspect acceptance. Along any infinite accepted support it forces $\ell_M(n)/\log n\to\infty$. Therefore squares, powers of two, Fibonacci numbers, deterministic hash predicates, and many other supports can be made to reproduce the same exact-ledger/noncompactness pattern.

[\[cor:selector\]]{#cor:selector label="cor:selector"} The existence of an exact unmarked product $\prod_{n\in S}(1-n^{-s})$ from closed computation cycles, together with the clock-dilution obstruction, does not distinguish rational primes from an arbitrary infinite decidable support. The wrapper is `SELECTOR_TAUTOLOGICAL` and `PROVES_TOO_MUCH`.

The word "arbitrary" here concerns decidable support after a total program has been fixed. It does not claim a uniform decision procedure for all subsets of the integers.

## State-subdivision instability

The return marker reveals an even simpler presentation control.

[\[thm:subdivision\]]{#thm:subdivision label="thm:subdivision"} Fix an infinite support $S$ and totals $T_n=\log n$. There are two vertex-disjoint recurrent presentations with the same unmarked factors $1-n^{-s}$:

1.  one loop per $n\in S$, whose diagonal adjacency is trace class for $\operatorname{Re}s>1$;

2.  a subdivision of the $n$th loop into $\ell_n$ edges, with the same total roof, where $\ell_n/\log n\to\infty$; every nonnegative allocation in this presentation is noncompact.

Their graph-step factors are respectively $1-zn^{-s}$ and $1-z^{\ell_n}n^{-s}$.

The first operator is diagonal with trace norm $\sum_{n\in S}n^{-\sigma}<\infty$ for $\sigma>1$. Both finite cycle products at $z=1$ equal $1-n^{-s}$. The second presentation is noncompact by [\[prop:compactness-criterion\]](#prop:compactness-criterion){reference-type="ref" reference="prop:compactness-criterion"}. The marked factors follow from [\[lem:cycle-block\]](#lem:cycle-block){reference-type="ref" reference="lem:cycle-block"}.

Thus an Euler identity at $z=1$ is blind to graph-step subdivision, while compactness of the natural vertex adjacency is not. This is why the route protocol requires one frozen presentation and one frozen operator before an analytic determinant receives credit.

# Exact finite certificate and controls {#sec:certificate}

The infinite claims above are theorems. A separate deterministic prototype checks that the executable graph matches the contracted source lock and that no factor-existence shortcut is hidden in its transitions. The final suite passed $12/12$ tests. Independent prime enumeration is confined to sealed validation after graph construction; no target-zero data are present.

::: {#tab:prime-certificate}
     $p$   $\ell(p)$   $\ell(p)/\log p$   $\exp[-2\log p/\ell(p)]$
  ------ ----------- ------------------ --------------------------
       5           5            3.10667                   0.525306
     101         202            43.7692                   0.955334
    1009        3075            444.575                   0.995511
    4093       15293            1838.76                   0.998913

  : Selected prime-cycle certificates. The simulated path length is identically the formula in [\[eq:exact-length\]](#eq:exact-length){reference-type="eqref" reference="eq:exact-length"}. The last column shown is the smallest possible largest edge-weight modulus at $\sigma=2$, achieved by uniform allocation.
:::

Formula and explicit local-state traversal agree for all 564 primes through 4096. The source audit materializes 1,651 reachable quotient states at its frozen cutoff, finds zero forbidden factor identifiers or calls, verifies that the successful terminal transition is contracted, and confirms that reject paths enter acyclic cemetery rays.

## Marker and power-trace firewall

For a small exact cutoff at $s=2$, rational arithmetic verifies

-   raw and induced products are exactly equal at $z=1$;

-   they are exactly unequal at $z=1/3$;

-   the finite block power traces obey [\[eq:block-traces\]](#eq:block-traces){reference-type="eqref" reference="eq:block-traces"} at every tested nonzero power.

The equality at $z=1$ is therefore an expected specialization, not evidence that graph steps and return steps are interchangeable.

## Source-roof and universal controls

At $p=4093$, retaining the summable transient source roofs yields a total cycle clock approximately $28780.7834$ times $\log p$. This finite value illustrates the wrong-clock side of [\[eq:clock-dichotomy\]](#eq:clock-dichotomy){reference-type="eqref" reference="eq:clock-dichotomy"}; summability and the infinite lower bound are proved analytically.

Four accepted-support controls use the same uniformly prescribed $n^2+2$ padded runtime. Their most favorable largest edge weights near the cutoff are displayed in [\[tab:decider-controls\]](#tab:decider-controls){reference-type="ref" reference="tab:decider-controls"}. Exact products hold by construction for every accepted cycle.

L0.25rrX support & accepted count & largest accepted & optimal maximum edge weight\
squares & 63 & 4096 & 0.9999990084\
powers of two & 12 & 4096 & 0.9999990084\
Fibonacci numbers & 16 & 2584 & 0.9999976465\
seeded hash modulo five & 820 & 4090 & 0.9999990057\

These controls do not prove noncompactness by extrapolation; they instantiate [\[thm:decider\]](#thm:decider){reference-type="ref" reference="thm:decider"}. They show concretely why a verifier-per-input presentation cannot by itself certify arithmetic selectivity.

## Evidence firewall

All support, path-length, endpoint, source-scan, rational determinant, and power-trace comparisons are exact. Floating edge weights and clock ratios are illustrations only. The artifact ledger is regenerated twice and requires byte-identical hashes. The suite invokes neither Route B nor Riemann-zero training, validation, testing, fitting, or comparison.

# Strict route evaluation and limitations {#sec:route}

The recurrent closure improves the orbit census but fails the frozen same-object determinant gate. The final tuple is $$\boxed{
\begin{gathered}
(\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
\texttt{A1\_PASS\_ANALYTIC},\ \texttt{A2\_FAIL},\\
\texttt{A3\_FAIL},\ \texttt{A4\_FAIL}).
\end{gathered}}$$

#### A0: structural arithmetic relation.

The finite-full-shift skeleton supplies alphabet sum, tensor multiplication, successor, order, and entropy. The quotient state $q$ is explicitly advanced rather than hidden in a factor-existence guard. This earns structural, not analytic, arithmetic credit.

#### A1: analytic ledger pass.

The recurrent graph has exactly one primitive cycle for each prime and none for composites. Its total cycle weight is $p^{-s}$ and temporal repetitions are coherent. The normally convergent product [\[eq:raw-product\]](#eq:raw-product){reference-type="eqref" reference="eq:raw-product"} is an exact analytic orbit ledger on $\operatorname{Re}s>1$.

#### A2: fail.

The specified whole vertex adjacency is noncompact for every nonnegative exact-clock allocation and lies in no finite Schatten class. Therefore its ordinary Hilbert-space Fredholm determinant is unavailable. The raw orbit product is not substituted for it, and the induced diagonal is a different object. This is the only meaning of `A2_FAIL`; determinants on other spaces or under other regularizations are not ruled out.

#### A3: fail.

No continuation of the operator family, functional equation, Gamma factor, trivial-zero treatment, prime-number theorem, or Weil-type trace identity is derived. The known continuation of $\zeta$ cannot be imported backward into the noncompact adjacency.

#### A4: fail.

No canonical self-adjoint, unitary, Hamiltonian, scattering, or normal critical-line operator is constructed, and no spectrum is identified with nontrivial zeta zeros. The essential unit circle in [\[thm:essential-circle\]](#thm:essential-circle){reference-type="ref" reference="thm:essential-circle"} is an obstruction of the verifier clock, not a Hilbert--Pólya realization.

The corresponding registry is

    GO_RECURRENT_VERIFIER_ORBIT_LEDGER
    GO_CLOCK_DILUTION_THEOREM

    STOP_WHOLE_VERTEX_COMPACTNESS
    STOP_WHOLE_VERTEX_FREDHOLM_DETERMINANT
    FIRST_RETURN_COLLAPSE
    SELECTOR_TAUTOLOGICAL
    PROVES_TOO_MUCH

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED

## Explicit exclusions

The result does not rule out overlapping recurrent grammars, signed or matrix-valued cancellations, anisotropic quotient spaces, semifinite or regularized determinants, induced/local zeta functions, or geometric and scattering carriers. It does not say that roofs approaching zero invalidate countable-state suspensions. It does not deny the legitimacy of first return; it records that first return contracts the computation and changes the step marker.

The strongest counterargument is that the long verifier is merely a state subdivision of one prime return. We agree. turns that observation into the decisive same-object lesson: the unmarked Euler ledger is subdivision-invariant while compactness of the natural vertex presentation and its graph-step marker are not.

# Conclusion {#sec:conclusion}

Closing an explicit primality computation does place arithmetic instructions inside periodic dynamics. The contracted full-shift semiring verifier has one simple primitive cycle exactly for each prime, and that cycle contains the complete successor-by-successor quotient search. Its length is exactly $2+\sum_{d\le\sqrt p}\lceil p/d\rceil$ and asymptotically $\frac12p\log p$. With total entropy clock $\log p$, every primitive orbit has the desired weight $p^{-s}$.

The repair nevertheless fails at the natural whole-operator gate. A clock of size $\log p$ divided among order $p\log p$ states must create an edge clock tending to zero. Across disjoint prime blocks the resulting near-unit weights form orthogonal noncompactness witnesses. The adjacency has essential norm one, no finite Schatten membership, and an essential approximate unit circle. Consequently the raw Euler orbit product cannot be promoted to its ordinary Fredholm determinant.

Inducing makes the boundary exact. First return gives the trace-class diagonal prime-loop operator and the factor $1-zp^{-s}$, but the original cycle contributes $1-z^{\ell(p)}p^{-s}$. At $z=1$ the distinction vanishes; the arithmetic computation vanishes with it. Padded total deciders and state subdivision reproduce the same pattern for arbitrary decidable supports. The model is therefore algorithmically explicit but dynamically selector-tautological.

The next Symbolic Dynamics candidate should not add another vertex-disjoint verifier wrapper. It should start from a shared, overlapping, genuinely recurrent semiring-local grammar and prove a primitive-cycle separation theorem before selecting a roof, determinant, or target-zero comparison. For SD-C22 the verdict is complete: recurrent orbit ledger achieved, whole vertex Fredholm determinant obstructed, Route A rejected, Route B locked, and no claim about Riemann zeros.

# Supplementary proof details {#app:proofs}

## Endpoint count in the contracted convention

For prime $p$, each tested divisor $d$ contributes the edges $$T_{p,d}\to Q_{p,d,2}\to\cdots\to
Q_{p,d,\lfloor p/d\rfloor+1}\to T_{p,d+1}.$$ There are $1+\lfloor p/d\rfloor=\lceil p/d\rceil$ such edges, because $d\nmid p$. The two remaining edges are the initial $I_p\to T_{p,2}$ and terminal $T_{p,m+1}\to I_p$. Retaining a separate accept state would add one edge; it is not the object studied here.

For $p=2,3$ the divisor sum is empty and $\ell(p)=2$. For $p\ge5$ every $p/d$ in the sum is nonintegral, explaining why the lower harmonic bound in [\[eq:length-bounds\]](#eq:length-bounds){reference-type="eqref" reference="eq:length-bounds"} is strict there but not at the two smallest primes.

## Boundedness and reducing prime blocks

On the functional graph every vertex has exactly one forward image and every nonnegative-roof edge weight has modulus at most one. For a finitely supported vector $x$ on a component whose forward map is injective, the weighted shift is a contraction. The accepted prime components are simple cycles and hence injective; their direct sum has norm at most one. The frozen composite source roofs provide a bounded whole operator as well. All compactness and Schatten obstructions already occur on the reducing accepted subspace, so no claim depends on the detailed cemetery bound.

## Essential-norm witness modulo compact operators

Let $K$ be compact and let $(\delta_{u_p})$ be the orthonormal sequence from [\[thm:noncompact\]](#thm:noncompact){reference-type="ref" reference="thm:noncompact"}. Then $K\delta_{u_p}\to0$ in norm, while $\left\lVert L_s\delta_{u_p}\right\rVert\to1$. Hence $$\left\lVert L_s-K\right\rVert\ge
\limsup_p\left\lVert(L_s-K)\delta_{u_p}\right\rVert\ge1.$$ Taking the infimum over compact $K$ gives the essential-norm lower bound. The contraction upper bound gives equality.

## Schatten calculation for a nonnormal block

No eigenvalue/singular-value substitution is made. If $B_s\delta_{v_j}=w_j\delta_{v_{j+1}}$, then $$B_s^*B_s\delta_{v_j}=|w_j|^2\delta_{v_j}.$$ Thus the singular values are exactly $|w_j|$. The block is generally nonnormal when the edge moduli differ, but Jensen's inequality in [\[eq:jensen-schatten\]](#eq:jensen-schatten){reference-type="eqref" reference="eq:jensen-schatten"} is therefore still an exact Schatten calculation.

## Singular Weyl sequence

For a cyclic block, solve $B_sx=\lambda_px$ recursively from one nonzero coordinate. The compatibility condition is $\lambda_p^{\ell(p)}=p^{-s}$, which is exactly [\[eq:block-spectrum\]](#eq:block-spectrum){reference-type="eqref" reference="eq:block-spectrum"}; finite dimension permits normalization. Choosing one such eigenvector on each of pairwise disjoint prime blocks makes the sequence orthonormal even though individual blocks are nonnormal. Nearest roots approximate any prescribed unit phase because the angular mesh tends to zero. This proves the singular-sequence argument without invoking a normal-operator spectral theorem.

## Normal convergence of the raw product

Let $K$ be compact in $\{(s,z):\operatorname{Re}s>1,\ |z|\le1\}$. There is $\epsilon>0$ with $\operatorname{Re}s\ge1+\epsilon$ on $K$. Then $$\sum_p\sup_K|z^{\ell(p)}p^{-s}|
\le\sum_pp^{-1-\epsilon}<\infty.$$ The Weierstrass criterion proves normal convergence. This statement needs no trace of the infinite noncompact adjacency; it is a direct convergence theorem for the primitive factors.

## Why the return marker changes

For one $\ell$-cycle of total weight $w$, $$\operatorname{Tr}B^r=
\begin{cases}
\ell w^k,&r=k\ell,\\
0,&\ell\nmid r.
\end{cases}$$ The finite trace-log identity gives $$\exp\left(-\sum_{k\ge1}
\frac{z^{k\ell}}{k\ell}\ell w^k\right)=1-z^\ell w.$$ The first-return loop instead has trace $w^k$ at every return power and factor $1-zw$. The specialization $z=1$ forgets the elapsed graph time. Carrying $z^\ell$ as part of the return weight preserves it explicitly but does not turn return steps back into original graph steps.

## Universal padding quantifiers

The padding in [\[thm:decider\]](#thm:decider){reference-type="ref" reference="thm:decider"} is fixed uniformly as a function of input, before the accept/reject result is consulted. For instance, run $n$ dummy successor steps after the original total machine halts, then branch according to the stored result. This is acceptance-independent, although it is of course part of the chosen source presentation. It shows sensitivity to runtime presentation, not independence from all source choices.

# Claim, anti-claim, and route ledger {#app:ledger}

L0.31L0.18X statement & status & reason\
Expanded recurrent graph cycles exactly on primes & theorem & explicit quotient successor search plus square-root criterion\
Contracted prime cycle has $\ell(p)=2+\sum_{d\le\sqrt p}\lceil p/d\rceil$ & theorem & exact edge census, including the two endpoint edges\
Every exact-clock vertex adjacency is noncompact & theorem & minimum-roof edges give orthogonal near-isometric witnesses\
Accepted restriction lies in no finite Schatten class & theorem & exact singular values plus Jensen's inequality\
Unit circle is essential approximate spectrum & theorem & normalized eigenvectors on disjoint growing blocks\
Raw product equals $1/\zeta(s)$ at $z=1$ & theorem & normally convergent primitive-factor product on $\operatorname{Re}s>1$\
Raw product is $\det(I-zL_s)$ & false / not claimed & whole $L_s$ is noncompact and not trace class\
First-return determinant is exact & theorem & trace-class diagonal $R_se_p=p^{-s}e_p$\
First return preserves graph-step marker & false unless transported & original factor has $z^{\ell(p)}$, return factor has $z$\
Roofs tending to zero invalidate suspension flows & false / not claimed & the obstruction concerns the frozen vertex operator\
The compactness criterion is new in abstract form & not claimed & elementary weighted-shift framework is classical\
Finite implementation uses no factor oracle & exact certificate & 1,651 quotient states, zero forbidden calls, acyclic rejects\
Finite tests prove the infinite no-go & false / not claimed & all infinite statements have analytic proofs\
The model yields a critical-line or RH operator & false / not claimed & A3 and A4 fail; no target-zero data are used\

#### Frozen route package.

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_FAIL,
     A3_FAIL,
     A4_FAIL)

    GO_RECURRENT_VERIFIER_ORBIT_LEDGER
    GO_CLOCK_DILUTION_THEOREM
    STOP_WHOLE_VERTEX_COMPACTNESS
    STOP_WHOLE_VERTEX_FREDHOLM_DETERMINANT
    FIRST_RETURN_COLLAPSE
    SELECTOR_TAUTOLOGICAL
    PROVES_TOO_MUCH

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED

The positive and negative lines are both part of the result. The recurrent primitive ledger is exact, and the same graph fails the requested ordinary Fredholm determinant. An induced determinant or a formal orbit product does not erase that same-object failure.
