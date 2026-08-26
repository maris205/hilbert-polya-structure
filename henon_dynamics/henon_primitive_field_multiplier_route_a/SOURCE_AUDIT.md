# C172 source audit

- Candidate: `HCS-C172`.
- Frozen source commit: `ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f`.
- Evaluation date: 2026-08-26.
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
- Object: \(T_a(x)=ax\) on an arbitrary finite field \(\mathbb F_Q\), where
  \(Q\geq2\) is a prime power and \(a\) is any primitive element.
- One multiplication is one clock tick.  Fixed points use counting measure;
  the Koopman space uses normalized counting measure.
- Determinants are separated: the Artin--Mazur zeta is defined from
  \(\#\operatorname{Fix}(T_a^n)\), while \(\det(I-zU_a)\) is the finite
  Koopman determinant.
- Registered bibliography/citation population: zero.  No novelty or priority
  claim is made.

## Arithmetic gate

Prime-power cardinality and finite-field multiplication are intrinsic, so the
source has a weak arithmetic relation.  It does not produce a dictionary from
rational primes to primitive orbits, a \(\log p\) clock, von Mangoldt weights,
or target local data.  A composite cyclic surrogate and any random permutation
with the same cycle type have identical zeta and Koopman spectra.  The verdict
is therefore only `A0_WEAK_ARITHMETIC_RELATION`.

## Integrity boundary

The proof covers every prime power and every primitive generator.  Eighteen
small prime-power ledgers are regression sentinels only.  No global Euler
product, local factor, root number, automorphy, target divisor or functional
equation, Hilbert--Pólya construction, or Route-B authorization is inferred.

## Stage 2.5 pre-computation integrity audit

1. **Implementation bug — N/A at design time.** No result had yet been
   accepted; independent cyclic enumeration and symbolic permutation matrices
   were mandatory before release.
2. **Hallucinated citation — CLEAR.** The citation population was frozen at
   zero, with no novelty or priority claim.
3. **Hallucinated experimental result — CLEAR.** Planned exact sentinels were
   not represented as already-run experiments.
4. **Shortcut reliance — CLEAR.** The exponent-coordinate proof for every
   prime power was required; a finite field list could not establish it.
5. **Bug-as-insight — N/A at design time.** No anomalous output existed, and
   independent reconstruction was a hard gate for later interpretation.
6. **Methodology fabrication — CLEAR.** The source object, clock, two
   determinant conventions, controls, cutoffs and commands were frozen first.
7. **Frame-lock — CLEAR.** The plan required composite cyclic, nonprimitive
   and same-cycle controls and allowed rejection or downgrade at A0.

## Stage 4.5 post-result integrity audit

1. **Implementation bug — CLEAR.** Independent cycle enumeration, SymPy
   matrices, byte replay and semantic mutation attacks reproduce the result.
2. **Hallucinated citation — CLEAR.** The released citation population remains
   exactly zero.
3. **Hallucinated experimental result — CLEAR.** All counts and hashes are
   traceable to stored deterministic outputs; no statistical trial is claimed.
4. **Shortcut reliance — CLEAR.** Finite ledgers remain sentinels and the
   primitive-coordinate proof carries the all-\(Q\) theorem.
5. **Bug-as-insight — CLEAR.** Independent reconstructions agree and corrupted
   semantics are rejected rather than promoted.
6. **Methodology fabrication — CLEAR.** Released methods, commands, cutoffs,
   field list and determinant conventions match the frozen protocol.
7. **Frame-lock — CLEAR.** Same-cycle controls demonstrate genericity and force
   the qualified `A0_WEAK_ARITHMETIC_RELATION` verdict rather than an arithmetic
   promotion.
