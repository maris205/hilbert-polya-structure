# Paper 42 Phase-1 preauthority package

Proposed candidate: `SD-C44` (commissioned identifier; authority allocation
remains a root-governance decision).

Working title: **Finite-Field Clocks Do Not Become Rational Primes: Exact
Factor Non-Descent for the Full Shift**.

Status: `INPUTS_FROZEN_FOR_INDEPENDENT_DA`. This directory is a portable
Phase-1 research package, not authority, not a preregistered experiment, and
not a Paper-42 repository integration. Only its final research-input bytes are
frozen before independent review.

## Outcome first

The retrospective rule in `SELECTION_AND_PROVENANCE.md`, applied to the six
immutable Session-4 cards, returns `SD-C01` uniquely. The rule and all theorem
witnesses were formulated after the card outcomes were known. It therefore
earns no prospective, outcome-independent, novelty, priority, ranking, or
authorization credit.

The source-owned positive facts remain unchanged. For the full `q`-shift,
where `q` is one of `2, 3, 5`, primitive necklaces of length `n` are counted by

\[
 N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d},
\]

the same count as monic irreducible polynomials of degree `n` over
`F_q`. With a free symbol marker `z` and clock `log q` per symbol,

\[
 Z_q(s,z)=\prod_{\gamma\in\operatorname{Prim}_q}
 \left(1-z^{|\gamma|}q^{-s|\gamma|}\right)^{-1}
 =\frac1{1-zq^{1-s}}.
\]

Paper 42 asks only whether this exact function-field factor ledger can descend
to the rational-prime Euler ledger without changing its object, clock, marker,
multiplicity, or determinant owner. Three exact witnesses answer no:

1. the primitive necklace `[01]` has clock `2 log q`; a same-clock rational
   prime image would have to equal `q^2`, which is composite;
2. length one already has `q` distinct source factors, all with weight
   `q^{-s}`, whereas the rational-prime factor at `q` has multiplicity one;
3. the marked logarithm's `z` coefficient is `q^(1-s)`, whereas the target
   coefficient is the prime zeta series `P(s)=sum_p p^{-s}`.

Thus no total source-factor map to rational primes can preserve the exact
clock, and no factorwise identification can preserve marker, weight, and
multiplicity. The source determinant remains a valid function-field dynamical
determinant; the theorem is a type/ownership closure, not a criticism of that
positive structure.

Expected strict Route tuple:

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

## Package map

- `RESEARCH_QUESTION_BRIEF.md` — bounded question and FINER assessment.
- `METHODOLOGY_BLUEPRINT.md` — exact proof and collision-audit method.
- `SELECTION_AND_PROVENANCE.md` — six-card retrospective selector.
- `SOURCE_LOCK.md` — typed source, allowed operations, and portability rules.
- `OBJECT_MARKER_OPERATOR_CONTRACT.md` — object/clock/marker/operator ownership.
- `DERIVATION_PACKAGE.md` — formula chain and projection matrix.
- `PROOF_PACKAGE.md` — complete exact proofs and quantifier notes.
- `THEOREM_FALSIFIERS.md` — independent defeat conditions.
- `EXACT_WITNESS_LEDGER.md` — finite witnesses and positive controls.
- `LITERATURE_NOVELTY_AUDIT.md` — primary-source and recent-window collision
  audit through 2026-08-17.
- `ROUTE_RECORD_CENSUS.md` — terminal-P39 and separate P40/P41 audit state.
- `ROUTE_EXPECTATION.yaml` — strict v0.2 preauthority Route expectation.
- `DA_HANDOFF.md` — independent devil's-advocate acceptance gates.
- `SOURCE_HASHES.sha256` — portable `repo:` and `dependency:` source IDs.
- `RESEARCH_LOCK.json`, `SHA256SUMS.txt` — self-excluding package seals.

## Authority boundary

The intended portable namespace is
`papers/42-function-field-clock-non-descent/preauthority` relative to the
`symbolic_dynamics` root. The staging location is not sealed. No authority
tree, mirror, Git state, root README, paper manifest, Route registry, or
candidate registry was modified. Independent DA and root governance are
mandatory before any authority write.
