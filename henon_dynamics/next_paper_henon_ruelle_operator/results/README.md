# Results ledger

Status: **no project-specific computational result yet**.

This directory will contain only immutable production artifacts produced after
R001. Pilot artifacts belong in a separately marked development location and
cannot be cited as confirmatory results.

Expected artifacts:

| Artifact | Minimum contents |
|---|---|
| `dependency_manifest.json` | source paths, SHA-256 hashes, environment, source-control state |
| `geometry_interface_check.json` | inherited covering/cone/coding checks |
| `dimension_theorem_preflight.json` | theorem/erratum version, hypothesis ledger, local-or-compact ambient applicability, early kill verdict |
| `variation_certificate.json` | \(C_0\), \(\theta\), cylinder widths, rounding mode, checker result |
| `roof_gauge_bridge_certificate.json` | adapted tangent scales, exact invariant-frame proof, bounded/Hölder \(b_u\), physical \(H_6\)-identity, symbolic \(\sigma\)-pullback, telescoping periodic-sum proof/checks |
| `cohomology_certificate.json` | state-wise reference past, transfer-function tail, positivity status or original-roof/operator-only fallback, periodic-sum checks |
| `known_truth_controls.json` | constant and synthetic finite-memory exact controls |
| `operator_convergence.json` | memory depths, sparse sizes, pressure and leading-spectrum enclosures |
| `pressure_root_certificate.json` | target uniqueness proof, envelope-positivity flag, root-sandwich or pressure-sign brackets, memory tail, final interval |
| `basic_set_certificate.json` | R015 open isolating neighborhood, local maximality, mixing/hyperbolicity dependencies |
| `angle_coboundary_certificate.json` | physical Euclidean Jacobians/angle, symbolic pullbacks, angle lower bound, area-preserving identity |
| `hausdorff_dimension_certificate.json` | R015/R020 dependency hashes including `roof_gauge_bridge_certificate.json`, stable-pressure reindexing/cohomology, unstable root transported to the stable root, independent-stable status plus any separate variation/tail artifact hashes, total dimension interval |
| `cycle_operator_crosscheck.json` | independent word/cycle/trace and orientation checks |
| `structural_controls.json` | flat/random/shuffled/precision outcomes |
| `contour_certificate.json` | analytic-domain theorem/version, closed-interior coverage, continuation domain, optional pole ledger, fixed contour, tail, minimum modulus, Rouché margin |
| `independent_check.json` | second implementation verdict for every required artifact |
| `ANALYSIS.md` | theorem/result/non-claim summary and Route-A interpretation |

Rules:

- Every number in a theorem or abstract must trace to a machine-readable field.
- Numerical roots without a uniform limiting certificate are labeled finite
  approximants.
- No box-counting plot is a substitute for the Hausdorff-dimension theorem and
  its local-basic-set certificate.
- `NOT_CERTIFIED` is a result state, not a failure to report.
- The 2,170 inherited cycles are local survivor cycles, never a global Hénon
  catalogue.
