# Marked spectral incidences versus trace-map returns

## Outcome

This project is a system-level pivot from the area-preserving Hénon map to the
Fibonacci Schrödinger trace map

\[
T(x,y,z)=(2xy-z,x,y).
\]

It produced a finite incidence obstruction, a source-faithful symbolic
boundary calculation, and two complementary all-level clock obstructions.

First, finite periodic-approximant spectral conditions are one-coordinate
section incidences of the marked energy line

\[
\ell_\lambda(E)=\left(\frac{E-\lambda}{2},\frac E2,1\right),
\]

whereas a trace-map periodic point is a three-coordinate return.  Exact escape
witnesses and 48 modular gcd calculations refute the two naive identifications

\[
d_k(E)=0,\pm2
\quad\Longleftrightarrow\quad
T^m\ell_\lambda(E)=\ell_\lambda(E),
\qquad m\in\{k,q_k\}.
\]

The scoped decision is

```text
HCS-C13: KILL_SECTION_HIT_EQUALS_TRACE_MAP_RETURN_AT_M_EQUALS_K_OR_QK
```

Second, Casdagli's large-coupling Markov coding gives an exact positive
structural identity for marked spectral-band paths.  The primary spectral
language is the source ten-state presentation.  With its endpoint vectors,

\[
u_{10}^\top A_{10}^kv_{10}=F_{k+2},\qquad
u_{10}^\top(I-zA_{10})^{-1}v_{10}=\frac{1+z}{1-z-z^2},
\]

whereas the closed-orbit zeta is

\[
\det(I-zA_{10})^{-1}
=\bigl((1+z)^2(1-z+z^2)(1-z-z^2)\bigr)^{-1}.
\]

This is a genuine boundary/closed distinction, but it counts bands rather
than producing the energy polynomial \(d_k(E)\).  Casdagli's source parameter
is related by

\[
E_{\rm C}=E-\lambda/2,\qquad V_{\rm C}=\lambda/2,
\]

so his proved regime \(V_{\rm C}\ge8\) corresponds to \(\lambda\ge16\), not
to the coupling-one incidence audit.  The unweighted count descends to a
six-state quotient only after decorating its initial symbol \(6\) with the
lift to old state \(R_6\); arbitrary energy weights need not descend.

```text
HCS-C13B: PROVED_SOURCE_FAITHFUL_MARKED_BAND_PATH_SERIES_DIFFERS_FROM_CLOSED_ZETA
```

Third, an all-level degree theorem rules out a much larger natural class.  At
level \(k\), let \(B_k(E)\) have any finite dimension \(N_k\), polynomial
entries of degree at most a uniform \(D\), and polynomial boundary vectors of
uniformly bounded degree.  Then

\[
\deg_E\operatorname{tr}B_k(E)^k\le kD,
\]

and every boundary coefficient \(u_k(E)^\top B_k(E)^kv_k(E)\) has the same
linear degree bound up to a uniform constant.  The Fibonacci discriminant
instead has

\[
\deg_Ed_k=q_k=F_{k+2}.
\]

Therefore no such uniformly bounded-polynomial passive family in trace-map
time can reproduce all Fibonacci discriminants, either as closed-path traces,
boundary-resolvent coefficients, or order-\(k\) coefficients of the associated
finite determinants.  This conclusion is dimension-independent: merely
increasing \(N_k\) does not change the energy-degree bound.  A growing-order
full characteristic determinant such as \(\det(EI-H_{k,\theta})\) is a
different observable, not an exception to the trace statement.

```text
HCS-C13P: PROVED_DIMENSION_INDEPENDENT_PASSIVE_PARAMETER_BOUNDED_POLYNOMIAL_DEGREE_CLOCK_OBSTRUCTION
```

Fourth, the exact escape witnesses give a zero-radius obstruction that does
not assume polynomial energy dependence.  After the strict escape triple,

\[
|x_{j+1}|>|x_j||x_{j-1}|,
\qquad \log|d_j(E_*)|\ge cF_j,
\]

so, at \(E_*=0,-1\),

\[
|d_k(E_*)|^{1/k}\longrightarrow\infty.
\]

Both \(\sum_k d_k(E_*)z^k\) and
\(\sum_{k\ge1}d_k(E_*)z^k/k\) therefore have radius of convergence zero.
No scalar germ analytic at \(z=0\) can reproduce the first series literally
coefficientwise, and no analytic \(\Delta\) with \(\Delta(0)=1\) can reproduce
the second through a literal logarithmic-trace identity.  This includes fixed
bounded-operator resolvent matrix elements and standard analytic Fredholm
determinants, not merely finite matrices.

```text
HCS-C13G: PROVED_ZERO_RADIUS_RENORMALIZATION_CLOCK_OBSTRUCTION_AT_EXACT_ESCAPE_ENERGIES
```

These theorems do **not** rule out all energy-dependent Fredholm determinants.
Physical-time indexing by \(q_k\), a \(k\)-dependent or nonanalytic family, a
construction singular at a witness, nonlinear/composition dynamics, a moving
energy evaluation functional, or an indirect divisor map can evade their
hypotheses.  Infinite dimension by itself is not an escape from C13G if the
claimed scalar coefficient or logarithmic determinant is still a germ
analytic at \(z=0\); growing state dimension by itself cannot evade C13P.  A
general boundary operator remains `NOT_TESTABLE` until its space, weights,
variables, clock, normalization, and claimed coefficient/divisor identity are
defined.

## Exact witnesses

Let \(w_{-1}=b,w_0=a,w_{k+1}=w_kw_{k-1}\), with
\(V(a)=\lambda,V(b)=0\), and retain the chronological product

\[
M(w;E)=A_{V(c_q)}(E)\cdots A_{V(c_1)}(E),\qquad
A_v(E)=\begin{pmatrix}E-v&-1\\1&0\end{pmatrix}.
\]

Writing \(d_k(E)=\operatorname{tr}M(w_k;E)\),

\[
d_{k+1}=d_kd_{k-1}-d_{k-2},\qquad
(d_{-2},d_{-1},d_0)=(2,E,E-\lambda).
\]

At \(\lambda=1\), \(d_1(E)=E(E-1)-2\).  The finite-approximant band edge
\(E=0\) and finite-approximant discriminant-zero root \(E=-1\) both have
escaping, hence nonperiodic, trace-map orbits.  They are section energies for
the length-\(q_1\) periodic approximant, not points being asserted to lie in
the spectrum of the infinite Fibonacci Hamiltonian.  Here
\(d_k(E)=2\cos\theta\) uses the total Floquet phase \(\theta\) accumulated
across the full \(q_k\)-site cell, so the latter root has
\(\theta=\pi/2\pmod\pi\).

The registered finite audit covers \(k=1,\ldots,8\), sections
\(d_k=0,\pm2\), clocks \(m=k,q_k\), and return times through 55.  All 48
simultaneous gcds equal 1 over \(\mathbb F_{1000003}[E]\).  A separate
implementation verifies the same 48 cases at \(p=1000033\) and 30 cases
directly over \(\mathbb Q[E]\).

## Reproduce

Requires Python 3 and SymPy.

```bash
python code/trace_map_audit.py --out-dir results
python code/coding_boundary_audit.py --out-dir results
python code/degree_clock_audit.py --out-dir results
python code/value_growth_audit.py --out-dir results
python code/independent_check.py
python code/test_trace_map_audit.py
python code/test_coding_boundary_audit.py
python code/test_degree_clock_audit.py
python code/test_value_growth_audit.py
```

No experiment averages a substitution word or replaces its chronological
matrix product by an incidence matrix.

## Project map

- `DERIVATION_PACKAGE.md`: exact recurrences, incidence audit, and theorems.
- `SOURCE_AUDIT.md`: primary literature and novelty boundary.
- `IDEA_REPORT.md`: breadth-first candidate decision.
- `EXPERIMENT_PLAN.md`: frozen claim-driven protocol and theorem gate.
- `code/`: incidence producer, source-faithful symbolic-boundary, degree, and
  value-growth audits, regression tests, and independent checker.
- `results/`: exact certificates and ledgers.
- `paper/`: manuscript and roadmap.
- `evaluations/route_a/`: versioned formal screening records.
