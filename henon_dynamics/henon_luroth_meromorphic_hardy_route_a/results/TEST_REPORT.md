# Executed test report

- Producer: deterministic exact payload, PASS.
- Separate checker: 12 branches; 16 seven-dimensional finite matrices; 10 operator-residue matrices and 10 scalar residues; 340 complete four-branch words. Independent checker: 1,169 matrix cells plus all word itineraries and all residue ranks. SymPy: 220 exact identities. High precision: six dual Hurwitz values, the s=1 value, four telescoping controls and three complex-phase controls; working digits 100, agreement tolerance 1e-80.
- Repaired-hash and parser audit: 32 semantic attacks, 3 JSON attacks and
  9 strict YAML attacks, **44/44 refused** by the standalone checker.
- Two-directory replay and three smoke tests are rerun as mandatory release
  lanes; their actual stdout is captured in the release manifest.
- All six entry scripts must refuse both optimized modes (12 refusals).
- All three manuscript rounds have passed independent double-fresh builds,
  settled warning scans and embedded/subset-font checks. Final PDF has four
  pages, all actually viewed by root after rasterization at 95 dpi.
- A self-excluding exact physical ledger and full nonwrite reconstruction
  remain required for a release PASS; read the final manifest for that receipt.

The initial failed real-input phase test is
retained in the seven-mode review. No failed run is included in PASS counts.
