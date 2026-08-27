# C194 test report

All commands were run from the package root under Python 3 with exact integer,
`Fraction`, or SymPy arithmetic.

## Producer

```text
python3 code/c194_holte_producer.py
```

Result: `C194_PRODUCER_PASS`; 72 cases, 1,836 transition cells, 392 semigroup
tuples, 96 power-identity tuples; payload
`15c02c5b83f6314fef0e3c786f7bdad09feeb1d7a557b7df7bd88db30eb3106f`.

## Independent checker

```text
python3 code/c194_holte_checker.py
```

Result: `C194_CHECKER_PASS`; 24,602 assertions.  The checker imports no
producer code.  It uses Holte's slack-variable coefficient with
inclusion--exclusion, enumerates descents of all permutations through `n=8`,
and uses Faddeev--LeVerrier rather than the producer's spectral product.

## SymPy oracle

```text
python3 code/c194_sympy_crosscheck.py
```

Result: `C194_SYMPY_PASS`; 14,248 checks: 2,488 matrix/stationary checks, 792
coefficient checks, 5,544 trace checks, 2,160 eigenspace checks and 3,264
semigroup checks.

## Byte replay

```text
python3 code/c194_replay.py
```

Result: `C194_REPLAY_PASS`; 537,471 bytes, SHA-256
`b165dd9ae0b60009db7c9489d969a6910500bb5aec72fea1ec226cf147e43b18`.

## Semantic mutation

```text
python3 code/c194_mutation.py
```

Result: `C194_MUTATION_PASS`; 159 repaired-hash semantic attacks and one
stale-hash attack rejected.

## Paper build

Each round used two XeLaTeX passes with

```text
SOURCE_DATE_EPOCH=1787788800 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
```

Two further fresh directories, each seeded only with final `main.tex`, produced
the same final SHA-256
`9351c9ed695028aa34aa1abc2302c00bfa8c687e03f015c58c6309517b028cc7`.
The final pass-2 log examined at build time and both fresh pass-2 logs have no
warning, undefined reference, missing character, overfull/underfull box,
badness, fatal message or error.
All fonts are embedded and subsetted.  Both pages were rendered and visually
inspected.

## Proof boundary

The finite census validates implementations.  Holte 1997 owns the infinite
transition, semigroup and diagonalization theorem; Diaconis--Fulman 2009 owns
the cited convergence analysis.
