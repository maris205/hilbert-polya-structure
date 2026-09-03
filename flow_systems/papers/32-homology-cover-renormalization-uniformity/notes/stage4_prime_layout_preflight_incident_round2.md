# Paper 32 Stage 4-prime layout preflight incident (Round 2)

- Recorded at: `2026-09-03T18:33:48Z`
- Scope: independent application and isolated preview of the authorized Stage 4-prime Round-2 writer patch
- Result: `FAIL_CLOSED_LAYOUT_ONLY`
- Scientific values changed by this incident handling: `no`
- Canonical manuscript, bibliography, PDF, science directories, route state, and registered claim surfaces changed: `no`

## Frozen first attempt

- Patch SHA-256: `6e7a93bb08a7cd2e2c3d91aca8f09be03f72bdf455fd76fdf9133bfa5725a9aa`
- Applied draft SHA-256: `b81355f5d808660b572c1dc795c7e4a26560b2899fa385a62969179c5316345c`
- Apply report SHA-256: `60129658386f502a964361e85cccc51245dcb2193a0cedd8c15b432cee6dc87e`
- Temporary preview PDF SHA-256: `03e45373fd915ff0af2d1cf6ba44ca02841a112c6be0b26ba2e5126ffc12f6f5`
- Temporary final LaTeX log SHA-256: `011070ed6fefc3fb0ee6a65a8d7c30dbaaa3cdc101a780fce10f16f394f123d4`
- Isolated build directory: `/tmp/p32-stage4-prime-build.tKoyi1`

The official ARS patch applier succeeded with 18 operations, 18 unique targets, and 114/131 pre-existing blocks preserved byte-identically. The isolated `lualatex -> bibtex -> lualatex -> lualatex` sequence produced a PDF and ended with no undefined citations, undefined references, missing glyphs, or fatal errors. It nevertheless emitted eight overfull-box diagnostics, so the candidate was not promoted.

## Layout findings

The final log records eight overfull boxes (maximum `58.39977pt`) in material introduced or replaced by the authorized patch:

1. long notes-side paths and adjacent SHA-256 renderings in the replay, claim-passage, conditional-lemma, analytic-registry, and reader-manifest paragraphs;
2. one unsplit displayed logarithmic-summand identity;
3. the pinned GitHub tree URL and its long commit/path components.

The affected authorized carriers are the insertion after `B0128` and replacement blocks `B0047`, `B0060`, `B0090`, and `B0098` (with repeated reader-manifest material also present in authorized `B0125`). No additional scientific claim, number, citation judgment, roadmap item, target block, or operation type is required.

## Fail-closed disposition

The first applied draft, apply report, patch, and writer-side artifacts are retained under `notes/stage4_prime_layout_superseded_20260904/`. Current applied-draft and apply-report paths are withdrawn before re-emission. A writer may issue a full replacement patch only with semantic-neutral TeX line-break/layout changes within the already authorized carriers. A separate applier must then replay the unchanged authority checks and rebuild from scratch. Stage 4.5 and canonical promotion remain unauthorized and unstarted for Paper 32.
