# P29 Stage 4′ Round-2 layout preflight incident

Date: **2026-09-04 UTC**

Status: **REVIEWED — FIRST DISTINCT-CONTEXT APPLY IS NOT THE FINAL CHAIN**

The first distinct-context application succeeded mechanically, with 8/8
authorized operations, an authorization witness of `pass`, no structural
flags, and 105/113 source blocks preserved byte-identically.  Its isolated
LuaLaTeX--BibTeX--LuaLaTeX--LuaLaTeX preflight also completed with zero command
failures and produced a 15-page A4 PDF.  The layout gate nevertheless found
seven overfull boxes, so this applied draft is not eligible for the final
Stage-4′ evidence chain.

## Frozen first-attempt bindings

- patch SHA-256: `843a25c2ea3f18ce7f53151fcbbb0cc5ecd1c52394758b8a1fc3cc1e72fa7dc8`;
- applied draft SHA-256: `7cce1c333bcdca7ef4eb2eca5f7d9f4fbbc1b7b4f97911aa5d4f995c7d3cd1ed`;
- apply-report SHA-256: `9a399cecb749a728d7bf61a7e5dc4bbdbdc51bd4053971b9d1778ccffd71a17b`;
- temporary build directory: `/tmp/p29-stage4-prime-preflight.n4tRvn`;
- preflight PDF pages: `15`;
- overfull boxes: `7`; maximum reported excess: `94.31284pt`.

## Exact layout findings

- B0112: four unbreakable typed-state/interface tokens, including the mechanism,
  performance, and replay stop names;
- B0113: one unbreakable control-stop token;
- B0107: one unbreakable schema identifier;
- B0084: one unbreakable fixture SHA-256 token.

No scientific, evidentiary, review-disposition, citation, canonical, initial-system,
or Route defect was observed.  The permitted remediation is limited to
semantic-neutral discretionary line breaks inside the same already authorized
`replace_block` targets.  A writer context must re-emit the complete patch; the
orchestrator must then reapply it from the unchanged Stage-4 Round-1 base and
repeat the isolated build.  This incident record and the first apply artifacts
must remain preserved and excluded from the final evidence chain.

## Second layout attempt

- Recorded at: `2026-09-03T18:47:37Z`
- Patch SHA-256: `26df9d32270950dcfe0ac323430ab714e5666507aee4fe084486f315584f0402`
- Applied draft SHA-256: `c4e8e617a4d87a30c25b245edca1439a959cf952be4e24ef2cae218b04125ffa`
- Apply report SHA-256: `8033de7722d4ac308001f134fc275f9453550893c0aee34c91cdaba0cc7d2f59`
- Temporary preview PDF SHA-256: `9e475424fce8c0556023a49f710c876e0634370ec7f98d8012f35d09f2f2247c`
- Temporary final LaTeX log SHA-256: `f4ddedb4b895bc03b9cbb2d8eb099c367fc1fd3155da380b25558ac9ecd345bb`
- Isolated build directory: `/tmp/p29-stage4-prime-build.ivPbBj`
- Result: `FAIL_CLOSED_LAYOUT_ONLY`

The second patch remained semantically identical after removal of discretionary
breaks, and its official application again passed.  The fresh four-command build
reduced the layout failures from seven to five but did not eliminate them: three
long stop-state sequences in the `B0112` reader map, one control stop state in
`B0113`, and the long crosswalk schema/hash presentation in `B0107` remained
overfull (maximum `69.53595pt`).  Citations and references were fully resolved,
the PDF was 15 pages, and no fatal or missing-glyph error occurred.

This second candidate is retained under
`notes/stage4_prime_layout_superseded_attempt2_20260904/` and excluded from the
final chain.  A further writer re-emission may add scoped paragraph-level TeX
tolerance/layout controls in `B0112`, `B0113`, and `B0107`, without changing a
scientific token, citation, value, target, or operation type.  A new independent
application and clean build remain mandatory.

## Third layout attempt

- Patch SHA-256: `d02911b1f000716d703c68934dca899120de00c2f8d311778d55d9b7793f7135`;
- applied draft SHA-256: `3eb2aae993d6e513688705cb0d6eebe63d0e2012ef01415573e1db420b7970d6`;
- apply-report SHA-256: `8283d3770118134528217e03c2c25b5c8c1b8ed3e1a4f7d566b50144fd77c155`;
- temporary preview PDF SHA-256: `b7f37eda750195f8d1fdcec72f96a51149f2341ac2a112cbed849a24c98a5843`;
- temporary final LaTeX log SHA-256: `ef117499b02f846a9c591780c6859041b3a26965053cb0c268122ba3e711072d`;
- isolated build directory: `/tmp/p29-stage4-prime-attempt3.2EE5p5`;
- result: `FAIL_CLOSED_LAYOUT_ONLY`.

The third complete patch added only scoped paragraph-level tolerance controls
around B0107, B0112, and B0113; removing those controls restores the second
attempt byte-for-byte. Its official application again passed with 8 operations
and 105/113 preserved blocks. The four-command build produced a 15-page A4 PDF
with zero undefined citations, undefined references, missing glyphs, or fatal
errors, but one `28.86852pt` overfull box remained in B0107's presentation of
the literal schema name `p29-source-inventory-to-literature-matrix-crosswalk/1.0`.

This candidate is preserved under
`notes/stage4_prime_layout_superseded_attempt3_20260904/` and is excluded from
the final evidence chain. The only admissible next layout correction is to
render that same literal schema name with a URL/path macro that permits line
breaking, inside the already authorized B0107 `replace_block`. Scientific,
evidentiary, citation, numeric, canonical, initial-system, and Route content
remain unchanged. A distinct writer re-emission, independent application, and
clean isolated build remain mandatory.

## Fourth layout attempt

- Patch SHA-256: `7827a265b0148151c6c317caa8c00782d3bdaec5152edee6e8ad6f2ac3868f77`;
- applied draft SHA-256: `f6d7548c3ee80b130169f8c6f5d6a8991b5c87eca0ab59a82a19464559a954a5`;
- apply-report SHA-256: `c78169154fa0d7af9e4409fbb0c71670daaf6f927f954383c0b71c1f4cf3abf6`;
- temporary preview PDF SHA-256: `d9887bd42fa2754931b78762fa364166c7ea14e8b83b84c8e0638fae59d50d3f`;
- temporary final LaTeX log SHA-256: `33b2b5a23452f81eef32d31099d04a90a6b9aad8d88fbe0984dc3871cebb5aac`;
- isolated build directory: `/tmp/p29-stage4-prime-attempt4.yA9Dk2`;
- result: `FAIL_CLOSED_LAYOUT_ONLY`.

The fourth patch changed only the B0107 rendering of the exact schema literal
to a breakable `\path{...}` form. That occurrence became clean, but the same
literal also occurs in the separately authorized B0080 reproducibility block.
The build therefore retained one `28.86852pt` overfull box at the B0080
occurrence. All other diagnostics remained zero and the PDF remained 15 pages.
This candidate is preserved under
`notes/stage4_prime_layout_superseded_attempt4_20260904/` and excluded from the
final evidence chain. A final writer-only layout re-emission may apply the same
literal-preserving path rendering plus scoped paragraph tolerance to B0080.
