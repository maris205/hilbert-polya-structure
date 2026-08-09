# Repository update

## Release identity

- Candidate: HCS-C23
- Source commit: `4817c47be086703c550882464f40bf68701368d3`
- Release tag: `hcs-c22g-c23-audited-closure-v1`
- Release decision: `CLOSED_AT_CYCLIC_RESULTANT_BASELINE`

## Audited handoff

The release retains the finite-free fixed-algebra theorem, exact norm-event
equivalence, two non-dihedral chronology separations, complete frozen prime
rows, and independent rank-backend checks. It adds the exact identity

\[
\Delta_{w,r}=\operatorname{Res}_X(P_w(X),X^r-1),
\]

which closes every fixed-word repetition tower as classical cyclic-resultant
baseline. The former broad ledger is cancelled; no Euler product is
authorized.

Verification:

```bash
./code/run_c23.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
```

The formal Route-A record is
`evaluations/route_a/hcs_c23/20260809T104226Z.yaml`.
