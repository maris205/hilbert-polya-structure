# C193 theorem package

## 1. Frozen equation and maps

Write

\[
 P(x,y,z)=x^2+y^2+z^2-3xyz.
\]

For each coordinate, the Vieta transformation replaces it by the other root;
for example

\[
 R_z(x,y,z)=(x,y,3xy-z).
\]

A **normalized Markoff triple** is a positive integral zero of `P` with
`x<=y<=z`.  Coordinate permutations are quotient symmetries.  The root is
`r=(1,1,1)`.

## 2. Algebraic invariance

Direct expansion gives

\[
 P(x,y,3xy-z)=P(x,y,z),\qquad R_z^2=\mathrm{id}.
\]

Viewing `P=0` as a quadratic in `z`, its two roots are `z` and
`z'=3xy-z`, with

\[
 z+z'=3xy,\qquad zz'=x^2+y^2.
\]

Thus `z'>0` for every positive solution.  The other coordinate involutions
follow by symmetry.

## 3. Unique parent and strict descent

### Lemma 1 (unique maximum)

Every normalized positive solution other than `(1,1,1)` has `y<z`.

**Proof.**  If `y=z`, the equation becomes

\[
 (3x-2)y^2=x^2.
\]

For `x>=2`, the right side divided by `3x-2` is smaller than `x`, whereas
`y^2>=x^2`; this is impossible.  For `x=1`, the equation gives `y=1`, hence
the root.  Therefore every non-root maximum is unique.  ∎

### Lemma 2 (lower Vieta root)

For a non-root triple, `0<z'<=y<z`.

**Proof.**  Positivity follows from `zz'=x^2+y^2`.  Let

\[
 q(t)=t^2-3xyt+x^2+y^2.
\]

Then

\[
 q(y)=x^2-(3x-2)y^2\le0.
\]

For `x=1` this is `1-y^2<=0`; for `x>=2`, use `y>=x` and
`3x-2>1`.  Since the upward-opening quadratic has roots `z'` and `z`, and
`y<=z`, the inequality places `y` between them.  Lemma 1 makes the last
inequality strict.  ∎

Define the autonomous descent

\[
 D(x,y,z)=\operatorname{sort}(x,y,3xy-z)
\]

away from the root, and fix the root.  Lemma 2 proves that the integer height
`h=max(x,y,z)` strictly decreases at every non-root step.

### Lemma 3 (every other Vieta edge ascends)

Before sorting, replacing either nonmaximal coordinate gives

\[
 3yz-x>z,\qquad 3xz-y>z.
\]

Indeed, `z(3y-1)-x >= 2z-x>0` and
`z(3x-1)-y >= 2z-y>0`, since `x,y>=1` and `z>=y>=x`.
Both replacements remain positive Markoff solutions by polynomial
invariance.  Consequently every labelled Vieta edge, after passing to the
permutation quotient, is either the unique descending parent edge or an
ascending child edge.  No lateral edge is omitted from the tree.

## 4. Global tree theorem

### Theorem 3 (all positive solutions)

Every normalized positive Markoff triple reaches `(1,1,1)` after finitely
many applications of `D`.  Reversing these edges generates every positive
solution.  Each non-root vertex has exactly one parent, so the normalized
positive-solution graph is a rooted tree.

**Proof.**  Strict decrease of the positive integer height forces finite
termination.  The only possible terminal normalized solution is the root:
otherwise Lemma 2 supplies another smaller parent.  The source-locked Markoff
orbit theorem says every positive solution belongs to the Vieta/permutation
orbit of the root; equivalently the reversed descent edges exhaust the
positive solutions.  Lemma 1 makes the descending coordinate unique, hence
the parent is unique; Lemma 3 proves that every remaining Vieta edge is an
ascending child edge.  A connected graph in which every non-root vertex has a
unique parent and height decreases toward the root contains no cycle.  ∎

The first two exceptional branch levels have repeated coordinate mutations:
after quotienting permutations, the root has the single child `(1,1,2)` and
that node the single child `(1,2,5)`.  This does not affect unique parenthood.

## 5. Dynamical and arithmetic boundary

The autonomous descent has no non-root periodic orbit because height strictly
decreases.  This does not contradict involutivity of the labelled coordinate
maps `R_x`, `R_y`, `R_z` before sorting and permutation quotient; the
autonomous map chooses a state-dependent generator and an orientation.

The integer surface and Vieta maps give genuine intrinsic Diophantine
structure, warranting `A0_WEAK_ARITHMETIC_RELATION`.  They do not identify
rational primes as primitive orbits, prime powers as repetitions, or `log p`
as a clock.  A tree adjacency operator would be a formal post hoc choice and
no target divisor or analytic normalization is present.  Therefore

```text
(A0,A1,A2,A3,A4)=(WEAK_ARITHMETIC_RELATION,FAIL,FAIL,FAIL,FORMAL_HINT)
overall ROUTE_A_REJECTED
Route B false
scope NO_BAD_EULER_OR_ROOT_NUMBER
```

The theorem does **not** prove that the largest Markoff coordinate determines
the remaining two coordinates.  That Frobenius uniqueness problem remains
open and is logically unnecessary here.  Mod-prime Markoff graphs and strong
approximation are also outside scope.
