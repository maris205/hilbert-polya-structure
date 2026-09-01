# Paper improvement log

## Round 0 — owner and Markov core

The original draft froze the character multiplier, counted conductor shells,
and supplied the conditional-expectation reconstruction.  Its central proof
was the telescoping positive-generator formula.  It did not yet claim the
zeta, determinant, sharp scale endpoints, or boundary atlas.

## Round 1 — sharp analytic thresholds

The second draft added compact resolvent, positive-time heat trace, exact
staircase counting, liminf/limsup discrete-scale oscillation, the locally
uniform log-periodic heat profile, and the if-and-only-if resolvent Schatten
threshold including equality divergence.  It also separated heat-semigroup
membership in every \(\mathcal S_q\) from resolvent membership.

## Round 2 — complete meromorphic and hostile closure

The final draft added the full vertical pole lattice and common residue,
\(\zeta(0)\), \(\zeta'(0)\), the primed determinant, and explicit
\(\alpha=0\), \(\mu=0\), \(t=0\), \(\alpha\to\infty\), and \(p=2\)
faces.  It clarified that \(\alpha\downarrow0\) is strong but not norm
convergence, added finite-quotient DFT evidence, and made the composite-
branching proves-too-much obstruction and A0-weak ceiling explicit.

All three revisions are compiled from one conditional source.  Each revision
was built twice in fresh directories with the fixed epoch; replicas were
byte-identical, the three archived revision hashes were distinct, and the
final `main.pdf` is exactly round 2.

## Independent direct-owner repair

A hostile source review found that Example 5.1 of
Chacón-Cortés--Zúñiga-Galindo is not merely nearby: at dimension one it already
prints the same positive shell spectrum, multiplicities, geometric zeta, and
vertical pole lattice.  The final source audit and manuscript now state that
identity explicitly and assign those formulas zero originality credit.  The
retained value is the integrated zero-mode/Markov reconstruction,
scale/Schatten/determinant/boundary closure, independent DFT certificate, and
strict Route-A obstruction.  The release gate now requires the Example 5.1
and arXiv:1511.02146 tokens in addition to the DOI.  The final source also
defines the quasi-Schatten convention for `0<q<1`, labels the scaling limit
with `m -> infinity`, cites the VVZ monograph in the text, and declares the
v0.2.0 evaluation schema explicitly.
