# P164 Review B — independent proof rederivation

**Role:** independent Hostile Review B; neither author nor Review A  
**Literal map:** `T_q(w)_i = 1{w_i=w_(i+1)}` on cyclic words  
**Claimed range:** `q>=3`, `n=2^m>=4`  
**External status:** `HOLD_EXTERNAL`

This derivation was completed from the displayed literal rule before the
author or Review-A canonical controls were used.  The Review-B verifier does
not import either earlier implementation.

## 1. Literal first step and affine tail

Write `c(w)_i=1{w_i!=w_(i+1)}` and let `1` denote the all-one binary word.
Then, coordinate by coordinate,

```text
T_q(w)=1+c(w).
```

For a binary word `b`, equality is the complement of XOR.  If `S` is the
cyclic next-coordinate shift and `D=I+S` over `F_2`, then

```text
T_q(b)=1+Db,       D1=0.
```

Induction therefore gives, for every source and every `t>=1`,

```text
T_q^t(w)=1+D^(t-1)c(w).
```

No assertion about the nonlinear front is smuggled into this linear identity:
the sole source-dependent datum passed to the tail is the literal change mask.

## 2. Dyadic repeated-root operator

Identify `F_2^n` with `F_2[x]/(x^n-1)`.  Up to the harmless shift convention,
`D` is multiplication by `x+1`.  For `n=2^m`,

```text
x^n-1=(x+1)^n  in F_2[x].
```

Thus the cyclic module is `F_2[u]/(u^n)` with `D` multiplication by `u`.
Consequently, for `0<=j<=n`,

```text
D^n=0,
dim ker D^j=j,
im D^j=ker D^(n-j),
|im D^j|=2^(n-j).
```

All endpoint cases are literal: `ker D^0={0}`, `ker D^n=F_2^n`, and
`im D^n={0}`.

## 3. Change-mask multiplicity

Fix a binary mask `c` of weight `r`.  A q-ary source with mask `c` assigns
equal letters across zero edges and unequal letters across one edges.
Contracting the zero edges leaves the cyclic multigraph with `r` change
edges.  Its proper-colouring count is

```text
chi_q(c)=(q-1)^r+(-1)^r(q-1).
```

For `r=0` this equals `q`.  For `r=1` it is zero, as one change around a
cycle is impossible.  When `q>=3`, every `r>=2` gives a positive count: the
even case is immediate, and the odd case is
`(q-1)((q-1)^(r-1)-1)>0`.  Hence the unit masks are exactly the forbidden
masks in the theorem's range.

## 4. Clock, shells, checkpoints, and the last shell

The all-one word is fixed.  Every other constant source has change mask zero
and reaches it in one step.  A nonconstant source has nonzero mask and depth

```text
1+min{j>=0 : D^j c(w)=0}.
```

Since `D^n=0`, all sources are absorbed by time `n+1`.  If

```text
W_(j,d)(a)=sum_(D^j c=d) a^wt(c),
C_(n,j)(q)=W_(j,0)(q-1)+(q-1)W_(j,0)(-1),
```

then `C_(n,j)(q)` is exactly the q-ary source mass whose mask lies in
`ker D^j`.  Successive differences give the depth-`j+1` shell.

For a dyadic `j<n`, Frobenius gives `D^j=I+S^j`.  The kernel has `j` free
bits, each repeated `n/j` times, so

```text
W_(j,0)(a)=(1+a^(n/j))^j.
```

Because `n/j` is even, `W_(j,0)(-1)=2^j`, which yields the printed checkpoint.

The last shell consists of feasible odd-weight masks, since
`ker D^(n-1)` is the even-weight hyperplane.  With `x=q-1`, its mass is

```text
((x+1)^n-(x-1)^n)/2 - x*2^(n-1)
= (q^n-(q-2)^n)/2 - (q-1)2^(n-1).
```

Its strict positivity follows from the first positive term in the odd part:

```text
((x+1)^n-(x-1)^n)/2 - x2^(n-1)
>= x(nx^(n-2)-2^(n-1))
>= x2^(n-2)(n-2)>0.
```

The height is therefore sharply `n+1`.  Since every state is absorbed at the
fixed all-one state, that state is the unique recurrent point.

## 5. Image staircase and every-target affine enumerator

At time one, outputs are the complements of feasible masks.  Exactly the
`n` unit masks are absent, so the first image has size `2^n-n`.

For `t>=2`, set `j=min(t-1,n)`.  The iterate identity gives the inclusion

```text
im T_q^t subseteq 1+im D^j.
```

Every coset of `ker D^j` has a feasible representative.  If a selected
representative is not a unit, it is already feasible.  If it is a unit `e_i`,
add the all-one vector, which belongs to `ker D^j` for every `1<=j<=n`.
The replacement has weight `n-1>=3` and is feasible.  This explicitly covers
the capped endpoint `j=n`.  Hence

```text
im T_q^t=1+im D^j,      |im T_q^t|=2^(n-j).
```

For binary `y`, put `d=y+1`.  Summing the exact source multiplicity over the
affine solution set gives

```text
|(T_q^t)^(-1)(y)|
= W_(j,d)(q-1)+(q-1)W_(j,d)(-1).
```

Positive-time nonbinary targets are impossible because the first iterate is
binary.

At `t=n` one has `j=n-1`, so the image is the two targets `{0,1}`.  The
all-zero target corresponds to odd masks, and its fibre is exactly the last
shell above.  At `t=n+1`, `j=n` and all `q^n` sources have reached the sole
target `1`; all later times are identical.  These are the repaired last-shell
and `j=n` sentinels.

## 6. Complete time-two spectrum

The image of `D` is the even-weight hyperplane and `ker D={0,1}`.  For each
supported `d`, the two solutions are a complementary pair `{c,c+1}`.  If
`rho=min(wt(c),n-wt(c))` and `x=q-1`, summing their multiplicities gives

```text
x^rho+x^(n-rho)+2x(-1)^rho.
```

Because `n` is even, the complementary weights have the same parity.  For
`r<n/2`, every weight-r mask determines one complementary pair, giving
`binom(n,r)` targets.  At `r=n/2`, each pair is counted twice, giving
`binom(n,n/2)/2`.  These are parameter-class counts, not counts of distinct
numerical fibre values.  At `n=4,q=4`, the `r=1` and `r=2` values are both
24, so their target multiplicities merge to `4+3=7`, exactly as warned in
the manuscript.

## 7. Midpoint spectrum

At `j=n/2`,

```text
D^(n/2)=I+S^(n/2).
```

Thus a supported syndrome is `d=(u,u)`.  In each opposite coordinate pair,
a zero bit of `u` requires equal mask bits and contributes `1+a^2`; a one bit
requires unequal bits and contributes `2a`.  For `h=wt(u)`,

```text
W_(n/2,d)(a)=(1+a^2)^(n/2-h)(2a)^h.
```

At `a=-1` this is `2^(n/2)(-1)^h`.  Substitution in the affine enumerator
produces the displayed midpoint formula, and choosing the h nonzero
coordinates of `u` gives `binom(n/2,h)` parameter classes.

## 8. Scope boundaries attacked

| Boundary | Independent result |
|---|---|
| `q=2` | feasible masks are exactly the even-weight masks, each with multiplicity 2; the first-image formula and source repair change |
| `n=2` | feasible masks are only `00,11`; after two steps the image is a singleton, not the claimed two-element staircase |
| nondyadic `n=6` | `D^n` is nonzero and feasible masks can fail to absorb in the claimed window |
| nondyadic exponent `j=3` at `n=8` | `D^3` is not `I+S^3`; only powers of two support the checkpoint shortcut |
| `j=n` | the all-one kernel vector is still available; the image is the singleton `{1}` and the fibre has mass `q^n` |
| `t=n` | image is `{0,1}`; the zero-target fibre is exactly the positive last shell |

All theorem statements respect these boundaries.  No counterexample or
logical gap was found.

