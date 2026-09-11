# Root focused scout — random-permutation fixed-point sieve (`RPS`)

**Date:** 2026-09-03 UTC  
**Route:** A, stochastic finite/rank-changing dynamics  
**Author-side decision:** `AMBER_HIGH_PENDING_INDEPENDENT_HOSTILE_GATE`  
**External state:** `HOLD_EXTERNAL`

## Outcome first

Fix `n>=2`.  The phase space is the Boolean lattice `2^[n]`.  From a current
set `A`, sample an independent uniform permutation `pi in S_n` and update

```text
A -> A intersect Fix(pi).                              (1)
```

The process is a dependent-coordinate sieve, not independent thinning: a
permutation cannot have exactly `n-1` fixed points.  Its subset-containment
indicators nevertheless give a complete eigenbasis.  This produces an exact
all-time/every-endpoint kernel, the absorption PGF and moments, a sharp tail,
and a cycle-marked history polynomial that retains the symmetric-group
structure discarded by the unmarked chain.

Ordinary rencontres numbers, inclusion--exclusion, the cycle index of `S_n`,
and common fixed-point counts receive zero contribution.  Word-measure work
explicitly studies common fixed points of random permutations and is a serious
owner neighbour.  The proposed residual is therefore amber until a hostile
review decides whether the integrated Markov/spectral/history package is
paper-sized after that subtraction.

## 1. All-time every-endpoint histories

Let `A_t` be the state after `t` updates, start at `A`, and fix `B subset A`.
Put `a=|A|`, `b=|B|`.  Inclusion--exclusion over the points of `A\B` gives
the exact number of permutation histories with endpoint `B`:

```text
H_t(A,B)=sum_(j=0)^(a-b) (-1)^j C(a-b,j)(n-b-j)!^t.   (2)
```

The value is zero when `B` is not a subset of `A`.  Division by `(n!)^t`
gives the transition probability.  Formula (2) is valid at `t=0`, where it
is the Kronecker delta.

For every positive time the support has one exact obstruction:

```text
P^t(A,B)>0  iff  B subset A
and not (A=[n] and |B|=n-1).                          (3)
```

The exceptional target would force every sampled permutation to fix `n-1`
points and hence the last point.  Every other endpoint is realized already
at one step, using a derangement on `A\B` or a transposition with a point
outside `A` in the singleton-loss case.

## 2. Full diagonalization and absorption

For each `S subset [n]`, set `phi_S(A)=1[S subset A]`.  Then

```text
P phi_S = lambda_|S| phi_S,
lambda_r=(n-r)!/n!.                                   (4)
```

Indeed `S` survives one epoch precisely when the sampled permutation fixes
every point of `S`.  The `2^n` containment indicators form the Boolean-zeta
basis, so (4) is a complete diagonalization (repeated numerical eigenvalues
remain equipped with their explicit basis vectors).

Let `T` be the first time at the empty set and start from a nonempty set of
size `a`.  Then

```text
P(T<=t)=sum_(j=0)^a (-1)^j C(a,j) lambda_j^t,          (5)

E T=sum_(j=1)^a (-1)^(j+1) C(a,j)/(1-lambda_j),       (6)

E T^2=sum_(j=1)^a (-1)^(j+1) C(a,j)
             (1+lambda_j)/(1-lambda_j)^2.             (7)
```

Equivalently, for `|s|<lambda_1^(-1)`,

```text
E[s^T]=1-(1-s) sum_(j=1)^a
          (-1)^(j+1) C(a,j)/(1-s lambda_j).           (8)
```

For `n>=3`, the survival tail has the sharp first two scales

```text
P(T>t)=a n^(-t)-C(a,2)[n(n-1)]^(-t)
        + O(lambda_3^t).                              (9)
```

The exact finite sum preceding (9) handles all small boundaries.  At `n=2`,
`lambda_1=lambda_2=1/2`, so the combined leading coefficient must be used.
At `n=1`, the nonempty state is absorbing; this is why the paper family is
stated for `n>=2`.

The singleton self-loop probability is `1/n`, so the labelled transition
atlas recovers `n` without using the visible phase cardinality `2^n`.

## 3. Cycle-marked every-history refinement

The unmarked kernel forgets how each sampled permutation is assembled.  Let
`cyc(pi)` be its number of cycles and define

```text
H_t(A,B;u)=sum_(histories A_t=B) u^(sum_r cyc(pi_r)). (10)
```

If `s` prescribed letters must be fixed, the cycle enumerator of the
permutations is

```text
R_(n,s)(u)=u^s u^(overline(n-s)),                     (11)
```

where `u^(overline m)=u(u+1)...(u+m-1)` and the empty
product is one.  The marked analogue of (2) is

```text
H_t(A,B;u)=sum_(j=0)^(a-b) (-1)^j C(a-b,j)
                         R_(n,b+j)(u)^t.              (12)
```

Although (12) is alternating, its coefficients are nonnegative because it
counts literal histories.  It is target-sensitive through `b`, valid at all
times, and specializes to (2) at `u=1`.  Separate variables for the `t`
epochs follow by replacing the power in (12) by a product; the one-variable
form is sufficient for the proposed short paper.

## 4. Proof and collision ceiling

Zero-credit material:

- the rencontres distribution and derangement inclusion--exclusion;
- the probability `(n-r)!/n!` that prescribed points are fixed;
- the unsigned Stirling/cycle-index identity (11);
- generic diagonalization by zeta/Möbius bases on the Boolean lattice;
- generic absorbing-chain manipulations from a spectral expansion.

The permitted residual, if the owner gate accepts it, is only the conjunction
for the literal sieve: exact endpoint kernel and its single support hole,
explicit containment eigenbasis, absorption transform/moments and boundary
tail, and the all-time cycle-marked history refinement.

Nearest internal systems are deliberately separated:

- P158 intersects a graph with random cuts; complementary binary histories
  and labelled graph endpoints govern its fibres.  `RPS` evolves subsets by
  dependent fixed sets and is diagonalized by symmetric-group stabilizers.
- current `RTI` intersects a subset of `F_2^d` with random translates; its
  history compresses to a random subspace rank and its target stabilizer.
  `RPS` has no spatial translations, span rank, or affine-coset product.
- P136 is a random cover process on sunflower forests; P151 is a first-passage
  walk on spiders.  Neither provides (2), (4), or (12).

## 5. Exact evidence

Run

```text
python3 docs/papers162_166_sequence/scouting/root_random_permutation_sieve/verify_scout.py
```

The verifier builds the literal transition matrix by enumerating all
permutations through `n=7`; compares six powers with (2) at every ordered
source/target pair; checks every containment eigenvector; and independently
solves the triangular absorption recurrences for (5)--(7).  Through `n=5`, it
also enumerates permutations by cycle count and compares three marked matrix
powers coefficientwise with (12).  The frozen run makes `217,551` exact
assertions and ends in `STATUS PASS`.

Enumeration is bounded falsification evidence, not a proof or owner
certificate.

## Author-side gate

```text
RPS  AMBER_HIGH_PENDING_INDEPENDENT_HOSTILE_GATE
HOLD_EXTERNAL
```
