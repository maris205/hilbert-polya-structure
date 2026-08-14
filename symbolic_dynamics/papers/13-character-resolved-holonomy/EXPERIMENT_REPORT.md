# SD-C15 Experiment Report

## Frozen outcome

SD-C15 succeeds as a same-parent character resolution and fails as an
arithmetic-selective transverse mechanism:

```text
GO_CHARACTER_RESOLUTION
/ STOP_ARITHMETIC_SELECTIVITY
/ STOP_TIME_REVERSAL
/ STOP_SCOPED
/ PROVES_TOO_MUCH
```

Route B remains locked.

## Exact identities

For the primary \(+1/+1\) charges, every mixed closed base word has strictly
positive total charge. The exact census for \(N=2,3,4,5\) through power 12
contains no charge-zero mixed word. Consequently,

\[
[w^0]\operatorname{Tr}L_s(w)^r=\sum_p p^{-rs}
\]

at every finite cutoff and all orders, and the coefficientwise zero mode of
the trace-log is the reciprocal Euler product.

The two-atom determinant is

\[
\det(I-zL(w))=(1-zx)(1-zy)-z^2a^2w^2.
\]

Replacing the reversed charge by \(-1\) moves this mixed term into degree
zero. The inverse census first leaks at \(r=2\), as preregistered.

For \(\Re s>1\), \(\sum_n|a_n(s)|<\infty\); therefore both weighted shifts
forming \(A_s\), and hence every Bloch fiber \(L_s(w)\), are trace class.

## Frozen determinant matrix

The run covers 384 inventory/cutoff/source/determinant combinations and all
1024 characters in each combination. The continuant constant coefficient
equals

\[
d_0=\prod_{n=1}^N(1-zp_n^{-s})
\]

with residual exactly zero in every row. Every primary row also has a
nonconstant coefficient: the observed response energy ranges from
`1.855046598600402e-09` to `0.09081813205497141`.

The adversarial table additionally covers all 3072 combinations of the 32
positive-charge fields with the eight cutoffs, four source points, and three
determinant points. Together with the 384 inventory rows it contains 3456
frozen control rows; all determinant degrees remain below the 1024-character
grid size.

At the frozen summary point \((N,s,z)=(32,1.5,0.35)\),

| inventory | \(E\) |
|---|---:|
| tensor primes | `0.01491104027906271` |
| composites | `0.002353524613482555` |
| shuffled primes | `0.00005027756158583232` |
| random increasing | `0.00003197088387131679` |

All 32 frozen positive-charge controls also move, with

```text
0.011522075401440002 <= E <= 0.014221391124950388.
```

Thus the preregistered control-collapse condition fails decisively. This is
already forced analytically by the nonzero two-atom coefficient
\(-z^2a_n(s)^2w^{q_n^++q_n^-}\) for positive real \(s\), so the numerical
matrix confirms rather than creates the obstruction.

## Independent checks

- 12/12 unit tests pass.
- The exact positive census has zero charge-zero mixed rows.
- The inverse census has 144 aggregated charge-zero mixed rows across the
  four cutoffs, first appearing at power two.
- The selected dense, trace-power, 80-digit, and DFT determinant checks have
  maximum residual `6.087272963323595e-16`.
- Gauge and roof-reparameterization controls have maximum residual
  `6.206335383118183e-17`.
- The forward-DAG determinant polynomial has degree zero and \(E=0\).
- The results checksum ledger verifies the two source files and all five
  generated artifacts.

## Route-A interpretation

The tensor-prime origin, deck-normalized lifted ledger, trace-class Bloch
family, and exact Euler neutral coefficient establish A0--A2 for the frozen
parent object.  These are different readouts of one equivariant family; no
unitary character fiber itself has the Euler ledger.  They do not
establish a target divisor or arithmetic transverse response. Composite,
shuffled, random-increasing, and random-positive-charge controls reproduce
the character motion. Rank/entropy phases are gauge, the roof twist merely
translates \(s\), inverse time reversal corrupts degree zero, and the forward
DAG returns to determinant invisibility.

No Riemann-zero data, root census, target crossing, fitted character, analytic
completion, Weil compression, RH conclusion, or Hilbert--Pólya operator is
claimed.
