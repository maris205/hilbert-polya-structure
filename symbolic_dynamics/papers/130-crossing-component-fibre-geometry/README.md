# P130 — Crossing-component fibre geometry

Status: **ANONYMOUS ROUND-2 / GO_INTERNAL / HOLD_EXTERNAL**.

The paper fixes a cut on a chord matching and replaces each crossing-graph
component by consecutive endpoint pairs.  Its contribution ceiling is narrow:
the all-size target-wise sibling-list inverse, the resulting pointwise fibre
product, and the unique largest-fibre target.  The one-step retraction,
Catalan image, connected-component enumeration, noncrossing transform,
A111088 coefficients and generic uncrossing/parallel-part geometry are
zero-credit background.  In particular, each nonempty immediate-sibling
list is an exact specialization of an Igusa parallel set; a degree-zero list
is only the singleton factor `A_0=1` bookkeeping used in the fibre product.
The static localization and compatible-merge mechanism receives no
contribution credit.

Package contents:

- `main.tex`, `references.bib`, `main.pdf` — anonymous round-two manuscript;
- `main_round0_original.pdf` — immutable pre-review PDF;
- `main_round1.pdf` — Review-A repair snapshot;
- `main_round2.pdf` — final internal-review snapshot, byte-identical to
  `main.pdf`;
- `code/verify.py`, `code/verification_output.txt` — deterministic exact
  verifier and canonical stdout;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`,
  `CONTROL_RESULTS.md`, `BUILD.md` — theorem, ownership and build records;
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md` and
  `IMPROVEMENT_LOG.md` — two independent reviews, consolidated disposition
  and repair record;
- `FINAL_QA.md`, `SHA256SUMS` — final mechanical QA and integrity manifest.

The controlling independent gate is
`../../docs/papers127_131_sequence/phase1/HOSTILE_GATE_CROSSING_PLANARISATION.md`.
It required the four-step all-size inverse and the owner subtraction now
present in the manuscript.  Round one made the parent-comparability
contradiction explicit, replaced the false uniform-gap wording by the
selected/unselected-child containment lemma, and closed the virtual-root
induction.  Round two closes Review B's two minor wording issues: the Igusa
specialization is restricted to nonempty sibling lists, with degree zero
treated as `A_0` bookkeeping, and P110 is identified as cyclic partition
shift--join dynamics.  The fresh verifier passed **735,609 assertions**; the
isolated four-stage build produced the same 4-page PDF as the local build.
Current `main.pdf` and `main_round2.pdf` have SHA-256
`c5a4fd3976a733c62a7f8f4e90b773cc6300970b9a25ac95b33f68a491f9c3fa`.
No novelty, priority, authorship, submission or external-release decision is
made.
