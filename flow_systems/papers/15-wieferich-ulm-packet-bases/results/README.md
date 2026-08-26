# Paper 15R control results

No generated control result is authorized merely by the presence of the source
implementation.  At the end of this remediation-authoring phase this directory
contains this README only.  There is no generation receipt, execution receipt,
test receipt, or cleanup receipt.

If a later execution gate succeeds, the generator will create exactly these
nine additional regular files, with no directory, cache, lock, temporary, or
auxiliary member:

```text
valuation_normalization_controls.csv
exponent_order_branch_controls.csv
finite_kernel_truncation_controls.csv
torsion_closure_type_controls.csv
signature_nonpromotion_controls.csv
owner_firewall_controls.csv
proof_ceiling_controls.csv
target_summary.csv
manifest.json
```

The first eight are canonical CSV artifacts.  Their frozen data-row counts are
16, 14, 18, 10, 12, 15, 26, and 9, totaling 120.  Their registered negative-row
counts are 4, 2, 4, 3, 4, 9, 9, and 0, totaling 35.  `manifest.json` is the
ninth generated member; it binds the eight artifact bytes, the 14 authority
sources, design lock/current review/historical implementation-gate provenance,
and the six implementation sources.  Its exact top-level schema remains twelve
keys; it excludes itself from the artifact-hash list, contains no `dag` key,
and rejects `self_sha256`, `result_review`, and every future back-edge.

The verifier reconstructs the frozen manifest-dependency graph from those
existing semantic blocks.  It has the exact eight nodes and twelve edges:

```text
A -> D
D -> R
R -> G
G -> I
I -> C
C -> M
M -> V
A -> M
D -> M
R -> M
G -> M
I -> M
```

The unique topological order is `A,D,R,G,I,C,M,V`.  `V` denotes the future
review successor and is not serialized as a manifest object.  The v2/v3
implementation-remediation gates remain external governance and do not become
authority bindings, manifest nodes, or edges.

The exact aggregate block records eight CSV artifacts, nine generated members,
120 body rows, 35 explicit semantic negatives, 35 detected negatives, 28
package mutation classes, 173 unit-test methods, two fresh generations, three
byte-identical copies, zero tolerance, and `RANDOM_USED=false` /
`NETWORK_USED=false`.  These are frozen expected values, not current run
observations.

These controls can record finite arithmetic diagnostics, typed scope failures,
owner/type firewall checks, and explicit proof ceilings.  They cannot establish
an infinite-family theorem, GRH/Chebotarev/density statement, compact-group
classification, Haar/trace/operator/determinant statement, or the final Ulm
classification claim.  A future PASS would mean only that the frozen control
package reproduced and its registered negative mutations were detected under
the exact possession protocol.

The hook/custody HC hash is not result evidence.  The current execution profile
is unaccepted, so these nine files remain absent and no manifest is presently
materialized.  Only a separate future execution-governance gate that pins the
exact HC and one execution-window class before wrapper invocation can make the
future branch eligible; that gate still cannot self-certify HP/HG/HM/MECH/H or
turn source-authoring checks into an execution receipt.
