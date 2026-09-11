# LFAS re-entry exact replay receipt

Date: 2026-09-05 UTC. Author of this re-entry: `/root/batch197_lzk_gate`.
Two consecutive fresh Python processes ran `verify_lfas_reentry.py` with
`PYTHONDONTWRITEBYTECODE=1`. Both exited 0; their complete stdout strings
were directly compared and were byte-identical. The common output was
stored with `apply_patch` in `CANONICAL.txt`.

| Item | SHA-256 |
|---|---|
| verifier | `edc428dd758673500cb8b80639d707f21f7ddc717d5aa40e084f41188df5056c` |
| canonical / common stdout | `d70487cf0f6174e58692e68a72e290f0c6ff5856e59f6ce807d0082860d92322` |

Each replay reports 11 exhaustive parameter boxes, 38 sharp wide-regime
witnesses, and 1,076,738 assertions. Counts are per run, not added across
replays. A prior development run also passed and is not part of this pair.
The scripts import no old author implementation. Finite tests support the
deductive proof and do not supply the arbitrary-parameter argument.
