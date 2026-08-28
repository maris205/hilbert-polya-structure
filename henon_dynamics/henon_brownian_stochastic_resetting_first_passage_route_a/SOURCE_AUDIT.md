# Source and ownership audit

## Primary references

| Key | Verified bibliographic record | Imported attribution | Not claimed here |
|---|---|---|---|
| `evans_majumdar_prl_2011` | M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, PRL 106, 160601 (2011), DOI `10.1103/PhysRevLett.106.160601` | fixed-point resetting model, renewal propagator and stationary Laplace law | priority or novelty |
| `evans_majumdar_jpa_2011` | M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, J. Phys. A 44, 435001 (2011), DOI `10.1088/1751-8113/44/43/435001` | first-passage renewal calculation and optimal-rate equation | priority or a new optimum |
| `evans_majumdar_schehr_2020` | M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and applications*, J. Phys. A 53, 193001 (2020), DOI `10.1088/1751-8121/ab7cfe` | review context and notation cross-check | a review is not used as proof of a new claim |

The manuscript labels these as source attribution.  The independent scripts
reproduce the displayed identities and explicitly state their finite-evidence
boundary; no literature novelty is asserted.

## Realization/convention audit

The free process on `R` and the killed first-passage process are separate.  The
stationary Laplace density is only for the former.  The latter is sub-Markov
after absorption.  Resetting is always to `0`, the start is `0`, and the target
is the positive point `a`; changing any of these conventions changes the
formula and is outside this package.

## Claim firewall

No prime or zero table, local arithmetic datum, Euler factor, root number,
automorphy assertion, target divisor, functional equation, or Hilbert–Pólya
operator enters the evidence.  The transform denominator is a renewal
resolvent only.
