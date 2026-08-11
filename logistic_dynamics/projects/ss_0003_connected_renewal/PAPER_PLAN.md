# Paper plan — SS-0003 connected integer-renewal Dirichlet transfer

Paper status: `planned`.

## Working contribution

Constructs a connected countable renewal graph whose rank-two Fredholm determinant is exactly 2-zeta(s) on Re(s)>1 and whose scalar a-points have the correct Theta(T log T) fixed-strip order.

## Claim-evidence boundary

| Item | Paper treatment |
|---|---|
| Frozen object | State exactly from `source_lock.yaml` |
| Main result | Prove or reproduce only the source-locked checkpoint |
| Strongest failure | Positivity forces a unique forbidden real determinant zero in (1,2), and the all-integer primitive alphabet has no prime/von-Mangoldt law. |
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
