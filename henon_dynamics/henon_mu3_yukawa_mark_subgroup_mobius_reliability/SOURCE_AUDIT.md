# C77 source audit

| Source | Role | SHA-256 |
|---|---|---|
| `henon_mu3_yukawa_mark_generation_blocker_reliability/results/c73_generation_blocker_reliability_evidence.json` | C73 top reliability authority | `e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5` |
| `henon_mu3_yukawa_mark_generation_blocker_reliability/C73_PREFREEZE_MANIFEST.json` | C73 prefreeze binding | `a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d` |
| `henon_mu3_yukawa_mark_closure_incidence_lift/results/c75_closure_incidence_lift_evidence.json` | C75 named coordinates and twenty subgroups | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` |
| `henon_mu3_yukawa_mark_closure_incidence_lift/C75_PREFREEZE_MANIFEST.json` | C75 prefreeze binding | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` |
| `henon_mu3_yukawa_mark_closure_orbit_atlas/results/c76_closure_orbit_atlas_evidence.json` | sixteen coordinates, twenty subgroup rows, C76 closure convention | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` |
| `henon_mu3_yukawa_mark_closure_orbit_atlas/C76_PREFREEZE_MANIFEST.json` | C76 release binding and gate record | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` |

The C76 evidence records the ambient core as
`Z/9 + Z/3 + Z/2`, sixteen named coordinates, and twenty subgroups in a
fixed index order.  C77 treats those rows as the mathematical source of the
poset; no subgroup is reconstructed from an abstract isomorphism type.

The C76 effective label group has order `1920`, while the preceding lifted
ambient object has order `11520` and a six-element action kernel.  That
effective-versus-ambient distinction is inherited as a boundary condition,
but C77's polynomial itself is indexed by generated subgroups and is checked
against all supports directly.

The C77 producer, checker, and SymPy cross-check verify all six raw source
hashes before reading coordinates or closure rows.  The canonical C77 evidence
hash is `f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634`.
Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
