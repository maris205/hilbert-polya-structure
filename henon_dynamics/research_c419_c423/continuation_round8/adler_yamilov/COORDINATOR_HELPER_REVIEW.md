# AY8 coordinator nonauthor helper review

2026-09-08 UTC. Internal model review, not human peer review.
The coordinator read the complete 408-line [proof](PROOF_PACKAGE.md),
[source audit](SOURCE_AUDIT.md), frozen diagnostic protocol, entire
implementation, and [execution receipt](DIAGNOSTIC_RECEIPT.md).
The mathematical reconstruction below does not use the finite counts.

## Verdict

**PASS for the global ordinary rational native-period helper.**
For nonzero integer $k$, every nonzero ordinary rational periodic
state has $N=m$ or $2m$ with
$m\in\{3,4,5,6,7,8,9,10,12\}$, hence $N\le24$.
The origin and inherited $k=0$ pair-swap case are handled separately.
No mandatory mathematical correction was found.

**Original AY7 integral structural atlas: NOT CLOSED.**
This helper does not identify every integral family, decide all
admissible divisibility/scaling strata, or prove that every listed
possible period occurs. Known QRT reduction and Mazur torsion own
the main general mechanisms. A helper PASS is not paper admission.

## 1. Product quotient and cubic checked by hand

Writing $x=ps$, $y=rq$, $z=pq$, $w=rs$ gives
$xy=zw$, $z+w=I$ and $J=DE-1+kw$.
I independently recovered
$w=(C-DE)/k$, $z=(DE-L)/k$ and
$$D^2E^2-aDE-k^2(D+E)+e=0.$$
Substitution in the native update gives
$D'=a/D+k^2/D^2-E$, $E'=D$. Only $k,D$ are divided out;
zero individual coordinates remain in scope.

The square completion is exactly
$$
(2D^2E-aD-k^2)^2
=4k^2D^3+(a^2-4e)D^2+2ak^2D+k^4.
$$
Thus the stated Weierstrass cubic, inverse birational formula and
coefficient $a/2$ are correct. Its monic odd-degree right side is
not a square even over the algebraic-closure rational function
field, so the singular cases are irreducible as claimed.

For the point $P=(0,k/2)$, the chord slope
$(Y-k/2)/X$ gives
$X(Q+P)=a/(2X)+k^2/(2X^2)-kY/X^2$.
Using the inverse cubic formula recovers exactly $D'$.
The reflected intersection ordinate agrees with the updated pair
$(D',D)$. In particular the native step is addition by $P$,
not $2P$ or its negative. The ordinary conditions retain $X,D'\ne0$.

## 2. Smooth and singular periodicity

On a smooth cubic, periodicity is equivalent to torsion of the
rational point $P$ by cancellation in the group. $P\ne O$ and
$P\ne-P$ exclude orders one and two.
The exact rational torsion list was checked in the author-primary
[Balakrishnan–Mazur exposition, section 1.4](https://arxiv.org/pdf/2307.04752);
its group list yields precisely the asserted possible element orders.
This is a stated external classical input, not a new proof of Mazur.
The inaccessible original 1977 PDF is not claimed as read.

A singular monic cubic has a unique repeated root, rational by
Galois invariance, and that root is nonzero since $k\ne0$.
For a node, the displayed parameterization reduces the chord
relation to the equality of the line polynomial at $d$ and $-d$.
Its resulting multiplicative parameter lies in a field of degree
at most two. Rational torsion is therefore restricted by
$\varphi(j)\le2$, with only $3,4,6$ remaining after the same
identity/inverse exclusions. This includes nonsplit nodes.

For a cusp, reciprocal normalization parameter gives the additive
law. The nonzero parameter of $P$ has infinite additive order.
The unique singular point lies outside either smooth group:
$f(r)=f'(r)=0$ gives $2r^3=ar+k^2$, so its quotient is
$(D,E)=(r,r)$ and is fixed. It has not been discarded by applying
a smooth-fibre theorem beyond its domain.

## 3. Exceptional quotients and the native lift

With constant nonzero $h$, the recurrence matrix has distinct real
eigenvalues, neither $1$ nor $-1$. No positive power can have an
eigenvalue one. Periodicity forces the first channel zero, then
the second, yielding only the origin. This excludes all quotient
fixed points, including the singular one.
A quotient two-cycle with values $u,v$ forces
$2uv-k^2/u=2uv-k^2/v$, hence $u=v$.

The product matrix factorization is zero-safe. If it vanishes,
one channel is identically zero and $D_n=1$.
The cyclic sum of
$s_n(s_{n+1}-s_{n-1})=ks_n^2$, or the first-channel version,
forces the other channel zero over the reals.
Thus every nonzero rational periodic state lies over a nonzero
rank-one product matrix at every time.

For such a matrix, rational factorizations differ by exactly one
nonzero rational scaling factor. The scaling action is free and
commutes with the native map, including zero entries. Returning
the quotient after $m$ steps therefore multiplies the factor by
$t\in\mathbb Q^*$; an actual period forces $t$ to be a rational
root of unity. The alternatives $t=1,-1$ give exactly $N=m,2m$.
No assumption that torsion downstairs automatically closes the
upstairs orbit has entered the proof.

## 4. Hand controls and diagnostic scope

I independently substituted the universal six-cycle family:
the denominators are $-k,k,1$ and three updates give the negative
of the initial nonzero state. Periods one/two are excluded directly
by the scalar recurrence, and period three is excluded by that
negative sign. The $k=\pm1$ zero coordinates remain valid.
The $k=4$ four-step half-orbit has denominator sequence
$4,1,4,-2$, gives $-v$, and has quotient least period four.
The parameter-sign conjugacy gives the $k=-4$ control.

The diagnostic's actual emitted twelve JSON rows agree with its
receipt table, including the displayed $k=2$ witness. I read the
integer graph implementation: it enforces both native current
denominators, exact divisibility, target box/domain membership,
and extracts directed cycles with no period cutoff. This is a
source/output consistency check, **not** an independently executed
reconstruction of its finite census.

The sole diagnostic execution remains the author's one run.
The review executed no mathematical program and did not consume
another allowance. Its global proof PASS is independent of every
count in the table; the explicit witnesses were replayed by hand.

## 5. Source ownership and final limitations

The coordinator read the relevant body of
[Fordy–Kassotakis, Example 3.3](https://arxiv.org/pdf/1301.1927),
including the map, invariants, quotient and scalar lift. This
confirms ownership of the broad reduction mechanism.
Its extracted reduced-coordinate formula has the stated sign
discrepancy at the explicit test state; this review did not visually
attest the printed page and does not upgrade it to a printed erratum.
The author proof is derived from the original map, not that component.

No worldwide novelty clearance or full-paper source reading is
claimed. The current-team research-review fallback was used;
no external GPT-5.4 review or paid API ran. No old mathematical/build
rerun, manuscript, PDF, formal evaluation or Git write was performed.
The batch skill retains the complete atlas gate and
NO_BAD_EULER_OR_ROOT_NUMBER. This review closes only the helper gate.
