# Paper 48 Improvement Log

Date: 2026-08-18 UTC.

## Plan phase

The first GPT-5.4 xhigh formal plan review returned HOLD at 7/10 with three
major issues:

1. binary paired-shell necessity was described as equality-only;
2. manuscript PLAN_READY and later protected-authority closure were not
   separated clearly; and
3. the page budget did not explicitly include floats and transition space.

The plan and claims matrix were repaired so that the binary construction
covers the full relevant bad range, the two gates are independent, and the
16–20 page occupancy budget includes the abstract and all floats.  The
same-specification recheck returned PLAN_READY at 9/10 with no critical or
major blocker.

## Draft and figure phase

- Generated the critical-surface PDF/PNG from the exact digit formula.
- Generated the digit-threshold and validation-census LaTeX tables from the
  frozen canonical summary.
- Created source-retained TikZ diagrams for the proof pipeline and the two
  pinching geometries.
- Wrote an eight-section manuscript and four technical appendices.
- Expanded the finite-shell trace-power limit and absolute convergence in
  the main text rather than relying on a certificate or finite computation.

## Paper improvement round 1

The GPT-5.4 xhigh review returned Revise at 8.8/10.  It found no theorem,
endpoint, trace/determinant, least-period, or ownership error.  Its one major
submission-readiness issue was internal workflow state in the publication
manuscript.  The revision:

- moved development hashes, route tokens, and protected-authority status out
  of the paper and into this candidate handoff;
- clarified the zero-completed fixed-length tensor boundary;
- changed the table notation to sigma_c(q=2);
- recast audit and adversarial replay prose in reader-facing terms; and
- retained a neutral statement that no external archival attestation is
  claimed.

## Paper improvement round 2

The final GPT-5.4 xhigh review returned ACCEPT at 9.4/10.  It reported no
critical, major, minor, or required action and explicitly verified
nonregression of every mathematical and evidence-boundary condition.

## Compilation evolution

- Round 0 PDF:
  31de17347040aaedeb848217a95f4608360155b75092a88d876b9cb4b29b56f3.
- Round 1 PDF:
  6fa88f1a3901776484dcfe8f1914e5167a5ad45501e4061d31483295012e52d6.
- Round 2 accepted PDF:
  6fa88f1a3901776484dcfe8f1914e5167a5ad45501e4061d31483295012e52d6.
- Withdrawn predecessor after two nonsemantic visual-QA copyedits:
  daaf6435625c6f1206f3e1faaec090619f2bc2750be5e1b4ca2cf748c0063867.
- Repaired pre-closure candidate PDF:
  5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573.

All preserved reviews and PDFs are under reviews/ and
paper/review_artifacts/.

After the accepted round-2 artifact was frozen, page-by-page visual QA
removed one duplicated word in a cross-reference and changed the table
header from sigma_c(2) to sigma_c(q=2), matching the already-reviewed
caption.  No formula, claim, datum, proof step, or domain changed.

## Pre-closure HOLD repair

The predecessor `daaf6435625...` was withdrawn after an exact extraction,
bibliographic, and frozen-scope audit.  The repair made four bounded changes:

1. Every explicit stretchy-size delimiter that emitted an extension-font
   control glyph was replaced by a fixed semantic delimiter.  The preamble
   now loads the generic and Computer Modern glyph-to-Unicode maps and
   enables `\pdfgentounicode`.  Poppler default/layout/raw and PyMuPDF now
   each have zero illegal C0, DEL, C1, U+FFFD, or Private Use Area characters;
   the unsanitized bbox XHTML parses directly as XML.
2. The Lucas record for DOI `10.24033/bsmf.127` was corrected from volume 2
   to official volume 6 in both the bibliography and source-verification
   ledger.
3. Section 6 was restored from a bilateral \(\mathbb Z\)-indexed shift to the
   frozen one-sided \(\mathbb N_0\)-indexed edge shift.  The periodic-word
   definition now explicitly repeats to the right.  The least-period sets
   and witnesses are unchanged, and no broader dynamical scope is claimed.
4. Page text density was recomputed as Unicode code-point counts after
   removing characters satisfying `str.isspace()`.  The exact minimum is
   page 7 with 1,180 non-whitespace characters.  The earlier “greater than
   1,200 characters” statement was a byte-count characterization and is
   withdrawn.

Two fresh fixed-epoch lanes independently regenerated the plot and tables,
then rebuilt the paper.  All generated assets and the two PDFs are
byte-identical.  Sixteen fresh page renders were visually checked; final
logs, fonts, citations, three Poppler modes, PyMuPDF text, and raw bbox XML
all passed their stated checks.  The retained audit material is under
`paper/logs/preclosure/`, `paper/preclosure_builds/`, and
`paper/previews/preclosure/`.

The accepted round-2 record remains historical evidence for the preserved
round-2 artifact.  It is not silently treated as an independent review of
this repair.  The writer-side nonregression ledger supplies exact anchors for
the independent writer audit.

## Procedural incident record

Early in extraction-script creation, one direct patch invocation inherited
the shared mirror working directory and briefly created
/root/autodl-tmp/symbolic_dynamics/scripts/extract_canonical_results.py.
The intended bytes were copied to the writer candidate and that exact mirror
file was immediately deleted.  The root coordinator was notified and
acknowledged the incident; the mirror will be atomically rebuilt by the root
workflow.  All subsequent patches were invoked through an explicit
/tmp/paper48_writer_candidate working directory.  No authority, Git,
README, integration-candidate, or protected-output content was modified.

Several generated diagnostic logs were also initially redirected to
top-level /tmp names.  They were moved into logs/transient/ inside the
candidate, and no such top-level diagnostic files remain.  They contained
build or asset-regeneration output only.

## Protected closure and remaining external gate

After the live P48 authority independently reached its post-output state, the
writer took two canonical captures without modifying that authority.  The
captures are byte-identical and cover 75 protected nodes (57 files and 18
directories).  The portable manifest is
`PROTECTED_STATEA_TREE.tsv`, SHA-256
`2c45b1c5cf683855b1a7b798edb719e9ab117d3223aa1d5cf4678efb12f16191`.
An independently implemented replay matched the sealed 59-node Stage-0 tree,
the exact 16-node output namespace, State-A tree `c23b5903...`, and the raw
post-output verdict hash `6f69cddf...`; its record has SHA-256
`d3db2a0579a96606da778c86f217849f2931b456f9e1e3556c307bd946c4d36c`.

The canonical science extraction was then repeated once against live State A
and frozen State B and once against the frozen A/B pair.  Both routes emitted
the same summary (`f3105dfe...`) and ledger (`dd1fbc2e...`).  Two fresh
fixed-epoch build lanes regenerated all data-driven assets and reproduced the
same repaired PDF (`5bb755f9...`).  Fresh Poppler default/layout/raw,
PyMuPDF, raw-bbox XML, font, citation, final-log, page-count, and structural
checks all passed; the structured QA record is `evidence/PDF_QA.json`.

The earlier `WAIT_PROTECTED_AUTHORITY` state is therefore retired.  The exact
minimal writer overlay is frozen in dependency order (content to manifest to
report to handoff to self-excluded seal), with controlling status
`HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.  This log does not claim CLEAN or grant
installation, publication, Git, README, mirror, or authority-write permission.
