# SD-C21 Exact Experiment Plan

## Frozen question

Can the full-shift semiring skeleton compile trial division into a stationary
countable Markov shift with an exact prime/prime-power primitive ledger and a
same-operator Fredholm determinant, without a prime table or an existential
factor oracle?  If so, does the recurrent dynamics contain more arithmetic
information than a diagonal prime-loop model?

No target-zero data are allowed.  The semiring operations, expanded quotient
search, edge roofs, determinant convention, cutoffs, and controls are frozen
before execution.

## Claim-to-certificate matrix

| ID | claim | exact certificate | GO/STOP rule |
|---|---|---|---|
| E1 | quotient search is local rather than oracle-backed | AST audit plus materialized `Q:n:d:q` states and successor/reject/overshoot edges | `GO_NO_ORACLE` iff all forbidden identifier counts are zero and every Q transition class occurs |
| E2 | the verifier accepts exactly rational primes | independent sieve comparisons at `N=32,64,128,256,512` | `GO_SUPPORT` iff false-positive and false-negative counts are zero at every cutoff |
| E3 | the recurrent core is exactly the accepted loop set | exact SCC census on the expanded graph through `N=24` and Q-state audit through `N=64` | `GO_EXACT_PRIMITIVES` iff recurrent nodes equal `A:p` |
| E4 | power traces and the finite determinant are exact | rational traces through `r=12` at `s=2`; independent Bareiss determinant through `N=8` | `GO_SAME_OBJECT_DETERMINANT` iff every identity is exact |
| E5 | the raw weighted adjacency has an honest `S_1` domain | entrywise trace-norm sums at five cutoffs and four frozen real parts | theorem boundary remains `Re(s)>1`; rows are regression evidence only |
| E6 | the selector depends on the compatible semiring source | transported presentation, entropy shuffle, additive-only, bounded-depth, shifted-target, and random controls | report exact breaks/invariance without fitting |
| E7 | the mechanism is arithmetic-selective | polynomial-UFD and four arbitrary total-decider wrappers | `SELECTOR_TAUTOLOGICAL / PROVES_TOO_MUCH` iff every wrapper reproduces its declared support and diagonal determinant |
| E8 | Route B is ready | source-locked gate audit | always false for this paper |

## Frozen exact protocol

The scientific generator exposes divisor candidates by successor and expands
the cofactor search into states `Q:n:d:q`.  It is forbidden to call a helper
that decides whether a factor exists.  For each Q state the code compares
`d*q` with `n`: equality enters a one-way cemetery ray, strict overshoot
advances `d`, and strict undershoot advances `q`.

The finite graph determinant uses a fixed prefix `N=8` because the explicit
Q graph is intentionally larger than the macro verifier.  The SCC and trace
certificates use `N=24`; support and presentation controls use `N=512`.
Every calculation is integer, rational, deterministic finite graph
arithmetic, or a theorem-ledger real sum.  No root calculation occurs.

## Run order

1. generate exact primary artifacts and the no-oracle certificate;
2. run all thirteen exact regression tests;
3. derive comparison tables and the frozen Route tuple;
4. audit CSV/JSON/YAML schema, LF discipline, scope, and caches;
5. freeze the code/result SHA-256 ledger;
6. repeat the complete run and require byte-identical ledger bytes.

## Reproducibility

From the Paper 19 project root:

```bash
python experiments/run_sdc21_exact_suite.py --verify-byte-determinism
```

The run is CPU-only and requires no GPU, training data, fitted parameter, or
network access.  JSON keys are sorted, CSV column order is fixed, LF is
required, and elapsed-time/timestamp metadata are forbidden.

## Claim boundary

Passing E1 proves implementation-level local quotient search, not emergent
recurrent arithmetic.  Passing E2--E5 proves an exact same-operator Euler
determinant only on `Re(s)>1`.  E7 is the decisive stopping gate: a total
decider can compile any decidable support into the same diagonal periodic
core.  No continuation, Gamma factor, functional equation, Weil form,
critical-zero statement, self-adjoint operator, RH claim, or Route-B claim is
part of the experiment.
