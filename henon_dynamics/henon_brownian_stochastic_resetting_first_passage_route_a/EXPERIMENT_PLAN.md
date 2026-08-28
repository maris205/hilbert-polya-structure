# C214 evidence and validation plan

## Claim ledger

| ID | Claim | Evidence | Boundary |
|---|---|---|---|
| C1 | free renewal propagator and erfc integral | producer rows; independent quadrature checker | grid is regression, formula is analytic |
| C2 | free stationary Laplace density is normalized | stationary and normalization rows; two-sided quadrature | not a killed-process stationary law |
| C3 | killed FPT/survival transforms | exact SymPy renewal algebra and 108 rows | reset/target convention frozen |
| C4 | MFPT and all-moment derivative identities | transform derivative, zero-limit checks, symbolic Taylor jet | finite moments rely on positive parameters |
| C5 | unique positive optimal rate and boundaries | root residual, sign bracket, boundary ledger | no arithmetic interpretation |

## Reproducible chain

1. Generate the canonical JSON payload with fixed 100-digit arithmetic.
2. Run the producer-independent checker; it computes the reset integral by
   quadrature after the substitution `u=y^2` and checks every row/schema key.
3. Run the SymPy cross-check for the heat equation, renewal identity,
   transform relation, moments, and optimum.
4. Run clean-process replay and hostile repaired-hash, stale-hash, and
   unknown-key mutations.
5. Compile the manuscript with LuaLaTeX at a fixed epoch, retaining three
   substantively different revision PDFs.
6. Build the self-excluded release manifest and check hashes, text, fonts,
   page count, and sidecar closure.

No fitting, prime lookup, zero matching, or external runtime input is allowed.

## Stopping criteria

Any formula disagreement, failed normalization, mistaken realization boundary,
bad transform/moment sign, nondeterministic producer/PDF, overfull layout,
missing citation lock, or accepted mutation stops release.
