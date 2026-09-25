# Hamiltonian-return card — ASFS-20260915-WHR01

**Candidate ID:** ASFS-20260915-WHR01  
**Version:** 1, frozen 2026-09-15 before the proof or computation.  
**Initial status:** P0 HYPOTHESIS — COMPLETE ENERGY OWNER AND FULL RETURN LEDGER OPEN.

This is the single Lane H contract under the
[168 frozen scope](../168-source-return-breadth-frontier/candidate-card.md).
It changes the geometric generator, carrier and clock; no clock, packet,
trace or Route result transfers from an earlier object.

## Frozen full Hamiltonian owner

For every integer n>=2 define the finite proper-divisor witness count

\[
a(n)=\sum_{2\le d<n}\mathbf1_{\{d\mid n\}},\qquad
V_a(q)=(1-a)\log\cosh q+a q.
\]

All integer components and all real states are retained in

\[
\mathcal X=\coprod_{n\ge2}\mathbb R^4_{q,p,Q,P},\quad
\Omega=dq\wedge dp+dQ\wedge dP,\quad
H_n=\tfrac12p^2+V_{a(n)}(q)+QP.
\]

Fix the energy **H=1 for every n before the audit**. The full primary
energy owner is \(\mathcal E=\coprod_nH_n^{-1}(1)\), with the actual
Hamiltonian vector field defined by \(\iota_{X_H}\Omega=dH\).
The proposed complete ODE is

\[
\dot q=p,\qquad \dot p=-V'_{a(n)}(q),\qquad
\dot Q=Q,\qquad\dot P=-P.
\]

No prime-dependent energy, added roof, reset seam or deletion of real
Hamiltonian states is allowed.

## Frozen section and operational return owner

The full transverse section is

\[
\Sigma=\{(n,q,p,Q,P)\in\mathcal E:q=0,\ p>0\}.
\]

Let M be the subset of Sigma on which actual section hits extend
indefinitely in both forward and backward Hamiltonian time, with the
first positive and last negative section-hit times finite. The proposed
map F is the actual first positive return on this maximal bi-return
domain; tau is its actual elapsed Hamiltonian time. Their existence,
smoothness, positivity, invariant domain and accumulated-time divergence
are audit obligations, not assumptions that all of Sigma returns.

The suspension is the endpoint-glued quotient of
\(\{(z,t):z\in M,0\le t\le\tau(z)\}\) by
\((z,\tau(z))\sim(Fz,0)\). Its proposed owner map sends
\([z,t]\) to the full Hamiltonian flow point \(\Phi^t(z)\).
The image is precisely the return-saturation of M if proved. It is **not
assumed to equal the entire energy surface**. All nonreturning states in
the full energy owner must be classified to verify that no closed orbit
was discarded. The prime oscillator energy E=1-QP is an audit variable;
which signs of E correspond to actual full-energy states must be proved.

| P0 field | Frozen definition / boundary |
| --- | --- |
| Source lineage | Prime/composite divisibility symbols and exclusion constraint -> full finite witness count -> conservative oscillator/escape potential with a transverse hyperbolic Hamiltonian pair -> actual Poincare return map |
| Permitted inputs | All n, all trial divisors 2<=d<n, ordinary divisibility, the fixed displayed potential and energy 1; no prime table, prime-selected components, log-n roof, von Mangoldt weights or zero data |
| Source evolution | The count is a fixed coefficient computed by the same finite formula on every component; no chronological cross-n sieve trajectory or computation-time clock is claimed |
| Full geometry | Countable disconnected four-dimensional Hamiltonian manifold; complete regular full energy and positive-dimensional symplectic return domain remain to prove |
| Return form | The restriction of Omega to Sigma and then M; nondegeneracy and exact full return-map preservation must be checked |
| Clock | Actual elapsed time for the displayed autonomous ODE; no external reparameterization and no zero-time scale reset |
| Primitive ledger | All nonconstant closed orbits of the complete energy flow modulo oriented time shift, and all primitive F-orbits; prove exact correspondence, full multiplicity and repetitions |
| Degeneracy | Full transverse return derivative and all repeated monodromies to determine; no selection of a centre or zero section as the orbit definition |
| Analytic proposal | Ordinary unweighted full-orbit Z only as a minimal convergence diagnostic; operator, space, trace, Fredholm and analytic continuation NOT SUPPLIED |
| Measure | Componentwise canonical symplectic forms and Liouville volume; no finite canonical total probability or trace normalization is imposed |
| Controls | Set every witness to zero; composite-only diagnostic; arbitrary nonnegative integer witness replacement; remove the transverse QP term; compare unrestricted energy with the pre-fixed energy; audit every nonreturning state |
| PROVES_TOO_MUCH | The interpolation may realize arbitrary zero sets of integer constraints; actual clock ownership would not prove arithmetic naturalness or logarithmic prime timing |
| Stop rule | Stop at failed completeness/regularity/return ownership, hidden closed-orbit multiplicity, or an infinite common-time primitive packet family; no parameter, potential, energy or roof tuning |
| Later owner / Route | Hamiltonian owner explicitly supplied above, not inferred from a mapping torus; no contact/quantum construction; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

## Bounded history collision

[038](../038-hamiltonian-periodic-ledger-obligation/paper.md) states the
full positive-dimensional periodic-ledger obligation; it supplies no
Hamiltonian for this contract.
[152](../152-coupled-witness-henon-escape/candidate-card.md) uses the same
kind of complete witness count in a different discrete Hénon potential.
[155](../155-derivative-roof-completeness-test/paper.md) is the incomplete
derivative-roof comparator.
[160](../160-source-geometric-return-clock/candidate-card.md) supplies a
different full map with prespecified dilation/reset timing. The current
contract replaces that timing architecture with one continuous autonomous
Hamiltonian, while keeping the separate source-naturalness obligation.

## Version-1 audit result — tuple unchanged

**Candidate ID:** ASFS-20260915-WHR01  
**Status:** STOP — COMPLETE HAMILTONIAN RETURN OWNER; INFINITE COMMON-TIME PRIME PACKETS.

The [paper](paper.md) proves complete ambient Hamiltonian dynamics, regular
H=1, the full operational return domain and its symplectic positive-
dimensional first-return map. The actual roof is T(1-QP)>=2 pi. The
suspension is exactly the Hamiltonian return-saturation, not the entire
energy surface. All omitted energy states are explicitly nonclosed;
prime E<0 states do not exist.

Every full-energy primitive closed orbit is the unique energy-1 oscillator
oval on a prime component, with Q=P=0 derived from periodicity rather
than selected in the carrier. All primes have the same period T(1), and
all transverse repeats are hyperbolic. Infinitely many common-time packets
prevent the ordinary full unweighted orbit product on every right
half-plane. No energy or potential is tuned to repair the failure.

Decision: stop the clock/product contract, retain the owned Hamiltonian
geometry as a control. Source-naturalness remains OPEN; exact prime-log
timing fails. No operator or formal Route result is supplied. Formal
coordinates UNASSIGNED; Route B NOT INVOKED.
