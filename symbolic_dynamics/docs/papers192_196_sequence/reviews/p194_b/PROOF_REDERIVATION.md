# P194 Review-B proof rederivation

## Independent route

This reconstruction does not use the author's code or Review A's code.  It
organizes the proof through sign-word normal forms, rank on a coloured
component, Gelfand--Tsetlin branching, and reverse-edge classification.  The
finite verifier realizes those same objects by adjacent cancellation, Fomin
growth diagrams, cyclotomic factors, Young-poset linear orders, and matching
generation.

## 1. Sign normal form and the operator convention

Fix a colour `i` and erase all letters other than `i,i+1`.  Encode these by
`+,-`.  Repeatedly delete adjacent `+-`.  Every deletion shortens the sign
word, and the only irreducible words are

```text
-^a +^b.
```

Here the leading text means `a` minus signs followed by `b` plus signs.  The
normal form is independent of deletion order: crossing-free matching pairs
each plus with the first still-unmatched minus to its right, and the
unmatched signs are exactly the displayed residual signs.

Consequently `e_i` exists exactly when `a>0` and changes the occurrence
carrying the last residual minus.  After that change, the same occurrence is
the first residual plus, so `f_i` changes it back.  The dual statement proves
`e_i(f_i(w))=w` whenever `f_i(w)` exists.  Thus the paper's rightmost-minus
and leftmost-plus choices are mutually inverse along every colour string.

An unpaired minus exists exactly when the crossing-free matching fails to
match some `i+1` in a prefix.  Therefore all `e_i` are absent exactly when
every prefix has at least as many `i` as `i+1`, for every `i`: these are the
ballot/Yamanouchi words.

The orientation check is not optional.  Under this convention
`e_1(21)=11`; ordinary left-to-right insertion changes shape, whereas RSK of
the reversed words has shape `(2)` at both ends.

## 2. Rank, sinks, and the exact clock

Let `E(w)` be the sum of the letters.  Every nonholding scheduled step is a
single `e_i` edge, hence stays inside one crystal component and replaces
`i+1` by `i`.  Thus

```text
E(F(w)) = E(w)-1
```

on every effective step.  Strict decrease rules out nontrivial directed
cycles.  The holding states are precisely the crystal-highest words, and
each finite type-A component has exactly one such word.  Every orbit
therefore reaches the unique highest word in its starting component.

For reversed-word RSK shape `lambda`, the highest word has content `lambda`
and energy

```text
b(lambda) = sum_i i lambda_i.
```

Since the energy drops by one at every epoch, telescoping gives the exact
pointwise entrance time

```text
tau(w) = E(w)-b(lambda).
```

This proof also shows that the least-colour choice affects the route but not
the length of a raising-only path to the highest vertex.

Now `E(w)<=nk` and `b(lambda)>=n`, so `tau(w)<=n(k-1)`.  Equality forces
`E(w)=nk`, hence every letter is `k`; the word is `k^n`.  Its reversed RSK
shape is `(n)`, its endpoint is `1^n`, and its depth is exactly `n(k-1)`.
This proves sharpness and uniqueness, including `n=1`; for `k=1` the sole
depth is zero.

## 3. Schur layers by branching rather than insertion enumeration

Fix one recording tableau `Q` of shape `lambda`.  Reverse-word RSK identifies
the vertices of that component with semistandard tableaux `P` of shape
`lambda` over `[k]`; the letter energy is the sum of entries of `P`.  The
highest tableau fills row `r` by `r`, so its energy is `b(lambda)`.

For an independent derivation, define

```text
S_lambda^(r)(q) = s_lambda(1,q,...,q^(r-1)).
```

Removing all entries equal to `r` leaves a shape `mu` interlacing `lambda`.
The removed horizontal strip contributes
`q^((r-1)(|lambda|-|mu|))`.  Hence the Gelfand--Tsetlin branching recurrence
is

```text
S_lambda^(r)(q)
  = sum_(mu interlaces lambda)
      q^((r-1)(|lambda|-|mu|)) S_mu^(r-1)(q).
```

The row-filled tableau has exponent
`n(lambda)=sum_(r>=1)(r-1)lambda_r`.  Dividing by that lowest power gives the
component depth polynomial

```text
q^(-n(lambda)) s_lambda(1,q,...,q^(k-1))
 = q^(-b(lambda)) s_lambda(q,q^2,...,q^k).
```

Principal specialization then gives

```text
product_(x in lambda) (1-q^(k+ct(x))) / (1-q^(h(x))).
```

Review B reconstructs the right-hand polynomial without formal quotient
division: factor each `1-q^m` into cyclotomic polynomials and compare the
result with the branching recurrence.  This directly attacks both the
normalizing exponent and possible nonexact cancellation.

The recording tableau `Q` indexes the component.  The number of possible
`Q` is `f^lambda`, equivalently the number of linear extensions of the Young
cell poset.  Summing the component polynomial with that multiplicity proves
the global layer formula and specializes at `q=1` to `k^n`.

## 4. Fixed states and involutions

There is one fixed/highest word per component, so the fixed count is

```text
sum_(lambda partition n, length(lambda)<=k) f^lambda.
```

Under ordinary RSK, an involution has equal insertion and recording tableaux,
and every standard tableau arises this way.  The number of rows is the length
of the longest decreasing subsequence.  The same sum therefore counts
involutions with decreasing-subsequence length at most `k`; once `k>=n` it is
the telephone number with exponential generating function
`exp(z+z^2/2)`.

The reviewer control generates involutions directly as partial matchings,
computes their shapes by matrix growth, and compares each shape count with
Young-poset linear extensions.  It does not scan all permutations.

## 5. Complete reverse-edge classification

Fix a target `y`.  If a nonfixed source `x` maps to `y`, the scheduler chose
some colour `i` and `y=e_i(x)`.  Colour-string inversion forces
`x=f_i(y)`.  Moreover every `e_j(x)` with `j<i` was absent, since otherwise
the scheduler would have chosen a smaller colour.  Thus every nonfixed
source lies in the displayed atlas.

Conversely, suppose `x=f_i(y)` exists and all lower `e_j(x)` are absent.
Then `e_i(x)=y`, and the least available colour at `x` is `i`; hence
`F(x)=y`.  A self-source occurs exactly when the target is highest.  This
proves both directions of the targetwise set identity, including targets
with empty fibres.

Different colours give different source contents, so there are at most
`k-1` distinct lowering sources and at most one self-source.  Therefore every
fibre has size at most `k`; summing fibres counts every carrier word once.

## 6. Equality in the fibre bound

For `k>=2`, a fibre of size `k` must contain the self-source and every one of
the `k-1` colour candidates.  Hence the target is highest with padded content
`lambda`, and `f_i` exists for every `i`.  At a highest vertex this is
equivalent to

```text
lambda_1 > lambda_2 > ... > lambda_k >= 0.
```

The smallest possible size is therefore
`(k-1)+(k-2)+...+1=binom(k,2)`.

Conversely, when `n=binom(k,2)+s`, take the highest word of content

```text
(k-1+s,k-2,...,1,0).
```

All `f_i` exist.  For `j<i-1`, applying `f_i` does not touch the
`j,j+1` signature.  In the `(i-1)` signature it removes one minus and cannot
create an unpaired minus.  Since the target was highest, every lower
`e_j(f_i(y))` remains absent.  All lowerings are therefore scheduler-
admissible, and the self-source supplies the `k`th predecessor.  For `k=1`,
the carrier map is the identity and its sole fibre has size one.

## 7. Proof and evidence boundary

The deductions above establish the mathematical statements conditional on
standard crystal/RSK/Schur facts, all of which receive zero contribution
credit.  The 16,194,669 reviewer assertions are independent falsification
pressure on conventions and boundary cases; they are not proofs or novelty
evidence.  Defant--Williams crystal pop-stack sorting likewise receives zero
credit.  The residual remains the literal one-edge least-current-colour map
together with its labelled inverse atlas, under `OWNER_AMBER / HOLD_EXTERNAL`.
