# Exact experiment report — Paper 36 / SD-C38

## Outcome

The authority experiment reproduces the frozen Cayley-chain no-go with
physically separated source and evaluator processes. The source layer passes
`33/33` internal checks, the independent evaluator reproduces the prototype's
`33/33` semantic checks and passes `35/35` authority integration checks, and
the integration suite passes `53/53` tests.

The finite audit supports the theorem boundary but does not replace the
independent proofs of infinite Cayley-complex contractibility, marker
non-descent, trace-class ownership, or all-orders generic supertrace
cancellation.

## Freeze and prototype bridge

The root source lock and preregistration plus
`experiments/PREREGISTRATION.md` and `experiments/EXPERIMENT_PLAN.md` were
frozen before authority code and results. The prototype source is byte
preserved at SHA-256 `041b8a...`; the evaluator is semantically preserved but
its extra blank terminal line is removed to satisfy authority exact-EOF. The
bridge still verifies the original `/tmp` evaluator SHA `d2cbd2...`.

The prototype scientific SHA `499b1a...` is research evidence only. Authority
payloads were regenerated independently and have their own 19-file scientific
aggregate:

```text
58a5d3b404d85163edfe74bea45b077da07ac6ff4f0794aff0bf9f1fbcf6ea9e
```

## Physical source/evaluator separation

`source_generator.py` imports only the neutral `source_core.py` and emits raw
presentation arithmetic. `evaluate_results.py` imports no source module. It
independently reconstructs affine group actions, free reductions, identity
counts, finite incidence and cell matrices, rational ranks, marker data,
damped relation coefficients, and generic graded controls.

The AST firewall verifies distinct process files, exact bridge hashes, no
source-to-evaluator import, no evaluator-to-source import, and no forbidden
candidate identifier.

## Fresh and cold reproducibility

The canonical orchestrator executed the complete six-stage pipeline in three
initially absent result directories:

1. fresh run A;
2. fresh run B;
3. cache-free cold run C after another cache purge.

All 19 scientific payloads and all six captured stage stdout streams are
byte-identical across A, B, and C. Only A was published. The research lock
binds seven frozen authority documents plus the external research package;
its SHA-256 is:

```text
1f1f5ef49f09cf234063e23d6e12464cc24592bfb66648a6dcbb7e695f16051c
```

## Exact relation and trace controls

| `r` | relation length | first excess length | excess identity words | one cycle weight at `theta=1/2` |
|---:|---:|---:|---:|---:|
| 2 | 5 | 5 | 10 | `2^-24` |
| 3 | 6 | 6 | 12 | `2^-34` |
| 4 | 7 | 7 | 14 | `2^-46` |
| 5 | 8 | 8 | 32 | `2^-60` |

Every displayed relation word evaluates to the identity, is primitive, and
is cyclically nonbacktracking. At the baseline `r=4`, one based cycle has
exact positive weight `1/70368744177664`; hence the prequotient trace sees the
relation before complete filling removes the homotopy ledger.

## Marker and finite chain controls

The balanced `r=1` relation has side lengths two and two and preserves the
unit marker. Every `r=2,3,4,5` mutation compares lengths two and `r+1` and
fails marker descent.

| `(r,q,t)` | vertices | cycle dimension | `H_1` after affine cells | `H_1` after complete cells |
|---|---:|---:|---:|---:|
| `(1,4,3)` | 12 | 13 | 2 | 0 |
| `(2,3,2)` | 6 | 7 | 1 | 0 |
| `(3,4,2)` | 8 | 9 | 1 | 0 |
| `(4,5,2)` | 10 | 11 | 1 | 0 |
| `(4,7,3)` | 21 | 22 | 1 | 0 |
| `(5,6,2)` | 12 | 13 | 1 | 0 |

Every affine and complete boundary-square check vanishes. The residuals after
affine cells are omitted finite quotient relations, not evidence for an
infinite retained sector.

## Generic cancellation and Route-A decision

All 48 sampled scalar-lift powers vanish exactly. The symbolic identity

```text
Str(A_tilde^n)=(1-2+1)tau(A^n)=0
```

holds for the affine presentation, balanced commutation, and an arbitrary
matched two-generator/one-relator presentation. It therefore realizes the
proves-too-much control and retains no arithmetic sector.

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

The strict Route-A v0.2 card records all target-zero/root metrics as scoped
`not_applicable;...` strings and pairs all three provenance fields as
`PENDING_FIRST_ARTIFACT_COMMIT`.

## Dependencies and integrity contract

The 19 scientific payloads use only the Python standard library. PyYAML is
separately locked and used only to parse the strict Route-A card during the
integrity seal. No GPU, network, external dataset, floating tolerance,
target-zero datum, coefficient fit, or Route-B tool is used.

The final integrity stage requires the exact result inventory, a sorted and
unique 43-entry immutable SHA ledger, research and dependency pointers, A/B/C
certificates, Route-A schema and enums, UTF-8/LF, exactly one terminal LF, no
trailing whitespace or forbidden control bytes, and no Python/test cache.

The mutable Route YAML is deliberately excluded from the Stage-1 SHA ledger.
It is audited separately and is valid only with either three paired
`PENDING_FIRST_ARTIFACT_COMMIT` fields or three identical lowercase 40-hex
fields after a metadata-only seal. The root paper manifest is likewise outside
experiment integrity. Metadata-stability tests require identical integrity
bytes with the manifest present or absent and with a dummy paired Route seal.
Final ledger and report hashes are reported externally after the nonrecursive
seal.
