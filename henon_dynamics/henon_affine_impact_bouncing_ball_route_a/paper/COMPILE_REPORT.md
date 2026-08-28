# Compile report

Build epoch: SOURCE_DATE_EPOCH=1787788800; engine: LuaTeX 1.14.0;
paper size: A4.  Each revision was compiled in two passes; the settled
second-pass logs were inspected before build-sidecar cleanup (logs are not
payload files in the 28-file release).

| artifact | pages | bytes | SHA-256 |
|---|---:|---:|---|
| main_round0_original.pdf | 2 | 228733 | 4e5133e42d2b849d2d422551cbd3c0a9d87d1171ea6ea66f56e78e964cec5bbf |
| main_round1.pdf | 2 | 232847 | ea82e67d7ecdc35be4ec3b2e4de339849caac0141a0c05d5d57adb7ee805d776 |
| main_round2.pdf | 2 | 239515 | f6cc08eb6a122eebf0d27a7c2d6b213de3b59cbe5b2c11179958f382026c582b |
| main.pdf | 2 | 239515 | f6cc08eb6a122eebf0d27a7c2d6b213de3b59cbe5b2c11179958f382026c582b |

The three revision hashes are pairwise distinct and main.pdf is byte
identical to round 2.  A fresh fixed-epoch round-2 build in a clean temporary
directory reproduced the final SHA byte for byte; its settled pass had zero
warning, overfull, underfull, undefined-reference, and missing-character
lines.  The package contains no build sidecars by design.

pdffonts reports 16/16 fonts embedded and 16/16 subset.  pdftotext extracts
926 words (5137 bytes) from the final paper and includes the frozen scope
literal, the regular-section label S_+, and the r=0 boundary.  Visual
inspection of both 120-dpi page renders found no clipping, collision,
truncation, or illegible content.  The release manifest performs the final
text, font, page, hash, and 27-payload closure checks.
