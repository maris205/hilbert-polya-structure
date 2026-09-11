# Coordinator scout — random internal-matching retention

**State:** `RESERVE_BEHIND_G05 / HOLD_EXTERNAL`  
**Carrier:** subsets of a labelled set of even order `N=2m`.

At every epoch sample a fresh uniform perfect matching `M` of `[N]` and
replace `A` by the set of vertices whose matching partner also lies in `A`.
Equivalently, retain the endpoints of all edges of `M[A]`.  The state is
nested, but it loses an even number of vertices only after the first step.

## Exact target kernel

Let `B subseteq A`, `a=|A|`, and `b=|B|`.  Write

```text
P(r)=(r-1)!! for even r>=0, with P(0)=1, and P(r)=0 otherwise.
```

The exact number of perfect matchings producing the labelled endpoint `B` is

```text
C_N(a,b)=1_(b even) P(b) (N-a)_(a-b) P(N-2a+b).       (1)
```

Indeed, `B` must be internally matched; every vertex of `A\B` must be sent
injectively across the cut to `[N]\A`; and the unused outside vertices are
then internally matched.  Division by `P(N)` gives the labelled transition.
Consequently the size quotient is

```text
Q_ab=binom(a,b) C_N(a,b)/P(N),                         (2)
```

and relabelling equivariance plus nesting gives, for every `t>=0`,

```text
Pr(A_t=B | A_0=A)=1_(B subseteq A) (Q^t)_ab/binom(a,b). (3)
```

Thus the proposed inverse axis resolves every labelled target at every time,
not just the number of retained matching edges.

## Complementary spectrum

The diagonal layer value is zero for odd `a`, while for even `a`

```text
lambda_a=P(a)P(N-a)/P(N).                              (4)
```

The nonzero values satisfy `lambda_a=lambda_(N-a)` and strictly decrease as
even `a` approaches `N/2`.  In the size quotient, every complementary
interior even pair `a,N-a` contributes a genuine `J_2` block.  A direct proof
uses the positive adjacent transitions `k -> k-2`: the eigenvector recursion
through the intervening strictly smaller diagonal values reaches the repeated
upper layer with a nonzero compatibility obstruction.  The zero eigenvalue is
semisimple after ordering even layers before odd layers, because every update
lands in an even layer and the even-layer block is invertible.  The eigenvalue
one has two separate one-dimensional blocks, belonging to `emptyset` and the
full set.

Every proper nonempty state reaches `emptyset` almost surely; the full set is
an isolated fixed state.  The absorption CDF and mean are respectively
`(Q^t)_(a,0)` and the usual finite triangular recursion.  Polynomial-times-
exponential terms are forced by the complementary Jordan blocks.

## Boundary and exact pressure

- `N=2` has no transient complementary pair.
- `N=4` has one transient even layer and no repeated interior value.
- `N=6` is the first `J_2`, from dimensions two and four.
- Unsupported targets include every odd `B` and every `B` for which
  `a-b>N-a`.

`verify_matching_internal.py` exhausts all subsets and every perfect matching
through `N=8`, checks (1) target by target, checks stochastic row sums through
`N=10`, and verifies the predicted Jordan nullities in exact rational
arithmetic.  It makes 7,764 deterministic assertions.

## Owner and collision gate

Internal-edge counts of a random perfect matching, double-factorial matching
enumeration, matching association schemes, and generic triangular Markov-chain
algebra receive zero credit.  The bounded search found many uses of the
internal/crossing-edge distribution for a fixed subset, but no literal
resampled subset dynamics or complementary-Jordan statement.  That is only a
non-hit.

The principal problem is internal value overlap.  `G05` has the same
complementary-dimension resonance on a subspace lattice, with a stronger
ambient-map fibre; P170 already occupies a symmetric-group marked subset
erosion; and the old `PMI` reserve occupies repeated perfect-matching
intersection.  Therefore this candidate is not currently selectable beside
`G05`.  It is retained as a mathematically complete replacement reserve, not
as a sixth paper or a novelty claim.
