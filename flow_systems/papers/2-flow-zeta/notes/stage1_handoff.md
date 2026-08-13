# Stage-1 to Stage-2 Handoff

Date: 2026-08-13

## Frozen inputs

Stage 2 inherits the following results without reopening their clocks or relabelling their objects.

1. `DEN-WITT-Z-FIN` has `A0_ANALYTIC_ARITHMETIC_ORIGIN + A1_WEAK`.  For `Spec Z` and one explicitly allowed finite-kernel admissibility condition, denoted locally by `E_fin`, the periodic set is a disjoint union of compact packets `Gamma_p`; every orbit in `Gamma_p` has least period `log p`, and all periodic orbits are exhausted by the packets.  A rational prime does not select a unique isolated orbit.  Canonical packet multiplicity, transverse measure, phase, smooth monodromy, and trace weight are open or not testable.
2. `MOD-GEO` has `A1_PASS_ANALYTIC + A2_ANALYTIC_DETERMINANT` as a modular-flow benchmark, but is rejected as a rational-prime Hilbert--Pólya candidate.  Under unit-speed hyperbolic arc length, every repeated norm `N_gamma^r` is irrational, so its length support is disjoint from every `k log p`.
3. The modular Ruelle quotient removes the Selberg stability denominator at the level of the logarithmic derivative,

   ```text
   R_Gamma(s) = Z_Gamma(s) / Z_Gamma(s+1),
   R_Gamma'(s) / R_Gamma(s)
     = sum_[gamma primitive] sum_[r>=1] (log N_gamma) N_gamma^(-rs),
   ```

   under the fixed direct-product convention.  This repairs amplitude shape but not arithmetic support, multiplicity, divisor, or self-adjointness.
4. No Stage-1 object reaches strict A0 together with pass-level A1.  Route B remains forbidden.

## Interface carried forward

The only positive interface question inherited from Stage 1 is whether the compact packet `Gamma_p` admits a functorial, intrinsic transverse measure or trace that makes the whole packet contribute one derived repetition term.  Declaring every packet to count once is not an answer: it is the normalization that must be explained.

## Non-inheritance rules

- Do not infer a conventional Ruelle product from the packet-indexed formal Euler product.
- Do not import prime or zero fits from the prior Logistic--Henon papers.
- Do not use the modular near-prime proxy `tr(gamma^2)=t^2-2` as arithmetic support.
- Do not change the Deninger admissibility condition or either candidate's clock without issuing a new source lock and evaluation version.
- If a solution requires a general von Neumann-algebra programme, record it as `ROUND2_CLUE` and return to the flow-specific problem.
