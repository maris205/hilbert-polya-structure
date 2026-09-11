# UGR author certificate — actual execution receipt

2026-09-06 UTC. Python 3.12.3. Working directory for the commands below:
`/root/autodl-tmp/symbolic_dynamics`. Standard-library only; no runtime
repository/canonical reads or imports. This is an author certificate, not
independent UGR review.

## Preserved failures

Three local discovery programs tested insufficient dependency cones.
Their completed outputs are preserved, including counterexamples:

| Program / output | Exact local scope | Violations |
|---|---|---:|
| `local_probe.py` / `LOCAL_PROBE_CANONICAL.json` | All 19,683 length-nine words; only first three rows of extremum events | 290 |
| `local_probe_v2.py` / `LOCAL_PROBE_V2_CANONICAL.json` | All 177,147 length-eleven words; only first three event rows | 1496 |
| `local_probe_v3.py` / `LOCAL_PROBE_V3_CANONICAL.json` | Same length-eleven words; all four event rows | 204 |

These programs finish normally because they are counterexample finders;
their zero program exits are **not** PASS verdicts for their proposed
lemmas. `local_probe_v4.py` then handled all nine outer-letter extensions
of each of those 204 exceptions and reported zero violations. The proof
package includes the exact extension-coverage deduction.

The first integrated edge-based verifier execution (session 78426) exited
one at an over-strong core *test*: it compared a single center equation
with a classified weak-column rule that also uses the neighbour's own
equation. The exact failed input code is `verify_ugr.failed_v1.py`;
`FAILED_V1.stdout` is empty and `FAILED_V1.stderr` is the full 865-byte
traceback. No successful canonical existed at that failure. The correction
checks sufficiency on all five-type triples, and necessity on all
five-column windows satisfying the three center/neighbor equations.
The actual proof states that extra equation explicitly. Failed artifacts
were preserved before the corrected production, not overwritten.

## Corrected complete production

Final `verify_ugr.py` SHA-256:
`ca6bc9d408d09fbb1e3700432077c3843b68811c8c6dbf60de69d679f81a062a`.
The actual production command was

```sh
python3 docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/verify_ugr.py > docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/CANONICAL.json 2> docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/canonical.stderr
```

Session 80520 actually completed with exit zero. The complete canonical
is 224,755 bytes, SHA-256
`0d0944d63f300b79877b816b1c289ae91984b92f2b3082aa115d62d085baa9d9`.
Its stderr is empty. It reports **33,321 passing assertions**, status
`PASS`, with ordered checked-record digest
`6ef33d56f8b325fe0da0f9a8afb9fa3ad2fecadce577f5312e27ccb340ef63b3`.

## Two additional fresh raw-byte replay runs

Replay 1 (session 75174), exact command:

```sh
python3 docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/verify_ugr.py > docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay1.stdout 2> docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay1.stderr && cmp docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay1.stdout docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/CANONICAL.json > docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay1.cmp.stdout 2> docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay1.cmp.stderr
```

Replay 2 (session 93429), exact command:

```sh
python3 docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/verify_ugr.py > docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay2.stdout 2> docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay2.stderr && cmp docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay2.stdout docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/CANONICAL.json > docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay2.cmp.stdout 2> docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/replay2.cmp.stderr
```

Both sessions actually completed with exit zero; the `&&` chain establishes
both producer and comparator exits zero in each run. Both complete stdout
files have the canonical hash above. All six replay stderr/comparator files
are empty. These are additional executions after canonical production,
not rehashing old results.

## Coverage, with finite checks distinguished from proof

- All 27 literal triples verify the edge-sign update formula. All 90
  strict-center cases among the 243 five-letter words verify persistent
  extrema and their type reversal.
- All 177,147 inner words: 158,643 equal-center cases, 18,300 cases with
  an inner new-extremum witness, and 204 exceptions. Every exception has
  all nine outer extensions checked, yielding 1836 explicit witnesses.
  Their **complete list** is printed in the canonical. This is not a
  larger cycle-size atlas: coverage of all thirteen-letter words follows
  by the proved inner-window extension argument.
- Five-column compatibility is checked on the complete local alphabet:
  all 125 triples for sufficiency, and all 3125 five-column words for the
  converse; 116 satisfy all three necessary center/neighbor equations.
- All 28 allowed three-role paths satisfy the literal update under phase
  flip. Every graph edge respects that flip. The eight-role determinant
  is evaluated by exact Leibniz expansion (17 nonzero terms).
- Integer graph traces and the rational coefficient recurrence agree for
  indices 1–60. Indices 1 and 2 are formal graph values only, not a change
  to the original $n\ge3$ carrier. Core counts for $n=3,\ldots,10$ match
  the existing root observations; no new full cyclic atlas is run.
- Only the 27 states at $n=3$ are fully enumerated here. For $n=4,\ldots,10$
  the explicit single-hole source alone is checked against its derived
  all-time wave and exact entrance. No larger full-enumeration cutoff is
  used to rescue a signal or infer a sharp global bound.

The all-length mathematical implication, exact core converse and wave
proof are in [PROOF_PACKAGE.md](PROOF_PACKAGE.md). Successful certificate
replays do not imply source clearance; [SOURCE_HOLD.md](SOURCE_HOLD.md)
states the remaining independent-assessment obligation precisely.
