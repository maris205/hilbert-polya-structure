# HCS-P55: A three-block obstruction to local Galois-excess potentials

HCS-P55 attacks the open regularity gate isolated in HCS-P54.  On the frozen
four-state mixing H6 survivor, let \(E_\gamma\) be the nonphysical Galois
contribution to the Mahler height of the return multiplier.  A potential that
depends on \(r\) consecutive states pairs linearly with the cyclic
\(r\)-block incidence vector of each orbit.

Five exact primitive cycles give the shortest triple-block relation

\[
N_3(\gamma_3)+N_3(\gamma_5)
=N_3(\gamma_{4a})+N_3(\gamma_{4b}).
\]

The new period-five orbit has trace polynomial

\[
\begin{aligned}
Q_5(T)={}&T^6+3300T^5-34165368T^4-7291075328T^3\\
&+26529205510272T^2+3609165326736384T\\
&-4266315336505009664.
\end{aligned}
\]

All six trace roots are exactly isolated outside \([-2,2]\).  An independent
Sturm/derivative certificate proves that the physical coordinate root has
the required sign word and maps monotonically into the final trace interval.
Its Galois
excess satisfies \(E_5>E_{4a}\), while \(E_3>0\) and \(E_{4b}=0\).  Hence the
periodic-sum identity forced by the block relation fails:

\[
E_3+E_5>E_{4a}+E_{4b}.
\]

Therefore no locally constant potential depending on at most three
consecutive H6 states realizes the full excess assignment.  Any such local
model needs at least a four-symbol window.

The boundary is equally important.  The five witnesses themselves admit a
nonnegative four-block interpolation, and in fact every finite family of
periodic totals can be interpolated by a sufficiently long cylinder
function.  Thus this paper does **not** refute an unrestricted Hölder
realization.  It proves the correct quantitative gate in the one-sided H6
presentation: every length-\(m\) forward-block incidence relation must have
excess discrepancy decaying exponentially in \(m\) if one Hölder potential
exists.  A two-sided formulation would additionally require an explicit
cohomological reduction to a future-dependent representative.

## Status

- **PROVED:** exact primitive H6 cycle enumeration through period five;
- **PROVED:** exact period-four-a and period-five trace/multiplier fields;
- **PROVED:** no width-one, width-two or width-three local excess potential;
- **PROVED:** the five-row obstruction is finitely sharp at width four;
- **PROVED:** quantitative higher-block necessary condition for a Hölder
  realization;
- **OPEN:** all-orbit Hölder or controlled asymptotically additive
  realization;
- **OPEN:** an infinite sequence of higher-block relations that violates
  every Hölder decay rate;
- **OPEN:** rational-prime trace, completed determinant and Hilbert--Pólya
  operator.

Route A remains
`(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only],
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` with overall
`ROUTE_A_EXPLORATORY`.  The full Galois-weighted object still has no A2 pass.
Route B is not authorized.

## Reproduce

```bash
bash code/run_c55.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The final manuscript is [`paper/paper.pdf`](paper/paper.pdf).  Exact and
independent certificates, source locks, hostile reviews and the claim
firewall are retained in `results/` and `notes/`.
