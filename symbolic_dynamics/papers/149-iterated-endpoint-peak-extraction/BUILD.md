# Build and QA record — P149

## Pre-hostile build

- Engine: pdfTeX 1.40.22 / LaTeX2e, BibTeX 0.99d.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Result: success, 4 A4 pages, 368,101 bytes.
- Historical pre-hostile intermediate SHA-256:
  `c72edb2a165b959d1e9b9410e7f4d70dd630d289b41b351a996779811677c1ad`.
- Round-0: 4 pages, 367,680 bytes; SHA-256
  `2cbd557258087f59dc5a378a379137b137d85a0d767a20da6f919bb47d0e8dcd`.
- Bibliography: 4/4 entries cited and resolved; all are verified primary
  papers/author records.
- Cross-references/citations: zero unresolved warnings in the final log.
- Bad boxes: zero overfull or underfull warnings.
- Fonts: all embedded and subsetted.
- Metadata: title and author metadata blank; no creation/modification date;
  PDF unencrypted, version 1.5.
- Visual inspection: all four round-0 pages and the revised all-rank/clock page
  were rasterized and accepted.

## Exact control

- Canonical replay is byte-identical to `verification_output.txt`.
- Assertions: 1,228,181.
- Coverage: all 409,113 permutations through rank 9; iterate image sets
  through five steps; every feasible right section through source rank 8;
  recursive deepest witnesses; and every target comparison-poset fibre through
  source rank 8.
- Finite enumeration is counterexample pressure, not proof.

## Reproducibility

- Two consecutive in-place final builds are byte-identical.
- A clean source-only build from `main.tex` and `references.bib` was
  byte-identical to the then-current hostile-A PDF recorded below.
- Volatile PDF dates and trailer IDs are suppressed.

## Hostile-A convention/owner repair build

- `main.pdf` and `main_round1.pdf`: 4 A4 pages, 373,097 bytes,
  SHA-256
  `3a0e734d3edd708d6188406fbb94362658b5f5d690c34cc6897cab6e349a4a9d`.
- The Round-0 PDF remains unchanged at SHA-256
  `2cbd557258087f59dc5a378a379137b137d85a0d767a20da6f919bb47d0e8dcd`.
- Repair: Ji's exact two-zero-boundary static statistic is now the directly
  inspected zero-credit owner; Fu is correctly restricted to its one-sided
  exterior-peak convention; ordinary interior-pinnacle work is connected by the
  explicit padding bridge; run-sorting is described as a bijective
  equidistribution, not a pointwise invariant; three fixed-set/order neighbours
  and stable journal/DOI metadata are added; the false strict-bound sentence
  is replaced by strict rank descent.
- Bibliography in this historical artifact: 8/8 cited and resolved; settled log has no unresolved
  citation/reference, rerun request, or bad box.
- Review B is preserved with verdict 0 Critical / 1 Major / 1 Minor; its
  theorem, verifier, build, and visual interfaces pass, while its source-role
  Major is repaired in the next build.

## Self-QA boundary

`PROOF_PACKAGE.md` classifies the frozen theorem package as **PROVABLE AS
STATED**.  `SELF_QA.md` records the author-side contract, boundary-case,
source, and artifact audit.  Both hostile reviews are preserved.  Static
exact-boundary, one-sided, and ordinary-pinnacle owners are separated, and the
fibre theorem remains secondary.  External status is `HOLD_EXTERNAL`.

## Round-2 owner-repair closure

- Review A: 0 Critical / 1 Major / 2 Minor.  Its padding, run-sorting,
  fixed-set-neighbour, metadata, and strict-rank repairs are preserved.
- Review B: 0 Critical / 1 Major / 1 Minor.  The theorem package passed; its
  Major correctly rejected Fu as an exact two-zero-convention owner, and its
  Minor separated historical from current hashes.
- Direct repair: Ji 2025, Definition 2.1, was inspected as the exact static
  convention owner.  Fu remains a one-sided neighbour.  Official
  Carlitz--Scoville metadata and Ji's attribution are recorded, but no
  earliest-owner or priority claim is made without the original full text.
- Canonical `main.pdf` and `main_round2.pdf`: 4 A4 pages, 374,480 bytes,
  SHA-256
  `7a9e801bfecc08000db82ea37ff9b1e206e4e3ec0ca211c46481db1f401bbacb`.
- Bibliography: 9/9 entries cited and resolved.
- Two isolated source-only four-stage builds reproduce `main.pdf` byte for
  byte.  Settled logs have no undefined citation/reference, rerun request,
  bad box, or BibTeX warning.
- The canonical verifier transcript replays byte for byte with 1,228,181
  exact assertions.  All 4/4 final pages pass visual inspection.
- Internal result: ACCEPT / `GO_INTERNAL`.  External status:
  `HOLD_EXTERNAL`.
