# C88 source audit

| source | SHA-256 | role |
|---|---|---|
| C75 evidence | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` | sixteen named coordinates and twenty actual point-set subgroups |
| C75 manifest | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` | frozen C75 byte ledger |
| C83 evidence | `033f42f0eea2518f7cb269dd465d82d4871a729d2b93679fcd9f3af38cf9ca28` | complete top-subgroup assembly stopping law |
| C83 manifest | `981f9b07297f1b69676e8ced2625e69df5bd8fcd366415a2f984eb6311ddaa85` | frozen final C83 byte ledger |
| C85 evidence | `22bdaf9fa2fe08532b45eae51cf7704a1509764b5a09f10eebb98012224be152` | actual subgroup inclusion matrix and order convention |
| C85 manifest | `d1e0af8c896e8975ef7544714d379499b2d69e50bdaabf4d8d55621e4c42d261` | frozen C85 byte ledger |

The producer and independent checker SHA-256-bind all six raw byte strings
before parsing them.  They also require canonical JSON, status
`PREFREEZE_G3_PASS`, and the common scope literal.

The producer rebuilds all `65536` closures through an indexed transition
table.  The checker independently enumerates the twenty subgroups from the
54-point group law, uses direct finite-set expansion for every support,
independently enumerates every target-minimal generating-support antichain,
and reconstructs the hit up-set from antichain containment.  It does not read
the producer's closure array, hit tables, pivotal counts, or probability rows.

C88 uses only actual point-set containment.  It does not infer containment
from an ambient or effective permutation action, and it does not claim
arithmetic/local data, Euler factors, root numbers, automorphy, a full
Burnside ring or table of marks, or a Hilbert--Polya operator.
