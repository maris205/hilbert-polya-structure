# C168 research question

For the natural four-symbol rank-three opening
`A=F4^*diag(1,0,1,1)`, can the complete register cycle be resolved for every
`k`, including its secular degree, zero generalized space, phase limit, and
joint phase/log-modulus fluctuations?  Can a same-clock moved-hole control
separate the non-torsion circle law from a torsion finite-group law without
manufacturing self-adjointness?

## Hard gate

An acceptable result must be unconditional in `k`, prove strict contraction
for every fixed nonzero Fourier mode using exact algebra rather than sampled
angles, and state the finite-`k` atomic total-variation obstruction.  A
finite ledger alone does not pass.

## Answer

Yes on the source side.  The rank-three tensor spectrum has exact
multinomial secular product and degree `3^k`.  The phase ratio
`r=(-3+i sqrt(7))/4` satisfies `r+r^(-1)=-3/2`, which excludes torsion.  The
phase Fourier law is therefore strictly contracting mode by mode and tends
weakly to Haar.  A mixed transform proves a joint
`Normal(0,log(2)^2/18) tensor Haar` limit.  The hole-zero control instead
converges in total variation to uniform measure on the fourth roots of
unity.  This does not supply a target-spectrum or self-adjoint construction.
