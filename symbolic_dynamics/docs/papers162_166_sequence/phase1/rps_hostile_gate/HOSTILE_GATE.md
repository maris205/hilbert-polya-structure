# RPS fresh independent hostile gate

**Object:** `A -> A intersect Fix(pi)` for independent uniform
`pi in S_n`  
**Review date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Decision:** **`KILL_ROUTINE_OWNER_AND_PORTFOLIO_COLLISION`**  
**Mathematical findings:** `0 Critical / 0 Major / 1 minor`

## 1. Outcome first

The advertised exact formulas are almost all correct.  A fresh literal
verifier confirms the complete endpoint kernel, its positive-time support
hole, the Boolean-zeta eigenbasis (including repeated eigenvalues), the
absorption CDF/PGF/first two moments, the cycle-marked history formula, and
the singleton recovery probe.  One boundary sentence needs repair: at
`n=3`, as well as `n=2`, two displayed factorial eigenvalues coalesce, so
the claimed sharp two-scale tail is not separated.

Correctness does not clear the value gate.  After owner subtraction, the
package has no paper-sized independent residual:

1. the state after `t` epochs is simply the initial set intersected with the
   common fixed set of `t` independent random permutations;
2. common fixed points of random symmetric-group images are explicitly
   inside the Puder/word-measure program;
3. the exact labelled fixed-set law is elementary prescribed-fixed-point
   inclusion--exclusion in the Diaconis fixed-set neighbourhood;
4. the zeta spectrum is a direct instance of random walks on a finite
   meet-semilattice/left regular band; and
5. the cycle mark merely replaces `(n-s)!` by the classical prescribed-fixed
   cycle polynomial before applying the same inclusion--exclusion.

The Markov packaging, hitting transform, and parameter probe do not form a
new proof axis after these deductions.  RPS is therefore **KILL**, not amber.
It should **not coexist with RTI**: both are monotone random-meet processes on
Boolean carriers, while RTI has the genuinely additional target-stabilizer
weighted inverse atlas that RPS lacks.

## 2. Exact independent derivation

Let `A_0=A`.  For independent permutations `pi_1,...,pi_t`, repeated use of
intersection gives the pathwise identity

```text
A_t = A intersect Fix(pi_1) intersect ... intersect Fix(pi_t).     (1)
```

No new statistic is created by the sequential presentation: the endpoint
is the common fixed set of the history, restricted to `A`.

### 2.1 Every-time, every-endpoint kernel

Fix `B subseteq A`, with `a=|A|`, `b=|B|`.  Every point in `B` must be fixed
by all `t` permutations, while every point of `A\B` must fail to be common
fixed.  If a chosen `j`-subset of `A\B` is additionally required to be
fixed by every permutation, each epoch has `(n-b-j)!` choices.  Boolean
inclusion--exclusion yields

```text
H_t(A,B)=sum_(j=0)^(a-b) (-1)^j binom(a-b,j)(n-b-j)!^t.     (2)
```

If `B` is not a subset of `A`, the count is zero.  At `t=0`, every factorial
is raised to the zeroth power and the alternating binomial sum is
`1[A=B]`, so (2) really includes the identity-time boundary.

For `t>=1`, a nonempty fibre exists for every `B subseteq A` except

```text
A=[n] and |B|=n-1.                                         (3)
```

Necessity follows because a permutation fixing `n-1` points fixes the last
one.  For sufficiency, if at least two points must be lost, derange those
points and fix the rest; if exactly one point must be lost and `A` is not
full, transpose it with a point outside `A`; if no point is lost, use the
identity.  One realizing epoch followed by identities realizes every
positive time.  This proves both directions of (3), including `n=1`.

### 2.2 Boolean-zeta diagonalization and repeated eigenvalues

For `S subseteq [n]`, define

```text
phi_S(A)=1[S subseteq A].
```

Writing `P` for the one-step Markov operator,

```text
(P phi_S)(A)
 = 1[S subseteq A] Pr(pi fixes S)
 = ((n-|S|)!/n!) phi_S(A).                                 (4)
```

The containment matrix is the Boolean zeta matrix.  Its inverse is the
Boolean Möbius matrix, so the `2^n` functions `phi_S` form a basis.  Thus
(4) is a complete diagonalization with

```text
lambda_r=(n-r)!/n!.
```

Repeated numerical eigenvalues do not destroy diagonalizability.  They must,
however, be stated correctly: for every `n>=2`,

```text
lambda_(n-1)=lambda_n=1/n!
```

and this eigenspace has the explicit `n+1` zeta-basis vectors of ranks
`n-1` and `n`.  At `n=1`, both eigenvalues equal one.

### 2.3 Absorption transform, moments, and exact boundaries

Let `T=min{t:A_t=empty}` and start from a nonempty `a`-set.  Substituting
`B=empty` in (2) and dividing by `(n!)^t` gives

```text
Pr(T<=t)=sum_(j=0)^a (-1)^j binom(a,j) lambda_j^t.           (5)
```

Therefore

```text
Pr(T>t)=sum_(j=1)^a (-1)^(j+1) binom(a,j) lambda_j^t.       (6)
```

For `n>=2`, every `lambda_j<1` when `j>=1`.  Summing (6), using
`E[T^2]=sum_(t>=0)(2t+1)Pr(T>t)`, and applying the standard tail/PGF
identity gives

```text
E T = sum_(j=1)^a (-1)^(j+1) binom(a,j)/(1-lambda_j),       (7)

E T^2 = sum_(j=1)^a (-1)^(j+1) binom(a,j)
                         (1+lambda_j)/(1-lambda_j)^2,       (8)

E[s^T] = 1-(1-s) sum_(j=1)^a
            (-1)^(j+1) binom(a,j)/(1-s lambda_j).           (9)
```

Equation (9) is initially valid for `|s|<lambda_1^(-1)` and also specifies
the corresponding rational continuation.  For the empty initial state it
is replaced by the boundary value one.

The small ranks are:

- `n=1`: the nonempty state is absorbing, so finite absorption formulas do
  not apply;
- `n=2`: `lambda_1=lambda_2=1/2`, and
  `Pr(T>t)=(a-binom(a,2))2^(-t)`;
- `n=3`: `lambda_2=lambda_3=1/6`, and
  ```text
  Pr(T>t)=a 3^(-t)
           -(binom(a,2)-binom(a,3))6^(-t);                 (10)
  ```
- `n>=4`: the first two scales are genuinely separated:
  ```text
  Pr(T>t)=a n^(-t)-binom(a,2)[n(n-1)]^(-t)+O(lambda_3^t).  (11)
  ```

The exact finite sum (6) is valid in all cases.

### 2.4 Minor finding RPS-m1: the `n=3` tail was not sharp as stated

The source contract calls (11) the “sharp first two scales” for `n>=3` and
mentions only the `n=2` collision.  At `n=3`, however,
`lambda_2=lambda_3=1/6`.  When `a=3`, for example, the true coefficient of
`6^(-t)` is `-3+1=-2`, not `-3`.  The displayed big-O equality is still a
loose true bound because its remainder is of the same scale, but its claimed
second coefficient is not a sharp asymptotic coefficient.

Required repair: state (11) for `n>=4` and insert the exact `n=3` branch
(10).  This is minor because (6) already contains the correction.

### 2.5 Cycle-marked histories

If `s` prescribed labels must be fixed, those labels contribute `s`
one-cycles and the remaining labels are arbitrary.  The unsigned Stirling
cycle enumerator gives

```text
R_(n,s)(u)=u^s product_(k=0)^(n-s-1)(u+k).                  (12)
```

Applying the same Boolean inclusion--exclusion used in (2), independently
at the level of cycle weights, gives

```text
H_t(A,B;u)=sum_(j=0)^(a-b) (-1)^j binom(a-b,j)
                              R_(n,b+j)(u)^t.               (13)
```

It is valid at `t=0`, has nonnegative coefficients because it is the literal
history enumerator, and specializes to (2) at `u=1`.  Formula (13) is
correct.  It is not an independent proof engine: it is exactly formula (2)
with the classical scalar prescribed-fixed count replaced by its equally
classical cycle polynomial.

### 2.6 Parameter recovery

From a singleton source, the unique nonempty endpoint is the same singleton.
Its self-loop probability is

```text
(n-1)!/n! = 1/n.                                           (14)
```

Thus the labelled one-step kernel recovers `n`.  The claim is correct but
the probe is a one-line marginal of (2)/(4), and phase cardinality already
exposes `n`; it supplies no independent theorem value.

## 3. Fresh verifier

`verify_hostile.py` uses only the Python standard library and imports no RPS
author code.  It independently:

- enumerates every literal permutation through `n=7` and reconstructs all
  labelled subset transition rows;
- compares times `0,...,5` with (2) for every ordered source/target pair and
  verifies the exact positive-time support hole;
- checks `M Z=Z D`, constructs and checks the Boolean Möbius inverse, and
  records the repeated eigenspaces;
- projects the literal chain to cardinalities, solves its rational moment and
  PGF recurrences, and compares (5)--(9), including `n=1,2,3`;
- constructs cycle-marked transition powers through `n=5`, time three, and
  compares every coefficient with (12)--(13); and
- verifies the singleton recovery map through `n=12`.

The canonical run has `331,278` exact assertions.  This is bounded
counterexample pressure, not a proof or owner certificate.

## 4. Owner/value and portfolio decision

The focused sources and exact subtraction are recorded in `OWNER_AUDIT.md`.
The decisive point is structural: RPS is multiplication by an i.i.d. random
element of the finite commutative idempotent semigroup `(2^[n], intersect)`.
Its spectrum, Möbius inversion, and absorption manipulation are instances of
the established semigroup-walk framework.  Its driving random element is a
fixed set of a uniform permutation; the `t`-fold product is precisely a
common fixed set, already a named object in the word-measure literature.

After those two owners are subtracted, (2) is prescribed-fixed-point
inclusion--exclusion, (13) is its cycle-index marking, and (14) is a marginal.
There is no remaining independent target geometry, inverse atlas, extremal
classification, or nonstandard stochastic statistic.

### Coexistence with RTI

`RPS` and `RTI` have different acting groups, but coexistence is not justified
at this batch's threshold.  Both are random intersections on Boolean state
spaces whose histories collapse to a cumulative algebraic object.  RTI then
adds a nontrivial target stabilizer/coset source polynomial; RPS stops at the
generic meet-walk kernel and a classical cycle decoration.  Keeping both
would duplicate the stochastic-intersection silhouette while selecting the
weaker package.

```text
RPS KILL_ROUTINE_OWNER_AND_PORTFOLIO_COLLISION
MAY_COEXIST_WITH_RTI NO
HOLD_EXTERNAL
```

No author file, paper, central ledger, or Git state was changed.

