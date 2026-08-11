# Paper plan — TH-0001 same-order Fourier-integral quantization

Paper status: `planned`.

## Working contribution

Constructs the natural same-order unitary FIO on L2(R), proves the exact generating-function relation, and audits the inherited antiunitary class.

## Claim-evidence boundary

| Item | Paper treatment |
|---|---|
| Frozen object | State exactly from `source_lock.yaml` |
| Main result | Prove or reproduce only the source-locked checkpoint |
| Strongest failure | A natural unitary lift does not supply a determinant, discrete target spectrum, self-adjoint generator, or prime-power trace formula. |
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
