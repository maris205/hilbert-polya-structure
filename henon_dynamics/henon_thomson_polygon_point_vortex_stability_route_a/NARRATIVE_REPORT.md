# Narrative report — HCS-C284

## One-sentence result

The equal positive point-vortex regular polygon has a raw-Hessian DFT block
`c*diag(2(N-1)-m(N-m),m(N-m))`, which closes the complete reduced linear
stability threshold: elliptic through six vortices, linearly degenerate only
in heptagon modes three and four, and hyperbolic from eight onward.

## Why this package is a full step

The theorem is not a finite list of spectra.  It begins with the logarithmic
Hamiltonian and one fixed sign convention, derives the angular velocity,
builds the rotating-frame Cartesian Hessian, moves to vertexwise radial and
tangential frames, evaluates the DFT by a root-of-unity identity, and then
handles the Euclidean and scale directions before classifying shape modes.
The argument works for every integer `N>=3` and records every parameter face.

The executable side follows a genuinely different route.  Its producer emits
the closed integer oracle.  Its checker reconstructs all raw `2N by 2N`
Hessians for `N=3..64`; it never imports a producer function or trusts the
reported Fourier blocks.  Exact SymPy cells and hostile mutations target the
same convention from two additional directions.  The checker also treats the
receipt as a strict contract: duplicate, unknown, missing, wrongly typed,
reordered, or semantically duplicated content is rejected even after its
payload hash is repaired.

## Main boundary

At `N=7`, the two conjugate shape blocks are nonzero nilpotent matrices.  This
is a linear degeneracy.  The package neither proves nor claims nonlinear
stability.  Later nonlinear literature is cited precisely so that a reader
cannot mistake the scope.

Likewise, the `m=0` Jordan block is the rotation/scale family and the first
harmonic contains translations.  These directions are identified before the
reduced spectrum is called stable or unstable.

## Evidence summary

- 2,077 exact mode cells;
- 62 complete polygon rows;
- 64 exact circulation/radius scale cells;
- seven exact symmetry-slice rows;
- eight named boundary cells;
- 65,655 checker assertions from raw Hessians and explicit slice vectors;
- 4,585 exact symbolic identities;
- two independent fresh byte replays;
- 76/76 hostile mutations rejected.

The finite domain is an implementation audit, not the proof of the theorem.
The all-`N` proof is the exact root sum

`sum (1-cos(m*theta_k))/(1-cos(theta_k))=m*(N-m)`

and the maximum `floor(N^2/4)`.

## Ownership and Route-A outcome

The polygon stability problem is classical, with Thomson and Havelock as
direct historical owners and later authoritative work explicitly cited.  The
package does not claim literature originality.  Its contribution is the
repository-local, convention-frozen theorem/evidence/release closure.

Natural relative periodic motion merits only `A1_WEAK`: one continuously
scaled symmetric family is not an isolated primitive-orbit ledger.  All other
coordinates fail.  The result is `ROUTE_A_REJECTED`; Route B remains locked;
the scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
