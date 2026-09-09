# C424–C428: actual Route-A reference routing

2026-09-09 UTC. This is a reading/provenance record, not an evaluation,
admission decision or claim that the five manuscripts already exist.

## Authority and actual reading

The coordinator read all 686 lines of
`flow_systems/skills/route-a-evaluator.md`, version 0.2.0, unchanged.
SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
Its relative prior-work paths were resolved in `flow_systems/`, not in
the shell's initial repository. The prescribed routing was completed in
this order: full `flow_systems/docs/prior_work/README.md` (434 lines),
the first three physical PDF pages of papers 1 through 6 in numerical
order, full flow obstruction register (48 lines), then full flow
candidate registry (34 lines). A truncated combined registry display
was followed by a complete standalone read.

The additional Hénon ownership reading comprised its full prior-work
README (553 lines), obstruction lines 1–92 and the C17/C18 entries
708–726, and candidate-registry lines 1–118, including the C409–C423
source/target and unit-clock boundaries. These are actual selected
reads, not an assertion that every historic paper was reviewed again.

## Six local PDF inputs

For each PDF, the ARS local `pdf_read_preflight.py` was actually invoked
once, with a separate output under
[`evaluation_inputs/prior_pdf_preflight/`](evaluation_inputs/prior_pdf_preflight/).
All six sidecars returned **UNAVAILABLE**, because `pypdf` is not
installed; the command's exit 0 is not a PDF-anchor PASS. No dependency
was installed. The coordinator instead read the complete displayed
output of `pdftotext -f 1 -l 3 -layout` for each actual local PDF.
This fulfills the bounded content read; it does not certify all PDF
anchors, every page, every proof, or the prior papers' conclusions.

Paths below are relative to `flow_systems/docs/prior_work/papers/`.

| Paper | Filename | SHA-256 |
| --- | --- | --- |
| 1 | `1-The emergence of prime distribution from low-dimensional deterministic chaos.pdf` | `78a65db26110ef8173c3d7dc50caf2b598e59b854e7b5afa3983891008cb953e` |
| 2 | `2-Transient Chaos and Topological Bounds in Prime Dynamics.pdf` | `05044a54a6bde0bbd71dc7c7c6deb305638803afe36f8fe2d4167b88c5ad898d` |
| 3 | `3-A Sequential Birkhoff Theorem.pdf` | `6ad40b40e81a22266c1ca5baa34b5692e4e0b4dbc7f4764b57db190193731f9b` |
| 4 | `4-riemann_logistic_v4_fixed.pdf` | `030c072bcec069ef1c3d87b84025ed830e40591970461e5195b2991adaedb0e3` |
| 5 | `5-An Area-Preserving Henon-Map Model.pdf` | `23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9` |
| 6 | `6-zeta-two-thirds.pdf` | `6792988e6cd0e17690621ce898abd5d534f98407741bc7cb14bbe7d07c77d72f` |

## What is and is not imported

Papers 1 and 2 provide the early heuristic and its subsequent limitations.
Paper 3's sequential theorem retains its hypotheses U1–U4 and the
almost-everywhere parameter qualification; it is not an unconditional
statement for every base greater than one. Paper 4's displayed
construction uses low-zero anchoring, and paper 5 supplies a numerical
geometric Hénon model, not a verified target determinant.
Paper 6's two-thirds claim is part of the supplied research background,
not a theorem independently certified in this batch. None of the new
source-system proofs relies on these six PDFs as a mathematical lemma.

The later formal evaluation must still distinguish source arithmetic
from target coefficients, retain missing controls as INCOMPLETE and
missing target metrics as NOT_TESTABLE, and preserve
`NO_BAD_EULER_OR_ROOT_NUMBER`. This record awards no A0–A4 grade and
cannot substitute for manuscript/evaluation review or final PDF inspection.
