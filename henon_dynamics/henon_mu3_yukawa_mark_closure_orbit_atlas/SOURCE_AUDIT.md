# C76 source audit

| Source | Role | SHA-256 |
|---|---|---|
| `henon_mu3_yukawa_mark_closure_incidence_lift/results/c75_closure_incidence_lift_evidence.json` | C75 closure-incidence authority | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` |
| `henon_mu3_yukawa_mark_closure_incidence_lift/C75_PREFREEZE_MANIFEST.json` | C75 prefreeze manifest | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` |

The C76 producer checks both byte hashes before reading coordinates, subgroup
rows, or C75 generators.  The checker repeats this check independently and
also verifies that the C76 evidence is canonical JSON with schema
`hcs-c76-finite-support-closure-orbit-atlas-prefreeze-v1`.

The C75 lifted symmetry group has order 11520.  Its order-six ambient factor
is a kernel for the induced action on the sixteen labels, so C76 uses the
faithful 1920-element label group.  The omitted factor is recorded in the
evidence and is not silently discarded.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
