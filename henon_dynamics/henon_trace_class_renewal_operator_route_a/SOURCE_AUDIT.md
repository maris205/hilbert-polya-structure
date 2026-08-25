# Source audit

## Source lock

- Object: `T=S+R` on `l2(N0)`.
- Advance: `S e_n=2^{-(n+1)}e_{n+1}`.
- Return: `R e_n=2^{-(n+1)}e_0`.
- Clock: one directed edge; a first-return excursion indexed by `m` has
  exactly `m` edges.
- Normalization: the displayed dyadic weights, with no fitted parameter.
- Determinant: the ordinary trace-class Fredholm determinant
  `det_F(I-zT)`.
- Arithmetic: exact rational reconstruction.

## Permitted sources

The release uses only the definition above, elementary Hilbert-space facts,
the rank-one determinant identity, and direct exact enumeration.  Earlier
repository packages are used only as scope controls, especially the warning
that a post-hoc scalar Fredholm representation does not establish natural
operator ownership.

## Excluded sources and claims

No prime table, target zero table, target divisor, arithmetic local factor,
Euler factor, root number, automorphy input, or Hilbert--Polya hypothesis is
used.  There is no literature novelty claim and no external reviewer claim.

## Reproducibility boundary

The finite ledgers stop at coefficient 16, trace 12, and primitive clock 10.
They test the implementation.  The infinite determinant, trace-class, order,
and primitive-product statements are proved separately and do not follow
from those cutoffs.
