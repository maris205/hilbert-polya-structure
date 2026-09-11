# Historical title and collision audit

The breadth pass was performed only after reading the existing paper-title
inventory and the prior collision/kill artefacts.

## Paper titles

- Scope: every live numeric directory in `papers/` with paper number at most
  181, sorted numerically and then lexically.
- Records: **176 live directories**.  The count reflects the historical gap
  P51--P56 and the two live P96 directories.
- SHA-256 of the newline-terminated sorted basename list:
  `1c7d3fed5c1452a69e67c7dd2a1845fe5124c2d61166aef739eedae4b2b0206b`.
- The retired alternate `papers/retired/160-binary-projective-steiner-triangle-collapse`
  was also inspected, giving 177 title records when that retired replacement
  is included.

The particularly relevant live titles P97, P102--P110, P115, P128, P135,
P137, P143, P164, P168, P171, and every title P172--P181 were then checked
against their sequence notes, rather than compared by title alone.

## Collision and kill reports

- Scope query: prior files under `docs/` whose basenames contain `collision`,
  `firewall`, or `kill_ledger`, excluding this lane's newly written files.
- Artefacts inspected: **88 files**, **503,708 bytes**.
- Aggregate audit digest, formed by hashing each sorted relative path, a NUL,
  its bytes, and a NUL:
  `192f5282a78fdc935ab7a0f0ca70178fa381b9d3376983b4666cf9cc3d597b24`.
- The sequence-level `HISTORICAL_COLLISION_SEED.md` files for P167--P181 and
  the current P182--P186 seed were separately included in the conceptual
  review even where a filename query already caught them.

The audit produced the mechanism-level exclusions frozen in
`COLLISION_FIREWALL.md`: fixed-linear/Jordan engines, monotone folds,
subspace-product closures, polarities, inverse spans, Gram maps, rank
feedback, and every P172--P181 mechanism.  Digests document the inspected
snapshot; they do not substitute for the explicit comparisons.

