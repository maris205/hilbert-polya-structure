# Paper 16 Exact Prototype Report

**Candidate:** SD-C18

**Artifact base:** `papers/16-equivariant-cycle-index-determinant/`

**Execution date:** 2026-08-14

**Data policy:** no Riemann-zero data; no external dataset; no fitting.

## Outcome

All frozen exact obligations passed:

- theorem checks: `12/12`;
- unit tests: `17/17`;
- squarefree cyclic words enumerated: `2..9366` for `n=2..7`;
- ghost-power rows: `56`;
- `C2` sign-power checks: `4008`;
- inventory-control rows: `455`;
- Schatten cutoff rows: `160`.

The result is positive only at the formal cycle-index level.  It is a negative
result for arithmetic character-resolved Fredholm fibers.

## Raw exact comparison table

| Audit | Frozen range | Exact result | Status |
|---|---|---|---|
| Squarefree primitive cycles | `n=2..7` | totals `2,6,26,150,1082,9366`; every word primitive | PASS |
| Scalar squarefree balance | `n=2..7` | positive equals negative at every `n` | PASS |
| `pqr` representation | `S_3` | `1 + sgn - Std`; character `(0,0,3)` | PASS |
| Burnside marks | `1,C2,C3,S3` | `(0,0,3,1)` | PASS |
| Higher Adams into `pqr` | `r=2..8` | no integral multidegree preimage | PASS |
| Rank-one vs diagonal ghosts | `n=2..8,r=2..8` | witness coefficient `r` versus `0` | PASS |
| Equal-weight rank-one modes | `n=2..8` | nontrivial eigenvalues `0`, determinants `1` | PASS |
| Distinct-weight symmetry | `n=2..8` | stabilizer order `1` | PASS |
| Equal-weight symmetry | `n=2..8` | stabilizer order `n!` | PASS |
| Diagonal superdeterminant | `n=2..8` | differs from pure Euler determinant in all cases | PASS |
| Projective zero-specialization | `2->1,...,8->7` | exact termwise equality | PASS |
| `C2` power-sign carrier | 4008 cases | all correct; naive integer Adams fails in 988 cases | PASS |
| Inventory controls | 455 rows | all reproduce finite identities/no-go | PASS |

## Key findings

### 1. Scalar cancellation hides actual recurrent label motion

**Observation.** At every tested squarefree degree, positive and negative
counts agree.  Nevertheless the `pqr` virtual character is `(0,0,3)` and
further nonzero character values persist through `n=7`.

**Interpretation.** Dimension/augmentation is a lossy readout.  It proves only
scalar cancellation, not an equivariant sign-reversing pairing.

**Implication.** A completed Burnside/species/cycle-index ledger is a legitimate
formal refinement of Paper 15.

**Next step.** If continued, move symmetry to a genuine commuting symbolic
fiber cocycle; base-label relabeling cannot survive prime specialization.

### 2. Arithmetic specialization destroys the required fixed symmetry

**Observation.** Distinct prime-square weights have stabilizer order one for
every `n=2..8`; equal weights restore all `n!` permutations.

**Interpretation.** The universal object is semilinearly covariant, but the
arithmetically specialized operator is not `S_n`-equivariant.

**Implication.** Character projectors cannot be interpreted as invariant
Fredholm fibers of the fixed arithmetic transfer.

**Next step.** Use genuine group extensions/cocycles, where the group acts on a
fiber independently of roof labels.

### 3. The natural analytic lift changes the determinant

**Observation.** The rank-one ledger uses `b(x)^r`; the diagonal subset lift
uses `b(x^r)`.  The coefficient witness is `r versus 0` for every frozen
`r>=2`.  At `x_2=1/4,x_3=1/9`, the target determinant is `2/3`, while the
diagonal superdeterminant is `24/35`.

**Interpretation.** Keeping subset representation data changes repetition and
introduces mixed factors such as `(1-x_p x_q)^-1`.

**Implication.** One cannot cite the scalar Euler determinant as the Fredholm
determinant of this resolved diagonal operator.

**Next step.** Any alternative operator must publish its full power traces
before claiming determinant equality.

### 4. The analytic threshold exists but belongs to the wrong object

**Observation.** The exact criterion is `D_s in S_q iff q Re(s)>1`.  At the
largest prime cutoff (`N=250`), the subset q-sum is about `6603.23` for
`sigma=0.6,q=1`, `7.01067` on the boundary `sigma=q=1`, and `0.519704` for
`sigma=2,q=1`.

**Interpretation.** The finite values illustrate divergence/convergence trends,
but membership follows from the infinite-product proof.

**Implication.** A trace-class diagonal operator exists for `Re(s)>1`, yet its
determinant remains the mixed-subset product.

**Next step.** Do not pursue regularized determinants until a correct primitive
ledger has been identified; regularization cannot remove the algebraic mismatch
without changing traces.

### 5. Controls prove universality, not arithmetic selectivity

**Observation.** Prime, composite-only, shuffled-prime, random-rational, and
free-commutative inventories pass every finite identity.  All 455 control rows
pass.

**Interpretation.** The mechanism is the Boolean/subset tensor grammar, not
the rational primes.

**Implication.** `PROVES_TOO_MUCH` is mandatory.  The prime specialization
supplies an analytic scale but no selective primitive mechanism.

**Next step.** Paper 17 must demand a grammar- or cocycle-derived arithmetic
distinction that fails matched controls.

## Representative analytic cutoff values

| Inventory | `N` | `sigma` | `q` | `q sigma` | Theorem class | finite subset q-sum |
|---|---:|---:|---:|---:|---|---:|
| primes | 250 | 0.6 | 1 | 0.6 | not `S_1` | 6603.2272 |
| primes | 250 | 1.0 | 1 | 1.0 | boundary, not `S_1` | 7.01067 |
| primes | 250 | 1.2 | 1 | 1.2 | `S_1` | 2.64543 |
| primes | 250 | 2.0 | 1 | 2.0 | `S_1` | 0.519704 |
| composites | 250 | 0.6 | 1 | 0.6 | not `S_1` | 4,361,105.71 |
| composites | 250 | 1.0 | 1 | 1.0 | boundary, not `S_1` | 24.1532 |
| composites | 250 | 1.2 | 1 | 1.2 | `S_1` | 4.05985 |
| composites | 250 | 2.0 | 1 | 2.0 | `S_1` | 0.206120 |

These are descriptive truncated products, not estimates of an infinite
determinant outside the proved convergence half-plane.

## Route decision

Resolved candidate:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

The inherited rank-one scalar shadow retains the Paper 14 scalar A2 identity, but it is not the character-resolved SD-C18 object. Its A2 coordinate is therefore not spliced into this tuple.

Frozen decisions:

```text
GO_FORMAL_EQUIVARIANT_LEDGER
STOP_CHARACTER_FREDHOLM_FIBERS
STOP_STANDARD_SUPERTRACE_INTERPRETATION
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Artifact index

- `results/summary.json` — top-level exact verdict;
- `results/squarefree_summary.json` — counts and scalar balance;
- `results/sn_character_table.csv` — all conjugacy-class characters through
  `S_7`;
- `results/burnside_cyclic_marks.csv` — cyclic-subgroup marks;
- `results/orbit_decomposition.csv` — transitive Burnside orbit decomposition
  by block-size necklace and stabilizer order;
- `results/s3_residual_certificate.json` — full `pqr` certificate;
- `results/ghost_power_audit.csv` — `b(x)^r` versus `b(x^r)` witnesses;
- `results/projective_c2_adams_certificate.json` — projective, sign, and Adams
  firewall;
- `results/rank_one_audit.csv` and `results/stabilizer_audit.csv` — fixed-fiber
  no-go;
- `results/diagonal_superdet_audit.csv` — exact mixed-factor mismatch;
- `results/schatten_cutoffs.csv` — descriptive cutoff table;
- `results/control_audit.csv` — all inventory controls;
- `results/SHA256SUMS.txt` — frozen code/result hashes.
