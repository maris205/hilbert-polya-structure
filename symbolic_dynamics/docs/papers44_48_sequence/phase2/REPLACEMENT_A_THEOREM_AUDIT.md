# Replacement A Theorem Audit — Arithmetic Pole Walls

## Status and ownership subtraction

`UNNUMBERED HOLD_BACKUP / ARCHIVAL CONDITIONAL AUDIT / NO AUTHORITY WRITE`

Finite-`B` soficity, entropy approximation, general PFT zeta formulas, and
single-system Perron orbit asymptotics are prior-owned.  None of those items
is counted as novelty here.  The candidate survives only as a theorem on a
singular limit of a nested arithmetic family: fixed-point coefficients
stabilize, but convergence radii jump and the dominant poles condense onto a
strict interior circle.

## Frozen arithmetic family

Let `b_i=p_i^{a_i}` be pairwise coprime prime powers with distinct primes
`p_i`, `sum_i 1/b_i < infinity`, and

```text
R_j = product_{i<=j} p_i,
Q_j = product_{i<=j} b_i,
delta_j = product_{i<=j} (1-1/b_i),
delta_infinity = product_i (1-1/b_i) > 0.
```

Define `X_j` to be the binary hereditary shift whose support misses at least
one residue class modulo every `b_i`, `i<=j`.
Let `X_infinity=intersection_j X_j`.  The prime-square tower is the canonical
control `a_i=2`.

## Theorem package to prove

### 1. Entropy and fixed-period separation

```text
h_top(X_j)=delta_j log 2 -> delta_infinity log 2 > 0.
```

A nonzero `n`-periodic point of `X_j` exists exactly when `R_j|n`.
Consequently `X_infinity` has only the zero periodic point and

```text
F_infinity(n)=1,
zeta_infinity(z)=(1-z)^(-1),
h_per(X_infinity)=0.
```

Thus `h_per(X_j)=h_top(X_j)` tends to a positive number while
`h_per(X_infinity)=0`; periodic entropy is not upper semicontinuous along
this nested sofic/hereditary tower.

### 2. Direct finite-stage pole factor

For each omission tuple `r in product_i Z/b_i Z`, the corresponding
periodically constrained full shift has a `Q_j`-state right-resolving cycle.
CRT makes the shift action on omission tuples one cycle of length `Q_j`.
Distinct tuples have distinct maximal masks, so the presentation is
follower-separated.

For `n=Q_j m`, the union over the `Q_j` maximal masks gives

```text
F_j(n) = Q_j 2^(delta_j n) + O_j(2^((delta_j-1/Q_j)n)).
```

Every proper overlap forbids at least one additional phase in a `Q_j`
period.  For the finitely many other residue classes of `n mod Q_j`, the
exponential rate is also strictly below `delta_j log 2`.  Hence, directly
from `log zeta_j=sum_n F_j(n)z^n/n`,

```text
zeta_j(z) = g_j(z)/(1-2^(delta_j Q_j) z^Q_j),
```

where `g_j` is analytic and nonzero on a disk strictly larger than
`rho_j=2^(-delta_j)`.  The `Q_j` simple dominant poles are therefore

```text
Pi_j={rho_j exp(2 pi i k/Q_j): 0<=k<Q_j}.
```

This proof is required; a bare appeal to generic PFT rationality is not an
admissible contribution.

### 3. Local uniform convergence on the maximal centered disk

For a length-`n` periodic word, put `g_i=gcd(n,b_i)`.  Admissibility is
equivalent to omitting at least one class modulo each `g_i`.  There are at
most `D=product_i g_i` choices of omitted effective classes.  Pairwise
coprimality gives `D|n`, hence `D<=n`, and CRT leaves at most

```text
2^(n product_i(1-1/g_i)) <= 2^(delta_j n)
```

words per choice.  Therefore the stronger uniform estimate is

```text
F_j(n)=1 if R_j does not divide n,
F_j(n)<=n 2^(delta_j n) otherwise.
```

For every `r<rho_infinity=2^(-delta_infinity)`, choose `J(r)` so that
`r<rho_j` and `a_j=2^delta_j r<1` for every `j>=J(r)`.  On that tail,

```text
sup_{|z|<=r}|log zeta_j(z)+log(1-z)|
 <= sum_{m>=1}a_j^(m R_j)
 = a_j^R_j/(1-a_j^R_j) -> 0.
```

Thus no auxiliary growth assumption on `Q_j` is needed, and
`zeta_j -> (1-z)^(-1)` locally uniformly on `|z|<rho_infinity` even though
the coefficientwise limit has radius one.

### 4. Quantitative pole wall and maximality

The radii satisfy `rho_j -> rho_infinity<1`, whereas `Q_j -> infinity`.
Consequently

```text
d_H(Pi_j,rho_infinity S^1)
 <= |rho_infinity-rho_j| + pi rho_j/Q_j -> 0.
```

Every neighborhood of every point of the critical circle is hit by poles of
all sufficiently large stages.  Hence the centered disk in part 3 is the
maximal common holomorphic convergence domain; coefficientwise convergence
cannot be promoted across any arc of the pole wall.

## General criterion

The paper must isolate the proof into an abstract criterion with:

1. a first-extra-period scale `L_j -> infinity`;
2. a fixed-point envelope `F_j(n)-F(n) <= P(n)exp(h_j n)` supported on
   multiples of `L_j`, with `h_j->h>0` and one fixed polynomial `P`;
3. a cyclic maximal-entropy presentation of period `q_j->infinity` and a
   strict entropy gap for all proper overlaps.

Items 1--2 give local uniform convergence on `|z|<exp(-h)`; item 3 gives a
quantitative dominant-pole wall.  The prime-power family must verify every
hypothesis without importing the conclusion from a general PFT formula.

## Required controls

- prime squares `b_i=p_i^2`;
- a non-square bounded-exponent prime-power tower;
- a failed control with `delta_infinity=0`;
- a high-exponent control demonstrating that local convergence does not need
  `log Q_j=o(R_j)`;
- direct fixed-word enumeration versus the omission-tuple/CRT evaluator;
- direct rational-zeta denominator versus the pole-necklace evaluator.

## Admission decision

The four finite-stage CRT statements alone remain `STOP_STANDALONE`.  A full
abstract convergence theorem, arithmetic class, direct pole factor,
Hausdorff pole-wall rate, and periodic-entropy discontinuity could form one
indivisible unit, but Nordin--Noorani already own each finite-stage Perron
necklace and this candidate has not received a second proof/source signature.
It remains an unnumbered `HOLD_BACKUP`, outside the active Paper 44--48
sequence.
