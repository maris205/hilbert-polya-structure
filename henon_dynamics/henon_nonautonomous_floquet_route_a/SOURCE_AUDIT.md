# Source and scope audit

## Frozen candidate

The source model is the explicit polynomial cocycle

\[
F_t(x,y)=(x^2+\alpha_t x+\beta_t-y,x),
\quad (\alpha_0,\beta_0)=(0,0),\quad(\alpha_1,\beta_1)=(1,1/3).
\]

Every phase has Jacobian determinant one.  The samples `xi=-1,+1` are frozen
representatives used to make a finite exact pilot.  They are not asserted to
be periodic points or to define a Markov partition.

## Modeling choices

The four block symbols `(s0,s1)` and adjacency

\[
Q=\begin{pmatrix}1&1&0&0\\0&1&1&0\\1&0&0&1\\0&1&0&1\end{pmatrix}
\]

are a transparent finite symbolic model.  Their provenance is the experiment
design, not an imported prime/zero table.  The target-weighted transfer block
is `A_ij=Q_ij M_j`.

## Forbidden claims and data

No prime list, zero list, Euler factor, root number, automorphy datum, fitted
target spectrum, or Hilbert–Pólya operator is read or used.  The package is
explicitly under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Evidence status

The exact integer ledger and all checks are reproducible.  Geometric orbit
completeness, an analytic coding theorem, and a Fredholm owner are not
established; those limitations are repeated in the theorem package and paper.
