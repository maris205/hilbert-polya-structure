# Paper plan — Strict-monotone autonomous Logistic clock-lift obstruction

Paper status: `planned`.

## Working contribution

Proves that the exact autonomous lift of the frozen logarithmic aging schedule has all full-state periodic orbits on the static U_c boundary.

## Claim-evidence boundary

| Item | Paper treatment |
|---|---|
| Frozen object | State exactly from `source_lock.yaml` |
| Main result | Prove or reproduce only the source-locked checkpoint |
| Strongest failure | The strict Lyapunov clock creates no recurrent aging orbits and adds a neutral clock multiplier, so occupation-matrix cycles cannot be used as chronological UPOs. |
| Route-A decision | Quote `route_a_evaluation.yaml` without promotion |
| Route B / RH | Explicit nonclaim |

## Proposed structure

1. Frozen dynamical object and data firewall.
2. Primitive-orbit or operator ledger.
3. Exact/certified result.
4. Reproduction protocol and source hashes.
5. Strongest obstruction and claim boundary.
6. Smallest legitimate reopening task.

## Reproducibility boundary

The manuscript may use only files named in `SOURCE_PROVENANCE.yaml`.  Any
later theorem edge requires a new source lock, evaluation version, and mirror
checkpoint.
