# AA01/USP focused specialist threshold gate

**Decision:** `KILL`  
**Mathematical status:** formulas correct after scope normalization  
**Contribution status:** no paper-sized theorem remains after Gaussian/LDU
subtraction  
**External status:** `HOLD_EXTERNAL`  
**Review role:** specialist threshold review, not an author paper draft

## Outcome first

`AA01/USP` should not receive a P162--P166 paper slot.  The survival,
first-failure, prescribed-target, empty-target, and failure-sink formulas are
correct.  The problem is stronger than a missing citation: all of them are
projections or cumulative sums of one elementary reverse-Schur coordinate
bijection.  The identifiability statement also divides two instances of that
same monomial count.

Moreover, the counting theorem does not use commutativity or locality.  With
the order of multiplication fixed, it holds over every finite associative
unital ring, depending only on

```text
Q = |R|,       U = |R^x|.
```

Independent exhaustive controls passed not only on the two nonisomorphic
local rings `Z/4Z` and `F_2[epsilon]/(epsilon^2)`, but also on the nonlocal ring
`Z/6Z` and the noncommutative ring `M_2(F_2)`.  This robustness is a
correctness strength but a contribution weakness: the proposed finite-local-
ring specificity is absent.

The earlier hostile gate also reached `KILL`.  The decision here is
independent: it follows from the normalized bijection and the specialist
owner/value subtraction below, not from voting with that report.

## 1. Frozen literal system and scope correction

Let `R` be a finite associative ring with identity, not necessarily
commutative or local.  Write `R^x` for its two-sided unit group.  For a
nonempty square matrix

```text
        [ a  b ]
A   =   [      ],
        [ c  D ]
```

where `a` is scalar, `b` is a row, and `c` is a column, define

```text
S(A) = D - c a^(-1) b             if a is a unit,
       dagger                      otherwise.
```

The empty matrix and `dagger` are fixed.  This is the exact update used by
the scout.  Associativity and a two-sided inverse for `a` suffice; neither
commutativity nor a unique maximal ideal is used below.

The honest theorem scope is therefore broader than the proposed one:

> USP is ordered unit-pivot Gaussian elimination over a finite unital ring,
> stopped at the first nonunit pivot.

This reframe does not save the candidate.  It makes the Gaussian nature more
explicit.

## 2. The single coordinate lemma

Fix `B in M_k(R)`.  A one-step predecessor of `B` is specified uniquely by

```text
a in R^x,       b in R^(1 x k),       c in R^(k x 1),
D = B + c a^(-1)b.
```

Conversely these choices always give `S(A)=B`.  Hence the map

```text
(a,b,c,B)  ->  [ a                 b ]
                [ c   B+c a^(-1)b ]
```

is a bijection from
`R^x x R^(1 x k) x R^(k x 1) x M_k(R)` onto the unit-pivot stratum in
`M_(k+1)(R)`.  Iterating this bijection is precisely reverse ordered LDU/Schur
elimination.  Every formula in the candidate is a marginal of this one
bijection.

## 3. Independent formula audit

### 3.1 Prescribed matrix targets at every time

For `t>=0`, every fixed `B in M_k(R)` has exactly

```text
F_(k,t)(B) = U^t Q^(2kt+t(t-1))
```

predecessors in the matching source stratum `M_(k+t)(R)`.  Indeed, the
successive reverse block sizes are `k,k+1,...,k+t-1`, so the product is

```text
product_(j=0)^(t-1) U Q^(2(k+j)).
```

The count is independent of `B`.  The `t=0` value is one.  There is no
exception when `k=0`; the formula then counts the successful `t x t`
matrices that first reach the empty matrix at step `t`.

### 3.2 Survival and exact first-failure shells

Put `n=k+t`.  Summing the constant target fibre over all
`Q^((n-t)^2)` targets gives

```text
Surv(n,t) = U^t Q^(n^2-t),              0<=t<=n.
```

For `0<=j<n`, exact first failure at step `j+1` has size

```text
FailExact(n,j+1)
  = U^j (Q-U) Q^(n^2-j-1)
  = U^j Q^(n^2-j)(1-U/Q).
```

The full-success shell has size

```text
Success(n) = U^n Q^(n^2-n).
```

The mass identity is the finite geometric telescoping identity

```text
sum_(j=0)^(n-1) FailExact(n,j+1) + Success(n) = Q^(n^2).
```

Thus the apparently separate survival and failure theorems do not have
separate proof objects.

### 3.3 Failure sink: stratumwise and pooled

For a source stratum `M_n(R)`, let `s=min(t,n)`.  The number reaching
`dagger` by time `t` is

```text
D_(n,t) = Q^(n^2) - U^s Q^(n^2-s).
```

This handles both regimes: for `t<n` it is the complement of time-`t`
survival; for `t>=n` it is the complement of complete success.  At `t=0` it
is zero.

If the actual finite carrier pools all matrix sizes `0,...,N` together with
the fixed sink, then the sink fibre is instead

```text
|(T_N^t)^(-1)(dagger)|
 = 1 + sum_(n=1)^N
       [Q^(n^2)-U^min(t,n) Q^(n^2-min(t,n))].
```

The leading `1` is the sink itself.  This pooled formula must not be replaced
by a single-stratum failure shell.

### 3.4 Empty target: matching stratum versus pooled carrier

The prescribed-target formula at `(k,t)=(0,t)` counts only successful
sources in `M_t(R)`:

```text
F_(0,t)(empty) = U^t Q^(t(t-1)).
```

In the capped pooled carrier, smaller successful matrices have already
arrived at the fixed empty state.  Therefore

```text
|(T_N^t)^(-1)(empty)|
 = 1 + sum_(j=1)^min(t,N) U^j Q^(j^2-j).
```

The leading `1` is the empty matrix itself.  This is the required boundary
correction when the paper-level carrier is the disjoint union rather than a
single source stratum.

### 3.5 `(Q,U)` identifiability and its ceiling

The one-step fibre over the empty target from `M_1(R)` is

```text
F_(0,1)=U.
```

The one-step fibre over any scalar target from `M_2(R)` is

```text
F_(1,1)=UQ^2.
```

Hence `U=F_(0,1)` and `Q=sqrt(F_(1,1)/F_(0,1))`.  For a finite local ring,
this also recovers the residue-field size

```text
q = Q/(Q-U),
```

because the nonunits form the maximal ideal.  Nothing in the atlas recovers
the additive group, characteristic, nilpotency length, multiplication table,
or isomorphism class of `R`.

This is not a second inverse theorem: it is parameter reading from two
monomials generated by the same coordinate lemma.

## 4. Nonisomorphic-ring and broader-ring attacks

### 4.1 Same `(Q,U)`, different local rings

```text
R_1 = Z/4Z,                         characteristic 4,
R_2 = F_2[epsilon]/(epsilon^2),     characteristic 2.
```

Both have `(Q,U)=(4,2)` and are nonisomorphic because ring characteristic is
an isomorphism invariant.  Every USP census above is therefore identical on
the pair.  Exhaustion through source size three confirmed this point for all
survival times, exact failure shells, matching-stratum target fibres, and the
capped pooled empty/failure fibres.

This blindness is especially relevant against the flag/Bruhat literature:
Onn--Prasad--Vaserstein show that broader double-coset/relative-flag data over
local principal ideal rings can depend on the ring in specific ranks and
lengths.  USP stays only in the elementary unit-pivot chart and cannot see
those ring-dependent strata.

### 4.2 Locality and commutativity are unused

The independent controls also passed on

```text
Z/6Z:       Q=6,  U=2        (commutative, nonlocal),
M_2(F_2):   Q=16, U=6        (noncommutative, nonlocal).
```

For `M_2(F_2)`, multiplication order was preserved exactly in
`D-ca^(-1)b`.  The result confirms the deductive observation that the proof
uses only an associative product and a two-sided pivot inverse.  A theorem
whose advertised local-ring content survives unchanged on these controls
has no residual local arithmetic axis.

## 5. Direct-owner search and subtraction

### Queries used

```text
"LU decomposition" "finite local ring" matrices
"LDU decomposition" matrices over local rings
"Schur complement" "finite local ring"
"Gaussian elimination" finite local rings pivot unit
number matrices finite field LU leading principal minors nonzero
finite field big Bruhat cell LDU count GL_n(q)
finite local ring Bruhat decomposition GL_n Borel big cell
Schur complement map finite field counting fibres
partial LU decomposition finite field pivot probability
```

### Primary records checked

1. D. Stott Parker, *Schur complements obey Lambek's categorial grammar:
   Another view of Gaussian elimination and LU decomposition*, Linear
   Algebra and its Applications 278 (1998), 63--84,
   [DOI 10.1016/S0024-3795(97)10033-7](https://doi.org/10.1016/S0024-3795(97)10033-7).
   Its abstract explicitly treats Schur complements as abstractions of
   Gaussian elimination, includes LU/UL decomposition, and studies quotient
   identities.  It directly owns USP's update and recursive quotient
   mechanism.
2. U. Onn, A. Prasad, and L. Vaserstein, *A note on Bruhat decomposition of
   GL(n) over local principal ideal rings*, Communications in Algebra 34
   (2006), 4119--4130,
   [DOI 10.1080/00927870600876250](https://doi.org/10.1080/00927870600876250),
   [arXiv:math/0506094](https://arxiv.org/abs/math/0506094).  This is a direct
   primary treatment of upper-triangular double cosets and relative full
   flags over local principal ideal rings.  It also records where those
   double-coset counts depend on the ring, highlighting exactly what USP's
   `(Q,U)` atlas discards.
3. P. Choosuwan, S. Jitman, and P. Udomkavanich, *Determinants of Matrices
   over Commutative Finite Principal Ideal Rings*,
   [arXiv:1605.06826](https://arxiv.org/abs/1605.06826).  The primary paper
   determines fixed-determinant counts over finite chain rings and extends
   them multiplicatively to finite principal ideal rings.  It does not state
   USP's literal sink packaging, but it confirms that finite-ring matrix
   enumeration is mature adjacent input.
4. M.-C. Yeung and T. F. Chan, *Probabilistic Analysis of Gaussian
   Elimination Without Pivoting*, SIAM Journal on Matrix Analysis and
   Applications 18 (1997), 499--517,
   [DOI 10.1137/S0895479895291741](https://doi.org/10.1137/S0895479895291741).
   Its probability model is continuous rather than finite-ring uniform, so
   it is not an exact counting owner; it is nevertheless direct ownership of
   pivot-failure probabilistic packaging for no-pivot Gaussian elimination.

The bounded search did not retrieve a primary paper displaying the exact
finite-ring all-time sink and prescribed-Schur-target formulas in this
notation.  That is recorded as `BOUNDED_NO_LITERAL_CONJUNCTION_HIT`, not as a
novelty inference.  The kill does not depend on finding the literal formula:
the progress threshold is already failed after direct mechanism subtraction.

## 6. Zero-credit ledger and residual theorem mass

| item | credit after specialist subtraction | reason |
|---|---|---|
| scalar Schur complement update | zero | Gaussian elimination/LU primitive; Parker direct owner |
| recursive/quotient law | zero | standard recursive Schur/LDU structure |
| unit leading pivots / no-pivot success chart | zero | big-cell/leading-pivot condition |
| lower, diagonal, upper coordinate counts | zero | direct cardinalities of triangular coordinates |
| survival census | zero | marginal of the reverse coordinate bijection |
| first-failure census | zero | difference of two survival marginals |
| prescribed-target fibres | zero | same bijection with the final block held fixed |
| empty and failure sink fibres | zero | cumulative bookkeeping across source strata |
| `(Q,U)` recovery | zero | ratio of two monomials from the same count |
| local-ring specialization | zero | theorem actually holds for every finite unital associative ring |

After this subtraction there is no independent temporal invariant, no
ring-sensitive arithmetic classification, no nontrivial image geometry, and
no inverse theorem beyond reading two cardinalities.  The candidate offers
one reusable counting lemma with corollaries, not two theorem axes.

## 7. Independent executable evidence

[`verify_specialist_gate.py`](verify_specialist_gate.py) imports no scout or
hostile-gate implementation.  It exhaustively checks:

- all matrices through size three over `Z/4Z` and
  `F_2[epsilon]/(epsilon^2)`;
- all matrices through size two over `Z/6Z` and `M_2(F_2)`;
- all admissible survival times and exact failure shells;
- every matching-stratum target in the tested ranges;
- capped-`N=3` pooled empty and failure fibres at and beyond saturation;
- `(Q,U)` recovery, the characteristic witness separating the two order-four
  local rings, and an explicit noncommutativity witness.

The frozen run summary is

```text
AA01_USP_SPECIALIST_GATE
RINGS [('Z4', 4, 2, 3, 2, 32), ('F2eps', 4, 2, 3, 2, 32), ('Z6', 6, 2, 2, 2, 72), ('M2F2', 16, 6, 2, 6, 1536)]
POOLED cap=3 empty/failure formulas PASS on Z4 and F2eps
BOUNDARY Z6(nonlocal) and M2F2(noncommutative) PASS
NONISOMORPHIC char(Z4)=4 char(F2eps)=2 same(Q,U)=(4,2)
ASSERTIONS 1183983
STATUS PASS
```

The arithmetic scout replay byte-matched its `CANONICAL.txt`; the independent
batch hostile verifier also replayed with 747,537 assertions and `STATUS
PASS`.  Computation is falsification pressure, while the all-parameter proof
is the coordinate bijection in Section 2.

## 8. Verdict and frozen ceiling

### Verdict: `KILL`

The formulas are correct, including the boundaries omitted by a
matching-stratum statement.  They are nevertheless a renamed no-pivot
Gaussian-elimination/LDU chart, and all advertised axes come from one product
coordinate count.  This fails the batch requirement of a clear advance with
two independent theorem axes.

The maximum internal statement worth retaining is:

> For any finite associative unital ring, reverse unit-pivot Schur
> coordinates give the stratumwise prescribed-target fibres, survival and
> failure shells above; capped empty/failure fibres are their explicit
> cumulative sums.

This must be labelled an elementary Gaussian/LDU enumeration.  It is not a
paper reserve and carries no novelty, priority, or external-release claim.
Re-entry would require a genuinely ring-sensitive invariant—one that
distinguishes rings with the same `(Q,U)`—and a second proof object not
obtained by marginalizing the same reverse factorization.
