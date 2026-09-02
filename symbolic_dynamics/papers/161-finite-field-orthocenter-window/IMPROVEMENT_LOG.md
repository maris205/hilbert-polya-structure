# P161 improvement log

**Current state:** `ROUND-2 / REVIEW B ACCEPTED / HOLD_EXTERNAL`.

## Immutable baseline

`main_round0_original.pdf` remains the byte-exact pre-review freeze:

- 4 A4 pages, 305,817 bytes;
- SHA-256 `b0e241883509857362f59688b6ea18422959b07862681cabe13bedfe0d1f79c0`.

## Hostile Review A disposition

Review A returned `REVISE — 0 Critical / 0 Major / 1 Minor`.  Its independent
1,767,768-assertion audit passed every mathematical, source-boundary, and
scope interface, including the `p=3` empty-core boundary and a `p=5` negative
anisotropy control.

The single finding was a reproducibility-record mismatch: every Round-0 build
emitted a pdfTeX font-expansion ordering warning although the author build
record presented the settled output as clean.  This is fixed by retaining
microtype protrusion and disabling expansion explicitly.  No mathematical
text, theorem, proof, bibliography, verifier, transcript, or assertion count
changed.

## Round-1 artifact

- `main.pdf` and `main_round1.pdf` are byte-identical;
- 4 A4 pages, 304,462 bytes;
- SHA-256 `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214`;
- a fresh verifier replay remains byte-identical to the 1,317,843-assertion
  transcript, SHA-256
  `26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c`;
- the settled build now has zero selected warnings, bad boxes, undefined
  references, and rerun requests;
- all 21 font rows remain embedded, subsetted, and Unicode mapped.

## Hostile Review B and Round-2 freeze

Fresh Review B returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`.
It independently rederived the complete theorem, replayed the author and
Review-A lanes twice, and added a code-independent 6,262,521-assertion lane
covering `p=3,7,11,19` plus an isotropic `p=5` scope control.  Two source-only
cold builds matched Round 1 byte for byte; 21/21 font rows and all four
rendered pages passed inspection.  Review A's build-only repair therefore
remains closed and no further source or mathematical change was requested.

`main_round2.pdf` is the no-change acceptance freeze and is byte-identical to
`main.pdf` and `main_round1.pdf`: 4 A4 pages, 304,462 bytes, SHA-256
`1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214`.
Round 2 remains internal under `HOLD_EXTERNAL`.
