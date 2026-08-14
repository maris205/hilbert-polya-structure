# HCS-P56: An infinite block-incidence ladder and a four-block obstruction

HCS-P56 continues the exact Galois-excess regularity test from HCS-P55 on
the same frozen four-state H6 survivor.  It replaces the open instruction
“find growing higher-block relations” by two explicit primitive families

\[
A_m=0^{m-2}21,\qquad B_m=0^{m-3}231,
\]

and proves the all-width identity

\[
N_m(A_m)+N_m(B_{m+2})=N_m(A_{m+1})+N_m(B_{m+1})
\quad(m\ge3).
\]

The proof is an exact insertion formula: both block-row differences are

\[
e_{0^{m-1}2}+e_{10^{m-1}}-e_{10^{m-2}2}.
\]

The first new ladder member is the period-six word `000231`.  Its exact
coordinate tuple is `(a,a,c,d,d,c)`, where

\[
c=-\frac{\sqrt7}{6},\quad
a=\frac{-1-\sqrt{25+4\sqrt7}}{12},\quad
d=\frac{-1+\sqrt{25+4\sqrt7}}{12}.
\]

Its trace and multiplier polynomial are

\[
T_6=18062+5352\sqrt7,
\]

\[
z^4-36124z^3+125728518z^2-36124z+1,
\]

and its Galois excess is

\[
E_{B_6}=\operatorname{arcosh}(9031-2676\sqrt7).
\]

At width four, the ladder forces

\[
E_{A_4}+E_{B_6}=E_{A_5}+E_{B_5}.
\]

The exact data prove the strict opposite inequality.  A shared nonphysical
period-five trace root gives

\[
E_{A_5}+E_{B_5}>2\operatorname{arcosh}(355),
\]

whereas

\[
E_{A_4}+E_{B_6}
<\operatorname{arcosh}(52)+\operatorname{arcosh}(1951).
\]

The integer comparison

\[
709^2=502681>405808=104\cdot3902
\]

proves the separation.  Therefore no locally constant potential depending
on at most four consecutive symbols realizes the full Galois-excess
assignment.

This finite witness is sharp: seven cycles have a determinant-one
width-five incidence minor.  Hence all seven totals, including the excesses,
can be interpolated at width five.  The general one-sided Hölder question is
still open.  The infinite ladder now gives its explicit necessary condition:

\[
|\Delta_m|\le C(4m+4)\vartheta^{\alpha m},
\]

where

\[
\Delta_m=E_{A_m}+E_{B_{m+2}}-E_{A_{m+1}}-E_{B_{m+1}}.
\]

## Status

- **PROVED:** exact primitive H6 cycle census through period six;
- **PROVED:** an infinite cyclic block-incidence ladder for every `m >= 3`;
- **PROVED:** exact radical coordinates and degree-four multiplier field for
  `B6`;
- **PROVED:** no width-one through width-four local excess potential;
- **PROVED:** the seven-row witness is finitely sharp at width five;
- **PROVED:** explicit exponentially decaying necessary sequence for any
  one-sided Hölder realization;
- **OPEN:** asymptotics or a recurrence for `Delta_m`;
- **OPEN:** an unrestricted one- or two-sided Hölder realization/no-go;
- **OPEN:** the full Galois-weighted determinant and every arithmetic or
  Hilbert--Pólya bridge.

Route A remains
`(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only],
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` with overall
`ROUTE_A_EXPLORATORY`.  Route B is not authorized.

## Reproduce

```bash
bash code/run_c56.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The manuscript is [`paper/paper.pdf`](paper/paper.pdf).  The primary and
independent JSON certificates, exact proof package, evaluator records,
hostile reviews and claim-boundary audit are retained in this directory.
