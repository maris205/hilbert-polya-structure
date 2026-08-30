# Narrative report — P120

Status: **anonymous author draft / external HOLD**.

## Technical story

A plane rooted tree carries a child list at every vertex.  P120 reads the
order of every fringe subtree in the old tree and reverses exactly those
child lists whose fringe order is odd.  Reordering children changes no
fringe order, so the same local trigger set survives the update.  Each local
reversal has order two and the reversals commute, which makes the global map
an involution.

The fixed set is less automatic.  At an even-order root there is no root
reversal, so every child must itself be fixed.  At an odd-order root the
child tuple must agree with the reverse of its componentwise image.  The
children therefore form a twisted palindrome: arbitrary off-centre trees
occur in pairs `(T,M(T))`, and an optional central tree must be fixed.  Root
parity forces that central tree to have even order.

This local criterion yields exact enumeration.  If `E` and `O` mark fixed
trees of even and odd order and `A` is the ordinary plane-tree series, an
even root takes the odd-order part of a sequence of fixed children, while an
odd root takes a sequence of arbitrary twisted pairs and possibly one even
fixed centre.  The result is

```text
E = x O / ((1-E)^2-O^2),
O = x (1+E) / (1-A(x^2)).
```

Writing `F=E+O`, `G=E-O`, and `B=A(x^2)` reduces the system to two rational
identities plus `B^2-B+x^2=0`.  Direct elimination produces an explicit
degree-six polynomial for `F`; `P_y(0,0)=-3` selects the unique
zero-constant branch in `Q[[x]]`.  A sparse exact control independently
reconstructs the full resultant `4*x^2*P`.  This is the algebraic gate
required for promotion.  No singularity analysis or asymptotic claim is
included.

Since the map is an involution, the fixed coefficients already determine
the entire finite dynamics at each order: all remaining trees form
two-cycles.  The iterate-fixed counts alternate by time parity, and the zeta
function is the corresponding product of `(1-z)` and `(1-z^2)` factors.

## Early separating objects

Write a tree as a tuple of its root's children and write `()` for a leaf.
The order-four tree `((),((),))` is fixed by P120 but not by global mirror.
At order nine,

```text
(((),((),)),(((),),()))
```

is fixed by global mirror but not by P120.  Thus the two fixed sets are
incomparable.  The 2026 Catalan involution `h` is also nonliteral: on plane
trees it sends the three-leaf star to a depth-three path, whereas P120
preserves the complete parent--child relation and fixes that star.  Its
published Catalan size is edge count; after translating to the present
vertex order, its fixed counts at orders four and six are 1 and 2, compared
with P120 counts 5 and 36.  This is a count separation, not the false parity
separation that would result from mixing the two size conventions.

## Owner subtraction

Plane-tree mirror symmetry, Catalan enumeration, parity extraction,
context-free generating functions, resultant elimination, involution cycle
bookkeeping, and dynamical zeta functions are all mature tools and receive
zero contribution credit.  Direct external neighbors include the
Chen--Shapiro--Yang parity-reversing involution, Deutsch's ordered-tree
bijection, Li--Lin--Zhao's binary/plane-tree involutions, the 2026 abstract
Catalan involution `h`, and recent plane-tree cyclic-sieving actions.  Each
changes a different object feature or uses a different literal action.

The bounded search through 2026 found no source stating the odd-fringe
trigger together with its fixed grammar and finite cycle census.  Search
absence is not a novelty or priority certificate.  The residual scope is
only that exact map-specific conjunction.

## P114 firewall

P114 deletes all eligible nonroot leaves, changes the vertex set, absorbs to
an edgeless rooted forest, measures depth by height, and counts Cayley
basins/fibres.  P120 never deletes or reparents a vertex, stays within one
fixed Catalan set, and has no transient state because every orbit has period
one or two.  The carriers, updates, clocks, enumerations, and recurrent
objects are different object by object.

## Boundary and nonclaims

The empty lane is adjoined separately as a singleton identity with
`a_0=f_0=1`.  The one-vertex tree is also fixed.  The ordinary generating
functions start at order one, so no empty-tree constant is silently inserted
into `A`, `E`, `O`, or `F`.

The manuscript makes no asymptotic, irreducibility, minimal-polynomial,
priority, owner-clearance, or broad Catalan-action claim.  External posting,
submission, and specialist contact remain **HOLD**.
