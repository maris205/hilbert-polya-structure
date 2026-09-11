# Replacement theorem-spike gate

## Outcome

There is **no surviving theorem spike** and no paper allocation.  RX01 passed
the complete internal and exact-mechanical gate, but the bounded owner check
found a direct literal algorithmic owner.  RX03 showed a second clean finite
pattern, but the P132--P136 internal ledger already kills its centre-descent
engine.  The derivations are retained below to make the negative decision
auditable rather than silently discarding the signals.

## Rejected spike RX01 — least-antipode rerooting

Let `T` be a labelled tree and

`F_T(r)=min argmax_v d_T(r,v)`.

For `|T|>1`, let `a` be the least-labelled peripheral vertex, and let `b` be
the least-labelled vertex at diameter distance from `a`.  The exact pilot
supports the following uniform package for every labelled tree, not merely
paths or generic trees.

### Candidate all-time theorem

For every vertex `r`,

`F_T(r)=a` if `d_T(r,a)>=d_T(r,b)`, and `F_T(r)=b` otherwise.

Consequently `F_T(a)=b`, `F_T(b)=a`, the image is exactly `{a,b}`, and every
root is recurrent or enters the unique 2-cycle in one step.  For `t>=1`, if
`z=F_T(r)`, then

`F_T^t(r)=z` for odd `t`, and `F_T^t(r)=F_T(z)` for even `t`.

The singleton tree is the sole fixed boundary case.

### Candidate every-target inverse theorem

Only `a` and `b` have nonempty fibres, and

```text
F_T^{-1}(a)={r:d_T(r,a)>=d_T(r,b)},
F_T^{-1}(b)={r:d_T(r,a)< d_T(r,b)}.
```

These are exact tree metric halfspaces.  If the diameter is odd, deleting its
central edge produces the two fibres (the component containing `b` maps to
`a`).  If the diameter is even with centre `c`, delete the first diameter
edge from `c` toward `a`; that strict `a`-branch is the fibre of `b`, while
its complement, including `c`, is the fibre of `a`.  This covers every target,
including empty fibres.

### Candidate spectral corollary

The deterministic transition matrix on the `n` possible roots of a fixed
nontrivial tree has characteristic polynomial

`x^(n-2)(x-1)(x+1)`.

Indeed its functional graph has one directed 2-cycle and every other state
has depth one.  Across all `n^(n-2)` labelled trees, the eigenvalues `1` and
`-1` would each have multiplicity `n^(n-2)`, and zero would have multiplicity
`(n-2)n^(n-2)`.

### Uniform proof route that was available

Perturb each label by a distinct infinitesimal pendant length chosen so that
smaller labels win distance ties.  The standard two-sweep diameter theorem on
the perturbed tree produces the same canonical endpoints `a,b`.  The tree
diameter identity

`ecc_T(r)=max(d_T(r,a),d_T(r,b))`

then gives the two-target decoder.  Distance difference along the unique
`a`--`b` path is monotone and is constant on every component hung from a path
vertex, so its strict/weak sign gives the central-edge or central-vertex fibre
cut.  The orbit and spectrum follow immediately.

### Why the spike is killed

The official AtCoder ABC428 E task asks for this same map at **every** vertex,
using the largest rather than smallest label for ties.  Reversing all labels
conjugates that rule to RX01.  More decisively, the official editorial already
uses an infinitesimal label perturbation and the fact that a fixed diameter
pair contains a farthest vertex for every root.  Thus the proof route and the
two-target decoder above are directly present.  Once that is subtracted, the
one-step entry, centre-cut fibres, and rank-two spectrum are immediate
read-offs and do not form a sufficiently independent residual theorem.

Decision: **`KILL_DIRECT_OWNER`**.

## Rejected spike RX03 — antipodal geodesic pursuit

The update moves the root one edge toward its least farthest vertex.  The
pilot finds only a 2-cycle for every nontrivial labelled tree through seven
vertices and global maximum depths `floor((n-1)/2)`.

The apparent theorem has a short uniform route.  If the tree has a central
edge, every noncentral vertex moves one step toward that edge and its endpoints
swap.  If it has a single centre `c`, every noncentral vertex moves one step
toward `c`; the centre moves to the neighbour `q` on the path to its least
peripheral vertex, and `q` moves back to `c`.  Hence the unique recurrent edge
is the central edge in the bicentral case and `{c,q}` in the unicentral case.
Every-target fibres are the outward children of a target, with the appropriate
recurrent-edge neighbour added at its two endpoints.

This does not survive internal subtraction.  The earlier `TR3` candidate is
the literal “move to a least-labelled neighbour of strictly smaller
eccentricity” centre descent and was permanently killed as direct.  RX03 is
that same map away from the centre, with one centre arrow redirected to create
a 2-cycle.  The extra boundary arrow supplies no independent mechanism.

Decision: **`KILL_INTERNAL_DIRECT`**.

## Boundary

The theorem statements above are rejected derivations, not claims reserved
for P187--P191.  The exact pilot is counterexample pressure only.  The owner
search is bounded, and neither its hits nor its non-hits establish a global
literature theorem.
