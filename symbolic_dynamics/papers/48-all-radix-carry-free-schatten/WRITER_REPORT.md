# Paper 48 writer closure report

Candidate: `SD-C50` / paper 48 writer overlay

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

This is a writer-side closure record.  It is neither an independent writer
audit nor an installation, publication, protected-authority write, Git,
README, or mirror authorization.  It does not claim CLEAN.

## Outcome and evidence boundary

The overlay contains a complete anonymous 16-page A4 manuscript on the
positive-integer carry-free radix operator.  Its infinite Schatten, endpoint,
trace, determinant, and least-period conclusions are proved analytically in
the manuscript.  Finite evaluator lanes, machine PASS fields, mutations,
protected-tree checks, and the externally supplied post-output verdict are
validation and provenance evidence only; none is promoted to a proof of an
infinite theorem.

The paper keeps the two-sided phase identity
`B_(b,s)=U_t B_(b,sigma) U_t`, distinguishes active from hidden digit walls,
uses the binary paired-shell compression across the full necessary range,
restricts ordinary trace and determinant to trace class, asserts the
regularized-determinant logarithm only locally, deletes the zero word, and
uses only the frozen one-sided edge shift.  It makes no priority,
exhaustiveness, composite-radix Kummer, completed-function, or target-divisor
claim.

## Protected State-A closure

Two canonical live captures produced identical portable manifests.  The
final `PROTECTED_STATEA_TREE.tsv` has 75 rows after its header: 57 regular
files and 18 directories, including the root.  Its SHA-256 is
`2c45b1c5cf683855b1a7b798edb719e9ab117d3223aa1d5cf4678efb12f16191`.

An independently implemented replay verified:

- exact sealed Stage 0: 59 nodes, 44 regular files, 15 directories;
- exact declared `outputs/`: 16 nodes, 13 regular files, 3 directories;
- State-A tree:
  `c23b59034303af74f2a9433b92f9f5c1e1cce4510bd8032ef1214372390bda58`;
- preoutput seal `2726c5ea...`, static manifest `663400ef...`, base/static
  inventory `133b8e...`, preauthority ledger `f5669e...`, and integration
  contract `dcbf0029...`;
- externally supplied post-output verdict raw SHA-256:
  `6f69cddfd069d267e5a71f8ec342df71c31d456152a8ba910d93829daadcb5f9`.

The replay JSON has SHA-256
`d3db2a0579a96606da778c86f217849f2931b456f9e1e3556c307bd946c4d36c`;
the 44-file Stage-0 sums file has SHA-256
`a9a32253171ea307271fd7e8fec9ffac0a449eb07ec72db0ff20255ba3b5ec91`.
The external verdict is reported only as an authenticated input.  This writer
record does not adopt its disposition as a writer-side CLEAN claim.

## Canonical science and reproducibility

Canonical extraction was repeated by two routes: live State A plus frozen
State B, and frozen State A plus frozen State B.  Both emitted byte-identical
artifacts:

- summary SHA-256:
  `f3105dfe1733bcd8aa240d9ebcf9125acc44704a96d7c5682fbf991381548b3d`;
- results-ledger SHA-256:
  `dd1fbc2ee0fb16bf4df7ff74cbc2dc59fa00e02e18d545f3b782c1ee4f55fc62`.

The replay checked 1,965 finite rows per lane, 8,010 digit-interval
comparisons, and 420 shell-envelope rows.  These counts are controls, not
proof premises.

Two fresh fixed-epoch lanes independently regenerated the plot and both
tables, then rebuilt with `SOURCE_DATE_EPOCH=1787011200`.  Both lane PDFs and
the named PDF are byte-identical at SHA-256
`5bb755f9b2b0eaf56c79b8de5e94253bc9e7ed4b8d6ef9fd4c815f832cf54573`.
The predecessor
`daaf6435625c6f1206f3e1faaec090619f2bc2750be5e1b4ca2cf748c0063867`
is withdrawn and is absent from the overlay.

Fresh PDF QA passed with record SHA-256
`35ca8645da483bf30c098a9f5c66db83f75dd01dc423b180ec434805e6021ed1`:
all four extraction families have zero illegal C0, DEL, C1, U+FFFD, and
Private Use Area characters; unsanitized raw bbox XHTML parses directly as
XML; all 33 font rows are embedded, subset, and ToUnicode-mapped; citations
are closed; the final log is warning-free; and the exact Unicode
non-whitespace minimum is page 7 with 1,180 characters.  Byte identity with
the previously inspected 16-page PDF supplies visual nonregression.

## Bounded pre-closure repairs

The final source corrects four isolated issues without changing the theorem:

1. semantic delimiters and explicit glyph-to-Unicode maps replace the
   extension-font constructions that caused illegal extraction controls;
2. Lucas DOI `10.24033/bsmf.127` has official volume 6 in both source ledger
   and bibliography;
3. Section 6 uses the frozen one-sided `N_0` shift rather than a bilateral
   shift; and
4. page-density reporting uses Unicode code points, withdrawing the earlier
   byte-count description.

The final bibliography and compile log have SHA-256 values
`5134393a0988d7ace63593598c8a35703057d06c225ed9de85ca92405f87526a`
and
`70355e1f5afe9ae91ebc5555885269e856caddb5f60b22e16c527b03c9f906f1`.

## Reviews

The formal plan gate progressed from HOLD 7/10 to PLAN_READY 9/10.  The same
GPT-5.4 xhigh manuscript reviewer returned Revise 8.8/10 in round 1 and
ACCEPT 9.4/10 with no required action in round 2.  That acceptance predates
the bounded repairs and is retained as historical evidence, not silently
transferred to the repaired PDF.  The writer-side nonregression ledger and
exact anchors are included for independent audit.

## Exact minimal writer overlay

`PAPER_MANIFEST.tsv` has exactly 50 sorted content rows and SHA-256
`dc202c75ce087f944f42ab39f6ba75d616a100dcc4e6822a2a8154d0f6269efa`.
It excludes exactly itself, `WRITER_REPORT.md`, `HANDOFF.md`, and
`WRITER_SEAL.json`.  After closure the overlay contains 54 regular files,
all mode 0644, and 11 directories including the root, all mode 0755.

The overlay contains no symlink, cache, LaTeX auxiliary, `outputs/**`,
`evidence/publication_gate/**`, frozen protected copy, Git path, README, or
mirror path.  Candidate-only build lanes, raw extraction files, rendered
previews, and transient logs are intentionally outside the minimal overlay.
The dependency direction is content to manifest to report to handoff to
self-excluded seal.  No manifest-covered file contains the writer-seal hash.

## Procedural transparency

The improvement log preserves the earlier direct-patch mirror incident: one
transient script was created in the shared mirror and immediately deleted,
the root coordinator was notified, and subsequent patches used the explicit
candidate working directory.  This closure wrote only under `/tmp`; it did
not modify the live authority, integration candidate, Git, README, or mirror.
