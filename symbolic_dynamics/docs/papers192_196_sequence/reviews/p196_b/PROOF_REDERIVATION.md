# P196 Review-B proof rederivation

This reconstruction uses cyclic binary relations and an eigenvector root
argument.  It does not use the author's section/preimage construction as the
image proof, the author's determinant row operations, Review A's determinant
lemma, Review A's Leibniz expansion, or direct weak-chain enumeration.

## 1. Symbol-labelled relations

Put `M=q-1`.  For each output symbol `c` define a `q` by `q` binary matrix

```text
R_c(a,b) = 1{a => b = c},       0 <= a,b <= M.
```

Rows represent a source letter at site `i`, columns the source letter at site
`i+1`.  Therefore, for a cyclic target `y=(y_0,...,y_(m-1))`, expanding the
matrix trace gives

```text
tr(R_(y_0) R_(y_1) ... R_(y_(m-1)))
  = sum_(x_0,...,x_(m-1)) product_i R_(y_i)(x_i,x_(i+1))
  = |T^(-1)(y)|,
```

where `x_m=x_0`.  This is an exact cyclic constraint count, not an
asymptotic transfer argument.

The truth table has two matrix forms.  Let `U=R_M`; then

```text
U(a,b)=1{a<=b}.
```

For `c<M`, let `e_c` be the `c`th coordinate vector and let
`u_c(a)=1{a>c}`.  Then

```text
R_c = u_c e_c^T.
```

Thus every nontop output relation has rank one.

## 2. Image and fibre product from positivity

First take the all-top target.  Its fibre size is `tr(U^m)`.  The matrix `U`
is upper triangular with every diagonal entry one, so the same holds for
`U^m` and

```text
tr(U^m)=q.
```

Now suppose that `y` has cyclically ordered nontop sites `p_1,...,p_s`,
values `a_j=y_(p_j)`, and positive cyclic gaps `d_j`.  Starting the trace at
`p_1` and substituting `R_a=u_a e_a^T` gives the exact rank-one split

```text
|T^(-1)(y)|
 = product_(j=1)^s [ e_(a_j)^T U^(d_j-1) u_(a_(j+1)) ],
```

with cyclic `a_(s+1)=a_1`.

For `r>=1`, an entry of `U^r` counts a weakly ordered path with fixed
endpoints, so repeated hockey-stick summation gives

```text
(U^r)_(a,c) = binom(c-a+r-1,r-1)   if c>=a,
              0                    otherwise.
```

When `d=1`, the bracket is `e_a^T u_b=1{a>b}`.  When `d>=2`, it is

```text
sum_(c>b) (U^(d-1))_(a,c)
 = binom(M-a+d-1,d-1)
   - 1{b>=a} binom(b-a+d-1,d-1)
 = G_d(a,b).
```

This proves the full product in the manuscript.

It also proves the image iff without constructing a source.  A violation of
the core language is exactly an adjacent pair of nontop target letters
`a,b` with `a<=b`; its distance-one factor is zero.  Conversely, every
distance-one factor in a legal target equals one, and every longer gap has a
positive assignment ending at `M>b`.  Hence the relation trace is positive
exactly for the stated language `L`, including the all-top word:

```text
im(T)=L.
```

## 3. Action on the positive core and clocks

Let `y` be legal.  If `y_(i+1)=M`, then `y_i=>y_(i+1)=M=y_(i+1)`.  If
`y_(i+1)<M`, legality says `y_i>y_(i+1)`, so the strict branch again gives
`y_i=>y_(i+1)=y_(i+1)`.  Therefore

```text
T(y)_i=y_(i+1),       T|L=S.
```

The defining local condition is rotation invariant.  Thus `S` permutes `L`.
Every state enters `L` in one update by the image result, while every state in
`L` is already recurrent under rotation.  This proves the exact depth
dichotomy.  A fixed core word is constant.  A constant `c<M` violates the
core condition at every site, so `M^m` is the unique fixed state.  Every
recurrent period divides `m`.

At `m=1`, the condition `y_0<M => y_0>y_0` leaves only `M`; directly every
one-letter source maps to it.  Hence the core size is one and its fibre size
is `q`, exactly as the general proof asserts.

## 4. Closed walks, fixed iterates, and cycles

Let

```text
A_(a,b)=1{b=M or a>b}.
```

An edge `a->b` is precisely a legal consecutive core pair.  Taking the cyclic
wrap into account, based closed walks of length `m` are in bijection with the
labelled core words, and hence

```text
|L_(q,m)|=tr(A^m).
```

For `r>=1`, an `r`-iterate fixed point must be recurrent and hence is a core
word fixed by `S^r`.  Such a length-`m` word is obtained by repeating a legal
cyclic word of length `g=gcd(m,r)`.  Consequently

```text
|Fix(T^r)|=tr(A^g).
```

For `d|m`, decomposing the points fixed by `S^d` according to their least
rotation period gives `tr(A^d)=sum_(e|d) P_e`.  Ordinary divisor-lattice
inversion yields the manuscript's formulas for `P_d` and `C_d=P_d/d`.

## 5. Characteristic polynomial by eigenvector recurrence

This derivation avoids determinants.  For a vector `v=(v_0,...,v_M)`,

```text
(Av)_a = sum_(b<a) v_b + v_M.
```

Suppose `Av=lambda v`.  The value `lambda=0` is impossible: the row-zero
equation gives `v_M=0`, and differences of successive row equations then
give `v_0=...=v_(M-1)=0`.

For `1<=a<=M`, subtracting the equation at `a-1` from that at `a` gives

```text
lambda(v_a-v_(a-1))=v_(a-1),
lambda v_a=(lambda+1)v_(a-1).
```

The row-zero equation is `lambda v_0=v_M`.  A nonzero eigenvector must have
`v_0!=0`; iterating the recurrence and using `M=q-1` gives

```text
lambda^q=(lambda+1)^(q-1).
```

Conversely, every root of

```text
P_q(lambda)=lambda^q-(lambda+1)^(q-1)
```

is nonzero, and the choice
`v_a=((lambda+1)/lambda)^a` satisfies all eigen-equations.  It remains to
protect multiplicities.  If `P_q` and `P_q'` shared a root, logarithmic
division of the two equations would force

```text
q/lambda=(q-1)/(lambda+1), hence lambda=-q.
```

But

```text
P_q(-q)=(-1)^q [q^q+(q-1)^(q-1)] != 0.
```

Thus `P_q` is square-free and has `q` distinct complex roots.  Each is an
eigenvalue of the `q` by `q` matrix `A`; its monic characteristic polynomial
has the same `q` roots, proving

```text
det(lambda I-A)=lambda^q-(lambda+1)^(q-1).
```

Cayley--Hamilton immediately gives the stated binomial trace recurrence.

## 6. Higher-time fibres and mass

For every source `x`, its first image lies in `L`; all later steps are shifts.
Thus

```text
T^t(x)=S^(t-1)T(x)       (t>=1).
```

For a core target `y`, applying `S^(1-t)` yields

```text
|(T^t)^(-1)(y)|=|T^(-1)(S^(1-t)y)|.
```

Targets outside the core have empty higher-time fibres as well.  Finally,
the one-step fibre sets partition the `q^m` source states, which proves the
mass identity.

## 7. Independent executable reconstruction

`verify_review_b_p196.py` represents states by packed integers.  It builds the
literal synchronous map digit by digit, but obtains inverse counts from the
cyclic relation product.  It compares the literal indegree, relation trace,
and published product for every target.  It also checks labelled higher-time
fibres, direct rotation periods, fixed iterates, and mass.  Its characteristic
polynomial implementation is Faddeev--LeVerrier and its gap control uses
entries of powers of `U`; it imports neither earlier program.

Conclusion: the central theorem package is provable as stated.
