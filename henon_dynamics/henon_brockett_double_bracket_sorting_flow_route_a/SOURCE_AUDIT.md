# C185 source audit

## Locked source

R. W. Brockett, “Dynamical systems that sort lists, diagonalize matrices, and
solve linear programming problems,” *Linear Algebra and its Applications* 146
(1991), 79–91. DOI:
[10.1016/0024-3795(91)90021-N](https://doi.org/10.1016/0024-3795(91)90021-N).

The publisher metadata fixes the author, title, journal, volume, pages, year,
and DOI.  The publisher abstract explicitly identifies the equation
`dH/dt=[H,[H,N]]`, its gradient-flow interpretation, and its sorting,
diagonalization, and optimization roles.

## Attribution boundary

The following are classical and are not claimed as new:

- the double-bracket equation and orthogonal-orbit setting;
- its normal-metric gradient interpretation;
- the use of the flow to sort lists and diagonalize symmetric matrices;
- the corresponding convergence framework for generic simple data.

The package contributes an artifact-level synthesis, not a mathematical
priority claim: it writes one proof ledger covering all `n`, resolves every
pair-mode sign by the inversion number, supplies exact finite regression and
independent reconstruction, freezes the repeated-spectrum boundary, and
applies the Route-A v0.2 arithmetic gate.

## Claim-to-source audit

| Claim | Status | Ownership |
|---|---|---|
| double-bracket sorting/diagonalization flow | classical | Brockett 1991 |
| gradient and isospectral mechanisms | classical | Brockett framework; rederived here |
| all-size pair-mode/Morse ledger | proved in package | synthesis of classical consequences; no priority claim |
| exact `n<=7` regression and repaired-hash audit | computed in package | validation artifact |
| strict Route-A rejection | package evaluation | not a statement in the classical source |

The source registry population is exactly one.  This is a source lock, not a
novelty survey.  No claim is made that one citation exhausts later work on
double-bracket flows.

## Forbidden promotion audit

Neither Brockett’s terminology nor the Lax form supplies rational-prime
semantics.  The package does not turn a local tangent characteristic
polynomial into a global dynamical determinant, does not interpret the
state-dependent skew generator as a fixed quantum Hamiltonian, and does not
invoke arithmetic local data, Euler factors, root numbers, automorphy,
Hilbert--Polya, or Route B.
