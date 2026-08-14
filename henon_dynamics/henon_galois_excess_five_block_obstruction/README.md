# HCS-P57: A five-block obstruction for Hénon Galois excess

HCS-P57 advances the all-width incidence ladder of HCS-P56 by one exact
algebraic stage.  On the same frozen four-state H6 survivor, write

\[
A_m=0^{m-2}21,\qquad B_m=0^{m-3}231.
\]

The ladder identity at width five is

\[
N_5(A_5)+N_5(B_7)=N_5(A_6)+N_5(B_6).
\]

This project derives the missing `A6`, `A7`, and `B7` trace algebra.  The
six-cycle `A6` has reflection pattern `(a,b,c,d,c,b)` and irreducible trace
polynomial

\[
F_6(T)=T^3+48342T^2-334511988T+306994257352.
\]

Its physical trace is the unique root in `(-54575,-54574)`.  The seven-cycle
reflection pattern `(a,b,c,d,d,c,b)` has a degree-fourteen coordinate
polynomial and an irreducible, totally real degree-fourteen trace polynomial.
The physical `A7` and `B7` cycles are two real embeddings of that one field:

\[
T(A_7)\in(-390512,-390511),\qquad
T(B_7)\in(230985,230986).
\]

The resulting Galois-excess discrepancy is

\[
\Delta_5
=E(A_5)+E(B_7)-E(A_6)-E(B_6)
=139.7325728699720846\ldots>0.
\]

The sign is exact.  For \(a>2\),

\[
\log(a-1)<\operatorname{arcosh}(a/2)<\log a.
\]

The certified trace intervals imply

\[
E(A_5)>
\log(709\cdot588\cdot389\cdot769\cdot4444),
\]

whereas

\[
E(A_6)+E(B_6)<\log(1095\cdot5138\cdot3902).
\]

The two integer products differ by

\[
554187019465548>0.
\]

Since \(E(B_7)>0\), the width-five identity is violated.  Therefore no
locally constant potential depending on at most five consecutive H6 states
realizes every primitive-orbit Galois excess.

The finite witness is sharp.  The four relation rows have a determinant
`-1` width-six minor, and the cumulative nine rows from P55--P57 have a
determinant `+1` width-six minor.  Thus their prescribed totals can be
interpolated at width six.  This does **not** construct an all-orbit
width-six or Hölder potential.

## Status

- **PROVED:** primitive H6 cycle census through period seven;
- **PROVED:** exact reflection reductions for `A6`, `A7`, and `B7`;
- **PROVED:** irreducible cubic `A6` trace field;
- **PROVED:** irreducible totally real degree-fourteen shared `A7/B7` trace
  field and reciprocal degree-twenty-eight multiplier polynomial;
- **PROVED:** \(\Delta_5>0\) by an exact integer comparison;
- **PROVED:** no width-one through width-five local excess potential;
- **PROVED:** finite sharpness at width six via unimodular minors;
- **OPEN:** the asymptotic size and sign pattern of \(\Delta_m\);
- **OPEN:** an unrestricted one- or two-sided Hölder realization/no-go;
- **OPEN:** the full Galois-weighted determinant, rational-prime trace and
  every Hilbert--Pólya operator gate.

Route A remains
`(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only],
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` with overall
`ROUTE_A_EXPLORATORY`.  Route B is not authorized.

## Reproduce

```bash
bash code/run_c57.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The manuscript is [`paper/paper.pdf`](paper/paper.pdf).  Primary and
independent certificates, tests, exact proof ledgers, evaluator records and
hostile reviews are retained in this directory.
