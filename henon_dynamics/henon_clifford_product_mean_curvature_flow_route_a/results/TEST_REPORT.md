# C319 test report

- Producer: PASS; payload `a230ab23856151f6cd6e486768924988ebac736d3cca63e6b73d7244b3b031e0`.
- Independent checker: PASS, 22,738 checks.
- SymPy cross-check: PASS, 1,204 exact identities.
- Isolated producer replay: PASS, byte for byte.
- Hostile evidence/YAML suite: PASS, 39/39 rejected.
- Optimized Python: all five executable lanes refuse `python -O`.
- Evaluation lock: raw SHA-256
  `59d4dd4f971c7a91d48c31630e903009bb641dc90fd082835b46bd2d15225339`;
  semantic SHA-256
  `b88d5bc5d78f9b917bfbabcc91d29748172f28b05922d2477570cabef542f49f`.
- PDF: three deterministic, substantively distinct LuaLaTeX revisions;
  clean logs, embedded subset fonts, and successful rasterization are
  release-gated.
