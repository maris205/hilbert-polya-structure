# Exact-pilot self-check

The verifier is standard-library-only, enumerates canonical RREF subspaces,
constructs each transition independently, decomposes each finite functional
graph, checks every target fibre, and increments an explicit assertion count.
It does not import project code or write cache files when invoked as below.

Two fresh Python processes were run from the repository root:

```bash
tmp1=$(mktemp)
tmp2=$(mktemp)
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/scouting/algebra_lane/verify_algebra_lane.py >"$tmp1"
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers182_186_sequence/scouting/algebra_lane/verify_algebra_lane.py >"$tmp2"
cmp "$tmp1" "$tmp2"
cmp "$tmp1" \
  docs/papers182_186_sequence/scouting/algebra_lane/CANONICAL.txt
```

Frozen result:

- independent processes: 2;
- systems explicitly enumerated: 3 (two finalists plus one collision kill-control);
- parameter boxes: 15;
- transitions: 334,363;
- assertions: 1,707,811;
- transition digest:
  `d4865b98955027f396370ea9d05e6d161da932b9eb31b019b6df929b5dd6d36d`;
- stdout comparison: byte-identical;
- final status: `RESULT=PASS`.

The assertion count includes RREF canonicity, subspace counts, lattice tables,
iterate identities, full graph decompositions, all target fibres, projection
lift counts, and closed census formulas.  Enumeration covers prime fields;
the proofs in `THEOREM_SPIKES.md` supply the prime-power extension.

