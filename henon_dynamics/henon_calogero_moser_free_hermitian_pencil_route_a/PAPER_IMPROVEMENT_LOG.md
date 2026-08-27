# C196 paper improvement log

This records internal artifact-bound review/revision, not external peer
review, an independent error process, or an acceptance score.

## Artifact progression

| Stage | Pages | SHA-256 | Substantive state |
|---|---:|---|---|
| Round 0 | 2 | `2e24674136745c31b864676a29cbb5f37046b9375c0d15da2b46c06137704a28` | signs, rank-one simplicity, Newton factor, completeness, trace integrals |
| Round 1 | 2 | `e0707ed751677e8ac58dec6b0048b54f41daaa4b25b550d1835e259c75257b45` | simple `L_0`, gauged intercepts, forward/inverse global atlas |
| Round 2/final | 3 | `efa8b97487763be814a0e3c5b65fe56616a377e3e2aacc7d97e26e611061b008` | both ends, rank reversal, aperiodicity, schema-closed evidence and exact Route-A closure |

## Round 1 findings and repairs

1. **Major:** pencil completeness alone left the scattering geometry implicit.
2. **Major:** asymptotic velocities alone did not show global coverage.
3. **Major:** the inverse denominator sign and reconstructed simplicity needed
   proofs.
4. **Boundary:** calling the coordinates symplectic would require a separate
   two-form argument.

The revision added `e^*v_a=1`, derived
`Q_tilde_ab=ig/(lambda_b-lambda_a)`, proved the inverse for arbitrary ordered
`lambda` and real `a`, reused the rank-one contradiction for reconstructed
`Q_tilde`, and stated only the proved global bijection.

## Round 2 findings and repairs

1. **Major:** negative-time order must use `N+1-j`.
2. **Major:** intercepts belong to spectral lines, not fixed particle ranks.
3. **Major:** aperiodicity must follow from distinct velocities, not finite
   trajectories.
4. **Scope:** natural quantization must not become a target spectral claim.
5. **Evidence:** `N<=7` results needed an explicit regression-only firewall.

The final revision added both expansions and velocity errors, attached each
intercept to its spectral line, proved linear relative-diameter growth,
printed validation totals, locked
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, and added all
degenerate/model/source/declaration boundaries.

## Final format audit

- all three round hashes differ and round 2 equals `main.pdf`;
- final and two fresh fixed-epoch logs contain no warning, missing glyph, bad
  box, undefined reference, or error;
- all fonts are embedded and subsetted;
- two fresh builds are byte-identical to the release PDF;
- extracted text retains both abstracts, formulas, tuple, scope, declarations,
  and DOI references;
- all three pages were inspected at 140 dpi with no clipping, overlap, broken
  glyph, blank page, or illegible equation.
