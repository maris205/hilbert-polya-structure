# HCS-C383: Friedrichs Aharonov–Bohm full scattering

This package closes one noncompact magnetic subtype from its singular operator domain through the complete continuous spectrum, wave operators, full angular scattering distribution, local heat kernel, gauge covariance, and physical time-reversal classification. It also proves two obstructions: the heat semigroup is noncompact, and at noninteger flux the scattering correction is noncompact with cutoff-dependent finite determinant products.

The main deliverables are [the analytic proof](proof/ANALYTIC_PROOF.md), [final paper](paper/main.pdf), [exact receipt](results/c383_ab_evidence.json), and [Route-A evaluation](evaluations/route_a/HCS-C383/2026-09-05.yaml). The three manuscript rounds close domain/spectrum, full scattering, then heat/symmetry/obstructions. They are substantive versions of this one paper, not three paper counts.

Classical AB formulas are not claimed as new discoveries. The package increment is their integrated and independently checked domain, sign, distribution, cutoff, and physical-symmetry audit. The strict tuple is `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall `ROUTE_A_REJECTED`. `NO_BAD_EULER_OR_ROOT_NUMBER`; no Hilbert–Pólya operator or Route B.

Run `python3 -B code/c383_release_manifest.py` for a non-writing final release audit. Building PDFs or writing the manifest requires the explicit script switches documented in [reproducibility](REPRODUCIBILITY.md).
