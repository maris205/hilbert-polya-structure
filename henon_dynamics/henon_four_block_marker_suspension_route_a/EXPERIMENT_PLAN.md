# C139 exact validation plan

## Claim/evidence matrix

| Claim | Infinite proof | Finite sentinel | Independent failure test |
|---|---|---|---|
| eight-state determinant | cofactor derivation | seven-monomial receipt | SymPy determinant |
| trace/product for every period | path bijection and formal logarithm | periods 1–12 | state-path DP versus word enumeration |
| memory-3 impossibility | periodic sums are block-count dot products | explicit period-6 pair | recompute width 1–4 counts |
| five-basis sector separation | multiquadratic independence proof | pair clock vector | SymPy embedding rank |
| residual noninjectivity | explicit primitive nonrotation pair | first collision through period 7 | necklace and rotation reconstruction |

## Execution

1. Run the producer and freeze canonical JSON bytes.
2. Run the standard-library checker, which imports no producer code.
3. Run the SymPy determinant/trace/basis reconstruction.
4. Replay the producer into a temporary path and demand byte identity.
5. Run all repaired-hash semantic mutations and the stale-hash control.
6. Compile and retain round 0, review/fix round 1, review/fix round 2/final.
7. Perform two fresh fixed-epoch builds, font inspection, warning scan, and
   rendered-page visual inspection.
8. Generate a manifest only after exactly 27 payload files exist.

## Stop rules

Downgrade or stop if the determinant differs, the witness shares its marker
count, any infinite identity depends on the period-12 replay, a repaired-hash
mutation is accepted, the PDF is nondeterministic or visually defective, or
any target/arithmetic/Route-B claim enters the package.
