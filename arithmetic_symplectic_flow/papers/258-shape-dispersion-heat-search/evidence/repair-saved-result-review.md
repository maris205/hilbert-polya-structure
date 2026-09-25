# CS08 fixed-winner repair — independent saved-evidence review

Scope `ASFS-DISCOVERY-20260919-CS08`; execution `CS08-REPAIR-FIXED-01`.
Research label 2026-09-19; saved-only review 2026-09-18 UTC.
Status: `ANALYZED — SAVED EVIDENCE CROSS-CHECKED`; no blocking inconsistency found.
This review did not reproduce the search or execute any new scientific run.

## Bound evidence and actual completion

| Artifact | SHA256 |
| --- | --- |
| [repair runner](../resume_fixed.py) | `94e8f9a0a6435ad86f8bbe159782cd0a5fe6763e985f33c4da64e59154c8c1ce` |
| [repair input locks](../repair-input-locks.json) | `fe8c4cbb2a7b7fac5be90a2653d58191431b79e5c3f466f04d8a6c5c71dec397` |
| [result](run-2-fixed/result.json) | `e28940479a89ca8bdf133035430403a4de3bdaef0c37db5654051d3f7a6ec2e1` |
| [manifest](run-2-fixed/manifest.json) | `0ccdaed7a57d57c116a973c04725e26339a3d53a283c678119851cd10e1c0495` |
| [training-array freeze](run-2-fixed/training-arrays-frozen.json) | `af75e608e467daf74a7c2ef2b495e35d3d938f722f43a5faf7b893882622c3fa` |
| [file inventory](run-2-fixed/file-inventory.json) | `83f837d62fee810a64625509c7be5624a2905592ca162b11e3b74c92589ec171` |
| [launch receipt](repair-launch-receipt.json) | `c3c7072a3414200686c7f4958376458b943eb4da252e2df699192c47268a0b63` |
| [pointwise CSV](run-2-fixed/points.csv) | `c6dd96fb0b95b8538b5e751c2760107e5d9ab9644456080ff0fe9a51454521f3` |

Launcher reports actual exit **0**, PID **64098**, without timeout. Started event
23:42:25.303309Z, completed event 23:43:57.469873Z: event interval 92.166564s.
Internal elapsed before final serialization was 93.142345s, starting earlier
than the event stream; neither number is mislabelled exact total wall time.
Recorded peak RSS 297068 KiB (290.105469 MiB); all three BLAS thread settings 1.
New run: **101 files, 478484239 bytes**, including its self-excluding inventory.

Exactly **22/22/22 propagation/full-SVD/static-readout attempts and completions**
are independently corroborated by event counts and the 22 heat/22 static
objects. This is 10 newly recomputed training matrices plus 12 fixed postchecks;
optimization and target-generation counts are zero. Combined with the original
323 completed forwards, the two executions total 345. Old failed execution
remains failed; recovery is not retroactive completion or a fresh search.

## Saved-only method and integrity checks

Used ephemeral `PYTHONDONTWRITEBYTECODE=1 python -` stdin audits; state analysis
additionally set `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1`.
Loaded JSON/CSV and NPZ with `allow_pickle=False`; did not import either runner.
No forward, SVD/eigh, root solve, optimizer, or target-generation call occurred.
Decomposition entry points were guarded during the state audit. Matrix products,
sums, norms, logarithmic readout and DST-I transforms of **saved states** only
were used; these do not rerun the chronological evolution or spectral solve.

- 1044 hash/inventory/event/identity checks, 3262 array/diagnostic checks and
  101 final target/role/receipt checks: no failures. Separately delegated
  independent metric/CSV arithmetic: 232792 scalar/metadata/role checks,
  no failures. Counts describe checked fields, not a statistical confidence score.
- All 34 repair locks and 16 original locks matched; the original 815-file
  membership, sizes and SHA256 matched. Every new inventoried file and all
  40 frozen training heat/static NPZ/JSON hashes matched. Both start/end
  verification records agree. All earlier source/review records were preserved.
- B0068/O0089/Q0107/U0135/D0158 identities and every frozen role record remain
  exactly unchanged. Original winner JSON and its new byte copy both have SHA
  `5e28a599e29e1032b27f35ae91d81c362378d0c268cbb37c8a4d3ba58028583f`.
  Q0107 remains primary; all 22 actual theta/N/L/B/beta and q/p arrays match
  their prescribed roles. New and original minimum IDs retain separate owners.
- Ten reconstruction completion events and ten static completion events precede
  `training_arrays_frozen` at 23:42:38.109210Z. The first development-read event
  is later, 23:42:38.109676Z; its freeze hash matches. All 320 target values equal
  the original first-100 array plus the five locked historical reference files.
- Checked **45 objects × 4 fit windows**, **44 comparisons × 4 windows**, and
  **14400 point rows**. Independent formulas used MAPE=100 mean(|pred−truth|/truth),
  worst=100 max(|pred−truth|/truth), G=100 max(|left−right|/truth), and raw-energy
  G with the left object's energy denominator. All G/raw-G and CSV arithmetic
  differences are zero. Independent `math.fsum` means differ by at most
  2.84217e−14 percentage points in MAPE, 2.32831e−10 in MSE and 3.55271e−15 in
  normalized spacing error; these are floating summation differences.

## Reconstruction, complete spectra and states

All ten physical contexts and canonical original selection arrays compare
exactly to their run-1 NPZ owners. Reconstructed fields remain separate.
Maximum reconstruction differences over ten roles: sigma **3.77475828e−15**
(contract tolerance 1e−12), full E **2.27373675e−13**, first-320 E
**1.91402449e−13**, prediction **1.41653800e−10**, scale **1.93267624e−12**.
Original and reconstructed masks agree; all ten readouts are valid. None of
these recomputed spectra replaced original sigma/E/prediction/scale or J.

All 22 full sigma arrays are positive, finite and ordered; every saved mask has
N true entries and zero false entries. Minimum required sigma319/sigma0 across
all roles is **0.1458077472**, well above the 1e−10 first-320 rule. Full tails
require separate care; examples below show their much larger dynamic ranges.

| Object | Full minimum sigma | sigma0/minimum sigma | Required sigma319/sigma0 |
| --- | ---: | ---: | ---: |
| B N1279 | 2.50313e−9 | 3.98139e8 | 0.571747085 |
| O N1279 | 1.91668e−11 | 5.19970e10 | 0.572427414 |
| Q N1279 | 1.93361e−8 | 5.15431e7 | 0.571643167 |
| U N1279 | 2.46940e−9 | 4.03561e8 | 0.567922799 |
| D N1279 | 2.46940e−9 | 4.03561e8 | 0.567922799 |
| Q B128/N1279 | 1.93280e−8 | 5.15646e7 | 0.571646670 |
| Q L10/N1599 | 9.56395e−22 | 1.04208e21 | 0.571643167 |

The mask means positive finite logarithmic readout, **not certified relative
accuracy of every tail singular value**. In particular, the box role's ~21-order
full range is not validated by its good first-320 ratio or Frobenius moment.

Independently recomputed left/right equation arrays, boundary and high-momentum
occupancies equal saved values exactly; orthogonality recalculations differ by
at most 4.42e−29. Across 22 heat objects: max left/right residuals
5.03974e−15/5.99561e−15; max relative residual 6.01581e−15; orthogonality
≤5.37310e−14; full-spectrum Frobenius-moment relative mismatch ≤6.45162e−16.
Across 22 static objects: max equation residual 2.41038e−12, orthogonality
≤5.63669e−14, relative symmetry defect ≤2.73192e−17. Full C/H and all spectra
are present, but only the first 320 states are saved: no full-state reconstruction
claim is made. The 384-entry minimum ledger matches its JSONL serialization;
all heat minima, minimizers and schedule values match their indexed rows.

For Q, the maximum first-320 occupation in the highest ceil(N/5) momentum modes
is about 0.510886, 0.541463, 0.355256, then 3.03079e−27 at N511/639/1023/1279.
The cutoff band itself moves with N. Across all roles, maximum boundary mass is
1.39569e−11, yet momentum occupation reaches 0.549534: a small spatial-edge mass
does not certify cutoff adequacy. These diagnostics accompany, not replace, G.

## All five fixed families: four-window fits

Each cell is **MAPE / worst percentage error** at the prespecified N1279/L8/B64.
All 45 objects and all windows were audited; complete values remain in
[development metrics](run-2-fixed/development-fit-metrics.json) and the CSV.
Targets 101–320 were already known; these are not blind validation results.

| Family | 1–100 | 101–300 | 301–320 | 1–320 |
| --- | ---: | ---: | ---: | ---: |
| B | 1.957695 / 5.474616 | 5.162069 / 6.644065 | 6.676396 / 6.812084 | 4.255348 / 6.812084 |
| O | 1.924015 / 5.723029 | 4.628515 / 6.016102 | 6.038109 / 6.170964 | 3.871458 / 6.170964 |
| Q | 1.709232 / 5.249433 | 4.277943 / 5.727547 | 5.760972 / 5.898319 | 3.567910 / 5.898319 |
| U | 1.939756 / 5.642399 | 4.882009 / 6.335276 | 6.365012 / 6.500197 | 4.055243 / 6.500197 |
| D | 1.939756 / 5.642399 | 4.882009 / 6.335276 | 6.365012 / 6.500197 | 4.055243 / 6.500197 |

Q's original joint-training J=0.8334677293752334 and nonzero quintic parameter
remain a finite selected improvement; the two training grids were not holdouts.
Q full-320 MAPE/worst at N511 was 33.441982/205.348415%, and at N639
6.759063/47.105298%: finer-grid improvement does not erase those coarse records.
Old fixed S0047/N1535 has full-320 3.738668/6.351622%; this comparator supplies
no transferred Route credit. O improves original J/M relative to B but has a
worse first-100 worst error; U/D both chose z=0, hence no logarithmic-structure gain.

## Coarse versus finer stability: G percent

| Family / grid pair | 1–100 | 101–300 | 301–320 | 1–320 |
| --- | ---: | ---: | ---: | ---: |
| B 639→1023 | 4.48971e−11 | 30.468002 | 46.784239 | 46.784239 |
| B 1023→1279 | 8.38239e−12 | 3.86666e−12 | 3.45572e−12 | 8.38239e−12 |
| O 639→1023 | 5.63345e−11 | 33.300874 | 51.355581 | 51.355581 |
| O 1023→1279 | 9.99487e−12 | 9.42814e−12 | 9.01258e−12 | 9.99487e−12 |
| Q 639→1023 | 4.78600e−11 | 35.452135 | 52.903616 | 52.903616 |
| Q 1023→1279 | 7.97679e−12 | 3.90075e−12 | 3.52840e−12 | 7.97679e−12 |
| U 639→1023 | 6.26273e−11 | 29.778919 | 45.780783 | 45.780783 |
| U 1023→1279 | 6.34534e−12 | 5.84754e−12 | 5.42058e−12 | 6.34534e−12 |
| D 639→1023 | 6.26273e−11 | 29.778919 | 45.780783 | 45.780783 |
| D 1023→1279 | 6.34534e−12 | 5.84754e−12 | 5.42058e−12 | 6.34534e−12 |
| Q B64→B128 | 0.00166273833 | 0.00165534288 | 0.00133267661 | 0.00166273833 |
| Q L8/N1279→L10/N1599 | 4.14243e−11 | 4.10750e−11 | 4.05694e−11 | 4.14243e−11 |

Every coarse pair fails the 2% line in the high-index windows. Every finer pair
and both fixed Q diagnostics pass. Thus **the full refinement chain does not
pass**; only its stated later pairs do. B128 also changes path quadrature, not
only splitting; the box pair keeps spatial step 1/80. Each object uses its own
E0 scale. Finite pairwise agreement is not infinite-cutoff convergence.

## Static comparison and scoped decision

All 22 same-parameter static owners are preserved without optimization. Across
their 88 windows, heat MAPE/worst are both very slightly lower in 58 and higher
in 30; there is no universal heat dominance. Maximum heat/static prediction
G is **1.29416910e−7%**, raw-energy relative difference **1.21261124e−7%**;
maximum absolute MAPE/worst differences are only 1.09671e−7/1.25963e−7 percentage
points. Do not call them identically equal or an established dynamical advantage.

Portfolio: **advance** Q0107 only as a finite engineering benchmark, with the
decisive positive fact being fixed-parameter finer-grid/time/box stability;
**stop** claims of whole-chain stability, resolved full-tail accuracy, logarithmic
structure gain, or demonstrated thermal superiority. A new architectural claim
requires a fresh scoped contract, not additional automatic repair computations.
Same-object ledger remained intact; frozen identities and earlier negative
records remain untouched. The authorized single repair is complete.
ARS interpretation/reproducibility checks distinguish saved arithmetic from
rerun verification, training from known development data, and tiny numerical
differences from mechanism evidence; no p-value, causal, or population claim.
Run passport remains `UNVERIFIED` as an independent-search reproduction;
A0/A1/A2/T0–T3 not evaluated; formal `UNASSIGNED`; B `NOT INVOKED`.
