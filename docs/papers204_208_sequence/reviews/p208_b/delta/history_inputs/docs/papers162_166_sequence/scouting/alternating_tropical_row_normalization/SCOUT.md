# Alternating tropical row-normalization dynamics

**Handle:** `ATR`  
**Author-side decision:** `GREEN_PENDING_INDEPENDENT_HOSTILE_GATE`  
**External status:** `HOLD_EXTERNAL`

## Outcome first

For integers `n,q>=2`, let `X_{n,q}={0,...,q-1}^{n x n}`.  If

```text
R(A)_ij = A_ij - min_k A_ik,
T(A)    = R(A)^transpose,                                  (1)
```

then every orbit enters in at most two steps the set `C_{n,q}` of matrices
having a zero in every row and every column.  On that recurrent core, `T` is
exactly transpose.  Thus the only periods are one and two, the height is
exactly two, and the full recurrent and fixed-point counts have closed
inclusion--exclusion formulas.

The nontrivial residual is inverse rather than temporal.  Every one-step
target has a product fibre polynomial.  Every two-step target has an exact
zero-cover/potential fibre polynomial which distinguishes the placement of
its zeros, not merely its row and column maxima.  These formulas yield exact
depth shells and conserve all `q^(n^2)` sources.

The independent author verifier exhausts 86,084 matrices in six boxes,
including every `4 x 4` binary matrix and every `3 x 3` ternary matrix.  It
checks every target fibre in every box and the weighted source-sum polynomial
in four boxes: **903,345 exact assertions, STATUS PASS**.

## 1. The two-step projection and sharp clock

Put `B=R(A)`, and let `s_j=min_i B_ij`.  A direct second update gives

```text
T^2(A)_ij = B_ij-s_j.                                    (2)
```

Every row of `B` contains a zero.  If `B_ij=0`, then its column minimum
`s_j` is also zero, so subtracting the column minima preserves at least one
zero in every row.  Equation (2) also creates a zero in every column.
Consequently `C=T^2(A)` lies in `C_{n,q}`.

Conversely every `C in C_{n,q}` is in the second image because `T^2(C)=C`.
For such a `C`, row reduction does nothing and

```text
T(C)=C^transpose,  T^2(C)=C.                             (3)
```

Hence `T^4=T^2` on the full carrier.  A matrix is recurrent iff it lies in
`C_{n,q}`; it is fixed iff it is additionally symmetric.  The matrix with
first column zero and every other entry one has depth two, so the height-two
bound is sharp for every `n,q>=2`.

## 2. Exact images, recurrent points, and zeta function

The first image consists exactly of matrices with a zero in every column.
Therefore

```text
|im T| = (q^n-(q-1)^n)^n.                               (4)
```

Let `R_{n,q}=|C_{n,q}|`.  Inclusion--exclusion over rows and columns missing
a zero gives

```text
R_{n,q} = sum_{i,j=0}^n (-1)^(i+j) binom(n,i)binom(n,j)
            (q-1)^(n(i+j)-ij) q^((n-i)(n-j)).            (5)
```

There are `N=n(n+1)/2` independent entries in a symmetric matrix.  If a set
of `i` rows is forbidden to contain zero, every symmetric entry incident to
that set must be nonzero.  Thus the number of fixed points is

```text
F_{n,q} = sum_{i=0}^n (-1)^i binom(n,i)
            (q-1)^(N-binom(n-i+1,2)) q^binom(n-i+1,2).   (6)
```

There are `(R_{n,q}-F_{n,q})/2` strict two-cycles, and the Artin--Mazur zeta
function of the recurrent restriction is

```text
zeta_T(z)=(1-z)^(-F_{n,q})(1-z^2)^(-(R_{n,q}-F_{n,q})/2). (7)
```

## 3. Every-target one-step fibres

For a matrix `Y`, let `M_i(Y)=max_j Y_{ji}`, the maximum in column `i`, and
write `|Y|` for the sum of its entries.  A source of `Y` must have the form

```text
A_ij=Y_ji+r_i,  0<=r_i<=q-1-M_i(Y).                     (8)
```

This is possible exactly when every column of `Y` contains zero.  Therefore

```text
|T^(-1)(Y)| = product_i (q-M_i(Y)),                      (9)
```

on the first image and is zero otherwise.  More strongly, the source-sum
polynomial is

```text
P_Y^(1)(z)=z^|Y| product_i (sum_{r=0}^{q-1-M_i(Y)} z^(nr)). (10)
```

This records substantially more than the indegree: coefficient `z^a` counts
sources whose entries sum to `a`.

## 4. Every-target two-step fibres as zero-cover potentials

Fix `C in C_{n,q}` and define the zero set in row `i` by
`Z_i(C)={j:C_ij=0}`.  Every intermediate row-reduced matrix mapping to `C`
under column reduction is uniquely

```text
B_ij=C_ij+s_j.                                           (11)
```

The column potentials obey

```text
0<=s_j<=q-1-max_i C_ij,
{j:s_j=0} intersects Z_i(C) for every row i.             (12)
```

The second condition is the exact zero-cover constraint ensuring that `B`
is row reduced.  Given such an `s`, every source with `R(A)=B` is uniquely
`A_ij=B_ij+r_i`, where

```text
0<=r_i<=q-1-max_j(C_ij+s_j).                             (13)
```

It follows that

```text
|(T^2)^(-1)(C)|
 = sum_s product_i [q-max_j(C_ij+s_j)],                  (14)
```

where the sum is over (12), and the fibre is zero off the core.  The fully
weighted refinement is

```text
P_C^(2)(z)=z^|C| sum_s z^(n sum_j s_j)
  product_i (sum_{r=0}^{q-1-max_j(C_ij+s_j)} z^(nr)).    (15)
```

Unlike (9), (14) depends on the incidence pattern of the target zero sets.
It is an evaluated finite cover sum with explicit local bounds, not an
unevaluated sum over all sources.

## 5. Exact depth census

Let

```text
L_{n,q}=sum_{C in C_{n,q}} product_i(q-M_i(C)).           (16)
```

Summing the one-step fibres over recurrent targets counts exactly the states
of depth at most one.  Hence the three depth shells are

```text
depth 0: R_{n,q},
depth 1: L_{n,q}-R_{n,q},
depth 2: q^(n^2)-L_{n,q}.                                (17)
```

For `(n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)`, the verified shell triples
are respectively

```text
(7,7,2), (17,46,18), (31,153,72),
(265,169,78), (4051,9416,6216), (41503,14911,9122).      (18)
```

## 6. Boundaries and claim ceiling

- `n=1` has height one: every entry maps immediately to zero.
- `q=1` has a singleton carrier.  Both lower bounds are essential for sharp
  height two.
- Equations (4)--(6) are elementary inclusion--exclusion and receive no
  novelty credit by themselves.
- Kuhn--Munkres assignment algorithms own row and column subtraction of
  minima as a primitive.  This paper assigns zero credit to that primitive
  and does not claim an assignment algorithm.
- The permissible residual is the literal finite dynamical conjunction:
  the two-step projection/transposition graph together with the target-wise
  one- and two-step fibre polynomials and the induced depth census.
- No absolute novelty or priority claim is made.  External release remains
  `HOLD_EXTERNAL` pending specialist review.

## 7. Executable evidence

Run:

```bash
python3 docs/papers162_166_sequence/scouting/alternating_tropical_row_normalization/verify_atr.py
```

The verifier starts from (1), enumerates every literal source and target in
the six boxes, constructs empirical one- and two-step source-sum polynomials,
and compares them coefficientwise with (10) and (15).  It also checks
`T^4=T^2`, exact depth minimality, images, fixed points, two-cycle parity,
mass conservation, all target supports, and formulas (4)--(6).  Structural
count and boundary checks continue through `2<=n,q<=10`.

