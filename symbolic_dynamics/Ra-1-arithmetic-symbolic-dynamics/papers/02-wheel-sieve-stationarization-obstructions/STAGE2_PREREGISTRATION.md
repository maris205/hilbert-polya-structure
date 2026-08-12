# Stage-02 Research Gates

Date: 2026-08-12

Status: **theorem gates frozen; empirical source lock incomplete**

Primary family: **Symbolic Dynamics only**

Candidate ID: **withheld**

Route B: **locked**

## Problem anchor

Stage-01 `SD-C05` derives consecutive rational primes and \(\log p\) scale
increments from a short wheel recursion, but its level graph is acyclic.  This
stage asks whether a stationary symbolic object can be obtained without
erasing or manually replaying that arithmetic mechanism.

## Proved screening claims

### C1 — strict-extension obstruction

Any system semiconjugating **onto the frozen wheel shift** has no periodic
points, and the standard inverse-limit natural extension is empty.

Evidence: [G0 proof](G0_STRICT_EXTENSION_OBSTRUCTION.md).

### C2 — finite strong-bisimulation obstruction

The strong forward-bisimulation quotient of a finite DAG is acyclic.  Thus a
finite \(K=5,6,7\) wheel-DAG bisimulation audit can test code and partition
coarsening, but it cannot discover a quotient cycle.

### C3 — exact-clock locality obstruction

If the exact multiplier \(q_{k+1}\) is constant on quotient state classes,
its level-injective values prevent cross-level merging.  A finite alphabet
with a fixed finite-window decoder also cannot output the unbounded sequence
of exact multipliers.

Evidence for C2 and C3:
[G0B proof](G0B_BISIMULATION_AND_CLOCK_OBSTRUCTIONS.md).

The finiteness hypothesis in C2 matters: an infinite acyclic path may have a
cyclic strong-bisimulation quotient.  Such an infinite quotient still has to
pass C3 or supply a different exact clock decoder.

## Live research object

The only live branch in this stage is a new factor or observational recoding
of the **infinite** wheel path system.  It is not permitted to inherit
`SD-C05`'s A0 verdict.  The required specification is recorded in
[`OBSERVATIONAL_RECODING_SOURCE_LOCK.md`](OBSERVATIONAL_RECODING_SOURCE_LOCK.md).
It is currently incomplete, so no recoding experiment has been authorized.

## Gates

### G0 — category gate

State the direction of every map and choose exactly one category: extension,
factor, quotient, or recoding.  An extension stops at C1.  A finite strong
bisimulation stops at C2.  Calling an observational quotient a bisimulation is
a definition failure.

### G1 — infinite source-lock gate

Before code or a candidate ID, freeze all of:

1. the infinite alphabet and phase space;
2. the fixed level-blind rule and its canonical serialization/hash;
3. coding radius or a precise infinite-memory class;
4. vertex labels, edge labels, and parallel-edge multiplicity;
5. the shift-commuting map and the definition of the recoded dynamics;
6. terminal/boundary treatment for every finite approximation;
7. state or block complexity as a function of cutoff;
8. a total exact arithmetic decoder and clock decoder;
9. a path-lifting convention for recoded closed words.

At G1, set `determinant_convention: not_defined` and
`A2: A2_NOT_TESTABLE`.  A determinant is neither selected nor computed here.
If any item is missing, the branch is `NOT_TESTABLE`.

### G2 — arithmetic-fidelity gate

The new grammar must itself recover consecutive multipliers, exact unit
residues, and \(\tau=\log q\).  Recovery is checked on **all** source paths in
the declared domain, not only on a selected orbit.  A clock decoder that uses
a stored prime table, a level-specific rule, or the experimental cutoff fails
A0.

### G3 — periodic-orbit gate

For a frozen recoded system \((Y,S)\), distinguish:

- simple graph cycles;
- periodic points of the edge or vertex shift actually chosen in G1;
- closed words that lift to compatible source paths;
- closed words manufactured by concatenating incompatible representatives.

The finite audit uses the preregistered period cutoff \(N=12\).  It reports
\(\#\operatorname{Fix}(S^n)\) and Möbius-inverted primitive counts for every
\(1\le n\le N\), with orientations, multiplicities, decoded clocks, and one
shortest witness per nonzero period.  It does not claim a complete infinite
orbit ledger.  A1 credit requires a separate completeness theorem for the
infinite object.

### G4 — control and cutoff-consistency gate

Run, without selecting a best cutoff or seed:

1. finite strong-bisimulation regression on canonical \(K=5,6,7\) DAGs;
2. the source-locked observational recoding at the same cutoffs;
3. its clock-erased version;
4. matched fixed- and cyclic-deletion variants;
5. matched random-deletion variants with seeds `20260812`–`20260816`;
6. an acyclic hand graph and a cyclic stationary toy.

Label erasure may coarsen a partition and may increase the cycle count.  A
control cycle is not automatically a failure.  The comparison signature is:

```text
exact unit-set recovery
+ zero arithmetic-decoder violations
+ zero clock-decoder violations
+ period counts through N=12
+ decoded edge-label witness
+ frozen recoding-rule hash
```

Finite cutoff consistency must be defined by G1, including the terminal
marker and interior region.  Similar-looking \(K=5,6,7\) tables are not a
substitute for an infinite consistency theorem.

### G5 — determinant gate

Only after G1–G4 and an infinite A0/A1 ledger pass may a new `SD-C07` source
lock freeze an Artin–Mazur or Fredholm convention.  Until then A2 remains
`NOT_TESTABLE` and Route B remains locked.

## Mechanical outcome rules

Apply these rules in order.

1. **INVALID / NOT_TESTABLE:** code sanity fails; the category, equivalence,
   labels, decoder, cutoff consistency, or rule hash is undefined; a frozen
   rule is changed after seeing results; a required control/artifact is
   missing.
2. **THEOREM_STOP:** the proposal is a strict extension, a finite strong
   bisimulation expected to create cycles, a state-class exact-\(q\) quotient,
   or a finite-alphabet fixed-window exact-clock decoder.
3. **STOP_SCOPED:** the fully specified observational recoding has no periodic
   witness through \(N=12\), has any arithmetic/clock decoder violation, or
   its periodic words fail the declared path-compatibility test, or a matched
   non-arithmetic control reproduces the entire frozen joint signature.  This
   stops only that frozen recoding and cutoff claim.
4. **FINITE_ESCALATE:** one unchanged rule has zero decoder violations, a
   nonzero compatible periodic witness, the complete joint signature at every
   cutoff, all controls, and no matched non-arithmetic control with the same
   joint signature.  This authorizes an infinite source-lock theorem attempt;
   it does not establish A0, A1, `SD-C07`, or a determinant.

These outcomes are mutually exclusive by priority.  There is no positive
empirical GO rule before G1 is complete.

## Forbidden constructions and data

- prime tables or Riemann-zero tables;
- prime-indexed components;
- reset, wrap, or manually inserted \(k\to0\) edges;
- hand-assigned \(\log p\) roofs;
- hard-coding \((q_k)\) or \((Q_k)\) in an alphabet, transition table, or
  forbidden list;
- a universal computation tape whose purpose is to replay those sequences;
- borrowing the `SD-C04` determinant or `SD-C06` zeta quotient;
- inheriting A0 after forgetting the clock;
- expanding the existing cross-family `RC-03` clue;
- Route B.
