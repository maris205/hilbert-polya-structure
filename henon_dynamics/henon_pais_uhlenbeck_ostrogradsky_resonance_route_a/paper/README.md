# Paper build

`main.tex` contains three conditional revisions selected by
`\CRevisionRound=0,1,2`.  Round 0 proves the canonical and orbit theorem;
round 1 adds the complete Jordan/sign atlas; round 2 adds the self-adjoint
quantum difference-spectrum theorem and Route-A integrity boundary.

`main.pdf` must be byte-identical to `main_round2.pdf`.  The release gate
builds each revision twice in fresh temporary directories with
`SOURCE_DATE_EPOCH=1788480000`, requires byte identity, inspects settled logs,
fonts, text, and every rasterized page, and checks the compile-report hashes.
