# C163 narrative report

C158 left phase unresolved because modulus concentration alone forgets the
argument of each surviving eigenvalue.  C163 returns to the same full-cycle
tensor spectrum and retains the binomial label `j`.  This label makes the
phase a multiplicative random walk with two one-site phases.  Its Fourier
coefficient is therefore a single binomial factor raised to the `k`th power.

The only possible obstruction to Haar convergence is torsion of the phase
ratio.  For the frozen gate, the exact cosine of the phase difference has
primitive irreducible integer polynomial `3x^4-19x^2+27` and monic rational
minimal polynomial `x^4-(19/3)x^2+9`.  The latter has a nonintegral
coefficient, ruling out algebraic integrality, whereas a root-of-unity trace
would be integral.  This closes the obstruction unconditionally and for every
register length.

Keeping the same binomial label also couples phase to C158's centered
log-modulus fluctuation.  The exact mixed transform separates in the limit:
the zero circle mode gives the Gaussian characteristic function, while every
nonzero circle mode is exponentially killed.  The result is a product
Gaussian--Haar law, not merely two marginal statements.

The moved-hole projector supplies a hostile control rather than cosmetic
robustness: its phase ratio is exactly `i`, so it realizes the complementary
finite-subgroup branch.  The control shows why the algebraic non-torsion gate
is essential.  No model pivot was needed, and no target or arithmetic claim
was introduced.
