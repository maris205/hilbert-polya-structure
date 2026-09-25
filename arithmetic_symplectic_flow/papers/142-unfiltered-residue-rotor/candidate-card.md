# Broadened carrier card — ANG-20260915-URR01

**Version:** 1, 2026-09-15; frozen before mathematical audit or computation.  
**Initial status:** BROADENED HYPOTHESIS — T0--T3 OPEN.

Freeze the entire discrete space

\[
Y=\{(n,a,j): n\geq2,\ 1\leq a<n,\ j\in\mathbb Z/n\mathbb Z\},
\qquad F(n,a,j)=(n,a,j+a\bmod n).
\]

There is NO coprimality condition on a, no selected prime modulus, and no
prime-indexed initial state. All states, including nonunits, are kept.

| Field | Frozen specification |
| --- | --- |
| Lineage | Prime/composite divisibility exclusion -> modular return congruence for every nonzero increment; audit the equivalence instead of importing a prime predicate |
| Contrast | Not 065's adjacent-coprime shift and not a prefiltered unit rotation; no static removal of composite increments |
| Carrier / action | Exactly Y and F; proposed transformation groupoid by Z once invertibility is checked |
| Arithmetic inputs | All positive integer sizes n>=2, all nonzero residue increments, ordinary addition and reduction; no prime table or fitted data |
| Observable | Full n,a,j state; subgroup-return length of the same addition action |
| Roof / flow | Unit roof, (z,1) identified with (Fz,0); full suspension |
| Primitive packets | All least-period full F-orbits, all n and a retained, cyclic phases identified once, no reversal quotient |
| Arithmetic question | Does complete period structure in a fibre intrinsically distinguish prime n from composite n? Is that distinction more than an external label? |
| Analytic proposal | Ordinary unweighted product over the complete primitive ledger only if multiplicity and convergence permit; operator/domain/trace OPEN |
| Controls | Nonunit increments, prime increments, arithmetic removal, cross-n packet multiplicity, dilation/congruence aliases |
| Early decisive checks | Full inverse and primitive period; prime/composite return criterion; finite versus infinite multiplicity at one fixed length |
| Stop condition | Stop immediately if the full ordinary product has infinite fixed-length multiplicity; do not prefilter units, select a primitive sublattice, or assign a new roof to repair it |
| Classical fields | Finite-dimensional symplectic base, contact/Hamiltonian and quantum owner NOT APPLICABLE / NOT SUPPLIED |
| Route | Broadened T0--T3 only; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

This is a separate definition derived from a proposed residue-rotation seed
by retaining, not deleting, every nonzero slope. No assertion about its
periods, arithmetic selectivity or analytic product is assumed at the freeze.

## Version-1 audit append — 2026-09-15

**Current status:** STOP — NATIVE ARITHMETIC RETURNS; INFINITE TWO-PACKET MULTIPLICITY.  
**Portfolio:** fork.

The [paper](paper.md) proves F invertible and gives its complete periods
n/gcd(n,a), with gcd(n,a) primitive packets for each (n,a). Prime n is
equivalent to all packets in the complete n-fibre having period n.
This is native arithmetic return, not a prefiltered prime or unit carrier.

The same unit roof makes these the primitive flow lengths and gives
repetitions r times that length. For every k>=1 the allowed pair n=2k,a=k
supplies k two-packets. The resulting infinite length-two multiplicity
forces divergence of the ordinary unweighted product at every real s>0.
The precommitted stop therefore applies immediately.

T0 and T2 are ESTABLISHED. T1 is ESTABLISHED for divisibility-dependent
returns and the full-fibre prime/composite criterion, with no unique prime
packet or prime-log clock claimed. T3 is SCOPED FAIL for the ordinary
product; operator/domain/trace remain NOT SUPPLIED. No state was removed,
no packet identified across moduli, and no roof or owner changed.
Classical fields remain NOT APPLICABLE; formal Route coordinates UNASSIGNED;
Route B NOT INVOKED.
