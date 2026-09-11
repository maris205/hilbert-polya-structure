# P196 Review-A proof rederivation

This proof route starts from the literal truth table and uses a rank-one
determinant calculation rather than the row operations in the manuscript.

## 1. Exact image and core action

Let `M=q-1`, let indices be cyclic, and put `y=T(x)`.  Suppose
`y_(i+1)<M`.  A Gödel implication is nontop only in its strict branch, so

```text
x_(i+1) > x_(i+2),   y_(i+1)=x_(i+2).
```

If `y_i=M`, it is automatically larger than `y_(i+1)`.  Otherwise the same
strict branch gives `y_i=x_(i+1)>x_(i+2)=y_(i+1)`.  Hence every image word
obeys

```text
y_(i+1)<M  implies  y_i>y_(i+1).
```

Call this language `L`.  Conversely, for `y in L`, the implication
`y_i => y_(i+1)` equals `y_(i+1)`: if the consequent is top this is automatic,
and otherwise the defining strict descent invokes the second truth-table
branch.  Therefore `T(y)=S(y)`, where `S` is left rotation.  The condition
defining `L` is rotation invariant, so

```text
T(S^(-1)y)=y.
```

Thus `im(T)=L` and `T|L=S`.  This also proves the depth dichotomy.  A periodic
point must be in `im(T)` and hence in `L`; its period is a rotation period and
divides `m`.  A fixed core word is constant, and the core condition excludes
every constant below `M`.  The unique fixed point is `M^m`.

For `m=1`, the condition reads `y_0<M => y_0>y_0`, so `L={M}`.  Directly,
`T(a)=M` for every letter `a`; hence the general statements retain their
literal meanings at this boundary.

## 2. Closed-word counts and iterate-fixed points

Define `A_(a,b)=1` if `b=M` or `a>b`.  A cyclic word belongs to `L` precisely
when every consecutive ordered pair is an allowed edge, including the wrap.
It is therefore a based closed walk of length `m`, and
`|L|=tr(A^m)`.

On `L`, `T^r=S^r`.  A length-`m` word fixed by `S^r` is the repetition of a
word of length `g=gcd(m,r)`.  The cyclic legality condition descends exactly
to that base word, giving

```text
|Fix(T^r)| = tr(A^g).
```

Möbius inversion of `tr(A^d)=sum_(e|d) P_e` gives the stated least-period and
cycle formulas.

## 3. Characteristic polynomial by a different route

Let `L0` be the strictly lower-triangular matrix of ones and let `e_M` be the
last standard basis vector.  Every row of `A` has a one in its last column,
so

```text
A = L0 + 1 e_M^T.
```

For an indeterminate `lambda`, set `B=lambda I-L0`.  The matrix determinant
lemma gives

```text
det(lambda I-A)=det(B) (1-e_M^T B^(-1) 1).
```

Because `B` is lower triangular, `det(B)=lambda^q`.  Solve `Bz=1`.  If
`s_a=z_0+...+z_a` and `s_(-1)=0`, then

```text
lambda z_a - s_(a-1)=1,
1+s_a=(1+lambda^(-1))(1+s_(a-1)).
```

Consequently

```text
z_M=(lambda+1)^M/lambda^(M+1).
```

Substitution, with `M=q-1`, yields

```text
det(lambda I-A)=lambda^q-(lambda+1)^(q-1).
```

The calculation was made over the rational function field only to invert
`lambda`; both sides are polynomials, so the identity is polynomially valid,
including at `lambda=0`.  The reviewer program supplies an independent second
check by expanding the determinant over all permutations, not by row
operations or this rank-one lemma.

## 4. One-gap inverse count

Take a legal target other than `M^m`.  Let consecutive nontop positions be
`p,p'`, with cyclic distance `d`, and let their values be `a,b`.  The equation
at `p` fixes `x_(p+1)=a`.  Each intervening top target symbol imposes one weak
increase, and the equation at `p'` imposes a final strict cutoff.  Thus the
free sequence is exactly

```text
a=x_(p+1) <= x_(p+2) <= ... <= x_(p') <= M,
x_(p') > b.
```

There are `binom(M-a+d-1,d-1)` weak chains before the cutoff.  If `b>=a`, the
violating chains end at most `b` and number
`binom(b-a+d-1,d-1)`; if `b<a`, none violate.  This gives

```text
G_d(a,b)=binom(M-a+d-1,d-1)
         - 1_(b>=a) binom(b-a+d-1,d-1).
```

At `d=1` there are no free intervening entries.  The formula is `1` exactly
when `a>b` and `0` otherwise, matching the core condition.  If the target has
only one nontop site, the unique cyclic gap has `d=m`; it covers every source
coordinate once.

Different gaps share only their already fixed endpoint values and partition
the remaining source coordinates, so their counts multiply.  If the target
is all top, the cyclic source inequalities force a constant word and give
exactly `q` sources.  Targets outside `L` have no sources by the image result.

## 5. Every-time fibres

For arbitrary `x`, the first iterate `T(x)` lies in `L`; thereafter the map is
rotation.  Hence, for all `t>=1`,

```text
T^t(x)=S^(t-1)T(x).
```

Taking the inverse image of a core target `y` gives
`|(T^t)^(-1)(y)|=|T^(-1)(S^(1-t)y)|`.  Summing the one-step formula over the
core counts every source once, proving the mass identity `q^m`.

## 6. Independent finite reconstruction

`verify_review_a_p196.py` uses tuple words, literal implications, direct
incoming-edge tables, direct weak-chain enumeration, and a Leibniz
determinant.  It imports no author module.  Two fresh executions are byte
equal to `CANONICAL.txt`.

Conclusion: the complete mathematical package is provable as stated.
