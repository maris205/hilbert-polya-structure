# P25 Round-7 theorem — the universal q-symbol no-repeat determinant family

Date: **2026-08-28**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow: ARS Stage-1 research plus exact deterministic replay
- Typed object: `P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR`
- Freeze SHA-256:
  `41fec487b1473fe65adeaadebde769cdf065d67db7f53232e8202879a6fabddb`
- Core-output SHA-256:
  `9c3daaa1feffa23090cc4edf5c3cdf0398389f814ef4f0f6b14cad254f23d4d9`
- Target data: none

## The family

For every integer `q>=2`, let `A_q=J_q-I_q`.  The continuous-time object is
the unit-roof suspension of the q-symbol no-repeat shift.  Its clock is one
unit per symbolic step.  Primitive owners are oriented primitive cyclic words
modulo rotation; reversal remains a different owner unless it is already a
rotation.  Repetitions are positive traversal powers.

This is a family of symbolic negative controls.  It is not the physical
three-disk exterior billiard when `q=3`, because the latter uses Euclidean
flight length and physical stability data.

## Exact theorem

`[PROVED]` For every integer `q>=2`, every `n>=1`, and `u in {+1,-1}`,

```text
tr(A_q^n) = (q-1)^n + (q-1)(-1)^n,

P_n(q) = (1/n) sum_(d|n) mu(d)
         [(q-1)^(n/d) + (q-1)(-1)^(n/d)],

zeta_(q,u)(z)
 = product_p (1-u^(n_p) z^(n_p))^(-1)
 = det(I-u z A_q)^(-1)
 = 1 / [(1-(q-1)u z)(1+u z)^(q-1)].
```

Consequently,

```text
zeta_(q,-1)(z) = zeta_(q,+1)(-z).
```

The Euler products converge absolutely for `|z|<1/(q-1)`.  The displayed
rational functions then give their meromorphic continuation.

### Proof

The all-ones line is an eigenspace of `A_q` with eigenvalue `q-1`.  Its
codimension-one complement, consisting of vectors whose coordinates sum to
zero, has eigenvalue `-1`.  This proves the trace and determinant formulas.

Every closed symbolic walk is a unique positive power of a primitive oriented
cyclic owner.  Möbius inversion of

```text
tr(A_q^n) = sum_(d|n) d P_d(q)
```

gives the displayed primitive count.  Expanding the logarithm of the Euler
product separates those powers and yields

```text
log zeta_(q,u)(z) = sum_(n>=1) u^n tr(A_q^n) z^n/n,
```

which is the standard formal logarithm of `det(I-u z A_q)^(-1)`.  Replacing
`u=+1` by `u=-1` changes every occurrence of `z` to `-z` and proves the phase
substitution.  No target spectrum or arithmetic label enters any step.

## Exact finite replay

The checked artifact evaluates all `q=2,...,8` and all degrees through 12.
It contains 84 trace/count rows and 182 coefficient rows.  Direct integer
matrix powers agree with the closed trace formula on all 84 rows.  Primitive-
count Euler products, trace exponentials, and reciprocal determinant
recurrences agree coefficient by coefficient on all 182 rows, with zero
mismatches.

The cumulative primitive-owner counts through degree 12 are

```text
q=2:             1
q=3:           747
q=4:        69,706
q=5:     1,924,378
q=6:    26,039,187
q=7:   221,801,117
q=8: 1,366,778,692
```

These large values are formula evaluations, not enumerated orbit samples.
The replay uses exact integer/rational arithmetic and therefore has no
floating-point tolerance or precision drift.

## Paper-level consequence

Round 6 established exact determinant wiring for `q=3`.  Round 7 proves that
the same wiring and the same phase substitution hold for the entire
non-arithmetic family `q>=2`.  Exact primitive ownership plus an analytic
finite-dimensional determinant is therefore not arithmetic evidence: the
mechanism survives arbitrary alphabet size while A0 remains absent.

The family receives the typed tuple

```text
(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)
overall = ROUTE_A_REJECTED.
```

This is a reusable Route-A negative-control theorem.  It does not promote the
physical three-disk flow, whose tuple remains `UNASSIGNED`, and it does not
open Route B.

## Limitations and disclosure

The theorem concerns a unit roof, a finite symbolic adjacency matrix, and only
the two scalar step phases `u=+1,-1`.  It neither models the physical flight-
length roof nor establishes a Gutzwiller--Voros, multiple-scattering, quantum-
resonance, Riemann, or Dedekind divisor identity.  AI-assisted research and
code generation were used; all reported identities are accompanied by the
explicit proof above and deterministic exact-arithmetic artifacts.
