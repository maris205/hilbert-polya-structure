# Results

Regenerate from the project root with

```bash
python code/trace_map_audit.py --out-dir results --max-k 8 --prime 1000003
python code/coding_boundary_audit.py --out-dir results --max-k 15
python code/degree_clock_audit.py --out-dir results --max-k 30 --max-symbolic-k 10
python code/value_growth_audit.py --out-dir results --through-k 18
python code/independent_check.py
python code/test_trace_map_audit.py
python code/test_coding_boundary_audit.py
python code/test_degree_clock_audit.py
python code/test_value_growth_audit.py
```

Artifacts:

- `certificate.json`: exact recurrence, invariant, two escaping witnesses,
  chronology checks, and the scoped incidence decision;
- `modular_gcd_audit.csv`: 48 section-hit versus three-coordinate-return
  tests for \(k=1,\dots,8\), \(d_k=0,\pm2\), and clocks \(m=k,q_k\);
- `independent_check.json`: separate implementation checking the 48 persisted
  rows, 48 second-prime rows, 30 rational gcds, schemas, and chronological
  products;
- `symbolic_boundary_certificate.json`: source-faithful ten-state Casdagli
  band language, marked Fibonacci path counts, closed traces, determinant,
  boundary resolvent, and the decorated unweighted six-state quotient;
- `degree_clock_certificate.json`: dimension-independent uniform-degree
  theorem scope, escape routes, and symbolic degree verification;
- `degree_growth.csv`: the exponentially growing minimum per-step polynomial
  degree required to match \(d_k\) at each renormalization level;
- `value_growth_certificate.json`: exact rational product-growth inequalities
  at \(\lambda=1\), \(E=0,-1\), which imply infinite coefficient root growth
  and the zero-radius analytic-germ obstruction.

The modular certificate is an exact falsifier of the frozen incidence
equations.  Since the hit polynomial is monic over \(\mathbb Z\), gcd \(1\)
modulo the registered prime excludes every common root over
\(\overline{\mathbb Q}\) for those four univariate equations.

It is not a no-go theorem for arbitrary Fredholm determinants.  The C13P
all-level result has a different proof and scope: even for arbitrary finite
\(N_k\), uniformly bounded local polynomial degree gives only linear
energy-degree growth in trace-map time, while
\(\deg_Ed_k=F_{k+2}\).  State-dimension growth alone does not evade that
bound.  C13G separately proves \(|d_k(E_*)|^{1/k}\to\infty\), so both the
literal coefficient series and the logarithmic-trace series have radius zero.
It excludes matching by any scalar germ analytic at \(z=0\), including fixed
bounded-resolvent matrix elements and standard analytic Fredholm
determinants.  It does not exclude physical \(q_k\) indexing,
\(k\)-dependent/nonanalytic or witness-singular constructions, or indirect
energy-divisor maps.

The symbolic boundary certificate belongs to Casdagli's
\(V_{\rm C}\ge8\) regime, equivalently \(\lambda\ge16\).  It is not evidence
for the coupling-one incidence systems.  The coupling-one values
\(E=0,-1\) used by the incidence and zero-radius audits are
finite-periodic-approximant section energies, not asserted spectral points of
the infinite Fibonacci Hamiltonian.
