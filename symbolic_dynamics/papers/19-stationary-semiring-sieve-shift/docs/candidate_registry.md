# SD-C21 Candidate Registry

## SD-C21 — stationary full-shift-semiring sieve shift

```yaml
family: Symbolic Dynamics
phase_space: one-sided countable Markov edge shift
dynamics: deterministic expanded trial-division verifier with Q-state quotient search
function_space: ell^2 of graph vertices
determinant: det(I-zL_s)
honest_domain: Re(s)>1
route_b_invocation_allowed: false
status: rejected_after_exact_A1_A2_gain
```

### Positive structural prior

The alphabet-sum/tensor skeleton supplies successor, multiplication, additive
order, and entropy.  The fully expanded verifier accepts exactly the rational
primes.  Its only primitive cycles are the accepted self-loops, their temporal
repetitions give the prime powers, and a single trace-class weighted adjacency
satisfies

```text
Tr(L_s^r) = sum_p p^(-rs)
det(I-zL_s) = product_p (1-z p^(-s)).
```

### Stopping boundary

All quotient search and rejection states are transient.  Pruning them leaves
the same traces and determinant.  A universal total-decider wrapper and a
factorial-monoid specialization reproduce the construction for arbitrary
decidable supports.  The candidate is therefore `SELECTOR_TAUTOLOGICAL`,
`PRUNING_EQUIVALENT`, and `PROVES_TOO_MUCH`.

### Frozen Route tuple

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
