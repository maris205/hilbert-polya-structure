# P121 exact-control results

Status: **FRESH PAPER-LOCAL PASS / OWNER CLAIMS NONCOMPUTATIONAL**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The verifier uses only integers, `fractions.Fraction`, and the Python
standard library.  It performs no sampling, floating-point calculation,
network call, or third-party import.  Fresh stdout must be byte-identical to
`code/verify.out`.

## Stored result

```text
product_plus_one verifier: PASS
exact assertions: 139,589
history enumeration: every boundary order through n <= 9
finite laws/moments/minimum atom: n <= 12, raw moments r <= 6
moment hierarchy: coefficientwise r <= 6, n <= 60
marked antichains: coefficientwise n <= 60, histories n <= 9
mean Euler linearization: coefficientwise n <= 60
coefficient artifact: byte-parsed and exactly matched through n <= 12
arithmetic: integers and fractions.Fraction only
scope sentinel: r>=3 pole/radius and all ownership claims are noncomputational
```

## Assertion accounting

| Lane | Coverage | Assertions |
|---|---|---:|
| literal histories | every boundary order through `n=9`: terminal block, literal/tree equality, and antichain evaluation | 138,699 |
| history/DP/marked agreement | law equality, mass one, and average marked polynomial for each `n<=9` | 27 |
| raw-moment differential hierarchy | coefficient identities for `r=0,...,6`, `n<=60` | 413 |
| exact law moments and minimum atom | moments `r<=6`, minimum value, and minimum mass for `n<=12` | 108 |
| marked Riccati and specialization | linearized marked series, evaluation at `s=1`, singleton coefficient through `n<=60` | 180 |
| mean Euler linearization | formal logarithmic derivative versus first moments through `n<=60` | 60 |
| committed TSV artifact | header, shape, coefficients, two moments, minimum, mass, and support through `n<=12` | 98 |
| fixed sentinels | order-four law, tenth mean, fourth variance, twelfth support size | 4 |
| **total** |  | **139,589** |

The finite controls deliberately retain owned low-order formulas, the owned
fixed-tree marker, and the owned caterpillar probability as regression
interfaces.  They do not establish the objectwise identification as an
external ownership fact, Sturm comparison, any convergence radius, novelty,
or priority.
