# Paper20 R1 source-repair receipt

This out-of-band receipt records the final source repair after the first
expanded-source review.  It is excluded from the manuscript source preimage
and does not authorize a build or publication.

| stage | `paper/main.tex` bytes/LF | SHA-256 |
|---|---:|---|
| compact predecessor | 37,423 / 981 | `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014` |
| expanded source reviewed before ledger wording repair | 58,951 / 1,552 | `a4a12679acaad9dd258178a417f70c0fa3626266d5cd10b0f527c8e197f41779` |
| final frozen R1 source | 58,944 / 1,552 | `67b1bf3d18fdc01be1084d969dd273bbaa1e7fe5a1677eecaa758b64ea9efbb1` |

The only repair between the two expanded identities corrected the prose
classification of the five phase-ledger margins: the first and fourth are
face comparisons, while the other three compare selected terms with carried
coordinates.  No theorem, formula, assumption, citation, anti-claim, or
permission was changed.  The final source is frozen pending fresh independent
R1/R2 review.

The final metadata bindings are:

* `paper/BUILD_METADATA_R1.json`: 5,002 bytes, SHA
  `07df9ae892159220ded19f792a568cb3a24f1fe5d7139febd915fea78d97cdce`;
* `paper/SOURCE_REVISION_RECEIPT_R1.json`: 5,508 bytes, SHA
  `313460b46affade4a61522e86799db9789222e637e497aa2ad8fafb991fcc4a6`.
