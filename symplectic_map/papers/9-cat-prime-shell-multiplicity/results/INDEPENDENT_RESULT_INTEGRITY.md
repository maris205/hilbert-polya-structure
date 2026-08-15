# Independent Result-Integrity Review

Date: 2026-08-14 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Reviewer role: fresh independent post-run authority  
Decision: **PASS**

## Review boundary

I reviewed the frozen source/design bindings, deployment authority, raw
registered result, lifecycle records, post-run JUnit, and both official
reports.  I did not import any Paper-9 module, invoke the candidate, call a
registered-run entry point, build the result manifest, or modify any prior
artifact.  The scientific checks below were recomputed with an independent
standard-library-only exact-arithmetic script.  No network access, external
prime table, numerical value of (s), numerical logarithm, or zero data was
used.

Before this report was added, `results/` contained exactly the seven expected
precursor files.  They were all single-link regular files.  Adding this report
produces the exact eight-file pre-manifest inventory; the manifest is not yet
present and was not written by this review.

## Frozen artifact bindings

| Artifact | Independently observed SHA-256 | Status |
|---|---|---|
| `experiments/source_lock.json` | `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49` | exact |
| execution code/design tree | `466fb64928ad5f8b5b4c2643d8875c98568bbbdaabd4abeb6f24cc7ba13ecddb` | exact framed recomputation |
| `results/CODE_REVIEW.md` | `dffcd516d349ef864d078764b9e9ccaa2edccd70d52802e77b6965baa70b9b27` | exact Round-4 deployment authority |
| `results/PRE_EXECUTION_TESTS.xml` | `096dfff6203d48b22340e8def19bacca27294d383c1807f6856985fe99ff0cd8` | exact |
| `results/PRE_EXECUTION_AUDIT.json` | `a54ad84f5e889b9e54a4f4407b1e8a9021a001358188419ffa961f11d8f2b75a` | exact |
| `results/registered_run.claim.json` | `863d9d3c4e77bd2407776244c8e925abd60fd265cff5163698e81d32f144e2d4` | exact |
| `results/EXPERIMENT_RESULTS.json` | `448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab` | exact |
| `results/registered_run.json` | `bc82784449e50ec85c3d268197ab8489c7e2a888bfb35aa4a49915488b66273c` | exact |
| `results/POSTRUN_TESTS.xml` | `43f03d9be620188422dbb01d8ff016d4811eb505475214845ae17dffb21c6304` | exact; 23/23 pass |
| `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `66bfefe9dcf5731cb89a0597deed5df322f9bc24f9fc3a592d4790a46d2a4dc0` | exact |
| `experiments/OFFICIAL_VALIDATION_REPORT.md` | `32a1758362f94372a83588de63e2b5df33a8f7e45e0646de53154a2ca1afaab4` | exact |

The execution-tree hash was recomputed independently from the exact closed
inventory of 27 code files and the eight reviewed design paths, using the
specified length-framed path/content encoding.  All local design hashes and
all six frozen Paper-8 upstream hashes also match the source lock.  In
particular, `experiments/EXPERIMENT_TRACKER.md` remains byte-exact at
`00fc66f266b7a1ddcccc0b355ff7dbb6ea787f1d60319862dbd7d5da6262d0b9`.

## Independent finite-field reconstruction

I independently enumerated every nonzero vector in
(mathbb F_p^2), applied

\[
(x,y)\longmapsto(2x+y,x+y)\pmod p,
\]

and checked least periods, cyclic closure, disjointness, exhaustivity, and
the canonical representative of every cycle.  The raw data table is:

| (p) | shell size | point-period profile | primitive-cycle profile | (m_p) | split strata |
|---:|---:|---|---|---:|---|
| 2 | 3 | (3:3) | (3:1) | 1 | binary boundary |
| 3 | 8 | (4:8) | (4:2) | 2 | inert |
| 5 | 24 | (2:4, 10:20) | (2:2, 10:2) | 4 | ramified Jordan |
| 7 | 48 | (8:48) | (8:6) | 6 | inert |
| 11 | 120 | (5:120) | (5:24) | 24 | 4 eigenline plus 20 off-eigenline cycles |

Thus all 203 nonzero vectors occur exactly once in 37 primitive cycles.  The
independently generated canonical cycles agree entry-for-entry with the raw
JSON.

The separate analytic reconstruction also agrees:

- modulo 2, Cayley--Hamilton gives the unique length-three nonzero cycle;
- modulo 3 and 7, the characteristic polynomial is inert and the matrix
  orders are respectively 4 and 8, both dividing (p+1);
- modulo 11, the polynomial splits, the matrix order is 5, and the two
  eigenlines contribute 4 cycles while their complement contributes 20;
- modulo 5, (A=-I+N), with
  (N=\left(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\right)),
  (N^2=0), rank (N=1), and a five-element kernel.  The four nonzero
  kernel vectors have least period 2, while the other twenty vectors have
  least period 10.

These calculations establish the five registered finite controls.  The
all-odd-prime lower bound remains a proof-sourced statement, not an
extrapolation from these five rows.

## Product and repetition ledgers

The raw factors reconstructed solely from the cycle profiles are:

| (p) | exact raw-return factor | orbit-label degree | label coefficients at (r=1,2,3) |
|---:|---|---:|---|
| 2 | ((1-2^{-3s})^{-1}) | 1 | (1,1/2,1/3) |
| 3 | ((1-3^{-4s})^{-2}) | 2 | (2,1,2/3) |
| 5 | ((1-5^{-2s})^{-2}(1-5^{-10s})^{-2}) | 4 | (4,2,4/3) |
| 7 | ((1-7^{-8s})^{-6}) | 6 | (6,3,2) |
| 11 | ((1-11^{-5s})^{-24}) | 24 | (24,12,8) |

For each locked repeat (r=1,2,3), every raw monomial has exponent
(r|\gamma|) and aggregate coefficient
(\#\{\gamma:|\gamma|=\ell\}/r); the distinct orbit-label coefficient is
(m_p/r).  Every rational string and formal monomial in the raw JSON agrees
with this reconstruction.  In particular, the mixed ramified factor is not
silently replaced by the one-time label factor.

## Mechanism controls

All twelve registered controls are exactly `true`.  Independent rational
arithmetic reproduces the following key comparison:

| (p) | scalar degree | equal-weight power sums (r=1,2,3) | fractional outer exponents | selector discards |
|---:|---:|---|---|---:|
| 2 | 1 | (1,1,1) | (1) | 0 |
| 3 | 2 | (1,1/2,1/4) | (1/2,1/2) | 1 |
| 5 | 4 | (1,1/4,1/16) | (1/12,1/12,5/12,5/12) | 3 |
| 7 | 6 | (1,1/6,1/36) | six copies of (1/6) | 5 |
| 11 | 24 | (1,1/24,1/576) | twenty-four copies of (1/24) | 23 |

The nonzero scalar denominator has degree (m_p), so every registered odd
shell fails degree-one collapse.  Equal weights (1/m_p) repair only the
first power sum when (m_p>1).  The fractional exponents sum to one because
the cycles partition the complete shell; they are correctly labeled
`GLOBAL_NORMALIZED_COUNTING`.  The selector control retains one cycle only
by discarding (m_p-1) cycles and does not claim a canonical selector.

The symbolic composite record is internally exact: (q) remains `null` and
symbolic, no composite shell is enumerated, the cardinality is (J_2(q)),
and the normalized cycle-partition identity is explicitly labeled
proof-only and non-prime-specific.

## Lifecycle, forbidden inputs, and proof firewall

The durable chain is exact:

1. the authorized pre-execution audit records zero registered audits and no
   started prime;
2. the unique claim records `REGISTERED_RUN_0001`, count one, and exactly
   the primes (2,3,5,7,11);
3. the raw result binds that claim and records one exact audit;
4. the certified terminal binds both exact hashes, lists the same five
   primes as started and completed, and has no failure code.

The one-shot lifecycle test is present in the post-run suite.  The suite has
23 tests, zero failures, zero errors, and zero skips.  The exact directory
inventory, unique lifecycle files, exclusive-write contract, matching
counts, and certified terminal support `registered_run_count=1`; no
candidate rerun was performed during this review.

The result counters are exact integers, not booleans:

- candidate numerical runs: 0;
- generated prime target arrays: 0;
- numerical (s) or logarithm evaluations: 0;
- composite shells enumerated: 0;
- centralizer computations: 0;
- parameter/matrix searches: 0;
- normalization/selector searches: 0.

The flags for external prime tables and Riemann-zero data are `false`, and
the result contains exactly the five locked prime rows.  An independent AST
check found no network/process import root and no call to a numerical
logarithm, exponential, or network request primitive in the closed code
tree.  The registered evidence makes no all-prime or global-convergence
inference from the finite audit.

The proof-only contract correctly records only the three bounded convergence
statements: divergence for real (1<s\le2), failure of absolute convergence
for (1<\operatorname{Re}s\le2), and absolute convergence for
(\operatorname{Re}s>3).  It makes no claim in the gap
(2<\operatorname{Re}s\le3), no exact-abscissa or analytic-continuation
claim, and no prime/zero statement.  Centralizer quotients, matrix-valued
weights, numerator or alternating cancellation, transfer/Fredholm
determinants, cohomological superdeterminants, and enriched selectors remain
outside scope.  Route B is not opened.

Both official reports state the same finite ledger, product separation,
scope boundary, lifecycle chain, hashes, and terminal classification as the
raw evidence.  I found no inconsistency, unsupported extension, hidden
numerical fit, or stale binding.

## Verdict

The immutable result package is scientifically exact and provenance-closed
at the independent-review stage.  It certifies
`PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED /
A0_FAIL_GLOBAL_NORMALIZATION_ONLY / ROUTE_B_NOT_OPENED` within the frozen
scope.  The next authorized operation is the one-shot strict result-manifest
build; this review does not perform it.

PRIME_SHELL_RESULT_REVIEW_V1 {"candidate_id":"cat_prime_shell_multiplicity_obstruction_v1","execution_code_sha256":"466fb64928ad5f8b5b4c2643d8875c98568bbbdaabd4abeb6f24cc7ba13ecddb","result_sha256":"448de06e92bd7ab4e5374e5d1f57413df45859cd3476ff14b2691b63ac364fab","reviewer_independent":true,"source_lock_sha256":"662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49","verdict":"RESULT_PASS"}
