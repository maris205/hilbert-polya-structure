# Frozen experiment and theorem plan

## Claims under test

### C13: incidence claim

For \(m=k\) or \(m=q_k=F_{k+2}\), a spectral-section equation
\(d_k(E)=0,\pm2\) is equivalent to the trace-map return
\(T^m\ell(E)=\ell(E)\).

**Decision:** refuted in the registered scope and globally as a proposed
universal equivalence by explicit counterexamples.

### C13B: source-faithful marked-band language

Casdagli's endpoint-constrained spectral-band words define a boundary series
different from the closed-orbit zeta, and the unweighted language admits a
six-state quotient that preserves the marked count.

**Decision:** proved in the source ten-state presentation for
\(V_{\rm C}\ge8\), equivalently \(\lambda\ge16\).  The quotient requires the
initial symbol-\(6\) lift to old state \(R_6\).  General energy-dependent
weights are not claimed to descend.

### C13P: uniform polynomial passive-parameter claim

At every level, a finite weighted Markov/transfer matrix may have arbitrary
dimension \(N_k\) and arbitrary level-dependent coefficients, but uniformly
bounded polynomial dependence on \(E\) per renormalization step.  Such a
family can reproduce every Fibonacci discriminant \(d_k(E)\) as either a
closed-path trace, a uniformly bounded-degree boundary coefficient, or an
order-\(k\) finite-determinant coefficient.

**Decision:** analytically refuted for all levels by the degree/clock theorem.

### C13G: zero-radius analytic-germ claim

At either registered witness, a scalar germ analytic at \(z=0\) can reproduce
the discriminants literally as its \(z^k\) coefficients, or an analytic
normalized determinant can reproduce them as signed logarithmic traces.

**Decision:** analytically refuted.  At \(\lambda=1\), \(E_*=0,-1\),

\[
|d_k(E_*)|^{1/k}\longrightarrow\infty,
\]

so both \(\sum_kd_k(E_*)z^k\) and
\(\sum_{k\ge1}d_k(E_*)z^k/k\) have radius zero.  This excludes literal
coefficient/log-trace matching by any scalar germ analytic at zero, including
fixed bounded-resolvent matrix elements and standard analytic Fredholm
determinants.

### C13R: unrestricted Fredholm reframe

An energy-dependent boundary Fredholm construction may encode the finite-time
energy-line incidences through an explicitly defined indirect divisor map
while preserving chronology and respecting C13G.

**Decision:** `NOT_TESTABLE` until the function space, operator, weights,
variables, boundary functionals, and normalization are defined.

## Frozen finite audit

- substitution: \(w_{-1}=b,w_0=a,w_{k+1}=w_kw_{k-1}\);
- site potentials: \(V(a)=1,V(b)=0\);
- matrix order: later sites multiply on the left;
- trace recursion: \((d_{-2},d_{-1},d_0)=(2,E,E-1)\);
- spectral sections: \(d_k=0,+2,-2\);
- candidate return clocks: \(m=k\) and \(m=q_k=F_{k+2}\);
- exact levels: \(k=1,\ldots,8\);
- producer field: \(\mathbb F_{1000003}\);
- independent-check field: \(\mathbb F_{1000033}\), plus \(\mathbb Q[E]\)
  through \(k=5\);
- forbidden data: all Riemann prime and zero tables;
- arithmetic: exact only, no floating roots.

## Work packages

### WP0: source and convention lock — complete

Freeze the trace map, seed words, marked energy line, discriminant, physical
length, and hyperbolicity sources.  Use the all-coupling Damanik--Gorodetski--
Yessen framework for the coupling-one incidence work.  Use Casdagli's coding
only in its stated \(V_{\rm C}\ge8\) regime, which becomes \(\lambda\ge16\)
after \(E_{\rm C}=E-\lambda/2\), \(V_{\rm C}=\lambda/2\).  Do not transfer the
large-coupling band-language theorem to \(\lambda=1\).

### WP1: chronological algebra — complete

Directly multiply ordered site matrices and verify the trace recurrence and
Fricke invariant.  No word-incidence averaging is allowed.

### WP2: exact incidence falsifiers — complete

The finite-approximant band edge \(E=0\) and finite-approximant
discriminant-zero root \(E=-1\) at \(k=1\) have escaping trace-map orbits.
They are not being asserted to be spectral points of the infinite Fibonacci
Hamiltonian.  The 48-case modular audit finds no algebraic section/return
coincidence in the frozen levels and clocks.  The Bloch phase is the total
phase across the full periodic cell.

### WP3: independent implementation — complete

Use a separate polynomial representation and direct chronological matrix
multiplication.  Do not import producer code.  Validate the persisted schema,
all 48 original-prime rows, all 48 rows at a second prime, and 30 rational gcds.

### WP4: source-faithful band boundary — complete

Extract Casdagli's ten-state graph and endpoint selectors, verify the marked
Fibonacci word counts, boundary resolvent, closed determinant, and the
decorated unweighted six-state quotient.  Keep the original ten-state object
for arbitrary energy weights.

### WP5: all-level degree theorem — complete

Prove

\[
\deg_E\operatorname{tr}B_k(E)^k\le kD,
\qquad
\deg_E u_k(E)^\top B_k(E)^kv_k(E)\le D_u+kD+D_v,
\]

for arbitrary finite \(N_k\) with uniform degree bounds, then compare with
\(\deg_Ed_k=F_{k+2}\).  Apply the same filtration to order-\(k\) formal
determinant coefficients.  Audit the exact Fibonacci degrees symbolically
through \(k=10\) and the integer growth requirement through \(k=30\).

### WP6: zero-radius analytic-germ obstruction — complete

Use the exact escape triples to prove
\(|x_{j+1}|>|x_j||x_{j-1}|\), hence Fibonacci growth of the logarithms and
\(|d_k(E_*)|^{1/k}\to\infty\).  Apply Cauchy--Hadamard to the coefficient and
log-trace series, then exclude any literal realization by a scalar germ
analytic at zero.  Record exact rational growth through \(k=18\).

### WP7: unrestricted relative determinant — closed as not testable

No numerical transfer-operator spectrum is authorized.  Promotion would
require, before computation, an explicit Banach/Hilbert space,
\(\mathcal L_{E,\theta}\), boundary functionals, determinant convention,
normalization, and an all-level identity that explains how the degree theorem
is evaded.

## Falsification and escape routes

The C13P theorem is deliberately scoped.  It does not exclude physical-time
models, level-dependent exponential-degree weights, nonlinear/composition
renormalization, growing-order full characteristic determinants, or
non-polynomial operator families outside its degree filtration.  Growing
state dimension alone is not an escape for the tested \(k\)-step traces,
boundary coefficients, or order-\(k\) determinant coefficients.  C13G
separately excludes literal coefficient or logarithmic-trace matching at the
witnesses by **any** scalar germ analytic at zero; infinite dimension alone
does not evade it.  Its escape routes are physical-clock indexing by \(q_k\),
\(k\)-dependent or nonanalytic/zero-radius families, singularity at a witness,
composition or moving evaluation, and indirect divisor maps.  Any future
claim must state which remaining escape route it uses and why that route is
natural rather than target injection.

## Switch rule

The theorem gates are now resolved: the uniform-polynomial short-clock family
and the analytic-germ literal coefficient/log-trace family are closed, while
the proposed indirect boundary operator is not defined.  After the paper and
registry update, switch to a noncommuting \(S\)-integer solenoid skew product;
do not perform local Fibonacci parameter scans.
