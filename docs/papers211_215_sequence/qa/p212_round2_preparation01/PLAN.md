# P212 physical Round2 and terminal handoff preparation

Status before execution: SOURCE_ONLY. Final A, physical Round1, final B and
B's exact empty manuscript delta are accepted. This packet proposes the exact
three-document lifecycle update and one fixed 25-payload Round2 copy. It does
not itself grant a copy, build, review, science run, completion, Git action, or
external release.

`originals/` preserves the three live Round1 lifecycle bodies byte-for-byte;
`proposed/` records the complete post-B bodies. The changes only describe
accepted evidence and remaining obligations. They do not alter theorem rows,
proofs, verifier, parameters, canonical output, manuscript TeX/Bib, or PDF.
The accepted B delta is empty for manuscript sources and does not include
these later lifecycle documents.

`FILES.tsv` preserves all Round1 destination roles and order. Its first 24
source paths are identical to Round1; only the final scope source changes to
`p212_round2_binding01/FREEZE_SCOPE.md`. Expected Round1-to-Round2 change:
three lifecycle roles plus `FREEZE_SCOPE.md`; the other 21 payloads must be
whole-byte equal. The guarded recipe creates only absent `frozen_round2`,
copies each fixed source with no-clobber and raw comparison, and generates a
directory-relative nonself manifest. Failure is preserved without cleanup or
retry.

Root-compatible adoption requires: compare all originals to live and all
non-lifecycle mapped roles to Round1; verify accepted A/B originals and zero
current findings; apply exactly the three complete proposals; recompare live
to proposals; bind every current source, map, recipe and scope; issue one
single copy grant; then independently verify exact membership, all raw pairs,
the nonself manifest and the 4/21 changed/unchanged delta.

Only after physical Round2 may two separately bound source-only terminal
builds run. Each must start from a different absent cold output directory,
copy only the eight TeX/Bib inputs from frozen_round2, retain every pass and
diagnostic artifact, and render every actual page. Existing A/B products and
grants cannot be relabelled or reused. HOLD_EXTERNAL remains.
