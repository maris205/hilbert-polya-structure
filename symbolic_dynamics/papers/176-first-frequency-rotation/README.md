# P176 — First-frequency rotation on binary pointed necklaces

**Status:** `FINAL ROUND 2 / DUAL-REVIEW CLOSED /
AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.

The literal system is

```text
T_n(w) = rotate_left(w, multiplicity of w_0),    w in {0,1}^n.
```

At fixed Hamming weight `k`, a pointed necklace moves by `+k` when the
pointer sees `1` and by `-k` when it sees `0`.

## Round-0 result

The anonymous four-page AMS short note proves exactly five residual items:

1. the `+/-k` pointed-necklace component theorem, including every tail and
   recurrent component;
2. the complete possible-period inventory;
3. the sharp `n-2` clock and exactly two deepest states for `n>=3`;
4. the complete every-target predecessor list and global `0/1/2` fibre
   distribution; and
5. the primitive-block Möbius fixed census.

Høyer--Špalek's Hamming-weight-controlled quantum phase rotation,
Grošek--Hromada's fixed-weight coordinate-rotation classes, Gupta et al.'s
ordinary circular shifts, both frozen branches, P166's cyclic phase
architecture, the repeated value `n-2`, and indicator-style inverse notation
all receive zero contribution credit.  None of the external sources defines
the adaptive first-symbol gluing or its functional graph.

## Exact control

`code/verify_p176.py` is a standalone author/scout-derived regression
control using only the Python standard library.  It exhausts every binary
word for `1<=n<=18` and checks the literal functional graph against its
component, period, clock, fibre, and fixed-census prediction paths.  It is
not described as independent of discovery code.  Hostile Review A supplies
the genuinely independent bit-mask implementation through `n=19`.

```text
assertions:               2,828,503
verifier SHA-256:         2dd56b882925c908565a9a213c42db7acccbf4fc214b54460619b71fe0587b50
canonical SHA-256:        3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b
PDF SHA-256:              c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4
pages:                    4 (A4)
```

Two independent source-only cold builds reproduce the live PDF byte for byte.
`main_round0_original.pdf` and `main_round1.pdf` preserve the pre-source-
repair bytes; `main.pdf` equals `main_round2.pdf`.

## Artifact map

- `main.tex`, `references.bib`: anonymous self-contained manuscript.
- `main.pdf`: live canonical Round-2 four-page PDF.
- `main_round0_original.pdf`: byte-identical Round-0 freeze.
- `main_round1.pdf`, `main_round2.pdf`: immutable review-round receipts.
- `NARRATIVE_REPORT.md`: problem, mechanism, theorem package, and limits.
- `PAPER_PLAN.md`: claim-first architecture and section contract.
- `CLAIMS_EVIDENCE.md`: claim/proof/control traceability.
- `PROOF_PACKAGE.md`: author-side normalized dependency and boundary proof
  audit (`PROVABLE AS STATED`).
- `SOURCE_VERIFICATION.md`: publisher/arXiv metadata and subtraction audit.
- `code/verify_p176.py`, `code/CANONICAL.txt`: standalone
  author/scout-derived regression control and frozen transcript.
- `BUILD.md`, `SELF_QA.md`: deterministic build record and author-side QA.
- `build_*.log`: retained compile and cold-build traces.
- `SHA256SUMS`: artifact manifest.

The immutable Round-0 package predates hostile review.  The live package now
contains completed Reviews A/B; Review B's two source/provenance minors are
repaired and independently delta-accepted.

## Reproduction

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 code/verify_p176.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
sha256sum -c SHA256SUMS
```

The verifier output must equal `code/CANONICAL.txt` byte for byte.  Any
direct owner, literal embedding/conjugacy into P166, transferred P166
mass-exhaustion proof, or verifier failure activates the paper's strict kill
switch.  No external action is authorized.
