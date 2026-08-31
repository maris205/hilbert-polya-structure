# Narrative report

## Central advance

HCS-C265 turns the exponential Hawkes process into one complete source-local
theorem rather than a collection of simulation formulas.  The affine transform
closes finite-time event/count coupling.  The stationary Laplace ODE and
triangular generator recurrence close the entire intensity law at moment
level.  The main conceptual correction is to keep three commonly conflated
objects apart:

1. intensity covariance;
2. complete counting covariance, including its same-event Dirac atom;
3. the Fourier transform of that measure under an explicitly frozen
   normalization.

The window-count variance then follows by exact integration, and the Borel
family law identifies the genealogical source of the stability threshold.

## Evidence

The canonical evidence contains 320 subcritical cases.  A separate checker
reconstructs generator coefficients rather than importing the producer.
SymPy verifies generic transform identities; fresh replay is byte-exact;
hostile mutations target metadata, scope, the Route-A tuple, each covariance
object, moments, window coefficients, clusters, and boundary policy.

## Boundaries and limitations

At `a=0` the model is homogeneous Poisson.  At `nu=0` the empty process is
stationary.  For positive immigration, `a=b` and `a>b` rule out finite-
intensity stationarity through the mean equation.  The paper does not assert
that a finite regression grid proves these statements, nor that the Markov
generator is a quantum Hamiltonian.

Hawkes event clusters are random genealogies.  They do not define a
deterministic primitive-orbit ledger, rational-prime labels, a logarithmic
prime roof, a target divisor, or a Hilbert--Pólya spectrum.  The strict Route-A
outcome is therefore rejection with a formal generator hint only.
