# P92 — Primitive-Recurrence Avoidance Shifts

Status: **mechanically sealed GO for the frozen internal theorem package;
external release HOLD**.

For a primitive degree-`r` recurrence over `F_q`, this paper studies the
two-sided shift in which the recurrence discrepancy is required to be
nonzero at every coordinate.  With

```text
L = q^r - 1,  H = q^(r-1) - 1,  D = (q-1)^H,
```

the state adjacency matrix satisfies

```text
det(tI-A) = (t-(q-1))(t^L-D).
```

The theorem package includes:

- a conjugacy to a finite affine skew product over the full
  `(q-1)`-shift;
- a Fourier proof that separates the zero character from one weighted
  Singer cycle;
- every fixed-point count, every least-period orbit count, and the rational
  Artin--Mazur zeta function;
- mixing and the unique uniform maximal-entropy measure for `q >= 3`;
- the exact nonmixing binary boundary at `q=2`;
- first-anomaly recovery: `F_1` recovers `q`, and the first deviation from
  `F_1^n` occurs at `L=q^r-1`, recovering `r`.

## Exact controls

Run:

```text
python3 code/verify_primitive_avoidance.py
```

The program uses only the Python standard library.  It builds the actual
adjacency matrices for `(q,r)=(2,2),(3,2),(3,3),(4,2),(5,2)`, including an
independent `F_4 = F_2[u]/(u^2+u+1)` lane.  It checks 258 exact assertions:
Singer transitivity, the dual hyperplane count, the full characteristic
polynomial, regularity, mixing where claimed, traces through `L+1`, the
first anomaly, and parameter recovery.

## Build

`latexmk` is unavailable in the current environment.  From this directory,
use:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The expected artifact is `main.pdf` (six pages in the frozen draft).

## Ownership scope

Primitive polynomials, Singer cycles, and deterministic LFSR cycle structure
are prior art and are positively cited.  The general SFT determinant and
Parry measure are also not claimed.  The results proved here concern the
nonzero-error relation, its weighted Fourier block, and the resulting
delayed-anomaly symbolic theorem package.  No direct prior treatment of that
combined package was identified in the documented bounded search, but this
is not an absolute novelty or priority claim.
Public posting, submission, author contact, and venue selection remain
unauthorized and **HOLD**.

## Files

- `main.tex` — complete anonymous `amsart` manuscript with full proofs
- `references.bib` — four cited, source-verified references
- `code/verify_primitive_avoidance.py` — deterministic exact controls
- `CONTROL_RESULTS.md` — frozen control output and coverage
- `CLAIMS_EVIDENCE.md` — claim-to-proof/control ledger
- `HOSTILE_REVIEW.md` — two-pass internal adversarial review record
- `BUILD.md` — reproducible compilation record
- `FINAL_QA.md` — final log, PDF, font, text, and page-render audit
- `SHA256SUMS` — verified package checksums
- `main.pdf` — compiled six-page draft

The release manifest verifies locally with `sha256sum -c SHA256SUMS`.
