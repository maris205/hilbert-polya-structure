# C104 experiment plan

## Frozen objects

1. Candidate map: \(H_{1/7}(x,y)=(x^3-3x+1/7-y,x)\).
2. Candidate branch intervals: \((-∞,-1),(-1,1),(1,\infty)\).
3. Symbolic pilot: full one-sided shift on three labels.
4. Representative points: \((-2,0,3)\); derivative samples \((9,-3,24)\).
5. Word cutoff: \(n\le6\); no fitted parameters or roots.

## Gates

* G0: freeze the map, labels, representative samples, and determinant
  convention.
* G1: enumerate canonical primitive necklaces and verify the necklace-count
  formula independently.
* G2: reproduce matrix products, determinant-one property, and the primitive
  trace decomposition.
* G3: verify determinant coefficients and Newton identities with SymPy.
* G4: replay canonical bytes and reject semantic mutations.
* G5: compile two isolated deterministic PDFs and inspect fonts/layout.

## Next geometric stage

If this pilot remains useful, the next paper must replace the symbolic full
shift by a certified compact Hénon survivor set, solve periodic equations by
two independent methods, and compare the actual monodromy against the branch
ledger. A mismatch at any primitive length is a stop condition. Only after
that A1 gate may a function-space transfer operator be proposed for A2.
