# Compile report

Build epoch: SOURCE_DATE_EPOCH=1787788800; engine: LuaTeX 1.14.0; paper size:
A4.  Three substantive revisions were compiled in two settled passes and
round 2 was rebuilt twice in a clean temporary directory.  Hashes, page count,
font checks, extracted text, and visual inspection are summarized in the C218
release manifest; auxiliary build sidecars are excluded from the 27-payload
release.

| artifact | pages | SHA-256 |
|---|---:|---|
| main_round0_original.pdf | 3 | 55a5b488efb93c81a2c90dc49ceaace074bac083e014f283e33ef9b56755f82f |
| main_round1.pdf | 3 | 25d531c090b0c3450dbd9d02ff8643cdb5715eaca028832d970de1ad45ce4b71 |
| main_round2.pdf | 3 | 1d92dd1acfc9fd35d5f1622d32975dab9eac8a7de118624371b5d55eba623d97 |
| main.pdf | 3 | 1d92dd1acfc9fd35d5f1622d32975dab9eac8a7de118624371b5d55eba623d97 |

The two clean fixed-epoch round-2 rebuilds of the strengthened source both
returned the final hash.  The revision adds the exact Kelvin--Voigt generator
domain, an explicit normalized Weyl singular sequence, and the direct
non-eigenvalue argument at the spectral abscissa; the settled second-pass
logs contained no overfull, underfull, undefined-reference, or
missing-character records.  All fonts were embedded and subset.
