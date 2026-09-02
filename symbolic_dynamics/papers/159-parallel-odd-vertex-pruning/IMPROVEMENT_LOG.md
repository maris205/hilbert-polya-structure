# P159 improvement log

**Current state:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Immutable baseline

`main_round0_original.pdf` remains the byte-exact pre-review freeze:

- 5 A4 pages, 363,455 bytes;
- SHA-256 `bba68d57e9f46cda2996db072b703ff0b18e5d19c7edab2a53ef24d3032c8602`.

## Hostile Review A disposition

Review A returned `PASS — 0 Critical / 0 Major / 0 Minor`.  Its independent
syndrome-counting implementation executed 3,605,601 assertions and passed all
strict/diagonal, orientation, boundary, temporal-fibre, image, source, and PDF
attacks.  No theorem, proof, bibliography, verifier, transcript, or evidence
claim required repair.

The only source change before the Round-1 lifecycle freeze removes the stale
word “Round-0” from the declarations sentence; `HOLD_EXTERNAL` and every
release prohibition remain unchanged.  This is an administrative artifact
label, not a response to a finding and not a mathematical change.

## Round-1 artifact

- `main.pdf` and `main_round1.pdf` are byte-identical;
- 5 A4 pages, 363,444 bytes;
- SHA-256 `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d`;
- the unchanged 3,167,525-assertion verifier replay remains byte-identical to
  its transcript, SHA-256
  `363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879`;
- the settled build has zero selected warnings, bad boxes, undefined
  references, and rerun requests;
- all 27 font rows remain embedded, subsetted, and Unicode mapped.

## Hostile Review B disposition and Round 2

Review B returned `REVISE — 0 Critical / 0 Major / 1 Minor`.  Its fresh
derivation, 88,623-assertion independent control, author/reviewer verifier
replays, two source-only builds, and five-page inspection passed every
mathematical and artifact interface.

The sole finding was one stale sentence at the end of `CLAIMS_EVIDENCE.md`
claiming that neither formal review had occurred.  It now accurately records
Review A's zero findings and this Review-B lifecycle repair.  No manuscript,
formula, proof, bibliography, verifier, transcript, or PDF change was needed.

`main_round2.pdf` is the byte-identical accepted freeze of Round 1 and current
`main.pdf`: 5 A4 pages, 363,444 bytes, SHA-256
`72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d`.
Surviving severity is zero Critical, zero Major, and zero Minor.
