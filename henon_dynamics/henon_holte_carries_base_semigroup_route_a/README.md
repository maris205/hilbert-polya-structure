# HCS-C194: Holte carries base-semigroup Route-A package

This package freezes the carries process obtained by adding `n` independent
base-`b` digit columns.  For every `n>=1` and `b>=2`, it source-locks Holte's
transition matrix, the identity `P_a P_b=P_ab`, the base-independent
diagonalization with eigenvalues `1,b^-1,...,b^{-(n-1)}`, and the Eulerian
stationary law.  Trace, determinant, power and convergence formulas are exact
corollaries.  The all-parameter theorem is classical; the finite census is only
an executable regression certificate.

The frozen Route-A tuple is

`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.

The overall verdict is `ROUTE_A_REJECTED`; Route B is false.  Ordinary
positional addition gives a weak arithmetic relation, but neither prime bases
nor composite bases supply rational-prime orbit semantics.  The package makes
no claim about target tables, arithmetic local data, Euler factors, root
numbers, automorphy, a target divisor or a Hilbert--Polya operator.

## Reproduction

From this directory run:

```text
python3 code/c194_holte_producer.py
python3 code/c194_holte_checker.py
python3 code/c194_sympy_crosscheck.py
python3 code/c194_replay.py
python3 code/c194_mutation.py
python3 code/c194_release_manifest.py
```

The release contains 27 payload files plus the self-excluded manifest.  See
`SOURCE_AUDIT.md` for classical ownership, `THEOREM_PACKAGE.md` for the proof
ledger, and `results/TEST_REPORT.md` for the exact regression boundary.
