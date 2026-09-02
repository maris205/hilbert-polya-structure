# Narrative report

## Outcome

HCS-C295 closes the entire bound action–frequency geometry of the planar Hénon isochrone potential in one paper-sized theorem.  The result is larger than another numerical orbit sample: it identifies the exact circular energy boundary, integrates the radial action, derives the angular advance, classifies generic closed orbits, and resolves every degeneracy at the edge of the formula.

The decisive invariant is

\[
I=J_r+\frac12\left(\ell+\sqrt{\ell^2+4\mu b}\right),
\qquad H=-\frac{\mu^2}{2I^2}.
\]

It makes the isochrony transparent: \(\Omega_r=\mu^2/I^3\), so \(T_r\) depends on energy but not angular momentum.  Differentiation in \(\ell\) then returns the frequency ratio

\[
\beta=\frac12\left(1+\frac{\ell}{\sqrt{\ell^2+4\mu b}}\right).
\]

For a noncircular bound torus, closure is exactly \(\beta\in\mathbb Q\).  That compact sentence is correct only after three traps are removed: a circle is already closed even when the epicyclic ratio is irrational; a zero-angular-momentum trajectory crosses the regularized center and needs \(2T_r\) for full Cartesian return; and \(E<E_c\) is not an admissible action point.

## Evidence result

The deterministic certificate contains 108 orbit cells and eight boundary cells.  The orbit partition is:

- 36 circular or central-equilibrium degeneracies;
- 18 nonstationary radial center-crossing cases;
- 14 noncircular rational resonances;
- 40 noncircular irrational rosettes.

The producer-independent checker reconstructs exact quadratic-field entries and performs direct period/apsidal quadratures.  SymPy separately checks the symbolic reduction and all grid identities.  Fresh-path replay and hostile parser/schema mutations close reproducibility and validation gaps.  These computations are deliberately described as regression evidence, not proof by enumeration.

## Route-A reading

The model makes real progress on dynamics while remaining a poor arithmetic candidate.  It has exact intrinsic periods and resonant closed-orbit families, hence `A1_WEAK`; those families are continuous rather than an isolated enumerable primitive ledger.  It has no arithmetic local carrier (`A0_FAIL`), no source determinant (`A2_FAIL`), and no target analytic bridge (`A3_FAIL`).  Its bounded real potential gives a canonical self-adjoint Schrödinger quantization (`A4_NATURAL_QUANTIZATION`), but no target spectral identification.

Thus the conservative tuple is

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`,

with overall `ROUTE_A_REJECTED` and Route B locked.  Classical formula ownership remains with Hénon and the later cited isochrone-mechanics literature; the package claims reproducible closure, not literary priority.
