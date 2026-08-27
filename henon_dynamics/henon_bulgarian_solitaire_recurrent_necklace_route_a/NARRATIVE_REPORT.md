# C190 narrative report

## Material progress

C190 is one complete all-`N` noninvertible partition-dynamics paper, not one
fifth of a larger manuscript.  It starts from Brandt's strongest exact input:
recurrent Bulgarian-solitaire states are a fixed-weight binary-word layer and
the dynamics is rotation.  From that point it closes the entire periodic
ledger, the full finite zeta, and more than the recurrent spectrum: the full
Koopman algebraic spectrum includes a zero eigenvalue of multiplicity
`p(N)-binom(k,r)` contributed by transient vertices.

The reflection result is stated at the correct level.  `Q rho Q=rho^-1`
holds on the recurrent word layer, with `rho^a Q` giving `k` phase-labelled
formulas.  They need not be distinct on a nonfaithful weight layer, and no
global reversor is claimed for the noninvertible full map.

## Evidence separation

The infinite quantifier belongs to the cited Brandt/Akin--Davis theorem plus
the written combinatorial and linear-algebra proofs.  The checker separately
constructs all 215,307 partitions for `N<=40`, rather than reading the
producer's word list.  This is a strong convention and implementation oracle,
but it remains finite regression.

## Deliberate stopping boundary

The algebraic spectrum needs only the number of transient vertices, not the
shape of their trees.  Complete functional trees, exact hitting-time
distributions, and nilpotent Jordan sizes are therefore excluded rather than
silently inferred from the finite census.  That boundary prevents this paper
from becoming a fragment of a second transient-combinatorics project.

## Route-A conclusion

Primitive cycles are exact and the recurrent restriction is a natural finite
unitary, but neither carries intrinsic rational-prime semantics or a target
divisor.  The full Koopman map is nonunitary.  The strict verdict is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall rejected, Route B
false.
