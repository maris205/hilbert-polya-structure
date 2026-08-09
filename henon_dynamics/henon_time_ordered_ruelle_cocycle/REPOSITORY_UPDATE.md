# Repository update for HCS-C22 T1--T3

**Source commit:** `2d3dbddfa726e9a1e881447e50ed705942dbed87`
**Release tag:** `hcs-c22-t1t3-v1`
**Date:** 2026-08-09

## Included result

The source commit freezes the common-survivor theorem, complete tested local
chronology separations, the unit-numerator global residue-collapse theorem,
the exact-rational producer, a nonimporting checker, eleven regression/mutation
tests, compact result artifacts, and the staged T4--T5 kill rule.

The formal Route-A record is
[`evaluations/route_a/hcs_c22/20260809T050207Z.yaml`](evaluations/route_a/hcs_c22/20260809T050207Z.yaml).
Its conservative verdict is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\]

with overall status `ROUTE_A_EXPLORATORY`.  Route B remains closed.

## Verification

```bash
cd henon_dynamics/henon_time_ordered_ruelle_cocycle
python -m pip install -r requirements.txt
./code/run_c22.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
```

Expected outcome: producer T1/T2/T3 PASS, independent checker PASS, 11/11
tests PASS, and all seven artifact hashes OK.

## Next controlled move

T4 precedes T5.  First prove a nonzero convergence domain and correct
primitive repetition law for the local instability cycle expansion.  Only
then attempt a common complex domain and nuclear trace formula.  Failure of
either gate triggers a dynamical-form pivot under the project work budget;
it is not an impossibility theorem for every operator construction.
