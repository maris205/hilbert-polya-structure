# Finished-manuscript mathematical review: nonlinear two-pair Hamiltonian

**Candidate ID:** ASFS-20260915-NHC01  
**Review state:** COMPLETE — no unresolved mathematical blocker or required correction found in the scoped audit.  
**Candidate status reviewed:** ADVANCE — COMPLETE NONLINEAR TWO-PAIR HAMILTONIAN PACKETS; GLOBAL RETURN OWNER OPEN; NATURALNESS OPEN.  
**Actual final review time:** 2026-09-15 13:44:49 UTC (clock reading immediately before this receipt was written).  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Actual invocation, reading and authority

The actual finished-manuscript reviewer is
`/root/research_controller/nonlinear_two_pair_hamiltonian/nonlinear_hamiltonian_reviewer`.
It was invoked after the five author-owned core files existed and read
the current [paper](../paper.md), [frozen card](../candidate-card.md),
[claim ledger](../claim-ledger.md), [README](../README.md) and
[evidence index](README.md) completely. The review checks those actual
proofs, not just the proposal, a planned checklist or the author's summary.

The reviewer read the stream AGENTS, plan, current overview and roadmap
boundary, the prior-work guide and the Round-17 scope. For the actual
local dependencies it read 171's generator, primitive classification and
complete Proposition 5, and 176's generator, return-domain argument and
periodic/stability comparison passages. Only the scalar restriction of
171 is identified; no earlier full return owner or analytic result is
assumed. These local reads are not a literature or novelty audit. The
external claims in the prior-work guide were not evaluated or used as
premises of this proof audit.

ARS contributes bounded claim/evidence/reasoning and explicit
counterargument discipline. Its router, reviewer workflow and CER role
instructions were read; the caller's narrower audit authorization governs.
No full ARS review panel, editorial decision pipeline, configuration
interview, runtime, hook, external-model transport or script was invoked.
No venue criteria were supplied: `criteria_binding_unavailable`, with
no venue-fit, calibration or publication-readiness claim.

This is a separate actual invocation but a same-session, inherited-model,
nonblind model review. Author/proposal history and upstream comments were
visible. It is not human peer review, a fresh blind experiment, a
cross-family assessment or an independent-error certificate. The earlier
card-only `escape_inequality_check` is disclosed in the evidence index;
it is not counted as this finished-manuscript review.

A further read-only helper,
`/root/research_controller/nonlinear_two_pair_hamiltonian/nonlinear_hamiltonian_reviewer/clock_local_germ_check`,
read the actual paper and card and recomputed Sections 3--5 while this
reviewer audited the complete-state estimates and ownership. Its final
message confirmed the period bounds, feedback constants, local germs
and escaping-section control. The helper had inherited context and
received the reviewer's preliminary no-defect observation before its
final response; no blindness or independent-error process is claimed.
The responsible reviewer also directly checked those same formulas.
The helper wrote no file and ran no full-batch mechanical check.

## Claim, evidence and reasoning audit

### 1. Global transverse inequality and its exact use

From the displayed Hamilton equations,

\[
\dot L=2S+2\epsilon W
\sum_{j=1}^2(Q_j\Psi_{P_j}+P_j\Psi_{Q_j}).
\]

For each corresponding coordinate, the absolute value of the summand
is bounded by its square: for example
\(|Q_1\Psi_{P_1}|\le |Q_1\tanh Q_1|\le Q_1^2\).
Thus the perturbation sum has absolute value at most \(S\), and
\(0\le W\le1,\epsilon=1/100\) give
\(\dot L\ge99S/50\) on every real state, not merely on energy 1.
Integrating over any positive closed time forces \(S\equiv0\).

The signed-\(L\) warning is essential and is present in the manuscript
and NHC-1: this does not establish that \(S\) is increasing or that every
off-axis state escapes forward. No stronger escape claim is used.

### 2. Completeness, regularity and composite exclusion

The bounds \(|W'|\le4\), \(c_n\le5/4\), bounded first derivatives of
\(\Psi\), and the fixed epsilon yield precisely the scalar acceleration
bound \(C_n=5|1-a|+8a+4\epsilon\) and transverse linear-growth bounds
in (6). Integration in either time direction prevents finite-time
coordinate blowup. Componentwise constants suffice for the countable
disjoint union, since trajectories never change integer component.

At a critical point the vector field vanishes, so the same inequality
forces all transverse coordinates to zero. Thereafter \(p=0\).
Composite components have \(V'\ge3a+5>0\); prime critical energies are
only 0 and \(c_n>1\). Energy 1 is therefore regular on the entire owner.
Independently of transverse products or energy,
\[
\dot p\le-(3a+5)+4/100\le-199/25
\]
for every composite. The negative full-state bound is valid here because
the new interaction is bounded; 176's unbounded-product force reversal
has not been transferred to this different Hamiltonian.

### 3. Entire periodic ledger, orientation and repetitions

The transverse-zero axis is invariant, but it is not chosen as a reduced
carrier. Its necessity for every closed trajectory follows from item 1.
On it the scalar restriction is exactly (7) at energy 1. Composite
closure is excluded. For primes, the four simple roots of \(c_nW=1\)
produce one inner oval and two one-turn unbounded branches. Neither
outer branch closes. There is no equilibrium on this energy.

Consequently the full energy of the six-dimensional Hamiltonian has one primitive oriented
trajectory per prime, with no off-axis or outer extra packet. The
negative-momentum half belongs to the same orbit. Every positive-time
closure of that orbit is an integer traversal, giving \(rT_p\), not a
new component indexed by \(p^r\). The proof covers all states and all
repetitions without finite enumeration.

### 4. Actual physical period and unchanged scalar dependency

The substitution \(y=(1-q^2)/(1+q^2)\) gives
\(1-c_nW=c_n(y^2-\delta^2)\),
\(\delta=(n^2+1)^{-1/2}\), and the exact derivative and prefactor in
(10). On the lower interval the error is bounded by
\[
C\int_\delta^{1/2}\frac{y\,dy}{\sqrt{y^2-\delta^2}}
=C\sqrt{1/4-\delta^2}\le C/2.
\]
On the upper interval the denominator is at least \(\sqrt{1/20}\),
including \(n=2\), and \(f\) is integrable. The arcosh difference from
\(\log(1/\delta)\) is uniformly bounded. The remaining \(c_n^{-1/2}\)
factor changes the result only by a bounded error. Thus the coefficient
is exactly \(2\sqrt2\) in \(T_p=2\sqrt2\log p+O(1)\).

The scalar restriction, energy and clock match 171 as explicitly stated;
the new paper also writes out the calculation. This is not a new
primitive clock, exact \(\log p\) identity, time rescaling or import of
171's global return domain. Composite well-only integrals are correctly
labelled comparators, not composite periods.

### 5. Real nonlinear feedback at an attainable point

At (12), direct substitution gives
\[
W(1/2)=16/25,\quad c_2W=4/5,\quad I_1+I_2=3/16,\quad
\epsilon W=4/625.
\]
The lower bound \(1/80-4/625=61/10000>0\) verifies that the
specified real \(p\) exists and gives energy 1. The function
\(k(t)=2t/\sinh(2t)\) is strictly decreasing for positive \(t\);
the bracket in (11) is positive because \(P_1<Q_1\). Hence
\(\dot I_1>0\) at this actual state. Also \(W'(1/2)=192/125\),
so the additional scalar force is exactly \(-48\Psi_*/3125\).
The displayed cross-pair derivative is positive.

The abstract's plural “individual transverse product integrals” is
supported without a correction: the Hamiltonian and energy condition
are invariant under exchanging the two pairs, and exchanging them in
(12) yields an energy-1 point with \(\dot I_2>0\). These facts prove
coordinate-level feedback and failure of the named product integrals,
not nonintegrability, chaos or unrestricted nonconjugacy. The manuscript
maintains that distinction.

### 6. Local symplectic germs and determinant sign

The section form in (14) is the pullback of the ambient form, and
\(\dot q=p>0\) ensures transverse crossings. Smooth dependence near
the prime oval and the sole intervening negative-momentum crossing
justify the local first-positive-return germ. The variable-time terms
in the form pullback vanish on energy tangents because
\(\iota_X\Omega=dH\).

The interaction is fourth order transversely and has zero transverse
Hessian on the axis. Both the section's first-order energy correction
and the return-time correction to transverse coordinates vanish there.
This gives two copies of \(e^{rT_p},e^{-rT_p}\) for each fixed
positive integer \(r\). Each pair contributes a negative factor
\(2-e^{rT_p}-e^{-rT_p}\); the full signed determinant is its
strictly positive square as in (15).

This is a statement about local germs for each fixed packet and iterate,
not about a single invariant neighborhood for all iterates or a global
self-map. The usual neutral autonomous time/energy directions are
correctly excluded from the transverse multiplier list.

### 7. Full-section obstruction and OPEN original suspension P0

Point (16) has energy \(2-1=1\). On the invariant subspace
\(Q_2=P_2=0\), the interaction and all its first derivatives vanish.
The first product is \(-1\); the scalar energy is 2, so
\[
p^2=2(2-c_2W)\ge3/2.
\]
Its initially positive momentum cannot change sign, and \(q\) never
returns to zero. Thus the entire section is not a self-returning base.
The paper does not overstate this example as excluding every possible
invariant return domain.

Global invariant positive-dimensional return geometry, its full actual
roof, the return non-Zeno condition and suspension identification are
not supplied. Ambient Hamiltonian completeness and a complete periodic
ledger do not fill those separate P0 fields. Their OPEN status is
consistent across the five reviewed files.

### 8. Adversarial controls and analytic/Route boundary

The changed-witness control correctly retains packets on precisely the
zero set of an arbitrary nonnegative integer-valued coefficient. This
exposes a source-naturalness risk without refuting the scoped constructed
ledger. The epsilon-zero comparison keeps the same periodic clock and
linear multipliers; the interaction's novelty is limited to off-axis
nonlinear dynamics.

Removing both quadratic transverse terms really leaves a continuum
on \(Q_2=P_2=0\). Replacing the barrier coefficient by \(5/4\) gives
common prime periods; replacing it by 1 loses the inner periodic oval
and makes the axial barrier points critical on energy 1. These are
separately labelled controls, not alterations of the frozen owner.

No analytic zeta theorem, transfer space/operator, Fredholm determinant,
trace, contact or quantum owner is claimed. In particular 179's
scale-clock operator is not used. The A0/A1-related rows are scoped
Hamiltonian construction evidence, with naturalness and suspension P0
OPEN, not assigned formal Route coordinates. Route B is NOT INVOKED.

## Findings and disposition

No mathematical blocker or required minor correction was found in this
actual finished-manuscript audit. The explicit open global return fields
and naturalness are substantive limits, not findings that have been
silently marked resolved. No manuscript change was requested or made.
No finding quota or simulated independent endorsement is used.

The supported decision is **advance** the complete nonlinear Hamiltonian
owner within its bounded construction scope and end this proof lane.
Its decisive positive result is the all-state closed-orbit exclusion
inequality. It is not a completed original ASFS suspension P0, a new
primitive clock, a new linear Floquet law, or a formal Route pass.
Any later ownership construction must retain this generator and actual
time or receive a new candidate identity.

## Reviewed core identities and handoff

The author confirmed that the four files below were frozen. SHA-256 was
read using `sha256sum` at the 2026-09-15 13:42:20 UTC checkpoint,
after the reviewer's full manuscript reads; no core changed during the
subsequent bounded helper closure.

| Reviewed file | SHA-256 |
| --- | --- |
| [README.md](../README.md) | `a16d5347a64d9a2ba2e8480a6604f834ec5ebdf3b0dd9c0aeca40921d6125e75` |
| [paper.md](../paper.md) | `c15fb43ecb203c276c658f7d0be27f4889d2f029f7fde32681156b6bbd0b8ce1` |
| [candidate-card.md](../candidate-card.md) | `cbf36e9934e4a60abf06a87c22c6a7302e3e3065da8316a4737c18857fc74278` |
| [claim-ledger.md](../claim-ledger.md) | `5a45c55de6d3e77f92196c0ecde951e164903f924add5d1c1cdafe7b8c720ee0` |

The fully read evidence index is deliberately not hash-frozen so the
author can append this actual closure. This reviewer wrote only this
receipt via apply_patch and now stops writing. There was no numerical
experiment, external lookup, script, code/PDF/TeX artifact, Git mutation
or full-batch mechanical validation in this audit. Root alone retains
the final integrated inventory, link, current-ID/status, reviewed-hash
and protected-file checks; their results are not inferred here.
