# TR8: unchanged strong-height question and two bounded mechanisms

2026-09-08 UTC. This continues TR7, not a fresh paper contract.
Only this directory is writable by the arithmetic delegate.

## Original claim retained

For every $c\in\mathbb Q$, use
$F_c(x,y)=(y,y^2+c-x)$ on all affine algebraic points, with the original
forward/backward iterate clock and absolute projective Weil height:

$$
\widehat h_c^\pm(P)=\lim_{n\to\infty}2^{-n}h(F_c^{\pm n}P),
\qquad
b(c)=\inf_{\substack{P\in(\mathbb Q^{\rm tr})^2\\
                    P\notin\operatorname{Per}(F_c)}}
       \bigl(\widehat h_c^+(P)+\widehat h_c^-(P)\bigr).
$$

The question is the entire rational-parameter zero locus of $b$, with a
terminating input-$c$ decision. A positive answer requires an explicit
rational lower bound valid for every nonperiodic totally-real point;
a zero-gap answer requires a terminating construction of distinct
nonperiodic points with certified total canonical height at most $2^{-j}$.
Degrees, denominators, curves and zero coordinates are not restricted.
The exact [TR7 contract](../../continuation_round7/arithmetic_scout/SCOUT_REPORT.md)
remains authoritative. One parameter, a generic-sequence theorem, or a
horseshoe-region helper cannot replace it.

## Mechanism E: exceptional curves

Compare the actual generic equidistribution hypotheses with sequences
on a fixed curve, starting with the reversible diagonal. Seek a valid
curve-level lower bound or a way to extract a generic small sequence
without losing total reality, nonperiodicity or small total height.
The presence of infinitely many periodic points on a symmetry curve
cannot by itself supply nonperiodic witnesses.

Failure boundary: if only a generic equidistribution corollary follows,
record the exact missing curve/effectivity step. Do not admit that
smaller claim or declare the strong height gap proved.

During the hand feasibility check, a sharpened route was identified:
use the stabilized Zariski closures of all nonperiodic small-height
points and the two-sided height inequalities to test whether an
exceptional curve can persist. A second, explicit subcase to check is
$c>1$, where the native recurrence satisfies
$x_{n+1}-2x_n+x_{n-1}=(x_n-1)^2+c-1$; combine its strict convexity with
a finite real escape window. Both remain helpers within the same full
question, not additional contracts or mathematical executions.

## Mechanism K: fixed kicked closing equations

Test the coordinator's proposed construction with fixed
$\varepsilon=(0,1)$ and $F_c^N(P)=P+\varepsilon$, $N\ge3$.
Writing $a=-c$ and $P=(x_0,x_1)$ gives the cyclic quadratic equations

$$
x_i^2=a+x_{i-1}+x_{i+1}+\mathbf1_{i=0},
\qquad i\in\mathbb Z/N\mathbb Z.
$$

The first explicit region to test is rational $a\ge16$. The proposed
proof uses sign-wise square-root contraction and a complete algebraic
root count, nonarchimedean maximum estimates uniform in $N$, and the
midpoint $F_c^{\lfloor N/2\rfloor}(P)$. The all-positive branch is
proposed as a nonperiodic witness via real escape after the kick.

Required gates: all algebraic conjugates simultaneously real; complete
root exhaustion rather than one numerical branch; height bounds uniform
in $N$, including finite places and the fixed rational parameter;
actual nonperiodicity; effective root selection, distinctness and the
stated height-error certificate. Failure of any gate leaves the helper
unproved. Success still does not classify the remaining rational parameters.

The existing P62 periodic horseshoe exhaustion is prior ownership, not
this nonperiodic height construction. No old proof or program is rerun.

## Execution boundary

Default mathematical executions: zero. No diagnostic is yet authorized
by this file: any later single exact diagnostic must first specify its
complete input list, output, failure interpretation and the inherited
60 CPU-second / 256 MiB cap. No GPU, paid model API, Git mutation,
global index, old proof, manuscript or PDF is part of this lane.
Hand proof and targeted primary-source verification are the work here.
Maintain NO_BAD_EULER_OR_ROOT_NUMBER.
