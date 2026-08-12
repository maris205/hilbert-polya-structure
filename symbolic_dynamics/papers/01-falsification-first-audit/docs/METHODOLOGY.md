# Session-4 Methodology

## Scope rule

The primary family is symbolic dynamics.  Every candidate fixes one grammar,
clock, potential/cocycle, function space, and determinant convention.  Evidence
from different candidates is never assembled coordinatewise.  An implication
that requires a modular surface, quantum graph, Hamiltonian flow, independent
operator algebra, or other system family is written only to
[ROUND2_CLUES.md](../ROUND2_CLUES.md).

## Research sequence

1. Read the proposal and both evaluator specifications.
2. Audit the supplied prior work claim by claim.
3. Search primary literature by the obligation it can support:
   finite/sofic periodic zeta, countable thermodynamic formalism, renewal
   universality, arithmetic subshifts, Gauss/Farey transfer operators, and
   number-theoretical spin chains.
4. Freeze object definitions, forbidden data, cutoffs, precision, and controls.
5. Derive exact identities and no-go theorems before interpreting numerics.
6. Run finite experiments only as certificates, cutoff diagnostics, or
   adversarial controls.
7. Apply Route A separately to every frozen object.
8. Invoke Route B only if the same object reaches A4_ROUTE_B_READY.

## Literature protocol

Searches used title/author queries and obligation-focused query clusters such
as:

- “subshift finite type zeta determinant”;
- “countable Markov shift renewal zeta complex weight”;
- “Gauss map nuclear transfer operator Fredholm determinant”;
- “squarefree B-free symbolic dynamics”;
- “number theoretical spin chain Riemann zeroes”;
- “finite group extension shift periodic data determinant.”

Technical claims were checked against original papers, official author or
institute manuscripts, publisher records, or official mathematical reference
pages.  Secondary search snippets were discovery aids only.  The search is not
a theorem of nonexistence; the reported literature gap is labelled OPEN.

## Data separation

No Riemann-zero table is loaded anywhere in the experiment code.  The global
Riemann–von Mangoldt asymptotic is used only as a theorem-level growth
benchmark.  Rational primes appear only where the mathematical object itself
defines them (squarefree exclusions), generates them (wheel recursion), or
where an independent arithmetic check is explicitly labelled as validation.

Seeds and cutoffs are frozen in
[SESSION4_PREREGISTRATION.md](../SESSION4_PREREGISTRATION.md) and the
candidate-specific frozen-config files.  All seed ledgers are reported; no
best-seed selection is performed.

## Evidence discipline

- Algebraic identities and exhaustive integer checks may be PROVED or
  NUMERICALLY_CERTIFIED according to their mathematical scope.
- Floating-point truncations remain NUMERICAL_OBSERVATION.
- A finite truncation never establishes meromorphic continuation.
- Exact reconstruction of unrelated analytic controls is a PROVES_TOO_MUCH
  failure.
- Natural arithmetic in one object cannot repair the determinant of another.
- Failure at A0 or A1 blocks Route B, regardless of later formal similarity.

## Reproducibility standard

Every experiment records:

- source object and determinant convention;
- cutoffs and precision;
- complete seeds;
- exact versus floating fields;
- negative controls;
- machine-readable results;
- a claim boundary;
- the Route-B lock.

The final verification commands, seed ledgers, and result paths are collected
in [`EXPERIMENT_REPORT.md`](../EXPERIMENT_REPORT.md); repository artifact
checksums are stored in `PAPER_MANIFEST.sha256` at the Paper-01 project root.
