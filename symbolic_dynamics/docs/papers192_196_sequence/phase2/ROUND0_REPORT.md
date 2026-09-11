# Route A — Round-0 author freeze for P192–P196

Status: `5/5 ROUND0 FROZEN / HOSTILE REVIEW AUTHORIZED / HOLD_EXTERNAL`.

## Frozen manuscripts and exact controls

| paper | pages | author transitions | author assertions | canonical digest | Round-0 PDF SHA-256 |
|---:|---:|---:|---:|---|---|
| P192 | 3 | 280,392 | 1,962,920 | `67cc231e1e1ad859aca4c6de30f7a3dd76f81358ff2753b48bbdac06662cad24` | `aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1` |
| P193 | 5 | 409,113 | 7,985,745 | `28eedb5ba198c502e491d2788354ab2fe6de9785af1852bc3b4dd00f69f33761` | `e41e171c8f412cf93aae9510052ed0d8ad165125be1bd4c04133f1b410048267` |
| P194 | 4 | 25,384 | 618,419 | `15eae7619f324f7730af7dddb103820cb72434ebf897ee8ec4fde1c611e8df49` | `9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207` |
| P195 | 3 | 2,223,278 | 4,328,312 | `127008d8980f40a829a67bb2a1dd7005ac66f4655f25fb9713350e7480441287` | `bc0723b0b4417125122a40784f444565cdbd5565c5b65ac477042be2c209de3f` |
| P196 | 3 | 123,032 | 492,356 | `84ca454e3418703d34a5d0326f6f0eda679bd9901149353cf91a6b21fcbb9ad5` | `bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948` |
| **total** | **18** | **3,061,199** | **15,387,752** | — | — |

P192 additionally retains a separately implemented C++ stream over all
`9^7=4,782,969` Prüfer words.  It verifies all 128 history masks at `n=9`
and explicitly labels the history law as conjectural.

## Author-freeze boundary

Each directory contains anonymous `main.tex`, `references.bib`, a compiled
A4 PDF, narrative/plan/proof/claim/source/build/QA records, a paper-local
standard-library verifier, and an exact canonical transcript.  P192 also
preserves its pre-metadata-audit PDF under a noncanonical filename; its actual
Round-0 pin is byte-identical to the corrected canonical PDF.

Round 0 is author-side evidence, not process-separated review.  The PDFs do
not authorize novelty, posting, submission, or other external circulation.

