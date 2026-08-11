# Paper plan — QG-0001 exact base characteristic

Paper status: `planned`.

## Working contribution

Proves the exact pole-free base matching characteristic and its relation to the directed-bond secular determinant.

## Claim-evidence boundary

| Item | Paper treatment |
|---|---|
| Frozen object | State exactly from `source_lock.yaml` |
| Main result | Prove or reproduce only the source-locked checkpoint |
| Strongest failure | This is a single-component local theorem and does not define the infinite tower determinant or target divisor. |
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
