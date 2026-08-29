# Narrative and Derivation Report

## Target

Explain and prove how iid switching between two individually neutral
max-plus matrices creates a strictly positive linear height rate, while also
retaining an exact finite-time law, explicit Gaussian variance, pressure,
large deviations, and sharp pressure edges.

## Status

**COHERENT AS STATED / PROVABLE AS STATED.**

The endpoint and interior regimes must remain separate. For `p=0,1` the
environment is deterministic and the height is bounded. For `0<p<1` the
three-state kernel is primitive and supports the stochastic limit package.

## Invariant object

The single invariant object is

```text
H_n = max_i,j (M_n)_ij
    = max coordinates of M_n ⊗ (0,0)^T.
```

The projective gap is a finite state variable that carries the information
needed to update `H_n`; it never replaces `H_n` as the main object.

## Assumptions and convention

- Max-plus addition is maximum and max-plus multiplication is ordinary
  addition; matrix multiplication uses these operations.
- `X_1` acts first and `M_n=X_n⊗...⊗X_1`.
- `P(X_t=A)=p`, `P(X_t=B)=q=1-p`, independently over time.
- `H_0=0`; statements using primitivity, a stationary projective law, a
  positive drift, or a nondegenerate CLT assume `0<p<1`.

## Derivation strategy

The tropical route identifies an exact finite projective state. The
probabilistic route tilts its transition rewards. The first route supplies
the kernel consumed by the second, so they are complementary rather than
independent; the two variance calculations are independent only after that
kernel is fixed.

## Derivation map

1. `M_n⊗0` turns the global matrix maximum into a two-coordinate height.
2. Literal products show no rank-one reset through length two and exactly
   four at length three: `ABA/ABB/BAA/BAB`.
3. Direct application of `A` and `B` confines the coordinate difference to
   `{-3,-2,0,2,3}`.
4. Negative gaps, zero, and positive gaps have common transition/reward
   images, so strong lumping produces states `N,Z,P`.
5. Reward tilting produces `Q_p(y)` and the exact finite-time PGF.
6. At `y=1`, balance equations give the stationary law and drift.
7. A closed Poisson solution converts centered height increments into a
   bounded martingale difference, giving the SLLN/CLT and variance.
8. The characteristic cubic supplies a second derivative calculation from
   the fixed kernel, the pressure, and the LDP.
9. Reward geometry gives exact word support; scaling and diagonal similarity
   give the two temperature edges.

No approximation enters this chain.

## Main derivation

### 1. Literal projective state

Write the current vector, modulo an additive constant, as `(d,0)`. Applying
the generators gives

```text
A(d,0) = (max(d-2,-1), max(d+1,-1)),
B(d,0) = (max(d-1, 1), max(d-1,-2)).
```

Starting at `d=0`, this produces only `-3,-2,0,2,3`. Direct evaluation on
those five values gives the requested reward table after grouping negative,
zero, and positive gaps as `N,Z,P`.

The reset audit is separate from generator rank. The length-three products

```text
ABA = [[ 0,-2],[ 3, 1]]  -> gap -3,
ABB = [[ 1,-1],[ 1,-1]]  -> gap  0,
BAA = [[-1, 1],[-1, 1]]  -> gap  0,
BAB = [[ 1, 3],[-2, 0]]  -> gap  3
```

have row differences constant across both columns, so they send every
finite input to the displayed gap. Cross-sum defects show that no word of
length one or two resets and that these are exactly the length-three reset
words.

### 2. Finite-time transfer

If a transition with reward `r` is weighted by `y^r`, the row-oriented
kernel is

```text
Q_p(y) = [[0, p/y, qy],
          [py, 0, qy],
          [py, q/y, 0]].
```

The initial state is `Z`, hence

```text
E[y^H_n] = e_Z^T Q_p(y)^n 1.
```

A determinant expansion groups the three two-cycles and two three-cycles:

```text
det(rI-Q_p(y))
 = r^3 - (p^2+q^2+pq y^2)r - pq y
 = r^3 + (2a-1-a y^2)r - a y,
a=pq.
```

### 3. Drift and variance

At zero tilt, balance gives

```text
pi_N=p/(1+p),
pi_Z=(1-a)/(2+a),
pi_P=q/(1+q).
```

Only `N --A--> Z` and `P --B--> Z` carry reward `-1`, so

```text
mu = 1 - 2[p pi_N + q pi_P] = 3a/(2+a).
```

Let `f_i` be the conditional mean reward. The exact Poisson solution

```text
h_N=-2p/(1+p),  h_Z=0,  h_P=-2q/(1+q)
```

satisfies `(I-P)h=f-mu`. Therefore

```text
D_k = reward_k - mu + h(S_k)-h(S_(k-1))
```

is a bounded martingale difference. Its stationary second moment simplifies
to

```text
sigma^2 = 4a(1-a)(5-2a)/(2+a)^3.
```

The Perron cubic yields `rho'(0)=mu` and
`(log rho)''(0)=sigma^2`; the manuscript displays the partial derivatives
and the simplification. Conditional on the already derived kernel, the
second variance calculation is independent of the Poisson calculation.

### 4. Word geometry and pressure edges

Every reward is `+1` or `-1`. A negative reward always returns the chain to
`Z`, and the next reward from `Z` is positive. Hence negative rewards are
isolated:

```text
n mod 2 <= H_n <= n.
```

Every parity-compatible value is attained. For height `n-2k`, use the
prefix `(AA)^k`, whose `(+1,-1)` reward blocks return to `Z`, and append an
alternating suffix of length `n-2k`, whose rewards are all positive.

Avoiding every negative reward forces alternation after the first letter, so
exactly two words attain `H_n=n` for `n>=1`. Constant words attain the lower
bound.

For the positive edge, `Q_p(y)/y` converges to a matrix with spectral radius
`sqrt(pq)`. For the negative edge, with
`D_y=diag(y^(-1),1,y^(-1))`,

```text
D_y^(-1) Q_p(y) D_y
 -> [[0,p,0],[p,0,q],[0,q,0]],
```

whose spectral radius is `sqrt(p^2+q^2)=sqrt(1-2pq)`. These are identities
and finite-dimensional spectral limits, not approximations.

## Interpretation

Switching changes the projective itinerary. Each generator alone repeats a
two-cycle with zero average height reward, but a nondegenerate mixture visits
cross-generator transitions that raise the stationary reward average to
`3pq/(2+pq)`. The effect is switching-induced growth, not physical
stochastic resonance. Rank-one reset words do occur and place the pair
inside classical max-plus coupling/memory-loss territory; the pair-specific
contribution is the explicit finite kernel and formulas, not the reset
mechanism.

## Boundaries and non-claims

- Generic max-plus/topical SLLNs, CLTs, LDPs, memory loss, and Perron methods
  are prior framework, not contributions.
- Max-plus automata, random Lyapunov exponents, projective semigroups,
  reset/coupling methods, switching models, and Markov-jump systems are also
  directly owner-subtracted; the bibliography records the named sources.
- Row/column scalings, permutations, transpose, and additive normalization
  have not been exhaustively quotiented, so no equivalence-class claim is
  made.
- The exact finite computation does not prove limit theorems or novelty.
- The pressure is the scalar height pressure for this pair; no claim is made
  about arbitrary max-plus matrix products.
- At `p=0,1`, the stationary interior formulas are not used as proofs even
  though their algebraic limits are zero.
- Public release, submission, novelty, and priority remain HOLD.

## Open risks

- A specialist owner search must precede external use of the literal-pair
  conjunction.
- This is an author revision after two hostile reviews, not final QA.
- Internal distinction from prior papers must remain visible at the update,
  observable, and proof-engine levels.
