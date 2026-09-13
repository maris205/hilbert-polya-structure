# Independent source-design review — Paper 21

Verdict: PASS.

Scope checked: the frozen ten-file author set under `papers/21-three-mode-hamiltonian-cubic-degree/`, plus the three candidate-review provenance files at repo root.

## 1) Frozen inventory and framing check

The paper-root inventory is exactly these ten files and no others:

| Relative file | Bytes | LF | Mode | Hygiene |
|---|---:|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 3238 | 73 | 0644 | OK |
| `experiments/EXPERIMENT_TRACKER.md` | 2097 | 37 | 0644 | OK |
| `notes/CITATION_VERIFICATION.md` | 1338 | 17 | 0644 | OK |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 3266 | 55 | 0644 | OK |
| `notes/NOVELTY_ASSESSMENT.md` | 3014 | 58 | 0644 | OK |
| `notes/PROOF_PACKAGE.md` | 16199 | 427 | 0644 | OK |
| `notes/RESEARCH_QUESTION.md` | 2362 | 49 | 0644 | OK |
| `refine-logs/FINAL_PROPOSAL.md` | 2794 | 67 | 0644 | OK |
| `refine-logs/INITIAL_PROPOSAL.md` | 1543 | 44 | 0644 | OK |
| `refine-logs/REVIEW_SUMMARY.md` | 1392 | 28 | 0644 | OK |

Recomputed twice from the paper root using the required framed record
`uint64_be(name_len)||name_utf8||uint64_be(content_len)||content` over byte-sorted
relative POSIX names:

- content bytes: `37243`
- total LF: `855`
- framed length: `37691`
- aggregate SHA-256: `6ead7872f6af98876b89e62f1b34573cd8fcfc4a61f4202a5a8214c7590acf8f`

All ten files are UTF-8, have one terminal LF, and contain no CR, NUL, or BOM.
No symlinks were present.

Candidate-review provenance hashes matched exactly:

- R1: `d9362d3b07c38e2248494d2c0ec43209e7b0ce8fb089737326d61888b5d1d846`
- R1 correction: `6f455d8b40c873b8fc18568d95ed3e3b97de7528eddae911e83a00fe5214c132`
- R2: `70592ffe85111cefde9e8fa872688958c22ad7cbe6bf4671151d9e5893aad387`

The frozen source consistently uses the corrected selector theorem, not the
superseded R1 wording.

## 2) Independent theorem replay

I replayed the whole theorem family directly.

- Gradients are correct:
  - `∇V = (2q1 q2^2 q3^2 + g q1^{g-1}, 2q1^2 q2 q3^2, 2q1^2 q2^2 q3)`
  - `∇W = (2p1 p2^2 p3^2, 2p1^2 p2 p3^2, 2p1^2 p2^2 p3 + g p3^{g-1})`
- The triangular inverses are the obvious subtraction inverses.
- The Jacobian block forms are symplectic because the Hessians are symmetric, with `H_W` evaluated at the intermediate `P` for `T ∘ S`.
- The exponent matrices multiply correctly:
  - `A = [[g-1,0,0],[2,1,2],[2,2,1]]`
  - `B = [[1,2,2],[2,1,2],[0,0,g-1]]`
  - `C = BA = [[g+7,6,6],[2g+4,5,4],[2(g-1),2(g-1),g-1]]`
- The selector ledger is consistent and genuinely two-faced:
  - `M_S = (g-2) - 2x - 2y`
  - `M_T = (2g-6)x + (g-6)y - 6`
  - there is no third independent selector gap.
- Cone invariance is consistent with the stated split:
  - `U2-U1 = g-3-x-2y`
  - `U3-U1 = g-9 + (2g-8)x + (g-7)y`
  - `H = 1/2 (g^2 + 2gx + 4gy - 4g - 24x - 24y - 25)`
  - the `8≤g≤11` and `g≥12` bounds check out.
- Visibility and degree are correctly stated with the third coordinate:
  - `C-A` is entrywise positive
  - `U3-U2 > 0` and `U3-U1 > 0`
  - `deg(F^n) = e_3^T C^n 1` for `n≥0`
- The PF / row-sum bound is correct:
  - row sums are `g+19`, `2g+13`, `5(g-1)`
  - all are below `(g-1)^2` for `g≥8`
- The characteristic polynomial and mod-5 table are correct:
  - `χ_C(t) = t^3 - (2g+11)t^2 + (g^2-16g+19)t - 9(g-1)^2`
  - the residue-table values for `g mod 5 = 2,3,4` match the displayed no-root table
  - the corollary is correctly limited to the arithmetic statement; nothing overstates irreducibility over `K`
- The `g=7` note is correctly framed as a boundary failure, not a selector tie.

I found no stale `e_2`-visibility wording in the frozen source; all explicit degree claims use `e_3`.

## 3) Collision / novelty audit

The Paper12–20 comparison is bounded and internally non-colliding:

- Paper 12: period-three residue law — different invariant and no 3-mode sextic shear.
- Paper 13: primitive-cycle covers — different finite-cover geometry.
- Paper 14: four-step torus escape — different torus-escape mechanism, not a canonical gradient pair.
- Paper 15: quartic trace fibers — different fiber structure and dimension.
- Paper 16: support-size torus escape — different support threshold theorem.
- Paper 17: torus-coset decay — different recurrence family and geometry.
- Paper 18: marked scalar-boundary ramification — different boundary/ramification problem.
- Paper 19: translate/GCD obstruction — different translate obstruction.
- Paper 20: coupled Hamiltonian shear degree matrices in `A^4` — closest predecessor, but it is still a smaller, two-mode, four-dimensional family.

This supports only the paper-local bounded novelty statement, not any global
priority claim.

## 4) Citation audit

I verified the two cited arXiv records on the official arXiv pages:

- Blanc & van Santen, `1912.01324`, “Dynamical degrees of affine-triangular automorphisms of affine spaces”, submitted 2019-12-03.
- Shao & Sun, `2509.14584`, “Dynamical degrees of affine-triangular automorphisms in dimension four”, submitted 2025-09-18.

The source uses them only as terminology / context boundaries. It does not
pretend they prove the Paper21 theorem.

## 5) Permission and anti-claim audit

The frozen source stays in the allowed lane:

- no experiments, datasets, code, figures, builds, transport artifacts, or manuscript files in the source package;
- no genericity, entropy, topological-degree, periodic-point classification, torus/conjugacy, positive-characteristic, or priority claim in the theorem target;
- the title, scope, and page plan remain narrow and proof-first;
- the page budget stays in the stated `24–29` substantive-page band.

## 6) Minor wording notes

Keep the exact `e_3` visibility phrasing and the `H_2 = 2H` normalization in any downstream writing.
Keep the distinction between canonical Hamiltonian shears and the broader affine-triangular class explicit.

Overall conclusion: the frozen Paper21 source design is coherent, correctly framed, and ready for subsequent source-lock authorship only. It does not authorize manuscript/build/publication work.

SOURCE_DESIGN_PASS
