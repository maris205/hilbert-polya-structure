# Claims and evidence — P134

| theorem claim | all-parameter proof | paper-local exact control |
|---|---|---|
| image equals all valid border arrays | first-occurrence standardization preserves equality patterns and lies in `E_n` | closure and literal-vs-linear borders through `n=8`; image profiles through `n=9` |
| exactly `n-1` two-cycles for `n>=2` | direct `A_r <-> B_(r+1)` inspection plus strict mismatch-prefix growth | every recurrent state and period through `n=9` |
| valid depth at most `2n-5`, global depth at most `2n-4` | exhaustive indexed mismatch lemma and one-step entry into the valid image | every valid table/state through `n=9` |
| sharp maximum `0,0,1,2n-4` | explicit `e_n -> p_n` trajectory with one coordinate gained every two steps | full graphs through `n=9`; witness formulas through `n=32` |
| every target fibre at most `(n-1)!` | target-wise left-to-right exposure, including zero fibres of invalid targets | every target in `E_n` through `n=9` |
| only `0^n` and `010^(n-2)` maximize for `n>=2` | equality in the exposure bound plus proper-suffix-start exclusion | exact maximizer sets through `n=9` |

The verifier is deterministic, dependency-free, and uses exact Python
integers.  Enumeration is counterexample pressure; it does not substitute for
the proofs in `main.tex`.

## Credit subtraction

The following receive zero contribution credit: KMP/Morris--Pratt border
recursion, failure-link composition, border-array validation and construction,
minimum-alphabet realization, valid-array generation/census, the
inversion-sequence carrier, and generic finite-map/fibre terminology.

The bounded direct-owner non-hit is recorded only as a search result.  External
novelty, priority, authorship, posting, submission, and release remain on hold.

