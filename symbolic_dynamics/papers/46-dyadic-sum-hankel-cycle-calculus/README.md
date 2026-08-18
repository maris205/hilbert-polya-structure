# Paper 46 isolated integration candidate

Status: `PRE-OUTPUT / PREAUTHORITY / AUTHORITY WRITE FORBIDDEN`

This package implements the frozen P46 dyadic-sum Hankel experiment without
writing any authority, Git, repository README, mirror, registry, or
repository-manifest path. The sole research input is the non-writable
`preauthority/` tree, whose self-excluding manifest SHA-256 is
`fc132644764bb93927dbcd5cbf63917e48e2c512d72adc375ef7590210226bab`.

## Architecture

- `code/evaluator_m/evaluate.py` builds literal cutoff matrices and directly
  enumerates bounded closed walks.
- `code/evaluator_c/evaluate.py` independently enumerates dyadic
  anti-diagonals, valuation blocks, and algebraic cyclic solutions.
- `code/auditors/` separates proof, source, type, and implementation
  independence ownership.
- `code/route/` renders and validates both provenance states with two
  independent Route validators.
- `contracts/MUTATION_REGISTRY.json` contains 62 concrete instances in 25
  families, including every F01--F14 row and governance/integrity controls.
- `contracts/RESULT_SCHEMA.json` freezes every evaluator/comparison key,
  nested array shape, integer field, fraction encoding, and the sole explicit
  comparison Boolean. Comparator, type auditor, integrity auditor, and frozen
  external auditor validate this structure independently; Python's
  `True == 1` never satisfies an integer field.
- `external_auditor/frozen_auditor.py` checks the complete static/output tree
  outside the producer namespace and is exercised on 13 physical mutated
  clones. The three coordinated result attacks are each sent through the
  comparator (`X`), type auditor (`T`), integrity auditor (`G`), and frozen
  auditor (`F`), for 22 physical consumer invocations in total.
- Comparator producer mode writes the canonical comparison, while explicit
  `--mode audit-existing` reconstructs it from M/C and exactly audits the
  stored `results/exact_comparison.json`. Integrity has a corresponding
  `--phase audit-existing` check for an installed tree.
- `contracts/CLI_REJECTION_CONTRACT.json` fixes totalized validation behavior:
  missing arguments, unknown flags, unknown mutation identifiers, unsafe or
  nonexistent roots, and runtime validation failures produce exit `2`, empty
  stderr, and one canonical JSON rejection. Only explicit `--help` is human
  output with exit zero.
- `code/integration/run_integration.py` stages every byte, runs two complete
  reconstructions and a cold relocation, supports a forced late failure,
  atomically installs the single `outputs/` directory, and performs zero
  target writes when the installed bytes are already exact.
- Hash domains are deliberately acyclic. The static manifest excludes itself,
  `PREOUTPUT_STATIC_SEAL.json`, and `outputs/**`; the State-B paper manifest
  excludes itself and `PREOUTPUT_STATIC_SEAL.json`; and the receipt tree hash
  frames only final output-relative paths and their raw bytes. Consequently,
  replacing the pre-output seal cannot change either State-B manifest bytes or
  the output-tree hash. Both integrity auditors reject a paper manifest that
  attempts to include the seal.

The finite trace identity is always evaluated as a scale-dependent sum with
odd cutoff `floor(N/2^k)`. Only the proof auditor owns the separately typed
infinite geometric identity.

## Canonical execution

The canonical candidate itself is deliberately not executed and has no
`outputs/` directory. Full smoke uses a disposable clone:

```text
python -I -B code/integration/run_integration.py \
  --root ABSOLUTE_DISPOSABLE_CLONE \
  --output-root ABSOLUTE_DISPOSABLE_CLONE/outputs \
  --state A
```

State B additionally requires one nonzero lowercase 40-hex commit supplied
with `--commit`. It is publication-shaped evidence only and conveys no
authority or publication decision.
