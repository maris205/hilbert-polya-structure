# SD-C13 Experiment Report

## Executive result

The positive unitary-fiber escape is closed at the first moment:

\[
\tau(U)=1\Longrightarrow U=I
\]

for a faithful normalized trace. Ordinary-trace preservation through all
repetitions forces a one-dimensional trivial fiber.

    positive exact ledger plus visible motion: impossible
    nonfaithful hidden sector: ledger does not control determinant
    graded matched sector: moving determinant factor cancels
    roots-of-unity fiber: leakage delayed, not erased
    matched nonprime clocks: motion survives; PROVES_TOO_MUCH

No target-zero data or crossing census was used.

## Moment and rigidity census

Repetitions \(1\le r\le32\) were evaluated for identity, scalar-phase,
conjugate-phase, and cyclic permutation fibers. For every
\(m=2,\ldots,8\), \(\tau(P_m^r)=\mathbf 1_{m\mid r}\) with exact residual
zero.

The normalized Hilbert--Schmidt identity was checked on 32 random
diagonal-unitary controls in dimensions \(2,\ldots,8\). Maximum residual was
4.44e-16, and every nontrivial control had normalized trace different from
one. Exact Newton identities were checked for dimensions \(1,\ldots,8\);
only \(d=1\) is compatible with ordinary trace one at every repetition.

## Hidden and graded controls

For \(U=1\oplus V\), a nonfaithful state supported on the first summand has
exact moments one. The ordinary determinant retains \(\det(I-zV)\), whose
frozen motion reaches 8.883e-2; the state ledger does not control it.

For even \(=1\oplus V\), odd \(=V\), the supertrace equals one through every
tested repetition, but \(\operatorname{Ber}(I-zU)=1-z\). The moving sector
cancels. Maximum Berezinian residual was 2.22e-16.

## Recurrent controls

For a triangle with formal monomial \(xyz\), roots-of-unity fibers first
leak as follows:

| cycle size | first transfer power |
|---:|---:|
| 2 | 6 |
| 3 | 9 |
| 4 | 12 |
| 5 | 15 |
| 6 | 18 |
| 7 | 21 |
| 8 | 24 |

For two independent return paths,
\(a^r+(-1)^r b^r\) is nonzero for every repetition. Setting \(a=b\) cancels
odd powers only; even powers survive.

## Clock controls

Fiber dimensions 2, 3, 4 and 32 frozen phase seeds give:

| inventory | moving cases | total |
|---|---:|---:|
| tensor-prime entropy clocks | 96 | 96 |
| composites | 96 | 96 |
| random increasing clocks | 96 | 96 |

Every moving fiber first breaks the ledger at its dimension. Motion on
matched nonprime clocks makes the mechanism PROVES_TOO_MUCH.

## Route-A verdict

    A0_ANALYTIC_ARITHMETIC_ORIGIN
    A1_FAIL
    A2_ANALYTIC_DETERMINANT
    A3_FAIL
    A4_FAIL

    ROUTE_A_REJECTED
    GO_POSITIVE_MOMENT_RIGIDITY
    STOP_BLOCH_ESCAPE
    STOP_SCOPED / PROVES_TOO_MUCH
    ROUTE_B_LOCKED

The analytic determinant exists on its honest trace-class half-plane, but a
nontrivial determinant-visible fiber cannot retain the required positive
repetition ledger. No target divisor is claimed.

## Reproduction

From the Paper11 directory:

    python code/sdc13_unitary_fiber_experiment.py
    pytest -q code/test_sdc13_unitary_fiber_experiment.py
    sha256sum -c results/SHA256SUMS.txt

Frozen test result: 9 passed.
