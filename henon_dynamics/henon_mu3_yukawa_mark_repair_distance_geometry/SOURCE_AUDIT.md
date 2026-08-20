# C78 source audit

The producer must verify these inherited authorities before deriving repair
distances.  Digests are listed here so that a changed upstream receipt cannot
silently alter the named presentation.

| source | role | SHA-256 |
|---|---|---|
| `henon_mu3_yukawa_mark_generation_blocker_reliability/results/c73_generation_blocker_reliability_evidence.json` | C73 generation criterion | `e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5` |
| `henon_mu3_yukawa_mark_generation_blocker_reliability/C73_PREFREEZE_MANIFEST.json` | C73 release binding | `a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d` |
| `henon_mu3_yukawa_mark_closure_incidence_lift/results/c75_closure_incidence_lift_evidence.json` | C75 coordinates and subgroup points | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` |
| `henon_mu3_yukawa_mark_closure_incidence_lift/C75_PREFREEZE_MANIFEST.json` | C75 release binding | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` |
| `henon_mu3_yukawa_mark_closure_orbit_atlas/results/c76_closure_orbit_atlas_evidence.json` | C76 sixteen-label closure atlas | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` |
| `henon_mu3_yukawa_mark_closure_orbit_atlas/C76_PREFREEZE_MANIFEST.json` | C76 release binding | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` |
| `henon_mu3_yukawa_mark_subgroup_mobius_reliability/results/c77_subgroup_mobius_reliability_evidence.json` | C77 subgroup reliability | `f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634` |
| `henon_mu3_yukawa_mark_subgroup_mobius_reliability/C77_PREFREEZE_MANIFEST.json` | C77 release binding | `bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc` |

The C75 named coordinates are

```text
(1,0,0), (6,0,0), (0,1,0), (3,1,0), (0,0,0), (0,0,0),
(4,2,0), (3,2,0), (0,0,1), (0,0,0), (0,1,0), (3,1,0),
(0,0,0), (0,0,0), (2,1,0), (8,2,0).
```

The C76 authority fixes the ambient group as `Z/9 + Z/3 + Z/2`, 16 labels,
65536 supports, and the twenty subgroup rows.  Its effective label action has
order 1920; the preceding lifted object has order 11520 with a six-element
ambient kernel.  C78 inherits this boundary and does not substitute one
presentation for another.

The producer and independent checker read all eight listed source files
directly; the C76 authority is not inferred only through C77.  The canonical
C78 evidence digest is
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`.
The C78 prefreeze manifest is generated after the final file set is sealed,
excludes itself and transient build files, and is recorded in the round plan
and release summary rather than inside the hashed compile receipt.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
