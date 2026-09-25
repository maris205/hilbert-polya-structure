# Frozen nonlinear two-pair witness Hamiltonian

**Candidate ID:** ASFS-20260915-NHC01  
**Version:** 1, frozen 2026-09-15 before mathematical audit.  
**Initial status:** HAMILTONIAN-LEVEL P0 HYPOTHESIS — FULL CLOSED LEDGER OPEN; ASFS SUSPENSION P0 OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

This is Lane H of the [185 scope](../185-physical-clock-construction-frontier/candidate-card.md).
The identifier was checked with `rg -l 'ASFS-20260915-NHC01' papers --glob '*.md'`
before this card was written; no match was returned. This is a new
six-dimensional generator, not a modification of [171](../171-separatrix-witness-hamiltonian-clock/candidate-card.md)
or [176](../176-cross-coupled-witness-hamiltonian/candidate-card.md).

## Exact Hamiltonian owner

For every integer n >= 2, retain every real state and define

\[
a(n)=\sum_{2\le d<n}\mathbf1_{\{d\mid n\}},\qquad
c_n=1+n^{-2},\qquad W(q)=\frac{4q^2}{(1+q^2)^2},\qquad
\epsilon=\frac1{100},
\]
\[
\Psi(Q_1,P_1,Q_2,P_2)=\tanh Q_1\tanh P_1\tanh Q_2\tanh P_2,
\]
\[
\mathcal X=\coprod_{n\ge2}\mathbb R^6_{q,p,Q_1,P_1,Q_2,P_2},\qquad
\Omega=dq\wedge dp+dQ_1\wedge dP_1+dQ_2\wedge dP_2,
\]
\[
H_n=\frac{p^2}{2}+(1-a(n))c_nW(q)+8a(n)q
       +Q_1P_1+Q_2P_2+\epsilon W(q)\Psi.
\]

The primary owner is the **entire** level
\(\mathcal E=\coprod_{n\ge2}H_n^{-1}(1)\), with the disjoint-union
smooth topology and the actual Hamiltonian evolution defined by
\(\iota_X\Omega=dH\). Ambient completeness and regularity of this
energy are obligations, not assumptions. The same coefficient epsilon,
energy 1 and physical time units are fixed on all integers. No post-proof
tuning, time change, reset, deletion of off-axis states or selection of
one orbit from a periodic continuum is permitted.

## Operational section, not a supplied global base

The specified section is \(\Sigma=\{H=1,q=0,p>0\}\). Because W(0)=0,
its proposed coordinates are all four transverse coordinates satisfying
\(Q_1P_1+Q_2P_2<1\), with
\(p=\sqrt{2(1-Q_1P_1-Q_2P_2)}\) and section form
\(dQ_1\wedge dP_1+dQ_2\wedge dP_2\). Local or global existence of
actual returns must be proved. An operational first-return domain is not
automatically a globally invariant smooth symplectic manifold. In
particular, merely defining the set of all bi-infinite section hits does
not supply the original ASFS base-map contract.

**Global self-map F, its invariant positive-dimensional domain M, full
roof tau, non-Zeno return property and suspension identification: OPEN.**
If such a domain is established without changing this Hamiltonian, the
only admissible roof is its actual elapsed return time, and the only
admissible suspension is endpoint gluing
\((z,\tau(z))\sim(Fz,0)\), mapped by \([z,t]\mapsto\Phi^t(z)\)
onto the proved return-saturation. No such owner is imported from 171.
A complete full-energy periodic-orbit theorem can be recorded even if
this separate original ASFS suspension P0 remains OPEN.

| Field | Frozen scope |
| --- | --- |
| Prime-symbolic lineage | Proper-divisor symbols and their full witness-exclusion zero set -> conservative well/escape deformation -> six-dimensional nonlinear Hamiltonian lift. The retained observable is a(n), not a generic symplectic label or a conjugacy to historical Logistic/Henon maps |
| Allowed inputs | Every integer, every proper trial divisor, ordinary divisibility, fixed rational c_n and W, displayed tanh interaction, constants 8 and 1/100, energy 1 |
| Forbidden inputs | Prime or zero tables, von Mangoldt weights, assigned logarithmic roof, independent per-prime choices, fitted time schedules |
| Arithmetic chronology | Static finite witness coefficient; neither sequential trial division nor motion from n to n+1 is claimed |
| Primitive convention | All nonconstant closed trajectories of the entire energy modulo oriented physical-time translation; derive multiplicity, least period, all repeats and transverse monodromy |
| First discriminator | Test L = Q_1^2+Q_2^2-P_1^2-P_2^2 for a strict off-axis growth estimate on all real states, then completeness and regular energy |
| Interaction question | Test real off-axis feedback among the two pairs and the oscillator; no nonintegrability, chaos or unrestricted nonconjugacy claim is precommitted |
| Clock | Actual Hamiltonian time only. Any equality with 171's scalar period requires an explicit invariant-axis restriction, not transfer of its full return owner |
| Measure | Canonical componentwise volume and induced section symplectic form; no finite normalization of canonical volume or trace is supplied |
| Analytic owner | Ordinary orbit counting convention specified above; transfer operator, analytic zeta theorem, Fredholm determinant and trace NOT SUPPLIED in this bounded Hamiltonian contract |
| Controls | Entire energy and off-axis states; composites; epsilon-zero uncoupled comparator; changed witness zero set; absent hyperbolic terms; rational barrier versus constant or zero excess; actual versus assigned roof |
| Naturalness | OPEN: witness zero-set engineering and barrier/coupling choices are declared designs, with PROVES_TOO_MUCH risk |
| Stop / fork | Stop the relevant target at finite-time escape, hidden periodic multiplicity or an unclosed promised ownership step. If the full Hamiltonian ledger closes but global return geometry does not, retain the Hamiltonian result and explicitly leave ASFS suspension P0 OPEN; do not prolong local return repair. Any generator, coefficient, energy or clock change needs a new ID |
| Later owners and Routes | Contact and quantum owners NOT SUPPLIED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

The [prior-work guide](../../docs/prior_work/README.md) fixes the conceptual
lineage only. The proposed inequality, geometry and ledger must be proved
for this exact object. No prior Route credit, return strip, Floquet law,
trace or determinant is inherited.

## Version-1 audit result — unchanged full generator and physical time

**Candidate ID:** ASFS-20260915-NHC01  
**Status:** ADVANCE — COMPLETE NONLINEAR TWO-PAIR HAMILTONIAN PACKETS; GLOBAL RETURN OWNER OPEN; NATURALNESS OPEN.

The [proof](paper.md) establishes a complete ambient Hamiltonian flow,
regular entire energy 1, and the full-state inequality
Ldot >= (99/50)(Q_1^2+Q_2^2+P_1^2+P_2^2). Every full-energy closed
trajectory is consequently forced onto the invariant transverse-zero
axis; its scalar classification gives exactly one primitive oriented
packet per prime, none on composites, and every repetition.

The physical periods remain T_p=2 sqrt(2) log p+O(1), by explicit
identification with the same scalar equation and time units in 171.
Local four-dimensional symplectic Poincare germs have two copies of
exp(plus or minus r T_p) for the r-fold return. Real off-axis feedback
changes the oscillator force and makes I_1=Q_1P_1 nonconstant; neither
a new primitive clock nor nonintegrability or nonconjugacy is claimed.

The full section contains an explicit nonreturning trajectory. The
global invariant positive-dimensional return base, full roof, non-Zeno
return condition and suspension identification remain OPEN. This is
therefore a Hamiltonian-level construction, not a completed original
ASFS suspension P0. No analytic operator or trace is supplied.

Decision: **advance** the complete nonlinear Hamiltonian owner and end
the bounded lane with global return ownership and naturalness OPEN.
No coefficient, energy, state space or clock has changed. Formal Route
coordinates remain UNASSIGNED; Route B is NOT INVOKED.
