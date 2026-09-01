# Paper 24 Stage-5 finalization package

Status: **Stage 5 final paper complete; FULL completion checkpoint issued;
Stage 6 pending**.

## Locked deliverables

- `manuscript.tex` is the accepted marker-stripped LaTeX source, SHA-256
  `153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e`.
- `references.bib` is the accepted seven-entry bibliography, SHA-256
  `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87`.
- `content_proof.pdf` is the scholar-confirmed 15-page Stage-4.5 proof,
  SHA-256
  `7422198864a2c980c2033ab1851e4ef03886a4633cc644bb4fcef7b33576eaea`.
- `paper.pdf` is the reproducible 15-page A4 final PDF, SHA-256
  `8d690aa887c9aed27e1070b6bc840de333ff2d2de9f81a79945a034401025eeb`.
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
`f72efc209a139b7eb586b4db5b5b2ab9f8850d4728931c6c9f0882359c073931`.
The final log has 0 fatal errors, 0 undefined citations/references, 0 overfull
boxes, and 0 missing-glyph diagnostics; BibTeX reports 0 warnings. All 17 PDF
fonts are embedded. Five CID text fonts carry explicit Unicode maps; twelve
legacy Computer Modern Type-1 math subsets do not advertise ToUnicode in
`pdffonts`, so this package does not claim an all-font ToUnicode certificate.
Exact full-document Unicode text extraction is nevertheless demonstrated by
the proof/final text-hash equality. All 15 pages were rendered and visually
checked with no observed clipping, overlap, missing page, or illegible table.

Citation closure is 9 commands, 7 unique keys, and 7 BibTeX entries, with
0 missing, orphan, or duplicate keys. The formatter scan finds 0 ARS markers
and 0 hard-refusal tokens. Funding, conflict-of-interest, contribution, data
and code availability, ethics, and AI-assisted-research declarations remain
present.

## Scientific result and route boundary

The significant scientific result is unchanged: normalized trace divisibility
is ring-general rather than Gaussian-specific, while the signed first jet
improves finite loxodromic matrix compression (144 to 508 descriptors; largest
bucket 208 to 84) but leaves 10,468 collision rows and no singleton bucket.
This stops the tested scalar as an owner mechanism without constructing a
primitive-owner ledger or determinant.

Paper 24 remains at the early Route-A A0–A1 exploratory layer. The typed proxy
tuple stays
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; the complete
Bianchi flow is `UNASSIGNED`. Across the five-paper batch, positive arithmetic
A2 is `0/5`, Route-B invocations are `0/5`, and the 19 reported model
instances are not independent samples. Stage 5 gives no Route credit. The
governing hashes remain:

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
