# C156 exact-validation plan

## Claims under test

1. Prove the odd/even Fibonacci--Lucas factorizations of `A^n-I` and their
   Smith types for every `n`.
2. Separate the canonical correction `q_(A^n)` from the actual iterate
   cocycle `q_n=q_(A^n)+ell_n`; prove that `ell_n` is integer linear.
3. Prove `h_n rho_n` integral by an all-iterate parity lemma, without using a
   finite prefix as the proof.
4. Prove that the polarization is bilinear, distinct primary components are
   orthogonal, and the global zero count is the product of primary zero
   counts.
5. Enumerate every primary component exactly through `n=14` and preserve
   finite sharpness only as an observation.

## Independent paths

- Producer: fast matrix powers, coefficient accumulation, CRT idempotents,
  HNF reduction, and exact rational local histograms.
- Checker: iterative powers, five-point recovery of the cocycle polynomial,
  direct numerator cocycle iteration, and independent local enumeration.
- SymPy: Smith/Hermite forms, symbolic cocycle polarization, correct rotation
  polarization, primary histograms through `n=10`, and the parity-state proof.
- Replay: byte identity from a fresh output path.
- Mutation: repaired-hash semantic attacks plus a stale-hash control.

## Release gates

Two genuine internal theorem/scope reviews, round-preserved PDFs, LuaLaTeX
fixed-epoch double builds, embedded fonts, clean logs, visual inspection, and
an exact 27-payload manifest closure are mandatory.
