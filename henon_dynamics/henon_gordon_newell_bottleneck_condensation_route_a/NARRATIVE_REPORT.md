# Narrative report — canonical queues, reversal, and condensation

## One-sentence conclusion

An arbitrary finite irreducible Gordon–Newell network, including genuinely
nonreversible routing, is governed by one canonical complete-homogeneous
partition function whose derivatives, adjacent-population ratio, and maximal
weights respectively close occupancies, flows/reversal, and bottleneck
condensation.

## Why the theorem is one coherent step

The partition function is not an isolated normalization trick. It is the
common object behind four layers:

1. **Finite equilibrium.** Exact global balance gives
   `pi_N(n) proportional to product_i w_i^(n_i)` and
   `Z_N=h_N(w)` without detailed balance.
2. **Observable calculus.** Euler and ordinary weight derivatives give every
   joint occupancy moment. The adjacent ratio `Z_(N-1)/Z_N` gives the busy
   probability, station throughput, and every directed service-event flow.
3. **Arrow of time.** Stationary flow reversal transposes the traffic ledger
   and yields `p*_ij=e_j p_ji/e_i`. Nonzero stationary currents persist in
   nonreversible examples even though the same product law remains exact.
4. **Thermodynamic allocation.** The singularity of
   `product_i(1-w_i z)^(-1)` at the largest weight separates tight geometric
   coordinates from a uniform weak-composition bottleneck sector. A unique
   maximizer captures all but `O_P(1)` customers; a tie retains a random
   macroscopic Dirichlet split.

The tie is a feature rather than a nuisance. Replacing it by an infinitesimal
perturbation would change the theorem from Dirichlet condensation to a unique
bottleneck and would erase the all-equal face.

## Proof versus evidence

The paper proves the finite law by global balance, derives reversal from the
stationary Radon–Nikodym ratio, and proves condensation by a positive
coefficient convolution plus uniform-composition factorial moments. Those
arguments cover arbitrary finite `m`, all `N>=0`, and the `N->infinity`
sequence at fixed network parameters.

The JSON receipt has a narrower job. It contains 9 rational networks and all
177 of their composition states, three exact reconstructions of each finite
partition function, 165 degree-at-most-three factorial-moment cells, exact
event flows and reversed routing, 28 finite condensation cells, and 12
boundary cells. An independent checker rebuilds the Fraction generator and
its left nullspace. These cells detect implementation or transcription
errors; they do not replace the proof or certify untested parameter values by
enumeration.

## Classical ownership and non-originality

Gordon and Newell’s 1967 paper is the explicit classical owner of closed
exponential-server equilibrium and slowest-stage asymptotics. Kelly’s 1979
book owns the standard reversibility framework; Kelly and Yudovina give a
modern stochastic-network account. The paper cites those sources for
ownership and context and does not claim to invent product form,
time-reversal theory, or bottleneck asymptotics.

The source-local contribution is the exact unified statement, proof and
boundary ledger plus the independently reconstructible release artifact.

## Route-A stopping result

The network has a well-defined finite Markov generator, but that fact is not
a formal quantization and does not create a Hilbert–Pólya candidate. There is
no arithmetic origin, rational-prime carrier, logarithmic-prime clock,
intrinsic deterministic primitive-orbit ledger, target determinant, target
divisor, or same-clock unitary lift. Generic positive parameters vary
continuously and prove too much for unrelated networks.

Accordingly the tuple is exactly
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, the overall result is
`ROUTE_A_REJECTED`, and Route B is false under
`NO_BAD_EULER_OR_ROOT_NUMBER`.
