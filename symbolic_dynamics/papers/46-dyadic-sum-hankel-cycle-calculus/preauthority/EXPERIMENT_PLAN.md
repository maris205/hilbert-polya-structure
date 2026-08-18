# Claim-Driven Experiment Plan — Paper 46

## Status

PREAUTHORITY PLAN / NO RESULTS / NO IMPLEMENTATION AUTHORITY

## Frozen scientific questions

| Claim | Question | Evidence type |
|---|---|---|
| C1 | Does the support predicate equal the dyadic anti-diagonal enumerator? | exact finite exhaustive agreement |
| C2 | Does every edge preserve \(v_2\), including loops? | exact all-edge agreement |
| C3 | Are the sharp walls \(0,1/2,1\) represented by the proved divergent and summable certificates? | symbolic formula plus exact partial sums |
| C4 | Does the cutoff matrix split into scaled odd blocks exactly? | exact permutation/block equality |
| C5 | Does the cyclic solver return exactly the direct walk-enumerator solutions? | exhaustive label-tuple agreement |
| C6 | Do finite trace powers obey the exact scale-dependent truncated-block sum, while the proof-backed infinite trace obeys the geometric factor? | exact finite equality plus separately typed infinite identity |
| C7 | Are ordinary versus regularized determinant domains kept distinct? | typed domain audit |
| C8 | Do all hostile mutations hit the designated semantic class? | exact mutation outcomes |

## Frozen grids

### Structural grid

- cutoffs \(N\in\{8,16,32,64\}\);
- valuation blocks \(0\le k\le5\);
- exact support and loop enumeration over every ordered pair \(1\le m,n\le N\).

### Cycle grid

- lengths \(1\le r\le7\);
- ordered labels \(q_i\in\{2,4,8,16,32,64\}\);
- direct vertex bound \(1\le n_i\le64\);
- all tuples are evaluated, not sampled;
- primitive reduction is recorded separately from based-walk equality.

### Analytic grid

- \(\sigma\in\{0,1/4,1/2,3/4,1,5/4,2\}\);
- anti-diagonal levels \(1\le a\le16\);
- matching scales \(Q_j=4^j\), \(1\le j\le8\);
- exact rational arithmetic whenever exponents permit it;
- otherwise 160-bit interval arithmetic with the interval and rounding mode
  serialized.

### Trace grid

- \(s\in\{2,4\}\) for exact rational matrix traces;
- powers \(1\le r\le6\), with \(r=1\) used only in the trace-class domain;
- cutoffs \(N\in\{8,16,32\}\);
- separate cutoff-only complex controls \(s=2+i\) and \(s=3/4+i\).

If \(A_s^{(M)}\) is the odd block restricted to odd \(u\le M\), the exact
finite identity tested at cutoff \(N\) is

$$
\operatorname{Tr}\!\left((P_NH_sP_N)^r\right)
=\sum_{0\le k\le\lfloor\log_2N\rfloor}
2^{-krs}
\operatorname{Tr}\!\left(
(A_s^{(\lfloor N/2^k\rfloor)})^r
\right).
$$

The truncation changes with \(k\); this sum is not collapsed to a finite
geometric factor. The infinite identity

$$
\operatorname{Tr}(H_s^r)
=\frac{\operatorname{Tr}(A_s^r)}{1-2^{-rs}}
$$

is a separately typed, proof-backed statement in the legal domain.

## Independent evaluators

### Evaluator M

Builds the cutoff matrix from the bit predicate:

    x=m+n; x>=2 and x&(x-1)==0.

It directly enumerates walks, exact traces, support, loops, and cutoff
singular values. It does not call the cyclic solver or anti-diagonal
enumerator.

### Evaluator C

Builds support as the union of lists:

    (m, 2^a-m), 1<=m<2^a.

It then uses valuation blocks and the algebraic odd/even solver. It does not
construct the matrix used by Evaluator M and does not import its walk code.

## Canonical evidence objects

1. source packet and schema;
2. support and valuation certificate;
3. endpoint certificate;
4. cycle-solver certificate;
5. exact trace certificate;
6. determinant-domain certificate;
7. main evaluation;
8. independent evaluation;
9. adversarial mutation results;
10. reproducibility, transaction, and cold-relocation certificates;
11. result ledger;
12. mechanically rendered experiment report.

No output path or byte count is frozen until the integration blueprint is
separately audited.

## Mutation families

### Packet and source

- missing/extra/reordered keys;
- duplicate top-level and nested keys;
- bool/int/float substitutions;
- support, loop, branch, clock, marker, and cutoff changes;
- source-lock and parent-seal drift.

### Scientific semantics

- every F01–F14 falsifier;
- odd formula sign and factor changes;
- even compatibility deletion;
- positivity and odd-parity deletion;
- endpoint strictness changes;
- trace and determinant domain widening;
- matrix/cycle projection missing, extra, reordered, or type-changed fields.

### Results and integrity

- output delete, rename, extra, unsafe path, and symlink replacement;
- coordinated result edit plus recomputed ledger;
- report-only false claim plus canonical re-render attempt;
- evaluator check add/delete/rename;
- mutation registry omission;
- audit self-tamper;
- cache, auxiliary, host-path, and binary/text classification violations.

### Route and provenance

- every tuple field;
- Route-B booleans and reason;
- pending/actual commit state combinations;
- State-A manifest presence;
- State-B missing, malformed, unequal, or stale provenance;
- literature STOP_DUPLICATE kept external to Route terminals.

## Falsifier consumer matrix

| Falsifier | Designated consumers |
|---|---|
| F01 support replacement | Evaluator M and Evaluator C |
| F02 loop deletion | Evaluator M and Evaluator C |
| F03 inserted illegal edge | Evaluator M and Evaluator C |
| F04 boundedness at \(\sigma=0\) | Evaluator C endpoint lane and proof auditor |
| F05 \(S_2\) at \(\sigma=1/2\) | Evaluator C endpoint lane and proof auditor |
| F06 \(S_1\) at \(\sigma=1\) | Evaluator C endpoint lane and proof auditor |
| F07 odd-cycle factor deletion | Evaluator M direct walks and Evaluator C solver |
| F08 false even compatibility | Evaluator M direct walks and Evaluator C solver |
| F09 ordinary determinant in the \(S_2\)-only strip | typed read-only auditor |
| F10 nonreal Hermitian claim | typed read-only auditor |
| F11 edge labels retyped as primitives | typed read-only auditor |
| F12 cutoff used as endpoint proof | proof auditor |
| F13 marker/valuation-weight exchange | typed read-only auditor |
| F14 rational-prime selector claim | both strict Route validators |

The two science evaluators are not required to reject mutations outside their
owned lane. Consumer keys and outcomes must equal this matrix exactly.

## Acceptance rules

- exact support mismatch count: zero;
- exact cycle-solution mismatch count: zero;
- exact trace mismatch count: zero;
- theorem-failure count: zero;
- mutation survivors: zero;
- every negative is rejected by every consumer designated for its semantic
  class, with no missing or extra consumer keys;
- all positive controls pass with exact state names;
- first materialization installs only the declared output set;
- internal and external second runs perform zero physical replacements;
- forced late failure changes no target byte or metadata;
- cache, symlink, unsafe path, auxiliary, and host-token counts: zero.

## Interpretation

Passing results corroborate the implementation of a theorem proved
independently. They do not prove external novelty, rational-prime emergence,
or any Route-A target claim.
