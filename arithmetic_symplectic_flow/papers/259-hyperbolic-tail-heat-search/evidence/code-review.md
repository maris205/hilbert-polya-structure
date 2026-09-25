# CS09 — independent pre-execution implementation review

Scope: `ASFS-DISCOVERY-20260919-CS09`; research label 2026-09-19.
Material Passport: ARS experiment-agent; bounded validation of frozen code;
`ANALYZED — STATIC REVIEW + EXECUTED NONNUMERICAL LOGGER TESTS`.
Decision: no blocking implementation defect found in the reviewed final source.
Scientific controls/results have **not** been executed by this reviewer.

## Frozen inputs and actual review

Read the complete 735-line [runner](../run_search.py), 157-line
[candidate card](../candidate-card.md), [execution card](../execution-card.md),
17-entry lock manifest, and complete 408-line [form review](form-review.md).
Also inspected the locked inherited readout/state/static/comparison and output
utilities; these were not substituted for the new potential or its minima.

| Artifact | SHA256 |
| --- | --- |
| final `run_search.py` | `7e4879818eeced3c067cc4cb796490c11177f9834814a495d68943fe5d658290` |
| `candidate-card.md` | `592abf96ccdb5d4243c2c7ab19f2c9ced8a87e3f875fec276abb841aa2c5c0a6` |
| `execution-card.md` | `130852ed3cb4e5fc64c4ffdb30dcb185299ad07b2a122b38803c7e24059ace55` |
| `input-locks.json` | `8b22faf399d3650c8ac27c868a716317db4980a356ffb25f14c6837755148f50` |
| `form-review.md` | `47fba476cc63a440208bf6b73a62b88fdc6a5b137ab3c77d121712eb740c552f` |
| inherited 258 readout helper | `4c8a52f7b5f57519d09ef241e0a3c7e7633f35848b957857d1fc10bee05db763` |
| inherited 258 output/logger utility | `94e8f9a0a6435ad86f8bbe159782cd0a5fe6763e985f33c4da64e59154c8c1ce` |

All 17 locked files matched their byte hashes using a read-only SHA256 check.
The final source hash was checked before AST parsing and after complete reading.
No whole runner/helper module was imported in this review; no target arrays or
development ordinates were parsed. `evidence/run-1` was absent during tests.

## Actual nonnumerical tests

Executed `PYTHONDONTWRITEBYTECODE=1 python -` with an AST-only harness. It
compiled only `utc`, `make_logger`, and `logger_regression_test` from the
SHA-bound utility, supplied standard-library globals, and guarded scientific
entry points. The source's four-case logger test passed; additionally executed
the new runner's four full keyword shapes for winner start/completion and
propagation start/completion in a separate `StringIO` stream.

All four records preserved independent event/name values and their extra
metadata; UTC parsed with zero offset. Reserved `event` and `utc` overrides
both raised `ValueError` without appending output. Scientific-entry calls: 0.
AST inspection found one `np.linalg.svd`, one `helper.static_readout`, one
`minimize` call site and 22 event call sites, with no reserved metadata misuse.
These are actual logger tests and static call-site checks, not a numerical dry run.

## Kernel, derivatives, and minimum ownership

- `normalized_tail` implements degree-factorial coefficients for r=0,…,32,
  factoring q^(degree−d) and Horner-evaluating powers of (κq)^2. The direct
  branch uses the correct cosh/sinh parity, differentiated subtraction terms,
  and κ^(d−degree). All 0–4 derivatives match the frozen analytic formulas.
- κ=0 takes the exact polynomial branch. The final `np.any(~small)` guard
  avoids evaluating irrelevant negative powers of tiny κ when every point uses
  the series. This is the final reviewed source, not the earlier unguarded SHA.
- B/E/X definitions retain z*q5 or z*S5 as appropriate, the .002 coefficient,
  four-parameter versus five-parameter bounds, and the common low-order jet.
  New a,z,κ-dependent minima are never borrowed from old Q arrays.
- The [-12,12] V''' root, V'' minimum/zero cases, V' monotone partitions,
  literal-zero endpoints, merge tolerance and value/leftmost tie rule match
  the contract. Residual and endpoint checks stop on failure; floating roots
  remain non-certified, as the separate analytic review explicitly states.
- Scalar cache keys include canonical potential identity and exact float.hex
  parameters. κ=0 shares only the identical polynomial minimum; X with z=0
  may share the mathematically identical E minimum. Propagation/score caches
  remain separated by form, even for these identical-potential cases.
- Same-member W is formed from the continuous minimum, with only the permitted
  recorded tiny-negative clipping. The frozen cooling source supplies all
  midpoints; DST-I half-potential/drift/half-potential steps left-multiply the
  full identity. β=.02 and rest mass are counted once, not twice.
- The sole full SVD supplies sigma and cached first-320 left/right states.
  Inherited readout uses m−log(sigma)/β and each grid's own E0; it preserves
  complete raw spectra/masks without floors or clipping. No Gram/static proxy
  is used for training. The N63 free control uses 63 states, not a false 320.

## Selection, budget, and frozen evidence

- Nine seeds per form, shared RNG20260926 wide points and physical default
  preservation match the card. Rotation is B/E/X; each valid-seed form has
  one normalized bounded Nelder–Mead with maxfev32 and inward .06 simplex.
  Ranking uses all visited valid pairs, not just optimizer return values.
- At most 27+96=123 pair calls, 246 training propagations, one free propagation
  and eight postchecks: 255 forward/full-SVD calls. Exact within-form cached
  calls still count but do not trigger new propagation; no budget transfer.
- Only current best two matrices/states per form remain cached. Nonwinner
  compact files omit C/states and disclose reconstruction limits. Winner save
  consumes its original cached states, leaves selection sigma unchanged, and
  performs no extra forward/SVD. State equations and full-spectrum Frobenius
  moments are distinct from the saved partial-state reconstruction scope.
- Identity freeze precedes all training heat/static saves; at most six heat
  and six static arrays plus their JSON files are then SHA-frozen. The first
  parsing of 101–320 ordinates occurs only after this complete array freeze.
  Earlier byte hashes and original prediction-only regression are not dev fits.
- Every valid family gets N1023 and N1279; fixed primary alone gets B128 and
  L10/N1599. All eight possible post roles have their own same-parameter static
  readout: at most 6+8=14 static decompositions, enforced before each call.
  All-role four-window fits/G, own E0/scale, heat/static comparisons, and the
  old Q0107 comparator are reported without development-based reselection.
- INVALID training pairs are saved/penalized and excluded from ranking. No-valid
  seed forms skip optimization/postchecks with explicit missing status. Ordinary
  postcheck INVALID remains saved and makes dependent comparisons unassessable;
  there is no replacement winner, new N, or retry. Missing roles are not success.

## Operations and remaining checks

Attempted, completed and saved counts are separated; root/eigh internal attempts
are not presented as completed readouts. Exclusive output creation and the
inherited per-write 1 GiB guard cover binary files, JSON, and all log streams.
30s resource events record RSS as advisory. Single-thread BLAS and the 600s+10s
hard limit depend on the exact external launch command; this review did not run it.
Input bytes are checked at start and successful completion, with own-script and
winner-identity hashes checked again. Exceptions log and stop, without retry;
if failure precedes end verification, a saved-only audit must recheck input hashes.

The polynomial/Decimal60 evaluation controls, free-heat control, default double
regression, INVALID runtime branches, timings and actual count totals remain
untested here. They must be checked from the authorized run's saved evidence.
Final all-valid output would contain 14 heat + 14 static + one old comparator,
29 pointwise objects/9280 data rows; this is an expected count, not a result.
ARS validation discipline separates actual logger tests from static inference;
no inference about p-values, causal effects, population performance, blind tests,
infinite convergence, full-tail precision or thermal advantage is made.
Numerical status: `CANNOT_VERIFY — NOT_RERUN`; all scientific controls remain
inside the sole authorized execution. Formal coordinates remain `UNASSIGNED`;
A0/A1/A2/T0–T3 not evaluated; B `NOT INVOKED`; 241/242 remain paused.
