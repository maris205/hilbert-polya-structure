# Experiment and verification plan — HCS-C126

The computation is a theorem certificate, not a parameter search.

## Claim-to-test matrix

| Claim | Producer receipt | Independent check | Hostile test |
|---|---|---|---|
| \(f^n=T_{3^n}\) for all \(n\) | formal identity plus exact replay through \(n=4\) | fresh composition and Chebyshev reconstruction | alter a replay degree |
| \(3^n\) distinct real roots | exact two-family proof and multiplier classes | recomputed family counts and derivatives | replace “distinct” by multiplicity-only |
| unique fiber closure | closed geometric-sum formula | denominator and source convention checks | set multiplier to one |
| primitive/orientation counts | Möbius rows through \(n=12\) | separately implemented divisors and Möbius function | corrupt two nontrivial rows |
| \(\zeta_F=(1-3z)^{-1}\) | exact trace series | independent symbolic identity | replace 3 by 2 |
| all-period stability/repetition | exact triangular derivative theorem | multiplier/count reconstruction | corrupt an orientation row |
| controls fail structurally | exact factorizations | fresh SymPy factorization | claim nine distinct control roots |
| route boundary | canonical tuple and nonclaims | exact equality checks | promote A1/A2 or authorize Route B |

## Commands

```text
python3 code/c126_chebyshev_skew_producer.py
python3 code/c126_chebyshev_skew_checker.py
python3 code/c126_sympy_crosscheck.py
python3 code/c126_replay.py
python3 code/c126_mutation.py
```

## Release checks

1. Build the LaTeX paper twice in fresh directories with a frozen date.
2. Require byte equality between both builds and the checked-in PDF.
3. Require embedded fonts and a final log free of layout, reference, citation,
   and package warnings.
4. Render every page and inspect for clipping, collision, blank regions, and
   broken formulas.
5. Generate the content-addressed manifest only after the final paper and all
   reports are stable; require exact ledger closure.

## Stopping rule

The package is incomplete if any all-period statement is supported only by its
finite replay prefix, if either negative control is merely numerical, or if the
strict tuple is promoted by the source zeta alone.
