# Paper-writing improvement log

The manuscript has three content-distinct deterministic revisions.

## Round 0 — `main_round0_original.pdf`

Frozen the Hamiltonian, invariants, conic equation, and Route-A tuple.  This version intentionally kept the proof ledger short so that notation and sign conventions could be checked first.

## Round 1 — `main_round1.pdf`

Added the radial momentum polynomial and the explicit normalization
\[
 (2\pi)^{-1}\oint p_rdr=(\pi)^{-1}\int_{r_-}^{r_+}p_rdr,
\]
the period/action derivative check, all three collision antiderivatives, and the distinction between physical incompleteness and the regularized configuration equation.

## Round 2 — `main_round2.pdf` (release)

Added the hyperbolic scattering convention, the general fixed-time resonance \(T=mP(E)\) for every integer \(m\ge1\), the positive-dimensional fixed-shell consequence, exact ledger counts, independent checker/SymPy/replay/mutation results, historical DOI links, and the explicit statement that configuration continuation is not a full Ligon–Schaaf symplectomorphism.  The Route-A rejection and all prohibited-data nonclaims are now visible in the paper itself.

Both substantive revisions were rebuilt at a fixed `SOURCE_DATE_EPOCH`; hashes and font embedding are checked by the release script.
