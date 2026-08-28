# C209 evidence and validation plan

## Claim ledger

| ID | Claim | Evidence | Boundary |
|---|---|---|---|
| C1 | K is a bijection and K^2 is rotation by -1 | direct set-partition map for n<=8 | regression only; all-n identity is source combinatorics |
| C2 | fixed formula F_n(d) for every n | attributed type-A Kreweras CSP plus closed binomial reduction | source-derived, not a new theorem |
| C3 | exact periods/cycles/zeta/determinant/spectrum | independent integer Mobius and cycle algebra, n<=24 ledger | finite source only |
| C4 | rank duality and reflection reversor | direct map checks and permutation identities | no arithmetic interpretation |
| C5 | q-Catalan root values | independent SymPy cyclotomic remainders, n<=12 | symbolic regression |

## Reproducible chain

1. Run the producer to regenerate the canonical JSON payload.
2. Run the producer-independent checker (direct enumeration through `n=8`).
3. Run the SymPy cross-check (q-Catalan through `n=12`, closed ledger through
   `n=24`).
4. Run byte replay and the hostile mutation harness.
5. Compile the manuscript with LuaLaTeX in two fixed-epoch passes per round,
   retaining all three round PDFs.
6. Build the self-excluded release manifest and verify every file hash.

All integer operations are exact.  No fitting, target lookup, floating-point
root matching, or external runtime input is permitted.

## Stopping criteria

Any formula/map disagreement, missing row, nonintegral Mobius population,
failed root remainder, failed reflection, nondeterministic producer/PDF, or
accepted mutation stops release.  The route tuple remains conservative even
when all finite checks pass.
