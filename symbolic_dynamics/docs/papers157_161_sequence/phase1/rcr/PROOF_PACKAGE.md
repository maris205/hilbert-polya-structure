# RCR focused proof package

**Status:** `PROVABLE AS STATED / OWNER_AMBER / HOLD_EXTERNAL`.

## Claim

On anchored rectangles, update

```text
(x,y) -> (I,J),    I~Uniform{1,...,x}, J~Uniform{1,...,y},
```

with the two choices independent.  The claim is the conjunction of:

1. the exact one-dimensional absorption law and independent-geometric
   representation;
2. the exact rectangle absorption law, moments, support, and sharp tail; and
3. an every-time/every-target transition atlas and every-target potential,
   Green kernel, visit probability, and first-hit transform.

The source audit, not this proof, determines the owner ceiling.

## Assumptions

- `a,b,m` are positive integers.
- Conditional coordinate selections and selections between epochs are fresh
  and independent.
- Time zero and the visit at time zero are counted.
- `H_1=0`; `(1,1)` is absorbing.
- All products and sums over empty index sets use the usual conventions.

## Notation

For the one-coordinate chain write

```text
H_m=inf{t>=0:X_t=1},
p_t(m,k)=P_m(X_t=k),
U_(m,k)(z)=sum_(t>=0)p_t(m,k)z^t.
```

Put

```text
A_(m,r)=(-1)^(r-2) binom(m-1,r-1),
C_(m,k;r)=(-1)^(r-k)(m-1)!/[(k-1)!(r-k)!(m-r)!].
```

The harmonic sums are `h_n=sum_(q<=n)1/q` and
`h_n^(2)=sum_(q<=n)1/q^2`.

## Proof strategy

The lower-triangular first-step equations telescope after cumulative sums.
Their product solution supplies both the hitting PGF and every-target
resolvent.  Partial fractions yield exact finite exponential formulas.
Coordinate independence then gives the rectangle maximum clock and tensor
transition kernel.  Finally, monotonicity of both coordinates makes every
transient target a one-block visit: after departure it cannot be revisited.

## Dependency map

1. Lemma 1 proves coordinate independence and absorption.
2. Lemmas 2--4 prove the one-coordinate clock law.
3. Lemmas 5--6 prove the one-coordinate transition and first-hit atlas.
4. Lemmas 7--8 use Lemmas 1--4 for the rectangle clock.
5. Lemmas 9--10 use Lemmas 5--6 and coordinate independence for all spatial
   targets.
6. The boundary ledger checks every empty, absorbing, and inaccessible case.

## Proof

### Lemma 1: pathwise product construction and absorption

Let `(U_t,V_t)_(t>=1)` be iid pairs of independent uniform variables on
`(0,1)`, and define

```text
A_(t+1)=ceil(U_(t+1) A_t),
B_(t+1)=ceil(V_(t+1) B_t).
```

Conditional on `(A_t,B_t)=(x,y)`, this chooses a uniform cell of the current
rectangle.  The `A` coordinate depends only on the `U` sequence and the `B`
coordinate only on the `V` sequence, so the two coordinate chains are
independent as stochastic processes, not merely at one time.

From any rectangle contained in `[1,a]x[1,b]`, the next state is `(1,1)` with
conditional probability at least `1/(ab)`.  Iterating conditional
probabilities gives

```text
P(T_(a,b)>t) <= (1-1/(ab))^t.
```

Thus absorption is almost sure and all transforms used below exist in a
neighborhood of the closed unit disk.  The analogous one-dimensional bound
uses `1/m`.

### Lemma 2: one-dimensional PGF

Let `g_m(z)=E_m[z^H_m]`.  Then `g_1=1`, while first-step conditioning at
`m>=2` gives

```text
g_m=(z/m)sum_(j=1)^m g_j.
```

Define `S_m=sum_(j=1)^m g_j`.  Moving the self term to the left yields

```text
g_m=zS_(m-1)/(m-z),
S_m=S_(m-1)+g_m=mS_(m-1)/(m-z).
```

Starting from `S_1=1` and iterating,

```text
S_m=m!/[prod_(r=2)^m(r-z)],
g_m=z(m-1)!/[prod_(r=2)^m(r-z)].               (2.1)
```

This proves the formal identity and, by Lemma 1, the probability-transform
identity on a neighborhood of `|z|<=1`.  The product itself later shows the
larger exact disk `|z|<2`.

### Lemma 3: independent-geometric representation and moments

For independent `Z_r~Geom0((r-1)/r)`,

```text
E[z^Z_r]=(r-1)/(r-z).
```

Therefore the PGF of `1+sum_(r=2)^m Z_r` is

```text
z prod_(r=2)^m (r-1)/(r-z),
```

which is (2.1).  Uniqueness of probability generating functions proves

```text
H_m =_d 1+sum_(r=2)^m Z_r.                     (3.1)
```

For `Geom0(p)`, the mean and variance are `(1-p)/p` and
`(1-p)/p^2`.  With `p=(r-1)/r`, these are `1/(r-1)` and
`r/(r-1)^2=1/(r-1)+1/(r-1)^2`.  Summing independent moments in (3.1) gives

```text
E H_m=1+h_(m-1),
Var H_m=h_(m-1)+h_(m-1)^(2).                   (3.2)
```

For `m=1`, all three statements reduce separately to `H_1=0`.

### Lemma 4: exact one-dimensional distribution and tail

Lemma 5 below gives

```text
p_t(m,1)=1+sum_(r=2)^m
          (-1)^(r-1)binom(m-1,r-1)r^(-t).
```

Since state one is absorbing, `p_t(m,1)=P(H_m<=t)`.  Hence

```text
P(H_m>t)=sum_(r=2)^m
  (-1)^(r-2)binom(m-1,r-1)r^(-t).              (4.1)
```

Taking the difference between (4.1) at `t-1` and `t`, and using

```text
(r-1)binom(m-1,r-1)=(m-1)binom(m-2,r-2),
```

proves the stated PMF.  Its first atom is also immediate from the literal
one-step rule: `P(H_m=1)=1/m`.

The coefficient of `2^(-t)` in (4.1) is `m-1`; every remaining base is at
most `1/3`.  Multiplication by `2^t` and passage to the limit proves

```text
2^t P(H_m>t) -> m-1.                            (4.2)
```

Positive coefficients of a PGF cannot have a convergence radius exceeding
the reciprocal tail rate, while (2.1) is analytic on `|z|<2`; therefore the
radius is exactly two for `m>=2`.

### Lemma 5: the one-coordinate every-target resolvent

Fix target `k`.  Resolvent first-step conditioning in the **starting state**
gives

```text
U_(m,k)=1_{m=k}+(z/m)sum_(j=1)^m U_(j,k).       (5.1)
```

It is zero for `m<k`.  At `m=k`, (5.1) gives `U_(k,k)=k/(k-z)`.  For
`m>k`, define `V_m=sum_(j=k)^m U_(j,k)`.  Equation (5.1) gives

```text
U_(m,k)=zV_(m-1)/(m-z),
V_m=mV_(m-1)/(m-z).
```

Iteration from `V_k=k/(k-z)` yields

```text
U_(m,k)(z)
 = z(m-1)!/[(k-1)!prod_(q=k)^m(q-z)],           m>k.    (5.2)
```

The formula includes `k=1`; then the pole at `z=1` records permanent
occupation after absorption.

For any `m>=k`, partial fractions have the form

```text
U_(m,k)(z)=sum_(r=k)^m C_(m,k;r)/(1-z/r).       (5.3)
```

Indeed, multiplying (5.2) by `1-z/r` and setting `z=r` gives

```text
(m-1)!/[(k-1)! prod_(q=k,q!=r)^m(q-r)]
=(-1)^(r-k)(m-1)!/[(k-1)!(r-k)!(m-r)!].
```

The case `m=k` has coefficient one and agrees.  Comparing power-series
coefficients in (5.3) proves

```text
p_t(m,k)=sum_(r=k)^m C_(m,k;r)r^(-t).           (5.4)
```

### Lemma 6: one-coordinate hitting and Green laws

Let `tau_k` be the first hit of `k`.  By the strong Markov property,

```text
U_(m,k)(z)
=E_m[z^tau_k;tau_k<infinity] U_(k,k)(z).        (6.1)
```

For `m>k`, divide (5.2) by `k/(k-z)` to obtain

```text
E_m[z^tau_k;tau_k<infinity]
=z(m-1)!/[k!prod_(r=k+1)^m(r-z)].               (6.2)
```

At `z=1`, telescoping factorials give hit probability `1/k`.  Normalizing
(6.2) by this probability gives the PGF of
`1+sum_(r=k+1)^m Z_r`, proving the conditional hitting-time statement.

For `k>=2`, substituting `z=1` into the three cases of the resolvent proves

```text
G_1(m,k)=0, k/(k-1), 1/(k-1)
```

according as `m<k`, `m=k`, or `m>k`.  Equivalently, conditional on a hit,
the chain remains at `k` for a positive geometric number of visits with
departure probability `(k-1)/k`; after departure monotonicity forbids return.

### Lemma 7: rectangle CDF, PMF, and PGF

Under Lemma 1's pathwise construction, absorption occurs exactly when both
coordinates have hit one.  Thus

```text
T_(a,b)=max(H_a,H_b)                            (7.1)
```

with independent terms.  This immediately gives

```text
P(T<=t)=F_a(t)F_b(t),
P(T=t)=F_a(t)F_b(t)-F_a(t-1)F_b(t-1).          (7.2)
```

Write `S_m(t)=P(H_m>t)`.  Independence gives

```text
P(T>t)=S_a(t)+S_b(t)-S_a(t)S_b(t).             (7.3)
```

For any nonnegative integer-valued `N`,

```text
E[z^N]=1+(z-1)sum_(t>=0)P(N>t)z^t.             (7.4)
```

Substitute the finite exponential expansion (4.1) into (7.3), use
`sum_(t>=0)(z/q)^t=1/(1-z/q)` with the appropriate bases, and obtain exactly
the finite rational rectangle PGF in the theorem contract.  The derivation
is valid initially where the series converge and hence everywhere else as a
rational identity away from poles.

### Lemma 8: rectangle moments and sharp assertions

The standard tail identities

```text
E N   =sum_(t>=0)P(N>t),
E N^2 =sum_(t>=0)(2t+1)P(N>t)                  (8.1)
```

and

```text
sum_(t>=0)q^t=1/(1-q),
sum_(t>=0)(2t+1)q^t=(1+q)/(1-q)^2              (8.2)
```

give the two finite moment formulas term by term.

If `(a,b)!=(1,1)`, a one-step hit requires selecting `(1,1)` and has mass
`1/(ab)`.  At least one coordinate clock has positive mass at every positive
integer by (3.1), so the maximum has support `{1,2,...}`.  The coefficient of
`2^(-t)` in (7.3) is `(a-1)+(b-1)`; the product term has bases at most `1/4`.
This proves

```text
2^t P(T_(a,b)>t) -> a+b-2.                     (8.3)
```

When `a,b>=2`, both coordinate clocks are at least one and have full positive
support.  Hence `P(H_b>H_a)>0` and `P(H_a>H_b)>0`, which gives

```text
E max(H_a,H_b)>max(EH_a,EH_b).
```

Also `max(H_a,H_b)=H_a+H_b-min(H_a,H_b)` with the minimum at least one, so
the upper inequality is strict.  If one side equals one, its clock is zero
and all claimed boundary equalities are immediate.

### Lemma 9: the two-coordinate transition and potential atlas

By Lemma 1, for every `t>=0`,

```text
P^t_((a,b),(i,j))=p_t(a,i)p_t(b,j).             (9.1)
```

Substituting (5.4) into both factors proves the finite double expansion

```text
sum_(r=i)^a sum_(s=j)^b
C_(a,i;r)C_(b,j;s)(rs)^(-t).                   (9.2)
```

Multiplying by `z^t`, summing the geometric series, and interchanging only
finite sums proves

```text
U_((a,b),(i,j))(z)
=sum_(r=i)^a sum_(s=j)^b
 C_(a,i;r)C_(b,j;s)/(1-z/(rs)).                (9.3)
```

If a target coordinate exceeds the corresponding starting coordinate,
monotonicity makes it inaccessible and the potential is zero.  For a
transient target `(i,j)!=(1,1)`, every `rs>=ij>1`; thus (9.3) converges at
`z=1` and gives the claimed Green kernel.  Every occurrence is automatically
strictly before rectangle absorption.

### Lemma 10: visit probability and first-hit transform

At target `(i,j)`, the only transition that preserves both coordinates is
the selection of the upper-right cell itself, of mass `1/(ij)`.  Every other
transition lowers at least one coordinate, after which the target is forever
inaccessible.  Consequently a visit consists of one consecutive block whose
mean length is

```text
1/[1-1/(ij)]=ij/(ij-1).                        (10.1)
```

The expected occupation is the hit probability times (10.1), proving

```text
P(tau_(i,j)<infinity)=(ij-1)K/(ij).            (10.2)
```

More generally the strong Markov property at the first hit factors the
discounted potential as

```text
U_start,target(z)
=E_start[z^tau; tau<infinity] U_target,target(z),
U_target,target(z)=1/[1-z/(ij)].                (10.3)
```

Rearranging (10.3) proves the defective first-hit transform
`(1-z/(ij))U_start,target(z)`.

For target `(1,1)`, the visit probability is one and its ordinary occupation
is infinite.  Before absorption it is never occupied, so the killed Green is
zero.  Finally,

```text
sum_(t>=0)z^t P((A_t,B_t)=(1,1))
=sum_(t>=0)z^t P(T<=t)
=E[sum_(t>=T)z^t]
=E[z^T]/(1-z),                                  (10.4)
```

valid for `|z|<1`.  This completes the absorbing-target boundary.

## Boundary ledger

| case | clock | potential / hitting rule |
|---|---|---|
| `m=1` | `H_1=0`, `g_1=1`, CDF one | target one hit at time zero; ordinary occupation infinite |
| `(a,b)=(1,1)` | `T=0`, rectangle PGF one | killed Green zero; discounted potential `1/(1-z)` |
| exactly one unit side | rectangle clock equals the other coordinate clock | double sums collapse to the one-dimensional boundary |
| start equals transient target | first hit zero, probability one | Green `ij/(ij-1)` |
| target not coordinatewise below start | impossible | transition, potential, and hit probability all zero |
| transient target with `i=1` or `j=1` | allowed | `ij>1`, so every Green denominator remains nonzero |

## Corrections or missing assumptions

No mathematical correction to the scouting formulas is required.  The
focused statement must retain the time-zero convention, the harmonic-number
renaming, the separate absorbing-target convention, and the coordinatewise
accessibility condition.  Omitting any of these would make the theorem
ambiguous or false at a boundary.

## Open risks

- Ross and Durrett own the strict embedded chain and its independent visit
  mechanism; those inputs receive zero contribution credit.
- General decreasing-chain asymptotics, generic Bellman/resolvent methods,
  tensor-product transitions, and maxima of independent clocks receive zero
  credit.
- The literal anchored-rectangle plus full every-target conjunction still
  needs specialist owner review.  The current bounded non-hit is not novelty.
- No extension beyond the stated uniform, two-dimensional, fixed-anchor
  model is proved.
