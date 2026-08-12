# Proof Package

## Claim

Let $(X,\sigma)$ be the graded wheel-sieve path system and let
$\kappa:X\to C$ be a frozen injective clock, specialized to $q_{k+1}$ or
$\log q_{k+1}$ on level $k$ for the wheel source.  Consider a
shift-compatible map $\pi:X\to Y$ into a dynamical system $(Y,S)$ and a
single-valued decoder $d:\pi(X)\to C$ with $d\circ\pi=\kappa$.  The decoder
need not extend to all of $Y$ for the first claim.

1. No point of $\pi(X)$ is periodic under $S$.
2. Let the clock take values in a topological space $C$.  If $Y$ is
   topological, $S$ and $d:Y\to C$ are continuous,
   $Y_0=\overline{\pi(X)}$, and the lagged clock pairs remain separated from
   the diagonal, then $Y_0$ has no periodic point.  This covers both the
   discrete integer clock and the ordinary real-valued $q$ and $\log q$
   clocks.
3. The unrestricted claim “every observational recoding of the wheel source
   has no periodic point” is false.  Boundary periodic points can be created
   after clock erasure or with a discontinuous/partial decoder, but their
   arithmetic clock is not continuously inherited from the source.
4. No compact target admits a continuous total exact decoder into either
   $\mathbb N$ with its discrete topology or $\mathbb R$ with clock values
   $q_{k+1}$ or $\log q_{k+1}$.

## Status

- Claim 1: **PROVABLE AS STATED** under the explicit exact-decoder and
  semiconjugacy assumptions.
- Claim 2: **PROVABLE AFTER THE STATED TOPOLOGICAL ASSUMPTIONS**.  Decoder
  continuity and separation of lagged clock pairs from the diagonal are used
  essentially.  Discreteness is sufficient but not necessary.
- Claim 3: **PROVABLE AS STATED** by explicit counterexamples.
- Claim 4: **PROVABLE AS STATED** by compactness of the decoder image.
- A universal obstruction for arbitrary noncontinuous or non-shift-compatible
  recodings: **NOT CURRENTLY JUSTIFIED**.

## Assumptions

- $X=\bigsqcup_{k\ge0}X_k$ and $\sigma(X_k)\subseteq X_{k+1}$.
- $\ell(x)=k$ for $x\in X_k$.
- $q_j$ is the $j$-th rational prime and
  $\kappa(x)=q_{\ell(x)+1}$.
- $\pi\circ\sigma=S\circ\pi$.
- $d\circ\pi=\kappa$.
- Only Claim 2 assumes topologies, continuity of $S$ and $d$, and separation
  of lagged clock pairs from the diagonal.

## Notation

- $\operatorname{Per}_m(S)=\{y:S^my=y\}$ for $m\ge1$.
- $Y_0=\overline{\pi(X)}$ in Claim 2.
- The logarithmic roof is $\tau=\log\kappa$ and is derived only after the
  integer clock has been decoded.

## Proof Strategy

The image theorem is a contradiction between periodicity after decoding and
strict clock drift along the source grading.  The closure theorem turns
continuity into a common open neighborhood on which the decoded values at
times $0$ and $m$ agree, then intersects that neighborhood with the dense
image.  The boundary controls explicitly delete one hypothesis at a time.

## Dependency Map

1. Prime enumeration from Paper 01 implies
   $\kappa(\sigma^m x)\ne\kappa(x)$ for every $m\ge1$.
2. Semiconjugacy gives $S^m\pi(x)=\pi(\sigma^m x)$.
3. Exact decoding converts equality of target states into equality of the two
   source clock values.
4. Exact decoding also prevents a fiber of $\pi$ from meeting two levels.
5. Claim 2 additionally uses continuity of $(d,d\circ S^m)$, density of
   $\pi(X)$ in $Y_0$, and separation of lag-$m$ clock pairs from the
   diagonal.
6. Claim 4 uses compactness and the unbounded range of the wheel clock.
7. The counterexamples depend on neither arithmetic fitting nor Riemann-zero
   data; they only show why the hypotheses cannot be silently removed.

## Proof

### Step 1 — strict drift of the wheel clock

Take $x\in X_k$ and $m\ge1$.  Then $\sigma^m x\in X_{k+m}$, hence

$$
\kappa(x)=q_{k+1},
\qquad
\kappa(\sigma^m x)=q_{k+m+1}.
$$

Distinct indices give distinct rational primes, so

$$
\kappa(\sigma^m x)\ne\kappa(x).
$$

### Step 2 — exact-clock image obstruction

First observe that exact decoding forces level-consistent fibers.  If
$\pi(x)=\pi(x')$, then

$$
q_{\ell(x)+1}=d(\pi(x))=d(\pi(x'))=q_{\ell(x')+1},
$$

so $\ell(x)=\ell(x')$.  Hence
$\bar\ell(\pi(x))=\ell(x)$ is a well-defined grading on $\pi(X)$ and
$\bar\ell(S\pi(x))=\bar\ell(\pi(x))+1$.

Assume that $y=\pi(x)$ satisfies $S^my=y$ for some $m\ge1$.  Exact decoding
and semiconjugacy give

$$
\begin{aligned}
\kappa(x)
  &=d(\pi(x))
   =d(y)
   =d(S^my) \\
  &=d(S^m\pi(x))
   =d(\pi(\sigma^m x))
   =\kappa(\sigma^m x).
\end{aligned}
$$

This contradicts Step 1.  Therefore

$$
\pi(X)\cap\operatorname{Per}_m(S)=\varnothing
\qquad(m\ge1).
$$

In particular, if $\pi$ is onto, then $S$ has no periodic point.

### Step 3 — continuous closure obstruction

Embed the exact clock in the topological clock space $C$.  For fixed
$m\ge1$, set

$$
E_m=\{(\kappa(x),\kappa(\sigma^m x)):x\in X\}\subset C\times C
$$

and let $\Delta_C=\{(c,c):c\in C\}$.  By hypothesis,
$\overline{E_m}\cap\Delta_C=\varnothing$.

Assume that $y\in Y_0$ satisfies $S^my=y$.  The map

$$
F_m=(d,d\circ S^m):Y_0\longrightarrow C\times C
$$

is continuous, while exact decoding and semiconjugacy give
$F_m(\pi(x))=(\kappa(x),\kappa(\sigma^m x))$.  Since $\pi(X)$ is dense in
$Y_0$, continuity implies

$$
F_m(Y_0)\subseteq\overline{F_m(\pi(X))}=\overline{E_m}.
$$

But periodicity gives $F_m(y)=(d(y),d(y))\in\Delta_C$, contradicting the
separation hypothesis.  Hence

$$
Y_0\cap\operatorname{Per}_m(S)=\varnothing
\qquad(m\ge1).
$$

The argument does not assume that $Y$ is metrizable or first countable.
For $C=\mathbb N$ with the discrete topology, $E_m$ is disjoint from the
diagonal and already closed.  For $C=\mathbb R$ with the usual topology and
clock values $q_{k+1}$ or $\log q_{k+1}$, $E_m$ is locally finite and escapes
to infinity, so its closure also misses the diagonal.

### Step 3b — compact-target obstruction

Suppose $Y_0$ is compact and $d:Y_0\to\mathbb N$ is continuous for the
discrete topology.  Then $d(Y_0)$ is compact in a discrete space and is
therefore finite.  Exact decoding would put every $q_{k+1}$ in $d(Y_0)$, a
contradiction.  If instead $d:Y_0\to\mathbb R$ continuously decodes
$q_{k+1}$ or $\log q_{k+1}$, then $d(Y_0)$ is compact and hence bounded,
again contradicting the unbounded clock range.  Thus a compact symbolic
target cannot continuously carry the full exact wheel clock, independently
of whether it has periodic points.

### Step 4 — boundary fixed point after loss of decoder continuity

Let

$$
Y=\{0\}\cup\{(k+1)^{-1}:k\ge0\}\subset\mathbb R
$$

and define

$$
S(0)=0,
\qquad
S((k+1)^{-1})=(k+2)^{-1}.
$$

This $S$ is continuous.  Define $\pi(x)=(\ell(x)+1)^{-1}$.  Then
$\pi\circ\sigma=S\circ\pi$, the image is dense in $Y$, and $0$ is fixed.
On the image, the rule

$$
d((k+1)^{-1})=q_{k+1}
$$

is an exact decoder.  It has no continuous extension to the fixed point:
the sequence $q_{k+1}$ is unbounded while $(k+1)^{-1}\to0$.  A total
extension such as $d(0)=2$ exists only as a discontinuous decoder.  The value
at $0$ is not inherited continuously from the wheel clock.

### Step 5 — fixed point after clock erasure

Let $Y=\{*\}$, let $S(*)=*$, and let $\pi$ be constant.  This is a
shift-compatible surjection and its target has a fixed point.  No decoder can
satisfy $d\circ\pi=\kappa$, because the left side is constant and $\kappa$
is not.  Thus factor periodicity is easy to manufacture only after the exact
clock has been erased.

More generally, the factor $\pi_m(x)=\ell(x)\bmod m$ maps the grading to an
$m$-cycle.  It is shift-compatible, but a state revisited after one lap would
have to decode both $q_{k+1}$ and $q_{k+m+1}$.  Therefore it cannot carry a
single-valued exact clock decoder.

### Step 6 — why clock topology matters

The boundary construction becomes a continuous-decoder counterexample if
the clock is compactified.  Let

$$
C=\mathbb N\cup\{\infty\}
$$

be the one-point compactification of the discrete natural numbers.  In the
space from Step 4, define

$$
d((k+1)^{-1})=q_{k+1},\qquad d(0)=\infty.
$$

Then $d:Y\to C$ is continuous and $0$ remains fixed.  Here the lagged clock
pairs converge to $(\infty,\infty)$, so
$\overline{E_m}\cap\Delta_C\ne\varnothing$.  Thus continuity alone is
insufficient; the lag-pair separation in Claim 2 is essential.

Steps 1--6 prove Claims 1--4. $\square$

## Corrections or Missing Assumptions

- A shift-compatible map alone does not preserve the absence of periodic
  points from source to factor.  The exact decoder is the decisive extra
  hypothesis.
- Claim 2 needs a total continuous decoder on the closure, not merely a
  decoder defined on $\pi(X)$.
- Decoder continuity alone is insufficient for an arbitrary compactified
  clock codomain.  The lagged clock-pair closure must avoid the diagonal.
- A periodic point in $Y_0\setminus\pi(X)$ may be assigned a value by a
  discontinuous rule, but that assignment is not a continuous inheritance
  theorem.
- An orbit-level rule that assigns arithmetic data directly to new target
  cycles is outside the pointwise clock theorem.  Such a rule is a new
  arithmetic mechanism and must pass A0 independently.
- A non-shift-compatible observation is not a factor or dynamical recoding in
  the frozen category.

## Open Risks

- A separately defined symbolic system could possess periodic orbits and an
  independent, non-target-fitted arithmetic rule.  The theorem does not rule
  out such a system.
- The theorem does not classify every discontinuous measurable decoder.
  Such decoders require a separate naturality and function-space argument.
- The theorem excludes inherited periodic points, not every possible
  orbit-level arithmetic statistic on boundary cycles.
- No novelty claim will be made until the literature audit distinguishes the
  elementary general lemma from its wheel-sieve application.
