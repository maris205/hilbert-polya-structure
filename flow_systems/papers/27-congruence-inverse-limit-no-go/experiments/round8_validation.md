# P27 Round-8 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `P27-HOMOLOGY-RENORMALIZED-GEODESIC-PANEL`
- Freeze SHA-256: `88d10c3dcdee3387b16414d2c56d4934b6daeef6728acc689855049840850a72`
- Core SHA-256: `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`

## Exact structure

For `H_N=ker(Gamma -> H_1(Sigma;Z/NZ))`, the deck group is `(Z/NZ)^4`.
Every frozen primitive-content-one owner has exact deck order `N`; its full
preimage consists of `N^3` primitive lift components of physical period
`N*ell(g)`.  Thus the four frozen choices give

```text
raw clock, raw multiplicity:       (1-x_g^N)^(-N^3)
rescaled clock, raw multiplicity:  (1-x_g)^(-N^3)
raw clock, geometric mean:         (1-x_g^N)^(-1)
rescaled clock, geometric mean:    (1-x_g)^(-1)
```

Only the last quadrant recovers the base factor exactly at every level.  The
two raw-clock quadrants escape every fixed coefficient prefix; rescaling time
without multiplicity normalization instead makes the coefficient of `x_g`
grow as `N^3`.

## Exact replay

- Owner/level/quadrant rows: `96`.
- Exact coefficient rows through degree 12: `1248`.
- Three primitive owners and eight factorial moduli are retained.
- All computations use exact integers.

## Route and ownership boundary

This is a newly registered finite-panel calibrator with a new cover tower,
clock, and normalization.  It is not the Round-7 residual inverse-limit owner,
does not define a full-flow determinant, and is generic for every marked
genus-2 hyperbolic metric.  Hence A0 fails and the new candidate is
`ROUTE_A_REJECTED`; the original same-owner verdict is unchanged and Route B
remains closed.
