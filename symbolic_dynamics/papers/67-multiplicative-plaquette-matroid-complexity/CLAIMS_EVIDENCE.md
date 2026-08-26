# Claims and evidence ledger

| ID | Manuscript claim | Evidence type | Dependency | Status |
|---|---|---|---|---|
| C1 | every `n>=1` is uniquely `r a^i b^j` with `a` and `b` not dividing `r` | maximal divisibility exponents; coprimality | `gcd(a,b)=1` | PROVED |
| C2 | a root component satisfies the mixed-difference equation | coordinate substitution | C1 | PROVED |
| C3 | every component solution is `y_ij=u_i+v_j` | rectangle identity from vanishing mixed difference | C2 | PROVED |
| C4 | restriction to `B={n:ab not dividing n}` is a topological-group isomorphism | explicit coordinatewise inverse | C1--C3 | PROVED |
| C5 | an arbitrary finite projection has dimension `sum_r(|I_r|+|J_r|-c_r)` | rank of the vertex-potential map | C3 | PROVED |
| C6 | allowed finite labels are exactly those obeying alternating cycle sums | spanning-forest integration | C5 | PROVED |
| C7 | the vector matroid of the restricted coordinate evaluation maps is a direct sum of graphic matroids | row representation followed by transposition and a vertex-column sign change to an oriented incidence matrix | C5 | PROVED |
| C8 | Haar projection entropy is rank times `log q`; total correlation is cycle rank times `log q` | Haar pushforward to a finite quotient | C5 | PROVED |
| C9 | finite coordinates are jointly independent iff every incidence graph is a forest | entropy additivity together with graphic-matroid acyclicity | C7, C8 | PROVED |
| C10 | every two distinct coordinates are Haar independent | any two distinct edges form a forest in a simple bipartite graph | C9 | PROVED |
| C11 | prefix count is `q^(N-floor(N/(ab)))` | free-coordinate extension/count; internal constraint-row rank as a cross-check | C4 | PROVED |
| C12 | an `M x N` exponent rectangle has count `q^(M+N-1)` | graph is `K_{M,N}` | C5 | PROVED |
| C13 | rectangle total correlation is `(M-1)(N-1)log q` | cycle rank of `K_{M,N}` | C8 | PROVED |
| C14 | the prefix exponential rate is an arithmetic-prefix complexity, not automatically a dynamical entropy | definition/scope firewall | none | PROVED AS TERMINOLOGY |
| C15 | no exact collision was located in the bounded search frozen on 2026-08-25 | primary-source exact-string and neighborhood search | search coverage in `CITATION_AUDIT.md` | PROVISIONAL SEARCH STATUS |
| C16 | priority over all related results | bounded search cannot establish priority | none | NOT CLAIMED |
| C17 | deleting a cycle edge preserves projection dimension, deleting a bridge lowers it by one, and the dual addition laws hold | graphic-matroid rank plus `beta=|F|-d`; eleven deterministic graph transitions | C5, C7 | PROVED AND CONTROLLED |

## Evidence classes

- **Formal:** self-contained lemmas and proofs in the manuscript and
  `PROOF_PACKAGE.md`.
- **Control:** deterministic finite-field rank and enumeration checks in
  `code/verify_plaquette_matroid.py`; these catch implementation and
  transcription errors only.
- **External:** primary literature used for terminology, framework ownership,
  and scope subtraction.

## Release gate

Claims C1--C14 are closed at internal-draft level.  C15 remains bounded and
C16 remains outside the paper.  External release is held for a specialist
search in multiplicative subshifts, algebraic actions, finite-field coding,
and graphic-matroid random fields.
