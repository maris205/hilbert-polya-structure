# SD-C22 Exact Experiment Plan

## Frozen question

Close the explicitly expanded Paper 19 \(I/T/Q\) prime-verification path into
one vertex-disjoint recurrent cycle per accepted input by contracting the
acceptance boundary to
\(T_{p,\lfloor\sqrt p\rfloor+1}\to I_p\). If every accepted cycle has a
nonnegative edge roof with exact total \(\log p\), can its natural weighted
vertex adjacency be compact or trace class, and does first return preserve
the same marked determinant?

No prime/factor oracle is allowed in graph generation. No target-zero data,
root fitting, Route-B operator, or cross-family construction is allowed.

## Claim-to-certificate matrix

| ID | claim | exact certificate | GO/STOP rule |
|---|---|---|---|
| E1 | quotient search remains explicit and oracle-free | source audit plus materialized Q states through 64 | GO_NO_ORACLE iff forbidden macros are absent and Q states occur |
| E2 | contracted cycle length is exact | formula and independent transition traversal for all 564 primes through 4096 | GO_CYCLE_CENSUS iff every row agrees |
| E3 | exact total clock forces clock dilution | \(\ell(p)/\log p\) and optimal maximum edge weight at \(\sigma=1,2\) | STOP_COMPACTNESS by the distribution-free theorem; rows are witnesses |
| E4 | raw primitive and repetition ledgers are exact | exact rational block products and power traces for primes through 31 | GO_ORBIT_LEDGER iff every certificate agrees |
| E5 | raw and induced time markers differ | exact products at \(z=1\) and \(z=1/3\) | POINCARE_COLLAPSE iff equality holds only at the unmarked specialization |
| E6 | source-summable roofs repair trace class only by changing the clock | source-roof total divided by \(\log p\) | STOP_SOURCE_CLOCK when distortion grows |
| E7 | the obstruction is arithmetic-selective | padded square, power-of-two, Fibonacci, and seeded-hash deciders | PROVES_TOO_MUCH when all reproduce the same limiting edge-weight failure |
| E8 | Route B is ready | frozen source gate | always false |

## Frozen protocol

- Inputs: \(2\le n\le4096\).
- Formula: \(\ell(p)=2+\sum_{2\le d\le\lfloor\sqrt p\rfloor}\lceil p/d\rceil\).
- Witness cutoffs: 31, 127, 509, 2039, and 4093.
- Exact determinant prefix: primes through 31, \(s=2\), \(z\in\{1,1/3\}\).
- Exact power traces: first four nonzero repetitions of every prime block
  through 31.
- Spectral witnesses: \(\sigma\in\{1,2\}\).
- Universal controls: cutoff 4096 with padded runtime \(n^2+2\).
- Independent sieve: sealed validation only, never graph construction.

The theoretical compactness gate ranges over every nonnegative distribution
of total roof \(\log p\). Uniform roofs only attain the smallest possible
maximum edge weight and therefore provide the strongest finite witness.

## Run order

1. generate cycle, spectral, marker, source-clock, and universal-control data;
2. run all exact tests, including the no-oracle and endpoint audits;
3. derive the strict Route tuple;
4. audit CSV/JSON/YAML, target-zero fields, scope, provenance, and caches;
5. freeze the code/result SHA-256 ledger;
6. rerun and require byte-identical ledger bytes.

## Reproducibility

From the Paper 20 project root, run:

    python experiments/run_sdc22_exact_suite.py --verify-byte-determinism

The suite is CPU-only and uses no training data, GPU, network, stochastic
fitting, or target roots. JSON keys and CSV columns are deterministic, all
text uses LF, and runtime/timestamp fields are forbidden.

## Claim boundary

Finite witnesses audit exact formulas; they do not empirically prove the
infinite obstruction. The theorem applies to the natural vertex
\(\ell^2\)-space and vertex-disjoint recurrent verifier cycles. It does not
exclude overlapping recurrent grammars, cancellation-valued weights,
semifinite determinants, or nonstandard spaces that remove the cycle modes.
