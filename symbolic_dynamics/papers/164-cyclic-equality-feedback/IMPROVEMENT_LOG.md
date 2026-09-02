# P164 improvement log

External status remains `HOLD_EXTERNAL` throughout.

## Round 0

- Frozen PDF: `main_round0_original.pdf`
- SHA-256: `db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae`
- Hostile Review A verdict: `REVISE_MINOR — 0 Critical / 0 Major / 2 minor`

## Round 0 -> Round 1 repairs

1. Expanded the proof of the last-shell formula by setting `x=q-1` and
   displaying a strict positive lower bound for every `q>=3`, dyadic `n>=4`.
   No theorem statement or formula changed.
2. Expanded the image-surjectivity proof to quantify `1<=j<=n`, record
   `1 in ker D^j` also at the nilpotent cap `j=n`, and verify that a forbidden
   unit representative is replaced by a feasible weight-`n-1` mask.  No
   theorem statement or formula changed.

The repairs implement the executable recommendations in
`HOSTILE_REVIEW_A.md`.  Round 1 is to be rebuilt from source, reverified, and
frozen before Hostile Review B.

## Round 1 freeze

- `main.tex` SHA-256:
  `6a589c778137cb6e039f7a01710e7264686c6952321f0494ee3c992bfcda4218`
- `main.pdf` and `main_round1.pdf` SHA-256:
  `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26`
- PDF: 4 A4 pages, 301,337 bytes, blank identifying metadata, 23/23 fonts
  embedded/subsetted/Unicode mapped, settled build logs with zero warnings.
- Author replay: 1,154,387 assertions, byte-identical to its canonical
  transcript (`dddbb6ba...997f`).
- Review-A replay: 950,659 assertions, byte-identical to its canonical
  transcript (`5ad48573...830e`).

The original Round-0 PDF remains byte-identical at its pinned hash.  Round 1
is ready for an independent Hostile Review B.

## Review B and Round 2

Review B returned `0 Critical / 0 Major / 0 minor` after independently
rederiving the full result, executing 7,718,087 assertions, replaying its
canonical transcript three times, running fresh owner and P1--P165 collision
audits, and producing two source-only cold builds.  It found no executable
correction.

No source, theorem, proof, reference, verifier, or presentation change was
made.  `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` are
byte-identical at SHA-256
`b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26`;
the separate Round-0 artifact remains at
`db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae`.
The four-page artifact passes build, font, metadata, anonymity, visual, and
release-sentinel QA and remains `HOLD_EXTERNAL`.
