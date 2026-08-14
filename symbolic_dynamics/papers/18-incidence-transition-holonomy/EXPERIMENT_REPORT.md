# Experiment Report — SD-C20 Incidence-Transition Holonomy

## Outcome

The exact experiment confirms a genuine same-object nonabelian Artin
refinement and simultaneously rejects it as a Route-A candidate.  The frozen
`S3` edge cocycle is not in the natural count/gauge class, its four-step
commutator is detected by the standard representation, and its trivial block
retains the scalar Euler ledger.  However, every positive identity and every
leakage certificate is inventory-blind.  Six prime/nonprime control classes
reproduce the mechanism with pass-rate margin zero.

Frozen verdict:

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

No Riemann-zero data, target-spectrum fit, or cross-family object was used.

## Frozen symbolic object

For two atoms, states are `p,q,pq`, with arrival weights `x,y,-xy`.  The
frozen cocycle uses `r=(12)` on strict refinement, `t=(23)` on strict
coarsening, and the identity otherwise.  In two-atom type order
`(a,c,h,u,v)`, it is `(e,e,e,r,t)`.  The twisted arrival block is

`B_rho(S,T)=w(T) rho(alpha(S,T))`,

and `D_rho=det(I-B_rho)`.  Irreducible determinants are isotypic factors;
their regular-representation product is the determinant of the whole skew
extension.

## Exact formula certificate

The trivial and sign blocks both give

```text
D_triv(x,y)=D_sign(x,y)=(1-x)(1-y).
```

The exact six-dimensional standard block gives

```text
D_std(x,y)
 = (1-x)^2(1-y)^2
   + 3xy(x+y)(xy+1)(x+y-1).
```

The determinant-log expansion and an independent direct trace-power
calculation agree through total degree six.  Relative to the identity/counting
reference:

| monomial | exact coefficient |
|---|---:|
| `x^2 y` | `-3` |
| `x y^2` | `-3` |
| `x^2 y^2` | `-6` |
| unmarked `x^3 y^3` | `-9` |

The primitive edge word `[p,pq,q,pq]` has holonomy `(rt)^2`, standard
character `-1`, and identity-reference character `2`, hence isolated gap
`3`.  Its four directed edges have exactly one connected cyclic traversal.
The isolated gap is not the unmarked `x^3y^3` coefficient; the latter
aggregates distinct cycles and repetitions.

Primary artifact: `results/s3_exact_certificate.json`.

## Incidence grammar certificate

Every ordered pair of nonempty subsets through four atoms was enumerated and
partitioned by

`(u,v,w)=(|S\T|,|S∩T|,|T\S|)`.

The exact orbit counts are:

| atom count | raw pairs | incidence types | new types |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 9 | 5 | 4 |
| 3 | 49 | 13 | 8 |
| 4 | 225 | 26 | 13 |

These agree with `C(n+3,3)-(2n+1)`.  Orbit sizes and stabilizers were checked
exactly, so the classifier does not depend on atom names or values.

## Exhaustive two-atom group audit

Every `(a,c,h,u,v) in G^5` was enumerated.  Nontrivial one-dimensional
characters were audited as exact sparse polynomials.  Faithful survivors were
then evaluated on complete rectangular interpolation grids over three frozen
primes.  The CRT modulus exceeds `2(3d)!2^(3d)`, the stated absolute
coefficient bound, so passing all grids certifies equality over `Z[x,y]`.

| group | tables | 1D-clean | all-irrep clean | gauge-power | nongauge clean |
|---|---:|---:|---:|---:|---:|
| `S3` | 7,776 | 972 | 36 | 36 | 0 |
| `D4` | 32,768 | 512 | 64 | 64 | 0 |
| `Q8` | 32,768 | 512 | 64 | 64 | 0 |

For `Q8`, the four-dimensional real left-quaternion block is two copies of
the complex two-dimensional irrep and provides the faithful final audit.  The
large drop from 512 one-dimensional survivors to 64 all-irrep survivors is
an exact warning against abelianization-only tests.

Every final survivor satisfies

```text
h=a,  v=u^-1 a^3,  c=u^-1 a^2 u.
```

This is finite evidence for the frozen groups and two-atom grammar.  It is
not promoted to a universal theorem that determinants classify cocycles.

## Controls and arithmetic no-go

Five fixed seeds generate 30 inventory rows across:

- prime atoms;
- shuffled prime atoms;
- composite-only squarefree atoms;
- matched random integers;
- strictly increasing random rational atoms;
- algebraically independent formal variables.

All 30 rows retain the trivial factor, nonzero standard leakage, and
commutator gap three.  The prime pass rate and every control pass rate are
one.  Therefore

```text
identity_pass_rate_margin = 0
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
```

This is the decisive Route-A failure: transition holonomy is genuine, but it
is a universal subset-incidence mechanism with no intrinsic knowledge that
an atom is prime.

## Function-space boundary

The exact analytic ledger records two distinct thresholds:

| block | absolute subset series | proved trace-class half-plane |
|---|---|---|
| trivial rank-one arrival block | `prod_p(1+p^-sigma)-1` | `Re(s)>1` |
| nontrivial symmetric incidence block | `prod_p(1+p^-sigma/2)-1` | `Re(s)>2` |

The second threshold gives an honest Fredholm domain for the nontrivial
block.  No claim is made at or below its boundary, and no meromorphic
continuation, Gamma factor, functional equation, zero-counting law, or Weil
compression is inferred.

## Verification status

- fourteen exact tests: passed;
- `S3`, `D4`, `Q8` exhaustive counts: passed;
- standard determinant and both trace-log methods: passed;
- inventory control gate: `30/30`, hence `PROVES_TOO_MUCH`;
- target-zero data: not applicable and unused;
- Route B invocation: false.

The deterministic orchestrator runs the full generator, analyzer, tests,
schema/integrity audit, and SHA freeze twice and requires the complete
code/result ledger hash to remain identical.

## Next smallest in-family obligation

Do not add another fiber decoration to the same universal full-subset base.
The next Symbolic-Dynamics test should alter the allowed-word grammar itself
and demand an intrinsic separation theorem between prime and matched
arbitrary inventories before any continuation program is attempted.

Any geometric flat connection, quantum graph, scattering system, or
self-adjoint operator remains only a `ROUND2_CLUE` outside this experiment.
