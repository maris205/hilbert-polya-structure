# C304 paper builds

`main.tex` uses `\CRevisionRound` to produce three archived round variants:

- `main_round0_original.pdf`: core Fourier theorem;
- `main_round1.pdf`: energy, full fastest-shell and boundary proofs;
- `main_round2.pdf`: evidence, hostile audit, Route-A and scope closure.

`main.pdf` is the byte-identical final alias of `main_round2.pdf`; it is not
a fourth independently compiled round variant.

The release script compiles each round variant twice in fresh directories with
`SOURCE_DATE_EPOCH=1788393600`, rejects material warnings, verifies
embedded/subset fonts and text sentinels, and rasterizes every final page.
