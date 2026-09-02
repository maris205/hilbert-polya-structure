# P157 improvement log

**Current state:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Immutable baseline

`main_round0_original.pdf` remains the byte-exact pre-review freeze:

- 4 A4 pages, 331,521 bytes;
- SHA-256 `4188a459ad233e8a6a55d5706648617e833ea0f7771d324a368352182a2f9c0d`.

## Hostile Review A disposition

Review A found zero Critical and zero Major issues and requested two Minor
scope/attribution repairs:

1. replace the eponymic title with the neutral polynomial title, because the
   Burban–Drozd appendix itself presents the lifting result as known;
2. replace unqualified “complete finite dynamics/atlas” language with the
   exact proved scope, “complete temporal and one-step inverse atlas.”

Both repairs were implemented in the manuscript and author-side ledgers.
Burban–Drozd is now described as a direct prior/foundation record, never as
evidence of origination.  The theorem formulas, hypotheses, proof spine,
verifier, frozen transcript, and assertion count were not changed.

## Round-1 artifact

- `main.pdf` and `main_round1.pdf` are byte-identical;
- 4 A4 pages, 331,596 bytes;
- SHA-256 `f054f639f4c9ba9d462c183f417597390223b18ca3f74ba5907c39637ba4743e`;
- the Round-1 ledger initially reported zero warnings; Review B subsequently
  identified a font-expansion ordering warning in every settled pass;
- all 25 reported font rows remain embedded, subsetted, and Unicode mapped;
- all four pages were raster inspected after the repair.

## Hostile Review B disposition and Round 2

Review B returned `REVISE — 0 Critical / 0 Major / 1 Minor`.  All theorem
formulas and both Review-A wording repairs passed.  The sole finding was the
Round-1 font-expansion warning contradicting the build ledger.

**Disposition: fixed.**  Microtype protrusion is retained and expansion is
disabled.  The long transcript hash was placed on its own small centred line
to avoid the bad box exposed when expansion was removed.  These are
typesetting changes only; theorem text, proof, bibliography, verifier, frozen
transcript, and assertion count remain unchanged.

- `main.pdf` and `main_round2.pdf` are byte-identical;
- 4 A4 pages, 349,380 bytes;
- SHA-256 `6b0c1fb81c065a9213df4cb4af7b731e25e02e3306e6220a154899166e9129dd`;
- two source-only builds reproduce the canonical PDF byte for byte;
- the settled and isolated builds have zero actual warnings, bad boxes,
  undefined references, and rerun requests;
- all 25 font rows are embedded, subsetted, and Unicode mapped;
- all four Round-2 pages were raster inspected.

The Review-B Minor is closed.  Surviving severity is zero Critical, zero
Major, and zero Minor; external status remains `HOLD_EXTERNAL`.
