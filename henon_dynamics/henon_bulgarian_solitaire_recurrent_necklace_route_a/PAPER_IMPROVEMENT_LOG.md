# C190 paper improvement log

This records two actual internal review--revision--recompile rounds.  It is
not external peer review, an independent error process, or an acceptance
score.

## Artifact progression

| Stage | Pages | SHA-256 | Substantive state |
|---|---:|---|---|
| Round 0 baseline | 2 | `5aeb6d8128631751374a0dbc710095c781334a8bc4681724b7894adae12819af` | Brandt coordinates, fixed ledger, Möbius cycles, zeta, triangular/evidence boundary |
| Round 1 | 2 | `85cc22910952e28904f73362d1b0d801aca7c6d55631edfaee7388fdb5cbb366` | full Koopman characteristic polynomial, transient zero multiplicity, root spectrum, N=8 matrix-level sentinel |
| Round 2 / final | 2 | `aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d` | recurrent reflection family with nonfaithful caveat, noninvertible/global boundary, audit totals, strict Route-A stop, compact declarations and references |

## Round 1 hostile reading and repairs

### Findings

1. **Major:** a recurrent-only spectral discussion would underuse the
   noninvertible owner and leave the full operator ambiguous.
2. **Major:** `det(I-zU)=zeta^-1` needed a proof that transient vertices add
   zero characteristic roots but no determinant factors in `z`.
3. **Minor:** the N=8 cycle sentinel did not expose the transient spectral
   multiplicity.

### Repairs implemented before recompilation

- Added
  `det(xi I-U)=xi^(p(N)-binom(k,r)) product_d (xi^d-1)^(C_d)`.
- Separated algebraic zero multiplicity from unclaimed nilpotent Jordan sizes.
- Added reciprocal determinant, trace, and all root multiplicities.
- Added the N=8 values: zero multiplicity 16 and fourth-root multiplicities
  `(2,1,2,1)`.

## Round 2 hostile reading and repairs

### Findings

1. **Major:** a reflection claim could be misread as a global reversor of a
   noninvertible map.
2. **Major:** the `k` phase formulas could be misread as `k` distinct maps on
   a nonfaithful weight layer, which fails at the triangular boundary.
3. **Major:** a natural recurrent permutation should not be promoted from the
   frozen `A4_FORMAL_HINT` verdict to target quantization.
4. **Minor:** evidence totals, source ownership, AI-use disclosure, and the
   finite-regression boundary needed to be visible in the paper.
5. **Visual:** a literal missing backslash before `qquad` was found in the
   first round-2 render and repaired before freezing the final PDF.

### Repairs implemented before final recompilation

- Restricted `Q rho Q=rho^-1` to the recurrent core and explicitly denied a
  global reversor.
- Called `rho^a Q` phase-labelled formulas and stated that their actions need
  not be distinct.
- Locked the exact tuple
  `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
- Added 658,664 checker assertions, 2,210 SymPy checks, byte replay, and
  118+1 hostile rejections with the “not independent review” caveat.
- Added declarations, verified DOI links, fixed the rendered `\qquad`, and
  rebuilt from a clean fixed epoch.

## Final format audit

- final/fresh logs: no warnings, missing glyphs, bad boxes, or undefined
  references;
- all fonts: embedded and subsetted;
- two fresh fixed-epoch builds: byte-identical to `paper/main.pdf`;
- visual inspection: both pages readable, no clipping, overlap, broken glyph,
  or blank page; the compact declarations and references remain legible.
