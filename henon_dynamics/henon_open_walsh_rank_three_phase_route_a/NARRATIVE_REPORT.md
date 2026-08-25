# C168 narrative report

The new progress is not another binary phase walk.  Opening one of four
Walsh symbols leaves three nonzero one-site roots: a unit root and two roots
of common modulus `1/sqrt(2)`.  Their tensor products give an exact
multinomial secular law of degree `3^k` for every register length.

The key algebraic certificate is unusually short.  The ratio of the two
damped unit phases is `r=(-3+i sqrt(7))/4`, and
`r+r^(-1)=-3/2`.  A root-of-unity ratio would make this trace an algebraic
integer; a rational algebraic integer must be integral.  This excludes
torsion without numerical phase fitting.  The multiplicity-weighted phase
measure is the `k`-fold convolution of the three-atom law on
`{1,u_+,u_-}`.  Its `m`th Fourier coefficient is the `k`th power of the
three-atom average.  Every fixed nonzero mode contracts, hence the source
phases converge weakly to Haar.

The common damping of the two nontrivial roots makes log modulus a simple
two-level random variable, but its phase is not discarded.  The exact mixed
Fourier/characteristic transform proves joint convergence to a Gaussian
times Haar, rather than inferring independence from two marginal limits.

The hole-zero model is a deliberately sharp negative control.  Its phases
lie in the fourth roots of unity and converge in total variation to the
uniform finite-group law, at rate at most `(3/2)3^(-k)`.  The
hole1/hole3 reflection and antiunitary/projector-order identities remain
finite-dimensional controls.  They do not turn the open gate into a
self-adjoint Hamiltonian or authorize a target-spectrum comparison.
