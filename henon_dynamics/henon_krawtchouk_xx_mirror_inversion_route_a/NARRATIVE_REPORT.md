# Narrative report — HCS-C366

## Outcome

The engineered (N+1)-site XX chain has been closed from one particle to
the entire Fock space.  The single-particle Hamiltonian is exactly a spin
(N/2) (J_x) matrix, so its Krawtchouk spectrum and complete propagator
are analytic.  At half the transfer time an endpoint excitation has the
binomial distribution; at the transfer time the chain mirrors perfectly.

The decisive increment is not another one-particle diagonalization.  The
many-body propagator is proved to be the exterior power of the same unitary,
and the exact mirror phase

\[
(-i)^{mN}(-1)^{m(m-1)/2}
\]

is retained in every $m$-excitation sector. The full energy degeneracy
ledger follows from a recursively defined Gaussian-binomial generating
function. For a field $B\widehat m$, the exact $2\pi/|\Omega|$ propagator is
$e^{-i(2\pi B/|\Omega|)\widehat m}(-1)^{N\widehat m}$ and the exact
$4\pi/|\Omega|$ propagator is $e^{-i(4\pi B/|\Omega|)\widehat m}$; hence the
paper distinguishes sectorwise, parity, and literal full-Fock revivals.

## Evaluation

This is a complete source-local quantum-dynamics theorem with natural
quantization, not an arithmetic spectral construction.  Its strict Route-A
tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and the overall
verdict is `ROUTE_A_REJECTED`.  Route B remains false.

The collision boundary is explicit: C143 owns an inhomogeneous coined quantum
walk, while C171 owns Ehrenfest/Krawtchouk Markov lumping. C366 instead owns
the engineered XX perfect-transfer chain and its full exterior-power phase law.
