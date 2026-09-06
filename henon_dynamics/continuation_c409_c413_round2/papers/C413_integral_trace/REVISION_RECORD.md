# C413 actual manuscript revisions

2026-09-06. Independent reviewer: `scout_nonaffine_charp`.
The complete [manuscript review](../../positive_characteristic/REVIEW_C413_MANUSCRIPT.md)
passes the universal classification and all its proofs. The following
actual repairs are recorded separately from the original proof review.

## Author clarity pass before independent review

The twelve-triple two-column table is traversed by numeric index modulo
12, not by physical rows. The group-scope paragraph now states the correct
implication: whole-group finiteness implies single-map periodicity, but
not conversely. An unnecessary and imprecise compact-level phrase was
removed. The reviewer read and accepted those current-source corrections.

## R1: finite-cube qualifier — implemented

Section 5.2 now says that the 445 graph states, and the 49 states for the
small cube, are on cycles **wholly contained in their respective cubes**.
The other 76 small-cube initial states leave that cube; they are not thereby
declared globally nonperiodic. The explicit reviewer witness
`(-1,-2,-1) in B_3`, mapping to `(-2,-1,3)`, is included.

The exact theorem, all equations, and the Section 3 whole-cycle certificate
are unchanged. This is a diagnostic-prose precision correction. No old
finite census or symbolic checker was rerun; the reviewer requested none.
The same non-author reviewer has now read the affected source and appended
an explicit R1-resolved follow-up to the manuscript review. The actual
revised Section 5 hash is
`141b591d949c70902d9cd1f98be9144e1c5118e27dbc276d1364900d6a62f328`.
This closes the requested prose repair, not the remaining PDF release gate.

## R2: current source versus initial PDF — final build required

The original PDF hash in BUILD_REPORT is historical and predates the prose
repairs. It is not the accepted final artifact. The required two fresh final
builds and all-page visual QA will run only on the reviewed, corrected source.
Their actual receipt will close this item; it is not predeclared passed here.

### R2 actual closure

The coordinator has now completed both fresh builds from the corrected
source, compared their PDF bytes, and visually viewed all ten final pages.
The actual [final build report](../../FINAL_BUILD_REPORT.md) records the
commands and final PDF SHA-256
`60d9b0289b163216db7a217aeb06e8967053b00bc4f75ff7231eb3fa79ade552`.
This closes R2. The initial-PDF hash remains historical; no mathematical
source or old experiment was changed by this receipt update.
