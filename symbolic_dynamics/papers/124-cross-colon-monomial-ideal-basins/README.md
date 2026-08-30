# P124 — Cross-colon monomial-ideal basins

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

Let `R=k[x,y]/(x^a,y^b)` and let the synchronous map

`T(I)=x(I:y)+y(I:x)`

act on the monomial ideals of `R`.  The central result is a complete basin
classification: the first occupied total-degree diagonal and the parities
present on its trace determine the attracting fixed power or checker
two-cycle.  A four-state contact-parity transfer on staircase boundary paths
then gives every basin size uniformly in `a,b`; the terminal fixed basin has
the ballot closed form

`binom(a+b,a)-binom(a+b,min(a,b)-1)`.

The fixed/recurrent census and the sharp square/non-square transient depth
law are supporting results.  Disjunctive OR-path dynamics, lattice-path and
reflection arguments, monomial staircases, and colon arithmetic receive zero
contribution credit.  The bounded owner search is not a novelty or priority
certificate.  Public posting, submission, and external release remain
**HOLD**.

Run the exact controls from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon_basins.py
```

Together the independent programs make **1,735,656** exact assertions.  See
`CONTROL_RESULTS.md` and `BUILD.md` for the frozen transcripts and PDF build.

Review A found no critical or major issue and requested two support-only
repairs.  Round 1 corrected the proof anchors and added the explicit P107/P104
collision firewall.  Independent nonauthor Review B then returned zero
critical, zero major, and zero minor findings.  The consolidated decision is
`GO_INTERNAL`; public posting, submission, and external novelty or priority
language remain `EXTERNAL HOLD`.

Round 2 is a support-only mechanical closure.  It does not alter `main.tex`,
`references.bib`, either verifier, either canonical transcript, or any
pre-existing PDF.  `main_round2.pdf` is a byte-for-byte copy of `main.pdf`;
round 0, round 1, current, and round 2 all have SHA-256
`3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81`.
See `HOSTILE_REVIEW.md`, `FINAL_QA.md`, and `SHA256SUMS`.  Verify the frozen
package with:

```bash
sha256sum -c SHA256SUMS
```
