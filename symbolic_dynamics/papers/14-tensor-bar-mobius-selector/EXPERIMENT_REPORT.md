# SD-C16 Experiment Report

## Frozen outcome

The experiment separates one exact positive construction from two exact
negative boundaries:

```text
GO_TENSOR_MOBIUS_INCIDENCE_DETERMINANT
GO_GLOBAL_INCIDENCE_SELECTOR
STOP_FINITE_LOCAL_SELECTOR
STOP_FINITE_STATE_SELECTOR
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
STOP_ORBITWISE_PRIME_CORRESPONDENCE
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

No Riemann-zero data, root search, target crossing, fitted phase, or fitted
cutoff is used.

## 1. Local cocycle audit

On the bidirected path control inherited from Paper 13, a directed integer
cocycle is determinant-equivalent modulo coboundary to its round-trip edge
charges `k_i=q_i^++q_i^-`. Exact preservation of the neutral Euler sector
requires all `k_i` to have one strict sign. In the positive cone, the first
Fourier mode has one-edge sign and cannot cancel.

The frozen matrix contains 2,574 exact rational rows from 18 named rules at
four cutoffs, with 16 shuffled and 16 random-increasing seeds. Rules based on
three through eight consecutive tensor-prime adjacency tokens pass the naive
random controls, but all leak on explicitly nontrivial prefix/block-preserving
prime shuffles.

- Radius-one Boolean tables: 256 exhausted; one naive pass; zero robust pass.
- Labelled one-/two-state Mealy machines: 260 exhausted; zero robust pass.
- Rank, factor-depth, `v_2`, and entropy-bin coboundaries have the same full
  exact continuant as the constant representative.

Thus finite-local character motion remains `PROVES_TOO_MUCH` and is not used
to build the bar determinant.

## 2. Global tensor incidence

The tensor-divisor Möbius function was computed from the full-shift tensor
monoid without loading a prime coefficient table. In the formal tensor-prime
entropy basis, all 960 rows through principal-ideal cutoffs
`64,128,256,512` satisfy exactly

```text
Lambda_tensor(p^r) = log p,
Lambda_tensor(n) = 0 for mixed-prime n.
```

All Möbius inverse checks and every overlapping-cutoff check are exact. At
cutoff 512 there are 117 prime-power endpoints and 394 mixed-prime endpoints;
all 394 mixed endpoints have zero tensor Mangoldt vector.

The 136 inventory-control rows enforce the source boundary. Ordered and
shuffled prime lists become divisor closed after adjoining the tensor unit;
composite-only and generic random lists do not and therefore cannot redefine
`mu_tensor`. Evaluated in the ambient monoid, every inventory has exactly the
predicted prime-power support. All 32 entropy-relabel controls break the
selector, with at least 36 mixed-prime leaks. This confirms that compatible
tensor entropy, rather than incidence syntax alone, carries the arithmetic
content.

## 3. Raw reduced-bar determinant

The predeclared raw threshold is

```text
sigma_bar =
1.728647238998183618135103010297691464234109849335035732321285908423179...
```

the 80-digit solution of `zeta(sigma_bar)=2`. For every raw point,
`Re(s)>sigma_bar` and `zeta(Re(s))-1<1`. The 28-row word-length audit verifies

```text
F_bar = B-B^2+B^3-... = B/(1+B),
D_bar(s,1)=1-F_bar=1/zeta(s).
```

The maximum 80-digit residual of the exact geometric-remainder identity is
`1.9126762000924173e-81`; the maximum closed determinant identity residual is
`1.0542197943230523e-81`.

Raw convergence is correctly slow near the boundary. At word length 64:

| `s` | `abs(F-F_64)` | absolute geometric tail bound |
|---|---:|---:|
| `1.75` | `0.04197602763634342` | `2.1860567975637974` |
| `1.8` | `0.00015421747630950955` | `0.0024647343148828213` |
| `2` | `2.525498827254661e-13` | `1.1700021513921703e-12` |
| `1.9+0.6i` | `4.5194277672391e-14` | `2.958396244037778e-08` |

An independent finite-alphabet computation at `s=2`, endpoint cutoff 32,
uses exact rational arithmetic and satisfies every finite geometric-tail
identity exactly.

## 4. Endpoint-first Möbius completion

All 512 formal endpoint rows enumerate ordered factorization word layers and
independently compute the Dirichlet inverse. Every row satisfies

```text
[n] F_bar = -mu_tensor(n),
[n] D_bar = mu_tensor(n).
```

This proves the coefficient-grouped identity on `Re(s)>1`; it does not claim
raw absolute word convergence below `sigma_bar`.

As a separate numerical observation, an independent linear Möbius sieve was
summed at 80 digits through `N=100000`. Final determinant residuals are:

| `s` | `abs(sum_(n<=N) mu(n)n^(-s) - 1/zeta(s))` |
|---|---:|
| `1.1` | `1.5484883863625893e-4` |
| `1.25` | `2.7737331870089995e-5` |
| `1.5` | `1.5777644419417107e-6` |
| `1.7` | `1.5913717136704922e-7` |
| `1.25+0.75i` | `2.7839698494977572e-5` |

These residuals are not used as proof and are not zero-fitting metrics.

## 5. Trace-log and repetitions

The 81-row trace-log matrix uses three source points, three `z` values, and
nine repetition cutoffs through 256. Every point satisfies `abs(zF)<1`.
At the final cutoff the maximum trace-log residual is
`7.151980202205042e-30`; it occurs at the deliberately slow endpoint-grouped
point `s=1.25,z=1`. The corresponding determinant reconstruction residual is
`1.5564322421888084e-30`.

This verifies repetitions of the scalar bar-code return sum. It does not turn
tensor atoms into primitive temporal cycles: the actual primitives are
factorization-word necklaces.

## 6. Universal inversion control

The same alternating grammar was applied to all-object, composite-only,
prime-only, random-positive, random-support, synthetic-signed, shuffled-ramp,
and three scalar inventories. In every case, explicit word layers and an
independent Dirichlet inverse agree exactly, with zero convolution mismatch.

Therefore reciprocal inversion is a universal algebraic feature:

```text
F_X=B_X/(1+B_X),
D_X=1/(1+B_X).
```

This is the decisive `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH` result.
The arithmetic content lies in the frozen tensor source and entropy
derivative; the bar inversion itself does not distinguish that source from
generic weighted inventories.

## Route-A interpretation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
```

- A0 is analytic because tensor atoms, powers, entropy, `mu_tensor`, and
  `Lambda_tensor` are derived from one source without target data.
- A1 is weak because the bar shift has reproducible primitive necklaces, but
  they are not primes and the prime-power profile appears only after signed
  endpoint aggregation.
- A2 is analytic on the declared domains: a scalar trace-class Fredholm
  determinant exists, and at `z=1` equals `1/zeta(s)` on `Re(s)>1` after
  endpoint grouping.
- A3 fails: there is no completed functional equation, Gamma factor, global
  divisor theorem, Riemann--von Mangoldt law, or Weil compression.
- A4 fails: no natural unitary, scattering, Hamiltonian, or operator lift is
  supplied.

All target-zero fields are `not_applicable`. Route B remains locked.

## Verification

- Unit tests: 18/18 passed.
- Result/code checksum ledger: generated after the final code freeze.
- Cache policy: bytecode disabled and pytest cache disabled.
