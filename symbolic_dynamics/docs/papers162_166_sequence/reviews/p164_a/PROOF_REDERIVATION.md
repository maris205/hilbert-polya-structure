# Independent proof re-derivation for P164

## Claim

For `q >= 3` and `n = 2^m >= 4`, let

```text
T_q(w)_i = 1{w_i = w_(i+1)},
c(w)_i   = 1{w_i != w_(i+1)},
D        = I+S on F_2^n.
```

Theorem 1(A)--(D) of the pinned manuscript gives the exact iterates,
absorption clock and shells, all-time images and arbitrary-target fibres, and
the evaluated time-two and midpoint fibre spectra.

## Status

**PROVABLE AS STATED.**  No counterexample or missing hypothesis was found.
Two proof passages should be expanded before final acceptance; neither changes
a statement or formula.

## Assumptions and conventions

- Coordinates are cyclic modulo `n`.
- Binary addition is in `F_2`; `1` denotes the all-one vector.
- Depth is the first time an orbit enters the recurrent set.
- A positive-time nonbinary target has empty fibre.
- The fibre formula is used only for `t >= 1`; at `t=0` the map is the
  identity on the full q-ary carrier.
- `j=min(t-1,n)` caps the nilpotent tail after `D^n=0`.

## Dependency spine

```text
change-mask multiplicity chi_q(c)
          +
tail identity T_q^t(w)=1+D^(t-1)c(w)
          |
          +--> kernel flag --> depths, shells, sharp last layer
          |
          +--> affine images --> every-target weighted fibres
                                |
                                +--> complementary-pair spectrum at t=2
                                +--> coordinate-pair spectrum at t=n/2+1
```

## 1. Nonlinear front and affine tail

Put `r=wt(c)`.  Contract every equality edge of a cyclic word.  If `r>0`,
the quotient is the cycle with `r` change edges (allowing the familiar
two-edge multicycle at `r=2`), so its proper q-colouring count is

```text
chi_q(c)=(q-1)^r+(-1)^r(q-1).
```

At `r=0`, both the literal count and the displayed expression equal `q`.
Writing `x=q-1>=2`, the value vanishes exactly at `r=1`: it is zero there,
and for even `r` it is positive, while for odd `r>=3` it is
`x(x^(r-1)-1)>0`.  Thus the only infeasible binary change masks are units.

The first image is `T_q(w)=1+c(w)`.  On a binary word `b`, equality is the
complement of XOR, hence

```text
T_q(b)=1+Db.
```

Since `D1=0`, induction gives

```text
T_q^t(w)=1+D^(t-1)c(w),                     t>=1.       (1)
```

For dyadic `n`,

```text
F_2[x]/(x^n-1)=F_2[x]/((x+1)^n),
```

and `D` is multiplication by `x+1`.  Therefore it is one nilpotent Jordan
block:

```text
D^n=0,  dim ker D^j=j,  im D^j=ker D^(n-j),  0<=j<=n. (2)
```

## 2. Theorem A: clock, shells, and sharpness

The all-one word is fixed.  Every other constant word maps to it in one
step.  If `w` is nonconstant, (1) shows that it first reaches the all-one
word at

```text
1+min{j>=0:D^j c(w)=0}.
```

All states are absorbed, so the all-one word is the unique recurrent point.
Summing `chi_q(c)` over `ker D^j` gives `C_(n,j)(q)`.  Consequently the
depth-zero and depth-one shells have sizes `1` and `q-1`, and the
depth-`(j+1)` shell is `C_(n,j)-C_(n,j-1)`.

If `j<n` is dyadic, Frobenius gives `D^j=I+S^j`.  Its kernel consists of a
free length-j binary block repeated `n/j` times.  Its weight enumerator is

```text
(1+a^(n/j))^j,
```

and evaluating the two terms in `chi_q` yields the checkpoint formula

```text
C_(n,j)(q)=(1+(q-1)^(n/j))^j+(q-1)2^j.
```

The last shell is the `chi_q`-mass on the odd-weight masks, because
`ker D^(n-1)` is the even-weight hyperplane and `ker D^n=F_2^n`.  With
`x=q-1`, its size is

```text
L = ((x+1)^n-(x-1)^n)/2 - x 2^(n-1)
  = n x^(n-1) + sum_(odd k>=3) binom(n,k)x^(n-k) - x2^(n-1)
 >= x(n x^(n-2)-2^(n-1))
 >= x 2^(n-2)(n-2) > 0.                    (3)
```

This is the explicit inequality omitted from the manuscript proof.  It proves
that the height `n+1` is attained.

## 3. Theorem B: image staircase and every-target fibres

At time one, `y` occurs exactly when its complementary change mask `y+1` is
not a unit.  Hence the first image has size `2^n-n`.

For `t>=2`, put `j=min(t-1,n)`, so `1<=j<=n`.  Equation (1) gives the image
containment in `1+im D^j`.  Conversely, choose a representative `c` of any
coset with prescribed syndrome `D^j c=d`.  If `c` is not a unit, it is a
feasible change mask.  If `c=e_i` is a unit, then

```text
D^j(c+1)=D^j c,       wt(c+1)=n-1>=3,
```

because `D1=0`, hence `1 in ker D^j` for every such `j`, including `j=n`.
The repaired representative is feasible.  This proves

```text
im T_q^t=1+im D^j,    |im T_q^t|=2^(n-j).
```

The same repair fails at the excluded boundary `n=2`, where the complement
of a unit is another unit.

For a binary target `y`, each change mask in `D^j c=y+1` has exactly
`chi_q(c)` q-ary sources.  Summation gives

```text
|(T_q^t)^(-1)(y)|
 = W_(j,y+1)(q-1)+(q-1)W_(j,y+1)(-1).
```

Character orthogonality gives the displayed Fourier form in the manuscript;
it is a correct computational identity and is not needed as a separate
contribution.

## 4. Theorem C: time-two spectrum

The image of `D` is the even-weight hyperplane and `ker D={0,1}`.  Thus a
syndrome `d` occurs exactly when it has even weight, and every solvable
equation `Dc=d` has the complementary solution pair `{c,c+1}`.  Set

```text
rho(d)=min(wt(c),n-wt(c)).
```

Because `n` is even, both complementary weights have the parity of `rho`.
Adding their source multiplicities gives exactly

```text
(q-1)^rho+(q-1)^(n-rho)+2(q-1)(-1)^rho.
```

For `r<n/2`, every weight-r mask indexes one complementary pair, giving
`binom(n,r)` target classes.  At `r=n/2`, each pair is indexed twice, giving
`binom(n,n/2)/2`.  These are parameter-class multiplicities, not necessarily
distinct numerical fibre values.

## 5. Theorem D: midpoint spectrum

Frobenius gives

```text
D^(n/2)=I+S^(n/2).
```

Its image is exactly the duplicated half-words `d=(u,u)`.  If `h=wt(u)`,
each of the `n/2-h` zero coordinate-pairs permits equal mask bits and
contributes `1+a^2`; each of the `h` one coordinate-pairs permits unequal
bits and contributes `2a`.  Therefore

```text
W_(n/2,d)(a)=(1+a^2)^(n/2-h)(2a)^h.
```

Evaluation at `a=q-1` and at `a=-1` produces Theorem 1(D), including both
endpoints `h=0,n/2`.  There are `binom(n/2,h)` half-words of weight `h`.

## 6. Collision and boundary audit

- The wording after Theorem 1 correctly says that the stated multiplicities
  are parameter-class multiplicities and that equal numerical values must be
  merged.
- The verifier finds the announced time-two collision `(r=1,r=2)` at
  `(n,q)=(4,4)` and also a midpoint collision `(h=1,h=2)` there.
- It also finds both collision types at `(n,q)=(8,3)` for parameters `3,4`.
- At `t=0`, fibres are singleton fibres on the full q-ary carrier; no
  positive-time formula is applied.
- At `t=n+1` and thereafter, the image is the singleton all-one word and its
  fibre has size `q^n`.
- The hypotheses `q>=3`, `n>=4`, and dyadic `n` are essential, not cosmetic.

## Corrections and risks

No mathematical correction is required.  Before acceptance, insert (3) in
the proof of part (A), and expand the coset repair in part (B) to explicitly
cover `1<=j<=n`, especially `j=n`.  These are proof-completeness repairs, not
changes to Theorem 1.
