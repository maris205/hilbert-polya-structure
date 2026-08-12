# Research Question Brief

## Topic area

Global critical-value geometry of the area-preserving Hénon family, with
chronological periodic orbits retained and with the C32 Morse-local
information loss used as the starting obstruction.

## Primary research question

> Does the irreducible degree-nine equal-action collision locus of the exact
> period-five Hénon action carry a nontrivial quadratic Kummer cover whose
> fibers exactly detect whether the two colliding Morse-local factors have the
> same Hill-determinant square class?

## FINER assessment

| Criterion | Score | Justification |
|---|---:|---|
| Feasible | 5/5 | The exact marker, action remainder, Hill polynomial, collision field, and four split-prime controls are already computable by resultants and quotient-ring arithmetic. |
| Interesting | 5/5 | It converts C32's local loss of Hill information into a global arithmetic obstruction/repair mechanism. |
| Novel | 4/5 | The marker normalization and ordinary period-five Galois group are prior work; the action-node divisor coupled to the Hill square-class cover is search-bounded and still requires a Phase-2 primary-source audit. |
| Ethical | 5/5 | Pure mathematical and reproducible computational research; no human or sensitive data are involved. |
| Relevant | 5/5 | The answer decides whether global Hénon parameter monodromy retains arithmetic stability data erased by isolated Morse germs. |
| **Average** | **4.8/5** | No criterion falls below the continuation threshold. |

## Scope boundaries

### In scope

- the one-parameter area-preserving family
  \(H_A(q,p)=(1-Aq^2-p,q)\), equivalently the Hamiltonian recurrence after
  the exact scaling \(x=Aq\);
- exact period five and its six reversible cyclic orbits;
- the cyclic generating action \(\Phi_{5,A}\), modulo additive constants,
  cyclic coboundaries, and nonzero common rescaling;
- the plane action curve \(W_5(A,c)=0\), its normalization, its degree-nine
  equal-action node locus, its \(S_9\) parameter monodromy, and its local
  branch monodromy;
- the intrinsic Hill value \(\det(I-DH_A^5)\) on the two colliding branches;
- the descended square class \([N_H]=[h_1h_2]=[h_1/h_2]\);
- characteristic-zero exact proofs and explicitly declared good-prime
  specializations.

### Out of scope

- another fixed-parameter Galois-group table for the old marker cover;
- periods \(n>5\) before the period-five mechanism is closed;
- numerical fitting to Riemann zeros, prime gaps, or a target spectral line;
- identifying Frobenius degree with Hénon period;
- replacing chronological dynamics by an averaged transition matrix;
- claiming that a node/Kummer cover is already a Ruelle determinant,
  Picard--Lefschetz representation, or Hilbert--Pólya operator;
- Route B unless a later formal candidate explicitly passes the Route-A
  screening boundary.

## Key assumptions to test rather than presume

1. The degree-nine factor is not part of the old orbit-cover ramification.
2. Its generic plane singularity is an ordinary transverse double point.
3. Both colliding critical points remain nondegenerate on its generic point.
4. The symmetric Hill product is a canonical square-class invariant under
   branch exchange and common normalization.
5. That square class is nontrivial in the degree-nine number field.
6. No primary source has already computed this precise action-node/Hill
   Kummer cover.

## Sub-questions

1. What is the exact factorization of the action-curve discriminant, and how
   does it separate old periodic-point ramification from new equal-action
   self-intersections?
2. What is the arithmetic monodromy of the degree-nine collision parameters,
   and is the generic singularity over \(P_9=0\) a transverse node with two
   distinct nonparabolic exact period-five branches?
3. Does the Hill product \(N_H\) define a nonsquare class in the collision
   field, and do its finite-prime specializations reproduce both the C32
   collapse and a matched noncollapse control?

## Sub-question bindings

1. **Inherits:** family \(H_A\); exact period five; action observable;
   characteristic zero. **Deviations:** none.
2. **Inherits:** the same family, period, and degree-nine component; excludes
   lower-period and parabolic loci. **Deviations:** none.
3. **Inherits:** the same collision field and intrinsic Hill polynomial;
   finite fields are used only at declared good split primes. **Deviations:**
   none.

## Candidate questions considered

| Candidate | FINER average | Decision |
|---|---:|---|
| Period-five equal-action Hill Kummer cover | 4.8 | **Selected.** It directly globalizes the C32 obstruction and already has a theorem-level nonsquare pilot. |
| Full period-six exact-cover monodromy inside its maximal dihedral centralizer | 4.0 | **Reserve big door.** Substantial, but overlaps C12C/C21 and needs a larger reconstruction engine. |
| Raw parabolic discriminants for \(2\le n\le6\) | 3.2 | **Rejected as framed.** Low-period elimination and marker discriminants duplicate prior work unless coupled to a new invariant. |
