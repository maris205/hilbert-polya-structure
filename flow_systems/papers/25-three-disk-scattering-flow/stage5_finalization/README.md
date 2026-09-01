# Paper 25 Stage-5 finalization package

Status: **Stage 5 final paper complete; FULL completion checkpoint issued;
Stage 6 pending**.

## Locked deliverables

- `manuscript.tex` is the accepted marker-stripped LaTeX source, SHA-256
  `9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1`.
- `references.bib` is the accepted corrected derived eight-entry
  bibliography, SHA-256
  `a0bf0cd2f022f1b5dcc0bffdd1b28d135cef7c287f77c2a46e514480e2b3b5ab`.
  Canonical `paper/references.bib` remains unchanged.
- `content_proof.pdf` is the scholar-confirmed 13-page Stage-4.5 proof,
  SHA-256
  `34c5351403f81c22a16b8de0fa4e9011b0b3b5a5b7be6c321a25d47e4724fe65`.
- `paper.pdf` is the reproducible 13-page A4 final PDF, SHA-256
  `5968230a947956744c41d542a833e8cc165a0610980bb8bcdb3fed31c4f0198f`.
- `provenance_summary.md` carries the integrity, route, and package-verifier
  advisory boundaries. `submission_verification_report.json` is the
  machine-readable package audit and must pass freshness replay before reuse.

The citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`. Stage 5 changed
no scientific, declaration, citation, or bibliography content.

## Reproducible build

Set `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, then
run LuaLaTeX → BibTeX → LuaLaTeX → LuaLaTeX. Each LuaLaTeX call uses:

```text
lualatex -jobname=paper -interaction=nonstopmode -halt-on-error '\pdfvariable suppressoptionalinfo 512\relax\input{manuscript.tex}'
```

Two builds in completely independent temporary directories produced the same
PDF SHA-256 above. The final PDF and confirmed proof have the same
`pdftotext -layout` SHA-256,
`60aedb5e593ad6971ed37cda6206e2eab0aefc5653064f10f516f9208408b185`.
The final log has 0 fatal errors, 0 undefined citations/references, 0 overfull
boxes, and 0 missing-glyph diagnostics; BibTeX reports 0 warnings. Ten
underfull paragraph diagnostics in the Chinese abstract are retained as
nonblocking layout information. All 17 PDF fonts are embedded. Five CID text
fonts carry explicit Unicode maps; twelve legacy Computer Modern Type-1 math
subsets do not advertise ToUnicode in `pdffonts`, so this package does not
claim an all-font ToUnicode certificate. Exact full-document Unicode text
extraction is nevertheless demonstrated by the proof/final text-hash
equality. All 13 pages were rendered and visually checked with no observed
clipping, overlap, missing page, or illegible table.

Citation closure is 13 commands, 8 unique keys, and 8 BibTeX entries, with
0 missing, orphan, or duplicate keys. The formatter scan finds 0 ARS markers
and 0 hard-refusal tokens. Funding, conflict-of-interest, contribution, data
and code availability, ethics, and AI-assisted-research declarations remain
present.

## Scientific result and route boundary

The significant scientific result is unchanged: period-two and period-three
owners have exact mean roofs `d-2a` and `d-sqrt(3)a`, whose positive gap
`(2-sqrt(3))a` proves nonconstant roof cohomology and rules out every global
owner- and repetition-preserving substitution `z=exp(-cs)`. The 2,241-row
finite replay validates the frozen implementation but is not a second proof of
the theorem.

Paper 25 retains only an early Route-A A1–A2 typed symbolic calibrator. Its
tuple stays
`(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` and its
overall arithmetic route is rejected; the physical-flow tuple is
`UNASSIGNED`. Across the five-paper batch, positive arithmetic A2 is `0/5`,
Route-B invocations are `0/5`, and the 19 reported model instances are not
independent samples. Stage 5 gives no Route credit. The governing hashes
remain:

- `skills/route-a-evaluator.md`:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- `skills/route-b-evaluator.md`:
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

## Non-clean advisories and release boundary

- #660 remains `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
  SNAPSHOT_NOT_PROVIDED`; no clean tortured-phrase result is claimed.
- #672 remains `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE`; no carrier or
  agreement result exists.
- Pandoc/DOCX remains withheld: the preflight replay found material loss of
  theorem, mathematics, and citation structure.
- No venue profile is declared. Venue limits are therefore not checked and no
  venue-readiness, submission, or public-release claim is made.

The canonical `paper/` and `results/` trees were not modified. No submission,
upload, external contact, Git action, or Stage-6 transition has occurred.
