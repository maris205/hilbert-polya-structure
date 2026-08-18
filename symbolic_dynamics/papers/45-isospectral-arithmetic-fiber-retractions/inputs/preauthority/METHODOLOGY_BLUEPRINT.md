# Methodology blueprint

## Workflow contract

This package applies the proof-writer and experiment-plan disciplines in
that order:

1. freeze objects, quantifiers, domains, and ownership before calculation;
2. separate the algebraic basis prescription from bounded operator
   existence;
3. give a theorem status, assumptions, dependency map, detailed proof, and
   sharp endpoint witnesses;
4. reduce the scientific program to at most two primary claims;
5. attach each claim to an evidence block, decisive failure criterion, and
   independent evaluator;
6. preregister mutations before any implementation or result;
7. keep all output and authority work outside this stage.

These disciplines determine structure and auditability. They are not
scientific sources and receive no novelty credit.

## Two primary claims

### Claim C1: common cyclic ledger, different exact operator geometry

For every \(h\ge2\), the saturated and modulo retractions have the stated
distinct bounded domains, the same simple nonzero eigenvalues and legal
power traces, exact power-Schatten walls, and different normal-similarity
domains. In particular, throughout

\[
1/h<\sigma\le1,
\]

\(M_{h,s}\) is boundedly similar to normal while \(S_{h,s}\) is not, despite
their common legal determinant ledger.

### Claim C2: arithmetic distortion laws beyond the shared method

The saturated Riesz norms have the exact primorial optimizer and
three-regime maximal order; the two singular sequences have the explicit
Weyl constants \(C_{h,\sigma}\) and \(D_{h,\sigma}\), with
\(C_{h,1}=D_{h,1}=1\); and the self-commutators have the strict wall
\(\sigma q=1\), including the separate \(h=2\) necessity proof and Euler
control.

No third primary claim is permitted. The free-UFD clone and determinant
equality are controls.

## Claim-to-evidence map

| Claim | Proof evidence | Later evaluator evidence | Decisive failure |
|---|---|---|---|
| C1 | Lemmas 1--2 and Propositions 3--6 | direct finite fiber matrices plus independent exponent/Euler derivation | any domain, spectrum, trace, power, projection, or iff mismatch |
| C2 | Propositions 7--12 | exhaustive primorial checks, independent local products/counts, commutator spectra, endpoint mutations | wrong coefficient, strip, residue, crossover, or strict commutator wall |

Finite computations test implementations and exact local identities. They
do not replace the infinite proofs.

## Evidence labels

- PROVED: a complete derivation is in PROOF_PACKAGE.md.
- KNOWN_TOOL: standard theorem used with hypotheses stated.
- KNOWN_PRIMARY_SOURCE: externally owned context or method.
- INTERNAL_PREDECESSOR: Papers 27--30/P43 ownership to subtract.
- PREREGISTERED_WITNESS: exact target fixed before evaluation.
- PLANNED_EVALUATION: no output exists in this package.
- STOP_DUPLICATE: exact prior art absorbs the residual claim.
- STOP_GENERIC_SPECIALIZATION: only the \(h=2\) radical case remains.
- HOLD: a repairable source, proof, independence, or integrity gap.

## Five-stage proof architecture

1. Fiber stage: derive both preimages directly from prime exponents.
2. Operator stage: obtain block masses, domains, compactness, powers,
   ideals, spectrum, traces, and determinant legality.
3. Geometry stage: compute Riesz norms, prove uniform-projection similarity
   iff, and solve the exact primorial optimization.
4. Asymptotic stage: prove the generalized Dirichlet factorization,
   holomorphic strip, residue, positivity, Tauberian count, modulo count, and
   crossover.
5. Nonnormality stage: compute rank-one self-commutators, prove strict
   ideals, isolate the \(h=2\) witness, and apply the free-UFD firewall.

Each stage has a falsifier in THEOREM_FALSIFIERS.md.

## Two genuinely independent evaluator designs

### Evaluator A: map-to-matrix route

Evaluator A receives only the raw definitions of \(\tau_h\),
\(\omega_h\), the coefficient \(n^{-s/2}\), and a schema for its final
projection. It:

- factors integers by trial division;
- constructs fibers by enumerating \(n\) and applying the maps;
- constructs finite block matrices directly;
- obtains singular values, eigenvalues, powers, Riesz idempotents, and
  commutators from matrix operations;
- searches all \(h\)-free \(m\le x\) before comparing the maximizing label
  with a primorial;
- emits finite-compression diagnostics only. It is forbidden to emit an
  infinite boundedness, ideal, similarity, trace/determinant-domain, or
  Tauberian verdict from nested truncations.

It must not import the closed fiber formulas, Euler factors, Tauberian
residue, or Evaluator B's code or output.

### Evaluator B: exponent-to-Euler route

Evaluator B receives the same immutable raw definitions and final projection
schema, but no matrices, enumerated fibers, or Evaluator A artifact. It:

- derives local exponent states symbolically;
- forms Euler factors for block masses, powers, traces, and commutators;
- checks leading prime terms and strict convergence walls;
- expands \((1-p^{-z})L_p(z)\) and derives the Tauberian strip and residue;
- obtains Weyl constants from independent counting formulas;
- derives the primorial asymptotics from \(\vartheta(y)\), Mertens, and
  prime sums;
- builds the formal free-UFD clone by atom relabeling.

It must not import production helpers, fixtures, intermediate data, expected
tables, or output from Evaluator A.

### Independence boundary

The evaluators may share only:

- the byte-frozen EXPERIMENT_CONTRACT.json, including its neutral case IDs
  and raw input values;
- the byte-frozen MUTATION_REGISTRY.json;
- the strict EXPERIMENT_CONTRACT_SCHEMA.json and
  MUTATION_REGISTRY_SCHEMA.json, which supply the required output field
  names and exact data types;
- public library/runtime declarations;
- a comparator that reads only sealed final projections.

They must independently parse and expand every registered case. They may not
share source modules, generated expansions, seeds, fixtures, serialized
intermediates, expected values, tolerance-selection code, or postprocessing.
Each implementation must be authored and sealed independently before either
output is exposed.

## Canonical comparison contract

The final Draft-2020-12 schema has three explicit namespaces and rejects
unknown fields in every output, interval, hash-bearing record, mutation
outcome, and structured error.

Common exact fields, which both evaluators derive independently, include:

- finite case identifiers from the frozen neutral registry;
- map values and fiber membership on the semantic overlap;
- \(h\)-free and \(J_h(m)\) types;
- finite-block eigenvalue, power, rank, projection, and commutator
  invariants;
- primorial maximizing labels for shared finite exact cutoffs;
- mutation identifiers and rejection codes.

Evaluator-A-only fields retain raw matrix dimensions, enumeration
certificates, and direct finite spectra. Evaluator-B-only fields retain the
symbolic infinite trace, Euler factors, Tauberian strip and residue, and
closed asymptotic constants. Every infinite theorem certificate is consumed
by Evaluator B and an independent proof auditor, never by Evaluator A or the
finite comparator. These method-specific fields are required and schema
checked, but are not falsely declared byte-comparable to a quantity the
other route does not compute.

Common numerical fields include independently produced certified intervals
for finite singular values, projection norms, and overlapping partial
counts. The comparison tolerance and precision ladder are frozen before
execution. Common exact fields must be byte-identical; common numerical
intervals must overlap and have widths at most \(10^{-30},10^{-60},10^{-120}\)
at 128, 256, and 512 bits. Method
identities, exclusive fields, and internal check ledgers remain distinct.

The exact finite eigenvalue is not a rational complex pair. Both routes emit
the same strict `DIRICHLET_POWER` envelope. Base, numerator, and denominator
are canonical integer strings, so JSON numbers such as `6.0`, `6e0`, or
`1.0`, Booleans, plus signs, leading zeros, and `-0` cannot exploit JSON
Schema's mathematical-integer convention. The reduced real/imaginary
exponent uses `REAL_LOG_POSITIVE_BASE`. Each envelope stores the exact
RFC8785 JCS UTF-8 string and its recomputed SHA-256. A certified complex
rectangle may accompany it but cannot replace the symbolic AST.

Raw parsing is token based until duplicate-member detection completes at
every nesting depth; no last-win object is ever constructed. Unique members
may arrive in any order and must canonicalize to identical JCS bytes/hash.
Only a mismatch in stored canonical bytes/hash is rejected as
`NONCANONICAL_AST_STORAGE`.

Infinite coverage is a separate executable namespace. A has empty
`infinite_case_ids` and `infinite_records`; B has exactly the C-sorted 15
frozen IDs and one owner-B certificate per ID; P has the same IDs and one
owner-P audit per ID. The driver recomputes the frozen LF-joined set hash
and requires exact B-to-P equality of certificate payload, proof-dependency,
and analytic-derivation hashes. Overall P PASS is equivalent to all 15
per-case PASS verdicts.

## Mutation architecture

MUTATION_REGISTRY.json is the controlling, atomic registry. Every row fixes
a stable ID, exact target artifact, semantic domain, the complete
designated-consumer key set, exact rejection code, and required nonzero
exit. A JSON mutation supplies a resolvable RFC6901 pointer plus exact
`value_from` and `value_to`; a filesystem mutation selects one
of the closed typed operations. The runner uses a fresh disposable copy and
checks the exact pre-mutation JSON type/value or typed precondition before
performing any operation.
The only legal outcome union is the one in EXPERIMENT_CONTRACT.json:
ACCEPT, REJECT, or HARNESS_ERROR. A mutation is killed only when every and
only its designated consumers return REJECT with the row's exact code and
exit 2. A crash, exception, timeout, malformed payload, missing/extra or
duplicate consumer, ACCEPT, zero exit, or wrong code is a survivor and
places the run on HOLD.

Eight mutation families are mandatory:

- type: invalid \(h,k,q,m\), swapped map, wrong \(J_h\), complex
  \(s/\sigma\) confusion, finite/infinite fiber confusion;
- endpoint: every strict wall, the \(M\) existence condition, trace and
  determinant boundaries, \(\sigma=1\) similarity split, and
  \(C_{h,1}=D_{h,1}=1\);
- source: changed hash/DOI, old universal constant inequality, omitted
  P27--P30/P43 subtraction, generic method claimed as novelty;
- firewall: shared expected table, free-UFD clone counted positively,
  \(h=2\)-only paper admission, or Route expectation treated as outcome;
- semantic type: singular-value/eigenvalue confusion or projection norm
  treated as a probability;
- symbolic AST: rational-complex eigenvalue substitution or a non-real-log
  branch;
- infinite coverage: missing, extra, reordered, undeclared, wrong-owner,
  nonempty-A, or wrong-set-hash payloads;
- raw serialization: JSON-number/Boolean scalar confusion, duplicate-member
  last-win, false rejection of reordered unique keys, or trusted
  noncanonical JCS/hash storage.

The prose families above summarize the registry and do not create additional
unregistered mutations. Positive relocation and hygiene controls are
recorded separately and are not counted as mutation rejections.

## Delete-shared-method protocol

Before a paper-sized decision, remove:

- generic weighted composition and rank-one fiber algebra;
- generic Riesz/Gram/Schatten facts;
- all regularized-determinant mechanism;
- P27--P30/P43 owned lessons;
- the free-UFD construction itself;
- classical PNT, Mertens, Tauberian, and \(h\)-free density statements.

The remaining principal result must still contain the paired all-\(h\)
classification, exact maximal-order coefficient, two Weyl constants and
crossover, and the commutator law. If not, stop.

## Source and governance protocol

All external and internal owners are named in
LITERATURE_NOVELTY_AUDIT.md. An exact primary collision triggers
STOP_DUPLICATE. Search absence never becomes priority evidence.

GO/HOLD/STOP tokens are external scientific or publication dispositions.
They are not Route terminal codes. Only the strict Route validators own the
A0--A4 tuple, overall Route expectation, and Route-B fields.

This stage is read-only with respect to the authority repository and writes
only the requested /tmp package. No implementation run, result ledger,
Route evaluation, registry edit, mirror synchronization, or Git operation
is included.
