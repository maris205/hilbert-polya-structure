# Integrity Pre-Review

Date: 2026-08-13  
Candidate: `pcf_quadratic_prime_multiplier_obstruction_v1`  
Verdict: **PASS TO INDEPENDENT REVIEW**

This audit is a fail-closed pre-review check, not an independent scientific
review. The source lock remains the contemporaneous commitment; the three JSON
registries beside this file are retrospective traceability indexes.

## Frozen snapshot

- Source lock: `aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842`
- Manuscript source: `332a5426b79e314710efda44ffbfacd95c6b7bc2ba7e0eb44632edadbe158c21`
- Pre-review PDF: `e3279ccc6096a89f90c580e1ef8412440637bd1b84f7c1039b011442915e4c34`
- Bibliography: `b09a06c3eaf6f9bc700fdb6032cd8260f4c2a50d8b0bef8b8672b40f934e2979`
- Final result manifest status: `VERIFIED`; 37 tests, zero failures,
  errors, or skips.

## Seven-mode audit

1. **Claim/evidence alignment — PASS.** The all-period conclusion is linked
   only to the integrality/divisibility proof. Periods one through four are
   labeled an implementation audit and never promoted to an all-period
   empirical inference. `CLAIM_MANIFEST.json` records the open base-2 and
   complex-modulus boundaries.
2. **Experiment provenance — PASS.** The exact period cutoff and controls were
   frozen before candidate execution. `EXPERIMENT_PASSPORT.json` maps every
   reported computation to a raw JSON artifact. The command manifest records
   zero numerical candidate runs and no conditional high-period real-orbit
   ledger.
3. **Forbidden-data boundary — PASS.** The source-lock scan, command manifest,
   and final result manifest all state that no external rational-prime table or
   Riemann-zero data were accessed. No prime or zero fit is present.
4. **Citation integrity — PASS.** All 15 bibliography entries have a DOI,
   arXiv, publisher, or official metadata trail in
   `notes/CITATION_VERIFICATION.md`. Every manuscript citation is used within
   its recorded safe-claim boundary. No cited source is used to claim the
   elementary theorem as a priority result.
5. **Genealogy/originality — PASS WITH SCOPE NOTE.** The shared Logistic
   parameter and arithmetic motivation are explicitly attributed to Wang
   (2026). The manuscript states that the earlier prime-sieve claims and data
   are neither imported nor revalidated. No text reuse claim is made, and the
   new object is the autonomous exact multiplier certificate.
6. **Figure/data traceability — PASS.** Every figure has one definition and at
   least one substantive `Figure~\ref` link. `FIGURE_PACKAGE.json` records
   source data, transformations, output hashes, and limitations. All three PNG
   review copies were visually inspected; no collision or illegible panel was
   found. Figure 3 is fixed after the proof so it no longer interrupts the
   proposition.
7. **Build and presentation — PASS.** The sequence
   `pdflatex -> bibtex -> pdflatex -> pdflatex` produces an 11-page PDF with
   populated title, author, subject, and keyword metadata; embedded vector
   figures; no undefined citation/reference; and no overfull/underfull box or
   LaTeX warning in the final log.

## Mandatory interpretation boundaries

- The theorem requires the multiplier itself to be rational; it does not rule
  out a nonrational complex multiplier whose modulus happens to be a rational
  prime.
- The target `|lambda|=2^n` is open for periods at least two. More finite-period
  enumeration cannot close this all-period question.
- The cotangent construction is exact only on each regular branch. It is
  singular at `q=0`, noncompact, has overlapping branch images, and is not a
  global symplectomorphism.
- The paper opens no cycle-determinant, Riemann-zero, quantization, or Route-B
  claim.

The package is cleared for two independent manuscript-review rounds. Any
revision must preserve the pre-review PDF as a historical snapshot and update
the current registries and final hashes.
