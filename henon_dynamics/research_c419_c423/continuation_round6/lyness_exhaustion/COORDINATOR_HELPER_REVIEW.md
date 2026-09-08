# Non-author coordinator review of the sixth-pass LY4 helper

2026-09-08 UTC. Current-team internal mathematical review, not external
peer review. The coordinator did not author the reviewed identities or
segment. This review is narrow and does not certify the original full LY4
classification, which remains unproved.

## Actual inputs and method

Read all 205 lines of [PROOF_PACKAGE.md](PROOF_PACKAGE.md) and all 47 lines
of [SCOUT_REPORT.md](SCOUT_REPORT.md). Reviewed proof SHA-256:
`0b676ed86b70e0fba23010984fa9e7e5122d403b5deb41dffff3fcc6a79fcdaf`.
Checked the new algebra by direct substitution and subtraction, without
executing a mathematical program or rerunning accepted fifth-pass proofs.
The inherited rational-clock case bounds are used with their existing
review, not certified afresh here.

## Findings

1. The factorization is correct. With seven coordinates $(x,y,z,w,v,t,s)$,
   the recurrence gives $w(s-x)=v+t-y-z$ and $zt-yv=v-z$.
   Therefore $z(t-y)=(y+1)(v-z)$, and substitution gives
   $zw(s-x)=(y+z+1)(v-z)$ with no illegal cancellation. The relation
   $D_i=E_i+E_{i+2}+E_{i+4}$ then gives the stated second-order difference
   equation. It is not itself a contraction on the six-step differences.
2. Both midpoint equations follow from
   $ab-a'b'=\frac{a+a'}2(b-b')+\frac{b+b'}2(a-a')$.
   The invariant coefficient is unchanged after six indices by its
   two-periodicity. The signed equations do not justify a positive
   maximum principle. For the allowed two-period word $(3,8)$ the
   even invariant is indeed $2$ and the displayed triangle ratio is $4$.
3. All five recurrence equations in the eight-entry segment are correct,
   and its first two invariants are $9$ and $6m+3$. At its first index,
   the two-step difference is $3$, the six-step difference is $3m+3$,
   and the multiplier is $m+1$. This disproves the stated *local*
   bounded-multiplier inference only.
4. The explicit failure to extend integrally is also correct:
   $x_8=4+(2m-4)/(5m+2)$ is integral for positive $m$ only at $m=2$.
   At that parameter the segment is
   $(26,9,2,2,5,24,35,20)$, followed by $4$ and $13/7$.
   Hence it is not an integer periodic counterexample, and the author's
   distinction between the local obstruction and the unproved global
   hypothesis must be retained.
5. Given the already accepted case bounds quoted in the proof, solving
   $m=N/\gcd(N,2)$ and deleting the classified low-period/eight-period
   cases yields the displayed residual candidate list. It is only an
   upper list of allowed clocks, with no assertion of existence or of
   finiteness in the coefficient/height variables.

## Verdict and unresolved work

**PASS for the new identities, segment and its failed extension; no
must-fix issue found within that scope.** This is not a PASS for LY4,
hypothesis S, exhaustion E, or a finite residual core. The global cyclic
arithmetic implication and the complete return classification through
$\{1,-2\}$ remain missing. No new admission follows from these helpers.

The proof-writer requirement to keep the original claim separate from
proved auxiliary statements materially controls this verdict. No new
source query, mathematical execution, manuscript, formal evaluation or
target-arithmetic promotion is attached to this review.
