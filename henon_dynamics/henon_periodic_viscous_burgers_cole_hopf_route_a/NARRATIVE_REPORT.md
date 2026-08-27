# Narrative result report

HCS-C195 takes a deliberately large step within one dynamical model. Rather than
cataloguing a few explicit solutions, it identifies the whole periodic viscous-
Burgers phase leaf with a positive projective heat cone for every admissible
viscosity, circumference, mean, and Sobolev exponent.

The important normalization is that the true autonomous fixed-coordinate lift is
drift--heat, not simply heat: \(K_t=e^{t(\nu\partial_x^2-m\partial_x)}\). Pure heat
appears only after the Galilean coordinate \(y=x-mt\). This distinction fixes the
sign of the imaginary spectral part and prevents a time-dependent coordinate change
from being overstated as an autonomous conjugacy.

Once the projective coordinate is frozen, the global phase portrait follows. Heat
selects the strictly positive constant Fourier mode, so all Burgers solutions tend
to their conserved mean. This immediately collapses the forward recurrence set to
one constant. A finer spectral-gap expansion of the positive lift yields the exact
leading decay and phase drift for every nonconstant initial datum, while direct
linearization gives the entire complex spectrum.

The executable layer exercises 24 exact rational trigonometric lifts. It catches
algebra/sign/serialization regressions but does not stand in for the Sobolev proof.
The result is mathematically complete as a source-dynamics theorem and deliberately
negative for Route A: there is no intrinsic arithmetic origin, no nonconstant
periodic-orbit ledger, no target divisor or analytic structure, and no Hilbert--Pólya
operator. The classical linearization is only a formal A4 hint.
