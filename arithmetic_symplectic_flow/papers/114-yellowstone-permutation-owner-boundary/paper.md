# Yellowstone self-enumeration and its derived permutation cycles have different arithmetic owners

**Paper ID:** `114-yellowstone-permutation-owner-boundary`  
**Record ID:** `ASFS-SCOUT-20260914-81`  
**Date / status:** `2026-09-14; PRE-P0 STOP — HISTORY-DRIVEN ENUMERATION AND DERIVED PERMUTATION CYCLES CANNOT BE IDENTIFIED`  
**Route state:** `No formal ASFS Route-A coordinate; Route B NOT INVOKED`

## 1. Frozen constructions

The Yellowstone sequence begins with \(1,2,3\). At each later step it chooses the least positive integer not previously used that has a common factor with the value two places earlier and is coprime to the immediately preceding value. The source proves that the resulting sequence \(a(n)\) is a permutation of the positive integers.

There are two distinct dynamical presentations which must not be conflated:

1. The **generative action** updates a state \((H,u,v)\), where \(H\) is the finite ordered used history, by appending a new distinct value. Its selection rule is state-internal but its history grows at every step.
2. After the infinite enumeration is constructed, the **derived permutation** \(Y:\mathbb N\to\mathbb N\), \(Y(n)=a(n)\), has an ordinary functional graph. The source reports finite cycles of this permutation, for example \((6,8,14,16,10)\).

The latter is genuine finite recurrence for \(Y\), but it is not a return of the generative history state.

## 2. Exact nonreturn for the arithmetic-generating owner

Let \(U(H)\) be the finite set of values in the used history. The rule selects an unused value, hence every generative update satisfies

\[
 |U(H')|=|U(H)|+1.
\]

After \(r>0\) updates the cardinality increases by \(r\), so the faithful generative state cannot be periodic. Erasing \(H\) creates the derived permutation presentation; retaining a finite cycle of \(Y\) does not restore the historical data that made the least-unused arithmetic selection well-defined. This is an owner distinction, not an assertion that \(Y\) has no cycles.

## 3. Lineage and gate boundary

The construction uses internal gcd/coprimality constraints and no supplied prime table. This is a useful self-selection control. It nevertheless does not define a prime/composite sieve observable, a survivor/admissibility word, or a deformation from such a word to a Logistic/Hénon/conservative carrier. Its source observations about where primes occur in the plot cannot be upgraded to a map-generated prime-symbolic mechanism; several associated asymptotic descriptions in the source are explicitly conjectural.

| Gate | Evidence for this exact screen | Status |
| --- | --- | --- |
| A0 | gcd/coprimality self-selection, but no stipulated prime-symbolic/sieve lineage owner | scoped FAIL for ASFS admission |
| A1 | history action: exact nonreturn; derived permutation cycles: separate owner | scoped owner FAIL |
| A2 | no same-object roof, operator, or determinant | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop and fork.** This screen preserves the useful distinction between a self-generated enumeration and a completed permutation. Future candidates may use neither a growing-history selection process nor its post hoc functional-graph cycles as a substitute for one recurrent, prime-symbolic action.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source record](evidence/README.md)
- [044 Euclid–Mullin growth control](../044-euclid-mullin-graph-screen/paper.md)
- [090 Rowland recurrence control](../090-rowland-gcd-recurrence-nonreturn/paper.md)
- [108 source-action frontier](../108-source-action-frontier-cycle-11/paper.md)
