# Independent derivation package

Status: `GREEN_OWNER_THIN / HOLD_EXTERNAL`.  No novelty claim.

## 1. Definitions and conventions

Fix `n>=2`, write `G=Z/nZ`, and put `1=(1,...,1)`.  For `x in G^n`,

```text
w(x)=#{r:x_r != 0},             T(x)=x+w(x)1.
```

For an endofunction, the preperiod of a point is the number of strict steps
before it first reaches its eventual cycle.  A recurrent point has preperiod
zero.  `S(a,b)` denotes a Stirling number of the second kind, with the usual
zero conventions.  We use `0^0=1` in coefficient formulas.

## 2. Diagonal phase reduction

The action `x -> x+a1` of `G` on `G^n` is free: if `x+a1=x`, then every
coordinate gives `a=0`.  Thus every diagonal orbit has `n` points.

Fix one representative `x` and its histogram

```text
c_i=#{r:x_r=i},                 sum_i c_i=n.
```

Parametrize the orbit by `x-i1`.  Its number of zeros is `c_i`, so its weight
is `n-c_i`, which is `-c_i mod n`.  Therefore

```text
T(x-i1)=x-i1+(n-c_i)1=x-(i+c_i)1.
```

This proves the literal conjugacy to

```text
g_c(i)=i+c_i mod n.                                      (2.1)
```

Changing the representative cyclically rotates `c` and conjugates (2.1) by
a phase rotation.  No primality assumption occurs.

## 3. Cycles consume all mass

Let `i_0,...,i_{ell-1}` be a cycle of (2.1).  Summing the nonnegative integer
increments around it gives

```text
sum_{j=0}^{ell-1} c_{i_j} = q n
```

for an integer `q>=0`.  The left side is at most `sum_i c_i=n`.

- If `q=0`, then all cycle increments vanish.  Each arrow is `i->i`, so the
  cycle has length one.
- If the cycle is nontrivial, `q=1`.  Thus its entries consume all histogram
  mass.  Every vertex off the cycle has `c_i=0` and is fixed, and a second
  nontrivial cycle is impossible.

On a nontrivial cycle all increments are positive.  Lift the residues around
the circle.  Since the positive increments have total exactly `n`, the
visited vertices occur in clockwise order and each `c_i` is exactly the gap
to the next visited vertex.  Conversely, choose any subset `C` with
`|C|=ell>=2`, label each point by its clockwise gap to the next point, and put
zero elsewhere.  Equation (2.1) has the unique `ell`-cycle `C` and fixes the
complement.  There are therefore `binom(n,ell)` histogram maps with a
nontrivial `ell`-cycle.

The singleton support case has one entry `n`; (2.1) is then the identity, so
it belongs to the fixed boundary rather than to a nontrivial cycle.

## 4. Lifted least-period census

First count fixed states directly.  A state is fixed iff `w(x)=0 mod n`.
Since `0<=w(x)<=n`, this means `w(x)=0` or `w(x)=n`.  Hence

```text
P_{n,1}=1+(n-1)^n.                                      (4.1)
```

For `ell>=2`, a state of least period `ell` has phase zero on the unique
nontrivial cycle.  Write its successive clockwise gaps starting at zero as
the positive composition

```text
a_1+...+a_ell=n.
```

The corresponding histogram has these `a_j` on the cycle support and zero
elsewhere.  The number of labelled words with that histogram is
`n!/(a_1!...a_ell!)`.  Therefore

```text
P_{n,ell}
 = sum_{a_1+...+a_ell=n, a_j>0} n!/(a_1!...a_ell!)
 = ell! S(n,ell).                                        (4.2)
```

The last equality counts surjections from `[n]` to an ordered set of `ell`
nonempty boxes.  Equations (4.1)--(4.2) immediately give

```text
#Fix(T^k)=sum_{ell|k,ell<=n}P_{n,ell}
```

and the finite Artin--Mazur product

```text
zeta_T(z)=product_{ell=1}^n (1-z^ell)^(-P_{n,ell}/ell).
```

The total recurrent count is

```text
D_{n,0}=(n-1)^n+sum_{ell=1}^n ell!S(n,ell).               (4.3)
```

## 5. Full transient-depth census

Consider a phase-zero point of exact positive preperiod `d`.  Its phase path
is

```text
0=S_0 -> S_1 -> ... -> S_d,
```

with distinct residues before the fixed endpoint.  Put
`a_j=c_{S_{j-1}}>0`.  The ordinary partial sums satisfy
`S_j=a_1+...+a_j` until a possible wrap.  But the sum of the masses on the
visited transient sites is at most the total mass `n`.  Equality to `n`
would give endpoint residue zero, equal to the start, which is impossible.
Thus no wrap occurs and, as ordinary integers,

```text
0=S_0<S_1<...<S_d=s<n.                                  (5.1)
```

The endpoint condition is `c_s=0`.  The `d` transient histogram entries are
fixed to `a_1,...,a_d`.  The remaining mass `n-s` is distributed freely over
the other `n-d-1` histogram positions.  For a fixed ordered positive
composition `(a_1,...,a_d)` of `s`, the multinomially weighted number of
labelled states is

```text
n!/(a_1!...a_d!) * (n-d-1)^(n-s)/(n-s)!.                 (5.2)
```

Indeed the exponential multinomial sum over the free positions is
`(n-d-1)^(n-s)/(n-s)!`.  Now

```text
sum_{a_1+...+a_d=s, a_j>0} 1/(a_1!...a_d!)
     =d!S(s,d)/s!,                                      (5.3)
```

again by ordered surjections.  Substituting (5.3) into (5.2) gives the closed
all-depth formula

```text
D_{n,d}=d! sum_{s=d}^{n-1} binom(n,s)S(s,d)
                   (n-d-1)^(n-s),       1<=d<=n-2.       (5.4)
```

A path of length `n-1` would visit all `n-1` positive sites before a zero
endpoint.  The sum of its increments would then be `n`, returning to its
start modulo `n`, a contradiction.  Hence every preperiod is at most `n-2`.

For equality, the positive support cannot have size `n-2`: the path would
again use all positive mass `n` and return to its start.  It must have size
`n-1`, so the histogram has one zero, one two, and all other entries one.
Let the zero be at `z` and the two at `e`.  If `e=z-1`, the double step jumps
over the zero and the positive sites form an `(n-1)`-cycle.  Otherwise phase
`z+1` follows unit steps to `e`, jumps over one site, and then follows unit
steps to `z`, for exactly `n-2` transient steps.  The only extra sharp phase
is `z+2`, occurring when `e=z+1`.  This proves the stated equality structure
and the counts `n(n-2)` and `n(n-1)`.

For an actual state to start in a sharp phase, its phase-zero histogram is
one of `n-1` rotations/placements; each has multinomial weight `n!/2`.
Therefore

```text
D_{n,n-2}=(n-1)n!/2.                                   (5.5)
```

At `n=2`, direct substitution shows that `T` is a permutation, so (5.4) has
an empty range and all four states have preperiod zero.

## 6. Target-resolved one-step inverse

Fix `y` and let `m_j=#{r:y_r=j}`.  If a source uses translation amount `k`,
then it is uniquely

```text
x=y-k1.
```

Its number of zeros is `m_k`, hence its weight is `n-m_k`.  It maps to `y`
exactly when

```text
k = n-m_k mod n.                                        (6.1)
```

For `k=0`, (6.1) means `m_0=0` or `m_0=n`.  For `1<=k<n`, it means the
ordinary equality `m_k=n-k`.  Distinct `k` give distinct sources, proving

```text
#T^{-1}(y)=1_{m_0 in {0,n}}+
           sum_{k=1}^{n-1}1_{m_k=n-k}.                   (6.2)
```

To mark all fibre sizes, sum the multinomial weights of all histograms.
For the zero coordinate, mark exponents zero and `n`; for positive coordinate
`k`, mark exponent `n-k`.  The exponential formula is exactly

```text
F_n(z)=n![u^n] A_0(u,z) product_{k=1}^{n-1}A_k(u,z),     (6.3)

A_0=e^u+(z-1)(1+u^n/n!),
A_k=e^u+(z-1)u^(n-k)/(n-k)!.
```

The coefficient of `z^0` counts the missing targets, and subtracting it from
`n^n` gives the exact one-step image size.

## 7. Sharp fibre maximum

Let `K={k in {1,...,n-1}:m_k=n-k}`.  If `|K|=r`, the required positive,
distinct masses satisfy

```text
n >= sum_{k in K}(n-k) >= 1+2+...+r.
```

Thus `r<=floor((sqrt(8n+1)-1)/2)`.  The zero-coordinate contribution can add
at most one.  If `m_0=n`, it excludes every positive condition; therefore a
maximum larger than one must have `m_0=0`.

For `n>=3`, put masses `j` at residue `n-j` for `1<=j<=r`.  If the triangular
sum is below `n`, place the remainder at residue one; for `n>=4` that residue
is unmarked and the remainder is too small to trigger its marked value.  The
case `n=3` has zero remainder.  This constructs a fibre of size `r+1`.
Equality in the upper bound is precisely `m_0=0` and `|K|=r`.  At `n=2`, a
direct check gives four singleton fibres.

## 8. Separation of proof axes

The forward dynamics uses mass exhaustion on cycles and a no-wrap argument
on transient paths.  The inverse theorem instead fixes the target and tests
the `n` possible diagonal shifts independently.  Neither proof supplies the
other.  Formula (5.4) is an all-time labelled census; formula (6.3) is a
one-step every-target inverse census.  Their conjunction is the proposed
paper-threshold residual after the owner subtraction.
