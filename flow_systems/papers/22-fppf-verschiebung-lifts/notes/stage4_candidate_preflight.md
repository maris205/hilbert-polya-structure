# P22 Stage 4 five-item candidate preflight

Date: **2026-08-25**

Status: **PASS FOR THE FIVE INCLUDED ITEMS; NOT A FINAL STAGE 4 PATCH**

The writer-emitted candidate
`notes/stage4_revision_patch_candidate_no_rev003.json` at SHA-256
`47da386e9fb3939fce60dcbf57f5d9be03851e53f036de2cde0254f2009856d3`
contains only `REV-001`, `REV-002`, `REV-004`, `REV-005`, and `REV-006`.
It deliberately omits `REV-003`, whose byline, contribution, funding, and
competing-interest values have not been supplied by a human author.

## Deterministic authorization/apply preview

The current ARS applier replayed the candidate in a temporary directory with
the exact anchored base, block manifest, immutable roadmap, author
adjudication, and claim-surface manifest.

```text
authorization_status=pass
report_format_version=1.3
ops_applied=9
blocks_total=102
blocks_touched=9
blocks_preserved_byte_identical=93
preserved_ratio=0.9118
fresh_block_ids=[B0103, B0104, B0105, B0106]
structural_flags.any=false
touched_ratio=0.0882
unregistered_claim_drift_review_required=true
preview_output_draft_hash=bde9a13bf90d
```

No heading was touched, the section count did not change, and the touched
ratio stayed below the 0.6 structural threshold.  The original anchored base
and all official manuscript artifacts were not modified.

## Token-conservation advisories

The advisory checker reported three expected, roadmap-attributed deltas:

1. `B0022 / REV-001`: added search date and primary-source proposition/page/
   Stacks-tag locators required by the auditable literature comparison.
2. `B0023 / REV-006`: added the abstract source-section notation `z_0` and
   the short-exact-sequence/template notation needed to close the logical
   bridge identified by independent audit.
3. `B0092 / REV-006`: restored the explicit theorem bound `N>1` in the
   conclusion-level template recap.

No citation token or protected-term delta was reported.  These rows are
advisories, not a semantic-fidelity certificate; independent review remains
required because all revised claim surfaces are unregistered under the
current contract.

## Temporary full build

After mechanically removing block markers from the temporary apply output,
the preflight ran LuaLaTeX, BibTeX, and two final LuaLaTeX passes against the
unchanged verified `references.bib`.

```text
build=PASS
pages=13
page_size=A4
pdf_version=1.5
undefined_citations=0
undefined_references=0
overfull_boxes=0
missing_glyphs=0
fatal_errors=0
preview_unanchored_sha256=d60aee649208c1ed4287d544f38b9bf98554c5860003e31a3ebadd83e2b02b49
preview_pdf_sha256=d8a5603f3428d1dc879a89b3b2df753ee619cdb4c7a8d40f8dc7b4be20d3cff7
```

The preview directory was removed after the checks.  These two preview hashes
are diagnostics only; they are not final manuscript/PDF artifacts and do not
enter the revision-evidence bundle.

## Hold condition

Do not apply or promote this candidate as the Stage 4 round.  A single final
patch must also contain the four human-approved `REV-003` replacements before
the official deterministic apply, Schema 8 completion, continuous evidence
bundle, final build, and Stage 4 mandatory checkpoint can close.
