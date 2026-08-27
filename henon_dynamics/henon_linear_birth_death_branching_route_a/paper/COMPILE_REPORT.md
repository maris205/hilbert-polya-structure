# Compile report

Build epoch: `SOURCE_DATE_EPOCH=1787788800`; engine: LuaTeX 1.14.0;
paper size: A4.

| artifact | pages | bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 3 | 183,207 | `a7f06d2a137d4b6081675f674e6121192acfc6b1748ad8d93f8a5f5e8e96008c` |
| `main_round1.pdf` | 4 | 197,696 | `150e6f0ccded222b2430a534bd7ad56dc2bf7ba6d52998d88a260a798c6ccbb4` |
| `main_round2.pdf` | 4 | 203,066 | `b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325` |
| `main.pdf` | 4 | 203,066 | `b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325` |

The three revision hashes and extracted-text hashes are pairwise distinct;
round 2 equals the final release. Two additional fresh fixed-epoch round-2
builds reproduced the released PDF byte for byte.

All revision and fresh-build logs contain zero warning, overfull, underfull,
undefined-reference and missing-character lines. `pdffonts` reports 24/24
fonts embedded and 24/24 subset. `pdftotext` extracts 2,136 words and 12,715
bytes from the final paper. It also extracts the exact frozen scope literal
`NO_BAD_EULER_OR_ROOT_NUMBER`. Visual inspection of all four 120-dpi page renders
found no clipping, collision, truncation or illegible content. The fourth page
is intentionally short because it contains declarations and the source lock.
