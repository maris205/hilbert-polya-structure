# Stage 2.5 input freeze — P67–P71

Freeze recorded: `2026-08-26T02:12:30Z`  
Evidence-search cutoff: `2026-08-26`  
Scope: internal integrity and priority audit only  
External release: `HOLD`

This receipt freezes the Stage-2 manuscripts before any Stage-2.5 corrective
edit.  A source-bundle digest is the SHA-256 of the sorted `sha256sum` stream
for `main.tex`, `references.bib`, every `sections/*.tex` file, and every
`code/*.py` file in the named paper directory.  Audit artifacts under
`stage2_5/` are intentionally outside that digest.

| Paper | PDF pages | frozen PDF SHA-256 | frozen source-bundle SHA-256 | claim-view SHA-256 |
|---|---:|---|---|---|
| P67 | 11 | `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e` | `46486b814812f77c78bf18544b587ea8d46c1567982a446085e8f1ede8a483ba` | `d60e2451b6b0c243bfd3ba3047e15d32ebb819d1af1e4c93c6885ef28960280f` |
| P68 | 7 | `b96ac6118ad81839eb796ad5640357ce710ff9e1372411bfa7931883dd3ac7c6` | `3b15c12b09071c2aecea7a8cd892dc98763f667bb9db7cac55008ecd014404b8` | `bb07f6f44433f69e76697dba6aa1b096e695905d9a1485a199e38396b3478806` |
| P69 | 10 | `09216444bcc5abd911b88d3ac28416ca5a547efe236b0a22b5fc39781a676b08` | `745c942b317b13e17942dda8a9aac1f0a3949f49b7ac4648be04277ede09c6fc` | `cf7f3e04ac14152a0144a9ffed61ee9f9e926e4e8c1a867093711034d67f675c` |
| P70 | 7 | `e20e1151597684736d72deeac8875d4be0e5e95d95ef2c187468d07f734f3ac5` | `5afb6863dcfad0def77cab2c81c57d47c3e029f7281213b5f37c6127f1d9fa72` | `be3a6824d0aa62148a0672978ab2dbd11ea5c6e047dd32ec7a5b34258953e7bb` |
| P71 | 9 | `ff85975c69b7848ff8675edde2e753ed9deb6cd377f37aeeb60669d403026bcf` | `2e15f6963fb4768fbdb4b393c1de520f40c695648a0eedf7ffd71cab4db8707c` | `59342c6d2cebb47402b7d52acc6aefd99753cd9db24090bf2768c126dc314517` |

The claim view is a derived, citation-preserving Markdown representation used
only for exact-byte claim registration.  It is not a replacement manuscript.
Any correction round must preserve this receipt, create a post-correction
receipt, rebuild the affected PDF, and rerun the affected audits.

