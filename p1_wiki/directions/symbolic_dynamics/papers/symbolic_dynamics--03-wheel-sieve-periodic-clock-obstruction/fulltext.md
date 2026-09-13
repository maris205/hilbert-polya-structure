---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--03-wheel-sieve-periodic-clock-obstruction"
canonical_tex: "symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction/main.tex"
canonical_pdf: "symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction/main.pdf"
source_sha256: "1cfda6588a2365dda0d00d09e6d22d8035d8783e1093d54a5bbce79edbdc3e25"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Clock Decoding and Periodic Factors of a Graded Wheel-Sieve Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/03-wheel-sieve-periodic-clock-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study whether a strictly graded symbolic realization of the recursive wheel sieve can be recoded into a stationary system with periodic orbits while retaining its exact prime clock. Let the source shift advance from level $k$ to $k+1$, and let its endogenous clock be the next wheel multiplier $q_{k+1}$. An equivariant source-to-target map admitting a single-valued decoder of this clock cannot identify two levels. Its direct image therefore inherits a strict grading and has no periodic points; no continuity, locality, finite alphabet, or compactness is needed. For orbit closures we give a topological extension under an explicit sufficient condition: a continuous decoder excludes $m$-periodic boundary points whenever the closure of the lag-$m$ clock pairs misses the diagonal. This condition holds for exact $q$ and $\log q$ in their ordinary topologies, but fails after one-point compactification. We also show that no compact target can continuously decode the full unbounded clock. Explicit symbolic counterexamples demonstrate that factors and closures can create cycles only by erasing the clock, making its extension discontinuous, or changing its topology. The elementary periodic contradiction is placed within the classical Livšic and ordered cohomology background; the contribution is its assumption-explicit wheel-sieve stationarization audit. Consequently this exact-clock branch stops before any periodic-orbit determinant is defined.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 12, 2026'
title: |
  Exact Clock Decoding and Periodic Factors\
  of a Graded Wheel-Sieve Shift
```

## Markdown 正文

# Introduction {#sec:introduction}

Forgetting information can create periodic factors of an aperiodic symbolic system. In an arithmetic model, however, the forgotten information may be exactly what made the symbols arithmetic. The wheel-sieve source considered here exposes this tension cleanly. Its dynamics advances through disjoint levels, and the transition out of level $k$ generates the next prime multiplier. The grading prevents recurrence; the multipliers provide the exact clock that a proposed stationarization is meant to retain.

Classical symbolic dynamics gives a precise language for shift-commuting maps and local codes [@hedlund1969; @lindmarcus2021]. Classical cohomological theory also makes periodic data a necessary compatibility condition: a coboundary has zero sum on every periodic orbit [@livsic1972]. In ordered cohomology, a nonnegative continuous integer coboundary for a chain-recurrent homeomorphism of a zero-dimensional compact metric space must vanish [@boylehandelman1996 Proposition 3.11]. The one-line observation that a periodic state cannot autonomously display a strictly advancing clock is therefore not presented here as a new universal theorem.

Our purpose is narrower and more operational. We close a residual branch left by a previous stationarization audit of one recursively generated wheel-sieve system. The audit had excluded strict extensions, forward-well-founded strong-bisimulation quotients, and finite-local finite-alphabet decoders, but it left open arbitrary-memory and countable alphabet observations. The present argument is independent of both alphabet size and decoder memory. It asks only whether the target state has one autonomous, single-valued rule that returns the exact source clock. Unlike the strict-extension direction from a proposed target back to the source, the present note studies source-to-target images and closures $\pi:X\to Y$.

The contributions are as follows.

1.  We prove that exact decoding makes every fiber of an equivariant source-to-target map level-consistent. The direct image inherits a strict grading and contains no periodic point, without topological assumptions.

2.  We prove an orbit-closure theorem under an explicit sufficient clock-topology condition: the closure of lagged clock pairs must avoid the diagonal. It applies to exact prime and log-prime clocks in their ordinary topologies. We separately give a feasibility result, independent of periodicity: compact targets cannot continuously decode the full unbounded clock at all.

3.  We give assumption-deletion controls. A level-modulo-$m$ factor has an $m$-cycle after clock erasure; a defect-shift closure gains a fixed point; and one-point compactification makes the boundary decoder continuous. These examples locate exactly where arithmetic inheritance fails.

4.  We translate the result into a falsification-first research decision. Exact wheel-clock factors and continuous exact-clock closures are theorem-stopped. A different internally generated arithmetic invariant remains logically open, but it must be evaluated as a new symbolic object rather than inheriting the wheel source's arithmetic credit.

A recent preprint proposes a deterministic, finite-alphabet but explicitly non-stationary S-adic automaton for the sieve of Eratosthenes [@heeren2026]. That construction reinforces the distinction at issue: symbolically realizing a stage-dependent sieve is not the same as producing a stationary periodic factor with an inherited exact clock. We make no priority claim for symbolic sieve encodings in general.

freezes the source and map direction. proves the set-theoretic obstruction, and [4](#sec:closure){reference-type="ref" reference="sec:closure"} treats orbit closures and compact targets. gives sharp counterexamples and separates an absolute clock from a suspension roof. records the scoped research decision. No determinant or operator is introduced.

# The graded wheel source and exact decoding {#sec:setup}

## Wheel recursion

Set $Q_0=1$ and $Q_1=q_1=2$, and recursively define $$q_{k+1}=\min\{n>q_k:\gcd(n,Q_k)=1\},
\qquad
Q_{k+1}=Q_kq_{k+1}.
\label{eq:wheel-recursion}$$ This rule contains no stored prime table.

[\[lem:prime-enumeration\]]{#lem:prime-enumeration label="lem:prime-enumeration"} For every $k\ge1$, $q_k$ is the $k$th rational prime and $Q_k=\prod_{j=1}^kq_j$.

The claim is true for $k=1$. Assume it through $k$. Every composite $n$ strictly between $q_k$ and the next prime has a prime divisor at most $q_k$, hence shares a factor with $Q_k$. The next prime shares none. Therefore the minimum in [\[eq:wheel-recursion\]](#eq:wheel-recursion){reference-type="eqref" reference="eq:wheel-recursion"} is precisely the next prime, and multiplication gives the formula for $Q_{k+1}$.

The arithmetic fact needed below is consequently modest but exact: the sequence $(q_k)$ is injective and unbounded. The dynamical obstruction would also apply to any other nonrecurrent chronology; primality enters only through [\[lem:prime-enumeration\]](#lem:prime-enumeration){reference-type="ref" reference="lem:prime-enumeration"}.

## Strict grading and target maps

At level $k\ge0$, let $$R_k=\{0\le r<Q_k:\gcd(r,Q_k)=1\}.$$ For $r\in R_k$, join $r$ to every lift $r+jQ_k\in R_{k+1}$ with $0\le j<q_{k+1}$ except the unique lift divisible by $q_{k+1}$. Let $X_k$ be the set of one-sided infinite paths whose first edge begins in $R_k$. Deleting the first edge gives the map $\sigma$ below. This residue graph fixes the wheel-sieve source, although the obstruction will use only its grading and exact multiplier clock.

Let $$X=\bigsqcup_{k\ge0}X_k,
\qquad
\sigma(X_k)\subseteq X_{k+1},
\label{eq:grading}$$ be the one-sided wheel tail-path system. Each $X_k$ is nonempty. Write $\ell(x)=k$ for $x\in X_k$ and define the exact integer clock and derived logarithmic value $$\kappa(x)=q_{\ell(x)+1},
\qquad
\tau(x)=\log\kappa(x).
\label{eq:clock}$$ Then $\ell(\sigma^n x)=\ell(x)+n$ and $\kappa(\sigma^n x)\ne\kappa(x)$ for every $n\ge1$.

[\[def:decoder\]]{#def:decoder label="def:decoder"} Let $S:Y\to Y$ be a self-map. A source-to-target map $\pi:X\to Y$ is *equivariant* if $$S\circ\pi=\pi\circ\sigma.
\label{eq:equivariance}$$ An *exact autonomous clock decoder* on the direct image is a single-valued function $d:\pi(X)\to C$ such that $$d(\pi(x))=a_{\ell(x)}
\label{eq:decoder}$$ for a frozen clock sequence $(a_k)$ in $C$. The wheel choices are $a_k=q_{k+1}$ or $a_k=\log q_{k+1}$. If $\pi$ is onto, it is called a factor map in the set-theoretic category used by the direct-image theorem.

The word *autonomous* is substantive. The decoder may read a state, edge, finite window, infinite window, or entire target configuration, but it must define one function of the target point. A rule that also reads the absolute time, source level, chosen lift, or traversal number is not a function on the target phase space. Classical sliding-block-code assumptions are therefore sufficient but not necessary for our theorem.

For $m\ge1$, write $$\operatorname{Per}_m(S)=\{y\in Y:S^my=y\}.$$ We distinguish the direct image $\pi(X)$ from an orbit closure $\overline{\pi(X)}$. The former needs no topology; the latter requires an explicit topology and inheritance rule.

# The direct-image obstruction {#sec:direct-image}

We first state the set-theoretic result for an arbitrary injective clock.

[\[lem:fiber\]]{#lem:fiber label="lem:fiber"} For maps $\pi:X\to Y$ and $\kappa:X\to C$, a function $d:\pi(X)\to C$ satisfying $d\circ\pi=\kappa$ exists if and only if $\kappa$ is constant on every fiber of $\pi$.

Necessity follows from $\pi(x)=\pi(x')\Rightarrow\kappa(x)=d(\pi(x))=d(\pi(x'))=\kappa(x')$. Conversely, fiber constancy makes the rule $d(\pi(x))=\kappa(x)$ independent of the chosen representative.

[\[thm:direct\]]{#thm:direct label="thm:direct"} Assume [\[eq:grading\]](#eq:grading){reference-type="eqref" reference="eq:grading"} and let $a_k$ be pairwise distinct. If $\pi:X\to Y$ is equivariant and admits an exact decoder in the sense of [\[def:decoder\]](#def:decoder){reference-type="ref" reference="def:decoder"}, then:

1.  no fiber of $\pi$ meets two different levels;

2.  $\pi(X)$ has a well-defined grading $\bar\ell$ satisfying $\bar\ell(Sy)=\bar\ell(y)+1$;

3.  $\pi(X)\cap\operatorname{Per}_m(S)=\varnothing$ for every $m\ge1$.

If $\pi$ is onto, then $Y$ has no periodic points.

If $\pi(x)=\pi(x')$, exact decoding gives $$a_{\ell(x)}=d(\pi(x))=d(\pi(x'))=a_{\ell(x')}.$$ Injectivity of the clock implies $\ell(x)=\ell(x')$. Hence $\bar\ell(\pi(x))=\ell(x)$ is well defined. Equivariance gives $$\bar\ell(S\pi(x))
=\bar\ell(\pi(\sigma x))
=\ell(\sigma x)
=\ell(x)+1.$$ If $S^my=y$ for $y\in\pi(X)$, iteration yields $\bar\ell(y)=\bar\ell(y)+m$, a contradiction.

[\[cor:wheel-direct\]]{#cor:wheel-direct label="cor:wheel-direct"} No equivariant factor of the graded wheel source can simultaneously have a periodic point and decode the exact pointwise clock $q_{k+1}$ or $\log q_{k+1}$.

Apply [\[thm:direct\]](#thm:direct){reference-type="ref" reference="thm:direct"} and [\[lem:prime-enumeration\]](#lem:prime-enumeration){reference-type="ref" reference="lem:prime-enumeration"}.

[\[rem:assumption-boundary\]]{#rem:assumption-boundary label="rem:assumption-boundary"} The proof does not use continuity, compactness, computability, finite memory, a finite alphabet, or injectivity of $\pi$. Pairwise distinctness can be weakened to $a_{k+m}\ne a_k$ for the particular period $m$ being excluded. Thus countable alphabets and infinite-memory decoders escape a finite-range theorem but do not escape [\[thm:direct\]](#thm:direct){reference-type="ref" reference="thm:direct"} while they remain single-valued target observables.

The same point can be expressed with a sequence decoder. Suppose $D:Y\to C^{\mathbb{N}}$ satisfies $D(Sy)=\operatorname{shift}D(y)$ and returns the full clock tail on the image. If $S^my=y$, then $D(y)$ is $m$-periodic. It cannot equal $(q_{k+1},q_{k+2},\ldots)$. Dropping shift equivariance merely stores an external chronology in the decoder and does not define a dynamical clock.

There is also a direct repetition-ledger consequence. If a target word of period $m$ is traversed twice while its lift advances through source levels, the same target edge would receive the two values $q_{k+j}$ and $q_{k+m+j}$. Either the target weight is fixed and fails exact decoding, or it depends on the lap number and is not autonomous. In the latter case the standard repetition identity for a roof, $T_{\gamma^r}=rT_\gamma$, is no longer a property of the target orbit.

# Orbit closures and compact targets {#sec:closure}

The direct image can be nonclosed. Its closure may contain new recurrent or periodic points, so exactness on $\pi(X)$ alone cannot control them. We now freeze the additional inheritance condition needed at the boundary.

Let $Y_0=\overline{\pi(X)}$ in a topological space $Y$, assume $S:Y_0\to Y_0$ is continuous, and let $C$ be a topological clock space. For $m\ge1$ define $$P_m=\{(a_k,a_{k+m}):k\ge0\}\subset C\times C,
\qquad
\Delta_C=\{(c,c):c\in C\}.
\label{eq:lag-pairs}$$

[\[thm:closure\]]{#thm:closure label="thm:closure"} Suppose $d:Y_0\to C$ is continuous and satisfies $d(\pi(x))=a_{\ell(x)}$. If $$\overline{P_m}\cap\Delta_C=\varnothing,
\label{eq:diagonal-separation}$$ then $Y_0\cap\operatorname{Per}_m(S)=\varnothing$.

Define the continuous map $$F_m:Y_0\to C\times C,
\qquad
F_m(y)=(d(y),d(S^my)).$$ Equivariance and exact decoding imply $F_m(\pi(X))=P_m$. Since $\pi(X)$ is dense in $Y_0$, continuity gives $F_m(Y_0)\subseteq\overline{P_m}$. If $S^my=y$, then $F_m(y)=(d(y),d(y))\in\Delta_C$, contradicting [\[eq:diagonal-separation\]](#eq:diagonal-separation){reference-type="eqref" reference="eq:diagonal-separation"}.

No metrizability, first countability, or continuity of $\pi$ is needed in this proof. The relevant regularity is continuity of the target dynamics and of the inherited clock.

[\[cor:closure-wheel\]]{#cor:closure-wheel label="cor:closure-wheel"} applies to each of the following:

1.  $C=\mathbb{N}$ with the discrete topology and $a_k=q_{k+1}$;

2.  $C=\mathbb{R}$ with its usual topology and $a_k=q_{k+1}$;

3.  $C=\mathbb{R}$ with its usual topology and $a_k=\log q_{k+1}$.

Consequently a continuous exact decoder of any of these clocks excludes all periodic points from $Y_0$.

In the discrete case, $P_m$ is closed and disjoint from the diagonal. In the real cases, both coordinates tend to $+\infty$ with $k$, so $P_m$ is locally finite in $\mathbb{R}^2$ and has no finite accumulation point. Hence it is closed in $\mathbb{R}^2$, and pairwise distinctness excludes its intersection with the diagonal.

Compactness gives a separate feasibility obstruction, independent of the periodic-point argument.

[\[prop:compact\]]{#prop:compact label="prop:compact"} Let $Y_0$ be compact and contain $\pi(X)$. There is no continuous total exact wheel-clock decoder $d:Y_0\to\mathbb{N}_{\mathrm{disc}}$. There is likewise no continuous decoder $d:Y_0\to\mathbb{R}$ of all values $q_{k+1}$ or $\log q_{k+1}$.

The continuous image of a compact space is compact. A compact subset of a discrete space is finite, while a compact subset of $\mathbb{R}$ is bounded. Exact decoding would place the infinite unbounded clock range in that image.

This proposition uses only compactness of $Y_0$ and continuity of $d$; it uses neither equivariance, periodicity, nor the diagonal-separation theorem.

Thus a compact finite-alphabet shift cannot continuously retain the complete absolute clock, regardless of decoder memory. A compactified or transformed clock may have a continuous extension, but it must then be checked against [\[eq:diagonal-separation\]](#eq:diagonal-separation){reference-type="eqref" reference="eq:diagonal-separation"}; continuity alone is not enough.

# Sharpness, boundary cycles, and roofs {#sec:sharpness}

The hypotheses above cannot be replaced by the statement that "factors of graded systems are aperiodic." Factors can create cycles freely.

## Clock erasure creates periodic factors

Fix $m\ge1$ and set $Y=\mathbb Z/m\mathbb Z$ with $S(i)=i+1\pmod m$. The map $$\pi_m(x)=\ell(x)\pmod m$$ is an equivariant surjection, and $Y$ is one $m$-cycle. It has no exact wheel-clock decoder: the same residue class receives the distinct values $q_{k+1},q_{k+m+1},\ldots$. This example proves that periodicity is obtained by forgetting chronology, not by stationarizing it faithfully.

It also shows sharpness with respect to the clock. If the frozen clock were periodic, $c_{k+m}=c_k$, then $d(i)=c_i$ would be an exact decoder on the same factor. Nonrecurrence of the wheel clock is therefore essential.

## A symbolic closure can gain a fixed point

Let $A=\{0,\#\}$, let $u\in A^{\mathbb Z}$ contain $\#$ only at coordinate $0$, and let $S$ be the left shift. Put $y_k=S^ku$ for $k\ge0$. Then $y_k\to 0^{\mathbb Z}$ in the product topology. The closed forward-invariant set $$Y=\{y_k:k\ge0\}\cup\{0^{\mathbb Z}\}$$ contains the fixed point $0^{\mathbb Z}$. Defining $\pi(x)=y_{\ell(x)}$ gives an equivariant image whose closure is $Y$.

On the image, $d(y_k)=q_{k+1}$ is exact. It has no continuous extension to $0^{\mathbb Z}$ with values in $\mathbb{N}_{\mathrm{disc}}$ or finite values in $\mathbb{R}$. A total assignment such as $d(0^{\mathbb Z})=2$ is discontinuous and post-hoc. The boundary fixed point is a genuine topological cycle but is arithmetically sterile relative to the inherited wheel clock.

Now change the clock topology to the one-point compactification $C=\mathbb{N}\cup\{\infty\}$ and set $d(0^{\mathbb Z})=\infty$. The decoder becomes continuous, yet the fixed point remains. Indeed $$(q_{k+1},q_{k+m+1})\longrightarrow(\infty,\infty),$$ so the lag-pair closure meets the diagonal and [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"} correctly does not apply. This control proves that "continuous decoder" is not a topology-free hypothesis.

## Absolute clock is not a suspension roof

A positive roof on a base system defines a suspension and assigns to a closed base orbit the sum of its roof values. It does not create new closed base orbits; standard periodic-orbit formalisms retain the repetition law $T_{\gamma^r}=rT_\gamma$ [@parrypollicott1990]. Calling the advancing absolute level label $\log q_{k+1}$ a roof therefore does not bypass [\[thm:direct\]](#thm:direct){reference-type="ref" reference="thm:direct"}. If one assigns a different value each time the same target edge is traversed, the quantity depends on external lap count or on a chosen source lift and is not an autonomous roof on the target.

We are not proving any obstruction to ordinary positive suspension roofs on periodic base systems. The obstruction concerns inherited pointwise absolute labels $q_{k+1}$ or $\log q_{k+1}$ on a revisited target state.

The alternatives form a sharp trichotomy:

1.  keep the exact clock in the target state, and the complete state is aperiodic;

2.  erase the clock, and periodic factors appear without inherited arithmetic labels;

3.  supply the clock from external time, a chosen lift, or traversal count, and the target is nonautonomous or the decoder is not single-valued.

# Consequences for the stationarization search {#sec:consequences}

The result is a compatibility screen, not a new arithmetic candidate. It must be applied to one frozen target object; arithmetic fidelity from the wheel source cannot be combined coordinatewise with periodic or determinant data from a different system.

\@L0.29\>XL0.22@ Proposed mechanism & Same-object diagnosis & Outcome\
Surjective factor with exact autonomous clock & The target inherits the strict grading and has no periodic point & [Theorem Stop]{.smallcaps}\
Direct image with arbitrary alphabet or memory & is independent of alphabet size and locality & [Theorem Stop]{.smallcaps}\
Orbit closure with continuous ordinary $q$ or $\log q$ decoder & Lagged clock pairs avoid the diagonal & [Theorem Stop]{.smallcaps}\
Level-modulo factor or constant factor & Cycles exist only after the exact clock is erased & arithmetic inheritance fails\
Boundary cycle with partial or discontinuous label & The cycle has no inherited target-intrinsic wheel clock & [Not Testable]{.smallcaps} as arithmetic ledger\
Appended periodic component with prime labels & Labels are an independent modeling choice, not a source consequence & forbidden transfer of A0 credit\
New intrinsic arithmetic invariant & Logically outside the theorem if it is not the levelwise wheel clock & new source lock and full audit required\

In the project's falsification-first terminology, a candidate needs both an endogenous arithmetic mechanism and a primitive-orbit ledger before an analytic determinant is meaningful. The exact-clock factor branch fails at the periodic-orbit gate. Clock-erased and boundary-only cycles fail to inherit the arithmetic mechanism. Therefore no candidate identifier is assigned here, no Artin--Mazur or Fredholm determinant is defined, and no zero comparison is authorized.

The result has deliberately low prime selectivity. Consecutive composites, random injective labels, and every other nonrecurrent chronology satisfy the same dynamical obstruction. This is appropriate for a negative compatibility theorem; primality is used only to establish that the wheel-generated clock is exact, injective, and unbounded. The theorem cannot be promoted into evidence for a zeta or spectral claim.

One route remains logically open inside Symbolic Dynamics: a new stationary grammar might generate periodic orbits carrying a different intrinsic arithmetic invariant. Such an object would not be a faithful stationarization of the levelwise wheel clock. It must start again at the arithmetic-origin gate, with its target space, transition rule, clock, function space, and orbit multiplicities frozen before any experiment. We record this only as the next source-lock problem, not as evidence supplied by the present theorem.

# Conclusion {#sec:conclusion}

An exact autonomous decoder cannot both forget the wheel source's level and retain its prime clock. It forces factor fibers to remain within a single level, transfers the strict grading to the direct image, and excludes all periodic points. With a continuous decoder, the conclusion extends to an orbit closure whenever lagged clock pairs stay away from the diagonal; this includes exact $q$ and $\log q$ in their usual topologies. Compact targets cannot continuously carry the full unbounded clock in the first place.

The counterexamples are equally important. Factors can have cycles after clock erasure, closures can acquire boundary cycles under a discontinuous decoder, and a compactified clock can make that decoder continuous. None of these cycles inherits a finite exact wheel clock. The valid conclusion is therefore scoped: the levelwise wheel chronology cannot be converted into an autonomous periodic-orbit ledger by factorization or continuous closure. It is not a prohibition on Symbolic Dynamics as a whole.

For the present research program, this is a theorem-level stopping result. The next admissible move is not a larger cutoff or a fitted determinant, but a new source lock for a genuinely different target-intrinsic arithmetic invariant. Until such an object supplies its own periodic and repetition ledger, analytic and spectral routes remain closed.

# Assumption-deletion audit {#app:audit}

\@L0.24\>X\>X@ Deleted or changed hypothesis & Explicit control & What the control proves\
Exact decoder & Constant factor or level modulo $m$ & Periodic factors are easy to manufacture after arithmetic chronology is forgotten.\
Decoder total on closure & Defect-shift fixed point with decoder only on $\pi(X)$ & A boundary cycle need not carry any inherited clock.\
Decoder continuity & Assign an arbitrary finite value at the defect-shift fixed point & Exactness on a dense image does not determine a boundary label.\
Lag-pair diagonal separation & One-point compactification $\mathbb{N}\cup\{\infty\}$ & Continuity alone does not exclude a boundary fixed point.\
Clock nonrecurrence & Periodic control $c_{k+m}=c_k$ & The level-modulo-$m$ factor then has an exact decoder; the hypothesis is sharp.\
Equivariance & Map levels to an arbitrary cycle without $S\pi=\pi\sigma$ & The construction is not a factor or dynamical recoding.\
Target-intrinsic decoder & Read absolute time, source lift, or traversal number & The rule is nonautonomous or multivalued on target states.\
Same-object discipline & Append a separately labeled periodic component & Its arithmetic labels require an independent origin audit.\

The direct-image theorem requires neither Hausdorffness nor continuity. The closure theorem does require a frozen topology on both target and clock. Measurability alone does not replace continuity: the defect-shift decoder with an arbitrary boundary value can be Borel measurable while the fixed point persists.

# Scope and decision record {#app:scope}

The paper studies only the Symbolic Dynamics family. It does not borrow a determinant, phase, operator, or clock from another system family. The frozen status is

    candidate_id: not_assigned
    determinant_convention: not_defined
    A2: A2_NOT_TESTABLE
    route_b_invocation_allowed: false
    outcome: THEOREM_STOP

The outcome applies to exact pointwise wheel-clock factors and to continuous exact-clock orbit closures satisfying diagonal separation. It does not cover a separately defined symbolic grammar with a different intrinsic arithmetic invariant. Such a grammar would be a new object and could not inherit the arithmetic verdict of the wheel source.

The recent non-stationary S-adic sieve proposal of @heeren2026 is recorded as related symbolic-dynamics work, not as a control and not as an ingredient in the proofs. Bratteli--Vershik or geometric realizations are not developed here; any such cross-object idea remains outside the present scope and may only be logged for a later round.
