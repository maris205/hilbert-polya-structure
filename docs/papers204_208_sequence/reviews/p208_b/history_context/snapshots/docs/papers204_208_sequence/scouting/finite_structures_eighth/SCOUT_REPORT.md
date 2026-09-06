# Eighth finite-structure scout — closed, six NO_PROMOTION

2026-09-06 UTC. Author: `batch197_fifth_scout`.
The prior Fosp desk checkpoint remains unchanged, and its BRF/FFR
suggestion provenance is credited in the intake and source ledger.

Outcome: **6 attempted literals, 105 fixed complete boxes, 179,716
state-map pairs; 0 promotions, 0 reserves, 0 new paper IDs.**
All six are NO_PROMOTION. No maximum cutoff or new full box was added.
External priority, publication and specialist-contact status is HOLD_EXTERNAL.
This is an author scout closure, not independent scientific acceptance.

## Literal scope and terminal finite profiles

The first-run definitions and all bounds are frozen in
[INTAKE.md](INTAKE.md). Integer partitions, Boolean matrices, ordered
DAGs and finite self-maps provide four non-word carrier types; FFR's
ordered tuples are explicitly not counted as another non-word carrier.

Here I is image size, R is recurrent-state count, H is maximum tail
length to a cycle, and m is maximum one-step fibre size. A cycle entry
`length:count` counts cycles, not states. These are finite-box facts only.

| Literal | Complete original bounds | Terminal box | States | I | R | H | m | Cycle histogram at terminal box |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| WGP: weighted-gap areas | partitions N=0…24 | N=24 | 1,575 | 226 | 6 | 15 | 44 | 1:6 |
| DSR: Durfee-square repacking | partitions N=0…24 | N=24 | 1,575 | 487 | 18 | 23 | 19 | 1:18 |
| UPA: exact-one permanental cofactor | all Boolean matrices n=0…4 | n=4 | 65,536 | 13,228 | 10,441 | 3 | 9,976 | 1:259, 2:5,091 |
| DP3: path count ≡1 modulo 3 | all fixed-order DAGs n=0…6 | n=6 | 32,768 | 21,874 | 19,609 | 9 | 21 | 1:1,623, 2:6,079, 4:1,457 |
| BRF: backward ancestor counts | all self-maps n=0…6 | n=6 | 46,656 | 7,823 | 11 | 17 | 120 | 3:1, 8:1 |
| FFR: first-fit final residuals | every M=0…5, k=0…5 | M=5,k=5 | 7,776 | 420 | 4 | 6 | 950 | 2:2 |

The terminal FFR row must not hide its original-box counterexample:
at M=5,k=2, `(1,1) → (3,3) → (2,2) → (1,1)` is a 3-cycle.
Likewise WGP has periods 9 at N=19 and 11 at N=23; terminal rows do
not summarize all earlier cycle lengths. The canonical output retains
every box, all maximizing fibre targets, maximum-height witness orbits,
longest cycles, and a digest of the complete sorted transition relation.

## Gate decisions after full deductions

| Literal | Actual theorem-level progress or deduction | Missing qualifying residual | Decision |
| --- | --- | --- | --- |
| WGP | Mass-preserving conjugate equal-column area regrouping; static primitive only | All-mass temporal structure and separate inverse | NO_PROMOTION |
| DSR | Complete fixed-point staircase-plus-tail characterization and static count proved | Global convergence/clock and a separately evaluated inverse; fixed states alone are insufficient | NO_PROMOTION |
| UPA | n≤3 is characteristic-two adjugation; all-size unique-perfect-matching branch is an old UPC adapter with U⁴=U² | All-size treatment of zero/multiple-matching branches and independent inverse | NO_PROMOTION |
| DP3 | Coarse all-size period divisor 2^(n−2), entry bound 2^(n−2)−1, proved by generic triangular reset/flip argument and fully deducted | Path-specific residual temporal advance and separately evaluated fibre structure | NO_PROMOTION |
| BRF | Elementary functional-graph backward counts; named fibres `(n−1)!` | Full temporal core/clock and evaluated arbitrary inverse or proved all-size extremes | NO_PROMOTION |
| FFR | Pairwise distinct-bin final residual sum < M; exact in-scope 3-cycle refutes a two-cycle guess | All-parameter iteration theorem and independent inverse | NO_PROMOTION |

The proofs, conventions, distinctions from old literals, and explicit
failed monotonicity guesses are in [PROOF_BOUNDARIES.md](PROOF_BOUNDARIES.md).
The actual historical/primary inputs and deductions are in
[SOURCES.md](SOURCES.md). Negative source search is not a priority claim.

## Reproduction and evidence

From `/root/autodl-tmp/symbolic_dynamics`:

```bash
python docs/papers204_208_sequence/scouting/finite_structures_eighth/pilot.py
python docs/papers204_208_sequence/scouting/finite_structures_eighth/verify.py
sha256sum -c docs/papers204_208_sequence/scouting/finite_structures_eighth/HISTORICAL_INPUTS.sha256
sha256sum -c docs/papers204_208_sequence/scouting/finite_structures_eighth/SHA256SUMS.txt
```

Both scripts are standard-library and stdout-only. `pilot.py` uses
direct definitions and walk decomposition; `verify.py` imports no pilot
code and instead uses Kahn deletion, Ferrers cells/conjugate multiplicities,
matching subset DP, explicit path subsets, reverse-reachability closure,
and bin content lists. It checks every canonical profile field, all
transition digests and specified proof controls on exactly the original
105 boxes. This is a separate **author** implementation, not an independent
review or a proof of untested sizes.

- `PILOT_CANONICAL.jsonl`: actual first pilot stdout, 105 rows.
- `PILOT_REPLAY.jsonl`: second actual pilot stdout, byte-identical.
- `AUTHOR_VERIFY_CANONICAL.jsonl`: actual separate implementation stdout,
  105 per-box checks and one aggregate control row; 179,716 state-map pairs.
- `AUTHOR_VERIFY_REPLAY.jsonl`: second actual author-check stdout,
  byte-identical to its canonical output.
- `RUN_RECEIPTS.json`: commands, actual exit codes and replay comparisons.
- `HISTORICAL_INPUTS.sha256`: whole-file pins of the collision originals.
- `SHA256SUMS.txt`: nonself manifest of the final package, including the
  untouched desk checkpoint, all source/proof/code/output/receipt files.

No code discrepancy or assertion failure occurred in either implemented
checker. Scientific nonpromotion and the FFR 3-cycle are retained as
negative evidence, not erased as failed runs. No central index, old
manuscript, accepted review, mirror, or Git path was changed by this scout.
