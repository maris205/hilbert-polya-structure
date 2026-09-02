# P165 final author-side QA

**Verdict:** `ROUND-2 INTERNAL ACCEPT / PASS / HOLD_EXTERNAL`.  Both hostile
reviews are complete.  Because neither requested a manuscript change, the
Round-0, Round-1, Round-2, and current PDFs remain byte-identical.

## Mathematical scope

- The map is visibly defined as padded shortening on one fixed labelled
  ambient space, with the strict `<2d(C)` threshold.
- The theorem separates the nonzero target from the zero target.
- Formula (7) is repeatedly identified as the simultaneous-extremizer count,
  not the complete target fibre.
- The zero-target equality is stated as
  `(T^t)^-1(0)={C:tau(C)<=t}`; its exact-depth minimal layer is explicitly a
  proper slice.
- `n=0`, `t=0`, nonzero full-support targets, `2^t-1>n`, labelled-code
  counting, and nonprime finite fields are covered.
- Jibril et al.'s entire one-step low-weight hitting-set route, including
  distance increase, is assigned zero contribution credit.

## Exact replay

Two fresh executions of `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py`
matched `code/CANONICAL.txt` byte for byte.  Each reports `605,733`
assertions and `RESULT PASS`.  No `__pycache__` directory was created.

## Typesetting and build

- canonical source build: settled after `pdflatex`, `bibtex`, and two further
  `pdflatex` passes;
- two source-only builds, each containing only `main.tex` and
  `references.bib`: both settled and matched `main.pdf` byte for byte;
- final and both cold settled logs: zero LaTeX/package warnings, undefined
  references or citations, rerun requests, overfull boxes, underfull boxes,
  and fatal errors;
- PDF: 4 A4 pages, 288,837 bytes, SHA-256
  `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a`;
- `main_round0_original.pdf` is byte-identical to `main.pdf`;
- all 23 font rows are embedded, subsetted, and Unicode mapped;
- title, author, subject, keywords, creator, and producer metadata are empty;
- PDF is unencrypted, has no form, and has no JavaScript.

## Anonymity and visual inspection

Extracted text contains no email address, local filesystem path, handle,
affiliation, acknowledgment, editing marker, or unresolved verification
marker.  The byline and running heads are anonymous, while bibliographic
author names are retained as required citations.  `HOLD_EXTERNAL` is visible.

All four pages were rendered at 144 dpi and inspected.  Equations, theorem
blocks, running heads, page numbers, declarations, and references are inside
the page box; there is no clipping, collision, overflow, or illegible text.
The final renders were byte-identical to the inspected renders after the
metadata-only rebuild.
