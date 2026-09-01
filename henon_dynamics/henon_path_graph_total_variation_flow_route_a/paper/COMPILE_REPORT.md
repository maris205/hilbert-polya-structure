# C279 compile report

- Engine: LuaLaTeX (LuaHBTeX, TeX Live 2022)
- `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`
- Fixed hexadecimal trailer ID: yes
- Passes per build: 2
- Fresh builds per revision: 2, in unrelated temporary trees
- Fresh-build comparison: byte-identical for rounds 0, 1, and 2
- Final-pass warnings: none (no layout, citation, reference, destination,
  undefined-control, or rerun warnings)
- Fonts: 24 font records, all embedded and subset
- Text extraction: PASS; theorem, ROF, scope, tuple, and verdict literals found
- Visual audit: all seven pages across the three retained revisions inspected;
  no crop, overlap, broken glyph, malformed equation, or blank content page
- Pages by round: 2, 2, and 3
- Final PDF bytes: 180,672
- `main.pdf` equals `main_round2.pdf` byte for byte

| artifact | SHA-256 |
|---|---|
| `main_round0_original.pdf` | `b85431ebb5bb422e8576e6699a7339eccda7e606b670148a12eae7a6f2e6976c` |
| `main_round1.pdf` | `e1a885228e3592e11a22c059c021c44aa15fdc5fe31ccc6d5c28503b4a122d13` |
| `main_round2.pdf` | `83b2d3b5cb296c37edf10cd6120ff430750953ed39c11a74cc467b207a1dc024` |
| `main.pdf` | `83b2d3b5cb296c37edf10cd6120ff430750953ed39c11a74cc467b207a1dc024` |

Round 0 contains well-posedness, dissipation, and finite consensus.  Round 1
adds the exact block velocity, no-splitting theorem, simultaneous-collision
rule, and event bound.  Round 2 adds the averaged-subgradient ROF proof,
executable receipt, full boundary statement, the Steidl--Hoefling direct-owner
boundary, and strict Route-A rejection.
