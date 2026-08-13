# Paper 4 independent peer review — Round 1 and final gate

**Manuscript:** *One Clock, One Characteristic: A Frobenius-Suspension Positive Control for Arithmetic Flow Zeta Functions*  
**Review date:** 2026-08-13  
**Final recommendation:** **ACCEPT**  
**Issue count:** **0 critical / 0 major / 0 residual required minor**

## 1. Submission lock

- `paper/manuscript.tex` SHA-256: `da04db49fc641c938f0ca2ecee7d9b4ad89b78a7fc6adebe871280b434ba8041`
- `paper/manuscript.pdf` and `paper/paper.pdf` SHA-256: `775c6016ae17fceb2f875b3cc5608563efae85b037553d8167597c4c45b5ae6a`
- Release PDF: 16 pages; the two PDFs are byte-identical.

## 2. Mathematical and Route verdict

The central proof chain passes independent checking: closed points of
\(\mathbb P^1_{\mathbb F_2}\) correspond to exact Frobenius cycles; the mapping
torus decomposes into circles of least period \(\deg(x)\log 2=\log N(x)\); the
formal orbit, Artin--Mazur, and Hasse--Weil zetas agree; absolute Euler-product
convergence is exactly \(\Re s>1\); and the one-clock obstruction follows from
unique factorization. The universal circle compiler is correctly classified as
an exact but target-encoded proves-too-much control.

The cohomological convention is sound: the manuscript distinguishes the
arithmetic point action \(a\mapsto a^2\) from the Frobenius operator in the
cited cohomological trace convention. For \(\mathbb P^1/\mathbb F_2\), the
cohomological determinant factors \(1-t\) and \(1-2t\) are correct, and no
operator equivalence with a circle-flow transfer determinant is inferred.

The three target-specific evaluations are internally consistent:

- native finite-field target: `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY`;
- unchanged flow against Riemann \(\zeta/\xi\): `ROUTE_A_REJECTED`;
- disjoint-prime compiler: `ROUTE_A_REJECTED / PROVES_TOO_MUCH`.

For all three, `A4_FAIL` with evidence `NOT_TESTABLE` is the correct enum pair:
no Hilbert space, operator domain, or natural quantization has been frozen.
`route_b_invocation_allowed: false` is consistent throughout.

## 3. Required minor revisions — closed

1. **Same-cycle-type theorem:** the original statement omitted the possibility
   of infinite permutation orbits. The final manuscript and proof audit now
   require every point to be periodic and explicitly explain that additional
   infinite orbits would give additional components. **Addressed.**
2. **Audit-source integrity:** `notes/proof_audit.md` now has
   \(\sum_{d\mid n}d\,a_d\), and `notes/source_audit.md` has a clean
   `\{\rm prime\}` expression with no embedded carriage-return byte. The
   protocol and composition blueprint were synchronized. **Addressed.**

The related wording improvement was also made: Table 1 now identifies the
discrete topology as the main additional modeling choice while separately
disclosing the frozen roof and orbit-zeta normalization.

## 4. Citation and source-claim audit

All six bibliography entries have coherent identities and support the claims
assigned to them: Artin--Mazur for the fixed-point zeta; Deligne for the
closed-point product, Frobenius dictionary, cohomological determinant, and
native functional relation; Parry--Pollicott for suspension conventions only;
Stacks Tags `01TF` and `03SL` for finite residue extensions and Frobenius
terminology; and Milne as an authoritative secondary cross-check. The Deligne
DOI/Numdam metadata, Artin--Mazur DOI metadata, Parry--Pollicott Numdam metadata,
and both Stacks tag identities agree with the bibliography. No citation is used
to transfer compact/hyperbolic results to the neutral countable suspension, and
no citation is used to claim a flow transfer-operator theorem. **Citation
verdict: PASS; no identity or claim-mapping defect found.**

## 5. Reproduction and release checks

- `bash experiments/reproduce.sh`: **13/13 tests passed**.
- Exact outputs: 8190 monic polynomials examined, 747 affine irreducibles, 748
  projective closed points through degree 12, and all 90 clock-grid solutions
  satisfy the same-characteristic/exponent identity.
- Manifest SHA-256:
  `1be4de28d2ca91829289afbebcbeff228294f289370874c97e2e4712f4be863c`.
- All three Route-A YAML files parse and reproduce the manuscript verdicts.
- Final LaTeX log has no unresolved references/citations, missing characters,
  overfull or underfull boxes, or LaTeX warnings relevant to release.
- `pdftotext` status-token adjacency scan is clean; visual reinspection of the
  revised candidate-lock, same-cycle, claim-ledger, and artifact-map pages found
  no clipping or missing glyphs.

## 6. Final adjudication

Both required minor findings are fully resolved. No critical, major, or
required minor issue remains. The paper is mathematically correct within its
explicit finite-field scope, keeps its cohomological and flow-operator notions
separate, rejects the Riemann promotion for a proved reason, and does not invoke
Route B.

**FINAL GATE: ACCEPT.**
