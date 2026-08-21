# C80 source audit

The producer and checker bind these predecessor receipts before deriving any
threshold statistic:

| source | role | SHA-256 |
|---|---|---|
| `henon_mu3_yukawa_mark_closure_incidence_lift/results/c75_closure_incidence_lift_evidence.json` | named coordinates and subgroup rows | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` |
| `henon_mu3_yukawa_mark_closure_incidence_lift/C75_PREFREEZE_MANIFEST.json` | C75 release binding | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` |
| `henon_mu3_yukawa_mark_closure_orbit_atlas/results/c76_closure_orbit_atlas_evidence.json` | all-support closure authority | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` |
| `henon_mu3_yukawa_mark_closure_orbit_atlas/C76_PREFREEZE_MANIFEST.json` | C76 release binding | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` |
| `henon_mu3_yukawa_mark_repair_distance_geometry/results/c78_repair_distance_geometry_evidence.json` | exact full-core repair boundary | `728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae` |
| `henon_mu3_yukawa_mark_repair_distance_geometry/C78_PREFREEZE_MANIFEST.json` | C78 release binding | `955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60` |

C79 is optional at implementation time and is not silently treated as an
authority.  C80's exact-closure row is independently checked against C78.
The scope literal remains `NO_BAD_EULER_OR_ROOT_NUMBER`.
