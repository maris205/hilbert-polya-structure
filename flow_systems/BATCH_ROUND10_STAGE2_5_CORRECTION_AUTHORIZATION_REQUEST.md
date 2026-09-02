# Round 10 Stage 2.5 finding-specific correction authorization request

Date: **2026-09-02 UTC**

Scope: Papers 29--33, Stage 2.5 integrity only. This request does not authorize
scientific execution, a new scientific result, a Route-A tuple, Route B, Stage
3, or collateral rewriting.

## Finding 1 — P29 reference metadata (blocking MEDIUM)

`P29-AB-MEDIUM-01`: the `P29-S15` chapter record correctly identifies the
chapter, author, title, pages, series volume, year, publisher, and DOI, but the
containing volume currently lists only Graham Higman as editor. The AMS
publisher advertisement, CiNii catalogue, and Google Books catalogue identify
S. I. Adian, W. W. Boone, and Graham Higman as the three editors.

Authorized target if confirmed:

- `papers/29-bianchi-ideal-owner-refinement/paper/references.bib`
- `P29-S15`, replace exactly
  `editor = {Higman, Graham}` with
  `editor = {Adian, S. I. and Boone, W. W. and Higman, Graham}`.

No other P29 bibliography field or manuscript prose may change.

## Finding 2 — P31 `G/I/C` reconstructability (blocking MAJOR)

`P31-E1-056`: the manuscript correctly defines `I` as the complete 138-row
input-to-owner incidence relation, `G` as the global owner projection, and `C`
as the cell/owner deduplication. It then overstates that publishing *any one*
of these surfaces destroys the information needed to reconstruct the other
two. Under the manuscript's own definitions, a complete `I` can induce both
`G` and `C`; only `G` or `C` alone loses the occurrence-level information
needed to reconstruct `I`.

Authorized target if confirmed:

- `papers/31-level11-conjugacy-owner-ledger/paper/manuscript.tex`, only the
  two-sentence reconstructability passage in the `G/I/C` subsection.
- Replace the universal nonreconstructability assertion exactly with:
  “Publishing only `G` or only `C` would destroy occurrence-level information
  needed to reconstruct `I`; conversely, a complete `I` can induce `G` and
  `C` by the stated projections, but separate materializations make the
  transformations independently auditable. For that reason their schemas,
  validation rules, and summary statistics should be declared
  independently.”
- In the conclusion, replace the stale generic statement that originality is
  unassessed exactly with: “The source corpus remains passage-unresolved. A
  bounded Stage 2.5 textual-originality screen found no exact match within its
  declared samples and corpora, but scientific contribution novelty remains
  unassessed; the formal Route-A tuple remains `UNASSIGNED`, positive
  arithmetic A2 remains absent, and Route B remains closed.”

Preserve all frozen counts (`138`, `55`, `9,453`), definitions, Route state,
nonexecution statement, and all other P31 scientific or methods claims.

## Finding 3 — P32 verified source-identity state (nonblocking MINOR)

`P32-AB-MINOR-01`: the authoritative journal record and the independent CERN
catalogue now verify the identity and metadata of `P32-S13` (Selberg 1956).
Four live English status statements and one Traditional-Chinese abstract
statement still call the record `PLAUSIBLE`. The historical Phase-2 sentence
that reports the earlier 25/1 classification remains accurate as history and
must not change. Bibliographic verification does not create a passage locator
or strengthen any scientific claim: `anchor=none`, background-only use, and
`claim_to_passage=INCONCLUSIVE` remain fixed.

Authorized targets if confirmed:

- `papers/32-homology-cover-renormalization-uniformity/paper/manuscript.tex`
  only at the current-state statements in the English abstract, Traditional-
  Chinese abstract, Section 2.3, limitations, and conclusion.
- Replace only the stale source-identity label with wording that says P32-S13
  is bibliographically `VERIFIED` but remains background-only.
- Preserve the historical Phase-2 sentence (`25 VERIFIED and P32-S13
  PLAUSIBLE`) byte-for-byte.
- Preserve every scientific assertion, owner/time/normalization definition,
  citation key, `anchor=none` marker, `INCONCLUSIVE` marker, Route state, and
  nonexecution statement.

## Allowed follow-through

If all three findings are confirmed, the agent may:

1. apply only the exact scoped replacements above;
2. rebuild only the affected P29, P31, and P32 PDFs in isolated temporary build
   directories using the existing plainnat numeric-citation toolchain;
3. add a repair-lineage receipt and post-repair input freeze;
4. regenerate only affected Stage-2.5 claim/evidence/originality sidecars;
5. re-run bibliography, citation, build, claim-coverage, evidence-row,
   claim-drift, integrity, and regression validators;
6. stop and request new authorization if any other canonical byte, scientific
   claim, numerical value, Route state, or registered claim strength would
   have to change.

The pre-repair Stage-1/Stage-2 artifacts remain immutable historical records.
Stage 3 remains unauthorized until the completed Stage-2.5 checkpoint is
shown to the scholar and separately confirmed.
