# P194 Review-A proof rederivation

This reconstruction begins from the literal sign rule.  It uses prefix
balances for the operators, Greene invariants for shape, Jacobi--Trudi for the
Schur polynomial, and Aitken's determinant for standard-tableau counts.  Those
routes are independent of the author verifier.

## 1. Signature, edited occurrence, and ballot words

Fix a colour `i` and, for a prefix ending at position `r`, put

```text
B_i(r) = #(letters i in positions <=r) - #(letters i+1 in positions <=r).
```

In the left-to-right `+-` cancellation, a minus survives precisely when it is
read with no unmatched plus available.  Equivalently, its position creates a
new strict minimum of `B_i`.  Hence the rightmost surviving minus is the last
strict record-minimum position.  There is no surviving minus if and only if
`B_i(r)>=0` for every prefix.

Doing this for every adjacent pair shows

```text
all e_i undefined  <=>  every prefix has #i >= #(i+1) for every i.
```

Thus the holding states are exactly ballot/Yamanouchi words.  The edited
occurrences also have the stated orientation.  If the reduced signature is
`-^a +^b`, changing its rightmost surviving minus to a plus makes that new
plus the leftmost surviving plus; `f_i` changes it back.  The converse is the
same argument.  Therefore the frozen `e_i` and `f_i` are partial inverses on
each colour string.

This convention cannot be silently replaced by the common opposite tensor
order.  Here

```text
e_1(21)=11,
shape(RSK(21))=(1,1),   shape(RSK(11))=(2),
shape(RSK(reverse(21)))=shape(RSK(reverse(11)))=(2).
```

The reviewer executable derives these shapes from Greene invariants rather
than row insertion.

## 2. Components, recurrence, and pointwise clock

Every effective scheduled move is one crystal edge and changes one letter
`i+1` to `i`.  It therefore preserves the crystal component and lowers

```text
E(w)=sum_a w_a
```

by exactly one.  Consequently no nonconstant directed cycle can exist.  A
finite type-A word-crystal component has one highest vertex, so the scheduled
orbit must terminate there and every recurrent state is fixed.

For this tensor convention the component label is

```text
lambda = shape(RSK(w_n ... w_1)).
```

Its highest word has content `lambda`, padded through `k`, and therefore
energy

```text
b(lambda)=sum_(i=1)^k i lambda_i.
```

Since every step drops energy by one, the first entrance time is exactly

```text
tau(w)=E(w)-b(lambda).
```

Now `E(w)<=nk` and `b(lambda)>=sum_i lambda_i=n`, so
`tau(w)<=n(k-1)`.  Equality in the first inequality requires every displayed
letter to be `k`; hence the only possible maximizer is `k^n`.  That word has
reverse-RSK shape `(n)`, ends at `1^n`, and realizes the bound.  This also
shows uniqueness without assuming equality cases for an arbitrary shape.

At `n=1`, the letter `a` follows colours `a-1,a-2,...,1`, has depth `a-1`,
and ends at `1`.  At `k=1`, the carrier consists only of `1^n`, which is fixed
with depth zero.  Thus neither degenerate parameter changes the convention or
the tail definition.

## 3. Component and global depth polynomials

Reverse-word RSK identifies a word with a pair `(P,Q)` of common shape
`lambda`, where `P` is semistandard over `[k]` and `Q` is standard.  Under the
frozen crystal convention the operators change `P` and preserve `Q`.  Thus a
fixed recording tableau `Q` indexes one component, and there are
`f^lambda` components of shape `lambda`.

The energy of the word is the entry sum of `P`; the row-constant highest
tableau has entry sum `b(lambda)`.  The weight enumerator of the semistandard
tableaux therefore gives

```text
D_(lambda,k)(q)=q^(-b(lambda)) s_lambda(q,q^2,...,q^k).
```

Write `n(lambda)=sum_(r>=1)(r-1)lambda_r`.  Since
`b(lambda)=n+n(lambda)` and Schur functions are homogeneous of degree `n`,

```text
q^(-b) s_lambda(q,q^2,...,q^k)
  = q^(-n(lambda)) s_lambda(1,q,...,q^(k-1)).
```

The principal specialization is

```text
s_lambda(1,q,...,q^(k-1))
  = q^(n(lambda)) product_(x in lambda)
      (1-q^(k+ct(x)))/(1-q^(h(x))).
```

The powers cancel exactly, giving the displayed component product.  Summing
over the `f^lambda` recording tableaux yields the global polynomial, and its
coefficient of `q^d` counts precisely the words whose energy excess is `d`.

The reviewer did not verify this by repeating the product division.  It
computed `s_lambda(1,q,...,q^(k-1))` from the Jacobi--Trudi determinant with
complete homogeneous polynomials, removed exactly `n(lambda)` leading
degrees, and cross-multiplied the result by the hook denominator.

## 4. The `q=1` limit and fixed/involution census

For an allowed shape `ell(lambda)<=k`, every cell in zero-based row `r` has
`k+c-r>=1`; hence no numerator exponent in the product is zero.  For positive
integers `A,B`,

```text
lim_(q->1) (1-q^A)/(1-q^B)=A/B.
```

The component value at one is therefore

```text
product_(x in lambda) (k+ct(x))/h(x)=s_lambda(1^k).
```

The Schur expression already proves that the apparent rational product is a
polynomial, so this limiting statement introduces no divisibility
assumption.  Summing `f^lambda s_lambda(1^k)` over allowed shapes counts all
`k^n` words.

Each component contributes one highest word, so the fixed census is
`sum f^lambda`.  Under ordinary RSK, an involution corresponds to a pair
`(Q,Q)`, one for every standard tableau.  Schensted identifies the number of
rows with longest decreasing subsequence length, giving the bounded-height
interpretation.  When `k>=n`, every partition of `n` is allowed.  Decomposing
an involution by the partner of `n` gives

```text
I_n=I_(n-1)+(n-1)I_(n-2),
```

and the usual labelled construction gives
`sum I_n z^n/n! = exp(z+z^2/2)`, including `I_0=1`.

## 5. Complete one-step inverse atlas

Let `x` be a nonfixed source and let colour `i` be selected.  If `F(x)=y`,
then `y=e_i(x)` and partial inversion gives `x=f_i(y)`.  The scheduler chose
`i` exactly when every `e_j(x)` for `j<i` was absent.  Thus every nonself
source occurs in the displayed atlas.  A self-source occurs exactly when all
raising operators are absent, namely when the target is highest.

Conversely, suppose `x=f_i(y)` exists and every lower `e_j(x)` is absent.
Then `e_i(x)=y`, colour `i` is the least available colour at `x`, and hence
`F(x)=y`.  This proves equality of sets, not merely equality of sizes.

Different colour candidates have different contents, so they are distinct.
There are at most `k-1` nonself candidates and at most one self candidate,
giving `|F^(-1)(y)|<=k`.  Empty fibres are permitted.  Finally, summing all
incoming fibres counts each of the `k^n` sources exactly once.

## 6. Necessity and sufficiency of the stable threshold

Assume `k>=2`.  A fibre of size `k` must use the one self slot and all `k-1`
colour slots.  Its target is therefore highest.  If its padded content is
`lambda=(lambda_1,...,lambda_k)`, the reduced `i`-signature of a highest word
contains only pluses, in number `lambda_i-lambda_(i+1)`.  Thus `f_i` exists
exactly when `lambda_i>lambda_(i+1)`.  Availability for every colour forces

```text
lambda_1>lambda_2>...>lambda_k>=0,
n=sum lambda_i >= (k-1)+(k-2)+...+1=binom(k,2).
```

This proves the necessity of the threshold, rather than only the existence of
a small witness.

For `s=n-binom(k,2)>=0`, take

```text
h=1^(k-1+s) 2^(k-2) ... (k-1)^1.
```

Its prefix counts are ballot and its padded content is strictly decreasing,
so every `f_i(h)` exists.  Put `x=f_i(h)`.  If `j<i-1`, the changed letter is
outside the `j`-signature.  For `j=i-1`, changing an `i` to `i+1` removes one
minus from that signature; removing a minus cannot create an unmatched
minus.  Since `h` had no unmatched lower-colour minus, every `e_j(x)` for
`j<i` remains absent.  Hence every `f_i(h)` is an admitted source, and the
self-source makes the fibre size exactly `k`.  At `k=1`, the unique state and
unique fibre have size one.

## 7. Independent finite reconstruction

`verify_review_a_p194.py` imports only the Python standard library and no
author path.  It reconstructs every transition and incoming set in the 30
complete boxes `k=1..5`, `n=1..6`.  Its shape routine implements Greene's
maximum-union theorem by assigning letters to up to `r` weakly increasing
chains; its Schur routine uses Jacobi--Trudi; and its `f^lambda` routine uses
the Aitken determinant.  It separately recognizes involutions through `S_8`,
computes longest decreasing subsequences directly, tests `n=1` and `k=1`
beyond the complete grid, and exercises staircase targets through `k=10`.

Two fresh processes are byte-equal to `CANONICAL.txt`.  This finite evidence
is counterexample pressure only.  The arguments above, not the enumeration,
establish the all-parameter claims.

Conclusion: the complete mathematical package is provable as stated.
