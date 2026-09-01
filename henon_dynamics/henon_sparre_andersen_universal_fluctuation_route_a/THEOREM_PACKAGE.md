# Proof Package

## Claim

Let `X_1,X_2,...` be iid real random variables with a continuous distribution
symmetric about zero, and put

$$
S_0=0,\qquad S_n=X_1+\cdots+X_n.
$$

Define

$$
q_0=1,\qquad q_n=\mathbb P(S_1>0,\ldots,S_n>0),
$$

the first strict descent

$$
\tau^-:=\inf\{n\geq1:S_n<0\},
$$

the positive partial-sum count

$$
N_n:=\#\{1\leq j\leq n:S_j>0\},
$$

and the almost-surely unique maximum time

$$
M_n:=\operatorname*{arg\,max}_{0\leq j\leq n}S_j.
$$

Then, for all `n>=0`,

$$
q_n=\frac{\binom{2n}{n}}{4^n},\qquad
\sum_{n\geq0}q_nz^n=(1-z)^{-1/2}\quad(|z|<1).
$$

For `n>=1`,

$$
\mathbb P(\tau^->n)=q_n,
\qquad
\mathbb P(\tau^-=n)=q_{n-1}-q_n=\frac{q_{n-1}}{2n}.
$$

For `0<=k<=n`,

$$
\mathbb P(N_n=k)=\mathbb P(M_n=k)=q_kq_{n-k}.
$$

Finally, both `N_n/n` and `M_n/n` converge weakly to the
`Beta(1/2,1/2)` law with density

$$
\frac{1}{\pi\sqrt{x(1-x)}}\,\mathbf 1_{(0,1)}(x).
$$

If continuity is removed, these formulas need not survive under either the
strict or nonnegative convention, and the maximum can fail to be unique.

## Status

**PROVABLE AS STATED**

## Assumptions

- The increments are iid.
- Their common law is symmetric about zero.
- Their common law is continuous.
- Strict positivity and strict descent use exactly the inequalities displayed
  above.

## Notation

- `Q(z)=sum_{n>=0}q_n z^n`.
- `(a)_n` is not used; every binomial coefficient has its usual integer
  meaning.
- `M_n` includes time zero among the candidate maximum times.

## Proof Strategy

First factor the event that the unique maximum occurs at time `k` into an
independent reversed premaximum survival event and a postmaximum negative
survival event.  Summing over `k` forces a convolution identity, which uniquely
determines the square-root generating function and hence every `q_n`.  The
Sparre–Andersen permutation-cycle lemma supplies the bivariate generating
function for `N_n`.  Coefficient extraction gives the second arcsine law.
Central-binomial asymptotics then give the common weak limit.  A two-step
atomic walk separates the excluded boundary.

## Dependency Map

1. Continuity implies no partial-sum ties and a unique maximum.
2. Independence and symmetry imply the pre/post maximum factorization.
3. Factorization plus total probability imply `Q(z)^2=(1-z)^(-1)`.
4. The positive-count law uses the permutation-cycle lemma under the same
   no-ties condition.
5. The first-descent law uses only the survival identity and the exact ratio
   `q_n/q_{n-1}`.
6. The scaling law uses central-binomial asymptotics and endpoint bounds.
7. The atomic counterexample is a direct four-path enumeration.

## Proof

### Step 1: no ties

For `0<=j<k`, the difference `S_k-S_j` is a sum of `k-j` independent
increments.  Its distribution is continuous, so
`P(S_k=S_j)=0`.  A finite union over pairs proves that
`S_0,...,S_n` are distinct almost surely.  In particular, `M_n` is unique and
`P(S_j=0)=0` for every positive `j`.

### Step 2: factor the maximum time

Fix `0<=k<=n`.  The event `M_n=k` is the intersection of

$$
S_k-S_{k-j}>0\quad(1\leq j\leq k)
$$

and

$$
S_{k+j}-S_k<0\quad(1\leq j\leq n-k).
$$

The first collection is the strict-survival event for the reversed block
`X_k,X_{k-1},...,X_1`.  Reversal preserves the joint iid law, so its
probability is `q_k`.  The second collection depends only on
`X_{k+1},...,X_n`.  After multiplying this block by `-1`, symmetry turns it
into a strict-survival event of length `n-k`, with probability `q_{n-k}`.
The two blocks are independent.  Therefore

$$
\mathbb P(M_n=k)=q_kq_{n-k}. \tag{1}
$$

### Step 3: determine the survival generating function

The unique maximum occurs at exactly one time, so summing (1) gives

$$
\sum_{k=0}^n q_kq_{n-k}=1\qquad(n\geq0). \tag{2}
$$

As a formal power-series identity, (2) is

$$
Q(z)^2=\frac{1}{1-z}.
$$

Because `Q(0)=q_0=1`, the positive square-root branch is forced:

$$
Q(z)=(1-z)^{-1/2}.
$$

The binomial series now yields

$$
q_n=\frac{\binom{2n}{n}}{4^n}. \tag{3}
$$

This argument proves universality without sampling any particular continuous
increment density.

### Step 4: positive partial sums

We use the Sparre–Andersen permutation-cycle lemma.  For iid increments whose
partial sums have no ties, it states the formal identity

$$
1+\sum_{n\geq1}z^n\mathbb E[u^{N_n}]
=\exp\!\left[
\sum_{m\geq1}\frac{z^m}{m}
\left(\mathbb P(S_m<0)+u^m\mathbb P(S_m>0)\right)
\right]. \tag{4}
$$

For completeness, the combinatorial mechanism behind (4) is as follows.
Condition on an increment vector in general position and average over all of
its permutations.  Write each permutation in disjoint cycles.  Rotate a cycle
at its unique extremal partial sum: a cycle with positive total contributes its
full length to the positive-partial-sum statistic, while a cycle with negative
total contributes zero.  Ordering the rotated cycles by their extremal levels
is a bijection back to linear increment orderings.  The labeled-cycle
exponential formula contributes the factor `1/m` for a cycle of length `m`.
Averaging over iid increments replaces the two cycle signs by
`P(S_m>0)` and `P(S_m<0)`, which gives (4).  Continuity supplies every
uniqueness assertion used by the rotation.

Symmetry and Step 1 give
`P(S_m>0)=P(S_m<0)=1/2`.  Thus (4) becomes

$$
1+\sum_{n\geq1}z^n\mathbb E[u^{N_n}]
=\frac{1}{\sqrt{(1-z)(1-uz)}}
=\left(\sum_{a\geq0}q_az^a\right)
  \left(\sum_{b\geq0}q_b(uz)^b\right). \tag{5}
$$

The coefficient of `z^n u^k` in (5) is `q_kq_{n-k}`.  Hence

$$
\mathbb P(N_n=k)=q_kq_{n-k}=\mathbb P(M_n=k).
$$

### Step 5: first strict descent

By Step 1, strict positivity and nonnegativity agree almost surely.  Therefore

$$
\{\tau^->n\}=\{S_1>0,\ldots,S_n>0\}
$$

up to a null set, so `P(tau^->n)=q_n`.  Taking consecutive differences gives
`P(tau^-=n)=q_{n-1}-q_n`.  Formula (3) also gives

$$
\frac{q_n}{q_{n-1}}=\frac{2n-1}{2n},
$$

and hence the displayed `q_{n-1}/(2n)` formula.

### Step 6: arcsine scaling

Stirling's formula gives

$$
q_m\sim\frac{1}{\sqrt{\pi m}}.
$$

Uniformly for `x` in a compact subinterval of `(0,1)` and
`k=floor(nx)`,

$$
nq_kq_{n-k}\longrightarrow
\frac{1}{\pi\sqrt{x(1-x)}}. \tag{6}
$$

To control the endpoints, the central-binomial bound
`q_m<=C/sqrt(m+1)` implies, for `0<epsilon<1/2`,

$$
\sum_{k\leq\epsilon n}q_kq_{n-k}
\leq C'\sqrt{\epsilon},
$$

uniformly in `n`; symmetry gives the same bound near one.  Equation (6) and a
Riemann-sum argument on `[epsilon,1-epsilon]`, followed by
`epsilon` tending to zero, prove weak convergence to the arcsine density.
Both `N_n` and `M_n` have the same finite-`n` law, so both converge.

### Step 7: atomic failure boundary

Let each increment equal `+1` or `-1` with probability `1/2`.  At `n=2`, the
four paths `++,+-,-+,--` give nonnegative survival probability `2/4`, whereas
the continuous universal value is `q_2=3/8`.  Under strict positivity the
positive-count histogram is `(2,1,1)/4`, not `(3,2,3)/8`, and the path `-+`
has a tied maximum at times zero and two.  Thus continuity cannot be removed
without changing conventions and formulas.

The claim follows. ∎

## Corrections or Missing Assumptions

None.  The no-ties assumption is explicit and is essential.

## Open Risks

- The theorem is intentionally restricted to iid continuous symmetric
  increments; broader exchangeable variants are not claimed.
- Finite exact enumeration audits the formulas but does not replace the
  permutation-cycle proof.
