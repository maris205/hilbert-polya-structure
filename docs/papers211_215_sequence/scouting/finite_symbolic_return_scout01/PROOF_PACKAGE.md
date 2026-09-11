# Proof package — clock normalization and exclusion limits

## Claim and status

**PROVABLE AS STATED** for the phase-lift proposition below.
It is an elementary comparison deduction, not a new candidate system,
new source theorem or independent review.

A new literal satisfying an all-parameter recurrent theorem and a materially
separate inverse / observable-enumeration theorem is
**NOT CURRENTLY JUSTIFIED BY THIS SCOUT**. No such literal was selected.

## Assumptions and notation

Let $X$ be finite and nonempty, $m\ge1$, and let
$U_0,\ldots,U_{m-1}:X\to X$ be bijections. Products act right-to-left.
Define the fixed sweep and its ordinary autonomous phase lift by

$$
S=U_{m-1}\cdots U_0,\qquad
F(x,j)=(U_jx,j+1\bmod m)
$$

on $X$ and $X\times\mathbb Z/m\mathbb Z$, respectively. Let
$H=X\times\{0\}$. The carrier contains every phase; the phase is not erased.
The first-return map means the first strictly positive visit to $H$.

## Strategy and dependency map

1. The explicit phase coordinate forces first return at $m$.
2. Composition identifies the return map with $S$.
3. Divisibility and minimality give exact periods, not just bounds.
4. Intersections of finite cycles with $H$ give an orbit bijection.

No source's graph theorem, experiment, canonical output or P212 formula is
needed for this general argument.

## Proof

Step 1. The inverse is
$F^{-1}(y,k)=(U_{k-1\bmod m}^{-1}y,k-1\bmod m)$, since either composition
restores the phase and cancels the same bijection. Thus $F$ is a permutation.
After $r$ steps from $H$, the phase is $r\bmod m$. The least positive
possible return is $m$, and exactly $m$ steps return every point to $H$.
Direct composition gives

$$F^m(x,0)=(Sx,0),\qquad F^{mk}(x,0)=(S^kx,0)\quad(k\ge0).$$

Step 2. Let $p$ be the least positive $S$-period of $x$; it exists because
$S$ is a permutation of a finite set. The displayed identity gives an
$F$-return at $mp$. Any positive $F$-return time is a multiple $mk$ by the
phase condition; then $S^kx=x$, whence $k\ge p$. The exact $F$-period is
therefore $mp$.

Step 3. Every $F$-orbit meets $H$, since advancing the phase visits zero.
Its intersection with $H$ is exactly one $S$-orbit, under $(x,0)\leftrightarrow x$:
successive visits are separated by $m$ and apply $S$ once. Distinct
$F$-orbits have disjoint intersections; an $S$-orbit generates one $F$-orbit.
Hence there is a bijection on orbit sets. A sweep orbit of size $p$ becomes
one microstep orbit of size $mp$, not $m$ distinct orbits. The number of
orbits is unchanged. This includes $m=1$. $\square$

## Application to the source clock, with its limits

For the common graph-label toggles on graphs with $n\ge2$, choose $m=n$ and
$U_j=\tau_{j+1}$. Defant's toric sweep is
$\tau_n\cdots\tau_1$; Seekamp's state includes the next-toggle label and
takes one toggle plus one phase advance. Thus the forest sweep period
$(n-1)t/\gcd(t,n)$ corresponds to microstep period
$n(n-1)t/\gcd(t,n)$ under this precise lift. For a tree these are
$n-1$ and $n(n-1)$, respectively. The apparent discrepancy is not a new
period phenomenon. This uses the source's forest theorem only at its stated
hypotheses; it supplies no arbitrary-graph or iterated-bridge classification.
[Defant](https://arxiv.org/pdf/2112.06843),
[Seekamp](https://arxiv.org/pdf/2512.00692).

## What bijectivity does and does not subtract

The old permutation desk already proves that a fixed word of swap-invariant
guarded involutions has a reverse-word inverse. Its genuine finite autonomous
factors, invariant restrictions and complete first-return maps are again
permutations. A forgotten observation that does not satisfy a commuting
factor identity is not covered.

These facts only give singleton immediate fibres. Cycle lengths, labelled
cycle multiplicities and observable decorations are additional information:
neither the inverse formula nor the statement “every state is recurrent”
determines them. A return section can conceal temporal information unless
its return-time function is also proved. We therefore do not infer that
sweep, general whirling or all promotion variants lack enumerative residuals.

Conversely, a known conjugacy transports orbit lengths and multiplicities,
and transports a specified statistic only when the statistic's adapter is
also supplied. A new coordinate name, phased presentation or reverse-word
decoder is not by itself a material second mechanism. P212's original
decorated-core census is an explicit occupied example of the distinction.

## Corrections and open risks

The phase proposition requires bijections and a full explicit phase carrier.
It does not assert a period law for state-dependent schedules, noninvertible
normalizers, arbitrary quotients or incomplete stopping observations.
No new scheduler, carrier repair or graph family is adopted here.

The proof is author work checked symbolically. Source ownership is bounded
by the body extents in the source report; it is not global priority,
manuscript acceptance or a successful numerical check.
