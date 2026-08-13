# Independent manuscript review — Round 2

**Paper:** *Normalized Algebraic Periodic Actions versus Prime Logarithms:
A Hénon Design Certificate*  
**Revised snapshot:** `paper/paper_round1_revision.pdf`  
**Review date:** 2026-08-14  
**Review mode:** fresh, read-only verification of the Round-1 revision; no
manuscript, code, result, figure, or integrity artifact was edited  
**Verdict:** `PASS`  
**May finalize:** **YES**  
**Confidence:** **0.98**

The two required scientific/provenance repairs and all five minor Round-1
items are closed.  I found no residual mathematical, scope, citation,
reproducibility, or presentation defect that should block finalization.  The
paper should retain its existing conservative publication boundary:
`MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED`; that is a positioning judgment about
standalone depth, not a correctness or integrity failure.

## Round-1 closure matrix

| Item | Round-2 verdict | Independent evidence |
|---|---|---|
| R1: false `log|A|` Figure-2 cell | `FULLY_ADDRESSED` | The displayed row and the machine ledger are exactly `EDGE | STOP/OUT | STOP/OUT`.  The manuscript separately states that `|A|` is algebraic but that no conclusion is made about `log|A|`. |
| R2: cell-level provenance | `FULLY_ADDRESSED` | `scope_matrix_ledger.py` derives all 27 cells through named fail-closed predicates and labels each cell `FROZEN_JSON_DERIVED` or `THEOREM_DEFINED`; Figure 2 consumes this ledger rather than a hard-coded matrix.  Five assertions check every status/evidence entry and mutations of the `log|A|`, algebraic-gauge, and `beta=0` predicates. |
| M1: deductive primary evidence | `FULLY_ADDRESSED` | Claims C4 and C8 in `CLAIM_MANIFEST.json` now cite `notes/PROOF_PACKAGE.md` as primary evidence and identify the corresponding JSON only as supporting implementation evidence. |
| M2: projective-dimension wording | `FULLY_ADDRESSED` | Theorem 5.1 explicitly identifies the fixed hyperplane `Z=0`; its homogenized equations force every `Q_j=0` there, and the positive-dimensional-projective-component argument is stated against that hyperplane. |
| M3: arXiv identifier | `FULLY_ADDRESSED` | The compiled bibliography prints `arXiv:2412.01668 [math.DS], v2`; extracted PDF text contains no raw HTTP/WWW URL. |
| M4: Figure-1 readability | `FULLY_ADDRESSED` | The countercontrol now uses the readable two-line label “Map-only countercontrol: transcendental normalization”; both the master and the compiled page are legible. |
| M5: conservative novelty | `FULLY_ADDRESSED` | The manuscript makes no historical-first or new-transcendence-theorem claim and explicitly retains the merge-if-depth-required disposition. |

## Mathematical and scope regression audit

The core chain remains correct.  Pole-free evaluation of a
`Qbar`-rational potential at finitely many algebraic orbit points gives an
algebraic action; Hermite--Lindemann excludes its equality with any logarithm
branch of a nontrivial algebraic target.  Algebraic scaling, averaging,
repetition, real/imaginary parts, and modulus preserve algebraicity, while
the manuscript correctly leaves logarithmic post-processing outside the
claim.

The autonomous and stepwise gauge formulas retain the full endpoint and
constant ledger.  Defined algebraic endpoint mismatch preserves algebraicity;
poles, undefined steps, multivalued gauges, and transcendental normalization
are not silently absorbed into the theorem.  The identity-map `log 2`
control remains a symbolic normalization counterexample rather than a numeric
experiment.

For the Hénon specialization, direct differentiation verifies the exact
potential, the type-1 generating function has the stated opposite sign on
the graph, and the cyclic recurrence preserves both neighbor slots at
periods one and two.  The no-point-at-infinity argument proves finiteness of
the affine periodic scheme for every finite period.  The non-Archimedean
maximum argument is quantified over the orbit field and proves only
`3A_G` is `S`-integral; the fixed point at `a=-1` with action `-1/3` keeps the
denominator-three boundary sharp.

The limitations remain aligned across abstract, theorems, figures, claim
manifest, and conclusion: no claim is made for `log|A|`, multiplier or
return-time clocks, multivalued or closed-nonexact cocycles, transcendental
normalizations, approximation, prime-orbit correspondences, zero-data fits,
zeta/trace/determinant constructions, or quantization.  Static JSON is
consistently described as implementation evidence; the all-period result is
deductive.

## Independent reproducibility and presentation checks

- Safe code suite: **82 passed in 0.95 s**.
- Figure-2 ledger suite: **5 passed in 0.03 s**.
- Frozen final result manifest: **35/35 hashes match**; its required-artifact
  validation remains `PASS`.
- Figure package: **27/27 declared source/input/output hashes match**.
- Two fresh full figure regenerations in an isolated copy reproduced all
  nine visual outputs plus the 27-cell provenance JSON byte for byte; their
  hashes match `FIGURE_PACKAGE.json`.
- Two fresh prescribed manuscript builds in that isolated copy produced the
  same PDF hash as the revised snapshot:
  `871197f5a385f68accf6d3ba7876e5df830e9eef43b4bf9e9ae52a3edb7bc996`.
- The revised PDF has **13 pages**, letter size, embedded/subset fonts, and no
  LaTeX error, warning, overfull/underfull box, undefined-reference, or
  undefined-citation diagnostic in the final logs.
- Independent visual inspection of all three masters and their affected
  compiled pages found no clipping, overlap, illegible label, or color/status
  ambiguity.  Figure 2 visibly uses the corrected `target-log conclusion`
  heading and corrected `log|A|` row.
- Source lock v3 and all 35 official results remain unchanged.  This review
  executed no candidate parameter substitution, periodic-point solve,
  candidate action evaluation, external prime-table access, or Riemann-zero
  access.

## Final decision

`PASS`.  Every mandatory Round-1 acceptance condition is independently
verified, no new blocking issue was found, and the revised snapshot may be
promoted to the final paper subject to the project's routine final integrity
copy/hash step.
