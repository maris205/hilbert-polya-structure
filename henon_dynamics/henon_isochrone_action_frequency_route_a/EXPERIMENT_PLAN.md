# Certificate experiment plan

## Objective

Falsify implementation errors in the all-parameter proof of the Hénon isochrone action–frequency atlas without mistaking samples for a proof.  The theorem lives in `THEOREM_PACKAGE.md`; computation checks its algebra, boundary bookkeeping, serialization, and release reproducibility.

## Frozen inputs

- Candidate: `HCS-C295`; obstruction: `HEN-O279`.
- Source commit: `f8d3ad9a8940b54e82854b2924be353575ed8fcb`.
- Evaluation date and epoch: `2026-09-02`, `1788307200`.
- Evaluator SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
- Parameter grid: \(\mu,b\in\{1,2,3\}\), \(\ell\in\{0,1,2,3\}\), action multiplier \(k\in\{1,2,3\}\).

## Evidence design

For each of 108 grid points, set

\[
A=\sqrt{\ell^2+4\mu b},\quad B=\ell+A,\quad
I=kB/2,\quad J_r=(k-1)B/2,\quad E=E_c/k^2.
\]

Every algebraic value is stored as exact coefficients \(a+c\sqrt d\); decimal strings are used only for high-precision turning-point controls.  Eight additional cells cover the forbidden, circular, open-bound, escape, positive-energy, radial, signed-momentum, and Kepler faces.

## Independent gates

1. **Producer:** deterministic sorted JSON with a self-excluding compact payload hash.
2. **Checker:** no producer import; exact key/type/value schemas; duplicate and nonfinite JSON rejection; duplicate, non-string, anchor, alias, merge, and timestamp-coercion-safe YAML handling; independent reconstruction of all exact fields.
3. **Quadrature controls:** direct 90-digit period and apsidal integrals for every noncircular grid row.
4. **SymPy:** independent circular-minimum, action-frequency, Vieta, apsidal, escape, Kepler, and full-grid identities.
5. **Replay:** two isolated output paths must reproduce the canonical evidence byte for byte.
6. **Mutation:** repaired-hash semantic attacks plus raw JSON and YAML parser attacks must all be rejected.
7. **Paper revisions:** round 0 proves the core action/period theorem; round 1 closes apsidal and degenerate boundaries; round 2 adds the finite certificate, conservative Route-A evaluation, and declaration boundary.
8. **Build:** each round is compiled twice in isolated directories with fixed epoch and a settled warning scan; hashes, pages, fonts, and text sentinels are checked.
9. **Manifest:** exact 27 payload files, no sidecars, six fresh builds, and a self-excluded file ledger.

## Failure policy

Any schema escape, algebraic mismatch, quadrature residual, nondeterministic byte, PDF warning, missing/substitute font, missing sentinel, extra file, stale hash, or forbidden claim blocks release.  A passing finite grid never upgrades the theorem status or Route-A tuple by itself.
