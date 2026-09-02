# Verification plan — HCS-C300

The full-data theorem is analytic.  Computation is a deterministic regression and release audit.

## Finite design

- Twenty constructed cases prescribe exact rational \(a,\rho_L,\rho_R,\rho_*,u_*\) and derive \(u_L,u_R\) from the two wave curves.
- The case spectrum contains all four nondegenerate patterns and every one- or two-zero-wave boundary: `R-R`, `R-S`, `S-R`, `S-S`, `Z-R`, `Z-S`, `R-Z`, `S-Z`, and `Z-Z`.
- Seventeen rarefactions check fan edges, midpoint characteristic relations, density profiles, and Riemann invariants.
- Seventeen shocks check both speed expressions, two Rankine--Hugoniot residuals, two strict Lax gaps, direct mechanical entropy production, and its closed negative formula.
- Four paired cases check common density scaling without changing velocity, pattern, or speeds.
- Four decreasing sound speeds check the exact symmetric separating root \(e^{-1/(2a)}\) and compressive root \(y^2\), \(y-y^{-1}=1/(2a)\).
- Eight boundary rows separate theorem domain, zero waves, vacuum inputs, and pressureless behavior.
- Total audited receipt cells: 437.

## Independent gates

1. Canonical JSON producer with payload self-hash.
2. Producer-free checker with an independently coded log-density bisection and exact formula reconstruction.
3. SymPy checks for eigenvalues, entropy compatibility/convexity, both shock families, Lax gaps, strict entropy production, fan invariants, and pressureless probes.
4. Two fresh producer outputs must equal the archived evidence byte for byte.
5. Repaired-hash semantic mutations plus hostile JSON/YAML parser mutations must all fail.
6. Three substantive PDFs must rebuild twice per round with fixed epoch, settled logs, embedded subset fonts, extracted-text contracts, and raster checks.
7. The release closer admits exactly 27 payload files and then writes the self-excluded 28th manifest.
