# Coordinator scout — odd-degree Seidel-switch feedback

**Date:** 2026-09-03 UTC  
**Candidate state:** `GREEN_OWNER_THIN / NOT YET ALLOCATED`  
**External state:** `HOLD_EXTERNAL`.

## Literal system and exact signal

On labelled simple graphs `G` on `[n]`, let `O(G)` be the even-cardinality
set of odd-degree vertices.  Define

```text
Psi_n(G) = the Seidel switch of G across O(G),
```

so precisely the edges with one endpoint in `O(G)` are toggled.  The first
exact pilot found an immediate parity bifurcation:

- odd `n`: `Psi_n` is an idempotent projection onto the Eulerian graphs;
- even `n`: `Psi_n` is an involution, fixed exactly on graphs whose degree
  parities are all equal;
- odd `n`: every Eulerian target has exactly `2^(n-1)` predecessors and every
  non-Eulerian target has none;
- even `n`: every target has its unique predecessor; and
- for an odd-order Eulerian target, even vertex subsets parameterize all
  predecessors and give a target-sensitive exact edge enumerator.

The verifier exhausts every labelled graph through `n=6`, every target and
time `0..4`, fixed iterates through time six, and every marked fibre through
`n=5`.  It adds deterministic random attacks through `n=25` and linearity
checks through `n=17`.  It records 550,448 exact assertions.

## Uniform derivation

Write a graph as `x in F_2^E` and let `B:F_2^E -> F_2^n` be the unoriented
incidence map.  Then `d=Bx` is the degree-parity vector and

```text
Psi_n(x) = x + B^T Bx.
```

For the complete labelled edge carrier,

```text
B B^T = J + (n mod 2) I.
```

Every degree vector has even coordinate sum, hence `Jd=0`.  Therefore the
new degree vector is zero for odd `n` and remains `d` for even `n`.  This
simultaneously proves idempotence/involution and the complete temporal graph.

For odd `n`, the fixed space is `ker B`, of dimension `C(n,2)-n+1`; every
switching class has one such target and size `2^(n-1)`.  For even `n`,
`B^T d=0` iff `d` is zero or all-one, so the fixed count is
`2^(C(n,2)-n+2)`.  The exceptional small carriers are explicit: height zero
at `n=1`; at `n=2` both graphs are fixed; odd `n>=3` has sharp preperiod one;
and even `n>=4` has both periods one and two.

Consequently, with `m=C(n,2)`, the finite-map zeta factors are

```text
odd n:  (1-z)^(-2^(m-n+1));
even n: (1-z)^(-F) (1-z^2)^(-(2^m-F)/2),
        F=2^(m-n+2),
```

with the evident `n=1` interpretation.

For odd `n` and Eulerian target `H`, choose the unique even representative
`D` of each complementary pair of vertex sets.  Then all predecessors are
`H triangle delta(D)`, and their edge-count polynomial is

```text
sum_(D subseteq [n], |D| even)
  u^( |E(H)| + |D|(n-|D|) - 2 e_H(D,D^c) ).
```

Thus the inverse axis is every-target and target-sensitive, not merely the
constant unmarked fibre size.

## Owner subtraction

Seidel switching, switching classes, their `2^(n-1)` labelled size, and the
Euler-graph representative/counting correspondence are classical and receive
zero contribution credit.  The strongest primary record found is Mallows and
Sloane, “Two-Graphs, Switching Classes and Euler Graphs are Equal in Number,”
*SIAM Journal on Applied Mathematics* 28(4), 876–880 (1975), DOI
`10.1137/0128070`.  The title-level and mechanism-level search found no source
formulating iteration of the degree-selected feedback map together with its
even-order involution and every-target marked predecessor law.  That bounded
non-hit is not novelty or ownership clearance.

The retained candidate residual is therefore narrow: the literal autonomous
choice of the switching set from the current degree signature, the odd/even
functional-graph bifurcation, the exact small-carrier boundaries, and the
target-sensitive marked inverse polynomial.  A direct owner for that
conjunction kills the candidate.

## Internal collision pressure

- P123 complements odd connected components rather than a degree-determined
  cut; its component dynamics does not transfer the incidence-matrix proof.
- P145 randomly pushes orientations at a chosen vertex; it is a Markov chain
  on orientations, not deterministic cut switching on simple graphs.
- P112 reverses tournament upsets and P138 uses word-prefix XOR; neither has
  the cut/cycle-space projection or degree-signature involution.
- P171's graph square appears after Boolean Gram formation and closes graph
  distances.  It neither switches edges nor preserves switching classes.

## Current decision

The signal is exact, sharp, uniform, and two-axis, so the system survives the
coordinator scout as `GREEN_OWNER_THIN`.  It is not allocated a paper number
until the parallel lanes and a direct hostile owner gate are compared.

## Deterministic replay receipt

Two fresh bytecode-disabled executions made after the canonical run both
matched `CANONICAL.txt` byte for byte.  All three transcripts have SHA-256

```text
5a1042ebf5581f3d6175ae9e61cb7df63f5046886b9d438461e6b8b865166247.
```

The transcript's internal payload digest is
`a8846c185af8883f0b7f1ba4fe8544b15b60b86a8ad0bc76d4c9cf3a65f017ca`.
This replay establishes deterministic implementation consistency only; it is
not proof, novelty evidence, or owner clearance.
