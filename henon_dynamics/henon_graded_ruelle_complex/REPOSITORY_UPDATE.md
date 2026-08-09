# Repository update

## Release identity

- Candidate: HCS-C22G
- Source commit: `4817c47be086703c550882464f40bf68701368d3`
- Release tag: `hcs-c22g-c23-audited-closure-v1`
- Release decision: `CLOSED_AS_CONDITIONAL_BLUEPRINT_AFTER_THEOREM_AUDIT`

## Audited handoff

The release retains exact one-step complex pinning constants, the physical
tangent-fibre and product-contour conventions, the block determinant sign,
and candidate exterior parity. It withdraws the earlier claims of proved
all-word kernel composition, order-zero nuclearity, canonical nuclear trace,
jointly entire Fredholm factors, and meromorphic continuation on
\(\mathbb C^2\).

Verification:

```bash
./code/run_c22g.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The formal Route-A record is
`evaluations/route_a/hcs_c22g/20260809T104226Z.yaml`.
