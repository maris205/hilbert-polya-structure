# Finite-support log-factor torus flow

**Paper ID:** 224-log-factor-torus-flow  
**Candidate ID:** ANG-20260918-LFT01  
**Date / status:** 2026-09-18; PRE-P0 BROADENED SCREEN  
**Route state:** Owner-level T0 and T2 exact; T1 source established but log-scale naturalness OPEN; T3 NOT SUPPLIED. Formal Route-A coordinates are UNASSIGNED and Route B is NOT INVOKED.

## Abstract

This paper freezes a broadened arithmetic action before analysing it.  The
source is the multiplicative monoid of positive integers, viewed through its
monoid algebra: indecomposable elements under divisor factorisation are derived
internally and are exactly the primes.  For every nonempty finite set \(J\) of
such atoms, the carrier has one component
\(T_J=\prod_{a\in J}\mathbb R/(\log a)\mathbb Z\), with the same translation
vector \((1,\ldots,1)\).  The full carrier is the disjoint coproduct of all
these components.

The exact owner-level result is that a singleton prime component is one
primitive circle of period \(\log p\), with repeats \(m\log p\), whereas no
mixed component has a positive-period closed orbit.  Mixed translations are
therefore nonperiodic quasiperiodic actions (but remain recurrent as compact
torus translations); two-atom components are dense,
while density for larger components is left conditional on the corresponding
reciprocal-log frequency independence.  The logarithmic lattice is a declared
scale design, not a derived natural clock.  No momentum/cotangent lift,
finite-dimensional symplectic map, transfer operator, determinant, or Route
claim is supplied.

## 1. Candidate identity and same-object ledger

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Carrier | \(X_{\mathrm{LFT}}=\coprod_{\varnothing\ne J\Subset\mathsf A}T_J\), a graded arithmetic action/groupoid carrier | frozen |
| Arithmetic source | \(\mathsf M=(\mathbb N_{\ge1},\cdot)\), its monoid algebra, and the divisor-defined indecomposable set \(\mathsf A\) | frozen |
| Flow | \(\phi^t_J(\theta)_a=\theta_a+t\pmod{\log a}\) on every component | frozen |
| Clock | Component periods \(\log a\); a declared logarithmic scale convention | frozen but naturalness OPEN |
| Closed-orbit ledger | All actual closed flow orbits in every component; no singleton-sector restriction | exact in this paper |
| Repetition convention | Primitive singleton period \(\log p\); its positive repeats; no mixed repeats | exact in this paper |
| Operator / trace / determinant | None | NOT SUPPLIED |
| Classical symplectic base/map | None; this is not a finite-dimensional symplectic object | NOT APPLICABLE |
| Optional lift | No cotangent, momentum, Hamiltonian, contact, or quantum lift | deliberately absent |

The flow, source, clock convention, and orbit ledger above belong to one
coproduct.  The clock is not imported from a different physical flow.  A
future lift would change the phase space and owner, and must receive a new
candidate card; adding momenta would in particular create continuum families
over the base torus packets.

## 2. Question and claim boundary

### Question

Does divisor admissibility supply a same-object broadened flow whose complete
periodic ledger retains prime singleton packets without selecting a prime
subsector by hand?

### Strongest supported claim

Yes at the owner level, with a qualified clock boundary: the intrinsic atom
source supplies all singleton prime circles, and the full flow has exactly
those singleton closed-orbit packets.  All mixed finite atom sets are
nonperiodic.  The statement is an exact elementary theorem for the frozen
carrier; the naturalness of the declared logarithmic scale remains OPEN.

### Explicit nonclaims

- This is not a finite-dimensional symplectic map or a mapping-torus
  suspension, and no classical A0/A1/A2 or Route-A pass is claimed.
- No transfer operator, zeta function, determinant, trace formula, quantum
  spectrum, or Riemann-zero comparison is supplied.
- The logarithms are not claimed to emerge as physical time from the monoid
  action.  They are the frozen scale design.
- Density of every mixed torus is not claimed: it holds for two distinct atoms,
  while higher-rank density requires reciprocal-log frequency independence.
- Results from the distinct positive controls 193 (rapid-decay cone quotient)
  and 196 (finite-face cotangent coproduct) are not borrowed.

## 3. Definitions, inputs, and provenance

Let \(\mathsf M=(\mathbb N_{\ge1},\cdot)\).  Its real monoid algebra has a
basis \(\{e_n:n\ge1\}\) and multiplication \(e_me_n=e_{mn}\).  An integer
\(a>1\) is an atom when it is not a product \(bc\) with \(b,c>1\).  This is
the only arithmetic admissibility test used here.  The elementary fundamental
theorem of arithmetic gives

\[
 \mathsf A=\{a>1:a\text{ is an atom}\}=\{p:p\text{ is prime}\}.
\]

No finite prime list, prime-indexed parameter choice, von Mangoldt weight,
prime-power table, or zero data is an input.  Let
\(\mathcal J=\{J\subset\mathsf A:0<|J|<\infty\}\).  For each \(J\),

\[
 T_J=\prod_{a\in J}\mathbb R/(\log a)\mathbb Z,
 \quad
 X_{\mathrm{LFT}}=\coprod_{J\in\mathcal J}T_J.
\]

The disjoint coproduct remembers the support label \(J\); it does not identify
components with equal dimension.  The atom set is countable, hence the family
of finite supports is countable.  Consequently this coproduct is locally
compact and second countable (each component is a compact metrizable torus),
although it is not a smooth manifold of one fixed dimension.  The action is
translation by \(t\) in every coordinate; every component is compact and the
action is complete for all real \(t\).  This is an `ANG` broadened carrier.

The prime-symbolic lineage is explicit: divisor/composite admissibility is
converted into an intrinsic atom alphabet, finite supports provide symbolic
packets, and the torus action is the broadened carrier.  No sequential
deformation or Hénon lift is asserted.  The relation to 193 and 196 is only a
boundary comparison: they motivate checking mixed support and ownership, but
their completion, cotangent geometry, and analytic owners are separate.

## 4. Exact flow and orbit proof

### 4.1 Singleton atoms

Take \(J=\{p\}\).  The component is \(T_{\{p\}}=\mathbb R/(\log p)\mathbb Z\),
and \(\phi^t(\theta)=\theta+t\).  Every point traverses the whole circle,
and the least positive return time is \(\log p\).  Thus the component owns
one primitive geometric orbit (up to phase) and the repetition times are
\(m\log p\), \(m=1,2,\ldots\).  The full coproduct contains one such circle
for each atom, with no manually selected prime sector.

### 4.2 Mixed supports have no closed orbit

Suppose \(|J|\ge2\), and choose distinct \(a,b\in J\).  A positive return
time \(t\) would require integers \(m,n\ge1\) with

\[
 t=m\log a=n\log b.
\]

Exponentiating gives \(a^m=b^n\).  Since \(a\) and \(b\) are distinct
indecomposable integers, unique factorisation makes this impossible.  Hence
no point of \(T_J\) is periodic, and the mixed component contributes no
primitive or repeated closed orbit to the intrinsic ledger.

The same argument applies to every pair in a larger support.  For two atoms,
\(\log b/\log a\notin\mathbb Q\), so the one-parameter subgroup is dense in
the two-torus by the standard irrational-translation criterion.  In higher
dimension the orbit is a quasiperiodic translation with closure a subtorus;
it is dense in all of \(T_J\) precisely when the frequencies
\(\{1/\log a:a\in J\}\) are rationally independent.  That higher-rank
independence is not silently inferred from unique factorisation and is left
OPEN.  What is unconditional for every mixed \(J\) is the absence of a
positive period.

### 4.3 Full packet and repetition ledger

The closed-orbit set of the full disjoint coproduct is therefore exactly

\[
 \bigsqcup_{p\in\mathsf A}T_{\{p\}},
\]

where each circle is one primitive packet with length \(\log p\).  All mixed
components remain in the carrier and are explicitly recorded as nonperiodic
(not as nonrecurrent); they are not discarded to manufacture a prime-only
result.  Repetition is
intrinsic to each singleton flow and is not a second orbit in another support.

## 5. Controls and adverse findings

| Control | Result |
| --- | --- |
| Composite atom control | A composite integer is decomposable and never labels a singleton component; composites are excluded by the source rule, not by deleting periodic composite orbits afterward. |
| Mixed-support control | Every finite \(|J|\ge2\) component is retained and shown nonperiodic; no representative orbit is selected. |
| Clock ownership | \(\log a\) is used by the same component that owns the orbit, but its naturalness is not proved. |
| Full-coproduct control | The ledger is computed on all finite atom supports, not on a prime-sector restriction. |
| 193 comparison | The rapid-decay cone quotient is a different carrier and completion; no state, action, measure, or trace is imported. |
| 196 comparison | The finite-face cotangent coproduct is a different conservative owner; no cotangent form, momentum, or operator is imported. |
| Lift control | Adding a cotangent/momentum coordinate would make continuum packets over each base component and is a new candidate, not a harmless completion. |
| `PROVES_TOO_MUCH` control | The construction does not claim that every finite support is periodic; in fact it proves the opposite for mixed supports. |

The main adverse finding is therefore not a failure of the exact broadened
ledger, but a naturalness boundary: the atom rule explains which circles are
present, while the logarithmic lattice is still a declared scale choice.

## 6. Gate assessment

| Gate | Evidence for this exact candidate | Status | Limitation / next obligation |
| --- | --- | --- | --- |
| T0 | One coproduct, one action, one support label, one intrinsic orbit ledger | ESTABLISHED at broadened owner level | Variable component dimensions prevent a classical finite-dimensional admission |
| T1 | Divisor-defined atoms are endogenous; \(\log a\) lattice is declared | PARTIAL / NATURALNESS OPEN | Derive or replace the scale without inserting prime times |
| T2 | All singleton and mixed components classified; repetitions only on singleton circles | ESTABLISHED | Higher-rank density is not needed for the no-period result and remains OPEN |
| T3 | No same-object transfer operator, zeta, or determinant | NOT SUPPLIED | Requires a new operator contract and candidate card |
| Classical A0/A1/A2 | No finite-dimensional symplectic map or suspension | NOT APPLICABLE | A classical realization would be a new candidate, not a lift of this result |
| Route B | No Route-A readiness and no authorization | NOT INVOKED | No coordinate may be issued |

## 7. Conclusion and decision

**Portfolio position: advance as a broadened owner-level control; fork before
any geometry or analytic promotion.**  The candidate gives a clean, same-object
prime singleton packet and an exact negative mixed-support control.  It does
not yet give a natural arithmetic clock or a classical symplectic object.  The
next admissible step is either a new card deriving the logarithmic scale from
the same carrier, or a separately frozen carrier that supplies an operator.
Adding a momentum/cotangent factor is explicitly not that next step: it is a
new candidate and would create continuum packet multiplicity.

## Reproducibility / evidence index

- [Frozen candidate card](candidate-card.md)
- [Claim and boundary ledger](claim-ledger.md)
- [Evidence and verification record](evidence/README.md)

The proof uses only the displayed definitions, unique factorisation, and the
standard torus-translation criterion.  No numerical run, external source,
prime table, or imported operator was used.
