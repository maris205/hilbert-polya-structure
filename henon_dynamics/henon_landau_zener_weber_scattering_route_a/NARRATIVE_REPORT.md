# Narrative report

This round changes subtype decisively: C224 is a nonautonomous scattering
problem, not an autonomous excitation-block model.  The linearly swept gap
has one avoided crossing, and eliminating a component exposes a Weber
equation.  The connection coefficient is therefore a global statement about
the two asymptotic time sectors, rather than a fitted finite-window number.

The main theorem fixes a diabatic gauge and gives the SU(2) matrix with
`P=exp(-2*pi*delta)` and
`phi_S=pi/4+delta(log(delta)-1)+arg Gamma(1-i delta)`, where
`delta=g^2/v`.  Wronskian conservation and Hermiticity give unitarity;
different diagonal phase conventions alter only off-diagonal phases.  The
derivative formula proves strict monotonicity, while `g=0`, sudden, adiabatic,
negative-coupling, and turning-point boundaries close the singular cases.

The reproducibility ledger then integrates the original ODE on three finite
windows for five rational parameter cases.  The finite matrix is useful for
checking signs, norm preservation, and the approach to the asymptotic law, but
its discrepancies are reported rather than hidden.  This separation prevents
the common overclaim that a finite RK4 matrix is an exact finite-time Weber
propagator.

Route-A assessment is correspondingly strict.  There is no source-defined
primitive periodic family, arithmetic owner, target determinant, or target
divisor.  The only positive flag is an intrinsic unitary/scattering candidate;
it does not authorize Route B or a Hilbert–Pólya interpretation.
