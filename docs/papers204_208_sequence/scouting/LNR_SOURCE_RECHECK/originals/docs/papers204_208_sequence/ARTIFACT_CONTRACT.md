# Paper/review artifact roles for the new five-seat batch

This layout is fixed before the first paper review. It adapts the inherited
hostile-review procedure to modular short manuscripts without changing any
historical package or parser. Root must implement/check this layout directly;
an old-layout audit result is not reused as a new-batch PASS.

## Scientific and frozen inputs

Each numbered paper has `main.tex`, `math_commands.tex`, `sections/*.tex`,
`references.bib`, `PROOF_PACKAGE.md`, `verify.py`, and `CANONICAL.json`.
The local verifier imports no pilot, old-paper or reviewer implementation.
`PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`, and
`SOURCE_AUDIT.md` bind framing and claim/source scope. `README.md` records
the actual lifecycle and authorship. An author execution receipt names the
complete fresh replay pair and byte comparisons.

`frozen_round0/`, `frozen_round1/`, and `frozen_round2/` are physical,
immutable copies of the respective accepted scientific/documentary input
sets, including the PDF available at that freeze. Each has a complete
directory-relative nonself `SHA256SUMS`. Freeze 1 follows accepted A delta;
freeze 2 follows accepted B delta. Rejected numbered papers remain present.

## Exactly two manuscript-review packages

Locations are `reviews/pNNN_a/` and `reviews/pNNN_b/` under this batch.
Their roles are:

| Artifact | Required content |
|---|---|
| `REPORT.md` | Exact verdict, provenance, claim-by-claim attack, finding census |
| `verify.py`, `CANONICAL.json` | One standalone independent checker and its complete actual stdout |
| `REPLAY_LOG.md` | Commands, interpreter/settings, child exit codes, complete output/byte comparison receipt |
| `SOURCE_AND_PROOF.md` | Deductive route, literal collision subtraction and primary-source contexts/read limits |
| `BUILD_REPORT.md` | Actual source-only build and actual page inspection, with input/output pins |
| `INPUT_PINS.sha256` | Complete reviewed scientific/documentary freeze inputs, workspace-root-relative |
| `FINDINGS.json` | Severity-labelled findings with exact open/resolved state; no open mathematical/evidence finding at acceptance |
| `DELTA.md` | Reviewer-accepted exact repaired or no-change delta, with before/after pins |
| `SHA256SUMS` | Complete directory-relative manifest of every review artifact except itself |

Additional real evidence such as original build logs, independently generated
tables, PNGs, or a frozen initial finding report belongs in the package and
must be covered by its manifest. Empty templates do not count as reviews.
Reviewer A starts from pinned Round 0; B starts from pinned Round 1 and uses
a materially different representation from both the author and A. The two
reviewers must be distinct nonauthor processes. Candidate-gate familiarity
is disclosed and never substituted for manuscript review.

Root inspects originals and executes each author/A/B checker twice during
the final gate, comparing actual stdout with its canonical bytes. A prior
valid pair may be reused only under the workflow's full dependency key,
with that reuse clearly labelled; the first five-paper terminal gate still
checks all five contracts.

## Terminal builds and views

`qa_final/cold_build_1/` and `cold_build_2/` begin from source-only inputs:
the live final TeX, bibliography, required local resources/styles, and no
auxiliary or PDF products. Two actual physical builds run. Record the
engine, environment settings, input/source hashes, full logs, exit codes,
page counts, unresolved-reference/citation checks, fonts, and PDF hashes.
Use explicit reproducible build settings and compare the PDFs when claiming
byte identity. Render every final PDF page and actually view it; file
existence or a digest is not a viewing receipt.

The final batch auditor checks all five admitted contracts, freezes, review
deltas, zero current findings, replay pairs, builds, all-page viewing records,
link closure and complete nonself manifests. Every internal result retains
`OWNER_AMBER / HOLD_EXTERNAL`. Private Git synchronization is a separate
evidence-backed action and never means public release.
