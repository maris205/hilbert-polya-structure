# C163 test report

- Producer: PASS; deterministic exact evidence frozen.
- Independent checker: PASS; 646 assertions.
- SymPy reconstruction: PASS; 170 checks.
- Replay: PASS; byte-for-byte equality.
- Hostile mutation suite: PASS; 94 repaired-hash semantic mutations and one
  stale-hash mutation rejected.
- Algebra gate: PASS; exact primitive irreducible integer polynomial, monic
  rational minimal polynomial, and nonintegrality receipt, not a decimal
  root-of-unity guess.
- Control gate: PASS; exact moved-hole order-four spectrum and 32 residue/TV
  rows independently reconstructed.
- Claim boundary: PASS; phase claims are explicitly source-side, while
  self-adjointness, target/arithmetic structure, and Route B remain false.
- PDF/manifest: recorded in `paper/COMPILE_REPORT.md` and
  `C163_RELEASE_MANIFEST.json` after final closure.
