# Paper configuration

## Identity

- **Paper ID:** `integral-area-henon-multiplier-support-v1`
- **Title:** *Rational Periodic Multiplier Moduli under Good Reduction: A
  Hénon Certificate and Exact Audit*
- **Author:** Liang Wang
- **Article type:** specialist mathematical-dynamics article; theorem plus
  source-locked exact implementation audit
- **Format:** 11 pt `article`, one-inch margins, author--year citations
- **Pre-review date:** 2026-08-14
- **Round-1 revision date:** 2026-08-14
- **Finalization date:** 2026-08-14
- **Revision status:** `COMPLETE_LOCAL / FINAL_REVIEW_PASS`; all three Round-1
  minor comments independently verified in Round 2
- **Compiled length:** 11 pages including appendices and references

## Central claim configuration

The paper may claim the following and no stronger conclusion:

1. finite periodic points of the stated monic generalized Hénon compositions
   over an (S)-integer ring are (S)-integral;
2. determinant-one integral return monodromy makes both multipliers algebraic
   (S)-units;
3. an **exact** rational multiplier modulus is supported only on the
   predeclared rational bad primes;
4. for the frozen integral map (H_u(X,Y)=(X^2-u-Y,X)), every exact rational
   multiplier modulus equals one at every period;
5. the exact (n\leq3) ledger audits the implementation but does not prove the
   all-period statement;
6. the (a=-15/16) fixed point with multipliers (2,1/2) is a sharp
   bad-support control.

## Mandatory scope language

- The paper is **not** a universal symplectic no-go theorem.
- It does not classify irrational or approximate moduli, singular values, or
  Lyapunov exponents.
- It does not identify complex conjugation with the reciprocal eigenvalue.
- It does not decide whether (+1) or (-1) occurs for the frozen map.
- It makes no prime--orbit correspondence, spectral determinant, target-zero,
  compactness, or quantization claim.
- No external prime table or zero-ordinate dataset may be used.

## Evidence policy

| Evidence class | Permitted role |
|---|---|
| Main mathematical proof | All-period theorem and frozen corollary |
| Exact period ledger, (n=1,2,3) | Software implementation audit only |
| Five selected-embedding cycles | Finite exact observations only |
| Sharp and boundary controls | Assumption and classification checks |
| Approximate display values | Human-readable display only; never rationality evidence |

The source lock is the prospective commitment.  The claim, experiment, and
figure manifests are retrospective indexes and may not be used to rewrite the
source-locked hypothesis or endpoint.

## Bibliography policy

Only records in `../notes/CITATION_VERIFICATION.md` and
`references.bib` may be cited.  Each record was checked against a primary DOI
or author-supplied arXiv entry.  Citations provide context; none substitutes
for the theorem proved in the manuscript.

## Figure policy

- All three figures must be regenerated with
  `python paper/figures/generate_all.py` from the frozen JSON package.
- PDF and SVG are vector masters; PNG is a review rendering.
- Figure scripts must reject a failed run, a wrong candidate, or a changed
  source-lock hash.
- Fixed metadata and a fixed SVG hash salt make all nine outputs byte-for-byte
  reproducible.

## Build policy

Run `paper/build.sh`.  It fixes `SOURCE_DATE_EPOCH`, runs BibTeX, and performs
four LaTeX passes.  A valid build has no undefined citations or references, no
overfull/underfull boxes, embedded fonts, 11 letter-size pages, and the same
SHA-256 hash on a repeated build.  `paper_pre_review.pdf` is the immutable
snapshot handed to the independent manuscript reviewer;
`paper_round1_revised.pdf` is the deterministic author-revised artifact.
`paper_final.pdf` is the terminal local artifact and is byte-identical to that
independently approved revision.

## Pipeline boundary

Independent Round 1 returned `PASS_WITH_MINORS`; all three repairs were then
independently verified in Round 2, which returned `PASS — MAY FINALIZE` with no
remaining required minor.  The local paper and final integrity stages are
complete.  Repository synchronization remains deferred to the five-paper batch
close under the Session rules.
