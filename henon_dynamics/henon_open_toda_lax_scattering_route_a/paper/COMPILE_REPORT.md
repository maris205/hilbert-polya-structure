# Compilation report

The three revision PDFs were built with LuaLaTeX in two separate fresh
temporary directory trees.  Every revision received two consecutive builds at
SOURCE_DATE_EPOCH=1787875200; the settled second-pass bytes matched across the
fresh trees and the copied release files are content-distinct across revisions.  The final
paper/main.pdf is byte-identical to paper/main_round2.pdf.

The final PDF has 3 pages.  pdffonts reports embedded subset Latin Modern
fonts for every face; text extraction contains the Toda model, Lax/scattering
theorem, exact N=2 formula, repeated-root polynomial, the strict
ROUTE_A_REJECTED tuple, and NO_BAD_EULER_OR_ROOT_NUMBER.  Settled logs contain
no overfull/underfull boxes, undefined references, missing characters, or
errors.  Build sidecars were removed before manifest closure.

Release hashes (SHA-256) are `main_round0_original.pdf`
`e762404f290b85fe752c67c6fe34f1ff06ffffbac58ed00ae8c5610268c2ec74`,
`main_round1.pdf`
`cf8b62437f8d0781bd107482605a40b88ff2733265b7589f180541ab18044d12`, and
`main_round2.pdf`/`main.pdf`
`9fe2fd33f7f7a8c62bb27e05590180a3448c647c43688d6a20e55d7726fa0ce1`.
Independent fresh directories produced identical bytes for each revision.
