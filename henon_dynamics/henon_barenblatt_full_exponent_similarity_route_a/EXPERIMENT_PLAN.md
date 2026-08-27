# Exact validation plan

## Theorem layer

Derive the similarity exponent and integrated profile equation for arbitrary
real `m>0`.  Solve it separately on `m>1`, `m=1`, and `0<m<1`; prove the
mass-normalization map is strictly monotone and hence unique.  Evaluate mass
and all absolute moments by Beta/Gamma integrals, including divergence at and
above the fast-diffusion threshold.  Prove the pressure/free-boundary and
rescaled stationary identities.  Define both branches of the free energy,
derive its first variation and dissipation identity, and state the exact
finite-energy/regularity/boundary-decay domain.  Treat profiles through the
locally absolutely continuous `F^m` representative and an almost-everywhere
zero-flux identity, so the uniqueness class is mathematically closed.

## Executable layer

The producer uses nine exact rational exponents
`{1/4,1/3,1/2,2/3,1,3/2,2,3,5}`, two exact masses `{1,3/2}`, five profile
locations, and six moment orders `{0,1,2,3,4,5}`.  This yields 18 profiles,
90 profile samples, and 108 moment cells.  Constants are computed with 100
working decimal digits and serialized at 82
significant digits; these are distinct, machine-checked metadata fields.

Validation is intentionally redundant:

1. a checker that does not import the producer recursively freezes every
   schema, theorem/scope literal, exact case/sample/moment grid, Beta mass,
   chemical constant, regime null rule, and serialized precision;
2. a separate SymPy path verifies generic porous/fast profile laws, the
   transformed Beta mass and moment integrals and their exponents, the
   pressure/interface coefficient, stationary chemical potentials, both
   free-energy first variations, and the sharp threshold identities;
3. byte replay regenerates the canonical evidence in a temporary directory;
4. hostile mutations test repaired-hash semantic/schema changes and stale
   hashes;
5. three materially different manuscripts are built at fixed epoch;
6. two fresh final builds must be byte-identical, with embedded subset fonts,
   extractable text, visual inspection, and a warning-free log;
7. a self-excluded manifest closes exactly 27 payload files.

The finite grid is a regression surface, not evidence for universal
quantification; the proof layer carries every `m>0` and `M>0`.
