# Independent LZK replay receipt

Date: 2026-09-05 UTC. Reviewer process: `/root/batch197_lzk_gate`.

Two consecutive fresh Python processes ran

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers197_201_sequence/reviews/lzk_stage1_20260905/verify_lzk_gate.py
```

Both exited 0. Their complete stdout strings were compared directly and
were byte-identical. The common stdout was stored as `CANONICAL.txt` using
`apply_patch`. Each run reports 20 boxes and 459,463 exact assertions.
These are LZK-only assertions, not the author lane's multi-system count.
An earlier development run also passed; it is not included in the two-run
receipt pair or assertion count.

| Artifact | SHA-256 |
|---|---|
| `verify_lzk_gate.py` | `9a04d5b4db039371f6052d998e40c3b7eb19083056fd3e5e53a14a201be7dacb` |
| `CANONICAL.txt` / common replay stdout | `09ceb3da76aeb6af0ddcb5540f9cc74dd6d47aec8c7f2cb8753f0729e5526cce` |

The verifier uses no nonstandard dependencies, author imports, random seed,
file writes, or floating point. Its mathematical boundary is the finite
boxes printed in the transcript. Arbitrary-parameter claims derive from
`PROOF_AND_COLLISION.md`, not from the assertion count.
