# A4.14 manuscript-integration review

Review date: 2026-08-06 UTC  
Mode: independent secondary-agent, read-only, release-blocking review  
Disposition: **ACCEPT**

## Scope checked

The review cross-checked the A4.14 certificate, S0 summary, manifest,
independent checker, postcheck, release provenance, programme and manuscript
claim ledgers, Appendix G, Section 8, conclusion, README/roadmap/decision
records, and the rebuilt PDF.  It did not modify any file.

## Findings

- Every layer binds exactly `S000`, `S025`, and `S050` at 128 and 256 MPFR
  bits: six trees, 3,016 evaluated nodes, and 1,532 leaves comprising 183
  energy exclusions plus 1,349 return exclusions.
- The independent checker records 89,962 exact-decimal checks and zero
  failures.  The milestone is `PASS_IMPLEMENTATION_SMOKE` and
  `final_status` remains null.
- All 6,055 producer-manifest file hashes replayed with zero failures.  The
  four-release read-only audit also passed; the S0 release binds 18 objects.
- The A4.14 certificate hash is
  `f87b701de17d7fca12c0fcfbd4d24496107d34c3f2c21ea3e15d5cdec49855b2`;
  the release-provenance hash is
  `5b7397bac1d577014551e6c03f708b1a729146b8cbe306f3756fafdbfedd5ad0`;
  and the release-bound evaluator hash is
  `b768de84247cd847a3c1b518ec08a7bcfc766e31c20c01bcdd0c75b06d319d53`.
- The complete Paper 02 suite passed 95 tests.  A clean four-pass LaTeX build
  produced 31 pages with no undefined citation, reference, or build error;
  the only overfull box was a nonmaterial 1.548 pt bibliography line.
- No manuscript or programme record promotes the three-slab smoke to the
  other 48 slabs, a phase/global cover, the quantitative trace domain, a
  prime/zeta correspondence, Hilbert--Polya, or RH.

## Non-blocking historical note

`research/programme_snapshot/CLAIM_LEDGER.md` predates A4.14 and uses the
then-current phrase “74 current regression tests.”  A separate snapshot
status marker now makes that frozen-as-of boundary explicit; the file is not
part of the current claim authority.

