# Compile report

Build epoch: SOURCE_DATE_EPOCH=1787788800; engine: LuaTeX 1.14.0;
paper size: A4.  Each revision was compiled in two passes; the settled
second-pass logs were inspected before build-sidecar cleanup (logs are not
payload files in the 28-file release).

| artifact | pages | bytes | SHA-256 |
|---|---:|---:|---|
| main_round0_original.pdf | 2 | 233251 | 8f8ba9c01b587da34f33757933b63987cb2059afff49118aba5b339776d3b355 |
| main_round1.pdf | 2 | 234828 | 48ffbad88af35a982ce38b54980fec048f533e62114eccb62d0a9b8e91705426 |
| main_round2.pdf | 2 | 242099 | 50298402105c9fbeb5bb642c0397caa6c18dd9cfeac922543cd5aaa070192461 |
| main.pdf | 2 | 242099 | 50298402105c9fbeb5bb642c0397caa6c18dd9cfeac922543cd5aaa070192461 |

The three revision hashes are pairwise distinct and main.pdf is byte
identical to round 2.  A fresh fixed-epoch round-2 build in a clean temporary
directory reproduced the final SHA byte for byte; a second settled pass had
zero warning, overfull, underfull, undefined-reference, and missing-character
lines.  The package contains no build sidecars by design.

pdffonts reports 17/17 fonts embedded and 17/17 subset.  pdftotext extracts
892 words (5611 bytes) from the final paper and includes the frozen scope
literal.  Visual inspection of both 120-dpi page renders found no clipping,
collision, truncation, or illegible content.  The release manifest performs
the final text, font, page, hash, and 27-payload closure checks.
