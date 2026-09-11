# Historical auditor representation caveat

The byte-exact preserved historical independent auditor is io_lane/sources/original_inspect_build.py:
49,009 bytes / SHA-256 1e33d87282ef711a1a7ca0a8f13b3cd49a42ee0be2ac8596a7382e0c84e65a2f.
A new parent native cmp -s against the actual historical original exits 0; the
child already preserved its own complete original-source read/cmp evidence.

The top-level original_inspect_build.py display/source-lineage copy is
49,010 bytes / SHA-256 76586d13ecdc545ba1c2a26483d1225e8c3dbf2aff93444c59e260a18e669022:
apply_patch added one trailing blank line during main-agent copying.
The complete actual native diff is preserved in ORIGINAL_SOURCE_REPRESENTATION_NATIVE.json.
No executable line differs. That display copy was read/pinned, never imported or executed.
Its 49,010-byte pin was already accurately captured in each own run's ENTRY.
Do not call it byte-identical to the historical original; use the exact child copy
and the complete native original read result instead.

The top-level display copy and all old run input/source pins remain unchanged.
This new caveat is an immutable supplement; it does not rewrite run01–04 or
any historical source. The independent terminal checker is a separately
disclosed derivative with its own exact executed-source bytes and full deltas.

