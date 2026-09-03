# P169 improvement log

## Review A repair

Hostile Review A returned `0 Critical / 0 Major / 1 Minor` and classified
the complete theorem package as `PROVABLE AS STATED`.

The sole finding was bibliographic currency.  The Round-0 package cited the
valid arXiv record `2407.15889` for Ji--Li--Wang, while the same work now has
a formal *Annals of Combinatorics* publication.  The repaired package:

- replaces the preprint-only BibTeX data by volume 29, issue 4, pages
  1155--1175 (2025), DOI `10.1007/s00026-025-00760-3`;
- renames the citation key from `JiLiWang2024` to `JiLiWang2025` and retains
  the arXiv identifier as an auxiliary field/link;
- updates `SOURCE_VERIFICATION.md` and the planning ledger; and
- makes the visible lifecycle phrase round-independent while retaining
  `HOLD_EXTERNAL`.

No theorem, proof, formula, example, verifier, claim ceiling, ownership
subtraction, or lifecycle decision changed.  The immutable
`main_round0_original.pdf` remains the exact author artifact; the repaired
source and PDF are the input to Hostile Review B.

## Review B closeout

Hostile Review B returned `0 Critical / 0 Major / 1 Minor` and independently
classified every theorem as `PROVABLE AS STATED`.  Its block-tuple verifier
made 8,698,292 exact assertions, with two byte-identical executions, and
reconstructed complete fibres by three independent routes.

The sole finding was a deferred packaging mismatch: the author README,
historical QA prose, and pre-repair checksum manifest still described the
mutable `main.pdf` as the Round-0 artifact.  The closeout therefore:

- keeps `main_round0_original.pdf` as the immutable author freeze;
- freezes the repaired PDF as `main_round1.pdf`, `main_round2.pdf`, and the
  live `main.pdf` under the repaired hash;
- updates `README.md`, `SELF_QA.md`, and `BUILD.md` to separate historical
  and current artifacts; and
- regenerates `SHA256SUMS` only after the full dual-review package is frozen.

This repair changes documentation and integrity packaging only.  It changes
no manuscript source, theorem, proof, formula, example, verifier, ownership
conclusion, or lifecycle decision.  External status remains `HOLD_EXTERNAL`.
