# C148 paper improvement log

No external reviewer, external model, numerical review score, venue judgment,
acceptance prediction, or cross-model independence claim was used.  Two real
internal theorem/scope/presentation audits were followed by source edits and
fixed-epoch recompilation.  All three stages are retained.

## Round 0: baseline

- Artifact: `paper/main_round0_original.pdf`
- SHA-256: `a4504aa66b6c3138a9fa84846b735af62936b5f2238ad875564482b5132f583e`
- Pages: 2

The baseline fixed the gate, corrected the one-step rank, proved the tensor
power and gcd trace identities, gave the Newton recurrence and local primitive
product, and stated the closed and moved-hole controls.  The first internal
audit found three actionable defects: the exact degree `2^k` lacked an
algebraic-zero-multiplicity proof, the paper did not give a compact receipt for
all five polynomial sizes, and the long Route-A tuple caused a 62.71 pt
overfull box.

## Round 1: spectral-multiplicity and layout revision

- Artifact: `paper/main_round1.pdf`
- SHA-256: `f4ad4a779dd846849fd3fd9eb1a1fdc846088b37ab227119d0659a0270841de1`
- Pages: 2

Round 1 added the triangularization/spectral-mapping proof of zero algebraic
multiplicity `3^k-2^k`, the five-row dimension/rank/degree/support-size table,
and an explicit absolute-path majorant.  It also broke the Route-A verdict
across lines, eliminating layout warnings.  The second internal audit found a
remaining control-logic gap: the manuscript did not say whether changing
projector order was spectrally meaningful, and the moved-hole statement did
not display its exact coefficient.

## Round 2: control-separation and final visual revision

- Artifacts: `paper/main_round2.pdf`, `paper/main.pdf`
- SHA-256: `7d74eb952880972d2d73a87e32eb69bbcdd65f430c19aa1ab168bc1e3548dd89`
- Pages: 2

The final revision proves `P F3^*=F3 A F3^*`, so the projector-order control is
unitarily similar and leaves every secular polynomial unchanged.  It contrasts
this with `P0=diag(0,1,1)`, whose exact trace changes the linear coefficient.
The gcd proof now counts cut crossings by residue modulo `gcd(n,k)`.  Visual
inspection also caught and removed one literal `qquad` token introduced during
editing and compacted a nearly blank third page without deleting mathematical
content.

Two fresh isolated fixed-epoch builds equal the release PDF byte for byte.
Every font is embedded; both final logs contain no warnings, overfull or
underfull boxes, undefined references/citations, or duplicate labels.  Both
rendered pages were inspected at 144 dpi and have no clipping, overlap,
truncation, broken formula, literal source token, or unintended blank page.
