# C84 source audit

The producer and independent checker byte-bind every upstream file they read.

| source | SHA-256 | role |
|---|---|---|
| C75 evidence | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` | named coordinates, subgroup point sets, ambient lifted order |
| C75 manifest | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` | C75 release binding |
| C76 evidence | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` | effective generators and seven full-core-minimal orbits |
| C76 manifest | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` | C76 release binding |
| C79 evidence | `147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879` | repair formula and ten exact `(rho,W)` counts |
| C79 manifest | `982cce509de371d59c4b87cda75af057d994c6fc36146daddc3b983c9c63246c` | C79 release binding |

The independent checker reconstructs the twenty C75 subgroups as point sets
inside `Z/9 + Z/3 + Z/2`, builds the complete 65536-entry closure table, and
does not accept C79's structural basis formula as a substitute for closure
enumeration.  C76's seven representatives are expanded under its five
effective label generators before the all-deleted equality is tested.

The group actions remain distinct: C75's ambient lifted group has order
`11520`, whereas C76's faithful effective label action has order `1920`.
Neither is promoted to a full Burnside ring or table-of-marks computation.
