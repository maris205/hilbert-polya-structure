# C215 evidence and validation plan

## Claim ledger

| ID | Claim | Evidence | Boundary |
|---|---|---|---|
| C1 | partition-valued owner and Bell counts | independent partition enumerator through `n=8` | finite enumeration is regression only |
| C2 | all-`n` block rates and hypoexponential transitions | 312 exact-grid rows, row sums, Chapman--Kolmogorov | formula is source-level theorem |
| C3 | independent holdings and MRCA law | rate/mean/variance rows and transform derivatives | projective coupling stated separately |
| C4 | total branch length and exact CDF | 60 rows, order-statistic beta-integral SymPy proof | `n=1` convention explicit |
| C5 | infinite absorption and determinant firewall | limit row, monotone coupling prose, hostile mutations | no Artin--Mazur claim |

## Reproducible chain

1. Generate the canonical JSON certificate with fixed 100-digit arithmetic.
2. Run the producer-independent recursive checker; it recomputes every
   transition, semigroup identity, moment, partition count, and CDF.
3. Run the SymPy partial-fraction, derivative, beta-integral, and limit checks.
4. Run clean-process byte replay and hostile repaired-hash, stale-hash, and
   unknown-key mutations.
5. Compile the manuscript with LuaLaTeX at a fixed epoch, preserving three
   substantively different revision PDFs.
6. Build the self-excluded release manifest and verify file hashes, text,
   fonts, page count, and sidecar closure.

No fitting, prime lookup, zero matching, or external runtime input is allowed.

## Stopping criteria

Any partial-fraction disagreement, non-stochastic row, failed Chapman--
Kolmogorov identity, wrong branch CDF/moment, mistaken projective limit,
nondeterministic producer/PDF, or accepted mutation stops release.
