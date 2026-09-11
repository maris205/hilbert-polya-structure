# Floored complex square root on a finite integer square

2026-09-08 UTC. Author: `/root/round211_nonlinear_scout`.
`NO_PROMOTION / ONE_LITERAL_ATTEMPT / ZERO_RESERVES /
ZERO_SCIENTIFIC_EXECUTIONS / HOLD_EXTERNAL`.

The lane considered one literal, abbreviated FCSR below. The provisional
name QCS in a parent progress message denotes this same map, not another
candidate or variant. No second or third literal was nominated. Root
specified the lane and mechanism-credit boundary but supplied no new
proof contribution to FCSR and made no admission commitment.

## Claim and assumptions

For an integer $M\ge0$, let $X_M=\{0,\ldots,M\}^2$. Set
$$\rho=\sqrt{a^2+b^2},\qquad
T(a,b)=\left(\left\lfloor\sqrt{\frac{\rho+a}{2}}\right\rfloor,
            \left\lfloor\sqrt{\frac{\rho-a}{2}}\right\rfloor\right).$$
This is the componentwise downward rounding of the principal square root
of $a+ib$. Both square roots are nonnegative. All calculations use the old
ordered pair; there is no modular reduction, reset, clipping, sign choice,
randomness, or altered boundary rule.

Write $\operatorname{isqrt}(n)=\lfloor\sqrt n\rfloor$ for a
nonnegative integer $n$. The same literal has the exact integer formula
$$r=\operatorname{isqrt}(a^2+b^2),\qquad
T(a,b)=\left(\operatorname{isqrt}\left(\left\lfloor\frac{r+a}{2}\right\rfloor\right),
             \operatorname{isqrt}\left(\left\lfloor\frac{r-a}{2}\right\rfloor\right)\right).$$
This equivalence is a mathematical identity, not an executed verifier.

We prove the following elementary boundaries:

1. The map closes on $X_M$. For $M=0$ its only state is fixed. For
   $M\ge1$, the recurrent set is exactly $\{(0,0),(1,0)\}$, both fixed.
2. For $M\ge1$, the full basin of $(0,0)$ is exactly
   $\{(0,0),(0,1)\}$. Every other state terminates at $(1,0)$.
3. If $S=a^2+b^2$ and $h(a,b)$ is fixed-point entrance time, then
   $$h(a,b)\le\min\{t\ge1:2^{2^t}>S\}.$$
   Fixed states have $h=0$. This bound is explicitly **not sharp** in
   general and is only ordinary radial contraction.
4. Every target fibre has the evaluated one-dimensional square-root sum
   proved below. This is a quantization-window calculation, not a new
   independent inverse mechanism or a sharp maximum-fibre theorem.

## Status and missing obligation

The four statements are `PROVABLE AS STATED` as elementary author
deductions. A sharp full-square time formula, a complete pointwise depth
classification and a global maximum-fibre theorem are **NOT CURRENTLY
JUSTIFIED**. No finite run supports them. In particular, neither the real
axis's scalar square-root clock nor an unquantized complex-root iterate may
be substituted for the actual rounded two-coordinate orbit.

## Strategy and dependency map

Integer output thresholds allow replacing $\rho$ by its integer part.
The squared Euclidean norm then falls at least as fast as integer square
root. The first iterate has first coordinate at least the second, removing
the extra unit-norm point from the recurrent region. Finally, fixing the
old first coordinate converts the four output inequalities into an
explicit integer interval for the old second coordinate.

1. Integer thresholds prove the exact integer formula.
2. A coordinate bound proves finite-carrier closure.
3. Squared-norm descent and first-quadrant order prove the recurrent set
   and the nonsharp time bound.
4. Positivity of the real output proves the two basin descriptions.
5. Squaring sign-checked inequalities proves the full-target floor sum.

## Proof

### 1. Integer-threshold identity and closure

For every integer $k\ge0$, the first real square-root coordinate is at
least $k$ precisely when $\rho\ge2k^2-a$. The right side is an integer,
so this is equivalent to $r\ge2k^2-a$. Taking the integer output threshold
again gives the displayed formula for the first coordinate. Replacing
$-a$ by $+a$ proves the second formula. Since $r\ge a$, all arguments
of integer square root in the literal formula are nonnegative.

Let $p,q$ be the unrounded real and imaginary root coordinates. Then
$p\ge q\ge0$. For $0\le a,b\le M$,
$$p^2=\frac{\rho+a}{2}\le\frac{\sqrt2+1}{2}M<(M+1)^2.$$
The strict inequality follows because $(\sqrt2+1)/2<2$ and
$(M+1)^2-2M=M^2+1>0$. Therefore $\lfloor p\rfloor\le M$,
and $0\le\lfloor q\rfloor\le\lfloor p\rfloor\le M$.
This proves closure, including $M=0$ without a special repaired rule.

### 2. Norm descent, recurrence and the stated bound

Put $(u,v)=T(a,b)$. Since $u\le p$, $v\le q$ and both are nonnegative,
$$u^2+v^2\le p^2+q^2=\rho=\sqrt S.$$
The left side is an integer, so it is at most $\operatorname{isqrt}(S)$.
For $S\ge2$ this is strictly smaller than $S$. Thus every orbit eventually
has squared norm at most one. After the first step $u\ge v$, so the only
such possible states are $(0,0)$ and $(1,0)$. They are fixed by direct
substitution. The time-zero remaining norm-one state $(0,1)$ maps to
$(0,0)$. This proves that there are no other recurrent points.

Iterating the norm inequality gives
$$S_t\le\operatorname{isqrt}^{\,t}(S)=\left\lfloor S^{1/2^t}\right\rfloor.$$
The identity follows by integer thresholds: the right side is at least
$k$ precisely when $S\ge k^{2^t}$, which is also the threshold for the
iterated integer square root. If $2^{2^t}>S$, then $S_t\le1$. For
$t\ge1$ the ordered-coordinate argument above makes the state fixed,
proving the bound. This proves no equality statement for that bound.

### 3. Complete endpoint basins

When $a\ge1$, the first unrounded root coordinate satisfies
$p^2=(\rho+a)/2\ge a\ge1$. Thus its rounded value is at least one,
and this property persists. When $a=0$, both unrounded coordinates equal
$\sqrt{b/2}$. If $b\ge2$, the first output is again at least one.
Only $(0,0)$ and $(0,1)$ can therefore enter the origin, and both do.
All remaining states must reach the other fixed point by Step 2.

For $M\ge1$, the two basin sizes are consequently $2$ and
$(M+1)^2-2$. This census is a direct consequence of the positivity split,
not an extra independent theorem axis.

### 4. Evaluated every-target inverse formula

Let $(u,v)\in X_M$. If $u<v$, its fibre is empty because every output
has ordered coordinates. Suppose $u\ge v$, and put $U=u+1$, $V=v+1$.
For each integer
$$0\le a\le A_*:=\min(M,U^2-1),$$
define the nonnegative integers
$$D_a=\max\{0,\;4u^2(u^2-a),\;4v^2(v^2+a)\},$$
$$E_a=\min\{M^2,\;4U^2(U^2-a)-1,\;4V^2(V^2+a)-1\}.$$
Here $E_a\ge0$: $U,V\ge1$ and $U^2-a\ge1$. Set
$\operatorname{csqrt}(d)=\lceil\sqrt d\rceil$ for $d\ge0$; this
equals $0$ at zero and $1+\operatorname{isqrt}(d-1)$ at positive integers.
Then
$$|T^{-1}(u,v)|=
\sum_{a=0}^{A_*}\max\{0,\operatorname{isqrt}(E_a)-
                                   \operatorname{csqrt}(D_a)+1\}.$$
This sum has no unknown recurrence coefficient, unspecified lattice-point
count or search over the second source coordinate.

To prove it, the lower real-coordinate condition $p\ge u$ requires
$\rho\ge2u^2-a$. If $a\ge u^2$, it is automatic and its displayed
squared lower bound is nonpositive. If $a<u^2$, the right side is
positive and squaring gives $b^2\ge4u^2(u^2-a)$. The lower imaginary
condition $q\ge v$ gives $\rho\ge2v^2+a\ge0$, equivalently
$b^2\ge4v^2(v^2+a)$. Combining them and $b\ge0$ gives $b^2\ge D_a$.

For the upper real condition $p<U$, one must have $a<U^2$, since
$p^2\ge a$. Under this necessary restriction, $2U^2-a>0$, so
$\rho<2U^2-a$ is equivalent to $b^2<4U^2(U^2-a)$.
The upper imaginary condition $q<V$ has positive right side $2V^2+a$
and is equivalent to $b^2<4V^2(V^2+a)$. Since $b$ is an integer,
these strict inequalities and $b\le M$ combine to $b^2\le E_a$.

Thus, at this fixed $a$, all and only valid second coordinates are the
integers in
$$[\operatorname{csqrt}(D_a),\operatorname{isqrt}(E_a)].$$
Their count is the nonnegative part in the formula. Distinct $a$ give
disjoint source pairs, proving the complete sum. At $(u,v)=(0,0)$ it
returns exactly two sources for $M\ge1$ and one for $M=0$, consistent
with Step 3. No maximizer conclusion follows from this check. ∎

## Counterexample to a tempting time shortcut

Hand substitution gives
$$T(0,2)=(1,1),\qquad T(1,1)=(1,0),\qquad T(2,0)=(1,0).$$
Therefore on the same $M=2$ square the imaginary-axis source has entrance
two, while the real-axis source has entrance one. The real-axis scalar
iteration is not the full-square worst-case clock. These are symbolic
checks, not a scientific execution or a sampled pilot.

## Subtraction and final disposition

The principal-root formula and ordinary radial shrinkage are established
elementary primitives. The full-target sum explicitly slices the square
of a unit quantization cell into integer intervals; evaluating that
ordinary one-dimensional window does not introduce a separate new inverse
mechanism. The actual old QRM rule is different, as documented in the
[source memo](SOURCE_AND_COLLISION.md); we do not use a false QRM identity
to reject FCSR.

There is no proved sharp full temporal result or a new independent
extremum here. The requested two-axis signal has not emerged, so this one
literal closes `NO_PROMOTION` without a pilot, larger cutoff, variant,
reserve, manuscript number or self-review. The elementary formulas remain
negative evidence. No PRE or other closed candidate is reopened.
