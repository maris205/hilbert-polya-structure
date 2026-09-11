# P190 author improvement log

## Round-0 freeze

The author pass established the all-time good-run normal form, parity-sensitive
sharp tails, every-target trace and gap fibres, zero-output spectrum, image
criterion, and mass identity. The exact verifier made 1,555,420 assertions in
26 finite boxes. The anonymous four-page PDF was frozen unchanged as
`main_round0_original.pdf` with SHA-256
`5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66`.

## Hostile Review A findings

The process-separated reviewer independently represented cyclic words as
base-`q` integers and reconstructed fibres by directed walks. Its 2,615,881
assertions found no mathematical counterexample and opened two Minor
presentation findings:

1. `P190-A-MI-01`: Eq. (11) contained a leading comma before the first matrix
   index. The comma was deleted; the proved row-current/column-next direction
   is unchanged.
2. `P190-A-MI-02`: `\paragraph{CRediT.}` rendered as `CRediT..` under the
   document class. The source heading was changed to `\paragraph{CRediT}` so
   the class supplies exactly one full stop.

No theorem, proof, table, citation, owner statement, or lifecycle boundary was
changed. The deterministic rebuild produced `main.tex` SHA-256
`73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300`
and `main_round1.pdf` SHA-256
`81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d`.
The original Review-A process rechecked the requested delta, reran its
independent control, closed both findings, and returned
`PASS_DELTA_ACCEPTED` with final open census `0/0/0`.
`OWNER_AMBER / HOLD_EXTERNAL` remains binding.

## Hostile Review B and Round 2

Review B reopened the theorem from an anchor-gap decomposition. Every
nonzero target was rebuilt by fixing anchor letters and counting the
intervening zero-producing blocks by a reviewer-owned dynamic program, rather
than by either the author's cyclic trace products or Review A's directed-walk
tables. Its 1,438,171 exact assertions rechecked the good-run normal form,
parity-sensitive sharp tails, every-target image criterion, the all-zero
fibre recurrence, and mass identity, and returned
`Critical 0 / Major 0 / Minor 0`.

No further source or PDF change was requested. `main_round2.pdf` is therefore
byte-identical to the accepted Round-1 artifact, with SHA-256
`81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d`.
Terminal QA on 2026-09-04 completed both physical source-only cold builds,
final manifests, and closed reviewer replays. `OWNER_AMBER / HOLD_EXTERNAL`
remains binding.
