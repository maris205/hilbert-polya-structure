# HCS-C18 result certificates

These files are the frozen compact outputs of the HCS-C18 producer and its
independent checker.

- `arithmetic_counts.csv`: 2,000 exact rows of phi, roots of minus one, and
  unoriented open counts.
- `open_series.csv`: 12 partial-sum/closed-form comparisons with elementary
  tail bounds.
- `endpoint_ledger.csv`: 30 rational endpoint rows and the data underlying
  147 exact composition checks.
- `exact_certificates.json`: formula locks, the residue at s=1, endpoint
  metadata, and three representative-dependent double-coset products.
- `scattering_checks.json`: five spectral points at each of levels 2, 6, 30,
  and 210, Walsh channels, functional equation, unitarity, determinant,
  product permutations, and projector-resolved scope controls.
- `summary.json`: compact scientific decision and headline metrics.
- `independent_check.json`: PASS report from a 110-digit implementation that
  imports no producer code.

The projector fields certify parameter-to-edge assignment and endpoint-path
sensitivity only. They explicitly do not claim that the spectral parameter is
dynamical time or that intrinsic chronology has been constructed.
