# Decoder V2 — exact two-finding source repair

SOURCE_ONLY / HOLD_OPERATIONAL / HOLD_EXTERNAL. Original four files remain
unchanged, including V1's two independently identified defects. V2 is the
new decode.v2.proposed.mjs.txt carrier; CONTRACT.md applies with these
explicit clarifications. No independent acceptance is yet claimed.

1. Before any PT_DYNAMIC tag interpretation, require filesz <= memsz and
   require fileAt(d.vaddr,d.filesz,d.span) === d.offset. The reused fileAt
   proves one and only one file-backed PT_LOAD translation for the entire
   parsed dynamic span. Failure retains header/program records and exact
   dynamic program-header span as HOLD_DYNAMIC_FILESIZE_GT_MEMORY or
   HOLD_DYNAMIC_FILE_VADDR_MAPPING_MISMATCH (or existing mapping HOLD).
   The existing positive/aligned size and in-file terminated NULL/tail
   checks remain; no runtime address or arbitrary file alias is followed.
2. Move only the needed-name filter and cache-candidate census insertion
   below row construction and hwcaps extension/index/string validation.
   Every row now receives those structural checks even if its name is
   irrelevant. Emission and named-state census remain same-name only.
   A malformed unrelated hwcaps reference sets the exact row-span HOLD;
   earlier emitted candidates remain and complete_same_name_scan stays
   false. No malformed record is silently skipped by name filtering.

No other source edits, bounds, loader/cache support, manifest authority,
source-role/selection claim or operational permissions change. Existing
32/96/64 ceilings and all original partial-result catch boundaries remain.
DATA_REQUEST.v2.proposed.json differs from V1 only in proposed_source.

The independent finding cites the loader's use of dynamic virtual address
and memory extent. This repair directly reconciles that program-header
view with the existing unique-file-mapping helper; it does not certify an
installed loader version. Same reviewer must receive the exact V2 delta.
No source import, execution, syntax/AST test or actual captured-body parse.
