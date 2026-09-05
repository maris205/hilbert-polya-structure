# Claim-driven executable checks

Parameters are frozen before computation: eight fluxes 0, 1/7, 1/4, 1/3, 1/2, 2/3, 3/4, 6/7; angular channels -32 through 32; integer gauge shifts -2 through 2 and base channels -8 through 8; cutoff sizes 0 through 64. No target-data training, validation, fitting, or sealed target test occurs.

The producer uses absolute-difference phases. The checker independently uses the two signed channel halves and reconstructs gauge invariance through squared mechanical angular momenta. Closed heat formulas are checked by direct spectral quadrature of ordinary Bessel functions. Cross sections are checked through a complex amplitude modulus rather than the producer's sine quotient. SymPy separately checks the radial equation, phase pieces, gauge identity, Abel rational expression, and symmetry identity.

Two isolated directories run the copied producer and locked YAML for byte comparison. Hostile mutations repair their payload hash before attacking semantic fields. Duplicate JSON keys, nonfinite values, and duplicate/aliased/merged YAML are separately rejected. Exact finite checks are analytic arithmetic; decimal checks remain numerical observations.
