# Repository update for HCS-C22 T1--T4 and orbitwise scalar T5

**Mathematical source commit:** cab8a79f5d3e8e81a48958aec69d371ac23af08e
**Release tag:** hcs-c22-t4-orbitwise-scalar-t5-v1
**Date:** 2026-08-09

## Included result

The source commit freezes:

- the T1 common-survivor theorem, T2 complete tested chronology
  separations, and T3 unit-numerator global residue collapse;
- the T4 intrinsic instability Euler determinant, exact repetition and
  fixed-point log-trace identities, and explicit nonzero normal-convergence
  domain;
- common strict two-letter base-pinning and unstable-projective/logarithm
  domains;
- an exact no-go for orbitwise fixed-point-denominator cancellation by a
  multiplicative scalar geometric cocycle, on both the base and natural
  projective lift;
- the explicit boundary that compensation among distinct same-period orbits
  in an unmarked aggregate scalar trace is not excluded; and
- the source-locked HCS-C22G graded exterior Ruelle--Lefschetz roadmap, with
  no nuclear or supertrace theorem yet claimed.

The current formal Route-A record is
[20260809T081750Z.yaml](evaluations/route_a/hcs_c22/20260809T081750Z.yaml).
Its conservative verdict remains

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\]

with overall status ROUTE_A_EXPLORATORY.  T4 improves the internal dynamical
determinant theorem but supplies no target divisor or arithmetic
normalization, so A2 does not pass.  Route B remains closed.

## Verification

From the repository root:

    cd henon_dynamics/henon_time_ordered_ruelle_cocycle
    python -m pip install -r requirements.txt
    ./code/run_c22.sh
    ./code/run_c22_t4.sh
    pytest -q code/test_c22.py code/test_c22_t4.py
    sha256sum -c results/ARTIFACT_HASHES.sha256

Expected outcome: T1--T4 and both common-domain gates PASS; the orbitwise
scalar-cancellation flag is false as the expected theorem outcome; both
independent checkers PASS; all 26 tests PASS; and all 16 artifact hashes are
OK.

## Historical release

The earlier T1--T3 source commit
2d3dbddfa726e9a1e881447e50ed705942dbed87 and tag
hcs-c22-t1t3-v1 remain valid historical records.  Their formal evaluation,
[20260809T050207Z.yaml](evaluations/route_a/hcs_c22/20260809T050207Z.yaml),
correctly records the pre-T4 state and is superseded as the current entry by
the evaluation above.

## Next controlled move

HCS-C22G receives one large nuclear/supertrace gate.  It must construct the
joint three-complex-dimensional half-inverse domains, coherent orientation
bundle, nuclear-of-order-zero exterior operators, and exact chronological
supertrace.  Failure or a merely noneffective substitution of prior art
closes the C22 operator lineage; no Ulam grid, longer cycle catalogue, or
finite-section spectrum is an accepted fallback.
