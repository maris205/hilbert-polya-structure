# Round 2 independent final review

Manuscript: *Raw Rational-Prime Multipliers at a Frozen PCF Quadratic: Divisibility Obstruction and Exact Audit*  
Date of review: August 13, 2026  
Reviewer mode: full local read of the prior review/response, revised manuscript/PDF, raw research package, and new final manifest; independent symbolic spot-checks; independent temp-copy test/build/hash verification

Score: 8.8/10  
Verdict: PASS

## Executive assessment

The round-1 mandatory issues are fixed, and I do not find a new blocker.

In particular:

1. the manuscript now proves the claimed PCF provenance inside the paper itself and explicitly separates that provenance from the proof of the divisibility theorem and its multiplier corollaries; and
2. the new artifact manifest is internally consistent: I independently verified 45/45 hash matches against the current tree, and a fresh rebuild reproduced the same manifest byte-for-byte.

I also rechecked the main mathematical chain, the modulus-only boundary, the `p=2` open status, and the branchwise-only cotangent scope. I do not see a regression in any of them. The revised PDF is clean, the tests pass, and the visual presentation is acceptable.

## What I checked

- Read `paper/reviews/round1_review.md` and `paper/reviews/round1_response.md`.
- Read the revised `paper/manuscript.tex` and confirmed that `paper/manuscript.pdf` is byte-identical to `paper/paper_round1.pdf`.
- Read the main package materials, including:
  - `notes/PROOF_PACKAGE.md`
  - `notes/DERIVATION_PACKAGE.md`
  - `results/VALIDATION_REPORT.md`
  - `results/EXPERIMENT_RESULTS.md`
  - `results/final_result_manifest.json`
  - `results/proof_audit.json`
  - `results/candidate_multiplier_audit.json`
  - `results/control_audit.json`
  - `results/conjugacy_audit.json`
  - `results/symplectic_bridge_audit.json`
  - `results/source_lock_validation.json`
  - `paper/CLAIM_MANIFEST.json`
  - `paper/EXPERIMENT_PASSPORT.json`
  - `paper/FIGURE_PACKAGE.json`
  - `paper/INTEGRITY_PRE_REVIEW.md`
- Inspected the key implementation files behind the exact audit and manifest generation, especially:
  - `code/prime_multiplier/dynatomic.py`
  - `code/prime_multiplier/resultant.py`
  - `code/prime_multiplier/candidate.py`
  - `code/prime_multiplier/controls.py`
  - `code/prime_multiplier/symplectic.py`
  - `code/prime_multiplier/protocol.py`
  - `code/scripts/build_result_manifest.py`
  - `code/tests/test_protocol.py`
- Independently reran in a temporary copy of the project:
  - `python -m pytest -q -p no:cacheprovider code/tests` → `37 passed in 35.06s`
  - manifest verification and rebuild
  - `pdflatex -> bibtex -> pdflatex -> pdflatex` for `paper/manuscript.tex`

## Targeted fix 1: PCF exact critical orbit and non-dependence

This fix is real.

The revised manuscript now gives the critical orbit explicitly at
`paper/manuscript.tex:247-257`:

\[
0 \mapsto 1 \mapsto -(u-1) \mapsto (u-1) \mapsto (u-1).
\]

The algebra checks out. Writing \(d=u-1\), the manuscript's identity
\[
f_u(\pm d)=1-u(u-1)^2=d
\]
is equivalent to \(P(u)=u^3-2u^2+2u-2=0\), since
\[
1-u(u-1)^2-(u-1)=-(u^3-2u^2+2u-2).
\]
I independently verified that equivalence symbolically.

Just as importantly, the manuscript now says explicitly at
`paper/manuscript.tex:255-257` that this finite critical orbit supplies
parameter provenance only, and that neither Theorem 3.1 nor the multiplier
corollaries uses postcritical finiteness.

That non-dependence claim is consistent with the actual proof structure:

- The divisibility theorem at `paper/manuscript.tex:180-217` uses only monicity, algebraic-integer coefficients, the factorization \(F'=mH\), and rationality of the multiplier.
- The raw-prime corollary at `paper/manuscript.tex:289-300` specializes only to `g'(z)=2z`, the fixed-point exclusions \(\lambda=\pm2\), and the linear conjugacy.
- The exponent-prime corollary at `paper/manuscript.tex:309-315` is the stated 2-adic valuation argument.

So the revised paper no longer has the standalone PCF-framing gap identified in round 1.

## Targeted fix 2: 45/45 final manifest integrity

This fix is also real.

The current `results/final_result_manifest.json` has SHA-256

`85f356dfce1e2257e7482840f1125a279289ccc215d52e1498a9dd0d94f18789`

and contains 45 artifact entries.

I independently checked all 45 listed files against the current tree in a
temporary copy:

- missing entries: `0`
- hash mismatches: `0`
- total matches: `45/45`

I then reran the project’s own deterministic builder,
`code/scripts/build_result_manifest.py`, in the temp copy. It reproduced:

- the same 45-entry artifact set; and
- the same manifest SHA-256
  `85f356dfce1e2257e7482840f1125a279289ccc215d52e1498a9dd0d94f18789`.

So the old manifest-integrity problem is resolved.

## Regression recheck

### 1. Main theorem/corollary chain

I still do not see a flaw in the core chain.

- Theorem 3.1 remains correctly stated for points fixed by \(F^n\), not only exact period-\(n\) points (`paper/manuscript.tex:188-194`).
- The monicity/integrality step and the chain-rule content factorization remain correct (`paper/manuscript.tex:197-215`).
- The modulus-only limitation remains explicit (`paper/manuscript.tex:227-231`).
- The period-one closure \(\lambda=\pm2\Rightarrow u=0,2\), both impossible for the frozen cubic, remains correct (`paper/manuscript.tex:295-299`).
- The `p=2`, `n>=2` rational exponent-prime case remains explicitly open (`paper/manuscript.tex:302-319`), which is the right scope.

### 2. Exact audit / controls / conjugacy

No regression found.

- `results/candidate_multiplier_audit.json` is still `PASS`, with the frozen periods
  `n=1,2,3,4`, formal degrees `2,2,6,12`, exact degrees `2,2,6,12`, and no rational candidates.
- `results/control_audit.json` is still `PASS`. The controls still recover:
  - `{0,2}`, `{4}`, `{8}`, `{16}` for `z^2`;
  - `{-2,4}`, `{-4}`, `{-8,8}`, `{-16,16}` for `z^2-2`;
  - and `{-1,3}` at period 1 for `z^2-3/4`, with formal period-2 contamination recorded and exact period-2 degree reduced to zero.
- `results/conjugacy_audit.json` is still `PASS` for all periods 1 through 4, with all listed checks true.

So the exact-audit side still supports the manuscript’s intended role: implementation certificate, not all-period proof substitute.

### 3. Complex-modulus / open-boundary / cotangent scope

These boundaries are preserved clearly enough.

- Nonrational complex modulus remains outside the theorem (`paper/manuscript.tex:227-231`, `279-280`, `497`).
- The `p=2` exponent-prime residual remains open and is not blurred by the finite audit (`paper/manuscript.tex:305-319`, `496`, `506-510`).
- The cotangent bridge is still correctly scoped as branchwise exact only. The manuscript continues to state the critical-line singularity, overlapping branch images, noncompactness, and the exclusion of critical cycles with zero multiplier (`paper/manuscript.tex:461-468`, `473-477`, `498`).
- `results/symplectic_bridge_audit.json` remains `PASS` with the corresponding negative-geometry flags true:
  one-form pullback zero, determinant one on the regular locus, reciprocal-pair return spectrum, rejection at `q=0`, overlapping branch images, and unbounded regular domain.

## Build, PDF, and visual check

The package passes an independent temp-copy rebuild and presentation check.

- `paper/manuscript.pdf` and `paper/paper_round1.pdf` are byte-identical:
  `160e9c6fa12c35f500fbae39d9316fc55e8c9b4f1b044ef3deda6037e0b5b1c3`.
- In the temp copy, `pdflatex -> bibtex -> pdflatex -> pdflatex` succeeded cleanly.
  (`latexmk` is not installed in this environment, so I used the explicit compile path instead.)
- Resulting PDF checks:
  - 11 total pages
  - conclusion on page 8
  - references begin on page 10
  - no undefined citations/references
  - no LaTeX warnings
  - no overfull or underfull boxes
  - all fonts embedded in the PDF
- I visually inspected rendered pages containing Figures 1, 2, and 3 and did not find a figure collision, truncation, or unreadable panel.

## Non-blocking note

I still mildly prefer more publication-style typography in Figure 2 panel (b), where the exact polynomials retain code-normalized strings such as `L**2`. But this is presentation polish only. It does not affect correctness, scope discipline, or artifact integrity, and it is not a reason to hold the package.

## Bottom line

Round-1’s two substantive defects are fixed:

- the PCF label is now established in the paper and explicitly marked as non-essential to the proof chain; and
- the final artifact manifest is now genuinely consistent with the current package.

I do not see a mathematical, reproducibility, or scope regression elsewhere in the package. My final round-2 recommendation is therefore:

**PASS**.
