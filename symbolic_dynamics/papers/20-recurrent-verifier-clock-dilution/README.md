# Paper 20 — Recurrent Verifier Cycles and Clock Dilution

## Result

This project tests the most direct repair of the previous semiring sieve:
place the entire explicit primality verification path on a recurrent cycle.
The repair succeeds at the orbit level and fails at the natural whole-operator
level.

For every prime $p$, the contracted expanded quotient-search cycle has

\[
\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}
\left\lceil\frac pd\right\rceil
=\frac12p\log p+(\gamma-1)p+O(\sqrt p).
\]

Giving that cycle the exact entropy clock $\log p$ makes one traversal weigh
$p^{-s}$.  But the clock is spread over $\asymp p\log p$ graph steps.  Under
every nonnegative allocation, some edge weight approaches one.  The natural
source-weighted vertex adjacency on $\ell^2(V)$ therefore has essential norm
one, is noncompact, lies in no finite Schatten class, and has the unit circle
in its essential approximate spectrum.

The raw combinatorial orbit product

\[
\prod_p(1-z^{\ell(p)}p^{-s})
\]

still converges normally for $\operatorname{Re}s>1$, $|z|\le1$, and equals
$1/\zeta(s)$ at $z=1$.  It is **not** the ordinary Fredholm determinant of
the noncompact whole adjacency.  First return gives the trace-class diagonal
$R_s e_p=p^{-s}e_p$, but contracts the verification and changes the step
marker from $z^{\ell(p)}$ to $z$.

## Main files

- [Paper PDF](main.pdf)
- [LaTeX source](main.tex)
- [Source lock](SOURCE_LOCK.md)
- [Preregistration](PREREGISTRATION.md)
- [Proof package](PROOF_PACKAGE.md)
- [Narrative report](NARRATIVE_REPORT.md)
- [Paper plan](PAPER_PLAN.md)
- [Literature audit](LITERATURE_AUDIT.md)
- [Figure specification](FIGURE_SPEC.md)
- [Round-2 clues](ROUND2_CLUES.md)
- [Experiment report](EXPERIMENT_REPORT.md)
- [Derivation package](DERIVATION_PACKAGE.md)
- [Compilation report](COMPILATION_REPORT.md)

## Exact evidence

- 12/12 deterministic tests passed.
- Formula and explicit traversal agree for all 564 primes through 4096.
- The contracted convention gives $\ell(5)=5$ and
  $\ell(4093)=15293$.
- At $p=4093$ and $\sigma=2$, even the optimal uniform allocation has
  largest edge weight $0.9989128997668932$.
- The summable source-roof control has total clock approximately
  $28780.78337618892\log p$ at $p=4093$.
- Exact rational products agree at $z=1$ and differ at $z=1/3$.
- The no-oracle audit materializes 1,651 quotient states and finds zero
  forbidden factor identifiers or calls.
- Squares, powers of two, Fibonacci numbers, and a seeded hash support
  reproduce the obstruction under acceptance-independent padded runtimes.

Finite evidence checks the implementation.  The noncompactness, Schatten,
essential-spectrum, orbit-product, and return-collapse claims are proved
analytically.

## Route verdict

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED

GO_RECURRENT_VERIFIER_ORBIT_LEDGER
GO_CLOCK_DILUTION_THEOREM
STOP_WHOLE_VERTEX_COMPACTNESS
STOP_WHOLE_VERTEX_FREDHOLM_DETERMINANT
FIRST_RETURN_COLLAPSE
SELECTOR_TAUTOLOGICAL
PROVES_TOO_MUCH
```

No Riemann-zero data, fitted target roots, or Route-B object is used.  The
next in-family obligation is an overlapping genuinely recurrent
semiring-local grammar with a primitive-cycle separation theorem proved
before any roof or determinant is selected.
