# Random q-colour refinement (RCR): exact scout and strict value gate

**Scout date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Decision:** **`KILL_CLASSICAL_PAINTBOX_FRAGMENTATION_AND_DECORATIVE_COLUMN_MARKING`**  
**Exact audit:** `0` mathematical counterexamples; `4,012,464` independent
assertions; two fresh canonical replays byte-matched

## 1. Outcome first

The proposed process is completely soluble.  Its cumulative random input is
one uniform `q^t`-colouring; every source-to-target probability is a product
of falling factorials; absorption and the total block count reduce to finite
occupancy; and the partition-lattice zeta basis diagonalizes the whole Markov
operator with eigenvalues `q^(k-n)` of multiplicity `S(n,k)`.

The requested target-sensitive history polynomial also exists.  If a target
has block sizes `(s_1,...,s_k)`, group its block indices into prospective
source blocks.  A group `G` contributes `(q^t)_(|G|)` histories and source
size `sum_(i in G) s_i`.  Marking the extra equal pairs distinguishes, for
example, targets of types `(3,1)` and `(2,2)`, even though their unweighted
columns agree.

Those successes do **not** pass the paper gate.  Two classical interfaces own
the dynamics:

1. the one-block initial condition is precisely the common refinement of
   kernel partitions of iid uniform maps, directly studied by Krachun and
   Yakubovich (their alphabet has size `n`); and
2. from an arbitrary partition, the transition kernel is exactly the finite
   uniform-paintbox instance of the standard blockwise fragmentation kernel.

The spectrum is a direct meet-semilattice/left-regular-band specialization.
The new weighted polynomial is a marked column transform of the already known
full transition kernel, with no unexpected product, target obstruction,
extremum, or inverse classification.  After zero-credit subtraction, it is
not a genuinely independent second theorem axis.  This is therefore a strict
**owner/value kill**, not a mathematical-failure kill.

## 2. Literal system and conventions

Fix integers `n>=1` and `q>=2`.  Let `Pi_n` be the set of partitions of
`[n]`.  Write

```text
sigma <= pi
```

when `sigma` refines `pi`.  At each epoch choose independently and uniformly
a colouring

```text
c : [n] -> [q]
```

and update

```text
T_c(pi) = pi meet ker(c).                                  (2.1)
```

Here the meet is common refinement.  The discrete partition is denoted
`delta`; it is the unique absorbing state.  Falling factorials and Stirling
numbers use

```text
(x)_j = x(x-1)...(x-j+1),       S(b,j) = Stirling2(b,j),
(x)_0 = 1.
```

All formulas below include `t=0`.  Put `Q=q^t`, so `Q=1` at time zero.

## 3. Cumulative signature theorem

Let `c_1,...,c_t` be a colour history and attach to each element its signature

```text
a(x) = (c_1(x),...,c_t(x)) in [q]^t.                       (3.1)
```

Associativity and commutativity of meet give pathwise

```text
T_(c_t)...T_(c_1)(pi) = pi meet ker(a).                    (3.2)
```

Identifying `[q]^t` with an alphabet of size `Q`, histories are in bijection
with all functions `a:[n]->[Q]`.  Thus the entire `t`-step law is one uniform
`Q`-colour refinement.  No stochastic approximation is involved.

At `t=0`, the empty signature is constant, `ker(a)` is the one-block
partition, and (3.2) is the identity.

## 4. Every-source/every-target transition theorem

Fix `pi,sigma in Pi_n`.  If `sigma<=pi`, let

```text
k_B = number of sigma-blocks contained in the pi-block B.  (4.1)
```

Then the exact number of length-`t` colour histories sending `pi` to `sigma`
is

```text
N_t(pi,sigma)
 = 1_{sigma<=pi} product_(B in pi) (Q)_(k_B).              (4.2)
```

Consequently

```text
P^t(pi,sigma)
 = 1_{sigma<=pi} q^(-tn) product_(B in pi) (q^t)_(k_B).   (4.3)
```

### Proof

For (3.2) to equal `sigma`, the signature must be constant on every
`sigma`-block.  Inside a fixed source block `B`, its `k_B` target blocks must
receive pairwise distinct signatures; there are `(Q)_(k_B)` assignments.
Different source blocks impose no cross-condition, because `pi` already
separates them, so signatures may be reused and the factors multiply.  A
non-refining target is impossible.  This proves (4.2), and there are `Q^n`
histories in total.

The support is therefore exact:

```text
supp P^t(pi,.)
 = {sigma<=pi : k_B<=q^t for every B in pi}.               (4.4)
```

It is the full lower interval below `pi` as soon as
`q^t >= max_(B in pi)|B|`.  The row-mass identity is

```text
sum_(sigma<=pi) product_B (Q)_(k_B) = Q^n,                 (4.5)
```

which also follows by partitioning all signatures according to their kernels
inside the source blocks.

At `t=0`, `(1)_k` vanishes for `k>1`, so only `sigma=pi` has mass one.  This
checks the boundary without an exception clause.

## 5. Absorption distribution and exact mean

Suppose the source blocks of `pi` have sizes `b_1,...,b_m`.  Absorption by
time `t` means that every source block receives distinct signatures.  Hence

```text
F_pi(t) := Pr_pi(tau<=t)
 = product_(i=1)^m (Q)_(b_i) / Q^(b_i),       Q=q^t.       (5.1)
```

The factors are independent because the signatures on disjoint source blocks
are independent.  Formula (5.1) covers the discrete source: every `b_i=1`,
so `F_delta(0)=1` and `tau=0`.

For an exact finite expression for the expectation, expand

```text
A_pi(x) := product_i (x)_(b_i) = sum_(j=m)^n a_j x^j,
a_n=1.                                                     (5.2)
```

Since `F_pi(t)=sum_j a_j q^(t(j-n))`, summing the tail gives

```text
E_pi[tau]
 = sum_(t>=0) (1-F_pi(t))
 = - sum_(j=m)^(n-1) a_j / (1-q^(j-n)).                   (5.3)
```

The `j=n` term cancels the constant `1`.  Formula (5.3) is zero for the
discrete partition and finite for every `q>=2`.  The exact first-hit law is

```text
Pr_pi(tau=t)=F_pi(t)-F_pi(t-1),             t>=1,          (5.4)
```

with the time-zero atom determined by (5.1).  The verifier also computes the
mean independently from the one-step triangular recurrence and obtains (5.3)
for every partition through `n=6` and `q in {2,3,5}`.

## 6. Exact block-count occupancy law

Within one source block of size `b`, exactly `j` output blocks occur when its
`b` elements use exactly `j` of the `Q` signatures.  The number of such
assignments is

```text
(Q)_j S(b,j).                                               (6.1)
```

Disjoint source blocks use independent element-signatures.  Therefore, if
`K_t` is the number of blocks after `t` epochs,

```text
E_pi[z^(K_t)]
 = Q^(-n) product_(i=1)^m
     [sum_(j=1)^(min(b_i,Q)) (Q)_j S(b_i,j) z^j].          (6.2)
```

Coefficient extraction is the complete block-count distribution.  This is
ordinary labelled balls-in-boxes occupancy, block by block; no contribution
credit is assigned to it.

## 7. Complete partition-lattice spectrum

For `rho in Pi_n`, define the zeta function

```text
Z_rho(pi) = 1_{rho<=pi}.                                   (7.1)
```

For the one-step Markov operator acting on functions,

```text
(P Z_rho)(pi)
 = 1_{rho<=pi} Pr(rho<=ker(c))
 = q^(#rho-n) Z_rho(pi),                                  (7.2)
```

because a colouring constant on every block of `rho` has `q^(#rho)` choices.
The zeta functions form a basis of functions on the finite partition lattice.
Thus the complete spectrum is

```text
lambda_k = q^(k-n),              multiplicity S(n,k),
k=1,...,n.                                                (7.3)
```

For `q>=2` these eigenvalues are distinct across ranks, and (7.1) supplies a
full eigenbasis.  In particular,

```text
det(I-zP)=product_(k=1)^n (1-z q^(k-n))^(S(n,k)),          (7.4)
```

and the `t`-step eigenvalues are `q^(t(k-n))`.  The eigenvalue one has
multiplicity one, consistently with the unique absorbing state.

This proof is useful as a two-line specialization, but the result sits
directly inside finite meet-semilattice/left-regular-band walk theory and is
zero-credit in the value decision.

## 8. Target-sensitive all-source history polynomial

Fix a target `sigma` with indexed blocks `C_1,...,C_k` and sizes
`s_i=|C_i|`.  Every possible source `pi>=sigma` corresponds uniquely to a set
partition `Gamma` of the index set `[k]`: a group `G in Gamma` says that the
target blocks with indices in `G` belong to one source block.  Put

```text
s(G) = sum_(i in G) s_i.                                   (8.1)
```

By (4.2), the number of histories for that source is

```text
product_(G in Gamma) (Q)_(|G|).                            (8.2)
```

### Source-block-size multivariate form

The exact polynomial recording the sizes of all source blocks is

```text
H_(sigma,t)(x_1,...,x_n)
 = sum_(Gamma in Pi_k)
     product_(G in Gamma) [(Q)_(|G|) x_(s(G))].            (8.3)
```

### Pair-count and source-rank form

Let `p(pi)=sum_(B in pi) binom(|B|,2)`.  Merging the target blocks in `G`
creates

```text
d_s(G)=sum_({i,j} subset G) s_i s_j                       (8.4)
```

new equal pairs.  The bivariate marked column is

```text
M_(sigma,t)(u,v)
 = sum_(Gamma in Pi_k) v^(|Gamma|)
     product_(G in Gamma) [(Q)_(|G|) u^(d_s(G))].          (8.5)
```

Equivalently its coefficient at `u^d v^r` counts all pairs
`(pi,history)` ending at `sigma` with `#pi=r` and
`p(pi)-p(sigma)=d`.

These polynomials admit an exact subset recurrence.  For nonempty
`A subseteq[k]`, choose its least index `a` and set

```text
H_empty=1,
H_A=sum_(G subseteq A, a in G) (Q)_(|G|) x_(s(G)) H_(A\G). (8.6)
```

The analogous recurrence for (8.5) replaces `x_(s(G))` by
`v u^(d_s(G))`.

The marking is genuinely target-sensitive.  For the two four-element target
types,

```text
M_((3,1),t) = Q^2 v^2 + Q(Q-1) v u^3,
M_((2,2),t) = Q^2 v^2 + Q(Q-1) v u^4.                     (8.7)
```

At `u=v=1` the two columns agree, and more generally the unweighted column
depends only on `k`, not on `(s_1,...,s_k)`.  Equation (8.7) confirms that the
requested weight avoids that collapse.

### Why this does not rescue the candidate

Before any formula is evaluated,

```text
M_(sigma,t)(u,v)
 = sum_(pi>=sigma) q^(tn) P^t(pi,sigma)
     u^(p(pi)-p(sigma)) v^(#pi).                           (8.8)
```

Thus it is a user-chosen marked column transform of the already complete
kernel (4.3).  The grouping proof merely evaluates (8.8) by listing the
coarsenings of `sigma`.  Unlike RTI's stabilizer/coset inverse polynomial,
(8.5) exposes no new reachability obstruction, hidden sufficient statistic,
product factorization, or parameter-recovery phenomenon.  Its target
sensitivity is real but decorative; it does not meet the batch's independent
second-axis standard.

## 9. Boundary attacks

| boundary | exact outcome |
|---|---|
| `n=1` | the sole partition is already discrete; all kernels are the `1x1` identity |
| `t=0` | `Q=1`; (4.2) is one only at `sigma=pi`, (5.1) is the correct time-zero CDF |
| `q=1` | every colouring kernel is the one-block partition, so the chain never moves; this is why the theorem domain requires `q>=2` |
| target not refining source | probability zero by (4.2) |
| `k_B>q^t` | probability zero because `(q^t)_(k_B)=0` |
| source already discrete | absorption time zero and (5.3) is the empty sum |
| target discrete | (4.2) becomes exactly the numerator in (5.1) |

No hidden small-`n`, time-zero, or unsupported-target exception was found.

## 10. Independent executable audit

`verify_scout.py` imports no author or repository code.  It generates set
partitions as restricted-growth strings and literally enumerates colour
histories.  Its checks include:

- iterative meets versus the cumulative-signature identity;
- every source/target cell, including all zero cells;
- row mass and exact absorption numerators;
- full block-count distributions;
- every target's marked all-source history polynomial;
- closed absorption means versus an independent one-step recursion;
- every zeta eigenrelation and every Stirling multiplicity;
- `n=1`, `t=0`, `q=1`, and the `(3,1)` versus `(2,2)` witness.

Frozen coverage:

```text
18 exhaustive (n,q,t) boxes
337,856 literal source x history cases
4,012,464 assertions
STATUS PASS
```

The frozen transcript is `CANONICAL.txt`.  Two fresh simultaneous executions
both matched it byte for byte.  A source-only syntax compilation also passed.

```text
CANONICAL.txt sha256
7a3edec877e6ad3ce8583c566469d7b31dfeba36a15a92aca23b0000fbcfd2ab

verify_scout.py sha256
c3160fee9cdd4714b0b534d8ee652b49c690d082bd8f9b6a8bf2cd68fc073868
```

## 11. Owner and portfolio subtraction

The detailed record is in `OWNER_SEARCH_LOG.md`.  The decisive ledger is:

| component | owner/background subtraction | residual value |
|---|---|---|
| repeated colours become `q^t` signatures | composition of iid finite paintboxes / random maps | zero credit |
| arbitrary-source refinement | standard blockwise fragmentation kernel | zero credit |
| top-source absorption | Krachun--Yakubovich random-map partition meet on the `q=n` slice; birthday separation | elementary finite-`q` extension |
| block-count law | classical occupancy `(Q)_j S(b,j)` | zero credit |
| zeta spectrum | Brown / Ayyer et al. semigroup-walk theory | direct specialization |
| weighted target polynomial | marked sum of exact transition columns over partition coarsenings | correct but dependent decoration |

Internally, P110 already uses the full partition lattice and zeta/Mobius
technology; P118 occupies graph colouring and source-target colour fibres;
P126 occupies refinement dynamics; and P158 plus same-batch RTI occupy much
stronger random-intersection/history-signature lanes.  RAE and RPS were
already killed for dependent column/meet axes.  RCR is not literally
conjugate to any one of those papers, but its proof engine and theorem
silhouette are more crowded, not less.

## 12. Final gate

```text
FORMULAS_CORRECT YES
EXHAUSTIVE_REPLAY PASS_X2
TARGET_WEIGHT_GENUINELY_SIZE_SENSITIVE YES
TARGET_WEIGHT_INDEPENDENT_OF_FULL_KERNEL NO
DIRECT_RANDOM_MAP_MEET_OWNER YES_ON_Q_EQUALS_N_TOP_SOURCE_SLICE
DIRECT_PAINTBOX_FRAGMENTATION_KERNEL YES
SEMILATTICE_SPECTRUM_ZERO_CREDIT YES
PAPER_SIZED_OWNER_THIN_RESIDUAL NO
DECISION KILL_CLASSICAL_PAINTBOX_FRAGMENTATION_AND_DECORATIVE_COLUMN_MARKING
HOLD_EXTERNAL
```

Do not promote RCR to a P162--P166 paper.  The formulas are suitable as an
internal exact-control example for random refinement, but not as a new batch
slot.
