# History completion of the escape-carry screen

**Paper ID:** 221-natural-extension-carry  
**Candidate ID:** ANG-20260918-HIC01  
**Date:** 2026-09-18.  
**Status:** T0/T2 ESTABLISHED; T1 PARTIAL; STOP — SQRT CLOCK AND k MULTIPLICITY.  
**Evidence class:** direct symbolic proof from the frozen rule; no numerical search.

## 1. Scope and object

Candidate 219 froze a deterministic map T on states x=(n,d,k,e), with n,d≥2,
k∈ℤ and e∈{0,1}:

1. e=0, d²≤n and d does not divide n: (n,d,k,0) → (n,d+1,k,0);
2. e=0, d²≤n and d divides n: (n,d,k,0) → (n+d,d+1,k+1,1);
3. e=0 and d²>n: (n,d,k,0) → (n,2,k,0);
4. e=1: (n,d,k,1) → (n+1,2,k,0).

This paper does not alter that rule. It takes its full bi-infinite history
carrier

    X̂ = { (xⱼ)ⱼ∈ℤ : T(xⱼ)=xⱼ₊₁ for every j },

and its two-sided shift T̂, (T̂x̂)ⱼ=xⱼ₊₁. The carrier is a broadened ANG
history/inverse-limit object, not a finite-dimensional symplectic manifold or
a selected periodic subsystem.

The exact lineage is the prior-work prime/composite observable and
divisor-admissibility rule, deformed to a sequential scan in 219 and now
completed by two-sided histories. No claim is made to have completed the
Logistic/Hénon-to-positive-dimensional-symplectic arrow.

| Same-object row | Owner and boundary |
| --- | --- |
| Carrier and base action | full X̂ and its two-sided shift T̂ under ANG-20260918-HIC01 |
| Arithmetic source | exactly the four divisor-scan/carry branches of T above |
| Coding and projection | x̂=(xⱼ); π₀ T̂=T π₀, but π₀ need not be onto |
| Clock and flow | roof τ≡1 and endpoint quotient Y=(X̂×[0,1])/∼, with (x̂,1)∼(T̂x̂,0) |
| Primitive/repetition convention | all shift orbits and their unit-roof flow orbits, with every k-copy retained |
| Classical symplectic/Hamiltonian owner | NOT APPLICABLE; not asserted |
| Operator, measure, trace, zeta/determinant | OPEN / NOT SUPPLIED; none borrowed |

## 2. The shift is genuinely invertible

The inverse is (T̂⁻¹x̂)ⱼ=xⱼ₋₁. Both maps are continuous for the product of
discrete topologies, and the defining relation T(xⱼ)=xⱼ₊₁ is preserved by
either shift. Hence T̂ is a homeomorphism of X̂, even though the projection
π₀:X̂→X need not be onto and T itself is not injective.

The projection obstruction is concrete. The state (2,3,0,0) has no
T-preimage: an output with d=3 would have to come from the non-divisor branch
at d=2, which requires 2²≤2, and the divisor branch outputs e=1. Therefore
(2,3,0,0) is not π₀(x̂) for any history. Any point in π₀(X̂) necessarily
belongs to Tʳ(X) for every finite r and, more strongly, its predecessors must
fit one coherent bi-infinite chain; no converse from finite-depth
predecessors is assumed. Thus history completion repairs invertibility only on
the surviving history carrier; it does not retain every original state.

## 3. Monotone n forces the complete history to be prime-periodic

Let x̂=(xⱼ) be any history, and write nⱼ for the n-coordinate of xⱼ. Every
branch of T leaves n unchanged or increases it, and branches 2 and 4 increase
it strictly. Consequently nⱼ is nondecreasing in j. For j≤0 it is bounded by
n₀, so an integer-valued monotone sequence can have only finitely many strict
increases. There is J and an integer N such that nⱼ=N for all j≤J.

On this constant-n tail, branches 2 and 4 are impossible. The tail therefore
uses only branches 1 and 3, has e=0, and keeps k fixed. If N is composite, a
scan starting at d=2 reaches a divisor d≤√N after finitely many non-divisor
steps (with branch 3 returning any overshoot to d=2), forcing branch 2. This
contradicts constant n. Hence N is prime.

For a prime p set q=floor(√p). The only bi-infinite fixed-p scan is

    (p,2,k,0) → (p,3,k,0) → … → (p,q+1,k,0) → (p,2,k,0),

with the evident one-state interpretation when q=1. Since the forward rule is
deterministic, once the history tail lies on this cycle, every later
coordinate remains on it. Therefore every history in X̂ is exactly a periodic
prime scan history. There are no nonperiodic histories.

This is an intrinsic consequence of taking the full history space, not a
manually selected recurrent subset. It also answers the retention question:
nonperiodic states of the original X are not retained; indeed no nonperiodic
history survives.

## 4. Complete periodic ledger and carry multiplicity

Every prime p and every k∈ℤ supplies one cycle

    C_{p,k} = { (p,d,k,0) : 2≤d≤q+1 },   q=floor(√p),

whose primitive period is q. Each phase of C_{p,k} gives one shift-periodic
history, and the q phases form one primitive shift orbit. Conversely, if a
history is shift-periodic of period m, its zeroth coordinate is T-periodic;
the monotonicity argument above forces it into exactly one C_{p,k}. Hence
these are all periodic histories, with no hidden extra histories from the
non-injective reset.

For fixed p there is a separate primitive orbit for every k∈ℤ. The history
completion therefore preserves the countably infinite carry multiplicity
instead of quotienting it away. The primitive period remains q=floor(√p)
under the frozen unit shift clock. No log p value is generated by the
history construction.

### Unit suspension and full repetition law

In the endpoint quotient Y from the card, define
φᵗ([x̂,u])=[T̂ᵐx̂,u+t−m], with the integer m chosen so 0≤u+t−m<1.
The endpoint identification makes this independent of the representative.
Since T̂ is invertible and τ≡1, the formula defines a complete flow for every
real t; forward and backward accumulated roof times diverge, so there is no
Zeno defect.

A closed flow orbit must return to the zero-height section after an integer
number of roof crossings, and its return is precisely a shift return.
Therefore the full primitive flow ledger consists of one γ_{p,k} for each
prime p and k∈ℤ, with

    T_{γ_{p,k}} = floor(√p),    T_{γ_{p,k}^r} = r floor(√p),  r≥1.

There is no reversal quotient or selection of one phase as an extra orbit.
The flow has no further closed or nonclosed orbits, because all of X̂ was
classified above. This is a topological suspension of the broadened carrier,
not a classical symplectic-suspension admission.

## 5. Broadened audit and stop

| Audit | Result | Boundary |
| --- | --- | --- |
| T0 carrier/type and ownership | PASS | X̂ and T̂ are one explicitly defined ANG object |
| T1 endogenous arithmetic/clock | PARTIAL PASS | divisibility source is inherited exactly; unit clock remains sqrt-scale |
| T2 packet, primitive convention, repetition | PASS | exactly one prime cycle for each (p,k), with all phases and repetitions |
| T3 same-object operator/trace | OPEN / not supplied | no operator, zeta, or determinant was frozen |

The construction repairs the semigroup's local noninvertibility at the history
level and gives a clean prime-only periodic ledger. It does not improve the
clock or the carry multiplicity, and it removes every nonperiodic history.
Under the frozen stop rule this is a decisive broadened-track STOP/FORK, not a
formal Route-A result. A future fork would have to derive a different clock or
a principled carry quotient from the same source; inserting log p or selecting
one k is forbidden.

No Route-A coordinate was evaluated. Route B is not invoked.

## 6. Controls and reproducibility boundaries

The controls are exact, with no cutoff or floating-point precision:

- Arithmetic negative control: a composite constant-n tail must hit a
  divisor and cannot be a full history.
- Projection/ownership control: (2,3,0,0) has no predecessor; the extension
  must not be advertised as retaining all original transient states.
- Multiplicity control: k is unchanged on every surviving history; selecting
  k=0 would be a new quotient/selection, not the frozen object.
- Clock control: τ≡1 fixes every primitive time above; a log p roof would
  change the candidate.
- PROVES_TOO_MUCH boundary: two-sided history completion is invertible for
  any deterministic rule. Invertibility itself is not arithmetic evidence;
  the prime-only classification uses the specific divisor test.

The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
and [evidence record](evidence/README.md) contain the identity and exact
proof/check scope. There is no external-source or numerical claim.
