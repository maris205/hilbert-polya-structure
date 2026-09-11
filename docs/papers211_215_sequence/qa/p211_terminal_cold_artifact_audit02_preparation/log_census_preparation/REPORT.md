# Cold-build 2 log-census auditor source preparation

Status: **SOURCE_PREPARATION_NO_RUN**. The complete cold2 log input set and a new standalone auditor-function source are ready for parent source reception. No auditor function, Python, TeX, scientific/controller program, host query or page-view tool was executed. No cold1 or cold2 original was changed.

Use [diagnostic_census.source_only.v02.py](diagnostic_census.source_only.v02.py): 12,924 bytes; SHA-256 228614c455a09f80f6c25c97c1315a1cdb2a3be6e5ac97a17ca64a19e46d6665. It supplies the requested diagnostic_census() using the documented helpers/globals; [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md) states its exact additional input and integration obligations. It has not been imported, compiled or tested.

## Actual cold2 inputs and observations

[RAW_LOG_ROLES.json](RAW_LOG_ROLES.json) resolves the eighteen roles from cold2's own actual tree: eight main.log copies, six main.blg copies, and four pass/BibTeX stdout files. All 18 were read completely with archived native request/results and native raw SHA-256/byte counts: 241,382 bytes total. All returned text is ASCII with complete transported length equal to native bytes. Final repeat inventories and all raw hash/size listings are unchanged.

The actual cold2 text—not an assumption from cold1—contains a font-expansion warning in pass2 log line 624 and pass3 log line 608:

> pdfTeX warning (font expansion): font should be expanded before its first use

The three after-pass logs are:

| Role | Bytes | Lines | Emitted warning lines | Undefined matching lines | Underfull diagnostics |
|---|---:|---:|---:|---:|---:|
| pass1 | 27,506 | 737 | 31 | 29 | 1 |
| pass2 | 26,096 | 671 | 8 | 5 | 2 |
| pass3 | 25,362 | 643 | 1 | 0 | 2 |

Exact pass1 SHA-256: e93dc0a15a6292d9f2d15a84d7885ce8bec66f29df9a58e8175937b77c103916.
Exact pass2 SHA-256: d67af1d6530912713852c11275ffc9273c385617b42bba88e7a9a12c84fec3dc.
Exact pass3 SHA-256: 23cd58bfffd50cd3d9d9a3d441ff1da30e1e7f55c00df697740a2e4a8508dc0a.

[COLD2_LOG_CENSUS.preparation.v02.json](COLD2_LOG_CENSUS.preparation.v02.json) contains every case-insensitive warning/undefined/missing-character/overfull/underfull/rerun/error-or-fatal literal match, its exact line and ±2-line context, for all eighteen actual bodies. Literal counts are not emission counts: final log's two “warning” literal lines comprise the engine warning and package metadata; five “rerun” literal matches are loader/Info records, not actual final rerun requests. The two microtype character-029 Info contexts explicitly concern ignored protrusion settings; they are not actual TeX “Missing character” lines. The six BLG “warning$ -- 0” rows are function-call statistics, not emitted warnings.

The actual final log has no undefined matching line, actual TeX missing-character line, overfull diagnostic, or emitted rerun request; it retains two underfull diagnostics and the engine warning. This is preparation collation only, not evidence that the warning is harmless or that glyphs are lost. No diagnostic is accepted, waived or closed here.

This lane did not open cold2 MEASURED_NOT_VIEWED.json. The proposed future function must read that actual separately bound input and dynamically compare its warning array with emitted final-log warnings, preserving multiplicity. It never imports the prepared census as checks and contains no assumed cold1 warning/count. Future root diagnostic disposition remains required.

## Preservation and limits

All native request/result objects are retained under native/. There were no failed or truncated native reads in this preparation. Both source/census drafts are preserved; only v02 is designated. The small revision explicitly classified BibTeX counter metadata and added a DETAILS no-overwrite guard; neither draft was run.

The project workflow was read completely and used to keep preparation, actual execution, diagnostic disposition, visual review and terminal acceptance separate. Relevant current state/index excerpts were also read; they are recovery context, not substitutes for the underlying cold2 records. Parent owns full native/runtime/capture-specific source and its later source reception. This packet supplies no full cold2 artifact audit, no manuscript review, no build acceptance, no terminal PASS and no external action.

The complete nonself manifest is constructed from actual native payload hashes plus exact newly serialized sealing records. Parent must independently verify it when receiving this source-preparation packet. OWNER_AMBER / HOLD_EXTERNAL remains in force.
