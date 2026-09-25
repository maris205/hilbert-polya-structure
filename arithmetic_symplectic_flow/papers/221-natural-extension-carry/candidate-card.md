# Broadened candidate card — history completion of the escape-carry screen

**Candidate ID:** `ANG-20260918-HIC01`  
**Version:** 1, frozen 2026-09-18 before the audit.  
**Outcome:** T0/T2 ESTABLISHED; T1 PARTIAL; STOP — SQRT CLOCK AND k MULTIPLICITY.  
**Parent relation:** fresh broadened-carrier fork of 219; no result or owner is
transferred from 219.

## Frozen object

Let X and T:X→X be exactly the four-branch escape-carry rule in
[219's card](../219-reversible-escape-carry/candidate-card.md). Define the
full bi-infinite history space

    X̂ = { x̂=(xⱼ)ⱼ∈ℤ ∈ X^ℤ : T(xⱼ)=xⱼ₊₁ for every j∈ℤ }.

The topology is the product of discrete topologies. The carrier action is the
full shift

    (T̂ x̂)ⱼ = xⱼ₊₁,

and the fixed clock is one unit per shift step. The coordinate projection is
π₀(x̂)=x₀ and satisfies π₀ T̂ = T π₀.

The suspension meant by the frozen unit roof is the endpoint quotient

    Y = (X̂ × [0,1]) / ((x̂,1) ∼ (T̂x̂,0)).

The flow φᵗ translates the second coordinate, using T̂ or its inverse whenever
an integer endpoint is crossed. The half-open interval [0,1) is only a
representative convention after that quotient. This unpacks the already-fixed
unit roof; it introduces no new clock or arithmetic input.

This is a canonical inverse-limit/history completion of the *whole* frozen
non-invertible rule, not a selected recurrent subset and not a repair of 219's
reset branch.

| Field | Frozen content |
| --- | --- |
| Carrier/type | X̂, a full history/inverse-limit carrier; broadened ANG, not a finite-dimensional symplectic manifold |
| Action | two-sided shift T̂ on all histories; no chosen periodic subsystem |
| Arithmetic mechanism | divisibility and the (n,d,k,e) updates inherited exactly through T |
| Symbolic lineage | divisor admissibility → sequential scan → escape-carry → canonical history completion |
| Projection | X̂→X by π₀; surjectivity is an explicit audit target |
| Clock | unit shift roof only; no inserted log p or prime table |
| Flow owner | the unit-roof endpoint quotient Y with translation flow φᵗ |
| Periodic convention | primitive periods of the full shift action; every phase is retained; k∈ℤ is not quotiented |
| Operator/trace owner | OPEN; no borrowed operator or determinant |
| Classical symplectic owner | NOT APPLICABLE for this broadened card; no Route-A coordinate |
| Stop rule | stop if history completion is empty, loses the arithmetic source, or leaves the inherited prime clock and multiplicity unchanged |

## Frozen controls

1. The non-surjective projection control: a state with no T-preimage cannot
   be the zeroth coordinate of a full history.
2. The periodic-history control: a shift-periodic history must project to a
   T-periodic state, and conversely each T-periodic state has its canonical
   periodic history.
3. The carry multiplicity control: prime cycles occur separately for every
   k∈ℤ; no representative or quotient is selected.
4. The unit-clock control: history completion does not change the number of
   shift steps in a periodic orbit.

Unknown fields remain OPEN; they are not inherited from 219 or from any other
candidate.
