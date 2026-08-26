# GPT-5.4/xhigh official Round 1 — author resolution

**Status:** all requested Round-1 revisions implemented and author-side checks
completed. This document records the authors' response; it is not a Round-2
review verdict. External release remains **HOLD**.

The complete hostile review is preserved without alteration at
`reviews/GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md`. It supplied no numerical
score, so none is inferred here.

## Frozen snapshots

- Pre-review manuscript:
  `main_pre_gpt54_round1.pdf`, 10 pages, 368,885 bytes,
  SHA-256
  `1ef742b0bd882e179185db0d57413c65cde496d53711495eff5b96c9e3cd386e`.
- Revised manuscript:
  `main_gpt54_round1.pdf`, 10 pages, 371,616 bytes,
  SHA-256
  `09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08`.
- `main.pdf` is byte-identical to the revised snapshot.

## Finding-by-finding resolution

| Official Round-1 finding | Author resolution | Synchronized files |
|---|---|---|
| Step 4 used the known-base Vandermonde lemma at index zero without stating that case, and blurred the recovered coefficient with the signed multiplicity difference | Lemma 5.1 now permits any \(r\) consecutive nonnegative indices, explicitly including \(m_0=0\). Theorem 5.2 now uses \(R_0,\ldots,R_{r-1}\), recovers \(b_d=(c_d^+-c_d^-)/d\), and only then multiplies by the already recovered \(d\) to obtain \(\delta_d=c_d^+-c_d^-\). | `sections/5_moment_recovery.tex`, `sections/1_introduction.tex`, `PROOF_PACKAGE.md`, `CLAIMS_EVIDENCE.md`, `NARRATIVE_REPORT.md` |
| Existing controls did not exercise the Frobenius--Schur zero branch | Added an exact \(C_3\) control. The script checks all group axioms, derives indicator signature \([1,0,0]\), compares direct and character-formula Hom/fixed counts, and runs the complete reconstruction/trichotomy. | `code/verify_surface_flat_sft.py`, `code/verify_surface_flat_sft.out`, `CONTROL_RESULTS.md`, `sections/7_scope_controls.tex`, `CLAIMS_EVIDENCE.md` |
| The former terminology was misleading for the all-modulus probes | Replaced it throughout author-facing manuscript and package material by “families” or “divisibility-directed families.” The divisibility direction remains explicit. | `sections/*.tex` and the package Markdown ledgers/reports |
| Klug's role needed sharper historical wording | Klug is now identified as the chosen modern normalization source/account. The text explicitly preserves historical ownership of the classical Mednykh and Frobenius--Schur formulas, without adding unverified original metadata. | `sections/1_introduction.tex`, `sections/2_background.tex`, `sections/7_scope_controls.tex`, `CITATION_AUDIT.md` |

## Exact zero-indicator control receipt

For \(C_3\), the frozen computation records:

- group axioms: PASS;
- irreducible-degree/indicator data:
  \(d=(1,1,1)\), \(\nu=(1,0,0)\);
- orientable fixed counts for \(m=1,\ldots,4\):
  \([243,19683,1594323,129140163]\);
- nonorientable fixed counts for \(n=1,\ldots,5\):
  \([9,81,729,6561,59049]\);
- normalized moments \(P=(3,3,3,3)\), \(Q=(1,1)\), and
  \(R=(1,1,1)\);
- reconstruction
  \((c_1^+,c_1^-,c_1^0)=(1,0,2)\): PASS.

The rerun output is byte-identical to
`code/verify_surface_flat_sft.out`, whose SHA-256 is
`c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d`.
The \(D_8/Q_8\) separation and \(S_3\) cross-order checks also remain passing.

## Build and author QA

- Full build:
  `pdflatex -> bibtex -> pdflatex -> pdflatex`; every command exited zero.
- Final log search: zero warnings, undefined references/citations,
  multiply-defined labels, overfull boxes, underfull boxes, or errors.
- Terminology gate: active manuscript and standing package sources use only
  “families” or “divisibility-directed families”; reviews and author audit
  history retain the superseded word solely to record the finding.
- Malformed-exponent gate: zero source matches for the literal `^{,`.
- PDF: 10 A4 pages, 371,616 bytes; 23 font records, all embedded and subset;
  empty Author metadata and no volatile PDF dates.
- Layout-preserving text extraction: 576 lines, 4,894 words, 38,387 bytes.
- Author visual inspection of revised pages 6, 7, and 9 confirms the expanded
  moment lemma, corrected Step 4, and the \(C_3\) zero-indicator control are
  legible and unclipped.

No priority claim is made. Official Round-2 review remains pending, and the
external-release state remains **HOLD**.
