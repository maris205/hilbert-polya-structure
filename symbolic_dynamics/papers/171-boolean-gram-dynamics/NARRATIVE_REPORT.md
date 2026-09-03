# Narrative report — Boolean Gram closure

## Outcome first

The candidate survives only as an owner-thin exact note.  The mathematics is
closed and unusually transparent: one Boolean Gram step destroys the source's
orientation, and every later step is simply a squaring of the resulting
looped row-intersection graph.  That yields a logarithmic clock with a path
witness.  A different reading of the same columns yields a complete inverse
formula, including targets outside the image.

## Why the temporal statement is exact

For `G=AA^T`, symmetry gives `Gamma(G)=G^2`; induction doubles the Boolean
power at every subsequent time.  Because every active vertex of a Gram graph
has a loop, a path of length at most `r` can be padded to a walk of length
exactly `r`.  Hence the iterate at time `t` knows precisely which pairs have
distance at most `2^(t-1)`.  Stabilization is therefore not just bounded by a
diameter: its first time is the ceiling of the binary logarithm of that
diameter, with one initial Gram step.

The endpoint relation connects exactly the vertices in the same active
component.  These endpoints are partial equivalence relations, and conversely
every partial equivalence relation is Boolean symmetric-idempotent.  Thus the
functional graph has no nontrivial cycles.  Choosing active vertices and then
partitioning them gives the Bell transform `Bell(n+1)`.

## Why the inverse statement is separate

Write each source column by its support `C_r`.  The output is the union of the
squares `C_r x C_r`.  For a prescribed target, an allowed column is therefore
exactly an empty support or a fully looped clique.  The output is exact when
the ordered list of `n` columns covers each target loop and edge atom and
creates no forbidden atom.  Inclusion--exclusion over the missed atoms counts
all such ordered lists.

This formulation keeps details that are easy to lose in a graph-only
translation: diagonal loops are requirements; isolated looped vertices need
singleton columns; zero columns are legal; equal columns are legal; and the
columns retain their matrix labels.  The resulting formula returns zero both
for structurally invalid targets and for compatible targets whose loop-edge
cover number exceeds `n`.

## Hostile subtraction result

The gate found strong direct owners for nearly every ingredient:

- Fitting proves monotone growth of powers of `AA^T` over Boolean algebras and
  gives arbitrary-length strict examples.
- repeated Boolean squaring/transitive closure is classical;
- graph intersection representations and edge clique covers are classical;
- modern symmetric Boolean factorization explicitly studies `M=WW^T` and
  recovery of `W`.

Those sources prevent any claim that the two engines themselves are new.
However, the bounded search did not locate a source treating the literal
self-map as a finite functional graph with the exact source clock and sharp
carrier height, nor one coupling that temporal census to the complete
ordered-column fibre for every target.  The contract's direct-owner kill
switch was therefore not triggered, but the only defensible status is
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Internal collision result

The three closest portfolio systems are not relabelings or conjugates:

- P127 works over `F_2`, adds a parity outer product, has periods up to four,
  and solves fibres through margin equations.
- P143 maps rows to inclusion residuals, lands in preorders, and has a
  transpose phase with depth at most two.
- P163 is a complemented lower-shadow system on powerset families with
  Johnson-shell clocks.

They share Boolean, transpose, closure, or relation vocabulary but not the
literal update or either proof engine.  These distinctions are collision
control, not evidence of novelty.

## Evidence and lifecycle

The paper-local verifier checks 594,955 assertions.  It exhausts every source
and compatible or incompatible target through `n=4`, compares literal and
formula fibres, checks cover feasibility, tests the all-time identity for
four iterates, and verifies every clock and endpoint.  It separately runs the
sharp path family through `n=64` and all named boundaries.

This is an anonymous author Round-0 artifact.  It is not externally cleared
and contains no submission, release, novelty, or priority decision.
