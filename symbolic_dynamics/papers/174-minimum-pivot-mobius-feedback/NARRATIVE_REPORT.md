# P174 narrative report: minimum-pivot Möbius feedback

**Round:** anonymous final Round 2; dual hostile reviews closed  
**Decision:** `PROVISIONAL_AMBER / HOLD_EXTERNAL`  
**Paper type:** finite-dynamics AMS short note

## One-sentence contribution

For a `k`-subset of `P^1(F_p)`, translate by its least finite point and
invert; the resulting state-dependent map has an exact two-level image
tower, an inversion core, and an every-target inverse whose admissible
pivots form a target-dependent initial interval.

## The technical story

Fix a prime `p` and `2 <= k <= p`.  Order the finite representatives as
`0<1<...<p-1<infinity`.  If `a(S)` is the least finite point of a state
`S`, update every point by

```text
x -> 1/(x-a(S)).
```

The selected pivot always becomes infinity.  If infinity was already
present, it becomes zero.  Those two observations give the complete temporal
spine:

```text
all k-subsets -> subsets containing infinity
              -> subsets containing {0,infinity}.
```

The second image is recurrent.  There the pivot is zero, so the map is the
ordinary inversion involution on `F_p^*`.  Hence `M^4=M^2`; the tail layers
are exactly

```text
C(p-1,k-2), C(p-1,k-1), C(p,k)
```

at depths zero, one, and two.  Fixed recurrent states are the inversion-
invariant `(k-2)`-subsets of `F_p^*`, counted for odd `p` by

```text
[u^(k-2)] (1+u)^2 (1+u^2)^((p-3)/2).
```

All other recurrent states form two-cycles.  The smallest parameter
`(p,k)=(2,2)` is a three-vertex chain of depths `2,1,0` ending in a fixed
state, so no odd-prime shorthand is used at that boundary.

## The inverse axis

Every image contains infinity, which settles all zero fibres.  For a target
`R` containing infinity, set

```text
b(R) = max{ the integer representative of y^(-1) :
            y in R intersect F_p^* },   max(empty)=0,
h(R) = p-b(R).
```

A source with proposed pivot `a` is forced by projective inversion.  Its
finite points other than `a` are `a+y^(-1) mod p`.  The pivot condition is
equivalent to absence of modular wraparound, so precisely

```text
a = 0,1,...,h(R)-1
```

are valid.  Thus the fibre size is `h(R)` and its pivot enumerator is
`1+z+...+z^(h(R)-1)`.  This target-sensitive interval is the only part of the
package not already removed by the internal architecture firewall.  It also
gives the fibre distribution

```text
#{R : |M^(-1)(R)|=h} = C(p-h,k-2),  1<=h<=p,
```

and the maximum fibre `p-k+2`.

## Owner and internal subtraction

Fixed fractional-linear dynamics, projective configuration orbits, and the
`PGL(2,q)` action on projective-line subsets are cited background and receive
zero credit.  Ordered minimal/canonical images and canonizing elements are
also explicitly subtracted: P174 neither minimizes over a group nor remains
constant on group orbits.  A bounded search did not locate the literal
state-dependent map, but that non-hit is not evidence of novelty, priority,
ownership, or freedom to operate.

Three internal neighbours are also subtracted explicitly.

- P96 already studies finite subsets under a map induced from a fixed base
  transformation.  P174's transformation is selected from the current
  subset, but fixed-map hyperspace language is not a contribution.
- P168 already studies inverse-span dynamics on finite-field subspaces.
  P174 takes no span, and none of P168's Gaussian/inverse-subspace machinery
  proves the modular pivot interval; inversion itself remains zero credit.
- The killed AQN control shows that “select a group element from the state,
  normalize to a section, then expose a classical action” is not a
  paper-sized claim.  P174 therefore claims only the literal containment
  tower plus the nonuniform target-local pivot law.

The clock is shallow and the coordinate order is artificial.  A specialist
owner or a general adaptive-section theorem may still kill the residual.
After both hostile reviews, the correct final status is still
`PROVISIONAL_AMBER / HOLD_EXTERNAL`, not green.

## Evidence package

The proof is uniform in every prime and every `2<=k<=p`.  Independently,
`verify_p174.py` exhausts all 69 parameter boxes for
`p in {2,3,5,7,11,13,17,19}` and every allowed `k`.  It rebuilds every edge,
orbit, image, target fibre, pivot set, fibre distribution, fixed count, and
boundary case without importing scouting code.  Its canonical run contains
131,018,555 assertions.  Review A adds 161,536 assertions and Review B adds
4,755,152, with every finding closed.  Computation is falsification evidence,
not a replacement for the proof.
